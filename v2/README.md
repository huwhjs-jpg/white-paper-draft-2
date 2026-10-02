# China Playbook v2 (batch 3) working files

- `00-evidence-topup-note.md`: one-page note on the evidence top-up (brief §7), 2 Oct 2026.
- `text/ch1.html`, `text/ch3.html`: new chapter text in assembly-source conventions (h3/h4, `.inbrief`, `.exm`, `.case`, `sup`), ready for `parse.py`.
- `review/ch1-review.html`, `review/ch3-review.html`: side-by-side review pages (new text against approved v1 text, change notes, fix log, decisions, sources).
- `tools/`: `review_page.py` builds the review pages from `text/`, `chapter_data.py` (notes, fix log, decisions) and `sources.py` (new N-numbered sources).

Rebuild the review pages with `python3 v2/tools/review_page.py ch1 ch3`. This needs beautifulsoup4 and lxml.
