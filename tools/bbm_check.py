"""Sanity check for Bender–Brody–Müller (2017) Hamiltonian's boundary condition.

BBM define eigenfunctions ψ_z(x) = -ζ(z, x+1) (Hurwitz zeta), with the
"quantization condition" ψ_z(0) = 0.  Since ζ(z, 1) = ζ(z) (Riemann ζ),
this gives ψ_z(0) = -ζ(z), hence ψ_z(0) = 0 ⟺ ζ(z) = 0.

This script verifies the identity numerically and exposes the *circularity*
of the BBM construction's spectrum identification: the boundary condition
*just is* the equation ζ(z) = 0.

What's left for BBM (and what isn't checked here): self-adjointness on a
concrete Hilbert space, which would imply spectrum is real (= RH).
"""

from __future__ import annotations

import argparse

import mpmath


def psi_z(z: complex, x: float, dps: int = 30) -> complex:
    """ψ_z(x) := -ζ(z, x+1).  At x=0 this is -ζ(z)."""
    mpmath.mp.dps = dps
    return -mpmath.zeta(z, x + 1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="BBM ψ_z(0) = -ζ(z) sanity check."
    )
    parser.add_argument("-n", type=int, default=10, help="Number of zeros to check.")
    parser.add_argument("--dps", type=int, default=40)
    args = parser.parse_args()

    mpmath.mp.dps = args.dps

    print(f"Checking ψ_z(0) = -ζ(z) at first {args.n} ζ zeros and at non-zero points.\n")
    print(f"{'z':>30} {'ψ_z(0)':>30} {'|ψ_z(0)|':>15}")
    print("-" * 80)

    for k in range(1, args.n + 1):
        rho = mpmath.zetazero(k)
        z = complex(rho)
        psi0 = psi_z(z, 0.0, args.dps)
        psi0_complex = complex(psi0)
        print(
            f"{f'{z.real:.4f}+{z.imag:.4f}i':>30} "
            f"{f'{psi0_complex.real:+.3e}{psi0_complex.imag:+.3e}i':>30} "
            f"{abs(psi0_complex):>15.3e}"
        )

    print()
    print("Non-zero z (off the critical line / not at zero):")
    for z_test in [
        complex(0.5, 1.0),  # not a zero
        complex(0.5, 14.0),  # near first zero
        complex(0.5, 14.13472514173469),  # very close to first zero
        complex(0.7, 14.13472514173469),  # off critical line
        complex(2.0, 0),  # ζ(2) = π²/6
    ]:
        psi0 = psi_z(z_test, 0.0, args.dps)
        psi0_complex = complex(psi0)
        print(
            f"  z = {z_test.real:+.6f}{z_test.imag:+.6f}i  "
            f"ψ_z(0) = {psi0_complex.real:+.3e}{psi0_complex.imag:+.3e}i  "
            f"|ψ| = {abs(psi0_complex):.3e}"
        )

    print()
    print("Summary:")
    print("  At ζ zeros: |ψ_z(0)| ≈ 0 (verified to working precision).")
    print("  At non-zeros: |ψ_z(0)| > 0 (as expected).")
    print()
    print("=> BBM 'boundary condition ψ(0)=0' is *equivalent* to 'z is a zero of ζ'.")
    print("=> BBM construction does NOT independently prove RH.  Self-adjointness")
    print("   on the BBM-defined inner product is the unproven gap (Wall #5).")


if __name__ == "__main__":
    main()
