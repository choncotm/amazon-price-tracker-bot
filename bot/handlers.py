import asyncio
import logging
from urllib.parse import quote

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from affiliate import with_affiliate_tag
from db import SessionLocal
from i18n import LANGUAGE_NAMES, t
from models import PriceHistory, Track, User
from scraper import ScrapeError, fetch_product

logger = logging.getLogger(__name__)

BOT_LINK = "https://t.me/amazon_pricetracker_v0_bot"
PRIVACY_URL = "https://choncotm.com/amazon-price-tracker/policy"


def _share_dialog_url(lang: str) -> str:
    return f"https://t.me/share/url?url={quote(BOT_LINK)}&text={quote(t('share_caption', lang))}"


def _main_menu(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(t("menu_track", lang), callback_data="menu_track")],
            [InlineKeyboardButton(t("menu_list", lang), callback_data="menu_list")],
            [InlineKeyboardButton(t("menu_history", lang), callback_data="menu_history")],
            [
                InlineKeyboardButton(t("menu_language", lang), callback_data="menu_language"),
                InlineKeyboardButton(t("menu_contact", lang), callback_data="menu_contact"),
            ],
            [
                InlineKeyboardButton(t("menu_share", lang), callback_data="menu_share"),
                InlineKeyboardButton(t("menu_privacy", lang), url=PRIVACY_URL),
            ],
            [InlineKeyboardButton(t("menu_help", lang), callback_data="help")],
        ]
    )


def _with_help_button(lang: str, rows: list | None = None) -> InlineKeyboardMarkup:
    rows = list(rows or [])
    rows.append([InlineKeyboardButton(t("menu_help", lang), callback_data="help")])
    return InlineKeyboardMarkup(rows)


def _product_keyboard(
    lang: str, track_id: int, link: str, include_help: bool = True
) -> InlineKeyboardMarkup:
    rows = [
        [InlineKeyboardButton(t("view_product", lang), url=link)],
        [InlineKeyboardButton(t("history_button", lang), callback_data=f"history:{track_id}")],
        [InlineKeyboardButton(t("delete_product", lang), callback_data=f"untrack:{track_id}")],
    ]
    return _with_help_button(lang, rows) if include_help else InlineKeyboardMarkup(rows)


def _language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(name, callback_data=f"lang:{code}")] for code, name in LANGUAGE_NAMES.items()]
    )


async def _send_product(
    update: Update, text: str, keyboard: InlineKeyboardMarkup, image_url: str | None
) -> None:
    if image_url:
        await update.effective_message.reply_photo(image_url, caption=text, reply_markup=keyboard)
    else:
        await update.effective_message.reply_text(text, reply_markup=keyboard)


def _get_or_create_user(session, update: Update) -> User:
    telegram_id = update.effective_user.id
    chat_id = update.effective_chat.id
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if user is None:
        user = User(telegram_id=telegram_id, chat_id=chat_id)
        session.add(user)
        session.commit()
    return user


def _get_lang(update: Update) -> str:
    session = SessionLocal()
    try:
        return _get_or_create_user(session, update).language
    finally:
        session.close()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    session = SessionLocal()
    try:
        lang = _get_or_create_user(session, update).language
    finally:
        session.close()

    await update.effective_message.reply_text(t("help", lang), reply_markup=_main_menu(lang), parse_mode="HTML")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    lang = _get_lang(update)
    await update.effective_message.reply_text(t("help", lang), reply_markup=_main_menu(lang), parse_mode="HTML")


async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    lang = _get_lang(update)
    await update.effective_message.reply_text(
        t("choose_language", lang), reply_markup=_language_keyboard()
    )


async def on_menu_language_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    lang = _get_lang(update)
    await update.effective_message.reply_text(
        t("choose_language", lang), reply_markup=_language_keyboard()
    )


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    lang = _get_lang(update)
    await update.effective_message.reply_text(
        t("contact_text", lang), reply_markup=_with_help_button(lang)
    )


async def on_menu_contact_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    lang = _get_lang(update)
    await update.effective_message.reply_text(
        t("contact_text", lang), reply_markup=_with_help_button(lang)
    )


async def on_menu_share_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    lang = _get_lang(update)
    keyboard = _with_help_button(
        lang, [[InlineKeyboardButton(t("share_open_button", lang), url=_share_dialog_url(lang))]]
    )
    await update.effective_message.reply_text(t("share_message", lang), reply_markup=keyboard)


async def on_language_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = query.data.split(":", 1)[1]
    if lang not in LANGUAGE_NAMES:
        return

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        user.language = lang
        session.commit()
    finally:
        session.close()

    await query.edit_message_text(t("language_set", lang, name=LANGUAGE_NAMES[lang]))
    await query.message.reply_text(t("help", lang), reply_markup=_main_menu(lang), parse_mode="HTML")


async def _track_url(update: Update, context: ContextTypes.DEFAULT_TYPE, url: str, lang: str) -> None:
    await update.effective_message.reply_text(t("fetching", lang))

    try:
        product = await asyncio.to_thread(fetch_product, url)
    except (ScrapeError, Exception) as exc:
        logger.warning("Scrape failed for %s: %s", url, exc)
        await update.effective_message.reply_text(
            t("scrape_failed", lang), reply_markup=_with_help_button(lang)
        )
        return

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        item = Track(
            user_id=user.id,
            url=product["url"],
            title=product["title"],
            image_url=product.get("image"),
            last_price=product["price"],
            currency="EUR",
        )
        session.add(item)
        session.commit()
        item_id = item.id
    finally:
        session.close()

    link = with_affiliate_tag(product["url"])
    msg = t("product_added", lang, id=item_id, title=product["title"], price=product["price"])
    await _send_product(update, msg, _product_keyboard(lang, item_id, link), product.get("image"))


async def track(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = _get_lang(update)

    if not context.args:
        context.user_data["awaiting_url"] = True
        await update.effective_message.reply_text(
            t("ask_link", lang), reply_markup=_with_help_button(lang)
        )
        return

    context.user_data.pop("awaiting_url", None)
    await _track_url(update, context, context.args[0], lang)


async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.user_data.pop("awaiting_url", False):
        return
    lang = _get_lang(update)
    await _track_url(update, context, update.message.text.strip(), lang)


async def list_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        lang = user.language
        tracks = session.query(Track).filter_by(user_id=user.id).all()
        if not tracks:
            await update.effective_message.reply_text(
                t("list_empty", lang), reply_markup=_with_help_button(lang)
            )
            return

        for track_item in tracks:
            text = t(
                "product_line",
                lang,
                id=track_item.id,
                title=track_item.title,
                price=track_item.last_price,
            )
            link = with_affiliate_tag(track_item.url)
            keyboard = _product_keyboard(lang, track_item.id, link, include_help=False)
            await _send_product(update, text, keyboard, track_item.image_url)

        await update.effective_message.reply_text(
            t("list_end", lang), reply_markup=_with_help_button(lang)
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
    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        lang = user.language

        if not context.args:
            await update.effective_message.reply_text(
                t("untrack_usage", lang), reply_markup=_with_help_button(lang)
            )
            return

        try:
            track_id = int(context.args[0])
        except ValueError:
            await update.effective_message.reply_text(
                t("untrack_invalid_id", lang), reply_markup=_with_help_button(lang)
            )
            return

        title = _delete_track(session, user, track_id)
        if title is None:
            await update.effective_message.reply_text(
                t("untrack_not_found", lang), reply_markup=_with_help_button(lang)
            )
            return
    finally:
        session.close()

    await update.effective_message.reply_text(
        t("untrack_success", lang, id=track_id), reply_markup=_with_help_button(lang)
    )


async def on_untrack_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    track_id = int(query.data.split(":", 1)[1])

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        lang = user.language
        title = _delete_track(session, user, track_id)
    finally:
        session.close()

    chat_id = query.message.chat_id
    try:
        await query.message.delete()
    except Exception:
        logger.exception("Failed to delete product message for track #%s", track_id)

    if title is None:
        text = t("untrack_not_found_button", lang)
    else:
        text = t("untrack_success_button", lang, id=track_id, title=title)

    await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=_with_help_button(lang))


async def on_help_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    lang = _get_lang(update)
    await query.message.reply_text(t("help", lang), reply_markup=_main_menu(lang), parse_mode="HTML")


async def on_menu_track_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    lang = _get_lang(update)
    context.user_data["awaiting_url"] = True
    await update.effective_message.reply_text(
        t("ask_link", lang), reply_markup=_with_help_button(lang)
    )


async def on_menu_list_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    await list_tracks(update, context)


async def _show_history_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        lang = user.language
        tracks = session.query(Track).filter_by(user_id=user.id).all()
    finally:
        session.close()

    if not tracks:
        await update.effective_message.reply_text(
            t("list_empty", lang), reply_markup=_with_help_button(lang)
        )
        return

    rows = [
        [
            InlineKeyboardButton(
                track_item.title[:40], callback_data=f"history:{track_item.id}"
            )
        ]
        for track_item in tracks
    ]
    await update.effective_message.reply_text(
        t("choose_product_history", lang), reply_markup=_with_help_button(lang, rows)
    )


async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop("awaiting_url", None)
    await _show_history_menu(update, context)


async def on_menu_history_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    await _show_history_menu(update, context)


async def on_history_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    track_id = int(query.data.split(":", 1)[1])

    session = SessionLocal()
    try:
        user = _get_or_create_user(session, update)
        lang = user.language
        track_item = session.query(Track).filter_by(id=track_id, user_id=user.id).first()
        if track_item is None:
            await query.message.reply_text(
                t("untrack_not_found_button", lang), reply_markup=_with_help_button(lang)
            )
            return

        title = track_item.title
        history = (
            session.query(PriceHistory)
            .filter_by(track_id=track_id)
            .order_by(PriceHistory.checked_at.asc())
            .all()
        )
        entries = [(h.checked_at, h.old_price, h.new_price) for h in history]
    finally:
        session.close()

    if not entries:
        text = t("history_empty", lang, title=title)
    else:
        lines = [t("history_header", lang, title=title)]
        for checked_at, old_price, new_price in entries:
            sign = "+" if new_price > old_price else "-"
            lines.append(
                t(
                    "history_line",
                    lang,
                    date=checked_at.strftime("%d/%m/%Y %H:%M"),
                    sign=sign,
                    old_price=old_price,
                    new_price=new_price,
                )
            )
        text = "\n".join(lines)

    await query.message.reply_text(text, reply_markup=_with_help_button(lang))
