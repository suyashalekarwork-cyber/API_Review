# Best-Model Evaluation — 13 Models on Identical Products

Which model should the Fareharbor extraction pipeline use? Two independent
measurements on the same 10 hard products, with prompt V4.4 unchanged so the
model is the only variable.

1. **Content survival** — did the supplier's words make it into the output?
2. **Placement** — did they land in the *right field*?

These turn out to be nearly uncorrelated, and only the second one decides
whether the data is usable.

---

## Headline result

**gpt-5.4-nano.** Best on both measurements, at $50 to process all 23,034
products.

| Model | Coverage | MISSING | Placement HIGH / MED | Cost 23,034 |
|---|---|---|---|---|
| **gpt-5.4-nano** | **99.75%** | **0** | **1 / 4** | **$50** |
| gpt-5.5-pro | 99.24% | 1 | 4 / 19 | $7,309 |
| gpt-5-mini | 99.16% | 1 | 1 / 17 | $75 |
| gpt-5.6-terra | 99.13% | 1 | 3 / 18 | $487 |
| gpt-4o-mini *(current)* | 89.38% | 26 | 2 / 8 | $28 |

Nine further models were tested; the full 13-model ranking is in
`best_model_13_summary.md`.

Against the incumbent gpt-4o-mini: **+10.4 coverage points, 26 missing units
→ 0, for $22 more** across the entire catalogue. Strictly better on both axes.

**gpt-5.4-nano beats gpt-5.5-pro at 1/146th the cost** — including on
placement, where gpt-5.5-pro is last of the five audited.

---

## Why coverage alone is not enough

Product 451390: every model scored 99–100% coverage. Two of them filed
**"a COMPLIMENTARY shuttle bus"** under `redo_desc_what_excluded` — *"what is
NOT included"*. The words all survived, so coverage saw nothing wrong, while
the output told the customer the opposite of what the supplier wrote.

The cause is the prompt, not the model. V4.4 maps the raw label `extras:` to
`redo_desc_what_excluded`, assuming "extras" means paid add-ons, and states the
mapping "is authoritative and overrides your own judgment" — so a model
following the prompt correctly produces the wrong answer. **gpt-5.5-pro and
gpt-5.6-terra, the two most expensive models tested, both obeyed and both got
it wrong.** No change of model fixes it.

**How often this actually happens** (measured across all 11,231 Fareharbor
rows, not just these 10 products):

| `extras:` section contains | Rows | V4.4 verdict |
|---|---|---|
| Paid signals only | 438 | correct — genuinely not included |
| Ambiguous (no clear signal) | 407 | unknowable from keywords |
| **Free signals only** | **8** | **misfiled** |
| Mixed free + paid | 9 | needs sentence-level handling |

862 products carry an `extras:` section and only **8 (0.9%) are clearly
misfiled** — the mapping is right in the large majority of cases. The defect is
real and customer-facing on those 8, but it is not a pipeline-wide problem. An
earlier draft of this README called it "the single largest defect" on the
strength of a single product, before the frequency was measured; that was
wrong, and the fix belongs in code rather than a prompt-version bump.

The general lesson holds regardless of the count: **coverage counts words that
survived and cannot see that they contradict the field they landed in.** That
is the whole reason the placement audit exists.

`enchanted_forest_field_mapping.txt` walks through this product field by
field.

---

## Files

| File | What it is |
|---|---|
| `best_model_13_summary.md` | Full 13-model ranking, cost, reliability, recommendation |
| `best_model_13.xlsx` | 7 sheets — see below |
| `best_model_13_review.txt` | Raw source + every model's output, readable without Excel |
| `placement_audit_10_report.txt` | Placement audit: verdict, evidence, all 126 findings by product |
| `enchanted_forest_field_mapping.txt` | Product 451390 walked through field by field |

### `best_model_13.xlsx` sheets

| Sheet | Contents |
|---|---|
| `Ranking` | 13 models: coverage, MISSING, fields filled, cost, tokens |
| `Quality_vs_Cost` | Coverage against cost — where quality plateaus |
| `Per_Product` | 10 products x 13 models |
| `Side_By_Side` | Every field, all 13 models in adjacent columns |
| `Top_Models_Side_By_Side` | Narrowed to top 3 + gpt-5.6-terra + incumbent, with raw source alongside |
| `Raw_Source` | Full raw text per product |
| `Content_By_Model` | All 28 fields per product per model |

---

## Scripts (`scripts/`)

Run in order:

| Script | Does |
|---|---|
| `build_best_model_batches.py` | Builds one JSONL per model. Parameter sets are read from `model_compatibility_final.json`, never guessed — gpt-4 family needs `max_tokens`+`temperature`, gpt-5/o-series need `max_completion_tokens` only, and the wrong one fails the entire batch |
| `run_best_model_batches.py` | Submits one Batch job per model, polls concurrently. Tracks truncation and unparseable JSON separately from quality |
| `screen_best_models.py` | Scores content survival; merges 4 previously-measured models verbatim |
| `verify_best_models.py` | 6 integrity assertions (see below) |
| `build_best_model_workbook.py` | Builds the workbook + review txt |
| `add_top4_sheet.py` | Adds the narrowed side-by-side sheet |
| `audit_placement_10.py` | The placement audit — 7 detectors |
| `build_placement_report.py` | Renders the audit report |

**Not included** — these live in the pipeline repo and are unchanged proven
code: `loss_detector.py`, `screen_model_comparison.py`,
`build_model_comparison_batches.py`, and
`model_compatibility_final.json`. The scripts import them directly, so they
are here to document method, not as a standalone runnable package.

`run_best_model_batches.py` reads `OPENAI_API_KEY` from the environment. No
key is stored in this repo.

---

## How much to trust this

**Verified.** Integrity assertions passed: state files match screen output (no
fix was applied), extracted text traces back to raw source (no invented
content), and the 4 merged baselines are numerically unchanged. Prompts were
confirmed byte-identical to the original run, so the merge is genuinely
comparable.

**Reliability is separate from capability.** `gpt-5-nano`, `o4-mini` and
`gpt-5` returned truncated or unparseable output on some products. Scored
naively they look poor; measured only on responses that worked, all three
reach ~99%. They are unreliable, not weak — that distinction only surfaced
because bad JSON was tracked separately from quality.

**Limits, stated plainly:**

- **10 products.** Small. Directionally useful, not statistically settled.
- **The placement audit is regex, and regex cannot do judgement.** Three
  detectors produced confidently wrong answers on the first run and were
  corrected only by reading the raw text:
  - `D2` flagged 29 splits for gpt-5.5-pro; most were paragraphs straddling
    two labels, which *should* go to two fields → 12 after fixing.
  - `D1` flagged `"3 and under are free"` as a contradiction; it is a rate
    card listing a free tier among paid ones → price lists exempted.
  - `D4` flagged models for routing cancellation text out of the catch-all
    into `redo_desc_cancellation` — off-map per V4.4 but *better* for the
    reader → downgraded to INFO.
  All published counts are post-correction. **The evidence is the result; the
  counts are only a way to sort it.**
- **No LLM judge and no human verdict has been run.** Rule-based detection
  finds defects it was told to look for and misses types nobody has named.
  Absence of a finding is not proof of correct placement.
- **gpt-5.4-nano's coverage is slightly flattering.** On product 391584 it
  reached 100% partly by duplicating content across two fields. Coverage
  rewards duplication, since a word counted twice still counts.

---

## Before a full production run

1. **Strip markdown in code.** gpt-5.4-nano leaves `**`/`##` in 17 fields —
   worst of any model. Cosmetic, trivially fixable, zero risk. Highest
   value-per-effort item here.
2. **Fix the 8 misfiled `extras:` rows in code, not in the prompt** — move
   free-signal text out of `what_excluded` into `what_included`. Deterministic,
   no re-run, no regression risk. A V4.7 prompt bump is not worth a full re-run
   and re-validation for 0.9% of rows, and added narrowing rules are exactly
   what caused the V4.6 regression (rules made the model drop content instead
   of routing it to the catch-all).
3. **Run a judge** on gpt-5.4-nano vs gpt-4o-mini to confirm the audit.
4. **Check the duplication behaviour** on a wider sample.
