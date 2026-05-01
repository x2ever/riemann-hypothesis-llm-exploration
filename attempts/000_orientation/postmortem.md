# Postmortem — Attempt 000

## 결론

**부분 성공** (orientation 의 의도된 범위 내).

- 8편 정독 + background 4파일 + INDEX 사고과정 + specialist 라운드 7명 + walls 5개 + 결합 4개 + 다음 시도 후보 3개 도출 완료.
- 본 시도는 *증명 시도가 아님* — DoD 모두 만족.
- **운영 결함 3개** 발견 (HARNESS §7 의 개선 후보).

## 무엇이 작동했나

1. **specialist 패널 첫 가동**: 7명 시뮬레이션이 RH 의 다른 측면을 부각하고 *수렴 지점*과 *격차* 모두 식별.
2. **벽 분류**: 5개 본질적 벽 (FROBENIUS-GAP, FORWARD-TIME, SHARP-CONSTANT, CONSPIRACY, SELF-ADJOINT-RIGOR) — 각각 어떤 접근법이 부딪히는지 mapping.
3. **결합 식별**: 4개 결합 후보 (II+VI, III+VI, V+VII, II+VII+code) — 단일 분류 보다 강할 가능성 신호.
4. **Riemann 1859 재해석**: RH 가 *부산물*. 다음 시도들이 *RH 를 직접 노리지 않는* 옵션 포함.

## 어디서 막혔나

본 시도는 *meta-attempt* 라 "막힘" 의 의미가 다름. 한계:

- **벽 분류의 *본질성* 검증 불가**: 본 시도 내에서 벽이 *진짜* 본질적인지 검증 도구 없음. 다음 시도들이 진짜 그 벽에 부딪힐 때 검증.
- **specialist 시뮬레이션 한계**: S2 와 S3 의 답이 confirmation bias 가능. 진짜 specialist 의 *반대 시각* 시뮬레이션 가능성 미확인.
- **결합 식별의 자의성**: 4개 결합 후보가 *plausible* 하나 *왜 specifically 그 4개* 인지 정량 근거 약함.

## 알려진 벽인가, 새로운 벽인가

본 시도가 식별한 5개 벽 중:
- **#1 FROBENIUS-GAP**: 알려짐 (Bombieri Clay 명시). *재발견* 이 본 시도 가치.
- **#2 FORWARD-TIME**: Rodgers–Tao paper 자체에서 비대칭 인지하나 *명시적 wall name* 부여한 사례 적음. 본 시도가 *명명* 한 가치.
- **#3 SHARP-CONSTANT**: 알려짐. mollifier 분야 일반.
- **#4 CONSPIRACY**: 알려짐 (Iwaniec, Conrey).
- **#5 SELF-ADJOINT-RIGOR**: 알려짐 (BBM 자체 인정).

→ *새로움* 은 벽 자체가 아니라 *벽 사이 mapping* + *결합 후보* + 우회 cross-domain 후보.

## 다음 시도 후보 (DoD 핵심 산출물)

3개 후보. 각각 좁은 가설 + specialist 의무 호출 + cross-domain pass 후보 + 코드 채널 + 성공/실패 기준.

---

### 후보 A: `001_li_criterion_rmt_cross_check`
**가설** (좁음):
> "Li's criterion λ_n 의 sign distribution 이 RMT (GUE) 가 예측하는 형태와 *얼마나* 정합적인가? n 이 커질 때 정량 일치하면 RH 의 새 양적 evidence; 어긋나면 RH 의 *어떤 측면이 RMT 와 분리되는지* 신호."

- **분류**: II (동치) + VII (RMT) + IX (computational).
- **specialist 의무 호출**: S1 (해석적) + S4 (RMT) + Tier 2 추가: S11 (free probability — 미탐색 채널).
- **cross-domain pass 후보**: 신호처리 spectrum analysis (λ_n 의 sign sequence 를 *시계열* 로 보고 power spectrum 분석).
- **코드 채널**: `tools/li_criterion.py` 기존 + RMT λ 분포 계산 모듈 (`tools/rmt_li.py` 신규 작성).
- **성공 기준**: 첫 100 ~ 1000 zeros 사용 λ_1..λ_100 계산 + GUE 무작위 행렬 100 개의 동등 quantity 비교 + 분포 일치/불일치 정량.
- **실패 기준**: RMT 와 *완전 일치* 또는 *완전 비정합* 둘 다 진단 불가 시 — 도구가 sharp 하지 않음 의미.
- **예상 막힘**: Li's criterion 자체에 *모든 영점* 합 필요인데 유한 truncation. 보정 항 정량.
- **가치**: *작은* 시도. 코드 활용 강함. 결과가 *단순한 confirmation* 이라도 baseline 정량.

---

### 후보 B: `002_forward_heat_via_optimal_transport`
**가설** (좁음 but 야심):
> "Rodgers–Tao 의 zeros heat flow 동역학 ($\partial_t x_k = 2\sum_{j \neq k} 1/(x_k - x_j)$) 을 *optimal transport* 의 gradient flow 로 재해석. Wasserstein metric 위에서 forward-time 의 contraction 을 보일 수 있는가?"

- **분류**: VI (heat flow) + XI (비정통: optimal transport).
- **specialist 의무 호출**: S5 (조합·하드해석) + S6 (양자/통계물리) + S4 (확률 — Wasserstein 측도).
- **cross-domain pass 후보**: Ricci flow on metric measure spaces (Lott–Sturm–Villani synthetic Ricci), gradient flow of free energy.
- **코드 채널**: zeros 의 forward heat 시뮬레이션 + Wasserstein-2 distance 시간에 따라 추적 (`tools/heat_flow_wasserstein.py` 신규).
- **성공 기준**: forward-time 에서 *어떤 functional* 이 단조 (energy 또는 Wasserstein-W₂(empirical, GUE)) 함을 *수치* 또는 *부분 정량* 으로 시작. 정성적 단조성 신호 발견.
- **실패 기준**: *모든* 시도된 functional 이 forward-time 에서 단조 X (즉 비대칭이 *측도* 차원에서 더 깊다).
- **예상 막힘**: empirical zero distribution 의 Wasserstein 추정에 정밀도 문제. forward-time evolution 의 정량 추적이 numerical instability 가능.
- **가치**: 벽 #2 (FORWARD-TIME) 직접 도전. cross-domain 강점 활용. **실패해도 vacuum 이 vacuum 임을 정량화** — `learnings/walls.md` 에 강력한 입력.

---

### 후보 C: `003_riemann_xi_as_byproduct_search`
**가설** (Riemann 직관 직접 따름, 가장 비정통):
> "Riemann 의 1859 paper 가 보여준 *RH 는 explicit formula 의 부산물* 시각을 따라, RH 를 *직접* 노리지 않는 어떤 *더 큰 structure* (특정 함수 가족, 새 trace formula, 새 explicit formula) 안에서 RH 가 *trivially* 따라 나오는 형태를 찾는다."

- **분류**: 메타 — IV/V/VIII 의 union + cross-domain.
- **specialist 의무 호출**: S1 + S2 + S3 (가장 깊은 분야들 동시) + S9 (논리 — meta 시각).
- **cross-domain pass 후보**: 정보이론 (maximum entropy distribution as explicit formula), 위상 (cobordism / TQFT 의 partition function 형식).
- **코드 채널**: 비교적 약함 — 이 시도는 *개념적*. 다만 *후보 함수 가족* 발견 시 수치 검증 (작은 case).
- **성공 기준**: RH 가 *정확히 어떤 더 큰 statement* 의 *trivial corollary* 인지 후보 1개 이상 식별 — 그것이 (i) 알려진 더 어려운 추측이거나 (ii) 새 statement 라면 미증명.
- **실패 기준**: 후보가 *모두* 알려진 RH-동치들과 trivially 동치 → 새 시각 부재.
- **예상 막힘**: 본 시도는 *philosophical*. 정량 결과 산출이 어려울 가능성. *후보 발견* 자체가 valuable 한지 자기 평가 어려움.
- **가치**: 가장 *야심* 적이고 *high variance*. 잘 되면 본 프로젝트의 *direction* 자체를 바꿀 수 있음. 안 되면 1주 정도 brainstorm 하다 결론 X.

---

## 추천 순서
1. **후보 A 먼저** (`001_li_criterion_rmt_cross_check`) — small, computational, 도구 검증 동시.
2. **후보 B 다음** (`002_forward_heat_via_optimal_transport`) — 벽 #2 직접 도전, 야심.
3. **후보 C 마지막** (`003_riemann_xi_as_byproduct_search`) — A, B 의 *결과* 가 후보 C 의 brainstorm 입력 가능.

세 후보가 *서로 정보 공유* 함 (A 의 RMT 정합 결과 → B 의 measure 도구 → C 의 더 큰 structure 후보).

---

## 추출된 보조정리/관찰 (lemmas/ 후보)

본 시도에선 *증명된 lemma 무*. 다음 시도들이 산출 시 `lemmas/` 로.

## 학습 누적

본 postmortem 의 발견을 다음 두 파일에 누적:
- `learnings/walls.md` — 5개 벽 + 우회 후보 ☐
- `learnings/approaches_taxonomy.md` — 11개 분류 + 4개 결합 + 우선순위 ☐
- `learnings/specialist_consensus.md` — 7명 specialist 첫 사용 결과 + 운영 결함 3개 ☐
- `learnings/cross_domain_lens.md` — 본 시도에서 떠오른 cross-domain 후보 ☐

위 4개 파일 채우는 작업을 *Step 7* 로 이어서.

## 운영 결함 + HARNESS 개선 후보

1. **§7 Tier 1 분리**: 대수기하 (function field, étale cohomology) 와 algebraic number theory (Iwasawa, families) 분리 권장. 현재 S2 안에 두 시각 혼재.
2. **§7 confirmation bias 방지**: specialist 답을 다른 specialist 가 보지 못하게 *blind* 라운드 권장. 두 번째 의견을 독립적으로.
3. **§7 반환 라운드**: 본 시도에서 미시도 — 다음 시도 (`001_*`) 에서 처음 검증.
4. **§6 cross-domain pass 의 D (problem morphing)** 가 *defaults* 로 너무 형식적. 더 야심적 morphing 권장 가이드 추가.
5. **§8 computational** 의 정밀도 메타 표기가 freeform — 표준 양식 권장 ($[numerical, dps=N, k=K, seed=S]$).

위 5개를 다음 시도 시작 전 HARNESS 에 반영 가능 — 단, *과도한 형식주의* 위험. 발견된 결함이 실제 다음 시도에서 손해를 끼친 후 반영 권장.
