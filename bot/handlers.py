import asyncio
import logging

from telegram import Update
from telegram.ext import ContextTypes

from affiliate import with_affiliate_tag
from db import SessionLocal
from models import Track, User
from scraper import ScrapeError, fetch_product

logger = logging.getLogger(__name__)


def _get_or_create_user(session, update: Update) -> User:
    telegram_id = update.effective_user.id
    chat_id = update.effective_chat.id
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if user is None:
        user = User(telegram_id=telegram_id, chat_id=chat_id)
        session.add(user)
        session.commit()
    return user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    session = SessionLocal()
    try:
        _get_or_create_user(session, update)
    finally:
        session.close()

    await update.message.reply_text(
        "Salut ! Je surveille des prix Amazon.\n\n"
        "/track <url> - suivre un produit\n"
        "/list - voir mes produits suivis\n"
        "/untrack <id> - arrêter de suivre un produit\n"
        "/help - afficher cette aide"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


async def track(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage : /track <url_amazon>")
        return

    url = context.args[0]

    await update.message.reply_text("Récupération du prix en cours...")

    try:
        product = await asyncio.to_thread(fetch_product, url)
    except (ScrapeError, Exception) as exc:
        logger.warning("Scrape failed for %s: %s", url, exc)
        await update.message.reply_text(
            "Je n'ai pas réussi à récupérer le prix de ce produit. Vérifie le lien."
        )
        return

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        item = Track(
            user_id=user.id,
            url=product["url"],
            title=product["title"],
            last_price=product["price"],
            currency="EUR",
        )
        session.add(item)
        session.commit()
        item_id = item.id
    finally:
        session.close()

    link = with_affiliate_tag(product["url"])
    msg = (
        f"Produit ajouté (#{item_id}) : {product['title']}\n"
        f"Prix actuel : {product['price']:.2f}\n{link}"
    )
    await update.message.reply_text(msg)


async def list_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        tracks = session.query(Track).filter_by(user_id=user.id).all()
        if not tracks:
            await update.message.reply_text("Tu ne suis aucun produit pour l'instant.")
            return

        lines = [f"#{t.id} - {t.title} - {t.last_price:.2f}" for t in tracks]
        await update.message.reply_text("\n".join(lines))
    finally:
        session.close()


async def untrack(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("Usage : /untrack <id>")
        return

    try:
        track_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("L'id doit être un nombre.")
        return

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        item = session.query(Track).filter_by(id=track_id, user_id=user.id).first()
        if item is None:
            await update.message.reply_text("Produit introuvable.")
            return
        session.delete(item)
        session.commit()
    finally:
        session.close()

    await update.message.reply_text(f"Produit #{track_id} supprimé.")
