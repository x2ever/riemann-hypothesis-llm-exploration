# Attempt 110: Bender-Brody-Müller 2017 Hamiltonian DEEP
**Type**: A (Mode A deep, 8 components)

## Cut self-check (`lemmas/dont_try_directions.md`)
- Cut 5 (모든 spectral 후보 = circular):
  - BBM Ĥψ_z(x) = i(2z-1)ψ_z(x), ψ_z(x) = -ζ(z, x+1).
  - Boundary condition ψ_z(0) = -ζ(z, 1) = -ζ(z) = 0 ⟺ z is ζ zero.
  - Lemma 1 Cut criterion (1, 2) 정확 yes — paper-direct circular by construction.
  - 본 deep read = *paper-direct mapping 만* (circular 의 paper-direct 검증). cut X.

## DoD
- §I introduction + Hamiltonian eq (1).
- §II Δ̂ 와 Δ̂^{-1} via Borel sum + Bernoulli numbers (eq 2-3).
- Eigenfunction ψ_z(x) = -ζ(z, x+1), eigenvalue i(2z-1) (eq 4).
- Boundary condition ψ_z(0) = 0 ⟺ -ζ(z) = 0.
- iĤ PT-symmetric (eq 5).
- Pseudo-Hermitian metric η̂ = sin² (p̂/2).
- Biorthogonality (eq 7) + self-orthogonality at non-RH zeros (Jordan blocks).
- Numerical: ζ(z, 1) = ζ(z) at first zeros, eigenvalue formula i(2z-1).
- Wall #5 paper-direct deeper.
- Lemma 1 6단계 paper-direct full check (BBM).
- Specialist Δ 추정.
