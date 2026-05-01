"""Discrete quantum walk on ζ-zeros line."""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


def main() -> None:
    print("=== Quantum Walk on ζ-zeros (NOVEL) ===\n")

    N = 50
    zeros = np.array([float(mp.zetazero(n).imag) for n in range(1, N + 1)])
    spacings = np.diff(zeros)
    print(f"First {N} ζ-zeros γ_n.")
    print(f"Mean spacing: {spacings.mean():.4f}, std: {spacings.std():.4f}")
    print(f"Predicted by RvM: 2π/log γ_n.")

    coin_unitary = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

    psi = np.zeros((N, 2), dtype=complex)
    psi[0, 0] = 1.0

    print("\n--- Walk on ζ-zeros line, T=20 steps ---")
    T = 20
    for t in range(T):
        psi = psi @ coin_unitary.T
        new_psi = np.zeros_like(psi)
        for n in range(N):
            if n + 1 < N:
                new_psi[n + 1, 0] += psi[n, 0]
            if n - 1 >= 0:
                new_psi[n - 1, 1] += psi[n, 1]
        psi = new_psi

    prob = np.abs(psi[:, 0]) ** 2 + np.abs(psi[:, 1]) ** 2
    if prob.sum() > 0:
        prob = prob / prob.sum()

    print(f"Probability distribution after T={T}:")
    for n in range(min(20, N)):
        bar = "█" * int(prob[n] * 100)
        print(f"  γ_{n+1}={zeros[n]:6.2f}  p={prob[n]:.4f}  {bar}")

    print("\n--- Counterfactual: uniform spacing line ---")
    psi2 = np.zeros((N, 2), dtype=complex)
    psi2[0, 0] = 1.0
    for t in range(T):
        psi2 = psi2 @ coin_unitary.T
        new_psi = np.zeros_like(psi2)
        for n in range(N):
            if n + 1 < N:
                new_psi[n + 1, 0] += psi2[n, 0]
            if n - 1 >= 0:
                new_psi[n - 1, 1] += psi2[n, 1]
        psi2 = new_psi

    prob2 = np.abs(psi2[:, 0]) ** 2 + np.abs(psi2[:, 1]) ** 2
    if prob2.sum() > 0:
        prob2 = prob2 / prob2.sum()

    print(f"Standard deviation, ζ-zeros walk: {np.std(np.arange(N) * prob):.4f}")
    print(f"Standard deviation, uniform walk: {np.std(np.arange(N) * prob2):.4f}")
    print("\nObservation: Hadamard QW has same spread regardless of underlying line.")
    print("→ ζ-zeros structure NOT visible in standard QW. *failure*.")


if __name__ == "__main__":
    main()
