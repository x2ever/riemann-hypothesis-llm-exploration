# Attempt 116: Lagarias §6 Bounds for S_f(n, π) — RH-Conditional DEEP
**Type**: A (Mode A deep, 8 components)

## Cut self-check (`lemmas/dont_try_directions.md`)
- Cut 6 (positivity 단독 RH): paper §6 가 *RH 가정 하 S_f bound*. mapping 만. cut X.

## DoD
- §6 Definition: incomplete Li coefficient λ_n(T, π) (eq 6.1).
- §6 Theorem 6.1: S_f(n, π) = λ_n(√n, π^∨) + O(√n log n). RH ⟹ λ_n(√n, π^∨) = O(√n log n).
- §6 Proof: kernel k_n(s) = (1+1/s)^n - 1, contour integral over C_1, deform to C_2(n).
- §6 Lemma 6.1: L'/L bound in critical strip.
- §6 4 contour segments: I_2^(I)/(II)/(III)/(IV) bounds.
- §6 RH part (eq 6.14): zero density Theorem 2.1(4).
- 결합 §5 + §6: λ_n ~ (N/2) n log n + C_1 n + O(√n log n) (RH 가정).
- Wall #6 *unconditional + conditional* combination paper-direct.
- Lemma 3 15th evidence (RH-conditional S_f bound).
- Specialist Δ.
