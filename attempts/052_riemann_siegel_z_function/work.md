# Work — Attempt 052 (Z(t) sanity)

[numerical, dps=30]

## Z(t) at zeros (numerical zero confirmation)
첫 10 zeros: |Z(t_k)| ~ 10^{-15} (machine precision).

## Z(t) at midpoints (sign alternation)
모두 nonzero, 부호 alternation:
- midpoint 1-2: +2.32
- midpoint 2-3: -1.46
- midpoint 3-4: +2.85
- midpoint 4-5: -0.93
- ...

## 분석 (suppressed confidence)

[rigorous]:
- Hardy function $Z(t) = e^{i\theta(t)}\zeta(1/2+it)$ real for real t.
- Z(t_k) = 0 at zeros (Hardy 1914 → 무한 zeros on critical line).
- Sign alternation between consecutive zeros.

[증명 X]:
- 알려진 fact (Hardy, Riemann-Siegel)의 mpmath sanity check.
- *우리 contribution 0*.
- yellow flag word 회피.

## "예상 가능 결과" self-check
yes — paper-direct sanity.
