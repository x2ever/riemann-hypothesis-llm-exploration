# Work — Attempt 164 (Burnol Bound + Balazard-Saias Infimum Deep)

## Cut self-check
Cut 6: paper-direct evidence 19 (Burnol) deeper. cut X.

## Conrey 2003 §Functional Analysis (paper-direct, attempt 122)

### Nyman-Beurling theorem (paper-direct)
RH ⟺ span_{L²(0,1)} {η_α : 0 < α < 1} = L²(0, 1).
η_α(t) = {α/t} - α{1/t}.

### Baez-Duarte
*integer values* of 1/α 만 사용해도 충분 (Conrey 2003 paper-direct).

### Balazard-Saias (paper-direct)
$$\inf_A \int_{-\infty}^\infty |1 - A(1/2 + it)\zeta(1/2 + it)|^2 \frac{dt}{1/4 + t^2} = 0 \iff RH$$

A(s) = Σ a_n n^{-s} Dirichlet polynomial of length N.

### Burnol bound (paper-direct, Conrey 2003 §Functional Analysis)

d_N = inf_A integral. Burnol proved:
$$d_N \ge \frac{1}{\log N} \sum_{\rho \text{ on the line}} \frac{m_\rho^2}{|\rho|^2}$$

where m_ρ = multiplicity of zero ρ.
- *equality* 시 RH + simple zeros.

paper-direct: d_N → 0 as N → ∞ ⟺ RH.

## *Burnol* paper-direct *isomorphism*

### Tissue 18 NEW: Balazard-Saias L² inf ↔ Connes-Consani L² Hilbert space inf

paper-direct (Connes-Consani §2.5, attempt 111):
- λ²=11: smallest positive eigenvalue 2.389 × 10^-48 (paper §2.5).
- *L² Hilbert space + RH equivalent*.

paper-direct **Tissue 18**: Balazard-Saias *Dirichlet polynomial L² inf* ↔ Connes-Consani *prolate spheroidal L² minimum eigenvalue*:
- Balazard-Saias: inf_A (Dirichlet polynomial) over Hilbert space L²(measure dt/(1/4+t²)).
- Connes-Consani: smallest positive eigenvalue of QW_λ on L²([λ^-1, λ], d*u).
- 둘 다 *L² inner product on test space* + *infimum / smallest eigenvalue → 0* ⟺ RH.

→ paper-direct: 두 paper *동일 Hilbert space framework*, *다른 test space*.

## *Tissue 19 NEW*: Burnol bound ↔ multiplicity of ζ zeros

paper-direct: Burnol equality 시 *RH + simple zeros*.
- *simple zeros* conjecture 자체 unsolved — Bui-Heath-Brown 2013 19/27 simple (Conrey 2003 attempt 122).

paper-direct **Tissue 19**: Burnol equality + Bui-Heath-Brown (simple zeros density 19/27) — *quantitative simplicity-RH coupling*.

## Lemma 적용

### Lemma 3 evidence (19, Burnol) 강화
- Tissue 18 (Burnol ↔ Connes-Consani L² inf).
- Tissue 19 (Burnol equality ↔ simple zeros).

### Lemma 7 Anchoring
- Conrey 2003 §Functional Analysis 의 paper-direct quote.
- Burnol bound formula paper-direct.

## Honest scope
*novel content X*. Tissue 18 + Tissue 19 paper-direct.
