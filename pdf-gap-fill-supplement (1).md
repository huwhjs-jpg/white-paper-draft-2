# PDF Gap-Fill Supplement to *Lessons from YCP's Past White Papers*

**Companion to:** `analysis/china-playbook-lessons-from-past-white-papers.md` (the "baseline").
**Prepared:** 28 September 2026.
**Scope:** This document does not re-analyse the 16 papers. It does three things:

1. It resolves every gap the baseline flagged as unreadable or only partly readable in the Markdown conversions.
2. It corrects baseline statements that turned out to be conversion artefacts rather than faults in the papers.
3. It adds what the original brief asked for but the Markdown could not show: colour, layout, typography, exhibit design and exhibit counts.

The baseline has been updated to match. This supplement holds the evidence and the detail behind those updates.

---

## 0. How the PDFs were checked

- **Two methods.** Every page of all 16 PDFs (602 pages) was rendered as an image and inspected, and the PDF text layer was extracted and compared with the Markdown. Where a gap sat in a chart or graphic, the page was rendered at high resolution and read directly.
- **Page numbers.** In all 16 PDFs the printed page number equals the PDF page number. The cover is unnumbered page 1, and the offices page and back cover are unnumbered. **P16 does have printed page numbers (2–28).** The baseline was wrong to say it has none, so P16 can now be cited by page like the other papers.
- **Status labels used below:**
  - **Resolved:** the content is now read in full.
  - **Genuine:** the fault is in the published PDF, so the baseline was right.
  - **Artefact:** the fault exists only in the Markdown or in text hidden behind the artwork, so the printed page is fine and the baseline claim is retracted or downgraded.
  - **New:** a point the Markdown hid entirely.

### 0.1 A finding about the files: hidden text layers

Three PDFs carry text that is **invisible in print** but present in the text layer. It shows up in copy-paste, search, screen readers and any AI or Markdown extraction. This explains three of the baseline's "production errors":

| Paper | Hidden content | Where | Effect on the Markdown |
|---|---|---|---|
| P11 *Powering Successful Digital Transformation* | P8's entire "Conclusion & Key Takeaways" (five paragraphs, including the "go see and assess" (GSA) passage), in **white text** behind P11's blue conclusion pages | pp17–18 | Read as P8's text interleaved into P11's conclusion |
| P13 *Sustainability Governance* | P4's title in **white** after the correct running header | p15 | Read as a garbled running header |
| P7 *India's Logistics Industry* | A second copy of the warehousing "Opportunity:" box in the text layer | p35 | Read as a duplicated paragraph |

These are real file-hygiene defects, because anyone who extracts or quotes the PDF will get the wrong text. They are not visible production errors, though. **Lesson for the China Playbook:** before release, extract the text layer of the final PDF and diff it against the approved copy (see §5, checklist items).

---

## 1. Resolution of the gaps flagged in the baseline

The baseline's "Read this first" table listed damage in 11 files. The status of each is below.

| # | Paper | Baseline gap | Status | What the PDF shows (printed page) |
|---|---|---|---|---|
| 1 | P14 | CJK glyphs on pp23, 42, 47; chart axes as stray numbers | **Resolved (artefact)** | Clean text on all three pages. See §1.1. |
| 2 | P16 | No page numbers; TOC empty; five "Implication" boxes empty | **Resolved (artefact)** | Pages numbered 2–28; full TOC on p2; all five boxes have text. See §1.2. |
| 3 | P11 | Conclusion pp17–18 interleaved with P8 text | **Resolved (artefact / hidden layer)** | The printed conclusion is clean; the P8 text is hidden. See §1.3. |
| 4 | P1 | Exec summary first sentence split (p3); risk cube only as labels (p49); country photos unreadable | **Resolved** | Exec summary is intact; cube read in full; photos are decorative skylines. See §1.4. |
| 5 | P10 | "Bridging the Nuclear Capacity Gap" (p43) and participant graphic (p48) garbled | **Resolved** | Both read in full. See §1.5. |
| 6 | P5 | Table 1 scores not captured (p6) | **Resolved** | Harvey-ball scores read. **The verdict cannot be reproduced from them.** See §1.6. |
| 7 | P7 | Archetype × segment markers (p42) and M&A pitfalls table (pp50–51) not captured | **Resolved** | Full matrix and full pitfalls grid read, plus the p49 heat map. See §1.7. |
| 8 | P13 | Board-model percentages (p16) could not be mapped to models | **Resolved** | All six mapped. See §1.8. |
| 9 | P3 | Operator names missing from Figure 4 (p32) | **Resolved** | Names were logos. Two new text–figure conflicts found. See §1.9. |
| 10 | P2 | Conclusion bullets out of order (p17) | **Resolved (artefact)** | Clean two-column layout. See §1.10. |
| 11 | P15 | Services graphic garbled (p23) | **Resolved** | Five service boxes read. See §1.11. |

### 1.1 P14 *Japan's Capital Markets*: the glyph-damaged passages

The PDF text is clean. The CJK characters came from the Markdown converter's font mapping. The exact wording is below.

- **p23, soft law becoming hard law:** "While the 'comply or explain' principle may appear to lack enforceability, in practice it operates with far greater force. In Japan, unique market dynamics have effectively transformed this soft law framework into de facto hard law. Companies unable to offer economically rational explanations for holding policy shareholdings or posting low PBRs are effectively compelled to take action. … PE funds in Japan thus play the role not of shelter, but of surgeons — stepping in to perform structural surgery when firms can no longer escape reform."
  - The same page carries a SOX cost table (Fiscal Year | Total Cost (Average per Company) | Notes): 2004 (Year 1 of SOX), USD 4.36 million; early 2020s, USD 1.2–1.5 million.
  - Its source sits in the left margin: "FEI survey (FY2004); Protiviti surveys (early 2020s)".
- **p42, return drivers:** "According to a 2025 survey by Bain & Company, the percentage of GPs citing 'multiple expansion' as the main driver of returns has plummeted from **69%** five years ago to just **24%** today."
  - The chart pairs a grey "The Past: Multiple-Driven Returns" panel with a blue "The Future: Top-Line Growth" panel.
- **p47, closing sentences:** "…the Japanese market is finally emerging from decades of stagnation and stepping into a new era of true value creation. It is in this structural transformation, where capital and talent become more fluid, that Japanese companies can find a path toward regaining global competitiveness."
- **p27 chart (the Markdown's "孼.0 / 孴.孵"):**
  - Activist proposal mix: Capital Policy 44%, Governance 29%, Disclosure 18%, Other 9%.
  - A PBR-by-sector bar chart on a 0–9.0 axis. The Markdown's "孼.0" was "9.0" and "孴.孵" was "1.2".
  - Sector values include 0.88, 1.03, 1.00, 0.75, 0.74, 0.70, 0.62, with 1.2 for "All companies".
- **Authors (p48), which the baseline could not resolve:**
  - **Daisuke Katano:** Managing Partner, Group Officer, Co-Head of the Management Services Division. He is listed first.
  - **Masa Matsuoka:** Managing Partner, Japan Regional CEO.
  - Minor slip: Katano's bio calls him "our Partner" while his title is Managing Partner.
- **Genuine faults confirmed:**
  - **TOC and body titles differ for all four chapters.** For example, TOC Ch3 reads "Catalysts for Change: The True Nature of Pressure from Activists", while the body reads "The Catalyst of Transformation – The Enforcement Power Behind Activist Intervention".
  - **"Alligator" switches to "crocodile":** pp7 and 9 use "alligator's mouth"; p47 uses "crocodile mouth".
  - **"Doubles" vs 7.3×:** p47 says market capitalisation "doubles", against 7.3× earlier.

### 1.2 P16 *System Integration in the Generative AI Era*: page numbers, TOC and implication boxes

- **Page numbers and TOC.** Pages are numbered 2–28. The TOC on p2 lists: Executive Summary 3; Introduction 4; Initial Hypotheses on System Integration in the Generative AI Era (March 2026) 6; How the Hypotheses Have Evolved: July 2026 Update 8; Key Shifts Reshaping the System Integration Model 11; Four Strategic Contests Defining the Future of System Integration 19; Issues and Agenda for the Next Phase 23; Authors 25.
  - Sources (pp27–28) are not in the TOC.
- **Page map for the elements the baseline cited "by section":**
  - Masthead and scope statement: cover (p1).
  - Key Findings and Implications for Business Leaders: p3.
  - News-hook introduction: p4.
  - Background, Intended Readers and Mini Glossary: p5.
  - Causal chain and Premises: p6.
  - Core Hypotheses table: p7.
  - Five-point verdict scale: p8.
  - Verdict table: p9.
  - Perspective Break 1 ("The Story of the 'Reins'"): p10.
  - Hypothesis sections: pp12–17.
  - Perspective Break 1 again ("The Day Generative AI Became a 'Strategic Commodity'"): p18.
  - Contests: pp20–22.
  - "The Through-Line": p22.
  - THE QUESTION: p23.
  - Perspective Break 3: p24.
  - Authors: pp25–26.
  - Sources: pp27–28.
- **The five "Implication" boxes, which the Markdown showed as empty:**

| Page | Section | Implication text (exact) |
|---|---|---|
| p12 | Surviving SIers become "AI Integrators" | "Given moves like Agent 365, MCP, and A2A, we believe the harness is emerging as a distinct market category. For systems integrators, this is a major opportunity—and, as giant platform players are moving to control the general-purpose harness, also a threat." |
| p13 | Supply capacity expands | "The March supply-expansion hypothesis is correct. But reading it as a simple reduction in person-month requirements is misleading. More precisely, we are at the stage where the conditions for faster AI-generated output are now in place, but growth in generated volume and growth in verification burden are distinct dynamics. The review and verification debt building up behind the scenes—the backlog of AI-produced output that humans have not yet been able to vouch for—will become the next major competitive battleground for systems integration." |
| p14 | Customising general-purpose products | "The March hypothesis about the role of the 'AI Integrator' is updated to a division of labor between the platform providers' general-purpose layer and context-specific implementation by systems integrators. Designing secure arrangements for each client's data boundaries, permissions, approval workflows, audit trails, legacy-system connections, and accountability remains highly context-dependent work. This is where systems integrators retain their value." |
| p16 | Build demand remains strong | "More precisely, what is collapsing is not the need for hiring but the traditional apprenticeship model. That is precisely why TCS and DXC are, right now, not cutting headcount but investing in rebuilding talent-development pipelines at a scale of tens of thousands of people. That distinction is what will matter five years from now." |
| p17 | Japanese systems integrators | "For Japanese systems integrators, the near-term question is whether generative AI can alleviate labor shortages. The fundamental question, however, is whether the industry can shift to a value-delivery model—AI Integrator or industry-specific Context OS—before downward pressure on person-month pricing intensifies. Firms must use the current tailwind to fund that transition." |

- p15 has no Implication box. It carries a pull quote with a photo instead: "Enterprise AI value comes from understanding business context…" (K. Krithivasan, TCS [16]).
- **Pattern worth copying:** every hypothesis section follows the same sequence of claim-plus-verdict headline, evidence paragraphs, then a boxed Implication that restates the verdict in one "more precisely" sentence. This is the per-learning template recommended in the baseline (Rec. 4).
- **Baseline corrections:**
  - **Contest 4 does not list B before A.** Panel A (Invest in Hiring/Training) is on the left and B (Freeze Hiring) on the right (p22), so the baseline item is withdrawn.
  - **The running header is present on every page,** in two variants: "How AI Agents are Redefining…: The Path Toward 2030" and, on p11, "How AI Agents Are Redefining… — the Path Toward 2030".
- **Genuine faults confirmed or found:**
  - **"PERSPECTIVE BREAK 1" appears twice** (pp10, 18), and there is **no Perspective Break 2,** yet p10 tells readers to "see Perspective Break 2".
  - **Citation numbers are off by four on p16.** The Anthropic Economic Index is cited as [13] but is source 17; Stanford "Canaries" is cited as [14] but is source 18.
  - **The hypothesis table labels each row "Hypotheses 1…7"** in the plural (p7).
  - **p24 refers to "Chapter 4",** but no chapter is numbered.

### 1.3 P11 *Powering Successful Digital Transformation*: the conclusion

- **The printed pp17–18 are clean.** The title is "Conclusion: From Transformation To Sustained Value". p17 has five paragraphs; p18 has two, on the TMO/PMO roadmap and on digital transformation as "a powerful engine for value creation and business model reinvention".
- **The governing thought reads cleanly on p17:** "Ultimately, sustainable digital transformation is not defined by the technologies deployed, but by the value realized."
- **What the Markdown picked up:** P8's conclusion (pp20–21 of P8) sits in white text frames behind P11's artwork, at P8's own coordinates, with a duplicate hidden "ycp.com / 17" footer.
- **Verdict:** this is a template-reuse leftover, invisible in print but present in the text layer (see §0.1). It is not a visible production error. The fact that P11 was built from P8's file does fit the other shared-text evidence (P4 and P8 share a sentence).

### 1.4 P1 *Strategic Pathways for Industrial MNCs*

- **Exec summary (p3) is intact.** It is two columns and four paragraphs. The first sentence is complete: "Asia's industrial and infrastructure renaissance is gathering momentum at a pace unseen in recent history." The Markdown split came from the column break.
- **Risk cube (p49).** A 3-D cube. Its faces are the three "Risk Classification" layers: **Policy Risks, Macro Risks, Execution Risks**. An arrow band gives three "Evaluative Parameters": **Impact → Likelihood → Time**. The lead-in reads: "Think of risk as a three-layer cube: macro weather fronts, policy crosswinds, and execution stalls."
  - p50 then shows "Risk classification: Three-dimensional thinking", with two example boxes per layer: currency volatility and interest-rate instability (macro); incentive reversals and election-cycle resets (policy); permitting and licensing delays and utility unreliability (execution).
- **Risk matrix (p51).** Parameter × High / Medium / Low, with a navy header row. **The Red/Amber/Green scale is text only:** "Red: <12 months / Amber: 1–3 years / Green: >3 years". The cells are not colour-coded.
- **Country photos** are decorative skyline photographs with no data:
  - Indian city at night (p14);
  - Jakarta, with the Selamat Datang monument (p17);
  - Ho Chi Minh City (p20);
  - Bangkok (p23);
  - Kuala Lumpur, with the Petronas Towers (p26);
  - Manila (p29).
- **Country-chapter template, identical for all six markets:**
  1. Skyline photo.
  2. Country name.
  3. A **one-row scorecard strip**: eight cells for the seven pillar scores plus the final score, with a weight row.
  4. Macro snapshot / Policy trends paragraphs.
  5. "What works and what doesn't" (Strengths | Risks), with a navy header.
  6. "Opportunity window" (Program | Scale and scope | Timeline and business context).
  7. A navy **"Why now? + tagline"** band.
  8. "Industrial themes in play" (three icon bullets).
- **The six taglines,** which the Markdown did not attach to their countries:
  - India, "The broad frontier growth engine";
  - Indonesia, "The localization fortress";
  - Vietnam, "The export sweet spot";
  - Thailand, "Final boarding for incentive express";
  - Malaysia, "Logistics and energy transformation underway";
  - Philippines, "Catching the infrastructure crest".
- **Case openers** use brand logos over photos: Daikin (p40) and Schneider Electric (p42).
- **Confirmed:** P1 has no "ycp.com" footer and no author emails, and its back page reads "Copyright © 2025".

### 1.5 P10 *Unlocking India's Nuclear Sector*

**p43 "Bridging the Nuclear Capacity Gap".** A header band runs from **LAW (SHANTI Act)** to **ENERGY REALITY (Functional Market)**. Below it are six columns, one per Chapter 4 challenge cluster, each with its flagship fix:

| Challenge cluster | Mechanism shown | One-line effect (as printed) |
|---|---|---|
| Market Entry and Institutional Framework | Dedicated Strategic Services Agency (DSSA): from "Legal Shell" to "Functional Market" | "Acts as a technology custodian and liability firewall to protect foreign reactor IP." |
| Regulatory Friction and Operational Realities | Shift to a "Design Certification" Model (a Years → Months arrow) | "Separates site approval from reactor design to compress licensing from years to months." |
| Commercial Viability and Long-Term Sustainability | Product Inspection → Process Qualification | "Enables self-certification for qualified vendors to eliminate manufacturing bottlenecks and idle time." Plus a box, "Fiscal Interventions for Project Returns": **GST Zero-Rating** (removes 18% tax on reactor equipment; 20–30 paise lower per-unit tariff), **Heavy Water Leasing** (capex to opex), **Nuclear PLI** (4–6% incentive on incremental sales) |
| Financial Risk Architecture for Bankability | Nuclear Catastrophe Bonds & Proxy Insurance | "Solving the 'Hot Zone' Insurance Gap … transfer risk to capital markets." |
| Strategic Dependencies and Supply Chain Resilience | Guaranteed Access: Sovereign Nuclear Fuel & Material Banks | "Aggregates demand for critical materials and guarantees fuel access via leasing models." |
| Social License and Human Capital | From CSR to Shared Prosperity | "Grants host communities equity stakes or free electricity to build long-term social license." |

- This one page is the **best single-exhibit summary of a "challenge → named mitigation" chapter in the set.** It is a direct model for a China Playbook failure-mode or remedy summary (see §5).
- **Caveat:** "Nuclear PLI 4–6%" is a *proposal*. The text on p41 says, "There is no Production Linked Incentive (PLI) scheme for nuclear heavy manufacturing." The exhibit does not mark it as proposed.

**p48 "Market Segmentation and Strategic Positioning of Private Participants".** Two tiers sit around an atom icon:

- **Lead Project Adopters & Operators:**
  - Large Energy Majors and IPPs: "Anchor grid-connected projects by absorbing construction risks and managing long-term assets."
  - Hard-to-Abate Industrial Players: "Implement captive, behind-the-meter nuclear solutions…"
- **Delivery, Supply, and Financial Enablers:**
  - EPC and Infrastructure Specialists: "Drive fleet-mode deployment and cost efficiencies using nuclear-certified quality systems…"
  - Specialized Manufacturers & Supply Chain: "Build domestic depth through heavy forgings and precision components via long-term strategic partnerships."
  - Financial Institutions & Asset Managers: "Provide stable, long-duration capital to lower costs and enable developers to recycle equity."

Named Indian firms appear only in the text on p49 (e.g. NTPC, Tata Power, Adani Power, L&T, Godrej & Boyce). **The two-tier "adopters vs enablers" split is a useful device for the China Playbook's reader groups** (OEMs and incumbents vs dealers and financiers).

**Other P10 checks:**

- **Timeline (p25), genuine errors confirmed.** It prints "1964" for the Atomic Energy Act (the text on p26 says 1962). Its 2025 node says the acts were "substantially amended under the SHANTI Bill", while p26 says the Act "repealed both".
  - Timeline nodes: 1964; 1969 Tarapur; 1983 AERB; 2008 Indo-U.S. agreement and NSG waiver; 2010 CLND Act; 2024 100 GW target and BSR tender (16 sites); 2025 SHANTI.
- **Printed typos, all genuine:**
  - "the form sources" (p11);
  - "~INR 5 Cr/MW" for the PFBR (p15);
  - "INR 25-30/ MW" for the BSMR (p15), which is missing "Cr".
- **Exec-summary exhibits (p4), which the Markdown flattened:**
  - A timeline in two halves: "1947–2025: Seven Decades of Foundation" and "2025–2047: Two Decades of Radical Scaling". It runs from 8.88 GW (2025) to 22.5 GW (2032 target), 67.4 GW (2042) and 100 GW (2047), with ">90 GW needed in just 22 years" and "~20 lakh crore (~USD 210 billion)".
  - An A–G opportunity wheel.

### 1.6 P5 *SEA IPO Landscape*: Table 1 scores, and why the verdict does not follow

**Table 1 "Comparative Scoring of Funding Options" (p6).** Scores are Harvey balls: ¼ = Very low, ½ = Low, ¾ = Moderate, full = High. The "Final Verdict" column is shaded.

| Option | Capital Scale | Cost of Capital | Control / Dilution | Flexibility & Speed | **Final Verdict** |
|---|---|---|---|---|---|
| Bank Loan | Low | Moderate | Very low | Moderate | **Moderate** |
| M&A | Moderate | High | High | Low | **Low** |
| Bond | Low | Moderate | Very low | Low | **Moderate** |
| IPO | High | Moderate | Moderate | Low | **High** |

Source: "YCP Research & Analysis" (below the table, left).

**New finding: the verdicts cannot be reproduced.** The text says options are scored "from least favorable [to] most favorable" and the verdict is "the weighted composite score". The word "to" is missing in the original.

- **With equal weights** (Very low = 1 … High = 4), the totals are Bank Loan 9, M&A 13, Bond 8 and IPO 12. M&A scores highest yet is ranked **Low**, and it beats Bank Loan on three of four criteria yet ranks below it.
- **If "High" cost of capital or dilution means *worse*** (a natural reading), the totals become Bank Loan 11, M&A 7, Bond 10 and IPO 10. IPO is then no longer top.
- **Either way** the verdict depends on weights that are not disclosed and on a criterion direction that is not stated.

This strengthens the baseline's "undisclosed weights" point. **It is the clearest example in the set of why the China Playbook must publish weights and criterion direction if it scores anything** (baseline Rec. 10).

**Other P5 corrections:**

- **Table 5 (p18) has no empty rows.** Steps 5–10 share one merged right-hand cell with three bullets ("Monitor regulatory filings…", "Oversee consistency of disclosures…", "Track readiness for listing…"). The Markdown split the merged cell, so the baseline item is **withdrawn**.
- **The data note on p7 reads "year-to-date"** (hyphenated at a line break). The baseline's "original spelling: year-todate" is **withdrawn**.
- **Figure 2 (p11) consequence codes are coloured squares:** R = orange (Regulatory = Disclosure Risk), V = bright blue (Valuation = Investor Confidence Risk), T = navy (Timeline = Execution Risk). There are 11 readiness factors (3 / 3 / 3 / 2).
- **Genuine faults confirmed:**
  - Figure 1 (p7) is never narrated in the text. It shows stacked IPO counts by country (Malaysia navy, Singapore royal blue, Thailand light blue, Vietnam teal, Indonesia grey) with a funds-raised line, 2016–2025.
  - The Singapore board-lot contradiction (p8).

### 1.7 P7 *India's Logistics Industry*: the matrices

**Archetype × segment map (p42).** Legend: navy = Primary, bright blue = Secondary, light blue = Limited, grey = No presence. The three logistics-centric columns are ringed and captioned "The logistics-centric segments are the focus of this white paper".

| Archetype | Transportation Infrastructure | Peripheral Infrastructure | Distribution Infrastructure | Logistics Services |
|---|---|---|---|---|
| Infrastructure Developers | **Primary** | Secondary | – | – |
| Inland Container & Logistics Operators | – | **Primary** | Secondary | Secondary |
| Infra-Backed EXIM Service Providers | Limited | Secondary | Secondary | **Primary** |
| Logistics Providers | – | – | **Primary** | **Primary** |
| Pureplay Service Providers | – | – | – | **Primary** |
| PE-Led Platforms | Limited | Limited | **Primary** | Limited |

**M&A attractiveness heat map (p49).** The Markdown missed this completely. Legend: green = High, yellow = Medium, pink = Low. Rows are acquirer types; columns are target ownership types.

| Acquirer ↓ / Target → | Family-Owned | Conglomerate logistics arms | PE-Backed | Venture-Backed |
|---|---|---|---|---|
| Global logistics cos | High ("Local market access through potential of complete ownership in a few years") | High ("Collaborations likely to be led by partnership") | High ("Local market access through institutionalized mid-sized players") | Medium ("Tech enablement…; acquirer likely to be Indian subsidiaries of global companies") |
| Domestic logistics cos | High ("Consolidation potential with deep local expertise") | **Low** ("Low probability of acquisitions, as these targets tend to be well-funded") | Medium ("Increase in market share in a specific niche/geography; valuations may be high") | High ("Tech enablement and differentiation") |
| Financial players | High ("Platform build-up: consolidation and upside from institutionalisation") | Medium ("Investors are likely to take a small stake…") | High ("Ownership likely to shift to later-stage investors") | Medium ("High valuation growth potential") |

**M&A pitfalls grid (pp50–51).** Headed "Considerations and Pitfalls to Look Out For in M&A". It covers five target types across four diligence areas. Each area opens with an italic "what to check" band that spans all columns, followed by pitfalls specific to each target type.

- **Market & Competitor Assessment.** Check band: SAM/TAM, revenue and profit pools, growth projections, peer set, value proposition.
  - Family-owned: "Business model shaped by promoter relationships rather than market benchmarks".
  - Conglomerate arms: "Market position inflated by captive group volumes"; "Compete under internal cost structures, not market rates".
  - PE-backed: "margins under pressure due to aggressive pricing".
  - Venture-backed: "TAM frequently overstated".
- **Customer Assessment.**
  - Family-owned: "Customer stickiness driven by personal promoter relationships… churn risk post-acquisition is material".
  - Conglomerate arms: "Revenue risk after separation".
  - PE-backed: "Short-term contracts with downside risk".
  - Venture-backed: "Heavy focus on customer acquisition, often discount-led".
- **Leadership and Talent.**
  - Family-owned: "Decision-making centralized with promoter".
  - Large corporates: "Local teams constrained by global HQ".
  - PE-backed: "stress between founder versus PE on decision making".
  - Venture-backed: "Founder-dependent execution… high talent churn".
- **Value Creation.** Check band: "Thesis must clearly articulate synergy hypothesis, e.g.: Consolidation / Geographic expansion / Customer access / Capability acquisition".
  - Conglomerate arms: "Synergies overstated due to captive volumes; one-time separation costs often underestimated".
  - Venture-backed: "Dependence on continued funding (cash runway risk)".

**Why this matters for the China Playbook:** the "check band + pitfall per counterparty type" format transfers directly. A dealer-network or JV-partner diligence grid by partner type (family distributor, listed dealer group, conglomerate, Chinese OEM's own subsidiary) would reuse it one for one.

**New and corrected items for P7:**

- **New: the ownership-type columns drift across three consecutive exhibits.** p48 lists five target types (including "MNCs/Corporates"); the p49 heat map uses four (it drops large corporates); pp50–51 use five again, as "Large Logistics Corporates".
- **Artefact: the "duplicated paragraph" (p35) is printed once.** The copy is only in the text layer (§0.1), so the baseline item is **withdrawn**.
- **New: the p35 stacked chart has no legend.** "Grade A Warehousing Stock (Million Sq Ft)" shows 60 + 28 = 88 (2019), 148 + 90 = 238 (2024) and 360 + 260 = 620 (2030), but the two stack segments are unlabelled. The running header on p35 is also overprinted by the photo.
- **Genuine: truck distance.** The p29 chart shows India 287 km/day (USA 750, Europe 650, China 550), while the text on p28 says "300".
- **Genuine and visible: the p59 About Us page.** Its header shows P4's title ("From Strategy to Execution: Change Management as the Engine of Operational Transformation") and its body describes the Supply Chain Solutions Division.

### 1.8 P13 *Sustainability Governance*: board-model chart (p16)

The chart is titled "Board-Level Sustainability Governance: A Spectrum of Models" and has six navy-gradient bars:

| Model | Share of companies | Label on chart |
|---|---|---|
| Embedded in Governance | **31%** | "Most effective for long-term ESG accountability" |
| Standalone ESG Committee | **20%** | Transitional structures, "each can evolve towards fuller integration" (bracket spans the middle four bars) |
| Layered onto Existing Committee | **10%** | (as above) |
| Distributed Across Committees | **10%** | (as above) |
| Individual Board Advocate | **15%** | (as above) |
| Ad Hoc / Informal Oversight | **12%** | "Highest governance risk – limited board-level accountability" |

- **The call-out is consistent with the numbers.** "Our assessment of client boards finds a similar distribution to broader industry surveys, with the majority of companies still operating in transitional or informal oversight structures": transitional 55% plus informal 12% gives 67%.
- **New: the shares total 98%,** with no rounding note.
- **New: YCP's data is not separated from the benchmark.** The source note, in the left margin, reads "Based on our analysis of board governance practices. Industry benchmarks referenced from BCG - INSEAD Board ESG Pulse Check (March 2022)". The chart does not show which figures are YCP's client data and which are the benchmark's, and it gives no sample size.
- **New: the paper ranks the models two ways.** The p15 table calls Distributed Across Committees "The preferable practical pathway for most companies", while the p16 chart labels Embedded in Governance "Most effective".
- **Downgraded to hidden layer:** the p15 "garbled header" is P4's title in white (§0.1). p15 also lacks the ycp.com footer.
- **New typo:** "Prefixes sustainability into key business contexts" (p15, probably "Embeds").
- **Genuine, confirmed:**
  - Stage 1 list numbered off by one (p29: the intro sentence is item 1);
  - "accountability of diffusion" (p29);
  - the "ultimate objective" sentence repeated on p17 and p23.
- **Maturity curve (p27):** a stepped staircase on Governance Engagement (y) × Organizational Capability (x). The stages darken from Stage 1 "Emerging – Invisibility Problem" (navy) to Stage 4 "Leading – Complacency Problem" (light blue).

### 1.9 P3 *Transportation Economy*: Figure 4 (p32)

The operator names are logos:

| | Airports Authority of India | GMR | Adani | Fairfax | Zurich Airport |
|---|---|---|---|---|---|
| Airports operated in India | 110 | 4 | 7 | 1 | 1 |
| Notable airports | Chennai, Calcutta | Delhi, Hyderabad, Goa, Nagpur | Mumbai, Ahmedabad, Jaipur, Navi Mumbai | Bangalore | Noida (second airport in Delhi) |
| Passengers served | 130m (FY24) | 103m | 89m | 41m | 12 MPPA capacity, "to be operational in 2025" |
| Presence in India | ~30 years | ~20 | ~5 | ~8 | ~5–10* |

*"First entered Indian market in early 2000s but exited; recently entered in 2019." Source: YCP Research & Analysis.

- **New, genuine text–figure conflicts:**
  - The text says GMR has "three major international airports (Delhi, Hyderabad and Goa)"; the figure says 4.
  - The text says Adani operates "six brownfield airports"; the figure says 7.
  - "To be operational in 2025" is stale in a February 2026 paper.
  - The table uses logos only, so it cannot be read by text extraction or screen readers.
- **Corrections to the baseline:**
  - **Source-line placement:** P3's sources sit in the **left margin beside the exhibit, under a short blue rule**, not above the tables. Only the title sits above.
  - **"Passanger" appears three times:** twice in Table 4's column headers (p16) and once in the Figure 4 title (p34).
  - **Figure order on p35:** Figure 6 appears before Figure 5.
  - **The Japan chapter (pp8–13)** has no data exhibit, as the baseline said.

### 1.10 P2 *Indonesia's Oil and Gas*: conclusion (p17)

The layout is clean: a two-column navy page.

1. Kicker "Conclusion:" and title "Building a Resilient Energy Future".
2. Introduction.
3. **Column 1:** "Shared Commitment Among Key Players" (Industry / Government / Investor bullets), then "Moving From Fragmentation to Synergy".
4. **Column 2:** the Central Energy Competitiveness Council paragraph, then "The National Imperative" (energy security and self-sufficiency; economic diversification; energy transition and climate commitments).
5. Closing sentence: "…can pivot from a heritage of challenges to a future marked by resilience, sustainability, and global competitiveness…"

The Markdown interleaved the two columns.

**Other P2 checks:**

- **Genuine:** "Nelson Complexity Index is -5 (below regional peers in 9-10)" is printed in the PDF (p11). It is probably meant to be "~5".
- **Refining, a correction:** the value-chain graphic (p7) places Refining **only under Downstream**, while the text on p6 defines "Midstream (transportation, refining, and processing)". So this is a text-vs-graphic conflict, not "refining listed twice on p7".
- **p7 investment bars (USD bn, 2020–24):** upstream 11 → 15 (+10%), midstream 2 → 4 (+19%), downstream 2 → 5 (+26%). The source, "American Fuel and Petrochemical Manufacturers", is confirmed as mismatched.
- **p8 waterfall (KBPD):** crude lifting ~500 plus imports ~350 give refinery intake ~850. Refinery output ~800 (marked in red as the "Critical Gap"), product imports ~500 and FAME/LPG ~200 reach end customers at ~1,500. The chart is badged "Illustrative" and sourced to the Directorate General of Oil & Gas. **Red is used only for the gap, which is a disciplined use of an alert colour.**

### 1.11 P15 *Source-to-Pay*: services graphic (p23)

A navy panel titled "Digitization" with a chip illustration and five service boxes:

- **Source-to-Pay Digitization:** Requirements Gathering; Process Design & Mapping; Configurations & Integrations.
- **Expense Management Digitization:** Testing, Training & Deployment; Annual Maintenance & Upgrades; Helpdesk Support.
- **Change Management:** Stakeholder Adoption & Capability Enablement; Transformation Governance & Post-Go-Live Support.
- **Sustainability Digitization:** Adoption & ROI Capture.
- **Procurement Digital Transformation:** P2P Platform Implementation & Process Digitization; Advanced Spend Analytics & Intelligent Automation.

The text above it claims "57+ implementations" and "Since 2016".

- **New:** the three bullets under "Expense Management" are generic implementation services, not expense-specific, so they are probably mis-grouped.
- **Artefact, retracted:** "7085%" (baseline P15 weaknesses). p9 prints "Automates 70-85% of manual tasks end-to-end" across a line break.
- **Genuine:**
  - Cases 1–3 have no numbers under "Quantified Impact". Case 3's "100% visibility into contract lifecycles" describes a state, not an improvement.
  - The six case pages (pp27–38) are full navy pages and are not in the TOC.

---

## 2. Other baseline statements corrected by the PDFs

| Baseline statement | Correction |
|---|---|
| "Standard legal disclaimer on the **inside cover** (15/16)" | The disclaimer is small print at the **foot of the front cover** in 15/16 papers. P16's cover carries its own scope-and-currency statement instead. |
| "Table of contents with page numbers 15/16 (P16 empty)" | **16/16.** |
| "Running header … 15/16 (not visible in P16)" | **16/16.** The running header is a thin rule above and below the full title, top left. |
| P16 "no page numbers", "n/a" printed pages; cited "by section" | Printed pages 2–28, 30 PDF pages. P16 joins the **short cluster** (8 short papers, not 7). |
| P16 weaknesses "TOC empty; Implication boxes empty"; "Contest 4 lists B before A" | Withdrawn (§1.2). |
| P11 "conclusion corrupted" | Printed conclusion clean; hidden P8 text layer (§1.3). |
| P5 "empty rows in Table 5"; "year-todate" | Withdrawn (§1.6). |
| P7 "duplicated paragraph (p35)" | Hidden layer only (§1.7). |
| P13 "running header on p15 garbled" | Hidden white text only (§1.8). |
| P15 "typo 7085%" | Artefact (§1.11). |
| P1 "exec summary first sentence split" | Artefact (§1.4). |
| P4 "six client vignettes" | **Seven** (North America, South America, Europe, three in Asia, Middle East). **Five of the seven "Client Quote" cells are empty.** Only North America and Middle East have quotes, and the Middle East row has two. The Europe row and the first Asia row report qualitative results only. |
| P14 "which title belongs to whom is ambiguous" | Resolved (§1.1). |
| P2 "Refining listed twice … (p7)" | Text-vs-graphic conflict (§1.10). |
| P3 "Source lines sit above tables" | Left margin (§1.9). |
| Source-line placement "below a chart (P1, P2), above a table (P3, P5), side margin (P9, P14)" | **The house default is the left margin, beside the exhibit, under a short blue rule, in italic grey:** P3, P4, P8, P9, P12, P13, P14. The exceptions are **below the exhibit** in P1, P2 and P5 (Table 1). P10 has few source lines, all in the margin. |

---

## 3. Visual design: what the Markdown could not show

The original brief asked for layout and exhibit conventions. The baseline could report colour only where a paper named it. From the renders and the PDF font and colour data, the house identity is below.

### 3.1 House visual identity (15 YCP papers; P16 follows it too)

| Element | Convention | Variation |
|---|---|---|
| **Page** | A4 portrait (595 × 842 pt), single column of body text inset from the left, generous white space | P1's exec summary (p3) and P2's conclusion (p17) use two columns |
| **Typography** | **Palatino Linotype** (serif) for titles, chapter heads and exhibit titles; **Segoe UI / Yu Gothic UI** (sans) for body, tables and labels. The same pairing appears in every paper | P10 adds Raleway and Poppins in graphics; P6, P7, P9, P11 and P13 have Minion Pro in places |
| **Palette** | Navy (~#001C44 / #0D1E43) for headings and dark panels; bright "YCP blue" (~#007FFF / #198CFF) for kickers, sub-heads and highlights; royal blue (~#1423A8) for the page-number tab; pale blue fills for table zebra rows and call-outs; white page ground | Non-blue colour is rare and purposeful: **red** for the P2 "Critical Gap"; **orange** for P5's R code and India on P7's FTA map; **green/yellow/pink** only on P7's heat map (p49). The blue-to-grey legend of P7 (p42) shows that intensity scales stay in blue |
| **Cover** | Navy panel with a blue-toned photo in a rounded frame, YCP logo top left, month–year pill top right, title in Palatino with a blue kicker line; disclaimer small print at the foot | YCP Renoir papers (P4, P8, P11) carry the "YCP Renoir" logo |
| **Running header / footer** | Header: full paper title between two thin rules. Footer: **royal-blue square page tab bottom left**, "ycp.com" bottom right | P1 and P2 (Dec 2025): title and page number, no ycp.com |
| **Section openers** | Two patterns: (a) a full-width **navy→blue gradient band** with a white Palatino title and a lead paragraph; (b) a **full-bleed photo** with the title in a white panel or on navy | P16 uses AI imagery on divider pages |
| **Headings** | Blue "Kicker:" plus a navy remainder ("Introduction: IPOs in…"; "Thailand: The Social Commerce Powerhouse") | — |
| **Exhibit title** | Palatino, **underlined with a thin navy rule**, left-aligned above the exhibit ("Table 1. Comparative Scoring…") | — |
| **Tables** | Navy→royal-blue gradient header row with white bold text; pale-blue zebra rows; thin blue rules | P14 uses darker navy tables |
| **Call-outs** | Navy→blue gradient boxes with white text for "Key Insight", "Opportunity:", "Implication", "Why now?" and pull quotes. Pale-blue panels for "Key Takeaways". Tabbed labels for Context / Implications / Government & Industry Response (P7) | — |
| **Charts** | Navy bars with a bright-blue highlight on the focus bar; CAGR shown in a blue bubble with an arrow; values printed on the bars; few gridlines | — |
| **Icons** | Blue line icons in circles or rounded squares for lists (principles, pillars, drivers) | — |
| **Photography** | Stock: city skylines, glass facades, ports and ships, handshakes, abstract blue data or network imagery. **Photos never carry data**, except P3's MOU signing (p25) | — |
| **Back matter** | "Authors" in large Palatino with square photos, name, blue title, email and bio; "Our Offices" on navy with the YCP roundel watermark; a white back cover with the logo and "Copyright © [year]" | P5 adds a Contributors page (seven photos) |

**What this means for the China Playbook:** the house template already standardises type, colour and page furniture. The things that vary, and so need an explicit decision, are **exhibit numbering, source-line position, and whether colour carries meaning.** Colour-coded scales are rare but effective when used: P5's Harvey balls, P7's four-level presence map, P7's traffic-light heat map and P5's R/V/T codes.

### 3.2 Colour-coded encodings found in the PDFs

None of these survived the Markdown.

| Encoding | Paper, page | Levels | Assessment |
|---|---|---|---|
| Harvey balls | P5, p6 | Very low / Low / Moderate / High | Compact, but the criterion direction is ambiguous (§1.6) |
| Blue-intensity presence map | P7, p42 | Primary / Secondary / Limited / None | Stays on-brand; readable in greyscale |
| Traffic-light heat map | P7, p49 | High / Medium / Low | Clear, but it is the only off-palette colour in the paper |
| Coloured letter codes | P5, p11 | R / V / T | Ties each factor to a consequence at a glance |
| Red "critical gap" accent | P2, p8 | One alert colour | A disciplined way to use red |
| Stage staircase darkening | P13, p27 | Four stages | Darkness implies severity, so the least mature stage is darkest |
| RAG in words only | P1, p51 | Red / Amber / Green thresholds | The colour is named but not applied, a missed opportunity |

### 3.3 Exhibit counts, recounted from the page renders

"Exhibit" here means any chart, table, diagram, map, stat-tile group or framework graphic. Decorative photos are excluded. Counts are ± about 10%.

| Paper | Baseline estimate | PDF count | Notes |
|---|---|---|---|
| P1 | 35–40 | **~45** | Includes 30 repeated country panels (5 per country × 6); numbered only Figures 1–3 |
| P2 | ~6 | **~7** | Twin chart, value chain with bars, waterfall, barriers table, 6 stat tiles, 5 imperative cards |
| P3 | ~25 | **~27** | 17 numbered (Tables 1–8, Figures 1–9 with two duplicates) plus ~10 unnumbered (TOD phase diagrams, entry-paths diagram, three-phase panel) |
| P4 | ~4 | **~7** | Figure 1 (a nested staircase: Procedural 3 + Behavioral 3 + Cultural 2 = eight stages), Figure 2, the three-column stages page (p19), the quote box, the 3-page results table, icon lists |
| P5 | 9 | **9** | Tables 1–6 and Figures 1–3; Table 6 is a roadmap graphic, not a table |
| P6 | minimal | **~8** | One true table (p38); flag-icon country lists; example boxes; Foxconn pull quote. No charts |
| P7 | ~30 | **~45** | ~20 charts, 3 maps, ~12 tables and matrices, ~10 claim banners with "Categories getting impacted" icons |
| P8 | ~5 | **~6** | Figure 1, two industry tables, outcome tiles, journal boxes |
| P9 | 3 | **3** | Confirmed |
| P10 | ~15 | **~18** | Adds the p4 wheel, the p7 three-stage program graphic, the p23 privatisation wheel and the p25 timeline |
| P11 | ~4 | **~7** | Trends panel, five-step band, TMO icon list, four-drivers cards, results tiles |
| P12 | ~15 | **~19** | Six country tile trios, plus tables and process graphics |
| P13 | ~5 | **~10** | Eight-duty icon list, comparative table, board-model chart, disclosure table, maturity curve, four failure-mode banners |
| P14 | ~25 | **~35** | Most pages pair a chart with side annotations and a "Key Insight" |
| P15 | ~10 | **~14, plus 6 case layouts** | |
| P16 | few | **~12** | Hypotheses table, verdict-scale icons, verdict table, 5 implication boxes, 4 contest panels, pull quote |

**Revised density benchmarks for the China Playbook (about 50 pages):** P10 has about 18 in 52 pages, P14 about 35 in 48, and P7 about 45 in 59. The baseline's target of about 22 exhibits is at the **low end** of the long, research-led papers. **About 25–30** is closer to house norms for the long papers (P3, P7, P14).

### 3.4 Other visual details the Markdown dropped

- **P1:** the "Why now?" bands are navy with white text; the scorecard strip sits at the top of each country chapter; appendices pp52–55 are on navy.
- **P3:** the Delhi Aerocity case (pp36–37) uses a full-height Qutub Minar photo and then a full navy page. Stakeholder-flow diagrams (pp19–21) label arrows with what flows (support, resources, services).
- **P7:** "Key Takeaways" (pp32, 40, 52) sit on a pale-blue panel. There are three maps: trade routes (p16); an FTA world map (p17: orange = India, navy = FTA concluded, blue = ongoing, grey = none); and MMLPs and port-linked terminals (p34).
- **P8:** Figure 1 (p8) is "The Operational Excellence Journey". It runs STRATEGY → Operational Excellence Transformation Journey → RESULTS.
  - **Core Technical Enablers:** Processes, System, Structure, Competencies.
  - **Core Tactical Approach:** Awareness → Buy-In → Adoption → Ownership.
  - **New:** these four enablers do not map onto the text's **five** pillars (MCS, Processes, Organisation, Digital, People), which adds another label-drift case.
  - Outcome tiles (p19): +5–15% revenue, +20–40% throughput, +10–35% productivity, ≥3:1 ROI, 5–15% cost reduction. No basis is given.
- **P9:** the China–APEC trade chart (p9) shows 2016 2.4, 2017 2.7, 2018 3.0, 2019 2.9, 2020 3.0, 2021 3.9, 2022 3.9, 2023 3.6, 2024 3.7 and 2025E 3.8 (USD tn). **New:** it sits under the heading "U.S. Market: Concentrated Growth in a Narrow Set", so the exhibit and the heading do not match.
- **P12:** the TikTok Shop GMV table (p22) has three **new** problems:
  - The text says "Every major SEA market posted triple-digit growth", but the Philippines shows +99% and Singapore "—".
  - The country values sum to about USD 39–45bn, against a stated regional total of USD 45.6bn.
  - Thailand is called "Second-largest globally" (p22), while Indonesia is "second-largest … after Thailand" (p19) and the largest in the same table. The Indonesia/Thailand ranking conflict is therefore three-way.
  - Two cells of the Regional Overview (p18) are "2h+ est.".
- **P12, P13, P14:** source lines sit in the left margin under a short blue bar, in italic grey.
- **P14:** p7 is a "Key Insight" page with four tiles (Historic Turning Point 2024; U.S. Market Precedent; Driver of Reform; Collapse of Entry Barriers) and a blue Key Insight bar. The **Fuji Soft case (p33)** is on a navy page with a "PE Market Response and Ecosystem" flow diagram and a KKR deal bar.
- **P15:** "Key Takeaways" panels (pp8, 12, 15, 18, 21, 26); a roadmap chevron (Assess → POC → Scale → Optimize, p13); a benchmark strip (5 days PO cycle time, 65% spend under management, 40% fully automated invoices, p21).

---

## 4. Net effect on the baseline's cross-paper findings

| Baseline finding | Change |
|---|---|
| "Production or template errors ≥8 papers" | Split into **visible** errors (P3 duplicate figure numbers; P6 misplaced paragraph; P7 wrong About page; P13 list numbering; P14 TOC/body mismatch; P15 cases missing from the TOC; P16 duplicated and missing Perspective Break labels) and **hidden text-layer leftovers** (P7, P11, P13). P5 leaves the list. |
| "Internal numbers that disagree: 9 papers" | Unchanged in count. The PDFs add new cases: P3 (GMR 3 vs 4, Adani 6 vs 7), P12 (GMV table vs text and total), P13 (98% total). |
| "Labels or framework counts drift: 7 papers" | Add P7 (ownership-type columns across pp48–51). P8, already listed, gains a second case (four enablers in Figure 1 vs five pillars in the text). P16's Contest-4 order is withdrawn, but P16 stays in the list for its Perspective Break labels. **Now 8 papers:** P1, P2, P4, P6, P7, P8, P14, P16. |
| "Opaque scoring: P1, P5, P13" | Strengthened. P5's verdict cannot be reproduced from its own scores. P13's chart mixes client data with a 2022 benchmark and does not total 100%. |
| "Exhibits unnumbered or inconsistently numbered: 15" | Unchanged. |
| "Source line on most exhibits: 3/16 (P3, P12, P14)" | Unchanged (confirmed by counting source lines in the text layer). |
| Exhibit-density benchmarks | Raised (§3.3). |
| Ranking of best papers | Unchanged. P10's p43 bridge exhibit strengthens its #1 place. P7's matrices, now readable, strengthen its #2 place. P16's method and implication boxes strengthen its #3 place, and its "empty TOC" weakness is withdrawn. |

---

## 5. Additions to the China Playbook recommendations

These add to the baseline's Step 3; they do not replace it.

1. **One exhibit that bridges challenges to fixes (extends Rec. 7).** Close the failure-modes chapter with a single page in the style of P10 p43: six columns, one per failure mode, each giving the named mode, the named remedy, and a one-line effect. Mark any remedy that is a proposal rather than existing policy (P10 did not; see §1.5).
2. **Declare colour semantics once and reuse them (extends Rec. 12).**
   - Keep the house blues for intensity scales (Primary / Secondary / Limited / None, as in P7 p42).
   - Reserve one alert colour (red, as in P2 p8) for "structural threat" or "time margin < 12 months".
   - Apply RAG as actual colour, not just words (P1 p51 named it but did not apply it).
   - For verdict tables (structural vs cyclical), use a five-step blue scale with the "Inconclusive" step in grey.
3. **If anything is scored, publish direction as well as weights (extends Rec. 10).** P5 shows that a Harvey-ball grid without criterion direction and weights produces verdicts that readers cannot check. State for each criterion whether "high" is good or bad, publish the weights, and show the composite score next to the verdict.
4. **Keep client data and benchmarks separate in any chart (extends Rec. 9).** P13 p16 does not. If the China Playbook uses YCP client or field observations, show them as a separate series with n and date, next to the public benchmark.
5. **Use counterparty-type diligence grids (extends Rec. 6).** P7's p49 heat map and pp50–51 pitfalls grid are a ready template for the dealer, JV-partner and acquirer sections. For example: rows are acquirer or partner types (incumbent OEM, Chinese OEM, dealer group, financier); columns are target types; each cell has an attractiveness rating and a one-line rationale; then check bands and pitfalls by type.
6. **Use a two-tier reader map (extends Rec. 6 and §3.0).** P10 p48's "Lead adopters vs Delivery / financial enablers" split maps neatly onto the Playbook's audiences: CEOs, APAC and country heads, and strategy teams on one side; dealers, financiers and policymakers on the other.
7. **Set exhibit density to about 25–30 for a 50-page paper** (revises Rec. 12 and §3.4 of the baseline).
8. **Avoid logo-only tables.** P3's operator table cannot be read by text extraction or screen readers. Put company names in text, even where logos are shown.
9. **Add these pre-publication checks** (they are merged into the baseline checklist):
   - Extract the text layer of the final PDF and diff it against the approved copy. This catches hidden leftover frames such as those in P7, P11 and P13.
   - Check every chart has a legend for every series or stack segment (P7 p35 does not).
   - Mark every proposed (not yet enacted) policy as proposed, in exhibits as well as in text (P10 p43).
   - Check that parts sum to the stated total and that percentages sum to 100% or carry a rounding note (P12 p22, P13 p16).
   - Keep the column and category sets consistent across consecutive exhibits (P7 pp48–51).
   - Keep figure numbers in page order (P3 p35).

---

*All page references are printed page numbers, which equal PDF page numbers in all 16 files. Quotations are exact from the PDF text layer, checked against the rendered page.*
