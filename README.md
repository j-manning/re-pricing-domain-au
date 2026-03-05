# re-pricing-domain-au

Weekly scraper for **Domain.com.au** listing fees (Australia) — private seller rates.

## Platform

Domain.com.au is Australia's second-largest real estate portal (behind REA Group / realestate.com.au).

## Pricing Model

Domain does not publish agency pricing publicly (negotiated commercially per agency).
Private seller rates are documented by third-party resellers.

| Tier | Fee (AUD) |
|------|-----------|
| Standard | $699 |
| Premium | $799 |
| Deluxe | $969 |

- `fee_period = per_listing`
- `currency = AUD`
- `location_note = private seller`
- `hybrid_note = "private seller rate only; agent pricing negotiated"`

Source: [For Sale By Owner — Domain listing fees](https://www.forsalebyowner.com.au/learn/how-to-sell-privately/domain-listing-fees/)

## Notes on REA Group (realestate.com.au)

REA Group pricing is not publicly available. Estimates from competition authority proceedings
suggest AUD $2,500–$5,000+ per listing in premium suburbs. See `data/notes.md`.

## Output

`data/pricing.csv` — 3 rows per scrape date (private seller tiers only).

## Running Locally

```bash
pip install -r requirements.txt
python scraper.py
```
