# Intuition Calibration

> 외부 critique #7 (~attempt 184+) 신규. LLM 의 *직관 훈련* 누적 데이터.
> Phase 1 planning.md 의 직관 score → Phase 3 결과 비교.
>
> **본 실험의 핵심 질문**: LLM 의 "직관" 이 *random* 인가 *학습 가능* 인가?

## 운영

매 cycle 종료 시 본 파일에 한 행 추가:

| Cycle | 후보 (직관 score) | 선택 후보 | 결과 | 적중 여부 |
|---|---|---|---|---|
| 1 (attempt 184) | D=8 (Lemma 1 ceiling), E=7, C=6, G=6, F=5, A=4, B=3, H=3 | D | partial success (가설 본질 적중, axiom 7+11 → 6 sharpening) | **PARTIAL YES** (8/10 직관 → 본질 맞음, detail 변경) |
| 2 (attempt 185) | E=8 (Wall #2 codification), A=7, C=6, F=6, B=5, D=4, H=4, G=3 | E | full success (가설 변경 X, sharpening 불필요, lemma 동일 형식 재사용) | **FULL YES** (8/10 직관 → 정확 적중) |
| 3 (attempt 186) | C=8 (cross-tissue + positivity unification + critique #8 흡수 → positive sub-direction 의무), A=7, B=6, E=6, D=5, F=5, G=5, H=4 | C | partial success — Sub-direction A sharpened to *active program* (Connes-Consani arithmetic site missing Riemann-Roch). 외부 paper Connes 2019 essay 활용. lemma file 산출 X (codification 회피), positivity_unification upgrade. | **PARTIAL YES** (8/10 직관 → ceiling 본질 적중, *codification* → *active program* pivot) |
| 4 (attempt 187) | F=8 (Connes-Consani 후속 + cycle 3 mapping), A=8, E=7, C=6, G=6, H=6, B=5, D=4 | F | partial success — (a) active continuation + (b) still-open H¹ + (c) cycle 3 unification 가설 partial sharpen (Wall #1 단독). 외부 paper 의무 첫 적용 success. | **PARTIAL YES** (8/10 직관 → active continuation 적중, Wall #2 별개 axis sharpening) |
| 5 (attempt 188) | A=8 (2021 Selecta Math Weil positivity, path 1 monitoring), E=7, F=7, B=6, D=6, C=4 | A | partial success — (a) path 1 direct progress 발견 + (b) general semi-local still-open. Theorem 1 + Corollary 2 paper-direct + 2018→2021 bridging. | **PARTIAL YES** (8/10 직관 → path 1 monitoring 적중, single archimedean narrow scope sharpening) |
| 6 (attempt 189) | **A=9** (PNAS 2022 prolate spectrum, cycle 1 retroactive test), B=8 (publishable, critique #9), F=7, C=6, D=6, E=5 | A | partial success — (b) cycle 1 universal NO 11/11 강화 + (c) UV asymptotic new candidate type + (d) cycles 5+6 Sonin space link. Critique #9 publishable preprint outline finalize. | **PARTIAL YES** (9/10 직관 → flexibility test 적중, prolate axiom 6 NO 결과 cycle 1 강화) |
| 7 (attempt 190) | **A=9** (preprint Section 1+2 본문 작성, critique #9 direct externalization), D=7 (blog post), B=6, C=6, E=5 | A | full success — `papers/preprint_draft_axiom6_ceiling.md` 첫 commit (Section 1+2 본문 + 환각 검증 통과). Cycle 7 narrow scope single-turn. | **FULL YES** (9/10 직관 → critique #9 외부화 첫 manifest 정확 적중) |

## 누적 분석 (cycles 2 후)

### 분야별 직관 적중률 (cycle 1 + 2)
- **Codification meta-analysis 가설** (cycle 1 D, cycle 2 E, 둘 다 score 8): **2/2 적중** (PARTIAL + FULL). *직관 신뢰 zone 잠정 확인*.
- 다른 분야 후보 (Wall #1/#3/#4/#6 codification, Master Form, Wall #2 직접 도전 등): 미실험.

### 직관 *틀린* 경우 패턴 (cycle 1)
- Cycle 1 직관 PARTIAL YES (FULL X): *가설 specifics* (axiom 7+11 vs axiom 6 alone) 는 audit 후 sharpening.
- 학습: 직관은 *broad pattern* 잡기 유용, *narrow specifics* 는 sharpening 필요.
- 그러나 cycle 2 는 *original parsimonious* — sharpening 불필요. *wall 의 character* 가 sharpening 여부 결정.

### 직관 신뢰 zone 식별 (cycle 2 후 갱신)
- *Meta-analysis codification 가설*: **2/2 적중** (high confidence).
- *Lemma 형식 재사용* zone: **검증** (cycle 2 가 cycle 1 형식 직접 재사용 성공).
- 외부 paper 의존 가설 (B 우회 도전): 미실험.
- *Wall character 의존*: cycle 1 (Wall #5 = 10 candidates 풍부) vs cycle 2 (Wall #2 = 4 candidates) — *candidate 수 적을수록 sharpening 불필요* 가설.

### 누적 통계 (cycles 7)

| 직관 score range | 적중률 |
|---|---|
| 9/10 (cycle 1 retroactive + critique #9 externalization) | **2/2 (100% — 1 PARTIAL + 1 FULL)** |
| 8/10 (codification + meta-obstruction + active program + direct progress) | **5/5 (100% — 1 FULL + 4 PARTIAL)** |
| 7/10 (다른 wall codification) | 미실험 |
| 5-6/10 (meta sub) | 미실험 |
| 3-4/10 (NOVEL / catch-up) | 미실험 |

→ 8-9/10 직관 zone **7/7 적중** (2 FULL + 5 PARTIAL). N=7 → *consistent pattern* 강화. **9/10 zone 첫 FULL YES** (cycle 7).

### Cycle 6 특성

- **Cycle 1 retroactive test 적중**: 9/10 직관이 *cycle 1 axiom 6 NO 의 5-cycle 후 flexibility test* 정확. 결과 = lemma 강화 (11/11), prolate axiom 6 NO 확인.
- **Critique #9 publishable artifact**: cycle 6 = 외부화 첫 시도. cycles 1-5 internal accumulation 외 axis.

### Cycle 5 의 새 발견

- **Direct progress evidence zone**: cycles 1-4 negative codification + active monitoring 외 *direct active progress 1년* 패턴 (cycle 5).
- 직관 8/10 score 가 *이 zone 도 포착* — codification + active monitoring + direct progress 모두 *broad codification meta-zone*.

### Cycle 3 의 새 직관 패턴

**외부 critique 흡수 + 외부 paper 활용 효과**:
- Cycle 3 직관 PARTIAL YES (FULL X): codification 가설 표면적 적중, *active program* sharpening 으로 pivot.
- 학습: 직관이 *broad pattern* 잡기 + *외부 critique* 가 *specific direction* sharpening 트리거.
- **외부 paper search 가 cycle quality 결정**: Connes 2019 essay 정독 X 시 Sub-direction A = speculative. 정독 시 = *active program direction*.

## 누적 분석 (cycles 5+ 후)

### 분야별 직관 적중률
- RMT 후보: ?/?
- NCG 후보: ?/?
- 해석적 (mollifier 등): ?/?
- Cross-domain novel: ?/?

### 직관 신뢰 zone 식별
누적 후 *어떤 분야* 의 직관이 *적중률 높은지* 식별.

### 직관 *틀린* 경우의 패턴
- 어떤 신호를 잘못 읽었나?
- *예상 가능 zone* 외부 결과는 직관이 잡았나?

## 정직 규율

- 직관 score 는 *Phase 1 시점에 commit* — 결과 본 후 *retroactive 수정 금지*.
- 직관이 random 으로 판명되면 그 자체가 학습 (LLM intuition = pattern matching, not insight).
- 누적 < 5 cycles 에서는 통계적 신뢰 X — *trend 식별만*.
