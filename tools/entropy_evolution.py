"""Track differential entropy of kernel-smoothed empirical measure under zero ODE.

H[μ_t] = -∫ ρ_t(x) log ρ_t(x) dx,
where ρ_t(x) = (1/N) Σ K_h(x - x_k(t)) and K_h is a Gaussian kernel.

forward (t > 0): zeros spread, expect H ↑.
backward (t < 0): zeros cluster, expect H ↓.

If asymmetric → path-dependent functional caught (unlike Wasserstein).
"""

from __future__ import annotations

import argparse
import math

import numpy as np

from heat_flow_simulation import initial_zeros, rk4_step


def kernel_density_entropy(
    x: np.ndarray, bandwidth: float, n_grid: int = 1000, span_factor: float = 5.0
) -> float:
    """Estimate differential entropy of N(x_k, h²) mixture density via grid quadrature."""
    n = len(x)
    x_min, x_max = float(np.min(x)), float(np.max(x))
    pad = span_factor * bandwidth
    xs = np.linspace(x_min - pad, x_max + pad, n_grid)
    # density: (1/N) Σ N(x; x_k, h²)
    diffs = xs[:, None] - x[None, :]  # shape (n_grid, n)
    pdfs = np.exp(-0.5 * (diffs / bandwidth) ** 2) / (
        bandwidth * math.sqrt(2 * math.pi)
    )
    rho = np.mean(pdfs, axis=1)
    rho_safe = np.clip(rho, 1e-30, None)
    h_value = -float(np.trapezoid(rho_safe * np.log(rho_safe), xs))
    return h_value


def main() -> None:
    parser = argparse.ArgumentParser(description="Entropy evolution under zero ODE.")
    parser.add_argument("-n", type=int, default=20)
    parser.add_argument("-T", type=float, default=0.001)
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--bandwidth", type=float, default=0.3)
    parser.add_argument("--dps", type=int, default=30)
    args = parser.parse_args()

    x0 = initial_zeros(args.n, args.dps)
    h0 = kernel_density_entropy(x0, args.bandwidth)
    print(f"x0 range [{x0[0]:.3f}, {x0[-1]:.3f}], H[μ_0] = {h0:.6f}")
    print(f"bandwidth = {args.bandwidth}")
    print()

    print(f"{'direction':>10} {'t':>10} {'H[μ_t]':>15} {'ΔH':>15}")
    print("-" * 55)
    for direction, label in [(+1, "forward"), (-1, "backward")]:
        dt = direction * args.T / args.steps
        x = x0.copy()
        for step in range(args.steps + 1):
            t = step * dt
            h_val = kernel_density_entropy(x, args.bandwidth)
            if step % max(1, args.steps // 5) == 0 or step == args.steps:
                print(
                    f"{label:>10} {t:>10.5f} {h_val:>15.6f} "
                    f"{h_val - h0:>+15.3e}"
                )
            if step < args.steps:
                x = rk4_step(x, dt)

    print()
    print("Note: H is differential entropy of kernel density estimate.")
    print("If forward dH/dt > 0 and backward dH/dt < 0 → path-dependent asymmetry caught.")


if __name__ == "__main__":
    main()
