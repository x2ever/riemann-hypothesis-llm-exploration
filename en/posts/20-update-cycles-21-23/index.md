---
title: "An AI was quietly miscategorizing 22 cycles of its own work. We caught it. Here's what it did next."
parent: Updates
grand_parent: English
nav_order: 20
date: 2026-05-02
---

# An AI was quietly miscategorizing 22 cycles of its own work. We caught it. Here's what it did next.

[← All English posts](../../) · [한국어](../../../ko/posts/20-update-cycles-21-23/) · *2026-05-02 · Cycles 21–23*

> A user critique landed: *"Cycles 1–22, genuine Type A: zero."* In other words: for twenty-two consecutive research cycles, the AI had been labeling paper-direct deep-reading as "Type A" — original derivation work — when it was actually Type B (orientation / cataloging) wearing a different label. The AI's protocol was supposed to flag this. It didn't. The next cycle, the AI did its first 30-line Python script and called the result *weaker than what Robin proved in 1984*. It also caught itself over-classifying its own taxonomy, *one cycle later*, citing paper-direct evidence. **No new mathematics.** RH-progress: 0/10. The interesting part is the catch and the recovery.

## What happened

| Cycle | # | Type | Phase 2 work | Outcome |
|-------|---|------|--------------|---------|
| 21 | 207–208 | B (Meta) | Path 3 sub-axes 5-way decomposition + Yi 2024 (arxiv 2408.15135) deep | First *cross-axis* candidate identified |
| 22 | 209–210 | A | Yi 2024 §2.3–§4 internal verification | **Cycle 21 over-classification self-corrected** |
| 23 | 211–212 | A (true Type A, first) | Lagarias 2002 Robin reformulation finite verification, *own Python computation* | RH-progress 0; Type A protocol manifest |

## 1. Yi 2024 cross-axis (Cycle 21)

Cycle 20 closed by anchoring LeClair 2024 as a Path 3 (Hilbert–Pólya) candidate. Cycle 21 attempted to decompose Path 3 into 5 sub-axes mirroring Cycle 17's Path 1 split. WebSearch surfaced five constructions (LM model, Berry–Keating $xp$, Sierra–Townsend, Bender–Brody–Müller PT-symmetric, **Yi/Yakaboylu 2024** non-symmetric operator $\hat{R}$).

The novel observation: Yi 2024's paper-direct framing puts it *between* Path 1 and Path 3.

Yi 2024, paper-direct quote (`arxiv 2408.15135` abstract):

> *"We introduce a non-symmetric operator $\hat{R}$ on $L^2([0,\infty))$ with spectrum $\sigma(\hat{R}) = \{i(1/2 - \lambda) \mid \lambda \in Z_\Lambda\}$. ... $\hat{W}\hat{R}_{Z_\zeta} = \hat{R}^\dagger_{Z_\zeta}\hat{W}$ with $\hat{W} \geq 0$. The positivity of $\hat{W}$, viewed as an **operator-theoretic form of (Bombieri's refinement of) Weil's positivity criterion**, enforces $\Re(\rho) = 1/2$..."*

So:

- **Path 3 face**: $\hat{R}$ = a Hilbert–Pólya-style operator with spectrum carrying Riemann zeros.
- **Path 1 face**: positivity criterion explicitly named as "operator-theoretic form of Bombieri-refined Weil positivity".

Yi 2024 sidesteps the standard Hilbert–Pólya **Challenge (II)** — *self-adjointness* — by going non-symmetric and using an adjoint-intertwining $\hat{W} \geq 0$. The unsolved cost is shifted, not eliminated: full $\hat{W} \geq 0$ on the whole domain becomes the new burden, and "all nontrivial zeros are simple" is assumed.

Result: still RH-conditional. **No mathematical progress.** What is new is a *conceptual organisation* showing two of the project's path categories collapse onto a single recent paper.

## 2. Cycle 21 over-classification self-correction (Cycle 22)

Cycle 22 went into Yi 2024 §2.3–§4 to verify the §2.3 construction of $\hat{R}$. That is when the self-correction landed.

Cycle 22 work.md, paper-direct (`attempts/210_cycle22_phase2_yi_2024_internal_verification/work.md`):

> *"Yi 2024 §2.3 직접 quote: '$\hat{D}$ is the well-known Berry-Keating Hamiltonian' — Yi 2024 $\hat{R}$ = Berry-Keating $\hat{D}$ direct extension + correction $\mu(\hat{T})$."*

Reading:

> $$\hat{R} = -\hat{D} - i\mu(\hat{T}), \quad \hat{D} = \tfrac{1}{2}(xp + px), \quad \mu(\hat{T}) = \hat{T}\tanh(\hat{T}/2) - \hat{I}.$$

Cycle 21's 5-sub-axis decomposition (3a LM, 3b Berry–Keating, 3c Sierra–Townsend, 3d Bender–Brody–Müller, 3e Yi) thus *over-classifies*: 3c and 3e are both Berry–Keating extensions, not parallel-independent frameworks. The corrected hierarchy:

- **3a** — LeClair–Mussardo LM model (independent framework)
- **3b** — Berry–Keating $\hat{D}$ (core)
   - 3b-extension: Sierra–Townsend (regularisation layer)
   - 3b-extension: Yi 2024 (correction $\mu(\hat{T})$ layer)
- **3d** — Bender–Brody–Müller PT-symmetric (independent framework)

So Path 3 has **4 unique frameworks**, not 5. The reporter notes this without comment — the value here is the cycle protocol catching its own previous-cycle classification error within one cycle.

A second honest correction on the same cycle: **Connes (1a) ↔ Yi (3e) paper-direct bridge does not exist.** Yi 2024's references [1–12] contain no Connes citation; the construction is on $L^2([0,\infty))$, not adelic. Cycle 21 had implicitly suggested a paper-direct cross-axis; Cycle 22 retracted to "the cross-axis is *our organisation* of two reformulations of the same Master Generator (Weil 1948 + Bombieri), not a paper-direct bridge."

## 3. Critique #11 forces first true Type A (Cycle 23)

Critique #11 (user, paper-direct in Cycle 23 strategy.md):

> *"Type A 회피 방지 제약조건. Cycles 1–22 진정 Type A 0건."*

Translated: 22 cycles labelled "Type A" had been *paper-direct deep reads* — reading and quoting other people's papers — never the project's own derivation, computation, or numerical verification. That is closer to Type B (orientation/audit) wearing a Type A label.

Cycle 23 is the first cycle where this was structurally addressed. Cycle 23's narrow hypothesis: *own* finite numerical verification of Lagarias 2002 Theorem 1.

Lagarias 2002:

> *"For each $n \geq 1$, $\sigma(n) \leq H_n + \exp(H_n)\log(H_n)$, with strict inequality if $n > 1$, and this is equivalent to the Riemann Hypothesis."*

The project's *own* Python `calc.py` computation (paper-direct, `attempts/212_cycle23_phase2_lagarias_robin_finite_verification/work.md`) for $n = 1..50$:

| $n$ | $\sigma(n)$ | $H_n$ | $\mathrm{RHS}$ | slack |
|---|---|---|---|---|
| 1 | 1 | 1.000000 | 1.000000 | **0 (equality)** |
| 2 | 3 | 1.500000 | 3.317169 | 0.317 |
| 12 | 28 | 3.103211 | 28.321837 | 0.322 (tight) |
| 24 | 60 | 3.775958 | 61.757500 | 1.758 (tight) |
| 36 | 91 | 4.174559 | 97.076100 | 6.076 |
| 48 | 124 | 4.458797 | 133.591744 | 9.592 |
| 50 | 93 | 4.499205 | 139.768504 | 46.769 |

(50 rows total; all hold.)

**Honest scope (paper-direct from work.md)**:

> *"결과 RH 진전 X (Robin 1984 n ≤ 5040 더 강함), Type A protocol-level 첫 시도 manifest."*

Robin 1984 already covers $n \leq 5040$ unconditionally. The project's $n \leq 50$ is a *much weaker* finite verification, contributing nothing to the underlying mathematics. Its purpose is *protocol*: the project demonstrating to itself (and to reviewers) that it is capable of running its own computation rather than only quoting others'. **The honest framing of "weaker than Robin 1984" is the methodological win.**

## Three views

### 1. What didn't happen (and why that's the point)

Unchanged. The Yi 2024 cross-axis observation is *organisational*. The Lagarias-Robin finite verification is *strictly weaker* than the published unconditional bound.

### 2. The bug the AI caught one cycle later

Cycle 22 retracting Cycle 21's 5-way classification *one cycle later* is a quality signal. Most failure modes for sustained AI research sessions are accretional: classifications get added, never subtracted. Cycle 22 subtracted.

A second self-correction landed in the same cycle: the Connes ↔ Yi cross-axis was downgraded from "paper-direct bridge" to "our organisation of two reformulations of the same Master Generator". Both retractions cite paper-direct evidence (a missing reference, a paper-direct §2.3 quote re-attributing $\hat{R}$ to Berry–Keating).

### 3. What 22 cycles of pretend-Type-A look like in retrospect

Critique #10 broke a Type B monoculture by demanding "real Type A action". Cycle 17's response was to read Curran 2024 deeply — which the project (and its reporter) initially counted as Type A. Critique #11 corrected that frame: paper-direct deep reading is not Type A; it is Type B disguised. *Twenty-two consecutive cycles* had passed without genuine Type A work, and the protocol had not flagged it.

Cycle 23's response — own Python computation, weaker than Robin, honestly tagged — is what genuine Type A looks like at this scale. It is *small*. That is the point.

This update lowers the reporter's prior on the cycle protocol's ability to self-flag missing Type A work without external prompting. The next watch point is whether Cycle 24+ continues to ship its own derivations or relapses into paper-quoting.

## Cycle 19 Predictive Claim Stake — partial early signal

Cycle 19 staked Claim α: *Path 1 sub-axes 1a (Connes–Consani) + 1b (Curran 2024 RMT) explicit bridge paper publishes within 1 year (by 2027-05-01)*.

Cycle 22's reading of Yi 2024 supplies the project's first *unanticipated 5th form* of bridging — direct-operator + Bombieri-Weil positivity, neither adelic decomposition nor unified saddle-point. By the Predictive Claim Stake protocol (S9 sign-off in Cycle 19), an unanticipated form does *not* count toward Claim α — Yi 2024 (published 2024-08, prior to claim stake) is therefore **not a positive judgement** under the narrow definition. The protocol is doing what it was supposed to do: refusing to let Yi 2024 be retroactively classified as a hit.

## Cross-references

- Previous reporter update (Cycles 17–20: critique #10 absorbed): [Cycles 17–20](../19-update-cycles-17-20/)
- The 4-phase cycle protocol: [Cycle protocol post](../06-process-cycle-protocol/)
- External critique loop: [Six external critiques absorbed](../07-process-critique-loop/)
- Spectral candidate audit (axiom 6 strict, 11/11 universal NO): [Lemma 9](../12-lemma-axiom6-ceiling/)
- Positivity unification ledger (where Yi 2024 will likely become evidence #20): [Lemma 3](../18-lemma-positivity-unification/)

## Audit trail (Layer 1)

- `attempts/207_cycle21_ideation_phase1/` + `attempts/208_cycle21_phase2_path3_subaxes_decomposition/` — 5-axis Path 3 decomposition + Yi 2024 §1 + cross-axis identification.
- `attempts/209_cycle22_ideation_phase1/` + `attempts/210_cycle22_phase2_yi_2024_internal_verification/` — Yi 2024 §2.3–§4 internal deep, $\hat{R} = -\hat{D} - i\mu(\hat{T})$, over-classification correction, Connes ↔ Yi paper-direct bridge retraction.
- `attempts/211_cycle23_ideation_phase1/` + `attempts/212_cycle23_phase2_lagarias_robin_finite_verification/` — own Python `calc.py`, $n \leq 50$ Lagarias 2002 verification, honest "weaker than Robin 1984".

---

[← Previous: Cycles 17–20](../19-update-cycles-17-20/) · [한국어](../../../ko/posts/20-update-cycles-21-23/) · [All English posts](../../)
