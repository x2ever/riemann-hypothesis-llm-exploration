# Work — Attempt 146 (Lemma 1 Axiom 7 — Normalizability/Self-adjoint Real Spectrum)

## Cut self-check
Cut 5 (모든 spectral 후보 = circular): Lemma 1 axiom 강화. cut X.

## Lemma 1 6단계 (attempts 010, 029, 109, 110, 111, 120, 133)

기존 6 axioms:
1. spectrum = ζ zeros exact.
2. Hamiltonian def w/ ζ.
3. self-adjoint 입증.
4. Frobenius gap trace formula.
5. single H prime visibility.
6. number field Lefschetz analogue.

attempt 120 axiom 7 후보: *spectrum eigenvalues all real*.

본 attempt = axiom 7 의 paper-direct verification + 추가 axiom 8 후보.

## Axiom 7 (attempt 120) — *spectrum eigenvalues all real*

paper-direct check:

| Candidate | (7) eigenvalues all real |
|---|---|
| BBM 2017 | E_n = -2γ_n (RH 가정 yes, RH false 시 complex pairs) |
| Sierra §III/§V | continuous spectrum (real if self-adjoint) |
| Sierra 2007 H_2 | real (deficiency indices (1,1)) |
| Connes-Consani 2021 | real (Dirac D_0 real eigenvalues, perturbation 보존) |
| Connes 1999 §VI | distribution support real (paper §VI eq 16 zeros real if RH) |
| Lagarias §8 (1) hypothetical | **NO** (λ = s²-1/4 = -γ²+iγ complex) |

→ paper-direct: **Lagarias §8 (1) fail axiom 7**. *self-acknowledged hypothetical*.

## Axiom 8 NEW — *Eigenstates normalizable* (paper-direct, BBM §III quote)

paper-direct (BBM 2017 §III, attempt 110):
> "the connection of this Hamiltonian to physical systems is at best tenuous because the eigenstates of Ĥ in our inner-product space are *not normalizable*."

→ paper-direct *new axiom 8*: *eigenstates normalizable* (in associated Hilbert space).

| Candidate | (8) eigenstates normalizable |
|---|---|
| BBM 2017 | **NO** (paper-direct §III quote) |
| Sierra §III xp | NO (continuous spectrum, plane wave-like) |
| Sierra §V H_I | YES (boundary condition self-adjoint extension) |
| Sierra 2007 H_2 | partial (Jost function asymptotic) |
| Connes-Consani 2021 | YES (finite rank perturbation of D_0 on circle, finite dim subspace) |
| Connes 1999 §VI | (cutoff trace formula, distribution sense) |
| Lagarias §8 (1) hypothetical | undefined |

→ paper-direct: BBM 2017 *fails axiom 8 self-acknowledged*. Connes-Consani 2021 *passes*.

## Axiom 9 NEW — *Domain of Hamiltonian explicit* (paper-direct, BBM §III quote)

paper-direct (BBM 2017 §III, attempt 110):
> "Identifying the *domain* of Ĥ remains a difficult and open problem."

→ paper-direct *new axiom 9*: *domain explicitly identified*.

| Candidate | (9) domain explicit |
|---|---|
| BBM 2017 | **NO** (paper-direct §III quote) |
| Sierra §III xp | YES (L²(0, ∞) essentially self-adjoint) |
| Sierra §V H_I | YES (boundary condition (5.10) defines domain) |
| Sierra 2007 H_2 | YES (von Neumann (1, 1) extension) |
| Connes-Consani 2021 | YES (finite rank L²(ℝ_+*/μ^ℤ)) |
| Connes 1999 §VI | partial (cutoff R_Λ Hilbert space defined) |

→ paper-direct: *axiom 9 fail* = BBM 2017 의 self-acknowledged limitation.

## Lemma 1 *9-axiom 표 update*

| Candidate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| BBM 2017 | YES | YES | NO | NO | P | NO | YES (RH) | **NO** | **NO** |
| Sierra §III xp | NO | NO | YES | NO | NO | NO | YES | NO | YES |
| Sierra §V H_I | NO | NO | YES (ϑ) | NO | NO | NO | YES | YES | YES |
| Sierra 2007 H_2 | NO | P | YES | NO | NO | NO | YES | P | YES |
| Connes-Consani 2021 | NO | NO | YES | P | P | P | YES | YES | YES |
| Connes 1999 §VI | (n/a) | (cutoff) | (formal) | YES | YES | distrib | distrib | (cutoff) | P |
| Lagarias §8 (1) hypothetical | YES | YES | issue | NO | NO | NO | **NO** | undef | undef |

→ paper-direct: **Connes-Consani 2021 passes most axioms** (1 NO, 2 NO, 3-6, 7-9 YES/PARTIAL). *least circular + best rigor*.

## Lemma 적용

### Lemma 1 update — 9 axioms
기존 6 axioms + Axiom 7 (attempt 120) + 2 new (8, 9).
- Axiom 8: eigenstates normalizable (BBM paper-direct 강한 fail).
- Axiom 9: domain explicit (BBM paper-direct 강한 fail).

### Lemma 7 Anchoring 강화
- BBM §III 3 quotes anchor (eigenvalues real X / normalizable X / domain unclear).
- → BBM 2017 *self-acknowledged 3-axiom fail*.

## Honest scope
*novel content X*. Lemma 1 9-axiom 강화. paper-direct *9 candidates 비교*.
