# Work — Attempt 176 (Connes-Consani 2021 §2.1 *Concrete QW_λ Spectral Form* DEEP)

## Cut self-check
Cut 6: paper-direct deeper. cut X.

## Connes-Consani 2021 §2.1 paper-direct (page 9-15)

attempt 111 §1-§2 deep follow-up.

### §2.1.1 Weil Distributions (paper-direct eq 2.3-2.7)

**Non-archimedean** (eq 2.3):
$$\mathcal W_p(f) := (\log p) \sum_{m=1}^\infty (f(p^m) + f^\sharp(p^m))$$

**Archimedean** (eq 2.4):
$$\mathcal W_\mathbb R(f) := (\log 4\pi + \gamma) f(1) + \int_1^\infty \left(f(x) + f^\sharp(x) - \frac{2}{x}f(1)\right) \frac{dx}{x - x^{-1}}$$

After Mellin → Fourier translation (eq 2.6, 2.7):
$$W_p(F) = (\log p) \sum_{m=1}^\infty p^{-m/2} (F(p^m) + F(p^{-m}))$$
$$W_\mathbb R(F) = (\log 4\pi + \gamma) F(1) + \int_1^\infty (F(x) + F(x^{-1}) - 2 x^{-1/2} F(1)) \frac{x^{1/2}}{x - x^{-1}} d^*x$$

→ paper-direct: paper §2.1.1 = **paper-direct Master Generator (Weil 1948 eq 9.5 attempt 172) explicit form**.

### §2.1.2 Semi-local Weil Quadratic Form (paper-direct eq 2.8-2.10)

(eq 2.8):
$$QW(f, g) = \psi(f^* * g), \quad \psi(F) := \hat F(i/2) + \hat F(-i/2) - W_\mathbb R(F) - \sum_p W_p(F)$$

(eq 2.9): W_∞(F) = ∫ |F̂(t)|² 2 ∂_t θ(t)/(2π) dt.
(eq 2.10): θ(t) = -(t/2) log π + Im log Γ(1/4 + it/2) — **Riemann-Siegel angular function**.

### Proposition 2.1 (paper-direct eq 2.11) — *concrete QW_λ form*

For λ > 1:
$$QW_\lambda(f, f) = \int |\hat f(t)|^2 \frac{2 \partial_t \theta(t)}{2\pi} dt + 2 \Re(\hat f(i/2) \overline{\hat f(-i/2)}) - \sum_{1 \le n \le \lambda^2} \Lambda(n) \langle f | V(n) f \rangle$$

(eq 2.12): ⟨f | V(n) g⟩ = n^{-1/2} ((f* * g)(n) + (f* * g)(n^{-1})).

→ paper-direct **concrete computable form** of QW_λ.
- 1st term: Q_∞ via θ Riemann-Siegel.
- 2nd term: pole contributions (s = 0, 1).
- 3rd term: prime contributions Σ Λ(n) over n ≤ λ².

### §2.1.3 Real basis (paper-direct eq 2.21)

$$\xi_n(x) = (-1)^n \sqrt{2/L} \cos(2\pi n x/L), \quad n > 0$$
$$\xi_n(x) = (-1)^n \sqrt{2/L} \sin(2\pi n x/L), \quad n < 0$$
$$\xi_0(x) = L^{-1/2}$$

L = 2 log λ.

### Lemma 2.6 (paper-direct page 15) — *6-case σ matrix*

η_n(u) = ξ_n(log u). σ(n, m) = QW(η_n, η_m).

paper-direct **6-case explicit table** (paper page 15):

| (m, n) | (n>0) | (n=0) | (n<0) |
|---|---|---|---|
| m>0, n≠m | n sin(2πmy/L) - m sin(2πny/L) ... | -sin(2πmy/L) ... | 0 |
| m=n>0 | (L-y)/L cos(2πny/L) - sin(2πny/L)/(2πn) | ∅ | ∅ |
| m=0 | -sin(2πny/L)/(√2 πn) | (L-y)/L | 0 |
| m<0, n≠m | 0 | 0 | -m sin(2πny/L)+n sin(2πmy/L) |
| m=n<0 | ∅ | ∅ | sin(2πny/L)/(2πn) + (L-y)/L cos(2πny/L) |

→ paper-direct **explicit matrix form** of QW_λ on basis ξ_n.

### σ split σ = σ^+ ⊕ σ^- (paper §2.1.3 끝)

σ(n, m) = 0 for n ≥ 0, m < 0 (Lemma 2.6 (ii)).

→ QW_λ = QW_λ^+ ⊕ QW_λ^- (even/odd parts).

paper-direct: paper §2.5 의 λ²=11 smallest positive eigenvalue 2.389×10^-48 = *σ^+ smallest eigenvalue*.

## *Master Generator* paper-direct verification (attempt 172 → 176)

paper-direct: 
- attempt 172: Lagarias §9 Appendix Master Generator T[f] = f̂(0) - W[f] + f̂(1) = Σ_v W_v(f).
- 본 attempt 176: Connes-Consani §2.1 = paper-direct *same Master Generator*.

paper-direct **psi(F) form** (Connes-Consani eq 2.8):
$$\psi(F) := \hat F(i/2) + \hat F(-i/2) - W_\mathbb R(F) - \sum_p W_p(F)$$

→ Lagarias §9 T[f] = f̂(0) - W[f] + f̂(1)에서:
- f̂(0) ↔ F̂(-i/2) (paper §2.1.2 eq 2.9 의 *zero side at s=0*).
- f̂(1) ↔ F̂(i/2) (s=1).
- W[f] ↔ W_ℝ(F) + Σ_p W_p(F).

→ paper-direct *동일 Master Generator 의 다른 좌표 변환* (Mellin vs Fourier).

## *Tissue 23 NEW*: Connes-Consani §2.1 ψ(F) ↔ Lagarias §9 T[f]

paper-direct **Tissue 23**: Connes-Consani 2021 §2.1 ψ(F) = Lagarias-Li §9 Appendix T[f]:
- ψ(F) = F̂(i/2) + F̂(-i/2) - W_ℝ(F) - Σ_p W_p(F).
- T[f] = f̂(0) - W[f] + f̂(1) = Σ_v W_v(f).
- Mellin transform 좌표 변환 만 다름.

mapped 23/19 (Tissue 23 cross-class).

## *Wall #1 paper-direct quantitative concrete form*

paper-direct: Connes-Consani §2.1 = **Wall #1 paper-direct concrete computable form**:
- 6-case σ matrix explicit (paper Lemma 2.6).
- *number field* 측 explicit *basis representation*.
- Function field side *trivially polynomial w = q^{-s}* (Lagarias §8 (2)) — number field 측 *infinite series* but *concrete*.

→ paper-direct: Wall #1 의 *number field 측 concrete form* paper-direct.

## Lemma 적용

### Lemma 3 evidence (10 Connes-Consani) 강화
- attempt 111 (§1-§2 light) + 176 (§2.1 deep).
- *concrete spectral form* paper-direct.
- *Master Generator paper-direct verification*.

### Lemma 7 Anchoring (3 NEW quotes)
- Connes-Consani §2.1.1 eq (2.4): W_ℝ(f) = (log 4π + γ) f(1) + ...
- Connes-Consani Proposition 2.1 eq (2.11): QW_λ explicit.
- Connes-Consani Lemma 2.6: 6-case σ matrix.
- catalog 36 → 39 quotes.

## Honest scope
*novel content X*. Connes-Consani §2.1 paper-direct deep + Tissue 23 (ψ(F) ↔ T[f]) + Wall #1 concrete form + Master Generator double verification.
