# Eleven-Axiom Ceiling for Hilbert-Pólya Candidates: 11/11 Universal NO Including UV-Asymptotic Prolate Operator (Connes-Moscovici 2022)

> **Status**: Preprint draft — cycle 7 of sustained research, Section 1+2 only.
> Sections 3-7 deferred to subsequent cycles.
> Internal use: cycles 1-6 externalization first manifest.

## Abstract (Cycle 6 outline 그대로)

We test eleven self-adjoint candidates for the Hilbert-Pólya program against an eleven-axiom strict criterion derived from four specialist viewpoints (operator algebra/NCG, RMT, quantum physics, logic). All eleven candidates fail axiom 6 (single Hamiltonian uniqueness, no fine-tune): paper-direct quotes from each candidate's source paper directly anchor each NO. We further verify that five external falsifier domains (Selberg trace, function field RH transfer, Berry quantum chaos, Atiyah, prolate UV-asymptotic) preserve the universal NO. The result is a paper-direct empirical universal NO for the current state of Hilbert-Pólya program (1998-2022).

## 1. Introduction

The Riemann Hypothesis (RH) — *all non-trivial zeros of the Riemann zeta function ζ(s) lie on the critical line Re(s) = 1/2* — has remained unproven since Riemann's 1859 paper [Riemann 1859]. Among the program-level approaches to RH, the Hilbert-Pólya conjecture (1914 letter to Landau) proposes a *spectral interpretation*: there exists a self-adjoint operator $H$ on a concrete Hilbert space such that the imaginary parts of the non-trivial zeros of ζ are exactly the eigenvalues of $H$. If such $H$ existed, the reality of its eigenvalues (a spectral theorem consequence) would directly imply RH.

Despite a century of effort, no rigorous Hilbert-Pólya candidate has been constructed. Notable attempts include:
- Berry-Keating's classical $H = xp$ proposal (1999).
- Bender-Brody-Müller (BBM) Hamiltonian (2017), with the eigenfunction $\psi_z(x) = -\zeta(z, x+1)$ trivially encoding ζ-zeros via boundary condition.
- Sierra's $xp$-model variants (2007, 2016).
- Connes' adelic spectral interpretation (1999).
- Connes-Consani arithmetic site framework (2014+).
- Connes-Moscovici prolate spheroidal operator UV spectrum (2022, PNAS).

We refer to this collective body of attempts as the *Hilbert-Pólya program* and use *Wall #5 (SELF-ADJOINT-RIGOR)* (after [internal taxonomy]) for the recurrent obstacle: *no paper-direct candidate satisfies a strict criterion for being a single, fine-tune-free, fully self-adjoint operator whose spectrum captures all non-trivial ζ-zeros*.

In the present paper, we make this informal observation precise. We define eleven axioms (Section 2), each derived as the *strict union* of four specialist viewpoints (operator algebra / NCG, RMT, quantum physics, logic), and we audit eleven paper-direct candidates against the *strict version* of axiom 6 (single Hamiltonian uniqueness). We find:

> **Main observation (paper-direct empirical)**: All eleven candidates fail axiom 6 (strict). Each NO is anchored by a *direct quote* from the candidate's source paper, including the most recent published candidate (Connes-Moscovici 2022 prolate operator), which fails axiom 6 due to two specific fine-tune values $\lambda \in \{1, \sqrt{2}\}$ and deficiency indices (4, 4) admitting multiple self-adjoint extensions.

We do *not* claim a proof of necessity; the observation is empirical, restricted to the 1998-2022 Hilbert-Pólya literature we have audited. Section 6 discusses the gap between *empirical* and *necessary* universal NO, and the open question of ZFC-independence.

The point of this paper is to *codify* the current paper-direct status of the Hilbert-Pólya program, to provide a *falsifier criterion* for future candidates (any future candidate satisfying axiom 6 strict YES would refute this observation), and to frame the next steps for the program: either *find such a candidate* (construct $H$ rigorously) or *prove the impossibility* of a single fine-tune-free operator.

## 2. Eleven-Axiom Strict Definition

We define an *eleven-axiom strict criterion* for a Hilbert-Pólya candidate $H$. Each axiom is the *strict union* of four specialist interpretations (each individually strong; the union is strongest). A candidate $H$ satisfies axiom $k$ (strict) iff $H$ satisfies axiom $k$ under *all* four specialist viewpoints simultaneously.

### Specialist Viewpoints

- **S3 (Operator Algebra / NCG)**: standard Hilbert space and self-adjoint extension framework, à la Connes' adelic program.
- **S4 (Random Matrix Theory)**: GUE/CUE eigenvalue distribution and statistics, à la Montgomery-Odlyzko-Keating-Snaith.
- **S6 (Quantum Physics, PT-symmetric)**: $H$ as a physical Hamiltonian, Bender-Boettcher PT-symmetric framework, pseudo-Hermitian inner product (Mostafazadeh).
- **S9 (Logician)**: ZFC formal definability and provability.

### The Eleven Axioms

| # | Axiom (strict) |
|---|---|
| 1 | **Asymptotic match**: the smooth-part counting function $N_H(E)$ of $H$'s spectrum agrees with the Riemann counting $N_\zeta(E) \sim (E/2\pi)(\log(E/2\pi) - 1)$ to leading order. |
| 2 | **Zero-spectrum identification**: there exists a bijection between non-trivial ζ-zeros $\{\rho_n\}$ and eigenvalues of $H$ (under all four specialist viewpoints simultaneously); RH is *not* assumed in this identification. |
| 3 | **Self-adjoint extension on a concrete Hilbert space**: $H$ extends uniquely (or with explicit unitary parameter) to a self-adjoint operator on a *concrete*, paper-stated Hilbert space. |
| 4 | **Eigenvalues real (RH-conditional)**: the eigenvalues of $H$ are real (under RH or unconditionally, as paper-stated). |
| 5 | **Domain explicit**: the domain of $H$ is explicit (Schwartz space, $L^2$ subspace, etc.). |
| 6 | **Single Hamiltonian uniqueness, no fine-tune**: there exists *one* canonical operator $H$ on *one* canonical Hilbert space, *capturing all ζ-zeros simultaneously*, *without* fine-tuning a parameter (boundary angle $\vartheta$, Sobolev exponent $\delta$, deformation $\lambda$, etc.). |
| 7 | **Eigenvalues real (RH-equivalent claim)**: the reality of all $H$-eigenvalues is paper-stated as RH-equivalent (one direction is provable from rigor of $H$). |
| 8 | **Normalizable**: eigenfunctions are square-integrable on the chosen Hilbert space. |
| 9 | **Domain explicit (paper-quoted)**: paper provides explicit equation defining $\text{Dom}(H)$. |
| 10 | **Symmetry (PT/CP/T)**: $H$ has a paper-stated symmetry (parity, time-reversal, PT, CP, etc.) compatible with the eigenvalue reality. |
| 11 | **Biorthogonal completeness**: in the PT-symmetric or $\eta$-pseudo-Hermitian framework, the eigenbasis is *complete and biorthogonal*; in the Hermitian framework, the eigenbasis is *complete orthonormal*. |

### Axiom 6 in Detail (the Ceiling Axiom)

Axiom 6 captures the *single point of universal NO* across all eleven candidates we audit (Section 3). The strict definitions across four viewpoints converge:

- **NCG (S3)**: $\exists$ a single self-adjoint $D$ on a fixed Hilbert space $\mathcal{H}$, with $\text{Sp}(D) \leftrightarrow \{\rho_n\}$ a bijection, *no fine-tune parameter*.
- **PT physics (S6)**: $\exists$ a single PT-symmetric $H$ in *unbroken PT phase* (eigenvalues real), with biorthogonal complete eigenbasis labeled by $\{\rho_n\}$, *no fine-tune*.
- **Analytic (S1)**: $\exists$ a *single* mollifier-style transform (Levinson/Conrey extension) capturing all zeros simultaneously (not a *family* of mollifiers).
- **Logician (S9)**: ZFC proves $\exists !\, H : \text{Sp}(H) \cap i\mathbb{R} = i \cdot \{\text{Im} \rho_n\}$, *constructively*.

A candidate satisfies axiom 6 (strict) iff *all four* viewpoints' definitions are simultaneously paper-direct YES.

### Falsifier of the Universal NO

The *falsifier* of our main observation is a *single paper-direct candidate* that satisfies axiom 6 (strict) under all four viewpoints. We have audited the 1998-2022 published candidates we are aware of (BBM, Sierra×3, Connes×2, Connes-Consani, Lagarias §8 hypothetical, Berry-Keating, Sierra 2007 Jost, Connes-Moscovici 2022 prolate); none satisfies axiom 6 (strict). The audit is presented in Section 3.

## (Sections 3-7 deferred to subsequent cycles)

Section 3 (Eleven-candidate audit), Section 4 (Universal NO 11/11 result with paper-direct quote table), Section 5 (Five-domain falsifier search), Section 6 (Empirical vs necessary, ZFC-independence open), Section 7 (Cycle protocol meta — sustained research methodology) will be expanded in cycles 8-12 of the sustained research protocol.

---

## Internal Notes (cycle 7 work, not for preprint submission)

### Paper-Direct Anchors (Section 1 + 2)

- Section 1 reference list: Riemann 1859, BBM 2017, Sierra 2007, Sierra 2016, Berry-Keating 1999, Connes 1999 §III, Connes-Consani 2021 §1, Connes-Moscovici 2022 (PNAS, arxiv 2112.05500).
- Section 2 axiom definitions: cycle 1 work.md (10 candidates × 11-axiom audit), cycle 6 work.md (prolate 11th candidate), `lemmas/spectral_candidate_circularity_check.md`, `lemmas/lemma1_axiom6_ceiling.md`.

### Honest Limitations (paper §6 candidates)

- Empirical universal NO only — *not* necessary universal NO (S9 logician 경고 cycles 1-6).
- ZFC-independence open.
- Audit limited to 1998-2022, may miss pre-1998 or non-published candidates.
- "Paper-direct" criterion = directly quoted from candidate's own paper, may miss reinterpretations.

### Next Steps

- Cycle 8: Section 3 audit table 본문 (11 candidates × 11 axioms full table).
- Cycle 9: Section 4 universal NO result + paper-direct quote table (47+ quotes catalog 활용).
- Cycle 10: Section 5 falsifier search (5 분야 cycle 2+).
- Cycle 11: Section 6 honest limit (necessary vs empirical, ZFC).
- Cycle 12: Section 7 cycle protocol meta (sustained research methodology).
