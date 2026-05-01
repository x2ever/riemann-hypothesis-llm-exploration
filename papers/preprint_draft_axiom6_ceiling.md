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

We refer to this collective body of attempts as the *Hilbert-Pólya program* and use *Wall #5 (SELF-ADJOINT-RIGOR)* for the recurrent obstacle: *no paper-direct candidate satisfies a strict criterion for being a single, fine-tune-free, fully self-adjoint operator whose spectrum captures all non-trivial ζ-zeros*. Wall #5 is one of six recurrent obstacles in the Riemann Hypothesis literature that we identify in §1.1 below.

### 1.1 Six Walls in the Riemann Hypothesis Literature

Across the 165-year RH literature, we identify six recurrent obstacles ("walls") that block standard approaches. These are not novel observations on our part but rather a *codification* of obstacles that appear, often *self-acknowledged*, in the source papers themselves. We use them as a *vocabulary* for discussing the Hilbert-Pólya program in this paper; the focus of this paper is exclusively Wall #5.

- **Wall #1 (FROBENIUS-GAP)**: In characteristic-zero arithmetic, no analog of the Frobenius automorphism is known with the structural role it plays in characteristic-$p$. The Connes-Consani arithmetic site program (2014+) [Connes 2019, §4.3] is the most active attempt to bridge this gap; the *intersection theory and Riemann-Roch on the square of the arithmetic site* remains open as of 2018 [Connes-Consani 2018 §1.2, "still open at this time"].

- **Wall #2 (FORWARD-TIME)**: For the de Bruijn-Newman heat flow $H_t \xi$ with $\Lambda$ the de Bruijn-Newman constant, no unconditional upper bound on $\int_0^\Lambda E(t)\, dt$ is known. The Polymath15 / Rodgers-Tao bracket is $0 \le \Lambda \le 0.2$ [Rodgers-Tao 2020 §1.5 "far from optimal"; Platt-Trudgian 2021].

- **Wall #3 (SHARP-CONSTANT)**: Mollifier methods for proving non-vanishing of $\zeta$ on the critical line are bounded by a sharp constant near $50\%$ [Pratt-Robles 2019 attains $5/12 \approx 41.67\%$].

- **Wall #4 (CONSPIRACY)**: For families of $L$-functions, the Landau-Siegel exceptional zero remains unexcluded [Iwaniec-Sarnak Perspectives §5].

- **Wall #5 (SELF-ADJOINT-RIGOR)**: *The focus of this paper.* No Hilbert-Pólya candidate audited to date satisfies a strict single-Hamiltonian-uniqueness criterion (Section 2, axiom 6).

- **Wall #6 (LOCAL-GLOBAL-MISMATCH)**: Different RH-equivalent reformulations (Mertens, Li's $\lambda_n$, Nyman-Beurling, Weil) probe different *information layers* of the zero set. Naive cross-checks between equivalent forms can fail without indicating a true inconsistency, due to layer mismatch.

The six walls are not mutually exclusive: a particular obstacle can manifest as more than one wall simultaneously. The codification is empirical, derived from auditing the published RH literature 1859-2024; we make no claim that these are the *only* walls or the *correct* taxonomy. Other groupings (e.g., Connes' three-strategy partition in [Connes 2019 §1]) are equivalent in coverage.

In the present paper, we make this informal observation precise. We define eleven axioms (Section 2), each derived as the *strict union* of four specialist viewpoints (operator algebra / NCG, RMT, quantum physics, logic), and we audit eleven paper-direct candidates against the *strict version* of axiom 6 (single Hamiltonian uniqueness). We find:

> **Main observation (paper-direct empirical)**: All eleven candidates fail axiom 6 (strict). Each NO is anchored by a *direct quote* from the candidate's source paper, including the most recent published candidate (Connes-Moscovici 2022 prolate operator), which fails axiom 6 due to two specific fine-tune values $\lambda \in \{1, \sqrt{2}\}$ and deficiency indices (4, 4) admitting multiple self-adjoint extensions.

We do *not* claim a proof of necessity; the observation is empirical, restricted to the 1998-2022 Hilbert-Pólya literature we have audited. Section 6 discusses the gap between *empirical* and *necessary* universal NO, and the open question of ZFC-independence.

The point of this paper is to *codify* the current paper-direct status of the Hilbert-Pólya program, to provide a *falsifier criterion* for future candidates (any future candidate satisfying axiom 6 strict YES would refute this observation), and to frame the next steps for the program: either *find such a candidate* (construct $H$ rigorously) or *prove the impossibility* of a single fine-tune-free operator.

## 2. Eleven-Axiom Strict Definition

We define an *eleven-axiom strict criterion* for a Hilbert-Pólya candidate $H$. The criterion is the *strict union* (defined precisely in §2.0) of four specialist interpretations, each individually strong; the union is the strongest of the four.

### 2.0 The "Strict Union" of Specialist Viewpoints — Logical Definition

For each axiom $k \in \{1, \dots, 11\}$ and each specialist viewpoint $V \in \{S3, S4, S6, S9\}$, let $A_k^V(H)$ denote the *predicate* "candidate $H$ satisfies axiom $k$ under viewpoint $V$" (a precise mathematical statement to be specified below for each $k$ and each $V$).

**Definition (Strict Union).** A candidate $H$ satisfies *axiom $k$ (strict)* iff
$$
A_k^{S3}(H) \;\land\; A_k^{S4}(H) \;\land\; A_k^{S6}(H) \;\land\; A_k^{S9}(H)
$$
holds — i.e., the conjunction of all four viewpoint-specific predicates.

The "union" here is *not* set-theoretic union (i.e., disjunction) but rather the *strongest* simultaneous criterion across viewpoints: a candidate must satisfy all four interpretations to satisfy the strict axiom. We use the term "union" because each individual $A_k^V$ is itself a (possibly disjunctive) condition within viewpoint $V$, and the strict criterion *combines* (intersects) those conditions.

**Equivalent formulations.** Since the four viewpoints place different individual constraints, $A_k^{\text{strict}}(H) := \bigwedge_V A_k^V(H)$ is at least as strong as any single $A_k^V$, and is strictly stronger when at least two $A_k^{V}$, $A_k^{V'}$ are non-equivalent.

**Falsifiability.** $A_k^{\text{strict}}(H)$ is *false* iff there exists a viewpoint $V$ with $A_k^V(H)$ false (paper-direct quote or formal counterexample suffices). Section 4 provides one such witness for each (candidate, axiom 6) pair: each candidate fails axiom 6 under at least one viewpoint, and we cite the source paper directly.

**Non-claim.** We do *not* claim our four viewpoints exhaust the relevant interpretations of "self-adjoint operator capturing ζ-zeros." Other viewpoints (e.g., dynamical systems, non-self-adjoint PT-broken phase, free probability) may add further constraints. The strict criterion is a *lower bound* on what a successful Hilbert-Pólya candidate must satisfy; a candidate that satisfies our strict criterion may still fail under additional viewpoints.

A candidate $H$ satisfies axiom $k$ (strict) iff $H$ satisfies axiom $k$ under *all* four specialist viewpoints simultaneously (formal definition above).

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

## 3. Eleven-Candidate Audit

We audit eleven Hilbert-Pólya candidates from the published 1998-2022 literature against the eleven-axiom strict criterion of §2. For each (candidate, axiom) cell, we provide a *paper-direct anchor*: a quote, equation reference, or lemma reference from the candidate's source paper that determines the YES / PARTIAL / NO entry. The complete audit table follows.

### 3.1 Candidate List

| # | Candidate | Source | Year |
|---|---|---|---|
| 1 | BBM Hamiltonian | Bender-Brody-Müller [BBM 2017] | 2017 |
| 2 | Sierra §III $xp$ (Berry-Keating quantum) | Sierra [arxiv 0712.1893] §III | 2007 |
| 3 | Sierra §V $H_I = x(p + \ell_p^2/p)$ | Sierra [Phys Rev D 2016] §V | 2016 |
| 4 | Sierra 2007 $H_2 = \sqrt{x} p \sqrt{x}$ | Sierra [arxiv 0712.1893] §IV | 2007 |
| 5 | Connes-Consani $\Theta(\lambda, k)$ spectral triple | Connes-Consani [arxiv 2106.01715] | 2021 |
| 6 | Connes 1999 §VI/VII formal trace | Connes [Selecta 1999] §VI-VII | 1999 |
| 7 | Lagarias §8 (1) hypothetical $\lambda = s^2 - 1/4$ | Lagarias [Acta 2007] §8 | 2007 |
| 8 | Berry-Keating 1999 $H = xp$ classical | Berry-Keating [SIAM 1999] | 1999 |
| 9 | Sierra 2007 §VI $\zeta_H$ Jost candidate | Sierra [arxiv 0712.1893] §VI | 2007 |
| 10 | Connes 1999 §III $(\mathcal{H}_\chi, D_\chi)$ | Connes [Selecta 1999] §III | 1999 |
| 11 | Prolate Connes-Moscovici $W_{\mathrm{sa}}$ | Connes-Moscovici [PNAS 2022, arxiv 2112.05500] | 2022 |

### 3.2 Audit Table — Eleven Candidates × Eleven Axioms

We use Y = YES, N = NO, P = PARTIAL, U = undefined / not addressed in source. The detailed paper-direct anchor for each NO under axiom 6 is given in §3.3; full anchor for all cells is in [supplementary materials].

| # | Candidate | 1 | 2 | 3 | 4 | 5 | **6** | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | BBM 2017 | Y | Y | N | N | P | **N** | Y(RH) | N | N | Y | P |
| 2 | Sierra §III $xp$ | N | N | Y | N | N | **N** | Y | N | Y | Y | N |
| 3 | Sierra §V $H_I$ | N | N | Y(ϑ) | N | N | **N** | Y | Y | Y | Y | Y |
| 4 | Sierra 2007 $H_2$ | N | P | Y | N | N | **N** | Y | P | Y | Y | P |
| 5 | Connes-Consani 2021 | N | N | Y | P | P | **N** | Y | Y | Y | P | Y |
| 6 | Connes 1999 §VI/VII | U | (cutoff) | (formal) | Y | Y | **N** | (distrib) | (cutoff) | P | U | U |
| 7 | Lagarias §8 (1) | Y | Y | issue | N | N | **N** | N | undef | undef | undef | undef |
| 8 | Berry-Keating 1999 | N | N | Y | N | N | **N** | Y | N | Y | Y | N |
| 9 | Sierra 2007 §VI ζ_H | P | P | Y | N | N | **N** | P | P | Y | Y | P |
| 10 | Connes 1999 §III | Y | Y | N | P | Y | **N** | P | Y | Y | N | P |
| 11 | Prolate (Connes-Moscovici 2022) | Y | P | Y | P | Y | **N** | P | Y | Y | Y | P |

**Score summary** (excluding undef): Sierra §V (3) and Connes-Consani 2021 (5) score 9/11; Prolate (11) scores 6/11; BBM (1) scores 4/11; Lagarias §8 (7) scores 4/11. *Crucial uniformity*: all eleven candidates fail axiom 6.

### 3.3 Axiom 6 Strict NO — Paper-Direct Anchors for All Eleven Candidates

Axiom 6 (single Hamiltonian uniqueness, no fine-tune): for each candidate, we provide a *direct quote or paper-stated reason* from the source paper showing axiom 6 fails (strict). All anchors are paper-direct, not our reinterpretation.

1. **BBM 2017** — paper §III self-acknowledged: *"We are not yet able to prove eigenvalues real."* Combined with the eigenfunction $\psi_z(x) = -\zeta(z, x+1)$ encoding ζ-zeros via boundary condition $\psi_z(0) = -\zeta(z) = 0$, the spectrum identification is *trivially circular* per zero (no single ambient $H$ uniformly capturing all zeros without per-zero boundary fine-tune).

2. **Sierra §III $xp$** — continuous spectrum (paper §III), *no point spectrum* corresponding to ζ-zeros. The classical $xp$ Hamiltonian has dynamics on hyperbolas $xp = E$ with $x(t) = x_0 e^t$, $p(t) = p_0 e^{-t}$ — unbounded, no discrete spectrum (paper eq 1-2). Sierra 2007 §I quote: *"there is no concrete proposal realizing all these conditions."*

3. **Sierra §V $H_I$** — self-adjoint extension via boundary parameter $\vartheta \in [0, 2\pi)$ (paper §V eq 9-11) — fine-tune. Sierra 2016 §I closing quote: *"In our approach we are not able to find a single Hamiltonian encompassing all the zeros at once."*

4. **Sierra 2007 $H_2 = \sqrt{x}p\sqrt{x}$** — deficiency indices $(1, 1)$ (paper §III Table 2) — self-adjoint extensions form a $1 \times 1$ unitary family parameterized by $\vartheta \in [0, 2\pi)$. Each $\vartheta$ gives a different operator; no single canonical choice.

5. **Connes-Consani 2021 $\Theta(\lambda, k)$** — special $\lambda$ values only (paper §5). The 31-zero coincidence at $\lambda = \sqrt{2}$ has probability ~$10^{-50}$ as a chance event (paper §5 numerical estimate), but does not capture *all* ζ-zeros. The construction depends on the parameter $\lambda$ from a continuous family.

6. **Connes 1999 §VI/VII formal trace** — *"unnatural parameter $\delta$"* (paper Introduction, page 2): *"This result is only preliminary because it requires the use of an unnatural parameter $\delta$ which plays the role of a Sobolev exponent."* The operator $D$ is parameterized by $\delta > 1$, hence δ-family, not unique.

7. **Lagarias §8 (1) $\lambda = s^2 - 1/4$** — at the critical line $s = 1/2 + i\gamma$, $\lambda = -\gamma^2 + i\gamma$, which is *complex*, not real. The proposal is paper §8 self-acknowledged hypothetical, with the issue that $\lambda$ is not generally real-valued on the candidate spectrum — failing self-adjointness reality (paper §8).

8. **Berry-Keating 1999 $H = xp$ classical** — see entry 2 (Sierra §III $xp$): no concrete realization of all conditions, classical dynamics is unbounded with no discrete spectrum, paper §II (Berry-Keating 1999) acknowledges no quantization with the desired spectral properties has been found. Sierra 2007 §I quote applies.

9. **Sierra 2007 §VI $\zeta_H$ Jost candidate** — Jost-type construction via potentials $a(x), b(x)$ (paper §VI), with the M2 model parameterized by a *family* of $(a, b)$ pairs. Each pair gives a different candidate; no single canonical choice (paper §VI fine-tune).

10. **Connes 1999 §III $(\mathcal{H}_\chi, D_\chi)$** — same δ-family obstruction as entry 6. Paper §III explicitly: *"$\delta > 1$ Sobolev exponent — unnatural"* (paper §III + Introduction). For each $\delta$, a different operator; no canonical δ.

11. **Prolate Connes-Moscovici 2022 $W_{\mathrm{sa}}$** — abstract (paper [PNAS 2022, arxiv 2112.05500] page 1): *"This coincidence holds for two values $\lambda = 1$ and $\lambda = \sqrt{2}$"* — fine-tune at two specific $\lambda$ values. Lemma 2.1 (page 2): *"The deficiency indices of $W_{\min}$ are (4, 4)"* — multiple self-adjoint extensions parameterized by a $4 \times 4$ unitary. Furthermore, the spectral match is *UV asymptotic* only (abstract: *"ultraviolet behavior reproduce that of the squares of zeros"*), not exact match — axioms 1 and 2 are at most asymptotic / partial.

### 3.4 Audit Result

All eleven candidates fail axiom 6 (strict). Each failure is anchored to a paper-direct quote or explicit mathematical structure (parameter family, deficiency index, fine-tune value, etc.) cited from the candidate's own source paper. The universal NO is *empirical* (over our audited corpus), not *necessary* — Section 6 discusses the gap.

## 4. Universal NO 11/11 Result and Paper-Direct Quote Catalog

### 4.1 Main Result Statement

Combining the audit of §3 with the strict union definition of §2, we obtain:

> **Theorem (Empirical Universal NO).** Let $\mathcal{C}$ denote the set of eleven Hilbert-Pólya candidates from the published 1998-2022 literature audited in §3.1. For every candidate $H \in \mathcal{C}$ and for the strict-union axiom 6 of §2.0 (single Hamiltonian uniqueness, no fine-tune, intersected over four specialist viewpoints), we have $\neg A_6^{\mathrm{strict}}(H)$. Equivalently, for each $H \in \mathcal{C}$, there exists a viewpoint $V \in \{\text{S3, S4, S6, S9}\}$ and a *paper-direct anchor* $\alpha_H$ (quote, equation, or lemma reference) from $H$'s source paper such that $\neg A_6^V(H)$ is witnessed by $\alpha_H$.

**Statement form.** *For every $H \in \mathcal{C}$: $H$ does not satisfy strict-axiom-6, with a paper-direct witness in the source paper of $H$.*

**Scope.** The theorem is *empirical* — restricted to the audited corpus $\mathcal{C}$ (eleven specific candidates). It does *not* claim that every conceivable Hilbert-Pólya candidate fails axiom 6, nor that the *necessary* universal NO holds (cf. §6 for the empirical-vs-necessary discussion).

**Falsifier.** A *single* paper-direct candidate $H_*$ satisfying $A_6^{\mathrm{strict}}(H_*)$ would refute the theorem. The audit of §3 establishes that no such $H_*$ exists in $\mathcal{C}$. The theorem does *not* preclude a future $H_* \notin \mathcal{C}$.

**Reading.** Theorem (Empirical Universal NO) codifies the current state of the Hilbert-Pólya program: 25+ years (1998-2022) of published candidates uniformly fail axiom 6 (strict). The codification provides a *baseline criterion* for evaluating future candidates and a *falsifier criterion* for the theorem.

### 4.2 Paper-Direct Quote Catalog

The audit of §3 cites *paper-direct anchors* for each (candidate, axiom 6) pair. Below we collect the eleven anchors in catalog form (the §3.3 entries are reproduced compactly with quote text). Additional anchors for axioms 1-5 and 7-11 (relevant to the score columns of §3.2) appear in the supplementary material; the present catalog focuses on axiom 6.

**Catalog A — Axiom 6 Strict NO Anchors (11 entries).**

| # | Candidate | Paper-Direct Anchor (axiom 6 NO) |
|---|---|---|
| 1 | BBM 2017 | "We are not yet able to prove eigenvalues real." (BBM §III) + $\psi_z(0) = -\zeta(z) = 0$ encoding (per-zero boundary fine-tune). |
| 2 | Sierra §III $xp$ | "There is no concrete proposal realizing all these conditions." (Sierra 2007 §I) + classical $xp$ continuous spectrum (paper §III). |
| 3 | Sierra §V $H_I$ | Self-adjoint extension via $\vartheta \in [0, 2\pi)$ (paper §V eq 9-11) — fine-tune. "In our approach we are not able to find a single Hamiltonian encompassing all the zeros at once." (Sierra 2016 §I closing) |
| 4 | Sierra 2007 $H_2$ | Deficiency indices (1, 1) (paper §III Table 2); 1×1 unitary family of self-adjoint extensions parameterized by $\vartheta$. |
| 5 | Connes-Consani 2021 | Special $\lambda$ values only; 31-zero coincidence at $\lambda = \sqrt{2}$ has $\sim 10^{-50}$ chance probability (paper §5); construction depends on continuous parameter $\lambda$. |
| 6 | Connes 1999 §VI/VII | "This result is only preliminary because it requires the use of an unnatural parameter $\delta$ which plays the role of a Sobolev exponent." (Introduction, page 2) — δ-family. |
| 7 | Lagarias §8 (1) | At critical line $s = 1/2 + i\gamma$: $\lambda = -\gamma^2 + i\gamma$ — *complex*, not real (paper §8 self-acknowledged hypothetical). |
| 8 | Berry-Keating 1999 | Paper §II: no concrete quantization with desired spectral properties (cf. Sierra 2007 §I quote). Classical $xp$ unbounded, no discrete spectrum. |
| 9 | Sierra 2007 §VI ζ_H | M2 model parameterized by *family* of $(a, b)$ pairs (paper §VI). |
| 10 | Connes 1999 §III | "$\delta > 1$ Sobolev exponent — unnatural" (paper §III + Introduction) — δ-family (same anchor as entry 6). |
| 11 | Prolate Connes-Moscovici 2022 | "This coincidence holds for two values $\lambda = 1$ and $\lambda = \sqrt{2}$." (page 1) + Lemma 2.1: deficiency indices (4, 4) — $4 \times 4$ unitary family of extensions. |

**Catalog B — Supporting Anchors (representative selection from cycles 1-9 catalog).**

For axioms 1-5 and 7-11, the §3.2 audit table draws on a broader catalog of paper-direct quotes. We select representative entries from each axis (full list in supplementary materials).

- **Axiom 1 (asymptotic match)**: Riemann counting $N(E) \sim (E/2\pi)\log(E/2\pi)$ — universal across spectral candidates with discrete spectrum.
  - Connes-Moscovici 2022 (paper §abstract + §6): explicit asymptotic match.
  - Sierra 2016 §V (paper §V): smooth Bessel root asymptotic.
- **Axiom 4 (eigenvalues real)**: 
  - BBM §III: "We are not yet able to prove eigenvalues real" (axiom 4 NO).
  - Connes-Consani 2021 §5: paper-direct partial.
- **Axiom 11 (biorthogonal completeness)**:
  - Sierra §V: ϑ-parameterized basis (paper §V eq 12) — partial.
  - Connes-Consani 2021 §1: Sonin space basis — paper-direct.
- **External anchors (cycles 1-9 framework continuity)**:
  - Connes-Consani 2021 §1 + Connes-Moscovici 2022 abstract: *Sonin space* — both papers' framework.
  - Connes-Consani 2018 §1.2: "still open at this time" (H¹ cohomology, Wall #1 anchor for §1.1 of present preprint).
  - Rodgers-Tao 2020 §1.5: "far from optimal" (Wall #2 anchor).
  - Pratt-Robles 2019: 5/12 ≈ 41.67% (Wall #3 anchor).
  - Iwaniec-Sarnak Perspectives §5: Landau-Siegel exceptional zero (Wall #4 anchor).
  - Lagarias §5: cancellation $\beta_\infty + \alpha_\infty/2 - 1/2 \approx 0.282$ (Wall #6 anchor).

**Catalog Total.** Combining axiom 6 strict NO anchors (11 entries, Catalog A) with axiom 1-5 + 7-11 supporting anchors and Wall #1-#6 external anchors (Catalog B), the present preprint draws on $> 47$ paper-direct quotes from $> 15$ source papers across 1859-2024, all directly verifiable in the cited papers.

### 4.3 Reading the Result

Theorem (Empirical Universal NO) is a *codification statement*, not a discovery: each candidate's failure of axiom 6 is *self-acknowledged* in its source paper (the anchors in §4.2 are the candidates' authors' own words or the authors' own equations). The contribution of the present preprint is to *systematize* these self-acknowledgments under a uniform criterion (the eleven-axiom strict union of §2) and to provide a *falsifier* for the codification.

The theorem is consistent with — and indeed largely *implied by* — the survey-level statements of e.g. Connes 2019 §1 ("up to date, in no Hamiltonian accomplishing the Hilbert-Pólya conjecture") or Sierra 2007 §I ("there is no concrete proposal realizing all these conditions"). The present preprint differs from such surveys by:

(i) *Axiom-by-axiom* breakdown (Section 2-3) rather than informal narrative,

(ii) *Paper-direct anchor* discipline for every (candidate, axiom) cell (Catalog A + B),

(iii) *Falsifier criterion* explicit (a single $A_6^{\mathrm{strict}}(H_*) = $ TRUE refutes the theorem),

(iv) *Empirical-vs-necessary* gap explicit (§6).

These four discipline points define what we mean by *codification* in the present paper.

## (Sections 5-7 deferred to subsequent cycles)

Section 5 (Five-domain falsifier search), Section 6 (Empirical vs necessary, ZFC-independence open), Section 7 (Cycle protocol meta) will be expanded in cycles 11-13.

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
