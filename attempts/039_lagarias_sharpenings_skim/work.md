# Work — Attempt 039 (Voros 2006)

## Theorem (asymptotic criterion for RH) — paper-direct

For $n \to \infty$, λ_n 의 *sharp dichotomy*:

- **[RH true]** ⟺ tempered: $\lambda_n \sim \frac{1}{2} n(\log n - 1 + \gamma - \log 2\pi) \pmod{o(n)}$.
- **[RH false]** ⟺ non-tempered: $\lambda_n \sim \sum_{\arg\tau_k > 0} \left(\frac{\tau_k + i/2}{\tau_k - i/2}\right)^n + c.c. \pmod{o(e^{\varepsilon n})}$ — exponentially growing oscillations.

이 두 *mutually exclusive* large-n behaviors 가 RH 의 *sharp* asymptotic criterion.

## Wall #6 (LOCAL-GLOBAL-MISMATCH) 의 paper-direct resolution

[rigorous]:

attempt 001 의 cross-check (λ_n^(ζ) vs RMT GUE) 가 mismatch 한 이유 *paper-direct*:
- λ_n 은 *large-n asymptotic* 에서 RH 정보 sharp.
- 첫 N=100 영점 truncation 은 *asymptotic 영역 진입 X*.
- truncation effect 가 *RH-equivalent 정보* 를 가림.

attempt 027 의 numerical (n=20 ratio≈1) 이 *partial confirmation* — n=20 도 still sub-asymptotic.

→ Wall #6 (LOCAL-GLOBAL-MISMATCH) 의 본질: *truncation effect* + asymptotic 진입 limit. 이는 attempt 001 의 *redirection* 신호 — 더 큰 n + 더 많은 zeros 필요.

## RH-true vs RH-false 의 *exponential gap* (Voros)

[rigorous, paper-direct]:

만약 RH false 이면 λ_n 가 *exponentially* oscillate. 이는 *수치적으로 관찰 가능* — 충분히 큰 n 에서 RH true asymptotic (n log n) vs RH false (e^{εn}) 가 *완전 분리*.

→ *수치 RH 검증 channel*: n 충분히 크면 두 behaviors 구별 가능. 우리 attempt 027 의 n=20 결과가 tempered 와 일관 — RH true 와 정합 (수치적 evidence, *증명* X).

## 본 시도 honest 결과

- Wall #6 의 paper-direct resolution.
- attempt 001 의 mismatch 가 truncation effect 의 산물 명시 확정.
- *novel content X*. paper-direct.

## "예상 가능 결과" self-check
yes — Voros paper Theorem 직접.

## Lemma extraction trigger
*lemma X*. wall sharpening only — `learnings/walls.md` 에 wall #6 갱신.
