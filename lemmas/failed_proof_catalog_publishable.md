# Failed Proof Catalog (Publishable Draft)

> **Source**: 외부 critique #5 #4 (~attempt 136). Lemma 4 정식화.
> **Status**: 외부 publication 후보 (American Math Monthly / Math Magazine 류).

## Title (proposal)
*"A Catalog of Failed RH Proofs: A 5-Category Framework for Critical Reading"*

## Abstract (draft)

The Riemann Hypothesis (RH) has attracted numerous proof attempts over a century, the vast majority failing. We present a 5-category framework for systematic critical reading of proposed RH proofs, derived from analysis of historical failures (Rademacher, Atiyah 2018, etc.). Each category identifies a distinct failure mode: (A) trivial circularity, (B) reference circularity, (C) identity transplant, (D) multi-valued inversion, (E) self-acknowledged speculation. The framework serves as a checklist for both proof-writers and reviewers.

## Categories (with paper-direct examples)

### Category A — Trivial Circular
**Definition**: spectrum identification자체가 *trivially* 영점 조건과 동치.
**Example (paper-direct)**:
- BBM 2017 (attempt 010, 110): ψ_z(0) = -ζ(z, 1) = -ζ(z) = 0 ⟺ z is ζ zero. *boundary condition*은 정확히 영점 조건.
- Lagarias §8 (1) hypothetical (attempt 117, 120): λ = s² - 1/4 with s = ζ-zero — 그러나 추가 issue (eigenvalues complex under RH, not self-adjoint).

### Category B — Reference Circular
**Definition**: 핵심 객체의 well-definedness 가 *다른 paper* (미발표 또는 미검증) 에 의존.
**Example (paper-direct)**:
- Atiyah 2018 (attempt 131): T(s) Todd function의 explicit form은 paper [2] (Royal Society 제출, 미발표) 에 의존. 본 paper §3 proof는 §2 properties 에 의존, properties 는 [2] 에 의존.

### Category C — Identity Transplant
**Definition**: 식이 *limited domain* (linear approximation) 에서만 성립한다고 정의 → proof 에서 *exact* equality 사용.
**Example (paper-direct)**:
- Atiyah 2018 §2.6: T{(1+f)(1+g)} = T{1+f+g} (linear approximation, paper §2 명시). §3 proof 에서 *exact* equality 로 사용.
- *공통 pattern*: weakly analytic / formal power series approximation → exact identity 로 transplant.

### Category D — Multi-valued Inversion
**Definition**: f(g(s)) = 0 → g(s) = 0 step에서 *multi-valued* inverse 무시.
**Example (paper-direct)**:
- Atiyah 2018 §3 ζ ≡ 0 derivation: F(s) = T{1+ζ(s+b)} - 1 = 0 → 1+ζ(s+b) ∈ T^{-1}(1). *T^{-1}(1)* 가 *multi-valued* (paper §2 의 weakly analytic + polynomial degree k(K)).

### Category E — Self-acknowledged Speculation
**Definition**: paper 자체에서 *"general case undecidable"* 또는 유사한 speculation + 동시 *proof claim*.
**Example (paper-direct)**:
- Atiyah 2018 §5: "RH most general undecidable in Gödel sense" + §3 *proof by contradiction* (intuitionistic logic 외 valid X).
- *self-contradiction*: §3 proof 와 §5 undecidable claim 양립 불가.

## §3.3 Step Gap Identification (sub-category, attempt 131)

paper §3.3 의 *F(s) = 2F(s)* statement = *paper-direct 부정확*.

추정 corrected step:
- 2.6: T{(1+F)²} = T{1+2F}.
- 2.7: T(1+2F) = T(1+F)² = (1+F)².
- 양변 = (1+F)² 일치.
- *F = 2F* 직접 derivation 부재.

→ *step gap* = *paper-direct 부정확 statement* + *derivation 부재* 의 paper-direct 검증.

## Application Protocol

새 RH proof 후보 등장 시:
1. **Category A check** (`lemmas/spectral_candidate_circularity_check.md` 6 단계).
2. **Category B check**: 외부 paper 의존 + verify (preprint server 에 존재? peer-reviewed?).
3. **Category C check**: limited identity 의 *전 domain* 사용 여부.
4. **Category D check**: inverse step의 multi-value 처리.
5. **Category E check**: self-acknowledged speculation 동반.

복수 카테고리 fail → *failed proof* high probability.

## Future Work

- de Branges proofs (40년치) 적용.
- Other claimed RH disproofs 적용.
- BSD / Yang-Mills 류 다른 problem 으로 framework 확장.

## References (paper-direct)

- Atiyah 2018 *The Riemann Hypothesis*. ICM 2018 expansion.
- BBM 2017 *Hamiltonian for the zeros of the Riemann zeta function*. Bender-Brody-Müller. arXiv:1608.03679.
- Sierra 2007 *H = xp with interaction and the Riemann zeros*. arXiv:math-ph/0702034.
- Sierra 2016 *Riemann zeros as spectrum and the Riemann hypothesis*. arXiv:1601.01797.
- Conrey 2003 *The Riemann Hypothesis*. Notices AMS 50 No 3.

## Status
- Draft form — 본 lemma 가 *publishable* 가 되려면 다음 작업:
  - 더 많은 historical false proofs 적용 (de Branges, Rademacher 등).
  - 5 categories 의 *mathematical rigor* (formal definition each category).
  - *peer review* 외 비공식 검토.
- 본 프로젝트 100+ attempts 의 *가장 publishable* 산출 (외부 critique #5 #4).
