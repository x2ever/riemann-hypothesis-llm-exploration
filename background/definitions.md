# Definitions — 기본 객체와 관습

> 출처: Riemann 1859 (Wilkins 영역), Bombieri Clay, Conrey 2003 Notices. 본 프로젝트의 기호·관습은 본 파일을 표준으로 함.

## 1. Riemann zeta function ζ(s)

복소 변수 s = σ + it (σ, t ∈ ℝ).

### 1.1 Dirichlet 급수 (Re(s) > 1)
$$
\zeta(s) := \sum_{n=1}^\infty \frac{1}{n^s}
$$
절대수렴 영역: σ > 1.

### 1.2 Euler product (Re(s) > 1)
$$
\zeta(s) = \prod_{p \text{ prime}} \left(1 - p^{-s}\right)^{-1}
$$
Euler 1737. 산술 기본정리 (유일 인수분해) 의 해석적 표현.

### 1.3 해석적 연속
ζ(s) 는 ℂ 전체로 *meromorphic* 으로 연속되며 단 하나의 단순 극점 s = 1 (residue 1).

Riemann 의 연속 도구: 적분 표현
$$
\Gamma(s)\zeta(s) = \int_0^\infty \frac{x^{s-1}}{e^x - 1}\,dx \quad (\Re s > 1)
$$
+ Hankel contour 변형. (Riemann 1859 참조; 본 프로젝트에서는 Π(s-1) = Γ(s) 기호로 구식·신식 통일.)

### 1.4 함수방정식 (대칭형)
$$
\pi^{-s/2}\,\Gamma\!\left(\frac{s}{2}\right)\zeta(s) = \pi^{-(1-s)/2}\,\Gamma\!\left(\frac{1-s}{2}\right)\zeta(1-s)
$$
또는 동치로
$$
\zeta(s) = 2^s \pi^{s-1}\,\sin\!\frac{\pi s}{2}\,\Gamma(1-s)\,\zeta(1-s).
$$
(상세 유도: `functional_equation.md`)

## 2. ξ(s) 와 Ξ(t)

### 2.1 ξ(s) — Bombieri Clay 정의
$$
\xi(s) := \tfrac{1}{2}\, s(s-1)\, \pi^{-s/2}\, \Gamma\!\left(\frac{s}{2}\right)\, \zeta(s)
$$
- ξ(s) 는 *entire* (전해석).
- ξ(s) = ξ(1-s).
- 영점: 정확히 ζ(s) 의 비자명 영점 (자명 영점은 Γ 인자가 상쇄, s=1 의 극점은 (s-1) 인자가 상쇄, s=0 는 s 인자).

### 2.2 Ξ(t) (Riemann 의 변수 변환)
s = ½ + it 대입:
$$
\Xi(t) := \xi\!\left(\tfrac{1}{2} + it\right)
$$
- Ξ(t) 는 *real* for *real* t (functional equation 으로 유도됨).
- Ξ(t) 는 *even*: Ξ(t) = Ξ(-t).
- **Riemann 가설 (Ξ 형식)**: Ξ(t) 의 모든 영점 t 가 *실수*.

> **사고 과정 추정**: Riemann 이 ξ 와 Ξ 를 도입한 이유는 함수방정식 대칭축이 σ = 1/2 임을 *변수 변환으로 명시적으로 만든 것*. Ξ(t) 가 실/짝함수 라는 사실이 Hilbert–Pólya 직관 (실수 스펙트럼) 의 출발점이다.

## 3. 영점 분류

### 3.1 자명 영점 (Trivial zeros)
$$
\zeta(-2) = \zeta(-4) = \zeta(-6) = \cdots = 0
$$
함수방정식의 sin(πs/2) 인자에서 옴. RH 와 무관.

### 3.2 비자명 영점 (Nontrivial zeros)
*임계 띠* (critical strip) 0 < σ < 1 안에 위치. 무한 개. 통상 표기:
$$
\rho = \beta + i\gamma, \qquad 0 < \beta < 1.
$$
함수방정식 + 켤레 대칭 + Hadamard 제약으로 영점은 *4쌍* 패턴: ρ, 1-ρ, ρ̄, 1-ρ̄.

### 3.3 임계선 (Critical line)
$$
\Re(s) = \tfrac{1}{2}.
$$
**Riemann Hypothesis (RH)**: 모든 비자명 영점이 임계선 위에 있다 (β = 1/2).

## 4. 영점 카운팅 N(T)

$$
N(T) := \#\{\rho = \beta + i\gamma : \zeta(\rho) = 0,\ 0 < \beta < 1,\ 0 < \gamma \le T\}
$$
**Riemann–von Mangoldt formula**:
$$
N(T) = \frac{T}{2\pi}\log\frac{T}{2\pi} - \frac{T}{2\pi} + \frac{7}{8} + S(T) + O(1/T)
$$
- $S(T) := \pi^{-1}\arg\zeta(\tfrac{1}{2} + iT)$ (특정 경로 인자, $S(T) = O(\log T)$)
- 평균 영점 간격 (높이 $T$ 근처) ≈ $2\pi / \log T$.

$N_0(T) :=$ 임계선 위 영점 수. **RH ⟺ $N_0(T) = N(T)$ for all T**.

## 5. von Mangoldt 함수와 ψ(x)

### 5.1 von Mangoldt 함수
$$
\Lambda(n) := \begin{cases} \log p & n = p^k,\ p\text{ prime},\ k \ge 1 \\ 0 & \text{otherwise} \end{cases}
$$

### 5.2 Chebyshev ψ(x)
$$
\psi(x) := \sum_{n \le x} \Lambda(n)
$$

### 5.3 Explicit formula (Riemann–von Mangoldt)
$$
\psi(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \log 2\pi - \tfrac{1}{2}\log(1 - x^{-2})
$$
유효: $x > 1$, $x$ ≠ 소수 거듭제곱. ρ 합은 비자명 영점 (대칭 한정합).

> **본질적 메시지**: 소수 분포는 ζ 의 영점 *직접* 으로 결정된다. 영점이 임계선 위 (Re ρ = 1/2) 면 $|x^\rho/\rho| = O(\sqrt x / |\rho|)$ 이고 ψ(x) - x 의 오차가 $O(\sqrt x \log^2 x)$ 로 sharp.

## 6. Möbius 함수와 M(x)

### 6.1 Möbius 함수
$$
\mu(n) := \begin{cases} 1 & n=1 \\ (-1)^k & n = p_1\cdots p_k\ (\text{distinct primes}) \\ 0 & \exists p,\ p^2 \mid n \end{cases}
$$

### 6.2 Mertens 함수
$$
M(x) := \sum_{n \le x} \mu(n)
$$

### 6.3 RH 동치 (Conrey 2003)
$$
\text{RH} \Longleftrightarrow M(x) = O(x^{1/2+\varepsilon}) \text{ for all } \varepsilon > 0
$$
주의: *Mertens 추측* $|M(x)| \le \sqrt x$ 는 1985 Odlyzko–te Riele 가 반증. 그러나 $O(x^{1/2+\varepsilon})$ (RH 동치) 는 여전히 미해결.

수치: `tools/mertens.py`.

## 7. Riemann–Siegel formula (계산용)

$$
Z(t) := e^{i\theta(t)}\zeta(\tfrac{1}{2}+it), \quad \theta(t) := \arg\Gamma\!\left(\tfrac{1}{4} + \tfrac{it}{2}\right) - \tfrac{t}{2}\log\pi
$$
Z(t) 는 *real* — Hardy 함수. Z(t) 의 부호 변화로 영점 검출. Riemann–Siegel 의 점근 전개로 빠른 계산 가능 ($t^{1/2}$ 시간).

## 8. L-functions (일반화)

### 8.1 Dirichlet L-function
χ: Dirichlet character mod q (primitive). $L(s, \chi) := \sum \chi(n)/n^s$.
- Euler product, 함수방정식, RH 의 일반화 (GRH: Generalized Riemann Hypothesis).

### 8.2 Hasse–Weil L (타원곡선)
$E: y^2 = x^3 + Ax + B$. $L_E(s) := \sum a(n)/n^s$, $a_p = p - N_p$.
- 모듈러성 (Wiles et al.) 으로 함수방정식 보장.
- BSD 추측 등.

### 8.3 일반 global L-function
$L$-functions := Dirichlet 급수 + Euler product + 함수방정식 + 적당한 성장 조건. **GRH** = 모든 *적절한* L-function 의 비자명 영점이 임계선 위.

> Bombieri Clay: "RH 의 진짜 본질은 단일 ζ 가 아니라 *L-functions 가족 전체*에서 보아야 가능 — Langlands 프로그램과 연결."

## 9. 본 프로젝트 표기 규약

- 복소 변수: s = σ + it, σ = Re(s), t = Im(s).
- 비자명 영점: ρ = β + iγ.
- $\sum_\rho$ 는 conjugate-paired 대칭합 (Cauchy 의미의 한정합).
- 정밀도 표기: `[numerical, dps=N, k zeros]` 메타.
- 모든 새 객체는 본 파일에 추가 — *앞으로의 시도는 본 파일의 정의를 기준*.
