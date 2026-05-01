# Approaches Taxonomy — 진화하는 접근법 분류

> attempt 000 (orientation) 산출. `background/approaches.md` 의 *정적 분류* 를 본 파일에서 *진화* — 새 결합·새 우선순위·새 분류는 본 파일에 누적.

## 11개 기본 분류 (background/approaches.md 참조)

I. 해석적 (mollifier)
II. 동치 변환
III. Spectral / Hilbert–Pólya
IV. NCG / Connes
V. Function field 유추
VI. de Bruijn–Newman / heat flow
VII. RMT
VIII. Families / Iwaniec
IX. Numerical
X. Probabilistic
XI. Unconventional

## 결합 가능 쌍/삼중 (000 식별)

### Strong combos (시도 가치 높음)

#### Combo 1: II + VI (동치 + heat flow)
- 아이디어: 동치 형태 (Mertens, Li, Nyman) 를 heat flow 변형 — $M_t(x), \lambda_n^{(t)}, \eta^{(t)}_\alpha$ family 정의.
- 우선순위: ★★

#### Combo 2: III + VI (spectral + heat flow)
- 아이디어: BBM 류 Hamiltonian 의 *time-evolved* version. heat flow 와 spectral 동시.
- 우선순위: ★★ (high variance)

#### Combo 3: V + VII (function field + RMT)
- 아이디어: Katz–Sarnak symmetry types 의 number field family 적용 + L-function conspiracy 정량 통제.
- 우선순위: ★★★ (Iwaniec 라인의 자연 확장)

#### Combo 4: II + VII + IX (동치 + RMT + computational)
- 아이디어: Li's λ_n 의 sign distribution 을 GUE 와 정량 비교. 코드 강력.
- 우선순위: ★★★ (작고 검증 가능 — 첫 시도 후보 A)

### Promising new combos (additional candidates)

#### Combo 5: VI + X (heat flow + 확률)
- 아이디어: zeros heat flow 를 stochastic process 로 보고 stationary distribution 분석.

#### Combo 6: III + XI (spectral + Lee-Yang)
- 아이디어: Lee-Yang style positivity 를 ζ 에 직접 import 시도.

#### Combo 7: V + III (function field + spectral)
- 아이디어: function field 측 cohomology 의 spectral 표현을 number field 에 옮김 (Connes program 의 본질이 사실 이것).

#### Combo 8: I + VIII (mollifier + families)
- 아이디어: 다중 mollifier on family — variational / multi-objective.

## 우선순위 (000 평가, 다음 시도들 진행하며 갱신)

### Tier S (즉시 시도 가치)
- Combo 4 (II+VII+IX) — `001_li_criterion_rmt_cross_check`
- Combo 1 (II+VI) — 동치 + heat flow

### Tier A (강한 관심)
- Combo 3 (V+VII) — Iwaniec 후속
- Combo 2 (III+VI) — high variance, high reward
- Single XI (Lee-Yang direct import)

### Tier B (보조 / brainstorm)
- Combo 5, 6, 7
- Single V (function field 직접) — specialist depth 부족 시 risky
- Single XI 개별 채널

### Tier C (defer)
- Single I (mollifier push) — specialist 영역
- Single IX (numerical SOTA) — HPC 영역
- Combo 8 — Iwaniec specialist 영역

## 분류 갭 (현재 분류로 못 잡는 채널)

### 갭 1: *Riemann 본인의 explicit formula* 시각
- "RH 가 부산물" 시각 — 11개 분류 모두 RH 를 *직접* 노림.
- 신규 분류 후보: **XII. Macro / Indirect** — 더 큰 structure 안에서 RH 가 자연 결론.
- 후보 시도: `003_byproduct_search`.

### 갭 2: *논리 / 메타수학* 채널
- §XI (Unconventional) 안에 있으나 분리 가치.
- 신규 분류 후보: **XIII. Metamathematical** — RH 의 ZFC/PA 위 위치, 독립성.
- 우선순위 낮음 (직접 증명 도구 X) but cross-cut.

### 갭 3: *통합 양정치성 (Wall #1~5 의 메타)*
- `walls.md` 의 메타 가설: 모든 벽이 "산술적 양정치성 부재" 의 표현.
- 분류라기보다 *목표* — "양정치 form 발견" 이 통합 목표.

## 우선순위 변경 trigger

다음 시도들 진행하며 본 파일 갱신:
- 어떤 combo 가 *예상보다 좋은 결과* → 우선순위 ↑
- 어떤 combo 가 *반복적으로 실패* → 우선순위 ↓
- 새 combo 떠오름 → 추가
- 새 분류 갭 → 추가

## 사용 ledger

| Attempt | 사용 분류/combo | 결과 |
|---|---|---|
| 000 | meta | 11+4 정리, 5 갭, 3 다음 후보 |
| 001 | Combo 4 (II + VII + IX) | **부분 부정**: naive cross-check 무의미 (벽 #6 LOCAL-GLOBAL-MISMATCH). 우회: unfolded, Keating–Snaith. |

## 갱신 (attempt 001 학습)

### Combo 4 의 한계 — *공통 layer* 필요
- 단순 결합으로는 동치들이 cross-check 안 됨 (벽 #6).
- 보강: Combo 4' (II + VII + IX with *unfolded local statistics*) 우선순위 ↑.

### 새 분류 후보 (attempt 001 의 부산물)
- **XII. Free probability** (S11 의 R-transform) — XI 안에 있던 채널을 *분리*.
  - 우선순위: ★★ (high variance)
  - 후보 시도: `004_li_lambda_rtransform`
