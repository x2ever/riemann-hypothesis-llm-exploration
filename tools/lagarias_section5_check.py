"""Lagarias §5 unconditional asymptotic for S_∞(n, π) numerical verification."""

from __future__ import annotations

import math

import mpmath as mp


def main() -> None:
    """Verify Lagarias §5 numerical constants + S_∞ asymptotic formula."""
    mp.mp.dps = 50

    print("=== Lagarias §5 Unconditional Asymptotic Verification ===\n")

    print("--- Constants (paper §5) ---")
    gamma = mp.euler
    print(f"γ (Euler) = {float(gamma):.10f}")

    C1_triv = (gamma - 1 - mp.log(2 * mp.pi)) / 2
    print(f"C_1(π_triv) = (1/2)(γ - 1 - log(2π)) = {float(C1_triv):.10f}")
    print("(paper §5 eq 5.4: -1.1303307)")

    beta_inf = mp.quad(lambda t: mp.exp(-t / 2) / t, [1, mp.inf])
    print(f"β_∞ = ∫_1^∞ e^(-t/2) dt/t = {float(beta_inf):.10f}")
    print("(paper §5 eq after 5.11: 0.559774)")

    alpha_inf = mp.quad(lambda t: (1 - mp.exp(-t / 2)) / t, [0, 1])
    print(f"α_∞ = ∫_0^1 (1 - e^(-t/2)) dt/t = {float(alpha_inf):.10f}")
    print("(paper §5 eq 5.21: 0.443842)")

    print("\n--- S_∞(n, π_triv) asymptotic numerical (eq 4.11) ---")
    print("S_∞(n, π_triv) = -Σ_{j=1}^n (-1)^{j+1} C(n,j) (1 - 1/2^j) ζ*(j)")
    print("ζ*(1) = log(4π) + γ, ζ*(j) = ζ(j) for j ≥ 2.")
    print(f"\n{'n':<8}{'S_∞(n)':<25}{'(1/2) n log n':<25}{'C_1 n':<25}{'sum':<25}{'rel err':<10}")

    zeta_star_1 = mp.log(4 * mp.pi) + gamma
    for n in [10, 20, 50, 100]:
        s_inf_paper = mp.mpf(0)
        for j in range(1, n + 1):
            sign = (-1) ** (j + 1)
            binom = mp.binomial(n, j)
            factor = 1 - mp.mpf(1) / (2**j)
            zeta_star_j = zeta_star_1 if j == 1 else mp.zeta(j)
            s_inf_paper -= sign * binom * factor * zeta_star_j

        leading = mp.mpf(n) * mp.log(n) / 2
        c1_term = C1_triv * n
        approx = leading + c1_term
        rel_err = abs(s_inf_paper - approx) / abs(s_inf_paper)
        print(f"{n:<8}{float(s_inf_paper):<25.6f}{float(leading):<25.6f}{float(c1_term):<25.6f}{float(approx):<25.6f}{float(rel_err):<10.4f}")

    print("\n--- T_20(n, 0) leading order (Lemma 5.1) ---")
    print("T_20(n, 0) = (1/2) n log n + ((-1/2)Γ'/Γ(1) + β_∞ + 1/√e - 1) n + O(1).")
    digamma_at_1 = -gamma  # ψ(1) = -γ
    coeff = -digamma_at_1 / 2 + beta_inf + 1 / mp.sqrt(mp.e) - 1
    print(f"Coefficient: -ψ(1)/2 + β_∞ + 1/√e - 1 = {float(coeff):.10f}")

    print("\n--- Wall #6 cancellation note ---")
    print("S_∞(n, π_triv) ~ (1/2) n log n + C_1 n  unconditional.")
    print("S_f(n, π_triv) ~ ??? (paper §6, RH-conditional). 본 attempt scope X.")
    print("λ_n = S_∞ - S_f + 1 의 cancellation = Wall #6 paper-direct.")


if __name__ == "__main__":
    main()
