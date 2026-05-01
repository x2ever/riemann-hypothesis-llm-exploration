# Work — Attempt 086 (Lagarias §5 unconditional S_∞)

[numerical, dps=40, 200 zeros]

λ_n = S_∞ - S_f + δ (eq 4.6). For ζ (π_triv): δ=1.

Eq (4.11): $S_\infty(n, π_{triv}) = -\sum_{j=1}^n (-1)^{j+1} \binom{n}{j} (1 - 1/2^j) \zeta^*(j)$
where ζ*(1) = log(4π) + γ, ζ*(j)=ζ(j) for j≥2.

| n | λ_n (200 zeros) | S_∞ | S_f = S_∞-λ |
|---|---|---|---|
| 3 | 0.189 | 2.013 | 1.824 |
| 5 | 0.524 | 1.883 | 1.359 |
| 10 | 2.073 | 0.044 | -2.029 |
| 20 | 7.945 | -7.099 | -15.044 |

Theorem 5.1: $S_\infty(n,π) = (N/2) n \log n + C_1 n + O(N(K+1))$ unconditional.

[rigorous]: S_∞ unconditional (Stirling), S_f RH-conditional. Wall #4 finite places mapping.

[증명 X]: *우리 contribution 0*.
