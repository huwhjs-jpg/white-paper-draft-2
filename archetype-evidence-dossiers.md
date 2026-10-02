# The China Playbook: archetype evidence dossiers

Batch 2 evidence build, 1 October 2026. It builds on the 29 September draft, the fact-check files and the 1 October research run, and adds a 36-product UN Comtrade screen, an 11-year series for 15 products, company filings and two Indian trade-remedy cases. Free, publicly verifiable sources only. Every figure carries its source, and secondary sources are flagged.

---

## 1. What the evidence says, in brief

1. **Five archetypes, defined by who buys and how.**
   - Site and fleet equipment: the paper's reference case.
   - Plant utility equipment.
   - Production machinery.
   - Motion and power components.
   - Automation. It splits in two: robot arms, servo and PLC; and warehouse robots, AMRs and cobots.
2. **The biggest new finding is production machinery** (injection-moulding machines, machining centres, CNC lathes, laser cutters). This is not compressors and pumps.
   - Across India, Indonesia, Thailand and Malaysia, China's share of injection-moulding machine imports rose from 24% in 2015 to 60% in 2025. Japan's fell from 38% to 16%.
   - In CNC lathes China passed Japan in 2025.
   - The leading Chinese maker attributes its overseas growth to Chinese manufacturers investing abroad.
   - This is the clearest filing-level evidence anywhere in the paper for **following home-country customers**, which the v1 draft could only call plausible.
3. **Robots turned in 2025.**
   - China became a net exporter of industrial robots in 2025.
   - In the same year it overtook Japan as the largest source of robot imports in all four markets with 2025 data:
     - India: 34% against 30%.
     - Indonesia: 62% against 12%.
     - Thailand: 44% against 28%.
     - Malaysia: 40% against 36%.
   - The robot makers' own overseas businesses are still small or shrinking. Estun's overseas share fell from 34.1% to 29.9%. So the share is moving through hardware exports and integrators, not through Chinese-owned channels.
4. **High share invites trade cases earlier in mid-level machinery than in heavy equipment.** India imposed anti-dumping duties on Chinese industrial laser machines in December 2023 and on Chinese injection-moulding machines in June 2025.
   - Rates run up to 147.20% for lasers and 63% for injection-moulding machines.
   - Crane duties, by contrast, were recommended and never imposed.
   - Incumbents with Indian plants (Shibaura Machine India, Milacron India) were among the petitioners.
5. **"Same moves, different order" holds, but who the buyer is sets the order.**
   - **Factories buying production machinery or automation:** the beachhead is the Chinese-owned factory abroad. Local plants and service follow quickly, and so do trade cases.
   - **Plant engineers buying compressors and pumps through distributors:** price and channel come first and the system later. Here incumbents answer with fighter ranges.
   - **Warehouse robots and cobots:** these were born global. Their beachheads are developed markets, so India and Southeast Asia are follower markets.
6. **Customer credit (Learning 2) does not travel into mid-level products.**
   - We found no evidence of Chinese makers financing buyers of compressors, pumps, machine tools or robot arms in these markets.
   - It reappears in warehouse robots as subscription: Geek+'s subscription orders rose more than 75% in H1 2026.

---

## 2. Method

- **Trade data.** UN Comtrade public API (preview endpoint), reporter-reported imports by value, pulled through the browser on 1 October 2026.
  - The screen covers 36 HS codes across India, Indonesia, Thailand, Vietnam and Malaysia for 2015, 2019 and 2022–2025.
  - The series covers 15 codes for every year from 2015 to 2025.
  - The pull reproduces the paper's existing figures exactly, which validates it:
    - Thai pumps: 33.3% → 53.4%.
    - Indian compressors: 44.0% → 52.6%.
    - Indonesian excavators: 33.1% → 74.5%, and US$590.6m → US$1,248.8m.
  - Vietnam has not reported 2024 or 2025.
  - The preview's quantities are imputed, so we don't use them for unit values or prices.
- **Company and regulator evidence.** Annual reports and results announcements (HKEX, CNINFO, SSE, SZSE), company releases, DGTR findings and customs notifications, IFR releases, and the China customs administration via state media.
- **Grades.** These are the paper's existing evidence grades (Appendix C), applied to India and Southeast Asia:
  - **Strong:** regulator findings, filings or trade data show both the move and its effect.
  - **Moderate:** the move is documented, but its effect rests on company claims or indirect data.
  - **Weak:** there is little public evidence of the move.
- **Limits.**
  - HS codes are narrower than product families.
  - HS 847950 ("industrial robots n.e.s.") misses robots classified elsewhere, such as welding robots.
  - Import data show where a machine shipped from, not whose badge it carries.
  - No free source splits ASEAN robot installations by supplier country.

---

## 3. The trade screen: where China gained, and who lost

China's share of import value, value-weighted across the five markets, 2019 → latest year (2024; 2023 for Vietnam). Full tables are in `comtrade_screen.md` and `comtrade_series.md`.

| Archetype | Product (HS) | China, 2019 → 2024 | Who lost | Import value, latest |
|---|---|---|---|---|
| Site and fleet (reference) | Excavators (842952) | 28% → 58% | Japan | US$2.3bn |
| | Electric forklifts (842710) | 36% → 65% | Japan | US$0.56bn |
| Plant utility | Compressors n.e.s. (841480) | 34% → 46% | Japan 20% → 15% | US$2.6bn |
| | Portable compressors (841440) | 32% → 66% | Japan 21% → 6%; US 12% → 5% | US$0.15bn |
| | Centrifugal pumps (841370) | 38% → 48% | Japan 9% → 5% | US$1.2bn |
| | Large generator sets (850213) | 42% → 69% | Korea 9% → 2%; Germany 7% → 2% | US$0.8bn |
| Production machinery | Injection-moulding machines (847710) | 33% → 56% | Japan 31% → 19%; Taiwan 9% → 4%; Korea 8% → 3% | US$0.97bn |
| | Machining centres (845710) | 7% → 24% | Japan 50% → 41%; Taiwan 15% → 10% | US$0.79bn |
| | CNC lathes (845811) | 10% → 21% | Japan 46% → 26% | US$0.31bn |
| | Laser machine tools (845611) | 38% → 49% | Germany 13% → 9% | US$0.62bn |
| Motion and power components | Gears and gearboxes (848340) | 29% → 49% | Japan 21% → 14% | US$1.4bn |
| | Ball bearings (848210) | 36% → 45% | Japan 26% → 16% | US$1.6bn |
| | AC motors, 0.75–75 kW (850152) | 40% → 44% | Germany 17% → 14% | US$0.47bn |
| | Hydraulic motors (841229) | 9% → 21% | Japan 22% → 13% | US$0.4bn |
| | Hydraulic valves (848120) | 9% → 12% | — | US$0.55bn |
| | Industrial valves n.e.s. (848180) | 30% → 34% | — | US$4.0bn |
| Automation | Industrial robots n.e.s. (847950) | 25% → 32% | Japan 32% → 29%; Korea 16% → 11% | US$0.46bn |
| | Control panels incl. PLC (853710) | 29% → 43% | Japan 15% → 7% | US$5.7bn |
| | Small DC motors incl. servo (850131) | 44% → 52% | Japan 18% → 7% | US$1.3bn |

**Crossover years.** These are the years China passed Japan as the larger import source, value-weighted across India, Indonesia, Thailand and Malaysia (the four markets reporting every year from 2015 to 2025).

| Product | Crossover | 2025: China vs Japan |
|---|---|---|
| Compressors, pumps, laser machines, control panels | Before 2015 (China already ahead) | Compressors 48% vs 15% |
| Electric forklifts | 2017 | 72% vs 11% |
| Excavators | 2019 | 63% vs 20% |
| Other forklifts | 2019 | 74% vs 19% |
| Injection-moulding machines | 2020 | 60% vs 16% |
| Robots | 2025 | 42% vs 27% |
| CNC lathes | 2025 | 27% vs 26% |
| Machining centres | Not yet | 21% vs 45% |

**What the screen rules in and out.**
- Production machinery and automation show the largest and most recent shifts, so they earn a place in Chapter 3.
- Hydraulic valves and industrial valves barely moved, and neither has company evidence behind it. They stay out.
- Gearboxes and bearings moved, but the gearbox code also covers wind-turbine and EV gearing. With no listed Chinese champion abroad to anchor them, they stay in a supporting role.

---

## 4. Archetype dossiers

### A. Site and fleet equipment (reference case)

Excavators, cranes and forklifts are covered in draft v1 and stay the reference case. New data:
- China's share of excavator imports was 63% in 2025 across the four markets, and 73.4% in Indonesia.
- Electric forklifts reached 72%.

**The clock** (four phases):
- Probe: 2007–15.
- Beachheads: 2016–21.
- Push: 2022–24. Turning point 1 is 2022 at company level, when SANY's overseas share went from 23% to 45.7%. Exports passed home sales in units in 2023.
- Embed: 2025–26.

**CCMA unit series, now back to 2016** (domestic / export):

| Year | Domestic | Export |
|---|---|---|
| 2016 | 62,993 | 7,327 |
| 2017 | 130,559 | 9,672 |
| 2018 | 184,190 | 19,100 |
| 2019 | 209,077 | 26,616 |
| 2020 | 292,864 | 34,741 |
| 2023 | 89,980 | 105,038 |
| 2025 | 118,518 | 116,739 |

The export share was 7–11% of units from 2016 to 2020 and about 50% from 2023.

### B. Plant utility equipment: compressors, pumps, generator sets

**Who buys and how.** Plant engineers and contractors, through distributors. Energy cost and uptime decide repeat purchases, and the aftermarket is large.

**Position.**
- **Compressors.** China's share rose from 33% (2015) to 48% (2025) across the four markets. In India it has moved between 42% and 55% since 2015, and was 49.3% in 2025.
- **Pumps.** China's share rose from 28% to 53%. India is the exception, flat at 32–39% since 2015.
- **Portable compressors.** India jumped from 14% (2015) to 77% (2025).
- **Large generator sets.** Malaysia rose from 20% to 84% (2019 → 2024).

**The makers.** Chinese makers' overseas businesses are modest, and in these markets they are thin:
- **Kaishan.** About 50% of revenue is overseas, including geothermal. Its Indian unit sold about US$10m and 533 compressors in 2025. That is small against Indian compressor imports from China of roughly US$500m.
- **Nanfang (CNP).** About 19% overseas.
- **Lingxiao.** About 54% overseas.

The Chinese share of compressor imports is therefore mostly unbranded, OEM and low-end flow, not a few branded makers building channels.

**Clock: Beachheads moving into early Push.** No crossover is needed, since China was already the largest source. Branded channels and plants are only starting.

| Learning | Grade | Evidence |
|---|---|---|
| L1 Narrow beachhead | Moderate | Entry at the low-upfront-cost end. ELGi said the Chinese range "targets customers prioritizing low upfront costs over energy efficiency… typically served by Chinese products" (Q2 FY26 call summary). The portable-compressor niche in India rose from 35% (2019) to 78% (2024). |
| L2 Credit | Weak | No evidence found. |
| L3 Price, then lifecycle | Price: moderate. Lifecycle: weak | ELGi: "very low-cost compressors from China" at the bottom of the market (Aug 2026 call). There is no Chinese service network of note. Incumbents' aftermarket is the defence: ELGi earns 28–30% of India revenue from aftermarket, against 15–16% globally. |
| L4 Localise | Moderate | Kaishan India (2019; Mumbai facility "supports local manufacturing and testing"; 3,000 compressors supplied). Leo Pump Indonesia (wholly owned; Tangerang warehouse; about 12 distributors). Hanbell Bac Ninh (Vietnam, 2024, mainly service). CNP's first overseas service centre (Vietnam, 2024). Junhe's Thai plant (mass production by Nov 2025) and Taifu's Vietnamese plant look aimed at US and EU exports, so they are export bases, not host-market channels. |
| L5 Rules | Weak (rules act as barriers) | India rescinded the machinery Omnibus Technical Regulation (S.O. 239(E), 14 Jan 2026), which would have required BIS certification. A Pumps (Quality Control) Order was published in draft on 13 May 2025, covering 12 pump types; whether it has been finally notified is not confirmed. The hermetic-compressor QCO remains. |
| L6 Technology wedge | Weak to moderate | Energy efficiency and permanent-magnet motors. ELGi cut imported motors from 75–80% to about 5% and said Chinese motor prices had fallen below their metal cost (Feb 2026 investor meet). |

**Incumbents' responses.**
- **A fighter range on its own channel.** ELGi's low-cost tier was validated, took first orders, and launches in Hyderabad in September 2026. ELGi said "a separate distributor network was established for this tier… it requires a different mindset" (Q1 FY27 call summary). This is a sharper version of the fighter-brand move.
- **Owning Chinese mid-tier brands.** Atlas Copco bought Liutech (2002) and Shanghai Bolaite (2006, mid-range screw compressors below 450 kW). This mirrors Jungheinrich's AntOn. We have not checked whether these brands are sold in India or ASEAN.
- **In-sourcing motors** (ELGi).

**Failure modes observed.**
- A loyal installed base holds: Indian pumps are flat, which fits a strong domestic industry and BIS standards.
- Buyers return where energy cost matters: this is the ELGi segment logic.

**Gaps.** No brand-level shares exist. The large-genset surge in Malaysia coincides with Chinese firms building data centres there, but we found no evidence that those firms specify Chinese generator sets. Treat it as a hypothesis.

### C. Production machinery: injection-moulding machines, machine tools, laser cutters (new)

**Who buys and how.** Manufacturers, including Chinese-owned plants abroad, sold direct and through dealers with application centres. The purchase is tied to a factory build or line expansion.

**Position.**
- **Injection-moulding machines.** Across the four markets China's share rose from 24% (2015) to 31% (2019), 56% (2024) and 60% (2025). Japan's fell from 38% to 16%. By country in 2024: Indonesia 66%, Thailand 53% (68% in 2025), India 53% (47% in 2025, the year of the duty).
- **CNC lathes.** China rose from 6% to 27% and passed Japan (26%) in 2025. Thailand reached 58%.
- **Machining centres.** China rose from 2% to 21%, with Thailand at 43% in 2025. Japan still leads at 45%.
- **Laser machine tools.** China has led since HS 845611 began in 2017; it reached 55% in 2025.
- **India's own market.** Subject imports from China and Taiwan rose from under 4% of Indian demand to 19% between 2020-21 and the year to September 2023, according to the Indian producers who filed the DGTR case.

**The makers.**

| Maker | Overseas share | Notes |
|---|---|---|
| Haitian International | 42.8% of RMB17,733.2m revenue in 2025; overseas +26.4% | Domestic sales were flat |
| Yizumi | 29.90% of RMB6,048m in 2025, a record | Target is 50% by 2030 |
| HSG, Bodor (laser cutters) | — | Each claims market leadership in India |

**The follow-the-customer statement.** Haitian's own 2025 results statement says overseas growth came "在中国制造企业加快国际化布局的带动下", that is, "driven by Chinese manufacturers accelerating their international expansion". It adds that industrial customers' faster global capacity build-out and continued overseas investment "provided strong support" (haitian.com, March 2026). Southeast Asia and South America led.

**Clock: Push, with Embed starting.**
- The crossover with Japan was 2020 for injection-moulding machines and 2025 for CNC lathes.
- Local plants and service sites date from 2014–19.
- Trade defence in India arrived in 2023 and 2025.

| Learning | Grade | Evidence |
|---|---|---|
| L1 Beachhead (following home-country customers) | Strong | Haitian's statement above. Gains are largest where Chinese manufacturing investment concentrates (Thailand, Indonesia, Vietnam). India, with less Chinese FDI, still went from 23% to 53%, so price matters too. |
| L2 Credit | Weak | No evidence of maker or partner financing. |
| L3 Price, then lifecycle | Price: moderate. Lifecycle: moderate | DGTR found dumping margins of 40–70% and price suppression: Indian producers' costs rose while their prices did not. China's machine-tool exports are "predominantly low-to-mid-end" (industry report). A media anecdote puts a Chinese machine at about a quarter of the Japanese quote in Vietnam (36Kr, unverified). Lifecycle: Haitian India keeps spare-part stocks and application centres. Bodor India has a Mumbai repair centre for core components, a five-year warranty on three core components, more than 150 local staff and more than 2,000 machines in India (Aug 2024). |
| L4 Localise | Moderate (thinner than announced) | Haitian India (subsidiary 2014; Kadi plant opened 28 Apr 2018, planned at 1,800 machines a year; second plant planned for 2024). Haitian Vietnam (phase 2 in 2019). Yizumi India (Gujarat plant leased in 2017; 3,500 machines delivered by Sep 2025). HSG's US$10m India factory plan (Jan 2025). **Caution:** in the DGTR case, Indian producers said "Haitian has imported around 900 plastic processing machines in the period of investigation" and is "only a reseller and trader". Haitian gave no evidence of Indian production, so the regulator did not treat it as a domestic producer (paras 47, 54). |
| L5 Rules | Weak | Trade media cite India's PLI scheme and Vietnam's bonded warehouses as Haitian site criteria; this is not verified. Rules have mainly been used against Chinese makers (see trade remedies below). |
| L6 Technology wedge | Moderate | Servo-hydraulic, energy-saving injection-moulding machines (the Haitian India product line). Fibre lasers: China held 56.6% of global laser-equipment revenue in 2024, and more than 70% of China's high-power lasers are made at home (secondary). |

**Trade remedies.** This is failure mode 3, and here it has happened, not just been recommended.

- **Industrial laser machines.**
  - DGTR started the case in October 2022 on Sahajanand Laser Technology's application.
  - Duties were imposed by Notification 15/2023-Customs (ADD) on 22 Dec 2023, for five years:

    | Producer | Duty |
    |---|---|
    | HSG | 22.54% |
    | Han's Laser group | 24.66% |
    | Bystronic's China plants | 30.16% |
    | Jiangsu Yawei | 43.35% |
    | Bodor | 84.22% |
    | Oree | 87.30% |
    | Gweike | 90.49% |
    | TRUMPF China | Nil |
    | All others | 147.20% |

  - HSG's Indian factory plan followed in January 2025.
- **Injection-moulding machines.**
  - The case covers machines of 40–1,500 tonnes. It was initiated on 29 Mar 2024 and the final findings came on 27 Mar 2025.
  - Duties were imposed by Notification 21/2025-Customs (ADD) on 26 Jun 2025, for five years:

    | Producer | Duty |
    |---|---|
    | Chen Hsong (China) | 27% |
    | Yizumi | 35% |
    | Fu Chun Shin | 48% |
    | All other Chinese producers | 63% |
    | All other Taiwanese producers | 53% |

  - China's share of India's injection-moulding imports fell from 53% (2024) to 47% (2025).
- **Who petitioned.** The applicants, through the Plastic Machinery Manufacturers Association of India (PMMAI), were Electronica, Milacron India, Shibaura Machine India and Windsor (57% of Indian production). Two of the four are foreign incumbents with Indian plants.

**Incumbents' responses.**
- **Localised incumbents use trade defence** (Shibaura India, Milacron India).
- **Retreat to the high end.** Japan still leads machining centres. Fanuc and Yaskawa are investing in US plants after Fanuc lost its top shipment position in China.
- **Incumbents sourcing from China get caught.** Bystronic's China-made lasers carry a 30.16% duty.

**What it teaches.** Where the buyer is a factory, Chinese machinery follows Chinese factories abroad, and local service follows the installed base. Where domestic producers exist, trade defence arrives within three to four years of the surge, so localising behind the wall becomes the next move. HSG, Haitian and Yizumi all have Indian plants or plans. How deep that localisation goes can be tested, as the DGTR record on Haitian shows.

### D. Motion and power components: gearboxes, motors, bearings, hydraulics

**Who buys and how.** Other OEMs and panel builders. Components are specified into designs, so switching is slow.

**Position.**
- Gearboxes rose from 29% to 52% (2015 → 2025, four markets).
- AC motors rose from 36% to 48%.
- Hydraulic motors rose from 7% to 20%.
- Hydraulic and industrial valves barely moved.

**The makers.**
- **Wolong Electric Drive** (2025 annual report). Revenue was RMB15,454m. Asia-Pacific excluding China grew 45.56% to RMB1,563m, while domestic revenue fell 12.06%. About 41% of revenue is overseas. It has plants in Vietnam and Mexico, and owns ATB in Austria.
- **Hengli Hydraulic** (2025, secondary review of the annual report).
  - Revenue was RMB10,941m.
  - Overseas sales are "over 35%" of revenue.
  - Its Mexico plant ran trial production in 2025 and reaches full output in Q2 2026. It was inaugurated as a US$325m plant in June 2025.
  - An Indian entity was incorporated in 2020.

**Clock: Beachheads.** The evidence fits "follow the OEM customers": Hengli builds where its global excavator customers build. India- and ASEAN-specific evidence is thin.

| Learning | Grade | Evidence |
|---|---|---|
| L1 Beachhead | Moderate | Following OEM customers (Hengli in Mexico; Wolong's Asia-Pacific growth) |
| L2 Credit | Weak | — |
| L3 Price, then lifecycle | Weak | — |
| L4 Localise | Moderate | Wolong Vietnam; Hengli Mexico; Hengli India entity |
| L5 Rules | Weak | — |
| L6 Technology wedge | Weak | — |

**Use in the paper:** a supporting case of "suppliers follow the OEMs", not a full archetype.

### E1. Automation: robot arms, servo and PLC

**Who buys and how.** Factories, through system integrators. The buyer is the line builder, and the robot is specified with the line.

**Position.**
- **China customs.** Industrial robot exports rose 48.7% in 2025 and exceeded imports for the first time. "Asia remains the primary market… key destinations including Vietnam, Thailand, and India" (GAC deputy administrator, Jan 2026). H1 2026 exports were RMB6.29bn, up 18.6%, to 141 countries.
- **Importers' data (HS 847950).** China overtook Japan in 2025 in all four markets with 2025 data:

  | Market | China, 2019 | China, 2025 | Japan, 2025 |
  |---|---|---|---|
  | India | 16% | 34% | 30% |
  | Indonesia | 25% | 62% | 12% |
  | Thailand | 31% | 44% | 28% |
  | Malaysia | 26% | 40% | 36% |

  Indonesia's 2025 jump is large and needs explaining before it is published.
- **Related lines.** Control panels (which include PLCs) rose from 26% to 44%, and Japan fell to 7%.

**The makers.** Their own overseas businesses lag:
- **Estun** (HKEX annual results, 30 Mar 2026). Revenue was RMB4,888.01m. Overseas revenue was RMB1,462.67m, up 6.80%, against mainland revenue up 29.79%. The overseas share fell from 34.1% to 29.9%. Estun named Southeast Asia as a development focus.
- **Inovance** (2025 annual report summary). Revenue was RMB45.10bn. Its industrial robots "won top customers in markets such as Vietnam and Korea". It is building plants in Hungary and Thailand; an earlier check found the Thai plant is for its EV powertrain business. Its overseas share is about 6% (secondary source).
- **Efort.** It booked a RMB154.8m impairment on its overseas integration business and a RMB497m loss in 2025.

**Clock: Probe moving into Beachheads, with the turn in 2025.**

| Learning | Grade | Evidence |
|---|---|---|
| L1 Beachhead | Moderate | Two routes. (1) **A local champion as partner:** the Somboon Siasun Tech joint venture in Thailand (Somboon Advance Technology 50.0003%, Siasun 49.9997%; THB30m). It supplies robots, engineering and smart warehouses to automotive, and SAT's own customers include Toyota, Honda, Mazda, Isuzu and Mitsubishi (NNA, 2020). The partnership has since built what Siasun calls "Southeast Asia's first 5G smart factory" in the EEC (Siasun, Mar 2025). (2) **The supply chain moves with the customer:** in Feb 2026 Thailand's BOI approved more than THB10bn from five Chinese makers of humanoid-robot parts (Seenpin, Beite, Sanhua Intelligent Drives, Tuopu, Xusheng) in Chachoengsao (Nation Thailand). |
| L2 Credit | Weak | — |
| L3 Price, then lifecycle | Price: moderate. Lifecycle: weak | Estun and Inovance are "growing rapidly by competing on low prices", and Fanuc lost its top shipment position in China (Financial News, Sep 2026, citing MIR). A claim that Chinese robot export prices average about a third of China's import prices is unverified. No Chinese robot service network in the region is documented. |
| L4 Localise | Weak | No regional robot assembly found; the JV is engineering and integration |
| L5 Rules | Moderate (Thailand) | BOI promotion used to cluster Chinese robot-component makers in the EEC |
| L6 Technology wedge | Weak to moderate | AI vision, cobots and smart warehouses are bundled in Siasun's Thai projects. Humanoid components are being positioned. |

**Failure modes observed.**
- **Overseas acquisitions lose money** (Efort).
- **Price wars at home drain cash.** Efort described "volume without revenue, revenue without profit".
- **The home lead is not yet carried by Chinese brands abroad** (Estun's falling overseas share).

**Incumbents' responses.** Japanese makers are refocusing on the US. Fanuc is building a US$90m plant in Michigan and Yaskawa a US$180m plant in Wisconsin. In FY2025 their combined Americas sales (¥360.7bn) passed their China sales (¥344.5bn).

### E2. Automation: warehouse robots, AMRs and cobots

**Who buys and how.** Logistics and manufacturing users, sold as solutions and increasingly by subscription.

**Position.** These firms were born global:
- **Geek+ (H1 2026).** "Over 75%" of revenue came from outside mainland China, at a 46.2% gross margin. Subscription orders were RMB156m, up more than 75%; in the Americas they rose 455%. It has 81,000 robots deployed in more than 40 countries.
- **Dobot.** Overseas revenue was 59.1% in 2023 and 53.7% in 2024. Its subsidiaries are in the US, Germany and Japan.
- **Hai Robotics.** A Southeast Asia headquarters in Singapore since 2022, enlarged in 2024. More than 1,000 projects in more than 40 countries.

**Clock: Push globally, early in India and ASEAN.** Their beachheads are the US, Europe, Japan and Korea, so India and Southeast Asia are follower markets.

| Learning | Grade | Evidence |
|---|---|---|
| L1 Beachhead | Moderate | Beachheads are in developed markets, not this region |
| L2 Credit | Moderate | Subscription (robots-as-a-service) is credit built into the product: Geek+'s subscription orders rose more than 75% |
| L3 Price, then lifecycle | Weak | — |
| L4 Localise | Weak | No regional plants |
| L5 Rules | Weak | — |
| L6 Technology wedge | Moderate | Software and AI-led systems |

**Gap.** We found no named Chinese AMR or cobot deployments in India, Indonesia, Thailand or Vietnam in public sources. Treat this as a forward look only.

---

## 5. The grid: which learnings travel to which archetype

Grades apply to India and Southeast Asia. ● strong, ◐ moderate, ○ weak.

| Learning | Site and fleet (ref.) | Plant utility | Production machinery | Components | Robot arms, servo, PLC | AMRs and cobots |
|---|---|---|---|---|---|---|
| L1 Beachhead | ● | ◐ low-cost end | ● follow Chinese factories | ◐ follow OEMs | ◐ local partner; supply chain | ◐ (beachheads elsewhere) |
| L2 Credit | ● | ○ | ○ | ○ | ○ | ◐ subscription |
| L3 Price, then lifecycle | ● | ◐ / ○ | ◐ / ◐ | ○ | ◐ / ○ | ○ |
| L4 Localise | ● | ◐ | ◐ (thinner than announced) | ◐ | ○ | ○ |
| L5 Rules | ● | ○ (barrier) | ○ (used against them) | ○ | ◐ BOI clustering | ○ |
| L6 Technology wedge | ● (forklifts) | ◐ energy efficiency | ◐ servo-hydraulic; fibre laser | ○ | ◐ | ◐ |
| Phase in 2026 | Embed | Beachheads → early Push | Push → Embed | Beachheads | Probe → Beachheads (2025 turn) | Push globally; early here |
| Failure modes seen | All six | Installed base holds; buyers return on energy cost | **Trade cases (imposed)**; localisation thinner than claimed | — | Overseas acquisitions lose money; price wars at home | — |

**How the order of moves differs.**
- **Factory buyers** (production machinery, robots, components): follow the customer → local service → local plant → trade case. All of it comes fast.
- **Distributor-sold plant equipment:** price → distributors → local warehouse and service → (later) plants. Incumbents answer with fighter ranges.
- **Born-global solutions:** developed-market beachhead → subscription → follower markets.

---

## 6. What this changes in the paper

1. **Chapter 3 gets a stronger spine.**
   - Lead with the crossover-year clock (Section 3) and the grid (Section 5).
   - Make production machinery the main new case.
   - Compressors and pumps become the contrast: same moves, slower, with fighter brands.
   - Robotics gets the 2025 turn, with AMRs as the born-global variant.
2. **The box "following home-country customers" becomes an evidenced move.**
   - Haitian's filing statement, plus the trade gains concentrated where Chinese FDI is high.
   - Consider promoting it to a named sub-move under Learning 1.
3. **Failure mode 3 gains two imposed Indian cases** (lasers 2023; injection-moulding machines 2025). This contrasts with cranes, where duties lapsed. It also adds the incumbents-with-local-plants petitioner pattern.
4. **Learning 4 gets a caution:** announced plants are not always production plants (the DGTR record on Haitian).
5. **Learning 2 gets a boundary:** credit does not travel into mid-level products, except as subscription in AMRs.
6. **Signposts gain:**
   - China's share of robot imports.
   - India's anti-dumping docket on capital goods.
   - Whether Japanese machine-tool share holds in machining centres.

---

## 7. Corrections and flags found in this batch (fixed and logged)

- **India compressors.** The paper says 44.0% → 52.6% (2019–2024), which is correct. 2025 fell back to 49.3%. Say "rose mainly in 2024".
- **India highway pace.** "25 km a day in FY26" is correct (CareEdge, 25 Sep 2026). The 21 km figure in the headline is the FY27 expectation.
- **Indonesia coal.** "About 720 Mt" is the energy ministry's projection of 2026 output (Katadata, 10 Sep 2026), not a quota. Word it as a projection. The ministry's November 2025 signal of "below 700 Mt" was a plan. The final RKAB total is still to find.
- **Estun.** The overseas share from the HKEX annual results (34.1% → 29.9%) matches the paper's 34.16% → 29.92%. Keep the paper's figures and replace the Sina citation with the HKEX document.
- **Inovance.** The 2025 annual report summary gives no overseas split. Keep "about 6%" labelled as a secondary source. Add the primary statement that its robots won top customers in Vietnam.
- **CCMA series 2016–2019** added. The 2015 export share (10.2% of sales) comes from the CCMA's 2016 release; the 2015 absolute figure is not sourced.
- **Haitian India.** Our early message called its Gujarat plant evidence of localisation. That needs the DGTR caution above.

---

## 8. Gaps still open

- No public supplier-country split of robot installations in ASEAN (IFR's tables are paid).
- Why Indonesia's robot imports jumped in 2025.
- Brand shares for compressors and pumps.
- Whether Atlas Copco's Chinese brands are sold in India and ASEAN.
- Whether India's Pumps QCO has been finally notified.
- Whether Chinese firms building data centres specify Chinese generator sets.
- Named AMR or cobot deployments in India and ASEAN.
- Chinese machine-tool makers' plants in the region (only HSG has an announced plan).

---

## 9. Sources (selection; full log in `log.md`)

**Trade data**
- UN Comtrade public API, preview endpoint: https://comtradeapi.un.org/public/v1/preview/C/A/HS (pulled 1 Oct 2026)

**Production machinery**
- Haitian 2025 results statement: https://www.haitian.com/cn/all-cn/%E6%B5%B7%E5%A4%A9%E5%9B%BD%E9%99%85%E5%85%AC%E5%B8%832025%E5%B9%B4%E5%BA%A6%E4%B8%9A%E7%BB%A9/
- Haitian 2025 results summary (K-Online, 19 Mar 2026): https://www.k-online.com/en/Media_News/News/Haitian_International_Revenue_rises_to_around_EUR_2.24_billion_in_2025
- Haitian India plant (5 May 2018): https://eu.newsroom.haitian.com/all-en/grand-opening-of-new-factory-of-haitian-huayuan-india/
- Haitian Vietnam phase 2 (5 Mar 2019): https://www.haitian.com/en/2019/03/05/second-phase-plant-of-haitian-vietnam/
- Yizumi India (12 Sep 2025): https://www.yizumi.com/en/news/product/IMM/fruitful-results-3500-machines-delivery-at-yizumi-india-factory
- Yizumi 2025 results (EEO, 17 Apr 2026): http://www.eeo.com.cn/2026/0417/841964.shtml
- Bodor India (8 Aug 2024): https://www.bodor.com/en/news/company/Warmly-celebrate-the-fifth-anniversary-of-the-Bodor-India-subsidiary.html
- HSG India (15 Jan 2025): https://themachinemaker.com/news/hsg-laser-leads-indias-laser-cutting-industry-in-2024-and-plans-super-factory-and-enhanced-localization/

**Trade remedies (India)**
- DGTR final findings, plastic processing machines (27 Mar 2025): https://dgtr.gov.in/sites/default/files/2025-04/Final_FF_PPM_NCV_27.03.2025_0.pdf
- Customs Notification 21/2025-Customs (ADD): https://worldtradescanner.com/Ntfn%2021-Cus(ADD)-26.06.2025.htm
- Customs Notification 15/2023-Customs (ADD), industrial laser machines: https://taxguru.in/custom-duty/anti-dumping-duty-industrial-laser-machines-import-china.html

**Robots**
- Estun 2025 annual results (HKEX): https://www.hkexnews.hk/listedco/listconews/sehk/2026/0330/2026033003426.pdf
- Inovance 2025 annual report summary (CNINFO): https://static.cninfo.com.cn/finalpage/2026-04-28/1225208487.PDF
- China customs on robot exports (Global Times, Jan 2026): https://www.globaltimes.cn/page/202601/1353238.shtml
- H1 2026 robot exports (CGTN, 16 Jul 2026): https://news.cgtn.com/news/2026-07-16/Chinese-industrial-robot-exports-accelerate-in-H1-2026-1OPsmseJktO/p.html
- Somboon Siasun joint venture (NNA): https://english.nna.jp/articles/16699
- Thailand BOI approval of humanoid-robot parts makers (Nation Thailand, 23 Feb 2026): https://www.nationthailand.com/business/investment/40062862
- Japanese robot makers' US investment (Financial News, 30 Sep 2026): https://en.fnnews.com/news/202609301411141531

**AMRs and cobots**
- Geek+ H1 2026 results: http://www.prnewswire.com/news-releases/subscription-based-services-boom-geek-reports-2026-interim-results-orders-up-35-5-breakthroughs-across-the-business-spectrum-302867104.html
- Dobot 2024 annual results: https://software-1256299428.cos.na-siliconvalley.myqcloud.com/2025/relations/0324/ANNUAL%20RESULTS%20ANNOUNCEMENT%20FOR%20THE%20YEAR%20ENDED%2031%20DECEMBER%202024.pdf

**Components**
- Wolong Electric Drive 2025 annual report: http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2026/2026-3/2026-03-21/12008255.PDF
- Hengli Hydraulic 2025 review (163.com): https://www.163.com/dy/article/KQVTTCGT0553JROZ.html

**Plant utility equipment**
- Kaishan 2025 annual report summary (SZSE): https://disc.static.szse.cn/download/disc/disk03/finalpage/2026-04-22/d3fa1086-c8cb-4fc2-a376-4643bab85875.PDF
- Chinese pump makers H1 2025 (CGMIA): https://pu.cgmia.org.cn/News/Detail/23622
- ELGi Q1 FY27 call highlights: https://finance.yahoo.com/markets/stocks/articles/elgi-equipments-ltd-bom-522074-010534382.html
- Atlas Copco acquires Bolaite (2006): https://www.atlascopcogroup.com/en/media/press-releases/2006/atlas-copco-to-acquire-chinese-compressor-company
- Leo Pump Indonesia distributors: https://leopumps.co.id/distributor
- Kaishan India: https://kaishanindia.com/about-us.php

**Timeline**
- CCMA 2019 excavator sales (d1cm): https://news.d1cm.com/20200110112241.shtml
- CCMA 2017–2018 excavator sales (Qianzhan): https://www.qianzhan.com/analyst/detail/220/190201-492b4099.html
- CCMA 2016 excavator sales (SANY): https://www.sanygroup.com/industryNews/2780.html
