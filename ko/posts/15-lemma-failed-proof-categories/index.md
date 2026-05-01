---
title: "Lemma 4 — Failed Proof Categories (전문)"
parent: 보조정리
grand_parent: 한국어
nav_order: 15
date: 2026-05-02
---

# Lemma 4 — Failed Proof Categories

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/15-lemma-failed-proof-categories/) · *2026-05-02*

> **Process lemma** — 실패 RH proofs의 systematic critical reading 5-category framework. Atiyah 2018 case study가 5개 모두 manifest ([Finding 4](../05-finding-atiyah-step-gap/) 참조).

## Background

실패 RH proofs는 *반면교사* — 과거 failure mode 분석으로 향후 spectral / analytic / arithmetic 후보가 같은 trap 회피.

## 5 categories

### Category A — Trivial Circular

Spectrum identification이 *trivially* $\zeta$-zero condition과 동치.

- **상세 templete**: [Lemma 1 — Spectral Candidate Circularity Check](../14-lemma-spectral-circularity-check/).
- **예시**: BBM 2017, Sierra 2007/2016 ($\psi_z(0) = -\zeta(z)$ boundary condition).

### Category B — Reference Circular

핵심 객체의 well-definedness가 **다른 paper**에 의존, 그 paper가 *unpublished or unverified*.

- **예시**: Atiyah 2018 → paper [2] (Royal Society 제출, preprint 시점 미발표). Atiyah의 $T$ function이 [2]에 의존, 2018 preprint 자체에 explicit construction X.
- Proof의 foundation이 citation에, paper 자체에 없음.

### Category C — Identity Transplant

Equation이 **limited domain** (예: linear approximation)에서만 성립한다고 정의됐는데, proof에서 **exact** equality로 사용.

- **예시 (Atiyah 2018)**:
  - §2.6 (paper-direct, *"weakly analytic"* — 즉 linear approximation): $T\{(1+f)(1+g)\} = T\{1+f+g\}$
  - §3가 이를 $f = g = F$ ($F$는 *작지 않음*)로 exact equality 사용 → $F = 2F$ 도출.
  - Substitution이 §2.6의 stated domain of validity 외부.

### Category D — Generic Multi-valued Inversion

$f(g(s)) = 0 \implies g(s) = 0$ 형태 step에서, inverse $f^{-1}$가 *generically multi-valued*임을 무시하고 single-valued처럼 취급.

- **예시 (Atiyah 2018)**: §3가 $T(1+w) = 1 \implies w = 0$를 inferring해서 $\zeta \equiv 0$ 도출. 그러나 $T^{-1}(1)$은 generically multi-valued (Atiyah의 Todd function = polynomial of bounded degree, multiple preimages).

### Category E — Self-acknowledged Speculation

Paper 자체가 *"the most general case is undecidable"* 같은 disclaimer + *"proof"* claim 양립 시도. 둘 다 author의 settled position일 수 없음.

- **예시 (Atiyah 2018)**:
  - §3가 proof by contradiction claim.
  - §5: *"The most general version of the Riemann Hypothesis will be an undecidable problem in the Gödel sense."*
  - §3 proof 맞으면 §5와 모순, §5 맞으면 §3와 모순. 둘 다 settled position 불가능.

## 평가 protocol — framework 적용

새 RH proof / spectral candidate에 5 check 적용:

1. **A-check**: Paper의 axiom/hypothesis가 결론과 trivially 동치?
2. **B-check**: 핵심 객체가 unpublished/unverified external work 의존?
3. **C-check**: Equation이 stated validity domain 외부에서 사용?
4. **D-check**: Function inversion이 uniqueness argument 없이 수행?
5. **E-check**: Paper의 self-acknowledged disclaimer가 proof claim과 모순?

**2개 이상 trigger** → 구조적 failure 강한 evidence.

## Atiyah 2018 paper-direct deep verification (5/5 manifestations)

Atiyah 2018 §1–§5 deep read 시 5 categories 모두 manifest:

| Category | Atiyah 2018 manifestation |
|---|---|
| **B — Construction undefined** | $T(s)$ explicit form paper-direct 부재 (Royal Society [2] 의존) |
| **C — Property inconsistency** | §2.6 (logarithm-like multiplicative→additive) + §2.7 ($T(1+s)=T(1+s/2)^2$ exponential) + polynomial degree $k(K)$ — 셋이 *$T \equiv 1$ 외엔 inconsistent* |
| **C/D — Proof step ambiguity** | §3.3의 *"$F(s) = 2F(s)$"* statement는 §2.6 + §2.7 만으로 paper-direct *도출 X* (derivation은 [Finding 4](../05-finding-atiyah-step-gap/)) |
| **E — Self-contradiction** | §3 proof by contradiction + §5 "RH undecidable in Gödel sense" — paper-direct self-acknowledged inconsistency |
| **A/B — Not naturally arising** | $T(s)$ construction artificial (Hirzebruch Todd polynomial + von Neumann fusion *speculative*) — 자연스럽게 등장하는 analytic object 아님 |

→ Paper-direct **5/5 categories** all manifested in Atiyah 2018, self-contained.

## §3.3 corrected derivation — 실제 내용

Paper의 §2.6, §2.7만 사용:

- §2.6 with $f = g = F$:
$$T\{(1+F)^2\} = T\{1+2F\}$$
- §2.7 with $s = 2F$:
$$T(1+2F) = T(1+F)^2$$
- 합성. $X := T(1+F)$:
$$T\{(1+F)^2\} = T\{1+2F\} = X^2$$

양변 $X^2$ 일치. 합 statement는 $X^2 = X^2$ — **tautology**. Paper-direct *"$F = 2F$"* derivation은 §2.6 + §2.7만으로 **도출 X**.

전체 step-by-step derivation은 [Finding 4](../05-finding-atiyah-step-gap/).

## 본 framework 가치

Framework는 **prescriptive** (무엇을 찾을지) — *descriptive* post-hoc 분석 아님. Reviewer/proof-writer가 새 RH proof attempt 검토 시 5-question checklist 분 단위:

1. **A**: trivially circular?
2. **B**: reference circular?
3. **C**: identity transplant?
4. **D**: multi-valued inversion?
5. **E**: self-acknowledged contradiction?

2+ categories trigger → 구조적 의심. Atiyah 2018은 5개 모두 trigger — framework가 그 case study에서 추출됨.

## Framework 향후 적용

Systematic application 후보:

- **de Branges' RH proof series** — 다년 attempts, partial retractions
- **Amateur preprint catalog** (vixra archive of failed RH attempts)
- **Historical Hilbert program failures** — nuance: 같은 structural sense의 "failed proofs"는 아니지만 Category A/B 일부 early attempts에 존재

프로젝트는 systematic application 미수행. Framework는 *American Mathematical Monthly* / *Math Magazine* 류 standalone expository contribution publication-ready.

## *아닌* 것

- 5 check 모두 pass하는 proof가 옳다는 보장 X (necessary, sufficient X).
- Atiyah 또는 어떤 author 개인 비판 X. Failure modes는 *structural*, personal X.
- 수학 contribution 아님 — *수학 proof attempt 평가 *practice* 에 대한 contribution.

## Reading order

- 적용 case study: [Finding 4 — Atiyah 2018 §3.3 step gap](../05-finding-atiyah-step-gap/).
- Detailed Category A template: [Lemma 1](../14-lemma-spectral-circularity-check/).
- Reporter's manager-mode review: [Reporter Flag — Cycle Protocol over-claim](../11-reporter-flag-cycle-protocol-overclaim/).

---

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/15-lemma-failed-proof-categories/)
