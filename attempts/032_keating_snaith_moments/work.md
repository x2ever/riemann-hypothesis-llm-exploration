# Work — Attempt 032 (Keating-Snaith Moments)

## g_k formula (KS 1999)
$g_k = k!^2 \prod_{j=0}^{k-1} \frac{j!}{(j+k)!}$

Numerical:
- $g_1 = 1$
- $g_2 = 1/3 \approx 0.333$
- $g_3 \approx 0.00417$
- $g_4 \approx 1.06 \times 10^{-6}$

(Conrey 2003 의 $g_2=2$, $g_3=42$ 는 *다른 normalization* — *2k-th moment 의 k!² 분모 포함 vs KS 행렬 측 g_k* 차이.)

## I_k(T) at small T

[numerical, dps=30, n_points=100]

| T | I_1(T) | I_2(T) | I_3(T) |
|---|---|---|---|
| 50 | 2.31 | 13.17 | 107.4 |
| 100 | 2.98 | 24.21 | 283.4 |
| 200 | 3.98 | 50.84 | 1067 |

### Asymptotic 진입 평가

KS 예측: $I_k(T) \sim g_k \cdot a_k \cdot (\log T)^{k^2}$.
- log 50 = 3.9, log 200 = 5.3.
- $(log T)^9 / (log T)^4 = (log T)^5$ (k=3 vs k=2 ratio).
- Empirical $I_3/I_2$ ratio 변화: T=50: 8.2, T=200: 21.
- 예측 $(5.3/3.9)^5 = 5.0$.
- *Discrepancy 4배* — *작은 T*에서 KS asymptotic 미진입.

→ **본 시도 numerical 만으로는 KS 검증 불가**. T = $10^6$+ 필요 (Odlyzko 영역).

## 결론

[rigorous]:
- $g_k$ formula confirmation (분야 표준).
- I_k(T) 의 small-T behavior — KS 예측과 quantitative 일치 *못 함*.

honest negative — *우리 한정 numerical 으로 KS asymptotic 검증 X*.

## "예상 가능 결과" self-check
yes — strategy 의 "asymptotic 진입 가능성 평가" 가 *negative* 가 예상.

## Lemma extraction trigger
*lemma X*. KS asymptotic 의 *우리 numerical scale 진입 못함* 의 honest 인정 — 외부 critique 와 일관.
