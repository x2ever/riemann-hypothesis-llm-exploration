---
title: "Lemma 10 — Wall #2 axiom-α universal NO across 4 paper-direct candidates (full content)"
date: 2026-05-02
lang: en
---

# Lemma 10 — Wall #2 (Forward Heat Flow) Axiom α Universal NO

[← All English posts](../../) · [한국어](../../../ko/posts/13-lemma-wall2-axiom-alpha/) · *2026-05-02*

> **The full process lemma**, embedded directly. Source: Cycle 2. Same logical structure as [Lemma 9](../12-lemma-axiom6-ceiling/), different Wall.

> ## Status disclaimer
>
> *Empirical* universal NO. *Necessary* universal NO is **not proven** (S9 caveat: 4-paper enumeration → induction leap). ZFC-independence not ruled out.
>
> Wall mapping: **Wall #2 (FORWARD-TIME ENERGY)** paper-direct quantitative codification.

## Background — what is "axiom α"?

The de Bruijn–Newman constant $\Lambda$ is defined via the heat-flow modification of the Riemann $\xi$-function. For each $t \in \mathbb{R}$, define:
$$H_t(z) := \int_0^\infty e^{tu^2} \Phi(u) \cos(uz) \, du$$
where $\Phi$ is the standard Riemann $\xi$-kernel. Newman's classical result (1976) is:
$$\Lambda \leq 0 \iff \mathrm{RH}.$$

The forward heat flow $H_t$ for $t \geq 0$ has zeros that *spread* (Polya–de Bruijn, Newman). The energy of the zero configuration:
$$E(t) := \sum_{j < k} \frac{1}{(\gamma_j(t) - \gamma_k(t))^2}$$
where $\{\gamma_j(t)\}$ are the imaginary parts of $H_t$'s zeros, satisfies a monotonicity relation that controls how zeros spread.

**Axiom α (strict):** *There exists an unconditional upper bound on $\int_0^\Lambda E(t) \, dt$ that is RH-independent, fine-tuning-free, and constructive.*

Such a bound, if obtained, would close the gap between $\Lambda \geq 0$ (Rodgers–Tao 2020, unconditional) and $\Lambda \leq 0 \iff \mathrm{RH}$ (Newman 1976).

## Statement of the lemma

Of 4 paper-direct candidates relevant to forward heat flow (Polymath15, Rodgers–Tao 2020, Platt–Trudgian 2021, Newman 1976), **the count satisfying axiom α strict is zero**.

> **An unconditional upper bound on $\int_0^\Lambda E(t) \, dt$, RH-free, fine-tuning-free, constructive** — this combination is not realized in any paper-direct candidate to date.

## Axiom α strict — 4-specialist consensus

| Discipline | Strict definition | Falsifiability |
|---|---|---|
| **NCG (S3)** | Unconditional Hilbert–Schmidt operator-norm bound on $\int E \, dt$ | Bound absent or RH-conditional $\implies$ NO |
| **Quantum physics (S6)** | Unbroken-phase energy bound with explicit thermalization model | Broken phase or absent $\zeta$ heat-flow physical model $\implies$ NO |
| **Analytic (S1)** | Mellin-transform–based closed bound | Combinatorial optimization barrier reached $\implies$ NO |
| **Logician (S9)** | ZFC-provable *constructive* bound (abstract equivalence ≠ enough) | ZFC-independent or *abstract equivalence only* $\implies$ NO |

Common essence: **unconditional + constructive + RH-independent**.

## Audit table — 4 paper-direct candidates

| # | Paper | Verdict | Paper-direct anchor |
|---|---|---|---|
| 1 | **Polymath15** (de Bruijn–Newman upper) | NO | Theorem 1.1 gives $\Lambda \leq 0.22$ as a *conditional* bound (3-tool combination: numerical RH + analytic asymptotic + barrier). Unconditional bound not provided. |
| 2 | **Rodgers–Tao 2020** ($\Lambda \geq 0$ unconditional) | NO | Paper §1.5 self-acknowledges: *"we are able to control integrated energies that resemble the quantities $\int_{\Lambda/2}^0 E(t) dt$"* — but this is **backward-time only** ($t \in [\Lambda/2, 0]$, not forward). Same §1.5: *"far from optimal"*. The forward direction is not given. |
| 3 | **Platt–Trudgian 2021** (RH up to $H = 3 \times 10^{12}$) | NO | Sharper $\Lambda \leq 0.2$ obtained *via numerical RH up to height $H = 3 \times 10^{12}$*. The improvement comes from extending numerical verification, not from a theoretical bound on $\int_0^\Lambda E(t) dt$. |
| 4 | **Newman 1976** ($\Lambda \leq 0 \iff \mathrm{RH}$) | NO | Definition only. The equivalence $\Lambda \leq 0 \iff \mathrm{RH}$ is *abstract* — it does not provide an unconditional upper bound on $\int E \, dt$. |

**Result: 4/4 axiom α strict NO. Status: $0 \leq \Lambda \leq 0.2$, with no closure mechanism.**

## Falsifier search — adjacent fields

The lemma searches 5+ adjacent fields for any source that might provide an unconditional ∫E(t)dt bound:

- **Bombieri–Lagarias 1999** — provides $\Lambda \geq 0$ *lower* bound only. Upper bound absent. *Not a falsifier.*
- **Selberg method (mollifier)** — addresses Wall #3 (50% barrier on critical-line zero density), not directly connected to ∫E(t)dt. *Not a falsifier.*
- **Bourgain–Gamburd–Sarnak expander** — heat semigroup *form-similar* but integrated-bound shape not present. *Not a falsifier.*
- **Otto's calculus / Wasserstein gradient flow** — the project's own attempt 007 (a separate cycle) verified that this approach is time-symmetric, while Wall #2 is fundamentally asymmetric (forward vs backward). *Not a falsifier.*
- **Concentration compactness (Lions–Brezis)** — provides limit-point analysis but not forward-time control. *Not a falsifier.*
- **Free probability R-transform** — addresses Wall #6 (LOCAL-GLOBAL-MISMATCH) axis, not Wall #2. *Not a falsifier.*

**No falsifier found across 5+ adjacent fields.**

## Specialist Δ — anchored to paper §-end quotes

**S1 (analytic number theory) — Tao + Conrey paraphrase:**
- Polymath15 §6 paper-direct: *"this is the limit of the present method"* — combinatorial-optimization internal ceiling.
- Iwaniec phrase *"extra little tiny bit"* (same essence as Wall #4) — empirical limit of the field.

**S5 (Tao, hard analysis) — Tao paraphrase:**
- Rodgers–Tao 2020 §1.5: *"we are able to control integrated energies that resemble the quantities $\int_{\Lambda/2}^0 E(t) dt$"* + *"far from optimal"*.
- The essential issue is **time-asymmetry**: Rodgers–Tao's method controls backward only.

**S6 (quantum physics):** No paper-direct anchor. The absence of a physical model for $\zeta$ heat flow is itself an anchor.

**S9 (logician):** Lagarias 2002 ($\mathrm{RH}$ is $\Pi_1$) — anchor for measuring axiom α's logical strength.

## Caveats (the project's own)

- Axiom α strict definition varies across NCG / quantum / analytic / logician viewpoints. The lemma uses 4-viewpoint consensus.
- **RH progress: 0/10.** Wall #2 *empirical-record codification*, not an obstruction theorem.
- The lemma's *real value*: a baseline + falsifier criterion for future Wall #2 work.
- Same logical structure as [Lemma 9](../12-lemma-axiom6-ceiling/) — empirical NO + falsifier survival + necessary unproven. The format-reuse is the project's evidence that the codification template is generalizable across walls.

## Falsifier criterion — what would retract this lemma

A single paper providing **all four** of the following retracts the lemma:

1. An **unconditional explicit upper bound** on $\int_0^\Lambda E(t) dt$ — paper-direct quote.
2. **RH not assumed** — paper-direct verification.
3. **Constructive form** (abstract equivalence ≠ enough) — paper-direct.
4. **No fine-tuning parameter** — paper-direct quote or parameter-free definition.

If all four are simultaneously paper-direct YES, the lemma retracts.

## What this is *not*

- **Not a proof** that no such bound can exist. The lemma is empirical (4 candidates + 5+ falsifier fields).
- **Not RH progress.** Wall #2 codification, not RH path.
- **Not closed under ZFC analysis.** Newman 1976's $\Lambda \leq 0 \iff \mathrm{RH}$ is *abstract* — whether axiom α has a constructive form provable in ZFC is undetermined.

## Why this codification might be useful

If a new Wall #2 paper appears, the four-item falsifier criterion runs in minutes:

1. Does the paper claim an unconditional bound? (vs. conditional like Polymath15)
2. Is RH not assumed? (vs. Newman's abstract equivalence)
3. Is the bound constructive? (vs. equivalence-only)
4. Is there no fine-tuning?

If any of these fails, the candidate stays in axiom α strict NO. If all four pass — the lemma retracts.

## Reading order

- For high-level narrative: see [Finding 2: Wall #2 unconditional bound 4/4 NO](../03-finding-wall2-bound/).
- For the parallel codification on Wall #5 (spectral self-adjoint): see [Lemma 9](../12-lemma-axiom6-ceiling/).
- For the project's broader context (Connes–Consani 2018→2021 progress relevant to path 1, distinct from Wall #2): see [Finding 3](../04-finding-connes-consani-progress/).

## Refuting / strengthening this lemma

If you have a paper providing an unconditional + constructive bound on $\int_0^\Lambda E(t) dt$, please email **x2ever.han@gmail.com**.

---

[← All English posts](../../) · [한국어](../../../ko/posts/13-lemma-wall2-axiom-alpha/)
