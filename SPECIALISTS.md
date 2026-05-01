# Specialist Personas — 분야별 심층 검토 패널

> RH는 한 분야의 깊이만으로는 안 풀린다. 하지만 *피상적 cross-domain 유추*만으로도 안 풀린다. 풀린다면 — **여러 분야를 각각 깊이 이해한 사람** (또는 그런 사람들의 조합) 이 풀 가능성이 높다. 이 하네스는 그 조건을 *시뮬레이션*하기 위한 specialist 패널을 운영한다.

## 운영 원리

Cross-domain pass (HARNESS §6) 는 **유추 generation**. 본 패널은 그 유추를 **각 분야 깊이로 검증·확장**하는 단계.

각 specialist 는:
- 해당 분야의 *기술적 도구·정리·관습·한계*를 깊이 알고 있는 가상 페르소나로 행동.
- 자기 분야 시각에서 RH(또는 현재 시도)에 대해 (a) 무엇이 자명한가 (b) 무엇이 비-자명한가 (c) 자기 분야의 어떤 도구가 본질적으로 적용 가능한가 (d) 어떤 함정에 빠지기 쉬운가 를 답.
- **자기 분야의 한계도 명시**: 분야 내에서 풀린 비슷한 문제와 *왜 RH는 그 도구로 안 풀리는지*.

generalist (Claude 메인 흐름) 가 페르소나들을 *순회 호출* + 결과 *충돌 조정* + *통합 가설* 작성.

## 패널 구성

### Tier 1 — 핵심 (모든 시도에 호출 의무)

#### S1. 해석적 정수론자 (Analytic Number Theorist)
- **배경**: Hardy–Littlewood–Selberg–Levinson–Conrey–Iwaniec 라인. mollifier, mean value 정리, large sieve, exponential sum, ζ moments.
- **본능적 질문**: "이 시도의 *주요 분석적 추정* 은? Cauchy–Schwarz 어디서 손해를 봤는가? mean value 정리의 어떤 정확한 상수가 필요한가?"
- **알려진 한계**: 임계선 위 비율 1을 못 도달. mollifier optimization 의 본질적 상한.
- **함정 경고**: "임계선 위 비율을 100% 까지 올린다 ≠ RH". 모든 영점이라는 보장이 아니다.

#### S2a. 대수기하학자 — Function field RH (Algebraic Geometer)
- **배경**: Weil conjectures, étale cohomology, Frobenius eigenvalue, Deligne. Function field 에서 RH는 *증명되어 있다* (Weil 1948 / Deligne 1974).
- **본능적 질문**: "function field 에서 RH 증명에 본질적으로 사용된 *positivity* 또는 *cohomological* 구조 중에서, number field 로 옮기면 *정확히 어디서* 부서지는가? characteristic 0 에서 Frobenius 의 대응물이 무엇인가?"
- **알려진 한계**: number field 에는 Frobenius 가 없다. 'arithmetic site' / Connes–Consani / Deninger 가 채워보려는 시도들.
- **함정 경고**: "Weil 증명을 흉내내자" 는 흔한 오류. cohomology base ring 차이를 무시함.

#### S2b. 대수적 정수론자 — Iwasawa·class field·motivic L (Algebraic Number Theorist)
- **배경**: Iwasawa theory, class field theory, modular forms, motivic L-functions, BSD conjecture, automorphic representations.
- **본능적 질문**: "이 시도가 어떤 L-function 가족에 위치? 그 가족의 functional equation 의 root number / 부호 / Euler factor 가 어떻게 영점 분포에 반영? automorphic side (Langlands) 와의 연결?"
- **알려진 한계**: GRH 도 미해결. Iwaniec 의 family 시도가 Landau–Siegel 제거 직전에 막힘.
- **함정 경고**: motivic + automorphic 가족이 *너무 다양* — 본 시도가 *특정* 가족에 한정되어야 statement 의미.

#### 운영 메모 (S2 분리 후)
- 시도가 function field 측 도구만 의지하면 S2a 만, families/automorphic 측이면 S2b 만, 둘 다면 둘 다 호출.
- 이전엔 두 시각이 S2 안에 혼재 → confirmation bias 위험 → 분리.

#### S3. 작용소대수·NCG 전문가 (Operator Algebra / NCG)
- **배경**: Connes, Selberg trace formula, spectral triples, Type III factor, KMS state, idele class group.
- **본능적 질문**: "이 시도가 *어떤 spectral 객체*를 가정하는가? 그 객체의 자기수반성·실재성은 어떻게 보증되는가? trace 가 well-defined 한 영역은?"
- **알려진 한계**: Connes 의 trace formula 는 RH 와 *동치 변형*은 가능했으나 본 등식의 한쪽을 *독립적으로* 증명하는 건 미해결.
- **함정 경고**: 형식적 spectral interpretation 자체는 RH 증명 아님. "Hamiltonian 을 적었다" 와 "그 Hamiltonian 의 자기수반 확장이 *유일하게* 존재하고 스펙트럼이 영점과 *bijective* 하게 일치한다" 는 다르다.

#### S4. Random matrix / 확률론자 (RMT / Probabilist)
- **배경**: Montgomery, Odlyzko, Keating–Snaith, Katz–Sarnak. GUE pair correlation, Selberg–GUE moments, characteristic polynomial.
- **본능적 질문**: "이 시도의 결론이 RMT 모델 (CUE / GUE) 의 예측과 정합적인가? 모멘트의 sharp constant 가 맞는가? local statistics 가 어떤 universality class 인가?"
- **알려진 한계**: RMT 는 *모델*이지 RH 의 증명이 아니다. 정합성은 강력한 신호이나 logical implication 아님.
- **함정 경고**: "GUE 와 일치하니 RH가 참이다" 는 비-증명. 일치는 conditional 분포의 일관성일 뿐.

#### S5. 조합론·해석학자 (Combinatorics / Hard Analysis — Tao 류)
- **배경**: additive combinatorics, dispersive PDE, sum–product, regularity. de Bruijn–Newman 류, Selberg sieve.
- **본능적 질문**: "이 시도에서 *불연속적 양*과 *연속적 양* 의 변환은 어디서 일어나는가? 어떤 *energy method* 가 적용 가능한가? 정보 손실은 어디서 발생?"
- **알려진 한계**: Λ ≥ 0 (Rodgers–Tao) 은 풀렸으나 Λ ≤ 0 (=RH) 의 비대칭성.
- **함정 경고**: heat flow / diffusion 류는 *영점을 옮긴다*. 시간 t=0 에서의 영점 분포 자체에 대한 statement 가 결국 필요.

### Tier 2 — 보조 (시도 성격에 따라 호출)

#### S6. 양자 물리학자 (Quantum Physicist)
- **배경**: PT-symmetric Hamiltonian, quantum chaos (Berry–Keating "H = xp"), 통계역학 partition function.
- **본능적 질문**: "이 객체가 어떤 *물리계*의 partition function 으로 해석되는가? 그 계의 *대칭*과 영점 위치의 관계?"

#### S7. 동역학계 전공자 (Dynamical Systems)
- **배경**: Ruelle / dynamical zeta, length spectrum, ergodic theory, foliated spaces (Deninger).
- **본능적 질문**: "ζ 를 어떤 동역학계의 *length zeta* 로 해석할 때 'flow'는 무엇? 'periodic orbit' 의 prime 대응은?"

#### S8. 위상수학자 / 대수적 위상 (Topologist)
- **배경**: K-theory, homotopy, sheaf cohomology, motivic.
- **본능적 질문**: "영점들의 *moduli* 공간이 있는가? 'cycle' 으로 보면 어떤 cohomology class?"

#### S9. 논리·증명론자 (Logician)
- **배경**: PA, ZFC, 독립성, computability, reverse mathematics.
- **본능적 질문**: "RH 의 증명에 *어떤 공리*가 본질적으로 필요한가? RH 의 ZFC 독립성 가능성은? Π_1 statement 인가?" (실제로 RH 는 Π_1 이라 false 면 유한 검증으로 반증 가능)

#### S10. 컴퓨터 과학자 / 알고리즘 (CS / Algorithmics)
- **배경**: ζ computation 복잡도, 영점 verification 알고리즘, Riemann–Siegel formula, 정밀도 issue.
- **본능적 질문**: "이 시도의 *알고리즘적 verification* 가능 부분은? 정밀도가 부족해 false positive 가능성은?"

#### S11. 확률론자 — 자유확률 (Free Probability)
- **배경**: Voiculescu free probability, free convolution, large random matrix limit.
- **본능적 질문**: "ζ 모멘트가 어떤 free 확률 객체의 cumulant 로 해석되는가? RMT 보다 더 정확한 결합 모델은?"

### Tier 3 — 비정통 / 실험적 (선택)

#### S12. 정보이론가 (Information Theory)
- **배경**: entropy, KL divergence, rate-distortion.
- **본능적 질문**: "ζ 영점 분포에 *최대 엔트로피 원리* 가 있는가?"

#### S13. 최적수송 / 미분기하 (Optimal Transport)
- **배경**: Wasserstein, Ricci flow, gradient flow on measures.
- **본능적 질문**: "영점 측도의 evolution 을 gradient flow 로 보면? 'Ricci-positive' 같은 정성적 보증?"

#### S14. ML / 근사이론 (Approximation Theory)
- **배경**: neural net 으로 ζ 표현 학습, 학습된 representation 분석.
- **본능적 질문**: "ζ 의 *학습 가능 표현* 이 분류적 구조를 드러내는가?" (대부분 막다른 길일 가능성. 그래도 brainstorm 단계엔 가치)

---

## 호출 프로토콜 (시도별 운영)

각 attempt 의 strategy.md 에 다음 워크플로우 추가:

### Step 1. 패널 선택
시도의 본성에 맞춰 **Tier 1 전부 + Tier 2 중 관련 1-3개** 선택. 의무적 비대칭성: 자기 시도가 의지하는 분야뿐 아니라 *다른* 분야 specialist 도 반드시 호출 (한쪽 시각으로 빠지지 않게).

### Step 2. 각 specialist 라운드 (single pass)
선택된 각 specialist 마다 다음 4개 질문에 답을 적는다 (`attempts/NNN_*/specialist_round.md`):

```markdown
## S_k — <name> (specialist 이름)

### a. 자명/비자명 분리
이 시도에서 본 분야 시각으로 *자명한 부분*과 *비-자명한 도약*은?

### b. 사용 가능 도구
본 분야의 어떤 정리/기법이 적용 가능? 정확한 statement 까지.

### c. 분야 내 알려진 함정
이 종류 시도에서 본 분야 사람들이 자주 빠지는 오류·환상은?

### d. 본 분야의 한계 신호
본 분야 도구만으로는 *어디까지 가고 막히는가*? 그 막힘이 RH 본질에 대해 말해주는 것은?
```

### Step 3. 충돌 조정 (cross-examination)
specialist 들의 답이 서로 *모순*되거나 *상호 강화*하는 지점을 찾아 정리. 이 단계가 generalist (메인 흐름) 의 본 역할.

```markdown
## Cross-examination

### 모순 (서로 다른 specialist가 충돌하는 지점)
- S1 vs S4: ...
- S2 vs S3: ...

### 상호 강화 (둘 이상이 같은 방향을 가리킴)
- S2 + S3 + S6: ... (이런 합치는 강한 신호)

### 격차 (어떤 specialist도 답 못 한 곳)
- ...
```

### Step 4. 통합 가설
specialist 라운드와 cross-examination 후 *수정된* strategy 를 적는다. 처음 strategy 와 비교해 무엇이 바뀌었는가도 기록 (학습 데이터).

### Step 5. 시도 후 반환 라운드
시도 종료 시, 막힌 곳을 가지고 **specialist 들에게 다시 묻는다**: "이 막힘에 대해 본 분야 사람이라면 무엇을 시도하겠는가?"

postmortem.md 의 마지막에 *반환 라운드 결과* 를 기록 → 다음 시도의 입력.

## Blind Round Protocol (결함 1 반영 — attempt 000)

> 첫 호출 시 specialist 답이 *다른 specialist 의 답을 보고 영향* 받을 수 있다 — confirmation bias. 이를 방지:

### A. 첫 패스 — Blind
- 각 specialist 가 *독립적*으로 답. 다른 specialist 의 답을 *참조 X*.
- specialist 답을 별도 섹션 (`## S_k blind`) 에 작성. 호출 시점 명시.

### B. 둘째 패스 — Cross-examination
- 모든 blind 답이 모인 후, generalist (메인 흐름) 가 *모순/강화/격차* 를 식별.
- 모순이 발견되면 *모순 specialist 들에게 다시* 호출 — "S_j 가 X 라고 답함, 본인 답을 수정·강화·반박?". 이건 non-blind.

### C. 운영 효과
- A 단계가 *진짜 분야 시각의 다양성* 을 잡음.
- B 단계가 통합·결합.
- 첫 호출이 *다른 specialist 답에 노출되지 않으면* 동일 결론 수렴은 *진짜 사실* 신호 (분야들이 정말 같은 본질을 가리킴).

### D. 운영 비용 vs 가치
- 작은 시도 (Type A small, Type C, etc.) 에선 blind round 의 ROI 작음 — generalist 의 빠른 통합으로도 충분.
- 큰 시도 (Type A 야심, Type B meta) 에선 blind round 의무.
- Strategy.md 의 specialist 호출 섹션에 `[blind: yes/no]` 명시.

---

## 정직 체크 — Specialist 시뮬레이션의 한계

> 이 패널은 *진짜 전문가*가 아니라 LLM 의 시뮬레이션이다. 실제 전문가의 직관·감각·실수 경험과 일치한다는 보장 없음.

규율:
1. specialist 가 자기 분야 정리를 *인용* 할 때는 *정확한 statement 까지* 적기 — 모호하면 버림.
2. specialist 가 "이건 본 분야에서 잘 알려진 결과다" 라고 말하면 *literature 확인* 의무 (papers/INDEX.md 또는 검색).
3. 한 시도 안에서 같은 specialist 의 *의견 변경* 이 일어나면 그 자체가 학습 신호 — 기록.
4. specialist 라운드 결과가 메인 흐름의 *기존 의견을 단순 강화* 만 한다면 의심: 진짜 specialist 시각이 아니라 confirmation bias 일 수 있다.

## 체크리스트 — 모든 시도에 적용

- [ ] Tier 1 (S1–S5) 전부 호출했는가?
- [ ] Tier 2 중 시도 성격에 맞는 specialist 1-3 추가 호출했는가?
- [ ] 본 시도가 *의지하는 분야* 외의 specialist 도 *반드시* 호출했는가?
- [ ] cross-examination 에서 모순·강화·격차 모두 기록했는가?
- [ ] specialist 의 분야-내 정리 인용은 *정확한 statement* 와 함께인가?
- [ ] *반환 라운드* (postmortem 시) 도 수행했는가?
