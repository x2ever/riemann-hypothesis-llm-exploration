# Work — Attempt 078 (Farey-Franel-Landau 1924)

[numerical]

Franel-Landau: RH ⟺ Σ |F_i - i/N|² = O(N⁻¹⁺ᵋ).

| n | N=#F_n | Σ|F_i-i/N|² | bound N⁻¹ | Σ|F_i-i/N| | bound √N |
|---|---|---|---|---|---|
| 10 | 33 | 0.0203 | 0.030 | 0.653 | 5.74 |
| 20 | 129 | 0.0158 | 0.0078 | 1.016 | 11.36 |
| 50 | 775 | 0.0089 | 0.0013 | 1.610 | 27.84 |
| 100 | 3045 | 0.0050 | 0.000328 | 2.089 | 55.18 |

[rigorous]: 작은 N에서 일관, asymptotic 결정 불가.

[증명 X]: known elementary RH-equivalent. *우리 contribution 0*.
