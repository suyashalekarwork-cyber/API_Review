# gpt-5.5-pro — 50 Products, Raw Extraction, No Paste Fix

Prompt V4.4, unchanged. No paste fix, no judge. This measures the model's
unassisted extraction on the hardest products we have, plus inputs larger than
anything it has previously been tested on.

## 1. Why these 50

Deliberately **not** a representative sample — a proportional draw would be
mostly easy products and would stress nothing.

**Group A — 35 products from inside the 500-run.** These have an existing
gpt-4o-mini extraction, so the workbook gets a real before/after at zero extra
cost (gpt-4o-mini was **not** re-run; values are read from disk).

| Bucket | n | Avg words | gpt-4o-mini placement |
|---|---|---|---|
| worst_placement | 10 | 309 | **26.1%** |
| most_wrong_fields | 8 | 545 | 55.8% |
| longest_in_500 | 8 | 634 | 72.3% |
| long_and_broken | 6 | 559 | 57.0% |
| clean_control | 3 | 294 | 85.5% |

**Group B — 15 products from outside the 500-run, 651-1,200 words.** The
500-run was stratified with a **650-word cap**, so 650 words was the largest
input gpt-5.5-pro had ever seen. 1,433 untested products sit in this band.

Extremes were excluded on purpose: 1,772 products exceed 650 words and the
largest is 4,458, but a 4,000-word input risks hitting the 8,000-token output
ceiling, and truncated output would look exactly like content loss. The
651-1,200 band is 1.7x bigger than anything previously tested while staying
clear of that confound.

## 2. Batch execution

| Metric | Value |
|---|---|
| Requests | **89/89 completed, 0 failed** |
| Wall clock | 819s (~14 min) |
| Prompt tokens | 335,261 |
| Completion tokens | 120,402 |
| Cost | **N/A — pricing not confirmed** on this account |
| Truncated responses | **0** |

11 sides were deliberately not sent: 10 products have no booking notes and one
has no description. Sending empty messages wastes calls and invites invented
content, so those sides were skipped and treated as empty fields.

## 3. HEADLINE — coverage by bucket

| Group / bucket | n | Avg words | Coverage | Missing | Partial |
|---|---|---|---|---|---|
| worst_placement | 10 | 309 | **100.00%** | 0 | 0 |
| most_wrong_fields | 8 | 545 | 99.49% | 2 | 1 |
| longest_in_500 | 8 | 634 | 99.64% | 1 | 2 |
| long_and_broken | 6 | 559 | 98.17% | 2 | 3 |
| clean_control | 3 | 294 | 100.00% | 0 | 0 |
| long_651_800 | 5 | 733 | 99.76% | 1 | 0 |
| long_801_1000 | 5 | 923 | 99.82% | 0 | 2 |
| long_1001_1200 | 5 | 1080 | 99.78% | 0 | 2 |
| **GROUP A** | 35 | 479 | **99.49%** | 5 | 6 |
| **GROUP B** | 15 | 912 | **99.79%** | 1 | 4 |
| **OVERALL** | 50 | 609 | **99.58%** | **6** | 10 |

Two things stand out:

**Long inputs do not degrade it.** Group B (avg 912 words, up to 1,137) scored
*higher* than Group A (avg 479 words) — 99.79% vs 99.49%. The 1,001-1,200 band
lost zero units. Whatever the model's ceiling is, 1,200 words is not near it.

**The hardest bucket scored perfect.** The 10 products the judge rated worst for
gpt-4o-mini (avg 26.1% placement) came back at 100% coverage, 0 missing.

## 4. Verification — all assertions passed

| Check | Result |
|---|---|
| Every selected product present | PASS |
| State file == raw screen output (no fix applied) | PASS |
| Truncation flagged, not silently counted | PASS |
| Extracted text traces back to raw source | PASS |

The last check is a hallucination guard: every field with 8+ words must have
≥50% of its words present in the raw source. With Group B inputs 1.7x larger
than anything previously tested, invention was a real risk worth asserting
rather than assuming. Nothing failed.

## 5. An important correction about the "0% placement" products

Both 723099 and 207835 were selected as worst-case (0.0% placement accuracy).
Hand-checking them shows the score is misleading:

- **Both products have exactly ONE field.** A single judge disagreement scores
  0%, so the number reflects sample size, not catastrophic failure.
- **gpt-5.5-pro produced byte-identical output to gpt-4o-mini on both.**

The judge's objections were reasonable but debatable: for 723099 it argued
*"Only available for Go Ballooning customers for voucher redemption"* is an
eligibility restriction rather than description; for 207835 that a step-by-step
route with named stops belongs in itinerary rather than about.

**Implication:** the 500-run's placement percentages are noisy on
few-field products. That is worth knowing before the judge runs on this set.

## 6. Where the two models genuinely differ (Group A, 440 field comparisons)

Coverage says both models capture the content. Placement is where they diverge:

| | Count |
|---|---|
| Identical values | 109 |
| Only gpt-5.5-pro filled | 55 |
| Only gpt-4o-mini filled | 60 |

**Fields only gpt-5.5-pro filled** — it makes finer distinctions:
`redo_booking_departure_info` (9), `redo_desc_what_excluded` (7),
`redo_desc_other` (6), `redo_booking_contact` (6),
`redo_booking_before_arrival` (5), `redo_booking_cancellation` (5)

**Fields only gpt-4o-mini filled** — dominated by catch-alls:
`redo_booking_other` (9), `redo_booking_check_in` (7), `redo_min_age` (6),
`redo_desc_highlights` (6), `redo_booking_inclusions` (5)

The pattern is consistent with the judge's earlier finding that gpt-4o-mini
over-uses catch-all buckets: gpt-5.5-pro routes content into specific fields
(departure_info, contact, before_arrival, cancellation) where gpt-4o-mini
leaves it in `booking_other`.

**This is a hypothesis, not a measurement.** Coverage cannot confirm which
placement is correct — only the judge or manual review can. Both models filling
`redo_desc_itinerary` in 3 cases each shows the disagreement runs both ways.

## 7. Judge — not run

Deliberately deferred. When it runs it will use **gpt-4o-mini, not gpt-5.5-pro**,
so the model is not marking its own homework.

One caveat to carry forward: in the earlier judge comparison gpt-4o-mini agreed
with the majority only **74.5%** of the time (others ~89%) and flagged 16.1% of
fields against their ~24%. **It under-flags.** A clean result from it is weaker
evidence than the same result from a stronger judge — but anything it *does*
flag is very likely real.

Commands, when approved:
```
python build_judge_batches.py  --run gpt55raw --models gpt-4o-mini
python run_judge_batches.py    --run gpt55raw --models gpt-4o-mini
python score_judge_verdicts.py --run gpt55raw --models gpt-4o-mini
```

Note on the filename: `gpt55raw_post_fix_state.json` ends `_post_fix_state`
only because `build_judge_batches.py` resolves its input as
`{--run}_post_fix_state.json`. **No fix was applied** — that is asserted in
`verify_gpt55_50.py`, not assumed.

## 8. Conclusion

On raw extraction, gpt-5.5-pro is **near-perfect on content**: 99.58% coverage
across 50 deliberately-hard products, only 6 missing units in total, and no
degradation at all on inputs up to 1,137 words. On this evidence its raw output
would not need the deterministic paste fix — the fix exists to rescue lost
content, and there is almost none to rescue.

The open question is **placement**, which this pass cannot answer. The
side-by-side shows the two models disagree on roughly 115 of 440 fields, with
gpt-5.5-pro favouring specific fields and gpt-4o-mini favouring catch-alls. That
pattern favours gpt-5.5-pro, but it needs the judge or manual review to confirm.

Cost remains the unresolved constraint: 335k prompt + 120k completion tokens for
50 products, with no confirmed rate on this account.
