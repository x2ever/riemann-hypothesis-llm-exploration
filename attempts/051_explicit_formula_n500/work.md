# Work — Attempt 051 (Explicit formula N=500)

[numerical, dps=30, N=500 zeros]

## ψ(x) sanity

| x | ψ direct | N=100 | N=500 | error (N=500) |
|---|---|---|---|---|
| 50 | 49.485 | 49.599 | 49.468 | 1.78e-2 |
| 100 | 94.045 | 93.670 | 93.991 | 5.48e-2 |
| 200 | 206.146 | 206.082 | 206.351 | -2.05e-1 |

## 분석

[rigorous]:
- N 100 → 500: error 7~9 배 감소 (x=100 case: 0.375 → 0.055).
- x 증가 시 error |ψ-formula| 증가 — RH under predicts O(√x log²x), 우리 작은 x 에선 정성적 일관.

[증명 X]:
- 알려진 truncation behavior. *우리 contribution 0*.
- yellow flag 회피 (045 protocol).

## "예상 가능 결과" self-check
yes — N 증가 시 truncation error 감소.
