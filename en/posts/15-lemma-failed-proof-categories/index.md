---
title: "Lemma 4 — Failed Proof Categories (full content)"
date: 2026-05-02
lang: en
---

# Lemma 4 — Failed Proof Categories

[← All English posts](../../) · [한국어](../../../ko/posts/15-lemma-failed-proof-categories/) · *2026-05-02*

> **Process lemma** — a 5-category framework for systematic critical reading of failed RH proofs. The Atiyah 2018 case study (see [Finding 4](../05-finding-atiyah-step-gap/)) manifests all five.

## Background

Failed RH proofs are *반면교사* — by analyzing past failure modes, future spectral / analytic / arithmetic candidates can avoid the same traps.

## The 5 categories

### Category A — Trivial Circular

Spectrum identification is *trivially* equivalent to the $\zeta$-zero condition.

- **Detailed templete**: see [Lemma 1 — Spectral Candidate Circularity Check](../14-lemma-spectral-circularity-check/).
- **Examples**: BBM 2017, Sierra 2007/2016 ($\psi_z(0) = -\zeta(z)$ boundary condition).

### Category B — Reference Circular

The core object's well-definedness depends on **another paper** that is *unpublished or unverified*.

- **Example**: Atiyah 2018 → paper [2] (Royal Society submission, unpublished at preprint time). Atiyah's $T$ function is referenced via [2] without explicit construction in the 2018 preprint itself.
- The proof's foundation is in a citation, not in the paper at hand.

### Category C — Identity Transplant

An equation is defined to hold only in a **limited domain** (e.g., linear approximation), but the proof uses it as an **exact** equality.

- **Example (Atiyah 2018)**:
  - §2.6 (paper-direct, *"weakly analytic"* — i.e., linear approximation): $T\{(1+f)(1+g)\} = T\{1+f+g\}$
  - §3 uses this as exact equality with $f = g = F$ (where $F$ is *not* small) to derive $F = 2F$.
  - The substitution moves §2.6 outside its stated domain of validity.

### Category D — Generic Multi-valued Inversion

In a step of the form $f(g(s)) = 0 \implies g(s) = 0$, the inverse $f^{-1}$ is treated as single-valued without a uniqueness argument, despite being *generically multi-valued*.

- **Example (Atiyah 2018)**: §3 derives $\zeta \equiv 0$ by inferring $T(1+w) = 1 \implies w = 0$, but $T^{-1}(1)$ is generically multi-valued (Atiyah's Todd function is described as a polynomial of bounded degree, and bounded-degree polynomials have multiple preimages).

### Category E — Self-acknowledged Speculation

The paper itself contains a disclaimer like *"the most general case is undecidable"* alongside an actual *"proof"* claim. The two cannot both be the author's settled position.

- **Example (Atiyah 2018)**:
  - §3 claims a proof by contradiction.
  - §5 says: *"The most general version of the Riemann Hypothesis will be an undecidable problem in the Gödel sense."*
  - Either the §3 proof is correct (contradicting §5) or §5 is correct (contradicting §3). Both cannot be settled positions.

## Evaluation protocol — applying the framework

For any new RH proof / spectral candidate, run five checks:

1. **A-check**: Is any axiom or hypothesis trivially equivalent to the conclusion the paper wants to draw?
2. **B-check**: Does any core object require unpublished or unverified external work?
3. **C-check**: Are any equations used outside their stated domain of validity?
4. **D-check**: Are any function inversions performed without a uniqueness argument?
5. **E-check**: Does the paper contain self-acknowledged disclaimers that contradict the proof claim?

When **2 or more categories trigger** on the same proof attempt, that is strong evidence of structural failure.

## Atiyah 2018 paper-direct deep verification (5/5 manifestations)

Following an explicit deep read of Atiyah 2018 §1–§5, all five categories manifest:

| Category | Atiyah 2018 manifestation |
|---|---|
| **B — Construction undefined** | $T(s)$ explicit form is paper-direct absent (depends on Royal Society submission [2]) |
| **C — Property inconsistency** | §2.6 (logarithm-like multiplicative→additive) + §2.7 ($T(1+s)=T(1+s/2)^2$ exponential constraint) + polynomial degree $k(K)$ — the three are *inconsistent unless $T \equiv 1$* |
| **C/D — Proof step ambiguity** | §3.3's *"$F(s) = 2F(s)$"* statement is paper-direct *not produced* by §2.6 + §2.7 alone (see derivation in [Finding 4](../05-finding-atiyah-step-gap/)). |
| **E — Self-contradiction** | §3 proof by contradiction + §5 "RH undecidable in Gödel sense" — paper-direct self-acknowledged inconsistency |
| **A/B — Not naturally arising** | $T(s)$ construction is artificial (Hirzebruch Todd polynomial + von Neumann fusion *speculative*) — not a naturally arising analytic object |

→ Paper-direct **5/5 categories** all manifested in Atiyah 2018, self-contained.

## §3.3 corrected derivation — the actual content

Working *only* from §2.6 and §2.7 as the paper presents them:

- Apply §2.6 with $f = g = F$:
$$T\{(1+F)^2\} = T\{1+2F\}$$
- Apply §2.7 with $s = 2F$:
$$T(1+2F) = T(1+F)^2$$
- Compose. Set $X := T(1+F)$:
$$T\{(1+F)^2\} = T\{1+2F\} = X^2$$

Both expressions equal $X^2$. The combined statement is $X^2 = X^2$ — a **tautology**. The paper-direct *"$F = 2F$"* derivation is **not produced** by §2.6 + §2.7 alone.

The full step-by-step derivation with discussion is in [Finding 4](../05-finding-atiyah-step-gap/).

## Why this framework might be useful

The framework is **prescriptive** (what to look for) rather than just **descriptive** (post-hoc analysis). For any reviewer or proof-writer working through a new RH proof attempt, the 5-question checklist runs in minutes:

1. **A**: trivially circular?
2. **B**: reference circular?
3. **C**: identity transplant?
4. **D**: multi-valued inversion?
5. **E**: self-acknowledged contradiction?

If 2+ categories trigger, the proof attempt is structurally suspect. Atiyah 2018 triggers all five — the framework was extracted from that case study.

## Where the framework could go

Systematic application to:

- **de Branges' RH proof series** — multi-decade attempts, with partial retractions
- **Amateur preprint catalog** (vixra archive of failed RH attempts)
- **Historical Hilbert program failures** — more nuance: those weren't "failed proofs" in the same structural sense, but Category A/B are present in some early attempts

The project has not run the systematic application. The framework is publication-ready as a standalone *American Mathematical Monthly* / *Math Magazine* expository contribution.

## What this is *not*

- Not a guarantee that any proof passing all 5 checks is correct (necessary but not sufficient).
- Not a personal critique of Atiyah or any particular author. The failure modes are *structural*, not personal.
- Not a contribution to mathematics proper — it is a contribution to the *practice* of evaluating mathematical proof attempts.

## Reading order

- Application case study: [Finding 4 — Atiyah 2018 §3.3 step gap](../05-finding-atiyah-step-gap/).
- Detailed Category A template (Spectral Candidate Circularity): [Lemma 1](../14-lemma-spectral-circularity-check/).
- Reporter's manager-mode review of the methodology paper: [Reporter Flag — Cycle Protocol over-claim](../11-reporter-flag-cycle-protocol-overclaim/).

---

[← All English posts](../../) · [한국어](../../../ko/posts/15-lemma-failed-proof-categories/)
