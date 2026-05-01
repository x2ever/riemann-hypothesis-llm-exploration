# Work — Attempt 134 (Optimal Test Function for Weil Formula — *NOVEL*)

## Numerical
| family | param | LHS (zeros) | RHS (primes) | ratio |
| Gaussian | σ=10 | 1.07 | 10.54 | 0.10 |
| Gaussian | σ=50 | 30.45 | 10.54 | 2.89 |
| Gaussian | σ=100 | 86.80 | 10.54 | 8.23 |
| Fejer | T=200 | 18.13 | 107.27 | 0.17 |

## Finding
- Gaussian σ small → LHS ≪ RHS (zeros decay too fast).
- Gaussian σ large → LHS ≫ RHS (primes truncation).
- *crossover* at σ ≈ 30: LHS ≈ RHS.
- Fejer (compact support) → 균형 not reached at T=200.

## Failure
- *No optimal h* 발견. trade-off Heisenberg-like (Conrey 2003 §Weil).
- 본 시도 = paper-direct 알려진 *bandlimited* test function research 의 naive 재현.

## Honest scope
*paper-direct rediscovery*. Selberg / Burnol bandlimited test function literature. novel content X.
