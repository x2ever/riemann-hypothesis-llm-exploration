# Attempt 002: Harness Maintenance — 운영 결함 반영 + 도구 일반화
**Type**: C (Harness maintenance)

## 가설/전략

본 시도는 *증명 시도가 아님*. 000 + 001 에서 발견된 운영 결함 + 도구 부족을 *즉시 반영* 하여 다음 시도들의 효율 향상:

1. **결함 1 (S2/S3 confirmation bias)**: blind round protocol 을 SPECIALISTS.md 에 추가.
2. **결함 2 (S2 분리)**: S2 를 S2a (대수기하·function field) + S2b (대수적 정수론·Iwasawa) 로 분리.
3. **도구 일반화 (001 의 부산물)**: `tools/cross_check.py` — 임의의 두 RH-동치 quantity 의 cross-check framework. li_rmt 의 3-mode (naive/affine/rank) 패턴 추출.

## 동기

- 매번 같은 결함을 *재발견* 하는 것보다 한 번 정비.
- `tools/cross_check.py` 는 다음 attempts (002 unfolded pair correlation, 003 Keating-Snaith moments, 004 R-transform) 모두에서 재사용 가능.
- Type A/B 만 누적되지 않게 type 다양화 — *증명이 아닌 시도도 가치* 라는 사용자 원칙 따름.

## 산출물 (DoD)

- [ ] `SPECIALISTS.md` 의 §"Tier 1" 에 S2 → S2a + S2b 분리.
- [ ] `SPECIALISTS.md` 끝에 §"Blind round protocol" 추가 (결함 1 반영).
- [ ] `tools/cross_check.py` 작성 + smoke test.
- [ ] `tools/README.md` 갱신.
- [ ] `HARNESS.md` ledger 업데이트.

## 예상 막힘 지점
- 도구 일반화가 *과도한 추상화* 위험. li_rmt 가 working 하므로 그것의 *최소 일반화* 만.

## 명시적 비-실패
- Type C 는 *증명 시도 X* — 산출물 적게 나와도 "막힘" 아님. 향후 Type A 시도들이 본 산출을 활용 못 하면 그때 *재정비*.
