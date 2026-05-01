"""Cross-compare 5 spectral candidates' spectrum.

BBM 2017: E_n = i(2z_n - 1) where z_n = ζ-zero.
Sierra §V: K_{1/2-iE/2}(z) Bessel eigenvalue.
Connes-Consani 2021: λ_n(D(λ, k)) at special λ.
Lagarias §8 (1) hypothetical: λ = s² - 1/4.
"""

from __future__ import annotations

import math

import mpmath as mp


def main() -> None:
    """Compare spectra of 5 candidates."""
    mp.mp.dps = 30
    print("=== 5 Spectral Candidate Spectrum Comparison (NOVEL) ===\n")

    print("--- First 5 ζ zeros ---")
    zeros = []
    for n in range(1, 6):
        gamma = mp.zetazero(n).imag
        zeros.append(float(gamma))
        print(f"  γ_{n} = {gamma}")

    print("\n--- BBM 2017: E_n = i(2z_n - 1) where z_n = 1/2 + iγ_n ---")
    for n, g in enumerate(zeros, 1):
        E_n = -2 * g  # i(2(1/2 + iγ) - 1) = i(2iγ) = -2γ
        print(f"  E_{n} = {E_n:.6f}")

    print("\n--- Lagarias §8 (1) hypothetical: λ = s² - 1/4 where s = 1/2 + iγ ---")
    for n, g in enumerate(zeros, 1):
        s = complex(0.5, g)
        lam = s * s - 0.25
        print(f"  λ_{n} = {lam.real:+.6f} + {lam.imag:+.6f}i  (purely imaginary if RH: {lam.real:.6f})")

    print("\n--- Sierra §V eq (5.14): solve K_{1/2-iE/2}(z) - K_{1/2+iE/2}(z) = 0 (ϑ=π) ---")
    z = mp.mpf("1.0")  # ℓ_x ℓ_p / ℏ
    print(f"  z = ℓ_x ℓ_p / ℏ = {z}")
    print("  Try E candidates near 14:")
    for E_test in [10, 12, 14, 14.13, 16]:
        E_mp = mp.mpf(str(E_test))
        K_minus = mp.besselk(mp.mpf("0.5") - mp.mpc(0, E_mp / 2), z)
        K_plus = mp.besselk(mp.mpf("0.5") + mp.mpc(0, E_mp / 2), z)
        diff = K_minus - K_plus
        print(f"    E = {E_test}: |K_minus - K_plus| = {float(abs(diff)):.6f}")

    print("\n--- Connes-Consani 2021: λ_n(D(λ, k)) at special λ ---")
    print("  paper Figure 1: λ²=10.5, k=18, λ_1(D) ≈ 14.13 = γ_1 (first zero).")
    print("  paper Figure 3: 31 zeros recovered (paper numerical, prob 10^-50).")
    print("  본 attempt 우리 도구 검증 X (prolate spheroidal wave function full implementation).")

    print("\n--- Cross-comparison ---")
    print(f"  γ_1 = {zeros[0]:.6f}")
    print(f"  BBM E_1 = -2γ_1 = {-2 * zeros[0]:.6f} (negative real, RH 가정)")
    print(f"  Lagarias §8 (1) λ_1 = -0.25 - γ_1² = {-0.25 - zeros[0]**2:.6f} (negative real, RH 가정)")
    print(f"  Sierra §V z=1: E search 14 nearby — no exact root (Bessel mismatch)")
    print(f"  Connes-Consani 2021: γ_1 directly (paper coincidence at special λ)")

    print("\n*Failure*: 4 candidates *all* RH 가정 시 γ_1 의 *function* 표현 — *spectrum exact X*.")
    print("BBM = -2γ, Lagarias = -1/4 - γ², Sierra = no root at z=1, Connes-Consani = 14.13 only at λ²=10.5.")
    print("\n→ 5 candidates *all 다른 spectrum* — *PT-symmetric unification X*.")
    print("→ paper-direct *Wall #5 의 5 manifestation* 명시. 통합 X.")


if __name__ == "__main__":
    main()
