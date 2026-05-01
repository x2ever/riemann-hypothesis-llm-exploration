# Specialist Round — Attempt 000

> HARNESS §7 의 첫 가동. 각 specialist 는 RH 와 본 *orientation* 시도에 대해 4질문에 답.
> 본 라운드는 *시뮬레이션* — 진짜 전문가 답변 보장 X. 분야-내 정리 인용은 정확한 statement 필수, 모호하면 표시.

---

## S1 — 해석적 정수론자 (Hardy–Selberg–Conrey 라인)

### a. 자명/비자명 분리 (RH 자체에 대해)
- **자명**: 함수방정식, 임계 띠 안 영점, 임계선 위 무한 영점 (Hardy 1914), 비율 ≥ 41.05% 임계선 위 (Bui–Conrey–Young).
- **비자명 도약 1**: 비율을 100% 까지 push — Cauchy–Schwarz 가 sharp 에 못 닿음. mollifier 길이가 길어지면 비대각 항이 폭발.
- **비자명 도약 2**: $S(T) = O(\log T)$ 무조건 — Selberg. RH 가정 시 $S(T) = O(\log T / \log\log T)$. 무조건 형 push 가 막힘.

### b. 사용 가능 도구
- **Mean value theorems**: $\int_0^T |\zeta(\tfrac{1}{2}+it)|^{2k}\,dt$ 추정. $k=1$ (Hardy–Littlewood), $k=2$ (Ingham). $k=3$ 무조건 미해결.
- **Mollifier**: $M(s) = \sum_{n \le N} a_n n^{-s}$ 의 최적 계수 — variational. Sharp constants by Conrey, Soundararajan.
- **Density theorem**: $N(\sigma, T)$ — Carlson, Halász, Heath-Brown, Ingham.
- **Riemann–Siegel**: $\zeta(\tfrac{1}{2}+it)$ asymptotic.
- **Approximate functional equation**: $\zeta(s) = \sum_{n \le X} + \chi(s) \sum_{n \le Y} + \mathrm{error}$.

### c. 분야 내 함정
- **mollifier 길이 환상**: 길이 N 을 늘리면 비율 push 가 자동이라는 착각. 비대각 sum 이 폭발하므로 *nontrivial sum estimate* 이 매번 필요.
- **moment 와 RH 의 거리**: $I_k$ asymptotic 이 RH 자체와 *직접* 동치 아님. moment family 가 *RMT 와 정합* 해도 RH 증명 X.
- **L-function conspiracy**: Landau–Siegel zero 가 *어떤* L-function 가족에 존재하면 *모든* 가족이 그것을 모방 — 한 곳에서 결과를 다른 곳으로 옮길 때 *지속성* 가정에 주의.

### d. 본 분야 한계 신호
- 해석적 도구는 *50% 벽* — Iwaniec 의 "extra little tiny bit" 을 못 넘음.
- Conrey 의 결론 (2003): "RH 는 진짜 *arithmetic* 질문이고 해석 도구로는 풀리지 않을 가능성".
- → RH 의 본질적 어려움은 *해석학 외부* (algebraic, spectral) 에 있다는 신호.

### orientation 시도에 대한 평
- 본 시도의 분류 (`approaches.md` §I) 가 정확. 단, *Iwaniec 가족* 은 §I 와 §VIII 사이에 위치 — 해석적이지만 family 위.
- 권장: 다음 시도들이 *단일* ζ 만 보지 말 것. families view 가 modern 해석적 정수론의 main current.

---

## S2 — 대수기하학자 / Function Field

### a. 자명/비자명 분리
- **자명**: function field 의 RH 는 *증명됨* (Weil 1948 곡선, Deligne 1974 일반).
- **자명**: number field ↔ function field 의 *형식적* 유추 (Hasse, Artin, ..., Iwasawa).
- **비자명 도약 1**: number field 의 cohomology 대응물 — 무엇이고 어떻게 정의되는가?
- **비자명 도약 2**: ℤ 가 ℱ_q[T] 와 다른 *근본적* 이유 — characteristic 0 의 무한 자리, archimedean place.

### b. 사용 가능 도구
- **Riemann–Roch + algebraic index theorem**: function field 측의 양정치성 핵심.
- **Étale cohomology**: $H^i_{\mathrm{ét}}(C, \mathbb Q_\ell)$ 의 Frobenius eigenvalues = ζ(C, s) 영점.
- **Lefschetz fixed point**: trace = number of fixed points.
- **Motivic cohomology** (가설적): Beilinson, Deligne motives.
- **Arithmetic site (Connes–Consani)**: 산술 측의 cohomology 후보.

### c. 분야 내 함정
- **순진한 유추 함정**: "ℤ 를 ℱ_p[T] 처럼 다루자" 는 시도가 잠시 흥분되나 archimedean place (∞) 가 fundamentally 다른 차원 — 무시 시 나중에 *모든 결과가 부정확*.
- **base ring 의 implicit 변경**: function field 도구의 어떤 단계는 *암묵적으로* finite 이라 가정. 이 단계가 number field 에서 어디인지 추적 어려움.

### d. 본 분야 한계 신호
- Bombieri Clay 의 핵심 미해결: "Is there a theory in the global case, playing the same role as cohomology does for varieties over a field of positive characteristic?"
- → 답이 *예* 라면 RH 풀림. 답을 *발견* 하는 것이 본 분야의 게임.

### orientation 시도에 대한 평
- 본 시도의 분류 (`approaches.md` §V) 정확. 그러나 §IV (NCG) 는 §V 의 *번역* 이지 독립 분야 아님. 결합 권장: §IV + §V 동시 호출.
- 권장: function field 측에서 *어느 단계* 가 number field 에서 막히는지 *정확히* 점검 — 막힌 단계가 곧 RH 본질.

---

## S3 — NCG · 작용소대수 (Connes 라인)

### a. 자명/비자명 분리
- **자명**: ζ 의 Hadamard product 는 자기수반 연산자의 spectrum 형식.
- **자명**: Selberg trace formula 가 함수체 측의 explicit formula 와 정합.
- **비자명 도약 1**: number field 위의 *trace 항등식* 자체가 RH 의 *동치 변형* — 항등식의 한쪽 (Weil distribution 양정치성) 을 독립적으로 증명해야 RH ⇒.
- **비자명 도약 2**: 자기수반 H 가 *어떤 Hilbert 공간 위에서* 자연스럽게 정의되는가 — domain identification.

### b. 사용 가능 도구
- **Type III factor + KMS state** (Bost–Connes 시스템).
- **Idele class group $C_K = A_K^*/K^*$**: adelic spectral 해석.
- **Spectral triple $(A, H, D)$**: Connes 의 *비교환 기하* basic object.
- **Weil distribution**: Weil 의 explicit formula 의 *분포* 시각.

### c. 분야 내 함정
- **형식 동치 vs 증명**: trace formula 의 *형식 등식* 자체는 RH 와 동치 *변형* — 더 어려워졌을 수도 있음.
- **type III factor 의 정량 부재**: type III factor 가 well-defined 하나 *수량적* 정리가 거의 없음 — 정성적 도구.

### d. 본 분야 한계 신호
- 25년 (1999~2025) 동안 큰 정량적 진전 없음. 단계적 *명료화* (Connes–Consani 시리즈) 만.
- Connes 본인이 "전 생애 program" 으로 표현 — 빠른 풀이 기대 X.

### orientation 시도에 대한 평
- 본 시도의 분류 (§IV) 정확. 다만 *외부에서* (non-NCG specialist) 본 분야 평가는 어렵다 — Connes specialist depth 호출 의무.
- 권장: 다음 시도들이 NCG 를 *직접 전개* 하기보다는 *조합* (NCG + heat flow, NCG + RMT) 의 가능성 검토.

---

## S4 — RMT / 확률

### a. 자명/비자명 분리
- **자명**: 영점 statistics 가 GUE 와 일치 (수치적, Odlyzko millions of zeros).
- **자명**: Montgomery 의 pair correlation conditional on RH.
- **비자명 도약 1**: GUE conjecture 자체 *unconditional* 증명 — 어떤 도구가 필요한가?
- **비자명 도약 2**: RMT 가 ζ 의 *spectral interpretation* 에 어떤 명확한 다리?

### b. 사용 가능 도구
- **Gaussian Unitary Ensemble**: Wigner, Dyson — local statistics.
- **Characteristic polynomial moments**: Keating–Snaith 모델.
- **Free probability** (Voiculescu): RMT 의 *비가환* 일반화 — 미탐색 채널.
- **Determinantal point process**: 영점 분포의 정형화.
- **Hierarchical models**: family 통계.

### c. 분야 내 함정
- **모델과 증명 혼동**: GUE conjecture 가 *모델* 임을 잊고 RH 의 evidence 로 과도 해석.
- **family 평균과 단일 객체**: family 통계가 단일 ζ 의 결정적 statement 를 *주지 않음*.
- **moment 무한 vs 유한**: $I_k(T)$ 의 asymptotic 은 $k \le 2$ 만 증명, $k \ge 3$ 추측. 작은 k 에서의 정량 결과를 무비판 일반화 위험.

### d. 본 분야 한계 신호
- RMT 가 *evidence* 로는 강력 — 그러나 *증명 도구* 로는 한계.
- Katz–Sarnak symmetry types 분류는 *function field 에선* 증명 가능. number field 측의 unconditional 결과 부재.
- → RMT 자체보다 *RMT + 다른 분야 도구* 의 결합이 길.

### orientation 시도에 대한 평
- 본 시도의 §VII 정확. 다만 free probability 가 미탐색 — XI (비정통) 보다는 VII 의 확장으로 분류 고려.
- 권장: 다음 시도가 *RMT 정합성을 가정* 하고 그것이 다른 동치 형태에 어떤 제약을 주는지 분석 (II + VII 결합).

---

## S5 — 조합·하드해석 (Tao 류)

### a. 자명/비자명 분리
- **자명**: heat flow + zeros 동역학 + Coulomb repulsion (Csordas–Smith–Varga).
- **자명**: Λ ≥ 0 (Rodgers–Tao 2020) — backward-time 분석.
- **비자명 도약 1**: forward-time 에서 zeros 의 *clustering* 정량 통제 — 일반적으로 어려움.
- **비자명 도약 2**: Newman 의 *generalized* conjecture (Pólya 류 함수의 RH-like statement) — 일부만 풀림.

### b. 사용 가능 도구
- **Steepest descent / saddle point** (Tao paper §2 참조).
- **Gaussian heat kernel** + Stirling.
- **Pigeonhole + Bourgain energy method**.
- **Local equilibrium / arithmetic progression 분석**: log-gas 통계물리에서 import.
- **Riemann–von Mangoldt Lemma** for $H_t$ — Lemma 4 변형.

### c. 분야 내 함정
- **시간 방향 비대칭 무시**: backward 분석을 forward 에 그대로 적용 시 즉시 막힘.
- **heuristic vs rigorous**: physical 직관 (log-gas) 이 자연스러우나 정량 변환은 매번 nontrivial.

### d. 본 분야 한계 신호
- Λ ≥ 0 풀린 후 5년 — Λ ≤ 0 (=RH) 무진전. 본 도구의 한계가 *forward time control 부재* 임이 명확.
- 우회 후보: 시간 매개변수 *없이* 직접 zero distribution 통제 (e.g., 정량 Mertens, family pair correlation).

### orientation 시도에 대한 평
- 본 시도의 §VI 정확. 결합 후보 §VI + §VII (heat flow + RMT) 명시 권장.
- 권장: 다음 시도가 *forward-time control* 도구를 cross-domain 에서 (물리: Calogero–Moser, optimal transport, Ricci flow) 가져오는 시도.

---

## S6 — 양자물리 (Tier 2)

### a. 자명/비자명 분리
- **자명**: Lee–Yang 정리 (ferromagnet partition function 영점이 단위원 위) — RH 의 *물리적 형식 유추*.
- **자명**: Coulomb gas / log-gas — RMT 의 물리적 모델.
- **비자명 도약 1**: ζ 가 어떤 *구체적* 물리계의 partition function 인가? (Berry–Keating 직관 → BBM 시도 → self-adjointness gap)
- **비자명 도약 2**: PT-symmetric Hamiltonian → 실수 spectrum — 물리에서 잘 알려진 trick. 그러나 mathematically rigorous 확장이 어려움.

### b. 사용 가능 도구
- **Lee–Yang theorem** (Onsager, Asano).
- **Calogero–Moser system**: integrable many-body.
- **PT-symmetric quantum mechanics** (Bender 라인).
- **Quantum chaos / Berry–Keating** "H = xp".
- **Conformal field theory** + zeta regularization.

### c. 분야 내 함정
- **형식 동일성에 흥분**: 물리계의 partition function 영점 ≠ 수학 ζ — *유추는 강하나 직접 증명 X*.
- **rigorous 부재 자기-속임**: 물리에서 OK 인 step (formal series, divergent integral regularization) 이 수학적으로 미정의일 수 있음.

### d. 본 분야 한계 신호
- BBM 의 self-adjointness gap → 물리적 직관이 *마지막 한 발자국* 을 못 만듦.
- → 물리 도구는 *후보 발견* 에 강력, *증명* 에 약함.

### orientation 시도에 대한 평
- 본 시도의 §III 와 §VI 의 *물리적 측면* 정확. §XI (비정통) 의 후보 *Lee–Yang 직접 import* 가 흥미 — 미탐색 가능성.
- 권장: 다음 시도 중 하나가 *Lee–Yang style positivity* 를 number field 측에 어떻게 도입할지 brainstorm.

---

## S9 — 논리·증명론자 (Tier 2)

### a. 자명/비자명 분리
- **자명**: RH 는 $\Pi_1$ statement (Lagarias 동치 등으로 elementary 형식). 즉 *false* 이면 *유한* 검증으로 반증 가능.
- **자명**: ZFC 가 RH 를 결정하는지 미상. 단, $\Pi_1$ statement 의 ZFC 독립성이 가능하긴 함 (Goodstein 류).
- **비자명 도약**: RH 가 *PA 에서 증명 불가* 일 가능성 — 그러면 어떤 *더 강한 시스템* 이 필요한가?

### b. 사용 가능 도구
- **Reverse mathematics**: 어떤 공리 시스템이 RH 동치 statement 를 증명 가능?
- **Π_1 conservation**: ZFC + 일부 large cardinal 의 Π_1 결과는 ZFC 에서 증명 가능.
- **ω-consistency**: 연결.

### c. 분야 내 함정
- **독립성 vs 거짓**: RH 가 *PA-independent* 와 *false* 는 다르다. independence 는 *증명 시도가 무의미하다* 는 *함의 X*.
- **공리적 불충분 환상**: "ZFC 가 RH 못 증명" 가설은 흥미로우나 직접적 증거 부재.

### d. 본 분야 한계 신호
- 메타수학적 도구는 "RH 가 *어떤 공리* 에서 증명 가능한가" 를 묻기엔 약함 — 직접 증명 시도에 도움이 적음.
- 그러나 *consistency proof* 시각 (Riemann–von Mangoldt 형 항등식들이 어떤 axiomatic system 에서 자연스럽게 나오는가) 은 미탐색.

### orientation 시도에 대한 평
- 본 시도가 §XI (비정통) 에 logic 채널을 명시하지 않음. 추가 권장.
- 권장: 다음 시도 후보 중 하나는 *Lagarias σ(n) 동치* 의 *combinatorial proof* 시도 — 본 동치는 가장 elementary 이라 *어떤 elementary axiom system* 위에서 가장 가까이 가 있는지 분석 가치.

---

## Cross-examination — 모순/강화/격차

### 모순 (specialist 간 충돌)
- **S1 vs S2**: S1 은 "RH 는 *해석* 으로 못 풀린다 → algebraic" 시각, S2 는 "algebraic 도구가 number field 에 직접 옮겨가지 않는다 → 새 도구 필요" 시각. 같은 결론을 다른 방향에서 보고 있다 — 강한 신호 (모순 X, 사실은 강화).
- **S4 vs S5**: S4 (RMT) 는 "정합성 evidence", S5 (Tao 류) 는 "Λ ≤ 0 forward control 부재". 둘 다 *증명 X* 이라는 결론으로 수렴.
- (실질적 모순 없음 — 모든 specialist 가 *어렵다* 에 동의.)

### 강화 (다수 specialist 같은 방향)
- **S1 + S2 + S3 + Conrey 2003**: "L-function *families*" 가 main current.
- **S2 + S3**: "function field cohomology 의 number field 대응물" 이 핵심 미해결.
- **S5 + S6**: heat flow + log-gas 의 *forward-time* 통제가 비대칭 본질.
- **S6 + (S3)**: Lee–Yang style positivity ↔ Weil distribution positivity — 같은 맥락의 *positivity 의 본질* 추구.

### 격차 (어떤 specialist 도 답 못 함)
- **forward-time zero 동역학 통제**: S5 한계. 다른 specialist 도 답 X.
- **Frobenius 대응물 in characteristic 0**: S2, S3 모두 미해결.
- **Riemann 의 *원래 마음속 증명 시도* 의 흔적**: 모든 specialist 가 추측만. (Siegel 의 Nachlass 분석으로 일부만.)
- **PA / ZFC 에서 RH 증명 가능성**: S9 가 대답 못 함 (분야 자체가 분리).

## 운영 결함 발견 (HARNESS §7 개선 후보)

본 첫 가동에서 발견된 specialist 패널 운영 문제:

1. **시뮬레이션 중복**: S2 와 S3 가 같은 결론 (cohomology 갭) 으로 빠르게 수렴 — 두 specialist 의 *독립성* 점검 필요. 향후 시도에선 한 명의 답을 다른 specialist 에 *blind* 시도 권장.
2. **Tier 1 의 5개가 충분한가**: function field 측의 *대수적 number theory* 와 *대수기하* 가 분리되지 않음 — S2 안에 두 시각 혼재. 분리 권장.
3. **반환 라운드 (postmortem 시)** 의 효과 — 본 시도에선 미시도. 다음 시도에서 검증.
