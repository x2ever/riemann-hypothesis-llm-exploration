"""Voros §3 secondary zeta Z(σ) ↔ Lagarias §4 τ_n Hurwitz isomorphism check."""

from __future__ import annotations

import mpmath as mp


def voros_Z(sigma: float, num_zeros: int = 100) -> mp.mpc:
    """Z(σ) = Σ_k 1/x_k^σ, x_k = 1/4 + γ_k²."""
    total = mp.mpc(0)
    for k in range(1, num_zeros + 1):
        gamma = mp.zetazero(k).imag
        x_k = mp.mpf("0.25") + gamma**2
        total += 1 / x_k**sigma
    return total


def lagarias_tau(n: int) -> mp.mpf:
    """τ_n(π_triv) = (-1/2)^{n+1} ζ(n+1, 1/2)."""
    return (mp.mpf("-0.5")) ** (n + 1) * mp.zeta(n + 1, mp.mpf("0.5"))


def main() -> None:
    mp.mp.dps = 30
    print("=== Voros Z(σ) ↔ Lagarias τ_n Tissue (NUMERICAL) ===\n")

    print("Voros: x_k = 1/4 + γ_k². Z(σ) = Σ x_k^{-σ} (nontrivial zeros).")
    print("Lagarias: τ_n = (-1/2)^{n+1} ζ(n+1, 1/2). Hurwitz half-integer (trivial side).")
    print("Tissue 3 (attempt 137): nontrivial zero power sum vs trivial zero archimedean.\n")

    print(f"{'σ / n':<10}{'Voros Z(σ)':<25}{'Lagarias τ_n':<25}{'Z(σ) at σ=n+1?':<20}")
    for n in [1, 2, 3, 4, 5, 6, 8, 10]:
        Z_val = voros_Z(n + 1, num_zeros=100)
        tau_val = lagarias_tau(n)
        print(f"σ=n+1={n+1:<5}{str(complex(Z_val)):<25}{float(tau_val):<25.10f}{str(complex(Z_val)):<20}")

    print("\n--- Voros Z(σ) → Lagarias τ_n correspondence test ---")
    print("Hypothesis: Z(σ) at σ=n+1 might relate to τ_n via Hadamard product expansion.")
    print("Z(σ) = Σ_k (1/4 + γ_k²)^{-σ}. τ_n via trivial zeros = different power sum.")

    print("\nVoros 의 Z(σ) 첫 zero contributions (γ_1=14.13, x_1≈200):")
    gamma_1 = mp.zetazero(1).imag
    x_1 = mp.mpf("0.25") + gamma_1**2
    print(f"x_1 = {float(x_1):.4f}")
    for sigma in [1, 2, 3, 5]:
        single = 1 / x_1**sigma
        full = voros_Z(sigma, num_zeros=100)
        ratio = single / full
        print(f"  σ={sigma}: x_1^(-σ) = {float(single):.6e}, Z(σ) = {float(full.real):.6e}, ratio = {float(ratio.real):.4f}")

    print("\nObservation: σ=1 dominated by tail (nontrivial zeros 다수 contribute).")
    print("σ=large: x_1 dominates (Voros saddle point limit).")
    print("→ Voros Z = nontrivial zeros power sum.")
    print("→ Lagarias τ = trivial zeros archimedean Hurwitz sum.")
    print("→ paper-direct: 두 form 의 *zero classes* 가 다름 — Tissue 3 **complementary**.\n")

    print("--- λ_n decomposition (paper-direct, attempt 105 + 137) ---")
    print("Lagarias §4: λ_n = S_∞ - S_f + δ.")
    print("S_∞ = Σ binomial τ_{j-1} = trivial side Hurwitz sum (Lagarias).")
    print("S_f = primes side (Lagarias §6).")
    print("Voros Z = secondary zeta of nontrivial zeros (different decomposition).")
    print("→ Voros vs Lagarias = *different decomposition coordinates* of same ξ.")


if __name__ == "__main__":
    main()
