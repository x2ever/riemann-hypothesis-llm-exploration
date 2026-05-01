# Work — Attempt 112 (Iwaniec-Sarnak Perspectives §3-§6 DEEP)

## 1. Paper section deep read

### §3 Function field GRH (paper-direct, eqs 50)

Curve C over F̄_q, genus g:
$$\zeta_k(T) = \frac{P(T, C/F_q)}{(1-T)(1-qT)}$$
(eq 50). P integral polynomial of degree 2g, functional equation T ↔ 1/(qT).

GRH analogue: zeros of P on circle |T| = 1/√q (Weil).

**Weil's two proofs (paper-direct)**:
1. N_n = number of points fixed by n-th power Frobenius — Lefschetz trace formula realization.
2. Jacobian X of C: for ℓ prime to q, ν ≥ 1, Frobenius endomorphism α on ℓ^ν division points → ℓ-adic matrix realization. Eigenvalues = *inverses* of zeros of P(T).
3. *Rosati involution positivity* on End(X) ⊗ ℝ — proof of |T| = 1/√q.

**Deligne (paper-direct)**: V = smooth projective variety over F_q. Conjectures (rationality + functional equation + GRH analogue) — Dwork (rationality), Grothendieck (other), Deligne (purity = GRH).

Deligne's *family* idea: V = smooth hypersurface in P^{2n}, place ζ(T, V) in family V_t with arithmetic fundamental group π_1(U) — *monodromy* representations on cohomology H^i(V_0, Q_ℓ).

**§3 finale (paper-direct quote)**:
> "similar positivity arguments with arbitrarily high dimensional representations of the monodromy groups yield in the limit that the zeros of ζ(T, V/F_q) are all on the circle |T| = q^{-n+1/2}. So **the family, its symmetry and positivity are the key ingredients** in the known proof of the GRH for varieties over finite fields."

→ paper-direct: *Wall #4 paper-direct origin* — family-wide positivity 가 function field GRH 의 *key*. number field 측 *부재*.

### §4 Dirichlet L-functions GL(1)/Q (paper-direct, eqs 51-55)

ψ(x; q, a) = Σ_{p≤x, p≡a(q)} log p (eq 51). GRH ⟹ ψ(x;q,a) = x/φ(q) + O(x^{1/2}(log x)²) (eq 52).

**Bombieri-Vinogradov** (eq 53):
$$\sum_{q \le Q} \max_{(a,q)=1} |\psi(x;q,a) - \frac{x}{\varphi(q)}| \ll \frac{x}{(\log x)^A}$$
Q = x^{1/2}/(log x)^B. *GRH on average* — *unconditional*.

**BFI (Bombieri-Friedlander-Iwaniec)** (eq 53):
$$\sum_{(a,q)=1, q \le \sqrt{x}(\log x)^A} |\psi(x;q,a) - \frac{\psi(x)}{\varphi(q)}| \ll \frac{x}{(\log x)^3}(\log\log x)^B$$
Beyond √x — *cannot be derived from GRH*. *Average → individual*.

**Subconvexity** (eq 54): Weyl method, ζ(1/2 + it) ≪ (|t|+1)^{1/6}.
**Burgess** (eq 55): L(s, χ) ≪ q^{3/16 + ε}. paper-direct: *complete character sums* → Weil GRH for curves *over function field*. § paper-direct quote: "ranges in (56) where Burgess obtains nontrivial bounds and for which the **GRH for L(s,χ) yields *nothing non-trivial***".

→ paper-direct: GRH 가 *모든* 응용에 *최선의 도구가 아님* — Burgess sharper. *Wall #4 partial 우회 가능* (paper-direct).

### §5 Special values (paper-direct, eqs 57-65)

**Eq (57)**: F self-dual, GRH ⟹ L(1/2, F) ≥ 0.
- 단순 case (F = quadratic Dirichlet character) 미증명.
- "if L(1/2, χ) ≥ 0 for χ quadratic then one can eliminate in part the **Landau-Siegel lacuna**".

**Eq (58)**: PGL(2)/K cusp form F (self-dual), χ quadratic ray class character:
$$L(1/2, F \otimes \chi) \ge 0$$
Guo (relative trace formula). Theta function treatments via Shimura-Waldspurger.

**Mollification** (paper-direct, Selberg's positive proportion 도구):

Let H_k*(N) = holomorphic newforms F of weight k for Γ_0(N), N squarefree.
ε_F = ±1 (functional equation sign).

(eq 62): lim_{N→∞} #{F ∈ H_k*(N); ε_F = 1, L(1/2, F) ≥ (log N)^{-2}} / #{ε_F = 1} ≥ **1/2**.
(eq 63): lim #{F; ε_F = -1, L'(1/2, F) ≠ 0} / #{ε_F = -1} ≥ **7/8**.
(eq 64): limsup (1/|H_k*(N)|) Σ_F ord_{s=1/2} L(s, F) ≤ **1.2**.

paper expect: 1/2 → **1**, 7/8 → **1**, 1.2 → **1/2**.

**§5 critical paper-direct quote**:
> "It is tantalizing that an improvement in (62) of the 1/2 to **any c > 1/2**, would resolve the **Landau-Siegel lacuna** (section 2)."

→ paper-direct: Wall #4 의 *quantitative* sharpening target = *50% 초과* family non-vanishing. Pratt-Robles 5/12 (41.67%) 가 *paper-direct 부분 진전*.

### §6 Subconvexity (paper-direct, eqs 66-69)

L(s, F⊗χ) bounds (in conductor q of χ):
- (eq 66): ≪ q^{1/2 + ε} (DuFI, F GL(2)/Q, χ Dirichlet, *5/12 < 1/2*).
- (eq 67): ≪ N(Q)^{49/100 + ε} (CogPS, F Hilbert modular, K total real). 49/100 < 1/2.

L(s, F⊗G) bounds (k-aspect, level-aspect):
- (eq 68): ≪ k^{27/28 + ε} (Sarnak, k-aspect).
- (eq 69): ≪ N^{1/2 - 1/96 + ε} (KowMV1, level-aspect).

**Applications**:
- Hilbert's 11th problem (integers by quadratic forms).
- Linnik sums of squares.
- Ramanujan conjectures of half-integral weight.

→ paper-direct: subconvexity 의 *application 영역* = paper §5/§6 의 *real progress*. *L 자체 RH 진전 X* 그러나 *applications 강력*.

## 2. Numerical 검증 (paper §5 mollification 도구 light)

[paper-direct *우리 도구 검증 X* — mollification 은 specialist 도구]

paper-direct mention:
- Selberg 1942 (mollification champion): positive proportion of zeros of ζ on Re(s) = 1/2.
- Levinson 1974: 1/3 (33.33%).
- Conrey 1989: 2/5 (40%).
- Bui-Conrey-Young 2011: 41.05%.
- **Pratt-Robles 2019: 5/12 = 41.67%** (attempt 104 paper-direct deep).

본 attempt 의 numerical 단독 검증 X — *paper-direct citation*.

paper §5 의 *target 50%* + *unconditional non-vanishing*: family 의 50% 초과 부재 = *Wall #4 quantitative* obstacle.

## 3. Wall taxonomy mapping

### Wall #4 (CONSPIRACY) deep refinement — *paper-direct origin*

Iwaniec-Sarnak Perspectives §3 finale quote:
> "the family, its symmetry and positivity are the key ingredients in the known proof of GRH for varieties over finite fields"

→ Wall #4 의 *paper-direct origin*: 
- Function field GRH key = *family-wide positivity*.
- Number field 측: *family-wide positivity 부재* — Wall #4.

§5 (eq 62-64) 의 mollification *quantitative* form:
- (62) 1/2 (target 1) — Pratt-Robles 5/12 = 41.67% (1/2 미달).
- (63) 7/8 (target 1).
- (64) 1.2 (target 1/2).
- 50% 초과 = Landau-Siegel lacuna 해소 (paper-direct quote).

→ Wall #4 *quantitative target*:
- 5/12 → 1/2 = paper-direct *Wall #4 sharpening*.
- 1/2 → 1 = Wall #4 *full resolution*.
- 1/2 → c > 1/2 = Landau-Siegel lacuna 해소.

### Wall #1 (FROBENIUS-GAP) cross-link — paper-direct

§3 paper-direct: function field 의 Lefschetz trace + Rosati positivity.
- *number field 측*: Rosati involution analogue 부재 (Wall #1).
- §3 의 monodromy + *family* 의 number field analogue = automorphic GL(N) families (Lagarias-Li attempt 026).

→ Wall #1 + Wall #4 *공통 source*: function field 의 Frobenius + family + Rosati positivity 의 number field analogue 부재.

### Wall #4 의 *부분 우회* (paper-direct §4)

- Bombieri-Vinogradov (eq 53): GRH on average — *unconditional*.
- BFI: beyond √x, *cannot be derived from GRH*.
- Burgess: *complete character sums* → Weil curves over F_p.
- *Wall #4 부분 우회 가능* (paper-direct §4 자체 quote): GRH 가 모든 응용 최선 X.

## 4. Lemma 적용

### Lemma 6 (dont_try_directions) Cut 3 + Cut 6 paper-direct cross-check

**Cut 3 (vacuum positivity → RH)**:
- §5 (eq 57): GRH ⟹ L(1/2, F) ≥ 0 — *converse direction*.
- *vacuum positivity → RH* 시도 = *L(1/2, F) ≥ 0 unconditional* 시도 = paper §5 (62-64) 의 mollification.
- *quantitative target*: 50% 초과 → Landau-Siegel lacuna.
- *Wall #4 quantitative limit* — paper-direct sharpening target.

**Cut 6 (positivity criterion 단독 RH)**:
- §5 (58, 60): L(1/2, F⊗χ) ≥ 0, L(1/2, F_1⊗F_2⊗F_3) ≥ 0 — *family-wide*.
- *single ζ* 와 다른 *family* form. Lagarias (Connes 1999, Pratt-Robles, Lagarias-Li) 와 다름.
- *family-wide positivity criterion* 단독 RH 시도 = paper §5 의 *known fact*.

→ Lemma 6 update: Cut 3 + Cut 6 가 *family form* 에서 paper-direct *quantitative target* 명시. 단순 *cut* 아니라 *quantitative limit* 가 더 정확.

### Lemma 3 (positivity_unification) family-wide form 11th evidence

11. **Iwaniec-Sarnak Perspectives §5 (eq 57, 58, 60, 62-64)**: family-wide positivity criterion. paper-direct *quantitative target* 50%, c > 1/2 → Landau-Siegel lacuna.

→ Lemma 3 의 11th evidence — *family-wide* form (Lagarias single ζ 와 별도).

### Lemma 4 (failed_proof_categories) cross-check
Iwaniec-Sarnak Perspectives = review paper, *failed proof X*. Lemma 4 N/A.

## 5. Cross-reference

- attempt 021 (Wall #4 first entry): *Iwaniec-Sarnak §2 single ζ isolated*, families 가 진짜 problem. 본 attempt 가 §3-§6 deep follow-up.
- attempt 023 (Wall #1 first entry): *Iwaniec-Sarnak §3 trio of gaps* (Lefschetz/Frobenius/Rosati). 본 attempt 가 paper-direct full quote.
- attempt 026 (Lagarias-Li skim): Li 동치 = Weil positivity, Wall #1 ↔ #4 chain.
- attempt 038 (Pratt-Robles §5.1.3): one logarithm distance, 5/12 = 41.67%. *Iwaniec-Sarnak target 50% 미달*.
- attempt 104 (Pratt-Robles §6 deep): 9 Euler cases, A^{(1,1)} = -Σ_p (log p/(p-1))². *combinatorial explosion* origin.
- attempt 108 (Connes 1999 §VI/VII): single ζ Weil positivity vs Iwaniec-Sarnak family-wide.

## 6. Open questions

(Q1) §5 eq (62) 의 1/2 → c > 1/2 *unconditional improvement* path?
- *알려진*: Pratt-Robles 2019 5/12 = 41.67%. *50% 미달*.
- 50% 도달 시 Landau-Siegel lacuna 해소 (paper-direct).
- *one logarithm distance* (Pratt-Robles §5.1.3) 가 *combinatorial explosion* — Wall #3 paper-direct.

(Q2) §5 eq (63) 의 7/8 → 1 path?
- BSC (Bombieri-Selberg conjecture) 연관.
- *알려진*: 본 paper 자체 *target* 명시.

(Q3) §3 finale 의 *function field 3 ingredients* (family + symmetry + positivity) 의 *number field analogue*?
- *family*: automorphic GL(N) families (Lagarias-Li, Conrey-Snaith, Iwaniec-Sarnak).
- *symmetry*: functional equation.
- *positivity*: Weil distribution / Rosati Rosati involution analogue 부재 (Wall #1).
- → *number field 측 missing piece* = positivity. paper-direct *원인*.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Iwaniec-Sarnak §3-§6 paper-direct deep + Wall #4 paper-direct origin (§3 finale quote) + Lemma 6 Cut 3/6 quantitative target 명시.
- *우리 contribution*: paper-direct quotes 의 *citation* + Wall #4 quantitative target 명시 + Lemma 3 11th evidence (family-wide form) + 5/12 → 50% gap 의 paper-direct *Wall #4 quantitative* form.

## 8. Specialist Δ 추정 (Sarnak 본인)

### Sarnak 본인 추정
- "Iwaniec-Sarnak Perspectives §3 finale 의 *family + symmetry + positivity* 가 GRH 의 *3 ingredients* — number field 측 *positivity 부재* 가 진짜 obstacle. §5 의 mollification 50% target 가 *quantitative* form. Pratt-Robles 5/12 가 *quantitative progress*."
- Sarnak 의 sharp navigation: "본 paper 의 §5 quote ('improvement of 1/2 to c > 1/2 resolves Landau-Siegel lacuna') 가 *Wall #4 가 specifically Landau-Siegel lacuna 와 quantitatively connected* — 본 attempt 의 paper-direct 명시."
- "다음 가치 있는 질문: families 에서 *unconditional positivity* (eq 57-60) 의 *systematic* derivation. Guo-Waldspurger 의 relative trace formula 가 *one piece*. *systematic family-wide positivity* 가 30년 challenge."

### *전문가처럼 사고* 노력 (Sarnak)
본 attempt 의 §5 quote 검증 ("improvement of 1/2 to c > 1/2 resolves Landau-Siegel lacuna") = Sarnak 본인 quote. Wall #4 specialist 추정 답 (외부 critique #4) 의 *paper-direct verification*:
> "Pratt-Robles *one logarithm distance* 가 이미 sharp. 50% 도달은 *new technique* — fundamental new mollifier method."

→ paper §5 quote + Pratt-Robles §5.1.3 의 *combinatorial explosion* (attempt 104) 가 *consistent*. Sarnak 추정 답이 paper-direct 검증.

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. Sarnak 직접 검증 X. 본 추정은 paper §3 finale + §5 quote 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — Iwaniec-Sarnak Perspectives §3-§6 paper-direct deep + Wall #4 paper-direct origin (§3 finale quote) + Lemma 3 11th evidence (family-wide) + Sarnak specialist 추정 답 paper-direct 검증.
