# Attempt 012: Path-dependent Functional — KL / Entropy of Kernel-smoothed Measure
**Type**: A (Proof attempt, computational)

## 가설/전략

007 의 Wasserstein 이 forward-backward 대칭이라 부적합 — *path-dependent* functional 필요.

> **H1**: $\mu_t$ 의 *kernel-smoothed* 밀도 $\rho_t(x) := (1/N) \sum_k K_h(x - x_k(t))$ 의 differential entropy $H[\mu_t] = -\int \rho_t \log \rho_t$ 가 forward (t > 0) 와 backward (t < 0) 에서 *비대칭* 거동.
>
> **H2**: 만약 $\frac{d}{dt} H[\mu_t]$ 가 forward 에서 양 (entropy 증가) backward 에서 음이면 — 비대칭 캐치 + Wall #2 의 forward control 후보 functional.
>
> **H3 (실패 시)**: H 가 부호 의존 X (Wasserstein 처럼 대칭) → 다른 path-dependent 후보 필요.

## 동기

- 007 의 직접 후속.
- entropy 가 *concave* — 일반적으로 mixing/spreading 시 증가, clustering 시 감소. ODE 의 forward = spread → entropy ↑ 예상.

## DoD
- [ ] `tools/entropy_evolution.py` 신규
- [ ] N=20 영점, kernel bandwidth h 선택, forward/backward 적분
- [ ] H[μ_t] 시간 추적
- [ ] forward vs backward d/dt H 비교
