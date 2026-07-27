# -*- coding: utf-8 -*-
# Сборщик прототипа сайта «Настоящие отношения». v2: иконки, инфографика, журнальная сетка.
import re
import pathlib

ROOT = pathlib.Path(__file__).parent

# ============ ИКОНКИ (линейные, stroke=currentColor) ============
def ic(body, vb=48):
    return (f'<svg class="ic" viewBox="0 0 {vb} {vb}" fill="none" stroke="currentColor" '
            f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')

ICONS = {
# книга: понимание без изменений
"book": ic('<path d="M24 12c-4-3-10-4-15-3v26c5-1 11 0 15 3 4-3 10-4 15-3V9c-5-1-11 0-15 3z"/><path d="M24 12v26"/>'),
# петля-повтор
"loop": ic('<path d="M14 18a12 12 0 0 1 21 6"/><path d="M34 30a12 12 0 0 1-21-6"/><path d="M35 15v9h-9"/><path d="M13 33v-9h9"/>'),
# щит с трещиной: сильный снаружи
"shield": ic('<path d="M24 6l14 5v11c0 9-6 16-14 20-8-4-14-11-14-20V11z"/><path d="M24 14l-3 7h6l-4 9"/>'),
# две чашки: быт
"cups": ic('<path d="M8 20h12v7a6 6 0 0 1-12 0z"/><path d="M28 20h12v7a6 6 0 0 1-12 0z"/><path d="M20 22h3M40 22h3"/><path d="M10 38h28"/>'),
# стрелка в потолок
"ceiling": ic('<path d="M8 10h32"/><path d="M24 38V18"/><path d="M17 25l7-7 7 7"/><path d="M14 14l-2-2M34 14l2-2"/>'),
# линза-знак
"lens": ic('<circle cx="19" cy="24" r="12"/><circle cx="29" cy="24" r="12"/>'),
# слои: глубина
"layers": ic('<path d="M24 8l16 8-16 8-16-8z"/><path d="M8 24l16 8 16-8"/><path d="M8 32l16 8 16-8"/>'),
# люди кругом: группа
"people": ic('<circle cx="24" cy="14" r="5"/><circle cx="10" cy="30" r="5"/><circle cx="38" cy="30" r="5"/><path d="M17 20l-3 5M31 20l3 5M16 34h16"/>'),
# календарь-практика
"calendar": ic('<rect x="8" y="10" width="32" height="30" rx="3"/><path d="M8 18h32M16 6v8M32 6v8"/><path d="M17 28l5 5 9-10"/>'),
# речь: разговор
"speech": ic('<path d="M8 12h32v20H22l-8 8v-8H8z"/><path d="M15 20h18M15 26h12"/>'),
# механизм
"gear": ic('<circle cx="24" cy="24" r="7"/><path d="M24 8v6M24 34v6M8 24h6M34 24h6M13 13l4 4M31 31l4 4M35 13l-4 4M17 31l-4 4"/>'),
# развилка-путь
"route": ic('<path d="M12 40V22a8 8 0 0 1 8-8h16"/><path d="M30 8l6 6-6 6"/><circle cx="12" cy="43" r="2.4"/>'),
# цель
"target": ic('<circle cx="24" cy="24" r="16"/><circle cx="24" cy="24" r="9"/><circle cx="24" cy="24" r="2.4"/>'),
# рассвет: утро
"sunrise": ic('<path d="M8 34h32"/><path d="M16 34a8 8 0 0 1 16 0"/><path d="M24 12v6M12 20l3 3M36 20l-3 3"/>'),
# гора: опора
"mountain": ic('<path d="M6 38l12-20 7 11 5-7 12 16z"/><path d="M18 18l3 5"/>'),
# монеты: деньги и дело
"coins": ic('<circle cx="18" cy="30" r="10"/><circle cx="30" cy="18" r="10"/><path d="M27 18h6M30 15v6"/>'),
# пламя: энергия
"flame": ic('<path d="M24 6c2 6 10 10 10 19a10 10 0 0 1-20 0c0-5 3-8 5-11 1 3 2 4 5 6 0-6-2-9 0-14z"/>'),
# маятник: реакция кормит
"pendulum": ic('<path d="M10 8h28"/><path d="M24 8v7"/><path d="M24 15 L33 33"/><circle cx="34.5" cy="37" r="4.5"/><path d="M13 30a17 17 0 0 1 2-12" stroke-dasharray="2.6 4.4"/>'),
# зеркало мира
"mirror": ic('<ellipse cx="24" cy="23" rx="11" ry="15"/><path d="M19.5 14.5c-2.2 2.6-2.8 7-1.6 10.4"/><path d="M13 41h22M24 38v3"/>'),
# лампа: открытие, наука
"lamp": ic('<path d="M15 19a9 9 0 1 1 18 0c0 5-4 6.5-5 10h-8c-1-3.5-5-5-5-10z"/><path d="M20 34h8M21 39h6"/><path d="M24 6v3M10 19h3M35 19h3"/>'),
# песочные часы: 90 секунд
"hourglass": ic('<path d="M14 7h20M14 41h20"/><path d="M16 7c0 8 5.5 10 8 17-2.5 7-8 9-8 17M32 7c0 8-5.5 10-8 17 2.5 7 8 9 8 17"/>'),
}

def icon(name, color="var(--wine)"):
    return f'<span class="icwrap" style="color:{color}">{ICONS[name]}</span>'

# ============ ИНФОГРАФИКА ============
def loop_diagram(dark=False):
    ring = "#D08A5F" if dark else "#6E3B4B"
    soft = "rgba(242,237,228,.75)" if dark else "#6B615C"
    node_bg = "#22303C" if dark else "#FFFFFF"
    node_line = "rgba(208,138,95,.45)" if dark else "rgba(110,59,75,.3)"
    txt = "#F2EDE4" if dark else "#322D2B"
    sage = "#8FA48B" if dark else "#7D8C74"
    halo = "#17222C" if dark else "#FAF7F2"
    def node(x, y, num, label, cap, anchor="middle"):
        return f'''
<g>
<circle cx="{x}" cy="{y}" r="34" fill="{node_bg}" stroke="{node_line}" stroke-width="1.5"><animate attributeName="r" values="34;36;34" dur="4s" begin="{num}.8s" repeatCount="indefinite"/></circle>
<text x="{x}" y="{y+9}" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="26" fill="{ring}">{num}</text>
</g>
<text x="{x}" y="{y-48}" text-anchor="{anchor}" font-family="Manrope,sans-serif" font-weight="700" font-size="16" fill="{txt}" stroke="{halo}" stroke-width="6" paint-order="stroke" stroke-linejoin="round">{label}</text>
<text x="{x}" y="{y-30}" text-anchor="{anchor}" font-family="Manrope,sans-serif" font-size="12.5" fill="{soft}" stroke="{halo}" stroke-width="5" paint-order="stroke" stroke-linejoin="round">{cap}</text>'''
    return f'''<svg viewBox="0 0 520 560" role="img" aria-label="Событийный круг: событие, эмоция, старое решение, сценарий" style="max-width:520px;width:100%;height:auto">
<circle cx="260" cy="290" r="150" fill="none" stroke="{ring}" stroke-width="1.6" stroke-dasharray="3 7" opacity=".8"/>
<g fill="{ring}">
<path d="M398 217 l14 -3 -6 13 z"/>
<path d="M330 425 l-3 14 12 -7 z"/>
<path d="M122 363 l-14 3 6 -13 z"/>
<path d="M190 155 l3 -14 -12 7 z"/>
</g>
{node(260, 140, "1", "Событие", "слово, взгляд, цифра на счёте")}
{node(410, 290, "2", "Эмоция", "тело вспыхивает раньше мысли")}
{node(260, 440, "3", "Старое решение", "принятое когда-то, чаще в детстве")}
{node(110, 290, "4", "Сценарий", "финал знакомый, круг замыкается")}
<text x="260" y="285" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="19" fill="{txt}">Событийный</text>
<text x="260" y="308" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="19" fill="{txt}">круг</text>
<text x="260" y="330" text-anchor="middle" font-family="Manrope,sans-serif" font-size="12" fill="{sage}">быстрее сознания</text>
</svg>'''

def timeline_svg():
    return '''<svg viewBox="0 0 980 190" role="img" aria-label="Путь программы: три модуля с перерывами 3-5 недель" style="width:100%;height:auto">
<line x1="60" y1="70" x2="920" y2="70" stroke="rgba(110,59,75,.25)" stroke-width="2" stroke-dasharray="2 6"/>
<g font-family="Manrope,sans-serif">
<circle cx="110" cy="70" r="30" fill="#6E3B4B"/>
<text x="110" y="79" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="24" fill="#FAF5F0">I</text>
<text x="110" y="128" text-anchor="middle" font-weight="700" font-size="15" fill="#322D2B">Возвращение к себе</text>
<text x="110" y="148" text-anchor="middle" font-size="13" fill="#6B615C">2,5 дня очно</text>
<text x="255" y="52" text-anchor="middle" font-size="12.5" fill="#7D8C74">3-5 недель</text>
<text x="255" y="92" text-anchor="middle" font-size="11.5" fill="#6B615C">интеграция</text>
<circle cx="400" cy="70" r="30" fill="#6E3B4B"/>
<text x="400" y="79" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="24" fill="#FAF5F0">II</text>
<text x="400" y="128" text-anchor="middle" font-weight="700" font-size="15" fill="#322D2B">Внутренняя свобода</text>
<text x="400" y="148" text-anchor="middle" font-size="13" fill="#6B615C">5 дней очно</text>
<text x="545" y="52" text-anchor="middle" font-size="12.5" fill="#7D8C74">3-5 недель</text>
<text x="545" y="92" text-anchor="middle" font-size="11.5" fill="#6B615C">интеграция</text>
<circle cx="690" cy="70" r="30" fill="#17222C"/>
<text x="690" y="79" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="22" fill="#D08A5F">III</text>
<text x="690" y="128" text-anchor="middle" font-weight="700" font-size="15" fill="#322D2B">Создатель реальности</text>
<text x="690" y="148" text-anchor="middle" font-size="13" fill="#6B615C">3 месяца в жизни</text>
<path d="M735 70h120" stroke="#D08A5F" stroke-width="3"/>
<path d="M845 62l14 8-14 8z" fill="#D08A5F"/>
<text x="800" y="52" text-anchor="middle" font-size="12.5" fill="#D08A5F">результаты остаются</text>
</g>
</svg>'''

FAVICON = ("data:image/svg+xml,"
  "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
  "%3Ccircle cx='38' cy='50' r='28' fill='none' stroke='%237D8C74' stroke-width='6'/%3E"
  "%3Ccircle cx='62' cy='50' r='28' fill='none' stroke='%236E3B4B' stroke-width='6'/%3E"
  "%3Cpath d='M50 24.7 A28 28 0 0 1 50 75.3 A28 28 0 0 1 50 24.7 Z' fill='%236E3B4B'/%3E%3C/svg%3E")

CSS = """
@font-face{font-family:'Playfair Display';src:url('/chizhovy2/fonts/playfair-cyrillic.woff2') format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;font-weight:400 900;font-display:swap}
@font-face{font-family:'Playfair Display';src:url('/chizhovy2/fonts/playfair-latin.woff2') format('woff2');unicode-range:U+0000-00FF,U+2000-206F;font-weight:400 900;font-display:swap}
@font-face{font-family:'Manrope';src:url('/chizhovy2/fonts/manrope-cyrillic.woff2') format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;font-weight:200 800;font-display:swap}
@font-face{font-family:'Manrope';src:url('/chizhovy2/fonts/manrope-latin.woff2') format('woff2');unicode-range:U+0000-00FF,U+2000-206F;font-weight:200 800;font-display:swap}
:root{--bg:#FAF7F2;--ink:#322D2B;--ink-soft:#6B615C;--wine:#6E3B4B;--wine-deep:#552C3A;--sage:#7D8C74;--sage-deep:#5C6B54;--linen:#EFE9DF;--sand:#C9A87C;--line:rgba(110,59,75,.14);--night:#17222C;--night2:#22303C;--copper:#D08A5F;--ntext:#F2EDE4;color-scheme:light}
*{box-sizing:border-box}
html{font-size:17px;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Manrope',-apple-system,'Segoe UI',sans-serif;line-height:1.72;-webkit-font-smoothing:antialiased;overflow-x:clip}
svg{max-width:100%}
img{max-width:100%;display:block}
a{color:var(--wine)}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.narrow{max-width:1080px;margin:0 auto;padding:0 24px}
.narrow>*{max-width:720px}
/* Двухколоночный разворот: текст слева, врезка справа. Правая пустота заполняется смыслом */
.tside{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:56px;align-items:start}
.tside>.col{min-width:0}
.tside>.col>*{max-width:660px}
.side{min-width:0;position:sticky;top:96px}
.side .box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px 22px 20px}
.side .box+.box{margin-top:14px}
.side .lbl{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--copper);margin-bottom:10px}
.side .big{font-family:'Playfair Display',Georgia,serif;font-size:2.2rem;line-height:1;color:var(--wine);margin-bottom:8px}
.side p{font-size:.9rem;line-height:1.55;color:var(--ink-soft);margin:0}
.side .cit{font-family:'Lora',Georgia,serif;font-style:italic;font-size:.98rem;line-height:1.5;color:var(--ink)}
.side .who{font-size:.78rem;color:var(--ink-soft);margin-top:8px}
.side img{width:100%;border-radius:10px;display:block}
.side .cap{font-size:.78rem;color:var(--ink-soft);margin-top:8px}
.dark .side .box{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.13)}
.dark .side .cit,.dark .side .big{color:#fff}
.dark .side p,.dark .side .who,.dark .side .cap{color:rgba(255,255,255,.72)}
@media (max-width:980px){
  .tside{grid-template-columns:1fr;gap:24px}
  .side{position:static}
  .tside>.col>*{max-width:none}
}
h1,h2,h3,h4{font-family:'Playfair Display',Georgia,serif;line-height:1.2;text-wrap:balance;margin:0 0 .5em}
/* Держим последнюю пару слов заголовка вместе там, где она влезает в колонку */
.kp{white-space:nowrap}@media (max-width:980px){.kp{white-space:normal}}
.kpm{white-space:nowrap}@media (max-width:399px){.kpm{white-space:normal}}
h2{font-size:clamp(1.7rem,4vw,2.3rem);font-weight:600}
h3{font-size:1.22rem;font-weight:600}
p{margin:0 0 1.1em}
p,li,figcaption,blockquote,dd,dt,summary,td,th{text-wrap:pretty}
section{padding:76px 0}
.eyebrow{font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--wine);margin:0 0 16px;display:flex;align-items:center;gap:10px}
.eyebrow::before{content:'';width:26px;height:2px;background:var(--sand)}
.hero .eyebrow::before{display:none}
.center .eyebrow::before{display:none}
.sub{color:var(--ink-soft);max-width:640px}
.btn{display:inline-block;padding:16px 30px;border-radius:5px;font-weight:700;font-size:.98rem;text-decoration:none;letter-spacing:.01em}
.btn-wine{background:var(--wine);color:#FAF5F0}.btn-wine:hover{background:var(--wine-deep)}
.btn-ghost{color:var(--wine);border:1.5px solid var(--wine)}
.btn-copper{background:var(--copper);color:#1B1410}
.dark .btn-ghost,.hero .btn-ghost{color:var(--ntext);border-color:rgba(242,237,228,.5)}
.hero .btn-ghost:hover{background:rgba(242,237,228,.12)}

/* Иконки */
.icwrap{display:inline-flex;width:46px;height:46px;align-items:center;justify-content:center;border-radius:10px;background:rgba(110,59,75,.07);margin-bottom:16px}
.icwrap .ic{width:27px;height:27px}
.dark .icwrap{background:rgba(208,138,95,.12)}

/* Контурные номера (по референсу) */
.card{position:relative}
.bignum{position:absolute;top:8px;right:16px;font-family:'Playfair Display',Georgia,serif;font-size:3.2rem;line-height:1;font-weight:600;color:transparent;-webkit-text-stroke:1.3px rgba(201,168,124,.6);pointer-events:none}
.dark .bignum{-webkit-text-stroke-color:rgba(208,138,95,.45)}

/* Сферы жизни кружками */
.spheres{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;text-align:center}
.sphere .ring{width:122px;height:122px;margin:0 auto 16px;border-radius:50%;border:1.5px solid rgba(201,168,124,.8);display:flex;align-items:center;justify-content:center;background:radial-gradient(circle at 35% 30%,#fff,var(--linen))}
.sphere .ring .ic{width:46px;height:46px;color:var(--wine)}
.sphere b{display:block;font-family:'Playfair Display',Georgia,serif;font-size:1.08rem;margin-bottom:4px}
.sphere span{font-size:.82rem;color:var(--ink-soft);line-height:1.5}

/* Меню */
.nav{position:sticky;top:0;z-index:50;background:rgba(250,247,242,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;gap:22px;padding-top:12px;padding-bottom:12px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);margin-right:auto}
.logo b{font-family:'Playfair Display',Georgia,serif;font-size:1.02rem;line-height:1.1}
.logo span{display:block;font-size:.68rem;color:var(--ink-soft)}
.menu{display:flex;gap:4px;align-items:center}
.mi>.mtop{background:none;border:0;font-family:inherit;display:inline-flex;align-items:center}
.logo b{white-space:nowrap}
.menu>a,.mi>.mtop{font-size:.88rem;font-weight:600;color:var(--ink);text-decoration:none;padding:9px 11px;border-radius:6px;cursor:pointer;list-style:none;white-space:nowrap;transition:background .2s,color .2s}

.mi>.mtop::after{content:'';display:inline-block;width:5px;height:5px;margin-left:7px;border-right:1.6px solid currentColor;border-bottom:1.6px solid currentColor;transform:translateY(-2px) rotate(45deg);opacity:.5}
.menu>a:hover,.mi:hover>.mtop,.mi.on>.mtop{color:var(--wine);background:rgba(110,59,75,.06)}
.menu>a.on{color:var(--wine)}
.mi{position:relative}
.msub{position:absolute;top:calc(100% + 6px);left:-4px;min-width:274px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px;box-shadow:0 26px 50px -28px rgba(50,45,43,.55);opacity:0;visibility:hidden;transform:translateY(7px);transition:opacity .2s ease,transform .2s ease,visibility .2s;z-index:60}
.mi:last-of-type .msub{left:auto;right:-4px}
.mi::after{content:'';position:absolute;top:100%;left:0;right:0;height:10px}
.mi:hover .msub,.mi:focus-within .msub{opacity:1;visibility:visible;transform:none}
.msub a{display:block;padding:9px 12px;border-radius:6px;font-size:.88rem;font-weight:600;color:var(--ink);text-decoration:none;line-height:1.35}
.msub a span{display:block;font-size:.76rem;font-weight:400;color:var(--ink-soft);margin-top:2px}
.msub a:hover{background:var(--linen);color:var(--wine)}
.msub .sep{height:1px;background:var(--line);margin:7px 10px}
.menu .cta{padding:10px 18px;border-radius:5px;background:var(--wine);color:#FAF5F0;font-size:.88rem;font-weight:600;text-decoration:none;white-space:nowrap;margin-left:6px}
.menu .cta:hover{background:var(--wine-deep);color:#FAF5F0}
@media (max-width:1240px) and (min-width:921px){.logo span{display:none}.menu{gap:1px}.menu>a,.mi>.mtop{font-size:.83rem;padding:9px 8px}.menu .cta{padding:10px 14px;font-size:.83rem}}
#mtoggle{display:none}
.burger{display:none;cursor:pointer;padding:8px;margin-left:auto}
.burger span{display:block;width:22px;height:2px;background:var(--ink);margin:5px 0}
@media (max-width:980px){
  .burger{display:block}
  .logo{margin-right:0}
  .nav .wrap{flex-wrap:wrap;gap:8px}
  .menu{display:none;width:100%;flex-direction:column;align-items:stretch;gap:2px;padding:8px 0 16px;max-height:78vh;overflow-y:auto}
  #mtoggle:checked ~ .menu{display:flex}
  .menu>a,.mi>.mtop{font-size:1rem;padding:12px 4px;border-bottom:1px solid var(--line);border-radius:0}
  .mi{width:100%}
  .mi>.mtop{display:flex;width:100%;justify-content:space-between;align-items:center;text-align:left}
  .mi>.mtop::after{margin-left:auto;margin-right:4px;transform:translateY(-2px) rotate(45deg);transition:transform .2s}
  .mi.on>.mtop::after{transform:translateY(2px) rotate(-135deg)}
  .msub{position:static;opacity:1;visibility:visible;transform:none;box-shadow:none;border:none;background:transparent;min-width:0;padding:0;display:none}
  .mi.on .msub{display:block;padding:4px 0 8px 12px}
  .mi:hover .msub{display:none}
  .mi.on:hover .msub{display:block}
  .msub a{padding:12px 8px;font-size:.95rem}
  .msub a span{display:none}
  .msub .sep{display:none}
  .menu .cta{margin:12px 0 0;text-align:center;padding:14px;font-size:1rem}
}

/* Хиро */
.hero{position:relative;background:var(--night);color:var(--ntext)}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.48}
.hero .veil{position:absolute;inset:0;background:linear-gradient(165deg,rgba(23,34,44,.5),rgba(23,34,44,.93) 80%)}
.hero .in{position:relative;z-index:1;max-width:1080px;margin:0 auto;padding:110px 24px 92px}
.hero .in>*{max-width:860px}
.hero.short .in{padding:78px 24px 64px}
.hero .eyebrow{color:var(--copper)}
.hero h1{font-size:clamp(2.3rem,6vw,3.7rem);font-weight:500;color:#fff}
.hero .lead{font-size:1.17rem;line-height:1.65;color:rgba(242,237,228,.85);max-width:640px;margin-top:22px}
.hero .acts{margin-top:34px;display:flex;gap:14px;flex-wrap:wrap}

/* Сетки */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.grid5{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.grid5>*{grid-column:span 2}
.grid5>*:nth-child(4),.grid5>*:nth-child(5){grid-column:span 3}
.grid5 .card{padding:20px 18px}
.grid5 .card p{font-size:.86rem}
.only-m{display:none}
.nails3{grid-template-columns:repeat(3,1fr)}
.card{background:var(--linen);border:1px solid var(--line);border-radius:8px;padding:26px 24px}
.card h3{margin-bottom:8px}
.card p{margin:0;font-size:.93rem;color:var(--ink-soft)}
.card a{font-weight:700;font-size:.9rem;text-decoration:none}
.white{background:#fff}
.nails{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.nails2{grid-template-columns:1fr 1fr}
.nail{background:#fff;border:1px solid var(--line);border-radius:8px;padding:20px}
.nail b{display:block;font-family:'Playfair Display',Georgia,serif;font-size:1.9rem;font-weight:600;color:var(--wine);font-variant-numeric:tabular-nums}
.nail span{font-size:.8rem;color:var(--ink-soft);line-height:1.5}
.dark{background:var(--night);color:var(--ntext)}
.dark h2,.dark h3{color:#fff}
.dark p{color:rgba(242,237,228,.8)}
.dark .eyebrow{color:var(--copper)}
.dark .eyebrow::before{background:rgba(208,138,95,.6)}
.dark .card{background:var(--night2);border-color:rgba(208,138,95,.25)}
.dark .card h3{color:#fff}
.dark .card p{color:rgba(242,237,228,.65)}


/* Два этажа */
.floors{margin:26px 0}
.floor{border:1px solid rgba(110,59,75,.25);border-radius:10px;padding:20px 24px;background:#fff}
.floor b{display:block;font-family:'Playfair Display',Georgia,serif;font-size:1.12rem;margin-bottom:4px}
.floor span{font-size:.9rem;color:var(--ink-soft);line-height:1.6}
.floor.deep{background:var(--linen);border-color:rgba(110,59,75,.4)}
.floor.deep b{color:var(--wine)}
.fl-link{display:flex;justify-content:flex-end;align-items:center;gap:8px;padding:7px 16px;color:var(--wine);font-size:.78rem;font-weight:700;letter-spacing:.06em}
.fl-link svg{width:13px;height:22px}

/* Диаграмма + легенда */
.diagrow{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.legend{display:grid;gap:14px}
.legend .li{display:flex;gap:14px;align-items:flex-start}
.legend .li i{font-style:normal;font-family:'Playfair Display',Georgia,serif;font-size:1.15rem;color:var(--copper);flex:0 0 26px;text-align:center}
.legend .li b{display:block;font-size:.95rem}
.legend .li span{font-size:.85rem;color:rgba(242,237,228,.65);line-height:1.5}

/* Таймлайн */
.timeline{background:#fff;border:1px solid var(--line);border-radius:10px;padding:34px 26px 20px;overflow-x:auto}
.timeline svg{min-width:760px}
.timeline-m{display:none;background:#fff;border:1px solid var(--line);border-radius:10px;padding:26px 22px}
.timeline-m .tm{display:flex;gap:16px;align-items:flex-start}
.timeline-m .tm .c{flex:0 0 46px;height:46px;border-radius:50%;background:var(--wine);color:#FAF5F0;display:flex;align-items:center;justify-content:center;font-family:'Playfair Display',Georgia,serif;font-size:1.15rem}
.timeline-m .tm.last .c{background:var(--night);color:var(--copper)}
.timeline-m .tm b{display:block;padding-top:4px}
.timeline-m .tm span{display:block;font-size:.85rem;color:var(--ink-soft)}
.timeline-m .gap{margin:6px 0 6px 22px;border-left:2px dashed rgba(110,59,75,.35);padding:8px 0 8px 20px;font-size:.8rem;color:var(--sage-deep)}

/* Фото */
.ph{border-radius:8px;overflow:hidden;border:1px solid var(--line)}
.ph img{width:100%;height:100%;object-fit:cover}
.mosaic{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:210px;gap:12px}
.mosaic .ph:first-child{grid-column:span 2;grid-row:span 2}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:44px;align-items:center}
.split .ph{aspect-ratio:4/3}

/* Цитаты */
.pull{border-left:3px solid var(--wine);padding:4px 0 4px 26px;margin:30px 0}
.pull .q{font-family:'Playfair Display',Georgia,serif;font-size:1.3rem;line-height:1.45;font-weight:500}
.pull .who{margin-top:10px;font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft)}
.dark .pull{border-color:var(--copper)}
.dark .pull .q{color:#fff}
.dark .pull .who{color:rgba(242,237,228,.6)}

/* Афиша */
.poster{position:relative;border-radius:10px;overflow:hidden;background:var(--night);color:var(--ntext)}
.poster .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.4}
.poster .veil{position:absolute;inset:0;background:linear-gradient(rgba(23,34,44,.55),rgba(23,34,44,.92))}
.poster .in{position:relative;z-index:1;padding:56px 48px}
.poster h3{font-size:2rem;font-weight:500;color:#fff}
.poster p{color:rgba(242,237,228,.75);max-width:520px}

/* FAQ */
details{background:#fff;border:1px solid var(--line);border-radius:8px;padding:4px 24px;margin-bottom:12px}
details summary{cursor:pointer;font-weight:700;padding:16px 0;list-style:none;display:flex;justify-content:space-between;gap:14px;align-items:center}
details summary::after{content:'+';font-family:'Playfair Display',Georgia,serif;font-size:1.5rem;color:var(--wine);flex:0 0 auto}
details[open] summary::after{content:'\\2212'}
details p{color:var(--ink-soft);padding-bottom:16px;margin:0}

/* Плашки тем (хаб статей) */
.chiplist{margin-top:10px}
.chiplist span{display:inline-block;background:#fff;border:1px solid var(--line);border-radius:100px;padding:7px 15px;margin:0 8px 10px 0;font-size:.84rem;color:var(--ink-soft);line-height:1.4}
.chiplist span.soon{color:var(--sand);border-color:rgba(201,168,124,.5);font-weight:700}
.chiplist a{display:inline-block;background:#fff;border:1.5px solid rgba(110,59,75,.4);border-radius:100px;padding:7px 15px;margin:0 8px 10px 0;font-size:.84rem;font-weight:600;color:var(--wine);text-decoration:none;line-height:1.4}
.chiplist a:hover{background:var(--wine);color:#FAF5F0}

/* Список-ссылки (истоки на главной) */
.linklist{display:grid;gap:10px}
.linklist a{display:flex;gap:14px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px 18px;text-decoration:none;color:var(--ink);transition:transform .3s ease,box-shadow .3s ease}
.linklist a:hover{transform:translateX(4px);box-shadow:0 12px 26px -18px rgba(50,45,43,.45)}
.linklist b{display:block;font-size:.95rem}
.linklist span{display:block;font-size:.82rem;color:var(--ink-soft);line-height:1.45}
.linklist .ic{width:22px;height:22px;flex:0 0 22px;color:var(--wine)}

/* Футер */
footer{background:var(--night);color:var(--ntext);padding:64px 0 40px}
footer h4{font-family:'Playfair Display',Georgia,serif;font-size:1rem;color:var(--copper);margin:0 0 14px}
footer .cols{display:grid;grid-template-columns:1.25fr 1fr 1fr 1fr 1fr;gap:28px}
footer a{color:rgba(242,237,228,.8);text-decoration:none;display:block;padding:4px 0;font-size:.9rem}
footer a:hover{color:#fff}
footer .fine{margin-top:44px;padding-top:20px;border-top:1px solid rgba(242,237,228,.15);font-size:.78rem;color:rgba(242,237,228,.5);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}

/* Анимации появления и ховеры */
.rv{opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s ease}
.rv.on{opacity:1;transform:none}
.card,.nail{transition:transform .35s ease,box-shadow .35s ease}
.card:hover,.nail:hover{transform:translateY(-4px);box-shadow:0 16px 34px -20px rgba(50,45,43,.4)}
.btn{transition:transform .25s ease,background .25s ease}
.btn:hover{transform:translateY(-2px)}
.sphere .ring{transition:transform .4s ease,border-color .4s ease}
.sphere:hover .ring{transform:scale(1.06);border-color:var(--wine)}
@media (prefers-reduced-motion: reduce){.rv{opacity:1;transform:none;transition:none}}

@media (max-width:860px){
  /* Пальцу нужно не меньше 44px: на телефоне поднимаем зоны нажатия */
  .chiplist a,.chiplist span{padding:12px 16px}
  footer a{padding:9px 0}
  section{padding:52px 0}
  .grid2,.grid3,.split,.diagrow{grid-template-columns:1fr}
  .grid5{grid-template-columns:1fr 1fr}
  .grid5>*,.grid5>*:nth-child(4),.grid5>*:nth-child(5){grid-column:auto}
  .nails3{grid-template-columns:1fr 1fr}
  .mosaic{grid-template-columns:1fr 1fr;grid-auto-rows:160px}
  .nails,.spheres{grid-template-columns:1fr 1fr}
  .poster .in{padding:36px 26px}
  footer .cols{grid-template-columns:1fr 1fr}
}
@media (max-width:600px){
  .bignum{display:none}
  .only-d{display:none}
  .only-m{display:block}
  .chiplist span{font-size:.78rem;padding:6px 12px}
  .poster h3{font-size:1.5rem;overflow-wrap:break-word}
  .timeline{display:none}
  .timeline-m{display:block}
}
@media (max-width:480px){
  .nails,.nails2,.nails3{grid-template-columns:1fr}
  .grid5{grid-template-columns:1fr}
  .grid5>*,.grid5>*:nth-child(4),.grid5>*:nth-child(5){grid-column:auto}
  footer .cols{grid-template-columns:1fr}
  .btn{padding:14px 20px;font-size:.92rem}
  .hero .acts .btn{width:100%;text-align:center}
}
"""

LOGO_SVG = """<svg width="42" height="36" viewBox="0 0 100 100" aria-hidden="true"><circle cx="38" cy="50" r="28" fill="none" stroke="#7D8C74" stroke-width="4"/><circle cx="62" cy="50" r="28" fill="none" stroke="#6E3B4B" stroke-width="4"/><path d="M50 24.7 A28 28 0 0 1 50 75.3 A28 28 0 0 1 50 24.7 Z" fill="#6E3B4B" opacity=".9"/></svg>"""

MENU_GROUPS = [
    ("Главная", "/chizhovy2/", None),
    ("Метод", "/chizhovy2/metod/", None),
    ("Обучение", None, [
        ("/chizhovy2/programma/", "Программа целиком", "три модуля и сопровождение"),
        ("/chizhovy2/modul-1/", "Модуль I. Возвращение к себе", "2,5 дня очно"),
        ("/chizhovy2/modul-2/", "Модуль II. Внутренняя свобода", "5 дней очно"),
        ("/chizhovy2/marafon/", "Модуль III. Создатель&nbsp;реальности", "3 месяца в жизни"),
        ("sep", "", ""),
        ("/chizhovy2/kak-prohodit/", "Как проходит обучение", "путь ученика по шагам"),
        ("/chizhovy2/tehniki-sceny/", "Техники сцены", "инструменты работы"),
        ("/chizhovy2/praktiki/", "Ежедневные практики", "из чего состоит день"),
        ("/chizhovy2/slovar/", "Словарь школы", "язык группы простыми словами"),
    ]),
    ("Истоки", None, [
        ("/chizhovy2/istoki/", "Из чего собран метод", "обзор пяти опор"),
        ("sep", "", ""),
        ("/chizhovy2/istoki/moreno-psihodrama/", "Морено и психодрама", "живая сцена"),
        ("/chizhovy2/istoki/zeland-transerfing/", "Зеланд и трансерфинг", "маятники, важность, зеркало"),
        ("/chizhovy2/istoki/est-transformaciya/", "est и «Трансформация»", "откуда пошли погружения"),
        ("/chizhovy2/istoki/goddard/", "Невилл Годдард", "состояние, в котором уже получилось"),
        ("/chizhovy2/istoki/nauka/", "Наука за методом", "ЛеДу, Гоулман, Болте Тейлор"),
    ]),
    ("Люди", None, [
        ("/chizhovy2/vedushchie/", "Алексей и Ирина", "кто ведёт школу"),
        ("/chizhovy2/manifest/", "Манифест школы", "принципы, которые не продаются"),
        ("sep", "", ""),
        ("/chizhovy2/istorii/", "Истории учеников", "полные истории с точкой А"),
        ("/chizhovy2/otzyvy/", "Короткие отзывы", "голоса из групп"),
        ("/chizhovy2/soobshchestvo/", "Сообщество", "команды, забеги, свои люди"),
    ]),
    ("Кому", None, [
        ("/chizhovy2/para/", "Парам", "когда проходят вдвоём"),
        ("/chizhovy2/dlya-predprinimatelej/", "Предпринимателям", "сильный снаружи, устал внутри"),
        ("/chizhovy2/dlya-zhenshchin/", "Женщинам", "вернуть себя себе"),
        ("sep", "", ""),
        ("/chizhovy2/somneniya/", "Частые сомнения", "три главных «а вдруг»"),
        ("/chizhovy2/bezopasnost/", "Безопасность и границы", "кому не подойдёт"),
    ]),
    ("Начать", None, [
        ("/chizhovy2/start/", "С чего начать", "маршрут новичка за три шага"),
        ("/chizhovy2/gid/", "Гайд бесплатно", "«Кто пишет сценарий твоей жизни»"),
        ("/chizhovy2/stati/", "Статьи школы", "библиотека разборов"),
        ("sep", "", ""),
        ("/chizhovy2/voprosy/", "Вопросы и ответы", "формат, глубина, условия"),
        ("/chizhovy2/kontakty/", "Контакты", "Telegram и запись"),
    ]),
]

# какие разделы подсвечивать: active -> группа
GROUP_OF = {}
for gname, gurl, items in MENU_GROUPS:
    if items:
        for u, t, c in items:
            if u != "sep":
                GROUP_OF[u.strip("/").split("/")[-1]] = gname

def nav(active=""):
    parts = []
    for gname, gurl, items in MENU_GROUPS:
        if items is None:
            if gurl == "/chizhovy2/":
                on = " class=\"on\"" if active == "glavnaya" else ""
            else:
                on = " class=\"on\"" if active and gurl.strip("/").endswith(active) else ""
            parts.append(f'<a href="{gurl}"{on}>{gname}</a>')
        else:
            links = ""
            for u, t, cap in items:
                if u == "sep":
                    links += '<div class="sep"></div>'
                else:
                    links += f'<a href="{u}">{t}<span>{cap}</span></a>'
            parts.append(f'<div class="mi"><button class="mtop" type="button" aria-expanded="false">{gname}</button><div class="msub">{links}</div></div>')
    items_html = "".join(parts)
    return f"""<nav class="nav"><div class="wrap">
<a class="logo" href="/chizhovy2/">{LOGO_SVG}<div><b>Настоящие отношения</b><span>Школа Алексея и&nbsp;Ирины Чижовых</span></div></a>
<label class="burger" for="mtoggle" aria-label="Меню"><span></span><span></span><span></span></label>
<input type="checkbox" id="mtoggle">
<div class="menu">{items_html}<a class="cta" href="/chizhovy2/sessiya/">Собеседование</a></div>
</div></nav>"""

FOOTER = """<footer><div class="wrap">
<div class="cols">
<div>
""" + LOGO_SVG + """
<p style="margin:14px 0 0;color:rgba(242,237,228,.7);font-size:.9rem;max-width:280px">Школа трансформации Алексея и&nbsp;Ирины Чижовых. Очные тренинги малыми группами и&nbsp;сопровождение до&nbsp;результата.</p>
</div>
<div><h4>Школа</h4>
<a href="/chizhovy2/metod/">Метод</a>
<a href="/chizhovy2/programma/">Программа целиком</a>
<a href="/chizhovy2/modul-1/">Модуль I. Возвращение к&nbsp;себе</a>
<a href="/chizhovy2/modul-2/">Модуль II. Внутренняя&nbsp;свобода</a>
<a href="/chizhovy2/marafon/">Модуль III. Создатель&nbsp;реальности</a>
<a href="/chizhovy2/kak-prohodit/">Как проходит обучение</a>
<a href="/chizhovy2/praktiki/">Ежедневные практики</a>
<a href="/chizhovy2/tehniki-sceny/">Техники сцены</a>
<a href="/chizhovy2/slovar/">Словарь школы</a>
</div>
<div><h4>Истоки метода</h4>
<a href="/chizhovy2/istoki/">Из чего собран метод</a>
<a href="/chizhovy2/istoki/moreno-psihodrama/">Морено и&nbsp;психодрама</a>
<a href="/chizhovy2/istoki/zeland-transerfing/">Зеланд и&nbsp;трансерфинг</a>
<a href="/chizhovy2/istoki/est-transformaciya/">est и&nbsp;«Трансформация»</a>
<a href="/chizhovy2/istoki/goddard/">Невилл Годдард</a>
<a href="/chizhovy2/istoki/nauka/">Наука за&nbsp;методом</a>
</div>
<div><h4>Люди</h4>
<a href="/chizhovy2/vedushchie/">Алексей и&nbsp;Ирина</a>
<a href="/chizhovy2/manifest/">Манифест школы</a>
<a href="/chizhovy2/istorii/">Истории учеников</a>
<a href="/chizhovy2/otzyvy/">Короткие отзывы</a>
<a href="/chizhovy2/soobshchestvo/">Сообщество</a>
<a href="/chizhovy2/para/">Тренинг для пар</a>
<a href="/chizhovy2/dlya-predprinimatelej/">Для предпринимателей</a>
<a href="/chizhovy2/dlya-zhenshchin/">Для женщин</a>
</div>
<div><h4>Начать</h4>
<a href="/chizhovy2/start/">С чего начать</a>
<a href="/chizhovy2/gid/">Гайд «Кто пишет сценарий твоей жизни»</a>
<a href="/chizhovy2/stati/">Статьи школы</a>
<a href="/chizhovy2/somneniya/">Частые сомнения</a>
<a href="/chizhovy2/bezopasnost/" style="white-space:nowrap">Безопасность и&nbsp;границы</a>
<a href="/chizhovy2/sessiya/">Собеседование</a>
<a href="/chizhovy2/kontakty/">Контакты</a>
<a href="https://t.me/+LVptSH6Mt4hhYmFi">Telegram-канал</a>
</div>
</div>
<div class="fine"><span>«Настоящие отношения» · chizhovy.ru</span><span>Прототип сайта. Результаты участников&nbsp;индивидуальны.</span></div>
</div></footer>"""

# Заголовки, у которых последняя пара слов НЕ влезает в колонку на узком экране.
# Замерено рендером (headfit): для них перенос оставляем естественный.
_FORCED_LIMIT = [None]
_NO_GLUE_HEADS = {
    "Внутренняя свобода",
    "Возвращение к себе",
    "Вспомни последнюю ссору, которая пошла по знакомому кругу",
    "Всё понимаешь, а жизнь не меняется",
    "Группа, которая не расходится",
    "Двое, которые живут так, как учат",
    "Джилл Болте Тейлор · нейроанатом",
    "Всё начинается с состояния",
    "Всё начинается с состояния, а не усилий",
    "Запись не берёт выходных",
    "Запись нельзя переубедить. Её можно только переписать",
    "Как мы работаем с истоками",
    "Откуда эти отзывы",
    "Кто пишет сценарий твоей жизни",
    "Модуль II. Внутренняя свобода",
    "О чём договариваемся на старте",
    "От собеседования до Марафона",
    "Открытия и благодарности",
    "Почему «Настоящие отношения»",
    "Путь ученика по шагам",
    "Разговор, который ты откладывал годами",
    "Сложа руки ты не сидел. В том-то и дело",
    "Собеседование в школу",
    "Создатель реальности",
    "Спокойствие и уверенность",
    "Статьи, после которых что‑то щёлкает",
    "Тренинг «Настоящие отношения»",
    "Три идеи, которые мы используем",
    "Чего на собеседовании не будет",
    "Что ещё меняет старую запись",
    "Что происходило с людьми",
    "К чему приходят участники",
}

_BLOCK_RE = re.compile(
    r'<(p|h1|h2|h3|h4|li|blockquote|figcaption|dd|dt)(\s[^>]*)?>(.*?)</\1>',
    re.S | re.I)

def _glue_last_pair(inner: str, tag: str = 'p', limit: int = None) -> str:
    """Склеивает последние два слова блока неразрывным пробелом, чтобы последнее
    слово не падало сиротой на отдельную строку ни на одной ширине экрана.
    Следит, чтобы получившийся НЕРАЗРЫВНЫЙ КУСОК не стал шире колонки:
    иначе заголовок обрежется краем экрана на телефоне."""
    if re.search(r'<(p|div|ul|ol|li|h[1-4]|table|section)\b', inner, re.I):
        return inner
    # предел длины неразрывного куска: у заголовков шрифт крупный, им нужно строже
    # Заголовки: склеиваем последнюю пару, КРОМЕ тех, у которых пара шире колонки
    # на узком экране (замерено рендером, список ниже). Иначе крупный заголовок
    # вылезет за край и потянет горизонтальную прокрутку.
    if tag.lower() in ('h1', 'h2', 'h3', 'h4'):
        plain = re.sub(r'<[^>]*>', '', inner)
        plain = plain.replace('&nbsp;', ' ').replace('\xa0', ' ')
        plain = re.sub(r'\s+', ' ', plain).strip()
        if plain in _NO_GLUE_HEADS:
            return inner
        limit = 99
    else:
        limit = 26
    if limit is not None and tag.lower() not in ('h1', 'h2', 'h3', 'h4'):
        pass
    if _FORCED_LIMIT[0] is not None:
        limit = _FORCED_LIMIT[0]
    # позиции ОБЫЧНЫХ пробелов вне тегов (неразрывные не считаем)
    spaces, depth = [], 0
    for i, ch in enumerate(inner):
        if ch == '<':
            depth += 1
        elif ch == '>':
            depth = max(0, depth - 1)
        elif ch == ' ' and depth == 0:
            spaces.append(i)
    if not spaces:
        return inner
    vis = lambda s: (s.replace('&nbsp;', '\xa0').replace('&#8288;', '')
                      .replace('&nbsp', '\xa0'))
    for pos in reversed(spaces):
        tail = re.sub(r'<[^>]*>', '', inner[pos + 1:]).strip()
        head = re.sub(r'<[^>]*>', '', inner[:pos]).strip()
        if not tail or not head:
            continue
        # что реально склеится: хвостовая неразрывная цепочка головы
        # плюс головная неразрывная цепочка хвоста
        prev_chain = vis(head).split(' ')[-1]
        next_chain = vis(tail).split(' ')[0]
        if not prev_chain or not next_chain:
            continue
        run = len(prev_chain) + 1 + len(next_chain)
        if run > limit:
            return inner
        return inner[:pos] + '&nbsp;' + inner[pos + 1:]
    return inner

# Текстовые блоки, свёрстанные не абзацем, а div/span: цитаты, подписи под фото.
# Их обычный разбор по тегам не ловит, а сирота там видна так же.
_TEXTBOX_RE = re.compile(
    r'(<(?:div|span)\s+class="(?:q|who|cap|t-lead|t-body|gap)"[^>]*>|<span>)'
    r'([^<]{20,}?)(</(?:div|span)>)',
    re.S)

def typo(html: str) -> str:
    """Типографский проход: ни одного слова-сироты в конце абзаца, заголовка, цитаты."""
    html = _BLOCK_RE.sub(
        lambda m: f'<{m.group(1)}{m.group(2) or ""}>'
                  f'{_glue_last_pair(m.group(3), m.group(1))}</{m.group(1)}>',
        html)
    def fix_box(m):
        _FORCED_LIMIT[0] = 26          # столько влезает и в цитату, и в подпись
        try:
            return m.group(1) + _glue_last_pair(m.group(2), 'p') + m.group(3)
        finally:
            _FORCED_LIMIT[0] = None
    return _TEXTBOX_RE.sub(fix_box, html)

def page(title, desc, active, body):
    body = typo(body)
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="/chizhovy2/site.css">
</head>
<body>
{nav(active)}
{body}
{typo(FOOTER)}
<script>
document.querySelectorAll('.mi > .mtop').forEach(btn => {{
  btn.addEventListener('click', e => {{
    if (window.innerWidth > 980) return;
    e.preventDefault();
    const mi = btn.parentElement, wasOpen = mi.classList.contains('on');
    document.querySelectorAll('.mi.on').forEach(o => {{ o.classList.remove('on'); o.querySelector('.mtop').setAttribute('aria-expanded','false'); }});
    if (!wasOpen) {{ mi.classList.add('on'); btn.setAttribute('aria-expanded','true'); }}
  }});
}});
if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {{
  const els = document.querySelectorAll('.card,.pull,.nail,.sphere,figure,.poster,.floor,.role,.split > *,.diagrow > *,section h2,.stepline .st');
  els.forEach(e => e.classList.add('rv'));
  const io = new IntersectionObserver(es => es.forEach(x => {{
    if (x.isIntersecting) {{ x.target.classList.add('on'); io.unobserve(x.target); }}
  }}), {{threshold:.12}});
  els.forEach(e => io.observe(e));
}}
</script>
</body>
</html>"""

floors = """<div class="floors">
<div class="floor"><b>Этаж слов</b><span>книги, разговоры, решения «с&nbsp;понедельника». Сюда стучались прошлые попытки</span></div>
<div class="fl-link"><span>работа идёт сюда</span><svg viewBox="0 0 14 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 1v17M2 14l5 7 5-7"/></svg></div>
<div class="floor deep"><b>Этаж эмоции и&nbsp;тела</b><span>здесь хранится запись. И&nbsp;здесь&nbsp;же её&nbsp;переписывают: в&nbsp;живой сцене</span></div>
</div>"""

P = {}

# ================= ГЛАВНАЯ =================
P["index.html"] = ("Настоящие отношения · школа трансформации Чижовых",
"Очный тренинг и три месяца сопровождения: выход из повторяющихся сценариев в отношениях, деле и состоянии.", "glavnaya", f"""
<div class="hero"><div class="bg" style="background-image:url('/chizhovy2/images/site-hero.png')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Школа трансформации Алексея и&nbsp;Ирины Чижовых</p>
<h1>Перепиши сценарий своей жизни</h1>
<p class="lead">Очный тренинг и&nbsp;три месяца сопровождения. Перестаёшь ходить по&nbsp;одному и&nbsp;тому же&nbsp;кругу и&nbsp;начинаешь строить отношения, дело и&nbsp;себя по&nbsp;своему выбору.</p>
<div class="acts"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a><a class="btn btn-ghost" href="/chizhovy2/gid/">Читать гайд бесплатно</a></div>
</div></div>

<section><div class="wrap">
<div class="nails">
<div class="nail"><b>16&nbsp;лет</b><span>в&nbsp;трансформационной практике</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе, каждого знаем по&nbsp;имени</span></div>
<div class="nail"><b>3</b><span>модуля очного погружения</span></div>
<div class="nail"><b>3&nbsp;месяца</b><span>сопровождения после тренинга</span></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Для тебя, если</p>
<h2>Что-то из этого точно про тебя</h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><span class="bignum">01</span>{icon('book')}<h3>Всё понимаешь, а жизнь не меняется</h3><p>Книги прочитаны, курсы пройдены, выводы сделаны. Реакции те&nbsp;же, что пять лет назад.</p></div>
<div class="card"><span class="bignum">02</span>{icon('loop','var(--sage-deep)')}<h3>Сценарии повторяются</h3><p>Разные люди, новые обстоятельства, финал одинаковый. В&nbsp;отношениях, в&nbsp;деньгах, в&nbsp;теле.</p></div>
<div class="card"><span class="bignum">03</span>{icon('shield','var(--sand)')}<h3>Для всех опора, а сам устал</h3><p>Бизнес, семья, статус, всё по&nbsp;списку. И&nbsp;усталость, о&nbsp;которой некому&nbsp;рассказать.</p></div>
<div class="card"><span class="bignum">04</span>{icon('cups','var(--sage-deep)')}<h3>Быт съел близость</h3><p>Календарь общий, разговоры про логистику. Не&nbsp;ссоритесь, потому что&nbsp;незачем.</p></div>
<div class="card"><span class="bignum">05</span>{icon('ceiling','var(--sand)')}<h3>Деньги упёрлись в&nbsp;потолок</h3><p>Рывки вверх быстро выравниваются обратно. Цифра дохода годами почти&nbsp;одна.</p></div>
<div class="card"><span class="bignum">06</span>{icon('lens')}<h3>Хочется настоящего</h3><p>Не&nbsp;казаться, а&nbsp;быть. В&nbsp;паре, в&nbsp;деле, с&nbsp;собой. С&nbsp;этого запроса у&nbsp;нас начинали многие.</p></div>
</div>
<div class="chiplist" style="margin-top:22px"><a href="/chizhovy2/dlya-predprinimatelej/">Я предприниматель</a><a href="/chizhovy2/para/">Мы пара</a><a href="/chizhovy2/dlya-zhenshchin/">Хочу вернуть себя</a><a href="/chizhovy2/start/">С чего начать</a></div>
</div></section>

<section class="dark"><div class="wrap">
<div class="diagrow">
<div>
<p class="eyebrow">Метод</p>
<h2>Мы работаем с&nbsp;причиной</h2>
<p>Повторы держатся не&nbsp;на&nbsp;характере и&nbsp;не&nbsp;на&nbsp;«таком партнёре». Их&nbsp;крутит событийный круг: старое решение включается быстрее сознания и&nbsp;доигрывает знакомый финал.</p>
<p>Разорвать круг усилием не&nbsp;выходит. Мы&nbsp;разбираем его там, где он&nbsp;записан: в&nbsp;эмоции и&nbsp;теле, в&nbsp;живой групповой работе, где старая сцена проигрывается заново и&nbsp;заканчивается&nbsp;по-другому.</p>
<p style="margin-top:24px"><a class="btn btn-ghost" href="/chizhovy2/metod/">Разобрать метод подробно</a></p>
</div>
<div>{loop_diagram(dark=True)}</div>
</div>
</div></section>

<section style="padding-bottom:0"><div class="wrap">
<p class="eyebrow">Четыре сферы жизни</p>
<h2>Меняется всё сразу</h2>
<p class="sub">Запись одна, а&nbsp;платит за&nbsp;неё вся жизнь сразу. Поэтому и&nbsp;меняются сферы вместе, когда причина найдена.</p>
<div class="spheres" style="margin-top:32px">
<div class="sphere"><div class="ring">{ICONS['lens']}</div><b>Отношения</b><span>пара, дети, родители,&nbsp;близость</span></div>
<div class="sphere"><div class="ring">{ICONS['coins']}</div><b>Деньги и&nbsp;дело</b><span>доход, рост, решения без страха</span></div>
<div class="sphere"><div class="ring">{ICONS['flame']}</div><b>Энергия и&nbsp;тело</b><span>силы, сон, спорт, ясная&nbsp;голова</span></div>
<div class="sphere"><div class="ring">{ICONS['people']}</div><b>Окружение</b><span>команда, друзья, среда&nbsp;роста</span></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Программа</p>
<h2>Три модуля, один путь</h2>
<div class="timeline" style="margin-top:28px">{timeline_svg()}</div>
<div class="timeline-m" style="margin-top:28px">
<div class="tm"><div class="c">I</div><div><b>Возвращение к&nbsp;себе</b><span>2,5 дня очно</span></div></div>
<div class="gap">месяц на&nbsp;интеграцию</div>
<div class="tm"><div class="c">II</div><div><b>Внутренняя свобода</b><span>5 дней очно</span></div></div>
<div class="gap">ещё 3-5 недель до&nbsp;финала</div>
<div class="tm last"><div class="c">III</div><div><b>Создатель реальности</b><span>3 месяца в&nbsp;жизни, результаты&nbsp;остаются</span></div></div>
</div>
<div class="grid3" style="margin-top:26px">
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/site-m1.png" alt="Утро, женщина пишет в дневник у окна" loading="lazy"></div><h3>I. Возвращение к&nbsp;себе</h3><p>Увидеть свои паттерны, установки и&nbsp;то, откуда они родом. Первый честный контакт с&nbsp;собой.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-1/">Про первый модуль</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-07.jpg" alt="Группа тренинга в тёплом зале" loading="lazy"></div><h3>II. Внутренняя свобода</h3><p>Страх, вина, обида, чужие ожидания. Перезапись решений, которые правили годами.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-2/">Про второй модуль</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-10.jpg" alt="Команда выпуска тренинга" loading="lazy"></div><h3>III. Создатель реальности</h3><p>Команда, еженедельные встречи, новые действия и&nbsp;результаты, которые остаются.</p><p style="margin-top:12px"><a href="/chizhovy2/marafon/">Про Марафон</a></p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Какие возможности откроются</p>
<h2>Что <span class="kpm">становится возможным</span></h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><span class="bignum">01</span>{icon('ceiling')}<h3>Дело пробивает потолок</h3><p>Видишь, что именно держало обороты и&nbsp;заставляло цепляться за&nbsp;«стабильный» заработок. Убираешь причину, не&nbsp;симптом.</p></div>
<div class="card"><span class="bignum">02</span>{icon('route','var(--sage-deep)')}<h3>Понимание себя</h3><p>Кто я, куда бегу, почему всё повторяется по&nbsp;спирали. Видишь свои сильные стороны и&nbsp;путь к&nbsp;целям.</p></div>
<div class="card"><span class="bignum">03</span>{icon('lens','var(--sand)')}<h3>Крепкие отношения</h3><p>Выходишь из&nbsp;разрушающих связей и&nbsp;затяжных конфликтов, налаживаешь отношения с&nbsp;близкими.</p></div>
<div class="card"><span class="bignum">04</span>{icon('mountain','var(--sage-deep)')}<h3>Спокойствие и&nbsp;уверенность</h3><p>Внутренняя опора вместо выдержки на&nbsp;зубах. Острые моменты перестают выбивать из&nbsp;седла.</p></div>
<div class="card"><span class="bignum">05</span>{icon('people','var(--sand)')}<h3>Своё окружение</h3><p>Люди, с&nbsp;которыми можно в&nbsp;разведку и&nbsp;в&nbsp;дело. Навык слышать, договариваться, играть вместе.</p></div>
<div class="card"><span class="bignum">06</span>{icon('sunrise')}<h3>От понимания к&nbsp;действию</h3><p>Перестаёшь откладывать жизнь на&nbsp;потом. Путь от&nbsp;идеи до&nbsp;реализации сокращается в&nbsp;разы.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Как это выглядит</p>
<h2>Наши группы, фотографии без постановки</h2>
<p class="sub">Это живые выпуски школы. Малые группы, очная работа, люди, которых мы&nbsp;знаем по&nbsp;именам и&nbsp;историям.</p>
<div class="mosaic" style="margin-top:28px">
<div class="ph"><img src="/chizhovy2/images/real/real-05.jpg" alt="Выпуск группы тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-06.jpg" alt="Группа тренинга в зале" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-01.jpg" alt="Группа у камина с сертификатами" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-11.jpg" alt="Команда участников" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-13.jpg" alt="Выпуск модуля" loading="lazy"></div>
</div>
</div></section>

<section class="dark" style="padding:0"><div class="wrap" style="padding-top:76px;padding-bottom:76px">
<div class="pull"><div class="q">«Появилось ощущение, что вижу себя на&nbsp;всей шахматной доске, а&nbsp;не&nbsp;в&nbsp;одной клетке.»</div><div class="who">Участник тренинга, предприниматель</div></div>
<div class="pull"><div class="q">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше.»</div><div class="who">Участник второго модуля</div></div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Читать истории целиком</a></p>
</div></section>

<section><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Ведущие</p>
<h2>Двое, которые живут так, как учат</h2>
<p>Алексей: коуч с&nbsp;сертификацией ICF, 16&nbsp;лет практики, триатлет. Ирина: трансформационный тренер, шесть лет готовилась к&nbsp;этому формату, работает на&nbsp;глубине, которую участники вспоминают&nbsp;годами.</p>
<p>Вместе 17&nbsp;лет. Школу ведёт пара, у&nbsp;которой отношения живые: с&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них.</p>
<p style="margin-top:20px"><a class="btn btn-ghost" href="/chizhovy2/vedushchie/">Познакомиться</a></p>
</div>
<div class="ph"><img src="/chizhovy2/images/real/portret.jpg" alt="Алексей и Ирина Чижовы, портрет" loading="lazy"></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Истоки метода</p>
<h2 style="font-size:clamp(1.55rem,4vw,2.3rem)">Рассказываем, из чего собран метод</h2>
<p>Сильной работе нечего прятать. Мы&nbsp;открыто называем школы и&nbsp;авторов, на&nbsp;которых выросли: психодрама Морено, трансерфинг Зеланда, тренинги погружения от&nbsp;est, практика состояния Годдарда. И&nbsp;показываем, что взяли, что переработали за&nbsp;16&nbsp;лет и&nbsp;почему это работает с&nbsp;точки зрения науки.</p>
<p style="margin-top:20px"><a class="btn btn-ghost" href="/chizhovy2/istoki/">Разобрать истоки</a></p>
</div>
<div class="linklist">
<a href="/chizhovy2/istoki/moreno-psihodrama/">{ICONS['people']}<div><b>Якоб Морено и&nbsp;психодрама</b><span>живая сцена вместо разговоров о&nbsp;жизни</span></div></a>
<a href="/chizhovy2/istoki/zeland-transerfing/">{ICONS['loop']}<div><b>Вадим Зеланд и&nbsp;трансерфинг</b><span>маятники, важность, зеркало мира</span></div></a>
<a href="/chizhovy2/istoki/est-transformaciya/">{ICONS['flame']}<div><b>est и&nbsp;«Трансформация» Рейнхарта</b><span>откуда пошли тренинги погружения</span></div></a>
<a href="/chizhovy2/istoki/goddard/">{ICONS['sunrise']}<div><b>Невилл Годдард</b><span>состояние, в котором уже получилось</span></div></a>
<a href="/chizhovy2/istoki/nauka/">{ICONS['book']}<div><b>Наука за&nbsp;методом</b><span>ЛеДу, Гоулман, Болте&nbsp;Тейлор,&nbsp;Голвитцер</span></div></a>
</div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="poster"><div class="bg" style="background-image:url('/chizhovy2/images/site-dark.png')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Ближайшие даты</p>
<h3>Модуль II. Внутренняя&nbsp;свобода</h3>
<p>Пять дней, после которых страх, вина и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p>
<p style="margin-top:24px"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Занять место</a></p>
</div></div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Начни с разговора на час</h2>
<p class="sub" style="margin:0 0 26px">Собеседование в&nbsp;школу: час о&nbsp;твоей ситуации и&nbsp;честный ответ, чем школа может помочь. Для читателей сайта&nbsp;бесплатно.</p>
<a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a>
</div></section>
""")

# ================= МЕТОД =================
P["metod/index.html"] = ("Метод школы · Настоящие отношения",
"Событийный круг, состояние и психодрама: подробный разбор, как устроена перезапись сценариев.", "metod", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-metod.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Метод школы</p><h1>Всё начинается <span class="kp">с состояния</span></h1>
<p class="lead">Мы&nbsp;не&nbsp;учим «правильно общаться» и&nbsp;не&nbsp;выдаём мотивацию на&nbsp;неделю. Мы&nbsp;находим старую запись, по&nbsp;которой идут твои реакции, и&nbsp;помогаем переписать её&nbsp;там, где она хранится. Ниже метод разобран по&nbsp;винтикам.</p>
<div class="acts"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a><a class="btn btn-ghost" href="/chizhovy2/vedushchie/">Кто ведёт</a></div>
</div></div>

<section><div class="narrow">
<p class="eyebrow">Главная идея</p>
<h2>Муравей и&nbsp;слон</h2>
<p>Разум мал и&nbsp;суетлив, как муравей. Состояние огромно, как слон. Пока слон лежит или идёт в&nbsp;другую сторону, план можно тащить куда угодно: масса не&nbsp;та. Поэтому решения «с&nbsp;понедельника» держатся до&nbsp;первого настоящего стресса, а&nbsp;цели из&nbsp;ежедневника не&nbsp;доходят до&nbsp;жизни.</p>
<p>Порядок обратный: сначала слон, потом муравей. Меняется состояние, меняются решения. Меняются решения, меняется жизнь. Ученики после тренинга говорят об&nbsp;этом коротко: мир зеркалит состояние.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:26px">
<div class="nail"><b>95%</b><span>дня человек живёт на&nbsp;автопилоте привычных&nbsp;реакций</span></div>
<div class="nail"><b>12&nbsp;мс</b><span>фора эмоционального мозга перед&nbsp;думающим (ЛеДу)</span></div>
<div class="nail"><b>90&nbsp;сек</b><span>живёт химия эмоции, если&nbsp;её&nbsp;не&nbsp;кормить (Болте&nbsp;Тейлор)</span></div>
</div></div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Механика повтора</p>
<h2>Событийный круг</h2>
<div class="diagrow" style="margin-top:30px">
<div>{loop_diagram(dark=True)}</div>
<div>
<div class="legend">
<div class="li"><i>1</i><div><b>Событие</b><span>Что-то происходит: слово, взгляд, сумма на&nbsp;счёте. Само по&nbsp;себе оно нейтрально.</span></div></div>
<div class="li"><i>2</i><div><b>Эмоция</b><span>Реакция тела опережает мысль: аварийный центр мозга получает сигнал за&nbsp;миллисекунды до&nbsp;осмысления.</span></div></div>
<div class="li"><i>3</i><div><b>Старое решение</b><span>«Злиться опасно», «просить стыдно», «я&nbsp;сам». Принято в&nbsp;детстве, работает во&nbsp;взрослой жизни.</span></div></div>
<div class="li"><i>4</i><div><b>Сценарий</b><span>Поведение идёт по&nbsp;записи, финал тот&nbsp;же, что в&nbsp;прошлый раз. Круг замыкается и&nbsp;укрепляется.</span></div></div>
</div>
<p style="margin-top:18px">Разорвать круг усилием не&nbsp;выходит: он&nbsp;быстрее сознания. Его размыкают в&nbsp;точке&nbsp;3. Там живёт старое&nbsp;решение.</p>
</div>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">Почему разговоры не помогают</p>
<h2>Запись лежит этажом ниже</h2>
<p>Книги, курсы и&nbsp;беседы стучатся в&nbsp;думающий этаж. Запись лежит этажом ниже: в&nbsp;эмоции и&nbsp;теле. Договариваться с&nbsp;ней словами&nbsp;то&nbsp;же самое, что уговаривать плёнку звучать иначе. Поэтому понимание копится годами, а&nbsp;реакции остаются прежними.</p>
{floors}
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Инструмент №1</p>
<h2>Психодрама: старое решение меняют прямо в&nbsp;сцене</h2>
<p class="sub">Метод психиатра Якоба Морено. Сто лет практики по&nbsp;всему миру. Человек не&nbsp;рассказывает о&nbsp;ситуации, а&nbsp;возвращается в&nbsp;неё&nbsp;и&nbsp;меняет решение прямо внутри сцены.</p>
<div class="split" style="margin-top:30px">
<div class="ph"><img src="/chizhovy2/images/metod-scena.png" alt="Сцена психодрамы: участник в центре, группа вокруг" loading="lazy"></div>
<div>
<p>Со&nbsp;стороны это похоже на&nbsp;живой театр без сценария. Изнутри это самая точная работа, которую мы&nbsp;знаем: сцена достаёт запись целиком, с&nbsp;эмоцией, телом и&nbsp;тем самым решением.</p>
<p>Морено называл результат спонтанностью: способностью дать новый ответ на&nbsp;старую ситуацию. По-нашему: момент, когда пульт возвращается к&nbsp;хозяину.</p>
<p style="margin-top:14px"><a href="/chizhovy2/tehniki-sceny/">Техники сцены с&nbsp;разбором</a> · <a href="/chizhovy2/istoki/moreno-psihodrama/">Про Морено и&nbsp;психодраму</a></p>
</div>
</div>
<div class="grid5" style="margin-top:30px" id="psy-steps">
<div class="card"><span class="bignum">1</span><h3>Запрос</h3><p>Называешь сцену, которая держит: ссора, разговор, который откладываешь годами, момент из&nbsp;детства.</p></div>
<div class="card"><span class="bignum">2</span><h3>Сцена</h3><p>Участники группы становятся героями твоей истории. Пространство зала превращается в&nbsp;ту&nbsp;кухню, тот кабинет, тот&nbsp;двор.</p></div>
<div class="card"><span class="bignum">3</span><h3>Проживание</h3><p>Говоришь из&nbsp;себя настоящего то, что тогда осталось несказанным. Тело включается раньше слов. Так и&nbsp;надо.</p></div>
<div class="card"><span class="bignum">4</span><h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место другого: отца, партнёра, себя-ребёнка. Сцена, которую ты&nbsp;носил годами, впервые видна целиком.</p></div>
<div class="card"><span class="bignum">5</span><h3>Новое решение</h3><p>Прямо в&nbsp;сцене принимаешь другое решение. Теперь оно записано так&nbsp;же глубоко, как старое: телом и&nbsp;эмоцией.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Пустой стул</p>
<h2>Разговор, который ты&nbsp;откладывал годами</h2>
<p>Иногда сцена строится вокруг пустого стула. На&nbsp;нём сидит тот, с&nbsp;кем так и&nbsp;не&nbsp;поговорил: отец, бывший, ты&nbsp;сам из&nbsp;прошлого. Разговор случается сейчас, и&nbsp;тело отпускает то, что держало.</p>
<p>После таких процессов участники говорят: «снял рюкзак», «стало легче дышать». Это буквальные ощущения: напряжение, которое тело держало годами, находит выход.</p>
</div>
<div class="ph"><img src="/chizhovy2/images/metod-stul.png" alt="Пустой стул в луче тёплого света" loading="lazy"></div>
</div>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Вокруг сцены</p>
<h2>Что ещё меняет старую запись</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('flame','var(--copper)')}<h3>Работа с&nbsp;телом</h3><p>Запись живёт в&nbsp;мышцах и&nbsp;дыхании. Телесные практики достают её&nbsp;там, куда слова не&nbsp;доходят, и&nbsp;учат выходить из&nbsp;захвата за&nbsp;те&nbsp;самые 90&nbsp;секунд.</p></div>
<div class="card">{icon('gear','var(--copper)')}<h3>Разбор вины и&nbsp;ответственности</h3><p>Вина сливает энергию и&nbsp;зовёт наказание. Ответственность возвращает силу. Разницу учимся чувствовать телом, а&nbsp;не&nbsp;запоминать&nbsp;словами.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Группа как зеркало</h3><p>10-20 человек, у&nbsp;которых те&nbsp;же боли под другими фамилиями. В&nbsp;чужой сцене узнаёшь свою запись быстрее, чем в&nbsp;своей.</p></div>
<div class="card">{icon('sunrise','var(--copper)')}<h3>Ежедневная практика</h3><p>После модулей: утренний фокус дня, вечерние открытия и&nbsp;благодарности. Девяносто дней Марафона делают новый ответ&nbsp;привычкой.</p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Наука за&nbsp;методом</p>
<h2>Кто это проверил до&nbsp;нас</h2>
<div class="grid2" style="margin-top:26px">
<div class="card white"><h3>Джозеф ЛеДу · нейробиолог</h3><p>Показал «короткий путь» страха: миндалина получает сигнал за&nbsp;12&nbsp;миллисекунд, раньше думающей коры. Вот почему реакция обгоняет&nbsp;намерение.</p></div>
<div class="card white"><h3>Дэниел Гоулман · психолог</h3><p>Описал «захват»: в&nbsp;момент вспышки разумная часть мозга приглушается. «Взять себя в&nbsp;руки» тогда физически нечем.</p></div>
<div class="card white"><h3>Джилл Болте Тейлор&nbsp;·&nbsp;нейроанатом</h3><p>Правило 90&nbsp;секунд: химия эмоции сама уходит из&nbsp;крови за&nbsp;полторы минуты, если не&nbsp;подкармливать её&nbsp;мыслями по&nbsp;кругу.</p></div>
<div class="card white"><h3>Якоб Морено · психиатр</h3><p>Создал психодраму и&nbsp;доказал: новый ответ, прожитый в&nbsp;сцене телом и&nbsp;эмоцией, записывается так&nbsp;же глубоко, как детское решение.</p></div>
</div>
<p style="margin-top:18px"><a href="/chizhovy2/istoki/nauka/">Все пять открытий с&nbsp;разбором: наука за&nbsp;методом</a></p>
<div class="pull" style="margin-top:24px"><div class="q">«Труднее всего было принять точку&nbsp;А. Принять, что мир это зеркало, и&nbsp;всё, что со&nbsp;мной происходит, я&nbsp;транслирую сам.»</div><div class="who">Участник тренинга</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Три опоры результата</p>
<h2>Почему изменения остаются</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('layers')}<h3>Глубина</h3><p>Очные модули по&nbsp;несколько дней: время дойти до&nbsp;причины, а&nbsp;не&nbsp;снять&nbsp;симптом.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Группа</h3><p>Малая группа, каждого знаем по&nbsp;имени. В&nbsp;чужих историях узнаёшь свою, в&nbsp;своих перестаёшь быть один.</p></div>
<div class="card">{icon('calendar','var(--sand)')}<h3>Практика</h3><p>Три месяца сопровождения: новые реакции закрепляются действиями в&nbsp;обычной жизни, пока не&nbsp;станут&nbsp;своими.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Кому метод не&nbsp;подойдёт</h2>
<p>Честно: тем, кто ищет волшебную таблетку за&nbsp;вечер. Тем, кто пока не&nbsp;готов работать в&nbsp;группе. И&nbsp;тем, кому сейчас нужна медицинская помощь, а&nbsp;не&nbsp;тренинг: об&nbsp;этом мы&nbsp;говорим прямо и&nbsp;подсказываем, куда идти.</p>
<p>Для всех остальных вход один: собеседование. Час честного разговора, где вместе решаем, твой это метод или нет. Для пришедших с&nbsp;сайта бесплатно.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/programma/" style="margin-left:8px">Смотреть программу</a></p>
</div></section>
""")

# ================= ПРОГРАММА =================
P["programma/index.html"] = ("Программа · Настоящие отношения",
"Три модуля школы: Возвращение к себе, Внутренняя свобода, Создатель реальности.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-06.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Программа</p><h1>Путь из&nbsp;трёх модулей</h1>
<p class="lead">У&nbsp;каждого модуля своя задача: увидеть старую запись, переписать её&nbsp;и закрепить новое делами. Между модулями 3-5&nbsp;недель, чтобы всё улеглось в&nbsp;обычной жизни.</p></div></div>

<section><div class="wrap">
<div class="timeline">{timeline_svg()}</div>
<div class="grid3" style="margin-top:26px">
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/site-m1.png" alt="Модуль I" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль I · 2,5 дня</p><h3>Возвращение к&nbsp;себе</h3><p>Видишь свои повторяющиеся паттерны, установки и&nbsp;их&nbsp;источники. Результат: осознанность и&nbsp;первый честный контакт с&nbsp;собой.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-1/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-07.jpg" alt="Модуль II" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль II · 5 дней</p><h3>Внутренняя свобода</h3><p>Глубокая работа с&nbsp;состояниями: страх, вина, обида, зависимость от&nbsp;чужого мнения. Результат: сила, спокойствие, ясность.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-2/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-13.jpg" alt="Модуль III" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль III · 3 месяца</p><h3>Создатель реальности</h3><p>Интеграция в&nbsp;жизнь: видение, команда, ежедневная практика, результаты в&nbsp;деле и&nbsp;отношениях. Это и&nbsp;есть Марафон.</p><p style="margin-top:12px"><a href="/chizhovy2/marafon/">Подробнее</a></p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Как попасть на программу</h2>
<div class="card white" style="margin-top:20px">{icon('speech')}<h3>Начало:&nbsp;собеседование</h3><p>Час разговора о&nbsp;твоей ситуации. Честно решаем, подходит&nbsp;ли тебе школа. Для пришедших с&nbsp;этого сайта собеседование бесплатное.</p></div>
<div class="card white" style="margin-top:12px">{icon('people','var(--sage-deep)')}<h3>Формат</h3><p>Очные модули в&nbsp;Москве малой группой 10-20 человек, между погружениями 3-5 недель с&nbsp;поддержкой, после третьей ступени три месяца сопровождения.</p></div>
<div class="card white" style="margin-top:12px">{icon('target','var(--sand)')}<h3>Для кого</h3><p>Для взрослых людей, готовых брать ответственность: предприниматели, руководители, пары. Участников отбираем на&nbsp;собеседовании. Глубина требует&nbsp;готовности.</p></div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Зачем нужны недели между модулями</h2>
<p>Пауза в&nbsp;3-5 недель работает как часть метода, а&nbsp;вовсе не&nbsp;организационная заминка. После погружения человек возвращается в&nbsp;обычную жизнь и&nbsp;там проверяет, что изменилось на&nbsp;самом деле: как теперь идут разговоры дома, что происходит в&nbsp;конфликте, сколько сил остаётся к&nbsp;вечеру.</p>
<p>Именно в&nbsp;эти недели видно, где новое уже работает, а&nbsp;где старая запись держит крепко. С&nbsp;этим человек и&nbsp;приходит на&nbsp;следующее погружение, поэтому разбор идёт по&nbsp;живому.</p>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Три задачи</p>
<h2>Что решает каждый модуль</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('lens','var(--copper)')}<h3>Увидеть</h3><p>Первая ступень отвечает на&nbsp;вопрос «что со&nbsp;мной происходит и&nbsp;откуда это взялось». Без этого шага любые техники бьют мимо.</p></div>
<div class="card">{icon('flame','var(--copper)')}<h3>Переписать</h3><p>Второй идёт к&nbsp;решениям, которые держат сценарий: страх, вина, обида. Работа глубокая, поэтому и&nbsp;формат пять дней.</p></div>
<div class="card">{icon('calendar','var(--copper)')}<h3>Закрепить</h3><p>Третий переносит новое в&nbsp;обычную жизнь: девяносто дней практики, команда и&nbsp;еженедельные разборы с&nbsp;ведущими.</p></div>
</div>
<p style="margin-top:22px;color:rgba(242,237,228,.75)">Пропустить ступень не&nbsp;выйдет: без первого модуля второй бьёт вслепую, без третьего результат тает через пару месяцев. Подробнее про сам подход: <a href="/chizhovy2/metod/" style="color:#D08A5F">метод школы</a> и&nbsp;<a href="/chizhovy2/kak-prohodit/" style="color:#D08A5F">как проходит обучение</a>.</p>
</div></section>

<section><div class="narrow">
<h2>Частые вопросы о&nbsp;программе</h2>
<details><summary>Обязательно проходить все три модуля?</summary><p>Решение принимается после каждого: никто не&nbsp;обязывает идти дальше. При этом путь построен как единое целое, и&nbsp;участники, прошедшие все три ступени, получают принципиально другой результат, чем те, кто остановился на&nbsp;первой.</p></details>
<details><summary>Что если пропущу набор между модулями?</summary><p>Можно продолжить со&nbsp;следующей группой: пауза в&nbsp;пару месяцев не&nbsp;критична, если ты&nbsp;держишь практику. Длинные перерывы обсуждаем лично, иногда полезнее пройти модуль заново.</p></details>
<details><summary>Модули проходят очно или онлайн?</summary><p>Очно, малым составом. Живая сцена и&nbsp;работа группы через экран не&nbsp;воспроизводятся. Онлайн проходит только сопровождение третьего модуля: еженедельные встречи команды.</p></details>
<details><summary>Сколько стоит участие?</summary><p>Условия обсуждаем лично, вместе с&nbsp;датами ближайшего набора. Для тех, кто пришёл с&nbsp;этого сайта, сам разговор бесплатный.</p></details>
<p style="margin-top:24px">Больше ответов: <a href="/chizhovy2/voprosy/">вопросы и&nbsp;ответы</a>, <a href="/chizhovy2/somneniya/">частые сомнения</a>, <a href="/chizhovy2/bezopasnost/">безопасность и&nbsp;границы</a>.</p>
<p style="margin-top:28px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a></p>
</div></section>
""")

# ================= МОДУЛЬ 1 =================
P["modul-1/index.html"] = ("Модуль I. Возвращение к себе · Настоящие отношения",
"Два с половиной дня: увидеть свои паттерны и их источники.", "modul-1", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-m1.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль I · два с&nbsp;половиной дня</p><h1>Возвращение к&nbsp;себе</h1>
<p class="lead">Первый модуль отвечает на&nbsp;вопрос, с&nbsp;которого начинается любой сдвиг: что со&nbsp;мной происходит на&nbsp;самом деле и&nbsp;откуда это&nbsp;взялось.</p></div></div>

<section><div class="narrow">
<h2>Что происходит за&nbsp;эти дни</h2>
<p>Пятничный вечер, суббота и&nbsp;воскресенье. Погружение начинается с&nbsp;эмоционального входа в&nbsp;пространство тренинга: телефоны в&nbsp;сторону, маски снимаются постепенно и&nbsp;сами.</p>
<div class="card white" style="margin:18px 0 12px">{icon('book')}<h3>Видишь, что повторяется</h3><p>Повторяющиеся реакции, роли и&nbsp;установки, из&nbsp;которых соткан твой день: где ты&nbsp;терпишь, где убегаешь, где стараешься казаться.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('route','var(--sage-deep)')}<h3>Находишь, откуда это взялось</h3><p>В&nbsp;живых процессах видно, где было принято старое решение и&nbsp;чью интонацию ты&nbsp;до&nbsp;сих пор носишь как&nbsp;свою.</p></div>
<div class="card white">{icon('lens','var(--sand)')}<h3>Снова слышишь себя</h3><p>К&nbsp;воскресному вечеру появляется то, что участники называют «впервые за&nbsp;годы услышал себя». Отсюда начинается настоящая работа.</p></div>
<div class="pull"><div class="q">«Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка колоссальная.»</div><div class="who">Участник первого модуля</div></div>
<p><strong>Результат модуля: осознанность.</strong> Ты&nbsp;видишь свою запись. Развидеть её&nbsp;уже не&nbsp;получится, и&nbsp;это лучшее, что могло&nbsp;случиться.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">По часам</p>
<h2>Как устроены два с&nbsp;половиной дня</h2>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">1</span>{icon('speech')}<h3>Вечер пятницы</h3><p>Знакомство группы и&nbsp;вход в&nbsp;пространство. Первые честные ответы на&nbsp;вопрос «зачем я&nbsp;здесь». К&nbsp;концу вечера зал перестаёт быть комнатой незнакомых людей.</p></div>
<div class="card"><span class="bignum">2</span>{icon('people','var(--sage-deep)')}<h3>Суббота</h3><p>Самый длинный день: живые процессы, работа в&nbsp;парах и&nbsp;группе, первые сцены. Здесь обычно и&nbsp;случается то, ради чего люди приезжают.</p></div>
<div class="card"><span class="bignum">3</span>{icon('sunrise','var(--sand)')}<h3>Воскресенье</h3><p>Сборка: что увидел, что с&nbsp;этим делать в&nbsp;понедельник. Договорённости с&nbsp;собой на&nbsp;недели интеграции до&nbsp;второго модуля.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>С чем работают на&nbsp;первом модуле</h2>
<p>Материал приносишь ты: свою реальную жизнь, а&nbsp;не&nbsp;учебные задачи. Чаще всего в&nbsp;зале звучат такие темы.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('loop')}<h3>Повторяющиеся ссоры</h3><p>Один и&nbsp;тот&nbsp;же сюжет с&nbsp;партнёром, родителями или на&nbsp;работе. Смотрим, в&nbsp;какой точке круг замыкается.</p></div>
<div class="card">{icon('shield','var(--sage-deep)')}<h3>Роли, которые надоели</h3><p>Сильный, удобная, спасатель, тот, кто всегда справится. Откуда роль взялась и&nbsp;что будет, если её&nbsp;снять.</p></div>
<div class="card">{icon('book','var(--sand)')}<h3>Установки из&nbsp;детства</h3><p>«Просить стыдно», «злиться опасно», «я&nbsp;сам». Находим, чьим голосом они сказаны впервые.</p></div>
<div class="card">{icon('flame')}<h3>Замороженные чувства</h3><p>Место, где когда-то было больно и&nbsp;пришлось закрыться. Оживляем бережно и&nbsp;по&nbsp;шагам.</p></div>
</div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что забирают с&nbsp;собой</h2>
<p>Первый модуль не&nbsp;решает всё: он&nbsp;открывает глаза и&nbsp;даёт первые инструменты. Дальше идут недели интеграции, когда увиденное проверяется обычной жизнью, а&nbsp;за&nbsp;ними <a href="/chizhovy2/modul-2/" style="color:#D08A5F">второй модуль</a>, где старые решения переписываются.</p>
<div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>2,5 дня</b><span>вечер пятницы плюс выходные, без отрыва от&nbsp;работы</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе, каждого знаем по&nbsp;имени</span></div>
<div class="nail"><b>3-5 недель</b><span>интеграции до&nbsp;следующего модуля</span></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Кто приезжает на&nbsp;первый модуль</h2>
<p>Люди, у&nbsp;которых снаружи в&nbsp;основном порядок, а&nbsp;внутри давно не&nbsp;складывается: <a href="/chizhovy2/dlya-predprinimatelej/">предприниматели</a> в&nbsp;усталости, <a href="/chizhovy2/para/">пары</a> в&nbsp;тихом кризисе, <a href="/chizhovy2/dlya-zhenshchin/">женщины</a>, которые устали жить в&nbsp;режиме ожидания. Возраст обычно от&nbsp;тридцати до&nbsp;пятидесяти.</p>
<p>Специальной подготовки не&nbsp;нужно: ни&nbsp;книг, ни&nbsp;опыта терапии, ни&nbsp;умения красиво говорить о&nbsp;чувствах. Нужна готовность три дня быть честным с&nbsp;собой. Как проходит вход в&nbsp;школу и&nbsp;почему через разговор, описано на&nbsp;странице <a href="/chizhovy2/sessiya/">собеседования</a>.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Начать с&nbsp;собеседования</a> <a class="btn btn-ghost" href="/chizhovy2/modul-2/" style="margin-left:8px">Дальше: Модуль II</a></p>
</div></section>
""")

# ================= МОДУЛЬ 2 =================
P["modul-2/index.html"] = ("Модуль II. Внутренняя свобода · Настоящие отношения",
"Пять дней глубокой работы: страх, вина, обида, внутренняя опора.", "modul-2", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-dark.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль II · пять дней</p><h1>Внутренняя свобода</h1>
<p class="lead">Самый глубокий модуль школы. Пять дней, после которых вина, тревога и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p></div></div>

<section><div class="narrow">
<h2>С чем работаем</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('flame')}<h3>Страх и&nbsp;важность</h3><p>Разбираем, как раздутая ставка парализует действия, и&nbsp;возвращаем способность выбирать спокойно.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Вина и&nbsp;ответственность</h3><p>Первая сливает энергию и&nbsp;притягивает наказание, вторая возвращает силу. Учимся различать их&nbsp;телом.</p></div>
<div class="card">{icon('loop','var(--sand)')}<h3>Обида</h3><p>Старые обиды держат сценарии годами. Проживаем их&nbsp;до&nbsp;конца в&nbsp;безопасном пространстве группы.</p></div>
<div class="card">{icon('mountain')}<h3>Внутренняя опора</h3><p>Собираем состояние, в&nbsp;котором ты&nbsp;не&nbsp;зависишь от&nbsp;оценки, настроения партнёра и&nbsp;погоды на&nbsp;рынке.</p></div>
</div>
<div class="pull"><div class="q">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше.»</div><div class="who">Участник второго модуля</div></div>
<p><strong>Результат модуля: сила, спокойствие, ясность.</strong> Плюс инструменты, которыми ты&nbsp;дальше пользуешься сам: тело помнит, как выходить из&nbsp;захвата.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Пять дней</p>
<h2>Почему именно столько</h2>
<p class="sub">За выходные психика едва успевает открыться, а&nbsp;перестроиться уже нет. Пять дней подряд дают то, ради чего существует формат погружения: защиты снимаются, и&nbsp;работа идёт на&nbsp;той глубине, куда обычная жизнь не&nbsp;пускает.</p>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">1-2</span>{icon('layers')}<h3>Первые дни</h3><p>Разгон и&nbsp;снятие брони. Здесь становится видно, сколько сил уходило на&nbsp;поддержание образа «у&nbsp;меня всё хорошо».</p></div>
<div class="card"><span class="bignum">3</span>{icon('flame','var(--sage-deep)')}<h3>Третий день</h3><p>Самый плотный. Обычно именно тут человек доходит до&nbsp;решения, которое принял двадцать или тридцать лет назад, и&nbsp;встречается с&nbsp;ним лицом к&nbsp;лицу.</p></div>
<div class="card"><span class="bignum">4-5</span>{icon('mountain','var(--sand)')}<h3>Последние дни</h3><p>Сборка нового: опора, спокойствие, договорённости с&nbsp;собой. Возвращение в&nbsp;жизнь происходит мягко, а&nbsp;не&nbsp;как выброс из&nbsp;самолёта.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Что меняется после второго модуля</h2>
<p>Первый модуль показывает запись, второй её&nbsp;переписывает. Разница чувствуется в&nbsp;мелочах: в&nbsp;том, как ты&nbsp;реагируешь на&nbsp;резкое слово, как принимаешь решения под давлением, сколько сил остаётся к&nbsp;вечеру.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('speech')}<h3>Разговоры становятся другими</h3><p>Появляется пауза между уколом и&nbsp;ответом. В&nbsp;эту паузу помещается выбор, которого раньше просто не&nbsp;было.</p></div>
<div class="card">{icon('ceiling','var(--sage-deep)')}<h3>Решения даются легче</h3><p>Когда страх перестаёт диктовать, большие ходы в&nbsp;деле и&nbsp;в&nbsp;жизни уходят из&nbsp;режима «потом».</p></div>
<div class="card">{icon('cups','var(--sand)')}<h3>Дома стало теплее</h3><p>Часть напряжения в&nbsp;паре держалась на&nbsp;твоей половине общего сценария. Убирается одна сторона, меняется вся конструкция.</p></div>
<div class="card">{icon('hourglass')}<h3>Энергии больше</h3><p>Силы, которые уходили на&nbsp;удержание брони и&nbsp;старых обид, освобождаются. Это замечают первым делом близкие.</p></div>
</div>
<p class="note" style="margin-top:20px">Инструменты, которые остаются: <a href="/chizhovy2/praktiki/">ежедневные практики</a>, работа с&nbsp;состоянием и&nbsp;навык замечать <a href="/chizhovy2/slovar/">маятники</a> раньше, чем схватился.</p>
</div></section>

<section class="dark"><div class="narrow">
<h2>Честно о&nbsp;трудностях</h2>
<p>Пять дней бывают тяжёлыми. Слёзы в&nbsp;зале это норма, усталость к&nbsp;середине тоже. Иногда человек упирается и&nbsp;злится на&nbsp;ведущих: сопротивление здесь ожидаемо, и&nbsp;мы&nbsp;к&nbsp;нему готовы.</p>
<p>При этом никто не&nbsp;ломает тебя через колено: глубина добровольна, темп твой, остановиться можно в&nbsp;любой момент. Правила зала и&nbsp;границы работы описаны на&nbsp;странице <a href="/chizhovy2/bezopasnost/" style="color:#D08A5F">безопасности</a>.</p>
</div></section>

<section><div class="narrow">
<p>Второй модуль идут те, кто прошёл <a href="/chizhovy2/modul-1/">первый</a> и&nbsp;выдержал недели интеграции: увидел свою запись в&nbsp;деле и&nbsp;захотел с&nbsp;ней разобраться. Дальше <a href="/chizhovy2/marafon/">Марафон</a>, где новое поведение закрепляется девяноста днями практики.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Занять место</a> <a class="btn btn-ghost" href="/chizhovy2/marafon/" style="margin-left:8px">Дальше: Марафон</a></p>
</div></section>
""")

# ================= МАРАФОН =================
P["marafon/index.html"] = ("Модуль III. Создатель реальности · Настоящие отношения",
"Три месяца практики в жизни: команда, еженедельные встречи, результаты, которые остаются.", "marafon", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-10.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль III · три месяца</p><h1>Создатель реальности</h1>
<p class="lead">Инсайты выветриваются за&nbsp;две недели, если их&nbsp;не&nbsp;закрепить действиями. Марафон нужен ровно для&nbsp;этого: три месяца ты&nbsp;каждый день пробуешь новое в&nbsp;обычной жизни, пока оно не&nbsp;станет твоим.</p></div></div>

<section><div class="narrow">
<h2>Как устроены три месяца</h2>
<div class="card white" style="margin:20px 0 12px">{icon('people')}<h3>Команда</h3><p>Ты&nbsp;идёшь не&nbsp;один: рядом люди с&nbsp;общей целью и&nbsp;напарник у&nbsp;каждого. Поддержка работает даже в&nbsp;два часа ночи.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('speech','var(--sage-deep)')}<h3>Еженедельные встречи</h3><p>Разборы с&nbsp;Алексеем и&nbsp;Ириной: что получилось, где старая запись взяла своё, какой следующий шаг.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('sunrise','var(--sand)')}<h3>Ежедневная практика</h3><p>Утром формулируешь главный фокус дня, вечером подводишь итог: открытия и&nbsp;благодарности. Простая дисциплина, которая за&nbsp;90&nbsp;дней перепрошивает привычный способ&nbsp;жить.</p></div>
<div class="card white">{icon('target')}<h3>Реальные цели</h3><p>Работа идёт на&nbsp;твоих живых задачах: дело, деньги, отношения, тело. Смотрим на&nbsp;факты, а&nbsp;не&nbsp;на&nbsp;ощущения.</p></div>

<div class="pull"><div class="q">«Раньше я&nbsp;отсеивал людей по&nbsp;уровню жизни. Сейчас просто строю настоящие отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами.»</div><div class="who">Выпускник Марафона, предприниматель</div></div>
<p><strong>Итог: другие поступки и&nbsp;новые результаты.</strong> Не&nbsp;состояние после тренинга, а&nbsp;жизнь, которая продолжает расти,&nbsp;когда сопровождение&nbsp;закончилось.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Девяносто дней</p>
<h2>Как выглядит неделя на&nbsp;Марафоне</h2>
<p class="sub">Ритм простой и&nbsp;повторяемый: он&nbsp;и&nbsp;делает работу. Ничего героического, всё встраивается в&nbsp;обычную жизнь с&nbsp;работой и&nbsp;детьми.</p>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('sunrise')}<h3>Каждое утро</h3><p>Намерение на&nbsp;день в&nbsp;командный чат: из&nbsp;какого состояния иду и&nbsp;что создаю. Две минуты, которые задают тон всему&nbsp;дню.</p></div>
<div class="card">{icon('calendar','var(--sage-deep)')}<h3>Каждый вечер</h3><p>Открытия и&nbsp;благодарности: что понял про себя, где старая запись взяла своё, за&nbsp;что спасибо дню и&nbsp;людям.</p></div>
<div class="card">{icon('people','var(--sand)')}<h3>Раз в&nbsp;неделю</h3><p>Живая встреча с&nbsp;Алексеем и&nbsp;Ириной: разбор ситуаций недели, ответы на&nbsp;вопросы, следующий шаг для каждого.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Почему так долго</h2>
<p>После погружения человек возвращается в&nbsp;ту&nbsp;же квартиру, к&nbsp;тем&nbsp;же людям и&nbsp;в&nbsp;тот&nbsp;же рабочий чат. Всё вокруг помнит его прежним и&nbsp;мягко тянет обратно в&nbsp;знакомую роль. Без поддержки на&nbsp;этом отрезке инсайты выветриваются за&nbsp;пару недель: это главная причина, по&nbsp;которой тренинги «не&nbsp;работают».</p>
<p>Марафон закрывает именно этот разрыв. Каждый день ты&nbsp;делаешь новый выбор в&nbsp;реальных обстоятельствах, каждую неделю приносишь результат на&nbsp;разбор, и&nbsp;рядом идёт команда, которая видит твои сдвиги со&nbsp;стороны. За&nbsp;девяносто дней новое поведение перестаёт требовать усилий.</p>
<div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>90 дней</b><span>ежедневной практики в&nbsp;обычной&nbsp;жизни</span></div>
<div class="nail"><b>13</b><span>недель с&nbsp;разбором у&nbsp;ведущих</span></div>
<div class="nail"><b>1</b><span>напарник, который держит, когда тяжело</span></div>
</div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Над чем работают участники</h2>
<p>Цели приносит каждый свои, и&nbsp;они всегда из&nbsp;настоящей жизни: запустить дело, которое откладывалось три года. Восстановить отношения с&nbsp;отцом. Выйти из&nbsp;найма. Вернуть спорт. Перестать срываться на&nbsp;детей. Сделать предложение. Уехать в&nbsp;поездку, на&nbsp;которую полгода не&nbsp;решался.</p>
<p>Итог меряем фактами: сделал или отложил, поговорил или снова промолчал. Что из&nbsp;этого выходит на&nbsp;практике, видно в&nbsp;<a href="/chizhovy2/istorii/komanda-mir/" style="color:#D08A5F">истории команды «МИР»</a>.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Выпуски Марафона</p>
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-10.jpg" alt="Команда Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-11.jpg" alt="Выпуск Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-13.jpg" alt="Финал модуля" loading="lazy"></div>
</div>
<p style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Обсудить участие на&nbsp;собеседовании</a></p>
</div></section>
""")

# ================= ДЛЯ ПАР =================
P["para/index.html"] = ("Тренинг для пар · Настоящие отношения",
"Муж и жена проходят тренинг вместе: близость растёт с двух сторон.", "para", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-para-itog.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Для пар</p><h1>Когда приходят вдвоём, меняются оба</h1>
<p class="lead">Годами ездить на&nbsp;тренинги и возвращаться домой, где партнёр остался прежним, тяжело. А&nbsp;можно прийти вдвоём и&nbsp;переписать общий сценарий с&nbsp;двух сторон сразу.</p></div></div>

<section><div class="narrow">
<h2>Что происходит с&nbsp;парой</h2>
<p>У&nbsp;двоих всегда две записи, и&nbsp;они цепляются друг за&nbsp;друга, как шестерёнки: её&nbsp;обида включает его&nbsp;тишину, а&nbsp;тишина кормит обиду. На&nbsp;тренинге каждый работает со&nbsp;своей записью, и&nbsp;шестерёнки&nbsp;расцепляются.</p>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('mountain')}<h3>Он</h3><p>Возвращает опору и&nbsp;уверенность: решения из&nbsp;спокойствия, дело и&nbsp;достаток растут без надрыва.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Она</h3><p>Оживает: раскрывается, вдохновляет, выходит из&nbsp;режима ожидания и&nbsp;обслуживания.</p></div>
</div>
<p style="margin-top:24px">Дальше начинается то, ради чего школа носит своё имя: <strong>настоящие отношения.</strong> Разговоры, которые заканчиваются ближе, чем начинались. Быт, в&nbsp;котором снова видно человека. Общие цели вместо параллельных жизней.</p>
<p>Пары в&nbsp;зале работают наравне со&nbsp;всеми: одни процессы вместе, другие по&nbsp;отдельности. Прийти одному тоже можно: отношения меняются, даже когда запись переписывает один из&nbsp;двоих.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Знакомые ситуации</p>
<h2>С чем приходят пары</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('cups')}<h3>Соседи по&nbsp;квартире</h3><p>Общий календарь, счёт и&nbsp;дети. Разговоры про логистику. Не&nbsp;ссоритесь, потому что&nbsp;незачем.</p></div>
<div class="card">{icon('loop','var(--sage-deep)')}<h3>Ссоры по&nbsp;кругу</h3><p>Один и&nbsp;тот&nbsp;же сценарий с&nbsp;теми&nbsp;же словами и&nbsp;финалом. Повод разный, спектакль один и&nbsp;тот&nbsp;же.</p></div>
<div class="card">{icon('speech','var(--sand)')}<h3>Стена молчания</h3><p>Он&nbsp;уходит в&nbsp;себя, она добивается ответа, он&nbsp;закрывается сильнее. Знакомый круг, из&nbsp;которого не&nbsp;выйти уговорами.</p></div>
<div class="card">{icon('flame')}<h3>Близости почти не осталось</h3><p>Тепло ушло в&nbsp;быт, нежность стала редкостью. Оба помнят, как было, и&nbsp;оба не&nbsp;знают, куда это делось.</p></div>
<div class="card">{icon('ceiling','var(--sage-deep)')}<h3>Кризис после десяти лет</h3><p>Дети подросли, цели достигнуты, и&nbsp;вдруг непонятно, что дальше и&nbsp;зачем вместе.</p></div>
<div class="card">{icon('mirror','var(--sand)')}<h3>Один меняется, другой на месте</h3><p>Один меняется, другой остаётся. Расстояние растёт молча, пока однажды не&nbsp;становится слишком большим.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Почему вдвоём сильнее</h2>
<p>Когда один приносит домой новое понимание, второй его не&nbsp;разделяет: слова звучат чужими, изменения выглядят как претензия. Это нормальная реакция и&nbsp;частая причина, по&nbsp;которой хорошая работа одного упирается в&nbsp;стену.</p>
<p>Когда проходят оба, общий язык появляется сразу. Вы&nbsp;видели одно и&nbsp;то&nbsp;же, называете вещи одними словами и&nbsp;дома продолжаете разговор, а&nbsp;не&nbsp;начинаете спор заново. Дальше это превращается в&nbsp;навык: слышать друг друга там, где обычно включался старый сценарий.</p>
<div class="pull"><div class="q">«Мы перестали выяснять, кто прав. Стало интересно, что с&nbsp;ним происходит на&nbsp;самом деле.»</div><div class="who">Участница, прошла модули вместе с&nbsp;мужем</div></div>
<p>Если партнёр пока не&nbsp;готов, приходить одному не&nbsp;только можно, но&nbsp;и&nbsp;полезно: твоя половина общего сценария в&nbsp;твоих руках, а&nbsp;шестерёнка перестаёт крутиться, когда останавливается одна из&nbsp;двух. Частые опасения на&nbsp;этот счёт разобраны на&nbsp;странице <a href="/chizhovy2/somneniya/">сомнений</a>.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться вдвоём</a> <a class="btn btn-ghost" href="/chizhovy2/programma/" style="margin-left:8px">Программа целиком</a></p>
</div></section>
""")

# ================= ВЕДУЩИЕ =================
P["vedushchie/index.html"] = ("Алексей и Ирина Чижовы · Настоящие отношения",
"Ведущие школы: коуч ICF и трансформационный тренер, вместе 17 лет.", "vedushchie", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/portret.jpg');background-position:center 25%"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Ведущие</p><h1>Алексей и&nbsp;<span class="kpm">Ирина Чижовы</span></h1>
<p class="lead">Школу отношений ведёт пара, которая 17&nbsp;лет живёт вместе: быт, кризисы и&nbsp;выход из&nbsp;них они прошли сами. Поэтому в&nbsp;зале нет теории с&nbsp;чужих слов.</p></div></div>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Кто ведёт</p>
<h2>Двое, которые живут так, как&nbsp;учат</h2>
<div class="grid2" style="margin-top:24px">
<div class="card white">{icon('mountain')}<h3>Алексей</h3><p>Коуч с&nbsp;сертификацией ICF, 16&nbsp;лет практики. Держит структуру и&nbsp;точность процесса: с&nbsp;ним безопасно идти в&nbsp;глубину, потому что он&nbsp;видит дорогу&nbsp;целиком.</p></div>
<div class="card white">{icon('flame','var(--sand)')}<h3>Ирина</h3><p>Трансформационный тренер. Шесть лет готовилась к&nbsp;этому формату под руководством наставника. Работает на&nbsp;глубине. Участники говорят, что она «вскрывает и&nbsp;собирает», и&nbsp;вспоминают её&nbsp;работу&nbsp;годами.</p></div>
</div>
<p style="margin-top:24px">Роли в&nbsp;зале дополняют друг друга: его&nbsp;опора и&nbsp;её&nbsp;чувствование, структура и&nbsp;глубина. В&nbsp;паре ведущих это видно с&nbsp;первого часа: один размечает дорогу, вторая идёт туда, где живое.</p>
<p>Поэтому здесь не&nbsp;учат жить и&nbsp;не&nbsp;мотивируют. Вместе разбираются, откуда берётся твоя реакция и&nbsp;по&nbsp;какой причине в&nbsp;паре повторяется один сюжет. Иногда непросто. Зато по-настоящему.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Вместе</div><div class="big">17 лет</div><p>Свой быт, свои кризисы и&nbsp;свои выходы из&nbsp;них. Отношения, о&nbsp;которых говорят в&nbsp;зале, они строят каждый&nbsp;день.</p></div>
<div class="box"><div class="lbl">Из чата команды</div><div class="cit">«Благодарю Ирину и&nbsp;Алексея за&nbsp;вклад в&nbsp;мою&nbsp;трансформацию.»</div><div class="who">Солвита И., участница третьего модуля</div></div>
</aside>
</div></div></section>

<section class="dark"><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как они пришли к&nbsp;этому</p>
<h2>Сначала своя жизнь, потом&nbsp;зал</h2>
<p>Школа выросла не&nbsp;из&nbsp;теории. Сначала были свои повторяющиеся круги: разговоры на&nbsp;одних и&nbsp;тех&nbsp;же местах, попытки договориться словами, откаты после хороших недель. Всё то, с&nbsp;чем люди приходят сюда сейчас. Знакомо изнутри.</p>
<div class="pull"><div class="q">«У&nbsp;нас не&nbsp;было идеальной истории. Было непонимание, ошибки, потери, моменты, где казалось: дальше некуда. Именно там началось настоящее.»</div><div class="who">Из обращения Алексея и&nbsp;Ирины к&nbsp;каналу школы</div></div>
<p>Дальше шестнадцать лет практики: сотни залов, тысячи разобранных сцен, свои ошибки ведущих и&nbsp;свои находки. Из&nbsp;пяти источников осталось то, что реально меняет жизнь участников, остальное отсеялось. Как именно отбирали, разобрано в&nbsp;<a href="/chizhovy2/istoki/" style="color:#D08A5F">истоках метода</a>.</p>
<p>Ирина шесть лет готовилась к&nbsp;этому формату под руководством наставника, прежде чем встать в&nbsp;пару ведущих. Не&nbsp;курс выходного дня, а&nbsp;долгая работа с&nbsp;собственной глубиной: вести человека можно только туда, где был сам. Иначе никак.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Практика</div><div class="big">16 лет</div><p>Столько за&nbsp;спиной у&nbsp;Алексея: залы, группы, сопровождение. Метод собран и&nbsp;проверен на&nbsp;этой&nbsp;дистанции.</p></div>
<div class="box"><div class="lbl">Подготовка Ирины</div><div class="big">6 лет</div><p>Под руководством наставника, до&nbsp;первого зала в&nbsp;роли&nbsp;ведущей.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<p class="eyebrow">Как они работают вместе</p>
<h2>Две роли в&nbsp;зале</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('mountain')}<h3>Он держит порядок и время</h3><p>Ведёт процесс и&nbsp;видит карту целиком. Знает, куда идти дальше и&nbsp;где остановиться. С&nbsp;таким ведущим не&nbsp;страшно заходить далеко: дорога размечена.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Она уводит вглубь</h3><p>Чувствует, что происходит с&nbsp;человеком, раньше слов. Идёт туда, где живое, и&nbsp;остаётся рядом до&nbsp;конца&nbsp;процесса.</p></div>
</div>
<p class="sub" style="margin-top:22px;max-width:none">Это те&nbsp;же два начала, которые мы&nbsp;помогаем соединить внутри каждого участника: опора и&nbsp;чувствительность, структура и&nbsp;живость. Пара ведущих показывает их&nbsp;в&nbsp;работе, а&nbsp;не&nbsp;объясняет на&nbsp;словах.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Дисциплина это часть метода</p>
<h2>Говорят только о&nbsp;том, что&nbsp;прошли сами</h2>
<div class="split" style="margin-top:28px">
<div class="ph"><img src="/chizhovy2/images/real/zabeg-selfi.jpg" alt="Алексей и Ирина на набережной после старта" loading="lazy"></div>
<div>
<p>Алексей: триатлет, финишер IronMan&nbsp;70.3. Не&nbsp;ради медалей. Длинная дистанция каждый день проверяет то, чему школа учит в&nbsp;зале. На&nbsp;трассе это видно буквально: сначала состояние, решения принимаются из&nbsp;спокойствия, а&nbsp;доходит тот, кто играет в&nbsp;долгую.</p>
<p>Команды школы выходят на&nbsp;забеги вместе: тело быстро выдаёт, где ты&nbsp;себя обманываешь, и&nbsp;честно радуется, когда ты&nbsp;настоящий.</p>
</div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Что видят участники</p>
<h2>Почему это важно для&nbsp;группы</h2>
<p>Когда школу отношений ведёт один человек, всегда остаётся вопрос: а&nbsp;как у&nbsp;него самого. Здесь ответ виден сразу: работают двое, вместе семнадцать лет, со&nbsp;своим бытом, своими кризисами и&nbsp;выходами из&nbsp;них.</p>
<p>В зале это даёт две вещи. Первое: любую семейную сцену участники разбирают с&nbsp;двух сторон, мужской и&nbsp;женской, без перекоса в&nbsp;чью-то пользу. Второе: ведущие не&nbsp;идеализируют отношения и&nbsp;не&nbsp;делают вид, что у&nbsp;них всё гладко. Об&nbsp;этом прямо сказано в&nbsp;<a href="/chizhovy2/manifest/">манифесте школы</a>.</p>
<p>Есть и&nbsp;третье, о&nbsp;котором говорят чаще всего: с&nbsp;группой остаются после модуля. Разборы каждую неделю, ответы в&nbsp;чате, поддержка на&nbsp;забегах и&nbsp;в&nbsp;два часа ночи. Как это устроено, видно на&nbsp;странице <a href="/chizhovy2/soobshchestvo/">сообщества</a>.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Слова участников</div><div class="cit">«Благодарен Ирине за&nbsp;её&nbsp;погружённость.»</div><div class="who">Из ежедневных записей команды</div></div>
<div class="box"><div class="cit">«Благодарю Алексея за&nbsp;разговор и&nbsp;включённость в&nbsp;мою жизнь.»</div><div class="who">Участник третьего модуля</div></div>
<div class="box"><div class="cit">«Спасибо за&nbsp;поддержку, понимание и&nbsp;пространство, где можно&nbsp;проявиться.»</div><div class="who">Из чата команды МИР</div></div>
</aside>
</div></div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Познакомиться лично</h2>
<p class="sub" style="margin:0 0 26px">Час разговора о&nbsp;твоей ситуации: смотрим, что происходит, и&nbsp;вместе решаем, по&nbsp;пути&nbsp;ли&nbsp;нам. Для&nbsp;читателей сайта бесплатно.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>
""")

P["otzyvy/index.html"] = ("Истории учеников · Настоящие отношения",
"Живые истории выпускников школы: до, во время и после тренинга.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-05.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истории учеников</p><h1>Их словами, без глянца</h1>
<p class="lead">Отзывы под рекламу мы&nbsp;не&nbsp;переписываем. Ниже живые фрагменты из&nbsp;анкет, чатов и&nbsp;писем, опубликованные с&nbsp;согласия авторов. Опыт у&nbsp;каждого свой. И&nbsp;результат&nbsp;тоже.</p></div></div>

<section><div class="narrow">
<!-- ПРОТОТИП: подписи и полные версии согласовать с авторами перед публикацией -->
<div class="card white" style="margin-bottom:16px">
<p class="eyebrow" style="margin-bottom:10px">Предприниматель, пришёл в самый тяжёлый момент</p>
<p>«Я&nbsp;находился в&nbsp;фазе, которую называют дном: кассовый разрыв, долги, расставание с&nbsp;девушкой, друзья отвернулись. Не&nbsp;хотелось ни&nbsp;с&nbsp;кем общаться, хотелось закрыться в&nbsp;коробочку и&nbsp;сидеть&nbsp;одному.</p>
<p>На&nbsp;тренинге я&nbsp;долго сопротивлялся, как баран. Труднее всего было принять точку&nbsp;А: признать, где я&nbsp;на&nbsp;самом деле. А&nbsp;потом увидел, что покупал отношения вместо того, чтобы их&nbsp;строить.</p>
<p style="margin-bottom:0">Сейчас строю настоящие отношения везде. Деньги начали приходить, энергии много, и&nbsp;я&nbsp;умею ей&nbsp;распоряжаться. Цели выросли кратно, научился играть в&nbsp;долгую. Одной фразой: получил новую версию&nbsp;себя».</p>
</div>
<div class="card white" style="margin-bottom:16px">
<p class="eyebrow" style="margin-bottom:10px">Участница второго модуля</p>
<p style="margin-bottom:0">«Годами затыкала свои боли: научилась обезболивать и&nbsp;не&nbsp;слышать себя, стала чёрствой к&nbsp;себе. На&nbsp;модуле впервые за&nbsp;много лет плакала при людях и&nbsp;поняла, что это не&nbsp;стыдно. Теперь знаю, что могу быть яркой, настоящей, звонкой, сама по&nbsp;себе».</p>
</div>
<div class="card white">
<p class="eyebrow" style="margin-bottom:10px">Выпускница Марафона</p>
<p style="margin-bottom:0">«Полгода не&nbsp;могла решиться, даже паспорт найти не&nbsp;могла. А&nbsp;сегодня внутри приняла решение, и&nbsp;паспорт нашёлся. Купила тур, еду на&nbsp;море на&nbsp;Новый год».</p>
</div>

<p style="margin-bottom:22px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Полные истории: с&nbsp;точкой&nbsp;А и&nbsp;переломом</a></p>
<div class="pull"><div class="q">«Моя жизнь точно разделена на&nbsp;до&nbsp;и&nbsp;после.»</div><div class="who">Участница школы</div></div>
<div class="pull"><div class="q">«Спасибо, что помогли прожить стену, которую я&nbsp;так долго строил. Теперь она мне не&nbsp;нужна.»</div><div class="who">Участник школы</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">По ступеням</p>
<h2>Что говорят после каждого модуля</h2>
<p class="sub">Слова разные, а&nbsp;узор один: сначала человек видит свою запись, потом снимает груз и&nbsp;переносит новое в&nbsp;жизнь.</p>
<div class="grid3" style="margin-top:26px">
<div class="card white"><p class="eyebrow" style="margin-bottom:10px">После модуля&nbsp;I</p>
<p class="serif" style="font-style:italic">«Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка колоссальная».</p>
<p class="serif" style="font-style:italic;margin-top:12px">«Впервые за&nbsp;годы услышал себя, а&nbsp;не&nbsp;то, что должен хотеть».</p></div>
<div class="card white"><p class="eyebrow" style="margin-bottom:10px">После модуля&nbsp;II</p>
<p class="serif" style="font-style:italic">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше».</p>
<p class="serif" style="font-style:italic;margin-top:12px">«Годами затыкала свои боли. Теперь знаю, что могу быть яркой и&nbsp;звонкой, сама по&nbsp;себе».</p></div>
<div class="card white"><p class="eyebrow" style="margin-bottom:10px">После Марафона</p>
<p class="serif" style="font-style:italic">«Раньше я&nbsp;отсеивал людей по&nbsp;уровню жизни. Сейчас просто строю настоящие отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами».</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">По сферам</p>
<h2>Где именно меняется жизнь</h2>
<p class="sub">Ниже четыре сферы и&nbsp;голоса участников о&nbsp;том, где перемены становятся заметны&nbsp;первыми.</p>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('cups')}<h3>Отношения</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Вместо эмоций решила стать вкладом в&nbsp;отношения, говорить с&nbsp;уважением и&nbsp;любовью. И&nbsp;вот первые ростки».</p></div>
<div class="card">{icon('ceiling','var(--sage-deep)')}<h3>Дело и&nbsp;достаток</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Деньги начали приходить, энергии много, и&nbsp;я&nbsp;умею ей&nbsp;распоряжаться. Цели кратно увеличились, научился играть в&nbsp;долгую».</p></div>
<div class="card">{icon('route','var(--sand)')}<h3>Решения</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Вчера писала намерение, а&nbsp;сегодня отследила, что оно сбылось. Яркая и&nbsp;расслабленная жизнь это моё».</p></div>
<div class="card">{icon('people')}<h3>Окружение</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Когда убираю фокус с&nbsp;себя и&nbsp;вовлечён в&nbsp;команду, энергия кратно растёт, и&nbsp;люди поворачиваются ко&nbsp;мне&nbsp;лицом».</p></div>
</div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Полные истории целиком</a></p>
</div></section>

<section class="dark"><div class="narrow">
<h2>Откуда эти отзывы</h2>
<p>Слова учеников мы&nbsp;не&nbsp;правим под рекламу. Заказных текстов здесь нет. Только живые куски: из&nbsp;анкет после модулей, из&nbsp;рабочих чатов команд, из&nbsp;писем, которые приходят спустя год после выпуска, когда человек давно живёт своей&nbsp;жизнью.</p>
<p>Каждый фрагмент публикуется с&nbsp;согласия автора. Без исключений. Имена чаще всего убираем: люди делятся личным, и&nbsp;это важнее красивой подписи. Суммы, сроки и&nbsp;скорость перемен у&nbsp;каждого свои, поэтому мы&nbsp;не&nbsp;обещаем повторения чужого результата и&nbsp;не&nbsp;выносим цифры дохода на&nbsp;витрину.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-03.jpg" alt="Группа выпуска" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-09.jpg" alt="Участники тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
</div>
<p style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Начать свою историю</a></p>
</div></section>
""")

# ================= ВОПРОСЫ =================
P["voprosy/index.html"] = ("Вопросы и ответы · Настоящие отношения",
"Честные ответы: формат, глубина, группа, условия участия.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Вопросы и&nbsp;ответы</p><h1>Что спрашивают перед стартом</h1>
<p class="lead">Собрали то, что чаще всего звучит на&nbsp;собеседованиях. Если своего вопроса не&nbsp;нашёл, задай его лично: контакты внизу.</p></div></div>

<section><div class="narrow">
<details><summary>На чём основан метод?</summary><p>На&nbsp;практической психологии: психодрама Якоба Морено, работа с&nbsp;состоянием и&nbsp;групповые процессы, проверенные за&nbsp;16&nbsp;лет практики. Глубину даём через живой опыт, объясняем через понятные механизмы работы мозга и&nbsp;тела. Все опоры метода мы&nbsp;показываем открыто: <a href="/chizhovy2/istoki/">раздел «Истоки»</a>.</p></details>
<details><summary>Я уже ходил к&nbsp;психологу. Чем это отличается?</summary><p>Личная терапия строится на&nbsp;разговоре, час в&nbsp;неделю. Здесь работа идёт в&nbsp;живых сценах, телом и&nbsp;эмоцией, в&nbsp;погружении на&nbsp;несколько дней. Инструменты разные, и&nbsp;они хорошо дополняют друг друга.</p></details>
<details><summary>Боюсь групповой работы. Придётся раскрываться перед&nbsp;чужими?</summary><p>Глубина всегда добровольна: никто не&nbsp;вытаскивает силой. Обычно уже к&nbsp;вечеру первого дня зал перестаёт быть чужим: у&nbsp;людей одинаковые боли, и&nbsp;в&nbsp;соседней истории ты&nbsp;узнаёшь свою.</p></details>
<details><summary>Можно прийти одному, без&nbsp;партнёра?</summary><p>Да. Большинство участников приходят по&nbsp;одному. Отношения меняются, даже когда работает один из&nbsp;двоих: твоя половина общего сценария в&nbsp;твоих руках.</p></details>
<details><summary>Сколько времени занимает программа?</summary><p>Модуль I: 2,5&nbsp;дня, пятничный вечер плюс выходные. Второй: пять дней подряд. Третий: три месяца сопровождения при обычной жизни. Между ступенями 3-5 недель.</p></details>
<details><summary>Что за собеседование и&nbsp;сколько оно стоит?</summary><p>Час личного разговора о&nbsp;твоей ситуации. Для тех, кто пришёл с&nbsp;этого сайта, собеседование бесплатное. По&nbsp;итогам обе стороны честно решают, идти&nbsp;ли дальше; условия модулей обсуждаются там&nbsp;же.</p></details>
<details><summary>Какие гарантии?</summary><p>Честная одна. Мы&nbsp;даём процесс, группу, сопровождение и&nbsp;16&nbsp;лет опыта. Дальше метод срабатывает ровно настолько, насколько включаешься ты, поэтому результат у&nbsp;каждого свой.</p></details>
<details><summary>Как попасть на тренинг?</summary><p>Школа растёт через рекомендации, без массовой рекламы. Первый шаг один для всех: собеседование. Запись через Telegram, кнопка ниже.</p></details>
<p style="margin-top:28px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a></p>
</div></section>
""")

# ================= СЕССИЯ =================
P["sessiya/index.html"] = ("Собеседование в школу · Настоящие отношения",
"Час живого разговора о твоей ситуации: как проходит, что спрашивают, что будет после. Для читателей сайта бесплатно.", "sessiya", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-sessiya.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Первый шаг</p><h1>Собеседование в&nbsp;школу</h1>
<p class="lead">Час живого разговора о&nbsp;твоей ситуации. Знакомимся, разбираемся вместе и&nbsp;решаем, по&nbsp;пути ли&nbsp;нам. Для&nbsp;читателей сайта бесплатно.</p>
<div class="acts"><a class="btn btn-copper" href="https://t.me/+LVptSH6Mt4hhYmFi">Записаться</a><a class="btn btn-ghost" href="#kak">Что будет на&nbsp;разговоре</a></div>
</div></div>

<section id="kak"><div class="narrow">
<h2>Как проходит</h2>
<div class="card white" style="margin:20px 0 12px">{icon('speech')}<h3>Ты рассказываешь</h3><p>Что происходит и&nbsp;что уже пробовал. Без подготовки и&nbsp;правильных слов: как&nbsp;есть. Сумбурно, с&nbsp;паузами, перескакивая с&nbsp;темы на&nbsp;тему: нормально. Мы&nbsp;слушаем и&nbsp;задаём вопросы.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('gear','var(--sage-deep)')}<h3>Разбираем, как это устроено</h3><p>Где в&nbsp;твоей истории крутится сценарий и&nbsp;что его держит. Обычно уже этот час даёт первое «вот оно&nbsp;что»: человек видит свой круг со&nbsp;стороны, часто впервые за&nbsp;годы. Опора та&nbsp;же, что и&nbsp;в&nbsp;зале: <a href="/chizhovy2/metod/">событийный круг</a> из&nbsp;четырёх точек.</p></div>
<div class="card white">{icon('route','var(--sand)')}<h3>Вместе решаем, что дальше</h3><p>Годится&nbsp;ли тебе школа, с&nbsp;какого модуля заходить и&nbsp;стоит&nbsp;ли вообще. Отговорить можем так&nbsp;же честно, как&nbsp;пригласить. Условия участия обсудим здесь&nbsp;же, спокойно и&nbsp;без давления.</p></div>

<div class="nails nails3" style="margin-top:28px">
<div class="nail"><b>60&nbsp;минут</b><span>личного разговора, онлайн или&nbsp;очно</span></div>
<div class="nail"><b>Бесплатно</b><span>для тех, кто пришёл с&nbsp;этого&nbsp;сайта</span></div>
<div class="nail"><b>0</b><span>обязательств: решение принимаешь&nbsp;потом</span></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Чтобы не&nbsp;было сюрпризов</p>
<h2>О чём обычно спрашиваем</h2>
<p class="sub">Готовиться не&nbsp;нужно, но&nbsp;если хочется понимать заранее, вот примерные направления разговора. Отвечать на&nbsp;все не&nbsp;обязательно.</p>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('target')}<h3>Что происходит сейчас</h3><p>Какая ситуация привела тебя сюда: отношения, состояние, дело, здоровье. Что именно болит и&nbsp;как&nbsp;давно.</p></div>
<div class="card">{icon('loop','var(--sage-deep)')}<h3>Что повторяется</h3><p>Есть&nbsp;ли сюжет, который идёт по&nbsp;кругу с&nbsp;разными людьми или в&nbsp;разных местах. Обычно человек называет его сам за&nbsp;пять&nbsp;минут.</p></div>
<div class="card">{icon('book','var(--sand)')}<h3>Что уже пробовал</h3><p>Книги, курсы, терапия, спорт, смена работы. Это важно: значит, ты&nbsp;не&nbsp;сидел сложа руки, и&nbsp;мы&nbsp;не&nbsp;будем предлагать пройденное.</p></div>
<div class="card">{icon('sunrise')}<h3>К чему хочешь прийти</h3><p>Как выглядит жизнь, ради которой стоит идти в&nbsp;работу. Даже приблизительный ответ показывает направление.</p></div>
</div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Чего на&nbsp;собеседовании не&nbsp;будет</h2>
<p>Мы&nbsp;знаем, чего люди опасаются, когда идут «на&nbsp;разговор со&nbsp;школой». Поэтому говорим прямо.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('shield','var(--copper)')}<h3>Давления и&nbsp;дожима</h3><p>Никаких «места заканчиваются, решай сейчас». Думай столько, сколько нужно: неделю, месяц, полгода.</p></div>
<div class="card">{icon('speech','var(--copper)')}<h3>Скриптов и&nbsp;менеджеров</h3><p>Разговор ведут те, кто ведёт группы. Не&nbsp;отдел продаж и&nbsp;не&nbsp;бот с&nbsp;анкетой.</p></div>
<div class="card">{icon('lens','var(--copper)')}<h3>Ярлыков и&nbsp;диагнозов</h3><p>Мы&nbsp;не&nbsp;объясняем человеку, какой он, и&nbsp;не&nbsp;выдаём заключений. Смотрим на&nbsp;механику повтора, а&nbsp;не&nbsp;на&nbsp;личность.</p></div>
<div class="card">{icon('gear','var(--copper)')}<h3>Обещаний чуда</h3><p>Гарантий перемен не&nbsp;даём: метод срабатывает там, где человек включается сам. Об&nbsp;этом честно говорим сразу.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Что происходит после</h2>
<p>Если по&nbsp;итогам разговора мы&nbsp;оба видим, что дорога общая, ты&nbsp;узнаёшь даты ближайшего набора, условия участия и&nbsp;с&nbsp;какого модуля заходить: чаще всего это первый, 2,5&nbsp;дня. Дальше решение за&nbsp;тобой: никто не&nbsp;звонит с&nbsp;напоминаниями и&nbsp;не&nbsp;шлёт «последний шанс».</p>
<p>Если видим, что сейчас не&nbsp;время или задача не&nbsp;наша, тоже скажем прямо и&nbsp;подскажем, куда смотреть. Такие разговоры у&nbsp;нас бывают, и&nbsp;мы&nbsp;считаем их&nbsp;нормальной частью работы: <a href="/chizhovy2/bezopasnost/">границы описаны отдельно</a>.</p>
<div class="pull"><div class="q">«Труднее всего было принять точку&nbsp;А. Принять, что мир это зеркало, и&nbsp;всё, что со&nbsp;мной происходит, я&nbsp;транслирую сам.»</div><div class="who">Участник тренинга</div></div>
<p>Многие говорят, что сам этот час уже сдвинул что-то с&nbsp;места: за&nbsp;16&nbsp;лет через такие встречи прошли сотни человек, а&nbsp;в&nbsp;группу мы&nbsp;берём по&nbsp;10-20. Так и&nbsp;задумано: беседа строится по&nbsp;той&nbsp;же логике, что и&nbsp;работа в&nbsp;зале, просто в&nbsp;очень коротком формате. Что бывает дальше, можно почитать в&nbsp;<a href="/chizhovy2/istorii/">историях учеников</a>, а&nbsp;частые опасения разобраны на&nbsp;странице <a href="/chizhovy2/somneniya/">сомнений</a>.</p>
</div></section>

<section style="padding-top:0"><div class="narrow">
<div style="background:var(--linen);border:1px solid var(--line);border-radius:10px;padding:34px">
<h3 style="font-size:1.5rem">Записаться</h3>
<p class="sub" style="margin:10px auto 22px">Напиши слово «собеседование» в&nbsp;наш Telegram, и&nbsp;мы&nbsp;согласуем время. Отвечаем лично, без ботов и&nbsp;рассылок.</p>
<a class="btn btn-wine" href="https://t.me/+LVptSH6Mt4hhYmFi">Написать в&nbsp;Telegram</a>
<p class="note" style="margin-top:18px">Ещё не&nbsp;готов писать? Начни с&nbsp;<a href="/chizhovy2/gid/">бесплатного гайда</a>: там ядро метода и&nbsp;самодиагностика на&nbsp;десять пунктов.</p>
</div>
</div></section>
""")

# ================= ИСТОКИ МЕТОДА =================

def splav_svg():
    """Истоки-обзор: пять источников сходятся в знак школы и уходят в зал."""
    src = [(90,"Морено","сцена"),(270,"Зеланд","язык"),(450,"est","формат"),(630,"Годдард","состояние"),(810,"Наука","проверка")]
    heads = ""
    for x,name,cap in src:
        heads += f"""<circle cx="{x}" cy="46" r="26" fill="#FFFFFF" stroke="rgba(110,59,75,.3)" stroke-width="1.5"/>
<text x="{x}" y="42" text-anchor="middle" font-family="Manrope,sans-serif" font-weight="800" font-size="12.5" fill="#322D2B">{name}</text>
<text x="{x}" y="56" text-anchor="middle" font-family="Manrope,sans-serif" font-size="10" fill="#8C8378">{cap}</text>
<path d="M{x} 76 C {x} 120 450 116 450 152" fill="none" stroke="#B8935F" stroke-width="1.6"/>"""
    return f"""<svg viewBox="0 0 900 320" role="img" aria-label="Пять истоков сходятся в метод школы" style="width:100%;height:auto">
{heads}
<g>
<circle cx="432" cy="196" r="34" fill="none" stroke="#7D8C74" stroke-width="3"/>
<circle cx="468" cy="196" r="34" fill="none" stroke="#6E3B4B" stroke-width="3"/>
<path d="M450 166.6 A34 34 0 0 1 450 225.4 A34 34 0 0 1 450 166.6 Z" fill="#6E3B4B" opacity=".9"/>
</g>
<text x="450" y="258" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="19" fill="#322D2B">Метод школы</text>
<path d="M450 268 v18" stroke="#B8935F" stroke-width="2"/>
<path d="M450 292 l-7 -8 h14 z" fill="#B8935F"/>
<text x="450" y="312" text-anchor="middle" font-family="Manrope,sans-serif" font-size="12.5" fill="#655C55">проверено залом: 16 лет, сотни историй</text>
</svg>"""

def est_lenta_svg():
    """Лента времени жанра погружения: от est до школы."""
    pts = [(120,"1971","Сан-Франциско: первый est","#6E3B4B","#FAF5F0"),(370,"1976","Рейнхарт пишет «Книгу est»","#B8935F","#1B1410"),(620,"13 лет","сотни тысяч выпускников","#5C6B54","#F3F1EA"),(830,"сегодня","камерные школы глубины","#17222C","#D08A5F")]
    g = ""
    for x,year,cap,bg,fg in pts:
        g += f"""<circle cx="{x}" cy="64" r="31" fill="{bg}"/>
<text x="{x}" y="70" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-size="14.5" fill="{fg}">{year}</text>
<text x="{x}" y="120" text-anchor="middle" font-family="Manrope,sans-serif" font-weight="700" font-size="12.5" fill="#322D2B">{cap.split(":")[0] if ":" in cap else cap}</text>"""
        if ":" in cap:
            g += f"""<text x="{x}" y="137" text-anchor="middle" font-family="Manrope,sans-serif" font-size="11.5" fill="#655C55">{cap.split(":")[1].strip()}</text>"""
    return f"""<svg viewBox="0 0 940 160" role="img" aria-label="Лента жанра: от est 1971 года до сегодняшних школ" style="width:100%;height:auto;min-width:680px">
<line x1="70" y1="64" x2="880" y2="64" stroke="rgba(110,59,75,.25)" stroke-width="2" stroke-dasharray="2 6"/>
{g}
</svg>"""

def goddard_shema_svg(dark=True):
    """Два хода: просьба против состояния."""
    return """<svg viewBox="0 0 900 240" role="img" aria-label="Обычный ход и обратный ход Годдарда" style="width:100%;height:auto">
<g font-family="Manrope,sans-serif">
<text x="30" y="34" font-size="13" font-weight="800" fill="rgba(242,237,228,.55)" letter-spacing="2">ПРИВЫЧНЫЙ ХОД</text>
<g fill="#22303C" stroke="rgba(242,237,228,.2)">
<rect x="30" y="50" width="230" height="46" rx="6"/><rect x="335" y="50" width="230" height="46" rx="6"/><rect x="640" y="50" width="230" height="46" rx="6"/>
</g>
<g fill="rgba(242,237,228,.75)" font-size="13.5" text-anchor="middle">
<text x="145" y="78">хочу и прошу</text><text x="450" y="78">жду и сомневаюсь</text><text x="755" y="78">всё как вчера</text>
</g>
<path d="M265 73h60M570 73h60" stroke="rgba(242,237,228,.35)" stroke-width="2"/>
<path d="M322 73l-8-5v10zM627 73l-8-5v10z" fill="rgba(242,237,228,.35)"/>
<text x="30" y="152" font-size="13" font-weight="800" fill="#D08A5F" letter-spacing="2">ХОД ГОДДАРДА</text>
<g fill="#6E3B4B">
<rect x="30" y="168" width="230" height="46" rx="6"/><rect x="335" y="168" width="230" height="46" rx="6"/><rect x="640" y="168" width="230" height="46" rx="6"/>
</g>
<g fill="#FAF5F0" font-size="13.5" font-weight="700" text-anchor="middle">
<text x="145" y="196">живу состоянием итога</text><text x="450" y="196">решаю и делаю иначе</text><text x="755" y="196">события меняются</text>
</g>
<path d="M265 191h60M570 191h60" stroke="#D08A5F" stroke-width="2.4"/>
<path d="M322 191l-9-5.5v11zM627 191l-9-5.5v11z" fill="#D08A5F"/>
</g>
</svg>"""

def mayatnik_svg():
    """Зеланд: маятник, который кормится реакцией."""
    return """<svg viewBox="0 0 900 250" role="img" aria-label="Маятник: реакция раскачивает, спокойствие гасит" style="width:100%;height:auto">
<g font-family="Manrope,sans-serif">
<path d="M450 30 L250 178" stroke="#6E3B4B" stroke-width="3"/>
<circle cx="244" cy="184" r="24" fill="#6E3B4B"/>
<circle cx="450" cy="30" r="6" fill="#322D2B"/>
<path d="M180 120 a300 300 0 0 1 60 -52" fill="none" stroke="rgba(110,59,75,.5)" stroke-width="2" stroke-dasharray="3 6"/>
<path d="M660 68 a300 300 0 0 1 60 52" fill="none" stroke="rgba(110,59,75,.5)" stroke-width="2" stroke-dasharray="3 6"/>
<path d="M450 30 L656 178" stroke="rgba(110,59,75,.28)" stroke-width="2" stroke-dasharray="4 6"/>
<circle cx="662" cy="184" r="24" fill="none" stroke="rgba(110,59,75,.35)" stroke-width="2" stroke-dasharray="3 5"/>
<text x="160" y="228" font-size="13" font-weight="800" fill="#6E3B4B">ДЁРНУЛСЯ: КАЧНУЛ СИЛЬНЕЕ</text>
<text x="586" y="228" font-size="13" font-weight="800" fill="#7D8C74">НЕ СРЕАГИРОВАЛ: ЗАТУХАЕТ</text>
<text x="450" y="120" text-anchor="middle" font-family="Lora,Georgia,serif" font-style="italic" font-size="14" fill="#655C55">скандал, новости, чужая паника</text>
</g>
</svg>"""

def istoki_dalee(*items):
    """Перелинковка внизу страницы истоков: соседние страницы раздела."""
    links = "".join(f'<a href="{u}">{t}</a>' for u, t in items)
    return f"""<section style="padding-top:0"><div class="narrow">
<p class="eyebrow">Другие истоки метода</p>
<div class="chiplist">{links}<a href="/chizhovy2/istoki/">Все истоки</a></div>
</div></section>"""

MOST = """<section><div class="narrow">
<h2>Читать полезно, а&nbsp;меняет жизнь работа в&nbsp;зале</h2>
<p class="sub">Книги дают карту, а&nbsp;сценарий переписывается в&nbsp;зале, телом и&nbsp;эмоцией. Начни с&nbsp;бесплатного гайда или приходи на&nbsp;собеседование: час разговора о&nbsp;твоей&nbsp;ситуации.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>"""

MOST = """<section style="padding-top:0"><div class="narrow">
<h2>Читать полезно, а&nbsp;меняет жизнь работа в&nbsp;зале</h2>
<p class="sub" style="margin:0 0 26px">Книги дают карту, а&nbsp;сценарий переписывается в&nbsp;зале, телом и&nbsp;эмоцией. Начни с&nbsp;бесплатного гайда или приходи на&nbsp;собеседование: час разговора о&nbsp;твоей&nbsp;ситуации.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>"""

P["istoki/index.html"] = ("Истоки метода · Настоящие отношения",
"Психодрама Морено, трансерфинг Зеланда, est, Годдард и наука: из чего собран метод школы и что мы переработали за 16 лет.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки метода</p><h1>Из чего собран метод</h1>
<p class="lead">Любая сильная школа выросла из&nbsp;чужих идей. Мы&nbsp;называем свои опоры открыто: вот авторы, у&nbsp;которых мы&nbsp;взяли лучшее, и&nbsp;вот что мы&nbsp;с&nbsp;этим сделали за&nbsp;16&nbsp;лет живой практики.</p></div></div>

<section><div class="narrow">
<h2>Почему мы&nbsp;это показываем</h2>
<p>На&nbsp;рынке принято прятать истоки: метод подаётся как озарение основателя, а&nbsp;источники остаются за&nbsp;кадром. Нам такой театр не&nbsp;нужен. Взрослый человек имеет право знать, на&nbsp;что опирается, и&nbsp;проверить каждый корень нашей&nbsp;работы.</p>
<p>К&nbsp;тому&nbsp;же честность про истоки сама по&nbsp;себе часть метода. Путь ученика начинается с&nbsp;точки&nbsp;А: признать, где ты&nbsp;на&nbsp;самом деле. Мы&nbsp;делаем то&nbsp;же самое: показываем, откуда выросли.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Пять опор</p>
<h2>Карта истоков</h2>
<div class="grid3" style="margin-top:28px">
<div class="card"><span class="bignum">01</span>{icon('people')}<h3>Якоб Морено: психодрама</h3><p>Живая сцена вместо разговоров о&nbsp;жизни. Академическое ядро метода: обмен ролями, дублирование, работа группой. Психодраме сто лет, и&nbsp;она до&nbsp;сих пор глубже большинства&nbsp;новинок.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/moreno-psihodrama/">Разобрать</a></p></div>
<div class="card"><span class="bignum">02</span>{icon('loop','var(--sage-deep)')}<h3>Вадим Зеланд: трансерфинг</h3><p>Маятники, важность, намерение, зеркало мира. Язык, на&nbsp;котором ученики школы описывают свою ежедневную практику.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/zeland-transerfing/">Разобрать</a></p></div>
<div class="card"><span class="bignum">03</span>{icon('flame','var(--sand)')}<h3>est: тренинги погружения</h3><p>Сан-Франциско, 1971&nbsp;год, Вернер Эрхард. Два уикенда, которые делили жизнь надвое. Корень жанра, в&nbsp;котором работает наша группа.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/est-transformaciya/">Разобрать</a></p></div>
<div class="card"><span class="bignum">04</span>{icon('sunrise')}<h3>Невилл Годдард: состояние</h3><p>«Реальность откликается на&nbsp;состояние». Основа практики намерения, которую ученики ведут девяносто дней Марафона.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/goddard/">Разобрать</a></p></div>
<div class="card"><span class="bignum">05</span>{icon('lamp','var(--sage-deep)')}<h3>Наука: почему это работает</h3><p>ЛеДу, Гоулман, Болте Тейлор, Голвитцер, Либерман. Каждый термин истоков стоит у&nbsp;нас на&nbsp;научной&nbsp;подпорке.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/nauka/">Разобрать</a></p></div>
<div class="card linen"><span class="bignum">06</span>{icon('lens')}<h3>Сплав: наш метод</h3><p>Сцена Морено, язык Зеланда, формат погружения, практика состояния и&nbsp;наука в&nbsp;одном процессе, проверенном 16&nbsp;годами групп.</p><p style="margin-top:12px"><a href="/chizhovy2/metod/">Как устроен метод</a></p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Одной схемой</p>
<h2>Пять источников, один метод</h2>
<div class="only-d" style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:30px 22px 18px;margin-top:26px">{splav_svg()}</div>
<div class="only-m" style="margin-top:22px">
<div class="chiplist" style="text-align:center"><span>Морено · сцена</span><span>Зеланд · язык</span><span>est · формат</span><span>Годдард · состояние</span><span>Наука · проверка</span></div>
<div style="text-align:center;color:var(--sand);font-size:1.4rem;line-height:1;margin:4px 0 10px">↓</div>
<div class="card white" style="text-align:center"><h3 style="margin-bottom:4px">Метод школы</h3><p>16 лет зала, сотни историй</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Как мы работаем с истоками</h2>
<ol class="steps" style="margin-top:18px;margin-left:22px">
<li style="margin-bottom:12px"><b>Берём рабочее.</b> Из&nbsp;каждой школы мы&nbsp;взяли то, что раз за&nbsp;разом даёт результат в&nbsp;зале, и&nbsp;оставили за&nbsp;бортом всё, что красиво звучит и&nbsp;ничего не&nbsp;меняет.</li>
<li style="margin-bottom:12px"><b>Перерабатываем.</b> На&nbsp;каждой странице истоков честный разбор: что автор говорил, что мы&nbsp;взяли и&nbsp;что переработали под живую групповую работу.</li>
<li><b>Проверяем практикой.</b> Единственный судья: изменения в&nbsp;жизни учеников. Всё, что осталось в&nbsp;методе, прошло через сотни историй.</li>
</ol>
</div></section>
{MOST}
""")

P["istoki/moreno-psihodrama/index.html"] = ("Якоб Морено и психодрама · Истоки метода",
"Психодрама: живая сцена, обмен ролями, пустой стул. Что школа взяла у Морено и что переработала.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/metod-scena.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Психодрама</p><h1 style="font-size:clamp(1.75rem,6vw,3.7rem)">Сцена, на&nbsp;которой переигрывают жизнь</h1>
<p class="lead">Якоб Леви Морено, венский психиатр, ещё в&nbsp;1921&nbsp;году заметил: человек меняется на&nbsp;сцене быстрее, чем в&nbsp;кресле напротив врача. Так родилась психодрама, академическое ядро нашего&nbsp;метода.</p></div></div>

<section><div class="narrow">
<h2>Что придумал Морено</h2>
<p>Морено (1889-1974) начинал с&nbsp;«театра спонтанности» в&nbsp;Вене: обычные люди разыгрывали на&nbsp;сцене не&nbsp;пьесы, а&nbsp;собственные истории. И&nbsp;он&nbsp;заметил странное. В&nbsp;такой игре человек вдруг выходит из&nbsp;заученной роли и&nbsp;находит новый ответ на&nbsp;старую ситуацию. Позже, уже в&nbsp;Америке, наблюдение превратилось в&nbsp;метод, которым сегодня работают в&nbsp;десятках&nbsp;стран.</p>
<p>Главная ставка простая. О&nbsp;проблеме бесполезно рассказывать, в&nbsp;неё нужно вернуться. Участники группы становятся героями твоей истории, пространство зала превращается в&nbsp;ту&nbsp;кухню или тот кабинет, и&nbsp;сцена&nbsp;оживает.</p>
</div>
<div class="wrap"><div class="grid3" style="margin-top:26px">
<div class="card"><h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место отца, партнёра, начальника. Отвечаешь себе его словами. Пять минут в&nbsp;чужой роли дают больше, чем год&nbsp;объяснений.</p></div>
<div class="card"><h3>Дублирование</h3><p>Человек рядом договаривает то, что ты&nbsp;чувствуешь и&nbsp;не&nbsp;решаешься сказать. Невысказанное впервые звучит&nbsp;вслух.</p></div>
<div class="card"><h3>Зеркало</h3><p>Свою сцену играют другие, а&nbsp;ты&nbsp;смотришь со&nbsp;стороны, как зритель в&nbsp;зале. Иногда одного этого хватает, чтобы увидеть сценарий&nbsp;целиком.</p></div>
</div></div>
<div class="narrow">
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:26px">
<div class="nail"><b>1921</b><span>«театр спонтанности» в&nbsp;Вене: первая сцена&nbsp;метода</span></div>
<div class="nail"><b>100&nbsp;лет</b><span>психодраме: живой метод, а&nbsp;не&nbsp;модная&nbsp;новинка</span></div>
<div class="nail"><b>Десятки</b><span>стран, где психодрамой работают&nbsp;сегодня</span></div>
</div></div>
<div class="narrow">
<div class="pull"><div class="q">«Покажи мне, а&nbsp;не&nbsp;рассказывай». Этой фразой Морено развернул психологию своего времени.</div><div class="who">Принцип психодрамы</div></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что мы&nbsp;взяли и&nbsp;что переработали</h2>
<p><b style="color:#D08A5F">Взяли:</b> сцену как главный инструмент, группу как усилитель, пустой стул, обмен ролями. Разговор, который не&nbsp;случился в&nbsp;жизни, происходит у&nbsp;нас в&nbsp;зале. Тело проживает его&nbsp;по-настоящему.</p>
<p><b style="color:#D08A5F">Переработали:</b> у&nbsp;Морено спонтанность сама по&nbsp;себе считалась лекарством. Мы&nbsp;поставили сцену на&nbsp;карту событийного круга: она ведёт к&nbsp;конкретной точке, к&nbsp;старому решению, и&nbsp;там происходит перезапись. Сцена у&nbsp;нас средство. Цель это новый сценарий в&nbsp;жизни.</p>
<p>Поэтому после сцены работа не&nbsp;заканчивается. Решение закрепляется практикой между модулями и&nbsp;тремя месяцами&nbsp;Марафона.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/zeland-transerfing/", "Зеланд и трансерфинг"), ("/chizhovy2/istoki/nauka/", "Наука за методом"), ("/chizhovy2/metod/", "Метод целиком"))}
{MOST}
""")

P["istoki/zeland-transerfing/index.html"] = ("Вадим Зеланд и трансерфинг · Истоки метода",
"Маятники, важность, намерение, зеркало мира: как язык трансерфинга работает в школе и что мы объясняем через мозг.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-zeland.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Трансерфинг</p><h1>Маятники, важность, зеркало мира</h1>
<p class="lead">С&nbsp;2004 года книги Вадима Зеланда «Трансерфинг реальности» разошлись миллионными тиражами. Для наших учеников это язык ежедневной практики: точный, образный и&nbsp;удобный в&nbsp;работе.</p></div></div>

<section><div class="narrow">
<h2>Три идеи, которые мы&nbsp;используем</h2>
<div class="card white" style="margin:20px 0 12px">{icon('pendulum')}<h3>Маятники</h3><p>Структуры, которые кормятся твоей реакцией: скандал, лента новостей, чужая паника, офисная война. Дёрнулся, значит отдал энергию. У&nbsp;Зеланда это образ; в&nbsp;зале он&nbsp;становится навыком: заметить крючок и&nbsp;не&nbsp;схватиться.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('ceiling','var(--sage-deep)')}<h3>Важность</h3><p>Чем сильнее вцепился в&nbsp;результат, тем хуже он&nbsp;даётся: раздутая ставка парализует. Снятая важность возвращает лёгкость и&nbsp;точность. Знакомо по&nbsp;переговорам, по&nbsp;свиданиям, по&nbsp;любому «очень&nbsp;надо».</p></div>
<div class="card white">{icon('mirror','var(--sand)')}<h3>Зеркало мира</h3><p>Мир читает состояние. Слова для него шум. Пока внутри страх, снаружи собираются поводы бояться. Ученики после тренинга говорят коротко: мир&nbsp;зеркалит.</p></div>

<div style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:26px 18px 10px;margin-top:26px">{mayatnik_svg()}</div>
<div class="pull"><div class="q">«Отследил сегодня несколько маятников, не&nbsp;среагировал, и&nbsp;получилось удержать состояние весь день.»</div><div class="who">Из отчёта ученика на&nbsp;Марафоне</div></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что мы&nbsp;взяли и&nbsp;что переработали</h2>
<p><b style="color:#D08A5F">Взяли:</b> рабочий язык (он&nbsp;теперь живёт в&nbsp;нашем <a href="/chizhovy2/slovar/" style="color:#D08A5F">словаре школы</a>). На&nbsp;Марафоне трансерфинг входит в&nbsp;список чтения, а&nbsp;его термины живут в&nbsp;ежедневной практике: утром намерение, вечером разбор, где катался на&nbsp;маятниках и&nbsp;где удержал состояние.</p>
<p><b style="color:#D08A5F">Переработали:</b> у&nbsp;Зеланда это философия для самостоятельного чтения, и&nbsp;у&nbsp;неё есть слабое место: прочитал, восхитился, через месяц забыл. Мы&nbsp;дали каждому термину механизм и&nbsp;тренировку. Маятник у&nbsp;нас это твоя знакомая петля реакции, и&nbsp;её видно на&nbsp;событийном круге. Важность это ставка, которая включает страх и&nbsp;сжимает выбор. Чтение даёт понимание. Держать состояние учат девяносто дней практики с&nbsp;командой и&nbsp;разборами.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/goddard/", "Невилл Годдард"), ("/chizhovy2/istoki/est-transformaciya/", "est и «Трансформация»"), ("/chizhovy2/istoki/nauka/", "Наука за методом"))}
{MOST}
""")

P["istoki/est-transformaciya/index.html"] = ("est и «Трансформация» Рейнхарта · Истоки метода",
"Тренинг est Вернера Эрхарда и книга «Трансформация» Люка Рейнхарта: откуда пошёл жанр погружения и что школа сделала иначе.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-est.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · est</p><h1>Тренинг, с которого начался жанр</h1>
<p class="lead">Сан-Франциско, 1971&nbsp;год. Вернер Эрхард проводит первый тренинг est: два выходных подряд, жёсткие правила зала и&nbsp;сотни тысяч выпускников за&nbsp;тринадцать лет. Так родился жанр тренингов погружения, в&nbsp;котором работает и&nbsp;наша школа.</p></div></div>

<section><div class="narrow">
<h2>Что происходило в&nbsp;зале est</h2>
<p>Люди сидели в&nbsp;зале по&nbsp;шестнадцать часов, сдавали часы на&nbsp;входе и&nbsp;держали слово не&nbsp;вставать до&nbsp;перерыва. Ведущий разбирал их&nbsp;истории при всех, без анестезии. Звучит жёстко, так и&nbsp;было. Но&nbsp;у&nbsp;формата оказалась настоящая сила: за&nbsp;два уикенда защита психики, которую час терапии даже не&nbsp;царапает, снималась, и&nbsp;человек впервые видел свою жизнь без привычных оправданий.</p>
<p>В&nbsp;России est знают по&nbsp;книге «Трансформация» Люка Рейнхарта, автора знаменитого «Дайсмена»: он&nbsp;описал тренинг изнутри, день за&nbsp;днём, с&nbsp;репликами зала. Прочитать её&nbsp;стоит хотя&nbsp;бы ради того, чтобы почувствовать, как устроено погружение.</p>
</div>
<div class="wrap"><div class="timeline" style="margin-top:26px">{est_lenta_svg()}</div>
<div class="timeline-m" style="margin-top:26px">
<div class="tm"><div class="c" style="font-size:.82rem">1971</div><div><b>Первый est</b><span>Сан-Франциско, Вернер Эрхард</span></div></div>
<div class="gap">жанр набирает силу</div>
<div class="tm"><div class="c" style="font-size:.82rem">1976</div><div><b>«Книга est»</b><span>Рейнхарт описывает тренинг изнутри</span></div></div>
<div class="gap">13 лет: сотни тысяч выпускников</div>
<div class="tm last"><div class="c" style="font-size:.7rem">сейчас</div><div><b>Камерные школы глубины</b><span>жанр повзрослел, масштаб сменился на&nbsp;глубину</span></div></div>
</div></div>
<div class="wrap"><div class="grid3" style="margin-top:26px">
<div class="card"><h3>Ответственность</h3><p>Ты&nbsp;источник своих&nbsp;результатов. Обстоятельства реальны, но&nbsp;автор реакции на&nbsp;них всегда ты. С&nbsp;этой точки начинается взрослая работа над жизнью.</p></div>
<div class="card"><h3>Понять и&nbsp;пережить</h3><p>est первым развёл эти вещи: понимание живёт в&nbsp;голове и&nbsp;ничего не&nbsp;сдвигает. Жизнь меняет только пережитый опыт. Вся индустрия погружений выросла из&nbsp;этого&nbsp;различия.</p></div>
<div class="card"><h3>Слово</h3><p>Личность строится из&nbsp;обещаний, которые ты&nbsp;держишь. Начал опаздывать на&nbsp;встречи с&nbsp;собой, значит сценарий уже водит тебя за&nbsp;руку.</p></div>
</div></div></section>

<section class="dark"><div class="narrow">
<h2>Что мы&nbsp;взяли и&nbsp;что переработали</h2>
<p><b style="color:#D08A5F">Взяли:</b> формат погружения на&nbsp;несколько дней, потому что психика открывается только в&nbsp;длинной работе. Правила зала как рамку безопасности. Честность без скидок: на&nbsp;собеседовании мы&nbsp;можем и&nbsp;отговорить, если школа не&nbsp;твой&nbsp;инструмент.</p>
<p><b style="color:#D08A5F">Переработали:</b> почти всё остальное. est работал залами по&nbsp;двести пятьдесят человек и&nbsp;провокацией; мы&nbsp;выбрали противоположный масштаб. Группы 10-20 участников, бережная глубина вместо давления, живая сцена взамен лекции и&nbsp;три месяца сопровождения после, чтобы результат не&nbsp;выветрился к&nbsp;понедельнику.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/moreno-psihodrama/", "Морено и психодрама"), ("/chizhovy2/istoki/zeland-transerfing/", "Зеланд и трансерфинг"), ("/chizhovy2/programma/", "Как устроены наши модули"))}
{MOST}
""")

P["istoki/goddard/index.html"] = ("Невилл Годдард · Истоки метода",
"Состояние, в котором уже получилось: идея Невилла Годдарда, практика намерения на Марафоне и её научный двойник.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-goddard.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Годдард</p><h1>Состояние, в котором уже получилось</h1>
<p class="lead">Невилл Годдард, лектор с&nbsp;Барбадоса, полвека собирал залы в&nbsp;Америке с&nbsp;одной мыслью: какое состояние, такие и&nbsp;события. Его идею наши ученики проверяют девяносто дней подряд.</p></div></div>

<section><div class="narrow">
<h2>Главная идея Годдарда</h2>
<div class="pull" style="margin-top:6px"><div class="q">«Все события уже существуют. Вы&nbsp;не&nbsp;создаёте их, вы&nbsp;входите в&nbsp;них, проживая состояние того, кем вы&nbsp;хотите&nbsp;быть.»</div><div class="who">Невилл Годдард (1905-1972)</div></div>
<p>Реальность откликается на&nbsp;состояние, а&nbsp;не&nbsp;на&nbsp;просьбу. Просить и&nbsp;ждать бесполезно, пока внутри ты&nbsp;остаёшься человеком, у&nbsp;которого «пока не&nbsp;получилось»: из&nbsp;такого состояния рождаются те&nbsp;же действия и&nbsp;те&nbsp;же события, что вчера. Годдард предлагал обратный ход: сначала прожить состояние человека, у&nbsp;которого уже есть, и&nbsp;дать ему вести решения.</p>
<p>Звучит смело. Но&nbsp;вспомни, как легко даётся день, когда ты&nbsp;с&nbsp;утра в&nbsp;силе, и&nbsp;как вязнет тот&nbsp;же список дел в&nbsp;день, когда внутри тяжесть. Состояние уже управляет твоими событиями. Вопрос только, кто держит руль.</p>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что мы&nbsp;взяли и&nbsp;что переработали</h2>
<p><b style="color:#D08A5F">Взяли:</b> ежедневную практику намерения на&nbsp;Марафоне. Утром формулируешь, из&nbsp;какого состояния идёшь в&nbsp;день и&nbsp;что создаёшь. Вечером записываешь открытия и&nbsp;благодарности. Девяносто дней подряд, с&nbsp;командой и&nbsp;разборами: этого хватает, чтобы новый способ жить стал привычкой.</p>
<p><b style="color:#D08A5F">Переработали:</b> рамку. У&nbsp;Годдарда мистика середины прошлого века, мы&nbsp;же показываем механизм: состояние управляет фильтрами внимания и&nbsp;качеством решений. Стоит ему сдвинуться, и&nbsp;человек замечает другие возможности, делает новые шаги, получает иные события. У&nbsp;практики намерения есть и&nbsp;научный двойник: психолог Питер Голвитцер показал, что конкретно сформулированное намерение в&nbsp;разы повышает шанс дойти до&nbsp;действия.</p>
</div>
<div class="wrap only-d" style="margin-top:30px">{goddard_shema_svg()}</div>
<div class="narrow only-m" style="margin-top:26px">
<p style="font-size:.72rem;font-weight:800;letter-spacing:.16em;color:rgba(242,237,228,.55);margin-bottom:8px">ПРИВЫЧНЫЙ ХОД</p>
<div class="card" style="margin-bottom:14px"><p style="margin:0">хочу и&nbsp;прошу → жду и&nbsp;сомневаюсь → всё как вчера</p></div>
<p style="font-size:.72rem;font-weight:800;letter-spacing:.16em;color:#D08A5F;margin-bottom:8px">ХОД ГОДДАРДА</p>
<div class="card" style="background:#6E3B4B;border-color:#6E3B4B"><p style="margin:0;color:#FAF5F0;font-weight:700">живу состоянием итога → решаю и&nbsp;делаю иначе → события&nbsp;меняются</p></div>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/zeland-transerfing/", "Зеланд и трансерфинг"), ("/chizhovy2/istoki/nauka/", "Наука за методом"), ("/chizhovy2/marafon/", "Марафон: 90 дней практики"))}
{MOST}
""")

P["istoki/nauka/index.html"] = ("Наука за методом · Истоки метода",
"ЛеДу, Гоулман, Болте Тейлор, Голвитцер, Либерман: открытия, на которых стоит работа школы.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-nauka.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Наука</p><h1>Почему это работает</h1>
<p class="lead">Сцена, состояние, погружение: за&nbsp;каждым инструментом школы стоит исследование. Ниже пять открытий и&nbsp;то, как&nbsp;мы используем каждое в&nbsp;зале.</p></div></div>

<section><div class="wrap"><div class="nails nails3" style="margin-bottom:26px">
<div class="nail"><b>12&nbsp;мс</b><span>фора эмоционального мозга перед&nbsp;думающим</span></div>
<div class="nail"><b>90&nbsp;сек</b><span>живёт химия эмоции, если&nbsp;её&nbsp;не&nbsp;кормить</span></div>
<div class="nail"><b>100&nbsp;лет</b><span>групповой сцене&nbsp;Морено</span></div>
</div></div>
<div class="narrow">
<div class="card white" style="margin-bottom:12px"><span class="bignum">12&nbsp;мс</span><h3>Джозеф ЛеДу: эмоция быстрее мысли</h3><p>Сигнал об&nbsp;угрозе доходит до&nbsp;эмоционального центра мозга за&nbsp;12&nbsp;миллисекунд. Думающая кора получает его позже. Поэтому обещание «в&nbsp;следующий раз отвечу спокойно» рассыпается: реакция стартует раньше решения. В&nbsp;зале мы&nbsp;работаем с&nbsp;самой записью, она быстрее любой силы&nbsp;воли.</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Дэниел Гоулман: эмоции берут верх</h3><p>В&nbsp;острый момент миндалина перехватывает управление, и&nbsp;умный взрослый человек ведёт себя как не&nbsp;свой. Гоулман назвал это захватом. На&nbsp;тренинге ты&nbsp;учишься видеть его в&nbsp;лицо и&nbsp;выходить из&nbsp;него через тело: пока миндалина рулит, уговоры&nbsp;бессильны.</p></div>
<div class="card white" style="margin-bottom:12px"><span class="bignum">90&nbsp;с</span><h3>Джилл Болте Тейлор: девяносто секунд</h3><p>Химия эмоции живёт в&nbsp;теле около полутора минут. Всё, что дольше, поддерживает уже мысль, которая крутит эмоцию по&nbsp;кругу. Пауза и&nbsp;внимание к&nbsp;телу разжимают этот круг. Тренируем это с&nbsp;первого&nbsp;дня.</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Питер Голвитцер: сила намерения</h3><p>Точное намерение поднимает шанс действия в&nbsp;разы по&nbsp;сравнению с&nbsp;расплывчатым «надо&nbsp;бы»: голове нужны место, время и&nbsp;первый шаг. Иначе не&nbsp;работает. Наша утренняя практика на&nbsp;Марафоне стоит на&nbsp;этом&nbsp;открытии.</p></div>
<div class="card white"><h3>Мэттью Либерман: назови чувство, и&nbsp;оно слабеет</h3><p>Названная вслух эмоция теряет силу: слова снижают активность миндалины. На&nbsp;этом держится половина работы группы. Чувство впервые получает имя и&nbsp;звучит при&nbsp;людях.</p></div>

<p style="margin-top:26px">И&nbsp;над всем этим сто лет психодрамы Морено: групповой формат, где все эти механизмы включаются разом, в&nbsp;одной живой сцене. Наука здесь рамка честности. Мы&nbsp;берём проверенное и&nbsp;не&nbsp;обещаем&nbsp;чудес.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/moreno-psihodrama/", "Морено и психодрама"), ("/chizhovy2/istoki/goddard/", "Невилл Годдард"), ("/chizhovy2/metod/", "Метод целиком"))}
{MOST}
""")

# ================= ИСТОРИИ УЧЕНИКОВ =================
P["istorii/index.html"] = ("Истории учеников · Настоящие отношения",
"Полные истории выпускников школы: точка А, работа, что изменилось. С согласия авторов, без глянца.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istorii-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истории учеников</p><h1>Что здесь происходит с людьми</h1>
<p class="lead">Люди приходят сюда с&nbsp;разным грузом. Ниже их&nbsp;истории как&nbsp;есть: точка А, сопротивление и&nbsp;то, что изменилось. Публикуем с&nbsp;разрешения самих учеников. Результат у&nbsp;каждого свой.</p></div></div>

<section><div class="wrap">
<!-- ПРОТОТИП: полные версии историй согласованы с авторами до публикации -->
<div class="grid2">
<div class="card white"><span class="chip" style="background:rgba(110,59,75,.08);color:var(--wine)">Личный путь</span>
<h3>Предприниматель: заново после дна</h3>
<p>Кассовый разрыв, сорвавшаяся свадьба, друзья отвернулись. На&nbsp;тренинг он&nbsp;пришёл в&nbsp;свой день рождения. Что было дальше, почему труднее всего далась точка&nbsp;А и&nbsp;как жизнь собралась&nbsp;обратно.</p>
<p style="margin-top:14px"><a href="/chizhovy2/istorii/predprinimatel/">Читать его историю</a></p></div>
<div class="card white"><span class="chip" style="background:rgba(92,107,84,.12);color:var(--sage-deep)">Опыт команды</span>
<h3>Девяносто дней команды «МИР»</h3>
<p>Пятнадцать человек, три месяца Марафона: практика утром и&nbsp;вечером, живой чат. Всё словами самих участников.</p>
<p style="margin-top:14px"><a href="/chizhovy2/istorii/komanda-mir/">Как прошли 90&nbsp;дней</a></p></div>
</div>
<p class="note" style="margin-top:18px">Раздел пополняется. Ещё несколько историй сейчас на&nbsp;согласовании у&nbsp;авторов.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Короткой строкой</p>
<h2>Что рассказывают ученики</h2>
<div class="grid3" style="margin-top:26px">
<div class="card"><p class="serif" style="font-style:italic">«Намерение это когда я&nbsp;знаю, что в&nbsp;моей жизни возможно только так. Тогда и&nbsp;важности нет, я&nbsp;просто&nbsp;знаю».</p><p class="note" style="margin-top:10px">Участница Марафона</p></div>
<div class="card"><p class="serif" style="font-style:italic">«Когда убираю фокус с&nbsp;себя и&nbsp;вовлечён в&nbsp;команду, энергия кратно растёт, и&nbsp;люди поворачиваются ко&nbsp;мне&nbsp;лицом».</p><p class="note" style="margin-top:10px">Участник Марафона</p></div>
<div class="card"><p class="serif" style="font-style:italic">«Когда цель и&nbsp;мечта действительно мои, всё происходит легко, порой на&nbsp;грани фантастики».</p><p class="note" style="margin-top:10px">Участница Марафона</p></div>
</div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/otzyvy/">Ещё отзывы о&nbsp;школе</a></p>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Что общего у&nbsp;этих историй</h2>
<p>Люди приходят из&nbsp;разных точек: один после потери бизнеса, другая из&nbsp;тихого благополучия, где всё есть и&nbsp;ничего не&nbsp;радует. Сюжеты разные, а&nbsp;узор один и&nbsp;тот&nbsp;же.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('target')}<h3>Сначала точка&nbsp;А</h3><p>Всё начинается с&nbsp;честного признания, где человек находится на&nbsp;самом деле, без смягчений и&nbsp;объяснений, почему так вышло. Шаг самый трудный, и&nbsp;почти все называют его&nbsp;переломным.</p></div>
<div class="card">{icon('shield','var(--sage-deep)')}<h3>Потом сопротивление</h3><p>«Долго упирался», «не&nbsp;верил», «сидел и&nbsp;злился». Психика защищает привычный порядок, даже когда он&nbsp;давно разрушает жизнь: старое хотя&nbsp;бы знакомо, а&nbsp;новое пугает сильнее любой боли. Упирался почти&nbsp;каждый.</p></div>
<div class="card">{icon('lens','var(--sand)')}<h3>Дальше узнавание</h3><p>Момент, когда человек видит свою запись целиком. В&nbsp;группе это называют «нолик провалился», и&nbsp;это радость, а&nbsp;не&nbsp;поражение.</p></div>
<div class="card">{icon('sunrise')}<h3>И только потом результаты</h3><p>Деньги, отношения, здоровье подтягиваются позже, как следствие другого состояния и&nbsp;других поступков. Ни&nbsp;одна история не&nbsp;начинается с&nbsp;них.</p></div>
</div>
<p class="note" style="margin-top:20px">Слова, которые здесь звучат, разобраны в&nbsp;<a href="/chizhovy2/slovar/">словаре школы</a>.</p>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Начать свою историю</h2>
<p class="sub" style="margin:0 0 26px">Первый шаг у&nbsp;всех один: час честного разговора. Для читателей сайта он&nbsp;&#8288;бесплатный.</p>
<a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a>
</div></section>
""")

P["istorii/predprinimatel/index.html"] = ("Предприниматель: заново после дна · Истории учеников",
"Полная история ученика школы: кризис, сопротивление, точка А и как жизнь собралась обратно.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoriya-biznes.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">История ученика</p><h1>Заново после дна</h1>
<p class="lead">Предприниматель, пришёл весной 2024. Дальше его слова, почти без правок и&nbsp;с его согласия. Имя он&nbsp;просил не раскрывать, а&nbsp;неудобные места мы&nbsp;не убирали. Результат у&nbsp;каждого свой.</p></div></div>

<section><div class="narrow">
<!-- ПРОТОТИП: текст согласован с автором до публикации -->
<h2>Точка&nbsp;А</h2>
<p>«Я&nbsp;находился в&nbsp;фазе, которую называют дном. Кассовый разрыв на&nbsp;десятки миллионов, долги, заработки в&nbsp;один день стали ноль, накопления потрачены. Расстался с&nbsp;девушкой, которой сделал предложение: свадьбу пришлось отложить из-за денег, а&nbsp;она не&nbsp;захотела&nbsp;ждать.</p>
<p>Самое тяжёлое: сильно било по&nbsp;эго. Друзья отвернулись, из&nbsp;делового клуба выгнали, тянулся хвост репутации. Не&nbsp;хотелось ни&nbsp;с&nbsp;кем общаться, хотелось закрыться в&nbsp;коробочку и&nbsp;сидеть одному. Крах я&nbsp;понимал, а&nbsp;вот как начать снова и&nbsp;где найти силы, понять не&nbsp;мог. Убегал как умел: закрывался, алкоголь, спорт, суета, пытался казаться хорошим».</p>

<h2 style="margin-top:34px">Как он&nbsp;пришёл</h2>
<p>«Подруга давно рассказывала о&nbsp;тренинге, но&nbsp;тогда мне было не&nbsp;надо. А&nbsp;тут друг увидел моё состояние и&nbsp;сказал: я&nbsp;знаю решение. Когда я&nbsp;понял, что он&nbsp;говорит про то&nbsp;же самое место, я&nbsp;решил: это вторая возможность. Пошёл не&nbsp;раздумывая, прямо в&nbsp;свой день рождения. Подарил себе тренинг. Единственное, что останавливало: простое недоверие, что поможет».</p>

<h2 style="margin-top:34px">Что происходило</h2>
<p>«Долго сопротивлялся, как баран. Проваливался в&nbsp;своё. Труднее всего было принять точку&nbsp;А: признать, где я&nbsp;на&nbsp;самом деле. Потребовалось время, чтобы увидеть, в&nbsp;чём я&nbsp;жил.</p>
<p>Главное, что я&nbsp;увидел: мир это зеркало. Всё, что со&nbsp;мной происходит, это то, что я&nbsp;сам транслирую. Я&nbsp;покупал отношения вместо того, чтобы их&nbsp;строить, использовал людей ради выгоды. Когда защита наконец упала, в&nbsp;группе это называют «нолик провалился», я&nbsp;впервые обрадовался правде о&nbsp;себе».</p>
<div class="pull"><div class="q">«Ура, нолик <span style="white-space:nowrap">наконец-то провалился.»</span></div><div class="who">Из его сообщения группе в&nbsp;тот вечер</div></div>

<h2 style="margin-top:34px">Что изменилось</h2>
<p>«Сейчас я&nbsp;строю настоящие отношения везде: в&nbsp;деле, с&nbsp;близкими, с&nbsp;собой. Деньги начали приходить, энергии много, и&nbsp;я&nbsp;умею ей&nbsp;распоряжаться: держу состояние через спорт и&nbsp;благодарности, не&nbsp;сливаю её&nbsp;по&nbsp;мелочам. Раньше отсеивал людей по&nbsp;уровню жизни, сейчас просто строю отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами. Цели кратно увеличились, научился играть в&nbsp;долгую. И&nbsp;мне стало всё равно на&nbsp;чужое мнение обо мне.</p>
<p>Одной фразой: получил новую версию&nbsp;себя».</p>
<div class="pull"><div class="q">«Появилось ощущение, что вижу себя на&nbsp;всей шахматной доске, а&nbsp;не&nbsp;в&nbsp;одной клетке.»</div><div class="who">Его формула итога</div></div>
<p class="note">История личная, поэтому без имени. Суммы и&nbsp;скорость перемен у&nbsp;каждого свои: школа не&nbsp;обещает повторения чужого результата и&nbsp;не&nbsp;берётся предсказывать&nbsp;сроки.</p>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Узнал себя в этом?</h2>
<p class="sub" style="margin:0 0 26px">Его путь начался с&nbsp;одного честного разговора о&nbsp;том, где он&nbsp;на&nbsp;самом деле находится. Твой может начаться так&nbsp;же. Собеседование для читателей сайта&nbsp;бесплатное.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/istorii/komanda-mir/" style="margin-left:8px">Ещё история: команда «МИР»</a></p>
</div></section>
""")

P["istorii/komanda-mir/index.html"] = ("Девяносто дней команды «МИР» · Истории учеников",
"Как выглядит Марафон изнутри: утренние намерения, вечерние благодарности и команда, голосами участников.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-10.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Марафон изнутри</p><h1>Девяносто дней команды «МИР»</h1>
<p class="lead">Осень 2022&nbsp;года, пятнадцать человек, третий модуль «Создатель реальности». Три месяца: раз в&nbsp;неделю разбор с&nbsp;Алексеем и&nbsp;Ириной, между ними ежедневная практика. Ниже их&nbsp;история, собранная из&nbsp;живого командного&nbsp;чата.</p></div></div>

<section><div class="wrap">
<!-- ПРОТОТИП: цитаты из закрытого чата, согласие авторов получено до публикации -->
<div class="nails nails3" style="margin-bottom:26px">
<div class="nail"><b>15</b><span>человек в&nbsp;команде&nbsp;«МИР»</span></div>
<div class="nail"><b>90</b><span>дней ежедневной&nbsp;практики</span></div>
<div class="nail"><b>Раз в&nbsp;неделю</b><span>встреча-разбор с&nbsp;ведущими, все три&nbsp;месяца</span></div>
</div></div>
<div class="narrow">
<h2>Как устроен их&nbsp;день</h2>
<p>Утром каждый пишет в&nbsp;чат намерение на&nbsp;день: из&nbsp;какого состояния идёт и&nbsp;что создаёт. Вечером открытия и&nbsp;благодарности: что произошло, где старая запись взяла своё, за&nbsp;что спасибо дню и&nbsp;людям. Раз в&nbsp;неделю вся команда встречается с&nbsp;ведущими на&nbsp;разбор.</p>
<p>Простая механика, но&nbsp;девяносто дней подряд она перепрошивает привычный способ жить. Вот как это звучало у&nbsp;них, без правок:</p>
<div class="card white" style="margin:20px 0 12px"><p class="serif" style="font-style:italic;margin:0">«Пишу утром намерение, вечером сравниваю. Так приятно ощущать, что к&nbsp;концу дня большая часть намерений&nbsp;сбылась».</p></div>
<div class="card white" style="margin-bottom:12px"><p class="serif" style="font-style:italic;margin:0">«Отследил сегодня несколько маятников, не&nbsp;среагировал, и&nbsp;благодаря этому удержал состояние весь день».</p></div>
<div class="card white"><p class="serif" style="font-style:italic;margin:0">«Вместо эмоций решила стать вкладом в&nbsp;отношения: говорить с&nbsp;уважением и&nbsp;любовью. И&nbsp;вот первые ростки. Сердце открывается, и&nbsp;я&nbsp;в&nbsp;этот момент&nbsp;настоящая».</p></div>

<h2 style="margin-top:34px">Что происходило с&nbsp;людьми</h2>
<p>У&nbsp;каждого своя история внутри общей. Одна участница полгода не&nbsp;могла решиться на&nbsp;поездку, даже паспорт не&nbsp;находился: после работы в&nbsp;группе приняла решение внутри, и&nbsp;всё сложилось за&nbsp;день, паспорт нашёлся, тур куплен. Другой заметил: стоит убрать фокус с&nbsp;себя и&nbsp;вложиться в&nbsp;команду, энергия кратно растёт, и&nbsp;люди поворачиваются&nbsp;лицом.</p>
<div class="pull"><div class="q">«Намерение это когда я&nbsp;знаю, что в&nbsp;моей жизни возможно только так. В&nbsp;чём я&nbsp;так была уверена по&nbsp;жизни, всё&nbsp;сбылось.»</div><div class="who">Участница команды «МИР»</div></div>
<p>К&nbsp;финалу модуля в&nbsp;чате появились слова, ради которых школа и&nbsp;работает: «жизнь становится легче и&nbsp;лучше, пусть пока в&nbsp;мелочах, но&nbsp;я&nbsp;это вижу». Перемены приходят малым и&nbsp;остаются, потому что их&nbsp;держат девяносто дней&nbsp;практики.</p>
<p class="note">Цитаты из&nbsp;закрытого командного чата, публикуются с&nbsp;согласия участников. Имена убраны. Результат у&nbsp;каждого свой.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-10.jpg" alt="Команда Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-11.jpg" alt="Участники команды" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
</div>
<p style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy2/marafon/">Как устроен Марафон</a> <a class="btn btn-ghost" href="/chizhovy2/sessiya/" style="margin-left:8px">Записаться на&nbsp;собеседование</a></p>
</div></section>
""")

# ================= СЛОВАРЬ ШКОЛЫ =================
P["slovar/index.html"] = ("Словарь школы · Настоящие отношения",
"Точка А, событийный круг, маятники, важность, намерение, нолик провалился: язык школы с переводом на обычный.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/slovar-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Язык школы</p><h1>Словарь школы</h1>
<p class="lead">У&nbsp;выпускников есть свой язык: короткие слова, за&nbsp;которыми стоят большие механизмы. Здесь перевод на&nbsp;обычный русский, чтобы на&nbsp;первой же&nbsp;группе всё было понятно.</p></div></div>

<section><div class="wrap">
<p class="eyebrow">Про честность с&nbsp;собой</p>
<div class="grid2" style="margin-top:10px;margin-bottom:34px">
<div class="card white">{icon('target')}<h3>Точка&nbsp;А</h3><p>Честное признание, где ты&nbsp;сейчас. Без прикрас и&nbsp;оправданий. Шаг первый и&nbsp;самый трудный: пока точка&nbsp;А не&nbsp;принята, двигаться&nbsp;некуда.</p></div>
<div class="card white">{icon('shield','var(--sand)')}<h3>Нолик провалился</h3><p>Момент, когда защита падает и&nbsp;человек наконец видит правду о&nbsp;себе. В&nbsp;группе это праздник. Отсюда и&nbsp;начинается настоящая&nbsp;работа.</p></div>
<div class="card white">{icon('loop','var(--sage-deep)')}<h3>Событийный круг</h3><p>Механизм повтора: событие включает эмоцию, эмоция будит старое решение, и&nbsp;оно доигрывает знакомый сценарий. Круг успевает провернуться раньше, чем включается сознание, поэтому усилием воли его не&nbsp;разорвать, сколько ни&nbsp;обещай себе&nbsp;спокойствия.</p></div>
<div class="card white">{icon('layers')}<h3>Этаж слов и&nbsp;этаж тела</h3><p>Понимание живёт на&nbsp;верхнем этаже. Запись хранится на&nbsp;нижнем: в&nbsp;эмоции и&nbsp;теле. Книги стучатся в&nbsp;верхний, работа школы идёт на&nbsp;нижний.</p></div>
</div>

<p class="eyebrow">Про состояние</p>
<div class="grid2" style="margin-top:10px;margin-bottom:34px">
<div class="card white">{icon('flame')}<h3>Сначала состояние</h3><p>Главное здесь: всё начинается с&nbsp;состояния, а&nbsp;не с&nbsp;планов на&nbsp;бумаге. Меняется оно, меняются решения, за&nbsp;ними события. Ученики говорят короче: мир&nbsp;зеркалит.</p></div>
<div class="card white">{icon('mountain','var(--sage-deep)')}<h3>Муравей и&nbsp;слон</h3><p>Разум мал и&nbsp;суетлив, как муравей. Состояние огромно, как слон. Пока слон идёт в&nbsp;другую сторону, планы разума весят меньше грамма: масса не&nbsp;та.</p></div>
<div class="card white">{icon('gear','var(--sand)')}<h3>Захват</h3><p>Момент, когда эмоциональный мозг перехватывает управление. Умный взрослый человек ведёт себя как не&nbsp;свой, и&nbsp;пока захват держит, «взять себя в&nbsp;руки» физически&nbsp;нечем.</p></div>
<div class="card white">{icon('hourglass')}<h3>Девяносто секунд</h3><p>Столько живёт химия эмоции, если не&nbsp;кормить её&nbsp;мыслями по&nbsp;кругу. Пауза и&nbsp;внимание к&nbsp;телу дают волне пройти. Дальше решается&nbsp;ясно.</p></div>
</div>

<p class="eyebrow">Про ежедневную практику</p>
<div class="grid2" style="margin-top:10px">
<div class="card white">{icon('route')}<h3>Намерение</h3><p>Утренняя практика Марафона: из&nbsp;какого состояния иду в&nbsp;день и&nbsp;что создаю. Желание просит. Намерение спокойно&nbsp;знает.</p></div>
<div class="card white">{icon('ceiling','var(--sand)')}<h3>Важность</h3><p>Раздутая ставка на&nbsp;результат, которая включает страх и&nbsp;сжимает выбор. Снял важность, вернулась лёгкость. Переговоры, свидания и&nbsp;большие решения идут после этого&nbsp;иначе.</p></div>
<div class="card white">{icon('pendulum','var(--sage-deep)')}<h3>Маятники</h3><p>Всё, что кормится твоей реакцией: скандал, лента новостей, чужая паника. Дёрнулся, отдал энергию. Навык школы: заметить крючок и&nbsp;не&nbsp;схватиться.</p></div>
<div class="card white">{icon('people')}<h3>Быть вкладом</h3><p>Развернуть фокус с&nbsp;«что мне дадут» на&nbsp;«что я&nbsp;даю». В&nbsp;паре, в&nbsp;команде, в&nbsp;деле. Участники отмечают: энергия от&nbsp;этого не&nbsp;уходит, а&nbsp;прибывает.</p></div>
<div class="card white">{icon('calendar')}<h3>Играть в&nbsp;долгую</h3><p>Горизонт вместо суеты: строить отношения и&nbsp;дело на&nbsp;годы, не&nbsp;выжимая быструю выгоду из&nbsp;каждой встречи. Опора выпускников в&nbsp;решениях.</p></div>
<div class="card white">{icon('sunrise','var(--sand)')}<h3>Открытия и&nbsp;благодарности</h3><p>Вечерняя практика: что понял за&nbsp;день и&nbsp;за&nbsp;что спасибо дню и&nbsp;людям. Держит новый способ жить крепче любой&nbsp;мотивации.</p></div>
</div>
<p class="note" style="margin-top:22px">Часть слов пришла из&nbsp;истоков метода: подробнее в&nbsp;разделах <a href="/chizhovy2/istoki/zeland-transerfing/">про трансерфинг</a> и&nbsp;<a href="/chizhovy2/istoki/nauka/">про науку</a>.</p>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Слова оживают в&nbsp;зале</h2>
<p class="sub" style="margin:0 0 26px">Читать словарь полезно, а&nbsp;по-настоящему эти слова понимаешь телом, в&nbsp;зале, когда очередь доходит до&nbsp;твоей сцены. Начни с&nbsp;гайда или запишись на&nbsp;собеседование.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>
""")

# ================= КОМУ: ПРЕДПРИНИМАТЕЛИ =================
FINCTA = """<section style="padding-top:0"><div class="narrow">
<h2>Начни с разговора на час</h2>
<p class="sub" style="margin:0 0 26px">Собеседование в&nbsp;школу: час о&nbsp;твоей ситуации и&nbsp;честный ответ, чем мы&nbsp;можем помочь. Для читателей сайта&nbsp;бесплатно.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Сначала почитать гайд</a></p>
</div></section>"""

P["dlya-predprinimatelej/index.html"] = ("Для предпринимателей · Настоящие отношения",
"Для всех опора, а сам устал: как школа работает с теми, кто привык всё тащить сам.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoriya-biznes.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Кому подходит · Предприниматели</p><h1>Для всех опора, а сам устал</h1>
<p class="lead">Бизнес, семья, статус: всё по&nbsp;списку. И&nbsp;усталость, о&nbsp;которой некому рассказать, потому что ты&nbsp;для всех опора. Мы&nbsp;шестнадцать лет работаем с&nbsp;людьми, которые привыкли тащить сами.</p></div></div>

<section><div class="narrow">
<h2>Знакомые ситуации</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('ceiling')}<h3>Дело упёрлось в потолок</h3><p>Рывки вверх быстро выравниваются обратно. Цифра оборота годами почти одна, и&nbsp;рынок тут ни&nbsp;при&nbsp;чём: держит старая запись.</p></div>
<div class="card">{icon('shield','var(--sand)')}<h3>Держать лицо</h3><p>Просить о&nbsp;помощи стыдно, показывать усталость нельзя. Панцирь, который когда-то спасал, теперь просто тяжёлый.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Решения из&nbsp;страха</h3><p>Суета, перестраховка, откладывание больших ходов. Он&nbsp;шепчет тише жадности, но&nbsp;рулит&nbsp;чаще.</p></div>
<div class="card">{icon('cups')}<h3>Дома сил уже нет</h3><p>Семье достаётся остаток после дела. Обычно он&nbsp;мал, и&nbsp;все это&nbsp;чувствуют.</p></div>
</div>
<div class="pull"><div class="q">«Я&nbsp;понимал крах, но&nbsp;не&nbsp;понимал, как начать снова и&nbsp;где найти силы.»</div><div class="who">Из истории ученика-предпринимателя</div></div>
<p>Один из&nbsp;наших учеников пришёл ровно из&nbsp;этой точки: кассовый разрыв, долги, отвернувшиеся друзья. Его полная история, с&nbsp;сопротивлением и&nbsp;переломом, опубликована с&nbsp;его согласия: <a href="/chizhovy2/istorii/predprinimatel/">заново после дна</a>.</p>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что меняется у владельца бизнеса</h2>
<p>Работа идёт с&nbsp;причиной, и&nbsp;она у&nbsp;потолка, страха и&nbsp;усталости общая: старые решения, которые крутят <a href="/chizhovy2/metod/" style="color:#D08A5F">событийный круг</a>. Когда запись переписана, меняется сразу несколько сфер. Большие решения принимаются спокойно. Дело перестаёт держаться на&nbsp;надрыве. Дома снова видно человека, а&nbsp;не&nbsp;функцию.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>16&nbsp;лет</b><span>практики с&nbsp;состоявшимися взрослыми&nbsp;людьми</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе: окружение твоего уровня, без&nbsp;толпы</span></div>
<div class="nail"><b>3&nbsp;месяца</b><span>сопровождения: результат закрепляется в&nbsp;деле</span></div>
</div></div></section>

<section><div class="narrow">
<h2>Что обычно мешает решиться</h2>
<p>Люди этого склада откладывают такую работу годами, и&nbsp;причины повторяются. Разберём три главные, потому что они&nbsp;же держат и&nbsp;сам потолок.</p>
<div class="card white" style="margin:20px 0 12px">{icon('hourglass')}<h3>«Разберусь, когда станет посвободнее»</h3><p>Свободнее не&nbsp;становится: дело забирает ровно то&nbsp;время, которое ему отдаёшь. Пять дней погружения выглядят дорого до&nbsp;тех пор, пока не&nbsp;посчитаешь, сколько лет уже съел один и&nbsp;тот&nbsp;же круг.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('shield','var(--sage-deep)')}<h3>«Я не&nbsp;из&nbsp;тех, кто ходит на&nbsp;тренинги»</h3><p>Понятная позиция после рынка, где обещают миллионы за&nbsp;выходные. Здесь другой формат: малая группа, отбор через разговор и&nbsp;никаких залов с&nbsp;таймерами. Проверить просто, начав с&nbsp;<a href="/chizhovy2/somneniya/">честного разбора сомнений</a>.</p></div>
<div class="card white">{icon('people','var(--sand)')}<h3>«Не&nbsp;хочу говорить о&nbsp;личном при чужих»</h3><p>В группе оказываются такие&nbsp;же взрослые люди с&nbsp;похожими историями, а&nbsp;личное остаётся в&nbsp;зале: это <a href="/chizhovy2/bezopasnost/">базовое правило</a>. Глубину выбираешь сам, темп твой.</p></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что меняется в&nbsp;деле</h2>
<p>Мы&nbsp;не&nbsp;учим управлять компанией и&nbsp;не&nbsp;даём бизнес-советов. Работа идёт с&nbsp;тем, из&nbsp;какого состояния принимаются решения. Рычаг оказывается сильным. Из&nbsp;покоя человек по-другому ведёт переговоры, легче делегирует и&nbsp;точнее считает&nbsp;риск.</p>
<p>Ученики чаще всего называют три сдвига: перестал держать всё на&nbsp;себе, начал видеть доску целиком вместо одной клетки, стал играть в&nbsp;долгую. Как это выглядело в&nbsp;жизни, видно в&nbsp;<a href="/chizhovy2/istorii/predprinimatel/" style="color:#D08A5F">истории ученика</a>.</p>
</div></section>
{FINCTA}
""")

# ================= КОМУ: ЖЕНЩИНЫ =================
P["dlya-zhenshchin/index.html"] = ("Для женщин · Настоящие отношения",
"Отношения, состояние, сценарии: как школа работает с теми, кто устал жить в режиме ожидания и обслуживания.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-m1.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Кому подходит · Женщины</p><h1>Вернуть себя себе</h1>
<p class="lead">Годами ждёшь, что&nbsp;тебя заметят, оценят, что&nbsp;близкий наконец изменится. Здесь работа начинается с&nbsp;другого конца: с&nbsp;твоего состояния, привычных реакций и&nbsp;той половины отношений, которая зависит от&nbsp;тебя.</p></div></div>

<section><div class="narrow">
<h2>С чем приходят чаще всего</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('loop')}<h3>Один сценарий с&nbsp;разными людьми</h3><p>Мужчины разные, финал одинаковый. Значит, дело не&nbsp;в&nbsp;них: сюжет приходит вместе с&nbsp;тобой, разворачивается по&nbsp;одной и&nbsp;той&nbsp;же схеме, и&nbsp;переписать его получится только&nbsp;изнутри.</p></div>
<div class="card">{icon('cups','var(--sand)')}<h3>Быт вместо близости</h3><p>Один календарь на&nbsp;двоих, разговоры про логистику. Не&nbsp;ссоритесь, потому что&nbsp;незачем. А&nbsp;хочется, чтобы снова было о&nbsp;чём молчать вдвоём.</p></div>
<div class="card">{icon('flame','var(--sage-deep)')}<h3>Чувства под анестезией</h3><p>Научилась обезболивать и&nbsp;не&nbsp;слышать себя. Снаружи «всё нормально», внутри давно тихо и&nbsp;пусто.</p></div>
<div class="card">{icon('speech')}<h3>Говоришь, а тебя не слышат</h3><p>Просьбы звучат как упрёки, разговоры кончаются глухой стеной. Дело не&nbsp;в&nbsp;словах: в&nbsp;состоянии, из&nbsp;которого они&nbsp;сказаны.</p></div>
</div>
<div class="pull"><div class="q">«Теперь знаю, что могу быть яркой, настоящей, звонкой, сама по&nbsp;себе.»</div><div class="who">Участница второго модуля</div></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что меняется</h2>
<p>На&nbsp;сцене видно, где чувства ушли в&nbsp;тень и&nbsp;какое решение их&nbsp;там держит: чаще всего оно принято очень рано, там, где показывать себя было опасно или бессмысленно. Когда запись переписана, возвращается то, что было под анестезией: яркость, желания, голос. Близкие замечают это раньше тебя. Отношения подтягиваются следом, <a href="/chizhovy2/para/" style="color:#D08A5F">даже когда работает один из&nbsp;двоих</a>.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>Сцена</b><span>работа телом и&nbsp;эмоцией, где хранится&nbsp;запись</span></div>
<div class="nail"><b>Группа</b><span>место, где тебя слышат с&nbsp;первого&nbsp;слова</span></div>
<div class="nail"><b>90&nbsp;дней</b><span>практики, чтобы новое состояние стало&nbsp;обычным</span></div>
</div></div></section>

<section><div class="narrow">
<h2>Три вопроса, которые задают почти все</h2>
<div class="card white" style="margin:20px 0 12px">{icon('speech')}<h3>«А если муж против?»</h3><p>Так бывает часто, и&nbsp;это не&nbsp;повод отказываться от&nbsp;своей работы: приходить одной можно и&nbsp;нужно, потому что твоя половина общего сценария всё равно в&nbsp;твоих руках. Многие мужчины приходят вторым заходом сами, увидев перемены дома. Про совместный формат: <a href="/chizhovy2/para/">тренинг для пар</a>.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('cups','var(--sage-deep)')}<h3>«Куда деть детей на&nbsp;пять дней?»</h3><p>Вопрос решаемый, и&nbsp;его стоит решить. Пять дней в&nbsp;году на&nbsp;себя это меньше, чем женщины обычно тратят на&nbsp;чужие дела за&nbsp;неделю. Первый модуль вообще идёт с&nbsp;вечера пятницы по&nbsp;воскресенье.</p></div>
<div class="card white">{icon('flame','var(--sand)')}<h3>«Я снова буду плакать при всех?»</h3><p>Слёзы в&nbsp;зале случаются, и&nbsp;это разморозка, а&nbsp;вовсе не&nbsp;слабость. Участницы говорят об&nbsp;этом как о&nbsp;самом ценном: «впервые за&nbsp;годы плакала при людях и&nbsp;поняла, что это не&nbsp;стыдно».</p></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Чего здесь точно не&nbsp;будет</h2>
<p>Ни&nbsp;уроков женственности, ни&nbsp;советов «как удержать мужчину», ни&nbsp;списков правильного поведения. Мы&nbsp;не&nbsp;делим людей на&nbsp;роли и&nbsp;не&nbsp;выдаём инструкций, как надо жить.</p>
<p>Работа идёт с&nbsp;другим: где ты&nbsp;себя приглушила, какое решение это держит и&nbsp;что вернётся, когда оно перестанет действовать. Дальше ты&nbsp;решаешь сама, как это применить: в&nbsp;паре, в&nbsp;деле, с&nbsp;детьми, с&nbsp;матерью. Принципы школы описаны в&nbsp;<a href="/chizhovy2/manifest/" style="color:#D08A5F">манифесте</a>.</p>
</div></section>
{FINCTA}
""")

# ================= КАК ПРОХОДИТ =================
P["kak-prohodit/index.html"] = ("Как проходит обучение · Настоящие отношения",
"Путь ученика по шагам: собеседование, три модуля с интеграцией, сопровождение. Что происходит в зале.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-06.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Как проходит</p><h1>Путь ученика по&nbsp;шагам</h1>
<p class="lead">Без сюрпризов: рассказываем по&nbsp;порядку, что&nbsp;будет от&nbsp;первого разговора до&nbsp;перемен, которые остаются надолго. Каждый шаг добровольный, на&nbsp;любом можно остановиться.</p></div></div>

<section><div class="wrap">
<p class="eyebrow">Маршрут</p>
<h2>От собеседования до&nbsp;Марафона</h2>
<div class="timeline" style="margin-top:28px">{timeline_svg()}</div>
<div class="timeline-m" style="margin-top:28px">
<div class="tm"><div class="c">I</div><div><b>Возвращение к&nbsp;себе</b><span>2,5 дня очно</span></div></div>
<div class="gap">месяц на&nbsp;интеграцию</div>
<div class="tm"><div class="c">II</div><div><b>Внутренняя свобода</b><span>5 дней очно</span></div></div>
<div class="gap">ещё 3-5 недель до&nbsp;финала</div>
<div class="tm last"><div class="c">III</div><div><b>Создатель реальности</b><span>3 месяца в&nbsp;жизни, результаты&nbsp;остаются</span></div></div>
</div>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">0</span>{icon('speech')}<h3>Собеседование</h3><p>Час живого разговора: твоя ситуация, честный взгляд и&nbsp;решение с&nbsp;двух сторон, по&nbsp;пути&nbsp;ли нам. Для&nbsp;читателей сайта бесплатно.</p></div>
<div class="card"><span class="bignum">1-2</span>{icon('people','var(--sage-deep)')}<h3>Очные модули</h3><p>Погружение на&nbsp;несколько дней: сцены, разборы, работа с&nbsp;состоянием в&nbsp;группе 10-20 человек. Между модулями недели интеграции: новое проверяется обычной жизнью.</p></div>
<div class="card"><span class="bignum">3</span>{icon('calendar','var(--sand)')}<h3>Марафон</h3><p>Три месяца в&nbsp;настоящей жизни: команда, еженедельные разборы с&nbsp;ведущими и&nbsp;<a href="/chizhovy2/praktiki/">ежедневная практика</a>.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Что происходит в&nbsp;зале</h2>
<p>Ядро работы: <a href="/chizhovy2/istoki/moreno-psihodrama/">живая сцена</a>. Ты&nbsp;называешь ситуацию, которая держит, группа помогает её&nbsp;построить, и&nbsp;несостоявшийся разговор наконец происходит. Рядом разборы, работа с&nbsp;состоянием и&nbsp;простые приёмы, которые уезжают с&nbsp;тобой домой и&nbsp;делают своё дело в&nbsp;обычный вторник, когда никакой группы рядом&nbsp;нет.</p>
<p>Глубина всегда добровольна: никто не&nbsp;вытаскивает силой, темп каждый выбирает сам. Обычно уже к&nbsp;вечеру первого дня зал перестаёт быть чужим: у&nbsp;людей одинаковые боли, и&nbsp;в&nbsp;соседней истории ты&nbsp;узнаёшь свою. Подробнее о&nbsp;рамках: <a href="/chizhovy2/bezopasnost/">безопасность и&nbsp;границы</a>.</p>
<div class="pull"><div class="q">«Ты получишь ровно ту&nbsp;порцию, которая нужна именно&nbsp;сейчас.»</div><div class="who">Слова выпускника новичкам</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Организация</p>
<h2>Бытовые вопросы</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('calendar')}<h3>Когда и&nbsp;где</h3><p>Очно в&nbsp;Москве, малой группой. Первый модуль начинается в&nbsp;пятницу вечером, чтобы не&nbsp;пришлось брать отпуск. Даты ближайшего набора называем на&nbsp;собеседовании.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Сколько человек</h3><p>От десяти до&nbsp;двадцати. Меньше не&nbsp;даёт нужной динамики сцены, больше лишает камерности: за&nbsp;шестнадцать лет цифра проверена десятками групп.</p></div>
<div class="card">{icon('shield','var(--sand)')}<h3>Что взять с&nbsp;собой</h3><p>Удобную одежду, воду и&nbsp;готовность к&nbsp;длинным дням. Ни&nbsp;конспектов, ни&nbsp;подготовки: материал приносишь ты&nbsp;сам, своей жизнью.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Что происходит между модулями</h2>
<p>Недели интеграции это рабочая часть программы. Ты&nbsp;выходишь в&nbsp;обычные дни и&nbsp;наблюдаешь: где новое уже держится, а&nbsp;где старая запись отыгрывает своё. Никаких заданий на&nbsp;оценку, только честные наблюдения.</p>
<p>Ведущие остаются на&nbsp;связи, а&nbsp;группа продолжает общаться в&nbsp;чате. Этот материал становится основой следующего погружения: приходишь не&nbsp;с&nbsp;чистого листа, а&nbsp;с&nbsp;конкретными местами, где заклинило.</p>
</div></section>
{FINCTA}
""")

# ================= ПРАКТИКИ =================
P["praktiki/index.html"] = ("Ежедневные практики · Настоящие отношения",
"Утреннее намерение, вечерние открытия и благодарности, маятники и важность: как выглядит день ученика.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/slovar-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Практики школы</p><h1>Из чего состоит день ученика</h1>
<p class="lead">Каждый день несколько коротких действий, которые держат состояние и&nbsp;внимание. Ниже практики Марафона, как их&nbsp;ведут наши команды.</p></div></div>

<section><div class="narrow">
<div class="timeline-m" style="display:block;margin-bottom:26px">
<div class="tm"><div class="c" style="background:var(--sand);color:#1B1410">У</div><div><b>Утро: намерение</b><span>из какого состояния иду в&nbsp;день и&nbsp;что создаю</span></div></div>
<div class="gap">днём: замечать маятники, снимать&nbsp;важность</div>
<div class="tm last"><div class="c">В</div><div><b>Вечер: открытия и&nbsp;благодарности</b><span>что понял за&nbsp;день, за&nbsp;что спасибо</span></div></div>
</div>

<h2>Разбираем каждую практику</h2>
<div class="card white" style="margin:20px 0 12px">{icon('route')}<h3>Намерение на&nbsp;день</h3><p>Утром формулируешь не&nbsp;список дел, а&nbsp;фокус дня и&nbsp;состояние, из&nbsp;которого в&nbsp;него идёшь: «в&nbsp;моей жизни возможно только так». Желание просит, намерение спокойно&nbsp;знает. Научная опора: <a href="/chizhovy2/istoki/nauka/">исследования Голвитцера</a>.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('pendulum','var(--sage-deep)')}<h3>Выход из&nbsp;маятников</h3><p>Днём замечаешь, что кормится твоей реакцией: скандал, лента, чужая паника. Заметил крючок, не&nbsp;схватился, сохранил энергию. Словами ученика: «отследил, не&nbsp;среагировал, удержал состояние весь день».</p></div>
<div class="card white" style="margin-bottom:12px">{icon('ceiling','var(--sand)')}<h3>Снятие важности</h3><p>Где вцепился, там и&nbsp;заклинило. Раздутая ставка включает страх и&nbsp;сжимает выбор до&nbsp;одного варианта, который почти всегда хуже остальных. Отпустил, вернулась лёгкость: переговоры, свидания, большие решения идут&nbsp;иначе.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('people')}<h3>Быть вкладом</h3><p>Развернуть фокус с&nbsp;«что мне дадут» на&nbsp;«что я&nbsp;даю»: дома, в&nbsp;команде, в&nbsp;деле и&nbsp;в&nbsp;разговоре, который не&nbsp;хочется начинать. Участники отмечают: энергия от&nbsp;этого прибывает, и&nbsp;люди поворачиваются&nbsp;лицом.</p></div>
<div class="card white">{icon('sunrise','var(--sage-deep)')}<h3>Открытия и&nbsp;благодарности</h3><p>Вечером короткий итог: что открыл про себя, за&nbsp;что спасибо дню и&nbsp;людям. Закрепляет новый способ жить надёжнее любой мотивации.</p></div>

<p class="note" style="margin-top:18px">Термины из&nbsp;практик разобраны в&nbsp;<a href="/chizhovy2/slovar/">словаре школы</a>, живой пример девяноста дней: <a href="/chizhovy2/istorii/komanda-mir/">история команды «МИР»</a>.</p>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Почему это работает</h2>
<p>Практики выглядят обманчиво просто: пара минут утром, пара вечером. Сила в&nbsp;другом. Каждое утро ты&nbsp;выбираешь состояние сам, вместо того чтобы получить его по&nbsp;умолчанию от&nbsp;новостей и&nbsp;чужого настроения. Каждый вечер закрепляешь то, что сработало.</p>
<p>За этим стоит понятный механизм: конкретно сформулированное намерение резко повышает шанс дойти до&nbsp;действия, а&nbsp;названные вслух чувства теряют власть. Подробнее в&nbsp;разделе <a href="/chizhovy2/istoki/nauka/">про науку</a>. Плюс эффект накопления. Девяносто повторов подряд делают усилие&nbsp;привычкой.</p>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Частые ошибки</p>
<h2>Из-за чего практика перестаёт работать</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('book','var(--copper)')}<h3>Писать для галочки</h3><p>Формальная запись перестаёт быть выбором. Лучше одна честная строка, чем красивый абзац ни&nbsp;о&nbsp;чём.</p></div>
<div class="card">{icon('loop','var(--copper)')}<h3>Бросать после срыва</h3><p>Пропустил три дня, решил, что не&nbsp;получилось. Практика начинается заново с&nbsp;любого дня, и&nbsp;это нормальный ход.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Делать в&nbsp;одиночку</h3><p>Без команды и&nbsp;разборов человек не&nbsp;видит собственных слепых зон. Поэтому практика идёт внутри группы, а&nbsp;не&nbsp;в&nbsp;личном блокноте.</p></div>
</div>
</div></section>
{FINCTA}
""")

# ================= МАНИФЕСТ =================
P["manifest/index.html"] = ("Манифест школы · Настоящие отношения",
"Почему школа называется «Настоящие отношения» и какие принципы здесь не продаются.", "vedushchie", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/portret.jpg');background-position:center 25%"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Манифест</p><h1>Почему «Настоящие отношения»</h1>
<p class="lead">Название школы не&nbsp;только про пары. Это про отношения с&nbsp;собой, с&nbsp;делом, с&nbsp;близкими и&nbsp;с правдой. Про всё, где кончается «казаться» и&nbsp;начинается «быть».</p></div></div>

<section><div class="narrow">
<div class="pull" style="margin-top:0"><div class="q">«У&nbsp;нас не&nbsp;было идеальной истории. Было непонимание, ошибки, потери, моменты, где казалось: дальше некуда. Именно там началось настоящее.»</div><div class="who">Алексей и&nbsp;Ирина Чижовы</div></div>
<p>Школу ведёт пара, которая семнадцать лет строит свои отношения: с&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них. Поэтому здесь не&nbsp;учат жить и&nbsp;не&nbsp;мотивируют со&nbsp;сцены. Вместе разбираются: откуда берётся твоя реакция и&nbsp;что с&nbsp;этим делать&nbsp;по‑настоящему.</p>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Принципы, которые не&nbsp;продаются</p>
<h2>На чём стоим</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('target','var(--copper)')}<h3>Отбор важнее выручки</h3><p>Вход через собеседование, и&nbsp;это фильтр, а&nbsp;не&nbsp;формальность. Отговорить можем так&nbsp;же честно, как&nbsp;пригласить.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Маленькая группа важнее большого зала</h3><p>Группы 10-20 человек, каждого знаем по&nbsp;имени. Расти будем числом групп, зал большим не&nbsp;станет.</p></div>
<div class="card">{icon('speech','var(--copper)')}<h3>Честность важнее красивой картинки</h3><p>Истории учеников публикуем с&nbsp;согласия и&nbsp;без глянца, результат у&nbsp;каждого свой. Истоки метода <a href="/chizhovy2/istoki/" style="color:#D08A5F">называем&nbsp;открыто</a>.</p></div>
<div class="card">{icon('mountain','var(--copper)')}<h3>Глубина важнее скорости</h3><p>Мы&nbsp;за&nbsp;работу с&nbsp;причиной, поэтому формат длинный: погружение, интеграция, сопровождение. Быстрых чудес не&nbsp;обещаем.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Во что мы&nbsp;верим</h2>
<p>Человек не&nbsp;сломан. Что&nbsp;бы с&nbsp;ним ни&nbsp;происходило, внутри цела способность выбирать, просто её&nbsp;перекрывают решения, принятые когда-то в&nbsp;трудный момент. Тогда они спасали. Сегодня держат.</p>
<p>Поэтому мы&nbsp;не&nbsp;чиним людей и&nbsp;не&nbsp;ставим диагнозов. Мы&nbsp;помогаем добраться до&nbsp;точки, где выбор был сделан впервые, и&nbsp;принять другое решение: осознанно, из&nbsp;сегодняшнего дня. Всё остальное человек делает сам, и&nbsp;в&nbsp;этом смысле школа возвращает авторские права на&nbsp;собственную жизнь.</p>
<p>Ещё мы&nbsp;верим, что глубокая работа возможна без надрыва и&nbsp;без цирка. Без криков со&nbsp;сцены, без унижения ради «слома эго», без таймеров на&nbsp;оплату и&nbsp;без ночных марафонов на&nbsp;выносливость, после которых истощение легко спутать с&nbsp;прорывом. Взрослому человеку достаточно честного зеркала и&nbsp;безопасного пространства, чтобы увидеть своё и&nbsp;сделать шаг.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Почему такое имя</p>
<h2>«Настоящие» значит без масок</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('mirror')}<h3>С собой</h3><p>Первое, что здесь налаживается, это связь с&nbsp;самим собой. Пока внутри идёт война, снаружи мира не&nbsp;будет.</p></div>
<div class="card">{icon('cups','var(--sage-deep)')}<h3>С близкими</h3><p>Когда снимаются роли, в&nbsp;паре и&nbsp;в&nbsp;семье впервые за&nbsp;годы становится видно живого человека вместо функции.</p></div>
<div class="card">{icon('target','var(--sand)')}<h3>С делом и&nbsp;миром</h3><p>Дело, деньги, окружение перестают быть сценой, где нужно казаться. Оттого и&nbsp;результаты становятся другими.</p></div>
</div>
</div></section>
{FINCTA}
""")

# ================= БЕЗОПАСНОСТЬ =================
P["bezopasnost/index.html"] = ("Безопасность и границы · Настоящие отношения",
"Честные рамки работы: кому школа не подойдёт, правила группы, добровольность глубины.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Безопасность и&nbsp;границы</p><h1>Сначала правила, потом глубина</h1>
<p class="lead">Работать всерьёз можно только там, где безопасно. Поэтому у&nbsp;школы есть правила, и&nbsp;мы называем их&nbsp;до начала, а&nbsp;не после.</p></div></div>

<section><div class="narrow">
<h2>На чём держится безопасность</h2>
<div class="card white" style="margin:20px 0 12px">{icon('route')}<h3>Глубину выбираешь сам</h3><p>Никто не&nbsp;вытаскивает силой: темп и&nbsp;меру открытости каждый выбирает сам. Сцена начинается, когда ты&nbsp;готов.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('shield','var(--sage-deep)')}<h3>Личное остаётся в&nbsp;зале</h3><p>Истории участников не&nbsp;выносятся из&nbsp;группы, это базовое правило. Публикуем только то, на&nbsp;что автор дал согласие, и&nbsp;спрашиваем каждый&nbsp;раз.</p></div>
<div class="card white">{icon('speech','var(--sand)')}<h3>Честность с первого дня</h3><p>Собеседование для того и&nbsp;нужно, чтобы решить с&nbsp;двух сторон, твоё&nbsp;ли это место. Если видим, что нет, говорим об&nbsp;этом&nbsp;сразу.</p></div>

<h2 style="margin-top:34px">Кому школа не&nbsp;подойдёт</h2>
<p>Тем, кто ищет волшебную таблетку за&nbsp;вечер. Тем, кто пока не&nbsp;готов работать в&nbsp;группе. И&nbsp;тем, кому сейчас нужна медицинская помощь: тренинг её&nbsp;не&nbsp;заменяет. Об&nbsp;этом мы&nbsp;говорим прямо на&nbsp;первом&nbsp;разговоре и&nbsp;подсказываем, куда идти, потому что погружение требует сил, а&nbsp;в&nbsp;остром состоянии оно скорее нагрузит, чем&nbsp;поможет.</p>
<p>Остальное про формат разобрано на&nbsp;странице <a href="/chizhovy2/voprosy/">вопросов и&nbsp;ответов</a>.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Правила зала</p>
<h2>О чём договариваемся на&nbsp;старте</h2>
<p class="sub">Эти договорённости озвучиваются в&nbsp;первый вечер, действуют все дни модуля и&nbsp;распространяются на&nbsp;всех, кто в&nbsp;зале, включая&nbsp;ведущих.</p>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('shield')}<h3>Конфиденциальность</h3><p>Всё, что прозвучало в&nbsp;зале, остаётся в&nbsp;зале. Своим опытом делиться можно, чужими историями&nbsp;нет.</p></div>
<div class="card">{icon('speech','var(--sage-deep)')}<h3>Говорим о&nbsp;себе</h3><p>Без советов, диагнозов и&nbsp;оценок в&nbsp;адрес других участников. Только свой опыт и&nbsp;свои&nbsp;чувства.</p></div>
<div class="card">{icon('route','var(--sand)')}<h3>Право на&nbsp;паузу</h3><p>Стоп можно сказать в&nbsp;любой момент, и&nbsp;это уважают все, без уговоров и&nbsp;просьб объясниться: человек сам знает свой край, а&nbsp;вытащенное силой всё равно не&nbsp;удержится.</p></div>
<div class="card">{icon('people')}<h3>Присутствие</h3><p>Телефоны в&nbsp;стороне, опоздания и&nbsp;уходы по&nbsp;делам не&nbsp;практикуются. Глубина держится на&nbsp;непрерывности.</p></div>
<div class="card">{icon('flame','var(--sage-deep)')}<h3>Трезвость</h3><p>Никакого алкоголя и&nbsp;веществ на&nbsp;время модуля. Работа идёт с&nbsp;тонкими состояниями: любая химия сверху сбивает и&nbsp;точность ведущего, и&nbsp;собственное чувство&nbsp;участника.</p></div>
<div class="card">{icon('gear','var(--sand)')}<h3>Ответственность</h3><p>Ты&nbsp;решаешь, насколько глубоко идти и&nbsp;что делать с&nbsp;увиденным. Ведущие держат процесс, но&nbsp;жизнь за&nbsp;тебя не&nbsp;проживают.</p></div>
</div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Кто ведёт и за что отвечает</h2>
<p>Группу всегда ведут двое: <a href="/chizhovy2/vedushchie/" style="color:#D08A5F">Алексей и&nbsp;Ирина</a>. Один держит структуру и&nbsp;видит карту целиком, вторая идёт за&nbsp;живым и&nbsp;чувствует состояние участника раньше слов. За&nbsp;шестнадцать лет через их&nbsp;зал прошли десятки&nbsp;групп.</p>
<p>Поэтому в&nbsp;тяжёлом процессе рядом всегда есть тот, кто видит происходящее со&nbsp;стороны и&nbsp;знает, как вывести человека обратно. В&nbsp;одиночку так не&nbsp;работают.</p>
</div></section>
{FINCTA}
""")

# ================= СООБЩЕСТВО =================
P["soobshchestvo/index.html"] = ("Сообщество выпускников · Настоящие отношения",
"Команды, забеги, поддержка после модулей: во что превращается группа после тренинга.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-12.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Сообщество</p><h1>Группа, которая не&nbsp;расходится</h1>
<p class="lead">Модуль заканчивается, а&nbsp;люди остаются рядом: общие практики, встречи, забеги и&nbsp;поддержка, которая работает даже в&nbsp;два часа ночи.</p></div></div>

<section><div class="narrow">
<h2>Во что превращается группа</h2>
</div>
<div class="wrap"><div class="grid3" style="margin-top:24px">
<div class="card">{icon('people')}<h3>Команда</h3><p>На&nbsp;Марафоне группа собирается вокруг общей цели, у&nbsp;каждого свой напарник. Такой уровень окружения многим встречается&nbsp;впервые.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Забеги</h3><p>Команды выходят на&nbsp;старты вместе с&nbsp;Алексеем: тело быстро выдаёт, где ты&nbsp;себя обманываешь, и&nbsp;честно радуется, когда ты&nbsp;настоящий.</p></div>
<div class="card">{icon('cups','var(--sage-deep)')}<h3>Свои люди</h3><p>Выпускники дружат домами, делают дела вместе и&nbsp;приводят в&nbsp;школу близких: сарафан у&nbsp;нас главный канал с&nbsp;первого&nbsp;года.</p></div>
</div></div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Живые кадры</p>
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-01.jpg" alt="Группа у камина с сертификатами" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-09.jpg" alt="Участники тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-03.jpg" alt="Выпуск группы" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-13.jpg" alt="Финал модуля" loading="lazy"></div>
</div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Истории людей с&nbsp;этих фото</a></p>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Что происходит после выпуска</h2>
<p>Формально сопровождение заканчивается через три месяца. Фактически люди остаются рядом: чаты команд живут годами. Один каждое утро продолжает писать намерение, другой собирает своих на&nbsp;пробежку, третий зовёт на&nbsp;день рождения половину группы.</p>
<p>Это не&nbsp;клуб по&nbsp;расписанию, а&nbsp;живая среда. Она держится на&nbsp;простой вещи: люди прошли вместе то, чего обычно не&nbsp;проходят даже с&nbsp;близкими, и&nbsp;после такого общение идёт сразу по&nbsp;сути.</p>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('speech')}<h3>Разговор без предисловий</h3><p>Не&nbsp;нужно объяснять контекст и&nbsp;подбирать слова: все говорят на&nbsp;одном языке и&nbsp;помнят свою точку&nbsp;А.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Поддержка, когда сорвался</h3><p>Когда старая запись берёт своё, рядом есть те, кто это уже проходил и&nbsp;не&nbsp;станет утешать общими словами.</p></div>
<div class="card">{icon('target','var(--sand)')}<h3>Общие дела</h3><p>Совместные проекты, партнёрства, найм внутри среды. Похожие ценности сводят людей&nbsp;быстро.</p></div>
<div class="card">{icon('flame')}<h3>Новые приходят через своих</h3><p>Большинство участников школы пришли по&nbsp;рекомендации выпускников. Это главный канал набора с&nbsp;первого года.</p></div>
</div>
</div></section>
{FINCTA}
""")

# ================= С ЧЕГО НАЧАТЬ =================
P["start/index.html"] = ("С чего начать · Настоящие отношения",
"Маршрут новичка: гайд, собеседование, первый модуль. Три шага без обязательств.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Новичку</p><h1>С чего начать</h1>
<p class="lead">Не&nbsp;нужно сразу решаться на&nbsp;модуль. Вот короткий маршрут. Каждый шаг бесплатный и добровольный, и&nbsp;после каждого становится понятнее.</p></div></div>

<section><div class="narrow">
<div class="card white" style="margin-bottom:12px"><span class="bignum">01</span>{icon('book')}<h3>Прочитай гайд</h3><p>«Кто пишет сценарий твоей жизни»: главное ядро метода в&nbsp;одном выпуске, с&nbsp;самодиагностикой. Полчаса чтения, чтобы примерить механику на&nbsp;себя. <a href="/chizhovy2/gid/">Читать&nbsp;гайд</a></p></div>
<div class="card white" style="margin-bottom:12px"><span class="bignum">02</span>{icon('lens','var(--sage-deep)')}<h3>Осмотрись</h3><p>Как устроен <a href="/chizhovy2/metod/">метод</a> и&nbsp;<a href="/chizhovy2/kak-prohodit/">путь ученика</a>, из&nbsp;чего <a href="/chizhovy2/istoki/">собран подход</a>, что говорят <a href="/chizhovy2/istorii/">люди в&nbsp;историях</a>. Всё открыто, без&nbsp;«узнаете на&nbsp;вебинаре».</p></div>
<div class="card white"><span class="bignum">03</span>{icon('speech','var(--sand)')}<h3>Приходи на&nbsp;собеседование</h3><p>Час живого разговора о&nbsp;твоей ситуации: честный взгляд со&nbsp;стороны и&nbsp;понятный следующий шаг. Для&nbsp;читателей сайта бесплатно. <a href="/chizhovy2/sessiya/">Записаться</a></p></div>
<p class="note" style="margin-top:18px">Дальше всё по&nbsp;порядку: <a href="/chizhovy2/programma/">программа из&nbsp;трёх модулей</a>, между ними интеграция, после: Марафон и&nbsp;сообщество.</p>
</div></section>
{FINCTA}
""")

# ================= КОНТАКТЫ =================
P["kontakty/index.html"] = ("Контакты · Настоящие отношения",
"Как связаться со школой: Telegram, запись на собеседование.", "", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Контакты</p><h1>На связи</h1>
<p class="lead">Отвечаем сами, без ботов и заготовленных фраз. Пиши так,&nbsp;как тебе удобно.</p></div></div>

<section><div class="narrow">
<div class="grid2" style="margin-top:6px">
<div class="card white">{icon('speech')}<h3>Telegram</h3><p>Канал школы: анонсы наборов, живые тексты пары, ответы на&nbsp;вопросы. Там&nbsp;же видно, как мы&nbsp;говорим и&nbsp;о&nbsp;чём думаем, задолго до&nbsp;всякого собеседования: самый простой способ понять, свои мы&nbsp;люди или&nbsp;нет.</p><p style="margin-top:12px"><a href="https://t.me/+LVptSH6Mt4hhYmFi">Открыть Telegram</a></p></div>
<div class="card white">{icon('calendar','var(--sage-deep)')}<h3>Собеседование</h3><p>Час разговора о&nbsp;твоей ситуации, онлайн или очно. Для читателей сайта&nbsp;бесплатно.</p><p style="margin-top:12px"><a href="/chizhovy2/sessiya/">Записаться</a></p></div>
</div>
<p class="note" style="margin-top:20px">Реквизиты и&nbsp;документы для оплаты появятся здесь вместе с&nbsp;онлайн-оплатой.</p>
</div></section>
{FINCTA}
""")

# ================= ТЕХНИКИ СЦЕНЫ =================
P["tehniki-sceny/index.html"] = ("Техники сцены · Настоящие отношения",
"Обмен ролями, дублирование, зеркало, пустой стул: инструменты живой сцены с разбором.", "metod", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/metod-stul.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Инструменты в зале</p><h1>Техники живой сцены</h1>
<p class="lead">Со&nbsp;стороны сцена похожа на&nbsp;театр без сценария. На&nbsp;самом деле всё устроено точно: вот инструменты, которыми ведущие меняют старую запись, и&nbsp;вот что&nbsp;делает каждый.</p></div></div>

<section><div class="narrow">
<div class="card white" style="margin-bottom:12px">{icon('people')}<h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место другого человека из&nbsp;своей сцены и&nbsp;отвечаешь себе его словами. Пять минут в&nbsp;чужой роли показывают то, что годами не&nbsp;видно из&nbsp;своей: почему он&nbsp;молчит, чего она боится, что на&nbsp;самом деле стоит за&nbsp;фразой, которая тебя ранит.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('speech','var(--sage-deep)')}<h3>Дублирование</h3><p>Человек из&nbsp;группы становится рядом и&nbsp;договаривает то, что ты&nbsp;чувствуешь, но&nbsp;не&nbsp;решаешься произнести. Когда невысказанное впервые звучит вслух, тело отзывается сразу. Значит,&nbsp;попали.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('mirror','var(--sand)')}<h3>Зеркало</h3><p>Выходишь из&nbsp;собственной сцены и&nbsp;смотришь её&nbsp;со&nbsp;стороны, как зритель. Так впервые видно сценарий целиком: где включилась старая запись, в&nbsp;какой момент финал стал предрешён и&nbsp;что каждый из&nbsp;участников делал, чтобы всё закончилось именно&nbsp;так.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('cups')}<h3>Пустой стул</h3><p>Напротив ставится стул, и&nbsp;на&nbsp;нём «сидит» тот, с&nbsp;кем так и&nbsp;не&nbsp;поговорили: отец, бывший, ты&nbsp;сам из&nbsp;прошлого. Отложенный на&nbsp;годы разговор происходит здесь, и&nbsp;у&nbsp;него наконец появляется финал.</p></div>
<div class="card white">{icon('sunrise','var(--sage-deep)')}<h3>Новое решение</h3><p>Кульминация сцены: там, где когда-то был сделан старый выбор, ты&nbsp;делаешь другой. Новое пишется так&nbsp;же глубоко, как прежнее, телом и&nbsp;эмоцией. Поэтому и&nbsp;держится.</p></div>
<p style="margin-top:22px">Откуда эти инструменты и&nbsp;почему им&nbsp;сто лет: <a href="/chizhovy2/istoki/moreno-psihodrama/">Морено и&nbsp;психодрама</a>. Как сцена встроена в&nbsp;общую работу: <a href="/chizhovy2/metod/">метод целиком</a>.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Как это выглядит</p>
<h2>Одна сцена от&nbsp;начала до&nbsp;конца</h2>
<p class="sub">Условный случай, собранный из&nbsp;типичных ситуаций зала. Живые сцены идут по-разному, но&nbsp;порядок примерно такой.</p>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">1</span><h3>Запрос</h3><p>Мужчина говорит: с&nbsp;отцом двадцать лет холодно, разговора не&nbsp;выходит. Обозначаем сцену: кухня родительской квартиры, ему пятнадцать.</p></div>
<div class="card"><span class="bignum">2</span><h3>Разогрев</h3><p>Участник группы становится отцом, ещё один занимает место самого героя. Обстановка собирается из&nbsp;деталей: где стоял стол, кто где сидел.</p></div>
<div class="card"><span class="bignum">3</span><h3>Действие</h3><p>Звучит то, что тогда осталось внутри. Тело включается раньше слов: голос садится, руки дрожат, это нормальный ход процесса.</p></div>
<div class="card"><span class="bignum">4</span><h3>Обмен ролями</h3><p>Он встаёт на&nbsp;место отца и&nbsp;отвечает себе его словами. Часто именно тут впервые становится видно, что отец тоже не&nbsp;умел иначе.</p></div>
<div class="card"><span class="bignum">5</span><h3>Новое решение</h3><p>В точке, где когда-то было принято «своих чувств не&nbsp;показывать», принимается другое. Ведущий помогает произнести его вслух.</p></div>
<div class="card linen"><span class="bignum">6</span><h3>Возвращение</h3><p>Группа делится тем, что откликнулось в&nbsp;их&nbsp;историях. Герой выходит из&nbsp;роли и&nbsp;возвращается в&nbsp;сегодняшний день.</p></div>
</div>
<p class="note" style="margin-top:20px">Кто отвечает за&nbsp;безопасность процесса, описано на&nbsp;странице <a href="/chizhovy2/bezopasnost/">границ работы</a>.</p>
</div></section>
{FINCTA}
""")

# ================= ТРИ СОМНЕНИЯ =================
P["somneniya/index.html"] = ("Частые сомнения · Настоящие отношения",
"«Не верю, что поможет», «боюсь группы», «нет времени», «а вдруг станет хуже»: восемь честных разборов перед решением.", "somneniya", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/somneniya-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Перед решением</p><h1>Сомнения перед первым шагом</h1>
<p class="lead">Мы&nbsp;слышим их&nbsp;на&nbsp;каждом собеседовании и&nbsp;считаем хорошим знаком: сомневается тот, кто относится к&nbsp;делу серьёзно. Ниже восемь самых частых. Разбираем каждое начистоту, и&nbsp;если ты&nbsp;прав в&nbsp;своих опасениях, так&nbsp;и скажем.</p></div></div>

<section style="padding-bottom:40px"><div class="wrap">
<p class="eyebrow">Коротко</p>
<h2>О чём чаще всего думают</h2>
<div class="chiplist" style="margin-top:18px">
<span>Не&nbsp;верю, что поможет</span><span>У&nbsp;меня особый случай</span><span>Уже был у&nbsp;психолога</span><span>Боюсь группы</span><span>Нет времени</span><span>А вдруг станет хуже</span><span>Эффект пройдёт через неделю</span><span>Мужчине такое не&nbsp;нужно</span>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>1. «Просто не&nbsp;верю, что поможет»</h2>
<p>Самое прямое из&nbsp;всех, и&nbsp;мы&nbsp;его уважаем. Рынок тренингов приучил людей к&nbsp;обещаниям, после которых ничего не&nbsp;меняется. Недоверие тут здоровая реакция психики, признак осторожности, которая не&nbsp;раз тебя спасала.</p>
<p>Единственный честный ответ: проверяемость. Мы&nbsp;открыто показываем, <a href="/chizhovy2/istoki/">из&nbsp;чего собран метод</a> и&nbsp;на&nbsp;какой <a href="/chizhovy2/istoki/nauka/">науке</a> он&nbsp;стоит, публикуем <a href="/chizhovy2/istorii/">истории учеников</a> без глянца и&nbsp;не&nbsp;обещаем гарантированных перемен. Первый шаг ни&nbsp;к&nbsp;чему не&nbsp;обязывает: час разговора, после которого ты&nbsp;решаешь сам.</p>
<div class="pull"><div class="q">«Что останавливало? Просто недоверие, что поможет.»</div><div class="who">Ученик, который пришёл в&nbsp;кризисе и&nbsp;остался на&nbsp;все три модуля</div></div>

<h2 style="margin-top:36px">2. «У&nbsp;меня особый случай»</h2>
<p>Отчасти правда. Биографии у&nbsp;всех разные, и&nbsp;на&nbsp;сцене твоя разбирается индивидуально, без единого шаблона. Но&nbsp;механика повтора у&nbsp;людей общая: событие, эмоция, старое решение, знакомый финал. Поэтому в&nbsp;чужой истории на&nbsp;группе ты&nbsp;так часто узнаёшь свою: случаи особые, а&nbsp;<a href="/chizhovy2/metod/">круг один</a>.</p>
<p>За шестнадцать лет через зал прошли предприниматели после банкротства, пары на&nbsp;грани развода, руководители в&nbsp;выгорании, женщины, которые годами не&nbsp;слышали себя. Каждый заходил со&nbsp;словами «у&nbsp;меня всё сложнее». И&nbsp;все находили свою запись.</p>

<h2 style="margin-top:36px">3. «Я уже был у&nbsp;психолога»</h2>
<p>И&nbsp;это хорошо. Терапия и&nbsp;тренинг не&nbsp;соперники. Кабинетный формат идёт словами, по&nbsp;часу в&nbsp;неделю. Понимание он&nbsp;собирает отлично. Здесь всё держится на&nbsp;теле и&nbsp;эмоции, в&nbsp;живой сцене, в&nbsp;погружении на&nbsp;несколько дней: другой инструмент для другого слоя.</p>
<p>То, что ты&nbsp;накопил у&nbsp;психолога, здесь превращается в&nbsp;пережитый опыт. Многие наши ученики продолжают терапию параллельно. Мы&nbsp;это&nbsp;поддерживаем.</p>
</div></section>

<section style="padding:0"><div class="wrap">
<div class="ph" style="aspect-ratio:16/7"><img src="/chizhovy2/images/somneniya-gruppa.png" alt="Круг участников в зале тренинга" loading="lazy"></div>
</div></section>

<section><div class="narrow">
<h2>4. «Боюсь группы. Придётся раскрываться перед чужими»</h2>
<p>Звучит чаще остальных, и&nbsp;по-человечески понятно. Правда такая: глубина всегда добровольна, никто не&nbsp;вытаскивает силой, темп выбираешь ты. Можно первый день просто смотреть.</p>
<p>Обычно уже к&nbsp;вечеру первого дня чужих в&nbsp;зале не&nbsp;остаётся: у&nbsp;людей одинаковые боли, и&nbsp;это выясняется быстро. А&nbsp;ещё именно группа делает работу такой сильной: <a href="/chizhovy2/tehniki-sceny/">сцене нужны люди</a>, чужая история включает твою, и&nbsp;поддержка держит там, где одному тяжело. Все рамки описаны на&nbsp;странице <a href="/chizhovy2/bezopasnost/">безопасности</a>: личное остаётся в&nbsp;зале.</p>

<h2 style="margin-top:36px">5. «Нет времени: работа, дети, проекты»</h2>
<p>Его действительно нужно немало: два с&nbsp;половиной дня на&nbsp;первом модуле, пять дней на&nbsp;втором, дальше три месяца практики внутри обычной жизни. Мы&nbsp;не&nbsp;делаем вид, что это можно пройти между делом.</p>
<p>Встречный вопрос, который мы&nbsp;задаём на&nbsp;собеседовании: сколько времени уже съел повторяющийся круг? Ссоры по&nbsp;одному сценарию, решения, отложенные на&nbsp;годы, вечера в&nbsp;тяжёлом состоянии. Обычно счёт идёт не&nbsp;на&nbsp;дни, а&nbsp;на&nbsp;годы, и&nbsp;на&nbsp;этом фоне неделя погружения выглядит иначе.</p>

<h2 style="margin-top:36px">6. «А вдруг станет хуже: разведусь, поссорюсь, всё развалится»</h2>
<p>Страх понятный, и&nbsp;основание у&nbsp;него есть. Когда человек выходит из&nbsp;привычной роли, отношения вокруг перестраиваются. Но&nbsp;направление перемен задаёшь ты, а&nbsp;не&nbsp;тренинг. Мы&nbsp;не&nbsp;ведём к&nbsp;решениям «уходи» или «оставайся»: мы&nbsp;возвращаем способность видеть ситуацию ясно и&nbsp;выбирать спокойно.</p>
<p>По опыту групп чаще происходит обратное. То, что держалось на&nbsp;тяжёлом молчании, оживает. Пары нередко приходят вторым заходом уже <a href="/chizhovy2/para/">вдвоём</a>, потому что одному из&nbsp;двоих стало тесно молчать.</p>
</div></section>

<section style="padding:0"><div class="wrap">
<div class="ph" style="aspect-ratio:16/7"><img src="/chizhovy2/images/somneniya-nedoverie.png" alt="Мужчина у окна утром, решение принимается" style="object-position:center 8%" loading="lazy"></div>
</div></section>

<section><div class="narrow">
<h2>7. «Уже пробовал тренинги. Эффект держался неделю»</h2>
<p>Знакомо, и&nbsp;причина обычно одна: работа шла на&nbsp;верхнем этаже. Вдохновение, конспект, новые слова, а&nbsp;запись осталась там&nbsp;же, где была, в&nbsp;эмоции и&nbsp;теле. Первый стресс возвращает старую реакцию, и&nbsp;человек решает, что дело в&nbsp;нём.</p>
<p>Поэтому у&nbsp;нас формат длинный: погружение, недели интеграции между модулями и&nbsp;три месяца сопровождения. За&nbsp;девяносто дней новое поведение перестаёт быть праздничным и&nbsp;становится обычным. Как это выглядит день за&nbsp;днём: <a href="/chizhovy2/praktiki/">ежедневные практики</a> и&nbsp;<a href="/chizhovy2/istorii/komanda-mir/">история команды «МИР»</a>.</p>

<h2 style="margin-top:36px">8. «Мужчине такое не&nbsp;нужно»</h2>
<p>В зале примерно поровну тех и&nbsp;других. Мужская часть обычно упрямее всех на&nbsp;входе и&nbsp;благодарнее всех на&nbsp;выходе. Приходят за&nbsp;ясностью в&nbsp;решениях, за&nbsp;потолком в&nbsp;деле, за&nbsp;отношениями, которые перестали работать.</p>
<p>Школу ведёт пара. Алексей говорит на&nbsp;понятном языке: структура, дисциплина, дистанция, результат. <a href="/chizhovy2/dlya-predprinimatelej/">Отдельная страница для тех, кто привык тащить сам</a>.</p>
<div class="pull"><div class="q">«На тренинге я&nbsp;долго сопротивлялся, как баран. Труднее всего было принять точку&nbsp;А.»</div><div class="who">Из истории ученика-предпринимателя</div></div>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Честно</p>
<h2>Когда мы говорим «не сейчас»</h2>
<p class="lead" style="color:rgba(242,237,228,.75)">Бывают ситуации, когда правильный ответ «не&nbsp;сейчас» или «не&nbsp;сюда». Мы&nbsp;говорим об&nbsp;этом прямо на&nbsp;собеседовании и&nbsp;не&nbsp;берём человека ради заполненной группы.</p>
<div class="grid3" style="margin-top:24px">
<div class="card">{icon('shield','var(--copper)')}<h3>Нужна медицинская помощь</h3><p>Острое состояние, психиатрический диагноз в&nbsp;обострении: тренинг не&nbsp;заменяет врача. Подскажем, куда идти.</p></div>
<div class="card">{icon('calendar','var(--copper)')}<h3>Нет сил именно сейчас</h3><p>Переезд, роды, похороны, аврал на&nbsp;работе. Погружение требует сил, лучше прийти через полгода в&nbsp;своём темпе.</p></div>
<div class="card">{icon('target','var(--copper)')}<h3>Ищешь быстрый рецепт</h3><p>Если нужен готовый скрипт «как заставить его измениться», мы&nbsp;не&nbsp;поможем: работа идёт с&nbsp;тем, кто пришёл.</p></div>
</div>
<p style="margin-top:24px"><a class="btn btn-ghost" href="/chizhovy2/bezopasnost/">Все границы работы</a></p>
</div></section>

<section><div class="narrow">
<h2>Где всё это можно спросить вслух</h2>
<p>Собеседование и&nbsp;существует для сомнений. Час живого разговора: ты&nbsp;рассказываешь свою ситуацию, мы&nbsp;разбираем механику и&nbsp;честно говорим, поможет&nbsp;ли здесь школа. Отговорить можем так&nbsp;же спокойно, как&nbsp;пригласить.</p>
<div class="nails nails3" style="margin-top:22px">
<div class="nail"><b>60&nbsp;минут</b><span>онлайн или очно, без подготовки и&nbsp;правильных&nbsp;слов</span></div>
<div class="nail"><b>Бесплатно</b><span>для тех, кто пришёл с&nbsp;этого&nbsp;сайта</span></div>
<div class="nail"><b>0</b><span>обязательств: решение принимаешь&nbsp;потом</span></div>
</div>
<p style="margin-top:24px">Осталось сомнение, которого здесь нет? Принеси его на&nbsp;разговор: это ровно то&nbsp;место, где на&nbsp;него ответят прямо. Что ещё спрашивают о&nbsp;формате, собрано в&nbsp;разделе <a href="/chizhovy2/voprosy/">вопросов и&nbsp;ответов</a>.</p>
</div></section>

<section style="padding:0"><div class="wrap">
<div class="ph" style="aspect-ratio:16/7"><img src="/chizhovy2/images/somneniya-posle.png" alt="Осенняя дорожка в парке на закате" loading="lazy"></div>
</div></section>
{FINCTA}
""")

# ================= СТАТЬИ (ХАБ) =================
P["stati/index.html"] = ("Статьи школы · Настоящие отношения",
"Библиотека школы: разборы про отношения, состояние, сценарии, трансерфинг и психодраму языком метода.", "stati", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/stati-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Библиотека школы</p><h1 style="font-size:clamp(1.75rem,5.5vw,3.7rem)">Статьи, после&nbsp;которых что‑то&nbsp;щёлкает</h1>
<p class="lead">Разбираем то,&nbsp;с чем приходят в&nbsp;школу: почему ссоры идут по&nbsp;кругу, куда уходят силы и&nbsp;кто на&nbsp;самом деле пишет твой сценарий. Говорим языком метода и&nbsp;опираемся на&nbsp;науку.</p></div></div>

<section><div class="wrap">
<p class="eyebrow">Карта библиотеки</p>
<h2>Пять разделов библиотеки</h2>
<p class="sub">Ниже карта тем на&nbsp;вырост. Первые пять статей уже в&nbsp;работе, и&nbsp;каждая готовая появится здесь ссылкой, чтобы карта постепенно превращалась в&nbsp;библиотеку. Пока они пишутся, начни с&nbsp;бесплатного гайда: там метод разобран целиком, с&nbsp;самодиагностикой.</p>
<div class="grid2" style="margin-top:28px">
<div class="card">{icon('cups')}<h3>Отношения в паре</h3>
<div class="chiplist"><span>Ссоры по&nbsp;одному кругу</span><span>Быт съел близость</span><span>Муж молчит</span><span>Один сценарий с&nbsp;разными людьми</span><span>Кризис после десяти лет</span><span>Партнёры-соседи</span><span>Как говорить, чтобы услышали</span></div></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Состояние и&nbsp;выгорание</h3>
<div class="chiplist"><span>Нет сил при&nbsp;успехе</span><span>Тревога фоном</span><span>Всё понимаю, ничего не&nbsp;меняю</span><span>Устал быть сильным</span><span>Откуда берётся энергия</span></div></div>
<div class="card">{icon('route','var(--sage-deep)')}<h3>Сценарии и&nbsp;решения</h3>
<div class="chiplist"><span>Жизненный сценарий</span><span>Установки из&nbsp;детства</span><span>Денежный потолок</span><span>Самосаботаж</span><span>Почему аффирмации не&nbsp;работают</span></div></div>
<div class="card">{icon('loop')}<h3>Трансерфинг и&nbsp;est</h3>
<div class="chiplist"><span>Маятники простыми словами</span><span>Важность и&nbsp;как её&nbsp;снять</span><span>Намерение против желания</span><span>Что такое тренинг est</span><span>«Трансформация» Рейнхарта:&nbsp;разбор</span></div></div>
</div>
<div class="card linen" style="margin-top:16px">{icon('people','var(--sage-deep)')}<h3>Психодрама и метод школы</h3>
<div class="chiplist"><span>Что такое психодрама</span><span>Пустой стул</span><span>Как проходит групповая работа</span><span>Тренинг и&nbsp;терапия: в&nbsp;чём разница</span></div></div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Пока библиотека растёт</h2>
<p class="sub" style="margin:0 0 26px">Главное ядро школы уже собрано в&nbsp;бесплатном гайде «Кто пишет сценарий твоей жизни». Полчаса чтения. А&nbsp;живые вопросы можно принести на&nbsp;собеседование: для&nbsp;читателей сайта оно бесплатное.</p>
<p><a class="btn btn-wine" href="/chizhovy2/gid/">Читать гайд</a> <a class="btn btn-ghost" href="/chizhovy2/sessiya/" style="margin-left:8px">Записаться на&nbsp;собеседование</a></p>
</div></section>
""")

css_path = ROOT / "site.css"
css_path.write_text(CSS.strip() + "\n", encoding="utf-8")
n = 0
for rel, (title, desc, active, body) in P.items():
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(page(title, desc, active, body), encoding="utf-8")
    n += 1
print(f"OK v2: site.css + {n} страниц (иконки, диаграмма, таймлайн, мозаика, фавикон)")
