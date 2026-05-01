# Work — Attempt 000

## 2026-05-01 — orientation 진행

### Step 1: background 4파일 작성 [completed]
- `definitions.md`: ζ, ξ, Ξ, Λ, ψ, M, N(T), L-functions
- `functional_equation.md`: 두 증명 (Riemann 1859), 임계선 = 1/2 의 의미, 함수방정식이 *주는* 것과 *주지 않는* 것
- `known_results.md`: A (증명) / B (추측) / C (반례·실패) / D (수치) / E (RH 결과) / F (사용 가능 lever)
- `approaches.md`: 11개 분류 + 5개 본질적 벽 (A–E) + 행동 권장

### Step 2: papers/INDEX.md 사고과정 추정 [completed]
- 8편 모두 *결과 + 출발점 가설 + 핵심 도약 + 막혔던 곳 + 메타 학습* 5요소 채움.
- 가장 가치있는 통찰:
  - **Riemann 1859**: RH 가 *주된 statement 가 아니라* explicit formula 의 *부산물*. → "RH 를 직접 풀려 하지 말고 더 큰 그림의 부산물로 풀릴 가능성" — 본 프로젝트의 *macro hint*.
  - **Bombieri Clay**: 핵심 미해결 = "number field 의 cohomology 대응물" — 한 문장으로 *중심 갭* 명시.
  - **Conrey 2003**: "RH 는 진짜 *arithmetic* 질문" — 해석적 도구 한계 인정. families 가 main current.
  - **Rodgers–Tao**: backward time 분석으로 Λ ≥ 0 — *forward time* 비대칭이 RH 의 본질적 어려움.
  - **BBM**: *형식적* spectrum 일치는 가능, *self-adjointness rigorous* 가 본질 갭.

### Step 3: specialist 라운드 [completed]
- 7명 (S1, S2, S3, S4, S5, S6, S9) 호출.
- 결과: `specialist_round.md`.
- **핵심 강화**: S2 + S3 + S6 가 모두 *positivity 의 본질* 로 수렴 — function field 의 algebraic index theorem ↔ NCG 의 Weil distribution positivity ↔ Lee-Yang 류 positivity. 셋이 같은 본질을 다른 언어로 보고 있을 가능성.
- **핵심 격차**: forward-time zero 동역학 통제 (S5 만 인지하고 답 X), Frobenius char 0 대응물 (S2/S3 인지, 답 X).
- **운영 결함 발견**:
  - S2 와 S3 의 답이 너무 정합적 — confirmation bias 가능. 향후 *blind* round 필요.
  - Tier 1 의 5명 분류가 *대수기하 vs 대수적 정수론* 을 분리 못 함.

### Step 4: 본질적 벽 (walls) 추출 [in progress]
`approaches.md` §메타 의 5개 벽 (A–E) 을 더 정량화·구체화:

#### 벽 #1 (FROBENIUS-GAP): char 0 의 Frobenius 대응물 부재
- 영향: §IV (NCG), §V (function field), §VIII (families) 의 *상한*.
- 정량 신호: Connes 1999 → 2021 의 25년 진화에도 trace formula 의 *한쪽 양정치성* 미증명.
- 우회 후보: motivic cohomology, arithmetic site, Deninger foliated dynamics — 모두 *정의는 있으나 증명 도구 부재*.

#### 벽 #2 (FORWARD-TIME): heat flow forward-time zero 통제 부재
- 영향: §VI (de Bruijn–Newman) — 비대칭의 본질.
- 정량 신호: Rodgers–Tao 2020 후 5년, Λ ≤ 0 무진전.
- 우회 후보: optimal transport (Wasserstein gradient flow), Calogero-Moser integrable, Ricci flow.

#### 벽 #3 (SHARP-CONSTANT): mollifier 의 50% 벽
- 영향: §I (해석적), §VIII (families) 의 *상한*.
- 정량 신호: Levinson 1/3 → Conrey 40.2% → Bui–Conrey–Young 41.05% — 50% 한참 못 미침.
- 우회 후보: families 평균, mollifier 가족 (다중 개수 동시).

#### 벽 #4 (CONSPIRACY): L-function conspiracy / Landau–Siegel
- 영향: §VIII (families) 의 *상한*.
- 정량 신호: Iwaniec 의 "extra little tiny bit" — 50% 의 +1bit.
- 우회 후보: 새 family construction, exotic L-functions (Iwaniec 의 high rank elliptic).

#### 벽 #5 (SELF-ADJOINT-RIGOR): spectral 후보의 self-adjointness rigorous 부재
- 영향: §III (Hilbert–Pólya), §IV (NCG).
- 정량 신호: Berry–Keating 1999 → BBM 2017 → 후속 논문들 — 모두 *형식적 일치* 단계 못 넘음.
- 우회 후보: deficiency index 계산, Krein theory, modular operator (Tomita–Takesaki).

### Step 5: 결합 가능 쌍/삼중 식별 [in progress]
`approaches.md` 의 11개 분류를 *함께* 적용하면 strong 한 시도:

#### 결합 1: II + VI (동치변환 + heat flow)
- Mertens 동치 ($M(x) = O(x^{1/2+ε})$) 를 heat flow 시각으로 — $M_t(x)$ family 정의 후 forward-time 분석.
- 미탐색 가능성. cross-domain S5 호출.

#### 결합 2: III + VI (spectral + heat flow)
- BBM Hamiltonian Ĥ 의 *time-evolved* version $H_t$ — heat flow 의 spectral 해석 + Newman 류 통일.
- specialist S3 + S5 + S6 동시.

#### 결합 3: V + VII (function field + RMT)
- Katz–Sarnak symmetry type 분석을 number field 의 *partial* (작은 conductor) family 에 적용 + family conspiracy 의 정량 통제.
- specialist S2 + S4.

#### 결합 4: II + VII + computational
- Li's criterion λ_n ≥ 0 + RMT moments 정합성 + 수치 검증 — 세 동치 가지에서 같은 결과.
- 도구: `tools/li_criterion.py` + RMT moment 추가 모듈 + cross-check.

### Step 6: 다음 시도 후보 도출 [in progress]
postmortem 에 정리.

## 메모

- **자기 회의 점검**: 본 orientation 의 *분류와 벽* 이 모두 문헌에 *암묵적으로* 이미 있는 것. 본 프로젝트의 *비교우위* 는 *분류 자체* 가 아니라 (i) 분류의 *명시화 + 누적* (ii) *결합 시도* (iii) cross-domain 강제 (iv) 코드 동시 (v) specialist 패널 강제. 다음 시도들에서 이 5개 채널이 진짜 가치를 만들어내는지 검증.

- **함정 자기 진단**: 본 작업이 *너무 평면적* — 분류가 그럴듯하나 실제로 *벽 #1~#5* 가 진짜 본질적인지 확신 X. 다음 시도가 진짜 막힐 때 어디서 막히는지가 진짜 검증.

- **Riemann 1859 의 통찰 재강조**: RH 가 *부산물* 가능성. 시도 후보 중 *RH 를 직접 노리지 않는* 시도가 1개 이상 포함되어야 함.

[numerical, dps=50] verify_zeros.py -n 50 — 첫 50개 영점 모두 Re=1/2. baseline OK.
