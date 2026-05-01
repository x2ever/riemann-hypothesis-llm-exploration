# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 본 레포의 본질 (먼저 읽기)

이 디렉토리는 **일반적 소프트웨어 프로젝트가 아니다.** Riemann 가설(RH)에 대한 *반복적 증명 시도와 누적 학습 시스템*이다.

- **Calibration**: RH 는 1859년 이후 165+ 년간 미해결. 본 프로젝트의 *현실적 목표는 증명이 아니라 "체계적으로 시도하면서 어디서·왜 막히는지 누적 학습"*이다 (`README.md` 캘리브레이션 섹션).
- **현재 상태 (~2026-05)**: 181+ attempts 진행, 6 walls, 7 lemmas, 19 evidence × 27 tissues, 17 PDFs. **진정 RH 진전 0/10** (외부 감시자 평가 인정).
- "증명했다" 라고 느끼면 거의 확실히 오류 (95%+ 미묘한 가정 누락 / 순환 논리). `HARNESS.md §3` 의 "증명했다" 트리거 4 체크 필수.

새 instance 는 작업 시작 전 **반드시** `README.md` + `HARNESS.md` + `SPECIALISTS.md` 정독. 본 CLAUDE.md 는 그 위에 *operational summary*.

## 작업 흐름 (절대 준수)

### 1. 새 시도 시작 전 의무 사전 작업
1. `learnings/` 전체 빠르게 재훑기 (특히 `walls.md`, `external_critique_2026-05.md`, `specialist_intuition_gaps.md`).
2. 직전 attempt 의 `postmortem.md` 정독 — 같은 벽 반복 회피.
3. `lemmas/dont_try_directions.md` 의 Cut 1-7 자가 검토 — 본 시도가 부분 재시도면 컷 또는 *재고려 사유* 명시.
4. 추가 lemmas 도 살피기: `positivity_unification_hypothesis.md`, `failed_proof_categories.md`, `specialist_delta_anchoring_protocol.md`.

### 2. Attempt 폴더 생성 (시간순 NNN, 이미 181까지 사용됨)
```
attempts/NNN_<keyword>/
├── strategy.md       # 시작 전 — Type 명시 (A/B/C/D/E), 가설, 막힘 예측, DoD, Positivity check
├── work.md           # 진행 중 누적 — 시간순, 각 단계 [rigorous|plausible|hand-wave|guess] 태그
├── specialist_round.md   # (Tier 1 + 관련 Tier 2 specialist 호출 결과)
└── postmortem.md     # 끝/중단 시 — 결과, 막힘, lemma extraction, 예상 가능 self-check
```

### 3. **Pre-batched plan 거부** (외부 critique #6, ~attempt 181 신규)
- `mkdir attempts/NNN-MMM` (5+ directory 미리 생성) **금지**.
- 각 attempt 끝나면 *postmortem* 결과 → 다음 attempt *그때 결정* (lazy planning).
- "180까지", "100개 더" 같은 milestone-driven attempt 거부 — *quality threshold* 도달 시만 milestone.
- Mode A deep 9th component: **Pre-iteration reflection** — strategy.md 시작에 직전 postmortem 직접 인용 + 본 attempt quality basis.

### 4. 5가지 Attempt Type (strategy.md 첫 줄 의무 표시)
| Type | 의미 | 산출 |
|---|---|---|
| **A** | Proof attempt — 좁은 가설 직접 증명/반증 시도 | lemma, partial result, 명시적 막힘 |
| **B** | Meta / orientation — 지도·분류·가능성 평가 | learnings/, 분류, 다음 후보 |
| **C** | Harness maintenance — 하네스 자체 개선 | HARNESS / SPECIALISTS / tools 변경 |
| **D** | Reflection / idea-refresh — 시간차 후 재검토 | 재해석, 새 우회, 폐기 확정 |
| **E** | Literature deepening — 논문 정독 + INDEX 갱신 | papers/ 추가, 사고 과정 추정 강화 |

> Type A 만 누적하면 narrow. B/C/D/E 도 정기적으로. Mode A minimal (얕은 stamp/sanity) **거부** — Mode A deep 의무 (`HARNESS.md §0`).

### 5. 매 시도 의무 3-pass (생략 금지)
- **Breadth pass (§6)**: cross-domain 유추 — analogy sweep + tool import + outsider 질문 + problem morphing.
- **Depth pass (§7)**: Tier 1 (S1-S5) 전부 + Tier 2 1-3 specialist 호출. 큰 시도는 Blind round 의무.
- **Computational lever (§8)**: numerical sanity / equivalent reformulation / counterexample search 중 1개 이상.

## 정직 (Honesty) 규율 — 절대

자기기만이 가장 큰 적. 다음 강제:

1. **확신도 태깅**: 모든 비자명 단계에 `[rigorous|plausible|hand-wave|guess]` 중 하나.
2. **순환 논증 체크**: 결론을 어디선가 (변형된 형태로) 가정하지 않았나?
3. **수치 ≠ 증명**: `[numerical, dps=50, n=10^4]` 같은 메타데이터 의무. n=10^6 까지 성립 ≠ ∀n.
4. **알고리즘 한계 인지**: 영점 계산 자체가 RH 가정 하 빠른 알고리즘 (Riemann-Siegel) — 순환 의존 주의.
5. **Yellow flag 단어 list** (외부 critique #2, attempt 045): "resolved", "확정", "증명" 사용 시 retracted 검토. 자율 stamp 금지.
6. **NOVEL Quota** (외부 critique #5): paper 외부 cross-domain 시도 = 1회 sequence 만. paper-direct rediscovery 인지 시 즉시 종결, paper-direct deep 복귀.
7. **Specialist Δ Anchoring** (Lemma 7): §8 Specialist Δ 작성 시 paper §끝 quote anchor 의무. quote 외 추정 = 환각 위험 명시.
8. **"novel content 0/10" affirmation**: Mode A deep 매 attempt postmortem 의무.

## 디렉토리 지도

```
prove_riemann_hypothesis/
├── README.md            # 미션, 캘리브레이션, 현재 상태, attempts ledger 요약
├── HARNESS.md           # 반복 루프 명세 (§0-§8) — 가장 중요한 master spec
├── SPECIALISTS.md       # 분야별 specialist 패널 운영 protocol
├── background/          # definitions, functional_equation, known_results, approaches (4 files)
├── papers/
│   ├── INDEX.md         # 논문 17편 사고 과정 추정 + 우선순위
│   ├── WISHLIST.md      # 다음 다운로드 후보
│   ├── pdf/             # PDF 파일들 (17개)
│   └── notes/           # (선택) 논문별 정독 노트
├── attempts/NNN_<key>/  # 시도별 (000_orientation ~ 181_external_critique_6_response_pre_batched)
├── learnings/           # walls.md (6 walls), cross_domain_lens, specialist_*, external_critique_*
├── lemmas/              # 검증된 보조정리 7개 — 재사용 가능 (재증명 금지)
└── tools/               # 38개 mpmath/sympy 모듈 (uv 기반)
```

## 도구 (tools/) 사용

```bash
cd tools
uv sync                                    # 첫 setup
uv run python verify_zeros.py -n 50 --dps 50      # 영점 검증 예시
uv run python li_criterion.py -N 20 --zeros 100   # Li's λ_n 계산 예시
uv run python pair_correlation.py -n 200 --bins 20 # GUE pair correlation
```

- Stack: Python 3.12+, mpmath, sympy, numpy, matplotlib (uv lockfile 존재).
- Format: ruff line-length 100, double quotes.
- 새 모듈 추가는 *시도 진행 중 필요할 때만* — 미리 만들지 않음. docstring 에 *수학적 정의* + *알려진 한계* 명시.
- 모든 코드 호출 결과는 work.md 에 `[numerical, dps=N, ...]` 태그 + `tools/<file>.py:func` reference 포함.

## 논문 읽기 프로토콜 (HARNESS §2)

논문은 결과뿐 아니라 **저자가 그 아이디어에 도달한 사고 과정 추정**까지 기록:
- 출발점 가설, 핵심 도약 (key leap), 막혔을 만한 곳, 버려진 시도 추정.
- `papers/INDEX.md` 에 표면 / 심층 / 메타 3-tier 작성. 예시는 INDEX.md 의 [riemann1859], [bombieri-clay] 항목.
- 새 PDF 추가: `uv run python tools/fetch_paper.py arxiv <id> --key <slug>` → INDEX.md 스텁 stdout → 사람이 직접 편집.

## 주요 Lemmas (재사용 — 재증명 금지)

- `lemmas/positivity_unification_hypothesis.md` — 5 walls 의 positivity component mapping (synthesis, *proof X*).
- `lemmas/spectral_candidate_circularity_check.md` — 6 axiom + Lemma 1 11-axiom (Sierra/BBM/Connes-Consani 등 평가).
- `lemmas/levinson_durbin_mollifier_open_question.md` — Mollifier non-Toeplitz, signal-processing 후보 탈락.
- `lemmas/dont_try_directions.md` — Cut 1-7, pre-attempt self-check 입력.
- `lemmas/failed_proof_categories.md` + `failed_proof_catalog_publishable.md` — 6 categories (Atiyah/de Branges/BBM/Lagarias §8 매핑).
- `lemmas/specialist_delta_anchoring_protocol.md` — Lemma 7, paper §끝 quote anchor 의무 (Mode A deep).

## 기존 6 Walls (반복 충돌 패턴)

| # | 이름 | 본질 |
|---|---|---|
| 1 | FROBENIUS-GAP | number field 위 Frobenius 대응물 부재 (Connes/Deninger 미해결) |
| 2 | FORWARD-TIME | ∫E(t)dt unconditional bound 부재. 현재 0 ≤ Λ ≤ 0.2 |
| 3 | SHARP-CONSTANT | mollifier 50% 한계, *one logarithm distance* (Pratt-Robles) |
| 4 | CONSPIRACY | family 분리 / Landau-Siegel 미제거 |
| 5 | SELF-ADJOINT-RIGOR | spectral candidate 자기수반 확장 부재 (Sierra/BBM/Connes-Consani) |
| 6 | LOCAL-GLOBAL-MISMATCH | trivial zeros / archimedean log n / exponential cancellation 정량화 |

매 시도 postmortem 에 *어느 wall 에 부딪혔는지* `learnings/walls.md` 에 한 줄 추가.

## 커뮤니케이션 스타일

- 보고서/문서 한국어. 영어 인용은 quote 그대로.
- 코드 레벨 설명보다 *작업 중심* 설명 선호. 간결, 핵심만.
- Strategy 단계 cross-domain pass / specialist 패널이 *빈약하면 시도 자체가 빈약*. 시간 충분히 투입.
- "stop signal" 시 자율 진행 즉시 중단. CronCreate heartbeat 운영 시 사용자 stop signal → CronDelete.

## Heartbeat (자율 운영, cycle-aware — 외부 critique #7 반영)

`HARNESS.md §Sustained Research Cycle` 참조. heartbeat 가 *1 fire = 1 attempt stamp* 로 굳지 않도록 **4-Phase Cycle** 운영:

1. **Phase 1 — Ideation + Planning** (1 fire): `planning.md` 작성. *직관 훈련 섹션* 의무 (후보별 first-impression score + 근거). Cross-domain §6 + Specialist §7 blind round. 1개 narrow hypothesis 선택.
2. **Phase 2 — Sustained Research** (여러 fire, 같은 attempt 폴더): work.md 다중 turn 누적. 한 fire stamp 폐쇄 거부. DoD / 명시적 막힘 deep 이해 / 진전 X 3 연속 까지 지속.
3. **Phase 3 — Conclusion + Meta-learning** (1 fire): postmortem.md + `learnings/sustained_research_log.md` 갱신 (직관 적중률, meta 교훈). `learnings/intuition_calibration.md` 누적.
4. **Phase 4 — Iterate**: Phase 1 복귀, 직전 meta 교훈 명시 인용.

**Heartbeat = Stop hook 자동 monitoring** (Cron / ScheduleWakeup 폐기):
- `.claude/hooks/phase_monitor.py` (Stop hook) 가 매 응답 후 transcript 파싱 → phase token 검출 시 자동 continuation.
- 응답 끝 줄에 token 명시 의무: `[Phase 1 complete]` / `[Phase 2 turn N in progress]` / `[Phase 2 complete]` / `[Phase 3 complete]` / `[Cycle complete, next ideation ready]`.
- Token 없음 = 자연 종료 (사용자 수동 fire 까지 대기).
- ScheduleWakeup / Cron 호출 *불필요* — token 만 정확히 명시.
- 최초 시작: 사용자 명시 "cycle 시작" 또는 첫 heartbeat fire.
- 무한 루프 방지: `stop_hook_active` 플래그 + Phase 2 안전장치 (DoD 또는 진전 X 3 turns 연속).

## 절대 금지

- "증명 완료" 단정 (HARNESS §3 의 4 체크 통과 X 시).
- Pre-batched plan / mkdir 5+ directory 미리.
- Mode A minimal stamp (얕은 sanity check 만 50줄 미만 work.md).
- Specialist Δ paper quote anchor 없이 추정 (Lemma 7 위반).
- NOVEL spree (paper 외부 cross-domain idea 연속 시도) — 1회 sequence 만.
- Yellow flag 단어 ("resolved", "확정") 검증 없이 사용.
- 사용자 명시 권한 없이 git 명령 실행.
