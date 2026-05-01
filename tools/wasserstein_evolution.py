"""Track Wasserstein-2 evolution of ζ zero empirical measure under heat-flow ODE.

For empirical measures μ = (1/n) Σ δ_{x_k} with sorted points {x_k},
the W_2 distance reduces to:
    W_2(μ_a, μ_b)² = (1/n) · Σ_k (a_k - b_k)²
when both have the same number of points (sorted matched).

Tracks:
- W₂(μ_t, μ_0) along forward/backward ODE evolution.
- Energy E(t) for comparison.
- Numerical d/dt W₂² vs theoretical predictions from Otto's calculus.
"""

from __future__ import annotations

import argparse

import numpy as np

# Reuse the ODE machinery from heat_flow_simulation.
from heat_flow_simulation import (
    energy,
    initial_zeros,
    rk4_step,
    vector_field,
)


def w2_squared(x: np.ndarray, y: np.ndarray) -> float:
    """W₂² between empirical measures with same n points (matched by sort order)."""
    xs = np.sort(x)
    ys = np.sort(y)
    return float(np.mean((xs - ys) ** 2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Track W₂ evolution of ζ zero ODE."
    )
    parser.add_argument("-n", type=int, default=20)
    parser.add_argument("-T", type=float, default=0.001)
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--dps", type=int, default=30)
    args = parser.parse_args()

    x0 = initial_zeros(args.n, args.dps)
    print(f"Initial: N={args.n}, range [{x0[0]:.3f}, {x0[-1]:.3f}]")
    print()

    print(f"{'direction':>10} {'t':>10} {'W2^2':>15} {'energy':>15} {'dW2^2/dt':>15}")
    print("-" * 75)

    for direction, label in [(+1, "forward"), (-1, "backward")]:
        dt = direction * args.T / args.steps
        x = x0.copy()
        prev_w2 = 0.0
        for step in range(args.steps + 1):
            t = step * dt
            w2sq = w2_squared(x, x0)
            e = energy(x)
            if step > 0:
                dw2 = (w2sq - prev_w2) / abs(dt)
            else:
                dw2 = float("nan")
            if step % max(1, args.steps // 5) == 0 or step == args.steps:
                print(
                    f"{label:>10} {t:>10.5f} {w2sq:>15.4e} "
                    f"{e:>15.4f} {dw2:>15.4e}"
                )
            prev_w2 = w2sq
            if step < args.steps:
                x = rk4_step(x, dt)

    print()
    print(
        "Note: W₂² along the ODE solution. d/dt W₂² ~ 2·⟨v, x-x₀⟩ where v = dx/dt = 2·Σ 1/(x_k-x_j).\n"
        "Comparison with E(t) = Σ 1/(x_j-x_k)² should reveal Otto-type calculus structure."
    )


if __name__ == "__main__":
    main()
