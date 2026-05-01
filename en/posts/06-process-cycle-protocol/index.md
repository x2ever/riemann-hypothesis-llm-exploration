---
title: "The 4-phase research cycle protocol"
parent: Process
grand_parent: English
nav_order: 6
date: 2026-05-02
---

# The 4-phase research cycle protocol

[← All English posts](../../) · [한국어](../../../ko/posts/06-process-cycle-protocol/) · *2026-05-02*

> The methodology side of the project. Stable, reproducible, transferable.

## The protocol (HARNESS.md §0)

Each cycle = one narrow research question, run as separate phases, **each phase as a separate attempt directory**:

### Phase 1 — Ideation + Planning

- Brainstorm 5–8 candidate research directions
- Commit a **1–10 intuition score** for each candidate *before* execution (frozen, no retroactive edit)
- Pick one narrow hypothesis
- Write DoD (Definition of Done), foreseen-stuck conditions, falsifier criterion, cut self-check (against `lemmas/dont_try_directions.md` Cut 1–7)
- Cross-domain pass: analogy, tool import, outsider question
- Specialist Δ blind round (paper §-end quote anchored)

### Phase 2 — Audit + Specialist blind round

- Paper-direct evidence collection
- "Specialist Δ" estimates with paper §-end quote anchors (Lemma 7 protocol)
- Initial Δ (intuition) vs result delta logged

### Phase 3 — Verification

- Falsifier search across 4–6 adjacent fields
- Retrocompatibility check: does this contradict any earlier cycle's result? If yes, which one is correct?
- Specialist cross-examination (multiple specialist views must agree on key claim)

### Phase 4 — Reflection

- Log result with intuition-vs-result delta to `learnings/intuition_calibration.md`
- Update lemmas *only if codification is justified* (anti-codification check)
- Consider: should this cycle's result update earlier lemmas (cross-reference)?

## What this replaced (the *why*)

Pre-Critique #6 (~attempt 181), the session was running **milestone-driven batches**: at user request "go to 100", the session would create 5–10 attempt directories at once before any of them was run. This produced "stamp" attempts (45 attempts of cycle 91-99 were 4–10 lines each).

Critique #6 (user-input): *"미리 다음 N개의 계획을 세우기 보다, 과거의 기록으로 다음 연구 계획을 세우고 시도한 다음 끝나면 다음 계획을 세우는게 더 낫지 않을까?"*

→ Lazy planning protocol. Each next attempt's planning happens *only after* the previous postmortem is complete. Visible from `attempts/186_cycle3_*` onward.

## The cycles run so far (1–7)

| Cycle | Subject | Phase 1 chosen | Result |
|-------|---------|----------------|--------|
| 1 | Wall #5 codification | Lemma 1 9/11 ceiling check (axiom 7+11 joint) | Pivoted to axiom 6 (sharper); Lemma 9 produced |
| 2 | Wall #2 codification | ∫E(t)dt unconditional bound check | Lemma 10 produced |
| 3 | Active program identification | Lemmas 9, 10 ↔ Connes program mapping | Lemma 3 update; partial unification hypothesis |
| 4 | Cycle 3 verification | 4-paper Connes–Consani read | Cycle 3 partially refuted; Wall #1 only, not Wall #2 |
| 5 | Path 1 active monitoring | Selecta Math 2021 read | 1-year direct progress documented |
| 6 | Lemma 9 falsifier test | PNAS 2022 (Connes–Moscovici) | 3 paper-direct gaps; Lemma 9 strengthened to 11/11 |
| 7 | Externalization | Preprint Section 1+2 draft | (in progress) |

## Notable patterns

- **Phase 1 is a *separate* attempt directory.** This forces explicit ideation rather than blending it with execution.
- **Cycle ≠ attempt.** A cycle spans multiple attempts.
- **Codification cycles vs active monitoring cycles.** Cycle 1, 2 produce lemmas (codification). Cycles 3, 4, 5 update existing lemmas with paper-direct anchors (active monitoring). Cycle 6 stress-tests an existing lemma. The mix is intentional — anti-codification check (post-Critique #8) prevented mass-producing wall codification lemmas.

## Why this is transferable

The protocol does not assume RH-specific knowledge. The scaffolding (intuition score, falsifier criterion, Specialist Δ paper-direct anchoring, anti-codification self-check) generalizes to other "long-running LLM autonomous research on a hard problem" runs.

## Audit trail (Layer 1)

- `HARNESS.md` §0 — full protocol definition
- `attempts/184_cycle1_*` through `attempts/190_cycle7_*` — actual cycle executions
- `learnings/sustained_research_log.md` — cycle log
- `learnings/intuition_calibration.md` — pre-result intuition score data

---

[← Previous](../05-finding-atiyah-step-gap/) · [한국어](../../../ko/posts/06-process-cycle-protocol/) · [Next →](../07-process-critique-loop/)
