import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application

from affiliate import with_affiliate_tag
from db import SessionLocal
from i18n import t
from models import PriceHistory, Track, User
from scraper import ScrapeError, fetch_product

logger = logging.getLogger(__name__)


async def check_prices(application: Application) -> None:
    session = SessionLocal()
    try:
        tracks = session.query(Track).all()
        for track_item in tracks:
            try:
                product = await asyncio.to_thread(fetch_product, track_item.url)
            except ScrapeError as exc:
                logger.warning("Scrape failed for track #%s: %s", track_item.id, exc)
                continue
            except Exception:
                logger.exception("Unexpected error checking track #%s", track_item.id)
                continue

            new_price = product["price"]
            old_price = track_item.last_price

            if new_price == old_price:
                continue

            session.add(
                PriceHistory(track_id=track_item.id, old_price=old_price, new_price=new_price)
            )
            track_item.last_price = new_price
            session.commit()

            user = session.query(User).filter_by(id=track_item.user_id).first()
            lang = user.language
            direction = t("price_drop", lang) if new_price < old_price else t("price_rise", lang)
            link = with_affiliate_tag(track_item.url)
            text = t(
                "price_alert",
                lang,
                direction=direction,
                title=track_item.title,
                old_price=old_price,
                new_price=new_price,
            )
            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(t("view_product", lang), url=link)],
                    [
                        InlineKeyboardButton(
                            t("delete_product", lang), callback_data=f"untrack:{track_item.id}"
                        )
                    ],
                    [InlineKeyboardButton(t("back_button", lang), callback_data="help")],
                ]
            )

            await application.bot.send_message(
                chat_id=user.chat_id, text=text, reply_markup=keyboard
            )
    finally:
        session.close()


def start_scheduler(application: Application, interval_minutes: int) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_prices, "interval", minutes=interval_minutes, args=[application])
    scheduler.start()
    return scheduler
