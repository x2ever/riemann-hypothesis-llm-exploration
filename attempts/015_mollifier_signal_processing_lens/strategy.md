# Attempt 015: Mollifier through Signal-Processing Lens
**Type**: A (Proof attempt, exploratory cross-domain)

## 가설/전략

Pratt-Robles (2019, arXiv:1802.10521) 정독 (§1.1, §1.2) — 핵심 quote (paper §1.2 끝):

> "there does not seem to be a random matrix analogue of mollifying as there is nothing that naturally corresponds to a partial Dirichlet series"

이건 RMT 측 specialists 가 *명시적 인정* 한 갭. 본 시도의 가설:

> **H1 (cross-domain bridge candidate)**: N. Levinson 1947 *Levinson–Durbin recursion* (signal processing AR model) 와 N. Levinson 1974 *mollifier method* (analytic NT) 사이에 *non-trivial bridge* 가 있을 수 있다 (동일인 N. Levinson, Toeplitz inverse / autocorrelation 형식 유사성).

> **H2 (negative)**: 두 algorithm 이 *이름만 공유* 본질 다를 수도. Honest scope 유지.

## 동기

- Wall #3 (SHARP-CONSTANT) 의 50% 벽 — mollifier optimization 의 *변분 한계*. 만약 AR model 의 *Yule-Walker / reflection coefficient* 시각이 적용 가능하면 새 angle.
- 외부 critique 반영 — *예상 가능 zone 외부* 시도. 본 가설은 (literature 검색 negative) 미탐색 가능성.
- Cross-domain bridge: 정수론 ↔ signal processing.

## 분류
- I (해석적/mollifier) + XI (비정통, 신호처리) + IX (computational).

## Specialist 의무 호출
- S1 (해석적): mollifier 의 정수론 측 시각.
- S10 (CS/algorithms): Levinson-Durbin 의 algorithm 측 시각.
- *진짜 specialist* 가 아닌 LLM 시뮬레이션 — HARNESS §7 한계 명시.

## DoD

- [ ] Pratt-Robles paper §3 "Constructing a mollifier" 의 polynomial $Q(x)$ 형태와 AR model 의 polynomial 비교.
- [ ] *형식 일치 vs 수학적 동치* 분리 (lemma `spectral_candidate_circularity_check.md` 의 lens 적용).
- [ ] 만약 *진짜 다리* 후보 발견 → `lemmas/levinson_durbin_mollifier_correspondence.md` (open question) 기록.
- [ ] 만약 *이름만 공유* 결론 → 그 자체 lemma 로 (open question 종료).

## 명시적 한계 (외부 critique 인정)

- 본 시도는 *논리적 hypothesis 형성 단계*. *novel mathematical content X* 가 likely outcome.
- 본 가설이 알려진 결과 (literature 한계) 가능성도 인정.
- "흥미로운 연결" 톤 회피 — *수학적 동치 증명이 없으면 brainstorm 단계*.

## 예상 결과

(예상 가능 zone self-check):
- 두 Levinson method 가 *형식적으로 유사* — 예상 가능 (둘 다 Toeplitz / autocorrelation).
- *수학적 동치* — 미상. literature 검색 negative 이지만 검색 한계.
- *RH 진전* — 0/10 거의 확실 (외부 critique 의 honest 위치).

→ 본 시도의 *진짜* 가치는: **(1) Pratt-Robles paper 깊이 정독 — 향후 시도들의 입력. (2) cross-domain bridge candidate 의 명시화 (open question 형태). (3) 그것이 알려진 답이 있는지 검증 후속.**
