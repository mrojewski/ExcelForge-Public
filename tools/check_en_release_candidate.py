"""Offline guardrails for the local Guardian G1.1 EN release candidate."""
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EN = DOCS / "en"
PUBLIC_RELEASE = "https://github.com/mrojewski/ExcelForge-Public/releases"
RELEASE_TAG = f"{PUBLIC_RELEASE}/tag/guardian-g1-1-pilot"
RELEASE_DOWNLOAD = f"{PUBLIC_RELEASE}/download/guardian-g1-1-pilot"
WINDOWS_GUIDE = f"{RELEASE_DOWNLOAD}/ExcelForge_Guardian_G1_1_Windows_Installation_Pilot_EN_rev1_0_FINAL.pdf"
MACOS_GUIDE = f"{RELEASE_DOWNLOAD}/ExcelForge_Guardian_G1_1_macOS_Installation_Pilot_EN_rev1_0_FINAL.pdf"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.elements = []

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


def parse(path):
    text = path.read_text()
    page = Page()
    page.feed(text)
    return text, page


pl_html, pl_page = parse(DOCS / "index.html")
en_html, en_page = parse(EN / "index.html")
ids = [attrs["id"] for _, attrs in en_page.elements if "id" in attrs]
assert len(ids) == len(set(ids)), "Duplicate EN IDs"
assert ("html", {"lang": "en"}) in en_page.elements
assert not any(tag == 'meta' and attrs.get('name') == 'robots' and 'noindex' in attrs.get('content', '') for tag, attrs in en_page.elements), 'EN homepage must be indexable'
assert not re.search(r"[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]", en_html), "Polish copy remains in EN homepage"
assert "href=\"../index.html\" lang=\"pl\"" in en_html, "Missing EN-to-PL switch"
assert "href=\"en/index.html\" lang=\"en\"" in pl_html, "Missing PL-to-EN switch"
assert en_html.count('<section') == pl_html.count('<section'), "PL/EN homepage section count differs"
assert en_html.count('<article') == pl_html.count('<article'), "PL/EN homepage article count differs"
assert en_html.count('class="download-card"') == pl_html.count('class="download-card"') == 2
assert en_html.count('class="step-number"') == pl_html.count('class="step-number"') == 4
assert en_html.count('class="accent"') == pl_html.count('class="accent"') == 3
assert en_html.count('class="platform-identifier"') == 2
assert en_html.count('Installation guide (PDF)') == 2
assert WINDOWS_GUIDE in en_html and MACOS_GUIDE in en_html, "Guide release URLs differ"
assert '../guides/' not in en_html, "Local guide fixture link remains"
assert "The English documents are informational translations; their Polish-language versions are authoritative." in en_html
assert 'href="terms.html"' in en_html and 'href="privacy.html"' in en_html
assert 'Guardian G1.1 Pilot — controlled Excel data splitting for Windows and macOS.' in en_html
assert '<title>Guardian G1.1 Pilot — controlled Excel data splitting | ExcelForge</title>' in en_html
assert '<link rel="canonical" href="https://excelforge.eu/en/">' in en_html
assert '<link rel="alternate" hreflang="pl" href="https://excelforge.eu/">' in en_html
assert '<link rel="alternate" hreflang="en" href="https://excelforge.eu/en/">' in en_html

allowed_external = {
    RELEASE_TAG,
    f"{RELEASE_DOWNLOAD}/ExcelForge_Guardian_G1.1_Windows_Pilot.zip",
    f"{RELEASE_DOWNLOAD}/ExcelForge_Guardian_G1.1_macOS_Pilot.zip",
    WINDOWS_GUIDE,
    MACOS_GUIDE,
}
allowed_local = {'../index.html', 'terms.html', 'privacy.html'}
for tag, attrs in en_page.elements:
    if tag == 'a':
        target = attrs.get('href', '')
        assert target, 'Empty EN link'
        if target.startswith('#'):
            assert target[1:] in ids, f'Missing EN anchor: {target}'
        elif target.startswith('mailto:'):
            assert target.split('?')[0] == 'mailto:support@excelforge.eu', f'Unexpected mail link: {target}'
        elif target in allowed_local:
            assert (EN / target).resolve().is_file(), f'Missing EN local link: {target}'
        else:
            assert target in allowed_external, f'Unexpected EN link: {target}'
    if tag in ('script', 'img') or (tag == 'link' and attrs.get('rel') in ('stylesheet', 'icon')):
        target = attrs.get('src', attrs.get('href', ''))
        assert target.startswith('../assets/'), f'Unexpected EN asset path: {target}'
        assert (EN / target).resolve().is_file(), f'Missing EN asset: {target}'

assert sha256((DOCS / 'licencja.html').read_bytes()).hexdigest() == 'd128e776246ae2d801c69c4ffeedd3b401c18cdb0011dbe0ae52f472703fb630', 'Terms PL baseline changed'
assert sha256((DOCS / 'prywatnosc.html').read_bytes()).hexdigest() == '927a1459e2e889b5f603aa4a1bc60d21b6cb9bd748d471592eac7723446d0ab9', 'Privacy PL baseline changed'

for pl_name, en_name, authority_link, title in (
    ('licencja.html', 'terms.html', '../licencja.html', 'Terms of Use'),
    ('prywatnosc.html', 'privacy.html', '../prywatnosc.html', 'Privacy Notice'),
):
    pl_text, pl_page = parse(DOCS / pl_name)
    en_text, legal_page = parse(EN / en_name)
    pl_ids = {attrs['id'] for _, attrs in pl_page.elements if 'id' in attrs}
    en_ids = {attrs['id'] for _, attrs in legal_page.elements if 'id' in attrs}
    assert pl_ids == en_ids, f'PL/EN legal IDs differ: {en_name}'
    assert en_text.count('<section') == pl_text.count('<section'), f'PL/EN legal sections differ: {en_name}'
    assert en_text.count('<h2') == pl_text.count('<h2') == 9, f'Legal headings differ: {en_name}'
    assert en_text.count('<p') == pl_text.count('<p') + 1, f'Unexpected EN legal paragraph: {en_name}'
    assert 'This English translation is provided for information purposes only.' in en_text
    assert 'is authoritative and prevails in the event of any discrepancy.' in en_text
    assert f'href="{authority_link}" lang="pl"' in en_text
    assert title in en_text and 'Effective from 22 September 2026.' in en_text
    assert not re.search(r'[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', en_text), f'Polish copy remains in {en_name}'

terms = (EN / 'terms.html').read_text()
privacy = (EN / 'privacy.html').read_text()
assert 'not open-source software' in terms
assert 'official ExcelForge download channel' in terms
assert 'unmodified, modified, repackaged' in terms
assert 'reverse engineering' in terms and 'interoperability' in terms
assert 'No provision of these Terms is intended to exclude or limit' in terms
assert 'up to 12 months after the matter is closed' in privacy
assert 'only Marcin Rojewski has access' in privacy
assert 'Zoho Mail in a European data centre' in privacy
assert 'Standard Contractual Clauses' in privacy
assert 'https://www.zoho.com/privacy/privacy-faq.html' in privacy
assert 'Cloudflare Web Analytics' in privacy
assert 'Cloudflare Customer DPA' in privacy
assert 'custom events, forms, remarketing, or user profiling' in privacy
for page in DOCS.rglob('*.html'):
    source = page.read_text()
    assert 'static.cloudflareinsights.com' not in source and 'data-cf-beacon' not in source, f'Manual Cloudflare beacon found in Pages source: {page.relative_to(DOCS)}'
assert not any(path.suffix.lower() in ('.zip', '.xlam', '.pdf', '.docx') for path in DOCS.rglob('*')), 'Release artifact found in website tree'
print('PASS: EN/PL structure, current legal and Cloudflare-analytics baselines, language authority, intended Release URLs, and clean Pages boundary.')
