# Spectral Candidate Circularity Check

> **Source**: attempt 010 (BBM truncation). 외부 감시자 비판으로 lemmas/ 추출 의무화.
> **Status**: 비판적 reading 도구 (proof X, methodology lemma).

## Statement

Hilbert–Pólya 류의 spectral 후보 (Berry–Keating xp, BBM Hamiltonian, Sierra extensions, Connes spectral triples 등) 를 평가할 때, 다음 *분리 의무*:

**[A] Trivial part (definitional / circular)**: spectrum 의 *멤버십* 정의가 영점 조건을 *입력*으로 받는 부분.

**[B] Non-trivial part**: 자기수반성 (self-adjoint extension on a concrete Hilbert space + uniqueness) 이 RH 의 *새 정보* 를 주는지, 또는 RH 와 *동치 변형* 인지.

**평가 시 의무**: 새 spectral 후보가 RH 증명 후보로 제안될 때, 본 lemma 의 (A) 와 (B) 를 *명시적으로 분리*. (A) 만 보이는 후보는 *증명 후보 아님* — 단지 동치 reformulation.

## Demonstration (BBM 사례, attempt 010)

BBM Hamiltonian:
$$\hat H = (1 - e^{-i\hat p})^{-1} (\hat x \hat p + \hat p \hat x) (1 - e^{-i\hat p})$$

- Eigenfunction: $\psi_z(x) = -\zeta(z, x+1)$ (Hurwitz zeta).
- Boundary condition: $\psi_z(0) = 0$.
- 내용: $\psi_z(0) = -\zeta(z, 1) = -\zeta(z)$.

따라서 $\psi_z(0) = 0 \iff \zeta(z) = 0$.

**[A] 자명**: spectrum identification (어떤 z 가 spectrum 멤버) ⟺ z 가 영점.
**[B] 미증명**: $\hat H$ 가 어떤 inner product 위에서 *self-adjoint* — 이게 입증되면 spectrum 실수 ⟹ RH.

수치 검증 (010, dps=40, N=10): $|\psi_z(0)| \approx 10^{-16}$ at zeros, $> 0.1$ off zeros.

## 적용 절차 (templates)

### 새 spectral 후보 평가 시
1. *Eigenfunctions* 의 explicit 형태가 알려진가?
2. Boundary condition 또는 spectrum 정의가 *어떤 함수의 vanishing* 인가?
3. 그 함수가 ζ 또는 ζ-related 인가?
4. (yes 라면) → [A] trivial. *non-trivial claim* 은 self-adjointness 만.
5. Self-adjointness rigorous 증명·반증 시도되었는가? → [B] 의 진행.
6. **(추가, attempt 029 Sierra)** Self-adjoint extension parameter 가 *모든* 영점을 *동시* 매칭하는가? — *single Hamiltonian for all zeros* 의 존재.
   - Sierra 2016 §I 직접: "one needs to fine tune a parameter to see each individual zero. We are not able to find a single Hamiltonian encompassing all the zeros at once."
   - 즉 spectrum 이 *parametrically* RH 와 동치 — 실제 RH 증명 X 일 가능성.
   - 만약 (6) 의 답이 *single* H 미발견 → 본 spectral 후보가 *RH 증명 후보 아님*, 다른 동치 reformulation.

## 영향

- 본 프로젝트의 향후 attempts 에서 spectral 후보 (Sierra, Connes-Consani 등) 평가 시 본 lemma 적용.
- 새 후보가 [A] 만 산출하면 우리 직접 시도 우선순위 ↓.
- [B] 의 새 도구 (deficiency index, Krein, Tomita-Takesaki) 가 *진짜 진전* 채널.

## Dependencies

- `background/definitions.md`: ζ, Hurwitz ζ, 비자명 영점.
- `papers/INDEX.md`: bender-brody-mueller2017, sierra_2016, connes-consani2021.

## Where Used

- attempt 010 (산출).
- (예정) attempt 014+ — Sierra 2016/2007 정독 시.

## Caveats

- 본 lemma 는 *증명 도구가 아니라 비판적 reading 템플릿*. 그 자체로 RH 진전 X.
- 적용 시 *형식 일치* 와 *수학적 동치* 의 구분 의무 — 어떤 후보는 (A) 로 보이지만 (B) 가 *진짜 증명* 일 수도 있음 (그 가능성 자체는 본 lemma 가 배제 X).

## 6단계 paper-direct 표 (~attempts 110, 111, 120)

| Candidate | (1) spec=ζ | (2) def w/ ζ | (3) self-adj | (4) trace | (5) prime | (6) Lefschetz |
|---|---|---|---|---|---|---|
| BBM 2017 (attempt 110) | YES | YES indirect | NO | NO | PARTIAL | NO |
| Sierra §III xp | NO (cont) | NO | YES | NO | NO | NO |
| Sierra §V H_I | NO (smooth) | NO | YES (ϑ) | NO | NO | NO |
| Connes-Consani 2021 (attempt 111) | NO (special λ) | NO | YES | PARTIAL | PARTIAL | PARTIAL |
| Connes 1999 §VI/VII | (no spec cand) | (cutoff trace) | (formal trace + cutoff) | YES (Theorem 4) | YES (∫'_{k_v*}) | distribution-valued |
| Lagarias §8 (1) hypothetical | YES | YES (λ=s²-1/4) | *issue* | NO | NO | NO |
| Sierra 2007 H_2 (attempt 133) | NO (asymptotic) | PARTIAL (Jost dilation) | YES (deficiency) | NO | NO | NO |

→ Connes-Consani 2021 = *least circular* (1, 2 NO).

## 새 axiom (7) 후보 — attempt 120 NOVEL finding
*spectrum eigenvalues all real* (self-adjointness paper-direct verification).

| Candidate | (7) eigenvalues all real |
|---|---|
| BBM 2017 | E_n = -2γ_n (RH 가정 yes) |
| Sierra §V | Bessel root yes |
| Connes-Consani 2021 | yes |
| Connes 1999 §VI | distribution real |
| Lagarias §8 (1) hypothetical | **NO!** (λ = s²-1/4 = -γ²+iγ complex) |

→ paper-direct *Lagarias §8 (1) hypothetical* 의 *self-adjoint hypothesis 자체 technical issue* — paper *self-acknowledged hypothetical*.
