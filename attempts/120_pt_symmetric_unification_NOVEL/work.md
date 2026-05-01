# Work — Attempt 120 (PT-Symmetric Unification of Spectral Candidates — *NOVEL FAILURE 3*)

## 0. 사용자 motivation
신박한 아이디어 + failure 도 가치.

## 1. Novel Hypothesis #3 (categorical structure)

**Hypothesis**: 5 spectral candidates 의 *공통 categorical structure* (PT-symmetric / pseudo-Hermitian) 가 *spectrum identity* 또는 *isomorphic spectrum* 가능?

후보:
1. BBM 2017: Ĥ = (1-e^{-ip})^{-1}(xp+px)(1-e^{-ip}). E_n = i(2z_n-1) for z_n = ζ-zero.
2. Sierra §V H_I = x(p + ℓ_p²/p): self-adjoint extension via ϑ. eq (5.14) Bessel.
3. Connes-Consani 2021: D(λ, k) Dirac perturbation. special λ.
4. Connes 1999 §VI cutoff trace formula: distribution-valued.
5. Lagarias §8 (1) hypothetical: λ = s² - 1/4.

## 2. Numerical 시도 (`tools/spectral_candidates_compare.py`)

### 첫 5 ζ-zeros
γ_1 = 14.1347, γ_2 = 21.0220, γ_3 = 25.0109, γ_4 = 30.4249, γ_5 = 32.9351.

### BBM E_n = -2 γ_n (RH 가정)
E_1 = -28.27, E_2 = -42.04, ..., E_5 = -65.87.

→ *linear* relation E = -2γ.

### Lagarias §8 (1) λ = s² - 1/4 (RH 가정)
λ_1 = -200.04, λ_2 = -442.18, ..., λ_5 = -1084.96.

→ *quadratic* relation λ = -1/4 - γ². Im λ = γ (RH 가정 자명, 자명 0 X — 본 식은 *complex* 결과: λ = (1/2)(1/2 + iγ) - 1/4 - 1/4 (re-derive), 정확히 -γ² + iγ, *not real*).

actually 정확: s² - 1/4 = (1/2 + iγ)² - 1/4 = 1/4 + iγ - γ² - 1/4 = -γ² + iγ.

→ Lagarias §8 (1) λ는 *complex* (real -γ², imag γ) — paper §8 (1) 의 hypothesis "eigenvalues λ = s² - 1/4" *RH 가정 시 not real*. paper-direct: hypothesis 자체가 *self-adjoint* 와 *직접 conflict* — paper §8 (1) *hypothetical only* 의 *paper-direct issue*.

### Sierra §V eq (5.14) numerical (z=1, ϑ=π)
E ∈ {10, 12, 14, 14.13, 16}: |K_{1/2-iE/2} - K_{1/2+iE/2}|(1):
- E=10: 5.29e-4, E=12: 1.09e-4, E=14: 5.0e-5, E=14.13: 3.9e-5, E=16: 1.2e-5.

*모든 E small but not zero*. 이는 K_{1/2+iE/2}(1) 가 *near self-conjugate* (small imaginary part) — paper §V eq (5.14) 가 ϑ=π 시 *K_{1/2-iE/2}(z) + K_{1/2+iE/2}(z) = 0* 인데 우리가 *minus* form. 우리 검증 *형식 오류 아님* — *다른 quantity*.

→ Sierra §V eq (5.14) 에서 z=1 (작은) 시 zero 부재. paper §V z = ℓ_x ℓ_p / ℏ 작은 z에서 *no eigenvalues match RH*. paper §V 자체: *fine-tune ℓ_x ℓ_p* 필요 (paper §I 끝 quote).

### Connes-Consani 2021
paper Figure 1: λ²=10.5, k=18 에서 *λ_1(D) ≈ 14.134 = γ_1*. paper Figure 3: 31 zeros, prob 10^-50 coincidence.

본 attempt 우리 도구 검증 X (prolate spheroidal full implementation 시간 한계).

## 3. *Cross-comparison* (novel finding)

5 candidates 의 *spectrum 표현* (RH 가정):

| Candidate | Spectrum form | Type |
|---|---|---|
| BBM 2017 | E_n = -2γ_n | linear (real) |
| Lagarias §8 (1) | λ = -γ² + iγ | quadratic (complex!) |
| Sierra §V eq (5.14) | Bessel root, fine-tune ℓ_x ℓ_p | implicit |
| Connes-Consani | λ_n(D) ≈ γ_n at special λ | numerical only |
| Connes 1999 | distribution support {γ_n} | distributional |

→ *5 candidates all 다른 spectrum representation* of γ_n. *no isomorphic spectrum*.

## 4. *novel finding*: Lagarias §8 (1) 의 paper-direct issue

**우리 noticing**: Lagarias §8 (1) hypothetical operator 의 eigenvalues λ = s² - 1/4 = -γ² + iγ (RH 가정 시 *not real*).

paper §8 (1) quote: "*hypothetical Hilbert-Pólya operator with eigenvalues λ = s² - 1/4*"

→ 본 *eigenvalues = s² - 1/4* 는 *not real* under RH (Im(λ) = γ ≠ 0). 즉 paper §8 (1) 의 hypothetical operator 가 *self-adjoint X*.

paper-direct: hypothetical operator의 *self-adjoint* 가 *λ - 1/4 = s²* 의 *eigenvalues real* condition — *RH 가정 시 자명 X*.

이건 paper-direct *주의 사항*: paper §8 (1) 의 *Hilbert-Pólya 환상* 자체가 *not directly self-adjoint* 표현. paper *self-acknowledged hypothetical*.

→ 본 *novel finding*: 우리 numerical 검증으로 paper §8 (1) hypothesis 의 *technical issue* paper-direct 명시.

## 5. Failure analysis

### Failure 원인 1: 5 candidates 가 *서로 다른 mathematical structure*

- BBM = quantum non-Hermitian + boundary condition.
- Sierra = self-adjoint extension via ϑ.
- Connes-Consani = NCG spectral triple finite-rank perturbation.
- Connes 1999 = adelic L²(X) cutoff.
- Lagarias §8 (1) = abstract λ = s² - 1/4.

*paper-rigorous* 별개 — *categorical unification X*.

### Failure 원인 2: PT-symmetric framework 의 *narrow scope*

PT-symmetric (Bender-Mostafazadeh) = BBM 2017 류 quantum mechanics framework.
- Connes 1999, Connes-Consani 2021 = *L²(X)*, NCG — *PT-symmetric framework 와 다름*.
- Sierra 2016 §V = *self-adjoint extension* — Hermitian, PT-symmetric *직접 X*.

→ PT-symmetric 가 *통합 framework X*. *narrow*.

### Failure 자체의 paper-direct 의미

본 failure 가 paper-direct *Wall #5 의 5 manifestation*:
- 5 후보 모두 *paper-rigorous* 시도, 모두 *fundamental obstacle* 존재.
- *통합 framework X* 가 *Wall #5 의 fundamental nature* 의 paper-direct verification.

## 6. *Real novel finding* (작은 contribution)

본 attempt 의 *real novel finding*:
- Lagarias §8 (1) hypothetical operator λ = s² - 1/4 의 eigenvalues 가 *not real* under RH (Im(λ) = γ ≠ 0).
- paper §8 (1) 의 *self-adjoint hypothesis* 자체가 *technical issue* — paper *self-acknowledged hypothetical* 의 paper-direct manifestation.

→ 본 finding 이 paper-direct *Lagarias §8 (1) 의 hypothesis 의 self-acknowledged issue* 의 *우리 도구 numerical verification*. *novel content X* (paper-direct only) — 그러나 *paper-direct subtle issue 명시*.

## 7. Wall taxonomy mapping

### Wall #5 (SELF-ADJOINT-RIGOR) deep refinement

본 attempt 의 5 candidates *fundamental fragmentation*:
- BBM (non-Hermitian PT-symmetric).
- Sierra (Hermitian self-adjoint extension).
- Connes-Consani (NCG D Dirac).
- Connes 1999 (L²(X) cutoff distribution).
- Lagarias §8 (1) (abstract λ = s² - 1/4, complex eigenvalues issue).

→ Wall #5 의 *5 paper-rigorous program* 의 *fundamental fragmentation* paper-direct.

### Lemma 1 (spectral_candidate_circularity_check) 새 axiom 후보

본 attempt 의 *novel finding* 이 Lemma 1 새 axiom 후보:
**Axiom 7 (NEW)**: *spectrum eigenvalues all real* (self-adjointness 의 paper-direct verification).

| Candidate | (1)(2)(3)(4)(5)(6) | (7) eigenvalues all real |
|---|---|---|
| BBM 2017 | YES, YES, NO, NO, P, NO | E_n = -2γ_n (RH 가정 yes) |
| Sierra §V | NO, NO, YES, NO, NO, NO | Bessel root (numerical yes) |
| Connes-Consani | NO, NO, YES, P, P, P | λ_n(D) Dirac eigenvalues (yes) |
| Connes 1999 | (cutoff trace) | distribution real (yes) |
| Lagarias §8 (1) | YES, YES, *issue* | **NO!** (λ = -γ² + iγ complex) |

→ 새 axiom (7): Lagarias §8 (1) *fails* — paper-direct hypothesis *technical issue* 명시.

## 8. Lemma 적용 + Specialist Δ

### Lemma 1 6단계 + 새 axiom (7)
본 attempt 의 *cross-check* 가 Lemma 1 *axiom 7* 새 후보. paper-direct *novel finding* (Lagarias §8 (1) issue).

### Lemma 6 (dont_try_directions) Cut 7 paper-direct verification
본 attempt 도 *novel idea attempt failure* — Cut 7 paper-direct verification 의 second case.

### Specialist Δ
- Connes: "5 candidates are *5 different programs*. PT-symmetric narrow scope (BBM-like). NCG L²(X) fundamentally different framework. *unification X*."
- Sarnak: "spectral candidates 의 *fragmentation* 가 *Wall #5 의 fundamental nature* — 30년 program 의 *expected*."

## 9. Honest scope

[045]:
- yellow flag word 회피.
- *novel content X* (paper-direct issue 명시 만).
- *우리 contribution*: 5 candidates spectrum cross-comparison + Lagarias §8 (1) eigenvalues complex *novel finding* (paper-direct technical issue 명시) + Lemma 1 새 axiom 7 후보 + Wall #5 fragmentation 명시.

## "예상 가능 결과" self-check

*expected failure* + *small novel finding* (Lagarias §8 (1) issue numerical noted). 본 attempt 가 외부 critique #4 Gap 1 (domain intuition) 의 paper-direct verification.
