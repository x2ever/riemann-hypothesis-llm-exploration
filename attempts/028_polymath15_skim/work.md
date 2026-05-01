# Work — Attempt 028 (Polymath 15)

## §1 정독 정리

### Theorem 1.1
$\Lambda \le 0.22$ unconditionally.

### Theorem 1.2 (Upper bound criterion)
Suppose $t_0, X > 0$, $0 < y_0 \le 1$ obey:
- (i) **Numerical RH**: no zeros of $\zeta(\sigma + iT)$ with $\frac{1+y_0}{2} \le \sigma \le 1$, $0 \le T \le X/2$.
- (ii) **Asymptotic zero-free region at t_0**: no zeros of $H_{t_0}(x+iy) = 0$ with $x \ge X + \sqrt{1-y_0^2}$, $y_0 \le y \le \sqrt{1-2t_0}$.
- (iii) **Barrier at intermediate times**: no zeros of $H_t(x+iy) = 0$ with $X \le x \le X + \sqrt{1-y_0^2}$, $\sqrt{y_0^2 + 2(t_0-t)} \le y \le \sqrt{1-2t}$, $0 \le t \le t_0$.

Then $\Lambda \le t_0 + \frac{1}{2}y_0^2$.

### 적용 (paper §1)
$t_0 = 0.2$, $X = 6 \cdot 10^{10} + 83952 - 0.5$, $y_0 = 0.2$ → Λ ≤ 0.22.

### Theorem 1.3 (Effective Riemann-Siegel)
$H_t(x+iy)/B_t(x+iy) = f_t(x+iy) + O_\le(e_A + e_B + e_{C,0})$ where $f_t, B_t$ explicit, error terms computable.

## Wall #2 Sharper Formulation (paper-direct)

[rigorous, paper §1 직접]:

Wall #2 (FORWARD-TIME) 의 *진짜 정체*:
- *Unconditional* ∫E dt bound 부재 — 본 프로젝트 attempt 006 의 sharper.
- *Conditional* sharpening 가능 — Polymath 의 (i)+(ii)+(iii) 3-tool combination.
- (i) = numerical (specialist HPC), (ii) = analytical asymptotic, (iii) = barrier (hybrid).
- *Conditional* Λ ≤ 0.22 가 *unconditional* Λ ≤ 0 (=RH) 와 큰 갭 — 0.22 의 push 가 sharp 한계.

→ Wall #2 의 *현재 최선*:
- 3-tool combination 강화 — X 를 더 키우거나 (i) push.
- 본 프로젝트 한정 *novel content* X — Polymath specialist 영역.

## 본 시도의 honest 결과

- attempt 006 의 sharper formulation 이 *paper-direct evidence* 로 강화.
- Wall #2 우회는 *(i)+(ii)+(iii)* 의 sharp limit 까지가 전부 — 본질적 unconditional 갭 살아있음.
- *novel content X*. 외부 critique 와 일관.

## "예상 가능 결과" self-check
*yes*. Polymath 결과는 알려진 bound. 우리 wall taxonomy 와 mapping 이 가치.
