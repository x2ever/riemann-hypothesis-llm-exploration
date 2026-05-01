# Work — Attempt 069 (ζ special values)

[numerical, dps=30]

## ζ at integer arguments
| s | ζ(s) | Predicted | diff |
|---|---|---|---|
| 2 | 1.6449340668 | π²/6 = 1.6449340668 | 0 |
| 4 | 1.0823232337 | π⁴/90 = 1.0823232337 | 2.2e-16 |
| 0 | -0.5 | -1/2 | 0 (exact) |
| -1 | -0.0833... | -1/12 | 0 (exact) |
| -2 | 0 | 0 (trivial zero) | 0 |
| -3 | 1/120 = 0.00833 | exact | 0 |

[rigorous]: 알려진 ζ special values 의 mpmath sanity. RH 와 직접 무관.
[증명 X]: *우리 contribution 0*.

## "예상 가능 결과" self-check
yes — paper textbook values.
