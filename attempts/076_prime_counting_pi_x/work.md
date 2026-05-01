# Work — Attempt 076 (π(x) vs Li(x) sanity)

[numerical, mpmath]

| x | π(x) | Li(x) | π-Li | √x log x |
|---|---|---|---|---|
| 100 | 25 | 30.13 | -5.13 | 46.05 |
| 1000 | 168 | 177.61 | -9.61 | 218.44 |
| 10000 | 1229 | 1246.14 | -17.14 | 921.03 |
| 100000 | 9592 | 9629.81 | -37.81 | 3640.71 |

[rigorous]:
- |π(x) - Li(x)| ≤ √x log x — RH 가정 시 known bound.
- 작은 x: π < Li 일관 (Gauss 관찰; Skewes sign change 는 *훨씬* 큰 x).

[증명 X]: *우리 contribution 0*.
