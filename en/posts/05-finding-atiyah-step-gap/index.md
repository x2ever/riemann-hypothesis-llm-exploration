---
title: "Finding 4: Atiyah 2018 §3.3 has a paper-direct step gap"
parent: Findings
grand_parent: English
nav_order: 5
date: 2026-05-02
---

# Finding 4: Atiyah 2018 §3.3 has a paper-direct step gap

[← All English posts](../../) · [한국어](../../../ko/posts/05-finding-atiyah-step-gap/) · *2026-05-02*

> A failed-proof case study with the actual algebra. The gap was identified by the wider community at the time of Atiyah's 2018 preprint; this post derives it explicitly from the paper's own §2 axioms.

## Setup (Atiyah 2018, paper-direct)

The paper introduces a function $T: \mathbb{C} \to \mathbb{C}$ called the *Todd function* with two key properties:

**Property §2.6** (paper-direct, *"weakly analytic"*):
$$T\{(1+f)(1+g)\} = T\{1+f+g\}$$
The paper presents this as a *linear approximation* identity (this caveat will matter).

**Property §2.7** (paper-direct):
$$T(1+s) = T\!\left(1 + \tfrac{s}{2}\right)^2$$

The paper then claims a proof of RH by contradiction in §3.3.

## §3.3 — the paper's argument

Suppose $\zeta(b) = 0$ for some $b$ in the critical strip *off* the critical line. Define:
$$F(s) := T\{1 + \zeta(s+b)\} - 1$$

The paper claims:

> *"Then $F(s) = 2F(s)$ in characteristic 0, hence $F \equiv 0$."*

From $F \equiv 0$ the paper derives $\zeta \equiv 0$, contradiction, so no such $b$ exists, hence RH.

## The gap — explicit derivation

We work *only* from §2.6 and §2.7 as the paper presents them, and check whether $F = 2F$ follows.

**Step 1.** Apply §2.6 with $f = g = F$:
$$T\{(1+F)(1+F)\} = T\{1 + 2F\}$$
$$\therefore \quad T\{(1+F)^2\} = T\{1+2F\} \qquad (*)$$

**Step 2.** Apply §2.7 with $s = 2F$:
$$T(1+2F) = T(1+F)^2 \qquad (**)$$

**Step 3.** Compose $(*)$ and $(**)$. Set $X := T(1+F)$:
- LHS of $(*)$: $T\{(1+F)^2\}$
- $(**)$: $T(1+2F) = X^2$
- RHS of $(*)$: $T(1+2F) = X^2$

So we obtain
$$T\{(1+F)^2\} = X^2 \quad \text{and} \quad T(1+2F) = X^2.$$

Both equal $X^2$. The combined statement is
$$X^2 = X^2,$$

a tautology. **The derivation $F = 2F$ does not follow from §2.6 + §2.7 alone.**

## Why §2.6 cannot bear the weight

The paper itself frames §2.6 as a *linear approximation* (the *"weakly analytic"* qualifier in §2). Substituting $f = F$ where $F$ is *not* infinitesimally small is moving §2.6 outside its stated domain of validity.

This is **Category C of the failed-proof catalog (Identity transplant)**: an equation valid only in a *limited domain* (here: linear approximation) used as an *exact* equality in proof.

## A second gap in §3 — multi-valued inversion

Beyond the F=2F step, §3 also makes the inference:
$$T(1+\zeta(s+b)) = 1 \quad \implies \quad \zeta(s+b) \equiv 0$$

But $T^{-1}(1)$ is generically *multi-valued* — the paper does not produce a uniqueness argument for the inverse $T^{-1}$. Without uniqueness, $T(1+w) = 1$ does not imply $w = 0$. This is **Category D (Multi-valued inversion)**.

## A third issue — §5 vs §3

§5 of the same paper concludes:

> *"The most general version of the Riemann Hypothesis will be an undecidable problem in the Gödel sense."*

— which sits awkwardly alongside the §3 *"proof by contradiction"*. The two cannot both be the author's settled position. This is **Category E (Self-acknowledged speculation alongside proof claim)**.

## The 5 categories of failed RH proof manifestations

Atiyah 2018 manifests **all five** of the project's failed-proof categories:

| Category | Description | Atiyah 2018 manifestation |
|---|---|---|
| **A — Trivial circular** | Spectrum/hypothesis trivially equivalent to conclusion | §3 derivation encodes the zero condition $\zeta(s+b) = 0$ as $F = 0$, not derived from independent structure |
| **B — Reference circular** | Core object's well-definedness depends on unpublished work | $T(s)$ explicit form depends on Royal Society submission [2] (unpublished at preprint time) |
| **C — Identity transplant** | Equation valid only in *limited domain* used as *exact* in proof | §2.6 (linear approximation) used as exact in §3 (Step 1 above) |
| **D — Multi-valued inversion** | $f(g(s)) = 0 \implies g(s) = 0$ ignoring multi-valued inverse | $T(1+w) = 1 \implies w = 0$ without uniqueness argument |
| **E — Self-acknowledged speculation** | Paper contains *"undecidable"* alongside proof claim | §5 *"undecidable in Gödel sense"* + §3 *"proof by contradiction"* |

## The framework as a prescriptive checklist

The 5-category framework is *prescriptive* (what to look for) rather than just *descriptive* (post-hoc analysis). For a reviewer or proof-writer working through any new RH proof attempt:

1. **A-check**: Is any axiom, hypothesis, or definition trivially equivalent to the conclusion the paper wants to draw?
2. **B-check**: Does any core object require unpublished or unverified external work?
3. **C-check**: Are any equations used outside their stated domain of validity (e.g., approximations used as exact)?
4. **D-check**: Are any function inversions performed without a uniqueness argument?
5. **E-check**: Does the paper contain self-acknowledged disclaimers that contradict the proof claim?

When 2 or more categories trigger on the same proof attempt, that is strong evidence of structural failure. Atiyah 2018 triggers all five, which is the failure mode the framework was extracted from.

## What this finding is *not*

- The §3.3 gap identification is **not original to the project**. The broader mathematics community (Tao, several others) noted the issue independently at preprint release time.
- The **5-category framework** *is* the project's contribution — as a structured checklist transferable to other proof attempts.
- This is **not a personal critique of Atiyah**. At the time of the 2018 preprint Atiyah was 89; the failure mode is structural, not personal. The Todd function itself (separate from the proof attempt) remains a mathematically interesting object.
- This is **not RH progress** — it documents a way RH proof attempts fail, not how they succeed.

## Where the framework could go

Systematic application to:
- de Branges' RH proof series (multi-decade attempts, with partial retractions)
- amateur preprint catalog (vixra archive of failed RH attempts)
- historical Hilbert program failures (more nuance — those weren't "failed proofs" in the same structural sense)

The project has not run this systematically. The framework is publication-ready as a standalone *American Mathematical Monthly* / *Math Magazine*–style expository contribution.

## Refuting / strengthening this finding

If you can argue Atiyah 2018 §3.3 *does* derive $F = 2F$ from §2.6 + §2.7 alone, please email **x2ever.han@gmail.com**. Specifically: produce the missing intermediate step that this derivation does not see.

Or if you have a candidate failed proof that does *not* manifest any of the 5 categories — that would be a useful framework stress-test.

---

[← Previous: Finding 3](../04-finding-connes-consani-progress/) · [한국어](../../../ko/posts/05-finding-atiyah-step-gap/) · [Next: Process →](../06-process-cycle-protocol/)
