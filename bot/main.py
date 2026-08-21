import logging
import os

from dotenv import load_dotenv
from sqlalchemy import text
from telegram import BotCommand, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import handlers
from db import Base, SessionLocal, engine
from i18n import t
from models import User
from scheduler import start_scheduler

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def post_init(application: Application) -> None:
    await application.bot.set_my_name("Amazon Price Tracker")
    await application.bot.set_my_short_description(
        "Tracks Amazon product prices and alerts you the moment they drop. "
        "Free, fast, no manual checking needed."
    )
    await application.bot.set_my_description(
        "Send me an Amazon product link and I'll track its price for you.\n\n"
        "I'll notify you here the moment the price changes — no more manual "
        "checking.\n\n"
        "Commands: /track /list /untrack /history /language /help\n\n"
        f"Privacy policy: {handlers.PRIVACY_URL}"
    )

    await application.bot.set_my_commands(
        [
            BotCommand("start", "Start the bot"),
            BotCommand("track", "Track an Amazon product"),
            BotCommand("list", "View your tracked products"),
            BotCommand("untrack", "Stop tracking a product"),
            BotCommand("history", "Price history for a product"),
            BotCommand("language", "Change language"),
            BotCommand("help", "Show help"),
        ]
    )
    await application.bot.set_my_commands(
        [
            BotCommand("start", "Démarrer le bot"),
            BotCommand("track", "Suivre un produit Amazon"),
            BotCommand("list", "Voir mes produits suivis"),
            BotCommand("untrack", "Arrêter de suivre un produit"),
            BotCommand("history", "Historique des prix d'un produit"),
            BotCommand("language", "Changer de langue"),
            BotCommand("help", "Afficher l'aide"),
        ],
        language_code="fr",
    )

    interval = int(os.environ.get("CHECK_INTERVAL_MINUTES", "60"))
    start_scheduler(application, interval)
    logger.info("Scheduler started, checking prices every %s minutes", interval)


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Unhandled error while processing update", exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        lang = "en"
        if update.effective_user:
            session = SessionLocal()
            try:
                user = (
                    session.query(User)
                    .filter_by(telegram_id=update.effective_user.id)
                    .first()
                )
                if user:
                    lang = user.language
            finally:
                session.close()
        try:
            await update.effective_message.reply_text(t("error", lang))
        except Exception:
            logger.exception("Failed to notify user about the error")


def _migrate(engine) -> None:
    """Adds columns introduced after the initial schema. create_all() only
    creates missing tables, never alters existing ones, so this covers the gap
    for a project without a migration tool."""
    with engine.begin() as conn:
        conn.execute(
            text(
                "ALTER TABLE users ADD COLUMN IF NOT EXISTS "
                "referred_by_id INTEGER REFERENCES users(id)"
            )
        )


def main() -> None:
    Base.metadata.create_all(engine)
    _migrate(engine)

    token = os.environ["TELEGRAM_BOT_TOKEN"]
    application = (
        Application.builder()
        .token(token)
        .connect_timeout(20)
        .read_timeout(20)
        .write_timeout(20)
        .pool_timeout(20)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", handlers.start))
    application.add_handler(CommandHandler("help", handlers.help_command))
    application.add_handler(CommandHandler("track", handlers.track))
    application.add_handler(CommandHandler("list", handlers.list_tracks))
    application.add_handler(CommandHandler("untrack", handlers.untrack))
    application.add_handler(CommandHandler("history", handlers.history_command))
    application.add_handler(CommandHandler("language", handlers.language_command))
    application.add_handler(
        CallbackQueryHandler(handlers.on_untrack_button, pattern=r"^untrack:\d+$")
    )
    application.add_handler(
        CallbackQueryHandler(handlers.on_history_button, pattern=r"^history:\d+$")
    )
    application.add_handler(CallbackQueryHandler(handlers.on_help_button, pattern=r"^help$"))
    application.add_handler(
        CallbackQueryHandler(handlers.on_menu_track_button, pattern=r"^menu_track$")
    )
    application.add_handler(
        CallbackQueryHandler(handlers.on_menu_list_button, pattern=r"^menu_list$")
    )
    application.add_handler(
        CallbackQueryHandler(handlers.on_menu_history_button, pattern=r"^menu_history$")
    )
    application.add_handler(
        CallbackQueryHandler(handlers.on_menu_language_button, pattern=r"^menu_language$")
    )
    application.add_handler(
        CallbackQueryHandler(handlers.on_menu_share_button, pattern=r"^menu_share$")
    )
    application.add_handler(
        CallbackQueryHandler(handlers.on_menu_contact_button, pattern=r"^menu_contact$")
    )
    application.add_handler(
        CallbackQueryHandler(handlers.on_language_button, pattern=r"^lang:(fr|en|es|de|pt|ru)$")
    )
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.on_text))
    application.add_handler(
        ChatMemberHandler(handlers.on_my_chat_member, ChatMemberHandler.MY_CHAT_MEMBER)
    )
    application.add_error_handler(on_error)

    application.run_polling()


if __name__ == "__main__":
    main()
