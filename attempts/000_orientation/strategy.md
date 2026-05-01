# Attempt 000: Orientation — 지도 그리기
**Type**: B (Meta / orientation)

## 가설/전략

**시도 목표**: RH 의 *증명* 이 아니라 *지도 그리기*. 정독한 8편 논문 + 4개 background 파일 + HARNESS protocol 을 입력으로,
1. RH 시도가 반복적으로 부딪히는 **본질적 벽 N개** 정량화 (walls).
2. 11개 접근법 분류 (`background/approaches.md`) 의 *서로 결합 가능* 한 쌍·삼중 식별.
3. 다음 시도 (`001_*`) 의 strategy 후보 *3개* 도출 — 각각 좁은 가설 + specialist depth + cross-domain breadth + 코드 활용 채널 명시.

> **본 시도는 증명을 시도하지 않는다.** orientation = "어디로 갈 수 있는가" 의 정찰. 본 시도가 끝나야 *진짜 시도들*이 의미있는 가설로 시작된다.

## 동기

- 8편 정독 + background 작성으로 baseline 정보가 *내부* 에 축적됨. 이것을 *외부화* (md 파일) 하지 않으면 다음 시도가 같은 정보를 재구성해야 함.
- HARNESS 의 specialist 패널 (§7) + cross-domain (§6) + computational (§8) 프로토콜이 *처음 가동* — *meta-attempt* 에서 시범 운영 → 작동 안 하는 부분 발견 → 수정.
- "본질적 벽" 분류가 없으면 시도들이 *우연히 같은 벽* 에 반복 충돌. 미리 분류해두면 *직접 우회* 시도 가능.

## 예상 도구

- `background/*.md` 4개 파일.
- `papers/INDEX.md` 의 사고 과정 추정 8개.
- `tools/` 의 4개 모듈 (verify_zeros, mertens, li_criterion, pair_correlation) — 데이터 sanity check 용.
- HARNESS §6 (cross-domain), §7 (specialist), §8 (computational) 프로토콜.

## 예상 막힘 지점

미리 예측 (이 예측의 정확도 자체가 학습 데이터):

1. **specialist 시뮬레이션의 limit**: Tier 1 의 5명 시뮬레이션이 *서로 같은 답* 으로 수렴해 confirmation bias 일 가능성.
2. **벽 분류의 자의성**: A–E 의 5개 벽이 *외관상 분류* 일 뿐 진짜 본질적 분류가 아닐 수 있음.
3. **다음 시도 후보의 빈약함**: 도출되는 3개 후보가 모두 *문헌에 이미 있는 시도*일 가능성 — 본 프로젝트의 가치 부재 신호일 수 있음.
4. **cross-domain 의 거짓 양성**: 형식 유사를 진짜 다리로 착각.

## 성공 기준 (DoD)

- [x] `learnings/walls.md` — 본질적 벽 ≥ 5개, 각각 어느 접근법이 부딪히는지 mapping
- [x] `learnings/approaches_taxonomy.md` — 11개 분류 + 결합 가능 쌍 ≥ 3개
- [x] postmortem.md 에 다음 시도 (`001_*`) strategy 후보 *3개* — 각각:
  - 좁은 가설 1개
  - 의지 분류 + 의무 specialist 호출 명시
  - cross-domain pass 후보 1개
  - 코드 활용 채널 1개
  - 예상 성공/실패 기준 1개
- [x] specialist 패널 라운드를 *실제로* 수행 (5명 Tier 1 + 1~2 Tier 2) — 운영 결함 식별

## 명시적 실패 기준 (언제 그만둘지)

- 본 시도는 단일 작업 — *bounded scope*. 무한 진행 안 함.
- 만약 specialist 라운드에서 *완전 confirmation bias* (모든 specialist 가 trivially 같은 답) → 운영 결함 기록 후 stop, HARNESS §7 수정안 제안.
- 만약 벽 분류가 *모두 기존 문헌에 이미 명시된 형태* 라면 → "본 프로젝트의 비교우위는 분류가 아니라 *조합 시도* 자체" 로 결론 + 분류는 baseline 으로 사용.

## Cross-domain pass (HARNESS §6)

본 시도는 *meta-attempt* 라 cross-domain 직접 적용보다 **다음 시도들이 활용할 cross-domain 후보** 를 정리:

### A. 유추 패스 (RH 와 isomorphic 구조 후보, 시도 가치 ranking)
- **물리 (양자 / 통계물리)**: Lee–Yang, partition function 영점, log-gas — Rodgers–Tao 의 동역학과 직접. 우선순위 ★★★.
- **신호처리**: minimum-phase / all-pass 필터의 영점 → mollifier 의 일반화. 우선순위 ★★.
- **제어이론**: pole / zero placement, stability — RH 의 "stability of prime distribution" 로의 재해석. 우선순위 ★.
- **확률 / 자유확률**: GUE 가 익숙. free probability 가 미탐색. 우선순위 ★★.
- **위상수학 / TDA**: 영점의 persistence — 미탐색, 거짓 양성 위험 큼. 우선순위 ★.
- **정보이론**: maximum entropy + 영점 분포. 우선순위 ★ (낮음).

### B. 도구 임포트 (다음 시도 후보 채널)
- 통계물리 *log-gas equilibrium* 의 forward-time 분석 도구 → de Bruijn–Newman Λ ≤ 0 채널.
- 신호처리 *minimum-phase factorization* → mollifier 가족의 새 mollifier 후보.

### C. 외부인 설명 (다음 시도들이 답해야 할 질문)
- *물리학자*: "ζ 가 어떤 *구체적 물리계* 의 partition function 인가?" — Mellin-tranform 물리계가 있나?
- *제어공학자*: "primes 의 *transfer function* 이 있다면 그것의 *root locus* 분석은?"
- *논리학자*: "RH 가 ZFC 에서 결정 가능? Π_1 statement 이므로 *false* 면 finite proof 가능."

### D. 문제 변형
- **약화**: zero-free region 강화 → 임계선 ε 너머. (해석적, 알려짐)
- **강화**: GRH, Lindelöf — 동시 추구.
- **일반화**: function field (Weil 의 도구가 *왜 옮겨가지 않는지* 가 핵심).
- **특수화**: 작은 height 영점에 한정, simple 영점 가정 — 단순화된 sub-problem.

## Specialist 라운드 (시작) → `specialist_round.md`

다음 5명 Tier 1 + 2명 Tier 2 호출:
- S1 해석적 정수론자
- S2 대수기하·function field
- S3 NCG·작용소대수
- S4 RMT·확률
- S5 조합·하드해석 (Tao 류)
- S6 양자물리 (de Bruijn–Newman 의 물리적 해석 검토)
- S9 논리·증명론자 (RH 의 metamathematical 시각 — 새 채널)

## Computational verifications (HARNESS §8)

- baseline sanity: `tools/verify_zeros.py -n 50` (이미 동작 — 첫 50개 영점 검증)
- 다음 시도들이 자주 호출할 *공통* 데이터셋 미리 캐싱:
  - 첫 1000 영점 imag part 저장 (mpmath dps=50)
  - $M(x)$ for $x \le 10^4$ 저장
- 본 시도 자체에서는 *정량적* 코드 호출 적음 — 다음 시도 baseline 데이터 준비.

## 기록 흐름

1. **본 strategy.md** (현재) — orientation 의 사전 plan.
2. `specialist_round.md` — 7명 specialist 호출 결과.
3. `work.md` — 시간순 메모, 발견, 막힘.
4. `postmortem.md` — 결과 + 다음 시도 후보 3개.
