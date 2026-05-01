# Work — Attempt 012

## 2026-05-01 — entropy 시간 진화

[numerical, dps=30, N=20, T=0.001, bandwidth=0.3, RK4]

### 결과

| direction | t | H[μ_t] | ΔH |
|---|---|---|---|
| forward | 0.001 | 3.206017 | **+4.65e-5** |
| backward | -0.001 | 3.205924 | **-4.70e-5** |

### 핵심 발견

**Differential entropy H[μ_t] 가 forward-backward 비대칭** — Wasserstein (007 대칭) 과 대조.

- forward (t > 0): dH/dt ≈ +4.65e-2 (양, 단조 증가)
- backward (t < 0): dH/dt ≈ -4.70e-2 (음, 단조 감소)
- 부호 반대 — **strict anti-symmetric path-dependent functional**.

### 분석

[rigorous]:

- 영점이 forward 에서 *spread out* (repulsion 동역학) → kernel density 더 *균일* → 미분 entropy *증가*.
- backward 에선 *cluster* → density 더 *peaked* → entropy *감소*.
- 이 비대칭이 *isotropy 깨는* functional 후보.

[plausible]:

- Wasserstein-2 가 시간 대칭이었던 이유: 거리는 *경로 독립* — 출발지로부터의 거리만.
- entropy 는 *경로 종속* — 측도의 *형태* (concentration vs spread) 에 의존.
- 따라서 entropy 가 forward-backward asymmetry 의 *natural marker*.

### Wall #2 우회 후보 — entropy 채널

[plausible]:

본 결과가 Wall #2 의 *forward-time control* 채널 후보 제공:
- forward 에서 H[μ_t] 단조 증가 가정 시, $\int_0^T \dot H\,dt = H[\mu_T] - H[\mu_0] \ge 0$.
- 이걸 ODE 와 결합: $\dot H = \int (\dot \rho_t)(\log \rho_t + 1)\,dx$.
- ρ̇_t = -∂_x (ρ_t v_t) where v_t = drift field of zero ODE.
- 즉 $\dot H = -\int \rho_t (\partial_x \log \rho_t) v_t\,dx$.

이게 어떤 *integrated bound* 를 제공할 수 있는지가 다음 단계. (006 의 ∫E(t)dt 와 어떤 관계?)

### 다음 시도 후보

#### 013 — Type A (entropy bound 정량)
$\dot H[\mu_t]$ 와 energy E(t) 사이의 *알려진 부등식* 검색 — 가능하면 *log-Sobolev* 또는 *Otto's calculus* 형식. literature 확인.

#### 014 — Type E (literature)
Otto's calculus + log-Sobolev + Lott-Sturm-Villani 관련 paper 다운로드. 본 결과의 *진짜 의미* 평가.

#### 015 — Type A (계속 Wall #2)
$\dot H$ 의 ζ 영점 자체에 대한 *closed* 표현 시도. 본 시도의 numerical 을 analytical 로.

### 결론

**Positive — path-dependent functional 발견** (entropy). Wall #2 우회 채널의 *첫* 후보.

다만 cautious:
- 본 결과는 *이미 알려진 결과* 일 가능성 매우 높음 (entropy production = energy + Otto's calculus).
- *literature* 확인 필요 — 알려진 사실 재발견인지, 새 angle 인지.
