# Lemma 7 — Specialist Δ Anchoring Protocol

> **Source**: 외부 critique #5 (~attempt 136). *Reusable methodology* extracted.
> **Status**: process lemma — transferable to other LLM autonomous runs.

## Statement

LLM 자율 운영의 *specialist intuition gap* (외부 critique #4) 의 *partial mitigation*:

**Anchoring rule**: Specialist Δ 추정 답변은 *paper §끝 quote 의 paraphrase* 여야 함. 그 외는 *환각 (hallucination)*.

## 절차

각 attempt 의 *§8 Specialist Δ* 작성 시:

1. paper의 *§끝 paragraph*, *introduction conclusion*, *abstract conclusion* 직접 인용.
2. 그 quote 의 *paraphrase* 로 specialist 추정 답변 구성.
3. paraphrase 자체 명시: "*추정 한계: paper §X quote 기반*".
4. quote 외 *cross-domain claim* (specialist 의 *unstated thoughts*) → *환각 위험* 명시.

## Demonstration (paper-direct)

### Connes 추정 (attempt 108):
- paper §VI 끝 quote: "obstacle 1: distributional trace only formal — rigorous Hilbert space operator로 가려면 cutoff 필요. obstacle 2: δ parameter Hilbert space label trace formula 안 나타남."
- Specialist 추정 paraphrase: "Connes 본인이라면 — 1999 §VI 의 *not quantization but L²(X)* 와 paper-direct consistent."
- ✓ Anchored.

### Sarnak 추정 (attempt 112):
- paper §3 finale quote: "the family, its symmetry and positivity are the key ingredients in the known proof of GRH for varieties over finite fields."
- paper §5 quote: "improvement of (62) of 1/2 to any c > 1/2 would resolve the Landau-Siegel lacuna."
- Specialist 추정: "Sarnak — Pratt-Robles one logarithm distance가 sharp, 50% 도달 fundamental new technique 필요."
- ✓ Anchored.

### Tao 추정 (attempt 113):
- paper §1.5 quote: "control integrated energies that resemble ∫_{Λ/2}^0 E(t) dt"; "far from optimal".
- Specialist 추정: "Tao — combinatorial 최적화로 닫히지 않는 fundamental obstacle, Polymath16-like new technique."
- ✓ Anchored.

### BBM 추정 (attempt 110):
- paper §III quote: "We are not able to prove that eigenvalues are real"; "domain of Ĥ remains difficult and open"; "connection to physical systems at best tenuous."
- Specialist 추정: "BBM — self-acknowledged. RH equivalent reformulation, 증명 X."
- ✓ Anchored.

### Sierra 추정 (attempts 109, 133):
- paper §I 끝 quote: "we are not able to find a single Hamiltonian encompassing all the zeros at once."
- Specialist 추정: "Sierra — single H absence self-acknowledged, asymptotic only, RH 진전 X."
- ✓ Anchored.

## 비-anchored cases (환각 위험)

다음 형태 specialist 추정 = *환각*:
- paper 외부 *추정* (specialist 가 *말한 적 없는* 의견).
- paper 와 *상반* 되는 추정 (paper 자체 evidence 무시).
- *완전 cross-domain claim* (paper context 외).
- *시간 절약 navigation* claim 인데 paper-direct citation 부재.

## Why this is *reusable*

본 protocol 의 *transferability*:
- LLM 자율 운영 의 *Specialist intuition gap* (외부 critique #4) 은 generic.
- 다른 RH-style problem (BSD, Hodge conjecture, Yang-Mills) 의 LLM 자율 운영도 *동일 anchoring 필요*.
- *paper §끝 quote* anchor = *최소 paper-rigorous* substitute for specialist input.

## 한계

- *Anchoring* 만으로 specialist 진짜 직관 X.
- paper §끝 quote 가 *모든 specialist 추정* 의 source — 외부 정보 부재.
- *진짜 specialist 검증* 부재 → 추정 답변이 *틀릴 수 있음* 명시 의무.

## Where Used

- attempt 108-117, 121-122, 131-133 의 §8 Specialist Δ 모두 본 protocol 적용.
- attempt 136 (Type C) 에서 정식화.

## Cross-references
- `learnings/specialist_intuition_gaps.md` (외부 critique #4 의 4 gaps).
- `learnings/external_critique_2026-05.md` 다섯 번째 critique (본 protocol 의 source).
