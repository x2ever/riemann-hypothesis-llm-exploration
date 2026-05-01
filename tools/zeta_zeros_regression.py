"""γ_n linear regression — paper-direct N(T) inverse + residuals."""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


def main() -> None:
    print("=== γ_n linear regression (NOVEL) ===\n")

    N = 200
    gammas = np.array([float(mp.zetazero(n).imag) for n in range(1, N + 1)])
    n_arr = np.arange(1, N + 1)

    log_gamma_2pi = np.log(gammas / (2 * math.pi))
    paper_predict = (gammas / (2 * math.pi)) * (log_gamma_2pi - 1) + 7 / 8
    print(f"Riemann-von Mangoldt: n ≈ (γ_n/(2π))(log(γ_n/(2π))-1) + 7/8")
    print(f"Mean |n - paper_predict|: {np.mean(np.abs(n_arr - paper_predict)):.4f}")
    print(f"Max |n - paper_predict|: {np.max(np.abs(n_arr - paper_predict)):.4f}")

    print("\n--- Inverse: solve for γ_n given n ---")
    def estimate_gamma(n_val: int) -> float:
        approx = 14.0 + 6 * n_val
        for _ in range(30):
            ratio = approx / (2 * math.pi)
            if ratio < 1:
                approx = 2 * math.pi * 1.5
                continue
            f = ratio * (math.log(ratio) - 1) + 7 / 8 - n_val
            df = (1 / (2 * math.pi)) * math.log(ratio)
            if abs(df) < 1e-10:
                break
            approx -= f / df
            if approx < 14:
                approx = 14.0
        return approx

    estimates = np.array([estimate_gamma(int(n)) for n in n_arr])
    residuals = gammas - estimates
    print(f"Residual stats: mean={np.mean(residuals):.4f}, std={np.std(residuals):.4f}")
    print(f"Max |residual|: {np.max(np.abs(residuals)):.4f}")

    print("\n--- Residual S(γ_n) approximation ---")
    print("paper-direct: γ_n - ⟨γ_n⟩ = π S(γ_n) (small fluctuation).")
    S_n = residuals * math.pi
    print(f"S(γ_n) approx values:")
    for i in range(0, 30, 3):
        print(f"  n={i+1:3d}, γ_n={gammas[i]:8.4f}, residual={residuals[i]:+.4f}, S(γ_n)≈{S_n[i]:+.4f}")

    autocorr = np.corrcoef(residuals[:-1], residuals[1:])[0, 1]
    print(f"\nResidual autocorrelation (lag 1): {autocorr:.4f}")
    print("paper-direct: S(γ_n) is small *prime-driven* fluctuation.")


if __name__ == "__main__":
    main()
