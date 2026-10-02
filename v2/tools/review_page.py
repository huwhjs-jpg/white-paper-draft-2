"""Build a side-by-side review page: new v2 chapter text next to the approved v1 text it came from,
with a change note per section, a fix log, decisions for the user, and the sources cited.
Usage: python3 review_page.py ch1|ch3"""
import re, sys, html, json, os, copy
from bs4 import BeautifulSoup
sys.path.insert(0, os.path.dirname(__file__))
from sources import NEW
from chapter_data import PAGES

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V1 = BeautifulSoup(open(os.path.join(ROOT, 'china-playbook-assembly-source.html'), encoding='utf-8').read(), 'lxml')

# ---- v1 reference titles -------------------------------------------------
V1REF = {}
for tr in V1.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) >= 2 and re.fullmatch(r'\d+', tds[0].get_text().strip()):
        V1REF.setdefault(int(tds[0].get_text().strip()), tds[1].get_text(' ', strip=True))


def container(key):
    if key == 'exec':
        h = V1.find('h3', string=re.compile('^Executive summary'))
        return h.parent, h
    el = V1.find('div', id=key)
    return el, el.find('h3')


def v1_sub(key, h4=None, keep=None):
    """HTML of a v1 subsection. h4=None -> text before the first h4. keep: list of paragraph
    indexes (within that subsection) to show; others are dropped."""
    box, h3 = container(key)
    title = h3.get_text().strip()
    nodes, on = [], h4 is None
    for el in box.children:
        if not getattr(el, 'name', None):
            continue
        if el.name == 'h3':
            continue
        if el.name == 'h4':
            if on and h4 is not None:
                break
            if h4 is None:
                break
            on = el.get_text().strip().startswith(h4)
            continue
        if on:
            nodes.append(el)
    if keep is not None:
        nodes = [n for i, n in enumerate(nodes) if i in keep]
    out = []
    for n in nodes:
        n = copy.copy(n)
        cls = n.get('class') or []
        if 'exm' in cls:
            if 'empty' in cls:
                continue
            out.append('<p class="exref">%s: %s</p>' % (n.find('span', class_='exn').get_text(), n.find('b').get_text()))
            continue
        for sp in n.find_all('span', class_='exs'):
            sp.decompose()
        out.append(str(n))
    head = title + (' · ' + h4 if h4 else '')
    return '<div class="v1src"><p class="v1h">v1 · %s</p>%s</div>' % (html.escape(head), '\n'.join(out))


def cites(text):
    v1, new = set(), set()
    for m in re.findall(r'<sup>(.*?)</sup>', text):
        for part in m.split(','):
            part = part.strip()
            if part.startswith('N'):
                r = re.match(r'N(\d+)(?:[–-]N?(\d+))?', part)
                a = int(r.group(1)); b = int(r.group(2) or a)
                new.update('N%d' % i for i in range(a, b + 1))
            elif part:
                r = re.match(r'(\d+)(?:[–-](\d+))?', part)
                if r:
                    a = int(r.group(1)); b = int(r.group(2) or a)
                    v1.update(range(a, b + 1))
    return sorted(v1), sorted(new, key=lambda x: int(x[1:]))


def words(s):
    t = re.sub(r'<sup>.*?</sup>', '', s)
    t = re.sub(r'<div class="exm">.*?</div>', '', t, flags=re.S)
    t = re.sub(r'<div class="tw snap">.*?</div>', '', t, flags=re.S)
    return len(html.unescape(re.sub(r'<[^>]+>', ' ', t)).split())


def render_new(sec):
    s = str(sec)
    s = re.sub(r'<div class="exm"><span class="exn">(.*?)</span>\s*<b>(.*?)</b><span class="exs">(.*?)</span></div>',
               r'<figure class="exm"><span class="exn">\1</span><span class="ext">\2</span><span class="exs">\3</span></figure>', s)
    s = re.sub(r'<div class="tw snap">(.*?)</div>', r'<div class="tw">\1</div>', s, flags=re.S)
    s = s.replace('<div class="case"><b>', '<div class="case"><p class="caseh">').replace('</b><p>', '</p><p>', 1)
    return s


CSS = open(os.path.join(os.path.dirname(__file__), 'review.css')).read()


def build(key):
    P = PAGES[key]
    src = open(os.path.join(ROOT, 'v2', 'text', key + '.html'), encoding='utf-8').read()
    soup = BeautifulSoup(src, 'lxml')
    title = soup.find('h3').get_text()
    inbrief = soup.find('div', class_='inbrief')
    inbrief.b.decompose()
    total = words(src)
    v1all, newall = cites(src)
    secs = soup.find_all('section')
    parts = []
    parts.append('<title>%s</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap"><style>%s</style>' % (html.escape(P['page_title']), CSS))
    parts.append('<div class="wrap">')
    parts.append('<header class="top"><p class="kicker">The China Playbook for Emerging Asia · Batch 3 review · %s</p>' % P['date'])
    parts.append('<h1>%s</h1>' % html.escape(title))
    parts.append('<p class="answer">%s</p>' % inbrief.get_text())
    parts.append('<dl class="meta">'
                 '<div><dt>Words</dt><dd>%d <span>target about %s</span></dd></div>'
                 '<div><dt>Exhibits</dt><dd>%s</dd></div>'
                 '<div><dt>Approved text drawn on</dt><dd>%s</dd></div>'
                 '<div><dt>Fixes logged</dt><dd>%d</dd></div></dl>' % (total, P['target'], P['exhibits'], P['drawn'], len(P['fixes'])))
    parts.append('<nav class="toc"><a href="#decide">For your decision</a>' + ''.join(
        '<a href="#s%s">%s</a>' % (s['data-sec'].replace('.', '-'), s['data-sec']) for s in secs) +
        '<a href="#fixes">Fix log</a><a href="#sources">Sources</a></nav></header>')

    parts.append('<section id="decide" class="decide"><h2>For your decision</h2><p class="lede">%s</p><ol>' % P['decide_lede'])
    for d in P['decide']:
        parts.append('<li><p class="dh">%s</p><p>%s</p></li>' % d)
    parts.append('</ol></section>')

    parts.append('<div class="legend"><span class="lnew">New text (v2)</span><span class="lold">Approved text it came from (v1)</span></div>')
    for s in secs:
        n = s['data-sec']
        meta = P['sections'][n]
        h4 = s.find('h4')
        parts.append('<section class="pair" id="s%s">' % n.replace('.', '-'))
        parts.append('<div class="sechead"><span class="num">%s</span><h2>%s</h2></div>' % (n, h4.get_text()))
        parts.append('<div class="change"><p class="chl">What changed</p><ul>%s</ul></div>' % ''.join('<li>%s</li>' % c for c in meta['changes']))
        h4.decompose()
        new_html = render_new(s)
        new_html = re.sub(r'^<section[^>]*>|</section>$', '', new_html.strip())
        old = ''.join(v1_sub(*a) for a in meta['v1'])
        if meta.get('v1_none'):
            old += '<p class="nov1">%s</p>' % meta['v1_none']
        parts.append('<div class="cols"><div class="col new"><p class="colh">New text</p>%s</div><div class="col old"><p class="colh">Approved v1</p>%s</div></div></section>' % (new_html, old))

    parts.append('<section id="fixes" class="fixes"><h2>Fix log</h2><p class="lede">Accuracy fixes and wording changes made in this chapter, with the source. Items that change a verdict, learning or headline number are in "For your decision" above; none of these does.</p>'
                 '<div class="tw"><table><thead><tr><th>No.</th><th>What was fixed</th><th>Source</th></tr></thead><tbody>')
    for i, (what, srcs) in enumerate(P['fixes'], 1):
        parts.append('<tr><td class="n">%s-%d</td><td>%s</td><td>%s</td></tr>' % (P['fixprefix'], i, what, srcs))
    parts.append('</tbody></table></div></section>')

    parts.append('<section id="sources" class="sources"><h2>Sources cited in this chapter</h2>'
                 '<p class="lede">v1 numbers are kept until references are renumbered at assembly. N-numbers are new in batch 3. '
                 '“Search-verified” means the fact was confirmed through web search results that name the source page, because this session cannot open pages directly.</p>')
    parts.append('<h3>New sources</h3><div class="tw"><table><thead><tr><th>No.</th><th>Source</th><th>Type</th><th>How checked</th></tr></thead><tbody>')
    tmap = {'P': 'Primary', 'S': 'Secondary', 'D': 'Data'}
    for k in newall:
        t, url, st, chk = NEW[k]
        parts.append('<tr><td class="n">%s</td><td>%s <a href="%s">link</a></td><td>%s</td><td>%s</td></tr>' % (k, html.escape(t), html.escape(url), tmap[st], html.escape(chk)))
    parts.append('</tbody></table></div><h3>Approved (v1) references still cited</h3><ul class="v1refs">')
    for k in v1all:
        parts.append('<li><span class="n">%d</span> %s</li>' % (k, html.escape(V1REF.get(k, '(not in v1 list)'))[:220]))
    parts.append('</ul></section>')
    parts.append('<footer><p>Source files: <code>v2/text/%s.html</code> (paper text in assembly-source conventions), <code>v2/tools/chapter_data.py</code> (notes and fix log). Built %s.</p></footer></div>' % (key, P['date']))
    out = os.path.join(ROOT, 'v2', 'review', key + '-review.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write('\n'.join(parts))
    print(out, total, 'words;', len(v1all), 'v1 refs;', len(newall), 'new')


if __name__ == '__main__':
    for k in sys.argv[1:]:
        build(k)
