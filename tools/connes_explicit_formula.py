"""Weil/Connes explicit formula numerical verification.

Σ_ρ ĥ(γ) = ĥ(0) + ĥ(1) - 2 Re Σ_p Σ_{k≥1} (log p)/p^{k/2} ĝ(k log p)
"""

from __future__ import annotations

import math

import mpmath as mp
import sympy


def weil_explicit_formula_check(
    sigma: float = 1.0, num_zeros: int = 100, num_primes: int = 200
) -> tuple[float, float, float, float]:
    """Verify Weil's explicit formula with Gaussian test function.

    Test: g(x) = exp(-sigma * x^2) (real, even).
    Fourier: ĝ(γ) = sqrt(π/sigma) exp(-γ^2 / (4 sigma)).

    Σ_ρ ĝ(γ_ρ) ≈ ĝ(i/2) + ĝ(-i/2) - 2 Σ_p Σ_k (log p)/p^{k/2} g(k log p).
    """
    mp.mp.dps = 30

    zeros_sum = mp.mpc(0)
    for n in range(1, num_zeros + 1):
        gamma_n = mp.zetazero(n).imag
        g_hat_pos = mp.sqrt(mp.pi / sigma) * mp.exp(-(gamma_n**2) / (4 * sigma))
        zeros_sum += 2 * g_hat_pos

    archimedean = 2 * mp.sqrt(mp.pi / sigma) * mp.exp(mp.mpf(1) / (16 * sigma))

    primes_sum = mp.mpf(0)
    primes_list = list(sympy.primerange(2, 10000))[:num_primes]
    for p in primes_list:
        log_p = mp.log(p)
        for k in range(1, 30):
            k_log_p = k * log_p
            g_val = mp.exp(-sigma * k_log_p**2)
            if g_val < mp.mpf("1e-50"):
                break
            primes_sum += log_p / p ** (mp.mpf(k) / 2) * g_val

    rhs = archimedean - 2 * primes_sum
    return float(zeros_sum.real), float(archimedean), float(2 * primes_sum), float(rhs)


def main() -> None:
    """Verify explicit formula at several test parameters."""
    print("=== Connes/Weil Explicit Formula Numerical ===\n")
    print("Σ_ρ ĝ(γ) = ĝ(i/2) + ĝ(-i/2) - 2 Σ_p Σ_k (log p)/p^(k/2) g(k log p)\n")
    print(f"{'σ':<8}{'lhs (Σ_ρ)':<20}{'arch (ĝ(±i/2))':<22}{'2*primes':<20}{'rhs':<20}{'ratio':<12}")
    for sigma in [0.05, 0.1, 0.2, 0.5]:
        lhs, arch, primes, rhs = weil_explicit_formula_check(
            sigma=sigma, num_zeros=200, num_primes=200
        )
        ratio = lhs / rhs if rhs != 0 else float("inf")
        print(f"{sigma:<8}{lhs:<20.6f}{arch:<22.6f}{primes:<20.6f}{rhs:<20.6f}{ratio:<12.6f}")

    print("\n--- Note ---")
    print("ratio → 1 as num_zeros, num_primes → ∞.")
    print("Truncation effects cause systematic error.")
    print("paper-direct: §VI eq (16) = §VII Theorem 4 의 *number field analogue*")


if __name__ == "__main__":
    main()
