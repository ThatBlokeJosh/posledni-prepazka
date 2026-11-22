# Vesmírná stanice Orfeus

Návrh týmové textové adventury pro 4IT107 Programování v Javě. Technik na napadené vesmírné stanici obnovuje systémy a hledá cestu k únikovému modulu.

- [Návrh k odevzdání v PDF](output/pdf/vesmirna-stanice-orfeus-navrh.pdf)
- [Upravitelný zdroj návrhu](navrh.md)

Jména a rozdělení práce čtyř členů týmu jsou v šesté části návrhu.

PDF se regeneruje příkazem `uv run --with weasyprint python render_pdf.py` (nebo `python render_pdf.py` s nainstalovaným balíčkem WeasyPrint). Skript převede `navrh.md` do HTML/CSS a vysází ho přes WeasyPrint s fonty Space Grotesk, IBM Plex Sans a IBM Plex Mono ze složky `fonts/` (licence OFL).
