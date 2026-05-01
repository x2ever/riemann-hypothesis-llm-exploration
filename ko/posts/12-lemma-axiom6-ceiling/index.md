---
title: "Lemma 9 — Axiom-6 universal NO across 11 Hilbert-Pólya 후보 (전문)"
parent: 한국어
nav_order: 12
date: 2026-05-02
---

# Lemma 9 — Axiom 6 (Single Hamiltonian Uniqueness) Universal NO

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/12-lemma-axiom6-ceiling/) · *2026-05-02*

> **Process lemma 전문**, 본문 embed. Source: Cycle 1 (초기 draft) + Cycle 6 (PNAS 2022 retroactive falsifier test로 candidate #11 추가).

> ## Status disclaimer
>
> *Empirical* universal NO. *Necessary* universal NO **미증명** — S9 (logician) caveat: 165년 empirical NO에서 all-future-candidates NO로의 induction 비약. ZFC-independence 배제 X.
>
> Wall mapping: 본 lemma는 **Wall #5 (SELF-ADJOINT-RIGOR)**의 paper-direct 정량 codification.

## Statement

11 paper-direct Hilbert-Pólya류 spectral candidates 중 **axiom 6 strict 만족 = 0**.

> **단일 자기수반 operator $H$ on a fixed Hilbert space, 모든 비자명 $\zeta$-zeros를 bijective로 capture, fine-tuning parameter 부재** — 이 strict 조합은 paper-direct evidence에서 발견되지 않음.

## Axiom 6 strict — 4-specialist 합의 정의

"strict YES" criterion = 4개 분야별 정의의 simultaneous 합의:

| 분야 | Strict 정의 | Falsifiability |
|---|---|---|
| **NCG (S3)** | 단일 자기수반 $D$ on fixed $H$, 모든 $\zeta$-zeros $\leftrightarrow \mathrm{Sp}(D)$ bijective, fine-tune X | $\zeta$-zero $\mathrm{Sp}(D)$에서 missing $\implies$ NO |
| **양자물리 (S6)** | 단일 PT-symmetric $H$, *unbroken* PT phase, biorthogonal complete eigenbasis, eigenvalues bijective $\leftrightarrow \zeta$-zero imaginary parts | Broken PT 또는 fine-tune $\implies$ NO |
| **해석적 (S1)** | *단일* mollifier method 변환 (Levinson-style), 모든 zeros capture | Mollifier *family* 필요 시 $\implies$ NO (Pratt-Robles 50% 한계) |
| **logician (S9)** | ZFC에서 *"$\exists$ unique $H : \mathrm{Sp}(H) = $ {imag parts of $\zeta$-zeros}"* 증명 가능 | Existence-without-uniqueness 또는 ZFC-independent $\implies$ NO |

공통 본질: **fine-tuning 부재** + **모든 zeros 동시 capture**.

## Audit table — 11 paper-direct 후보

각 row의 anchor는 후보 출처 paper의 직접 인용.

| # | Candidate | Verdict | Paper-direct anchor |
|---|---|---|---|
| 1 | **BBM 2017** (Bender–Brody–Müller, *Phys. Rev. Lett.*) | NO | Paper 자체: *"We are not yet able to prove eigenvalues real"*. Boundary condition $\psi_z(0) = -\zeta(z, 1) = -\zeta(z)$, 즉 $\psi_z(0) = 0 \iff \zeta(z) = 0$ — spectrum identification이 *trivially* zero condition (Lemma 1 Step 6 BBM circular). |
| 2 | **Sierra §III** $xp$ (Berry–Keating 류) | NO | Continuous spectrum on real line — *no point spectrum*. 이산 $\zeta$-zeros capture 불가능. |
| 3 | **Sierra §V** $H_I$ | NO | Self-adjoint extension via parameter $\theta \in [0, 2\pi)$ — explicit fine-tune. Sierra 2016 §I: *"not able to find a single Hamiltonian encompassing all the zeros at once"*. |
| 4 | **Sierra 2007** $H_2$ | NO | Deficiency indices $(1,1)$, 자기수반 *family* parameterized by $1 \times 1$ unitary (Table 2). 하나의 canonical operator X. |
| 5 | **Connes–Consani 2021** $\Theta(\lambda, k)$ | NO | Special $\lambda$ values만; $\lambda^2 = 10.5, k = 18$에서 첫 31 zeros가 random-coincidence prob $\sim 10^{-50}$로 일치 — 그러나 spectrum이 *specific parameter choices*에서만 일치, 모든 zeros simultaneously X. |
| 6 | **Connes 1999** §VI/VII | NO | Paper introduction: *"unnatural parameter $\delta$"* — $\delta$-family of operators, 단일 X. |
| 7 | **Lagarias 2002** §8 (1) hypothetical | NO | Paper §8 hypothetical: $\lambda = s^2 - 1/4$. $s = 1/2 + i\gamma$ 대입 시 $\lambda = -\gamma^2 + i\gamma$, *복소수* — 자기수반 operator의 real spectrum과 incompatible. Paper 자체가 §8(1)을 hypothetical로 frame. |
| 8 | **Berry–Keating 1999** $H = xp$ | NO | Sierra 2007 §I quote: *"no concrete proposal realizing all conditions"*. Berry–Keating 1999 §II도 $xp$를 heuristic로 frame, rigorous candidate X. |
| 9 | **Sierra 2007** §VI $\zeta_H$ Jost | NO | M2 family of $(a, b)$ potentials — many operators, single X. |
| 10 | **Connes 1999** §III $(\mathcal{H}_\chi, D_\chi)$ | NO | Paper §III + introduction: *"$\delta > 1$ Sobolev exponent — unnatural"*. $\delta$-family. |
| 11 | **Connes–Moscovici 2022** ($W_{\mathrm{sa}}$, *PNAS*) | NO | UV asymptotic only — paper abstract: *"ultraviolet behavior reproduces"* (exact spectrum match X). $\lambda \in \{1, \sqrt{2}\}$ fine-tuning (paper §1). Lemma 2.1: deficiency indices $(4, 4)$ — multiple self-adjoint extensions, single canonical $H$ X. |

**Result: 11/11 axiom 6 strict NO.**

## Falsifier search — 인접 분야

11 direct 후보 외, lemma는 5+ 인접 분야에서 axiom 6 strict 만족 operator search:

- **Selberg trace formula** candidates — Selberg $\zeta$ (hyperbolic surfaces) $\neq$ Riemann $\zeta$ (length vs prime spectrum). Adelic version은 candidate #5. *Falsifier 아님.*
- **Function field RH** (Weil 1948 / Deligne 1974) — function-field 측은 axiom 6 YES (Frobenius eigenvalues), 그러나 **number field 측은 Wall #1 cohomological transfer 필요** = 별도 fundamental gap. Number field 측에서 *falsifier 아님*.
- **Berry's modified $H$**, quantum chaos "dressed" Hamiltonians — explicit single-$H$ construction literature 부재. *Falsifier 아님.*
- **Atiyah 2018 Todd-function approach** — explicit gap은 [Finding 4](../05-finding-atiyah-step-gap/) 참조. *Falsifier 아님.*
- **Connes–Moscovici 2022 (PNAS)** — Cycle 6 retroactive test, 위 candidate #11 참조. *Falsifier 아님* (UV asymptotic + fine-tune + multiple extensions).

**5+ 인접 분야 + 11 direct 후보 모두에서 falsifier 발견 X.**

## *아닌* 것

- 그런 operator 존재 불가능을 **증명하지 않음**. Lemma는 *empirical* — 11 후보 audit + 5+ falsifier 분야 search에서 axiom 6 strict 만족 X.
- **ZFC 분석에서 closed 아님.** RH는 $\Pi_1$ (Lagarias 2002). Universal-NO statement의 logical strength 미정; ZFC-independence 가능.
- **RH 진전 아님.** Lemma는 RH의 *언어 변경* — obstacle pattern codification, resolution path X. Lemma `Caveats` block에서 명시.

## Falsifier criterion — 본 lemma 폐기 조건

Lemma는 *falsifiable*. 다음 **3 항목 모두** 만족하는 단일 paper-direct candidate가 lemma 폐기:

1. **단일 $H$ on a fixed Hilbert space** — paper-direct quote.
2. **모든 $\zeta$-zeros $\leftrightarrow \mathrm{Sp}(H)$ bijective** — paper-direct verification.
3. **Fine-tuning parameter 부재** — paper-direct quote 또는 명시 parameter-free 정의.

3 항목 모두 paper-direct YES인 새 candidate 시 lemma 폐기 + 산출 cycle retroactive 정정.

## 본 codification이 가치 있을 수 있는 이유

Lemma는 향후 spectral candidate를 systematic test하는 **structured checklist**. Falsifier criterion 명시되어 있어 새 paper에 lemma 적용 시 분 단위:

1. Paper의 main spectral candidate 정의 정독.
2. Operator가 *단일* 인지 parameterized family인지 check.
3. Spectrum이 *모든* $\zeta$-zeros 매치 주장하는지 check (단순 asymptotic 아님).
4. Match 위해 parameter fine-tune 됐는지 check.

(2–4) 중 하나라도 fail 시 axiom 6 strict NO.

## Reading order

- 고수준 narrative: [Finding 1: 11/11 axiom-6 ceiling](../02-finding-axiom6-ceiling/).
- Candidate #11 추가의 falsifier-criterion application: Cycle 6의 Connes–Moscovici 2022 정독 ([Cycles 8–11 update](../10-update-cycles-8-11/) 참조).
- Wall #2 (forward heat flow)의 parallel codification: [Lemma 10](../13-lemma-wall2-axiom-alpha/).

## 반박 / 강화

axiom 6 strict-pass paper-direct candidate가 있다면 — **x2ever.han@gmail.com**. Lemma는 genuinely falsifiable.

---

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/12-lemma-axiom6-ceiling/)
