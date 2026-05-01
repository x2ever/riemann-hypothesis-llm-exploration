# Work — Attempt 059 (Lemma 2.2 verify)

[numerical, dps=40, 200+200 conj zeros]

## λ_n = Σ_{j=1..n} (-1)^{j-1} C(n,j) σ_j (Lagarias 2.18)

| n | direct | via σ_j | diff |
|---|---|---|---|
| 3 | 0.189091 | 0.189091 | 0 |
| 5 | 0.524022 | 0.524022 | 0 |
| 10 | 2.073258 | 2.073258 | 0 |
| 20 | 7.944988 | 7.944988 | 0 |

Diff exactly 0 (within mpmath precision) — Lagarias 2.18 의 numerical confirmation. paper-direct.

[증명 X]: *알려진 formula sanity*. *우리 contribution 0*.
