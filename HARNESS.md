# HARNESS — 반복 루프 명세

## 0. Attempt Types — 시도의 종류

> **매 시도가 증명일 필요는 없다.** 증명에 *필요한 모든 활동*이 attempt 으로 의미있다. *증명 시도가 아닌 시도들* 이 본 프로젝트의 절반 이상을 차지할 수 있고, 이것은 결함이 아니라 본 하네스의 의도된 운영 방식이다.

### 5가지 attempt type

#### Type A — Proof attempt (증명 시도)
좁은 가설을 정해 *직접* 증명·반증·정량 결과 도출 시도.
- 예: "Li's λ_n ≥ 0 의 새 sufficient condition 발견", "특정 mollifier 변형의 비율 push", "한 동치 형태의 새 부분 결과".
- 산출: lemma, partial result, 또는 명시적 막힘.

##### Mode A deep (사용자 명시 ~attempt 103+, 외부 critique #4 반영 ~attempt 107+)
- *Mode A minimal* (얕은 stamp/sanity) 거부.
- 각 deep attempt 의 의무 component:
  1. **Paper section deep read** (multi-page, key theorems quoted).
  2. **Numerical 검증 또는 derivation 재현** (quantitative).
  3. **Wall taxonomy mapping** (paper-direct, 어떤 wall sharpening).
  4. **Lemma 적용 또는 갱신** (재사용 가능 templete).
  5. **Cross-reference w/ 다른 paper / 시도** (consistency).
  6. **Open questions 도출** (다음 시도 입력).
  7. **Yellow flag check + novel content 0/10 affirmation**.
  8. **Specialist Δ 추정** (외부 critique #4 신규):
     - "Sarnak/Tao/Connes 라면 본 attempt 를 보고":
       (i) 이미 알려져 있나? (paper 인용 시 yes).
       (ii) 컷 사유는? (방향/wall/기술 부족).
       (iii) sharp navigation 추정.
     - 추정 자체가 *틀릴 수 있음* 명시.
     - 참조: `learnings/specialist_intuition_gaps.md`, `lemmas/dont_try_directions.md`.
- **Pre-attempt cut self-check** (외부 critique #4 신규):
  - strategy.md 작성 시 self-check: 본 시도가 `lemmas/dont_try_directions.md` Cut 1-6 중 부분 재시도?
  - 만약 yes → 컷 (또는 명시 *재고려 사유* 작성).
- 분량: work.md ≥ 50 lines. stamp 절대 금지.
- **NOVEL Quota** (외부 critique #5 신규, ~attempt 136):
  - NOVEL 시리즈 (paper 외부 cross-domain idea 시도) = *1회 sequence 만*.
  - sequence 내 첫 attempt 가 *paper-direct rediscovery* 또는 *expected failure* 인지 *빨리 인지*.
  - paper-direct rediscovery 인지 시 → *즉시 sequence 종결*. 다음 attempt = paper-direct deep 복귀.
  - 양적 압박 (사용자 "더 시도", "더 많이") 에서도 NOVEL spree 거부 — *quality first*.
  - 사례: 118-130 NOVEL spree (외부 critique #5 #1 인정, ROI 음수).
- **Specialist Δ Anchoring** (외부 critique #5 #2, Lemma 7):
  - §8 Specialist Δ 작성 시 paper §끝 quote anchor 의무.
  - quote 외 추정 = 환각 위험 명시.
  - 참조: `lemmas/specialist_delta_anchoring_protocol.md` (Lemma 7).
- **Lemma 3 Connective Tissue** (외부 critique #5 #3):
  - 다음 paper-direct attempts 에서 *paper A positivity ↔ paper B positivity* 의 *수학적 isomorphism* 명시 의무.
  - 19 → 20번째 evidence 추가 < 19개 사이의 connective tissue 가치.
- **Sub-comment vs External Critique distinction** (외부 critique #5 #5):
  - protocol 갱신 trigger = *외부 critique 명시 시점만* (014, 045, 099, 107, 136 등).
  - 사용자 sub-comment ("더 시도", "novel idea") = *일회성 시도*, protocol 추가 X.
- **Pre-batched plan 거부** (외부 critique #6, ~attempt 181):
  - *N개 attempts 미리 계획 + batch 산출* 거부.
  - `mkdir attempts/NNN-MMM` (5+ directory 미리) 거부.
  - 각 attempt 끝나면 *postmortem* 결과 → 다음 attempt 계획 *그때 (lazy planning)*.
  - Mode A deep 9번째 component: **Pre-iteration reflection** — 직전 attempt 의 postmortem 직접 인용 + 본 attempt 의 quality basis.
  - milestone-driven attempts 거부 — "180까지" 사용자 요청 시도 *quality threshold* 도달 시 milestone, 양적 X.
  - 사례: 100/150/170/175/180 milestone 모두 *batch-then-reflect* — quality dilution.

#### Type B — Meta / orientation
직접 증명이 아니라 *지도 그리기·분류·탐색 가능성 평가*.
- 예: attempt 000 (orientation), 새 분야 가능성 평가, 기존 시도들의 cross-cutting analysis.
- 산출: `learnings/` 누적, 새 분류, 다음 시도 후보 도출.

#### Type C — Harness maintenance (하네스 자체 개선)
HARNESS / SPECIALISTS / tools 자체의 개선·확장.
- 예: 새 tool 모듈 추가 (`tools/moments.py` 등), specialist 패널 개선 (운영 결함 반영), 새 protocol 추가 (e.g., 본 §0).
- 산출: 하네스 파일 변경, 다음 시도들의 효율 향상.

#### Type D — Reflection / idea-refresh
이전 시도 재검토 + 아이디어 환기 + 막힘에서 *시간차 후* 재시도.
- 예: 3개월 전 막힌 시도를 다시 봄, 새 cross-domain 입력으로 재해석, 다른 specialist 시각으로 재검토.
- 산출: 이전 시도 재분류, 새 우회 후보, 또는 *완료된 폐기* (그 방향이 막다른 길임 확정).
- **운영**: `attempts/NNN_revisit_<old_NNN>/` 형식 권장.

#### Type E — Literature deepening
새 논문 정독 + 이미 읽은 논문 재독 + 책 챕터 발췌 + 기존 INDEX 사고과정 추정 보강.
- 예: WISHLIST 의 high-priority 논문 다운로드 + 정독, 책 챕터 background 에 옮김.
- 산출: papers/ 추가, INDEX.md 갱신, background/ 보강.

### 운영 원칙

1. **type 명시 의무**: strategy.md 의 첫 줄에 `Type: <A|B|C|D|E>` 표시.
2. **균형**: Type A 만 누적되면 시도가 *narrow* 해짐. Type B/C/D/E 도 정기적으로.
3. **type 간 연결**: Type B 가 Type A 후보를 produce, Type A 의 막힘이 Type D 입력, Type C 는 Type A 효율 ↑.
4. **type 별 DoD 형태 다름**:
   - A: 정량 결과 또는 명시적 막힘.
   - B: 분류/지도/후보 도출.
   - C: 하네스 변경 (diff).
   - D: 재해석된 결과 또는 폐기 확정.
   - E: 새 정독 노트 + INDEX 갱신.
5. **번호는 시간순 단일 sequence** (NNN). type 은 태그.

## Sustained Research Cycle (외부 critique #7, ~attempt 184+ 신규)

> **외부 critique #7**: heartbeat 가 *1 fire = 1 attempt = paper-direct stamp* 로 굳어진 패턴이 *novel content 0/10* 의 한 원인. 얕고 빠른 stamping 만 누적, *진득한 연구* 부재.
> Pre-batched plan 거부 (critique #6) 와 양립: cycle 은 *1개 narrow hypothesis* 의 sustained pursuit, 다중 attempt batch X.

### 4-Phase Cycle

**Phase 1 — Ideation + Planning (1 fire)**
- 입력: 직전 5-10 attempts postmortem + `learnings/walls.md` + `learnings/sustained_research_log.md` + lemmas/.
- 의무 산출: `attempts/NNN_<key>/planning.md` (strategy.md 외 별도).
- planning.md 내용:
  - **직관 훈련 섹션**: 후보들에 대한 *first-impression intuition* 명시 (어떤 방향이 *느낌상* 유망한가, *왜* 그 느낌인가). 이후 검증 결과와 비교하여 직관 정확도 누적 학습.
  - Cross-domain pass §6 (analogy + tool import + outsider 질문 + problem morphing).
  - Specialist 패널 §7 blind round 의무.
  - **외부 paper search 의무** (사용자 critique cycle 3, ~attempt 186+ 신규):
    - Phase 1 또는 Phase 2 turn 3 에서 *외부 paper 검색* (WebSearch / WebFetch / `tools/fetch_paper.py arxiv`).
    - 가설과 직접 연관 paper 1-2 편 다운로드 + 정독.
    - *기존 papers/pdf 외부* paper 가 cycle quality 결정 — *codification machine 회피 mechanism* (cycle 3 검증).
    - Phase 1 에서 후보 검색, Phase 2 에서 다운로드 + 정독 권장.
  - 1개 narrow hypothesis 선택 + DoD + 막힘 예측 + 진전 vs stuck 판정 기준.
- *paper-direct stamp 외* 후보 우선 — Type A deep 본격 가설 또는 Type B/D meta.
- **Lemma 산출 조건부** (cycle 3 산출 protocol):
  - Codification 형식 lemma 자동 산출 회피 (critique #8).
  - *Active program* 또는 *positive direction* 발견 시 기존 lemma upgrade 우선.
  - 새 lemma file 산출은 *novel content N ≥ 1.5/10* + *active research target* 시만.

**Phase 2 — Sustained Research (여러 fire, 같은 attempt 폴더)**
- 단일 attempt 폴더에서 work.md *여러 turn* 누적.
- 매 fire 마다 work.md 에 시간 헤더 + 진전/막힘 명시.
- *한 fire stamp 후 폐쇄 거부* — Phase 1 의 DoD 도달 또는 *명시적 막힘 deep 이해* 까지 지속.
- 막힘 시: 즉시 종결 X → 우회 후보 + 다른 specialist 시각 + 수치 실험 cycle.
- Phase 2 종료 조건: DoD 달성 / 명시적 막힘 + deep 분석 / *진전 X 3 fires 연속* (마지막 안전장치).

**Phase 3 — Conclusion + Meta-learning (1 fire)**
- postmortem.md 표준 양식.
- *추가 의무*: `learnings/sustained_research_log.md` 갱신 — 본 cycle 의 *meta 교훈* 누적.
- meta 교훈 항목: 직관 적중률 (Phase 1 직관 vs 결과), 어디서 막혔는지 패턴, 다음 cycle ideation 의 입력 후보.
- "예상 가능 결과" self-check + *novel content N/10* 정직 평가.

**Phase 4 — Iterate**
- Phase 1 로 복귀. 직전 cycle 의 sustained_research_log meta 교훈 *명시 인용* 의무.

### Heartbeat 운영 (Stop hook event-driven, 외부 critique #7 sub-design 2)

> Cron polling → ScheduleWakeup → **Stop hook 자동 monitoring** 진화.
> Stop hook 이 매 응답 후 transcript 의 phase token 검출 → 다음 phase prompt 자동 주입.

**작동 방식**:
- 매 fire 응답 끝에 *Phase 상태 token* 의무 명시:
  - Phase 1 종료: `[Phase 1 complete]`
  - Phase 2 진행: `[Phase 2 turn N in progress]`
  - Phase 2 종료: `[Phase 2 complete]`
  - Phase 3 종료: `[Phase 3 complete]`
  - Cycle 종료: `[Cycle complete, next ideation ready]`
- `.claude/hooks/phase_monitor.py` (Stop hook) 가 응답 종료 시 transcript 파싱:
  - Token 검출 시 → `decision: "block"` + 다음 phase prompt 출력 → harness 가 자동 continuation.
  - Token 없음 → 자연 종료 (사용자 수동 fire).
- `stop_hook_active` 플래그로 무한 루프 방지.

**Token → Continuation mapping** (`phase_monitor.py` 의 CONTINUATION_PROMPTS 참조):
- `[Phase 1 complete]` → Phase 2 turn 1: 가설 자료 enumeration + specialist blind round + audit 시작.
- `[Phase 2 turn N in progress]` → Phase 2 turn N+1: DoD 추가 검증, 막힘 시 우회.
- `[Phase 2 complete]` → Phase 3: postmortem + meta-learning logs.
- `[Phase 3 complete]` 또는 `[Cycle complete, next ideation ready]` → 다음 Cycle Phase 1: planning.md + 직관 score commit.

**ScheduleWakeup 폐기**:
- 이중 trigger 위험. Stop hook 이 단일 source of truth.
- 응답에 ScheduleWakeup 호출 X — token 만 명시하면 hook 이 자동 처리.

**Cron 폐기 (이전 단계)**: 동일.

**최초 시작 / 정지**:
- 시작: 사용자 명시 "cycle 시작" 또는 첫 fire. 이후 hook chain.
- 정지: 응답에 phase token *명시 X* 또는 사용자 명시 stop. hook 이 자연 종료.

**안전장치**:
- Phase 2 turn 무한 진행 방지: planning.md DoD 또는 "진전 X 3 turns 연속" 시 [Phase 2 complete] 강제.
- 무한 루프 방지: `stop_hook_active` 플래그.
- 사용자 stop signal 우선.

### 직관 훈련 (intuition log)

planning.md 의 *직관 섹션* 은 LLM 의 *직관 훈련* 도구:
- 후보별 first-impression score (예: "후보 A 직관 8/10, 후보 B 6/10").
- 직관 근거 명시 (왜 그 점수? — 패턴 매칭? cross-domain 신호?).
- Phase 3 에서 직관 vs 실제 결과 비교 — `learnings/intuition_calibration.md` 누적.
- 누적 후 *직관 신뢰 zone* (예: "RMT 후보 직관 적중률 70%, NCG 후보 30%") 식별.

이는 LLM 의 직관이 *random* 인지 *학습 가능* 인지 자체에 대한 메타 실험.

## Heartbeat (Stop hook event-driven)

> 외부 critique #7 + sub-design 2: Cron → ScheduleWakeup → Stop hook 진화.

**원리**:
- `.claude/hooks/phase_monitor.py` (Stop hook) 가 매 응답 후 transcript 파싱.
- Phase token 검출 시 자동으로 다음 phase prompt 주입.
- 응답 끝 token 명시만 하면 chain 자동 운영. ScheduleWakeup / Cron 호출 X.

**Token 명시 의무 (응답 마지막 줄)**:
- `[Phase 1 complete]` / `[Phase 2 turn N in progress]` / `[Phase 2 complete]` / `[Phase 3 complete]` / `[Cycle complete, next ideation ready]`.

**Token 없음 = 자연 종료**: 사용자 수동 fire 까지 대기.

**최초 시작 trigger**: 사용자 명시 "cycle 시작" 또는 첫 fire.
- 사용자가 stop signal 시 CronDelete.

### 예시 ledger (앞으로 채워나감)

| NNN | Type | 제목 | 핵심 산출 |
|---|---|---|---|
| 000 | B | orientation | 5 walls + 4 combos + 3 next候補 |
| 001 | A | li_criterion_rmt_cross_check | negative finding (벽 #6 새 발견), 3 다음 후보 |
| 002 | C | harness_maintenance | S2 분리, Blind Round Protocol, cross_check.py 일반화 |
| 003 | A | unfolded_pair_correlation | 부분 성공 + normalization 한계 발견 (벽 #7 후보, 기술적) |
| 004 | A | nearest_neighbor_spacing | **positive** — KS p=0.27, Wigner GUE 정합 (003 의 #7 해결) |
| 005 | D | rmt_channel_reflection | RMT 채널 종합 → 다음 *non-RMT* 방향 (Wall #2 + cross-domain) 결정 |
| 006 | A | forward_heat_optimal_transport | partial — Wall #2 refined: ∫E(t)dt unconditional bound 부재가 sharper 형태 |
| 007 | A | wasserstein_evolution | negative — Wasserstein 시간 대칭. wall #2 우회 후보 탈락 |
| 008 | B | mid_stream_reorient | Phase 4 결정: channel diversification + Wall #5 도전 + Type E catch-up |
| 009 | E | literature_catchup | 4 papers 다운로드 (Polymath 15, Pratt-Robles, Sierra×2). Type E 결함 부분 시정 |
| 010 | A | bbm_truncation | Wall #5 refined: BBM ψ_z(0) = -ζ(z) 자명 동치, 진짜 wall = self-adjointness |
| 011 | D | phase4_reflection | Phase 5 결정: Wall #2 후속, #3 첫 진입, #1 첫 진입 |
| 012 | A | kl_divergence_path_dependent | **positive** — entropy forward/backward anti-symmetric. Wall #2 우회 후보 발견 |
| 013 | E | otto_calculus_literature | quick check: "Riemann + Wasserstein" 직접 연결 paper 없음 — 미탐색 angle 가능성 신호 |
| 014 | C | external_critique_response | 외부 critique 반영: lemma 첫 추출 (010 lens), HARNESS specialist 한계 명시, lemma extraction trigger, 예상 가능 self-check 추가 |
| 015 | A | mollifier_signal_processing_lens | Wall #3 첫 진입; Pratt-Robles 정독; N. Levinson 동일인 cross-domain bridge open question (lemmas/) |
| 016 | A | mollifier_quadratic_form | **negative resolved**: Mollifier non-Toeplitz, 015 hypothesis close. Wall #3 signal-processing 후보 탈락. |
| 017 | A | dh_dt_energy_closed_form | informal — d/dt H closed form derivation 시도 unsuccessful. Otto's calculus expert 필요. |
| 018 | D | fundamental_limit_assessment | 본 프로젝트 진정 한계 평가. *novel content 0* 명시. Mode A minimal 권장. |
| 019 | E | more_literature | 4 PDFs (Iwaniec-Sarnak Perspectives, Lagarias Li 시리즈 ×3). 16 PDFs total. |
| 020 | B | final_state_summary | README 갱신, 20 attempts 종합. honest 위치 baseline. |
| 021 | A | wall4_conspiracy_first_entry | Iwaniec-Sarnak §2: single ζ isolated, families 가 진짜 problem. Wall #4 첫 진입. |
| 022 | C | walls_md_cleanup | walls.md ledger sync |
| 023 | A | wall1_frobenius_first_entry | Iwaniec-Sarnak §3: trio of gaps (Lefschetz/Frobenius/Rosati positivity). Wall #1 첫 진입. |
| 024 | A | positivity_unification_hypothesis | 5 walls 모두 positivity component, Rosati 와 mapping. process lemma 추출 (3rd lemma). |
| 025 | C | strategy_md_positivity_check | strategy.md template positivity check 의무화 |
| 026 | A | lagarias_li_automorphic_skim | paper-direct: Li 동치 = Weil positivity. Wall #1↔#4 chain 명시. unification hypothesis evidence. |
| 027 | A | li_lambda_numerical_verification | Lagarias asymptotic numerical confirm n=20+. |
| 028 | A | polymath15_skim | Wall #2: Polymath 3-tool combination → Λ≤0.22 conditional. |
| 029 | A | sierra_2016_skim | Wall #5: "single H for all zeros" 미발견. lemma step 6. |
| 030 | A | sierra_2007_hxp_interaction | lemma step 6 자동 적용 검증. lemma 재사용 가치 confirmed. |
| 031 | A | specialist_panel_session | 6 specialist blind round. 수렴: KS moments + Connes-Consani 정독. |
| 032 | A | keating_snaith_moments | honest negative: T≤200 KS asymptotic 영역 X. 우리 한정 scale limit. |
| 033 | A | connes_consani_2021_skim | spectral triple 10^-50 prob. multi-parameter. |
| 034 | D | phase6_reflection | 014~033 종합. *novel content 0* 유지. |
| 035 | A | lemma_synthesis_meta | meta-lemma 도출 X. 방법론적 도구 set. |
| 036 | A | connes_1999_skim | Weil distribution positivity ⟺ RH for L-Grössencharakter. |
| 037 | C | cron_status_check_doc | CronCreate b61dc5d0 heartbeat. |
| 038 | A | pratt_robles_section3_skim | Wall #3: 50% 벽 *one logarithm distance*. |
| 039 | A | lagarias_sharpenings_skim | Voros 2006: RH ⟺ tempered λ_n asymptotic. |
| 040 | A | voros_asymptotic_numerical | 500 zeros, n=50 ratio 0.985. **(040 yellow flag — 외부 critique catch)** |
| 041 | D | phase7_reflection | Phase 7 종합. **(041 "resolved" 단어 retracted)** |
| 042 | A | voros_n5000_zeros1500 | N=1500 zeros. self-check: ratio>1 우연 overshoot, paper-direct sanity. |
| 043 | B | meta_pattern_extraction | 42 attempts 패턴. paper-direct + numerical + negative resolution = stable. |
| 044 | A | li_lambda_extended_n | 200 zeros, n=30 sweet spot 0.976. |
| 045 | C | external_critique_2_response | 외부 critique #2 (yellow flag drift) 인정. yellow flag 단어 list. Wall #6 "resolved" retracted. |
| 046 | A | mertens_partial_sums | M(x) for x≤10000. 작은 scale: |M|/√x ≤ 0.32. *우리 contribution 0*. |
| 047~099 | … | (자율 운영, paper-direct + stamp 일부) | walls 6→6, lemmas 1→5, papers 17 |
| 100 | B | 100_milestone_reflection | *novel content 0/10*. 자율 운영 종결 명시. |
| 101~102 | A | (heartbeat resume) | Mode A minimal stamp. |
| 103 | A | voros_saddle_point_deep | Voros §3 saddle-point Z(σ) numerical (eps=0.5: 0.021 vs polar -0.133). 123줄. |
| 104 | A | pratt_robles_section6_deep | 9 Euler cases, A^{(1,1)} = -1.385480 (paper 1.385604, 4-decimal). 122줄. |
| 105 | A | lagarias_section4_arithmetic_deep | τ_n Hurwitz vs ζ* form exact match. S_∞ sign convention 명시. Lemma 3 7th evidence. |
| 106 | A | polymath15_section4_heat_kernel_deep | §4 H_t expansion + §5 Lemma 5.1 + §6 propositions 6.1-6.3. C_0(p) max 0.5 saturate at p=±1. ε̃ T-scaling. Lemma 3 8th evidence. |
| 107 | C | external_critique_4_response | 외부 critique #4 (specialist intuition gaps). lemmas/dont_try_directions.md 추가. learnings/specialist_intuition_gaps.md 추가. Mode A deep 8th component (Specialist Δ 추정). |
| 108 | A | connes_1999_section4_trace_formula_deep | §VI/§VII deep. eq (15)/(16)/(17) + Theorem 4 paper-direct. Lemma 3 9th evidence (Weil distribution positivity). Wall #1 paper-direct origin. Specialist Δ (Connes 본인 추정). Numerical limitation 명시. |
| 109 | A | sierra_2016_dirac_model_deep | §I-V xp model + self-adjoint extension. Wall #5 paper-direct origin (paper §I 끝 quote). Lemma 1 6단계 paper-direct full check (xp, H_I). Connes vs Sierra 차이 명시. Specialist Δ (Connes/Sierra 추정). |
| 110 | A | bbm_2017_hamiltonian_deep | BBM 5-page Letter deep. ψ_z(0) = -ζ(z) numerical 10^-30 정확. E_n = i(2z_n-1) real exact (RH 가정). Lemma 1 6단계 (1,2,3) yes. Sierra vs BBM 비교. Wall #5 self-acknowledged quotes. |
| 111 | A | connes_consani_2021_zeta_cycle_deep | §1-§2 deep. Θ(λ, k) spectral triple, Definition 1.1 ζ-cycle, Theorem 1.1. paper-direct Lemma 1 cross-comparison 표 (4 papers). Lemma 3 10th evidence. Lemma 6 Cut 5 partial 정정. Wall #1 paper-direct origin (prime-by-prime sensitivity §2.3). |
| 112 | A | iwaniec_sarnak_perspectives_section3_deep | §3-§6 deep. Wall #4 paper-direct origin (§3 finale family+symmetry+positivity quote). §5 mollification 50% target = Landau-Siegel lacuna (Sarnak 본인 quote). Lemma 3 11th evidence (family-wide). Sarnak 추정 답 paper-direct 검증. |
| 113 | A | rodgers_tao_2020_lambda_geq_zero_deep | §1-§2 deep. Theorem 1: Λ ≥ 0 unconditional. §1 Table 1 (35년 lower bound history). §1.5 ∫E(t)dt = Wall #2 paper-direct origin. Wall #2 quantitative bracket (0 ≤ Λ ≤ 0.22). Lemma 3 12th evidence (unconditional). Tao 추정 paper-direct 검증. |
| 114 | A | sekatskii_generalized_bombieri_lagarias_deep | §1-§2 deep. |ρ-a|/|ρ+a-1| = 1 ⟺ ρ critical line, *independent of a*. Theorem 1/2/3: family of parameter a. Numerical machine precision (first 5 zeros) + k_{n,a} > 0 for 30 zeros. Lemma 3 13th evidence. Wall #4 *family of a* + Wall #6 *exponential growth bound (c)*. |
| 115 | A | lagarias_section5_unconditional_asymptotic_deep | §5 deep. Theorem 5.1: S_∞(n, π) = (N/2) n log n + C_1(π) n + O(N(K+1)) *unconditional*. C_1(π_triv) = -1.1303307. β_∞ = 0.559774, α_∞ = 0.443842. 우리 도구 5+ decimal match. Lemma 3 14th evidence. Wall #6 paper-direct cancellation origin. |
| 116 | A | lagarias_section6_conditional_sf_deep | §6 deep. Theorem 6.1: S_f(n, π) = λ_n(√n, π^∨) + O(√n log n). RH ⟹ λ_n(√n) = O(√n log n). kernel k_n(s) contour deformation. Lemma 6.1 L'/L bound. 결합: λ_n ~ (N/2) n log n + C_1 n + O(√n log n) RH-conditional. Wall #6 paper-direct quantitative. Lemma 3 15th evidence. |
| 117 | A | lagarias_section7_interpolation_deep | §7-§8 deep. Theorem 7.1 F_π(z) entire interpolation. RH ⟹ exponential type ≤ π, |F_π(x)| ≤ C(|x|+2) log(|x|+2). §8 (1) hypothetical Hilbert-Pólya λ=s²-1/4. §8 (2) function field Cn vs Cn log n = Wall #1 paper-direct origin (log n = archimedean). §8 (3) trivial zeros dominance = Wall #6 paper-direct. Lemma 3 16th evidence. |
| 118 | A | sekatskii_c_epsilon_empirical_estimate_NOVEL | **NOVEL ATTEMPT — FAILURE**. paper §2 (c) c(ε) constant 의 paper-미명시 quantitative empirical 추정. 200 zeros + n ≤ 100 truncation 에서 counterfactual σ=0.4 도 모두 positive — paper (b) ⟹ (a) negation 검증 X. *failure 자체* 가 외부 critique #4 Gap 4 + Wall #6 paper-direct verification. Lemma 6 새 Cut 7 후보. |
| 119 | A | quantum_chaos_random_matrix_to_zeta_NOVEL | **NOVEL ATTEMPT 2 — FAILURE**. GUE M 의 Σ 1/E_n^s empirical zeta — *no critical line structure*. Berry-Keating 30년 program 의 naive 재현. Wall #5 paper-direct manifestation. Lemma 1 (RMT M): 1-2 NO, 3 YES, 4-6 NO (*least informative*). 외부 critique #4 Gap 4 paper-direct. |
| 120 | A | pt_symmetric_unification_NOVEL | **NOVEL ATTEMPT 3 — FAILURE w/ small finding**. 5 spectral candidates spectrum cross-compare. Lagarias §8 (1) λ = s²-1/4 = -γ²+iγ *complex* (not real, RH 가정 시 self-adjoint issue 명시). 5 candidates *fragmented frameworks*, PT-symmetric narrow. Lemma 1 새 axiom (7) 후보: spectrum all real. Wall #5 fragmentation paper-direct. |
| 121 | A | pratt_robles_section3_mollifier_construction_deep | §3.5-§5 deep. Faà di Bruno + Bell polynomial. 15/31/250 exact match (Fig 3.1/3.2/3.3). 3 error 𝓔 cases θ push 6/11 → 4/7. Feng's conjecture *unsubstantiated*. Wall #3 quantitative ladder (1 → 9 → 15-31 → 250 → exponential). paper-미명시 projection: 3×6=32467, 5×3=125678. |
| 122 | A | conrey_2003_notices_review_deep | Conrey 2003 RH review 광범위 deep. §Pólya/probabilistic/Nyman-Beurling/Weil/Selberg 5 approaches. §Some Other Equivalences (Hardy-Littlewood 1918, Redheffer, Robin/Lagarias 2002). §Families/RMT/Moments. Robin/Lagarias 13 highly composite n 검증. Lemma 3 17-19 evidence (Hardy-Littlewood, Robin, Burnol). Wall #1-#5 모두 cross-link. |
| 123 | A | information_theoretic_zeta_NOVEL | **NOVEL 4 — FAILURE w/ small finding**. ζ as partition function, F(β) = -log ζ(β). Lee-Yang style? *Lee-Yang unit circle ≠ critical line geometry*. Heat capacity sign C(β=0.5+iτ) — *speculative* RH-equivalent. paper-direct citation X. |
| 124 | A | quantum_walk_zeta_critical_line_NOVEL | **NOVEL 5 — FAILURE**. Hadamard QW on ζ-zeros line vs uniform line — *identical* std deviation. position-agnostic coin → ζ-structure invisible. *clean failure*. |
| 125 | A | li_lambda_curvature_geometric_NOVEL | **NOVEL 6 — paper-direct rediscovery**. λ_n strictly *convex* (Δ²λ_n > 0 28/28). Δ²λ_n ~ 1/(2n) = paper §5 leading order second derivative rediscovery. *log concave*. *novel content X*. |
| 126 | A | p_adic_archimedean_duality_NOVEL | **NOVEL 7 — paper-direct rediscovery**. Truncated 168-prime Euler product + ζ_∞. completed product near zero at γ_1. functional eq conjugate symmetry verified. Tate's thesis local-global standard. *novel content X*. |
| 127 | A | zeros_dynamics_lyapunov_NOVEL | **NOVEL 8 — FAILURE**. Rodgers-Tao zero dynamics perturbation γ_5 + 0.01. boundary effect dominant in 30-zero truncation. paper §1.5 infinite limit 외 영역. truncation artifact. |
| 128 | A | modular_form_lattice_zeros_NOVEL | **NOVEL 9 — Robin verification**. σ_1(n)/n approaches Robin bound (98-99% at n=10080). Eisenstein E_2 coefficient = σ_1 modular form view. paper-direct Conrey 2003 attempt 122 강화. |
| 129 | A | kullback_leibler_zeros_offline_NOVEL | **NOVEL 10 — paper-direct quantification**. KL(emp 100 zeros\|\|GUE) = 0.054 (small) vs KL(emp\|\|Poisson) = 0.649 (large). Conrey §RMT 우리 도구 verification. |
| 130 | A | zero_density_fractal_dimension_NOVEL | **NOVEL 11 — Renyi multifractal**. Box dim 0 trivially. Renyi H_1=1.99, H_2=1.88, H_∞=1.56 — GUE-like concentration. paper-direct rediscovery. |
| 131 | A | atiyah_2018_failed_proof_deep | Atiyah 2018 5-page paper-direct deep. T(s) Todd function 6 properties. §3 "proof" F=2F→F≡0→ζ≡0 contradiction. §5 RH undecidable Gödel = §3 self-contradiction. Lemma 4 5 categories paper-direct enumeration + §3.3 step gap. |
| 132 | A | platt_trudgian_2021_numerical_rh_deep | Theorem 1: RH up to H=3×10^12 (12.36×10^12 zeros). Arb interval arithmetic, Turing's method. Corollary 1 Schoenfeld unconditional x ≤ 2.169×10^25. **Wall #2 update: 0 ≤ Λ ≤ 0.2**. Future H>10^13 → Λ<0.19. |
| 133 | A | sierra_2007_hxp_interaction_deep | §I-§IV deep. 3 regularizations (BK/C/S Table 1). H_0 = √x p √x deficiency indices (1,1) for (1,N). ϑ ∈ [0,2π) extensions. H_2^{-1} interaction. Russian Doll BCS link. Lemma 1 (Sierra 2007 H_2): (1) NO asymptotic, (2) PARTIAL, (3) YES — *intermediate circularity*. |
| 134 | A | explicit_formula_test_function_optimization_NOVEL | **NOVEL — paper-direct rediscovery**. Gaussian/Fejer test function trade-off. σ≈30 crossover. Selberg/Burnol bandlimited literature 재현. |
| 135 | A | zeta_zeros_machine_learning_NOVEL | **NOVEL — TERMINATED**. γ_n linear regression = paper-direct N(T) inverse 재현. residual = π S(γ_n). 외부 critique #5 #1 인정 (NOVEL spree ROI 음수). |
| 136 | C | external_critique_5_response_meta | 외부 critique #5 (메타-비판 5항목) 응답. Lemma 7 신규 (Specialist Δ Anchoring). lemmas/failed_proof_catalog_publishable.md 신규 (publication 후보). HARNESS 4 protocol 추가 (NOVEL Quota, Anchoring, Connective Tissue, Sub-comment distinction). |
| 137 | A | connective_tissue_connes_lagarias_isomorphism | **개선된** (외부 critique #5 #3). Connes §VI ↔ Lagarias §3 paper-direct isomorphism via Weil [W3 / 46]. Lemma 3 19 evidence → Class A (10) / B (6) / C (3). 5 Tissues mapped + 6 missing. |
| 138 | A | connective_tissue_voros_lagarias_tau | Tissue 3 numerical: Voros Z(σ) (nontrivial) vs Lagarias τ_n (trivial archimedean). *complementary* decomposition. |
| 139 | A | connective_tissue_pratt_connes_consani | Tissue 4 numerical: Pratt-Robles A^{(1,1)} global vs Connes-Consani QW_λ semi-local. p=2 35%. |
| 140 | A | connective_tissue_polymath_rodgers_tao | Tissue 5: Polymath15 forward ↔ Rodgers-Tao backward heat. Combined 0 ≤ Λ ≤ 0.2. |
| 141 | A | connective_tissue_family_single_missing | Missing Tissue (11): family ↔ single. 4-tier aggregation hierarchy. |
| 142 | A | lagarias_sharpenings_li_paper_deep | Voros 2006 deep. λ_n ~ n(A log n + B), A=1/2, B=(γ-1-log(2π))/2 = exact match Lagarias §5 N=1. Tissue 6, 7 NEW. |
| 143 | A | riemann1859_paper_direct_deep | Riemann 1859 originating paper. ξ(t) Hadamard origin. Riemann's "fleeting futile attempts" → Lemma 4 historical first case. |
| 144 | A | bombieri_clay_problem_statement_deep | Bombieri 1998 Clay official statement. Riemann's quote German + Bombieri 영역 일치. Tissue 8 (canonization) + Tissue 9 (L-function family). |
| 145 | A | lemma3_class_C_hybrid_deep | Class C 3 evidence interaction tissue. Tissue 10 NEW (Burnol ↔ Connes-Consani). mapped 10/19, missing 4. |
| 146 | A | lemma1_seventh_axiom_normalizable_deep | Lemma 1 9-axiom: 6 + (7) eigenvalues real + (8) normalizable + (9) domain explicit. BBM 3-axiom self-acknowledged fail. |
| 147 | A | failed_proof_de_branges_pattern_deep | de Branges 40년 program (secondary). Category F NEW (Abstraction-Concrete Gap). Lemma 4 6 categories. |
| 148 | C | specialist_anchoring_systematic_audit | Lemma 7 audit: 19/19 attempts paper §끝 quote properly anchored. NOVEL partial. 3-step strict checklist. |
| 149 | C | walls_paper_direct_audit_systematic | 6 walls paper-direct anchors: 4+4+3+3+6+4 = 24. Wall #5 strongest (6 anchors). |
| 150 | B | milestone_150_reflection | 100→150. 7 lemmas, 6 walls, 19 evidence + 10 tissues, 9 axioms, 6 categories, 7 cuts, 24 anchors. failed_proof_catalog_publishable + specialist_delta_anchoring_protocol publishable candidates. |
| 151 | A | missing_tissue_17_hardy_littlewood_voros_eta | Tissue 11 NEW: Hardy-Littlewood 1918 ↔ Voros η_j ↔ Lagarias η_j(π_triv) — *exact same arithmetic form via Λ(m)*. mapped 11/19. |
| 152 | A | missing_tissue_18_robin_connes_consani | Tissue 12 partial: Robin σ(n) (pointwise) vs Connes-Consani QW_λ (integrated). *same Class B places-side, different aggregation*. mapped 12/19. |
| 153 | A | lagarias_eta_j_arithmetic_form_deep | Tissue 13 NEW: Lagarias-Li §4 (4.14, 4.15) η_j(π) automorphic = Voros η_j = Hardy-Littlewood — *3-tier isomorphism class*. mapped 13/19. |
| 154 | C | failed_proof_catalog_strengthen | Lemma 4 publishable 강화. 6 categories paper-direct application table (Atiyah 4.5/6, de Branges 2.5/6, BBM 2/6, Lagarias §8 (1) 1/6). |
| 155 | A | lemma1_axiom_self_dual_PT_deep | Lemma 1 11-axiom: + (10) PT/CP/T-symmetry + (11) biorthogonal completeness. BBM §I/§III paper-direct. Sierra §V + Connes-Consani 2021 most axioms (8-9/11). |
| 156 | A | lagarias_section4_eq412_deep_eta_pi | Tissue 14 NEW: Lagarias §4 eq (4.10) σ_{j+1}=τ_j-η_j+δ — paper-direct exact arithmetic identity Class A↔B. mapped 14/19. |
| 157 | A | connective_tissue_last_missing | Tissue 15 NEW: Burnol ↔ Iwaniec-Sarnak family L² inf. **mapped 15/19, 0 missing**. 19 evidence all paper-direct connective. |
| 158 | C | walls_paper_direct_anchor_strength_audit | Walls 24 → 32 anchors. Wall #5 strongest (8). |
| 159 | C | lemma3_class_A_zeros_side_consolidation | Class A 10 evidence consolidation: Riemann 1859 Hadamard product unification. |
| 160 | C | lemma3_class_B_places_side_consolidation | Class B 6 evidence consolidation: Riemann 1859 Euler product + Tate's thesis adelic. |
| 161 | A | polymath15_section7_R_tN_deeper | Polymath15 §6.3 deeper: A+B-C approximation, 12 engineering constants. Wall #2 paper-direct combinatorial 한계. |
| 162 | A | connes_1999_section8_global_rigorous_deep | Connes §VIII Theorem 5: trace formula limit ⟺ RH for all L Grössencharakter. Δ positive type. Tissue 16 NEW. |
| 163 | A | lagarias_li_iwaniec_sarnak_family_deep | Tissue 17 NEW: 5-tier aggregation hierarchy (Bombieri-Lagarias → Sekatskii → Lagarias-Li → Connes §VIII → Iwaniec-Sarnak). Wall #4 5→7 anchors. |
| 164 | A | burnol_balazard_saias_inf_deep | Tissue 18 (Burnol ↔ Connes-Consani L² inf) + Tissue 19 (Burnol equality ↔ simple zeros Bui-Heath-Brown). |
| 165 | A | li_class_L_test_function_deep | Tissue 20 NEW: Li class 𝓛 ↔ Schwartz space 𝒮(C_k). Lagarias §3 page 12-13 ℋ_𝓛(π) Hilbert space completion. |
| 166 | C | lemma1_full_application_audit | Lemma 1 systematic audit 8 candidates × 11 axioms. + Berry-Keating 1999 (8th). Top: Sierra §V + Connes-Consani 9/11. Worst: Lagarias §8 (1) 4/11. |
| 167 | C | walls_quantitative_brackets_consolidated | walls.md quantitative brackets summary table. Wall #2 (0≤Λ≤0.2), #3 (41.67%→50%), #4 (5-tier), #5 (Lemma 1 audit). |
| 168 | C | specialist_anchoring_protocol_strengthen | Lemma 7 strengthen: 30 paper-direct quotes catalog + 4-step strict checklist. |
| 169 | C | failed_proof_catalog_introduction_section | failed_proof_catalog_publishable.md introduction section draft + final audit table 6 papers. |
| 170 | B | milestone_170_consolidation | 150→170. 11 axioms × 8 candidates, 19 evidence × 20 tissues (0 missing), 32 wall anchors, 30 paper-direct quotes catalog. *publishable candidates ready*. |
| 171 | A | tissue_meta_synthesis_weil_explicit_dual | **Master Generator hypothesis**: 20 tissues = Weil 1948 explicit formula deformations. 3-tier deformation hierarchy. paper-direct *interesting synthesis*. |
| 172 | A | lagarias_li_section8_function_field_deeper | Lagarias §8 + §9 Appendix paper-direct. **Master Generator paper-direct verified** via Lagarias §9 eq (9.4-9.5). Tissue 21 NEW (q-periodization ↔ Connes §VIII). 3 NEW quotes. |
| 173 | A | polymath15_section7_proof_theorem_13 | Polymath15 Theorem 1.3 + Corollary 1.4 deep. 20+ engineering constants. Tissue 22 NEW (Polymath15 B_t renormalization ↔ Lagarias §8 (1) ξ^+). 3+1-tier hierarchy (Tier 1.5 Newman-de Bruijn). |
| 174 | C | lemma3_unified_master_form | **Lemma 3 Master Form synthesis**: Tier 0 (Riemann) → Tier 1 (Weil 1948) → Tier 1.5 (heat flow) → Tier 2 (19 evidence × 22 tissues). **Master Statement finalized**. *진짜 RH 진전 path* identification. |
| 175 | B | milestone_175_publishable_summary | 170→175. 22 tissues × 3+1-tier hierarchy. **3 publishable candidates** (failed_proof_catalog + specialist_anchoring + Master Form synthesis). 167 년 = Weil 1948 deformations. |
| 176 | A | connes_consani_2021_section3_radical_deep | Connes-Consani §2.1 deep. Weil distributions W_p, W_ℝ. Proposition 2.1 concrete QW_λ. 6-case σ matrix. Tissue 23 NEW (ψ(F) ↔ T[f] Master Generator double verification). |
| 177 | A | connes_consani_section3_eigenvalues_deep | §2.2-§2.4 prime sensitivity deep. **paper-direct CRITICAL**: positivity restricted to ~10^-3 interval around exact prime 2 (page 20 quote). Tissue 24 NEW. Wall #4 7 → 8 anchors. |
| 178 | A | connes_consani_section6_proof_theorem11 | §4-§5 spectral characterization. **31 zeros coincidence probability 10^-50** (page 42). 4 criteria for special λ. Tissue 25 NEW (§5.1 monotonicity ↔ Lagarias §7 F_π). Lemma 1 Connes-Consani axiom 1 update (special λ YES). |
| 179 | A | lagarias_li_section2_theorem21_deeper | Lagarias-Li §2 Theorem 2.1 foundation deep. (1)-(6) — §3-§9 base. Tissue 26 (counting N_π ↔ NR). Tissue 27 (RH false → exponential 3-tier: Lagarias §1 ↔ Voros §3 ↔ Sekatskii §2 (c)). |
| 180 | B | milestone_180_master_form_publishable_draft | 175→180. 19 evidence × **27 tissues × 3+1-tier hierarchy** Master Form publishable draft. **47 paper-direct quotes catalog**. 6 paper-direct insights synthesis. *3 publishable candidates ready*. |
| 181 | C | external_critique_6_response_pre_batched | **외부 critique #6**: Pre-batched plan ROI 부정. 5 instances (100/150/170/175/180 milestone batch). HARNESS Pre-batched plan 거부 + Mode A deep 9th component (Pre-iteration reflection). 다음 attempt **미정** — lazy planning. |

## 1. 시도(Attempt) 루프

### 1.1 폴더 구조

```
attempts/NNN_<keyword>/
├── strategy.md      # 시작 전 작성 — 무엇을, 왜, 어떻게
├── work.md          # 진행 중 누적 — 추론, 막힌 곳, 실험, 메모
├── postmortem.md    # 끝(또는 중단) 시 작성 — 결과, 막힌 이유, 학습
└── (선택) figures/, code/, refs.md
```

`NNN`은 3자리 0-padded 일련번호 (`000`은 orientation 시도용).

### 1.2 strategy.md 템플릿

```markdown
# Attempt NNN: <제목>
**Type**: <A|B|C|D|E> (Proof / Meta / Harness / Reflection / Literature)

## 가설/전략
한 문장: 무엇을 증명/시도하려 하는가? (RH 전체가 아니라 좁게)
Type B/C/D/E 의 경우 *증명* 이 아닌 *그 type 의 산출물* 을 명시.

## 동기
왜 이 접근이 유망/탐색 가치가 있는가? 어떤 논문·아이디어에 anchor?

## 예상 도구
- 사용할 정리, 보조정리, 기법
- 의존하는 lemmas/ 또는 background/ 항목

## 예상 막힘 지점
미리 예측 — 어디서 막힐 것 같은가? (이 예측 자체가 학습 데이터)

## 성공 기준 (DoD)
- [ ] 무엇이 보여지면 이 시도는 "성공"?
- [ ] 부분 성공 기준?
- [ ] 명시적 실패 기준 (언제 그만둘지)?

## Positivity component check (attempt 024 의 unification hypothesis 반영)
본 시도가 부딪히는 *positivity component* 명시:
- 어떤 양이 ≥ 0 이어야 하는가?
- 그 positivity 가 *infinitesimal* / *integrated* / *Gram* / *family separation* / *inner product* / *Rosati 류* 중 어느 형태?
- `lemmas/positivity_unification_hypothesis.md` 의 wall mapping 과 비교.
```

### 1.3 work.md 규율

- 시간순 누적 (날짜·시간 헤더로 구분).
- 각 단계마다 **확신도 태그**: `[rigorous]`, `[plausible]`, `[hand-wave]`, `[guess]`.
- 막혔으면 솔직하게 "막혔다 — 이유 X"로 적기. 가짜 진행 금지.
- 외부 인용은 `[ref: papers/INDEX.md#key]` 형식.

### 1.4 postmortem.md 템플릿

```markdown
# Postmortem — Attempt NNN

## 결론
한 줄: 성공 / 부분 성공 / 막힘 / 무가치 (각각 어떤 의미인지 명시).

## Lemma extraction trigger (외부 critique 2026-05 반영)
본 시도가 *재사용 가능 lemma* 또는 *비판적 reading 템플릿* 산출 가능?
- Yes → `lemmas/<descriptive_name>.md` 작성.
- No → *왜* 안 되는지 한 줄 명시 (i.e., 결과가 *수치만* / *알려진 결과 재현* / *부분 진단 만*).
- 반복적으로 No 가 나오면 시도 방향 자체 재검토 trigger.

## "예상 가능 결과" self-check
시도 결과가 *strategy 단계에서 예상 가능* 했나?
- Yes → ROI 낮음. 다음 시도는 *예상 가능 zone 외부* 로.
- No → 결과 자체가 정보.

## 무엇이 작동했나
- (구체적으로)

## 어디서 막혔나
- 정확히 어떤 단계, 어떤 부등식/등식에서?
- 막힌 본질적 이유 (단순 계산 오류 vs 아이디어 한계)?

## 알려진 벽인가, 새로운 벽인가
- 문헌에 이미 알려진 장애물이라면 어디 (`papers/INDEX.md`)?
- 새로 발견한 패턴이면 `learnings/` 에 추가.

## 다음 시도 후보
- 같은 전략 변형: ...
- 직교 접근: ...
- 우회: 이 막힘을 가정으로 두고 다른 부분 진행?

## 추출된 보조정리/관찰
검증된 것은 `lemmas/`로 이동.
```

## 2. 논문 읽기 프로토콜

> 논문을 읽을 때는 아이디어뿐 아니라 **저자가 그 아이디어에 도달한 사고 과정을 추정**하며 읽는다. 이것이 새로운 아이디어를 생성하는 핵심 훈련이다.

각 논문에 대해 `papers/INDEX.md` 항목 + 필요시 `papers/notes/<key>.md` 작성:

### 2.1 표면 (논문이 명시하는 것)

- **결과**: 무엇을 증명했나? (정확한 statement)
- **주요 도구**: 어떤 기법/정리?
- **이전 결과 대비 개선**: 무엇을 강화했나?

### 2.2 심층 (저자의 사고 과정 추정 — 핵심)

이 섹션이 가장 중요하다. 추측이라도 명시적으로 적는다.

- **출발점 가설**: 저자는 어떤 직관/관찰에서 출발했을까?
  - 예: "Selberg는 trace formula를 보고 zeta zeros가 spectral 객체일 수 있다는 유추를 했을 것"
- **핵심 도약 (key leap)**: 어디가 비-자명한 점프인가? 왜 거기를 시도했을까?
  - 어떤 *기존 도구의 한계*를 보고, *어떤 다른 분야의 도구*를 빌려왔나?
- **막혔을 만한 곳**: 저자도 처음엔 막혔을 곳은? 어떻게 우회했나?
- **버려진 시도 (추정)**: 명시되지 않지만 시도했다 실패했을 접근은?

### 2.3 메타 (우리에게 주는 학습)

- **이 사고방식의 일반화**: 저자의 추론 패턴을 다른 곳에 적용 가능?
- **결합 가능성**: 다른 논문의 아이디어와 합쳐볼 수 있는 곳?
- **막힌 지점**: 이 논문도 결국 RH 자체는 못 풀었다. 어디가 그 한계?

### 2.4 작성 양식 (papers/INDEX.md 항목 예시)

```markdown
### [conrey1989] Conrey, "More than two fifths of the zeros of the Riemann zeta function are on the critical line"

- **상태**: downloaded / read / digested
- **링크**: papers/conrey1989.pdf
- **카테고리**: analytic / mollifier method
- **결과**: N(T) 영점 중 ≥ 40.88% 가 임계선 위에 있음
- **도구**: Levinson method + mollifier 최적화
- **사고 과정 추정**: Levinson(1974)의 1/3 결과를 본 저자는 mollifier를 더 정교하게 설계하면 비율을 올릴 수 있다고 봤을 것. 핵심 도약은 모리피어를 1차에서 더 긴 Dirichlet 다항식으로 확장한 것 — 이는 "변분 문제"로 환원되고, 변분 최적화 기법을 적용한 것이 비-자명. 막힘 지점: 이 방법은 본질적으로 "임계선에 있는 것을 세는" 도구라, 100%까지 올려도 RH 증명이 아니다 (모든 영점이라는 보장 X).
- **우리에게 주는 학습**: Levinson 계열은 비율 push 한계 있음. 본질적 우회 필요.
```

## 3. 정직 (Honesty) 규율

증명 시도에서 가장 큰 적은 **자기기만**이다. 다음 규칙 강제:

1. **확신도 태깅 의무**: 모든 비자명 단계에 `[rigorous|plausible|hand-wave|guess]` 중 하나.
2. **순환 논증 체크**: 결론을 어디선가 (변형된 형태로) 가정하지 않았나?
3. **한계 명시**: 가정 / 미증명 lemma / 누락된 케이스를 work.md 끝에 별도 섹션 "Open Gaps"로.
4. **"증명했다" 트리거**: postmortem 에 "증명 완료" 라고 쓰려면 *반드시* 다음 통과:
   - [ ] 모든 단계 `[rigorous]`?
   - [ ] Open Gaps 비어있음?
   - [ ] 알려진 반례 후보 (예: large height 영점) 에서 검증됨?
   - [ ] 본 시도가 *왜* 165년간의 다른 시도가 못 한 것을 했는지 한 단락 설명 가능?
   - 4번에 답이 없으면 거의 확실히 오류다.

## 4. learnings/ 누적 규칙

- 가로지르는 패턴 발견 시 즉시 `learnings/<topic>.md` 생성/업데이트.
- 예: `learnings/walls.md` (반복되는 벽), `learnings/heuristics.md` (작동한 휴리스틱), `learnings/approaches_taxonomy.md` (접근법 분류 진화).
- 매 시도 시작 시 `learnings/` 전체 빠르게 재훑기.

## 5. lemmas/ 운영

- 단일 attempt 안에서 검증된 보조정리는 `lemmas/<descriptive_name>.md`로 추출.
- 각 lemma 파일: statement, proof, where used, dependencies.
- 새 시도는 lemmas 재사용 가능 (재증명 X).

## 6. Cross-domain 확장 프로토콜 (강점 활용)

> 본 하네스를 운영하는 LLM(Claude)의 비교우위는 **수많은 도메인의 지식을 동시 보유 + 즉시 유추 가능**이라는 점이다. 사람 수학자는 평생 한 분야에 specialize 해야 하지만, LLM은 다른 분야의 도구·은유·구조를 즉시 빌려올 수 있다. 이 강점을 *우연*이 아니라 *프로토콜*로 강제한다.

각 시도의 strategy.md 에 **의무 섹션 "Cross-domain pass"** 를 둔다. 다음 4단계에 명시적으로 답:

### A. 유추 패스 (analogy sweep)
RH의 핵심 구조 — *"어떤 객체의 스펙트럼/영점이 특정 곡선 위에 있다"* — 와 isomorphic 또는 metaphorically 가까운 비-수학 분야 사례를 5개 이상 나열.

| 도메인 | 가능한 유추 |
|---|---|
| 물리 (양자) | 자기수반 연산자 스펙트럼이 실수 직선 위 (Hilbert–Pólya) |
| 통계물리 | Lee–Yang 정리: ferromagnet 분배함수 영점이 단위원 위 |
| 신호처리 | linear-phase / all-pass / minimum-phase 필터의 영점 위치 |
| 제어이론 | 시스템 안정성 = pole이 특정 반평면 |
| CS / 그래프 | spectral graph theory, expander, Ramanujan graph |
| 동역학계 | Ruelle / dynamical zeta 함수, Selberg ↔ length spectrum |
| 확률 | random matrix GUE eigenvalue 분포 |
| 코딩이론 | weight enumerator의 영점 (MacWilliams) |
| 화학 | molecular orbital의 에너지 준위 |
| 음악/음향 | resonance peak, formant 위치 |
| 경제 | Black–Scholes의 implied volatility surface 모양 |
| 생물 | population dynamics fixed point의 안정성 |

이 중 *시도와 직접 연결될 가능성이 있는 것*을 골라 B로.

### B. 도구 임포트 (tool import)
A에서 고른 분야의 *구체적 도구·정리·기법*을 1개 이상 명시. 그것이:
- (i) 이미 RH에 적용된 적 있는가? (literature 확인)
- (ii) 적용 시도되었으나 막혔다면 *왜* 막혔는가?
- (iii) 적용된 적 없다면 *왜 가능성이 있어 보이는가*?

(iii)이 본 하네스의 **탐색 채널**이다.

### C. 외부인 설명 패스 (explain-to-an-outsider)
RH를 다음 가상 청자에게 설명한다고 가정 — 각자의 직업적 본능이 던질 질문을 적는다:
- **물리학자**: "이 ζ는 어떤 Hamiltonian의 partition function인가?"
- **컴퓨터 과학자**: "이걸 결정하는 알고리즘의 시간 복잡도 lower bound는?"
- **엔지니어**: "이 시스템을 안정적으로 만드는 *제어*는 무엇인가?"
- **확률론자**: "어떤 random process의 zero-set 분포로 보이는가?"
- **위상수학자**: "이 영점들의 모듈라이 공간은?"
- **로직 전공자**: "이 statement의 *증명 가능성* 자체는 ZFC에서 결정 가능?"

질문 중 우리가 답을 *모른* 것이 새 각도가 될 수 있다.

### D. 제약 변형 (problem morphing)
- **약화**: 더 약한 statement 중 풀린 게 있나? (예: 무영점 영역, density bound)
- **강화**: 더 강한 statement (GRH, Lindelöf, GUE conjecture, Goldbach 류)는 RH와 어떻게 연결?
- **일반화**: function field (Weil이 풀음!), dynamical zeta, Selberg, Dirichlet L 등으로 확장 — *거기서 풀린 도구가 ζ로 옮겨가지 않는 이유*는?
- **특수화**: 부분적 영점 (작은 height)에 한정 시 어떤 lemma가 새로 통하나?

이 단계의 핵심은: **본 문제의 풀린 친척과 안 풀린 본인을 비교 → 친척에서 작동한 도구가 본인에게 안 통하는 *기술적 이유*가 곧 RH의 본질적 어려움**.

### Postmortem 후속
시도 종료 시 postmortem 에 한 단락:
- "Cross-domain pass에서 떠올린 X 도구는 실제로 시도해보니 Y 이유로 부적합 / 뜻밖에 Z 통찰을 줌"
- 누적 학습은 `learnings/cross_domain_lens.md` 에 (analogy → tool → 결과).

### 운영 메타
- A~D 의 답이 **빈약하면 시도 자체가 빈약하다**. strategy 단계에서 충분한 시간을 cross-domain pass 에 쓴다.
- 이 프로토콜은 LLM 운영 하네스 — *재생가능한 사고 패턴* 이지 *반드시 통하는 마법* 이 아니다.

## 7. Specialist 패널 (분야별 심층 검토)

> RH는 여러 분야를 *각각 깊이 이해한* 수학자가 풀 수 있을 가능성이 높다. §6 의 cross-domain 유추를 넘어, 각 분야 깊이로 *검증·확장* 하는 specialist 패널을 운영한다. 상세는 **`SPECIALISTS.md`** 참조.

핵심:
- Tier 1 (의무): 해석적 정수론 / 대수기하 (function field) / NCG·작용소대수 / RMT·확률 / 조합·하드해석 (Tao류) — 5개 specialist 페르소나.
- Tier 2 (선택): 양자물리, 동역학, 위상, 논리, CS, 자유확률 등.
- 각 specialist 는 자기 분야의 *기술적 도구·관습·한계* 시각으로 4개 질문에 답: (a) 자명/비자명 분리 (b) 사용 가능 도구 (c) 분야 내 함정 (d) 본 분야 한계가 RH 본질에 대해 말하는 것.
- generalist (메인 흐름) 가 specialist 답들의 *모순·강화·격차*를 정리하고 통합 가설 작성.
- 시도 종료 시 *반환 라운드* — 막힌 곳을 specialist 에게 다시 물어 다음 시도 입력으로.

§6 (cross-domain 유추) 와 §7 (specialist 깊이) 의 차이:
- §6 = **breadth pass** — 다른 분야가 보일 만한 *유사 구조* generation
- §7 = **depth pass** — 각 분야 *내부의 정확한 도구·한계·함정* 으로 검증·확장

두 패스는 보완적이며 둘 다 의무다.

## 8. Computational Lever (코드·실행 강점)

> 일반 수학자 대비 LLM+코드 환경의 비교우위는 **분 단위로 수치/기호 계산을 돌릴 수 있다는 점**. brainstorm 단계의 가설을 *즉시* 검증하거나 반증할 수 있다. 이 강점을 *우연*이 아니라 *프로토콜* 로 강제한다.

### 활용 채널
각 시도의 strategy.md 에 **"Computational verifications"** 섹션 추가. 다음 중 적용 가능한 것을 적시:

#### A. 수치적 가설 검증 (numerical sanity)
- 특정 statement 가 *작은 case* 에서 성립하는지 즉시 체크.
- 예: 새 가설 "X(n) ≤ f(n) for all n" → n=1..10000 에서 mpmath 로 계산.
- 반례 발견 시 가설 즉시 폐기 → 시간 절약.

#### B. 동치 형태 수치 비교 (equivalent reformulations)
RH 의 동치 statements 가 풍부함 (Conrey 2003 §"동치 형태"):
- M(x) = O(x^(1/2+ε)) (Mertens 류)
- Li's criterion: λ_n ≥ 0 for all n
- Nyman–Beurling: L²(0,1) span 조건
- Weil positivity: Σh(γ) ≥ 0
새 시도의 결과를 *다른 동치 형태로 변환해 수치 비교* 가능. 변환이 막히면 본 시도가 어떤 동치류와 충돌하는지 파악.

#### C. 보조 정리의 prototyping
새 lemma 후보를 sympy/mpmath 로 *기호 또는 수치* 검증 후 정식 증명 시작.
- 예: 적분 변환의 닫힌 형태 추측 → sympy 로 확인.
- 예: 부등식의 sharp constant 추측 → numerical optimization 으로 후보 추출.

#### D. 알려진 결과 재현
시도의 첫 단계로 *알려진 RH-동치 또는 부분 결과* 를 코드로 재현 — 도구 정확성 + 본인 이해도 동시 검증.

#### E. Counterexample search (sanity for "제 시도가 너무 강함")
"이 보조정리가 성립하면 RH" 같은 강한 명제를 만들었을 때, 그것이 *실제로 성립할 가능성이 있는지* 작은 case 검증. 너무 강하면 자명한 반례가 작은 n 에서 나옴.

#### F. RMT / 통계적 정합성
영점 분포가 GUE 등과 부합하는지 직접 시뮬레이션.

### tools/ 모듈 매핑
- `verify_zeros.py` — 영점 위치 검증 (이미 존재)
- `mertens.py` — M(x), 부분합, Mertens 추측 검증 (예정)
- `li_criterion.py` — λ_n 계산 (예정)
- `pair_correlation.py` — Montgomery pair correlation (예정)
- `moments.py` — I_k(T) zeta moments (예정)
- `explicit_formula.py` — von Mangoldt explicit formula 검증 (예정)
- `fetch_paper.py` — 논문 추가 (이미 존재)

새 모듈은 시도 진행 중 *필요 시* 추가 — 미리 다 만들지 않음.

### 정직 규율 (수치 검증의 함정)
1. **수치 ≠ 증명**: n=10^6 까지 성립한다고 ∀n 증명 아님. *반증* 도구로는 강력, *증명* 도구로는 무효.
2. **정밀도 명시**: mpmath dps 명시. 정밀도 부족이 false confirmation 이 될 수 있음.
3. **알고리즘 한계**: 영점 계산 자체가 RH 가정 하에 빠른 알고리즘 (Riemann-Siegel) — 순환 의존 주의.
4. **시드/seed 의존**: 통계 비교는 sample size + seed 명시.
5. 결과를 work.md 에 기록할 때 `[numerical, dps=50, n=10^4]` 같은 메타데이터 포함.

### 운영 메타
- `tools/` 에 새 모듈 작성 시 docstring 에 *수학적 정의* 와 *알려진 한계* 명시.
- 매 시도의 work.md 에서 코드 호출 결과는 `[numerical]` 태그 + 코드 위치 (`tools/<file>.py:func`) 로 reference.
- 코드로 *반례* 발견 시 `learnings/` 또는 `lemmas/` 에 영구 기록 — 미래 시도의 lower bound.
