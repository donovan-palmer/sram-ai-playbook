"""
build_pilot_gantt_charts.py
Generates two polished Gantt chart PNGs for embedding in Word documents.
  1. Customer and Dealer Warranty Support Pilot (Step 3A)
  2. Demand Forecasting and Supply Chain Optimization Pilot (Step 3B)

Run: python tools/build_pilot_gantt_charts.py
Output: deliverables/Gantt_Warranty_Support_Pilot.png
        deliverables/Gantt_Demand_Forecasting_Pilot.png
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR    = os.path.join(SCRIPT_DIR, "..", "deliverables")
os.makedirs(OUT_DIR, exist_ok=True)

# ── Design tokens ─────────────────────────────────────────────────────────────
SRAM_RED      = "#C8102E"   # SRAM brand red — phase headers
PILOT_ORANGE  = "#E8611A"   # Warm orange — active task bars (3A)
PILOT_PURPLE  = "#5C2D91"   # Deep purple — active task bars (3B)
SCALE_BLUE    = "#0065A4"   # Blue — scale/full deployment bars
ONGOING_ALPHA = 0.22
HEADER_BG     = "#1A1A2E"   # Near-black navy — section headers
HEADER_FG     = "white"
MILESTONE_CLR = "#1A1A2E"
GRID_CLR      = "#E8EAF0"
ROW_BG_ALT    = "#F7F8FC"   # subtle alternate row shading
BAR_H         = 0.52
HDR_H         = 0.68
ROW_PAD       = 0.28
FONT_TASK     = 8.5
FONT_HDR      = 9.0
FONT_AXIS     = 8.5


def make_gantt(title, subtitle, rows, x_min, x_max, x_ticks, x_labels,
               figsize, left_margin, output_path):
    """
    rows: list of dicts — type ∈ {'header','task','milestone'}
      header : name
      task   : name, start, end, color, ongoing_end (opt), milestone_at (opt)
      milestone: name, x, color, label
    """
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor("white")
    plt.subplots_adjust(left=left_margin, right=0.97, top=0.88, bottom=0.10)

    ax.set_facecolor("white")
    for sp in ax.spines.values():
        sp.set_visible(False)

    # ── assign y positions ───────────────────────────────────────────────────
    y_pos = []
    y = 0.0
    for r in rows:
        y_pos.append(y)
        y -= (HDR_H + ROW_PAD) if r["type"] == "header" else (BAR_H + ROW_PAD)

    y_bottom = y + ROW_PAD
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_bottom, HDR_H * 1.05)

    # ── alternating row shading ──────────────────────────────────────────────
    task_rows = [(yp, r) for yp, r in zip(y_pos, rows) if r["type"] == "task"]
    for i, (yp, _) in enumerate(task_rows):
        if i % 2 == 0:
            ax.axhspan(yp - BAR_H * 0.62, yp + BAR_H * 0.62,
                       color=ROW_BG_ALT, zorder=0, linewidth=0)

    # ── vertical grid lines ──────────────────────────────────────────────────
    for gx in x_ticks:
        ax.axvline(gx, color=GRID_CLR, linewidth=0.9, zorder=1)

    # ── draw rows ────────────────────────────────────────────────────────────
    yticks, ylabels = [], []

    for r, yp in zip(rows, y_pos):
        if r["type"] == "header":
            # Full-width header band
            rect = FancyBboxPatch(
                (x_min, yp - HDR_H * 0.08), x_max - x_min, HDR_H * 0.88,
                boxstyle="round,pad=0.02",
                facecolor=HEADER_BG, edgecolor="none", zorder=3
            )
            ax.add_patch(rect)
            ax.text(x_min + (x_max - x_min) * 0.008, yp + HDR_H * 0.30,
                    r["name"], color=HEADER_FG,
                    fontsize=FONT_HDR, fontweight="bold",
                    va="center", ha="left", zorder=4)

        elif r["type"] == "task":
            # Active bar
            w = r["end"] - r["start"]
            bar = ax.barh(yp, w, left=r["start"], height=BAR_H,
                          color=r["color"], edgecolor="white", linewidth=0.5,
                          align="center", zorder=3)

            # Rounded cap effect — thin white border
            ax.barh(yp, w, left=r["start"], height=BAR_H,
                    color="none", edgecolor=r["color"],
                    linewidth=1.0, align="center", zorder=4)

            # Ongoing / scale-out extension
            if r.get("ongoing_end"):
                ow = r["ongoing_end"] - r["end"]
                ax.barh(yp, ow, left=r["end"], height=BAR_H,
                        color=r["color"], alpha=ONGOING_ALPHA,
                        edgecolor="white", linewidth=0.5,
                        align="center", zorder=3, hatch="////")

            # Inline milestone diamond
            if r.get("milestone_at") is not None:
                ax.plot(r["milestone_at"], yp, marker="D", markersize=7,
                        color="white", markeredgecolor=MILESTONE_CLR,
                        markeredgewidth=1.2, zorder=5)

            yticks.append(yp)
            ylabels.append(r["name"])

        elif r["type"] == "milestone":
            ax.plot(r["x"], yp, marker="D", markersize=10,
                    color=r["color"], markeredgecolor="white",
                    markeredgewidth=0.9, zorder=5)
            ax.text(r["x"] + (x_max - x_min) * 0.008, yp,
                    r.get("label", ""),
                    fontsize=7.5, va="center", color=r["color"],
                    fontweight="bold")
            yticks.append(yp)
            ylabels.append(r["name"])

    # ── y-axis labels ────────────────────────────────────────────────────────
    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels, fontsize=FONT_TASK)
    ax.tick_params(axis="y", left=False, pad=5)

    # ── x-axis ───────────────────────────────────────────────────────────────
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, fontsize=FONT_AXIS)
    ax.tick_params(axis="x", bottom=False, pad=4)
    ax.xaxis.set_ticks_position("bottom")

    # ── month reference line (today = Month 0 start) ─────────────────────────
    # light dashed line at x_min to anchor the reader
    ax.axvline(x_min, color=SRAM_RED, linewidth=1.2,
               linestyle="--", alpha=0.5, zorder=2)

    # ── titles ───────────────────────────────────────────────────────────────
    fig.text(0.01, 0.97, title,
             fontsize=13, fontweight="bold", color="#1A1A2E",
             va="top", ha="left")
    fig.text(0.01, 0.925, subtitle,
             fontsize=8.5, color="#5A6070",
             va="top", ha="left")

    # ── legend ───────────────────────────────────────────────────────────────
    legend_handles = r.get("_legend", [])   # injected below
    if legend_handles:
        ax.legend(handles=legend_handles,
                  loc="lower right", fontsize=8,
                  framealpha=0.92, ncol=len(legend_handles),
                  edgecolor="#CCCCCC")

    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    print(f"Saved → {output_path}")
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
#  CHART 1 — Customer and Dealer Warranty Support Pilot  (Month 1–24)
# ══════════════════════════════════════════════════════════════════════════════

warranty_rows = [

    # ── Phase 1: Setup & Integration ─────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 1  ·  SETUP & INTEGRATION  (Month 1–3)"},

    {"type": "task",
     "name": "Pilot Design + Baseline Metrics",
     "start": 1, "end": 3,
     "color": PILOT_ORANGE},

    {"type": "task",
     "name": "Amazon Kendra + Bedrock Integration (AWS)",
     "start": 1, "end": 6,
     "color": PILOT_ORANGE},

    # ── Phase 2: AXS Pilot Launch ─────────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 2  ·  AXS DRIVETRAIN PILOT  (Month 4–6)"},

    {"type": "task",
     "name": "AXS Drivetrain Ticket Rollout  [100% human review]",
     "start": 4, "end": 9,
     "color": PILOT_ORANGE},

    {"type": "milestone",
     "name": "  Day-45 Draft Acceptance Checkpoint  (G3 ≥50% gate)",
     "x": 4.5,
     "color": SRAM_RED,
     "label": "◆  Day-45 Gate"},

    # ── Phase 3: Hammerhead & Warranty Track ──────────────────────────────────
    {"type": "header",
     "name": "PHASE 3  ·  HAMMERHEAD EXPANSION + WARRANTY TRACK  (Month 7–12)"},

    {"type": "task",
     "name": "Hammerhead Device Ticket Expansion",
     "start": 7, "end": 12,
     "color": PILOT_ORANGE},

    {"type": "task",
     "name": "Warranty Claim AI Review Track  [human final decision]",
     "start": 7, "end": 12,
     "color": PILOT_ORANGE},

    {"type": "milestone",
     "name": "  Day-90 Go / No-Go Decision",
     "x": 9,
     "color": SRAM_RED,
     "label": "◆  Go / No-Go"},

    # ── Phase 4: Scale ────────────────────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 4  ·  SCALE TO FULL CATALOG  (Month 13–24)"},

    {"type": "task",
     "name": "Full Product Catalog Rollout",
     "start": 13, "end": 24,
     "color": SCALE_BLUE},

    {"type": "task",
     "name": "Semi-Autonomous Response Tier  [low-risk ticket categories]",
     "start": 16, "end": 24,
     "color": SCALE_BLUE},
]

# x-axis: every month, labeled by month number
w_ticks  = list(range(1, 25))
w_labels = [f"M{m}" for m in w_ticks]

# Add legend to last row (hacky but clean)
warranty_legend = [
    mpatches.Patch(color=PILOT_ORANGE, label="Active Pilot Work"),
    mpatches.Patch(color=SCALE_BLUE,   label="Scale / Deployment"),
    mpatches.Patch(color=SRAM_RED,     label="Decision Gate  ◆"),
    mpatches.Patch(facecolor="white", edgecolor="#aaa",
                   hatch="////", label="Ongoing / Maintenance"),
]
warranty_rows[-1]["_legend"] = warranty_legend

make_gantt(
    title    = "Customer and Dealer Warranty Support Pilot",
    subtitle = "Step 3A  ·  Month 1–24  ·  ◆ = Decision Gate or Milestone  ·  Human approval required on all AI-drafted responses during pilot",
    rows     = warranty_rows,
    x_min=1, x_max=24,
    x_ticks=w_ticks, x_labels=w_labels,
    figsize=(18, 8),
    left_margin=0.26,
    output_path=os.path.join(OUT_DIR, "Gantt_Warranty_Support_Pilot.png"),
)


# ══════════════════════════════════════════════════════════════════════════════
#  CHART 2 — Demand Forecasting and Supply Chain Optimization Pilot (M22–36+)
# ══════════════════════════════════════════════════════════════════════════════

forecast_rows = [

    # ── Phase 0: Data Gate ────────────────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 0  ·  DATA READINESS  (Month 22–24)"},

    {"type": "task",
     "name": "Data Readiness Audit  [≥85% completeness required]",
     "start": 22, "end": 24,
     "color": PILOT_PURPLE},

    {"type": "milestone",
     "name": "  Data Quality Gate  —  hard go / no-go",
     "x": 24,
     "color": SRAM_RED,
     "label": "◆  Data Gate"},

    # ── Phase 1: Model Build ──────────────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 1  ·  MODEL DEVELOPMENT & BACK-TEST  (Month 25–30)"},

    {"type": "task",
     "name": "SageMaker Model Development  [top-50 SKUs by revenue]",
     "start": 25, "end": 30,
     "color": PILOT_PURPLE},

    {"type": "milestone",
     "name": "  Back-Test Validation Gate  (MAPE ≤15% required)",
     "x": 27,
     "color": SRAM_RED,
     "label": "◆  MAPE Gate"},

    # ── Phase 2: Shadow Mode ──────────────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 2  ·  SHADOW MODE PILOT  (Month 28–33)"},

    {"type": "task",
     "name": "Shadow Mode  —  Model Runs Parallel, Planners Observe",
     "start": 28, "end": 33,
     "color": PILOT_PURPLE},

    {"type": "milestone",
     "name": "  Shadow Checkpoint  (MAPE ≤20% live; adoption signal)",
     "x": 30,
     "color": SRAM_RED,
     "label": "◆  Shadow Chk"},

    # ── Phase 3: Active Pilot ─────────────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 3  ·  ACTIVE PILOT — PLANNERS ACT ON MODEL OUTPUT  (Month 31–36)"},

    {"type": "task",
     "name": "Active Pilot  —  Planners Act on Recommendations  [override logged]",
     "start": 31, "end": 36,
     "color": PILOT_PURPLE},

    {"type": "milestone",
     "name": "  Full Pilot Evaluation + Scale Decision",
     "x": 36,
     "color": SRAM_RED,
     "label": "◆  Scale Decision"},

    # ── Phase 4: Full Scale ───────────────────────────────────────────────────
    {"type": "header",
     "name": "PHASE 4  ·  FULL SCALE — ALL SKUs + BRANDS  (Month 37+)"},

    {"type": "task",
     "name": "Full SKU Catalog + Multi-Brand Deployment",
     "start": 37, "end": 42,
     "ongoing_end": 48,
     "color": SCALE_BLUE},

    {"type": "task",
     "name": "Quarterly Model Retraining Cadence",
     "start": 37, "end": 48,
     "color": SCALE_BLUE},
]

f_ticks  = list(range(22, 49))
f_labels = [f"M{m}" for m in f_ticks]

forecast_legend = [
    mpatches.Patch(color=PILOT_PURPLE, label="Active Pilot Work"),
    mpatches.Patch(color=SCALE_BLUE,   label="Scale / Deployment"),
    mpatches.Patch(color=SRAM_RED,     label="Decision Gate  ◆"),
    mpatches.Patch(facecolor="white", edgecolor="#aaa",
                   hatch="////", label="Ongoing / Maintenance"),
]
forecast_rows[-1]["_legend"] = forecast_legend

make_gantt(
    title    = "Demand Forecasting and Supply Chain Optimization Pilot",
    subtitle = "Step 3B  ·  Month 22–48  ·  ◆ = Decision Gate or Milestone  ·  Requires Step 2 Data Lakehouse (≥85% data quality) before launch",
    rows     = forecast_rows,
    x_min=22, x_max=48,
    x_ticks=f_ticks, x_labels=f_labels,
    figsize=(18, 8.5),
    left_margin=0.26,
    output_path=os.path.join(OUT_DIR, "Gantt_Demand_Forecasting_Pilot.png"),
)

print("\nDone. Both pilot Gantt charts saved to deliverables/")
