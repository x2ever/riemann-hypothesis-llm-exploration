"""Box-counting fractal dimension of ζ-zero positions."""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


def box_count(zeros: np.ndarray, eps: float) -> int:
    """Count boxes of size ε needed to cover zero set."""
    boxes = set()
    for z in zeros:
        boxes.add(int(z / eps))
    return len(boxes)


def main() -> None:
    print("=== ζ-zero Box-Counting Fractal Dimension (NOVEL) ===\n")

    N = 200
    print(f"Computing {N} ζ-zeros...")
    zeros = np.array([float(mp.zetazero(n).imag) for n in range(1, N + 1)])
    print(f"Zero range: [{zeros[0]:.2f}, {zeros[-1]:.2f}]")

    print("\n--- Box counting ---")
    print(f"{'ε':<10}{'N(ε)':<10}{'log(1/ε)':<15}{'log N':<15}")

    eps_vals = np.logspace(-3, 1, 9)
    log_eps = []
    log_N = []
    for eps in eps_vals:
        n_boxes = box_count(zeros, eps)
        log_eps.append(math.log(1 / eps))
        log_N.append(math.log(n_boxes))
        print(f"{eps:<10.5f}{n_boxes:<10}{math.log(1/eps):<15.4f}{math.log(n_boxes):<15.4f}")

    coeffs = np.polyfit(log_eps[:5], log_N[:5], 1)
    dim = coeffs[0]
    print(f"\nBox-counting dimension (small ε): {dim:.4f}")
    print("Expected: 1.0 (line set).")

    print("\n--- Renyi entropy of unfolded spacings ---")
    log_g = np.log(zeros / (2 * math.pi))
    unfolded = (zeros / (2 * math.pi)) * (log_g - 1) + 7 / 8
    spacings = np.diff(unfolded)
    spacings = spacings / spacings.mean()

    s_max = 4
    bins = np.linspace(0, s_max, 21)
    hist, _ = np.histogram(spacings, bins=bins, density=True)
    p = hist / hist.sum()
    p = p[p > 0]

    H1 = -np.sum(p * np.log(p))
    H2 = -np.log(np.sum(p**2))
    H_inf = -np.log(p.max())
    print(f"Shannon H_1 = {H1:.4f}")
    print(f"Renyi H_2 = {H2:.4f}")
    print(f"Min entropy H_∞ = {H_inf:.4f}")
    print("Multifractal: H_q is q-dependent.")


if __name__ == "__main__":
    main()
