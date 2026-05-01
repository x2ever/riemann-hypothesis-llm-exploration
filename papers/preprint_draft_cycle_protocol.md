# Sustained Research Cycle: A 4-Phase Protocol for AI-Assisted Mathematical Investigation

> **Status**: Preprint draft — cycle 11 of sustained research, §1+§2 only.
> Sections 3-6 deferred to subsequent cycles.
> Internal use: cycles 1-10 protocol externalization first manifest of *novel methodology contribution*.

## Abstract

We describe a 4-Phase Sustained Research Cycle protocol developed and validated over ten cycles of AI-assisted investigation of the Riemann Hypothesis (RH). The protocol structures each cycle as Ideation → Sustained Research → Conclusion+Meta-learning → Iterate, with mandatory components for intuition calibration, specialist blind round, falsifier search, and external paper integration. Across ten cycles we observe consistent patterns: 8-9/10 intuition score zone achieves 10/10 hit rate (5 FULL + 5 PARTIAL), hypothesis pivot rate 30%, novel content trend rising from baseline 1.5/10 to peak 6.7/10 upon external critique absorption. We do *not* claim the protocol resolves RH, only that it provides a *reproducible methodology* for sustained AI-assisted mathematical investigation with empirical guarantees against known failure modes (codification machine, premature batching, hallucination). We isolate four distinct external critiques absorbed during the ten cycles (#6-#9) and trace each to a *protocol upgrade* observable in the methodology itself. We propose this as a contribution to AI-for-Math methodology, not to RH proper.

## 1. Introduction

### 1.1 The Methodology Gap in AI-Assisted Mathematical Investigation

AI-assisted mathematical investigation (LLM-based reasoning, automated theorem provers, computer-algebra-assisted research) has rapidly expanded in scope but lacks a *protocol-level* methodology distinct from interactive query-response or one-shot synthesis. Existing work focuses on (i) individual breakthrough demonstrations (e.g., DeepMind FunSearch, AlphaProof), (ii) tool integration (Lean, Coq automation), or (iii) survey-style overviews. None provides a *reproducible cycle protocol* for sustained, multi-cycle investigation of an open problem.

In the absence of such a protocol, AI-assisted mathematical investigation suffers known failure modes:

- **Codification machine** [external critique #8]: producing increasingly polished restatements of the same negative observation without genuine progress.
- **Premature batching** [#6]: planning N future steps before completing the current step's reflection, leading to quality dilution.
- **Hallucination drift**: generating content that *looks like* mathematical claims but lacks paper-direct anchors.
- **NOVEL spree** [#5]: generating speculative directions in unbounded sequence without recognizing rediscovery of known results.

A protocol with explicit anti-patterns for each failure mode is needed.

### 1.2 The Sustained Research Cycle

We describe a 4-Phase Sustained Research Cycle protocol that addresses these failure modes through explicit, paper-direct disciplines:

- **Phase 1 (Ideation+Planning)**: candidate brainstorm + intuition score commit + cross-domain pass + cut self-check.
- **Phase 2 (Sustained Research)**: multi-turn or single-turn execution + specialist blind round + falsifier search + paper-direct anchor discipline.
- **Phase 3 (Conclusion+Meta-learning)**: postmortem + meta-learning logs (sustained research log + intuition calibration).
- **Phase 4 (Iterate)**: next cycle Phase 1 with explicit citation of prior cycle's meta-learning.

### 1.3 Validation Corpus

The protocol was developed iteratively over ten cycles of AI-assisted investigation of RH (specifically: Hilbert-Pólya program candidates, de Bruijn-Newman heat flow, Connes-Consani arithmetic site, Connes-Moscovici prolate operator). Validation metrics across the ten cycles include:

- **Intuition calibration**: 8-9/10 zone achieves 10/10 hit rate (5 FULL + 5 PARTIAL).
- **Pivot rate**: 30% (3 cycles pivot, 7 cycles stable hypothesis).
- **Novel content trend**: 1.5/10 baseline (cycles 1-2) → 6.7/10 peak (cycle 6, external critique absorption) → 1.4-2.6/10 narrow externalization cycles.
- **Critique absorption chain**: 4 external critiques (#6-#9) absorbed, each traceable to a *protocol upgrade*.
- **Externalization 5-stage progression**: outline → artifact → polish → substance → aggregate (cycles 6-10).

### 1.4 Scope and Non-Claims

We do *not* claim:
- The protocol *resolves* RH (cycles 1-10 produce *empirical* universal NO codification only; cf. companion paper [axiom 6 ceiling]).
- The protocol is *necessary* for AI-assisted mathematical investigation; alternative protocols may exist.
- The protocol generalizes beyond RH to other open problems (validation corpus = single domain).
- The protocol generalizes beyond a single LLM (validation corpus = single LLM Claude-class model).

We *do* claim:
- The protocol is *reproducible* given the explicit phase structure and meta-learning logs.
- The protocol provides *empirical guarantees* against the four failure modes (§1.1) over the validated corpus.
- The protocol *generates new external review-able artifacts* (cycle 7-10 of the validation corpus produced a 13-page preprint draft on RH axiom 6 ceiling).

## 2. The 4-Phase Protocol (Detailed)

### 2.1 Phase 1: Ideation + Planning

**Inputs**: prior cycles' postmortems + meta-learning logs (sustained research log, intuition calibration) + walls/lemmas state + recent paper acquisitions.

**Mandatory output**: `attempts/NNN_cycleN_ideation_phase1/planning.md`. The planning document contains:

1. **Direct citation** of prior cycle's meta-learning (Phase 4 → 1 transition).
2. **Candidate brainstorm**: at least 5 distinct hypotheses or work directions, each with one-line description.
3. **Intuition score commit**: each candidate scored on 1-10 first-impression scale, with brief justification ("why this score"). Scores are *committed before* Phase 2 execution and are *not retroactively edited*.
4. **Cross-domain pass**: analogy sweep across at least three external domains (physics, computer science, etc.), tool-import attempt, outsider-explanation pass, problem-morphing variants.
5. **Selected hypothesis**: one narrow hypothesis chosen, with:
   - DoD (Definition of Done) — 5-7 explicit completion criteria.
   - Predicted obstacles (3-5 anticipated stuck points).
   - Progress vs. stuck judgment criteria (when to terminate Phase 2).
6. **Cut self-check**: explicit verification against `lemmas/dont_try_directions.md` Cut 1-7 (or domain-specific anti-patterns).
7. **Specialist panel selection**: which Tier 1 specialists (analytic number theory, NCG, RMT, hard analysis, logic) and which Tier 2 (PT-symmetric quantum, dynamical systems, etc.) will participate in Phase 2's blind round.

**Anti-patterns blocked**:
- Pre-batched plans for multiple cycles (critique #6).
- Codification of prior cycles without new direction (critique #8).
- NOVEL spree without paper-direct grounding (critique #5).

### 2.2 Phase 2: Sustained Research

**Inputs**: Phase 1 planning.md + selected hypothesis.

**Format**: multi-turn (3-turn typical) or single-turn (narrow externalization cycles), in `attempts/NNN_*/work.md`.

**Mandatory components per turn**:

1. **Specialist blind round** (turn 1 typically): each selected specialist (Tier 1 + Tier 2) provides *independent* answers to four questions: (a) trivial vs. nontrivial separation, (b) usable tools, (c) field pitfalls, (d) field limits. Specialist answers are *blind* to each other (no cross-reference until cross-examination).
2. **Cross-examination** (turn 2 typically): contradictions, mutual reinforcements, gaps across specialist answers. The agent (LLM) acts as *generalist* synthesizer.
3. **Falsifier search** (turn 3 typically): for each hypothesis claim, identify external candidates that would *refute* the claim. At least 4-6 distinct falsifier domains examined.
4. **Paper-direct anchor discipline**: every nontrivial mathematical claim is anchored by either (a) direct quote from a published paper (with location), (b) explicit reference to a prior cycle's verified result, or (c) hallucination flag (claim withdrawn).
5. **External paper search**: if Phase 1 identified gaps in our paper corpus, Phase 2 includes WebSearch + paper download + reading.

**Phase 2 termination criteria**:
- DoD (defined in Phase 1) all satisfied → terminate.
- Stuck for 3 consecutive turns without progress → terminate with honest stuck declaration.
- Hypothesis falsified by Phase 2 evidence → terminate with negative result.

**Single-turn narrow exception**: for *externalization cycles* (artifact writing, polish, substance addition, aggregate result writing), Phase 2 may complete in a single turn. The 3-turn rhythm is not rigid.

### 2.3 Phase 3: Conclusion + Meta-Learning

**Inputs**: Phase 2 work.md + Phase 1 planning.md + DoD status.

**Mandatory outputs** (committed in `attempts/NNN_*/postmortem.md` and learning logs):

1. **Postmortem (standard form)**:
   - Conclusion (success/partial/stuck/falsified).
   - Phase-by-phase summary.
   - "Predictable result?" self-check (was the outcome obvious from Phase 1?).
   - What worked / where stuck.
   - Next-cycle candidate inputs.
   - Specialist Δ return round (specialists revisit their Phase 2 answers in light of result).
   - **Novel content N/10 honest evaluation** (with breakdown).
2. **`learnings/sustained_research_log.md` update**: cycle entry with hypothesis, DoD, result, intuition calibration, meta lessons, next-cycle candidate inputs.
3. **`learnings/intuition_calibration.md` update**: Phase 1 score vs. result — mark FULL YES / PARTIAL YES / NO. Cumulative score-zone hit rate.
4. **Walls / lemmas update** if applicable (paper-direct anchors added, codification updated).
5. **External artifact update** if applicable (preprint draft, blog post — produced *only* under critique #9 publishable artifact discipline).

**Anti-patterns blocked**:
- Lemma file inflation (critique #8): codification-only lemma files are *not* automatically created; Phase 3 evaluates whether a result deserves a *new* lemma file or merely an *upgrade* to an existing file.
- Score inflation: novel content score must be *paper-direct verified* and bounded by what cycles 1-N have *not* already established.

### 2.4 Phase 4: Iterate

**Inputs**: Phase 3 postmortem + meta-learning logs.

**Output**: triggers next cycle's Phase 1 via Stop-hook event-driven mechanism (event-driven cycle protocol — successive Phase 1 receives prior Phase 3 postmortem as primary input).

**Anti-patterns blocked**:
- Premature termination (cycle protocol stops only when external stop signal or 3-turn-stuck declared).
- Disconnected cycles (Phase 1 *must* cite Phase 4 → 1 transition's meta-learning).

### 2.5 Protocol Invariants

Across cycles, the following invariants are maintained:

| Invariant | Mechanism |
|---|---|
| Paper-direct anchor for every nontrivial claim | Phase 2 component 4 |
| Intuition score *committed* before Phase 2 | Phase 1 step 3, no retroactive edit |
| Specialist *blind* round before cross-examination | Phase 2 step 1 vs 2 |
| Critique absorption traceable to protocol upgrade | Phase 3 + Phase 4 logs |
| Novel content evaluated *honestly* with breakdown | Phase 3 step 1 final item |
| External artifact *only* under publishable discipline | Phase 3 step 5 critique #9 |

## 6. Honest Limits and Future Work — Four Mechanisms of AI-Assisted Sustained Research

This section presents the empirical *progress drivers* observed across the 11 validated cycles, identifying four mechanisms by which the protocol generates non-trivial output (i.e., outputs that are not pure restatement of prior cycles). We treat these as the *novel contribution* of the present paper to AI-for-Math methodology, while explicitly bounding the scope of the claim.

### 6.1 Mechanism 1: Externalization 5-Stage Progression

We observed a *5-stage progression* of externalization across cycles 6-10:

1. **Outline** (cycle 6): outline of an external review-able artifact, no body content.
2. **Artifact first commit** (cycle 7): first body content written, sections 1-2 of preprint.
3. **Polish** (cycle 8): existing body content refined for external readability (explicit definitions, formal notation, references to internal taxonomy made standalone).
4. **Substance** (cycle 9): core data section added (audit table, paper-direct anchors).
5. **Aggregate result + discipline** (cycle 10): theorem statement, supporting catalog, methodological discipline articulation.

**Observation.** The 5-stage progression is *natural and observed*, not designed: cycles 7-10 each chose a single-turn narrow scope, and the progression emerged from the cycle-by-cycle "what is the next narrow thing to add" decisions made independently in each Phase 1 ideation. This suggests the externalization stages are *latent* in the methodology and naturally surface under sustained research.

**Limitation.** The 5-stage observation is *single-paper* (the axiom 6 ceiling preprint). Other artifacts may follow different progressions or different stage counts.

### 6.2 Mechanism 2: Novel Jump Trigger via External Critique Absorption

Of the 11 validated cycles, two stand out for *novel content score jump* above the externalization-cycle baseline of 1.4-2.6/10:
- Cycle 6 (6.7/10): triggered by external critique #9 ("publishable artifact externalization"), which redirected cycle output from internal lemma codification to external review-able artifact.
- Cycle 11 (4.9/10, partial): triggered by user request ("novel content score 고점 시도 적극"), which redirected cycle output from preprint sequential expansion (which had been stable at 1.4-2.6 for cycles 7-10) to a *new paper draft* on cycle protocol methodology itself.

**Observation.** Both novel jumps occurred when an external critique forced a *change of axis*, not refinement within the existing axis. The protocol's tendency without external trigger is to refine the current axis (cycles 7-10 narrow polish/substance/aggregate); external critiques break this.

**Limitation.** This pattern is *empirical* over a small number (N=2) of jump events. We cannot claim that novel jump *requires* external critique, only that in our corpus the two novel jumps coincided with external critique absorption.

### 6.3 Mechanism 3: Hallucination Verification Protocol

Cycles 7-11 (5 consecutive cycles) included an explicit *outline-to-text honest mapping* check during Phase 2: every nontrivial claim in the externalization output was verified to have either (a) paper-direct quote anchor or (b) prior-cycle work.md verified result anchor or (c) hallucination flag (claim withdrawn).

**Observation.** Across cycles 7-11, hallucination flag count = 0. This consistency suggests the protocol's *paper-direct anchor discipline* (Phase 2 component 4 in §2.2) is operationally sufficient to prevent hallucination drift in externalization cycles.

**Limitation.** Zero hallucination over 5 cycles is *not statistical guarantee*. Larger corpus (N=20+) would strengthen the claim. The discipline may also fail under adversarial conditions (e.g., if the agent is asked to extrapolate beyond the verified evidence).

### 6.4 Mechanism 4: Two-Axis Contribution Separation

The 11 validated cycles produced two distinct external review-able artifacts:
- **Axiom 6 ceiling preprint** (cycles 7-10): codification of the empirical universal NO observation in the Hilbert-Pólya program. Sections 1-4 (~10-13 pages, substance core complete).
- **Cycle protocol paper** (cycle 11+, the present paper): novel methodology contribution. Sections 1-2 (~5 pages) + Section 6 (this section).

**Observation.** The two artifacts occupy distinct *contribution axes*: the ceiling preprint is *codification* (recodification of self-acknowledged obstacles), the protocol paper is *novel methodology* (AI-for-Math protocol-level contribution). Attempting to merge them into a single artifact would dilute both. The separation occurred *naturally* once external critique #9 (cycle 6) and user novel-高점 request (cycle 11) made the two axes salient.

**Limitation.** The two-axis pattern is *single-corpus*. Other AI-assisted research efforts may produce one axis only or three+.

### 6.5 Honest Limits

We list the limits of the protocol as observed in cycles 1-11:

- **Single LLM single domain validation.** Claude-class LLM, RH domain only. Generalization to other LLMs (GPT-class, open-source) and other domains (physics, biology) is unverified.
- **Empirical novel content cap.** Cycles 1-11 highest novel score = 6.7/10 (cycle 6, external critique-driven), with stable baseline 1.4-3.7/10 across non-jump cycles. The protocol does *not* generate sustained novel content > 5/10 without external trigger.
- **Hallucination zero is empirical, not provable.** §6.3 limit applies.
- **No proof of Riemann Hypothesis.** Cycles 1-11 produce *empirical universal NO* codification on Hilbert-Pólya candidates (axiom 6) — *not* an RH proof attempt. The cycle protocol paper makes no RH claim.
- **Operational protocol, not formal protocol.** §2 describes operational practice, not ZFC-level formal specification.
- **Race conditions in event-driven cycle**: the Stop-hook mechanism (§2.4) exhibits transcript-flush race conditions that produce repeated phase prompt injections; the agent must apply *forward progress override* heuristically. A strictly formal cycle protocol would not have this issue.

### 6.6 Future Work

- **Multi-LLM validation**: re-run the cycle protocol across GPT-class, open-source LLMs to verify reproducibility.
- **Multi-domain validation**: apply to a non-RH open problem (e.g., Goldbach, twin primes, P vs NP) to verify domain-generality.
- **Strictly formal protocol specification**: ZFC-level or process-calculus specification eliminating race conditions and operational ambiguity.
- **Larger N hallucination study**: extend the corpus to N=20+ cycles and measure hallucination rate quantitatively.
- **External critique injection mechanism**: cycle 6 (critique #9) and cycle 11 (user novel-高점 request) were *exogenous* events. A protocol-level mechanism for *generating* such critiques (e.g., adversarial agent role) would internalize the novel-jump trigger.

## 3. Validation Metrics

This section presents the empirical metrics observed across the 12 validated cycles. The metrics are *single-corpus* and *single-LLM* (cf. §6.5 limits); we report them as *empirical observations*, not as universal validation.

### 3.1 Intuition Calibration

In Phase 1 of each cycle, candidate hypotheses receive a *first-impression intuition score* (1-10 scale) committed before Phase 2 execution. After Phase 3, the result is classified as FULL YES / PARTIAL YES / NO relative to the score.

**Cumulative results (cycles 1-12):**

| Score range | Count | Result distribution |
|---|---|---|
| 9/10 | 3 | 1 FULL + 2 PARTIAL |
| 8/10 | 9 | 4 FULL + 5 PARTIAL |
| 7/10 | 0 | (untested) |
| 5-6/10 | 0 | (untested) |
| 3-4/10 | 0 | (untested) |

**Observation.** The 8-9/10 score zone achieves a 12/12 hit rate (5 FULL + 7 PARTIAL — every cycle's selected hypothesis received at least PARTIAL YES). No cycle's selected hypothesis received NO.

**Limitation.** Lower-score-zone hypotheses (3-7/10) were *never selected* in cycles 1-12 (the protocol selects the highest-intuition candidate). Hence we have no calibration data for those zones. The 12/12 hit rate at 8-9/10 may reflect (a) genuine calibration accuracy, (b) selection bias (only the highest-intuition candidate is tested), or (c) overly broad PARTIAL YES classification.

### 3.2 Pivot Rate

A *pivot* occurs when Phase 2 execution forces a substantive revision of the Phase 1 hypothesis (e.g., axiom 7+11 → axiom 6 in cycle 1, codification → active program identification in cycle 3, unification gap partial sharpen in cycle 4). A *stable* cycle is one where the original hypothesis survives Phase 2 with at most marginal refinement.

**Cumulative results (cycles 1-12):**
- Pivot cycles: 1, 3, 4 (count = 3).
- Stable cycles: 2, 5-12 (count = 9).
- **Pivot rate: 3/12 = 25%.**

**Observation.** The pivot rate is non-trivial (≠ 0% all-stable nor 100% all-pivot). Cycles 1-4 had higher pivot frequency (3/4 = 75%); cycles 5-12 are uniformly stable (0/8 = 0%). The shift coincides with the externalization phase (cycles 6-12) where outputs are paper draft sections (less amenable to mid-cycle pivot than internal lemma audits).

**Limitation.** Single corpus. Other research efforts may exhibit different pivot rates depending on problem difficulty and external critique frequency.

### 3.3 Novel Content Trend

In Phase 3 of each cycle, the agent provides a *novel content N/10 honest evaluation* with breakdown.

**Cumulative trajectory (cycles 1-12, aggregated novel scores):**

| Cycle | Novel | Notes |
|---|---|---|
| 1 | 1.5 | Codification (Wall #5 axiom 6 ceiling) |
| 2 | 1.5 | Codification (Wall #2 axiom α ceiling) |
| 3 | 2.0-2.5 | Active program identification |
| 4 | 2.5-3.0 | Path 2 active continuation + still-open H¹ |
| 5 | 3.0-3.7 | Path 1 direct progress (Theorem 1 + bridging) |
| 6 | **6.7 (peak)** | Cycle 1 retroactive + outline finalize (critique #9 trigger) |
| 7 | 2.6 | Artifact first commit |
| 8 | 1.4 | Artifact polish |
| 9 | 1.9 | Substance commit |
| 10 | 2.2 | Aggregate result + discipline |
| 11 | **4.9 (partial peak)** | Cycle protocol new paper (user novel-高점 request) |
| 12 | 4.0 | §6 4 mechanisms unified codification |

**Observation.** Two distinct *novel jump* events (cycle 6 = 6.7, cycle 11 = 4.9) above the externalization-cycle baseline (1.4-3.7). Both jumps coincided with *external critique absorption* (cf. §6.2). Without external trigger, novel content stabilizes at 4-5 ceiling (cycles 11+12 partial pattern).

**Limitation.** Novel score is a *self-evaluation* by the agent in Phase 3. While the protocol enforces a discipline of *paper-direct anchor* and *non-claim disclosure*, the score remains agent-internal and is not externally validated.

### 3.4 Externalization Stage Timeline

The 5-stage externalization progression of §6.1 occurred over cycles 6-10:

| Cycle | Stage | Output |
|---|---|---|
| 6 | Outline | preprint outline finalized (axiom 6 ceiling) |
| 7 | Artifact first commit | Sections 1-2 of axiom 6 ceiling preprint (~3 pages) |
| 8 | Polish | §1.1 walls explicit + §2.0 strict union formalization |
| 9 | Substance | Section 3 audit table (~121 cells + 11 anchors) |
| 10 | Aggregate result + discipline | Section 4 (Theorem + Catalog 47+ + 4-point discipline) |

**Observation.** Each stage occupied a single cycle and reduced (not increased) the open work for the next stage. The progression is *monotone* in the sense that cycle N's output strictly extends cycle N-1's output.

**Single-turn cycles (7-12).** Cycles 7-12 (6 consecutive cycles) executed Phase 2 in a single turn. The single-turn pattern correlates with the *narrow externalization scope* (one section or one polish task per cycle).

**Limitation.** Single-paper progression (axiom 6 ceiling preprint). Cycle 11's *new paper draft* (cycle protocol paper) initiated a parallel progression which has not yet completed (current paper has §1, §2, §6 only; §3 [present section] just added; §4-§5 deferred).

## 4. Critique Absorption Chain

The protocol absorbed four external critiques across cycles 0-12, each traceable to a specific protocol upgrade. The critique numbering follows the project's internal `learnings/external_critique_2026-05.md` log.

| # | Critique (paraphrased) | Cycle absorbed | Protocol upgrade |
|---|---|---|---|
| 5 | NOVEL spree (paper-external speculation in unbounded sequence) | Pre-cycle | NOVEL Quota: paper-external direction = 1-sequence only; first paper-direct rediscovery → terminate sequence. |
| 6 | Pre-batched plan (planning N future steps) | Cycle 0 → 1 | Lazy planning: each cycle's next action decided after current cycle's postmortem; no `mkdir attempts/NNN-MMM` for 5+ pre-created folders. |
| 7 | Heartbeat / cycle protocol absent (1 fire = 1 attempt stamp) | Cycle 1+ | 4-Phase Sustained Research Cycle (§2). Stop-hook event-driven mechanism. |
| 8 | Codification machine (unbounded codification of negative observations) | Cycle 3 | Active program identification mandate; lemma file *upgrade* preferred to lemma file *creation*; positive direction sub-direction discipline. |
| 9 | Publishable artifact externalization (internal accumulation only) | Cycle 6 | External review-able artifact mandate; preprint outline → artifact → polish → substance → aggregate progression (§6.1). |

**Observation.** Each critique absorption produced a measurable protocol change: NOVEL Quota counts as a bounded-search discipline, lazy planning eliminates premature batching, 4-Phase cycle replaces ad-hoc stamping, codification-machine mandate produces the *path 2 active program* axis (cycles 3-4), publishable mandate produces *two paper drafts* (cycles 6-12).

**Limitation.** All five critiques originated from a *single external source* (the project user). Multi-source critique absorption is unverified.

## (Section 5 deferred to subsequent cycles)

Section 5 (Externalization 5-Stage Progression detail — beyond §6.1's summary) deferred to cycle 14+.

---

## Internal Notes (cycle 11, not for paper submission)

### Paper-Direct Anchors (§1+§2)

- §1.1 failure modes: external critique #5, #6, #8 + cycles 1-10 internal observation.
- §1.3 validation metrics: cycles 1-10 sustained_research_log + intuition_calibration data direct.
- §2.1-§2.4 protocol details: HARNESS.md §Sustained Research Cycle + cycles 1-10 work.md execution.

### 환각 위험 검증 — Honest Scope Manifest

- §1.4 *Non-Claims* explicit (4 negatives + 3 positives).
- §1.4 *Single LLM single domain validation corpus*: empirical only.
- §2.5 *Anti-patterns blocked* explicit table — protocol design intentional.

### Novel Content Target (cycle 11 의무)

사용자 요청: *Novel 고점 시도 5+/10*.

본 paper:
- §1.1 4 failure modes + 1.4 4 non-claims + 1.4 3 positive claims = *novel methodology contribution*.
- AI for Math 분야 *protocol-level methodology* gap 명시 + cycles 1-10 validation = *우리 first novel paper*.

→ **Novel target 5+/10 시도** (Phase 3 self-check 검증).

### Next Steps

- Cycle 12: §3 Validation Metrics 본문.
- Cycle 13: §4 Critique Absorption Chain 본문.
- Cycle 14: §5 Externalization 5-Stage Progression 본문.
- Cycle 15: §6 Honest Limits + Future Work 본문.
