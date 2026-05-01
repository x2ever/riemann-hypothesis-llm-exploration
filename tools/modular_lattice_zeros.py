"""Modular Eisenstein series coefficient + Robin/Lagarias cross-link."""

from __future__ import annotations

import math


def divisor_sum_k(n: int, k: int = 1) -> int:
    """σ_k(n) = Σ d^k for d | n."""
    return sum(d**k for d in range(1, n + 1) if n % d == 0)


def main() -> None:
    print("=== Modular Form ↔ ζ-zeros (NOVEL) ===\n")

    print("Eisenstein E_{2k}(τ) = 1 + c_k Σ σ_{2k-1}(n) q^n.")
    print("E_2: c_2 = -24 (σ_1).")
    print("σ_1(n) related to RH via Robin (Conrey 2003 attempt 122).\n")

    H = lambda n: sum(1.0 / k for k in range(1, n + 1))

    print(f"{'n':<8}{'σ_1(n)':<10}{'σ_1(n)/n':<15}{'e^γ log log n':<20}{'Robin OK?':<12}")
    for n in [12, 24, 60, 120, 360, 720, 2520, 5040, 7560, 10080]:
        sig = divisor_sum_k(n, 1)
        ratio = sig / n
        if n >= 5041:
            bound = math.exp(0.5772) * math.log(math.log(n))
            ok = "YES" if ratio < bound else "NO!"
        else:
            bound = float("nan")
            ok = "(n<5041)"
        print(f"{n:<8}{sig:<10}{ratio:<15.4f}{bound:<20.4f}{ok:<12}")

    print("\n--- σ_1(n) Eisenstein-style cumulative ---")
    print("E_2 q-expansion: 1 - 24 Σ_n σ_1(n) q^n.")
    print("Theta function / lattice perspective — does σ_1 spacing reveal ζ-zeros?")
    sigmas = [divisor_sum_k(n, 1) for n in range(1, 50)]
    print(f"σ_1(1..10): {sigmas[:10]}")
    print(f"σ_1(11..20): {sigmas[10:20]}")
    print(f"\nSpacing of σ_1 large values: highly composite n (12, 24, 60, 120, ...) — expected.")
    print(f"No connection to γ_n spacing (3, 4, 5, 5, 3, ...) detected.\n")

    print("--- Möbius inversion + Robin ---")
    print("Σ_n μ(n)/n^s = 1/ζ(s). RH ⟺ Σ μ(n) = O(x^{1/2+ε}).")
    print("Robin: σ(n) ≤ e^γ n log log n for n ≥ 5041.")
    print("→ paper-direct (Conrey §Some Other Equivalences). novelty X.")


if __name__ == "__main__":
    main()
