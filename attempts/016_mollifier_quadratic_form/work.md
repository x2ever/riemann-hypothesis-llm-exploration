# Work — Attempt 016

## Pratt-Robles §3 정독 정리

### Mollifier 일반 형태 (paper §3.4, 식 3.6)

$$
\psi_d(s) = \sum_{\ell=0}^{K} (-1)^\ell \sum_{\ell_1 + \cdots + \ell_d = \ell}
(-1)^{1\ell_1 + 2\ell_2 + \cdots + d\ell_d}
\binom{\ell}{\ell_1, \ldots, \ell_d}
\sum_{n \le y_d} \frac{n^{\sigma_0 - 1/2}}{n^s}
\frac{(\mu \star \Lambda^{\star \ell_1} \star \Lambda_2^{\star \ell_2} \star \cdots \star \Lambda_d^{\star \ell_d})(n)}{(\log y_d)^{\sum r \ell_r}}
P_{d, \ell}\left(\frac{\log(y_d/n)}{\log y_d}\right)
$$

핵심 구조:
- $a_n = $ Möbius $\mu(n)$ × Bell polynomial of $\Lambda$-convolutions × polynomial $P_{d,\ell}(\log(y_d/n)/\log y_d)$.
- *square-free* $n$ 만 contribute (μ).
- $\Lambda^{\star k}$: von Mangoldt 의 k-fold Dirichlet convolution.

### Quadratic form 행렬

Mollifier optimization 의 main term 은:
$$
\frac{1}{T} \int_0^T |\zeta(\tfrac{1}{2}+it) \psi_d(\tfrac{1}{2}+it)|^2 dt
$$

Diagonal expansion (Pratt-Robles paper §1.2 eq (1.1) 의 mean value 형태):
$$
\sum_{hm = kn} \frac{\mu(h)\mu(k)}{m^{1/2+\alpha} n^{1/2+\beta} h^{1/2+\gamma} k^{1/2+\delta}}
$$

여기서 *index pair* $(m, n)$ 의 행렬 element 가 $\sum_{hm = kn} \mu(h)\mu(k) / \cdots$ — 즉 indices 의 *ratio* + prime structure 에 의존.

### Levinson-Durbin Toeplitz 와의 비교

[rigorous]:

**Levinson-Durbin Toeplitz**:
- $T_{i,j} = r_{|i-j|}$ — *index difference 만* 의존.
- 이게 algorithm 의 핵심 (translation invariance of stationary signal).

**Mollifier quadratic form**:
- 행렬 element 가 $\sum_{hm=kn} \mu(h)\mu(k) \cdot (\cdots)$ — *index ratio* + *prime factorization* 의존.
- $T_{m,n} \neq f(m/n)$ 만 도 아니고 — $\mu, \Lambda$ 에 의해 prime decomposition 이 결정적.
- **Translation invariance X** — index shift 하면 *prime factorization 변경*.

→ **Levinson-Durbin 의 Toeplitz 가정이 mollifier 행렬에서 위배**. 두 algorithm 의 *수학적 동치 X*.

[rigorous] 이 결론 — Pratt-Robles 의 mollifier 행렬 형태 자체가 prime-structure-dependent, Toeplitz X.

### 015 의 open question 종결

**Hypothesis H1 (Levinson mollifier ≡ Levinson-Durbin generalization)**: **NO** (negative).

**구체 이유**:
- Levinson-Durbin: Toeplitz matrix $T_{ij} = r_{|i-j|}$.
- Mollifier: matrix $T_{mn} = \sum_{hm=kn} \mu(h)\mu(k)/\cdots$ — *not* of form $r_{|m-n|}$.
- 두 algorithm 의 *core 가정 분리*.

[rigorous] honest 결론 — 단지 이름 일치는 동일인 N. Levinson 의 두 *별개* 작업.

(주의: *더 abstract framework* 에서 (예: 일반 *positive definite kernel inversion*) 두 algorithm 이 *별개 사례* 일 수는 있음. 그러나 *직접 mathematical equivalence* X.)

### Honest scope

- 본 시도는 015 의 가설을 *negative resolve*.
- *novel mathematical content X*.
- 그러나 *open question 종결* 자체가 가치 — speculation 의 honest closure.

### 다음 시도 후보

#### 017 — Type C
`lemmas/levinson_durbin_mollifier_open_question.md` 를 *resolved (negative)* 로 update + 본 시도의 lessons learned 분리해서 lemma 로.

#### 018 — Type A
다른 cross-domain bridge candidate 검색. 지금까지의 *negative* signals (Wasserstein, Levinson-Durbin) 의 패턴 추출.

#### 019 — Type A 또는 D
지금까지의 negative findings 종합 — *진짜 진전 가능성* 평가. (외부 critique 의 honest 위치 유지.)
