#!/usr/bin/env python3
"""
Build the SRAM AI Adoption Playbook presentation.

8-minute deck using Duarte's "What Is / What Could Be" contrast pattern
with a T-shaped structure (wide overview -> deep dive on support).

Usage:
    python3 tools/build_presentation.py

Output:
    presentation/SRAM_AI_Adoption_Playbook.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

# --- Color palette (dark executive theme) ---
BG_DARK = RGBColor(0x0F, 0x17, 0x2A)       # Deep navy background
BG_CARD = RGBColor(0x16, 0x21, 0x3A)       # Card/section background
ACCENT_BLUE = RGBColor(0x38, 0x9F, 0xF5)   # Primary accent
ACCENT_GREEN = RGBColor(0x34, 0xD3, 0x99)  # Success/positive
ACCENT_AMBER = RGBColor(0xFB, 0xBF, 0x24)  # Warning/attention
ACCENT_RED = RGBColor(0xEF, 0x44, 0x44)    # Alert/negative
TEXT_WHITE = RGBColor(0xF8, 0xFA, 0xFC)     # Primary text
TEXT_LIGHT = RGBColor(0x94, 0xA3, 0xB8)     # Secondary text
TEXT_DIM = RGBColor(0x64, 0x74, 0x8B)       # Tertiary text
DIVIDER = RGBColor(0x1E, 0x29, 0x3B)        # Subtle divider lines

SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)


def set_slide_bg(slide, color):
    """Set solid background color for a slide."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_shape(slide, left, top, width, height, fill_color, border_color=None, corner_radius=None):
    """Add a rounded rectangle shape."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    if corner_radius is not None:
        shape.adjustments[0] = corner_radius
    return shape


def add_text_box(slide, left, top, width, height, text, font_size=14,
                 color=TEXT_WHITE, bold=False, alignment=PP_ALIGN.LEFT,
                 font_name="Calibri"):
    """Add a text box with formatted text."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def add_multiline_text(slide, left, top, width, height, lines, font_size=14,
                       color=TEXT_WHITE, line_spacing=1.3, font_name="Calibri"):
    """Add a text box with multiple styled lines.

    lines: list of tuples (text, font_size, color, bold)
    """
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, line_data in enumerate(lines):
        if len(line_data) == 4:
            text, fs, col, bld = line_data
        elif len(line_data) == 3:
            text, fs, col = line_data
            bld = False
        else:
            text, fs = line_data
            col = color
            bld = False

        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = text
        p.font.size = Pt(fs)
        p.font.color.rgb = col
        p.font.bold = bld
        p.font.name = font_name
        p.space_after = Pt(fs * (line_spacing - 1) * 2)
    return txBox


def add_metric_card(slide, left, top, width, height, label, value,
                    value_color=ACCENT_BLUE, sub_text=None):
    """Add a metric card with large number and label."""
    card = add_shape(slide, left, top, width, height, BG_CARD, DIVIDER, 0.05)

    add_text_box(slide, left + Inches(0.3), top + Inches(0.25),
                 width - Inches(0.6), Inches(0.4),
                 label, font_size=11, color=TEXT_DIM)

    add_text_box(slide, left + Inches(0.3), top + Inches(0.55),
                 width - Inches(0.6), Inches(0.6),
                 value, font_size=28, color=value_color, bold=True)

    if sub_text:
        add_text_box(slide, left + Inches(0.3), top + Inches(1.15),
                     width - Inches(0.6), Inches(0.3),
                     sub_text, font_size=10, color=TEXT_LIGHT)


def add_bullet_card(slide, left, top, width, height, title, bullets,
                    title_color=ACCENT_BLUE, bullet_color=TEXT_LIGHT):
    """Add a card with title and bullet points."""
    card = add_shape(slide, left, top, width, height, BG_CARD, DIVIDER, 0.05)

    add_text_box(slide, left + Inches(0.3), top + Inches(0.2),
                 width - Inches(0.6), Inches(0.4),
                 title, font_size=16, color=title_color, bold=True)

    lines = [(f"\u2022  {b}", 12, bullet_color) for b in bullets]
    add_multiline_text(slide, left + Inches(0.3), top + Inches(0.65),
                       width - Inches(0.6), height - Inches(0.85),
                       lines, line_spacing=1.5)


def add_accent_line(slide, left, top, width, color=ACCENT_BLUE):
    """Add a thin horizontal accent line."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, Pt(3)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


# ============================================================
# BUILD THE PRESENTATION
# ============================================================

prs = Presentation()
prs.slide_width = SLIDE_WIDTH
prs.slide_height = SLIDE_HEIGHT

# Use blank layout
blank_layout = prs.slide_layouts[6]


# ----------------------------------------------------------
# SLIDE 1: Title
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_accent_line(slide, Inches(1.5), Inches(2.5), Inches(2), ACCENT_BLUE)

add_multiline_text(slide, Inches(1.5), Inches(2.7), Inches(10), Inches(3), [
    ("SRAM LLC", 42, TEXT_WHITE, True),
    ("AI Adoption Playbook", 28, ACCENT_BLUE, False),
    ("", 14, TEXT_DIM, False),
    ("Prepared for Executive Leadership", 14, TEXT_LIGHT, False),
    ("March 2026", 14, TEXT_DIM, False),
])

add_text_box(slide, Inches(1.5), Inches(6.2), Inches(10), Inches(0.5),
             "AIML 950  |  Human and Machine Intelligence  |  Northwestern Kellogg",
             font_size=11, color=TEXT_DIM)


# ----------------------------------------------------------
# SLIDE 2: "What Is" - SRAM Today
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_text_box(slide, Inches(0.8), Inches(0.4), Inches(6), Inches(0.5),
             "WHAT IS", font_size=12, color=ACCENT_BLUE, bold=True)
add_text_box(slide, Inches(0.8), Inches(0.7), Inches(10), Inches(0.7),
             "SRAM Today", font_size=32, color=TEXT_WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.3), Inches(1.2), ACCENT_BLUE)

# Left side: company overview
add_text_box(slide, Inches(0.8), Inches(1.6), Inches(5.5), Inches(1.0),
             "Private, Chicago-founded, $1B+ revenue. The second-largest bicycle "
             "component manufacturer globally. Dominant in mountain bike. "
             "Seven brands, three channels, one connected ecosystem.",
             font_size=14, color=TEXT_LIGHT)

# Metric cards row
add_metric_card(slide, Inches(0.8), Inches(2.8), Inches(2.5), Inches(1.5),
                "REVENUE", "$1B+", ACCENT_BLUE, "Private, not disclosed")
add_metric_card(slide, Inches(3.5), Inches(2.8), Inches(2.5), Inches(1.5),
                "EMPLOYEES", "3,000-5,000", ACCENT_BLUE, "Global operations")
add_metric_card(slide, Inches(6.2), Inches(2.8), Inches(2.5), Inches(1.5),
                "BRANDS", "7", ACCENT_BLUE, "Integrated portfolio")
add_metric_card(slide, Inches(8.9), Inches(2.8), Inches(2.5), Inches(1.5),
                "MTB POSITION", "#1", ACCENT_GREEN, "Market leader")

# Revenue streams
add_text_box(slide, Inches(0.8), Inches(4.6), Inches(6), Inches(0.4),
             "Revenue Architecture", font_size=16, color=TEXT_WHITE, bold=True)

streams = [
    ("Drivetrains + Braking", "SRAM RED, Force, Rival, Eagle", "Core engine", ACCENT_BLUE),
    ("Suspension", "RockShox forks and shocks", "High", ACCENT_BLUE),
    ("Wheels + Cockpit", "Zipp performance components", "Medium", ACCENT_BLUE),
    ("Connected Products", "Hammerhead Karoo, Quarq power", "Strategic", ACCENT_GREEN),
    ("Wear Parts + Service", "Chains, cassettes, pads, rotors", "Recurring", ACCENT_GREEN),
    ("Pedals + Adjacent", "TIME, Velocio, Ochain", "Growing", TEXT_DIM),
]

for i, (name, desc, importance, color) in enumerate(streams):
    y = Inches(5.1) + Inches(i * 0.35)
    add_text_box(slide, Inches(0.8), y, Inches(3), Inches(0.35),
                 name, font_size=12, color=color, bold=True)
    add_text_box(slide, Inches(4.0), y, Inches(4), Inches(0.35),
                 desc, font_size=11, color=TEXT_LIGHT)
    add_text_box(slide, Inches(8.2), y, Inches(2), Inches(0.35),
                 importance, font_size=11, color=TEXT_DIM)

# Right side: competitive context
add_bullet_card(slide, Inches(9.5), Inches(4.6), Inches(3.3), Inches(2.5),
                "Competitive Pressure",
                ["Shimano: wireless gravel (GRX RX827)",
                 "Campagnolo: 13-speed premium",
                 "microSHIFT: value mechanical alternative"],
                ACCENT_AMBER)


# ----------------------------------------------------------
# SLIDE 3: "What Could Be" - Where AI Fits (The Wide View)
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_text_box(slide, Inches(0.8), Inches(0.4), Inches(6), Inches(0.5),
             "WHAT COULD BE", font_size=12, color=ACCENT_GREEN, bold=True)
add_text_box(slide, Inches(0.8), Inches(0.7), Inches(10), Inches(0.7),
             "Where AI Fits Across SRAM", font_size=32, color=TEXT_WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.3), Inches(1.2), ACCENT_GREEN)

add_text_box(slide, Inches(0.8), Inches(1.6), Inches(11), Inches(0.6),
             "Four phases ordered by complexity, readiness, and time to return. "
             "Start bounded. Scale after proof.",
             font_size=14, color=TEXT_LIGHT)

# Phase cards
phases = [
    ("PHASE 1", "0-90 Days", "Immediate Wins",
     ["AI coding tools for engineering", "Support + warranty automation",
      "Individual productivity (notes, email)"],
     ACCENT_GREEN, "Low complexity, high visibility"),
    ("PHASE 2", "90-180 Days", "Data Foundation",
     ["Unified data layer (no ERP today)", "Demand forecasting",
      "Customer analytics (Shopify + telemetry)"],
     ACCENT_BLUE, "Requires data infrastructure"),
    ("PHASE 3", "180-365 Days", "Revenue Acceleration",
     ["OEM proposal automation", "Compatible part recommendations",
      "Documentation + translation"],
     ACCENT_BLUE, "Builds on Phase 2 data"),
    ("PHASE 4", "Year 2+", "AI-First Culture",
     ["AXS Intelligence Platform", "Generative design + R&D",
      "AI-tuned component performance"],
     ACCENT_AMBER, "Transformation territory"),
]

for i, (phase, timeline, title, bullets, color, note) in enumerate(phases):
    left = Inches(0.8) + Inches(i * 3.1)
    card_w = Inches(2.85)

    card = add_shape(slide, left, Inches(2.3), card_w, Inches(4.5), BG_CARD, DIVIDER, 0.03)

    # Phase label + timeline
    add_text_box(slide, left + Inches(0.2), Inches(2.45), Inches(1.2), Inches(0.3),
                 phase, font_size=11, color=color, bold=True)
    add_text_box(slide, left + Inches(1.5), Inches(2.45), Inches(1.2), Inches(0.3),
                 timeline, font_size=10, color=TEXT_DIM, alignment=PP_ALIGN.RIGHT)

    # Title
    add_text_box(slide, left + Inches(0.2), Inches(2.8), card_w - Inches(0.4), Inches(0.5),
                 title, font_size=18, color=TEXT_WHITE, bold=True)

    add_accent_line(slide, left + Inches(0.2), Inches(3.3), Inches(0.8), color)

    # Bullets
    lines = [(f"\u2022  {b}", 12, TEXT_LIGHT) for b in bullets]
    add_multiline_text(slide, left + Inches(0.2), Inches(3.5),
                       card_w - Inches(0.4), Inches(2.2),
                       lines, line_spacing=1.6)

    # Bottom note
    add_text_box(slide, left + Inches(0.2), Inches(5.8), card_w - Inches(0.4), Inches(0.5),
                 note, font_size=9, color=TEXT_DIM)

# Arrow / focus indicator
add_text_box(slide, Inches(0.8), Inches(7.0), Inches(12), Inches(0.4),
             "\u25B6  We recommend starting with Phase 1 Support Automation as the deep-dive pilot",
             font_size=13, color=ACCENT_GREEN, bold=True)


# ----------------------------------------------------------
# SLIDE 4: "But What Is" - The Support Problem
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_text_box(slide, Inches(0.8), Inches(0.4), Inches(6), Inches(0.5),
             "BUT WHAT IS", font_size=12, color=ACCENT_RED, bold=True)
add_text_box(slide, Inches(0.8), Inches(0.7), Inches(10), Inches(0.7),
             "The Support Problem is Visible", font_size=32, color=TEXT_WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.3), Inches(1.2), ACCENT_RED)

add_text_box(slide, Inches(0.8), Inches(1.6), Inches(11), Inches(0.6),
             "SRAM's churn risk is driven by support quality, not product quality. "
             "Riders love SRAM components but struggle with firmware, compatibility, and warranty resolution.",
             font_size=14, color=TEXT_LIGHT)

# Pain point cards
add_metric_card(slide, Inches(0.8), Inches(2.5), Inches(3.5), Inches(1.6),
                "TRUSTPILOT RATING", "1.6 / 5.0", ACCENT_RED,
                "Driven by warranty and support friction")

add_metric_card(slide, Inches(4.6), Inches(2.5), Inches(3.5), Inches(1.6),
                "DEALER QUESTIONS AUTOMATABLE", "~70%", ACCENT_GREEN,
                "Follow repeatable patterns")

add_metric_card(slide, Inches(8.4), Inches(2.5), Inches(4.1), Inches(1.6),
                "TOP COMPLAINT THEMES", "Firmware + Pairing", ACCENT_AMBER,
                "Reddit 2024-2025: shifting, updates, compatibility")

# Three-column evidence
add_bullet_card(slide, Inches(0.8), Inches(4.5), Inches(3.5), Inches(2.7),
                "Customer Pain Signals",
                ["Trustpilot: warranty frustration",
                 "Reddit: pairing + firmware failures",
                 "App store: AXS + Hammerhead complaints",
                 "Riders stating intent to switch to Shimano"],
                ACCENT_RED, TEXT_LIGHT)

add_bullet_card(slide, Inches(4.6), Inches(4.5), Inches(3.5), Inches(2.7),
                "Why Support is the Right Pilot",
                ["Pain is visible and measurable",
                 "Data advantage already in place",
                 "High volume of repeatable questions",
                 "No new data collection required"],
                ACCENT_GREEN, TEXT_LIGHT)

add_bullet_card(slide, Inches(8.4), Inches(4.5), Inches(4.1), Inches(2.7),
                "SRAM's Data Advantage",
                ["Structured knowledge base (manuals, guides)",
                 "AXS telemetry (firmware, error codes)",
                 "Hammerhead device data",
                 "Compatibility rules already documented"],
                ACCENT_BLUE, TEXT_LIGHT)


# ----------------------------------------------------------
# SLIDE 5: "What Could Be" - The 90-Day Pilot
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_text_box(slide, Inches(0.8), Inches(0.4), Inches(6), Inches(0.5),
             "WHAT COULD BE", font_size=12, color=ACCENT_GREEN, bold=True)
add_text_box(slide, Inches(0.8), Inches(0.7), Inches(10), Inches(0.7),
             "The 90-Day Support Pilot", font_size=32, color=TEXT_WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.3), Inches(1.2), ACCENT_GREEN)

# Workflow steps
add_text_box(slide, Inches(0.8), Inches(1.6), Inches(6), Inches(0.4),
             "How It Works", font_size=18, color=TEXT_WHITE, bold=True)

steps = [
    ("1", "TICKET ARRIVES", "Dealer or rider submits via Zendesk", "Zendesk AI routes and classifies"),
    ("2", "AI RETRIEVES", "Azure AI Search finds approved docs", "Pulls telemetry context from AXS"),
    ("3", "AI DRAFTS", "OpenAI generates clear response", "Sourced from knowledge base only"),
    ("4", "HUMAN REVIEWS", "Agent approves before sending", "100% human approval in pilot"),
    ("5", "QUALITY LOGGED", "Metrics tracked per interaction", "Weekly review with rollback trigger"),
]

for i, (num, title, line1, line2) in enumerate(steps):
    left = Inches(0.8) + Inches(i * 2.45)
    card_w = Inches(2.25)

    card = add_shape(slide, left, Inches(2.1), card_w, Inches(2.3), BG_CARD, DIVIDER, 0.04)

    # Step number circle
    circle = slide.shapes.add_shape(
        MSO_SHAPE.OVAL, left + Inches(0.15), Inches(2.25), Inches(0.4), Inches(0.4)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = ACCENT_BLUE
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(16)
    tf.paragraphs[0].font.color.rgb = TEXT_WHITE
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.word_wrap = False

    add_text_box(slide, left + Inches(0.15), Inches(2.75), card_w - Inches(0.3), Inches(0.35),
                 title, font_size=11, color=ACCENT_BLUE, bold=True)
    add_text_box(slide, left + Inches(0.15), Inches(3.1), card_w - Inches(0.3), Inches(0.5),
                 line1, font_size=11, color=TEXT_LIGHT)
    add_text_box(slide, left + Inches(0.15), Inches(3.55), card_w - Inches(0.3), Inches(0.5),
                 line2, font_size=10, color=TEXT_DIM)

# Scope and controls
add_text_box(slide, Inches(0.8), Inches(4.7), Inches(6), Inches(0.4),
             "Pilot Scope", font_size=18, color=TEXT_WHITE, bold=True)

add_bullet_card(slide, Inches(0.8), Inches(5.15), Inches(5.5), Inches(2.1),
                "Bounded Starting Point",
                ["AXS drivetrain + Hammerhead device support only",
                 "Dealer inbox + high-volume web forms only",
                 "Compatibility and firmware issues first",
                 "Human approval on all customer-facing responses"],
                ACCENT_BLUE)

add_bullet_card(slide, Inches(6.6), Inches(5.15), Inches(5.5), Inches(2.1),
                "Risk Controls",
                ["Human approval for warranty + safety decisions",
                 "Answers from approved docs only, never model knowledge",
                 "Weekly quality review with rollback trigger",
                 "No automated warranty adjudication in Phase 1"],
                ACCENT_AMBER)


# ----------------------------------------------------------
# SLIDE 6: Success Metrics + Financial Impact
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_text_box(slide, Inches(0.8), Inches(0.4), Inches(6), Inches(0.5),
             "MEASURING SUCCESS", font_size=12, color=ACCENT_BLUE, bold=True)
add_text_box(slide, Inches(0.8), Inches(0.7), Inches(10), Inches(0.7),
             "Pilot Metrics and Year-1 Financial Impact", font_size=32, color=TEXT_WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.3), Inches(1.2), ACCENT_BLUE)

# Pilot metrics
add_text_box(slide, Inches(0.8), Inches(1.6), Inches(6), Inches(0.4),
             "90-Day Pilot Metrics", font_size=18, color=TEXT_WHITE, bold=True)

metrics = [
    ("Time-to-first-response", "40% reduction"),
    ("Tickets without escalation", "15% improvement"),
    ("Agent productivity", "25% increase"),
    ("AI draft acceptance rate", "Above 70%"),
    ("Customer satisfaction", "No decline from baseline"),
]

for i, (metric, target) in enumerate(metrics):
    y = Inches(2.1) + Inches(i * 0.45)
    add_text_box(slide, Inches(0.8), y, Inches(4), Inches(0.4),
                 metric, font_size=13, color=TEXT_LIGHT)
    add_text_box(slide, Inches(5.0), y, Inches(2.5), Inches(0.4),
                 target, font_size=13, color=ACCENT_GREEN, bold=True)

# Financial impact - right side
add_text_box(slide, Inches(7.5), Inches(1.6), Inches(5), Inches(0.4),
             "Year-1 Financial Impact (All Phases)", font_size=18, color=TEXT_WHITE, bold=True)

# Big numbers
add_metric_card(slide, Inches(7.5), Inches(2.1), Inches(2.5), Inches(1.4),
                "NET YEAR-1 VALUE", "$10.2M", ACCENT_GREEN, "Expected case")
add_metric_card(slide, Inches(10.2), Inches(2.1), Inches(2.5), Inches(1.4),
                "RETURN ON SPEND", "3.8x", ACCENT_GREEN, "On $2.7M total spend")

# Breakdown
fin_lines = [
    ("Cost Reductions", 14, TEXT_WHITE, True),
    ("Support automation: $1.6M", 12, TEXT_LIGHT, False),
    ("Demand forecasting: $1.6M", 12, TEXT_LIGHT, False),
    ("Documentation: $0.24M", 12, TEXT_LIGHT, False),
    ("", 8, TEXT_DIM, False),
    ("Revenue Growth", 14, TEXT_WHITE, True),
    ("Customer retention: $3.0M", 12, TEXT_LIGHT, False),
    ("Package size increase: $4.0M", 12, TEXT_LIGHT, False),
    ("Proposal win rate: $2.5M", 12, TEXT_LIGHT, False),
    ("", 8, TEXT_DIM, False),
    ("Gross value: $12.9M", 13, ACCENT_BLUE, True),
    ("Total spend: ($2.7M)", 13, ACCENT_AMBER, False),
    ("Net value: $10.2M", 13, ACCENT_GREEN, True),
]

add_multiline_text(slide, Inches(7.5), Inches(3.7), Inches(5), Inches(3.5),
                   fin_lines, line_spacing=1.3)


# ----------------------------------------------------------
# SLIDE 7: 2031 Vision - AI-First SRAM
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_text_box(slide, Inches(0.8), Inches(0.4), Inches(6), Inches(0.5),
             "WHAT COULD BE", font_size=12, color=ACCENT_GREEN, bold=True)
add_text_box(slide, Inches(0.8), Inches(0.7), Inches(10), Inches(0.7),
             "SRAM 2031 - From Hardware to Intelligence", font_size=32, color=TEXT_WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.3), Inches(1.2), ACCENT_GREEN)

add_text_box(slide, Inches(0.8), Inches(1.6), Inches(11), Inches(0.6),
             "SRAM's full product stack creates a data moat no competitor can replicate. "
             "The rider who buys SRAM drivetrain, RockShox suspension, Quarq power, and Hammerhead "
             "computer gets a unified intelligence layer impossible with mixed components.",
             font_size=14, color=TEXT_LIGHT)

# Vision cards
visions = [
    ("AXS Intelligence Platform",
     "Unified rider dashboard showing power, gearing, suspension, "
     "and heart rate in one view. No competitor has the product breadth to match this.",
     ACCENT_BLUE),
    ("Predictive Maintenance",
     "Connected components predict chain, cassette, and brake pad replacement "
     "before failure. Installed base becomes recurring revenue.",
     ACCENT_GREEN),
    ("AI-Tuned Performance",
     "Suspension auto-adjusts to terrain. Shifting optimizes for rider power "
     "patterns. Products improve continuously after purchase.",
     ACCENT_GREEN),
    ("Dealer Intelligence",
     "Aggregated telemetry tells dealers which parts approach end-of-life "
     "in their service area. Proactive ordering replaces reactive.",
     ACCENT_BLUE),
]

for i, (title, desc, color) in enumerate(visions):
    row = i // 2
    col = i % 2
    left = Inches(0.8) + Inches(col * 5.8)
    top = Inches(2.5) + Inches(row * 2.2)
    card_w = Inches(5.5)
    card_h = Inches(1.9)

    card = add_shape(slide, left, top, card_w, card_h, BG_CARD, DIVIDER, 0.04)
    add_text_box(slide, left + Inches(0.3), top + Inches(0.2),
                 card_w - Inches(0.6), Inches(0.4),
                 title, font_size=16, color=color, bold=True)
    add_text_box(slide, left + Inches(0.3), top + Inches(0.65),
                 card_w - Inches(0.6), Inches(1.0),
                 desc, font_size=12, color=TEXT_LIGHT)

# Flywheel statement
add_shape(slide, Inches(0.8), Inches(6.8), Inches(11.5), Inches(0.5), BG_CARD, ACCENT_GREEN, 0.1)
add_text_box(slide, Inches(1.3), Inches(6.85), Inches(10.5), Inches(0.4),
             "The Flywheel: Hardware sells data access  \u2192  Data improves performance  \u2192  Performance sells hardware",
             font_size=14, color=ACCENT_GREEN, bold=True, alignment=PP_ALIGN.CENTER)


# ----------------------------------------------------------
# SLIDE 8: The Ask
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank_layout)
set_slide_bg(slide, BG_DARK)

add_text_box(slide, Inches(0.8), Inches(0.4), Inches(6), Inches(0.5),
             "THE DECISION", font_size=12, color=ACCENT_BLUE, bold=True)
add_text_box(slide, Inches(0.8), Inches(0.7), Inches(10), Inches(0.7),
             "Three Actions for SRAM's CEO", font_size=32, color=TEXT_WHITE, bold=True)
add_accent_line(slide, Inches(0.8), Inches(1.3), Inches(1.2), ACCENT_BLUE)

actions = [
    ("1", "Launch the 90-Day Support Pilot",
     "Scope it to AXS and Hammerhead dealer support. "
     "One product owner, one integration engineer. "
     "Human approval on all customer-facing outputs. Weekly quality reviews.",
     ACCENT_GREEN),
    ("2", "Begin Data Infrastructure Planning",
     "Initiate requirements for a unified data layer connecting Shopify, "
     "support systems, and telemetry data. This is the foundation for "
     "demand forecasting and AXS Intelligence.",
     ACCENT_BLUE),
    ("3", "Hold Sequencing Discipline",
     "Bounded, well-defined problems first. Broader transformation after "
     "measured proof. The 90-day pilot produces data to justify or redirect "
     "every subsequent investment.",
     ACCENT_AMBER),
]

for i, (num, title, desc, color) in enumerate(actions):
    top = Inches(1.8) + Inches(i * 1.8)

    card = add_shape(slide, Inches(0.8), top, Inches(11.5), Inches(1.5), BG_CARD, color, 0.03)

    # Number
    circle = slide.shapes.add_shape(
        MSO_SHAPE.OVAL, Inches(1.2), top + Inches(0.35), Inches(0.6), Inches(0.6)
    )
    circle.fill.solid()
    circle.fill.fore_color.rgb = color
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(22)
    tf.paragraphs[0].font.color.rgb = BG_DARK
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf.word_wrap = False

    add_text_box(slide, Inches(2.2), top + Inches(0.2), Inches(9.5), Inches(0.5),
                 title, font_size=20, color=TEXT_WHITE, bold=True)
    add_text_box(slide, Inches(2.2), top + Inches(0.7), Inches(9.5), Inches(0.7),
                 desc, font_size=13, color=TEXT_LIGHT)

# Bottom line
add_shape(slide, Inches(0.8), Inches(7.0), Inches(11.5), Inches(0.01), DIVIDER)

add_multiline_text(slide, Inches(0.8), Inches(6.3), Inches(11.5), Inches(0.7), [
    ("Expected Year-1 return: 3.8x  |  Downside bounded by 90-day pilot scope  |  "
     "Upside scales with SRAM's unique data advantage",
     13, ACCENT_GREEN, True),
])


# ----------------------------------------------------------
# SAVE
# ----------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
out_dir = os.path.join(repo_root, "presentation")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "SRAM_AI_Adoption_Playbook.pptx")
prs.save(out_path)
print(f"Saved presentation to {out_path}")
print(f"Slides: {len(prs.slides)}")
