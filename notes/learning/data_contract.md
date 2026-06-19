DATA-CONTRACT DERIVATION
========================

ANCHOR — pick the layer
-----------------------
Profiling a whole dataset?     -> ISOLATE once, then walk ALL five verdicts.
Judging one value / column?    -> ISOLATE, assign ONE verdict, answer just that.

Two checking layers, kept apart on purpose:
    Layer 1 — ETL / technical:  "Does the code crash?"  (types, nulls, table shape). The entry ticket only.
    Layer 2 — ML / MLOps:       "Do the data break the math or distort reality?". This is the focus.


ISOLATE THE SUBJECT   (once, before the walk)
---------------------------------------------
Name the exact thing:  the target y  |  one feature column  |  the split  |  the live stream.


THE FIVE VERDICTS   (every subject gets exactly one)
====================================================

---------------------
1. EXPECTED-NORMAL:    the guarantee value
    Mechanism: invariant.
    What bound / shape / set MUST always hold?
    What single deviation would prove a data or mapping error?
    Resolve: "[Subject] satisfies [guarantee]; any deviation = defect or mapping error."
---------------------
2. EXPECTED-ARTIFACT:  looks broken, but is known
    Mechanism: known origin.
    What is the EXACT source that produces it?
    Is it reproducible / countable (N rows)?
    How do you normalize it BEFORE the model ever sees it?
    Resolve: "[Value] arises from [source]; expected in ~[N] rows; normalize at [step] — no alarm."
---------------------
3. TRUE-DEFECT:        real corruption
    Mechanism: physical impossibility.
    Which bound does the value violate?
    Is the violation impossible, not merely rare?
    Resolve: "[Value] violates [bound]; impossible -> corruption, not distribution. Reject / fix."
---------------------
4. VALID-SENTINEL:     looks broken, IS meaning
    Mechanism: encoded semantics.
    Does the suspicious value carry a defined meaning?
    Which real defect looks identical — and how do you separate the two cleanly?
    Resolve: "[Value] means [semantics]; do NOT flag; never pool with [look-alike defect]."
---------------------
5. SILENT-DISTORTION:  passes, still lies
    Mechanism: technically valid, yet misleading.
    Nothing crashes — does it dilute importance / inflate the metric / fake redundancy / warp distances?
    What is the right remedy (drop / dedup / robust statistic / transform / different metric)?
    Resolve: "[Property] is technically fine but [deception]; remedy [X] — don't ignore, don't blind-drop."


CHECK   (after each Resolve)
----------------------------
Verdict assigned unambiguously? Did you confuse "rare" with "impossible"?
Is a sentinel (4) cleanly separated from an overflow / defect (3)?
Is the consequence named — for the MATH, the METRIC, or REALITY?


SUBJECT TYPES — what to run the walk over
-----------------------------------------
y  (the label)     -> classes, missing targets, encoding, imbalance, conflicting labels.
X  (the math)      -> dtype, inf / NaN and their single source, physical bounds, sentinels.
X  (reality)       -> zero-variance, duplicate columns, collinearity, correlation method, skew.
Split / pipeline   -> row leakage across the split, transform leakage (fit on train only), stratification.
Drift (operation)  -> live distribution vs training; nothing looks broken, the model still rots.


SYNTHESIS   (after the walk — the contract in one line)
-------------------------------------------------------
"Layer 1 asks 'does it run?', Layer 2 asks 'is the math right and does it match reality?'.
 Guarantees (1) hold, artifacts (2) get normalized, defects (3) get rejected, sentinels (4) get protected,
 distortions (5) get treated — and the imbalance/metric trap plus the correlation-method trap stay in YOUR head,
 because no tool catches those."


MAPPING TO A VALIDATION TOOL (e.g. deepchecks)
----------------------------------------------
Expectation                          Check family
-----------------------------------  ------------------------------------------------
Zero-variance columns          (5)   integrity  -> Single Value in Column
Full-row duplicates            (5)   integrity  -> Data Duplicates
Conflicting labels             (3)   integrity  -> Conflicting Labels
inf / special values           (2)   integrity  -> Special Values / Mixed Nulls
Outliers / plausibility        (3)   integrity  -> Outlier Sample Detection
String / encoding mismatch     (2)   integrity  -> String Mismatch
Train<->test leakage           (5)   train_test -> Data / Index Leakage
Distribution drift             (1)   train_test -> Feature / Label Drift
Multicollinearity              (5)   custom Spearman / MI check (NOT Pearson)
Imbalance -> metric choice     (1)   — no check, keep in head —
Sentinel vs overflow         (4/3)   — no check, keep in head —


FAIL-FAST
---------
Verdict unclear or subject fuzzy           -> back to ISOLATE.
"Rare" flagged as "impossible"             -> move verdict 3 to 1 or 5.
Sentinel (4) counted as a violation        -> split the pool, re-verdict.
Hunting a crash where nothing crashes      -> it's Layer 2 (distortion), not Layer 1.