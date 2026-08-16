import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram.ext import Application

from affiliate import with_affiliate_tag
from db import SessionLocal
from models import PriceHistory, Track, User
from scraper import ScrapeError, fetch_product

logger = logging.getLogger(__name__)


async def check_prices(application: Application) -> None:
    session = SessionLocal()
    try:
        tracks = session.query(Track).all()
        for t in tracks:
            try:
                product = await asyncio.to_thread(fetch_product, t.url)
            except ScrapeError as exc:
                logger.warning("Scrape failed for track #%s: %s", t.id, exc)
                continue
            except Exception:
                logger.exception("Unexpected error checking track #%s", t.id)
                continue

            new_price = product["price"]
            old_price = t.last_price
            session.add(PriceHistory(track_id=t.id, price=new_price))

            if new_price != old_price:
                t.last_price = new_price
                session.commit()

                direction = "Baisse" if new_price < old_price else "Hausse"
                link = with_affiliate_tag(t.url)
                text = f"{direction} de prix ! {t.title}\n{old_price:.2f} -> {new_price:.2f}\n{link}"

                user = session.query(User).filter_by(id=t.user_id).first()
                await application.bot.send_message(chat_id=user.chat_id, text=text)
            else:
                session.commit()
    finally:
        session.close()


def start_scheduler(application: Application, interval_minutes: int) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_prices, "interval", minutes=interval_minutes, args=[application])
    scheduler.start()
    return scheduler
