# Work — Attempt 072 (ζ'/ζ identity sanity)

[numerical, dps=30]

## ζ'/ζ(s) = -Σ Λ(n)/n^s (Re s > 1)

| s | ζ'/ζ direct (mpmath) | -Σ Λ/n^s (n≤1000) | diff |
|---|---|---|---|
| 2 | -0.569961 | -0.568959 | 0.001 (truncation) |
| 3 | -0.164823 | -0.164822 | 1e-6 (well-converged) |
| 1.5 | -1.505235 | -1.441928 | 0.06 (slow convergence near s=1) |
| 1.1 | -9.441036 | -4.428253 | 5.0 (very slow, near pole) |

[rigorous]: 알려진 Dirichlet series identity. n=1000 truncation 으로 s>2 에서 정확, s→1 에서 발산 가깝게 슬로우.
[증명 X]: *우리 contribution 0*.

## "예상 가능 결과" self-check
yes — known truncation behavior.
