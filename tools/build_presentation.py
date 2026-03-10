#!/usr/bin/env python3
"""
Build the SRAM AI Adoption Playbook presentation.

McKinsey-grade executive deck for an 8-minute class presentation.
Uses Duarte's "What Is / What Could Be" contrast pattern with
action titles (each slide title states the conclusion, not the topic).

Color scheme: SRAM brand palette, light theme.

Usage:
    python3 tools/build_presentation.py

Output:
    presentation/SRAM_AI_Adoption_Playbook.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
import os

# --- SRAM brand palette, light theme ---
# Sourced from sram.com: #1C1C1E, #E51937, #767676, #D9DBD8, #FFFFFF
BG_WHITE = RGBColor(0xF5, 0xF5, 0xF3)       # Warm off-white slide background
CARD_BG = RGBColor(0xFF, 0xFF, 0xFF)         # White card backgrounds
CARD_BORDER = RGBColor(0xE0, 0xE0, 0xDE)     # Subtle warm gray border
TEXT_PRIMARY = RGBColor(0x1C, 0x1C, 0x1E)    # SRAM near-black for headings
TEXT_BODY = RGBColor(0x3A, 0x3A, 0x3C)       # Dark gray for body text
TEXT_SECONDARY = RGBColor(0x76, 0x76, 0x76)  # SRAM mid-gray (#767676)
ACCENT_RED = RGBColor(0xE5, 0x19, 0x37)      # SRAM red - used sparingly
ACCENT_RED_SOFT = RGBColor(0xC4, 0x3B, 0x4F) # Muted red for emphasis
LIGHT_GRAY_BG = RGBColor(0xF0, 0xF0, 0xEE)  # Alternating row backgrounds
HIGHLIGHT_BG = RGBColor(0xFD, 0xF0, 0xF2)   # Very subtle red tint for highlight

SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# Shorthand
BG = BG_WHITE
CARD = CARD_BG
BORDER = CARD_BORDER
BLACK = TEXT_PRIMARY
BODY = TEXT_BODY
GRAY = TEXT_SECONDARY
RED = ACCENT_RED
FONT = "Calibri"


def set_slide_bg(slide, color=BG):
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = color


def add_rect(slide, left, top, width, height, fill=CARD, border=BORDER, radius=0.04):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if border:
        shape.line.color.rgb = border
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    shape.adjustments[0] = radius
    return shape


def text(slide, left, top, w, h, content, size=14, color=BODY, bold=False,
         align=PP_ALIGN.LEFT, italic=False):
    box = slide.shapes.add_textbox(left, top, w, h)
    box.text_frame.word_wrap = True
    p = box.text_frame.paragraphs[0]
    p.text = content
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = FONT
    p.font.italic = italic
    p.alignment = align
    return box


def multitext(slide, left, top, w, h, lines, spacing=1.3):
    box = slide.shapes.add_textbox(left, top, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    for i, (t, size, color, bold) in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = t
        p.font.size = Pt(size)
        p.font.color.rgb = color
        p.font.bold = bold
        p.font.name = FONT
        p.space_after = Pt(size * (spacing - 1) * 2)
    return box


def slide_header(slide, label, title):
    """Action-title header: small label + bold conclusion statement."""
    text(slide, Inches(0.8), Inches(0.3), Inches(6), Inches(0.25),
         label, size=11, color=GRAY, bold=True)
    text(slide, Inches(0.8), Inches(0.6), Inches(11.5), Inches(0.55),
         title, size=26, color=BLACK, bold=True)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                  Inches(0.8), Inches(1.15), Inches(0.8), Pt(3))
    line.fill.solid()
    line.fill.fore_color.rgb = RED
    line.line.fill.background()


def slide_footer(slide, page_num):
    """Consistent footer with page number."""
    text(slide, Inches(0.8), Inches(7.05), Inches(5), Inches(0.3),
         "SRAM AI Adoption Playbook", size=8, color=GRAY)
    text(slide, Inches(11.5), Inches(7.05), Inches(1.5), Inches(0.3),
         str(page_num), size=8, color=GRAY, align=PP_ALIGN.RIGHT)


def metric_card(slide, left, top, w, h, label, value, val_color=BLACK, sub=None):
    add_rect(slide, left, top, w, h, CARD, BORDER)
    text(slide, left + Inches(0.25), top + Inches(0.15), w - Inches(0.5), Inches(0.25),
         label, size=10, color=GRAY)
    text(slide, left + Inches(0.25), top + Inches(0.4), w - Inches(0.5), Inches(0.45),
         value, size=26, color=val_color, bold=True)
    if sub:
        text(slide, left + Inches(0.25), top + Inches(0.9), w - Inches(0.5), Inches(0.25),
             sub, size=9, color=GRAY)


def bullet_list(slide, left, top, w, h, items, color=BODY, size=12):
    lines = [(f"\u2022  {item}", size, color, False) for item in items]
    multitext(slide, left, top, w, h, lines, spacing=1.5)


def quote_box(slide, left, top, w, h, quote, attribution):
    """Styled quote callout with left accent bar."""
    add_rect(slide, left, top, w, h, CARD, BORDER)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, Pt(4), h)
    bar.fill.solid()
    bar.fill.fore_color.rgb = GRAY
    bar.line.fill.background()
    text(slide, left + Inches(0.35), top + Inches(0.1), w - Inches(0.6), h - Inches(0.4),
         f"\u201C{quote}\u201D", size=12, color=BODY, italic=True)
    text(slide, left + Inches(0.35), top + h - Inches(0.3), w - Inches(0.6), Inches(0.25),
         attribution, size=10, color=GRAY, bold=True)


def arrow_right(slide, left, top, w=Inches(0.3), h=Inches(0.3)):
    """Small right-pointing triangle arrow."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE, left, top, w, h)
    shape.rotation = 90.0
    shape.fill.solid()
    shape.fill.fore_color.rgb = GRAY
    shape.line.fill.background()


# ============================================================
# BUILD
# ============================================================

prs = Presentation()
prs.slide_width = SLIDE_WIDTH
prs.slide_height = SLIDE_HEIGHT
blank = prs.slide_layouts[6]
page = 0


# ----------------------------------------------------------
# SLIDE 1: Title
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)

# Thin red accent bar
line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                              Inches(1.5), Inches(2.4), Inches(1.2), Pt(3))
line.fill.solid()
line.fill.fore_color.rgb = RED
line.line.fill.background()

multitext(slide, Inches(1.5), Inches(2.6), Inches(10), Inches(2.5), [
    ("SRAM LLC", 44, BLACK, True),
    ("AI Adoption Playbook", 26, GRAY, False),
    ("", 10, GRAY, False),
    ("A $10M opportunity starting with a 90-day pilot", 16, BODY, False),
    ("", 8, GRAY, False),
    ("Prepared for Executive Leadership  |  March 2026", 13, GRAY, False),
])

text(slide, Inches(1.5), Inches(6.3), Inches(10), Inches(0.4),
     "AIML 950  |  Human and Machine Intelligence  |  Northwestern Kellogg",
     size=10, color=GRAY)


# ----------------------------------------------------------
# SLIDE 2: SRAM Today (action title: ecosystem advantage)
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "WHAT IS",
             "SRAM's connected ecosystem is unmatched in cycling")

text(slide, Inches(0.8), Inches(1.35), Inches(11.5), Inches(0.4),
     "Private, Chicago-founded. Second-largest bicycle component manufacturer globally. "
     "Dominant in mountain bike. Seven brands, three channels.",
     size=13, color=BODY)

# Metrics row - seed the Trustpilot problem early (Duarte tension)
metrics_data = [
    ("REVENUE", "$1B+", "Private, not disclosed", BLACK),
    ("BRANDS", "7", "Integrated portfolio", BLACK),
    ("MTB SHARE", "#1", "Market leader", BLACK),
    ("TRUSTPILOT", "1.6 / 5.0", "Support-driven churn risk", ACCENT_RED_SOFT),
]
for i, (label, value, sub, vc) in enumerate(metrics_data):
    metric_card(slide, Inches(0.8 + i * 3.05), Inches(2.0), Inches(2.8), Inches(1.25),
                label, value, vc, sub)

# The ecosystem story - horizontal flow of brands
text(slide, Inches(0.8), Inches(3.55), Inches(11.5), Inches(0.3),
     "The Connected Ecosystem (no competitor matches this breadth)",
     size=16, color=BLACK, bold=True)

eco_items = [
    ("SRAM", "Drivetrains\n+ Braking"),
    ("RockShox", "Suspension"),
    ("Zipp", "Wheels +\nCockpit"),
    ("Quarq", "Power\nMeters"),
    ("Hammerhead", "Cycling\nComputer"),
    ("TIME", "Pedals"),
]
for i, (brand, desc) in enumerate(eco_items):
    left = Inches(0.8 + i * 2.05)
    card_w = Inches(1.85)
    add_rect(slide, left, Inches(4.0), card_w, Inches(1.15), CARD, BORDER)
    text(slide, left + Inches(0.15), Inches(4.08), card_w - Inches(0.3), Inches(0.25),
         brand, size=11, color=BLACK, bold=True)
    text(slide, left + Inches(0.15), Inches(4.4), card_w - Inches(0.3), Inches(0.6),
         desc, size=10, color=GRAY)
    if i < len(eco_items) - 1:
        arrow_right(slide, left + card_w + Inches(0.02), Inches(4.45))

# AXS connector bar
add_rect(slide, Inches(0.8), Inches(5.35), Inches(12.1), Inches(0.35),
         CARD, BORDER, 0.1)
text(slide, Inches(1.2), Inches(5.37), Inches(11.3), Inches(0.3),
     "AXS Wireless Ecosystem  |  All connected, all generating data, "
     "all controlled through one platform",
     size=11, color=BLACK, bold=True, align=PP_ALIGN.CENTER)

# Interview quote - competitive advantage
quote_box(slide, Inches(0.8), Inches(5.9), Inches(12.1), Inches(0.85),
          "A Shimano rider uses the app to check compatibility. A Hammerhead rider uses it "
          "to train, navigate, and communicate with their component stack. That is a "
          "fundamentally different data relationship.",
          "Jordan Hartsell, VP Digital Products, SRAM")

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 3: Initiative Map (with highlighted pilot pick)
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "WHERE AI ADDS VALUE",
             "12 AI initiatives across four business functions")

text(slide, Inches(0.8), Inches(1.35), Inches(11), Inches(0.35),
     "Every function at SRAM has AI potential. Ordered by implementation "
     "complexity and time to return.",
     size=13, color=BODY)

initiatives = [
    ("SUPPORT", "AI Support Agent", "70% of dealer questions are repetitive", True),
    ("SUPPORT", "Warranty Automation", "Fraudulent and mis-filed claims cost time", False),
    ("SUPPORT", "Compatibility Assistant", "Riders get wrong parts, return them", False),
    ("SUPPLY CHAIN", "Demand Forecasting", "No forecasting system exists today", False),
    ("SUPPLY CHAIN", "Inventory Allocation", "Stockouts and rush shipping losses", False),
    ("SUPPLY CHAIN", "Customer Analytics", "Shopify data is siloed, unused", False),
    ("SALES", "OEM Proposal Automation", "Proposal cycles are slow, manual", False),
    ("SALES", "Part Recommendations", "No guided upsell at point of service", False),
    ("SALES", "DTC Personalization", "Velocio has no targeting capability", False),
    ("ENGINEERING", "Generative Design", "Physical testing is slow and expensive", False),
    ("ENGINEERING", "AXS Intelligence", "Telemetry data is collected but unused", False),
    ("ENGINEERING", "AI-Tuned Components", "Suspension and shifting are static", False),
]

for i, (area, initiative, problem, highlight) in enumerate(initiatives):
    col = i % 3
    row = i // 3
    left = Inches(0.8) + Inches(col * 4.1)
    top = Inches(2.0) + Inches(row * 1.25)
    card_w = Inches(3.85)
    card_h = Inches(1.05)

    if highlight:
        add_rect(slide, left, top, card_w, card_h, HIGHLIGHT_BG, RED)
        # Red left-edge accent bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                     left, top, Pt(4), card_h)
        bar.fill.solid()
        bar.fill.fore_color.rgb = RED
        bar.line.fill.background()
        text(slide, left + Inches(0.2), top + Inches(0.08), Inches(2.5), Inches(0.2),
             f"{area}  |  RECOMMENDED PILOT", size=8, color=RED, bold=True)
    else:
        add_rect(slide, left, top, card_w, card_h, CARD, BORDER)
        text(slide, left + Inches(0.2), top + Inches(0.08), Inches(1.5), Inches(0.2),
             area, size=8, color=GRAY, bold=True)
    text(slide, left + Inches(0.2), top + Inches(0.3), card_w - Inches(0.4), Inches(0.3),
         initiative, size=13, color=BLACK, bold=True)
    text(slide, left + Inches(0.2), top + Inches(0.65), card_w - Inches(0.4), Inches(0.35),
         problem, size=10, color=GRAY)

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 5: The Problem (with interview evidence)
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE PROBLEM",
             "Support quality drives churn, not product quality")

text(slide, Inches(0.8), Inches(1.35), Inches(11), Inches(0.35),
     "Riders love SRAM hardware. They struggle with firmware, "
     "compatibility, and warranty resolution.",
     size=13, color=BODY)

# Three big metrics
metric_card(slide, Inches(0.8), Inches(1.95), Inches(3.6), Inches(1.35),
            "TRUSTPILOT RATING", "1.6 / 5.0", ACCENT_RED_SOFT,
            "Warranty friction and support delays")
metric_card(slide, Inches(4.7), Inches(1.95), Inches(3.6), Inches(1.35),
            "AUTOMATABLE QUESTIONS", "~70%", BLACK,
            "Follow repeatable, documented patterns")
metric_card(slide, Inches(8.6), Inches(1.95), Inches(4.0), Inches(1.35),
            "TOP COMPLAINTS", "Firmware + Pairing", ACCENT_RED_SOFT,
            "Reddit, app stores, Trustpilot 2024-2025")

# Two columns: pain vs. advantage
add_rect(slide, Inches(0.8), Inches(3.65), Inches(5.5), Inches(2.45), CARD, BORDER)
text(slide, Inches(1.1), Inches(3.8), Inches(4.5), Inches(0.3),
     "Customer Pain Signals", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(1.1), Inches(4.15), Inches(4.8), Inches(1.8),
            ["Trustpilot reviews cite warranty frustration and delays",
             "Reddit 2024-25 threads on pairing failures and shifting",
             "App store reviews flag AXS and Hammerhead bugs",
             "Riders explicitly stating intent to switch to Shimano"],
            BODY, 11)

add_rect(slide, Inches(6.6), Inches(3.65), Inches(6.0), Inches(2.45), CARD, BORDER)
text(slide, Inches(6.9), Inches(3.8), Inches(5.0), Inches(0.3),
     "Why SRAM Can Fix This with AI", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(6.9), Inches(4.15), Inches(5.4), Inches(1.8),
            ["Structured knowledge base with manuals and guides",
             "AXS telemetry data on firmware, error codes, device state",
             "Hammerhead ride and device diagnostic data",
             "60-70% data-ready for AXS/Hammerhead support (per VP)"],
            BODY, 11)

# Interview quote at bottom
quote_box(slide, Inches(0.8), Inches(6.3), Inches(11.8), Inches(0.7),
          "The first question I ask anyone skeptical about AI is: do you want to spend "
          "your day searching a 200-page compatibility PDF, or do you want to spend it "
          "talking to dealers?",
          "Jordan Hartsell, VP Digital Products, SRAM")

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 6: The 90-Day Pilot
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE SOLUTION",
             "A 90-day pilot with human approval on every response")

# Workflow: 5 steps with arrows between them
steps = [
    ("1", "TICKET IN", "Dealer or rider\nsubmits via Zendesk"),
    ("2", "AI RETRIEVES", "Amazon Kendra\nfinds approved docs"),
    ("3", "AI DRAFTS", "Amazon Bedrock\nfrom knowledge base"),
    ("4", "HUMAN REVIEWS", "Agent approves\nbefore sending"),
    ("5", "QUALITY LOGGED", "Metrics tracked;\nweekly review"),
]

for i, (num, title, desc) in enumerate(steps):
    left = Inches(0.8) + Inches(i * 2.45)
    card_w = Inches(2.15)

    add_rect(slide, left, Inches(1.5), card_w, Inches(2.0), CARD, BORDER)

    # Number circle
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.15), Inches(1.65),
                                    Inches(0.35), Inches(0.35))
    circle.fill.solid()
    circle.fill.fore_color.rgb = BLACK
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(14)
    tf.paragraphs[0].font.color.rgb = BG_WHITE
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER

    text(slide, left + Inches(0.15), Inches(2.1), card_w - Inches(0.3), Inches(0.25),
         title, size=10, color=BLACK, bold=True)
    text(slide, left + Inches(0.15), Inches(2.4), card_w - Inches(0.3), Inches(0.9),
         desc, size=11, color=BODY)

    # Arrow between steps
    if i < len(steps) - 1:
        arrow_right(slide, left + card_w + Inches(0.02), Inches(2.35))

# Scope + Controls
add_rect(slide, Inches(0.8), Inches(3.85), Inches(5.8), Inches(2.55), CARD, BORDER)
text(slide, Inches(1.1), Inches(4.0), Inches(5.0), Inches(0.3),
     "Pilot Scope", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(1.1), Inches(4.35), Inches(5.2), Inches(1.8),
            ["AXS drivetrain + Hammerhead device support only",
             "Dealer inbox and high-volume web forms",
             "Compatibility and firmware issues first",
             "Human approval on all customer-facing responses"],
            BODY, 11)

add_rect(slide, Inches(6.85), Inches(3.85), Inches(5.8), Inches(2.55), CARD, BORDER)
text(slide, Inches(7.15), Inches(4.0), Inches(5.0), Inches(0.3),
     "Risk Controls", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(7.15), Inches(4.35), Inches(5.2), Inches(1.8),
            ["Human approval for warranty and safety decisions",
             "Answers sourced from approved docs only",
             "Weekly quality review with rollback trigger",
             "No automated warranty adjudication in Phase 1"],
            BODY, 11)

# Hartsell validation quote
quote_box(slide, Inches(0.8), Inches(6.6), Inches(11.8), Inches(0.55),
          "I would rather shut it down and restart than defend a mistake to Ken.",
          "Jordan Hartsell on the pull-the-plug criteria")

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 7: Metrics + Financials
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE RETURN",
             "$10.2M net value in Year 1 on $2.7M spend")

# LEFT: SMART Goals
text(slide, Inches(0.8), Inches(1.45), Inches(5.5), Inches(0.3),
     "SMART Goals (90 Days)", size=16, color=BLACK, bold=True)

smart_goals = [
    ("1", "First-response time", "-40%", "vs. current SLA"),
    ("2", "Tickets without escalation", "+15 pts", "vs. current rate"),
    ("3", "AI draft acceptance", ">70%", "agents approve draft"),
    ("4", "Agent throughput", "+25%", "tickets per agent/day"),
    ("5", "Customer satisfaction", "No decline", "CSAT holds flat"),
]

for i, (num, goal, target, detail) in enumerate(smart_goals):
    y = Inches(1.9) + Inches(i * 0.42)
    if i % 2 == 0:
        add_rect(slide, Inches(0.8), y - Inches(0.02), Inches(5.5), Inches(0.38),
                 LIGHT_GRAY_BG, None, 0.02)
    text(slide, Inches(0.9), y, Inches(0.25), Inches(0.3), num,
         size=11, color=GRAY, bold=True)
    text(slide, Inches(1.15), y, Inches(2.3), Inches(0.3), goal, size=11, color=BODY)
    text(slide, Inches(3.5), y, Inches(1.0), Inches(0.3), target,
         size=11, color=BLACK, bold=True)
    text(slide, Inches(4.5), y, Inches(1.7), Inches(0.3), detail,
         size=9, color=GRAY)

# Support savings math
text(slide, Inches(0.8), Inches(4.1), Inches(5.5), Inches(0.3),
     "Support Savings Math", size=14, color=BLACK, bold=True)
text(slide, Inches(0.8), Inches(4.45), Inches(5.5), Inches(0.9),
     "120 support staff x $90K avg. cost\n"
     "x 60% AI-addressable work\n"
     "x 35% productivity gain\n"
     "x 70% adoption = $1.6M",
     size=11, color=BODY)

# Scenario range
text(slide, Inches(0.8), Inches(5.55), Inches(5.5), Inches(0.3),
     "Scenario Range", size=14, color=BLACK, bold=True)

scenarios = [
    ("Conservative", "$4.5M net", "2.8x"),
    ("Expected", "$10.2M net", "3.8x"),
    ("Upside", "$22.5M net", "6.4x"),
]
for i, (label, value, roi) in enumerate(scenarios):
    y = Inches(5.9) + Inches(i * 0.35)
    text(slide, Inches(1.0), y, Inches(1.5), Inches(0.3), label, size=11, color=GRAY)
    text(slide, Inches(2.5), y, Inches(1.5), Inches(0.3), value,
         size=11, color=BLACK, bold=True)
    text(slide, Inches(4.0), y, Inches(1.0), Inches(0.3), roi, size=11, color=GRAY)

# RIGHT: Financial summary
text(slide, Inches(7.0), Inches(1.45), Inches(5.5), Inches(0.3),
     "Year-1 Financial Impact (All Phases)", size=16, color=BLACK, bold=True)

# Hero metric cards
metric_card(slide, Inches(7.0), Inches(1.9), Inches(2.8), Inches(1.2),
            "NET YEAR-1 VALUE", "$10.2M", BLACK, "Expected case")
metric_card(slide, Inches(10.0), Inches(1.9), Inches(2.8), Inches(1.2),
            "RETURN ON SPEND", "3.8x", BLACK, "On $2.7M total spend")

# Breakdown
fin_lines = [
    ("Cost Reductions", 13, BLACK, True),
    ("Support automation savings: $1.6M", 11, BODY, False),
    ("Demand forecasting savings: $1.6M", 11, BODY, False),
    ("Documentation and translation: $0.24M", 11, BODY, False),
    ("", 5, GRAY, False),
    ("Revenue Growth", 13, BLACK, True),
    ("Customer retention: $3.0M", 11, BODY, False),
    ("Package size increase: $4.0M", 11, BODY, False),
    ("Proposal win rate: $2.5M", 11, BODY, False),
]
multitext(slide, Inches(7.0), Inches(3.3), Inches(5.5), Inches(2.6), fin_lines, 1.2)

# Bottom summary
add_rect(slide, Inches(7.0), Inches(5.8), Inches(5.8), Inches(0.85), CARD, BORDER, 0.02)
multitext(slide, Inches(7.3), Inches(5.85), Inches(5.2), Inches(0.8), [
    ("Gross value: $12.9M", 12, BLACK, True),
    ("Setup + operating costs: ($2.7M)", 11, GRAY, False),
    ("Net value: $10.2M  |  Return: 3.8x", 13, BLACK, True),
], 1.15)

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 8: 2031 Vision
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "WHAT COULD BE",
             "Hardware company to performance intelligence by 2031")

text(slide, Inches(0.8), Inches(1.35), Inches(11.5), Inches(0.35),
     "Each connected SRAM product a rider buys increases the value of the data "
     "and the quality of the AI. No competitor can replicate this full-stack advantage.",
     size=13, color=BODY)

# Phase timeline across the top
phases = [
    ("PHASE 1", "0-90 days", "Support Pilot",
     "AI-assisted support\nfor AXS + Hammerhead"),
    ("PHASE 2", "90-180 days", "Data Foundation",
     "Unified data layer\n+ demand forecasting"),
    ("PHASE 3", "180-365 days", "Revenue Acceleration",
     "OEM automation +\npart recommendations"),
    ("PHASE 4", "Year 2+", "AI-First Culture",
     "AXS Intelligence\n+ predictive maintenance"),
]

for i, (phase, timing, title, desc) in enumerate(phases):
    left = Inches(0.8 + i * 3.1)
    card_w = Inches(2.85)
    bg_color = HIGHLIGHT_BG if i == 0 else CARD
    border_color = RED if i == 0 else BORDER
    add_rect(slide, left, Inches(1.95), card_w, Inches(1.55), bg_color, border_color)
    text(slide, left + Inches(0.2), Inches(2.05), card_w - Inches(0.4), Inches(0.2),
         f"{phase}  |  {timing}", size=9,
         color=RED if i == 0 else GRAY, bold=True)
    text(slide, left + Inches(0.2), Inches(2.3), card_w - Inches(0.4), Inches(0.3),
         title, size=14, color=BLACK, bold=True)
    text(slide, left + Inches(0.2), Inches(2.65), card_w - Inches(0.4), Inches(0.65),
         desc, size=11, color=BODY)
    if i < len(phases) - 1:
        arrow_right(slide, left + card_w + Inches(0.02), Inches(2.55))

# 2031 vision cards (2x2)
visions = [
    ("AXS Intelligence Platform",
     "Unified rider dashboard: power, gearing, suspension, heart rate "
     "in one view. No competitor has the product breadth to build this."),
    ("Predictive Maintenance",
     "Connected components predict chain and brake pad replacement "
     "before failure. Installed base becomes recurring revenue."),
    ("AI-Tuned Performance",
     "Suspension auto-adjusts to terrain. Shifting optimizes for rider "
     "power. Products improve continuously after purchase."),
    ("Dealer Intelligence",
     "Telemetry tells dealers which parts approach end-of-life in their "
     "area. Proactive ordering replaces reactive."),
]

for i, (title, desc) in enumerate(visions):
    col = i % 2
    row = i // 2
    left = Inches(0.8) + Inches(col * 6.2)
    top = Inches(3.85) + Inches(row * 1.35)
    card_w = Inches(5.95)
    card_h = Inches(1.15)

    add_rect(slide, left, top, card_w, card_h, CARD, BORDER)
    text(slide, left + Inches(0.25), top + Inches(0.1), card_w - Inches(0.5), Inches(0.3),
         title, size=13, color=BLACK, bold=True)
    text(slide, left + Inches(0.25), top + Inches(0.4), card_w - Inches(0.5), Inches(0.6),
         desc, size=11, color=BODY)

# Flywheel
add_rect(slide, Inches(0.8), Inches(6.65), Inches(11.7), Inches(0.4), CARD, BORDER, 0.1)
red_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(0.8), Inches(6.65), Pt(4), Inches(0.4))
red_bar.fill.solid()
red_bar.fill.fore_color.rgb = RED
red_bar.line.fill.background()
text(slide, Inches(1.2), Inches(6.68), Inches(11.0), Inches(0.3),
     "Hardware sells data access  \u2192  Data improves performance  "
     "\u2192  Performance sells hardware",
     size=13, color=BLACK, bold=True, align=PP_ALIGN.CENTER)

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 9: The Ask
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE DECISION",
             "Three actions for SRAM's CEO")

actions = [
    ("1", "Launch the 90-Day Support Pilot",
     "AXS and Hammerhead dealer support. One product owner, one integration "
     "engineer. Human approval on all outputs. Weekly quality reviews with "
     "defined rollback trigger."),
    ("2", "Begin Data Infrastructure Planning",
     "Unified data layer connecting Shopify, support systems, and telemetry. "
     "Foundation for Phase 2 forecasting and Phase 4 AXS Intelligence platform."),
    ("3", "Hold Sequencing Discipline",
     "Bounded, well-defined problems first. Broader transformation after measured "
     "proof. The 90-day pilot produces data to justify or redirect every "
     "subsequent investment."),
]

for i, (num, title, desc) in enumerate(actions):
    top = Inches(1.5) + Inches(i * 1.55)
    add_rect(slide, Inches(0.8), top, Inches(11.5), Inches(1.3), CARD, BORDER)

    # Number circle
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.2), top + Inches(0.25),
                                    Inches(0.5), Inches(0.5))
    circle.fill.solid()
    circle.fill.fore_color.rgb = BLACK
    circle.line.fill.background()
    tf = circle.text_frame
    tf.paragraphs[0].text = num
    tf.paragraphs[0].font.size = Pt(18)
    tf.paragraphs[0].font.color.rgb = BG_WHITE
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER

    text(slide, Inches(2.0), top + Inches(0.1), Inches(9.8), Inches(0.35),
         title, size=18, color=BLACK, bold=True)
    text(slide, Inches(2.0), top + Inches(0.5), Inches(9.8), Inches(0.6),
         desc, size=12, color=BODY)

# Bottom bar
add_rect(slide, Inches(0.8), Inches(6.25), Inches(11.5), Inches(0.6), CARD, BORDER, 0.1)
red_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(0.8), Inches(6.25), Pt(4), Inches(0.6))
red_bar.fill.solid()
red_bar.fill.fore_color.rgb = RED
red_bar.line.fill.background()
multitext(slide, Inches(1.3), Inches(6.28), Inches(10.5), Inches(0.55), [
    ("Expected Year-1 return: 3.8x on $2.7M spend", 13, BLACK, True),
    ("Downside bounded by 90-day pilot  |  Upside scales with "
     "SRAM's data advantage", 11, GRAY, False),
], 1.1)

slide_footer(slide, page)


# ===========================================================
# APPENDIX SLIDES (for Q&A backup)
# ===========================================================

# ----------------------------------------------------------
# APPENDIX A1: Full Financial Breakdown
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "APPENDIX",
             "Financial detail across three scenarios")

headers = ["Category", "Conservative", "Expected", "Upside"]
rows = [
    ("Support assistant savings", "$0.5M", "$1.6M", "$4.3M"),
    ("Forecasting + inventory", "$0.7M", "$1.6M", "$4.5M"),
    ("Documentation + translation", "$0.1M", "$0.24M", "$0.9M"),
    ("Customer retention revenue", "$1.5M", "$3.0M", "$4.5M"),
    ("Package size increase", "$2.0M", "$4.0M", "$8.0M"),
    ("Proposal win-rate revenue", "$1.3M", "$2.5M", "$3.8M"),
]
totals = [
    ("Gross value", "$6.1M", "$12.9M", "$26.0M"),
    ("Setup costs", "($1.2M)", "($2.0M)", "($2.5M)"),
    ("Operating costs", "($0.4M)", "($0.7M)", "($1.0M)"),
    ("Net Year-1 value", "$4.5M", "$10.2M", "$22.5M"),
    ("Return on spend", "2.8x", "3.8x", "6.4x"),
]

# Header row
for j, h in enumerate(headers):
    x = Inches(0.8 + j * 3.0) if j > 0 else Inches(0.8)
    text(slide, x, Inches(1.5), Inches(3.0), Inches(0.3),
         h, size=11, color=GRAY, bold=True)

# Data rows
for i, (cat, c, e, u) in enumerate(rows):
    y = Inches(1.9 + i * 0.4)
    if i % 2 == 0:
        add_rect(slide, Inches(0.8), y - Inches(0.02), Inches(11.5), Inches(0.38),
                 LIGHT_GRAY_BG, None, 0.02)
    text(slide, Inches(0.8), y, Inches(3.0), Inches(0.3), cat, size=11, color=BODY)
    text(slide, Inches(3.8), y, Inches(3.0), Inches(0.3), c, size=11, color=BODY)
    text(slide, Inches(6.8), y, Inches(3.0), Inches(0.3), e,
         size=11, color=BLACK, bold=True)
    text(slide, Inches(9.8), y, Inches(3.0), Inches(0.3), u, size=11, color=BODY)

# Separator line
sep_y = Inches(1.9 + len(rows) * 0.4)
line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                              Inches(0.8), sep_y, Inches(11.5), Pt(1))
line.fill.solid()
line.fill.fore_color.rgb = BORDER
line.line.fill.background()

# Total rows
for i, (cat, c, e, u) in enumerate(totals):
    y = sep_y + Inches(0.15 + i * 0.4)
    is_key = cat in ("Net Year-1 value", "Return on spend")
    text(slide, Inches(0.8), y, Inches(3.0), Inches(0.3), cat,
         size=11, color=BLACK, bold=is_key)
    text(slide, Inches(3.8), y, Inches(3.0), Inches(0.3), c,
         size=11, color=BLACK if is_key else BODY, bold=is_key)
    text(slide, Inches(6.8), y, Inches(3.0), Inches(0.3), e,
         size=11, color=BLACK, bold=True)
    text(slide, Inches(9.8), y, Inches(3.0), Inches(0.3), u,
         size=11, color=BLACK if is_key else BODY, bold=is_key)

text(slide, Inches(0.8), Inches(7.0), Inches(10), Inches(0.3),
     "APPENDIX A1", size=8, color=GRAY)


# ----------------------------------------------------------
# APPENDIX A2: Interview Highlights
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "APPENDIX",
             "Interview with Jordan Hartsell, VP Digital Products")

text(slide, Inches(0.8), Inches(1.35), Inches(11), Inches(0.3),
     "45-minute Zoom call  |  March 2026  |  Key quotes and insights",
     size=12, color=GRAY)

quotes = [
    ("On data readiness",
     "We have good data in pockets and messy data everywhere else. If I wanted "
     "to build a support AI today, I could get it to work well for AXS and "
     "Hammerhead. The moment a dealer asks about a RockShox fork on a 2019 "
     "frame with a third-party brake, I start to sweat.",
     "Validates bounded pilot scope"),
    ("On adoption barriers",
     "The resistance comes from customer-facing teams because they worry AI "
     "will produce confident-sounding wrong answers that damage dealer "
     "relationships they have spent years building.",
     "Human-in-the-loop is mandatory"),
    ("On competitive advantage",
     "A Shimano rider uses the app to check compatibility. A Hammerhead rider "
     "uses it to train, navigate, and communicate with their component stack. "
     "That is a fundamentally different data relationship.",
     "Hammerhead is SRAM's real AI moat"),
    ("On success criteria",
     "I want one workflow measurably faster, measurably more accurate, with no "
     "regression in dealer satisfaction scores.",
     "Aligns with our 90-day pilot targets"),
]

for i, (topic, quote, implication) in enumerate(quotes):
    y = Inches(1.85 + i * 1.3)
    add_rect(slide, Inches(0.8), y, Inches(11.8), Inches(1.1), CARD, BORDER)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(0.8), y, Pt(4), Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = GRAY
    bar.line.fill.background()
    text(slide, Inches(1.2), y + Inches(0.05), Inches(2.0), Inches(0.2),
         topic.upper(), size=9, color=GRAY, bold=True)
    text(slide, Inches(1.2), y + Inches(0.28), Inches(8.0), Inches(0.6),
         f"\u201C{quote}\u201D", size=11, color=BODY, italic=True)
    text(slide, Inches(9.5), y + Inches(0.35), Inches(2.8), Inches(0.5),
         f"\u2192 {implication}", size=10, color=BLACK, bold=True)

text(slide, Inches(0.8), Inches(7.0), Inches(10), Inches(0.3),
     "APPENDIX A2", size=8, color=GRAY)


# ----------------------------------------------------------
# APPENDIX A3: Phasing and Organizational Requirements
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "APPENDIX",
             "Phasing, talent, and organizational enablers")

phase_details = [
    ("Phase 1: Support Pilot", "0-90 days",
     ["1 integration engineer (internal or contractor)",
      "1 product owner from support organization",
      "Zendesk AI + Amazon Kendra + Bedrock",
      "No new AI/ML hires required"]),
    ("Phase 2: Data Foundation", "90-180 days",
     ["Add product managers and QA capacity",
      "Unified data layer linking CRM + inventory + telemetry",
      "AWS SageMaker for forecasting",
      "ERP system evaluation"]),
    ("Phase 3: Revenue Acceleration", "180-365 days",
     ["Salesforce Einstein/Agentforce for OEM proposals",
      "Compatibility rules engine for recommendations",
      "Cross-functional product + sales alignment",
      "Expected $2.5M from 1% win-rate improvement"]),
    ("Phase 4: AI-First Culture", "Year 2+",
     ["AXS Intelligence Platform development",
      "Digital twin and generative design capability",
      "Predictive maintenance subscription model",
      "AI-adjusted component performance"]),
]

for i, (title, timing, items) in enumerate(phase_details):
    col = i % 2
    row = i // 2
    left = Inches(0.8 + col * 6.2)
    top = Inches(1.5 + row * 2.7)
    card_w = Inches(5.95)
    card_h = Inches(2.45)

    bg_color = HIGHLIGHT_BG if i == 0 else CARD
    border_color = RED if i == 0 else BORDER
    add_rect(slide, left, top, card_w, card_h, bg_color, border_color)
    text(slide, left + Inches(0.25), top + Inches(0.1), card_w - Inches(0.5), Inches(0.3),
         title, size=14, color=BLACK, bold=True)
    text(slide, left + Inches(0.25), top + Inches(0.35), Inches(2.0), Inches(0.2),
         timing, size=10, color=RED if i == 0 else GRAY, bold=True)
    bullet_list(slide, left + Inches(0.25), top + Inches(0.65), card_w - Inches(0.5),
                Inches(1.6), items, BODY, 11)

text(slide, Inches(0.8), Inches(7.0), Inches(10), Inches(0.3),
     "APPENDIX A3", size=8, color=GRAY)


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
print(f"Slides: {len(prs.slides)} (9 content + 3 appendix)")
