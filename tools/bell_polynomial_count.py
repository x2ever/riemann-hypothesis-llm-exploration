"""Pratt-Robles §3 Bell polynomial diagram count verification."""

from __future__ import annotations

import math


def diagram_count_total(num_polys: int, total_power: int, max_subscript: int = 3) -> int:
    """Count total diagrams = sum over m_1+...+m_d=total_power of Π Σ B_{i, k_i}(1, ..., 1).

    Σ_{k=0}^{max_subscript} B_{i, k}(1,...,1) = Bell number B_i for max_subscript = i.
    """
    bell_partial = {}

    def B_partial(i: int, k: int) -> int:
        """B_{i, k}(1, 1, ..., 1) at x_j = 1."""
        if (i, k) in bell_partial:
            return bell_partial[(i, k)]
        if k == 0 and i == 0:
            return 1
        if k == 0 or i == 0:
            return 0
        if k > i:
            return 0
        result = 0
        for j in range(1, i - k + 2):
            result += math.comb(i - 1, j - 1) * B_partial(i - j, k - 1)
        bell_partial[(i, k)] = result
        return result

    bell_at_1 = {}
    for i in range(1, num_polys + 1):
        bell_at_1[i] = sum(B_partial(i, k) for k in range(0, max_subscript + 1))

    total = 0
    def enumerate_compositions(remaining: int, depth: int, current: list[int]) -> None:
        nonlocal total
        if depth == num_polys:
            if remaining == 0:
                product = 1
                for d, m in enumerate(current, 1):
                    product *= bell_at_1[d] ** m
                total += product
            return
        for m in range(0, remaining + 1):
            enumerate_compositions(remaining - m, depth + 1, current + [m])

    enumerate_compositions(total_power, 0, [])
    return total


def main() -> None:
    """Verify Pratt-Robles §3 diagram counts."""
    print("=== Pratt-Robles §3 Bell Polynomial Diagram Count ===\n")
    print("paper-direct: Bell numbers B_n at x_i = 1.")
    print("B_1 = 1, B_2 = 2, B_3 = 5, B_4 = 15, B_5 = 52, ...\n")

    print("--- Numerical Bell numbers (verification) ---")
    bell_partial_cache: dict = {}

    def B_partial(i: int, k: int) -> int:
        if (i, k) in bell_partial_cache:
            return bell_partial_cache[(i, k)]
        if k == 0 and i == 0:
            return 1
        if k == 0 or i == 0:
            return 0
        if k > i:
            return 0
        result = 0
        for j in range(1, i - k + 2):
            result += math.comb(i - 1, j - 1) * B_partial(i - j, k - 1)
        bell_partial_cache[(i, k)] = result
        return result

    for n in range(1, 6):
        bn = sum(B_partial(n, k) for k in range(0, n + 1))
        print(f"  B_{n} = {bn}")

    print("\n--- §3 (3.8): two polys × three powers ---")
    count = diagram_count_total(num_polys=2, total_power=3, max_subscript=3)
    print(f"  Σ (Σ_k B_{{1,k}}(1))^m_1 (Σ_k B_{{2,k}}(1, 1))^m_2  for m_1+m_2 = 3")
    print(f"  Computed: {count}, paper §3 Fig 3.1: 15")

    print("\n--- §3 (3.9): two polys × four powers ---")
    count = diagram_count_total(num_polys=2, total_power=4, max_subscript=3)
    print(f"  Computed: {count}, paper §3 Fig 3.2: 31")

    print("\n--- §3 (3.10): three polys × three powers ---")
    count = diagram_count_total(num_polys=3, total_power=3, max_subscript=3)
    print(f"  Computed: {count}, paper §3 Fig 3.3: 250")

    print("\n--- Wall #3 quantitative ladder ---")
    print("  d=0 (Conrey-Levinson): 1 mollifier piece (eq 3.7).")
    print("  d=1 (Feng): 9 cases (attempt 104 paper-direct). 41.67% = 5/12.")
    print("  d=2: 15-31 case range (Bell polynomial × powers).")
    print("  d=3: 250 diagrams.")
    print("  → combinatorial explosion = Wall #3 quantitative source.")

    print("\n--- Higher d projection (paper-미명시) ---")
    for d_total in [4, 5, 6]:
        c = diagram_count_total(num_polys=3, total_power=d_total, max_subscript=3)
        print(f"  3 polys × {d_total} powers: {c} diagrams")
    for d_n in [4, 5]:
        c = diagram_count_total(num_polys=d_n, total_power=3, max_subscript=3)
        print(f"  {d_n} polys × 3 powers: {c} diagrams")


if __name__ == "__main__":
    main()
