# Work — Attempt 038 (Pratt-Robles §5)

## §5 (Feng's conjecture proof) 정독

### Setup
- Mollifier coefficient $a_d = b_d + c_d$ where:
  - $b_d = \mu(d) P(\log N/d / \log N) \sum (\log q_1)(\log q_2) / (\log N)^2$ — Feng coefficient.
  - $c_d$ = correction, vanishes unless $d = p^k m$ ($k \ge 2$, $(m, p) = 1$, $m$ squarefree).
  - $c_d = (\log p)^2 \mu(m) / (\log N)^2$.

### Type I / II bounds
- Kloosterman sums (Deshouillers-Iwaniec, Bettin-Chandee-Radziwill) → mollifier extension.
- Type I bound: $(1+|w|)T^\varepsilon (AV^{3/2} W + AUV^{1/2})$.
- Type II bound: $\sum \nu(a) \sum r(v) \sum_{ef} \alpha(e)\beta(f) e(-a\overline{hef}/v)$.
- N = $T^{4/7 - \varepsilon}$ permissible (improved from Conrey's $\theta = 4/7$).

### Wall #3 의 *log 단위 한계* (paper §5.1.3 직접)

> "Observe that we could have afforded to lose one more logarithm, and we still would have had an acceptable bound. The reason for this is that since we are looking at Feng's K=2, we get to divide by two logarithms in order to make the coefficients bounded. However, the difference between Feng's K=2 and our K=2 is like a Conrey mollifier on average, which already has bounded coefficients. **This accounts for our bound being one logarithm smaller than we actually need it to be.**"

[rigorous]:

→ Wall #3 의 *진짜 정체*:
- mollifier 의 *log 단위* (precisely 1 logarithm) 가 *technical engineering* 으로 push 가능.
- 50% 벽 자체 = Cauchy-Schwarz sharp constant + Type I/II Kloosterman bounds 의 *integrated limits*.
- *본질적 새 도구* 없이는 50% 벽 못 넘음 (Iwaniec-Sarnak §2 의 (A2) 와 일관).

### 본 시도 honest 결과

[rigorous, paper-direct]:
- Wall #3 의 *quantitative* refinement: 50% 벽이 *log 단위 시간거리*.
- 본 paper 의 5/12 ≈ 41.667% 가 그 거리의 일부 push.
- *novel content X*. paper-direct.

## "예상 가능 결과" self-check
yes — Pratt-Robles paper 자체 인정.

## Lemma extraction trigger
*lemma X*. wall sharpening only.
