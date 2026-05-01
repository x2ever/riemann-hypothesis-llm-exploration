---
title: "Lemma 3 — Positivity unification hypothesis (19 paper-direct evidence ladder)"
parent: English
nav_order: 18
date: 2026-05-02
---

# Lemma 3 — Positivity unification hypothesis (19 paper-direct evidence ladder)

[← All English posts](../../) · [한국어](../../../ko/posts/18-lemma-positivity-unification/) · *2026-05-02*

> **Not a proof.** This post documents a *speculative process lemma*: an empirical observation that almost every RH-equivalent statement the project has read in the literature contains a *positivity component*, and that these components admit *formal* (not mathematical) cross-mappings. The project's own audit explicitly tags this as *"hypothesis / synthesis record — proven X, formal mapping only"*.
>
> Read this as: a bookkeeping artifact useful for *organising* the literature, not as evidence of a unifying mechanism. Connes / Deninger / Bombieri have spent decades on roughly this same intuition and the unification is still open.

## 1. The original statement (`lemmas/positivity_unification_hypothesis.md`, attempt 024)

The five "essential walls" identified in earlier cycles each carry a positivity component:

| Wall | Positivity component |
|---|---|
| #1 FROBENIUS-GAP | Rosati involution positivity (function field side, Iwaniec–Sarnak §3) |
| #2 FORWARD-TIME | Energy $E \geq 0$; *integrated* bound absent |
| #3 SHARP-CONSTANT | Mollifier Gram matrix positivity, sharp limit |
| #4 CONSPIRACY | Family separation positivity (Rankin–Selberg $\geq 0$) |
| #5 SELF-ADJOINT-RIGOR | Inner-product / metric positivity (BBM Hamiltonian) |

The unification *hypothesis* (paper-direct quote from the lemma file):

> *"5 essential walls all carry a positivity component. The unified source may be the number-field analogue of Rosati involution positivity (which works on the function-field side)."*

The lemma file then immediately disclaims:

> *"Formal mapping only — not mathematical equivalence. Speculation; not a proof candidate. Connes / Deninger / Bombieri programs are exactly this unification attempt — they too remain open."*

## 2. The 19 paper-direct evidence ladder

What makes the lemma worth keeping in the project is not the unification claim — it is the *bookkeeping*: a literal ledger of 19 published RH-equivalent positivity statements, each anchored to a specific paper section. The full list (paper-direct, project attempt numbers in brackets):

1. **Lagarias §3** [att. 056] — Weil scalar product $\langle G_n, G_m\rangle = \lambda_n + \lambda_{-m} - \lambda_{n-m}$. Positivity ⇔ RH on $\mathrm{GL}(1)$.
2. **Voros §3** [att. 103] — Secondary zeta $Z(\sigma) = \sum x_k^{-\sigma}$, saddle-point asymptotic ⇒ tempered $\lambda_n \iff \mathrm{RH}$.
3. **Bombieri–Lagarias 1999** — $\lambda_n \geq 0 \iff \mathrm{RH}$ (Li 1997 generalisation).
4. **Lagarias–Li automorphic** [att. 026] — Li-equivalence = Weil positivity, $\mathrm{GL}(N)$ generalisation.
5. **Sekatskii** — Bombieri–Lagarias sharper form.
6. **Pratt–Robles §6** [att. 104] — $A^{(1,1)} = -\sum_p (\log p/(p-1))^2$ (sign-convention negative).
7. **Lagarias §4** [att. 105] — $\tau_n = (-1/2)^{n+1}\zeta(n+1, 1/2)$, Hurwitz form.
8. **Polymath15** [att. 106] — Newman positivity $\Lambda \geq 0$, $H_t$ = forward heat-flow zeros real.
9. **Connes 1999 §VI eq (17)** [att. 108] — $h(u) \geq 0 \Rightarrow$ Weil-distribution RHS positive ⇔ RH for all Grössencharacters of $k$.
10. **Connes–Consani 2021 §1–§2** [att. 111] — Semi-local Weil quadratic form $QW_\lambda$ positivity ⇔ RH. Quantitative (finite primes $< \lambda^2$); numerical ($\lambda^2 = 11$: smallest positive eigenvalue $2.389\times 10^{-48}$).
11. **Iwaniec–Sarnak Perspectives §5** [att. 112] (eqs 57, 58, 60, 62–64) — Family-wide positivity criterion. $L(1/2, F) \geq 0$ (self-dual + GRH). Mollification eq (62) $1/2 \to c > 1/2$ = Landau–Siegel lacuna (Sarnak's own quote).
12. **Rodgers–Tao 2020 Theorem 1** [att. 113] — $\Lambda \geq 0$ *unconditional*. Newman positivity with full proof; de Bruijn–Newman constant.
   - Combined with **Platt–Trudgian 2021 Corollary 2** [att. 132]: $\Lambda \leq 0.2$ (paper §3.4 via $H = 3\times 10^{12}$ + Polymath15 §6 Table 1 row 2). Therefore $0 \leq \Lambda \leq 0.2$.
13. **Sekatskii 2014 §2 Theorems 1, 2, 3** [att. 114] — Generalised Bombieri–Lagarias + generalised Li. *Family of parameter $a$* (any real $a \neq 1/2$). Quantitative form: positivity ⇔ exponential growth bound $c(\varepsilon)e^{\varepsilon n}$.
14. **Lagarias §5 Theorem 5.1** [att. 115] — $S_\infty(n, \pi) = (N/2) n \log n + C_1(\pi) n + O(N(K+1))$ *unconditional*. $C_1(\pi_{\mathrm{triv}}) \approx -1.130\,330\,7$, $\beta_\infty \approx 0.559\,774$, $\alpha_\infty \approx 0.443\,842$.
15. **Lagarias §6 Theorem 6.1** [att. 116] — $S_f(n, \pi) = \lambda_n(\sqrt n, \pi^\vee) + O(\sqrt n \log n)$. RH-conditional. *§5 + §6 combined*: $\lambda_n \sim (N/2) n \log n + C_1 n + O(\sqrt n \log n)$ assuming RH.
16. **Lagarias §7 Theorem 7.1** [att. 117] — $F_\pi(z)$ entire, order-1 exponential type, $F_\pi(n) = \lambda_n$. RH ⇔ exponential type $\leq \pi$, $|F_\pi(x)| \leq C(|x|+2)\log(|x|+2)$.
17. **Hardy–Littlewood 1918** (Conrey 2003 §Some Other Equivalences, [att. 122]):
   $$\mathrm{RH} \iff \sum_{k=1}^\infty \frac{(-x)^k}{k!\,\zeta(2k+1)} = O\!\left(x^{-1/4}\right)\ \text{as}\ x \to \infty.$$
18. **Lagarias 2002 / Robin** (Conrey 2003, [att. 122]) — $\mathrm{RH} \iff \sigma(n) \leq H_n + \exp(H_n)\log H_n\ \forall n$. Number-theoretic equivalence (divisor-function bound).
19. **Burnol bound** (Conrey 2003 §Functional Analysis, [att. 122]):
   $$d_N \geq \frac{1}{\log N}\sum_{\rho \text{ on line}} \frac{m_\rho^2}{|\rho|^2}.$$
   Equality ⇒ RH + simple zeros (Balazard–Saias variant).

**No new mathematics here.** Every line is a published paper-direct anchor. The project's contribution is the *catalogue*.

## 3. Tissue isomorphism class structure (attempt 137)

Under Weil's explicit-formula duality the 19 evidence split into three classes:

### Class A — Zeros side (Lagarias-style, 10 evidence)
1, 2, 3, 4, 5, 7, 13, 14, 16, 17 — Lagarias §3, Voros §3, Bombieri–Lagarias, Lagarias–Li GL(N), Sekatskii, Lagarias §4 $\tau_n$, Sekatskii Theorems 2/3, Lagarias §5 $S_\infty$, Lagarias §7 $F_\pi$, Hardy–Littlewood 1918.

### Class B — Places side (Connes-style, 6 evidence)
6, 8, 9, 10, 15, 18 — Pratt–Robles §6, Polymath15 $H_t$, Connes 1999 §VI, Connes–Consani 2021 §1, Lagarias §6 $S_f$, Robin / Lagarias 2002.

### Class C — Hybrid (3 evidence)
11, 12, 19 — Iwaniec–Sarnak §5 family, Rodgers–Tao 2020 $\Lambda \geq 0$, Burnol.

### 5 paper-direct tissue isomorphisms

1. **Lagarias §3 ↔ Connes 1999 §VI** — Mellin-transform coordinate duality. Anchors: Lagarias §3 page 12 ("Burnol viewpoint") + Connes §VI page 27 ("Weil [W3] synthesis of explicit formulas for all L-functions").
2. **Bombieri–Lagarias $\lambda_n$ ↔ Connes §VI eq (17)** — Identical positivity-criterion form, different coordinates.
3. **Voros §3 secondary zeta ↔ Lagarias §4 $\tau_n$ Hurwitz** — Nontrivial-zero power sum vs trivial-zero archimedean.
4. **Pratt–Robles §6 $A^{(1,1)}$ ↔ Connes–Consani $QW_\lambda$** — Finite-primes contribution, prime-by-prime sensitive.
5. **Polymath15 $H_t$ ↔ Rodgers–Tao zero dynamics** — Forward ↔ backward heat. Combined: $0 \leq \Lambda \leq 0.2$.

13 of 19 mapped, 6 missing. The missing six are listed in Layer 1 as research candidates:

- (11) Iwaniec–Sarnak family ↔ Lagarias–Li $\mathrm{GL}(N)$ automorphic single (family ↔ single, not made paper-direct).
- (17) Hardy–Littlewood 1918 ↔ Lagarias–Li zeros-sum form (no paper-direct mapping).
- (18) Robin $\sigma(n)$ ↔ Connes–Consani $QW_\lambda$ (number-theoretic vs quadratic-form connection absent).
- Remaining cross-class connections.

## 4. Cycle 5 — measurable progress on path 1 (Connes–Consani 2018 → 2021)

Earlier in the project, "positivity unification" had been catalogued and then sat dormant. Cycle 5 (attempt 188) found a *paper-direct movement* on it.

**2018 still-open** (1805.10501, page 2, paper-direct):

> *"In the process to formulate a Riemann–Roch theorem on the square of the Scaling Site one faces a substantial difficulty. The problem, which is still open at this time, has to do with an appropriate definition of the sheaf cohomology (as idempotent monoid) $H^1$ ..."*

**2020/2021 bridging** (2006.13771, page 3):

> *"This paper is motivated by the desire to understand the link between the analytic Hilbert space theoretic strategy first proposed in [11], and the geometric approach pursued in the joint work of the two authors. ... **The first contribution of this paper is to make explicit the relation between the two approaches, thus overcoming the above problem.**"*

**Theorem 1 (paper page 3, paper-direct)**:

> *"Let $g \in C_c^\infty(\mathbb{R}_+^\times)$ have support in the interval $[2^{-1/2}, 2^{1/2}]$ and Fourier transform vanishing at $i/2$ and $0$. Then one has $W_\infty(g \ast g^*) \geq \mathrm{Tr}(\vartheta(g) S\, \vartheta(g)^*).$"*

**Corollary 2 (RH-equivalent inequality)**:

$$c|\hat g(0)|^2 + \sum_{s \in S} \hat g(s)\,\hat g(\bar s) \geq \mathrm{Tr}(\vartheta(g) S\, \vartheta(g)^*),$$

where $Z = 1/2 + iS$ is the multiset of nontrivial zeros.

**Honest scope** (paper §abstract self-quote): *"All the ingredients and tools used above make sense in the general semi-local case, where Weil positivity implies RH"* — i.e., the **single-archimedean case** is the only one done; the general semi-local case remains open.

## 5. Cycle 14 — Morishita 2026 external bridge

Cycle 14 (attempt 197) added a 2026 paper to the same cluster.

**Morishita 2026 (arxiv 2508.15971), page 2**:

> *"Although both Deninger's foliated dynamical systems and Connes–Consani's adelic spaces have the structures of foliation and dynamical system, their approaches seem deeply different. ... Their relation has been unknown for a long time."*

**Theorem 3.6 (paper-direct)**:

> *"Deninger's map gives rise to a continuous map from his foliated dynamical systems associated to abelian extensions of $\mathbb{Q}$ to Connes–Consani's adelic spaces such that it is Galois-equivariant and flow-anti-equivariant; in particular, **closed orbits attached to primes in both spaces are corresponding**."*

**Arithmetic linking homomorphism (paper-direct)**:
$$\mathrm{lk}_p : p^{\hat{\mathbb{Z}}} \to \hat{\mathbb{Z}}_{(p)}^\times := \prod_{q \neq p} \mathbb{Z}_q^\times.$$

So the Sub-Direction A (Connes–Consani arithmetic site) sequence on file:

$$2014 \to 2018\ (\text{still open}) \to 2022 \to 2024 \to 2026\ \text{(Morishita)}$$

is one paper per few years — *active continuation*, not stagnation. The H¹ cohomology component remains open per Connes–Consani 2018's own admission. Direct RH progress: still **0**.

## 6. Honest limits

Quoting the lemma file's own caveat block (`lemmas/positivity_unification_hypothesis.md`):

> *"Formal mapping only. Not mathematical equivalence. Speculation stage; not a proof candidate. Connes / Deninger / Bombieri programs are exactly this unification — they too are unsolved."*

What this lemma is *good for*:
- A single ledger to consult when reading a new RH-equivalent positivity claim ("which of the 19 lines is this redescribing?").
- A target list of 6 missing tissue isomorphisms — concrete, paper-direct, falsifiable research items.
- Documentation of cycle 5's measurable cross-paper movement (2018 → 2021).

What this lemma is *not*:
- Not a proof, not a proof sketch, not a proof strategy.
- Not a claim that the unification works. Only that *formal* mappings exist between particular pairs.
- Not an evaluation of the Connes program's success — explicitly out of scope.

## 7. Cross-references

- Spectral candidate audit (axiom 6 strict, 11/11 universal NO): [Lemma 9](../12-lemma-axiom6-ceiling/)
- Wall #2 unconditional bound audit (4/4 universal NO): [Lemma 10](../13-lemma-wall2-axiom-alpha/)
- Spectral candidate critical-reading template: [Lemma 1](../14-lemma-spectral-circularity-check/)
- Connes–Consani 2018 → 2021 progress: [Finding 3](../04-finding-connes-consani-progress/)
- Numerical evidence (Voros, Lagarias σⱼ, Mertens, Wigner): [Numerical evidence](../17-numerical-evidence/)

## 8. Audit trail (Layer 1)

- `lemmas/positivity_unification_hypothesis.md` — full source (extends through Cycles 3–6 + 14).
- `attempts/056` (Lagarias §3), `103` (Voros §3), `104–106` (Pratt–Robles, Lagarias §4, Polymath15), `108` (Connes 1999 §VI), `111–117` (Connes–Consani 2021, Iwaniec–Sarnak, Rodgers–Tao, Sekatskii, Lagarias §5/§6/§7), `122` (Conrey 2003 catalogue), `137` (tissue isomorphism analysis), `186–189` (Cycles 3–6), `197` (Cycle 14 Morishita 2026).
- `lemmas/dont_try_directions.md` Cut 6 — *"positivity criterion alone → RH"* explicitly cut.

---

[← Previous: Numerical evidence](../17-numerical-evidence/) · [한국어](../../../ko/posts/18-lemma-positivity-unification/) · [All English posts](../../)
