# Work — Attempt 046 (Mertens partial sums)

[numerical, x ≤ 10000]

## Mertens M(x) sample

| x | M(x) | M(x)/√x |
|---|---|---|
| 500 | -6 | -0.268 |
| 1000 | 2 | 0.063 |
| 3500 | 12 | 0.203 |
| 7000 | -25 | -0.299 |
| 8500 | 29 | 0.314 |
| 10000 | -23 | -0.230 |

## 분석 (suppressed confidence)

[rigorous]:
- 작은 x (≤ 10000) 에서 |M(x)| / √x ≤ 0.32. *Mertens 추측* (|M|/√x ≤ 1) 와 일관.
- 1985 Odlyzko-te Riele 가 *Mertens 추측* (≤ 1) 의 반증 — 첫 violations 가 *큰* x 에서. 우리 small x 에선 발견 X — *알려진 사실*.
- *RH-equivalent* M(x) = O(x^(1/2+ε)) 는 *Mertens 추측보다 약함*, 여전히 미해결.

[증명 X]:
- 본 시도가 RH 증명·반증 contribution **0**.
- 기존 도구 mertens.py 의 sanity check 만.
- *우리 contribution*: 작은 x 에서 numerical sample, paper 의 SOTA (Odlyzko 등의 *큰* x 에서 violations 확인) 에 비해 trivial scale.

## Yellow flag self-check (045 protocol)
- "resolved" / "evidence 강화" / "consistent" 사용 X.
- *novel content X* 명시.

## "예상 가능 결과" self-check
yes — Mertens function 의 standard partial sums.
