"""Offline checks for the Guardian G1.1 Pilot SEO readiness candidate."""
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
HOME = 'https://excelforge.eu/'
EN_HOME = 'https://excelforge.eu/en/'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def elements(name):
    parser = Page()
    parser.feed((DOCS / name).read_text())
    return parser.elements


def has_link(items, rel, href, **extra):
    return any(
        tag == 'link'
        and attrs.get('rel') == rel
        and attrs.get('href') == href
        and all(attrs.get(key) == value for key, value in extra.items())
        for tag, attrs in items
    )


pl, en = elements('index.html'), elements('en/index.html')
for items, canonical in ((pl, HOME), (en, EN_HOME)):
    assert not any(tag == 'meta' and attrs.get('name') == 'robots' and 'noindex' in attrs.get('content', '') for tag, attrs in items), 'Homepage carries noindex'
    assert has_link(items, 'canonical', canonical), f'Missing canonical {canonical}'
    assert has_link(items, 'alternate', HOME, hreflang='pl'), 'Missing Polish alternate'
    assert has_link(items, 'alternate', EN_HOME, hreflang='en'), 'Missing English alternate'
    assert has_link(items, 'alternate', HOME, hreflang='x-default'), 'Missing default alternate'
    assert any(tag == 'meta' and attrs.get('property') == 'og:type' and attrs.get('content') == 'website' for tag, attrs in items), 'Missing Open Graph website type'
    assert any(tag == 'meta' and attrs.get('property') == 'og:site_name' and attrs.get('content') == 'ExcelForge' for tag, attrs in items), 'Missing Open Graph site name'
    assert any(tag == 'meta' and attrs.get('property') == 'og:url' and attrs.get('content') == canonical for tag, attrs in items), 'Open Graph URL differs from canonical'

for name in ('licencja.html', 'prywatnosc.html', 'en/terms.html', 'en/privacy.html'):
    items = elements(name)
    assert any(tag == 'meta' and attrs.get('name') == 'robots' and attrs.get('content') == 'noindex, nofollow' for tag, attrs in items), f'Legal page should remain directly accessible but noindex: {name}'

robots = (DOCS / 'robots.txt').read_text()
assert 'User-agent: *' in robots and 'Allow: /' in robots
assert 'Sitemap: https://excelforge.eu/sitemap.xml' in robots
root = ElementTree.parse(DOCS / 'sitemap.xml').getroot()
namespace = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [node.text for node in root.findall('s:url/s:loc', namespace)]
assert urls == [HOME, EN_HOME], f'Unexpected sitemap URLs: {urls}'
print('PASS: PL/EN home indexability, canonicals, hreflang, sitemap, robots policy, and legal noindex boundary.')
