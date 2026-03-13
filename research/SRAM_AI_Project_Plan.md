# SRAM LLC — AI Initiative Project Plan
**Prepared for SRAM Executive Leadership | March 2026**

---

## 1. Purpose

This plan translates SRAM's four-step AI framework into an actionable roadmap. It answers three questions: how each initiative integrates into current processes, what success looks like (in SMART goal form), and what organizational capabilities — talent, data, and leadership — are required. The two near-term pilots are **Customer and Dealer Warranty Support** (Month 0–12) and **Demand Forecasting and Supply Chain Optimization** (Month 24–36), both targeting cost reduction before SRAM moves toward revenue-generating AI in Step 4.

---

## 2. Four-Step Framework

| Step | Name | Timeline | Objective |
|------|------|----------|-----------|
| **1** | Early Wins | Month 0–12 | Build AI fluency across the organization |
| **2** | Data Foundations | Month 0–24 | Unify SRAM's data infrastructure on AWS |
| **3** | Cost Reduction Pilots | Month 0–36 | AI-driven savings in support and supply chain |
| **4** | Revenue and Innovation | Month 36–60+ | AI-first product, sales, and R&D capabilities |

Steps 1, 2, and 3A run concurrently from Day 1. The warranty pilot does not require a complete data lakehouse — it runs on SRAM's existing AXS and Hammerhead knowledge bases. Step 2 enables the later, more data-intensive initiatives.

---

## 3. Step 1: Early Wins — AI Fluency (Month 0–12)

**What it does:** Deploys individual productivity AI tools across the organization before attempting workflow-level automation. Builds the internal champions needed to drive adoption in Steps 3 and 4.

**Initiatives:**
- **GitHub Copilot and Claude Code** for 250–400 software engineers — integrated directly into existing IDEs and Jenkins CI/CD pipelines
- **Microsoft CoPilot** across business functions (finance, sales ops, HR) — embedded in existing Microsoft 365 environment
- **Quarterly AI Innovation Forums** — cross-functional hackathons to surface internal use cases and identify future champions

**Integration into current processes:** All tools operate inside existing software environments. No process redesign required. Engineers keep current workflows; AI assists inline.

**SMART Goals:**
- By Month 6, ≥75% of software engineers use AI coding tools at least weekly, measured via GitHub Copilot and Claude usage dashboards
- By Month 9, ≥60% of business function staff use Microsoft CoPilot weekly, measured via M365 analytics
- By Month 12, ≥5 internal AI champions identified and assigned to Step 3 pilot teams, sourced from innovation forum participation

**Organizational enablers:** No new hires required. One internal program manager coordinates rollout. CTO sponsors engineering deployment; COO sponsors business function rollout. Without named executive sponsors, adoption stalls at the enthusiast layer.

---

## 4. Step 2: Data Foundations (Month 0–24)

**What it does:** Builds the unified data infrastructure that every Step 3 and Step 4 initiative depends on. SRAM currently has no ERP, no centralized CRM, and no data warehouse. Customer, inventory, telemetry, and support data exist in brand-level silos.

**Target architecture:** Source systems (SAP ERP, Salesforce CRM, AXS telemetry, Hammerhead/Karoo, Quarq, Shopify) → AWS Native Data Lakehouse → Integrated tools (PowerBI, Databricks, Amazon Bedrock/Claude, SageMaker, AgentForce)

**Implementation sequence:**
- Month 0–6: ERP and CRM vendor contracting; lakehouse architecture finalized
- Month 6–18: SAP go-live (SRAM core brands); Salesforce CRM live for dealer and warranty management; data pipelines from Shopify and support systems
- Month 12–24: AXS, Hammerhead, Quarq telemetry integrated; PowerBI and Databricks deployed; data quality validated for forecasting use case

**SMART Goals:**
- By Month 15, Salesforce CRM is live for dealer and warranty management across SRAM's core product lines
- By Month 18, SAP ERP is live for SRAM core drivetrain brands, with ≥80% of order and inventory data flowing into the lakehouse
- By Month 24, AXS and Hammerhead telemetry integration achieves ≥90% of active device data captured; lakehouse data quality score ≥85% on fields required for demand forecasting

**Organizational enablers:** Requires 3–5 data engineers (new hires or contract), one senior data architect (new hire, Month 1), and a system integrator for SAP and Salesforce implementation. A VP-level executive with cross-brand budget authority must own this step — brand-level teams will resist centralization without senior enforcement.

---

## 5. Pilot A: Customer and Dealer Warranty Support (Month 0–12)

### The Problem

SRAM's Trustpilot rating is 1.6 out of 5, driven by support failures — not product failures. Approximately 70% of inbound dealer and customer questions follow repeatable patterns. Warranty claims are processed manually, creating delays and exposing SRAM to fraudulent or duplicate submissions. The cost is both direct (support headcount, claim payouts) and indirect (customer churn to Shimano).

### Integration Into Current Processes

This pilot inserts AI into the existing Zendesk support workflow — it does not replace it.

**Current state:** Dealer/customer contacts → agent manually searches knowledge base → agent drafts and sends response

**Pilot state:** Ticket arrives in Zendesk → Amazon Kendra retrieves relevant documentation and device telemetry context → Amazon Bedrock (Claude) drafts a response → **human agent reviews and approves before sending** → outcome logged for model improvement

Human approval is mandatory throughout the pilot. This is not a temporary concession — it is the mechanism that protects dealer trust while the system proves accuracy. No automated sends until quality is validated.

**Warranty claim track (parallel):** AI agent cross-references warranty terms, purchase records, and historical claim patterns → produces a recommended decision with confidence score → warranty team member makes the final call

**Tool stack (all AWS-native):**

| Tool | Role |
|------|------|
| Zendesk AI | Ticket routing and agent interface |
| Amazon Kendra | Knowledge base retrieval (AXS and Hammerhead docs) |
| Amazon Bedrock (Claude) | Natural-language response drafting |
| Salesforce CRM | Dealer history and warranty records |

### SMART Goals

| Goal | Metric | Target | Timeline |
|------|--------|--------|----------|
| **G1: Response Time** | Avg time-to-first-response on dealer tickets | 40% reduction vs. pre-pilot baseline | Day 90 |
| **G2: Escalation Rate** | % tickets resolved without escalation | +15 percentage points vs. baseline | Day 90 |
| **G3: Draft Acceptance** | % AI drafts approved with minor/no edits by agents | ≥70% | Day 90 |
| **G4: Agent Throughput** | Tickets handled per agent per day | +25% vs. baseline | Day 90 |
| **G5: Customer Satisfaction** | CSAT on AI-assisted tickets vs. baseline | Flat or improving for ≥2 consecutive periods | Bi-weekly |
| **G6: Warranty Accuracy** | AI recommendation agreement with human decision (sampled) | ≥90% | Monthly |

**Kill criteria (any one triggers pause and review):** Two consecutive CSAT declines; any warranty error reaching a dealer without human review; dealer opt-out above 15%; G3 draft acceptance below 40% after scope adjustments; G3 below 50% at Day 45 triggers scope review.

**Pilot phases:** Month 1 — setup, baseline, Kendra indexing. Month 2–3 — AXS drivetrain tickets only, 100% human review. Month 4–5 — expand to Hammerhead devices. Month 6 — Day 90 go/no-go decision. Month 7–12 — scale to full product catalog if go decision confirmed.

**Financial impact:** Expected Year 1 net value of ~$5.0M ($1.6M support efficiency, $0.4M warranty fraud reduction, $3.0M retained customer revenue) on ~$0.5M implementation cost.

### Organizational Enablers — Pilot A

**Talent:** One internal product owner (dedicated, not secondary responsibility); one integration engineer (internal or contract); one support team lead managing agent adoption; one part-time data analyst for metrics.

**Data:** AXS and Hammerhead documentation must be audited and indexed before launch. Ninety days of historical Zendesk ticket data required to establish baseline metrics.

**Leadership:** One named C-suite sponsor owns the pilot outcome. The pilot product owner has pre-authorized rollback authority and reports at the existing weekly leadership cadence.

---

## 6. Pilot B: Demand Forecasting and Supply Chain Optimization (Month 24–36)

### The Problem

SRAM has no systematic demand forecasting engine. Production and inventory decisions are made without a model connecting order history, dealer sell-through, or seasonal patterns. The result: stockouts that lose sales, overproduction that drives markdowns, and reactive supply chain management. This is already an internal priority — the Month 24 start reflects data infrastructure dependency, not priority ranking.

### Integration Into Current Processes

**Current state:** Production planning driven by brand-level judgment and informal historical patterns; no centralized inventory visibility; dealer sell-through not systematically tracked.

**Pilot state:** Amazon SageMaker forecasting model ingests historical orders, dealer sell-through, inventory levels, and seasonal signals from the Step 2 lakehouse → generates SKU-level demand forecasts (13/26/52-week rolling) → supply chain planners review recommendations in PowerBI dashboard → planners approve or override with documented reason codes → model learns from override patterns.

Planners retain full decision authority. The model converts them from reactive problem-solvers into proactive decision-makers reviewing data-driven recommendations.

**Pilot phases:** Month 22–24 — data readiness audit (go/no-go gate: ≥85% data quality on pilot SKUs). Month 24–27 — SageMaker model development and back-test validation. Month 27–30 — shadow mode (model runs in parallel; planners observe but do not act on recommendations). Month 30–36 — active pilot (planners decide using model output). Month 36 — full evaluation and scale decision.

### SMART Goals

| Goal | Metric | Target | Timeline |
|------|--------|--------|----------|
| **G1: Forecast Accuracy** | MAPE on pilot SKU demand forecast | ≤15% (back-test); ≤20% (live) | Month 27; Month 30 |
| **G2: Stockout Reduction** | Stockout rate on pilot SKUs vs. baseline | 30% reduction | Month 36 |
| **G3: Markdown Reduction** | Markdown/write-down rate on pilot SKUs vs. baseline | 25% reduction | Month 36 |
| **G4: Inventory Efficiency** | Inventory turns on pilot SKUs vs. baseline | +15% improvement | Month 36 |
| **G5: Planner Adoption** | % of model recommendations acted upon (not overridden) | ≥60% | Month 36 |
| **G6: Financial Impact** | Annualized avoidable inventory loss recovered | ≥$1.6M | Month 36 evaluation |

**Kill trigger:** MAPE >25% at Month 30 → retrain before proceeding to active pilot.

**Financial impact:** Expected $4.8M annualized savings at full deployment ($2.5M stockout recovery, $1.5M markdown reduction, $0.8M carrying cost savings) on ~$1.2M annual operating cost.

### Organizational Enablers — Pilot B

**Talent:** One ML/data science lead (new hire, start Month 20); two supply chain analysts redeployed from existing team with AI workflow training; one data engineer (continuity from Step 2 team).

**Data:** Minimum three years of unified, SKU-level order history from the Step 2 lakehouse is required before model training begins. This is a hard gate — piloting on fragmented data produces unreliable outputs and undermines confidence in the approach.

**Leadership:** Supply Chain Director or COO as named pilot owner with monthly steering committee review. Planners must document all model overrides — this is non-negotiable policy, not optional, as override data trains future model iterations.

---

## 7. Step 4: Revenue and Innovation (Month 36–60+)

Step 4 initiatives are scoped and prioritized based on Step 1–3 outcomes. The four primary opportunities are:

- **AXS Intelligence Platform (Month 36–54):** Unify cross-brand telemetry into a rider performance intelligence layer; deliver via premium AXS app subscription tiers. Requires full lakehouse telemetry integration and cross-brand product alignment.
- **OEM Proposal Automation (Month 36–48):** Salesforce AgentForce with CPQ to accelerate proposal generation and improve OEM win rates. Fastest Step 4 initiative to deploy given Salesforce CRM is live.
- **Compatible Upgrade Recommendations (Month 42–60):** SageMaker recommendation engine driving cross-sell through dealer and DTC channels, powered by AXS telemetry and registered component data.
- **Generative Design and R&D Acceleration (Month 42–60):** Digital twin testing, AI-assisted patent search, and field telemetry informing new product design. Frees engineering capacity for higher-value innovation.

---

## 8. Leadership and Governance

The most important organizational decision in this plan is naming a **dedicated C-suite AI Sponsor** — one person with primary accountability for the transformation program, not a committee and not a secondary responsibility layered onto an existing role. This role must be designated before the warranty pilot launches.

**Governance cadence:**

| Cadence | Participants | Purpose |
|---------|-------------|---------|
| Weekly (pilot periods) | Pilot Owner, AI Sponsor, Support/SC Lead | Metrics review; issue escalation |
| Monthly | C-suite sponsors, Pilot Owners | Phase gate readiness; resource decisions |
| Quarterly | Full C-suite | Strategic alignment; Step 4 prioritization |

---

## 9. Three CEO Actions to Start

1. **Approve the Warranty Support Pilot now.** Name one internal product owner. Approve ~$500K setup budget. Set the Day 90 go/no-go decision date.
2. **Name the C-suite AI Sponsor.** One person. Primary accountability. This single decision determines whether Steps 2 and 3 succeed organizationally.
3. **Authorize Step 2 data infrastructure.** Begin SAP/Salesforce vendor selection in parallel with the warranty pilot. Every month of delay on data foundations delays demand forecasting and every Step 4 initiative by an equal amount.

---

## 10. Gantt Chart: Steps 1–3 Detail (Month 1–36)

*`████` = Active build | `────` = Ongoing operations | `[*]` = Go-live | `[✓]` = Decision gate*

```
INITIATIVE                          │Q1  │Q2  │Q3  │Q4  │Q5  │Q6  │Q7  │Q8  │Q9  │Q10 │Q11 │Q12 │
                                    │M1-3│M4-6│M7-9│M10 │M13 │M16 │M19 │M22 │M25 │M28 │M31 │M34 │
                                    │    │    │    │-12 │-15 │-18 │-21 │-24 │-27 │-30 │-33 │-36 │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 1: EARLY WINS                  │    │    │    │    │    │    │    │    │    │    │    │    │
  Copilot/Claude Code (Engineering) │████│████│████│████│────│────│────│────│────│────│────│────│
  Microsoft CoPilot (Business)      │████│████│████│████│────│────│────│────│────│────│────│────│
  AI Innovation Forums (Quarterly)  │    │[G] │    │[G] │    │[G] │    │[G] │    │    │    │    │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 2: DATA FOUNDATIONS            │    │    │    │    │    │    │    │    │    │    │    │    │
  ERP (SAP) Selection + Contract    │████│████│    │    │    │    │    │    │    │    │    │    │
  Salesforce CRM Implementation     │████│████│████│████│[*] │    │    │    │    │    │    │    │
  AWS Lakehouse Architecture        │████│████│    │    │    │    │    │    │    │    │    │    │
  Data Pipelines (Shopify/Support)  │    │████│████│████│████│    │    │    │    │    │    │    │
  SAP ERP Go-Live (Core Brands)     │    │    │████│████│████│[*] │    │    │    │    │    │    │
  AXS + Hammerhead Telemetry        │    │    │    │████│████│████│████│    │    │    │    │    │
  PowerBI / Databricks Deployment   │    │    │    │████│████│████│    │    │    │    │    │    │
  Data Quality Gate (Forecasting)   │    │    │    │    │    │    │    │[✓] │    │    │    │    │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 3A: WARRANTY SUPPORT PILOT     │    │    │    │    │    │    │    │    │    │    │    │    │
  Pilot Design + Baseline Setup     │████│    │    │    │    │    │    │    │    │    │    │    │
  Kendra + Bedrock Integration      │████│████│    │    │    │    │    │    │    │    │    │    │
  AXS Drivetrain Ticket Rollout     │    │████│████│    │    │    │    │    │    │    │    │    │
  Day-45 Scope Checkpoint           │    │[✓] │    │    │    │    │    │    │    │    │    │    │
  Hammerhead Ticket Expansion       │    │    │████│████│    │    │    │    │    │    │    │    │
  Warranty Claim AI Track           │    │    │████│████│    │    │    │    │    │    │    │    │
  Day-90 Go/No-Go Decision          │    │    │    │[✓] │    │    │    │    │    │    │    │    │
  Scale to Full Product Catalog     │    │    │    │    │████│████│████│────│    │    │    │    │
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 3B: DEMAND FORECASTING PILOT   │    │    │    │    │    │    │    │    │    │    │    │    │
  Data Readiness Audit + Gate       │    │    │    │    │    │    │    │[✓] │    │    │    │    │
  SageMaker Model Development       │    │    │    │    │    │    │    │    │████│████│    │    │
  Back-Test Validation (MAPE Gate)  │    │    │    │    │    │    │    │    │    │[✓] │    │    │
  Shadow Mode Pilot                 │    │    │    │    │    │    │    │    │    │████│████│    │
  Shadow Checkpoint (M30)           │    │    │    │    │    │    │    │    │    │    │    │[✓] │
  Active Pilot (Planners Decide)    │    │    │    │    │    │    │    │    │    │    │████│████│
  Full Evaluation + Scale Decision  │    │    │    │    │    │    │    │    │    │    │    │[✓] │
────────────────────────────────────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
[G] = Innovation Forum event   [*] = Go-live milestone   [✓] = Decision gate
```

---

## 11. Overview Gantt Chart: All Steps (Month 1–60)

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
  Pilot (AXS + Hammerhead)          │████│████│    │    │    │    │    │    │    │    │
  Scale to Full Catalog             │    │    │████│████│────│────│────│────│────│────│
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 3B: DEMAND FORECASTING         │    │    │    │    │    │    │    │    │    │    │
  Model Dev + Shadow Mode           │    │    │    │████│████│    │    │    │    │    │
  Active Pilot + Full Scale         │    │    │    │    │    │████│████│────│────│────│
────────────────────────────────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
STEP 4: REVENUE AND INNOVATION      │    │    │    │    │    │    │    │    │    │    │
  OEM Proposal Automation           │    │    │    │    │    │████│████│────│────│────│
  AXS Intelligence Platform         │    │    │    │    │    │████│████│████│████│████│
  Compatible Upgrade Recs Engine    │    │    │    │    │    │    │████│████│████│────│
  Generative Design / Digital Twin  │    │    │    │    │    │    │████│████│████│████│
────────────────────────────────────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
████ = Active build/deployment   ──── = Ongoing operations   [*] = Critical milestone
```

---

## Sources

**[1]** AI Value Creation Proposals, internal working document, March 2026. `AI_Value_Creation_Proposals.pdf`.

**[2]** Trustpilot, "SRAM Reviews." https://www.trustpilot.com/review/www.sram.com (accessed March 2026).

**[3]** SRAM AI Adoption Playbook, March 2026. `deliverables/SRAM_AI_Adoption_Playbook_wCitations.md`.

**[4]** SRAM AI Adoption Strategy reference analysis, February 28, 2026. `research/reference/sram_ai_strategy.md`.

**[5]** Reddit cycling community threads, r/cycling and r/sram, 2024–2025.
