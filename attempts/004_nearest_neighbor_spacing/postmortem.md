# Postmortem — Attempt 004

## 결론

**Positive — RMT 정합 확인**.

- KS p=0.27 → PASS (Wigner GUE 정합).
- 003 의 deviation 은 *normalization artifact* 확인.
- **RMT 정합성이 N=300 에도 sharp** — 향후 RMT 가정의 baseline 견고.

## 무엇이 작동했나

1. **깨끗한 PDF normalization**: 003 의 ratio mismatch 회피 — KS test 가 진짜 statistical signal.
2. **Wigner surmise**: GUE 의 분석적 근사로 sample 무의존, 1% 정확도. 빠른 비교.
3. **자기 비판 → 도구 진화**: 003 에서 발견한 normalization 문제를 004 에서 즉시 해결.

## 어디서 막혔나

- 막힘 X. 본 시도는 quantitative result 로 종결.

## 알려진 벽인가, 새로운 벽인가

**없음**. 본 시도는 RMT 의 알려진 universality 의 low-height 보강 — 도구 검증.

## 다음 시도 후보

본 시도의 positive 결과로 *RMT 정합을 가정* 가능. 다음 야심:

### 005 (Type D — Reflection)
**가설/목적**: 001+003+004 의 RMT 채널 *종합 reflection*. 무엇을 배웠는가? RMT 가 어디까지 sharp 하고 어디서 깨지는가? 다음 *non-RMT* 채널 결정.

- 분류: meta.
- DoD: RMT 채널의 positive/negative 결과 종합 + 다음 후보 1~3개.

### 006 — Keating–Snaith moments (Type A)
**가설**: $I_k(T) = (1/T)\int_0^T |\zeta(1/2+it)|^{2k} dt \sim g_k a_k (\log T)^{k^2}$. $g_3 = 42, g_4 = 24024$ 까지 *작은 T 에서* 검증.

- 분류: VII + IX.
- 도구: `tools/moments.py` 신규.
- 가치: RMT 의 *deeper* test.

### 007 — Wall #2 (FORWARD-TIME) 도전 (Type A 야심)
**가설**: Rodgers–Tao 의 backward heat flow 분석을 *forward* time 으로 변환 시도. Wasserstein gradient flow 또는 *time-reversal symmetry* 도구.

- 분류: VI + XI (optimal transport).
- 가치: 본질적 벽 직접 도전.

## 추출된 보조정리/관찰

- 정량 statement: **첫 300 ζ 영점의 unfolded nearest-neighbor spacing distribution 이 Wigner GUE 와 KS p=0.27 정합.**
- 이건 알려진 사실의 우리 도구 검증 — `lemmas/` 분리 가치 X (재현 가능 numeric).

## 학습 누적

- `learnings/walls.md` — 003 의 #7 (NORMALIZATION-MISMATCH) 가 *해결됨* 표시 ☐
- `learnings/specialist_consensus.md` — S4 의 RMT 정합 baseline 강화 ☐
- `learnings/approaches_taxonomy.md` — Combo (II + VII + IX) 가 *unfolded-PDF normalization 에서* 작동 ☐

## HARNESS 갱신
- ledger 에 004 추가.

## 메타

- 첫 *positive* 시도 — small but solid.
- 001 (negative) → 002 (harness) → 003 (partial) → 004 (positive) 의 진행이 healthy 패턴 — *negative finding 도 도구 진화로* 가치.
- 다음 시도 type 다양화: 005 = Type D 권장 (D 는 아직 미시도).
