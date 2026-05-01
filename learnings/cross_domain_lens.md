# Cross-domain Lens — 누적 유추·도구 임포트 기록

> HARNESS.md §6 의 Cross-domain pass 결과를 시도 가로질러 누적. *어느 분야의 어떤 도구를 RH에 적용했고 결과는?*

## 사용법

각 시도 종료 후 본 파일에 1줄 ~ 1단락 추가. 형식:

```
- [attempt NNN] 분야: <field> | 도구: <tool> | 시도: <어떻게 적용> | 결과: [부적합 / 부분 통찰 / 추가 시도 가치]
```

## 누적 (시간순)

- **[000]** 분야: 통계물리 (Lee–Yang) | 도구: ferromagnet partition function 영점이 단위원 위 정리 | 시도: brainstorm — 직접 ζ import 채널 명시 | 결과: 미시도, 후보 (003_byproduct_search 의 일부)
- **[000]** 분야: 신호처리 | 도구: minimum-phase / linear-phase 필터 영점 위치 | 시도: brainstorm — mollifier 의 filter 재해석 가능성 | 결과: 미시도, 후보 (벽 #3 SHARP-CONSTANT 우회)
- **[000]** 분야: 최적수송 | 도구: Wasserstein gradient flow + Lott–Sturm–Villani synthetic Ricci | 시도: 후보 002 의 핵심 채널 | 결과: 시도 002 에서 검증 예정
- **[000]** 분야: 자유확률 (Voiculescu) | 도구: free convolution, free moments | 시도: 후보 A (001) 의 sub-channel | 결과: 시도 001 에서 검증 예정
- **[000]** 분야: 양자물리 (PT-symmetric) | 도구: Bender 류 PT-symmetry, broken/unbroken | 시도: BBM 비판적 검토 | 결과: self-adjointness gap 식별 (벽 #5)
- **[000]** 분야: 동역학계 / Coulomb gas | 도구: Calogero–Moser integrable | 시도: brainstorm — Rodgers–Tao 의 ODE 와 직접 동형 | 결과: 후보 002 의 보조 채널
- **[001]** 분야: 자유확률 (Voiculescu) | 도구: R-transform of generating function Σ λ_n z^n | 시도: brainstorm (specialist S11 의 반환 라운드 부산물) | 결과: 미탐색, 후보 (`004_li_lambda_rtransform`)
- **[001]** 분야: 신호처리 (power spectrum) | 도구: λ_n sequence 의 spectral analysis | 시도: 데이터 부족 (N=20) 으로 미실행 | 결과: defer — N 충분 시 재시도 가치

## 메타 패턴

도구 임포트가 N회 반복되면 여기에 패턴을 추출:
- 어떤 도메인이 RH와 *구조적으로* 가장 가까운가?
- 어떤 도메인이 *언어적*으로만 가깝고 실제론 멀었는가?
- 새로 떠오른 채널이 있는가?

## 알려진 (문헌상) cross-domain 다리 — 베이스라인

신규 시도가 이미 있는 다리를 재발견하지 않게 메모:

- **Hilbert–Pólya**: 자기수반 연산자 스펙트럼 → 실수성. (Berry–Keating, Connes 등이 채움 시도)
- **Random Matrix Theory**: Montgomery 1973 (pair correlation = GUE), Keating–Snaith 2000 (moments)
- **Adelic / NCG**: Connes 1999 trace formula (ADL)
- **Function field analog**: Weil 1948 — function field에서 Riemann hypothesis 증명됨. 본질적 도구는 *Frobenius eigenvalue + 양정치성*. number field 로 옮길 수 없는 이유가 핵심 막힘.
- **Dynamical / Foliated spaces**: Deninger 프로그램.
- **Lee–Yang 류**: Newman–de Bruijn (DBN constant). Tao–Rodgers 2020.
- **Quantum chaos**: Berry–Keating "H = xp" 류.

새 채널 후보 (아직 미숙·논쟁적·또는 우리가 시도 가능):

- **Free probability** (Voiculescu): RMT 의 비가환 일반화. ζ 모멘트 계산에 적용 가능?
- **Tropical geometry**: zeros 의 piecewise-linear 그림자?
- **Topological data analysis**: persistence of zero distribution?
- **Information theory**: ζ 와 entropy / KL divergence 연결?
- **Optimal transport**: zero density 의 Wasserstein?
- **Category theory / sheaves**: 영점 sheafification?
- **ML / approximation theory**: neural net 으로 ζ 근사 후 학습된 표현 분석?

(이 후보들은 brainstorming 단계 — 대부분 막다른 길일 가능성이 높음. 시도 시 literature 확인 의무.)
