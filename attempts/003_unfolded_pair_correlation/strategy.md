# Attempt 003: Unfolded Pair Correlation — Low-Height Deviation
**Type**: A (Proof attempt, computational)

## 가설/전략

001 의 LOCAL-GLOBAL-MISMATCH (벽 #6) 우회 — *unfolded* zeros + GUE local statistic.

> **H1**: 첫 N 영점 (N=200~500) 의 unfolded pair correlation 이 GUE 예측 $1-(\sin \pi u / \pi u)^2$ 에 *얼마나* 정합? *low-height* 에서 RMT asymptotic 이 깨지는 정도 정량.
>
> **H2**: 만약 systematic deviation 이 발견되면, deviation 의 *형태* (small u / large u / oscillation) 가 RH 의 *어떤 측면* 이 RMT 외부인지 신호.
>
> **H3**: GUE 정합성이 *low-height 에서도* sharp 하게 성립하면 → RMT 의 universality 가 *우리 예상보다 강함*. 다음 시도에서 RMT 를 *더 신뢰* 할 수 있는 상한.

## 동기 (000 + 001 의 직접 후속)

- 001 의 부정적 결론 ("naive cross-check 무의미") 을 *unfolded* 로 우회 — 벽 #6 우회 후보의 첫 번째.
- 002 의 cross_check.py framework 시험 사용 (도구 설계 결함 발견 trigger).
- *Low-height* 에서의 RMT 정합 정량은 Odlyzko 가 millions 에서 했음. 우리는 *low-height* 에 한정 — 다른 정보 layer.

## 분류 + Specialist 의무 호출

- **분류**: VII (RMT) + IX (computational).
- **Tier 1 의무**: S1, S4, S5.
- **Blind round**: 작은 시도 — generalist 통합으로 충분 (Blind Round Protocol §D 의 ROI 매트릭스).

## Cross-domain Pass

### A. 유추
- *random matrix universality* (Erdős–Schlein–Yau, Tao–Vu): GUE 의 local statistics 가 *광범위한* 행렬 ensemble 에서 동일. ζ 가 그 universality class 에 있다는 evidence 의 정량 신호.

### B. 도구
- *Kolmogorov–Smirnov test*: empirical pair correlation 의 GUE 와의 거리 정량.
- *Wasserstein-1 distance*: 분포 비교의 다른 metric.

### C. 외부인
- *통계학자*: "sample size 가 적은데 KS test 의 power 는?" → bootstrap.
- *물리학자*: "low-height ≈ low-energy → Wigner-Dyson universality 의 *cross-over*?"

### D. 변형
- 약화: pair correlation 만 (3-pt, 4-pt 안 함).
- 강화: triple correlation 추가.
- 일반화: ζ 외에 Dirichlet L-function 의 첫 영점들도 unfolded 비교.

## Computational Verifications

### 코드
- `tools/pair_correlation.py` 기존 — N 늘려서 호출.
- `tools/unfolded_pc_extended.py` 신규 — KS test + Wasserstein + triple correlation.

### 데이터
- 첫 200 ~ 500 ζ 영점 (mpmath dps=30).
- 200 GUE 100x100 samples (이미 li_rmt 에서 검증).

### 정밀도
- mpmath dps=30 충분 (영점 imag part 6자리 정확).

## 예상 도구
- `mpmath.zetazero`
- `numpy.histogram`, `scipy.stats.kstest`
- 기존 `tools/pair_correlation.py` 의 `gue_density`

## 예상 막힘 지점

1. **첫 500 영점도 *low-height***: RMT asymptotic 이 깨질 수 있음. 그러나 깨지는 정량이 흥미.
2. **GUE 비교의 정확한 normalization**: Wigner semicircle 의 *bulk* density 와 unfolded ζ 의 비교는 *bulk-to-bulk* 매핑 필요.
3. **finite-size effect**: 200 영점은 RMT universality 의 sharp 검증에는 작음. statement 의 제약 명시 필요.

## 성공 기준 (DoD)

- [ ] `tools/unfolded_pc_extended.py` 작성 + 실행
- [ ] N=200 영점의 unfolded pair correlation histogram + GUE prediction overlay
- [ ] KS test p-value 계산
- [ ] postmortem 의 *deviation 의 형태* 분석 1단락
- [ ] 다음 시도 후보 1개 이상

## 명시적 실패 기준

- KS test p > 0.5 (정합성 강함) → 새 정보 X, "RMT universality 가 N=200 에서도 견고" 결론.
- KS test p < 0.05 (정합성 약함) → deviation 의 *형태* 가 흥미 — 다음 시도로 진화.
- *애매* (0.05 < p < 0.5) → sample size + bin 설정의 조정 필요, 본 시도 결론 미결.
