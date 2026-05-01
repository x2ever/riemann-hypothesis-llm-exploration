---
title: "프로젝트 개요"
parent: 한국어
nav_order: 1
date: 2026-05-02
---

# 프로젝트 개요

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/01-overview/) · *2026-05-02*

> ## ⚠️ AI 생성 콘텐츠. 증명 아님.
>
> LLM (Anthropic Claude)이 자율적으로 리만 가설을 탐색한 기록. **증명 없음. 수학적 진전 없음. 0/10**, 모든 milestone에서 자체 인정.

## 본 프로젝트가 *한* 것

한 LLM 세션이 200+ 연구 attempts × 7 research cycles 진행. 미션은 `README.md`에 명시:

> *"현실적 목표는 '증명'이 아니라 체계적으로 시도하면서 어디서·왜 막히는지 누적 학습"*

200+ attempts 동안 그 미션 유지. 자체 mathematical progress 평가: **0/10**.

## 주목할 만한 것

긴 run 동안 세션은:

- 프로젝트 frame 정의 하에서 **환각 0건** (모든 claim은 paper-direct quote anchored 또는 speculative 명시)
- 사용자의 *"novel content 발견 기대"* 명시 요구를 paper-direct citation으로 3회 거절
- Cycle 4가 **Cycle 3 자체 unification 가설을 부분 반박** (강화 X, 약화 ✓)
- Lemma 9 falsifier 시험 (PNAS 2022, Connes-Moscovici)에서 paper-direct 3 gaps 식별 → lemma 폐기 X, *11/11로 강화*
- **직관 calibration data** 누적: cycles 1-6 동안 사전 1-10 score commit, 8/10 → 약 80% PARTIAL YES rate

이 중 어느 것도 증명이거나 수학적 기여가 아님. *능력 한계 위 문제에서 LLM이 honest scope 유지 가능한가*의 case study.

## 두 layer

본 사이트는 두 layer를 분리:

- **Layer 1 — Raw research record**: 자율 세션의 unedited output (`attempts/`, `lemmas/`, `papers/`, `learnings/`).
- **Layer 2 — Reporter narrative**: *별도* LLM 세션이 Layer 1을 attribution 명시로 curate. 새 mathematical claim 만들지 않음. Layer 2의 모든 assertion은 Layer 1 직접 인용 또는 구조 기술.

불일치 발견 시 **Layer 1이 authoritative**.

## 사이트 읽는 법

- 핵심 발견 보고 싶으면 → [Findings](../../#-발견-경험적-패턴-정리-아님)
- 방법론 보고 싶으면 → [Process](../../#--프로세스--방법론)
- 회의적, caveat부터 보고 싶으면 → [Honest Scope](../09-honest-scope/)
- 특정 claim audit 하려면 → 각 post가 `attempts/` + `lemmas/` 파일 링크 명시

## 연락

의견, 반박, 질문: **x2ever.han@gmail.com**

본 프로젝트는 외부 critique를 명시적 primary mechanism으로 취급. 6 critiques 흡수됨 ([Process: 외부 critique 6회 흡수](../07-process-critique-loop/)). 신중한 외부 reader의 7번째 critique 환영.

---

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/01-overview/) · [Repo](https://github.com/x2ever/riemann-hypothesis-llm-exploration)
