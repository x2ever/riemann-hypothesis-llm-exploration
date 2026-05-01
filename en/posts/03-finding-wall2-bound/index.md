---
title: "Finding 2: Wall #2 ∫E(t)dt unconditional bound — 4/4 universal NO"
parent: Findings
grand_parent: English
nav_order: 3
date: 2026-05-02
---

# Finding 2: Wall #2 ∫E(t)dt unconditional bound — 4/4 universal NO

[← All English posts](../../) · [한국어](../../../ko/posts/03-finding-wall2-bound/) · *2026-05-02*

> Empirical observation, not a theorem. Same logical structure as Finding 1.

## Statement

Across the 4 paper-direct candidates relevant to the Newman–de Bruijn forward heat flow, **no unconditional + constructive + RH-independent bound on ∫_0^Λ E(t) dt has been published**.

Source: `lemmas/lemma2_wall2_axiom_alpha_ceiling.md`.

## Audit table (paper-direct anchored)

| # | Paper | axiom α strict | Paper-direct anchor |
|---|---|---|---|
| 1 | Polymath15 (de Bruijn–Newman upper) | NO | Λ ≤ 0.22 *conditional* (3-tool combination, Theorem 1.1). Unconditional bound not provided. |
| 2 | Rodgers–Tao 2020 (Λ ≥ 0 unconditional) | NO | "far from optimal" (paper §1.5). ∫_{Λ/2}^0 E(t)dt — *backward only* control, forward not given. |
| 3 | Platt–Trudgian 2021 (RH up to H = 3·10¹²) | NO | Λ ≤ 0.2 *via numerical RH up to H = 3·10¹²*; theoretical bound not provided. |
| 4 | Newman 1976 (Λ ≤ 0 ⟺ RH equivalence) | NO | Definition only; abstract equivalence, no unconditional bound. |

**4/4 universal axiom α strict NO.**

## Falsifier search (5 adjacent fields)

Beyond the 4 direct candidates, the lemma searches 5+ adjacent fields:

- **Bombieri–Lagarias 1999**: Λ ≥ 0 *lower* bound. Upper bound not provided. *Not a falsifier.*
- **Selberg method (mollifier)**: Wall #3 (50% barrier). Not directly connected to ∫E dt. *Not a falsifier.*
- **Bourgain–Gamburd–Sarnak expander**: heat semigroup *form similar*, integrated bound shape not present. *Not a falsifier.*
- **Otto's calculus / Wasserstein gradient flow**: 007 negative resolved (time-symmetric vs Wall #2 asymmetric). *Not a falsifier.*
- **Concentration compactness (Lions–Brezis)**: limit point analysis, forward control absent. *Not a falsifier.*
- **Free probability R-transform**: Wall #6 axis (LOCAL-GLOBAL), not Wall #2. *Not a falsifier.*

**No falsifier found across 5+ fields.**

## Specialist Δ — anchored to paper §-end quotes (Lemma 7 protocol)

- **Tao + Conrey (analytic)**: Polymath15 §6 *"this is the limit of the present method"* — combinatorial-optimization internal ceiling. Iwaniec phrase *"extra little tiny bit"* (same essence, Wall #4).
- **Tao (hard analysis)**: Rodgers-Tao 2020 §1.5 *"control integrated energies that resemble ∫_{Λ/2}^0 E(t) dt"* + *"far from optimal"*. Time-asymmetry essential — backward only.
- **Logician (S9)**: Lagarias 2002 (RH Π_1) — anchor for measuring axiom α's logical strength.

## Caveats (the project's own)

- **Empirical only** (4/4 + 5 falsifier fields). *Necessary universal NO not proven* — same induction-leap warning as Finding 1.
- 5-year flat (Rodgers–Tao 2020 → 2025) is an empirical fact, not an obstacle proof.
- **ZFC-independence of axiom α not ruled out.**
- Newman 1976's Λ = 0 ⟺ RH equivalence is *abstract*; whether axiom α has a constructive form provable in ZFC is undetermined.

## Falsifier (lemma retraction conditions)

Any paper providing all four:

1. Unconditional ∫_0^Λ E(t) dt explicit upper bound — paper-direct quote.
2. RH not assumed — paper-direct verification.
3. Constructive form (not abstract equivalence) — paper-direct.
4. No fine-tuning parameter — paper-direct quote or explicit definition.

…retracts the lemma.

## Cross-reference to Finding 1

**Same logical structure, different wall.** Lemma 9 (Wall #5, axiom 6) and Lemma 10 (Wall #2, axiom α) share:

- 4-specialist consensus on the axiom definition
- Paper-direct audit table
- Falsifier search across adjacent fields
- Explicit falsifier criterion
- *Empirical NO ≠ necessary NO* warning

This was deliberate (Cycle 2 "directly reused Cycle 1 format"). The reuse is the project's evidence that the codification template is generalizable.

## Audit trail (Layer 1)

- `lemmas/lemma2_wall2_axiom_alpha_ceiling.md` — full audit
- `attempts/185_cycle2_*` — Cycle 2 (lemma generation)
- `attempts/028_*`, `106_*`, `113_*`, `132_*`, `161_*`, `173_*` — per-paper readings

## Refuting this finding

If you have a paper providing an unconditional + constructive ∫E(t)dt upper bound, please email **x2ever.han@gmail.com**.

---

[← Previous](../02-finding-axiom6-ceiling/) · [한국어](../../../ko/posts/03-finding-wall2-bound/) · [Next: Finding 3 →](../04-finding-connes-consani-progress/)
