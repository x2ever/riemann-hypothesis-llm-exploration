# Work — Attempt 002

## 2026-05-01 — Type C 빠른 정비

### Step 1. SPECIALISTS.md S2 분리 [completed]
- S2 → S2a (대수기하·function field) + S2b (대수적 정수론·Iwasawa·motivic).
- 시도가 의지하는 측면에 맞춰 호출.

### Step 2. SPECIALISTS.md Blind Round Protocol [completed]
- §"Blind Round Protocol" 추가:
  - A. 첫 패스 — blind (각자 독립).
  - B. 둘째 패스 — cross-examination + 모순 specialist 재호출.
  - C. 운영 효과: 진짜 분야 다양성 + 가짜 confirmation 차단.
  - D. ROI 매트릭스: 작은 시도 X, 큰 시도 의무.

### Step 3. tools/cross_check.py 일반화 [completed]
- li_rmt 의 3-mode 패턴을 generic framework 로 추출.
- `CrossCheckResult` dataclass: n_values, zeta_values, model_means, model_stds, z_scores, mode.
- `diagnose()` 메서드: PASS / OFFSET / STRUCTURAL / AMBIGUOUS 자동 분류.
- smoke test (synthetic ζ ≈ model) — PASS 정상.

[numerical, synthetic test] cross_check 의 STRUCTURAL diagnosis 가 attempt 001 의 결과를 자동 분류 가능 — 향후 시도들에서 재사용.

### Step 4. README + ledger 업데이트 — 완료 후
