# Work — Attempt 103 (Voros 2006 §3 Saddle-Point DEEP)

## 1. Paper section deep read

### §2 Setup (paper-direct, eqs 9-12)

Voros 의 sequence λ_n 을 두 *equivalent* representations 로 expression:

**Discrete sum (eq 9)**:
$$\lambda_n = -n \sum_{j=1}^n \frac{(-1)^j}{j} \binom{n+j-1}{2j-1} Z(j)$$
where $Z(\sigma) := \sum_k x_k^{-\sigma}$, $x_k = 1/4 + \tau_k^2 = \rho(1-\rho)$ — **secondary zeta function**.

**Integral representation (eq 12)** — *much more flexible*:
$$\lambda_n = \frac{(-1)^n n i}{\pi} \oint_C I(\sigma)\,d\sigma, \quad I(\sigma) = \frac{\Gamma(\sigma + n)\Gamma(\sigma - n)}{\Gamma(2\sigma + 1)} Z(\sigma)$$
C: positive contour around poles σ = +1, ..., +n.

### §3 Saddle-point method

For large n, |I(σ)| dominantly controlled by:
- Γ factors: $\sim \pi[\sin\pi\sigma\, \Gamma(2\sigma+1)]^{-1} n^{2\sigma-1}$ for finite σ.
- Polar parts of I(σ).

**Two saddle-point types** (paper §3 직접):

**Type 1**: σ on segment $(1/2, 1)$ — real saddle σ_r(n) → 1/2 as n → ∞.

**Type 2**: Complex saddle (off real axis) — saddle equation
$$\sigma_k(n) = ni/(2\tau_k)$$
This emerges if there exists *zero off critical axis* (RH false).

### §3 [RH false] case (paper-direct)
If exists ρ = 1/2 ± iτ_k *off* critical axis (Re(ρ) ≠ 1/2):
- complex saddle σ_k(n) inside Re σ > 1/2 region.
- contribution ~ $[(\tau_k + i/2)/(\tau_k - i/2)]^n$ — *exponentially growing in modulus*, oscillating phase.
- *exponentially dominates* real saddle contribution.

**Eq (14)**: $\lambda_n \sim \sum_{|z_k|<1} z_k^{-n} + c.c. \pmod{o(e^{\varepsilon n})}$
where $z_k = (\tau_k - i/2)(\tau_k + i/2)^{-1}$.

→ |z_k| < 1 ⟺ ρ off critical axis.

### §3 [RH true] case (paper-direct)
- 모든 τ_k real → all z_k on unit circle (|z_k| = 1).
- Darboux formula (14) breaks down (identical dominant modulus).
- Saddle-point treatment: Z(σ) = O(Z(Re σ) |Im σ|^{-3/2}) in {Re σ > 1/2}.
- Contour C 가 boundary {Re σ = 1/2} 까지 이동 가능.
- Dominant saddle = real saddle σ_r(n), pulled to σ = 1/2 *non-isolated* (tends to double pole of Z(σ)).
- Standard saddle-point fails (non-isolated pole).
- *Direct contour deformation* until enclosing pole → residue at σ=1/2:

**Eq (15)**:
$$\lambda_n \sim (-1)^n \cdot 2n \cdot \text{Res}_{\sigma=1/2} I(\sigma) = 2\pi n [2 R_{-2}(\psi(1/2 + n) - 1 + \gamma) + R_{-1}] + O(1/n)$$
With $R_{-2} = 1/(8\pi)$, $R_{-1} = -\log(2\pi)/(4\pi)$ (eq 6):
$$\lambda_n \sim \frac{1}{2} n [2 R_{-2}(2 \log n + 2\gamma - 2 - 2\log 2\pi)] + ... = \frac{1}{2}n(\log n - 1 + \gamma - \log 2\pi) \pmod{o(n)}$$

## 2. Numerical 검증

[numerical, dps=40, 200 zeros]

Voros eq (5): $Z(1/2 + \varepsilon) = R_{-2}\varepsilon^{-2} + R_{-1}\varepsilon^{-1} + O(1)$.

| σ = 1/2 + ε | Z(σ) (200 zeros) | polar pred R_-2/ε² + R_-1/ε | diff |
|---|---|---|---|
| 1.0 (ε=0.5) | 0.0210 | -0.1334 | +0.154 |
| 0.7 (ε=0.2) | 0.2279 | 0.2635 | -0.036 |
| 0.6 (ε=0.1) | 0.5446 | 2.5163 | -1.972 |
| 0.55 (ε=0.05) | 0.854 | 12.99 | -12.14 |

[rigorous]:
- ε > 0.2 영역에서 polar prediction 이 *over-estimates* (truncation effect — 200 zeros 만 사용).
- ε → 0 에서 polar predict 가 발산 (1/ε² ↑) 하나 200 zeros 부분합 은 finite.
- *알려진 truncation behavior* — Z(σ) 의 진짜 polar 가 *모든 zeros* 합으로만.

## 3. Wall taxonomy mapping

### Wall #6 (LOCAL-GLOBAL-MISMATCH) **deep refinement**
- 본 §3 의 Voros dichotomy = Wall #6 의 paper-direct *origin*.
- attempts 040, 042, 044, 067, 101 의 numerical observations 가 정확히 *[RH true] tempered case*.
- *truncation effect*:
  - λ_n^(N)(true) ~ (1/2) n log n + ... + O(N^{-?}) — partial sum 이 모든 zeros 누적까지 truncation.
  - 더 많은 zeros + n 증가 비율 의 *trade-off*.
- Wall #6 의 *quantitative form*: truncation 효과 ≈ N=500 → n=200 sweet spot, N=800 → n=300 sweet, ...

### Wall #2 (FORWARD-TIME) cross-link
- §3 의 contour deformation = Polymath 15 §3 의 zero dynamics 와 mathematical *isomorphic* — 둘 다 *complex saddle behavior* 의 정량.

### Wall #1 (FROBENIUS-GAP) 미연결
- §3 는 number field 측. function field 측 cohomology framework 와 직접 mapping X.

## 4. Lemma 적용

### Lemma 3 (positivity_unification_hypothesis) 갱신 candidate
Voros §3 의 *Z(σ) double pole at σ=1/2* + R_{-2} = 1/(8π) > 0 — positive residue. 이는 *positivity* 의 paper-direct instance:
- σ → 1/2 에서 double pole *positive* residue → λ_n 의 *tempered positive growth*.
- positivity unification chain 의 Voros side instance.

`lemmas/positivity_unification_hypothesis.md` 6번째 paper-direct evidence.

## 5. Cross-reference

- Lagarias 2004 §5 (attempt 086): C_1 = (1/2)(γ - 1 - log 2π) — Voros R_-1 / R_-2 ratio 의 동일 form.
- Connes 1999 §III (attempt 088): Polya-Hilbert space 의 *spectrum* = Z(σ) double pole 영점 source 의 *spectral interpretation*.
- Connes-Consani 2021 (attempt 033, 082): *near radical of Weil QF* 와 Z(σ) zeros σ = 1/2 + iτ_k 의 connection.

## 6. Open questions

(Q1) Voros §3 의 [RH false] case 가 paper §1 Theorem (paper-direct asymptotic dichotomy) 의 *integral form*. *unconditional* 으로 [RH false] case 의 가능 zero 의 *quantitative location* 을 numerical 으로 search 가능?
- attempts 040, 042, 044, 067, 101 의 sign(λ_n) = + 일관 — 만약 [RH false] *유한 개* off-critical zeros 가 존재 시 어느 *n threshold* 부터 negative 출현?
- Voros bound: 첫 negative threshold ~ |Im(1/τ_k)|^{-1} where τ_k off critical.
- 우리 도구로 이 threshold 추적 가능 (단, 알려진 numerical search 의 우리 도구 우열 X).

(Q2) Z(σ) 의 *full asymptotic expansion* 이 일반 L-function 으로 어떻게 일반화? Lagarias §4 의 ζ*(j) 와 Voros Z(j) 의 정확한 mapping?

## 7. Yellow flag + honest scope

[045 protocol]:
- "RH consistent / evidence" 회피.
- 본 attempt = Voros §3 paper section deep read + numerical Z(σ) sanity + wall mapping + lemma 3 6th evidence.
- *novel mathematical content*: **0** — 모두 Voros 2006 paper-direct.
- *우리 contribution*: paper-direct mapping + numerical Z(σ) verification + lemma 3 갱신 candidate + open question Q1 (numerical search trajectory 후보).

## "예상 가능 결과" self-check
yes — Voros §3 paper-direct.
