# Postmortem — Attempt 006

## 결론

**Partial success — Wall #2 의 *sharper formulation***.

- ODE 시뮬레이션 작동 ✅
- forward 와 backward functional monotonicity 정량 ✅
- Wall #2 의 본질 재해석: *integrated energy bound* 가 정확한 wall (단순 monotonicity 부재 X) ✅
- 다음 시도 후보 3개 도출 ✅

## 무엇이 작동했나

1. **수치 ODE simulation**: RK4 안정. 작은 |t| 에서 결과 신뢰.
2. **functionals diagnostic**: energy, hamiltonian, gap stats — 각각 다른 정보. 결합으로 monotonicity 패턴 명확.
3. **Wall #2 재해석**: 본 시도의 *진짜 산출*. wall 의 *정확한 형태* 가 무엇인지 수치로 확인.

## 어디서 막혔나

- 짧은 |t| scale 으로 *Λ 근처* 의 dynamics 미관찰. T 를 |Λ|=0.2 까지 확장하면 *singular* zero collisions 발생 위험 — adaptive timestep 필요.
- Wasserstein-2 시각 미구현 — 코드 확장 필요.

## 알려진 벽인가, 새로운 벽인가

**Wall #2 (FORWARD-TIME) 재정의**. 더 sharp 한 형태:

> **Wall #2 (refined)**: $\int_0^\Lambda E(t)\,dt$ 의 unconditional upper bound 부재.
> ($\partial_t \mathcal{H} = -4E$ monotonicity 자체는 알려져 있음.)

`learnings/walls.md` 갱신.

## 다음 시도 후보

### 007 — Type E (Literature)
**가설**: Rodgers–Tao paper 의 §3 (Riemann-von Mangoldt for H_t, Lemma 4) 와 §4 (energy bounds) 정독. ∫E(t)dt 의 known bounds 정확히 파악.
- DoD: paper 정독 + INDEX 의 사고과정 추정 보강 + work.md 의 ∫E(t)dt 에 대한 literature 정리.

### 008 — Type A (Wasserstein 시각)
**가설**: ζ 영점의 empirical measure $\mu_t = (1/n) \sum \delta_{x_k(t)}$ 의 evolution 을 Wasserstein-2 metric 위 gradient flow 로 보고 *integrated* metric 분석.
- 도구: `tools/wasserstein_evolution.py` 신규.
- 가치: optimal transport ↔ heat flow 다리 — 우리의 cross-domain 강점.

### 009 — Type C (도구 확장)
**가설**: heat_flow_simulation.py 확장 — adaptive timestep, N=100, T까지 |Λ| ~ 0.2.
- DoD: 안정 simulation, Wasserstein 추가, larger time scale.

### 010 — Type A (시도 후속)
**가설**: 만약 008 에서 Wasserstein gradient 발견 → integrated W₂² bound 시도. 이게 wall #2 우회 직접 후보.

## 추출된 보조정리/관찰

**Observation 6.1 (수치)**: 첫 N=20 ζ 영점에 대해 ODE $\dot x_k = 2 \sum 1/(x_k - x_j)$ 의 forward-time 적분 시:
- $E(t) = \sum 1/(x_j - x_k)^2$ — strict decreasing
- $\mathcal{H}(t) = -\sum_{j<k} \log|x_j - x_k|$ — strict decreasing
- $\min_k (x_{k+1} - x_k)$ — strict increasing
- $\sigma_{\mathrm{gap}}(t)$ — strict decreasing

(이는 Rodgers–Tao Theorem 11 부근의 알려진 fact 의 수치 확인 — `lemmas/` 분리 X.)

**Reframed Wall #2**: forward-time 에서 *infinitesimal* monotonicity 는 있다. 본질적 어려움은 $\int_0^\Lambda E(t)\,dt$ 의 *unconditional* upper bound 부재.

## 학습 누적

- `learnings/walls.md` — Wall #2 refined statement 추가 ☐
- `learnings/cross_domain_lens.md` — Wasserstein gradient flow 가 *직접 적용 후보* 로 진화 ☐
- `learnings/specialist_consensus.md` — S5 (Tao 류) 의 forward-time 분석 부재 = *integrated* control 부재로 sharpening ☐

## HARNESS 갱신
- ledger 에 006 추가.

## 메타

- 첫 *야심 시도* (Wall 직접 도전).
- *완전 정복 X* 이지만 wall 의 *정확한 형태* 재해석 — 다음 시도들의 강력한 입력.
- 본 패턴: Wall 도전 → 부분 정복 또는 wall 의 sharpening — *항상* 가치 산출.
- LLM cross-domain 강점 발현 시작 — Wasserstein/optimal transport 가 다음 시도의 핵심 도구.
