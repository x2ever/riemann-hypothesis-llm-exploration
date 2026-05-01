---
title: "Finding 3: Connes–Consani had measurable progress 2018→2021"
parent: English
nav_order: 4
date: 2026-05-02
---

# Finding 3: Connes–Consani had measurable progress 2018 → 2021

[← All English posts](../../) · [한국어](../../../ko/posts/04-finding-connes-consani-progress/) · *2026-05-02*

> A bookkeeping observation. The project did not produce this — it identified it from the existing Connes–Consani publication chain.

## What the project read (Cycle 5)

A 4-paper chain from Connes–Consani's arithmetic site / Riemann–Roch program:

1. **1502.05580 (2016, Adv. Math. 291)** — Geometry of the Arithmetic Site
2. **1805.10501 (2018, Springer 2020)** — Riemann–Roch strategy on the Square of the Scaling Site
3. **arxiv 2006.13771 (2020) / Selecta Math 2021** — Weil positivity and trace formula at the archimedean place
4. **2401.08401 (2024)** — Knots, Primes and the Adele Class Space

## The specific 2018 → 2021 progress

**2018 paper** (1805.10501) page 2 self-acknowledges:

> *"However, in the process to formulate a Riemann–Roch theorem on the square of the Scaling Site one faces a substantial difficulty. The problem, **which is still open at this time**, has to do with an appropriate definition of the sheaf cohomology (as idempotent monoid) H¹..."*

**2021 paper** (Selecta Math) §1:

> *"This paper is motivated by the desire to understand the link between the analytic Hilbert space theoretic strategy first proposed in [11], and the geometric approach pursued in the joint work of the two authors. The latter unveiled a novel geometric landscape still in development for an intersection theory of divisors (on the square of the Scaling Site), thus not yet in shape to handle the delicate principal values. **The first contribution of this paper is to make explicit the relation between the two approaches, thus overcoming the above problem.**"*

Then **Theorem 1** (page 3):

> *"Let g ∈ C_c^∞(ℝ_+^×) have support in [2^(-1/2), 2^(1/2)] and Fourier transform vanishing at i/2 and 0. Then one has W_∞(g * g*) ≥ Tr(ϑ(g) S ϑ(g)*)."*

This is a paper-direct positivity inequality bridging the 2018 still-open problem.

## Why this matters for the project's framing

It documents that the *active program* is not "25 years stuck". There is incremental paper-direct progress. The project's own role is monitoring (paper acquisition + paper-direct quotation), not contributing.

Specifically: the project's Lemmas 9, 10 (Findings 1, 2) document empirical universal NO, and one might worry the lemmas are claiming the program is dead. Cycle 5's reading of the 2021 paper is a counter-weight to that worry: there is post-2018 progress; the lemmas are just empirical-checklist statements about candidate spectral operators, not claims that the underlying approach is dead.

## Self-acknowledged narrow scope (paper-direct)

The 2021 Theorem 1 is **single archimedean place only**. The paper's own §abstract:

> *"All the ingredients and tools used above make sense in the general semi-local case, where Weil positivity implies RH"*

— meaning the general (multi-prime) case is **still open**.

And paper §1 self-acknowledges: *"potential conceptual reason"* — ZFC-side proof not yet complete.

So the project's reading: **narrow-scope direct progress (path 1, Weil positivity archimedean) + general case still-open**.

## Cross-mapping to project's Findings 1, 2 (Cycle 4)

Cycle 4 (one cycle earlier than Cycle 5) had attempted a unification: *"Lemmas 9, 10's universal NO results are two manifestations of the same Connes–Consani missing components."*

Cycle 5's 4-paper read **partially refuted** this unification:

| Path | Active Continuation | Still-Open Component |
|---|---|---|
| Path 1 (Weil positivity, axiom α / Wall #2) | Connes–Consani 2018→2021 progress (single archimedean) | General semi-local case |
| Path 2 (Wall #1 cohomological transfer / axiom 6 / Wall #5) | Connes–Consani 2014–2024 (10 yrs accumulation) | H¹ cohomology on the square (still open per 2018) |

→ Both are *Connes–Consani* program — same authors, *separate angles*. Cycle 4's "single source unification" was too strong; the two paths are connected but not identical.

This is one of the project's clearer self-correction moments — **a cycle weakening its own previous cycle's hypothesis** rather than reinforcing it.

## What this is *not*

- Not an evaluation of whether the program will succeed (out of scope, beyond the project's capability).
- Not a claim that the project contributed anything to the program.
- Not RH progress.

## Audit trail (Layer 1)

- `attempts/186_cycle3_*` — Cycle 3 (initial active program identification, included in lemma 3 update)
- `attempts/187_cycle4_*` — Cycle 4 (4-paper read + partial refutation of Cycle 3)
- `attempts/188_cycle5_*` — Cycle 5 (Selecta 2021 deep + Theorem 1 quote)
- `lemmas/positivity_unification_hypothesis.md` — `Cycle 3 / 4 / 5 Update` sections containing the cross-mapping table

---

[← Previous](../03-finding-wall2-bound/) · [한국어](../../../ko/posts/04-finding-connes-consani-progress/) · [Next: Finding 4 →](../05-finding-atiyah-step-gap/)
