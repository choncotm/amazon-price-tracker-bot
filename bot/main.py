import logging
import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

import handlers
from db import Base, engine
from scheduler import start_scheduler

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def post_init(application: Application) -> None:
    interval = int(os.environ.get("CHECK_INTERVAL_MINUTES", "60"))
    start_scheduler(application, interval)
    logger.info("Scheduler started, checking prices every %s minutes", interval)


def main() -> None:
    Base.metadata.create_all(engine)

    token = os.environ["TELEGRAM_BOT_TOKEN"]
    application = Application.builder().token(token).post_init(post_init).build()

    application.add_handler(CommandHandler("start", handlers.start))
    application.add_handler(CommandHandler("help", handlers.help_command))
    application.add_handler(CommandHandler("track", handlers.track))
    application.add_handler(CommandHandler("list", handlers.list_tracks))
    application.add_handler(CommandHandler("untrack", handlers.untrack))

    application.run_polling()


if __name__ == "__main__":
    main()
