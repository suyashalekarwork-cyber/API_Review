# AI Placement-Accuracy Checker — gpt55raw (50 products)

Scope: **placement only** — does each extracted field's text belong under
that field name? This does NOT check faithfulness to the raw text and does
NOT look for content dropped entirely, so the score below is a placement
accuracy figure, not an overall extraction-quality score.

Judge: single model `gpt-5.6-terra` — its verdict stands alone (no vote, so no DISPUTED category and no cross-check on outliers).

## Human-review bands (per product)

| band | score | action | products | % | fields |
|---|---|---|---|---|---|
| **NO_HUMAN_NEEDED** | 80-100 | No human needed — ship as-is | 19 | 38.0% | 224 |
| **MAYBE_REVIEW** | 70-79.9 | Maybe — spot-check | 16 | 32.0% | 232 |
| **HIGHLY_RECOMMENDED** | 0-69.9 | Human review highly recommended | 15 | 30.0% | 151 |

- Fields judged: **607** across 50 products
- Placement accuracy: **74.5%** (452 CORRECT)
- WRONG_FIELD: 149
- GARBLED: 6
- DISPUTED (no majority): 0
- NO_VOTE (no model returned a verdict): 0

## Most-flagged fields

| field | flagged | judged | flag rate |
|---|---|---|---|
| `redo_desc_requirements` | 17 | 34 | 50% |
| `redo_desc_about` | 17 | 49 | 35% |
| `redo_desc_check_in` | 15 | 26 | 58% |
| `redo_booking_contact` | 14 | 29 | 48% |
| `redo_desc_other` | 14 | 31 | 45% |
| `redo_booking_other` | 13 | 20 | 65% |
| `redo_booking_what_to_bring` | 8 | 34 | 24% |
| `redo_booking_important_info` | 7 | 20 | 35% |
| `redo_booking_location` | 6 | 22 | 27% |
| `redo_desc_itinerary` | 6 | 24 | 25% |
| `redo_desc_what_excluded` | 5 | 22 | 23% |
| `redo_desc_highlights` | 4 | 15 | 27% |
| `redo_meeting_point` | 4 | 30 | 13% |
| `redo_booking_before_arrival` | 4 | 16 | 25% |
| `redo_desc_what_included` | 4 | 39 | 10% |
| `redo_booking_check_in` | 3 | 14 | 21% |
| `redo_booking_what_not_to_bring` | 3 | 13 | 23% |
| `redo_desc_duration_text` | 3 | 44 | 7% |
| `redo_desc_what_to_bring` | 2 | 29 | 7% |
| `redo_booking_departure_info` | 2 | 31 | 6% |
| `redo_booking_itinerary` | 1 | 4 | 25% |
| `redo_booking_inclusions` | 1 | 10 | 10% |
| `redo_booking_cancellation` | 1 | 9 | 11% |
| `redo_desc_cancellation` | 1 | 19 | 5% |

## Model agreement with the majority

| model | verdicts | matched majority | parse failures | flag rate |
|---|---|---|---|---|
| gpt-5.6-terra | 607 | 100.0% | 0 | 25.5% |
