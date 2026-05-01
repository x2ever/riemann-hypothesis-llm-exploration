"""Generic cross-check framework for two RH-related quantities.

Inspired by tools/li_rmt.py (attempt 001).  The pattern observed:
- One quantity computed from ζ zeros (deterministic).
- Another quantity from a model (RMT/GUE samples, or a candidate equivalent).
- Compare via z-score across multiple normalization modes.

Three normalization modes (from attempt 001):
  - "naive": no rescaling.
  - "affine": linear map of model values onto [min, max] of ζ-side.
  - "rank": rank-mapping (rigid ζ values + small model-driven jitter).

Discrepancy interpretation:
  - z constant across n   ⇒ truncation / multiplicative offset.
  - z systematic in n     ⇒ structural mismatch (Wall #6: LOCAL-GLOBAL-MISMATCH).

Limitation: the framework works for quantities indexable by an integer n
(λ_n, σ(n), I_k(T) for integer k, etc.).  Continuous quantities need adaptation.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class CrossCheckResult:
    """Output of a cross-check run."""

    n_values: list[int]
    zeta_values: list[float]
    model_means: list[float]
    model_stds: list[float]
    z_scores: list[float]
    mode: str

    def median_abs_z(self) -> float:
        return float(np.median(np.abs(self.z_scores)))

    def max_abs_z(self) -> float:
        return float(np.max(np.abs(self.z_scores)))

    def diagnose(self) -> str:
        """Heuristic interpretation of z-score pattern."""
        z = np.array(self.z_scores)
        if np.median(np.abs(z)) < 1.5:
            return "PASS (within 1.5 sigma — no detected mismatch)"
        if np.std(z) < 0.3 * np.mean(np.abs(z)):
            return "OFFSET (systematic multiplicative — try affine normalization)"
        if np.std(z) > 0.5 * np.mean(np.abs(z)):
            return "STRUCTURAL (z non-constant in n — possible LOCAL-GLOBAL-MISMATCH; Wall #6)"
        return "AMBIGUOUS (refine sample size or normalization)"


def cross_check(
    n_values: list[int],
    zeta_fn,  # callable: int -> float
    model_fn,  # callable: int, sample_idx -> float; or returns dict[int, list[float]]
    num_samples: int,
    mode: str = "naive",
) -> CrossCheckResult:
    """Run a cross-check.

    Args:
        n_values: indices to compare (e.g., [1, 2, ..., 20]).
        zeta_fn: deterministic function returning the ζ-side value at n.
        model_fn: either:
            (a) callable(n, sample_idx) -> float for sample-by-sample,
            (b) callable(n_values, num_samples) -> dict[int, np.ndarray] (vectorized).
            We try (b) first, fall back to (a).
        num_samples: number of model samples for mean/std.
        mode: "naive" / "affine" / "rank" — passed through to model_fn metadata.

    Returns CrossCheckResult.
    """
    zeta_vals = [zeta_fn(n) for n in n_values]

    # Try vectorized form first.
    try:
        model_dict = model_fn(n_values, num_samples)
        model_arrays = [np.asarray(model_dict[n]) for n in n_values]
    except TypeError:
        model_arrays = []
        for n in n_values:
            arr = np.array([model_fn(n, s) for s in range(num_samples)])
            model_arrays.append(arr)

    means = [float(np.mean(a)) for a in model_arrays]
    stds = [float(np.std(a, ddof=1)) for a in model_arrays]
    z_scores = []
    for v, m, s in zip(zeta_vals, means, stds):
        z_scores.append((v - m) / s if s > 0 else float("nan"))

    return CrossCheckResult(
        n_values=list(n_values),
        zeta_values=zeta_vals,
        model_means=means,
        model_stds=stds,
        z_scores=z_scores,
        mode=mode,
    )


def print_result(result: CrossCheckResult, label_zeta: str = "ζ", label_model: str = "model") -> None:
    """Pretty-print a CrossCheckResult."""
    print(f"Mode: {result.mode}")
    print(
        f"{'n':>4} {label_zeta+' value':>18} {label_model+' mean':>18} "
        f"{label_model+' std':>15} {'z-score':>10}"
    )
    print("-" * 70)
    for n, v, m, s, z in zip(
        result.n_values,
        result.zeta_values,
        result.model_means,
        result.model_stds,
        result.z_scores,
    ):
        print(f"{n:>4} {v:>18.6f} {m:>18.6f} {s:>15.6f} {z:>10.3f}")
    print("-" * 70)
    print(f"Median |z| = {result.median_abs_z():.3f}, Max |z| = {result.max_abs_z():.3f}")
    print(f"Diagnosis: {result.diagnose()}")


# Smoke test (when run directly)
if __name__ == "__main__":
    # Synthetic: ζ-side = sin(n); model = sin(n) + small noise. Should be PASS.
    rng = np.random.default_rng(0)

    def zeta_synth(n: int) -> float:
        return np.sin(n)

    def model_synth(ns, k):
        return {n: np.sin(n) + 0.1 * rng.standard_normal(k) for n in ns}

    res = cross_check(list(range(1, 11)), zeta_synth, model_synth, 100, mode="naive")
    print_result(res, "synth-ζ", "synth-model")
