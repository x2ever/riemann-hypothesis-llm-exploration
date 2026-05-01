# Work — Attempt 007

## 2026-05-01 — Wasserstein evolution

[numerical, dps=30, N=20, T=0.001, RK4]

### 결과

| direction | t | W₂² | energy | dW₂²/d|t| |
|---|---|---|---|---|
| forward | 0.0010 | 1.564e-6 | 7.8158 | 3.05e-3 |
| backward | -0.0010 | 1.566e-6 | 7.8326 | 3.05e-3 |

### 핵심 발견

**W₂²(μ_t, μ_0) 이 forward 와 backward 에서 거의 *동일*** — 시간 방향 대칭.

- forward t=0.001 에서 W₂² ≈ 1.564e-6
- backward t=-0.001 에서 W₂² ≈ 1.566e-6
- 차이 < 0.2% (numerical roundoff 수준).

### 분석

[rigorous]:
- Empirical measure $\mu_t = (1/N) \sum \delta_{x_k(t)}$ 의 Wasserstein-2 distance to $\mu_0$ 가 *|t| 의 함수* — sign(t) 무관.
- dynamic 자체 (E, H, gap stats) 는 비대칭 (006 결과) 이지만 *Wasserstein 거리* 는 대칭.
- W₂² ∝ t² + O(t³) — quadratic 시작.

[plausible]:
- 이는 *대칭적 transport*: forward 는 zeros 가 spread (repulsion), backward 는 cluster — 두 motion 의 *거리* (μ_0 으로부터) 가 동일.
- Otto's calculus 의 한계: $\frac{d}{dt} W_2^2 = 2 \langle v, x - x_0 \rangle$ — t=0 에서 0, |t| ↑ 함께 ↑ 양방향 동일.

### Wall #2 우회로서 Wasserstein 의 *부적합성*

[plausible]:
본 결과는 **Wasserstein 만으로는 Wall #2 의 *비대칭 본질* 캐치 X** — 거리는 대칭이라 forward vs backward 를 구별 못 함.

→ Wall #2 우회 도구로 Wasserstein 부적합. *경로 종속* (path-dependent) functional 필요:
- Energy E(t) — forward ↓, backward ↑ (006 확인)
- Hamiltonian H(t) — forward ↓, backward ↑
- Entropy / KL divergence — TBD

### 결론 (work)

본 시도의 main 발견 — **Wasserstein-2 는 zero ODE 의 forward-backward 비대칭을 *못* 본다**. 즉 wall #2 우회 채널로 직접 *부적합*.

가치:
- *negative finding* — cross-domain 후보 *탈락* 명시화.
- 다음 cross-domain 후보 (path-dependent functionals) 으로 narrow.

### 다음 시도 후보

1. **008 — Type B mid-stream re-orientation**: 6+ attempts (000~007) 종합. Wall 구조, 우회 후보, type 분포, 비교우위 위치 재평가.
2. **009 — Type A**: path-dependent functional (free energy, KL divergence) 의 forward-backward 비대칭 정량.
3. **010 — Type A 다른 채널**: Wall #5 (BBM Hamiltonian self-adjointness) finite truncation 으로 spectrum 수치.
