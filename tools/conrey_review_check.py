"""Conrey 2003 Notices numerical verifications.

- Hardy-Littlewood 1918 equivalence: Σ (-x)^k / (k! ζ(2k+1)) = O(x^{-1/4}).
- Robin/Lagarias 2002: σ(n) ≤ H_n + exp(H_n) log H_n.
- Moments g_k = k!² Π_{j=0}^{k-1} j!/(j+k)!.
"""

from __future__ import annotations

import math

import mpmath as mp


def hardy_littlewood_sum(x: float, max_k: int = 50) -> mp.mpf:
    """Σ_{k=1}^∞ (-x)^k / (k! ζ(2k+1))."""
    mp.mp.dps = 50
    x_mp = mp.mpf(str(x))
    total = mp.mpf(0)
    for k in range(1, max_k + 1):
        term = (-x_mp) ** k / (mp.factorial(k) * mp.zeta(2 * k + 1))
        total += term
    return total


def divisor_sum(n: int) -> int:
    """σ(n) = sum of divisors."""
    return sum(d for d in range(1, n + 1) if n % d == 0)


def harmonic(n: int) -> float:
    """H_n = 1 + 1/2 + ... + 1/n."""
    return sum(1.0 / k for k in range(1, n + 1))


def keating_snaith_g(k: int) -> int:
    """g_k = k!² Π_{j=0}^{k-1} j!/(j+k)! (Keating-Snaith 1999)."""
    result = math.factorial(k) ** 2
    for j in range(k):
        result *= math.factorial(j)
    for j in range(k):
        result //= math.factorial(j + k)
    return result


def main() -> None:
    """Verify Conrey 2003 paper formulas."""
    mp.mp.dps = 50
    print("=== Conrey 2003 Notices Numerical Verification ===\n")

    print("--- Hardy-Littlewood 1918 (paper §Some Other Equivalences) ---")
    print("RH ⟺ Σ_{k=1}^∞ (-x)^k / (k! ζ(2k+1)) = O(x^{-1/4}) as x → ∞.")
    print(f"{'x':<10}{'Σ':<25}{'x^(-1/4)':<25}{'ratio':<15}")
    for x in [10, 100, 1000, 10000]:
        s = hardy_littlewood_sum(x, max_k=80)
        bound = mp.mpf(x) ** (-0.25)
        ratio = abs(s) / bound
        print(f"{x:<10}{float(s):<25.10f}{float(bound):<25.10f}{float(ratio):<15.6f}")

    print("\n--- Robin/Lagarias 2002 criterion ---")
    print("RH ⟺ σ(n) ≤ H_n + exp(H_n) log H_n for all n ≥ 1.")
    print("Equivalent to Robin: σ(n) < e^γ n log log n for n ≥ 5041.")
    print(f"{'n':<8}{'σ(n)':<12}{'H_n':<15}{'exp(H_n) log H_n':<25}{'sum':<15}{'σ ≤ sum?':<10}")
    for n in [1, 2, 3, 4, 5, 6, 12, 24, 60, 120, 180, 720, 2520]:
        sigma = divisor_sum(n)
        Hn = harmonic(n)
        bound = Hn + math.exp(Hn) * math.log(Hn) if Hn > 0 else math.inf
        ok = "YES" if sigma <= bound else "NO"
        print(f"{n:<8}{sigma:<12}{Hn:<15.6f}{math.exp(Hn) * math.log(Hn):<25.6f}{bound:<15.6f}{ok:<10}")

    print("\n--- Keating-Snaith 1999 moments g_k ---")
    print("g_k = k!² Π_{j=0}^{k-1} j!/(j+k)!")
    print(f"{'k':<5}{'g_k':<20}{'(paper g_1, g_2, g_3, g_4)':<30}")
    paper = {1: 1, 2: 2, 3: 42, 4: 24024}
    for k in range(1, 6):
        g = keating_snaith_g(k)
        paper_val = paper.get(k, "?")
        match = "✓" if g == paper_val else ("?" if paper_val == "?" else "✗")
        print(f"{k:<5}{g:<20}{paper_val:<25} {match}")


if __name__ == "__main__":
    main()
