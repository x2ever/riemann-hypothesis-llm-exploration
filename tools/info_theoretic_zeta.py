"""ζ as partition function: free energy, entropy, heat capacity at various β."""

from __future__ import annotations

import mpmath as mp


def free_energy(beta: complex) -> complex:
    """F(β) = -log ζ(β)."""
    return -mp.log(mp.zeta(beta))


def entropy_real(beta_re: float, beta_im: float = 0.0, h: float = 1e-6) -> float:
    """S = -∂F/∂β_re (real part derivative)."""
    F_plus = free_energy(complex(beta_re + h, beta_im))
    F_minus = free_energy(complex(beta_re - h, beta_im))
    return float(((F_plus - F_minus) / (2 * h)).real)


def heat_capacity(beta_re: float, beta_im: float = 0.0, h: float = 1e-6) -> float:
    """C = -β² ∂²F/∂β² (Re)."""
    F0 = free_energy(complex(beta_re, beta_im))
    F_p = free_energy(complex(beta_re + h, beta_im))
    F_m = free_energy(complex(beta_re - h, beta_im))
    d2 = (F_p - 2 * F0 + F_m) / (h * h)
    return float(-(beta_re**2 * d2).real)


def main() -> None:
    mp.mp.dps = 30
    print("=== ζ as Partition Function (NOVEL) ===\n")
    print("F(β) = -log ζ(β), S = -∂F/∂β, C = -β² ∂²F/∂β².")
    print("Question: critical line β=1/2+iτ has special thermodynamic structure?\n")

    print(f"{'β':<25}{'F (Re)':<15}{'F (Im)':<15}{'S':<15}{'C':<15}")
    test_points = [
        (2.0, 0.0),
        (1.5, 0.0),
        (1.0, 0.0),  # pole
        (0.7, 0.0),
        (0.5, 0.0),  # critical line, real
        (0.5, 14.13),  # at first zero
        (0.5, 21.02),
        (0.5, 7.0),  # off zero
        (0.3, 14.13),  # off critical line
        (0.7, 14.13),
    ]
    for re_b, im_b in test_points:
        if abs(re_b - 1.0) < 0.01 and abs(im_b) < 0.01:
            print(f"β={re_b}+{im_b}i (pole, skip)")
            continue
        F = free_energy(complex(re_b, im_b))
        try:
            S = entropy_real(re_b, im_b)
        except Exception:
            S = float("nan")
        try:
            C = heat_capacity(re_b, im_b)
        except Exception:
            C = float("nan")
        print(f"β={re_b}+{im_b}i".ljust(25) + f"{float(F.real):<15.4f}{float(F.imag):<15.4f}{S:<15.4f}{C:<15.4f}")

    print("\nObservation: at zeros (β = 0.5 + iγ), F → +∞ (since ζ→0).")
    print("This is *Lee-Yang* style — partition function zeros on critical line.")
    print("BUT: classical Lee-Yang theorem requires *unit circle* zeros (different geometry).")
    print("→ ζ-zeros ≠ Lee-Yang zeros. *failure* of direct mapping.")


if __name__ == "__main__":
    main()
