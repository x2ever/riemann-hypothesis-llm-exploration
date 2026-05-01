# Attempt 010: BBM Hamiltonian — Boundary Condition Sanity Check
**Type**: A (Proof attempt, computational)

## 가설/전략

Bender–Brody–Müller (2017) 의 Hamiltonian 의 *eigenfunction* 정의:
$$\psi_z(x) = -\zeta(z, x+1)$$
(Hurwitz zeta) 와 boundary condition $\psi_z(0) = 0$.

이 boundary condition 의 *내용*:
$$\psi_z(0) = -\zeta(z, 1) = -\zeta(z)$$

따라서 $\psi_z(0) = 0 \iff \zeta(z) = 0$. 즉 BBM "boundary condition" 은 자동으로 ζ 영점 → spectrum.

> **H1 (sanity check)**: $\psi_z(0) = -\zeta(z)$ 항등식의 *수치 검증*. 첫 N 영점에서 $\psi_{\rho_n}(0) = 0$ (1e-10 정밀도).
>
> **H2 (의문)**: BBM 의 self-adjointness 주장이 *implicit 하게 RH 와 동치 변형* 인지 — boundary condition 자체가 영점을 *입력으로* 받음.
>
> **H3**: finite truncation 에서 ψ_z 가 어떻게 행동? non-zero z (영점이 아닌 z) 에서 $\psi_z(x) \to ?$ as $x \to 0$.

## 동기

- Wall #5 (SELF-ADJOINT-RIGOR) 의 *순환 점검* — BBM 의 spectrum 정의가 trivially RH 와 동치인지.
- 008 의 channel diversification — 새 채널 (HP/spectral).
- attempts 의 첫 *비판적 reading* — BBM 의 알려진 한계를 직접 확인.

## 분류
- III (HP/spectral) + IX (computational).

## DoD
- [ ] $\psi_z(0) = -\zeta(z)$ identity 수치 검증, 첫 10 영점.
- [ ] non-영점 z 에서 ψ_z(0) 의 *비-소멸* 확인.
- [ ] BBM 주장의 *circular vs non-trivial* 분리 명시.
- [ ] postmortem 에 Wall #5 sharper formulation.

## 명시적 비-실패

본 시도는 *증명 시도가 아니라 sanity check*. 결과가 trivial confirmation 이라도 valid — 그 *trivial* 함이 wall #5 의 본질.
