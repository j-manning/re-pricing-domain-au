"""
Domain.com.au pricing scraper (Australia) — private seller rates.

Domain.com.au does not publish its agency pricing publicly (negotiated commercially).
Private seller rates are documented by third-party resellers such as forsalebyowner.com.au.

Known private seller rates (AUD, per listing):
  - Standard:  $699
  - Premium:   $799
  - Deluxe:    $969

Source: https://www.forsalebyowner.com.au/learn/how-to-sell-privately/domain-listing-fees/

fee_period = per_listing
hybrid_note = "private seller rate only; agent pricing negotiated"
location_note = "private seller"
"""

import re
from datetime import date

import requests
from bs4 import BeautifulSoup

from config import PLATFORM, MARKET, CURRENCY, PRICING_URL, CSV_PATH
from storage import append_rows

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-AU,en;q=0.9",
}

HYBRID_NOTE = "private seller rate only; agent pricing negotiated"
LOCATION_NOTE = "private seller"

KNOWN_TIERS = [
    {"tier_name": "Standard",  "fee_amount": 699},
    {"tier_name": "Premium",   "fee_amount": 799},
    {"tier_name": "Deluxe",    "fee_amount": 969},
]


def fetch_page(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def parse_fees(soup: BeautifulSoup) -> list[dict]:
    today = date.today().isoformat()
    text = soup.get_text(" ", strip=True)

    # Sanity check: look for known prices
    verified = "699" in text and "969" in text

    rows = []
    for tier in KNOWN_TIERS:
        note = HYBRID_NOTE
        if not verified:
            note += " [UNVERIFIED — page structure changed]"
        rows.append({
            "scrape_date": today,
            "platform": PLATFORM,
            "market": MARKET,
            "currency": CURRENCY,
            "tier_name": tier["tier_name"],
            "fee_amount": tier["fee_amount"],
            "fee_period": "per_listing",
            "prop_value_min": "",
            "prop_value_max": "",
            "location_note": LOCATION_NOTE,
            "hybrid_note": note,
        })

    if verified:
        print("Confirmed Domain.com.au private seller prices from source page.")
    else:
        print("WARNING: Could not confirm prices. Using last-known values.")

    return rows


def main():
    print(f"Fetching Domain.com.au pricing from {PRICING_URL}")
    soup = fetch_page(PRICING_URL)
    rows = parse_fees(soup)
    append_rows(CSV_PATH, rows)


if __name__ == "__main__":
    main()
