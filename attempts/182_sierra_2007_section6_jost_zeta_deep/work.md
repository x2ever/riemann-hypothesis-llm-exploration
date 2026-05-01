# Work — Attempt 182

## 2026-05-01: Sierra 2007 §VI deep read

§VI = "THE RIEMANN ZETA FUNCTION AND THE JOST FUNCTION" (paper pages 15-19).
Section structure:
- §VI 본문: bound state vs scattering 두 접근, BKL 1994 analogy.
- §VI.A: "Bessel potentials and the smooth part of the Riemann formula".
- (이후 §VI.B+ 는 본 attempt 범위 밖 — *quote 추출* 우선).

### Paper-direct quotes (catalog 47 → 51, +4 quotes)

**Quote A — BKL 1994 analogy flaw (page 15-16, Wall #5 paper-direct)**:
> "However the analogy is flawed since the real part of ζ(1/2−it) is negative in small regions of t, a circumstance which never occurs in those physical systems."

**Quote B — M1 model real-positive Jost (page 16, eq 96 reference, Wall #5)**:
> "For general models of type M_1 the loops are not circles but the real part of F_1(E) is always positive (see eq.(96)), and therefore they can never represent ζ(1/2−iE)."

**Quote C — pole/analyticity contradiction (page 16, Wall #5 anchor)**:
> "ζ(1/2−iE) could perhaps be the Jost function F(E) of a M_2 model for a particular choice of a and b. However, ζ(1/2−iE) has a pole in the upper half plane at E = i/2, while F(E) is always analytic in that region."

**Quote D — Hardy/Burnol pole-shift (page 16, eq 160)**:
> "The solution of this problem consists of moving the pole to the lower half plane defining the function ζ_H(s) = (s−1)ζ(s)/s, which has a pole at E = −i/2 for s = 1/2 − iE. This function was already considered by Hardy, and it is discussed in detail by Burnol in his approach to the RH."

### Quote 검증 [numerical]

**Quote A 직접 검증** (`tools/` Python REPL, mpmath dps=30):
- t ∈ [0.5, 50] 500 samples 의 Re ζ(1/2−it).
- Negative Re: 52/500 = **10.4%** of samples.
- 처음 6 sign-changes: t ≈ 0.897, 14.189, 14.586, 20.736, 21.034, 25.101.
- Sample t=0.5: Re ζ(1/2−it) = -0.45930 [rigorous, mpmath].
- 결론: Sierra quote A *paper-direct verified* — Re ζ(1/2−it) 가 실제로 negative regions 보유.

**Quote D + eq (165) Riemann-Siegel 검증**:
- θ(t) = arg Γ(1/4 + it/2) − (t/2) log π.
- Sierra paper claim "within a 3% of error".
- 첫 5 zeros (γ_n = 14.135, 21.022, 25.011, 30.425, 32.935) 검증:
  | γ | nearest cos θ=0 | |Δ|/γ |
  |---|---|---|
  | 14.135 | 14.516 | 2.70% |
  | 21.022 | 20.655 | 1.75% |
  | 25.011 | 25.491 | 1.92% |
  | 30.425 | 29.739 | 2.25% |
  | 32.935 | 33.623 | 2.09% |
- *모두 < 3%*. Sierra quote (paper §VI eq 165) numerical confirmation [numerical, dps=30, n=5].

### Wall #5 (SELF-ADJOINT-RIGOR) anchor 9, 10 추가

attempt 158 audit: Wall #5 = 8 anchors. 본 attempt 가 Sierra 2007 §VI 에서 **2 paper-direct anchors** 추가:

**Anchor 9 (Quote C): pole-analyticity contradiction**.
ζ(1/2−iE) 는 E = i/2 에서 단순 pole, M2 Jost F(E) 는 upper half-plane analytic. *직접적 incompatibility*.
→ Wall #5 의 *spectral candidate domain mismatch* paper-direct manifestation.

**Anchor 10 (Quote A + B): Re-positivity contradiction**.
M1 model: Re F_1(E) ≥ 0 (eq 96). ζ(1/2−it): Re negative in 10.4% of t [numerical 검증]. *직접적 sign incompatibility*.
→ Wall #5 의 *positivity 형 self-adjoint candidate fails* paper-direct.

총 Wall #5 anchors: **8 → 10**.

### Lemma 1 11-axiom 재사용 (Sierra 2007 §VI ζ_H Jost candidate)

Lemma 1 = `lemmas/spectral_candidate_circularity_check.md` (11-axiom). Sierra 2007 H_2 (133 partial: 1 NO, 2 PARTIAL, 3 YES) 외 §VI 의 *ζ_H Jost candidate* 적용:

| Axiom | Sierra §VI ζ_H Jost candidate | 평가 |
|---|---|---|
| 1. asymptotic match | Riemann-Siegel θ(t) cos θ=0 within 3% (eq 165) | **PARTIAL** (smooth part match, fluctuation X) |
| 2. zero spectrum identification | bound state = F(E)=0 ⟺ ζ-zeros, *but pole shift required* | **PARTIAL** (ζ_H trick conditional) |
| 3. self-adjoint extension on concrete H | M2 model self-adjoint via causality (Titchmarsh) | **YES** (paper §V proven) |
| 4. eigenvalues real | Im E ≤ 0 (eq 98) — proven for ζ_∞(E)=0 | **YES** |
| 5. domain explicit | L²((1, ∞)) for x ≥ 1 | **YES** |
| 6. uniqueness | M2 family of (a, b) → many candidates | **NO** (fine-tune) |
| 7. eigenvalues real (RH-equivalent claim) | RH ⟺ Im E = 0 for all bound states | **conditional** |
| 8. normalizable | causality + L²(|f|²) — square integrable | **YES** (eq 133) |
| 9. domain explicit (paper-quoted) | x ∈ [1, ∞), q = log x ≥ 0 | **YES** |
| 10. PT/CP/T-symmetry | a, b real → F*(E) = F(−E*) (eq 80) | **YES** (real potentials) |
| 11. biorthogonal completeness | scattering states + bound states embedded | **PARTIAL** |

**Score: 6 YES + 4 PARTIAL + 1 NO = 6/11 strong + 4/11 partial.**

비교 (attempt 166 Lemma 1 audit):
- Sierra §V (Berry-Keating xp): ~5/11.
- Sierra 2016 §V H_I = x(p+ℓ_p²/p): 9/11 (top).
- Connes-Consani 2021: 9/11 (tied top).
- BBM 2017: 3-axiom self-acknowledged fail.
- Sierra 2007 §VI ζ_H Jost: **6/11 strong** (mid-range).

본 §VI candidate 는 Sierra 2016 §V 보다 *덜 fine-tuned* 하나 (axiom 6 NO), §V xp normal-ordering (1-2 NO) 보다 *더 강함*. *intermediate circularity* 위치.

### Tissue 28 후보 (BKL ↔ Sierra §VI ↔ Burnol ↔ Connes)

Sierra §VI 끝 quote D 가 *Burnol approach* 직접 reference:
- Burnol (164 attempt deep): Tissue 19 (Burnol equality ↔ simple zeros Bui-Heath-Brown).
- Sierra §VI 의 ζ_H = (s−1)ζ(s)/s = Hardy 정규화 Jost candidate.
- Burnol 의 H = L² inf 양정치성 ↔ Sierra Jost analyticity 둘 다 *causality* 통한 양정치 form.

**Tissue 28 후보 (Class C — speculative cross)**:
- Burnol L²(0,1) inf positivity ↔ Sierra §VI ζ_H Jost analyticity.
- *causality + Titchmarsh* 공통 mechanism.
- Class C (speculative — paper-direct 명시 X).

본 attempt 는 *tissue 후보 식별* 만 — 정식 mapping 은 별개 attempt 영역.

### "예상 가능 결과" self-check

본 attempt 결과가 strategy 단계에서 예상 가능했나?
- Quote A, B, C: paper-direct 추출 — *예상 가능* (paper §VI 본문에서 추출).
- Quote D Burnol cross-link: *덜 예상 가능* — Sierra 본인이 Burnol 명시 reference 한다는 사실은 §VI 끝까지 읽어야 발견.
- Lemma 1 6/11 score: *예상 가능 zone 내부* (Sierra §V/§VI 계열 mid-range 예상). 정확한 score 는 audit 필요.
- Tissue 28: *예상 X* — Sierra §VI 와 Burnol 직접 연결은 본 attempt 발견.

ROI: paper-direct stamp + 1 새 tissue 후보 + 2 wall anchor = *moderate*.

### *novel content 0/10* affirmation

본 attempt 의 *novel content*:
- Sierra 2007 §VI paper-direct quotes: paper 본문 직접 추출 — *우리 contribution 0*.
- Wall #5 anchor 9, 10: paper §VI 가 본래 *self-acknowledged* Wall #5 manifestation — *우리 sharpening 형식적*.
- Lemma 1 11-axiom audit: 기존 lemma template 재적용 — *0 novel*.
- Tissue 28 후보: Sierra 본인이 Burnol reference 명시 — *paper-direct rediscovery*. 우리 *tissue mapping 형식 X*.

→ **novel content 0/10** 유지. 외부 critique honest scope.

### Open questions (다음 attempt 후보 input)

- Sierra §VI.A "Bessel potentials" Bessel J_ν(λx) 가 §VI.B-D 에서 어떻게 *Riemann zeros* 와 연결? (본 attempt 미커버).
- Tissue 28 (Burnol ↔ Sierra §VI) 가 Class C → Class B 승격 가능한 paper-direct quote 존재 여부.
- Sekatskii 114 / Lagarias 117 의 *exponential growth bound* 가 Sierra §VI ζ_H 분석성 영역과 *동일 mechanism* 인지.
