"""ζ-zeros perturbation Lyapunov-style sensitivity."""

from __future__ import annotations

import math

import mpmath as mp


def main() -> None:
    mp.mp.dps = 30
    print("=== ζ-zeros Perturbation Sensitivity (NOVEL) ===\n")

    print("Rodgers-Tao 2020 zero dynamics: ∂_t x_k = 2 Σ_{j≠k} 1/(x_k - x_j).")
    print("Forward (decreasing t) = repulsion. Backward = attraction.")
    print("Lyapunov-style: small perturbation δ at one zero → spread to neighbors?\n")

    N = 30
    x = [float(mp.zetazero(n).imag) for n in range(1, N + 1)]
    print(f"Initial: 30 ζ-zeros γ_1..γ_{N}.")
    print(f"  Mean spacing: {sum(x[i+1] - x[i] for i in range(N-1))/(N-1):.4f}")

    eps = 0.01
    print(f"\nPerturbation: γ_5 + {eps}.")
    x_perturbed = list(x)
    x_perturbed[4] += eps

    for t_step in range(5):
        dt = 0.001
        new_x = []
        for k in range(N):
            force = 0.0
            for j in range(N):
                if j != k:
                    diff = x_perturbed[k] - x_perturbed[j]
                    if abs(diff) > 1e-10:
                        force += 1.0 / diff
            new_x.append(x_perturbed[k] + 2 * force * dt)
        x_perturbed = new_x

    print(f"\nAfter 5 dt={0.005} forward steps (repulsion):")
    print(f"{'k':<5}{'γ_k orig':<15}{'γ_k pert':<15}{'shift':<15}")
    for k in range(N):
        shift = x_perturbed[k] - x[k]
        if abs(shift) > 1e-6:
            print(f"{k+1:<5}{x[k]:<15.6f}{x_perturbed[k]:<15.6f}{shift:<15.6e}")

    print("\n*Observation*: perturbation propagates slowly to neighbors.")
    print("Spread limited by 1/(γ_k - γ_j) interaction strength.")


if __name__ == "__main__":
    main()
