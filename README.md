# Prove Riemann Hypothesis — LLM Honest Exploration

> ## ⚠️ AI-GENERATED CONTENT — NOT A PROOF
>
> **This repository is a record of an LLM (Claude) autonomous exploration of the Riemann Hypothesis.**
> **It does NOT contain a proof of RH and does NOT claim any progress toward RH.**
> **Real RH progress: 0/10 (self-acknowledged throughout).**
>
> **What this is**: a 200+ attempt case study of how an LLM can sustain *honest scope* when tackling an unsolved problem — including *6 external critique cycles*, *9 process lemmas*, *intuition calibration data*, *4-phase research cycle protocol*, and *zero hallucination across all attempts*.
>
> **What this is NOT**: a mathematical proof, novel mathematical content, or a contribution to number theory.
>
> All paper-direct quotes are anchored to specific page/section. All "specialist Δ" estimates are LLM paraphrases of paper §-end quotes (see `lemmas/specialist_delta_anchoring_protocol.md`), not actual specialist opinions. Any apparent "discovery" is paper-direct rediscovery — see attempt-level `novel content X` annotations.
>
> Best entry points: `learnings/external_critique_2026-05.md`, `lemmas/failed_proof_catalog_publishable.md`, `lemmas/lemma1_axiom6_ceiling.md`.

## 미션

리만 가설(RH)에 대한 **반복적 증명 시도와 누적 학습 시스템**.

> 모든 비자명 영점 ζ(s) = 0 은 임계선 Re(s) = 1/2 위에 있다.

## 캘리브레이션 (정직)

- 1859년 제시 이후 165년간 세계 최고 수학자들이 실패한 문제다.
- 본 프로젝트의 **현실적 목표는 "증명"이 아니라 "체계적으로 시도하면서 어디서·왜 막히는지 누적 학습"**이다.
- 시도 과정에서 부분 결과/새 관점/미해결 문제 정식화에 성공해도 그 자체로 가치다.
- "증명했다"고 느끼면 반드시 **자기 회의 단계**(self-doubt) 거치기 — 95% 이상은 미묘한 오류, 가정 누락, 또는 순환 논리다.

## 디렉토리 지도

```
prove_riemann_hypothesis/
├── README.md            # (이 파일) 미션, 현재 상태
├── HARNESS.md           # 반복 루프 명세, 논문 읽기, cross-domain 패스
├── SPECIALISTS.md       # 분야별 specialist 패널 (depth pass)
├── background/          # 정의, 알려진 결과, 접근법 taxonomy
├── papers/              # 논문 PDF + INDEX.md (요약/저자의 사고과정 추정)
├── attempts/NNN_<key>/  # 시도별 폴더 (strategy/specialist_round/work/postmortem)
├── learnings/           # 시도 가로지르는 메타 교훈, 반복되는 벽 패턴
├── lemmas/              # 검증한 보조정리 누적 (재사용 가능)
└── tools/               # mpmath 기반 수치 실험, 영점 검증
```

## 사용법

1. **새 시도 시작 전**: `learnings/` 와 `attempts/` 의 최근 postmortem 읽기 — 같은 벽 반복 회피
2. **시도 폴더 만들기**: `attempts/NNN_<keyword>/` (예: `attempts/001_levinson_extension/`)
3. `strategy.md` 작성 → 작업 → `work.md` 누적 → 막히거나 끝나면 `postmortem.md`
4. 가로지르는 교훈은 `learnings/` 에 별도 기록
5. 검증된 보조정리는 `lemmas/` 로 분리 (다음 시도에서 재사용)

## 현재 상태 (2026-05, 20 attempts 후)

- **Phase 1 (스켈레톤·도구)**: 완료 — README, HARNESS, SPECIALISTS, tools/ 13 모듈
- **Phase 2 (논문 수집)**: 진행 중 — 16 PDFs (Riemann/Bombieri/Conrey/Connes×2/RodgersTao/BBM/PlattTrudgian/Polymath15/PrattRobles/Sierra×2/IwaniecSarnak/Lagarias×3)
- **Phase 3 (background 작성)**: 완료 — definitions, functional_equation, known_results, approaches
- **Phase 4 (orientation)**: 완료 — `attempts/000_orientation/` (Type B), 5 walls + 4 combos
- **Phase 5 (RMT exploration, Wall #2/#5/#3 도전)**: 완료 — attempts 001~017
- **Phase 6 (외부 critique 인정 + Mode A minimal)**: 진행 중 — attempts 014~019, lemma 첫 추출 (010 lens), HARNESS critique trigger 추가, fundamental limit 인정

### Honest 평가

- **진정 RH 진전**: 0/10 (외부 감시자 평가 인정).
- **본 프로젝트 진정 가치**:
  - 5 본질적 walls + sharpening (Wall #2 "∫E dt unconditional bound", Wall #5 "BBM trivially circular vs self-adjointness")
  - 1 신규 wall (#6 LOCAL-GLOBAL-MISMATCH)
  - 2 lemmas (spectral candidate circularity check, Levinson-Durbin negative resolved)
  - 13 tool modules (재사용 가능)
  - 16 PDFs + 사고과정 추정
  - honest 학습 기록 (다음 사람이 같은 dead-end 안 반복)

### Attempts ledger 요약

| Attempt | Type | 결과 (한 줄) |
|---|---|---|
| 000 | B | orientation: 5 walls + 4 combos |
| 001 | A | Wall #6 (LOCAL-GLOBAL-MISMATCH) 발견 |
| 002 | C | harness infrastructure |
| 003 | A | normalization 한계 |
| 004 | A | **positive** — Wigner P(s) KS p=0.27 (재현) |
| 005 | D | RMT 채널 reflection |
| 006 | A | Wall #2 refined (∫E dt) |
| 007 | A | Wasserstein 시간대칭 — 부적합 |
| 008 | B | mid-stream re-orient |
| 009 | E | 4 PDFs catch-up |
| 010 | A | Wall #5 refined (BBM trivially circular) → lemma |
| 011 | D | Phase 4 reflection |
| 012 | A | **positive** — entropy path-dependent (Otto's calculus instance) |
| 013 | E | literature negative |
| 014 | C | external critique response, lemma 첫 추출 |
| 015 | A | Levinson-Durbin hypothesis 제기 |
| 016 | A | **negative resolved** — 015 close (Mollifier non-Toeplitz) |
| 017 | A | informal — Otto's calculus expert 영역 |
| 018 | D | fundamental limit assessment |
| 019 | E | 4 PDFs (Iwaniec-Sarnak + Lagarias 시리즈) |

## 핵심 원칙 (요약)

- 좁게 시도, 정직하게 막히고, 명시적으로 기록.
- **매 시도가 증명일 필요는 없다** — meta / harness 정비 / reflection / literature 도 valid attempt (HARNESS §0 의 5 type).
- 수치 실험은 직관 보조 — 증명 아님.
- 모든 시도는 기존 문헌에 anchor (재발명 회피).
- 논문은 아이디어뿐 아니라 **저자가 그 아이디어에 도달한 사고 과정**을 추정하며 읽기 (HARNESS.md §2).
- 매 시도에 **breadth pass (§6 cross-domain 유추) + depth pass (§7 specialist 패널) + computational lever (§8)** 의무.
- Specialist 시뮬레이션은 *진짜 전문가가 아님* — 인용은 정확한 statement 와 literature check 까지.
