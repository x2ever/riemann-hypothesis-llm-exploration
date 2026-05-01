# Work — Attempt 116 (Lagarias §6 Bounds for S_f — RH-Conditional DEEP)

## 1. Paper section deep read

### §6 Setup (paper-direct, eq 6.1)

**Incomplete Li coefficient**:
$$\lambda_n(T, \pi) := \sum_{\rho \in Z(\pi), |\Im(\rho)| \le T} \left(1 - \left(1 - \frac{1}{\rho}\right)^n\right)$$
T = cutoff parameter.

**Theorem 6.1 (paper-direct, eq 6.2)**:
For irreducible cuspidal (unitary) automorphic π on GL(N):
$$S_f(n, \pi) = \lambda_n(\sqrt n, \pi^\vee) + O(\sqrt n \log n)$$
O-constant depends on π.

**RH-conditional bound (eq 6.3)**:
If RH holds for L(s, π):
$$\lambda_n(\sqrt n, \pi^\vee) = O(\sqrt n \log n)$$

→ Combined: S_f(n, π) = O(√n log n) (RH-conditional).

### §6 Proof tactic (paper-direct, eqs 6.4-6.14)

**Kernel function** (eq 6.4):
$$k_n(s) := \left(1 + \frac{1}{s}\right)^n - 1 = \sum_{j=1}^n \binom{n}{j}\left(\frac{1}{s}\right)^j$$

**Contour integral** (eq 6.5):
$$\frac{1}{2\pi i} \int_{C_1} k_n(s) \left(-\frac{L'}{L}(s+1, \pi)\right) ds = \sum_{j=1}^n \binom{n}{j} \eta_{j-1} = S_f(n, \pi)$$
C_1 = small circle around s=0, residue calculation.

**Contour deformation** to rectangular C_2(n):
- Vertical: Re(s) = σ_0 (-3 < σ_0 < -2), σ_1 = 2√n.
- Horizontal: Im(s) = ±T = ±(√n + ε_n), 0 ≤ ε_n ≤ 1.

Residue theorem:
$$I_2(n) = S_f(n, \pi) + \sum_{\rho \in Z(\pi), |\Im(\rho)|<T} \left(\left(1 + \frac{1}{\rho-1}\right)^n - 1\right) + I_2^{triv}(n)$$

Trivial zero contribution: I_2^{triv}(n) = O(1) by eq (6.6).

**Symmetry** (paper §6, ρ ↦ 1 - ρ̄):
$$I_2(n) = S_f(n, \pi) - \lambda_n(T, \pi^\vee) + O(1)$$
(eq 6.7).

**Goal**: I_2(n) = O(√n log n).

### §6 Lemma 6.1 (paper-direct, eq 6.8)

$$\frac{L'}{L}(s, \pi) = \sum_{\{\rho: |\Im(\rho-s)|<1\}} \frac{1}{s - \rho} + O\left(\log \mathfrak q(\pi, s) \frac{L'}{L}(2, \pi)\right)$$
- $\mathfrak q(s, \pi) = Q(\pi) \prod_i (|s + \kappa_i(\pi)| + 3)$ analytic conductor.
- O-constant absolute.
- Standard Dirichlet L-function technique [12, Chap. 15], generalized.
- Ramanujan conjecture for L(s, π) needed for L'/L(2, π) control.

### §6 4 contour segment bounds (paper-direct)

**I_2^(I)** (vertical at σ_1 = 2√n):
- |k_n(s) - 1| ≤ (1 + 1/(2√n))^n ≤ exp(√n/2) < 2^√n.
- |L'/L(s, π)| ≤ C_0 2^{-(σ-2)} (eq 6.10).
- Combined: I_2^(I)(n) = o(1).

**I_2^(II)/I_2^(IV)** (horizontal at T = √n + ε_n):
- |1 + 1/s|^n ≤ ((1 + σ/(σ²+T²))² + 1/(σ²+T²))^{1/2} ≤ 1 + (σ+1)/(σ²+T²) (eq 6.11).
- T² ≥ n, -3 ≤ σ ≤ 3: |k_n(s)| ≤ (1 + 4/(16+n))^n + 1 ≤ e^4 + 1 = O(1).
- |L'/L(s, π)| = O((log T)²) = O((log n)²) (Lemma 6.1).
- Step σ = 3 to σ = 0: |k_n(s+1)+1|/|k_n(s)+1| ≤ e (eq 6.12). geometric decrease.
- O(log n) steps to reach O(1).
- I_2^(II)(n) = O(√n + (log n)³) = O(√n).

**I_2^(III)** (vertical at σ_0, -3 < σ_0 < -2):
- |k_n(s)| = O(1) by eq (6.6) (|1 + 1/(z-1)| < 1 for Re(z) < 1/2).
- |L'/L(s, π)| = O(log(|s|+2)) (Lemma 6.1).
- Length O(√n).
- I_2^(III)(n) = O(√n log n).

**Total**: I_2(n) = O(√n log n).

### §6 |λ_n(√n, π^∨) - λ_n(T, π^∨)| bound (paper-direct)

|T - √n| < 1: O(log n) zeros in interval. Each zero ρ = β + iγ with √n ≤ |γ| < √n + 1:
$$\left|\left(\frac{\rho-1}{\rho}\right)^n\right| \le \left|1 - \frac{\beta}{\beta^2 + \gamma^2}\right|^n \le |1 + 1/n|^{n/2} \le 2$$

→ |λ_n(√n) - λ_n(T)| = O(log n).

Combined: S_f(n, π) = λ_n(T, π^∨) + O(√n log n) = λ_n(√n, π^∨) + O(√n log n).

### §6 RH-conditional bound (eq 6.14)

If RH holds: ρ = 1/2 + iγ, |1 - 1/(ρ-1)| = |ρ/(ρ-1)| = |(-1/2 + iγ)/(1/2 + iγ)| = 1.
- Each zero contributes term of absolute value at most 2 to incomplete Li.
- Zero density Theorem 2.1(4): O(T log T + 1) zeros up to height T.
- λ_n(T, π) = O(T log T + 1) (eq 6.14).

→ λ_n(√n, π^∨) = O(√n log n) (RH-conditional).

### §6 결합 with §5 (Theorem 5.1)

paper §7, §6 결합:
- S_∞ = (N/2) n log n + C_1 n + O(N(K+1)) — unconditional.
- S_f = O(√n log n) — RH-conditional.
- λ_n = S_∞ - S_f + δ ~ (N/2) n log n + C_1 n + O(√n log n) — RH-conditional.

→ paper-direct: λ_n positive for large n, but only RH-conditional.

## 2. Numerical 검증 (Lagarias §6 RH-conditional)

[numerical, dps=30]

paper §6 직접 numerical 시간 한계 — contour integral 직접 X. 우리 도구 검증 가능 부분:

### λ_n(T, π_triv) numerical (incomplete Li)

| n | T = √n | λ_n(T, ζ) (numerical first 50 zeros) | √n log n (predicted upper) |
|---|---|---|---|
| 4 | 2 | 0 (no zeros |γ|<2) | 2.77 |
| 25 | 5 | 0 (γ_1=14 > 5) | 16.09 |
| 200 | 14.14 | partial (γ_1 included) | 74.95 |
| 1000 | 31.62 | small first ~5 zeros | 218.78 |

[계산 시간 다대 — 본 attempt scope 명시 X]

### λ_n full (T → ∞) numerical via 100 zeros (attempt 044/067 cross-ref)

attempt 044 (200 zeros): n=30 sweet spot 0.976. n>50 slow growth.
- paper §6 prediction: O(√n log n).
- attempt 044 numerical: 0.97 < ratio < 1.02. consistent.

paper §5 (S_∞) + §6 (S_f) 결합 numerical: attempt 044 의 0.976 ratio 가 paper-direct *(N/2) n log n + C_1 n* leading + O(√n log n) error 의 *우리 도구 검증*.

## 3. Wall taxonomy mapping

### Wall #6 (LOCAL-GLOBAL-MISMATCH) deep refinement — *paper-direct origin (cont)*

Lagarias §5 + §6 결합:
- §5: S_∞ ~ (N/2) n log n + C_1 n + O(N(K+1)) *unconditional*.
- §6: S_f = λ_n(√n, π^∨) + O(√n log n), *RH-conditional* λ_n(√n) = O(√n log n).
- λ_n = S_∞ - S_f + δ.

→ Wall #6 *paper-direct quantitative*:
- *unconditional* leading order: (N/2) n log n + C_1 n.
- *RH-conditional* error: O(√n log n).
- *unconditional cancellation*: paper-direct *partial*.

→ paper-direct 검증: *우리 wall taxonomy* 의 Wall #6 = *S_∞ - S_f cancellation 의 conditional vs unconditional* 의 paper-direct origin.

### Wall #1 (FROBENIUS-GAP) cross-link — paper-direct

paper §6 의 *Lemma 6.1 (eq 6.8)*: L'/L(s, π) = Σ_ρ 1/(s-ρ) + O(log q(π, s) · L'/L(2, π)).
- *Number field analogue* of *Frobenius eigenvalue trace* (function field 측).
- *Ramanujan conjecture* (L'/L(2, π) bound) 가 Wall #4 cross-link.
- 본 paper §6 가 paper §3 trio (Lefschetz/Frobenius/Rosati) 의 *number field 측 quantitative*.

### Wall #4 (CONSPIRACY) cross-link — Ramanujan conjecture

paper §6 quote (Lemma 6.1 proof):
> "If we know the Ramanujan conjecture holds for L(s, π), then we can control the size of L'/L(2, π) in the remainder term."

→ Wall #4 의 *Ramanujan conjecture cross-link*: paper §6 의 RH-conditional bound 자체가 *Ramanujan conjecture 가정 partial*. *family-wide* form 부분.

## 4. Lemma 적용

### Lemma 3 (positivity_unification) 15th paper-direct evidence

15. **Lagarias §6 Theorem 6.1** (attempt 116): S_f(n, π) = λ_n(√n, π^∨) + O(√n log n). RH-conditional λ_n(√n, π^∨) = O(√n log n). *quantitative S_f side bound*.

→ Lemma 3 의 15th evidence — *quantitative RH-conditional S_f bound*. attempt 115 (S_∞ unconditional) 와 결합 = paper-direct *cancellation* 의 *완성*.

### Lemma 6 (dont_try_directions) Cut 6 paper-direct full quantitative

paper §5 + §6 결합 *Wall #6 paper-direct quantitative*:
- *unconditional* (S_∞): (N/2) n log n + C_1 n + O(N(K+1)).
- *RH-conditional* (S_f): O(√n log n).
- *combined* λ_n: positive for large n, but RH-conditional.

→ Lemma 6 Cut 6 의 paper-direct *quantitative form*: positivity 단독 RH 시도 = *S_f unconditional bound* 시도. paper §6 자체가 *RH 가정* — *unconditional bound 부재* 가 *Wall #6 quantitative origin*.

### Lemma 4 (failed_proof_categories) cross-check
Lagarias §6 = *successful conditional bound*. Lemma 4 N/A.

## 5. Cross-reference

- attempt 044, 067 (li_lambda_extended_n): 200 zeros numerical, n=30 sweet spot.
- attempt 056 (Lagarias §3 deep): Weil scalar product.
- attempt 086 (Lagarias §5 skim): leading order.
- attempt 095 (Lagarias §7 F_π(z)): complex extension.
- attempt 105 (Lagarias §4 deep): τ_n Hurwitz form.
- attempt 115 (Lagarias §5 unconditional): 본 attempt 의 *짝* — S_∞ unconditional + S_f conditional.
- 본 attempt 116 = Lagarias §6 의 paper-direct *RH-conditional S_f bound*.

## 6. Open questions

(Q1) §6 의 *unconditional* S_f bound 가능?
- paper §6 자체: *RH 가정* 만. 그러나 *partial unconditional* 가능?
- *알려진*: zero density estimates (zero-free region) 가 partial unconditional bound 줄 수 있음.
- *우리 contribution X*: paper §6 자체 scope 만.

(Q2) §6 Lemma 6.1 의 *Ramanujan conjecture-free* form?
- paper-direct: Ramanujan 가정 부재 시 L'/L(2, π) bound 다대.
- automorphic L(s, π): GL(2) 까지 *부분 known*. GL(N) 일반은 *open*.

(Q3) 결합 λ_n asymptotic 의 *unconditional* 부분 / *conditional* 부분 sharper distinction?
- §5 (unconditional) leading + §6 (conditional) error.
- *우리 wall taxonomy* 의 Wall #6 의 paper-direct *quantitative form*.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Lagarias §6 paper-direct deep + §5 + §6 결합 paper-direct *Wall #6 quantitative form* + Lemma 3 15th evidence.
- *우리 contribution*: paper-direct mapping + paper §5 + §6 결합 *cancellation 의 paper-direct quantitative form* + Lemma 6 Cut 6 의 *quantitative form* 명시.

## 8. Specialist Δ 추정 (Lagarias 본인)

### Lagarias 본인 추정
- "Lagarias-Li 2004 §6 = *RH-conditional* technical bound. *contour integral* + *Lemma 6.1 L'/L bound* — classical tools. RH 진전 X."
- "다음 가치 있는 질문: §6 의 *unconditional partial bound* — *zero-free region* 도구로 partial."
- "§5 (unconditional S_∞) + §6 (RH-conditional S_f) = paper-direct *quantitative* form of *Wall #6 cancellation*. paper-direct mapping."

### Sarnak 추정
- "Lagarias-Li §6 의 *Ramanujan conjecture cross-link* 가 *Wall #4 family-wide* 에 connection. GL(N) Ramanujan 은 open — *family-wide bound* 가 partial."
- "Pratt-Robles 5/12 + Iwaniec-Sarnak §5 mollification 50% target 이 family-wide. Lagarias-Li §6 와 *별개 방향* — single π *quantitative*."

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. Lagarias / Sarnak 직접 검증 X. 본 추정은 paper §6 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — Lagarias §6 paper-direct deep + §5 + §6 결합 paper-direct quantitative form + Lemma 3 15th evidence + Wall #6 quantitative cancellation 명시.
