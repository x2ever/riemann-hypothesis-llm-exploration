"""Fetch a paper PDF and stage it into papers/pdf/ with INDEX.md stub.

Usage:
    uv run python fetch_paper.py arxiv 1801.05914 --key rodgers_tao_2020_dBN
    uv run python fetch_paper.py arxiv math/9811068 --key connes1999_ncg_trace
    uv run python fetch_paper.py url "https://example.com/paper.pdf" --key foo --filename foo.pdf
    uv run python fetch_paper.py search "tao de bruijn newman"   # WebSearch hint only

The script:
    1. Downloads the PDF to ../papers/pdf/<filename>.
    2. Verifies the magic bytes are %PDF.
    3. Prints a stub INDEX.md entry to stdout for the user to paste into papers/INDEX.md.

By design this script does NOT mutate INDEX.md automatically — INDEX.md is curated.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Final

import requests

PAPERS_DIR: Final[Path] = Path(__file__).resolve().parent.parent / "papers" / "pdf"
USER_AGENT: Final[str] = "Mozilla/5.0 (research; RH harness)"
PDF_MAGIC: Final[bytes] = b"%PDF"


def arxiv_url(arxiv_id: str) -> str:
    """Return the canonical PDF URL for an arXiv ID (handles new + old style)."""
    # Strip a leading "arxiv:" if user pasted it.
    cleaned = arxiv_id.removeprefix("arxiv:").removeprefix("arXiv:")
    return f"https://arxiv.org/pdf/{cleaned}"


def download_pdf(url: str, dest: Path) -> int:
    """Download URL to dest (overwrites). Returns size in bytes; raises on failure."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=60, stream=True)
    response.raise_for_status()
    with dest.open("wb") as fh:
        for chunk in response.iter_content(chunk_size=64 * 1024):
            if chunk:
                fh.write(chunk)
    return dest.stat().st_size


def verify_pdf(path: Path) -> None:
    """Raise if file does not start with %PDF magic bytes."""
    with path.open("rb") as fh:
        head = fh.read(4)
    if head != PDF_MAGIC:
        raise ValueError(
            f"Downloaded file is not a PDF (magic={head!r}). "
            f"Likely an HTML error page or paywall. Inspect: {path}"
        )


def emit_stub(key: str, filename: str, size_bytes: int, source_url: str) -> str:
    """Build a markdown stub for INDEX.md (printed to stdout, user pastes manually)."""
    size_kb = size_bytes // 1024
    return f"""
### [{key}] <Author, "Title", Year>
- **상태**: downloaded
- **카테고리**: <CAT>
- **파일**: `pdf/{filename}` ({size_kb} KB)
- **출처**: {source_url}
- **읽기 우선순위**: ★
- **사고 과정 추정 (TODO)**: <저자의 사고 흐름·도약 추정>
"""


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Fetch a paper PDF for the RH harness.")
    sub = parser.add_subparsers(dest="mode", required=True)

    p_arxiv = sub.add_parser("arxiv", help="Download by arXiv ID")
    p_arxiv.add_argument("arxiv_id", help="e.g. 1801.05914 or math/9811068")
    p_arxiv.add_argument("--key", required=True, help="INDEX.md key, e.g. rodgers_tao_2020_dBN")
    p_arxiv.add_argument("--filename", help="Override output filename (default <key>.pdf)")

    p_url = sub.add_parser("url", help="Download by direct URL")
    p_url.add_argument("url", help="Direct PDF URL")
    p_url.add_argument("--key", required=True, help="INDEX.md key")
    p_url.add_argument("--filename", help="Override output filename (default <key>.pdf)")

    p_search = sub.add_parser("search", help="Print search hint (no download)")
    p_search.add_argument("query", nargs="+", help="Search keywords")

    args = parser.parse_args()

    if args.mode == "search":
        query = " ".join(args.query)
        print(f"Search hint — try: arxiv.org / scholar.google / claymath.org with: {query}")
        print("Then run:  uv run python fetch_paper.py arxiv <id> --key <key>")
        return 0

    if args.mode == "arxiv":
        url = arxiv_url(args.arxiv_id)
    elif args.mode == "url":
        url = args.url
    else:
        parser.error(f"Unknown mode {args.mode!r}")
        return 2

    filename = args.filename or f"{args.key}.pdf"
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    dest = PAPERS_DIR / filename

    if dest.exists():
        print(f"SKIP (already exists): {dest}")
        size_bytes = dest.stat().st_size
    else:
        print(f"GET {url} -> {dest}")
        try:
            size_bytes = download_pdf(url, dest)
        except requests.HTTPError as e:
            print(f"FAIL: {e}", file=sys.stderr)
            return 1
        verify_pdf(dest)
        print(f"OK: {size_bytes // 1024} KB")

    print("\n--- INDEX.md stub (paste under '## 다운로드 완료') ---")
    print(emit_stub(args.key, filename, size_bytes, url))
    return 0


if __name__ == "__main__":
    sys.exit(main())
