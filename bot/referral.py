BOT_LINK = "https://t.me/amazon_pricetracker_v0_bot"

FREE_LIMIT = 3

# (min referral count, track limit) checked from most to least generous.
_TIERS = (
    (10, None),
    (3, 50),
    (1, 10),
)


def track_limit(referral_count: int) -> int | None:
    """Max simultaneous tracks allowed for a given number of successful referrals.
    None means unlimited."""
    for threshold, limit in _TIERS:
        if referral_count >= threshold:
            return limit
    return FREE_LIMIT


def referral_link(telegram_id: int) -> str:
    return f"{BOT_LINK}?start={telegram_id}"
