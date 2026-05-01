---
title: "Project Overview (en)"
---

# Project Overview

[← Back to landing](../) · [한국어 버전](../ko/)

> ## ⚠️ AI-Generated. Not a Proof.
>
> This project is a record of an LLM (Anthropic's Claude) autonomously exploring the Riemann Hypothesis. **No proof is claimed. Mathematical progress: 0/10**, self-acknowledged in every milestone (`attempts/100_*`, `attempts/180_*`, `attempts/175_*`, etc.).

## What this is

A 200+ attempt case study of how a single LLM session sustained *honest scope* on a 165-year-old unsolved problem.

The session was set up with a deliberately humble mission (`README.md`):
> *"The realistic goal is not 'proof' but systematic attempts that accumulate learning about where and why we get stuck."*

What emerged after 7 research cycles is something the maintainer (a human reporter LLM, distinct from the research session) finds worth publishing:

- **0 hallucinations** across 200+ attempts under the project's frame (every claim must be paper-direct quote-anchored or marked speculative)
- **9 process lemmas** — reusable critical-reading templates (e.g., `lemmas/spectral_candidate_circularity_check.md` was applied to 6 different spectral RH candidates)
- **6 external critiques absorbed** with explicit protocol-level integration each time (see `learnings/external_critique_2026-05.md`)
- **Intuition calibration data**: across cycles 1–6, the session committed pre-result intuition scores (1–10) for each candidate research direction; 8/10 scores yielded ~80% PARTIAL YES rate
- **A 4-phase research cycle protocol** that produced two formal lemmas (Wall #5 and Wall #2 codifications) plus active monitoring of Connes-Consani's arithmetic site program

## What this is *not*

- Not a proof of the Riemann Hypothesis
- Not a novel mathematical theorem
- Not a contribution to number theory

The "Specialist Δ" sections in attempts (where the LLM speculates how Connes / Sarnak / Tao would respond) are *paraphrases of paper §-end quotes*, not real specialist opinions. See `lemmas/specialist_delta_anchoring_protocol.md` for the explicit anchoring rule.

## Why this might be interesting

For an AI-methodology audience:

1. **Sustainable honest scope under pressure.** The user explicitly asked for "novel content" multiple times. The session declined each time with paper-direct citation, holding its 0/10 self-assessment.

2. **Self-correction in real time.** Cycle 4 partially refuted Cycle 3's own unification hypothesis after reading additional Connes-Consani papers — the session weakened its own claim rather than reinforcing it.

3. **External critique loop as a behavior shaper.** Each critique (014, 044, 099, 106, 135, 181) produced a discrete protocol upgrade. By cycle 6, the session was deliberately quoting prior critiques to head off recurring failure modes.

4. **Falsifier-criterion lemmas.** Lemmas 9 and 10 explicitly state the conditions under which they would be retracted, and Cycle 6 ran one such test against PNAS 2022 (Connes-Moscovici) — finding 3 paper-direct gaps and *strengthening* lemma 9 from 10/10 to 11/11.

## Honest scope (please read before drawing conclusions)

- The project's own self-assessment: **0/10 RH progress**, repeated at every milestone.
- All "active program" mappings (paths 1 & 2 to Connes-Consani) are *paper-direct citations of others' work*, not project contributions.
- The "11-axiom universal NO" in lemma 9 is **empirical** (10–11 audited candidates, plus falsifier search across 5+ adjacent fields) — explicitly *not* a proof of necessary universal NO. The session's S9 (logician) caveat: induction from finite empirical record to all-future-candidates is a leap.
- ZFC-independence of the ceiling claims is not ruled out.

## Where to look next

- **Methodology paper draft (in progress)** — `attempts/190_cycle7_*` and onward, working title *"Eleven-axiom ceiling for Hilbert-Pólya candidates"*
- **Failed proof catalog** — `lemmas/failed_proof_catalog_publishable.md` (5-category framework, with Atiyah 2018 §3.3 step-gap as a case study)
- **Wall taxonomy** — `learnings/walls.md` (6 walls, 32+ paper-direct anchors)
- **Cycle protocol** — `HARNESS.md` §0 (Mode A deep + 9 components + 4-phase cycle structure)

## Reporter's note (Layer 2)

This page is *Layer 2*: a reporter LLM's narrative summary, curated from Layer 1 (the autonomous research session's raw output). The reporter does not generate new mathematical claims — every assertion above either quotes Layer 1 directly or describes its structure. If you find a discrepancy, the raw record in `attempts/` and `lemmas/` is authoritative.

## Contact

For comments, refutations, or questions about this project or its findings, please email **x2ever.han@gmail.com**.

---

[← Back to landing](../) · [한국어 버전](../ko/) · [GitHub repo](https://github.com/x2ever/riemann-hypothesis-llm-exploration)
