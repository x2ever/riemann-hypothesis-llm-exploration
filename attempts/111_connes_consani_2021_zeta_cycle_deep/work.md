# Work — Attempt 111 (Connes-Consani 2021 ζ-cycle DEEP)

## 1. Paper section deep read

### §1 Introduction & Motivation (paper-direct)

**Hilbert-Pólya speculation context**: zeros 가 *self-adjoint operator* form 1/2 + iD 의 spectrum. *Hilbert-Pólya conjecture*. paper의 핵심: D Dirac operator 인 spectral triple.

**Construction (paper-direct)**: Spectral triple Θ(λ, k) = (𝒜(λ), ℋ(λ), D(λ, k)) for λ > 1, integer k < 2λ². Numerical observation:
- λ² = 10.5, k = 18: low lying spectrum of iD(λ, k) ≈ first 7-8 zeros of ζ (Figure 1).
- 31 first zeros recovered from special λ values, *agreement coincidence prob 10^-50*.

**핵심 numerical fact**: 위 λ values 에서 *k-dependence* of λ_n(D(λ, k)) *disappears* (Figure 2: curves λ_1(D(λ, 2k)) k = 4, 6, 8, ..., 16 cross at *common* y = 14.134 = γ_1).

### §1 Definition 1.1 (paper-direct)

> A *ζ-cycle* is a circle C of length L = log μ such that the subspace Σ_μ𝓔(𝒮_0^ev) is *not dense* in the Hilbert space L²(C).

여기서:
- 𝒮_0^ev = even Schwartz functions f with f(0) = 0 (and f̂(0) = 0 — codimension 2 subspace).
- 𝓔(f)(x) = x^{1/2} Σ_{n>0} f(nx) (eq 1.3) — *Eisenstein-like averaging*.
- Σ_μ : 𝒮_0^ev → L²(C) linear map, C = ℝ_+*/μ^ℤ.

**Theorem 1.1 (paper-direct)**:
(i) Spectrum of action of ℝ_+* on orthogonal of Σ_μ𝓔(𝒮_0^ev) in L²(C) = *imaginary parts of zeros of ζ on critical line*.
(ii) If ζ(1/2 + is) = 0, then circle of length integer multiple of 2π/s is a ζ-cycle, spectrum contains s.

→ paper-direct: *ζ-cycle 의 length 가 ζ zeros 와 정확히 connected* — non-trivial spectral realization.

### §1 D(λ, k) construction (eq 1.5, paper-direct)

prolate spheroidal wave functions ψ_{m,λ}(x) = PS_{2m,0}(2π λ², x/λ) (Slepian-Pollak 도구).
Π(λ, k) = associated orthogonal projection on first k+2 prolate functions.
$$D(\lambda, k) = (1 - \Pi(\lambda, k)) \circ D_0 \circ (1 - \Pi(\lambda, k)), \quad D_0 = -iu\,\partial_u$$

→ D_0 = standard Dirac on circle of length 2 log λ. D(λ, k) = finite rank perturbation. *kernel contains finite dim subspace from prolates*.

### §2 Semi-local Weil quadratic form (paper-direct)

Eq (1.1): QW(f, g) = Σ_{1/2 + is ∈ Z} f̃(s) ĝ(s), f̄̃ Mellin transform.
Eq (1.2): f̂ = ∫ f(u) u^{-is} d*u.

**paper-direct *known fact***: positivity of QW_λ for all λ ⟹ RH. RH holds ⟹ QW_λ strictly positive (Bombieri 1991, Yoshida 1992).

**§2 paper-direct numerical findings**:
- §2.2: archimedean -W_ℝ alone *positive* if computed in interval extending beyond L = log 2 (Figure 6).
- §2.3: positivity *restored* by including -W_2 (prime 2 contribution) in interval log 2 ≤ L < log 3.
- *sign QW_λ sensitive to replacement of -W_2 by -W_p* (p as real variable in small neighborhood of 2).
- positivity fails for *real values of p outside an interval of size < 10^-3 around 2*.

→ paper-direct: QW_λ positivity 가 *every prime p < λ²* contribution sensitive. *fine-tuned* prime cancellations.

### §2.5 Numerical (paper-direct)

λ² = 11: smallest positive eigenvalue of QW_λ on ℋ(λ) = L²([λ^-1, λ], d*u) is **2.389 × 10^-48**.

→ extremely small but positive — *near radical* of QW_λ.

paper-direct theoretical explanation (§3): radical of QW_λ ⊂ range of 𝓔.

### §1 finale (paper-direct)

For special λ values, eigenvalue λ_n(D(λ, k)) → coincides with γ_n (ζ zero imag part). These (μ, λ_n) points fulfill *quantization condition*:
$$\mu^{i\lambda_n} = 1$$
i.e., μ ∈ exp(2π/λ_n · ℤ_+). 본 attempt 111 의 *ζ-cycle quantization* paper-direct 핵심.

## 2. Numerical 검증 (paper §2 light replication)

[numerical 시간 한계]

paper §1 numerical: λ²=10.5, k=18, agreement first ~8 zeros random prob 10^-50.

본 attempt 시간 한계로 prolate spheroidal wave function full implementation 미실행. paper §2.5 의 2.389×10^-48 의 우리 도구 검증 = scipy.special.pro_ang1 또는 mpmath.prolate (가용 시) — *시간 비용 단독*.

[paper-direct 우리 도구 검증]: 본 attempt 의 numerical 은 *cited paper 자체의 numerical*. *우리 contribution X*.

paper-direct citation:
- Figure 1: λ²=10.5, k=18, 8 first eigenvalues 일치 visual.
- Figure 3: 31 zeros 일치, coincidence prob 10^-50.
- §2.5: smallest QW eigenvalue 2.389×10^-48 at λ²=11.

## 3. Wall taxonomy mapping

### Wall #1 (FROBENIUS-GAP) deep refinement

Connes-Consani 2021 paper의 *Wall #1 paper-direct origin*:
- §2 semi-local Weil quadratic form QW_λ — *finite primes p < λ²* contribution + archimedean.
- paper §2.3: prime *individual* sensitivity (sign 변화 around p=2).
- paper §1 abstract: "positivity of Weil quadratic form ⟹ RH".

→ Wall #1 의 *paper-direct mapping*:
- *Function field side*: Lefschetz formula 의 Frobenius positivity (Hodge index) — *automatic*.
- *Number field side*: Connes-Consani 2021 의 QW_λ positivity — *fine-tuned* prime contributions.
- Frobenius *exact analogue 부재* 의 paper-direct manifestation = *prime-by-prime* sensitivity.

### Wall #5 (SELF-ADJOINT-RIGOR) cross-link (paper-direct)

D(λ, k) self-adjoint by construction (cutoff projection (1-Π)∘D_0∘(1-Π) of self-adjoint D_0).
- Wall #5 의 *self-adjoint 부분 해소* — D self-adjoint paper-direct.
- 그러나 *spectrum = ζ zeros exact* 부재 (special λ 만, *fine-tune*).
- BBM 2017 vs Connes-Consani 2021: BBM (self-adjoint 부재 + circular by construction), Connes-Consani (self-adjoint OK + non-circular numerical match special λ).

### Lemma 1 (spectral_candidate_circularity_check) paper-direct full check

**Connes-Consani 2021 Θ(λ, k)**:
1. *D 의 spectrum = ζ zeros exact*? **NO** — generic λ X. only *special λ* (ζ-cycle) eigenvalues match. paper §1 numerical "coincidence" prob 10^-50.
2. *D 정의에 ζ*? **NO** — D = (1-Π)∘D_0∘(1-Π), prolate spheroidal Dirac perturbation. ζ 자체 정의 X.
3. *self-adjoint*? **YES** — D_0 self-adjoint, projection 보존.
4. *Frobenius gap trace formula*? **PARTIAL** — semi-local Weil QW_λ.
5. *single H prime visibility*? **PARTIAL** — λ² 에 따라 prime p < λ² visibility, fine-tune.
6. *number field Lefschetz analogue*? **PARTIAL** — semi-local Weil → arch + finite primes.

→ Lemma 1: Connes-Consani 2021 가 *circularity 회피* (1, 2 NO) — 본 프로젝트 본 lemma 의 *exception*. 그러나 *exact spectrum X* (special λ 만, 4-6 partial).

**대비 (Lemma 1 paper-direct full check 결과 종합)**:

| Paper | (1) spec=ζ | (2) def w/ ζ | (3) self-adj | (4) trace | (5) prime | (6) Lefschetz |
|---|---|---|---|---|---|---|
| BBM 2017 | YES | YES indirect | NO | NO | PARTIAL | NO |
| Sierra §III xp | NO (cont) | NO | YES | NO | NO | NO |
| Sierra §V H_I | NO (smooth) | NO | YES (ϑ) | NO | NO | NO |
| Connes-Consani 2021 | NO (special λ) | NO | YES | PARTIAL | PARTIAL | PARTIAL |
| Connes 1999 §VI/VII | (no spec cand) | (cutoff trace) | (formal trace + cutoff) | YES (Theorem 4) | YES (∫'_{k_v*}) | distribution-valued |

→ Connes-Consani 2021 의 *uniqueness*: (1, 2) NO + (3) YES + (4-6) partial. 가장 *less circular* spectral candidate.

## 4. Lemma 적용

### Lemma 3 (positivity_unification) 10th paper-direct evidence

Connes-Consani 2021 §1: positivity of QW_λ ⟺ RH (paper-direct quote). Lemma 3 의 10번째 paper-direct evidence:

10. **Connes-Consani 2021 §1, eq (1.1)**: QW_λ positivity ⟺ RH. *semi-local* (finite primes < λ²).
- 기존 9 evidence (Lagarias §3 Weil scalar, Voros §3, Bombieri-Lagarias, Lagarias-Li, Sekatskii, Pratt-Robles A^{(1,1)}, Lagarias §4 τ_n, Polymath15 Newman, Connes 1999 §VI eq 17).
- 본 evidence 가 *quantitative semi-local* form — *λ-cutoff* 명시.

### Lemma 6 (dont_try_directions) Cut 5 *exception*

Connes-Consani 2021 가 Lemma 6 Cut 5 의 *exception*. (1, 2) NO 의 *paper-direct verified*. 이건 *non-circular* spectral candidate 의 첫 번째 (lemma 1 의 paper-direct full check 결과).

→ Lemma 6 의 정정: Cut 5 의 *전부 spectral 후보 = circular* 진술이 *Connes-Consani 2021 case 에서 partial 정정*. 다른 5 criteria (3-6 partial).

### Lemma 1 (spectral_candidate_circularity_check) update

본 attempt 의 결과 — Lemma 1 의 6 단계 paper-direct full check 비교 표:
- BBM 2017: 1-2 yes (circular).
- Sierra §III/§V: 1-2 no, but 4-6 missing.
- Connes-Consani 2021: 1-2 no, 3 yes, 4-6 partial.
- Connes 1999: spectral candidate 자체 X (cutoff trace).

→ *least circular*: Connes-Consani 2021. *real* *spectral candidate 후보*.

## 5. Cross-reference

- attempt 010, 110 (BBM): *opposite extreme* — 정의에 ζ baked in.
- attempt 029, 030, 109 (Sierra): self-adjoint extension via boundary — partial.
- attempt 033 (Connes-Consani 2021 skim): *numerical coincidence 10^-50*. 본 attempt = deep follow-up.
- attempt 048, 060, 077, 082, 088, 092, 098 (Connes 1999 partial): "not quantization but L²(X)" 가 Connes 1999 의 *anti-quantization* 명시. Connes-Consani 2021 = *quantization* 으로 회귀? *NO* — paper §1 emphasizes *spectral triple* (NCG framework, not single Hilbert-Pólya operator). distinction maintained.
- attempt 100 milestone: "Connes-Consani 10^-50 + multi-parameter" — 본 attempt 가 deep paper-direct.

## 6. Open questions

(Q1) ζ-cycle quantization condition μ^{iλ_n} = 1 의 *natural derivation*?
- paper §5: arithmetic progression of multiples of 2π/γ_n, eigenvector already eigenvector of D_0.
- *알려진 fact*: paper §5.3 (eq) 에서 paper-direct.

(Q2) λ²=11 의 smallest positive eigenvalue 2.389×10^-48 의 *theoretical bound*?
- paper §3: radical of QW_λ ⊂ range of 𝓔. *near radical* explicit construction.
- *우리 numerical 단독 검증 X* (시간 한계).

(Q3) Connes-Consani 2021 의 *next step*: special λ values 의 *systematic explanation* 자연 등장?
- paper §6: Theorem 1.1 conceptual proof.
- *Connes 본인 추정* (외부 critique 4): "arithmetic site 의 cohomological 구조" 자연 등장 — 30년 program.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Connes-Consani 2021 §1-§2 paper-direct deep + Lemma 1 6단계 paper-direct full check + Lemma 3 10th evidence.
- *우리 contribution*: Lemma 1 paper-direct full check 표 (4 papers cross-comparison) + Lemma 6 Cut 5 의 *partial 정정* (Connes-Consani 2021 exception) + Lemma 3 의 semi-local quantitative form 10th evidence.

## 8. Specialist Δ 추정 (Connes / Consani)

### Connes 본인 추정
- "Connes-Consani 2021 = 1999 program 의 *quantitative numerical evidence* form. 1999 는 distributional, 2021 은 spectral triple Θ(λ, k) 의 numerical realization. *coincidence 10^-50* prob 가 conceptual explanation 의 motivator."
- Connes 의 sharp navigation: "next step = Theorem 1.1 의 conceptual proof + arithmetic site cohomological 구조 자연 등장. 30년 program 진행 중. 본 paper 가 *promising* 그러나 RH 직접 X."

### Consani 본인 추정
- "spectral triple 의 *finite rank perturbation* 이 *arithmetic site* 의 *truncation* 자연 reflection. ζ-cycle 의 *length quantization* 이 *Frobenius eigenvalues* 의 *number field analogue* 의 *partial form*."
- Consani navigation: "본 paper 가 *Wall #1 의 first concrete numerical breakthrough*. 그러나 family-wide systematic 부재. specialist (Sarnak, Tao) 검토 후 *full mathematical framework* 까지 다년."

### Paper §1 quote *self-honest*
> "We give numerical evidence that, when one varies L, the low lying spectrum of the perturbed spectral triple resembles the low lying zeros of the Riemann zeta function."
> "we *cannot expect* that they reproduce *exactly* the n-th zero of the zeta function" (paper §1 끝, k=2ℓ family condition).

→ paper 자체가 *exact* X 명시 — Wall #1 partial 만 paper-direct.

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. paper §1 quote + Connes 1999 §VI 끝 quote 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — Connes-Consani 2021 §1-§2 paper-direct deep + Lemma 1 paper-direct full check 표 + Lemma 3 10th evidence + Lemma 6 Cut 5 partial 정정.
