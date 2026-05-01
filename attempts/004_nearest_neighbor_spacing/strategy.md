# Attempt 004: Nearest-Neighbor Spacing vs Wigner Surmise
**Type**: A (Proof attempt, computational)

## 가설/전략

003 의 *normalization mismatch* 를 회피. P(s) (nearest-neighbor spacing distribution) 는 *probability density* — 양쪽 normalization 명확.

> **H1**: 첫 N (=300) 영점의 unfolded nearest-neighbor spacing 의 empirical PDF 가 Wigner surmise $P_{GUE}(s) = (32/\pi^2) s^2 \exp(-4s^2/\pi)$ 와 *정합*.
>
> **H2**: 만약 systematic deviation 발견 시, deviation 의 *형태* 가 ζ 의 RMT 외부 측면 신호.

이번엔 normalization 깨끗 — KS p-value 가 *진짜* statistical 신호.

## 분류 + Specialist
- **분류**: VII (RMT) + IX (computational).
- **Tier 1 의무**: S1, S4, S5.

## DoD
- [ ] `tools/spacing_distribution.py`
- [ ] N=300 영점 P(s) histogram vs Wigner overlay
- [ ] KS test p-value
- [ ] postmortem 결론
