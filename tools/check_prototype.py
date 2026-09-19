"""Offline guardrails for the unpublished Guardian website RC. No dependencies."""
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


html = (DOCS / "index.html").read_text()
css = (DOCS / "assets/site.css").read_text()
js = (DOCS / "assets/site.js").read_text()
page = Page()
page.feed(html)
ids = [a['id'] for _, a in page.elements if 'id' in a]
assert len(ids) == len(set(ids)), 'Duplicate IDs'
assert ('html', {'lang': 'pl'}) in page.elements
assert not re.search(r'Guardian G1(?!\.1)', html), 'Stale product name'
assert 'Publiczna dystrybucja Guardian G1.1 Pilot nie jest jeszcze autoryzowana.' in html
assert any(t == 'meta' and a.get('name') == 'robots' and a.get('content') == 'noindex, nofollow' for t, a in page.elements)
for tag, attrs in page.elements:
    if tag == 'a':
        target = attrs.get('href', '')
        assert target, 'Empty link'
        if target.startswith('#'):
            assert target[1:] in ids, f'Missing anchor: {target}'
        else:
            assert target.split('?')[0] == 'mailto:support@excelforge.eu', f'Unexpected active link: {target}'
        assert 'download' not in attrs
    if tag in ('script', 'img', 'link'):
        target = attrs.get('src', attrs.get('href', ''))
        assert target.startswith('assets/'), f'External/unexpected asset: {target}'
        assert (DOCS / target).is_file(), f'Missing asset: {target}'
buttons = [a for t, a in page.elements if t == 'button']
assert len(buttons) == 6 and sum('disabled' in a for a in buttons) == 5
assert sha256((DOCS / 'assets/EF_Block_Guardian_v0.png').read_bytes()).hexdigest() == 'b9bf927d140acc58e5f58c702065ba91808b652e9d451efb879cdb02db133ddd', 'Approved logo changed'
assert (DOCS / 'assets/Baloo2-Bold.ttf').is_file(), 'Missing local Baloo 2 asset'
assert '@font-face' in css and 'Baloo2-Bold.ttf' in css, 'Guardian mark must use its local font asset'
assert 'guardian-mark' in html and 'guardian-g-top' in html, 'Missing Guardian G1.1 V3 mark'
assert 'viewBox="0 0 144 184"' in html, 'Guardian mark must retain the V3 module'
assert 'Mniej utrudnień w pracy z danymi' in html
assert 'wyników testów' in html
assert not any(p.suffix.lower() in ('.zip', '.xlam', '.pdf', '.docx') for p in DOCS.rglob('*')), 'Release artifact in website'
assert '@media(prefers-reduced-motion:reduce)' in css
assert 'animation:none!important' in css
assert '@media(prefers-reduced-motion:no-preference)' in css
assert 'infinite' not in css
assert not re.search(r'@import|https?://', css)
assert not re.search(r'fetch\(|XMLHttpRequest|localStorage|sessionStorage|document\.cookie', js)
assert 'aria-expanded' in js and "event.key === 'Escape'" in js
assert html.count('class="step-number"') == 4
assert html.count('class="accent"') == 3
print('PASS: distribution boundary, anchors, local assets, approved logo, PL identity, motion guardrails, navigation hooks, content counts.')
