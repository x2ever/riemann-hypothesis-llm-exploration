# Work — Attempt 015

## 2026-05-01 — Pratt-Robles 정독 + cross-domain hypothesis

### Pratt-Robles §1 정독 정리

**핵심 정의** (paper p.6):
- $V(s) := Q(-\frac{1}{L}\frac{d}{ds})\zeta(s)$ where $L = \log T$.
- $Q(x)$: real polynomial, $Q(0) = 1$, $Q'(x) = Q'(1-x)$ (palindromic 류).
- 본 differential mollifier = Levinson 의 trick.

**핵심 도구** (paper §1.1):
- Autocorrelation ratios (Conrey-Farmer-Keating-Rubinstein-Snaith). 
- $R(\alpha, \beta, \gamma, \delta) := \int_0^T \frac{\zeta(s+\alpha)\zeta(1-s+\beta)}{\zeta(s+\gamma)\zeta(1-s+\delta)} dt$.
- Conjecture 1.1 (Conrey-Farmer-Zirnbauer): $R$ 의 정확한 asymptotic.
- 정수론자들이 RMT 측에 의지 (model + arithmetic factor).

**핵심 문장** (paper §1.2 끝, RMT 한계 인정):
> "there does not seem to be a random matrix analogue of mollifying as there is nothing that naturally corresponds to a partial Dirichlet series"

[rigorous] 이건 paper 자체의 statement.

### Cross-domain bridge hypothesis (H1)

**N. Levinson (1947)** — Levinson-Durbin recursion:
- 입력: autocorrelation $r_0, r_1, \ldots, r_n$ of stationary signal.
- 출력: AR 계수 $\{a_k\}$ such that $\sum_{k=0}^n a_k r_{j-k} = \begin{cases} \sigma^2 & j=0 \\ 0 & j > 0 \end{cases}$.
- 즉 $T_n \mathbf{a} = \mathbf{e}_0$ where $T_n$ = symmetric Toeplitz matrix of correlations.
- Order-recursive — efficient $O(n^2)$ inversion.
- *Reflection coefficients* $k_1, \ldots, k_n$ — AR model 의 *Schur* parametrization.

**N. Levinson (1974)** — Mollifier method (zeta zeros):
- $M(s) = \sum_{n \le y} a_n n^{-s}$ (mollifier).
- Optimization: $\int_0^T |\zeta(\frac{1}{2}+it) M(\frac{1}{2}+it)|^2 dt$ 최소화 등의 문제 → coefficients $a_n$.
- 이 minimization 이 *quadratic form on a* — 정확히 어떤 행렬?
- Pratt-Robles 식 (1.1) 의 $\sum_{hm=kn} \mu(h)\mu(k) / (m^{1/2+\alpha} n^{1/2+\beta} h^{1/2+\gamma} k^{1/2+\delta})$ — 정수 lattice 위 *correlation-like* sum.

**가능한 다리**:
- mollifier optimization 의 quadratic form 행렬이 *어떤 의미에서 Toeplitz*?
- mollifier coefficient $a_n$ 의 order-by-order 결정이 *Levinson-Durbin recursion*?
- *Reflection coefficient* 형식이 mollifier 길이 push 의 sharpness barrier 와 관계?

[hand-wave] 위 가설들은 *추측*. literature 검색 negative 이지만 그것 자체는 *증명* 아님. 진짜 검증 필요.

### Trivial circular vs non-trivial 분리 (lemma `spectral_candidate_circularity_check` 적용)

본 가설의 (A) trivial / (B) non-trivial 분리:

**[A] Trivial (likely)**: 두 Levinson algorithm 이 *Toeplitz / autocorrelation* 라는 일반 framework 안에 있다는 사실 — 자명. 둘 다 *quadratic minimization with Toeplitz constraint*.

**[B] Non-trivial (검증 필요)**: 
- mollifier 의 *arithmetic structure* (μ, Λ 같은 number-theoretic functions) 가 AR model 의 *signal autocorrelation* 와 *진짜 동치*인가?
- 또는 *형식 일치*만이고 본질 분리?

→ (B) 답이 *진짜 동치* 라면: signal processing 의 *Yule-Walker theory*, *Levinson-Durbin recursion*, *AR model identification* 등이 mollifier 분야에 직접 import.
→ *형식만 일치* 라면: bridge X.

[plausible] (B) 의 답을 본 시도에서 *결정* 못 함. 더 깊은 분석 필요.

### 본 시도의 honest 산출

1. **Pratt-Robles paper §1 정독 완료** — `papers/INDEX.md` 의 사고과정 추정 보강 가능.
2. **Cross-domain bridge candidate 명시화** — *open question* 로 lemmas/ 에 기록 가능.
3. **Wall #3 첫 진입** — channel diversification 진행.

### 다음 시도 후보

#### 016 — Type A: Pratt-Robles §3 (Constructing a mollifier) 깊이 정독
- mollifier coefficient $a_n$ 의 *explicit recursion* 가 있는지 확인.
- 만약 있다면 Levinson-Durbin 와 직접 비교.

#### 017 — Type E: signal processing literature on adaptive filtering / spectral estimation
- *Yule-Walker for arithmetic sequences* 같은 것이 있나?

#### 018 — Type A: Sierra 2016 정독 후 BBM-Sierra-Connes spectral 후보 평가
- lemma `spectral_candidate_circularity_check` 사용.

### 외부 critique self-check

- 예상 가능 결과? *부분 yes* (두 algorithm 의 형식 유사는 예상 가능). 하지만 *명시적 cross-domain hypothesis 의 진위* 는 미상.
- *실질적 진전* 0 — 본 시도는 *방향 sketch* 만.
- *novel mathematical content X* — 가설만.
- 외부 critique 의 *honest 위치* 유지: 본 시도가 *RH 진전* 아님 (미션 8.5/10 mode 의 또 한 attempt).
