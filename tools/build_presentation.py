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
    deliverables/SRAM_AI_Adoption_Playbook.pptx
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
GANTT_ACCENT = RGBColor(0x2D, 0x5F, 0x8A)   # Steel blue for bars and badges
GANTT_LIGHT = RGBColor(0xD4, 0xE4, 0xF0)    # Light blue for setup bars

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
    ("", 6, GRAY, False),
    ("Donovan Palmer, Ed Kreienberg, Will Zheng", 13, GRAY, False),
])

text(slide, Inches(1.5), Inches(6.3), Inches(10), Inches(0.4),
     "AIML 950  |  Human and Machine Intelligence  |  Northwestern Kellogg",
     size=10, color=GRAY)


# ----------------------------------------------------------
# SLIDE 2: What is SRAM? (plain-language intro)
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "CONTEXT",
             "SRAM makes the parts that make bikes go, stop, and shift")

# Subtitle
text(slide, Inches(0.8), Inches(1.5), Inches(11), Inches(0.5),
     "A $1B+ company headquartered in Chicago, powering bikes from weekend rides to the Tour de France.",
     size=14, color=GRAY)

# Product category cards (text only) - matches ecosystem slide order
sram_cards = [
    ("Drivetrains + Braking", "SRAM",
     "Gears, chains, and disc\nbrakes for every bike"),
    ("Suspension", "RockShox",
     "Forks and shocks that\nabsorb trail impacts"),
    ("Wheels + Cockpit", "Zipp",
     "Aero wheels, handlebars,\nand stems"),
    ("Power Meters", "Quarq",
     "Sensors that measure\nrider output in watts"),
    ("GPS Bike Computer", "Hammerhead",
     "On-bike computer for\nnavigation and training data"),
    ("Pedals", "TIME",
     "Clip-in pedal systems\nfor road and mountain"),
]

n_cards = len(sram_cards)
total_avail = Inches(11.7)  # 13.333 - 0.8 margins on each side
intro_gap = Inches(0.25)
intro_card_w = (total_avail - intro_gap * (n_cards - 1)) / n_cards
intro_card_h = Inches(2.4)
intro_start_x = Inches(0.8)
intro_card_top = Inches(2.2)

for i, (label, brand, desc) in enumerate(sram_cards):
    cx = intro_start_x + i * (intro_card_w + intro_gap)
    add_rect(slide, int(cx), intro_card_top, int(intro_card_w), intro_card_h)
    # Brand name (small, above)
    text(slide, int(cx), intro_card_top + Inches(0.2), int(intro_card_w), Inches(0.25),
         brand, size=10, color=GRAY, bold=True, align=PP_ALIGN.CENTER)
    # Product category label
    text(slide, int(cx), intro_card_top + Inches(0.55), int(intro_card_w), Inches(0.5),
         label, size=16, color=BLACK, bold=True, align=PP_ALIGN.CENTER)
    # Description
    text(slide, int(cx) + Inches(0.15), intro_card_top + Inches(1.2),
         int(intro_card_w) - Inches(0.3), Inches(1.0),
         desc, size=11, color=BODY, align=PP_ALIGN.CENTER)

# Bottom line
text(slide, Inches(0.8), Inches(5.0), Inches(11.7), Inches(0.5),
     "6 brands. 1 connected ecosystem. From weekend riders to Tour de France pros.",
     size=14, color=BODY, bold=True, align=PP_ALIGN.CENTER)

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 3: SRAM Today (action title: ecosystem advantage)
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "WHAT IS",
             "SRAM's connected ecosystem is unmatched in cycling")

# Metrics row - seed the Trustpilot problem early (Duarte tension)
metrics_data = [
    ("REVENUE", "$1B+", "Private, Chicago-founded", BLACK),
    ("BRANDS", "6", "Integrated portfolio", BLACK),
    ("MTB SHARE", "#1", "Market leader globally", BLACK),
    ("TRUSTPILOT", "1.6 / 5.0", "Support-driven churn risk", ACCENT_RED_SOFT),
]
for i, (label, value, sub, vc) in enumerate(metrics_data):
    metric_card(slide, Inches(0.8 + i * 3.05), Inches(1.6), Inches(2.8), Inches(1.25),
                label, value, vc, sub)

# The ecosystem story - horizontal flow of brands
eco_items = [
    ("SRAM", "Drivetrains + Braking"),
    ("RockShox", "Suspension"),
    ("Zipp", "Wheels + Cockpit"),
    ("Quarq", "Power Meters"),
    ("Hammerhead", "GPS Bike Computer"),
    ("TIME", "Pedals"),
]
for i, (brand, desc) in enumerate(eco_items):
    left = Inches(0.8 + i * 2.05)
    card_w = Inches(1.85)
    add_rect(slide, left, Inches(3.3), card_w, Inches(0.85), CARD, BORDER)
    text(slide, left + Inches(0.15), Inches(3.38), card_w - Inches(0.3), Inches(0.25),
         brand, size=12, color=BLACK, bold=True)
    text(slide, left + Inches(0.15), Inches(3.7), card_w - Inches(0.3), Inches(0.35),
         desc, size=10, color=GRAY)
    if i < len(eco_items) - 1:
        arrow_right(slide, left + card_w + Inches(0.02), Inches(3.6))

# AXS connector bar
add_rect(slide, Inches(0.8), Inches(4.5), Inches(12.1), Inches(0.35),
         CARD, BORDER, 0.1)
text(slide, Inches(1.2), Inches(4.52), Inches(11.3), Inches(0.3),
     "AXS Wireless Ecosystem  |  All 6 brands connect wirelessly and share data",
     size=11, color=BLACK, bold=True, align=PP_ALIGN.CENTER)

# Interview quote - competitive advantage
quote_box(slide, Inches(0.8), Inches(5.3), Inches(12.1), Inches(0.85),
          "Shimano riders use an app to check compatibility. Our riders use an ecosystem to train, "
          "navigate, tune their suspension, and monitor their entire component stack in real time. "
          "That is a fundamentally different level of engagement.",
          "Clint Weber, VP Global Sales & Manufacturing, SRAM")

text(slide, Inches(0.8), Inches(6.5), Inches(11.5), Inches(0.25),
     "Sources: MTB share per Bicycle Retailer industry analysis; Trustpilot rating as of Feb 2026 (n=180+ reviews)",
     size=8, color=GRAY)

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 3: Initiative Map (progressive build - 4 slides)
# ----------------------------------------------------------

# Function color coding
FUNC_COLORS = {
    "SUPPORT": RGBColor(0x2D, 0x5F, 0x8A),       # Steel blue
    "SUPPLY CHAIN": RGBColor(0x5B, 0x8C, 0x5A),   # Forest green
    "SALES": RGBColor(0x8B, 0x6D, 0x2E),           # Amber/gold
    "ENGINEERING": RGBColor(0x7A, 0x5C, 0x8A),     # Purple
}

# Rows grouped by function (top to bottom on slide)
# Order: ambitious/complex at top, measurable/proven at bottom
# Progressive reveal goes top-down, so SUPPORT lands last as the punchline
initiative_rows = [
    ("ENGINEERING", [
        ("Generative Design", "Physical testing is slow and expensive", False),
        ("AXS Intelligence", "Telemetry data is collected but unused", False),
        ("AI-Tuned Components", "Suspension and shifting are static", False),
    ]),
    ("SALES", [
        ("OEM Proposal Automation", "Proposal cycles are slow, manual", False),
        ("Part Recommendations", "No guided upsell at point of service", False),
        ("DTC Personalization", "Velocio has no targeting capability", False),
    ]),
    ("SUPPLY CHAIN", [
        ("Demand Forecasting", "No forecasting system exists today", False),
        ("Inventory Allocation", "Stockouts and rush shipping losses", False),
        ("Customer Analytics", "Shopify data is siloed, unused", False),
    ]),
    ("SUPPORT", [
        ("AI Support Agent", "70% of dealer questions are repetitive", True),
        ("Warranty Automation", "Fraudulent and mis-filed claims cost time", False),
        ("Compatibility Assistant", "Riders get wrong parts, return them", False),
    ]),
]

grid_left = Inches(2.4)
card_w = Inches(3.2)
card_h = Inches(0.9)

# Build order: top-down (ENGINEERING, +SALES, +SUPPLY CHAIN, +SUPPORT)
# Support lands last as the punchline with START HERE outline
page += 1
for build_step in range(4):
    # Rows visible: build_step=0 -> row 0 only, =1 -> rows 0-1, etc.
    visible_up_to = build_step  # 0, 1, 2, 3
    show_outline = (build_step == 3)  # Only on final build

    slide = prs.slides.add_slide(blank)
    set_slide_bg(slide)
    slide_header(slide, "WHERE AI ADDS VALUE",
                 "12 AI initiatives across four business functions")

    # Subtitle changes on final build
    if show_outline:
        sub = ("Start where domain knowledge is high and outcomes are measurable. "
               "Support is the proving ground for everything that follows.")
    else:
        sub = "AI opportunities exist across every function at SRAM."
    text(slide, Inches(0.8), Inches(1.35), Inches(11), Inches(0.35),
         sub, size=13, color=BODY)

    # Complexity arrow across the top
    arrow_labels = ["Quick Win", "Medium Effort", "Long-Term Bet"]
    for ci, alabel in enumerate(arrow_labels):
        ax = grid_left + Inches(ci * (3.2 + 0.15))
        text(slide, ax, Inches(1.75), card_w, Inches(0.22),
             alabel, size=9, color=GRAY, bold=True, align=PP_ALIGN.CENTER)

    arrow_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                        grid_left, Inches(1.97), Inches(10.05), Pt(2))
    arrow_line.fill.solid()
    arrow_line.fill.fore_color.rgb = BORDER
    arrow_line.line.fill.background()

    arrow_tri = slide.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE,
                                       grid_left + Inches(10.0), Inches(1.91),
                                       Inches(0.15), Inches(0.14))
    arrow_tri.fill.solid()
    arrow_tri.fill.fore_color.rgb = BORDER
    arrow_tri.line.fill.background()
    arrow_tri.rotation = 90.0

    # Draw rows top-down, only show revealed ones
    for ri, (area, items) in enumerate(initiative_rows):
        row_top = Inches(2.1) + Inches(ri * (0.9 + 0.25))
        fc = FUNC_COLORS[area]

        if ri > visible_up_to:
            continue  # Skip rows not yet revealed

        # Row label with colored accent bar
        label_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                           Inches(0.8), row_top, Pt(4), card_h)
        label_bar.fill.solid()
        label_bar.fill.fore_color.rgb = fc
        label_bar.line.fill.background()

        text(slide, Inches(0.95), row_top + Inches(0.25), Inches(1.35), Inches(0.4),
             area, size=9, color=fc, bold=True)

        for ci, (initiative, problem, highlight) in enumerate(items):
            left = grid_left + Inches(ci * (3.2 + 0.15))

            if highlight and show_outline:
                add_rect(slide, left, row_top, card_w, card_h, HIGHLIGHT_BG, RED)
                hbar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                              left, row_top, Pt(4), card_h)
                hbar.fill.solid()
                hbar.fill.fore_color.rgb = RED
                hbar.line.fill.background()
                text(slide, left + Inches(0.2), row_top + Inches(0.08),
                     Inches(2.5), Inches(0.2),
                     "RECOMMENDED PILOT", size=8, color=RED, bold=True)
            else:
                add_rect(slide, left, row_top, card_w, card_h, CARD, BORDER)

            text(slide, left + Inches(0.2), row_top + Inches(0.25),
                 card_w - Inches(0.4), Inches(0.3),
                 initiative, size=12, color=BLACK, bold=True)
            text(slide, left + Inches(0.2), row_top + Inches(0.55),
                 card_w - Inches(0.4), Inches(0.3),
                 problem, size=9, color=GRAY)

    # On final build, add the START HERE outline box around SUPPORT (row 3)
    if show_outline:
        support_row_top = Inches(2.1) + Inches(3 * (0.9 + 0.25))
        support_box = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(0.65), support_row_top - Inches(0.08),
            Inches(11.95), card_h + Inches(0.16))
        support_box.fill.background()
        support_box.line.color.rgb = FUNC_COLORS["SUPPORT"]
        support_box.line.width = Pt(2.5)

        text(slide, Inches(10.7), support_row_top - Inches(0.32),
             Inches(1.8), Inches(0.22),
             "START HERE", size=10, color=FUNC_COLORS["SUPPORT"], bold=True,
             align=PP_ALIGN.RIGHT)

    slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 4: The Problem (progressive build - 2 slides)
# ----------------------------------------------------------
page += 1

# Build 1: Just metrics
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE PROBLEM",
             "Support quality drives churn, not product quality")

text(slide, Inches(0.8), Inches(1.35), Inches(11), Inches(0.35),
     "Riders love SRAM hardware. They struggle with firmware updates, "
     "part compatibility, and warranty resolution.",
     size=13, color=BODY)

metric_card(slide, Inches(0.8), Inches(2.2), Inches(3.6), Inches(1.5),
            "TRUSTPILOT RATING", "1.6 / 5.0", ACCENT_RED_SOFT,
            "Warranty friction and support delays")
metric_card(slide, Inches(4.9), Inches(2.2), Inches(3.6), Inches(1.5),
            "AUTOMATABLE", "~70%", BLACK,
            "Questions follow documented patterns")
metric_card(slide, Inches(9.0), Inches(2.2), Inches(3.6), Inches(1.5),
            "TOP COMPLAINTS", "Firmware + Pairing", ACCENT_RED_SOFT,
            "Reddit, app stores, Trustpilot")

slide_footer(slide, page)

# Build 2: Metrics + quote
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE PROBLEM",
             "Support quality drives churn, not product quality")

text(slide, Inches(0.8), Inches(1.35), Inches(11), Inches(0.35),
     "Riders love SRAM hardware. They struggle with firmware updates, "
     "part compatibility, and warranty resolution.",
     size=13, color=BODY)

metric_card(slide, Inches(0.8), Inches(2.2), Inches(3.6), Inches(1.5),
            "TRUSTPILOT RATING", "1.6 / 5.0", ACCENT_RED_SOFT,
            "Warranty friction and support delays")
metric_card(slide, Inches(4.9), Inches(2.2), Inches(3.6), Inches(1.5),
            "AUTOMATABLE", "~70%", BLACK,
            "Questions follow documented patterns")
metric_card(slide, Inches(9.0), Inches(2.2), Inches(3.6), Inches(1.5),
            "TOP COMPLAINTS", "Firmware + Pairing", ACCENT_RED_SOFT,
            "Reddit, app stores, Trustpilot")

quote_box(slide, Inches(0.8), Inches(4.8), Inches(11.8), Inches(0.85),
          "The first question I ask anyone skeptical about AI is: do you want to spend "
          "your day searching a 200-page compatibility PDF, or do you want to spend it "
          "talking to dealers?",
          "Clint Weber, VP Global Sales & Manufacturing, SRAM")

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 5: The 90-Day Pilot (progressive build - 2 slides)
# ----------------------------------------------------------
page += 1

# --- Pilot slide: before/after showing what actually changes ---

# Build 1: before/after workflow
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE SOLUTION",
             "AI drafts responses, humans approve them, nobody gets a wrong answer")

# TODAY column
today_left = Inches(0.8)
col_w = Inches(5.5)
text(slide, today_left, Inches(1.5), col_w, Inches(0.3),
     "TODAY", size=14, color=ACCENT_RED_SOFT, bold=True)

today_steps = [
    ("1. Dealer emails a question",
     "\"Which AXS derailleur firmware works with my 2024 Eagle cassette?\""),
    ("2. Agent searches manually",
     "Opens a 200-page compatibility PDF.\nSearches across multiple documents and wikis."),
    ("3. Agent writes a response from scratch",
     "Types out the answer, double-checks part numbers,\nhopes nothing changed since last update."),
    ("4. Dealer waits",
     "Average first response: ~4 hours.\n70% of questions follow the same patterns."),
]
for i, (step, detail) in enumerate(today_steps):
    y = Inches(1.9) + Inches(i * 1.15)
    add_rect(slide, today_left, y, col_w, Inches(1.0), CARD, BORDER)
    text(slide, today_left + Inches(0.2), y + Inches(0.08),
         col_w - Inches(0.4), Inches(0.25),
         step, size=12, color=BLACK, bold=True)
    text(slide, today_left + Inches(0.2), y + Inches(0.38),
         col_w - Inches(0.4), Inches(0.55),
         detail, size=10, color=GRAY)

# PILOT column
pilot_left = Inches(6.8)
text(slide, pilot_left, Inches(1.5), col_w, Inches(0.3),
     "WITH AI PILOT", size=14, color=GANTT_ACCENT, bold=True)

pilot_steps = [
    ("1. Same question arrives",
     "Dealer submits via Zendesk. Nothing changes for them."),
    ("2. AI searches approved docs instantly",
     "Amazon Kendra indexes SRAM's compatibility tables,\nfirmware notes, and service bulletins."),
    ("3. AI drafts a response for the agent",
     "Amazon Bedrock generates an answer from the knowledge\nbase. Agent reviews and edits before sending."),
    ("4. Dealer gets a faster, verified answer",
     "Target first response: ~2.5 hours.\nAgent spends time on hard problems, not repetitive ones."),
]
for i, (step, detail) in enumerate(pilot_steps):
    y = Inches(1.9) + Inches(i * 1.15)
    bg = HIGHLIGHT_BG if i == 3 else CARD
    bd = GANTT_ACCENT if i == 3 else BORDER
    add_rect(slide, pilot_left, y, col_w, Inches(1.0), bg, bd)
    text(slide, pilot_left + Inches(0.2), y + Inches(0.08),
         col_w - Inches(0.4), Inches(0.25),
         step, size=12, color=BLACK, bold=True)
    text(slide, pilot_left + Inches(0.2), y + Inches(0.38),
         col_w - Inches(0.4), Inches(0.55),
         detail, size=10, color=GRAY)

# Arrow between columns
arrow_right(slide, Inches(6.35), Inches(3.5), Inches(0.35), Inches(0.35))

slide_footer(slide, page)

# Build 2: add scope constraints + quote
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE SOLUTION",
             "AI drafts responses, humans approve them, nobody gets a wrong answer")

# Scope constraints - 3 cards
scope_items = [
    ("SCOPE", "AXS + Hammerhead only",
     "Products where SRAM's documentation\nis complete and structured."),
    ("GUARDRAIL", "Human approves every response",
     "No AI answer reaches a dealer without\nan agent reviewing and sending it."),
    ("KILL SWITCH", "Weekly quality review",
     "2 weeks of quality decline, any safety\nerror, or 15% dealer opt-out stops the pilot."),
]
for i, (label, title, desc) in enumerate(scope_items):
    left = Inches(0.8) + Inches(i * 4.1)
    cw = Inches(3.85)
    add_rect(slide, left, Inches(1.6), cw, Inches(2.4), CARD, BORDER)
    text(slide, left + Inches(0.2), Inches(1.72), cw - Inches(0.4), Inches(0.2),
         label, size=9, color=GANTT_ACCENT, bold=True)
    text(slide, left + Inches(0.2), Inches(2.0), cw - Inches(0.4), Inches(0.35),
         title, size=16, color=BLACK, bold=True)
    text(slide, left + Inches(0.2), Inches(2.55), cw - Inches(0.4), Inches(0.8),
         desc, size=12, color=BODY)

quote_box(slide, Inches(0.8), Inches(4.6), Inches(11.8), Inches(0.85),
          "If it doesn't hit the metric, you shut it down, you learn from it, and you "
          "redeploy the resources. That discipline is what separates companies that build "
          "real AI capability from companies that accumulate AI debt.",
          "Clint Weber, VP Global Sales & Manufacturing, SRAM")

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 6b: SMART Goals (progressive build - one goal per click)
# ----------------------------------------------------------
page += 1

smart_goals_full = [
    ("G1", "Cut first-response time", "-40%", "Measured weekly vs. SLA baseline"),
    ("G2", "Resolve more tickets without escalation", "+15 pts", "Measured weekly vs. current rate"),
    ("G3", "AI draft acceptance rate", ">70%", "Below 50% at day 45 triggers scope review"),
    ("G4", "Increase agent throughput", "+25%", "Tickets handled per agent per day"),
    ("G5", "Hold customer satisfaction flat", "No decline", "Any sustained drop triggers rollback"),
]

for goals_shown in range(1, 6):  # 1, 2, 3, 4, 5
    slide = prs.slides.add_slide(blank)
    set_slide_bg(slide)
    slide_header(slide, "THE GOALS",
                 "Five SMART goals define pilot success at day 90")

    text(slide, Inches(0.8), Inches(1.35), Inches(11.5), Inches(0.35),
         "Weber set the bar: a 30% reduction in handle time on AXS support tickets "
         "with dealer satisfaction scores holding flat or improving.",
         size=13, color=BODY)

    for i, (gid, title, target, detail) in enumerate(smart_goals_full):
        if i >= goals_shown:
            break
        y = Inches(2.0) + Inches(i * 0.85)
        if i % 2 == 0:
            add_rect(slide, Inches(0.8), y - Inches(0.05), Inches(11.7), Inches(0.75),
                     LIGHT_GRAY_BG, None, 0.02)

        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                       Inches(1.1), y + Inches(0.12),
                                       Inches(0.55), Inches(0.4))
        badge.fill.solid()
        badge.fill.fore_color.rgb = GANTT_ACCENT
        badge.line.fill.background()
        badge.adjustments[0] = 0.15
        tf = badge.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = gid
        p.font.size = Pt(14)
        p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.font.bold = True
        p.alignment = PP_ALIGN.CENTER

        text(slide, Inches(1.9), y + Inches(0.08), Inches(5.5), Inches(0.4),
             title, size=16, color=BLACK, bold=True)
        text(slide, Inches(7.5), y + Inches(0.05), Inches(2.0), Inches(0.45),
             target, size=22, color=RED, bold=True)
        text(slide, Inches(9.5), y + Inches(0.15), Inches(3.0), Inches(0.35),
             detail, size=11, color=GRAY)

    # Show kill criteria only on final build
    if goals_shown == 5:
        text(slide, Inches(0.8), Inches(6.4), Inches(11.7), Inches(0.3),
             "Kill criteria: 2 weeks quality drop, any safety error reaching a dealer, "
             "or dealer opt-out above 15%",
             size=12, color=GRAY, align=PP_ALIGN.CENTER)

    slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 6c: Gantt Chart (progressive build - 3 slides)
# ----------------------------------------------------------
page += 1

# Gantt rows grouped by phase:
# Phase A (setup): rows 0-1
# Phase B (execution): rows 2-7
# Phase C (checkpoints): rows 8-10
gantt_rows = [
    ("Setup + Integration", "", 0, 1, GANTT_LIGHT,
     "Zendesk + Kendra + Bedrock integration; baseline metrics"),
    ("Knowledge Base Indexing", "", 0, 0.7, GANTT_LIGHT,
     "Index AXS + Hammerhead docs in Kendra"),
    ("AI Draft Rollout (AXS)", "G3", 0.7, 1.3, GANTT_ACCENT,
     "AI drafts responses; agents review 100%"),
    ("AI Draft Rollout (Hammerhead)", "G3", 1.2, 1.0, GANTT_ACCENT,
     "Expand to Hammerhead device tickets"),
    ("Response Time Tracking", "G1", 0.5, 2.5, GANTT_ACCENT,
     "Weekly measurement vs. SLA baseline"),
    ("Escalation Rate Tracking", "G2", 0.5, 2.5, GANTT_ACCENT,
     "Weekly measurement vs. baseline"),
    ("Throughput Measurement", "G4", 1.0, 2.0, GANTT_ACCENT,
     "Tickets/agent/day tracked weekly"),
    ("CSAT Monitoring", "G5", 0.5, 2.5, GANTT_ACCENT,
     "No decline for 2 consecutive periods"),
    ("Weekly Quality Reviews", "", 0.5, 2.5, GRAY,
     "Rollback trigger if quality drops 2 weeks"),
    ("Day-45 Checkpoint", "", 1.5, 0.15, RED,
     "Scope review if draft acceptance <50%"),
    ("Day-90 Go/No-Go", "", 2.85, 0.15, RED,
     "Decision: scale, adjust, or stop"),
]

# Build cutoffs: show rows 0..N
gantt_builds = [2, 8, 11]  # setup, +execution, +checkpoints

for build_idx, rows_shown in enumerate(gantt_builds):
    slide = prs.slides.add_slide(blank)
    set_slide_bg(slide)
    slide_header(slide, "THE TIMELINE",
                 "90-day pilot mapped to SMART goals")

    gantt_left = Inches(4.0)
    gantt_width = Inches(8.5)
    month_w = gantt_width / 3

    for mi, mlabel in enumerate(["Month 1", "Month 2", "Month 3"]):
        x = gantt_left + month_w * mi
        text(slide, x, Inches(1.4), month_w, Inches(0.25),
             mlabel, size=10, color=GRAY, bold=True, align=PP_ALIGN.CENTER)

    for di in range(1, 3):
        x = gantt_left + month_w * di
        divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                         x, Inches(1.65), Pt(1), Inches(5.0))
        divider.fill.solid()
        divider.fill.fore_color.rgb = CARD_BORDER
        divider.line.fill.background()

    row_height = Inches(0.38)
    for i, (label, goal_num, start, dur, color, desc) in enumerate(gantt_rows):
        if i >= rows_shown:
            break
        y = Inches(1.7) + row_height * i

        if i % 2 == 0:
            add_rect(slide, Inches(0.8), y, Inches(11.7), row_height,
                     LIGHT_GRAY_BG, None, 0.01)

        text(slide, Inches(0.8), y + Inches(0.05), Inches(2.8), Inches(0.28),
             label, size=9, color=BLACK, bold=True)

        if goal_num:
            text(slide, Inches(3.4), y + Inches(0.05), Inches(0.5), Inches(0.28),
                 goal_num, size=8, color=RED, bold=True)

        bar_x = gantt_left + month_w * start
        bar_w = month_w * dur
        bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                     int(bar_x), y + Inches(0.06),
                                     int(bar_w), Inches(0.24))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()
        bar.adjustments[0] = 0.15

        if dur >= 1.0:
            text(slide, int(bar_x) + Inches(0.1), y + Inches(0.06),
                 int(bar_w) - Inches(0.2), Inches(0.24),
                 desc, size=7,
                 color=RGBColor(0xFF, 0xFF, 0xFF) if color == GANTT_ACCENT else BLACK)

    # Legend only on final build
    if build_idx == len(gantt_builds) - 1:
        text(slide, Inches(0.8), Inches(6.1), Inches(11), Inches(0.25),
             "Day-45 checkpoint: scope review if draft acceptance < 50%  |  "
             "Day-90: go / no-go decision",
             size=9, color=GRAY, align=PP_ALIGN.CENTER)

    slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 8: Metrics + Financials
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE RETURN",
             "$10.2M net value in Year 1 on $2.7M spend")

# LEFT: Scenario range only - clean and spacious
text(slide, Inches(0.8), Inches(1.6), Inches(5.5), Inches(0.3),
     "Scenario Range", size=18, color=BLACK, bold=True)

scenarios = [
    ("Conservative", "$4.5M", "2.8x"),
    ("Expected", "$10.2M", "3.8x"),
    ("Upside", "$22.5M", "6.4x"),
]
for i, (label, value, roi) in enumerate(scenarios):
    y = Inches(2.3) + Inches(i * 0.9)
    if i == 1:  # Highlight expected case
        add_rect(slide, Inches(0.8), y - Inches(0.1), Inches(5.5), Inches(0.8),
                 HIGHLIGHT_BG, RED, 0.02)
    text(slide, Inches(1.0), y, Inches(2.0), Inches(0.5), label, size=14, color=GRAY)
    text(slide, Inches(3.0), y, Inches(1.8), Inches(0.5), value,
         size=24, color=BLACK, bold=True)
    text(slide, Inches(4.8), y + Inches(0.05), Inches(1.2), Inches(0.4),
         roi + " ROI", size=13, color=GRAY)

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

text(slide, Inches(0.8), Inches(6.5), Inches(5.5), Inches(0.25),
     "Estimates based on industry benchmarks, interview data, and SRAM public filings. "
     "Full breakdown in Appendix A1.",
     size=8, color=GRAY)

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE 9: 2031 Vision (progressive build - 2 slides)
# ----------------------------------------------------------
page += 1

visions = [
    ("AXS Intelligence Platform",
     "Unified rider dashboard: power, gearing, suspension, heart rate "
     "in one view. No competitor has the product breadth to build this.",
     "NEW REVENUE: Premium subscription tier"),
    ("Predictive Maintenance",
     "Connected components predict chain and brake pad replacement "
     "before failure. Installed base becomes recurring revenue.",
     "NEW REVENUE: Per-device monitoring subscription"),
    ("AI-Tuned Performance",
     "Suspension auto-adjusts to terrain. Shifting optimizes for rider "
     "power. Products improve continuously after purchase.",
     "NEW REVENUE: Premium optimization tier"),
    ("Dealer Intelligence",
     "Telemetry tells dealers which parts approach end-of-life in their "
     "area. Proactive ordering replaces reactive.",
     "NEW REVENUE: Dealer analytics license"),
]

for build in range(2):
    slide = prs.slides.add_slide(blank)
    set_slide_bg(slide)
    slide_header(slide, "WHAT COULD BE",
                 "Hardware company to performance intelligence by 2031")

    text(slide, Inches(0.8), Inches(1.35), Inches(11.5), Inches(0.35),
         "Each capability creates a new recurring revenue stream. "
         "SRAM's installed base of connected components becomes a platform, not a one-time sale.",
         size=13, color=BODY)

    # AXS Intelligence Platform - always shown
    axs_top = Inches(2.0)
    axs_w = Inches(11.7)
    axs_h = Inches(1.5)
    add_rect(slide, Inches(0.8), axs_top, axs_w, axs_h, HIGHLIGHT_BG, RED)
    hbar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                   Inches(0.8), axs_top, Pt(4), axs_h)
    hbar.fill.solid()
    hbar.fill.fore_color.rgb = RED
    hbar.line.fill.background()
    text(slide, Inches(1.2), axs_top + Inches(0.12), Inches(4.0), Inches(0.2),
         "THE UNLOCK", size=10, color=RED, bold=True)
    text(slide, Inches(1.2), axs_top + Inches(0.4), Inches(5.0), Inches(0.4),
         visions[0][0], size=20, color=BLACK, bold=True)
    text(slide, Inches(1.2), axs_top + Inches(0.9), Inches(10.5), Inches(0.5),
         visions[0][1], size=13, color=BODY)
    text(slide, Inches(8.0), axs_top + Inches(0.4), Inches(4.2), Inches(0.3),
         visions[0][2], size=11, color=RED, bold=True, align=PP_ALIGN.RIGHT)

    # Build 2: add supporting cards + flywheel
    if build == 1:
        for i, (title, desc, rev) in enumerate(visions[1:]):
            left = Inches(0.8) + Inches(i * 4.0)
            top = Inches(4.0)
            vc_w = Inches(3.75)
            vc_h = Inches(1.5)
            add_rect(slide, left, top, vc_w, vc_h, CARD, BORDER)
            text(slide, left + Inches(0.25), top + Inches(0.15),
                 vc_w - Inches(0.5), Inches(0.3),
                 title, size=13, color=BLACK, bold=True)
            text(slide, left + Inches(0.25), top + Inches(0.5),
                 vc_w - Inches(0.5), Inches(0.55),
                 desc, size=11, color=BODY)
            text(slide, left + Inches(0.25), top + Inches(1.15),
                 vc_w - Inches(0.5), Inches(0.25),
                 rev, size=9, color=RED, bold=True)

        # Flywheel
        add_rect(slide, Inches(0.8), Inches(6.0), Inches(11.7), Inches(0.45),
                 CARD, BORDER, 0.1)
        red_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                         Inches(0.8), Inches(6.0), Pt(4), Inches(0.45))
        red_bar.fill.solid()
        red_bar.fill.fore_color.rgb = RED
        red_bar.line.fill.background()
        text(slide, Inches(1.2), Inches(6.04), Inches(11.0), Inches(0.35),
             "Hardware sells data access  \u2192  Data improves performance  "
             "\u2192  Performance sells hardware",
             size=14, color=BLACK, bold=True, align=PP_ALIGN.CENTER)

    slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE: Organizational Enablers
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "WHAT IT TAKES",
             "Talent, data, and leadership required at each phase")

# Three columns: Talent, Data, Leadership
enabler_cols = [
    ("TALENT", [
        ("Phase 1", "1 integration engineer + 1 product owner.\n"
         "No new AI/ML hires. 250-400 existing engineers\n"
         "have capacity with AI-assisted tooling."),
        ("Phase 2+", "Add product managers and QA capacity.\n"
         "The constraint is PM and QA, not developers."),
    ]),
    ("DATA", [
        ("Today", "Good data in pockets, messy data everywhere\n"
         "else. 18 months of consolidation underway.\n"
         "AXS + Hammerhead data is pilot-ready."),
        ("Needed", "Unified data layer linking CRM, inventory,\n"
         "and telemetry. Foundation for Phase 2-4."),
    ]),
    ("LEADERSHIP", [
        ("Phase 1", "CEO assigns one accountable business owner\n"
         "with authority over scope and tooling decisions.\n"
         "Weekly quality reviews."),
        ("Open question", "Weber: 'Somebody at the C-suite level\n"
         "needs to own it. Not as a side responsibility.'\n"
         "Resolving this is a prerequisite for Phase 2."),
    ]),
]

col_w = Inches(3.75)
col_gap = Inches(0.2)
col_start = Inches(0.8)

for ci, (col_title, items) in enumerate(enabler_cols):
    cx = col_start + ci * (col_w + col_gap)

    # Column header
    text(slide, cx, Inches(1.5), col_w, Inches(0.3),
         col_title, size=14, color=BLACK, bold=True)

    for ri, (phase, detail) in enumerate(items):
        ry = Inches(2.0) + Inches(ri * 2.2)
        card_ht = Inches(2.0)
        add_rect(slide, cx, ry, col_w, card_ht, CARD, BORDER)
        text(slide, cx + Inches(0.2), ry + Inches(0.12), col_w - Inches(0.4), Inches(0.25),
             phase.upper(), size=9, color=GRAY, bold=True)
        text(slide, cx + Inches(0.2), ry + Inches(0.4), col_w - Inches(0.4), Inches(1.4),
             detail, size=11, color=BODY)

# Weber readiness quote
quote_box(slide, Inches(0.8), Inches(6.3), Inches(11.7), Inches(0.7),
          "We are 60 to 70 percent of the way to AI-ready data "
          "in the AXS and Hammerhead domain.",
          "Clint Weber, VP Global Sales & Manufacturing, SRAM")

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE: Trade-offs and Risks
# ----------------------------------------------------------
page += 1
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE TRADE-OFFS",
             "Three risks worth naming before the decision")

tradeoffs = [
    ("Dealer trust is fragile",
     "One confident wrong answer from the AI reaches a dealer, and the support "
     "team loses credibility it spent years building. Human-in-the-loop and "
     "weekly quality reviews mitigate this, but they also slow throughput gains.",
     "MITIGATION: Kill criteria trigger rollback at first safety error"),
    ("Data consolidation has no executive sponsor",
     "Weber owns sales and manufacturing but not the CRM, ERP, or inventory systems. "
     "Phase 2 requires a unified data layer across those systems. Without a "
     "senior sponsor, data integration stalls and the pilot stays isolated.",
     "MITIGATION: CEO assigns cross-functional data owner in parallel"),
    ("AI hype creates unrealistic internal expectations",
     "SRAM's engineering culture values precision. If leadership frames AI as a "
     "silver bullet rather than a tool, early imperfections will fuel skepticism "
     "and internal resistance to future phases.",
     "MITIGATION: Frame pilot as experiment with defined success and failure criteria"),
]

for i, (title, desc, mitigation) in enumerate(tradeoffs):
    top = Inches(1.5) + Inches(i * 1.75)
    add_rect(slide, Inches(0.8), top, Inches(11.5), Inches(1.5), CARD, BORDER)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(0.8), top, Pt(4), Inches(1.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_RED_SOFT
    bar.line.fill.background()
    text(slide, Inches(1.2), top + Inches(0.1), Inches(10.5), Inches(0.3),
         title, size=14, color=BLACK, bold=True)
    text(slide, Inches(1.2), top + Inches(0.45), Inches(10.5), Inches(0.6),
         desc, size=11, color=BODY)
    text(slide, Inches(1.2), top + Inches(1.1), Inches(10.5), Inches(0.25),
         mitigation, size=10, color=GRAY, bold=True)

slide_footer(slide, page)


# ----------------------------------------------------------
# SLIDE: The Ask
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
             "Simulated Interview with Clint Weber, VP Global Sales & Manufacturing")

text(slide, Inches(0.8), Inches(1.35), Inches(11), Inches(0.3),
     "AI-simulated interview  |  March 2026  |  Key quotes and insights",
     size=12, color=GRAY)

quotes = [
    ("On data readiness",
     "The areas where we've under-invested in process, data, and cross-functional "
     "integration are exactly the areas where AI could close the gap fastest. "
     "Customer support. Demand forecasting. Compatibility and documentation management.",
     "Validates bounded pilot scope"),
    ("On cultural barriers",
     "We built a Formula 1 car and then had a regional pit crew. The support "
     "infrastructure has lagged behind the hardware. That is a cultural artifact "
     "as much as a resource one.",
     "Human-in-the-loop is mandatory"),
    ("On competitive advantage",
     "Shimano riders use an app to check compatibility. Our riders use an "
     "ecosystem to train, navigate, tune their suspension, and monitor their "
     "entire component stack in real time. That rider does not churn.",
     "Hammerhead is SRAM's real AI moat"),
    ("On implementation discipline",
     "If it doesn't hit the metric, you shut it down, you learn from it, and "
     "you redeploy the resources. That discipline is what separates companies "
     "that build real AI capability from companies that accumulate AI debt.",
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
out_dir = os.path.join(repo_root, "deliverables")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "SRAM_AI_Adoption_Playbook.pptx")
prs.save(out_path)
print(f"Saved presentation to {out_path}")
n_slides = len(prs.slides)
n_appendix = 3
print(f"Slides: {n_slides} ({n_slides - n_appendix} content + {n_appendix} appendix)")
