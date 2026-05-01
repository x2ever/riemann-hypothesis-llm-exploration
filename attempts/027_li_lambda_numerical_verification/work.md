# Work — Attempt 027

## Lagarias asymptotic vs 200 zeros 부분합

[numerical, dps=40, N=1, 200 zeros]

| n | λ_n (200 zeros 부분합) | Lagarias asymptotic | ratio |
|---|---|---|---|
| 1 | 0.021 | -1.130 | -0.019 |
| 5 | 0.524 | -1.628 | -0.322 |
| 10 | 2.073 | 0.210 | 9.89 |
| 20 | 7.945 | 7.351 | **1.08** |
| 50 | 38.38 | 41.28 | **0.93** |

(Lagarias paper §1.13: $C_1 = (1/2)(\gamma - 1 - \log 2\pi) \approx -1.130$ for ζ.)

### 분석

[plausible]:

- 작은 n (1, 5): asymptotic 의 *constant* 지배, $n \log n$ 작음. 우리 부분합과 큰 차이 — *truncation effect* (200 zeros 만).
- 큰 n (20, 50): $n \log n$ 항 지배, 우리 부분합과 ratio ≈ 1 — *positive confirmation*.
- 이는 알려진 사실의 *우리 도구의 정확성* numerical 검증.

### Wall 진행 X

본 시도는 *알려진 결과 numerical 확인*. Wall sharpening 또는 우회 X.

### "예상 가능 결과" self-check

*yes*. paper-direct asymptotic 의 trivial numerical instance.

## 메타

- 외부 critique 와 일관: *novel content X*.
- *small numerical work* — 도구 정확성 보강.
