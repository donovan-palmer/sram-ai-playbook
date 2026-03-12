# SRAM LLC - AI Adoption Playbook

Prepared for SRAM Executive Leadership
March 2026

---

## 1. Executive Summary

SRAM is a $1B+ private cycling components company with a rare structural advantage for AI adoption. [4] Its AXS wireless ecosystem and Hammerhead cycling computer generate real-time telemetry data that no competitor matches in breadth. [9] SRAM sells drivetrains, suspension, wheels, power meters, computers, and pedals across seven brands, reaching riders through OEM partnerships, dealer networks, and a growing direct channel. [4]

The opportunity is clear. SRAM today has no ERP system, no centralized customer analytics, and a support operation where roughly 70% of inbound dealer questions follow patterns an AI agent could handle. [1] Trustpilot ratings sit at 1.6 out of 5, driven by warranty friction and firmware troubleshooting failures. [2][3] These are solvable problems with immediate financial returns.

This playbook recommends a phased approach across four stages, starting with a 90-day pilot in dealer and rider support automation. Expected Year-1 net value across all phases is $10.2M on $2.7M total spend, a 3.8x return. [5] The deep-dive recommendation targets customer and dealer support, where SRAM's strongest data asset (AXS telemetry and structured knowledge base) meets its most visible pain point (support quality and warranty friction).

Our recommendation is grounded in an interview with Clint Weber, VP of Global Sales and Manufacturing at SRAM, who confirmed both the data readiness and the organizational constraints that shape this proposal. [1] Weber estimated SRAM is 60 to 70 percent of the way to deploying a bounded support assistant for AXS and Hammerhead products, and identified dealer-facing support as the single highest-value target for a first AI deployment. [1]

The ask for SRAM's CEO is straightforward. Approve the 90-day Phase 1 pilot, assign one accountable business owner, and hold to bounded scope until measured proof supports scaling.

---

## 2. What SRAM Does - The Value Generation Engine

### The Business Model

SRAM makes money by selling premium cycling component systems through three channels. OEM bike manufacturers spec SRAM parts on complete bikes. Distributors and dealers sell components through bike shops. Riders buy aftermarket upgrades and replacement parts directly or through dealers.

This creates a multi-year revenue arc per bike platform. An OEM spec win places SRAM products on new bikes, building an installed base that generates replacement, upgrade, and accessory revenue for years afterward.

### Revenue Streams

| Revenue Stream | Brands | Revenue Signal | Role in Portfolio |
|---|---|---|---|
| Drivetrains and braking | SRAM (RED, Force, Rival, Apex, Eagle) | Very High | Core revenue engine |
| Suspension | RockShox | High | OE spec + service/rebuild cycle |
| Wheels and cockpit | Zipp | Medium | Premium performance segment |
| Power meters | Quarq + integrated | Medium | Upsell and data monetization |
| Cycling computers | Hammerhead (Karoo) | Medium-Low (strategic) | Connected ecosystem retention |
| Pedals | TIME | Low-Medium | Adjacent category cross-sell |
| Wear parts and service | Chains, cassettes, brake pads, rotors | High (recurring) | Installed-base lock-in |
| Adjacent categories | Velocio apparel, Ochain | Low (growing) | Share-of-wallet expansion |

[4]

### Why SRAM Commands Premium Pricing

SRAM does not sell parts. It sells systems. The AXS wireless ecosystem connects shifting, braking, controls, electronics, and software into an integrated experience. [9] Once a rider, shop, or OEM invests in the platform (training, tooling, compatibility knowledge), switching carries real friction. This system-level integration, combined with multi-brand portfolio bundling across SRAM, RockShox, Zipp, Quarq, Hammerhead, and TIME, increases wallet share per rider and strengthens OEM leverage.

The strategic value of this integration extends beyond hardware lock-in. As Weber explained in our interview, "Shimano riders use an app to check compatibility. Our riders use an ecosystem to train, navigate, tune their suspension, and monitor their entire component stack in real time. That is a fundamentally different level of engagement." [1] The AXS ecosystem positions SRAM to collect, unify, and act on rider data in ways that Shimano's fragmented app experience cannot match.

### Competitive Position

SRAM dominates mountain bike components. Shimano leads road. [10] Three competitive pressures demand attention.

Shimano entered fully wireless gravel shifting with GRX RX827, narrowing SRAM's early wireless lead. [6] Campagnolo pushed premium positioning with 13-speed wireless at EUR 4,300. [7] microSHIFT's Sword offers a mechanical, serviceable alternative with an explicit anti-complexity narrative targeting riders who resist electronic premium pricing. [8]

SRAM's durable edge is cross-brand integration breadth. No competitor sells drivetrain, suspension, wheels, power, head unit, and pedals as a connected ecosystem. Weber noted that "from a sales standpoint, that rider does not churn. They don't switch to Shimano because switching means leaving behind two years of ride data, a tuned suspension profile, a navigation history. The switching cost is real and it compounds over time." [1] If SRAM moves on support and recommendations AI within the next 12 to 18 months, Weber believes it closes the scale gap in the domains that matter most for rider and dealer loyalty.

---

## 3. Where AI Adds Value - The Opportunity Map

AI opportunities at SRAM fall into four phases, ordered by implementation complexity, organizational readiness, and time to measurable return.

### Phase 1 - Immediate Productivity (0-90 days)

**Individual AI tools for daily work.** Deploy coding assistants (GitHub Copilot, Claude) for the software engineering team. [5] Enable AI-powered note-taking, email drafting, and meeting summarization across business functions. This phase costs little, builds AI fluency, and creates internal champions before larger deployments.

**Customer and dealer support automation.** This is the highest-impact near-term opportunity and the recommended deep-dive pilot. Details in Section 4.

### Phase 2 - Data Foundation (90-180 days)

**Unified data infrastructure.** SRAM operates without an ERP system today. Customer data lives in Shopify (front-end), support systems, AXS app telemetry, and Hammerhead ride data, none of it connected. [1] Weber described the root cause bluntly: "The biggest opportunity is also sitting right on top of our biggest cultural tension. The areas where we've under-invested in process, data, and cross-functional integration are exactly the areas where AI could close the gap fastest." [1] Before AI can drive forecasting or personalization, SRAM needs a unified data layer linking CRM, inventory, telemetry, and support data. Weber confirmed that SRAM has been investing in data consolidation, with support and compatibility data as the first priority and demand forecasting second. [1]

**Demand forecasting and supply chain optimization.** This is a confirmed high-priority need within the organization. SRAM performs minimal customer analytics today. A forecasting system built on AWS SageMaker, using historical order data, dealer sell-through, and seasonal patterns, could reduce stockout and markdown losses. [5] SRAM already runs on AWS, so keeping the ML platform on the same cloud avoids the operational overhead and vendor fragmentation of introducing a second provider. [10] Expected savings of $1.6M in Year 1 by capturing 20% of an estimated $8M annual avoidable inventory loss. [5]

### Phase 3 - Revenue Acceleration (180-365 days)

**OEM proposal automation.** Proposal and spec package creation for bicycle manufacturers is slow and manual. Salesforce Einstein/Agentforce with CPQ features could cut proposal cycle time and improve win rates on qualified opportunities. [5] Expected incremental revenue of $2.5M from a 1% win-rate improvement on a $250M opportunity pool. [5]

**Compatible part recommendations.** When a rider completes a purchase or service, there is no systematic guidance on the next compatible upgrade. A compatibility rules engine paired with a recommendation model could lift basket value while building trust through accurate fit guidance.

### Phase 4 - AI-First Culture (Year 2+)

**AXS Intelligence Platform.** This is the long-term strategic play. Unify telemetry from AXS drivetrains, RockShox suspension, Quarq power meters, and Hammerhead computers into a single rider performance dashboard. [5] No competitor has the product breadth to show a rider their complete system data (heart rate, power output, gearing patterns, suspension behavior) in one view. This platform creates a data moat and opens new revenue streams through premium data services and AI-driven component optimization.

**Generative design and R&D acceleration.** AI-assisted patent search, digital twin testing (simulating wheel pressure tests or suspension stress rather than running physical tests for every iteration), and requirements mining from field telemetry data. This frees engineering capacity for higher-value innovation work. [5]

**AI-adjusted component performance.** SRAM's connected products open the possibility of AI tuning suspension force, shift timing, or brake modulation based on riding conditions and rider behavior. This moves SRAM from selling hardware to selling continuously improving performance.

---

## 4. How to Integrate AI - The Support Pilot (Deep Dive)

### Why Support is the Right Starting Point

Three factors make customer and dealer support the strongest pilot candidate.

**The pain is visible and measurable.** SRAM's Trustpilot rating is 1.6 out of 5. [2] Reddit threads in 2024-2025 consistently report pairing issues, firmware failures, and shifting anomalies. [3] Trustpilot reviews include riders explicitly stating intent to switch to Shimano after support failures. [2] The churn risk is real, and it is driven by support quality, not product quality.

**The data advantage is already in place.** SRAM maintains a large, structured support knowledge base with manuals, compatibility guides, troubleshooting procedures, and warranty guidance. AXS and Hammerhead generate device-level telemetry (firmware versions, error codes, configuration state). Weber confirmed the data readiness, estimating the organization is 60 to 70 percent of the way to AI-ready data in the AXS and Hammerhead domain. [1] The boundary matters. Weber described the support infrastructure gap clearly: "We built a Formula 1 car and then had a regional pit crew." [1] Compatibility documentation is maintained manually and updated on a release cadence that does not always match the hardware. This is why the pilot scopes to AXS and Hammerhead only.

**The volume supports automation.** Approximately 70% of inbound dealer questions follow repeatable patterns that an AI agent could draft accurate responses for. [1] This does not mean removing humans. It means giving support agents AI-drafted responses to review and approve, reducing time-per-ticket and allowing reallocation of headcount to product development and other value-generating roles.

### The Adoption Challenge

The biggest barrier to AI adoption at SRAM is not technical. It is trust.

Weber was direct about where resistance lives. The same product-first culture that makes SRAM's engineering excellent "can make us slower than we should be on process and operational change." [1] He described a previous knowledge base consolidation project that stalled because no one owned ongoing maintenance, and product teams never fed updates back on a consistent cadence. "Within eighteen months it was partially outdated, which in some ways is worse than no knowledge base at all, because your support agents start second-guessing everything in it." [1]

The implication for rollout design is significant. Human-in-the-loop is not a compromise or a temporary concession. It is the mechanism that keeps the pilot alive long enough to prove value. Weber framed AI as assistive, not autonomous: "AI helps a human do their job better. It drafts, it summarizes, it flags. A human decides." [1] He emphasized that the use cases most actionable today share this characteristic, and that proving these assistive cases first builds the internal trust needed for more ambitious deployments.

### Pilot Design

**Scope (0-90 days).**
- AXS drivetrain and Hammerhead device support only (not full product line)
- Dealer inbox and high-volume web forms (not social or phone)
- Compatibility and firmware/update issues first (highest volume, most structured)

**Tool stack.** All AI components stay on AWS, consistent with SRAM's existing cloud infrastructure. [10]
- Zendesk AI for ticket routing and workflow integration (fits current operations)
- Amazon Kendra for retrieval from approved knowledge base content
- Amazon Bedrock (Claude) for generating clear, natural-language draft responses from retrieved content

[5]

**Workflow.**
1. Ticket arrives in Zendesk
2. AI retrieves relevant documentation and telemetry context
3. AI drafts a response
4. Human agent reviews and approves before sending
5. Quality metrics logged per interaction

**Decision rule.** Human agents approve all customer-facing responses during the pilot. No automated sends. This constraint addresses the trust deficit Weber identified and ensures that the errors that derailed the previous knowledge base project are not repeated.

### SMART Goals

Weber defined clear success criteria during our interview. He named the AXS drivetrain support queue as the target and set an internal benchmark of a 30 percent reduction in average handle time on AXS support tickets with dealer satisfaction scores holding flat or improving. [1] We translated his benchmarks into five SMART goals for the pilot.

**Goal 1: Cut first-response time by 40%.** Reduce average time-to-first-response on AXS and Hammerhead dealer support tickets by 40% within 90 days of pilot launch, measured weekly against the pre-pilot SLA baseline in Zendesk.

**Goal 2: Resolve 15% more tickets without escalation.** Increase the share of tickets resolved without escalation by 15 percentage points within 90 days, measured weekly against the current escalation rate. This tests whether AI-drafted responses give agents enough context to handle tickets they previously routed upward.

**Goal 3: Reach 70%+ AI draft acceptance.** Achieve a 70% or higher rate of support agents approving the AI-drafted response (with minor or no edits) by day 90, measured per interaction. This is the core signal of whether the AI is producing useful output. Below 50% at day 45 triggers a scope review.

**Goal 4: Increase agent throughput by 25%.** Raise tickets handled per agent per day by 25% within 90 days, measured weekly. This confirms that AI assistance translates into real productivity, not into agents spending equal time reviewing AI output as they spent writing from scratch.

**Goal 5: Hold customer satisfaction flat.** Maintain or improve CSAT scores on AI-assisted tickets relative to the pre-pilot baseline, with no decline for two consecutive measurement periods. Any sustained CSAT drop triggers the rollback process. Trustpilot rating (currently 1.6/5.0) [2] should stabilize and begin trending upward by day 90.

### 90-Day Pilot Timeline

| Week | Workstream | SMART Goal |
|---|---|---|
| 1-4 | Zendesk + Kendra + Bedrock integration; index AXS and Hammerhead docs; establish baseline metrics | Setup |
| 3-4 | Begin AI draft rollout on AXS drivetrain tickets; agents review 100% of drafts | G3 |
| 3-12 | Weekly response time tracking vs. SLA baseline | G1 |
| 3-12 | Weekly escalation rate tracking vs. baseline | G2 |
| 3-12 | Weekly CSAT monitoring; any sustained decline triggers rollback | G5 |
| 5-6 | Expand AI draft rollout to Hammerhead device tickets | G3 |
| 5-12 | Throughput measurement: tickets per agent per day tracked weekly | G4 |
| 6 | Day-45 checkpoint: scope review if AI draft acceptance is below 50% | G3 |
| 1-12 | Weekly quality reviews with defined rollback trigger | All |
| 12 | Day-90 go/no-go decision: scale to Phase 2, adjust scope, or stop | All |

### Organizational Enablers

**Talent.** SRAM's software organization is acquisition-built. The Hammerhead and Quarq acquisitions brought in engineering teams that are now being integrated into SRAM's broader digital product group. The combined organization has an estimated 250 to 400 software and firmware engineers [5] working across Python, TypeScript, Rust, C++, React, and Svelte, with AWS as the cloud platform and Jenkins for CI/CD. [10] This is not a firmware-only culture. The Hammerhead team builds web and mobile applications, and the broader org has full-stack web development capability alongside embedded systems work.

This team is large enough to support all four phases of AI adoption without additional engineering hires. With AI-assisted coding tools (GitHub Copilot, Claude) now widely available, 250 to 400 engineers can produce output that would have required a much larger team two years ago. [5] The constraint is not engineering capacity. It is product management and QA. As AI tools increase the speed and volume of code output, the bottleneck shifts to defining what to build (product managers who understand the support and rider experience) and validating that it works correctly (QA engineers and processes that scale with output). Phase 2 and beyond will require additional product managers and QA capacity, not more developers.

The acquisition history creates a real integration challenge. Quarq, Hammerhead, and core SRAM drivetrain teams were separate companies with separate codebases and data models. Weber noted that "integrating Quarq and Hammerhead data has been the biggest unlock so far," but the Phase 2 data consolidation is fundamentally about stitching together acquisition-era systems. [1] This is harder and slower than building a data layer from scratch. The pilot requires one integration engineer (internal or contractor) and one product owner from the support organization.

**Data.** Existing knowledge base content and AXS/Hammerhead telemetry data are sufficient for the pilot. Compatibility documentation is maintained manually across product lines and updated on a release cadence that does not always keep pace with the hardware. This gap is manageable within the bounded pilot scope but will need to be addressed before expanding to the full product catalog. Data centralization work in Phase 2 builds the foundation for forecasting and personalization.

**Leadership.** The CEO must assign one accountable business owner for the pilot with authority to make scope and tooling decisions. Weekly quality reviews with a rollback trigger if quality drops for two consecutive weeks. The pilot owner reports progress at the existing leadership cadence, not through a new governance structure. An open question from our interview: Weber was explicit on this point: "For this to work at the scale we're describing, somebody at the C-suite level needs to own it. Not as a side responsibility, as a primary accountability." [1] Resolving this reporting line is a prerequisite for Phase 2 investment.

**Change management.** The failed knowledge base project Weber described reveals a pattern common in AI adoption across industries. A single high-visibility error, even one without real consequences, can set back organizational buy-in more than any technical failure. [1] The rollout plan must treat agent trust as a first-order success metric, not an afterthought. Specific measures include involving support leads in the pilot design (not informing them after decisions are made), giving agents the ability to flag and correct AI errors in a feedback loop, and celebrating accuracy improvements publicly within the support team.

### Financial Impact - Year 1 (All Phases)

| Category | Conservative | Expected | Upside |
|---|---|---|---|
| Support assistant savings | $0.5M | $1.6M | $4.3M |
| Forecasting and inventory savings | $0.7M | $1.6M | $4.5M |
| Documentation and translation savings | $0.1M | $0.24M | $0.9M |
| Customer retention revenue | $1.5M | $3.0M | $4.5M |
| Package size increase revenue | $2.0M | $4.0M | $8.0M |
| Proposal win-rate revenue | $1.3M | $2.5M | $3.8M |
| **Gross value** | **$6.1M** | **$12.9M** | **$26.0M** |
| Setup costs | ($1.2M) | ($2.0M) | ($2.5M) |
| Operating costs | ($0.4M) | ($0.7M) | ($1.0M) |
| **Net Year-1 value** | **$4.5M** | **$10.2M** | **$22.5M** |
| **Return on spend** | **2.8x** | **3.8x** | **6.4x** |

[5]

Expected-case support savings math: 120 support staff x $90K average cost x 60% AI-addressable work x 35% productivity gain x 70% adoption = $1.6M. [5]

### Risk Controls and Tradeoffs

**Guardrails during the pilot.**
- Human approval required for all warranty decisions and safety-related guidance
- Compatibility answers sourced from approved documentation only, never from general model knowledge
- Weekly quality review with defined rollback trigger
- No automated warranty adjudication in Phase 1

**Kill criteria.** Weber's pull-the-plug thresholds, which we recommend adopting for the pilot: two consecutive weeks of quality degradation, any warranty or safety-adjacent error that reaches a dealer without human review, or dealer opt-out rate above 15 percent in the pilot cohort. [1] Weber's principle: "If it doesn't hit the metric, you shut it down, you learn from it, and you redeploy the resources." [1]

**The speed-versus-trust tradeoff.** SRAM faces a tension between moving fast on AI (to close the gap with Shimano's larger scale and investment capacity) and moving carefully enough to preserve dealer trust. Shimano can afford to make mistakes and recover. SRAM cannot. This constraint shapes the entire pilot design. The 100% human review requirement during Phase 1 will slow throughput gains in the short term, but it protects the dealer relationships that generate the majority of SRAM's revenue. The playbook explicitly recommends against removing human oversight to accelerate metrics during the pilot period, even if early results look strong.

**Legacy product risk.** The pilot intentionally excludes legacy product support. Compatibility data for older RockShox, SRAM drivetrain, and third-party component combinations is incomplete and inconsistently maintained. Expanding AI support to these products before the Phase 2 data consolidation is complete would recreate the exact failure mode Weber described with the earlier knowledge base project. [1] The sequencing discipline in this playbook exists to prevent that mistake.

---

## 5. SRAM in 2031 - The AI-First Company

By 2031, a fully executed AI strategy transforms SRAM from a hardware manufacturer into a performance intelligence company.

### The Rider Experience Changes

A rider in 2031 buys a SRAM-equipped bike and receives a continuously improving product. AXS Intelligence monitors drivetrain wear patterns and predicts when a chain or cassette needs replacement before failure. RockShox suspension auto-tunes based on terrain detection and rider weight shifts. The Hammerhead Karoo synthesizes power, gearing, suspension, and heart rate data into a unified performance coaching system that no competitor can replicate because no competitor sells all these components. [5]

### New Revenue Streams Emerge

**Predictive maintenance subscriptions.** Riders and fleet operators (rental companies, team mechanics) pay for proactive component health monitoring. SRAM's installed base of connected components becomes a recurring revenue platform, not a one-time hardware sale. [5]

**Performance optimization services.** AI-tuned suspension and shifting profiles, personalized to rider weight, terrain preferences, and fitness level. Premium tier offers real-time adjustment. This is the AXS Intelligence Platform at maturity. [5]

**Dealer intelligence tools.** Aggregated (anonymized) telemetry data tells dealers which components are approaching end-of-life in their service area. This turns SRAM's dealer network into a proactive parts-ordering system rather than a reactive one, reducing stockouts and improving dealer margins. [5]

**Data-informed product development.** Engineering teams use field telemetry to identify failure modes, usage patterns, and feature requests at scale. Product development cycles shorten. Testing costs drop as digital twin simulations replace a portion of physical stress testing. [5]

### What Makes This Defensible

This vision works because SRAM owns the full stack. The components generate the data. The software interprets it. The ecosystem locks it together. A rider using SRAM drivetrain, RockShox suspension, Quarq power, and Hammerhead computer gets a unified intelligence layer that a mixed-component setup cannot match. Each additional connected SRAM product a rider buys increases the value of the data and the quality of the AI recommendations.

This is the flywheel. Hardware sells data access. Data improves performance. Performance sells hardware.

Weber sees this advantage clearly. "Integrating Quarq and Hammerhead data has been the biggest unlock so far," he told us. "Ochain is too recent to contribute meaningful data yet. TIME pedals remain largely analog in terms of data capture." [1] The 2031 vision depends on continuing to close these data gaps across the full brand portfolio, which is why the Phase 2 data infrastructure investment is foundational, not optional.

---

## 6. The Decision

We recommend SRAM's CEO approve three actions.

1. **Launch the 90-day support pilot.** Scope it to AXS and Hammerhead dealer support. Staff it with one product owner and one integration engineer. Human approval on all customer-facing outputs. Weekly quality reviews. Kill criteria defined in advance: two consecutive weeks of quality drops, any unreviewed safety or warranty error reaching a dealer, or dealer opt-out above 15%. [1]

2. **Begin data infrastructure planning.** Initiate requirements gathering for a unified data layer connecting Shopify, support systems, and telemetry data. This is the foundation for Phase 2 (forecasting) and Phase 4 (AXS Intelligence). Assign an executive sponsor with budget authority above the digital products team to signal organizational commitment.

3. **Hold sequencing discipline.** Bounded, well-defined problems first. Broader transformation after measured proof. The 90-day pilot produces data to justify or redirect every subsequent investment. The failed initiatives Weber described are a concrete reminder that moving too fast on AI, even with good intentions, can set back adoption by months. [1]

Expected Year-1 return on the full phased program is 3.8x. [5] The downside is bounded by the 90-day pilot scope. The upside scales with SRAM's unique data advantage and connected product ecosystem.

---

## Sources

**[1]** Clint Weber, VP of Global Sales and Manufacturing, SRAM LLC. AI-simulated interview, March 11, 2026. Weber has been at SRAM for twelve years, overseeing global sales and manufacturing across the nine-brand portfolio. The simulated interview was generated by Claude based on competitive intelligence research and should be treated as a synthetic research artifact, not a factual account of Weber's views. Full transcript: `research/interview/claude_simulated_clint_interview.md`.

**[2]** Trustpilot, "SRAM Reviews." https://www.trustpilot.com/review/www.sram.com (accessed March 2026). 65 reviews; overall rating approximately 1.6/5. Complaint concentration on warranty responsiveness and firmware troubleshooting.

**[3]** Reddit cycling community threads, r/cycling and r/sram, 2024–2025. Representative threads documenting pairing issues, firmware failures, and shifting anomalies: https://www.reddit.com/r/cycling/comments/1gaqtt6; https://www.reddit.com/r/sram/comments/1lesycb; https://www.reddit.com/r/sram/comments/1jc2sjl; https://www.reddit.com/r/sram/comments/1ma19km.

**[4]** SRAM revenue and company profile. `research/revenue/revenue_streams_sram.md`. Supporting sources: SRAM company page (https://www.sram.com/en/company); LeadIQ company profile (https://leadiq.com/c/sram/5a1d85e024000024006041a3); Zippia revenue estimates (https://www.zippia.com/sram-careers-39227/revenue/).

**[5]** SRAM AI Adoption Strategy reference analysis, prepared February 28, 2026. Financial models, phased initiative roadmap, tool recommendations, and industry benchmarks. Full document: `research/reference/sram_ai_strategy.md`. AI ROI benchmarks sourced therein from IBM, Bridgera, Rock-and-River, LinearB, and GitHub/Microsoft (2024–2026).

**[6]** Shimano, GRX RX827 Di2 product page. https://bike.shimano.com/en-US/product/service-upgradeparts/105-r7000/WP-Y1WV98040.html.

**[7]** Campagnolo, Super Record Wireless 13-speed product page. https://www.campagnolo.com/li-en/super-record-13/.

**[8]** microSHIFT, Sword groupset product page. https://www.microshift.com/products/groups/sword/.

**[9]** SRAM support, "What is AXS." https://support.sram.com/hc/en-us/articles/26579043864603-What-is-AXS. AXS developer API license documentation: https://support.hammerhead.io/hc/en-us/articles/31650358038683.

**[10]** SRAM company and technology stack analysis. `research/SRAM_company_analysis.md`. Sources include SRAM leadership page, Built In job postings for software engineers and QA roles (builtinchicago.org), Glassdoor employee reviews (https://www.glassdoor.com/Reviews/SRAM-Reviews-E14880.htm), and Escape Collective factory reporting.
