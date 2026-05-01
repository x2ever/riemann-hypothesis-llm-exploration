# Work — Attempt 110 (BBM 2017 Hamiltonian DEEP)

## 1. Paper section deep read

### §I Introduction (paper-direct)

5-page Letter (Bender-Brody-Müller 2017, *J. Phys. A* / arXiv:1608.03679).

**Main Hamiltonian (eq 1)**:
$$\hat H = \frac{1}{1 - e^{-i\hat p}}(\hat x \hat p + \hat p \hat x)(1 - e^{-i\hat p})$$

**Main findings (paper-direct quoted)**:
1. (i) *non-Hermitian* Ĥ formally satisfies Hilbert-Pólya conditions: ψ_n(0) = 0 ⟹ {(1 - iE_n)/2} are nontrivial zeros of ζ.
2. (ii) Classical limit Ĥ → 2xp (when x̂, p̂ commute) — Berry-Keating conjecture.
3. (iii) iĤ is *PT-symmetric* (modified — x̂, p̂ swap).
4. (iv) Pseudo-Hermitian: ⟨Ĥφ, ψ⟩ = ⟨φ, Ĥψ⟩ in alternative inner product (Hermitian).
5. (v) RH ⟺ eigenvalues nondegenerate; conversely if ζ zero off Re(z) = 1/2 then degenerate.

paper §I 끝 전 (이전 BK xp 의 한계): "such a Hamiltonian *has not been found*" up to BBM 2017.

### §II Δ̂ and Δ̂^{-1} (paper-direct)

Working with ℏ = 1, p̂ = -i ∂_x. e^{-ip̂} = shift operator (Taylor convergence radius > 1).

**Δ̂** (eq 2):
$$\hat\Delta f(x) = f(x) - f(x-1)$$
- annihilates unit-periodic functions — *no inverse* on smooth functions.
- *vanishing at infinity* class 에서는 Δ̂^{-1} 정의 가능.

**Δ̂^{-1}** (eq 3) via Bernoulli numbers:
$$\hat\Delta^{-1} f(x) = \frac{1}{i\hat p} \sum_{n=0}^\infty B_n \frac{(-i\hat p)^n}{n!} f(x)$$
B_1 = -1/2 convention. *Borel sum* of formal series.

### §II Eigenfunction derivation (paper-direct)

**Compute Δ̂^{-1} x^{-z}** via Bernoulli expansion + integral representation:
$$\hat\Delta^{-1} x^{-z} \sim \frac{\Gamma(2-z)}{1-z} \sum_{n=0}^\infty B_n \frac{(-1)^n}{n!} \frac{x^{1-z-n}}{\Gamma(2-z-n)}$$
(eq 4). Borel sum via Hankel contour:
$$\hat\Delta^{-1} x^{-z} = \frac{\Gamma(1-z)}{2\pi i} \int_C dt \frac{e^{xt} t^{z-1}}{1 - e^{-t}}$$
Negative of integral representation of *Hurwitz zeta function* ζ(z, x+1).

**Eigenfunction (paper-direct)**:
$$\psi_z(x) = -\zeta(z, x+1)$$
on positive half-line ℝ^+. Eigenvalue equation:
$$\hat H \psi_z(x) = \hat\Delta^{-1}(\hat x \hat p + \hat p \hat x) x^{-z} = i(2z - 1)\psi_z(x)$$

### §II Boundary condition (paper-direct)

ψ_z(0) = -ζ(z, 1) = -ζ(z). 
- BC ψ_z(0) = 0 ⟹ ζ(z) = 0 ⟹ z = z_n ∈ ζ zeros.
- E_n = i(2z_n - 1).
- Trivial zeros (z = -2n): ψ_z(x) = -B_{2n+1}(x+1)/(2n+1) — polynomial, *grows* as x → ∞ ⟹ NOT in domain.
- Nontrivial: |ψ_z(x)| ∼ x^{1-z}/(1-z) ⟹ subornean growth (sublinear).

→ paper-direct: *only nontrivial zeros* z_n = 1/2 - iE_n/2 contribute. RH ⟺ all E_n real.

### §III Pseudo-Hermiticity (paper-direct)

iĤ is PT-symmetric under modified PT: x̂ ↔ -p̂ (paper convention). 
- Berry-Keating quantization: ĥ^BK = x̂ p̂ + p̂ x̂, eigenstates ϕ_z^BK(x) = x^{-z}.
- ρ̂ = sin(p̂/2) similarity transform: ρ̂Ĥρ̂^{-1} = ĥ^BK.

**Hermitian adjoint** (eq 5):
$$\hat H^\dagger = (1 - e^{i\hat p})(\hat x \hat p + \hat p \hat x)\frac{1}{1 - e^{-i\hat p}}$$
**Metric** η̂ = sin²(p̂/2) — nonneg, bounded, Hermitian.
- pseudo-Hermitian: Ĥ^† = η̂ Ĥ η̂^{-1}.

### §III Biorthogonal states + RH equivalence (paper-direct)

ψ̃_n via Δ̂^† (forward difference operator). Inner product (eq 6):
$$\langle \tilde\psi_m | \psi_n \rangle = \int_0^\infty dx \, x^{-1 + i(E_n - \tilde E_m)/2}$$

- *If RH true* (Ē_m = E_m real): integral = 4πδ(E_n - E_m). Biorthogonal: ⟨ψ̃_m|ψ_n⟩ = 0 for m ≠ n.
- *If RH false* (some z_n with Re(z_n) ≠ 1/2): non-degeneracy fails. Self-orthogonality at exceptional points (Jordan block structures).

**RH equivalence (paper-direct)**:
- BC + completeness ⟹ ζ simple zeros equiv to RH (paper §III, ref [19]: Bui-Heath-Brown 2013, 19/27 simple).

### §III BBM 자체 인정 (paper-direct quotes)

> "We are *not able* to prove that the eigenvalues of Ĥ are real."
> "Identifying the domain of Ĥ remains a difficult and open problem."
> "Connection of this Hamiltonian to physical systems is *at best tenuous* because the eigenstates of Ĥ in our inner-product space are *not normalizable*."

→ paper-direct *self-honest* — Wall #5 의 *paper-direct origin*.

## 2. Numerical 검증

[numerical, dps=30, `tools/bbm_check2.py`]

### ψ_z(0) = -ζ(z) at first 5 ζ zeros

| n | γ_n | z_n = 1/2 + iγ_n | ψ_z(0) = -ζ(z_n) |
|---|---|---|---|
| 1 | 14.1347251417 | 1/2 + 14.13...i | -9.76e-32 + 6.13e-31i |
| 2 | 21.0220396388 | 1/2 + 21.02...i | 9.48e-32 + 4.23e-31i |
| 3 | 25.0108575801 | 1/2 + 25.01...i | 5.11e-31 - 1.47e-30i |
| 4 | 30.4248761259 | 1/2 + 30.42...i | -7.00e-31 - 1.18e-30i |
| 5 | 32.9350615877 | 1/2 + 32.94...i | 1.06e-30 - 1.64e-30i |

[rigorous]: machine precision *zero* (10^-30 level) — paper-direct boundary condition ψ_z(0) = -ζ(z) = 0 정확 검증.

### Eigenvalue E_n = i(2z_n - 1)

| n | E_n | Im E_n |
|---|---|---|
| 1 | -28.2694502834 | 0 (exact) |
| 2 | -42.0440792775 | 0 (exact) |
| 3 | -50.0217151603 | 0 (exact) |
| 4 | -60.8497522517 | 0 (exact) |
| 5 | -65.8701231755 | 0 (exact) |

[rigorous]: E_n = i(2(1/2 + iγ_n) - 1) = i(2iγ_n) = -2γ_n *real exactly* — by construction (assume RH).

→ *circular by construction*: 우리가 z_n = 1/2 + iγ_n 입력 ⟹ E_n real. 그러나 *paper 의 자체 self-acknowledged wall*: 만약 RH 가 *false* 이면 E_n 가 *complex*. 즉 *eigenvalue real ⟺ RH* — 본 BBM 의 *target*.

### Trivial zero 검증 (z = -2, -4, -6)

| n | z = -2n | ψ_z(10) | ψ_z(100) |
|---|---|---|---|
| 1 | -2 | 385.000 | 3.38e+05 |
| 2 | -4 | 25333.000 | 2.05e+09 |
| 3 | -6 | 1978405.000 | 1.48e+13 |

[paper-direct]: trivial zero 의 ψ_z 가 x^{2n+1} 로 polynomial 발산 — paper §II 명시. *not in BBM Hilbert space domain*.

### η̂ inner product Mellin integral
paper §III eq (6) ⟨ψ̃_m | ψ_n⟩ = ∫_0^∞ x^{-1 + i(E_n - Ē_m)/2} dx.
- 본 numerical: time cost 다대 (시간 한계로 본 attempt 미실행).
- paper-direct *형식 argument* — RH 가정 하 distributional 4π δ(E_n - E_m).

## 3. Wall taxonomy mapping

### Wall #5 (SELF-ADJOINT-RIGOR) deep refinement — *paper-direct origin*

BBM 2017 paper의 *self-acknowledged 한계*:
1. "We are not able to prove that eigenvalues are real."
2. "Identifying the domain of Ĥ remains a difficult and open problem."
3. "Connection to physical systems at best tenuous — eigenstates not normalizable."

→ Wall #5 의 *완전한 paper-direct 검증*:
- ψ_z(0) = -ζ(z) → BC 가 *boundary condition = ζ zero condition*. attempt 010 의 Lemma 1 source.
- non-Hermitian Ĥ + alternative inner product η̂ = sin²(p̂/2) → *pseudo-Hermitian 형식 일치만*.
- BBM = paper §I 의 "associated Hilbert space" 명시 부재 — 본질적 self-adjoint 입증 미실행.

### Wall #5 의 *Sierra 2016 vs BBM 2017 비교* (paper-direct)

| Aspect | Sierra 2016 | BBM 2017 |
|---|---|---|
| H form | x(p + ℓ_p²/p) bounded | (1-e^{-ip})^{-1}(xp+px)(1-e^{-ip}) non-local |
| Self-adjoint | extension via ϑ ∈ [0,2π) | non-Hermitian + pseudo-Hermitian metric |
| Spectrum | eq (5.14) Bessel K | E_n = i(2z_n-1), z_n ∈ ζ zeros |
| Circular? | partial (V boundary) | full (ψ_z(0) = -ζ(z)) |
| RH equivalent? | ϑ=π fine-tune | E_n real ⟺ RH |
| Self-acknowledged limit | "not single H for all zeros" | "not able to prove E_n real" |

→ 두 paper 모두 *self-honest*. Wall #5 *paper-direct origin* 양쪽 명시.

### Lemma 1 (spectral_candidate_circularity_check) 6단계 — BBM 2017 paper-direct full check

1. *D 의 spectrum이 ζ 의 zeros 에 *exact* equal*? **YES** — by boundary condition ψ_z(0) = -ζ(z) = 0.
2. *Hamiltonian 의 정의 자체에 ζ 가*? **YES indirectly** — Δ̂^{-1} 의 Bernoulli expansion 이 Hurwitz zeta 와 직접. ψ_z(x) = -ζ(z, x+1).
3. *self-adjoint 입증 부재*? **YES** — paper §III 자체 인정.
4. *Frobenius gap 메우는 trace formula 부재*? **YES** — 본 paper 자체 X.
5. *single H 가 모든 prime 보는 부재*? **PARTIAL** — paper §III Discussion 끝: "expectation value of x̂p̂^{-1}x̂ in renormalized state ψ_n gives leading term in counting prime numbers smaller than Λ" — *very partial* prime visibility.
6. *number field Lefschetz analogue 부재*? **YES** — paper-direct.

→ Lemma 1 의 6단계 *paper-direct full check*: BBM 이 (1, 2, 3) 정확 yes (*circular by construction* + *self-adjoint 미증명*). (5) partial.

### Wall #1 cross-link (paper-direct)

BBM Discussion 끝 의 *prime counting* claim (Λ/log Λ) — *partial* Wall #1 (Frobenius gap) 우회 시도. 그러나 *exact prime distribution* X — *only leading term*.

## 4. Lemma 적용

### Lemma 1 (spectral_candidate_circularity_check) — 6단계 paper-direct full check 위.

본 attempt 가 Lemma 1 의 *paper-direct origin* 검증. attempt 010 의 lens 가 BBM 2017 paper §I-III 에서 *direct quoted form* 으로 검증.

### Lemma 6 (dont_try_directions) Cut 5 paper-direct citation

본 attempt 의 BBM paper §I quote ("not able to prove eigenvalues real") + Sierra 2016 §I quote ("not able to find single Hamiltonian") 가 Cut 5 의 *direct paper citation*.

→ Cut 5 가 *우리 자체 관찰* 만이 아니라 *paper-direct quote* 기반 — strengthened.

### Lemma 4 (failed_proof_categories)

BBM 2017 = *failed proof X*. paper 자체가 *self-honest* about limitations. Lemma 4 적용 N/A.

## 5. Cross-reference

- attempt 010 (BBM truncation): 본 attempt 가 deep paper-direct. ψ_z(0) = -ζ(z) 의 numerical 정확 검증 (10^-30 level).
- attempt 029, 030, 109 (Sierra 2016): non-Hermitian 시도 + self-adjoint extension 비교.
- attempt 108 (Connes 1999 §VI/VII): "not quantization but L²(X) passage" — BBM quantization approach 와 명시적 distinction.
- attempt 100 milestone: BBM paper 자체가 Wall #5 의 *self-acknowledged origin*.

## 6. Open questions

(Q1) BBM paper §III Discussion 끝 의 "prime counting" claim 의 *quantitative* 검증?
- 본 attempt 시간 한계.
- paper-direct *partial* — only leading term.
- specialist (Connes/BBM) 추정: "이건 *paper level* claim 이지 *증명* X. exact prime distribution 부재 = Wall #1 partial".

(Q2) BBM η̂ = sin²(p̂/2) 의 *Hilbert space 의 정확한 정의*?
- paper §III 미해결.
- Mellin transform 과의 *naturally* 일치 여부.

(Q3) BBM PT-symmetric *broken phase* 가 RH false case 의 *physical signature*?
- paper §III: "If iĤ has *maximally broken* PT symmetry then eigenvalues are pure-imaginary complex-conjugate pairs, RH follows."
- *broken phase 의 unconditional 검증*은 BBM paper level 자체 X.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. BBM 2017 paper-direct re-paraphrase + ψ_z(0) numerical 정확 검증 (10^-30 level) + Lemma 1 6단계 paper-direct full check.
- *우리 contribution*: BBM paper §I/§III self-acknowledged quotes 의 *paper-direct citation* 으로 Wall #5 origin 명시 + Sierra 2016 vs BBM 2017 비교 + Lemma 1 의 (1, 2, 3) yes 명시.

## 8. Specialist Δ 추정 (Connes / BBM 본인)

### Connes 본인 추정
- "BBM 2017 = quantization approach. 1999 §VI 끝에서 거부한 path. 그러나 *PT-symmetric* approach 가 *novel* — 그러나 *RH 진전 X*. eigenstates not normalizable + domain unclear = *self-adjoint rigor 미해결*. self-adjoint 가 입증되면 RH 따름 — 그러나 *입증 부재* 가 본질적 wall."
- Connes navigation: "paper-direct *partial prime counting* 이 *Connes-Consani 의 arithmetic site* 의 *quantization 시도*. 그러나 spectral interpretation 자연 등장 X — Connes 1999 §VI 의 'not quantization' 명시 vs BBM 의 quantization 직접 충돌."

### BBM 본인 추정
- "paper §III 의 *self-acknowledged* limitations 가 honest. 'not able to prove E_n real' = paper-direct. *RH equivalent reformulation* 만, *증명 X*."
- BBM navigation: "domain identification + self-adjoint rigorous proof = next 30 년 challenge. PT-symmetric extension theory 의 progress = potential path. 그러나 5 paragraphs Letter 의 *수학적 framework* 만, *physics rigor* 부재."

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. BBM paper §III 끝 quote + Connes 1999 §VI 끝 quote 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — BBM 2017 paper-direct deep + Lemma 1 6단계 paper-direct full check + Wall #5 self-acknowledged origin 명시.
