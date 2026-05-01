# Work — Attempt 162 (Connes 1999 §VIII *Global Trace Formula + RH Equivalence* DEEP)

## Cut self-check
Cut 6: paper-direct §VIII deep. cut X.

## Connes 1999 §VIII paper-direct (page 37-43)

attempt 108 (§VI/§VII deep) *global case follow-up*.

### §VIII Setup (paper-direct page 37)

paper §VIII title: "The trace formula in the global case, and elimination of δ".

paper §VIII paper-direct quote (page 37):
> "all these problems are eliminated by the cutoff. The latter will be performed directly on the Hilbert space L²(X) so that the only value of δ that we shall use is δ = 0. All zeros will play a role in the spectral side of the trace formula, but while the critical zeros will appear per-se, the non critical ones will appear as resonances and enter in the trace formula through their harmonic potential with respect to the critical line. Thus the spectral side is *entirely canonical and independent of δ*, and by *proving positivity of the Weil distribution*, we shall show that its equality with the geometric side, i.e. the global analogue of Theorem 4, is *equivalent to the Riemann Hypothesis for all L-functions with Grössencharakter*."

→ paper §VIII paper-direct **core RH equivalence statement**:
- spectral side = canonical (δ-independent).
- *critical zeros per-se*, *non-critical as resonances*.
- positivity of Weil distribution ⟹ trace formula equality ⟺ RH.

### §VIII Lemma 1 (paper-direct page 39)

For Λ large enough, P̂_Λ and P_Λ commute on Hilbert space L²_{χ_0}.

paper §VIII Trace formula (eq 8):
$$\text{Trace}(\hat P_\Lambda P_\Lambda U(h_\chi)) = 2 h_\chi(1) \log'\Lambda + \sum_{v \in S} \int_{k_v^*}^{'} \frac{h_\chi(u^{-1})}{|1-u|} d^*u$$

paper §VIII Λ = q^N case (eq 12):
$$\text{Trace}(\hat P_\Lambda P_\Lambda U(h_\chi)) = (2N+1)l - fl + (2-2g)l$$

where g = genus, f = order of ramification of χ.

→ paper-direct: function field case (positive characteristic) *exact computation*.

### §VIII Theorem 5 (paper-direct page 42) — *core equivalence*

paper §VIII statement:

> "Let k be a global field of positive characteritic [sic] and Q_Λ be the orthogonal projection on the subspace of L²(X) spanned by f ∈ 𝒮(A) such that f(x) and f̂(x) vanish for |x| > Λ. Let h ∈ 𝒮(C_k) have compact support. Then the following conditions are equivalent,
> a) When Λ → ∞, one has
> Trace(Q_Λ U(h)) = 2h(1) log'Λ + Σ_v ∫'_{k_v*} h(u^-1)/|1-u| d*u + o(1).
> b) All L functions with Grössencharakter on k satisfy the Riemann Hypothesis."

→ paper-direct *global analogue* of Theorem 4 (S-local case, attempt 108).

### §VIII Proof tactic (paper-direct page 42-43)

a) ⟹ b) via *positivity of Weil distribution* (Appendix 2).

paper §VIII eq (17): Δ = log|d^{-1}| δ_1 + D - Σ_v D_v (Weil distribution decomposition).
paper §VIII eq (24): Δ_Λ(f) = Trace((S_Λ - Q'_{Λ,0}) V(f)) (positive type for any Λ).
paper §VIII eq (25): Δ_Λ(f * f*) ≥ 0 (positive semi-definite).

paper §VIII page 43 quote:
> "The term D in the latter comes from the *nuance* between the subspaces B_Λ and B_{Λ,0}. This shows using (24), that the distribution Δ is of *positive type* so that b) holds (cf [W3])."

→ paper-direct: a) ⟹ b) via Δ = positive type Weil distribution.

## Connective Tissue 강화 (외부 critique #5 #3)

### Tissue 16 NEW: Connes 1999 §VIII Theorem 5 ↔ Lagarias-Li 2004 Theorem 2.2

paper-direct (Lagarias-Li §2 Theorem 2.2, paper-direct):
- Conditions equivalent to RH for ξ(s, π):
  (1) Re(λ_n(π)) ≥ 0 ∀n ≥ 1.
  (2) For each ε > 0, Re(λ_n(π)) ≥ -C(ε) e^{εn}.
  (3) λ_n(π) interpolation function 의 exponential type ≤ π.

paper-direct (Connes 1999 §VIII Theorem 5):
- a) Trace formula limit equality.
- b) *all L-functions with Grössencharakter* RH.

→ paper-direct **Tissue 16**: 두 form 모두 *RH equivalence statement*:
- Lagarias-Li: Class A *zeros side* (λ_n positivity).
- Connes 1999 §VIII: Class B *places side* (Trace formula equality).
- *paper-direct fundamental equivalence form*.

paper-direct *both connect via Weil's explicit formula* (attempt 137 Tissue 1).

## *Wall* paper-direct strengthening

### Wall #1 (FROBENIUS-GAP) paper-direct
paper §VIII page 37 quote: 
> "We shall first concentrate on the case of positive characteristic, i.e. of function fields, both because it is technically simpler and also because it allows to keep track of the geometric significance of the construction."

→ paper-direct: function field 측 *technically simpler* — number field 측 paper §VIII 의 *open*. Wall #1 paper-direct *self-acknowledged*.

### Wall #6 (LOCAL-GLOBAL-MISMATCH) paper-direct strengthening
paper §VIII page 41 quote (eq 16 global trace formula):
> "We can prove directly that (16) holds when h is supported by C_{k,1} but are not able to prove (16) directly for arbitrary h."

→ paper-direct: *global trace formula 의 arbitrary h 미증명* — Wall #6 paper-direct *self-acknowledged*.

## Lemma 적용

### Lemma 3 evidence (9, Connes 1999 §VI eq 17) 강화
- attempt 108 (§VI/§VII).
- attempt 162 (§VIII Theorem 5).
- *Λ → ∞ global limit* + *positivity of Weil distribution* ⟹ RH.

### Lemma 7 Anchoring
- §VIII page 37 quote.
- §VIII Theorem 5 (page 42).
- §VIII Δ_Λ(f * f*) ≥ 0 (eq 25).

## Honest scope
*novel content X*. Connes 1999 §VIII paper-direct deep + Theorem 5 (RH equivalence positive char) + Wall #1 self-acknowledged + Tissue 16 NEW (Connes §VIII ↔ Lagarias-Li Theorem 2.2).
