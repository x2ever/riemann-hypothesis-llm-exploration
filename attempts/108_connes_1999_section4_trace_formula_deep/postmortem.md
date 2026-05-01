# Postmortem — Attempt 108 (Mode A deep, 8 components)

Connes 1999 §VI/§VII deep:
- §VI eq (15) Trace U(h) = Σ_v ∫ h(u^-1)/|1-u| d*u (master).
- §VI eq (16) ĥ(0)+ĥ(1) - Σ ĥ(χ,ρ) + ∞h(1) (Weil distribution form).
- §VI eq (17) h ≥ 0 ⟹ RHS positive ⟺ RH for all Grössencharakters.
- §VII Theorem 4 S-local rigorous: Trace(R_Λ U(h)) = 2h(1) log'Λ + Σ_v ∫' h(u^-1)/|1-u| d*u + o(1).

## Numerical limitation
Gaussian test function 의 too-fast decay → 단순 form 으로 검증 X.
paper §VI eq (16) full Weil distribution = bandlimited test 또는 Hermite + more zeros 필요.

## Wall mapping
- #1 paper-direct origin: 형식 vs rigorous trace, δ-cutoff, Frobenius analogue absence.
- #5 cross-link: not quantization but L² (paper §VI 끝).
- #6 partial 해소: S-local rigorous via §VII Theorem 4.

## Lemma 3 9th paper-direct evidence: Connes 1999 §VI eq (17).

## Specialist Δ (Connes 본인 추정)
- 알려진 paper paraphrase. 새 content X.
- 다음 가치 있는 질문: arithmetic site cohomology + L²(X) spectral 융합 (Connes-Consani 후속).
- 추정 자체 한계 명시.

## Honest scope
*novel content 0/10*. paper §VI/§VII paper-direct re-paraphrase + 우리 도구의 numerical limitation 명시.

## HARNESS
- ledger 108 (Type A, Mode A deep 8 components).
