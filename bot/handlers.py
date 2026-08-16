import asyncio
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from affiliate import with_affiliate_tag
from db import SessionLocal
from models import Track, User
from scraper import ScrapeError, fetch_product

logger = logging.getLogger(__name__)

WELCOME_TEXT = "Salut ! Utilise les boutons ci-dessous 👇"

HELP_TEXT = (
    "Salut ! Je surveille des prix Amazon.\n\n"
    "/track <url> - suivre un produit\n"
    "/list - voir mes produits suivis\n"
    "/untrack <id> - arrêter de suivre un produit\n\n"
    "/help - afficher cette aide"
)


def _main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🔍 Suivre un produit", callback_data="menu_track")],
            [InlineKeyboardButton("📋 Mes produits", callback_data="menu_list")],
            [InlineKeyboardButton("❓ Aide", callback_data="help")],
        ]
    )


def _with_help_button(rows: list | None = None) -> InlineKeyboardMarkup:
    rows = list(rows or [])
    rows.append([InlineKeyboardButton("❓ Aide", callback_data="help")])
    return InlineKeyboardMarkup(rows)


def _product_keyboard(track_id: int, link: str, include_help: bool = True) -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton("Voir le produit", url=link)],
        [InlineKeyboardButton("🗑 Supprimer ❌", callback_data=f"untrack:{track_id}")],
    ]
    return _with_help_button(rows) if include_help else InlineKeyboardMarkup(rows)


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
    context.user_data.pop("awaiting_url", None)
    session = SessionLocal()
    try:
        _get_or_create_user(session, update)
    finally:
        session.close()

    await update.effective_message.reply_text(WELCOME_TEXT, reply_markup=_main_menu())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    await update.effective_message.reply_text(HELP_TEXT, reply_markup=_main_menu())


async def _track_url(update: Update, context: ContextTypes.DEFAULT_TYPE, url: str) -> None:
    await update.effective_message.reply_text("Récupération du prix en cours...")

    try:
        product = await asyncio.to_thread(fetch_product, url)
    except (ScrapeError, Exception) as exc:
        logger.warning("Scrape failed for %s: %s", url, exc)
        await update.effective_message.reply_text(
            "Je n'ai pas réussi à récupérer le prix de ce produit. Vérifie le lien.",
            reply_markup=_with_help_button(),
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
    msg = f"Produit ajouté (#{item_id}) : {product['title']}\nPrix actuel : {product['price']:.2f}"
    await update.effective_message.reply_text(msg, reply_markup=_product_keyboard(item_id, link))


async def track(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        context.user_data["awaiting_url"] = True
        await update.effective_message.reply_text(
            "📋 Colle le lien du produit Amazon à suivre ci-dessous.",
            reply_markup=_with_help_button(),
        )
        return

    context.user_data.pop("awaiting_url", None)
    await _track_url(update, context, context.args[0])


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.user_data.pop("awaiting_url", False):
        return
    await _track_url(update, context, update.message.text.strip())


async def list_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        tracks = session.query(Track).filter_by(user_id=user.id).all()
        if not tracks:
            await update.effective_message.reply_text(
                "Tu ne suis aucun produit pour l'instant.", reply_markup=_with_help_button()
            )
            return

        for t in tracks:
            text = f"#{t.id} - {t.title}\nPrix actuel : {t.last_price:.2f}"
            link = with_affiliate_tag(t.url)
            await update.effective_message.reply_text(
                text, reply_markup=_product_keyboard(t.id, link, include_help=False)
            )

        await update.effective_message.reply_text(
            "Fin de la liste.", reply_markup=_with_help_button()
        )
    finally:
        session.close()


def _delete_track(session, user: User, track_id: int) -> str | None:
    item = session.query(Track).filter_by(id=track_id, user_id=user.id).first()
    if item is None:
        return None
    title = item.title
    session.delete(item)
    session.commit()
    return title


async def untrack(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    if not context.args:
        await update.effective_message.reply_text(
            "Usage : /untrack <id>", reply_markup=_with_help_button()
        )
        return

    try:
        track_id = int(context.args[0])
    except ValueError:
        await update.effective_message.reply_text(
            "L'id doit être un nombre.", reply_markup=_with_help_button()
        )
        return

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        title = _delete_track(session, user, track_id)
        if title is None:
            await update.effective_message.reply_text(
                "Produit introuvable.", reply_markup=_with_help_button()
            )
            return
    finally:
        session.close()

    await update.effective_message.reply_text(
        f"Produit #{track_id} supprimé.", reply_markup=_with_help_button()
    )


async def on_untrack_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    track_id = int(query.data.split(":", 1)[1])

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        title = _delete_track(session, user, track_id)
        if title is None:
            await query.edit_message_text(
                "Produit introuvable ou déjà supprimé.", reply_markup=_with_help_button()
            )
            return
    finally:
        session.close()

    await query.edit_message_text(
        f"Produit #{track_id} supprimé : {title}", reply_markup=_with_help_button()
    )


async def on_help_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(HELP_TEXT, reply_markup=_main_menu())


async def on_menu_track_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    context.user_data["awaiting_url"] = True
    await update.effective_message.reply_text(
        "📋 Colle le lien du produit Amazon à suivre ci-dessous.",
        reply_markup=_with_help_button(),
    )


async def on_menu_list_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    await list_tracks(update, context)
