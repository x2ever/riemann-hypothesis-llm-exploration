# Functional Equation — ζ(s) 의 대칭과 임계선의 의미

> 출처: Riemann 1859 (Wilkins), Bombieri Clay §I. 함수방정식이 *왜* 임계선 σ = 1/2 을 자연스럽게 만드는지가 본 파일의 핵심.

## 1. Statement

대칭형:
$$
\boxed{\quad \pi^{-s/2}\,\Gamma\!\left(\tfrac{s}{2}\right)\,\zeta(s) \;=\; \pi^{-(1-s)/2}\,\Gamma\!\left(\tfrac{1-s}{2}\right)\,\zeta(1-s) \quad}
$$
좌변을 $\Lambda(s)$ 로 두면 $\Lambda(s) = \Lambda(1-s)$ — *대칭축은 s ↔ 1-s 의 고정점, 즉 s = 1/2*.

비대칭(고전) 형식:
$$
\zeta(s) = 2^s \pi^{s-1} \sin\!\frac{\pi s}{2}\,\Gamma(1-s)\,\zeta(1-s).
$$

## 2. Riemann 의 두 증명

### 2.1 첫 증명 — 적분 contour 변형 (Riemann 1859 §II)
- 출발: $\Gamma(s)\zeta(s) = \int_0^\infty \frac{x^{s-1}}{e^x - 1}\,dx$ (Re s > 1).
- 적분 contour 를 (+∞ → 0 → +∞) 형 Hankel contour 로 변형:
  $$
  2\sin(\pi s)\,\Gamma(s)\,\zeta(s) = i\int_C \frac{(-x)^{s-1}}{e^x-1}\,dx
  $$
  ($C$: 원점을 양의 방향으로 도는 닫힌 contour)
- contour 를 음의 방향으로 변형하면 무한 다극점 $\pm 2\pi i n$ 에서의 residue 합이 됨.
- 이로부터 $\zeta(s)$ 와 $\zeta(1-s)$ 의 직접 관계.

### 2.2 둘째 증명 — Jacobi theta 함수
- 핵심 항등식 (Jacobi):
  $$
  \theta(x) := \sum_{n=1}^\infty e^{-n^2 \pi x}, \qquad 2\theta(x) + 1 = x^{-1/2}\bigl(2\theta(1/x) + 1\bigr).
  $$
- Mellin 변환:
  $$
  \pi^{-s/2}\,\Gamma\!\left(\tfrac{s}{2}\right)\,\zeta(s) = \int_0^\infty \theta(x)\,x^{s/2 - 1}\,dx \quad (\Re s > 1).
  $$
- 적분을 $[0,1] + [1,\infty)$ 로 분할, $[0,1]$ 부분에 Jacobi 항등식 ($x \mapsto 1/x$) 으로 변수 변환:
  $$
  \pi^{-s/2}\Gamma\!\left(\tfrac{s}{2}\right)\zeta(s) = \frac{1}{s(s-1)} + \int_1^\infty \theta(x)\bigl(x^{s/2-1} + x^{(1-s)/2 - 1}\bigr)\,dx.
  $$
- 우변이 $s \leftrightarrow 1-s$ 에 대해 *명시적으로 대칭*. ✓

## 3. 왜 임계선 σ = 1/2 인가

### 3.1 대칭 관점 (즉각적)
$\Lambda(s) = \Lambda(1-s)$ 의 고정점은 $s = 1/2 + it$ (실수 t 에 대해). 영점들이 *대칭축에 대해 짝지어짐*: ρ ↔ 1-ρ. 따라서 *모든* 영점이 한 직선 위에 있을 후보 직선은 σ = 1/2 외에 없다 (만약 모두 한 직선 위라면).

### 3.2 Hadamard 제약과 임계 띠
- 함수방정식 + Euler product 결합:
  - σ > 1: ζ(s) ≠ 0 (Euler product 절대수렴).
  - σ < 0: 함수방정식 + (1-s) 측의 ζ(1-s) ≠ 0 + Γ(s/2) 극점이 자명영점만 만듦.
  - 따라서 *모든 비자명 영점은 0 ≤ σ ≤ 1 (임계 띠) 안*.
- 임계 띠 *내부* 에서 함수방정식이 유일한 fixed-axis = σ = 1/2.

### 3.3 Ξ(t) 의 실/짝성
$\Xi(t) := \xi(1/2 + it)$ 가 *실값/짝함수*. 영점이 모두 *실수* t ⟺ 모든 비자명 영점이 σ = 1/2 위 ⟺ RH.

> **Hilbert–Pólya 직관의 출발**: Ξ(t) = 0 의 해 t 가 *실수* 라는 statement 는 *어떤 자기수반 연산자의 spectral statement* 와 같은 모양. 따라서 ζ 영점 = 어떤 Hilbert space 위의 자기수반 연산자 H 의 eigenvalue 라면 RH 자동.

### 3.4 함수방정식의 깊이 — 단일 사실 아님
함수방정식은 *uniqueness* 를 부여:
- Selberg 의 4개 공리 (Selberg class) 중 하나가 "함수방정식". 이 공리는 L-function 후보를 강력히 제한.
- 함수방정식 *없이는* RH 의 statement 자체가 의미 없다 (대칭축이 없음).

## 4. 함수방정식의 일반화 — RH가 *왜 보편적*인가

| 객체 | 함수방정식 형태 | RH 형태 |
|------|----------------|---------|
| ζ(s) | s ↔ 1-s | β = 1/2 |
| Dirichlet L(s, χ) | s ↔ 1-s + 가우스 합 부호 | β = 1/2 (GRH) |
| Hasse–Weil L_E(s) | s ↔ 2-s (centered at 1) | β = 1 |
| Modular L_f(s) (weight k) | s ↔ k - s | β = k/2 |
| Function field ζ(C, s) | s ↔ 1-s | β = 1/2 (Weil 1948 *증명됨*) |

대칭축이 *어떤 quantity 의 1/2* — 그것이 그 L-function 의 "critical line".

> Bombieri Clay 의 시각: "RH 는 단일 ζ 의 statement 가 아니라 *함수방정식+Euler product 가 부여하는 깊은 산술 구조*의 발현이다."

## 5. 함수방정식이 *주는 것* vs *주지 않는 것*

### 주는 것
- 영점 분포의 대칭 (β ↔ 1-β).
- 임계 띠로 영점 제한.
- 가능한 임계선 σ = 1/2 의 후보화.
- $\sum_\rho \frac{1}{|\rho|^2}$ 같은 합의 수렴 조건.

### *주지 않는 것* (RH 가 막혀온 본질)
- 영점이 *임계선 위에 있다*는 것은 함수방정식만으로 *나오지 않는다*.
- 함수방정식이 만족되지만 RH 가 *거짓* 인 객체가 존재할 수 있다 — 예컨대 일반적 Dirichlet 급수 (Selberg class 외).
- *왜* β = 1/2 이 정확한 값인지에는 산술적/스펙트럴 추가 입력이 필요.

## 6. 사고 과정 추정 (Riemann 의 시각)

- Riemann 1859 §III: "이 등식은 알려진 Π 함수의 성질을 통해 다음과 같이 표현 가능…" — 매우 간결. 그는 함수방정식을 *증명* 하나, 그 *의미* 를 길게 논하지 않는다.
- 대신 ξ(t) 도입 (s = 1/2 + ti 대입) 후 *바로* "the roots are very probably real" 추측.
- 추정: Riemann 은 함수방정식을 보자마자 σ = 1/2 의 특수성을 인지했고, ξ 의 실/짝성으로 영점 실수성을 *수치적으로* 확인했을 것. 그러나 *증명 시도* 는 "fleeting futile attempts" 로 멈춘 것.
- **시사점**: Riemann 의 "증명 전략" 이 우리에게 *전혀 남아있지 않다* — 그가 어디서 막혔는지조차 모름. (Siegel 이 Nachlass 에서 일부 발굴: Riemann–Siegel formula 등 계산 도구만 남음.)

## 7. 본 프로젝트에서의 함의

- 임계선의 *대칭 의미* 는 명확 — 따라서 RH 의 *형식*은 자연스럽다.
- *내용* (β = 1/2 인 이유) 은 함수방정식 외부에서 와야 한다. 즉 추가 산술/스펙트럴 입력이 필요.
- 시도 시 함수방정식만 사용하면 **명백히 부족** — 다른 도구 (Euler product / spectral / 산술) 와 결합 필요.
- 함수방정식만으로 RH 를 유도하는 것처럼 보이는 시도는 *순환 논증* 이 거의 확실 (어디선가 함수방정식의 변형을 추가 가정으로 넣었음).
