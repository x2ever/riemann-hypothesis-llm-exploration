---
title: "Lemma 3 — Positivity unification 가설 (19 paper-direct evidence ladder)"
parent: 한국어
nav_order: 18
date: 2026-05-02
---

# Lemma 3 — Positivity unification 가설 (19 paper-direct evidence ladder)

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/18-lemma-positivity-unification/) · *2026-05-02*

> **증명 아님.** 본 post는 *speculative process lemma* 기록: 프로젝트가 읽은 거의 모든 RH-equivalent statement이 *positivity component*를 포함하며, 이들 사이에 *형식적*(수학적 X) cross-mapping 가능하다는 경험적 관찰. 프로젝트 자체 audit 표시: *"hypothesis / synthesis record — proven X, formal mapping only"*.
>
> 따라서 본 post는: literature *organising*에 유용한 bookkeeping artifact일 뿐, unifying mechanism의 evidence 아님. Connes / Deninger / Bombieri가 정확히 이 직관을 수십 년간 추구했고 통합은 여전히 open.

## 1. 원래 statement (`lemmas/positivity_unification_hypothesis.md`, attempt 024)

기존 cycles에서 식별된 5 essential walls 모두 positivity component 보유:

| Wall | Positivity component |
|---|---|
| #1 FROBENIUS-GAP | Rosati involution positivity (function field, Iwaniec–Sarnak §3) |
| #2 FORWARD-TIME | Energy $E \geq 0$; *integrated* bound 부재 |
| #3 SHARP-CONSTANT | Mollifier Gram matrix positivity, sharp limit |
| #4 CONSPIRACY | Family separation positivity (Rankin–Selberg $\geq 0$) |
| #5 SELF-ADJOINT-RIGOR | Inner-product / metric positivity (BBM Hamiltonian) |

Unification *가설* (lemma 파일 paper-direct quote):

> *"5 본질 walls 모두 positivity component 보유. 통합 source 가 Rosati involution positivity (function field) 의 number field 대응물 가능성."*

Lemma 파일 자체 disclaimer:

> *"Formal mapping only — 수학적 동치 X. Speculation 단계; proof candidate 아님. Connes / Deninger / Bombieri program이 정확히 이 unification — 그들도 미해결."*

## 2. 19 paper-direct evidence ladder

본 lemma의 가치는 unification claim 자체가 아니라 *bookkeeping*: 19 published RH-equivalent positivity statement 명단, 각각 paper section 단위로 anchored. 전체 list (paper-direct, 프로젝트 attempt 번호 괄호):

1. **Lagarias §3** [att. 056] — Weil scalar product $\langle G_n, G_m\rangle = \lambda_n + \lambda_{-m} - \lambda_{n-m}$. positivity ⇔ $\mathrm{GL}(1)$ RH.
2. **Voros §3** [att. 103] — Secondary zeta $Z(\sigma) = \sum x_k^{-\sigma}$, saddle-point asymptotic ⇒ tempered $\lambda_n \iff \mathrm{RH}$.
3. **Bombieri–Lagarias 1999** — $\lambda_n \geq 0 \iff \mathrm{RH}$ (Li 1997 generalisation).
4. **Lagarias–Li automorphic** [att. 026] — Li-equivalence = Weil positivity, $\mathrm{GL}(N)$ generalisation.
5. **Sekatskii** — Bombieri–Lagarias의 sharper form.
6. **Pratt–Robles §6** [att. 104] — $A^{(1,1)} = -\sum_p (\log p/(p-1))^2$ (sign convention 다름).
7. **Lagarias §4** [att. 105] — $\tau_n = (-1/2)^{n+1}\zeta(n+1, 1/2)$, Hurwitz form.
8. **Polymath15** [att. 106] — Newman positivity $\Lambda \geq 0$, $H_t$ = forward heat-flow zeros real.
9. **Connes 1999 §VI eq (17)** [att. 108] — $h(u) \geq 0 \Rightarrow$ Weil distribution RHS positive ⇔ $k$의 모든 Grössencharacter에 대한 RH.
10. **Connes–Consani 2021 §1–§2** [att. 111] — Semi-local Weil quadratic form $QW_\lambda$ positivity ⇔ RH. *quantitative* (finite primes $< \lambda^2$); numerical ($\lambda^2 = 11$: smallest positive eigenvalue $2.389\times 10^{-48}$).
11. **Iwaniec–Sarnak Perspectives §5** [att. 112] (eqs 57, 58, 60, 62–64) — Family-wide positivity criterion. $L(1/2, F) \geq 0$ (self-dual + GRH). Mollification eq (62) $1/2 \to c > 1/2$ = Landau–Siegel lacuna 해소 (Sarnak 본인 quote).
12. **Rodgers–Tao 2020 Theorem 1** [att. 113] — $\Lambda \geq 0$ *unconditional*. Newman positivity full proof; de Bruijn–Newman constant.
   - **Platt–Trudgian 2021 Corollary 2** [att. 132] 결합: $\Lambda \leq 0.2$ (paper §3.4 via $H = 3\times 10^{12}$ + Polymath15 §6 Table 1 row 2). 결합: $0 \leq \Lambda \leq 0.2$.
13. **Sekatskii 2014 §2 Theorems 1, 2, 3** [att. 114] — Generalised Bombieri–Lagarias + generalised Li. *parameter $a$ family* (any real $a \neq 1/2$). Quantitative form: positivity ⇔ exponential growth bound $c(\varepsilon)e^{\varepsilon n}$.
14. **Lagarias §5 Theorem 5.1** [att. 115] — $S_\infty(n, \pi) = (N/2) n \log n + C_1(\pi) n + O(N(K+1))$ *unconditional*. $C_1(\pi_{\mathrm{triv}}) \approx -1.130\,330\,7$, $\beta_\infty \approx 0.559\,774$, $\alpha_\infty \approx 0.443\,842$.
15. **Lagarias §6 Theorem 6.1** [att. 116] — $S_f(n, \pi) = \lambda_n(\sqrt n, \pi^\vee) + O(\sqrt n \log n)$. RH-conditional. *§5 + §6 결합*: $\lambda_n \sim (N/2) n \log n + C_1 n + O(\sqrt n \log n)$ (RH 가정).
16. **Lagarias §7 Theorem 7.1** [att. 117] — $F_\pi(z)$ entire, order-1 exponential type, $F_\pi(n) = \lambda_n$. RH ⇔ exponential type $\leq \pi$, $|F_\pi(x)| \leq C(|x|+2)\log(|x|+2)$.
17. **Hardy–Littlewood 1918** (Conrey 2003 §Some Other Equivalences, [att. 122]):
   $$\mathrm{RH} \iff \sum_{k=1}^\infty \frac{(-x)^k}{k!\,\zeta(2k+1)} = O\!\left(x^{-1/4}\right)\ \text{as}\ x \to \infty.$$
18. **Lagarias 2002 / Robin** (Conrey 2003, [att. 122]) — $\mathrm{RH} \iff \sigma(n) \leq H_n + \exp(H_n)\log H_n\ \forall n$. *Number-theoretic* equivalence (divisor function bound).
19. **Burnol bound** (Conrey 2003 §Functional Analysis, [att. 122]):
   $$d_N \geq \frac{1}{\log N}\sum_{\rho \text{ on line}} \frac{m_\rho^2}{|\rho|^2}.$$
   Equality ⇒ RH + simple zeros (Balazard–Saias variant).

**새 mathematics 없음.** 모든 line이 published paper-direct anchor. 프로젝트 기여 = *catalogue* 자체.

## 3. Tissue isomorphism class structure (attempt 137)

Weil's explicit-formula duality 하 19 evidence를 3 classes로 분리:

### Class A — Zeros side (Lagarias-style, 10 evidence)
1, 2, 3, 4, 5, 7, 13, 14, 16, 17 — Lagarias §3, Voros §3, Bombieri–Lagarias, Lagarias–Li GL(N), Sekatskii, Lagarias §4 $\tau_n$, Sekatskii Theorems 2/3, Lagarias §5 $S_\infty$, Lagarias §7 $F_\pi$, Hardy–Littlewood 1918.

### Class B — Places side (Connes-style, 6 evidence)
6, 8, 9, 10, 15, 18 — Pratt–Robles §6, Polymath15 $H_t$, Connes 1999 §VI, Connes–Consani 2021 §1, Lagarias §6 $S_f$, Robin / Lagarias 2002.

### Class C — Hybrid (3 evidence)
11, 12, 19 — Iwaniec–Sarnak §5 family, Rodgers–Tao 2020 $\Lambda \geq 0$, Burnol.

### 5 paper-direct tissue isomorphisms

1. **Lagarias §3 ↔ Connes 1999 §VI** — Mellin-transform 좌표 duality. Anchor: Lagarias §3 page 12 ("Burnol viewpoint") + Connes §VI page 27 ("Weil [W3] synthesis of explicit formulas for all L-functions").
2. **Bombieri–Lagarias $\lambda_n$ ↔ Connes §VI eq (17)** — Positivity criterion 동일 form, 좌표 다름.
3. **Voros §3 secondary zeta ↔ Lagarias §4 $\tau_n$ Hurwitz** — Nontrivial zero power sum vs trivial zero archimedean.
4. **Pratt–Robles §6 $A^{(1,1)}$ ↔ Connes–Consani $QW_\lambda$** — Finite primes contribution, prime-by-prime sensitive.
5. **Polymath15 $H_t$ ↔ Rodgers–Tao zero dynamics** — Forward ↔ backward heat. 결합: $0 \leq \Lambda \leq 0.2$.

19 중 13 mapped, 6 missing. Layer 1에서 missing 6은 research candidates로 명시:

- (11) Iwaniec–Sarnak family ↔ Lagarias–Li $\mathrm{GL}(N)$ automorphic single (family ↔ single, paper-direct 부재).
- (17) Hardy–Littlewood 1918 ↔ Lagarias–Li zeros sum form (paper-direct mapping 부재).
- (18) Robin $\sigma(n)$ ↔ Connes–Consani $QW_\lambda$ (number-theoretic vs quadratic form 연결 부재).
- 그 외 cross-class connections.

## 4. Cycle 5 — path 1 measurable progress (Connes–Consani 2018 → 2021)

프로젝트 초기에 "positivity unification"은 catalogue 후 dormant 상태. Cycle 5 (attempt 188)이 paper-direct movement 발견.

**2018 still-open** (1805.10501, page 2, paper-direct):

> *"In the process to formulate a Riemann–Roch theorem on the square of the Scaling Site one faces a substantial difficulty. The problem, which is still open at this time, has to do with an appropriate definition of the sheaf cohomology (as idempotent monoid) $H^1$ ..."*

**2020/2021 bridging** (2006.13771, page 3):

> *"This paper is motivated by the desire to understand the link between the analytic Hilbert space theoretic strategy first proposed in [11], and the geometric approach pursued in the joint work of the two authors. ... **The first contribution of this paper is to make explicit the relation between the two approaches, thus overcoming the above problem.**"*

**Theorem 1 (paper page 3, paper-direct)**:

> *"Let $g \in C_c^\infty(\mathbb{R}_+^\times)$ have support in the interval $[2^{-1/2}, 2^{1/2}]$ and Fourier transform vanishing at $i/2$ and $0$. Then one has $W_\infty(g \ast g^*) \geq \mathrm{Tr}(\vartheta(g) S\, \vartheta(g)^*).$"*

**Corollary 2 (RH-equivalent inequality)**:

$$c|\hat g(0)|^2 + \sum_{s \in S} \hat g(s)\,\hat g(\bar s) \geq \mathrm{Tr}(\vartheta(g) S\, \vartheta(g)^*),$$

$Z = 1/2 + iS$ = nontrivial zeros multiset.

**Honest scope** (paper §abstract self-quote): *"All the ingredients and tools used above make sense in the general semi-local case, where Weil positivity implies RH"* — 즉, **single-archimedean case**만 완료, general semi-local case 여전히 open.

## 5. Cycle 14 — Morishita 2026 external bridge

Cycle 14 (attempt 197)이 동일 cluster에 2026 paper 추가.

**Morishita 2026 (arxiv 2508.15971), page 2**:

> *"Although both Deninger's foliated dynamical systems and Connes–Consani's adelic spaces have the structures of foliation and dynamical system, their approaches seem deeply different. ... Their relation has been unknown for a long time."*

**Theorem 3.6 (paper-direct)**:

> *"Deninger's map gives rise to a continuous map from his foliated dynamical systems associated to abelian extensions of $\mathbb{Q}$ to Connes–Consani's adelic spaces such that it is Galois-equivariant and flow-anti-equivariant; in particular, **closed orbits attached to primes in both spaces are corresponding**."*

**Arithmetic linking homomorphism (paper-direct)**:
$$\mathrm{lk}_p : p^{\hat{\mathbb{Z}}} \to \hat{\mathbb{Z}}_{(p)}^\times := \prod_{q \neq p} \mathbb{Z}_q^\times.$$

따라서 Sub-Direction A (Connes–Consani arithmetic site) sequence:

$$2014 \to 2018\ (\text{still open}) \to 2022 \to 2024 \to 2026\ \text{(Morishita)}$$

— 수년 단위 paper accumulation, *active continuation*. H¹ cohomology component은 Connes–Consani 2018 자기 인정 still-open. 직접 RH 진전: 여전히 **0**.

## 6. Honest limits

Lemma 파일 자체 caveat block (`lemmas/positivity_unification_hypothesis.md`):

> *"Formal mapping only. 수학적 동치 X. Speculation 단계; proof candidate 아님. Connes / Deninger / Bombieri program이 정확히 이 unification — 그들도 미해결."*

본 lemma의 *유용한* 점:
- 새 RH-equivalent positivity claim 읽을 때 참조 ledger ("19 line 중 어느 것의 재기술인가?").
- 6 missing tissue isomorphism이 concrete, paper-direct, falsifiable research items.
- Cycle 5의 measurable cross-paper 움직임 (2018 → 2021) 기록.

본 lemma의 *아닌* 점:
- 증명, proof sketch, proof strategy 아님.
- Unification 이 작동한다는 claim 아님. 특정 pair 사이의 *형식적* mapping 만.
- Connes program 성공 여부 평가 아님 — out of scope.

## 7. Cross-references

- Spectral candidate audit (axiom 6 strict, 11/11 universal NO): [Lemma 9](../12-lemma-axiom6-ceiling/)
- Wall #2 unconditional bound audit (4/4 universal NO): [Lemma 10](../13-lemma-wall2-axiom-alpha/)
- Spectral candidate critical-reading template: [Lemma 1](../14-lemma-spectral-circularity-check/)
- Connes–Consani 2018 → 2021 progress: [Finding 3](../04-finding-connes-consani-progress/)
- Numerical evidence (Voros, Lagarias σⱼ, Mertens, Wigner): [Numerical evidence](../17-numerical-evidence/)

## 8. Audit trail (Layer 1)

- `lemmas/positivity_unification_hypothesis.md` — full source (Cycles 3–6 + 14 까지 확장).
- `attempts/056` (Lagarias §3), `103` (Voros §3), `104–106` (Pratt–Robles, Lagarias §4, Polymath15), `108` (Connes 1999 §VI), `111–117` (Connes–Consani 2021, Iwaniec–Sarnak, Rodgers–Tao, Sekatskii, Lagarias §5/§6/§7), `122` (Conrey 2003 catalogue), `137` (tissue isomorphism analysis), `186–189` (Cycles 3–6), `197` (Cycle 14 Morishita 2026).
- `lemmas/dont_try_directions.md` Cut 6 — *"positivity criterion alone → RH"* explicit cut.

---

[← 이전: Numerical evidence](../17-numerical-evidence/) · [English](../../../en/posts/18-lemma-positivity-unification/) · [전체 한국어 포스트](../../)
