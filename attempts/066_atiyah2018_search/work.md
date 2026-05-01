# Work — Attempt 066 (Atiyah 2018)

## Paper structure
- 5 페이지 short paper.
- §1 introduction (Abel lecture 출처).
- §2 Todd function T(s) — *weakly analytic*, properties 2.2-2.7.
- §3 proof of RH — by contradiction, F(s) = T{1+ζ(s+b)}-1.
- §4 "Deus ex Machina" — *magic 인정* (저자 자체 표현).
- §5 final speculations.

## §3 "proof" 의 logical structure

(i) Suppose ∃ b in critical strip, off critical line, ζ(b) = 0.
(ii) F(s) := T{1 + ζ(s+b)} - 1.
(iii) F(0) = T{1+0} - 1 = T(1) - 1 = 0 (by 2.3).
(iv) 2.6 의 multiplicative identity 적용: T{(1+f)(1+g)} = T{1+f+g}.
(v) f = g = F substitute → F(s) = 2F(s).
(vi) C char 0 → F ≡ 0.
(vii) T(1+s) = 1 ⟹ s = 0 (T invertible) → ζ(s+b) ≡ 0 → ζ ≡ 0 contradiction.

## 치명적 결함 (paper-direct, 알려진 비판들)

[rigorous]:

**결함 1 — T 의 존재성**: T 의 properties (2.2-2.7) 가 paper [2] (Royal Society 제출, *미발표*) 에 의존. Atiyah 가 본 paper 에서 *summarize 만*. *T 자체의 well-definedness verify 불가*.

**결함 2 — 2.6 식의 strong condition**: T{(1+f)(1+g)} = T{1+f+g} 가 *polynomial 의 linear approximation* 단계 (paper 자체 인정 — "linear approximation of expansion"). 그러나 §3 proof 에서 *exact* equality 사용 — 일관성 X.

**결함 3 — F(s) = 2F(s) 의 identity 추출**: (1+F)(1+F) = 1 + 2F + F² ≠ 1 + 2F. T{1+2F+F²} = T{1+2F} 라는 *이중 적용* 이 2.6 의 strict 한 한정 (degree 0 또는 linear) 위배.

**결함 4 — T invertibility**: T(1+s) ≡ 1 ⟹ s ≡ 0 *step* — T 가 polynomial of bounded degree 이면 T^{-1} 가 *generically multi-valued*. paper 가 specifics 미제시.

**결함 5 — §5 자체 인정**: "the most general version of the Riemann Hypothesis will be an undecidable problem in the Gödel sense" — 이건 *proof claim* 과 *충돌*. paper 의 RH proof 가 specific case 만 인지하나, 같은 §5 가 *most general* 은 undecidable 이라 명시.

## Wall mapping

본 paper 의 fail 은 lemma `spectral_candidate_circularity_check` 의 *step 6 trivial circular* 와 다름. 새 fail 카테고리:
- *Reference circular*: 핵심 객체 (T) 의 well-definedness 가 다른 paper 에 의존, 그 paper 미발표/검증 X.
- *Identity transplant*: linear approximation level 식을 *exact* 으로 사용.

## Lemma 후보

**Failed proof analysis lemma** 추가 가치 — 본 paper 의 fail 카테고리 명시.

## 우리 contribution

[rigorous, paper-direct]:
- *알려진 fail* 의 우리 wall taxonomy 와 mapping.
- *novel content X*. paper-direct critical reading.

## "예상 가능 결과" self-check
yes — 알려진 fail.

## yellow flag check (045)
- "evidence" / "강화" / "resolved" 사용 X.
- "fail" 단어는 paper-direct critical reading — yellow X.
