# Postmortem — Attempt 001

## 결론

**Negative finding (도구 명료화)**.

- H1 (naive cross-check) **기각**.
- H2 (어긋나는 방향이 정보) **부분 확인** — 분리 자체는 RMT 문헌에 알려짐.
- RH 증명 직접 기여 ✗.
- 도구 인프라 검증 ✅.
- *어떤 cross-check 가 informative 한지* 의 경계 명료화 ✅.

## 무엇이 작동했나

1. **3-mode 비교 framework** (`tools/li_rmt.py`) — naive / affine / rank — 각 mode 가 다른 정보를 줌. 한 mode 만으로는 분석이 불완전.
2. **반환 라운드 (HARNESS §7)** 첫 검증 — 작은 가치 산출. 큰 막힘 시도에서 더 의미.
3. **부산물 — S11 의 새 후보**: *Σ λ_n z^n 의 free probability R-transform*.

## 어디서 막혔나

- 본 시도는 *naive cross-check* 자체가 무의미함을 발견. 즉 "막힘" 이 아니라 "*잘못 가설* 임을 발견".
- 본질적 어려움: λ_n 이 영점의 *global position* 의존, RMT 는 *local statistics* 만 model — 두 동치 형태가 *서로 다른 정보 layer*.

## 알려진 벽인가, 새로운 벽인가

본 시도가 부딪힌 *암묵적 벽* — RMT 문헌 내에서 *알려진* 사실 ("RMT 는 local 만"). 본 프로젝트의 시각에선 *재발견*. 본질적 *새* 벽 X.

다만 본 시도의 *명시적* 형태로 인해 **새로운 wall 후보 추가**: 
**Wall #6 (LOCAL-GLOBAL-MISMATCH)**: ζ 의 *RH-동치 형태들* 이 *서로 다른 정보 layer* 에 sensitive. 직접 cross-check 가 무의미한 형태가 많다. (이는 Combo 4 의 자연 부정 — 동치 끼리 cross-check 하려면 *공통 layer* 필요.)

## 다음 시도 후보

### `002_unfolded_pair_correlation_extended`
**Type**: A (Proof attempt)

**가설**: ζ 영점을 unfold 후 GUE pair correlation 의 *higher-order correlation* (3-pt, 4-pt) 정합성 검증. 만약 어긋남 발견 시 RMT model 의 *limit* — RH 의 *어느 측면* 이 RMT 외부인지 신호.

- 분류: VII (RMT) + IX (computational).
- specialist: S4, S5, S1.
- 코드: `tools/pair_correlation.py` 확장 + `tools/triple_correlation.py` 신규.
- DoD: N=200 ~ 500 영점 + 비교 plot + n-pt correlation 비교.
- 가치: 작고 검증 가능. 본 시도의 *부정적* 결론 (raw 비교 무의미) 을 *공식 sharp* 비교로 진화.

### `003_keating_snaith_moments`
**Type**: A

**가설**: $I_k(T) = (1/T)\int_0^T |\zeta(1/2+it)|^{2k} dt$ 의 RMT 예측 ($g_k a_k (\log T)^{k^2}$) 을 작은 T 에서 수치 검증. 어긋남 발견 시 — 본 시도의 *local layer* 채널이 어디서 나뉘는지.

- 분류: VII + IX.
- specialist: S1, S4.
- 코드: `tools/moments.py` 신규.
- DoD: T ≤ 100 ~ 1000 + g_1, g_2, g_3 (and 큰 k 까지) 비교.
- 가치: Keating–Snaith conjecture 의 *작은 case* 검증. RMT 정합성의 *direct* 검증.

### `004_li_lambda_rtransform`  
**Type**: A (탐색적)

**가설**: 본 시도의 부산물 — Σ λ_n z^n 의 R-transform (free probability) 의 *형식 일치* 시도. 미탐색 채널.

- 분류: II + XI.
- specialist: S11 (자유확률) — Tier 3 추가.
- 코드: sympy + 수치 R-transform.
- DoD: 첫 20 λ_n 의 generating function 의 분석 + free probability 객체 후보 식별.
- 가치: high variance — 새 채널일 가능성 / 막다른 길일 가능성 모두.

## 추출된 보조정리/관찰

`lemmas/` 후보 없음 — 본 시도가 negative finding.

`learnings/walls.md` 에 **벽 #6 (LOCAL-GLOBAL-MISMATCH)** 추가.

## 학습 누적

- `learnings/walls.md` — 벽 #6 추가 ☐
- `learnings/cross_domain_lens.md` — S11 의 R-transform 후보 추가 ☐
- `learnings/specialist_consensus.md` — 첫 반환 라운드 결과 ☐
- `learnings/approaches_taxonomy.md` — Combo 4 의 한계 (LOCAL-GLOBAL-MISMATCH) 노트 ☐

## 메타 — 본 시도의 ROI

- **시간 비용**: 1 turn (낮음).
- **산출**: negative finding + tool + 다음 후보 3개 + 새 wall 후보.
- **중간 평가**: *효율적*. 본 시도가 만약 "RMT 와 정확 일치" 같은 trivially confirming 결과였으면 가치 더 적었을 것. *negative finding* 이 더 informative.
- **시사점**: type A 의 small computational 시도가 효율적인 *제거(elimination)* 도구. 큰 시도 (002 forward_heat) 전에 small 시도 여러 개로 *방향* 사전 점검.

## HARNESS 개선 후보 (Type C 후보)

- `learnings/walls.md` 에 *벽 #6* 자동 추가 — 향후 시도에서 LOCAL-GLOBAL-MISMATCH 점검 의무화.
- `tools/li_rmt.py` 의 3-mode framework 를 다른 RH-동치 cross-check 의 *템플릿* 으로 — `tools/cross_check.py` 일반화 가치.
