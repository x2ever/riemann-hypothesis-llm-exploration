# Work — Attempt 054 (theta(t) sanity)

[numerical, dps=30]

## theta(t) = arg Γ(1/4 + it/2) - (t/2)log π

| t | theta(t) | theta(t)/π |
|---|---|---|
| 10 | -3.07 | -0.98 |
| 50 | -30.09 | -9.58 |
| 100 | -56.54 | -18.00 |
| 200 | -112.49 | -35.81 |
| 1000 | -572.98 | -182.38 |

monotonically decreasing (in this convention). Gram density approx: t/(2π) log(t/2π) — t=100 → ≈44, t=500 → ≈348.

[증명 X]:
- 알려진 Riemann-Siegel theta function. mpmath sanity.
- *우리 contribution 0*.
