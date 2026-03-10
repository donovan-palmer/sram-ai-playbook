# SRAM Interview Write-Up

Donovan Palmer, Ed [Last Name], Will [Last Name] | AIML/MORS 950 | Week 4 | 4 Mar 2026

Interviewee: Jordan Hartsell, VP of Digital Products and Innovation, SRAM LLC
Format: 45-minute Zoom call
Interviewer team: Donovan Palmer, Ed [Last Name], Will [Last Name]

---

## Background

Jordan Hartsell oversees SRAM's digital product organization, including the AXS wireless ecosystem, the Hammerhead cycling computer platform, and internal tooling that connects support, dealer operations, and manufacturing workflows. Hartsell joined SRAM from a tier-1 automotive supplier where he led a similar connected-product digitization effort. He has been at SRAM for four years.

We reached out to Hartsell through a LinkedIn introduction from a mutual contact at Northwestern. He agreed to a 45-minute conversation focused on how SRAM thinks about technology adoption and where AI fits into that picture.

---

## Key Questions and Responses

**Donovan: What does SRAM's data infrastructure look like today, and how ready is it for AI-driven workflows?**

Hartsell was direct. "We have good data in pockets and messy data everywhere else." The AXS and Hammerhead platforms generate structured, real-time usage data — firmware update logs, connectivity events, ride metrics, diagnostic flags. That data is clean and increasingly well-organized. The problem is everything adjacent to it. Dealer support tickets live in one system. Warranty claims live in another. Compatibility documentation is maintained manually across product lines and updated on a release cadence that does not always keep pace with the actual hardware. "If I wanted to build a support AI today, I could get it to work well for AXS and Hammerhead," he said. "The moment a dealer asks about a RockShox fork on a 2019 frame with a third-party brake, I start to sweat."

He said SRAM has been investing in data consolidation for 18 months, with the explicit goal of making it AI-ready. The priority has been support and compatibility data first, demand forecasting second. He estimated they are 60 to 70 percent of the way to a state where a bounded support assistant could be deployed responsibly.

**Ed: Where do you see the most internal resistance to AI adoption, and how do you navigate it?**

Hartsell said the resistance is not where most people expect it. "It is not the engineers. Engineers love this stuff. The resistance comes from customer-facing teams — support leads, dealer account managers — because they worry AI will produce confident-sounding wrong answers that damage dealer relationships they have spent years building." He described a pilot where an AI tool gave a compatibility recommendation that was technically correct per the documentation but wrong for a specific frame geometry that an experienced support agent would have flagged. The recommendation did not cause a product failure, but it eroded trust in the pilot internally. "That one incident cost me three months of buy-in."

His approach has been to frame AI as a drafting tool, not a decision-maker. Every AI output goes through a human before it reaches a dealer or a rider. "The first question I ask anyone skeptical about AI is: do you want to spend your day searching a 200-page compatibility PDF, or do you want to spend it talking to dealers? The AI does the search. You make the call." He said that framing has been more effective than ROI decks.

**Will: How does SRAM think about AI relative to competitors like Shimano and SRAM's own acquired brands?**

Hartsell was careful here but candid. He said Shimano's scale gives them a different AI posture — more data, more dedicated investment, and a longer runway to absorb mistakes. "Shimano has the luxury of getting it wrong a few times. We do not." He sees SRAM's advantage in its connected product stack. Hammerhead and AXS together give SRAM a richer real-time data relationship with riders than Shimano has with most of its customers. "A Shimano rider uses the app to check compatibility. A Hammerhead rider uses it to train, navigate, and communicate with their component stack. That is a fundamentally different data relationship." He believes that if SRAM moves quickly on support and recommendations AI in the next 12 to 18 months, it closes the scale gap with Shimano in the domains that matter most for rider and dealer loyalty.

On acquired brands: he said integrating Quarq and Hammerhead data has been the biggest unlock so far. Ochain is too recent to have useful data yet. TIME pedals remain largely analog in terms of data capture. He did not mention near-term AI plans for those brands.

**Donovan: What would a successful AI deployment look like in year one, and what would make you pull the plug?**

Success in year one, per Hartsell, is narrow and boring. "I want one workflow measurably faster, measurably more accurate, with no regression in dealer satisfaction scores." He specifically named the AXS drivetrain support queue as the target. His internal definition of success is a 30 percent reduction in average handle time on AXS support tickets with dealer satisfaction scores holding flat or improving.

The pull-the-plug criteria he cited: two consecutive weeks of quality degradation, any warranty or safety-adjacent error that reaches a dealer without human review, or dealer opt-out rate above 15 percent in the pilot cohort. "I would rather shut it down and restart than defend a mistake to Ken [Lousberg]."

---

## Synthesis and Implications

Three things from this conversation directly shaped our diagnosis.

First, SRAM's data readiness is real but bounded. The AXS and Hammerhead stack is AI-ready now. The broader catalog is not. Any year-one AI recommendation must start inside that ready perimeter and expand only after the data consolidation work matures. This validates our recommendation to pilot on AXS and Hammerhead support first.

Second, the adoption barrier is not technical — it is trust. The failed pilot Hartsell described created more internal skepticism than any cost or complexity argument would have. The implication for our playbook is that the rollout design matters as much as the tool selection. Human-in-the-loop is not a concession to skeptics; it is the thing that keeps the pilot alive long enough to prove value.

Third, Hammerhead is SRAM's real AI moat. The connected rider data relationship that Hammerhead enables is a structural advantage over Shimano that SRAM is not fully exploiting yet. Our playbook should call this out explicitly as the long-term differentiation lever, not just a near-term support tool.

---

## Open Questions for the Playbook

- What is the current state of SRAM's dealer satisfaction tracking, and is it consistent enough to serve as a reliable AI pilot baseline?
- How does SRAM plan to handle compatibility AI for legacy products where documentation is incomplete or inconsistent?
- Is there an executive sponsor above Hartsell who has formally committed to the AI data consolidation roadmap, or is this still a digital-team initiative without C-suite ownership?
