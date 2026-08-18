# Amazon Price Tracker Bot

[English](#english) | [Français](#français)

## English

Telegram bot ([@amazon_pricetracker_v0_bot](https://t.me/amazon_pricetracker_v0_bot)) that tracks the price of Amazon products and notifies you when it changes.

Live on [choncotm.com](https://choncotm.com) — see the [privacy policy](https://choncotm.com/amazon-price-tracker/policy/).

### Problem

Amazon prices fluctuate constantly, and manually re-checking whether an item you want has dropped in price is tedious and easy to forget.

### Solution

A Telegram bot: send it an Amazon product link, it tracks the price in the background and pings you on Telegram as soon as it changes.

Runs on an OVH VPS, alongside my other projects (each in its own Docker container).

### How it works

- Send the bot an Amazon product link to start tracking it
- A scheduled job periodically re-scrapes the price (Playwright)
- If the price changes, the bot sends you a Telegram notification
- Product links include an Amazon Associates affiliate tag

### Structure

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

### Stack

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- SQLAlchemy + PostgreSQL
- APScheduler for the periodic price checks
- Playwright for scraping Amazon product pages
- Docker, deployed on an OVH VPS

### Running

```sh
docker compose up -d --build
```

Requires a `.env` file with the bot token and Postgres credentials.

### Stats API

`stats_api/` is a small internal FastAPI service (its own container, `stats-api` in `docker-compose.yml`) that reads this project's own Postgres DB (read-only, via lightweight mirror models — never writes to the bot's own tables) and exposes aggregated stats (including a breakdown of users by language) over HTTP for the choncotm.com admin dashboard, plus weekly, monthly, and yearly report generation (weekly on Monday night, monthly on the night of the 1st of each month, yearly on January 1st).

It's reached from choncotm.com's `stats-api` container over a shared external Docker network (`bot-stats-net`, created once with `docker network create bot-stats-net` and joined by both projects). Every request must include an `X-Internal-Token` header matching the `BOT_STATS_TOKEN` env var (same value in both projects' `.env`).

Required env vars (added to this project's `.env`, alongside the existing ones): `BOT_STATS_TOKEN` (shared secret with choncotm.com).

---

## Français

Bot Telegram ([@amazon_pricetracker_v0_bot](https://t.me/amazon_pricetracker_v0_bot)) qui suit le prix de produits Amazon et te prévient quand il change.

En ligne sur [choncotm.com](https://choncotm.com) — voir la [politique de confidentialité](https://choncotm.com/amazon-price-tracker/policy/).

### Problème

Les prix Amazon fluctuent en permanence, et revérifier manuellement si un article que tu veux a baissé de prix est fastidieux et facile à oublier.

### Solution

Un bot Telegram : tu lui envoies un lien de produit Amazon, il suit le prix en arrière-plan et te notifie sur Telegram dès qu'il change.

Tourne sur un VPS OVH, aux côtés de mes autres projets (chacun dans son propre conteneur Docker).

### Fonctionnement

- Envoie au bot un lien de produit Amazon pour commencer à le suivre
- Une tâche planifiée re-scrape périodiquement le prix (Playwright)
- Si le prix change, le bot t'envoie une notification Telegram
- Les liens produits incluent un tag d'affiliation Amazon Associates

### Structure

```
.
├── bot/
│   ├── main.py           # point d'entrée
│   ├── handlers.py       # gestionnaires de commandes/messages Telegram
│   ├── scraper.py        # scraping des prix Amazon (Playwright)
│   ├── scheduler.py      # tâches périodiques de vérification des prix (APScheduler)
│   ├── affiliate.py      # marquage des liens d'affiliation
│   ├── db.py / models.py # couche base de données (SQLAlchemy)
│   ├── i18n.py           # traductions du bot
│   ├── requirements.txt
│   └── Dockerfile
├── stats_api/             # API de stats interne pour le dashboard admin de choncotm.com (voir plus bas)
└── docker-compose.yml     # bot + PostgreSQL + API de stats
```

### Stack technique

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- SQLAlchemy + PostgreSQL
- APScheduler pour les vérifications de prix périodiques
- Playwright pour scraper les pages produits Amazon
- Docker, déployé sur un VPS OVH

### Lancer

```sh
docker compose up -d --build
```

Nécessite un fichier `.env` avec le token du bot et les identifiants Postgres.

### API de stats

`stats_api/` est un petit service FastAPI interne (son propre conteneur, `stats-api` dans `docker-compose.yml`) qui lit la base Postgres de ce projet (en lecture seule, via des modèles miroirs légers — n'écrit jamais dans les tables du bot) et expose des stats agrégées (dont une répartition des utilisateurs par langue) en HTTP pour le dashboard admin de choncotm.com, plus la génération de rapports hebdomadaires, mensuels et annuels (hebdo le lundi dans la nuit, mensuel la nuit du 1er de chaque mois, annuel le 1er janvier).

Il est accessible depuis le conteneur `stats-api` de choncotm.com via un réseau Docker externe partagé (`bot-stats-net`, créé une fois avec `docker network create bot-stats-net` et rejoint par les deux projets). Chaque requête doit inclure un en-tête `X-Internal-Token` correspondant à la variable d'environnement `BOT_STATS_TOKEN` (même valeur dans les `.env` des deux projets).

Variables d'environnement requises (ajoutées au `.env` de ce projet, en plus des existantes) : `BOT_STATS_TOKEN` (secret partagé avec choncotm.com).
