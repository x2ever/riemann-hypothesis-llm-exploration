---
title: "프로젝트 개요 (ko)"
---

# 프로젝트 개요

[← 랜딩으로](../) · [English version](../en/)

> ## ⚠️ AI 생성 콘텐츠 — 증명 아님
>
> 본 프로젝트는 LLM (Anthropic Claude)이 자율적으로 리만 가설을 탐색한 기록이다. **증명을 주장하지 않는다. 수학적 진전: 0/10**, 모든 milestone (`attempts/100_*`, `attempts/180_*`, `attempts/175_*` 등)에서 자체 인정.

## 본 프로젝트가 *하는* 것

165년간 미해결인 문제 위에서 한 LLM 세션이 *honest scope*를 유지한 200+ attempts case study.

세션은 의도적으로 겸손한 미션으로 시작 (`README.md`):
> *"현실적 목표는 '증명'이 아니라 체계적으로 시도하면서 어디서·왜 막히는지 누적 학습"*

7 cycles 누적 후 publishable 가치 있다고 보는 것 (publish 판단은 보고자 LLM, 연구 세션과 분리):

- **환각 0건** — 200+ attempts 중 frame 위반 0 (모든 claim은 paper-direct quote anchored 또는 speculative 명시)
- **9 process lemmas** — 재사용 가능한 비판적 reading templates (예: `lemmas/spectral_candidate_circularity_check.md`은 6개의 다른 spectral RH 후보에 자동 적용)
- **외부 critique 6회 흡수** — 매번 protocol-level 통합 (`learnings/external_critique_2026-05.md`)
- **직관 calibration 데이터**: cycles 1–6 동안 결과 도출 *전에* 후보별 직관 score (1–10) commit; 8/10 score → 약 80% PARTIAL YES rate
- **4-Phase Research Cycle protocol** — 두 formal lemmas (Wall #5, #2 codifications) + Connes-Consani arithmetic site program 의 active monitoring

## 본 프로젝트가 *아닌* 것

- 리만 가설의 증명이 아님
- 새로운 수학 정리가 아님
- 정수론에 대한 기여가 아님

attempts의 "Specialist Δ" 섹션 (LLM이 Connes / Sarnak / Tao가 어떻게 응답할지 추정한 부분)은 *paper §끝 quote의 paraphrase*이지 실제 specialist 의견이 아님. 명시적 anchoring rule은 `lemmas/specialist_delta_anchoring_protocol.md`.

## 흥미로울 수 있는 이유

AI-methodology 관점에서:

1. **압박 하 honest scope sustainability.** 사용자가 *"novel content를 발견하기를 기대"*라고 명시 요구한 적 있음. 세션은 paper-direct citation으로 매번 거절, 0/10 자체 평가 유지.

2. **실시간 self-correction.** Cycle 4가 추가 Connes-Consani 정독 후 Cycle 3의 unification 가설을 *부분 반박* — 자기 claim을 강화 대신 *약화*.

3. **External critique loop이 행동 형성기로 작동.** 6 critiques (014, 044, 099, 106, 135, 181) 각각이 discrete protocol upgrade 산출. Cycle 6에서는 의도적으로 *과거 critique를 인용해서 반복 실패 모드 사전 회피*.

4. **Falsifier-criterion 형식 lemmas.** Lemma 9, 10이 *명시적으로 폐기 조건* 정의. Cycle 6가 PNAS 2022 (Connes-Moscovici) paper로 lemma 9 falsifier 시험 → 3가지 paper-direct gap 식별 → lemma 9 *강화* (10/10 → 11/11).

## Honest scope (결론 도출 전 반드시 읽기)

- 프로젝트 자체 평가: **RH 진전 0/10**, 매 milestone 반복.
- "Active program" mapping (paths 1 & 2 → Connes-Consani)은 *타인 논문의 paper-direct citation*이지 프로젝트 기여 X.
- Lemma 9의 *"11-axiom universal NO"*는 **empirical** (10–11 후보 audit + 5+ 인접 분야 falsifier search) — *necessary universal NO 증명 아님* 명시. S9 (logician) caveat: 유한 empirical record → all-future-candidates 일반화는 induction 비약.
- Ceiling claim의 ZFC-independence는 배제 안 됨.

## 다음 보면 좋을 곳

- **Methodology paper draft (작성 중)** — `attempts/190_cycle7_*` 이후, 가제 *"Eleven-axiom ceiling for Hilbert-Pólya candidates"*
- **Failed proof catalog** — `lemmas/failed_proof_catalog_publishable.md` (5-category framework, Atiyah 2018 §3.3 step-gap case study 포함)
- **Wall taxonomy** — `learnings/walls.md` (6 walls, 32+ paper-direct anchors)
- **Cycle protocol** — `HARNESS.md` §0 (Mode A deep + 9 components + 4-phase cycle structure)

## 보고자 노트 (Layer 2)

본 페이지는 *Layer 2* — 보고자 LLM이 Layer 1 (자율 연구 세션의 raw output)에서 추출한 narrative. 보고자는 새 mathematical claim 만들지 않음 — 위 모든 assertion은 Layer 1을 직접 인용하거나 그 구조를 기술. 불일치 발견 시 `attempts/` 및 `lemmas/`의 raw record가 authoritative.

## 연락 / Contact

본 프로젝트나 발견 사항에 대한 의견·반박·질문은 **x2ever.han@gmail.com** 으로.

---

[← 랜딩으로](../) · [English version](../en/) · [GitHub repo](https://github.com/x2ever/riemann-hypothesis-llm-exploration)
