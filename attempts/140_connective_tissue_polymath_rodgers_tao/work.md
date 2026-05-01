# Work — Attempt 140 (Tissue 5: Polymath15 H_t ↔ Rodgers-Tao zero dynamics)

## Cut self-check
Cut 6: paper-direct tissue. cut X.

## Tissue 5 paper-direct (attempt 137)
**Polymath15** (attempt 106): H_t = ∫_0^∞ e^{tu²} Φ(u) cos(zu) du.
- Forward heat: ∂_t H_t = -∂_zz H_t (paper §1).
- 결과 (Polymath15): Λ ≤ 0.22.
- 결과 (Platt-Trudgian 2021 sharper, attempt 132): Λ ≤ 0.2.

**Rodgers-Tao 2020** (attempt 113): ∂_t x_k = 2 Σ_{j≠k} 1/(x_k - x_j).
- Backward heat zero dynamics (assume Λ < 0).
- Hamiltonian 𝓗(t) = Σ log(1/|x_j - x_k|).
- Monotonicity ∂_t 𝓗 = -4 E(t).
- 결과: Λ ≥ 0.

## Tissue 5 isomorphism (paper-direct)
*동일 ξ-function*, *두 시간 방향* analysis:
- Forward (Polymath15): Λ ≤ 0.22 → 0.2 (Platt-Trudgian).
- Backward (Rodgers-Tao): Λ ≥ 0.
- **Combined**: 0 ≤ Λ ≤ 0.2.

paper-direct *complementary forms*:
- Polymath15 H_t = ξ-function 의 explicit Fourier representation (Φ super-exp decay).
- Rodgers-Tao = ξ-zeros 의 dynamical system (zeros = particles, Coulomb-like 1/(x_j-x_k) repulsion).

## Mathematical isomorphism (paper-direct)
**Time-reversal of heat equation**:
- Forward heat ∂_t = -∂_zz: zeros 가 stable equilibrium 향함 (paper Polymath15).
- Backward heat ∂_t = +∂_zz: zeros 가 *expand* (paper Rodgers-Tao).
- Backward 의 stable point = *Λ = 0* (Newman conjecture).

paper-direct: 동일 *ξ-function* 의 *2 time directions* 의 *quantitative complementary*.

## Specialist Δ Anchoring (Lemma 7)
- Polymath15 §1 quote: "H_t의 forward heat flow Newman 1976 Λ definition".
- Rodgers-Tao §1.5 quote (attempt 113): "control integrated energies that resemble ∫_{Λ/2}^0 E(t) dt".
- 둘 다 paper §끝 anchored.

## Honest scope
*novel content X*. Tissue 5 paper-direct confirmation. Combined Λ bracket 0 ≤ Λ ≤ 0.2.
