# Work — Attempt 017

## 분석적 derivation

### Setup

Empirical measure: $\mu_t = (1/N) \sum_{k=1}^N \delta_{x_k(t)}$.

ODE (Csordas–Smith–Varga): $\dot x_k = 2 \sum_{j \neq k} \frac{1}{x_k - x_j}$.

Kernel-smoothed density: $\rho_t(x) = (1/N) \sum_k K_h(x - x_k(t))$, $K_h(x) = (1/h) K(x/h)$ Gaussian.

Differential entropy: $H[\mu_t] = -\int \rho_t(x) \log \rho_t(x) \,dx$.

### d/dt 유도

[rigorous]:

$\dot \rho_t(x) = -(1/N) \sum_k K_h'(x - x_k) \dot x_k$ (chain rule on kernel).

이건 *velocity field* 의 정의 issue. Empirical measure 의 *macroscopic* velocity field 는:
$$
v_t(x) = \frac{1}{\rho_t(x)} \cdot \left(- \frac{1}{N} \sum_k K_h(x - x_k) \dot x_k \right) \cdot (\text{integrated form})
$$
즉 continuity equation: $\partial_t \rho + \partial_x(\rho v) = 0$.

### 단순화 — empirical 직접 (kernel-free heuristic)

(*주의*: 이 단계는 informal. 진정 rigorous 는 더 정밀한 기교 필요.)

$\dot H \approx -\frac{1}{N} \sum_k \dot x_k \cdot \partial_x \log \rho_t (x_k)$.

영점 ODE: $\dot x_k = 2 \sum_j 1/(x_k - x_j)$ (j ≠ k).

따라서:
$$
\dot H \approx -\frac{2}{N} \sum_{k \neq j} \frac{1}{x_k - x_j} \cdot \partial_x \log \rho_t(x_k)
$$

[hand-wave] kernel-smoothed density 의 logarithmic derivative 가 *작은 h limit* 에서 $\partial_x \log \rho_t(x_k) \to $ "local mean drift" — 정의가 미묘.

### Direct numerical fitting (analytical 보다 더 honest)

본 시도의 *analytical* 진전이 어렵다. 대신 *numerical correspondence*:

[plausible]:

데이터:
- 012: forward dH/dt ≈ +0.0465 at t = 0.001, N=20.
- 006: forward dE/dt ≈ (E(0.001) - E(0))/0.001 = (7.8158 - 7.8242)/0.001 = **-8.4**.

비율: dH/dt ÷ |dE/dt| = 0.0465 / 8.4 ≈ **0.0055**.

이 비율의 *analytical* 의미? 알려진 Otto's calculus 라면 $\dot H = c \cdot \int |\nabla \rho/\rho|^2 \rho$ 같은 *Fisher information* 형태. 하지만 우리 ODE 는 *Coulomb interaction* (1/r) 이라 일반 heat 와 다름.

### Honest scope 유지

본 분석은 *novel mathematical content X* — Otto's calculus 의 *informal heuristic*. 진정 rigorous 는 expert 영역.

가능 결론:
1. 두 numerical 양 사이에 *constant ratio* 는 *small t expansion* 의 산물 — 일반적 fact.
2. 이 ratio 의 *physical meaning* (Otto's calculus 에서) 미상 (우리 한정).
3. 더 *진짜* 분석은 expert NCG / SDE / log-gas literature 필요.

### 결론

본 시도의 *honest 결과*:
- d/dt H 의 closed form 직접 derivation 시도 — *informal* 단계 못 넘음.
- numerical ratio (dH/dE) 의 *analytical 의미* 미상.
- expert literature 가 필요한 영역.

→ **본 시도 ROI 낮음**. 외부 critique 의 honest 위치와 일관.

### Lemma extraction trigger

*lemma 산출 X*. 
*왜*: 수학 분석이 *informal* 단계만, *rigorous closed form* 못 산출.

→ HARNESS §1.4 의 trigger 작동: "결과가 informal heuristic 만" 라는 자기 분류.

## "예상 가능 결과" self-check

*yes*. strategy 에서 인정한 대로 — 본 시도가 알려진 Otto's calculus 의 미세 instance 일 가능성 매우 높음. *novel content X* 가 예상되었고, 그게 결과.

→ *이런 시도 반복은 ROI 낮음*. 다음 시도는 *예상 가능 zone 외부* 로 더 나아가기.
