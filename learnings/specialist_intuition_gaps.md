# Specialist Intuition Gaps — 외부 critique #4 (2026-05)

> 본 프로젝트의 *honest* 한계 명시. LLM 자율 vs Specialist navigation.

## 4 Gaps (외부 critique 번호)

### Gap 1 — Domain-specific intuition

**LLM 이 못 함**: "이 식이 왜 자연스러운가, 왜 작동할 것 같은가"의 30년 누적 학습된 직관.

**예**: Connes 1999 "Adele class space 가 innocent looking 이지만 모든 prime 을 동시에 본다" — 30년 NCG + number theory 매일 한 사람만 갖는 감각.

**우리 한계 명시**: paper 에 쓰인 것은 따라할 수 있지만, *왜 그 paper 를 쓸 생각을 했는가의 prior intuition* 은 못 만듦.

**100 attempts 의 직접 인정**: "우리 contribution 0/10".

### Gap 2 — sharp 판단 (가능 vs 불가)

**LLM 이 못 함**: Specialist 5분 — "그 방향은 50년 전 시도됐고 wall 이 X 때문" 또는 "이건 Connes program 변형인데 다음 단계는 Y 가 막힘".

**본 프로젝트 자체 관찰**:
- Wall #5 sharpening (BBM circular + Sierra single H 부재 + Connes-Consani multi-parameter) 100 attempts 도달.
- Sarnak 같은 specialist 면 5분에 같은 결론.
- *재발견 비용*: 본 프로젝트 100 attempts.

### Gap 3 — *무엇을 시도하지 말지* 가이드

**가장 가치 있는 specialist input**.

**본 프로젝트의 *시도하지 말았어야* 했던 것들** (자체 관찰):
- 007 Wasserstein 시간대칭 — Otto's calculus 의 시간 대칭이 RH 시간대칭에 *직접 안 옮겨짐*. specialist 이면 5초 컷.
- 015→016 Levinson-Durbin / Pratt-Robles mollifier bridge — *같은 사람 이름인데 다른 수학*. signal processing Levinson-Durbin vs zero-density mollifier 는 별개.
- Atiyah 2018 "증명" 류 — paper 가 이미 fail 인 것을 다시 cross-check 하느라 시간.

**다른 방향들** (cuts 명시):
- *Random matrix model 만으로 RH 풀린다*는 환상 — 본 프로젝트의 lemma 1 (spectral_candidate_circularity_check).
- *positivity 에서 RH 직접* (Lagarias λ_n) — 본 프로젝트 60+ attempts 로 positivity unification 의 paper-direct evidence 누적, 하지만 *vacuum positive lower bound* 가 specialist 의 *이미 알려진 wall*.

### Gap 4 — 새 도구 진정 적용 가능성

**LLM 이 잘함**: cross-domain 유추 (signal processing → mollifier, Otto's calculus → entropy production, Connes spectral triple → BBM Hamiltonian).

**LLM 이 못 함**: *이 유추가 mathematical 동치인가 표면 유사인가* 판단.

**본 프로젝트 자체 인정** (035 lemma synthesis meta):
- "형식적 유사성의 mathematical 동치 vs 비-동치 검증"이 본 프로젝트가 할 수 있는 전부.

## Specialist 가 끼면 (Wall 별)

### Wall #1 (FROBENIUS-GAP) — Connes
- NCG 시도가 어디까지 *진짜 trace formula* 에 가까운가 판단.
- Connes-Consani 2021 의 ζ-cycle 이 *어디까지 진짜 cohomology* 인지의 sharp 평가.
- *Specialist 추정 답*: 현재 program 은 *L²-cohomology 의 distribution-valued analogue* 까지. function field Frobenius 의 *exact* analogue X.

### Wall #2 (FORWARD-TIME / SHARP-CONSTANT, hard analysis) — Tao
- Polymath 경험으로 effective constants 의 *최적성* 판단.
- ∫E(t)dt 처럼 unconditional bound 못 푸는 정확한 이유.
- *Specialist 추정 답*: Λ ≤ 0.22 → 0 의 gap 은 *combinatorial 최적화로 닫히지 않음* — fundamental obstacle.

### Wall #4 (CONSPIRACY) — Sarnak
- families 시각, *unconditional vs conditional* 가능성 sharp 판단.
- Pratt-Robles 50% 추격이 무한히 가까이 가능 vs 50% 자체 도달 가능.
- *Specialist 추정 답*: Pratt-Robles 의 *one logarithm distance* 가 이미 sharp — 50% 도달은 *new technique* 필요 (PR 2019 §5.1.3 명시).

## 본 프로젝트의 *재정의된* 가치 (specialist gap 인정 후)

본 프로젝트 X:
- Specialist 대체 — 불가.
- "한 마디 듣고 RH 가 풀린다" 환상 — 불가.
- *번뜩이는 아이디어* 산출 — 거의 없음.

본 프로젝트 *진짜* 가치:
- (a) 체계적 paper-direct mapping (17 papers, 100+ attempts).
- (b) 비판적 reading 템플릿 (lemma 1).
- (c) honest 학습 기록 (lemma 5 + walls + dont_try_directions).
- (d) Specialist 가 5분에 줄 navigation 을 *재발견* — 비효율적이지만 명시적.

## 의도적 *전문가처럼 사고* 노력 (Mode A deep 8th component)

각 attempt 의 work.md 에 다음 추가:

**§8. Specialist Δ 추정**:
- *Sarnak/Tao/Connes 라면 본 attempt 를 보고*:
  - (i) 이미 알려져 있나? (yes/no/probably yes — paper 인용 가능 시 yes).
  - (ii) 컷 사유는? (방향 자체 / 다음 단계 wall / 기술 부족).
  - (iii) sharp navigation 추정?
- 이 추정 자체가 *틀릴 수 있음* 명시 — specialist 직접 검증 X.

목적: *시간 절약 모드* — 새 시도 전 self-check 으로 시도 자체 cut 가능.