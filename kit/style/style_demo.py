import sys
import os; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','karuzela'))
from route import route_html
R=route_html(2,4,'NASTĘPNY PRZYSTANEK','Wielki start: 27–28.11')
HEAD='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="common.css"><style>.pill{position:absolute;top:52px;right:64px}%s</style></head><body>%s</body></html>'
LOGO='<div class="logo" style="color:#fff">mytravel<b style="color:#ffd400">cast</b>.com</div>'
rows=[('Wiedeń','Rathausplatz','13.11–26.12'),('Tallinn','Stare Miasto','20.11–6.01'),('Drezno','Striezelmarkt','25.11–24.12')]
def w(n,css,body): open(f's{n}.html','w').write(HEAD%(css,body))
# A – karty (obecny)
w(1,'''body{background:linear-gradient(160deg,#ff3d1f,#e0102f)}.pill{background:#0a2238}
h2{position:absolute;left:64px;top:150px;font-family:IDK;font-size:92px;line-height:1;color:#fff;letter-spacing:-1.8px}
h2 .hl{background:#ffd400;color:#0a2238;padding:0 14px 4px;border-radius:14px;display:inline-block;margin-top:10px;transform:rotate(-1.5deg)}
.rows{position:absolute;left:64px;right:64px;top:420px;display:flex;flex-direction:column;gap:22px}
.row{background:#fff;border-radius:28px;padding:34px;display:flex;justify-content:space-between;align-items:center}
.k{font-family:IDK;font-size:50px;color:#0a2238}.k small{display:block;font-family:IDS;font-size:26px;color:#4d6478}
.v{font-family:IDK;font-size:44px;background:#ffe1d9;color:#d42a0c;border-radius:16px;padding:10px 20px}''',
LOGO+'<span class="pill">STYL A · KARTY</span><h2>Ruszają<br><span class="hl">w&nbsp;listopadzie</span></h2><div class="rows">'+''.join(f'<div class="row"><div class="k">{a}<small>{b}</small></div><div class="v">{c}</div></div>' for a,b,c in rows)+'</div>'+R)
# B – pasy: zdjęcie u góry, kolorowy blok, tekst bez białych podkładów
w(2,'''body{background:#0057ff}.pill{background:#ff2e88}
.ph{position:absolute;left:0;right:0;top:0;height:600px;background:url(praga.jpg) center/cover}
.ph:after{content:'';position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(0,20,60,.55),rgba(0,0,0,0))}
svg.cut{position:absolute;left:0;top:510px}
.blk{position:absolute;left:64px;right:64px;top:620px}
h2{font-family:IDK;font-size:78px;line-height:1;color:#ffe600;letter-spacing:-1.5px}
.l{display:flex;align-items:baseline;justify-content:space-between;border-bottom:3px solid rgba(255,255,255,.35);padding:26px 0}
.k{font-family:IDK;font-size:56px;color:#fff}.k small{font-family:IDS;font-size:26px;color:#bcd3ff;margin-left:14px}
.v{font-family:IDK;font-size:56px;color:#ffe600}''',
'<div class="ph"></div><svg class="cut" width="1080" height="120" viewBox="0 0 1080 120"><path d="M0,60 L1080,0 L1080,120 L0,120 Z" fill="#0057ff"/></svg>'+LOGO+'<span class="pill">STYL B · PASY</span><div class="blk"><h2>Ruszają w&nbsp;listopadzie</h2>'+''.join(f'<div class="l"><div class="k">{a}<small>{b}</small></div><div class="v">{c}</div></div>' for a,b,c in rows)+'</div>'+R)
# C – naklejki na pełnym zdjęciu
w(3,'''body{background:#123 url(praga_tall.jpg) center/cover}.pill{background:#00c2a8}
.fade{position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(180deg,rgba(0,20,40,.55),rgba(0,0,0,0))}
h2{position:absolute;left:56px;top:150px;font-family:IDK;font-size:86px;line-height:1.05;color:#fff;text-shadow:0 4px 20px rgba(0,0,0,.5)}
.st{position:absolute;left:56px;font-family:IDK;color:#0a2238;padding:16px 26px;border-radius:12px;box-shadow:0 10px 26px rgba(0,0,0,.35);font-size:44px}
.st small{display:block;font-family:IDX;font-size:26px;letter-spacing:2px;opacity:.8}''',
'<div class="fade"></div>'+LOGO+'<span class="pill">STYL C · NAKLEJKI</span><h2>Ruszają<br>w&nbsp;listopadzie</h2>'
'<div class="st" style="top:420px;background:#ffe600;transform:rotate(-3deg)"><small>WIEDEŃ</small>13.11–26.12</div>'
'<div class="st" style="top:600px;left:380px;background:#ff5fa2;color:#fff;transform:rotate(2.5deg)"><small>TALLINN</small>20.11–6.01</div>'
'<div class="st" style="top:790px;left:120px;background:#3ee0ff;transform:rotate(-1.5deg)"><small>DREZNO</small>25.11–24.12</div>'+R)
# D – plakat: gradient, wielkie daty, zdjęcie w kole
w(4,'''body{background:linear-gradient(135deg,#ff6a00 0%,#ff0f7b 100%)}.pill{background:#0a2238}
.circ{position:absolute;right:-90px;top:120px;width:520px;height:520px;border-radius:50%;background:url(wieden.jpg) center 35%/cover;border:14px solid #ffe600}
h2{position:absolute;left:64px;top:170px;font-family:IDK;font-size:80px;line-height:1;color:#fff;width:520px}
.big{position:absolute;left:64px;right:64px;top:640px}
.b{display:flex;align-items:baseline;gap:22px;margin-bottom:6px}
.d{font-family:IDK;font-size:104px;letter-spacing:-3px;color:transparent;-webkit-text-stroke:4px #fff;line-height:1.1}
.c{font-family:IDK;font-size:46px;color:#ffe600}.c small{display:block;font-family:IDS;font-size:26px;color:#fff}''',
LOGO+'<span class="pill">STYL D · PLAKAT</span><div class="circ"></div><h2>Ruszają w&nbsp;listopadzie</h2><div class="big">'+''.join(f'<div class="b"><div class="d">{c.split("–")[0]}</div><div class="c">{a}<small>do {c.split("–")[1]}</small></div></div>' for a,b,c in rows)+'</div>'+R)
