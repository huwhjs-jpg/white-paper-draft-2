# China Playbook upgrade: handover brief v3

Written 2 October 2026, at the end of the third working chat (1–2 October 2026). **This brief is self-contained.** It folds in what matters from briefs v1 (29 Sep) and v2 (1 Oct), which are in the kit for reference only.

**Where things stand, in one paragraph.** The paper, *The China Playbook for Emerging Asia*, was rewritten and approved section by section (Steps 1–8), and Word draft v1 was built: 62 pages, body 46, 31 exhibits and 147 references. The user then asked for:
- a much shorter paper, with the chapters inside 20 pages;
- a dated timeline with turning points;
- extensions to mid-level industrial products and to robotics;
- substantial evidence behind every product group.

This chat ran a full evidence build: a UN Comtrade screen of 36 products, an 11-year series for 15 products, company filings, and two Indian trade-remedy cases. It rebuilt the outline around that evidence and then simplified it for non-expert readers. **The user has approved outline v5 (section 4).** The next chat should:
1. run a short evidence top-up (section 7);
2. write the paper in the v5 structure, Chapters 1 and 3 first, each shown next to the approved text (section 8);
3. rebuild the exhibits, build Word draft v2, and run the full Step 9 checks, including an independent reviewer (sections 9–10).

---

## 0. Files

| What | Where in the kit (`china-playbook-handover-kit-v3.zip`) |
|---|---|
| This brief | `HANDOVER-BRIEF-v3.md` |
| **Approved outline v5** | `outline/restructure-v5.html`. v4 is kept in the same folder for its fuller evidence-by-section tables. |
| **Evidence dossiers** (the depth behind Chapter 3) | `evidence/archetype-evidence-dossiers.md`; a rendered version is in `evidence/archetype-evidence.html` |
| **Evidence log with every source** and the trade data | `evidence/evidence-log-and-trade-data.md`. The raw pieces are also kept separately: `log.md`, `comtrade_screen.md` and `comtrade_series.md`. |
| Earlier research (1 Oct) | `research/evidence-upgrade-report-2026-10-01.md` |
| **Approved text** (the assembly source, v1 structure) | `original-kit/text/china-playbook-assembly-source.html` |
| Word draft v1 and its PDF | `draft/` |
| Build pipeline, data and 28 rendered exhibits | `build/` |
| Fact-check files and reference data | `research/*.json` |
| Fonts | `fonts/` |
| Exhibit source (built exhibits), pack data, step pages and scripts | `original-kit/` |
| Briefs v1 and v2 | `original-kit/HANDOVER-BRIEF.md`, `HANDOVER-BRIEF-v2.md` |
| Benchmark of 16 past YCP papers, and the house visual style | Not in the zip. They are the user's own Project files `china-playbook-lessons-from-past-white-papers.md` and `pdf-gap-fill-supplement.md`, and the user attaches them separately. |

**Published pages on the old account.** The outline page (https://claude.ai/artifact/9Qs4wZsjt6K6vtvYEYZySm) is shared by link. The evidence page and the exhibit chooser are private to the old account. Everything they contain is in the kit, so don't rely on the links.

---

## 1. The user's standing instructions (follow these throughout)

- **Free, publicly verifiable sources only.** No paid databases, surveys or interviews.
- **Write for a reader who is not an industry expert.** Use plain words, define each term once, keep acronyms in the glossary, and put no product codes in the text. Keep the structure simple and flowing.
- **Body length.** The chapters must fit in 20 pages; the executive summary, About this paper and appendices are excluded. Page allocation is to be "sorted later", so write to the word guide in section 8 and fit at the end.
- **Fix accuracy errors directly and log them.** Show the user first anything that would change a verdict, a learning or a headline number in the executive summary.
- **Work in batches,** and show each chapter side by side with the approved text.
- **Robotics stays a separate section** (3.3), integrated naturally after factory machines.
- **Ignore for now** the back-matter order, firm formatting and the house template's look.
- **Keep the governing thought, the six learning labels, the six reader types and the six failure modes exactly as approved** (section 3).
- **Firm-focused, not author-focused:** no author bios. Voice is "we" for judgements, never "you".
- **Style notes from the user's reactions:** they asked for "simpler, easier to understand, better flowing", and asked "simplify and elaborate" when a status update was too dense. So prefer short paragraphs, plain sentences and clear signposting.

---

## 2. Status

**Done**
- Steps 1–8: approved text for the 15 v1 chapters, plus front and back matter, in the assembly source.
- 11 decisions settled (brief v2 §1), including:
  - the built colour scheme (China blue #0B6FD9, Japan amber #C07A00);
  - six failure modes;
  - India's verdict is "structural";
  - the tunnel-boring-machine incentive is restored (ref 128);
  - signpost thresholds kept (Komatsu above 25% for two quarters; electric above 5% of excavator exports);
  - crane-duty wording flagged for counsel in two places.
- Word draft v1 built (`build/`), with FX at 28 Sep 2026 rates (brief v2 §2a).
- Fact-check: batch 2 of 3 is done (`research/check_2.json`: 37 ok, 4 partial, 3 unreachable). Batches 1 and 3 never ran; check surviving claims chapter by chapter instead.
- Evidence build (batch 2), outline v4, then the simplified outline v5, which is **approved**.

**Left**
1. Evidence top-up (section 7).
2. Write: Chapters 1 and 3 first, then 2 and 4, the conclusion, the executive summary, About this paper and the appendices (section 8).
3. Nine body exhibits plus the appendix set (section 9).
4. References renumbered, with about 40 new sources; Word draft v2; fit the body to 20 pages; Step 9 (section 10).
5. Firm inputs (section 11).

---

## 3. Locked items (unchanged)

- **Governing thought:** Chinese OEMs won share mainly by redesigning the commercial system around the machine, not by selling it cheaply, and most of their moves can be copied.
- **Central question (approved wording):** Which of the moves that won Chinese OEMs share can be copied, by whom and how fast, and which product categories will they reach next?
- **Qualifier added in Chapter 3:** in the next products the same moves arrive in a different order, and the buyer decides the order.
- **Six learnings (labels locked):**
  1. Enter through a narrow beachhead, then broaden.
  2. Treat customer credit as part of the product.
  3. Price just enough, then invest in the lifecycle.
  4. Localise plants, then export from the host.
  5. Turn local-content and investment rules into an advantage. Never write "FDI rules".
  6. Use electrification as the entry wedge.

  v5 groups them, without renaming them, as **Get in** (1, 6), **Win the sale** (2, 3) and **Stay** (4, 5).
- **Six reader types:** global incumbents; Indian and ASEAN champions; dealers; financiers; Chinese OEMs planning their next market; policymakers.
- **Six failure modes:**
  - Buyers return where uptime matters.
  - A loyal installed base holds.
  - High share invites trade cases.
  - Overseas acquisitions lose money.
  - Dealer networks outgrow parts supply.
  - Price wars at home drain cash.
- **Accuracy fixes F1–F13 stay applied** (brief v1 §3). The key ones:
  - **F1:** India's crane duties were recommended on 19 Sep 2025 but not imposed within the three months Rule 18(1) allows. Never write "pending".
  - **F2:** the 10% / 12.5% US tariffs come from the forced-labour Section 301 action, effective 24 Jul 2026.
  - **F6:** United Tractors' Jan–Aug 2026 figures: Komatsu 2,689 (−21%); large mining 436 (−49%).
  - **F8:** the combined Komatsu and Hitachi share is "indicative".
  - **F9:** parts and service is about 37% of United Tractors' machinery revenue, H1 2026.

---

## 4. The approved outline (v5)

Four plain questions, three kinds of buyer, one story. The full page is `outline/restructure-v5.html`.

**Three tools the reader learns once:**
1. **A three-stage timeline:**
   - *exporting the surplus*, to 2021;
   - *going overseas-first*, 2022–24 (SANY's overseas share went from 23% to 45.7% of revenue in 2022);
   - *owning the system*, from 2025 (plants, own finance companies, repair and parts).

   This replaces the old phase names Probe, Beachheads, Push and Embed. Don't use those names.
2. **One measure of progress:** the year China overtook Japan as the main supplier.

   | Product | Year China overtook Japan |
   |---|---|
   | Electric forklifts | 2017 |
   | Excavators | 2019 |
   | Other forklifts | 2019 |
   | Plastic-moulding (injection-moulding) machines | 2020 |
   | Robots | 2025 |
   | CNC lathes | 2025 |
   | Machining centres | Not yet (China 21%, Japan 45% in 2025) |
   | Compressors, pumps, laser machines, control panels | China already ahead in 2015 |

   These are import data, value-weighted, for India, Indonesia, Thailand and Malaysia.
3. **Three kinds of buyer:**
   - contractors and fleets buying through dealers (excavators, cranes, forklifts);
   - factories (plastic-moulding machines, machine tools, laser cutters, and robots);
   - plant engineers buying off the shelf through distributors (compressors, pumps, generators).

**Executive summary** (1 page, about 600 words):
- the governing thought;
- the shift in three numbers: Indonesian excavator imports from China 33% → 75%; Indian crane imports 35% → 93%; robots passed Japan in 2025;
- the structural verdict;
- the six learnings in one line each, grouped;
- the next categories in two lines;
- one line per reader.

**About this paper** (1 page): the reader map points to the four chapters and the appendix profiles. Scope: three kinds of buyer, five markets. Method in three sentences.

### Chapter 1. What happened?

*Answer:* In under a decade Chinese makers became the main suppliers of heavy equipment in India and Southeast Asia. The shift turned twice, and it is structural, not a commodity boom.

- **1.1 The size of the shift.** Three numbers (see above). Exhibit 1: where China gained, by country and product (the v1 heat map, 19 pairs, 2019 → 2024; add 2025 where it helps).
- **1.2 When it turned.**
  - China's home market collapsed after 2021, and overseas became the main business in 2022.
  - From 2025 Chinese makers began owning the whole system abroad.
  - The 2026 rule changes in India, Indonesia and the US get one paragraph here.
  - Exhibit 2: the timeline, using the CCMA domestic and export units 2016–H1 2026 and SANY's overseas share, with the two turns marked.
- **1.3 Not just a commodity boom.**
  - Komatsu lost share in Indonesia while the market grew and coal output hit records.
  - China also gained in products unrelated to mining.
  - Plain verdict: structural in India and Indonesia, and in four of five Thai categories.
  - The five tests move to the method appendix. The Indonesia brand chart becomes a sentence.
- **1.4 The open question.** Will share bought partly on easy credit survive the 2026–27 downturn? Evidence:
  - exports were +33.5% in H1 2026;
  - Indonesian mining work-plan (RKAB) approval delays, and lenders' caution;
  - payment delays in Indian road building.

### Chapter 2. How did they do it?

*Answer:* Not by being cheapest. They redesigned how the machine is sold, financed, serviced and made. Each move can be copied, and most are cheaper for incumbents to copy.

Each of the six learnings gets four short beats: what they did, one example, where it stops, and what others can copy. Group them in three pairs:

- **2.1 Get in.**
  - SANY India's long-reach excavator niche: 52% within about 18 months, then cranes, piling and port machinery through the same dealers.
  - Chinese forklift makers arrived as buyers switched to electric: China supplied 60–69% of electric-forklift imports in 2024.
  - Limit: Tata Hitachi won back mining-excavator share (from 20% to about 35%).
  - A single sentence on following Chinese customers abroad belongs here; the full story is in Chapter 3.
- **2.2 Win the sale.**
  - Credit: SANY's distributor and MNC Leasing signed an **MoU** in Dec 2017 (not a financing agreement); low-down-payment financing followed in 2018; a RMB1.45bn agreement in Sep 2025; and OJK licensed PT Sany Indonesia Finance on 14 Sep 2026 (decision KEP-56/D.06/2026). XCMG's ABC Multifinance joint venture launched in Sep 2026.
  - India's crane case: related importers got up to three years' credit. DGTR treats this as an export-price adjustment, so don't call it a cause of injury.
  - Price: Chinese cranes undercut Indian prices by only 0–10% (April 2023–March 2024), and asking prices sit inside incumbents' ranges.
  - Lifecycle: United Tractors' parts and service held at about 37%; XCMG's Balikpapan remanufacturing base.
  - Limit: credit-led share is exposed in a downturn.
  - Exhibit 3: SANY's finance story (from v1 Ex 14, with "MoU" corrected).
- **2.3 Stay.**
  - Four Chinese OEMs build in India.
  - New plants and service bases since Nov 2025 in Indonesia and Thailand: Heli Rayong, Hangcha Chonburi, LiuGong Karawang, XCMG Weda Bay ("XCMG's first overseas new-energy factory"), and XCMG Balikpapan remanufacturing.
  - Rules: Indonesia's TKDN 25% credit for investing locally (Permenperin 35/2025); India's Press Note 2 60-day track.
  - Limits: plants depend on trade policy, and announced plants are not always production. See Haitian (section 5).
  - Exhibit 4: the moves over time (v1 Ex 20, updated).

### Chapter 3. Where is it heading next?

*Answer:* Into the machines factories buy, because Chinese factories abroad bring Chinese machines with them, and then into robots. Equipment bought off the shelf through distributors moves more slowly, on price first. How a product is bought decides how long incumbents have.

- **3.1 How a product is bought sets the pace.** The three kinds of buyer, and where each product stands. Exhibit 5: where each product stands, showing the year China overtook Japan and which of the six moves are already visible.
- **3.2 Machines for factories follow Chinese factories.** This covers plastic-moulding machines, machine tools and laser cutters.
  - Haitian's own 2025 results credit Chinese manufacturers going abroad.
  - China's import share rose from 24% to 60% in ten years; Japan's fell from 38% to 16%.
  - Service and local plants follow fast.
  - So do trade duties: India taxed Chinese laser cutters in Dec 2023 and plastic-moulding machines in Jun 2025.
  - Exhibit 6: factory machines, China against Japan, 2015–2025, with India's duty dates.
- **3.3 Robots: the same path, one step behind.**
  - China became a net exporter of robots in 2025, and that year overtook Japan in all four markets with 2025 data.
  - Chinese robot makers' own businesses abroad are still small, so the share moves through hardware, installers and local partners. "Get in" has happened; "Win the sale" and "Stay" have not yet.
  - Warehouse robots are the exception (born global) and get one paragraph.
  - Exhibit 7: robots, China against Japan by country, 2019 and 2025.
- **3.4 Off-the-shelf equipment moves on price first.**
  - Compressors and pumps gain share through low-priced, often unbranded imports.
  - Chinese brands have little local presence yet.
  - Incumbents answer with cheaper second ranges: ELGi's 2026 range sells through a separate dealer network.
- **3.5 The window, and our view to 2030.**
  - For each kind of buyer: how far Chinese firms have got, what comes next, and how long incumbents have.
  - The approved "our view by category" table moves here, with rows added for factory machines and robots.
  - Note which moves do not travel: customer credit outside heavy equipment. It reappears only as subscription in warehouse robots.

### Chapter 4. What should you do about it?

*Answer:* The playbook has limits, and incumbents are already learning from it. Every reader has a first move, and five signs will show how fast the next products move.

- **4.1 Where the playbook breaks.** The six failure modes in one table, split two ways:
  - Where incumbents hold (2):
    - Tata Hitachi.
    - Thai excavators: Japan's share rose from 39.8% to 50.8% while China's stayed at about 36%. This is a sentence; the detail goes to Appendix A.
  - Where Chinese firms stumble (4):
    - Trade cases: cranes recommended but lapsed; lasers and plastic-moulding machines imposed; UK excavator duties; EU cases.
    - Efort's impairment and losses.
    - Neta's dealers outgrowing its parts supply.
    - Efort's "volume without revenue" price war.
- **4.2 Incumbents are already copying it.** Three responses:
  - **Cheaper second brands:** ELGi; United Tractors' second-tier line; Jungheinrich's AntOn, made for it by EP Equipment; Atlas Copco's Chinese brands Liutech and Bolaite.
  - **Trade duties pursued by incumbents with Indian plants:** Shibaura Machine India and Milacron India were among the petitioners.
  - **Retreat to premium:** Volvo's SDLG exit; Fanuc and Yaskawa building US plants.
- **4.3 Your first move.** One line for each of the six readers, with full lists in Appendix C. Exhibit 8: actions by reader (v1 Ex 29, simplified).
- **4.4 Five things to watch.** Exhibit 9 (v1 Ex 30, cut to five):
  - China's share of robot imports;
  - India's next trade-duty decisions on capital goods;
  - further maker-owned finance companies in Indonesia;
  - Komatsu's share (threshold: above 25% for two quarters);
  - the electric share of China's equipment exports (threshold: above 5% of excavator exports).

**Conclusion: a playbook open to every firm.** The approved argument, plus the window: how long incumbents have depends on who their buyers are.

**Appendices**
- **A. Country profiles:** India, Indonesia, and Thailand with Vietnam and Malaysia. The crane case, Komatsu's share series and the Thai counter-case go here.
- **B. Product profiles:** factory machines, robots, off-the-shelf equipment, and a short note on components (gearboxes, motors, hydraulics).
- **C. Actions in full,** and partner checks.
- **D. Method:** the five tests, evidence grades, how the timeline and the "overtook Japan" years are dated, data limits, FX.
- **E. Glossary.**
- **F. Trade data.**
- Then References and About YCP.

---

## 5. The evidence base: key facts and their sources

Full detail and URLs are in `evidence/archetype-evidence-dossiers.md` and `evidence/evidence-log-and-trade-data.md`. **Primary** marks filings, regulator records and customs notices.

**Trade data.** UN Comtrade public API, pulled 1 Oct 2026. It is validated against v1: Thai pumps 33.3% → 53.4%; Indian compressors 44.0% → 52.6%; Indonesian excavators 33.1% → 74.5%, US$590.6m → US$1,248.8m.

| Product | China's import share | Japan's import share | Basis |
|---|---|---|---|
| Plastic-moulding machines | 24% (2015) → 31% (2019) → 56% (2024) → 60% (2025) | 38% → 16% | Four markets |
| CNC lathes | 6% → 27% | 26% in 2025 | Four markets |
| Machining centres | 2% → 21% | 45% in 2025 | Four markets |
| Robots (HS 847950) | 22% (2019) → 42% (2025) | 36% → 27% | Four markets |
| Compressors | 33% → 48% | — | Four markets, 2015 → 2025 |
| Pumps | 28% → 53% | — | Four markets, 2015 → 2025 |
| Gearboxes | 29% → 52% | — | Four markets, 2015 → 2025 |
| Control panels (incl. PLC) | 26% → 44% | Japan 7% | Four markets, 2015 → 2025 |
| Large generator sets | 42% → 69% | — | Five markets, 2019 → 2024 |

- Robots in 2025, China against Japan: India 34% vs 30%; Indonesia 62% vs 12% (this jump is unexplained; see section 7); Thailand 44% vs 28%; Malaysia 40% vs 36%.
- Plastic-moulding machines by country: India 23% (2019) → 53% (2024) → 47% (2025, the year of the duty); Thailand 68% in 2025.
- Pumps in India stayed flat at 32–39%. Indian portable compressors went from 14% (2015) to 77% (2025). Malaysian large generator sets rose from 20% (2019) to 84% (2024).
- Hydraulic and industrial valves barely moved (9% → 12% and 30% → 34%), so they are excluded.

**Factory machines.**
- **Haitian.** 2025 revenue RMB17,733.2m, of which overseas RMB7,601.5m (42.8%), up 26.4%.
  - Its own statement: "在中国制造企业加快国际化布局的带动下" ("driven by Chinese manufacturers accelerating their international expansion"). Source: haitian.com/cn 2025 results (primary).
  - India subsidiary 2014; Kadi (Gujarat) plant opened 28 Apr 2018 (planned 1,800 machines a year); Vietnam plant (phase 2 in 2019); Indonesia subsidiary 2015.
  - **Caution (DGTR, primary):** Indian producers said Haitian "imported around 900 plastic processing machines in the period of investigation" and is "only a reseller and trader". Haitian gave no evidence of production, so it was not treated as a domestic producer (paras 47(l), 54).
- **Yizumi.** 2025 revenue RMB6,048m; overseas 29.90% (a record). Gujarat plant since 2017; 3,500 machines delivered by Sep 2025.
- **Bodor India.** Founded 2019. More than 2,000 machines in India, more than 150 local staff, a Mumbai repair centre, and a five-year warranty on core components (Aug 2024).
- **HSG.** US$10m India factory plan (Jan 2025); claims leadership in India.
- **DGTR case on plastic processing machines.**
  - Initiated 29 Mar 2024; final findings 27 Mar 2025; period of investigation Oct 2022–Sep 2023.
  - Applicants: Electronica, Milacron India, Shibaura Machine India and Windsor (57% of Indian production).
  - Subject imports rose from under 4% to 19% of Indian demand, according to the applicants. Dumping margins were 40–70%, with price suppression.
  - Duty (Notification 21/2025-Customs (ADD), 26 Jun 2025, five years):

    | Producer | Duty |
    |---|---|
    | Chen Hsong (China) | 27% |
    | Yizumi | 35% |
    | Fu Chun Shin | 48% |
    | Other Chinese producers | 63% |
    | Other Taiwanese producers | 53% |
    | Husky, Huarong | 0% |

- **Laser machines.** DGTR case initiated Oct 2022 (applicant: Sahajanand). Duty imposed by Notification 15/2023-Customs (ADD), 22 Dec 2023:

  | Producer | Duty |
  |---|---|
  | HSG | 22.54% |
  | Han's Laser | 24.66% |
  | Bystronic's China plants | 30.16% |
  | Yawei | 43.35% |
  | Bodor | 84.22% |
  | Oree | 87.30% |
  | Gweike | 90.49% |
  | TRUMPF China | Nil |
  | All others | 147.20% |

  Amendment 04/2026-Customs (ADD) of 8 Apr 2026 renamed Bystronic Shenzhen as DNE Laser.
- **Market context.** China's machine-tool exports were about US$8.2bn in 2024, passing Germany. They are "predominantly low-to-mid-end" (industry report, secondary). In H1 2026 China's machinery exports rose 20%; to India +26.5%, Vietnam +18.8% and ASEAN +19.5% (CMIF via AMT, 8 Sep 2026).

**Robots.**
- **China customs.** Industrial robot exports rose 48.7% in 2025 and exceeded imports for the first time. "Asia remains the primary market… key destinations including Vietnam, Thailand, and India" (GAC deputy administrator, 14 Jan 2026). H1 2026 exports were RMB6.29bn, up 18.6%, to 141 countries.
- **Estun** (HKEX annual results, primary). 2025 revenue RMB4,888.01m. Overseas RMB1,462.67m (+6.80%), against mainland +29.79%. The overseas share fell from 34.1% to 29.9%.
- **Inovance** (CNINFO annual report summary, primary). Revenue RMB45.10bn. Its robots "won top customers in markets such as Vietnam and Korea". Plants are being built in Hungary and Thailand; the Thai plant is for the EV business per an earlier check. The overseas share is about 6% (secondary source).
- **Efort.** RMB154.8m impairment on its overseas integration business; RMB497m loss.
- **Somboon Siasun Tech.** A Thai joint venture: Somboon Advance Technology 50.0003%, Siasun 49.9997%, THB30m capital. Somboon supplies Toyota, Honda, Mazda, Isuzu and Mitsubishi (NNA, 2020). Siasun describes a "5G smart factory" in the EEC (Mar 2025).
- **Thailand BOI, 23 Feb 2026.** Five Chinese humanoid-robot parts makers approved for more than THB10bn in Chachoengsao.
- **Fanuc** lost its top shipment position in China. Fanuc and Yaskawa are building US plants (Financial News, 30 Sep 2026).
- **IFR.** India installed about 10,500 robots in 2025 (+15%). The public data have no supplier split for ASEAN.
- **Warehouse robots and cobots.**
  - Geek+ H1 2026: more than 75% of revenue overseas; subscription orders up more than 75%.
  - Dobot: overseas 59.1% (2023) and 53.7% (2024).
  - Hai Robotics: Singapore headquarters for Southeast Asia.
  - No named deployments in India or ASEAN were found.

**Off-the-shelf equipment.**
- **Kaishan.** About 50% overseas, including geothermal. Its Indian unit sold about US$10m and 533 compressors in 2025, against roughly US$500m of compressor imports from China.
- **ELGi** (Q1 FY27 call, 14 Aug 2026): the low-cost tier is validated, first orders are in, and it launches in September in Hyderabad. "A separate distributor network was established for this tier". India aftermarket is 28–30% of revenue, against 15–16% globally.
- **Atlas Copco** bought Liutech (2002) and Bolaite (2006).
- **Leo Pump Indonesia** (about 12 distributors); Junhe's Thai plant and Taifu's Vietnamese plant, which are export-oriented.
- **Rules.** India's Omnibus machinery regulation was rescinded (S.O. 239(E), 14 Jan 2026). The Pumps QCO was published in draft on 13 May 2025; its final status is unconfirmed.

**Components** (appendix note only).
- Wolong: Asia-Pacific revenue outside China rose 45.56% in 2025; Vietnam plant (annual report, primary).
- Hengli: overseas over 35%; Mexico plant in full production in Q2 2026 (secondary).

**Timeline (CCMA units, domestic / export).**

| Year | Domestic | Export |
|---|---|---|
| 2016 | 62,993 | 7,327 |
| 2017 | 130,559 | 9,672 |
| 2018 | 184,190 | 19,100 |
| 2019 | 209,077 | 26,616 |
| 2020 | 292,864 | 34,741 |
| 2021 | — | 68,427 |
| 2023 | 89,980 | 105,038 |
| 2024 | — | 100,588 |
| 2025 | 118,518 | 116,739 |
| H1 2026 | — | 73,295 |

Exports were 7–11% of units from 2016 to 2020 and about half from 2023. SANY's overseas share: 23% (2021), 45.7% (2022), 63% (2025).

---

## 6. Corrections to carry into the rewrite (fix and log)

1. MNC Leasing and SANY Perkasa signed an MoU in Dec 2017. Source the description "SANY's distributor" or drop it.
2. Crane case: soften "the damage came from… long credit". DGTR treats the credit as a price adjustment.
3. SANY Chakan: write "more than INR 1,000 crore invested". The 1,200 machines exported is a company-level figure, not the plant's.
4. XCMG Weda Bay is "XCMG's first overseas new-energy factory".
5. Turning point 1 is 2022 at company level; 2023 is when exports passed home sales in units.
6. Chinese suppliers held 55% of China's robot market in 2025, **down** from 57%.
7. India rescinded the Omnibus Technical Regulation (S.O. 239(E), 14 Jan 2026). The hermetic-compressor QCO remains.
8. India compressors: the rise came mainly in 2024; 2025 was 49.3%.
9. Indonesian coal: "about 720 Mt" is the energy ministry's **projection** of 2026 output (Katadata, 10 Sep 2026), not a quota. Confirm the final RKAB total.
10. Highway pace: "25 km a day in FY26" is correct. The 21 km/day in the headline is the FY27 expectation (CareEdge, 25 Sep 2026).
11. Inovance: keep "about 6% overseas" labelled as a secondary source.
12. ELGi: label "25–30%" as a company estimate, not comparable with import shares.
13. Estun: cite the HKEX annual results instead of Sina.
14. HINABI citation (old ref 150): drop it if it supports nothing.
15. Haitian India: never present it as proof of local production without the DGTR caution.

---

## 7. Evidence top-up (do first; keep it short)

1. **Why Indonesia's robot imports went 62% Chinese in 2025.** Look for new Chinese-owned battery, nickel or EV plants, and check the Comtrade partner detail.
2. **Primary checks:** Haitian's HKEX 2025 annual report (overseas by region if disclosed); Hengli's 2025 annual report (overseas share); the DGTR laser final findings (Indian market share and import figures).
3. **India's Pumps QCO:** draft or final?
4. **Indonesia's final 2026 coal quota** (RKAB total).
5. **The unreachable v1 sources:** the asking-price pages (TractorJunction, Desimachines, INAPROC), the INAPROC TKDN listing and the GeM listing. Check them, or drop and soften the claims.
6. **Atlas Copco's Chinese brands:** are they sold in India or ASEAN?
7. **Optional:** a named warehouse-robot or cobot deployment in India or ASEAN.
8. **Optional:** one sentence on why Thai excavators held for Japan, if a public source explains it.

**Method notes:**
- **UN Comtrade** works through the user's Chrome (Claude in Chrome) from the page context: `fetch('https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=699&period=2024&partnerCode=0,156,392&cmdCode=847950&flowCode=M')`.
  - Only **one period per call.**
  - Keep each call under about 500 rows; split long code lists.
  - Filter rows on `customsCode=='C00' && motCode==0 && partner2Code==0`.
  - Reporter codes: India 699, Indonesia 360, Thailand 764, Vietnam 704 (no 2024–25 data), Malaysia 458. Partner codes: World 0, China 156, Japan 392, Germany 276, Korea 410, Taiwan ("Other Asia nes") 490.
  - **Preview quantities are imputed, so never use them for unit values.**
  - Save results via `localStorage`, because tab state is lost on restart.
  - Return small chunks: tool output truncates at about 1,500 characters, and strings containing "n=" can be blocked.
- **Other sources.** The workspace shell cannot reach most websites; use WebFetch, or read the page in Chrome. WebFetch can hit a session limit; Chrome's `get_page_text` works for many pages it can't fetch.
- **Scaling trap.** WebFetch often mis-scales Chinese figures (亿元 rendered as "billion"). Re-derive figures from the original numbers.

---

## 8. Writing plan (batch 3)

**Order:** Chapter 1 → Chapter 3 → (user review) → Chapter 2 → Chapter 4 → Conclusion → Executive summary → About this paper → Appendices A–F.

**For each chapter, deliver a review page** with three parts:
- the new text;
- beside it, the approved v1 text it came from (cite v1 chapter and section), so the user can see what was kept, cut or moved;
- a fix log listing what was corrected, with the source.

Publish each as a page the user can open (an artifact), and save it to the Project.

**Word guide.** About 7,000 body words in total; fit to 20 pages at the end.

| Section | Words | Exhibits |
|---|---|---|
| Chapter 1 | about 900 | 2 |
| Chapter 2 | about 2,200 | 2 |
| Chapter 3 | about 2,000 | 3 |
| Chapter 4 | about 1,500 | 2 |
| Conclusion | about 300 | — |

Capacity check from v1: a full text page holds 610–680 words; half-page exhibits; four chapter breaks.

**Style:**
- Plain English for non-experts. Short paragraphs. Claim headlines. One idea per paragraph.
- Each fact told once; refer back instead of repeating.
- Define "OEM" once as "equipment maker"; "Chinese makers" is fine in running text.
- No product codes in the text. Acronyms go to the glossary: TKDN, RKAB, DGTR, OJK, QCO, BIS, PLC, AMR.
- Label company claims, competitors' claims and our own calculations.
- Use dated facts with "as of" where they move.
- Use the recurring cast so readers can follow: SANY, Haitian, ELGi, Tata Hitachi, United Tractors / Komatsu.

**References.**
- Renumber by first citation, starting from `build/data/refs_final.json` (147 refs) and the mapping in `build/refs.py` and `build/refs_final.py`.
- Add the new batch 2 sources from the evidence log (about 40).
- Drop references no longer cited.
- Give every entry a "Used for" note.
- Exhibit source lines use the same numbers.

---

## 9. Exhibits (9 in the body)

The colour scheme is fixed: China blue #0B6FD9 and Japan amber #C07A00 (dark-mode pair #3383E0 / #B97A12). Charts go to an exhibit page for the user to review before they go into Word.

| No. | Exhibit | Built from |
|---|---|---|
| 1 | Where China gained, by country and product, 2019 → 2024 | v1 Ex 7 / pack heat map (`build/ex/ex07.png`, `pack_ex.py`) |
| 2 | The timeline: home vs export units 2016–H1 2026, SANY's overseas share, two turns | New; v1 Ex 5 as a base (`built-03`) |
| 3 | SANY's finance story in Indonesia | v1 Ex 14 (`ex14.png`; source in `original-kit/exhibit-source/all.json`); fix "MoU" |
| 4 | The moves over time | v1 Ex 20 (`ex20.png`); add the 2025–26 moves |
| 5 | Where each product stands: the year China overtook Japan, and which moves are visible | New, from `comtrade_series.md` and the dossier grades |
| 6 | Factory machines: China vs Japan, 2015–2025, with India's duty dates | New, from `comtrade_series.md` |
| 7 | Robots: China vs Japan by country, 2019 and 2025 | New, from `comtrade_series.md` and section 5 |
| 8 | Actions by reader | v1 Ex 29 (`ex29.png`), simplified |
| 9 | What to watch (five), with thresholds | v1 Ex 30 (`ex30.png`), cut to five |

**Appendix candidates:**
- India's crane-case panels (v1 Ex 24);
- India registrations (Ex 23);
- Indonesia's service footprint (Ex 25);
- the plant map (Ex 17);
- Komatsu and Hitachi shares (Ex 9);
- the Thai counter-case (Ex 26);
- the Comtrade values table (B1, extended).

**Rendering.** Run `python3 build/render_ex.py`, which builds from `original-kit/exhibit-source/all.json` and `css.json` plus `pack_ex.py`. Playwright renders at 860 px and 2.5×; cap image height at 700 px.

---

## 10. Build Word draft v2 and the Step 9 checks

**Pipeline** (paths are absolute; see section 12):
1. `parse.py` turns the assembly source into `doc_v1.json`.
2. `edits.py` produces `doc_v2.json`.
3. `refs.py` and `refs_final.py` handle references.
4. `prep_model.py` produces `model.json`.
5. `bash build.sh <name> [toc.json]` runs `build_docx.js`, then `post.py`, then the LibreOffice PDF render.
6. `pages.py` reports section pages and writes `toc.json` for the second pass.

**For v2 the content source changes.** Parse the new chapter texts, not the v1 assembly source. The simplest route is to write the new chapters into the same HTML conventions as the assembly source (h3 chapter, h4 sections, `.inbrief`, `.case`, `.exm` exhibit markers, `sup` citations) and reuse `parse.py`. Otherwise, extend `prep_model.py`.

**Format:** A4; house fonts (Palatino Linotype headings, Segoe UI body); navy / YCP blue; running header; page tab with "ycp.com"; In-brief panels; case boxes; failure-mode blocks; action lists with horizon chips; a real TOC field. The user said to ignore template aesthetics for now, so reuse v1 styling as it stands.

**Step 9 checks:**
- every number against its reference and its exhibit (run in small batches);
- the benchmark checklist (`china-playbook-lessons-from-past-white-papers.md` §3.2, plus `pdf-gap-fill-supplement.md` §5);
- the 20-page body count;
- a PDF text-layer diff against the source;
- a look at every exhibit page at full size;
- **an independent reviewer**: a separate agent that has not seen the work reads the whole draft cold.

---

## 11. Firm inputs still missing (keep the yellow placeholders)

- House disclaimer and legal entity.
- About YCP facts: one-line description, office count, way of working.
- Contact email or page.
- Office list.
- Publication month (data as of 28 Sep 2026; extend to the top-up date where figures are refreshed).
- Optional: house .dotx template, logo, cover photo.
- Counsel's view on the crane-duty wording.

---

## 12. Technical notes

- **Unpack** `build/` to `/home/claude/build` and `original-kit/` to `/home/claude/kit/kit`. The scripts use those absolute paths.
- **Fonts:** copy `fonts/*.ttf` to `~/.fonts` and `fonts/fonts.conf` to `~/.config/fontconfig/fonts.conf`, then run `fc-cache -f`. This maps Palatino to TeX Gyre Pagella and Segoe UI to Selawik.
- **Node:** docx and playwright may be installed globally (check `npm ls -g`). Run `npm install` in `build/` for `@fontsource/ibm-plex-mono`. Chromium is at `/opt/pw-browsers`; don't run `playwright install`.
- **Gotchas:**
  - docx-js spacing needs `lineRule:'auto'`.
  - `post.py` strips `w:highlightCs`.
  - Avoid empty spacer paragraphs after lists.
  - Cap exhibit images at 700 px tall.
- **Network:** the shell is allowlisted (package registries and GitHub). Websites and data APIs go through WebFetch or the user's Chrome.
- **Fact-check runs:** use small batches, because large batches hit usage limits before.
