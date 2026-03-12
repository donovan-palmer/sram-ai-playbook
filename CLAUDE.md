# CLAUDE.md

This file provides guidance to AI agents working in this repository.

## What This Repository Is

Group project workspace for AIML/MORS 950 "Human and Machine Intelligence" at Northwestern (Kellogg), Winter 2026. The goal is a C-suite-ready AI Adoption Playbook for SRAM LLC (6-8 pages).

## Repository Structure

### Deliverables (what gets turned in)
- `deliverables/SRAM_AI_Adoption_Playbook.md` — final 6-8 page AI adoption playbook
- `deliverables/SRAM_AI_Adoption_Playbook.pptx` — 8-minute presentation deck

### Research (supporting analysis and sources)
- `research/analysis.md` — primary competitive intelligence document
- `research/SRAM_company_analysis.md` — tech stack and org analysis
- `research/revenue/` — revenue stream analysis
- `research/competitors/` — competitor analysis
- `research/interview/` — simulated interview with Clint Weber, VP Global Sales and Manufacturing
- `research/reference/` — supplementary strategy reference
- `research/prompts/` — prompts used for AI-assisted content generation
- `research/analysis-hub.html` — generated HTML viewer (do not edit directly)
- `research/syllabus.md` — course syllabus

### Tools (build scripts)
- `tools/build_presentation.py` — generates the presentation PPTX into `deliverables/`
- `tools/build_analysis_hub.py` — compiles all `.md` files into `research/analysis-hub.html`

## How to Rebuild the Analysis Hub

After editing any markdown file, run:

```
python3 tools/build_analysis_hub.py
```

No dependencies beyond the Python standard library.

## Confidence Labeling Convention

Every claim in analysis documents uses one of three labels:

- `Confirmed` — explicit source evidence
- `Inference` — reasoned synthesis from confirmed facts
- `Speculative` — plausible but not directly verified

Every claim cites a bracketed source (e.g., `[S1]`). The source list lives at the bottom of `analysis.md`.

## Who You Are Working With

Most contributors are non-technical MBA students. They are not engineers. Assume they do not know git, markdown, or how terminals work.

- Explain what you are about to do before you do it, in plain English
- After making changes, summarize what changed and why in one or two sentences
- Ask before doing anything that cannot be undone
- If something fails, explain the problem simply and suggest the next step
- Proactively suggest what to work on next if the user seems unsure

## Agent Ground Rules

- Do not edit `research/analysis-hub.html` directly. Always rebuild via the Python script.
- Do not remove confidence labels or source citations from any claim.
- Do not add claims without a label and a source citation.
- Keep all changes in feature branches named `feature/{feature-name}`.
- Open a PR before merging into main.
- Small, incremental commits. One logical change per commit.
- All commits attributed to the committing team member only. No Co-Authored-By lines.
- After a PR is merged, delete the remote feature branch to keep the repo clean.
