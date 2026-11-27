"""Zrzut mapy mytravelcast.com w przeglądarce bezgłowej.
Użycie: python3 mtc_shot.py REGION MIESIĄC WYJŚCIE.png [szer] [wys]
REGION: ŚWIAT/EUROPA/AFRYKA/AZJA/AMERYKI/OCEANIA, MIESIĄC: STY..GRU
Podstawia d3 i fonty DM z lokalnych plików (CDN zablokowane w środowisku)."""
import sys, glob, os
from playwright.sync_api import sync_playwright
V = os.environ.get('MTC_VENDOR', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendor'))
region, month, out = sys.argv[1], sys.argv[2], sys.argv[3]
W = int(sys.argv[4]) if len(sys.argv) > 4 else 1600
H = int(sys.argv[5]) if len(sys.argv) > 5 else 1000
d3 = open(f'{V}/d3-7.8.5/package/dist/d3.min.js', 'rb').read()
def fontcss():
    css = ''
    for fam, pkg in (('DM Sans', 'fontsource-dm-sans-5.3.0'), ('DM Mono', 'fontsource-dm-mono-5.3.0')):
        for f in sorted(glob.glob(f'{V}/{pkg}/package/files/*-normal.woff2')):
            name = os.path.basename(f)
            if '-latin-' not in name and '-latin-ext-' not in name: continue
            w = name.split('-')[-2]
            css += "@font-face{font-family:'%s';font-weight:%s;font-style:normal;src:url('https://localfont/%s/%s') format('woff2');}\n" % (fam, w, pkg, name)
    return css
CSS = fontcss()
import re, subprocess, tarfile
def npm_file(spec, path):
    safe = spec.replace('/', '_').replace('@', '_')
    d = f'{V}/npm_{safe}'
    if not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
        out = subprocess.run(['npm', 'pack', spec, '--silent', '--pack-destination', d], capture_output=True, text=True)
        tgz = glob.glob(f'{d}/*.tgz')[0]
        with tarfile.open(tgz) as t: t.extractall(d, filter='data')
    f = f'{d}/package/{path}'
    return open(f, 'rb').read() if os.path.isfile(f) else None
def route(r):
    u = r.request.url
    m = re.match(r'https://cdn\.jsdelivr\.net/npm/((?:@[^/]+/)?[^/@]+@[^/]+)/(.+?)(?:\?.*)?$', u)
    if m:
        body = npm_file(m.group(1), m.group(2))
        if body is not None:
            ct = 'application/json' if u.endswith('.json') else 'application/javascript'
            return r.fulfill(status=200, body=body, content_type=ct)
        return r.abort()
    if 'fonts.googleapis.com' in u: return r.fulfill(status=200, body=CSS, content_type='text/css')
    if u.startswith('https://localfont/'):
        pkg, name = u.split('/')[-2:]
        return r.fulfill(status=200, body=open(f'{V}/{pkg}/package/files/{name}','rb').read(), content_type='font/woff2')
    if 'googletagmanager' in u or 'er-api.com' in u: return r.abort()
    return r.continue_()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=2, locale='pl-PL')
    fails = []
    pg.on('requestfailed', lambda q: fails.append(q.url[:120]))
    pg.route('**/*', route)
    pg.goto('https://mytravelcast.com/?lang=pl', wait_until='networkidle', timeout=60000)
    pg.wait_for_timeout(1500)
    pg.locator('#map-cta-label').click(force=True)
    pg.wait_for_timeout(4000)
    for t in ('Pomiń', 'Skip'):
        loc = pg.get_by_text(t, exact=True)
        if loc.count():
            try: loc.first.click(force=True)
            except Exception: pass
    pg.wait_for_timeout(800)
    loc = pg.get_by_role('button', name=re.compile('^'+region+'$', re.I))
    print('region', loc.count())
    if loc.count(): loc.first.click(force=True)
    pg.wait_for_timeout(2500)
    loc = pg.get_by_text(re.compile('^'+month+'$', re.I))
    print('month', loc.count())
    if loc.count(): loc.last.click(force=True)
    STYLE = os.environ.get('STYLE')
    if STYLE:
        st = pg.get_by_role('button', name=re.compile('^'+STYLE+'$', re.I))
        print('style', st.count())
        if st.count(): st.first.click(force=True)
        pg.wait_for_timeout(2500)
    pg.wait_for_timeout(1500)
    SHIFT = int(os.environ.get('SHIFT', '0'))
    if SHIFT:
        rng = pg.locator('input[type=range]').first
        rng.focus()
        for _ in range(abs(SHIFT)):
            pg.keyboard.press('ArrowRight' if SHIFT > 0 else 'ArrowLeft')
            pg.wait_for_timeout(40)
        print('window:', pg.evaluate("[...document.querySelectorAll('*')].map(e=>e.innerText||'').filter(t=>/KIEDY JEDZIESZ/i.test(t)&&t.length<80)[0]||''"))
    pg.wait_for_timeout(3000)
    pg.screenshot(path=out)
    print('failed:', fails)
    b.close()
