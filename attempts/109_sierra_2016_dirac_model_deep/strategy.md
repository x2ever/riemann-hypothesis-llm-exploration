# Attempt 109: Sierra 2016 §I-V xp Model + Self-adjoint Extension DEEP
**Type**: A (Mode A deep, 8 components)

## Cut self-check (`lemmas/dont_try_directions.md`)
- Cut 5 (모든 spectral 후보 = circular):
  - Sierra 2016 §III/§V 가 *spectral candidate* (xp Hamiltonian + self-adjoint extension).
  - paper §I 끝: "fine tune a parameter to *see* each individual zero. In our approach we are not able to find a single Hamiltonian encompassing all the *zeros* at once."
  - 즉 Sierra paper 자체가 *Wall #5 의 single H 부재* paper-direct origin 명시.
  - 본 deep read = *paper-direct mapping 만* (그 origin 의 paper-direct 검증). cut X.

## DoD
- §II classical xp (BKC): n(E) = (E/2π)(log E/(ℓ_x ℓ_p) - 1) + 7/8 + Connes 변형.
- §III quantum xp Ĥ = √x p̂ √x: ψ_E(x) = x^{-1/2 + iE/ℏ}, *continuous* spectrum.
- §III eq (3.7): Σ ψ_E(nx) = (x^{-1/2 + iE/ℏ}/√(2πℏ)) ζ(1/2 - iE/ℏ) — zeros at ζ zero.
- §V H_I = x(p + ℓ_p²/p) self-adjoint extension via boundary condition ϑ.
- §V eq (5.14): e^{iϑ} K_{1/2 - iE/2}(ℓ_x ℓ_p) - K_{1/2 + iE/2}(ℓ_x ℓ_p) = 0 — eigenvalue condition.
- Wall #5 paper-direct deeper.
- Lemma 1 (spectral_candidate_circularity_check) 6단계 paper-direct cross-check.
- Specialist Δ 추정 (Connes / Sierra 본인).
