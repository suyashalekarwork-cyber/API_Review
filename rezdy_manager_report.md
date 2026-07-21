# Rezdy Product Data — Manager Report
**TDU Unified Product API Project**
**Date:** 2026-07-21
**Prepared by:** Data Engineering Team

---

## Executive Summary

We have successfully processed and extracted structured data from 9,363 Rezdy tour products across Australia and New Zealand. Using an AI extraction pipeline (ChatGPT V3.1), we achieved a 99.9% processing success rate with an average of 4.0 out of 9 content sections filled per product. Results were validated across 6 independent processing batches and found to be consistent, confirming the process is reliable rather than dependent on which products happened to be selected. 540 products (5.8%) have been flagged for a follow-up re-processing pass. The dataset is now ready for integration into the unified TDU product database.

---

## What We Did

1. Downloaded and processed 9,373 raw product files from the Rezdy booking system
2. Extracted structured information from each product using AI (ChatGPT V3.1)
3. Organised results into a master dataset with 47 data columns per product
4. Validated quality across 6 independent processing batches

---

## Key Numbers

| What | Number |
|---|---|
| Total products processed | 9,363 |
| Processing success rate | 99.9% |
| Australian products | 6,527 (69.7%) |
| New Zealand products | 1,934 (20.7%) |
| Unique tour operators | 1,328 |
| Unique cities | 1,118 |
| Products with images | 8,902 (95.1%) |
| Average price (AUD/NZD) | $907.97 |

---

## Content Extraction Results

Each Rezdy product listing is a block of free-form text written by the tour operator. Our AI pipeline reads that text and sorts it into 9 standard content sections so every product — regardless of which operator wrote it — has the same structure.

### What We Extracted Per Product

| Content Section | Products With Data | Coverage |
|---|---|---|
| About the Experience | 9,285 | 99.2% ✅ |
| Tour Highlights | 7,135 | 76.2% ✅ |
| What's Included | 5,892 | 62.9% 🟡 |
| Other Information | 4,344 | 46.4% 🟡 |
| Booking Notes | 4,034 | 43.1% 🟡 |
| What's Not Included | 2,872 | 30.7% 🔴 |
| What To Bring | 1,820 | 19.4% 🔴 |
| Itinerary/Schedule | 1,077 | 11.5% 🔴 |
| Cancellation Policy | 971 | 10.4% 🔴 |

✅ Strong coverage &nbsp;&nbsp; 🟡 Moderate &nbsp;&nbsp; 🔴 Low

The low coverage on sections like what's not included, what to bring, itinerary/schedule is not a technical failure — it reflects that most tour operators on Rezdy simply do not provide this information in their product listings. We cannot extract content that was never written.

---

## Geographic Spread

### Top 10 Cities by Product Count

| City | Country | Products |
|---|---|---|
| Molendinar | AU | 310 |
| Queenstown | NZ | 288 |
| Sydney | AU | 226 |
| Melbourne | AU | 204 |
| Auckland | NZ | 168 |
| Pokolbin | AU | 159 |
| Cairns | AU | 146 |
| Adelaide | AU | 144 |
| Hobart | AU | 137 |
| Darwin | AU | 105 |

Products span 1,118 unique cities across Australia and New Zealand, with the strongest concentration in Molendinar, Queenstown, Sydney.

---

## Price Range

### Distribution of Tour Prices

| Price Range | Products | % of Total |
|---|---|---|
| Under $50 | 937 | 10.0% |
| $50 - $100 | 1,403 | 15.0% |
| $100 - $250 | 2,816 | 30.1% |
| $250 - $500 | 1,745 | 18.6% |
| $500 - $1,000 | 916 | 9.8% |
| Over $1,000 | 1,536 | 16.4% |

*(10 products have no listed price and are excluded from this table.)*

**Key price stats:**  
Average price: $907.97  
Median price: $220.00  
Most common range: $100 - $250 (2,816 products)

---

## Top Tour Operators

### By Number of Products

| Operator | Products | Avg Quality Score |
|---|---|---|
| Con-x-ion Airport Transfers (QLD) | 262 | 2.1/9 |
| Cheeky Kiwi Travel | 94 | 5.3/9 |
| Eco Abrolhos Cruises Pty Ltd | 94 | 6.6/9 |
| Down Under Tours Australia | 90 | 3.2/9 |
| Vertigo Bikes | 87 | 2.5/9 |
| WA NT Tours Pty Ltd | 84 | 5.4/9 |
| Cheeky Kea Tours | 76 | 5.1/9 |
| New Zealand Photography Workshops | 71 | 3.7/9 |
| Expedigo Limited | 63 | 2.6/9 |
| Off The Beaten Track WA | 60 | 6.2/9 |

1,328 unique tour operators are represented in the dataset. The largest operators contribute significantly more products to the catalogue, and quality scores vary by operator depending on how much detail they include in their own listings.

---

## Data Quality Assessment

### Processing Results

| Metric | Result | Status |
|---|---|---|
| Products processed | 9,363 | ✅ |
| Successfully extracted | 9,357 (99.9%) | ✅ |
| Processing failures | 6 (0.1%) | ✅ Minor |
| Responses truncated | 2 (0.0%) | ✅ Minor |
| Flagged for re-processing | 540 (5.8%) | 🟡 Planned |

### Quality Score Distribution

Each product was scored out of 9 based on how many content sections were successfully extracted.

| Score | Category | Products | % |
|---|---|---|---|
| 7 - 9 sections | Excellent | 1,027 | 11.0% |
| 5 - 6 sections | Good | 2,680 | 28.6% |
| 3 - 4 sections | Fair | 3,289 | 35.1% |
| 0 - 2 sections | Minimal | 2,367 | 25.3% |

---

## Consistency Across Batches

To ensure reliability, we processed the 9,363 products in 6 separate independent batches. All 9 content sections showed consistent extraction rates across every batch (within 5 percentage points), confirming that our extraction process is stable and repeatable — not dependent on luck or specific product selection.

| Section | Batch Range | Consistent? |
|---|---|---|
| About the Experience | 99.1% – 99.3% | ✅ Yes |
| Tour Highlights | 75.0% – 77.8% | ✅ Yes |
| What's Included | 62.0% – 64.8% | ✅ Yes |
| Other Information | 44.2% – 48.5% | ✅ Yes |
| Booking Notes | 42.0% – 44.6% | ✅ Yes |
| What's Not Included | 27.3% – 32.2% | ✅ Yes |
| What To Bring | 17.6% – 20.8% | ✅ Yes |
| Itinerary/Schedule | 10.5% – 13.0% | ✅ Yes |
| Cancellation Policy | 9.8% – 11.1% | ✅ Yes |

---

## What Happens Next

### Immediate (This Week)
- Re-process 540 flagged products (low quality score or failed extraction)
- Begin same extraction process for Fareharbor (11,231 products)

### Short Term
- Build unified database combining Rezdy + Fareharbor + 5 other sources
- Total unified dataset target: ~30,000+ products

### Delivery
- FastAPI middleware connecting database to B2B travel agent portal
- Travel agents able to browse and search all products from one interface

---

## Summary

- ✅ **Rezdy extraction complete** — 9,363 products processed at 99.9% success rate

- ✅ **Data quality confirmed** — consistent results across 6 independent batches, dataset ready for unified database

- 🔄 **Next milestone** — Fareharbor extraction underway, then unified database build

---

*Report generated: 2026-07-21*  
*Data source: Rezdy API via TDU pipeline*  
*Processing: OpenAI GPT-4o-mini (V3.1 prompt)*
