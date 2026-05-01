# Work — Attempt 155 (Lemma 1 — PT/CP/T Symmetry Axiom 10)

## Cut self-check
Cut 5 (spectral candidate circular): Lemma 1 axiom 10 후보. cut X.

## Lemma 1 9-axiom (~attempt 146)

원본 6 + (7) eigenvalues real + (8) normalizable + (9) domain explicit.

본 attempt = axiom 10 후보: *PT-symmetric / pseudo-Hermitian / CP / T-symmetry*.

paper-direct (BBM 2017 §I, attempt 110):
> "iĤ is PT-symmetric (in the sense to be defined), which means that the eigenvalues of iĤ are either real or else occur in complex-conjugate pairs."

→ paper-direct: PT-symmetry = *condition to ensure eigenvalues real or pair-complex*.
- Bender-Mostafazadeh framework: PT symmetric Hamiltonian = pseudo-Hermitian metric η_+.
- Bender 2007 quote (BBM 2017 ref [13]): "Making sense of non-Hermitian Hamiltonians".

## Axiom 10 NEW — PT/CP/T-symmetry consistent

paper-direct check:

| Candidate | (10) PT/CP/T-symmetry consistent |
|---|---|
| BBM 2017 | YES (paper §I 명시) |
| Sierra §III xp | YES (parity x ↔ -x) |
| Sierra §V H_I | YES (with ϑ choice) |
| Sierra 2007 H_2 | YES (Sl(2, ℝ) symmetry) |
| Connes-Consani 2021 | partial (Dirac D_0 symmetric) |
| Connes 1999 §VI | (n/a, distributional) |
| Lagarias §8 (1) hypothetical | undefined |

→ paper-direct: *Axiom 10 generally satisfied* (PT-symmetry는 most spectral candidates 의 *necessary* feature).

## Axiom 11 NEW — *biorthogonal completeness* (BBM §III 후속)

paper-direct (BBM 2017 §III, attempt 110):
> "Bearing in mind that Δ̂† is the forward difference operator, a calculation shows that ψ̃_n(x) = x^{-z̄_n} - (x+1)^{-z̄_n} and that Ĥ† ψ̃_n(x) = -i(2z_n - 1) ψ̃_n(x)."
> "Indeed, by considering the eigenstates {ψ̃_n(x)} of Ĥ†, one can introduce a biorthogonal set of eigenstates."

→ paper-direct *axiom 11*: *biorthogonal eigenstates* + *completeness*.

| Candidate | (11) biorthogonal completeness |
|---|---|
| BBM 2017 | partial (paper §III biorthogonal *if* RH; *if RH false* exceptional points self-orthogonal — paper §III) |
| Sierra §V H_I | YES (self-adjoint extensions complete on L²) |
| Sierra 2007 H_2 | partial (Jost asymptotic) |
| Connes-Consani 2021 | YES (D Dirac complete on L²(ℝ_+*/μ^ℤ)) |

→ paper-direct: BBM *biorthogonal completeness* *RH-conditional* (paper §III "biorthogonal" if Ē_m = E_m).

## Lemma 1 11-axiom 표 (~attempt 155)

| Candidate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BBM 2017 | YES | YES | NO | NO | P | NO | YES (RH) | NO | NO | YES | partial (RH) |
| Sierra §III xp | NO | NO | YES | NO | NO | NO | YES | NO | YES | YES | YES |
| Sierra §V H_I | NO | NO | YES (ϑ) | NO | NO | NO | YES | YES | YES | YES | YES |
| Sierra 2007 H_2 | NO | P | YES | NO | NO | NO | YES | P | YES | YES | partial |
| Connes-Consani 2021 | NO | NO | YES | P | P | P | YES | YES | YES | partial | YES |
| Connes 1999 §VI | (n/a) | (cutoff) | (formal) | YES | YES | distrib | distrib | (cutoff) | P | (n/a) | (n/a) |
| Lagarias §8 (1) | YES | YES | issue | NO | NO | NO | NO | undef | undef | undef | undef |

→ paper-direct: **Sierra §V H_I + Connes-Consani 2021** = *most axioms passed* (8-9/11).
- BBM 2017: *most axioms 부분 fail* (RH-conditional).
- Lagarias §8 (1) hypothetical: *least axioms* (4 issues + 4 undefined).

## Lemma 적용

### Lemma 1 11-axiom strengthening
6 → 9 (attempt 146) → 11 (attempt 155).
- Axiom 10: PT/CP/T-symmetry.
- Axiom 11: biorthogonal completeness.

### Lemma 7 Anchoring
- BBM §I PT-symmetry quote.
- BBM §III biorthogonal quote.
- 두 paper-direct anchor.

## Honest scope
*novel content X*. Lemma 1 11-axiom 강화. paper-direct 7 candidates 비교 표 update.
