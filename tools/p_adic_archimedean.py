"""p-adic vs archimedean local factors of ζ."""

from __future__ import annotations

import math

import mpmath as mp
import sympy


def main() -> None:
    mp.mp.dps = 30
    print("=== p-adic ↔ Archimedean Duality (NOVEL) ===\n")

    print("ζ_p(s) = (1 - p^{-s})^{-1} (Euler local factor).")
    print("ζ_∞(s) = π^{-s/2} Γ(s/2).")
    print("Completed: ζ̂(s) = ζ_∞(s) · Π_p ζ_p(s) = ζ_∞(s) ζ(s).")
    print("Functional eq: ζ̂(s) = ζ̂(1-s).\n")

    primes = list(sympy.primerange(2, 1000))
    print(f"Use {len(primes)} primes. Truncated archimedean part.")

    for s_re, s_im in [(0.5, 14.13), (0.5, 21.02), (0.5, 7.0), (0.7, 14.13)]:
        s = mp.mpc(s_re, s_im)
        prod = mp.mpf(1)
        for p in primes:
            prod *= 1 / (1 - mp.mpf(p) ** (-s))
        zeta_inf = mp.pi ** (-s / 2) * mp.gamma(s / 2)
        completed = zeta_inf * prod
        completed_paper = zeta_inf * mp.zeta(s)
        ratio = completed / completed_paper if abs(completed_paper) > 1e-30 else 0
        print(f"\ns = {s_re}+{s_im}i:")
        print(f"  Π_p (1-p^{{-s}})^{{-1}} (truncated): {complex(prod):.6f}")
        print(f"  Completed truncated: {complex(completed):.6f}")
        print(f"  Completed exact (zeta_inf · zeta): {complex(completed_paper):.6f}")
        print(f"  Ratio truncated/exact: {complex(ratio):.6f}")

    print("\n--- Functional eq check on critical line ---")
    print("ζ̂(s) = ζ̂(1-s). At s = 0.5+iτ, this is automatic (s = 1-s̄ symmetry).")
    for tau in [14.13, 21.02, 7.0]:
        s = mp.mpc(0.5, tau)
        s_dual = mp.mpc(0.5, -tau)
        zhat_s = mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
        zhat_dual = mp.pi ** (-s_dual / 2) * mp.gamma(s_dual / 2) * mp.zeta(s_dual)
        print(f"  τ={tau}: ζ̂(1/2+iτ) = {complex(zhat_s):.6e}")
        print(f"          ζ̂(1/2-iτ) = {complex(zhat_dual):.6e}  (conjugate {complex(zhat_s.conjugate()):.6e})")

    print("\nObservation: paper §VI Connes 1999 Σ_v ∫ h(u^-1)/|1-u| du = sum over all places.")
    print("Truncated Euler product captures *finite primes only*. archimedean missing.")
    print("→ p-adic ↔ archimedean duality 는 paper-direct *Tate's thesis* — 우리 partial 만.")


if __name__ == "__main__":
    main()
