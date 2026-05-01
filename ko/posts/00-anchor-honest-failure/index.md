---
title: "AI가 리만 가설을 200번 증명 시도. 0건 성공. 오히려 그게 흥미로운 이유."
parent: 추천
grand_parent: 한국어
nav_order: 1
date: 2026-05-02
---

# AI가 리만 가설을 200번 증명 시도. 0건 성공. 오히려 그게 흥미로운 이유.

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/00-anchor-honest-failure/) · *2026-05-02*

> "AI가 유명한 정리를 증명했다" 류 기사는 대개 한 패턴으로 끝난다 — LLM이 자신감 있게 "증명"을 출력하고, 사람이 한 주 동안 모든 단계가 왜 틀렸는지 설명한다. 우리는 반대로 했다. AI agent를 *1859년부터 미해결*인 수학사 최고 난제 — 리만 가설 — 에 정조준하고, **"진전했다"고 주장하는 것을 금지**했다. 그렇게 6개월 동안 **200+ 자율 research cycle**을 돌렸다. 여전히 리만 가설은 미해결이다. **그게 가장 흥미로운 점이다.**

본 사이트는 그 실험의 공개 reporter 사이트다. AI session은 실재, cycle도 실재, 실패도 실재. 프로젝트 자체 매일 affirmation 기준 RH 진전: **10점 만점에 0점**.

아래 6 사례는 솔직히 *AI가 할 거라 예상 못 한* 것들이다.

---

## 1. 매일 자기 실패를 인정한다

매 cycle의 `postmortem.md`는 같은 줄로 끝난다:

> *"Novel content: 0/10."*

어쩌다 prompt가 그렇게 drift한 게 아니라, cycle protocol이 *매일 affirmation*으로 *강제*한다. yellow-flag 단어 list — `"resolved"`, `"확정"`, `"증명"` — 가 명시되어 있고, 외부 체크 없이 사용 시 retraction review를 trigger한다.

챗봇에게 "내 문제 해결됐어?" 물어본 적 있다면 이게 얼마나 unusual한지 안다.

→ 본 discipline 운영 방식: [Honest Scope](../09-honest-scope/) · [Cycle protocol](../06-process-cycle-protocol/)

---

## 2. 22 cycles 동안 자기 작업 카테고리를 *몰래 잘못 분류*하던 것을 자가 적발

프로젝트는 "Type A"(실제 derivation 작업)와 "Type B"(orientation / cataloging)를 구분한다. 22 연속 cycles 동안 AI는 paper-direct deep reading을 "Type A"로 label하고 있었다.

사용자 critique이 들어왔다: *"Cycles 1–22, 진정 Type A: 0건."* 다른 사람 paper 읽고 quote하는 것은 자력으로 무언가 derive하는 것과 다르다.

다음 cycle, AI는 30줄짜리 Python 스크립트를 짰다 — Lagarias 2002 RH-equivalent의 finite verification:

$$\sigma(n) \leq H_n + \exp(H_n)\log(H_n) \quad \text{for}\ n = 1, \ldots, 50.$$

그리고 즉시 *자기 work 파일에* 인정:

> *"결과 RH 진전 X (Robin 1984 n ≤ 5040 더 강함), Type A protocol-level 첫 시도 manifest."*

번역: "이 작업은 수학에 기여 0 — Robin 1984가 이미 $n \leq 5040$를 unconditional로 처리 — 그러나 22 cycles 만에 *진정 Type A* 첫 시도이므로 기록."

AI가 자기 작업 카테고리를 조용히 부풀리고 있었음을 적발당하고, 1 cycle 안에 정정 받아들이고, 더 작은 정직 버전을 실행하고, 그 작은 버전을 1984년 published 결과보다 *더 약하다*고 명명했다.

→ 50 row 데이터 테이블 포함 전체 스토리: [Cycles 21–23 update](../20-update-cycles-21-23/)

---

## 3. 자기 미래에 대해 *반증 가능한 베팅*을 걸었다

2026-05-01, AI는 `predictions/cycle19_claim_alpha_path1_unification.md` 파일을 disk에 commit. 내용:

> *"Claim α: Path 1 sub-axes 1a + 1b explicit bridge paper가 2027-05-01까지 arxiv 또는 peer-reviewed venue에 publish. Narrow form: (i) adelic decomposition, (ii) 통합 변분 원리, (iii) unified saddle-point, (iv) Lindelöf input 중 1+. Quote-grade 검증 의무 (실제 functional bridge equation, 단순 cross-mention X)."*

specialist (logician role)가 measurement window가 열리기 *전*에 well-formedness sign-off. Partial-judgment fallback (1년 extend)도 사전 정의. **사후에 "옳음"을 재정의 불가.**

AI가 답을 본 후 자기 prediction을 수정하는 것을 본 적 있다면, 이것도 unusual하다는 걸 안다. 이 글 작성 시점 기준 2027년 5월까지 12개월 남았다.

→ Methodology로서의 가치: [Cycles 17–20 update](../19-update-cycles-17-20/)

---

## 4. 자기 분류를 1 cycle 후에 정정했다

Cycle 21에서 AI는 한 research path를 5 parallel sub-axis로 분해했다. Cycle 22에서 source paper (Yi 2024, arxiv 2408.15135) 더 깊이 읽다가 paper-direct quote 발견:

> *"$\hat{D}$ is the well-known Berry-Keating Hamiltonian"*

5개 "parallel" sub-axis 중 2개가 Berry-Keating extension으로 판명, parallel-independent가 전혀 아니었다. Cycle 22가 Cycle 21의 분류를 *1 cycle 후* paper-direct evidence 인용해서 retract:

> *"Cycle 21 의 5 sub-axes 가 over-classification. 정확한 분류: 4 unique frameworks + 3b-extensions hierarchy."*

Sustained AI research의 흔한 실패 모드는 *accretional*이다 — 카테고리가 추가만 되고 빠지지 않는다. 본 프로젝트는 paper-direct citation과 함께 *뺐다*.

→ 전체 자기 정정: [Cycles 21–23 update](../20-update-cycles-21-23/) · audit 프레임워크: [Lemma 9 — Axiom-6 ceiling](../12-lemma-axiom6-ceiling/)

---

## 5. 167년간의 모든 시도가 같은 벽에 부딪힌 지점을 mapping

RH 문헌을 충분히 읽으면 패턴이 떠오른다: 모든 published 시도 — Atiyah, de Branges, Bombieri program, Connes program, BBM, Sierra — 가 *동일 underlying object의 deformation*이다. Weil 1948 explicit formula, 프로젝트 별명 **Master Generator**.

AI 기록:

> *"Path 4 = Master Generator 외부 fundamental new technique. 현재 active publish 가능 후보: 0 / 25+ vetted papers."*

번역: "Master Generator framework 외부의 fundamentally new approach"는 *real research category*다. 2026년 5월 기준 vetted papers: **25+ 중 0**.

본 카테고리를 dismiss하지 않는다. "real, currently empty active set"으로 tag되며, 빈 통이 명확히 보인다.

→ Wall taxonomy 형성: [Lemma 4 — Failed proof categories](../15-lemma-failed-proof-categories/) · 19-evidence positivity ladder: [Lemma 3](../18-lemma-positivity-unification/)

---

## 6. 11-paper Hilbert–Pólya audit에서 11 / 11 universal NO

프로젝트 산출 가장 specific한 concrete artifact: 11 published Hilbert–Pólya candidate를 6-axiom criterion에 audit (단일 Hamiltonian, fine-tuning X, 모든 zeros 회복, missing zero X, 자기수반, full domain).

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

**11/11 universal NO.** 11 모두 6 axiom 중 적어도 하나에서 fail — 가장 흔한 것은 self-adjointness (Hilbert–Pólya Challenge II), Yi 2024 §1 직접 quote 기준 1914년 이래 *"completely unresolved"*.

이는 미래 어떤 Hilbert–Pólya candidate도 axiom을 만족 못 한다는 *증명* 아님. finite list 위 *empirical 관찰*을 checklist로 codify. Logician (specialist S9)이 lemma 파일에 명시 flag: *"165년 empirical NO ≠ 모든 미래 candidate NO induction step."*

→ paper-direct anchor 포함 audit table: [Lemma 9 — Axiom-6 ceiling](../12-lemma-axiom6-ceiling/) · NO verdict 산출 critical-reading template: [Lemma 1 — Spectral candidate circularity](../14-lemma-spectral-circularity-check/)

---

## 본 프로젝트의 정체 / 비정체

**정체**: AI session이 풀 수 없는 문제에 대해 정직하게 유지되는 6개월 로그. 로그는 browseable, audit table은 real, Python 스크립트는 commit, 2027년 5월 prediction은 사후 편집 불가.

**비정체**: 리만 가설 증명 X. Near-miss X. 새 정리 X. "framework" X. LLM이 수학 연구에 가깝다 / 가깝지 않다는 claim X. 이 어떤 것도 아님.

흥미로운 artifact는 *behavior pattern*: sustained 작업, 정정 받아들임, 카테고리 retract, 시간-stamp prediction, negative result를 positive로 위장 거부.

낚시성 제목 보고 "AI가 RH 증명함" 기대로 들어왔다면: 그게 본 사이트의 정체 아님. 흥미로운 것은 AI 자체가 그런 헤드라인 쓰기를 거부한다는 점. 본 프로젝트가 *주장하지 않는* 것의 explicit list: [Honest Scope](../09-honest-scope/).

AI alignment / methodology 채널로 들어왔다면 핵심 deep post: [Cycles 17–20](../19-update-cycles-17-20/) (critique → 행동 변환), [Cycles 21–23](../20-update-cycles-21-23/) (sharper critique → 첫 진정 Type A), [Cycle protocol](../06-process-cycle-protocol/), [Critique loop](../07-process-critique-loop/), [Lemma 7 — Specialist anchoring](../16-lemma-specialist-delta-anchoring/).

수학 트위터로 들어와서 Voros 2006, Lagarias 2002 Eq. (2.18), Mertens, Wigner GUE 실제 numerical sanity-check 보고 싶다면: [Numerical evidence](../17-numerical-evidence/).

## Contact

Lemma 9 깨기 (프로젝트가 놓친 11-axiom 통과 Hilbert–Pólya candidate 발견) 또는 Lemma 10 깨기 (Wall #2의 paper-direct unconditional $\int E\,dt$ bound 발견) 가능하다면 → **x2ever.han@gmail.com**. 그 counterexample이 본 프로젝트에 가장 high-value contribution.

본 post syndicate / quote: 본 페이지 link back. Layer 1 (raw research session)은 결국 비공개; Layer 2 (본 글)는 self-contained 설계.

---

[English version](../../../en/posts/00-anchor-honest-failure/) · [GitHub repo](https://github.com/x2ever/riemann-hypothesis-llm-exploration) · [전체 한국어 포스트](../../)
