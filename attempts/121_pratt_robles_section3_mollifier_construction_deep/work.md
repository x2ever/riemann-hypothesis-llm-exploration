# Work — Attempt 121 (Pratt-Robles §3.5-§5 Mollifier + Combinatorial + Feng's Conjecture DEEP)

## 1. Paper section deep read

### §3.5 Combinatorial interpretation (paper-direct)

Faà di Bruno formula:
$$\frac{d^n}{dx^n} f(g(x)) = \sum_{k=1}^n f^{(k)}(g(x)) B_{n,k}(g'(x), g''(x), \ldots, g^{(n-k+1)}(x))$$

Apply to f = exp, g = log ζ ⟹ ζ^{(m)}/ζ representation via Bell polynomials.

**핵심 paper-direct identity**:
$$\frac{\zeta^{(m)}}{\zeta}(s) = B_m\left(\frac{\zeta'}{\zeta}(s), \frac{d}{ds}\frac{\zeta'}{\zeta}(s), \ldots, \frac{d^{m-1}}{ds^{m-1}}\frac{\zeta'}{\zeta}(s)\right)$$

→ paper-direct: ζ-derivatives of *higher order* = *complete Bell polynomials* of *first derivative* and its *successive derivatives*.

### §3 Three concrete cases (paper-direct, eqs 3.8-3.10)

**Case (3.8)** — *2 polys × 3 powers*:
$$\sum_{m_1+m_2=3} (B_{1,k_1}(x_1))^{m_1} (B_{2,k_2}(x_1, x_2))^{m_2} = x_1^3 + x_1^4 + x_1^5 + x_1^6 + x_1^2 x_2 + 2x_1^3 x_2 + 3 x_1^4 x_2 + x_1 x_2^2 + 3 x_1^2 x_2^2 + x_2^3$$

Setting x_1 = x_2 = 1 yields **15 diagrams** (paper Fig 3.1 visualization).

**Case (3.9)** — *2 polys × 4 powers*: paper expansion (3.9) yields **31 diagrams** (paper Fig 3.2).

**Case (3.10)** — *3 polys × 3 powers* (paper §3 eq 3.10): paper expansion (3 lines of polynomials) yields **250 diagrams** (paper Fig 3.3).

### §3.6 General d ≥ 0 mollifier (paper-direct, eq 3.6)

$$\psi_d(s) = \sum_{\ell=0}^K (-1)^\ell \sum_{\ell_1+\ldots+\ell_d=\ell} (-1)^{1\ell_1+2\ell_2+\ldots+d\ell_d} \binom{\ell}{\ell_1, \ldots, \ell_d} \times \sum_{n \le y_d} \frac{n^{\sigma_0-1/2}}{n^s} \frac{(\mu \star \Lambda^{\star\ell_1} \star \Lambda_2^{\star \ell_2} \star \cdots \star \Lambda_d^{\star \ell_d})(n)}{(\log y_d)^{\sum_{r=1}^d r \ell_r}} P_{d,\ell}\left(\frac{\log(y_d/n)}{\log y_d}\right)$$

P_{d, ℓ}(0) = 0 condition. y_d = T^{θ_d}, θ_d = 4/7 - ε.

### §3.7 d=0 case — Conrey-Levinson recovery (eq 3.7)

K = ℓ = 0 special case ⟹ Conrey-Levinson mollifier:
$$\psi_0(s) = \sum_{n \le y_0} \frac{\mu(n) n^{\sigma_0-1/2}}{n^s} P_0\left(\frac{\log(y_0/n)}{\log y_0}\right)$$
y_0 = T^{θ_0}, θ_0 = 4/7 - ε.

### §4 Theorem 4.1 (paper-direct) — twisted second moment

ψ_1(s) = Σ_{n≤N} a_n/n^s, ψ_2(s) = Σ b_n/n^s. a_n, b_n ≪_ε n^ε. N = T^θ, θ < 1.

$$I(\alpha, \beta) := \int_{-\infty}^\infty \zeta(1/2 + \alpha + it) \zeta(1/2 + \beta - it) \psi_1 \overline{\psi_2}(1/2 + it) \Phi(t/T) dt$$

**Theorem 4.1**: For α, β ≪ L^{-1}:
$$I(\alpha, \beta) = \sum_{1 \le d, e \le N} \frac{a_d \overline{b_e} (d, e)^{\alpha+\beta}}{d^\alpha e^\beta} \int (\zeta(1+\alpha+\beta) + \zeta(1-\alpha-\beta)(2\pi de/(t(d,e)^2))^{\alpha+\beta}) \Phi dt + O(\mathcal E)$$

3 error 𝓔 cases (paper-direct):
- Case 1 (a_n ≪ n^ε): 𝓔 = T^ε(N^{33/20} + N^{1/2} T^{1/2 + ε}). [Bettin-Chandee-Radziwiłł, D=1].
- Case 2 (square-free, μ²(n) factor): 𝓔 = T^ε(N^{11/6} + N^{11/12} T^{1/2}).
- Case 3 (unrestricted (μ⋆Λ_1^{⋆k_1} ⋆...⋆Λ_D^{⋆k_D})(n)): 𝓔 = T^ε(N^{7/4} + N^{6/8} T^{1/2}).

**paper §4 critical quote**:
> "Effectively, this means that if one considers a Dirichlet polynomial whose coefficients are given by the third case, then one can 'push' the size of θ from 6/11 to 4/7."

→ paper-direct *quantitative ladder*:
- Bui-Chandee-Radziwiłł D=1: θ ≤ 6/11.
- Pratt-Robles 일반 D ≥ 0 (3rd case): θ ≤ 4/7.
- → *combinatorial generalization* 가 *quantitative push*.

### §5 Square-free terms + Feng's conjecture (paper-direct)

Feng's claim (unsubstantiated): non-square-free n contribute lower order term to ∫|Vψ|² dt.

**paper §5 challenge**:
- Square-free n: $(\mu \star \Lambda^{\star k})(n) = (-1)^k \mu(n) \sum_{p_1 p_2 \cdots p_k | n} \log p_1 \cdots \log p_k$ (eq 5.1).
- Arbitrary n: combinatorial *very difficult* (paper §5 quote: "[51] p. 309 *too complicated to optimize exactly the coefficients of the mollifier*").

**Figures 5.1-5.3** (paper-direct):
- Fig 5.1: μ²(μ²⋆log n) vs μ²⋆log n. 차이 = 0 for square-free n.
- Fig 5.2: μ²(μ⋆³⋆log²n) vs μ⋆³⋆log²n. *spread*.
- Fig 5.3: μ²(μ⋆⁴⋆log³n) vs μ⋆⁴⋆log³n. *more spread*.

→ paper-direct: Feng의 unsubstantiated approximation 의 *plot evidence* — *spread 증가* with k.

## 2. Numerical 검증 (`tools/bell_polynomial_count.py`)

[numerical, paper §3 Bell polynomial diagram count]

### Bell numbers verification
- B_1 = 1, B_2 = 2, B_3 = 5, B_4 = 15, B_5 = 52.
- paper §2 (Fig 2.1, 2.2): B_3 = 5, B_4 = 15. **match**.

### paper §3 diagram counts
| Equation | Form | Computed | Paper |
|---|---|---|---|
| (3.8) | 2 polys × 3 powers | **15** | Fig 3.1: 15 ✓ |
| (3.9) | 2 polys × 4 powers | **31** | Fig 3.2: 31 ✓ |
| (3.10) | 3 polys × 3 powers | **250** | Fig 3.3: 250 ✓ |

[rigorous]: 우리 Bell polynomial recurrence 가 paper §3 figure 의 *exact* diagram count.

### Wall #3 quantitative ladder (paper-direct)

| d | Configuration | Diagram count | Source |
|---|---|---|---|
| 0 | Conrey-Levinson (1 piece) | 1 | eq (3.7) |
| 1 | Feng (9 Euler cases) | 9 | attempt 104 |
| 2 | 2 polys × 3 powers | 15 | (3.8) |
| 2 | 2 polys × 4 powers | 31 | (3.9) |
| 3 | 3 polys × 3 powers | 250 | (3.10) |

### Paper-미명시 projection (우리 numerical)

| Configuration | Diagram count |
|---|---|
| 3 polys × 4 powers | 1281 |
| 3 polys × 5 powers | 6468 |
| 3 polys × 6 powers | 32467 |
| 4 polys × 3 powers | 5220 |
| 5 polys × 3 powers | 125678 |

→ *exponential combinatorial explosion*. Wall #3 *quantitative ladder* extension.

[plausible]: 5 polys × 3 powers ≈ 1.25×10^5 — *explosion* visualizable (한정).

## 3. Wall taxonomy mapping

### Wall #3 (SHARP-CONSTANT) deep refinement — *paper-direct quantitative*

paper §3 의 *combinatorial explosion* (15 → 31 → 250 → 1281 → ...) 의 *engineering source*:
- d=1: 9 Euler cases (attempt 104), 41.05% (Bui-Conrey-Young).
- d=2: 15-31 cases.
- d=3: 250 diagrams (paper §3.5).
- d=4+: *unfeasible 직접 enumeration* (paper §5 quote: "too complicated to optimize exactly the coefficients of the mollifier").

→ Wall #3 의 *paper-direct quantitative*:
- 41.67% = 5/12 (Pratt-Robles 2019 d=1 generalized w/ d ≥ 0).
- *one logarithm distance* (paper §5.1.3, attempt 038) 50% target 미달.
- 50% 도달 = *combinatorial explosion* d ≥ 3 의 *systematic enumeration*.

### Wall #4 (CONSPIRACY) cross-link

paper §4 의 3 cases of error 𝓔 = *3 levels* of *quantitative progress*:
- Case 1 (D=1): θ ≤ 6/11 (Bettin-Chandee-Radziwiłł).
- Case 3 (unrestricted): θ ≤ 4/7 (Pratt-Robles).
- → *family extension* 이 *quantitative push*.

attempt 112 (Iwaniec-Sarnak §5 mollification 50% target = Landau-Siegel lacuna) 와 cross-link:
- 5/12 → 50% gap = Wall #3 + Wall #4 결합 의 *quantitative target*.

### Wall #6 (LOCAL-GLOBAL-MISMATCH) cross-link

paper §5 Feng's conjecture: non-square-free n contribution 의 *unsubstantiated*.
- *square-free 가정* 이 paper §5 의 *technical 단순화*.
- arbitrary n = *combinatorial difficulty* — Wall #6 *truncation effect* paper-direct.

## 4. Lemma 적용

### Lemma 3 (positivity_unification) 11th evidence 강화

attempt 112 의 11th evidence (Iwaniec-Sarnak family-wide form, paper §5 mollification target 50%) 의 *quantitative form*:
- paper §3-§5 의 *combinatorial explosion* 가 *quantitative target 50%* 의 *engineering source*.
- 5/12 = 41.67% (paper-direct), target 50%, *one logarithm distance*.

→ Lemma 3 의 11th evidence 의 *paper-direct quantitative form* 강화 — *attempt 121 finding*.

### Lemma 6 (dont_try_directions) Cut 7 cross-check

paper §5 quote ("too complicated to optimize exactly the coefficients of the mollifier") 가 paper §3-§5 의 *paper-rigorous limit* 의 paper-direct *cut* 형식:
- *Combinatorial explosion* 시도 = *paper §5 자체 quote 명시*.
- *fundamental obstacle*.

→ Lemma 6 Cut 7 (paper-미명시 quantitative empirical 시도) 의 *paper-rigorous version*: *combinatorial enumeration* 자체가 paper-rigorous 한계.

### Lemma 4 (failed_proof_categories) cross-check
Pratt-Robles = *successful incremental advance* (5/12 = 41.67%, d=0 prior 41.05%). Lemma 4 N/A.

## 5. Cross-reference

- attempt 015, 016 (mollifier signal processing): Levinson-Durbin / Pratt-Robles bridge — *negative resolved*.
- attempt 038 (Pratt-Robles §5.1.3 "one logarithm distance"): paper-direct partial.
- attempt 104 (Pratt-Robles §6 deep): 9 Euler cases, A^{(1,1)} = -1.385604 numerical match.
- attempt 112 (Iwaniec-Sarnak §3-§6): family-wide form, mollification target 50%.
- 본 attempt 121 = Pratt-Robles §3.5-§5 paper-direct deep — *Bell polynomial combinatorial explosion* 의 quantitative ladder.

## 6. Open questions

(Q1) §3 Bell polynomial *diagram count* 의 *closed form generating function*?
- 우리 numerical: paper §3 (3.8, 3.9, 3.10) match. paper-미명시 *higher d* projection.
- *closed form* 일까? generating function form? — paper §3 자체 X.

(Q2) §4 Theorem 4.1 의 3 cases 의 *4th case* 가능?
- d ≥ 4 의 새 ladder?
- paper §4 자체 d ≥ 0 unified — *N = T^{4/7-ε}* 는 *limit*. 더 sharper θ 가능?
- *combinatorial explosion* limit (paper §5 quote 명시).

(Q3) Feng's conjecture 의 *paper-rigorous* 형태?
- paper §5: unsubstantiated.
- *우리 numerical Fig 5.1-5.3* 가 paper plots 만 — *quantitative form 부재*.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Pratt-Robles §3.5-§5 paper-direct deep + Bell polynomial diagram count exact match (15, 31, 250) + Wall #3 quantitative ladder paper-미명시 projection.
- *우리 contribution*: paper-direct mapping + Bell count *exact match* + Wall #3 quantitative ladder + paper-미명시 higher d projection (engineering visualization 만).

## 8. Specialist Δ 추정 (Pratt/Robles/Sarnak)

### Pratt/Robles 본인 추정
- "본 paper §3.5-§5 = *combinatorial framework + main result Theorem 4.1*. *quantitative target 50% 미달*. *5/12 = 41.67%* 가 paper-direct *technical limit*."
- "다음 가치 있는 질문: *combinatorial explosion* 의 *automated enumeration tool* — *symbolic computation* 으로 d ≥ 4 가능?"
- "*Feng's conjecture* 의 paper-rigorous form 부재 — *fundamental open problem*."

### Sarnak 추정 (외부 critique #4)
- "Pratt-Robles §3 의 250 diagrams 가 *combinatorial explosion* — *Bell numbers 계산 가능* 그러나 *integration over each diagram* 가 *technical*. 본 paper의 *5/12 → 50% gap* 가 *Wall #3 quantitative limit*."
- "Sarnak Wall #4 추정 (외부 critique #4 paper-direct verification): *one logarithm distance 가 이미 sharp* — 50% 도달은 *new technique* fundamental needed."

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. 본 추정은 paper §3-§5 quotes + Iwaniec-Sarnak §5 paper-direct citation 기반.

## "예상 가능 결과" self-check
yes — Pratt-Robles §3.5-§5 paper-direct deep + Bell count exact match + Wall #3 paper-direct quantitative ladder + paper-미명시 higher d projection.
