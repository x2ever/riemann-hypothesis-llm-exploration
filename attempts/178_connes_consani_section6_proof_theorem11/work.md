# Work — Attempt 178 (Connes-Consani 2021 §4-§5 *Spectral Characterization of Zeta Zeros* DEEP)

## Cut self-check
Cut 5 (모든 spectral 후보 = circular) — Lemma 1 (1) *spectrum = ζ zeros exact*: NO for generic λ but YES at special λ (paper-direct numerical near-coincidence). cut X (paper-direct mapping).

## Connes-Consani 2021 §4-§5 paper-direct (page 35-45)

attempt 111 §1 + 176, 177 §2 deep follow-up.

### §4.1 Examples μ = 5.5, 6.5, 7.5, 8.5, 9.5, 10.5

paper-direct *6 numerical examples* (paper §4.1):

#### μ = 5.5 (paper §4.1.1, page 35)
λ_j vs ζ_j:
- 14.781 vs 14.1347 (γ_1)
- 21.701 vs 21.022 (γ_2)
- 25.547 vs 25.0109 (γ_3)
- 29.345 vs 30.4249 (γ_4)
- 33.168 vs 32.9351 (γ_5)

#### μ = 9.5 (paper §4.1.5, page 39)
14 eigenvalues vs 14 ζ-zeros (paper page 39 table). 본 case에서 *near coincidence* visible.

### §4.2 Average discrepancy (paper-direct page 41-42)

paper-direct *3 metrics*:

**Mean absolute error A(μ)**:
- A(5.5) = 0.635, A(6.5) = 0.447, A(7.5) = 0.529.
- A(8.5) = 0.457, A(9.5) = 0.395.

**Root-mean-square R(μ)**:
- R(5.5) = 0.691, ..., R(9.5) = 0.460.

**Normalized RMS NR(μ)** (paper page 41-42):
- NR(5.5) = 0.0376 (3.76%).
- NR(7.5) = 0.0206.
- NR(8.5) = 0.0148.
- NR(9.5) = 0.0103 (~1%).
- NR(10.5) = 0.00995 (<1%).

paper-direct quote (page 42):
> "These numbers show that the normalized root-mean-square deviation is *steadily improving* and reaches 1% (one percent) for μ = 9.5 and then drops to less than one percent for μ = 10.5."

→ paper-direct: λ_j(D(λ, k)) → ζ_j *quantitative convergence* with NR ≈ 1% at μ = 9.5.

### §5 Zeta zeros from spectral triples (paper-direct, page 42)

paper-direct quote (page 42):
> "The main observation of this section is that, for any n ∈ ℕ there are *special values of the parameter λ* at which the dependence of λ_n(D(λ, k)) on k *disappears*. For these special values of λ the *common value* of the λ_n(D(λ, k)) coincides with the imaginary part ζ_n of the n-th zero of the Riemann zeta function. Moreover, these special values of λ form a *geometric progression* whose scale factor is the exponential of π/ζ_n."

→ paper-direct **CRITICAL FINDING**:
- Special λ values 에서 λ_n(D(λ, k)) = ζ_n *exactly*.
- Special λ values *geometric progression* with ratio exp(π/ζ_n).

paper-direct quote (page 42 끝):
> "Applying the last method for the small range of λ in the interval (2, 4) one obtains the agreement with the *first 31 zeros* ζ_n (n ≤ 31) of zeta with sufficient accuracy to assess the *probability of a fortuitous coincidence at 10^-50*."

→ paper-direct: 31 zeros *probability of coincidence* 10^-50 — **paper-direct strong evidence**.

### §5.1-§5.4 4 criteria (paper-direct page 42)

4 criteria to detect special λ values:
1. **§5.1**: Comparison λ_n(D(λ, 2ℓ)) ↔ λ_n(D(λ, 2ℓ+1)).
2. **§5.2**: Evolution of λ_n(D(λ, k)) as function of λ.
3. **§5.3**: Quantization criterion μ^{i λ_n} = 1.
4. **§5.4**: Eigenvector far from D_0(λ).

paper-direct: 4 criteria 의 결합 → 31 first zeros recovery (page 42).

### §5.1 Lemma 5.1, 5.2 (paper-direct page 43-44)

**Lemma 5.1** (paper page 43): mini-max for self-adjoint matrix A, E ⊂ Ker A:
$$\mu_n(A) = \max_{\substack{F \subset A \\ \dim F = n, F \perp E}} \min_{\xi \in F, ||\xi||=1} \langle \xi | A \xi \rangle$$

**Proposition 5.2** (paper page 43): D = QDQ self-adjoint matrix, P ⊂ M_N(ℂ) projection, Q = 1-P, D_P := QDQ:
$$\mu_n(D_P) = \max_{F \perp P, \dim F = n} \min_{\xi \in F} \langle \xi | D \xi \rangle$$

(eq 5.4): 직접 derivation of *positive eigenvalues monotonicity*.

(eq 5.2): λ_n(D(λ, k+1)) ≤ λ_n(D(λ, k)) ∀n, λ.

→ paper-direct *monotonicity*: even k vs odd k+1 의 *positive eigenvalues monotonic*.

## *Tissue 25 NEW*: Connes-Consani §5.1 monotonicity ↔ Lagarias §7 F_π interpolation

paper-direct **Tissue 25**: 
- Connes-Consani §5.1 (eq 5.2): λ_n(D(λ, k+1)) ≤ λ_n(D(λ, k)).
- Lagarias §7 (Theorem 7.1, attempt 117): F_π entire function order 1 exponential type ≤ π under RH.

paper-direct: 두 paper 모두 *interpolation / monotonicity* — *parameter k (CC) vs n (Lagarias)*.

mapped 25/19 (Tissue 25 cross-class).

## *Wall #1 paper-direct quantitative manifestation*

paper-direct: Connes-Consani §5 = paper-direct **NCG approach 의 quantitative progress**:
- 31 first zeros recovered with *coincidence probability 10^-50*.
- Special λ values *geometric progression*.
- 4 criteria for detection.
- Wall #1 paper-direct *partial bridge*.

→ Wall #1 paper-direct: Connes 1999 program 의 22년 후 *quantitative numerical evidence*.

## *Lemma 1 (Spectral Candidate Circularity) update*

attempt 111: Connes-Consani 2021 = *least circular* (1, 2 NO).
attempt 146: 9-axiom audit.
attempt 155: 11-axiom audit.

본 attempt 178 update:
- Connes-Consani 2021 axiom (1) "spectrum = ζ exact": **YES at special λ (paper §5)**.
- 그러나 *generic λ*에서는 NO.
- → *partial circular at special λ values*, *non-circular generic*.

paper-direct: Connes-Consani 2021 = *most subtle Lemma 1 candidate* — *not circular by construction*, but *converges to ζ at special λ*.

## *진짜 흥미* paper-direct insight (anchored)

paper §5 quote (paper-direct page 42):
> "the probability of a fortuitous coincidence at 10^-50"

paper-direct: 31 zeros *coincidence probability 10^-50* = paper-direct *strong empirical evidence for*:
- *D(λ, k) spectrum = ζ-zeros at special λ* (Theorem 1.1 (i)).
- *not coincidental* — paper-direct.

→ paper-direct: Connes-Consani 2021 = paper-direct *strongest spectral candidate evidence* (Lemma 1 framework).

## Lemma 적용

### Lemma 3 evidence (10 Connes-Consani) 강화
- attempts 111, 176, 177, 178 누적.
- *spectral characterization* paper-direct.

### Lemma 7 Anchoring (NEW quotes)
- Connes-Consani §4.2 page 42 quote: "NR ≈ 1% at μ = 9.5".
- Connes-Consani §5 page 42 quote: "probability 10^-50 fortuitous coincidence".
- Connes-Consani §5.1 eq (5.2) monotonicity.
- catalog 41 → 44 quotes.

### Lemma 1 update (Connes-Consani axiom 1)
- generic λ: NO.
- Special λ: YES (paper §5).
- *most subtle candidate*.

## Honest scope
*novel content X*. Connes-Consani §4-§5 paper-direct deep + Tissue 25 + Wall #1 paper-direct progress + Lemma 1 update (Connes-Consani axiom 1 partial yes at special λ).

*paper-direct strong finding*: 31 zeros coincidence probability 10^-50 = paper-direct *strongest spectral candidate evidence*.
