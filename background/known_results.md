# Known Results — RH 관련 알려진 정리·동치·부분 결과

> 출처: Bombieri Clay, Conrey 2003 Notices, Rodgers–Tao 2020, Platt–Trudgian 2021. 무엇이 *증명되었고* 무엇이 *추측인지* 명확히 분리. 시도 진행 시 본 파일을 *baseline*. 새 시도는 여기에 적힌 결과를 *재증명할 필요 없이 사용*.

## A. 증명된 결과 (rigorous, 인용 가능)

### A1. 해석적 연속 + 함수방정식 (Riemann 1859)
- ζ(s) 는 ℂ 전체로 meromorphic, s=1 에서만 단순 극점.
- 함수방정식: $\Lambda(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s) = \Lambda(1-s)$.

### A2. 비자명 영점은 임계 띠 안 (Riemann 1859)
- $0 < \Re(\rho) < 1$ for all nontrivial ρ.

### A3. 무영점 영역 + 소수 정리 (Hadamard, de la Vallée Poussin 1896)
- $\zeta(1+it) \neq 0$ for $t \in \mathbb R$.
- $\Rightarrow$ Prime Number Theorem: $\pi(x) \sim x/\log x$ (i.e., $\psi(x) \sim x$).

### A4. Vinogradov–Korobov 무영점 영역 (1958)
- $\zeta(\sigma + it) \neq 0$ for $\sigma \ge 1 - c/(\log|t|)^{2/3}(\log\log|t|)^{1/3}$, |t| ≥ 3.
- ⇒ Prime Number Theorem with error $\pi(x) - \mathrm{Li}(x) = O(x \exp(-c'(\log x)^{3/5}/(\log\log x)^{1/5}))$.
- RH 가정 시 error 가 $O(\sqrt{x}\log x)$ — 현재 알려진 무조건 결과보다 훨씬 강함.

### A5. Hardy 1914 — 임계선 위 무한 영점
- ξ(½ + it) = 0 의 실수해 t 가 무한히 많다.
- 도구: ξ(½ + it) 의 부호 변화 + Mellin transform 기법.

### A6. Hardy–Littlewood — density on critical line
- 적당한 비율의 영점이 임계선 *근처*. 그 후 정량 강화 시리즈.

### A7. Selberg 1942 — positive proportion
- 임계선 위 영점 비율 > 0 (positive proportion). 첫 *정성적* 양적 결과.

### A8. Levinson 1974 — 1/3
- $\liminf_{T \to \infty} \frac{N_0(T)}{N(T)} \ge 1/3$.
- 도구: ξ′ 영점이 ξ 영점에 가까이 있다 (Rolle 류) + mollifier.

### A9. Conrey 1989 — > 40% (정확히 0.40219...)
- Levinson 방법 + 더 긴 mollifier (Dirichlet polynomial) + 변분 최적화.

### A10. Bui–Conrey–Young 2011 — > 41.05%
- mollifier 더 정교화. 현재 무조건 best.

### A11. Ingham 1940 (density theorem)
- $N(\alpha, T) := \#\{\rho : \beta \ge \alpha,\ |\gamma| \le T\}$.
- $N(\alpha, T) = O(T^{3(1-\alpha)/(2-\alpha) + \varepsilon})$ for $\frac{1}{2} \le \alpha \le \frac{3}{4}$.
- 임계선에서 멀어질수록 영점 *희소함*을 증명 (RH 까지 가지 않은 결과).

### A12. Deligne 1974 — function field RH (Weil conjectures)
- 함수체 위의 ζ-function ζ(C, s) 에 대해 RH 가 *증명됨* (Weil 1948 곡선의 경우, Deligne 1974 일반).
- 도구: étale cohomology + Lefschetz fixed point + algebraic index theorem.
- *RH 본인을 증명하지 않음* — 다만 비교 대상.

### A13. Platt–Trudgian 2021 — 영점 검증 SOTA
- 첫 $3 \cdot 10^{12}$ 개의 ζ 영점이 모두 임계선 위 (간단·다중성 1).
- 알고리즘: Riemann–Siegel + interval arithmetic.
- 이전 best (Gourdon 2004) 기준 약 3배.

### A14. Rodgers–Tao 2020 — Λ ≥ 0 (de Bruijn–Newman)
- de Bruijn–Newman 상수 Λ ≥ 0 (Newman 1976 의 *추측*을 증명).
- RH ⟺ Λ ≤ 0. 따라서 RH ⟺ Λ = 0. 현재 알려진 것: $0 \le \Lambda$ + numeric upper bounds 점근적으로 0 으로.

### A15. 동치 형태들 (각각 RH 와 *증명된 동치*)

#### A15.1 π(x) error
$$
\text{RH} \iff \pi(x) = \mathrm{Li}(x) + O(\sqrt x \log x).
$$

#### A15.2 ψ(x) error
$$
\text{RH} \iff \psi(x) = x + O(\sqrt x \log^2 x).
$$

#### A15.3 Mertens-type
$$
\text{RH} \iff M(x) = O(x^{1/2 + \varepsilon}) \text{ for all } \varepsilon > 0.
$$
(Mertens 추측 $|M(x)| \le \sqrt x$ 는 1985 Odlyzko–te Riele 가 *반증* — 더 약한 동치는 여전히 살아있음.)

#### A15.4 Li's criterion (Li 1997)
$$
\text{RH} \iff \lambda_n \ge 0 \text{ for all } n \ge 1
$$
where $\lambda_n = \sum_\rho [1 - (1-1/\rho)^n]$.

#### A15.5 Nyman–Beurling
$$
\text{RH} \iff \overline{\mathrm{span}}_{L^2(0,1)}\{\eta_\alpha : 0 < \alpha < 1\} = L^2(0,1)
$$
where $\eta_\alpha(t) = \{\alpha/t\} - \alpha\{1/t\}$. (Baez-Duarte: $\alpha = 1/n$ 정수해도 OK.)

#### A15.6 Weil's positivity (Weil 1952)
$$
\text{RH} \iff \sum_\gamma h(\gamma) \ge 0 \text{ for all admissible } h(r) = h_0(r)\overline{h_0(\bar r)}.
$$
- 간격 합으로 표현되는 양정치성. *function field RH 증명의 직접 유추*.

#### A15.7 Lagarias 2002
$$
\text{RH} \iff \sigma(n) \le H_n + e^{H_n}\log H_n \quad \forall n,
$$
where $H_n = 1 + 1/2 + \cdots + 1/n$. (산술적 매우 elementary 동치.)

#### A15.8 Hardy–Littlewood 1918
$$
\text{RH} \iff \sum_{k=1}^\infty \frac{(-x)^k}{k!\,\zeta(2k+1)} = O(x^{-1/4}) \text{ as } x \to \infty.
$$

## B. 추측 (RH 와 같은 strength 또는 강함, 미해결)

### B1. RH 자체
$\Re(\rho) = 1/2$ for all nontrivial ρ.

### B2. GRH (Generalized RH)
모든 *primitive* Dirichlet L-function (일반화: 모든 Selberg-class L-function) 의 비자명 영점이 임계선 위.

### B3. Lindelöf hypothesis
$$
\zeta(\tfrac{1}{2} + it) = O(|t|^\varepsilon) \text{ for every } \varepsilon > 0.
$$
- RH ⇒ Lindelöf (proven). 역방향 *미해결* — Lindelöf 가 더 약함.
- 현재 best 무조건 bound: $\zeta(\frac{1}{2} + it) = O(t^{1/6 + \varepsilon})$ (Bourgain 2017).
- "convexity bound" $t^{1/4 + \varepsilon}$ 보다 좋아진 정도.

### B4. Montgomery's pair correlation conjecture (1973)
$$
\sum_{\frac{2\pi\alpha}{\log T} < \gamma - \gamma' \le \frac{2\pi\beta}{\log T}} 1 \sim N(T)\int_\alpha^\beta \left(1 - \left(\frac{\sin\pi u}{\pi u}\right)^2\right)du
$$
RMT (Gaussian Unitary Ensemble) pair correlation 과 *동일* — Dyson 의 식별.

### B5. GUE conjecture (Montgomery–Odlyzko)
영점의 *모든* local statistics 가 GUE 대칭 (large random unitary matrices).

### B6. Keating–Snaith conjecture (2000)
$$
I_k(T) := \frac{1}{T}\int_0^T |\zeta(\tfrac{1}{2} + it)|^{2k}\,dt
$$
$I_k(T) \sim g_k a_k (\log T)^{k^2}$ where $g_k = k!^2 \prod_{j=0}^{k-1} \frac{j!}{(j+k)!}$, $a_k$ arithmetic factor.
- $g_1=1$ (Hardy–Littlewood), $g_2=2$ (Ingham), $g_3=42$ (Conrey–Ghosh), $g_4 = 24024$ (Conrey–Gonek + Keating–Snaith 일치).

### B7. Katz–Sarnak symmetry
L-functions 의 가족이 (orthogonal / unitary / symplectic) 한 *symmetry type* 으로 분류, 영점 분포가 그 타입의 RMT 와 일치.

### B8. Riemann's simplicity conjecture
모든 비자명 영점이 *simple* (다중도 1). $S(T) = O(\log T)$ 와 함께 결합되어 알려진 영점 모두 simple, but ∀ 미해결.

### B9. de Bruijn–Newman = 0
Λ = 0 (RH 와 동치). 현재 $0 \le \Lambda$ + 작은 upper bound (Λ < 0.2 같은 류 — 시간 따라 개선).

## C. 알려진 *반례* / 잘못된 시도 (배움)

### C1. Mertens 추측 (반증)
$|M(x)| \le \sqrt x$ — Odlyzko–te Riele 1985 가 반증. 정확한 첫 반례 x 는 미상이나 $x < 10^{40}$ 에서 존재 보장.
- **교훈**: "RH 보다 강해 보이는 elementary statement" 가 거짓일 수 있다. 본인 시도가 너무 강하면 의심.

### C2. Rademacher 사건
RH disprove 시도. 결함 발견 (Siegel 이 검증). Time 지가 기사화하려다 철회.
- **교훈**: RH 의 거짓을 주장하는 시도도 검증 의무.

### C3. Atiyah 2018
*proof* 주장 → 즉시 결함 지적. preprint 만 존재.
- **교훈**: famous mathematician 도 RH 시도에서 실수 가능. 비판적 검토 필수.

### C4. de Branges
긴 시리즈의 시도. 지속적으로 결함 지적.
- **교훈**: long-running personal program 도 외부 검증 없이는 신뢰 불가.

## D. 수치 검증 한계

### D1. 영점 검증 (height ≤ T)
- van de Lune et al. (1986): $T \approx 5 \cdot 10^8$ → 첫 1.5 billion 영점.
- Odlyzko (계속): $10^{20}, 10^{21}, 10^{22}$ 근방 millions of 영점.
- Platt–Trudgian (2021): 첫 $3 \cdot 10^{12}$ 영점 모두 임계선 위 *rigorously verified*.

### D2. 직접적 함의
- 만약 RH 가 거짓이면 *임계선에서 벗어난* 첫 영점의 imaginary part 는 *최소* 영점 검증 한계 이상.
- 즉 *반례 후보의 lower bound* — 현재 약 $T \approx 3 \cdot 10^{12}$.

## E. RH 의 결과들 (RH true 일 때 따라오는 것들)

### E1. PNT 강화
- $\pi(x) = \mathrm{Li}(x) + O(\sqrt x \log x)$.
- $p_{n+1} - p_n = O(\sqrt{p_n} \log p_n)$ — 소수 간격 sharp bound.

### E2. 산술 함수 estimates
- $\sigma(n) = O(n \log\log n)$ (Robin's 부등식과 관련).
- divisor 합, twin prime 정량 추측 등에 영향.

### E3. Dirichlet 가족 + Chebotarev 효과
- L(s, χ) 들 영점이 1/2 위 → 등차수열 안 소수 분포 sharp.
- Chebotarev density 정리의 effective 형태 (Hooley 등).

### E4. Miller's 원시성 검정 (deterministic)
- GRH 가정 시 polynomial-time 결정적 prime test (Miller 1976).
- (무조건 polynomial: AKS 2002.)

## F. 본 프로젝트에서 사용 가능한 lever

각 시도는 다음을 *re-prove 없이 사용 가능* (단 출처 명시 의무):

- A1–A14: 모든 증명된 결과
- A15: 동치 형태 (특히 A15.3 Mertens, A15.4 Li, A15.5 Nyman–Beurling, A15.6 Weil — strategic 접근의 출발점이 될 수 있음)
- E: RH true 가정 시 결론 — 본인 시도가 이런 결과들과 *consistent* 한지 sanity check 가능

추측 (B) 들은 *가정* 으로 사용 가능하나 strategy.md 에 명시 의무.
