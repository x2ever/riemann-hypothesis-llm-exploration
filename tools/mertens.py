"""Mertens function M(x) = Σ μ(n) for n ≤ x and related RH equivalents.

RH ⟺ M(x) = O(x^(1/2 + ε)) for every ε > 0.
Stronger: Mertens conjecture |M(x)| ≤ √x — *disproved* by Odlyzko & te Riele 1985.

수치 도구. 작은 x 에 대해 빠른 검증·시각화·반례 후보 추출용.
"""

from __future__ import annotations

import argparse
from functools import cache

import mpmath


@cache
def mobius(n: int) -> int:
    """Möbius function μ(n) via trial factorization. O(√n) per call.

    μ(1) = 1; μ(n) = (-1)^k if n is product of k distinct primes; 0 if any p² | n.
    """
    if n == 1:
        return 1
    p = 2
    factors = 0
    m = n
    while p * p <= m:
        if m % p == 0:
            m //= p
            factors += 1
            if m % p == 0:
                return 0
        p += 1
    if m > 1:
        factors += 1
    return -1 if factors % 2 else 1


def mertens(x: int) -> int:
    """M(x) = Σ_{n ≤ x} μ(n). O(x √x) naive — fine for x ≤ 10^6 ish."""
    return sum(mobius(n) for n in range(1, x + 1))


def mertens_ratio(x: int) -> float:
    """M(x) / √x. Mertens conjecture asserted |·| ≤ 1 — *disproved* (Odlyzko–te Riele 1985)."""
    return mertens(x) / x**0.5


def main() -> None:
    """CLI entry — print M(x), M(x)/√x, M(x)/x^(1/2+ε)."""
    parser = argparse.ArgumentParser(description="Mertens function and RH equivalent ratios.")
    parser.add_argument("x_max", type=int, help="Compute M(x) up to this value.")
    parser.add_argument("--step", type=int, default=1000, help="Print every <step> values.")
    parser.add_argument("--epsilon", type=float, default=0.0, help="Use exponent 1/2 + ε.")
    args = parser.parse_args()

    exponent = 0.5 + args.epsilon
    print(f"{'x':>10} {'M(x)':>10} {'M(x)/sqrt(x)':>15} {'M(x)/x^'+str(exponent):>20}")
    print("-" * 60)
    running = 0
    for n in range(1, args.x_max + 1):
        running += mobius(n)
        if n % args.step == 0 or n == args.x_max:
            ratio_half = running / n**0.5
            ratio_eps = running / n**exponent
            print(f"{n:>10} {running:>10} {ratio_half:>15.6f} {ratio_eps:>20.6f}")
    print()
    print("주의: M(x) = O(x^(1/2+ε)) ⟺ RH. 수치는 *증명 아님*; 반증 도구로만 강력.")
    print("Mertens 추측 |M(x)|/√x ≤ 1 은 1985년 Odlyzko–te Riele 가 반증.")


if __name__ == "__main__":
    main()
