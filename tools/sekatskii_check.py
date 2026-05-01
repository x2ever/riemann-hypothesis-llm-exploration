"""Sekatskii generalized Bombieri-Lagarias numerical verification.

|ρ - a| / |ρ + a - 1| = 1 ⟺ ρ on critical line, independent of a.
k_{n,a} = Σ_ρ (1 - ((ρ-a)/(ρ+a-1))^n) ≥ 0 ⟺ RH.
"""

from __future__ import annotations

import mpmath as mp


def main() -> None:
    """Verify Sekatskii generalization on first ζ zeros."""
    mp.mp.dps = 30

    print("=== Sekatskii Generalized Bombieri-Lagarias ===\n")

    print("--- |ρ-a|/|ρ+a-1| = 1 verification at first 5 zeros ---")
    print("paper-direct: independent of a (ρ on critical line).")
    print(f"{'n':<5}{'γ':<20}{'a=0':<20}{'a=0.3':<20}{'a=2':<20}{'a=-1.5':<20}")
    for n in range(1, 6):
        rho = mp.mpc(mp.mpf("0.5"), mp.zetazero(n).imag)
        for a_val in [0, 0.3, 2, -1.5]:
            a = mp.mpf(str(a_val))
            ratio = abs(rho - a) / abs(rho + a - 1)
            print(f"{a_val:>5}: {float(ratio):<10.6f}", end="  ")
        print()

    print("\n--- k_{n, a} = Σ_ρ Re(1 - ((ρ-a)/(ρ+a-1))^n) for first 30 zeros ---")
    print("paper Theorem 1: RH ⟺ k_{n,a} ≥ 0 for any real a ≠ 1/2.")
    print(f"{'n':<5}", end="")
    for a_val in [0, 0.3, 2, -1.5]:
        print(f"{'a=' + str(a_val):<20}", end="")
    print()

    for n in [1, 2, 3, 5, 10, 15]:
        print(f"{n:<5}", end="")
        for a_val in [0, 0.3, 2, -1.5]:
            a = mp.mpf(str(a_val))
            k_n_a = mp.mpf(0)
            for j in range(1, 31):
                rho = mp.mpc(mp.mpf("0.5"), mp.zetazero(j).imag)
                term = 1 - ((rho - a) / (rho + a - 1)) ** n
                k_n_a += term.real
                rho_bar = mp.mpc(mp.mpf("0.5"), -mp.zetazero(j).imag)
                term_bar = 1 - ((rho_bar - a) / (rho_bar + a - 1)) ** n
                k_n_a += term_bar.real
            print(f"{float(k_n_a):<20.6f}", end="")
        print()


if __name__ == "__main__":
    main()
