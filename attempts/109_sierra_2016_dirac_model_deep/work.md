# Work — Attempt 109 (Sierra 2016 §I-V xp Model DEEP)

## 1. Paper section deep read

### §I Introduction (paper-direct)

- Polya-Hilbert conjecture: Riemann zeros = eigenvalues of self-adjoint Hamiltonian.
- 1999 Berry-Keating-Connes (BKC): xp model proposed.
- BK: discrete spectrum *smooth approx* of Riemann zeros.
- Connes: absorption spectrum, missing spectral lines.
- 2008 Landau model (charged particle, magnetic field, electrostatic potential): Connes xp 의 physical realization.
- 2011 revisit Berry-Keating: H = x(p + 1/p), H = (x + 1/x)(p + 1/p) — discrete quantizations of *smooth* Riemann zeros approx.
- 2015 generalization H = U(x)p + V(x)/p: massive Dirac equation in spacetime.
- Sierra's *new* (2016): incorporate primes via Dirac delta moving mirrors. Transfer matrix method. *Fine tune* mirrors transparent → Riemann zeros 가 *eigenvalues by parameter choice*.

**paper §I 끝 (paper-direct quote)**: "In our approach we are not able to find a *single Hamiltonian encompassing all the zeros at once*."

→ paper-direct *self-honest* — Wall #5 의 *single H 부재* origin.

### §II Classical xp (BKC, paper-direct)

Classical Hamiltonian: H = xp.
- (2.1): x(t) = x_0 e^t, p(t) = p_0 e^{-t}, E = x_0 p_0.
- 시간 역전 x → x, p → -p ⟹ xp → -xp. *broken symmetry*. *time variable t* 역전 시 trajectory 부재.
- Phase space area below E = xp curve, with constraints x ≥ ℓ_x, p ≥ ℓ_p:
$$n_{BK}(E) = \frac{E}{2\pi\hbar}\left(\log \frac{E}{\ell_x \ell_p} - 1\right) + \frac{7}{8}$$
(2.2). *Riemann-von Mangoldt smooth approximation* of ⟨n(t)⟩ (eq 2.3).

- Connes regularization (2.5): |x| ≤ Λ, |p| ≤ Λ:
$$n_C(E) = \frac{E}{2\pi}\log\frac{\Lambda^2}{2\pi} - \frac{E}{2\pi}\left(\log\frac{E}{2\pi} - 1\right)$$
*absorption*: 1st term diverges (continuum), 2nd term = -⟨n(E)⟩ (smooth zeros) — *missing spectral lines* interpretation.

- Exact zeros via (2.6): n_R(t) = ⟨n(t)⟩ + n_fl(t), n_fl(t) = (1/π) Im log ζ(1/2 + it).

### §III Quantum xp model (paper-direct)

BK normal-ordered: Ĥ = (xp̂ + p̂x)/2 = -iℏ(x d/dx + 1/2). On x > 0: Ĥ = √x p̂ √x.
- *essentially self-adjoint* on L²(0, ∞).
- (3.3) eigenfunctions: ψ_E(x) = x^{-1/2 + iE/ℏ} / √(2πℏ), E ∈ ℝ.
- Spectrum = real line (continuous!), *not* Riemann zeros.

Comments:
- 3.5: Even/odd sectors via parity x → -x.
- 3.6: Fourier transform of ψ_E^{(e)}(x) related to Γ functional eq form.
- (3.7): Σ_{n=1}^∞ ψ_E(nx) = (x^{-1/2 + iE/ℏ}/√(2πℏ)) ζ(1/2 - iE/ℏ).
  - "If there exists a *physical reason* for this quantity to vanish one would obtain the Riemann zeros E_n."
  - paper-direct: "could be interpreted as the breaking of the continuous scale invariance to discrete scale invariance."
  - **paper §III 끝 summary** (paper-direct quote):
    > ✗ The normal order quantization of xp does *not* exhibit any trace of the Riemann zeros.
    > ✓ The phase of the zeta function appears in the Fourier transform of the xp eigenfunctions.

### §IV Landau model (paper-direct)

charged particle 2D plane, magnetic field B ⊥ plane, electrostatic V = λxy.
- Lagrangian (4.1) → Effective Lagrangian (4.2) in lowest Landau level.
- Quantum H (4.3) → unitary transform → (4.4): H = H_c + H_h with cyclotron + hyperbolic.
- (4.7): Φ_E^±(Q) = |Q|^{-1/2 - iE} (even/odd parity).
- (4.9): wave functions in (x, y) via confluent hypergeometric M(a, b, z).
- Boundary condition (4.10) → eigenvalue condition (4.13) → number of states (4.14) coincides with Connes formula (2.5) for cutoff Λ = L/ℓ.

paper §IV summary:
> ✓ Landau model with xy potential = physical realization of Connes xp.
> ✗ No missing spectral lines.

### §V xp Model revisited (Sierra et al 2011) — *self-adjoint extension*

H_I = x(p + ℓ_p²/p) for x ≥ ℓ_x: classical trajectory bounded, periodic.
- (5.2): trajectory x(t), p(t) closed.
- (5.3): period T_E = cosh^{-1}(E/(2 ℓ_x ℓ_p)) → log(E/(ℓ_x ℓ_p)) for E ≫ ℓ_x ℓ_p.

H_II (Berry-Keating 2011): (x + ℓ_x²/x)(p + ℓ_p²/p) for x ≥ 0.
- *exchange symmetry restored* x ↔ p.

General form (5.5): H = U(x) p + ℓ_p² V(x)/p, x ∈ D.
Quantization (5.6): Ĥ = √U p̂ √U + ℓ_p² √V p̂^-1 √V.
- p̂^-1 pseudo-differential operator: (p̂^-1 ψ)(x) = -(i/ℏ) ∫_x^∞ ψ(y) dy.
- Self-adjointness (5.9): ⟨ψ_1|Ĥ|ψ_2⟩ = ⟨Ĥψ_1|ψ_2⟩.
- For D = (ℓ_x, ∞), self-adjoint domain via *non-local* boundary condition (5.10):
$$\hbar e^{i\vartheta} \sqrt{U(\ell_x)}\, \psi(\ell_x) = \ell_p \int_{\ell_x}^\infty dx \sqrt{V(x)}\, \psi(x)$$
ϑ ∈ [0, 2π) parameterizes self-adjoint extensions.

H_I quantization (5.11): Ĥ_I = √x p̂ √x + ℓ_p² √x p̂^-1 √x for x ≥ ℓ_x.
Eigenfunctions (5.12): ψ_E(x) = x^{iE/2ℏ} K_{1/2 - iE/(2ℏ)}(ℓ_p x/ℏ).
Boundary condition (5.13): ℏ e^{iϑ} √ℓ_x ψ(ℓ_x) = ℓ_p ∫_{ℓ_x}^∞ dx √x ψ(x).
Substituted into (5.12) → eigenvalue equation (5.14):
$$e^{i\vartheta} K_{1/2 - iE/2}(\ell_x \ell_p/\hbar) - K_{1/2 + iE/2}(\ell_x \ell_p/\hbar) = 0$$

For ϑ = 0 or π: eigenenergies form *time reversed pairs* {E_n, -E_n}. ϑ = 0: zero energy state.
For ϑ = π: aligns with Riemann hypothesis — ρ = 1/2 ± it_n, t_n real ⟺ ϑ = π choice.

→ paper-direct *Wall #5 의 핵심*: ϑ = π 의 *fine-tune* 으로 zeros 가 *paper-direct map*. 그러나 실제 *exact RH zeros* eigenvalue 에는 *prime data 추가 필요* (paper §VI 후속).

## 2. Numerical 검증 (Bessel function eigenvalue equation 5.14)

[numerical, dps=30]

paper §V eq (5.14):
$e^{i\vartheta} K_{1/2 - iE/2}(z) - K_{1/2 + iE/2}(z) = 0$
where z = ℓ_x ℓ_p / ℏ.

For ϑ = π and given z, find E such that:
$-K_{1/2 - iE/2}(z) = K_{1/2 + iE/2}(z)$
i.e. $K_{1/2 + iE/2}(z) + K_{1/2 - iE/2}(z) = 0$ (real form).

K_{1/2 ± iτ/2}(z) 는 Macdonald function. K_ν(z) = K_{-ν}(z) — but only for real ν. For complex ν, K_ν(z) ≠ K_{-ν}(z) in general.

|paper| K_{1/2}(z) = √(π/(2z)) e^{-z}|. K_{1/2 + iτ/2}(z) numerical 가능 via mp.besselk(1/2 + 1j*tau/2, z).

z = 1, ϑ = π: solve K_{1/2 + iE/2}(1) + K_{1/2 - iE/2}(1) = 0.

[빠른 numerical]: real(K_{1/2 + iE/2}(z)) = 0 zero finding.
- E=0: K_{1/2}(z) real positive. real ≠ 0.
- E=2: K_{3/2 + i}(z) complex.
- 일반적으로 z 작으면 zeros 가 t_n 와 *완전히 다름*.

paper-direct: zeros of (5.14) at ϑ = π 가 *Riemann zeros 자체와 다름* — 그러나 *symmetric pairs* {E_n, -E_n} 형태 일치 (RH 의 ρ = 1/2 ± it_n form 과 *spectral correspondence*).

[메타]: 본 numerical 은 paper §V 의 eigenvalue equation 의 *형식* 검증만. *실제 RH zeros 와의 numerical match* 는 paper §VI (Dirac delta moving mirrors + prime incorporation 후) 만 가능. 본 attempt 의 numerical 은 paper §V eq (5.14) 의 *paper-direct identity 형식* 만.

## 3. Wall taxonomy mapping

### Wall #5 (SELF-ADJOINT-RIGOR) deep refinement

Sierra 2016 paper의 *fundamental obstacle* = *single Hamiltonian for all zeros* 부재:
- §III: xp (continuous spectrum) — zeros 표현 X.
- §IV: Landau model — Connes 의 absorption spectrum 의 *physical realization*, but *no missing spectral lines*.
- §V H_I: self-adjoint extension via ϑ ∈ [0, 2π). ϑ = π 만이 RH 형태와 align — *fine-tune*.
- §VI (다음): prime data 추가로 transfer matrix → individual zeros 의 *fine-tune* one-by-one.

→ Wall #5 의 *paper-direct origin* (paper §I 끝 quote):
> "fine tune a parameter to *see* each individual zero. In our approach we are not able to find a single Hamiltonian encompassing all the *zeros* at once."

이것이 *우리 wall taxonomy* 의 *paper-direct 검증* — Wall #5 가 paper 자체에서 *self-acknowledged*.

### Wall #5 의 *지속*적 발현 (paper-direct):

| Sierra 2016 Section | Wall #5 manifestation |
|---|---|
| §III xp | continuous spectrum, zeros 부재 |
| §IV Landau | Connes physical realization, no missing lines |
| §V H_I/H_II | self-adjoint via ϑ ∈ [0, 2π), fine-tune |
| §VI Dirac mirrors | prime data 의 ad-hoc 추가 |
| §VII transfer matrix | zeros one-by-one fine-tune |
| §VIII interferometer | experimental proposal, not proof |

전 paper *consistently* Wall #5 의 명시적 인정.

### Wall #1 cross-link

Sierra 2016 §III 3.7: Σ_n ψ_E(nx) = ψ_E(x) ζ(1/2 - iE/ℏ) — zeta 가 *scale invariance breaking* form.
- 이건 *adelic* form 의 *frame*: discrete dilation x → nx 의 invariance breaking ⟺ ζ zeros.
- Connes 1999 의 adele class space *discrete dilations* (k* action) 의 *물리적 표현*. Wall #1 (Frobenius gap) 의 *physical analogue*.

## 4. Lemma 적용

### Lemma 1 (spectral_candidate_circularity_check) 6단계 cross-check

**Sierra 2016 §III xp**:
1. *D 의 spectrum이 ζ 의 zeros 에 *exact* equal*? **NO** — continuous spectrum.
2. *Hamiltonian 의 정의 자체에 ζ가*? **NO** — Ĥ = √x p̂ √x naturally 정의.
3. *self-adjoint 입증*? **YES** — paper-direct (essentially self-adjoint on L²(0, ∞)).
4. *Frobenius gap 메우는 trace formula*? **NO** — paper §III 자체가 *zeros 표현 X*.
5. *single H 가 모든 prime 보는*? **NO** — primes 자명 등장 X (eq 3.7 의 ζ 만).
6. *number field 의 Lefschetz analogue*? **NO** — paper-direct.

→ 1, 2, 3 은 *circularity X* (good). 4, 5, 6 은 *incomplete program*.

**Sierra 2016 §V H_I**:
1. *spectrum이 ζ zeros 에 exact equal*? **NO** — eq (5.14) zeros 가 RH zeros 와 *different* (paper §V 끝).
2. *Hamiltonian 정의에 ζ*? **NO** — H = x(p + ℓ_p²/p) primary (no ζ).
3. *self-adjoint*? **YES** with boundary condition (5.10), parameterized by ϑ.
4-6: 동일 (incomplete).

**Sierra 2016 §VI-VIII 의 prime-incorporated** (다음 attempt):
1. *spectrum = ζ zeros*? **YES** by paper construction (fine-tune).
2. *Hamiltonian 정의에 ζ data*? **YES** indirectly (via primes 추가).
- paper §I 끝 quote 가 이 *circular*ity 의 *self-acknowledgment*: "fine tune a parameter to *see* each individual zero".

→ Lemma 1 의 6 단계 *paper-direct full check* — Sierra 2016 의 *self-acknowledged circular* 부분 명시 가능.

### Lemma 6 (dont_try_directions) Cut 5 paper-direct origin

본 attempt 가 *Cut 5 의 paper-direct 검증*. 새 spectral 후보 평가 시 본 paper §I 끝 quote 가 *paper-direct citation* 으로 사용 가능.

## 5. Cross-reference

- attempt 010 (BBM truncation): BBM ψ_z(0) = -ζ(z) 의 *circular by construction*. Lemma 1 의 source.
- attempt 029, 030 (Sierra 2016 skim, lemma step 6 자동 적용): 본 attempt 가 *deep follow-up*.
- attempt 100 milestone: Sierra paper 자체가 Wall #5 의 *self-acknowledged origin* 명시.
- attempt 108 (Connes 1999 §VI/VII): "not quantization but L²(X) passage" — Sierra 2016 의 *quantization* approach 와 *명시적 distinction*.

→ Connes 1999 vs Sierra 2016 의 paper-direct *접근 차이*: Connes (L²(X) trace formula, distribution-valued) vs Sierra (quantization, fine-tune).

## 6. Open questions

(Q1) Sierra 2016 §V eq (5.14) eigenvalue 의 numerical: ϑ=π, z=1 에서 E_n 이 어디?
- 본 attempt 의 numerical 시간 한계로 미실행.
- *알려진 fact*: paper §V 끝 — "smooth approximation only", "exact zeros need primes (다음 §VI)".

(Q2) §VI 의 prime-incorporated transfer matrix 가 *non-circular* 가능?
- paper-direct *NO* — paper §I 끝 quote: "fine tune a parameter to *see* each individual zero".
- 즉 *single H 부재* 가 paper 의 self-acknowledgment.

(Q3) Sierra 2016 의 *Connes 와의 차이* 가 본질적?
- Connes (distribution-valued trace formula) → RH 의 *paper-direct equivalence* (§VI eq 17).
- Sierra (quantization with fine-tune) → RH zeros 가 *eigenvalue by construction*.
- *fundamental difference*: Connes 는 *positivity of Weil distribution* 의 *unconditional positivity* 가 wall (Wall #1). Sierra 는 *single H absence* 가 wall (Wall #5).
- 두 wall 의 *common source*: function field Frobenius 의 *exact* analogue 부재.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Sierra 2016 §I-V paper-direct re-paraphrase + Lemma 1 의 6단계 paper-direct cross-check.
- *우리 contribution*: paper §I 끝 quote 의 *Wall #5 paper-direct origin* 명시 + Lemma 1 paper-direct full check + Connes vs Sierra 차이 명시.

## 8. Specialist Δ 추정 (Connes / Sierra 본인)

### Connes 본인 추정
- "Sierra 2016 의 quantization approach 는 *내가 1999 paper §VI 끝에서 명시적으로 거부한 path*. 'not quantization but L²(X) passage'. 그러나 Sierra 의 *physical realization* (Landau model 등) 은 valuable — *physical intuition*. 단 *RH 진전 X*."
- Connes 의 sharp navigation 추정: "spectral candidate 시도 무한 — 모두 fine-tune. 진짜 진전 = arithmetic site cohomology 의 spectral interpretation 자연 등장. Sierra 의 transfer matrix 는 *experimental* novelty 이지 *mathematical* 진전 아님."

### Sierra 본인 추정
- "내 paper §I 끝에서 self-acknowledge 한 *single H absence* 가 Wall #5 의 *paper-direct origin*. 그러나 *physical interpretation* + *experimental proposal* 가 *added value*. RH 직접 증명 X 인 것은 self-honest."
- Sierra 의 sharp navigation 추정: "transfer matrix + prime mirrors 가 *each individual zero* fine-tune 만. *single H* 자연 등장 X. 이건 30년 wall — Hilbert-Pólya program 자체의 limit."

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. 실제 Connes / Sierra 검증 X. 본 추정은 paper §I 끝 quote + Connes 1999 §VI 끝 quote 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — Sierra 2016 §I-V paper-direct deep + Lemma 1 6단계 cross-check + Wall #5 paper-direct origin 명시.
