# Work — Attempt 033 (Connes-Consani 2021)

## §1 정독 정리

### Setup
- Spectral triple $\Theta(\lambda, k) = (\mathcal{A}(\lambda), \mathcal{H}(\lambda), D(\lambda, k))$.
- $\mathcal{H}(\lambda) = L^2([\lambda^{-1}, \lambda], d^*u)$.
- $D(\lambda, k)$ = finite-rank perturbation of Dirac on circle of length $2 \log \lambda$.
- 도구: *prolate spheroidal wave functions* (Slepian의 시간-주파수 localization).

### Theorem 1.1
(i) Multiplicative group $\mathbb{R}_+^*$ action 의 *orthogonal* spectrum = ζ zeros 의 imaginary parts on critical line.
(ii) If $\zeta(1/2 + is) = 0$, then circle of length $2\pi n / s$ ($n \in \mathbb{N}$) is a ζ-cycle.

### ζ-cycle (Definition 1.1)
Circle C of length $L = \log \mu$ such that subspace $\Sigma_\mu \mathcal{E}(\mathcal{S}_0^{ev})$ is *not dense* in $L^2(C)$.

### 핵심 numerical (paper §1 직접)

For $\lambda^2 = 10.5$, $k = 18$: low-lying spectrum 의 첫 31 eigenvalues 가 ζ zeros first 31 imaginary parts 와 *기괘하게* 일치.
- "the probability of obtaining such agreement from a random choice is of the order of $10^{-50}$".
- 즉 *수치적* 으로 매우 강한 evidence.

### 핵심 한계 (paper §1 자체 인정)

- 본 결과는 *theoretical explanation of numerical coincidence* — *RH 증명 X*.
- *parameter family* $(\lambda, k)$ — single 후보 X.
- λ vary 시 eigenvalue 가 ζ zero 와 맞는 *crossing point* 에서 매칭, *구간* 매칭 X.

### Wall #5 lemma step 6 적용 (033, paper-direct)

[rigorous]:
- Connes-Consani 의 spectral triple = sophisticated Hilbert-Pólya 후보.
- Lemma `spectral_candidate_circularity_check` step 6 (single H for all zeros): **부분 적용**.
  - λ vary + k integer 의 *parameter family*.
  - Single (λ, k) 가 모든 ζ zeros 매칭 X — λ 값 따라 *일부* zeros 만.
  - 즉 *multi-parameter* family — Sierra 와 비슷.

### Wall #4 (CONSPIRACY) 와의 연결

paper §3 (abstract 보임): Weil quadratic form positivity = RH.
- λ = √2 numerical positivity 만 증명 (Connes 2014).
- 더 큰 λ: archimedean alone fail, prime 2 contribution 포함하면 부분 회복.
- λ² grows past prime power → positivity fail without that prime — *prime 별 contribution 의 중요성*.

→ Wall #4 의 *family* 시각이 직접 증거 — *prime 별 family* 의 *positivity 통합* 이 RH.

### 본 시도 결과

- Wall #5 의 lemma step 6 적용 confirmation (lemma 재사용 가치 또).
- Wall #4 의 *prime-by-prime* family 시각 sharpening.
- *novel content X*. paper-direct.

### "예상 가능 결과" self-check
yes — Connes-Consani 가 paper 자체에서 honest 인정.
