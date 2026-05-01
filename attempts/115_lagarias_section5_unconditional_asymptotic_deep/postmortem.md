# Postmortem — Attempt 115 (Mode A deep, 8 components)

Lagarias-Li 2004 §5 Unconditional Asymptotic deep:
- Theorem 5.1 (eq 5.1): S_∞(n, π) = (N/2) n log n + C_1(π) n + O(N(K(π)+1)).
- C_1(π) = (N/2)(γ - 1 - log(2π)) + (1/2) log Q(π).
- C_1(π_triv) = (1/2)(γ - 1 - log(2π)) ≈ -1.1303307.
- Lemma 5.1 (T_20): β_∞ = ∫_1^∞ e^(-t/2) dt/t ≈ 0.559774.
- Lemma 5.2 (T_21): α_∞ = ∫_0^1 (1 - e^(-t/2)) dt/t ≈ 0.443842.

## Numerical (5+ decimal places)
- C_1(π_triv) = -1.1303307008 (paper -1.1303307).
- β_∞ = 0.5597735948 (paper 0.559774).
- α_∞ = 0.4438420791 (paper 0.443842).
- S_∞(100, π_triv): 116.975 (실제 eq 4.11) vs 117.225 (asymptotic prediction), rel err 0.2%.

## Wall #6 paper-direct origin
λ_n = S_∞ (unconditional, §5) - S_f (RH-conditional, §6) + δ.
*cancellation* 가 우리 wall taxonomy 의 paper-direct.

## Wall #6 quantitative cancellation
β_∞ + (1/2)α_∞ - 1/2 ≈ 0.282 (paper §5 Lemma 5.1+5.2 합).

## Lemma 3 14th evidence
unconditional asymptotic for S_∞ — partial unconditional form.

## Specialist Δ
- Lagarias: "technical asymptotic via Stirling, no surprise, RH 진전 X."
- Sarnak: "classical asymptotic, family progress X."

## Honest scope
*novel content 0/10*. paper-direct deep + numerical 정확 검증 + Lemma 3 14th evidence + Wall #6 paper-direct origin.

## HARNESS
- ledger 115 (Type A, Mode A deep 8 components).
