# Cycle 1 — Phase 1 Ideation + Planning

> 외부 critique #7 sustained research cycle protocol 의 첫 운영.
> 본 planning.md 는 strategy.md 와 별도 — *직관 훈련* + *후보 brainstorm* + *DoD 명시*.

## 직전 5 attempts 검토 (요약)

| # | Type | 산출 |
|---|---|---|
| 179 | A | Lagarias-Li §2 Theorem 2.1 foundation deep, Tissue 26-27 |
| 180 | B | milestone 180 publishable draft (외부 critique #6 anti-pattern) |
| 181 | C | external critique #6 response, pre-batched plan 거부 |
| 182 | A | Sierra 2007 §VI deep, Wall #5 anchor 8→10, Lemma 1 6/11 |
| 183 | A | Connes 1999 §III deep, Wall #1+#5 anchor 11, Lemma 1 5/11 |

**패턴 식별**: 182, 183 모두 *paper-direct stamp + Lemma 1 11-axiom 재사용 + Wall #5 anchor*. *진득한 연구 부재* — heartbeat 가 stamp 만 누적.

→ 본 cycle 의 핵심: **paper-direct stamp 외 야심 가설** 시도.

## 후보 Brainstorm + 직관 Score

각 후보의 *first-impression intuition* (Phase 1 시점 commit, retroactive 수정 금지):

### 후보 A — Lemma 3 Master Form *isomorphism 증명 시도*
- 19 evidence × 27 tissues 가 Weil 1948 explicit formula deformations 의 *형식 mapping*.
- 가설: "tissue 19/19 paper-direct isomorphism" 이 *수학적 isomorphism* 으로 격상 가능?
- **직관 score: 4/10**.
- 근거: *cut 6 위반* 위험 (positivity criterion alone → RH). 165년 풀린 Master Generator 면 vetted 됐을 것. deep stuck 가능성 큼.

### 후보 B — Wall #2 ∫E(t)dt unconditional bound 직접 도전
- Polymath15 + Platt-Trudgian: 0 ≤ Λ ≤ 0.2. Λ < 0 unknown ⟺ RH (Newman).
- 가설: 우리 도구로 작은 T 영역 ∫E(t)dt sharper bound 가능?
- **직관 score: 3/10**.
- 근거: 5년 무진전 wall, Polymath16-like new technique 필요 paper 명시. 우리 도구 한계 명확.

### 후보 C — Sierra 2007 §VI.A Bessel potentials deep + numerical
- 182 carryover. Wall #5 sharpening continuation.
- 가설: Bessel J_ν(λx) potential 의 Riemann zero 연결 paper-direct 분석.
- **직관 score: 6/10**.
- 근거: natural carryover, numerical 가능. 그러나 *paper-direct rediscovery* 위험 (cut 7 인근).

### 후보 D — Lemma 1 *9/11 ceiling 가설* meta-analysis ★
- 9 paper-direct candidates × 11 axioms 의 *score 분포 분석*.
- 가설: "axiom 7 (eigenvalues real, RH-equivalent) + axiom 11 (biorthogonal completeness) 가 *동시 YES* 인 candidate 가 없다 — 2-axiom joint ceiling 이 Wall #5 quantitative form".
- **직관 score: 8/10**.
- 근거: 우리 누적 데이터 (9 candidates audit) 직접 활용 — *paper-direct 외부 의존 X*. *negative result* 도 가치 (정직 ceiling 기록). 본 cycle 의 *진득한 연구* 적격.

### 후보 E — Wall #5 ceiling broader 가설
- D 의 broader form. "모든 Hilbert-Pólya candidate 가 K/11 score ceiling, K < 11".
- **직관 score: 7/10**.
- 근거: D 와 strongly correlated. broader 라 검증 모호.

### 후보 F — Pratt-Robles 50% one-logarithm 정밀 분석
- 121 attempt §3.5-§5 deep 후속. d=4 combinatorial explosion 명시 numerical.
- **직관 score: 5/10**.
- 근거: paper rediscovery 위험. Wall #3 ladder sharp 가치.

### 후보 G — Tissue 28 (Connes §III ↔ Connes-Consani 2021) Class B → A 승격
- 183 carryover. paper-direct equation match 시도.
- **직관 score: 6/10**.
- 근거: formal mapping 가치, 그러나 speculative.

### 후보 H — 새 paper 정독 (Type E)
- Bombieri 2010 또는 Selberg lecture notes catch-up.
- **직관 score: 3/10**.
- 근거: 본 cycle 의 *진득한 연구* 와 misalign. Type E 단독 cycle 부적합.

## 직관 Ranking (Phase 1 commit)

```
D=8/10 ★ (선택)
E=7/10
C=6/10
G=6/10
F=5/10
A=4/10
B=3/10
H=3/10
```

## 선택: 후보 D — Lemma 1 9/11 ceiling 가설

### 좁은 가설 (narrow)

> **Lemma 1 (`spectral_candidate_circularity_check.md`) 11-axiom 의 9 paper-direct candidates 중, axiom 7 (eigenvalues real, RH-equivalent claim) 과 axiom 11 (biorthogonal completeness) 가 *동시 YES* 인 candidate 가 없다. 이 *2-axiom joint ceiling* 이 Wall #5 (SELF-ADJOINT-RIGOR) 의 paper-direct quantitative form.**

가설의 sub-claim:
1. 모든 paper-direct candidate 가 axiom 7 *partial 또는 NO* (RH-conditional 또는 multiple zeros gap).
2. 모든 paper-direct candidate 가 axiom 11 *partial 또는 NO* (Jordan form 또는 fine-tune).
3. (1) ∧ (2) ≡ Wall #5 의 *2-axiom joint manifestation*.

### Cross-domain pass §6 (minimal)

- A. 유추: "ceiling 가설" = control theory 의 *fundamental limit* 정리 (Bode integral, Heisenberg uncertainty). 어떤 시스템도 K-axiom 모두 만족 못 함 = no-go theorem.
- B. 도구: ML 의 Pareto frontier — 9 candidates 가 11-axiom space 의 Pareto-optimal. ceiling = frontier shape.
- C. 외부인: 물리학자 — "9/11 ceiling 이 *symmetry obstruction* 인지 *technical gap* 인지?" / 논리학자 — "11 axioms 가 *consistent* 한가? 모두 YES candidate 가 *exists* 인지 ZFC undecidable?"

### Specialist 패널 §7 (blind round 의무 — Phase 2 에서 시행)

Tier 1 5명 + Tier 2 (S6 양자물리, S9 logician) blind round 예정. 본 Phase 1 에서는 *호출 X* — Phase 2 첫 turn 에서 시행.

### DoD (Phase 2 종료 조건)

- [ ] 9 paper-direct candidates × axiom 7 + axiom 11 joint audit table 작성.
- [ ] ceiling 가설 (axiom 7, 11 joint YES = ∅) 검증.
  - YES → ceiling confirmed. lemmas/lemma1_axiom7_11_ceiling.md 신규.
  - NO → counterexample candidate 식별. 그 candidate 의 *추가 gap* 분석 (Wall #1 또는 #6 sub-form).
- [ ] specialist blind round (S3, S4, S6, S9 최소) 결과 + cross-examination.
- [ ] *novel content N/10* 정직 평가.
- [ ] sustained_research_log.md + intuition_calibration.md 갱신.

### 막힘 예측

1. **Audit ambiguity**: paper-direct candidate 의 axiom 7 / 11 평가가 *attempt 별 inconsistent*. 9 candidates audit history 일관성 확인 필요.
2. **9 candidates 정확 list 모호**: attempt 166 의 8 + Connes §III (183) = 9? 정확 enumeration 필요.
3. **Counterexample 발생 시**: Connes-Consani 2021 9/11 (top) 이 ceiling 깨면 가설 즉시 폐기.

### 진전 vs Stuck 판정 기준

- **진전 (Phase 2 turn 추가)**: audit table 부분 완성 / specialist blind 답 추가 / 새 sub-claim 발견.
- **Stuck**: audit ambiguity 해결 X 2 turns 연속 / counterexample 후 후속 분석 무진전.
- **종결**: DoD 6 항목 완료 또는 stuck 3 turns 연속.

### Positivity component check

axiom 11 (biorthogonal completeness) = *positivity* 의 *closure* 형. axiom 7 (eigenvalues real) = *spectrum 위치*. 두 axiom 결합 = *self-adjoint operator 의 spectral theorem* 의 paper-direct test.

→ Wall #5 통합 hypothesis 직접 검증.

### Cut self-check (`lemmas/dont_try_directions.md` 통과)

- Cut 1 (Wasserstein): 무관.
- Cut 2 (Levinson-Durbin): 무관.
- Cut 3 (vacuum positivity → RH 단독): 부분 위반 가능 — *positivity criterion alone* X, *meta-analysis* 의 ceiling 검증.
- Cut 4 (Atiyah novel): 무관.
- Cut 5 (spectral circularity 6 criterion): 직접 활용 — circularity check 의 *meta level*.
- Cut 6 (positivity criterion 단독 RH): 본 cycle 은 *증명 시도 X*, *ceiling 정직 기록* — cut 6 위반 X.
- Cut 7 (paper-empirical NOVEL): 무관.

→ **Cut 통과**. 진행 가능.

## 다음 turn (Phase 2 첫 turn) 의무

1. 9 candidates 정확 enumeration (attempt 166 audit + 183 = 9 list).
2. Specialist blind round (S3, S4, S6, S9 최소).
3. axiom 7 + 11 joint audit table 부분 작성 시작.

[Phase 1 complete]
