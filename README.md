# SRAM AI Adoption Playbook

Group project for AIML/MORS 950 "Human and Machine Intelligence" — Northwestern Kellogg, Winter 2026.

**Goal:** Produce a C-suite-ready AI Adoption Playbook for SRAM LLC (6–8 pages).

**Team lead:** Donovan Palmer

---

## Getting Started (No Technical Experience Required)

You will use Claude Code to contribute to this project. Claude Code is an AI assistant that works directly inside this repository. It reads the project files, understands the context, and helps you write, edit, and organize content.

### Step 1 — Install Claude Code

Open your terminal (on Mac, press Cmd + Space and type "Terminal") and run:

```
npm install -g @anthropic-ai/claude-code
```

If you do not have Node.js installed, download it first from https://nodejs.org and then run the command above.

### Step 2 — Clone This Repository

In your terminal, run:

```
git clone https://github.com/donovan-palmer/sram-ai-playbook.git
cd sram-ai-playbook
```

This downloads the project to your computer.

### Step 3 — Open Claude Code

From inside the project folder, run:

```
claude
```

Claude Code will start up, read all the project files automatically, and be ready to help. You do not need to explain the project to it. It already knows the context.

### Step 4 — Ask Claude to Help You

Just type what you want to do. For example:

- "Summarize what we have so far on the AI adoption strategy"
- "Add a section on demand forecasting to the AI adoption outline"
- "What are SRAM's biggest competitors and how do they compare?"
- "Review the revenue analysis and tell me what is missing"

Claude will make changes, explain what it did, and ask before doing anything significant.

---

## What Is In This Repository

| File or Folder | What It Contains |
|---|---|
| `analysis.md` | Full competitive intelligence on SRAM — company overview, revenue, competitors, leadership |
| `ai adoption/ai-adoption-outline.md` | AI adoption strategy with prioritized use cases and tool recommendations |
| `revenue/revenue_streams_sram.md` | Breakdown of SRAM's revenue streams |
| `competitors/competitors_sram.md` | Competitor analysis |
| `prompts/ai-adoption.prompt.md` | The prompt used to generate the AI adoption content (for reference) |
| `analysis-hub.html` | A single HTML file that displays all the analysis in one place — open it in your browser |
| `tools/build_analysis_hub.py` | Script that rebuilds `analysis-hub.html` after you make edits |
| `syllabus.md` | Course syllabus for reference |

---

## How to View the Full Analysis

Open `analysis-hub.html` in your browser. It pulls everything together in one readable view. If you make edits to any markdown file, ask Claude to rebuild it:

> "Rebuild the analysis hub"

---

## How Claims Are Labeled

Every factual claim in the analysis files carries one of three labels:

- `Confirmed` — backed by a direct source
- `Inference` — reasoned from confirmed facts
- `Speculative` — plausible but not verified

Every claim also has a bracketed source (like `[S1]`). The full source list is at the bottom of `analysis.md`. Do not add claims without a label and a source.

---

## How to Contribute

Claude Code handles the technical parts. You focus on the content.

1. Tell Claude what you want to add or change
2. Review what Claude proposes before it makes changes
3. Claude will create a branch, commit the change, and open a pull request
4. Donovan reviews and merges

If you get stuck, just ask Claude: "What should I work on next?" or "Walk me through how to contribute."

---

## Questions

Reach out to Donovan Palmer directly.
