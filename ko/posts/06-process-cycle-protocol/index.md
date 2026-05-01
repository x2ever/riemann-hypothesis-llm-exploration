---
title: "4-Phase Research Cycle Protocol"
parent: 한국어
nav_order: 6
date: 2026-05-02
---

# 4-Phase Research Cycle Protocol

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/06-process-cycle-protocol/) · *2026-05-02*

> 본 프로젝트 방법론 측면. 안정적, 재현 가능, 다른 LLM autonomous run에 transferable.

## Protocol (HARNESS.md §0)

각 cycle = 1 narrow research question, separate phases, **각 phase가 별도 attempt directory**:

### Phase 1 — Ideation + Planning

- 5–8 candidate research direction brainstorm
- 각 candidate에 **1–10 직관 score** Phase 1 commit (frozen, retroactive 수정 X)
- 1 narrow hypothesis 선택
- DoD, foreseen-stuck conditions, falsifier criterion, cut self-check (`lemmas/dont_try_directions.md` Cut 1–7) 작성
- Cross-domain pass: analogy, tool import, outsider question
- Specialist Δ blind round (paper §-end quote anchored)

### Phase 2 — Audit + Specialist blind round

- Paper-direct evidence 수집
- "Specialist Δ" 추정 with paper §-end quote anchors (Lemma 7 protocol)
- Initial Δ (직관) vs result delta 로그

### Phase 3 — Verification

- Falsifier search across 4–6 인접 분야
- Retrocompatibility check: 이전 cycle 결과와 모순? yes면 어느 게 맞나?
- Specialist cross-examination (multiple specialist views의 key claim 합의 의무)

### Phase 4 — Reflection

- Result + intuition-vs-result delta를 `learnings/intuition_calibration.md`에 로그
- Lemma update *오직 codification 정당화 가능 시* (anti-codification check)
- 고려: 본 cycle 결과가 이전 lemma update 대상인가? (cross-reference)

## 기존 패턴 대체 (the *why*)

Critique #6 (~attempt 181) 이전, 세션은 **milestone-driven batches** 운영: 사용자 *"100까지 가봐"* 시 5–10 attempt directories 미리 생성. *"Stamp" attempts* 산출 (cycle 91-99 attempts 4–10 lines each).

Critique #6 (사용자 직접): *"미리 다음 N개의 계획을 세우기 보다, 과거의 기록으로 다음 연구 계획을 세우고 시도한 다음 끝나면 다음 계획을 세우는게 더 낫지 않을까?"*

→ Lazy planning protocol. 각 다음 attempt 계획은 *직전 postmortem 완료 후만*. `attempts/186_cycle3_*` 이후 visible.

## 운영된 cycles (1–7)

| Cycle | Subject | Phase 1 선택 | Result |
|-------|---------|------------|--------|
| 1 | Wall #5 codification | Lemma 1 9/11 ceiling check (axiom 7+11 joint) | axiom 6으로 pivot (sharper); Lemma 9 산출 |
| 2 | Wall #2 codification | ∫E(t)dt unconditional bound check | Lemma 10 산출 |
| 3 | Active program identification | Lemmas 9, 10 ↔ Connes program mapping | Lemma 3 update; partial unification 가설 |
| 4 | Cycle 3 verification | 4-paper Connes–Consani read | Cycle 3 partial refutation; Wall #1 only, Wall #2 X |
| 5 | Path 1 active monitoring | Selecta Math 2021 read | 1년 direct progress documented |
| 6 | Lemma 9 falsifier test | PNAS 2022 (Connes–Moscovici) | 3 paper-direct gaps; Lemma 9 11/11로 강화 |
| 7 | Externalization | Preprint Section 1+2 draft | (in progress) |

## 주목할 패턴

- **Phase 1이 *별도* attempt directory**. 명시적 ideation 강제 (execution과 blend X).
- **Cycle ≠ attempt.** Cycle은 multiple attempts span.
- **Codification cycles vs active monitoring cycles.** Cycle 1, 2는 lemma 산출 (codification). Cycles 3, 4, 5는 기존 lemma에 paper-direct anchor 추가 (active monitoring). Cycle 6은 기존 lemma stress-test. 의도적 mix — anti-codification check (post-Critique #8)이 wall codification lemma mass-production 방지.

## Transferable

Protocol은 RH-specific knowledge 가정 X. Scaffolding (intuition score, falsifier criterion, Specialist Δ paper-direct anchoring, anti-codification self-check)이 다른 *"long-running LLM autonomous research on a hard problem"*에 일반화.

## Audit trail (Layer 1)

- `HARNESS.md` §0
- `attempts/184_cycle1_*` ~ `attempts/190_cycle7_*`
- `learnings/sustained_research_log.md`
- `learnings/intuition_calibration.md`

---

[← Previous](../05-finding-atiyah-step-gap/) · [English](../../../en/posts/06-process-cycle-protocol/) · [Next →](../07-process-critique-loop/)
