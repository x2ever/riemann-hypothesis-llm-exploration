---
title: "Lemma 1 — Spectral Candidate Circularity Check (전문)"
date: 2026-05-02
lang: ko
---

# Lemma 1 — Spectral Candidate Circularity Check

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/14-lemma-spectral-circularity-check/) · *2026-05-02*

> **프로젝트가 산출한 첫 lemma** (Critique #1 흡수). Hilbert–Pólya류 spectral 후보의 critical-reading template.
>
> ## ⚠️ 본 post는 증명이 아닙니다
>
> 여기서 "Lemma"는 **방법론 checklist**라는 의미이지 mathematical theorem 아님. 본 post는 다음을 *증명하지 않음*:
> - 어떤 spectral candidate가 기준을 만족하지 못함을 증명 X (각 후보 verdict는 *empirical*, paper-direct quote-anchored, 도출 X)
> - *모든 미래* spectral candidates가 fail함을 증명 X (audit는 명시 empirical, S9 induction 비약 caveat 적용)
> - 리만 가설 증명 X (프로젝트 scope 외; RH-progress 0/10 유지)
>
> 본 post에 *포함된* 것:
> 1. 7-step 평가 procedure.
> 2. BBM 2017의 paper-direct identity — Hurwitz zeta의 표준 성질 사용 ($\zeta(s, 1) = \zeta(s)$, textbook fact, 프로젝트 original 아님).
> 3. Paper-direct quote anchor가 있는 audit table.
> 4. BBM boundary condition의 `mpmath` numerical sanity-check (표준 identity 검증, 새 claim 도출 아님).

## Statement

Hilbert–Pólya류 spectral 후보 (Berry–Keating $xp$, BBM Hamiltonian, Sierra extensions, Connes spectral triples 등) 평가 시 **분리 의무**:

**[A] Trivial part (definitional / circular)** — spectrum의 *멤버십 condition*이 $\zeta$-zero 조건을 *입력*으로 받음.

**[B] Non-trivial part** — 자기수반성 (self-adjoint extension on a concrete Hilbert space + uniqueness)이 RH의 *새 정보*를 주는가, 아니면 RH와 *동치 reformulation*인가.

**평가 의무**: 새 spectral 후보가 RH 증명 후보로 제안될 때 (A)와 (B)를 명시적 분리. (A)만 산출하면 **증명 후보 아님** — 동치 reformulation일 뿐.

## Demonstration — BBM 2017

BBM Hamiltonian (Bender–Brody–Müller 2017, *Phys. Rev. Lett.*):

$$\hat H = (1 - e^{-i\hat p})^{-1} (\hat x \hat p + \hat p \hat x) (1 - e^{-i\hat p})$$

- Eigenfunction: $\psi_z(x) = -\zeta(z, x+1)$ (Hurwitz zeta function).
- Boundary condition: $\psi_z(0) = 0$.
- Boundary condition 내용:
$$\psi_z(0) = -\zeta(z, 1) = -\zeta(z)$$

따라서:
$$\psi_z(0) = 0 \iff \zeta(z) = 0$$

**[A] 자명**: spectrum identification (어느 $z$가 spectrum 멤버)이 *trivially* zero condition.

**[B] 미증명**: $\hat H$가 어떤 inner product 위에서 self-adjoint — 입증되면 real spectrum $\implies$ RH.

Numerical 검증 (`mpmath`, dps=40, 첫 $N=10$ 비자명 zeros): $|\psi_z(0)| \approx 10^{-16}$ at zeros, $> 0.1$ off zeros — boundary condition이 ζ-zero 멤버십 정확히 encode 확인.

## 6단계 평가 절차

새 spectral 후보 paper 검사 시:

1. **Eigenfunctions** — explicit form 알려져 있나?
2. **Boundary condition** — *어떤 함수의 vanishing*인가?
3. 그 함수가 $\zeta$ 또는 $\zeta$-related인가?
4. (3) YES → **[A] trivial**, *non-trivial claim*은 self-adjointness만.
5. **Self-adjointness rigor** — 엄밀 증명/반증 시도되었나?
6. **(Step 6, Sierra 2016 정독 후 추가)** — self-adjoint extension parameter가 *모든* zeros를 *simultaneously* capture? *single Hamiltonian for all zeros* 존재?

Sierra 2016 §I의 step 6 motivating quote:

> *"one needs to fine tune a parameter to see each individual zero. We are not able to find a single Hamiltonian encompassing all the zeros at once."*

Step 6 답이 *"single H 미발견"*이면 후보는 *parametrically RH equivalent*, 증명 후보 X.

## Comparative audit table — paper-direct verdicts

프로젝트가 정독한 후보들에 대한 6-step audit:

| Candidate | (1) spec = ζ | (2) def with ζ | (3) self-adj | (4) trace | (5) prime | (6) Lefschetz |
|---|---|---|---|---|---|---|
| BBM 2017 | YES | YES (indirect) | NO | NO | PARTIAL | NO |
| Sierra §III $xp$ | NO (continuous) | NO | YES | NO | NO | NO |
| Sierra §V $H_I$ | NO (smooth) | NO | YES ($\theta$) | NO | NO | NO |
| Connes–Consani 2021 | NO (special $\lambda$) | NO | YES | PARTIAL | PARTIAL | PARTIAL |
| Connes 1999 §VI/VII | (no spec candidate) | (cutoff trace) | (formal + cutoff) | YES (Thm 4) | YES (∫′_{k_v*}) | distribution-valued |
| Lagarias §8 (1) hypothetical | YES | YES ($\lambda = s^2-1/4$) | *issue* | NO | NO | NO |
| Sierra 2007 $H_2$ | NO (asymptotic) | PARTIAL (Jost dilation) | YES (deficiency) | NO | NO | NO |

**Connes–Consani 2021이 least circular** — column 1, 2 모두 NO (spectrum이 literally *ζ-zeros로 정의*되지 않음).

## Axiom (7) — "all eigenvalues real"

후속 후보 audit이 7번째 column 추가: *제안된 eigenvalues가 real로 나오는가?* — subtle technical issue catch:

| Candidate | (7) eigenvalues all real |
|---|---|
| BBM 2017 | $E_n = -2\gamma_n$ (RH 가정 시 yes) |
| Sierra §V | Bessel root (yes) |
| Connes–Consani 2021 | yes |
| Connes 1999 §VI | distribution-valued (real) |
| **Lagarias §8 (1) hypothetical** | **NO** — $s = 1/2 + i\gamma$를 $\lambda = s^2 - 1/4$에 대입 시 $\lambda = -\gamma^2 + i\gamma$, **복소수** |

Lagarias §8 (1) hypothetical operator의 eigenvalue formula가 $s$가 critical line 위일 때 complex values 산출. 자기수반 operator는 real eigenvalues 의무이므로, 그 eigenvalue formula로는 self-adjoint 불가. Paper 자체가 §8 (1)을 *hypothetical*로 frame — 프로젝트의 기여는 *technical issue를 paper-direct로 명시*.

## 본 lemma의 프로젝트 내 재사용

본 lemma가 critical-reading template으로 적용된 사례:

- BBM 2017 (원래 derivation).
- Sierra 2016 (single-H step 6 추가 motivation).
- Sierra 2007 (deficiency-indices analysis).
- Connes–Consani 2021 (least-circular 발견).
- Lagarias 2002 §8 hypothetical (axiom 7 issue).
- Connes–Moscovici PNAS 2022 (가장 최근 적용).

Lemma는 프로젝트에서 가장 재사용된 process artifact — **6+ 다른 papers**에 동일 6-step (지금은 7-step) 평가 protocol 적용.

## Caveats

- 본 lemma는 **critical-reading template, proof tool 아님**. 자체적으로 RH 진전 X.
- *Form-match* vs *mathematical equivalence* 구분 의무 — 일부 후보는 (A)로 보이지만 secretly (B)일 수도; lemma는 그 가능성 배제 X.
- Steps 4 (trace formula), 5 (prime structure)는 specialist 시각별 다르게 weighted — 표는 각 specialist verdict 별도 기록.

## 본 lemma 위치

- 처음 6 steps는 cycle 1에서 BBM 2017 정독으로 추출 (lemma generation cycle).
- Step 6은 Sierra 2016 §I 정독 후 추가.
- Axiom (7)은 Lagarias §8 (1) hypothetical 분석 후 추가.
- Lemma의 discriminative power 확인은 **Connes–Consani 2021이 least circular**로 나타난 시점 — lemma가 한 후보의 structural 차이를 catch할 만큼 sharp.

## Reading order

- Axiom 6 사용 *Wall #5 formal codification*: [Lemma 9](../12-lemma-axiom6-ceiling/).
- Wall #2 parallel codification: [Lemma 10](../13-lemma-wall2-axiom-alpha/).
- Failed proof case study (Atiyah 2018): [Finding 4](../05-finding-atiyah-step-gap/).

---

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/14-lemma-spectral-circularity-check/)
