# Specialist 패널 누적 합의·불일치 추적

> 시도 가로질러 specialist 들의 *반복적 의견* 과 *지속적 불일치* 를 추적. 패턴이 보이면 RH 본질에 대한 단서.

## 사용법

각 시도 종료 후 본 파일에 specialist 별 1-2줄 요약 추가.

## Specialist 별 누적 (시도 N회 진행 후 채워나감)

### S1. 해석적 정수론자
- [000] mollifier 50% 벽 / Cauchy–Schwarz sharp 못 닿음. RH 는 *해석학 외부* 에서 해결 가능성. families 가 main current.
- [001] λ_n 은 position-dependent — RMT model scope 외. Keating–Snaith moments 가 더 적절.

### S2. 대수기하학자 / Function field
- [000] function field RH 풀린 도구 (Riemann–Roch + algebraic index + étale cohomology + Frobenius) 의 *number field 대응물 부재* — Bombieri Clay 의 핵심 미해결.

### S3. 작용소대수·NCG
- [000] Connes trace formula 가 RH 동치 *변형*. 한쪽 (Weil distribution 양정치성) 의 독립적 증명 필요. 25년 진화 정성적, 정량 부족.

### S4. RMT / 확률
- [000] GUE 와 영점 통계 정합 — 강한 evidence 이지만 model ≠ proof. unconditional GUE conjecture 자체 미증명.
- [001] RMT 의 정합성 statement 는 *normalized local* 위에서. raw quantity (λ_n) 비교는 fail 이 정상.

### S5. 조합·하드해석 (Tao 류)
- [000] Λ ≥ 0 (Rodgers–Tao) 풀림. forward-time 비대칭이 Λ ≤ 0 (=RH) 의 본질 장애. 5년 무진전.
- [001] cross-check 의 *informative-zone 명료화* 가 valuable. RH 직접 기여 X 이지만 도구 진화.

### Tier 2 (호출된 시도에서만)
- [000] S6 양자물리: BBM self-adjointness gap. 물리 도구는 *후보 발견* 강력, *증명* 약함.
- [000] S9 논리: RH 는 Π_1 statement. ZFC 독립성 가능성 미상. 직접 증명 도구로는 약함.
- [001] S11 자유확률: Σ λ_n z^n 의 R-transform — 미탐색 채널. 새 후보 도출 (`004_li_lambda_rtransform`).

## 반복 합의 (모든 specialist 가 같은 방향 가리킴)

특정 *기술적 장애물* 에 대해 다수 specialist 가 동의하면 그것이 RH 의 가장 본질적 어려움일 가능성.

- **[000] "양정치성의 산술적 source 부재"**: S2 (Hodge index 의 number field 대응 부재) + S3 (Weil distribution 양정치성 미증명) + S6 (Lee–Yang 류 직접 import 어려움) 가 모두 *같은 본질* 의 다른 표현으로 보임. 5개 벽 (`walls.md`) 의 메타 가설 = 통합 양정치성.
- **[000] "families view"**: S1 (Conrey 결론) + S4 (Katz–Sarnak) + S2 (function field family) 가 single ζ 보다 family 시각이 main current 라는 데 동의.

## 지속 불일치 (specialist 간 합의 안 됨)

서로 다른 분야 사람이 끝까지 다른 답을 내는 지점.

- (000 에선 *심각한* 불일치 없음 — 모두 어렵다 + 분야별 한계로 수렴.) 이것 자체가 의심 신호: confirmation bias 가능성.

## 모든 분야 격차 (어느 specialist 도 답 못 함)

진짜 미지의 영역. 새 도구·새 분야가 필요할 수 있는 곳:

- **[000] forward-time zero 동역학 통제** — S5 만 인지, 답 X. (벽 #2)
- **[000] Frobenius 대응물 in characteristic 0** — S2, S3 모두 인지, 답 X. (벽 #1)
- **[000] Riemann 본인의 *원래 마음속 증명 시도* 흔적** — Siegel Nachlass 일부 외 미상.
- **[000] PA / ZFC 위 RH 의 위치** — S9 가 분야 분리로 답 못 함. 직접 도구 X.

## 운영 결함 발견 (HARNESS §7 개선)

- [000] **결함 1**: S2 와 S3 의 답이 빠르게 confirmation 으로 수렴. *blind* 라운드 가치.
- [000] **결함 2**: Tier 1 의 5명 분류에서 *대수기하* (function field, étale) 와 *대수적 정수론* (Iwasawa, families) 이 S2 안에 혼재. 분리 권장.
- [000] **결함 3**: 반환 라운드 (postmortem 시 specialist 재호출) 미시도. 다음 시도에서 첫 검증.
- [001] **결함 3 검증**: 반환 라운드 첫 시도. *작은 가치* 만 산출 (S11 의 R-transform 후보 1개). 본 시도의 small-attempt scope 와 ROI 안 맞음 — *큰 막힘 시도* 에서 반환 라운드가 더 의미. 향후 attempt size 와 반환 라운드 trigger 를 연계.
