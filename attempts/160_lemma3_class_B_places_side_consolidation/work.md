# Work — Attempt 160 (Lemma 3 Class B Places Side Consolidation)

## Cut self-check
Type C: Lemma 3 Class B consolidation.

## Class B — 6 places-side evidence (attempt 137)

paper-direct *historical chain*:

```
1859 Riemann Euler product log ζ = -Σ log(1-p^{-s}) (attempt 143 originating)
  ↓
1837 Dirichlet primes in arithmetic progressions
  ↓
1948 Tate's thesis adelic
  ↓
1999 Connes adelic L²(X) trace formula
  ↓
{Pratt-Robles 2019, Connes-Consani 2021, Lagarias §6 2004, Robin 2002}
```

## 6 evidence consolidation

### 6. **Pratt-Robles §6 A^{(1,1)}** (attempt 104)
$$A^{(1,1)}_{0,0}(0,0;0,0) = -\sum_p \left(\frac{\log p}{p-1}\right)^2 \approx -1.385604$$
mollifier arithmetic factor.

### 8. **Polymath15 H_t Newman positivity** (attempt 106)
$$H_t(z) = \int_0^\infty e^{tu^2} \Phi(u) \cos(zu) du, \quad \Phi(u) = \sum_n (2\pi^2 n^4 e^{9u} - 3\pi^2 n^2 e^{5u}) e^{-\pi n^2 e^{4u}}$$
primes implicit via Φ super-exp decay.
RH ⟺ Λ ≤ 0 ⟺ all H_t zeros real.

### 9. **Connes 1999 §VI** (attempt 108)
$$\text{Trace } U(h) = \sum_v \int_{k_v^*} \frac{h(u^{-1})}{|1-u|} d^*u$$
all places sum (archimedean + finite primes).
RH ⟺ h(u) ≥ 0 ⟹ RHS positive.

### 10. **Connes-Consani 2021 §1 QW_λ** (attempt 111)
$$QW(f, g) = \sum_{1/2 + is \in Z} \tilde f(s) \hat g(s)$$
semi-local restricted to primes p < λ².
RH ⟺ QW_λ positive ∀λ.

### 15. **Lagarias §6 S_f** (attempt 116)
$$S_f(n, \pi) = \lambda_n(\sqrt n, \pi^\vee) + O(\sqrt n \log n)$$
RH ⟹ λ_n(√n) = O(√n log n).
*kernel k_n(s) contour integral* (paper §6 eq 6.4-6.13).

### 18. **Robin/Lagarias 2002** (attempt 122)
$$\sigma(n) \le H_n + \exp(H_n) \log H_n \quad \forall n \iff RH$$
divisor function bound.

## *Class B internal isomorphism* (paper-direct connective tissue)

### Tissue 2 (attempt 137): Bombieri-Lagarias λ_n positivity ↔ Connes §VI eq (17) h(u) ≥ 0
- *positivity criterion*, 다른 좌표.

### Tissue 4 (attempt 139): Pratt-Robles ↔ Connes-Consani QW_λ
- *prime-by-prime sensitivity*, p=2 dominant.
- mollifier arithmetic vs quadratic form positivity.

### Tissue 11 (attempt 151): Hardy-Littlewood ↔ Voros η ↔ Lagarias η
- η_j = (-1)^j/j! Σ Λ(m)(log m)^j/m.
- *Stieltjes cumulants over primes*.

### Tissue 12 (attempt 152): Robin σ(n) ↔ Connes-Consani QW_λ
- *same Class B places-side*, *different aggregation*.

### Tissue 13 (attempt 153): Lagarias η_j 3-tier (Hardy-Littlewood ↔ Voros ↔ Lagarias)
- *unified arithmetic Stieltjes cumulants*.

## *Class B 의 paper-direct unification*

6 evidence 모두 *Riemann 1859 Euler product* 의 generalization:
1. Riemann 1859: log ζ = -Σ log(1-p^{-s}) primes side.
2. Pratt-Robles §6: prime sum (log p/(p-1))² engineering.
3. Connes 1999 §VI: adelic Σ_v ∫_{k_v*}.
4. Connes-Consani 2021: semi-local QW_λ semi-local.
5. Lagarias §6: contour integral kernel + L'/L Lemma 6.1.
6. Robin: σ(n) divisor multiplicative.

→ paper-direct: Class B *unified via Riemann's Euler product 1859 + Tate's thesis 1948 adelic*.

## Lemma 3 Class A + Class B consolidation summary

Class A (10 evidence) → Riemann 1859 Hadamard product unification.
Class B (6 evidence) → Riemann 1859 Euler product unification.

→ paper-direct: **Lemma 3 19 evidence = Riemann 1859 originating chain (attempt 143) + Lagarias §4 eq (4.10) Class A ↔ Class B identity (attempt 156)**.

## Honest scope
*novel content X*. Class B 6 evidence consolidation + Riemann 1859 Euler product unification.
