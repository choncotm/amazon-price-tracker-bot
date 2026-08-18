# amazon-price-tracker-bot

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