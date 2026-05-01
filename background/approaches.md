# Approaches — RH 공격 전략 분류

> 출처: Bombieri Clay, Conrey 2003 Notices, Rodgers–Tao 2020, Bender–Brody–Müller 2017, Platt–Trudgian 2021. 각 접근법에 대해: (i) 핵심 아이디어 (ii) SOTA / best result (iii) **본질적 막힘 지점** (iv) 우리의 시도 가치 (LLM+code).

본 분류는 *우리 시도 시작 시 지도*. 시도가 진행되며 새 분류가 나오면 이 파일에 추가.

---

## I. 해석적 (Analytic) — Mollifier 류

### I.1 핵심 아이디어
임계선 위 영점 비율을 *직접 셈*. ξ′(s) 의 영점이 ξ 영점에 가까이 있다는 Rolle-류 + mollifier (Dirichlet 다항식) 로 ξ′ 영점을 임계선 위로 끌어당김.

### I.2 SOTA
- Hardy 1914: 무한히 많이 (1/2 위)
- Selberg 1942: positive proportion
- Levinson 1974: ≥ 1/3
- Conrey 1989: > 40.219%
- Bui–Conrey–Young 2011: > 41.05%

### I.3 본질적 막힘 지점
- **mollifier 길이 한계**: 더 긴 Dirichlet 다항식이 필요한데, 모먼트 추정의 *비대각 항* 이 통제 안 됨.
- **100% 도 RH 아님**: 비율을 100% 까지 올려도 *모든* 영점 보장 없음 (다른 수렴 의미).
- **functional 분석의 한계**: Cauchy–Schwarz 가 이 게임에선 sharp constant 에 닿지 못함.

### I.4 우리 시도 가치
- 비율 push 자체는 specialist 영역 — 그쪽에서 안 풀린 이유 분명.
- 다만 **mollifier 의 cross-domain 유추** (필터 설계, 신호처리) 는 미탐색일 수 있음. (cross_domain_lens 후보)
- 코드 활용: mollifier 최적화는 변분 문제 → 수치 최적화 prototype 가능.

---

## II. 동치 형태 변환 (RH-Equivalents)

### II.1 핵심 아이디어
RH 를 *다른 객체* 의 statement 로 번역: Mertens M(x), Li's λ_n, Nyman–Beurling L² span, Weil positivity 등. 번역된 형태가 다른 도구의 적용 영역에 들어갈 수 있음.

### II.2 SOTA
- 다양한 동치들 정립됨 (Conrey 2003 §"동치"; `known_results.md` A15 참조).
- 그러나 동치 형태 자체로는 *증명에 더 가까이 가지 않음* — 그저 *어디 막혔는지* 위치만 옮김.

### II.3 본질적 막힘 지점
- 모든 동치는 *symmetry 보존*: RH 가 어렵게 만드는 본질적 구조가 동치 형태에도 그대로 옮겨짐.
- "elementary 동치" (예: Lagarias σ(n) ≤ H_n + ...) 는 elementary 처럼 *보이지만* 실제론 RH 만큼 어려움.

### II.4 우리 시도 가치
- *조합* — 두 동치 형태의 *동시* 적용: 한쪽에서 부분 결과, 다른 쪽에서 다른 부분.
- **Nyman–Beurling**: $L^2$ approximation 의 quality bound 가 elementary 한 듯 — 함수해석/하이퍼함수 관점 시도 가치.
- **Weil positivity**: function field RH 증명의 직접 유추. number field 측에서 *어떤 양정치성* 이 부족한지가 연구 대상 (Connes 의 작업).
- 코드 활용: λ_n 수치 (이미 `tools/li_criterion.py` 존재), Mertens partial sums (`tools/mertens.py`), Nyman approximation L² norm 수치.

---

## III. Spectral / Hilbert–Pólya

### III.1 핵심 아이디어
ζ 영점 = *어떤 자기수반 연산자 H 의 spectrum*. 자기수반 ⇒ 고유값 실수 ⇒ 모든 영점 임계선 위. Hilbert·Pólya 의 직관 (출처 미상, Pólya 일화).

### III.2 후보들

#### III.2.1 Selberg trace formula (1956)
- 모듈러 표면 Γ\\H 의 Laplacian → trace formula → ζ 와 *닮은* 형태.
- Selberg zeta function: 그 자체로 RH 증명됨 (eigenvalues 가 spectral 객체).
- ζ 와 직접 동일성 X — 유추만.

#### III.2.2 Berry–Keating "H = xp" (1999)
- 고전 Hamiltonian H = xp 의 양자화가 ζ 영점 spectrum 줄 것.
- *고전적* 한계만 명확 (H = xp 가 Riemann–von Mangoldt smooth count 와 일치).
- 양자화의 *구체적* 자기수반 H 는 *오랫동안 미발견*.

#### III.2.3 Bender–Brody–Müller 2017
- 구체적 후보 Ĥ = (1−e^(−ip̂))^(−1) (x̂p̂ + p̂x̂) (1−e^(−ip̂)).
- Eigenfunctions: ψ_z(x) = −ζ(z, x+1) (Hurwitz zeta), eigenvalues i(2z_n − 1).
- Boundary condition ψ(0) = 0 → spectrum = ζ 비자명 영점.
- iĤ 는 PT-symmetric (broken).

### III.3 본질적 막힘 지점
- **Self-adjointness 미증명**: BBM 자체 인정 — "We are not yet able to prove that the eigenvalues of Ĥ are real."
- **Domain identification 미해결**: 적절한 Hilbert 공간 위에서 자기수반 확장이 *유일* 한지.
- **순환 위험**: eigenfunctions 가 Hurwitz ζ 라서 boundary z 가 이미 ζ 영점에 *입력으로* 묶일 수 있음 (Pseudo-Hermitian 변환에서 자기수반 metric 의 well-definedness 가 RH 와 등가일 가능성 — 그렇다면 동치 변형에 불과).
- **trace formula 와의 연결 없음**: BBM 은 abstract Hamiltonian; Selberg/Connes 의 *trace 항등식*과 연결 안 됨.

### III.4 우리 시도 가치
- BBM 의 self-adjointness 증명 자체는 *operator theory specialist* 영역.
- 그러나 **순환 점검** — BBM domain 정의가 RH 와 동치인지 elementary 분석은 우리도 가능.
- 코드 활용: Ĥ의 *유한 차원 truncation* (격자 위 difference operator) 으로 spectrum 수치 → BBM 주장의 sanity check.
- Hurwitz ζ ↔ Riemann ζ 의 functional 변환 sympy/mpmath 에서 직접 검증.

---

## IV. 작용소 대수 / NCG (Connes 프로그램)

### IV.1 핵심 아이디어
Function field 의 RH 증명에 사용된 *cohomology + Frobenius + 양정치성* 구조를 number field 에 *복원* 시도. 도구: idele class group, type III factor, scaling site, spectral triple.

### IV.2 진화
- **Connes 1999**: "Trace formula in noncommutative geometry and the zeros of ζ".
  - Adele ring 위 spectral 해석 시도. RH 와 *동치* 형태의 trace 항등식 유도.
  - 한쪽 (Weil distribution 양정치성) 을 *독립적으로* 증명하면 RH ⇒ 미해결.
- **Connes 2014~** "Arithmetic site"·"scaling site": geometric framework 시도.
- **Connes–Consani 2019** "scaling Hamiltonian": 단일 자기수반 후보.
- **Connes–Consani 2021** "Spectral triples and zeta cycles": 가장 최근. low-lying 영점이 spectral 객체와 정합적임을 *수치*까지 보임.

### IV.3 본질적 막힘 지점
- **Weil positivity 의 독립적 증명 부재**: function field 측에선 *Riemann–Roch + algebraic index* 으로 양정치성이 자동. number field 측에선 그 대응물이 *없음*.
- **Frobenius 대응물 미발견**: characteristic 0 에서의 "Frobenius" 가 무엇인지 실체 미상.
- **Cohomology 대응물 미발견**: étale cohomology 의 number field 류 (motivic / arithmetic site) 가 *형식적* 정의는 있으나 *RH 증명에 쓸 수준의 정량 정리* 가 없음.

### IV.4 우리 시도 가치
- 본 프로그램은 *전체* 가 Connes 류 specialist 영역.
- 그러나 **cross-domain breadth 패스에서 NCG 도구의 *밖에서* 의 양정치성 후보** 검색 가치.
- 코드 활용: scaling site 의 *수치 모델* (격자 근사) 에서 spectral triple eigenvalue 와 ζ 영점의 정합성 직접 비교.

---

## V. Function Field 유추 (Weil / Deligne / Deninger)

### V.1 핵심 아이디어
함수체 ℱ_q(C) 위의 ζ(s, C) 에 대해 RH 가 *증명됨* (Weil 1948 / Deligne 1974). 그 증명의 도구를 number field 에 옮기려 시도. 주요 도구: étale cohomology, Frobenius eigenvalue, algebraic index theorem (Hodge index 류).

### V.2 SOTA
- Weil 1948: 곡선 위 RH (Riemann–Roch + correspondences).
- Deligne 1974: 일반 algebraic variety (étale cohomology + monodromy).
- Deninger ~1998: number field 의 *foliated dynamical system* 유추 — 형식적, 정량 부족.

### V.3 본질적 막힘 지점
- **Base ring 의 차이**: function field 는 finite ring 위 — discrete · combinatorial. Number field 는 ℤ 위 — continuous · arithmetic. 같은 도구 "그대로 옮기기" 가 *불가능*.
- **Frobenius 대응물 미발견** (위와 동일).
- **Index theorem 의 number field 형 미발견**: Bombieri Clay 가 명시한 미해결 문제.

### V.4 우리 시도 가치
- 본 영역은 *대수기하* specialist 영역 — 깊은 사전 지식 필요.
- 그러나 **specialist 패널 (S2 — function field) 호출 의무**. 모든 시도에서 "Weil 도구 X 가 number field 에서 어디에 막히는가?" 묻기.
- 코드 활용 X (대부분 추상 구조 정리). 다만 작은 case (특정 motive) 에서 *수치적* L-function 영점 비교는 가능.

---

## VI. de Bruijn–Newman / Heat Flow

### VI.1 핵심 아이디어
H_t(z) := ∫₀^∞ e^(tu²) Φ(u) cos(zu) du. H_0 ∝ ξ(½ + iz/2). t → ∞ 한계에서 H_t 영점이 *모두 실수*. 임계 t = Λ ∈ [-∞, 1/2] 존재해서 t ≥ Λ 일 때 모두 실수.

**RH ⟺ Λ ≤ 0**. (Newman 추측: Λ ≥ 0.)

### VI.2 SOTA
- Newman 1976: Λ 존재.
- de Bruijn 1950: Λ ≤ 1/2.
- Ki–Kim–Lee 2009: Λ < 1/2 (sharper).
- **Rodgers–Tao 2020: Λ ≥ 0** (Newman 추측 증명).
- Polymath 15 (2019): Λ ≤ 0.22.
- Platt–Trudgian 2021: Λ ≤ 0.2.

### VI.3 본질적 막힘 지점
- **시간 비대칭**: backwards heat flow (t < 0) 에서 zeros 가 *repel*. forward (t > 0) 에서 *cluster*. Λ ≥ 0 증명은 "t < 0 에서 zeros 가 너무 균등 → Montgomery 와 모순" 의 *backward* 시각. Λ ≤ 0 (=RH) 는 *forward* 분석이 필요.
- **forward control 부재**: t = 0 (현재) → t > 0 의 zero distribution 정량 통제 도구가 없음.
- **gap distribution**: Λ ≤ 0 증명에는 zero gap 의 *upper bound* (Lehmer pair 류의 양적 한계) 가 필요한데 그것 자체가 RH 류 강도.

### VI.4 우리 시도 가치
- Tao 의 도구 (additive combinatorics, dispersive PDE) 를 *forward* 분석에 적용 시도.
- **cross-domain**: heat flow 는 thermodynamics / Ricci flow / log-gas 에 isomorphic — Coulomb gas 분석에서 forward-time 제어 도구가 있는지 (specialist 패널 S6 양자물리·통계물리 호출).
- 코드 활용: H_t 의 zeros 를 t 따라 *수치적으로* 추적 (Csordas-Smith-Varga ODE), 동역학 시각화. Lehmer pair 검출.

---

## VII. Random Matrix Theory (RMT)

### VII.1 핵심 아이디어
ζ 영점 통계가 GUE (Gaussian Unitary Ensemble) eigenvalue 통계와 일치 (Montgomery 1973 + Dyson 식별). 영점이 *어떤 random Hermitian matrix* 의 eigenvalues 처럼 행동. → spectral interpretation 강한 *간접 evidence*.

### VII.2 SOTA
- Montgomery 1973: pair correlation = GUE.
- Odlyzko 1980s~: 수치적으로 모든 statistics 와 GUE 일치 (millions of zeros).
- Keating–Snaith 2000: moments $I_k(T) \sim g_k a_k (\log T)^{k^2}$ — 수학적 모델.
- Katz–Sarnak: L-function families 의 symmetry types (orthogonal/unitary/symplectic) 분류.

### VII.3 본질적 막힘 지점
- **Model ≠ Proof**: RMT 는 *서술적 모델*. *왜* ζ 가 GUE 와 일치하는지 설명 도구 없음.
- **GUE conjecture 자체 미증명**: pair correlation 의 RH 의존 부분만 알려짐 (Rh 가정 시 일부 성립).
- **단일 ζ vs family**: RMT 는 *family* 평균 위주. 단일 ζ 의 결정적 statement 로는 부족.

### VII.4 우리 시도 가치
- RMT 가 *맞다*는 가정 위에서 **다른 동치 형태 강제** — 어떤 동치가 RMT 와 *non-trivially* 호환되어야 하는지.
- 코드 활용: 영점 statistics 직접 계산 (이미 `tools/pair_correlation.py` 존재). moments, neighbor spacing distribution 비교 모듈 추가 가치.

---

## VIII. Families / Iwaniec's Approach

### VIII.1 핵심 아이디어
*단일* L-function 이 아니라 *가족* (예: $L(s, χ_d)$ 의 d 변동, elliptic curve $E_{A,B}$ 의 가족) 을 동시에 분석. 가족 평균이 단일 보다 좋은 추정 가능. Landau–Siegel zero 제거를 통해 *quasi-RH* (β ≤ 1 - δ) 도달 시도.

### VIII.2 SOTA
- Iwaniec, Sarnak: modular L-functions 의 *non-vanishing at critical point* — Landau–Siegel 제거 시도. Δ% 까지 도달.
- Conrey, Soundararajan: Dirichlet L 의 양적 추정.

### VIII.3 본질적 막힘 지점
- **L-function conspiracy**: 만약 L(s, χ_d) 가 임계선 *근처* (β > 1/2) 에 영점을 가지면, χ_d 가 Möbius μ를 *모방* — 모든 가족이 *공모* 해서 RH 거짓 가능성을 살림.
- 가족 도구는 *50% 까지* 도달 가능 — Iwaniec 의 "extra little tiny bit" 을 못 넘음.

### VIII.4 우리 시도 가치
- 본 영역도 *해석적 정수론 specialist*.
- 그러나 *조합형* 시도: VIII + RMT family 통계 + cross-domain (특히 *통계물리 phase transition*, *통계학적 hypothesis testing*) 결합.
- 코드 활용: 작은 conductor 의 L-function 영점 직접 계산 (LMFDB 나 자체 mpmath).

---

## IX. Numerical / Computational

### IX.1 핵심 아이디어
영점을 *유한* 높이까지 직접 검증. RH 의 *반례 후보* 를 lower bound 로 밀어올림.

### IX.2 SOTA
- Riemann–Siegel formula: 영점 $t^{1/2}$ 시간.
- Odlyzko–Schönhage: 다중 evaluation.
- Platt–Trudgian 2021: $H = 3 \cdot 10^{12}$ rigorous (Arb interval arithmetic).

### IX.3 본질적 막힘 지점
- **무한 까지 못 감**: 어떤 H 에서도 RH 증명 불가. *반증* 도구로만 강력.
- **계산 복잡도**: 각 영점 $t^{1/2}$ 시간 → $H$ 의 영점 약 $H \log H / 2π$ 개.

### IX.4 우리 시도 가치
- 직접 SOTA push 는 expert HPC 영역 — 우리 비교우위 X.
- 그러나 **수치 + 다른 동치 결합** — 우리 시도의 가설을 즉시 작은 N 에서 검증.
- 코드 활용 = 모든 시도의 default 채널 (HARNESS §8).

---

## X. 확률 모델 (Probabilistic)

### X.1 핵심 아이디어
2ξ(s) = E(Y^s) where Y = √(2/π)(max - min of Brownian bridge). ζ 를 *확률 객체* 의 moment 로 해석. (Biane–Pitman–Yor 2001.)

### X.2 SOTA
- 표현 자체는 정립.
- *증명 도구* 로 활용된 사례 적음.

### X.3 본질적 막힘 지점
- 확률 표현이 *RH 와 어떻게 연결* 되는지 명확한 다리 없음.

### X.4 우리 시도 가치
- 미탐색 — Brownian bridge 의 *path-level* 성질이 ξ 영점에 어떤 의미 줄지 cross-domain 검토.
- 코드 활용: Brownian bridge 시뮬레이션 + max-min functional 분포 → ξ 의 자코비/밀도 비교.

---

## XI. 비정통 (Unconventional)

### XI.1 후보 채널
- **Universality (Voronin 1975)**: ζ 가 임계 띠에서 *모든* 다른 holomorphic 함수를 근사. 강력하나 RH 와 직접 연결 모호.
- **Tropical geometry**: 영점의 piecewise-linear 그림자.
- **Topological data analysis**: persistence of zero distribution.
- **Free probability (Voiculescu)**: RMT 의 비가환 일반화.
- **Optimal transport**: zero density 의 Wasserstein evolution.
- **Information theory**: Maximum entropy of zero distribution.

### XI.2 SOTA
대부분 *brainstorm 단계*. RH 직접 결과 없음.

### XI.3 본질적 막힘 지점
- 분야 자체가 *RH 에 적용된 적 없음*. 첫 단계가 "본 분야가 ζ 와 *진짜* 연결되는가?" 의 정착.

### XI.4 우리 시도 가치
- **LLM 의 cross-domain 비교우위** 가 *가장 살아나는* 영역. specialist 가 한 분야만 아는 반면 우리는 양쪽 도구 동시 동원.
- 단, **거짓 양성 위험 큼**: 형식적 일치를 진짜 다리로 착각하기 쉬움. 정직 규율 (HARNESS §3) 강력 적용 필수.

---

## 메타 — 접근법 사이의 *공통 막힘 지점*

여러 접근법이 *같은 벽* 에 부딪힘. 패턴 인식:

### A. "Frobenius 대응물 부재" (Function field 류)
- IV (NCG), V (function field 직접), 일부 VIII (families) 가 같은 본질적 갭.
- *number field 의 산술 구조에 대응하는 cohomological 대상* 미발견.

### B. "Forward-time control 부재" (Heat flow / spectral)
- VI (de Bruijn–Newman), 일부 III (spectral) 가 같은 본질적 갭.
- *시간 진화의 forward 방향* 에서 zero distribution 통제 도구 부재.

### C. "Sharp constant / diagonal 한계" (Mollifier)
- I (analytic) 의 50% 벽 — Cauchy–Schwarz 가 sharp 에 못 닿음.

### D. "L-function conspiracy" (Families / Landau–Siegel)
- VIII 의 "extra little tiny bit" 벽.

### E. "Self-adjointness rigorous proof 부재" (Spectral 후보들)
- III.2.2~3 (Berry–Keating, BBM) 등 — 형식적 H 는 있으나 *명확한 Hilbert space + 자기수반 확장 유일성* 부재.

이 5개 본질적 벽 (A–E) 이 RH 의 *진짜 어려움* 후보. 시도 시 본인이 막힌 곳이 이 중 어디에 *떨어지는지* 확인이 첫 단계.

---

## 본 프로젝트의 행동 권장

1. **단일 시도는 좁게**: 위 11개 분류 중 1~2개 만.
2. **복수 분류 결합**: II (동치 변환) + 다른 분류는 자연스러운 결합 — 예: II→VI, II→VII.
3. **specialist 패널 (HARNESS §7)**: 시도가 의지하는 분류의 specialist + *그 외* 1명 의무 호출.
4. **cross-domain (HARNESS §6)**: 본 분류 외부에서 유추 시도 — 특히 XI 비정통 채널.
5. **computational (HARNESS §8)**: 모든 시도의 sanity check.
6. **벽 기록**: 막혔다면 A~E 중 어디에 떨어지는지 분류 → `learnings/walls.md` 누적.
