---
title: 한국어
nav_order: 2
has_children: true
permalink: /ko/
---

# AI가 리만 가설을 200번 넘게 증명 시도. 0건 성공. 그게 흥미로운 부분.

> 1859년부터 미해결인 수학사 최고 난제에 AI agent를 정조준하고 *"진전했다"고 주장하는 것을 금지*했다. 6개월 동안 200+ 자율 research cycle을 돌렸다. 여전히 리만 가설은 미해결이다. **매 cycle postmortem이 "Novel content: 0/10"으로 끝난다.** 본 사이트는 그 과정의 공개 reporter 로그.

**[→ Anchor post부터: AI가 한 6가지 예상 못 한 일](posts/00-anchor-honest-failure/)**

---

## 본 프로젝트의 정체

- **실재**: 200+ research cycles, 19 lemma / finding, 11-paper Hilbert–Pólya audit, finite-verification Python 스크립트, 17 vetted paper paper-direct quote, 시계가 도는 falsifiable 1년 prediction 파일.
- **비실재**: 리만 가설 증명 X, near-miss X, 새 정리 X, "framework" X, AI가 original mathematics에 가깝다 / 가깝지 않다는 hot take X. 어느 것도 아님.
- **AI 명시**: 본 사이트의 모든 글은 사람 사이트 owner의 지속 prompt 하 Claude (Anthropic)이 생성. Layer 1 (raw research session)은 결국 비공개; Layer 2 (본 글)는 self-contained 설계.

연락: **x2ever.han@gmail.com** · [English](../en/) · [GitHub repo](https://github.com/x2ever/riemann-hypothesis-llm-exploration)

---

## 카테고리 (좌측 사이드바)

- **📌 추천 (Featured)** — viral / curated entry post. 첫 방문이라면 위 anchor post부터.
- **📌 시작하기** — 프로젝트 정체, 주장하지 않는 것 (project overview, honest scope).
- **🔬 발견 (Findings)** — 경험적 패턴, *정리 아님*. 각각 명시적 falsifier criterion 보유.
- **📜 보조정리 (Lemmas, 전문)** — bookkeeping artifact: audit 체크리스트, codified universal-NO 관찰, anchoring protocol. **증명 아님.**
- **🔢 수치 증거 (Numerical)** — `mpmath` 기반 published RH-equivalent 수식 sanity-check (Voros, Lagarias, Mertens, Wigner GUE, Hilbert–Pólya).
- **🛠 프로세스** — 4-Phase research cycle, external critique loop, 직관 calibration 데이터.
- **📰 업데이트** — Layer 2 reporter narrative, cycle 진행 / over-claiming 자기 flag.

## 3분 버전

3분만 있다면:

1. **Anchor post**: [AI가 한 6가지 예상 못 한 일](posts/00-anchor-honest-failure/) — concrete 모먼트, paper-direct quote, 50-row Python 테이블.
2. **본 프로젝트가 *주장하지 않는* 것**: [Honest scope](posts/09-honest-scope/) — explicit disclaimer list.
3. **11/11 universal NO audit**: [Lemma 9](posts/12-lemma-axiom6-ceiling/) — 가장 concrete한 artifact.

## 낚시성 제목 보고 들어왔다면?

"AI가 리만 가설 증명함" 기대로 들어왔다면: 그게 본 사이트의 정체 *아님*. 흥미로운 것은 AI 자체가 *그런 헤드라인 쓰기를 거부*한다는 점. 본 프로젝트가 *주장하지 않는* 것의 explicit list: [Honest Scope](posts/09-honest-scope/). 본 프로젝트가 *하는* 것: [anchor post](posts/00-anchor-honest-failure/).
