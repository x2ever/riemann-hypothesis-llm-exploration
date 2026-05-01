---
title: "Finding 4: Atiyah 2018 §3.3 paper-direct step gap"
parent: 한국어
nav_order: 5
date: 2026-05-02
---

# Finding 4: Atiyah 2018 §3.3 paper-direct step gap

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/05-finding-atiyah-step-gap/) · *2026-05-02*

> 본 프로젝트의 *failed-proof catalog* case-study 기여. Gap 자체는 Atiyah 2018 발표 시점에 community가 식별; 본 프로젝트의 기여는 systematic critical reading의 5-category framework.

## The gap (paper-direct)

Atiyah 2018 *"The Riemann Hypothesis"* §3.3가 derivation 주장:

> ζ가 critical strip에서 critical line off에 zero b를 가진다고 가정. F(s) := T{1 + ζ(s+b)} − 1. **F(s) = 2F(s)** ⟹ F = 0 (in characteristic 0).

attempt 131이 §2.6, §2.7만 사용해서 직접 검증:

- §2.6 (paper-direct, weakly analytic): T{(1+f)(1+g)} = T{1+f+g}
- §2.7 (paper-direct): T(1+s) = T(1+s/2)²

Direct computation:

- T{(1+F)²} = T{1+2F} (§2.6, f=g=F)
- T(1+2F) = T(1+F)² = (1+F)² (§2.7)
- 양변 = (1+F)²

§2.6 + §2.7만으로 *F = 2F* 도출 X. **§3.3 step gap** 명시 식별.

본 finding은 Atiyah 2018 발표 시점에 broader community (Tao 등)가 독립적으로 식별한 것과 일관.

## 본 프로젝트의 기여: 5-category framework

`lemmas/failed_proof_catalog_publishable.md`이 실패 RH proofs의 systematic critical reading framework 제안:

- **Category A — Trivial circular**: spectrum identification 자체가 ζ-zero 조건과 trivially 동치
- **Category B — Reference circular**: 핵심 객체의 well-definedness가 미발표/미검증 paper에 의존
- **Category C — Identity transplant**: equation이 *limited domain* (linear approximation)에서만 성립인데 proof에서 *exact*로 사용
- **Category D — Multi-valued inversion**: f(g(s)) = 0 ⟹ g(s) = 0 step에서 multi-valued inverse 무시
- **Category E — Self-acknowledged speculation**: paper 자체에서 *"undecidable"* 또는 유사 disclaimer + *proof claim* 양립

**Atiyah 2018은 5 categories 모두 manifest** — framework의 self-evidence test:

- A: §3 derivation의 spectrum/zero relation trivially circular
- B: T(s) Todd function explicit form이 Royal Society submission [2] (미발표) 의존
- C: §2.6 (linear approximation, paper §2 명시)을 §3 proof에서 exact로 사용
- D: §3 derivation의 1+ζ(s+b) ∈ T⁻¹(1)이 multi-valued inverse 무시
- E: §5 *"general case undecidable in Gödel sense"* + §3 *"proof by contradiction"* 양립

## 가치 가능성

5-category framework가 reviewer + proof-writer에게 systematic gap-finding *prescriptive* checklist 제공. *Post-hoc descriptive*가 아니라.

## 본 프로젝트가 *아닌* 것

- §3.3 gap **본 프로젝트 original X** — Atiyah 2018 발표 시점에 community 식별. 본 프로젝트 기여는 *categorization framework*.
- Atiyah 본인 비판 아님 — 2018 paper 시점 89세, 실패 모드는 personal X, structural.

## 향후 framework 확장 가능성

de Branges series, 다양한 amateur preprint 등. 본 프로젝트는 systematic 미수행 — publishable potential.

## Audit trail (Layer 1)

- `lemmas/failed_proof_categories.md`
- `lemmas/failed_proof_catalog_publishable.md`
- `attempts/066_atiyah2018_search/`
- `attempts/131_atiyah_2018_failed_proof_deep/`
- `attempts/154_failed_proof_catalog_strengthen/` (Category F + de Branges mention)

## 반박 / 강화

§2.6 + §2.7만으로 F = 2F 도출 가능 argument: **x2ever.han@gmail.com**. 또는 5 categories 어디에도 manifest 안 하는 candidate failed proof — framework stress-test 환영.

---

[← Previous](../04-finding-connes-consani-progress/) · [English](../../../en/posts/05-finding-atiyah-step-gap/) · [Next →](../06-process-cycle-protocol/)
