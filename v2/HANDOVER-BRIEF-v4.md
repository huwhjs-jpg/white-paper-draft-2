# China Playbook upgrade: handover brief v4

Written 2 October 2026, at the end of the fourth working session. **This brief is self-contained.** It supersedes brief v3 (same date, earlier), which stays in the kit for reference. Read this first, then the draft.

## Where things stand

The paper, *The China Playbook for Emerging Asia*, is being rewritten from its approved v1 text (15 chapters, Word draft v1 of 62 pages) into a shorter four-chapter paper. The body must fit in 20 pages.

**In this session:**
1. **The evidence top-up from brief v3 §7 was run.** Most sources were opened and checked directly once network access was granted; a few still block automated reading.
2. **All four chapters were written.** Each was published next to the approved v1 text with a fix log. The chapters were then **rewritten for flow** at the user's request: plainer and less mechanical, written for a normal reader.
3. **First drafts were written** of the executive summary, About this paper and the conclusion.
4. **A plan for the appendices** was set out; the appendices themselves are not written yet.
5. **Everything was packaged here:** the integrated draft is `China Playbook — Draft v2 full text (2 Oct 2026)`, in .md, .html and .docx.

**What the user has seen and said:**
- Approved outline v5.
- Asked for plain language: "assume a normal human is reading this", and avoid AI jargon such as "load-bearing".
- Said "proceed" to the flow rewrite and to the provisional decisions (§5).
- Has not yet reviewed the rewritten chapters, the executive summary, About this paper or the conclusion.

---

## 0. Files

### For the Claude Project (upload these; the names are dated)

| File | What it is | Status |
|---|---|---|
| China Playbook — Handover Brief v4 (2 Oct 2026).md | This brief | **Supersedes brief v3** |
| China Playbook — Draft v2 full text (2 Oct 2026).md (and .docx) | The integrated draft: summary, about page, four chapters, conclusion, appendix plan, references cited | **Current text** |
| China Playbook — Outline v6 plain-language (2 Oct 2026).md | The structure, in plain words | **Supersedes outline v5** (keep v5 as the approved base) |
| China Playbook — Decisions and fix log, batch 3 (2 Oct 2026).md | Every decision, move and correction, by chapter and section | Current |
| China Playbook — Sources added in batch 3 (2 Oct 2026).md | New sources N1–N41, v1 references still cited, open source gaps | Current |
| China Playbook — Evidence top-up note (2 Oct 2026).md | The one-page top-up note | Current |
| China Playbook — New research data, batch 3 (2 Oct 2026).md | UN Comtrade robot re-pull and verbatim filing extracts | Current |
| china-playbook-handover-kit-v4.zip | Everything: the v3 kit contents plus all batch 3 work, scripts and raw data | Current |

### Existing Project files and their status

| File | Status |
|---|---|
| China Playbook — Handover Brief v3 (2 Oct 2026).md / HANDOVER-BRIEF-v3.md | Superseded by v4. Keep for history. |
| restructure-v5.html | The approved outline; superseded in presentation by outline v6. Keep. |
| china-playbook-assembly-source.html | The approved v1 text. **Still needed:** the appendices are built from it (v1 Chapters 10–15, Appendices A–C). |
| archetype-evidence-dossiers.md; evidence-log-and-trade-data.md | Still valid. Apply the corrections in §6 below (Hengli, Haitian share, laser case date). |
| china-playbook-lessons-from-past-white-papers.md; pdf-gap-fill-supplement.md | Benchmark and house style. Unchanged; use them for the Step 9 checks. |
| china-playbook-handover-kit-v3.zip | Superseded by kit v4, which contains it in full. |

### Inside kit v4

| Path | What it is |
|---|---|
| `HANDOVER-BRIEF-v4.md` | This brief |
| `v2/draft/` | The integrated draft (.md, .html, .docx) |
| `v2/text/` | Source text in assembly-source HTML conventions (h3/h4, `.inbrief`, `.exm`, `.case`, `.tw`, `sup`), ready for `parse.py`. Files: `exec`, `about`, `ch1`–`ch4`, `conclusion`, `appendices-plan` |
| `v2/review/` | Side-by-side review pages for Chapters 1–4 |
| `v2/tools/` | `assemble_draft.py` (builds the draft), `review_page.py` (builds the review pages), `chapter_data.py` (notes, fix logs, decisions), `sources.py` (N-source register), `review.css` |
| `v2/research/` | `comtrade/` (raw JSON plus README summary); `filings/extracts-read-2-Oct-2026.md` |
| `v2/outline-v6.md`, `decisions-and-fix-log.md`, `sources-batch3.md`, `00-evidence-topup-note.md` | Working notes (the same as the Project files above) |
| `benchmark/` | The two benchmark files |
| `build/`, `original-kit/`, `research/`, `evidence/`, `outline/`, `fonts/`, `draft/` | Unchanged from kit v3: build pipeline, approved text, fact-check JSON, dossiers, v1 Word draft |

**Published review pages** (the user's account, private): Chapter 1 https://claude.ai/artifact/U8MqWfPoUwgznHBNMiMcUe · Chapter 2 https://claude.ai/artifact/2DgAnHgmiHYb8X17A6DRBu · Chapter 3 https://claude.ai/artifact/WqDbtqY1gGcX4XYU1QRwPa · Chapter 4 https://claude.ai/artifact/PS45feWA1EaiciZaAW9Pmm. Everything on them is in the kit, so don't rely on the links.

**GitHub:** repository `huwhjs-jpg/white-paper-draft-2`, branch `claude/magical-davinci-uj8x0f`.

---

## 1. The user's standing instructions (follow throughout)

- **Free, publicly verifiable sources only.** No paid databases, surveys or interviews.
- **Write for a normal reader, not an industry expert.**
  - Use plain words, short paragraphs and clear signposting.
  - Define each term once; keep acronyms in the glossary; no product codes in the text.
  - Avoid AI jargon and stock phrases ("load-bearing", "worth noting", "lens" and the like).
  - Prefer a story to a framework: introduce each tool where it is first needed.
- **Body length:** the chapters must fit in 20 pages (about 7,000 words). The executive summary, About this paper and the appendices are excluded.
- **Accuracy:** fix accuracy errors directly and log them. Show the user first anything that changes a verdict, a learning or a headline number.
- **Batches:** work in batches, and show each chapter side by side with the approved text, with a fix log.
- **Robots** stay a separate section (3.3), placed after factory machines.
- **Ignore for now** the back-matter order, firm formatting and the house template's look.
- **Keep exactly as approved:** the governing thought, the central question, the six learning labels, the six reader types and the six failure modes (§3).
- **Firm-focused, not author-focused:** no author bios. Use "we" for judgements, never "you".
- **When the user says "proceed",** they mean carry on and adopt the proposals on the table. Still list anything provisional so they can reverse it.

---

## 2. Status

**Done**
- Steps 1–8 of the original rewrite (approved v1 text; Word draft v1).
- Outline v5 approved; evidence build batch 2 (dossiers, 36-product trade screen, 2015–25 series).
- **Batch 3 (this session):**
  - evidence top-up, mostly checked against primary sources;
  - Chapters 1–4 written, side-by-side pages published, then rewritten for flow;
  - first drafts of the executive summary, About this paper and the conclusion;
  - appendix plan, integrated draft and this package.

**Left (in order)**
1. **User review** of the rewritten Chapters 1–4, the executive summary, About this paper and the conclusion. Get explicit sign-off on the provisional decisions in §5.
2. **Appendices A–F**, from the plan in the draft (each item names its source material).
3. **Nine body exhibits** plus the appendix exhibits (§8).
4. **References:**
   - renumber by first citation;
   - merge the v1 references still cited with N1–N41;
   - drop the ones no longer cited;
   - give every entry a "Used for" note;
   - exhibit source lines use the same numbers.
5. **Word draft v2** through the build pipeline (§9), fitted to 20 body pages.
6. **Step 9 checks**, including an independent reviewer (§9).
7. **Firm inputs** (§10).

---

## 3. Locked items (unchanged)

- **Governing thought:** Chinese OEMs won share mainly by redesigning the commercial system around the machine, not by selling it cheaply, and most of their moves can be copied.
- **Central question:** Which of the moves that won Chinese OEMs share can be copied, by whom and how fast, and which product categories will they reach next?
- **Chapter 3 qualifier:** in the next products the same moves arrive in a different order, and the buyer decides the order.
- **Six learnings (labels locked):**
  1. Enter through a narrow beachhead, then broaden.
  2. Treat customer credit as part of the product.
  3. Price just enough, then invest in the lifecycle.
  4. Localise plants, then export from the host.
  5. Turn local-content and investment rules into an advantage. Never write "FDI rules".
  6. Use electrification as the entry wedge.

  They are grouped as Getting in (1, 6), Winning customers (2, 3) and Staying (4, 5). **In the running text the labels appear in bold without numbers**, so the reading order does not jump; numbers appear only in lists such as the appendices.
- **Six reader types:** global incumbents; Indian and ASEAN champions; dealers; financiers; Chinese OEMs planning their next market; policymakers.
- **Six failure modes:**
  - buyers return where uptime matters;
  - a loyal installed base holds;
  - high share invites trade cases;
  - overseas acquisitions lose money;
  - dealer networks outgrow parts supply;
  - price wars at home drain cash.
- **Locked fixes from earlier briefs still apply.** The key ones:
  - **F1:** India's crane duties were recommended on 19 Sep 2025 and not imposed within the three months Rule 18(1) allows. Never write "pending".
  - **F2:** the 10% / 12.5% US tariffs come from the forced-labour Section 301 action, effective 24 Jul 2026.
  - **F6:** United Tractors, Jan–Aug 2026: Komatsu 2,689 units (−21%); large mining 436 units (−49%).
  - **F8:** the combined Komatsu and Hitachi share is "indicative".
  - **F9:** parts and service are about 37% of United Tractors' machinery revenue (H1 2026).
- **Settled decisions from earlier briefs:**
  - colours: China blue #0B6FD9, Japan amber #C07A00 (dark mode #3383E0 / #B97A12);
  - India's verdict is "structural";
  - signpost thresholds: Komatsu above 25% for two quarters; electric above 5% of excavator exports;
  - the crane-duty wording is flagged for counsel.

---

## 4. The structure (outline v6)

The full outline is in `Outline v6 plain-language`, and the full text is in the draft. In brief:

- **Executive summary** (first draft):
  - the governing thought;
  - three numbers: Indonesia's excavator imports from China 33% → 75%; India's crane imports 35% → 93%; robots passed Japan in 2025;
  - the verdict;
  - the six learnings by pair;
  - what comes next;
  - the limits;
  - one line per reader.
- **About this paper** (first draft): reader map, scope, method, links to YCP's Dec 2025 and Jun 2026 papers.
- **Chapter 1. What happened?**
  - Opens on the Komatsu puzzle: share fell from 29% to 20% while coal output was near its record.
  - 1.1 The size of the shift (Exhibit 1).
  - 1.2 The two turns, 2022 and 2025, with the 2026 rule changes (Exhibit 2).
  - 1.3 Not a commodity boom; the verdict.
  - 1.4 The credit question. Ends with the central question.
- **Chapter 2. How did they do it?** Three stories, each ending with "What others can copy":
  - 2.1 Getting in.
  - 2.2 Winning customers (Exhibit 3).
  - 2.3 Staying (Exhibit 4).
- **Chapter 3. Where is it heading next?**
  - 3.1 How a product is bought sets the pace, introducing the three kinds of buyer and the "overtook Japan" years (Exhibit 5).
  - 3.2 Factory machines follow Chinese factories (Exhibit 6).
  - 3.3 Robots, one step behind (Exhibit 7; warehouse-robot box).
  - 3.4 Off-the-shelf equipment moves on price.
  - 3.5 How much time each kind of buyer leaves.
- **Chapter 4. What can each reader do?** *(retitled; provisional)*
  - 4.1 Where it breaks: the failure-mode table, plus the limits of each move.
  - 4.2 The established brands are already copying it.
  - 4.3 A first move per reader (Exhibit 8).
  - 4.4 Our view to 2030 and five signs to watch (Exhibit 9).
- **Conclusion** (first draft).
- **Appendices A–F** (planned).

Body length is about 6,800 words: Chapter 1 about 1,130; Chapter 2 about 1,850; Chapter 3 about 2,160; Chapter 4 about 1,670, including tables.

---

## 5. Decisions taken in batch 3 (confirm with the user)

**Provisional decisions** (the user said "proceed"; each is reversible):
1. **Thai excavators.**
   - Do not say "Japanese brands held Thai excavators". SANY Thaiyont reports it was Thailand's top excavator seller in 2020 (1,600 units) and 2021 (1,840 units, 30.4%) (N41).
   - The Thailand verdict is unchanged.
   - Failure mode 2 is evidenced with India: JCB backhoes (34,632 against LiuGong's 1,061 registrations in FY26) and Indian pumps flat at 32–39%.
   - The Thai line is removed from the executive summary.
2. **Indian excavator asking prices dropped.**
   - TractorJunction: SANY INR 41–43 lakh against Komatsu INR 74–76 lakh, a gap too wide and too source-dependent to support "inside the incumbents' range".
   - Learning 3 now rests on DGTR's 0–10% crane undercutting, the INAPROC listings (SANY Rp2.10bn against Komatsu Rp2.25bn, including VAT) and SANY's 2021 price cut.
3. **Crane credit attributed to XCMG.** The "not normal" three-year credit in the DGTR findings (paras 47, 134) is XCMG's related exporter's, and DGTR uses it to adjust export prices; it is not named as a cause of injury. The v1 executive summary's Learning 2 line is reworded accordingly.
4. **Chapter 4 title:** "What can each reader do?" replaces the approved "What should you do about it?", to keep "we, never you".
5. **Our judgements in Chapter 3.5:** factories have "a few years at most"; for robots, "until about 2030"; plant engineers, the longest window.
6. **New thresholds for signs 1–3:**
   - China above 50% of robot imports, or the first Chinese robot service or assembly site in the region;
   - any Indian duty imposed on Chinese construction equipment;
   - a second maker-owned finance licence in Indonesia.
7. **Moved out of the body** into the appendices (§8 plan):
   - the overseas-revenue league table;
   - the UK–India and EU–India agreements, the US Section 122 surcharge and the US excess-capacity case;
   - the state-support paragraph;
   - three dropped signposts (Press Note 2 approvals, EU–India entry into force, coal quotas);
   - the "three paths" scenarios;
   - mixed channels and SANY India's auction portal;
   - the Thai EV 3.5 box (Neta stays as failure mode 5).

**Approved by the user ("Proceed")**, the flow rewrite:
- Chapter 1 opens on the Komatsu puzzle.
- The tools are introduced where first needed.
- Chapter 2 is told as three stories.
- The "where it stops" material is in Chapter 4.1.
- The 2030 view and the five signs are merged at the end of Chapter 4.

---

## 6. Corrections (fixed and logged)

**From brief v3 §6, now applied:**
- (1) MoU, with Sany Perkasa as SANY's "official distributor" (its own site, ref 92).
- (2) Crane credit softened (see §5.3).
- (3) Chakan "more than INR 1,000 crore", with the 1,200 machines being SANY India's company-wide figure.
- (4) Weda Bay is "XCMG's first overseas new-energy factory".
- (5) Turning point 1 is 2022 at company level; exports passed home sales in units in 2023.
- (6) Robots: 55%, down from 57%.
- (7) Omnibus regulation rescinded; QCO is a draft.
- (8) India compressors rose mainly in 2024; 49.3% in 2025.
- (9) 720 Mt is a projection, not a quota.
- (10) Highway pace: 25 km a day in FY26; 21 km a day expected in FY27.
- (11) Inovance "about 6%" labelled secondary.
- (12) ELGi's estimate is not used in the body.
- (13) Estun cited to HKEX.
- (14) HINABI: drop if unused (Appendix A).
- (15) The Haitian caution is included.

**New in batch 3** (the details and sources are in the decisions log):
- **Haitian:** overseas share 42.9%, not 42.8%. The filing's English wording credits "the global expansion of Chinese enterprises". The annual report carries an **INR1,859m (RMB146m) provision** for an Indian customs anti-dumping claim against Haitian's Indian unit, already present in 2024.
- **India's laser case:** initiated **29 Sep 2022** (not October); findings dated 27 Sep 2023 and posted 5 Oct 2023. **Imports from China held 78% (2018-19) to 83% (2021-22) of Indian demand** (findings table, read by OCR).
- **Hengli:** overseas sales about **19%** (RMB2,106m, +1.6%, against RMB8,750m at home), not "over 35%". This corrects the dossier.
- **SANY 2022:** overseas gross margin 26.4% against 21.9% in China. "For the first time" is dropped; the release doesn't say it.
- **Coal:**
  - 2025 output 817.48 Mt (an earlier estimate said 790 Mt);
  - the 2026 work-plan (RKAB) target was about 600 Mt, with 580 Mt approved by 27 Mar;
  - lenders were reluctant to lend without approval (Jakarta Post, 9 Apr);
  - 95% of revised plans were approved by 29 Sep, with output "in between" 720 Mt (Detik).
- **Indonesia's local-content score:** 51.21% is the combined score (TKDN 36.2 plus BMP 15), which is the one tested against the 40% bar. SANY's listing shows 0% and is marked as an import.
- **GeM listing claim** replaced by the July 2020 tender-registration rule.
- **XCMG's +23.6% new-energy growth** dropped; it is not in the cited source.
- **Atlas Copco:** Liutech now markets dedicated ranges for India and Southeast Asia (its own pages); Bolaite not found.
- **Hai Robotics** opened a Penang factory in 2025; "with a manufacturing partner" is dropped, because it is not stated.

---

## 7. Key evidence added in batch 3

Full detail is in the top-up note, the sources register and the research-data file.

**Robots (UN Comtrade re-pull, 2 Oct 2026):**
- **Four markets:** China 22% → 42%, Japan 36% → 27% (2019 → 2025).
- **By country, 2025:**

  | Market | China | Japan |
  |---|---|---|
  | India | 34% | 30% |
  | Thailand | 44% | 28% |
  | Malaysia | 40% | 36% |
  | Indonesia | 62% | 12% |

- **Indonesia's 62% is lumpy:** US$61.5m from China out of US$99.1m. US$51m of the Chinese total arrived in Sep–Dec 2025, US$30.2m of it in October alone, which suggests one or more large plant fit-outs (BYD's Subang plant is a possibility, unconfirmed). Japan fell from US$22.2m to US$11.4m.
- **Without Indonesia,** China went from 21% to 37% and Japan from 35% to 31%. The headline holds.

**Primary filings read:**
- DGTR crane findings (credit and undercutting paragraphs);
- DGTR laser findings (market-share table);
- Haitian 2025 results and annual report;
- Hengli 2025 annual report.

**Pages read:**
- SANY FY2022 release;
- IMA (coal 2025);
- CNBC Indonesia (RKAB 580 Mt and the about-600 Mt target);
- Jakarta Post (lenders and RKAB);
- Detik (95% approved; about 720 Mt);
- SANY Thaiyont (30.4%);
- Liutech India and Southeast Asia pages;
- Hai Robotics (Penang);
- the pumps QCO draft;
- TractorJunction (SANY and Komatsu prices);
- Sany Perkasa (official distributor).

**Still search-verified only** (the sites block automated reading):
- INAPROC listings (N40);
- Desimachines;
- the Investing.com ELGi summary (N37);
- the electrive BYD article (N21).

**Open gaps:**
- the source for Inovance's "about 6%";
- the full URL for the Siasun March 2025 page;
- who bought Indonesia's 2025 robots;
- a named warehouse-robot deployment in India or ASEAN;
- Bolaite in India or ASEAN;
- India's final pumps QCO (watch for it).

---

## 8. Exhibits (nine in the body) and appendices

| No. | Exhibit | Build from |
|---|---|---|
| 1 | Where China gained, by country and product, 2019 → 2024 (add 2025 where reported) | v1 Ex 7 / pack heat map (`build/ex/ex07.png`, `pack_ex.py`) |
| 2 | Timeline: home vs export excavator units 2016–H1 2026, SANY's overseas share, the two turns | New; v1 Ex 5 as base. Data in brief v3 §5 and the Ch1 text |
| 3 | SANY's finance story in Indonesia (2017 MoU → 2018 loans → 2025 RMB1.45bn → 2026 licence; XCMG joint venture) | v1 Ex 14; fix "MoU" |
| 4 | The moves over time (add the 2025–26 moves) | v1 Ex 20 |
| 5 | Where each product stands: year China overtook Japan, and which moves are visible | New; `evidence/comtrade_series.md` and the dossier grades |
| 6 | Factory machines: China vs Japan, 2015–2025, with India's duty dates (Dec 2023 lasers; Jun 2025 plastic-moulding) | New; `comtrade_series.md` |
| 7 | Robots: China vs Japan by country, 2019 and 2025 | New; `v2/research/comtrade/README.md` |
| 8 | Actions by reader | v1 Ex 29, simplified to first moves plus horizons |
| 9 | Five signs, with latest reading and threshold | v1 Ex 30, cut to five (table in Ch4.4) |

- **Colours:** China blue #0B6FD9, Japan amber #C07A00.
- **Rendering:** `python3 build/render_ex.py` (Playwright at 860 px and 2.5×; cap 700 px tall).
- **Review first:** charts go to an exhibit page for the user before Word.
- **Appendix exhibit candidates:** v1 Ex 24 (crane case), Ex 23 (India registrations), Ex 25 (Indonesia service footprint), Ex 17 (plant map), Ex 9 (Komatsu and Hitachi shares), Ex 26 (Thai categories), and B1 (Comtrade values, extended).

**Appendix plan:** see `v2/text/appendices-plan.html`, also printed in the draft. Each item names its source material in the v1 assembly source, the dossiers and the batch 3 research.

---

## 9. Word draft v2 and the Step 9 checks

**Pipeline** (from brief v3; scripts expect `build/` at `/home/claude/build` and `original-kit/` at `/home/claude/kit/kit`):
1. `parse.py`: point `SRC` at a concatenation of `v2/text/*.html` in paper order (exec, about, ch1–ch4, conclusion, appendices). The files already follow its conventions (h3, h4, `.inbrief`, `.exm`, `.case`, `.tw`, `sup`). One gap: the `.copy` paragraphs and `<section>` wrappers, which `parse.py` should treat as plain `p` and pass-through.
2. `edits.py` produces `doc_v2.json`.
3. `refs.py` and `refs_final.py`: renumber, merging N-numbers from `v2/tools/sources.py`.
4. `prep_model.py` produces `model.json`.
5. `bash build.sh <name> [toc.json]`.
6. `pages.py` reports pages; target 20 body pages.

**Format:**
- A4; house fonts (Palatino Linotype headings, Segoe UI body; mapped to TeX Gyre Pagella and Selawik via `fonts/fonts.conf`).
- Navy / YCP blue; running header; page tab; In-brief panels; case boxes; a real TOC field.
- The user said to ignore the house template's look for now.

**Step 9 checks:**
- Every number against its reference and its exhibit, in small batches.
- The benchmark checklist: `china-playbook-lessons-from-past-white-papers.md` §3.2 and `pdf-gap-fill-supplement.md` §5.
- The 20-page body count.
- A PDF text-layer diff against the source.
- A look at every exhibit page at full size.
- **An independent reviewer:** a separate agent that has not seen the work reads the whole draft cold.

---

## 10. Firm inputs still missing (keep the placeholders)

- The house disclaimer and legal entity.
- About YCP: a one-line description, office count and way of working.
- A contact email or page, and the office list.
- The publication month. Data are as of 28 Sep 2026, refreshed to 2 Oct 2026 for re-checked figures.
- Optional: the house .dotx template, logo and cover photo.
- Counsel's view on the crane-duty wording.

---

## 11. Technical notes

- **Network:** after the user changed the environment settings on 2 Oct, the shell reached UN Comtrade, WITS, HKEXnews, DGTR and most sites directly with `curl`.
  - Some sites still block automated reading: INAPROC renders by script; bisnis.com sits behind Cloudflare; Investing.com and electrive also block.
  - If a new session's network is restricted again, ask the user to allow those hosts (environment settings, then Network access).
- **UN Comtrade:** `https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=360&period=2025&partnerCode=0,156,392&cmdCode=847950&flowCode=M`
  - Monthly data: use `/C/M/` with `period=202510`.
  - One period per call; filter on `customsCode=='C00' && motCode==0 && partner2Code==0`.
  - Retry on empty responses (rate limit).
  - Reporters: India 699, Indonesia 360, Thailand 764, Malaysia 458, Vietnam 704 (no 2024–25 data).
  - Preview quantities are imputed, so never use them for unit values.
- **HKEXnews filings:**
  - Get the stock ID: `https://www1.hkexnews.hk/search/prefix.do?callback=callback&lang=EN&type=A&name=01882&market=SEHK` (Haitian = 13410).
  - List filings: `titleSearchServlet.do?...&stockId=13410&fromDate=YYYYMMDD&toDate=YYYYMMDD...`
- **Scanned PDFs** (for example the DGTR laser findings): `pdftoppm -r 150 -gray -png`, then `tesseract` (install with `apt-get install -y tesseract-ocr`; the container is reset between sessions).
- **Python:** `pip install beautifulsoup4 lxml python-docx`. LibreOffice failed to open files in this container, so the Word reading copy is built with python-docx; the house-styled Word file comes from `build/`.
- **Rebuild:**
  - review pages: `python3 v2/tools/review_page.py ch1 ch2 ch3 ch4`;
  - integrated draft: `python3 v2/tools/assemble_draft.py`.
- **Watch for:** WebFetch-style tools mis-scale Chinese figures (亿元 rendered as "billion"), so re-derive figures from the original numbers.
