"""Vygeneruje PDF návrhu z navrh.md (HTML/CSS přes WeasyPrint).

Spuštění: uv run --with weasyprint python render_pdf.py
"""
import re
from html import escape
from pathlib import Path

from weasyprint import HTML

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output/pdf/vesmirna-stanice-orfeus-navrh.pdf"
DOC_TITLE = "Vesmírná stanice Orfeus"
FOOTER_LEFT = "4IT107 Programování v Javě"
FOOTER_RIGHT = "Vesmírná stanice Orfeus - Návrh hry "

CSS = """
:root{ --ink:#0A0A0A; --body:#34383F; --muted:#6B7280; --accent:#2563EB;
  --rule:#E5E7EB; --box:#F9FAFB; --tint:#EFF4FF; --warn:#EA580C; }
@font-face{font-family:'Grotesk';src:url('fonts/SpaceGrotesk.ttf');}
@font-face{font-family:'Plex';src:url('fonts/IBMPlexSans.ttf');}
@font-face{font-family:'PlexMono';src:url('fonts/IBMPlexMono-Regular.ttf');font-weight:400;}
@font-face{font-family:'PlexMono';src:url('fonts/IBMPlexMono-Medium.ttf');font-weight:500;}

@page{ size:A4; margin:18mm 20mm 16mm 20mm;
  @bottom-left{ content:"FOOTER_LEFT"; font-family:'Plex'; font-size:7.5pt; color:#9AA1AC; }
  @bottom-right{ content:"FOOTER_RIGHT" counter(page); font-family:'Plex'; font-size:7.5pt; color:#9AA1AC; } }
@page cover{ margin:20mm; @bottom-left{ content:none; } @bottom-right{ content:none; } }

html{ font-family:'Plex'; color:var(--body); font-size:9.4pt; line-height:1.48; }
body{ margin:0; }

/* Cover */
.cover{ page:cover; height:257mm; position:relative; }
.cover .block{ position:absolute; top:78mm; left:0; right:0; }
h1.title{ font-family:'Grotesk'; font-weight:700; font-size:40pt; line-height:1.05; letter-spacing:-1pt;
  color:var(--ink); margin:0 0 14pt; }
.cover .lead{ font-size:12pt; line-height:1.5; color:var(--body); max-width:125mm; margin:0; }
.toc{ position:absolute; bottom:0; left:0; right:0; border-top:1pt solid var(--rule); padding-top:10pt; }
.toc table{ width:100%; border-collapse:collapse; }
.toc td{ padding:4pt 0; border-bottom:.5pt solid var(--rule); font-size:9.5pt; color:var(--ink); }
.toc td.n{ color:var(--muted); width:26pt; }
.toc tr.l3 td{ font-size:8.8pt; color:var(--body); padding:2.5pt 0; }
.toc tr.l3 td:first-child{ padding-left:0; }
.toc tr.l2 td{ font-weight:600; }

/* Sections */
h2{ break-before:page; font-family:'Grotesk'; font-weight:700; font-size:20pt; letter-spacing:-.4pt;
  color:var(--ink); margin:0 0 14pt; line-height:1.2; }
h3{ font-family:'Grotesk'; font-weight:700; font-size:13pt; letter-spacing:-.2pt; color:var(--ink);
  margin:20pt 0 8pt; line-height:1.25; }
h2 + h3, .pb + h3{ margin-top:0; }
h4{ font-family:'Plex'; font-weight:600; font-size:10.4pt; color:var(--ink); margin:14pt 0 5pt; }
h3 + h4{ margin-top:4pt; }
.num{ color:var(--muted); margin-right:7pt; }
.pb{ break-before:page; height:0; }
p{ margin:0 0 7pt; text-align:left; orphans:3; widows:3; }
code{ font-family:'PlexMono'; font-size:.9em; color:var(--ink); background:var(--box);
  border:.5pt solid var(--rule); border-radius:2pt; padding:0 2.5pt; }

ul.feat{ list-style:none; padding-left:0; margin:4pt 0 8pt; }
ul.feat li{ position:relative; padding-left:13pt; margin-bottom:5pt; }
ul.feat li:before{ content:"-"; position:absolute; left:0; color:var(--muted); }

.note{ border-left:2.5pt solid var(--accent); background:var(--tint); padding:8pt 11pt;
  border-radius:0 3pt 3pt 0; margin:0 0 12pt; color:var(--ink); }

/* Tables */
table.data{ width:100%; border-collapse:collapse; margin:4pt 0 12pt; font-size:8.3pt; line-height:1.38; }
table.data thead{ display:table-header-group; }
table.data th{ font-weight:600; font-size:8pt; color:var(--ink); text-align:left; padding:0 6pt 4pt 0;
  border-bottom:1pt solid var(--ink); vertical-align:bottom; }
table.data td{ padding:3.2pt 6pt 3.2pt 0; border-bottom:.5pt solid var(--rule); vertical-align:top; color:var(--body); }
table.data tr{ break-inside:avoid; }
table.data td.id{ color:var(--muted); white-space:nowrap; }
table.data td.cmd{ font-family:'PlexMono'; font-size:7.8pt; color:var(--ink); }
table.data td.dash{ color:#B6BCC6; }
table.data td.hit{ color:var(--ink); font-weight:600; }
table.data td.warn{ color:var(--warn); font-weight:600; }

/* Map */
.map{ margin:6pt 0 14pt; border:.6pt solid var(--rule); border-radius:5pt; background:var(--box); padding:10pt; }
.map svg{ width:100%; height:auto; display:block; }
"""


def inline(text):
    safe = escape(text, quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", safe)


def station_map():
    names = ["Kajuta", "Chodba", "Chladicí komora", "Můstek", "Sklad", "Dílna",
             "Ošetřovna", "Servisní tunel", "Strojovna", "Předsíň", "Hangár",
             "Únikový modul", "Zadní strojovna", "Servisní šachta"]
    details = ["Start · klika · rozvaděč", "", "Ventil", "Konzole",
               "Skříň: pojistka", "Servisní stojany", "", "",
               "Přepravka: patrona", "", "Schránka: karta · panel",
               "Cíl · startovací pult", "Ohnisko nákazy", "Ohnisko nákazy"]
    w = 50  # poloviční šířka uzlu
    xs = [182, 312, 442, 572]
    columns = [0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 3]
    pos = [(xs[c], 125 + 94 * (i // 4)) for i, c in enumerate(columns)]
    pos += [(182, 32), (52, 219)]
    links = [(i, i + 1) for i in range(11)] + [(0, 12), (7, 13)]
    gates = {(3, 4): "A", (4, 5): "B", (8, 9): "C", (10, 11): "D", (0, 12): "E", (7, 13): "F"}
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 624 340">']

    for a, b in links:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        hot = b >= 12
        style = 'stroke="#EA580C" stroke-dasharray="4 3"' if hot else 'stroke="#93B4F5"'
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {style} stroke-width="1.6"/>')
    for i, (x, y) in enumerate(pos):
        start, goal, hot = i == 0, i == 11, i >= 12
        fill = "#FFF4ED" if hot else ("#2563EB" if goal else "#FFFFFF")
        stroke = "#EA580C" if hot else ("#2563EB" if (start or goal) else "#D7DCE3")
        ink = "#FFFFFF" if goal else "#0A0A0A"
        sub = "#DBE6FD" if goal else ("#EA580C" if hot else "#6B7280")
        num = "#DBE6FD" if goal else ("#EA580C" if hot else "#2563EB")
        out.append(f'<rect x="{x-w}" y="{y-21}" width="{2*w}" height="42" rx="5" fill="{fill}" '
                   f'stroke="{stroke}" stroke-width="{1.2 if (start or goal or hot) else .8}"/>')
        ty = y - 2 if details[i] else y + 3.5
        out.append(f'<text x="{x-w+8}" y="{ty}" font-family="PlexMono" font-weight="500" font-size="7.5" fill="{num}">{i:02d}</text>')
        out.append(f'<text x="{x-w+22}" y="{ty}" font-family="Grotesk" font-weight="700" font-size="8.6" fill="{ink}">{names[i]}</text>')
        if details[i]:
            out.append(f'<text x="{x-w+8}" y="{y+11}" font-family="Plex" font-size="6.8" fill="{sub}">{details[i]}</text>')
    for (a, b), label in gates.items():
        (x1, y1), (x2, y2) = pos[a], pos[b]
        x, y = (x1 + x2) / 2, (y1 + y2) / 2
        color = "#EA580C" if b >= 12 else "#0A0A0A"
        out.append(f'<rect x="{x-9}" y="{y-9}" width="18" height="18" rx="4" fill="{color}"/>')
        out.append(f'<text x="{x}" y="{y+3.5}" text-anchor="middle" font-family="PlexMono" '
                   f'font-weight="500" font-size="9" fill="#FFFFFF">{label}</text>')
    out.append("</svg>")
    return '<div class="map">' + "".join(out) + "</div>"


def heading(level, text):
    m = re.match(r"(\d+(?:\.\d+)*)\.?\s+(.*)", text)
    if not m:
        return f"<h{level}>{inline(text)}</h{level}>"
    num, title = m.groups()
    label = f"{num}." if level == 2 else num
    return f'<h{level}><span class="num">{label}</span>{inline(title)}</h{level}>'


COL_WIDTHS = {"Tah": [5, 21, 14, 14, 19, 27]}


def table(rows):
    head, body = rows[0], rows[1:]
    widths = COL_WIDTHS.get(head[0])
    cols = "".join(f'<col style="width:{w}%">' for w in widths) if widths else ""
    out = [f'<table class="data"><colgroup>{cols}</colgroup><thead><tr>']
    out += [f"<th>{inline(c)}</th>" for c in head]
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>")
        for i, cell in enumerate(row):
            cls = []
            if i == 0 and re.fullmatch(r"\d+", cell):
                cls.append("id")
            if head[i] in ("Příkaz",) and head[0] in ("Tah", "První použití"):
                cls.append("cmd")
            if cell == "-":
                cls.append("dash")
            elif head[i] == "Změna":
                cls.append("warn" if cell.startswith("Nákaza") else "hit")
            attr = f' class="{" ".join(cls)}"' if cls else ""
            out.append(f"<td{attr}>{inline(cell)}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def build_html():
    lines = (ROOT / "navrh.md").read_text().splitlines()
    title = lines[0][2:]
    lead = next(l for l in lines[1:] if l.strip())
    body_lines = lines[lines.index(lead) + 1:]

    toc = []
    for l in body_lines:
        m = re.match(r"(##|###) (\d+(?:\.\d+)?)\.?\s+(.*)", l)
        if m:
            toc.append((len(m.group(1)), m.group(2), m.group(3).strip()))

    parts = ['<section class="cover"><div class="block">',
             f'<h1 class="title">{inline(title)}</h1>',
             f'<p class="lead">{inline(lead)}</p></div>',
             '<div class="toc"><table>']
    parts += [f'<tr class="l{lvl}"><td class="n">{n}{"." if lvl == 2 else ""}</td><td>{escape(t)}</td></tr>'
              for lvl, n, t in toc]
    parts.append("</table></div></section>")

    rows, items, note, page_break = [], [], False, False

    def flush():
        nonlocal rows, items
        if rows:
            parts.append(table(rows))
            rows = []
        if items:
            parts.append('<ul class="feat">' + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items = []

    for line in body_lines + [""]:
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not all(c == "---" for c in cells):
                rows.append(cells)
            continue
        if line.startswith("- "):
            items.append(line[2:])
            continue
        flush()
        if line == "<!-- page -->":
            page_break = True
            continue
        if line.startswith("## "):
            page_break = False  # kapitola začíná novou stranou sama
        elif line and page_break:
            parts.append('<div class="pb"></div>')
            page_break = False
        if line == "<!-- map -->":
            parts.append(station_map())
        elif line == "<!-- note -->":
            note = True
        elif line.startswith("#"):
            hashes, _, text = line.partition(" ")
            parts.append(heading(len(hashes), text))
        elif line and not line.startswith("<!--"):
            cls = ' class="note"' if note else ""
            parts.append(f"<p{cls}>{inline(line)}</p>")
            note = False

    css = CSS.replace("FOOTER_LEFT", FOOTER_LEFT).replace("FOOTER_RIGHT", FOOTER_RIGHT)
    return (f'<!doctype html><html lang="cs"><head><meta charset="utf-8">'
            f"<title>{escape(DOC_TITLE)}</title><style>{css}</style></head>"
            f"<body>{''.join(parts)}</body></html>")


def main():
    html = build_html()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(ROOT)).write_pdf(str(OUTPUT))
    print(f"Hotovo: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
