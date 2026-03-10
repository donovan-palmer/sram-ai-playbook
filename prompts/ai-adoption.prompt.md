**PROMPT:**

You are a strategic business consultant. Create a **1-page executive outline** for SRAM LLC on how the company is positioned for AI adoption, with a clear focus on:
- lowering cost,
- increasing value in existing revenue streams, and
- creating new revenue opportunities.

Use **plain language only**. Avoid technical jargon unless briefly explained in simple terms.

## Output Goal

Write this as if it is going to SRAM's CEO. Make it direct, practical, and decision-oriented.
The output must support two uses:
- a clean Markdown executive outline, and
- a website/executive HTML version that uses cards and grids while preserving the exact same content.

Do not use `[FACT]` or `[ASSUMPTION]` labels.
Do not reference `analysis.md`.

## Required Structure

Use the exact section flow below:

1. **Where SRAM Stands Today**
- 2-3 short sentences on why SRAM is in a good position to adopt AI.
- Explicitly state what SRAM stands for (Scott, Ray, and Sam).
- Explain "connected workflows" in plain terms using AXS/Hammerhead examples (for example: setup, firmware updates, diagnostics, usage data).
- Include this principle clearly: highest theoretical upside is not always the best first priority.
- State that the first wave should focus on well-bounded, clearly defined problems with strong internal domain knowledge.

2. **Priority Areas: Process, Problem, Tool, and Value**
- Provide a table with these columns:
  - `Priority`
  - `Business Process`
  - `Main Problem Today`
  - `AI Tool Choice`
  - `Year 1 Cost Savings`
  - `Year 1 Revenue Gain / Business Value`
- Include at least 4 core rows:
  - Rider/dealer support, warranty, compatibility help
  - Demand forecasting and inventory allocation
  - Bicycle manufacturer proposals and package design
  - Technical documentation and translation
- Include a 5th optional/Phase 3 row for:
  - Compatible next-part recommendations at end of customer journey
- Include a 6th Phase 3 row for:
  - Product development workflow support (requirements mining, firmware test acceleration, design-review prep)
- For each row, include simple back-of-the-envelope math in one line.
- In the `AI Tool Choice` explanation, explain why each named tool is the right fit for that specific process (workflow fit, data fit, speed-to-value).

3. **Total Year 1 Business Case**
- Show totals as three-number scenarios in this format:
  - `conservative / expected / upside`
- Add one plain-language line explaining what those three values mean.
- Include:
  - total value before costs
  - one-time setup cost
  - ongoing Year 1 operating cost
  - net Year 1 value
- Include a simple expected-case return line (for example: expected net value divided by expected total spend).

4. **Year 1 Net Financial Picture, Rollout, and Risk Controls**
- Keep this as one integrated section that combines:
  - financial summary,
  - rollout sequence, and
  - risk controls.
- 0-90 days: narrow first launch with this exact starting scope:
  - Product scope: AXS drivetrains + Hammerhead devices.
  - Channel scope: dealer support inbox + top-volume web support form entries.
  - Task scope: compatibility checks, firmware/update guidance, and standard troubleshooting.
  - Pilot decision rule: AI drafts responses; human agents approve all customer-facing responses.
- 90-180 days: expand to next bounded process.
- 180-365 days: expand to later-stage processes.
- Explicitly state: do not build a brand-new enterprise platform in Phase 1.
- Include risk controls such as:
  - human approval for warranty/safety exceptions,
  - approved-source compatibility answers only,
  - weekly quality review with rollback triggers.

5. **CEO Decision Needed**
- Clear decision bullets on what to approve now.
- Re-state the sequencing rule: bounded, well-defined first; big-system overhaul later.

## Website Rendering Requirements

- The website version must preserve all Markdown content (no dropped sections, no omitted bullets).
- Use a consistent card-and-grid information architecture:
  - Section 2 as process cards (including the Phase 3 product-development card).
  - Cost and revenue sections as multi-card grids.
  - Net financial + rollout + risk controls as compact grid blocks in one integrated section.
- Keep typography and spacing consistent across all sections (single type scale and spacing scale).
- Keep print behavior visually consistent with the web layout (avoid radically different print-only rearrangements).
- Ensure the design remains readable and professional on desktop and mobile.

## Style Rules

- Keep it to one page.
- Use plain business language.
- Define any unavoidable term immediately in plain language.
- Be explicit about who buys from SRAM when relevant (bike manufacturers, dealers/shops, riders).
- Prefer practical tool stacks that can be integrated into existing workflows.
- SRAM runs on AWS. All AI tool recommendations must use AWS-native services (Amazon Bedrock, Amazon Kendra, AWS SageMaker). Do not recommend Azure, GCP, or OpenAI directly.
- Use descriptive language instead of shorthand phrases. For example:
  - Say "support assistant savings" instead of "support copilot savings".
  - Say "keep more existing customers buying SRAM" instead of "retention uplift".
  - Say "larger multi-brand package sales" instead of "cross-brand attach uplift".
  - Say "win more bicycle manufacturer opportunities through faster proposals" instead of "OEM proposal cycle win lift".
- Do not use unexplained abbreviations such as `L/B/H`, `AHT`, `MAPE`, or `fill-rate`.

## Context to Use

SRAM LLC is a private company in performance cycling components and connected cycling technology (drivetrains/brakes, RockShox suspension, Zipp wheels/cockpit, Quarq power meters, Hammerhead cycling computers, TIME pedals).

Known process areas to consider:
- bicycle manufacturer sales planning and proposal workflows
- demand forecasting and inventory/channel planning
- dealer and rider support (warranty, troubleshooting, documentation)
- firmware/app support for AXS/Hammerhead
- compatibility and content management
- multi-brand selling across SRAM/RockShox/Zipp/Quarq/Hammerhead/TIME
