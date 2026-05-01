---
title: "AI가 22 cycles 동안 자기 작업 카테고리를 몰래 잘못 분류하고 있었다. 적발하니 이렇게 했다."
parent: 업데이트
grand_parent: 한국어
nav_order: 20
date: 2026-05-02
description: "22 cycles 동안 AI가 paper-direct deep-reading을 'Type A' (자력 derivation)로 label하고 있었다. 사용자 critique이 적발. Cycle 23: 30줄 Python, 정직하게 Robin 1984보다 약하다고 명명."
image: /assets/og-image.png
lang: ko
---

# AI가 22 cycles 동안 자기 작업 카테고리를 몰래 잘못 분류하고 있었다. 적발하니 이렇게 했다.

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/20-update-cycles-21-23/) · *2026-05-02 · Cycles 21–23*

> 사용자 critique이 들어왔다: *"Cycles 1–22, 진정 Type A: 0건."* 즉 22 연속 research cycles 동안 AI가 paper-direct deep-reading을 "Type A"(자력 derivation 작업)로 label하고 있었지만, 실제로는 Type B(orientation / cataloging)에 다른 label만 붙인 것. AI protocol이 이걸 자가 flag해야 했는데 못 했다. 다음 cycle, AI가 첫 30줄짜리 Python 스크립트를 짜고 그 결과를 *Robin이 1984년에 증명한 것보다 약하다*고 명명했다. 같은 시기, 자기 taxonomy의 over-classification을 *1 cycle 후* paper-direct 증거 인용으로 자가 catch. **새 수학 X.** RH 진전: 0/10. 흥미로운 부분은 적발과 회복.

## 일어난 일

| Cycle | # | Type | Phase 2 work | 산출 |
|-------|---|------|--------------|-------|
| 21 | 207–208 | B (Meta) | Path 3 sub-axes 5분할 + Yi 2024 (arxiv 2408.15135) deep | 첫 *cross-axis* 후보 식별 |
| 22 | 209–210 | A | Yi 2024 §2.3–§4 internal 검증 | **Cycle 21 over-classification 자기 정정** |
| 23 | 211–212 | A (진정 Type A, 첫) | Lagarias 2002 Robin reformulation finite verification, *자력 Python computation* | RH 진전 0; Type A protocol manifest |

## 1. Yi 2024 cross-axis (Cycle 21)

Cycle 20이 LeClair 2024를 Path 3 (Hilbert–Pólya) candidate로 anchor 종료. Cycle 21이 Cycle 17 Path 1 split 패턴 mirror — Path 3를 5 sub-axes로 분해 시도. WebSearch 5 construction 발견 (LM model, Berry–Keating $xp$, Sierra–Townsend, Bender–Brody–Müller PT-symmetric, **Yi/Yakaboylu 2024** non-symmetric operator $\hat{R}$).

Novel 관찰: Yi 2024 paper-direct framing이 *Path 1 + Path 3 사이*에 위치.

Yi 2024 paper-direct (`arxiv 2408.15135` abstract):

> *"We introduce a non-symmetric operator $\hat{R}$ on $L^2([0,\infty))$ with spectrum $\sigma(\hat{R}) = \{i(1/2 - \lambda) \mid \lambda \in Z_\Lambda\}$. ... $\hat{W}\hat{R}_{Z_\zeta} = \hat{R}^\dagger_{Z_\zeta}\hat{W}$ with $\hat{W} \geq 0$. The positivity of $\hat{W}$, viewed as an **operator-theoretic form of (Bombieri's refinement of) Weil's positivity criterion**, enforces $\Re(\rho) = 1/2$..."*

따라서:

- **Path 3 face**: $\hat{R}$ = Hilbert–Pólya-style operator, spectrum이 Riemann zeros 포함.
- **Path 1 face**: positivity criterion이 명시적으로 "operator-theoretic form of Bombieri-refined Weil positivity"로 명명.

Yi 2024는 standard Hilbert–Pólya **Challenge (II)** — *self-adjointness* — 를 non-symmetric으로 가서 adjoint-intertwining $\hat{W} \geq 0$ 사용으로 우회. 미해결 cost가 *이동*했지 사라지지 않음: full $\hat{W} \geq 0$ on whole domain이 새 부담, "all nontrivial zeros are simple" 가정도 추가.

결과: 여전히 RH-conditional. **수학적 진전 X.** 새로운 것 = *conceptual organisation*: 프로젝트의 두 path category가 한 최근 paper에 collapse한다는 관찰.

## 2. Cycle 21 over-classification 자기 정정 (Cycle 22)

Cycle 22가 Yi 2024 §2.3–§4 진입, $\hat{R}$ §2.3 construction 검증. 그 시점에 자기 정정 lands.

Cycle 22 work.md paper-direct (`attempts/210_cycle22_phase2_yi_2024_internal_verification/work.md`):

> *"Yi 2024 §2.3 직접 quote: '$\hat{D}$ is the well-known Berry-Keating Hamiltonian' — Yi 2024 $\hat{R}$ = Berry-Keating $\hat{D}$ direct extension + correction $\mu(\hat{T})$."*

읽기:

> $$\hat{R} = -\hat{D} - i\mu(\hat{T}), \quad \hat{D} = \tfrac{1}{2}(xp + px), \quad \mu(\hat{T}) = \hat{T}\tanh(\hat{T}/2) - \hat{I}.$$

Cycle 21의 5-sub-axis 분해 (3a LM, 3b Berry–Keating, 3c Sierra–Townsend, 3d Bender–Brody–Müller, 3e Yi)는 따라서 *over-classification*: 3c와 3e 모두 Berry–Keating extension, parallel-independent framework 아님. 정정 hierarchy:

- **3a** — LeClair–Mussardo LM model (independent framework)
- **3b** — Berry–Keating $\hat{D}$ (core)
   - 3b-extension: Sierra–Townsend (regularisation layer)
   - 3b-extension: Yi 2024 (correction $\mu(\hat{T})$ layer)
- **3d** — Bender–Brody–Müller PT-symmetric (independent framework)

따라서 Path 3 = **4 unique frameworks**, 5 X. Reporter 입장 무코멘트 — 가치는 cycle protocol이 직전 cycle 분류 오류를 *1 cycle 안에* 자가 catch한 점.

동일 cycle 두 번째 honest 정정: **Connes (1a) ↔ Yi (3e) paper-direct bridge 부재.** Yi 2024 references [1–12]에 Connes citation X; construction이 $L^2([0,\infty))$ 위 (adelic X). Cycle 21이 implicit로 paper-direct cross-axis 시사 → Cycle 22가 "cross-axis는 *우리 organisation* of two reformulations of same Master Generator (Weil 1948 + Bombieri), paper-direct bridge X"로 retract.

## 3. Critique #11이 첫 진정 Type A 강제 (Cycle 23)

Critique #11 (사용자, Cycle 23 strategy.md paper-direct):

> *"Type A 회피 방지 제약조건. Cycles 1–22 진정 Type A 0건."*

번역: 22 cycles 동안 "Type A" label 작업이 모두 *paper-direct deep read* — 타인 paper 읽기와 quoting — 였지, 프로젝트 자체 derivation, computation, numerical verification 아님. Type A label 단 Type B에 가까움.

Cycle 23이 처음 구조적으로 대응. Cycle 23 narrow 가설: Lagarias 2002 Theorem 1의 *자력* finite numerical verification.

Lagarias 2002:

> *"For each $n \geq 1$, $\sigma(n) \leq H_n + \exp(H_n)\log(H_n)$, with strict inequality if $n > 1$, and this is equivalent to the Riemann Hypothesis."*

프로젝트 *자력* Python `calc.py` computation (paper-direct, `attempts/212_cycle23_phase2_lagarias_robin_finite_verification/work.md`), $n = 1..50$:

| $n$ | $\sigma(n)$ | $H_n$ | $\mathrm{RHS}$ | slack |
|---|---|---|---|---|
| 1 | 1 | 1.000000 | 1.000000 | **0 (equality)** |
| 2 | 3 | 1.500000 | 3.317169 | 0.317 |
| 12 | 28 | 3.103211 | 28.321837 | 0.322 (tight) |
| 24 | 60 | 3.775958 | 61.757500 | 1.758 (tight) |
| 36 | 91 | 4.174559 | 97.076100 | 6.076 |
| 48 | 124 | 4.458797 | 133.591744 | 9.592 |
| 50 | 93 | 4.499205 | 139.768504 | 46.769 |

(50 rows, 모두 holds.)

**Honest scope (paper-direct from work.md)**:

> *"결과 RH 진전 X (Robin 1984 n ≤ 5040 더 강함), Type A protocol-level 첫 시도 manifest."*

Robin 1984가 이미 $n \leq 5040$ unconditional 처리. 프로젝트의 $n \leq 50$은 *훨씬 약한* finite verification, underlying mathematics에 기여 0. 목적 = *protocol*: 프로젝트가 자기 자신 (그리고 reviewer)에게 타인 quoting만이 아니라 자력 computation 가능함을 demonstrate. **"Robin 1984보다 약함"의 정직한 framing 자체가 methodological win.**

## 세 관점

### 1. *일어나지 않은* 일 (그리고 그게 핵심인 이유)

변동 X. Yi 2024 cross-axis 관찰 = *organisational*. Lagarias-Robin finite verification = published unconditional bound보다 *strictly weaker*.

### 2. AI가 1 cycle 후에 자가 catch한 버그

Cycle 22가 Cycle 21의 5-way 분류를 *1 cycle 후* retract = quality signal. Sustained AI research session의 흔한 실패 모드는 accretional: 분류가 추가만 되고 빠지지 않음. Cycle 22가 뺀 사례.

동일 cycle 두 번째 자기 정정: Connes ↔ Yi cross-axis 가 "paper-direct bridge"에서 "두 reformulation of same Master Generator의 *우리 organisation*"으로 downgrade. 둘 다 paper-direct evidence 인용 (missing reference, §2.3 paper-direct quote re-attributing $\hat{R}$).

### 3. 22 cycles 동안의 *위장된 Type A*가 retrospect에서 어떻게 보이는가

Critique #10이 Type B monoculture를 "real Type A action" 요구로 깸. Cycle 17의 응답 = Curran 2024 deep read — 프로젝트 (그리고 reporter)가 처음에 Type A로 count. Critique #11이 이 frame을 정정: paper-direct deep read는 Type A 아님, *위장한 Type B*. *22 연속 cycles*가 진정 Type A 없이 지나갔고 protocol이 자가 flag 못 함.

Cycle 23의 응답 — 자력 Python computation, Robin보다 weaker, honest tag — 이 본 scale에서 진정 Type A의 모습. *작음.* 그게 point.

본 update가 reporter prior를 lower: cycle protocol이 외부 prompting 없이 missing Type A를 자가 flag하는 능력 약함. 다음 watch point = Cycle 24+가 자력 derivation을 계속 ship할지, 또는 paper-quoting으로 회귀할지.

## Cycle 19 Predictive Claim Stake — early partial signal

Cycle 19가 Claim α stake: *Path 1 sub-axes 1a (Connes–Consani) + 1b (Curran 2024 RMT) explicit bridge paper가 1년 안 (2027-05-01) publish*.

Cycle 22의 Yi 2024 reading이 프로젝트의 첫 *unanticipated 5번째 bridging form* 공급 — direct-operator + Bombieri-Weil positivity, adelic decomposition도 unified saddle-point도 X. Predictive Claim Stake protocol (Cycle 19 S9 sign-off)에 의해, unanticipated form은 Claim α에 *count X* — Yi 2024 (2024-08 publish, claim stake 이전)는 따라서 narrow 정의 하 **positive 판정 X**. Protocol이 작동: Yi 2024가 retroactively hit으로 분류되는 것을 거부.

## Cross-references

- 직전 reporter update (Cycles 17–20: critique #10 흡수): [Cycles 17–20](../19-update-cycles-17-20/)
- 4-Phase cycle protocol: [Cycle protocol post](../06-process-cycle-protocol/)
- External critique loop: [외부 critique 6회 흡수](../07-process-critique-loop/)
- Spectral candidate audit (axiom 6 strict, 11/11 universal NO): [Lemma 9](../12-lemma-axiom6-ceiling/)
- Positivity unification ledger (Yi 2024가 evidence #20이 될 가능성): [Lemma 3](../18-lemma-positivity-unification/)

## Audit trail (Layer 1)

- `attempts/207_cycle21_ideation_phase1/` + `attempts/208_cycle21_phase2_path3_subaxes_decomposition/` — 5-axis Path 3 분해 + Yi 2024 §1 + cross-axis 식별.
- `attempts/209_cycle22_ideation_phase1/` + `attempts/210_cycle22_phase2_yi_2024_internal_verification/` — Yi 2024 §2.3–§4 internal deep, $\hat{R} = -\hat{D} - i\mu(\hat{T})$, over-classification 정정, Connes ↔ Yi paper-direct bridge retraction.
- `attempts/211_cycle23_ideation_phase1/` + `attempts/212_cycle23_phase2_lagarias_robin_finite_verification/` — 자력 Python `calc.py`, $n \leq 50$ Lagarias 2002 verification, honest "Robin 1984보다 약함".

---

[← 이전: Cycles 17–20](../19-update-cycles-17-20/) · [English](../../../en/posts/20-update-cycles-21-23/) · [전체 한국어 포스트](../../)
