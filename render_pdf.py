"""Vygeneruje PDF návrhu z navrh.md (ReportLab a fonty Noto Sans)."""
import os
import re
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Flowable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output/pdf/posledni-prepazka-navrh.pdf"
FONT_DIR = Path(os.environ.get("NOTO_FONT_DIR", "/usr/share/fonts/noto"))
for name in ("Regular", "Bold"):
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / f"NotoSans-{name}.ttf")))

INK = colors.HexColor("#182f3c")
TEAL = colors.HexColor("#12615f")
LINE = colors.HexColor("#cadcdd")
LIGHT = colors.HexColor("#eff6f5")
WIDTH = A4[0] - 88
BODY = ParagraphStyle("body", fontName="Regular", fontSize=9, leading=13,
                      textColor=INK, spaceAfter=7)
TITLE = ParagraphStyle("title", parent=BODY, fontName="Bold", fontSize=32,
                       leading=39, textColor=TEAL, spaceAfter=9)
SECTION = ParagraphStyle("section", parent=BODY, fontName="Bold", fontSize=21,
                         leading=27, spaceBefore=8, spaceAfter=11)
SUB = ParagraphStyle("sub", parent=BODY, fontName="Bold", fontSize=12,
                     leading=16, textColor=TEAL, spaceBefore=7)
CELL = ParagraphStyle("cell", parent=BODY, fontSize=8, leading=11, spaceAfter=0)
HEADER = ParagraphStyle("header", parent=CELL, fontName="Bold", textColor=colors.white)


def para(text, style=BODY):
    safe = escape(text.replace("—", "–"))
    safe = re.sub(r"`([^`]+)`", r'<font color="#12615f">\1</font>', safe)
    return Paragraph(safe, style)


class StationMap(Flowable):
    def __init__(self):
        super().__init__()
        self.width = WIDTH
        self.height = 370

    def draw(self):
        names = ["Kajuta", "Chodba", "Chladicí komora", "Velín", "Sklad", "Dílna",
                 "Ošetřovna", "Servisní tunel", "Strojovna", "Předsíň", "Hangár",
                 "Únikový modul", "Zadní strojovna"]
        details = ["Start · klika · rozvaděč", "", "Ventil", "Konzole", "Pojistka", "",
                   "", "", "Patrona", "", "Karta · panel rampy", "Cíl · startovací pult",
                   "Ohnisko nákazy"]
        xs = [55, 187, 319, 451]
        columns = [0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 3]
        positions = [(xs[col], 247 - 94 * (idx // 4)) for idx, col in enumerate(columns)]
        positions.append((55, 340))
        canvas = self.canv
        gates = {3: "A", 4: "B", 8: "C", 10: "D"}

        def connect(left, right, label=None):
            x1, y1 = positions[left]
            x2, y2 = positions[right]
            canvas.setStrokeColor(TEAL)
            canvas.setLineWidth(1.3)
            canvas.line(x1, y1, x2, y2)
            if label:
                x, y = (x1 + x2) / 2, (y1 + y2) / 2
                canvas.setFillColor(TEAL)
                canvas.roundRect(x - 8, y - 8, 16, 16, 3, fill=1, stroke=0)
                canvas.setFillColor(colors.white)
                canvas.setFont("Bold", 8)
                canvas.drawCentredString(x, y - 3, label)

        for idx in range(11):
            connect(idx, idx + 1, gates.get(idx))
        connect(0, 12)
        for idx, (x, y) in enumerate(positions):
            canvas.setFillColor(colors.HexColor("#f9e9e4") if idx == 12 else LIGHT)
            canvas.setStrokeColor(LINE)
            canvas.roundRect(x - 53, y - 21, 106, 42, 5, fill=1, stroke=1)
            canvas.setFillColor(INK)
            canvas.setFont("Bold", 8.5)
            canvas.drawCentredString(x, y + 3 if details[idx] else y - 3, f"{idx}  {names[idx]}")
            if details[idx]:
                canvas.setFont("Regular", 7.3)
                canvas.drawCentredString(x, y - 10, details[idx])


def table(rows):
    labels = rows[0]
    weights = {
        "Tah": [.065, .18, .15, .12, .14, .345],
        "ID": [.065, .39, .20, .345],
        "Jméno a příjmení": [.23, .13, .25, .16, .23],
        "První použití": [.16, .20, .64],
        "Příkaz": [.22, .39, .39],
    }.get(labels[0], [.34, .66])
    cells = [[para(cell, HEADER if i == 0 else CELL) for cell in row]
             for i, row in enumerate(rows)]
    return Table(cells, colWidths=[WIDTH * width for width in weights], repeatRows=1,
                 style=TableStyle([
                     ("BACKGROUND", (0, 0), (-1, 0), TEAL),
                     ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
                     ("VALIGN", (0, 0), (-1, -1), "TOP"),
                     ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                     ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                     ("LINEBELOW", (0, -1), (-1, -1), .5, LINE),
                 ]))


def footer(canvas, doc):
    canvas.setStrokeColor(LINE)
    canvas.line(44, 43, A4[0] - 44, 43)
    canvas.setFillColor(TEAL)
    canvas.setFont("Regular", 8)
    canvas.drawString(44, 29, "Poslední přepážka  ·  Návrh hry  ·  4IT107")
    canvas.drawRightString(A4[0] - 44, 29, str(doc.page))


def main():
    flow = []
    rows = []
    for line in (ROOT / "navrh.md").read_text().splitlines() + [""]:
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if not all(cell == "---" for cell in cells):
                rows.append(cells)
            continue
        if rows:
            flow.extend([table(rows), Spacer(1, 9)])
            rows = []
        if line == "<!-- page -->":
            flow.append(PageBreak())
        elif line == "<!-- map -->":
            flow.append(StationMap())
        elif line.startswith("### "):
            flow.append(para(line[4:], SUB))
        elif line.startswith("## "):
            flow.append(para(line[3:], SECTION))
        elif line.startswith("# "):
            flow.append(para(line[2:], TITLE))
        elif line.startswith("- "):
            flow.append(para("• " + line[2:]))
        elif line and not line.startswith("<!--"):
            flow.append(para(line))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=44, rightMargin=44,
                      topMargin=44, bottomMargin=57, title="Poslední přepážka",
                      author="Tým 4IT107").build(flow, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    main()
