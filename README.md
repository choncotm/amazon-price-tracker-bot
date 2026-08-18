# Amazon Price Tracker Bot

Telegram bot ([@amazon_pricetracker_v0_bot](https://t.me/amazon_pricetracker_v0_bot)) that tracks the price of Amazon products and notifies you when it changes.

Live on [choncotm.com](https://choncotm.com) — see the [privacy policy](https://choncotm.com/amazon-price-tracker/policy/).

## How it works

- Send the bot an Amazon product link to start tracking it
- A scheduled job periodically re-scrapes the price (Playwright)
- If the price changes, the bot sends you a Telegram notification
- Product links include an Amazon Associates affiliate tag

## Stack

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- SQLAlchemy + PostgreSQL
- APScheduler for the periodic price checks
- Playwright for scraping Amazon product pages

## Structure

- `bot/main.py` — entry point
- `bot/handlers.py` — Telegram command/message handlers
- `bot/scraper.py` — Amazon price scraping
- `bot/scheduler.py` — periodic price-check jobs
- `bot/affiliate.py` — affiliate link tagging
- `bot/db.py`, `bot/models.py` — database layer
- `bot/i18n.py` — bot translations

## Running

```sh
docker compose up -d --build
```

Requires a `.env` file with the bot token and Postgres credentials.
