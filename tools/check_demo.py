"""Offline checks for the PL and EN Guardian G1.1 demo routes."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

DOCS = Path(__file__).resolve().parents[1] / 'docs'
MEDIA = '../assets/media/guardian-g1-1/'
VIDEOS = {'windows-direct', 'windows-buffer', 'macos-direct', 'macos-buffer'}


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.elements = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

    def attrs(self, tag):
        return [attrs for name, attrs in self.elements if name == tag]


for lang, home, download, other_demo in (
    ('pl', DOCS, 'pobierz', '../en/demo/'),
    ('en', DOCS / 'en', 'download', '../../demo/'),
):
    path = home / 'demo/index.html'
    page = Page(path)
    assert page.attrs('html') == [{'lang': lang}]
    assert {'href': 'demo/'} in Page(home / 'index.html').attrs('a')
    assert {'href': './', 'aria-current': 'page'} in page.attrs('a')
    assert {'href': other_demo, 'lang': 'en' if lang == 'pl' else 'pl'} in page.attrs('a')
    assert {'href': f'../#{download}', 'class': 'button'} in page.attrs('a')
    for link in page.attrs('a'):
        url = urlsplit(link['href'])
        if url.scheme or url.netloc:
            assert url.scheme == 'mailto', f'Unexpected external demo link: {url.geturl()}'
            continue
        destination = (path.parent / url.path).resolve() if url.path else path
        if destination.is_dir():
            destination /= 'index.html'
        assert destination.is_relative_to(DOCS) and destination.is_file(), link
        if url.fragment:
            assert any(attrs.get('id') == url.fragment for _, attrs in Page(destination).elements), link

    players = page.attrs('video')
    if lang == 'en':
        assert not players and not page.attrs('source') and '.mp4' not in path.read_text(encoding='utf-8')
        assert '<h1 id="demo-title">Coming soon</h1>' in path.read_text(encoding='utf-8')
        continue

    assert len(players) == 4
    assert {player['src'] for player in players} == {f'{MEDIA}{name}.mp4' for name in VIDEOS}
    ids = {attrs['id'] for _, attrs in page.elements if 'id' in attrs}
    for player in players:
        assert 'controls' in player and 'playsinline' in player and 'autoplay' not in player
        assert player.get('preload') == 'none'
        assert set(player['aria-labelledby'].split()) <= ids and player['aria-describedby'] in ids

print('PASS: PL/EN demo routes, locale and download links, four opt-in PL videos, and EN placeholder.')
