# Work — Attempt 044

[numerical, dps=50, 200 zeros]

| n | λ_n | Voros prediction | ratio |
|---|---|---|---|
| 10 | 2.07 | 0.21 | 9.89 (sub-asymptotic) |
| 30 | 16.70 | 17.11 | **0.976** |
| 50 | 38.38 | 41.28 | 0.930 |
| 100 | 98.03 | 117.23 | 0.836 |
| 200 | 224.72 | 303.77 | 0.740 |
| 500 | 495.80 | 988.49 | 0.502 |
| 1000 | 544.75 | 2323.55 | 0.234 (severe truncation) |

## 분석

[rigorous]:
- n=30 sweet spot (200 zeros 에서): ratio 0.976.
- 500 zeros 에서는 sweet spot n=50 (ratio 0.985, attempt 040).
- → *zero count* ↑ 함께 *valid n range* ↑ — 정량 truncation crossover.

## "예상 가능 결과" self-check
yes — paper-direct numerical, attempt 040 pattern 의 fast 검증.
