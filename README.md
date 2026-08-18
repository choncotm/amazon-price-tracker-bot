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
├── stats_api/             # internal stats API for the choncotm.com admin dashboard (see below)
└── docker-compose.yml     # bot + PostgreSQL + stats API
```

## Stack

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- SQLAlchemy + PostgreSQL
- APScheduler for the periodic price checks
- Playwright for scraping Amazon product pages
- Docker, deployed on an OVH VPS

## Running

```sh
docker compose up -d --build
```

Requires a `.env` file with the bot token and Postgres credentials.

## Stats API

`stats_api/` is a small internal FastAPI service (its own container,
`stats-api` in `docker-compose.yml`) that reads this project's own
Postgres DB (read-only, via lightweight mirror models — never writes to
the bot's own tables) and exposes aggregated stats over HTTP for the
choncotm.com admin dashboard, plus monthly/yearly report generation
(same schedule as choncotm.com's own site-stats reports: night of the
1st of each month, and January 1st).

It's reached from choncotm.com's `stats-api` container over a shared
external Docker network (`bot-stats-net`, created once with `docker
network create bot-stats-net` and joined by both projects). Every
request must include an `X-Internal-Token` header matching the
`BOT_STATS_TOKEN` env var (same value in both projects' `.env`).

Required env vars (added to this project's `.env`, alongside the
existing ones): `BOT_STATS_TOKEN` (shared secret with choncotm.com).
