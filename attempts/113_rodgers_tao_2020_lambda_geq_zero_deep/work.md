# Work — Attempt 113 (Rodgers-Tao 2020 Λ ≥ 0 §1-§2 DEEP)

## 1. Paper section deep read

### §1 Introduction (paper-direct, eqs 1-4)

**H_0** (eq 1): H_0(z) = (1/8) ξ(1/2 + iz/2). 
- ξ Riemann xi (eq 2): ξ(s) = (s(s-1)/2) π^{-s/2} Γ(s/2) ζ(s).
- H_0 entire even, functional eq H_0(z̄) = H_0(z̄).
- RH ⟺ all zeros of H_0 are real.

**Fourier representation** (eq 3):
$$H_0(z) = \int_0^\infty \Phi(u) \cos(zu) du$$
$$\Phi(u) = \sum_{n=1}^\infty (2\pi^2 n^4 e^{9u} - 3\pi^2 n^2 e^{5u}) \exp(-\pi^2 n^2 e^{4u})$$
super-exponentially decaying, Φ(u) = Φ(-u) (Poisson summation).

**De Bruijn family** (eq 4):
$$H_t(z) = \int_0^\infty e^{tu^2} \Phi(u) \cos(zu) du$$
*backwards* heat flow ∂_t H_t = -∂_zz H_t.

**Pólya 1926**: H_t purely real zeros for some t ⟹ H_{t'} purely real for all t' > t.
**De Bruijn 1950**: H_t purely real for t ≥ 1/2.
**Newman 1976**: -∞ < Λ ≤ 1/2, "RH true ⟺ Λ ≤ 0". Conjectured Λ ≥ 0: "if RH is true, it is only barely so".

**Table 1** (paper §1, paper-direct lower bound history):
| Λ ≥ | Date | Author |
|---|---|---|
| -∞ | 1976 | Newman |
| -50 | 1988 | Csordas-Norfolk-Varga |
| -5 | 1991 | te Riele |
| -0.385 | 1992 | Norfolk-Ruttan-Varga |
| -0.0991 | 1991 | Csordas-Ruttan-Varga |
| -4.379×10^{-6} | 1994 | Csordas-Smith-Varga |
| -5.895×10^{-9} | 1993 | Csordas-Odlyzko-Smith-Varga |
| -2.63×10^{-9} | 2000 | Odlyzko |
| -1.15×10^{-11} | 2011 | Saouter-Gourdon-Demichel |

→ paper-direct: 35년 동안 *0 미달* 만 — Newman conjecture *full proof* = Rodgers-Tao 2020.

**Theorem 1** (paper-direct): One has Λ ≥ 0.

### §1 Proof outline (paper-direct)

Assume Λ < 0 for contradiction.
1. *Repulsion phenomenon* (Csordas-Smith-Varga 1994): negative Λ ⟹ adjacent zeros of H_0 cannot be too close to other nearby zeros.
2. *Strengthened to local equilibrium*: Λ<0 ⟹ zeros 가 nearly always *arithmetic progression-like* locally, gaps stay close to global average gap.
3. *Contradict* Montgomery pair correlation (or Conrey-Ghosh-Goldston-Gonek-Heath-Brown estimate).

→ paper-direct: backwards heat flow + dynamics → contradicts known *non-arithmetic-progression* local distribution of ζ zeros.

### §1.5 Hamiltonian + gradient flow (paper-direct, eqs 5-6)

zeros of H_t (Λ < t ≤ 0) = (x_j(t))_{j ∈ ℤ*}, simple, real, symmetric.

**Gradient flow** (eq 5):
$$\partial_t x_k(t) = 2 \sum_{j \neq k} \frac{1}{x_k(t) - x_j(t)}$$
*Coulomb-like repulsion* (1D log-gas dynamics).

**Hamiltonian**:
$$\mathcal H(t) = \sum_{j,k: j \neq k} \log \frac{1}{|x_j(t) - x_k(t)|}$$

**Monotonicity** (eq 6):
$$\partial_t \mathcal H(t) = -4 E(t)$$
where:
$$E(t) = \sum_{j,k: j \neq k} \frac{1}{|x_j(t) - x_k(t)|^2}$$

**paper-direct quote** (paper §1.5 끝):
> "we are able to control integrated energies that resemble the quantities ∫_{Λ/2}^0 E(t) dt"

→ Wall #2 (FORWARD-TIME) paper-direct origin: ∫E(t)dt 의 *integrated bound* 가 paper §1.5 *핵심* + technical 어려움 source. *우리 wall taxonomy* 의 paper-direct 검증.

### §1 control 단계 (paper-direct)

**Riemann-von Mangoldt asymptotic** for H_t:
- t = 0 (classical): T/(4π) log(T/(4π)) - T/(4π) + O(log T).
- Λ < t ≤ 0 (paper §3): T/(4π) log T - T/(4π) + o(log² T) (down to length scale α ≍ log T).

**Lemma 4** (paper §2 outline):
$H_t(z) \ll \exp(-\pi x/8 + O_C(\log_+^2 x))$ for z = x - iκ log_+ x, 0 ≤ κ ≤ C, Λ < t ≤ 0.

**Tool**: saddle-point method + Stirling — same as Polymath15 §6 (attempt 106 paper-direct deep).

### §2 Lemma 4 (paper §2, eqs 7-9)

eq (7): H_t(z) ≪ exp(-πx/8 + O_C(log_+² x)).
eq (8): more precise H_t(z) = exp(-πx/8 + O_C(log_+² x)) for κ ≥ C'.
eq (9): H_t'/H_t(z) = (i/4) log(iz/(4π)) + O_C(log_+ x / x).

**paper §2 quote**:
> "The main tool used to prove these bounds is the saddle point method, in which various contour integrals are shifted until they resemble the integral for the Gamma function, to which the Stirling approximation may be applied."

→ paper-direct: Polymath15 §6 (attempt 106) 동일 도구 — saddle + Stirling.

## 2. Numerical 검증 (paper §1 Table 1 + H_0 (γ_1))

[numerical, dps=30]

paper §1 Table 1 의 *현재 SOTA*: Polymath15 (paper §1 footnote): Λ ≤ 0.22.

본 attempt 의 numerical light:
- H_0(γ_1) where γ_1 = 14.1347... = Im(first ζ zero):
  H_0(14.1347...) = (1/8) ξ(1/2 + i·14.1347.../2) = (1/8) ξ(1/2 + 7.067i).
  Wait — ξ(1/2 + iz/2) ⟹ z = 2γ ⟹ z = 28.27 의 H_0 zero.
- 즉 H_0 의 zero 들 = 2 γ_n (paper-direct).

(numerical 검증 시간 한계로 본 attempt 는 paper-direct quote 만)

paper §1 Table 1 *current SOTA*:
- Polymath15: Λ ≤ 0.22.
- Rodgers-Tao 2020: Λ ≥ 0.
- Combined: 0 ≤ Λ ≤ 0.22.
- *RH* ⟺ Λ ≤ 0 (Newman).
- *strict* Λ ≤ 0 미증명.

## 3. Wall taxonomy mapping

### Wall #2 (FORWARD-TIME) deep refinement — *paper-direct origin*

Rodgers-Tao 2020 §1.5 quote:
> "we are able to control integrated energies that resemble the quantities ∫_{Λ/2}^0 E(t) dt"

→ Wall #2 의 *paper-direct origin*:
- *Forward-time*: H_t for t > 0 의 zeros real (Polymath15 t = 0.22).
- *Backwards-time*: H_t for Λ < t ≤ 0 의 zeros 의 *local equilibrium*.
- *integrated energy* ∫_{Λ/2}^0 E(t) dt = paper §1.5 *핵심 도구*.
- *우리 wall taxonomy* 의 ∫E(t)dt = paper-direct origin (attempts 006, 012, 049 의 본 paper-direct).

### Wall #2 *quantitative* sharpening (Rodgers-Tao 2020 + Polymath15)

| Bound | Paper | Year |
|---|---|---|
| Λ ≤ 0.22 | Polymath15 | 2018 |
| Λ ≥ 0 | Rodgers-Tao | 2020 |
| Λ = 0 ⟺ "RH barely true" (Newman) | conjectured | 1976 |
| Λ < 0 | RH false |

paper-direct *gap*: 0 ≤ Λ ≤ 0.22, *strict equality* Λ = 0 *미증명*. RH ⟺ Λ ≤ 0.

→ Wall #2 *quantitative*: Λ ∈ [0, 0.22]. *closing the gap* = Wall #2 sharpening.

### Wall #4 cross-link — Montgomery pair correlation

paper §1 proof outline의 *contradiction* = Montgomery pair correlation. paper-direct:
> "this can be ruled out by the existing results on the local distribution of zeroes, such as pair correlation estimates of Montgomery [16]."

→ Wall #4 (CONSPIRACY) paper-direct cross-link: Λ ≥ 0 proof = *Montgomery pair correlation* assumed result. *Wall #4 가 indirect Wall #2 입증의 essential tool*.

### Wall #5 (FORWARD-TIME / SELF-ADJOINT-RIGOR) cross-link
paper §1.5 의 1D log-gas Hamiltonian 𝓗(t) = log gas. *spectral* interpretation 가능 (Calogero-Moser system 와 유사). 그러나 paper §1 footnote: "dynamics here are not Newtonian; (5) prescribes velocity, not acceleration".
- Wall #5 *partial cross-link*: log-gas Hamiltonian 의 self-adjoint extension X (gradient flow form).

## 4. Lemma 적용

### Lemma 3 (positivity_unification) 12th paper-direct evidence

Rodgers-Tao 2020 Theorem 1 = Λ ≥ 0:
- Λ = de Bruijn-Newman constant. Λ ≤ 0 ⟺ RH (Newman 1976).
- Λ ≥ 0 (paper-direct) — RH-conditional X, *unconditional*.
- *Λ ≥ 0* 자체가 *positivity*. Newman의 "barely true" — Λ = 0 시 boundary RH.

12. **Rodgers-Tao 2020 Theorem 1** (attempt 113): Λ ≥ 0 unconditional. Newman positivity의 *full proof*.

→ Lemma 3 의 12th evidence — *unconditional* (다른 evidence 들은 *conditional* mapping 만).

### Lemma 6 (dont_try_directions) Cut 1 paper-direct cross-check

본 attempt 가 *backwards heat* (Rodgers-Tao 2020) — *Otto's calculus forward heat* (attempt 007 Wasserstein) 와 *opposite direction*. attempt 007 의 *시간 대칭* X 가 paper-direct.

→ Cut 1 정정: backwards heat 의 *opposite direction* 이 paper-direct *time-reversibility 부재* 명시. *Wasserstein 시간대칭이 RH 와 무관* 이라는 attempt 007 의 결론이 본 attempt 의 paper-direct 검증.

### Lemma 4 (failed_proof_categories) cross-check
Rodgers-Tao 2020 = *successful proof* (Theorem 1). Lemma 4 (failed proof) 적용 X — *opposite case* (success).

본 attempt 의 *positive feature*: Rodgers-Tao 2020 = *paper-direct full proof* of Newman conjecture. paper §1 의 *35년 lower bound history* (Table 1) 의 *culmination*.

## 5. Cross-reference

- attempt 006 (forward heat optimal transport): partial Wall #2 refinement, ∫E(t)dt unconditional bound 부재.
- attempt 007 (Wasserstein evolution): negative — Wasserstein 시간대칭. 본 attempt 의 *opposite direction* paper-direct.
- attempt 012 (KL divergence path-dependent): positive — entropy forward/backward anti-symmetric.
- attempt 028 (Polymath15 skim): Wall #2 SOTA (Λ ≤ 0.22). 본 attempt = *opposite bound* (Λ ≥ 0).
- attempt 049 (heat flow simulation): forward heat simulation. paper §1 의 *backwards*.
- attempt 106 (Polymath15 §4-§6 deep): *forward* Λ ≤ 0.22 의 paper-direct deep.

→ attempts 028, 106 (Polymath15 forward) + 113 (Rodgers-Tao backwards) = Wall #2 의 *full quantitative bracket*: 0 ≤ Λ ≤ 0.22.

## 6. Open questions

(Q1) Λ = 0 *strict equality* 의 path?
- *알려진*: RH ⟺ Λ ≤ 0. 그러므로 Λ < 0 false ⟹ Λ ≥ 0 (Rodgers-Tao). Λ = 0 인지 Λ > 0 인지 *unknown* — RH 직접 결정.
- *Newman 추정*: Λ = 0. "barely true". 그러나 *direct proof* X.

(Q2) §1.5 의 ∫_{Λ/2}^0 E(t) dt *integrated energy bound* 의 sharpness?
- paper §1.5: log(1/|x_{j+1}(t) - x_j(t)|) ≪ log² j log log j. "far from optimal".
- *우리 contribution X*: 본 attempt 의 paper-direct citation 만.

(Q3) Generalized Newman conjecture (paper §1 Remark 3 + footnote 5)?
- Dobner 2020: Λ ≥ 0 *Riemann-Siegel approximation* 도구 — 본 paper의 heat equation 도구 unnecessary.
- Generalized Newman: forthcoming work, *significantly simpler proof* (paper §1 footnote 5).

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Rodgers-Tao 2020 §1-§2 paper-direct deep + Wall #2 paper-direct origin (∫E(t)dt) + Lemma 3 12th evidence.
- *우리 contribution*: paper §1 Table 1 historical bracket + Wall #2 full quantitative bracket (0 ≤ Λ ≤ 0.22) + Lemma 6 Cut 1 의 backwards-heat *paper-direct opposite direction* 검증.

## 8. Specialist Δ 추정 (Tao 본인)

### Tao 본인 추정
- "Rodgers-Tao 2020 = backwards heat flow analysis 의 *technical tour de force*. Polymath15 의 forward 와 *complementary*. 35년 lower bound 기록의 *full proof*."
- "그러나 *RH 자체 진전 X* — Λ = 0 strict equality 가 RH 와 등가. Λ ≥ 0 + Λ ≤ 0.22 의 *gap 0.22* 가 *Wall #2 quantitative* 한계."
- Tao sharp navigation: "본 paper의 *integrated energy* 도구는 *partial differential equations* 의 새 도구 — *Polymath16*-like community 시도가 *new technique* fundamental needed. ∫E(t)dt 의 *unconditional sharper bound* 가 30년 challenge — combinatorial 최적화로 닫히지 않음."

### *전문가처럼 사고* 노력 (Tao Wall #2 추정)
외부 critique #4 의 Tao 추정: "Λ ≤ 0.22 → 0 의 gap 은 combinatorial 최적화로 닫히지 않는 *fundamental obstacle*."
→ paper §1.5 ∫_{Λ/2}^0 E(t)dt + paper §3 down to length scale α ≍ log T = paper-direct *technical 어려움*. Tao 추정 답이 paper §1.5 quote ("far from optimal") 의 *paper-direct verification*.

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. Tao 직접 검증 X. 본 추정은 paper §1 Table 1 + §1.5 quote 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — Rodgers-Tao 2020 §1-§2 paper-direct deep + Wall #2 paper-direct origin + Lemma 3 12th evidence + Tao 추정 paper-direct 검증.
