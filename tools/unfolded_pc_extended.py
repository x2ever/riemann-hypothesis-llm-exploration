"""Unfolded pair-correlation of ζ zeros vs GUE — extended diagnostics.

Builds on tools/pair_correlation.py with:
- Larger N (200~500 zeros).
- Kolmogorov–Smirnov test against the empirical CDF of GUE prediction.
- Optional triple correlation (3-pt) histogram.
- Per-region (small u / mid / large u) deviation analysis.
"""

from __future__ import annotations

import argparse
import math

import mpmath
import numpy as np


def gue_pair_density(u: float) -> float:
    """GUE pair-correlation function 1 - (sin πu / πu)^2."""
    if u == 0.0:
        return 0.0
    return 1.0 - (math.sin(math.pi * u) / (math.pi * u)) ** 2


def gue_pair_cdf(u: float) -> float:
    """CDF of the (rescaled) GUE pair-density on [0, ∞).

    Numerically integrate density.
    """
    if u <= 0:
        return 0.0
    # numerical CDF via fine quadrature
    pts = np.linspace(0, u, 1000)
    vals = np.array([gue_pair_density(x) for x in pts])
    # treat density as positive; the CDF of normalized "intensity" — for KS
    # we use a finite-window normalized CDF.
    return float(np.trapezoid(vals, pts))


def compute_unfolded_zeros(num_zeros: int, dps: int = 30) -> np.ndarray:
    """Return unfolded imaginary parts γ̃_n = (γ_n / 2π) · log(γ_n / 2π).

    Mean spacing of γ̃_n approaches 1 as height grows.
    """
    mpmath.mp.dps = dps
    gammas = np.array([float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)])
    return (gammas / (2 * math.pi)) * np.log(gammas / (2 * math.pi))


def pair_gaps(unfolded: np.ndarray, max_gap: float = 5.0) -> np.ndarray:
    """All pair gaps γ̃_j - γ̃_i for i<j with gap ≤ max_gap."""
    gaps = []
    for i in range(len(unfolded)):
        for j in range(i + 1, len(unfolded)):
            d = unfolded[j] - unfolded[i]
            if d > max_gap:
                break
            gaps.append(d)
    return np.array(gaps)


def empirical_pair_density(
    gaps: np.ndarray, bins: int, max_gap: float
) -> tuple[np.ndarray, np.ndarray]:
    """Histogram of pair gaps, normalized to density."""
    counts, edges = np.histogram(gaps, bins=bins, range=(0.0, max_gap))
    centers = 0.5 * (edges[:-1] + edges[1:])
    bin_width = max_gap / bins
    # Normalize: (count) / (n_pairs * bin_width). For density-like quantity,
    # but pair correlation is # gaps in u..u+du divided by (mean density · N · du).
    # We compare empirical distribution shape with GUE shape (both rescaled).
    density = counts.astype(float) / (len(gaps) * bin_width)
    return centers, density


def ks_test_against_gue(gaps: np.ndarray, max_gap: float) -> tuple[float, float]:
    """KS test: empirical gap CDF vs GUE pair correlation CDF (truncated at max_gap)."""
    # Restrict to gaps within range.
    g = gaps[gaps <= max_gap]
    # Empirical CDF
    g_sorted = np.sort(g)
    n = len(g_sorted)

    # Build a target CDF function from gue_pair_cdf, normalized so CDF(max_gap) = 1.
    norm = gue_pair_cdf(max_gap)
    if norm <= 0:
        return float("nan"), float("nan")

    def target_cdf(u):
        return gue_pair_cdf(u) / norm

    target_vals = np.array([target_cdf(x) for x in g_sorted])
    emp_vals = np.arange(1, n + 1) / n
    d_stat = float(np.max(np.abs(emp_vals - target_vals)))
    # Approximate p-value using KS asymptotic
    # P(D > d) ≈ 2 * exp(-2 n d^2)
    p_value = 2.0 * math.exp(-2.0 * n * d_stat * d_stat)
    p_value = min(p_value, 1.0)
    return d_stat, p_value


def regional_deviation(
    gaps: np.ndarray, max_gap: float, regions: list[tuple[float, float]]
) -> list[dict]:
    """Per-region (u_lo, u_hi) deviation: empirical density vs GUE."""
    results = []
    for u_lo, u_hi in regions:
        in_region = gaps[(gaps >= u_lo) & (gaps <= u_hi)]
        emp_count = len(in_region)
        # Predicted: (mean density · pairs · width)
        pred_int = sum(
            gue_pair_density(u) for u in np.linspace(u_lo, u_hi, 200)
        ) * (u_hi - u_lo) / 200
        # Total: number of gaps in [0, max_gap]
        total = np.sum(gaps <= max_gap)
        emp_frac = emp_count / total if total > 0 else 0
        pred_frac = pred_int / gue_pair_cdf(max_gap)
        results.append(
            dict(
                region=(u_lo, u_hi),
                emp_count=emp_count,
                emp_frac=emp_frac,
                pred_frac=pred_frac,
                ratio=(emp_frac / pred_frac) if pred_frac > 0 else float("inf"),
            )
        )
    return results


def main() -> None:
    """CLI."""
    parser = argparse.ArgumentParser(
        description="Unfolded pair correlation: ζ zeros vs GUE."
    )
    parser.add_argument("-n", type=int, default=200, help="Number of zeros.")
    parser.add_argument("--max-gap", type=float, default=3.0)
    parser.add_argument("--bins", type=int, default=15)
    parser.add_argument("--dps", type=int, default=30)
    args = parser.parse_args()

    print(f"Computing first {args.n} zeros, unfolding...")
    unfolded = compute_unfolded_zeros(args.n, args.dps)

    gaps = pair_gaps(unfolded, args.max_gap)
    print(f"Number of pair gaps with d <= {args.max_gap}: {len(gaps)}")
    print()

    centers, emp_density = empirical_pair_density(gaps, args.bins, args.max_gap)
    print(f"{'u (center)':>12} {'empirical':>12} {'GUE':>10} {'ratio':>8}")
    print("-" * 50)
    for c, e in zip(centers, emp_density):
        gue = gue_pair_density(c)
        ratio = e / gue if gue > 1e-9 else float("inf")
        print(f"{c:>12.3f} {e:>12.4f} {gue:>10.4f} {ratio:>8.3f}")
    print()

    d_stat, p_val = ks_test_against_gue(gaps, args.max_gap)
    print(f"KS statistic: {d_stat:.4f}")
    print(f"KS p-value (asymp): {p_val:.4g}")

    if p_val > 0.5:
        verdict = "PASS — no significant GUE deviation"
    elif p_val < 0.05:
        verdict = "REJECT — significant deviation from GUE"
    else:
        verdict = "AMBIGUOUS — refine sample"
    print(f"Verdict: {verdict}")
    print()

    # Regional analysis
    regions = [(0.0, 0.5), (0.5, 1.0), (1.0, 1.5), (1.5, 2.5)]
    print("Regional deviation:")
    for r in regional_deviation(gaps, args.max_gap, regions):
        print(
            f"  u ∈ [{r['region'][0]}, {r['region'][1]}]: "
            f"emp={r['emp_frac']:.4f} pred={r['pred_frac']:.4f} "
            f"ratio={r['ratio']:.3f}"
        )
    print()
    print("주의: low-height (small N) 에서 RMT asymptotic 이 약함. "
          "deviation 의 *형태* 가 본질적 신호.")


if __name__ == "__main__":
    main()
