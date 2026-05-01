# Work — Attempt 030 (Sierra 2007)

## §I-IV 정독

### Setup
- $H_0 = xp$ + non-local interaction $V$ (two potentials a(x), b(x)).
- Inverse Hamiltonian $1/H = 1/H_0 + V'$.
- Spectrum determined by Jost function $J(E)$ in upper half plane.

### Self-adjoint extensions (paper Table 2)
| Type | Interval (a,b) | Deficiency indices (n_+, n_-) | Self-adjoint? |
|---|---|---|---|
| BK (Berry-Keating) | (1, ∞) | (1, 0) | No |
| C (Connes) | (0, N) | (0, 1) | No |
| S (Sierra) | (1, N) | (1, 1) | **Yes** (parameterized) |
| T | (0, ∞) | (0, 0) | Yes (essentially) |

Sierra type S: 1-parameter family of extensions $\theta \in [0, 2\pi)$.

### 핵심 결과 (paper §IV)
- Resonances on real axis (bound states) or below (resonances).
- Potentials chosen → resonances *asymptotically converge* to Riemann zeros.
- *Single* potential 이 *모든 영점* 매칭 못 함 (paper 자체 인정 §IV).
- Eq. (39): $h_D = E$ — coupling constant ↔ energy linear (cf. Khuri / Chadan: $\lambda = s(s-1)$).

### Wall #5 lemma 적용 (lemma step 6)

[rigorous, paper-direct]:

Sierra 2007 의 모델은 lemma `spectral_candidate_circularity_check.md` 의 step 6 *exactly*:
- (1)~(2): boundary condition + spectrum 정의 가능.
- (3): ζ-related (asymptotically).
- (4): trivial 부분 — "spectrum identification" 자체.
- (5): self-adjointness type S 에 대해 *parameterized*.
- (6): **single Hamiltonian for all zeros 미발견** — Sierra 자체 인정 (§IV).

→ Sierra 2007 의 *RH 증명 후보 X*. 다른 동치 reformulation. lemma 적용 작동.

### 본 시도의 honest 결과
- lemma `spectral_candidate_circularity_check.md` 가 *Sierra 사례에 자동 적용* — 우리 비판적 reading template 의 실용 검증.
- Wall #5 의 *paper-direct* status 한 번 더 확정.
- *novel content X*.

## "예상 가능 결과" self-check
yes — Sierra 자체 honest 인정.
