"""Montgomery's pair correlation conjecture for ζ zeros.

Normalized zero gaps: γ̃_n = (γ_n / 2π) log(γ_n / 2π).

Montgomery 1973 conjecture:
    Σ_{α ≤ γ̃ - γ̃' ≤ β} 1 ~ N(T) ∫_α^β [1 - (sin πu / πu)²] du

The integrand 1 - (sin πu / πu)² coincides with the GUE pair correlation function
(Gaussian Unitary Ensemble) — Dyson's identification.

수치 도구: 영점 간격 정규화 → 히스토그램 비교.
RMT 모델 정합성 신호 — 증명 X. RH 에 대한 *간접 evidence* 만 제공.
"""

from __future__ import annotations

import argparse
import math

import mpmath


def normalized_gaps(num_zeros: int, dps: int = 30) -> list[float]:
    """Compute normalized gaps γ̃_{n+1} - γ̃_n for n = 1..num_zeros - 1.

    Each γ̃_n = (γ_n / 2π) log(γ_n / 2π) where γ_n is the imaginary part of the n-th zero.
    """
    mpmath.mp.dps = dps
    gammas = [float(mpmath.zetazero(n).imag) for n in range(1, num_zeros + 1)]
    normalized = [(g / (2 * math.pi)) * math.log(g / (2 * math.pi)) for g in gammas]
    return [normalized[i + 1] - normalized[i] for i in range(len(normalized) - 1)]


def gue_density(u: float) -> float:
    """GUE pair-correlation density 1 - (sin πu / πu)² (Montgomery–Dyson)."""
    if u == 0:
        return 0.0
    return 1.0 - (math.sin(math.pi * u) / (math.pi * u)) ** 2


def main() -> None:
    """CLI — print histogram of normalized gaps + GUE prediction at bin centers."""
    parser = argparse.ArgumentParser(description="Pair correlation of zeta zeros vs GUE.")
    parser.add_argument("-n", type=int, default=200, help="Number of zeros (default 200).")
    parser.add_argument("--bins", type=int, default=20, help="Histogram bins.")
    parser.add_argument("--max", type=float, default=3.0, help="Max gap to histogram.")
    parser.add_argument("--dps", type=int, default=30, help="Decimal precision.")
    args = parser.parse_args()

    print(f"Computing first {args.n} zeros and normalized gaps...")
    gaps = normalized_gaps(args.n, args.dps)
    bin_width = args.max / args.bins
    counts = [0] * args.bins
    for g in gaps:
        idx = int(g / bin_width)
        if 0 <= idx < args.bins:
            counts[idx] += 1
    total = sum(counts)
    print(f"\n{'bin center':>12} {'empirical':>12} {'GUE':>10}")
    print("-" * 40)
    for i in range(args.bins):
        center = (i + 0.5) * bin_width
        emp_density = counts[i] / (total * bin_width) if total else 0.0
        gue = gue_density(center)
        print(f"{center:>12.3f} {emp_density:>12.4f} {gue:>10.4f}")
    print()
    print("주의: 본 통계 정합성은 RH 의 간접 evidence — 증명 아님.")


if __name__ == "__main__":
    main()
