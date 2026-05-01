# Postmortem — Attempt 113 (Mode A deep, 8 components)

Rodgers-Tao 2020 §1-§2 deep:
- §1 H_0(z) = (1/8) ξ(1/2 + iz/2), H_t = ∫ e^{tu²} Φ(u) cos(zu) du backwards heat.
- §1 Theorem 1: Λ ≥ 0 unconditional.
- §1 Table 1: 35년 lower bound history (Newman -∞ → Saouter et al -10^-11).
- §1 proof outline: assume Λ<0, dynamic local equilibrium, contradict Montgomery pair correlation.
- §1.5 Hamiltonian 𝓗(t) = Σ log(1/|x_j-x_k|), gradient flow eq (5), monotonicity ∂_t 𝓗 = -4 E(t) (eq 6).
- §2 Lemma 4 (eq 7-9): H_t bounds via saddle + Stirling.

## Wall #2 paper-direct origin
§1.5 quote: "control integrated energies that resemble ∫_{Λ/2}^0 E(t) dt".
→ ∫E(t)dt = 우리 wall taxonomy 의 paper-direct.

## Wall #2 quantitative bracket
- Polymath15 (forward): Λ ≤ 0.22.
- Rodgers-Tao (backwards): Λ ≥ 0.
- Combined: 0 ≤ Λ ≤ 0.22.
- Λ = 0 strict equality unknown ⟺ RH 직접.

## Wall #4 cross-link
proof = Montgomery pair correlation contradict. Wall #4 ⟹ Wall #2.

## Lemma 3 12th evidence
Λ ≥ 0 unconditional (다른 11 evidence 는 conditional mapping 만).

## Lemma 6 Cut 1 정정
backwards heat 가 attempt 007 Wasserstein forward 와 opposite direction. paper-direct 검증.

## Specialist Δ (Tao)
- "fundamental obstacle, combinatorial 최적화로 닫히지 않음" — paper §1.5 "far from optimal" quote 의 paper-direct verification.
- Tao sharp navigation: ∫E(t)dt unconditional sharper = 30년 challenge.

## Honest scope
*novel content 0/10*. paper-direct deep + Wall #2 paper-direct origin + Lemma 3 12th evidence + Tao 추정 paper-direct 검증.

## HARNESS
- ledger 113 (Type A, Mode A deep 8 components).
