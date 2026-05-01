# Work — Attempt 152 (Missing Tissue 18: Robin/Lagarias 2002 ↔ Connes-Consani QW_λ)

## Cut self-check
Cut 6: tissue mapping. cut X.

## Missing Tissue (18) — attempt 137 명시
> "(18) Robin σ(n) ↔ Connes-Consani QW_λ (number-theoretic vs quadratic form connection 부재)."

본 attempt = mapping 시도.

## paper-direct (2 papers)

### Robin/Lagarias 2002 (Conrey 2003, attempt 122):
RH ⟺ σ(n) ≤ H_n + exp(H_n) log H_n ∀n ≥ 1. equivalent Robin 1984: σ(n) < e^γ n log log n for n ≥ 5041.

σ(n) = Σ_{d | n} d (divisor sum).

### Connes-Consani 2021 §2 (attempt 111):
QW_λ on test functions f, g support [λ^-1, λ]:
QW(f, g) := Σ_{1/2 + is ∈ Z} f̄̃(s) ĝ(s).

paper §2.3: positivity 'sensitive' to *individual prime contribution* (e.g., p=2 sign change).

## Tissue 12 attempt mapping

### Direct?
- Robin: σ(n) — divisor function bound for *individual* n.
- Connes-Consani: QW_λ — quadratic form positivity for *all λ*.
- 직접 isomorphism *어렵다*.

### Indirect via *Mertens-type* link?

paper-direct (Conrey 2003 §Initial Ideas):
- Mertens conjecture |M(x)| ≤ √x ⟹ RH — *disproved* by Odlyzko-te Riele 1985.
- M(x) = Σ_{n ≤ x} μ(n) (Möbius).
- σ(n) ↔ μ(n) *Möbius pair* of multiplicative functions.

paper-direct: σ(n) Robin form ↔ M(x) Mertens form *via multiplicative function*.
- σ = Σ_{d|n} d = id * 1 (Dirichlet convolution).
- μ = (1)^{-1} Möbius inverse.
- σ * μ = id.

### Indirect via *Selberg trace formula* link?

paper-direct (Conrey 2003 §Selberg, attempt 122):
- Selberg trace formula: Σ h(r_j) = -h(0) - g(0) log(π/2) + ... + Σ_n Λ(n)/n g(2 log n) + Σ_P Σ_ℓ ...

→ Selberg trace = *primes side* Class B.
- Connes-Consani QW_λ = *primes restricted to p < λ²* (semi-local Selberg).

paper-direct: Robin σ(n) ↔ *not directly Connes-Consani QW_λ*. *both Class B places-side* but *different aggregation*:
- Robin: pointwise *upper bound* (n별).
- Connes-Consani: *integrated quadratic form*.

→ paper-direct **Tissue 12 partial mapping**: 두 form *same Class B*, *different aggregation* (pointwise vs integrated).

## Tissue 12 update

mapped 12/19, missing 2.

## Specialist Δ Anchoring (Lemma 7)
- Robin (Conrey 2003 §Some Other Equivalences) anchor.
- Connes-Consani §2.3 anchor: "positivity restored by adding the contribution of the prime 2".
- 두 form *both Class B*, *different aggregation* — paper-direct *partial mapping*.

## Honest scope
*novel content X*. Tissue 12 partial: Robin (pointwise) vs Connes-Consani (integrated) — same Class B, different aggregation.
