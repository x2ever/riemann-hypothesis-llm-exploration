# Work — Attempt 070 (|ζ(1/2 + it)| samples)

[numerical, dps=30]

| t | |ζ(1/2 + it)| | convexity bound t^(1/4) | Lindelöf t^ε |
|---|---|---|---|
| 10 | 1.549 | 1.778 | ≈1 |
| 50 | 0.341 | 2.659 | ≈1 |
| 100 | 2.693 | 3.162 | ≈1 |
| 500 | 1.472 | 4.729 | ≈1 |
| 1000 | 0.998 | 5.623 | ≈1 |
| 5000 | 0.804 | 8.409 | ≈1 |

모든 t 에서 |ζ| ≤ convexity bound (t^1/4) — *trivial sanity*. Lindelöf bound (RH 가정 시 O(t^ε)) 와도 정합.

[증명 X]: *우리 contribution 0*.

## "예상 가능 결과" self-check
yes — Lindelöf 알려진 fact.
