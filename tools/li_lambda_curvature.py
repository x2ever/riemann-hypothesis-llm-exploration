"""λ_n curvature/convexity exploration."""

from __future__ import annotations

import math

import mpmath as mp


def li_lambda(n: int, num_zeros: int = 200) -> float:
    """λ_n = Σ_ρ (1 - (1-1/ρ)^n)."""
    total = mp.mpf(0)
    for j in range(1, num_zeros + 1):
        gamma = mp.zetazero(j).imag
        for sign in [+1, -1]:
            rho = mp.mpc(mp.mpf("0.5"), sign * gamma)
            term = 1 - (1 - 1 / rho) ** n
            total += term.real
    return float(total)


def main() -> None:
    mp.mp.dps = 30
    print("=== λ_n Curvature/Convexity (NOVEL) ===\n")

    print("Computing λ_n for n=1..30 with 100 zeros...")
    lambdas = []
    for n in range(1, 31):
        lambdas.append(li_lambda(n, num_zeros=100))

    print(f"\n{'n':<5}{'λ_n':<15}{'Δλ':<15}{'Δ²λ':<15}{'log conv?':<15}")
    for n in range(len(lambdas)):
        l = lambdas[n]
        dl = lambdas[n + 1] - lambdas[n] if n + 1 < len(lambdas) else float("nan")
        d2l = (
            lambdas[n + 2] - 2 * lambdas[n + 1] + lambdas[n]
            if n + 2 < len(lambdas)
            else float("nan")
        )
        if 0 < n < len(lambdas) - 1:
            lc = "YES" if lambdas[n - 1] * lambdas[n + 1] >= lambdas[n] ** 2 else "NO"
        else:
            lc = "-"
        print(f"{n+1:<5}{l:<15.6f}{dl:<15.6f}{d2l:<15.6f}{lc:<15}")

    print("\n--- Δ² λ analysis ---")
    deltasq = [
        lambdas[n + 2] - 2 * lambdas[n + 1] + lambdas[n] for n in range(len(lambdas) - 2)
    ]
    pos = sum(1 for x in deltasq if x > 0)
    neg = sum(1 for x in deltasq if x < 0)
    print(f"Δ²λ > 0 count: {pos}/{len(deltasq)}")
    print(f"Δ²λ < 0 count: {neg}/{len(deltasq)}")

    print("\n--- log convex? log λ_{n+1} ≤ (log λ_n + log λ_{n+2})/2 ---")
    log_conv = []
    for n in range(1, len(lambdas) - 1):
        if lambdas[n - 1] > 0 and lambdas[n + 1] > 0 and lambdas[n] > 0:
            lhs = math.log(lambdas[n])
            rhs = (math.log(lambdas[n - 1]) + math.log(lambdas[n + 1])) / 2
            log_conv.append(lhs <= rhs)
    print(f"Log convex satisfied: {sum(log_conv)}/{len(log_conv)}")


if __name__ == "__main__":
    main()
