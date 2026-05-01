# Work — Attempt 074 (Dirichlet η(s))

[numerical, dps=30]

η(s) = (1 - 2^(1-s)) ζ(s).

## η at ζ zeros (should be 0)
| ρ | |η(ρ)| |
|---|---|
| 0.5+14.135i | 1.5e-30 |
| 0.5+21.022i | 8.9e-31 |
| 0.5+25.011i | 2.6e-30 |

## η extra zeros at s = 1 + 2πin/log 2
| n | s | |η(s)| |
|---|---|---|
| 1 | 1+9.0647i | 6.5e-16 |
| 2 | 1+18.13i | 1.8e-15 |
| 3 | 1+27.19i | 2.0e-15 |

[rigorous]: η zeros = ζ zeros + extra at Re=1 (where 2^(1-s) = 1). 알려진 factorization. *우리 contribution 0*.

## "예상 가능 결과" self-check
yes.
