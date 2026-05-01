"""Li's criterion: RH ⟺ λ_n ≥ 0 for all n ≥ 1.

λ_n := (1/(n-1)!) (d^n/ds^n) [s^(n-1) log ξ(s)] |_{s=1}
     = Σ_ρ [1 - (1 - 1/ρ)^n]   (sum over nontrivial zeros)

이 동치는 Li 1997 이 증명. RH 가 참이라면 λ_n ≥ 0, 양의 정수성은 spectral interpretation 의 단서.

수치 검증: λ_n 을 영점으로부터 계산해 양수임을 확인. 하나라도 음수면 RH 거짓.
(현재 알려진 영점들에 대해 모두 양수임이 확인됨 — RH 가정과 일관.)
"""

from __future__ import annotations

import argparse

import mpmath


def li_lambda_from_zeros(n: int, num_zeros: int = 100, dps: int = 50) -> mpmath.mpf:
    """Compute λ_n using sum over first num_zeros zero pairs.

    λ_n = Σ_ρ [1 - (1 - 1/ρ)^n], summed over ρ and conjugate ρ̄.
    """
    mpmath.mp.dps = dps
    total = mpmath.mpf(0)
    for k in range(1, num_zeros + 1):
        rho = mpmath.zetazero(k)
        # rho and its conjugate contribute symmetrically
        for r in (rho, rho.conjugate()):
            total += 1 - (1 - 1 / r) ** n
    return total.real  # imaginary parts cancel exactly via conjugate pairing


def main() -> None:
    """CLI entry — compute λ_n for n = 1..N from a finite set of zeros."""
    parser = argparse.ArgumentParser(description="Li's criterion λ_n via finite zero sum.")
    parser.add_argument("-N", type=int, default=20, help="Compute λ_1..λ_N (default 20).")
    parser.add_argument("--zeros", type=int, default=100, help="Number of zeros (default 100).")
    parser.add_argument("--dps", type=int, default=50, help="Decimal precision (default 50).")
    args = parser.parse_args()

    print(f"Computing λ_1..λ_{args.N} from first {args.zeros} zeros at {args.dps} dps.")
    print(f"Truncation: real λ_n = sum over *all* zeros; here partial sum only.")
    print(f"{'n':>4} {'λ_n (partial)':>25} {'sign':>8}")
    print("-" * 45)
    for n in range(1, args.N + 1):
        ln = li_lambda_from_zeros(n, args.zeros, args.dps)
        sign = "+" if ln > 0 else ("0" if ln == 0 else "-")
        print(f"{n:>4} {mpmath.nstr(ln, 12):>25} {sign:>8}")
    print()
    print("주의: 유한 zero 합은 *근사*. 진짜 λ_n 은 무한합 — 수렴 추정 필요.")
    print("RH ⟺ λ_n ≥ 0 ∀n. 음수가 발견되면 RH 거짓의 신호.")


if __name__ == "__main__":
    main()
