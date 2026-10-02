# Lessons from YCP's Past White Papers for *The China Playbook for Emerging Asia*

**Scope:** every white paper in this repository, read in full; per-paper extraction (Step 1), cross-paper synthesis (Step 2), and application to the China Playbook draft (Step 3).
**Prepared:** 28 September 2026. **Updated:** 28 September 2026, after checking every page of the 16 source PDFs. The evidence behind each correction is in the companion document `analysis/pdf-gap-fill-supplement.md`.

---

## Read this first: what was reviewed and what could not be read

**There are 16 papers in the repository, not 15.** All 16 are analysed below. One of them, *System Integration in the Generative AI Era* (P16), is a joint paper by NTT DATA INTELLILINK, YCP and AI Brain Partners rather than a YCP-only publication. If your count of 15 excluded it, you can set it aside. I still rank it highly because its evidence method fits your paper closely.

**How references work.** "P1" to "P16" refer to the papers as listed in the comparison table in Step 1. Page numbers are the printed page numbers, which equal the PDF page numbers in all 16 files. P16 is numbered too (pp2–28), so it is now cited by page like the others. Quotes are exact, including the original spelling.

**How the source files were checked.** The first version of this analysis worked from Markdown conversions of the designed PDFs. This version has been checked against the PDFs themselves: every page was rendered and inspected, and the PDF text layer was compared with the Markdown. As a result:

- **Charts, maps, photos, colour and layout** are now covered. Section 3 of the supplement describes the house visual identity (palette, typography, page template, exhibit styling) and recounts the exhibits.
- **Every gap flagged in the first version has been resolved.** Some were conversion artefacts; others hid genuine faults, or new ones. The table below summarises what changed.
- **Hidden text layers.** Three PDFs carry text that is invisible in print but present in the text layer (P11, P13, P7). This produced three of the "production errors" the first version reported. They are real file-hygiene defects, because any copy-paste or extraction picks them up, but they are not visible on the page.

| File | What the Markdown showed | What the PDF shows |
|---|---|---|
| P14 *Japan's Capital Markets* | CJK glyphs on pp23, 42, 47; chart axes as stray numbers | Clean text. Passages recovered (e.g. GPs citing multiple expansion fell "from 69% … to just 24%", p42). Author titles resolved: Katano is Managing Partner, Group Officer, Co-Head of Management Services; Matsuoka is Managing Partner, Japan Regional CEO (p48). |
| P16 *System Integration in the GenAI Era* | No page numbers; empty TOC; five empty "Implication" boxes | Pages numbered 2–28; full TOC on p2; all five Implication boxes have text (pp12, 13, 14, 16, 17). |
| P11 *Powering Successful Digital Transformation* | P8's conclusion interleaved into pp17–18 | The printed conclusion is clean. P8's text sits in **hidden white text frames** behind the artwork, so this is a template leftover, not a visible error. |
| P1 *Strategic Pathways* | Exec summary sentence split; risk cube as labels; photos unreadable | Exec summary intact (two columns). Risk cube = Policy / Macro / Execution faces × Impact → Likelihood → Time (p49). Photos are decorative skylines. The RAG scale on p51 is text only, not colour. |
| P10 *Unlocking India's Nuclear Sector* | pp43 and 48 graphics garbled | p43 maps six challenge clusters to six named mechanisms (DSSA, design certification, process qualification plus GST zero-rating / heavy-water leasing / "Nuclear PLI", catastrophe bonds, fuel and material banks, community equity). p48 splits participants into "Lead Project Adopters & Operators" and "Delivery, Supply, and Financial Enablers". |
| P5 *SEA IPO Landscape* | Table 1 scores missing | Harvey-ball scores recovered (p6). **The final verdicts cannot be reproduced from them**, whichever way the criteria are read. Table 5 has **no** empty rows: it has one merged cell. |
| P7 *India's Logistics Industry* | p42 markers and pp50–51 table missing | Archetype × segment map, M&A heat map (p49) and 5 × 4 pitfalls grid all recovered. The "duplicated paragraph" on p35 is hidden-layer only. |
| P13 *Sustainability Governance* | p16 percentages unmapped | Embedded 31%, Standalone ESG Committee 20%, Layered 10%, Distributed 10%, Individual Board Advocate 15%, Ad Hoc 12% (total 98%). The p15 "garbled header" is P4's title in hidden white text. |
| P3 *Transportation Economy* | Operator names missing from Figure 4 (p32) | The names were logos: AAI 110 airports, GMR 4, Adani 7, Fairfax 1, Zurich 1. They conflict with the text ("three" GMR airports, "six" Adani airports). |
| P2 *Indonesia's Oil and Gas* | Conclusion bullets out of order (p17) | Clean two-column page. |
| P15 *Source-to-Pay* | Services graphic garbled (p23) | Five service boxes recovered. "7085%" was an artefact: the PDF reads "70-85%". |

---

# STEP 1 — Extraction from each paper

## 1.0 Side-by-side comparison

Papers are listed by publication date. "Words" is the body text excluding the office-address list; it still includes author bios and appendices.

| # | Paper (short title) | Date | Printed pp | ≈ Words | Authors | Exec summary | Headline style | Exhibit numbering | Sourcing | Cases | Actions by reader type | Firm pitch | Relevance to China Playbook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Strategic Pathways for Industrial MNCs in Emerging Asian Growth Corridors | Dec 2025 | 58 | 12,300 | 4 | 1p prose, no numbers | Mixed; country nicknames | Figures 1–3, then stops | Inline names; 1 source line; no reference list | 3 company + 1 client + ~12 one-liners | No (MNCs only) | Moderate | **Very high** (same countries, compressors, pumps, localisation rules) |
| P2 | Advancing Indonesia's Oil and Gas Sector | Dec 2025 | 20 | 4,100 | 4 | 2p prose, no numbers | Topic-led | None | Some source lines; inline "(SKK Migas, 2023)" | None | **Yes** (industry, government, investor) | None | Medium (Indonesia policy) |
| P3 | Transportation Economy: How Mobility Shapes Urban Development in Japan, China and India | Feb 2026 | 45 | 10,200 | 4 | 1p prose, no numbers | Topic-led | Tables 1–8, Figures 1–9 (duplicate numbers) | Source line on most exhibits | Delhi Aerocity + named deals | Partly | None | Medium (country-chapter template; China entry paths) |
| P4 | From Strategy to Execution: Change Management | Mar 2026 | 25 | 5,100 | 1 | ~1.5p prose + section previews | Topic-led | Figures 1–2 | Sources bundled at section ends | 7 client vignettes in a table | No | Heavy | Low |
| P5 | Southeast Asia IPO Landscape | Mar 2026 | 22 | 4,800 | 2 + 7 contributors | ~1.5p prose + numbered pillars | Topic-led | **Tables 1–6, Figures 1–3 (consistent)** | Few; "YCP Research & Analysis" | 2 anonymised public + 1 client | No | Medium | Medium (country table; readiness framework) |
| P6 | Resilience by Design: Nearshoring, Friend-Shoring and Regional Supply Networks | Apr 2026 | 44 | 10,800 | 5 | ~1.5p prose + pillars + 5 steps | Topic-led | None | Mostly unattributed statistics | Many short, 3 anonymised | No | Light | Medium (China+1; Thailand) |
| P7 | India's Logistics Industry: Mapping Growth and Value Creation Pathways | May 2026 | 59 | 12,400 | 5 | ~2p, **quantified, ends with actions by player type** | **Claim-led** | None | Sources appendix grouped by type; few source lines | ~10 named deals | **Yes** (incumbents, new entrants, international players) | Light CTA | **High** (India; archetypes; maturity model) |
| P8 | The Operational Transformation Analysis Approach | May 2026 | 23 | 5,200 | 1 | ~1.5p roadmap | Topic-led | Figure 1 only | Bundled; journal side boxes | None | No | Heavy | Low |
| P9 | Global Operations in an Era of Structural Recalibration | Jun 2026 | 15 | 2,900 | 2 | 1p prose | Mixed | None | Thin | None | No | None | Medium (China outward investment) |
| P10 | Unlocking India's Nuclear Sector: Commercial Opportunities Created by the SHANTI Act | Jun 2026 | 52 | 12,600 | 4 | 3p, quantified, **ends on the central question** | Mixed; coined labels | None | Statute sections; few source lines incl. "YCP Internal" | 5 country cases + named firms | **Yes** (participant archetypes + policymakers) | Invitation only | **High** (policy-shift logic; mitigations; archetypes) |
| P11 | Powering Successful Digital Transformation | Jul 2026 | 25 | 5,300 | 1 | 1p prose + stat bullets | Topic-led | None | **Numbered superscripts + reference list** (includes blogs) | 1 client case | No | Heavy | Low (failure-mode format) |
| P12 | Creativity in the Age of AI Algorithms | Jul 2026 | 26 | 5,700 | 3 | **None** (thesis stated in opening) | **Claim-led** (Why/How chapters) | None | **Source line on almost every exhibit** | None | No | Heavy | Medium (country profile format; SEA comparator table) |
| P13 | Building Sustainability Governance Frameworks for Performance | Jul 2026 | 41 | 8,100 | 1 | 1p, **answer-first** | Mixed | None | Light; one client-data exhibit | None | Partly (board vs management) | Light | **High** (failure-mode and trigger template) |
| P14 | Japan's Capital Markets: Structural Transformation and a New Value Creation Ecosystem | Aug 2026 | 48 | ~13,200 | 2 | 5p, quantified, hook fact | **Claim-led**, metaphor system | None | **Most precise source notes in the set** | Named public deals; Fuji Soft case | Partly (executives, investors) | None | High (structural-shift argument; exhibit captions) |
| P15 | The Next Era of Source-to-Pay | Aug 2026 | 42 | 7,800 | 4 | 1p, numbers-heavy | Topic-led | None | Unnumbered reference list, not linked to claims | 6 client cases | No (CPO/CFO/COO) | **Heaviest** | Low |
| P16 | System Integration in the Generative AI Era (joint paper) | Sep 2026 | 28 | 6,400 | 5 (3 firms) | **"Key Findings" list + implications** | **Claim + verdict** | None | **28 numbered sources, each noting the figure used** | Short, cited | No | None | **High** (hypothesis-and-verdict method; horizon-based "contests") |

**Legend.** *Claim-led*: most section headlines state a conclusion. *Topic-led*: most name a subject. *Firm pitch*: None → Light (bios, About page, one line) → Moderate → Heavy (multi-page capability sections).

**Exhibit counts** in the per-paper sections below were recounted from the PDF page renders. The first version's estimates, made from the Markdown, were low for most long papers. See the supplement, §3.3.

---

## P1 · Strategic Pathways for Industrial MNCs in Emerging Asian Growth Corridors

1. **Basics.** December 2025. Printed pages run to 58: body pp3–51, appendices pp52–55, authors pp56–57, offices p58. About 12,300 words. Authors (pp56–57): Pavan Madamsetty (Partner), Akarsh Varma (Manager), Rohit Jain (Senior Analyst), Vibhuti Roach (Junior Associate). The reader is not stated; it is implied to be industrial-goods MNCs and "business decision‑makers" (p8).
2. **Central question and governing thought.** *Central question (inferred):* where and how should industrial MNCs enter India and the ASEAN‑5 to win from the infrastructure build-out? *Governing thought (inferred from pp3, 8):* the build-out is funded and time-bound; the winners verify budgeted demand, qualify under localisation rules, match channels to deal economics and scale their footprint in stages.
3. **Structure.** Exec summary (p3) → "The Macro Case" (pp4–8) → "Country Attractiveness Framework" (pp9–12) → "Market Deep Dives", six countries at about 3pp each (pp13–31) → "Playing to Win" playbook with cases (pp32–45) → "Recommendations and Risks" (pp46–51) → Appendices (abbreviations; scoring rubric). *Opens* with the claim of a "once-in-a-generation growth platform" (p3) and a GI Hub USD 94tn vs USD 79tn investment-gap exhibit (p5). *Closes* on the risk matrix and "resilience must be designed in, not bolted on" (p51). There is no conclusion section.
4. **Executive summary.** One page, about 350 words, four prose paragraphs, no numbers, no bullets. Findings are phrased as behaviours of winners: "They verify that demand is budgeted, not merely announced." (p3)
5. **Headlines.** Mixed. Claims: "Global infrastructure is bigger than ever, and it’s heading to Asia." (p5); "Defending champions are slowing down" (p8); country taglines such as "Indonesia: Localization fortress (3.50/5)" (p11). Topics: "Looking at Asia" (p7); "Market Deep Dives" (p13). Figure titles are topic labels, e.g. "Figure 2: Growth in value of infra-assets managed by funds globally" (p6).
6. **Evidence.**
   - Public sources are named in the text (IMF, World Bank PPI, UNCTAD, JETRO, Oxford Economics, Preqin, Moody's).
   - Only one exhibit has a source line ("Source: Preqin (2025)", p6), and there is no reference list.
   - About 12 company examples are unsourced.
   - Firm experience appears only in the anonymised "YCP in Action" case (pp44–45). There is no survey or interview data.
   - The country chapters are data-dense; the playbook is mostly opinion plus examples.
7. **Exhibits.**
   - **Count and types:** about 45 (recounted from the PDF), including 30 panels repeated across the six country chapters. Types:
     - weighted pillar table (p10) and attractiveness matrix (p11);
     - a scorecard strip at the top of each country chapter;
     - "What works and what doesn't" Strengths/Risks panels;
     - "Opportunity window" tables (Program | Scale and scope | Timeline and business context);
     - a delivery-model decision tree (p37) and a route-to-customer table (p39);
     - case templates (Prize in sight / Edge to capture / Gameplan to deliver);
     - a risk cube (p49), a High/Medium/Low risk matrix with Red/Amber/Green time margins (p51; the RAG thresholds are written in words and the cells are not coloured), and a 1–5 scoring rubric (pp54–55).
   - **Layout:** each country chapter opens with a decorative skyline photo, then a one-row scorecard strip. A navy "Why now?" band carries the country tagline: India "The broad frontier growth engine"; Indonesia "The localization fortress"; Vietnam "The export sweet spot"; Thailand "Final boarding for incentive express"; Malaysia "Logistics and energy transformation underway"; Philippines "Catching the infrastructure crest". Numbering stops at Figure 3 (p6).
   - **Risk cube (p49):** three faces (Policy / Macro / Execution Risks) × three "Evaluative Parameters" (Impact → Likelihood → Time), introduced as "macro weather fronts, policy crosswinds, and execution stalls".
   - **Most effective:**
     - *The Attractiveness Matrix plus the A2 rubric* makes the ranking auditable (weights and 1–5 bands are shown).
     - *The Opportunity window tables* turn a pipeline into dated tender windows a sales head can act on.
     - *The risk matrix* adds "time margin" to likelihood and impact, which turns risks into a calendar.
8. **Frameworks and tools.**
   - A 7-pillar Country Selection Framework weighted 20/20/15/15/10/10/10, with "z score" scoring logic (p10) and a rubric (A2).
   - A market viability test (Market Access Mechanics / Advantage Window / Execution Elasticity), with four questions each (p33), applied to Atlas Copco (p34).
   - A Product–Market Fit "Decision Lens" (p35) and a value-proposition trio ("Start With the 'Money Map'", "Reduce Operational Anxiety, Not Just Cost", "Turn Compliance into Currency", p36).
   - A delivery-model tree with a "Filter:" question per entry mode (pp37–38), a three-filter channel test (p39), and the risk cube (pp49–51).
9. **Case studies.**
   - **Company cases:** Atlas Copco in Thailand (1p, p34), Daikin in India (pp40–41), Schneider Electric in Vietnam (pp42–43).
   - **Client case:** an anonymised YCP engagement (pp44–45).
   - **One-liners:** about 12 "Case in play" and "Example" items, e.g. GF Piping's "42% TKDN score" (p36).
   - Cases are introduced under labels ("Entry Viability in Action", "Playbook in Action") and serve to show that the frameworks work. None is sourced.
10. **Actions for readers.** Nine recommendations under four headings (pp47–48). Each is a bold imperative, an anonymised mini-case, and a rule, e.g. "Anchor ambition to funded demand, not press releases … Ground ambitions in budget that is already parked, and your forecasts will hold." (p47). There is one reader type and almost no timeframes; the exception is "Install a policy radar that scans twice a year" (p48).
11. **Tone and voice.** Confident and promotional, sometimes in the second person ("Where you should look", p8). Urgency is repeated in every "Why now?" box, and there is little hedging. *Representative:* "This is not a speculative opportunity: it is an execution-driven market operating on a defined timetable." (p16)
12. **Firm positioning.** Moderate: a two-page "YCP in Action" case (pp44–45), four bios and an office list. There is no call to action.
13. **Weaknesses.**
    - **Contradictory incentive figures:** India's PLI schemes "refund 10–18% of incremental revenue" (p14), but "Four PLI schemes reimburse up to 1% of incremental sales" (p15).
    - **Mismatched base figure:** "nearly 16% of the expected infrastructure investment of USD 79 trillion in Asia and the Middle East" (p8) applies the global figure to Asia and the Middle East, which is shown as USD 46tn on p6.
    - **Scoring method described two ways:** z-scores (p10) versus rubric bands (A2).
    - **Competition scored backwards:** "Very intense competition … crowded marketplace" scores 5 (p55) and so raises attractiveness.
    - **Typo in rubric:** "CPI 40-30" (p55).
    - **Stale timing:** advice to "localize … by early 2025" (p19) in a December 2025 paper.
    - **Urgency clichés:** "The longer you wait, the less advantageous it will be." (p22)
    - **Sourcing:** no reference list, and company cases are unsourced.

## P2 · Advancing Indonesia's Oil and Gas Sector: Pathways to Resilience and Sustainable Growth

1. **Basics.** December 2025. Printed pages run to 20 (body pp3–17). About 4,100 words. Authors (pp18–19): Septian Waluyan (Partner), Yan Arthur Johanes (Director), Nabila Ailsa (Associate), Kara Carolluna (Analyst). The reader is implied: government, operators and investors (the conclusion addresses all three, p17).
2. **Central question and governing thought.** *Central question (inferred):* what must Indonesia change to attract capital and close its oil-and-gas supply gap? *Governing thought (inferred):* barriers across the value chain are interconnected and need five coordinated reforms, from contracts to a competitiveness council.
3. **Structure.** Exec summary (pp3–4) → Overview (pp5–8) → Structural Barriers (pp9–11) → Global Investor Priorities (pp12–13) → five numbered Strategic Imperatives (pp14–16) → Conclusion (p17). *Opens* with President Prabowo's two energy ambitions (p3). *Closes* on the sector pivoting "from a heritage of challenges to a future marked by resilience, sustainability, and global competitiveness" (p17).
4. **Executive summary.** Two pages, about 400 words, five prose paragraphs. It describes what Indonesia is doing rather than what the paper finds, and has no numbers. It ends with a roadmap sentence ("This white paper outlines the data-driven context, urgent challenges, and actionable imperatives…", p4).
5. **Headlines.** Mostly topics ("Overview: Indonesia’s Oil and Gas Sector", p5). Sub-heads are part claim: "Upstream Challenges: Aging Reserves and Financing Complexity" (p9). The chart labels are claims: "Domestic crude lifting remains suboptimal" and "Intake volumes and refinery output continue to decline" (p8; they appear as numbered call-outs 1 and 2 on the flow chart).
6. **Evidence.**
   - Government statistics, SKK Migas, IEA and Indonesian press (Kontan, Bisnis Indonesia).
   - Stat tiles carry bold inline citations such as "(SKK Migas, 2023)" and "(IEA, 2022)" (p11).
   - The international precedents (Saudi Aramco and BlackRock, TotalEnergies, Norway's 78% deduction, Brazil) are unsourced (pp12–13).
   - There is no firm data and no reference list.
7. **Exhibits.**
   - **Count and types:** about 7, all unnumbered: a twin chart of GDP contribution and energy mix (p6); a value-chain schematic with investment bars (p7); a supply–demand flow in KBPD marked "Illustrative", with numbered call-outs (p8); a "Summary of Structural Barriers" table (p11); six stat tiles, each with its own citation (p11).
   - **Source lines** are italic "_Source: …_" below the exhibit.
   - **Colour:** the house blues throughout; red is used once, for the "Critical Gap" on the p8 flow, which is a disciplined alert colour.
   - **Most effective:**
     - *The supply–demand flow* makes the gap concrete ("Domestic crude lifting (~500 KBPD) meets only ~60% of refinery demand (~850 KBPD)", p8).
     - *The stat tiles* show one fact, one source, one tile.
8. **Frameworks and tools.** The upstream/midstream/downstream value chain is the organising spine. An "investor priorities" lens has five criteria (pp12–13).
9. **Case studies.** None. International examples get one or two sentences each.
10. **Actions for readers.** Five numbered imperatives, "01" to "05" (pp14–16). Each has a problem line, three named proposals (e.g. "National Energy Investment Fast-Track Program", "Oil and Gas Decarbonization Fund") and an outcome line. The conclusion assigns roles to **Industry / Government / Investor** (p17). This is reader-type segmentation.
11. **Tone and voice.** A formal policy register built on "must", with no "we" and many adjectives. *Representative:* "Capital investment is the lifeblood of transformation. However, regulatory delays elevate project risk and deter investment." (p10)
12. **Firm positioning.** None beyond bios and offices.
13. **Weaknesses.**
    - **Contradiction on midstream use:** utilisation "averaging at 94%" (p9), yet the summary table lists "Underutilization" (p11).
    - **Garbled figure (printed in the PDF, not a conversion error):** "Nelson Complexity Index is -5 (below regional peers in 9-10)" (p11).
    - **Refining placed in two stages:** the text defines "Midstream (transportation, refining, and processing)" (p6), but the value-chain graphic puts Refining under Downstream only (p7).
    - **Council named two ways:** "Oil and Gas Competitiveness Council" (p16) vs "Central Energy Competitiveness Council" (p17).
    - **Stale target:** "a competitive global energy hub by 2025 and beyond" (p4) in a December 2025 paper.
    - **Sourcing:** "Source: American Fuel and Petrochemical Manufacturers" (p7) is attached to Indonesian investment data.
    - **Thin evidence** behind the recommendations.

## P3 · Transportation Economy: How Mobility Shapes Urban Development in Japan, China, and India

1. **Basics.** February 2026. Printed pages run to 45 (body pp3–42). About 10,200 words. Authors (pp43–44): Masa Matsuoka (Managing Partner, Japan Regional Manager), Pooja Yadav (Manager, YCP India), Gaurav Rathore (Manager, YCP India), Weizhi Fu (Director, YCP China). The reader is "business professionals" (p3), with foreign firms and brands also addressed.
2. **Central question and governing thought.** *Central question (inferred):* how have Japan, China and India built different transport-led urban models, and where are the openings for business? *Governing thought (stated, p3):* the three countries developed distinct models — station-centred Japan, metro/HSR-led China, airport-centred India — which create exportable models and partnership openings (p42).
3. **Structure.** Exec summary (p3) → Introduction (pp4–7) → Japan (pp8–13, about 6pp) → China (pp14–26, about 13pp) → India (pp27–41, about 15pp) → Conclusion (p42). Each country chapter ends with "Business Opportunities and International Implications" (pp12, 23, 38). *Opens* with the Homo sapiens "Great Journey", the Crusades and the Silk Road (p4). *Closes* with "Two broad categories of opportunity" (p42).
4. **Executive summary.** One page, about 280 words, four prose paragraphs. It gives one line per country model, then a roadmap. There are no numbers and no findings list.
5. **Headlines.** Mostly topics ("Japan", "Overview of China’s Urban Rail Transit Landscape", p14). Some claims: "Airports: India's Unique Success" (p29); "Metros: Rapid Scale, Strong Impact, and the Need to Reset Financial Sustainability" (p40).
6. **Evidence.**
   - Ministry of Transport (PRC), China Association of Metro, AAI, CEIC, Knight Frank, Propstack, and "YCP Research & Analysis" (Tables 1 and 7; Figures 3 and 6).
   - The source lines are specific, e.g. Table 2 ends "compiled by YCP." (p6).
   - Some claims are unsourced ("Industry analyses indicate…", p10). There is no reference list.
7. **Exhibits.**
   - **Count and numbering:** about 27. Tables 1–8 and Figures 1–9 are numbered (17 in all), but Figure 3 (pp31, 33) and Figure 4 (pp32, 34) each appear twice, and Figure 6 precedes Figure 5 (p35). Titles sit above each exhibit; source lines sit in the left margin beside it, under a short blue rule.
   - **Figure 4 (p32), major airport operators:** the operator names are logos (AAI, GMR, Adani, Fairfax, Zurich Airport), with airports operated (110 / 4 / 7 / 1 / 1), passengers and years of presence. Because the names are logos, text extraction loses them.
   - **Most effective:**
     - *"Table 6. TOD Project Lifecycle: Stakeholder Roles & Responsibilities"* (p22), five stakeholder groups × three phases, shows who does what and when.
     - *The China three-phase panel* (p17), with rows Model / Driver / Constraint / Implication and a separate "Implication (Foreign)" row.
     - *The non-aeronautical revenue per passenger benchmark* (p34), which places Indian airports against global hubs.
8. **Frameworks and tools.** Three national archetypes; China's three TOD eras; a TOD lifecycle (Planning & Construction → Operation → Transformation & Expansion); "Two Potential Entry Paths for Foreign Companies" (Path A: support services; Path B: commercial operations) (p23).
9. **Case studies.** A two-page Delhi Aerocity case (pp36–37: rentals, 7–8% yields vs 3–6%, 3,800 rooms at 75% occupancy). Named deal examples include SP Group's energy-performance contract (p24), the ORIX–Chengdu Metro MOU (p25) and Perennial's hospital at Guangzhou Baiyun (p26).
10. **Actions for readers.** Opportunity sections per country. The conclusion names two categories (exporting development models; partnerships between transport operators and consumer businesses, p42). Audiences are implied rather than listed.
11. **Tone and voice.** Descriptive and historical; uses "We outline key monetization themes" (p38). *Representative:* "In this sense, India lies ahead of Japan in opening airport operations to the private sector." (p11)
12. **Firm positioning.** None beyond author bios.
13. **Weaknesses.**
    - **Contradiction on facing pages:** Penn Station has 294,000 daily passengers in Table 2 (p6) but 600,000 in Table 3 and the text (pp6–7).
    - **Duplicate figure numbers.**
    - **Scope drift:** the paper "examines the relationship between migration and consumption" (p5).
    - **Uneven chapters,** and the Japan chapter has no data exhibit.
    - **No cross-country synthesis exhibit.**
    - **Typos,** e.g. "Passanger" (three times: Table 4 headers, p16; Figure 4 title, p34) and "lays concentrated" (p11).
    - **Text vs figure:** GMR has "three major international airports" in the text but 4 airports in Figure 4 (p32); Adani has "six brownfield airports" in the text but 7 in the figure. Noida is shown as "to be operational in 2025" in a February 2026 paper.

## P4 · From Strategy to Execution: Change Management as the Engine of Operational Transformation (YCP Renoir)

1. **Basics.** March 2026. Printed pages run to 25. About 5,100 words. Single author: Leon Van Hout, CEO Europe, YCP Renoir (p25). The reader is leaders running transformation programmes (implied).
2. **Central question and governing thought.** *Central question (inferred):* why do transformations fail to stick? *Governing thought (stated, p23):* "Change sticks when it is owned by people, reinforced by leaders, measured through performance management systems, and embedded into daily work."
3. **Structure.** Exec summary (pp3–4) → why transformation breaks down (pp5–6) → five principles (pp7–9) → framework (pp10–11) → leadership (pp12–13) → change champions (pp14–15) → versatility (p16) → "Our Approach to Implementation" (pp17–22) → Conclusion (p23). *Opens* with "nearly 70% of change initiatives fail" (p5). *Closes* with the bold maxim above and a soft invitation (p23).
4. **Executive summary.** About 400 words: one dense paragraph, then "Specifically, this white paper explores the following:" and five section previews (p4). It is a roadmap with no numbers.
5. **Headlines.** Topics ("Leadership", "Insufficient Resources"). Some are descriptive claims: "Leadership Commitment and Alignment: A Continuous Enabler to Maintain and Reinforce Change" (p12).
6. **Evidence.** Sources are bundled at the end of sections ("_Source(s): Harvard DCE Professional & Executive Development, Springer Link, MDPI_", p6). The "70%" figure is not linked to a specific source. The firm's client results table (pp20–22) is the strongest evidence.
7. **Exhibits.**
   - **Count and types:** about 7: "Figure 1: The Eight Stages of Implementation" (p10; a nested staircase of Procedural (Awareness, Development, Installation), Behavioral (Compliance, Understanding, Usage) and Cultural (Implementation, Sustainability) change); "Figure 2: The 3-Phase Proprietary Process…" (p18); a client results table (Region | Client Need | What We Did | Results | Client Quote) (pp20–22); a client quote from a "Leading bank in Thailand" (p19).
   - **Most effective:** *the results table* runs need → action → quantified result → quote, e.g. "USD 2 million in annualized cost savings" and "↓94% reduction in overdue critical work" (p20).
8. **Frameworks and tools.**
   - Five principles.
   - Three levers with time-to-effect estimates: procedural "a few weeks to several months", behavioural "several months", cultural "one to three years" (p11). This is a useful device for separating fast from slow change.
   - Change-champion selection criteria (p14).
   - Three organisational contexts (p16).
9. **Case studies.** Seven anonymised client vignettes in the results table (North America, South America, Europe, three in Asia, Middle East; 1–2 lines each). They show that the method works across regions.
10. **Actions for readers.** Principles and framework steps; one reader type.
11. **Tone and voice.** Formal, with some unclear phrasing ("seldom with serious impacts on their day-to-day struggles", p5). *Representative:* "Organizational transformation rarely fails due to a lack of ambition or strategy. More often, it falters at the point where new ideas must be translated into everyday behaviors, routines, and decisions." (p23)
12. **Firm positioning.** Heavy: six pages on the firm's approach, including the proprietary "Focus Process®" and the "MAT Governance Model" (p19), plus the client table and an About Us page.
13. **Weaknesses.**
    - **Principle labels change:** the exec summary lists "people, ownership, co-development, performance, and sustainability" (p4), but the body uses different names (pp7–9).
    - **Used before defined:** the "Eight Stages of Implementation" are referenced on p6 but defined on p10.
    - **Undefined acronym:** "MAT" is never defined.
    - **Ambiguous result:** "↑ 21% purchase order delivery lead time" (p20).
    - **Incomplete table:** five of the seven "Client Quote" cells are empty (pp20–22), and two vignettes (Europe; the first Asia row) report no quantified result.
    - **Weak sourcing:** "70%" has no specific source, and "MPDI" is a typo (p11).

## P5 · Southeast Asia IPO Landscape: Building Readiness for Long-Term Success

1. **Basics.** March 2026. Printed pages run to 22. About 4,800 words. Authors (p21): Karambir Anand (Managing Partner and SEA Regional Manager) and Dhendy Rizki Fadhillah (Partner). A separate "Contributors" page (p22) lists seven managers, analysts and associates; this is the only paper that credits a contributor team. The reader is SEA founders and management teams weighing an IPO (implied).
2. **Central question and governing thought.** *Central question (inferred):* is an IPO the right route, and what does readiness require? *Governing thought (stated, p4):* readiness rests on four pillars, and companies "that treat the IPO as an enterprise-wide transformation, rather than a one-time transaction, are best positioned to succeed".
3. **Structure.** Exec summary (pp3–4) → Introduction and funding-option comparison (pp5–6) → Country overview (pp7–10) → Four pillars and two cases (pp11–14) → PMO (pp15–19) → Conclusion (p20).
4. **Executive summary.** About 480 words: prose plus four numbered pillars, each with a bold label and a one-line definition, plus a paragraph on YCP's support. There are no numbers.
5. **Headlines.** Topics ("Current Overview: SEA IPO Landscape (2015 – 2025)", p7). Sub-heads are part claim: "Financial Strength: A Resilient Foundation for Public Markets" (p12). Each country row in Table 2 has a claim line: "Malaysia has the highest IPO volume growth, with a 10-year CAGR of 14.7%" (p8).
6. **Evidence.** Light. Table 1 is sourced "YCP Research & Analysis" (p6). A data note says "2025 data is year-to-date through November 2025 (partial year)" (p7), and a footnote explains that the sector outlook is based on national master plans (p10). Country statistics are otherwise unsourced, and there is no reference list.
7. **Exhibits.**
   - **Count and numbering:** 9, and this is **the only paper with fully consistent numbering**: Tables 1–6 and Figures 1–3.
   - **Most effective:**
     - *"Figure 2. The Four Pillars of IPO Readiness"* (p11) ties every readiness factor to a metric and to a consequence code: R = regulatory/disclosure risk, V = valuation/investor-confidence risk, T = timeline/execution risk.
     - *"Table 2. Country Comparison"* (pp8–10) puts one claim line per country above its levers and sectors.
     - *"Figure 3. IPO Preparation Process…"* (p17) gives phase durations in weeks.
8. **Frameworks and tools.** Funding options scored on four criteria with Harvey balls (Table 1, p6: Very low / Low / Moderate / High; the weights for the "weighted composite" are not disclosed); four readiness pillars; the PMO role and structure (Tables 3–4); a 9–12-month timeline.
9. **Case studies.**
   - **"Equity Story and Value Creation"** (p13): an unnamed but recognisable company ("from USD 47 billion to below USD 10 billion"), diagnosed pillar by pillar.
   - **"Strategic Listing Beyond Borders"** (p14): an unnamed Philippines-based firm listing on SGX.
   - **A YCP client case** (p19).
   - All three use the paper's own four-pillar lens, which is a strong device.
10. **Actions for readers.** For companies: start early, build the four pillars, and treat the listing venue as a strategic choice (p20). One reader type.
11. **Tone and voice.** Formal and clear; "we compare the four funding options" (p6). *Representative:* "IPO success is not determined by market timing alone. Public market investors increasingly focus on discipline, transparency, and execution certainty." (p3)
12. **Firm positioning.** Medium: a pitch paragraph in the exec summary (p4), then pp17–19 on YCP's PMO role and the YCP case.
13. **Weaknesses.**
    - **Chart not discussed:** Figure 1 is never narrated in the text.
    - **Undisclosed weights** in Table 1.
    - **Unsourced case:** the recognisable public case is anonymised and carries no source.
    - **Verdicts that cannot be reproduced** (Table 1, p6). M&A scores Moderate / High / High / Low but gets a "Low" verdict, below Bank Loan (Low / Moderate / Very low / Moderate → "Moderate"), even though it beats Bank Loan on three of four criteria. IPO (High / Moderate / Moderate / Low) gets "High". The criterion direction is not stated either (is a "High" cost of capital good or bad?). The intro sentence also drops a word: "from least favorable most favorable".
    - **Self-contradiction:** the Singapore row says both "Reducing standard board-lot sizes (proposed)" and "Increasing board-lot size…" (p8).
    - **Thin conclusion,** with no numbers.

## P6 · Resilience by Design: A Strategic Playbook for Nearshoring, Friend-Shoring, and Regional Supply Networks

1. **Basics.** April 2026. Printed pages run to 44. About 10,800 words. Authors (pp41–43): Saurabh Mehta (Managing Partner, Supply Chain Solutions Division CEO) and four Directors (Tiago Bonetto, Deepak Karnani, Pankaj Vivek, Prashant Giri), with emails. The reader is supply-chain and procurement leaders (implied).
2. **Central question and governing thought.** *Central question (inferred):* how should firms redesign supply networks for a fragmented world? *Governing thought (stated, p40):* "resilience is not built in the moment of crisis; it is designed long before it."
3. **Structure.** Exec summary (pp3–4) → why resilience matters (pp5–7) → framework (pp8–10) → nearshoring, reshoring and friend-shoring (pp11–19) → globalisation (p20) → local supply systems (pp21–26) → policy (World Bank study, pp27–30) → global implications (pp31–33) → future (pp34–38) → Conclusion (pp39–40).
4. **Executive summary.** About 330 words: one prose paragraph, then "Strategic Pillars" (three bullets) and "A Five-Step Implementation Guide" (Diagnostic / Redesign / Digitize / Partner / Monitor). It closes: "Resilience is not a defensive stance; it is a tactical advantage." (p4). There are no numbers.
5. **Headlines.** Mostly topics ("Nearshoring: Regionalizing Production", p11). Some claims: "Regional networks outperform global networks in environments with systemic volatility." (p26); "Friend-Shoring (No Evidence)" (p28).
6. **Evidence.** Several statistics are unattributed: "Recent industry surveys show that more than 80%…" and "exceeds 45% of a year’s EBITDA" (p5); "A 2022 survey found that 64% of CEOs" (p32); "Recent research shows 73% of firms" (p35). One World Bank study is summarised over four pages (pp27–30). There is no reference list, no source lines and no firm data.
7. **Exhibits.** Minimal (about 8 counting flag-icon country lists, example boxes and a Foxconn pull quote, p12): one table of "five major macro-trends by 2035" (p38) and no charts. The rest is repeated Benefits/Risks bullet lists, country lists and photos. There is no standout exhibit.
8. **Frameworks and tools.**
   - Resilience by Design pillars, each with "Key Actions" (pp8–10).
   - "From Total Cost of Ownership (TCO) to Total Cost of Risk (TCR)" (p6).
   - Four regional network archetypes, e.g. "Make Where You Sell" (p24).
   - "Resilience Capital" components (p36).
9. **Case studies.** Two-to-four-sentence cases (TSMC, Toyota, Apple, Cisco). Two longer ones: Foxconn in Guadalajara (pp12–13, including a direct quote from Foxconn) and Intel in Ohio (pp15–16). Three anonymised "Example" cases give Intervention / Results (pp24–25) and are unsourced.
10. **Actions for readers.** "Strategic Imperatives for Leaders" (p26) and "The Leadership Imperative" (p37). These are generic and address one reader type.
11. **Tone and voice.** Formal and aphoristic, with occasional "we" ("We are entering the era of Resilience by Design", p4). *Representative:* "Networks do not diversify themselves. Suppliers are not resilient by default. Contracts do not automatically mitigate risk." (p39)
12. **Firm positioning.** Light: an About Us page (p44) and bios. One bio says "Before joining Consus", which appears to be a legacy firm name (p41).
13. **Weaknesses.**
    - **Framework counts disagree:** three pillars in the exec summary (p4) vs "four pillars" (p8); a five-step guide (p4) vs a four-phase framework (p10).
    - **Misplaced paragraph:** a nearshoring paragraph sits inside the reshoring section (p14).
    - **Odd phrasing** that reads like a paraphraser: "initiative-taking approach" (p8), "Optimism in Design" (p9).
    - **Unsourced statistics.**
    - **Lopsided coverage:** heavy on US policy for an Asia-focused firm; almost no exhibits.
    - **Cross-paper tension:** Thailand is called an EV hub "for non-Chinese investors" (p18), while P1 highlights "Chinese OEMs led by BYD" in Rayong (P1, p24).

## P7 · India's Logistics Industry: Mapping Growth and Value Creation Pathways

1. **Basics.** May 2026. Printed pages run to 59. About 12,400 words. Authors (pp57–58): Jatin Gulati (Managing Partner, Practice Leader of Management Services Division), Kadam Aggarwal (Partner), Harish Mouli (Director), Shubhangi Jasoriya (Manager), Revanth Chetluru (Team Lead), with emails and prior employers. **The reader is stated** (p3): "strategic investors, financial sponsors, infrastructure developers, logistics operators, and global entrants evaluating India as a growth market."
2. **Central question and governing thought.** *Central question (stated as section titles):* what makes the market compelling, where are the opportunities, and how are different players capturing value? *Governing thought (stated, p5):* "the defining success factor will be strategic clarity".
3. **Structure.** A separate Introduction (p3) → Exec summary (pp4–5) → Market Attractiveness (pp6–32, about 27pp) → Key Opportunities (pp33–40) → Value Capture Strategies (pp41–52) → Conclusion (p53) → Appendix: abbreviations and sources (pp54–56). Every section ends with a "Key Takeaways" page (pp32, 40, 52) and a signpost to the next section.
4. **Executive summary.** About 480 words: prose plus two bullet sets. **Quantified** ("~10% annually between 2024 and 2030, outperforming the ~8% global growth rate", p4; Grade A stock "from ~238 million sq ft today to ~620 million sq ft by 2030", p5). It **ends with actions by player type**: "Incumbent players must seek clarity on their areas of play… Domestic new entrants should pursue selective, adjacency-led expansion, while international players must align their India strategy with broader portfolio objectives" (p5).
5. **Headlines.** **Claims** above almost every page: "India: The fastest-growing major economy globally" (p6); "India’s high dependence on road freight contributes to elevated logistics costs" (p28); "From the investment activities of various archetypes, two key routes emerge: PPP & M&A" (p45). Chart titles stay descriptive with units ("India’s GDP Growth Trajectory (2022–2030P)", p6).
6. **Evidence.**
   - IMF WEO (April 2026), RBI, World Bank LPI, Economic Survey, PIB, NITI Aayog, Knight Frank, JLL, BCG and CEIC.
   - "Appendix - Sources" (p56) groups sources by type but does not link them to specific claims.
   - The evidence base is stated in the introduction: "a synthesis of in-house expertise, client engagements, industry discussions, and ongoing market analysis" (p3).
   - Few exhibits carry source lines; one example is p17 ("Source: Trade Intelligence and Analytics (TIA) Portal | Department of Commerce").
7. **Exhibits.**
   - **Count:** about 45, unnumbered (about 20 charts, 3 maps, about 12 tables and matrices, and about 10 navy "claim banners" tagged with "Categories getting impacted" icons).
   - **Repeating page templates:** constraint pages use Context / Implications / Government & Industry Response (pp26–31); opportunity pages use facts plus a bold "Opportunity:" line (pp33–39).
   - **Most effective:**
     - *The logistics maturity matrix* (p10): four dimensions × five stages (Foundational → Intelligent Ecosystem), mapped to eras.
     - *The PPP risk matrix* (pp46–47): PPP type × lifecycle stage (Demand & Revenue / Value & Return Sensitivity / Bid Strategy / Post-Bid Governance), which works as a ready-made diligence checklist.
     - *The port turnaround benchmark* (p30): Malaysia 12, Singapore 18, Japan 24, India 53 hours.
     - *The M&A attractiveness heat map* (p49): acquirer type (global logistics cos / domestic logistics cos / financial players) × target ownership type, colour-coded green / yellow / pink (High / Medium / Low), each cell with a one-line rationale. Only one cell is Low: domestic acquirers of conglomerate logistics arms ("targets tend to be well-funded").
     - *The M&A pitfalls grid* (pp50–51): five target types × four diligence areas (Market & Competitor; Customer; Leadership & Talent; Value Creation). Each area opens with a "what to check" band, then pitfalls by type, e.g. "Market position inflated by captive group volumes" (conglomerate arms), "TAM frequently overstated" (venture-backed).
8. **Frameworks and tools.** A four-segment value chain; the maturity model; six player archetypes with named companies (p41); an archetype × segment presence map (p42; Primary / Secondary / Limited / None in four shades of blue, e.g. Infrastructure Developers are Primary in transportation infrastructure; PE-Led Platforms are Primary in distribution infrastructure); PPP-vs-M&A route logic ("The choice of route is fundamentally shaped by the structural nature of the underlying asset", p45); an M&A lens by target ownership type with a High/Medium/Low heat map (pp48–51).
9. **Case studies.** About 10 named deals in structured rows (Players / Asset & Type / Investment Type / Rationale), e.g. Allcargo–Gati and Delhivery–Ecom Express (pp43–44). They are short and serve to evidence the patterns of each archetype.
10. **Actions for readers.** **Organised by player type** in the exec summary (p5) and conclusion (p53). The PPP and M&A tables are the most specific actions in the paper.
11. **Tone and voice.** Analytical and bullet-dense, like a slide deck; uses "we" ("We have defined an integrated risk and value framework", p46). *Representative:* "Success in the next phase for players operating in different parts of the value chain will depend on clarity of positioning – where to play across core and adjacent segments, and how each move contributes to a defined value creation thesis." (p53)
12. **Firm positioning.** Light and specific: "We welcome the opportunity to discuss how these insights apply to your organization and share perspectives from our experience in bid advisory and buy- and sell-side M&A." (p53). On p59, the About Us text describes the wrong division (Supply Chain), and the running header visibly shows P4's title.
13. **Weaknesses.**
    - **Inconsistent numbers:** growth of ~10% (pp4, 13) vs "~9% CAGR" (p12); truck distance of "300 kilometers per day" (p28) vs 287 in the chart; LPI customs score of 3.2 (p31) vs ~3.1 (p25); ULIP integrating "34" systems (p24) vs "35+" (p31).
    - **Abbreviation clash:** PLI stands for both Peripheral Logistics Infrastructure and Production Linked Incentive (appendix #25 and #36).
    - **Wrong gloss:** "ESD" is defined as "Extended Storage Deposit" (p55).
    - **Unlabelled chart:** the Grade A warehousing stack (p35: 60 + 28, 148 + 90, 360 + 260) has no legend for its two segments. (The "duplicated paragraph" reported in the first version exists only in the hidden text layer.)
    - **Category drift across consecutive exhibits:** target ownership types number five on p48, four on p49 and five on pp50–51, and they are named differently each time.
    - **Imbalance:** attractiveness gets 27 pages; the conclusion gets 1.

## P8 · The Operational Transformation Analysis Approach: Revealing Performance Gaps Across the Value Chain (YCP Renoir)

1. **Basics.** May 2026. Printed pages run to 23. About 5,200 words. Single author: Daniel Menezes, Partner (p23). The reader is generic leadership.
2. **Central question and governing thought.** *Central question (inferred):* why does value leak across the value chain, and how do you find it? *Governing thought (inferred from p20):* value leakage is systemic, so observation-based diagnosis across five pillars reveals and quantifies it.
3. **Structure.** Exec summary (pp3–4) → breakdowns (pp5–7) → framework (pp8–11) → industries (pp12–14) → insight to impact (pp15–17) → YCP Renoir division (pp18–19) → Conclusion (pp20–21). Each section opens with a firm-voice pull quote, e.g. "What you can’t see across your value chain is often what costs you the most." (p5)
4. **Executive summary.** About 330 words. It previews sections ("Specifically, this white paper explores:"), is a roadmap and has no numbers.
5. **Headlines.** Descriptive topics ("Core Pillars of the Operational Transformation Analysis Framework", p9); few claims.
6. **Evidence.** Eurostat, MuleSoft and HBR, bundled at the end of a section ("_Source(s): Eurostat, 2025 Connectivity Benchmark Report by MuleSoft from Salesforce, Harvard Business Review, YCP Renoir_", p7). Journal side boxes (e.g. "_Source: ScienceDirect, Economic Letters, Volume 247, February 2025_", p15). Firm outcome ranges on p19 ("+5–15%" revenue, "≥3:1" ROI) have no stated basis.
7. **Exhibits.** About 6. "Figure 1: The Operational Excellence Journey…" (p8) is the only numbered exhibit. It runs STRATEGY → journey → RESULTS, with four "Core Technical Enablers" (Processes, System, Structure, Competencies) over four "Core Tactical Approach" steps (Awareness → Buy-In → Adoption → Ownership). **Most effective:** *the industry table* (Industries | Common Performance Gaps | Diagnostic Tools, pp12–13), which is concrete per sector, e.g. a corrective vs preventive maintenance ratio review for oil and gas.
8. **Frameworks and tools.** Five pillars (MCS, Processes, Organisation, Digital, People) and a four-step analysis (Discovery → Deep Dive → Opportunity Identification → Case for Change) (pp10–11).
9. **Case studies.** None.
10. **Actions for readers.** Framework steps only.
11. **Tone and voice.** Formal, abstract and repetitive. *Representative:* "Most performance breakdowns occur at functional interfaces, where structural ambiguity leads to misalignment, delayed decisions, and fragmented execution." (p9)
12. **Firm positioning.** Heavy: a two-page division profile, outcome claims, and a bold final call to action: "For organizations seeking structured clarity on value creation, risk exposure, and priority actions, YCP Renoir applies this analysis approach…" (p21).
13. **Weaknesses.**
    - **Reads as a methodology brochure,** with no cases or data.
    - **Unsupported outcome ranges.**
    - **Name drift:** "Operational Excellence Analysis Approach" (pp12, 16).
    - **Undefined acronym:** "OXD" (p18).
    - **Figure vs text:** Figure 1's four enablers do not match the five pillars in the text (MCS, Processes, Organisation, Digital, People).
    - **Shared text:** one sentence is identical in P4 (p6 here, P4 p5), and this paper's whole conclusion sits, as hidden white text, behind P11's conclusion pages (P11 pp17–18). That suggests P11 was built from this file.

## P9 · Global Operations in an Era of Structural Recalibration

1. **Basics.** June 2026. Printed pages run to 15 (the shortest paper). About 2,900 words. Authors (p15): Pilar Dieter (Managing Partner, Group Officer, Americas and EU Regional CEO) and Angelina Peng (Director, Shanghai). The reader is multinationals and "global operators" (implied).
2. **Central question and governing thought.** *Central question (inferred):* how are capital, trade and AI infrastructure realigning? *Governing thought (stated, p3):* "success in 2026 won’t come from isolated initiatives. Capital strategy, regional positioning, technology, and infrastructure need to work in lockstep."
3. **Structure.** Exec summary (p3) → three themes: Asia as capital exporter (pp4–7), trade reordering (pp8–11), AI infrastructure (pp12–13). Each ends with a "Strategic Implications of …" subsection. Conclusion (p14).
4. **Executive summary.** About 170 words, four short paragraphs, no numbers.
5. **Headlines.** Mixed: "Asia’s Rise as a Global Capital Exporter" (p4); "U.S. Market: Concentrated Growth in a Narrow Set" (p9). Implications are phrased as claims: "Capital Allocation Reflects Industrial Strategy" (p7).
6. **Evidence.** Thin. UNCTAD (USD 605bn, 40%), outward FDI stocks, RCEP ~30% of GDP. Many claims are unquantified ("data centers already account for a notable share", p13). One source line: "Source(s): APEC Economic Trends Report; APEC Policy Support Unit" (p9).
7. **Exhibits.** 3: a Japan vs China table by dimension (Capital Role / Investment Orientation / Sector Emphasis / Strategic Objective / Global Positioning) (p6); a "China-APEC Trade Volume" chart (p9); a table comparing US-centred trade with regional blocs (p10). **Most effective:** *the Japan vs China dimension table*, a compact and neutral comparison of two national playbooks.
8. **Frameworks and tools.** Comparison tables only.
9. **Case studies.** None.
10. **Actions for readers.** None concrete.
11. **Tone and voice.** Measured and heavily hedged ("may", "increasingly"). *Representative:* "Rather than signaling deglobalization, current trade patterns reflect a reconfiguration of global integration across overlapping regional systems." (p11)
12. **Firm positioning.** None.
13. **Weaknesses.**
    - **Thin and unsourced.**
    - **Loosely linked themes.**
    - **Exhibit under the wrong heading:** the China–APEC trade chart (p9; USD 2.4tn in 2016 to 3.8tn in 2025E) sits under "U.S. Market: Concentrated Growth in a Narrow Set".
    - **Repetitive conclusion:** paragraphs 4–5 repeat the infrastructure point (p14).
    - **No actions.**

## P10 · Unlocking India's Nuclear Sector: Commercial Opportunities Created by the SHANTI Act

1. **Basics.** June 2026. Printed pages run to 52. About 12,600 words. Authors (pp51–52): Ashish Sharma (Managing Partner, Group Officer, India Regional CEO), Ankit Hoshing (Partner), Sarthak Gupta (Team Lead), Aashish Tripathy (Analyst). The reader is private capital, industrial participants and policymakers ("dialogue—between industry, finance, and policy", p50).
2. **Central question and governing thought.** **Both are stated.**
   - *Central question:* "The central question is no longer whether the private sector will participate in India’s nuclear expansion, but how, and under what institutional architecture, that participation will take shape." (p5)
   - *Governing thought:* "A third engine—private capital—is therefore no longer a policy preference; it is an arithmetic necessity." (p18), backed by run-rate arithmetic of "~130 MW per year over 70 years versus a required run rate of ~4,000 MW per year" (p18).
3. **Structure.** Exec summary (pp3–5) → Ch1 Landscape (pp6–18) → Ch2 Privatisation and the SHANTI Act (pp19–28) → Ch3 Global Lessons (pp29–35) → Ch4 Challenges and Mitigations (pp36–43) → Ch5 Opportunities (pp44–49) → Conclusion (p50). The transitions are explicit, e.g. "With the enabling ecosystem now defined and the path to bankability cleared, the focus shifts to the scale of value creation." (p43)
4. **Executive summary.** Three pages, about 900 words. Narrative and **quantified** (≈9 GW today; 100 GW by 2047; INR 20 lakh crore, about USD 210bn). It embeds two exhibits (a 1947–2047 timeline and an A–G opportunity wheel) and ends on the central question. There is no numbered findings list.
5. **Headlines.** Chapter titles are topics. Case headlines carry the lesson ("United Kingdom: Privatization, Market Failure, and Revenue Support", p32). Challenges get **memorable coined labels**: "The Fuel Cycle Trap" (p41), "The “Hot Zone” Insurance Gap" (p40), "Tariff Determination Dilemma" (p38).
6. **Evidence.**
   - CEA roadmap, IEA, and **statutes cited by section** (e.g. Section 17(b) of the 2010 Act, p25; Sections 2(9), 37 and 8(4) of SHANTI, pp37–40).
   - Source lines include firm analysis: "Sources: Academic Research, PRS India, IISD, BNEF, CEA, YCP Internal" (p11).
   - There is an FX note: "~USD 210 billion at the time of preparing this report" (p3).
   - No reference list.
7. **Exhibits.**
   - **Count:** about 18, unnumbered: timeline (p4); total-cost stacked bar with the call-out "Least total cost for firm power" (p11; the call-out sits beside the nuclear bar); a six-technology × ten-attribute table (pp13–16); "Quantified Requirements" tables for financial, natural and human resources by 2037 and 2047 (pp20–21); "Impact of SHANTI Act - Before and After" (p28); "Framework for Private Nuclear Investment" (p35); a participant segmentation graphic (p48: "Lead Project Adopters & Operators" (energy majors and IPPs; hard-to-abate industrials) vs "Delivery, Supply, and Financial Enablers" (EPC; specialised manufacturers; financial institutions)); and "Bridging the Nuclear Capacity Gap" (p43).
   - **Most effective:**
     - *The Before/After table*: six rows, each changing one thing.
     - *The Framework table:* its "Lessons From" column ties every principle to a country case (Canada, UK, Japan, Germany, USA).
     - *The total-cost chart,* whose call-out states the conclusion on the chart itself.
     - *"Bridging the Nuclear Capacity Gap"* (p43): one page that runs from "LAW (SHANTI Act)" to "ENERGY REALITY (Functional Market)", with one column per challenge cluster, its named fix and its effect. Examples: DSSA as a "liability firewall to protect foreign reactor IP"; design certification "to compress licensing from years to months"; GST zero-rating, heavy-water leasing and a "Nuclear PLI" of 4–6%; catastrophe bonds for the "Hot Zone" insurance gap. It is the best single-page summary of a problem → fix chapter in the set.
8. **Frameworks and tools.**
   - Six constraints that justify privatisation.
   - The six-pillar investment framework (p35).
   - **A challenge → named mitigation pattern** across six clusters (Ch4, pp37–42, summarised on p43). Examples: a DSSA modelled on AECL (p37), a HAM transitional tariff (p38), a "Right to Access" protocol worth "12–18 months" (p39), a Lender’s Direct Agreement (p40), and a "Nuclear Dividend" of 1–2% of output (p42).
   - Seven opportunity segments, A–G; A and B are sized (~35–40 GW; ~10–15 GW) (p45).
   - Five participant archetypes with named Indian firms (pp48–49).
9. **Case studies.** Five country cases (US, Canada, UK, Japan, Europe), about 1p each: context → mechanism → a boxed "Key Takeaway". They are introduced by "India is not the first country to pursue nuclear privatization. It therefore benefits from a late-mover advantage" (p29) and then synthesised into the Framework table.
10. **Actions for readers.** Named mitigations for policymakers (Ch4); roles by participant archetype (Ch5); and a three-part agenda in the conclusion with a time box ("The next 12–18 months must be a period of deliberate choices", p50).
11. **Tone and voice.** Authoritative and argued, with appropriate hedging. *Representative:* "However, an addressable market is not the same as an accessible one." (p50)
12. **Firm positioning.** Minimal: "we invite you to join that conversation" (p50). No services pitch.
13. **Weaknesses.**
    - **Long exec summary** (3pp) with no findings list.
    - **Date conflict:** the timeline dates the Atomic Energy Act to "1964" (p25), but the text says 1962.
    - **Amended or repealed?** p25 says the acts were "substantially amended under the SHANTI Bill", while p26 says "It repealed both".
    - **Implausible figure:** PFBR capex of "~INR 5 Cr/MW" (p15), against INR 15–16 Cr/MW for PHWR.
    - **Typos:** "form sources" (p11); "INR 25-30/MW" (p15).
    - **Voice slip:** the conclusion speaks as if YCP were an investor ("For us, this means evaluating whether our entry point is in captive industrial power…", p50).
    - **Unsized segments:** C–G are not sized.
    - **Proposal shown as fact:** the p43 exhibit lists a "Nuclear PLI" (4–6% incentive) without marking it as a proposal, while p41 says "There is no Production Linked Incentive (PLI) scheme for nuclear heavy manufacturing"; the scheme is proposed, not in force.

## P11 · Powering Successful Digital Transformation: Driving Measurable Business Value (YCP Renoir)

1. **Basics.** July 2026. Printed pages run to 25. About 5,300 words. Single author: Max Ferrin, Partner & Group Head of Transformation (p25). The reader is leaders running digital transformation (implied).
2. **Central question and governing thought.** *Central question (inferred):* why does digital/AI transformation fail, and what process makes it deliver value? *Governing thought (stated, p17):* "Ultimately, sustainable digital transformation is not defined by the technologies deployed, but by the value realized."
3. **Structure.** Exec summary (pp3–4) → urgency (pp5–6) → five failure modes (pp7–8) → five-step framework (pp9–12) → TMO (pp13–14) → AI imperative (pp15–16) → Conclusion (pp17–18; clean in print, but P8's conclusion sits behind it as hidden white text, see "Read this first") → "The YCP Advantage" (p19) → client case (pp20–22) → References (p23).
4. **Executive summary.** About 230 words: short prose plus three statistics with superscript citations (e.g. AI spending "USD 2.5 trillion in 2026",³ p4). No findings.
5. **Headlines.** Topics ("The Framework for Success", p9). The failure-mode headlines are pointed: "Implementing technology for the sake of technology" (p7), "Change management is an afterthought" (p8).
6. **Evidence.** **Numbered superscripts and a numbered reference list** (9 entries in APA style with URLs, p23). Sources mix Gartner, Forrester and WEF with blogs (intuition.com, elementor.com, allaboutai.com). Reference 7 is never cited. The same statistic is cited to two sources (4 on p5, 9 on p6).
7. **Exhibits.** About 7: a five-step band with "Change management is embedded throughout every stage of this framework." (p9); a four-tile trends panel (p6); a "4 Key Drivers" icon set (p15); result tiles (p22). Nothing is numbered. **Most effective:** *the five-step band*, because its one-line caption states the design principle.
8. **Frameworks and tools.** **Failure modes in a "Mistake:" format** (pp7–8): headline → "Mistake:" line → explanation → example. A choice between PMO and TMO by maturity (p13).
9. **Case studies.** One anonymised chemical-company case (pp20–22) laid out as Summary / Background / Challenge / Approach / Implementation / Results. The results are outputs ("100 total opportunities"), not business outcomes.
10. **Actions for readers.** Embedded in the framework steps; one reader type.
11. **Tone and voice.** Direct, in the second person. *Representative:* "Many companies think change management involves sending an email before a tool’s go-live date." (p8)
12. **Firm positioning.** Heavy: "The YCP Advantage" lists eight numbered benefits (p19), plus the case and an About Us page.
13. **Weaknesses.**
    - **Hidden leftover text:** P8's full conclusion is embedded, invisibly, behind the conclusion pages (pp17–18). It surfaces in any copy-paste or text extraction.
    - **Impossible date:** "as of late 2026, 78% of global companies report using AI" (p15) in a July 2026 paper, cited to an October 2025 blog.
    - **Inconsistent figure:** USD 2.5tn (p4) vs 2.52tn (p15).
    - **Weak sources** (blogs).
    - **Thin core topic:** the AI chapter is only two pages.
    - **Generic,** with nothing specific to Asia.

## P12 · Creativity in the Age of AI Algorithms: How Ideas are Chosen, Shaped, and Scaled by Code

1. **Basics.** July 2026. Printed pages run to 26. About 5,700 words. Authors (p26): Eucel Maximo (Partner, Interactive Solutions Division), Arianne Chuidian (Senior Content Marketing Associate), Andrea Gerada (Associate). **The reader is stated** (p3): "It is written for CMOs and digital marketing teams who sense that the old playbook no longer works".
2. **Central question and governing thought.** *Governing thought (stated):* "The central thesis is simple but consequential: short-form platforms and AI have shifted creative authority from humans to feedback loops." (p3)
3. **Structure.** "The New Creative Order" (p3) → five chapters titled as claims, each with a short sub-title ("The end of the gatekeeper era", p4), pp4–22 → "The Strategic Imperative" (p23) → "How YCP Can Help" (pp24–25). **There is no executive summary and no conclusion.**
4. **Executive summary.** None. The opening page does the job: a narrative ("That world is over."), three stat tiles, the thesis, and the stakes ("Those that don’t will keep funding campaigns that algorithms have already decided to bury.", p3).
5. **Headlines.** **Claim-led.** "Chapter 1: Why Algorithms Now Decide What ‘Good Creative’ Means" (p4); "Authentic, imperfect, but engaging content beats polished, expensive ads." (p15). Each country profile has a nickname headline, e.g. "Thailand: The Social Commerce Powerhouse" (p20).
6. **Evidence.** **Nearly every exhibit carries a "Sources:" line** with publisher and year (e.g. "_Sources: DataReportal / We Are Social / Meltwater — Digital 2025; Marketing-Interactive 2025_", p18). Quality is mixed: DataReportal, WARC and Nielsen sit alongside stat aggregators (ZipDo, Digital Silk, Teleprompter.com). Some claims are unattributed ("Research confirms that 71%", p6). One range is honest: "an estimated 127 to 165 million active users depending on the source" (p19).
7. **Exhibits.**
   - **Count and types:** about 19: stat tiles; the process diagram "How AI Decides What Goes Viral" (p5); a Signal | What It Measures | Why It Matters table (p6); an AI capability table (p12); **"Regional Overview: Key Digital Indicators by Country"**, six countries × six metrics (p18); per-country profiles, each with three KPI tiles tagged with rank ("(#1 globally)"); a TikTok Shop GMV table (p22); a "Traditional Approach vs YCP Approach" table (p25).
   - **Most effective:**
     - *The Regional Overview table*: comparable, sourced metrics for six countries on one page.
     - *The per-country profile* format (nickname headline → paragraph → "For brands, …" so-what line → three KPI tiles → source).
     - *The Signal table.*
8. **Frameworks and tools.** Light: the signal table, and "The New Brand Framework: Flexible Systems, Not Fixed Assets" (p16).
9. **Case studies.** None.
10. **Actions for readers.** Three implications ("First… Second… Third…", p6), a "For brands, …" line in each country profile, and a "Cost of Inaction / Opportunity" pair (p23). One reader type.
11. **Tone and voice.** Punchy, journalistic, short sentences, second person. *Representative:* "Today, algorithms decide which creative gets seen, how long it survives, and whether it deserves more distribution." (p3)
12. **Firm positioning.** Heavy: pp24–25 on services, "Why YCP: The Cost Advantage", and "Our clients consistently see improved ROAS" (p24), unsupported. The thesis (24–32 creatives a month) maps directly onto the service being sold.
13. **Weaknesses.**
    - **No exec summary or conclusion.**
    - **Aggregator sources.**
    - **Source label doesn't match the text:** "Meta’s 2024 Ad Performance Report" vs a source line reading "Meta Analytics, 2023" (p9).
    - **Unreconciled figures:** Indonesia is TikTok Shop's "second-largest … after Thailand" (p19, Q1 2025) but the largest in the FY2025 table (p22), where Thailand is "Second-largest globally". The same table says "Every major SEA market posted triple-digit growth", but it shows the Philippines at +99% and Singapore "—", and its country values (about USD 39–45bn) do not clearly add up to the stated USD 45.6bn.
    - **Sales close.**

## P13 · Building Sustainability Governance Frameworks for Performance

1. **Basics.** July 2026. Printed pages run to 41. About 8,100 words. Single author: Imad Alfadel, Partner, Sustainability Solutions Division (p41). The reader is boards and executive teams (implied).
2. **Central question and governing thought.** **Both are stated.**
   - *Central question:* "However, a critical question remains unanswered: Which governance structures work when?" (p26)
   - *Governing thought:* the commitment–performance gap reflects "a more fundamental structural problem: sustainability governance structures mismatched to organizational capability." (p3)
3. **Structure.** Exec summary (p3) → Introduction (pp4–6) → the dual-layer structure (pp7–25, about 19pp) → Maturity–Governance Mismatch across four stages (pp26–37) → The Way Forward (pp38–39, **2pp**) → About the division (p40). *Opens* with the gap between commitment and performance. *Closes* on "matched governance".
4. **Executive summary.** One page, about 280 words, four prose paragraphs. **Answer-first**: the gap → the usual explanation → the real cause → the mechanism → how the paper differs ("This approach differs from prescriptive 'best practice' guidance…"). No numbers.
5. **Headlines.** Mixed. Bold claim lead-ins: "Governance failures underlie ESG performance failures" (p6); "Role clarity prevents dysfunction." (p39). The failure modes are named in the headlines: "The Governance Failure Mode: Invisibility" (p28).
6. **Evidence.** Light: Harvard Law School Forum, IFRS, SFDR, BCG–INSEAD. Unsourced generalisations ("Good corporate governance is consistently linked to higher profitability and lower risk", p6). **Firm data:** "Our assessment of client boards finds a similar distribution to broader industry surveys" (p16), with the source line "Based on our analysis of board governance practices. Industry benchmarks referenced from BCG - INSEAD Board ESG Pulse Check (March 2022)". The sample size is not given.
7. **Exhibits.** About 10. **Most effective:**
   - *"Comparative Analysis of Governance Models"* (pp14–15): Model | Strategic Pros | Critical Risks/Cons | Ideal Use Case for six models, which works as a decision aid.
   - *The Sustainability Maturity Curve* (p27), which names the failure mode for each stage: Invisibility, Silo, Coordination, Complacency.
   - *The board-model chart* (p16): Embedded in Governance 31%; Standalone ESG Committee 20%; Layered onto Existing Committee 10%; Distributed Across Committees 10%; Individual Board Advocate 15%; Ad Hoc / Informal 12%. The middle four are bracketed as "Transitional structures".
   - Also useful: a table comparing disclosure frameworks, labelled "as of 2024" (p20).
8. **Frameworks and tools.** **A stage template repeated for four maturity stages** (pp28–37): Organizational Characteristics → Common Indicators → Governance Failure Mode (A. Board Level / B. Management Level) → "Why Advanced Governance Models Fail at This Stage" → "Observable Trigger Patterns". There are also decision rules ("Smaller boards (under 7 directors)… may find Models 1 or 5 more practical", p17) and six success factors.
9. **Case studies.** None; one hypothetical (water-stressed regions, p11).
10. **Actions for readers.** Decision factors that map context to a model (p17), success factors, and "What This Means for Your Organization" (p39). Board and management are distinguished.
11. **Tone and voice.** Measured and analytical; coins terms ("what we term the sustainability governance paradox", p4). *Representative:* "When structures exceed organizational capability, they create complexity without corresponding effectiveness. When structures lag capability, they constrain performance and frustrate talented teams." (p3)
12. **Firm positioning.** Light: a one-page About the division with a list of services (p40).
13. **Weaknesses.**
    - **No cases.**
    - **Thin evidence.**
    - **Imbalance:** about 35pp of diagnosis vs 2pp of way forward.
    - **Repetition:** the "ultimate objective" sentence appears on p17 and again on p23.
    - **Template leftover (hidden):** P4's title sits in white text after the running header on p15. It is invisible in print, but present in the text layer.
    - **Chart problems (p16):** the shares total 98%; YCP's client data and the BCG–INSEAD 2022 benchmark are not distinguished; no sample size.
    - **Models ranked two ways:** Distributed Across Committees is "The preferable practical pathway for most companies" (p15), but the chart labels Embedded in Governance "Most effective" and treats Distributed as transitional (p16).
    - **Typo:** "Prefixes sustainability into key business contexts" (p15).
    - **Numbering error:** the Stage 1 list is off by one (p29).
    - **Typos:** "accountability of diffusion" (p29).
    - **Dated table:** the disclosure table is "as of 2024".

## P14 · Japan's Capital Markets: Structural Transformation and the Emergence of a New Value Creation Ecosystem

1. **Basics.** August 2026. Printed pages run to 48. About 13,200 words (estimated after removing chart-axis numbers). Authors (p48): Daisuke Katano (Managing Partner, Group Officer, Co-Head of the Management Services Division) and Masa Matsuoka (Managing Partner, Japan Regional CEO). The reader is corporate executives, investors and PE (the conclusion addresses executives and investors, p47).
2. **Central question and governing thought.** *Central question (inferred):* is the fall in listed companies a decline or a renewal? *Governing thought (stated, p6):* "these three forces—TSE as the foundation, activists as the catalyst, and PE funds as the executors—form a tightly integrated ecosystem that is accelerating privatizations and corporate restructuring in Japan."
3. **Structure.** **The chapters mirror the argument**: global context (Ch1) → Foundation: TSE reform (Ch2) → Catalyst: activists (Ch3) → Executor: PE (Ch4) → Conclusion (p47). Each chapter ends with a synthesis and a bridge ("In the next chapter, we explore how activist investors are becoming the 'spark'…", p24). *Opens* with a hook fact: "In 2024, Japan’s equity market passed a historic inflection point: for the first time, the number of delistings exceeded the number of initial public offerings (IPOs)." (p3)
4. **Executive summary.** Five pages, about 1,000 words. Prose with bold bullets and a public/private "dual structure", then a one-page "Key Insight" summary with four tiles (p7). Quantified.
5. **Headlines.** **Claim-led, with a consistent metaphor system.** "The Role of PE Funds: From "Shelter" to "Surgeon"" (p24); "Why Japan Is an "Activist Heaven": 3 Structural Reasons" (p32); the exhibit title "Over 80% of delistings are driven by strategic or ownership-led decisions." (p14).
6. **Evidence.** **The most precise source notes in the set**, e.g.:
   - "Source: JPX, Corporate Governance White Paper 2025 (data edition), Fig. 123" (p22);
   - definitions reconciled: "EY reports 109 companies (Jan–Jun) under a different definition" (p25);
   - "Note: Chart values are rounded. The published +320% growth rate is calculated using the unrounded base value…" (p37);
   - "IPO counts exclude Tokyo Pro Market (TPM)" (p12);
   - "Chart is illustrative" (p9).

   In-text citations such as "(Preqin/JPEA, Chart 4)" (p38). No reference list.
7. **Exhibits.**
   - **Count and layout:** about 35, unnumbered. Each is laid out as chart + side annotation boxes + a boxed "Key Insight" or "Implication:".
   - **Most effective:**
     - *The IPO vs delisting crossover chart* (p12): one picture carries the thesis.
     - *The "alligator's mouth" chart* (p9), whose caption states the takeaway.
     - *The Japan "(Activist Heaven)" / U.S. "(High Friction)" / Europe "(High Barrier)" table* (p31): labelled comparative verdicts.
8. **Frameworks and tools.** The three-force ecosystem; PBR = ROE × PER (p16); a hard law vs soft law table (p24); public/private dual structure.
9. **Case studies.** A one-page Fuji Soft case ("Activists Preparing the Stage for PE", p33) and named public deals (Seven & i/York, TechnoPro, Toshiba, Alinamin) as deal cards (p41).
10. **Actions for readers.** Boxed implications, e.g. "a PE-led carve-out should be seriously considered as a default option" (p19). Conclusion messages go to executives and investors (p47).
11. **Tone and voice.** Declarative, metaphor-rich, sometimes overclaiming ("irreversible"; "The outdated image of "vultures" is gone.", p24). *Representative:* "Japanese activists often don’t need to win the vote: the mere threat of a binding proposal brings management to the table." (p31)
12. **Firm positioning.** None overt. The section "Consulting Firms as an 'Artificial Supply Source'" (p44) praises consultants but notes their limits.
13. **Weaknesses.**
    - **Long exec summary** (5pp).
    - **Repeated fact:** the US "8,090 → 4,010, 7.3x" point appears at least four times.
    - **Contradiction:** the conclusion says market cap "doubles" (p47) vs 7.3x earlier; the metaphor also switches from "alligator" to "crocodile mouth" (p47).
    - **Stale forecast:** "By the end of 2025 … expected to fall to 3,782" (p12) in an August 2026 paper.
    - **TOC and body chapter titles differ.**
    - **One-sided view of PE.**

## P15 · The Next Era of Source-to-Pay: Building an AI-Powered Procurement Operating Model

1. **Basics.** August 2026. Printed pages run to 42. About 7,800 words. Authors (pp41–42): Saurabh Mehta (Managing Partner, Supply Chain Solutions Division CEO), Arun Gupta (Director), Rinkoo Singh (Manager), Shivi Malik (Analyst). **The reader is stated** (p3): "designed for CPOs, CFOs, COOs, and transformation leaders".
2. **Central question and governing thought.** *Governing thought (stated, p3):* "AI-driven Source-to-Pay (S2P) is no longer optional; it is now a strategic necessity".
3. **Structure.** Exec summary (p3) → Why AI (pp4–8) → capabilities (pp9–12) → roadmap (pp13–15) → change management (pp16–18) → ROI (pp19–21) → "How YCP Supports…" (pp22–26) → **six client cases (pp27–38, not listed in the TOC)** → Conclusion (p39) → References (p40). Each section ends with "Key Takeaways".
4. **Executive summary.** One page, about 220 words, three paragraphs, **dense with numbers** ("from USD 13-20 to approximately USD 2-3 per invoice"; "2-5x ROI").
5. **Headlines.** Topics ("Implementation Roadmap"). Claim sub-decks: "AI Source-to-Pay success hinges on proving value beyond cost savings…" (p19).
6. **Evidence.** **No in-text citations.** An unnumbered reference list (13 items, p40) is not linked to any claim and is heavy on vendors (Ivalua ×4, GEP, SAP). Some references are misdated (a KPMG PDF from 2014 listed as 2025). Unsupported claims include "cutting implementation timelines by 40% versus traditional Big Four/SI approaches" (p13) and being "recognized as a leader in the Gartner Magic Quadrant for Source-to-Pay Suites" (p25).
7. **Exhibits.** About 14, plus six case layouts on full navy pages: a stat banner (p4); "Business Impact at a Glance" (p4); "Traditional vs. AI-Enabled Source-to-Pay" by stage (p5); a roadmap (pp13–14); "4 Pillars of AI Adoption" (p16); KPI categories with benchmark tiles (p21). **Most effective:** *the Traditional vs AI table by process stage*, a clear before/after for each step, and the call-out "Key executive decision: Allocate 90 days for Assessment and POC to validate 2-5x ROI before scaling enterprise-wide." (p14)
8. **Frameworks and tools.** A four-stage roadmap (Assess / POC / Scale / Optimize); four change pillars; four KPI categories.
9. **Case studies.** Six anonymised client cases of about 2pp each (pp27–38) in a fixed template: client → Key Challenge → Our Approach → "Quantified Impact" (Cycle time / Cost / Compliance / Adoption) → Strategic Outcome. **Cases 1–3 contain no numbers under "Quantified Impact".** Cases 4–6 do (e.g. "Procurement turnaround times improved by nearly 50%", p34).
10. **Actions for readers.** The roadmap and the 90-day decision; one reader group.
11. **Tone and voice.** Assertive sales register. *Representative:* "We don't start with software demos. We start by quantifying the current "cost of doing nothing,"" (p25)
12. **Firm positioning.** **The heaviest in the set**: about 17 of 39 body pages cover YCP's services, delivery model, "The YCP Commitment" and client cases.
13. **Weaknesses.**
    - **Headline statistics repeated** five to six times.
    - **Inconsistent figures:** invoice cost "USD 3–20" (p4) vs "USD 13-20" elsewhere; spend under management "nearly 60%" (p3) vs "Up to 87%" (p4).
    - **Geography mismatch in Case 3:** the footprint is Vietnam/Thailand/Malaysia/Myanmar/HK, but the rollout is "across Malaysia, Indonesia, and China" (p31).
    - **Unlinked references.**
    - **Mis-grouped services:** in the services graphic (p23), "Expense Management Digitization" lists generic implementation services (testing, maintenance, helpdesk).

## P16 · System Integration in the Generative AI Era: How AI Agents are Redefining Delivery, Governance, and Talent — The Path Toward 2030 (joint paper)

1. **Basics.** Published September 2026 by NTT DATA INTELLILINK, YCP and ABP. "Three-Month Publication Series, Issue No. 1". About 6,400 words; printed pages run to 28 (30 PDF pages). Authors (pp25–26):
   - NTT DATA INTELLILINK: Masatoshi Hiraoka, Naoto Kajiwara, Takahiro Shida;
   - YCP: Tsukasa Sato (Partner, Digital Transformation Division);
   - ABP: Kohei Nakamura (President & Representative Director).

   Each is listed with expertise keywords and email; there are no bios. **The reader is stated** under "Intended Readers" (p5): clients' "managers and department heads", executives, and students and early-career professionals.
2. **Central question and governing thought.**
   - *Governing thought (stated, Executive Summary, p3):* "Generative AI is beginning to shift the axis of competition in system integration (SI)—from how fast and how much organizations can build (delivery capacity) to how safely and auditably they can operate AI agents…"
   - *Central question (stated, "THE QUESTION", p23):* "Which platforms will you depend on? In what contexts will you implement them? How quickly can you provide assurance? And who will you develop to lead over the next five years?"
3. **Structure.**
   - **Front matter unique in the set (cover and pp5–6):** a masthead with the verification period and an as-of date ("figures and cases in the text are current as of the end of the verification period (July 14, 2026)"), "Background and Aims", "Intended Readers", "Mini Glossary", and "Premises (setting the scope for the discussion)".
   - **Body:** a news-hook introduction (p4) → seven March 2026 hypotheses (p7) → a five-point verdict scale (p8) → a verdict table (p9) → one section per hypothesis (pp12–17) → "Four Strategic Contests" by time horizon (pp19–22) → "Issues and Agenda for the Next Phase" (pp23–24) → three "Perspective Break" interludes (pp10, 18, 24) → a numbered source list (pp27–28).
   - **The TOC (p2)** lists every chapter with page numbers; the sources are not listed in it.
4. **Executive summary.** About 300 words on one page (p3): a one-sentence thesis, **"Key Findings"** (six bullets, each a full claim sentence, e.g. "Sovereignty, export controls, and geopolitical availability are becoming the primary constraints of architecture design."), and "Implications for Business Leaders" (one paragraph).
5. **Headlines.** **Claim plus verdict**: "Surviving Systems Integrators Become “AI Integrators” — Progressed Far Beyond Expectations" (p12); "Build Demand Remains Strong — But the Skill Threshold for Junior Talent Is Inferred to Be Rising" (p16).
6. **Evidence.**
   - **The best citation practice in the set:** 28 numbered sources ("Numbered, for verification", pp27–28), each with publisher, date, URL and the exact figure it supports (e.g. "METR … (~19% slowdown; CI ~+2% to +39%)").
   - Comparability caveats: "the three figures cover different scopes, denominators, and periods and are not directly comparable" (p13).
   - Figures are labelled "self-reported", "company-disclosed" or "vendor survey", and field observations are flagged as such ("Observations from the authors’ day-to-day interactions…", p17).
   - **Two citation-number errors (p16):** the Anthropic Economic Index is cited as [13] instead of [17], and Stanford "Canaries" as [14] instead of [18].
7. **Exhibits.** About 12:
   - a hypotheses table (p7);
   - a verdict-scale icon row (p8);
   - a verdict table (H1–H7 | Content | Verdict (as of July) | Update, p9);
   - **five boxed "Implication" statements**, one closing each hypothesis section (pp12, 13, 14, 16, 17), each restating the verdict in one "more precisely" sentence;
   - four A-vs-B contest panels with a navy "Authors' View" box (pp20–22);
   - a TCS pull quote (p15).

   Design: royal and navy blue, with AI imagery on the divider pages. **Most effective:** *the verdict table*, which grades each prior claim on a declared five-point scale ("Progressed far beyond expectations / Progressed as hypothesized / Inconclusive / Moved in the opposite direction / Clearly rejected").
8. **Frameworks and tools.** A causal chain (p6); seven hypotheses; the verdict scale; four contests by horizon (within 1 year; 1–3 years ×2; 3–10 years), each A vs B with an explicit authors' call.
9. **Case studies.** Short, cited examples (DXC OASIS as "A Symbolic Case"; TCS; Fujitsu; TIS; IBM).
10. **Actions for readers.** An explicit position per contest ("The choice largely leans B.", p20; "The choice is A: Treat sovereignty… as the first constraint of the design.", p21; "A slight edge to A — but this does not mean simply increasing headcount.", p22). One reader framing.
11. **Tone and voice.** Candid and calibrated ("inferred", "inconclusive"); openly invites challenge ("We would genuinely welcome your feedback, counterarguments, and perspectives…", p24). *Representative:* "More precisely, what is collapsing is not the need for hiring but the traditional apprenticeship model." (p16)
12. **Firm positioning.** None.
13. **Weaknesses.**
    - **Citation-number errors** (p16).
    - **Duplicated and missing labels:** "PERSPECTIVE BREAK 1" appears twice (pp10, 18); there is no Break 2, although p10 refers readers to it.
    - **Small slips:** hypotheses labelled "Hypotheses 1…7" (p7); p24 refers to "Chapter 4" although no chapter is numbered.
    - **Narrow and provisional:** Japan-specific, with conclusions provisional by design (it is issue 1 of a series).

---

# STEP 2 — Synthesis across all 16

## 2.1 House style: what most papers do, and how many do it

Counts are out of 16 unless stated otherwise. Where a convention varies, the variants are listed rather than forced into one rule.

### Front and back matter

| Convention | Count | Papers / variation |
|---|---|---|
| Month–year dateline on the cover | **16/16** | All |
| Standard legal disclaimer (small print at the foot of the **front cover**) | **15/16** | All except P16, whose cover carries a joint scope-and-currency statement instead. The entity named varies: "YCP", "YCP Renoir" (P4, P8, P11), or "YCP Supply Chain" (P6). |
| Table of contents with page numbers | **16/16** | TOC and body titles differ in P14. P15's TOC omits its six case studies; P16's omits its sources. |
| Titled "Executive Summary" | **15/16** | Not P12 (its opening page does the job) |
| Titled "Conclusion" | **12/16** | Two more have an equivalent (P13 "The Way Forward"; P16 "Issues and Agenda for the Next Phase"). P1 and P12 have none. |
| Authors section | **16/16** | Bios in 15 (P16 lists expertise keywords only); email addresses in 14 (not P1, P2) |
| Office list on the back pages | **16/16** | All |
| "About Us" / about-the-division page | **6/16** | P4, P6, P7, P8, P11, P13 |
| Running header with the full title on each page | **16/16** | The title sits between two thin rules, top left. Footer: royal-blue page-number tab bottom left, plus "ycp.com" bottom right in 14 papers (absent in the two Dec-2025 papers, P1 and P2). |
| House typography and palette | **16/16** | Palatino Linotype for titles and exhibit titles; Segoe UI / Yu Gothic UI for body text; navy (~#001C44) and bright blue (~#007FFF) on white. Other colours only as deliberate accents (see 2.6). |
| Glossary or abbreviations list | **3/16** | P1 (A1, with a "Meaning" column), P7 (92 abbreviations), P16 (an up-front "Mini Glossary") |
| Methodology statement | **2 substantive, 3 partial** | Substantive: P1 (scoring logic + rubric), P16 (verification period, premises, numbered sources). Partial: P7 (evidence-base sentence, p3), P5 (data notes), P13 (client-data note). |
| Reader stated explicitly | **4/16** | P7 (p3), P12 (p3), P15 (p3), P16 ("Intended Readers") |
| An "as of" date for the data | **1/16 overall** | P16. Partial: P5 (partial-year note), P10 (FX date), P14 (month-end tallies). |
| Contributors credited | **1/16** | P5 (p22) |

### Length

Two clusters:

- **Short papers (15–28 printed pages): 8** — P2, P4, P5, P8, P9, P11, P12, P16 (28 pp, about 6,400 words).
- **Long papers (41–59 pages): 8** — P1, P3, P6, P7, P10, P13, P14, P15.

A draft of about 50 pages sits with P1 (58), P7 (59), P10 (52) and P14 (48). Within the long cluster, body text runs from about 7,800 to 13,200 words.

### Executive summaries (out of the 15 papers that have one)

| Convention | Count | Papers / variation |
|---|---|---|
| About 500 words or fewer (roughly 1–1.5 pages) | **13/15** | Exceptions: P10 (~900 words, 3pp) and P14 (~1,000 words, 5pp) |
| Mainly prose | **14/15** | Only P16 leads with a bulleted "Key Findings" list. **No paper numbers its findings.** |
| Contains any numbers | **5/15** | P7, P10, P11, P14, P15 |
| Mainly a roadmap ("this paper examines…") rather than findings | **6/15** | P2, P3, P4, P5, P6, P8 |
| States the answer in the first paragraph | **5/15** | P9, P13, P15, P16; P12's opening page does the same |
| Ends with actions by reader type | **1/15** | P7 (p5) |

### Headlines and exhibit design

| Convention | Count | Papers / variation |
|---|---|---|
| Section headlines mostly claims | **4** | P7, P12, P14, P16 |
| Mixed claims and topics | **4** | P1, P9, P10, P13 |
| Mostly topics | **8** | P2, P3, P4, P5, P6, P8, P11, P15 |
| Exhibit titles descriptive rather than claims | **14/16** | Claim-titled exhibits mainly in P14 (and P2's chart labels). In P7 and P14 the claim sits in the page headline above a descriptive chart title. |
| Exhibits numbered at all | **5/16** | Only P5 is consistent. P1 stops at Figure 3; P3 repeats numbers; P4 and P8 number only one or two. Format varies: "Figure 1:" (P1, P4, P8) vs "Table 1." / "Figure 1." (P3, P5). |
| At least one exhibit with a source line | **12/16** | Not P6 or P15. P11 and P16 use numbered citations instead. |
| Source line on most exhibits | **3/16** | P3, P12, P14 |
| Source label wording | varies | "Source:" (P1, P2, P3, P5, P14) / "Sources:" (P3, P10, P12) / "Source(s):" (P4, P8, P9). **Placement:** the house default is the **left margin beside the exhibit, under a short blue rule, in italic grey** (P3, P4, P8, P9, P12, P13, P14). Below the exhibit in P1, P2 and P5 (Table 1). |
| Colour used to carry meaning | **5/16** | P5 (Harvey balls; R/V/T coloured codes), P7 (blue-intensity presence map; green/yellow/pink heat map), P2 (a red "Critical Gap"), P13 (maturity stages darkening), P14 (grey "past" vs blue "future" panels). P1 names a RAG scale but does not colour it. |
| Firm's own analysis credited as a source | **7/16** | "YCP Research & Analysis" (P3, P5), "YCP Internal" (P10), "YCP Renoir" (P8), "our analysis of board governance practices" (P13), "self-analysis" (P7), authors' field observations (P16) |
| Stat tiles / KPI banners | **8/16** | P2, P7, P8, P10, P11, P12, P14, P15 |
| A-vs-B comparison tables | **9/16** | P1, P3, P9, P10, P12, P13, P14, P15, P16 |
| Stage, maturity or phase models | **7/16** | P3, P4, P5, P7, P10, P13, P14 |

### Evidence

| Convention | Count | Papers / variation |
|---|---|---|
| Reference list or bibliography | **4/16** | P7 (grouped by source type, not linked to claims), P11 (numbered), P15 (unnumbered, not linked), P16 (numbered, with the exact figure each source supports) |
| Numbered in-text citations | **2/16** | P11, P16 |
| At least one unattributed "research shows" / "surveys show" statistic | **≥8/16** | P1, P3, P4, P6, P8, P12, P13, P15 |
| Formal primary research by the firm (survey or interview programme) | **0/16** | The closest are P13's client-board assessment, P16's field observations, and P7's reference to "client engagements, industry discussions" |

### Cases and actions

| Convention | Count | Papers / variation |
|---|---|---|
| Any cases or examples | **11/16** | None in P2, P8, P9, P12, P13 |
| Named public-company cases | **7** | P1, P3, P6, P7, P10, P14, P16 |
| Anonymised client cases | **5** | P1, P4, P5, P11, P15 (P6's anonymised examples are not attributed to clients) |
| Actions organised by reader type | **3 clearly, 3 partly** | Clearly: P2, P7, P10. Partly: P3, P13 (board vs management), P14 (executives vs investors). |
| Actions with a time box | **4** | P1 ("twice a year"), P10 ("next 12–18 months"), P15 ("90 days"), P16 (horizon-based contests) |
| A "so-what" device at the end of sections | **9/16** | "Key Takeaways" (P7, P15); "Key Insight" / "Implication:" (P14, P16); "Implication for Brands" (P12); "Why now?" (P1); "Key Takeaway" per case (P10); "Strategic Implications of…" (P9); "Business Opportunities and International Implications" (P3) |

### Tone and firm positioning

**Tone.** The default is formal third person with occasional "we" (most papers). Six papers address the reader directly as "you/your" (P1, P11, P12, P13, P15, P16). Calibrated hedging is strongest in P9, P10 and P16. Urgency and overclaiming are most marked in P1, P12, P14 and P15.

**Firm positioning** varies from none to about 44% of pages:

| Intensity | Papers |
|---|---|
| None | P2, P3, P9, P14, P16 |
| Light (bios, an About page, one line) | P6, P7, P10, P13 |
| Medium | P1, P5 |
| Heavy (multi-page capability sections) | P4, P8, P11, P12, P15 |

## 2.2 Where the papers disagree

**Conventions that genuinely vary** (so you should choose rather than follow a rule):

- **Executive summary format:** prose vs "Key Findings".
- **Headline style:** claims vs topics.
- **Exhibit conventions:** numbering, the source label, and where it sits.
- **Voice:** "we" vs "you".
- **Firm pitch:** research-led papers keep it to a line (P7, P10, P14, P16); capability papers devote whole sections to it (P4, P8, P11, P12, P15).

**Four substantive tensions matter for the China Playbook:**

1. **What role Chinese investment plays in Thailand.**
   - P6 calls Thailand an EV hub "for non-Chinese investors" (P6, p18).
   - P1 highlights "Chinese OEMs led by BYD" pledging ">USD 1.44 billion" around Rayong (P1, p24).
   - Your Thailand case should reconcile the two with dated evidence.
2. **The standard of proof for "structural".**
   - P1 asserts "a structural, not cyclical, uplift in demand" (P1, p7) without a test. P14 calls change "irreversible" (P14, e.g. p4).
   - P16 instead grades each claim on a declared scale and says so when evidence is "Inconclusive".
   - Your structural-vs-cyclical test should follow P16.
3. **The firm's published view of Chinese outward investment.**
   - P9 frames it as aimed at "upstream industries, resource security, and advanced industrial inputs" (P9, p5).
   - Your paper extends this to OEM market entry and dealer-led competition. Say so explicitly so the two papers don't appear to conflict.
4. **Is competition good or bad?**
   - P1's scorecard gives *higher* attractiveness to "Very intense competition… crowded marketplace" (P1, p55).
   - In your paper, Chinese competition is a threat to incumbents but an opportunity for dealers and financiers. State the direction of any scoring explicitly.

## 2.3 What the best papers do differently

**Ranking criteria:**

- a clear question and governing thought;
- quality and traceability of evidence;
- a structure that serves the argument;
- useful exhibits;
- actions a named reader can take;
- production quality.

These rankings are my judgement.

### #1 — P10 *Unlocking India's Nuclear Sector*

- **It states its question and answers it with arithmetic.** The central question is written out (p5). The governing thought, "arithmetic necessity" (p18), rests on a stated run-rate comparison (~130 MW a year historically vs ~4,000 MW a year required). The reader can check the logic, not just the rhetoric.
- **It turns cases into rules.** Five one-page country cases each end in a boxed "Key Takeaway" (pp30–34). A synthesis table then maps each principle to the countries it came from (p35). No other paper converts its cases into a framework so explicitly.
- **It pairs every problem with a named, specific fix, then summarises them all on one page.** Chapter 4 gives each issue a memorable label ("The Fuel Cycle Trap", p41). Each label is paired with a concrete mechanism, often quantified: "Right to Access" saves "12–18 months" (p39); heavy-water leasing saves "INR 1,500–2,000 crore" (p38). The one-page "Bridging the Nuclear Capacity Gap" (p43) then puts all six clusters and fixes side by side.
- **Its actions fit the participant.** Five archetypes are named with example Indian firms (pp48–49), policy fixes are separated out, and the conclusion is time-boxed (p50).
- **What not to copy:**
  - the 3-page exec summary with no findings list;
  - the internal date and "amended vs repealed" contradictions (pp25–26);
  - the voice slip in the conclusion, where the firm writes as if it were an investor.

### #2 — P7 *India's Logistics Industry*

- **It tells readers who it is for and what it rests on,** before the exec summary (p3).
- **Its exec summary is quantified and ends with actions for three player types** (pp4–5). It is the only exec summary in the set that does both.
- **Its sections are questions and its headlines are answers.** The TOC asks "What Makes…Compelling?", "Where Are Opportunities…?" and "How Different Player Archetypes Are Approaching…?", and nearly every page headline is a claim.
- **Every section closes with a "Key Takeaways" page and a signpost** (pp32, 40, 52), which helps readers who skim.
- **Its tools can be used as they stand:** a maturity matrix (p10), an archetype × segment map (p42), a PPP lifecycle risk matrix (pp46–47), an M&A attractiveness heat map (p49), and a five-type × four-area M&A pitfalls grid (pp50–51).
- **What not to copy:**
  - the inconsistent growth rates and other figures;
  - a 27-page attractiveness section against a 1-page conclusion;
  - slide-like bullet density;
  - a sources appendix that is not linked to claims.

### #3 — P16 *System Integration in the Generative AI Era* (joint paper)

- **It has the best evidence method in the set:**
  - 28 numbered sources, each annotated with the exact figure used;
  - caveats on comparability and self-reporting;
  - field observations labelled as observations;
  - a single "as of" date for all figures.
- **It sets its method out up front:** premises that bound the scope, a mini-glossary, and intended readers.
- **It holds itself to account.** Hypotheses are stated in advance, then graded on a five-point verdict scale that includes "Inconclusive" and "Clearly rejected". **This is a ready-made model for your structural-vs-cyclical test and signposts to 2030.**
- **It takes positions.** Each of the four "contests" is set on a time horizon and ends with an explicit authors' call.
- **Its sections close consistently.** Every hypothesis section ends with a boxed "Implication" that restates the verdict in one "more precisely" sentence (pp12–17).
- **What not to copy:**
  - the citation-number mismatches (p16);
  - the duplicated "Perspective Break 1" label and the missing Break 2 (pp10, 18).
- **Caveat:** it is a joint paper and Japan-specific.

### Close contenders

- **P14 *Japan's Capital Markets*** — the structure follows the logic of the argument (foundation → catalyst → executor), with the best source notes in the set and captions that state the takeaway. Held back by a 5-page exec summary, repetition and overclaiming.
- **P13 *Sustainability Governance*** — the clearest answer-first exec summary, and a failure-mode template repeated across four stages with "Observable Trigger Patterns". Held back by having no cases and a 2-page "way forward".
- **P1 *Strategic Pathways*** — the most relevant to your topic, with strong tools (scorecard, viability test, delivery-model tree). Held back by weak sourcing and a contradictory scoring method.

## 2.4 Recurring weaknesses to avoid

| Weakness | Papers | Example |
|---|---|---|
| **Internal numbers that disagree** | **9**: P1, P2, P3, P7, P10, P11, P12, P14, P15 | Penn Station 294,000 vs 600,000 on facing pages (P3, pp6–7); PLI "10–18%" vs "up to 1%" (P1, pp14–15); "doubles" vs 7.3× (P14, p47); GMR "three" airports vs 4 in the figure (P3, p32) |
| **Labels or framework counts drift within a paper** | **8**: P1, P2, P4, P6, P7, P8, P14, P16 | 3 vs 4 pillars and 5 vs 4 steps (P6, pp4, 8, 10); council named two ways (P2, pp16–17); TOC and body titles differ (P14); ownership types 5 → 4 → 5 across pp48–51 (P7); four enablers vs five pillars (P8) |
| **Unattributed statistics** | **≥8** | "Recent industry surveys show…" (P6, p5); "Research confirms that 71%" (P12, p6) |
| **Exec summary is a roadmap, not findings, or has no numbers** | **6 roadmap; 10 without numbers** | P2, P3, P4, P5, P6, P8 |
| **Production or template errors (visible)** | **≥8**: P3, P4, P6, P7, P13, P14, P15, P16 | Wrong division on the About page and P4's title in the header (P7, p59); duplicate and out-of-order figure numbers (P3); five empty quote cells (P4); list numbered off by one (P13, p29); cases missing from the TOC (P15); duplicated and missing "Perspective Break" labels (P16) |
| **Hidden text-layer leftovers** (invisible in print, present in any extraction) | **3**: P7, P11, P13 | P8's whole conclusion behind P11's (pp17–18); P4's title in white on P13 p15; a duplicate "Opportunity" box on P7 p35 |
| **Charts that do not add up or lack a legend** | **3**: P7, P12, P13 | Stack segments unlabelled (P7, p35); country GMVs vs the regional total (P12, p22); board-model shares total 98% (P13, p16) |
| **Time-stale wording** | **5**: P1, P2, P11, P13, P14 | "hub by 2025 and beyond" in a Dec-2025 paper (P2, p4); "as of late 2026" in a Jul-2026 paper (P11, p15); a disclosure table "as of 2024" (P13, p20) |
| **Unsupported promotional claims** | **4**: P8, P11, P12, P15 | The Gartner MQ claim (P15, p25); outcome ranges with no basis (P8, p19); "Our clients consistently see improved ROAS" (P12, p24) |
| **Cases that are unsourced, anonymised-but-recognisable, or "quantified" without numbers** | **5**: P1, P5, P6, P11, P15 | P15 cases 1–3; the P5 p13 case; P1's company one-liners |
| **Repetition** | **5**: P1, P6, P13, P14, P15 | S2P headline statistics repeated 5–6 times (P15); US listing fact repeated ≥4 times (P14) |
| **Diagnosis outweighs what to do** | **4**: P7, P13, P3, P9 | 35pp of diagnosis vs 2pp of way forward (P13) |
| **Opaque scoring** | **3**: P1, P5, P13 | Two scoring methods and inverted competition scoring (P1); undisclosed weights and criterion direction, so the Table 1 verdicts cannot be reproduced from the scores (P5, p6); client data mixed with a 2022 benchmark and no sample size (P13, p16) |
| **Actions not segmented by reader** | **10** | Most papers write for one undifferentiated leader |
| **Exhibits unnumbered or inconsistently numbered** | **15** | Only P5 numbers every exhibit consistently |

## 2.5 Reusable template for a long white paper (about 45–55 printed pages)

Target pages include exhibits. The skeleton borrows each element from the paper that does it best.

| # | Section | Target | Guidance | Precedent |
|---|---|---|---|---|
| 0 | Cover, disclaimer, TOC | 2–3 pp | Month–year dateline; the house disclaimer; a TOC whose titles match the body exactly | House style (15–16/16); P14 shows the risk of TOC/body mismatch |
| 1 | **About this paper** | 1 p | Who it is for (and which chapters each reader should read); scope and exclusions; "data as of" date; sources and method in three sentences; pointer to the full methodology | P16 front matter; P7 p3 |
| 2 | **Executive summary** | 2 pp (max ~700 words) | Line 1: the governing thought. Then **numbered findings, each a full claim sentence with one number**. Then one verdict paragraph. Then **one line per reader group**. No roadmap sentences. | P16 "Key Findings"; P13 answer-first; P7 quantified + reader actions; P10 ends on the question |
| 3 | Context: "the shift in numbers" | 4–6 pp | Open on one striking, verifiable fact; 3–4 exhibits max; end with the central question stated in words | P14 hook fact (p3); P10 question (p5) and arithmetic (p18) |
| 4 | Core argument chapters (e.g. the learnings) | 14–18 pp | One claim headline per unit; the same internal template each time; a named case per unit; a boxed "so what" at the end | P1 recommendations (imperative + mini-case + rule, pp47–48); P10 challenge → mitigation; P14 "Key Insight" boxes |
| 5 | Test or diagnostic chapter | 3–5 pp | Declared criteria and a verdict scale; a verdict per item with the evidence and "what would change our view" | P16 verdict scale; P1 risk matrix (p51) for time margins |
| 6 | Country or segment chapters | 10–14 pp | A parallel template: snapshot scorecard → what happened → what worked / what didn't → policy levers → implications box. Size chapters to their weight; put comparators in one table. | P1 country chapters; P3 chapter endings; P12 country profiles and Regional Overview (p18) |
| 7 | Failure modes | 3–4 pp | Named failure modes, symptoms, "why it fails", early-warning triggers | P13 stage template (pp28–37); P11 "Mistake:" format (pp7–8); P10 coined labels |
| 8 | **Actions by reader group** | 4–6 pp (≥10% of body) | A matrix of reader × action, then 3–5 specific, time-boxed actions per reader | P7 (p5, p53); P10 (pp48–50); P2 (p17); P3 Table 6 (p22); P15 (p14) |
| 9 | Signposts or outlook | 2–3 pp | An indicator table: indicator → threshold → what it would mean → who should react → when to review | P16 contests by horizon; P1 time-margin RAG (p51); P13 trigger patterns |
| 10 | Conclusion | 1 p | Restate the governing thought; end on one question or three-part agenda; one soft, specific invitation | P10 (p50); P16 "THE QUESTION"; P7 CTA (p53) |
| 11 | Appendices | 4–8 pp | Methodology and definitions; scoring rubric if you score; glossary with meanings; numbered references with the figure each supports | P1 A1–A2; P16 sources; P7 abbreviations |
| 12 | Authors, contributors, about the firm, offices | 3–4 pp | Bios with email; a contributors line; one About page | House style; P5 contributors (p22) |

**For a 20–25-page paper:** drop sections 5 and 9, merge 6 into 4, and keep the exec summary to 1 page (P5 and P13 show the short format working).

## 2.6 Exhibit playbook

| Exhibit type | Where it recurs | Best used for | Best example | Rules |
|---|---|---|---|---|
| **Stat tiles / KPI banner** | P2, P7, P8, P10, P11, P12, P14, P15 | Opening hooks; per-country headline facts | P2 p11 (one fact + its own citation per tile); P12 country trios with rank tags | Max 3–4 tiles; each tile sourced; no repeating the same tiles across sections (P15 repeats them) |
| **Weighted scorecard / heat table** | P1, P5 | Ranking countries or options | P1 p11 + rubric pp54–55 | Show weights, the direction of each criterion, and one method only (P1 describes two); publish the rubric; disclose weights. P5's Harvey-ball grid (p6) shows what goes wrong without them: its verdicts cannot be reproduced from its own scores. Print the composite score next to the verdict |
| **Attractiveness heat map with rationale per cell** | P7 | Rating partners, targets or acquirers by type | P7 M&A Attractiveness Across Capital Provider Types (p49) | Three levels only; a one-line reason in every cell; keep the row and column categories identical across related exhibits (P7 changes them between pp48 and 51) |
| **Diligence grid by counterparty type** | P7 | What to check, and the pitfall for each type of partner | P7 Considerations and Pitfalls (pp50–51) | A shaded "what to check" band per area, then one pitfall per type; same types as the heat map |
| **Presence map (entity × segment)** | P7 | Who plays where | P7 archetype × segment (p42) | Four levels in one hue (Primary / Secondary / Limited / None); ring the columns the paper focuses on |
| **Problem → fix bridge (one page)** | P10 | Summarising a challenges-and-mitigations chapter | P10 "Bridging the Nuclear Capacity Gap" (p43) | One column per challenge: challenge, named fix, one-line effect; mark proposals as proposals (P10 does not) |
| **Comparison table (dimension × entity)** | P1, P3, P9, P10, P12, P13, P14, P15, P16 | Contrasting two playbooks or models | P9 Japan vs China (p6); P10 Before/After (p28); P13 Pros / Risks / Ideal Use Case (pp14–15); P14 labelled verdicts (p31) | 4–6 rows; parallel wording in each cell; a verdict label per column where possible |
| **Stage / maturity model** | P3, P4, P5, P7, P10, P13, P14 | Showing how an actor or market evolves | P7 maturity matrix mapped to eras (p10); P13 maturity curve naming the failure mode per stage (p27) | Name each stage; say what moves an actor from one stage to the next |
| **Timeline** | P10, P13, P14 | Chronology and milestones; targets to 2030 or later | P10 1947–2047 (p4) | Mark "actual" vs "target"; put the paper's as-of date on the axis |
| **Benchmark bar (one metric, several peers)** | P3, P7, P10 | A single, decisive comparison | P7 port turnaround (p30); P3 non-aero revenue per passenger (p34) | Sort bars; highlight the focus country; single source |
| **Chart with a claim call-out** | P10, P14 | Carrying the thesis in a picture | P14 IPO-vs-delisting crossover (p12); P10 "Least total cost for firm power" (p11) | Put the takeaway sentence under the chart (P14 p9) |
| **Flow / ecosystem / decision-tree diagram** | P1, P3, P10, P14 | Who does what; entry-mode choice | P1 delivery-model tree with a "Filter:" question per branch (pp37–38); P3 stakeholder flows (pp19–21) | Label arrows with what flows (money, rights, product) |
| **Opportunity window / pipeline table** | P1 | Dated windows for action | P1 Program / Scale and scope / Timeline (pp16–31) | Dates and funding status in every row; flag stale windows before publication |
| **Lifecycle × stakeholder matrix** | P3 | Actions by reader and phase | P3 Table 6 (p22) | Rows = reader groups; columns = phases or horizons |
| **Risk matrix** | P1, P7 | Risks with timing | P1 likelihood / impact / time margin with RAG (p51); P7 PPP lifecycle risks (pp46–47) | Define High / Medium / Low thresholds in the table itself (P1 does this), and apply the RAG colours to the cells (P1 names them only in words) |
| **Hypothesis / verdict table** | P16 | Testing claims; tracking signposts | P16 H1–H7 verdicts | Declare the scale first; allow "Inconclusive" |
| **Case template box** | P1, P4, P5, P10, P11, P15 | Consistent cases | P1 Prize / Edge / Gameplan (pp40–43); P4 Need / Action / Result / Quote (pp20–22); P10 "Key Takeaway" | Same fields every time; a quantified result or none at all (P15's "Quantified Impact" without numbers is the anti-pattern) |
| **Maps** | P3, P7, P10 | Footprints, corridors, plant or dealer locations | P7 MMLP and port map (p34); P7 FTA map (p17); P10 capacity map (p8) | Numbered legend; the date of the footprint |
| **Boxed implication after each unit** | P14, P16 | Carrying the "so what" | P16 "Implication" boxes (pp12–17); P14 "Key Insight" bars | One or two sentences; restate the verdict; start "More precisely…" where it corrects a lazy reading (P16 p16) |

### Rules for titles and sources, taken from the strongest practice

1. **Put the claim in the headline above the exhibit** (P7, P14). Keep the exhibit title descriptive, with its unit and period: "India’s GDP Growth Trajectory (2022–2030P)" (P7, p6); "Figure 1. Southeast Asia Total Number of IPOs and Funds Raised (in USD Billion)" (P5, p7).
2. **Add a one-sentence takeaway caption where the chart carries the argument.** P14 p9: "In the U.S., the number of listed companies has halved over the past 30 years, while total market capitalization expanded more than sevenfold…"
3. **Number every exhibit consecutively with one label.** Only P5 does this; P1 stops at 3 and P3 duplicates numbers. Pick one word ("Exhibit") and one punctuation style.
4. **Use one source-line format in one position.** The house position is the left margin beside the exhibit, under a short blue rule, in italic grey (P3, P9, P12, P13, P14). The house wording varies: "Source:", "Sources:" and "Source(s):". The most useful style names the publication, date and table or figure number, as in P14: "Source: JPX, Corporate Governance White Paper 2025 (data edition), Fig. 123". Add "YCP analysis" where you transformed the data (P3, P10).
5. **Put data caveats in a note line under the source:**
   - partial year (P5 p7);
   - exclusions (P14 p12, "IPO counts exclude Tokyo Pro Market (TPM)");
   - rounding (P14 p37);
   - definition differences (P14 p25);
   - comparability (P16).
6. **Label schematics "Illustrative"** (P2 p8; P14 p9 "Chart is illustrative").
7. **Give currency conversions a date** (P10 p3: "at the time of preparing this report").
8. **Every series needs a legend and every part must add up.** P7's warehousing stack (p35) has no legend. P13's board-model shares total 98% (p16). P12's country values do not reconcile with its regional total (p22).
9. **Put company names in text, not only as logos.** P3's operator table (p32) is readable only as logos, so extraction and screen readers lose it.

### Colour rules, taken from what works in the PDFs

The house template fixes type (Palatino titles, Segoe UI / Yu Gothic UI body) and colour (navy and bright blue on white). Colour carries meaning in only five papers. Where it does, it works best when:

- **intensity scales stay in one hue.** P7 p42 uses four shades of blue for Primary / Secondary / Limited / None, which reads in greyscale and stays on-brand;
- **one alert colour is reserved for one meaning.** P2 p8 uses red only for the "Critical Gap";
- **traffic lights are used sparingly and always with a legend.** P7 p49 is the only off-palette colour in its paper;
- **the scale is applied, not just named.** P1 p51 describes Red/Amber/Green in words but leaves the cells uncoloured;
- **Harvey balls have a stated direction.** P5 p6 leaves unclear whether "High" is good.

## 2.7 Phrase and headline bank (20 items, quoted exactly)

**Headlines that make a claim**

| # | Quote | Source | Why it works |
|---|---|---|---|
| 1 | "Global infrastructure is bigger than ever, and it’s heading to Asia." | P1, p5 | Claim plus direction in 10 words |
| 2 | "Defending champions are slowing down" / "Promising contenders rise up" | P1, p8 | Paired contrast headlines |
| 3 | "Anchor ambition to funded demand, not press releases" | P1, p47 | Imperative in "X, not Y" form |
| 4 | "Treat manufacturing depth as a staged investment, not a leap of faith" | P1, p48 | Imperative in "X, not Y" form |
| 5 | "Turn Compliance into Currency" | P1, p36 | Short, memorable reframe |
| 6 | "The Role of PE Funds: From "Shelter" to "Surgeon"" | P14, p24 | "From X to Y" shift |
| 7 | "Why Japan Is an "Activist Heaven": 3 Structural Reasons" | P14, p32 | Why + number + label |
| 8 | "The Fuel Cycle Trap" | P10, p41 | Coined label for a failure mode |
| 9 | "Surviving Systems Integrators Become “AI Integrators” — Progressed Far Beyond Expectations" | P16, p12 | Claim plus verdict |
| 10 | "India’s high dependence on road freight contributes to elevated logistics costs" | P7, p28 | Cause → effect page headline |

**Transitions and framing**

| # | Quote | Source | Why it works |
|---|---|---|---|
| 11 | "The central question is no longer whether the private sector will participate in India’s nuclear expansion, but how, and under what institutional architecture, that participation will take shape." | P10, p5 | "No longer whether, but how" framing |
| 12 | "However, a critical question remains unanswered: Which governance structures work when?" | P13, p26 | Question as a bridge between parts |
| 13 | "Before examining the scaling challenge itself, it is important to step back and understand why addressing it has become imperative." | P10, p9 | Signposted step back |
| 14 | "With the enabling ecosystem now defined and the path to bankability cleared, the focus shifts to the scale of value creation." | P10, p43 | Recap + pivot |

**"So what" lines**

| # | Quote | Source | Why it works |
|---|---|---|---|
| 15 | "A third engine—private capital—is therefore no longer a policy preference; it is an arithmetic necessity." | P10, p18 | Reframes a preference as a necessity |
| 16 | "However, an addressable market is not the same as an accessible one." | P10, p50 | Crisp distinction |
| 17 | "However, while India has clearly emerged as a gateway economy, it has not yet become a major transhipment hub." | P7, p19 | Concession + limit |
| 18 | "Missing one pillar weakens valuation, but missing multiple can destroy it." | P5, p13 | Escalation |
| 19 | "More precisely, what is collapsing is not the need for hiring but the traditional apprenticeship model." | P16, p16 | Corrects a lazy reading |
| 20 | "Japan’s history of building systems during periods of population expansion, and now operating them during demographic stagnation or decline, offers both a benchmark and a warning." | P3, p13 | Two-sided lesson |

**Formulations to avoid** (they read as sales copy and weaken credibility):

- "The longer you wait, the less advantageous it will be." (P1, p22)
- "In the Philippines, timing isn’t optional—it defines profitability and strategic access." (P1, p31)
- "AI-driven Source-to-Pay (S2P) is no longer optional; it is now a strategic necessity" (P15, p3)

---

# STEP 3 — Applying this to *The China Playbook for Emerging Asia*

I have not seen the draft itself. The recommendations below work from your brief:

- **Readers:** CEOs, APAC and country heads, strategy teams, dealers, financiers, policymakers.
- **Sectors:** construction equipment, material handling, compressors and pumps, robotics.
- **Countries:** India and Indonesia in depth, Thailand as a focused case, Vietnam and Malaysia as comparators.
- **Shape:** about 50 pages; free public sources with numbered references; six learnings; a structural-versus-cyclical test; country chapters; failure modes; actions by reader group; signposts to 2030. Exhibits to be chosen later.

Where I say "check", I cannot tell from the brief whether the draft already does it.

## 3.0 Proposed shape, mapped onto the template (about 50 body pages)

| Section | Target | Built from |
|---|---|---|
| About this paper: reader map, scope, as-of date, sources in brief | 1 p | P16 front matter; P7 p3 |
| Executive summary | 2 pp | P16 Key Findings; P13 answer-first; P7 p5 |
| Ch1 The rise in numbers, ending on the central question | 4 pp | P14 hook fact; P10 question (p5) and arithmetic (p18) |
| Ch2 Six learnings (about 2.5 pp each) | 15 pp | P1 pp47–48; P10 Ch3–4; P14 Implication boxes |
| Ch3 Structural or cyclical? The test | 4 pp | P16 verdict scale; P13 triggers |
| Ch4 Country chapters: India 4, Indonesia 4, Thailand case 2.5, Vietnam + Malaysia comparator 1.5 | 12 pp | P1 country template; P3 chapter endings; P12 p18 comparator table |
| Ch5 Failure modes | 3 pp | P13 pp28–37; P10 coined labels; P11 pp7–8 |
| Ch6 Actions by reader group: one matrix page + about 0.7 p per group | 5 pp | P7; P10 pp48–50; P3 Table 6; P2 p17 |
| Ch7 Signposts to 2030 | 2 pp | P16 contests; P1 p51 |
| Conclusion | 1 p | P10 p50; P16 "THE QUESTION" |
| Back matter: methodology and definitions (2), glossary (1), references (3–4), authors and contributors (2), About YCP + contact (1), offices (1) | ~10 pp | P1 A1–A2; P16; P5 p22 |

If your 50 pages *include* back matter, trim Chapter 2 to about 13 pp and Chapter 4 to about 10 pp.

## 3.1 Prioritised recommendations

### High priority

**1. Make the executive summary answer-first and quantified: the governing thought, six numbered learnings, the verdict, and a line for each reader. Keep it to two pages or less.**

- **What to do.**
  - Open with the governing thought in one sentence.
  - List the six learnings, numbered, each a full claim sentence carrying one sourced number.
  - Add one sentence giving the overall structural-versus-cyclical verdict.
  - Add six one-line "what this means for…" statements, one per reader group.
  - Cut every "this paper examines…" sentence.
- **Precedents:** P16 "Key Findings"; P13's answer-first logic (p3); P7's quantified summary that ends with actions by player type (pp4–5).
- **Avoid:** roadmap summaries (P2, P3, P4, P8); 3–5-page summaries (P10, P14); numbers that change between summary and body (P15: "nearly 60%" vs "Up to 87%", pp3–4).

**2. State the central question in words, and back the governing thought with arithmetic the reader can check.**

- **What to do.** Write the question as a single sentence at the end of Chapter 1, and repeat it in the conclusion. Anchor the answer in a visible calculation.
- **Precedent:** P10 does both. The question is on p5: "The central question is no longer whether…but how…". The governing thought on p18 rests on "~130 MW per year over 70 years versus a required run rate of ~4,000 MW per year".
- **Your equivalent** might be the average share-point shift per year by sector and country compared with the incumbents' historical trajectory. That is illustrative only; use whatever your data supports.

**3. Turn the structural-versus-cyclical test into a declared, graded method.**

- **What to do.**
  - Before giving any verdict, define the criteria and a verdict scale. For example: *Structural / Likely structural / Inconclusive / Likely cyclical / Cyclical*.
  - Show a verdict table: driver × country, with the evidence behind each cell and "what would change this verdict".
  - Allow an "Inconclusive" where the evidence is thin.
- **Precedents:** P16's five-point scale and H1–H7 verdict table, which keeps "Inconclusive" verdicts with reasons; P13's "Observable Trigger Patterns" as the "what would change our view" column.
- **Avoid:** asserting the conclusion without a test (P1 p7: "a structural, not cyclical, uplift"; P14's repeated "irreversible").

**4. Give all six learnings the same internal template, with a claim headline and a named, sourced case.**

- **What to do.** Each learning, about 2.5 pp:
  - a claim headline in a proven form ("X, not Y", as in P1 p47/p48, or "From X to Y", as in P14 p24);
  - 2–3 sourced data points;
  - one named case (a Chinese OEM, a sector and a country);
  - a sentence on the limits of the learning;
  - a boxed implication for incumbents, and where relevant for dealers and financiers.
- **Precedents:** P1's recommendations (a bold imperative, a mini-case, then a one-line rule, pp47–48); P10's cases each ending in a boxed "Key Takeaway"; P14's "Implication:" boxes (p19).
- **Improve on P1:** its mini-cases carry no sources.

**5. Run every country chapter on one template, sized to its role; handle the comparators in a single table.**

- **What to do.**
  - India and Indonesia: the same sequence — snapshot strip → what Chinese OEMs did → what worked / what didn't → policy levers (e.g. PLI, TKDN) → implications box.
  - Thailand: a 2–3-page case in the Delhi Aerocity style of P3 (pp36–37), with dated facts.
  - Vietnam and Malaysia: one comparator table in the style of P12's "Regional Overview" (p18), not two mini-chapters.
- **Precedents:** P1's country chapters (Macro snapshot → Policy trends → Strengths/Risks → Opportunity window, pp14–31); P3's closing "Business Opportunities and International Implications" section in each chapter.
- **Reconcile with past papers:**
  - P1 (December 2025) already scored and characterised these five markets ("Indonesia: Localization fortress", p11). Either stay consistent or say what has changed.
  - Resolve the Thailand tension between P1 (p24, "Chinese OEMs led by BYD") and P6 (p18, "for non-Chinese investors").
- **Avoid:** uneven chapters (P3); an urgency box in every chapter (P1 "Why now?").

**6. Write the actions as a reader-group matrix, then 3–5 time-boxed actions for each of the six groups.**

- **What to do.**
  - Build one page with rows for CEOs, APAC/country heads, strategy teams, dealers, financiers and policymakers, and columns for *next 12 months*, *12–36 months* and *to 2030*.
  - Then give each group 3–5 actions. Each starts with a verb, names its horizon, and says which learning it follows from.
  - Give policymakers named mechanisms, not exhortations.
- **Precedents:**
  - P7, the clearest reader-type actions (p5, p53);
  - P10, participant archetypes with named firms (pp48–49) and a time box ("The next 12–18 months…", p50);
  - P2, Industry / Government / Investor roles (p17);
  - P3 Table 6, a stakeholder × phase matrix (p22);
  - P15's call-out "Key executive decision…" (p14);
  - P10 Chapter 4's named mechanisms, as a model for policy asks;
  - P10's two-tier participant map (p48: "Lead Project Adopters & Operators" vs "Delivery, Supply, and Financial Enablers"), which maps onto the Playbook's readers (CEOs, APAC and country heads, and strategy teams vs dealers, financiers and policymakers);
  - P7's M&A heat map (p49) and pitfalls grid (pp50–51), as a template for the dealer, JV-partner and acquirer sections (rows = partner or acquirer type, e.g. incumbent OEM, Chinese OEM, dealer group, financier; each cell rated with a one-line reason; then "what to check" and pitfalls by type).
- **Avoid:** the undifferentiated reader of ten past papers; P2's "must" statements with no mechanism behind them.

**7. Name each failure mode, and give its symptoms, cause and early-warning trigger.**

- **What to do.**
  - Give each failure mode a short, memorable label.
  - For each, list symptoms at the CEO/board level and at the country or dealer level, explain why it happens, and list observable triggers.
  - Link each one to a learning.
  - Close the chapter with one page that bridges each failure mode to its remedy: one column per mode, giving the named mode, the named remedy and a one-line effect. Mark any remedy that is a proposal rather than existing policy.
- **Precedents:** P13's four-stage template ("The Governance Failure Mode: Invisibility" → A. Board Level / B. Management Level → "Why … Fail" → "Observable Trigger Patterns", pp28–37); P10's labels ("The Fuel Cycle Trap", p41); P11's "Mistake:" line format (pp7–8); **P10's one-page "Bridging the Nuclear Capacity Gap" (p43)** for the closing summary.
- **Avoid:** generic Benefits/Risks bullet lists (P6, pp11–20); showing a proposed policy as if it existed (P10's "Nuclear PLI" on p43 vs p41).

### Medium priority

**8. Turn the signposts to 2030 into an indicator table the reader can monitor.**

- **Columns:** indicator; current value with its as-of date; threshold; which verdict it supports (structural or cyclical); who should react; review cadence.
- **Precedents:** P16's horizon-based contests and graded updates; P1's risk matrix, which adds a Red/Amber/Green "time margin" (p51); P1's "Install a policy radar that scans twice a year" (p48).
- **Optional:** P16 frames itself as a "living document". You could commit to a revisit.

**9. Make free public sourcing a visible strength.**

- **What to do.**
  - Link every statistic to a numbered reference, and note in each reference the exact figure used and the access date.
  - Give one "data as of" date.
  - Flag company-reported and estimated figures.
  - Prefer primary sources (government statistics, filings, registrations) to aggregators.
- **Precedents:** P16 (28 annotated sources; comparability caveats); P14 (source notes naming the figure, the date and definition differences).
- **Avoid:** unlinked vendor-heavy lists (P15); aggregator statistics (P12); unattributed "surveys show" (P6); mixing the firm's own client data with a public benchmark in one unlabelled series (P13, p16). Show YCP data as its own series, with n and date.

**10. Add a methodology and definitions box (1 page up front plus 1–2 pages in an appendix).**

- **Define:**
  - what counts as a "Chinese OEM";
  - the boundaries of the four sectors;
  - the share metric (units vs value; registrations vs shipments) and how it differs by country;
  - the period covered, and why these countries get these depths;
  - how verdicts are reached, and whether there is any scoring;
  - the FX basis.
- **Precedents:** P16's front matter (verification period, premises, intended readers, glossary); P1's scoring logic and published rubric (p10, pp54–55); P7's evidence-base sentence (p3); P10's FX note (p3).
- **Avoid:** P1's two conflicting scoring descriptions and its competition score pointing the wrong way; P5's Harvey-ball verdicts, which cannot be reproduced because neither the weights nor the criterion direction are stated (p6). Print the composite score beside any verdict.

**11. Make headlines claims; keep exhibit titles descriptive.**

- **What to do.** Every chapter and page headline should state a finding. The TOC can use questions, as P7 does. Exhibit titles stay descriptive, with unit and period.
- **Precedents:** P7, P14, P16 and P12 (the claim-led papers).
- **Avoid:** topic labels such as "Overview" or "Market Deep Dives" (the eight topic-led papers).

**12. Reserve exhibit slots now, even though the exhibits are chosen later.**

- **What to do.**
  - Fix the numbering ("Exhibit 1…n"), the source-line format and position (house default: left margin), and the caption rule now (Step 2.6).
  - Decide the colour semantics now: one blue intensity scale; one alert colour; RAG applied as colour; grey for "Inconclusive" (see the colour rules in 2.6).
  - Aim for about **25–30 exhibits**. Counts recounted from the PDFs: P10 has about 18 in 52 pages, P14 about 35 in 48, P7 about 45 in 59. The earlier target of about 22 is at the low end for the firm's long research papers.
  - See 3.4 for suggested slots.

### Standard priority

**13. Keep the tone confident but calibrated, and neutral about China.**

- **What to do.**
  - Use "we" for judgements.
  - Describe Chinese OEMs' capabilities and choices factually, and source any claims about subsidies or pricing.
  - Avoid urgency clichés and overclaiming.
  - Use at most one metaphor system, and use it consistently (P14 shifts from "alligator" to "crocodile", p47).
- **Precedents:** P10 and P16 for calibration; P9's even-handed Japan vs China comparison table (p6).
- **Avoid:** P1 p22 ("The longer you wait…"); P15 p3 ("no longer optional"); P10's voice slip on p50.

**14. Balance diagnosis and action.**

- **What to do.** Give failure modes, actions and signposts together at least 20% of body pages (about 10 of 50). Keep context to about 4 pages.
- **Precedent:** P10 spends about 14 of about 48 body pages on challenges and opportunities (Ch4–5).
- **Avoid:** P13 (2 pages of way forward after about 35 of diagnosis) and P7 (27 pages of attractiveness against a 1-page conclusion).

**15. Position the firm with a light touch and one specific call to action.**

- **What to do.** Include author bios with emails, a contributors line, a one-page About YCP, and one line naming the relevant capabilities (for example market entry, channel and dealer design, localisation and incentive qualification, M&A). Optionally, add one anonymised client vignette with quantified results in P4's Need / Did / Result table format.
- **Precedents:** P7 p53 ("We welcome the opportunity to discuss…"); P5's contributors page (p22).
- **Avoid:** multi-page capability sections (P15, P11, P12, P8).

## 3.2 Pre-publication checklist

Each item notes the past slip it guards against.

### A. Argument and structure

- [ ] The central question appears as one sentence at the end of Chapter 1 and again in the conclusion. *(P10 p5/p50)*
- [ ] The governing thought is the first sentence of the executive summary. *(P13, P16)*
- [ ] Each learning is worded identically in the exec summary, its chapter headline and the conclusion. *(Label drift in P4, P6)*
- [ ] Every learning has at least one named, sourced case. *(P1 cases unsourced)*
- [ ] Structural/cyclical verdicts use the declared scale and show "what would change this verdict". *(P16 method)*
- [ ] Every failure mode has observable triggers. *(P13)*
- [ ] Every reader group has 3–5 actions, each with a horizon. *(P10, P15)*
- [ ] Every signpost has a current value, a threshold and an as-of date.
- [ ] Failure modes, actions and signposts together take at least 20% of body pages. *(P13, P7 imbalance)*
- [ ] Thailand facts reconcile P1 p24 and P6 p18, and any change from P1's December 2025 country view is explained.
- [ ] The paper states how it extends P9's framing of Chinese outward investment (P9 p5).

### B. Executive summary

- [ ] Two pages or less; answer first; numbered findings; at least one number per finding; one line per reader group. *(P2, P3, P4, P8 are roadmaps)*
- [ ] No "this paper examines…" sentences.
- [ ] Every number in the summary appears, identically, in the body. *(P15, P7)*

### C. Evidence and numbers

- [ ] Every statistic has a numbered reference; no bare "research shows". *(≥8 papers)*
- [ ] Each reference records the figure used and the date accessed. *(P16)*
- [ ] There is one "data as of" date, and every "by 2025/2026" phrase has been checked against the publication date. *(P2 p4, P11 p15, P14 p12)*
- [ ] Numbers have been cross-checked across text, exhibits, summary and conclusion. *(9 papers had conflicts)*
- [ ] Company-reported, registration-based and estimated figures are labelled as such. *(P16)*
- [ ] Share definitions are harmonised across countries, or the differences are stated.
- [ ] FX conversions carry a date. *(P10 p3)*
- [ ] If anything is scored: weights, criterion direction and rubric are published, and there is only one method. *(P1, P5)*

### D. Exhibits

- [ ] Numbered "Exhibit 1…n", with no duplicates or gaps. *(P3, P1)*
- [ ] Claim headline above; descriptive title with unit and period; a takeaway caption where the exhibit carries the argument. *(P7, P14)*
- [ ] One source-line format and one position throughout, with notes for estimates, partial years, exclusions and rounding. *(P14, P5)*
- [ ] Schematics are labelled "Illustrative". *(P2, P14)*
- [ ] Every exhibit is referred to in the text. *(P5 Figure 1 is not)*
- [ ] No empty rows or cells. *(P4's results table: five of seven quote cells empty)*
- [ ] Every chart has a legend for every series or stack segment. *(P7 p35)*
- [ ] Parts sum to the stated total; percentages sum to 100% or carry a rounding note. *(P12 p22; P13 p16)*
- [ ] Row and column categories are identical across related exhibits. *(P7 pp48–51)*
- [ ] Figures appear in number order. *(P3 p35)*
- [ ] Proposed policies are marked as proposals in exhibits as well as in text. *(P10 p43)*
- [ ] Company names appear as text, not only as logos. *(P3 p32)*
- [ ] Colour semantics follow the declared scale; any RAG named is also applied. *(P1 p51)*

### E. Language and tone

- [ ] No urgency clichés and no "no longer optional". *(P1, P15)*
- [ ] Neutral, factual language about Chinese firms and policy; policy claims are sourced.
- [ ] One consistent voice for judgements. *(P10 p50 slip)*
- [ ] Every acronym and coined term is defined, and no acronym has two meanings. *(P4 "MAT", P8 "OXD", P7 "PLI")*

### F. Production

- [ ] TOC titles match body titles. *(P14)*
- [ ] Running headers show this paper's title on every page. *(P7 p59, P13 p15)*
- [ ] No text pasted in from other papers. *(P11 conclusion)*
- [ ] Framework and list counts are consistent everywhere. *(P6: 3 vs 4 pillars)*
- [ ] The About page describes the right division. *(P7 p59)*
- [ ] Proofread proper nouns and tables. *("Passanger", three times in P3)*
- [ ] Extract the text layer of the final PDF and diff it against the approved copy, so that no hidden frames from a reused template survive. *(P11 pp17–18 carries P8's whole conclusion in white text; P13 p15 and P7 p35 have similar leftovers)*
- [ ] Every page carries the running header and footer. *(P13 p15 lacks "ycp.com")*

### G. Front and back matter present

- [ ] Dateline and disclaimer; TOC; About this paper; methodology and definitions; glossary; numbered references; author bios with emails; contributors; About YCP; call-to-action line; offices.

## 3.3 What the paper is probably missing

The first rows are what the house almost always includes; the later rows are rarer but matter more for this paper.

| Element | How often past papers include it | Best precedent | Why it matters here | Check |
|---|---|---|---|---|
| Dateline + standard disclaimer | 16/16 and 15/16 | House standard | Legal baseline, especially for a paper on another country's firms | Confirm |
| TOC matching body titles | 15/16 | P5, P7 | Six reader groups will navigate by chapter | Confirm |
| Executive summary | 15/16 | P16, P13, P7 | The most-read page | Check its format against Rec. 1 |
| Conclusion (1 page) | 14/16 incl. equivalents | P10 p50; P16 "THE QUESTION" | The brief lists signposts but not a conclusion | Check |
| **About the authors** (bios + emails) | 15/16 bios; 14/16 emails | P7, P10 | Credibility on a sensitive topic | Check |
| Office list | 16/16 | House standard | — | Confirm |
| **Call to action** (one specific line) | About half the papers have a closing line or invitation; P7's is the most specific | P7 p53 | Turns readers into conversations without undermining neutrality | Likely missing |
| **About YCP page** | 6/16 | P7, P13 | Optional; keep to one page | Optional |
| **Methodology / definitions box** | 2/16 substantive (P1, P16) | P16 front matter; P1 A2 | **Needed more here than in most past papers:** you make structural/cyclical judgements, rely on free public data, and compare 4 sectors × 5 countries with different share definitions | Likely missing |
| **Glossary / abbreviations** | 3/16 | P1 A1 (with "Meaning") | Policy and trade terms such as TKDN, PLI, BOI, EEC and knock-down (CKD/SKD) assembly (all discussed in P1), plus OEM | Likely missing |
| **"About this paper" / reader map** | 4/16 state the reader explicitly | P16 "Intended Readers"; P7 p3 | With six reader groups, tell each where to go | Likely missing |
| **"Data as of" date** | 1/16 | P16 masthead | Fast-moving market shares and policies | Likely missing |
| Contributors credit | 1/16 | P5 p22 | Recognises the research team | Optional |
| Chapter-end "so what" boxes | 9/16 | P7 "Key Takeaways"; P14 "Implication:" | Helps readers who skim; carries the reader-group implications | Check |
| Numbered references linked to claims | 2/16 (P11, P16) | P16 | You already have numbered references; linking each to its claim and figure would make this among the best-sourced papers the firm has published | Check linkage |
| "Limits of this analysis" paragraph | 0/16 (P16's premises and "Inconclusive" verdicts come closest) | P16 | Protects the verdicts; natural home is the methodology box | Likely missing |

## 3.4 Exhibit slot plan (types only; the content is your choice)

| Chapter | Suggested slots (about 27) | Type (see 2.6) | Precedent |
|---|---|---|---|
| Exec summary | 1: six-learning summary panel or verdict strip | Stat tiles or verdict table | P14 "Key Insight" page (p7); P16 |
| Ch1 Rise in numbers | 3: share shift by sector × country; timeline of market entries; one hook chart with a claim call-out | Benchmark or stacked bars; timeline; chart with call-out | P7 p12; P10 p4; P14 p12 |
| Ch2 Six learnings | 9: one per learning, plus 3 boxed "implication" statements where a learning carries the argument | Comparison table (Chinese OEM playbook vs incumbent), flow diagram, benchmark bar; boxed implication | P9 p6; P1 pp37–38; P7 p30; P16 pp12–17 |
| Ch3 Structural vs cyclical | 2: criteria table; verdict table (driver × country) | Hypothesis/verdict table | P16 |
| Ch4 Countries | 6: India and Indonesia snapshot strips and policy-lever tables; Thailand case box; Vietnam + Malaysia comparator table | Scorecard strip, opportunity/policy table, case template, comparator table | P1 pp14–19; P3 pp36–37; P12 p18 |
| Ch5 Failure modes | 2: failure-mode map (mode × symptom × trigger); a one-page failure → remedy bridge | Stage/maturity-style matrix; problem → fix bridge | P13 p27; P10 p43 |
| Ch6 Actions | 3: reader group × horizon matrix; partner/acquirer attractiveness heat map; diligence pitfalls by partner type | Lifecycle × stakeholder matrix; heat map; diligence grid | P3 Table 6; P7 pp49–51 |
| Ch7 Signposts | 1: indicator table with RAG time margins | Risk matrix / verdict tracker | P1 p51; P16 |
| Appendix | 1: scoring rubric or definitions table, if you score | Rubric | P1 pp54–55 |

---

*End of document. All page references are to the printed page numbers, which equal the PDF page numbers in all 16 files (P16 included). Checked against the source PDFs on 28 September 2026. See `analysis/pdf-gap-fill-supplement.md` for the evidence behind each correction and for the house visual identity.*
