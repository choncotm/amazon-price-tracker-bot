# Amazon Price Tracker Bot

Telegram bot ([@amazon_pricetracker_v0_bot](https://t.me/amazon_pricetracker_v0_bot)) that tracks the price of Amazon products and notifies you when it changes.

Live on [choncotm.com](https://choncotm.com) — see the [privacy policy](https://choncotm.com/amazon-price-tracker/policy/).

## Problem

Amazon prices fluctuate constantly, and manually re-checking whether an item you want has dropped in price is tedious and easy to forget.

## Solution

A Telegram bot: send it an Amazon product link, it tracks the price in the background and pings you on Telegram as soon as it changes.

Runs on an OVH VPS, alongside my other projects (each in its own Docker container).

## How it works

- Send the bot an Amazon product link to start tracking it
- A scheduled job periodically re-scrapes the price (Playwright)
- If the price changes, the bot sends you a Telegram notification
- Product links include an Amazon Associates affiliate tag

## Structure

```
.
├── bot/
│   ├── main.py           # entry point
│   ├── handlers.py       # Telegram command/message handlers
│   ├── scraper.py        # Amazon price scraping (Playwright)
│   ├── scheduler.py      # periodic price-check jobs (APScheduler)
│   ├── affiliate.py      # affiliate link tagging
│   ├── db.py / models.py # database layer (SQLAlchemy)
│   ├── i18n.py           # bot translations
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml     # bot + PostgreSQL
```

## Stack

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- SQLAlchemy + PostgreSQL
- APScheduler for the periodic price checks
- Playwright for scraping Amazon product pages

## Running

```sh
docker compose up -d --build
```

Requires a `.env` file with the bot token and Postgres credentials.
