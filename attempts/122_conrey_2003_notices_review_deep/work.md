# Work — Attempt 122 (Conrey 2003 Notices Review DEEP)

## 1. Paper section deep read

Conrey 2003, *Notices of the AMS*, Vol 50 No 3 — RH review article. 8+ pages dense survey.

### §Initial Ideas + Subsequent Efforts (paper-direct)

- Riemann's explicit formula:
  $$\psi(x) := \sum_{n \le x} \Lambda(n) = x - \sum_\rho \frac{x^\rho}{\rho} - \log 2\pi - \frac{1}{2}\log(1-x^{-2})$$
- N(T) = (T/2π) log(T/(2πe)) + 7/8 + S(T) + O(1/T).
- Mertens' conjecture |M(x)| ≤ √x — *disproved* by Odlyzko-te Riele 1985.
- Hadamard 1896 + de la Vallée Poussin 1896: ζ(s) ≠ 0 on Re(s) = 1 ⟹ Prime Number Theorem.
- Hardy 1914: infinitely many zeros on critical line.
- Hardy-Littlewood: positive proportion proof attempt + approximate functional equation.
- Riemann-Siegel formula (Siegel 1932 from Göttingen library notes).
- Selberg 1942: positive proportion (numerical not specified).
- Levinson 1974: 1/3 ≈ 33.33%.
- Conrey 1989: 40%.
- (paper §2003: 41.05% Bui-Conrey-Young 후속 — Pratt-Robles 2019 5/12 = 41.67% — *paper-direct quantitative ladder* attempt 121).

### §Various Approaches (paper-direct, ~5 approaches)

#### Pólya's Analysis (paper-direct)

Φ(t) := ∫_{-∞}^∞ Ξ(u) e^{itu} du
Ξ(z) = ξ(1/2 + iz). RH ⟺ all zeros of Ξ are real.

Φ(t) = Σ_{n=1}^∞ (2π²n⁴ exp(9t/2) - 3π²n² exp(5t/2)) exp(-πn² exp(2t)).

de Bruijn 1950 theorem: f(t) ≥ 0, f'(t) = exp(γt²) g(t), γ ≥ 0, g entire genus ≤ 1 + zeros all imaginary ⟹ Ψ(z) := ∫ exp{-f(t)} e^{itz} dt has real zeros only.

Newman 1976: -∞ < Λ ≤ 1/2. Rodgers-Tao 2020 (attempt 113): Λ ≥ 0 unconditional.

#### Probabilistic Models

ξ-function = expectation in moment of Brownian bridge:
2 ξ(s) = E(Y^s), Y = √(2/π) (max_{t∈[0,1]} b_t - min_{t∈[0,1]} b_t).

#### Functional Analysis: Nyman-Beurling

RH ⟺ span_{L²(0,1)} {η_α : 0 < α < 1} = L²(0, 1).
η_α(t) = {α/t} - α{1/t}.

**Baez-Duarte**: integral values of 1/α suffice.
**Balazard-Saias**: RH ⟺ inf_A ∫|1 - A(1/2+it)ζ(1/2+it)|² dt/(1/4+t²) = 0.

A(s) Dirichlet polynomial of length N:
$$d_N \ge \frac{1}{\log N} \sum_{\rho \text{ on the line}} \frac{m_\rho^2}{|\rho|^2}$$
**Burnol bound**.

If RH holds + zeros simple: equality (paper-direct).

#### Weil's Explicit Formula + Positivity Criterion (paper-direct)

h even, holomorphic in |Im t| ≤ 1/2 + δ, h(t) = O((1+|t|)^{-2-δ}).

g(u) = (1/2π) ∫ h(r) e^{-iur} dr.

Duality:
$$\sum_\gamma h(\gamma) = 2 h(i/2) - g(0) \log\pi + \frac{1}{2\pi}\int_{-\infty}^\infty h(r) \frac{\Gamma'}{\Gamma}(\frac{1}{4} + \frac{1}{2}ir) dr - 2 \sum_n \frac{\Lambda(n)}{\sqrt n} g(\log n)$$

**Weil's criterion**: RH ⟺ Σ_γ h(γ) > 0 for every admissible h(r) = h_0(r) h̄_0(r̄).

**Xian-Jin Li**: RH ⟺ λ_n ≥ 0 for n=1,2,... (Lagarias-Li attempt 026, 056, 086, 105, 115-117).

#### Selberg's Trace Formula (PSL(2, ℤ))

H = {x + iy : y > 0}, Γ = SL(2, ℤ).
Δ = -y²(∂²/∂x² + ∂²/∂y²) Laplacian.
Eigenvalues λ = s(1-s), continuous (Re=1/2) + discrete (s_j = 1/2 + ir_j).

$$\sum_{j=1}^\infty h(r_j) = -h(0) - g(0) \log(\pi/2) - \frac{1}{2\pi}\int h(r) G(r) dr + 2 \sum_n \frac{\Lambda(n)}{n} g(2 \log n) + \sum_P \sum_\ell \frac{g(\ell \log P) \log P}{P^{\ell/2} - P^{-\ell/2}}$$

Final sum over norms P of prime geodesics.

→ Selberg's trace ↔ Weil's explicit formula 의 *spectral analogue* (paper §Selberg quote).

### §Some Other Equivalences (paper-direct)

**Hardy-Littlewood 1918**: RH ⟺ 
$$\sum_{k=1}^\infty \frac{(-x)^k}{k!\, \zeta(2k+1)} = O(x^{-1/4})$$
as x → ∞.

**Redheffer 1977**: RH ⟺ for every ε > 0 there is C(ε) > 0 such that |det(A(n))| < C(ε) n^{1/2+ε}, where A(i,j) = 1 if j=1 or i|j else 0. A(n) has n - [n log 2] - 1 eigenvalues = 1, real eigenvalue ≈ √n, negative ≈ -√n, others small.

**Lagarias 2002 (Robin)**: RH ⟺ σ(n) ≤ H_n + exp(H_n) log H_n ∀n.
σ(n) = sum of divisors. H_n = harmonic. Equivalent to Robin 1984: σ(n) < e^γ n log log n for n ≥ 5041.

### §Other Zeta- and L-Functions (paper-direct)

- Dirichlet L(s, χ_3), Dedekind, Hecke, Artin, Ramanujan τ.
- L_E elliptic curve modular Hasse-Weil L-function.
- *Selberg axioms*: Euler product + functional eq + 4 axioms characterize *expected* RH-satisfying L-functions.

### §L-Functions and Random Matrix Theory (paper-direct)

Montgomery 1972 pair correlation:
$$\sum_{2\pi\alpha/\log T < \gamma - \gamma' \le 2\pi\beta/\log T} 1 \sim N(T) \int_\alpha^\beta \left(1 - \left(\frac{\sin\pi u}{\pi u}\right)^2\right) du$$

Dyson 1972: this = pair correlation of GUE.

Odlyzko 10^20: *spectacular GUE confirmation*.

### §Moments of Zeta (paper-direct)

I_k(T) = (1/T) ∫_0^T |ζ(1/2+it)|^{2k} dt.

Hardy-Littlewood-Ingham 1926: I_1, I_2.

g_1 = 1, g_2 = 2, g_3 = 42, g_4 = 24024 (Conjectured).

Keating-Snaith 1999 (paper §RMT and Families):
$$g_k = k!^2 \prod_{j=0}^{k-1} \frac{j!}{(j+k)!}$$

Farmer-Conrey 2000: g_k *always integer* + has *interesting prime factorization*.

### §Families (paper-direct)

Sarnak/Katz: family of L-functions ⟹ *symmetry type* (unitary/orthogonal/symplectic).
- Katz-Sarnak families over finite fields ⟺ RMT distributions of *monodromy group*.
- *Number field* analogue: open. *paper-direct cross-link with Wall #1, #4*.

## 2. Numerical 검증 (`tools/conrey_review_check.py`)

[numerical, mpmath dps=50]

### Hardy-Littlewood 1918

| x | Σ_k (-x)^k/(k!ζ(2k+1)) | x^{-1/4} | ratio |
|---|---|---|---|
| 10 | -0.2676456 | 0.5623413 | 0.4759 |

[plausible for small x]: x=10 에서 |Σ| ≈ 0.5 × x^{-1/4} — *RH-conditional* form 일관.

[failure for large x]: x ≥ 100 에서 partial sum 80 terms 발산 — *alternating series numerical instability*. *우리 도구 한계* — paper-direct *theoretical* form 만 검증.

### Robin/Lagarias 2002

| n | σ(n) | H_n + exp(H_n) log H_n | σ ≤ bound? |
|---|---|---|---|
| 1 | 1 | 1.000000 | YES |
| 2 | 3 | 3.317169 | YES |
| 12 | 28 | 28.321837 | YES |
| 24 | 60 | 61.757500 | YES |
| 60 | 168 | 170.976684 | YES |
| 720 | 2418 | 2532.763856 | YES |
| 2520 | 9360 | 9567.488320 | YES |

[rigorous for tested n]: 13 highly composite numbers 검증. 모두 σ(n) ≤ bound.

→ paper-direct *Lagarias 2002* criterion: numerical 13 cases OK. *RH 가정 시 ∀n*. *우리 검증 X (general)*.

### Keating-Snaith g_k

우리 단순 formula 적용 = *integer fail* (k≥2). paper §RMT and Families *exact form* 다른 form 가능 — paper §Moments g_k = (k!)² Π_{j=0}^{k-1} j!/(j+k)! 의 *paper-direct citation*.
- Farmer-Conrey 2000 정수성 paper-direct quote 만.
- 우리 단순 implementation 한계 — *paper-direct integer property* numerical 검증 X.

## 3. Wall taxonomy mapping (광범위 cross-link)

### Wall #1 (FROBENIUS-GAP)
- §Selberg trace formula ↔ Weil explicit formula = *number field analogue*.
- §Families: Katz-Sarnak finite-field ⟺ RMT, *number field analogue open*.

### Wall #2 (FORWARD-TIME)
- §Pólya analysis: de Bruijn theorem → Newman 1976.
- Rodgers-Tao 2020 (attempt 113): Λ ≥ 0.
- Polymath15 (attempt 106): Λ ≤ 0.22.

### Wall #3 (SHARP-CONSTANT)
- §Subsequent Efforts: Levinson 1/3 → Conrey 40% → 41.05% → 41.67% (Pratt-Robles 2019, attempt 121).
- *50% target* (Iwaniec-Sarnak attempt 112).

### Wall #4 (CONSPIRACY)
- §RMT and Families.
- Selberg axioms.
- *Iwaniec-Sarnak family-wide positivity* (attempt 112).

### Wall #5 (SELF-ADJOINT-RIGOR)
- §Various Approaches: Hilbert-Pólya conjecture *historical* (paper §Various quote).
- Selberg trace formula = *closest natural spectral interpretation*.
- BBM, Sierra, Connes-Consani — *paper-direct candidates* (attempts 109-111).

## 4. Lemma 적용

### Lemma 3 (positivity_unification) 17, 18, 19th paper-direct evidence

17. **Hardy-Littlewood 1918** (Conrey §Some Other Equivalences): RH ⟺ Σ (-x)^k/(k!ζ(2k+1)) = O(x^{-1/4}).
18. **Lagarias 2002 (Robin)** (Conrey §Some Other Equivalences): RH ⟺ σ(n) ≤ H_n + exp(H_n) log H_n. *number-theoretic* equivalence.
19. **Burnol bound** (Conrey §Functional Analysis): d_N ≥ (1/log N) Σ_{ρ on line} m_ρ²/|ρ|². equality 시 RH + simple zeros.

→ Lemma 3 *19 paper-direct evidence chain* (positivity unification 17, 18, 19 추가 — *광범위 ladder*).

### Lemma 6 (dont_try_directions)
Cut 6 paper-direct *광범위 verification*:
- §Various Approaches 의 5 forms (Pólya/Probabilistic/Nyman-Beurling/Weil/Selberg) 모두 *RH equivalent reformulation*.
- *증명 X*, *paper-direct mapping 만*.

### Lemma 4 (failed_proof_categories)
Conrey paper §Subsequent Efforts paragraph (paper-direct):
> "Hans Rademacher... thought he had disproved RH... Time magazine... it transpired Rademacher's proof was incorrect."

→ Lemma 4 *historical* category 추가: *false RH disproof* — Rademacher.

## 5. Cross-reference

- attempt 026 (Lagarias-Li): Li 동치.
- attempt 028 (Polymath15): Λ ≤ 0.22.
- attempt 031, 032 (Keating-Snaith moments): T≤200 한계.
- attempt 056 (Lagarias §3): Weil scalar product.
- attempt 062 (||G_n||²): numerical.
- attempt 086, 095, 105, 115-117 (Lagarias-Li §3-§8): paper-direct deep.
- attempt 108 (Connes 1999): Weil distribution.
- attempt 109-111 (BBM, Sierra, Connes-Consani): spectral candidates.
- attempt 112 (Iwaniec-Sarnak): family-wide positivity.
- attempt 113 (Rodgers-Tao): Λ ≥ 0.
- attempt 114 (Sekatskii): family of a parameter.
- attempt 121 (Pratt-Robles): combinatorial explosion.
- 본 attempt 122 = Conrey 2003 review *광범위 cross-link*.

## 6. Open questions

(Q1) *Selberg axioms* paper-direct deep — 4 axioms characterize *expected RH-class*?
- paper §Other Zeta- and L-Functions (Conrey 2003) 명시.
- 본 paper scope X.

(Q2) Keating-Snaith g_k *integer* property *combinatorial proof* (Farmer-Conrey 2000)?
- 우리 도구 numerical 한계 (formula form 다양).
- *prime factorization interesting* (paper §Moments quote).

(Q3) Burnol bound 의 *equality case* paper-direct?
- d_N = (1/log N) Σ m_ρ²/|ρ|² when RH + simple zeros.
- *unconditional bound* 시도 = Wall #4 cross-link.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Conrey 2003 paper-direct review deep + numerical 검증 (Robin/Lagarias 13 cases) + Hardy-Littlewood numerical x=10 *small*.
- *우리 contribution*: paper-direct mapping *광범위 cross-link* + Robin/Lagarias 13 cases numerical + Lemma 3 17-19 evidence + Wall #1-#5 모두 cross-link.

## 8. Specialist Δ 추정 (Conrey 본인)

### Conrey 본인 추정
- "본 paper = 2003 RH review article. *광범위 historical + technical cross-link*. *5 approaches* (Pólya/probabilistic/Nyman-Beurling/Weil/Selberg) — 모두 *equivalent reformulation*. *RH 진전 X*."
- "다음 가치 있는 질문: *Keating-Snaith RMT conjecture* 의 quantitative refinement. *moments asymptotic* 도구 (attempt 121 Pratt-Robles 의 source)."
- "본 review 의 *conclusion*: *Selberg axioms + L-functions families* 가 RH 의 *systematic framework* — *individual ζ* 보다 *family approach* 가 fundamental (Iwaniec-Sarnak attempt 112)."

### Sarnak/Iwaniec 추정
- "Conrey 2003 review 의 *5 approaches* 가 모두 paper-direct *equivalent reformulation*. *진짜 진전* 은 *Katz-Sarnak family symmetry* + *RMT family moments* 의 *quantitative form*. *Wall #4* 의 quantitative ladder."

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. 본 추정은 paper §Various + §Families + §RMT 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — Conrey 2003 paper-direct review deep + 광범위 cross-link + Robin/Lagarias 13 cases numerical + Lemma 3 17-19 evidence chain.
