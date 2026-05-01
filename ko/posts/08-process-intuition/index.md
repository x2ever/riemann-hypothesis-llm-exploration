---
title: "직관 calibration 데이터"
parent: 한국어
nav_order: 8
date: 2026-05-02
---

# 직관 calibration 데이터

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/08-process-intuition/) · *2026-05-02*

> 사전 1–10 score, Phase 1에서 frozen, 결과 비교. 6 cycles 데이터. Protocol auditable; calibration claim *empirical-only*.

## Protocol

각 cycle Phase 1 ideation 시 5–8 candidate research direction brainstorm. 각 candidate에 1–10 *직관 score* Phase 1 commit (frozen, retroactive 수정 X). 가장 높은 score 후보 → Phase 2 execution.

Cycle 완료 후 결과 verdict 로그:
- **YES** — broad pattern 적중, narrow result confirmed
- **PARTIAL YES** — broad pattern 적중, narrow result sharpening 필요
- **PARTIAL** — broad pattern 적중, 그러나 후속 cycle에서 weakened
- **NO** — broad pattern 틀림

## 데이터 (6 cycles)

| Cycle | Top score | 선택된 candidate | Verdict | Note |
|-------|-----------|-----------------|---------|------|
| 1 | 8/10 | Lemma 1 9/11 ceiling (axiom 7+11 joint) | PARTIAL YES | axiom 6으로 pivot (sharper); Lemma 9 |
| 2 | 8/10 | Wall #2 ∫E(t)dt codification | YES | Lemma 10 (cycle 1 형식 재사용) |
| 3 | 8/10 | Cycles 1+2 → Connes program meta-mapping | PARTIAL | Cycle 4가 Wall #2 mapping 부분 반박 |
| 4 | 8/10 | Connes-Consani 4-paper read | YES | Cycle 3 partial refutation; Wall #1-only |
| 5 | 8/10 | Selecta Math 2021 deep | YES | 1년 direct progress 식별 |
| 6 | 9/10 | PNAS 2022 falsifier of Lemma 9 | YES | 3 paper-direct gaps; Lemma 9 11/11 |

**경험적 패턴**: 8/10 score → 4 YES / 2 PARTIAL = 약 80% PARTIAL-YES-or-better rate (n = 5 at score 8).

9/10 score → 1 YES (n = 1). 9/10 calibration claim 불가능.

## Caveats

- **n = 6은 너무 작음** — 통계적 유의성 calibration claim 불가능. 위 패턴은 suggestive, significant X.
- 7/10 미만 candidate는 *선택 안 됨* → 실제 outcome 미관찰 = false-negative data 부재.
- **Reporter bias**: score commit한 동일 세션이 verdict 평가. 3rd-party-blind verdict assessment X.
- Cycle 3의 *PARTIAL* verdict는 Cycle 4가 부분 반박해서 emerge. 즉 후속 cycle이 이전 verdict update 가능. Protocol의 *feature*, bug X. 그러나 *"verdict"* 자체가 moving target임 의미.

## *유용한* 점

방법론 — *commit numeric pre-result score, freeze, run, log delta* —은 다른 LLM autonomous research run에 transferable. 산출:

1. **Auditable predictions**. 본 프로젝트 reading 누구나 score가 Phase 1에서 실제 commit됐는지 check (`attempts/<cycle>_*/planning.md` timestamps).
2. **Time-series calibration tracking**. n = 100 cycles 시 calibration curve 의미 있어짐.
3. **Anti-rationalization discipline**. Score frozen 후 positive outcome match 위해 retroactive raise 불가능.

## 본 데이터가 *아닌* 것

- Calibration *claim* 아님 (n 너무 작음).
- LLM 직관 일반 측정 아님 — 본 세션, 본 도메인, 본 protocol만.
- Number로 transferable X; *discipline*으로 transferable.

## Audit 방법

각 cycle:

1. `attempts/<cycle>_*/planning.md` — Phase 1 file. Score가 Phase 2 run 전 commit 확인.
2. `attempts/<later>_*/work.md` 또는 `lemmas/<lemma>.md` — Phase 2/3/4 result.
3. `learnings/intuition_calibration.md` — verdict log.

Git history (timestamps)이 temporal order 확정.

## Audit trail (Layer 1)

- `learnings/intuition_calibration.md`
- `learnings/sustained_research_log.md`
- `attempts/184_*` ~ `attempts/189_*`

---

[← Previous](../07-process-critique-loop/) · [English](../../../en/posts/08-process-intuition/) · [Next: Honest Scope →](../09-honest-scope/)
