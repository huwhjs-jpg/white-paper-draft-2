# China Playbook v2 (batch 3) working files

- `00-evidence-topup-note.md`: one-page note on the evidence top-up (brief §7), 2 Oct 2026.
- `text/ch1.html` to `text/ch4.html`: new chapter text in assembly-source conventions (h3/h4, `.inbrief`, `.exm`, `.case`, `sup`), ready for `parse.py`.
- `review/ch1-review.html` to `review/ch4-review.html`: side-by-side review pages (new text against approved v1 text, change notes, fix log, decisions, sources).
- `draft/`: integrated draft v2 (.md, .html, .docx), built by `tools/assemble_draft.py`.
- `HANDOVER-BRIEF-v4.md`, `outline-v6.md`, `decisions-and-fix-log.md`, `sources-batch3.md`, `research/`: handover notes and raw research.
- `tools/`: `review_page.py` builds the review pages from `text/`, `chapter_data.py` (notes, fix log, decisions) and `sources.py` (new N-numbered sources).

Rebuild the review pages with `python3 v2/tools/review_page.py ch1 ch2 ch3 ch4`. This needs beautifulsoup4 and lxml.
