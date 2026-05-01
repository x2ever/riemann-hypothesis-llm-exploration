# Work — Attempt 058 (N(T) sanity)

[numerical, mpmath.nzeros]

| T | #zeros | N(T) predicted | diff |
|---|---|---|---|
| 50 | 10 | 9.42 | +0.58 |
| 100 | 29 | 29.00 | -0.00 |
| 200 | 79 | 79.19 | -0.19 |
| 500 | 269 | 269.59 | -0.59 |

Riemann-von Mangoldt $N(T) \sim T/(2\pi)\log(T/(2\pi)) - T/(2\pi) + 7/8$ — *알려진 fact* mpmath sanity. diff = S(T) = O(log T).

[증명 X]: *우리 contribution 0*.
