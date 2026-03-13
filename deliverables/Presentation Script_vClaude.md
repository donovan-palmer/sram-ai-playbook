# SRAM AI Adoption Playbook — Presentation Script

*Prepared for AIML 950 | Human and Machine Intelligence | Northwestern Kellogg | March 2026*
*Estimated delivery time: 8–9 minutes at a measured pace. Trim Slides 12, 13, or either build sequence (7–10 or 17–18) if time is tight and you need to reach 6–7 minutes.*

---

## TALKING POINTS BY SLIDE

**Slide 1 — Title**
- Frame the ask: a pragmatic, phased AI roadmap for SRAM executive leadership

**Slide 2 — The Business**
- SRAM is a $1B+ private company with 6 brands forming one connected cycling ecosystem
- Distribution across OEM, dealer, and DTC channels creates a multi-year customer journey

**Slide 3 — Competitive Advantage**
- #1 in MTB globally; no competitor matches SRAM's cross-brand integration breadth
- The Trustpilot 1.6/5 rating is the vulnerability — support quality, not product quality, is the threat to the moat

**Slide 4 — The Strategy**
- Four sequential steps: democratize AI tooling → data infrastructure → operational pilots → revenue innovation
- Each step gates the next; sequencing discipline is the plan's core logic

**Slide 5 — Step 1: AI Tooling**
- GitHub Copilot/Claude Code for engineers; Microsoft CoPilot for business staff; $300K/yr
- Goal is fluency and champions, not cost savings — net benefit ~$700K/yr

**Slide 6 — Step 2: Data Infrastructure**
- SRAM has no centralized ERP, CRM, or data warehouse today — that is the single biggest barrier
- $10M AWS-native lakehouse investment; enables $36.6M/yr in downstream value; Steps 3B and 4 cannot happen without it

**Slides 7–10 — Where AI Adds Value (build)**
- 12 initiatives across engineering, sales, supply chain, and support
- Support is the recommended starting point: highest domain knowledge, most measurable, no data infrastructure dependency

**Slide 11 — Step 3A: The Problem**
- 1.6/5 Trustpilot driven by support failure, not hardware failure
- 70% of dealer tickets follow repeatable patterns that an AI agent can draft — today it takes 4 hours; target is 2.5

**Slide 12 — Step 3A: The Pilot**
- Bounded scope: AXS and Hammerhead tickets only; three systems (Zendesk, Kendra, Bedrock); human approves every response
- Kill switch: two weeks of quality decline triggers full rollback

**Slide 13 — Step 3A: Metrics**
- Five SMART goals: response time −40%, escalation rate +15pts, draft acceptance >70%, throughput +25%, CSAT flat
- Day-90 scope review; Day-120 formal go/no-go

**Slide 14 — Step 3A: Financials**
- $500K setup; $300K/yr operating; gross benefits include $400K warranty accuracy + efficiency gains + customer retention upside
- 12-month pilot with scale to full catalog contingent on Day-120 gate

**Slide 15 — Step 3B: Demand Forecasting**
- No forecasting system exists at SRAM today — highest near-term operational priority per SRAM leadership
- Requires Step 2 data lakehouse as a hard gate; SageMaker model trained on unified order, sell-through, and seasonal data

**Slide 16 — Step 3B: Financials**
- $500K setup; $700K/yr operating; $4.8M gross benefit; ~$4.1M net annually
- Plus one-time working capital release from inventory reduction; planner adoption target >60%

**Slides 17–18 — What Could Be (build)**
- Four new revenue streams enabled by the data foundation: AXS Intelligence, predictive maintenance, AI-tuned performance, dealer intelligence
- Hardware sells data access → data improves performance → performance sells hardware

**Slide 19 — Step 4: New Revenue**
- $10.5M total investment; $32.5M/yr at scale across four initiatives
- AXS Intelligence is the centerpiece at ~$20M ARR; no competitor has the product breadth to replicate it

**Slide 20 — Risks**
- Three named risks: dealer trust fragility, no executive sponsor for data, AI hype creating false expectations
- All three are manageable with the right governance decisions before the pilot launches

---

## PRESENTATION SCRIPT

---

### Slide 1 — Title

Good [morning/afternoon]. Today we're presenting an AI adoption playbook for SRAM — a phased, pragmatic roadmap designed to strengthen your competitive moat, improve operating efficiency, and unlock new revenue. We'll cover both the near-term pilots we recommend starting immediately and where this takes SRAM by 2031.

---

### Slide 2 — The Business

SRAM is a $1B-plus private company built around one core insight: cycling components work better as a connected system than as individual products. Six brands — SRAM drivetrains, RockShox suspension, Zipp wheels, Quarq power meters, Hammerhead computers, and TIME pedals — all communicate through the AXS wireless ecosystem. Customers come in as OEM bike buyers and stay through aftermarket upgrades, service, and performance tools. That multi-year customer journey is SRAM's competitive trap, and it's exactly what makes the AI opportunity here so significant.

---

### Slide 3 — Competitive Advantage

SRAM holds the number one market share position in mountain biking globally. No competitor sells drivetrains, suspension, wheels, computers, and pedals as a single connected platform — that integration breadth is the moat. But there's one number on this slide that should concern this room: a 1.6 out of 5 on Trustpilot. That rating isn't driven by hardware failures. It's driven by support failures — firmware pairing issues, compatibility confusion, warranty friction. Riders love the product. They're leaving because of what happens after the sale. That is both the problem and the first opportunity.

---

### Slide 4 — The Strategy

Our recommendation is a four-step program. Step one democratizes AI tooling across the organization — low cost, fast to deploy, builds internal fluency. Step two builds the data infrastructure that everything else depends on. Step three deploys AI to the two highest-value operational problems: customer support and demand forecasting. Step four is where SRAM becomes an AI-first company — new subscription revenue, smarter products, and a widened competitive moat. The sequencing is the strategy. Each step enables the next. You cannot skip to Step 4.

---

### Slide 5 — Step 1: Democratize AI Tooling

Step one has no new hires, no new infrastructure, and no meaningful disruption to current workflows. GitHub Copilot and Claude Code go to the software engineering team — this accelerates the technical build work that Steps 2 through 4 require. Microsoft CoPilot rolls out to business functions for meeting notes, email, and summarization. Quarterly AI innovation forums surface grassroots use cases and identify the internal champions who will own future phases. Total cost is roughly $300,000 per year with an estimated $1 million per year in labor productivity savings — net benefit around $700,000. The real return here is organizational readiness.

---

### Slide 6 — Step 2: Enterprise Data Consolidation

This is the most important investment in the plan, and the one that doesn't get headlines. SRAM operates today without a centralized ERP, CRM, or data warehouse. Customer data lives in Shopify. AXS telemetry is siloed from Hammerhead ride data. SAP inventory data never touches Salesforce dealer data. That fragmentation makes enterprise AI impossible. We're recommending a $10 million, 24-month investment in an AWS-native data lakehouse — built on infrastructure SRAM already uses. The standalone return is minimal. The downstream value it unlocks across Steps 3B and 4 is $36.6 million per year. This is the foundation. It starts now, in parallel with everything else.

---

### Slides 7–10 — Where AI Adds Value

Across SRAM's four business functions — engineering, sales, supply chain, and support — we've identified 12 distinct AI opportunities. *(advance through build)* The question isn't whether AI applies to SRAM. It clearly does across every function. The question is where to start. Our answer is support. Domain knowledge is high, outcomes are measurable within 90 days, and it doesn't require the data lakehouse to be live. It's the proving ground for everything that follows.

---

### Slide 11 — Step 3A: The Problem

Here's what's happening in SRAM's support queue today. A dealer emails a question — say, which AXS derailleur firmware works with a 2024 Eagle cassette. An agent opens a 200-page compatibility PDF, searches wikis and past tickets, writes the answer from scratch, double-checks the part numbers, and sends a response roughly four hours later. That same pattern repeats for 70% of all inbound tickets. Every single day. Multiply that across AXS and Hammerhead support volume and you have a structurally inefficient operation that is actively generating Trustpilot reviews telling riders to switch to Shimano.

---

### Slide 12 — Step 3A: The Pilot

The pilot is deliberately narrow. AXS and Hammerhead dealer support tickets only. Three systems: Zendesk receives the ticket, Amazon Kendra searches approved SRAM documentation, Amazon Bedrock drafts a response citing the source document. The support agent reviews, edits if needed, and approves before anything reaches a dealer. Human approval on every response — no exceptions. Two consecutive weeks of quality decline triggers an automatic rollback. This is not a bet-the-brand deployment. It is a bounded experiment with defined success criteria and a built-in kill switch.

---

### Slide 13 — Step 3A: What We Measure

We measure five things: first response time cut by 40%, first-contact resolution rate up 15 points, AI draft acceptance above 70%, agent throughput up 25%, and dealer CSAT holding flat. Any metric that misses its Day-90 early warning threshold triggers a specific corrective action before the Day-120 formal go/no-go decision. Weber set the bar in our conversation with him: 30% reduction in handle time with dealer satisfaction scores holding. Our targets exceed that bar.

---

### Slide 14 — Step 3A: Financials and Timeline

Setup cost is $500,000 — integration engineering, knowledge base build, product owner time. Annual operating cost runs roughly $300,000 in platform licensing and maintenance. On the benefit side, warranty claim accuracy improvement alone is worth approximately $400,000 annually, before counting efficiency gains in the support department or the revenue impact of reduced churn. The 12-month pilot timeline builds through integration in months one and two, AXS rollout through month three, Hammerhead expansion through month six, and scale to the full product catalog contingent on passing the Day-120 gate.

---

### Slide 15 — Step 3B: Demand Forecasting

Clint Weber told us directly that demand forecasting is the most actionable near-term opportunity SRAM sees internally. That view is consistent with what we found: SRAM has no forecasting system today. Production planning runs on brand-level judgment with no centralized inventory visibility and no systematic tracking of dealer sell-through. The result is stockouts that absorb margin through rush shipping and overstocks that clear at markdown. Amazon SageMaker, trained on the unified lakehouse data, runs first in shadow mode alongside existing planner decisions, then moves to active pilot with full planner override authority. This is gated behind the Step 2 data foundation — which is why that investment starts immediately.

---

### Slide 16 — Step 3B: Financials and Timeline

Setup is approximately $500,000. Annual operating cost is $700,000 — data science lead, SageMaker compute, data engineering. Annual gross benefit is $4.8 million from stockout loss recovery and markdown reduction, yielding approximately $4.1 million net annually. There is also a one-time working capital release from inventory reduction that is difficult to size precisely but material. Planner adoption target is greater than 60% of model recommendations acted upon. This is a 9-times return on operating cost once the program reaches steady state.

---

### Slides 17–18 — What Could Be

If Steps 1 through 3 execute as planned, SRAM exits year three with something no competitor can replicate: a unified data asset spanning drivetrain performance, suspension behavior, power output, GPS ride data, and component health across millions of connected devices. *(advance)* That asset enables four new revenue streams. AXS Intelligence becomes a premium subscription tier — a unified rider performance dashboard at a price point Peloton and Garmin cannot match because neither has SRAM's product breadth. Predictive maintenance turns the installed base into recurring revenue. AI-tuned performance means components improve after purchase. Dealer intelligence turns telemetry into proactive inventory management. Hardware sells data access. Data improves performance. Performance sells hardware.

---

### Slide 19 — Step 4: New Revenue Streams

Step 4 totals roughly $10.5 million in investment across four initiatives, generating $32.5 million per year at scale. AXS Intelligence is the centerpiece at approximately $20 million in annual recurring revenue. OEM proposal automation adds $2.5 million annually from a 1% improvement in win rate. Compatible upgrade recommendations add $4 million annually in cross-sell and dealer inventory lift. Generative design and R&D acceleration compounds the product pipeline. These are not speculative outcomes — they are the direct result of the data infrastructure and organizational trust built in Steps 1 and 2.

---

### Slide 20 — Trade-offs and Risks

We want to name three risks honestly. First, dealer trust is fragile. One confidently wrong answer from the AI reaches a dealer and the support team loses credibility built over years. The kill criteria exist for this reason — one safety error triggers full rollback. Second, data consolidation has no executive sponsor today. Clint Weber owns sales and manufacturing, not the ERP, CRM, or inventory systems. Step 2 stalls without a single senior leader with cross-functional authority to enforce it. Third, AI hype will create unrealistic internal expectations in an engineering culture that values precision. The pilot needs to be framed as an experiment with defined success and failure criteria — not a transformation announcement.

The ask for this room is three decisions: launch the support pilot, name the C-suite data sponsor, and authorize the Step 2 infrastructure investment. Those three actions set the full program in motion.

Thank you.
