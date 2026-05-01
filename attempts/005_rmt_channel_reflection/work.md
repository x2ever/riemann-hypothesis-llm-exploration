# Work — Attempt 005 (Reflection)

## RMT 채널 3 시도 종합

### 001 (Li's λ_n vs RMT)
- **결과**: negative — naive cross-check 무의미 (벽 #6 LOCAL-GLOBAL-MISMATCH 발견).
- **원인**: λ_n 은 영점의 *global position* 의존, RMT 는 *local statistic* model.
- **얻은 것**: 도구 (3-mode framework), 새 벽 명시화.

### 003 (Unfolded pair correlation)
- **결과**: partial — KS p=0.056, deviation 발견.
- **원인 (사후 판명)**: normalization mismatch (pair correlation density vs probability density 혼동).
- **얻은 것**: 도구 한계 발견 → 004 의 깨끗 normalization motivation.

### 004 (Wigner surmise P(s))
- **결과**: positive — KS p=0.27 PASS.
- **원인**: 깨끗 PDF normalization, level repulsion + peak 위치 정확 정합.
- **얻은 것**: RMT 정합성 baseline 견고. Odlyzko millions 의 우리 N=300 부분 검증.

## 종합 평가

### RMT 채널의 *현재 상태*
- **알려진 사실 (Odlyzko)**: ζ 영점 statistics 가 GUE 와 millions of zeros 까지 정합.
- **우리가 추가한 것**: 도구 framework + LOCAL-GLOBAL-MISMATCH 명시화 + 우리의 N=300 baseline 검증.
- **새 정보 산출**: 거의 없음. *재발견* + *명시화*.

### 본 프로젝트의 *비교우위* 가 RMT 채널에서 발휘되었나?

**대체로 X**. 이유:
1. **RMT specialists 가 깊다**: Odlyzko, Keating, Snaith, Katz, Sarnak, Conrey, Soundararajan — 분야 specialist 가 우리보다 훨씬 깊은 도구 + 큰 sample size.
2. **우리 N 작음**: 300 영점 vs Odlyzko 의 $10^{20}$. 통계 power 절대 부족.
3. **cross-domain 활용 부족**: free probability (S11) 채널 brainstorm 만 — 실제 사용 X. 다른 분야 도구 임포트 미발현.
4. **LLM + code 의 *진짜* 강점**: literature 종합, *meta* 분석, *문제 변형*. RMT 의 raw 수치 검증보다 *접근법 간 결합* 또는 *비정통 채널* 에서 더 발현.

### 그러나 *negative finding* 의 가치

3 시도가 *RH 증명에 직접 기여 X* 이지만:
- 도구 (`tools/li_rmt.py`, `tools/cross_check.py`, `tools/pair_correlation.py`, `tools/spacing_distribution.py`) — *재사용 가능*.
- 벽 #6 명시화 — 다음 시도들의 *제거 도구*.
- 도구 framework — 다른 채널 (non-RMT) 에서도 활용 가능 trigger.

→ **방향 전환 시점**. RMT 채널은 *baseline 으로 두고* 다음 큰 시도는 *non-RMT* 에서.

## 다음 방향 결정

### 후보 종합

| 후보 | Type | 분류 | 우선순위 | 비교우위 발휘? |
|---|---|---|---|---|
| Keating-Snaith moments | A | VII (RMT extended) | 중 | △ (RMT specialist 영역) |
| Wall #2 forward heat (optimal transport) | A | VI + XI | 상 | ★★ (cross-domain 강점) |
| BBM finite truncation | A | III | 중 | ★ (code 활용 가능) |
| Lee-Yang positivity import | A | XI | 중 | ★★ (cross-domain) |
| Riemann 1859 explicit formula 직접 | A 또는 B | VII or meta | 중 | ★ (재해석) |
| Type E literature deepening | E | meta | 중 | ★ (다음 시도 입력) |
| Wall #1 FROBENIUS-GAP 직접 | A 야심 | IV+V | 하 | △ (specialist depth 부족) |
| Free probability R-transform (001 부산물) | A 탐색 | XI/XII | 중 | ★★ (미탐색 채널) |

### 결정

**다음 attempt 006 = Type A — Wall #2 (FORWARD-TIME) 도전 via optimal transport**.

근거:
- 본 프로젝트의 cross-domain 강점이 가장 발휘됨 (optimal transport ↔ heat flow ↔ RMT 의 다리).
- code 강점 활용 (Wasserstein 시뮬레이션, gradient flow tracking).
- 본질적 벽 #2 직접 도전 — 잘 안 되더라도 *벽의 정량화* 자체가 가치.
- 다음 *non-RMT* 시도 — type/topic 다양화.

**다음 attempt 007 = Type E — Literature deepening**:
- 006 시작 전 또는 이후, *Berry-Keating, Newman, Wasserstein gradient flow* 관련 논문 다운로드.
- WISHLIST 의 high-priority 정독.

**다음 attempt 008 = Type A — Free probability R-transform** (001 부산물).
- 미탐색 채널, high variance.

### HARNESS 메타 개선 후보 (Type C 후보)

본 reflection 에서 발견:
- Type 분포 추적: 000(B) 001(A) 002(C) 003(A) 004(A) 005(D) — Type 별 카운트 자동 표시 가치 (HARNESS ledger 에 column 추가).
- 채널 분포 추적: RMT 가 3/5 → narrow. 채널 다양성 강제 protocol 후보.

## 결론 (work)

본 reflection 의 핵심 결정: **다음 야심 시도 (006) 는 Wall #2 + optimal transport** — non-RMT cross-domain 채널.
