# Failed Proof Categories (Process Lemma)

> **Source**: attempt 066 (Atiyah 2018 정독). *Process lemma* — 알려진 failed RH proofs 의 fail pattern 분류.

## Background
Failed RH proofs 의 분석은 *반면교사* — 향후 spectral / analytic / arithmetic 후보 평가 시 같은 trap 회피.

## Fail Categories

### Category A — Trivial Circular (lemma `spectral_candidate_circularity_check`)
- Spectrum identification 자체가 *trivially* 영점 조건과 동치.
- Examples: BBM 2017 (attempt 010), Sierra 2007/2016 (attempt 029, 030).

### Category B — Reference Circular (NEW, attempt 066)
- 핵심 객체 (예: Atiyah 의 T function) 의 well-definedness 가 *다른 paper* 에 의존.
- 그 paper 가 미발표/검증 X.
- Example: Atiyah 2018 → paper [2] (Royal Society 제출, 미발표).

### Category C — Identity Transplant (NEW, attempt 066)
- 어떤 식이 *limited domain* (e.g., linear approximation) 에서만 성립한다고 정의.
- 그러나 proof 에서 *exact* equality 로 사용.
- Example: Atiyah 2018 의 2.6 식 (linear approximation) 을 §3 의 F(s)=2F(s) 추출에 *exact*.

### Category D — Generic Multi-valued Inversion
- f(g(s)) = 0 → g(s) = 0 step 에서 f의 inverse 가 *multi-valued* 임을 무시.
- Example: Atiyah §3 의 ζ ≡ 0 derivation step.

### Category E — Self-acknowledged Speculation
- Paper 자체에서 "most general case is undecidable" 같은 *speculation* 동시 *proof claim* 양립 시도.
- Example: Atiyah §5 — RH most general case undecidable 인정 vs paper Q-case proof.

## 평가 protocol (새 paper / 후보)

새 RH proof / spectral candidate 에 대해:
1. Category A check (lemma `spectral_candidate_circularity_check` step 6).
2. Category B check (외부 paper 의존 + verify).
3. Category C check (limited identity 의 *전 domain* 사용 여부).
4. Category D check (inverse step 의 multi-value 처리).
5. Category E check (self-acknowledged speculation 동반).

복수 카테고리 fail → *failed proof* high probability.

## Status
*Process lemma* — proven X. *Critical reading templete* — 향후 후보 평가 시 적용.

## Dependencies
- `lemmas/spectral_candidate_circularity_check.md`: Category A 의 detailed templete.
- `papers/INDEX.md`: atiyah2018 의 사고과정 추정.

## Where Used
- attempt 066 (산출).
- 향후 새 RH proof 후보 등장 시.

## Paper-direct deep verification (~attempt 131)

Atiyah 2018 paper §1-§5 paper-direct deep 의 *5 categories self-evidence*:
1. **Construction undefined**: T(s) explicit form paper-direct 부재 (paper [2] = Royal Society submission 미발표).
2. **Property inconsistency**: 2.6 (logarithm-like multiplicative→additive) + 2.7 (T(1+s)=T(1+s/2)² exponential constraint) + polynomial degree k(K) — *inconsistent unless T ≡ 1*.
3. **Proof step ambiguity**: §3.3 의 *F(s) = 2F(s)* statement paper-direct *부정확* — 정확 step 추정 *F²(s) = 0* (since (1+F)² = T(1+F)² = T((1+F)²) = T(1+2F+F²), but 2.6 implies T(1+2F+F²) = T(1+2F)).
4. **Self-contradiction**: §3 proof by contradiction + §5 RH undecidable in Gödel — paper-direct *self-acknowledged inconsistency*.
5. **Not naturally arising**: T(s) construction *artificial* (Hirzebruch Todd polynomial + von Neumann fusion *speculative*). Lemma 1 Cut 5 paper-direct.

→ paper-direct 5 categories *all* manifested in Atiyah 2018 self-contained.

## §3.3 추정 corrected step

paper claim: F(s) = 2F(s) → F = 0.
Direct via 2.6 + 2.7: T{(1+F)²} = T{1+2F}. By 2.7: T(1+2F) = T(1+F)² = (1+F)². 그러므로 T{(1+F)²} = (1+F)². 그러나 paper-direct 2.6: T{(1+F)²} = T{(1+F)(1+F)} = T{1+2F} = (1+F)². 즉 양변 일치, F 의 *trivially F=0 strain 없음*.

→ paper §3.3 *step gap*: 2.6 + 2.7 만으로 F = 0 직접 derivation 부재. *paper §3 proof step 不完*.
