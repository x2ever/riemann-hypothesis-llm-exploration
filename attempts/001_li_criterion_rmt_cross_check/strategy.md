# Attempt 001: Li's λ_n vs RMT GUE Cross-Check
**Type**: A (Proof attempt, computational)

## 가설/전략

Li's criterion (`background/known_results.md` A15.4):
$$
\lambda_n = \sum_\rho \left[1 - \left(1 - \frac{1}{\rho}\right)^n\right], \qquad \text{RH} \iff \lambda_n \ge 0 \ \forall n.
$$

만약 ζ 영점이 GUE 의 *moment-matching* 분포와 정합이라면, λ_n 의 *기대값* 과 *분산* 이 GUE 무작위 행렬의 동등 quantity 로 예측 가능. 본 시도의 좁은 가설:

> **H1**: 첫 N 영점의 부분합 $\lambda_n^{(N)} := \sum_{|γ| \le γ_N} [1 - (1-1/\rho)^n]$ 의 *truncation 보정 후* 값이, 동일 size 의 GUE 행렬에서 계산한 동등 quantity 와 *통계적으로* 일치한다 (작은 n 에서).
>
> **H2**: 만약 어긋나면, 어긋나는 *방향* 이 RH 의 어떤 측면이 RMT 와 *분리되는지* 신호.

## 동기

- 두 RH-동치 (Li + RMT 정합성) 의 *교차 검증*. 같은 결과를 두 방향에서.
- 코드 강점: 둘 다 정밀 계산 가능.
- 결합 4 (II + VII + IX) 의 첫 instantiation.

## 분류 + Specialist 의무 호출

- **분류**: II (동치 변환 — Li) + VII (RMT) + IX (computational).
- **Tier 1 의무**: S1 (해석적), S4 (RMT), S5 (Tao 류).
- **Tier 2 추가**: S11 (자유확률 — RMT 일반화). 혹시 free probability 가 truncation 보정에 적합한 도구 제공하는지.

## Cross-domain Pass (HARNESS §6)

### A. 유추 sweep
- **신호처리**: λ_n sequence 의 *power spectrum* 분석 — RMT 가 예측하는 spectrum 과 비교.
- **확률**: λ_n 을 random partial sum 으로 보고 CLT (central limit theorem) 적용 가능?
- **물리**: Coulomb gas 의 *moment* — λ_n 이 그것에 어떻게 대응?
- **CS**: monte carlo + variance reduction (control variates).

### B. 도구 임포트
- *Free probability* (Voiculescu) 의 free cumulant — λ_n 의 RMT 대응이 free cumulant 로 깔끔해질 가능성.
- *Stein's method* — 정합성을 정량화 (분포 거리).

### C. 외부인 설명
- 통계학자: "이 실험의 *power*는? sample size 충분?" → 분산 추정 + sample size 결정.
- 물리학자: "λ_n 은 어떤 *thermodynamic* quantity 로 해석?" → free energy moments?
- 신호처리: "sign(λ_n) sequence 의 entropy 는?" → predictable vs random.

### D. 변형
- **약화**: H1 을 sign 만 (λ_n > 0 ∀n) 으로 약화 — 이미 알려진 (수치적). 본 시도는 *값* 수준.
- **강화**: λ_n + 분산 + 고차 모멘트 동시 일치 시도.
- **일반화**: 다른 동치 형태 (Mertens, Nyman) 와의 *공동* RMT 대응.

## Computational Verifications (HARNESS §8)

코드 핵심:
1. **λ_n^(N)** : 첫 N 영점으로부터 직접 계산 (`tools/li_criterion.py` 확장).
2. **GUE λ_n** : N×N GUE 행렬을 sample, 그 eigenvalue 에서 동등 quantity 계산.
3. **truncation 보정** : λ_n^(N) → λ_n 의 점근식. (Li 의 sum 무한 → 유한 보정.)
4. **분포 비교** : 1000 GUE samples 의 λ_n 분포에 ζ 의 λ_n 이 어디 위치?

신규 모듈:
- `tools/li_rmt.py` — GUE λ_n 시뮬레이션 + ζ 와 비교.

정밀도: mpmath dps=30 (충분), GUE 샘플 ≥ 200.

## 예상 도구
- `tools/li_criterion.py` (이미 존재) — 기존 함수 재사용.
- `tools/li_rmt.py` (신규) — GUE 시뮬레이션 + 통계 비교.
- `mpmath.zetazero` for 영점.
- `numpy.random` + `scipy.linalg.eigvalsh` for GUE (이미 dependency 에 있음).

## 예상 막힘 지점

미리 예측:

1. **truncation 보정의 정확도**: λ_n 의 무한합 truncation 보정 항을 정확히 계산 못 하면 H1/H2 검증 자체가 noise 에 묻힘.
2. **GUE size 와 ζ 영점 size 의 매핑**: GUE N×N 의 eigenvalue 가 ζ 의 첫 N 영점에 *어떤 normalization* 으로 대응? Keating-Snaith 의 normalization (height 에서) 사용해야.
3. **λ_n 의 정의역 차이**: Li's λ_n 이 ρ 자체 (complex) 의 합이지만 GUE eigenvalue 는 실수. Conjugate pairing 처리 후 비교 가능한지 확인 필요.

## 성공 기준 (DoD)

- [ ] `tools/li_rmt.py` 작성 + 실행 가능
- [ ] 첫 100 영점으로 λ_1, ..., λ_20 의 *값* 계산 + 200 GUE 샘플로 *예측 분포* 계산
- [ ] 비교 plot 또는 표 (`figures/`)
- [ ] *통계적 결론* 1줄: "정합 / 부분 정합 / 어긋남" + 정량 (예: z-score)
- [ ] cross-domain pass 결과 1단락
- [ ] postmortem 의 "다음 시도 후보" 1개 이상

## 명시적 실패 기준

- truncation 보정이 너무 부정확해서 H1/H2 검증 자체가 vacuous 면 → *계산 도구 자체가 sharp 하지 않음* 결론 + lesson, 시도 종료.
- GUE 와 정확히 일치 시 → "당연한 일치, 본 시도가 새로운 정보 안 줌" → 다음 시도가 *어긋나는 시나리오* 를 더 적극적으로 찾아야.
