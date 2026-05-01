"""Verify the first N nontrivial zeros of the Riemann zeta function lie on Re(s) = 1/2.

수치 실험 — 직관 보조 도구. 이것은 RH의 증명이 아니다.
유한 개의 영점 검증은 RH의 *반증*은 가능해도 *증명*은 불가능하다.
"""

from __future__ import annotations

import argparse

import mpmath


def verify_first_n_zeros(n: int, dps: int = 50) -> list[tuple[int, mpmath.mpc, mpmath.mpf]]:
    """Compute the first n nontrivial zeros and verify Re(s) = 1/2.

    Args:
        n: Number of zeros to compute (counted from the first one above the real axis).
        dps: Decimal precision for mpmath.

    Returns:
        List of (index, zero, deviation_from_half) tuples.
        deviation = |Re(zero) - 1/2| (should be 0 to working precision if RH holds).
    """
    mpmath.mp.dps = dps
    results: list[tuple[int, mpmath.mpc, mpmath.mpf]] = []
    half = mpmath.mpf("0.5")
    for k in range(1, n + 1):
        zero = mpmath.zetazero(k)
        deviation = abs(zero.real - half)
        results.append((k, zero, deviation))
    return results


def main() -> None:
    """CLI entry — print first N zeros with their Re-deviation from 1/2."""
    parser = argparse.ArgumentParser(description="Verify Re(zeta_zero) = 1/2 numerically.")
    parser.add_argument("-n", type=int, default=20, help="Number of zeros (default 20)")
    parser.add_argument("--dps", type=int, default=50, help="Decimal precision (default 50)")
    args = parser.parse_args()

    print(f"Computing first {args.n} nontrivial zeros at {args.dps} dps...")
    print(f"{'k':>4} {'Im(zero)':>30} {'|Re - 1/2|':>15}")
    print("-" * 55)

    max_dev = mpmath.mpf(0)
    for k, zero, dev in verify_first_n_zeros(args.n, args.dps):
        max_dev = max(max_dev, dev)
        print(f"{k:>4} {mpmath.nstr(zero.imag, 20):>30} {mpmath.nstr(dev, 4):>15}")

    print("-" * 55)
    print(f"Max deviation from Re=1/2: {mpmath.nstr(max_dev, 4)}")
    print()
    print("주의: 유한 영점 검증은 RH 증명이 아니다. 직관/수치 신호용으로만 사용.")


if __name__ == "__main__":
    main()
