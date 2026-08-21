import hashlib
import hmac
import os
import time
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from fastapi import Body, Depends, FastAPI, HTTPException, Request, Response
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import Session, declarative_base, sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
WEBAPP_SESSION_SECRET = os.environ["WEBAPP_SESSION_SECRET"]

COOKIE_NAME = "webapp_session"
SESSION_MAX_AGE = 60 * 60 * 24 * 30  # 30 days
LANGUAGE_CODES = {"fr", "en", "es", "de", "pt", "ru"}

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
serializer = URLSafeTimedSerializer(WEBAPP_SESSION_SECRET)


# Writable mirrors of the bot's own tables (owned by bot/models.py) — kept as a
# separate service like stats_api, so no cross-container Python import.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    chat_id = Column(BigInteger, nullable=False)
    language = Column(String(8), nullable=False, default="en")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    url = Column(Text, nullable=False)
    title = Column(Text)
    image_url = Column(Text)
    last_price = Column(Float)
    currency = Column(String(8), default="EUR")


class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False)
    old_price = Column(Float, nullable=False)
    new_price = Column(Float, nullable=False)
    checked_at = Column(DateTime)


def with_affiliate_tag(url: str) -> str:
    tag = os.environ.get("AMAZON_ASSOCIATE_TAG")
    if not tag:
        return url
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query))
    query["tag"] = tag
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def verify_telegram_auth(data: dict) -> int:
    """Verifies a Telegram Login Widget payload and returns the Telegram user id.

    Algorithm: https://core.telegram.org/widgets/login#checking-authorization
    """
    data = dict(data)
    check_hash = data.pop("hash", None)
    if not check_hash:
        raise HTTPException(status_code=400, detail="Missing hash")

    auth_date = data.get("auth_date")
    if not auth_date or time.time() - int(auth_date) > 86400:
        raise HTTPException(status_code=400, detail="Stale login data")

    data_check_string = "\n".join(f"{k}={data[k]}" for k in sorted(data))
    secret_key = hashlib.sha256(TELEGRAM_BOT_TOKEN.encode()).digest()
    computed_hash = hmac.new(
        secret_key, data_check_string.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(computed_hash, check_hash):
        raise HTTPException(status_code=401, detail="Invalid Telegram signature")

    return int(data["id"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def require_user(request: Request, db: Session = Depends(get_db)) -> User:
    cookie = request.cookies.get(COOKIE_NAME)
    if not cookie:
        raise HTTPException(status_code=401, detail="Not logged in")
    try:
        telegram_id = serializer.loads(cookie, max_age=SESSION_MAX_AGE)
    except (BadSignature, SignatureExpired):
        raise HTTPException(status_code=401, detail="Session expired")

    user = db.query(User).filter_by(telegram_id=telegram_id).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Unknown user")
    return user


app = FastAPI()


@app.post("/auth/telegram")
def auth_telegram(response: Response, payload: dict = Body(...), db: Session = Depends(get_db)):
    telegram_id = verify_telegram_auth(payload)

    user = db.query(User).filter_by(telegram_id=telegram_id).first()
    if user is None:
        # Private-chat ids equal the user's own Telegram id, so this matches
        # what the bot itself would create on a first /start.
        user = User(telegram_id=telegram_id, chat_id=telegram_id)
        db.add(user)
        db.commit()

    token = serializer.dumps(telegram_id)
    response.set_cookie(
        COOKIE_NAME,
        token,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=SESSION_MAX_AGE,
    )
    return {"ok": True, "language": user.language}


@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(COOKIE_NAME)
    return {"ok": True}


@app.get("/me")
def me(user: User = Depends(require_user)):
    return {"telegram_id": user.telegram_id, "language": user.language}


@app.get("/products")
def list_products(user: User = Depends(require_user), db: Session = Depends(get_db)):
    tracks = db.query(Track).filter_by(user_id=user.id).all()
    return [
        {
            "id": t.id,
            "title": t.title,
            "price": t.last_price,
            "currency": t.currency,
            "image_url": t.image_url,
            "link": with_affiliate_tag(t.url),
        }
        for t in tracks
    ]


@app.delete("/products/{track_id}")
def delete_product(track_id: int, user: User = Depends(require_user), db: Session = Depends(get_db)):
    track = db.query(Track).filter_by(id=track_id, user_id=user.id).first()
    if track is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(track)
    db.commit()
    return {"ok": True}


@app.get("/products/{track_id}/history")
def product_history(track_id: int, user: User = Depends(require_user), db: Session = Depends(get_db)):
    track = db.query(Track).filter_by(id=track_id, user_id=user.id).first()
    if track is None:
        raise HTTPException(status_code=404, detail="Product not found")

    history = (
        db.query(PriceHistory)
        .filter_by(track_id=track_id)
        .order_by(PriceHistory.checked_at.asc())
        .all()
    )
    return {
        "title": track.title,
        "history": [
            {
                "checked_at": h.checked_at.isoformat() if h.checked_at else None,
                "old_price": h.old_price,
                "new_price": h.new_price,
            }
            for h in history
        ],
    }


@app.post("/language")
def set_language(
    payload: dict = Body(...), user: User = Depends(require_user), db: Session = Depends(get_db)
):
    language = payload.get("language")
    if language not in LANGUAGE_CODES:
        raise HTTPException(status_code=400, detail="Unknown language")
    user.language = language
    db.commit()
    return {"ok": True, "language": language}
