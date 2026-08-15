import re

from playwright.sync_api import sync_playwright

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

PRICE_SELECTORS = [
    "#corePrice_feature_div span.a-offscreen",
    "#corePriceDisplay_desktop_feature_div span.a-offscreen",
    "#priceblock_ourprice",
    "#priceblock_dealprice",
    "span.a-price span.a-offscreen",
]

TITLE_SELECTOR = "#productTitle"


class ScrapeError(Exception):
    pass


def fetch_product(url: str) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True, args=["--disable-blink-features=AutomationControlled"]
        )
        try:
            context = browser.new_context(
                user_agent=USER_AGENT,
                locale="fr-FR",
                viewport={"width": 1280, "height": 800},
            )
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(1500)

            title_el = page.query_selector(TITLE_SELECTOR)
            title = title_el.inner_text().strip() if title_el else None

            price = None
            for selector in PRICE_SELECTORS:
                el = page.query_selector(selector)
                if el:
                    price = _parse_price(el.inner_text())
                    if price is not None:
                        break
        finally:
            browser.close()

    if price is None:
        raise ScrapeError("Could not find a price on the page")

    return {"title": title or url, "price": price}


def _parse_price(raw: str) -> float | None:
    cleaned = re.sub(r"[^\d,.]", "", raw)
    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    elif "," in cleaned:
        cleaned = cleaned.replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None
