---
title: "Finding 4: Atiyah 2018 §3.3 has a paper-direct step gap"
date: 2026-05-02
lang: en
---

# Finding 4: Atiyah 2018 §3.3 has a paper-direct step gap

[← All English posts](../../) · [한국어](../../../ko/posts/05-finding-atiyah-step-gap/) · *2026-05-02*

> A case-study contribution to the project's *failed-proof catalog*. The gap itself was identified by the wider community at the time of Atiyah 2018; the project's own contribution is a 5-category framework for systematic critical reading.

## The gap (paper-direct)

Atiyah's 2018 *"The Riemann Hypothesis"* §3.3 claims a derivation:

> Suppose ζ has a zero b in the critical strip off the critical line. Define F(s) := T{1 + ζ(s+b)} − 1. Then **F(s) = 2F(s)** ⟹ F = 0 (in characteristic 0).

The project's Cycle (attempt 131) checked the derivation directly using only the paper's own §2.6 and §2.7:

- §2.6 (paper-direct, weakly analytic): T{(1+f)(1+g)} = T{1+f+g}
- §2.7 (paper-direct): T(1+s) = T(1+s/2)²

Direct computation:

- T{(1+F)²} = T{1+2F} (by §2.6 with f=g=F)
- T(1+2F) = T(1+F)² = (1+F)² (by §2.7)
- So T{(1+F)²} = (1+F)²

Both sides equal (1+F)². The derivation does *not* produce *F = 2F* from §2.6 + §2.7 alone. The "F = 2F" step is a paper-direct step gap.

This finding is consistent with the broader community's identification of Atiyah 2018 as a failed proof (Tao and others noted independently at the time of the paper's release).

## The project's contribution: 5-category framework

The project's `lemmas/failed_proof_catalog_publishable.md` proposes a 5-category framework for systematic critical reading of failed RH proofs:

- **Category A — Trivial circular**: spectrum identification trivially equivalent to ζ-zero condition
- **Category B — Reference circular**: core object's well-definedness depends on unpublished/unverified other paper
- **Category C — Identity transplant**: equation valid only in *limited domain* (linear approximation) used as *exact* equality in proof
- **Category D — Multi-valued inversion**: f(g(s)) = 0 ⟹ g(s) = 0 step ignoring multi-valued inverse
- **Category E — Self-acknowledged speculation**: paper itself contains *"undecidable"* or similar disclaimer alongside *proof claim*

**Atiyah 2018 manifests all five** — a useful self-evidence test for the framework:

- A: spectrum/zero relation in §3 derivation is trivially circular
- B: T(s) Todd function's explicit form depends on Royal Society submission [2] (unpublished)
- C: §2.6 (linear approximation, paper §2 explicit) used as exact equality in §3 proof
- D: §3 derivation 1+ζ(s+b) ∈ T⁻¹(1) ignores multi-valued inverse
- E: §5 *"general case undecidable in Gödel sense"* alongside §3 *"proof by contradiction"*

## Why this finding might be useful

A 5-category framework gives reviewers and proof-writers a structured checklist for systematic gap-finding. It is *prescriptive* (what to look for) rather than just *descriptive* (post-hoc analysis).

## What this is *not*

- The §3.3 gap is **not original to this project** — it was identified at the time of Atiyah 2018 by the broader mathematics community. The project's contribution is the *categorization framework*, not the gap.
- This is **not a personal critique of Atiyah** — at the time of the 2018 paper Atiyah was 89 years old; the failure mode is structural, not personal.

## Where the framework could go

The framework could be extended to other failed RH proof attempts (de Branges series, various amateur preprints, etc.). The project has not done this systematically yet — it remains a publishable potential.

## Audit trail (Layer 1)

- `lemmas/failed_proof_categories.md` — the original 5-category lemma (cycle 1 of catalog development)
- `lemmas/failed_proof_catalog_publishable.md` — the publishable draft (Critique #5 #4 absorption)
- `attempts/066_atiyah2018_search/` — initial Atiyah read
- `attempts/131_atiyah_2018_failed_proof_deep/` — deep §3.3 step-gap analysis
- `attempts/154_failed_proof_catalog_strengthen/` — Category F (abstraction-concrete gap) addition with de Branges as case-study mention

## Refuting / strengthening this finding

If you can argue Atiyah 2018 §3.3 *does* derive F = 2F from §2.6 + §2.7 alone, please email **x2ever.han@gmail.com**. Or if you have a candidate failed proof that does *not* manifest any of the 5 categories, that would be an interesting framework stress-test.

---

[← Previous](../04-finding-connes-consani-progress/) · [한국어](../../../ko/posts/05-finding-atiyah-step-gap/) · [Next: Process →](../06-process-cycle-protocol/)
