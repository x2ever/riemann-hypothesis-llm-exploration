---
title: "Numerical evidence — paper-direct formulas, mpmath data tables"
parent: Numerical evidence
grand_parent: English
nav_order: 17
date: 2026-05-02
---

# Numerical evidence — paper-direct formulas, mpmath data tables

[← All English posts](../../) · [한국어](../../../ko/posts/17-numerical-evidence/) · *2026-05-02*

> Concrete numerical sanity-checks the project ran against published formulas. None of these is a new theorem; they are *empirical confirmations* of established RH-equivalent statements. All computations were performed with `mpmath` at high precision (dps = 30 to 50).
>
> **Why this post**: a reader asked, *"where are the actual equations and the mathematical derivations?"* — and they were right. The project's `attempts/` log contains substantial numerical work using paper-direct formulas, but the blog had not surfaced it. This post collects the most relevant data tables inline.

## 1. Voros 2006 tempered asymptotic — Li coefficients $\lambda_n$

**Setup (Voros, "Sharpenings of Li's criterion for the Riemann hypothesis", 2006)**

The Li coefficients are defined by:
$$\lambda_n = \sum_{\rho} \left(1 - \left(1 - \tfrac{1}{\rho}\right)^n\right)$$
summed over non-trivial $\zeta$-zeros $\rho = 1/2 + i\gamma$ (with multiplicity, conjugate-paired). Li's criterion (1997):

$$\mathrm{RH} \iff \lambda_n \geq 0 \text{ for all } n \geq 1.$$

**Voros 2006 sharp dichotomy (paper §1, Theorem)**:

- *RH true* (tempered case): $\lambda_n \sim \frac{n}{2}\left(\log n - 1 + \gamma - \log 2\pi\right) + o(n)$
- *RH false*: $\lambda_n \sim \sum_{|z_k|<1} z_k^{-n} + \overline{z_k}^{-n}\ \mathrm{mod}\ o(e^{\varepsilon n})$ where $z_k = (\tau_k - i/2)/(\tau_k + i/2)$ for off-line zeros — *exponentially growing oscillations*.

The two are mutually exclusive in the large-$n$ limit.

**Project's numerical run** (`mpmath`, dps=50, 500 zeros, $C_1 = (\gamma - 1 - \log 2\pi)/2 \approx -1.130$):

| $n$ | $\lambda_n^{(500)}$ (partial sum) | Voros prediction | ratio | sign |
|---|---|---|---|---|
| 10 | 2.16 | 0.21 | 10.33 | + (sub-asymptotic) |
| 50 | 40.66 | 41.28 | **0.985** | + (sweet spot) |
| 100 | 107.12 | 117.23 | **0.914** | + (good agreement) |
| 200 | 260.77 | 303.77 | 0.859 | + |
| 500 | 707.36 | 988.49 | 0.716 | + (truncation begins) |
| 1000 | 1218.90 | 2323.55 | 0.525 | + |
| 2000 | 1367.54 | 5340.24 | 0.256 | + (truncation dominant) |

**Observations** (paper-direct, no new claim):
1. **Sweet spot $n \approx 50$**: ratio $\approx 1.0$ — quantitative agreement with Voros tempered prediction.
2. **All $n$ have $\mathrm{sign}(\lambda_n) = +$** in our sample. The Voros *RH-false* case (exponential oscillations) is *not observed* in the data — consistent with RH being true in the verified region.
3. **Truncation effect**: $n > 200$ ratio decays because the partial-sum over 500 zeros undercounts the contribution. More zeros → larger valid $n$ range.

This is **not** RH evidence in any new sense — it is a numerical sanity-check that our `li_criterion.py` tool reproduces Voros's published asymptotic. The state-of-the-art numerical RH verification (Platt-Trudgian 2021, $H = 3 \times 10^{12}$) is many orders of magnitude beyond the project's 500-zero scale.

## 2. Lagarias 2002 — Eq. (2.18), $\lambda_n$ via power sums $\sigma_j$

**Setup (Lagarias 2002, *Acta Arith.*)**

Define the power sums of inverse $\zeta$-zeros:
$$\sigma_j := \sum_{\rho} \frac{1}{\rho(1-\rho))^j}\ \text{(roughly; see paper §2 for the exact definition with modifications)}$$

Lagarias paper §2, Eq. (2.18) connects Li coefficients to power sums:
$$\lambda_n = \sum_{j=1}^n (-1)^{j-1} \binom{n}{j} \sigma_j$$

**Project's numerical verification** (`mpmath`, dps=40, 200 zeros + 200 conjugate-paired):

| $j$ | $\sigma_j$ |
|---|---|
| 2 | $-4.20 \times 10^{-2}$ |
| 3 | $-1.11 \times 10^{-4}$ |
| 4 | $+7.36 \times 10^{-5}$ |
| 5 | $+7.15 \times 10^{-7}$ |

Now the verification table — $\lambda_n$ computed two ways:

| $n$ | $\lambda_n$ (direct) | $\lambda_n$ via Eq. (2.18) | diff |
|---|---|---|---|
| 3 | 0.189091 | 0.189091 | 0 |
| 5 | 0.524022 | 0.524022 | 0 |
| 10 | 2.073258 | 2.073258 | 0 |
| 20 | 7.944988 | 7.944988 | 0 |

**Diff is exactly zero** within `mpmath` precision (40 decimal digits). This is a *numerical confirmation of Lagarias's Eq. (2.18)*, not a new result.

## 3. Mertens function $M(x)$ — RH-equivalent statement

**Setup**: the Mertens function is
$$M(x) := \sum_{n \leq x} \mu(n)$$
where $\mu$ is the Möbius function. Two related statements:

- **Mertens conjecture** (1897): $|M(x)|/\sqrt{x} \leq 1$ for all $x \geq 1$. **Disproved** by Odlyzko–te Riele (1985), violations occur at very large $x$.
- **RH-equivalent**: $M(x) = O(x^{1/2+\varepsilon})$ for every $\varepsilon > 0$. *Weaker* than Mertens, *equivalent* to RH.

**Project's numerical run** (small $x$, Möbius direct sum, `mpmath`):

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

Maximum $|M(x)|/\sqrt{x}$ in this range: **0.32**.

**Observations**:
1. In our small-$x$ window ($x \leq 50000$), $|M(x)|/\sqrt{x} < 0.4$ — consistent with both (now-disproved) Mertens and RH-equivalent statements.
2. Odlyzko–te Riele's 1985 disproof shows the first violation of $|M|/\sqrt{x} \leq 1$ occurs at *very large* $x$, far beyond our window. This is consistent with our small-$x$ data not seeing it.
3. The verification of $M(x) = O(x^{1/2+\varepsilon})$ requires asymptotic analysis far beyond our data scale — not attempted.

Project's contribution: **0** novel content. The sample is a sanity-check of `mertens.py` against textbook fact (Möbius sum convergence pattern).

## 4. Wigner surmise — GUE pair-correlation of unfolded $\zeta$-zeros

**Setup (Montgomery 1973 conjecture; Odlyzko numerical confirmation)**

For unfolded non-trivial $\zeta$-zeros (i.e., zeros rescaled to local mean spacing 1), the *nearest-neighbor spacing distribution* $P(s)$ should match the Gaussian Unitary Ensemble (GUE) Wigner surmise asymptotically:

$$P_{\mathrm{GUE}}(s) = \frac{32}{\pi^2} s^2 \exp\!\left(-\frac{4 s^2}{\pi}\right)$$

**Project's KS test**:

| Sample | $D_n$ (KS statistic) | $p$-value | Verdict |
|---|---|---|---|
| $N = 300$ zeros (attempt 004) | 0.043 | 0.272 | **PASS** (don't reject GUE) |
| $N = 500$ zeros (attempt 048) | 0.0563 | 0.0812 | **MARGINAL** |

**Observations**:
1. Larger $N$ → KS test becomes *sharper*, smaller deviations are detected. The drop from $p = 0.27$ to $p = 0.08$ is *not* evidence the GUE conjecture is wrong; it is the expected behavior when comparing a finite empirical histogram against an asymptotic distribution.
2. The state-of-the-art (Odlyzko, billions of zeros) shows excellent quantitative GUE agreement. Our 500-zero scale is too small to claim or refute anything.
3. Project's contribution: **0** novel content. This is `pair_correlation.py` and `spacing_distribution.py` running their basic functionality.

## 5. Hilbert–Pólya hypothetical operator — formal statement

**Setup (Hilbert, Pólya, ~1914 — informal letters; widely attributed)**

The conjectural form: there exists a self-adjoint operator $H = H^\dagger$ on some concrete Hilbert space such that
$$\mathrm{Sp}(H) = \{\gamma_n : n \geq 1\}$$
where $\{\gamma_n\}$ are the imaginary parts of the non-trivial $\zeta$-zeros. If so, the spectral theorem implies $\gamma_n \in \mathbb{R}$, hence RH.

**Project's role here**: not a search for $H$. The project tested 11 paper-direct candidates (BBM 2017, Sierra 2007/2016, Connes-Consani 2021, etc.) for the *strict* version of the Hilbert-Pólya criterion (axiom 6 strict: single $H$, no fine-tune, all zeros). All 11 fail. See [Lemma 9](../12-lemma-axiom6-ceiling/) and [Finding 1](../02-finding-axiom6-ceiling/) for the audit table and per-candidate paper-direct anchors.

The Lagarias §8 (1) hypothetical operator is technically incompatible with self-adjointness:
$$\lambda = s^2 - \tfrac{1}{4}, \quad s = \tfrac{1}{2} + i\gamma \implies \lambda = -\gamma^2 + i\gamma$$
which is **complex**. A self-adjoint operator's spectrum must be real, so the eigenvalue formula $\lambda = s^2 - 1/4$ cannot apply to a self-adjoint operator — paper §8 (1) frames it as *hypothetical* for this reason.

## What this post is *not*

- **Not** a proof of any RH-equivalent statement. Each section contains numerical *verification* of a published asymptotic or formula, not a derivation.
- **Not** novel mathematical content. Every formula above is from a published paper (Voros 2006, Lagarias 2002, Montgomery 1973, etc.).
- **Not** large-scale. The project's 500-zero / 50000-Mertens scale is many orders below state-of-the-art (Platt-Trudgian's $3 \times 10^{12}$ zeros, Odlyzko's billions of zeros).

The project's contribution is paper-direct **bookkeeping** — confirming our `mpmath`-based tools reproduce published formulas, and noting where truncation effects bound the valid range.

## Cross-references

- For the lemma that audits 11 spectral candidates against the Hilbert-Pólya criterion: [Lemma 9](../12-lemma-axiom6-ceiling/)
- For the lemma that audits 4 papers against the Wall #2 ($\int E\,dt$) bound: [Lemma 10](../13-lemma-wall2-axiom-alpha/)
- For the spectral candidate critical-reading template (with explicit BBM derivation): [Lemma 1](../14-lemma-spectral-circularity-check/)
- For Connes–Consani 2018→2021 progress on Weil positivity (path 1): [Finding 3](../04-finding-connes-consani-progress/)

---

[← All English posts](../../) · [한국어](../../../ko/posts/17-numerical-evidence/)
