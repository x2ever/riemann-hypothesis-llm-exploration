---
title: "Finding 1: An 11/11 axiom-6 ceiling across Hilbert-Pólya candidates"
parent: English
nav_order: 2
date: 2026-05-02
---

# Finding 1: An 11/11 axiom-6 ceiling across Hilbert–Pólya candidates

[← All English posts](../../) · [한국어](../../../ko/posts/02-finding-axiom6-ceiling/) · *2026-05-02*

> **Empirical observation, not a theorem.** No proof of RH. Universal NO is *empirical*, not *necessary*. ZFC-independence not ruled out. Falsifier explicit.

## Statement

Across **11 paper-direct Hilbert–Pólya–style spectral candidates** audited so far, **none satisfies axiom 6 strict** — defined (by 4-specialist consensus) as:

> A single self-adjoint operator on a fixed Hilbert space, capturing all ζ non-trivial zeros bijectively, with **no fine-tuning parameter**.

Source: `lemmas/lemma1_axiom6_ceiling.md`.

## The 11 audited candidates

| # | Candidate | axiom 6 strict | Paper-direct anchor |
|---|---|---|---|
| 1 | BBM 2017 (Bender–Brody–Müller) | NO | "We are not yet able to prove eigenvalues real" + boundary cond. ψ_z(0) = -ζ(z) per-zero circular |
| 2 | Sierra §III xp (Berry–Keating type) | NO | continuous spectrum, no point spectrum |
| 3 | Sierra §V H_I | NO | self-adjoint via parameter ϑ ∈ [0, 2π) — fine-tune; "not able to find single H encompassing all zeros at once" |
| 4 | Sierra 2007 H_2 | NO | deficiency indices (1,1), self-adjoint *family* parameterized by 1×1 unitary |
| 5 | Connes–Consani 2021 Θ(λ, k) | NO | special λ values *only*, 31 zeros 10⁻⁵⁰ random-match probability — *not all zeros* |
| 6 | Connes 1999 §VI/VII | NO | "unnatural parameter δ" — δ-family, not unique |
| 7 | Lagarias §8 (1) hypothetical | NO | λ = s² − 1/4 = −γ²+iγ complex (paper §8 self-acknowledged hypothetical) |
| 8 | Berry–Keating 1999 H = xp | NO | "no concrete proposal realizing all conditions" (Sierra 2007 §I quote) |
| 9 | Sierra 2007 §VI ζ_H Jost | NO | M2 family of (a, b) potentials → many candidates |
| 10 | Connes 1999 §III (ℋ_χ, D_χ) | NO | "δ > 1 Sobolev exponent — *unnatural*" — δ-family |
| 11 | Connes–Moscovici PNAS 2022 (UV prolate) | NO | UV asymptotic only (not exact match), λ ∈ {1, √2} fine-tune, deficiency (4,4) |

## How the 4-specialist consensus on "axiom 6 strict" was built

The lemma defines strict YES as agreement across 4 viewpoints:

- **NCG (S3)**: single self-adjoint D on fixed H, all ζ-zeros ↔ Sp(D) bijective, no fine-tune. Falsified if any ζ-zero missing.
- **Quantum physics (S6)**: single PT-symmetric H, *unbroken* PT phase, biorthogonal complete eigenbasis. Falsified by broken PT or fine-tune.
- **Analytic (S1)**: a single mollifier-method transformation capturing all zeros. Falsified by mollifier-family (Pratt–Robles 50% limit).
- **Logician (S9)**: ZFC-provable *"∃ unique H : Sp(H) = ζ-zeros imag part"*. Falsified by existence-without-uniqueness, or ZFC-independence.

Common essence: *no fine-tuning + simultaneous capture of all zeros*.

## The strongest test the lemma underwent (Cycle 6)

The lemma declares its own falsifier criterion (3 conditions). Cycle 6 ran an explicit test against **Connes–Moscovici PNAS 2022** ("UV prolate spectrum matches the zeros of zeta"). Three paper-direct gaps were identified:

1. **UV asymptotic only** — agreement is in a limit, not exact spectrum match
2. **Fine-tuning** — λ ∈ {1, √2} parameter values
3. **Deficiency indices (4, 4)** — self-adjoint extension is a 4-parameter family, not single H

So PNAS 2022 fails axiom 6 strict. The lemma is *strengthened* (10/10 → 11/11), not retracted.

## What this is *not*

- **Not a proof of necessary universal NO.** From the lemma's `Status` block:
  > *"Necessary universal NO 미증명 — S9 logician 경고: 165 years empirical NO ≠ all-future-candidates NO. Induction is a leap."*
- **Not RH progress.** The lemma's `Caveats` explicitly says: *"RH 진전 X — RH 의 *언어 변경* (Cut 6 위반 회피, 본 lemma 는 *증명 시도 X*, *empirical record 만*)"*.
- **Not closed under ZFC analysis.** RH itself is Π_1 (Lagarias 2002); the ceiling's logical strength is undetermined.

## Why this might still be useful

The lemma is a **structured checklist** future spectral candidates can be tested against systematically. Specifically the falsifier criterion is explicit:

> *Falsifier (lemma 폐기 조건): 어떤 paper-direct candidate 가 axiom 6 strict YES 시 즉시 폐기. 검증 절차:*
> *1. Single H on fixed Hilbert space — paper-direct quote.*
> *2. 모든 ζ-zeros ↔ Sp(H) bijective — paper-direct verification.*
> *3. Fine-tuning parameter 부재 — paper-direct quote 또는 explicit 정의.*

If a new candidate ever passes all three, the lemma retracts. That is the discipline.

## Audit trail (Layer 1)

- `lemmas/lemma1_axiom6_ceiling.md` — the lemma itself with full audit table
- `attempts/184_cycle1_*` — Cycle 1 (lemma generation)
- `attempts/189_cycle6_*` — Cycle 6 (PNAS 2022 falsifier test)
- `attempts/010_*`, `109_*`, `110_*`, `111_*`, `117_*`, `133_*`, `178_*`, `182_*`, `183_*` — per-candidate paper-direct readings

## Refuting this finding

If you have a paper-direct candidate that strict-passes axiom 6 — please email **x2ever.han@gmail.com**. The lemma is genuinely falsifiable.

---

[← All English posts](../../) · [한국어](../../../ko/posts/02-finding-axiom6-ceiling/) · [Next: Finding 2 →](../03-finding-wall2-bound/)
