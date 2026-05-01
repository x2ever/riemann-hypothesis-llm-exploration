# Postmortem — Attempt 012

## 결론

**Positive finding** — entropy 가 forward-backward 비대칭 path-dependent functional.

- dH_forward/dt > 0, dH_backward/dt < 0 — 부호 반대 ✅
- Wasserstein (대칭) 과 대조 — 채널 분리 명시 ✅
- Wall #2 우회 *후보* (Wasserstein 탈락 후) ✅

## 무엇이 작동했나

- 1 turn 으로 *positive finding* — 작은 시도의 ROI.
- 007 의 negative 가 012 의 *positive* 로 직접 진화 — sequential learning.

## 어디서 막혔나

- 본 결과의 *literature 위치* 미확인. 알려진 결과인지 (Otto's calculus, log-Sobolev) 확인 필요.

## 알려진 벽인가, 새로운 벽인가

Wall #2 의 *우회 후보* — entropy 채널. 다만 *알려진 결과 재발견* 가능성 높음.

## 다음 시도 후보

### 013 — Type E (literature 확인)
Otto's calculus / log-Sobolev / Wasserstein gradient flow 와 ζ 영점 ODE 의 연결 — 알려진 결과 검색.

### 014 — Type A (analytical 변환)
$\dot H[\mu_t]$ 의 ζ 영점에 대한 closed expression 시도.

### 015 — Type A (Wall #3 또는 #1 첫 진입) — Phase 5 plan 따름.

## 추출된 보조정리/관찰

**Observation 12.1**: ζ 영점 ODE $\dot x_k = 2 \sum 1/(x_k - x_j)$ 하 kernel-smoothed empirical measure $\mu_t$ 의 differential entropy 가:
- forward (t > 0): strictly increasing (수치)
- backward (t < 0): strictly decreasing (수치)
- bandwidth h = 0.3, N=20 영점 으로 검증.

(이는 Otto's calculus / log-Sobolev 의 알려진 fact 일 가능성 — 다음 시도에서 literature 확인.)

## 학습 누적

- `learnings/walls.md` — Wall #2 우회 후보 entropy 추가 ☐
- `learnings/cross_domain_lens.md` — Otto's calculus 를 직접 사용 채널 ☐
- `learnings/specialist_consensus.md` — S5 (Tao) + S4 (확률) 의 entropy production 시각 ☐

## HARNESS 갱신
- ledger 012 추가.

## 메타

- Phase 5 첫 시도 *positive*.
- *작은 시도 + sequential learning* 의 효율 패턴.
- 007 (negative) → 012 (positive) — *negative finding 이 positive 로 진화* 가 본 프로젝트의 핵심 메커니즘 검증.
