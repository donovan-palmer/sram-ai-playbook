#!/usr/bin/env python3
"""
Build the SRAM AI Adoption Playbook presentation.

8-minute deck using Duarte's "What Is / What Could Be" contrast pattern
with a T-shaped structure (wide overview -> deep dive on support).

Color scheme derived from sram.com brand palette.

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
TEXT_PRIMARY = RGBColor(0x1C, 0x1C, 0x1E)     # SRAM near-black for headings
TEXT_BODY = RGBColor(0x3A, 0x3A, 0x3C)        # Dark gray for body text
TEXT_SECONDARY = RGBColor(0x76, 0x76, 0x76)   # SRAM mid-gray (#767676)
ACCENT = RGBColor(0x1C, 0x1C, 0x1E)          # Black accent (clean, not red)
ACCENT_RED = RGBColor(0xE5, 0x19, 0x37)      # SRAM red - used sparingly
ACCENT_RED_SOFT = RGBColor(0xC4, 0x3B, 0x4F) # Muted red for emphasis

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


def text(slide, left, top, w, h, content, size=14, color=BODY, bold=False, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(left, top, w, h)
    box.text_frame.word_wrap = True
    p = box.text_frame.paragraphs[0]
    p.text = content
    p.font.size = Pt(size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = "Calibri"
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
        p.font.name = "Calibri"
        p.space_after = Pt(size * (spacing - 1) * 2)
    return box


def slide_header(slide, label, title):
    text(slide, Inches(0.8), Inches(0.3), Inches(6), Inches(0.25),
         label, size=11, color=GRAY, bold=True)
    text(slide, Inches(0.8), Inches(0.6), Inches(11), Inches(0.5),
         title, size=32, color=BLACK, bold=True)
    # Thin red accent line (the only red on most slides)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                  Inches(0.8), Inches(1.15), Inches(0.8), Pt(3))
    line.fill.solid()
    line.fill.fore_color.rgb = RED
    line.line.fill.background()


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


# ============================================================
# BUILD
# ============================================================

prs = Presentation()
prs.slide_width = SLIDE_WIDTH
prs.slide_height = SLIDE_HEIGHT
blank = prs.slide_layouts[6]


# ----------------------------------------------------------
# SLIDE 1: Title
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)

# Thin red accent bar
line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                              Inches(1.5), Inches(2.6), Inches(1.2), Pt(3))
line.fill.solid()
line.fill.fore_color.rgb = RED
line.line.fill.background()

multitext(slide, Inches(1.5), Inches(2.8), Inches(10), Inches(2.5), [
    ("SRAM LLC", 44, BLACK, True),
    ("AI Adoption Playbook", 26, GRAY, False),
    ("", 12, GRAY, False),
    ("Prepared for Executive Leadership", 14, BODY, False),
    ("March 2026", 13, GRAY, False),
])

text(slide, Inches(1.5), Inches(6.3), Inches(10), Inches(0.4),
     "AIML 950  |  Human and Machine Intelligence  |  Northwestern Kellogg",
     size=10, color=GRAY)


# ----------------------------------------------------------
# SLIDE 2: SRAM Today
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "WHAT IS", "SRAM Today")

text(slide, Inches(0.8), Inches(1.4), Inches(11), Inches(0.7),
     "Private, Chicago-founded, $1B+ revenue. The second-largest bicycle component "
     "manufacturer globally. Dominant in mountain bike. Seven brands, three channels, "
     "one connected ecosystem.",
     size=14, color=BODY)

# Metrics row
metrics_data = [
    ("REVENUE", "$1B+", "Private, not disclosed"),
    ("EMPLOYEES", "3,000-5,000", "Global operations"),
    ("BRANDS", "7", "Integrated portfolio"),
    ("MTB POSITION", "#1", "Market leader"),
]
for i, (label, value, sub) in enumerate(metrics_data):
    metric_card(slide, Inches(0.8 + i * 2.85), Inches(2.4), Inches(2.6), Inches(1.3),
                label, value, BLACK, sub)

# Revenue streams (clean two-column list)
text(slide, Inches(0.8), Inches(4.0), Inches(5), Inches(0.35),
     "Revenue Architecture", size=16, color=BLACK, bold=True)

streams = [
    ("Drivetrains + Braking", "SRAM RED, Force, Rival, Eagle"),
    ("Suspension", "RockShox forks and shocks"),
    ("Wheels + Cockpit", "Zipp performance components"),
    ("Connected Products", "Hammerhead Karoo, Quarq power"),
    ("Wear Parts + Service", "Chains, cassettes, pads, rotors"),
    ("Pedals + Adjacent", "TIME, Velocio, Ochain"),
]

for i, (name, desc) in enumerate(streams):
    y = Inches(4.5) + Inches(i * 0.4)
    text(slide, Inches(0.8), y, Inches(3.2), Inches(0.35),
         name, size=12, color=BLACK, bold=True)
    text(slide, Inches(4.2), y, Inches(4.5), Inches(0.35),
         desc, size=11, color=GRAY)

# Competitive context (right side)
add_rect(slide, Inches(9.2), Inches(4.0), Inches(3.5), Inches(3.0), CARD, BORDER)
text(slide, Inches(9.5), Inches(4.15), Inches(3.0), Inches(0.35),
     "Competitive Pressure", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(9.5), Inches(4.6), Inches(3.0), Inches(2.2),
            ["Shimano: wireless gravel (GRX RX827)",
             "Campagnolo: 13-speed premium",
             "microSHIFT: value mechanical"], BODY, 11)


# ----------------------------------------------------------
# SLIDE 3: Initiative Map (NEW - the "vast web of opportunity")
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE OPPORTUNITY", "AI Initiatives Across SRAM")

text(slide, Inches(0.8), Inches(1.4), Inches(11), Inches(0.5),
     "Every function at SRAM has AI potential. The map below shows initiatives by "
     "business area and the specific problem each one solves.",
     size=14, color=BODY)

# Grid of initiative cards: 3 columns x 4 rows
initiatives = [
    ("SUPPORT", "AI Support Agent", "70% of dealer questions are repetitive"),
    ("SUPPORT", "Warranty Automation", "Fraudulent and mis-filed claims cost time"),
    ("SUPPORT", "Compatibility Assistant", "Riders get wrong parts, return them"),
    ("SUPPLY CHAIN", "Demand Forecasting", "No forecasting system exists today"),
    ("SUPPLY CHAIN", "Inventory Allocation", "Stockouts and rush shipping losses"),
    ("SUPPLY CHAIN", "Customer Analytics", "Shopify data is siloed, unused"),
    ("SALES", "OEM Proposal Automation", "Proposal cycles are slow, manual"),
    ("SALES", "Part Recommendations", "No guided upsell at point of service"),
    ("SALES", "DTC Personalization", "Velocio has no targeting capability"),
    ("ENGINEERING", "Generative Design", "Physical testing is slow and expensive"),
    ("ENGINEERING", "AXS Intelligence", "Telemetry data is collected but unused"),
    ("ENGINEERING", "AI-Tuned Components", "Suspension and shifting are static"),
]

for i, (area, initiative, problem) in enumerate(initiatives):
    col = i % 3
    row = i // 3
    left = Inches(0.8) + Inches(col * 4.1)
    top = Inches(2.2) + Inches(row * 1.25)
    card_w = Inches(3.85)
    card_h = Inches(1.05)

    add_rect(slide, left, top, card_w, card_h, CARD, BORDER)
    text(slide, left + Inches(0.2), top + Inches(0.08), Inches(1.5), Inches(0.2),
         area, size=8, color=GRAY, bold=True)
    text(slide, left + Inches(0.2), top + Inches(0.3), card_w - Inches(0.4), Inches(0.3),
         initiative, size=13, color=BLACK, bold=True)
    text(slide, left + Inches(0.2), top + Inches(0.65), card_w - Inches(0.4), Inches(0.35),
         problem, size=10, color=GRAY)

# Bottom callout - subtle with thin red left border effect
add_rect(slide, Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.35), CARD, BORDER, 0.1)
# Tiny red accent on the left edge
red_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(0.8), Inches(7.0), Pt(4), Inches(0.35))
red_bar.fill.solid()
red_bar.fill.fore_color.rgb = RED
red_bar.line.fill.background()
text(slide, Inches(1.2), Inches(7.03), Inches(11.0), Inches(0.3),
     "We focus on the area with the highest uplift and fastest proof: Customer and Dealer Support",
     size=12, color=BLACK, bold=True, align=PP_ALIGN.CENTER)


# ----------------------------------------------------------
# SLIDE 4: The Support Problem (deep dive begins)
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE PROBLEM", "Support Quality Drives Churn, Not Product Quality")

text(slide, Inches(0.8), Inches(1.4), Inches(11), Inches(0.5),
     "Riders love SRAM components but struggle with firmware, compatibility, "
     "and warranty resolution. The data is clear.",
     size=14, color=BODY)

# Three big metrics
metric_card(slide, Inches(0.8), Inches(2.2), Inches(3.6), Inches(1.5),
            "TRUSTPILOT RATING", "1.6 / 5.0", ACCENT_RED_SOFT,
            "Driven by warranty and support friction")

metric_card(slide, Inches(4.7), Inches(2.2), Inches(3.6), Inches(1.5),
            "DEALER QUESTIONS AUTOMATABLE", "~70%", BLACK,
            "Follow repeatable patterns")

metric_card(slide, Inches(8.6), Inches(2.2), Inches(4.0), Inches(1.5),
            "TOP COMPLAINTS", "Firmware + Pairing", ACCENT_RED_SOFT,
            "Reddit 2024-2025: shifting, updates, compatibility")

# Two columns: pain vs. advantage
add_rect(slide, Inches(0.8), Inches(4.1), Inches(5.5), Inches(3.0), CARD, BORDER)
text(slide, Inches(1.1), Inches(4.25), Inches(4.5), Inches(0.35),
     "Customer Pain Signals", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(1.1), Inches(4.7), Inches(4.8), Inches(2.2),
            ["Trustpilot: warranty frustration and support delays",
             "Reddit: pairing issues, firmware failures, shifting anomalies",
             "App stores: AXS and Hammerhead companion complaints",
             "Riders explicitly stating intent to switch to Shimano"],
            BODY, 11)

add_rect(slide, Inches(6.6), Inches(4.1), Inches(6.0), Inches(3.0), CARD, BORDER)
text(slide, Inches(6.9), Inches(4.25), Inches(5.0), Inches(0.35),
     "Why SRAM Has the Data to Fix This", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(6.9), Inches(4.7), Inches(5.4), Inches(2.2),
            ["Structured knowledge base: manuals, compatibility guides, troubleshooting",
             "AXS telemetry: firmware versions, error codes, device state",
             "Hammerhead ride and device data",
             "Compatibility rules already documented and maintained"],
            BODY, 11)


# ----------------------------------------------------------
# SLIDE 5: The 90-Day Pilot
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE SOLUTION", "90-Day Support Pilot")

# Workflow: 5 steps in a clean horizontal flow
steps = [
    ("1", "TICKET IN", "Dealer or rider submits via Zendesk"),
    ("2", "AI RETRIEVES", "Azure AI Search finds approved docs + AXS telemetry"),
    ("3", "AI DRAFTS", "OpenAI generates response from knowledge base only"),
    ("4", "HUMAN REVIEWS", "Agent approves before sending (100% in pilot)"),
    ("5", "QUALITY LOGGED", "Metrics tracked; weekly review with rollback trigger"),
]

for i, (num, title, desc) in enumerate(steps):
    left = Inches(0.8) + Inches(i * 2.45)
    card_w = Inches(2.25)

    add_rect(slide, left, Inches(1.6), card_w, Inches(2.2), CARD, BORDER)

    # Number circle
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.15), Inches(1.75),
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

    text(slide, left + Inches(0.15), Inches(2.2), card_w - Inches(0.3), Inches(0.25),
         title, size=10, color=BLACK, bold=True)
    text(slide, left + Inches(0.15), Inches(2.5), card_w - Inches(0.3), Inches(1.0),
         desc, size=11, color=BODY)

# Scope + Controls (two clean cards)
add_rect(slide, Inches(0.8), Inches(4.15), Inches(5.8), Inches(3.0), CARD, BORDER)
text(slide, Inches(1.1), Inches(4.3), Inches(5.0), Inches(0.35),
     "Pilot Scope", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(1.1), Inches(4.7), Inches(5.2), Inches(2.2),
            ["AXS drivetrain + Hammerhead device support only",
             "Dealer inbox and high-volume web forms",
             "Compatibility and firmware issues first",
             "Human approval on all customer-facing responses"],
            BODY, 11)

add_rect(slide, Inches(6.85), Inches(4.15), Inches(5.8), Inches(3.0), CARD, BORDER)
text(slide, Inches(7.15), Inches(4.3), Inches(5.0), Inches(0.35),
     "Risk Controls", size=14, color=BLACK, bold=True)
bullet_list(slide, Inches(7.15), Inches(4.7), Inches(5.2), Inches(2.2),
            ["Human approval for warranty and safety decisions",
             "Answers sourced from approved docs only",
             "Weekly quality review with rollback trigger",
             "No automated warranty adjudication in Phase 1"],
            BODY, 11)


# ----------------------------------------------------------
# SLIDE 6: Metrics + Financials
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "MEASURING SUCCESS", "Pilot Metrics and Year-1 Financial Impact")

# Left: pilot metrics
text(slide, Inches(0.8), Inches(1.5), Inches(6), Inches(0.35),
     "90-Day Pilot Targets", size=16, color=BLACK, bold=True)

metrics_list = [
    ("Time-to-first-response", "40% reduction"),
    ("Tickets without escalation", "15% improvement"),
    ("Agent productivity", "25% increase"),
    ("AI draft acceptance rate", "Above 70%"),
    ("Customer satisfaction", "No decline"),
]

for i, (met, target) in enumerate(metrics_list):
    y = Inches(2.0) + Inches(i * 0.45)
    text(slide, Inches(0.8), y, Inches(4.0), Inches(0.35), met, size=12, color=BODY)
    text(slide, Inches(5.0), y, Inches(2.0), Inches(0.35), target, size=12, color=BLACK, bold=True)

# Right: financials
text(slide, Inches(7.5), Inches(1.5), Inches(5), Inches(0.35),
     "Year-1 Financial Impact (All Phases)", size=16, color=BLACK, bold=True)

metric_card(slide, Inches(7.5), Inches(2.0), Inches(2.5), Inches(1.3),
            "NET YEAR-1 VALUE", "$10.2M", BLACK, "Expected case")
metric_card(slide, Inches(10.2), Inches(2.0), Inches(2.5), Inches(1.3),
            "RETURN ON SPEND", "3.8x", BLACK, "On $2.7M total spend")

fin_lines = [
    ("Cost Reductions", 13, BLACK, True),
    ("Support automation: $1.6M", 11, BODY, False),
    ("Demand forecasting: $1.6M", 11, BODY, False),
    ("Documentation: $0.24M", 11, BODY, False),
    ("", 6, GRAY, False),
    ("Revenue Growth", 13, BLACK, True),
    ("Customer retention: $3.0M", 11, BODY, False),
    ("Package size increase: $4.0M", 11, BODY, False),
    ("Proposal win rate: $2.5M", 11, BODY, False),
    ("", 6, GRAY, False),
    ("Gross value: $12.9M", 12, BLACK, True),
    ("Total spend: ($2.7M)", 12, GRAY, False),
    ("Net value: $10.2M", 12, BLACK, True),
]
multitext(slide, Inches(7.5), Inches(3.5), Inches(5.0), Inches(3.5), fin_lines, 1.25)


# ----------------------------------------------------------
# SLIDE 7: 2031 Vision
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "2031 VISION", "From Hardware Manufacturer to Performance Intelligence")

text(slide, Inches(0.8), Inches(1.4), Inches(11), Inches(0.5),
     "SRAM's full product stack creates a data moat no competitor can replicate. "
     "The rider with SRAM drivetrain, RockShox suspension, Quarq power, and Hammerhead "
     "computer gets a unified intelligence layer impossible with mixed components.",
     size=14, color=BODY)

visions = [
    ("AXS Intelligence Platform",
     "Unified rider dashboard showing power, gearing, suspension, and heart rate "
     "in one view. No competitor has the product breadth to match this."),
    ("Predictive Maintenance",
     "Connected components predict chain, cassette, and brake pad replacement "
     "before failure. Installed base becomes a recurring revenue platform."),
    ("AI-Tuned Performance",
     "Suspension auto-adjusts to terrain. Shifting optimizes for rider power "
     "patterns. Products improve continuously after purchase."),
    ("Dealer Intelligence",
     "Aggregated telemetry tells dealers which parts approach end-of-life in their "
     "service area. Proactive ordering replaces reactive."),
]

for i, (title, desc) in enumerate(visions):
    col = i % 2
    row = i // 2
    left = Inches(0.8) + Inches(col * 5.9)
    top = Inches(2.2) + Inches(row * 2.1)
    card_w = Inches(5.65)
    card_h = Inches(1.85)

    add_rect(slide, left, top, card_w, card_h, CARD, BORDER)
    text(slide, left + Inches(0.3), top + Inches(0.15), card_w - Inches(0.6), Inches(0.35),
         title, size=15, color=BLACK, bold=True)
    text(slide, left + Inches(0.3), top + Inches(0.55), card_w - Inches(0.6), Inches(1.1),
         desc, size=12, color=BODY)

# Flywheel
add_rect(slide, Inches(0.8), Inches(6.5), Inches(11.7), Inches(0.45), CARD, BORDER, 0.1)
red_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(0.8), Inches(6.5), Pt(4), Inches(0.45))
red_bar.fill.solid()
red_bar.fill.fore_color.rgb = RED
red_bar.line.fill.background()
text(slide, Inches(1.2), Inches(6.55), Inches(11.0), Inches(0.35),
     "Hardware sells data access  \u2192  Data improves performance  \u2192  Performance sells hardware",
     size=13, color=BLACK, bold=True, align=PP_ALIGN.CENTER)


# ----------------------------------------------------------
# SLIDE 8: The Ask
# ----------------------------------------------------------
slide = prs.slides.add_slide(blank)
set_slide_bg(slide)
slide_header(slide, "THE DECISION", "Three Actions for SRAM's CEO")

actions = [
    ("1", "Launch the 90-Day Support Pilot",
     "Scope it to AXS and Hammerhead dealer support. One product owner, "
     "one integration engineer. Human approval on all outputs. Weekly quality reviews."),
    ("2", "Begin Data Infrastructure Planning",
     "Initiate requirements for a unified data layer connecting Shopify, support systems, "
     "and telemetry data. This is the foundation for forecasting and AXS Intelligence."),
    ("3", "Hold Sequencing Discipline",
     "Bounded, well-defined problems first. Broader transformation after measured proof. "
     "The 90-day pilot produces data to justify or redirect every subsequent investment."),
]

for i, (num, title, desc) in enumerate(actions):
    top = Inches(1.5) + Inches(i * 1.6)
    add_rect(slide, Inches(0.8), top, Inches(11.5), Inches(1.35), CARD, BORDER)

    # Number circle
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.2), top + Inches(0.28),
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

    text(slide, Inches(2.0), top + Inches(0.12), Inches(9.8), Inches(0.4),
         title, size=18, color=BLACK, bold=True)
    text(slide, Inches(2.0), top + Inches(0.55), Inches(9.8), Inches(0.65),
         desc, size=12, color=BODY)

# Bottom bar
add_rect(slide, Inches(0.8), Inches(6.45), Inches(11.5), Inches(0.4), CARD, BORDER, 0.1)
red_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,
                                 Inches(0.8), Inches(6.45), Pt(4), Inches(0.4))
red_bar.fill.solid()
red_bar.fill.fore_color.rgb = RED
red_bar.line.fill.background()
text(slide, Inches(1.2), Inches(6.48), Inches(10.8), Inches(0.35),
     "Expected Year-1 return: 3.8x  |  Downside bounded by 90-day pilot  |  "
     "Upside scales with SRAM's unique data advantage",
     size=12, color=BLACK, bold=True, align=PP_ALIGN.CENTER)


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
