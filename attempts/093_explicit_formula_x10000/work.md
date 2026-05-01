# Work — Attempt 093 (ψ(x) explicit formula at x=10000)

[numerical, dps=30, N=500 zeros]

| | value |
|---|---|
| ψ(10000) direct (Λ sum) | 10013.397 |
| ψ(10000) formula (N=500) | 10019.020 |
| diff | -5.62 |
| Schoenfeld (RH) bound √x log²x/(8π) | 337.5 |

[rigorous]:
- diff 5.62 = N=500 truncation 잔차.
- Schoenfeld 1976 bound 337.5 — 우리 diff 안.
- N→∞ 시 diff→0.

[증명 X]: *우리 contribution 0*.
