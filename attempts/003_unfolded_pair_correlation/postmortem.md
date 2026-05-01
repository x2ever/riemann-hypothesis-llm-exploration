# Postmortem — Attempt 003

## 결론

**부분 성공 + 도구 한계 발견**.

- unfolded pair correlation 비교 실행 ✅
- KS p=0.056 (AMBIGUOUS) — quantitative 해석은 normalization 정확화 필요
- *small-gap suppression* 의 질적 신호 발견 (level repulsion *방향* 일치)
- **cross_check.py 의 한계 발견** — 연속 quantity (correlation density) 에 직접 적용 X

## 무엇이 작동했나

- 도구 (`tools/unfolded_pc_extended.py`) 작성 + 실행 — 새 모듈.
- 자기 비판: normalization 문제를 *postmortem 단계 전* (work.md) 에서 인지 — premature 결론 회피.
- finite-N effect 의 정량 신호 (small-gap region 의 ratio 0.325).

## 어디서 막혔나

- **본질적**: GUE pair correlation density vs empirical pair-gap probability density 의 *normalization 동치성* 미정의. KS test 와 ratio 의 quantitative 결론을 못 냄.
- **도구**: cross_check.py 가 integer index 만 — 연속 u 에 적용 X.

## 알려진 벽인가, 새로운 벽인가

알려진 (RMT 문헌의 normalization convention) 벽 — *재발견*. 다음 시도가 normalization 을 정확히 한 후 비교해야.

`learnings/walls.md` 새 벽 후보:
- **벽 #7 (NORMALIZATION-MISMATCH)**: 두 quantity 비교 시 *normalization* 자체가 동치 아닐 수 있음. 형태/절대값 분리 필요.
  - 단, 이는 *기술적* 벽 — 본질적 RH 벽이 아니라 *비교 방법론* 벽. wall 분류에서 분리.

## 다음 시도 후보

### 004 — `nearest_neighbor_spacing` (Type A)
**가설**: nearest-neighbor spacing distribution P(s) — Wigner surmise $P_{GUE}(s) = (32/\pi^2) s^2 e^{-4s^2/\pi}$ 와 비교. P(s) 는 normalization 명확 (probability density on s ≥ 0).

- 분류: VII + IX.
- 도구: `tools/spacing_distribution.py` 신규.
- DoD: N=300+ 영점 + KS / Wasserstein-1 distance to Wigner.

### 005 — `cross_check_continuous` (Type C)
**가설**: cross_check.py 를 *연속 quantity* (probability density, intensity ratio) 에 일반화. attempt 003 에서 부족했던 도구.

- 분류: harness maintenance.
- DoD: 새 함수 `cross_check_density()` + smoke test.

### 006 — `n_extension_up_to_5000` (Type A 인프라)
**가설**: N=5000 영점 캐싱 (mpmath 시간 비용 큼). 향후 모든 RMT 비교의 baseline.

- 분류: IX (computational infrastructure).
- 비용: mpmath dps=30 with N=5000 약 시간 단위. 한 번 캐시.

## 추출된 보조정리/관찰

- 없음 — 본 시도는 quantitative 결론 X.
- *방법론적 관찰* (work.md 에 기록).

## 학습 누적

- `learnings/walls.md` — 벽 #7 후보 추가 ☐
- `learnings/approaches_taxonomy.md` — Combo 4 가 002 일반화 후 더 sharp ☐
- `learnings/specialist_consensus.md` — S4 의 normalization 강조 강화 ☐

## HARNESS 갱신
- ledger 에 003 추가 — Type A small computational, partial success.

## 메타 — Type A 의 ROI

- 001, 003 둘 다 *negative finding* (각각 LOCAL-GLOBAL-MISMATCH, NORMALIZATION-MISMATCH).
- *negative finding* 들이 도구 / 방법론 명료화로 가치 — 누적 시 다음 시도들의 효율 향상.
- 그러나 *3개 연속 negative* 시 시도 방식 자체 재검토 필요 (Type D reflection trigger).
