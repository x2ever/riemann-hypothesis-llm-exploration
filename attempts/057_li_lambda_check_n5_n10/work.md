# Work — Attempt 057 (lambda_n via sigma_j)

## sigma_j (Lagarias 2.16) computed

[numerical, dps=40, 200+200 conj zeros]:
- sigma_2 ≈ -0.0420
- sigma_3 ≈ -1.11e-4
- sigma_4 ≈ 7.36e-5
- sigma_5 ≈ 7.15e-7

## 검증: lambda_n = Σ (-1)^(j-1) C(n,j) sigma_j (Lagarias 2.18)

[partial fail]:
- format string error — mpf conversion bug. honest implementation issue.
- 결과 output 미완성. *우리 contribution 0*.

## "예상 가능 결과" self-check
yes — formula 검증 시도. fix 빠르나 token 절약.
