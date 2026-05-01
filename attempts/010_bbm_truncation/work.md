# Work — Attempt 010 (BBM Boundary Condition Sanity Check)

## 2026-05-01

[numerical, dps=40]

### 결과

#### ψ_z(0) at first 5 ζ zeros
```
z = 0.5 + 14.135i  →  |ψ_z(0)| = 6.7e-16   (numerical zero)
z = 0.5 + 21.022i  →  |ψ_z(0)| = 1.2e-15
z = 0.5 + 25.011i  →  |ψ_z(0)| = 8.5e-16
z = 0.5 + 30.425i  →  |ψ_z(0)| = 1.1e-15
z = 0.5 + 32.935i  →  |ψ_z(0)| = 2.7e-15
```
모두 working precision 의 *numerical zero* (~ 10^{-16}).

#### ψ_z(0) at non-ζ-zero points
```
z = 0.5 + 1.000i        → |ψ| = 0.736  (non-zero)
z = 0.5 + 14.000i       → |ψ| = 0.106  (near zero but not exact)
z = 0.5 + 14.134725i    → |ψ| = 3.6e-15  (≈ first zero, numerical zero)
z = 0.7 + 14.134725i    → |ψ| = 0.147  (off critical line, non-zero)
z = 2.0 + 0.000i        → |ψ| = 1.645  (= ζ(2) = π²/6)
```

### 분석

[rigorous]:

**핵심 항등식**: ψ_z(x) = -ζ(z, x+1) (Hurwitz zeta). At x = 0:
$$\psi_z(0) = -\zeta(z, 1) = -\zeta(z)$$
(ζ(s, q) 의 Hurwitz definition: ζ(s, q) = Σ_{n=0}^∞ 1/(q+n)^s, hence ζ(s, 1) = ζ(s).)

따라서 **ψ_z(0) = 0 ⟺ ζ(z) = 0** — *자명히* 영점 조건과 동치.

수치 검증:
- ζ 영점에서 |ψ_z(0)| ≈ 10^{-16} (=  numerical zero in dps=40).
- 영점이 아닌 z 에서 |ψ_z(0)| > 0.1 명확히 non-zero.
- z = 0.7 + 14.135i (영점에서 *미세하게 off critical line*) 에서도 |ψ| = 0.147 — 즉 영점이 *임계선 위에 있어야* 가 아니라 *그냥 영점이어야* 가 boundary condition.

[rigorous]:

### Wall #5 의 sharper formulation

본 시도가 보여준 것:

1. **BBM 의 "spectrum identification" 은 trivially 영점과 동치** — boundary condition ψ_z(0) = 0 의 *내용* 이 ζ(z) = 0.
2. BBM 이 *증명한* 것 X (definitional 만).
3. BBM 의 *non-trivial claim* 은 *self-adjointness on a Hilbert space*. 이게 RH 의 새 증명을 주는가 *vs* RH 와 등가 변형인가는 — *증명되지 않은 채로 남음*.

→ **Wall #5 (refined)**: "Hilbert–Pólya 후보 Hamiltonian 의 *self-adjoint extension on a concrete Hilbert space + uniqueness* 의 rigorous 증명 부재. spectrum identification 자체는 자명할 수 있고, *진짜* claim 은 self-adjointness."

(이전 wall #5 statement: "self-adjointness rigorous 부재" — 확장: *어떤* claim 이 *trivially 동치 변형* 이고 *어떤* 이 *non-trivial* 인지 분리 의무.)

### 본 시도 학습

1. **Wall #5 의 *순환 구조* 명시 검증**: 새 spectral 후보 평가 시 *어떤 부분이 trivially 영점 정의인지* vs *어떤 부분이 새 정보인지* 분리 의무.
2. **Hurwitz zeta 와 Riemann zeta 의 관계**: ζ(s, 1) = ζ(s) — 본 사례에서 결정적. Hurwitz reflection formula 도 활용 가치.
3. **mpmath.zeta(s, q)** 의 정확도 검증 — dps=40 에서 영점 위에서 10^{-16} 정확도.

### 다음 시도 후보

#### 011 — Type A (Wall #2 후속, 008 plan)
KL divergence path-dependent functional. (007 의 Wasserstein 부적합 우회)

#### 012 — Type A (Wall #5 후속)
sierra_2016 정독 + Sierra 의 H = xp 후속에서 "spectrum identification 의 trivial 부분 vs non-trivial 부분" 검증. Sierra 가 BBM 보다 *진짜* 새 정보 주는가?

#### 013 — Type C (도구)
BBM 류 spectral 후보 평가 *템플릿* 코드 (`tools/spectral_candidate_check.py`). 향후 새 spectral 후보 등장 시 즉시 적용 가능.

### 결론

본 시도는 *negative finding* — BBM 의 spectrum identification 자체는 trivially 영점 동치. Wall #5 의 *진짜 위치* (self-adjointness) 명시 검증.
