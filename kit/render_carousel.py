"""Renderuje karuzelę: python3 render_carousel.py KATALOG PREFIKS [LICZBA_SLAJDÓW]
KATALOG zawiera s1.html..sN.html (1080x1350). Wynik: KATALOG/PREFIKS-1..N.jpg + contact.jpg (podgląd)."""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
d = os.path.abspath(sys.argv[1]); pre = sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 4
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for i in range(1, n + 1):
        pg.goto(f'file://{d}/s{i}.html'); pg.wait_for_timeout(600)
        pg.screenshot(path=f'{d}/tmp.png')
        Image.open(f'{d}/tmp.png').convert('RGB').save(f'{d}/{pre}-{i}.jpg', 'JPEG', quality=92)
    b.close()
os.remove(f'{d}/tmp.png')
sh = Image.new('RGB', (550 * n - 10, 675), 'white')
for i in range(n): sh.paste(Image.open(f'{d}/{pre}-{i+1}.jpg').resize((540, 675)), (550 * i, 0))
sh.save(f'{d}/contact.jpg', quality=85); print('ok', n)
