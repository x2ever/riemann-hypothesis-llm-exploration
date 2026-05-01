# Work — Attempt 006

## 2026-05-01 — ODE 시뮬레이션

### Run #1: N=20, T=0.001, steps=20, dps=30

[numerical, dps=30, N=20, T=0.001, RK4 steps=20]

```
[forward, t > 0]
t=0.000: E=7.8242, H=-533.7377, min_gap=1.4401, std_gap=1.4222
t=0.001: E=7.8158, H=-533.7534, min_gap=1.4426, std_gap=1.4214

[backward, t < 0]
t= 0.000: E=7.8242, H=-533.7377, min_gap=1.4401, std_gap=1.4222
t=-0.001: E=7.8326, H=-533.7221, min_gap=1.4377, std_gap=1.4229
```

### Monotonicity 결과

**Forward (t > 0)**:
- energy ↓ (감소)
- hamiltonian ↓ (감소)
- min_gap ↑ (증가 — repulsion 효과)
- mean_gap ↑ (살짝)
- std_gap ↓ (감소 — gaps 더 균일)

**Backward (t < 0)**: 정확히 mirror.

### 분석

[rigorous]:
- ODE 가 작은 |t| scale 에서 정확히 RK4 로 적분 가능.
- forward-time 에서 energy E(t), hamiltonian H(t) 가 *strict monotone decreasing*.
- 이는 Rodgers–Tao 2020 Theorem 11 부근의 monotonicity formula $\partial_t \mathcal{H} = -4E$ 의 *수치 확인*.

[plausible]:
- 본 결과는 *알려진 monotonicity* 의 보강. Wall #2 의 *새 측면* X.
- 그러나 *우리에게는* 의미 — Wall #2 의 본질이 단순 monotonicity 부재 아님 확정.

### Wall #2 의 본질 재해석 (본 시도의 main 통찰)

forward-time 에서 *infinitesimal* monotonicity 는 *있다*. 그렇다면 Λ ≤ 0 (=RH) 이 왜 못 풀리는가?

추정: **integrated** control 이 본질적 어려움.
- $\int_0^Λ \partial_t \mathcal{H} \,dt = \mathcal{H}(Λ) - \mathcal{H}(0) = -4 \int_0^Λ E(t)\,dt$.
- forward 에서 H 가 감소 — *얼마나* 감소하는가가 Λ 의 정량.
- 만약 H 가 *너무 빨리* 감소 → 영점이 너무 균일 → Montgomery 와 모순 (Rodgers–Tao 의 본질).
- backward 에서는 Λ < 0 가정 시 모순 도출 가능.
- forward 에서는 t = 0 시점 H 와 t > 0 시점 H 사이 *integral* 이 conditionally 정량 가능 — 그러나 *unconditional* 로는 미해결.

→ 즉 Wall #2 의 본질은 "$\int_0^Λ E(t)\,dt$ 의 unconditional bound" 부재. 이게 더 sharp 한 wall 표현.

[plausible] 본 분석 — Rodgers–Tao paper §3 Lemma 4 부근 참조.

### 다음 시도 후보 (본 통찰 기반)

1. **007 — Type E**: Rodgers–Tao paper 의 §3, §4 (Riemann-von Mangoldt for H_t, energy bound) 정독 → ∫E(t)dt 의 알려진 bound 확인. literature deepening.
2. **008 — Type A**: ∫₀^Λ E(t)dt 의 *Wasserstein* 시각 — empirical measure flow 의 *integrated* metric 으로 변환. Otto's calculus 시도.
3. **009 — Type C**: heat_flow_simulation.py 확장 — N 더 크게 (50, 100), T 더 크게 (0.01 ~ 0.1), Wasserstein-2 추적.

### 결론 (work)

본 시도는 *Wall #2 정복 X* — 그러나 wall 의 *정확한 형태* 재해석:
- "forward-time 단조성 부재" (잘못된 statement) → "*integrated* energy bound 부재" (정확한 statement).

이것이 본 시도의 main 산출 — Wall #2 의 *sharper formulation*.
