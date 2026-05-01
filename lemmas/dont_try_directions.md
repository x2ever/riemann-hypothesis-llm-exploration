# Lemma 6 — *가지 말아야 할 Directions*

> Specialist 가 5분에 줄 *cut guidance* 의 본 프로젝트 자체 관찰판.
> 본 프로젝트가 시도하고 *실제로* wall 만난 directions + 외부 paper 에서 known fail.

## 명시 cuts

### Cut 1 — Wasserstein 시간대칭 → RH 시간대칭

**시도**: attempt 007. Otto's calculus 의 entropy/Wasserstein gradient flow 가 RH 의 functional equation 시간대칭 ξ(s) = ξ(1-s) 와 *동형* 인지 검토.

**왜 컷**:
- Otto's calculus 는 Riemannian manifold 의 probability measure space 의 gradient flow.
- RH functional equation 은 *holomorphic* symmetry — analytic continuation.
- 두 *시간대칭* 의 mathematical structure 가 *별개*. 표면 유사.

**Specialist 5초**: "Otto's calculus 시간대칭은 *L² gradient*, RH 는 *분석적 holomorphic* — 다른 시간".

### Cut 2 — Levinson-Durbin / Pratt-Robles mollifier *같은 사람 다른 수학*

**시도**: attempts 015, 016. Levinson 의 1974 *one third theorem* (33%) 와 Norman Levinson 의 prediction theory (Levinson-Durbin recursion).

**왜 컷**:
- *같은 Norman Levinson* 이지만 두 분야는 *완전히 다른 수학*:
  - Prediction theory: AR(p) coefficient recursion, signal processing.
  - Zero-density mollifier: Riemann ξ 함수의 critical line zero density 추측.
- Pratt-Robles 2019 의 mollifier 는 *Levinson 1974 의 후속* — Levinson-Durbin recursion 과 *전혀 무관*.

**Specialist 5초**: "이름 같은 사람일 뿐 분야 다름".

**우리 노력**: lemma `levinson_durbin_mollifier_open_question.md` RESOLVED (negative).

### Cut 3 — Vacuum positivity → RH

**시도**: attempts 020-074 (positivity unification 시리즈).

**왜 미부분 컷** (cut 의 *부분 적용*):
- λ_n ≥ 0 ⟺ RH (Li 1997). 이건 *theorem*.
- *λ_n > 0 의 unconditional lower bound* 시도 = 본 프로젝트 lemma 3 의 8 paper-direct evidence chain.
- 그러나 *positivity 에서 RH 직접* 은 specialist 의 *이미 알려진 wall*: vacuum lower bound 는 *S_∞ - S_f* 의 binomial-amplified cancellation 으로 *trivial* 안 됨.

**Specialist 추정 답**: "Lagarias 2004 generalization 후 자율 시도 (Bombieri-Lagarias 1999 이전 + 후) *모두* 부분 sharpening 만. 진짜 unconditional lower bound 는 Hilbert-Pólya 또는 자명 Weil scalar product 가 진짜 spectral 일 때만".

**우리 자체 인정**: lemma 3 의 paper-direct evidence chain *= mapping* 만. *증명 X*.

### Cut 4 — Atiyah-style "novel proof" 재시도

**시도 X**: 002 에서 cross-check 만. Atiyah 2018 fail 패턴 (`failed_proof_categories.md` lemma 4) 추출.

**왜 컷**:
- Atiyah Todd function: T(s) = T(2s)·... 이 *all primes simultaneously* 항등식 만족하는 인공 구성. *not naturally arising* analytic function.
- "Hadamard product 으로 induce" 가 자연스러운 *Connes-style* 시도가 아닌 *fictional construction*.

**Specialist 5초**: "naturally arising X — Hilbert-Pólya 후보 자체가 Hilbert-Pólya 의 본질을 가린 fictional".

### Cut 5 — *모든 spectral 후보 = circular*

**시도 X**: attempts 010 lens (spectral_candidate_circularity_check lemma 1).

**6단계 cut criterion**:
1. *D 의 spectrum이 ζ 의 zeros 에 *exact* equal* 라고 *bake* 되어 있으면 = circular.
2. *Hamiltonian 의 정의 자체* 에 ζ 가 들어가면 (BBM 같은 경우) = circular by construction.
3. *self-adjoint 입증 부재* 면 = unrigorous.
4. *Frobenius gap 메우는 trace formula* 부재 면 = incomplete program.
5. *single H 가 모든 prime 보는* 구조 부재 면 = local-global mismatch.
6. *number field 의 Lefschetz analogue* 명시 부재 면 = function field imitation.

**Specialist 5초**: BBM (1, 2 yes), Connes-Consani (1, 4 partial), Sierra (3 yes — distribution rigor 부족).

**~Attempt 118 (NOVEL ATTEMPT FAILURE) — Cut 7 후보**:
*paper-미명시 quantitative form 의 LLM 도구 empirical 추정 시도*.
- 시도 가능, *결과 = paper-direct citation 만* + 우리 도구 fundamental limitation.
- 외부 critique #4 Gap 4 (새 도구 적용 가능성) 의 *paper-direct verification*.
- Specialist 5초: "infinitely many handling 부재 — paper theoretical tool (Dirichlet 등) 만 가능."
- 사용 방법: LLM 도구 *paper-rigorous infinity scope 외* attempt = expected failure 명시.

**~Attempt 111 update (Connes-Consani 2021 paper-direct full check)**:
- Connes-Consani 2021 = *least circular* spectral candidate (Lemma 1 검사 결과).
- (1) spec=ζ: NO (special λ 만, 10^-50 prob coincidence — non-circular).
- (2) def w/ ζ: NO (D = (1-Π)∘D_0∘(1-Π) prolate spheroidal Dirac perturbation).
- (3) self-adjoint: YES.
- (4-6): partial.
→ Cut 5 의 *부분 정정*: 모든 spectral candidate 가 (1, 2) yes 는 X. Connes-Consani exception. 그러나 (4-6) partial 만 — *exact RH spectrum* 부재.
→ specialist 추정 (Connes): "RH 직접 X, conceptual explanation 다년".

### Cut 6 — *positivity criterion 의 단독* RH 증명

**시도 X**: 본 프로젝트 자체 관찰.

**왜 컷**:
- Bombieri-Lagarias / Voros / Sekatskii / Lagarias-Li / Pratt-Robles — 모두 positivity criterion 의 *paper-direct* derivation.
- 그러나 *unconditional lower bound* λ_n > 0 (n ≥ 1) 시도 = 본 프로젝트 lemma 3 의 *paper-direct mapping* 만 + *증명 X*.
- Connes 1999 §IV trace formula 의 *positivity ↔ RH* 가 paper-direct equivalence — 그러나 trace formula 의 *unconditional positivity* 는 number field 측 *Wall #1*.

**Specialist 5초**: "positivity criterion 들은 RH 의 *언어 변경* — Hilbert-Pólya 의 *self-adjoint* 또는 Wall #1 의 *function field Lefschetz analogue* 가 진짜 진전."

## 사용 방법

각 새 attempt 의 strategy.md 작성 시 self-check:
- 본 시도가 *Cut 1-6* 중 하나의 *부분 재시도* 인가?
- 만약 yes → *컷* (또는 명시 *재고려 사유* 작성).
- 만약 no → 진행 가능 (그러나 Mode A deep 8 components 따름).

## 한계

- 본 lemma 자체가 *우리 자체 관찰 + 외부 paper cited fact* 만. *진짜* specialist 직접 검증 X.
- 향후 외부 critique 또는 specialist 검토 시 본 lemma 정정 가능성 명시.
- 본 lemma 의 cuts 가 *너무 conservative* 가능성 — 모든 시도를 차단하면 *아무 시도 X* 가 되므로 *plausible incremental sharpening* 은 cut X.