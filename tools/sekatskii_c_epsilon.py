"""Sekatskii §2 Theorem 2 (c) c(ε) empirical estimate.

paper §2 (c): Σ_ρ Re(1 - ((ρ-a)/(ρ-2σ+a))^n) ≥ -c(ε) e^{εn}.
Estimate empirical c via numerical k_{n, a, σ}.
"""

from __future__ import annotations

import math

import mpmath as mp


def k_n_a_sigma(n: int, a: float, sigma: float, num_zeros: int = 100) -> float:
    """Σ_ρ Re(1 - ((ρ-a)/(ρ-2σ+a))^n) over first num_zeros pairs."""
    mp.mp.dps = 30
    total = mp.mpf(0)
    a_mp = mp.mpf(str(a))
    sigma_mp = mp.mpf(str(sigma))
    for j in range(1, num_zeros + 1):
        gamma = mp.zetazero(j).imag
        for sign in [+1, -1]:
            rho = mp.mpc(mp.mpf("0.5"), sign * gamma)
            term = 1 - ((rho - a_mp) / (rho - 2 * sigma_mp + a_mp)) ** n
            total += term.real
    return float(total)


def main() -> None:
    """Empirical c(ε) estimate."""
    print("=== Sekatskii §2 (c) c(ε) Empirical Estimate ===\n")
    print("paper-direct: Σ Re(...) ≥ -c(ε) e^{εn}.")
    print("Empirical: c_emp(ε, n) = -Σ / e^{εn} (when Σ < 0).")
    print("If Σ > 0 always, c(ε) trivially satisfied — paper bound 무관.\n")

    a = 0.0
    sigma = 0.5
    print(f"a = {a}, σ = {sigma} (case σ = 1/2)")
    print(f"|ρ - a|/|ρ + a - 1| = 1 ⟺ on critical line.")
    print()

    print(f"{'n':<5}{'k_n':<20}{'sign':<8}", end="")
    for eps in [0.5, 0.2, 0.1, 0.05, 0.01]:
        print(f"e^{{{eps}n}}/k_n " if False else f"c(ε={eps}): ", end="")
    print()

    for n in [1, 5, 10, 20, 30, 50, 70, 100]:
        k_val = k_n_a_sigma(n, a, sigma, num_zeros=200)
        sign = "+" if k_val >= 0 else "-"
        print(f"{n:<5}{k_val:<20.6f}{sign:<8}", end="")
        for eps in [0.5, 0.2, 0.1, 0.05, 0.01]:
            if k_val < 0:
                c_emp = -k_val / math.exp(eps * n)
                print(f"{c_emp:<10.4e} ", end="")
            else:
                print(f"{'(positive)':<10} ", end="")
        print()

    print("\n--- Try a = 2, σ = 0.5 (Sekatskii family of a) ---\n")
    a = 2.0
    sigma = 0.5
    print(f"a = {a}, σ = {sigma}")
    print(f"{'n':<5}{'k_n':<20}{'sign':<8}", end="")
    for eps in [0.5, 0.2, 0.1, 0.05]:
        print(f"c(ε={eps}): ", end="")
    print()

    for n in [1, 5, 10, 20, 30, 50, 70, 100]:
        k_val = k_n_a_sigma(n, a, sigma, num_zeros=100)
        sign = "+" if k_val >= 0 else "-"
        print(f"{n:<5}{k_val:<20.6f}{sign:<8}", end="")
        for eps in [0.5, 0.2, 0.1, 0.05]:
            if k_val < 0:
                c_emp = -k_val / math.exp(eps * n)
                print(f"{c_emp:<10.4e} ", end="")
            else:
                print(f"{'(positive)':<10} ", end="")
        print()

    print("\n--- Counterfactual: σ = 0.4 (Sekatskii Theorem 2 case σ ≠ 1/2) ---")
    print("paper §2: a < σ ⟹ (a) Re ρ ≤ σ ⟺ (b) positivity.")
    print("If σ = 0.4 < 1/2 = Re ρ, condition (a) fails ⟹ (b) violated possibly.\n")
    a = 0.0
    sigma = 0.4
    print(f"a = {a}, σ = {sigma}")
    print(f"{'n':<5}{'k_n^σ':<20}{'sign':<8}c(0.1) c(0.05)")
    for n in [1, 5, 10, 20, 30, 50]:
        k_val = k_n_a_sigma(n, a, sigma, num_zeros=100)
        sign = "+" if k_val >= 0 else "-"
        print(f"{n:<5}{k_val:<20.6f}{sign:<8}", end="")
        for eps in [0.1, 0.05]:
            if k_val < 0:
                c_emp = -k_val / math.exp(eps * n)
                print(f"{c_emp:<10.4e} ", end="")
            else:
                print(f"{'(pos)':<10} ", end="")
        print()


if __name__ == "__main__":
    main()
