# Open Question: Levinson-Durbin ↔ Levinson Mollifier Correspondence? — **RESOLVED (Negative)**

> **Source**: attempt 015 (proposed) + attempt 016 (resolved negative).
> **Status**: ~~Open question~~ → **Closed (negative)**. 수학적 동치 X.

## RESOLUTION (attempt 016)

**Hypothesis H1**: Levinson-Durbin recursion ≡ Levinson 1974 mollifier 의 arithmetic generalization?

**Answer**: **NO**.

**Reason**:
- Levinson-Durbin: Toeplitz matrix $T_{ij} = r_{|i-j|}$, *translation invariant*.
- Mollifier quadratic form: $T_{mn} = \sum_{hm=kn} \mu(h)\mu(k) / (\cdots)$, *prime-factorization-dependent*.
- Mollifier 행렬은 translation invariance X — Levinson-Durbin 의 핵심 가정 위배.

**Closure**: 두 algorithm 의 *이름 공유* 는 동일인 N. Levinson 의 두 *별개* 작업. 직접 mathematical equivalence 미존재. 더 abstract framework (positive definite kernel inversion 등) 에서 *각각 사례* 일 수 있으나 *직접 다리* X.

[rigorous] 본 closure.

---

## Original (15) Background

## Background

N. Levinson (1912~1975) 의 두 작업:
- 1947: Levinson-Durbin recursion (signal processing) — Toeplitz matrix inversion + AR model.
- 1974: Mollifier method (analytic number theory) — ratio of zeros on critical line.

Pratt-Robles 2019 (arXiv:1802.10521 §1.2): "there does not seem to be a random matrix analogue of mollifying as there is nothing that naturally corresponds to a partial Dirichlet series."

이는 *RMT 측에서 mollifier 대응 부재* 의 직접 인정. 가능성: *signal processing AR model* 측 대응이 있을 수 있다.

## Hypothesis

**Mollifier method (1974) 의 *수학적 본질* 이 Levinson-Durbin recursion (1947) 의 *infinite-dimensional / arithmetic generalization* 인가?**

구체적 sub-questions:

(Q1) Mollifier coefficient optimization $\min_a \int |\zeta(\frac{1}{2}+it) M_a(\frac{1}{2}+it)|^2 \,dt$ 가 *어떤 quadratic form* 의 minimization 인가? 그 행렬이 *Toeplitz* 또는 *Toeplitz-like*?

(Q2) Mollifier 의 *arithmetic structure* (μ, Λ, Dirichlet conv) 가 AR model 의 *signal autocorrelation* 와 *대응* 인가?

(Q3) Levinson-Durbin recursion 의 *order-recursive* 성질이 mollifier 길이 $y = T^\theta$ 의 push (Conrey 의 $\theta = 4/7$) 와 관련?

(Q4) Reflection coefficient $|k_n| < 1$ 같은 *stability constraint* 가 mollifier 의 sharp constant (50% wall) 의 변형?

## Status (외부 비판 honest 인정)

- (Q1)~(Q4) 답이 *yes* 이면: signal processing 의 *Yule-Walker, AR identification, lattice filter* 등이 mollifier 분야에 import.
- 답이 *no* (이름만 공유): bridge 부재.
- **현재 답을 *모름***. literature 검색 negative 이지만 검색 한계 가능성.
- 본 lemma 는 *open question* — 진짜 lemma 가 아님.

## 검증 path (예정)

- 016: Pratt-Robles §3 (mollifier 구성) 깊이 정독 — coefficient recursion 확인.
- 017: signal processing literature 에서 *arithmetic generalizations of Levinson-Durbin* 검색.
- 018: 만약 (Q1) yes 라면 — quadratic form 행렬 explicit 형태 작성, Toeplitz 검증.

## 만약 *yes* 라면 (가상 진전)

- Wall #3 (SHARP-CONSTANT) 우회: signal processing 의 *adaptive filter* 또는 *spectral estimation* 도구로 50% 벽 push.
- *RH 우회* X — Wall #3 push 는 100% 까지 가도 RH 직접 증명 X (모든 영점 보장 없음, 알려진 한계).

## 만약 *no* 라면 (likely)

- 두 Levinson 의 이름 일치는 *동명이인 / 동일인 우연*.
- 본 open question 종료, lemmas/ 에 *negative 결론* 으로 archive.

## Caveats

- 외부 critique trigger: 본 hypothesis 가 *예상 가능* + *novel mathematical content X* 위험.
- 만약 *형식 일치* 만 발견되고 *수학 동치* 미증명 시 lemma X — open question 으로 archive.
- 본 file 자체는 *프로세스 lemma* — 향후 시도들의 입력 record.

## Dependencies / Where Used

- Source: pratt_robles_2019_5_12 (papers/pdf/), Pratt-Robles paper §1.2 quote.
- 적용 lens: `lemmas/spectral_candidate_circularity_check.md` (trivial vs non-trivial 분리).
- 향후 시도 016, 017, 018 의 입력.
