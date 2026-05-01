---
title: "Numerical evidence — paper-direct 수식, mpmath data tables"
parent: 한국어
nav_order: 17
date: 2026-05-02
---

# Numerical evidence — paper-direct 수식, mpmath data tables

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/17-numerical-evidence/) · *2026-05-02*

> 프로젝트가 published 수식 대비 실행한 구체적 numerical sanity-check 모음. 어느 것도 새 정리 아님 — established RH-equivalent statements의 *empirical confirmation*. 모든 계산 `mpmath` 고정밀 (dps = 30~50).
>
> **본 post의 이유**: reader가 *"실제 수식·도출은 어디?"*라고 물었음 — 정확한 지적. 프로젝트 `attempts/` 로그에는 paper-direct 수식 사용 numerical 작업 substantial하나 블로그에서 surface 안 됐음. 본 post가 가장 관련 있는 data tables를 inline으로 모음.

## 1. Voros 2006 tempered asymptotic — Li 계수 $\lambda_n$

**Setup (Voros 2006, "Sharpenings of Li's criterion for the Riemann hypothesis")**

Li 계수 정의:
$$\lambda_n = \sum_{\rho} \left(1 - \left(1 - \tfrac{1}{\rho}\right)^n\right)$$
비자명 $\zeta$-zeros $\rho = 1/2 + i\gamma$ 합 (multiplicity, conjugate-paired). Li criterion (1997):

$$\mathrm{RH} \iff \lambda_n \geq 0 \text{ for all } n \geq 1.$$

**Voros 2006 sharp dichotomy (paper §1, Theorem)**:

- *RH true* (tempered): $\lambda_n \sim \frac{n}{2}\left(\log n - 1 + \gamma - \log 2\pi\right) + o(n)$
- *RH false*: $\lambda_n \sim \sum_{|z_k|<1} z_k^{-n} + \overline{z_k}^{-n}\ \mathrm{mod}\ o(e^{\varepsilon n})$, $z_k = (\tau_k - i/2)/(\tau_k + i/2)$ off-line zeros — *exponentially growing oscillations*.

Large-$n$ limit에서 mutually exclusive.

**프로젝트 numerical run** (`mpmath`, dps=50, 500 zeros, $C_1 = (\gamma - 1 - \log 2\pi)/2 \approx -1.130$):

| $n$ | $\lambda_n^{(500)}$ (partial sum) | Voros prediction | ratio | sign |
|---|---|---|---|---|
| 10 | 2.16 | 0.21 | 10.33 | + (sub-asymptotic) |
| 50 | 40.66 | 41.28 | **0.985** | + (sweet spot) |
| 100 | 107.12 | 117.23 | **0.914** | + (good agreement) |
| 200 | 260.77 | 303.77 | 0.859 | + |
| 500 | 707.36 | 988.49 | 0.716 | + (truncation begins) |
| 1000 | 1218.90 | 2323.55 | 0.525 | + |
| 2000 | 1367.54 | 5340.24 | 0.256 | + (truncation dominant) |

**관찰** (paper-direct, 새 claim 아님):
1. **Sweet spot $n \approx 50$**: ratio $\approx 1.0$ — Voros tempered prediction과 quantitative agreement.
2. **모든 $n$에서 $\mathrm{sign}(\lambda_n) = +$**. Voros *RH-false* case (exponential oscillations)는 *관찰되지 않음* — verified region에서 RH true와 consistent.
3. **Truncation effect**: $n > 200$에서 ratio 감쇠 — partial-sum over 500 zeros가 contribution under-count. 더 많은 zeros → 더 큰 valid $n$ range.

이건 **새 의미**의 RH evidence 아님 — `li_criterion.py` tool이 Voros published asymptotic 재현하는지 numerical sanity-check. SOTA RH numerical verification (Platt-Trudgian 2021, $H = 3 \times 10^{12}$)은 본 프로젝트 500-zero scale보다 many orders 위.

## 2. Lagarias 2002 — Eq. (2.18), $\lambda_n$ via power sums $\sigma_j$

**Setup (Lagarias 2002, *Acta Arith.*)**

Inverse $\zeta$-zeros power sums:
$$\sigma_j := \sum_{\rho} \frac{1}{(\rho(1-\rho))^j}\ \text{(대략; 정확 정의는 paper §2)}$$

Lagarias paper §2 Eq. (2.18):
$$\lambda_n = \sum_{j=1}^n (-1)^{j-1} \binom{n}{j} \sigma_j$$

**프로젝트 numerical 검증** (`mpmath`, dps=40, 200 zeros + 200 conjugate-paired):

| $j$ | $\sigma_j$ |
|---|---|
| 2 | $-4.20 \times 10^{-2}$ |
| 3 | $-1.11 \times 10^{-4}$ |
| 4 | $+7.36 \times 10^{-5}$ |
| 5 | $+7.15 \times 10^{-7}$ |

검증 표 — $\lambda_n$ 두 방식 계산:

| $n$ | $\lambda_n$ (direct) | $\lambda_n$ via Eq. (2.18) | diff |
|---|---|---|---|
| 3 | 0.189091 | 0.189091 | 0 |
| 5 | 0.524022 | 0.524022 | 0 |
| 10 | 2.073258 | 2.073258 | 0 |
| 20 | 7.944988 | 7.944988 | 0 |

**Diff exactly zero** within `mpmath` precision (40 decimal digits). *Lagarias Eq. (2.18) numerical confirmation*, 새 결과 아님.

## 3. Mertens function $M(x)$ — RH-equivalent statement

**Setup**: Mertens function:
$$M(x) := \sum_{n \leq x} \mu(n)$$
$\mu$ = Möbius function. 두 관련 statement:

- **Mertens conjecture** (1897): $|M(x)|/\sqrt{x} \leq 1$ for all $x \geq 1$. Odlyzko–te Riele (1985)이 **반증**, violations 매우 큰 $x$에서.
- **RH-equivalent**: $M(x) = O(x^{1/2+\varepsilon})$ for all $\varepsilon > 0$. Mertens보다 *약함*, RH와 *동치*.

**프로젝트 numerical** (small $x$, Möbius direct sum, `mpmath`):

| $x$ | $M(x)$ | $\|M(x)\|/\sqrt{x}$ |
|---|---|---|
| 500 | $-6$ | 0.268 |
| 1000 | $+2$ | 0.063 |
| 3500 | $+12$ | 0.203 |
| 7000 | $-25$ | 0.299 |
| 8500 | $+29$ | 0.314 |
| 10000 | $-23$ | 0.230 |
| 20000 | $+26$ | 0.184 |
| 50000 | $+23$ | 0.103 |

본 range 최대 $|M(x)|/\sqrt{x}$: **0.32**.

**관찰**:
1. Small-$x$ window ($x \leq 50000$)에서 $|M(x)|/\sqrt{x} < 0.4$ — (이미 반증된) Mertens와 RH-equivalent 모두와 consistent.
2. Odlyzko–te Riele 1985의 disproof 증명: $|M|/\sqrt{x} \leq 1$ 첫 violation은 *매우 큰* $x$에서, 본 window 외부. Small-$x$ data가 못 보는 게 정상.
3. $M(x) = O(x^{1/2+\varepsilon})$ 검증은 본 data scale 외 asymptotic analysis 필요 — 시도 X.

프로젝트 기여: **0** novel content. `mertens.py`이 textbook fact (Möbius sum 수렴 pattern) 재현 sanity-check.

## 4. Wigner surmise — GUE pair-correlation of unfolded $\zeta$-zeros

**Setup (Montgomery 1973 conjecture; Odlyzko numerical confirmation)**

Unfolded 비자명 $\zeta$-zeros (local mean spacing 1로 rescale)의 *nearest-neighbor spacing distribution* $P(s)$가 asymptotic하게 Gaussian Unitary Ensemble (GUE) Wigner surmise와 일치 conjecture:

$$P_{\mathrm{GUE}}(s) = \frac{32}{\pi^2} s^2 \exp\!\left(-\frac{4 s^2}{\pi}\right)$$

**프로젝트 KS test**:

| Sample | $D_n$ (KS statistic) | $p$-value | Verdict |
|---|---|---|---|
| $N = 300$ zeros (attempt 004) | 0.043 | 0.272 | **PASS** (GUE reject 안 함) |
| $N = 500$ zeros (attempt 048) | 0.0563 | 0.0812 | **MARGINAL** |

**관찰**:
1. 더 큰 $N$ → KS test sharper, 작은 deviation도 detect. $p = 0.27$ → $p = 0.08$ 감소는 GUE conjecture가 *틀렸다는 evidence 아님* — finite empirical histogram을 asymptotic distribution과 비교 시 expected behavior.
2. SOTA (Odlyzko, billions of zeros)는 우수한 quantitative GUE agreement. 본 500-zero scale은 claim/refute 불가.
3. 프로젝트 기여: **0** novel content. `pair_correlation.py` + `spacing_distribution.py` 기본 기능 실행.

## 5. Hilbert–Pólya hypothetical operator — formal statement

**Setup (Hilbert, Pólya ~1914 — informal letters; widely attributed)**

추측 form: $H = H^\dagger$ self-adjoint operator on some concrete Hilbert space, 다음 성질:
$$\mathrm{Sp}(H) = \{\gamma_n : n \geq 1\}$$
$\{\gamma_n\}$ = 비자명 $\zeta$-zeros imaginary parts. 그렇다면 spectral theorem이 $\gamma_n \in \mathbb{R}$ 함의, 따라서 RH.

**프로젝트 역할**: $H$ search 아님. 11 paper-direct candidates (BBM 2017, Sierra 2007/2016, Connes-Consani 2021, etc.)를 *strict* Hilbert-Pólya criterion (axiom 6 strict: single $H$, no fine-tune, all zeros)에 대해 test. 11 모두 fail. Audit table + per-candidate paper-direct anchors는 [Lemma 9](../12-lemma-axiom6-ceiling/) + [Finding 1](../02-finding-axiom6-ceiling/) 참조.

Lagarias §8 (1) hypothetical operator는 self-adjointness와 technically incompatible:
$$\lambda = s^2 - \tfrac{1}{4}, \quad s = \tfrac{1}{2} + i\gamma \implies \lambda = -\gamma^2 + i\gamma$$
**복소수**. 자기수반 operator의 spectrum은 real 의무이므로, eigenvalue formula $\lambda = s^2 - 1/4$는 self-adjoint operator에 적용 불가 — paper §8 (1)이 *hypothetical*로 frame하는 이유.

## *아닌* 것

- 어떤 RH-equivalent statement의 **증명 X**. 각 섹션은 published asymptotic/formula의 numerical *verification*, derivation 아님.
- **Novel mathematical content X**. 위 모든 수식은 published paper 출처 (Voros 2006, Lagarias 2002, Montgomery 1973 등).
- **Large-scale X**. 500-zero / 50000-Mertens scale은 SOTA (Platt-Trudgian $3 \times 10^{12}$ zeros, Odlyzko billions)보다 many orders 아래.

프로젝트 기여 = paper-direct **bookkeeping** — `mpmath` 도구가 published 수식 재현 확인 + truncation effect로 valid range 제한 명시.

## Cross-references

- 11 spectral candidates audit (Hilbert-Pólya criterion): [Lemma 9](../12-lemma-axiom6-ceiling/)
- 4 papers audit (Wall #2 $\int E\,dt$ bound): [Lemma 10](../13-lemma-wall2-axiom-alpha/)
- Spectral candidate critical-reading template (BBM derivation 포함): [Lemma 1](../14-lemma-spectral-circularity-check/)
- Connes–Consani 2018→2021 progress (path 1): [Finding 3](../04-finding-connes-consani-progress/)

---

[← 한국어 포스트 전체](../../) · [English](../../../en/posts/17-numerical-evidence/)
