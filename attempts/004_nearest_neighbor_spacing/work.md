# Work — Attempt 004

## 2026-05-01 — Run #1

[numerical, dps=30, N=300, bins=20]

### 결과

- #spacings = 299, mean = 1.0000 (normalization 정확).
- **KS statistic D_n = 0.0573**
- **KS p-value = 0.2724**
- **Verdict: PASS — consistent with Wigner GUE**

### Histogram (요약)

| s | P_emp | P_Wigner | ratio |
|---|-------|----------|-------|
| 0.075 | 0.0 | 0.018 | 0.0 (level repulsion ✓) |
| 0.375 | 0.334 | 0.381 | 0.877 |
| 0.675 | 1.048 | 0.827 | 1.267 |
| 0.975 | 1.159 | 0.919 | 1.262 (peak 위치 일치) |
| 1.275 | 0.669 | 0.665 | 1.006 |
| 1.575 | 0.312 | 0.342 | 0.913 |
| 1.875 | 0.178 | 0.130 | 1.376 |
| 2.025+ | 0.0 | small | 0.0 (tail sparse) |

### 분석

[rigorous]:
- 정확한 normalization 으로 *깨끗* 비교. 003 의 deviation 은 normalization artifact 였음 — 본 시도가 그것을 *직접 확인*.
- Wigner GUE 와 통계 정합. KS p=0.27 은 통계적으로 *deviation 신호 없음*.
- Level repulsion (s≈0) 정확 발현. Peak 위치 (s≈0.9) 정합.
- finite-N (300) 에서도 RMT universality 가 sharp.

[plausible]:
- 본 결과는 Odlyzko 의 millions 결과의 *low-height 부분 검증*. 새 정보는 아니나 *우리 도구의 정확성 baseline*.

### 결론

본 시도는 *positive*. 003 후속으로 normalization 정확화 → RMT 정합 확인. 첫 N=300 영점이 GUE Wigner surmise 와 KS p=0.27 통계 정합.

→ **RMT 정합성을 baseline 으로 사용 가능** — 다음 시도들이 RMT 정합을 *입력* (가정) 으로 사용해 다른 RH-동치 검증.

### 학습
1. **003 의 deviation 은 normalization artifact**: 본 시도가 *직접 확인*.
2. **RMT universality 의 sharpness**: N=300 (low height) 에서도 통계적으로 발현 — Odlyzko 결과의 보강.
3. **도구 검증**: `tools/spacing_distribution.py` 의 정확한 normalization framework 가 향후 RMT 비교에 baseline 역할.

### 향후 시도 후보

본 시도의 *positive* 결과로 다음이 자연스러움:

- **005 (Type D Reflection)**: 001+003+004 의 RMT 채널 종합. 무엇을 배웠고 다음 *non-RMT* 채널은 어디?
- **006**: Keating–Snaith moments — RMT 의 native quantity. 더 sharp 한 검증.
- **007**: 야심 — Wall #1 (FROBENIUS-GAP) 또는 Wall #2 (FORWARD-TIME) 직접 도전.
