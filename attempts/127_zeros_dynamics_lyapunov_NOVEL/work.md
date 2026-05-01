# Work — Attempt 127 (ζ-zeros Lyapunov Sensitivity — *NOVEL FAILURE/finding*)

## Hypothesis
Rodgers-Tao 2020 zero dynamics: ∂_t x_k = 2 Σ 1/(x_k - x_j). 단일 zero perturbation 의 *propagation*?

## Numerical
- 30 zeros, perturb γ_5 by +0.01.
- 5 forward steps (dt=0.005).

| Behavior | Pattern |
|---|---|
| Boundary effect | γ_25, γ_28, γ_29, γ_30 (top boundary) shift +0.01 to +0.016 (largest) |
| γ_5 itself | +0.005951 (smaller than initial 0.01 — repulsion 분산) |
| Most neighbors | -0.005 to -0.01 (attractive shift towards perturbed zero) |
| Long-range | shift |γ_25 - γ_5| ≈ 56, but shift 11.5e-3 — 일관 *non-decay* due to *cumulative force from boundary* |

## *Observation*
- *boundary effect dominant*: far-from-perturbed zero (top) shifts more than middle. *truncation artifact* (no force from γ_31, γ_32, ... pulls top zeros).
- 우리 numerical = *finite-N truncation* — paper §1.5 (Rodgers-Tao 2020) 의 *integrated energy* 가 *infinite N* 형태.

## Failure analysis
- *Truncation effect dominant*: 30 zeros 에서 boundary force 균형 깨짐.
- *physical Lyapunov spectrum* 추출 X (정확 dynamics는 *paper §1.5 quantitative tool* 외).
- *novel pattern X*: *truncation artifact* 만.

## Wall #2 cross-link (Rodgers-Tao 2020)
paper §1.5 quote: "control integrated energies that resemble ∫_{Λ/2}^0 E(t) dt".
- 우리 numerical 가 *finite-N + finite-t* — paper full *infinite limit* 부재.
- *우리 도구 fundamental limitation* (attempt 118 의 same lesson).

## Honest scope
*novel content X*. *truncation artifact dominant*. paper-direct *infinite limit* 부재.
