# Attempt 007: Wasserstein-2 Evolution of Zero Empirical Measure
**Type**: A (Proof attempt, computational, cross-domain)

## 가설/전략

006 의 직접 후속. ζ 영점 동역학을 *empirical measure* $\mu_t = (1/N) \sum_k \delta_{x_k(t)}$ 의 evolution 으로 보고 Wasserstein-2 metric 위 *integrated* 거동 추적.

> **H1**: $\mu_t$ 의 W₂-distance to fixed reference measure (ζ 의 t=0 분포) 가 |t| 따라 *어떻게* 변하는가? 단조 X / 단조 ↑ / 단조 ↓ ?
>
> **H2**: 만약 W₂² 의 시간 미분이 forward-time 에서 *bounded* (closed 형태) → Wall #2 refined 의 우회 후보.
>
> **H3**: $\frac{1}{2} \frac{d}{dt} W_2^2(\mu_t, \mu_{t_0})$ 의 *Otto's calculus* 형식이 ∫E(t)dt 와 어떤 관계?

## 동기

- 006 에서 wall #2 refined: ∫E(t)dt unconditional bound 부재.
- Otto's calculus: gradient flow on probability measures, $\frac{d}{dt} W_2^2 = -2 \langle \nabla \text{functional}, \cdot \rangle$.
- Wasserstein 는 cross-domain 강점 (synthetic Ricci, Lott-Sturm-Villani, Otto's calculus).

## 분류
- VI (heat flow) + XI (optimal transport) + IX (computational).

## DoD
- [ ] `tools/wasserstein_evolution.py` — W₂ 시간 추적
- [ ] N=20 영점 forward/backward integration + W₂ history plot
- [ ] $\frac{d}{dt} W_2^2$ 의 수치 vs energy E(t) 비교
- [ ] postmortem 결론
