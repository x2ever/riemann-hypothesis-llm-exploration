"""Weil explicit formula 의 test function efficiency."""

from __future__ import annotations

import math

import mpmath as mp
import sympy


def gaussian_h(t: float, sigma: float) -> float:
    return math.exp(-t**2 / (2 * sigma**2))


def fejer_h(t: float, T: float) -> float:
    if abs(t) >= T:
        return 0.0
    return (1 - abs(t) / T) ** 2


def hermite_h(t: float, sigma: float, k: int) -> float:
    """Hermite-like."""
    H = {0: 1, 2: 4 * t**2 - 2, 4: 16 * t**4 - 48 * t**2 + 12}.get(k, 0)
    return H * math.exp(-t**2 / (2 * sigma**2))


def main() -> None:
    mp.mp.dps = 30
    print("=== Optimal Test Function for Weil Formula (NOVEL) ===\n")

    primes = list(sympy.primerange(2, 1000))
    zeros = [float(mp.zetazero(n).imag) for n in range(1, 200)]

    print(f"{'family':<20}{'param':<15}{'LHS (zeros)':<20}{'RHS (primes)':<20}{'ratio':<15}")

    for sigma in [1, 5, 10, 50, 100]:
        lhs = sum(2 * gaussian_h(g, sigma) for g in zeros)
        rhs = sum(
            2 * (math.log(p) / math.sqrt(p)) * gaussian_h(math.log(p) * sigma * 0.5, sigma)
            for p in primes
        )
        ratio = lhs / rhs if rhs != 0 else float("inf")
        print(f"{'Gaussian':<20}{f'σ={sigma}':<15}{lhs:<20.4f}{rhs:<20.4f}{ratio:<15.4f}")

    for T_val in [10, 30, 100, 200]:
        lhs = sum(fejer_h(g, T_val) for g in zeros)
        rhs = sum(
            2 * (math.log(p) / math.sqrt(p)) * fejer_h(math.log(p), T_val)
            for p in primes
        )
        ratio = lhs / rhs if rhs != 0 else float("inf")
        print(f"{'Fejer':<20}{f'T={T_val}':<15}{lhs:<20.4f}{rhs:<20.4f}{ratio:<15.4f}")


if __name__ == "__main__":
    main()
