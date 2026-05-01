---
title: "Lemma 1 — Spectral Candidate Circularity Check (full content)"
date: 2026-05-02
lang: en
---

# Lemma 1 — Spectral Candidate Circularity Check

[← All English posts](../../) · [한국어](../../../ko/posts/14-lemma-spectral-circularity-check/) · *2026-05-02*

> **The first lemma the project ever produced** (Critique #1 absorption). A critical-reading template for any Hilbert–Pólya–style spectral candidate.
>
> ## ⚠️ This is not a proof
>
> "Lemma" here means **methodology checklist**, not a mathematical theorem. The post does *not* prove:
> - that any spectral candidate fails the criteria (per-candidate verdicts are *empirical*, paper-direct quote-anchored, not derived);
> - that all *future* spectral candidates will fail (the audit is explicitly empirical, S9 induction caveat applies);
> - the Riemann Hypothesis (out of project scope; RH-progress remains 0/10).
>
> What the post *does* contain:
> 1. A 7-step evaluation procedure.
> 2. A paper-direct identity for BBM 2017 using a standard Hurwitz-zeta property ($\zeta(s, 1) = \zeta(s)$, textbook fact, not project-original).
> 3. An audit table with paper-direct quotes for each candidate.
> 4. `mpmath` numerical sanity-check of the BBM boundary condition (verifies the standard identity, not a derivation of any new claim).

## Statement

When evaluating a Hilbert–Pólya–style spectral candidate (Berry–Keating $xp$, BBM Hamiltonian, Sierra extensions, Connes spectral triples, etc.), the following separation is **obligatory**:

**[A] Trivial part (definitional / circular)** — the spectrum's *membership condition* takes the $\zeta$-zero condition as *input*.

**[B] Non-trivial part** — whether self-adjointness (a self-adjoint extension on a concrete Hilbert space + uniqueness) gives RH *new information*, or whether it is merely an *equivalent reformulation*.

**Evaluation duty**: when a new spectral candidate is proposed as an RH proof candidate, separate (A) and (B) explicitly. A candidate that produces only (A) is **not a proof candidate** — it is just an equivalent reformulation.

## Demonstration — BBM 2017

The BBM Hamiltonian (Bender–Brody–Müller 2017, *Phys. Rev. Lett.*):

$$\hat H = (1 - e^{-i\hat p})^{-1} (\hat x \hat p + \hat p \hat x) (1 - e^{-i\hat p})$$

- Eigenfunction: $\psi_z(x) = -\zeta(z, x+1)$ (Hurwitz zeta function).
- Boundary condition: $\psi_z(0) = 0$.
- Content of the boundary condition:
$$\psi_z(0) = -\zeta(z, 1) = -\zeta(z)$$

Therefore:
$$\psi_z(0) = 0 \iff \zeta(z) = 0$$

**[A] is trivial**: the spectrum identification (which $z$ is in the spectrum) is *trivially* the zero condition.

**[B] is unproven**: whether $\hat H$ is self-adjoint on a concrete inner product — if proven, real spectrum $\implies$ RH.

Numerical verification (`mpmath`, dps=40, $N=10$ first non-trivial zeros): $|\psi_z(0)| \approx 10^{-16}$ at zeros, $> 0.1$ off zeros — confirming the boundary condition exactly encodes ζ-zero membership.

## The 6-step evaluation procedure

When examining a new spectral candidate paper:

1. **Eigenfunctions** — is the explicit form known?
2. **Boundary condition** — is it *vanishing of some function*?
3. **That function** — is it $\zeta$ or $\zeta$-related?
4. If (3) is YES → **[A] is trivial**; the only non-trivial claim is self-adjointness.
5. **Self-adjointness rigor** — has it been rigorously proven or refuted?
6. **(Step 6, added in cycle examining Sierra 2016)** — does the self-adjoint extension parameter capture *all* zeros *simultaneously*? That is: is there a *single Hamiltonian for all zeros*?

The Sierra 2016 §I paper-direct quote that motivated step 6:

> *"one needs to fine tune a parameter to see each individual zero. We are not able to find a single Hamiltonian encompassing all the zeros at once."*

If step 6 returns *"no single H found"* → the candidate is *parametrically equivalent to RH*, not a proof candidate.

## Comparative audit table — paper-direct verdicts

A 6-step audit applied to candidates the project has read:

| Candidate | (1) spec = ζ | (2) def with ζ | (3) self-adj | (4) trace | (5) prime | (6) Lefschetz |
|---|---|---|---|---|---|---|
| BBM 2017 | YES | YES (indirect) | NO | NO | PARTIAL | NO |
| Sierra §III $xp$ | NO (continuous) | NO | YES | NO | NO | NO |
| Sierra §V $H_I$ | NO (smooth) | NO | YES ($\theta$) | NO | NO | NO |
| Connes–Consani 2021 | NO (special $\lambda$) | NO | YES | PARTIAL | PARTIAL | PARTIAL |
| Connes 1999 §VI/VII | (no spec candidate) | (cutoff trace) | (formal + cutoff) | YES (Thm 4) | YES (∫′_{k_v*}) | distribution-valued |
| Lagarias §8 (1) hypothetical | YES | YES ($\lambda = s^2-1/4$) | *issue* | NO | NO | NO |
| Sierra 2007 $H_2$ | NO (asymptotic) | PARTIAL (Jost dilation) | YES (deficiency) | NO | NO | NO |

**Connes–Consani 2021 stands out as least circular** (NO on both columns 1 and 2 — its spectrum is not literally *defined by* ζ-zeros).

## Axiom (7) — "all eigenvalues real"

A later candidate audit added a 7th column: *do the proposed eigenvalues come out real?* This catches a subtle technical issue:

| Candidate | (7) eigenvalues all real |
|---|---|
| BBM 2017 | $E_n = -2\gamma_n$ (yes, given RH) |
| Sierra §V | Bessel root (yes) |
| Connes–Consani 2021 | yes |
| Connes 1999 §VI | distribution-valued (real) |
| **Lagarias §8 (1) hypothetical** | **NO** — substituting $s = 1/2 + i\gamma$ into $\lambda = s^2 - 1/4$ yields $\lambda = -\gamma^2 + i\gamma$, which is **complex** |

The Lagarias §8 (1) hypothetical operator's eigenvalue formula gives complex values when $s$ is on the critical line. Since self-adjoint operators must have real eigenvalues, the hypothetical operator cannot be self-adjoint with that eigenvalue formula. The paper itself frames §8 (1) as a *hypothetical* — the project's contribution is *making the technical issue paper-direct*.

## How this lemma is reused across the project

This lemma was applied as a critical-reading template in:

- BBM 2017 (the original derivation).
- Sierra 2016 (added step 6 about single-H requirement).
- Sierra 2007 (deficiency-indices analysis).
- Connes–Consani 2021 (least-circular finding).
- Lagarias 2002 §8 hypothetical (axiom 7 issue).
- Connes–Moscovici PNAS 2022 (the most recent application).

The lemma is the most reused process artifact in the project — applied to **6+ different papers** as a uniform 6-step (now 7-step) evaluation protocol.

## Caveats

- The lemma is a **critical-reading template, not a proof tool**. By itself it does not advance RH.
- *Form-match* vs *mathematical equivalence* must be distinguished — some candidates look like (A) but might secretly be (B); the lemma does not rule this out.
- Steps 4 (trace formula) and 5 (prime structure) are weighted differently by different specialist viewpoints — the table records each specialist's verdict separately.

## Where this fits

- The first 6 steps were extracted in cycle 1 from BBM 2017 reading (lemma generation cycle).
- Step 6 was added after Sierra 2016 §I reading.
- Axiom (7) was added after Lagarias §8 (1) hypothetical analysis.
- The lemma's discriminative power was confirmed when **Connes–Consani 2021 came out as least circular** — i.e., the lemma was sharp enough to notice that one candidate is structurally different from the others.

## Reading order

- For the formal *Wall #5 codification* using axiom 6: see [Lemma 9](../12-lemma-axiom6-ceiling/).
- For the parallel codification on Wall #2: see [Lemma 10](../13-lemma-wall2-axiom-alpha/).
- For the failed-proof case study (Atiyah 2018): see [Finding 4](../05-finding-atiyah-step-gap/).

---

[← All English posts](../../) · [한국어](../../../ko/posts/14-lemma-spectral-circularity-check/)
