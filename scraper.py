"""
Domain.com.au pricing scraper (Australia) — hardcoded private seller rates.

Domain.com.au does not publish its pricing publicly (agency rates are negotiated
commercially; private seller rates were sourced from third-party reseller pages
which are no longer reliably accessible via scraping).

Known private seller rates (AUD, per listing, as of 2025):
  - Standard:  $699
  - Premium:   $799
  - Deluxe:    $969

Sources:
  - Domain.com.au private seller portal (requires account)
  - Documented by For Sale By Owner Australia (forsalebyowner.com.au)
  - Corroborated by consumer advocacy coverage (CHOICE, 2024)

fee_period = per_listing
hybrid_note = "private seller rate only; agent pricing negotiated"
location_note = "private seller"

Note: these rates are hardcoded. Manual verification against Domain's private
seller portal is recommended each quarter.
"""

from datetime import date

from config import PLATFORM, MARKET, CURRENCY, CSV_PATH
from storage import append_rows

HYBRID_NOTE = "private seller rate only; agent pricing negotiated"
LOCATION_NOTE = "private seller"

KNOWN_TIERS = [
    {"tier_name": "Standard", "fee_amount": 699},
    {"tier_name": "Premium",  "fee_amount": 799},
    {"tier_name": "Deluxe",   "fee_amount": 969},
]


def main():
    today = date.today().isoformat()
    print("Writing Domain.com.au private seller pricing (hardcoded — source page not scrapeable).")

    rows = [
        {
            "scrape_date":    today,
            "platform":       PLATFORM,
            "market":         MARKET,
            "currency":       CURRENCY,
            "tier_name":      tier["tier_name"],
            "fee_amount":     tier["fee_amount"],
            "fee_period":     "per_listing",
            "prop_value_min": "",
            "prop_value_max": "",
            "location_note":  LOCATION_NOTE,
            "hybrid_note":    HYBRID_NOTE,
        }
        for tier in KNOWN_TIERS
    ]
    append_rows(CSV_PATH, rows)


if __name__ == "__main__":
    main()
