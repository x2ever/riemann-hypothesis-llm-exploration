# Work — Attempt 092 (Wall #4 — Density theorem quantitative)

[numerical]

N(σ, T) bounds:
- Carlson 1920: O(T^{4σ(1-σ)+ε})
- Ingham 1940: O(T^{3(1-σ)/(2-σ)+ε}) for σ ∈ [1/2, 3/4]

| σ | Carlson 4σ(1-σ) | Ingham 3(1-σ)/(2-σ) |
|---|---|---|
| 0.50 | 1.000 | 1.000 |
| 0.60 | 0.960 | 0.857 |
| 0.70 | 0.840 | 0.692 |
| 0.75 | 0.750 | 0.600 |
| 0.80 | 0.640 | 0.500 |
| 0.90 | 0.360 | 0.273 |
| 1.00 | 0.000 | 0.000 |

Ingham > Carlson (sharper) for σ ∈ [1/2, 3/4]. σ=1 zero-free.

[증명 X]: paper-direct quantitative. *우리 contribution 0*.
