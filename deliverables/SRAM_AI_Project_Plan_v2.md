# SRAM AI Initiative — Project Plan
*Prepared for SRAM Executive Leadership | March 2026*

---

Based on our research and analysis of SRAM's business, we view the AI value creation opportunity as both broad and deep. To realize those benefits, however, there is a specific sequencing we recommend SRAM follow. This project plan builds on the four-step framework outlined in our AI Value Creation Proposals and answers the three most critical execution questions: how each initiative integrates into SRAM's existing processes, how we measure success, and what organizational capabilities — talent, data, and leadership — SRAM must have in place before each phase can succeed.

The two near-term pilots we recommend SRAM prioritize are the cost reduction initiatives: **Customer and Dealer Warranty Support** and **Demand Forecasting and Supply Chain Optimization**. These represent the clearest path to measurable, near-term value. The revenue-generating initiatives in Step 4 are real and significant, but they depend on the infrastructure and organizational trust that only the earlier steps can build.

---

## *Step 1: Early Wins (Month 0 – Month 12)*

It is clear based on our research that SRAM's internal processes are not necessarily tech-forward. As such, there is meaningful lift from implementing initial "early win" strategies to proliferate and democratize AI use within the organization. These strategies will not only support employee-level AI development, but also position the right people to succeed in the more ambitious steps that follow.

**1. AI Productivity Tools:**

> ***Problem:*** Without baseline AI familiarity across the organization, more sophisticated Step 3 and Step 4 deployments will face cultural resistance from employees who have never worked alongside AI tools. The risk is not technical failure — it is organizational rejection.

> ***Solution:*** Deploy **GitHub Copilot** and **Claude Code** for SRAM's software engineering team to enhance productivity and accelerate the technical infrastructure work that later steps require. Roll out **Microsoft CoPilot** for AI-powered note-taking, email drafting, and meeting summarization across business functions. Both tools integrate directly into existing environments — IDEs and Microsoft 365 — requiring no workflow redesign. Run quarterly internal AI innovation forums to surface grassroots use cases and identify the internal champions who will lead Step 3 adoption.

**How success is measured** — *SMART Goals:*
- By Month 6, ≥75% of software engineers are active weekly AI coding tool users, measured via GitHub and Claude usage dashboards
- By Month 9, ≥60% of business function staff are active weekly CoPilot users, measured via Microsoft 365 analytics
- By Month 12, ≥5 cross-functional internal AI champions are identified and assigned to Step 3 pilot teams

**Financial Estimate — Step 1:**

| | Amount |
|---|---|
| **Incremental Costs** | |
| GitHub Copilot Enterprise (300 engineers × $39/mo × 12) | $140K/yr |
| Microsoft CoPilot (500 business users × $30/mo × 12) | $180K/yr |
| Innovation forums + program management | $80K/yr |
| **Total Annual Investment** | **~$400K/yr** |
| **Benefits — Cost Savings** | |
| Engineering productivity gain (300 engineers × 20% efficiency lift on coding tasks) | ~$1.5M labor equiv./yr |
| Business function efficiency (500 staff × 10% time savings) | ~$500K labor equiv./yr |
| **Total Annual Benefit** | **~$2.0M/yr** |
| **Net Annual Value** | **~$1.6M** |
| **ROI** | **~5x** |

*Note: Productivity benefit is expressed as labor-equivalent value. Step 1 savings are meaningful but secondary to the organizational readiness these tools create for Steps 3 and 4.*

**What SRAM needs to be ready:**
This phase costs little and requires no new hires — only one internal program manager to coordinate rollout. The CTO must sponsor the engineering deployment and the COO must sponsor the business function rollout. Without named executive sponsors, adoption stalls at the enthusiast layer and never reaches the critical mass that Step 3 requires.

---

## *Step 2: Data Foundations (Month 0 – Month 24)*

Critical to the plan is making a deliberate investment in SRAM's data infrastructure. SRAM today operates without a centralized ERP, CRM, or data warehouse. Customer data lives in Shopify. AXS telemetry is siloed from Hammerhead ride data. Inventory and production data exist at the brand level. A unified data layer is not optional — it is the prerequisite on which every Step 3 and Step 4 initiative depends.

**1. AWS-Native Data Lakehouse:**

> ***Problem:*** SRAM cannot deploy demand forecasting, AXS Intelligence, or upgrade recommendation AI without a unified data layer. Launching any of these initiatives on fragmented, brand-siloed data would produce unreliable outputs and set back organizational confidence in the approach — the exact failure mode SRAM has experienced before with internally managed knowledge bases.

> ***Solution:*** Our proposal is to construct an AWS-native data "lakehouse," given SRAM already uses AWS today, upon which modern BI, analytics, and AI/ML tools can sit. Source systems — **SAP** (ERP), **Salesforce** (CRM and dealer/warranty management), AXS telemetry, Hammerhead/Karoo, and Quarq power data — feed into a centralized platform. **PowerBI** and **Databricks** sit on top for business intelligence and analytics. **Amazon Bedrock**, **SageMaker**, and **AgentForce** sit on top as the AI/ML layer. While not where AI directly adds value, this infrastructure is the unlock that makes everything else possible.

**How success is measured** — *SMART Goals:*
- By Month 15, Salesforce CRM is live for dealer and warranty management across SRAM's core product lines
- By Month 18, SAP ERP is live for SRAM core brands with ≥80% of order and inventory data flowing into the lakehouse
- By Month 24, AXS and Hammerhead telemetry integration achieves ≥90% of active device data captured, and the lakehouse data quality score reaches ≥85% on all fields required for demand forecasting

**Financial Estimate — Step 2:**

| | Amount |
|---|---|
| **Incremental Costs** | |
| SAP ERP implementation (license + SI partner) | $2.5–4.0M |
| Salesforce CRM implementation (license + config) | $0.5–1.0M |
| AWS Lakehouse build (S3, Glue, Redshift, pipelines) | $0.5–0.8M |
| Data engineering team (3–5 hires × $180K × 24 months) | $2.2–3.6M |
| Senior Data Architect (1 hire × $220K × 24 months) | $0.4M |
| **Total 24-Month Investment** | **$6.1–9.8M** |
| **Ongoing Annual Operating Cost (post-implementation)** | **~$1.5M/yr** |
| **Benefits — Cost Savings (Direct)** | |
| Elimination of brand-silo reporting redundancies | ~$500K/yr |
| Reduced manual data reconciliation across finance/ops | ~$500K/yr |
| Improved inventory visibility (partial stockout reduction before full 3B) | ~$500K/yr |
| **Total Direct Annual Benefit** | **~$1.5M/yr** |
| **Indirect Value** | Unlocks full Step 3 and Step 4 value ($10M+ in downstream annual savings and revenue) |

*Note: Step 2's primary return is not in direct savings — it is in making all subsequent AI initiatives viable. Without this infrastructure, Steps 3B and 4 cannot be deployed. The $6–10M investment should be evaluated against the $50M+ in cumulative downstream value it enables.*

**What SRAM needs to be ready:**
This step requires 3–5 data engineers (new hires or a system integrator partner), one senior data architect hired at Month 1 to own the lakehouse design permanently, and a VP-level executive with cross-brand budget authority who can enforce data centralization over brand-level resistance. This is not a technology project — it is a cross-functional organizational change that will encounter resistance from brand teams accustomed to owning their own systems.

---

## *Step 3: Cost Reduction (Month 0 – Month 36)*

This is where our plan begins to bear fruit. After SRAM employees and systems are positioned to adopt AI at the process level, the most logical near-term value creation opportunities are in cost savings. We have identified two leading pilots to address in this category.

---

**1. Customer and Dealer Warranty Support (Month 0 – Month 12):**

> ***Problem:*** SRAM's Trustpilot rating is 1.6 out of 5, with reviews consistently citing warranty friction and unresolved firmware failures as the primary drivers. [2] Customers explicitly state intent to switch to Shimano after support failures. The churn risk is real, and it is driven by support quality — not product quality. Today, service support is not handled centrally, approximately 70% of inbound dealer and customer questions follow repeatable patterns that are handled manually, and warranty claims are processed without systematic screening. This creates real customer retention risk, lost revenues, and inflated costs — all addressable without touching the product itself.

> ***AI Solution:*** SRAM maintains a large support knowledge base with manuals, compatibility guides, troubleshooting procedures, and warranty guidance. **Amazon Bedrock**, powered by **Claude**, can act as an AI agent retrieving relevant documentation and device telemetry context from **Amazon Kendra**, then drafting accurate, natural-language responses to the ~70% of tickets that follow structured, repeatable patterns. A human support agent reviews and approves every response before it is sent — no automated sends during the pilot. This human-in-the-loop design is not a temporary compromise; it is the mechanism that preserves dealer trust while the system builds its track record. In parallel, AI agents trained on centralized product and warranty terms data can more quickly and accurately assess inbound warranty claims, reducing fraud and frivolous submissions that drag on SRAM's cost base. Once piloted, the long-term solution can move toward a fully automated support function that learns continuously from prior interactions.

**How this integrates into current processes:**

The pilot does not replace the Zendesk support workflow — it inserts into it.

*Current state:* Dealer contacts → agent manually searches knowledge base → agent drafts and sends response

*Pilot state:* Ticket arrives in Zendesk → Kendra retrieves relevant docs and device context → Bedrock (Claude) drafts response → human agent reviews and approves → outcome logged for model improvement

**How success is measured** — *SMART Goals:*

| Goal | Metric | Target | By |
|------|--------|--------|----|
| G1: Response Time | Avg time-to-first-response on AXS/Hammerhead dealer tickets | 40% reduction vs. baseline | Day 90 |
| G2: Escalation Rate | % tickets resolved without escalation | +15 percentage points vs. baseline | Day 90 |
| G3: Draft Acceptance | % AI drafts approved by agents with minor/no edits | ≥70% | Day 90 |
| G4: Agent Throughput | Tickets handled per agent per day | +25% vs. baseline | Day 90 |
| G5: Customer Satisfaction | CSAT on AI-assisted tickets | Flat or improving, ≥2 consecutive periods | Bi-weekly |
| G6: Warranty Accuracy | AI recommendation agreement with human decision (sampled) | ≥90% | Monthly |

*Kill criteria:* Two consecutive CSAT declines; any warranty error reaching a dealer without human review; dealer opt-out above 15%; G3 draft acceptance below 40% after scope adjustments.

**Pilot phases:** Month 1 — setup and baseline. Month 2–3 — AXS drivetrain tickets only, 100% human review. Month 4–5 — expand to Hammerhead devices (contingent on Day 45 acceptance rate ≥50%). Month 6 — Day 90 go/no-go decision. Month 7–12 — scale to full product catalog.

**Financial Estimate — Step 3A:**

| | Conservative | Expected | Upside |
|---|---|---|---|
| **Incremental Costs** | | | |
| Setup (Zendesk/Kendra/Bedrock integration, integration engineer, indexing) | $350K | $500K | $650K |
| Annual operating cost (AWS compute, Zendesk tier, QA, maintenance) | $200K/yr | $300K/yr | $400K/yr |
| **Benefits — Cost Savings** | | | |
| Support efficiency (120 staff × $90K × 60% AI-addressable × 35% gain × 70% adoption) | $1.0M/yr | $1.6M/yr | $2.5M/yr |
| Warranty claim accuracy (fraud/duplicate reduction) | $200K/yr | $400K/yr | $800K/yr |
| **Benefits — Revenue Protection** | | | |
| Customer retention (reduced churn from support failures) | $1.5M/yr | $3.0M/yr | $4.5M/yr |
| **Total Annual Gross Benefit** | **$2.7M** | **$5.0M** | **$7.8M** |
| **Net Year 1 Value (after costs)** | **$2.2M** | **$4.5M** | **$7.1M** |
| **ROI on Setup Investment** | **~6x** | **~9x** | **~11x** |

**What SRAM needs to be ready:**
- *Talent:* One named internal product owner with dedicated time; one integration engineer (internal or contract); one support team lead managing agent adoption
- *Data:* AXS and Hammerhead documentation audited and indexed in Kendra before launch; 90 days of historical Zendesk ticket data to establish measurement baseline
- *Leadership:* One named C-suite sponsor who owns the pilot outcome as a primary accountability — not a secondary responsibility. Pre-authorized rollback authority for the pilot product owner

---

**2. Demand Forecasting and Supply Chain Optimization (Month 24 – Month 36):**

> ***Problem:*** Based on our research, SRAM views this as one of the most actionable and near-term value-additive initiatives in the portfolio. SRAM effectively has no demand forecasting engine in place today, and as such this is already high priority within the organization. For any manufacturer, stockouts, markdown losses, and overproduction are hallmarks of inefficiency and among the largest "avoidable" costs in the business. Better syncing production with the actual sales cycle can yield significant value gains without impacting the product or the customer experience whatsoever.

> ***Solution:*** With the benefit of the formalized data lakehouse from Step 2, a forecasting system built on **Amazon SageMaker** — using historical order data, dealer sell-through rates, and seasonal patterns — could meaningfully reduce stockout and markdown losses. SRAM already runs on AWS, so keeping the ML platform on the same cloud avoids the operational overhead and vendor fragmentation of introducing a second provider. ML models largely perform analysis autonomously using inventory, production schedule, and manufacturing site data embedded in the lakehouse. This allows AI agents to do the analysis and pre-planning of proposed responses, turning supply chain planners into true decision makers rather than reactive problem-solvers — and freeing up SRAM resources accordingly.

**How this integrates into current processes:**

*Current state:* Production planning driven by brand-level judgment and informal historical patterns; no centralized inventory visibility; dealer sell-through not systematically tracked

*Pilot state (shadow mode, Month 27–30):* SageMaker model runs in parallel with existing planning; planners receive model recommendations alongside current inputs but make decisions as normal — model observed, not acted upon yet

*Pilot state (active, Month 30–36):* Planners act on model recommendations with full override authority; all overrides logged with reason codes; model retrains quarterly from override patterns

**How success is measured** — *SMART Goals:*

| Goal | Metric | Target | By |
|------|--------|--------|----|
| G1: Forecast Accuracy | MAPE on pilot SKU demand forecast | ≤15% on back-test; ≤20% on live data | Month 27; Month 30 |
| G2: Stockout Reduction | Stockout rate on pilot SKUs vs. baseline | 30% reduction | Month 36 |
| G3: Markdown Reduction | Markdown/write-down rate on pilot SKUs vs. baseline | 25% reduction | Month 36 |
| G4: Inventory Efficiency | Inventory turns on pilot SKUs vs. baseline | +15% improvement | Month 36 |
| G5: Planner Adoption | % of model recommendations acted upon vs. overridden | ≥60% | Month 36 |
| G6: Financial Impact | Annualized avoidable inventory loss recovered | ≥$1.6M | Month 36 |

*Kill trigger:* MAPE >25% at Month 30 triggers retraining before proceeding to the active pilot phase.

**Pilot phases:** Month 22–24 — data readiness audit (hard gate: ≥85% data quality on pilot SKUs). Month 24–27 — SageMaker model development and back-test validation. Month 27–30 — shadow mode. Month 30–36 — active pilot. Month 36 — full evaluation and scale decision.

**Financial Estimate — Step 3B:**

| | Conservative | Expected | Upside |
|---|---|---|---|
| **Incremental Costs** | | | |
| Setup (SageMaker development, data science lead ramp, analyst training) | $400K | $500K | $700K |
| Annual operating cost (ML lead, SageMaker compute, data engineer time) | $500K/yr | $700K/yr | $900K/yr |
| **Benefits — Cost Savings** | | | |
| Stockout loss recovery (lost sales on out-of-stock SKUs) | $1.5M/yr | $2.5M/yr | $4.0M/yr |
| Markdown/write-down reduction | $1.0M/yr | $1.5M/yr | $2.5M/yr |
| Inventory carrying cost savings (20% inventory reduction on ~$125M) | $0.6M/yr | $0.8M/yr | $1.5M/yr |
| Planning labor efficiency | $200K/yr | $400K/yr | $700K/yr |
| **Total Annual Gross Benefit** | **$3.3M** | **$5.2M** | **$8.7M** |
| **Net Annual Value (after operating costs)** | **$2.8M** | **$4.5M** | **$7.8M** |
| **One-Time Working Capital Release** (inventory reduction) | $10M | $15–20M | $25M |
| **ROI on Setup Investment** | **~7x** | **~9x** | **~11x** |

**What SRAM needs to be ready:**
- *Talent:* One ML/data science lead (new hire, start Month 20 to allow ramp time); two supply chain analysts redeployed from the existing team with AI workflow training; data engineer continuity from the Step 2 team
- *Data:* Minimum three years of unified, SKU-level order history from the Step 2 lakehouse — this is a hard go/no-go gate. Piloting on fragmented data produces unreliable outputs
- *Leadership:* Supply Chain Director or COO as named pilot owner. Planners must document all model overrides — non-optional policy, as override data directly feeds future model improvement

---

## *Step 4: Revenue Uplift and Enhanced Innovation via AI-First Culture (Month 36 – Month 60 and onward)*

Revenue-driven value creation initiatives often fall more towards the high-risk, high-reward end of the spectrum in terms of potential investments. This is no different for SRAM. The focus of our proposal through Steps 1–3 is on building the early wins and critical infrastructure to support being an AI-first enterprise. As a result, there are various potential opportunities for AI adoption in Step 4 with likely outsized returns, but we view these as longer-term innovations in the project plan that will be explored, prioritized, and ultimately decisioned as the data infrastructure and organizational capability matures.

**1. AXS Intelligence Platform (Month 36–54):**

Consolidate telemetry from AXS drivetrains, RockShox suspension, Quarq power meters, and Hammerhead computers into a unified rider performance intelligence layer. Using **SageMaker** for analytics and **Amazon Bedrock** for agentic recommendations, SRAM can deliver real-time suggestions and component self-optimization via a new "AXS Intelligence" brand within the AXS app — unlocking premium tiered subscription revenue and deepening the competitive data moat no competitor can replicate.

| | Amount |
|---|---|
| **Investment** | $3–5M (platform build, Years 3–5) + $1–2M/yr ongoing |
| **Revenue Uplift** | |
| AXS Premium subscriptions (conservative: 50K users × $79/yr) | $4M ARR |
| AXS Premium subscriptions (base case: 150K users × $95/yr blended) | $14M ARR |
| Incremental parts/accessories via predictive maintenance | $2–8M/yr |
| OEM/retailer data intelligence (B2B tier) | $1–4M/yr |
| **Total Revenue at Scale (Base Case)** | **~$20M ARR** |
| **ROI** | **~5–7x on platform investment** |

**2. Generative Design and R&D Acceleration (Month 42–60):**

AI-assisted design, digital twin simulation (replacing physical lab iterations), and automated patent search free engineering capacity for higher-value innovation work. Field telemetry data from AXS Intelligence trains AI agents on actual performance data to propose and evaluate new designs at a speed that purely human-driven processes cannot match.

| | Amount |
|---|---|
| **Investment** | $2–4M (tooling + engineering time, Years 4–5) |
| **Benefits — Cost Savings** | |
| Physical prototype iterations avoided (2–3 per product line, 5 major lines/yr) | $750K–$3M/yr |
| Time-to-market compression (2–4 months earlier per major product launch) | $2–6M/yr equiv. revenue acceleration |
| **Benefits — Revenue Uplift** | |
| Weight/performance improvements enabling premium pricing maintenance | $1–5M/yr |
| **Total Annual Benefit** | **$3.75–14M/yr** |

**3. OEM Proposal Automation (Month 36–48):**

**Salesforce AgentForce** with CPQ (configure, price, quote) features accelerates spec proposal generation, automates documentation, and provides AI-assisted deal intelligence for OEM sales teams — improving win rates and reducing the manual cross-functional burden that currently slows SRAM's response to OEM opportunities.

| | Amount |
|---|---|
| **Investment** | $500K–$1M (AgentForce implementation + CPQ configuration) |
| **Revenue Uplift** | |
| 1% improvement in OEM win rate on ~$250M opportunity pool | $2.5M/yr |
| Reduced proposal cycle time (sales efficiency) | $500K/yr labor equiv. |
| **Total Annual Benefit** | **~$3.0M/yr** |
| **ROI** | **~4–5x** |

**4. Compatible Upgrade Recommendations (Month 42–60):**

A **SageMaker** recommendation engine paired with a compatibility rules engine lifts rider basket value through dealer and DTC channels, using AXS telemetry and registered component data to drive predictive maintenance alerts, compatible upgrade suggestions, and personalized outreach — turning SRAM's installed base into an active revenue engine.

| | Amount |
|---|---|
| **Investment** | $500K–$800K (recommendation engine build) |
| **Revenue Uplift** | |
| Cross-sell/upsell lift (3–5% of registered user base making one incremental purchase) | $2–4M/yr |
| Dealer inventory turnover improvement | $500K–$1M/yr |
| **Total Annual Benefit** | **$2.5–5M/yr** |
| **ROI** | **~4–7x** |

---

## Consolidated Financial Summary

The table below shows high-level investment and expected annual benefit at steady state across all four steps. All figures represent expected-case estimates; conservative and upside ranges are shown in the individual step sections above.

| Step | Initiative | Setup / Total Investment | Annual Operating Cost | Annual Benefit (Steady State) | Net Annual Value | ROI |
|------|-----------|------------------------|----------------------|-------------------------------|-----------------|-----|
| **Step 1** | AI Productivity Tools | — | ~$400K/yr | ~$2.0M (productivity) | ~$1.6M | ~5x |
| **Step 2** | Data Foundations | $6–10M (24-month) | ~$1.5M/yr | ~$1.5M direct + downstream unlock | — | Enabler |
| **Step 3A** | Warranty Support Pilot | ~$500K | ~$300K/yr | ~$5.0M (savings + retention) | ~$4.5M | ~9x Y1 |
| **Step 3B** | Demand Forecasting Pilot | ~$500K | ~$700K/yr | ~$5.2M (cost savings) | ~$4.5M | ~9x |
| **Step 4** | AXS Intelligence Platform | $3–5M | $1–2M/yr | ~$20M ARR at scale | ~$18M | ~5–7x |
| **Step 4** | Generative Design / R&D | $2–4M | — | $3.75–14M/yr | ~$7M | ~3–5x |
| **Step 4** | OEM Proposal Automation | $500K–1M | — | ~$3.0M/yr | ~$2.5M | ~4–5x |
| **Step 4** | Compatible Upgrade Recs | $500K–800K | — | $2.5–5M/yr | ~$3.5M | ~5–7x |
| **Total Program** | | **~$15–22M** | **~$2.9M/yr** | **~$39M+/yr at maturity** | **~$34M+/yr** | **~4x blended** |

**Key one-time value:** The demand forecasting initiative (Step 3B) also generates an estimated $15–20M working capital release from inventory reduction — a one-time balance sheet benefit that partially offsets the Step 2 infrastructure investment.

**Overall program framing:** The full AI transformation — Steps 1 through 4 — requires approximately $15–22M in cumulative investment over five years and is expected to generate $39M+ in annual value at maturity, representing a blended ~4x return. Time to first positive ROI is 6–9 months, driven by Step 1 productivity gains and the early Stage 3A warranty pilot results.

---

## Leadership and Governance

The single most important organizational decision in this entire plan is naming a **dedicated C-suite AI Sponsor** — one person with primary accountability for the transformation program. Not a committee, and not a secondary responsibility layered onto an existing role. This designation must happen before the warranty pilot launches. Every phase that follows depends on having someone at the C-suite level with the authority and mandate to resolve cross-functional conflicts, enforce data centralization, and maintain sequencing discipline when individual business units push to move faster than the infrastructure supports.

Beyond the sponsor, the governance structure should be lightweight:

| Cadence | Participants | Purpose |
|---------|-------------|---------|
| Weekly (during active pilots) | Pilot Owner, AI Sponsor, relevant team lead | Metrics review; issue escalation |
| Monthly | C-suite sponsors, Pilot Owners | Phase gate readiness; resource decisions |
| Quarterly | Full C-suite | Strategic alignment; Step 4 initiative prioritization |

---

## Three Actions for SRAM's CEO

**1. Approve the Warranty Support Pilot now.** Name one internal product owner with dedicated time. Approve ~$500K in setup budget. Set the Day 90 go/no-go review date. This is the lowest-risk, highest-visibility entry point into SRAM's AI transformation, requires no data infrastructure investment to begin, and should yield ~$4.5M in net Year 1 value.

**2. Name the C-suite AI Sponsor.** One person. Primary accountability. This single decision is the highest-leverage action in the plan — the program does not survive the organizational friction of Step 2 and Step 3 without it.

**3. Authorize the Step 2 data infrastructure investment.** Begin SAP and Salesforce vendor selection in parallel with the warranty pilot. Every month of delay on data foundations is a month of delay on demand forecasting, AXS Intelligence, upgrade recommendations, and OEM automation. The $6–10M Step 2 investment unlocks what we estimate to be $34M+ in steady-state annual value across Steps 3 and 4. The sequencing cannot be compressed — it can only be started sooner.

---

## Gantt Chart: Steps 1–3 Detail (Month 1–36)

*`████` = Active build | `────` = Ongoing / maintenance | `[*]` = Go-live | `[✓]` = Decision gate | `[G]` = Event*

```
INITIATIVE                          │Q1  │Q2  │Q3  │Q4  │Q5  │Q6  │Q7  │Q8  │Q9  │Q10 │Q11 │Q12 │
                                    │M1-3│M4-6│M7-9│M10 │M13 │M16 │M19 │M22 │M25 │M28 │M31 │M34 │
                                    │    │    │    │-12 │-15 │-18 │-21 │-24 │-27 │-30 │-33 │-36 │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 1: EARLY WINS                  │    │    │    │    │    │    │    │    │    │    │    │    │
  Copilot / Claude Code (Eng.)      │████│████│████│████│────│────│────│────│────│────│────│────│
  Microsoft CoPilot (Business)      │████│████│████│████│────│────│────│────│────│────│────│────│
  AI Innovation Forums              │    │[G] │    │[G] │    │[G] │    │[G] │    │    │    │    │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 2: DATA FOUNDATIONS            │    │    │    │    │    │    │    │    │    │    │    │    │
  ERP (SAP) Selection & Contract    │████│████│    │    │    │    │    │    │    │    │    │    │
  Salesforce CRM Implementation     │████│████│████│████│[*] │    │    │    │    │    │    │    │
  AWS Lakehouse Architecture        │████│████│    │    │    │    │    │    │    │    │    │    │
  Data Pipelines (Shopify/Support)  │    │████│████│████│████│    │    │    │    │    │    │    │
  SAP ERP Go-Live (Core Brands)     │    │    │████│████│████│[*] │    │    │    │    │    │    │
  AXS + Hammerhead Telemetry Intg.  │    │    │    │████│████│████│████│    │    │    │    │    │
  PowerBI / Databricks Deployment   │    │    │    │████│████│████│    │    │    │    │    │    │
  Data Quality Gate (Forecasting)   │    │    │    │    │    │    │    │[✓] │    │    │    │    │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 3A: WARRANTY SUPPORT PILOT     │    │    │    │    │    │    │    │    │    │    │    │    │
  Pilot Design + Baseline Setup     │████│    │    │    │    │    │    │    │    │    │    │    │
  Kendra + Bedrock Integration      │████│████│    │    │    │    │    │    │    │    │    │    │
  AXS Drivetrain Ticket Rollout     │    │████│████│    │    │    │    │    │    │    │    │    │
  Day-45 Scope Checkpoint           │    │[✓] │    │    │    │    │    │    │    │    │    │    │
  Hammerhead Ticket Expansion       │    │    │████│████│    │    │    │    │    │    │    │    │
  Warranty Claim AI Review Track    │    │    │████│████│    │    │    │    │    │    │    │    │
  Day-90 Go / No-Go Decision        │    │    │    │[✓] │    │    │    │    │    │    │    │    │
  Scale to Full Product Catalog     │    │    │    │    │████│████│████│────│    │    │    │    │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 3B: DEMAND FORECASTING PILOT   │    │    │    │    │    │    │    │    │    │    │    │    │
  Data Readiness Audit              │    │    │    │    │    │    │    │████│    │    │    │    │
  Data Quality Gate                 │    │    │    │    │    │    │    │[✓] │    │    │    │    │
  SageMaker Model Development       │    │    │    │    │    │    │    │    │████│████│    │    │
  Back-Test Validation (MAPE Gate)  │    │    │    │    │    │    │    │    │    │[✓] │    │    │
  Shadow Mode Pilot                 │    │    │    │    │    │    │    │    │    │████│████│    │
  Shadow Checkpoint                 │    │    │    │    │    │    │    │    │    │    │    │[✓] │
  Active Pilot (Planners Decide)    │    │    │    │    │    │    │    │    │    │    │████│████│
  Full Evaluation + Scale Decision  │    │    │    │    │    │    │    │    │    │    │    │[✓] │
────────────────────────────────────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
[G] = Innovation Forum   [*] = Go-live milestone   [✓] = Decision gate
```

---

## Overview Gantt Chart: All Steps (Month 1–60)

```
INITIATIVE                          │H1Y1│H2Y1│H1Y2│H2Y2│H1Y3│H2Y3│H1Y4│H2Y4│H1Y5│H2Y5│
                                    │M1-6│M7  │M13 │M19 │M25 │M31 │M37 │M43 │M49 │M55 │
                                    │    │-12 │-18 │-24 │-30 │-36 │-42 │-48 │-54 │-60 │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 1: EARLY WINS                  │    │    │    │    │    │    │    │    │    │    │
  AI Productivity Tools             │████│████│────│────│────│────│────│────│────│────│
  Innovation Forums                 │████│████│████│────│────│────│────│────│────│────│
  C-Suite AI Sponsor Named          │[*] │    │    │    │    │    │    │    │    │    │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 2: DATA FOUNDATIONS            │    │    │    │    │    │    │    │    │    │    │
  SAP ERP Implementation            │████│████│████│[*] │    │    │    │    │    │    │
  Salesforce CRM Implementation     │████│████│[*] │    │    │    │    │    │    │    │
  AWS Data Lakehouse Build          │████│████│████│████│────│────│────│────│────│────│
  Full Telemetry Integration        │    │████│████│[*] │────│────│────│────│────│────│
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 3A: WARRANTY SUPPORT           │    │    │    │    │    │    │    │    │    │    │
  Pilot — AXS + Hammerhead Scope    │████│████│    │    │    │    │    │    │    │    │
  Scale to Full Catalog             │    │    │████│████│────│────│────│────│────│────│
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 3B: DEMAND FORECASTING         │    │    │    │    │    │    │    │    │    │    │
  Model Dev + Shadow Mode           │    │    │    │████│████│    │    │    │    │    │
  Active Pilot + Full Scale         │    │    │    │    │    │████│████│────│────│────│
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 4: REVENUE & INNOVATION        │    │    │    │    │    │    │    │    │    │    │
  OEM Proposal Automation           │    │    │    │    │    │████│████│────│────│────│
  AXS Intelligence Platform         │    │    │    │    │    │████│████│████│████│████│
  Compatible Upgrade Recs Engine    │    │    │    │    │    │    │████│████│████│────│
  Generative Design / Digital Twin  │    │    │    │    │    │    │████│████│████│████│
  AI-Adjusted Component Performance │    │    │    │    │    │    │    │████│████│████│
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
ORGANIZATIONAL ENABLERS             │    │    │    │    │    │    │    │    │    │    │
  Data Engineering Team             │████│████│────│────│────│────│────│────│────│────│
  ML / Data Science Lead            │    │    │████│────│────│────│────│────│────│────│
  QA Scale-Up                       │    │    │    │    │████│────│────│────│────│────│
  Cross-Brand PM (AXS Intelligence) │    │    │    │    │████│────│────│────│────│────│
────────────────────────────────────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
████ = Active build/deployment   ──── = Ongoing operations   [*] = Critical milestone
```

---

## Sources

**[1]** AI Value Creation Proposals, internal working document, March 2026. `AI_Value_Creation_Proposals.pdf`.

**[2]** Trustpilot, "SRAM Reviews." https://www.trustpilot.com/review/www.sram.com (accessed March 2026). 65 reviews; overall rating approximately 1.6/5.

**[3]** SRAM AI Adoption Playbook, March 2026. `deliverables/SRAM_AI_Adoption_Playbook_wCitations.md`.

**[4]** SRAM AI Adoption Strategy reference analysis, February 28, 2026. `research/reference/sram_ai_strategy.md`. Financial models, phased initiative roadmap, tool recommendations, and industry benchmarks sourced therein from IBM, Bridgera, Rock-and-River, LinearB, and GitHub/Microsoft (2024–2026).

**[5]** Reddit cycling community threads, r/cycling and r/sram, 2024–2025.
