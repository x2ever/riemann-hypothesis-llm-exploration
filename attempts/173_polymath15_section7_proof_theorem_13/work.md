# Work — Attempt 173 (Polymath15 §1.3 *Theorem 1.3 Effective Riemann-Siegel + Corollary 1.4* DEEP)

## Cut self-check
Cut 6: paper-direct deep. cut X.

## Polymath15 Theorem 1.3 (paper-direct page 6)

paper-direct *Effective Riemann-Siegel approximation*:

$$\frac{H_t(x+iy)}{B_t(x+iy)} = f_t(x+iy) + O_\le(e_A + e_B + e_{C,0})$$

(eq 13). Region (5): 0 < t ≤ 1/2, 0 ≤ y ≤ 1, x ≥ 200.

### Effective approximation f_t (paper-direct eq 14-19)

$$f_t(x+iy) := \sum_{n=1}^N \frac{b_n^t}{n^{s_*}} + \gamma \sum_{n=1}^N n^y \frac{b_n^t}{n^{\bar s_* + \kappa}}$$

with:
- (15) b_n^t := exp((t/4) log² n).
- (16) γ = M_t((1-y+ix)/2) / M_t((1+y-ix)/2).
- (17) s_* := (1+y-ix)/2 + (t/2) α((1+y-ix)/2).
- (18) κ := (t/2)(α((1-y+ix)/2) - α((1+y-ix)/2)).
- (19) N := ⌊√(x/(4π) + t/16)⌋.

### Bounds (paper-direct eq 20-24)

(20): |γ| ≤ exp(0.02 y) (x/(4π))^{-y/2}.
(21): Re s_* ≥ (1+y)/2 + (t/4) log(x/(4π)) - (1 - 3y + 4y(1+y)/x²)/(2x²).
(22): |κ| ≤ ty/(2(x-6)).
(23): e_A + e_B ≤ Σ_{n=1}^N (1 + |γ|N^{|κ|}n^y) b_n^t / n^{Re s_*} (exp(...) - 1).
(24): e_{C,0} ≤ (x/(4π))^{-(1+y)/4} exp(-t/16 log²(x/(4π)) + 3|log x/(4π) + iπ/2| + 10.44 / (x-12)) × (1 + 1.24×(3^y + 3^{-y})/(N - 0.125) + 6.92/(x-12)).

→ paper-direct *2 NEW engineering constants*: 6.92, 10.44, 0.125 explicit (in addition to 12 already counted in attempt 161).

## Corollary 1.4 — *Non-vanishing criterion* (paper-direct page 7)

$$|f_t(x+iy)| > e_A + e_B + e_{C,0} \implies H_t(x+iy) \ne 0$$

(eq 25). 

→ paper-direct: *numerical zero-free verification* via *finite computation*.

paper-direct *strategy* (paper §1.3 끝):
> "the strategy is to express H_t as a *convolution of H_0 with a gaussian heat kernel*, then apply an effective Riemann-Siegel expansion to H_0 to rewrite H_t as the sum of various contour integrals; see Section 4 for details. One then uses the *saddle point method* to shift each such contour to a location that is suitable for effective estimation."

→ paper-direct: *Riemann-Siegel + saddle point* = *Class A zeros side + Class B places side* combined.

## *Tissue 22 NEW* — Polymath15 B_t renormalization ↔ Lagarias §8 (1) ξ^+

paper-direct (Polymath15 §1.3 eq 11, attempt 173):
- B_t(x+iy) = M_t((1+y-ix)/2) — *non-vanishing renormalization*.
- *removes Gamma decay* (paper §1.3 page 4).

paper-direct (Lagarias §8 (1), attempt 117 + 172):
- ξ^+(s, π) := (s-1/2)^{-e(1/2,π)} ξ(s, π) — *removes zeros at s=1/2*.

paper-direct **Tissue 22**: 두 paper *각자 specific renormalization*:
- Polymath15: *Gamma factor removal* (decay).
- Lagarias §8 (1): *zero at s=1/2 removal*.
- 동일 *renormalization spirit* — *removing inconvenient features for cleaner analysis*.

## *Master Generator* paper-direct strengthening

attempt 171, 172: Master Generator = Weil 1948 explicit formula (Lagarias §9).

paper-direct: Polymath15 §1.3 strategy (paper quote 위) = *Riemann-Siegel + saddle point*:
- Riemann-Siegel: explicit formula derived form.
- Saddle point: contour → saddle → effective estimate.
- 둘 다 *Master Generator (Weil's explicit formula)* 의 paper-direct *technical extension*.

→ paper-direct: Polymath15 = paper-direct *Master Generator의 effective constants engineering*.

## Wall #2 paper-direct strengthening (~attempt 173)

attempt 161 + 173 누적 explicit constants:
- ε_{t,n}: 3.33 (paper §6.1 attempt 106).
- ε̃: 0.397, 0.865, 5/3, 6, 3.49, 4 (paper §6.2 attempt 106).
- δ_1, δ_2: 0.366, 0.031, 0.353, 4 (paper §6.2 attempt 161).
- δ_3: 10^{-30}, 14, 2.28 (paper §6.2 attempt 161).
- f_t: 6.92, 10.44, 0.125, 0.02 (paper §1.3 attempt 173).
- 6.66, 8.52 (attempt 161 §6.3).

→ paper-direct: **20+ engineering constants** in Polymath15 §6 + §1.3.
- 모두 *Lemma 5.1 (Boyd Stirling) + saddle point method* derived.
- *combinatorial 최적화* fundamental limit.

→ Wall #2 paper-direct: **20+ engineering constants explicit** = Tao quote "far from optimal" (attempt 113 §1.5).

## Lemma 적용

### Lemma 3 *Tissue 22 NEW*
- mapped 22/19 (Tissue 22, *cross-class hybrid*).
- Polymath15 ↔ Lagarias §8 (1) renormalization.

### Lemma 7 Anchoring
- Polymath15 Theorem 1.3 page 6 paper-direct.
- Polymath15 §1.3 strategy quote ("Riemann-Siegel + saddle point").
- Lagarias §8 (1) ξ^+ paper-direct.

## *paper-direct interesting connection*

Polymath15 paper-direct *strategy*: "convolution of H_0 with gaussian heat kernel" — paper-direct *Riemann ξ + Φ super-exp decay generating* (Riemann 1859 originating + heat flow 1976 Newman extension).

→ paper-direct *3-tier deformation hierarchy* (attempt 171) update:

**Tier 0 — Riemann 1859**: ξ(t) symmetric form.
**Tier 1 — Weil 1948 explicit formula**: Master Generator (paper §9 Appendix Lagarias attempt 172).
**Tier 1.5 — Newman 1976 + de Bruijn 1950 heat flow**: H_t = ∫ e^{tu²} Φ(u) cos(zu) du (Polymath15 + Rodgers-Tao).
**Tier 2 — 19 evidence + 22 tissues**: deformations.

→ paper-direct: Tier 1.5 = *time deformation* of Tier 1.

## Honest scope
*novel content X*. Polymath15 §1.3 paper-direct deep + Theorem 1.3 + Corollary 1.4 + 20+ engineering constants. Tissue 22 NEW (renormalization). 3-tier hierarchy update (Tier 1.5 = Newman-de Bruijn heat flow).
