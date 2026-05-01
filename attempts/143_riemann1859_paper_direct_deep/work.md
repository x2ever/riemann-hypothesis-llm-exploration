# Work — Attempt 143 (Riemann 1859 *Originating Source* DEEP)

## Cut self-check
Cut 6: paper-direct *historical originating source*. cut X.

## 1. paper deep read (paper-direct)

Riemann 1859, "Über die Anzahl der Primzahlen unter einer gegebenen Grösse" (Wilkins 영역 1998). 8 pages, *RH 의 originating paper*.

### §1 Euler product → analytic continuation (paper-direct)

paper page 1:
- Euler: Π_p 1/(1 - 1/p^s) = Σ_n 1/n^s = ζ(s) (Re s > 1).
- ∫₀^∞ e^{-nx} x^{s-1} dx = Π(s-1)/n^s.
- ⟹ Π(s-1) ζ(s) = ∫₀^∞ x^{s-1}/(e^x - 1) dx.

### §2 Contour integral + functional equation (paper page 2)

contour ∫_∞^∞ (-x)^{s-1}/(e^x - 1) dx (positive sense around 0).
- 2 sin πs Π(s-1) ζ(s) = i ∫_∞^∞ (-x)^{s-1}/(e^x - 1) dx.
- Residue calculus: 2 sin πs Π(s-1) ζ(s) = (2π)^s Σ_n n^{s-1} ((-i)^{s-1} + i^{s-1}).
- → **functional equation**: 2 sin πs Π(s-1) ζ(s) = (2π)^s [(-i)^{s-1} + i^{s-1}] ζ(1-s).
- Π(s/2 - 1) π^{-s/2} ζ(s) *unchanged* under s → 1-s (paper-direct page 2 끝).

### §3 ξ(t) symmetric form (paper page 3)

s = 1/2 + ti. Define:
$$\xi(t) := \Pi(s/2)(s-1) \pi^{-s/2} \zeta(s) \quad (\text{paper page 3})$$

ξ(t) entire, ξ(-t) = ξ(t) (real, even).

paper page 3:
$$\xi(t) = \frac{1}{2} - (tt + 1/4) \int_1^\infty \psi(x) x^{-3/4} \cos(\frac{1}{2} t \log x) dx$$

ψ(x) = Σ_{n=1}^∞ e^{-nnπx} (Jacobi theta function).
Functional equation 2 ψ(x) + 1 = x^{-1/2} (2 ψ(1/x) + 1) (paper-direct, Jacobi Fund. §184).

### §4 *Riemann Hypothesis statement* (paper page 4 quote, paper-direct)

> "The number of roots of ξ(t) = 0, whose real parts lie between 0 and T is approximately = T/(2π) log T/(2π) - T/(2π)."

(Riemann-von Mangoldt formula original.)

> "**One now finds indeed approximately this number of real roots within these limits, and it is *very probable* that all roots are real. Certainly one would wish for a stricter proof here; I have meanwhile *temporarily put aside the search for this after some fleeting futile attempts*, as it appears unnecessary for the next objective of my investigation.**"

→ *paper-direct* original *RH statement* by Riemann himself:
- "very probable that all roots are real" — **RH의 historical 출발점**.
- "stricter proof would be desired" — *Riemann himself acknowledged proof gap*.
- "**fleeting futile attempts**" — *Riemann himself acknowledged failed attempts*. **Lemma 4 (failed_proof_categories) historical 첫 case**.

### §5 log ξ(t) Hadamard product (paper page 4 끝)

paper page 4:
$$\log \xi(t) = \sum_\alpha \log\left(1 - \frac{tt}{\alpha\alpha}\right) + \log \xi(0)$$

α = roots of ξ(t) = 0.
- *infinite product* over zeros = Riemann's original (paper-direct).
- 후속 Hadamard 1893 product: ξ(s) = ξ(0) Π_ρ (1 - s/ρ) e^{s/ρ} (zeros) — generalization.

### §6 π(x) explicit formula (paper page 4-5)

f(x) = π(x) + (1/2) π(x^{1/2}) + (1/3) π(x^{1/3}) + ... + correction.

log ζ(s) = -Σ log(1 - p^{-s}) = Σ p^{-s} + (1/2) Σ p^{-2s} + ...

Riemann의 original *prime counting formula* via inverse Mellin transform of log ζ.

## 2. Connective Tissue (paper-direct *Originating Source*)

### Riemann 1859 = *Class A (zeros side) 의 historical source*

paper-direct: Riemann 1859 page 4 *log ξ(t) = Σ_α log(1 - tt/αα) + log ξ(0)* = **Hadamard product 의 prototype**. *zero-side decomposition* 의 출발점.

→ paper-direct **8 papers (attempt 137 Class A 10 evidence) 의 originating tissue**:
1. Lagarias §3: ⟨F, G⟩_{W(π)} = Σ_ρ F(ρ)̄G(1-ρ̄). *Riemann's Hadamard product 의 sesquilinear extension*.
2. Voros §3 (attempt 142): Z(σ) = Σ x_k^{-σ}, x_k = ρ(1-ρ). *Riemann's symmetrized Hadamard product 의 power sum*.
3. Bombieri-Lagarias λ_n = Σ_ρ [1-(1-1/ρ)^n]. *Riemann's zeros 의 Li 변환*.
4-5, 7, 13, 14, 16, 17 (Lagarias-Li, Sekatskii, Lagarias §4/§5/§7, Hardy-Littlewood) 모두 Riemann의 ξ(t) symmetric form 의 generalization.

### Riemann 1859 = *Class B (places side) 의 historical source*

paper page 1 Euler product = paper-direct Class B places side originating:
- log ζ(s) = -Σ log(1 - p^{-s}) (paper page 4) = primes side.
- Connes 1999 §VI Σ_v ∫_{k_v*} = adelic generalization (Tate's thesis 의 source).
- Pratt-Robles A^{(1,1)} = -Σ_p (log p/(p-1))² = paper-direct prime sum.
- Robin σ(n) = Σ_{d|n} d = number-theoretic divisor.

## 3. paper-direct *Wall* historical sources

### Wall #1 (FROBENIUS-GAP): *Riemann 1859 자체 자명 X*
- Riemann 1859 = number field 측 의 first formal treatment.
- *function field analogue* = Weil 1948 conjectures (generalization).
- Wall #1 의 *paper-direct historical* = Riemann 1859 의 *no Frobenius hint*.

### Wall #5 (SELF-ADJOINT-RIGOR): *Riemann 1859 zeros real*
- Riemann himself: "very probable that all roots are real".
- *Hilbert-Pólya conjecture*는 *zeros real* 의 *physical interpretation*. Riemann 1859 의 paper-direct 추측.

## 4. Specialist Δ Anchoring (Lemma 7)

### Riemann 본인 추정 (paper-direct anchored)
- "very probable that all roots are real" — paper page 4.
- "stricter proof would be desired; fleeting futile attempts" — paper page 4.
- "appears unnecessary for the next objective of my investigation" — paper page 4.
- → Riemann himself: *RH 가 진짜 RH 의 originating statement*. *failed attempts* explicitly acknowledged.

[Anchoring]: 본 quotes 가 paper page 4 제 6 paragraph 직접 인용.

### Conrey 추정 (외부 critique #4 paper-direct, attempt 122)
- Conrey 2003 §Initial Ideas: "Riemann gave an explicit formula for π(x) in terms of complex zeros ρ = β + iγ of ζ(s). It is not difficult to show that RH is equivalent to..."
- → paper-direct: Conrey 본인 *Riemann original RH statement* 인용.

## 5. Lemma 적용

### Lemma 4 (failed_proof_categories) historical 첫 case 추가

paper-direct: Riemann himself acknowledged "fleeting futile attempts" in his 1859 paper.
- 본 statement = *first historical record* of failed RH proof attempts.
- Lemma 4 의 5 categories 의 *prototype*: Riemann's own failed attempts before 1859 publication.

→ Lemma 4 *historical timeline*:
- 1859: Riemann himself (paper-direct quote).
- 1900s: Hardy-Littlewood, Selberg, Levinson, ...
- 1940s: Rademacher (false disproof).
- 2018: Atiyah (5 categories paper-direct enumeration).

### Lemma 3 (positivity_unification) Originating Source 추가

paper-direct: Riemann 1859 page 4 log ξ(t) = Σ log(1-tt/αα) + log ξ(0) = *paper-direct Class A originating source*.
- 19 evidence 의 historical *anchor point*.
- 본 paper 가 *모든 후속 zeros-side evidence 의 source*.

### Lemma 7 (Specialist Δ Anchoring) 적용
- Riemann original quote anchored.
- Conrey 2003 §Initial Ideas anchor.

## 6. paper-direct *Wall #6 self-acknowledged*

paper page 4 quote: "fleeting futile attempts; appears unnecessary for the next objective".
- *Riemann himself*: RH proof attempt *failed*, *postponed*.
- → **paper-direct historical proof of Wall #6 (LOCAL-GLOBAL-MISMATCH)**: Riemann himself unable to prove despite having all the tools.
- 후속 paper 가 *Riemann의 unfinished business*.

## 7. Honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Riemann 1859 paper-direct deep + *originating source* identification + Lemma 4 historical first case + Lemma 3 originating tissue.
- *우리 contribution*: paper-direct citation of Riemann's *acknowledged failed attempts* (Lemma 4 historical first) + Riemann의 Hadamard product *origin* of Class A zeros-side (Lemma 3 connective tissue).

## 8. *역사적 sequence map*

paper-direct *Riemann 1859 originating tissue*:

```
Riemann 1859 (originating)
  ├─ ξ(t) symmetric form
  │     └─ Class A (zeros side):
  │         ├─ Hadamard 1893 (product)
  │         ├─ Li 1997 (criterion)
  │         ├─ Bombieri-Lagarias 1999 (λ_n)
  │         ├─ Voros 2006 (secondary zeta)
  │         └─ Lagarias-Li 2004 (GL(N))
  │
  ├─ Euler product / log ζ
  │     └─ Class B (places side):
  │         ├─ von Mangoldt explicit formula
  │         ├─ Selberg trace formula
  │         ├─ Connes 1999 (adelic distributional)
  │         └─ Connes-Consani 2021 (semi-local QW_λ)
  │
  └─ N(T) Riemann-von Mangoldt
       └─ Class C (hybrid):
           ├─ Newman 1976 (Λ ≥ 0 conjecture)
           ├─ Polymath15 2018 (Λ ≤ 0.22)
           └─ Rodgers-Tao 2020 (Λ ≥ 0)
```

→ paper-direct: Riemann 1859 = *all 19 evidence 의 historical originating tissue*.

## "예상 가능 결과" self-check
yes — Riemann 1859 paper-direct deep + Lemma 4 historical first case (Riemann himself acknowledged failed attempts) + Lemma 3 originating tissue identification.
