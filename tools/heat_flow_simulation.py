"""Numerical simulation of the Csordas–Smith–Varga ODE for ζ zero dynamics.

ODE: dx_k/dt = 2 · Σ_{j ≠ k} 1/(x_k - x_j)

This governs the real zeros x_k(t) of H_t under the (backwards) heat equation
∂_t H_t = -∂_zz H_t in the Rodgers–Tao convention.

Forward-time control (t > 0) of this ODE remains a key gap (Wall #2 in our
project). This script does small numerical integration and tracks several
functionals to look for forward-time monotonicity.

CAVEATS:
- For 50 zeros this is qualitative only. Wall #2 won't be solved here.
- The repulsion 1/(x_k - x_j) is singular as gaps shrink — adaptive timestep
  may be needed for backward (t < 0) where zeros cluster.
"""

from __future__ import annotations

import argparse
import math

import mpmath
import numpy as np


def initial_zeros(num_zeros: int, dps: int = 30) -> np.ndarray:
    """First num_zeros imaginary parts γ_k of ζ zeros."""
    mpmath.mp.dps = dps
    return np.array([float(mpmath.zetazero(k).imag) for k in range(1, num_zeros + 1)])


def vector_field(x: np.ndarray) -> np.ndarray:
    """Right-hand side of dx_k/dt = 2 Σ_{j≠k} 1/(x_k - x_j)."""
    n = len(x)
    out = np.zeros(n)
    for k in range(n):
        for j in range(n):
            if j != k:
                d = x[k] - x[j]
                out[k] += 2.0 / d
    return out


def rk4_step(x: np.ndarray, dt: float) -> np.ndarray:
    """One Runge–Kutta 4 step for the zero ODE."""
    k1 = vector_field(x)
    k2 = vector_field(x + 0.5 * dt * k1)
    k3 = vector_field(x + 0.5 * dt * k2)
    k4 = vector_field(x + dt * k3)
    return x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def energy(x: np.ndarray) -> float:
    """E(t) = Σ_{j ≠ k} 1/(x_j - x_k)^2."""
    n = len(x)
    e = 0.0
    for k in range(n):
        for j in range(n):
            if j != k:
                e += 1.0 / (x[k] - x[j]) ** 2
    return e


def hamiltonian(x: np.ndarray) -> float:
    """H(t) = Σ_{j < k} log(1/|x_j - x_k|).  (Half of full sum to avoid double count.)"""
    n = len(x)
    h = 0.0
    for j in range(n):
        for k in range(j + 1, n):
            h += math.log(1.0 / abs(x[k] - x[j]))
    return h


def gap_stats(x: np.ndarray) -> tuple[float, float, float]:
    """Min, mean, std of consecutive gaps."""
    gaps = np.diff(np.sort(x))
    return float(np.min(gaps)), float(np.mean(gaps)), float(np.std(gaps, ddof=1))


def simulate(
    x0: np.ndarray, t_final: float, n_steps: int, direction: int = +1
) -> tuple[np.ndarray, list[dict]]:
    """Integrate ODE from x0 to t_final using RK4 with n_steps.

    direction=+1: forward (dx/dt > 0 dynamics, zeros spread).
    direction=-1: backward (zeros cluster).
    Returns (final_x, history of functionals).
    """
    dt = direction * t_final / n_steps
    x = x0.copy()
    history = []
    for step in range(n_steps + 1):
        t = step * dt
        e = energy(x)
        h = hamiltonian(x)
        mg, meang, stdg = gap_stats(x)
        history.append(
            dict(
                t=t,
                energy=e,
                hamiltonian=h,
                min_gap=mg,
                mean_gap=meang,
                std_gap=stdg,
            )
        )
        if step < n_steps:
            x = rk4_step(x, dt)
    return x, history


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simulate ζ zero dynamics ODE forward and backward."
    )
    parser.add_argument("-n", type=int, default=20, help="Number of zeros")
    parser.add_argument("-T", type=float, default=0.001, help="|t| final")
    parser.add_argument("--steps", type=int, default=20, help="Integration steps")
    parser.add_argument("--dps", type=int, default=30)
    args = parser.parse_args()

    print(f"Loading first {args.n} ζ zeros (dps={args.dps})...")
    x0 = initial_zeros(args.n, args.dps)
    print(f"x0 range: [{x0[0]:.3f}, {x0[-1]:.3f}], min gap = {gap_stats(x0)[0]:.4f}")
    print()

    print(f"Simulating forward to t = {args.T} ...")
    xf, hist_f = simulate(x0, args.T, args.steps, direction=+1)

    print(f"Simulating backward to t = -{args.T} ...")
    xb, hist_b = simulate(x0, args.T, args.steps, direction=-1)

    print()
    print(
        f"{'t':>10} {'energy':>15} {'hamiltonian':>15} "
        f"{'min_gap':>10} {'mean_gap':>10} {'std_gap':>10}"
    )
    print("-" * 80)
    print("[forward, t > 0]")
    for h in hist_f[::max(1, args.steps // 5)]:
        print(
            f"{h['t']:>10.5f} {h['energy']:>15.4f} {h['hamiltonian']:>15.4f} "
            f"{h['min_gap']:>10.4f} {h['mean_gap']:>10.4f} {h['std_gap']:>10.4f}"
        )
    print("[backward, t < 0]")
    for h in hist_b[::max(1, args.steps // 5)]:
        print(
            f"{h['t']:>10.5f} {h['energy']:>15.4f} {h['hamiltonian']:>15.4f} "
            f"{h['min_gap']:>10.4f} {h['mean_gap']:>10.4f} {h['std_gap']:>10.4f}"
        )

    # Monotonicity check
    print()
    print("Forward monotonicity:")
    for key in ["energy", "hamiltonian", "min_gap", "mean_gap", "std_gap"]:
        vals = [h[key] for h in hist_f]
        diffs = np.diff(vals)
        if np.all(diffs >= -1e-9):
            mono = "↑ (non-decreasing)"
        elif np.all(diffs <= 1e-9):
            mono = "↓ (non-increasing)"
        else:
            mono = f"non-monotone (Δrange {np.min(diffs):+.2e}, {np.max(diffs):+.2e})"
        print(f"  {key:>12}: {mono}")

    print("Backward monotonicity:")
    for key in ["energy", "hamiltonian", "min_gap", "mean_gap", "std_gap"]:
        vals = [h[key] for h in hist_b]
        diffs = np.diff(vals)
        if np.all(diffs >= -1e-9):
            mono = "↑ (non-decreasing)"
        elif np.all(diffs <= 1e-9):
            mono = "↓ (non-increasing)"
        else:
            mono = f"non-monotone"
        print(f"  {key:>12}: {mono}")


if __name__ == "__main__":
    main()
