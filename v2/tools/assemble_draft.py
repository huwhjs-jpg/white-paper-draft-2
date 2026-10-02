"""Assemble the integrated v2 draft from v2/text/*.html into one standalone HTML file, a Markdown file
and (via LibreOffice) a Word file. Citations keep v1 reference numbers and batch-3 N-numbers until the
references are renumbered at assembly.
Usage: python3 v2/tools/assemble_draft.py"""
import os, re, sys, html, subprocess, shutil
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(__file__))
from sources import NEW
from review_page import V1REF, cites

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TXT = os.path.join(ROOT, 'v2', 'text')
OUT = os.path.join(ROOT, 'v2', 'draft')
NAME = 'China Playbook — Draft v2 full text (2 Oct 2026)'
ORDER = ['exec', 'about', 'ch1', 'ch2', 'ch3', 'ch4', 'conclusion', 'appendices-plan']
STATUS = {
    'exec': 'First draft, 2 Oct 2026, not yet reviewed by the user',
    'about': 'First draft, 2 Oct 2026, not yet reviewed by the user',
    'ch1': 'Draft, rewritten for flow 2 Oct 2026; awaiting user review',
    'ch2': 'Draft, rewritten for flow 2 Oct 2026; awaiting user review',
    'ch3': 'Draft, rewritten for flow 2 Oct 2026; awaiting user review',
    'ch4': 'Draft, rewritten for flow 2 Oct 2026; awaiting user review',
    'conclusion': 'First draft, 2 Oct 2026, not yet reviewed by the user',
    'appendices-plan': 'Plan only; appendices not yet written',
}

parts = {k: open(os.path.join(TXT, k + '.html'), encoding='utf-8').read() for k in ORDER}
allsrc = ''.join(parts.values())
v1, new = cites(allsrc)


def body_words(s):
    t = re.sub(r'<sup>.*?</sup>', '', s)
    t = re.sub(r'<div class="exm">.*?</div>', '', t, flags=re.S)
    return len(html.unescape(re.sub(r'<[^>]+>', ' ', t)).split())


CSS = """
:root{--ink:#0D1E43;--text:#1F2A40;--muted:#5B6782;--rule:#D6DEEA;--blue:#0B6FD9;--pale:#EAF2FD;--amber:#C07A00;--amberbg:#FBF1DE;--paper:#FFFFFF}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ink:#E6ECF7;--text:#CBD4E6;--muted:#8F9BB4;--rule:#2A3650;--blue:#3383E0;--pale:#16294A;--amber:#B97A12;--amberbg:#2E2414;--paper:#111827;color-scheme:dark}}
:root[data-theme="dark"]{--ink:#E6ECF7;--text:#CBD4E6;--muted:#8F9BB4;--rule:#2A3650;--blue:#3383E0;--pale:#16294A;--amber:#B97A12;--amberbg:#2E2414;--paper:#111827;color-scheme:dark}
body{background:var(--paper);color:var(--text);font-family:"Source Serif 4","Palatino Linotype",Palatino,Georgia,serif;font-size:16.5px;line-height:1.6}
.wrap{max-width:760px;margin:0 auto;padding-inline:20px;padding-block:32px 72px}
h1,h2,h3,h4{color:var(--ink);text-wrap:balance}
h1{font-size:34px;line-height:1.15;margin:0 0 6px} .sub{font-size:19px;color:var(--muted);margin:0 0 18px}
h3{font-size:26px;margin:56px 0 6px;padding-top:16px;border-top:2px solid var(--ink)} h4{font-size:19px;margin:28px 0 6px}
.status{font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;font-size:12px;letter-spacing:.04em;color:var(--amber);background:var(--amberbg);display:inline-block;padding:2px 8px;border-radius:3px;margin:0 0 10px}
.banner{font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;font-size:14px;border:1px solid var(--rule);padding:12px 14px;border-radius:6px;color:var(--muted)}
.inbrief{background:var(--pale);padding:12px 14px;border-radius:4px;font-style:italic;margin:10px 0 16px}.inbrief b{font-style:normal;margin-right:6px;color:var(--ink)}
.exm{margin:16px 0;padding:10px 12px;border:1px dashed var(--blue);border-radius:4px;font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;font-size:14px}
.exn{color:var(--blue);font-weight:600;margin-right:6px}.exs{display:block;color:var(--muted);font-size:12px}
.case{margin:16px 0;padding:12px 14px;border-left:3px solid var(--amber);background:var(--amberbg)}
.copy{border-left:3px solid var(--blue);padding-left:12px}
sup{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10px;color:var(--blue)}
.tw{overflow-x:auto;margin:14px 0} table{border-collapse:collapse;width:100%;font-family:"IBM Plex Sans","Segoe UI",system-ui,sans-serif;font-size:13.5px}
th,td{text-align:left;vertical-align:top;padding:6px 8px;border-bottom:1px solid var(--rule)} th{color:var(--muted);font-weight:600}
td,li,p{overflow-wrap:anywhere} .refs li{font-size:13.5px;margin-bottom:4px} .toc a{color:var(--blue)}
.note{color:var(--muted);font-style:italic}
"""


def build_html():
    out = ['<title>China Playbook Draft v2</title>',
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&family=IBM+Plex+Sans:wght@400;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap">',
           '<style>%s</style><div class="wrap">' % CSS,
           '<h1>The China Playbook for Emerging Asia</h1>',
           '<p class="sub">What industrial leaders can learn from Chinese equipment makers\' rise in India and Southeast Asia</p>',
           '<p class="banner"><b>Working draft v2, 2 October 2026.</b> Data as of 2 October 2026 where re-checked, otherwise 28 September 2026. '
           'Reference numbers are provisional: plain numbers are the approved v1 references, and N-numbers are sources added in batch 3. '
           'They will be renumbered by first citation at assembly. Exhibits are shown as placeholders. '
           'Body chapters: about %d words (target about 7,000 for 20 pages).</p>' % sum(body_words(parts[k]) for k in ('ch1', 'ch2', 'ch3', 'ch4')),
           '<h4>Contents</h4><ul class="toc">']
    for k in ORDER:
        t = BeautifulSoup(parts[k], 'lxml').find('h3').get_text()
        out.append('<li><a href="#%s">%s</a></li>' % (k, html.escape(t)))
    out.append('<li><a href="#refs">References cited in this draft</a></li></ul>')
    for k in ORDER:
        s = parts[k]
        s = re.sub(r'<section[^>]*>|</section>', '', s)
        s = s.replace('<div class="paper" id="%s">' % k, '<div class="paper" id="%s">' % k, 1)
        s = re.sub(r'(<h3>.*?</h3>)', r'\1<p class="status">%s</p>' % STATUS[k], s, count=1)
        out.append(s)
    out.append('<div id="refs"><h3>References cited in this draft (provisional numbering)</h3><h4>Approved v1 references still cited</h4><ul class="refs">')
    for n in v1:
        out.append('<li><b>%d</b> %s</li>' % (n, html.escape(V1REF.get(n, '(see v1 reference list)'))))
    out.append('</ul><h4>Sources added in batch 3</h4><ul class="refs">')
    for k in new:
        t, url, st, chk = NEW[k]
        out.append('<li><b>%s</b> %s <a href="%s">%s</a> <i>(%s; %s)</i></li>' % (k, html.escape(t), html.escape(url), html.escape(url), {'P': 'primary', 'S': 'secondary', 'D': 'data'}[st], html.escape(chk)))
    out.append('</ul></div></div>')
    return '\n'.join(out)


def to_md(h):
    s = BeautifulSoup(h, 'lxml')
    lines = []
    def runs(el):
        t = ''
        for c in el.children:
            if isinstance(c, str):
                t += c
            elif c.name == 'sup':
                t += '[' + c.get_text() + ']'
            elif c.name in ('b', 'strong'):
                t += '**' + runs(c).strip() + '**'
            elif c.name in ('i', 'em'):
                t += '*' + runs(c).strip() + '*'
            elif c.name == 'a':
                t += runs(c)
            elif c.name == 'br':
                t += ' '
            else:
                t += runs(c)
        return re.sub(r'\s+', ' ', t)
    def walk(el):
        for c in el.children:
            if isinstance(c, str) or c.name in ('style', 'title', 'link'):
                continue
            cls = c.get('class') or []
            if c.name == 'h1': lines.append('# ' + c.get_text().strip() + '\n')
            elif c.name == 'h3': lines.append('\n## ' + c.get_text().strip() + '\n')
            elif c.name == 'h4': lines.append('\n### ' + c.get_text().strip() + '\n')
            elif c.name == 'p':
                pre = '> ' if 'status' in cls or 'banner' in cls else ''
                lines.append(pre + runs(c).strip() + '\n')
            elif c.name in ('ul', 'ol'):
                for li in c.find_all('li', recursive=False):
                    lines.append('- ' + runs(li).strip())
                lines.append('')
            elif c.name == 'div' and 'inbrief' in cls:
                lines.append('> ' + runs(c).strip() + '\n')
            elif c.name == 'div' and 'exm' in cls:
                lines.append('> **[' + c.find('span', class_='exn').get_text() + ']** ' + c.find('b').get_text() + ' *(' + c.find('span', class_='exs').get_text() + ')*\n')
            elif c.name == 'div' and 'case' in cls:
                b = c.find('b'); title = b.get_text(); b.extract()
                lines.append('> **' + title + '** ' + ' '.join(runs(p).strip() for p in c.find_all('p')) + '\n')
            elif c.name == 'div' and 'tw' in cls:
                tb = c.find('table'); rows = tb.find_all('tr')
                for i, tr in enumerate(rows):
                    cells = [runs(td).strip().replace('|', '/') for td in tr.find_all(['th', 'td'])]
                    lines.append('| ' + ' | '.join(cells) + ' |')
                    if i == 0:
                        lines.append('|' + '---|' * len(cells))
                lines.append('')
            else:
                walk(c)
    walk(s.body or s)
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(lines))


def to_docx(h, path):
    """Plain reading copy in Word (not the house layout; that comes from build/ at Word draft v2)."""
    import docx
    from docx.shared import Pt, RGBColor
    d = docx.Document()
    st = d.styles['Normal']; st.font.name = 'Palatino Linotype'; st.font.size = Pt(11)
    for name in ('Heading 1', 'Heading 2', 'Heading 3'):
        d.styles[name].font.name = 'Palatino Linotype'; d.styles[name].font.color.rgb = RGBColor(0x0D, 0x1E, 0x43)
    soup = BeautifulSoup(h, 'lxml')
    def add_runs(par, el, bold=False, ital=False):
        for c in el.children:
            if isinstance(c, str):
                t = re.sub(r'\s+', ' ', c)
                if t: r = par.add_run(t); r.bold = bold; r.italic = ital
            elif c.name == 'sup':
                r = par.add_run('[' + c.get_text() + ']'); r.font.superscript = True; r.font.color.rgb = RGBColor(0x0B, 0x6F, 0xD9)
            elif c.name in ('b', 'strong'): add_runs(par, c, True, ital)
            elif c.name in ('i', 'em'): add_runs(par, c, bold, True)
            else: add_runs(par, c, bold, ital)
    def walk(el):
        for c in el.children:
            if isinstance(c, str) or c.name in ('style', 'title', 'link'): continue
            cls = c.get('class') or []
            if c.name == 'h1': d.add_heading(c.get_text().strip(), 0)
            elif c.name == 'h3': d.add_heading(c.get_text().strip(), 1)
            elif c.name == 'h4': d.add_heading(c.get_text().strip(), 2)
            elif c.name == 'p':
                par = d.add_paragraph(); add_runs(par, c)
                if 'status' in cls or 'banner' in cls or 'note' in cls:
                    for r in par.runs: r.italic = True; r.font.color.rgb = RGBColor(0xC0, 0x7A, 0x00)
            elif c.name in ('ul', 'ol'):
                for li in c.find_all('li', recursive=False):
                    par = d.add_paragraph(style='List Bullet'); add_runs(par, li)
            elif c.name == 'div' and ('inbrief' in cls or 'case' in cls):
                par = d.add_paragraph(); add_runs(par, c, ital=('inbrief' in cls))
                par.paragraph_format.left_indent = Pt(18)
            elif c.name == 'div' and 'exm' in cls:
                par = d.add_paragraph()
                r = par.add_run('[' + c.find('span', class_='exn').get_text() + '] ' + c.find('b').get_text()); r.bold = True; r.font.color.rgb = RGBColor(0x0B, 0x6F, 0xD9)
                r = par.add_run('  (' + c.find('span', class_='exs').get_text() + ')'); r.italic = True
            elif c.name == 'div' and 'tw' in cls:
                rows = c.find('table').find_all('tr')
                ncol = max(len(tr.find_all(['th', 'td'])) for tr in rows)
                t = d.add_table(rows=0, cols=ncol); t.style = 'Table Grid'
                for tr in rows:
                    cells = tr.find_all(['th', 'td']); row = t.add_row().cells
                    if len(cells) == 1:
                        m = row[0].merge(row[-1]); add_runs(m.paragraphs[0], cells[0], bold=True); continue
                    for i, td in enumerate(cells[:ncol]):
                        add_runs(row[i].paragraphs[0], td, bold=(td.name == 'th'))
                d.add_paragraph()
            else: walk(c)
    walk(soup.body or soup)
    d.save(path)


def main():
    os.makedirs(OUT, exist_ok=True)
    h = build_html()
    hp = os.path.join(OUT, NAME + '.html'); open(hp, 'w', encoding='utf-8').write(h)
    mp = os.path.join(OUT, NAME + '.md'); open(mp, 'w', encoding='utf-8').write(to_md(h))
    dp = os.path.join(OUT, NAME + '.docx'); to_docx(h, dp)
    print(hp); print(mp); print(dp); print(len(v1), 'v1 refs;', len(new), 'new refs')


if __name__ == '__main__':
    main()
