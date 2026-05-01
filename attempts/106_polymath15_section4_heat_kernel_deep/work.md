# Work — Attempt 106 (Polymath15 §4-6 Heat Kernel + Estimates DEEP)

## 1. Paper section deep read

### §4 Heat-evolution form (paper-direct, eqs 36-41)

**Riemann-Siegel-like exact identity** (eq 36):
$$\frac{1}{8}\xi(s) = R_{0,0}(s) + R_{0,0}^*(1-s)$$

R_{0,0}(s) (eq 37): contour integral
$$R_{0,0}(s) := \frac{1}{8} \frac{s(s-1)}{2} \pi^{-s/2} \Gamma(s/2) \int_{0\swarrow 1} \frac{w^{-s} e^{i\pi w^2}}{e^{\pi i w} - e^{-\pi i w}} dw$$
contour from 0 to 1 in direction $e^{5\pi i/4}$.

Gauss-Riemann-Siegel expansion: $R_{0,0}(s) = \sum_{n=1}^N r_{0,n}(s) + R_{0,N}(s)$ where:
- $r_{0,n}(s) := \frac{1}{8} \frac{s(s-1)}{2} \pi^{-s/2} \Gamma(s/2) n^{-s}$ (eq 37) — *exact* (Hadamard product piece).
- $R_{0,N}(s)$ (eq 38) — error contour integral.

**Heat-flow construction** (eq 39):
$$H_t(z) = \sum_{n=1}^N r_{t,n}\left(\frac{1+iz}{2}\right) + \sum_{n=1}^N r^*_{t,n}\left(\frac{1-iz}{2}\right) + R_{t,N}\left(\frac{1+iz}{2}\right) + R^*_{t,N}\left(\frac{1-iz}{2}\right)$$
where:
$$r_{t,n}(s) := \int_\mathbb{R} r_{0,n}(s + \sqrt{t}v) \frac{1}{\sqrt{\pi}} e^{-v^2}\,dv$$
$$R_{t,N}(s) := \int_\mathbb{R} R_{0,N}(s + \sqrt{t}v) \frac{1}{\sqrt{\pi}} e^{-v^2}\,dv$$

**핵심**: r_{0,n}, R_{0,N} 의 Gaussian convolution 은 *forward heat equation* under t > 0. 즉 H_t 가 H_0 = (1/8)Ξ(z/2) 의 *Gaussian kernel* evolution.

### §4 Saddle-point reformulation (eqs 40, 41)

eq (40): $r_{t,n}(s) = \exp(-t\alpha_n^2/4) \int_\mathbb{R} \exp(-\sqrt{t}v\alpha_n) r_{0,n}(s + \sqrt{t}v + (t/2)\alpha_n) (1/\sqrt{\pi})e^{-v^2}dv$
- arbitrary α_n (with Im(s), Im(s + (t/2)α_n) same sign).
- 후술 §6.1 에서 saddle-point near v=0 만들기 위해 α_n 선택.

eq (41): R_{t,N} 동일 form with β_N. saddle-point 근처 stationary phase.

[paper-direct]: §4 의 핵심 = 1/8 ξ(s) 의 *algebraic* 분해 (Hadamard like) + Gaussian heat evolution.

### §5 Elementary estimates (Lemma 5.1, paper-direct)

(i) $a/x + b/x^2 + c/x^3 = O_\le(a/(x - \max(b/a, \sqrt{c/a})))$ for x > b/a, sqrt(c/a). geometric series consolidation.

(ii) $\log(1 + O_\le(1/x)) = O_\le(1/(x-1))$ for x > 1. Taylor of log + geometric.

(iii) $\exp(O_\le(1/x)) = 1 + O_\le(1/(x-0.5))$ for x > 1/2. exp Taylor + k! ≥ 2^k (k≥2) trick.

(iv) $\exp(O_\le(x)) = 1 + O_\le(e^x - 1)$.

(v) Effective Stirling (Boyd 1994): Γ(z) = √(2π) exp((z-1/2)log z - z + O_≤(1/(12(|z|-0.246)))).
Inner: |R_2(z)| ≤ (2√2 + 1) C_2 Γ(2) / ((2π)^3 |z|^2) for Re z ≥ 0, C_2 = (1+ζ(2))/2 = (1+π²/6)/2.

(vi) $\log^a |x+iy|/(x-c)^b$ non-increasing for x ≥ x_0 ≥ exp(a/b). monotonicity by differentiation.

[paper-direct]: §5 = 모든 effective estimates 의 *toolkit*. paper §6 의 propositions 가 이걸 반복 사용.

### §6.1 Proposition 6.1 (r_{t,n} estimate)

Proposition (eq after 44): For σ real, T ≥ 10, n positive integer, 0 < t ≤ 1/2:
$$r_{t,n}(\sigma + iT) = M_t(\sigma + iT) \frac{b_n^t}{n^{\sigma+iT+(t/2)\alpha(\sigma+iT)}} (1 + O_\le(\varepsilon_{t,n}(\sigma+iT)))$$
where (eq 44):
$$\varepsilon_{t,n}(\sigma+iT) := \exp\left(\frac{(t^2/8)|\alpha(\sigma+iT) - \log n|^2 + t/4 + 1/6}{T - 3.33}\right) - 1$$

Proof tactic: eq (40) with α_n := α(σ+iT) - log n. Taylor expansion of log M_0 to second order. Apply Lemma 5.1(i)-(iii) to consolidate error terms.

핵심 identity (eq 47):
$$\int_\mathbb{R} \exp\left(\frac{tv^2}{2(T-3.08)}\right) \frac{1}{\sqrt{\pi}} e^{-v^2} dv = \left(1 - \frac{t}{2(T-3.08)}\right)^{-1/2}$$

[paper-direct]: σ-uniform bound. r_{t,n} 의 *quantitative* approximation.

### §6.2 Proposition 6.2 (Arias de Reyna), 6.3 (R_{t,N})

R_{0,N} 의 contour integral ∫_{N\swarrow N+1} w^{-s} e^{iπw²}/(e^{πiw} - e^{-πiw}) dw 의 *explicit* expansion (eq 53):
$$\int = (-1)^{N-1} U a^{-\sigma} \left(\sum_{k=0}^K \frac{C_k(p, \sigma)}{a^k} + RS_K(s)\right)$$
where:
- $a := \sqrt{T'/(2\pi)}$, $N := \lfloor a \rfloor$, $p := 1 - 2(a-N) \in [-1, 1]$.
- $U := \exp(-i(T'/2 \log T'/(2\pi) - T'/2 - π/8))$.
- C_0 paper-direct (eq 53):
$$C_0(p) = \frac{e^{i\pi(p^2/2 + 3/8)} - i\sqrt{2}\cos(\pi p/2)}{2\cos(\pi p)}$$
(removing singularities at p = ±1/2). |C_0(p)| ≤ 1/2 on [-1, 1].

Proposition 6.3 (eq 59):
$$R_{t,N}(\sigma+iT) = (-1)^{N-1} U e^{\pi i\sigma/4} \exp(t\pi^2/64) M_0(iT')(C_0(p) + O_\le(\tilde\varepsilon(\sigma+iT)))$$
where:
$$\tilde\varepsilon(\sigma+iT) := \left(\frac{0.397 \times 9^\sigma}{a - 0.865} + \frac{5}{3(T-6)}\right) \exp\left(\frac{3.49}{T-4}\right)$$

[paper-direct]: H_t 의 *terminator term* = M_0(iT') C_0(p) + smaller error.

## 2. Numerical 검증

[numerical, dps=30]

### C_0(p) 검증 (eq 53)

$|C_0(p)| ≤ 1/2$ verification on $p \in [-1, 1]$:

| p | C_0(p) | \|C_0\| |
|---|---|---|
| -1.0 | 0.461940 - 0.191342i | 0.500000 |
| -0.8 | 0.355373 - 0.235554i | 0.426351 |
| -0.5 (lim) | 0.250000 - 0.250000i | 0.353553 |
|  0.0 | 0.191342 - 0.245167i | 0.310996 |
| +0.5 (lim) | 0.250000 - 0.250000i | 0.353553 |
| +1.0 | 0.461940 - 0.191342i | 0.500000 |

[rigorous]: C_0(±1) = max. *exact 1/2*. paper bound saturated at endpoints. 대칭 |C_0(-p)| = |C_0(p)| 확인 (eq 53 의 cos symmetry).

### ε̃(σ+iT) (eq 59) 정량

| T | a = √(T'/2π) | ε̃(0.5+iT) |
|---|---|---|
| 10 | 1.264 | 6.08e+0 |
| 30 | 2.187 | 1.11e+0 |
| 100 | 3.990 | 4.14e-1 |
| 1000 | 12.616 | 1.03e-1 |
| 10000 | 39.894 | 3.07e-2 |

[plausible]: T=10 에서 ε̃ ≈ 6 (bound 안 좋음), T ≥ 100 부터 useful. Polymath15 가 T ≥ 200 부터 numerical 검증 시작 — paper-consistent.

σ scaling at T=1000: ε̃(0) = 3.6%, ε̃(0.5) = 10.3%, ε̃(1) = 30.7%. 9^σ factor 효과 가시.

### Boyd effective Stirling

|R_2(z)| ≤ (2√2 + 1) C_2 / ((2π)^3 |z|^2) ≈ 0.0204 / |z|².
- z = 10: |R_2| ≤ 2.04e-4
- z = 100: |R_2| ≤ 2.04e-6

[paper-direct]: 이 bound 가 §6.3 의 1/(12|z| - 3) 형태로 변환 (Lemma 5.1(i) 적용).

### eq (47) 적분 항등식

| T | (1 - t/(2(T-3.08)))^{-1/2} | exp(t/(4(T-3.33))) |
|---|---|---|
| 10 | 1.003632 | 1.003755 |
| 100 | 1.000258 | 1.000259 |
| 1000 | 1.000025 | 1.000025 |

[rigorous]: 두 form Lemma 5.1(ii) 적용 후 essentially 동일. paper §6.1 finale 직접 확인.

### α_n imag bound (eq 46)

Im α_n ≥ -1.5/T:
- T=10: -0.15 (paper-explicit)
- T=100: -0.015
- T=1000: -0.0015

이 bound 가 σ + iT + √t v + (t/2)α_n 의 Im 가 same sign 유지하는 *quantitative* condition.

## 3. Wall taxonomy mapping

### Wall #5 (FORWARD-TIME) deep refinement

Polymath15 의 *forward-only* heat flow:
- H_t 는 forward t > 0 의 *quantitative* control (Λ ≤ 0.22).
- Backward t < 0 시 r_{t,n}, R_{t,N} 의 Gaussian convolution 발산 — Wall #5 *paper-direct origin*.
- Connes-Consani 2021 의 다른 방향: forward heat 가 *not* RH 직접 — Λ ≤ 0 만 strict.

§4 의 *exact* Riemann-Siegel decomposition 이 forward-time 만 tractable 하게 만든 *기술적* 이유.

### Wall #2 (SHARP-CONSTANT, hard analysis) cross-link

Polymath15 §6 의 effective constants (3.33, 3.08, 0.865, 0.397×9^σ 등) 가 *exhaustive* — Tao 의 Polymath 경험 추정 (사용자 critique 의 Tao 참조).
- 이 정확한 constants 는 Lemma 5.1 + Boyd Stirling + 조합.
- 더 나은 constants 는 *combinatorial finite-step optimization*.
- *Λ ≤ 0.22* → 0 의 gap = combinatorial 최적화로 메우지 못함 (현재).

이건 specialist 직관: "constant 줄이는 건 산업"이라고 Tao 가 명시한 paper §1 introduction.

### Wall #1 (FROBENIUS-GAP) cross-reference

Polymath15 의 *finite N* expansion (eq 39) 은 *function field* 의 Lefschetz formula 의 number field "imitation" — H_t = sum + remainder. 그러나 finite cohomology 가 아닌 *contour integral asymptotic* — Wall #1 의 Lemma 4 (failed_proof_categories) 의 "structure imitation 수치 매개" 와 일치.

## 4. Lemma 적용

### Lemma 5 (failed_proof_categories) cross-check

Polymath15 는 *failed proof X* — successful incremental advance (Λ ≤ 0.22). Lemma 5 적용 N/A.

### Lemma 3 (positivity_unification) potential link

H_t 의 *zeros 가 real* (RH-equivalent for t = 0) ⟺ Newman 의 positive Λ. positivity 가 *forward-time monotonic*. Lemma 3 의 8th paper-direct evidence 가능 (Newman positivity = Λ ≥ 0 의 *Hermite criterion* paper-direct form).

paper §1 cite: De Bruijn 1950 + Newman 1976 의 H_t = (1/2) Ξ(t) form. paper-direct.

### Lemma 1 (spectral_candidate_circularity_check) cross-link

H_t = forward heat flow ⟹ Hilbert-Pólya 후보 spectral interpretation X (직접). attempt 049 (heat_flow_simulation) cross-ref.

## 5. Cross-reference

- attempt 049 (heat_flow_simulation): forward heat flow 의 우리 simulation 시도 — paper §4 의 정확한 form 과 일치 확인.
- attempt 057-062 (Voros): Z(σ) saddle-point method = §6.1 의 saddle 방법론 *유사* (formal).
- attempt 086 (Lagarias): unconditional asymptotic = §6 의 effective constants *동일 spirit*.
- attempt 105 (Lagarias §4): generalized Li 와 H_t 의 *상관관계 X* — λ_n 은 ξ(s)/ξ(0) 의 *log expansion*, H_t 는 ξ 의 heat kernel evolution. 관계는 ξ을 통해 *간접*.

## 6. Open questions

(Q1) Polymath15 §6 의 effective constants 가 *Boyd Stirling* (Lemma 5.1(v)) 의 1994 추정에 *binding* 되어 있는가? Boyd 후속 research 가 더 sharp constants 줬다면 Polymath15 reproof 가 Λ < 0.22 로 개선?
- *알려진 fact*: Boyd 1994 가 "current best" effective Stirling.

(Q2) C_0(p) 의 |C_0| ≤ 1/2 bound 가 *최적*인가, 아니면 더 sharp bound 존재?
- numerical: 0.310996 ≤ |C_0| ≤ 0.500000 on [-1,1].
- average |C_0| ≈ 0.39. Cauchy-Schwarz 등으로 averaged form 의 더 나은 control 가능?
- paper §6.2 cite: "n=0 case of [2, Theorem 6.1]" — 더 큰 n 으로 sharper bounds 가능.

(Q3) eq (40) saddle-point parameter α_n = α(σ+iT) - log n 의 *최적성*: 이 선택이 stationary phase 정확히 v=0 ⟺ derivative 0. 다른 saddle 은 useful?
- paper §6.1 finale: α_n 이 *unique* stationary saddle.

## 7. Yellow flag + honest scope

[045]:
- yellow flag word 회피.
- *novel content X*. Polymath15 §4-6 paper-direct deep + numerical 4 quantities 검증.
- *우리 contribution*: paper-direct mapping + numerical (C_0 max 0.500 saturate 확인, ε̃ T-scaling, Boyd bound 정량) + Wall #2/#5 cross-link.

## "예상 가능 결과" self-check
yes — Polymath15 §4-6 paper-direct deep + 4 numerical 검증.
