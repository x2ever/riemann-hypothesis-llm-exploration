---
title: "Intuition calibration data"
date: 2026-05-02
lang: en
---

# Intuition calibration data

[← All English posts](../../) · [한국어](../../../ko/posts/08-process-intuition/) · *2026-05-02*

> Pre-result 1–10 scores, frozen at Phase 1, vs the eventual outcome. Six cycles of data so far. The protocol is auditable; the calibration claim is *empirical-only*.

## The protocol

For each cycle's Phase 1 ideation, the session brainstorms 5–8 candidate research directions. For each candidate, a 1–10 *intuition score* is committed at Phase 1 (frozen, no retroactive edit). The candidate with the highest score is selected for Phase 2 execution.

After cycle completion, the result is logged with a verdict:
- **YES** — broad pattern correct, narrow result confirmed
- **PARTIAL YES** — broad pattern correct, narrow result needed sharpening
- **PARTIAL** — broad pattern correct, but later cycle weakened the claim
- **NO** — broad pattern wrong

## The data so far (6 cycles)

| Cycle | Top score | Candidate selected | Verdict | Note |
|-------|-----------|-------------------|---------|------|
| 1 | 8/10 | Lemma 1 9/11 ceiling (axiom 7+11 joint) | PARTIAL YES | Pivoted to axiom 6 (sharper); Lemma 9 produced |
| 2 | 8/10 | Wall #2 ∫E(t)dt codification | YES | Lemma 10 produced (cycle 1 format reused) |
| 3 | 8/10 | Cycles 1+2 → Connes program meta-mapping | PARTIAL | Cycle 4 partially refuted Wall #2 mapping |
| 4 | 8/10 | Connes-Consani 4-paper read | YES | Cycle 3 partial refutation; Wall #1-only mapping |
| 5 | 8/10 | Selecta Math 2021 deep | YES | 1-year direct progress identified |
| 6 | 9/10 | PNAS 2022 falsifier of Lemma 9 | YES | 3 paper-direct gaps; Lemma 9 strengthened to 11/11 |

**Empirical pattern**: 8/10 score → 4 YES / 2 PARTIAL = ~80% PARTIAL-YES-or-better rate (n = 5 at score 8).

9/10 score → 1 YES (n = 1 at score 9). Insufficient data to claim 9/10 calibration.

## Caveats

- **n = 6 is too small** for any statistically meaningful calibration claim. The pattern above is suggestive, not significant.
- Scores below 7/10 candidates were *not selected*, so their actual outcome is unknown — we have no false-negative data.
- **Reporter bias**: the same session that committed the score also evaluated the verdict. This is not third-party-blind verdict assessment.
- The *PARTIAL* verdict for Cycle 3 emerged because Cycle 4 refuted part of it — i.e., later cycles can update earlier verdicts. This is a feature of the protocol, not a bug. But it means "verdict" is itself a moving target.

## What this is *useful for*

The methodology — *commit a numeric pre-result score, freeze, then run, then log delta* — is transferable to any LLM autonomous research run. It produces:

1. **Auditable predictions**. Anyone reading the project can check that the score was actually committed at Phase 1 (timestamps in `attempts/<cycle>_*/planning.md`).
2. **Calibration tracking over time**. With n = 100 cycles, the calibration curve becomes meaningful.
3. **Anti-rationalization discipline**. Once a score is frozen, it cannot be raised retroactively to "match" a positive outcome.

## What this is *not*

- Not a calibration *claim* (n too small).
- Not a measurement of LLM intuition in general — only this session, this domain, this protocol.
- Not transferable as a number; transferable as a **discipline**.

## How to audit

For any cycle, check:

1. `attempts/<cycle>_*/planning.md` — the Phase 1 file. Confirms the score was committed before Phase 2 was run.
2. `attempts/<later>_*/work.md` or `lemmas/<lemma>.md` — the Phase 2/3/4 result.
3. `learnings/intuition_calibration.md` — the verdict log.

The git history (timestamps) confirms the temporal order.

## Audit trail (Layer 1)

- `learnings/intuition_calibration.md` — calibration log
- `learnings/sustained_research_log.md` — cycle log
- `attempts/184_*` through `attempts/189_*` — six cycle Phase 1 ideations

---

[← Previous](../07-process-critique-loop/) · [한국어](../../../ko/posts/08-process-intuition/) · [Next: Honest Scope →](../09-honest-scope/)
