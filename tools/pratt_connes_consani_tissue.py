"""Tissue 4 numerical: Pratt-Robles A^{(1,1)} ↔ Connes-Consani QW_λ prime sensitivity."""

from __future__ import annotations

import math

import sympy


def pratt_A11_partial(p_max: int) -> float:
    """A^{(1,1)} = -Σ_p (log p / (p-1))² up to p ≤ p_max."""
    return -sum((math.log(p) / (p - 1)) ** 2 for p in sympy.primerange(2, p_max + 1))


def main() -> None:
    print("=== Tissue 4: Pratt-Robles A^{(1,1)} ↔ Connes-Consani QW_λ ===\n")

    print("Pratt-Robles §6 (attempt 104): A^{(1,1)} = -Σ_p (log p/(p-1))².")
    print("Connes-Consani §2.3 (attempt 111): QW_λ semi-local primes p < λ². sign sensitive p=2.\n")

    print(f"{'p_max':<10}{'partial A^{(1,1)}':<25}{'cumulative removal of p_first':<30}")
    primes = list(sympy.primerange(2, 1000))[:30]
    cumulative = 0.0
    for i, p in enumerate(primes):
        cumulative -= (math.log(p) / (p - 1)) ** 2
        print(f"  through p={p:<5}: A_partial = {cumulative:<25.6f} (added p={p}: {-(math.log(p)/(p-1))**2:.6f})")

    print("\n--- p=2 sensitivity (Connes-Consani §2.3 paper-direct) ---")
    print("Pratt-Robles only-p=2: -(log 2/1)² = -0.480453.")
    print(f"  Pratt-Robles full p≤100000 (attempt 104): -1.385480 (paper -1.385604).")
    print(f"  p=2 contribution / total: {0.480453/1.385480:.4f} ≈ 35%.")

    print("\nConnes-Consani §2.3 quote (paper-direct, attempt 111):")
    print('  "the contribution from the archimedean place alone ceases to be positive"')
    print("  in interval log(λ²) in [log 2 - 0.2, log 2 + 0.2]")
    print('  "positivity is restored by adding the contribution of the prime 2"')

    print("\n→ paper-direct Tissue 4 confirmation:")
    print("  Pratt-Robles A^{(1,1)} = global Σ_p sum (no individual sensitivity).")
    print("  Connes-Consani QW_λ = local λ-cutoff (prime-by-prime sensitivity).")
    print("  *same prime-side* class, *different scoping* (global sum vs local cutoff).")


if __name__ == "__main__":
    main()
