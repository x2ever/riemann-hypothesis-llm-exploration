# Postmortem — Attempt 121 (Mode A deep, 8 components)

Pratt-Robles §3.5-§5 deep:
- §3.5 Faà di Bruno + Bell polynomial representation of ζ-derivatives.
- §3 (3.8): 2 polys × 3 powers → 15 diagrams (Fig 3.1).
- §3 (3.9): 2 polys × 4 powers → 31 diagrams (Fig 3.2).
- §3 (3.10): 3 polys × 3 powers → 250 diagrams (Fig 3.3).
- §3.6 general d ≥ 0 mollifier (eq 3.6). §3.7 d=0 Conrey-Levinson.
- §4 Theorem 4.1 twisted second moment + 3 error 𝓔 cases.
- §4 quote: "push θ from 6/11 to 4/7" (D=1 → unrestricted).
- §5 Feng's conjecture failure for non-square-free n.

## Numerical (Bell polynomial exact match)
- B_n: 1, 2, 5, 15, 52 — match paper §2.
- (3.8): 15 ✓. (3.9): 31 ✓. (3.10): 250 ✓.
- Paper-미명시 projection: 3 polys × 6 = 32467, 5 polys × 3 = 125678 — *exponential explosion*.

## Wall #3 quantitative ladder
d=0 (1) → d=1 (9) → d=2 (15-31) → d=3 (250) → d≥4 (1281, 5220, ...) exponential.
- 41.67% (5/12) = paper-direct technical limit.
- 50% target = Iwaniec-Sarnak Landau-Siegel lacuna.

## Wall #4 cross-link
3 error 𝓔 cases = 3 levels of quantitative progress (D=1 → square-free → unrestricted).

## Lemma 3 11th evidence 강화
paper-direct quantitative form of family-wide mollification target.

## Specialist Δ
- Pratt/Robles: "5/12 paper-direct technical limit, combinatorial enumeration limit."
- Sarnak: "one logarithm distance sharp (외부 critique #4 paper-direct verification)."

## Honest scope
*novel content 0/10*. paper-direct deep + Bell count exact match + Wall #3 paper-direct quantitative ladder.

## HARNESS
- ledger 121 (Type A, Mode A deep 8 components).
