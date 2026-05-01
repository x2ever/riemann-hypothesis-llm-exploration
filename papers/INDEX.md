# Papers Index

> **읽기 프로토콜**: 각 논문에 대해 *결과*뿐 아니라 *저자의 사고 과정 추정*을 기록한다. HARNESS.md §2 참조. **Cross-domain 패스**(HARNESS §6)도 적용한다.

## 상태 범례

- `target` — 다운로드 예정
- `downloaded` — PDF 확보, 미독
- `skimmed` — 훑음 (statement·구조 파악)
- `read` — 읽음
- `digested` — 사고 과정·일반화·cross-domain 정리 완료

## 카테고리 약자

- **FND** — 기초/원본 (Riemann 1859, Hadamard, de la Vallée Poussin)
- **REV** — 종합 리뷰
- **ANA** — 해석적 (Hardy–Littlewood, Selberg, Levinson, Conrey)
- **RMT** — Random Matrix Theory (Montgomery, Odlyzko, Keating–Snaith)
- **ADL** — Adelic / Connes / NCG
- **DBN** — de Bruijn–Newman 상수 (Newman, Tao, Rodgers)
- **HP**  — Hilbert–Pólya 류 (spectral 해석)
- **NUM** — 수치 검증, 알고리즘 (Odlyzko–Schönhage, Platt)
- **CLY** — Clay 공식 문제 statement
- **NEG** — 잘못된/철회된 시도 (배움 자료)

---

## 다운로드 완료 (8편)

### [riemann1859] Riemann, "On the Number of Prime Numbers less than a Given Quantity" (1859, Wilkins 영역)
- **상태**: read
- **카테고리**: FND
- **파일**: `pdf/riemann1859_wilkins.pdf` (117 KB)
- **출처**: maths.tcd.ie/pub/HistMath (Wilkins 1998 영역)
- **읽기 우선순위**: ★★★ (모든 것의 출발점)
- **사고 과정 추정**:
  - **출발점**: Euler product = Dirichlet series 라는 사실. 1859년 Cauchy 의 복소 함수론이 정착되어 *적분 표현* 으로의 확장이 자연스러움.
  - **핵심 도약 1**: 함수방정식 도출에 *Jacobi theta 함수* 사용 (1829 Jacobi Fund. §184 인용). 정수론 ↔ theta 함수 ↔ Mellin transform 다리 — 다른 분야 도구 *수입* 의 시초.
  - **핵심 도약 2**: ξ(t) := s(s−1) Π(s/2−1) π^(−s/2) ζ(s) (s=1/2+ti) 로 *변수 변환* — 대칭축을 명시적으로 만들고 *실/짝함수* 임을 드러냄. 이 한 줄이 Hilbert–Pólya 직관의 씨앗.
  - **막혔던 곳**: "그러나 더 엄밀한 증명이 바람직하다; 본 연구의 다음 목표에는 불필요해 보여 잠시 보류" (자필). 본인이 시도하다 막힌 흔적.
  - **버려진 시도**: 명시되지 않으나 ξ(t) Hadamard product 의 모든 영점이 실수임을 *직접* 보이려 했을 것. (Siegel 의 Nachlass 분석으로 Riemann–Siegel formula 발굴 — Riemann 은 *수치 검증* 까지 했음.)
  - **메타 학습**: 본 논문은 *9 페이지에 8개의 새 아이디어* 를 압축. 각 아이디어가 그 자체로 separate 분야의 시작이 됨. RH 자체는 *지나가는 추측* 이고 본 논문의 진짜 목표는 *explicit formula for π(x)*. 우리 시도 시 시사점: RH 를 *직접 푸는 것이 아니라 다른 큰 그림의 부산물* 로 풀릴 가능성.

### [bombieri-clay] Bombieri, "Problems of the Millennium: The Riemann Hypothesis"
- **상태**: read
- **카테고리**: CLY / REV
- **파일**: `pdf/bombieri_clay.pdf` (155 KB)
- **출처**: claymath.org 공식 problem statement
- **읽기 우선순위**: ★★★ (공식 정의 + 알려진 결과 요약)
- **사고 과정 추정**:
  - **Bombieri 의 강조점 선택**: 본 문서는 *정의* 가 형식이지만 §IV "varieties over finite fields" 에 가장 큰 분량 — Bombieri 는 RH 의 *진짜 어려움* 이 number field 측에서 *function field 측의 cohomology + Frobenius + index theorem 대응물 부재* 라고 본다.
  - **결론적 질문 (§V 끝)**: "Is there a theory in the global case, playing the same role as cohomology does for Zeta functions of varieties over a field of positive characteristic?" — 이 한 문장이 본 문서의 *진짜* statement of difficulty.
  - **언급되지 않은 것**: 해석적 (Conrey 류 mollifier) 은 §III 에서 짧게만. Bombieri 는 본 영역이 RH 본질에 닿지 않는다고 보는 듯.
  - **신뢰의 근거**: §III "evidence" 에서 RH 신뢰 근거를 셋으로 정리 — (i) 수치 검증 (ii) 함수체 측의 정확한 유사 정리 (iii) RMT 정합성. (i)+(iii) 은 *실증적*, (ii) 가 *구조적* — 후자가 핵심.
  - **메타 학습**: Clay 공식 문서는 *문제 정의 + 알려진 결과 + 본질적 어려움* 의 균형있는 입문서지만 *증명 전략* 은 거의 다루지 않음 — 그건 의도적. 우리 시도 시 본 문서를 *base camp* 로.

### [conrey2003] Conrey, "The Riemann Hypothesis" (Notices AMS, 2003)
- **상태**: read
- **카테고리**: REV / ANA
- **파일**: `pdf/conrey2003_notices.pdf` (383 KB)
- **출처**: ams.org/notices/200303/fea-conrey-web.pdf
- **읽기 우선순위**: ★★★ (접근법 종합 리뷰의 정수)
- **사고 과정 추정**:
  - **Conrey 의 핵심 시각** (결론 §): "RH 는 진정한 *arithmetic* 질문이고 *해석학* 도구로는 풀리지 않을 가능성 — *families of L-functions* 를 봐야 진전 가능". Bombieri 와 같은 결론 (function field 측의 산술 구조).
  - **무게 분배의 신호**: Pólya analysis (Φ Fourier transform, Mellin) 와 Selberg trace, 각각 한 섹션 — Conrey 는 spectral 채널 자체는 *시도 가치* 인정. RMT 와 families 에 가장 큰 분량 — 이게 그의 *현재 가는* 방향.
  - **흥미로운 confession**: "There is a growing body of evidence indicating that one needs to consider families of L-functions in order to make progress on this difficult question" — Iwaniec 의 가족 + Landau–Siegel 제거 프로그램에 동조.
  - **버려진 (또는 보수적인) 채널**: NCG / function field 직접 시도는 짧게만. "전혀 다른 새 아이디어가 필요할 수도" — 즉 그도 *현재 도구* 로는 안 풀린다고 봄.
  - **메타 학습**: Conrey 는 *직접 풀려는* 사람보다는 *어디 갈 수 있는지 지도 그리는* 사람의 시각. 본 리뷰는 specialist 패널 S1 (해석적 정수론) 의 시각을 가장 잘 보여주는 자료.

### [connes1999] Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function" (1999)
- **상태**: downloaded (서론 추정 — full read 는 시도 시)
- **카테고리**: ADL / HP
- **파일**: `pdf/connes1999_ncg_trace.pdf` (508 KB)
- **출처**: arXiv:math/9811068
- **읽기 우선순위**: ★★ (NCG 접근의 출발점)
- **사고 과정 추정**:
  - **출발점 가설**: Connes 가 NCG 의 창시자 — type III factor, idele class group, KMS state 같은 *자기 분야 도구* 가 RH 의 *spectral* 측면에 자연 적용 가능하다는 직관.
  - **핵심 도약**: idele class group $C_K = A_K^* / K^*$ 위의 action 으로 *adelic spectral 해석* 구성. number field 의 *모든 자리 (place) 를 동시* 에 본다는 점이 핵심 — function field 측의 *closed point set* 의 number field 대응.
  - **현재 한계** (Conrey 2003 평): trace formula identity 는 RH 와 *동치* 변형 — 한쪽 (Weil distribution 양정치성) 을 *독립적* 으로 증명해야 RH ⇒. 이 양정치성이 곧 본 프로그램의 핵심 미해결.
  - **버려진 시도 추정**: Connes 는 처음 *직접 자기수반 H 구성* 을 시도했을 것. 그러나 type II_1 trace 의 well-definedness 가 RH 와 등가임을 깨닫고 *trace 항등식* 으로 우회.
  - **메타 학습**: 본 논문은 *NCG 의 도구 입력* 자체가 RH 본질에 어떻게 접근하는지 보여주는 patterning template. 다만 *외부에서* 정량 평가는 어려움 (Connes 의 specialist 영역).

### [rodgers-tao2020] Rodgers & Tao, "The de Bruijn–Newman constant is non-negative" (2020)
- **상태**: read
- **카테고리**: DBN
- **파일**: `pdf/rodgers_tao_2020_dBN.pdf` (492 KB)
- **출처**: arXiv:1801.05914
- **읽기 우선순위**: ★★★ (최근 메이저 결과)
- **사고 과정 추정**:
  - **출발점**: Newman 1976 의 Λ ≥ 0 추측. Csordas–Smith–Varga 의 zeros 동역학 (5): ∂_t x_k = 2 Σ_{j≠k} 1/(x_k − x_j) — Coulomb-type repulsion. 이 ODE 가 *log-gas* 또는 Calogero 시스템과 동형.
  - **핵심 도약 1**: Λ < 0 가정 → "zeros 가 너무 균등 spaced (arithmetic progression-like)" 결론 → Montgomery pair correlation 과 모순. *반대 가정에서 모순* 의 backward 시각.
  - **핵심 도약 2**: Hamiltonian H(t) = Σ log(1/|x_j − x_k|) 형식적 + 단조 감소 ∂_t H = −4E. *gradient flow* 시각으로 동역학 정량화.
  - **도구 임포트**: 통계물리 *log-gas* 의 *local equilibrium* 개념 + Bourgain pigeon-hole + saddle point method (Stirling) — 다양한 분야 도구의 *조합*. Tao 의 시그니처 스타일.
  - **막혔던 곳 (저자 인정)**: "without GUE, narrow gap upper bounds 가 부족" — strategy 가 일단 *unconditional* 로 가려면 weaker tool 만 가능. relaxation to local equilibrium 으로 우회.
  - **왜 Λ ≤ 0 은 안 풀리는가**: paper 자체에서 명시 X 이나 명백 — backwards heat flow 에서 zero 가 *repel*, forwards 에서 *cluster*. Λ ≥ 0 은 backward 비교, Λ ≤ 0 (=RH) 은 forward control 필요. forward 는 일반적으로 *expansion / clustering* 으로 정량 통제 어려움.
  - **메타 학습**: Tao 류 hard analysis 가 RH 의 *부분적* 결과 (Λ ≥ 0) 까지는 도달했지만 *비대칭의 본질 — 시간 방향* 이 남은 게임. 우리 시도 시 *forward* time control 도구가 cross-domain 에서 (예: optimal transport, Ricci flow) 있는지 검색 가치.

### [platt-trudgian2021] Platt & Trudgian, "The Riemann hypothesis is true up to 3 · 10^12" (2021)
- **상태**: read
- **카테고리**: NUM
- **파일**: `pdf/platt_trudgian_2021_3e12.pdf` (130 KB)
- **출처**: arXiv:2004.09765
- **읽기 우선순위**: ★ (수치 검증 SOTA — 증명 도구 X, 신뢰도 background)
- **사고 과정 추정**:
  - **저자 동기**: 다른 explicit 정수론 정리 (prime bounds, zero-free region, π(x) − Li(x) 부호 변화) 가 *영점 검증 한계 H* 에 직접 의존 — H push 자체가 다른 정리들의 정량 개선으로 즉시 전이.
  - **방법론 (단순)**: Riemann–Siegel + *interval arithmetic* (Arb 라이브러리). Sign change counting + Turing's method (모든 예상 영점 검출 보장).
  - **핵심 도약 (이번 논문)**: 정밀도를 *isolated zero 위치까지* 가지 않고 *sign change 만* 검출 — 계산량 절약. Gourdon 2004 (interval arithmetic 없는) 보다 22% 더 높이.
  - **버려진 야망 (추정)**: 더 높은 H 를 위해 GPU / 분산 컴퓨팅 시도 가능했을 것. 본 논문은 *rigorous 단계* 에 집중 (이전 결과들은 publication 부족).
  - **부산물 (Corollary)**: ψ(x) − x ≤ √x log²x/(8π) up to 2.169·10^25 — explicit prime bound. Λ ≤ 0.2 (de Bruijn–Newman).
  - **메타 학습**: 수치 검증은 *영원히 RH 못 푼다*. 그러나 H 가 큰 정도는 *반례 후보의 lower bound* + 다른 explicit 정리의 *constant 강화* — 두 의미 모두에서 가치. 우리 시도에서 이 H = 3·10^12 를 *sanity check* baseline 으로 사용.

### [bender-brody-mueller2017] Bender, Brody, Müller, "Hamiltonian for the zeros of the Riemann zeta function" (2017)
- **상태**: read
- **카테고리**: HP
- **파일**: `pdf/bender_brody_mueller_2017_hamiltonian.pdf` (135 KB)
- **출처**: arXiv:1608.03679 (PRL 2017)
- **읽기 우선순위**: ★★ (구체적 Hilbert–Pólya 시도, 비판적 검토 필요)
- **사고 과정 추정**:
  - **출발점**: Berry–Keating "H = xp" 의 양자화 후보 (오랜 미해결). Bender 자신의 *PT-symmetric quantum mechanics* (비-Hermitian 인데 실수 스펙트럼 가능) 도구 임포트.
  - **핵심 구성**: Ĥ = (1−e^(−ip̂))^(−1) (x̂p̂ + p̂x̂) (1−e^(−ip̂)). Eigenfunctions ψ_z(x) = −ζ(z, x+1) (Hurwitz zeta), eigenvalues i(2z_n − 1). Boundary condition ψ(0) = 0 → spectrum 결정.
  - **저자 인정 한계 (직접 인용)**: "We are not yet able to prove that the eigenvalues of Ĥ are real". 즉 *self-adjointness rigorous 증명 부재*. Pseudo-Hermiticity 변환으로 metric inner product 도입 시도 — heuristic.
  - **순환 위험 (우리 평)**: ψ_z(x) = −ζ(z, x+1) 가 boundary condition ψ(0) = 0 을 만족하려면 z 가 ζ 영점이어야 함. 즉 spectrum 의 멤버십 자체가 *입력으로* ζ 영점을 가정. domain identification 의 *유일성* (RH 와 등가) 이 따로 증명되지 않으면 *trivially equivalent* 위험.
  - **버려진 시도 추정**: 직접 self-adjoint extension 의 deficiency index 분석을 시도했다 막혔을 것. Pseudo-Hermitian 우회.
  - **메타 학습**: 본 논문은 *형식적 일치* 의 강력한 사례 (Berry–Keating 직관의 구체화). 그러나 *rigorous proof* 으로의 갭이 큼. 우리 시도 시 — Ĥ 의 *유한 차원 truncation* 으로 spectrum 수치 비교 가능 (코드 활용 채널).

### [iwaniec_sarnak_perspectives_2000] Iwaniec & Sarnak, "Perspectives on the Analytic Theory of L-Functions" (2000)
- **상태**: downloaded (정독은 후속)
- **카테고리**: REV / ANA
- **파일**: `pdf/iwaniec_sarnak_perspectives_2000.pdf` (10.7 MB — 큰 paper)
- **출처**: IAS publications
- **읽기 우선순위**: ★★★ (analytic 정수론 + L-function 종합 review)
- **사고 과정 추정 (TODO)**: Iwaniec + Sarnak 가 분야 전체 시각 — L-functions 의 central problems + 도구 + outlook. Bombieri Clay 와 함께 *baseline*.

### [lagarias_sharpenings_li] Lagarias, "Sharpenings of Li's Criterion" (2006)
- **상태**: downloaded
- **카테고리**: ANA / Li 동치
- **파일**: `pdf/lagarias_sharpenings_li.pdf` (174 KB)
- **출처**: arXiv:math/0506326
- **읽기 우선순위**: ★★ (Li 동치의 정량 sharpening)
- **사고 과정 추정 (TODO)**: Li 1997 의 λ_n ≥ 0 동치 의 정량 향상. attempt 001 (li_rmt) 의 후속 시도 기반.

### [sekatskii_generalized_bombieri_lagarias] Sekatskii, "Generalized Bombieri-Lagarias' Theorem and Generalized Li's Criterion" (2014)
- **상태**: downloaded
- **카테고리**: ANA / Li 동치
- **파일**: `pdf/sekatskii_generalized_bombieri_lagarias.pdf` (113 KB)
- **출처**: arXiv:1304.7895
- **읽기 우선순위**: ★ (Li 동치 일반화)

### [lagarias_li_coefficients_automorphic] Lagarias, "Li Coefficients for Automorphic L-Functions" (2004)
- **상태**: downloaded
- **카테고리**: ANA / VIII families
- **파일**: `pdf/lagarias_li_coefficients_automorphic.pdf` (413 KB)
- **출처**: arXiv:math/0404394
- **읽기 우선순위**: ★ (Li 동치의 automorphic GL(N) 일반화 — Wall #4 conspiracy 와 연결)

### [polymath15_dbn_upper] D.H.J. Polymath, "Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn-Newman constant" (2019)
- **상태**: downloaded (정독은 후속 시도)
- **카테고리**: DBN
- **파일**: `pdf/polymath15_dbn_upper.pdf` (2107 KB)
- **출처**: arXiv:1904.12438
- **읽기 우선순위**: ★★★ (Wall #2 직접 관련)
- **사고 과정 추정 (TODO)**: Polymath 협력 — Tao 의 backward analysis 위에서 *effective* (정량) heat flow 도구로 Λ ≤ 0.22. 계산 + theoretical bound. 우리 attempt 006 의 ∫E(t)dt 와 직접 연관 — 정독 시 그 bound 의 *어디가 sharp 한지* 발굴.

### [pratt_robles_2019_5_12] Pratt, Robles, Zaharescu, Zeindler, "More than five-twelfths of the zeros of ζ are on the critical line" (2019)
- **상태**: downloaded (정독은 후속 시도)
- **카테고리**: ANA / mollifier
- **파일**: `pdf/pratt_robles_2019_5_12.pdf` (2485 KB)
- **출처**: arXiv:1802.10521
- **읽기 우선순위**: ★★ (Wall #3 SHARP-CONSTANT 의 SOTA 갱신)
- **사고 과정 추정 (TODO)**: Bui–Conrey–Young 41% 위에서 5/12 (≈ 41.667%). Kloosterman sums 의 평균 + longer mollifier — Wall #3 의 점진적 push 의 가장 최근 단계. 정독 시 50% 벽이 *왜* 그렇게 sharp 한지 이해.

### [sierra_2016_riemann_zeros_spectrum] Sierra, "The Riemann Zeros as Spectrum and the Riemann Hypothesis" (2016)
- **상태**: downloaded (정독은 후속 시도)
- **카테고리**: HP / spectral
- **파일**: `pdf/sierra_2016_riemann_zeros_spectrum.pdf` (2083 KB)
- **출처**: arXiv:1601.01797
- **읽기 우선순위**: ★★ (Wall #5 직접 관련, H=xp 후속)
- **사고 과정 추정 (TODO)**: Berry–Keating 후속 — Sierra 의 long-term 프로그램. attempt 010 (BBM truncation) 시 비교 대상.

### [sierra_2007_hxp_interaction] Sierra, "H = xp with interaction and the Riemann zeros" (2007)
- **상태**: downloaded (정독은 후속 시도)
- **카테고리**: HP / spectral
- **파일**: `pdf/sierra_2007_hxp_interaction.pdf` (436 KB)
- **출처**: arXiv:math-ph/0702034
- **읽기 우선순위**: ★ (Berry–Keating 의 직접 후속, interaction term 추가)
- **사고 과정 추정 (TODO)**: H = xp 의 *interaction term* 첨가로 Berry–Keating 의 한계 (smooth count 만, 실제 영점 X) 우회 시도. 어떤 형태의 interaction 이 영점 정합 만드는가가 핵심.

### [connes-consani2021] Connes & Consani, "Spectral triples and zeta cycles" (2021)
- **상태**: downloaded (full read 는 시도 시)
- **카테고리**: ADL / HP
- **파일**: `pdf/connes_consani_2021_zeta_cycles.pdf` (2.6 MB)
- **출처**: arXiv:2106.01715
- **읽기 우선순위**: ★★ (Connes 프로그램 최신)
- **사고 과정 추정 (서론 + 메타 추정)**:
  - **1999 → 2021 진화**: 1999 의 trace formula 가 *형식 동치* 였다면, 2021 는 *low-lying ζ 영점이 spectral triple 의 spectrum 과 정합* 함을 *수치까지* 보여주는 단계. 즉 Connes 도 본인 program 이 *직접 RH 증명* 보다는 *증거 축적 + 구조 명료화* 의 단계임을 인정.
  - **핵심 새 객체 후보**: "zeta cycle" — function field 측의 closed point cycle 의 number field 대응 후보. parameter λ, k 에 의존 — 즉 *family* 시각.
  - **저자 시각 추정**: Connes 는 RH 가 *NCG 가 충분히 발달하면 자연 결론* 이라고 봄. 그러나 충분히 발달하는 게 *언제* 일지에 대해선 회의적. 전 생애 program 으로.
  - **메타 학습**: 본 논문은 NCG 프로그램의 *현재 상태* 를 보여주는 marker. specialist 패널 S3 (NCG·작용소대수) 호출 시 본 논문이 baseline.

---

## 추가 다운로드 방법

새 논문이 필요하면 `WISHLIST.md` 에 먼저 적고, 다음 명령으로 다운로드:

```bash
cd tools
uv run python fetch_paper.py arxiv <id> --key <key>
uv run python fetch_paper.py url "<URL>" --key <key>
```

다운로드 후 stdout 의 스텁을 본 INDEX.md `## 다운로드 완료` 섹션에 붙이고 *카테고리/우선순위/사고 과정 추정* 채움.

---

## 다운로드 예정 (target)

### [conrey1989] Conrey, "More than two fifths of the zeros are on the critical line"
- 상태: target (저널 PDF 무료 X — 후속 논문/리뷰로 보완)
- 카테고리: ANA / mollifier

### [montgomery1973] Montgomery, "The pair correlation of zeros of the zeta function"
- 상태: target

### [keating-snaith2000] Keating & Snaith, "Random matrix theory and ζ(1/2 + it)"
- 상태: target
- 카테고리: RMT

### [katz-sarnak] Katz & Sarnak, "Zeroes of zeta functions and symmetry"
- 상태: target
- 카테고리: RMT / REV

### [berry-keating1999] Berry & Keating, "H = xp and the Riemann zeros"
- 상태: target
- 카테고리: HP

### [iwaniec-perspectives] Iwaniec, "Perspectives on the analytic theory of L-functions"
- 상태: target
- 카테고리: REV / ANA

### [atiyah2018] Atiyah, "The Riemann Hypothesis" (preprint, 2018) — 실패 사례
- 상태: target
- 카테고리: NEG
- 메모: 즉시 결함 지적된 시도. 좋은 *반면교사* — 학습 자료.

### [selberg-trace] Selberg trace formula 원본 + 현대 해설
- 상태: target

### [deninger] Deninger, "Some analogies between number theory and dynamical systems on foliated spaces"
- 상태: target

### Function field 측 — Weil 1948 RH for curves over finite fields
- 상태: target (Weil's resolution of function field analog — 핵심 비교 대상)

---

## 책 (PDF 무료 X — background/ 에 핵심만 옮김 예정)

- Edwards, *Riemann's Zeta Function* (Dover) — 표준 입문
- Titchmarsh, *The Theory of the Riemann Zeta-function* — 고전 reference
- Iwaniec & Kowalski, *Analytic Number Theory* (AMS Colloquium 53)
- Iwaniec, *Lectures on the Riemann Zeta Function*
- Karatsuba & Voronin, *The Riemann Zeta-Function*

---

## Read 순서 제안

1. **bombieri_clay** (공식 statement, 1순위)
2. **conrey2003_notices** (접근법 지도)
3. **riemann1859_wilkins** (원본)
4. **rodgers-tao2020** (최근 메이저 결과 + Tao 사고 패턴)
5. **connes1999** → **connes-consani2021** (NCG 진화)
6. **bender-brody-mueller2017** (구체적 HP 후보, 비판적)
7. **platt-trudgian2021** (수치 SOTA — 빠르게 훑음)
