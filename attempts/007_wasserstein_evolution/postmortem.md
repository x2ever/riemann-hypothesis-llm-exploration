# Postmortem — Attempt 007

## 결론

**Negative finding (informative) — Wasserstein 부적합**.

- W₂(μ_t, μ_0) 가 *시간 방향 대칭* — forward/backward 구별 X.
- Wall #2 우회 후보 중 Wasserstein 채널 *탈락*.
- Cross-domain candidates list 좁아짐.

## 무엇이 작동했나

- 빠른 numerical experiment (1 turn) 으로 Wasserstein 채널의 *부적합* 확정.
- Otto's calculus 의 *한계* 가 본 시도에서 명시적으로 드러남.
- 006 의 도구 (heat_flow_simulation) 재사용 — 시도 간 도구 공유 효율 검증.

## 어디서 막혔나

본 시도에서 *예상한* 막힘 — Wasserstein 이 비대칭 못 보는 것 자체가 핵심 발견. 막힘 = 학습.

## 알려진 벽인가, 새로운 벽인가

새 *세부 벽* 아닌 — wall #2 의 우회 후보 탈락 1개. `learnings/walls.md` 의 wall #2 우회 후보 리스트에서 Wasserstein 제거.

## 다음 시도 후보

### 008 — Type B (Mid-stream Re-orientation)
6+ attempts 누적 — 종합 시점. RMT 채널 (005 D 에서 종합), heat flow 채널 (006, 007 진행), 그러나 broader stock-take 미실시.

### 009 — Type A (Path-dependent functionals)
KL divergence, free energy, entropy production — Wasserstein 와 달리 *경로 종속*. forward-backward 비대칭 캐치 가능.

### 010 — Type A (Wall #5)
BBM Hamiltonian finite truncation — 새 채널, code 강점.

## 추출된 보조정리/관찰

**Observation 7.1 (수치)**: ODE $\dot x_k = 2 \sum 1/(x_k - x_j)$ 하 Wasserstein-2 distance $W_2(\mu_t, \mu_0)$ 가 *|t| 의 함수* — forward/backward 대칭 (small |t| ≤ 0.001, N=20 에서 확인). 

[plausible] 이는 *isotropic* transport 의 산물 — 일반적으로 Otto's calculus 의 quadratic 시작점 $W_2^2 \sim |\dot \mu|^2 t^2$.

## 학습 누적

- `learnings/walls.md` — wall #2 우회 후보에서 Wasserstein 탈락 표시 ☐
- `learnings/cross_domain_lens.md` — Wasserstein 이 *대칭 functional* — 비대칭 캐치 X 노트 ☐
- `learnings/approaches_taxonomy.md` — XI 우회 후보 좁아짐 ☐

## HARNESS 갱신
- ledger 에 007 추가.

## 메타

- *negative finding 의 가치* 다시 한 번. 본 시도가 1 turn 으로 해결.
- 008 = Type B mid-stream re-orientation 권장 — type 다양화 + 누적 데이터 종합.
