# Session Prompts — Unified AI Adoption Playbook
## AIML/MORS 950, Northwestern Kellogg, Winter 2026

This file documents the exact prompts used in the Claude Code session that produced
`ai adoption/unified-ai-playbook-2031.md` and the supporting reference materials.
It is preserved here so the reasoning process is transparent and reproducible.

---

## Session Overview

**Date:** 2026-03-06
**Tool:** Claude Code (claude-sonnet-4-6)
**Working directory:** C:\claude_output\AIML950SRAM
**Repository:** https://github.com/donovan-palmer/sram-ai-playbook

The session began with cloning the repository, reading all key files,
and then performing a structured analysis and synthesis exercise that
produced the unified playbook.

---

## Prompts Used (In Order)

### Prompt 1 — Clone the repository

> Please clone this public repository https://github.com/donovan-palmer/sram-ai-playbook.git
> to my current working directory for this class. You should follow the CLAUDE.md file
> exclusively as it defines some of the key git processes for you to follow so that you
> can contribute to the project.

**What this produced:** Claude cloned the repository, read CLAUDE.md, and summarized
the project structure and contribution rules (feature branches, PRs, no Co-Authored-By
lines, confidence labeling convention, analysis-hub rebuild process).

---

### Prompt 2 — Read the key files

> Can you please read back to me the key files within the repository as a starting point?

**What this produced:** Claude read and summarized all four primary documents in parallel:
- `analysis.md` — competitive intelligence
- `revenue/revenue_streams_sram.md` — revenue architecture
- `competitors/competitors_sram.md` — competitor map
- `ai adoption/ai-adoption-outline.md` — original AI adoption pilot proposal

---

### Prompt 3 — Explain the collaboration workflow

> Assume I have no prior coding or GitHub experience and do not understand that lingo.
> Please walk me through how I can work with Claude to collaborate with the owner of
> the repository I just had you access.

**What this produced:** A plain-English guide explaining repositories, branches, commits,
and pull requests using Google Docs and track-changes analogies. Defined the user's role
(describe what to add/change; provide sources) versus Claude's role (all technical steps).

---

### Prompt 4 — Compare the two strategy documents

> Can you perform a detailed comparison of the sram_ai_strategy.md file to the
> ai-adoption-outline.md file from the cloned repository. Please include a complete
> breakdown of what is unique to each AI strategy, what is shared, how the financial
> forecasts compare, and how the action plans and measurement criteria compare.

**What this produced:** A six-section structured comparison covering:
1. What the documents share
2. What is unique to `ai-adoption-outline.md` (the repo file)
3. What is unique to `sram_ai_strategy.md` (the reference file)
4. Financial forecast comparison (side-by-side table)
5. Action plan comparison (phase timing, scope, accountability)
6. Measurement criteria comparison (success metrics, rollback rules, guardrails)

Key finding: the two documents are complementary — the outline is a bounded 90-day
pilot proposal; the strategy document is a 3-year transformation case with manufacturing,
engineering, and platform depth. Neither alone is complete.

---

### Prompt 5 — Propose the merged strategy

> How would you propose merging these two proposals into an actionable near-term pilot
> program that ultimately informs a long-term AI adoption strategy that would be fully
> implemented with run-rate financial impacts realized by 2031? Please focus on refining
> key areas of alignment between the two proposals, finding parallel processes to more
> efficiently implement and accomplish proposed outcomes, and maximize financial returns
> of the overall adoption program. Please provide a detailed summary of the ultimate
> proposal for the AI adoption playbook.

**What this produced:** A full synthesis proposal organized around four design principles:
1. Start bounded, build infrastructure
2. Run parallel tracks where dependencies allow
3. Let the AXS platform be the financial engine
4. Apply human approval and rollback rules across all phases

The proposal included:
- 5-year financial model ($238M cumulative net, $105-120M 2031 steady-state annual value)
- Five parallel Phase 1 tracks with no interdependencies
- Phase 2 manufacturing and R&D AI additions
- Phase 3 AXS subscription and B2B data intelligence launch
- Phase 4-5 compounding layer through 2031
- Parallel process architecture identifying shared infrastructure vs. sequential dependencies
- Risk register with 8 identified risks, probabilities, impacts, and mitigations
- Five specific CEO approvals required to begin

---

### Prompt 6 — Formalize as a repository contribution

> Yes please draft this as a formal document to contribute to the repository — following
> the CLAUDE.md rules, on a new feature branch, with a PR for Donovan to review. Can you
> also make a separate contribution to the repository that shows the prompts I used to
> generate this output and also the sram_ai_strategy.md itself for reference?

**What this produced:** This current set of files:
- `ai adoption/unified-ai-playbook-2031.md` — the formal merged playbook
- `prompts/unified-playbook-session.prompt.md` — this file
- `reference/sram_ai_strategy.md` — the supplementary strategy document for reference

Two feature branches and two PRs to `donovan-palmer/sram-ai-playbook`:
- `feature/unified-ai-adoption-playbook`
- `feature/session-reference-materials`

---

## Notes on the Analytical Process

The merged playbook is not a simple combination of the two source documents.
The key synthesis decisions were:

1. **Data infrastructure moved to Phase 1.** Both source documents treated the Snowflake
   unified data lake as a future-phase concern. The merged plan moves it to Phase 1 because
   it is the prerequisite for every high-value Phase 2 and Phase 3 initiative. Deferring it
   was identified as the single most expensive sequencing mistake available.

2. **Engineering AI tools moved to Week 1.** The outline did not include this at all.
   The strategy document included it but did not emphasize the parallel-track logic.
   The merged plan makes it Week 1, Track A, because it has zero dependencies and
   generates $8M in labor equivalent value that effectively funds the rest of the program.

3. **Demand forecasting moved from Phase 2 to Phase 1.** The outline sequenced it after
   support. The merged plan runs it in parallel from Month 1 because there is no dependency
   between the two tracks, and running them in parallel captures $7M+ in Year 1 savings
   that the original outline deferred.

4. **Governance applied universally.** The outline had strong rollback rules and human
   approval requirements but scoped them only to customer service. The merged plan applies
   the same governance framework across all phases and all use cases.
