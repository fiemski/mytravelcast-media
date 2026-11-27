"""Renderuje Story: python3 render_story.py PLIK.html WYNIK.jpg (1080x1920)."""
import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
src = os.path.abspath(sys.argv[1]); out = sys.argv[2]; tmp = out + '.png'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto('file://' + src); pg.wait_for_timeout(700); pg.screenshot(path=tmp); b.close()
Image.open(tmp).convert('RGB').save(out, 'JPEG', quality=92); os.remove(tmp); print('ok')
