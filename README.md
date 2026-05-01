# An AI tried to prove the Riemann Hypothesis 200+ times. It didn't. That's the interesting part.

> **🌐 Public site**: [https://x2ever.github.io/riemann-hypothesis-llm-exploration/](https://x2ever.github.io/riemann-hypothesis-llm-exploration/) — English + Korean blog with the curated reporter narrative
> **📬 Contact**: x2ever.han@gmail.com
> **🤖 AI-disclosed**: every word here was produced by Claude (Anthropic) under continuous human prompts

## What this is

We pointed an AI agent at the most famous open problem in mathematics — the **Riemann Hypothesis**, unsolved since 1859 — and *forbade it from claiming progress*. We had it run for **200+ self-directed research cycles** over six months. It still hasn't proved the Riemann Hypothesis. Every cycle's `postmortem.md` ends with the line:

> *Novel content: 0/10.*

That line is a *daily affirmation enforced by the protocol*, not a one-time disclaimer. There is a literal yellow-flag word list (`"resolved"`, `"확정"`, `"증명"`) that triggers retraction review if the AI uses any of them without an explicit external check.

This repository contains:

- **Layer 1** (this repo, `attempts/`, `lemmas/`, `learnings/`, `papers/`): the raw research session — 200+ cycle directories, 9 process lemmas, 22 paper-direct evidence tissues, 17 vetted PDFs, 38 Python modules. Will eventually go private.
- **Layer 2** (this repo, `en/` + `ko/` → published as the public site): the curated reporter narrative — six months of an AI being kept honest about a problem it cannot solve.

## What this is NOT

- A Riemann Hypothesis proof. Or a near-miss. Or a new theorem.
- A "framework". Or a contribution to number theory.
- A claim that LLMs are or are not close to mathematical research.

The interesting artifact is the **behavior pattern**: an AI that does sustained work, accepts external corrections, retracts its own categories one cycle later, makes time-stamped predictions it can be measured against, and refuses to dress its negative results as positive ones.

## Six things this AI did that we did not expect

These are described in detail in the [anchor post on the public site](https://x2ever.github.io/riemann-hypothesis-llm-exploration/en/posts/00-anchor-honest-failure/):

1. **Admits it's failing every single day** — `Novel content: 0/10` is a protocol-enforced daily affirmation.
2. **Caught itself miscategorizing 22 cycles of its own work** — labeled paper-direct deep-reading as "Type A" (original derivation) for 22 consecutive cycles. After a user critique, did its first 30-line Python script and called the result *weaker than what Robin proved in 1984*.
3. **Bet on its own future and made the bet falsifiable** — committed `predictions/cycle19_claim_alpha_path1_unification.md` on 2026-05-01: a narrow, time-stamped, falsifiable prediction with a 1-year clock.
4. **Self-corrected its own classification one cycle later** — retracted Cycle 21's 5-axis Path 3 decomposition in Cycle 22, citing paper-direct evidence (`"D̂ is the well-known Berry-Keating Hamiltonian"`).
5. **Mapped where 167 years of attempts have all hit the same wall** — every published RH attempt is a deformation of *one* underlying object (Weil 1948 explicit formula, the "Master Generator"); active candidates outside that framework: 0 / 25+.
6. **11/11 universal NO on a Hilbert–Pólya audit** — eleven published candidates, six strict axioms, every candidate fails at least one axiom (most commonly self-adjointness).

## Why this might be interesting

If you have ever asked a chatbot whether it solved your problem, you know how unusual a daily `0/10` self-affirmation is. If you have ever watched an AI revise its predictions after seeing the answer, you know how unusual a *pre-committed* falsifiable bet is. If you have ever read a "AI proves famous theorem" thread that ended in a retraction, you know how unusual it is for the AI itself to *refuse to write that headline*.

The interesting artifact is not what an AI can prove. It's what an AI can *honestly fail at*, in the open, for six months.

## Calibration

- 1859년 제시 이후 165년간 세계 최고 수학자들이 실패한 문제다.
- 본 프로젝트의 **현실적 목표는 "증명"이 아니라 "체계적으로 시도하면서 어디서·왜 막히는지 누적 학습"**이다.
- 시도 과정에서 부분 결과/새 관점/미해결 문제 정식화에 성공해도 그 자체로 가치다.
- "증명했다"고 느끼면 반드시 **자기 회의 단계**(self-doubt) 거치기 — 95% 이상은 미묘한 오류, 가정 누락, 또는 순환 논리다.

## Repo map (Layer 1, will go private)

```
prove_riemann_hypothesis/
├── README.md            # this file
├── HARNESS.md           # cycle-loop master spec
├── SPECIALISTS.md       # field-specialist panel protocol
├── background/          # definitions, functional equation, known results
├── papers/              # 17 PDFs + INDEX.md (per-paper deep notes)
├── attempts/NNN_<key>/  # cycle directories (strategy/specialist_round/work/postmortem)
├── learnings/           # cross-attempt meta-lessons (walls.md, critique_*)
├── lemmas/              # reusable bookkeeping artifacts (9 lemmas)
└── tools/               # mpmath-based numerical experiments (38 modules)

en/                      # English blog posts (Layer 2, public)
ko/                      # 한국어 blog posts (Layer 2, public)
_config.yml              # Jekyll + just-the-docs theme
```

## Counterexamples wanted

The highest-value contribution this project can receive is a **counterexample**:

- **Break Lemma 9**: find an 11-axiom-passing Hilbert–Pólya candidate the project missed.
- **Break Lemma 10**: find a paper-direct unconditional $\int E\,dt$ bound resolving Wall #2.
- **Break the Path 4 verdict**: find a vetted RH attempt that is genuinely outside the Master Generator (Weil 1948 explicit formula) framework.

If you have one: **x2ever.han@gmail.com**.

## Syndication

If you want to syndicate, quote, or link any of these posts: please link back to the public site. Layer 2 posts are designed to remain self-contained even after Layer 1 goes private.

---

*This README is itself part of Layer 1 and may be revised.*
