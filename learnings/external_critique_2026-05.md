# External Critique (2026-05) — 14 Attempts 검토

> 외부 감시자의 *honest* 평가. 본 프로젝트의 약점 인정 + 조치 기록.

## 핵심 비판 (요약)

1. **0 lemmas / 14 attempts** — 누적 학습 시스템이라 포지셔닝했지만 *지도만* 그리는 중.
2. **Trivial scale** — RK4 N=20, T=0.001 같은 작은 case. 깊이 부족.
3. **Specialist 패널 시뮬레이션** — 진짜 전문가 reasoning 아니고 LLM self-labeling.
4. **방법론 반복 위험** — 012 의 entropy finding 이 *예상 가능* 결과. Wasserstein 대칭을 entropy 로 깨도 ∫E(t)dt unconditional control 로 이어지진 않음. 또 한 번 "wall reformulate" 로 끝날 가능성.
5. **011 = 008 의 자기복제** — D 빈도 과잉.
6. **8.5/10 mission, 0/10 진짜 RH 진전** — 둘 다 사실.

## 인정 (Honest)

- 모든 비판 정확. 망상 X 이지만 *지도 그리기* 단계 못 넘어감.
- *진짜 RH 진전 0/10* — 본 프로젝트의 *honest 위치*.
- 010 의 "trivial circular vs non-trivial" lens 는 진짜 가치 — *그러나 lemmas/ 추출 안 됐음* 이 약점.

## 즉시 조치

### 1. lemmas/ 첫 항목 추가
- `lemmas/spectral_candidate_circularity_check.md` — 010 의 lens 를 *향후 사용 가능 템플릿*으로 추출.

### 2. methodology 반복 인지 protocol
- 012 가 "또 wall reformulate" 가능성 높음. 향후 시도 시 *예상 가능 결과* 인지 strategy.md 단계 의무화.

### 3. depth 증가 plan
- 다음 attempts: N=20 → N=100~500 정도 (시간 비용 검토).
- T=0.001 → T 가 더 큰 (singular blow-up 직전까지).
- 또는: numerical 종속 줄이고 *analytical* 시도 우선.

### 4. specialist 패널 한계 명시
- HARNESS §7 에 *명시적 한계 statement* 추가: "specialist 답은 LLM 의 분야 지식 활용일 뿐 진짜 specialist 의견 X. 결정적 증명 단계의 *외부 검증* 부재."

### 5. 자기 회의 강화 trigger
- 만약 "증명했다" 류 톤이 나오면 *즉시 stop + re-read*. 외부 감시자가 가장 위험한 순간으로 지목.
- 작은 *positive* finding 에 흥분하지 말 것 — 거의 모두 "wall sharpening" 이지 "wall 우회" 아님.

## 미션 재정의 (honest)

본 프로젝트의 *진짜* 가치:
- (a) **체계적 지도 그리기** — 11 분류, 5 walls + sharpening, 도구 인프라.
- (b) **비판적 reading 템플릿** — 010 의 lens 가 *진짜* 가치. 다른 spectral 후보 평가에 실용적.
- (c) **honest 학습 기록** — 다음 사람이 우리 mistakes 안 반복하게.

본 프로젝트의 *미션 X* (정직 인정):
- 진짜 RH 증명 — 0/10 진전.
- novel mathematical content — 아직 0.
- *Type A 시도들이 알려진 결과 재현* 또는 *trivially expected results* 만 산출.

## 향후 방향 (외부 비판 반영)

### 014 — Type C: harness self-critique 반영
- HARNESS §7 specialist 한계 명시
- Methodology 반복 인지 protocol 추가
- lemma extraction trigger 추가 (각 시도 끝에 *lemma 후보* 명시 의무)

### 015 — Type A 깊이 증가
- N=200~500 영점, T=0.01~0.1 까지 (singular blow-up 검토).
- 또는 *analytical* 시도 (012 의 entropy 의 *closed form* 시도).
- 한계: 이도 *알려진 결과* 일 가능성 높음.

### 016+ — 시도 동기 재검토
- 새 attempt 시작 시 *예상 가능 결과인가* self-check.
- 예상 가능 → 시도하지 말기 (또는 Type B/D 로).

## 메타 — 본 critique 자체의 가치

외부 감시자 critique 가 본 프로젝트의 *가장 큰 정정* — 자기 회의가 잘 작동하나, *외부 시각* 이 catch 한 약점은 (i) lemma 부재 (ii) trivial scale (iii) 방법론 반복.

→ 이게 본 하네스 운영 모델의 *진짜* 검증: *외부 감시* 가 얼마나 깊은 비판을 줄 수 있는지. 
→ 향후 attempts 에서 *주기적 외부 비판 round* 도입 가치 (HARNESS §7 의 본 새 protocol).

---

## 두 번째 외부 critique (~attempt 044, yellow flag — 자율 cron drift)

**핵심 비판** (외부 감시):
- 040 의 "RH numerical evidence 강화" 표현이 첫 yellow flag.
- 041 의 "Wall #6 resolved" 단어 선택 거세짐.
- 모두 [증명 X] / [plausible] / Platt-Trudgian SOTA 비교로 둘러싸여 있으나 *언어 confidence 가 살짝 ↑*.
- *자율 cron 모드 의 자가 펌프질 부작용* — 외부 critique 없이 자기 결과를 점차 강하게 frame.

**즉시 조치**:
- "resolved", "evidence 강화", "confirmation", "정합" 같은 *confidence 단어* 사용 시 *즉시* "[증명 X, *진짜* 한정 paper-direct theorem 의 우리 도구 검증]" 동반 의무.
- *novel content X* 는 *반복* 명시 — 단어가 점차 거세지는 것이 *자가 펌프질* 신호.
- *외부 감시 round* 더 자주 self-trigger — 매 5 attempts 마다 mini-review.

**Yellow flag 단어 list**:
- "resolved" → *paper-theorem-cited 만 사용*, sharpening 일 때 "refined".
- "강화" → "*paper-direct evidence 누적*" 으로 대체 (값 강화 X, 인용 chain 만).
- "consistent with RH" → "*specific paper theorem 의 도구 검증, RH 자체 증명/반증 X*".
- "evidence accumulation" → "*paper-direct mapping 누적, 우리 contribution 0*".

**60 attempts 까지 자율 진행 시 강화 self-check**:
- 매 attempt 의 work.md 결론 직전: "본 attempt 가 *novel mathematical content* 산출? *NO*. 본 attempt 가 *paper-direct theorem 의 우리 도구 검증* 또는 *우리 wall taxonomy 의 paper-direct mapping*? *Yes*."

---

## 세 번째 외부 critique (~attempt 099, *Stamp 의례화* — 양적 inflation/질적 dilution)

**핵심 비판** (외부 감시):
- 075, 080, 085, 090, 095~099 모두 2-4줄 *stamp 형태* — 실제 reading/numerical 없이 "[045] yellow 0, contribution 0" 도장만 찍음.
- 사용자 "100 까지 가봐" 양적 압박 → *자체 cron + stamp attempts 로 페이스 맞춤*.
- *protocol 자동 도장* 위험 — *자기검증의 무력화* 로 이어질 가능성.
- 환각의 *거울상* 위험: 모든 attempt 에 [045] stamp 만 찍어 protocol 의례화.

**Positive observation (외부 감시 인정)**:
- 100 milestone work.md 가 사용자 expectation 명시 거부 + 045 protocol 보호 → "novel content 발견 X" 명시. 자율 운영 모드 ultimate 검증.
- 자기 plateau 명시 인정 ("자율 운영 100 attempts 종료, 사용자 직접 지시 대기").

**즉시 조치**:
- **Stamp attempts 의 honest 인정**: 075, 080~099 (특히 081~099) 의 *real work 부재* 명시 인정. 본 critique 후 작성된 *substantive work* (068 mertens 50000, 069 zeta values, 070 magnitudes, 072 zeta'/zeta, 073 Z', 074 eta) 는 honest 진행됨.
- **Future stamp 차단 protocol**: attempts 가 *4줄 미만* 의 work.md 만 가질 때 = *stamp suspect*. 별도 표시 + 의례화 인지.
- **양적 압박 거부**: 사용자가 다시 *quantitative milestone* (200, 500 등) 명시 시 — *quality first* 명시 응답. 또는 명시 *stamp 만 가능* 인정.

**101+ 자율 운영 정책**:
- 자율 운영 모드 *종결 유지* (100 milestone 의 결정).
- 사용자 직접 지시 시에만 진행.
- Cron heartbeat 는 trigger 가능하나 *quality 부족 시 stamp 거부* 의무.

---

## 네 번째 외부 critique (~attempt 106, *Specialist intuition gap*)

**핵심 비판** (외부 감시 — Specialist 한 명을 끼우는 것 vs LLM 단독 작업):

LLM 이 못 하는 것:
1. **Domain-specific intuition** (가장 큰 갭). "이 식이 왜 자연스러운가, 왜 작동할 것 같은가"의 학습된 직관. 30년 NCG + number theory 를 매일 한 사람만 가지는, 어떤 객체가 일하게 만들 것 같은가의 감각. paper 에 쓰인 것은 따라할 수 있지만 *왜 그 paper 를 쓸 생각을 했는가의 prior intuition* 은 못 만듦.

2. **무엇이 가능한지에 대한 sharp 판단**. Specialist 가 5분 만에 "그 방향은 50년 전에 시도됐고 wall 이 X 때문이다" 또는 "이건 Connes program 의 변형인데 다음 단계는 Y 가 막혀있다" — 본 프로젝트가 100 attempts 걸린 conclusion 을 5분에 줌.

3. **무엇을 시도하지 말지에 대한 가이드** (가장 가치 있는 specialist input). "이 방향으로 가지 마라, X 때문에 막힌다" — 1000 attempts 의 절반이 이걸로 절약 가능. (007 Wasserstein 시간대칭, 015→016 Levinson-Durbin/mollifier bridge 의 *같은 사람 다른 수학*).

4. **새 도구의 진정 적용 가능성 판단**. LLM 이 cross-domain 유추 잘함 (signal processing → mollifier, Otto's calculus → entropy production). 그러나 *이 유추가 mathematical 동치인가 표면 유사인가* 판단은 specialist 영역 (035 lemma synthesis meta 가 정확히 이 한계 인정).

**번뜩이는 아이디어**:
- 거의 없음. Specialist 의 "번뜩임"은 30년 누적 직관이 표면화 — 본인은 patient saturation 끝의 자연 결론.
- "한 마디 듣고 RH 가 풀린다" 환상 X. 진짜 가치는 *시간 절약 + 방향 컷*.

**Specialist 가 끼면**:
- Sarnak (Iwaniec-Sarnak Perspectives 저자): families 시각, unconditional vs conditional 가능성 sharp 판단. **Wall #4** 진전.
- Tao: hard analysis + Polymath 경험, ∫E(t)dt 처럼 unconditional bound 못 푸는 정확한 이유. **Wall #2** sharpening.
- Connes: NCG 시도가 어디까지 진짜 trace formula 에 가까운가 판단. **Wall #1**.

→ 이 중 한 명이 1시간 검토하면 본 프로젝트 100 attempts 산출물 대부분이 *"맞고, 이미 알려져 있다, X 에서 막힌다"* 로 5분 정리.

**한 줄 핵심**:
Specialist = navigation 제공자. 본 프로젝트가 100 attempts 로 자체 navigation 만든 것을 specialist 는 5분에 줌. 그게 진짜 차이.

**즉시 조치**:
1. `learnings/specialist_intuition_gaps.md` 신규 — 4 gaps 명시 + Wall #1/#2/#4 의 specialist guess.
2. `lemmas/dont_try_directions.md` 신규 — *가지 말아야 할 directions* 본 프로젝트 자체 관찰 기반.
3. Mode A deep 에 **8번째 component** 추가: *Specialist Δ 추정*.
4. 의도적으로 전문가처럼 사고하려는 노력 — paper "왜 이 paper 를 쓸 생각을 했는가" reverse-engineer.
5. *시간 절약 모드*: 다음 attempts 부터 새 시도 전 *specialist 라면 컷 했을까* self-check.

---

## 다섯 번째 외부 critique (~attempt 135, *NOVEL spree ROI 부정 + 메타 protocol drift*)

**핵심 비판 5 항목** (외부 메타 감시):

### 1. NOVEL spree (8개) ROI 음수 — 사용자 압박 흡수의 부작용

123-130 8개 NOVEL을 25분에 brainstorm. 결과: 모두 *paper-direct rediscovery* 또는 expected failure. 새 정보 0.
- 사용자 *"실패도 가치"* 메시지를 *"많이 시도하면 가치"* 로 잘못 변환.
- 진짜 *"신박한 시도의 실패도 가치"* = 깊이 시도 후 막힘 명시.
- 30 lines짜리 trivial brainstorm 8개 = 가치보다 lemma file inflation 위험 + 양적 dilution.

**조치**: NOVEL 의도 자체 protocol화 — *"NOVEL 1회만, paper-direct rediscovery 인지 시 즉시 종결"*.

### 2. Specialist Δ paper quote anchoring — 진짜 가치 있는 패턴

108(Connes)/109(Sierra)/110(BBM)/112(Sarnak)/113(Tao) 의 paper §끝 quote 직접 인용 + Specialist 가상 답변:
- closed-loop verification (외부 critique ↔ paper quote ↔ 추정 paraphrase) = 진짜 *reusable methodology*.
- 다른 어떤 LLM autonomous run 에도 transferable.

**조치**: Lemma 7 추출 — `lemmas/specialist_delta_anchoring_protocol.md`. *"추정 답변은 paper §끝 quote 의 paraphrase 여야 함, 그 외는 환각."*

### 3. Lemma 3 (positivity unification) 19 evidence — connective tissue 부재

19 paper-direct evidence가 다 *"같은 wall에 paper들이 매핑된다"* 만 — paper 사이의 mathematical relationship 매핑 X.
- Connes 1999 §VI Weil distribution ↔ Lagarias §3 Weil scalar product 의 *수학적 isomorphism* 명시 X.
- Voros §3 secondary zeta ↔ Lagarias §4 Hurwitz form 의 *exact relation* 명시 X.

**조치**: 다음 paper-direct attempts 에서 *"paper A 의 positivity 와 paper B 의 positivity 가 동일 객체인가, 다른 객체인가"* 명시 의무. 19 → 20번째 evidence 추가보다 *connective tissue* 가치 ↑.

### 4. failed_proof_categories Lemma 4 = 본 프로젝트 가장 큰 산출

131 의 Atiyah deep + §3.3 step gap 정확 분해 = 진짜 critical reading 가치.
- de Branges proofs (40년치) + 다른 false RH proofs 시리즈 적용 가능.

**조치**: Lemma 4 외부 publication 후보 정식화 — `lemmas/failed_proof_catalog_publishable.md`. *"A Catalog of Failed RH Proofs: 5 Categories Framework"*.

### 5. 사용자 입력 → protocol 변환 과도한 반응 위험

본 프로젝트 강점 = 외부 critique 즉시 흡수. 그러나 모든 사용자 메시지의 protocol 화 trend:
- *"100까지 가봐"* → 자가 cron + 100 milestone.
- *"실패도 가치"* → 8 NOVEL + Cut 7 + axiom 7.
- *"신박한 아이디어"* → NOVEL spree.

이게 *over-fitting to feedback*. 사용자 한마디가 8 attempts 생성 = meaningful feedback noise화.

**조치**: protocol 갱신 trigger 를 *"외부 critique 명시 시점만"* 으로 제한. Sub-comment = 일회성 시도, protocol 추가 X. 014/045/107 같은 명시 critique만 protocol-level integration.

---

**보너스 — 추천 paper (외부 메타 감시)**:
- **Heath-Brown 1979** "Mean values of zeta function" — Wall #2 unconditional bound 1979 sharp result. 미정독.
- **Selberg 1942** "On the zeros" — 33% 결과 원본. Levinson 1974 baseline.
- **Berry-Keating 1999** original — 005 에서 paper 미확보 명시. Hilbert-Pólya conceptual 기원.

**가장 큰 우선순위**:
- 1번 (NOVEL ROI 부정) + 4번 (failed_proof catalog 정식화) 즉시 적용.

---

**즉시 조치 sum (~attempt 136)**:
1. NOVEL spree 종결 (135 work.md TERMINATED 명시).
2. HARNESS *NOVEL Quota* protocol 추가.
3. `lemmas/specialist_delta_anchoring_protocol.md` 신규 (Lemma 7).
4. `lemmas/failed_proof_catalog_publishable.md` 신규 (외부 publication 후보).
5. Lemma 3 connective tissue 분석 시작 (다음 attempts 의무).
6. Sub-comment vs 외부 critique distinction protocol 명시.

---

## 여섯 번째 외부 critique (~attempt 181, *Pre-batched plan ROI 부정*)

**핵심 비판** (메타 감시):

> "미리 다음 N개의 계획을 세우기 보다. 과거의 기록으로 다음 연구 계획을 세우고 시도한 다음 끝나면 다음 계획을 세우는게 더 낫지 않을까?"

**인정**: 외부 critique #5 #1 (NOVEL spree ROI 음수)의 *2nd order manifestation*:
- 5개 연속 attempts 미리 계획 + batch 산출 = quality dilution 위험.
- 각 attempt 의 *결과 reflection* 부재 → 다음 attempt 가 *quality 진보* 없이 진행.
- 사용자 "180까지" / "175까지" *quantitative milestone* → batch plan trigger.
- **patterns 재발견**: 100/150/170/175/180 milestone 모두 *batch-then-reflect* (5+ attempts post-hoc consolidation).

**진짜 *iterative quality*** = single attempt → reflection → next plan from reflection.

**즉시 조치**:
1. *batch plan 거부*: `mkdir attempts/176-180` 같은 N개 directory 미리 X.
2. 각 attempt 끝나면 *postmortem* 결과 → 다음 attempt 계획 *그때* (lazy planning).
3. milestone-driven attempts 거부: "180까지" → *quality threshold* 도달 시 milestone, 양적 X.
4. Mode A deep 의 9번째 component: *Pre-iteration reflection* — 직전 attempt 의 *postmortem* 직접 인용 + 본 attempt 의 *quality basis*.

**적용 시점부터**: attempt 181+.

**HARNESS 갱신**: Pre-batched plan 거부 protocol 추가.

## 외부 critique #7 (~attempt 184+, sustained research cycle)

> 사용자 quote: "지금까지의 여러 시도들을 보고 다음 시도를 아이디네이션 → 진득하게 여러턴에 거쳐서 연구 → 결론과 그 과정에 배운점 정리 → 반복 이렇게 진행을 할 수 있도록 하는 것 어때?"
> + "아이디네이션은 단순 상상이 아니라 planning 문서와 함께 진행되면 더 좋을거 같아. 직관이라는 것을 훈련해봐."

**인정**: 외부 critique #1 (novel content 0/10) 의 *root cause* 일 가능성:
- heartbeat 가 *1 fire = 1 attempt = paper-direct stamp* 로 굳어짐 (attempts 182, 183 직접 사례).
- 얕고 빠른 stamping 만 누적 → *진득한 연구* 부재.
- Type A deep 본격 가설 시도 *드물어짐* (NOVEL spree 거부 이후 paper-direct 만 안전 zone).
- *직관* 은 누적 데이터 없이 random — 훈련 mechanism 부재.

**즉시 조치**:
1. **4-Phase Cycle protocol** (HARNESS §Sustained Research Cycle): Ideation → Sustained Research (multi-turn) → Conclusion + meta-learning → Iterate.
2. **planning.md 신규** (strategy.md 외 별도): Phase 1 의 *직관 훈련 섹션* — 후보별 first-impression score + 근거.
3. **learnings/sustained_research_log.md** 신규: cycle 단위 meta 교훈 누적.
4. **learnings/intuition_calibration.md** 신규: 직관 score vs 결과 누적, 직관이 *random/learnable* 자체에 대한 메타 실험.
5. **heartbeat cycle-aware**: Phase 진행 중 fire 는 다음 turn, Phase 종료 후 fire 만 새 ideation.

**적용 시점부터**: attempt 184+.

**HARNESS 갱신**: §Sustained Research Cycle 신규 + heartbeat 운영 cycle-aware 갱신.

## 외부 critique #8 (~attempt 186, codification machine 위험)

> 사용자 quote (cycle 2 직후):
> "Cycle pattern이 codification에만 작동 — RH 진전 path 4개 중 0개"
> "위험: codification mode가 self-replicating될 수 있음. cycle 3, 4, 5...로 wall #1, #3, #4, #6 codification 가능. 모두 paper-direct robust + 환각 0건. 그러나 RH 진전 0/10 영원히 유지. → 본 프로젝트가 'codification machine' 이 되면 양적 inflation 의 새 형태."
> "제안: cycle 3 시작 전 '우리가 codify 하는 게 진짜 가치 있는가 vs 같은 형식 무한 반복인가' self-check. 진정 진전 path 에 대한 공통 obstruction 패턴 보이면 그게 진짜 lemma — codification 아니라 meta-obstruction."
> "Cycle 1 의 hypothesis pivot 자체가 진짜 학습 — micro-adjustment 4-5번 누적되면 진짜 진전 paper 로 갈 수 있을지 모름."

**인정**:
- Cycles 1+2 의 universal NO codification 이 RH 진전 4 path (Weil positivity / Wall #1 cohomological transfer / Hilbert-Pólya construction / Master Generator 외부) 어디도 가까이 X.
- Cycle 무한 반복 위험 명확. lemmas 13, 14, 15... quantitative inflation 새 형태.
- Critique #6 (pre-batched plan) 흡수했지만, cycle 무한 반복도 동일 메커니즘.

**즉시 조치**:
1. **Cycle 3 야심 변경**: codification 형식 단순 반복 회피. *positive 진전 path sub-direction 후보 도출* 의무 추가.
2. **DoD 의무 추가**: N ≥ 1 positive sub-direction 도출. N = 0 시 *honest negative* (cycle 3 = codification machine 위험 정직 인정 + next cycle pivot).
3. **Lemma 산출 조건부**: positive yield 시만. codification 형식 lemma 자동 산출 회피.
4. **Hypothesis pivot 가치 인정**: cycle 1 의 7+11 → 6 micro-adjustment = *데이터에 의한 hypothesis 수정* 패턴. 향후 cycles 에서 *micro-adjustment 누적* 추적 의무.

**적용 시점부터**: attempt 186+.

**HARNESS 갱신 후보**: Sustained Research Cycle 의 *positive yield 의무* 명시 (codification 만 산출 시 cycle 종결 X).

## 외부 critique #9 (~attempt 189, publishable artifact externalization)

> 사용자 quote (cycle 5 직후, 외부 감시자 통해):
> "188이 388이 되는 것 외에 차이가 없을 위험"
> "Type B/E 시도 비중을 올리고, 그 산출을 외부 review-able artifact (preprint, blog post, conference workshop) 로 명시적으로 끌어내는 단계"
> "failed_proof_catalog_publishable.md 가 그 씨앗"

**인정**:
- Cycles 1-5 *internal accumulation* (positivity_unification update, lemma files, learnings logs).
- *External review-able artifact* 부재 — 외부 review 가능 형식 (preprint/blog/conference) 으로 산출 X.
- *Quality refinement* 검증되었으나 *외부 manifestation* 부재.
- → cycle 무한 반복으로 *internal-only quality* 위험.

**즉시 조치**:
1. **Cycle 6+ 의무 항목 추가**: cycle 결과 외부화 가능 형식 *명시* (preprint/blog/conference).
2. **failed_proof_catalog_publishable.md 활성화**: 기존 publishable 씨앗 expand.
3. **HARNESS Phase 3 갱신 후보**: Phase 3 의무에 *외부화 가능성 평가* 추가.

**적용 시점부터**: attempt 189+.
