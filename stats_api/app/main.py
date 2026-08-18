import os
from datetime import datetime, timedelta, timezone

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import Depends, FastAPI, Header, HTTPException
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
    UniqueConstraint,
    create_engine,
    func,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]
BOT_STATS_TOKEN = os.environ["BOT_STATS_TOKEN"]

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Read-only mirrors of the bot's own tables (owned by bot/models.py) —
# only the columns this API needs to aggregate.
class BotUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)


class BotTrack(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    last_price = Column(Float)
    currency = Column(String(8))
    created_at = Column(DateTime)


class BotPriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)
    track_id = Column(Integer)
    old_price = Column(Float, nullable=False)
    new_price = Column(Float, nullable=False)
    checked_at = Column(DateTime)


# Owned by this service — new table, doesn't touch the bot's own schema.
class Report(Base):
    __tablename__ = "stats_reports"
    __table_args__ = (UniqueConstraint("period_type", "period_label"),)

    id = Column(Integer, primary_key=True)
    period_type = Column(String(10), nullable=False)  # "monthly" or "yearly"
    period_label = Column(String(20), nullable=False)  # "2026-07" or "2026"
    total_users = Column(Integer, nullable=False)
    new_users = Column(Integer, nullable=False)
    total_tracks = Column(Integer, nullable=False)
    new_tracks = Column(Integer, nullable=False)
    price_drops = Column(Integer, nullable=False)
    price_rises = Column(Integer, nullable=False)
    generated_at = Column(DateTime(timezone=True), server_default=func.now())


Base.metadata.create_all(engine)

app = FastAPI()


def require_token(x_internal_token: str = Header(None)) -> None:
    if x_internal_token != BOT_STATS_TOKEN:
        raise HTTPException(status_code=401, detail="invalid token")


def generate_report(period_type: str, start: datetime, end: datetime, label: str) -> None:
    db = SessionLocal()
    try:
        total_users = db.query(BotUser).filter(BotUser.created_at < end).count()
        new_users = (
            db.query(BotUser)
            .filter(BotUser.created_at >= start, BotUser.created_at < end)
            .count()
        )
        total_tracks = db.query(BotTrack).filter(BotTrack.created_at < end).count()
        new_tracks = (
            db.query(BotTrack)
            .filter(BotTrack.created_at >= start, BotTrack.created_at < end)
            .count()
        )
        price_drops = (
            db.query(BotPriceHistory)
            .filter(
                BotPriceHistory.checked_at >= start,
                BotPriceHistory.checked_at < end,
                BotPriceHistory.new_price < BotPriceHistory.old_price,
            )
            .count()
        )
        price_rises = (
            db.query(BotPriceHistory)
            .filter(
                BotPriceHistory.checked_at >= start,
                BotPriceHistory.checked_at < end,
                BotPriceHistory.new_price > BotPriceHistory.old_price,
            )
            .count()
        )
        db.add(
            Report(
                period_type=period_type,
                period_label=label,
                total_users=total_users,
                new_users=new_users,
                total_tracks=total_tracks,
                new_tracks=new_tracks,
                price_drops=price_drops,
                price_rises=price_rises,
            )
        )
        db.commit()
    except IntegrityError:
        db.rollback()  # report for this period already exists
    finally:
        db.close()


def run_monthly_report() -> None:
    now = datetime.now(timezone.utc)
    this_month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if this_month_start.month == 1:
        prev_month_start = this_month_start.replace(
            year=this_month_start.year - 1, month=12
        )
    else:
        prev_month_start = this_month_start.replace(month=this_month_start.month - 1)
    label = prev_month_start.strftime("%Y-%m")
    generate_report("monthly", prev_month_start, this_month_start, label)


def run_yearly_report() -> None:
    now = datetime.now(timezone.utc)
    this_year_start = now.replace(
        month=1, day=1, hour=0, minute=0, second=0, microsecond=0
    )
    prev_year_start = this_year_start.replace(year=this_year_start.year - 1)
    label = str(prev_year_start.year)
    generate_report("yearly", prev_year_start, this_year_start, label)


scheduler = BackgroundScheduler(timezone="UTC")
scheduler.add_job(run_monthly_report, CronTrigger(day=1, hour=0, minute=5))
scheduler.add_job(run_yearly_report, CronTrigger(month=1, day=1, hour=0, minute=10))
scheduler.start()


@app.get("/stats/live", dependencies=[Depends(require_token)])
def stats_live():
    since = datetime.now(timezone.utc) - timedelta(days=30)
    db = SessionLocal()
    try:
        total_users = db.query(BotUser).count()
        new_users_30d = db.query(BotUser).filter(BotUser.created_at >= since).count()
        total_tracks = db.query(BotTrack).count()
        new_tracks_30d = (
            db.query(BotTrack).filter(BotTrack.created_at >= since).count()
        )
        price_drops_30d = (
            db.query(BotPriceHistory)
            .filter(
                BotPriceHistory.checked_at >= since,
                BotPriceHistory.new_price < BotPriceHistory.old_price,
            )
            .count()
        )
        price_rises_30d = (
            db.query(BotPriceHistory)
            .filter(
                BotPriceHistory.checked_at >= since,
                BotPriceHistory.new_price > BotPriceHistory.old_price,
            )
            .count()
        )
        recent = (
            db.query(BotPriceHistory, BotTrack.title)
            .join(BotTrack, BotTrack.id == BotPriceHistory.track_id)
            .order_by(BotPriceHistory.checked_at.desc())
            .limit(20)
            .all()
        )
        recent_changes = [
            {
                "title": title or "(produit sans titre)",
                "old_price": ph.old_price,
                "new_price": ph.new_price,
                "checked_at": ph.checked_at.isoformat() if ph.checked_at else None,
            }
            for ph, title in recent
        ]
    finally:
        db.close()

    return {
        "total_users": total_users,
        "new_users_30d": new_users_30d,
        "total_tracks": total_tracks,
        "new_tracks_30d": new_tracks_30d,
        "price_drops_30d": price_drops_30d,
        "price_rises_30d": price_rises_30d,
        "recent_changes": recent_changes,
    }


@app.get("/stats/reports", dependencies=[Depends(require_token)])
def stats_reports():
    db = SessionLocal()
    try:
        reports = db.query(Report).order_by(Report.period_label.desc()).all()
    finally:
        db.close()

    def serialize(r: Report) -> dict:
        return {
            "period_label": r.period_label,
            "total_users": r.total_users,
            "new_users": r.new_users,
            "total_tracks": r.total_tracks,
            "new_tracks": r.new_tracks,
            "price_drops": r.price_drops,
            "price_rises": r.price_rises,
        }

    return {
        "monthly": [serialize(r) for r in reports if r.period_type == "monthly"],
        "yearly": [serialize(r) for r in reports if r.period_type == "yearly"],
    }
