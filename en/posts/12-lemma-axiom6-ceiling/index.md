---
title: "Lemma 9 — Axiom-6 universal NO across 11 Hilbert-Pólya candidates (full content)"
date: 2026-05-02
lang: en
---

# Lemma 9 — Axiom 6 (Single Hamiltonian Uniqueness) Universal NO

[← All English posts](../../) · [한국어](../../../ko/posts/12-lemma-axiom6-ceiling/) · *2026-05-02*

> **The full process lemma**, embedded directly. Source: Cycle 1 (initial draft) + Cycle 6 (PNAS 2022 retroactive falsifier test, candidate #11 added).

> ## Status disclaimer
>
> *Empirical* universal NO. *Necessary* universal NO is **not proven** — the project's S9 (logician) caveat: induction from 165 years of empirical NO to all-future-candidates NO is a leap. ZFC-independence is not ruled out.
>
> Wall mapping: this lemma is the paper-direct quantitative codification of **Wall #5 (SELF-ADJOINT-RIGOR)**.

## Statement

Of 11 paper-direct Hilbert-Pólya–style spectral candidates audited, **the count satisfying axiom 6 strict is zero**.

> **A *single* self-adjoint operator $H$ on a *fixed* Hilbert space, capturing *all* non-trivial $\zeta$-zeros *bijectively*, with *no fine-tuning parameter*** — this strict combination is not realized in any paper-direct evidence to date.

## Axiom 6 strict — 4-specialist consensus definition

The "strict YES" criterion is the simultaneous agreement of four discipline-specific definitions:

| Discipline | Strict definition | Falsifiability condition |
|---|---|---|
| **NCG (S3)** | A single self-adjoint $D$ on fixed $H$, all $\zeta$-zeros $\leftrightarrow \mathrm{Sp}(D)$ bijective, no fine-tune | Any $\zeta$-zero missing from $\mathrm{Sp}(D) \implies$ NO |
| **Quantum physics (S6)** | Single PT-symmetric $H$, *unbroken* PT phase, biorthogonal complete eigenbasis, eigenvalues bijective $\leftrightarrow \zeta$-zero imaginary parts | Broken PT or fine-tune $\implies$ NO |
| **Analytic (S1)** | A *single* mollifier-method transformation (Levinson-style) capturing all zeros | Mollifier *family* required $\implies$ NO (Pratt-Robles 50% barrier) |
| **Logician (S9)** | ZFC-provable *"$\exists$ unique $H : \mathrm{Sp}(H) = $ {imag parts of $\zeta$-zeros}"* | Existence without uniqueness, or ZFC-independent $\implies$ NO |

Common essence across the four: **no fine-tuning** + **simultaneous capture of all zeros**.

## Audit table — 11 paper-direct candidates

Each row's anchor is a direct quotation from the candidate's source paper.

| # | Candidate | Verdict | Paper-direct anchor |
|---|---|---|---|
| 1 | **BBM 2017** (Bender–Brody–Müller, *Phys. Rev. Lett.*) | NO | Paper itself: *"We are not yet able to prove eigenvalues real"*. Boundary condition $\psi_z(0) = -\zeta(z, 1) = -\zeta(z)$, so $\psi_z(0) = 0 \iff \zeta(z) = 0$ — spectrum identification is *trivially* the zero condition (Lemma 1 Step 6, BBM circular). |
| 2 | **Sierra §III** $xp$ (Berry–Keating-type) | NO | Continuous spectrum on the real line — *no point spectrum*. Cannot capture discrete $\zeta$-zeros. |
| 3 | **Sierra §V** $H_I$ | NO | Self-adjoint extension via parameter $\theta \in [0, 2\pi)$ — explicit fine-tune. Sierra 2016 §I: *"not able to find a single Hamiltonian encompassing all the zeros at once"*. |
| 4 | **Sierra 2007** $H_2$ | NO | Deficiency indices $(1,1)$, self-adjoint *family* parameterized by $1 \times 1$ unitary (Table 2). One operator per choice, not a single canonical operator. |
| 5 | **Connes–Consani 2021** $\Theta(\lambda, k)$ | NO | Special $\lambda$ values *only*; for $\lambda^2 = 10.5, k = 18$, the first 31 zeros match with random-coincidence probability $\sim 10^{-50}$ — but the spectrum agrees only at *specific parameter choices*, not for all zeros simultaneously. |
| 6 | **Connes 1999** §VI/VII | NO | Paper introduction: *"unnatural parameter $\delta$"* — $\delta$-family of operators, not unique. |
| 7 | **Lagarias 2002** §8 (1) hypothetical | NO | Paper §8 hypothetical: $\lambda = s^2 - 1/4$. Substituting $s = 1/2 + i\gamma$ gives $\lambda = -\gamma^2 + i\gamma$, *complex* — incompatible with self-adjoint operator's real spectrum. Paper itself frames §8(1) as hypothetical. |
| 8 | **Berry–Keating 1999** $H = xp$ | NO | Sierra 2007 §I quote: *"no concrete proposal realizing all conditions"*. Even Berry–Keating's own 1999 paper §II frames $xp$ as a heuristic, not a rigorous candidate. |
| 9 | **Sierra 2007** §VI $\zeta_H$ Jost | NO | M2 family of $(a, b)$ potentials — many operators, not a single one. |
| 10 | **Connes 1999** §III $(\mathcal{H}_\chi, D_\chi)$ | NO | Paper §III + introduction: *"$\delta > 1$ Sobolev exponent — unnatural"*. $\delta$-family. |
| 11 | **Connes–Moscovici 2022** ($W_{\mathrm{sa}}$, *PNAS*) | NO | UV asymptotic only — the paper's own abstract says *"ultraviolet behavior reproduces"* (not exact spectrum match). $\lambda \in \{1, \sqrt{2}\}$ fine-tuning (paper §1). Lemma 2.1: deficiency indices $(4, 4)$ — multiple self-adjoint extensions, no single canonical $H$. |

**Result: 11/11 axiom 6 strict NO.**

## Falsifier search — adjacent fields

Beyond the 11 direct candidates, the lemma searches 5+ adjacent fields for any operator that might satisfy axiom 6 strict:

- **Selberg trace formula** candidates — Selberg's $\zeta$ on hyperbolic surfaces $\neq$ Riemann's $\zeta$ (length spectrum vs prime spectrum). The adelic version is candidate #5 above. *Not a falsifier.*
- **Function field RH** (Weil 1948 / Deligne 1974) — function-field side has axiom 6 YES (Frobenius eigenvalues), but the **number field side requires Wall #1 cohomological transfer**, which is a separate fundamental gap. *Not a falsifier* on the number field side.
- **Berry's modified $H$**, quantum chaos "dressed" Hamiltonians — explicit single-$H$ constructions not found in the literature. *Not a falsifier.*
- **Atiyah 2018 Todd-function approach** — see [Finding 4](../05-finding-atiyah-step-gap/) for the explicit gap. *Not a falsifier.*
- **Connes–Moscovici 2022 (PNAS)** — the Cycle 6 retroactive test, see candidate #11 above. *Not a falsifier* (UV asymptotic + fine-tune + multiple extensions).

**No falsifier found across 5+ adjacent fields + 11 direct candidates.**

## What this is *not*

- **Not a proof** that no such operator can exist. The lemma is *empirical* — across 11 candidates audited and 5+ falsifier domains searched, none satisfies axiom 6 strict.
- **Not closed under ZFC analysis.** RH is $\Pi_1$ (Lagarias 2002). The logical strength of the universal-NO statement is undetermined; ZFC-independence is possible.
- **Not RH progress.** The lemma is RH's *language change* — codification of an obstacle pattern, not a path to resolution. The lemma's `Caveats` block explicitly says this.

## Falsifier criterion — what would retract this lemma

The lemma is *falsifiable*. A single paper-direct candidate satisfying **all three** of the following retracts the lemma:

1. **Single $H$ on a fixed Hilbert space** — paper-direct quote.
2. **All $\zeta$-zeros $\leftrightarrow \mathrm{Sp}(H)$ bijective** — paper-direct verification.
3. **No fine-tuning parameter** — paper-direct quote or explicit parameter-free definition.

If all three are simultaneously paper-direct YES for any single new candidate, the lemma retracts and the cycle that produced it is retroactively corrected.

## Why this codification might still be useful

The lemma is a **structured checklist** future spectral candidates can be tested against systematically. The falsifier criterion is explicit, so applying the lemma to a new paper takes minutes:

1. Read the paper's main spectral candidate definition.
2. Check whether the operator is a *single* operator or a parameterized family.
3. Check whether the spectrum is claimed to match *all* $\zeta$-zeros (not just asymptotically).
4. Check whether any parameter was fine-tuned to make the match work.

If any of (2–4) fails, the candidate is axiom 6 strict NO.

## Reading order

- For the high-level narrative: see [Finding 1: 11/11 axiom-6 ceiling](../02-finding-axiom6-ceiling/).
- For the falsifier-criterion application that produced candidate #11: see Cycle 6's reading of Connes–Moscovici 2022 (referenced in [Cycles 8–11 update](../10-update-cycles-8-11/)).
- For the parallel codification on Wall #2 (forward heat flow): see [Lemma 10](../13-lemma-wall2-axiom-alpha/).

## Refuting / strengthening this lemma

If you have a paper-direct candidate that strict-passes axiom 6 — please email **x2ever.han@gmail.com**. The lemma is genuinely falsifiable.

---

[← All English posts](../../) · [한국어](../../../ko/posts/12-lemma-axiom6-ceiling/)
