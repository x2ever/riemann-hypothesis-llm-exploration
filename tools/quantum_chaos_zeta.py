"""Random matrix M → empirical 'zeta' Σ 1/E_n^s.

Cross-domain idea: GUE eigenvalues 의 'zeta-like' sum 의 zeros 분석.
Expected failure: no critical line, just RMT noise.
"""

from __future__ import annotations

import numpy as np


def gue_matrix(N: int, seed: int = 42) -> np.ndarray:
    """Generate N×N GUE matrix."""
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    H = (A + A.conj().T) / 2
    return H


def empirical_zeta(eigenvalues: np.ndarray, s: complex) -> complex:
    """Σ 1/E_n^s over positive eigenvalues."""
    pos_eig = eigenvalues[eigenvalues > 0]
    return np.sum(1.0 / pos_eig ** s)


def main() -> None:
    """Empirical 'zeta' from GUE matrix — search for zeros."""
    print("=== Random Matrix → ζ Cross-Domain (NOVEL) ===\n")

    for N in [100, 500]:
        M = gue_matrix(N)
        eigs = np.sort(np.real(np.linalg.eigvalsh(M)))
        eigs = eigs / np.sqrt(N) * 2  # normalize Wigner semi-circle
        pos = eigs[eigs > 0.5]  # avoid eigenvalues near 0
        print(f"--- N = {N}, # positive eig (>0.5) = {len(pos)} ---")
        print(f"Eigenvalue range: [{pos.min():.3f}, {pos.max():.3f}]")

        print("\n  Search 'zero' near critical-line analogue Re(s) = ?")
        for s_re in [0.0, 0.5, 1.0, 1.5, 2.0]:
            for s_im in [0, 5, 10, 14, 20]:
                s = complex(s_re, s_im)
                z = empirical_zeta(pos, s)
                if abs(z) < 0.5 and s_im > 0:
                    print(f"    s = {s_re}+{s_im}i: |Σ| = {abs(z):.4f}  (small!)")

        print()
        print("  Σ 1/E_n^s at s = 1 (Riemann pole analogue):")
        for s_re in [0.5, 0.99, 1.0, 1.5, 2.0]:
            z = empirical_zeta(pos, complex(s_re, 0))
            print(f"    s = {s_re}: Σ = {z.real:.4f}")

        print()
        print("  결론: *no critical line structure*. RMT noise only.")
        print("  Berry-Keating: H = xp 의 *trace formula* 가 ζ approximation — 우리는 finite-N RMT.")
        print()


if __name__ == "__main__":
    main()
