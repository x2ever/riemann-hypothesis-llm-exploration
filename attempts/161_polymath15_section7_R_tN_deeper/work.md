# Work — Attempt 161 (Polymath15 §6.3 *A+B-C approximation* DEEP)

## Cut self-check
Cut 6: paper-direct deeper. cut X.

## Polymath15 §6.3 paper-direct (paper page 26-32)

attempt 106 (§4-§6.1 deep) follow-up.

### eq (61): ε bound
$$\varepsilon \le \frac{10}{3(T-6)} \exp\left(\frac{10}{3(T-6)}\right)$$

### δ decomposition (paper §6.2 eq 64)
$$\delta = \delta_1 + \delta_2 + \delta_3$$

paper-direct δ_1, δ_2, δ_3 final bounds (paper page 28-29):
$$\delta_1 \le \frac{0.366 \times 9^\sigma}{a - 0.865} \exp\left(\frac{3.49}{T-4}\right)$$
$$\delta_2 \le \frac{0.031 \times 2^{-\sigma}}{a - 0.353} \exp\left(\frac{3.49}{T-4}\right)$$
$$\delta_3 \le \frac{2 \times 10^{-30}}{a^{14}} \quad \text{(extremely small)}$$

→ paper-direct *engineering constants*: 0.366, 0.031, 0.865, 0.353, 3.49, 10^{-30}/a^{14}.

### Corollary 6.4 — *A + B - C approximation* (paper-direct)

paper-direct quote (paper §6.3):
$$H_t(x+iy) = A_{t,N}(x+iy) + B_{t,N}(x+iy) - C_t(x+iy) + O_\le(E_A + E_B + E_C)$$

A, B, C definitions (paper-direct):
- $A_{t,N}(x+iy) := M_t(s_-) \sum_{n=1}^N \frac{b_n^t}{n^{s_- + (t/2)\alpha(s_-)}}$
- $B_{t,N}(x+iy) := M_t(s_+) \sum_{n=1}^N \frac{b_n^t}{n^{s_+ + (t/2)\alpha(s_+)}}$
- $C_t(x+iy) := 2 e^{-\pi i y/8} (-1)^N \exp(t\pi^2/64) \Re(M_0(iT') C_0(p) U e^{\pi i/8})$

s_+, s_- (paper-direct):
- $s_+ = (1+y-ix)/2$
- $s_- = (1-y+ix)/2$

### Proposition 6.6 (paper-direct Estimates)

(i) |γ| ≤ exp(0.02 y) (x/(4π))^{-y/2}.
(ii) Re s_+ ≥ (1+y)/2 + (t/4) log(x/(4π)) - ((1-3y + 8y(1-y)/x²)_+ t)/(2x²).
(iii) κ = O_≤(ty/(2(x-6))).

(iv-vi) e_A, e_B, e_C explicit bounds (paper §6.3 eq 71-74).

## Wall #2 paper-direct strengthening

paper §6.3 *all engineering constants* (0.366, 0.031, 0.865, 0.353, 0.626, 0.02, 3.49, 8.52, 12) explicit 명시:
- 모두 *Lemma 5.1 (Stirling, Boyd 1994) + saddle-point method* derived.
- *combinatorial 최적화 한계*.
- Tao quote (attempt 113 paper-direct §1.5): "far from optimal".

→ paper-direct: Wall #2 의 *combinatorial 최적화 fundamental limit* paper-direct verification.

## *Wall #2 quantitative* paper-direct count

paper §6.3 alone: **8 explicit constants** (0.366, 0.031, 0.865, 0.353, 0.02, 3.49, 8.52, 12).
paper §6.1, 6.2 (attempt 106): 추가 4 (3.33, 3.08, 3.49, 0.626).
- 총 **12 paper-direct engineering constants** in Polymath15 §6.

→ Wall #2 paper-direct: *combinatorial 최적화* 12 explicit constants — Tao "far from optimal" quote.

## Lemma 적용

### Lemma 3 evidence (8) Polymath15 강화
- attempt 106 + 161 결합.
- *engineering constants* 12 explicit.
- *Newman positivity Λ ≥ 0* Rodgers-Tao backward complementary (attempt 113 + 132).

### Lemma 7 Anchoring
- paper §6.3 Corollary 6.4 + 6.5 + Proposition 6.6 paper-direct.

## Honest scope
*novel content X*. Polymath15 §6.3 paper-direct deep + 12 engineering constants + Wall #2 *combinatorial 최적화 fundamental limit* paper-direct verification.
