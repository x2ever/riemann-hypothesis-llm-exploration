# Attempt 132: Platt-Trudgian 2021 Numerical RH up to 3×10^12 DEEP
**Type**: A (Mode A deep, 8 components)

## Cut self-check
- 본 paper = numerical RH bound. cut X (paper-direct mapping).

## DoD
- Theorem 1: RH true up to H = 3,000,175,332,800. 12,363,153,437,138 lowest zeros.
- §2 algorithm: Turing's method + Arb interval arithmetic + Riemann-Siegel.
- 7.5 million core hours, 3.6 GHz Xeon, NCI Raijin/Gadi clusters.
- §3.1 Bounds on primes: Schoenfeld 1976 |ψ(x)-x| ≤ (1/8π) x^{1/2} log² x. Corollary 1 range x ≤ 2.169×10^25.
- §3.2 Zero-free regions: Mossinghoff-Trudgian R=5.573.
- §3.4 *de Bruijn-Newman constant Λ ≤ 0.2* (Polymath15 §6 → Corollary 2 with H > 2.51×10^12).
- Wall #2 quantitative bracket update: 0 ≤ Λ ≤ 0.2 (vs Λ ≤ 0.22).
- paper-direct historical context (Wedeniwski, Gourdon, Franke).
- Specialist Δ.
