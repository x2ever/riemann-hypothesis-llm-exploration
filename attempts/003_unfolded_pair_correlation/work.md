# Work — Attempt 003

## 2026-05-01 — Run #1 (N=300)

[numerical, dps=30, N=300, bins=15, max_gap=3.0]

### 결과 요약

- pair gaps with d ≤ 3: 547
- KS statistic: 0.0572
- KS p-value (asymp): 0.05599
- **Verdict: AMBIGUOUS** (간신히 reject 임계 안)

### Regional ratios (empirical / GUE)

| u 영역 | ratio | 해석 |
|---|---|---|
| [0, 0.5] | 0.325 | small gaps *현저히 적음* (level repulsion 강함) |
| [0.5, 1.0] | 0.920 | 정합 |
| [1.0, 1.5] | 1.089 | 살짝 과잉 |
| [1.5, 2.5] | 1.087 | 살짝 과잉 |

### 자기 비판적 분석 — Normalization issue

[hand-wave] 본 시도의 *empirical density* normalization 이 GUE pair correlation density (1 - sinc²) 와 *직접 비교* 가능한지 의심.

- GUE pair correlation function $R_2(u) = 1 - (\sin\pi u/\pi u)^2$ 는 *intensity ratio* (mean density 로 나눈) 이지 *probability density* X.
- 본 코드의 empirical density 는 pair gap 의 *probability density* — 둘 다 *형태* (shape) 만 비교 가능, *절대값* 매칭 X.
- 따라서 ratio 들이 1 에서 멀어진 것 자체는 *normalization 부정확* 산물 가능성 높음.

[plausible] 이 분석.

### 그러나 *형태* 정보는 있음

normalization 문제 빼고 *형태* 만 보면:
- empirical 의 *0 근처 결핍* (small gaps suppression) — GUE 의 level repulsion 과 일치 *방향*
- 단, 강도가 GUE 예측의 1/3 — *지나치게 강한* repulsion 신호 가능성
- 또는 finite-N (300) 의 statistical fluctuation
- 또는 실제 RMT universality 가 *low height* 에서 깨지는 정량 신호

### KS test 의 의미

[plausible] KS p = 0.056 자체도 normalization 의 산물일 수 있음. KS test 는 *CDF* 비교인데 GUE side CDF 정의 자체가 모호. 본 결과는 *qualitative* 만 신뢰.

### 결론 — 본 시도의 위치

[rigorous]:
- cross_check.py framework 가 *연속 quantity* 에 직접 적용 X — 본 시도가 그것을 *발견*. attempt 002 의 도구 한계 검증.
- normalization 의 정확화 없이 KS / regional analysis 의 quantitative 결론은 *premature*.
- 다만 small-gap suppression 의 *질적* 신호는 견고 — 다음 시도가 정량 해야 함.

### 본 시도 학습
1. **도구 한계 발견**: cross_check.py 의 *integer-indexed* 가정이 연속 quantity 에 안 맞음. 향후 generalization 필요 (Type C 후보).
2. **normalization 의 중요성**: 형태 비교에선 *동일 normalization* 강제 — 통계 정합 검증의 fundamental.
3. **finite-N effect**: N=300 으로는 RMT universality 의 sharp 검증 어려움. Odlyzko 의 millions 와 우리의 hundreds 사이의 정보 격차 인지.

### 다음 시도 후보

1. **004 — normalization 정확 후 동일 분석**: empirical 와 GUE 양쪽을 *동일 형식* (probability density 또는 intensity ratio) 로 통일 후 재계산.
2. **005 — N 확장**: 1000~5000 영점까지 확장 (mpmath 시간 비용 검토).
3. **006 — 다른 quantity**: nearest-neighbor spacing distribution (P(s)) 직접 — pair correlation 보다 normalization 단순.
