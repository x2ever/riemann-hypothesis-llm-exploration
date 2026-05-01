"""KL divergence between empirical ζ-zero spacing and GUE prediction."""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


def gue_wigner_dyson(s: float) -> float:
    """GUE pair correlation density (approximation)."""
    return (32 / math.pi**2) * s**2 * math.exp(-4 * s**2 / math.pi)


def main() -> None:
    print("=== KL(empirical || GUE) divergence (NOVEL) ===\n")

    N = 100
    print(f"Computing {N} ζ-zeros...")
    zeros = np.array([float(mp.zetazero(n).imag) for n in range(1, N + 1)])

    log_g = np.log(zeros / (2 * math.pi))
    unfolded = []
    for j, gam in enumerate(zeros):
        unfolded.append((gam / (2 * math.pi)) * (log_g[j] - 1) + 7 / 8)

    spacings = np.diff(unfolded)
    spacings = spacings / spacings.mean()

    print(f"Mean spacing (normalized): {spacings.mean():.4f}")
    print(f"Std: {spacings.std():.4f}")

    bins = np.linspace(0, 4, 21)
    hist, _ = np.histogram(spacings, bins=bins, density=True)
    bin_centers = 0.5 * (bins[1:] + bins[:-1])

    gue_pdf = np.array([gue_wigner_dyson(s) for s in bin_centers])

    eps = 1e-10
    kl = np.sum(hist * np.log((hist + eps) / (gue_pdf + eps)) * (bins[1] - bins[0]))
    print(f"\nKL(empirical || GUE) = {kl:.4f}")

    poisson_pdf = np.exp(-bin_centers)
    kl_poisson = np.sum(hist * np.log((hist + eps) / (poisson_pdf + eps)) * (bins[1] - bins[0]))
    print(f"KL(empirical || Poisson) = {kl_poisson:.4f}")

    print("\nIf RH true: empirical ≈ GUE → KL → 0.")
    print(f"KL(emp || GUE) - KL(emp || Poisson) = {kl - kl_poisson:.4f}")
    print(f"  (negative = closer to GUE than Poisson)")

    print("\n--- Histogram ---")
    for c, h, g in zip(bin_centers, hist, gue_pdf):
        bar = "█" * int(h * 30)
        print(f"  s={c:.2f}: emp={h:.3f}  GUE={g:.3f}  {bar}")


if __name__ == "__main__":
    main()
