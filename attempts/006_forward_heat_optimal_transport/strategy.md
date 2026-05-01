# Attempt 006: Wall #2 (FORWARD-TIME) — Heat Flow Numerical Quantification
**Type**: A (Proof attempt, computational, ambitious)

## 가설/전략

Wall #2 (FORWARD-TIME) 직접 도전. **단** 한 번 시도로 풀릴 가능성 거의 0 — 본 시도의 *현실적* 목표는:

> **H1**: Csordas–Smith–Varga ODE $\partial_t x_k = 2 \sum_{j \neq k} 1/(x_k - x_j)$ 를 ζ 첫 50 영점에서 시작해 forward (t > 0) 와 backward (t < 0) 소량 적분. 다음 functionals 의 *시간 단조성* 검증:
>   - Energy $E(t) = \sum 1/(x_j - x_k)^2$
>   - Hamiltonian $\mathcal{H}(t) = \sum \log(1/|x_j - x_k|)$
>   - Min gap, mean gap, gap variance
>   - Wasserstein-2 distance to Riemann–von Mangoldt expected distribution
>
> **H2**: 단조 *forward-time* functional 발견 시 → Wall #2 우회 후보.
> **H3**: 모든 후보가 forward-time 단조 X → Wall #2 의 정량 confirmation, *어떤 functional 이 깨지는지* 가 본 시도의 정보.

## 동기

- 005 에서 결정한 다음 *non-RMT* + cross-domain 시도.
- Rodgers–Tao 2020 의 backward analysis 와 *대조* — forward 가 어떻게 다른지 직접 관찰.
- LLM cross-domain 강점 (heat flow ↔ optimal transport ↔ Coulomb gas) 활용.

## 분류

- **VI** de Bruijn–Newman 핵심.
- **XI** optimal transport / Wasserstein.
- **IX** computational.

## Specialist 의무 호출

- S5 (Tao 류, hard analysis) — 본 ODE 의 backward analysis 전문.
- S4 (확률) — Wasserstein 측도.
- S6 (양자/통계물리) — log-gas / Coulomb gas 시각.
- (Tier 2): S11 (자유확률) — empirical measure flow.

## Cross-domain Pass

### A. 유추
- log-gas / Coulomb gas (β=2 Dyson Brownian motion)
- Calogero–Moser integrable system
- Wasserstein gradient flow on probability measures
- Ricci flow on metric measure spaces

### B. 도구 임포트
- *Wasserstein-2 distance*: 영점 분포 evolution 의 거리 metric.
- *Lott-Sturm-Villani synthetic Ricci*: 측도 위의 곡률 — gradient flow 의 contraction 가능성.
- *Otto's calculus*: probability measure 위 PDE 의 Hamiltonian 시각.

### C. 외부인
- 통계물리: "이 ODE 의 thermodynamic limit equilibrium 은? Wigner semicircle? Riemann-von Mangoldt?"
- 적분동역학: "integrable invariant 가 있는가? Calogero-Moser 와 같은 conservation laws?"

### D. 변형
- 약화: 작은 N (10~50 zeros) — full system 대신 부분 동역학.
- 강화: 무한 N limit — empirical measure flow.
- 일반화: ζ 외에 다른 L-function (Dirichlet) 의 zero ODE.

## Computational Verifications

### 코드
- `tools/heat_flow_simulation.py` 신규.
  - ODE solver (Runge-Kutta 4) on first N zeros.
  - Time step dt (small, 적절 안정성).
  - Track: E(t), H(t), min/mean gap, Wasserstein-2.
  - Forward (t > 0) and backward (t < 0) symmetric runs.

### 예상 numerical issues
- *Singular* repulsion 1/(x_k - x_j) — gaps 가 0 에 가까워지면 timestep 줄여야.
- *N=50 가 충분히 representative*? Boundary effect 가능. 단, scope 제한 인정.
- mpmath dps=20+ for stability.

## 예상 도구
- numpy + RK4 ODE.
- scipy.linalg.toeplitz 등 일반 NumPy.

## 예상 막힘 지점

1. ODE 의 *singular* term — zeros 너무 가까워지면 instability.
2. *어떤 functional 이 forward-time 단조* 인지 *알려진 답이 없다* — 시행착오.
3. N=50 으로 *meaningful* 결론 얻기 어려움. 정성 신호만.

## 성공 기준 (DoD)

- [ ] `tools/heat_flow_simulation.py` 작성 + 실행
- [ ] 첫 50 영점 ODE 적분 |t| ≤ 0.01 정도 (작은 step)
- [ ] E(t), H(t), Wasserstein-2 시간 추적 plot/표
- [ ] forward vs backward 비대칭 정량 1단락
- [ ] postmortem 의 "발견/막힘" 명확

## 명시적 실패 기준

- numerical instability 너무 심해서 *어떤 결론도 못 냄* → 작은 N (10) 으로 재시도, 그래도 실패 시 종료 + 도구 한계 기록.
- 모든 functionals 가 trivially 정합 (forward = backward 까지) → "ODE 시뮬레이션이 짧은 시간 scale 에선 비대칭 안 보임" 결론, longer-time 시도 후속.

## 알려진 한계 (정직)

- 본 시도는 Wall #2 를 *풀려는* 것이 아님. *정량화* 시도.
- 잘되면 → 정성적 비대칭 신호 + 다음 시도 후보.
- 안되면 → 본 도구의 한계 + non-numerical 시도 (정리 분석) 후속.
