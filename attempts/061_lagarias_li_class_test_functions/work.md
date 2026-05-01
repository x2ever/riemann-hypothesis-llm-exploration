# Work — Attempt 061 (Lagarias Theorem 3.1)

## Special test functions G_n(s) (paper §3, eq 3.2)
$$G_n(s) := 1 - (1 - 1/s)^n, \quad n \in \mathbb Z$$

The set $\{G_n : n \neq 0\}$ forms vector space basis of Li class $\mathcal L$.

## Theorem 3.1 (paper-direct)
$$\langle G_n, G_m \rangle_{\mathcal W(\pi)} = \lambda_n(\pi) + \lambda_{-m}(\pi) - \lambda_{n-m}(\pi)$$
In particular:
$$||G_n||^2_{\mathcal W(\pi)} = \lambda_n(\pi) + \lambda_{-n}(\pi) = 2\Re(\lambda_n(\pi))$$

## 의미 (paper-direct)

[rigorous]:
- Li positivity $\Re(\lambda_n) \ge 0$ ⟺ $||G_n||^2 \ge 0$ — Weil scalar product positive semidefinite **on $G_n$ basis**.
- 즉 *Li coefficient = Weil norm of specific test function*.
- Test function basis $\{G_n\}$ 가 *Li class $\mathcal L$* 의 basis — Li 동치의 *operational* version.

## Lemma 4.2 (paper §4, Arithmetic decomposition)

$$\lambda_n(\pi) = S_\infty(n, \pi^\vee) - S_f(n, \pi^\vee) + \delta(\pi)$$
- $S_\infty$ = archimedean places contribution.
- $S_f$ = finite places contribution.

## Theorem 5.1 (paper §5, *unconditional* archimedean asymptotic)
$$S_\infty(n, \pi) = (N/2) n \log n + C_1(\pi) n + O(N(K(\pi)+1))$$
*unconditional* (RH 무관).

→ RH for $\xi(s, \pi)$ 가 들어가는 부분은 $S_f$ (finite places). archimedean 은 Stirling 만으로.

## Wall mapping (paper-direct)

- Wall #4 (CONSPIRACY) 와 직접: family $\pi$ 에 대한 λ_n(π) ≥ 0.
- Wall #1 (FROBENIUS-GAP) 의 number field 형: Weil scalar product 위 G_n basis.
- Lemma 3 (positivity unification) 의 *operational* form — G_n basis 가 *test function set*, $||G_n||^2 = 2\Re(\lambda_n)$.

[증명 X]: *우리 contribution = paper-direct mapping*. *novel content X*. yellow flag word *avoided* (045 protocol).

## "예상 가능 결과" self-check
yes — Lagarias paper-direct.
