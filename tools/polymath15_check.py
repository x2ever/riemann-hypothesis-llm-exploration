"""Polymath15 §4-6 numerical verification.

C_0(p), ε̃(σ+iT), Boyd effective Stirling 의 numerical checks.
"""

from __future__ import annotations

import math

import mpmath as mp


def C_0(p: mp.mpf) -> mp.mpc:
    """Polymath15 eq (53): C_0(p)."""
    pi = mp.pi
    num = mp.exp(1j * pi * (p**2 / 2 + 3 / 8)) - 1j * mp.sqrt(2) * mp.cos(pi * p / 2)
    den = 2 * mp.cos(pi * p)
    return num / den


def C_0_at_singularity(sign: int) -> mp.mpc:
    """C_0 at p = ±1/2 (l'Hopital). sign = +1 (p=+1/2) or -1 (p=-1/2)."""
    eps = mp.mpf("1e-30")
    return C_0(sign * mp.mpf("0.5") + eps)


def epsilon_tilde(sigma: float, T: float, t: float) -> float:
    """Polymath15 eq (59) of Proposition 6.3: error term R_{t,N}."""
    T_prime = T + math.pi * t / 8
    a = math.sqrt(T_prime / (2 * math.pi))
    return (0.397 * 9**sigma / (a - 0.865) + 5 / (3 * (T - 6))) * math.exp(
        3.49 / (T - 4)
    )


def boyd_stirling_R2_bound(z: complex) -> float:
    """Boyd effective Stirling remainder bound for R_2(z)."""
    z_abs = abs(z)
    C2 = 0.5 * (1 + math.pi**2 / 6)
    if z.real >= 0:
        return (2 * math.sqrt(2) + 1) * C2 * math.gamma(2) / ((2 * math.pi) ** 3 * z_abs**2)
    return (
        (2 * math.sqrt(2) + 1)
        * C2
        * math.gamma(2)
        / ((2 * math.pi) ** 3 * z_abs**2 * abs(1 - math.exp(2j * math.pi * z)))
    )


def main() -> None:
    """Polymath15 §4-6 numerical checks."""
    mp.mp.dps = 30

    print("=== Polymath15 §4-6 numerical verification ===\n")

    print("--- C_0(p) numerical (eq 53) ---")
    print("Bound: |C_0(p)| ≤ 1/2 for p ∈ [-1, 1]")
    for p_val in [-1, -0.8, -0.5 + 1e-10, -0.3, 0, 0.3, 0.5 - 1e-10, 0.8, 1]:
        c0 = C_0(mp.mpf(str(p_val)) if p_val != 0 else mp.mpf(0))
        print(f"  C_0({p_val:+.3f}) = {complex(c0):.6f}, |C_0| = {float(abs(c0)):.6f}")

    print("\n--- ε̃(σ+iT) error bound (Proposition 6.3) ---")
    print("σ=0.5, t=0.1:")
    for T in [10, 30, 100, 1000, 10000]:
        eps = epsilon_tilde(0.5, T, 0.1)
        a = math.sqrt((T + math.pi * 0.1 / 8) / (2 * math.pi))
        print(f"  T={T:6d}, a={a:8.3f}, ε̃ = {eps:.6e}")

    print("\nσ=0, σ=0.5, σ=1 at T=1000, t=0.1:")
    for sigma in [0.0, 0.5, 1.0]:
        eps = epsilon_tilde(sigma, 1000, 0.1)
        print(f"  σ={sigma}, ε̃ = {eps:.6e}")

    print("\n--- α_n imag bound (eq 46) ---")
    print("Im α_n ≥ -1/(2T) - 1/T = -1.5/T. T=10: -0.15. T=100: -0.015.")
    for T in [10, 30, 100, 1000]:
        bound = -1.5 / T
        print(f"  T={T:5d}: -1.5/T = {bound:.5f}")

    print("\n--- Boyd effective Stirling R_2 bound ---")
    print("|R_2(z)| ≤ (2sqrt(2)+1) C_2 Γ(2) / (2π)^3 |z|^2.")
    C2 = 0.5 * (1 + math.pi**2 / 6)
    coef = (2 * math.sqrt(2) + 1) * C2 / (2 * math.pi) ** 3
    print(f"  C_2 = {C2:.6f}, prefactor = {coef:.6f}")
    print("  z = 10+0i: |R_2| ≤ {:.6e}".format(boyd_stirling_R2_bound(10 + 0j)))
    print("  z = 100+0i: |R_2| ≤ {:.6e}".format(boyd_stirling_R2_bound(100 + 0j)))

    print("\n--- Eq (47) integral identity ---")
    print("∫_R exp(tv²/(2(T-3.08))) (1/√π) e^{-v²} dv = (1 - t/(2(T-3.08)))^{-1/2}")
    for T_val in [10, 100, 1000]:
        t = 0.1
        coef = t / (2 * (T_val - 3.08))
        rhs = (1 - coef) ** (-0.5)
        print(f"  T={T_val}: rhs = {rhs:.6f}, vs exp(t/(4(T-3.33))) = {math.exp(t/(4*(T_val-3.33))):.6f}")


if __name__ == "__main__":
    main()
