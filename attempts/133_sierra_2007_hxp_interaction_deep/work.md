# Work — Attempt 133 (Sierra 2007 H=xp Interaction DEEP)

## 1. Paper section deep read

Sierra 2007, "H = xp with interaction and the Riemann zeros".

### §I Introduction (paper-direct context)

- Hilbert-Pólya: zeros of ζ = eigenvalues of self-adjoint operator.
- Selberg 1950s trace formula → Riemann explicit formula analogue.
- Montgomery 1973 → GUE pair correlation.
- Berry 1986 quantum chaos: zeros = chaotic Hamiltonian eigenvalues, primes label periodic orbits.
- Berry-Keating 1999: H = xp, semiclassical = Riemann smooth.
- Connes adelic: H = xp 의 다른 regularization → continuum spectrum + missing lines.
- Sierra previous [20]: Russian Doll BCS ↔ H = xp link.

paper §I quote (paper-direct):
> "Up to date, it is not known a Hamiltonian accomplishing the Hilbert-Pólya conjecture."

### §II Semiclassical 3 regularizations (paper-direct, Table 1)

Classical H = xp, trajectory x(t) = x_0 e^t, p(t) = p_0 e^{-t}.

| Type | Regularization | 𝒩(E) |
|---|---|---|
| **BK** | \|x\|>l_x, \|p\|>l_p | (E/2π)(log(E/2π) - 1) + 1 |
| **C** | \|x\|<Λ, \|p\|<Λ | (E/π) log Λ - (E/2π)(log(E/2π) - 1) |
| **S** | l_x < x < Λ | (E/2π) log(Λ/l_x) |

Riemann-von Mangoldt smooth: ⟨𝒩(E)⟩ ∼ (E/2π)(log(E/2π) - 1) + 7/8.

→ paper-direct: BK 일치 (smooth part). C 의 *missing* term -E/2π(log E/2π - 1) = "missing spectral lines". S diverges (continuum).

### §III H_0 = xp quantization (paper-direct, eqs 6-17)

- (eq 6) H_0 = (1/2)(xp + px) normal ordered, p = -iℏ d/dx.
- (eq 7) On x ≥ 0: H_0 = √x p √x = -iℏ √x (d/dx) √x.
- (eq 8) Symmetric on L²(a, b) iff iℏ[aψ*(a)φ(a) - bψ*(b)φ(b)] = 0.
- Von Neumann deficiency indices n_±:

| Type | (a, b) | (n_+, n_-) | Self-adjoint? |
|---|---|---|---|
| **BK** | (1, ∞) | (1, 0) | NO |
| **C** | (0, N) | (0, 1) | NO |
| **S** | (1, N) | (1, 1) | YES (U(1) extensions) |
| **T** | (0, ∞) | (0, 0) | YES (essentially) |

→ paper-direct: only S, T self-adjoint. S → *infinite SA extensions* parameterized by ϑ ∈ [0, 2π).

### §III S-regularization (1, N) eigenvalue (paper-direct, eqs 12-17)

Boundary condition (eq 12): 𝒟(H_{0,ϑ}) = {ψ : e^{iϑ}ψ(1) = √N ψ(N)}.

Eigenfunctions (eq 14): ψ_E(x) = C/x^{1/2 - iE/ℏ}, E ∈ ℝ.

Quantization (eq 16):
$$N^{iE/\hbar} = e^{i\vartheta} \implies E_n = \frac{2\pi\hbar}{\log N}(n + \vartheta/(2\pi))$$

→ *discrete spectrum* with level spacing 2πℏ/log N.

ϑ = π special case (eq 24):
$$E_n = \frac{2\pi\hbar}{\log N}(n + 1/2)$$
*symmetric pairs* {E_n, -E_n}. *hermitean antisymmetric*.

### §III B Inverse Hamiltonian 1/H_0 (paper-direct, eqs 18-24)

(eq 18) H_0^{-1}(x, x') = (i/2ℏ) sign(x-x')/√(xx').
- Schrödinger eq (19): (i/2ℏ) ∫ sign(x-x')/√(xx') ψ(x') dx' = E^{-1} ψ(x).
- Variable change φ(x) = ψ(x)/√x.
- Eigenvalue eq → x dφ/dx = (1 - iE/ℏ) φ.
- Solution: φ(x) = C/x^{1 - iE/ℏ}, ψ(x) = C/x^{1/2 - iE/ℏ}.

이건 H_0 의 same eigenvalues. H_0 와 1/H_0 *isospectral on negative side* — *paired* {E_n, -E_n}.

### §IV H_0 with interactions (paper-direct, eqs 25-33)

H = H_0 + V perturbation. Or 1/H = 1/H_0 + V'.

paper choose 1/H form (eq 27):
$$H_2^{-1}(x, x') = \frac{i}{2\hbar} \frac{\text{sign}(x-x') + a(x)b(x') - b(x)a(x')}{\sqrt{\epsilon(x)\epsilon(x')}}$$
a(x), b(x) real functions, ε(x) positive monotone.

H_2^{-1} = hermitean antisymmetric. *spectrum real symmetric around 0*.

Sl(2, ℝ) symmetry (eq 29-30): (a, b) → (αa+βb, γa+δb) invariance, αδ - βγ = 1.

### §V-VI Jost function + Riemann zeros 점근 (paper §V-§VI not shown in pages 1-7, but abstract):

paper abstract (paper-direct):
> "We find potentials for which the resonances converge asymptotically toward the average position of the Riemann zeros."

→ paper-direct: *asymptotic convergence* 만. *exact* 부재.

paper abstract continuation:
> "Furthermore, a linear superposition of them, obtained by the action of integer dilations, yields a Jost function whose real part vanishes at the Riemann zeros and whose imaginary part resembles the one of the zeta function."

→ paper-direct: linear superposition + integer dilations 의 *Jost function*: real part vanishes at Riemann zeros. *paper-direct construction-by-dilation* — Lemma 1 (1) borderline.

### §VI 끝 paper-direct *self-acknowledgment* (paper abstract):
> "Our results suggest the *existence* of a quantum mechanical model where the Riemann zeros would make a point like spectrum embedded in the continuum."
> "The associated spectral interpretation would *resolve the emission/absorption debate* between Berry-Keating and Connes."

→ paper-direct *suggest*, *not proof*. Wall #5 paper-direct.

## 2. Lemma 1 6단계 paper-direct check (Sierra 2007 H_2 model)

1. *spectrum = ζ zeros exact*? **NO** — *asymptotic convergence* (paper abstract). Linear superposition Jost function의 *real part vanishes* at zeros — *zero-finding by construction*.
2. *def w/ ζ*? **PARTIAL** — V (a, b) functions free; *Jost function 의 dilation superposition* 자체 ζ-independent. 그러나 *resonance convergence* 의 paper-direct *fine-tune* 가능성.
3. *self-adjoint*? **YES** (S-regularization (1, N), n_± = (1, 1) U(1) extensions).
4. *Frobenius gap*? **NO**.
5. *single H prime*? **NO** — H_2 single Hamiltonian 그러나 prime *direct visibility* 부재.
6. *number field Lefschetz*? **NO**.

→ paper-direct: (1, 2) NO/PARTIAL + (3) YES + (4-6) NO. **less circular than BBM, more circular than Connes-Consani 2021**.

### Lemma 1 표 update (~attempt 133)

| Candidate | (1) spec=ζ | (2) def w/ ζ | (3) self-adj | (4-6) |
|---|---|---|---|---|
| BBM 2017 | YES | YES | NO | NO |
| Sierra §III/§V | NO | NO | YES | NO |
| **Sierra 2007 H_2** | **NO** (asymptotic) | **PARTIAL** | **YES** | NO |
| Connes-Consani 2021 | NO (special λ) | NO | YES | PARTIAL |
| Lagarias §8 (1) | YES | YES | *issue* | NO |

Sierra 2007 = *intermediate* circularity.

## 3. Wall taxonomy mapping

### Wall #5 (SELF-ADJOINT-RIGOR) deep refinement
- Sierra 2007 paper-direct *self-adjoint via deficiency index* (1, 1) — *paper-rigorous*.
- 그러나 *spectrum = ζ zeros 부재* (asymptotic only) → Wall #5 *paper-direct partial*.

### Wall #4 (CONSPIRACY) cross-link
- §I Russian Doll BCS link [20]: H = xp ↔ superconductivity model.
- *cross-domain* cross-link (paper-direct).

### Wall #1 (FROBENIUS-GAP) cross-link  
- §I "Hamiltonian conjectured by Berry-Keating": Selberg trace formula analogue.
- *function field Selberg* 의 *number field analogue* attempt.

## 4. Lemma 적용

### Lemma 1 6단계 paper-direct check 강화 (위)

### Lemma 6 (dont_try_directions) Cut 5 paper-direct cross-check
Sierra 2007 = paper-rigorous *less circular* (1, 2) NO/PARTIAL. 그러나 *exact spectrum X* (asymptotic only). Cut 5 paper-direct partial.

### Lemma 4 (failed_proof_categories) cross-check
Sierra 2007 = *successful incremental construction* (Russian Doll link, Jost function). Lemma 4 N/A.

## 5. Cross-reference

- attempt 010 (BBM truncation): Lemma 1 source.
- attempt 029, 030 (Sierra 2016 partial): lemma step 6 검증.
- attempt 109 (Sierra 2016 §I-V deep): self-adjoint extension.
- attempt 110 (BBM 2017 deep): ψ_z(0) = -ζ(z) circular.
- attempt 111 (Connes-Consani 2021 deep): least circular.
- 본 attempt 133 = Sierra 2007 paper-direct deep, intermediate circularity.

## 6. Open questions

(Q1) §V-§VI (page 8+) Jost function 의 *dilation superposition* 자세 form?
- 우리 본 attempt scope (pages 1-7) 외.
- *partial circularity* (linear superposition + integer dilations 가 ζ-data 함의 가능성).

(Q2) Russian Doll BCS [20] cross-link 의 *physical interpretation*?
- paper §I 끝 quote *별도 paper for separate work*.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Sierra 2007 paper-direct deep + Lemma 1 6단계 paper-direct check 강화 (intermediate circularity).
- *우리 contribution*: paper-direct mapping + Lemma 1 표 update + Wall #5 paper-direct partial 명시.

## 8. Specialist Δ 추정 (Sierra/Connes)

### Sierra 본인 추정
- "본 paper §VI = *resonance convergence asymptotic*. *exact spectrum X*. 다음 paper (2016 [§VI 이후]) 가 *transfer matrix + prime mirrors* 로 ad-hoc fine-tune."
- "Russian Doll BCS link = *physical interpretation* 만, *RH 진전 X*."

### Connes 추정 (외부 critique #4)
- "Sierra 2007 H_2 interaction = *quantization* path — Connes 1999 §VI 끝 'not quantization but L²(X)' 와 다름."
- "*asymptotic convergence* 만, *Wall #5 fundamental limit*."

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. paper §I + §VI abstract paper-direct citation 기반.

## "예상 가능 결과" self-check
yes — Sierra 2007 paper-direct deep + Lemma 1 표 update (Sierra 2007 intermediate circularity).
