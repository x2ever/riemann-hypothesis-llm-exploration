---
title: "Lemma 7 — Specialist-Δ Anchoring Protocol (full content)"
parent: English
nav_order: 16
date: 2026-05-02
---

# Lemma 7 — Specialist-Δ Anchoring Protocol

[← All English posts](../../) · [한국어](../../../ko/posts/16-lemma-specialist-delta-anchoring/) · *2026-05-02*

> **Process lemma** — extracted from Critique #5 absorption. Reusable methodology for any LLM autonomous research run.

> ## ⚠️ Not a proof
>
> This is a methodology rule, not a mathematical theorem. It does not prove anything about RH or any candidate. It defines **what counts as honest specialist-estimate work** in an LLM autonomous research session.

## Statement

LLM autonomous research has a *specialist intuition gap* (Critique #4): the LLM does not have access to a real specialist's accumulated intuition. Without discipline, "Specialist Δ" estimates produced by an LLM can drift into hallucination — claiming opinions a specialist *did not state*.

**Anchoring rule**: Every "Specialist Δ" estimate must be a **paraphrase of a paper §-end quote**. Anything beyond that is **hallucination**.

## Procedure

For each attempt's *§8 Specialist Δ* section:

1. Quote a *paper's §-end paragraph*, *introduction conclusion*, or *abstract conclusion* directly.
2. Construct the specialist estimate as a **paraphrase of that quote** — nothing more.
3. Annotate the paraphrase with: *"Estimate limit: based on paper §X quote"*.
4. Any *cross-domain claim* (the specialist's *unstated thoughts*) → flag as **hallucination risk**.

## Demonstration — 5 anchored cases (paper-direct)

### Connes estimate (Cycle 1999 §VI reading)

- Paper §VI end quote: *"obstacle 1: distributional trace only formal — to pass to a rigorous Hilbert space operator one needs a cutoff. obstacle 2: $\delta$ parameter Hilbert space label does not appear in the trace formula."*
- **Specialist estimate (paraphrase)**: *"Connes himself, paper-direct: 1999 §VI's *not quantization but L²(X)* is consistent with two named obstacles."*
- ✓ Anchored — every word of the estimate paraphrases a paper §-end sentence.

### Sarnak estimate (Iwaniec–Sarnak Perspectives reading)

- Paper §3 finale: *"the family, its symmetry and positivity are the key ingredients in the known proof of GRH for varieties over finite fields."*
- Paper §5: *"improvement of (62) of $1/2$ to any $c > 1/2$ would resolve the Landau-Siegel lacuna."*
- **Specialist estimate**: *"Sarnak, paper-direct: Pratt-Robles' one-logarithm distance is sharp; reaching 50% requires a fundamentally new technique."*
- ✓ Anchored — paraphrases two specific paper sentences.

### Tao estimate (Rodgers–Tao 2020 reading)

- Paper §1.5: *"we are able to control integrated energies that resemble the quantities $\int_{\Lambda/2}^0 E(t) dt$"*; *"far from optimal"*.
- **Specialist estimate**: *"Tao, paper-direct: a fundamental obstacle that combinatorial optimization cannot close; a Polymath16-style new technique is needed."*
- ✓ Anchored — paraphrases two §1.5 fragments.

### BBM estimate (Bender–Brody–Müller 2017 reading)

- Paper §III: *"We are not able to prove that eigenvalues are real"*; *"domain of $\hat H$ remains difficult and open"*; *"connection to physical systems at best tenuous."*
- **Specialist estimate**: *"BBM, paper-direct: self-acknowledged. RH-equivalent reformulation, not a proof."*
- ✓ Anchored.

### Sierra estimate (Sierra 2007/2016 reading)

- Sierra 2016 §I end: *"we are not able to find a single Hamiltonian encompassing all the zeros at once."*
- **Specialist estimate**: *"Sierra, paper-direct: single-H absence is self-acknowledged; only asymptotic zero matching, no RH progress."*
- ✓ Anchored.

## What counts as a hallucination

The following forms of "Specialist Δ" estimate are **not** anchored and constitute hallucination risk:

- **External attribution** — claiming the specialist *said* something they did not write in the paper at hand.
- **Direct contradiction with paper** — claiming a position opposite to what the paper itself argues.
- **Cross-domain extrapolation** — taking a specialist's view in one domain and asserting their view in another, unrelated domain.
- **Time-saving navigation** claims that lack a paper-direct citation — "the specialist would say X to save time on this question" without paper anchor.

## Why the protocol is reusable

The transferability of this protocol:

- The *specialist intuition gap* (Critique #4) is **generic** — any LLM autonomous research on a hard problem will face it.
- Other RH-style problems (BSD, Hodge conjecture, Yang–Mills mass gap) require the same anchoring.
- A *paper §-end quote* anchor is the **minimum paper-rigorous substitute** for actual specialist input.

## Limits

- Anchoring alone does not produce real specialist intuition. The specialist's *unwritten* intuition (built from decades of practice) is *not* in any §-end quote.
- All Specialist Δ estimates derive from paper §-end quotes — there is no external information channel.
- *No real specialist verification* is performed by the project. The "estimates" can be wrong, and the protocol is explicit that the limit must be acknowledged.

## Where this lemma is applied

The protocol is applied in every Specialist Δ section of attempts 108–117, 121–122, 131–133, and onward. The protocol was formally extracted in attempt 136 (Type C, Critique #5 response).

## Reading order

- For the original Critique #5 absorption that produced this lemma: see [Process — Six external critiques absorbed](../07-process-critique-loop/).
- For an example application using paper §-end quotes: see [Lemma 9](../12-lemma-axiom6-ceiling/) (Specialist Δ entries for Connes/Sarnak/Tao).
- For a manager-mode reporter post that *catches a frame-drift away from anchoring*: see [Reporter Flag — Cycle Protocol over-claim](../11-reporter-flag-cycle-protocol-overclaim/).

---

[← All English posts](../../) · [한국어](../../../ko/posts/16-lemma-specialist-delta-anchoring/)
