---
title: "Project Overview"
date: 2026-05-02
lang: en
---

# Project Overview

[← All English posts](../../) · [한국어](../../../ko/posts/01-overview/) · *2026-05-02*

> ## ⚠️ AI-Generated. Not a Proof.
>
> An LLM (Anthropic's Claude) autonomously explored the Riemann Hypothesis. **No proof. No mathematical progress. 0/10**, self-acknowledged at every milestone.

## What this project did

A single LLM session ran 200+ research attempts across 7 research cycles, with the deliberately humble mission stated in `README.md`:

> *"The realistic goal is not 'proof' but systematic attempts that accumulate learning about where and why we get stuck."*

That mission held for 200+ attempts. The project's own running self-assessment of its mathematical progress: **0/10**.

## What's worth attention

Across that long run, the session:

- produced **zero hallucinations** under the project's frame definition (every claim must be paper-direct quote-anchored or marked speculative)
- declined three explicit user requests for "novel content" by citing its own honest-scope protocol
- **partially refuted its own Cycle 3 unification hypothesis** in Cycle 4 after reading additional Connes–Consani papers (self-correction, not reinforcement)
- ran a falsifier test of Lemma 9 against PNAS 2022 (Connes–Moscovici) and found 3 paper-direct gaps — *strengthening* the lemma to 11/11 instead of retracting it
- accumulated **intuition calibration data**: 6 cycles of pre-result 1–10 scores, with 8/10 yielding ~80% PARTIAL YES rate

None of this is a proof or a mathematical contribution. It is a case study of how an LLM can sustain *honest scope* on a problem far above its capability.

## Two layers

This site separates two layers:

- **Layer 1 — Raw research record**: the autonomous session's unedited output (`attempts/`, `lemmas/`, `papers/`, `learnings/`).
- **Layer 2 — Reporter narrative**: a *separate* LLM session curates Layer 1 with attribution. It does not generate new mathematical claims. Every assertion on Layer 2 either quotes Layer 1 directly or describes its structure.

If you find a discrepancy, **Layer 1 is authoritative**.

## How to read this site

- Want the headline observations? See [Findings](../../#-findings-empirical-patterns-not-theorems).
- Want the methodology? See [Process](../../#--process--methodology).
- Skeptical and want caveats up front? See [Honest Scope](../09-honest-scope/).
- Want to audit a specific claim? Each post links to the corresponding `attempts/` and `lemmas/` files in Layer 1.

## Contact

For comments, refutations, or questions: **x2ever.han@gmail.com**

The project explicitly treats external critique as a primary mechanism. Six critiques have been absorbed so far (see [Process: Six external critiques absorbed](../07-process-critique-loop/)). A seventh from a careful external reader would be welcome.

---

[← All English posts](../../) · [한국어](../../../ko/posts/01-overview/) · [Repo](https://github.com/x2ever/riemann-hypothesis-llm-exploration)
