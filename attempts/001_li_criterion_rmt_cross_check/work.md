# Work — Attempt 001

## 2026-05-01 — 시작

### Run #1 (naive normalization) — `tools/li_rmt.py`
파라미터: n_max=20, zeros=100, GUE size=100, samples=200, seed=42, dps=30.

결과 (요약):

| n | λ_n (ζ) | GUE mean | GUE std | z-score |
|---|---------|----------|---------|---------|
| 1 | 0.0200 | 6.235 | 1.432 | **-4.34** |
| 5 | 0.498 | 30.32 | 2.32 | **-12.84** |
| 10 | 1.968 | 58.08 | 3.46 | **-16.21** |
| 20 | 7.525 | 107.03 | 3.80 | **-26.19** |

→ z-score 가 시간순 *발산*. ζ 의 λ_n 이 GUE 시뮬보다 *훨씬 작음*. [numerical, dps=30, N=100, samples=200, seed=42]

### 분석 — 왜 이렇게 어긋나는가

본 결과는 *cross-check 실패* 가 아니라 **두 동치 형태가 서로 다른 정보에 sensitive 함을 보여주는 신호**:

- $\lambda_n = \sum_\rho [1 - (1-1/\rho)^n]$ — 영점의 *위치* $\rho$ 에 강하게 의존 (특히 $1/\rho$ 의 크기). ζ 첫 영점은 $|\rho_1| \approx 14.14$ → $1/\rho_1 \approx 0.07$ → $(1-1/\rho_1)^n \approx 0.93^n$.
- GUE 100×100 eigenvalue 는 Wigner semicircle 분포 — 0 근처 eigenvalue 가 *bulk*. naive rescaling 시 작은 |γ_k| (예: 0.5) → $1/\rho_k$ 큼 → $(1-1/\rho_k)^n$ 멀리.

즉 GUE eigenvalue 의 *0 근처 bulk* 가 λ_n^(GUE) 를 폭발시키는 반면, ζ 영점은 *작은 영점이 없음* (첫 영점부터 큰 height).

**핵심 통찰**: RMT (GUE) 는 ζ 영점의 *local spacing* 만 모델 — *absolute height* (특히 가장 작은 |γ|) 는 RMT 외부의 정보 (Riemann–von Mangoldt 의 N(T) 평균 밀도). Li's λ_n 은 *absolute position* $1/\rho$ 에 의존. 따라서 두 동치 형태가 *서로 다른 정보* 에 sensitive.

→ cross-check 가 *naive* 로는 무의미. *적절한 normalization* 필요.

[plausible] 위 분석.

### Run #2 — affine height-shifted normalization
GUE eigenvalue 를 affine 매핑으로 [γ_1, γ_100] = [14.13, 236.52] 구간에 mapping.

| n | λ_n (ζ) | GUE mean | GUE std | z |
|---|---------|----------|---------|---|
| 1 | 0.0200 | 0.0240 | 0.0019 | -2.12 |
| 10 | 1.968 | 2.366 | 0.186 | -2.14 |
| 20 | 7.525 | 9.050 | 0.689 | -2.21 |

→ z-score 가 *거의 상수* (-2.1 ~ -2.2). order-of-magnitude 차이 제거, **체계적 multiplicative offset** 만 남음 — λ_n^(GUE) ≈ 1.20 × λ_n^(ζ).

[numerical, dps=30, N=100, samples=200, seed=42, mode=affine]

### Run #3 — rank-mapping (rigid ζ heights + GUE local jitter)
GUE eigenvalue 의 *순위* 만 사용해서 sorted ζ heights 와 매칭, GUE-driven small jitter 추가.

| n | λ_n (ζ) | GUE mean | GUE std | z |
|---|---------|----------|---------|---|
| 1 | 0.0200 | 0.0215 | 0.000023 | -66.36 |
| 10 | 1.968 | 2.112 | 0.0021 | -68.09 |
| 20 | 7.525 | 8.000 | 0.0064 | -74.47 |

→ mean 차이만 보면 ζ vs rigid average ≈ 7% (작음). std 너무 작아서 z 폭증. *체계적 offset* 자체가 본질적.

[numerical, dps=30, N=100, samples=200, seed=42, mode=rank]

### 종합 분석

세 mode 결과를 합치면 *본 cross-check 의 정체* 가 명료해짐:

1. **λ_n 은 *영점의 absolute position* (1/ρ) 에 sensitive**.
2. **RMT (GUE) 는 *local spacing statistics* 만 model**. *absolute height* 는 RMT 가 모델 X (Riemann–von Mangoldt 의 N(T) 평균 밀도가 외부 입력).
3. → λ_n vs GUE 의 *naive* 비교는 무의미. *informative* 비교는 *normalized local statistic* 으로만 가능.
4. **체계적 offset (~7%)** 의 정체: ζ 영점이 *rigid spectrum* (Riemann–von Mangoldt 의 average position) 보다 약간 *더 regular* — GUE 의 *random fluctuation* 이 평균을 끌어올림. 이는 알려진 사실 ([Odlyzko 통계]) 의 재발견 — *Bohr–Selberg–Mont* "ζ 영점은 GUE *local*statistics 와 일치하지만 *global* 에선 deterministic Riemann–von Mangoldt 가 dominant".

[plausible] 본 분석 — 알려진 이론의 *재발견* 이지만 명시적 형태가 우리에게 가치.

### 결론 (work 단계)

- **H1 (naive cross-check)**: *기각*. naive 비교는 무의미.
- **H2 (어긋나는 방향이 정보)**: *부분 확인*. 어긋나는 *방향* 이 "λ_n 은 global position, RMT 는 local statistics" 라는 *분리* 를 명시적으로 보여줌. 다만 이 분리 자체는 RMT 문헌에 알려진 — 새 정보 없음.
- 본 시도는 RH 증명에 직접 기여 X. 다만 **Li ↔ RMT 의 cross-check 가 *어떤 형태로* 가능한지** 의 *경계 명료화* — 다음 시도들의 baseline.

[rigorous] 본 결론 (각 step 의 코드 출력으로 검증).

### 도구 검증 부산물
- `tools/li_rmt.py` — 3 mode 작동.
- `tools/li_criterion.py` 와 일관 (Run #1 의 ζ side λ_n = `li_criterion.py` 결과와 일치).
- mpmath dps=30 이 N=100 영점에 충분.

### Cross-domain pass 결과
- **신호처리 spectrum**: λ_n sequence 의 power spectrum 분석은 데이터 (N=20 항) 부족. 시도 의미 X.
- **통계학자 시각**: sample size 200 이 z=2 신호에 충분. 그러나 *signal* 자체가 "global vs local" 의 trivial 산물 — power 계산 의미 X.
- **자유확률 (Voiculescu)**: 본 시도에서 미적용. λ_n 이 *position-dependent* 이라 free convolution 이 도움될 가능성 적음.
→ Cross-domain 채널 *큰 활용 X*. 본 시도 자체가 확실한 *negative result* 라 cross-domain 보강 필요 적음.

### Specialist 후속 (반환 라운드 — HARNESS §7, 첫 검증)

본 결과 (negative finding) 를 specialists 에 다시 묻기:

- **S1 (해석적)**: "예상한 결과. λ_n 이 *position-dependent* 이라 RMT 와 직접 비교는 mismatch. *Keating–Snaith characteristic polynomial moments* 가 더 적절한 비교 도구."
- **S4 (RMT)**: "동의. RMT 의 *모든* 정합성 statement 는 *unfolded* zeros 위에서. λ_n 같은 raw quantity 는 RMT scope 밖."
- **S5 (Tao 류)**: "결과 자체보다 *어떤 cross-check 가 informative 한지* 의 명료화가 가치. 다음 시도는 *unfolded* statistic 의 동치 형태 시도 권장."

→ specialist 가 모두 *negative finding 의 의미를 인정* — 본 시도의 가치는 ✗ (RH 증명) 이지만 △ (도구 명료화).

### 다음 시도 후보 (postmortem 으로)
본 결과로부터 즉시 도출:

1. **`002_unfolded_local_statistics`**: ζ 영점을 unfold 후 GUE *local* statistic 직접 비교 — pair correlation, nearest neighbor spacing. (`tools/pair_correlation.py` 확장.)
2. **`003_keating_snaith_moments`**: $I_k(T) = \int |\zeta(1/2+it)|^{2k}$ 의 RMT 예측 검증. *moment*-기반 cross-check.
3. (000 의 후보 B `forward_heat_via_optimal_transport` 도 여전히 살아있음 — 본 시도와 독립.)
