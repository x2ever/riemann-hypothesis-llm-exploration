# Attempt 111: Connes-Consani 2021 §1-§2 ζ-cycle DEEP
**Type**: A (Mode A deep, 8 components)

## Cut self-check (`lemmas/dont_try_directions.md`)
- Cut 5 (모든 spectral 후보 = circular):
  - Connes-Consani 2021 spectral triple Θ(λ, k) — D(λ, k) 정의에 ζ 부재.
  - paper 자체 numerical *coincidence* 명시 (31 zeros 일치 random prob ~10^-50).
  - special λ values (ζ-cycle) 만 eigenvalues 일치 — not all λ.
  - Lemma 1 (1, 2) *NO* — not circular by construction. cut X.

## DoD
- §1 abstract + Figure 1 (λ²=10.5, k=18: blue iD spectrum vs red ζ zeros).
- §1 Definition 1.1 (ζ-cycle) + Theorem 1.1.
- §1 D(λ, k) = (1 - Π(λ, k)) ∘ D_0 ∘ (1 - Π(λ, k)) (eq 1.5).
- §1 prolate spheroidal wave functions ψ_{m,λ}(x) = PS_{2m,0}(2π λ², x/λ).
- §2 semi-local Weil quadratic form QW_λ (eq 1.1).
- §2.3 prime sensitivity (positivity restored by adding -W_p, p=2).
- §2.5 numerical: λ²=11, smallest positive eigenvalue 2.389×10^-48.
- Wall #1 paper-direct deeper.
- Lemma 1 6단계 paper-direct check (Connes-Consani 2021).
- Lemma 3 10th evidence.
- Specialist Δ.
