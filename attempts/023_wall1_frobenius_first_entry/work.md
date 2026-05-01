# Work — Attempt 023 (Wall #1 첫 진입)

## Iwaniec-Sarnak §3 정독

### Function Field RH 증명 도구 (paper 직접)

$$\zeta_k(T) = \frac{P(T, C/\mathbb{F}_q)}{(1-T)(1-qT)}, \quad |T_\rho| = 1/\sqrt{q}$$

핵심 도구 (Weil/Deligne):

(I) **Lefschetz trace formula**: $N_n$ (= # points on C over $\mathbb{F}_{q^n}$) 를 *Frobenius morphism 의 fixed points* 로 표현 → linear algebra (eigenvalue trace).

(II) **Frobenius eigenvalue spectral interpretation**: Jacobian X 위의 Frobenius endomorphism α 가 $\ell^\nu$-division points 위에 ℓ-adic matrix 로 작용. **α 의 eigenvalues = inverses of zeros of P(T)**.

(III) **Rosati involution positivity**: 영점이 |T| = 1/√q 위에 있다는 statement 의 핵심 — α 의 endomorphism ring 에서 *positivity argument*.

→ paper 직접 인용: "the proof that the zeros are on the circle 1/√q requires a further elaborate analysis of α in the endomorphism ring of X and in particular the **use of the positivity of Rosati involutions**"

### Wall #1 의 *trio of gaps*

[rigorous] paper 의 직접 statement:

Number field 측에서 *세 가지* 대응물 부재:
1. **Lefschetz trace formula 의 number field 형**: 알려진 *trace formula* 들 (Selberg, Connes, Arthur) 가 일부 후보이나 RH 직접 적용 안 됨.
2. **Frobenius char 0 대응물**: 미상 — Bombieri Clay 의 핵심 미해결.
3. **Rosati involution positivity 의 산술 대응물**: Connes Weil distribution positivity, Hodge index conjecture 등이 후보.

→ Wall #1 의 *진짜 정체* = **trio of gaps**. Connes, Deninger, Bombieri 의 시도들이 *각각 다른 trio component* 시도.

### 본 시도의 honest 결과

- Wall #1 statement *trio* 로 sharpening — paper-direct.
- *novel content X*. Iwaniec-Sarnak 의 *명시적 인용* 으로 우리 wall 진화.

### Lemma extraction trigger

*lemma X*. wall sharpening only.

### "예상 가능 결과" self-check

*yes*. Wall #1 의 *trio of gaps* 가 paper 정독 후 명시화 — 새 정보 X 이지만 우리 wall 명시화.

## 다음 시도

- 024 — Type C: HARNESS 의 specialist 패널 의 Wall #1 mapping.
- 025 — Type A: 양정치성 메타 가설 (`learnings/walls.md` §메타) 과 Rosati positivity 의 직접 연결 시도.
