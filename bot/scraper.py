import re

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
}

PRICE_SELECTORS = [
    "#corePrice_feature_div span.a-offscreen",
    "#corePriceDisplay_desktop_feature_div span.a-offscreen",
    "#priceblock_ourprice",
    "#priceblock_dealprice",
    "span.a-price span.a-offscreen",
]

TITLE_SELECTORS = ["#productTitle"]


class ScrapeError(Exception):
    pass


def fetch_product(url: str) -> dict:
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    title = None
    for selector in TITLE_SELECTORS:
        node = soup.select_one(selector)
        if node:
            title = node.get_text(strip=True)
            break

    price = None
    for selector in PRICE_SELECTORS:
        node = soup.select_one(selector)
        if node:
            price = _parse_price(node.get_text(strip=True))
            if price is not None:
                break

    if price is None:
        raise ScrapeError("Could not find a price on the page")

    return {"title": title or url, "price": price}


def _parse_price(raw: str) -> float | None:
    cleaned = re.sub(r"[^\d,.\s\xa0]", "", raw).strip()
    cleaned = cleaned.replace("\xa0", "").replace(" ", "")
    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    elif "," in cleaned:
        cleaned = cleaned.replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None
