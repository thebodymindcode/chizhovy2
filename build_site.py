# -*- coding: utf-8 -*-
# Сборщик прототипа сайта «Настоящие отношения». v2: иконки, инфографика, журнальная сетка.
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
.narrow{max-width:720px;margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif;line-height:1.2;text-wrap:balance;margin:0 0 .5em}
h2{font-size:clamp(1.7rem,4vw,2.3rem);font-weight:600}
h3{font-size:1.22rem;font-weight:600}
p{margin:0 0 1.1em}
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
.dark .btn-ghost{color:var(--ntext);border-color:rgba(242,237,228,.5)}

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
.menu{display:flex;gap:15px;align-items:center;flex-wrap:wrap}
.menu a{font-size:.87rem;font-weight:600;color:var(--ink);text-decoration:none}
@media (max-width:1180px) and (min-width:921px){.logo span{display:none}.menu{gap:12px}.menu a{font-size:.84rem}}
.menu a:hover,.menu a.on{color:var(--wine)}
.menu .cta{padding:10px 18px;border-radius:5px;background:var(--wine);color:#FAF5F0}
.menu .cta:hover{background:var(--wine-deep);color:#FAF5F0}
#mtoggle{display:none}
.burger{display:none;cursor:pointer;padding:8px;margin-left:auto}
.burger span{display:block;width:22px;height:2px;background:var(--ink);margin:5px 0}
@media (max-width:920px){
  .burger{display:block}
  .logo{margin-right:0}
  .nav .wrap{flex-wrap:wrap;gap:8px}
  .menu{display:none;width:100%;flex-direction:column;align-items:flex-start;gap:4px;padding:10px 0 14px}
  .menu a{padding:9px 0;font-size:1rem}
  #mtoggle:checked ~ .menu{display:flex}
}

/* Хиро */
.hero{position:relative;background:var(--night);color:var(--ntext)}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.48}
.hero .veil{position:absolute;inset:0;background:linear-gradient(165deg,rgba(23,34,44,.5),rgba(23,34,44,.93) 80%)}
.hero .in{position:relative;z-index:1;max-width:860px;margin:0 auto;padding:110px 24px 92px}
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

MENU = [
    ("/chizhovy2/metod/", "Метод"),
    ("/chizhovy2/programma/", "Программа"),
    ("/chizhovy2/para/", "Для пар"),
    ("/chizhovy2/vedushchie/", "Ведущие"),
    ("/chizhovy2/istoki/", "Истоки"),
    ("/chizhovy2/istorii/", "Истории"),
    ("/chizhovy2/stati/", "Статьи"),
    ("/chizhovy2/voprosy/", "Вопросы"),
    ("/chizhovy2/gid/", "Гайд"),
]

def nav(active=""):
    items = "".join(
        f'<a href="{u}"{" class=\"on\"" if u.strip("/").endswith(active) and active else ""}>{t}</a>'
        for u, t in MENU)
    return f"""<nav class="nav"><div class="wrap">
<a class="logo" href="/chizhovy2/">{LOGO_SVG}<div><b>Настоящие отношения</b><span>Школа Алексея и&nbsp;Ирины Чижовых</span></div></a>
<label class="burger" for="mtoggle" aria-label="Меню"><span></span><span></span><span></span></label>
<input type="checkbox" id="mtoggle">
<div class="menu">{items}<a class="cta" href="/chizhovy2/sessiya/">Собеседование</a></div>
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

def page(title, desc, active, body):
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
{FOOTER}
<script>
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
"Очный тренинг и три месяца сопровождения: выход из повторяющихся сценариев в отношениях, деле и состоянии.", "", f"""
<div class="hero"><div class="bg" style="background-image:url('/chizhovy2/images/site-hero.png')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Школа трансформации Алексея и&nbsp;Ирины Чижовых</p>
<h1>Перепиши сценарий своей жизни</h1>
<p class="lead">Очный тренинг и&nbsp;три месяца сопровождения. Выходишь из&nbsp;повторяющихся кругов и&nbsp;начинаешь строить отношения, дело и&nbsp;себя из&nbsp;осознанного&nbsp;выбора.</p>
<div class="acts"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a><a class="btn btn-ghost" href="/chizhovy2/gid/">Скачать гайд бесплатно</a></div>
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
<h2>Узнаёшь себя хотя&nbsp;бы в&nbsp;одном</h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><span class="bignum">01</span>{icon('book')}<h3>Всё понимаешь, а&nbsp;не&nbsp;меняется</h3><p>Книги прочитаны, курсы пройдены, выводы сделаны. Реакции те&nbsp;же, что пять лет назад.</p></div>
<div class="card"><span class="bignum">02</span>{icon('loop','var(--sage-deep)')}<h3>Сценарии повторяются</h3><p>Разные люди, разные обстоятельства, финал одинаковый. В&nbsp;отношениях, в&nbsp;деньгах, в&nbsp;теле.</p></div>
<div class="card"><span class="bignum">03</span>{icon('shield','var(--sand)')}<h3>Сильный снаружи, устал внутри</h3><p>Бизнес, семья, статус, всё по&nbsp;списку. И&nbsp;усталость, о&nbsp;которой некому&nbsp;рассказать.</p></div>
<div class="card"><span class="bignum">04</span>{icon('cups','var(--sage-deep)')}<h3>Близость ушла в&nbsp;быт</h3><p>Календарь общий, разговоры про логистику. Не&nbsp;ссоритесь, потому что&nbsp;незачем.</p></div>
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
<p>Разорвать круг усилием не&nbsp;выходит. Мы&nbsp;разбираем его там, где он&nbsp;записан: в&nbsp;эмоции и&nbsp;теле, в&nbsp;живой групповой&nbsp;работе.</p>
<p style="margin-top:24px"><a class="btn btn-ghost" href="/chizhovy2/metod/">Разобрать метод подробно</a></p>
</div>
<div>{loop_diagram(dark=True)}</div>
</div>
</div></section>

<section style="padding-bottom:0"><div class="wrap">
<p class="eyebrow">Работаем по&nbsp;всей жизни</p>
<h2>Четыре сферы, один сдвиг</h2>
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
<div class="gap">3-5 недель интеграции</div>
<div class="tm"><div class="c">II</div><div><b>Внутренняя свобода</b><span>5 дней очно</span></div></div>
<div class="gap">3-5 недель интеграции</div>
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
<h2>Что становится возможным</h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><span class="bignum">01</span>{icon('ceiling')}<h3>Дело выходит из&nbsp;потолка</h3><p>Видишь, что именно держало обороты и&nbsp;заставляло цепляться за&nbsp;«стабильный» заработок. Убираешь причину, не&nbsp;симптом.</p></div>
<div class="card"><span class="bignum">02</span>{icon('route','var(--sage-deep)')}<h3>Ясность про себя</h3><p>Кто я, куда бегу, почему всё повторяется по&nbsp;спирали. Видишь свои сильные стороны и&nbsp;путь к&nbsp;целям.</p></div>
<div class="card"><span class="bignum">03</span>{icon('lens','var(--sand)')}<h3>Крепкие отношения</h3><p>Выходишь из&nbsp;разрушающих связей и&nbsp;затяжных конфликтов, налаживаешь отношения с&nbsp;близкими.</p></div>
<div class="card"><span class="bignum">04</span>{icon('mountain','var(--sage-deep)')}<h3>Спокойствие и&nbsp;уверенность</h3><p>Внутренняя опора вместо выдержки на&nbsp;зубах. Острые моменты перестают выбивать из&nbsp;седла.</p></div>
<div class="card"><span class="bignum">05</span>{icon('people','var(--sand)')}<h3>Своё окружение</h3><p>Люди, с&nbsp;которыми можно в&nbsp;разведку и&nbsp;в&nbsp;дело. Навык слышать, договариваться, играть вместе.</p></div>
<div class="card"><span class="bignum">06</span>{icon('sunrise')}<h3>От понимания к&nbsp;действию</h3><p>Перестаёшь откладывать жизнь на&nbsp;потом. Путь от&nbsp;идеи до&nbsp;реализации сокращается в&nbsp;разы.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Как это выглядит</p>
<h2>Наши группы, без стоковых улыбок</h2>
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
<h2>Двое, у&nbsp;которых совпадают&nbsp;слова&nbsp;и&nbsp;жизнь</h2>
<p>Алексей: коуч с&nbsp;сертификацией ICF, 16&nbsp;лет в&nbsp;трансформационной практике, триатлет. Ирина: трансформационный тренер, шесть лет готовилась к&nbsp;этому формату, работает на&nbsp;глубине, которую участники вспоминают&nbsp;годами.</p>
<p>Вместе 17&nbsp;лет. Школу отношений ведёт пара, у&nbsp;которой отношения живые: с&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них.</p>
<p style="margin-top:20px"><a class="btn btn-ghost" href="/chizhovy2/vedushchie/">Познакомиться</a></p>
</div>
<div class="ph"><img src="/chizhovy2/images/real/portret.jpg" alt="Алексей и Ирина Чижовы, портрет" loading="lazy"></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Истоки метода</p>
<h2>Метод с&nbsp;открытыми истоками</h2>
<p>Сильной работе нечего прятать. Мы&nbsp;открыто называем школы и&nbsp;авторов, на&nbsp;которых выросли: психодрама Морено, трансерфинг Зеланда, тренинги погружения от&nbsp;est, практика состояния Годдарда. И&nbsp;показываем, что взяли, что переработали за&nbsp;16&nbsp;лет и&nbsp;почему это работает с&nbsp;точки зрения науки.</p>
<p style="margin-top:20px"><a class="btn btn-ghost" href="/chizhovy2/istoki/">Разобрать истоки</a></p>
</div>
<div class="linklist">
<a href="/chizhovy2/istoki/moreno-psihodrama/">{ICONS['people']}<div><b>Якоб Морено и&nbsp;психодрама</b><span>живая сцена вместо разговоров о&nbsp;жизни</span></div></a>
<a href="/chizhovy2/istoki/zeland-transerfing/">{ICONS['loop']}<div><b>Вадим Зеланд и&nbsp;трансерфинг</b><span>маятники, важность, зеркало мира</span></div></a>
<a href="/chizhovy2/istoki/est-transformaciya/">{ICONS['flame']}<div><b>est и&nbsp;«Трансформация» Рейнхарта</b><span>откуда пошли тренинги погружения</span></div></a>
<a href="/chizhovy2/istoki/goddard/">{ICONS['sunrise']}<div><b>Невилл Годдард</b><span>состояние уже сбывшегося</span></div></a>
<a href="/chizhovy2/istoki/nauka/">{ICONS['book']}<div><b>Наука за&nbsp;методом</b><span>ЛеДу, Гоулман, Болте&nbsp;Тейлор,&nbsp;Голвитцер</span></div></a>
</div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="poster"><div class="bg" style="background-image:url('/chizhovy2/images/site-dark.png')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Ближайшее погружение</p>
<h3>Модуль II. Внутренняя&nbsp;свобода</h3>
<p>Пять дней, после которых страх, вина и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p>
<p style="margin-top:24px"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Занять место</a></p>
</div></div>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Начни с&nbsp;часа разговора</h2>
<p class="sub" style="margin:0 auto 26px">Собеседование в&nbsp;школу: час о&nbsp;твоей ситуации и&nbsp;честный ответ, чем школа может помочь. Для читателей сайта&nbsp;бесплатно.</p>
<a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a>
</div></section>
""")

# ================= МЕТОД =================
P["metod/index.html"] = ("Метод школы · Настоящие отношения",
"Событийный круг, состояние и психодрама: подробный разбор, как устроена перезапись сценариев.", "metod", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-metod.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Метод школы</p><h1>Жизнь слушается состояния</h1>
<p class="lead">Мы&nbsp;не&nbsp;учим «правильно общаться» и&nbsp;не&nbsp;выдаём мотивацию на&nbsp;неделю. Мы&nbsp;находим запись, которая пишет твои реакции, и&nbsp;помогаем переписать её&nbsp;там, где она хранится. Ниже метод разобран по&nbsp;винтикам.</p>
<div class="acts"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a><a class="btn btn-ghost" href="/chizhovy2/vedushchie/">Кто ведёт</a></div>
</div></div>

<section><div class="narrow">
<p class="eyebrow">Главная идея</p>
<h2>Муравей и&nbsp;слон</h2>
<p>Разум мал и&nbsp;суетлив, как муравей. Состояние огромно, как слон. Пока слон лежит или идёт в&nbsp;другую сторону, муравей может тащить план куда угодно: масса не&nbsp;та. Поэтому решения «с&nbsp;понедельника» держатся до&nbsp;первого настоящего стресса, а&nbsp;цели из&nbsp;ежедневника не&nbsp;доходят до&nbsp;жизни.</p>
<p>Управлять получается наоборот: сначала состояние, потом действия. Меняется состояние, меняются решения. Меняются решения, меняется жизнь. Ученики после тренинга говорят об&nbsp;этом коротко: мир зеркалит состояние.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:26px">
<div class="nail"><b>95%</b><span>дня человек живёт на&nbsp;автопилоте привычных&nbsp;реакций</span></div>
<div class="nail"><b>12&nbsp;мс</b><span>фора эмоционального мозга перед&nbsp;думающим (ЛеДу)</span></div>
<div class="nail"><b>90&nbsp;сек</b><span>живёт химия эмоции, если&nbsp;её&nbsp;не&nbsp;кормить (Болте&nbsp;Тейлор)</span></div>
</div></div></section>

<section class="dark"><div class="wrap">
<div class="diagrow">
<div>{loop_diagram(dark=True)}</div>
<div>
<p class="eyebrow">Механика повтора</p>
<h2>Событийный круг</h2>
<div class="legend" style="margin-top:8px">
<div class="li"><i>1</i><div><b>Событие</b><span>Что-то происходит: слово, взгляд, сумма на&nbsp;счёте. Само по&nbsp;себе оно нейтрально.</span></div></div>
<div class="li"><i>2</i><div><b>Эмоция</b><span>Реакция тела опережает мысль: аварийный центр мозга получает сигнал за&nbsp;миллисекунды до&nbsp;осмысления.</span></div></div>
<div class="li"><i>3</i><div><b>Старое решение</b><span>«Злиться опасно», «просить стыдно», «я&nbsp;сам». Принято в&nbsp;детстве, работает во&nbsp;взрослой жизни.</span></div></div>
<div class="li"><i>4</i><div><b>Сценарий</b><span>Поведение идёт по&nbsp;записи, финал тот&nbsp;же, что в&nbsp;прошлый раз. Круг замыкается и&nbsp;укрепляется.</span></div></div>
</div>
<p style="margin-top:18px">Разорвать круг усилием не&nbsp;выходит: он&nbsp;быстрее сознания. Его размыкают в&nbsp;точке 3, там, где живёт старое решение.</p>
</div>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">Почему разговоры не&nbsp;берут</p>
<h2>Запись хранится ниже слов</h2>
<p>Книги, курсы и&nbsp;беседы стучатся в&nbsp;думающий этаж. Запись лежит этажом ниже: в&nbsp;эмоции и&nbsp;теле. Договариваться с&nbsp;ней словами&nbsp;то&nbsp;же самое, что уговаривать плёнку звучать иначе.</p>
{floors}
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Инструмент №1</p>
<h2>Психодрама: перезапись в&nbsp;живой сцене</h2>
<p class="sub">Метод психиатра Якоба Морено, сто лет практики по&nbsp;всему миру. Человек не&nbsp;рассказывает о&nbsp;ситуации, а&nbsp;возвращается в&nbsp;неё&nbsp;и&nbsp;меняет решение прямо внутри сцены.</p>
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
<div class="card"><span class="bignum">3</span><h3>Проживание</h3><p>Говоришь из&nbsp;себя настоящего то, что тогда осталось несказанным. Тело включается раньше слов, и&nbsp;это&nbsp;правильно.</p></div>
<div class="card"><span class="bignum">4</span><h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место другого: отца, партнёра, себя-ребёнка. Сцена, которую ты&nbsp;носил годами, впервые видна целиком.</p></div>
<div class="card"><span class="bignum">5</span><h3>Новое решение</h3><p>Прямо в&nbsp;сцене принимаешь другое решение. Теперь оно записано так&nbsp;же глубоко, как старое: телом и&nbsp;эмоцией.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Пустой стул</p>
<h2>Разговор, который ты&nbsp;откладывал годами</h2>
<p>Иногда сцена строится вокруг пустого стула. На&nbsp;нём сидит тот, с&nbsp;кем разговор так и&nbsp;не&nbsp;случился: отец, бывший, ты&nbsp;сам из&nbsp;прошлого. Разговор происходит сейчас, и&nbsp;тело отпускает то, что держало.</p>
<p>После таких процессов участники говорят: «снял рюкзак», «стало легче дышать». Это не&nbsp;образы, это буквальные ощущения: напряжение, которое тело держало годами, находит выход.</p>
</div>
<div class="ph"><img src="/chizhovy2/images/metod-stul.png" alt="Пустой стул в луче тёплого света" loading="lazy"></div>
</div>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Вокруг сцены</p>
<h2>Что ещё работает на&nbsp;перезапись</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('flame','var(--copper)')}<h3>Работа с&nbsp;телом</h3><p>Запись живёт в&nbsp;мышцах и&nbsp;дыхании. Телесные практики достают её&nbsp;там, куда слова не&nbsp;доходят, и&nbsp;учат выходить из&nbsp;захвата за&nbsp;те&nbsp;самые 90&nbsp;секунд.</p></div>
<div class="card">{icon('gear','var(--copper)')}<h3>Разбор вины и&nbsp;ответственности</h3><p>Вина сливает энергию и&nbsp;зовёт наказание. Ответственность возвращает силу. Разницу учимся чувствовать телом, а&nbsp;не&nbsp;запоминать&nbsp;словами.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Группа как зеркало</h3><p>10-20 человек, у&nbsp;которых те&nbsp;же боли под другими фамилиями. В&nbsp;чужой сцене узнаёшь свою запись быстрее, чем в&nbsp;своей.</p></div>
<div class="card">{icon('sunrise','var(--copper)')}<h3>Ежедневная практика</h3><p>После модулей: утренний фокус дня и&nbsp;вечерняя ревизия с&nbsp;благодарностями. Девяносто дней Марафона делают новый ответ&nbsp;привычкой.</p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Наука за&nbsp;методом</p>
<h2>Кто это проверил до&nbsp;нас</h2>
<div class="grid2" style="margin-top:26px">
<div class="card white"><h3>Джозеф ЛеДу · нейробиолог</h3><p>Показал «короткий путь» страха: миндалина получает сигнал за&nbsp;12&nbsp;миллисекунд, раньше думающей коры. Вот почему реакция обгоняет&nbsp;намерение.</p></div>
<div class="card white"><h3>Дэниел Гоулман · психолог</h3><p>Описал «захват»: в&nbsp;момент вспышки разумная часть мозга приглушается. «Взять себя в&nbsp;руки» в&nbsp;этот момент физически нечем.</p></div>
<div class="card white"><h3>Джилл Болте Тейлор&nbsp;·&nbsp;нейроанатом</h3><p>Правило 90&nbsp;секунд: химия эмоции сама уходит из&nbsp;крови за&nbsp;полторы минуты, если не&nbsp;подкармливать её&nbsp;мыслями по&nbsp;кругу.</p></div>
<div class="card white"><h3>Якоб Морено · психиатр</h3><p>Создал психодраму и&nbsp;доказал: новый ответ, прожитый в&nbsp;сцене телом и&nbsp;эмоцией, записывается так&nbsp;же глубоко, как детское решение.</p></div>
</div>
<p style="margin-top:18px"><a href="/chizhovy2/istoki/nauka/">Все пять открытий с&nbsp;разбором: наука за&nbsp;методом</a></p>
<div class="pull" style="margin-top:24px"><div class="q">«Труднее всего было принять точку&nbsp;А. Признать, где я&nbsp;на&nbsp;самом деле. Дальше всё началось.»</div><div class="who">Участник тренинга</div></div>
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
<p>Честно: тем, кто ищет волшебную таблетку за&nbsp;вечер. Тем, кто пока не&nbsp;готов работать в&nbsp;группе. И&nbsp;тем, кому сейчас нужна медицинская помощь, а&nbsp;не&nbsp;тренинг: это мы&nbsp;говорим прямо на&nbsp;собеседовании и&nbsp;советуем, куда идти.</p>
<p>Для всех остальных вход один: собеседование. Час честного разговора, где вместе решаем, твой это метод или нет. Для пришедших с&nbsp;сайта бесплатно.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/programma/" style="margin-left:8px">Смотреть программу</a></p>
</div></section>
""")

# ================= ПРОГРАММА =================
P["programma/index.html"] = ("Программа · Настоящие отношения",
"Три модуля школы: Возвращение к себе, Внутренняя свобода, Создатель реальности.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-06.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Программа</p><h1>Путь из&nbsp;трёх модулей</h1>
<p class="lead">Каждый модуль решает свою задачу: увидеть запись, переписать её, закрепить новую жизнь действиями. Между модулями 3-5 недель на&nbsp;интеграцию.</p></div></div>

<section><div class="wrap">
<div class="timeline">{timeline_svg()}</div>
<div class="grid3" style="margin-top:26px">
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/site-m1.png" alt="Модуль I" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль I · 2,5 дня</p><h3>Возвращение к&nbsp;себе</h3><p>Видишь свои повторяющиеся паттерны, установки и&nbsp;их&nbsp;источники. Результат: осознанность и&nbsp;первый честный контакт с&nbsp;собой.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-1/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-07.jpg" alt="Модуль II" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль II · 5 дней</p><h3>Внутренняя свобода</h3><p>Глубокая работа с&nbsp;состояниями: страх, вина, обида, зависимость от&nbsp;чужого мнения. Результат: сила, спокойствие, ясность.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-2/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-13.jpg" alt="Модуль III" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль III · 3 месяца</p><h3>Создатель реальности</h3><p>Интеграция в&nbsp;жизнь: видение, команда, ежедневная практика, результаты в&nbsp;деле и&nbsp;отношениях. Это и&nbsp;есть Марафон.</p><p style="margin-top:12px"><a href="/chizhovy2/marafon/">Подробнее</a></p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Как устроено участие</h2>
<div class="card white" style="margin-top:20px">{icon('speech')}<h3>Начало:&nbsp;собеседование</h3><p>Час разговора о&nbsp;твоей ситуации. Честно решаем, подходит&nbsp;ли тебе школа. Для пришедших с&nbsp;этого сайта собеседование бесплатное.</p></div>
<div class="card white" style="margin-top:12px">{icon('people','var(--sage-deep)')}<h3>Формат</h3><p>Очные модули в&nbsp;Москве малой группой 10-20 человек, между модулями 3-5 недель с&nbsp;поддержкой, после третьего модуля три месяца сопровождения.</p></div>
<div class="card white" style="margin-top:12px">{icon('target','var(--sand)')}<h3>Для кого</h3><p>Для взрослых людей, готовых брать ответственность: предприниматели, руководители, пары. Мы&nbsp;отбираем участников на&nbsp;собеседовании, потому что глубина требует готовности.</p></div>
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
<div class="card white" style="margin:18px 0 12px">{icon('book')}<h3>Видишь свои паттерны</h3><p>Повторяющиеся реакции, роли и&nbsp;установки, из&nbsp;которых соткан твой день: где ты&nbsp;терпишь, где убегаешь, где стараешься казаться.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('route','var(--sage-deep)')}<h3>Находишь источники</h3><p>В&nbsp;живых процессах видно, где было принято старое решение и&nbsp;чью интонацию ты&nbsp;до&nbsp;сих пор носишь как&nbsp;свою.</p></div>
<div class="card white">{icon('lens','var(--sand)')}<h3>Возвращаешь контакт с&nbsp;собой</h3><p>К&nbsp;воскресному вечеру появляется то, что участники называют «впервые за&nbsp;годы услышал себя». Отсюда начинается настоящая работа.</p></div>
<div class="pull"><div class="q">«Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка колоссальная.»</div><div class="who">Участник первого модуля</div></div>
<p><strong>Результат модуля: осознанность.</strong> Ты&nbsp;видишь свою запись. Развидеть её&nbsp;уже не&nbsp;получится, и&nbsp;это лучшее, что могло&nbsp;случиться.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Начать с&nbsp;собеседования</a> <a class="btn btn-ghost" href="/chizhovy2/modul-2/" style="margin-left:8px">Дальше: Модуль II</a></p>
</div></section>
""")

# ================= МОДУЛЬ 2 =================
P["modul-2/index.html"] = ("Модуль II. Внутренняя свобода · Настоящие отношения",
"Пять дней глубокой работы: страх, вина, обида, внутренняя опора.", "modul-2", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-dark.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль II · пять дней</p><h1>Внутренняя свобода</h1>
<p class="lead">Самый глубокий модуль школы. Пять дней, после которых страх, вина и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p></div></div>

<section><div class="narrow">
<h2>С чем работаем</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('flame')}<h3>Страх и&nbsp;важность</h3><p>Разбираем, как раздутая ставка парализует действия, и&nbsp;возвращаем способность решать спокойно.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Вина и&nbsp;ответственность</h3><p>Вина сливает энергию и&nbsp;притягивает наказание. Ответственность возвращает силу. Учимся различать их&nbsp;телом.</p></div>
<div class="card">{icon('loop','var(--sand)')}<h3>Обида</h3><p>Старые обиды держат сценарии годами. Проживаем их&nbsp;до&nbsp;конца в&nbsp;безопасном пространстве группы.</p></div>
<div class="card">{icon('mountain')}<h3>Внутренняя опора</h3><p>Собираем состояние, в&nbsp;котором ты&nbsp;не&nbsp;зависишь от&nbsp;оценки, настроения партнёра и&nbsp;погоды на&nbsp;рынке.</p></div>
</div>
<div class="pull"><div class="q">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше.»</div><div class="who">Участник второго модуля</div></div>
<p><strong>Результат модуля: сила, спокойствие, ясность.</strong> Плюс инструменты, которыми ты&nbsp;дальше пользуешься сам: тело помнит, как выходить из&nbsp;захвата.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Занять место</a> <a class="btn btn-ghost" href="/chizhovy2/marafon/" style="margin-left:8px">Дальше: Марафон</a></p>
</div></section>
""")

# ================= МАРАФОН =================
P["marafon/index.html"] = ("Модуль III. Создатель реальности · Настоящие отношения",
"Три месяца практики в жизни: команда, еженедельные встречи, результаты, которые остаются.", "marafon", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-10.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль III · три месяца</p><h1>Создатель реальности</h1>
<p class="lead">Инсайты выветриваются за&nbsp;две недели, если их&nbsp;не&nbsp;закрепить действиями. Марафон существует ровно для этого: три месяца новая жизнь тренируется в&nbsp;настоящей.</p></div></div>

<section><div class="narrow">
<h2>Как устроены три месяца</h2>
<div class="card white" style="margin:20px 0 12px">{icon('people')}<h3>Команда</h3><p>Ты&nbsp;идёшь не&nbsp;один: группа становится командой с&nbsp;общей целью и&nbsp;напарником у&nbsp;каждого. Поддержка работает даже в&nbsp;два часа ночи.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('speech','var(--sage-deep)')}<h3>Еженедельные встречи</h3><p>Разборы с&nbsp;Алексеем и&nbsp;Ириной: что получилось, где старая запись взяла своё, какой следующий шаг.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('sunrise','var(--sand)')}<h3>Ежедневная практика</h3><p>Утром формулируешь главный фокус дня, вечером подводишь итог: открытия и&nbsp;благодарности. Простая дисциплина, которая за&nbsp;90&nbsp;дней перепрошивает привычный способ&nbsp;жить.</p></div>
<div class="card white">{icon('target')}<h3>Реальные цели</h3><p>Работа идёт на&nbsp;твоих живых задачах: дело, деньги, отношения, тело. Результат меряем фактами, не&nbsp;ощущениями.</p></div>

<div class="pull"><div class="q">«Раньше я&nbsp;отсеивал людей по&nbsp;уровню жизни. Сейчас просто строю настоящие отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами.»</div><div class="who">Выпускник Марафона, предприниматель</div></div>
<p><strong>Результат: новые действия и&nbsp;новые результаты.</strong> Не&nbsp;состояние после тренинга, а&nbsp;жизнь, которая продолжает расти,&nbsp;когда сопровождение закончилось.</p>
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
<div class="in"><p class="eyebrow">Для пар</p><h1>Когда проходят вдвоём, меняется сама пара</h1>
<p class="lead">Можно годами носить с&nbsp;тренингов инсайты в&nbsp;дом, где тебя ждёт прежний человек. А&nbsp;можно прийти вдвоём и&nbsp;переписать общий сценарий с&nbsp;двух сторон сразу.</p></div></div>

<section><div class="narrow">
<h2>Что происходит с&nbsp;парой</h2>
<p>У&nbsp;пары всегда два сценария, и&nbsp;они цепляются друг за&nbsp;друга, как шестерёнки: её&nbsp;обида включает его&nbsp;молчание, его&nbsp;молчание кормит её&nbsp;обиду. На&nbsp;тренинге каждый работает со&nbsp;своей записью, и&nbsp;шестерёнки&nbsp;расцепляются.</p>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('mountain')}<h3>Он</h3><p>Возвращает опору и&nbsp;уверенность: решения из&nbsp;спокойствия, дело и&nbsp;достаток растут без надрыва.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Она</h3><p>Возвращает себя: раскрывается, вдохновляет, перестаёт жить в&nbsp;режиме ожидания и&nbsp;обслуживания.</p></div>
</div>
<p style="margin-top:24px">Дальше начинается то, ради чего школа носит своё имя: <strong>настоящие отношения.</strong> Разговоры, которые заканчиваются ближе, чем начинались. Быт, в&nbsp;котором снова видно человека. Общие цели вместо параллельных жизней.</p>
<p>Пары на&nbsp;группе работают наравне со&nbsp;всеми: часть процессов вместе, часть по&nbsp;отдельности. Прийти одному тоже можно: отношения меняются, даже когда запись переписывает один из&nbsp;двоих.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться вдвоём</a></p>
</div></section>
""")

# ================= ВЕДУЩИЕ =================
P["vedushchie/index.html"] = ("Алексей и Ирина Чижовы · Настоящие отношения",
"Ведущие школы: коуч ICF и трансформационный тренер, вместе 17 лет.", "vedushchie", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/portret.jpg');background-position:center 25%"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Ведущие</p><h1>Алексей и&nbsp;Ирина Чижовы</h1>
<p class="lead">Школу отношений ведёт пара, которая 17&nbsp;лет строит свои. С&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них, поэтому в&nbsp;зале нет теории с&nbsp;чужих&nbsp;слов.</p></div></div>

<section><div class="narrow">
<div class="grid2">
<div class="card white">{icon('mountain')}<h3>Алексей</h3><p>Коуч с&nbsp;сертификацией ICF, 16&nbsp;лет в&nbsp;трансформационной практике. Держит структуру и&nbsp;точность процесса: с&nbsp;ним безопасно идти в&nbsp;глубину, потому что он&nbsp;видит дорогу&nbsp;целиком.</p></div>
<div class="card white">{icon('flame','var(--sand)')}<h3>Ирина</h3><p>Трансформационный тренер. Шесть лет готовилась к&nbsp;этому формату под руководством наставника. Работает на&nbsp;глубине: участники говорят, что она «вскрывает и&nbsp;собирает», и&nbsp;вспоминают её&nbsp;работу годами.</p></div>
</div>
<p style="margin-top:26px">Роли в&nbsp;зале дополняют друг друга: его&nbsp;опора и&nbsp;её&nbsp;чувствование, структура и&nbsp;глубина. Те&nbsp;же два начала, что мы&nbsp;помогаем соединить каждому&nbsp;участнику.</p>
<div class="pull"><div class="q">«У&nbsp;нас не&nbsp;было идеальной истории. Было непонимание, ошибки, потери, моменты, где казалось: дальше некуда. Именно там началось настоящее.»</div><div class="who">Из обращения Алексея и&nbsp;Ирины к&nbsp;каналу школы</div></div>
<p>Поэтому здесь не&nbsp;учат жить и&nbsp;не&nbsp;мотивируют. Здесь разбираются вместе: почему ты&nbsp;реагируешь так, как реагируешь, и&nbsp;почему в&nbsp;отношениях повторяется одно и&nbsp;то&nbsp;же. Иногда будет непросто. Иногда очень точно. Но&nbsp;всегда&nbsp;по-настоящему.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/real/zabeg-selfi.jpg" alt="Алексей и Ирина на набережной после старта" loading="lazy"></div>
<div>
<p class="eyebrow">Дисциплина как часть метода</p>
<h2>Слова, за&nbsp;которыми стоит тело</h2>
<p>Алексей: триатлет, финишер IronMan&nbsp;70.3. Не&nbsp;ради медалей: длинная дистанция каждый день проверяет то, чему школа учит в&nbsp;зале. Состояние первично, решения из&nbsp;спокойствия, играть в&nbsp;долгую.</p>
<p>Команды школы выходят на&nbsp;забеги вместе: тело быстро выдаёт, где ты&nbsp;себя обманываешь, и&nbsp;честно радуется, когда ты&nbsp;настоящий.</p>
</div>
</div>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Познакомиться лично</h2>
<p class="sub" style="margin:0 auto 26px">Собеседование: час разговора о&nbsp;твоей ситуации, честный взгляд со&nbsp;стороны и&nbsp;понятный следующий шаг. Для читателей сайта бесплатно.</p>
<a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться</a>
</div></section>
""")

# ================= ОТЗЫВЫ =================
P["otzyvy/index.html"] = ("Истории учеников · Настоящие отношения",
"Живые истории выпускников школы: до, во время и после тренинга.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-05.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истории учеников</p><h1>Их словами, без глянца</h1>
<p class="lead">Мы&nbsp;не&nbsp;переписываем отзывы под рекламу. Ниже живые фрагменты историй с&nbsp;согласия авторов. Каждая история личная, результат у&nbsp;каждого свой.</p></div></div>

<section><div class="narrow">
<!-- ПРОТОТИП: подписи и полные версии согласовать с авторами перед публикацией -->
<div class="card white" style="margin-bottom:16px">
<p class="eyebrow" style="margin-bottom:10px">Предприниматель, пришёл в&nbsp;кризис</p>
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
<p style="margin-bottom:0">«Полгода не&nbsp;могла решиться на&nbsp;поездку, даже паспорт найти не&nbsp;могла. После работы в&nbsp;группе просто приняла решение внутри, и&nbsp;всё сложилось за&nbsp;день. Мелочь? Для&nbsp;меня это была первая за&nbsp;годы вещь, сделанная для&nbsp;себя».</p>
</div>

<p style="margin-bottom:22px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Полные истории: с&nbsp;точкой&nbsp;А и&nbsp;переломом</a></p>
<div class="pull"><div class="q">«Моя жизнь точно разделена на&nbsp;до&nbsp;и&nbsp;после.»</div><div class="who">Участница школы</div></div>
<div class="pull"><div class="q">«Спасибо, что помогли прожить стену, которую я&nbsp;так долго строил. Теперь она мне не&nbsp;нужна.»</div><div class="who">Участник школы</div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-03.jpg" alt="Группа выпуска" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-09.jpg" alt="Участники тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
</div>
<p style="margin-top:30px;text-align:center"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Начать свою историю</a></p>
</div></section>
""")

# ================= ВОПРОСЫ =================
P["voprosy/index.html"] = ("Вопросы и ответы · Настоящие отношения",
"Честные ответы: формат, глубина, группа, условия участия.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Вопросы и&nbsp;ответы</p><h1>Спрашивают перед стартом</h1>
<p class="lead">Собрали то, что чаще всего звучит на&nbsp;собеседованиях. Если своего вопроса не&nbsp;нашёл, задай его лично: контакты внизу.</p></div></div>

<section><div class="narrow">
<details><summary>На чём основан метод?</summary><p>На&nbsp;практической психологии: психодрама Якоба Морено, работа с&nbsp;состоянием и&nbsp;групповые процессы, проверенные за&nbsp;16&nbsp;лет практики. Глубину даём через живой опыт, объясняем через понятные механизмы работы мозга и&nbsp;тела. Все опоры метода мы&nbsp;показываем открыто: <a href="/chizhovy2/istoki/">раздел «Истоки»</a>.</p></details>
<details><summary>Я уже ходил к&nbsp;психологу. Чем это отличается?</summary><p>Личная терапия работает словами и&nbsp;по&nbsp;часу в&nbsp;неделю. Здесь работа идёт в&nbsp;живых сценах, телом и&nbsp;эмоцией, в&nbsp;погружении на&nbsp;несколько дней. Это разные инструменты, и&nbsp;они хорошо дополняют друг друга.</p></details>
<details><summary>Боюсь групповой работы. Придётся раскрываться перед&nbsp;чужими?</summary><p>Глубина всегда добровольна: никто не&nbsp;вытаскивает силой. Обычно уже к&nbsp;вечеру первого дня группа перестаёт быть чужой: у&nbsp;людей одинаковые боли, и&nbsp;в&nbsp;чужой истории ты&nbsp;узнаёшь свою.</p></details>
<details><summary>Можно прийти одному, без&nbsp;партнёра?</summary><p>Да. Большинство участников приходят по&nbsp;одному. Отношения меняются, даже когда работает один из&nbsp;двоих: твоя половина общего сценария в&nbsp;твоих руках.</p></details>
<details><summary>Сколько времени занимает программа?</summary><p>Модуль I: два с&nbsp;половиной дня (пятничный вечер плюс выходные). Модуль II: пять дней. Модуль III: три месяца сопровождения при обычной жизни. Между модулями 3-5 недель.</p></details>
<details><summary>Что за собеседование и&nbsp;сколько оно стоит?</summary><p>Час личного разговора о&nbsp;твоей ситуации. Для тех, кто пришёл с&nbsp;этого сайта, собеседование бесплатное. По&nbsp;итогам обе стороны честно решают, идти&nbsp;ли дальше; условия модулей обсуждаются там&nbsp;же.</p></details>
<details><summary>Какие гарантии?</summary><p>Честная: метод работает, когда работаешь ты. Мы&nbsp;даём процесс, группу, сопровождение и&nbsp;16&nbsp;лет опыта. Результат складывается из&nbsp;этого и&nbsp;твоих действий, поэтому у&nbsp;каждого он&nbsp;свой.</p></details>
<details><summary>Как попасть на тренинг?</summary><p>Школа растёт через рекомендации, без массовой рекламы. Первый шаг один для всех: собеседование. Запись через Telegram, кнопка ниже.</p></details>
<p style="margin-top:28px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a></p>
</div></section>
""")

# ================= СЕССИЯ =================
P["sessiya/index.html"] = ("Собеседование · Настоящие отношения",
"Собеседование в школу: час о твоей ситуации, честный взгляд, понятный шаг. Бесплатно с сайта.", "sessiya", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-sessiya.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Первый шаг</p><h1>Собеседование в&nbsp;школу</h1>
<p class="lead">Час живого разговора о&nbsp;твоей ситуации. Не&nbsp;продажа и&nbsp;не&nbsp;диагностика по&nbsp;чек-листу: знакомимся и&nbsp;вместе решаем, по&nbsp;пути&nbsp;ли нам.</p></div></div>

<section><div class="narrow">
<h2>Как проходит</h2>
<div class="card white" style="margin:20px 0 12px">{icon('speech')}<h3>Ты рассказываешь</h3><p>Что происходит и&nbsp;что уже пробовал. Без подготовки и&nbsp;правильных слов: как есть.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('gear','var(--sage-deep)')}<h3>Разбираем механику</h3><p>Где в&nbsp;твоей истории крутится сценарий и&nbsp;что его держит. Обычно уже этот час даёт первое «вот оно что».</p></div>
<div class="card white">{icon('route','var(--sand)')}<h3>Вы решаете, что дальше</h3><p>Подходит&nbsp;ли тебе школа, с&nbsp;какого модуля заходить, и&nbsp;стоит&nbsp;ли вообще. Отговорить можем так&nbsp;же честно, как&nbsp;пригласить.</p></div>

<div class="nails nails2" style="margin-top:28px">
<div class="nail"><b>60&nbsp;минут</b><span>личного разговора, онлайн или очно</span></div>
<div class="nail"><b>Бесплатно</b><span>для тех, кто пришёл с&nbsp;этого сайта. Условия модулей обсуждаются лично</span></div>
</div>

<div style="background:var(--linen);border:1px solid var(--line);border-radius:10px;padding:34px;margin-top:30px;text-align:center">
<h3 style="font-size:1.4rem">Записаться</h3>
<p class="sub" style="margin:8px auto 22px">Напиши слово «собеседование» в&nbsp;наш Telegram. Ответим лично, без ботов и&nbsp;рассылок.</p>
<a class="btn btn-wine" href="https://t.me/+LVptSH6Mt4hhYmFi">Написать в&nbsp;Telegram</a>
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
<text x="145" y="196">живу состоянием итога</text><text x="450" y="196">решаю и действую иначе</text><text x="755" y="196">события меняются</text>
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
<p class="eyebrow">Дальше по&nbsp;истокам</p>
<div class="chiplist">{links}<a href="/chizhovy2/istoki/">Все истоки</a></div>
</div></section>"""

MOST = """<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Читать полезно. Меняет живая работа</h2>
<p class="sub" style="margin:0 auto 26px">Книги дают карту, а&nbsp;сценарий переписывается в&nbsp;зале, телом и&nbsp;эмоцией. Начни с&nbsp;бесплатного гайда или приходи на&nbsp;собеседование: час разговора о&nbsp;твоей&nbsp;ситуации.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Скачать гайд</a></p>
</div></section>"""

P["istoki/index.html"] = ("Истоки метода · Настоящие отношения",
"Психодрама Морено, трансерфинг Зеланда, est, Годдард и наука: из чего собран метод школы и что мы переработали за 16 лет.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки метода</p><h1>Из чего собран метод</h1>
<p class="lead">Каждая сильная школа стоит на&nbsp;чьих-то плечах. Мы&nbsp;называем свои опоры открыто: вот авторы, у&nbsp;которых мы&nbsp;взяли лучшее, и&nbsp;вот что мы&nbsp;с&nbsp;этим сделали за&nbsp;16&nbsp;лет живой практики.</p></div></div>

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
<h2>Пять притоков, один метод</h2>
<div class="only-d" style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:30px 22px 18px;margin-top:26px">{splav_svg()}</div>
<div class="only-m" style="margin-top:22px">
<div class="chiplist" style="text-align:center"><span>Морено · сцена</span><span>Зеланд · язык</span><span>est · формат</span><span>Годдард · состояние</span><span>Наука · проверка</span></div>
<div style="text-align:center;color:var(--sand);font-size:1.4rem;line-height:1;margin:4px 0 10px">↓</div>
<div class="card white" style="text-align:center"><h3 style="margin-bottom:4px">Метод школы</h3><p>пять притоков, проверено залом: 16&nbsp;лет, сотни историй</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Как мы&nbsp;обращаемся с&nbsp;истоками</h2>
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
<div class="in"><p class="eyebrow">Истоки · Психодрама</p><h1>Сцена, на&nbsp;которой переигрывают жизнь</h1>
<p class="lead">Якоб Леви Морено, венский психиатр, ещё в&nbsp;1921&nbsp;году заметил: человек меняется на&nbsp;сцене быстрее, чем в&nbsp;кресле напротив врача. Так родилась психодрама, академическое ядро нашего&nbsp;метода.</p></div></div>

<section><div class="narrow">
<h2>Что придумал Морено</h2>
<p>Морено (1889-1974) начинал с&nbsp;«театра спонтанности» в&nbsp;Вене: обычные люди разыгрывали на&nbsp;сцене не&nbsp;пьесы, а&nbsp;собственные истории. Он&nbsp;увидел, что в&nbsp;такой игре человек внезапно выходит из&nbsp;заученной роли и&nbsp;находит новый ответ на&nbsp;старую ситуацию. Позже, уже в&nbsp;Америке, он&nbsp;превратил это наблюдение в&nbsp;метод, которым сегодня работают в&nbsp;десятках стран.</p>
<p>Главная ставка здесь простая: о&nbsp;проблеме бесполезно рассказывать, в&nbsp;неё нужно вернуться. Участники группы становятся героями твоей истории, пространство зала превращается в&nbsp;ту&nbsp;кухню или тот кабинет, и&nbsp;сцена&nbsp;оживает.</p>
</div>
<div class="wrap"><div class="grid3" style="margin-top:26px">
<div class="card"><h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место отца, партнёра, начальника и&nbsp;отвечаешь себе его словами. Пять минут в&nbsp;чужой роли дают больше, чем год&nbsp;объяснений.</p></div>
<div class="card"><h3>Дублирование</h3><p>Человек рядом договаривает то, что ты&nbsp;чувствуешь и&nbsp;не&nbsp;решаешься сказать. Невысказанное впервые звучит&nbsp;вслух.</p></div>
<div class="card"><h3>Зеркало</h3><p>Смотришь собственную сцену со&nbsp;стороны, как зритель. Иногда этого достаточно, чтобы увидеть свой сценарий целиком.</p></div>
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
<p><b style="color:#D08A5F">Взяли:</b> сцену как главный инструмент, группу как усилитель, пустой стул, обмен ролями. Разговор, который не&nbsp;случился в&nbsp;жизни, происходит у&nbsp;нас в&nbsp;зале, и&nbsp;тело проживает его по-настоящему.</p>
<p><b style="color:#D08A5F">Переработали:</b> у&nbsp;Морено спонтанность сама по&nbsp;себе считалась лекарством. Мы&nbsp;поставили сцену на&nbsp;карту событийного круга: она ведёт к&nbsp;конкретной точке, к&nbsp;старому решению, и&nbsp;там происходит перезапись. Сцена у&nbsp;нас средство, а&nbsp;целью остаётся новый сценарий в&nbsp;жизни.</p>
<p>Поэтому после сцены работа не&nbsp;заканчивается: решение закрепляется практикой между модулями и&nbsp;тремя месяцами Марафона.</p>
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
<p><b style="color:#D08A5F">Переработали:</b> у&nbsp;Зеланда это философия для самостоятельного чтения, и&nbsp;у&nbsp;неё есть слабое место: прочитал, восхитился, через месяц забыл. Мы&nbsp;дали каждому термину механизм и&nbsp;тренировку. Маятник у&nbsp;нас это твоя знакомая петля реакции, и&nbsp;её видно на&nbsp;событийном круге. Важность это ставка, которая включает страх и&nbsp;сжимает выбор. А&nbsp;держать состояние учит не&nbsp;книга, а&nbsp;девяносто дней практики с&nbsp;командой и&nbsp;разборами.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/goddard/", "Невилл Годдард"), ("/chizhovy2/istoki/est-transformaciya/", "est и «Трансформация»"), ("/chizhovy2/istoki/nauka/", "Наука за методом"))}
{MOST}
""")

P["istoki/est-transformaciya/index.html"] = ("est и «Трансформация» Рейнхарта · Истоки метода",
"Тренинг est Вернера Эрхарда и книга «Трансформация» Люка Рейнхарта: откуда пошёл жанр погружения и что школа сделала иначе.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-est.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · est</p><h1>Два уикенда, с&nbsp;которых начался жанр</h1>
<p class="lead">Сан-Франциско, 1971&nbsp;год. Вернер Эрхард собирает первый тренинг est: два выходных подряд, жёсткие правила зала и&nbsp;сотни тысяч выпускников за&nbsp;тринадцать лет. Так родился жанр тренингов погружения, в&nbsp;котором работает и&nbsp;наша школа.</p></div></div>

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
"Состояние уже сбывшегося: идея Невилла Годдарда, практика намерения на Марафоне и её научный двойник.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-goddard.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Годдард</p><h1>Состояние уже сбывшегося</h1>
<p class="lead">Невилл Годдард, лектор с&nbsp;Барбадоса, полвека собирал залы в&nbsp;Америке с&nbsp;одной темой: события строятся из&nbsp;состояния, в&nbsp;котором ты&nbsp;живёшь. Его идею наши ученики проверяют девяносто дней подряд.</p></div></div>

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
<div class="card" style="background:#6E3B4B;border-color:#6E3B4B"><p style="margin:0;color:#FAF5F0;font-weight:700">живу состоянием итога → решаю и&nbsp;действую иначе → события&nbsp;меняются</p></div>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/zeland-transerfing/", "Зеланд и трансерфинг"), ("/chizhovy2/istoki/nauka/", "Наука за методом"), ("/chizhovy2/marafon/", "Марафон: 90 дней практики"))}
{MOST}
""")

P["istoki/nauka/index.html"] = ("Наука за методом · Истоки метода",
"ЛеДу, Гоулман, Болте Тейлор, Голвитцер, Либерман: открытия, на которых стоит работа школы.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-nauka.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Наука</p><h1>Почему это работает</h1>
<p class="lead">Сцена, состояние, погружение: у&nbsp;каждого инструмента школы есть научная подпорка. Здесь пять открытий, на&nbsp;которые мы&nbsp;опираемся, и&nbsp;то, как каждое живёт у&nbsp;нас в&nbsp;зале.</p></div></div>

<section><div class="wrap"><div class="nails nails3" style="margin-bottom:26px">
<div class="nail"><b>12&nbsp;мс</b><span>фора эмоционального мозга перед&nbsp;думающим</span></div>
<div class="nail"><b>90&nbsp;сек</b><span>живёт химия эмоции, если&nbsp;её&nbsp;не&nbsp;кормить</span></div>
<div class="nail"><b>100&nbsp;лет</b><span>групповой сцене&nbsp;Морено</span></div>
</div></div>
<div class="narrow">
<div class="card white" style="margin-bottom:12px"><span class="bignum">12&nbsp;мс</span><h3>Джозеф ЛеДу: эмоция быстрее мысли</h3><p>Сигнал об&nbsp;угрозе достигает эмоционального центра мозга за&nbsp;12&nbsp;миллисекунд, задолго до&nbsp;думающей коры. Поэтому обещание «в&nbsp;следующий раз отвечу спокойно» пустое: реакция стартует раньше решения. В&nbsp;зале мы&nbsp;работаем с&nbsp;самой записью: она быстрее любой силы воли.</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Дэниел Гоулман: эмоциональный захват</h3><p>В&nbsp;острый момент миндалина перехватывает управление, и&nbsp;умный взрослый человек ведёт себя как не&nbsp;свой. Гоулман назвал это захватом. На&nbsp;тренинге ты&nbsp;учишься видеть его в&nbsp;лицо и&nbsp;выходить из&nbsp;него через тело: пока миндалина рулит, уговоры&nbsp;бессильны.</p></div>
<div class="card white" style="margin-bottom:12px"><span class="bignum">90&nbsp;с</span><h3>Джилл Болте Тейлор: девяносто секунд</h3><p>Химия эмоции живёт в&nbsp;теле около полутора минут. Всё, что дольше, поддерживает уже мысль, которая крутит эмоцию по&nbsp;кругу. Пауза и&nbsp;внимание к&nbsp;телу разжимают этот круг, и&nbsp;этому мы&nbsp;тренируем буквально с&nbsp;первого дня.</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Питер Голвитцер: сила намерения</h3><p>Конкретно сформулированное намерение в&nbsp;разы повышает шанс действия по&nbsp;сравнению с&nbsp;простым «надо&nbsp;бы». Наша утренняя практика на&nbsp;Марафоне стоит на&nbsp;этом открытии.</p></div>
<div class="card white"><h3>Мэттью Либерман: назвать, чтобы ослабить</h3><p>Названная вслух эмоция теряет силу: слова снижают активность миндалины. Половина работы группы происходит именно здесь: чувство впервые получает имя и&nbsp;звучит вслух.</p></div>

<p style="margin-top:26px">И&nbsp;над всем этим сто лет психодрамы Морено: групповой формат, в&nbsp;котором все эти механизмы включаются разом, в&nbsp;одной живой сцене. Наука здесь рамка честности: мы&nbsp;берём проверенные механизмы и&nbsp;не&nbsp;обещаем чудес.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/moreno-psihodrama/", "Морено и психодрама"), ("/chizhovy2/istoki/goddard/", "Невилл Годдард"), ("/chizhovy2/metod/", "Метод целиком"))}
{MOST}
""")

# ================= ИСТОРИИ УЧЕНИКОВ =================
P["istorii/index.html"] = ("Истории учеников · Настоящие отношения",
"Полные истории выпускников школы: точка А, работа, что изменилось. С согласия авторов, без глянца.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istorii-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истории учеников</p><h1>Что происходит с&nbsp;людьми здесь</h1>
<p class="lead">Люди приходят сюда с&nbsp;разным грузом. Ниже их&nbsp;пути как есть: точка&nbsp;А, сопротивление и&nbsp;то, что изменилось. Публикуем с&nbsp;согласия авторов; у&nbsp;каждого свой результат.</p></div></div>

<section><div class="wrap">
<!-- ПРОТОТИП: полные версии историй согласованы с авторами до публикации -->
<div class="grid2">
<div class="card white"><span class="chip" style="background:rgba(110,59,75,.08);color:var(--wine)">Личный путь</span>
<h3>Предприниматель: заново после дна</h3>
<p>Кассовый разрыв, сорвавшаяся свадьба, друзья отвернулись. Что происходило на&nbsp;тренинге, почему труднее всего далась точка&nbsp;А и&nbsp;как жизнь собралась обратно.</p>
<p style="margin-top:14px"><a href="/chizhovy2/istorii/predprinimatel/">Читать его историю</a></p></div>
<div class="card white"><span class="chip" style="background:rgba(92,107,84,.12);color:var(--sage-deep)">Опыт команды</span>
<h3>Девяносто дней команды «МИР»</h3>
<p>Пятнадцать человек, три месяца Марафона: практика утром и&nbsp;вечером, живой чат. Всё словами самих участников.</p>
<p style="margin-top:14px"><a href="/chizhovy2/istorii/komanda-mir/">Как прошли 90&nbsp;дней</a></p></div>
</div>
<p class="note" style="margin-top:18px">Раздел пополняется: ещё несколько историй сейчас на&nbsp;согласовании у&nbsp;авторов.</p>
</div></section>

<section style="padding-top:0"><div class="wrap">
<p class="eyebrow">Короткой строкой</p>
<h2>Голоса из&nbsp;групп</h2>
<div class="grid3" style="margin-top:26px">
<div class="card"><p class="serif" style="font-style:italic">«Намерение это когда я&nbsp;знаю, что в&nbsp;моей жизни возможно только так. Тогда и&nbsp;важности нет, я&nbsp;просто&nbsp;знаю».</p><p class="note" style="margin-top:10px">Участница Марафона</p></div>
<div class="card"><p class="serif" style="font-style:italic">«Когда убираю фокус с&nbsp;себя и&nbsp;вовлечён в&nbsp;команду, энергия кратно растёт, и&nbsp;люди поворачиваются ко&nbsp;мне&nbsp;лицом».</p><p class="note" style="margin-top:10px">Участник Марафона</p></div>
<div class="card"><p class="serif" style="font-style:italic">«Когда цель и&nbsp;мечта действительно мои, всё происходит легко, порой на&nbsp;грани фантастики».</p><p class="note" style="margin-top:10px">Участница Марафона</p></div>
</div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/otzyvy/">Ещё отзывы о&nbsp;школе</a></p>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Начать свою историю</h2>
<p class="sub" style="margin:0 auto 26px">Первый шаг у&nbsp;всех этих историй один: час честного разговора. Для читателей сайта он&nbsp;&#8288;бесплатный.</p>
<a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a>
</div></section>
""")

P["istorii/predprinimatel/index.html"] = ("Предприниматель: заново после дна · Истории учеников",
"Полная история ученика школы: кризис, сопротивление, точка А и как жизнь собралась обратно.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoriya-biznes.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">История ученика</p><h1>Заново после дна</h1>
<p class="lead">Предприниматель, пришёл весной 2024. Записано с&nbsp;его слов, публикуется с&nbsp;согласия; имя по&nbsp;его просьбе скрыто. Результат у&nbsp;каждого свой.</p></div></div>

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
<div class="pull"><div class="q">«Ура, нолик наконец-то провалился.»</div><div class="who">Из его сообщения группе в&nbsp;тот вечер</div></div>

<h2 style="margin-top:34px">Что изменилось</h2>
<p>«Сейчас я&nbsp;строю настоящие отношения везде: в&nbsp;деле, с&nbsp;близкими, с&nbsp;собой. Деньги начали приходить, энергии много, и&nbsp;я&nbsp;умею ей&nbsp;распоряжаться: держу состояние через спорт и&nbsp;благодарности, не&nbsp;сливаю её&nbsp;по&nbsp;мелочам. Раньше отсеивал людей по&nbsp;уровню жизни, сейчас просто строю отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами. Цели кратно увеличились, научился играть в&nbsp;долгую. И&nbsp;мне стало всё равно на&nbsp;чужое мнение обо мне.</p>
<p>Одной фразой: получил новую версию&nbsp;себя».</p>
<div class="pull"><div class="q">«Появилось ощущение, что вижу себя на&nbsp;всей шахматной доске, а&nbsp;не&nbsp;в&nbsp;одной клетке.»</div><div class="who">Его формула итога</div></div>
<p class="note">История личная, поэтому без имени. Суммы и&nbsp;скорость перемен у&nbsp;каждого свои: школа не&nbsp;обещает повторения чужого результата.</p>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Узнал свою ситуацию?</h2>
<p class="sub" style="margin:0 auto 26px">Его путь начался с&nbsp;честного разговора о&nbsp;точке&nbsp;А. Твой может начаться так&nbsp;же: собеседование для читателей сайта&nbsp;бесплатное.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/istorii/komanda-mir/" style="margin-left:8px">Ещё история: команда «МИР»</a></p>
</div></section>
""")

P["istorii/komanda-mir/index.html"] = ("Девяносто дней команды «МИР» · Истории учеников",
"Как выглядит Марафон изнутри: утренние намерения, вечерние благодарности и команда, голосами участников.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-10.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Марафон изнутри</p><h1>Девяносто дней команды «МИР»</h1>
<p class="lead">Осень 2022&nbsp;года, пятнадцать человек, третий модуль «Создатель реальности». Три месяца еженедельных встреч с&nbsp;Алексеем и&nbsp;Ириной и&nbsp;ежедневной практики. Ниже их&nbsp;история, собранная из&nbsp;живого командного&nbsp;чата.</p></div></div>

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
<p style="margin-top:30px;text-align:center"><a class="btn btn-wine" href="/chizhovy2/marafon/">Как устроен Марафон</a> <a class="btn btn-ghost" href="/chizhovy2/sessiya/" style="margin-left:8px">Записаться на&nbsp;собеседование</a></p>
</div></section>
""")

# ================= СЛОВАРЬ ШКОЛЫ =================
P["slovar/index.html"] = ("Словарь школы · Настоящие отношения",
"Точка А, событийный круг, маятники, важность, намерение, нолик провалился: язык школы с переводом на обычный.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/slovar-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Язык школы</p><h1>Словарь школы</h1>
<p class="lead">У&nbsp;выпускников есть свой язык: короткие слова, за&nbsp;которыми стоят большие механизмы. Здесь перевод на&nbsp;обычный русский, чтобы ты&nbsp;понимал группу с&nbsp;первого дня.</p></div></div>

<section><div class="wrap">
<p class="eyebrow">Про честность с&nbsp;собой</p>
<div class="grid2" style="margin-top:10px;margin-bottom:34px">
<div class="card white">{icon('target')}<h3>Точка&nbsp;А</h3><p>Честное признание, где ты&nbsp;сейчас, без прикрас и&nbsp;оправданий. Первый и&nbsp;самый трудный шаг работы: пока точка&nbsp;А не&nbsp;принята, двигаться&nbsp;некуда.</p></div>
<div class="card white">{icon('shield','var(--sand)')}<h3>Нолик провалился</h3><p>Момент, когда защита падает и&nbsp;человек наконец видит правду о&nbsp;себе. В&nbsp;группе это праздник, потому что именно отсюда начинается настоящая работа.</p></div>
<div class="card white">{icon('loop','var(--sage-deep)')}<h3>Событийный круг</h3><p>Механизм повтора: событие включает эмоцию, эмоция будит старое решение, и&nbsp;оно доигрывает знакомый сценарий. Круг быстрее сознания, поэтому усилием воли не&nbsp;рвётся.</p></div>
<div class="card white">{icon('layers')}<h3>Этаж слов и&nbsp;этаж тела</h3><p>Понимание живёт на&nbsp;верхнем этаже, запись хранится на&nbsp;нижнем: в&nbsp;эмоции и&nbsp;теле. Книги стучатся в&nbsp;верхний, работа школы идёт на&nbsp;нижний.</p></div>
</div>

<p class="eyebrow">Про состояние</p>
<div class="grid2" style="margin-top:10px;margin-bottom:34px">
<div class="card white">{icon('flame')}<h3>Состояние первично</h3><p>Главная формула здесь: жизнь слушается состояния. Меняется оно, меняются решения, за&nbsp;ними события. Ученики говорят короче: мир&nbsp;зеркалит.</p></div>
<div class="card white">{icon('mountain','var(--sage-deep)')}<h3>Муравей и&nbsp;слон</h3><p>Разум мал и&nbsp;суетлив, как муравей. Состояние огромно, как слон. Пока слон идёт в&nbsp;другую сторону, планы разума весят меньше грамма: масса не&nbsp;та.</p></div>
<div class="card white">{icon('gear','var(--sand)')}<h3>Захват</h3><p>Момент, когда эмоциональный мозг перехватывает управление и&nbsp;умный взрослый человек ведёт себя как не&nbsp;свой. Пока захват держит, «взять себя в&nbsp;руки» физически&nbsp;нечем.</p></div>
<div class="card white">{icon('hourglass')}<h3>Девяносто секунд</h3><p>Столько живёт химия эмоции, если не&nbsp;кормить её&nbsp;мыслями по&nbsp;кругу. Пауза и&nbsp;внимание к&nbsp;телу дают волне пройти, дальше можно решать ясно.</p></div>
</div>

<p class="eyebrow">Про ежедневную практику</p>
<div class="grid2" style="margin-top:10px">
<div class="card white">{icon('route')}<h3>Намерение</h3><p>Утренняя практика Марафона: из&nbsp;какого состояния иду в&nbsp;день и&nbsp;что создаю. Желание просит, намерение спокойно&nbsp;знает.</p></div>
<div class="card white">{icon('ceiling','var(--sand)')}<h3>Важность</h3><p>Раздутая ставка на&nbsp;результат, которая включает страх и&nbsp;сжимает выбор. Снял важность, вернулась лёгкость: переговоры, свидания и&nbsp;большие решения идут иначе.</p></div>
<div class="card white">{icon('pendulum','var(--sage-deep)')}<h3>Маятники</h3><p>Всё, что кормится твоей реакцией: скандал, лента новостей, чужая паника. Дёрнулся, отдал энергию. Навык школы: заметить крючок и&nbsp;не&nbsp;схватиться.</p></div>
<div class="card white">{icon('people')}<h3>Быть вкладом</h3><p>Развернуть фокус с&nbsp;«что мне дадут» на&nbsp;«что я&nbsp;даю»: в&nbsp;паре, в&nbsp;команде, в&nbsp;деле. Участники отмечают: энергия от&nbsp;этого не&nbsp;уходит, а&nbsp;прибывает.</p></div>
<div class="card white">{icon('calendar')}<h3>Играть в&nbsp;долгую</h3><p>Горизонт вместо суеты: строить отношения и&nbsp;дело на&nbsp;годы, без выжимания быстрой выгоды. Опора выпускников в&nbsp;решениях.</p></div>
<div class="card white">{icon('sunrise','var(--sand)')}<h3>Открытия и&nbsp;благодарности</h3><p>Вечерняя практика: что понял за&nbsp;день и&nbsp;за&nbsp;что спасибо. Закрепляет новый способ жить лучше любой мотивации.</p></div>
</div>
<p class="note" style="margin-top:22px">Часть слов пришла из&nbsp;истоков метода: подробнее в&nbsp;разделах <a href="/chizhovy2/istoki/zeland-transerfing/">про трансерфинг</a> и&nbsp;<a href="/chizhovy2/istoki/nauka/">про науку</a>.</p>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Слова оживают в&nbsp;зале</h2>
<p class="sub" style="margin:0 auto 26px">Читать словарь полезно, а&nbsp;понимаешь его телом на&nbsp;тренинге. Начни с&nbsp;гайда или запишись на&nbsp;собеседование.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Скачать гайд</a></p>
</div></section>
""")

# ================= КОМУ: ПРЕДПРИНИМАТЕЛИ =================
FINCTA = """<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Начни с&nbsp;часа разговора</h2>
<p class="sub" style="margin:0 auto 26px">Собеседование в&nbsp;школу: час о&nbsp;твоей ситуации и&nbsp;честный ответ, чем мы&nbsp;можем помочь. Для читателей сайта&nbsp;бесплатно.</p>
<p><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Сначала почитать гайд</a></p>
</div></section>"""

P["dlya-predprinimatelej/index.html"] = ("Для предпринимателей · Настоящие отношения",
"Сильный снаружи, устал внутри: как школа работает с теми, кто привык всё тащить сам.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoriya-biznes.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Кому подходит · Предприниматели</p><h1>Сильный снаружи, устал внутри</h1>
<p class="lead">Бизнес, семья, статус: всё по&nbsp;списку. И&nbsp;усталость, о&nbsp;которой некому рассказать, потому что ты&nbsp;для всех опора. Мы&nbsp;шестнадцать лет работаем с&nbsp;людьми, которые привыкли тащить сами.</p></div></div>

<section><div class="narrow">
<h2>Знакомые сюжеты</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('ceiling')}<h3>Потолок в&nbsp;деле</h3><p>Рывки вверх быстро выравниваются обратно. Цифра оборота годами почти одна, и&nbsp;рынок тут ни&nbsp;при&nbsp;чём: держит старая запись.</p></div>
<div class="card">{icon('shield','var(--sand)')}<h3>Держать лицо</h3><p>Просить о&nbsp;помощи стыдно, показывать усталость нельзя. Панцирь, который когда-то спасал, теперь просто тяжёлый.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Решения из&nbsp;страха</h3><p>Суета, перестраховка, откладывание больших ходов. Он&nbsp;шепчет тише жадности, но&nbsp;рулит&nbsp;чаще.</p></div>
<div class="card">{icon('cups')}<h3>Дом на&nbsp;остатке батареи</h3><p>Семье достаётся остаток после дела. Обычно он&nbsp;мал, и&nbsp;все это&nbsp;чувствуют.</p></div>
</div>
<div class="pull"><div class="q">«Я&nbsp;понимал крах, но&nbsp;не&nbsp;понимал, как начать снова и&nbsp;где найти силы.»</div><div class="who">Из истории ученика-предпринимателя</div></div>
<p>Один из&nbsp;наших учеников пришёл ровно из&nbsp;этой точки: кассовый разрыв, долги, отвернувшиеся друзья. Его полная история, с&nbsp;сопротивлением и&nbsp;переломом, опубликована с&nbsp;его согласия: <a href="/chizhovy2/istorii/predprinimatel/">заново после дна</a>.</p>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что здесь получает предприниматель</h2>
<p>Работа идёт с&nbsp;причиной, и&nbsp;она у&nbsp;потолка, страха и&nbsp;усталости общая: старые решения, которые крутят <a href="/chizhovy2/metod/" style="color:#D08A5F">событийный круг</a>. Когда запись переписана, меняется сразу несколько сфер: большие ходы делаются из&nbsp;спокойствия, дело перестаёт держаться на&nbsp;надрыве, дома снова видно человека, а&nbsp;не&nbsp;функцию.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>16&nbsp;лет</b><span>практики с&nbsp;состоявшимися взрослыми&nbsp;людьми</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе: окружение твоего уровня, без&nbsp;толпы</span></div>
<div class="nail"><b>3&nbsp;месяца</b><span>сопровождения: результат закрепляется в&nbsp;деле</span></div>
</div></div></section>
{FINCTA}
""")

# ================= КОМУ: ЖЕНЩИНЫ =================
P["dlya-zhenshchin/index.html"] = ("Для женщин · Настоящие отношения",
"Отношения, состояние, сценарии: как школа работает с теми, кто устал жить в режиме ожидания и обслуживания.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-m1.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Кому подходит · Женщины</p><h1>Вернуть себя себе</h1>
<p class="lead">Годы в&nbsp;режиме ожидания и&nbsp;обслуживания: чтобы заметили, оценили, изменились. Здесь работа начинается с&nbsp;другого конца: с&nbsp;твоей записи, твоего состояния и&nbsp;твоей половины сценария.</p></div></div>

<section><div class="narrow">
<h2>С чем приходят чаще всего</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('loop')}<h3>Один сценарий с&nbsp;разными людьми</h3><p>Мужчины разные, финал одинаковый. Значит, общий знаменатель не&nbsp;в&nbsp;них: сценарий приходит с&nbsp;тобой, и&nbsp;его можно&nbsp;переписать.</p></div>
<div class="card">{icon('cups','var(--sand)')}<h3>Быт вместо близости</h3><p>Календарь общий, разговоры про логистику. Не&nbsp;ссоритесь, потому что&nbsp;незачем. А&nbsp;хочется, чтобы снова было о&nbsp;чём молчать вдвоём.</p></div>
<div class="card">{icon('flame','var(--sage-deep)')}<h3>Чувства под анестезией</h3><p>Научилась обезболивать и&nbsp;не&nbsp;слышать себя. Снаружи «всё нормально», внутри давно тихо и&nbsp;пусто.</p></div>
<div class="card">{icon('speech')}<h3>Сказать и&nbsp;не&nbsp;быть услышанной</h3><p>Просьбы звучат как упрёки, разговоры кончаются глухой стеной. Дело не&nbsp;в&nbsp;словах: в&nbsp;состоянии, из&nbsp;которого они&nbsp;сказаны.</p></div>
</div>
<div class="pull"><div class="q">«Теперь знаю, что могу быть яркой, настоящей, звонкой, сама по&nbsp;себе.»</div><div class="who">Участница второго модуля</div></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что меняется</h2>
<p>На&nbsp;сцене видно, где выключились чувства и&nbsp;какое решение это выключение держит. Когда запись переписана, возвращается то, что было под анестезией: яркость, желания, голос. Отношения подтягиваются следом: <a href="/chizhovy2/para/" style="color:#D08A5F">даже когда работает один из&nbsp;двоих</a>.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>Сцена</b><span>работа телом и&nbsp;эмоцией, где хранится&nbsp;запись</span></div>
<div class="nail"><b>Группа</b><span>место, где тебя слышат с&nbsp;первого&nbsp;слова</span></div>
<div class="nail"><b>90&nbsp;дней</b><span>практики, чтобы новое состояние стало&nbsp;обычным</span></div>
</div></div></section>
{FINCTA}
""")

# ================= КАК ПРОХОДИТ =================
P["kak-prohodit/index.html"] = ("Как проходит обучение · Настоящие отношения",
"Путь ученика по шагам: собеседование, три модуля с интеграцией, сопровождение. Что происходит в зале.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-06.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Как проходит</p><h1>Путь ученика по&nbsp;шагам</h1>
<p class="lead">Без сюрпризов: вот как устроено движение от&nbsp;первого разговора до&nbsp;результатов, которые остаются. Каждый шаг добровольный, на&nbsp;каждом можно остановиться.</p></div></div>

<section><div class="wrap">
<p class="eyebrow">Маршрут</p>
<h2>От собеседования до&nbsp;Марафона</h2>
<div class="timeline" style="margin-top:28px">{timeline_svg()}</div>
<div class="timeline-m" style="margin-top:28px">
<div class="tm"><div class="c">I</div><div><b>Возвращение к&nbsp;себе</b><span>2,5 дня очно</span></div></div>
<div class="gap">3-5 недель интеграции</div>
<div class="tm"><div class="c">II</div><div><b>Внутренняя свобода</b><span>5 дней очно</span></div></div>
<div class="gap">3-5 недель интеграции</div>
<div class="tm last"><div class="c">III</div><div><b>Создатель реальности</b><span>3 месяца в&nbsp;жизни, результаты&nbsp;остаются</span></div></div>
</div>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">0</span>{icon('speech')}<h3>Собеседование</h3><p>Час живого разговора: твоя ситуация, честный взгляд и&nbsp;решение с&nbsp;двух сторон, по&nbsp;пути&nbsp;ли нам. Для&nbsp;читателей сайта бесплатно.</p></div>
<div class="card"><span class="bignum">1-2</span>{icon('people','var(--sage-deep)')}<h3>Очные модули</h3><p>Погружение на&nbsp;несколько дней: сцены, разборы, работа с&nbsp;состоянием в&nbsp;группе 10-20 человек. Между модулями недели интеграции: новое проверяется обычной жизнью.</p></div>
<div class="card"><span class="bignum">3</span>{icon('calendar','var(--sand)')}<h3>Марафон</h3><p>Три месяца практики в&nbsp;настоящей жизни: команда, еженедельные разборы с&nbsp;ведущими, ежедневные&nbsp;<a href="/chizhovy2/praktiki/">практики</a>.</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="narrow">
<h2>Что происходит в&nbsp;зале</h2>
<p>Ядро работы: <a href="/chizhovy2/istoki/moreno-psihodrama/">живая сцена</a>. Ты&nbsp;называешь ситуацию, которая держит, группа помогает её&nbsp;построить, и&nbsp;разговор, который не&nbsp;случился в&nbsp;жизни, происходит здесь. Рядом разборы, работа с&nbsp;состоянием и&nbsp;простые практики, которые остаются с&nbsp;тобой после зала.</p>
<p>Глубина всегда добровольна: никто не&nbsp;вытаскивает силой, темп каждый выбирает сам. Обычно уже к&nbsp;вечеру первого дня группа перестаёт быть чужой: у&nbsp;людей одинаковые боли, и&nbsp;в&nbsp;чужой истории ты&nbsp;узнаёшь свою. Подробнее о&nbsp;рамках: <a href="/chizhovy2/bezopasnost/">безопасность и&nbsp;границы</a>.</p>
<div class="pull"><div class="q">«Ты получишь ровно ту&nbsp;порцию, которая нужна именно&nbsp;сейчас.»</div><div class="who">Слова выпускника новичкам</div></div>
</div></section>
{FINCTA}
""")

# ================= ПРАКТИКИ =================
P["praktiki/index.html"] = ("Ежедневные практики · Настоящие отношения",
"Утреннее намерение, вечерние открытия и благодарности, маятники и важность: как выглядит день ученика.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/slovar-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Практики школы</p><h1>Из чего состоит день ученика</h1>
<p class="lead">Никакой магии на&nbsp;час: короткие ежедневные действия, которые держат фокус и&nbsp;состояние. Ниже практики Марафона, как их&nbsp;ведут наши команды.</p></div></div>

<section><div class="narrow">
<div class="timeline-m" style="display:block;margin-bottom:26px">
<div class="tm"><div class="c" style="background:var(--sand);color:#1B1410">У</div><div><b>Утро: намерение</b><span>из какого состояния иду в&nbsp;день и&nbsp;что создаю</span></div></div>
<div class="gap">днём: замечать маятники, снимать&nbsp;важность</div>
<div class="tm last"><div class="c">В</div><div><b>Вечер: открытия и&nbsp;благодарности</b><span>что понял за&nbsp;день, за&nbsp;что спасибо</span></div></div>
</div>

<h2>Практики по&nbsp;одной</h2>
<div class="card white" style="margin:20px 0 12px">{icon('route')}<h3>Намерение на&nbsp;день</h3><p>Утром формулируешь не&nbsp;список дел, а&nbsp;состояние и&nbsp;фокус: «в&nbsp;моей жизни возможно только так». Желание просит, намерение спокойно&nbsp;знает. Научная опора: <a href="/chizhovy2/istoki/nauka/">Голвитцер о&nbsp;силе&nbsp;намерения</a>.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('pendulum','var(--sage-deep)')}<h3>Выход из&nbsp;маятников</h3><p>Днём замечаешь, что кормится твоей реакцией: скандал, лента, чужая паника. Заметил крючок, не&nbsp;схватился, сохранил энергию. Словами ученика: «отследил, не&nbsp;среагировал, удержал состояние весь день».</p></div>
<div class="card white" style="margin-bottom:12px">{icon('ceiling','var(--sand)')}<h3>Снятие важности</h3><p>Где вцепился, там и&nbsp;заклинило: раздутая ставка включает страх. Снял важность, вернулась лёгкость: переговоры, свидания, большие решения идут иначе.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('people')}<h3>Быть вкладом</h3><p>Развернуть фокус с&nbsp;«что мне дадут» на&nbsp;«что я&nbsp;даю». Участники отмечают: энергия от&nbsp;этого прибывает, и&nbsp;люди поворачиваются лицом.</p></div>
<div class="card white">{icon('sunrise','var(--sage-deep)')}<h3>Открытия и&nbsp;благодарности</h3><p>Вечером короткий итог: что открыл про себя, за&nbsp;что спасибо дню и&nbsp;людям. Закрепляет новый способ жить надёжнее любой мотивации.</p></div>

<p class="note" style="margin-top:18px">Термины из&nbsp;практик разобраны в&nbsp;<a href="/chizhovy2/slovar/">словаре школы</a>, живой пример девяноста дней: <a href="/chizhovy2/istorii/komanda-mir/">история команды «МИР»</a>.</p>
</div></section>
{FINCTA}
""")

# ================= МАНИФЕСТ =================
P["manifest/index.html"] = ("Манифест школы · Настоящие отношения",
"Почему школа называется «Настоящие отношения» и какие принципы здесь не продаются.", "vedushchie", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/portret.jpg');background-position:center 25%"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Манифест</p><h1>Почему «Настоящие отношения»</h1>
<p class="lead">Имя школы это не&nbsp;только про пары. Это про отношения с&nbsp;собой, с&nbsp;делом, с&nbsp;близкими и&nbsp;с&nbsp;правдой: везде, где кончается «казаться» и&nbsp;начинается «быть».</p></div></div>

<section><div class="narrow">
<div class="pull" style="margin-top:0"><div class="q">«У&nbsp;нас не&nbsp;было идеальной истории. Было непонимание, ошибки, потери, моменты, где казалось: дальше некуда. Именно там началось настоящее.»</div><div class="who">Алексей и&nbsp;Ирина Чижовы</div></div>
<p>Школу ведёт пара, которая семнадцать лет строит свои отношения: с&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них. Поэтому здесь не&nbsp;учат жить и&nbsp;не&nbsp;мотивируют со&nbsp;сцены. Здесь разбираются вместе: почему ты&nbsp;реагируешь так, как реагируешь, и&nbsp;что с&nbsp;этим делать&nbsp;по‑настоящему.</p>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Принципы, которые не&nbsp;продаются</p>
<h2>На чём стоим</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('target','var(--copper)')}<h3>Отбор важнее выручки</h3><p>Вход через собеседование, и&nbsp;это фильтр, а&nbsp;не&nbsp;формальность. Отговорить можем так&nbsp;же честно, как&nbsp;пригласить.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Камерность важнее масштаба</h3><p>Группы 10-20 человек, каждого знаем по&nbsp;имени. Расти будем числом групп, зал большим не&nbsp;станет.</p></div>
<div class="card">{icon('speech','var(--copper)')}<h3>Честность важнее красоты</h3><p>Истории учеников публикуем с&nbsp;согласия и&nbsp;без глянца, результат у&nbsp;каждого свой. Истоки метода <a href="/chizhovy2/istoki/" style="color:#D08A5F">называем&nbsp;открыто</a>.</p></div>
<div class="card">{icon('mountain','var(--copper)')}<h3>Глубина важнее скорости</h3><p>Мы&nbsp;за&nbsp;работу с&nbsp;причиной, поэтому формат длинный: погружение, интеграция, сопровождение. Быстрых чудес не&nbsp;обещаем.</p></div>
</div>
</div></section>
{FINCTA}
""")

# ================= БЕЗОПАСНОСТЬ =================
P["bezopasnost/index.html"] = ("Безопасность и границы · Настоящие отношения",
"Честные рамки работы: кому школа не подойдёт, правила группы, добровольность глубины.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Безопасность и&nbsp;границы</p><h1>Глубина требует рамок</h1>
<p class="lead">Сильная работа возможна только там, где безопасно. Поэтому у&nbsp;школы есть границы, о&nbsp;которых мы&nbsp;говорим до&nbsp;старта, а&nbsp;не&nbsp;после.</p></div></div>

<section><div class="narrow">
<h2>Три опоры безопасности</h2>
<div class="card white" style="margin:20px 0 12px">{icon('route')}<h3>Глубина добровольна</h3><p>Никто не&nbsp;вытаскивает силой: темп и&nbsp;меру открытости каждый выбирает сам. Сцена начинается тогда, когда ты&nbsp;к&nbsp;ней готов.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('shield','var(--sage-deep)')}<h3>Личное остаётся в&nbsp;зале</h3><p>Истории участников не&nbsp;выносятся из&nbsp;группы: это базовое правило групповой работы. Публикуем только то, на&nbsp;что автор дал согласие.</p></div>
<div class="card white">{icon('speech','var(--sand)')}<h3>Честность на&nbsp;входе</h3><p>Собеседование существует, чтобы решить с&nbsp;двух сторон, подходит&nbsp;ли тебе школа. Если видим, что не&nbsp;подходит, говорим прямо и&nbsp;советуем, куда идти.</p></div>

<h2 style="margin-top:34px">Кому школа не&nbsp;подойдёт</h2>
<p>Тем, кто ищет волшебную таблетку за&nbsp;вечер. Тем, кто пока не&nbsp;готов работать в&nbsp;группе. И&nbsp;тем, кому сейчас нужна медицинская помощь: тренинг её&nbsp;не&nbsp;заменяет, это мы&nbsp;говорим прямо на&nbsp;собеседовании.</p>
<p>Остальные вопросы о&nbsp;формате собраны на&nbsp;странице <a href="/chizhovy2/voprosy/">вопросов и&nbsp;ответов</a>.</p>
</div></section>
{FINCTA}
""")

# ================= СООБЩЕСТВО =================
P["soobshchestvo/index.html"] = ("Сообщество выпускников · Настоящие отношения",
"Команды, забеги, поддержка после модулей: во что превращается группа после тренинга.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-12.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Сообщество</p><h1>Группа, которая не&nbsp;расходится</h1>
<p class="lead">Модуль заканчивается, а&nbsp;люди остаются. Команды продолжают жить: практики, встречи, забеги и&nbsp;поддержка, которая работает даже в&nbsp;два часа ночи.</p></div></div>

<section><div class="narrow">
<h2>Во что превращается группа</h2>
</div>
<div class="wrap"><div class="grid3" style="margin-top:24px">
<div class="card">{icon('people')}<h3>Команда</h3><p>На&nbsp;Марафоне группа становится командой с&nbsp;общей целью и&nbsp;напарником у&nbsp;каждого. Такой уровень окружения многим встречается&nbsp;впервые.</p></div>
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
{FINCTA}
""")

# ================= С ЧЕГО НАЧАТЬ =================
P["start/index.html"] = ("С чего начать · Настоящие отношения",
"Маршрут новичка: гайд, собеседование, первый модуль. Три шага без обязательств.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Новичку</p><h1>С чего начать</h1>
<p class="lead">Не&nbsp;нужно сразу решаться на&nbsp;модуль. Вот короткий маршрут: каждый шаг бесплатный, добровольный и&nbsp;что-то проясняет.</p></div></div>

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
<p class="lead">Мы&nbsp;отвечаем лично, без ботов и&nbsp;менеджерских скриптов. Пиши, как удобно тебе.</p></div></div>

<section><div class="narrow">
<div class="grid2" style="margin-top:6px">
<div class="card white">{icon('speech')}<h3>Telegram</h3><p>Канал школы: анонсы наборов, живые тексты пары, ответы на&nbsp;вопросы.</p><p style="margin-top:12px"><a href="https://t.me/+LVptSH6Mt4hhYmFi">Открыть Telegram</a></p></div>
<div class="card white">{icon('calendar','var(--sage-deep)')}<h3>Собеседование</h3><p>Час разговора о&nbsp;твоей ситуации, онлайн или очно. Для читателей сайта&nbsp;бесплатно.</p><p style="margin-top:12px"><a href="/chizhovy2/sessiya/">Записаться</a></p></div>
</div>
<p class="note" style="margin-top:20px">Реквизиты и&nbsp;документы для оплаты появятся здесь вместе с&nbsp;онлайн-оплатой мини-продуктов.</p>
</div></section>
{FINCTA}
""")

# ================= ТЕХНИКИ СЦЕНЫ =================
P["tehniki-sceny/index.html"] = ("Техники сцены · Настоящие отношения",
"Обмен ролями, дублирование, зеркало, пустой стул: инструменты живой сцены с разбором.", "metod", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/metod-stul.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Инструменты работы</p><h1>Техники живой сцены</h1>
<p class="lead">Со&nbsp;стороны сцена похожа на&nbsp;театр без сценария. Внутри у&nbsp;неё точная механика: вот инструменты, которыми ведущие собирают перезапись, и&nbsp;что делает каждый из&nbsp;них.</p></div></div>

<section><div class="narrow">
<div class="card white" style="margin-bottom:12px">{icon('people')}<h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место другого человека из&nbsp;своей сцены и&nbsp;отвечаешь себе его словами. Пять минут в&nbsp;чужой роли показывают то, что годами не&nbsp;видно из&nbsp;своей: почему он&nbsp;молчит, чего она боится, что на&nbsp;самом деле стоит за&nbsp;фразой, которая тебя ранит.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('speech','var(--sage-deep)')}<h3>Дублирование</h3><p>Человек из&nbsp;группы становится рядом и&nbsp;договаривает то, что ты&nbsp;чувствуешь, но&nbsp;не&nbsp;решаешься произнести. Когда невысказанное впервые звучит вслух, тело отзывается сразу: значит,&nbsp;попали.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('mirror','var(--sand)')}<h3>Зеркало</h3><p>Выходишь из&nbsp;собственной сцены и&nbsp;смотришь её&nbsp;со&nbsp;стороны, как зритель. Так впервые видно сценарий целиком: где включилась старая запись и&nbsp;в&nbsp;какой момент финал стал предрешён.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('cups')}<h3>Пустой стул</h3><p>Напротив ставится стул, и&nbsp;на&nbsp;нём «сидит» тот, с&nbsp;кем разговор так и&nbsp;не&nbsp;случился: отец, бывший, ты&nbsp;сам из&nbsp;прошлого. Разговор, отложенный на&nbsp;годы, происходит здесь, и&nbsp;у&nbsp;него наконец появляется финал.</p></div>
<div class="card white">{icon('sunrise','var(--sage-deep)')}<h3>Новое решение</h3><p>Кульминация сцены: в&nbsp;точке, где когда-то было принято старое решение, ты&nbsp;принимаешь другое. Оно записывается так&nbsp;же глубоко, как прежнее: телом и&nbsp;эмоцией, поэтому и&nbsp;держится.</p></div>
<p style="margin-top:22px">Откуда эти инструменты и&nbsp;почему им&nbsp;сто лет: <a href="/chizhovy2/istoki/moreno-psihodrama/">Морено и&nbsp;психодрама</a>. Как сцена встроена в&nbsp;наш метод: <a href="/chizhovy2/metod/">метод целиком</a>.</p>
</div></section>
{FINCTA}
""")

# ================= ТРИ СОМНЕНИЯ =================
P["somneniya/index.html"] = ("Частые сомнения · Настоящие отношения",
"«У меня особый случай», «я уже был у психолога», «боюсь группы»: честный разбор трёх главных сомнений.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Перед решением</p><h1>Три сомнения, с&nbsp;которыми приходят</h1>
<p class="lead">Эти три фразы мы&nbsp;слышим на&nbsp;собеседованиях чаще всего. Разберём честно, без уговоров: где сомнение право, а&nbsp;где оно просто голос старой записи.</p></div></div>

<section><div class="narrow">
<h2>«У меня особый случай»</h2>
<p>Отчасти правда: биографии у&nbsp;всех разные, и&nbsp;на&nbsp;сцене твоя разбирается индивидуально, а&nbsp;не&nbsp;по&nbsp;шаблону. Но&nbsp;механика повтора у&nbsp;людей общая: событие, эмоция, старое решение, знакомый финал. Поэтому в&nbsp;чужой истории на&nbsp;группе ты&nbsp;так часто узнаёшь свою: случаи особые, а&nbsp;<a href="/chizhovy2/metod/">круг один</a>.</p>
<h2 style="margin-top:32px">«Я уже был у&nbsp;психолога»</h2>
<p>И&nbsp;это хорошо: терапия и&nbsp;тренинг не&nbsp;соперники, они дополняют друг друга. Личная терапия работает словами, по&nbsp;часу в&nbsp;неделю. Здесь работа идёт телом и&nbsp;эмоцией, в&nbsp;живых сценах, в&nbsp;погружении на&nbsp;несколько дней: другой инструмент для другого слоя. Понимание, которое ты&nbsp;накопил у&nbsp;психолога, на&nbsp;сцене превращается в&nbsp;пережитый опыт.</p>
<h2 style="margin-top:32px">«Боюсь группы»</h2>
<p>Самое частое и&nbsp;самое человеческое. Правда такая: глубина всегда добровольна, никто не&nbsp;вытаскивает силой, темп выбираешь ты. Обычно уже к&nbsp;вечеру первого дня чужих в&nbsp;зале не&nbsp;остаётся. А&nbsp;ещё именно группа делает работу такой сильной: <a href="/chizhovy2/tehniki-sceny/">сцене нужны люди</a>, и&nbsp;поддержка группы держит там, где одному тяжело. Рамки описаны на&nbsp;странице <a href="/chizhovy2/bezopasnost/">безопасности</a>.</p>
<div class="pull"><div class="q">«Труднее всего было принять точку&nbsp;А. Признать, где я&nbsp;на&nbsp;самом деле. Дальше всё началось.»</div><div class="who">Участник тренинга</div></div>
<p>Осталось сомнение, которого здесь нет? Принеси его на&nbsp;собеседование: разберём лично и&nbsp;честно.</p>
</div></section>
{FINCTA}
""")

# ================= СТАТЬИ (ХАБ) =================
P["stati/index.html"] = ("Статьи школы · Настоящие отношения",
"Библиотека школы: разборы про отношения, состояние, сценарии, трансерфинг и психодраму языком метода.", "stati", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/stati-hero.png')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Библиотека школы</p><h1 style="font-size:clamp(2rem,5.5vw,3.7rem)">Статьи, после&nbsp;которых что‑то&nbsp;щёлкает</h1>
<p class="lead">Разборы болей, с&nbsp;которыми приходят в&nbsp;школу: почему ссоры идут по&nbsp;кругу, куда уходят силы и&nbsp;кто на&nbsp;самом деле пишет твой сценарий. Языком метода, с&nbsp;опорой на&nbsp;науку.</p></div></div>

<section><div class="wrap">
<p class="eyebrow">Карта библиотеки</p>
<h2>Пять разделов библиотеки</h2>
<p class="sub">Ниже карта тем на&nbsp;вырост, первые пять статей уже в&nbsp;работе: каждая готовая появится здесь ссылкой. Пока они пишутся, начни с&nbsp;гайда, он&nbsp;собирает главное ядро метода в&nbsp;одном&nbsp;выпуске.</p>
<div class="grid2" style="margin-top:28px">
<div class="card">{icon('cups')}<h3>Отношения и&nbsp;пара</h3>
<div class="chiplist"><span>Ссоры по&nbsp;одному кругу</span><span>Близость ушла в&nbsp;быт</span><span>Муж молчит</span><span>Один сценарий с&nbsp;разными людьми</span><span>Кризис после десяти лет</span><span>Партнёры-соседи</span><span>Как говорить, чтобы услышали</span></div></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Состояние и&nbsp;выгорание</h3>
<div class="chiplist"><span>Нет сил при&nbsp;успехе</span><span>Тревога фоном</span><span>Всё понимаю, ничего не&nbsp;меняю</span><span>Устал быть сильным</span><span>Откуда берётся энергия</span></div></div>
<div class="card">{icon('route','var(--sage-deep)')}<h3>Сценарии и&nbsp;решения</h3>
<div class="chiplist"><span>Жизненный сценарий</span><span>Установки из&nbsp;детства</span><span>Денежный потолок</span><span>Самосаботаж</span><span>Почему аффирмации не&nbsp;работают</span></div></div>
<div class="card">{icon('loop')}<h3>Трансерфинг и&nbsp;est</h3>
<div class="chiplist"><span>Маятники простыми словами</span><span>Важность и&nbsp;как её&nbsp;снять</span><span>Намерение против желания</span><span>Что такое тренинг est</span><span>«Трансформация» Рейнхарта:&nbsp;разбор</span></div></div>
</div>
<div class="card linen" style="margin-top:16px">{icon('people','var(--sage-deep)')}<h3>Психодрама и&nbsp;метод</h3>
<div class="chiplist"><span>Что такое психодрама</span><span>Пустой стул</span><span>Как проходит групповая работа</span><span>Тренинг и&nbsp;терапия: в&nbsp;чём разница</span></div></div>
</div></section>

<section class="center" style="padding-top:0"><div class="narrow" style="text-align:center">
<h2>Пока библиотека растёт</h2>
<p class="sub" style="margin:0 auto 26px">Главное ядро метода уже собрано в&nbsp;бесплатном гайде «Кто пишет сценарий твоей жизни». А&nbsp;живые вопросы можно принести на&nbsp;собеседование: для&nbsp;читателей сайта оно бесплатное.</p>
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
