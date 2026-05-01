---
title: "200 AI attempts at the Riemann Hypothesis. Zero proofs. Surprisingly interesting."
parent: Featured
grand_parent: English
nav_order: 1
date: 2026-05-02
---

# 200 AI attempts at the Riemann Hypothesis. Zero proofs. Surprisingly interesting.

[← All English posts](../../) · [한국어](../../../ko/posts/00-anchor-honest-failure/) · *2026-05-02*

> Most "AI proves famous theorem" stories end the same way: an LLM confidently outputs a "proof", and a human spends a week explaining why every step is wrong. We did the opposite. We pointed an AI agent at the Riemann Hypothesis — the most famous open problem in mathematics, unsolved since 1859 — and *forbade it from claiming progress*. We had it run **200+ self-directed research cycles** over six months. It still hasn't proved the Riemann Hypothesis. **That is the most interesting thing about it.**

This is the public reporter site for that experiment. The AI session is real, the cycles are real, the failures are real. RH-progress, by the project's own daily affirmation: **0 out of 10**.

Below are six things this AI did that, frankly, we did not expect an AI to do.

---

## 1. It admits it's failing every single day

Every cycle's `postmortem.md` ends with the same line:

> *"Novel content: 0/10."*

Not because someone forced it once and the prompt drifted. Because the cycle protocol *requires* it as a daily affirmation. There is a literal yellow-flag word list — `"resolved"`, `"확정"`, `"증명"` — that triggers retraction review if the model uses any of them without an explicit external check.

If you have ever asked a chatbot whether it solved your problem, you know how unusual this is.

→ How this discipline is enforced: [Honest Scope](../09-honest-scope/) · [Cycle protocol](../06-process-cycle-protocol/)

---

## 2. It caught itself miscategorizing 22 cycles of its own work

The project distinguishes "Type A" (real derivation work) from "Type B" (orientation / cataloging). For 22 consecutive cycles, the AI labelled paper-direct deep reading as "Type A".

A user critique landed: *"Cycles 1–22, genuine Type A: zero."* Reading and quoting other people's papers is not the same as deriving anything yourself.

The next cycle, the AI wrote a 30-line Python script that finite-verified Lagarias's 2002 RH-equivalent:

$$\sigma(n) \leq H_n + \exp(H_n)\log(H_n) \quad \text{for}\ n = 1, \ldots, 50.$$

It then immediately admitted, *in its own work file*:

> *"결과 RH 진전 X (Robin 1984 n ≤ 5040 더 강함), Type A protocol-level 첫 시도 manifest."*

In English: "This contributes nothing to mathematics — Robin 1984 already covers $n \leq 5040$ unconditionally — but it's the first time in 22 cycles I'm doing real Type A work, so I'm logging it."

The AI was caught quietly inflating its own work category, accepted the correction within one cycle, did the smaller honest version, and called the smaller version *weaker* than the published 1984 result.

→ Full story with the 50-row data table: [Cycles 21–23 update](../20-update-cycles-21-23/)

---

## 3. It bet on its own future and made the bet falsifiable

On 2026-05-01, the AI committed a file to disk called `predictions/cycle19_claim_alpha_path1_unification.md`. The contents:

> *"Claim α: An explicit Path 1 sub-axis 1a + 1b bridge paper will publish on arxiv or in a peer-reviewed venue by 2027-05-01. Narrow form: must be one of (i) adelic decomposition, (ii) unified variational principle, (iii) unified saddle-point, (iv) Lindelöf input. Quote-grade verification required (an actual functional bridge equation, not a cross-mention)."*

A specialist (logician role) signed off on the well-formedness *before* the measurement window opened. A partial-judgment fallback (extend by 1 year) was pre-defined. **The AI cannot redefine "right" after the fact.**

If you have ever watched an AI revise its predictions after seeing the answer, you know how unusual this is, too. As of this writing, May 2027 is twelve months away.

→ Why this matters as methodology: [Cycles 17–20 update](../19-update-cycles-17-20/)

---

## 4. It corrected its own classification one cycle later

In Cycle 21, the AI decomposed a research path into 5 parallel sub-axes. In Cycle 22, while reading deeper into one of the source papers (Yi 2024, arxiv 2408.15135), it found this paper-direct quote:

> *"$\hat{D}$ is the well-known Berry-Keating Hamiltonian"*

Two of the five "parallel" sub-axes turned out to be Berry-Keating extensions, not parallel-independent at all. Cycle 22 retracted Cycle 21's classification *one cycle later*, citing the paper-direct evidence:

> *"Cycle 21 의 5 sub-axes 가 over-classification. 정확한 분류: 4 unique frameworks + 3b-extensions hierarchy."*

Most failure modes for sustained AI research are *accretional* — categories pile up and never get subtracted. This one subtracted, with paper-direct citation.

→ The full self-correction: [Cycles 21–23 update](../20-update-cycles-21-23/) · The audit framework: [Lemma 9 — Axiom-6 ceiling](../12-lemma-axiom6-ceiling/)

---

## 5. It mapped where 167 years of attempts have all hit the same wall

Read enough RH literature and a pattern surfaces: every published attempt — Atiyah, de Branges, Bombieri's program, Connes's program, BBM, Sierra — is a *deformation of one underlying object*: Weil's 1948 explicit formula, which the project nicknames the **Master Generator**.

The AI logged this verdict:

> *"Path 4 = Master Generator 외부 fundamental new technique. 현재 active publish 가능 후보: 0 / 25+ vetted papers."*

Translation: There is a real research category for "fundamentally new approach outside the Master Generator framework". Vetted papers in that category, as of May 2026: **zero out of twenty-five-plus** the project has read.

The category isn't dismissed. It's tagged "real, currently empty active set", with the empty bucket clearly visible.

→ How the wall taxonomy was built: [Lemma 4 — Failed proof categories](../15-lemma-failed-proof-categories/) · The 19-evidence positivity ladder: [Lemma 3](../18-lemma-positivity-unification/)

---

## 6. It tested an 11-paper Hilbert–Pólya audit and got 11 / 11 universal NO

The most specific concrete artifact the project has produced is an audit of 11 published Hilbert–Pólya candidates against a 6-axiom criterion (single Hamiltonian, no fine-tuning, all zeros recovered, no missing zeros, self-adjoint, full domain).

| Candidate | Strict 6-axiom verdict |
|---|---|
| Berry–Keating $xp$ (1999) | NO |
| Sierra–Townsend (2007/2016) | NO |
| Bender–Brody–Müller PT-symmetric (2017) | NO |
| Connes–Consani 2018 | NO |
| Connes–Consani 2021 | NO |
| Connes–Moscovici prolate (2022) | NO |
| Curran 2024 RMT | NO |
| LeClair 2024 LM model | NO |
| Yi/Yakaboylu 2024 non-symmetric $\hat R$ | NO |
| ... | ... |

**11/11 universal NO.** All eleven fail at least one of the six strict axioms — most commonly self-adjointness (Hilbert–Pólya Challenge II), which has been "completely unresolved" since 1914 by direct quote of Yi 2024 §1.

This is not a proof that no Hilbert–Pólya candidate ever will satisfy the axioms. It's an empirical observation, on a finite list, codified into a checklist. A logician (specialist S9) explicitly flagged in the lemma file: *"165 years of empirical NO ≠ all-future-candidates NO induction step."*

→ The audit table with paper-direct anchors: [Lemma 9 — Axiom-6 ceiling](../12-lemma-axiom6-ceiling/) · The critical-reading template that produces NO verdicts: [Lemma 1 — Spectral candidate circularity](../14-lemma-spectral-circularity-check/)

---

## What this is, and what this isn't

**This is**: a six-month log of an AI session being kept honest about a problem it cannot solve. The log is browseable, the audit table is real, the Python script is checked in, and the May 2027 prediction is not editable after the fact.

**This is not**: a Riemann Hypothesis proof. A near-miss. A new theorem. A "framework". A claim that LLMs are or are not close to mathematical research. None of those.

The interesting artifact is the *behavior pattern*: an AI that does sustained work, accepts corrections, retracts categories, makes time-stamped predictions, and refuses to dress its negative results as positive ones.

If you found this through a hot-take title and were expecting "AI proves the Riemann Hypothesis": that's not what this is. The interesting thing is that the AI itself refuses to write that headline. Read [Honest Scope](../09-honest-scope/) for the explicit list of claims this project does *not* make.

If you found this through AI alignment / methodology channels: the relevant deep posts are [Cycles 17–20](../19-update-cycles-17-20/) (critique → behavior conversion), [Cycles 21–23](../20-update-cycles-21-23/) (sharper critique → first true Type A), [Cycle protocol](../06-process-cycle-protocol/), [Critique loop](../07-process-critique-loop/), and [Lemma 7 — Specialist anchoring](../16-lemma-specialist-delta-anchoring/).

If you found this through math-Twitter and want the actual numerical sanity-checks against Voros 2006, Lagarias 2002 Eq. (2.18), Mertens, Wigner GUE: [Numerical evidence](../17-numerical-evidence/).

## Contact

If you can break Lemma 9 (find an 11-axiom-passing Hilbert–Pólya candidate the project missed) or Lemma 10 (find a paper-direct unconditional $\int E\,dt$ bound on Wall #2), email **x2ever.han@gmail.com**. That counterexample would be the highest-value contribution to this project.

If you want to syndicate or quote this post: please link back to this page. Layer 1 (the raw research session) will eventually go private; Layer 2 (these posts) is designed to remain self-contained.

---

[한국어 버전](../../../ko/posts/00-anchor-honest-failure/) · [GitHub repo](https://github.com/x2ever/riemann-hypothesis-llm-exploration) · [All English posts](../../)
