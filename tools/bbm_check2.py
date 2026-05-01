"""BBM 2017 paper §II/III numerical verification.

Hurwitz zeta ψ_z(x) = -ζ(z, x+1), eigenvalue i(2z-1), boundary condition ψ_z(0) = 0.
"""

from __future__ import annotations

import mpmath as mp


def main() -> None:
    """Check BBM eigenfunction & boundary condition at first 5 ζ zeros."""
    mp.mp.dps = 30

    print("=== BBM 2017 §II/III numerical verification ===\n")

    print("--- ψ_z(0) = -ζ(z, 1) = -ζ(z) check at first 5 ζ zeros ---")
    print(f"{'n':<5}{'γ_n':<25}{'z_n = 1/2 + iγ':<35}{'ψ_z(0) = -ζ(z,1)':<40}")
    for n in range(1, 6):
        rho = mp.zetazero(n)
        z_n = rho
        psi_at_0 = -mp.zeta(z_n, 1)
        print(f"{n:<5}{float(rho.imag):<25.10f}{str(z_n):<35}{str(complex(psi_at_0)):<40}")

    print("\n--- Eigenvalue E_n = i(2z_n - 1) at first 5 zeros ---")
    print(f"{'n':<5}{'γ_n':<25}{'E_n = i(2z_n-1)':<35}{'|Im E_n|':<20}")
    for n in range(1, 6):
        rho = mp.zetazero(n)
        z_n = rho
        E_n = 1j * (2 * z_n - 1)
        print(f"{n:<5}{float(rho.imag):<25.10f}{str(complex(E_n)):<35}{float(abs(E_n.imag)):<20.6e}")

    print("\nNote: E_n real ⟺ 2 Re(z_n) = 1 ⟺ Re(z_n) = 1/2 (RH).")
    print("BBM does NOT prove eigenvalues real — they assume RH or boundary condition.")

    print("\n--- ψ_z(x) = -ζ(z, x+1) growth at trivial zeros (z = -2n) ---")
    print(f"{'n':<5}{'z = -2n':<10}{'ψ_z(x=10)':<35}{'ψ_z(x=100)':<35}")
    for n in range(1, 4):
        z_triv = -2 * n
        psi_10 = -mp.zeta(z_triv, 11)
        psi_100 = -mp.zeta(z_triv, 101)
        print(f"{n:<5}{z_triv:<10}{float(psi_10):<35.6f}{float(psi_100):<35.6e}")

    print("\nTrivial zeros: ψ_z grows like x^{2n+1} — NOT in BBM Hilbert space.")
    print("Nontrivial zeros: ψ_z oscillates with subbornean growth.")

    print("\n--- η̂ = sin²(p̂/2) at first zeros (sketch) ---")
    print("PT-symmetric inner product ⟨φ,ψ⟩ = ⟨η̂φ|ψ⟩.")
    print("(η̂ acts in Fourier domain — exact ⟨ψ_m,ψ_n⟩ requires Mellin transform.)")
    print("paper §III biorthogonality: ⟨ψ̃_m|ψ_n⟩ = 0 for m≠n if all z_n satisfy RH.")
    print("Numerical 검증 = paper §III eq (6)-(7) Mellin integral, time cost large.\n")


if __name__ == "__main__":
    main()
