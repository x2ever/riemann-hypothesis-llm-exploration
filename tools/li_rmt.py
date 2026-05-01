"""Compare Li's λ_n (from ζ zeros) with the RMT-GUE prediction.

The aim is a cross-check between two RH-equivalents:
- Li's criterion: λ_n ≥ 0 ⟺ RH.
- RMT/GUE consistency: ζ zeros statistics match GUE eigenvalues.

If RH holds and the RMT model is faithful, then partial-sum λ_n
should fall within the predicted GUE distribution band.

For the GUE side we compute, for each N×N Hermitian matrix M with eigenvalues
{e_k}, the analogous quantity by mapping eigenvalues onto the critical line
via the Keating–Snaith mean-density rescaling. (Heuristic; the precise mapping
of GUE eigenvalues to ζ zeros at height T is via T·log(T/2π)/2π normalization.)

This is exploratory — the comparison is *conceptual* not a known theorem.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import mpmath
import numpy as np


@dataclass
class LiResults:
    """Container for λ_n values from ζ zeros."""

    n_values: list[int]
    lambda_values: list[float]
    n_zeros_used: int
    dps: int


def li_lambda_zeta(
    n_max: int, num_zeros: int, dps: int = 30
) -> LiResults:
    """Compute λ_1..λ_{n_max} from the first num_zeros nontrivial zeros of ζ."""
    mpmath.mp.dps = dps
    zeros = []
    for k in range(1, num_zeros + 1):
        rho = mpmath.zetazero(k)
        zeros.append(complex(rho))
        zeros.append(complex(rho.conjugate()))

    lambdas = []
    for n in range(1, n_max + 1):
        total = 0.0 + 0.0j
        for r in zeros:
            total += 1 - (1 - 1 / r) ** n
        # imaginary parts cancel under conjugation but accumulate roundoff
        lambdas.append(total.real)
    return LiResults(
        n_values=list(range(1, n_max + 1)),
        lambda_values=lambdas,
        n_zeros_used=num_zeros,
        dps=dps,
    )


def gue_eigenvalues(n: int, rng: np.random.Generator) -> np.ndarray:
    """Sample one N×N GUE matrix and return its eigenvalues (sorted, real).

    GUE: H = (A + A†)/2 where A has iid complex N(0, 1/2 + i 1/2) entries
    (so H has variance 1 on diagonal, 1/2 on off-diagonal).
    """
    A = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    H = (A + A.conj().T) / 2
    eigs = np.linalg.eigvalsh(H)
    return eigs


def li_lambda_gue(
    n_max: int,
    matrix_size: int,
    num_samples: int,
    seed: int,
    height_min: float | None = None,
    height_max: float | None = None,
) -> dict[int, np.ndarray]:
    """Compute analogous λ_n for GUE matrices, mapped onto ζ's height range.

    For each sample H ~ GUE(matrix_size) with eigenvalues e_k ∈ [-2√N, 2√N]
    (Wigner semicircle), we map them affinely onto [height_min, height_max]:
        γ_k = height_min + (e_k - e_min) · (height_max - height_min) / (e_max - e_min)
    and treat γ_k as imaginary parts of a "zero" ρ_k = 1/2 + i γ_k.

    This *shifts the GUE bulk away from 0* so the comparison reflects
    local-statistic agreement, not artifactual disagreement from γ ≈ 0.

    If height_min/max is None, fall back to old (naive) normalization.
    """
    rng = np.random.default_rng(seed)
    out = {n: np.zeros(num_samples) for n in range(1, n_max + 1)}
    for s in range(num_samples):
        eigs = gue_eigenvalues(matrix_size, rng)
        if height_min is not None and height_max is not None:
            e_min, e_max = float(eigs[0]), float(eigs[-1])
            gammas = height_min + (eigs - e_min) * (
                (height_max - height_min) / (e_max - e_min)
            )
        else:
            scale = np.sqrt(2 * matrix_size) / np.pi
            gammas = eigs * scale
        rhos = 0.5 + 1j * gammas
        rhos_with_conj = np.concatenate([rhos, rhos.conj()])
        rhos_with_conj = rhos_with_conj[np.abs(rhos_with_conj) > 1e-3]
        for n in range(1, n_max + 1):
            term = 1 - (1 - 1 / rhos_with_conj) ** n
            out[n][s] = float(np.sum(term).real)
    return out


def li_lambda_gue_unfolded(
    n_max: int,
    zeta_heights: list[float],
    matrix_size: int,
    num_samples: int,
    seed: int,
) -> dict[int, np.ndarray]:
    """GUE eigenvalues mapped onto ζ zero positions via the *Riemann–von Mangoldt
    cumulative density*.

    ζ zero density at height t is ~ (1/2π) log(t/2π).  We map GUE eigenvalue
    quantile q (within the Wigner semicircle CDF) onto the ζ zero whose
    cumulative N(t) lands at the same fractional position.  Concretely we
    sort GUE eigvals, then assign γ_k := zeta_heights[k] for k = 0..N-1.
    """
    rng = np.random.default_rng(seed)
    n_zeros = len(zeta_heights)
    out = {n: np.zeros(num_samples) for n in range(1, n_max + 1)}
    for s in range(num_samples):
        eigs = gue_eigenvalues(matrix_size, rng)
        # The k-th eigenvalue (sorted) plays the role of the k-th ζ zero.
        n_use = min(matrix_size, n_zeros)
        # Use rank-based mapping: GUE eigvals → quantile → corresponding zeta height.
        # Simplest version: assign sorted-eigval[k] → zeta_heights[k].
        # The eigval magnitude is *discarded*; we only use the rank.
        # This is a "perfect rigid spectrum" mapping — no fluctuation.
        # Better: keep eigvalue but rescale via cumulative.
        # For comparison we use rank-mapping (deterministic).
        gammas = np.array(zeta_heights[:n_use])
        # Add GUE-driven local fluctuations: take consecutive eigenvalue gaps
        # (normalized by mean GUE gap) and accumulate via the ζ mean spacing:
        #   γ̃_k = γ_k_mean_predicted + ε_k
        # where ε_k uses the GUE eigvalue's deviation from the rigid mean.
        # Simpler proxy: jitter by GUE local spacings vs unit spacing.
        eig_sub = eigs[:n_use]
        mean_e = np.mean(eig_sub)
        std_e = np.std(eig_sub)
        if std_e > 0:
            # Normalized deviation × local mean spacing of ζ
            mean_gap = (gammas[-1] - gammas[0]) / max(n_use - 1, 1)
            jitter = (eig_sub - mean_e) / std_e * (mean_gap / 4)
            # Use rigid γ_k as base + small jitter
            gammas = gammas + jitter
            # Re-sort to keep monotone (avoid pathologies)
            gammas = np.sort(gammas)
        rhos = 0.5 + 1j * gammas
        rhos_with_conj = np.concatenate([rhos, rhos.conj()])
        rhos_with_conj = rhos_with_conj[np.abs(rhos_with_conj) > 1e-3]
        for n in range(1, n_max + 1):
            term = 1 - (1 - 1 / rhos_with_conj) ** n
            out[n][s] = float(np.sum(term).real)
    return out


def main() -> None:
    """CLI: print λ_n from ζ side and GUE distribution side, with z-score."""
    parser = argparse.ArgumentParser(description="Li's λ_n: ζ vs GUE.")
    parser.add_argument("--n-max", type=int, default=20)
    parser.add_argument("--zeros", type=int, default=100)
    parser.add_argument("--matrix-size", type=int, default=100)
    parser.add_argument("--samples", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dps", type=int, default=30)
    parser.add_argument(
        "--mode",
        choices=["naive", "affine", "rank"],
        default="affine",
        help="GUE eigenvalue → ζ height mapping",
    )
    args = parser.parse_args()

    print(f"Computing λ_n from first {args.zeros} ζ zeros at dps={args.dps}...")
    zeta_res = li_lambda_zeta(args.n_max, args.zeros, args.dps)

    # Use the actual ζ zero heights for GUE-rank mapping (run #3).
    mpmath.mp.dps = args.dps
    zeta_heights = [
        float(mpmath.zetazero(k).imag) for k in range(1, args.zeros + 1)
    ]
    h_min = zeta_heights[0]
    h_max = zeta_heights[-1]

    print(
        f"Sampling {args.samples} GUE matrices of size {args.matrix_size} "
        f"(seed={args.seed})..."
    )

    if args.mode == "affine":
        print(f"Mode: affine height [{h_min:.3f}, {h_max:.3f}]")
        gue_res = li_lambda_gue(
            args.n_max,
            args.matrix_size,
            args.samples,
            args.seed,
            height_min=h_min,
            height_max=h_max,
        )
    elif args.mode == "rank":
        print(
            f"Mode: rank-mapping (rigid ζ heights + GUE-driven local jitter)"
        )
        gue_res = li_lambda_gue_unfolded(
            args.n_max,
            zeta_heights,
            args.matrix_size,
            args.samples,
            args.seed,
        )
    else:
        print(f"Mode: naive (no shift)")
        gue_res = li_lambda_gue(
            args.n_max, args.matrix_size, args.samples, args.seed
        )

    print()
    print(
        f"{'n':>4} {'λ_n (ζ)':>15} {'GUE mean':>15} {'GUE std':>15} "
        f"{'z-score':>10} {'sign(ζ)':>8}"
    )
    print("-" * 72)
    z_scores = []
    for n in range(1, args.n_max + 1):
        lam_z = zeta_res.lambda_values[n - 1]
        gue_arr = gue_res[n]
        mu = float(np.mean(gue_arr))
        sigma = float(np.std(gue_arr, ddof=1))
        z = (lam_z - mu) / sigma if sigma > 0 else float("nan")
        z_scores.append(z)
        sign = "+" if lam_z > 0 else ("0" if lam_z == 0 else "-")
        print(
            f"{n:>4} {lam_z:>15.6f} {mu:>15.6f} {sigma:>15.6f} "
            f"{z:>10.3f} {sign:>8}"
        )
    print()
    print(
        f"Median |z| = {np.median(np.abs(z_scores)):.3f},  "
        f"max |z| = {np.max(np.abs(z_scores)):.3f}"
    )
    print(
        "주의: GUE rescaling 은 heuristic (Keating–Snaith bulk density). "
        "z 가 *상수* 분포면 truncation bias, *systematic* 추세면 본질적 차이 신호."
    )


if __name__ == "__main__":
    main()
