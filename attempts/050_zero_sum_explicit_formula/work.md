# Work — Attempt 050 (Explicit formula sanity)

[numerical, dps=30, x=100, N=100 zeros]

## ψ(100)
- Direct (Λ(n) sum): 94.045
- Formula (100 zeros): 93.670
- Difference: 0.375

## 분석 (suppressed confidence, 045 protocol)

[rigorous]:
- $\psi(x) = x - \sum_\rho x^\rho/\rho - \log 2\pi - (1/2)\log(1-x^{-2})$ (Riemann-von Mangoldt explicit formula).
- Truncation: 첫 N=100 zeros 합 → 무한합 absolute convergence X (conditional only).
- Difference 0.375 = N=100 truncation 잔차.

[증명 X]:
- 알려진 *truncation* analysis. *우리 contribution 0*.
- 도구 explicit_formula sanity 만 — paper SOTA: high precision (Riemann-Siegel) 으로 ψ(x) 의 RH-equivalent 정량 검증.

## "예상 가능 결과" self-check
yes — 알려진 truncation behavior.
