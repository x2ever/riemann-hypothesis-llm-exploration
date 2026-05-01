# Papers Wishlist — 추가로 읽고 싶은 / 필요한 논문 큐

> 시도 중 "이 논문이 있었으면 좋겠다" 고 떠오르면 즉시 여기 추가. 다음에 일괄 다운로드.

## 운영
- 항목 형식: `- [ ] <검색 키워드 / 저자·제목·연도> — *왜 필요한지 한 줄*`
- 다운받았으면 체크 + INDEX.md 로 이동.
- 다운로드 명령:
  ```bash
  cd tools
  uv run python fetch_paper.py arxiv <id> --key <key>
  # 또는
  uv run python fetch_paper.py url "<URL>" --key <key>
  ```

## High priority (다음 다운로드 후보)

- [ ] **Conrey 1989** — "More than two fifths of zeros are on critical line" — Levinson 방법 핵심. (저널, 무료 PDF 어려울 수 있음 — *paywalled*; pratt_robles_2019_5_12 가 후속/대체)
- [x] **~~Pratt-Robles-Zaharescu-Zeindler 2019~~** — "More than five-twelfths" — *added 009*
- [x] **~~Polymath 15 2019~~** — DBN upper bound — *added 009*
- [x] **~~Sierra 2016~~** — "Riemann zeros as spectrum" — *added 009*
- [x] **~~Sierra 2007~~** — "H = xp with interaction" — *added 009*
- [ ] **Montgomery 1973** — "Pair correlation of zeros" — RMT 연결의 origin
- [ ] **Keating & Snaith 2000** — RMT moments — RMT 모델 정량
- [ ] **Katz & Sarnak** — "Zeroes of zeta functions and symmetry" — symmetry types 분류
- [ ] **Berry & Keating 1999** — "H = xp and the Riemann zeros" — quantum chaos / HP (book chapter, 어려움; sierra_2016 가 인용·요약)
- [x] **~~Iwaniec & Sarnak, "Perspectives on the analytic theory of L-functions"~~** — *added 019*
- [ ] **Selberg trace formula** — 원본 또는 현대 해설
- [ ] **Weil 1948** — function field 위 RH 증명 — 핵심 비교 대상 (영문 번역/해설)
- [ ] **Deninger** — "Some analogies between number theory and dynamical systems on foliated spaces"

## Medium priority

- [ ] **Levinson 1974** — "More than one-third of zeros..." — Conrey 1989 의 baseline
- [ ] **Hadamard 1896 / de la Vallée Poussin 1896** — 소수 정리 원본 (역사적, ζ 의 1+it 위 무영점)
- [ ] **Bombieri & Lagarias** — "Complements to Li's criterion" — paywalled. *대체*: lagarias_sharpenings_li (019 다운로드).
- [ ] **Li 1997** — "The positivity of a sequence of numbers and the Riemann hypothesis" — *대체*: lagarias_sharpenings_li (019).
- [x] **~~Lagarias, "Li coefficients for automorphic L"~~** — *added 019*
- [ ] **Bagchi 1981** — universality theorem 류
- [ ] **Voronin 1975** — universality 원본
- [ ] **Connes & Marcolli** — "Noncommutative Geometry, Quantum Fields and Motives"

## Low / 비정통

- [ ] **Atiyah 2018** — preprint (실패) — 학습 자료
- [ ] **de Branges** — 본인 시도 시리즈 (검증 어려움 — 비판적 자료)
- [ ] **Bender, Brody, Müller 후속 / 비판 논문** — 그들의 PRL 에 대한 응답
- [ ] **Voiculescu** — free probability 와 ζ moments 연결 시도

## 시도 중 추가된 후보

(비어있음 — 첫 시도 진행하며 누적)

## 메모
- arXiv ID 가 알려진 논문은 즉시 받을 수 있음.
- 저널 PDF (Crelle, Ann. Math., Acta) 는 대부분 paywall — 저자 홈페이지·preprint 서버 검색.
- 책 챕터는 PDF 없음 — `background/` 에 정의·핵심 정리 옮겨 적기.
