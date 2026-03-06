#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analysis-hub.html"


def md_files(root: Path):
    files = [p for p in root.rglob("*.md") if ".git" not in p.parts]
    return sorted(files, key=lambda p: str(p.relative_to(root)).lower())


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:80] or "section"


BADGES = {
    "Confirmed":   ("badge-confirmed",   "✓ Confirmed"),
    "Inference":   ("badge-inference",   "~ Inference"),
    "Speculative": ("badge-speculative", "? Speculative"),
}

def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", lambda m: _badge_or_code(m.group(1)), text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank">\1</a>', text)
    return text

def _badge_or_code(inner: str) -> str:
    if inner in BADGES:
        cls, label = BADGES[inner]
        return f'<span class="badge {cls}">{label}</span>'
    return f"<code>{inner}</code>"


def render_markdown(md: str, prefix: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    in_code = False
    in_ul = False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith("```"):
            close_ul()
            if not in_code:
                in_code = True
                out.append("<pre><code>")
            else:
                in_code = False
                out.append("</code></pre>")
            i += 1
            continue

        if in_code:
            out.append(html.escape(line))
            i += 1
            continue

        if not line.strip():
            close_ul()
            i += 1
            continue

        if line.startswith("|") and i + 1 < len(lines) and lines[i + 1].lstrip().startswith("|---"):
            close_ul()
            headers = [c.strip() for c in line.strip().strip("|").split("|")]
            out.append('<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in headers) + '</tr></thead><tbody>')
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in row) + '</tr>')
                i += 1
            out.append('</tbody></table></div>')
            continue

        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            close_ul()
            level = len(m.group(1))
            text = m.group(2).strip()
            sid = f"{prefix}-{slugify(text)}"
            out.append(f'<h{level} id="{sid}">{inline(text)}</h{level}>')
            i += 1
            continue

        m = re.match(r"^\s*[-*]\s+(.+)$", line)
        if m:
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(m.group(1).strip())}</li>")
            i += 1
            continue

        if line.strip() == "---":
            close_ul()
            out.append("<hr>")
            i += 1
            continue

        close_ul()
        out.append(f"<p>{inline(line.strip())}</p>")
        i += 1

    close_ul()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def file_label(rel: Path) -> str:
    parts = rel.parts
    if len(parts) > 1:
        return f"{parts[0]} / {rel.stem}"
    return rel.stem


def build() -> None:
    files = md_files(ROOT)
    nav_items = []
    sections = []

    for idx, p in enumerate(files, start=1):
        rel = p.relative_to(ROOT)
        section_id = f"doc-{idx}-{slugify(rel.stem)}"
        label = file_label(rel)
        folder = rel.parts[0] if len(rel.parts) > 1 else "root"
        nav_items.append(
            f'<a class="nav-link" href="#{section_id}" data-folder="{html.escape(folder)}">'
            f'<span class="nav-label">{html.escape(label)}</span>'
            f'</a>'
        )
        rendered = render_markdown(p.read_text(encoding="utf-8"), section_id)
        sections.append(
            f'<section class="doc fade-in" id="{section_id}" data-folder="{html.escape(folder)}">'
            f'<div class="doc-header">'
            f'<span class="doc-folder">{html.escape(str(rel.parent) if len(rel.parts) > 1 else "root")}</span>'
            f'<h2 class="doc-title">{html.escape(rel.stem.replace("-", " ").replace("_", " ").title())}</h2>'
            f'</div>'
            f'<div class="doc-body">{rendered}</div>'
            f'</section>'
        )

    page = f"""<!doctype html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SRAM AI Playbook</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;0,14..32,800;0,14..32,900;1,14..32,400&display=swap" rel="stylesheet">
  <style>
    :root {{
      --red: #e10600;
      --red-glow: rgba(225,6,0,0.25);
      --ink: #f1f5f9;
      --ink-2: #94a3b8;
      --ink-3: #64748b;
      --bg: #080b10;
      --panel: #0f1420;
      --panel-2: #141928;
      --border: rgba(255,255,255,0.07);
      --border-hover: rgba(255,255,255,0.13);
      --nav-bg: #070a0f;
      --accent: #60a5fa;
      --code-bg: #0d1117;
      --shadow: 0 4px 32px rgba(0,0,0,0.4);
      --shadow-lg: 0 12px 48px rgba(0,0,0,0.6);
      --shadow-red: 0 0 32px rgba(225,6,0,0.15);
      --transition: 180ms cubic-bezier(0.4,0,0.2,1);
      --radius: 14px;
    }}

    [data-theme="light"] {{
      --ink: #0d1117;
      --ink-2: #374151;
      --ink-3: #6b7280;
      --bg: #f4f6fa;
      --panel: #ffffff;
      --panel-2: #f8fafc;
      --border: #e5e8ee;
      --border-hover: #c8cdd8;
      --nav-bg: #0d1117;
      --code-bg: #f1f3f7;
      --shadow: 0 4px 24px rgba(13,17,23,0.08);
      --shadow-lg: 0 12px 40px rgba(13,17,23,0.14);
      --shadow-red: 0 0 24px rgba(225,6,0,0.08);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}

    body {{
      font-family: "Inter", system-ui, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.6;
      font-size: 15px;
      -webkit-font-smoothing: antialiased;
    }}

    /* ── PROGRESS BAR ── */
    #progress {{
      position: fixed; top: 0; left: 0;
      height: 2px; width: 0%;
      background: linear-gradient(90deg, var(--red), #ff4d4d);
      z-index: 9999;
      transition: width 60ms linear;
      box-shadow: 0 0 12px var(--red-glow);
    }}

    /* ── COMMAND PALETTE ── */
    #cmdOverlay {{
      display: none;
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.7);
      backdrop-filter: blur(6px);
      z-index: 9000;
      align-items: flex-start;
      justify-content: center;
      padding-top: 15vh;
    }}
    #cmdOverlay.open {{ display: flex; }}

    #cmdBox {{
      background: var(--panel);
      border: 1px solid var(--border-hover);
      border-radius: 16px;
      width: 560px;
      max-width: 90vw;
      box-shadow: var(--shadow-lg), 0 0 0 1px rgba(225,6,0,0.1);
      overflow: hidden;
    }}

    #cmdInput {{
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 1px solid var(--border);
      padding: 16px 20px;
      font-size: 16px;
      font-family: inherit;
      color: var(--ink);
      outline: none;
    }}

    #cmdInput::placeholder {{ color: var(--ink-3); }}

    #cmdResults {{
      max-height: 360px;
      overflow-y: auto;
      padding: 6px;
    }}

    .cmd-item {{
      padding: 10px 14px;
      border-radius: 9px;
      cursor: pointer;
      font-size: 13px;
      color: var(--ink-2);
      transition: all var(--transition);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .cmd-item:hover, .cmd-item.selected {{
      background: rgba(225,6,0,0.1);
      color: var(--ink);
    }}

    .cmd-item-icon {{ color: var(--ink-3); font-size: 15px; width: 18px; text-align: center; }}
    .cmd-hint {{ padding: 10px 14px; font-size: 11px; color: var(--ink-3); border-top: 1px solid var(--border); }}

    /* ── LAYOUT ── */
    .layout {{
      display: grid;
      grid-template-columns: 260px 1fr;
      min-height: 100vh;
    }}

    /* ── SIDEBAR ── */
    nav {{
      position: sticky; top: 0; height: 100vh;
      overflow-y: auto;
      background: var(--nav-bg);
      display: flex; flex-direction: column;
      border-right: 1px solid rgba(225,6,0,0.2);
    }}

    nav::-webkit-scrollbar {{ width: 3px; }}
    nav::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,0.08); border-radius: 2px; }}

    .nav-top {{
      padding: 22px 16px 16px;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }}

    .nav-logo {{
      display: flex; align-items: center; gap: 8px; margin-bottom: 10px;
    }}

    .nav-logo-mark {{
      width: 28px; height: 28px;
      background: var(--red);
      border-radius: 7px;
      display: flex; align-items: center; justify-content: center;
      font-weight: 900; font-size: 13px; color: #fff; letter-spacing: -0.5px;
    }}

    .nav-brand {{
      font-size: 15px; font-weight: 700; color: #fff; letter-spacing: -0.3px;
    }}

    .nav-sub {{
      font-size: 10.5px; color: #4b5563; margin-bottom: 12px; line-height: 1.4;
    }}

    .cmd-trigger {{
      width: 100%;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 8px;
      padding: 7px 10px;
      font-size: 12px;
      color: #64748b;
      font-family: inherit;
      cursor: pointer;
      text-align: left;
      display: flex; align-items: center; justify-content: space-between;
      transition: all var(--transition);
    }}
    .cmd-trigger:hover {{ border-color: rgba(255,255,255,0.15); color: #94a3b8; }}
    .cmd-trigger kbd {{
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 4px; padding: 1px 6px; font-size: 10px;
    }}

    .nav-links {{
      flex: 1; padding: 8px 8px 16px;
      display: flex; flex-direction: column; gap: 1px;
    }}

    .nav-section {{
      font-size: 9.5px; font-weight: 700;
      letter-spacing: 1px; text-transform: uppercase;
      color: #374151; padding: 10px 8px 3px;
    }}

    .nav-link {{
      display: flex; align-items: center; gap: 8px;
      text-decoration: none;
      color: #6b7280; font-size: 12.5px;
      padding: 6px 8px; border-radius: 7px;
      border: 1px solid transparent;
      transition: all var(--transition);
    }}

    .nav-link:hover {{ background: rgba(255,255,255,0.05); color: #d1d5db; }}

    .nav-link.active {{
      background: rgba(225,6,0,0.12);
      border-color: rgba(225,6,0,0.25);
      color: #fff;
    }}

    .nav-link.active::before {{
      content: ""; width: 3px; height: 14px;
      background: var(--red); border-radius: 2px; flex-shrink: 0;
    }}

    .nav-bottom {{
      padding: 12px 10px;
      border-top: 1px solid rgba(255,255,255,0.05);
      display: flex; gap: 6px;
    }}

    .nav-btn {{
      flex: 1;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.07);
      color: #6b7280; border-radius: 7px;
      padding: 6px 4px; font-size: 10.5px;
      font-family: inherit; cursor: pointer;
      transition: all var(--transition); text-align: center;
    }}
    .nav-btn:hover {{ background: rgba(255,255,255,0.1); color: #d1d5db; }}

    /* ── MAIN ── */
    main {{ padding: 28px 36px 72px; max-width: 960px; }}

    /* ── HERO ── */
    .hero {{
      position: relative; overflow: hidden;
      background: linear-gradient(135deg, var(--panel) 0%, var(--panel-2) 100%);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 30px 32px;
      margin-bottom: 18px;
      box-shadow: var(--shadow), var(--shadow-red);
    }}

    .hero-glow {{
      position: absolute; top: -60px; right: -60px;
      width: 280px; height: 280px;
      background: radial-gradient(circle, rgba(225,6,0,0.12) 0%, transparent 70%);
      pointer-events: none;
    }}

    .hero-stripe {{
      position: absolute; top: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, transparent, var(--red), #ff6b35, var(--red), transparent);
      background-size: 300% 100%;
      animation: shimmer 4s infinite linear;
    }}

    @keyframes shimmer {{
      0% {{ background-position: 200% 0; }}
      100% {{ background-position: -200% 0; }}
    }}

    .hero-eyebrow {{
      font-size: 10.5px; font-weight: 700;
      letter-spacing: 1.2px; text-transform: uppercase;
      color: var(--red); margin-bottom: 6px;
    }}

    .hero h1 {{
      font-size: 28px; font-weight: 900;
      letter-spacing: -0.8px;
      background: linear-gradient(135deg, var(--ink) 0%, var(--ink-2) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 4px;
    }}

    .hero-sub {{ font-size: 13px; color: var(--ink-3); }}

    .hero-row {{
      display: flex; align-items: flex-start;
      justify-content: space-between; gap: 20px; flex-wrap: wrap;
    }}

    .hero-actions {{ display: flex; gap: 8px; flex-shrink: 0; margin-top: 6px; }}

    .btn {{
      display: inline-flex; align-items: center; gap: 6px;
      padding: 9px 18px; border-radius: 10px;
      font-size: 13px; font-weight: 600;
      font-family: inherit; cursor: pointer; border: none;
      transition: all var(--transition); text-decoration: none;
      letter-spacing: -0.1px;
    }}

    .btn-primary {{
      background: var(--red);
      color: #fff;
      box-shadow: 0 4px 16px rgba(225,6,0,0.35);
    }}
    .btn-primary:hover {{ transform: translateY(-1px); box-shadow: 0 6px 24px rgba(225,6,0,0.45); }}

    .btn-ghost-light {{
      background: rgba(255,255,255,0.07);
      color: var(--ink-2);
      border: 1px solid var(--border);
    }}
    [data-theme="light"] .btn-ghost-light {{
      background: var(--panel-2); border-color: var(--border);
    }}
    .btn-ghost-light:hover {{ background: rgba(255,255,255,0.12); color: var(--ink); transform: translateY(-1px); }}

    /* ── METRICS ── */
    .metrics {{
      display: grid; grid-template-columns: repeat(4, 1fr);
      gap: 12px; margin-bottom: 18px;
    }}

    .metric {{
      position: relative; overflow: hidden;
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 18px 20px;
      box-shadow: var(--shadow);
      transition: transform var(--transition), box-shadow var(--transition), border-color var(--transition);
      cursor: default;
    }}

    .metric::after {{
      content: "";
      position: absolute; inset: 0;
      border-radius: 14px;
      background: radial-gradient(circle at 80% 20%, rgba(225,6,0,0.06), transparent 60%);
      pointer-events: none;
    }}

    .metric:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-lg);
      border-color: rgba(225,6,0,0.2);
    }}

    .metric-value {{
      font-size: 26px; font-weight: 900;
      letter-spacing: -1px; color: var(--red);
      font-variant-numeric: tabular-nums;
    }}

    .metric-label {{
      font-size: 10.5px; font-weight: 600;
      color: var(--ink-3); text-transform: uppercase;
      letter-spacing: 0.6px; margin-top: 3px;
    }}

    .metric-sub {{ font-size: 11.5px; color: var(--ink-3); margin-top: 1px; }}

    /* ── FILTERS ── */
    .filters {{
      display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 18px;
    }}

    .chip {{
      padding: 5px 14px; border-radius: 999px;
      font-size: 12px; font-weight: 500;
      border: 1px solid var(--border);
      background: var(--panel); color: var(--ink-3);
      cursor: pointer; transition: all var(--transition);
    }}

    .chip:hover {{ border-color: var(--border-hover); color: var(--ink); }}

    .chip.active {{
      background: var(--red); color: #fff;
      border-color: var(--red);
      box-shadow: 0 2px 12px rgba(225,6,0,0.3);
    }}

    /* ── DOC CARDS ── */
    .doc {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      margin-bottom: 12px;
      box-shadow: var(--shadow);
      overflow: hidden;
      transition: box-shadow var(--transition), border-color var(--transition), transform var(--transition);
    }}

    .doc:hover {{
      box-shadow: var(--shadow-lg);
      border-color: var(--border-hover);
    }}

    .doc.hidden {{ display: none; }}

    .doc-header {{
      padding: 15px 20px;
      border-bottom: 1px solid var(--border);
      display: flex; align-items: center; gap: 10px;
      cursor: pointer; user-select: none;
      transition: background var(--transition);
    }}

    .doc-header:hover {{ background: rgba(255,255,255,0.02); }}
    [data-theme="light"] .doc-header:hover {{ background: rgba(0,0,0,0.015); }}

    .doc-folder {{
      font-size: 9.5px; font-weight: 700;
      letter-spacing: 0.7px; text-transform: uppercase;
      color: var(--ink-3);
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border);
      padding: 2px 8px; border-radius: 999px; flex-shrink: 0;
    }}

    [data-theme="light"] .doc-folder {{ background: var(--bg); }}

    .doc-title {{
      font-size: 15px; font-weight: 700;
      color: var(--ink); flex: 1;
      transition: color var(--transition);
    }}

    .doc-header:hover .doc-title {{ color: var(--red); }}

    .doc-toggle {{
      color: var(--ink-3); font-size: 16px;
      transition: transform var(--transition); flex-shrink: 0;
    }}

    .doc.collapsed .doc-toggle {{ transform: rotate(-90deg); }}
    .doc.collapsed .doc-body {{ display: none; }}

    .doc-body {{ padding: 20px 22px 22px; }}

    /* ── TYPOGRAPHY ── */
    .doc-body h1 {{ font-size: 19px; font-weight: 800; margin: 18px 0 8px; color: var(--ink); letter-spacing: -0.3px; }}
    .doc-body h2 {{
      font-size: 15px; font-weight: 700; margin: 18px 0 8px;
      color: var(--ink); padding-left: 12px;
      border-left: 2px solid var(--red);
    }}
    .doc-body h3 {{ font-size: 13.5px; font-weight: 600; margin: 14px 0 5px; color: var(--ink-2); }}
    .doc-body h4 {{ font-size: 12.5px; font-weight: 600; margin: 10px 0 4px; color: var(--ink-3); }}
    .doc-body p {{ margin: 7px 0; font-size: 13.5px; color: var(--ink-2); line-height: 1.75; }}
    .doc-body ul {{ margin: 6px 0 10px 16px; }}
    .doc-body li {{ margin: 4px 0; font-size: 13.5px; color: var(--ink-2); line-height: 1.65; }}
    .doc-body hr {{ border: none; border-top: 1px solid var(--border); margin: 16px 0; }}
    .doc-body strong {{ color: var(--ink); font-weight: 600; }}
    .doc-body a {{ color: var(--accent); text-decoration: none; }}
    .doc-body a:hover {{ text-decoration: underline; }}
    .doc-body em {{ color: var(--ink-3); font-style: italic; }}

    .doc-body code {{
      background: var(--code-bg);
      padding: 2px 6px; border-radius: 5px;
      font-family: ui-monospace, "SF Mono", Menlo, monospace;
      font-size: 11.5px; color: #f97316;
      border: 1px solid var(--border);
    }}

    .doc-body pre {{
      background: #060a0f;
      color: #e2e8f0; padding: 14px 16px;
      border-radius: 10px; overflow: auto; margin: 10px 0;
      font-size: 12.5px; cursor: pointer;
      border: 1px solid rgba(255,255,255,0.05);
      position: relative;
    }}

    .doc-body pre::after {{
      content: "click to copy";
      position: absolute; top: 8px; right: 10px;
      font-size: 10px; color: #4b5563; font-family: inherit;
    }}

    .doc-body pre:hover::after {{ color: #9ca3af; }}
    .doc-body pre code {{ background: transparent; padding: 0; color: inherit; border: none; font-size: inherit; }}

    /* ── CONFIDENCE BADGES ── */
    .badge {{
      display: inline-flex; align-items: center; gap: 3px;
      padding: 1px 8px; border-radius: 999px;
      font-size: 11px; font-weight: 600; font-family: inherit;
      vertical-align: middle; margin: 0 1px;
      letter-spacing: 0.2px;
    }}

    .badge-confirmed {{
      background: rgba(16,185,129,0.12);
      color: #10b981;
      border: 1px solid rgba(16,185,129,0.25);
    }}

    .badge-inference {{
      background: rgba(96,165,250,0.12);
      color: #60a5fa;
      border: 1px solid rgba(96,165,250,0.25);
    }}

    .badge-speculative {{
      background: rgba(251,146,60,0.12);
      color: #fb923c;
      border: 1px solid rgba(251,146,60,0.25);
    }}

    /* ── TABLES ── */
    .table-wrap {{
      overflow-x: auto; margin: 10px 0 14px;
      border-radius: 10px; border: 1px solid var(--border);
    }}

    .doc-body table {{ width: 100%; border-collapse: collapse; font-size: 12.5px; min-width: 480px; }}

    .doc-body th, .doc-body td {{
      padding: 9px 12px; text-align: left;
      vertical-align: top; border-bottom: 1px solid var(--border);
    }}

    .doc-body th {{
      background: rgba(255,255,255,0.03);
      font-weight: 600; font-size: 11px;
      color: var(--ink-3); text-transform: uppercase; letter-spacing: 0.5px;
    }}

    [data-theme="light"] .doc-body th {{ background: var(--bg); }}

    .doc-body tr:last-child td {{ border-bottom: none; }}
    .doc-body tr:hover td {{ background: rgba(255,255,255,0.02); }}
    [data-theme="light"] .doc-body tr:hover td {{ background: rgba(0,0,0,0.015); }}

    /* ── ANIMATIONS ── */
    .fade-in {{
      opacity: 0; transform: translateY(18px);
      transition: opacity 450ms ease, transform 450ms ease;
    }}
    .fade-in.visible {{ opacity: 1; transform: none; }}

    /* ── TOAST ── */
    .toast {{
      position: fixed; bottom: 22px; right: 22px;
      background: var(--panel); color: var(--ink);
      padding: 10px 18px; border-radius: 10px;
      font-size: 13px; font-weight: 500;
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--border);
      opacity: 0; transform: translateY(8px);
      transition: all 260ms ease; pointer-events: none; z-index: 9998;
    }}
    .toast.show {{ opacity: 1; transform: none; }}

    /* ── RESPONSIVE ── */
    @media (max-width: 860px) {{
      .layout {{ grid-template-columns: 1fr; }}
      nav {{ position: relative; height: auto; }}
      main {{ padding: 16px 16px 48px; }}
      .metrics {{ grid-template-columns: repeat(2, 1fr); }}
      #cmdBox {{ width: 92vw; }}
    }}

    /* ── PRINT ── */
    @media print {{
      @page {{ size: Letter portrait; margin: 0.5in; }}
      body {{ background: #fff; color: #000; -webkit-print-color-adjust: exact; }}
      #progress, #cmdOverlay, nav, .hero-actions, .filters,
      .doc-toggle, .toast {{ display: none !important; }}
      .layout {{ grid-template-columns: 1fr; }}
      main {{ padding: 0; max-width: 100%; }}
      .doc {{ border: 1px solid #ddd; box-shadow: none; page-break-inside: avoid; margin-bottom: 14px; }}
      .doc.collapsed .doc-body {{ display: block !important; }}
      .hero {{ border: 1px solid #ddd; box-shadow: none; }}
      .hero h1 {{ -webkit-text-fill-color: #000; }}
      .metrics {{ gap: 10px; }}
      .metric {{ border: 1px solid #ddd; box-shadow: none; }}
    }}
  </style>
</head>
<body>
  <div id="progress"></div>
  <div class="toast" id="toast"></div>

  <!-- COMMAND PALETTE -->
  <div id="cmdOverlay" onclick="closeCmd(event)">
    <div id="cmdBox">
      <input id="cmdInput" placeholder="Search documents and sections..." autocomplete="off" />
      <div id="cmdResults"></div>
      <div class="cmd-hint">&#8593;&#8595; navigate &nbsp;&nbsp; Enter jump &nbsp;&nbsp; Esc close</div>
    </div>
  </div>

  <div class="layout">
    <!-- SIDEBAR -->
    <nav>
      <div class="nav-top">
        <div class="nav-logo">
          <div class="nav-logo-mark">S</div>
          <div class="nav-brand">SRAM AI Playbook</div>
        </div>
        <div class="nav-sub">Kellogg AIML/MORS 950 &mdash; Winter 2026</div>
        <button class="cmd-trigger" onclick="openCmd()">
          <span>&#128269; Search...</span>
          <kbd>&#8984;K</kbd>
        </button>
      </div>

      <div class="nav-links" id="navLinks">
        {''.join(nav_items)}
      </div>

      <div class="nav-bottom">
        <button class="nav-btn" onclick="toggleTheme()">&#9680; Theme</button>
        <button class="nav-btn" onclick="expandAll()">&#9633; Expand</button>
        <button class="nav-btn" onclick="window.print()">&#8599; Print</button>
      </div>
    </nav>

    <!-- MAIN -->
    <main>
      <div class="hero">
        <div class="hero-glow"></div>
        <div class="hero-stripe"></div>
        <div class="hero-row">
          <div>
            <div class="hero-eyebrow">AI Adoption Playbook &mdash; SRAM LLC</div>
            <h1>Executive Analysis Workspace</h1>
            <p class="hero-sub">{len(files)} documents &mdash; Competitive intelligence, revenue architecture, AI strategy</p>
          </div>
          <div class="hero-actions">
            <a class="btn btn-ghost-light" href="interview/interview.html">Interview &rarr;</a>
            <button class="btn btn-primary" onclick="window.print()">Export PDF</button>
          </div>
        </div>
      </div>

      <div class="metrics">
        <div class="metric">
          <div class="metric-value" data-count="10.2" data-prefix="$" data-suffix="M">$10.2M</div>
          <div class="metric-label">Year-1 Net Value</div>
          <div class="metric-sub">Expected case</div>
        </div>
        <div class="metric">
          <div class="metric-value" data-count="3.8" data-suffix="x">3.8x</div>
          <div class="metric-label">Return on Spend</div>
          <div class="metric-sub">Year 1</div>
        </div>
        <div class="metric">
          <div class="metric-value">90d</div>
          <div class="metric-label">Pilot Timeline</div>
          <div class="metric-sub">AXS + Hammerhead first</div>
        </div>
        <div class="metric">
          <div class="metric-value" data-count="{len(files)}">{len(files)}</div>
          <div class="metric-label">Documents</div>
          <div class="metric-sub">Analysis files</div>
        </div>
      </div>

      <div class="filters">
        <button class="chip active" data-filter="all" onclick="filterDocs('all',this)">All</button>
        <button class="chip" data-filter="root" onclick="filterDocs('root',this)">Overview</button>
        <button class="chip" data-filter="ai adoption" onclick="filterDocs('ai adoption',this)">AI Adoption</button>
        <button class="chip" data-filter="competitors" onclick="filterDocs('competitors',this)">Competitors</button>
        <button class="chip" data-filter="revenue" onclick="filterDocs('revenue',this)">Revenue</button>
        <button class="chip" data-filter="interview" onclick="filterDocs('interview',this)">Interview</button>
      </div>

      <div id="docs">{''.join(sections)}</div>

      <p style="text-align:center;font-size:11px;color:var(--ink-3);margin-top:40px;opacity:0.5;">
        {len(files)} markdown files &mdash; rebuild: <code>python3 tools/build_analysis_hub.py</code>
      </p>
    </main>
  </div>

  <script>
    // ── THEME ──
    const saved = localStorage.getItem('sram-theme');
    if (saved) document.documentElement.dataset.theme = saved;

    function toggleTheme() {{
      const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      localStorage.setItem('sram-theme', next);
    }}

    // ── PROGRESS ──
    const bar = document.getElementById('progress');
    window.addEventListener('scroll', () => {{
      const pct = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight) * 100;
      bar.style.width = Math.min(pct, 100) + '%';
    }}, {{passive:true}});

    // ── METRIC COUNTERS ──
    const metricEls = document.querySelectorAll('[data-count]');
    const mObs = new IntersectionObserver(entries => {{
      entries.forEach(e => {{
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = parseFloat(el.dataset.count);
        const prefix = el.dataset.prefix || '';
        const suffix = el.dataset.suffix || '';
        const isDecimal = target % 1 !== 0;
        let start = null;
        const duration = 900;
        function step(ts) {{
          if (!start) start = ts;
          const p = Math.min((ts - start) / duration, 1);
          const ease = 1 - Math.pow(1 - p, 3);
          const val = target * ease;
          el.textContent = prefix + (isDecimal ? val.toFixed(1) : Math.round(val)) + suffix;
          if (p < 1) requestAnimationFrame(step);
        }}
        requestAnimationFrame(step);
        mObs.unobserve(el);
      }});
    }}, {{threshold: 0.5}});
    metricEls.forEach(el => mObs.observe(el));

    // ── FADE IN ──
    const fadeObs = new IntersectionObserver(entries => {{
      entries.forEach((e, i) => {{
        if (e.isIntersecting) {{
          setTimeout(() => e.target.classList.add('visible'), i * 40);
        }}
      }});
    }}, {{threshold: 0.04}});
    document.querySelectorAll('.fade-in').forEach(el => fadeObs.observe(el));

    // ── ACTIVE NAV ──
    const navLinks = document.querySelectorAll('.nav-link');
    const navObs = new IntersectionObserver(entries => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{
          navLinks.forEach(l => l.classList.remove('active'));
          const a = document.querySelector(`.nav-link[href="#${{e.target.id}}"]`);
          if (a) {{ a.classList.add('active'); a.scrollIntoView({{block:'nearest'}}); }}
        }}
      }});
    }}, {{rootMargin: '-15% 0px -75% 0px'}});
    document.querySelectorAll('section.doc').forEach(s => navObs.observe(s));

    // ── COLLAPSE ──
    document.querySelectorAll('.doc-header').forEach(h => {{
      h.addEventListener('click', () => h.closest('.doc').classList.toggle('collapsed'));
    }});
    function expandAll() {{
      document.querySelectorAll('.doc').forEach(d => d.classList.remove('collapsed'));
    }}

    // ── FILTER ──
    function filterDocs(filter, btn) {{
      document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('section.doc').forEach(doc => {{
        doc.classList.toggle('hidden', filter !== 'all' && doc.dataset.folder !== filter);
      }});
      navLinks.forEach(l => {{
        l.style.display = (filter === 'all' || l.dataset.folder === filter) ? '' : 'none';
      }});
    }}

    // ── COMMAND PALETTE ──
    const allDocs = Array.from(document.querySelectorAll('section.doc')).map(s => ({{
      id: s.id,
      title: s.querySelector('.doc-title')?.textContent || s.id,
      folder: s.dataset.folder
    }}));

    function openCmd() {{
      document.getElementById('cmdOverlay').classList.add('open');
      document.getElementById('cmdInput').value = '';
      renderCmd('');
      setTimeout(() => document.getElementById('cmdInput').focus(), 50);
    }}

    function closeCmd(e) {{
      if (e.target === document.getElementById('cmdOverlay') || e.type === 'keydown') {{
        document.getElementById('cmdOverlay').classList.remove('open');
      }}
    }}

    let selectedIdx = 0;

    function renderCmd(q) {{
      const results = q
        ? allDocs.filter(d => d.title.toLowerCase().includes(q.toLowerCase()) || d.folder.toLowerCase().includes(q.toLowerCase()))
        : allDocs;
      selectedIdx = 0;
      const container = document.getElementById('cmdResults');
      container.innerHTML = results.slice(0, 8).map((d, i) =>
        `<div class="cmd-item ${{i===0?'selected':''}}" data-id="${{d.id}}" onclick="jumpTo('${{d.id}}')">
          <span class="cmd-item-icon">&#9643;</span>
          <span>${{d.title}}</span>
          <span style="margin-left:auto;font-size:10px;color:var(--ink-3)">${{d.folder}}</span>
        </div>`
      ).join('') || '<div class="cmd-item" style="opacity:0.5">No results</div>';
    }}

    function jumpTo(id) {{
      document.getElementById('cmdOverlay').classList.remove('open');
      const el = document.getElementById(id);
      if (el) {{ el.classList.remove('collapsed'); el.scrollIntoView({{behavior:'smooth', block:'start'}}); }}
    }}

    document.getElementById('cmdInput').addEventListener('input', e => renderCmd(e.target.value));

    document.getElementById('cmdInput').addEventListener('keydown', e => {{
      const items = document.querySelectorAll('.cmd-item[data-id]');
      if (e.key === 'ArrowDown') {{
        e.preventDefault();
        selectedIdx = Math.min(selectedIdx + 1, items.length - 1);
        items.forEach((it, i) => it.classList.toggle('selected', i === selectedIdx));
      }} else if (e.key === 'ArrowUp') {{
        e.preventDefault();
        selectedIdx = Math.max(selectedIdx - 1, 0);
        items.forEach((it, i) => it.classList.toggle('selected', i === selectedIdx));
      }} else if (e.key === 'Enter') {{
        const sel = document.querySelector('.cmd-item.selected[data-id]');
        if (sel) jumpTo(sel.dataset.id);
      }} else if (e.key === 'Escape') {{
        document.getElementById('cmdOverlay').classList.remove('open');
      }}
    }});

    document.addEventListener('keydown', e => {{
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {{ e.preventDefault(); openCmd(); }}
      if (e.key === 'Escape') document.getElementById('cmdOverlay').classList.remove('open');
    }});

    // ── TOAST ──
    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.classList.add('show');
      setTimeout(() => t.classList.remove('show'), 2000);
    }}

    // ── COPY CODE ──
    document.querySelectorAll('pre').forEach(pre => {{
      pre.addEventListener('click', () => {{
        navigator.clipboard.writeText(pre.textContent.replace('click to copy','').trim())
          .then(() => showToast('Copied'));
      }});
    }});
  </script>
</body>
</html>
"""

    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"Included {len(files)} markdown files")


if __name__ == "__main__":
    build()
