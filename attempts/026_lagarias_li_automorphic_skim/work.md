# Work — Attempt 026 (Lagarias automorphic Li)

## Paper §1, §2 정독 (paper-direct)

### Key results

(2.4): $\Lambda(s, \pi) = \epsilon(\pi) \Lambda(1-s, \pi^\vee)$ — automorphic L 의 functional equation.

(1.11): $\lambda_n(\pi) = S_\infty(n, \pi^\vee) - S_f(n, \pi^\vee) + \delta(\pi^\vee)$ — explicit formula (archimedean + finite places + pole).

(1.17, 1.18): RH for $L(s, \pi)$ 가정 시:
$$\lambda_n(\pi) = \frac{N}{2} n \log n + C_1(\pi) n + O(\sqrt n \log n)$$

(Theorem 1.1) **RH for L(s, π) ⟺ Re λ_n(π) ≥ 0 for all n ≥ 1**.

### Wall #1 ↔ Li 동치 의 paper-direct connection

(paper §1 직접 인용):
> "The third observation [from Bombieri-Lagarias 1999] was that each positivity condition $\lambda_n \ge 0$ encodes 'Weil positivity' of Weil's quadratic functional for a particular test function $g_n(x)$."

→ **Li 동치 $\lambda_n \ge 0$ 가 Weil's quadratic functional positivity 의 specific instance**. 

이는 attempt 024 의 *positivity unification hypothesis* 의 paper-direct evidence:
- Function field 측: Rosati involution positivity (Iwaniec-Sarnak §3, attempt 023).
- Number field 측: Weil's quadratic functional positivity = Li 동치 $\lambda_n \ge 0$.

→ **Wall #1 의 trio (III) Rosati positivity 의 number field 형이 Li 동치 ↔ Weil positivity**.

### Wall #4 (CONSPIRACY) 와의 직접 연결

본 paper 의 generalization $\lambda_n(\pi)$ 는 *family 위로 일반화*. 

[plausible]:
- Wall #4 의 *family conspiracy*: Li 동치를 family 로 일반화 시 *family-wide positivity* 가 GRH 동치.
- 즉 **GRH for L(s, π) family 는 family-wide $\lambda_n(\pi) \ge 0$ 동치** — Wall #4 sharper.

→ Wall #4 의 *진짜 statement*: "family 의 Li coefficients 가 동시에 모두 ≥ 0" — *single positivity 조건 이 family 결합*.

### Lemma 추출 후보

**Process Lemma**: "Li 동치 = Weil positivity 의 *number field 표현* of *Rosati positivity*"

이건 paper-direct fact, lemma 로 명시화 가치. 단 paper 자체에서 인정 — *알려진 결과*. 우리가 *재발견* 이 아니라 *우리 wall taxonomy 와 명시 mapping*.

### "예상 가능 결과" self-check
*yes*. Lagarias paper 의 제목 자체가 "Li coefficients for automorphic L" — Wall #4 family 와 직접 연결.

[rigorous] 본 시도의 결과 — paper-direct, 우리 wall taxonomy 보강.

## 다음
- 027 — Type C: lemmas/positivity_unification 갱신 (Li ↔ Rosati paper-direct evidence 추가).
- 028+: 사용자 신호.
