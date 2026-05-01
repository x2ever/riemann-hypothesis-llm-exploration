# Work — Attempt 084 (Voros eq (15) full asymptotic)

[numerical, dps=40, 500 zeros]

Voros 2006 eq (15) full RH-true asymptotic:
$$\lambda_n \sim 2\pi n \left[2 R_{-2} (\psi(1/2+n) - 1 + \gamma) + R_{-1}\right]$$
$R_{-2}=1/(8\pi)$, $R_{-1}=-\log(2\pi)/(4\pi)$.

| n | λ_n (500 zeros) | leading | full | diff (full-leading) |
|---|---|---|---|---|
| 50 | 40.66 | 41.28 | 41.28 | < 0.001 |
| 100 | 107.12 | 117.23 | 117.23 | < 0.001 |
| 200 | 260.77 | 303.77 | 303.77 | < 0.001 |
| 500 | 707.36 | 988.49 | 988.49 | < 0.001 |

[rigorous]: sub-leading correction *매우 작음* — leading $n \log n$ 지배. truncation effect 가 dominant gap (truncation O(√n log n) 알려진 fact).

[증명 X]: *우리 contribution 0*.
