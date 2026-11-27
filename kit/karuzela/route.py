"""Generuje HTML paska trasy: route_html(aktualny, wszystkie, etykieta_mala, tekst)."""
def route_html(cur, total, small, text):
    w, y = 330, 56
    xs = [20 + i * (w - 40) / (total - 1) for i in range(total)]
    dots = ''
    for i, x in enumerate(xs, 1):
        fill = '#0f2a43' if i < cur else ('#ffc23c' if i == cur else '#ffffff')
        stroke = '#0f2a43'
        r = 13 if i == cur else 9
        dots += f'<circle cx="{x:.0f}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
    done = f'<line x1="{xs[0]:.0f}" y1="{y}" x2="{xs[cur-1]:.0f}" y2="{y}" stroke="#0f2a43" stroke-width="4"/>'
    rest = f'<line x1="{xs[cur-1]:.0f}" y1="{y}" x2="{xs[-1]:.0f}" y2="{y}" stroke="#0f2a43" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>'
    px = xs[cur - 1]
    plane = (f'<g transform="translate({px - 26:.0f},{y - 52})">'
             '<path d="M0,22 L40,18 C48,17 54,19 56,22 C54,25 48,27 40,26 L0,24 Z" fill="#1592d1"/>'
             '<path d="M22,22 L12,36 L19,36 L33,23 Z" fill="#1592d1"/><path d="M3,22 L-3,12 L2,12 L10,20 Z" fill="#ff6b4a"/></g>')
    svg = f'<svg width="{w}" height="112" viewBox="0 0 {w} 112">{rest}{done}{dots}{plane}</svg>'
    return f'<div class="route"><div class="lbl"><small>{small}</small><span>{text}</span></div>{svg}</div>'
