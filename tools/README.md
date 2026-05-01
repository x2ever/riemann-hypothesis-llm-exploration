# tools — 수치 실험 인프라

> 수치 실험은 직관 보조다. **증명이 아니다.**

## 설치

```bash
cd tools
uv sync
```

## 스크립트

- `verify_zeros.py` — 첫 N개 비자명 영점이 Re(s)=1/2 에 있는지 mpmath로 확인
  ```bash
  uv run python verify_zeros.py -n 50 --dps 50
  ```

- `fetch_paper.py` — 논문 PDF 다운로드 + INDEX.md 스텁 생성
  ```bash
  # arXiv ID 로
  uv run python fetch_paper.py arxiv 1801.05914 --key rodgers_tao_2020_dBN

  # 직접 URL 로
  uv run python fetch_paper.py url "https://www.claymath.org/.../foo.pdf" --key foo

  # 검색 힌트만
  uv run python fetch_paper.py search "tao de bruijn newman"
  ```
  파일은 `papers/pdf/<key>.pdf` 로 저장. 매직바이트(%PDF) 검증 후 INDEX.md 에 붙일 스텁을 stdout 으로 출력 — INDEX.md 는 사람이 직접 편집 (큐레이션 유지).

- `mertens.py` — Mertens function M(x), RH 동치 |M(x)| = O(x^(1/2+ε)) 수치 검증
  ```bash
  uv run python mertens.py 100000 --step 5000
  ```

- `li_criterion.py` — Li's criterion λ_n ≥ 0 ⟺ RH, 영점 합으로 λ_n 근사
  ```bash
  uv run python li_criterion.py -N 20 --zeros 100
  ```

- `pair_correlation.py` — 영점 정규화 간격 vs GUE pair correlation density
  ```bash
  uv run python pair_correlation.py -n 200 --bins 20
  ```

- `li_rmt.py` — Li's λ_n vs RMT/GUE cross-check (3 mode: naive/affine/rank)
  ```bash
  uv run python li_rmt.py --n-max 20 --zeros 100 --mode affine
  ```

- `cross_check.py` — generic cross-check framework + auto-diagnosis (PASS/OFFSET/STRUCTURAL)
  ```bash
  uv run python cross_check.py  # synthetic smoke test
  ```

## 추가 예정 (시도 중 필요 시)

- `gram_points.py` — Gram point 분석
- `argument_principle.py` — 영점 카운팅 (N(T))
- `explicit_formula.py` — von Mangoldt 명시 공식 검증
- `moments.py` — I_k(T) zeta moments + Keating-Snaith 비교
