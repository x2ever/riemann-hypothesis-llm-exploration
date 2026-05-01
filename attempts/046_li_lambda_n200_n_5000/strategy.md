# Attempt 046: Mertens function partial sums (Type A small)
**Type**: A (Computational, sanity-checked)

## Positivity component
- M(x) ↔ RH (A15.3 known_results.md). 본 시도: 작은 x 에서 M(x) 의 부호 변동 + magnitude 추적.

## DoD
- M(x) for x = 1..10000.
- Mertens 추측 |M(x)| ≤ √x 의 violations 카운트 (alleged Odlyzko-te Riele 1985 disproof — 작은 x 에선 발견 X).
- 우리 contribution 0, paper-direct fact 의 우리 도구 검증.

## Yellow flag self-check (045 protocol)
- "evidence" / "resolved" / "강화" 사용 X.
- *novel content X*.
