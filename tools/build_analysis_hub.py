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


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


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
            out.append(
                '<table><thead><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in headers) + '</tr></thead><tbody>'
            )
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in row) + '</tr>')
                i += 1
            out.append('</tbody></table>')
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

        close_ul()
        out.append(f"<p>{inline(line.strip())}</p>")
        i += 1

    close_ul()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def build() -> None:
    files = md_files(ROOT)
    nav_items = []
    sections = []

    for idx, p in enumerate(files, start=1):
        rel = p.relative_to(ROOT)
        section_id = f"doc-{idx}-{slugify(rel.stem)}"
        nav_items.append(f'<li><a href="#{section_id}">{html.escape(str(rel))}</a></li>')
        rendered = render_markdown(p.read_text(encoding="utf-8"), section_id)
        sections.append(
            f'<section class="doc" id="{section_id}">'
            f'<h2 class="doc-title">{html.escape(str(rel))}</h2>'
            f'{rendered}'
            f'</section>'
        )

    page = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>SRAM Analysis Hub</title>
  <style>
    :root {{
      --sram-red: #e10600;
      --ink: #101114;
      --ink-soft: #4b5563;
      --line: #d8dde5;
      --bg: #f3f5f8;
      --panel: #ffffff;
      --charcoal: #111318;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      font-family: "Avenir Next", "Segoe UI", Arial, sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 7% -6%, rgba(225, 6, 0, 0.13), transparent 44%),
        radial-gradient(circle at 100% 0, rgba(16, 24, 40, 0.18), transparent 35%),
        var(--bg);
      line-height: 1.5;
    }}

    .layout {{
      display: grid;
      grid-template-columns: 300px 1fr;
      min-height: 100vh;
    }}

    nav {{
      position: sticky;
      top: 0;
      height: 100vh;
      overflow: auto;
      padding: 22px 16px;
      background: linear-gradient(180deg, #0f1116 0%, #141925 100%);
      color: #f3f4f6;
      border-right: 2px solid rgba(225, 6, 0, 0.55);
    }}

    .brand {{
      margin: 0 0 4px;
      font-size: 22px;
      letter-spacing: 0.2px;
      font-weight: 800;
      color: #fff;
    }}

    .sub {{
      margin: 0 0 14px;
      font-size: 12px;
      color: #c9d2df;
    }}

    .count-pill {{
      display: inline-block;
      font-size: 11px;
      color: #fff;
      background: rgba(225, 6, 0, 0.9);
      border-radius: 999px;
      padding: 4px 8px;
      margin-bottom: 12px;
      font-weight: 700;
      letter-spacing: 0.3px;
    }}

    nav ul {{ margin: 0; padding: 0; list-style: none; }}
    nav li {{ margin: 0 0 8px; }}

    nav a {{
      display: block;
      text-decoration: none;
      color: #d8e1ef;
      font-size: 13px;
      line-height: 1.35;
      padding: 8px 9px;
      border-radius: 8px;
      border: 1px solid transparent;
      transition: 140ms ease;
    }}

    nav a:hover {{
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(255, 255, 255, 0.18);
      color: #fff;
    }}

    main {{ padding: 18px 22px 28px; }}

    .hero {{
      background: linear-gradient(120deg, #fff 0%, #f8fafc 100%);
      border: 1px solid var(--line);
      border-left: 5px solid var(--sram-red);
      border-radius: 12px;
      padding: 14px 14px 12px;
      margin-bottom: 12px;
    }}

    .hero h1 {{ margin: 0 0 4px; font-size: 24px; }}
    .hero p {{ margin: 0; font-size: 13px; color: var(--ink-soft); }}

    .toolbar {{ display: flex; gap: 8px; justify-content: flex-end; margin: 0 0 10px; }}

    button {{
      border: 1px solid #232937;
      background: #1b2130;
      color: #fff;
      border-radius: 999px;
      padding: 8px 12px;
      font-size: 12px;
      cursor: pointer;
    }}

    .secondary {{ background: #fff; color: #1b2130; }}

    .doc {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 16px 17px;
      margin-bottom: 14px;
      box-shadow: 0 6px 16px rgba(15, 23, 42, 0.04);
    }}

    .doc-title {{
      margin: 0 0 12px;
      font-size: 17px;
      border-bottom: 1px solid var(--line);
      padding-bottom: 6px;
    }}

    h1, h2, h3, h4, h5, h6 {{ margin: 12px 0 6px; color: #101114; line-height: 1.3; }}
    p {{ margin: 6px 0; font-size: 14px; }}
    ul {{ margin: 6px 0 8px 20px; padding: 0; }}
    li {{ margin: 4px 0; font-size: 14px; }}

    code {{
      background: #f3f4f6;
      padding: 1px 4px;
      border-radius: 4px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 12px;
    }}

    pre {{
      background: #0b1020;
      color: #f1f5f9;
      padding: 10px 12px;
      border-radius: 8px;
      overflow: auto;
    }}

    pre code {{ background: transparent; padding: 0; color: inherit; }}

    table {{ width: 100%; border-collapse: collapse; margin: 8px 0 12px; font-size: 13px; }}
    th, td {{ border: 1px solid var(--line); padding: 7px 8px; text-align: left; vertical-align: top; }}
    th {{ background: #f8fafc; }}

    a {{ color: #1d4ed8; }}

    @media (max-width: 980px) {{
      .layout {{ grid-template-columns: 1fr; }}
      nav {{ position: relative; height: auto; border-right: none; border-bottom: 2px solid rgba(225, 6, 0, 0.55); }}
      main {{ padding: 12px; }}
      .doc {{ padding: 12px; }}
      .hero h1 {{ font-size: 21px; }}
    }}

    @media print {{
      @page {{ size: Letter portrait; margin: 0.45in; }}
      body {{ background: #fff; }}
      nav, .toolbar {{ display: none !important; }}
      .layout {{ grid-template-columns: 1fr; }}
      main {{ padding: 0; }}
      .hero {{ border: 1px solid #cfd6de; border-left: 3px solid #aaa; margin-bottom: 8px; }}
      .doc {{ border: none; border-radius: 0; box-shadow: none; padding: 0; margin: 0 0 12px; page-break-inside: avoid; }}
      .doc-title {{ border-bottom: 1px solid #bbb; }}
    }}
  </style>
</head>
<body>
  <div class=\"layout\">
    <nav>
      <p class=\"brand\">SRAM Analysis Hub</p>
      <p class=\"sub\">All Markdown analysis documents in one place</p>
      <span class=\"count-pill\">{len(files)} Documents</span>
      <ul>
        {''.join(nav_items)}
      </ul>
    </nav>
    <main>
      <section class=\"hero\">
        <h1>Executive Analysis Workspace</h1>
        <p>Unified view of competitive analysis, revenue streams, AI adoption strategy, and prompt artifacts. Use Print to export as PDF.</p>
      </section>
      <div class=\"toolbar\">
        <button class=\"secondary\" onclick=\"window.scrollTo({{top:0,behavior:'smooth'}})\">Top</button>
        <button onclick=\"window.print()\">Print / Save PDF</button>
      </div>
      {''.join(sections)}
    </main>
  </div>
</body>
</html>
"""

    OUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT}")
    print(f"Included {len(files)} markdown files")


if __name__ == "__main__":
    build()
