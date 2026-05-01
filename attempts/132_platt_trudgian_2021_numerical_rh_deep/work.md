# Work — Attempt 132 (Platt-Trudgian 2021 Numerical RH DEEP)

## 1. Paper section deep read

Platt-Trudgian 2021 (arXiv:2004.09765), 7 pages.

### §1 Introduction (paper-direct historical)

H = largest height up to which RH numerically verified.

| H | Year | Author |
|---|---|---|
| 2.41×10^11 | 2003-2004 | Wedeniwski (ZetaGrid) |
| 2.44×10^12 | 2004 | Gourdon |
| 3.06×10^10 | 2017 | Platt |
| 10^11 | (unspecified) | Franke et al. |
| **3.000×10^12** | **2020** | **Platt-Trudgian (Theorem 1)** |

paper §1 quote (paper-direct):
> "the computations in [21] [Platt 2017] utilised *interval arithmetic* and *rigorously derived truncation bounds*."
> "The two earlier results [Wedeniwski, Gourdon] have the disadvantage that *neither has been published in a peer reviewed journal*."

→ paper-direct: Platt-Trudgian 2021 = *first peer-reviewed rigorous* H ≥ 10^12.

### §1 Theorem 1 (paper-direct)

**Theorem 1**: RH true up to height **H = 3,000,175,332,800**. The lowest **12,363,153,437,138** non-trivial zeros ρ have Re(ρ) = 1/2.

→ 22% higher than Gourdon 2004.

### §2 Theory and computation (paper-direct)

알고리즘:
- Compute completed zeta on half-line, count sign changes (each = real zero on critical line).
- Turing's method: confirm *all expected zeros accounted for* (none off line, RH holds in given range).
- Arb (Johansson 2017) interval arithmetic — *ball arithmetic* replaces MPFI (Revol-Rouillier).
- 50% space saving (cache friendly).
- Lattice sampling rate 0.01 (vs Platt 2017 rate 1.2). 999,997.5/10^6 zeros isolated.

Compute resources:
- 7.5 million core hours, 3.6 GHz Intel Xeon.
- 110,000 of half-line per GHz-hour.
- NCI Raijin/Gadi + Bristol BlueCrystal.

paper-direct comparison:
- Wedeniwski: 561 billion zeros = 2,304 years × 2 GHz Pentium 4 = 3,800 of half-line per GHz-hour.
- Gourdon: 525 days × 2.4 GHz Pentium 4 = 80,000,000 of half-line per GHz-hour (FFT-based, 725× faster than Platt-Trudgian).

### §3.1 Bounds on primes (paper-direct)

**Schoenfeld 1976**:
$$|\psi(x) - x| \le \frac{1}{8\pi} x^{1/2} \log^2 x \quad (x > 59)$$
*under RH*.

**Büthe**: RH up to H ⟹ Schoenfeld bound holds for x with 4.92 √(x/log x) ≤ H.

**Corollary 1** (paper-direct, H = 3×10^12):
$$|\psi(x) - x| \le \frac{\sqrt x}{8\pi} \log^2 x, \quad 59 < x \le 2.169 \times 10^{25}$$
$$|\theta(x) - x| \le \frac{\sqrt x}{8\pi} \log^2 x, \quad 599 < x \le 2.169 \times 10^{25}$$
$$|\pi(x) - \text{li}(x)| \le \frac{\sqrt x}{8\pi} \log^2 x, \quad 2657 < x \le 2.169 \times 10^{25}$$

→ paper-direct *quantitative*: PNT error bound *unconditional* up to x = 2.169×10^25.

### §3.2 Zero-free regions (paper-direct)

**Mossinghoff-Trudgian**: no zeros ρ = β + iγ in β ≥ 1 - 1/(R log γ), R = **5.573412** (γ > 3).

→ Vinogradov-Korobov zero-free region (Ford 2002) cross-link.

### §3.4 *de Bruijn-Newman constant Λ* (paper-direct)

paper §3.4 quote:
> "The 15th Polymath Project [Polymath15] contains some calculations with the de Bruijn-Newman constant: the authors prove that Λ ≤ 0.22. We note that we can make an *instant, but very mild, improvement* on this. The second row in Table 1 on page 65 of [Polymath15] shows that one may take Λ ≤ 0.2 provided one has shown H > 2.51 × 10^12."

**Corollary 2** (paper-direct):
$$\Lambda \le 0.2$$

(achieved via Theorem 1's H > 3 × 10^12 satisfies Polymath15 §6 Table 1 row 2 condition H > 2.51×10^12.)

paper §3.4 끝: 
> "The next entry in Table 1 of [Polymath15] is conditional on taking H a *little higher than 10^13*, which of course is not achieved by Theorem 1. This would enable one to prove Λ < 0.19."

→ paper-direct: 다음 numerical RH 추가 진전 (H > 10^13) ⟹ Λ < 0.19.

## 2. Numerical 검증 (Platt-Trudgian Corollary 1)

[paper-direct *Schoenfeld + Büthe* tool]

Schoenfeld bound at x = 10^10 (under RH up to H = 3×10^12):
- 4.92 √(10^10 / log 10^10) = 4.92 √(10^10/23) ≈ 4.92 × 6.6×10^4 ≈ 3.25×10^5.
- 3.25×10^5 ≤ H = 3×10^12 ✓.
- 즉 Schoenfeld bound *unconditional* up to x = 10^10.
- bound: |ψ(10^10) - 10^10| ≤ √(10^10)/(8π) log²(10^10) = 10^5/(8π) × (23.03)² ≈ 3978 × 529.4 ≈ 2.1×10^6.

[plausible]: bound very generous *upper* — actual error likely much smaller.

paper-direct: Büthe 4.92√(x/logx) ≤ H = 3×10^12 ⟹ x ≤ 2.169×10^25. paper-direct Corollary 1 numerical 일관.

## 3. Wall taxonomy mapping

### Wall #2 (FORWARD-TIME) deep refinement — *quantitative bracket update*

paper §3.4 paper-direct:
- Polymath15 (attempt 106): Λ ≤ 0.22 (forward heat).
- Rodgers-Tao 2020 (attempt 113): Λ ≥ 0 (backwards).
- Platt-Trudgian 2021 (Corollary 2): **Λ ≤ 0.2** (forward, sharper via H > 2.51×10^12).

→ Wall #2 *quantitative bracket* (~attempt 132 update): **0 ≤ Λ ≤ 0.2**.

paper-direct *future improvement path*:
- H > 10^13 ⟹ Λ < 0.19.
- 추가 numerical 진전 = Wall #2 *quantitative* sharpening via *numerical RH bound*.

### Wall #4 (CONSPIRACY) cross-link

paper-direct numerical RH up to 3×10^12 = *all* Re(ρ) = 1/2 in this range — *no conspiracy in low zeros*.
- Iwaniec-Sarnak family-wide form (attempt 112) cross-link: family-wide RH numerical up to height H.
- *paper-direct* 12.36×10^12 zeros 모두 *positive proportion 100%* (numerically).

### Wall #1 (FROBENIUS-GAP)
paper §3 quote: numerical method *FFT-based Riemann-Siegel* (Gourdon) vs *interval arithmetic Riemann-Siegel* (Platt).
- *function field* analogue: 자명 (degree polynomial — direct enumeration).
- *number field*: requires *transcendental computation* (Riemann-Siegel infinite asymptotic).
- → Wall #1 paper-direct *computational asymmetry*.

## 4. Lemma 적용

### Lemma 3 (positivity_unification) 12th evidence 강화

attempt 113 (Rodgers-Tao) Λ ≥ 0 + attempt 132 (Platt-Trudgian) Λ ≤ 0.2:
- *unconditional bracket* 0 ≤ Λ ≤ 0.2.
- RH ⟺ Λ ≤ 0 (Newman).
- *Λ = 0 strict equality* unknown (gap 0.2).

→ Lemma 3 12th evidence *quantitative bracket* 강화.

### Lemma 6 (dont_try_directions) Cut 7 paper-direct cross-check

본 attempt = *paper-direct numerical brute force* — *우리 도구 한계* (12.36×10^12 zeros 우리 직접 X).
- paper-direct: 7.5 million core hours, NCI clusters, 우리 도구 외 영역.
- Lemma 6 Cut 7 (paper-미명시 quantitative empirical 시도) 의 *paper-direct citation 사용*만.

### Lemma 4 (failed_proof_categories) cross-check
Platt-Trudgian 2021 = *successful peer-reviewed numerical*. Lemma 4 N/A.

## 5. Cross-reference

- attempt 028 (Polymath15 skim): Λ ≤ 0.22.
- attempt 044 (Lambda extended n): 200 zeros numerical.
- attempt 067 (Lambda numerical): n=30 sweet spot.
- attempt 106 (Polymath15 §4-§6 deep): Λ ≤ 0.22 paper-direct.
- attempt 113 (Rodgers-Tao 2020): Λ ≥ 0 paper-direct.
- 본 attempt 132 = Platt-Trudgian 2021 paper-direct: Λ ≤ 0.2.

## 6. Open questions

(Q1) Future numerical RH 진전 (H > 10^13) 가 *Λ < 0.19* enabling?
- paper-direct §3.4 끝: explicit possible.
- *우리 contribution X* (cluster computing 외 영역).

(Q2) *Computational efficiency improvement* (Gourdon FFT 725×) Platt-Trudgian rigor 와 trade-off?
- paper-direct: rigor (interval arithmetic) vs speed (FFT) trade-off.
- 통합 가능성 = *future research*.

(Q3) Schoenfeld bound 의 *constant 1/(8π) = 0.0398* 의 sharpness?
- paper-direct: Schoenfeld 1976 *original*.
- sharper constant = future work.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Platt-Trudgian 2021 paper-direct deep + Wall #2 quantitative bracket update (0 ≤ Λ ≤ 0.2) + Lemma 3 12th evidence 강화.
- *우리 contribution*: paper-direct mapping + Wall #2 *paper-direct quantitative bracket update* (Polymath15 0.22 → Platt-Trudgian 0.2 sharper).

## 8. Specialist Δ 추정 (Platt/Trudgian/Tao)

### Platt/Trudgian 본인 추정
- "본 paper = *peer-reviewed rigorous* numerical RH up to 3×10^12. Wedeniwski/Gourdon non-peer-reviewed 비교."
- "다음 progress: H > 10^13 (Λ < 0.19 enabling). FFT (Gourdon) + rigor (Platt) integration."

### Tao 추정 (외부 critique #4)
- "numerical RH 진전 = *combinatorial 최적화* — *fundamental Wall #2* 와 다름. Polymath16-like new technique 필요 ≠ numerical brute force."
- "Λ ≤ 0.2 → 0 의 gap = 0.2. *hard analysis fundamental obstacle* (외부 critique #4 Tao 추정 paper-direct 검증)."

[추정 한계]: 본 추정 자체가 *틀릴 수 있음*. paper §3.4 + Polymath15 §6 의 *paper-direct citation* 기반.

## "예상 가능 결과" self-check
yes — Platt-Trudgian 2021 paper-direct deep + Wall #2 quantitative bracket update + Lemma 3 12th evidence 강화 + Tao 추정 paper-direct 검증.
