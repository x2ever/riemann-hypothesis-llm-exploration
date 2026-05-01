"""Nearest-neighbor spacing distribution P(s) of unfolded ζ zeros vs Wigner surmise.

Wigner surmise (GUE):
    P(s) = (32/π²) · s² · exp(-4s²/π)
which approximates the true GUE eigenvalue spacing distribution to high accuracy.

This is a clean comparison: both sides are honest probability densities on s ≥ 0.
KS test gives a real statistical signal.
"""

from __future__ import annotations

import argparse
import math

import mpmath
import numpy as np


def wigner_pdf(s: float) -> float:
    """GUE Wigner surmise probability density at s ≥ 0."""
    if s < 0:
        return 0.0
    return (32.0 / math.pi**2) * s**2 * math.exp(-4.0 * s**2 / math.pi)


def wigner_cdf(s: float) -> float:
    """CDF of Wigner surmise via numerical integration on [0, s]."""
    if s <= 0:
        return 0.0
    pts = np.linspace(0, s, 1000)
    vals = np.array([wigner_pdf(x) for x in pts])
    return float(np.trapezoid(vals, pts))


def unfolded_spacings(num_zeros: int, dps: int = 30) -> np.ndarray:
    """Compute nearest-neighbor spacings of unfolded zeros, normalized to mean 1."""
    mpmath.mp.dps = dps
    gammas = np.array(
        [float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)]
    )
    unfolded = (gammas / (2 * math.pi)) * np.log(gammas / (2 * math.pi))
    spacings = np.diff(unfolded)
    # Already normalized (mean spacing → 1 asymptotically), but rescale exactly:
    return spacings / np.mean(spacings)


def ks_test(spacings: np.ndarray) -> tuple[float, float]:
    """KS test of empirical spacing distribution against Wigner surmise CDF.

    Returns (D_n, asymptotic p-value).
    """
    sorted_s = np.sort(spacings)
    n = len(sorted_s)
    target = np.array([wigner_cdf(s) for s in sorted_s])
    emp = np.arange(1, n + 1) / n
    d_stat = float(max(np.max(emp - target), np.max(target - (emp - 1 / n))))
    # Asymptotic p-value (Kolmogorov)
    lam = (math.sqrt(n) + 0.12 + 0.11 / math.sqrt(n)) * d_stat
    p = 2.0 * sum(
        (-1) ** (k - 1) * math.exp(-2 * lam * lam * k * k) for k in range(1, 101)
    )
    p = max(min(p, 1.0), 0.0)
    return d_stat, p


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Nearest-neighbor spacing of ζ zeros vs Wigner GUE surmise."
    )
    parser.add_argument("-n", type=int, default=300)
    parser.add_argument("--bins", type=int, default=20)
    parser.add_argument("--max-s", type=float, default=3.0)
    parser.add_argument("--dps", type=int, default=30)
    args = parser.parse_args()

    print(f"Computing first {args.n} ζ zeros (dps={args.dps})...")
    spacings = unfolded_spacings(args.n, args.dps)
    print(f"#spacings = {len(spacings)}, mean = {np.mean(spacings):.4f}")
    print()

    counts, edges = np.histogram(
        spacings, bins=args.bins, range=(0.0, args.max_s)
    )
    centers = 0.5 * (edges[:-1] + edges[1:])
    bin_width = args.max_s / args.bins
    emp_density = counts.astype(float) / (len(spacings) * bin_width)

    print(f"{'s':>8} {'P_emp(s)':>12} {'P_Wigner(s)':>14} {'ratio':>8}")
    print("-" * 48)
    for c, e in zip(centers, emp_density):
        wig = wigner_pdf(c)
        ratio = e / wig if wig > 1e-9 else float("inf")
        print(f"{c:>8.3f} {e:>12.4f} {wig:>14.4f} {ratio:>8.3f}")
    print()

    d_stat, p_val = ks_test(spacings)
    print(f"KS statistic D_n = {d_stat:.4f}")
    print(f"KS p-value (asymptotic) = {p_val:.4g}")

    if p_val > 0.10:
        verdict = "PASS — consistent with Wigner GUE"
    elif p_val < 0.01:
        verdict = "REJECT — significant deviation"
    else:
        verdict = "MARGINAL — refine sample size"
    print(f"Verdict: {verdict}")
    print()
    print("주의: Wigner surmise 는 GUE 의 *분석적 근사* (정확 GUE 와는 작은 차이).")
    print("정확 비교는 GUE eigenvalue 시뮬레이션이 필요하나 surmise 가 1% 정확도.")


if __name__ == "__main__":
    main()
