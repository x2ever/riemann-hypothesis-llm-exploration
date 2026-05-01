# Work — Attempt 047 (Pair correlation N=500)

[numerical, dps=30, N=500, bins=25, max_gap=3.0]

## Density 비교

| u | empirical | GUE 1-(sin πu/πu)² |
|---|---|---|
| 0.060 | 0 | 0.012 (level repulsion) |
| 0.300 | 0.067 | 0.263 |
| 0.660 | 0.367 | 0.821 |
| 0.900 | 0.952 | 0.988 |
| 1.020 | 0.718 | 1.000 |
| 1.260 | 0.935 | 0.966 |

## 분석 (suppressed confidence, 045 protocol)

[rigorous]:
- empirical pair density 가 small u 에서 *낮음* — level repulsion 의 *방향* 일관 (Odlyzko millions 와 일관).
- 절대값 비교는 *normalization mismatch* — 003 attempt 의 lesson (Wall #6 attempt 001 발견).
- *qualitative* signal: GUE 와 *방향* 일치, *quantitative* match 는 N=500 에서 부족.

[증명 X]:
- 우리 contribution = 도구 검증 (N=300 → 500 sample 확장).
- *novel content X*.
- 정합성 평가 → 004 의 KS p=0.27 (Wigner P(s)) 가 더 정확 비교.

## "예상 가능 결과" self-check
yes.
