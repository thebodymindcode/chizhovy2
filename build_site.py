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
.wrap{max-width:940px;margin:0 auto;padding:0 24px}
.narrow{max-width:940px;margin:0 auto;padding:0 24px}
.narrow>*{max-width:none}
/* Двухколоночный разворот: текст слева, врезка справа. Правая пустота заполняется смыслом */
/* Заголовки секций по центру, текст под ними колонкой по центру */
section > .wrap > .eyebrow,
section > .wrap > h2,
section > .narrow > .eyebrow,
section > .narrow > h2{text-align:left;max-width:none;margin-left:0;margin-right:0}
section > .wrap > .eyebrow::before,
section > .narrow > .eyebrow::before{display:inline-block;vertical-align:middle}
section > .wrap > .eyebrow::before,
section > .narrow > .eyebrow::before{margin:0 10px 3px 0}
section > .wrap > h2 + .sub,
section > .narrow > h2 + .sub,
section > .wrap > h2 + p,
section > .narrow > h2 + p{text-align:left;max-width:none;margin-left:0;margin-right:0}
/* кнопки в центрированной секции стоят по центру, в узкой колонке слева */
.btns{text-align:left}
.btns .btn+.btn{margin-left:10px}
.tside .btns,.split .btns,.hero .btns,.diagrow .btns{text-align:left}
/* Система: широкая секция по центру, узкая колонка рядом с фото или врезкой слева */
.tside > .col > .eyebrow,
.tside > .col > h2,
.tside > .col > h3,
.split > div > .eyebrow,
.split > div > h2,
.split > div > h3{text-align:left}
.tside > .col > *{margin-left:0;margin-right:0}
.split > div > *{margin-left:0;margin-right:0;max-width:none}

.tside{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:56px;align-items:start}
/* если в колонке уже стоит сетка карточек, врезка рядом мешает: уводим её вниз в ряд */
.tside:has(> .col .grid2),
.tside:has(> .col .grid3){grid-template-columns:1fr}
.tside:has(> .col .grid2) > .side,
.tside:has(> .col .grid3) > .side{position:static;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:8px}
.tside:has(> .col .grid2) > .side .box + .box,
.tside:has(> .col .grid3) > .side .box + .box{margin-top:0}
/* если врезок не осталось, колонка исчезает и текст занимает всю ширину */
.tside:not(:has(.side .box)){grid-template-columns:1fr}
.tside:not(:has(.side .box)) > .side{display:none}
.card{display:flex;flex-direction:column}
.card>p:last-child:has(>a:only-child){margin-top:auto;padding-top:10px}
.tside>.col{min-width:0}
.tside>.col>*{max-width:none}
.side{min-width:0;position:sticky;top:96px}
.side .box{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px 22px 20px}
.side .box+.box{margin-top:14px}
.side .lbl{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--copper);margin-bottom:10px}
.side .big{font-family:'Playfair Display',Georgia,serif;font-size:2.2rem;line-height:1;color:var(--wine);margin-bottom:8px}
.side p{font-size:.9rem;line-height:1.55;color:var(--ink-soft);margin:0}
.side .cit{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:.98rem;line-height:1.5;color:var(--ink)}
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
/* каждый прямой ребёнок секции стоит по центру своего контейнера */
section > .wrap > *,
section > .narrow > *{margin-left:0;margin-right:0}
.tside > .col > *,
.split > div > *,
.hero .in > *{margin-left:0;margin-right:0}

/* ЖЕЛЕЗНОЕ ПРАВИЛО ВЫРАВНИВАНИЯ:
   секция целиком по центру, содержимое карточек и колонок по левому краю */
section > .wrap,
section > .narrow{text-align:left}
section .card,
section .box,
section .nail,
section .legend,
section details,
section .pull,
section .q,
section .who,
section li,
section .tm,
section table,
.tside > .col,
.split > div,
.hero .in{text-align:left}
section > .wrap > ul,
section > .narrow > ul,
section > .wrap > ol,
section > .narrow > ol{text-align:left;display:inline-block}

/* ЕДИНАЯ ШКАЛА ОТСТУПОВ: кратно 8, без разнобоя */
section > .wrap > .eyebrow,
section > .narrow > .eyebrow,
.tside > .col > .eyebrow,
.split > div > .eyebrow{margin:0 0 12px}
section > .wrap > h2,
section > .narrow > h2,
.tside > .col > h2,
.split > div > h2{margin:0 0 26px}
section > .wrap > h2 + p,
section > .narrow > h2 + p{margin-top:2px}
section > .wrap > h2 + p,
section > .narrow > h2 + p,
section > .wrap > h2 + .sub,
section > .narrow > h2 + .sub,
.tside > .col > h2 + p,
.split > div > h2 + p{margin-top:0}
section > .wrap > p,
section > .narrow > p{margin:0 0 20px}
.tside > .col > p,
.split > div > p{margin:0 0 20px}
section > .wrap > h3,
section > .narrow > h3,
.tside > .col > h3{margin:32px 0 12px}
section > .wrap > .grid2,
section > .wrap > .grid3,
section > .wrap > .grid5,
section > .wrap > .nails,
section > .wrap > .mosaic,
section > .wrap > .split,
section > .wrap > .tside,
section > .narrow > .grid2,
section > .narrow > .grid3{margin:32px 0 0}
section > .wrap > .btns,
section > .narrow > .btns{margin:32px 0 0;max-width:none}
section > .wrap > :last-child,
section > .narrow > :last-child{margin-bottom:0}
details + details{margin-top:12px}
/* ровный вертикальный ритм: соседние секции на одном фоне не складывают отступы,
   но секция со сменой фона всегда получает свой воздух */
section{padding-top:64px;padding-bottom:64px}
section.dark{padding-top:76px;padding-bottom:76px}
section > .wrap > :last-child,
section > .narrow > :last-child{margin-bottom:0}
section > .wrap > .grid2:last-child,
section > .wrap > .grid3:last-child,
section > .narrow > .grid2:last-child{margin-bottom:0}
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
.logo svg{flex:0 0 42px;width:42px;height:36px}
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
.hero .in{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:110px 24px 92px;text-align:left}
.hero .in>*{max-width:none;margin-left:0;margin-right:0}
.hero .acts{justify-content:flex-start}
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
.nails.nails3{grid-template-columns:repeat(3,1fr)}
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
.fl-link{justify-content:flex-start;display:flex;justify-content:flex-end;align-items:center;gap:8px;padding:7px 16px;color:var(--wine);font-size:.78rem;font-weight:700;letter-spacing:.06em}
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
.poster p{color:rgba(242,237,228,.75);max-width:600px}
.poster .in{text-align:left}
.poster .in>*{margin-left:0;margin-right:0}
.poster .btns{text-align:left}

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
footer .cols{display:grid;grid-template-columns:1.25fr .95fr .95fr .95fr 1.05fr;gap:26px;align-items:start}
@media (max-width:1200px){footer .cols{grid-template-columns:1.2fr 1fr 1fr}}
footer a{font-size:.86rem;line-height:1.5;color:rgba(242,237,228,.8);text-decoration:none;display:block;padding:4px 0;font-size:.9rem}
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
  footer a{font-size:.86rem;line-height:1.5;padding:9px 0}
  section{padding:52px 0}
  .grid2,.grid3,.split,.diagrow{grid-template-columns:1fr}
  .grid5{grid-template-columns:1fr 1fr}
  .grid5>*,.grid5>*:nth-child(4),.grid5>*:nth-child(5){grid-column:auto}
  .nails.nails3{grid-template-columns:1fr 1fr}
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
  .btn{display:block;width:100%;text-align:center}
  .btn+.btn{margin:10px 0 0!important}

  .nails,.nails2,.nails.nails3{grid-template-columns:1fr}
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
        ("/chizhovy2/marafon/", "Модуль III. Марафон", "3 месяца в жизни"),
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
        ("/chizhovy2/gid/", "Гайд бесплатно", "«Кто пишет сценарий твоей&nbsp;жизни»"),
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

FOOTER = """<footer><div class="wrap" style="max-width:1180px">
<div class="cols">
<div>
""" + LOGO_SVG + """
<p style="margin:14px 0 0;color:rgba(242,237,228,.78);font-size:.92rem;line-height:1.6;max-width:330px"><b style="display:block;color:#F2EDE4;font-weight:500;white-space:nowrap">Школа Алексея и&nbsp;Ирины&nbsp;Чижовых</b>Очные тренинги малыми группами и&nbsp;сопровождение до&nbsp;результата.</p>
</div>
<div><h4>Школа</h4>
<a href="/chizhovy2/metod/">Метод</a>
<a href="/chizhovy2/programma/">Программа целиком</a>
<a href="/chizhovy2/modul-1/">Модуль I</a>
<a href="/chizhovy2/modul-2/">Модуль II</a>
<a href="/chizhovy2/marafon/">Модуль III</a>
<a href="/chizhovy2/kak-prohodit/">Как проходит обучение</a>
<a href="/chizhovy2/praktiki/">Ежедневные практики</a>
<a href="/chizhovy2/tehniki-sceny/">Техники сцены</a>
<a href="/chizhovy2/slovar/">Словарь школы</a>
</div>
<div><h4>Истоки метода</h4>
<a href="/chizhovy2/istoki/">Из чего собран метод</a>
<a href="/chizhovy2/istoki/moreno-psihodrama/">Морено и&nbsp;психодрама</a>
<a href="/chizhovy2/istoki/zeland-transerfing/">Зеланд и&nbsp;трансерфинг</a>
<a href="/chizhovy2/istoki/est-transformaciya/">est и Рейнхарт</a>
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
<a href="/chizhovy2/dlya-predprinimatelej/">Предпринимателям</a>
<a href="/chizhovy2/dlya-zhenshchin/">Для женщин</a>
</div>
<div><h4>Начать</h4>
<a href="/chizhovy2/start/">С чего начать</a>
<a href="/chizhovy2/gid/">Гайд школы</a>
<a href="/chizhovy2/stati/">Статьи школы</a>
<a href="/chizhovy2/somneniya/">Частые сомнения</a>
<a href="/chizhovy2/bezopasnost/" style="white-space:nowrap">Границы работы</a>
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
    "Группа остаётся вместе",
    "Алексей и&nbsp;Ирина",
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
    "Отложенный на&nbsp;годы разговор",
    "Сложа руки ты не сидел. В том-то и дело",
    "Собеседование в школу",
    "Создатель реальности",
    "Спокойствие и уверенность",
    "Статьи школы",
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
        # пара должна влезать в самую узкую колонку (342px при шрифте h2 ~29px)
        limit = 18 if tag.lower() in ('h1', 'h2') else 24
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

_BTN_P = re.compile(r'<p(?![^>]*class=)([^>]*)>(\s*<a class="btn)', re.S)
_BTN_P2 = re.compile(r'<p class="((?:(?!btns)[^"])*)"([^>]*)>(\s*<a class="btn)', re.S)

_BTN_BARE = re.compile(
    r'(<div class="(?:narrow|wrap)"[^>]*>(?:(?!</div>).)*?)\n((?:<a class="btn[^>]*>.*?</a>\s*)+)(\n</div>)',
    re.S)

def btns_class(html: str) -> str:
    """Каждая кнопка живёт в контейнере .btns: одно правило выравнивает их все."""
    html = _BTN_P.sub(r'<p class="btns"\1>\2', html)
    html = _BTN_P2.sub(r'<p class="\1 btns"\2>\3', html)
    # кнопки, лежащие прямо в контейнере без обёртки
    html = _BTN_BARE.sub(lambda m: m.group(1) + '\n<p class="btns">' + m.group(2).strip() + '</p>' + m.group(3), html)
    return html

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
<link rel="stylesheet" href="/chizhovy2/site.css?v={CSS_VER}">
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
<div class="floor deep"><b>Этаж эмоции и&nbsp;тела</b><span>здесь хранится запись. И здесь&nbsp;же её&nbsp;переписывают: в&nbsp;живой сцене</span></div>
</div>"""

P = {}

# ================= ГЛАВНАЯ =================
P["index.html"] = ("Настоящие отношения · школа трансформации Чижовых",
"Очный тренинг и три месяца сопровождения: выход из повторяющихся сценариев в отношениях, деле и состоянии.", "glavnaya", f"""
<div class="hero"><div class="bg" style="background-image:url('/chizhovy2/images/site-hero.jpg')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Школа трансформации Алексея и&nbsp;Ирины Чижовых</p>
<h1>Перепиши сценарий своей жизни</h1>
<p class="lead">Очный тренинг и&nbsp;три месяца сопровождения. Перестаёшь ходить по&nbsp;одному и&nbsp;тому же&nbsp;кругу и&nbsp;начинаешь строить отношения, дело и&nbsp;себя по&nbsp;своему выбору.</p>
<div class="acts"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a><a class="btn btn-ghost" href="/chizhovy2/gid/">Читать гайд бесплатно</a></div>
</div></div>

<section><div class="wrap">
<div class="nails">
<div class="nail"><b>16&nbsp;лет</b><span>в&nbsp;практике, залы и&nbsp;группы</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе, каждого знаем по&nbsp;имени</span></div>
<div class="nail"><b>3</b><span>модуля очно, по&nbsp;2,5 и&nbsp;5 дней</span></div>
<div class="nail"><b>3&nbsp;месяца</b><span>сопровождения после тренинга</span></div>
</div>
</div></section>

<section><div class="wrap">
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
<p class="eyebrow">Метод</p>
<h2>Мы работаем с&nbsp;причиной</h2>
<div class="diagrow" style="margin-top:30px">
<div>
<p>Повторы держатся не на&nbsp;характере и не на&nbsp;«таком партнёре». Их&nbsp;крутит событийный круг: старое решение включается быстрее сознания и&nbsp;доигрывает знакомый финал.</p>
<p>Разорвать круг усилием не&nbsp;выходит. Мы&nbsp;разбираем его там, где он&nbsp;записан: в&nbsp;эмоции и&nbsp;теле, в&nbsp;живой групповой работе, где старая сцена проигрывается заново и заканчивается&nbsp;по-другому.</p>
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
<div class="gap">месяц на&nbsp;проверку в жизни</div>
<div class="tm"><div class="c">II</div><div><b>Внутренняя свобода</b><span>5 дней очно</span></div></div>
<div class="gap">ещё 3-5 недель до&nbsp;финала</div>
<div class="tm last"><div class="c">III</div><div><b>Создатель реальности</b><span>3 месяца в&nbsp;жизни, результаты&nbsp;остаются</span></div></div>
</div>
<div class="grid3" style="margin-top:26px">
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/site-m1.jpg" alt="Утро, женщина пишет в дневник у окна" loading="lazy"></div><h3>I. Возвращение к&nbsp;себе</h3><p>Увидеть, что повторяется, во&nbsp;что веришь и&nbsp;откуда это взялось. Первый честный контакт с&nbsp;собой.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-1/">Про первый модуль</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-07.jpg" alt="Группа тренинга в тёплом зале" loading="lazy"></div><h3>II. Внутренняя свобода</h3><p>Страх, вина, обида, чужие ожидания. Меняешь решения, которые управляли тобой годами.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-2/">Про второй модуль</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-10.jpg" alt="Команда выпуска тренинга" loading="lazy"></div><h3>III. Создатель реальности</h3><p>Команда, еженедельные встречи, новые действия и&nbsp;результаты, которые остаются.</p><p style="margin-top:12px"><a href="/chizhovy2/marafon/">Про Марафон</a></p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Что меняется в жизни</p>
<h2>Что <span class="kpm">становится возможным</span></h2>
<div class="grid3" style="margin-top:30px">
<div class="card"><span class="bignum">01</span>{icon('ceiling')}<h3>Дело пробивает потолок</h3><p>Видишь, что именно держало обороты и&nbsp;заставляло цепляться за&nbsp;«стабильный» заработок. Убираешь причину, не&nbsp;симптом.</p></div>
<div class="card"><span class="bignum">02</span>{icon('route','var(--sage-deep)')}<h3>Понимание себя</h3><p>Кто я, куда бегу, почему всё повторяется по&nbsp;спирали. Видишь свои сильные стороны и&nbsp;путь к&nbsp;целям.</p></div>
<div class="card"><span class="bignum">03</span>{icon('lens','var(--sand)')}<h3>Крепкие отношения</h3><p>Выходишь из&nbsp;разрушающих связей и&nbsp;затяжных конфликтов, налаживаешь отношения с&nbsp;близкими.</p></div>
<div class="card"><span class="bignum">04</span>{icon('mountain','var(--sage-deep)')}<h3>Спокойствие и&nbsp;уверенность</h3><p>Внутренняя опора вместо выдержки на&nbsp;зубах. Острые моменты перестают выбивать из&nbsp;седла.</p></div>
<div class="card"><span class="bignum">05</span>{icon('people','var(--sand)')}<h3>Своё окружение</h3><p>Люди, с&nbsp;которыми можно в&nbsp;разведку и в&nbsp;дело. Навык слышать, договариваться, играть вместе.</p></div>
<div class="card"><span class="bignum">06</span>{icon('sunrise')}<h3>От понимания к&nbsp;действию</h3><p>Перестаёшь откладывать жизнь на&nbsp;потом. Путь от&nbsp;идеи до&nbsp;реализации сокращается в&nbsp;разы.</p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Как это выглядит</p>
<h2>Наши группы</h2>
<p class="sub">Это живые выпуски школы. Малые группы, очная работа, люди, которых мы&nbsp;знаем по&nbsp;именам и&nbsp;историям.</p>
<div class="mosaic" style="margin-top:28px">
<div class="ph"><img src="/chizhovy2/images/real/real-05.jpg" alt="Выпуск группы тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-06.jpg" alt="Группа тренинга в зале" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-01.jpg" alt="Группа у камина с сертификатами" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-11.jpg" alt="Команда участников" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-13.jpg" alt="Выпуск модуля" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-04.jpg" alt="Работа в зале" loading="lazy"></div>
</div>
</div></section>

<section class="dark" style="padding:0"><div class="wrap" style="padding-top:76px;padding-bottom:76px">
<div class="pull"><div class="q">«Появилось ощущение, что вижу себя на&nbsp;всей шахматной доске, а не в&nbsp;одной клетке.»</div><div class="who">Участник тренинга, предприниматель</div></div>
<div class="pull"><div class="q">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше.»</div><div class="who">Участник второго модуля</div></div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Читать истории целиком</a></p>
</div></section>

<section><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Ведущие</p>
<h2>Алексей и&nbsp;Ирина</h2>
<p>Алексей: коуч с&nbsp;сертификацией ICF, 16&nbsp;лет практики, триатлет. Ирина: трансформационный тренер, шесть лет готовилась к&nbsp;этому формату, работает на&nbsp;глубине, которую участники вспоминают&nbsp;годами.</p>
<p>Школу ведут Алексей и&nbsp;Ирина. Вместе 17&nbsp;лет: быт, кризисы и&nbsp;выход из&nbsp;них прошли сами.</p>
<p class="btns" style="margin-top:20px"><a class="btn btn-ghost" href="/chizhovy2/vedushchie/">Познакомиться</a></p>
</div>
<div class="ph"><img src="/chizhovy2/images/real/portret.jpg" alt="Алексей и Ирина Чижовы, портрет" loading="lazy"></div>
</div>
</div></section>

<section><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Истоки метода</p>
<h2 style="font-size:clamp(1.55rem,4vw,2.3rem)">Рассказываем, из чего собран метод</h2>
<p>Сильной работе нечего прятать. Мы&nbsp;открыто называем школы и&nbsp;авторов, на&nbsp;которых выросли: психодрама Морено, трансерфинг Зеланда, тренинги погружения от&nbsp;est, практика состояния Годдарда. И&nbsp;показываем, что взяли, что переработали за 16&nbsp;лет и&nbsp;почему это работает с&nbsp;точки зрения науки.</p>
<p class="btns" style="margin-top:20px"><a class="btn btn-ghost" href="/chizhovy2/istoki/">Разобрать истоки</a></p>
</div>
<div class="linklist">
<a href="/chizhovy2/istoki/moreno-psihodrama/">{ICONS['people']}<div><b>Якоб Морено и&nbsp;психодрама</b><span>живая сцена вместо разговоров о&nbsp;жизни</span></div></a>
<a href="/chizhovy2/istoki/zeland-transerfing/">{ICONS['loop']}<div><b>Вадим Зеланд и&nbsp;трансерфинг</b><span>маятники, важность, зеркало мира</span></div></a>
<a href="/chizhovy2/istoki/est-transformaciya/">{ICONS['flame']}<div><b>est и&nbsp;«Трансформация» Рейнхарта</b><span>откуда пошли тренинги погружения</span></div></a>
<a href="/chizhovy2/istoki/goddard/">{ICONS['sunrise']}<div><b>Невилл Годдард</b><span>состояние, в котором уже получилось</span></div></a>
<a href="/chizhovy2/istoki/nauka/">{ICONS['book']}<div><b>Наука за&nbsp;методом</b><span>ЛеДу, Гоулман, Болте Тейлор,&nbsp;Голвитцер</span></div></a>
</div>
</div>
</div></section>

<section><div class="wrap">
<div class="poster"><div class="bg" style="background-image:url('/chizhovy2/images/site-dark.jpg')"></div><div class="veil"></div>
<div class="in">
<p class="eyebrow">Ближайшие даты</p>
<h3>Модуль II. Внутренняя&nbsp;свобода</h3>
<p>Пять дней, после которых страх, вина и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p>
<p style="margin-top:24px"><a class="btn btn-copper" href="/chizhovy2/sessiya/">Занять место</a></p>
</div></div>
</div></section>

<section><div class="narrow">
<h2>Начни с разговора</h2>
<p class="sub" style="margin:0 0 26px">Собеседование в&nbsp;школу: разговор о&nbsp;твоей ситуации и&nbsp;честный ответ, чем школа может помочь. Для читателей сайта&nbsp;бесплатно.</p>
<a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a>
</div></section>
""")

# ================= МЕТОД =================
P["metod/index.html"] = ("Метод школы · Настоящие отношения",
"Событийный круг, состояние и психодрама: подробный разбор, как устроена перезапись сценариев.", "metod", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-metod.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Метод школы</p><h1>Всё начинается <span class="kp">с состояния</span></h1>
<p class="lead">Мы не&nbsp;учим «правильно общаться» и не&nbsp;выдаём мотивацию на&nbsp;неделю. Мы&nbsp;находим старую запись, по&nbsp;которой идут твои реакции, и&nbsp;помогаем переписать её&nbsp;там, где она хранится. Ниже метод разобран по&nbsp;винтикам.</p>
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
<div class="nail"><b>90&nbsp;сек</b><span>живёт химия эмоции, если её не&nbsp;кормить (Болте&nbsp;Тейлор)</span></div>
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
<p style="margin-top:18px">Разорвать круг усилием не&nbsp;выходит: он&nbsp;быстрее сознания. Его размыкают в точке&nbsp;3. Там живёт старое&nbsp;решение.</p>
</div>
</div>
</div></section>

<section><div class="narrow">
<p class="eyebrow">Почему разговоры не помогают</p>
<h2>Запись лежит этажом ниже</h2>
<p>Книги, курсы и&nbsp;беседы стучатся в&nbsp;думающий этаж. Запись лежит этажом ниже: в&nbsp;эмоции и&nbsp;теле. Договариваться с&nbsp;ней словами то&nbsp;же самое, что уговаривать плёнку звучать иначе. Поэтому понимание копится годами, а&nbsp;реакции остаются прежними.</p>
{floors}
</div></section>

<section><div class="wrap">
<p class="eyebrow">Инструмент №1</p>
<h2>Психодрама: старое решение меняют прямо в&nbsp;сцене</h2>
<p class="sub">Метод психиатра Якоба Морено. Сто лет практики по&nbsp;всему миру. Человек не&nbsp;рассказывает о&nbsp;ситуации, а&nbsp;возвращается в неё и&nbsp;меняет решение прямо внутри сцены.</p>
<div class="split" style="margin-top:30px">
<div class="ph"><img src="/chizhovy2/images/metod-scena.jpg" alt="Сцена психодрамы: участник в центре, группа вокруг" loading="lazy"></div>
<div>
<p>Со&nbsp;стороны это похоже на&nbsp;живой театр без сценария. Изнутри это самая точная работа, которую мы&nbsp;знаем: сцена достаёт запись целиком, с&nbsp;эмоцией, телом и&nbsp;тем самым решением.</p>
<p>Морено называл результат спонтанностью: способностью дать новый ответ на&nbsp;старую ситуацию. По-нашему: момент, когда пульт возвращается к&nbsp;хозяину.</p>
<p style="margin-top:14px"><a href="/chizhovy2/tehniki-sceny/">Техники сцены с&nbsp;разбором</a> · <a href="/chizhovy2/istoki/moreno-psihodrama/">Про Морено и&nbsp;психодраму</a></p>
</div>
</div>
<div class="grid5" style="margin-top:30px" id="psy-steps">
<div class="card"><span class="bignum">1</span><h3>Запрос</h3><p>Называешь сцену, которая держит: ссора, разговор, который откладываешь годами, момент из&nbsp;детства.</p></div>
<div class="card"><span class="bignum">2</span><h3>Сцена</h3><p>Участники группы становятся героями твоей истории. Пространство зала превращается в ту&nbsp;кухню, тот кабинет, тот&nbsp;двор.</p></div>
<div class="card"><span class="bignum">3</span><h3>Проживание</h3><p>Говоришь из&nbsp;себя настоящего то, что тогда осталось несказанным. Тело включается раньше слов. Так и&nbsp;надо.</p></div>
<div class="card"><span class="bignum">4</span><h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место другого: отца, партнёра, себя-ребёнка. Сцена, которую ты&nbsp;носил годами, впервые видна целиком.</p></div>
<div class="card"><span class="bignum">5</span><h3>Новое решение</h3><p>Прямо в&nbsp;сцене принимаешь другое решение. Теперь оно записано так&nbsp;же глубоко, как старое: телом и&nbsp;эмоцией.</p></div>
</div>
</div></section>

<section><div class="wrap">
<div class="split">
<div>
<p class="eyebrow">Пустой стул</p>
<h2>Отложенный на&nbsp;годы разговор</h2>
<p>Иногда сцена строится вокруг пустого стула. На&nbsp;нём сидит тот, с&nbsp;кем так и не&nbsp;поговорил: отец, бывший, ты&nbsp;сам из&nbsp;прошлого. Разговор случается сейчас, и&nbsp;тело отпускает то, что держало.</p>
<p>После таких процессов участники говорят: «снял рюкзак», «стало легче дышать». Это буквальные ощущения: напряжение, которое тело держало годами, находит выход.</p>
</div>
<div class="ph"><img src="/chizhovy2/images/metod-stul.jpg" alt="Пустой стул в луче тёплого света" loading="lazy"></div>
</div>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Вокруг сцены</p>
<h2>Что ещё меняет старую запись</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('flame','var(--copper)')}<h3>Работа с&nbsp;телом</h3><p>Запись живёт в&nbsp;мышцах и&nbsp;дыхании. Телесные практики достают её&nbsp;там, куда слова не&nbsp;доходят, и&nbsp;учат выходить из&nbsp;захвата за те&nbsp;самые 90&nbsp;секунд.</p></div>
<div class="card">{icon('gear','var(--copper)')}<h3>Разбор вины и&nbsp;ответственности</h3><p>Вина сливает энергию и&nbsp;зовёт наказание. Ответственность возвращает силу. Разницу учимся чувствовать телом, а не запоминать&nbsp;словами.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Группа как зеркало</h3><p>10-20 человек, у&nbsp;которых те&nbsp;же боли под другими фамилиями. В&nbsp;чужой сцене узнаёшь свою запись быстрее, чем в&nbsp;своей.</p></div>
<div class="card">{icon('sunrise','var(--copper)')}<h3>Ежедневная практика</h3><p>После модулей: утренний фокус дня, вечерние открытия и&nbsp;благодарности. Девяносто дней Марафона делают новый ответ&nbsp;привычкой.</p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Наука за&nbsp;методом</p>
<h2>Кто это проверил до&nbsp;нас</h2>
<div class="grid2" style="margin-top:26px">
<div class="card white"><h3>Джозеф ЛеДу · нейробиолог</h3><p>Показал «короткий путь» страха: миндалина получает сигнал за 12&nbsp;миллисекунд, раньше думающей коры. Вот почему реакция обгоняет&nbsp;намерение.</p></div>
<div class="card white"><h3>Дэниел Гоулман · психолог</h3><p>Описал «захват»: в&nbsp;момент вспышки разумная часть мозга приглушается. «Взять себя в&nbsp;руки» тогда физически нечем.</p></div>
<div class="card white"><h3>Джилл Болте Тейлор ·&nbsp;нейроанатом</h3><p>Правило 90&nbsp;секунд: химия эмоции сама уходит из&nbsp;крови за&nbsp;полторы минуты, если не&nbsp;подкармливать её&nbsp;мыслями по&nbsp;кругу.</p></div>
<div class="card white"><h3>Якоб Морено · психиатр</h3><p>Создал психодраму и&nbsp;доказал: новый ответ, прожитый в&nbsp;сцене телом и&nbsp;эмоцией, записывается так&nbsp;же глубоко, как детское решение.</p></div>
</div>
<p style="margin-top:18px"><a href="/chizhovy2/istoki/nauka/">Все пять открытий с&nbsp;разбором: наука за&nbsp;методом</a></p>
<div class="pull" style="margin-top:24px"><div class="q">«Труднее всего было принять точку&nbsp;А. Принять, что мир это зеркало, и&nbsp;всё, что со&nbsp;мной происходит, я&nbsp;транслирую сам.»</div><div class="who">Участник тренинга</div></div>
</div></section>

<section><div class="wrap">
<div class="split" style="margin-bottom:44px">
<div class="ph"><img src="/chizhovy2/images/ob-zal-krug.jpg" alt="Зал со стульями по кругу" loading="lazy"></div>
<div>
<p class="eyebrow">Формат работы</p>
<h2 style="font-size:1.9rem">Как устроен зал</h2>
<p>Небольшая группа, стулья по&nbsp;кругу, двое ведущих. Ни&nbsp;рядов, ни&nbsp;кафедры, ни&nbsp;мест «получше»: каждый видит каждого, и&nbsp;ведущие сидят в&nbsp;том&nbsp;же круге.</p>
</div>
</div>
<p class="eyebrow">Три опоры результата</p>
<h2>Почему изменения остаются</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('layers')}<h3>Глубина</h3><p>Очные модули по&nbsp;несколько дней: время дойти до&nbsp;причины, а не снять&nbsp;симптом.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Группа</h3><p>Малая группа, каждого знаем по&nbsp;имени. В&nbsp;чужих историях узнаёшь свою, в&nbsp;своих перестаёшь быть один.</p></div>
<div class="card">{icon('calendar','var(--sand)')}<h3>Практика</h3><p>Три месяца сопровождения: новые реакции закрепляются действиями в&nbsp;обычной жизни, пока не станут&nbsp;своими.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Кому метод не&nbsp;подойдёт</h2>
<p>Честно: тем, кто ищет волшебную таблетку за&nbsp;вечер. Тем, кто пока не&nbsp;готов работать в&nbsp;группе. И&nbsp;тем, кому сейчас нужна медицинская помощь, а не&nbsp;тренинг: об&nbsp;этом мы&nbsp;говорим прямо и&nbsp;подсказываем, куда идти.</p>
<p>Для всех остальных вход один: собеседование. Час честного разговора, где вместе решаем, твой это метод или нет. Для пришедших с&nbsp;сайта бесплатно.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/programma/" style="margin-left:8px">Смотреть программу</a></p>
</div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-okno.jpg" alt="Вечер, который повторяется" loading="lazy"></div>
<div>
<p class="eyebrow">Почему это не&nbsp;лечится разговором</p>
<h2 style="font-size:1.9rem">Знакомый вечер</h2>
<p>Сцена знакомая: разговор закончился, дверь хлопнула, ты&nbsp;сидишь и&nbsp;прокручиваешь по&nbsp;кругу. Умом всё понятно уже давно. Меняется только тогда, когда доходишь до&nbsp;решения, которое всё это держит.</p>
</div>
</div>
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
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/site-m1.jpg" alt="Модуль I" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль I · 2,5 дня</p><h3>Возвращение к&nbsp;себе</h3><p>Видишь свои повторяющиеся паттерны, установки и их&nbsp;источники. Результат: осознанность и&nbsp;первый честный контакт с&nbsp;собой.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-1/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-07.jpg" alt="Модуль II" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль II · 5 дней</p><h3>Внутренняя свобода</h3><p>Работа со&nbsp;страхом, виной, обидой и&nbsp;зависимостью от&nbsp;чужого мнения. Дальше приходят сила и&nbsp;спокойствие.</p><p style="margin-top:12px"><a href="/chizhovy2/modul-2/">Подробнее</a></p></div>
<div class="card white"><div class="ph" style="aspect-ratio:4/3;margin-bottom:18px"><img src="/chizhovy2/images/real/real-13.jpg" alt="Модуль III" loading="lazy"></div><p class="eyebrow" style="margin-bottom:6px">Модуль III · 3 месяца</p><h3>Создатель реальности</h3><p>Три месяца в&nbsp;обычной жизни: команда, ежедневная практика, результаты в&nbsp;деле и&nbsp;отношениях. Это и&nbsp;есть Марафон.</p><p style="margin-top:12px"><a href="/chizhovy2/marafon/">Подробнее</a></p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Как попасть на программу</h2>
<div class="card white" style="margin-top:20px">{icon('speech')}<h3>Начало:&nbsp;собеседование</h3><p>Разговор о&nbsp;твоей ситуации. Честно решаем, подходит&nbsp;ли тебе школа. Для пришедших с&nbsp;этого сайта собеседование бесплатное.</p></div>
<div class="card white" style="margin-top:12px">{icon('people','var(--sage-deep)')}<h3>Формат</h3><p>Очные модули в&nbsp;Москве малой группой 10-20 человек, между погружениями 3-5 недель с&nbsp;поддержкой, после третьей ступени три месяца сопровождения.</p></div>
<div class="card white" style="margin-top:12px">{icon('target','var(--sand)')}<h3>Для кого</h3><p>Для взрослых людей, готовых брать ответственность: предприниматели, руководители, пары. Участников отбираем на&nbsp;собеседовании. Глубина требует&nbsp;готовности.</p></div>
</div></section>

<section><div class="narrow">
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


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как устроен день</p>
<h2>Из чего складывается модуль</h2>
<p>День на&nbsp;модуле идёт длинными блоками, без пар по&nbsp;сорок минут. Утро начинается с&nbsp;круга: каждый говорит, с&nbsp;чем пришёл сегодня и&nbsp;что изменилось со&nbsp;вчера. Дальше ведущие берут одну ситуацию из&nbsp;зала и&nbsp;разбирают её&nbsp;целиком, шаг за&nbsp;шагом. Остальные не&nbsp;зрители: часть встаёт в&nbsp;сцену, часть смотрит и&nbsp;узнаёт своё.</p>
<p>Перерывы короткие и&nbsp;общие, обедают все вместе. Это не&nbsp;мелочь: половина разговоров, которые люди потом называют переломными, случается именно за&nbsp;столом, а&nbsp;не&nbsp;в&nbsp;зале.</p>
<p>Вечер закрывает шеринг. Каждый называет своё открытие дня вслух, при всех. Тот, кто отмолчался, чаще всего наутро возвращается к&nbsp;тому&nbsp;же месту: невысказанное держится крепче высказанного.</p>
<h3 style="margin-top:26px">Что берут с&nbsp;собой</h3>
<p>Удобную одежду, воду и&nbsp;тетрадь. Телефоны в&nbsp;зале выключены: это правило, а&nbsp;не&nbsp;пожелание. Записи ведут от&nbsp;руки, потому что рука успевает за&nbsp;мыслью медленнее и&nbsp;оставляет главное.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Размер группы</div><div class="big">10-20</div><p>Столько человек в&nbsp;зале. Больше нельзя: ведущие держат каждого в&nbsp;поле внимания и&nbsp;знают по&nbsp;имени.</p></div>
<div class="box"><div class="lbl">Сколько длится</div><div class="big">2,5 и 5</div><p>Дней очно на&nbsp;первом и&nbsp;втором модуле. Третий идёт три месяца в&nbsp;обычной жизни.</p></div>
<div class="box"><div class="lbl">Телефоны</div><p>Выключены на&nbsp;всё время работы зала. Возвращаются в&nbsp;перерывах.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-lestnica.jpg" alt="Три ступени старой лестницы" loading="lazy"></div>
<div>
<p class="eyebrow">Чем этот путь отличается</p>
<h2 style="font-size:1.9rem">Почему три ступени, а&nbsp;не&nbsp;один интенсив</h2>
<p>За&nbsp;два дня можно увидеть свою запись. Переписать её&nbsp;за&nbsp;два дня нельзя: старое решение держится не&nbsp;на&nbsp;понимании, а&nbsp;на&nbsp;теле и&nbsp;привычке реагировать. Поэтому после первого модуля идут недели на&nbsp;проверку в&nbsp;жизни, потом второй, потом три месяца команды.</p>
<p>Люди, которые прошли только первую ступень, обычно говорят «было сильно». Те, кто дошёл до&nbsp;конца, говорят другое: называют конкретные вещи, которые изменились в&nbsp;деньгах, в&nbsp;доме, в&nbsp;теле. Разница не&nbsp;в&nbsp;мотивации, а&nbsp;в&nbsp;длине дистанции.</p>
</div>
</div>
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
"Два с половиной дня: увидеть, что повторяется, и откуда это взялось.", "modul-1", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-m1.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль I · два с&nbsp;половиной дня</p><h1>Возвращение к&nbsp;себе</h1>
<p class="lead">Первый модуль отвечает на&nbsp;вопрос, с&nbsp;которого начинается любой сдвиг: что со&nbsp;мной происходит на&nbsp;самом деле и&nbsp;откуда это&nbsp;взялось.</p></div></div>

<section><div class="narrow">
<h2>Что происходит за&nbsp;эти дни</h2>
<p>Пятничный вечер, суббота и&nbsp;воскресенье. Погружение начинается с&nbsp;эмоционального входа в&nbsp;пространство тренинга: телефоны в&nbsp;сторону, маски снимаются постепенно и&nbsp;сами.</p>
<div class="card white" style="margin:18px 0 12px">{icon('book')}<h3>Видишь, что повторяется</h3><p>Повторяющиеся реакции, роли и&nbsp;установки, из&nbsp;которых соткан твой день: где ты&nbsp;терпишь, где убегаешь, где стараешься казаться.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('route','var(--sage-deep)')}<h3>Находишь, откуда это взялось</h3><p>В&nbsp;живых процессах видно, где было принято старое решение и&nbsp;чью интонацию ты до&nbsp;сих пор носишь как&nbsp;свою.</p></div>
<div class="card white">{icon('lens','var(--sand)')}<h3>Снова слышишь себя</h3><p>К&nbsp;воскресному вечеру появляется то, что участники называют «впервые за&nbsp;годы услышал себя». Отсюда начинается настоящая работа.</p></div>
<div class="pull"><div class="q">«Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка колоссальная.»</div><div class="who">Участник первого модуля</div></div>
<p><strong>Результат модуля: осознанность.</strong> Ты&nbsp;видишь свою запись. Развидеть её&nbsp;уже не&nbsp;получится, и&nbsp;это лучшее, что могло&nbsp;случиться.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">По часам</p>
<h2>Как устроены два с&nbsp;половиной дня</h2>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">1</span>{icon('speech')}<h3>Вечер пятницы</h3><p>Знакомство группы и&nbsp;вход в&nbsp;пространство. Первые честные ответы на&nbsp;вопрос «зачем я&nbsp;здесь». К&nbsp;концу вечера зал перестаёт быть комнатой незнакомых людей.</p></div>
<div class="card"><span class="bignum">2</span>{icon('people','var(--sage-deep)')}<h3>Суббота</h3><p>Самый длинный день: живые процессы, работа в&nbsp;парах и&nbsp;группе, первые сцены. Здесь обычно и&nbsp;случается то, ради чего люди приезжают.</p></div>
<div class="card"><span class="bignum">3</span>{icon('sunrise','var(--sand)')}<h3>Воскресенье</h3><p>Сборка: что увидел, что с&nbsp;этим делать в&nbsp;понедельник. Договорённости с&nbsp;собой на&nbsp;недели на проверку в жизни до&nbsp;второго модуля.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>С чем работают на&nbsp;первом модуле</h2>
<p>Материал приносишь ты: свою реальную жизнь, а не&nbsp;учебные задачи. Чаще всего в&nbsp;зале звучат такие темы.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('loop')}<h3>Повторяющиеся ссоры</h3><p>Один и тот&nbsp;же сюжет с&nbsp;партнёром, родителями или на&nbsp;работе. Смотрим, в&nbsp;какой точке круг замыкается.</p></div>
<div class="card">{icon('shield','var(--sage-deep)')}<h3>Надоевшие роли</h3><p>Сильный, удобная, спасатель, тот, кто всегда справится. Откуда роль взялась и&nbsp;что будет, если её&nbsp;снять.</p></div>
<div class="card">{icon('book','var(--sand)')}<h3>Установки из&nbsp;детства</h3><p>«Просить стыдно», «злиться опасно», «я&nbsp;сам». Находим, чьим голосом они сказаны впервые.</p></div>
<div class="card">{icon('flame')}<h3>Замороженные чувства</h3><p>Место, где когда-то было больно и&nbsp;пришлось закрыться. Оживляем бережно и по&nbsp;шагам.</p></div>
</div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что забирают с&nbsp;собой</h2>
<p>Первый модуль не&nbsp;решает всё: он&nbsp;открывает глаза и&nbsp;даёт первые инструменты. Дальше идут недели, когда увиденное проверяется обычной жизнью, а за&nbsp;ними <a href="/chizhovy2/modul-2/" style="color:#D08A5F">второй модуль</a>, где старые решения переписываются.</p>
<div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>2,5 дня</b><span>вечер пятницы плюс выходные, без отрыва от&nbsp;работы</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе, каждого знаем по&nbsp;имени</span></div>
<div class="nail"><b>3-5 недель</b><span>интеграции до&nbsp;следующего модуля</span></div>
</div>
</div></section>


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Чего ждать по-честному</p>
<h2>Как это переживается изнутри</h2>
<p>Первые часы почти все сидят закрытые. Смотрят, оценивают, прикидывают, во&nbsp;что ввязались. Так у&nbsp;большинства, и&nbsp;ведущим это знакомо: никто не&nbsp;торопит и&nbsp;не&nbsp;тянет говорить силой.</p>
<p>Перелом обычно случается, когда кто-то в&nbsp;зале первым рассказывает своё без прикрас. Не&nbsp;красиво, а&nbsp;как есть: про долги, про молчание дома, про страх, что так и&nbsp;будет всегда. После этого зал меняется за&nbsp;полчаса, и&nbsp;говорить начинают остальные.</p>
<p>Дальше становится честно и&nbsp;местами тяжело. Люди плачут, злятся, вспоминают то, что не&nbsp;трогали годами. Один участник записал после первого дня коротко: «Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка колоссальная». Никого не&nbsp;вытаскивают силой: глубину человек выбирает сам.</p>
<p>К&nbsp;вечеру воскресенья состояние обычно тихое и&nbsp;ясное. Не&nbsp;эйфория, а&nbsp;спокойствие человека, который перестал спорить с&nbsp;очевидным.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Формат</div><div class="big">2,5 дня</div><p>Вечер пятницы, суббота и&nbsp;воскресенье целиком. Очно, малой группой.</p></div>
<div class="box"><div class="lbl">Что нужно взять</div><p>Удобную одежду, воду, тетрадь. Телефоны в&nbsp;зале выключены.</p></div>
<div class="box"><div class="lbl">Первый шаг</div><p>Собеседование: смотрим, твоя&nbsp;ли это задача, и&nbsp;отвечаем на&nbsp;вопросы.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-doroga.jpg" alt="Дорога через поля на рассвете" loading="lazy"></div>
<div>
<p class="eyebrow">После модуля</p>
<h2 style="font-size:1.9rem">Что происходит в&nbsp;первые недели</h2>
<p>Домой человек уезжает с&nbsp;одной ясной картиной: где он&nbsp;на&nbsp;самом деле и&nbsp;по&nbsp;какому кругу ходит. Первую неделю это держится само, дальше жизнь начинает возвращать в&nbsp;привычную колею: те&nbsp;же люди, тот&nbsp;же рабочий чат, те&nbsp;же поводы среагировать по-старому.</p>
<p>Поэтому между модулями идут недели на&nbsp;проверку в&nbsp;жизни, а&nbsp;не&nbsp;сразу следующий заезд. Увиденное надо попробовать руками: сказать то, что раньше проглатывал, не&nbsp;среагировать там, где всегда срывался, довести до&nbsp;конца то, что бросал.</p>
<p>С&nbsp;этими попытками человек и&nbsp;приходит на&nbsp;второй модуль. Разбирают уже не&nbsp;теорию, а&nbsp;живые случаи последних недель.</p>
</div>
</div>
</div></section>





<section><div class="wrap">
<p class="eyebrow">По часам</p>
<h2>Как проходит суббота</h2>
<p class="sub">Самый плотный день модуля. Ниже по&nbsp;шагам, без общих слов.</p>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('sunrise','var(--copper)')}<h3>10:00 · Круг</h3><p>Каждый говорит, с&nbsp;чем пришёл сегодня. Коротко, по&nbsp;одной фразе. Ведущие слушают, что повторяется у&nbsp;разных людей: с&nbsp;этого начинается день.</p></div>
<div class="card">{icon('lens')}<h3>11:00 · Разбор</h3><p>Берут одну живую ситуацию из&nbsp;зала и&nbsp;доходят до&nbsp;конца: где включилась старая реакция, какое решение за&nbsp;ней стоит и&nbsp;сколько лет оно работает.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>14:00 · Работа в&nbsp;парах</h3><p>Двое разбирают ситуации друг друга по&nbsp;схеме, которую только что видели. Здесь впервые пробуют говорить прямо, без смягчений.</p></div>
<div class="card">{icon('route')}<h3>16:00 · Сцена</h3><p>Ситуацию выносят в&nbsp;центр зала. Участники встают на&nbsp;роли людей из&nbsp;этой истории и&nbsp;говорят их&nbsp;словами.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>19:00 · Тишина</h3><p>Полчаса без разговоров. Не&nbsp;медитация: время, чтобы улеглось поднятое за&nbsp;день.</p></div>
<div class="card">{icon('speech','var(--copper)')}<h3>20:00 · Шеринг</h3><p>Каждый называет своё открытие дня вслух, при всех. Тот, кто отмолчался, наутро чаще всего возвращается к&nbsp;тому&nbsp;же месту.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Частые вопросы</p>
<h2>О чём спрашивают перед первым модулем</h2>
<details><summary>Меня заставят рассказывать личное при всех?</summary><p>Нет. Глубину человек выбирает сам, и&nbsp;это правило зала, а&nbsp;не&nbsp;вежливая формулировка. Можно просидеть весь модуль наблюдателем: часть людей так и&nbsp;делает в&nbsp;первый день, а&nbsp;включается на&nbsp;второй.</p></details>
<details><summary>А если я&nbsp;расплачусь при чужих людях?</summary><p>Так бывает почти у&nbsp;каждого второго. В&nbsp;зале это обычное дело: никто не&nbsp;утешает и&nbsp;не&nbsp;отводит глаза, потому что все понимают, зачем сюда пришли.</p></details>
<details><summary>Нужна подготовка, книги, дневник?</summary><p>Ничего не&nbsp;нужно. Приезжай как есть. Тетрадь дадим, остальное появится по&nbsp;ходу.</p></details>
<details><summary>Я&nbsp;уже был на&nbsp;тренингах, будет то&nbsp;же самое?</summary><p>Скорее всего нет. Здесь не&nbsp;мотивируют и&nbsp;не&nbsp;дают техник «на&nbsp;каждый день». Работают с&nbsp;одним: где именно ты&nbsp;принимаешь одно и&nbsp;то&nbsp;же решение и&nbsp;что оно тебе стоит.</p></details>
<details><summary>Можно приехать с&nbsp;партнёром?</summary><p>Можно, и&nbsp;многие приезжают. Работать будете отдельно, каждый со&nbsp;своей стороной. Для&nbsp;пар есть <a href="/chizhovy2/para/">отдельный формат</a>.</p></details>
</div>
<aside class="side">
<div class="box"><div class="lbl">Начало</div><div class="big">19:00</div><p>Вечер пятницы. Заканчиваем в&nbsp;воскресенье вечером.</p></div>
<div class="box"><div class="lbl">Перерывы</div><p>Обед и&nbsp;два коротких. Едят все вместе: за&nbsp;столом случается половина важных разговоров.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-telefon.jpg" alt="Телефоны на входе" loading="lazy"></div>
<div>
<p class="eyebrow">Правило зала</p>
<h2 style="font-size:1.9rem">Телефоны на&nbsp;входе</h2>
<p>Первое, что делают в&nbsp;зале, это выключают телефоны и&nbsp;складывают их&nbsp;в&nbsp;коробку. Не&nbsp;ради дисциплины: за&nbsp;три дня без экрана возвращается способность держать внимание дольше минуты, и&nbsp;без неё вся остальная работа не&nbsp;складывается.</p>
</div>
</div>
</div></section>

<section><div class="narrow">
<h2>Кто приезжает на&nbsp;первый модуль</h2>
<p>Люди, у&nbsp;которых снаружи в&nbsp;основном порядок, а&nbsp;внутри давно не&nbsp;складывается: <a href="/chizhovy2/dlya-predprinimatelej/">предприниматели</a> в&nbsp;усталости, <a href="/chizhovy2/para/">пары</a> в&nbsp;тихом кризисе, <a href="/chizhovy2/dlya-zhenshchin/">женщины</a>, которые устали жить в&nbsp;режиме ожидания. Возраст обычно от&nbsp;тридцати до&nbsp;пятидесяти.</p>
<p>Специальной подготовки не&nbsp;нужно: ни&nbsp;книг, ни&nbsp;опыта терапии, ни&nbsp;умения красиво говорить о&nbsp;чувствах. Нужна готовность три дня быть честным с&nbsp;собой. Как проходит вход в&nbsp;школу и&nbsp;почему через разговор, описано на&nbsp;странице <a href="/chizhovy2/sessiya/">собеседования</a>.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Начать с&nbsp;собеседования</a> <a class="btn btn-ghost" href="/chizhovy2/modul-2/" style="margin-left:8px">Дальше: Модуль II</a></p>
</div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-tetrad.jpg" alt="Тетрадь, с которой всё начинается" loading="lazy"></div>
<div>
<p class="eyebrow">Первые записи</p>
<h2 style="font-size:1.9rem">Тетрадь и&nbsp;первые записи</h2>
<p>На&nbsp;первом модуле много пишут от&nbsp;руки. Не&nbsp;конспект ведущих, а&nbsp;свои открытия: что повторяется, откуда пришло, где именно ты&nbsp;принимаешь одно и&nbsp;то&nbsp;же решение. Эти листы люди хранят годами.</p>
</div>
</div>
</div></section>

""")

# ================= МОДУЛЬ 2 =================
P["modul-2/index.html"] = ("Модуль II. Внутренняя свобода · Настоящие отношения",
"Пять дней глубокой работы: страх, вина, обида, внутренняя опора.", "modul-2", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-dark.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль II · пять дней</p><h1>Внутренняя свобода</h1>
<p class="lead">Самый глубокий модуль школы. Пять дней, после которых вина, тревога и&nbsp;чужие ожидания перестают решать за&nbsp;тебя.</p></div></div>

<section><div class="narrow">
<h2>С чем работаем</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('flame')}<h3>Страх и&nbsp;важность</h3><p>Разбираем, как раздутая ставка парализует действия, и&nbsp;возвращаем способность выбирать спокойно.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Вина и&nbsp;ответственность</h3><p>Первая сливает энергию и&nbsp;притягивает наказание, вторая возвращает силу. Учимся различать их&nbsp;телом.</p></div>
<div class="card">{icon('loop','var(--sand)')}<h3>Обида</h3><p>Старые обиды держат сценарии годами. Проживаем их до&nbsp;конца в&nbsp;безопасном пространстве группы.</p></div>
<div class="card">{icon('mountain')}<h3>Внутренняя опора</h3><p>Собираем состояние, в&nbsp;котором ты не&nbsp;зависишь от&nbsp;оценки, настроения партнёра и&nbsp;погоды на&nbsp;рынке.</p></div>
</div>
<div class="pull"><div class="q">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше.»</div><div class="who">Участник второго модуля</div></div>
<p><strong>Результат модуля: сила, спокойствие, ясность.</strong> Плюс инструменты, которыми ты&nbsp;дальше пользуешься сам: тело помнит, как выходить из&nbsp;захвата.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Пять дней</p>
<h2>Почему именно столько</h2>
<p class="sub">За выходные психика едва успевает открыться, а&nbsp;перестроиться уже нет. Пять дней подряд дают то, ради чего существует формат погружения: защиты снимаются, и&nbsp;работа идёт на&nbsp;той глубине, куда обычная жизнь не&nbsp;пускает.</p>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">1-2</span>{icon('layers')}<h3>Первые дни</h3><p>Разгон и&nbsp;снятие брони. Здесь становится видно, сколько сил уходило на&nbsp;поддержание образа «у&nbsp;меня всё хорошо».</p></div>
<div class="card"><span class="bignum">3</span>{icon('flame','var(--sage-deep)')}<h3>Третий день</h3><p>Самый плотный. Обычно именно тут человек доходит до&nbsp;решения, которое принял двадцать или тридцать лет назад, и&nbsp;встречается с&nbsp;ним лицом к&nbsp;лицу.</p></div>
<div class="card"><span class="bignum">4-5</span>{icon('mountain','var(--sand)')}<h3>Последние дни</h3><p>Сборка нового: опора, спокойствие, договорённости с&nbsp;собой. Возвращение в&nbsp;жизнь происходит мягко, а не&nbsp;как выброс из&nbsp;самолёта.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Что меняется после второго модуля</h2>
<p>Первый модуль показывает запись, второй её&nbsp;переписывает. Разница чувствуется в&nbsp;мелочах: в&nbsp;том, как ты&nbsp;реагируешь на&nbsp;резкое слово, как принимаешь решения под давлением, сколько сил остаётся к&nbsp;вечеру.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('speech')}<h3>Разговоры становятся другими</h3><p>Появляется пауза между уколом и&nbsp;ответом. В&nbsp;эту паузу помещается выбор, которого раньше просто не&nbsp;было.</p></div>
<div class="card">{icon('ceiling','var(--sage-deep)')}<h3>Решения даются легче</h3><p>Когда страх перестаёт диктовать, большие ходы в&nbsp;деле и в&nbsp;жизни уходят из&nbsp;режима «потом».</p></div>
<div class="card">{icon('cups','var(--sand)')}<h3>Дома стало теплее</h3><p>Часть напряжения в&nbsp;паре держалась на&nbsp;твоей половине общего сценария. Убирается одна сторона, меняется вся конструкция.</p></div>
<div class="card">{icon('hourglass')}<h3>Энергии больше</h3><p>Силы, которые уходили на&nbsp;удержание брони и&nbsp;старых обид, освобождаются. Это замечают первым делом близкие.</p></div>
</div>
<p class="note" style="margin-top:20px">Инструменты, которые остаются: <a href="/chizhovy2/praktiki/">ежедневные практики</a>, работа с&nbsp;состоянием и&nbsp;навык замечать <a href="/chizhovy2/slovar/">маятники</a> раньше, чем схватился.</p>
</div></section>


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Главный инструмент</p>
<h2>Пять дней вокруг живой сцены</h2>
<p>Второй модуль длиннее первого вдвое, и&nbsp;причина простая: увидеть свою запись можно быстро, а&nbsp;переписать её&nbsp;в&nbsp;один заход не&nbsp;получается. Нужно время, чтобы человек дошёл до&nbsp;настоящего эпизода, а&nbsp;не&nbsp;до&nbsp;удобной версии своей истории.</p>
<p>Основная работа идёт на&nbsp;сцене. Человек выбирает ситуацию, которая до&nbsp;сих&nbsp;пор жжёт: разговор с&nbsp;отцом, увольнение, вечер, когда всё развалилось. Участники группы встают на&nbsp;роли людей из&nbsp;этой сцены и&nbsp;говорят их&nbsp;словами. Дальше герой меняется местами с&nbsp;каждым и&nbsp;впервые слышит свою историю с&nbsp;другой стороны.</p>
<p>В&nbsp;этот момент почти всегда всплывает решение, принятое когда-то давно: «просить опасно», «я&nbsp;должен всё сам», «меня всё равно не&nbsp;услышат». Его не&nbsp;обсуждают, а&nbsp;проживают заново и&nbsp;меняют прямо в&nbsp;сцене, телом и&nbsp;голосом.</p>
<h3 style="margin-top:26px">Почему пять дней, а&nbsp;не&nbsp;три</h3>
<p>За&nbsp;три дня успевает выйти в&nbsp;сцену половина группы. Оставшиеся уезжают с&nbsp;чужими открытиями вместо своих. Пять дней дают время каждому: одна сцена на&nbsp;человека плюс роли в&nbsp;чужих, а&nbsp;это отдельная работа, которая часто бьёт не&nbsp;слабее собственной.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Формат</div><div class="big">5 дней</div><p>Очно, с&nbsp;утра до&nbsp;вечера, малой группой. Телефоны в&nbsp;зале выключены.</p></div>
<div class="box"><div class="lbl">Условие входа</div><p>Первый модуль. Без него сцена не&nbsp;срабатывает: человек ещё не&nbsp;видит свою запись.</p></div>
<div class="box"><div class="lbl">Кто ведёт</div><p>Алексей и&nbsp;Ирина вдвоём: один держит порядок и&nbsp;время, вторая уводит вглубь.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-zerkalo.jpg" alt="Зеркало в тёплом коридоре" loading="lazy"></div>
<div>
<p class="eyebrow">Что происходит с&nbsp;группой</p>
<h2 style="font-size:1.9rem">Чужая сцена работает как&nbsp;своя</h2>
<p>Первое удивление второго модуля: сильнее всего цепляет не&nbsp;своя работа, а&nbsp;чужая. Человек выходит в&nbsp;роли чьего-то отца и&nbsp;вдруг понимает про собственного больше, чем за&nbsp;двадцать лет размышлений.</p>
<p>Поэтому в&nbsp;зале нет зрителей. Даже если твоя сцена была вчера, сегодня ты&nbsp;стоишь в&nbsp;чужой и&nbsp;работаешь всерьёз. К&nbsp;пятому дню группа знает друг о&nbsp;друге такое, чего не&nbsp;знают близкие, и&nbsp;это держится годами.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Из чего состоит сцена</p>
<h2>Шесть шагов одной работы</h2>
<p class="sub">Так выглядит любая сцена на&nbsp;втором модуле, от&nbsp;первой фразы до&nbsp;выхода.</p>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('speech','var(--copper)')}<h3>1 · Ситуация</h3><p>Человек называет эпизод, который до&nbsp;сих&nbsp;пор жжёт. Не&nbsp;тему вообще, а&nbsp;конкретный вечер: кто где стоял, что было сказано.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>2 · Роли</h3><p>Участники группы встают на&nbsp;места людей из&nbsp;этой сцены. Ничего не&nbsp;играют: повторяют слова и&nbsp;интонацию так, как их&nbsp;описал герой.</p></div>
<div class="card">{icon('loop')}<h3>3 · Первый прогон</h3><p>Сцену проигрывают как было. Здесь обычно и&nbsp;становится видно, что человек сам делает шаг, который запускает знакомый финал.</p></div>
<div class="card">{icon('mirror')}<h3>4 · Обмен ролями</h3><p>Герой встаёт на&nbsp;место другого и&nbsp;отвечает себе его словами. Пять минут в&nbsp;чужой роли показывают то, что годами не&nbsp;видно из&nbsp;своей.</p></div>
<div class="card">{icon('target','var(--copper)')}<h3>5 · Старое решение</h3><p>Всплывает фраза, принятая когда-то давно: «просить опасно», «я&nbsp;должен сам», «меня не&nbsp;услышат». Её&nbsp;не&nbsp;обсуждают, а&nbsp;называют вслух в&nbsp;сцене.</p></div>
<div class="card">{icon('sunrise','var(--sand)')}<h3>6 · Другой финал</h3><p>Сцену играют заново, но&nbsp;человек принимает другое решение прямо там, телом и&nbsp;голосом. Тело запоминает этот вариант так&nbsp;же, как когда-то запомнило первый.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Частые вопросы</p>
<h2>О чём спрашивают перед вторым модулем</h2>
<details><summary>Обязательно выходить в&nbsp;сцену?</summary><p>Нет, но&nbsp;за&nbsp;пять дней в&nbsp;неё выходят почти все. Обычно человек соглашается тогда, когда посмотрел две-три чужие работы и&nbsp;увидел, что там не&nbsp;страшно.</p></details>
<details><summary>Что если я&nbsp;не&nbsp;помню детали?</summary><p>Память тела точнее, чем кажется. Достаточно начать с&nbsp;того, что помнишь: остальное всплывает уже в&nbsp;процессе, часто неожиданно для&nbsp;самого человека.</p></details>
<details><summary>Может стать хуже?</summary><p>Бывает тяжело в&nbsp;середине: поднятое требует времени, чтобы улечься. Поэтому после сцены человека не&nbsp;оставляют одного, а&nbsp;модуль не&nbsp;заканчивается сразу после самой сильной работы.</p></details>
<details><summary>Что если моя история слишком тяжёлая?</summary><p>Скажи об&nbsp;этом на&nbsp;собеседовании. Есть состояния, где сначала нужна другая помощь, и&nbsp;мы&nbsp;говорим об&nbsp;этом прямо, а&nbsp;не&nbsp;берём человека ради заполненной группы.</p></details>
<details><summary>Как выдержать пять дней подряд?</summary><p>День идёт блоками с&nbsp;перерывами, вечером все свободны. Тяжело обычно не&nbsp;физически, а&nbsp;от&nbsp;объёма увиденного: к&nbsp;третьему дню многие спят как в&nbsp;детстве.</p></details>
</div>
<aside class="side">
<div class="box"><div class="lbl">Сколько сцен</div><div class="big">1 своя</div><p>Плюс роли в&nbsp;чужих. Роль в&nbsp;чужой сцене часто бьёт не&nbsp;слабее собственной работы.</p></div>
<div class="box"><div class="lbl">Что после</div><p>Недели на&nbsp;проверку в&nbsp;жизни, потом Марафон: три месяца, чтобы новое стало привычным.</p></div>
</aside>
</div></div></section>




<section class="dark"><div class="narrow">
<h2>Честно о&nbsp;трудностях</h2>
<p>Пять дней бывают тяжёлыми. Слёзы в&nbsp;зале это норма, усталость к&nbsp;середине тоже. Иногда человек упирается и&nbsp;злится на&nbsp;ведущих: сопротивление здесь ожидаемо, и мы к&nbsp;нему готовы.</p>
<p>При этом никто не&nbsp;ломает тебя через колено: глубина добровольна, темп твой, остановиться можно в&nbsp;любой момент. Правила зала и&nbsp;границы работы описаны на&nbsp;странице <a href="/chizhovy2/bezopasnost/" style="color:#D08A5F">безопасности</a>.</p>
</div></section>

<section><div class="narrow">
<p>Второй модуль идут те, кто прошёл <a href="/chizhovy2/modul-1/">первый</a> и&nbsp;выдержал недели на проверку в жизни: увидел свою запись в&nbsp;деле и&nbsp;захотел с&nbsp;ней разобраться. Дальше <a href="/chizhovy2/marafon/">Марафон</a>, где новое поведение закрепляется девяноста днями практики.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Занять место</a> <a class="btn btn-ghost" href="/chizhovy2/marafon/" style="margin-left:8px">Дальше: Марафон</a></p>
</div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-stul.jpg" alt="Тот самый пустой стул" loading="lazy"></div>
<div>
<p class="eyebrow">Главный инструмент</p>
<h2 style="font-size:1.9rem">Тот самый пустой стул</h2>
<p>Напротив ставится стул, и&nbsp;на&nbsp;нём «сидит» тот, с&nbsp;кем разговор так и&nbsp;не&nbsp;случился: отец, бывший, ты&nbsp;сам десять лет назад. Отложенный на&nbsp;годы разговор происходит здесь, и&nbsp;у&nbsp;него наконец появляется финал.</p>
</div>
</div>
</div></section>

""")

# ================= МАРАФОН =================
P["marafon/index.html"] = ("Модуль III. Создатель реальности · Настоящие отношения",
"Три месяца практики в жизни: команда, еженедельные встречи, результаты, которые остаются.", "marafon", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-10.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Модуль III · три месяца</p><h1>Создатель реальности</h1>
<p class="lead">Инсайты выветриваются за&nbsp;две недели, если их не&nbsp;закрепить действиями. Марафон нужен ровно для&nbsp;этого: три месяца ты&nbsp;каждый день пробуешь новое в&nbsp;обычной жизни, пока оно не&nbsp;станет твоим.</p></div></div>

<section><div class="narrow">
<h2>Как устроены три месяца</h2>
<div class="card white" style="margin:20px 0 12px">{icon('people')}<h3>Команда</h3><p>Ты&nbsp;идёшь не&nbsp;один: рядом люди с&nbsp;общей целью и&nbsp;напарник у&nbsp;каждого. Поддержка работает даже в&nbsp;два часа ночи.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('speech','var(--sage-deep)')}<h3>Еженедельные встречи</h3><p>Разборы с&nbsp;Алексеем и&nbsp;Ириной: что получилось, где старая запись взяла своё, какой следующий шаг.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('sunrise','var(--sand)')}<h3>Ежедневная практика</h3><p>Утром формулируешь главный фокус дня, вечером подводишь итог: открытия и&nbsp;благодарности. Простая дисциплина, которая за 90&nbsp;дней перепрошивает привычный способ&nbsp;жить.</p></div>
<div class="card white">{icon('target')}<h3>Реальные цели</h3><p>Работа идёт на&nbsp;твоих живых задачах: дело, деньги, отношения, тело. Смотрим на&nbsp;факты, а не на&nbsp;ощущения.</p></div>

<div class="pull"><div class="q">«Раньше я&nbsp;отсеивал людей по&nbsp;уровню жизни. Сейчас просто строю настоящие отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами.»</div><div class="who">Выпускник Марафона, предприниматель</div></div>
<p><strong>Итог: другие поступки и&nbsp;новые результаты.</strong> Не&nbsp;состояние после тренинга, а&nbsp;жизнь, которая продолжает расти,&nbsp;когда сопровождение&nbsp;закончилось.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Девяносто дней</p>
<h2>Как выглядит неделя на&nbsp;Марафоне</h2>
<p class="sub">Ритм простой и&nbsp;повторяемый: он и&nbsp;делает работу. Ничего героического, всё встраивается в&nbsp;обычную жизнь с&nbsp;работой и&nbsp;детьми.</p>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('sunrise')}<h3>Каждое утро</h3><p>Намерение на&nbsp;день в&nbsp;командный чат: из&nbsp;какого состояния иду и&nbsp;что создаю. Две минуты, которые задают тон всему&nbsp;дню.</p></div>
<div class="card">{icon('calendar','var(--sage-deep)')}<h3>Каждый вечер</h3><p>Открытия и&nbsp;благодарности: что понял про себя, где старая запись взяла своё, за&nbsp;что спасибо дню и&nbsp;людям.</p></div>
<div class="card">{icon('people','var(--sand)')}<h3>Раз в&nbsp;неделю</h3><p>Живая встреча с&nbsp;Алексеем и&nbsp;Ириной: разбор ситуаций недели, ответы на&nbsp;вопросы, следующий шаг для каждого.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Почему так долго</h2>
<p>После погружения человек возвращается в ту&nbsp;же квартиру, к тем&nbsp;же людям и в тот&nbsp;же рабочий чат. Всё вокруг помнит его прежним и&nbsp;мягко тянет обратно в&nbsp;знакомую роль. Без поддержки на&nbsp;этом отрезке понятое выветривается за&nbsp;пару недель: это главная причина, по&nbsp;которой тренинги «не&nbsp;работают».</p>
<p>Марафон закрывает именно этот разрыв. Каждый день ты&nbsp;делаешь новый выбор в&nbsp;реальных обстоятельствах, каждую неделю приносишь результат на&nbsp;разбор, и&nbsp;рядом идёт команда, которая видит твои сдвиги со&nbsp;стороны. За&nbsp;девяносто дней новое поведение перестаёт требовать усилий.</p>
<div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>90 дней</b><span>ежедневной практики в обычной&nbsp;жизни</span></div>
<div class="nail"><b>13</b><span>недель с&nbsp;разбором у&nbsp;ведущих</span></div>
<div class="nail"><b>1</b><span>напарник, который держит, когда тяжело</span></div>
</div>
</div></section>


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как это работает на&nbsp;практике</p>
<h2>Работа переезжает в&nbsp;чат</h2>
<p>Марафон почти целиком идёт в&nbsp;обычной жизни. Зал остаётся позади, а&nbsp;работа переезжает в&nbsp;командный чат, куда каждый пишет каждый день. Утром намерение на&nbsp;день, вечером разбор: что сбылось, где сорвался, за&nbsp;что благодарен.</p>
<p>Первые две недели пишут ровно и&nbsp;бодро. Потом начинается настоящее: пропуски, отговорки, откаты в&nbsp;старые реакции. Это и&nbsp;есть рабочий материал, ради которого затевались три месяца, а&nbsp;не&nbsp;три дня. Разбирают именно эти места, на&nbsp;еженедельной встрече, при всех и&nbsp;без осуждения.</p>
<p>К&nbsp;середине тон в&nbsp;чате меняется. Люди перестают отчитываться и&nbsp;начинают говорить простыми словами: «сегодня сорвался на&nbsp;сына, увидел, откуда это», «первый раз попросил помощь и&nbsp;не&nbsp;умер». По&nbsp;этим строчкам ведущие и&nbsp;видят, что запись действительно меняется.</p>
<h3 style="margin-top:26px">Что делает команда</h3>
<p>Команда собирается на&nbsp;втором модуле и&nbsp;дальше идёт вместе. Это не&nbsp;чат поддержки с&nbsp;сердечками: у&nbsp;людей общие задачи, они пишут намерения друг за&nbsp;друга, встречаются на&nbsp;забегах и&nbsp;вытаскивают того, кто провалился. Один из&nbsp;участников сформулировал точнее всего: перестаёшь путать «я&nbsp;забыл» и&nbsp;«я&nbsp;подвёл своих».</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Сколько идёт</div><div class="big">3 месяца</div><p>Каждый день практика, раз в&nbsp;неделю разбор с&nbsp;Алексеем и&nbsp;Ириной.</p></div>
<div class="box"><div class="lbl">Где проходит</div><p>В&nbsp;обычной жизни. Встречи команды онлайн, поэтому город значения не&nbsp;имеет.</p></div>
<div class="box"><div class="lbl">Условие входа</div><p>Два очных модуля. Марафон закрепляет то, что на&nbsp;них открылось.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<p class="eyebrow">Что делают каждый день</p>
<h2>Четыре простых действия</h2>
<p class="sub">Ничего сложного. Сложное в&nbsp;том, чтобы делать это девяносто дней подряд.</p>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('sunrise','var(--copper)')}<h3>Намерение утром</h3><p>Пять минут. Не&nbsp;список дел, а&nbsp;состояние и&nbsp;итог дня, записанные так, будто он&nbsp;уже прошёл. Формулировки без частицы «не»: мозг её&nbsp;не&nbsp;замечает.</p></div>
<div class="card">{icon('calendar','var(--sage-deep)')}<h3>Разбор вечером</h3><p>Десять минут. Что сбылось из&nbsp;утреннего, где сорвался, что с&nbsp;этим делать завтра. Пишется в&nbsp;общий чат, при команде.</p></div>
<div class="card">{icon('coins')}<h3>Одно действие из&nbsp;новой записи</h3><p>Сказать то, что раньше проглатывал. Попросить помощь. Не&nbsp;среагировать там, где всегда срывался. Одно за&nbsp;день, зато настоящее.</p></div>
<div class="card">{icon('people','var(--sand)')}<h3>Вклад в&nbsp;команду</h3><p>Написать намерение за&nbsp;другого, поддержать того, кто выпал, приехать на&nbsp;забег. Это не&nbsp;вежливость: работа с&nbsp;фокусом на&nbsp;другом даёт больше, чем работа на&nbsp;себя.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Что происходит по&nbsp;месяцам</p>
<h2>Три месяца изнутри</h2>
<h3>Первый месяц</h3>
<p>Инерция после модуля ещё держит, писать легко, результаты появляются быстро и&nbsp;радуют. Ошибка этого месяца одна: решить, что дальше пойдёт так&nbsp;же само.</p>
<h3>Второй месяц</h3>
<p>Самый честный. Появляются пропуски, отговорки, откаты в&nbsp;старые реакции. Тут выясняется, что менялось по&nbsp;инерции, а&nbsp;что действительно изменилось. Разбирают именно эти места, и&nbsp;ради них затевались три месяца, а&nbsp;не&nbsp;три дня.</p>
<h3>Третий месяц</h3>
<p>Тон в&nbsp;чате меняется. Люди перестают отчитываться и&nbsp;пишут простыми словами: «сорвался на&nbsp;сына, увидел откуда», «первый раз попросил помощь и&nbsp;не&nbsp;умер». По&nbsp;таким строчкам и&nbsp;видно, что запись поменялась.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Каждую неделю</div><div class="big">1 разбор</div><p>Встреча команды с&nbsp;Алексеем и&nbsp;Ириной. Онлайн, поэтому город значения не&nbsp;имеет.</p></div>
<div class="box"><div class="lbl">Сколько пишут</div><p>Два коротких сообщения в&nbsp;день: утром намерение, вечером разбор.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-utro.jpg" alt="Пять минут, которые задают день" loading="lazy"></div>
<div>
<p class="eyebrow">Каждое утро</p>
<h2 style="font-size:1.9rem">Пять минут утром</h2>
<p>Утреннее намерение пишут до&nbsp;того, как открыли почту и&nbsp;чаты. Пять минут, лист бумаги или заметка в&nbsp;телефоне. Смысл не&nbsp;в&nbsp;тексте, а&nbsp;в&nbsp;том, что человек первым делом выбирает состояние сам, а&nbsp;не&nbsp;получает его от&nbsp;новостей и&nbsp;чужих сообщений.</p>
</div>
</div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Над чем работают участники</h2>
<p>Цели приносит каждый свои, и&nbsp;они всегда из&nbsp;настоящей жизни: запустить дело, которое откладывалось три года. Восстановить отношения с&nbsp;отцом. Выйти из&nbsp;найма. Вернуть спорт. Перестать срываться на&nbsp;детей. Сделать предложение. Уехать в&nbsp;поездку, на&nbsp;которую полгода не&nbsp;решался.</p>
<p>Итог меряем фактами: сделал или отложил, поговорил или снова промолчал. Что из&nbsp;этого выходит на&nbsp;практике, видно в&nbsp;<a href="/chizhovy2/istorii/komanda-mir/" style="color:#D08A5F">истории команды «МИР»</a>.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Выпуски Марафона</p>
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-10.jpg" alt="Команда Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-11.jpg" alt="Выпуск Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-13.jpg" alt="Финал модуля" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-08.jpg" alt="Разбор в кругу" loading="lazy"></div>
</div>
<p class="btns" style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Обсудить участие на&nbsp;собеседовании</a></p>
</div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-tropa.jpg" alt="Дорога длиннее, чем кажется" loading="lazy"></div>
<div>
<p class="eyebrow">Три месяца</p>
<h2 style="font-size:1.9rem">Дорога длиннее, чем кажется</h2>
<p>Марафон устроен как длинная дистанция: важно не&nbsp;как ты&nbsp;стартовал, а&nbsp;доходишь&nbsp;ли. Первые недели идут легко, потом начинается настоящая работа, и&nbsp;именно там команда вытаскивает тех, кто выдохся.</p>
</div>
</div>
</div></section>

""")

# ================= ДЛЯ ПАР =================
P["para/index.html"] = ("Тренинг для пар · Настоящие отношения",
"Муж и жена проходят тренинг вместе: близость растёт с двух сторон.", "para", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-para-itog.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Для пар</p><h1>Когда приходят вдвоём, меняются оба</h1>
<p class="lead">Годами ездить на&nbsp;тренинги и возвращаться домой, где партнёр остался прежним, тяжело. А&nbsp;можно прийти вдвоём и&nbsp;переписать общий сценарий с&nbsp;двух сторон сразу.</p></div></div>

<section><div class="narrow">
<h2>Что происходит с&nbsp;парой</h2>
<p>У&nbsp;двоих всегда две записи, и&nbsp;они цепляются друг за&nbsp;друга, как шестерёнки: её&nbsp;обида включает его&nbsp;тишину, а&nbsp;тишина кормит обиду. На&nbsp;тренинге каждый работает со&nbsp;своей записью, и шестерёнки&nbsp;расцепляются.</p>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('mountain')}<h3>Он</h3><p>Возвращает опору и&nbsp;уверенность: решения из&nbsp;спокойствия, дело и&nbsp;достаток растут без надрыва.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Она</h3><p>Оживает: раскрывается, вдохновляет, выходит из&nbsp;режима ожидания и&nbsp;обслуживания.</p></div>
</div>
<p style="margin-top:24px">Дальше начинается то, ради чего школа носит своё имя: <strong>настоящие отношения.</strong> Разговоры, которые заканчиваются ближе, чем начинались. Быт, в&nbsp;котором снова видно человека. Общие цели вместо параллельных жизней.</p>
<p>Пары в&nbsp;зале работают наравне со&nbsp;всеми: одни процессы вместе, другие по&nbsp;отдельности. Прийти одному тоже можно: отношения меняются, даже когда запись переписывает один из&nbsp;двоих.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Знакомые ситуации</p>
<h2>С чем приходят пары</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('cups')}<h3>Соседи по&nbsp;квартире</h3><p>Общий календарь, счёт и&nbsp;дети. Разговоры про логистику. Не&nbsp;ссоритесь, потому что&nbsp;незачем.</p></div>
<div class="card">{icon('loop','var(--sage-deep)')}<h3>Ссоры по&nbsp;кругу</h3><p>Один и тот&nbsp;же сценарий с теми&nbsp;же словами и&nbsp;финалом. Повод разный, спектакль один и тот&nbsp;же.</p></div>
<div class="card">{icon('speech','var(--sand)')}<h3>Стена молчания</h3><p>Он&nbsp;уходит в&nbsp;себя, она добивается ответа, он&nbsp;закрывается сильнее. Знакомый круг, из&nbsp;которого не&nbsp;выйти уговорами.</p></div>
<div class="card">{icon('flame')}<h3>Близости почти не осталось</h3><p>Тепло ушло в&nbsp;быт, нежность стала редкостью. Оба помнят, как было, и&nbsp;оба не&nbsp;знают, куда это делось.</p></div>
<div class="card">{icon('ceiling','var(--sage-deep)')}<h3>Кризис после десяти лет</h3><p>Дети подросли, цели достигнуты, и&nbsp;вдруг непонятно, что дальше и&nbsp;зачем вместе.</p></div>
<div class="card">{icon('mirror','var(--sand)')}<h3>Один меняется, другой на месте</h3><p>Один меняется, другой остаётся. Расстояние растёт молча, пока однажды не&nbsp;становится слишком большим.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Почему вдвоём сильнее</h2>
<p>Когда один приносит домой новое понимание, второй его не&nbsp;разделяет: слова звучат чужими, изменения выглядят как претензия. Это нормальная реакция и&nbsp;частая причина, по&nbsp;которой хорошая работа одного упирается в&nbsp;стену.</p>
<p>Когда проходят оба, общий язык появляется сразу. Вы&nbsp;видели одно и то&nbsp;же, называете вещи одними словами и&nbsp;дома продолжаете разговор, а не&nbsp;начинаете спор заново. Дальше это превращается в&nbsp;навык: слышать друг друга там, где обычно включался старый сценарий.</p>
<div class="pull"><div class="q">«Мы перестали выяснять, кто прав. Стало интересно, что с&nbsp;ним происходит на&nbsp;самом деле.»</div><div class="who">Участница, прошла модули вместе с&nbsp;мужем</div></div>
<p>Если партнёр пока не&nbsp;готов, приходить одному не&nbsp;только можно, но и&nbsp;полезно: твоя половина общего сценария в&nbsp;твоих руках, а&nbsp;шестерёнка перестаёт крутиться, когда останавливается одна из&nbsp;двух. Частые опасения на&nbsp;этот счёт разобраны на&nbsp;странице <a href="/chizhovy2/somneniya/">сомнений</a>.</p>
<p style="margin-top:26px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться вдвоём</a> <a class="btn btn-ghost" href="/chizhovy2/programma/" style="margin-left:8px">Программа целиком</a></p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">В&nbsp;зале</p>
<h2>Что происходит на сцене, когда вы пришли&nbsp;вдвоём</h2>
<p>Своя сцена у&nbsp;каждого. Человек возвращается в&nbsp;собственную историю, чаще всего далеко за&nbsp;пределы этой пары: в&nbsp;кухню родительской квартиры, в&nbsp;разговор с&nbsp;отцом, в&nbsp;день, когда решил, что просить бесполезно. Роли в&nbsp;этой сцене берут на&nbsp;себя другие участники группы. Живого партнёра в&nbsp;свою роль обычно не&nbsp;ставят: рядом с&nbsp;ним сцена за&nbsp;минуту сползает в&nbsp;привычное выяснение, кто&nbsp;прав.</p>
<p>Партнёр в&nbsp;это время сидит в&nbsp;зале и&nbsp;смотрит. Впервые за&nbsp;годы он&nbsp;видит историю целиком, без своей реплики внутри неё. Дальше идёт обмен ролями: человек встаёт на&nbsp;место другого и&nbsp;отвечает себе его словами. Пять минут в&nbsp;чужой роли показывают то, что из&nbsp;своей не&nbsp;видно годами. Как устроены остальные инструменты, разобрано в&nbsp;<a href="/chizhovy2/tehniki-sceny/">техниках&nbsp;сцены</a>.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Кто в&nbsp;ролях</div><div class="big">Группа</div><p>Отца, мать, бывшего, тебя самого в&nbsp;пятнадцать играют участники зала. Поэтому в&nbsp;сцене можно сказать всё до&nbsp;конца.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Дома</p>
<h2>Что меняется, когда вы вернулись&nbsp;домой</h2>
<p>Первым появляется общий язык. У&nbsp;ссоры возникает имя: старая запись, важность, точка&nbsp;А. Названная сцена короче безымянной, потому что оба уже видели её со&nbsp;стороны и&nbsp;узнают за&nbsp;пару реплик. Вместо «ты&nbsp;опять начинаешь» звучит другой вопрос: что сейчас включилось у каждого из&nbsp;нас.</p>
<p>Дальше меняется быт. Он&nbsp;перестаёт быть полем, где меряются вкладом, и&nbsp;снова становится просто бытом. Дети слышат другую интонацию раньше, чем взрослые успевают что-то им&nbsp;объяснить: запись передаётся именно&nbsp;интонацией.</p>
<p>На&nbsp;третьем модуле пары идут в&nbsp;одной команде и&nbsp;каждый день читают записи друг друга в&nbsp;общем чате. Многие говорят, что там впервые узнали, чего партнёр хочет на&nbsp;ближайший год: дома об&nbsp;этом почему-то не заходил&nbsp;разговор.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Общий&nbsp;язык</div><div class="big">14 слов</div><p>Столько понятий в&nbsp;<a href="/chizhovy2/slovar/">словаре школы</a>. После модуля пара говорит о&nbsp;трудном именно&nbsp;ими.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<p class="eyebrow">Как работают вдвоём</p>
<h2>Что происходит с&nbsp;парой в&nbsp;зале</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('people','var(--copper)')}<h3>Каждый со&nbsp;своей стороной</h3><p>Работают не&nbsp;«отношения вообще», а&nbsp;две половины одного круга. Каждый разбирает свои шаги, а&nbsp;не&nbsp;поведение второго.</p></div>
<div class="card">{icon('mirror')}<h3>Обмен ролями</h3><p>Партнёры встают на&nbsp;место друг друга и&nbsp;отвечают чужими словами. После этого спорить о&nbsp;том, «кто что имел в&nbsp;виду», обычно нечем.</p></div>
<div class="card">{icon('sunrise','var(--sage-deep)')}<h3>Другой финал</h3><p>Знакомая сцена проигрывается заново с&nbsp;новым решением. Тело запоминает этот вариант так&nbsp;же, как когда-то запомнило первый.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Частые вопросы&nbsp;пар</p>
<h2>О чём пары спрашивают на&nbsp;собеседовании</h2>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Мы будем в одной&nbsp;группе?</h3><p>Да, в&nbsp;одном зале. Часть процессов идёт вместе, остальные по&nbsp;отдельности, и&nbsp;это решают ведущие по&nbsp;ходу работы. Договариваться заранее не&nbsp;нужно.</p></div>
<div class="card"><h3>Придётся рассказывать про нашу семью при&nbsp;чужих?</h3><p>Глубину выбираешь сам, силой в&nbsp;процесс никто не&nbsp;тянет. Всё, что прозвучало в&nbsp;зале, остаётся в&nbsp;зале: это первое правило, о&nbsp;котором договариваются в&nbsp;<a href="/chizhovy2/bezopasnost/">первый вечер</a>.</p></div>
<div class="card"><h3>А если вскроется то, о&nbsp;чём мы молчали&nbsp;годами?</h3><p>Обычно ради этого и&nbsp;приходят. Разница в&nbsp;том, что разговор идёт внутри размеченного процесса и&nbsp;рядом двое ведущих, а не на&nbsp;кухне в&nbsp;полночь после третьего&nbsp;круга.</p></div>
<div class="card"><h3>Идти сразу вдвоём или по&nbsp;очереди?</h3><p>Работают оба варианта. Часто первым проходит тот, кому горит, а&nbsp;второй приходит следующим набором, когда видит перемены дома и&nbsp;начинает спрашивать&nbsp;сам.</p></div>
</div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Кому вдвоём&nbsp;рано</div><p>Если второй идёт только потому, что его уговорили: в&nbsp;зале он&nbsp;просидит все дни и&nbsp;увезёт домой раздражение. Если ждёте, что ведущие рассудят, кто прав: приговоров школа не&nbsp;выносит и к&nbsp;решениям «уходи» или «оставайся» не&nbsp;ведёт. Если одному сейчас нужна помощь врача: скажем об&nbsp;этом прямо на первом&nbsp;разговоре.</p></div>
<div class="box"><div class="lbl">Если готов только&nbsp;один</div><div class="big">Оба&nbsp;пути</div><p>Большинство участников приходят по&nbsp;одному. Отношения меняются и&nbsp;тогда: твоя половина общего сценария в твоих&nbsp;руках.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-para.jpg" alt="Утро на двоих" loading="lazy"></div>
<div>
<p class="eyebrow">Для пар</p>
<h2 style="font-size:1.9rem">Утро на&nbsp;двоих</h2>
<p>Общий стол, общий календарь, а&nbsp;разговоров всё меньше. С&nbsp;этого и&nbsp;начинают пары.</p>
</div>
</div>
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
<h2>Алексей и&nbsp;Ирина</h2>
<div class="grid2" style="margin-top:24px">
<div class="card white">{icon('mountain')}<h3>Алексей</h3><p>Коуч с&nbsp;сертификацией ICF, 16&nbsp;лет практики. Держит структуру и&nbsp;точность процесса: с&nbsp;ним безопасно идти в&nbsp;глубину, потому что он&nbsp;видит дорогу&nbsp;целиком.</p></div>
<div class="card white">{icon('flame','var(--sand)')}<h3>Ирина</h3><p>Трансформационный тренер. Шесть лет готовилась к&nbsp;этому формату под руководством наставника. Работает на&nbsp;глубине. Участники говорят, что она «вскрывает и&nbsp;собирает», и&nbsp;вспоминают её работу&nbsp;годами.</p></div>
</div>
<p style="margin-top:24px">Роли в&nbsp;зале дополняют друг друга: его&nbsp;опора и её&nbsp;чувствование, структура и&nbsp;глубина. В&nbsp;паре ведущих это видно с&nbsp;первого часа: один размечает дорогу, вторая идёт туда, где живое.</p>
<p>Поэтому здесь не&nbsp;учат жить и не&nbsp;мотивируют. Вместе разбираются, откуда берётся твоя реакция и по&nbsp;какой причине в&nbsp;паре повторяется один сюжет. Иногда это непросто.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Вместе</div><div class="big">17 лет</div><p>Свой быт, свои кризисы и&nbsp;свои выходы из&nbsp;них. Отношения, о&nbsp;которых говорят в&nbsp;зале, они строят каждый&nbsp;день.</p></div>
<div class="box"><div class="lbl">Из чата команды</div><div class="cit">«Благодарю Ирину и&nbsp;Алексея за вклад в&nbsp;мою&nbsp;трансформацию.»</div><div class="who">Солвита И., участница третьего модуля, с&nbsp;её&nbsp;согласия</div></div>
</aside>
</div></div></section>

<section class="dark"><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как они пришли к&nbsp;этому</p>
<h2>Сначала своя жизнь, потом&nbsp;зал</h2>
<p>Школа выросла не из&nbsp;теории. Сначала были свои повторяющиеся круги: разговоры на&nbsp;одних и тех&nbsp;же местах, попытки договориться словами, откаты после хороших недель. Всё то, с&nbsp;чем люди приходят сюда сейчас. Знакомо изнутри.</p>
<div class="pull"><div class="q">«У&nbsp;нас не&nbsp;было идеальной истории. Было непонимание, ошибки, потери, моменты, где казалось: дальше некуда. Именно там началось настоящее.»</div><div class="who">Из обращения Алексея и&nbsp;Ирины к&nbsp;каналу школы</div></div>
<p>Дальше шестнадцать лет практики: сотни залов, тысячи разобранных сцен, свои ошибки ведущих и&nbsp;свои находки. Из&nbsp;пяти источников осталось то, что реально меняет жизнь участников, остальное отсеялось. Как именно отбирали, разобрано в&nbsp;<a href="/chizhovy2/istoki/" style="color:#D08A5F">истоках метода</a>.</p>
<p>Ирина шесть лет готовилась к&nbsp;этому формату под руководством наставника, прежде чем встать в&nbsp;пару ведущих. Не&nbsp;курс выходного дня, а&nbsp;долгая работа с&nbsp;собственной глубиной: вести человека можно только туда, где был сам. Иначе никак.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Слова участника</div><div class="cit">«Благодарю Алексея за&nbsp;разговор и&nbsp;включённость в&nbsp;мою жизнь.»</div><div class="who">Из вечерних записей команды, опубликовано с&nbsp;согласия автора</div></div>
<div class="box"><div class="lbl">Практика</div><div class="big">16 лет</div><p>Столько за&nbsp;спиной у&nbsp;Алексея: залы, группы, сопровождение. Метод собран и&nbsp;проверен на этой&nbsp;дистанции.</p></div>
<div class="box"><div class="lbl">Подготовка Ирины</div><div class="big">6 лет</div><p>Под руководством наставника, до&nbsp;первого зала в роли&nbsp;ведущей.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<p class="eyebrow">Что за&nbsp;этим стоит</p>
<h2>Опыт, который не&nbsp;помещается в&nbsp;регалии</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('mountain','var(--copper)')}<h3>16 лет залов</h3><p>Сотни групп, тысячи разобранных сцен. За&nbsp;эти годы из&nbsp;пяти источников осталось только то, что реально меняет жизнь участников.</p></div>
<div class="card">{icon('lens')}<h3>Шесть лет подготовки</h3><p>Столько Ирина работала под&nbsp;руководством наставника, прежде чем встать в&nbsp;пару ведущих. Вести человека можно только туда, где был сам.</p></div>
<div class="card">{icon('cups','var(--sage-deep)')}<h3>17 лет вместе</h3><p>Свой быт, свои кризисы, свои выходы. Отношения, о&nbsp;которых идёт речь в&nbsp;зале, они строят каждый день.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Дистанция вместо медалей</h3><p>Алексей триатлет, финишер IronMan&nbsp;70.3. Длинная дистанция каждый день проверяет то, чему школа учит: доходит тот, кто играет вдолгую.</p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Как они работают вместе</p>
<h2>Две роли в&nbsp;зале</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('mountain')}<h3>Он держит порядок и время</h3><p>Ведёт процесс и&nbsp;видит карту целиком. Знает, куда идти дальше и&nbsp;где остановиться. С&nbsp;таким ведущим не&nbsp;страшно заходить далеко: дорога размечена.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Она уводит вглубь</h3><p>Чувствует, что происходит с&nbsp;человеком, раньше слов. Идёт туда, где живое, и&nbsp;остаётся рядом до конца&nbsp;процесса.</p></div>
</div>
<p class="sub" style="margin-top:22px;max-width:none">Это те&nbsp;же два начала, которые мы&nbsp;помогаем соединить внутри каждого участника: опора и&nbsp;чувствительность, структура и&nbsp;живость. Пара ведущих показывает их в&nbsp;работе, а не&nbsp;объясняет на&nbsp;словах.</p>
</div></section>

<section><div class="wrap">
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

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Что видят участники</p>
<h2>Почему это важно для&nbsp;группы</h2>
<p>Когда школу отношений ведёт один человек, всегда остаётся вопрос: а&nbsp;как у&nbsp;него самого. Здесь ответ виден сразу: работают двое, вместе семнадцать лет, со&nbsp;своим бытом, своими кризисами и&nbsp;выходами из&nbsp;них.</p>
<p>В зале это даёт две вещи. Первое: любую семейную сцену участники разбирают с&nbsp;двух сторон, мужской и&nbsp;женской, без перекоса в&nbsp;чью-то пользу. Второе: ведущие не&nbsp;идеализируют отношения и не&nbsp;делают вид, что у&nbsp;них всё гладко. Об&nbsp;этом прямо сказано в&nbsp;<a href="/chizhovy2/manifest/">манифесте школы</a>.</p>
<p>Есть и&nbsp;третье, о&nbsp;котором говорят чаще всего: с&nbsp;группой остаются после модуля. Разборы каждую неделю, ответы в&nbsp;чате, поддержка на&nbsp;забегах и в&nbsp;два часа ночи. Как это устроено, видно на&nbsp;странице <a href="/chizhovy2/soobshchestvo/">сообщества</a>.</p>
</div>
<aside class="side">
</aside>
</div></div></section>




<section><div class="narrow">
<h2>Познакомиться лично</h2>
<p class="sub" style="margin:0 0 26px">Разговор о&nbsp;твоей ситуации: смотрим, что происходит, и&nbsp;вместе решаем, по пути ли&nbsp;нам. Для&nbsp;читателей сайта бесплатно.</p>
<p class="btns"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>
""")

P["otzyvy/index.html"] = ("Истории учеников · Настоящие отношения",
"Живые истории выпускников школы: до, во время и после тренинга.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-05.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истории учеников</p><h1>Их словами, без глянца</h1>
<p class="lead">Отзывы под рекламу мы не&nbsp;переписываем. Ниже живые фрагменты из&nbsp;анкет, чатов и&nbsp;писем, опубликованные с&nbsp;согласия авторов. Опыт у&nbsp;каждого свой. И результат&nbsp;тоже.</p></div></div>

<section><div class="narrow">
<!-- ПРОТОТИП: подписи и полные версии согласовать с авторами перед публикацией -->
<div class="card white" style="margin-bottom:16px">
<p class="eyebrow" style="margin-bottom:10px">Предприниматель, пришёл в самый тяжёлый момент</p>
<p>«Я&nbsp;находился в&nbsp;фазе, которую называют дном: кассовый разрыв, долги, расставание с&nbsp;девушкой, друзья отвернулись. Не&nbsp;хотелось ни с&nbsp;кем общаться, хотелось закрыться в&nbsp;коробочку и сидеть&nbsp;одному.</p>
<p>На&nbsp;тренинге я&nbsp;долго сопротивлялся, как баран. Труднее всего было принять точку&nbsp;А: признать, где я на&nbsp;самом деле. А&nbsp;потом увидел, что покупал отношения вместо того, чтобы их&nbsp;строить.</p>
<p style="margin-bottom:0">Сейчас строю настоящие отношения везде. Деньги начали приходить, энергии много, и я&nbsp;умею ей&nbsp;распоряжаться. Цели выросли кратно, научился играть в&nbsp;долгую. Одной фразой: получил новую версию&nbsp;себя».</p>
</div>
<div class="card white" style="margin-bottom:16px">
<p class="eyebrow" style="margin-bottom:10px">Участница второго модуля</p>
<p style="margin-bottom:0">«Годами затыкала свои боли: научилась обезболивать и не&nbsp;слышать себя, стала чёрствой к&nbsp;себе. На&nbsp;модуле впервые за&nbsp;много лет плакала при людях и&nbsp;поняла, что это не&nbsp;стыдно. Теперь знаю, что могу быть яркой, настоящей, звонкой, сама по&nbsp;себе».</p>
</div>
<div class="card white">
<p class="eyebrow" style="margin-bottom:10px">Выпускница Марафона</p>
<p style="margin-bottom:0">«Полгода не&nbsp;могла решиться, даже паспорт найти не&nbsp;могла. А&nbsp;сегодня внутри приняла решение, и&nbsp;паспорт нашёлся. Купила тур, еду на&nbsp;море на&nbsp;Новый год».</p>
</div>

<p style="margin-bottom:22px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Полные истории: с точкой&nbsp;А и&nbsp;переломом</a></p>
<div class="pull"><div class="q">«Моя жизнь точно разделена на до и&nbsp;после.»</div><div class="who">Участница школы</div></div>
<div class="pull"><div class="q">«Спасибо, что помогли прожить стену, которую я&nbsp;так долго строил. Теперь она мне не&nbsp;нужна.»</div><div class="who">Участник школы</div></div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">По ступеням</p>
<h2>Что говорят после каждого модуля</h2>
<p class="sub">Слова разные, а&nbsp;узор один: сначала человек видит свою запись, потом снимает груз и&nbsp;переносит новое в&nbsp;жизнь.</p>
<div class="grid3" style="margin-top:26px">
<div class="card white"><p class="eyebrow" style="margin-bottom:10px">После модуля&nbsp;I</p>
<p class="serif" style="font-style:italic">«Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка колоссальная».</p>
<p class="serif" style="font-style:italic;margin-top:12px">«Впервые за&nbsp;годы услышал себя, а не&nbsp;то, что должен хотеть».</p></div>
<div class="card white"><p class="eyebrow" style="margin-bottom:10px">После модуля&nbsp;II</p>
<p class="serif" style="font-style:italic">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на&nbsp;десять меньше».</p>
<p class="serif" style="font-style:italic;margin-top:12px">«Годами затыкала свои боли. Теперь знаю, что могу быть яркой и&nbsp;звонкой, сама по&nbsp;себе».</p></div>
<div class="card white"><p class="eyebrow" style="margin-bottom:10px">После Марафона</p>
<p class="serif" style="font-style:italic">«Раньше я&nbsp;отсеивал людей по&nbsp;уровню жизни. Сейчас просто строю настоящие отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами».</p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">По сферам</p>
<h2>Где именно меняется жизнь</h2>
<p class="sub">Ниже четыре сферы и&nbsp;голоса участников о&nbsp;том, где перемены становятся заметны&nbsp;первыми.</p>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('cups')}<h3>Отношения</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Вместо эмоций решила стать вкладом в&nbsp;отношения, говорить с&nbsp;уважением и&nbsp;любовью. И&nbsp;вот первые ростки».</p></div>
<div class="card">{icon('ceiling','var(--sage-deep)')}<h3>Дело и&nbsp;достаток</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Деньги начали приходить, энергии много, и я&nbsp;умею ей&nbsp;распоряжаться. Цели кратно увеличились, научился играть в&nbsp;долгую».</p></div>
<div class="card">{icon('route','var(--sand)')}<h3>Решения</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Вчера писала намерение, а&nbsp;сегодня отследила, что оно сбылось. Яркая и&nbsp;расслабленная жизнь это моё».</p></div>
<div class="card">{icon('people')}<h3>Окружение</h3><p class="serif" style="font-style:italic;color:var(--ink)">«Когда убираю фокус с&nbsp;себя и&nbsp;вовлечён в&nbsp;команду, энергия кратно растёт, и&nbsp;люди поворачиваются ко мне&nbsp;лицом».</p></div>
</div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Полные истории целиком</a></p>
</div></section>



<section><div class="wrap">
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-03.jpg" alt="Группа выпуска" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-09.jpg" alt="Участники тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
</div>
<p class="btns" style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Начать свою историю</a></p>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как читать эти слова</p>
<h2>Почему отзывы звучат похоже</h2>
<p>Люди приходят с&nbsp;разным: один после потери бизнеса, другая из&nbsp;тихого благополучия, где всё есть и&nbsp;ничего не&nbsp;радует. А&nbsp;говорят потом примерно одно и&nbsp;то&nbsp;же: «увидел, откуда это», «перестал держать всё на&nbsp;себе», «дома стало тихо».</p>
<p>Причина простая. Сюжеты разные, а&nbsp;механика повтора у&nbsp;всех одна: старое решение крутит один и&nbsp;тот&nbsp;же круг. Когда меняется оно, меняется похожее у&nbsp;разных людей, поэтому и&nbsp;слова совпадают.</p>
<h3>Чего в&nbsp;этих словах нет</h3>
<p>Обещаний, что так будет у&nbsp;каждого. Результат зависит от&nbsp;того, включается&nbsp;ли человек сам, и&nbsp;мы&nbsp;говорим об&nbsp;этом прямо на&nbsp;собеседовании. Слова участников публикуем с&nbsp;их&nbsp;разрешения и&nbsp;не&nbsp;правим.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">За 16 лет</div><p>Через залы прошли сотни человек. Часть из&nbsp;них общается до&nbsp;сих&nbsp;пор.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-otzyvy.jpg" alt="Записи и письма учеников" loading="lazy"></div>
<div>
<p class="eyebrow">Откуда эти слова</p>
<h2 style="font-size:1.9rem">Записи и&nbsp;письма учеников</h2>
<p>Часть слов взята из&nbsp;командных чатов, часть из&nbsp;анкет после модулей. Публикуем с&nbsp;разрешения авторов и&nbsp;не&nbsp;правим.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Что меняется чаще всего</p>
<h2>Четыре сферы, о&nbsp;которых говорят</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('cups','var(--copper)')}<h3>Отношения</h3><p>Ссоры перестают идти по&nbsp;кругу. Люди начинают говорить прямо и&nbsp;слышать вторую сторону, а&nbsp;не&nbsp;свою версию про неё.</p></div>
<div class="card">{icon('ceiling')}<h3>Дело и&nbsp;достаток</h3><p>Решения принимаются спокойно, а&nbsp;не&nbsp;из&nbsp;страха потерять. Появляется способность отдавать задачи и&nbsp;думать вдолгую.</p></div>
<div class="card">{icon('lens','var(--sage-deep)')}<h3>Отношение к&nbsp;себе</h3><p>Проходит привычка доказывать. Человек перестаёт мерить себя чужими ожиданиями и&nbsp;начинает слышать своё.</p></div>
<div class="card">{icon('people','var(--sand)')}<h3>Окружение</h3><p>Меняется круг: уходят связи, державшиеся на&nbsp;выгоде, остаются те, с&nbsp;кем можно быть настоящим.</p></div>
</div>
</div></section>

""")

# ================= ВОПРОСЫ =================
P["voprosy/index.html"] = ("Вопросы и ответы · Настоящие отношения",
"Честные ответы: формат, глубина, группа, условия участия.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Вопросы и&nbsp;ответы</p><h1>Что спрашивают перед стартом</h1>
<p class="lead">Собрали то, что чаще всего звучит на&nbsp;собеседованиях. Если своего вопроса не&nbsp;нашёл, задай его лично: контакты внизу.</p></div></div>

<section><div class="narrow">
<details><summary>На чём основан метод?</summary><p>На&nbsp;практической психологии: психодрама Якоба Морено, работа с&nbsp;состоянием и&nbsp;групповые процессы, проверенные за 16&nbsp;лет практики. Глубину даём через живой опыт, объясняем через понятные механизмы работы мозга и&nbsp;тела. Все опоры метода мы&nbsp;показываем открыто: <a href="/chizhovy2/istoki/">раздел «Истоки»</a>.</p></details>
<details><summary>Я уже ходил к&nbsp;психологу. Чем это отличается?</summary><p>Личная терапия строится на&nbsp;разговоре, час в&nbsp;неделю. Здесь работа идёт в&nbsp;живых сценах, телом и&nbsp;эмоцией, в&nbsp;погружении на&nbsp;несколько дней. Инструменты разные, и&nbsp;они хорошо дополняют друг друга.</p></details>
<details><summary>Боюсь групповой работы. Придётся раскрываться перед&nbsp;чужими?</summary><p>Глубина всегда добровольна: никто не&nbsp;вытаскивает силой. Обычно уже к&nbsp;вечеру первого дня зал перестаёт быть чужим: у&nbsp;людей одинаковые боли, и в&nbsp;соседней истории ты&nbsp;узнаёшь свою.</p></details>
<details><summary>Можно прийти одному, без&nbsp;партнёра?</summary><p>Да. Большинство участников приходят по&nbsp;одному. Отношения меняются, даже когда работает один из&nbsp;двоих: твоя половина общего сценария в&nbsp;твоих руках.</p></details>
<details><summary>Сколько длится программа?</summary><p>Модуль I: 2,5&nbsp;дня, пятничный вечер плюс выходные. Второй: пять дней подряд. Третий: три месяца сопровождения при обычной жизни. Между ступенями 3-5 недель.</p></details>
<details><summary>Что за собеседование и&nbsp;сколько оно стоит?</summary><p>Час личного разговора о&nbsp;твоей ситуации. Для тех, кто пришёл с&nbsp;этого сайта, собеседование бесплатное. По&nbsp;итогам обе стороны честно решают, идти&nbsp;ли дальше; условия модулей обсуждаются там&nbsp;же.</p></details>
<details><summary>Какие гарантии?</summary><p>Честная одна. Мы&nbsp;даём процесс, группу, сопровождение и 16&nbsp;лет опыта. Дальше метод срабатывает ровно настолько, насколько включаешься ты, поэтому результат у&nbsp;каждого свой.</p></details>
<details><summary>Как попасть на тренинг?</summary><p>Школа растёт через рекомендации, без массовой рекламы. Первый шаг один для всех: собеседование. Запись через Telegram, кнопка ниже.</p></details>
<p style="margin-top:28px"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a></p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Продолжение</p>
<h2>Деньги, здоровье, близкие</h2>
<details><summary>Сколько это стоит и&nbsp;почему цены нет на&nbsp;сайте?</summary><p>Условия называем на&nbsp;собеседовании, когда уже видно, с&nbsp;какого модуля тебе заходить и нужен&nbsp;ли он вообще сейчас. Цифра без этого разговора ничего не&nbsp;объясняет: кому-то хватает первой ступени, кто-то идёт всю программу с&nbsp;сопровождением. Для тех, кто решает идти дальше, бывает льготная запись, и о&nbsp;ней мы&nbsp;говорим прямо, без таймеров на&nbsp;экране.</p></details>
<details><summary>А&nbsp;если не&nbsp;пойдёт? Можно уйти с&nbsp;середины?</summary><p>Да, и&nbsp;уговаривать никто не&nbsp;станет. Скажи об&nbsp;этом ведущим в&nbsp;зале, это разговор на&nbsp;две минуты. По&nbsp;опыту групп люди путают два разных состояния: «мне здесь не&nbsp;место» и&nbsp;«меня подводят к&nbsp;тому, куда я&nbsp;смотреть не&nbsp;хочу». Второе к&nbsp;вечеру чаще всего оборачивается самой важной частью&nbsp;модуля.</p></details>
<details><summary>Сколько времени занимает ежедневная практика?</summary><p>Пять минут утром на&nbsp;намерение и столько&nbsp;же вечером на&nbsp;открытия с&nbsp;благодарностями. У&nbsp;командного чата есть часы: первая запись до&nbsp;десяти, итог дня до&nbsp;двадцати двух. Раз в&nbsp;неделю встреча с&nbsp;ведущими, от&nbsp;получаса до&nbsp;часа, смотря сколько вопросов. Всё остальное происходит внутри обычного дня, отдельного часа практика не&nbsp;просит.</p></details>
<details><summary>Партнёр идти не&nbsp;хочет. Что тогда?</summary><p>Идти самому. Уговоры дают обратный ход: человек приезжает с&nbsp;чужим решением и&nbsp;все дни закрывается. Чаще выходит иначе: один проходит модуль, дома меняется тон разговоров, и&nbsp;через несколько недель второй записывается сам. Те, кто приезжает вдвоём, разбирают на&nbsp;сцене обе стороны одного сюжета: <a href="/chizhovy2/para/">про парный формат&nbsp;здесь</a>.</p></details>
<details><summary>Есть&nbsp;ли ограничения по&nbsp;здоровью?</summary><p>Скажи на&nbsp;собеседовании про диагнозы, лекарства, беременность и&nbsp;свежие потери: от&nbsp;этого зависит нагрузка. Дни в&nbsp;зале длинные, спишь меньше обычного, эмоции живые. Если человек сейчас в&nbsp;остром состоянии, в&nbsp;горе первых недель или в&nbsp;зависимости, мы&nbsp;просим сначала разобраться с&nbsp;этим и&nbsp;подсказываем, куда пойти. Лечения тренинг не&nbsp;заменяет.</p></details>
<details><summary>Что с&nbsp;записью и&nbsp;конфиденциальностью?</summary><p>Чужую работу в&nbsp;зале не&nbsp;снимают. Общие кадры бывают на&nbsp;выпуске и&nbsp;только с&nbsp;согласия тех, кто попал в&nbsp;объектив. Всё, что опубликовано на&nbsp;этом сайте, поставлено с&nbsp;разрешения авторов, имена убраны. Правило зала держится на&nbsp;простом: своим опытом делись сколько хочешь, чужую историю не выноси&nbsp;никогда.</p></details>
<details><summary>Я из&nbsp;другого города. Как быть?</summary><p>Первые два модуля очные, в&nbsp;Москве, и&nbsp;ради них люди едут издалека. Эти дни лучше прожить рядом с&nbsp;залом: если каждый вечер возвращаться в&nbsp;привычную обстановку, половина работы уходит впустую. Третий модуль идёт онлайн, встреча раз в&nbsp;неделю плюс командный чат, и&nbsp;там география уже не&nbsp;важна.</p></details>
<details><summary>Кто обычно в&nbsp;зале?</summary><p>Десять-двадцать человек, чаще всего от&nbsp;тридцати до&nbsp;пятидесяти лет. В&nbsp;одной из&nbsp;недавних групп рядом работали строитель со&nbsp;своей бригадой, эйчар большой компании, риелтор, фотограф и&nbsp;несколько предпринимателей. Профессия в&nbsp;зале ничего не&nbsp;решает: истории у&nbsp;всех разные, а&nbsp;круг, по&nbsp;которому человек ходит годами, часто один и тот&nbsp;же.</p></details>
<details><summary>Обязательно&nbsp;ли идти дальше первого модуля?</summary><p>Нет. Каждая ступень закончена сама по&nbsp;себе, а&nbsp;решение о&nbsp;следующей принимается через три-пять недель, когда увиденное уже проверено обычной жизнью. Кто-то останавливается после первого и&nbsp;спокойно живёт с&nbsp;этим дальше. А&nbsp;бывает, что команда доходит до&nbsp;третьего почти в полном&nbsp;составе.</p></details>
</div>
<aside class="side">
<div class="box"><div class="lbl">Формат</div><div class="big">2,5 + 5</div><p>Столько дней очно на&nbsp;первых двух модулях. Третий идёт три месяца внутри обычной жизни, без отрыва от&nbsp;дел.</p></div>
<div class="box"><div class="lbl">Возраст</div><div class="big">30-50</div><p>Обычная вилка группы. Верхней и&nbsp;нижней границы у&nbsp;нас нет, решает готовность работать.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-voprosy.jpg" alt="Спрашивают почти все" loading="lazy"></div>
<div>
<p class="eyebrow">Перед стартом</p>
<h2 style="font-size:1.9rem">Спрашивают почти все</h2>
<p>Ниже честные ответы на&nbsp;вопросы, которые задают до&nbsp;первого модуля.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Коротко о&nbsp;главном</p>
<h2>Четыре ответа до&nbsp;всех вопросов</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('calendar','var(--copper)')}<h3>Формат</h3><p>Три ступени: 2,5&nbsp;дня очно, 5&nbsp;дней очно и&nbsp;три месяца сопровождения. Между очными ступенями недели на&nbsp;проверку в&nbsp;жизни.</p></div>
<div class="card">{icon('people')}<h3>Группа</h3><p>10-20 человек, ведут двое. К&nbsp;третьему дню участники знают друг друга по&nbsp;имени.</p></div>
<div class="card">{icon('shield','var(--sage-deep)')}<h3>Вход</h3><p>Через собеседование. Мы&nbsp;смотрим, наша&nbsp;ли это задача, и&nbsp;говорим прямо, если сейчас не&nbsp;время.</p></div>
<div class="card">{icon('coins','var(--sand)')}<h3>Условия</h3><p>Стоимость и&nbsp;даты обсуждаем на&nbsp;собеседовании: они зависят от&nbsp;набора и&nbsp;ступени.</p></div>
</div>
</div></section>

""")

# ================= СЕССИЯ =================
P["sessiya/index.html"] = ("Собеседование в школу · Настоящие отношения",
"Живой разговор о твоей ситуации: как проходит, что спрашивают, что будет после. Для читателей сайта бесплатно.", "sessiya", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-sessiya.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Первый шаг</p><h1>Собеседование в&nbsp;школу</h1>
<p class="lead">Живой разговор о&nbsp;твоей ситуации. Знакомимся, разбираемся вместе и&nbsp;решаем, по&nbsp;пути ли&nbsp;нам. Для&nbsp;читателей сайта бесплатно.</p>
<div class="acts"><a class="btn btn-copper" href="https://t.me/+LVptSH6Mt4hhYmFi">Записаться</a><a class="btn btn-ghost" href="#kak">Что будет на&nbsp;разговоре</a></div>
</div></div>

<section id="kak"><div class="narrow">
<h2>Как проходит</h2>
<div class="card white" style="margin:20px 0 12px">{icon('speech')}<h3>Ты рассказываешь</h3><p>Что происходит и&nbsp;что уже пробовал. Без подготовки и&nbsp;правильных слов: как&nbsp;есть. Сумбурно, с&nbsp;паузами, перескакивая с&nbsp;темы на&nbsp;тему: нормально. Мы&nbsp;слушаем и&nbsp;задаём вопросы.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('gear','var(--sage-deep)')}<h3>Разбираем, как это устроено</h3><p>Где в&nbsp;твоей истории крутится сценарий и&nbsp;что его держит. Обычно уже этот час даёт первое «вот оно&nbsp;что»: человек видит свой круг со&nbsp;стороны, часто впервые за&nbsp;годы. Опора та&nbsp;же, что и в&nbsp;зале: <a href="/chizhovy2/metod/">событийный круг</a> из&nbsp;четырёх точек.</p></div>
<div class="card white">{icon('route','var(--sand)')}<h3>Вместе решаем, что дальше</h3><p>Годится&nbsp;ли тебе школа, с&nbsp;какого модуля заходить и стоит&nbsp;ли вообще. Отговорить можем так&nbsp;же честно, как&nbsp;пригласить. Условия участия обсудим здесь&nbsp;же, спокойно и&nbsp;без давления.</p></div>

<div class="nails nails3" style="margin-top:28px">
<div class="nail"><b>60&nbsp;минут</b><span>личного разговора, онлайн или&nbsp;очно</span></div>
<div class="nail"><b>Бесплатно</b><span>для тех, кто пришёл с этого&nbsp;сайта</span></div>
<div class="nail"><b>1</b><span>честный разговор о&nbsp;твоей&nbsp;задаче</span></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Чтобы не&nbsp;было сюрпризов</p>
<h2>О чём обычно спрашиваем</h2>
<p class="sub">Готовиться не&nbsp;нужно, но&nbsp;если хочется понимать заранее, вот примерные направления разговора. Отвечать на&nbsp;все не&nbsp;обязательно.</p>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('target')}<h3>Что происходит сейчас</h3><p>Какая ситуация привела тебя сюда: отношения, состояние, дело, здоровье. Что именно болит и как&nbsp;давно.</p></div>
<div class="card">{icon('loop','var(--sage-deep)')}<h3>Что повторяется</h3><p>Есть&nbsp;ли сюжет, который идёт по&nbsp;кругу с&nbsp;разными людьми или в&nbsp;разных местах. Обычно человек называет его сам за пять&nbsp;минут.</p></div>
<div class="card">{icon('book','var(--sand)')}<h3>Что уже пробовал</h3><p>Книги, курсы, терапия, спорт, смена работы. Это важно: значит, ты не&nbsp;сидел сложа руки, и мы не&nbsp;будем предлагать пройденное.</p></div>
<div class="card">{icon('sunrise')}<h3>К чему хочешь прийти</h3><p>Как выглядит жизнь, ради которой стоит идти в&nbsp;работу. Даже приблизительный ответ показывает направление.</p></div>
</div>
</div></section>


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как проходит разговор</p>
<h2>Как идёт разговор</h2>
<p>Созваниваемся в&nbsp;удобное время, обычно вечером. Никакой подготовки не&nbsp;нужно: не&nbsp;надо формулировать запрос, вспоминать детство или писать список целей. Достаточно прийти с&nbsp;тем, что беспокоит прямо сейчас.</p>
<p>Начинаем с&nbsp;твоей ситуации. Что происходит, сколько это длится, что уже пробовал и&nbsp;чем закончилось. Мы&nbsp;задаём вопросы, но&nbsp;не&nbsp;по&nbsp;анкете: слушаем, где повторяется одно и&nbsp;то&nbsp;же, и&nbsp;называем это вслух. Часто именно здесь человек впервые видит свой круг целиком.</p>
<p>Дальше честно говорим, поможет&nbsp;ли тут наш метод. Если задача не&nbsp;наша, скажем прямо и&nbsp;подскажем, куда идти. Если наша, объясним, с&nbsp;чего начинать и&nbsp;почему именно с&nbsp;этого.</p>
<h3 style="margin-top:26px">Что спросить у&nbsp;нас</h3>
<p>Спрашивают обычно про формат, про группу, про стоимость и&nbsp;про то, будет&nbsp;ли тяжело. Отвечаем на&nbsp;всё, включая неудобное: сколько стоит каждый модуль, что делать, если не&nbsp;пойдёт, и&nbsp;почему мы&nbsp;не&nbsp;даём гарантий.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Когда</div><p>В&nbsp;удобное время, чаще вечером. Созвон или встреча, как тебе&nbsp;удобнее.</p></div>
<div class="box"><div class="lbl">Подготовка</div><p>Не&nbsp;нужна. Приходи с&nbsp;тем, что беспокоит прямо сейчас.</p></div>
<div class="box"><div class="lbl">После</div><p>Решение принимаешь сам. Мы&nbsp;берём в&nbsp;группу тех, кто пришёл менять, а&nbsp;не&nbsp;пробовать.</p></div>
</aside>
</div></div></section>

<section class="dark"><div class="narrow">
<h2>Чего на&nbsp;собеседовании не&nbsp;будет</h2>
<p>Мы&nbsp;знаем, чего люди опасаются, когда идут «на&nbsp;разговор со&nbsp;школой». Поэтому говорим прямо.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('shield','var(--copper)')}<h3>Уговоров</h3><p>Мы&nbsp;не&nbsp;уговариваем и&nbsp;не&nbsp;торопим с&nbsp;ответом. При&nbsp;этом разговор нужен тому, кто уже решил менять, а&nbsp;не&nbsp;тому, кто зашёл послушать.</p></div>
<div class="card">{icon('speech','var(--copper)')}<h3>Скриптов и&nbsp;менеджеров</h3><p>Разговор ведут те, кто ведёт группы. Не&nbsp;отдел продаж и не&nbsp;бот с&nbsp;анкетой.</p></div>
<div class="card">{icon('lens','var(--copper)')}<h3>Ярлыков и&nbsp;диагнозов</h3><p>Мы не&nbsp;объясняем человеку, какой он, и не&nbsp;выдаём заключений. Смотрим на&nbsp;механику повтора, а не на&nbsp;личность.</p></div>
<div class="card">{icon('gear','var(--copper)')}<h3>Обещаний чуда</h3><p>Гарантий перемен не&nbsp;даём: метод срабатывает там, где человек включается сам. Об&nbsp;этом честно говорим сразу.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">После разговора</p>
<h2>Что происходит после</h2>
<p>Если по&nbsp;итогам разговора мы&nbsp;оба видим, что дорога общая, ты&nbsp;узнаёшь даты ближайшего набора, условия участия и с&nbsp;какого модуля заходить: чаще всего это первый, 2,5&nbsp;дня. Дальше решение за&nbsp;тобой: никто не&nbsp;звонит с&nbsp;напоминаниями и не&nbsp;шлёт «последний шанс».</p>
<p>Если видим, что сейчас не&nbsp;время или задача не&nbsp;наша, тоже скажем прямо и&nbsp;подскажем, куда смотреть. Такие разговоры у&nbsp;нас бывают, и мы&nbsp;считаем их&nbsp;нормальной частью работы: <a href="/chizhovy2/bezopasnost/">границы описаны отдельно</a>.</p>
<div class="pull"><div class="q">«Труднее всего было принять точку&nbsp;А. Принять, что мир это зеркало, и&nbsp;всё, что со&nbsp;мной происходит, я&nbsp;транслирую сам.»</div><div class="who">Участник тренинга</div></div>
<p>Многие говорят, что уже сам этот разговор сдвинул что-то с&nbsp;места: за 16&nbsp;лет через такие встречи прошли сотни человек, а в&nbsp;группу мы&nbsp;берём по&nbsp;10-20. Так и&nbsp;задумано: беседа строится по той&nbsp;же логике, что и&nbsp;работа в&nbsp;зале, просто в&nbsp;очень коротком формате. Что бывает дальше, можно почитать в&nbsp;<a href="/chizhovy2/istorii/">историях учеников</a>, а&nbsp;частые опасения разобраны на&nbsp;странице <a href="/chizhovy2/somneniya/">сомнений</a>.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Сколько идёт</div><p>Столько, сколько нужно. Кому-то хватает двадцати минут, с&nbsp;кем-то говорим дольше. Второго круга и&nbsp;«мы&nbsp;вам перезвоним» не&nbsp;будет.</p></div>
<div class="box"><div class="lbl">Сколько стоит</div><div class="big">0 ₽</div><p>Для читателей сайта бесплатно. Оплата обсуждается только если решаешь идти в&nbsp;модуль.</p></div>
<div class="box"><div class="lbl">Кто напротив</div><p>Разговор ведут те, кто ведёт группы: Алексей или Ирина. Не&nbsp;отдел продаж и не&nbsp;бот с&nbsp;анкетой.</p></div>
</aside>
</div></div></section>

<section><div class="narrow">
<div style="background:var(--linen);border:1px solid var(--line);border-radius:10px;padding:34px">
<h3 style="font-size:1.5rem">Записаться</h3>
<p class="sub" style="margin:10px auto 22px">Напиши слово «собеседование» в&nbsp;наш Telegram, и мы&nbsp;согласуем время. Отвечаем лично, без ботов и&nbsp;рассылок.</p>
<a class="btn btn-wine" href="https://t.me/+LVptSH6Mt4hhYmFi">Написать в&nbsp;Telegram</a>
<p class="note" style="margin-top:18px">Ещё не&nbsp;готов писать? Начни с&nbsp;<a href="/chizhovy2/gid/">бесплатного гайда</a>: там ядро метода и&nbsp;самодиагностика на&nbsp;десять пунктов.</p>
</div>
</div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/real/real-01.jpg" alt="Группа школы" loading="lazy"></div>
<div>
<p class="eyebrow">К чему ведёт разговор</p>
<h2 style="font-size:1.9rem">Что будет дальше</h2>
<p>На&nbsp;собеседование приходят с&nbsp;намерением что-то поменять, а&nbsp;не&nbsp;просто поговорить. Если по&nbsp;итогам решаем идти дальше, следующий шаг это первый модуль: небольшая группа, 2,5&nbsp;дня очно.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-chashki.jpg" alt="Разговор на двоих" loading="lazy"></div>
<div>
<p class="eyebrow">Как это выглядит</p>
<h2 style="font-size:1.9rem">Разговор на&nbsp;двоих</h2>
<p>Без анкет и&nbsp;скриптов. Ты&nbsp;рассказываешь, что происходит, мы&nbsp;задаём вопросы и&nbsp;называем вслух то, что видим. Дальше вместе решаем, по&nbsp;пути&nbsp;ли нам.</p>
</div>
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
    return f"""<section><div class="narrow">
<p class="eyebrow">Другие истоки метода</p>
<div class="chiplist">{links}<a href="/chizhovy2/istoki/">Все истоки</a></div>
</div></section>"""

MOST = """<section><div class="narrow">
<h2>Читать полезно, а&nbsp;меняет жизнь работа в&nbsp;зале</h2>
<p class="sub">Книги дают карту, а&nbsp;сценарий переписывается в&nbsp;зале, телом и&nbsp;эмоцией. Начни с&nbsp;бесплатного гайда или приходи на&nbsp;собеседование: разговор о твоей&nbsp;ситуации.</p>
<p class="btns"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>"""

MOST = """<section><div class="narrow">
<h2>Читать полезно, а&nbsp;меняет жизнь работа в&nbsp;зале</h2>
<p class="sub" style="margin:0 0 26px">Книги дают карту, а&nbsp;сценарий переписывается в&nbsp;зале, телом и&nbsp;эмоцией. Начни с&nbsp;бесплатного гайда или приходи на&nbsp;собеседование: разговор о твоей&nbsp;ситуации.</p>
<p class="btns"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>"""

P["istoki/index.html"] = ("Истоки метода · Настоящие отношения",
"Психодрама Морено, трансерфинг Зеланда, est, Годдард и наука: из чего собран метод школы и что мы переработали за 16 лет.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-hero.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки метода</p><h1>Из чего собран метод</h1>
<p class="lead">Любая сильная школа выросла из&nbsp;чужих идей. Мы&nbsp;называем свои опоры открыто: вот авторы, у&nbsp;которых мы&nbsp;взяли лучшее, и&nbsp;вот что мы с&nbsp;этим сделали за 16&nbsp;лет живой практики.</p></div></div>

<section><div class="narrow">
<h2>Почему мы&nbsp;это показываем</h2>
<p>На&nbsp;рынке принято прятать истоки: метод подаётся как озарение основателя, а&nbsp;источники остаются за&nbsp;кадром. Нам такой театр не&nbsp;нужен. Взрослый человек имеет право знать, на&nbsp;что опирается, и&nbsp;проверить каждый корень нашей&nbsp;работы.</p>
<p>К тому&nbsp;же честность про истоки сама по&nbsp;себе часть метода. Путь ученика начинается с точки&nbsp;А: признать, где ты на&nbsp;самом деле. Мы&nbsp;делаем то&nbsp;же самое: показываем, откуда выросли.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Пять опор</p>
<h2>Карта истоков</h2>
<div class="grid3" style="margin-top:28px">
<div class="card"><span class="bignum">01</span>{icon('people')}<h3>Якоб Морено: психодрама</h3><p>Живая сцена вместо разговоров о&nbsp;жизни. Академическое ядро метода: обмен ролями, дублирование, работа группой. Психодраме сто лет, и&nbsp;она до&nbsp;сих пор глубже большинства&nbsp;новинок.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/moreno-psihodrama/">Разобрать</a></p></div>
<div class="card"><span class="bignum">02</span>{icon('loop','var(--sage-deep)')}<h3>Вадим Зеланд: трансерфинг</h3><p>Маятники, важность, намерение, зеркало мира. Язык, на&nbsp;котором ученики школы описывают свою ежедневную практику.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/zeland-transerfing/">Разобрать</a></p></div>
<div class="card"><span class="bignum">03</span>{icon('flame','var(--sand)')}<h3>est: тренинги погружения</h3><p>Сан-Франциско, 1971&nbsp;год, Вернер Эрхард. Два уикенда, которые делили жизнь надвое. Корень жанра, в&nbsp;котором работает наша группа.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/est-transformaciya/">Разобрать</a></p></div>
<div class="card"><span class="bignum">04</span>{icon('sunrise')}<h3>Невилл Годдард: состояние</h3><p>«Реальность откликается на&nbsp;состояние». Основа практики намерения, которую ученики ведут девяносто дней Марафона.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/goddard/">Разобрать</a></p></div>
<div class="card"><span class="bignum">05</span>{icon('lamp','var(--sage-deep)')}<h3>Наука: почему это работает</h3><p>ЛеДу, Гоулман, Болте Тейлор, Голвитцер, Либерман. Каждый термин истоков стоит у&nbsp;нас на научной&nbsp;подпорке.</p><p style="margin-top:12px"><a href="/chizhovy2/istoki/nauka/">Разобрать</a></p></div>
<div class="card linen"><span class="bignum">06</span>{icon('lens')}<h3>Сплав: наш метод</h3><p>Сцена Морено, язык Зеланда, формат погружения, практика состояния и&nbsp;наука в&nbsp;одном процессе, проверенном 16&nbsp;годами групп.</p><p style="margin-top:12px"><a href="/chizhovy2/metod/">Как устроен метод</a></p></div>
</div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Одной схемой</p>
<h2>Пять источников, один метод</h2>
<div class="only-d" style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:30px 22px 18px;margin-top:26px">{splav_svg()}</div>
<div class="only-m" style="margin-top:22px">
<div class="chiplist" style="text-align:center"><span>Морено · сцена</span><span>Зеланд · язык</span><span>est · формат</span><span>Годдард · состояние</span><span>Наука · проверка</span></div>
<div style="text-align:center;color:var(--sand);font-size:1.4rem;line-height:1;margin:4px 0 10px">↓</div>
<div class="card white" style="text-align:center"><h3 style="margin-bottom:4px">Метод школы</h3><p>16 лет зала, сотни историй</p></div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Как читать эту карту</p>
<h2>Что каждый исток дал методу</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('people','var(--copper)')}<h3>Морено дал сцену</h3><p>Способ работать не&nbsp;разговором, а&nbsp;действием. Ситуация выносится в&nbsp;центр зала и&nbsp;проигрывается заново.</p></div>
<div class="card">{icon('pendulum')}<h3>Зеланд дал язык</h3><p>Короткие слова для&nbsp;сложных вещей: маятник, важность, зеркало. Ими группа объясняется с&nbsp;первого дня.</p></div>
<div class="card">{icon('layers','var(--sage-deep)')}<h3>est дал формат</h3><p>Несколько дней подряд без выхода в&nbsp;привычную жизнь, жёсткие правила зала, слово как&nbsp;обязательство.</p></div>
<div class="card">{icon('sunrise','var(--sand)')}<h3>Годдард дал состояние</h3><p>Работу с&nbsp;тем, из&nbsp;какого состояния человек входит в&nbsp;день. Отсюда утреннее намерение и&nbsp;вечерний разбор.</p></div>
<div class="card">{icon('gear')}<h3>Наука дала проверку</h3><p>Объяснение, почему это работает: ЛеДу, Болте Тейлор, Голвитцер, Либерман. Не&nbsp;вера, а&nbsp;механизм.</p></div>
<div class="card">{icon('lens','var(--copper)')}<h3>Зал дал отбор</h3><p>Шестнадцать лет практики решали, что остаётся. Красивое, но&nbsp;неработающее отсеивалось само.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Как мы работаем с истоками</h2>
<ol class="steps" style="margin-top:18px;margin-left:22px">
<li style="margin-bottom:12px"><b>Берём рабочее.</b> Из&nbsp;каждой школы мы&nbsp;взяли то, что раз за&nbsp;разом даёт результат в&nbsp;зале, и&nbsp;оставили за&nbsp;бортом всё, что красиво звучит и&nbsp;ничего не&nbsp;меняет.</li>
<li style="margin-bottom:12px"><b>Перерабатываем.</b> На&nbsp;каждой странице истоков честный разбор: что автор говорил, что мы&nbsp;взяли и&nbsp;что переработали под живую групповую работу.</li>
<li><b>Проверяем практикой.</b> Единственный судья: изменения в&nbsp;жизни учеников. Всё, что осталось в&nbsp;методе, прошло через сотни историй.</li>
</ol>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как пять опор сходятся&nbsp;вместе</p>
<h2>Один день модуля&nbsp;по&nbsp;частям</h2>
<p>Проще всего показать на&nbsp;обычном дне. Утро начинается с&nbsp;намерения: человек пишет, из&nbsp;какого состояния идёт в&nbsp;этот день и&nbsp;что создаёт. Годдард, доведённый до&nbsp;трёх строк&nbsp;в&nbsp;блокноте.</p>
<p>Дальше зал. Стулья по&nbsp;кругу, в&nbsp;середине пустое место, и&nbsp;разговор про отца за&nbsp;пару минут превращается в&nbsp;живую сцену, где отец сидит напротив и&nbsp;отвечает. Это Морено: методу сто лет, и&nbsp;ничего быстрее до&nbsp;сих пор&nbsp;не&nbsp;придумали.</p>
<p>Рамка вокруг всего этого пришла от&nbsp;est: несколько дней подряд, ясные правила, длинный день, из&nbsp;которого не&nbsp;выпрыгнуть в&nbsp;привычные дела и&nbsp;звонки. За&nbsp;два часа встречи человек не&nbsp;успевает выйти из-под своей&nbsp;защиты.</p>
<p>Вечером разбор на&nbsp;языке, который прижился в&nbsp;группах: где сегодня зацепило, где снял важность, что заметил за&nbsp;собой. Здесь удобен словарь Зеланда. А&nbsp;под всем этим лежит наука: полторы минуты паузы после сильного момента, названное вслух чувство, точная формулировка намерения. Пять источников не&nbsp;лежат по&nbsp;отдельным полкам, человек проходит через все за&nbsp;один&nbsp;день.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Как устроена программа</div><div class="big">3 модуля</div><p>Первый идёт два с&nbsp;половиной дня, второй пять, третий растянут на&nbsp;три месяца и&nbsp;живёт прямо в&nbsp;буднях, с&nbsp;командой и&nbsp;разборами.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Наша часть&nbsp;работы</p>
<h2>Что мы&nbsp;добавили к&nbsp;чужим&nbsp;находкам</h2>
<p>Своё в&nbsp;методе тоже есть, и&nbsp;это не&nbsp;мелочь. Мы&nbsp;называем это событийным кругом: карта, по&nbsp;которой видно, как давняя ситуация до&nbsp;сих пор управляет сегодняшними реакциями. В&nbsp;неё и&nbsp;собираются все инструменты, иначе они рассыпаются на&nbsp;красивые&nbsp;упражнения.</p>
<p>За&nbsp;бортом осталось многое. Залы на&nbsp;сотни человек, где ведущий работает с&nbsp;массой. Разовые погружения без&nbsp;продолжения: уезжаешь на&nbsp;подъёме, а&nbsp;через три недели живёшь как жил. И&nbsp;чтение вместо практики, самая распространённая ловушка умного&nbsp;взрослого.</p>
<h3>Надо ли&nbsp;читать что-то&nbsp;до&nbsp;старта</h3>
<p>Не&nbsp;обязательно. Книга Зеланда стоит в&nbsp;списке чтения на&nbsp;Марафоне, Рейнхарта берут те, кому интересно устройство жанра, а&nbsp;остальное происходит уже&nbsp;в&nbsp;зале.</p>
<h3>Я&nbsp;уже проходил другие&nbsp;тренинги</h3>
<p>Это частый случай. На&nbsp;собеседовании разбираем, что уже пройдено и&nbsp;где именно остановилось: обычно человек упирается не&nbsp;в&nbsp;новую технику, а&nbsp;в&nbsp;одно и&nbsp;то&nbsp;же&nbsp;место своей&nbsp;истории.</p>
<h3>А&nbsp;если опыта работы над собой нет&nbsp;совсем</h3>
<p>Многие так и&nbsp;приходят. Первый модуль как раз про то, чтобы увидеть свои повторы, и&nbsp;никакой подготовки для&nbsp;этого не&nbsp;требуется.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Своя рамка</div><div class="big">4 шага</div><p>Событие, эмоция, решение, повторяющийся сценарий. Как это разбирают в&nbsp;зале, на&nbsp;странице <a href="/chizhovy2/metod/">метода</a>.</p></div>
<div class="box"><div class="lbl">Отбор на&nbsp;входе</div><div class="big">Собеседование</div><p>Разговор о&nbsp;твоей ситуации до&nbsp;всякой оплаты. Иногда честный итог такой: сейчас идти&nbsp;не&nbsp;нужно.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-istoki.jpg" alt="Как они сошлись в один метод" loading="lazy"></div>
<div>
<p class="eyebrow">Пять источников</p>
<h2 style="font-size:1.9rem">Как они сошлись в&nbsp;один метод</h2>
<p>Психодрама, состояние, формат погружения, язык и&nbsp;наука. Каждый исток дал своё.</p>
</div>
</div>
</div></section>

{MOST}
""")

P["istoki/moreno-psihodrama/index.html"] = ("Якоб Морено и психодрама · Истоки метода",
"Психодрама: живая сцена, обмен ролями, пустой стул. Что школа взяла у Морено и что переработала.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/metod-scena.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Психодрама</p><h1 style="font-size:clamp(1.75rem,6vw,3.7rem)">Сцена вместо рассказа</h1>
<p class="lead">Якоб Леви Морено, венский психиатр, ещё в 1921&nbsp;году заметил: человек меняется на&nbsp;сцене быстрее, чем в&nbsp;кресле напротив врача. Так родилась психодрама, академическое ядро нашего&nbsp;метода.</p></div></div>

<section><div class="narrow">
<h2>Что придумал Морено</h2>
<p>Морено (1889-1974) начинал с&nbsp;«театра спонтанности» в&nbsp;Вене: обычные люди разыгрывали на&nbsp;сцене не&nbsp;пьесы, а&nbsp;собственные истории. И он&nbsp;заметил странное. В&nbsp;такой игре человек вдруг выходит из&nbsp;заученной роли и&nbsp;находит новый ответ на&nbsp;старую ситуацию. Позже, уже в&nbsp;Америке, наблюдение превратилось в&nbsp;метод, которым сегодня работают в десятках&nbsp;стран.</p>
<p>Главная ставка простая. О&nbsp;проблеме бесполезно рассказывать, в&nbsp;неё нужно вернуться. Участники группы становятся героями твоей истории, пространство зала превращается в ту&nbsp;кухню или тот кабинет, и сцена&nbsp;оживает.</p>
</div>
<div class="wrap"><div class="grid3" style="margin-top:26px">
<div class="card"><h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место отца, партнёра, начальника. Отвечаешь себе его словами. Пять минут в&nbsp;чужой роли дают больше, чем год&nbsp;объяснений.</p></div>
<div class="card"><h3>Дублирование</h3><p>Человек рядом договаривает то, что ты&nbsp;чувствуешь и не&nbsp;решаешься сказать. Невысказанное впервые звучит&nbsp;вслух.</p></div>
<div class="card"><h3>Зеркало</h3><p>Свою сцену играют другие, а ты&nbsp;смотришь со&nbsp;стороны, как зритель в&nbsp;зале. Иногда одного этого хватает, чтобы увидеть сценарий&nbsp;целиком.</p></div>
</div></div>
<div class="narrow">
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:26px">
<div class="nail"><b>1921</b><span>«театр спонтанности» в&nbsp;Вене: первая сцена&nbsp;метода</span></div>
<div class="nail"><b>100&nbsp;лет</b><span>психодраме: живой метод, а не модная&nbsp;новинка</span></div>
<div class="nail"><b>Десятки</b><span>стран, где психодрамой работают&nbsp;сегодня</span></div>
</div></div>
<div class="narrow">
<div class="pull"><div class="q">«Покажи мне, а не&nbsp;рассказывай». Этой фразой Морено развернул психологию своего времени.</div><div class="who">Принцип психодрамы</div></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что мы&nbsp;взяли и&nbsp;что переработали</h2>
<p><b style="color:#D08A5F">Взяли:</b> сцену как главный инструмент, группу как усилитель, пустой стул, обмен ролями. Разговор, который не&nbsp;случился в&nbsp;жизни, происходит у&nbsp;нас в&nbsp;зале. Тело проживает его&nbsp;по-настоящему.</p>
<p><b style="color:#D08A5F">Переработали:</b> у&nbsp;Морено спонтанность сама по&nbsp;себе считалась лекарством. Мы&nbsp;поставили сцену на&nbsp;карту событийного круга: она ведёт к&nbsp;конкретной точке, к&nbsp;старому решению, и&nbsp;там происходит перезапись. Сцена у&nbsp;нас средство. Цель это новый сценарий в&nbsp;жизни.</p>
<p>Поэтому после сцены работа не&nbsp;заканчивается. Решение закрепляется практикой между модулями и&nbsp;тремя месяцами&nbsp;Марафона.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/zeland-transerfing/", "Зеланд и трансерфинг"), ("/chizhovy2/istoki/nauka/", "Наука за методом"), ("/chizhovy2/metod/", "Метод целиком"))}
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как это&nbsp;началось</p>
<h2>Ангел на сцене, скандал за&nbsp;дверью</h2>
<p>В&nbsp;венском «театре спонтанности» начала двадцатых выступала молодая актриса, в&nbsp;записях Морено она проходит как Барбара. Ей&nbsp;доставались роли трогательных и&nbsp;нежных героинь, зал её&nbsp;обожал. Однажды после спектакля к&nbsp;режиссёру подошёл её&nbsp;муж Георг и&nbsp;рассказал, что дома всё наоборот: крики, битая посуда, оскорбления, а утром&nbsp;слёзы.</p>
<p>Морено сделал ход, которого от&nbsp;врача не&nbsp;ждут. Разбирать с&nbsp;Барбарой детство он не&nbsp;стал. Он&nbsp;дал ей&nbsp;другие роли: женщин с&nbsp;улицы, торговок, тех, кто орёт и&nbsp;хлопает дверью. Ярость, которая раньше доставалась мужу, начала выходить на&nbsp;публике, в&nbsp;безопасной форме игры. Через несколько недель Георг сказал, что дома стало тихо. Эту историю Морено потом называл одним из корней&nbsp;психодрамы.</p>
<p>Дальше всё пошло быстро. В&nbsp;1936 году он&nbsp;построил под Нью-Йорком лечебницу с&nbsp;круглой сценой в&nbsp;три яруса и&nbsp;балконом: пациенты выходили туда и&nbsp;проживали свою жизнь заново. День рождения метода он&nbsp;назначил сам, первое&nbsp;апреля.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Он&nbsp;придумал это слово</div><div class="big">1932</div><p>В&nbsp;этом году Морено предложил термин «групповая психотерапия». До&nbsp;него душевная работа считалась делом двоих: врача и&nbsp;пациента.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Психодрама в нашем&nbsp;зале</p>
<h2>Почему после сцены никто не даёт&nbsp;советов</h2>
<p>У&nbsp;Морено был твёрдый порядок: разогрев, действие, шеринг. Третье слово незнакомое, а&nbsp;вещь понятная. Когда работа закончилась, группа не&nbsp;обсуждает героя и не&nbsp;учит его жить. Каждый говорит про себя: что задело, где узнал свою историю. Правило железное, держат его&nbsp;ведущие.</p>
<p>Причина техническая. Человек выходит из&nbsp;процесса открытым, защита снята, и&nbsp;любая оценка в&nbsp;такую минуту бьёт по&nbsp;живому. Зато чужое «у&nbsp;меня было так же» делает обратное: сразу видно, что ты не один&nbsp;такой.</p>
<p>Вторая задача группы это вспомогательные Я. Участники становятся твоим отцом, партнёром, начальником, тобой самим в&nbsp;пятнадцать лет. Никто не&nbsp;изображает театр, реплики берутся из&nbsp;твоей же&nbsp;жизни. Обычно в&nbsp;этот момент человек впервые видит своё со&nbsp;стороны.</p>
<h3>Нужно ли уметь&nbsp;играть</h3>
<p>Нет, актёрских задач тут не&nbsp;ставят. Ты&nbsp;говоришь своими словами то, что и&nbsp;так носишь в&nbsp;себе. Роли раздаёт ведущий, и&nbsp;если фраза не&nbsp;идёт, рядом встаёт дублёр и&nbsp;договаривает за&nbsp;тебя.</p>
<h3>А&nbsp;если не&nbsp;захочу выходить в&nbsp;центр</h3>
<p>Выходят по&nbsp;своему решению, очередь никто не&nbsp;подгоняет. Работа при&nbsp;этом идёт и из&nbsp;зала: чужая сцена включает твою собственную память, и&nbsp;многие открытия случаются у&nbsp;тех, кто в&nbsp;этот раз просто сидел и&nbsp;смотрел.</p>
<h3>Останется ли это в&nbsp;группе</h3>
<p>Да. Всё, что прозвучало в&nbsp;зале, за&nbsp;его пределы не&nbsp;выносится, об&nbsp;этом договариваются в&nbsp;первый час первого модуля. Подробнее на&nbsp;странице про <a href="/chizhovy2/bezopasnost/">границы работы</a>.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Как устроен процесс</div><div class="big">3 части</div><p>Разогрев, действие, шеринг. Эту схему Морено собрал ещё в&nbsp;двадцатые, и с&nbsp;тех пор она почти не&nbsp;изменилась.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-moreno.jpg" alt="Сцена вместо рассказа" loading="lazy"></div>
<div>
<p class="eyebrow">Психодрама</p>
<h2 style="font-size:1.9rem">Главная находка Морено</h2>
<p>Морено заметил: человек меняется не&nbsp;когда рассказывает о&nbsp;ситуации, а&nbsp;когда проживает её&nbsp;заново.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Инструменты Морено</p>
<h2>Четыре приёма, дошедшие до&nbsp;наших залов</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('people')}<h3>Обмен ролями</h3><p>Человек встаёт на&nbsp;место другого и&nbsp;отвечает себе его словами. Морено считал это сердцем метода: понять другого можно только изнутри его роли.</p></div>
<div class="card">{icon('speech','var(--copper)')}<h3>Дублирование</h3><p>Кто-то из&nbsp;группы становится рядом и&nbsp;говорит вслух то, что герой чувствует, но&nbsp;не&nbsp;решается сказать.</p></div>
<div class="card">{icon('mirror','var(--sage-deep)')}<h3>Зеркало</h3><p>Герой выходит из&nbsp;сцены и&nbsp;смотрит, как её&nbsp;играют без него. Со&nbsp;стороны видно то, чего изнутри не&nbsp;поймать.</p></div>
<div class="card">{icon('lamp','var(--sand)')}<h3>Пустой стул</h3><p>На&nbsp;стуле «сидит» тот, с&nbsp;кем разговор так и&nbsp;не&nbsp;случился. Отложенный на&nbsp;годы разговор наконец происходит.</p></div>
</div>
<p class="sub" style="margin-top:24px">Подробный разбор каждого приёма и&nbsp;порядок работы в&nbsp;сцене собран на&nbsp;странице <a href="/chizhovy2/tehniki-sceny/">техник сцены</a>.</p>
</div></section>

{MOST}
""")

P["istoki/zeland-transerfing/index.html"] = ("Вадим Зеланд и трансерфинг · Истоки метода",
"Маятники, важность, намерение, зеркало мира: как язык трансерфинга работает в школе и что мы объясняем через мозг.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-zeland.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Трансерфинг</p><h1>Маятники, важность, зеркало мира</h1>
<p class="lead">С&nbsp;2004 года книги Вадима Зеланда «Трансерфинг реальности» разошлись миллионными тиражами. Для наших учеников это язык ежедневной практики: точный, образный и&nbsp;удобный в&nbsp;работе.</p></div></div>

<section><div class="narrow">
<h2>Три рабочие идеи</h2>
<div class="card white" style="margin:20px 0 12px">{icon('pendulum')}<h3>Маятники</h3><p>Структуры, которые кормятся твоей реакцией: скандал, лента новостей, чужая паника, офисная война. Дёрнулся, значит отдал энергию. У&nbsp;Зеланда это образ; в&nbsp;зале он&nbsp;становится навыком: заметить крючок и не&nbsp;схватиться.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('ceiling','var(--sage-deep)')}<h3>Важность</h3><p>Чем сильнее вцепился в&nbsp;результат, тем хуже он&nbsp;даётся: раздутая ставка парализует. Снятая важность возвращает лёгкость и&nbsp;точность. Знакомо по&nbsp;переговорам, по&nbsp;свиданиям, по&nbsp;любому «очень&nbsp;надо».</p></div>
<div class="card white">{icon('mirror','var(--sand)')}<h3>Зеркало мира</h3><p>Мир читает состояние. Слова для него шум. Пока внутри страх, снаружи собираются поводы бояться. Ученики после тренинга говорят коротко: мир&nbsp;зеркалит.</p></div>

<div style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:26px 18px 10px;margin-top:26px">{mayatnik_svg()}</div>
<div class="pull"><div class="q">«Отследил сегодня несколько маятников, не&nbsp;среагировал, и&nbsp;получилось удержать состояние весь день.»</div><div class="who">Из отчёта ученика на&nbsp;Марафоне</div></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что мы&nbsp;взяли и&nbsp;что переработали</h2>
<p><b style="color:#D08A5F">Взяли:</b> рабочий язык (он&nbsp;теперь живёт в&nbsp;нашем <a href="/chizhovy2/slovar/" style="color:#D08A5F">словаре школы</a>). На&nbsp;Марафоне трансерфинг входит в&nbsp;список чтения, а&nbsp;его термины живут в&nbsp;ежедневной практике: утром намерение, вечером разбор, где катался на&nbsp;маятниках и&nbsp;где удержал состояние.</p>
<p><b style="color:#D08A5F">Переработали:</b> у&nbsp;Зеланда это философия для самостоятельного чтения, и у&nbsp;неё есть слабое место: прочитал, восхитился, через месяц забыл. Мы&nbsp;дали каждому термину механизм и&nbsp;тренировку. Маятник у&nbsp;нас это твоя знакомая петля реакции, и&nbsp;её видно на&nbsp;событийном круге. Важность это ставка, которая включает страх и&nbsp;сжимает выбор. Чтение даёт понимание. Держать состояние учат девяносто дней практики с&nbsp;командой и&nbsp;разборами.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/goddard/", "Невилл Годдард"), ("/chizhovy2/istoki/est-transformaciya/", "est и «Трансформация»"), ("/chizhovy2/istoki/nauka/", "Наука за методом"))}
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Язык практики</p>
<h2>Почему эти слова прижились в&nbsp;зале</h2>
<p>Сам автор пишет под псевдонимом и&nbsp;почти не&nbsp;появляется на&nbsp;публике, зато его словарь разошёлся дальше книг. Причина в&nbsp;краткости. «Маятник» умещает в&nbsp;одно слово то, на&nbsp;что уходит абзац: чужой конфликт втягивает, ты&nbsp;отвечаешь, через минуту уже кричишь, а&nbsp;вечером не&nbsp;понимаешь, куда делись&nbsp;силы.</p>
<p>У&nbsp;нас проверка одна: термин годится, если после него человек может что-то сделать. Поэтому маятники мы не&nbsp;делим на&nbsp;добрые и&nbsp;злые. Это устройство, которое живёт твоей реакцией, и в&nbsp;разборе к&nbsp;нему идут три вопроса. Что здесь кормится мной. Зачем я&nbsp;сюда захожу и&nbsp;что мне тут нужно. Где сойти. Третий пункт самый важный: пока цель на&nbsp;виду, зайти можно куда угодно и&nbsp;выйти с&nbsp;тем, за чем&nbsp;пришёл.</p>
<p>С&nbsp;важностью та же&nbsp;история. После пяти дней второго модуля эта мысль расходится по&nbsp;вечерним отчётам почти дословно: страха нет, есть важность. Раздутая ставка включает тревогу и&nbsp;сжимает выбор до&nbsp;одного варианта, и он&nbsp;обычно худший из&nbsp;возможных.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Домашнее чтение</div><div class="big">5 ступеней</div><p>Столько частей у&nbsp;«Трансерфинга реальности». Книга стоит в&nbsp;списке чтения на&nbsp;все три месяца Марафона: одни читают её&nbsp;залпом, другие слушают в аудио за&nbsp;рулём.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как это выглядит в&nbsp;жизни</p>
<h2>Что пишут в отчётах первые&nbsp;недели</h2>
<p>Вечером каждый пишет открытия дня, коротко и&nbsp;своими словами. Вот дословно: «Я&nbsp;катаюсь на&nbsp;маятниках с&nbsp;самого утра. В&nbsp;обед вроде получилось вылезти в&nbsp;офигенное состояние. Но&nbsp;потом опять покатился». Поначалу это выглядит именно так, и&nbsp;такой текст мы&nbsp;считаем сильным: человек уже видит свой день&nbsp;изнутри.</p>
<p>Дальше навык растёт неровно. Сегодня заметил крючок и&nbsp;прошёл мимо, завтра влетел в&nbsp;спор в&nbsp;родительском чате и&nbsp;понял это только к&nbsp;ночи. Меняется другое: у&nbsp;дня появился вечер, где всё это видно, команда из&nbsp;10-20 человек рядом и&nbsp;еженедельный разбор с&nbsp;ведущими.</p>
<h3>Как проверить всё это на&nbsp;себе</h3>
<p>Семь дней и&nbsp;блокнот. Отмечай, где за&nbsp;день дёрнулся, и&nbsp;вечером смотри, сколько сил осталось. Обычно человек сам замечает, что почти всё съедают два или три постоянных места, и&nbsp;они у каждого&nbsp;свои.</p>
<h3>А&nbsp;если слово «маятник» не&nbsp;нравится</h3>
<p>Называй как удобно: втягивание, крючок, чужая игра. Держимся мы за&nbsp;навык, название тут вторично. В&nbsp;каждой группе через месяц появляются свои&nbsp;словечки.</p>
<h3>Чем этот исток отличается от&nbsp;соседних</h3>
<p>Зеланд отвечает на&nbsp;вопрос, куда за&nbsp;день уходит твоя сила. <a href="/chizhovy2/istoki/goddard/">Годдард</a> показывает, из&nbsp;какого состояния ты&nbsp;идёшь в&nbsp;день. <a href="/chizhovy2/istoki/moreno-psihodrama/">Морено</a> даёт инструмент, чтобы поменять то, что стоит за&nbsp;самой реакцией.</p>
</div>
<aside class="side">
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-zeland.jpg" alt="Маятник, который раскачивает" loading="lazy"></div>
<div>
<p class="eyebrow">Главная метафора</p>
<h2 style="font-size:1.9rem">Маятник, который раскачивает</h2>
<p>Структура живёт, пока в&nbsp;неё вкладывают эмоцию. Перестал раскачивать, и&nbsp;она отпустила.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Как это звучит в&nbsp;зале</p>
<h2>Три слова, которые команда говорит каждый день</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('pendulum','var(--copper)')}<h3>Маятник</h3><p>Структура, живущая на&nbsp;твоей эмоции: скандал в&nbsp;чате, спор в&nbsp;новостях, чужая паника. Перестал раскачивать, и&nbsp;она отпустила.</p></div>
<div class="card">{icon('ceiling')}<h3>Важность</h3><p>Раздутая ставка, которая включает страх и&nbsp;сжимает выбор. Снял важность, и&nbsp;решение принимается спокойно.</p></div>
<div class="card">{icon('mirror','var(--sage-deep)')}<h3>Зеркало</h3><p>Мир отражает состояние, а&nbsp;не&nbsp;желания. Поэтому работа идёт с&nbsp;состоянием, а&nbsp;не&nbsp;со&nbsp;списком целей.</p></div>
</div>
</div></section>

{MOST}
""")

P["istoki/est-transformaciya/index.html"] = ("est и «Трансформация» Рейнхарта · Истоки метода",
"Тренинг est Вернера Эрхарда и книга «Трансформация» Люка Рейнхарта: откуда пошёл жанр погружения и что школа сделала иначе.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-est.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · est</p><h1>С чего начался жанр</h1>
<p class="lead">Сан-Франциско, 1971&nbsp;год. Вернер Эрхард проводит первый тренинг est: два выходных подряд, жёсткие правила зала и&nbsp;сотни тысяч выпускников за&nbsp;тринадцать лет. Так родился жанр тренингов погружения, в&nbsp;котором работает и&nbsp;наша школа.</p></div></div>

<section><div class="narrow">
<h2>Что происходило в&nbsp;зале est</h2>
<p>Люди сидели в&nbsp;зале по&nbsp;шестнадцать часов, сдавали часы на&nbsp;входе и&nbsp;держали слово не&nbsp;вставать до&nbsp;перерыва. Ведущий разбирал их&nbsp;истории при всех, без анестезии. Звучит жёстко, так и&nbsp;было. Но у&nbsp;формата оказалась настоящая сила: за&nbsp;два уикенда защита психики, которую час терапии даже не&nbsp;царапает, снималась, и&nbsp;человек впервые видел свою жизнь без привычных оправданий.</p>
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
<div class="card"><h3>Понять и&nbsp;пережить</h3><p>est первым развёл эти вещи: понимание живёт в&nbsp;голове и&nbsp;ничего не&nbsp;сдвигает. Жизнь меняет только пережитый опыт. Вся индустрия погружений выросла из этого&nbsp;различия.</p></div>
<div class="card"><h3>Слово</h3><p>Личность строится из&nbsp;обещаний, которые ты&nbsp;держишь. Начал опаздывать на&nbsp;встречи с&nbsp;собой, значит сценарий уже водит тебя за&nbsp;руку.</p></div>
</div></div></section>

<section class="dark"><div class="narrow">
<h2>Что мы&nbsp;взяли и&nbsp;что переработали</h2>
<p><b style="color:#D08A5F">Взяли:</b> формат погружения на&nbsp;несколько дней, потому что психика открывается только в&nbsp;длинной работе. Правила зала как рамку безопасности. Честность без скидок: на&nbsp;собеседовании мы&nbsp;можем и&nbsp;отговорить, если школа не твой&nbsp;инструмент.</p>
<p><b style="color:#D08A5F">Переработали:</b> почти всё остальное. est работал залами по&nbsp;двести пятьдесят человек и&nbsp;провокацией; мы&nbsp;выбрали противоположный масштаб. Группы 10-20 участников, бережная глубина вместо давления, живая сцена взамен лекции и&nbsp;три месяца сопровождения после, чтобы результат не&nbsp;выветрился к&nbsp;понедельнику.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/moreno-psihodrama/", "Морено и психодрама"), ("/chizhovy2/istoki/zeland-transerfing/", "Зеланд и трансерфинг"), ("/chizhovy2/programma/", "Как устроены наши модули"))}
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Человек, с которого&nbsp;началось</p>
<h2>Жанр придумал продавец&nbsp;энциклопедий</h2>
<p>Вернер Эрхард появился на&nbsp;свет под другим именем. Джон Пол Розенберг родился в&nbsp;Филадельфии в&nbsp;1935 году, в&nbsp;1960 уехал из&nbsp;дома и&nbsp;взял себе новое имя, под которым его потом узнали сотни тысяч выпускников. Психологического образования у&nbsp;него не&nbsp;было. Была работа: сначала автомобили, потом энциклопедии, а&nbsp;дальше обучение&nbsp;продавцов.</p>
<p>Отсюда и&nbsp;вышла главная находка. Эрхард собрал не&nbsp;теорию, а&nbsp;формат: длинный зал, ясные правила, разбор при&nbsp;всех и&nbsp;никакого конспекта, который можно унести домой вместо изменений. Люди выходили оттуда с&nbsp;фразой «я&nbsp;понял», хотя новых знаний им&nbsp;никто не&nbsp;давал. Понимание там добывали из собственной&nbsp;жизни.</p>
<p>Дальше жанр разошёлся по&nbsp;миру и&nbsp;повзрослел. Залы на&nbsp;сотни человек сменились маленькими группами, провокация ушла, а&nbsp;формат погружения остался прежним: несколько дней подряд, без&nbsp;телефона в&nbsp;руке и без&nbsp;возможности сбежать в привычные&nbsp;дела.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Имя при&nbsp;рождении</div><div class="big">Розенберг</div><p>Он&nbsp;стал Вернером Эрхардом в&nbsp;1960 году. Через одиннадцать лет собрал первый тренинг в&nbsp;отеле Сан-Франциско, октябрь&nbsp;1971.</p></div>
<div class="box"><div class="lbl">Что читать</div><div class="big">1976</div><p>В&nbsp;этом году Люк Рейнхарт, автор «Дайсмена», выпустил книгу об&nbsp;est. Он&nbsp;описал эти два выходных изнутри, день за&nbsp;днём, репликами&nbsp;зала.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Куда мы это&nbsp;довели</p>
<h2>Обещание, данное себе в&nbsp;детстве</h2>
<p>У&nbsp;Эрхарда была сильная мысль про обещания: личность держится на&nbsp;том, что ты&nbsp;пообещал и&nbsp;выполнил. Мы&nbsp;довели её до&nbsp;конкретной работы. Тяжелее всего давит то, что человек когда-то сказал себе&nbsp;сам.</p>
<p>В&nbsp;зале такие фразы называют клятвами. Звучат они похоже: «я&nbsp;никогда не&nbsp;буду просить», «я&nbsp;всегда буду сильным», «меня больше никто не&nbsp;увидит слабой». Ребёнок в&nbsp;семь лет принимает решение, которое в&nbsp;тот день его спасает, и&nbsp;живёт по&nbsp;нему до&nbsp;сорока. Взрослый мужчина не&nbsp;может попросить о&nbsp;помощи и&nbsp;искренне считает это&nbsp;характером.</p>
<p>Работа идёт так: находим клятву, возвращаемся в&nbsp;день, когда она прозвучала, и&nbsp;там человек принимает <a href="/chizhovy2/tehniki-sceny/">новое решение</a> уже взрослыми глазами. Один участник написал в&nbsp;тот же&nbsp;вечер: «Когда работали с&nbsp;клятвой и&nbsp;новым решением, пошло какое-то наполнение что-ли. Прям кайф».</p>
<h3>Будут ли ломать и&nbsp;давить</h3>
<p>Нет. У&nbsp;Эрхарда провокация была инструментом, у&nbsp;нас работают глубина и&nbsp;время. Ведущих двое, в&nbsp;группе 10-20 человек, любой процесс можно остановить. Что в&nbsp;зале возможно и&nbsp;где проходит черта, описано на&nbsp;странице <a href="/chizhovy2/bezopasnost/">границ работы</a>.</p>
<h3>Сколько всё это&nbsp;занимает</h3>
<p>Первый модуль 2,5 дня, второй 5 дней, дальше три месяца сопровождения. У&nbsp;Эрхарда всё умещалось в&nbsp;два выходных, и&nbsp;это слабое место жанра: зал заканчивается, человек возвращается в ту же&nbsp;кухню и&nbsp;тот же&nbsp;офис. Три месяца нужны ровно затем, чтобы новое решение дожило до&nbsp;понедельника и&nbsp;осталось.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Формат сегодня</div><div class="big">10-20</div><p>Столько человек в&nbsp;нашей группе. У&nbsp;Эрхарда в&nbsp;зале сидели по&nbsp;двести пятьдесят, и&nbsp;каждый ждал очереди&nbsp;неделями.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-est.jpg" alt="Зал, где всё началось" loading="lazy"></div>
<div>
<p class="eyebrow">Формат</p>
<h2 style="font-size:1.9rem">Зал, где всё началось</h2>
<p>Эрхард собрал формат, в&nbsp;котором люди проводят вместе несколько дней подряд, без выхода в&nbsp;привычную жизнь.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Что осталось от&nbsp;формата</p>
<h2>Три вещи, взятые из&nbsp;est</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('layers','var(--copper)')}<h3>Несколько дней подряд</h3><p>Погружение работает, когда человек не&nbsp;возвращается каждый вечер в&nbsp;привычную жизнь. Защита успевает опуститься, и&nbsp;начинается настоящий разговор.</p></div>
<div class="card">{icon('shield')}<h3>Правила зала</h3><p>Приходить вовремя, телефоны выключены, ответственность за&nbsp;своё слово. Строго звучит, а&nbsp;работает быстро.</p></div>
<div class="card">{icon('speech','var(--sage-deep)')}<h3>Слово как&nbsp;обязательство</h3><p>Обещание, данное вслух при&nbsp;группе, держится иначе, чем мысленное. Отсюда работа с&nbsp;клятвами, которые человек дал себе когда-то давно.</p></div>
</div>
</div></section>

{MOST}
""")

P["istoki/goddard/index.html"] = ("Невилл Годдард · Истоки метода",
"Состояние готового итога: идея Невилла Годдарда, практика намерения на Марафоне и её научный двойник.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-goddard.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Годдард</p><h1>Состояние готового итога</h1>
<p class="lead">Невилл Годдард, лектор с&nbsp;Барбадоса, полвека собирал залы в&nbsp;Америке с&nbsp;одной мыслью: какое состояние, такие и&nbsp;события. Его идею наши ученики проверяют девяносто дней подряд.</p></div></div>

<section><div class="narrow">
<h2>Главная идея Годдарда</h2>
<div class="pull" style="margin-top:6px"><div class="q">«Все события уже существуют. Вы не&nbsp;создаёте их, вы&nbsp;входите в&nbsp;них, проживая состояние того, кем вы хотите&nbsp;быть.»</div><div class="who">Невилл Годдард (1905-1972)</div></div>
<p>Реальность откликается на&nbsp;состояние, а не на&nbsp;просьбу. Просить и&nbsp;ждать бесполезно, пока внутри ты&nbsp;остаёшься человеком, у&nbsp;которого «пока не&nbsp;получилось»: из&nbsp;такого состояния рождаются те&nbsp;же действия и те&nbsp;же события, что вчера. Годдард предлагал обратный ход: сначала прожить состояние человека, у&nbsp;которого уже есть, и&nbsp;дать ему вести решения.</p>
<p>Звучит смело. Но&nbsp;вспомни, как легко даётся день, когда ты с&nbsp;утра в&nbsp;силе, и&nbsp;как вязнет тот&nbsp;же список дел в&nbsp;день, когда внутри тяжесть. Состояние уже управляет твоими событиями. Вопрос только, кто держит руль.</p>
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
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Человек и его&nbsp;история</p>
<h2>Он собирался домой без денег на&nbsp;дорогу</h2>
<p>Невилл Годдард родился на&nbsp;Барбадосе в&nbsp;1905 году, в&nbsp;семнадцать лет приехал в&nbsp;Нью-Йорк учиться танцу и&nbsp;несколько лет выходил на&nbsp;бродвейскую сцену. Потом бросил всё ради лекций. Учителем его стал человек, которого он&nbsp;называл Абдуллой, и&nbsp;главный урок случился в 1933&nbsp;году.</p>
<p>Годдард хотел встретить Рождество на&nbsp;острове, у&nbsp;своих, а&nbsp;денег на&nbsp;дорогу не&nbsp;было совсем. Абдулла выслушал и&nbsp;ответил коротко: ты&nbsp;уже на&nbsp;Барбадосе. И&nbsp;велел каждый вечер укладываться спать так, будто ты&nbsp;уже дома. Годдард спорил про себя, злился, но&nbsp;делал ровно так. В&nbsp;начале декабря пришло письмо от&nbsp;брата: деньги и&nbsp;билет на&nbsp;пароход, третий класс. Перед самым отплытием кто-то отказался от&nbsp;каюты, и&nbsp;домой он поплыл&nbsp;первым.</p>
<p>Проверить эту историю сегодня невозможно, а&nbsp;рассказывал он её со&nbsp;сцены десятилетиями. Из&nbsp;неё выросло его единственное указание, и&nbsp;повторял он&nbsp;его до&nbsp;конца жизни: сначала стань тем, у&nbsp;кого уже получилось, и&nbsp;только потом смотри, что начнёт&nbsp;происходить.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Его формула</div><div class="big">Уже сбылось</div><p>Почувствуй, что желание исполнено, и&nbsp;живи из&nbsp;этого чувства. Десяток книг и&nbsp;сотни выступлений почти целиком про одно&nbsp;это.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Что из&nbsp;этого делаем&nbsp;мы</p>
<h2>Вечер важнее утра</h2>
<p>У&nbsp;Годдарда была своя вечерняя работа. Перед сном он&nbsp;пересматривал прошедший день и&nbsp;переигрывал в&nbsp;воображении момент, где всё пошло криво, чтобы не&nbsp;тащить старую запись в&nbsp;завтра. У&nbsp;нас вечер устроен по-своему: человек пишет открытия дня и&nbsp;благодарности, а&nbsp;команда это&nbsp;читает.</p>
<p>Звучит скромно, работает сильно. Утреннее намерение без&nbsp;вечернего разбора превращается в&nbsp;красивую строчку, о&nbsp;которой к&nbsp;обеду никто не&nbsp;помнит. Вечером же&nbsp;видно факт: где я&nbsp;сегодня был тем, кем решил быть с&nbsp;утра, а&nbsp;где меня унесло. Одна участница подсчитала на&nbsp;третьем месяце: к&nbsp;концу дня сбывается около 70 процентов написанного&nbsp;утром.</p>
<h3>Достаточно ли просто&nbsp;представлять</h3>
<p>Одного воображения мало. Состояние меняет решения, дальше идут поступки и&nbsp;события дня. Поэтому его сначала называют вслух, потом из&nbsp;него действуют, а&nbsp;вечером сверяют задуманное с&nbsp;прожитым.</p>
<h3>Если намерение не&nbsp;сбылось</h3>
<p>Это рабочий материал, и на&nbsp;разборе он&nbsp;ценнее удачного дня. Обычно видно одно из&nbsp;двух: либо человек сам себе не&nbsp;поверил и&nbsp;весь день внутренне торговался, либо цель оказалась чужой, взятой из&nbsp;ожиданий семьи или&nbsp;партнёров.</p>
<h3>Чем это отличается от позитивного&nbsp;мышления</h3>
<p>Уговоры вроде «всё будет отлично» держатся до&nbsp;первой плохой новости, потому что человек внутри знает правду. Здесь работа другая: ты&nbsp;входишь в&nbsp;состояние того, у&nbsp;кого уже получилось, и&nbsp;принимаешь сегодняшние решения из&nbsp;него. Проверяется это делами, а не&nbsp;настроением.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Каждый день</div><div class="big">90 дней</div><p>Столько подряд ученики Марафона держат утреннее намерение и&nbsp;вечерний разбор. Как это устроено по&nbsp;шагам, на&nbsp;странице <a href="/chizhovy2/praktiki/">практик школы</a>.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Человек и&nbsp;его&nbsp;история</p>
<h2>Он&nbsp;собирался домой без&nbsp;денег&nbsp;на&nbsp;дорогу</h2>
<p>Невилл Годдард родился на&nbsp;Барбадосе в&nbsp;1905 году, в&nbsp;семнадцать лет приехал в&nbsp;Нью-Йорк учиться танцу и&nbsp;несколько лет выходил на&nbsp;бродвейскую сцену. Потом бросил всё ради лекций. Учителем его стал человек, которого он&nbsp;называл Абдуллой, и&nbsp;главный урок случился в&nbsp;1933&nbsp;году.</p>
<p>Годдард хотел встретить Рождество на&nbsp;острове, у&nbsp;своих, а&nbsp;денег на&nbsp;дорогу не&nbsp;было совсем. Абдулла выслушал и&nbsp;ответил коротко: ты&nbsp;уже на&nbsp;Барбадосе. И&nbsp;велел каждый вечер укладываться спать так, будто ты&nbsp;уже дома. Годдард спорил про себя, злился, но&nbsp;делал ровно так. В&nbsp;начале декабря пришло письмо от&nbsp;брата: деньги и&nbsp;билет на&nbsp;пароход, третий класс. Перед самым отплытием кто-то отказался от&nbsp;каюты, и&nbsp;домой он&nbsp;поплыл&nbsp;первым.</p>
<p>Проверить эту историю сегодня невозможно, а&nbsp;рассказывал он&nbsp;её&nbsp;со&nbsp;сцены десятилетиями. Из&nbsp;неё выросло его единственное указание, и&nbsp;повторял он&nbsp;его до&nbsp;конца жизни: сначала стань тем, у&nbsp;кого уже получилось, и&nbsp;только потом смотри, что начнёт&nbsp;происходить.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Его формула</div><div class="big">Уже сбылось</div><p>Почувствуй, что желание исполнено, и&nbsp;живи из&nbsp;этого чувства. Десяток книг и&nbsp;сотни выступлений почти целиком про одно&nbsp;это.</p></div>
</aside>
</div></div></section>




<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-goddard.jpg" alt="Состояние вечером" loading="lazy"></div>
<div>
<p class="eyebrow">Годдард</p>
<h2 style="font-size:1.9rem">Состояние вечером</h2>
<p>Он&nbsp;советовал засыпать в&nbsp;состоянии человека, у&nbsp;которого желаемое уже случилось.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Как это выглядит у&nbsp;нас</p>
<h2>Что из&nbsp;Годдарда работает в&nbsp;зале</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('sunrise','var(--copper)')}<h3>Итог, а&nbsp;не&nbsp;список дел</h3><p>Утреннее намерение пишется в&nbsp;настоящем времени: «день прошёл именно так». Не&nbsp;план задач, а&nbsp;состояние, из&nbsp;которого человек в&nbsp;этот день идёт.</p></div>
<div class="card">{icon('hourglass')}<h3>Вечер важнее утра</h3><p>Годдард настаивал на&nbsp;последних минутах перед сном. У&nbsp;нас это вечерний разбор: что сбылось, где сорвался, чем день закончился внутри.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Механизм, а&nbsp;не&nbsp;вера</h3><p>Мы&nbsp;не&nbsp;просим верить. Состояние управляет вниманием и&nbsp;качеством решений, и&nbsp;это проверяется за&nbsp;девяносто дней практики.</p></div>
</div>
</div></section>

{MOST}
""")

P["istoki/nauka/index.html"] = ("Наука за методом · Истоки метода",
"ЛеДу, Гоулман, Болте Тейлор, Голвитцер, Либерман: открытия, на которых стоит работа школы.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoki-nauka.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Истоки · Наука</p><h1>Почему это работает</h1>
<p class="lead">Сцена, состояние, погружение: за&nbsp;каждым инструментом школы стоит исследование. Ниже пять открытий и&nbsp;то, как&nbsp;мы используем каждое в&nbsp;зале.</p></div></div>

<section><div class="wrap"><div class="nails nails3" style="margin-bottom:26px">
<div class="nail"><b>12&nbsp;мс</b><span>фора эмоционального мозга перед&nbsp;думающим</span></div>
<div class="nail"><b>90&nbsp;сек</b><span>живёт химия эмоции, если её не&nbsp;кормить</span></div>
<div class="nail"><b>100&nbsp;лет</b><span>групповой сцене&nbsp;Морено</span></div>
</div></div>
<div class="narrow">
<div class="card white" style="margin-bottom:12px"><span class="bignum">12&nbsp;мс</span><h3>Джозеф ЛеДу: эмоция быстрее мысли</h3><p>Сигнал об&nbsp;угрозе доходит до&nbsp;эмоционального центра мозга за 12&nbsp;миллисекунд. Думающая кора получает его позже. Поэтому обещание «в&nbsp;следующий раз отвечу спокойно» рассыпается: реакция стартует раньше решения. В&nbsp;зале мы&nbsp;работаем с&nbsp;самой записью, она быстрее любой силы&nbsp;воли.</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Дэниел Гоулман: эмоции берут верх</h3><p>В&nbsp;острый момент миндалина перехватывает управление, и&nbsp;умный взрослый человек ведёт себя как не&nbsp;свой. Гоулман назвал это захватом. На&nbsp;тренинге ты&nbsp;учишься видеть его в&nbsp;лицо и&nbsp;выходить из&nbsp;него через тело: пока миндалина рулит, уговоры&nbsp;бессильны.</p></div>
<div class="card white" style="margin-bottom:12px"><span class="bignum">90&nbsp;с</span><h3>Джилл Болте Тейлор: девяносто секунд</h3><p>Химия эмоции живёт в&nbsp;теле около полутора минут. Всё, что дольше, поддерживает уже мысль, которая крутит эмоцию по&nbsp;кругу. Пауза и&nbsp;внимание к&nbsp;телу разжимают этот круг. Тренируем это с первого&nbsp;дня.</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Питер Голвитцер: сила намерения</h3><p>Точное намерение поднимает шанс действия в&nbsp;разы по&nbsp;сравнению с&nbsp;расплывчатым «надо&nbsp;бы»: голове нужны место, время и&nbsp;первый шаг. Иначе не&nbsp;работает. Наша утренняя практика на&nbsp;Марафоне стоит на этом&nbsp;открытии.</p></div>
<div class="card white"><h3>Мэттью Либерман: назови чувство, и&nbsp;оно слабеет</h3><p>Названная вслух эмоция теряет силу: слова снижают активность миндалины. На&nbsp;этом держится половина работы группы. Чувство впервые получает имя и&nbsp;звучит при&nbsp;людях.</p></div>

<p style="margin-top:26px">И&nbsp;над всем этим сто лет психодрамы Морено: групповой формат, где все эти механизмы включаются разом, в&nbsp;одной живой сцене. Наука здесь рамка честности. Мы&nbsp;берём проверенное и не обещаем&nbsp;чудес.</p>
</div></section>
{istoki_dalee(("/chizhovy2/istoki/moreno-psihodrama/", "Морено и психодрама"), ("/chizhovy2/istoki/goddard/", "Невилл Годдард"), ("/chizhovy2/metod/", "Метод целиком"))}
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Что именно&nbsp;измерили</p>
<h2>За&nbsp;каждым словом стоит чей-то&nbsp;эксперимент</h2>
<p>Про эмоцию, которая обгоняет мысль, ЛеДу выяснил вот что: сигнал идёт двумя дорогами сразу. Короткая ведёт к&nbsp;эмоциональному центру напрямую, длинная заходит через думающую кору и&nbsp;добирается почти вдвое позже. Проследил он&nbsp;это в&nbsp;опытах на&nbsp;крысах в&nbsp;Нью-Йоркском университете. Пока разум разбирается, тело уже отпрыгнуло, повысило голос или замолчало. Спорить с&nbsp;такой форой бесполезно. Тормозить приходится задним числом, когда фраза уже&nbsp;сказана.</p>
<p>Про названные чувства Либерман поставил прямой опыт в&nbsp;2007 году в&nbsp;Калифорнийском университете в&nbsp;Лос-Анджелесе. Люди лежали в&nbsp;томографе и&nbsp;разглядывали злые и&nbsp;испуганные лица. Пока картинка шла молча, миндалина разгоралась. Стоило подобрать к&nbsp;лицу слово, и&nbsp;она стихала, а&nbsp;вместо неё включалась лобная кора. Название гасит&nbsp;вспышку.</p>
<p>Про намерение накоплено больше всего доказательств. Голвитцер с&nbsp;соавтором свёл воедино 94 исследования: везде сравнивали расплывчатое «надо бы&nbsp;заняться» с&nbsp;точным «в&nbsp;среду в&nbsp;семь утра, кроссовки у&nbsp;двери». Второе доводит до&nbsp;дела заметно чаще, и&nbsp;результат повторяется из&nbsp;опыта&nbsp;в&nbsp;опыт.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Свод исследований</div><div class="big">94</div><p>Столько работ вошло в&nbsp;подсчёт Голвитцера, участников больше восьми тысяч. Средний размер эффекта 0,65, для&nbsp;психологии это&nbsp;много.</p></div>
<div class="box"><div class="lbl">Декабрь 1996</div><div class="big">8 лет</div><p>Нейроанатом Болте Тейлор возвращала себе речь и&nbsp;счёт после кровоизлияния в&nbsp;левом полушарии. Ей&nbsp;было 37, и&nbsp;из&nbsp;её&nbsp;книги пришло правило 90&nbsp;секунд.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Где это видно&nbsp;в&nbsp;зале</p>
<h2>Три места, где это включено&nbsp;в&nbsp;работу</h2>
<p>Первое: пауза. После сильного процесса ведущий не&nbsp;торопит человека и&nbsp;не&nbsp;бросается утешать. Волна поднимается и&nbsp;проходит сама, на&nbsp;это уходит около полутора минут, и&nbsp;лучшее, что можно сделать за&nbsp;это время, побыть рядом&nbsp;молча.</p>
<p>Второе: сказать вслух. Всё, что осталось внутри, гоняется по&nbsp;кругу, а&nbsp;произнесённое при&nbsp;людях теряет заряд. Один участник записал вечером: «Очень круто зашло проговорить свой стыд. Энергия&nbsp;появилась».</p>
<p>Третье: формулировка. Утреннее намерение пишется так, чтобы в&nbsp;нём были состояние, место и&nbsp;первый шаг. Расплывчатое «буду спокойнее» умирает к&nbsp;обеду, точное живёт до&nbsp;вечера и&nbsp;попадает в&nbsp;вечерний&nbsp;разбор.</p>
<h3>Что измерено и&nbsp;что остаётся личным&nbsp;опытом</h3>
<p>Наука посчитала скорость реакции, эффект названного чувства и&nbsp;силу ясной формулировки. Это твёрдая почва. А&nbsp;вот как повернётся жизнь конкретного человека после модуля, не&nbsp;предскажет никто: истории учеников на&nbsp;сайте это личный опыт, и&nbsp;он&nbsp;у&nbsp;каждого&nbsp;свой.</p>
<h3>Чем эта страница отличается от&nbsp;других&nbsp;истоков</h3>
<p>Остальные разделы отвечают, откуда взяты инструменты: сцена, язык практики, формат погружения. Здесь ответ на&nbsp;другой вопрос, почему всё это вообще срабатывает на&nbsp;живом человеке. И&nbsp;заодно рамка честности: если механизма нет, приём в&nbsp;методе не&nbsp;задерживается.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Откуда это словечко</div><div class="big">1995</div><p>В&nbsp;этом году вышла книга Гоулмана про эмоциональный интеллект. Оттуда в&nbsp;обиход ушёл захват миндалины: момент, когда взрослый человек на&nbsp;секунду перестаёт себя&nbsp;узнавать.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-nauka.jpg" alt="Что говорят исследования" loading="lazy"></div>
<div>
<p class="eyebrow">Проверка</p>
<h2 style="font-size:1.9rem">Что говорят исследования</h2>
<p>За&nbsp;каждым инструментом школы стоит работа учёных: ЛеДу, Болте Тейлор, Голвитцер, Либерман.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Кто это проверял</p>
<h2>Четыре исследования под&nbsp;методом</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('flame','var(--copper)')}<h3>Джозеф ЛеДу</h3><p>Нейробиолог показал: сигнал доходит до&nbsp;аварийного центра мозга примерно на&nbsp;12&nbsp;миллисекунд раньше, чем до&nbsp;думающей коры. Реакция стартует до&nbsp;осмысления.</p></div>
<div class="card">{icon('hourglass')}<h3>Джилл Болте Тейлор</h3><p>Нейроанатом описала: химия вспыхнувшей эмоции живёт в&nbsp;теле около 90&nbsp;секунд. Дальше её&nbsp;держит только то, что человек сам себе рассказывает.</p></div>
<div class="card">{icon('target','var(--sage-deep)')}<h3>Питер Голвитцер</h3><p>Свод из&nbsp;94&nbsp;исследований, около 8000&nbsp;участников: конкретно сформулированное намерение резко поднимает шанс действия.</p></div>
<div class="card">{icon('speech','var(--sand)')}<h3>Мэттью Либерман</h3><p>Назвать чувство словом означает снизить его накал. Поэтому в&nbsp;зале просят говорить прямо, а&nbsp;не&nbsp;описывать общими фразами.</p></div>
</div>
</div></section>

{MOST}
""")

# ================= ИСТОРИИ УЧЕНИКОВ =================
P["istorii/index.html"] = ("Истории учеников · Настоящие отношения",
"Полные истории выпускников школы: точка А, работа, что изменилось. С согласия авторов, без глянца.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istorii-hero.jpg')"></div><div class="veil"></div>
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

<section><div class="wrap">
<p class="eyebrow">Короткой строкой</p>
<h2>Что рассказывают ученики</h2>
<div class="grid3" style="margin-top:26px">
<div class="card"><p class="serif" style="font-style:italic">«Намерение это когда я&nbsp;знаю, что в&nbsp;моей жизни возможно только так. Тогда и&nbsp;важности нет, я просто&nbsp;знаю».</p><p class="note" style="margin-top:10px">Участница Марафона</p></div>
<div class="card"><p class="serif" style="font-style:italic">«Когда убираю фокус с&nbsp;себя и&nbsp;вовлечён в&nbsp;команду, энергия кратно растёт, и&nbsp;люди поворачиваются ко мне&nbsp;лицом».</p><p class="note" style="margin-top:10px">Участник Марафона</p></div>
<div class="card"><p class="serif" style="font-style:italic">«Когда цель и&nbsp;мечта действительно мои, всё происходит легко, порой на&nbsp;грани фантастики».</p><p class="note" style="margin-top:10px">Участница Марафона</p></div>
</div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/otzyvy/">Ещё отзывы о&nbsp;школе</a></p>
</div></section>

<section><div class="narrow">
<h2>Что общего у&nbsp;этих историй</h2>
<p>Люди приходят из&nbsp;разных точек: один после потери бизнеса, другая из&nbsp;тихого благополучия, где всё есть и&nbsp;ничего не&nbsp;радует. Сюжеты разные, а&nbsp;узор один и тот&nbsp;же.</p>
<div class="grid2" style="margin-top:22px">
<div class="card">{icon('target')}<h3>Сначала точка&nbsp;А</h3><p>Всё начинается с&nbsp;честного признания, где человек находится на&nbsp;самом деле, без смягчений и&nbsp;объяснений, почему так вышло. Шаг самый трудный, и&nbsp;почти все называют его&nbsp;переломным.</p></div>
<div class="card">{icon('shield','var(--sage-deep)')}<h3>Потом сопротивление</h3><p>«Долго упирался», «не&nbsp;верил», «сидел и&nbsp;злился». Психика защищает привычный порядок, даже когда он&nbsp;давно разрушает жизнь: старое хотя&nbsp;бы знакомо, а&nbsp;новое пугает сильнее любой боли. Упирался почти&nbsp;каждый.</p></div>
<div class="card">{icon('lens','var(--sand)')}<h3>Дальше узнавание</h3><p>Момент, когда человек видит свою запись целиком. В&nbsp;группе это называют «нолик провалился», и&nbsp;это радость, а не&nbsp;поражение.</p></div>
<div class="card">{icon('sunrise')}<h3>И только потом результаты</h3><p>Деньги, отношения, здоровье подтягиваются позже, как следствие другого состояния и&nbsp;других поступков. Ни&nbsp;одна история не&nbsp;начинается с&nbsp;них.</p></div>
</div>
<p class="note" style="margin-top:20px">Слова, которые здесь звучат, разобраны в&nbsp;<a href="/chizhovy2/slovar/">словаре школы</a>.</p>
</div></section>

<section><div class="narrow">
<h2>Начать свою историю</h2>
<p class="sub" style="margin:0 0 26px">Первый шаг у&nbsp;всех один: честный разговор. Для читателей сайта он&nbsp;&#8288;бесплатный.</p>
<a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Узор в&nbsp;словах</p>
<h2>Как эти четыре шага звучат&nbsp;вживую</h2>
<p>Узор хорошо виден по&nbsp;фразам, которые повторяются из&nbsp;анкеты в&nbsp;анкету у&nbsp;людей, незнакомых между собой. Ниже по&nbsp;одной цитате на&nbsp;каждый шаг, все из разных&nbsp;историй.</p>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Точка&nbsp;А</h3><p class="serif" style="font-style:italic">«Принять, что мир это зеркало, и&nbsp;всё, что со&nbsp;мной происходит, я транслирую&nbsp;сам».</p><p class="note" style="margin-top:10px">Предприниматель. Это далось ему труднее всего за весь&nbsp;тренинг</p></div>
<div class="card"><h3>Сопротивление</h3><p class="serif" style="font-style:italic">«Меня доставали, показывали, что не&nbsp;так и&nbsp;где не&nbsp;так, а я&nbsp;опять проваливался в&nbsp;своё».</p><p class="note" style="margin-top:10px">Он&nbsp;же, про первые недели&nbsp;работы</p></div>
<div class="card"><h3>Узнавание</h3><p class="serif" style="font-style:italic">«Я&nbsp;так не&nbsp;плакал с&nbsp;детства. Чистка&nbsp;колоссальная».</p><p class="note" style="margin-top:10px">Участник после первого&nbsp;модуля</p></div>
<div class="card"><h3>Результаты</h3><p class="serif" style="font-style:italic">«Ощущение, что снял рюкзак, который тянул вниз. Как будто вешу килограммов на десять&nbsp;меньше».</p><p class="note" style="margin-top:10px">Участник после второго&nbsp;модуля</p></div>
</div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Один и тот же&nbsp;ход</div><div class="big">4 шага</div><p>Точка&nbsp;А, сопротивление, узнавание, результаты. Порядок не&nbsp;меняется ни у&nbsp;кого: сначала правда о&nbsp;себе, потом всё&nbsp;остальное.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Разница</p>
<h2>Чем истории отличаются друг от&nbsp;друга</h2>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Точкой&nbsp;входа</h3><p>Одни приходят с&nbsp;обрыва: долги, расставание, друзья перестали звонить. Другие из&nbsp;тихого благополучия, где всё сложилось и&nbsp;ничего не&nbsp;радует. Второй вход тяжелее признать: жаловаться вроде бы не на&nbsp;что.</p></div>
<div class="card"><h3>Скоростью</h3><p>У&nbsp;одних щёлкает в&nbsp;первые дни зала. Предпринимателю из&nbsp;нашей истории понадобилось несколько месяцев, чтобы увидеть, в&nbsp;чём он&nbsp;жил. Ни&nbsp;тот, ни&nbsp;другой темп не&nbsp;говорит о человеке&nbsp;ничего.</p></div>
<div class="card"><h3>Что оживает первым</h3><p>У&nbsp;одних первыми оттаивают отношения. У&nbsp;других выравнивается дело или меняется круг общения. Обычно человек ждёт перемен в&nbsp;одном месте, а&nbsp;замечает их совсем в&nbsp;другом.</p></div>
<div class="card"><h3>Тем, с кем&nbsp;пришёл</h3><p>Один идёт в&nbsp;зал сам, а&nbsp;дома всё равно становится иначе. Другая приходит с&nbsp;мужем, и&nbsp;тогда сценарий разбирают с&nbsp;двух сторон. Многие потом приводят близких: <a href="/chizhovy2/soobshchestvo/">сарафан</a> у&nbsp;школы главный канал с первого&nbsp;года.</p></div>
</div>
</div>
<aside class="side">
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как это&nbsp;собрано</p>
<h2>Откуда берутся эти&nbsp;истории</h2>
<p>Мы&nbsp;просим выпускников рассказать свой путь по&nbsp;пяти шагам: как было до&nbsp;тренинга, как решился прийти, что происходило в&nbsp;зале, что стало после и&nbsp;что сказал бы&nbsp;сомневающемуся. Просим наговорить голосом: так человек говорит живее, чем пишет, и в&nbsp;рассказ попадают детали, которые в&nbsp;тексте обычно&nbsp;приглаживают.</p>
<p>Дальше расшифровку мы&nbsp;собираем в&nbsp;историю и&nbsp;показываем автору целиком, до&nbsp;публикации. Слова оставляем его: «как баран», «в&nbsp;коробочку», «нолик провалился». Неудобные места не&nbsp;вырезаем, иначе история перестаёт быть чьей-то и&nbsp;становится рекламной. Имена чаще всего убираем по&nbsp;просьбе самих&nbsp;авторов.</p>
<p>Суммы дохода, сроки и&nbsp;скорость перемен на&nbsp;витрину не&nbsp;выносим. У&nbsp;каждого они свои, и&nbsp;чужая цифра сказала бы о&nbsp;твоём пути ровно&nbsp;ничего.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Анкета&nbsp;выпускника</div><div class="big">5 шагов</div><p>До, решение прийти, зал, после, слово сомневающемуся. Один и тот&nbsp;же порядок вопросов для&nbsp;всех.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-istorii.jpg" alt="Люди, а не кейсы" loading="lazy"></div>
<div>
<p class="eyebrow">Живые истории</p>
<h2 style="font-size:1.9rem">Люди, а&nbsp;не&nbsp;кейсы</h2>
<p>Здесь нет отредактированных success story. Есть точка А, сопротивление и&nbsp;то, что изменилось.</p>
</div>
</div>
</div></section>

""")

P["istorii/predprinimatel/index.html"] = ("Предприниматель: заново после дна · Истории учеников",
"Полная история ученика школы: кризис, сопротивление, точка А и как жизнь собралась обратно.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoriya-biznes.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">История ученика</p><h1>Заново после дна</h1>
<p class="lead">Предприниматель, пришёл весной 2024. Дальше его слова, почти без правок и&nbsp;с его согласия. Имя он&nbsp;просил не раскрывать, а&nbsp;неудобные места мы&nbsp;не убирали. Результат у&nbsp;каждого свой.</p></div></div>

<section><div class="narrow">
<!-- ПРОТОТИП: текст согласован с автором до публикации -->
<h2>Точка&nbsp;А</h2>
<p>«Я&nbsp;находился в&nbsp;фазе, которую называют дном. Кассовый разрыв на&nbsp;десятки миллионов, долги, заработки в&nbsp;один день стали ноль, накопления потрачены. Расстался с&nbsp;девушкой, которой сделал предложение: свадьбу пришлось отложить из-за денег, а&nbsp;она не захотела&nbsp;ждать.</p>
<p>Самое тяжёлое: сильно било по&nbsp;эго. Друзья отвернулись, из&nbsp;делового клуба выгнали, тянулся хвост репутации. Не&nbsp;хотелось ни с&nbsp;кем общаться, хотелось закрыться в&nbsp;коробочку и&nbsp;сидеть одному. Крах я&nbsp;понимал, а&nbsp;вот как начать снова и&nbsp;где найти силы, понять не&nbsp;мог. Убегал как умел: закрывался, алкоголь, спорт, суета, пытался казаться хорошим».</p>

<h2 style="margin-top:34px">Как он&nbsp;пришёл</h2>
<p>«Подруга давно рассказывала о&nbsp;тренинге, но&nbsp;тогда мне было не&nbsp;надо. А&nbsp;тут друг увидел моё состояние и&nbsp;сказал: я&nbsp;знаю решение. Когда я&nbsp;понял, что он&nbsp;говорит про то&nbsp;же самое место, я&nbsp;решил: это вторая возможность. Пошёл не&nbsp;раздумывая, прямо в&nbsp;свой день рождения. Подарил себе тренинг. Единственное, что останавливало: простое недоверие, что поможет».</p>

<h2 style="margin-top:34px">Что происходило</h2>
<p>«Долго сопротивлялся, как баран. Проваливался в&nbsp;своё. Труднее всего было принять точку&nbsp;А: признать, где я на&nbsp;самом деле. Потребовалось время, чтобы увидеть, в&nbsp;чём я&nbsp;жил.</p>
<p>Главное, что я&nbsp;увидел: мир это зеркало. Всё, что со&nbsp;мной происходит, это то, что я&nbsp;сам транслирую. Я&nbsp;покупал отношения вместо того, чтобы их&nbsp;строить, использовал людей ради выгоды. Когда защита наконец упала, в&nbsp;группе это называют «нолик провалился», я&nbsp;впервые обрадовался правде о&nbsp;себе».</p>
<div class="pull"><div class="q">«Ура, нолик <span style="white-space:nowrap">наконец-то провалился.»</span></div><div class="who">Из его сообщения группе в&nbsp;тот вечер</div></div>

<h2 style="margin-top:34px">Что изменилось</h2>
<p>«Сейчас я&nbsp;строю настоящие отношения везде: в&nbsp;деле, с&nbsp;близкими, с&nbsp;собой. Деньги начали приходить, энергии много, и я&nbsp;умею ей&nbsp;распоряжаться: держу состояние через спорт и&nbsp;благодарности, не&nbsp;сливаю её по&nbsp;мелочам. Раньше отсеивал людей по&nbsp;уровню жизни, сейчас просто строю отношения, и&nbsp;люди вокруг собрались такие, что доходы выросли сами. Цели кратно увеличились, научился играть в&nbsp;долгую. И&nbsp;мне стало всё равно на&nbsp;чужое мнение обо мне.</p>
<p>Одной фразой: получил новую версию&nbsp;себя».</p>
<div class="pull"><div class="q">«Появилось ощущение, что вижу себя на&nbsp;всей шахматной доске, а не в&nbsp;одной клетке.»</div><div class="who">Его формула итога</div></div>
<p class="note">История личная, поэтому без имени. Суммы и&nbsp;скорость перемен у&nbsp;каждого свои: школа не&nbsp;обещает повторения чужого результата и не&nbsp;берётся предсказывать&nbsp;сроки.</p>
</div></section>

<section><div class="narrow">
<h2>Узнал себя в этом?</h2>
<p class="sub" style="margin:0 0 26px">Его путь начался с&nbsp;одного честного разговора о&nbsp;том, где он на&nbsp;самом деле находится. Твой может начаться так&nbsp;же. Собеседование для читателей сайта&nbsp;бесплатное.</p>
<p class="btns"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/istorii/komanda-mir/" style="margin-left:8px">Ещё история: команда «МИР»</a></p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Неожиданное</p>
<h2>Что он нашёл вместо своей&nbsp;поломки</h2>
<p>Люди приходят в&nbsp;зал искать в&nbsp;себе неисправность. Обычно у&nbsp;человека уже есть версия, что с&nbsp;ним не&nbsp;так, и он&nbsp;ждёт, что её&nbsp;подтвердят. На&nbsp;вопрос о&nbsp;главном открытии тренинга он ответил&nbsp;коротко:</p>
<p>«Самое сильное и&nbsp;неожиданное: что я&nbsp;крутой. Быть в&nbsp;состоянии безусловной любви и&nbsp;отдавания. Быть в&nbsp;честности».</p>
<p>Дальше в том&nbsp;же ответе идёт неудобная часть про желание покупать отношения и&nbsp;использовать людей ради выгоды. Обе половины пришли к&nbsp;нему в&nbsp;один день, и в&nbsp;этом весь смысл работы: правда о&nbsp;себе приходит целиком, вместе с&nbsp;хорошим.</p>
</div>
<aside class="side">
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Сроки</p>
<h2>Сколько это заняло на самом&nbsp;деле</h2>
<p>Он&nbsp;пришёл весной 2024&nbsp;года и&nbsp;первые недели держал оборону. «Меня доставали, показывали, что не&nbsp;так и&nbsp;где не&nbsp;так, я&nbsp;опять проваливался в&nbsp;своё». Про сроки в&nbsp;анкете сказано прямо: «Потребовалось несколько месяцев, чтобы я&nbsp;увидел то, в&nbsp;чём я&nbsp;жил, и&nbsp;как я могу&nbsp;выкарабкаться».</p>
<p>Так и&nbsp;устроена программа: два с&nbsp;половиной дня первого модуля, пауза в&nbsp;три-пять недель, пять дней второго, дальше три месяца практики в&nbsp;обычной жизни. Перелом у&nbsp;него случился далеко не в&nbsp;первый вечер, и&nbsp;это самая частая история&nbsp;зала.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Сколько он шёл к&nbsp;этому</div><div class="big">Месяцы</div><p>Столько ушло у&nbsp;него на точку&nbsp;А. У&nbsp;других щёлкает в&nbsp;первые дни: темп ничего не&nbsp;говорит о&nbsp;человеке.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Что стало&nbsp;возможным</p>
<h2>Чем его жизнь отличается&nbsp;сегодня</h2>
<p>Кроме денег и&nbsp;целей, о&nbsp;которых он&nbsp;сказал выше, в&nbsp;анкете есть вещи потише. Он&nbsp;стал меньше тусоваться и&nbsp;старается быть максимально отдающим человеком. Появились новые направления в&nbsp;деле, которые он&nbsp;развивает без&nbsp;рывков. Суеты стало меньше.</p>
<p>Отдельно он&nbsp;описал навык, ради которого во&nbsp;многом и&nbsp;идут на&nbsp;третий модуль: «Я&nbsp;могу заходить в&nbsp;любые <a href="/chizhovy2/slovar/">маятники</a> и, имея свою цель, брать там только то, что мне нужно и&nbsp;что меня усилит, и&nbsp;выходить». Проще говоря, шумные истории вокруг перестали забирать его энергию&nbsp;даром.</p>
</div>
<aside class="side">
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Совет&nbsp;сомневающимся</p>
<h2>Что он говорит тем, кто ещё&nbsp;решает</h2>
<p>Последний вопрос анкеты звучит так: что скажешь человеку, который сейчас на&nbsp;твоём прежнем месте. Ответ мы оставили&nbsp;дословно.</p>
<div class="pull"><div class="q">«Точно идти. Ты&nbsp;точно получишь порцию той информации, которая необходима тебе именно в&nbsp;этот момент времени, какая она будет и&nbsp;что именно ждать никто не&nbsp;знает и не&nbsp;скажет, это просто&nbsp;произойдёт.»</div><div class="who">Из анкеты&nbsp;выпускника</div></div>
<p>Мы бы&nbsp;добавили одно. На&nbsp;тренинг он&nbsp;пошёл в&nbsp;свой день рождения и&nbsp;подарил его себе сам. Сомнения при этом остались при нём, они лишь перестали быть&nbsp;главными.</p>
</div>
<aside class="side">
</aside>
</div></div></section>

<section><div class="wrap">
<p class="eyebrow">Разбор по&nbsp;шагам</p>
<h2>Что именно с&nbsp;ним произошло</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('target','var(--copper)')}<h3>Точка А</h3><p>Кассовый разрыв, долги, расставание. Понимание краха есть, сил начать заново нет. Реакция знакомая: закрыться и&nbsp;тащить самому.</p></div>
<div class="card">{icon('shield')}<h3>Сопротивление</h3><p>«Долго упирался, как баран». Первые месяцы уходили на&nbsp;то, чтобы доказать залу и&nbsp;себе, что у&nbsp;него особый случай.</p></div>
<div class="card">{icon('lens','var(--sage-deep)')}<h3>Узнавание</h3><p>Самое трудное: принять точку А. Признать, что мир отражает то, что человек транслирует сам.</p></div>
<div class="card">{icon('sunrise','var(--sand)')}<h3>Результаты</h3><p>Новые направления, выросшие цели, отношения вместо сделок. Не&nbsp;за&nbsp;месяц: он&nbsp;сам говорит про несколько месяцев работы.</p></div>
</div>
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
<div class="nail"><b>15</b><span>человек в команде&nbsp;«МИР»</span></div>
<div class="nail"><b>90</b><span>дней ежедневной&nbsp;практики</span></div>
<div class="nail"><b>Раз в&nbsp;неделю</b><span>встреча-разбор с&nbsp;ведущими, все три&nbsp;месяца</span></div>
</div></div>
<div class="narrow">
<h2>Как устроен их&nbsp;день</h2>
<p>Утром каждый пишет в&nbsp;чат намерение на&nbsp;день: из&nbsp;какого состояния идёт и&nbsp;что создаёт. Вечером открытия и&nbsp;благодарности: что произошло, где старая запись взяла своё, за&nbsp;что спасибо дню и&nbsp;людям. Раз в&nbsp;неделю вся команда встречается с&nbsp;ведущими на&nbsp;разбор.</p>
<p>Простая механика, но&nbsp;девяносто дней подряд она перепрошивает привычный способ жить. Вот как это звучало у&nbsp;них, без правок:</p>
<div class="card white" style="margin:20px 0 12px"><p class="serif" style="font-style:italic;margin:0">«Пишу утром намерение, вечером сравниваю. Так приятно ощущать, что к&nbsp;концу дня большая часть намерений&nbsp;сбылась».</p></div>
<div class="card white" style="margin-bottom:12px"><p class="serif" style="font-style:italic;margin:0">«Отследил сегодня несколько маятников, не&nbsp;среагировал, и&nbsp;благодаря этому удержал состояние весь день».</p></div>
<div class="card white"><p class="serif" style="font-style:italic;margin:0">«Вместо эмоций решила стать вкладом в&nbsp;отношения: говорить с&nbsp;уважением и&nbsp;любовью. И&nbsp;вот первые ростки. Сердце открывается, и я в&nbsp;этот момент&nbsp;настоящая».</p></div>

<h2 style="margin-top:34px">Что происходило с&nbsp;людьми</h2>
<p>У&nbsp;каждого своя история внутри общей. Одна участница полгода не&nbsp;могла решиться на&nbsp;поездку, даже паспорт не&nbsp;находился: после работы в&nbsp;группе приняла решение внутри, и&nbsp;всё сложилось за&nbsp;день, паспорт нашёлся, тур куплен. Другой заметил: стоит убрать фокус с&nbsp;себя и&nbsp;вложиться в&nbsp;команду, энергия кратно растёт, и&nbsp;люди поворачиваются&nbsp;лицом.</p>
<div class="pull"><div class="q">«Намерение это когда я&nbsp;знаю, что в&nbsp;моей жизни возможно только так. В&nbsp;чём я&nbsp;так была уверена по&nbsp;жизни, всё&nbsp;сбылось.»</div><div class="who">Участница команды «МИР»</div></div>
<p>К&nbsp;финалу модуля в&nbsp;чате появились слова, ради которых школа и&nbsp;работает: «жизнь становится легче и&nbsp;лучше, пусть пока в&nbsp;мелочах, но я&nbsp;это вижу». Перемены приходят малым и&nbsp;остаются, потому что их&nbsp;держат девяносто дней&nbsp;практики.</p>
<p class="note">Цитаты из&nbsp;закрытого командного чата, публикуются с&nbsp;согласия участников. Имена убраны. Результат у&nbsp;каждого свой.</p>
</div></section>

<section><div class="wrap">
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-10.jpg" alt="Команда Марафона" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-11.jpg" alt="Участники команды" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
</div>
<p class="btns" style="margin-top:30px"><a class="btn btn-wine" href="/chizhovy2/marafon/">Как устроен Марафон</a> <a class="btn btn-ghost" href="/chizhovy2/sessiya/" style="margin-left:8px">Записаться на&nbsp;собеседование</a></p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Утро и&nbsp;вечер</p>
<h2>Что именно они писали каждый&nbsp;день</h2>
<p>Теперь подробнее, из&nbsp;чего складывались эти девяносто дней. Утренняя запись выглядит непривычно: человек пишет о&nbsp;дне в&nbsp;настоящем времени, будто тот уже прошёл именно так. Сначала состояние («я&nbsp;спокойный, открытый, отдающий»), следом сам день, описанный так&nbsp;же ровно. Форма важна: желание просит и&nbsp;уговаривает, знание просто&nbsp;описывает.</p>
<p>Пишут в&nbsp;общий чат, при всех. Это меняет тон сильнее любых правил: перед командой неловко сочинять красивый абзац ни о&nbsp;чём. И&nbsp;есть простая договорённость, которая держит всю практику: писать вовремя. Тот, кто опоздал, извиняется перед своими, а&nbsp;ведущие каждое утро говорят спасибо тем, кто&nbsp;успел.</p>
<p>Вечером в тот&nbsp;же чат уходит второй текст: открытия дня и&nbsp;благодарности. Первые чаще неудобные: где сегодня сорвался, где опять поймал себя на&nbsp;правоте, где промолчал. Вторые наоборот расходятся широко: ведущим, команде, партнёру, детям, случайным людям дня.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Ритм&nbsp;дня</div><div class="big">2 записи</div><p>Утренняя занимает пару минут, вечерняя чуть больше. Девяносто дней подряд, без выходных и без&nbsp;пропусков по&nbsp;настроению.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Три&nbsp;месяца</p>
<h2>Как менялся тон записей от&nbsp;сентября к&nbsp;декабрю</h2>
<p>В&nbsp;первые недели утренние записи похожи на&nbsp;список желаний: длинный, со&nbsp;словом «хочу» в&nbsp;каждой строке, половина про то, как должны повести себя другие люди. Ближе к&nbsp;середине список укорачивается, зато появляется главное слово вечера: «отследила». Человек начинает замечать связь между тем, из&nbsp;какого состояния он&nbsp;вышел утром, и&nbsp;тем, что случилось за&nbsp;день.</p>
<p>К&nbsp;декабрю уговоры из&nbsp;записей уходят совсем. Вместо них спокойное знание и&nbsp;фокус, развёрнутый с&nbsp;себя на&nbsp;других: кому я&nbsp;сегодня буду вкладом. Для новичков это самое неожиданное место всей практики, потому что делиться силами в&nbsp;трудный период кажется последним&nbsp;делом.</p>
</div>
<aside class="side">
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Раз в&nbsp;неделю</p>
<h2>Что происходило на&nbsp;разборе</h2>
<p>Еженедельная встреча в&nbsp;Zoom так и&nbsp;называлась: «Создатель реальности». Каждый приносил на&nbsp;неё свою неделю: что сделал, что отложил, где старая запись взяла своё. Смотрели на&nbsp;сделанное: поговорил или опять промолчал, начал или снова отложил. Ощущения от&nbsp;недели умеют уговаривать, поступки&nbsp;нет.</p>
<p>Разбирали пять сфер: отношения с&nbsp;близкими, деньги и&nbsp;дело, здоровье, самооценку и&nbsp;то, что происходит внутри команды. Ведущих двое, и в&nbsp;разборе это видно: один держит структуру и&nbsp;время, вторая идёт за&nbsp;живым и&nbsp;слышит состояние человека раньше его&nbsp;слов.</p>
<p>Самое ценное на&nbsp;таких встречах случается с&nbsp;теми, кто молчит. Пока разбирают чужую ситуацию, человек вдруг узнаёт свою: истории разные, а&nbsp;круг у&nbsp;всех устроен одинаково. К&nbsp;концу встречи у&nbsp;каждого появлялся следующий шаг на&nbsp;неделю, и&nbsp;через семь дней его спрашивали при&nbsp;всех.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">На&nbsp;разбор</div><div class="big">5 сфер</div><p>Близкие, дело и&nbsp;деньги, здоровье, самооценка, команда. Каждую неделю у&nbsp;каждого, все три&nbsp;месяца.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<p class="eyebrow">Из чего складывался их&nbsp;день</p>
<h2>Четыре опоры девяноста дней</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('sunrise','var(--copper)')}<h3>Утро: намерение</h3><p>Каждый писал в&nbsp;общий чат, из&nbsp;какого состояния идёт в&nbsp;день и&nbsp;что создаёт. Пять минут до&nbsp;почты и&nbsp;новостей.</p></div>
<div class="card">{icon('calendar')}<h3>Вечер: разбор</h3><p>Что сбылось, где сорвался, за&nbsp;что благодарен. Открыто, при&nbsp;команде, без причёсывания.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Вклад в&nbsp;другого</h3><p>Писали намерения друг за&nbsp;друга, поддерживали выпавших, приезжали на&nbsp;забеги. Работа с&nbsp;фокусом на&nbsp;другом давала больше, чем работа на&nbsp;себя.</p></div>
<div class="card">{icon('lens','var(--sand)')}<h3>Разбор раз в&nbsp;неделю</h3><p>Встреча с&nbsp;Алексеем и&nbsp;Ириной: смотрели именно те&nbsp;места, где человек откатывался в&nbsp;старое.</p></div>
</div>
</div></section>

""")

# ================= СЛОВАРЬ ШКОЛЫ =================
P["slovar/index.html"] = ("Словарь школы · Настоящие отношения",
"Точка А, событийный круг, маятники, важность, намерение, нолик провалился: язык школы с переводом на обычный.", "istoki", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/slovar-hero.jpg')"></div><div class="veil"></div>
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
<div class="card white">{icon('pendulum','var(--sage-deep)')}<h3>Маятники</h3><p>Всё, что кормится твоей реакцией: скандал, лента новостей, чужая паника. Дёрнулся, отдал энергию. Навык школы: заметить крючок и не&nbsp;схватиться.</p></div>
<div class="card white">{icon('people')}<h3>Быть вкладом</h3><p>Развернуть фокус с&nbsp;«что мне дадут» на&nbsp;«что я&nbsp;даю». В&nbsp;паре, в&nbsp;команде, в&nbsp;деле. Участники отмечают: энергия от&nbsp;этого не&nbsp;уходит, а&nbsp;прибывает.</p></div>
<div class="card white">{icon('calendar')}<h3>Играть в&nbsp;долгую</h3><p>Горизонт вместо суеты: строить отношения и&nbsp;дело на&nbsp;годы, не&nbsp;выжимая быструю выгоду из&nbsp;каждой встречи. Опора выпускников в&nbsp;решениях.</p></div>
<div class="card white">{icon('sunrise','var(--sand)')}<h3>Открытия и&nbsp;благодарности</h3><p>Вечерняя практика: что понял за&nbsp;день и за&nbsp;что спасибо дню и&nbsp;людям. Держит новый способ жить крепче любой&nbsp;мотивации.</p></div>
</div>
<p class="note" style="margin-top:22px">Часть слов пришла из&nbsp;истоков метода: подробнее в&nbsp;разделах <a href="/chizhovy2/istoki/zeland-transerfing/">про трансерфинг</a> и&nbsp;<a href="/chizhovy2/istoki/nauka/">про науку</a>.</p>
</div></section>

<section><div class="narrow">
<h2>Слова оживают в&nbsp;зале</h2>
<p class="sub" style="margin:0 0 26px">Читать словарь полезно, а&nbsp;по-настоящему эти слова понимаешь телом, в&nbsp;зале, когда очередь доходит до&nbsp;твоей сцены. Начни с&nbsp;гайда или запишись на&nbsp;собеседование.</p>
<p class="btns"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Читать гайд</a></p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Слова о&nbsp;работе в&nbsp;зале</p>
<h2>Ещё восемь слов из&nbsp;зала</h2>
<div class="card white" style="margin-bottom:12px"><span class="icwrap" style="color:var(--wine)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 40V22a8 8 0 0 1 8-8h16"/><path d="M30 8l6 6-6 6"/><circle cx="12" cy="43" r="2.4"/></svg></span><h3>Образ</h3><p>Роль, снятая с&nbsp;близкого человека и&nbsp;живущая внутри как своя: мать, отец, бабушка, старший брат. На&nbsp;модуле их&nbsp;находят, а&nbsp;дальше выбирают сознательно. Участница: «подумала, как бы&nbsp;поступила учительница начальных классов, вот это прямо очень&nbsp;помогает».</p></div>
<div class="card white" style="margin-bottom:12px"><span class="icwrap" style="color:var(--sage-deep)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M24 6l14 5v11c0 9-6 16-14 20-8-4-14-11-14-20V11z"/><path d="M24 14l-3 7h6l-4 9"/></svg></span><h3>Клятва</h3><p>Обещание, которое человек дал себе в&nbsp;трудную минуту. Держится годами. Звучит как приговор: «больно будет всегда, это никогда не&nbsp;закончится». В&nbsp;зале её&nbsp;находят, отпускают и&nbsp;ставят на&nbsp;это место новое решение. Короткая формула из&nbsp;чата: «Клятвы&nbsp;не&nbsp;дают&nbsp;расти».</p></div>
<div class="card white" style="margin-bottom:12px"><span class="icwrap" style="color:var(--sand)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 38l12-20 7 11 5-7 12 16z"/><path d="M18 18l3 5"/></svg></span><h3>Правота</h3><p>Состояние, в&nbsp;котором важнее оказаться правым, чем&nbsp;договориться. Съедает вечера, переговоры и&nbsp;отношения. Выход один: вопрос «какая цель?». Живая запись из&nbsp;чата: «Сегодня день провёл в&nbsp;правоте. Что привело к&nbsp;плохому завершению&nbsp;дня».</p></div>
<div class="card white"><span class="icwrap" style="color:var(--wine)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 18a12 12 0 0 1 21 6"/><path d="M34 30a12 12 0 0 1-21-6"/><path d="M35 15v9h-9"/><path d="M13 33v-9h9"/></svg></span><h3>Откат</h3><p>Возврат в&nbsp;прежнее состояние после подъёма. Накрывает через две-три недели почти каждого и&nbsp;считается нормальной частью маршрута. В&nbsp;списке благодарностей это выглядит так: «себе за&nbsp;то, что расту, хоть&nbsp;и&nbsp;с&nbsp;откатами».</p></div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Откуда эти слова</div><p>Одни звучат в&nbsp;зале, другие пришли из&nbsp;ежедневной практики. В&nbsp;словарь взяты те, что повторяются&nbsp;из&nbsp;года&nbsp;в&nbsp;год.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Слова из&nbsp;чата</p>
<h2>Чем говорят между&nbsp;модулями</h2>
<div class="card white" style="margin-bottom:12px"><span class="icwrap" style="color:var(--sage-deep)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="8" y="10" width="32" height="30" rx="3"/><path d="M8 18h32M16 6v8M32 6v8"/><path d="M17 28l5 5 9-10"/></svg></span><h3>Вовремя</h3><p>Норма команды: намерение до&nbsp;десяти утра, итог дня до&nbsp;двадцати двух. Опоздание одного записывают на&nbsp;всех, поэтому люди подтягивают друг друга сами. Каждый вечер в&nbsp;чате появляется строка ведущей: «Спасибо всем, кто&nbsp;вовремя».</p></div>
<div class="card white" style="margin-bottom:12px"><span class="icwrap" style="color:var(--wine)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 12h32v20H22l-8 8v-8H8z"/><path d="M15 20h18M15 26h12"/></svg></span><h3>Щедрое слушание</h3><p>Слушать, не&nbsp;готовя ответ и&nbsp;не&nbsp;перебивая собеседника своим опытом. В&nbsp;утренних записях стоит отдельным пунктом: «Я&nbsp;практикую щедрое слушание. В&nbsp;результате у&nbsp;меня получается выстраивать отношения с&nbsp;теми, с&nbsp;кем сегодня&nbsp;общался».</p></div>
<div class="card white" style="margin-bottom:12px"><span class="icwrap" style="color:var(--sand)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M24 12c-4-3-10-4-15-3v26c5-1 11 0 15 3 4-3 10-4 15-3V9c-5-1-11 0-15 3z"/><path d="M24 12v26"/></svg></span><h3>Сто целей</h3><p>Задание, после которого человек впервые видит размер собственных запретов. Список пишется легко ровно до&nbsp;тех пор, пока не&nbsp;кончаются привычные желания. Из&nbsp;вечерней записи: «100&nbsp;целей для меня достаточно сложно даётся, очень узко&nbsp;мыслю».</p></div>
<div class="card white"><span class="icwrap" style="color:var(--wine)"><svg class="ic" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="24" cy="14" r="5"/><circle cx="10" cy="30" r="5"/><circle cx="38" cy="30" r="5"/><path d="M17 20l-3 5M31 20l3 5M16 34h16"/></svg></span><h3>Обратная связь</h3><p>В&nbsp;чате её&nbsp;зовут коротко: «ОС». Правило простое: говоришь о&nbsp;том, что видишь, без диагнозов и&nbsp;советов. Это отдельный навык, и&nbsp;пишут о&nbsp;нём честно: «пока всё ещё сложно принимать ОС, не&nbsp;понимаю зачем, если выбор уже&nbsp;сделан».</p></div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Что делает опоздавший</div><p>Пишет сам, не&nbsp;дожидаясь вопроса: называет промах и&nbsp;ставит намерение на&nbsp;завтра. Никто его при этом&nbsp;не&nbsp;отчитывает.</p></div>
<div class="box"><div class="lbl">Длина списка</div><div class="big">100</div><p>Столько пунктов просят написать на&nbsp;первом модуле. Первые идут легко, дальше список встаёт, и&nbsp;это само по&nbsp;себе&nbsp;открытие.</p></div>
</aside>
</div></div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-zapis.jpg" alt="Рукописные страницы на столе" loading="lazy"></div>
<div>
<p class="eyebrow">Откуда взялись эти слова</p>
<h2 style="font-size:1.9rem">Откуда взялись эти слова</h2>
<p>Ни&nbsp;одно слово из&nbsp;этого словаря не&nbsp;придумано за&nbsp;столом. Все они появились в&nbsp;работе, прижились в&nbsp;группах и&nbsp;остались с&nbsp;людьми после выпуска: в&nbsp;чатах, на&nbsp;встречах, на&nbsp;забегах вроде этого.</p>
</div>
</div>
</div></section>




""")

# ================= КОМУ: ПРЕДПРИНИМАТЕЛИ =================
FINCTA = """<section><div class="narrow">
<h2>Начни с разговора</h2>
<p class="sub" style="margin:0 0 26px">Собеседование в&nbsp;школу: разговор о&nbsp;твоей ситуации и&nbsp;честный ответ, чем мы&nbsp;можем помочь. Для читателей сайта&nbsp;бесплатно.</p>
<p class="btns"><a class="btn btn-wine" href="/chizhovy2/sessiya/">Записаться на&nbsp;собеседование</a> <a class="btn btn-ghost" href="/chizhovy2/gid/" style="margin-left:8px">Сначала почитать гайд</a></p>
</div></section>"""

P["dlya-predprinimatelej/index.html"] = ("Для предпринимателей · Настоящие отношения",
"Для всех опора, а сам устал: как школа работает с теми, кто привык всё тащить сам.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/istoriya-biznes.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Кому подходит · Предприниматели</p><h1>Для всех опора, а сам устал</h1>
<p class="lead">Бизнес, семья, статус: всё по&nbsp;списку. И&nbsp;усталость, о&nbsp;которой некому рассказать, потому что ты&nbsp;для всех опора. Мы&nbsp;шестнадцать лет работаем с&nbsp;людьми, которые привыкли тащить сами.</p></div></div>

<section><div class="narrow">
<h2>Знакомые ситуации</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('ceiling')}<h3>Дело упёрлось в потолок</h3><p>Рывки вверх быстро выравниваются обратно. Цифра оборота годами почти одна, и&nbsp;рынок тут ни при&nbsp;чём: держит старая запись.</p></div>
<div class="card">{icon('shield','var(--sand)')}<h3>Держать лицо</h3><p>Просить о&nbsp;помощи стыдно, показывать усталость нельзя. Панцирь, который когда-то спасал, теперь просто тяжёлый.</p></div>
<div class="card">{icon('gear','var(--sage-deep)')}<h3>Решения из&nbsp;страха</h3><p>Суета, перестраховка, откладывание больших ходов. Он&nbsp;шепчет тише жадности, но рулит&nbsp;чаще.</p></div>
<div class="card">{icon('cups')}<h3>Дома сил уже нет</h3><p>Семье достаётся остаток после дела. Обычно он&nbsp;мал, и&nbsp;все это&nbsp;чувствуют.</p></div>
</div>
<div class="pull"><div class="q">«Я&nbsp;понимал крах, но не&nbsp;понимал, как начать снова и&nbsp;где найти&nbsp;силы.»</div><div class="who">Из истории ученика-предпринимателя</div></div>
<p>Один из&nbsp;наших учеников пришёл ровно из&nbsp;этой точки: кассовый разрыв, долги, отвернувшиеся друзья. Его полная история, с&nbsp;сопротивлением и&nbsp;переломом, опубликована с&nbsp;его согласия: <a href="/chizhovy2/istorii/predprinimatel/">заново после дна</a>.</p>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что меняется у владельца бизнеса</h2>
<p>Работа идёт с&nbsp;причиной, и&nbsp;она у&nbsp;потолка, страха и&nbsp;усталости общая: старые решения, которые крутят <a href="/chizhovy2/metod/" style="color:#D08A5F">событийный круг</a>. Когда запись переписана, меняется сразу несколько сфер. Большие решения принимаются спокойно. Дело перестаёт держаться на&nbsp;надрыве. Дома снова видно человека, а не&nbsp;функцию.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>16&nbsp;лет</b><span>практики с&nbsp;состоявшимися взрослыми&nbsp;людьми</span></div>
<div class="nail"><b>10-20</b><span>человек в&nbsp;группе: окружение твоего уровня, без&nbsp;толпы</span></div>
<div class="nail"><b>3&nbsp;месяца</b><span>сопровождения: результат закрепляется в&nbsp;деле</span></div>
</div></div></section>


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как это выглядит в&nbsp;зале</p>
<h2>Что вскрывается первым</h2>
<p>Первое, что вскрывается почти у&nbsp;каждого, это привычка тащить всё самому. Она выглядит как сила и&nbsp;годами приносила результат, поэтому её&nbsp;не&nbsp;трогают. Пока в&nbsp;сцене не&nbsp;выясняется, что за&nbsp;ней стоит старое решение: просить опасно, доверять дорого, надёжнее одному.</p>
<p>Второе, это разговоры, которые откладываются годами: с&nbsp;партнёром по&nbsp;бизнесу, с&nbsp;отцом, с&nbsp;собой пятилетней давности. В&nbsp;зале такой разговор наконец происходит, и&nbsp;у&nbsp;него появляется финал.</p>
<h3>Что меняется в&nbsp;деле</h3>
<p>Решения начинают приниматься из&nbsp;спокойствия, а&nbsp;не&nbsp;из&nbsp;страха потерять. Появляется способность отдавать задачи и&nbsp;не&nbsp;проверять каждые двадцать минут. Меняется горизонт: человек перестаёт бегать спринты и&nbsp;начинает играть в&nbsp;долгую.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Из анкеты ученика</div><div class="big">50 млн</div><p>Кассовый разрыв, с&nbsp;которым он&nbsp;пришёл. Через полтора года: новые направления и&nbsp;цели кратно&nbsp;выше.</p></div>
<div class="box"><div class="lbl">Формат</div><p>Очно, малой группой. Телефоны в&nbsp;зале выключены у&nbsp;всех.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<p class="eyebrow">Что меняется в&nbsp;деле</p>
<h2>Четыре сдвига, о&nbsp;которых говорят чаще всего</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('ceiling','var(--copper)')}<h3>Решения из&nbsp;спокойствия</h3><p>Крупные ходы перестают приниматься на&nbsp;адреналине и&nbsp;страхе потерять. Меняется не&nbsp;стратегия, а&nbsp;состояние, из&nbsp;которого она пишется.</p></div>
<div class="card">{icon('people')}<h3>Способность отдавать</h3><p>Задачи уходят команде без проверки каждые двадцать минут. Оказывается, дело не&nbsp;в&nbsp;людях, а&nbsp;в&nbsp;старом решении «надёжнее самому».</p></div>
<div class="card">{icon('route','var(--sage-deep)')}<h3>Горизонт вдолгую</h3><p>Спринты сменяются дистанцией. Появляются направления, которые не&nbsp;дают денег завтра, но&nbsp;меняют масштаб через год.</p></div>
<div class="card">{icon('cups','var(--sand)')}<h3>Дом перестаёт быть фоном</h3><p>Самое частое наблюдение: сначала выравнивается дома, потом в&nbsp;делах. Не&nbsp;наоборот.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<h2>Что обычно мешает решиться</h2>
<p>Люди этого склада откладывают такую работу годами, и&nbsp;причины повторяются. Разберём три главные, потому что они&nbsp;же держат и&nbsp;сам потолок.</p>
<div class="card white" style="margin:20px 0 12px">{icon('hourglass')}<h3>«Разберусь, когда станет посвободнее»</h3><p>Свободнее не&nbsp;становится: дело забирает ровно то&nbsp;время, которое ему отдаёшь. Пять дней погружения выглядят дорого до&nbsp;тех пор, пока не&nbsp;посчитаешь, сколько лет уже съел один и тот&nbsp;же круг.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('shield','var(--sage-deep)')}<h3>«Я не из&nbsp;тех, кто ходит на&nbsp;тренинги»</h3><p>Понятная позиция после рынка, где обещают миллионы за&nbsp;выходные. Здесь другой формат: малая группа, отбор через разговор и&nbsp;никаких залов с&nbsp;таймерами. Проверить просто, начав с&nbsp;<a href="/chizhovy2/somneniya/">честного разбора сомнений</a>.</p></div>
<div class="card white">{icon('people','var(--sand)')}<h3>«Не&nbsp;хочу говорить о&nbsp;личном при чужих»</h3><p>В группе оказываются такие&nbsp;же взрослые люди с&nbsp;похожими историями, а&nbsp;личное остаётся в&nbsp;зале: это <a href="/chizhovy2/bezopasnost/">базовое правило</a>. Глубину выбираешь сам, темп твой.</p></div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Что было в&nbsp;точке А</div><div class="big">50 млн</div><p>Кассовый разрыв, с&nbsp;которым он&nbsp;пришёл. Через полтора года: новые направления и&nbsp;цели кратно&nbsp;выше.</p></div>
</aside>
</div></div></section>

<section class="dark"><div class="narrow">
<h2>Что меняется в&nbsp;деле</h2>
<p>Мы не&nbsp;учим управлять компанией и не&nbsp;даём бизнес-советов. Работа идёт с&nbsp;тем, из&nbsp;какого состояния принимаются решения. Рычаг оказывается сильным. Из&nbsp;покоя человек по-другому ведёт переговоры, легче делегирует и&nbsp;точнее считает&nbsp;риск.</p>
<p>Ученики чаще всего называют три сдвига: перестал держать всё на&nbsp;себе, начал видеть доску целиком вместо одной клетки, стал играть в&nbsp;долгую. Как это выглядело в&nbsp;жизни, видно в&nbsp;<a href="/chizhovy2/istorii/predprinimatel/" style="color:#D08A5F">истории ученика</a>.</p>
</div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-biznes.jpg" alt="Кабинет после всех" loading="lazy"></div>
<div>
<p class="eyebrow">Про что это</p>
<h2 style="font-size:1.9rem">Кабинет после всех</h2>
<p>Все ушли, дела сделаны, а&nbsp;лёгкости нет. Обороты растут, внутри пусто. С&nbsp;этим и&nbsp;приходят чаще всего.</p>
</div>
</div>
</div></section>

{FINCTA}
""")

# ================= КОМУ: ЖЕНЩИНЫ =================
P["dlya-zhenshchin/index.html"] = ("Для женщин · Настоящие отношения",
"Отношения, состояние, сценарии: как школа работает с теми, кто устал жить в режиме ожидания и обслуживания.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-m1.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Кому подходит · Женщины</p><h1>Вернуть себя себе</h1>
<p class="lead">Годами ждёшь, что&nbsp;тебя заметят, оценят, что&nbsp;близкий наконец изменится. Здесь работа начинается с&nbsp;другого конца: с&nbsp;твоего состояния, привычных реакций и&nbsp;той половины отношений, которая зависит от&nbsp;тебя.</p></div></div>

<section><div class="narrow">
<h2>С чем приходят чаще всего</h2>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('loop')}<h3>Один сценарий с&nbsp;разными людьми</h3><p>Мужчины разные, финал одинаковый. Значит, дело не в&nbsp;них: сюжет приходит вместе с&nbsp;тобой, разворачивается по&nbsp;одной и той&nbsp;же схеме, и&nbsp;переписать его получится только&nbsp;изнутри.</p></div>
<div class="card">{icon('cups','var(--sand)')}<h3>Быт вместо близости</h3><p>Один календарь на&nbsp;двоих, разговоры про логистику. Не&nbsp;ссоритесь, потому что&nbsp;незачем. А&nbsp;хочется, чтобы снова было о&nbsp;чём молчать вдвоём.</p></div>
<div class="card">{icon('flame','var(--sage-deep)')}<h3>Чувства под анестезией</h3><p>Научилась обезболивать и не&nbsp;слышать себя. Снаружи «всё нормально», внутри давно тихо и&nbsp;пусто.</p></div>
<div class="card">{icon('speech')}<h3>Говоришь, а тебя не слышат</h3><p>Просьбы звучат как упрёки, разговоры кончаются глухой стеной. Дело не в&nbsp;словах: в&nbsp;состоянии, из&nbsp;которого они&nbsp;сказаны.</p></div>
</div>
<div class="pull"><div class="q">«Теперь знаю, что могу быть яркой, настоящей, звонкой, сама по&nbsp;себе.»</div><div class="who">Участница второго модуля</div></div>
</div></section>

<section class="dark"><div class="narrow">
<h2>Что меняется</h2>
<p>На&nbsp;сцене видно, где чувства ушли в&nbsp;тень и&nbsp;какое решение их&nbsp;там держит: чаще всего оно принято очень рано, там, где показывать себя было опасно или бессмысленно. Когда запись переписана, возвращается то, что было под анестезией: яркость, желания, голос. Близкие замечают это раньше тебя. Отношения подтягиваются следом, <a href="/chizhovy2/para/" style="color:#D08A5F">даже когда работает один из&nbsp;двоих</a>.</p>
</div>
<div class="wrap"><div class="nails nails3" style="margin-top:24px">
<div class="nail"><b>Сцена</b><span>работа телом и&nbsp;эмоцией, где хранится&nbsp;запись</span></div>
<div class="nail"><b>Группа</b><span>место, где тебя слышат с первого&nbsp;слова</span></div>
<div class="nail"><b>90&nbsp;дней</b><span>практики, чтобы новое состояние стало&nbsp;обычным</span></div>
</div></div></section>


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Как это выглядит в&nbsp;зале</p>
<h2>С чего начинается работа</h2>
<p>Почти всегда с&nbsp;одной сцены: обычный разговор дома, где всё пошло по&nbsp;знакомому кругу. Женщина ставит её&nbsp;в&nbsp;центре зала, участники встают на&nbsp;роли, и&nbsp;впервые становится видно со&nbsp;стороны, кто какой шаг делает первым.</p>
<p>Дальше обычно выясняется неприятное: часть шагов делает она сама. Не&nbsp;из&nbsp;вредности, а&nbsp;по&nbsp;старому решению, принятому когда-то в&nbsp;детстве: «просить нельзя», «если не&nbsp;я, то&nbsp;никто», «нужно потерпеть, и&nbsp;он&nbsp;поймёт». Это решение и&nbsp;меняют прямо в&nbsp;сцене.</p>
<h3>Что меняется дома</h3>
<p>Первое, что замечают, это тишина вместо привычного скандала на&nbsp;ровном месте. Второе, что муж или партнёр вдруг начинает разговаривать иначе, хотя на&nbsp;тренинг не&nbsp;ходил. Так и&nbsp;работает половина общего сценария: меняется одна сторона, конструкция перестаёт держаться.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Формат</div><div class="big">2,5 дня</div><p>Первый модуль очно, малой группой.</p></div>
<div class="box"><div class="lbl">Можно&nbsp;ли одной</div><p>Да. Больше половины приезжают без партнёра, и&nbsp;это работает.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<p class="eyebrow">Что меняется дома</p>
<h2>Четыре перемены, заметные первыми</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('speech','var(--copper)')}<h3>Разговоры без обвинений</h3><p>Уходит привычка начинать с&nbsp;претензии. Появляется возможность сказать прямо, чего хочешь, без намёков и&nbsp;проверок.</p></div>
<div class="card">{icon('shield')}<h3>Пропадает роль «сильной»</h3><p>Больше не&nbsp;нужно тащить всё и&nbsp;держать лицо. Просить о&nbsp;помощи оказывается не&nbsp;поражением, а&nbsp;нормальным ходом.</p></div>
<div class="card">{icon('flame','var(--sage-deep)')}<h3>Возвращается интерес</h3><p>Сначала к&nbsp;себе: что мне нравится, чего я&nbsp;хочу. Потом к&nbsp;партнёру: что с&nbsp;ним происходит на&nbsp;самом деле.</p></div>
<div class="card">{icon('lens','var(--sand)')}<h3>Видно свою половину</h3><p>Становится ясно, какие шаги в&nbsp;общем круге делаешь ты&nbsp;сама. Это неприятное открытие, но&nbsp;именно оно даёт рычаг.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<h2>Три частых вопроса</h2>
<div class="card white" style="margin:20px 0 12px">{icon('speech')}<h3>«А если муж против?»</h3><p>Так бывает часто, и&nbsp;это не&nbsp;повод отказываться от&nbsp;своей работы: приходить одной можно и&nbsp;нужно, потому что твоя половина общего сценария всё равно в&nbsp;твоих руках. Многие мужчины приходят вторым заходом сами, увидев перемены дома. Про совместный формат: <a href="/chizhovy2/para/">тренинг для пар</a>.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('cups','var(--sage-deep)')}<h3>«Куда деть детей на&nbsp;пять дней?»</h3><p>Вопрос решаемый, и&nbsp;его стоит решить. Пять дней в&nbsp;году на&nbsp;себя это меньше, чем женщины обычно тратят на&nbsp;чужие дела за&nbsp;неделю. Первый модуль вообще идёт с&nbsp;вечера пятницы по&nbsp;воскресенье.</p></div>
<div class="card white">{icon('flame','var(--sand)')}<h3>«Я снова буду плакать при всех?»</h3><p>Слёзы в&nbsp;зале случаются, и&nbsp;это разморозка, а&nbsp;вовсе не&nbsp;слабость. Участницы говорят об&nbsp;этом как о&nbsp;самом ценном: «впервые за&nbsp;годы плакала при людях и&nbsp;поняла, что это не&nbsp;стыдно».</p></div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Формат</div><div class="big">2,5 дня</div><p>Первый модуль очно. Дальше решаешь сама, идти&nbsp;ли дальше.</p></div>
</aside>
</div></div></section>

<section class="dark"><div class="narrow">
<h2>Чего здесь точно не&nbsp;будет</h2>
<p>Ни&nbsp;уроков женственности, ни&nbsp;советов «как удержать мужчину», ни&nbsp;списков правильного поведения. Мы не&nbsp;делим людей на&nbsp;роли и не&nbsp;выдаём инструкций, как надо жить.</p>
<p>Работа идёт с&nbsp;другим: где ты&nbsp;себя приглушила, какое решение это держит и&nbsp;что вернётся, когда оно перестанет действовать. Дальше ты&nbsp;решаешь сама, как это применить: в&nbsp;паре, в&nbsp;деле, с&nbsp;детьми, с&nbsp;матерью. Принципы школы описаны в&nbsp;<a href="/chizhovy2/manifest/" style="color:#D08A5F">манифесте</a>.</p>
</div></section>

<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-zhenshchina.jpg" alt="Вечер, когда всё уже сказано" loading="lazy"></div>
<div>
<p class="eyebrow">Про что это</p>
<h2 style="font-size:1.9rem">Вечер, когда всё уже сказано</h2>
<p>Он&nbsp;ушёл в&nbsp;телефон, ты&nbsp;сидишь на&nbsp;кухне и&nbsp;прокручиваешь разговор по&nbsp;кругу. Знакомо почти каждой, кто сюда приходит.</p>
</div>
</div>
</div></section>

{FINCTA}
""")

# ================= КАК ПРОХОДИТ =================
P["kak-prohodit/index.html"] = ("Как проходит обучение · Настоящие отношения",
"Путь ученика по шагам: собеседование, три модуля, недели на проверку в жизни, сопровождение. Что происходит в зале.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-06.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Как проходит</p><h1>Путь ученика по&nbsp;шагам</h1>
<p class="lead">Без сюрпризов: рассказываем по&nbsp;порядку, что&nbsp;будет от&nbsp;первого разговора до&nbsp;перемен, которые остаются надолго. Каждый шаг добровольный, на&nbsp;любом можно остановиться.</p></div></div>

<section><div class="wrap">
<p class="eyebrow">Маршрут</p>
<h2>От собеседования до&nbsp;Марафона</h2>
<div class="timeline" style="margin-top:28px">{timeline_svg()}</div>
<div class="timeline-m" style="margin-top:28px">
<div class="tm"><div class="c">I</div><div><b>Возвращение к&nbsp;себе</b><span>2,5 дня очно</span></div></div>
<div class="gap">месяц на&nbsp;проверку в жизни</div>
<div class="tm"><div class="c">II</div><div><b>Внутренняя свобода</b><span>5 дней очно</span></div></div>
<div class="gap">ещё 3-5 недель до&nbsp;финала</div>
<div class="tm last"><div class="c">III</div><div><b>Создатель реальности</b><span>3 месяца в&nbsp;жизни, результаты&nbsp;остаются</span></div></div>
</div>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">0</span>{icon('speech')}<h3>Собеседование</h3><p>Живой разговор: твоя ситуация, честный взгляд и&nbsp;решение с&nbsp;двух сторон, по пути&nbsp;ли нам. Для&nbsp;читателей сайта бесплатно.</p></div>
<div class="card"><span class="bignum">1-2</span>{icon('people','var(--sage-deep)')}<h3>Очные модули</h3><p>Погружение на&nbsp;несколько дней: сцены, разборы, работа с&nbsp;состоянием в&nbsp;группе 10-20 человек. Между модулями несколько недель: новое проверяется обычной жизнью.</p></div>
<div class="card"><span class="bignum">3</span>{icon('calendar','var(--sand)')}<h3>Марафон</h3><p>Три месяца в&nbsp;настоящей жизни: команда, еженедельные разборы с&nbsp;ведущими и&nbsp;<a href="/chizhovy2/praktiki/">ежедневная практика</a>.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Что происходит в&nbsp;зале</h2>
<p>Ядро работы: <a href="/chizhovy2/istoki/moreno-psihodrama/">живая сцена</a>. Ты&nbsp;называешь ситуацию, которая держит, группа помогает её&nbsp;построить, и&nbsp;несостоявшийся разговор наконец происходит. Рядом разборы, работа с&nbsp;состоянием и&nbsp;простые приёмы, которые уезжают с&nbsp;тобой домой и&nbsp;делают своё дело в&nbsp;обычный вторник, когда никакой группы рядом&nbsp;нет.</p>
<p>Глубина всегда добровольна: никто не&nbsp;вытаскивает силой, темп каждый выбирает сам. Обычно уже к&nbsp;вечеру первого дня зал перестаёт быть чужим: у&nbsp;людей одинаковые боли, и в&nbsp;соседней истории ты&nbsp;узнаёшь свою. Подробнее о&nbsp;рамках: <a href="/chizhovy2/bezopasnost/">безопасность и&nbsp;границы</a>.</p>
<div class="pull"><div class="q">«Ты получишь ровно ту&nbsp;порцию, которая нужна именно&nbsp;сейчас.»</div><div class="who">Слова выпускника новичкам</div></div>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Организация</p>
<h2>Бытовые вопросы</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('calendar')}<h3>Когда и&nbsp;где</h3><p>Очно в&nbsp;Москве, малой группой. Первый модуль начинается в&nbsp;пятницу вечером, чтобы не&nbsp;пришлось брать отпуск. Даты ближайшего набора называем на&nbsp;собеседовании.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Сколько человек</h3><p>От десяти до&nbsp;двадцати. Меньше не&nbsp;даёт нужной динамики сцены, больше лишает камерности: за&nbsp;шестнадцать лет цифра проверена десятками групп.</p></div>
<div class="card">{icon('shield','var(--sand)')}<h3>Что взять с&nbsp;собой</h3><p>Удобную одежду, воду и&nbsp;готовность к&nbsp;длинным дням. Ни&nbsp;конспектов, ни&nbsp;подготовки: материал приносишь ты&nbsp;сам, своей жизнью.</p></div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Что взять и&nbsp;к&nbsp;чему готовиться</p>
<h2>Бытовые вещи, о&nbsp;которых спрашивают</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('book','var(--copper)')}<h3>Что взять</h3><p>Удобную одежду, воду и&nbsp;тетрадь. Записи ведут от&nbsp;руки: рука успевает за&nbsp;мыслью медленнее и&nbsp;оставляет главное.</p></div>
<div class="card">{icon('calendar')}<h3>Как с&nbsp;едой</h3><p>Обед общий, перерывы короткие. За&nbsp;столом случается половина разговоров, которые потом называют переломными.</p></div>
<div class="card">{icon('shield','var(--sage-deep)')}<h3>Телефоны</h3><p>Выключены на&nbsp;всё время работы зала, у&nbsp;всех, включая ведущих. Возвращаются в&nbsp;перерывах.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Что происходит между модулями</h2>
<p>Недели интеграции это рабочая часть программы. Ты&nbsp;выходишь в&nbsp;обычные дни и&nbsp;наблюдаешь: где новое уже держится, а&nbsp;где старая запись отыгрывает своё. Никаких заданий на&nbsp;оценку, только честные наблюдения.</p>
<p>Ведущие остаются на&nbsp;связи, а&nbsp;группа продолжает общаться в&nbsp;чате. Этот материал становится основой следующего погружения: приходишь не с&nbsp;чистого листа, а с&nbsp;конкретными местами, где заклинило.</p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">По&nbsp;часам</p>
<h2>Как выглядит день на&nbsp;модуле</h2>
<p>День начинается задолго до&nbsp;зала. Одни выходят на&nbsp;пробежку, у&nbsp;других зарядка и&nbsp;холодный душ. Дальше завтрак и&nbsp;первая запись в&nbsp;чат. К&nbsp;началу приезжают заранее: опоздание одного здесь записывают на&nbsp;всю команду. Это выясняется в первое же&nbsp;утро.</p>
<p>Потом длинный рабочий блок. Телефоны лежат в&nbsp;стороне. Один выносит свою историю в&nbsp;центр зала, остальные работают в&nbsp;ролях или смотрят и&nbsp;после говорят, что откликнулось в их&nbsp;собственной жизни. Обед короткий и&nbsp;общий. За&nbsp;столом разговор продолжает то, что было в&nbsp;зале, и&nbsp;половина открытий случается именно&nbsp;там.</p>
<p>К&nbsp;вечеру приходит настоящая усталость. Заниматься собственной жизнью столько часов подряд непривычно, и&nbsp;тело чувствует это раньше головы. После зала команда чаще всего идёт ужинать вместе. До&nbsp;двадцати двух каждый пишет в&nbsp;чат открытия и&nbsp;благодарности. Смысл в&nbsp;том, чтобы назвать увиденное словами в тот&nbsp;же вечер: иначе к&nbsp;утру от&nbsp;него остаётся только общее хорошее&nbsp;чувство.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Окно утренней записи</div><div class="big">9-10</div><p>Час на намерение. Кто не успел, объясняется перед всеми: отметку о времени получает вся команда сразу.</p></div>
<div class="box"><div class="lbl">Перерыв</div><p>Обед вместе с&nbsp;группой, воздух, тишина. Уехать «на&nbsp;пару звонков» и&nbsp;вернуться в&nbsp;процесс не&nbsp;получается, поэтому дела закрывают до&nbsp;модуля.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Честно</p>
<h2>Что бывает тяжело</h2>
<p>Сопротивление появляется почти у&nbsp;всех. Это ожидаемая часть работы. Один спорит с&nbsp;ведущими, другой весь день молчит, третий шутит там, где больно. Выпускник описал свои первые недели так: «Я&nbsp;долго сопротивлялся, как баран. Меня доставали, показывали, что не&nbsp;так и&nbsp;где не&nbsp;так, я&nbsp;опять проваливался в&nbsp;своё». На это ушли месяцы.</p>
<p>Дальше тяжело становится через две-три недели после погружения. Старое возвращается и проверяет, всерьёз ли человек решил. В чате это выглядит так: «сегодня сложный день морально, откат мощный, как будто этого месяца и не было, свалился в ту точку, с которой начинал первый модуль». Проходит за несколько дней, и быстрее всего у тех, кто пишет об этом команде тем же вечером.</p>
<p>Помогает простое: держаться своих часов в чате, позвонить напарнику, вернуться к целям и не принимать больших решений на пике эмоции. Ведущие остаются на связи между модулями, и в группе сразу видно, если человек пропал.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Когда накрывает</div><div class="big">2-3 неделя</div><p>Обычный срок отката после модуля. Про него предупреждают заранее: так человек видит, что дело не в нём&nbsp;одном.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/real/real-03.jpg" alt="Группа после модуля" loading="lazy"></div>
<div>
<p class="eyebrow">Путь целиком</p>
<h2 style="font-size:1.9rem">Последний вечер модуля</h2>
<p>Последний вечер модуля проходит в&nbsp;кругу: каждый говорит, с&nbsp;чем уезжает. Фотографируются уже после, когда всё сказано.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-dver.jpg" alt="Дверь, в которую входят" loading="lazy"></div>
<div>
<p class="eyebrow">С чего начинается</p>
<h2 style="font-size:1.9rem">С чего начинается путь</h2>
<p>Всё начинается с&nbsp;одного разговора. Дальше человек сам решает, идти&nbsp;ли дальше: каждый следующий шаг добровольный, и&nbsp;на&nbsp;любом можно остановиться без объяснений.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-most.jpg" alt="Недели, которые решают" loading="lazy"></div>
<div>
<p class="eyebrow">Между модулями</p>
<h2 style="font-size:1.9rem">Недели между модулями</h2>
<p>Между очными ступенями проходит от&nbsp;трёх до&nbsp;пяти недель. Это не&nbsp;пауза: увиденное надо попробовать руками в&nbsp;обычной жизни, где никто не&nbsp;поддерживает и&nbsp;не&nbsp;разбирает по&nbsp;шагам. С&nbsp;этими попытками человек и&nbsp;приходит на&nbsp;следующий модуль.</p>
</div>
</div>
</div></section>

{FINCTA}
""")

# ================= ПРАКТИКИ =================
P["praktiki/index.html"] = ("Ежедневные практики · Настоящие отношения",
"Утреннее намерение, вечерние открытия и благодарности, маятники и важность: как выглядит день ученика.", "programma", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/slovar-hero.jpg')"></div><div class="veil"></div>
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
<div class="card white" style="margin-bottom:12px">{icon('people')}<h3>Быть вкладом</h3><p>Развернуть фокус с&nbsp;«что мне дадут» на&nbsp;«что я&nbsp;даю»: дома, в&nbsp;команде, в&nbsp;деле и в&nbsp;разговоре, который не&nbsp;хочется начинать. Участники отмечают: энергия от&nbsp;этого прибывает, и&nbsp;люди поворачиваются&nbsp;лицом.</p></div>
<div class="card white">{icon('sunrise','var(--sage-deep)')}<h3>Открытия и&nbsp;благодарности</h3><p>Вечером короткий итог: что открыл про себя, за&nbsp;что спасибо дню и&nbsp;людям. Закрепляет новый способ жить надёжнее любой мотивации.</p></div>

<p class="note" style="margin-top:18px">Термины из&nbsp;практик разобраны в&nbsp;<a href="/chizhovy2/slovar/">словаре школы</a>, живой пример девяноста дней: <a href="/chizhovy2/istorii/komanda-mir/">история команды «МИР»</a>.</p>
</div></section>

<section><div class="narrow">
<h2>Почему это работает</h2>
<p>Практики выглядят обманчиво просто: пара минут утром, пара вечером. Сила в&nbsp;другом. Каждое утро ты&nbsp;выбираешь состояние сам, вместо того чтобы получить его по&nbsp;умолчанию от&nbsp;новостей и&nbsp;чужого настроения. Каждый вечер закрепляешь то, что сработало.</p>
<p>За этим стоит понятный механизм: конкретно сформулированное намерение резко повышает шанс дойти до&nbsp;действия, а&nbsp;названные вслух чувства теряют власть. Подробнее в&nbsp;разделе <a href="/chizhovy2/istoki/nauka/">про науку</a>. Плюс эффект накопления. Девяносто повторов подряд делают усилие&nbsp;привычкой.</p>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Что мешает чаще всего</p>
<h2>Четыре причины, по&nbsp;которым практика встаёт</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('hourglass','var(--copper)')}<h3>«Нет пяти минут»</h3><p>Обычно это не&nbsp;про время, а&nbsp;про нежелание встречаться с&nbsp;собой. Пять минут находятся сразу, как только человек это признаёт.</p></div>
<div class="card">{icon('speech')}<h3>Пишет для&nbsp;галочки</h3><p>Красивые формулировки вместо честных. Такую запись видно сразу: она гладкая и&nbsp;ни&nbsp;о&nbsp;чём.</p></div>
<div class="card">{icon('loop','var(--sage-deep)')}<h3>Бросает после срыва</h3><p>Один пропущенный день превращается в&nbsp;неделю. Возвращаться после срыва тяжелее, чем начинать, поэтому команда вытаскивает сразу.</p></div>
<div class="card">{icon('shield','var(--sand)')}<h3>Делает в&nbsp;одиночку</h3><p>Без общего чата практика разваливается за&nbsp;две недели. Не&nbsp;из-за слабой воли: некому заметить, что тебя нет.</p></div>
</div>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Частые ошибки</p>
<h2>Из-за чего практика перестаёт работать</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('book','var(--copper)')}<h3>Писать для галочки</h3><p>Формальная запись перестаёт быть выбором. Лучше одна честная строка, чем красивый абзац ни о&nbsp;чём.</p></div>
<div class="card">{icon('loop','var(--copper)')}<h3>Бросать после срыва</h3><p>Пропустил три дня, решил, что не&nbsp;получилось. Практика начинается заново с&nbsp;любого дня, и&nbsp;это нормальный ход.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Делать в&nbsp;одиночку</h3><p>Без команды и&nbsp;разборов человек не&nbsp;видит собственных слепых зон. Поэтому практика идёт внутри группы, а не в&nbsp;личном блокноте.</p></div>
</div>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Механика</p>
<h2>Как выглядит запись в&nbsp;чате</h2>
<p>Утро начинается с&nbsp;образа. Первая строка описывает состояние, из&nbsp;которого человек идёт в&nbsp;день: «Я&nbsp;сегодня спокойная, доверяю себе и&nbsp;миру, не&nbsp;критикую и не&nbsp;оцениваю». Дальше идут пункты, и&nbsp;каждый заканчивается результатом: «провёл встречу, подписали договор», «сделал замер, согласовал&nbsp;стоимость».</p>
<p>Пишут в&nbsp;прошедшем времени, как о&nbsp;случившемся: «легла спать до&nbsp;23:00», «провела день в&nbsp;дороге спокойно». Первые дни рука сопротивляется такой форме. Дальше привыкает, и&nbsp;пункты становятся точнее: имена, сроки, суммы, конкретные&nbsp;разговоры.</p>
<p>Ведущая правит формулировки прямо в чате. Увидела частицу «не», отвечает сразу: «Частичку „не“ мозг не замечает. Переформулируй, что хочешь создать». Поэтому «не раздражаюсь» превращается в «спокойно принимаю людей», и в день он идёт уже с ней.</p>
<p>Вечером две части. Открытие это то, что человек увидел про себя за&nbsp;день, и&nbsp;отсюда легко соскользнуть в&nbsp;пересказ событий или в&nbsp;жалобу. Ведущая ловит это одним вопросом: «Сегодня у&nbsp;меня был откат. Это открытие? Или&nbsp;жалоба?».</p>
<p>Вечерний список пишут поимённо. Самые сильные строки достаются тем, с&nbsp;кем было тяжело: «Благодарен Мише, что сегодня истерил». В том&nbsp;же списке появляются охранник, бариста, водитель такси, который вернул телефон, и&nbsp;«случайное солнце в&nbsp;Питере». Себя туда тоже вписывают, и&nbsp;поначалу это даётся труднее&nbsp;всего.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Сон попал в&nbsp;практику</div><div class="big">112</div><p>Столько раз в&nbsp;одном чате встретилась строка «легла спать до&nbsp;23:00». Её писали четырнадцать человек из&nbsp;двадцати.</p></div>
<div class="box"><div class="lbl">Форма записи</div><p>Образ в первой строке, пункты с результатом, прошедшее время. Три детали, из-за которых запись работает. Без них выходит обычный дневник.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Через месяц</p>
<h2>Что меняется, когда практика&nbsp;прижилась</h2>
<p>Задание из ста пунктов показывает это первым. Первые строки идут легко, дальше список встаёт. «Сто целей оказалось сложным заданием. Поняла, что давно ставлю себе ограничения в желаниях, не разрешаю мечтать», написала участница на пятый день. Через месяц список дописывается, и в нём появляется то, о чём человек молчал годами.</p>
<p>Меняется и&nbsp;вечерняя запись. Сначала «всё бесит», а&nbsp;следом уже разбор: «отследила, откуда такая прищепка негатива». Смотреть на&nbsp;свой день становится привычкой, и&nbsp;тяжёлое перестаёт копиться&nbsp;внутри.</p>
<p>Самое неожиданное происходит дома. В&nbsp;одной семье за&nbsp;родителями каждый вечер наблюдала дочка. Однажды она написала свои намерения и&nbsp;попросила отправить их в&nbsp;командный чат. Первая строка звучала так: «Я&nbsp;сегодня смешная». Дальше шло «нарисовала что-то не&nbsp;реальное, а&nbsp;сказочное».</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Что сюда попадает</div><p>Сон, тренировка, звонок маме, цена в&nbsp;переговорах и&nbsp;разговор, который откладывали полгода.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/real/real-10.jpg" alt="Команда участников" loading="lazy"></div>
<div>
<p class="eyebrow">Кто это делает</p>
<h2 style="font-size:1.9rem">Практики держит команда</h2>
<p>В&nbsp;одиночку ежедневная практика разваливается за&nbsp;пару недель. Поэтому её&nbsp;ведут командой: люди пишут в&nbsp;общий чат, видят друг друга и&nbsp;вытаскивают того, кто выпал. Это те&nbsp;самые люди с&nbsp;фотографии.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-chasy.jpg" alt="Практика живёт по часам" loading="lazy"></div>
<div>
<p class="eyebrow">Каждый день</p>
<h2 style="font-size:1.9rem">Практика живёт по&nbsp;часам</h2>
<p>Утреннее намерение занимает пять минут, вечерний разбор десять. Сила не&nbsp;в&nbsp;длительности, а&nbsp;в&nbsp;том, что это происходит каждый день, включая те, когда не&nbsp;хочется совсем.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-svecha.jpg" alt="Разбор дня перед сном" loading="lazy"></div>
<div>
<p class="eyebrow">Каждый вечер</p>
<h2 style="font-size:1.9rem">Разбор дня перед сном</h2>
<p>Вечерняя часть занимает десять минут: что сбылось из&nbsp;утреннего намерения, где сорвался, за&nbsp;что благодарен. Последний пункт кажется формальностью ровно до&nbsp;того дня, когда человек впервые не&nbsp;может назвать ничего, и&nbsp;это становится самой честной записью недели.</p>
</div>
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
<p>Школу ведёт пара, которая семнадцать лет строит свои отношения: с&nbsp;бытом, кризисами и&nbsp;выходами из&nbsp;них. Поэтому здесь не&nbsp;учат жить и не&nbsp;мотивируют со&nbsp;сцены. Вместе разбираются: откуда берётся твоя реакция и&nbsp;что с&nbsp;этим делать&nbsp;по‑настоящему.</p>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Принципы, которые не&nbsp;продаются</p>
<h2>На чём стоим</h2>
<div class="grid2" style="margin-top:26px">
<div class="card">{icon('target','var(--copper)')}<h3>Отбор важнее выручки</h3><p>Вход через собеседование, и&nbsp;это фильтр, а не&nbsp;формальность. Отговорить можем так&nbsp;же честно, как&nbsp;пригласить.</p></div>
<div class="card">{icon('people','var(--copper)')}<h3>Маленькая группа важнее большого зала</h3><p>Группы 10-20 человек, каждого знаем по&nbsp;имени. Расти будем числом групп, зал большим не&nbsp;станет.</p></div>
<div class="card">{icon('speech','var(--copper)')}<h3>Честность важнее красивой картинки</h3><p>Истории учеников публикуем с&nbsp;согласия и&nbsp;без глянца, результат у&nbsp;каждого свой. Истоки метода <a href="/chizhovy2/istoki/" style="color:#D08A5F">называем&nbsp;открыто</a>.</p></div>
<div class="card">{icon('mountain','var(--copper)')}<h3>Глубина важнее скорости</h3><p>Мы за&nbsp;работу с&nbsp;причиной, поэтому формат длинный: очные дни, недели на&nbsp;проверку в&nbsp;жизни, сопровождение. Быстрых чудес не&nbsp;обещаем.</p></div>
</div>
</div></section>

<section><div class="narrow">
<h2>Во что мы&nbsp;верим</h2>
<p>Человек не&nbsp;сломан. Что&nbsp;бы с&nbsp;ним ни&nbsp;происходило, внутри цела способность выбирать, просто её&nbsp;перекрывают решения, принятые когда-то в&nbsp;трудный момент. Тогда они спасали. Сегодня держат.</p>
<p>Поэтому мы не&nbsp;чиним людей и не&nbsp;ставим диагнозов. Мы&nbsp;помогаем добраться до&nbsp;точки, где выбор был сделан впервые, и&nbsp;принять другое решение: осознанно, из&nbsp;сегодняшнего дня. Всё остальное человек делает сам, и в&nbsp;этом смысле школа возвращает авторские права на&nbsp;собственную жизнь.</p>
<p>Ещё мы&nbsp;верим, что глубокая работа возможна без надрыва и&nbsp;без цирка. Без криков со&nbsp;сцены, без унижения ради «слома эго», без таймеров на&nbsp;оплату и&nbsp;без ночных марафонов на&nbsp;выносливость, после которых истощение легко спутать с&nbsp;прорывом. Взрослому человеку достаточно честного зеркала и&nbsp;безопасного пространства, чтобы увидеть своё и&nbsp;сделать шаг.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Почему такое имя</p>
<h2>«Настоящие» значит без масок</h2>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('mirror')}<h3>С собой</h3><p>Первое, что здесь налаживается, это связь с&nbsp;самим собой. Пока внутри идёт война, снаружи мира не&nbsp;будет.</p></div>
<div class="card">{icon('cups','var(--sage-deep)')}<h3>С близкими</h3><p>Когда снимаются роли, в&nbsp;паре и в&nbsp;семье впервые за&nbsp;годы становится видно живого человека вместо функции.</p></div>
<div class="card">{icon('target','var(--sand)')}<h3>С делом и&nbsp;миром</h3><p>Дело, деньги, окружение перестают быть сценой, где нужно казаться. Оттого и&nbsp;результаты становятся другими.</p></div>
</div>
</div></section>
<section class="dark">`)
```
</div></section>
```
### (это первая закрывающая `</div></section>` после тёмной сетки из четырёх карточек; новый блок ложится сразу за ней)


<section><div class="wrap">
<p class="eyebrow">Как это видно в&nbsp;работе</p>
<h2>Пять решений, из&nbsp;которых собрана школа</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('people')}<h3>Малые группы</h3><p>10-20 человек, не&nbsp;больше. Иначе ведущие перестают видеть каждого, а&nbsp;человек превращается в&nbsp;зрителя.</p></div>
<div class="card">{icon('shield','var(--copper)')}<h3>Отбор на&nbsp;входе</h3><p>Разговор с&nbsp;каждым, кто пришёл, включая тех, кому мы&nbsp;в&nbsp;итоге скажем «сейчас не&nbsp;время».</p></div>
<div class="card">{icon('layers','var(--sage-deep)')}<h3>Длинный формат</h3><p>Очные дни, недели на&nbsp;проверку в&nbsp;жизни, три месяца сопровождения. Быстрых чудес не&nbsp;обещаем.</p></div>
<div class="card">{icon('lens','var(--sand)')}<h3>Работа с&nbsp;причиной</h3><p>Не&nbsp;снимаем симптом. Доходим до&nbsp;решения, которое крутит круг, и&nbsp;меняем его в&nbsp;сцене.</p></div>
<div class="card">{icon('cups')}<h3>Двое ведущих</h3><p>Мужская и&nbsp;женская сторона в&nbsp;одном зале. Любую семейную сцену разбирают с&nbsp;двух сторон.</p></div>
<div class="card">{icon('calendar','var(--copper)')}<h3>Жизнь после</h3><p>Команда остаётся вместе после выпуска. Практика без поддержки разваливается за&nbsp;две недели.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Проверка&nbsp;делом</p>
<h2>Как эти принципы выглядят в&nbsp;расписании</h2>
<p>Написать их&nbsp;легко. Дальше начинается цена: вот чем каждый из&nbsp;четырёх обходится школе на&nbsp;деле.</p>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Отбор</h3><p>Разговор с&nbsp;каждым, кто пришёл, включая тех, кому мы в&nbsp;итоге скажем «сейчас не&nbsp;время». Набор из-за этого идёт медленно, и&nbsp;группа иногда переносится на&nbsp;следующий поток. Мы на это&nbsp;согласны.</p></div>
<div class="card"><h3>Размер&nbsp;группы</h3><p>От&nbsp;десяти до&nbsp;двадцати человек в&nbsp;зале. Это значит, что за&nbsp;дни модуля очередь доходит до&nbsp;сцены каждого, а&nbsp;ведущие помнят, с&nbsp;чем именно ты&nbsp;пришёл в пятницу&nbsp;вечером.</p></div>
<div class="card"><h3>Честность</h3><p>Истории публикуются с&nbsp;согласия авторов, имена чаще всего убраны, суммы дохода на&nbsp;витрину не&nbsp;выносятся. Источники метода названы открыто, пятью отдельными&nbsp;<a href="/chizhovy2/istoki/">страницами</a>.</p></div>
<div class="card"><h3>Глубина</h3><p>Два с&nbsp;половиной дня, следом пять дней, потом ещё три месяца сопровождения. Короткого варианта у&nbsp;школы просто&nbsp;нет, и за&nbsp;один выходной здесь ничего не&nbsp;решается.</p></div>
</div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Между&nbsp;модулями</div><div class="big">3-5 недель</div><p>Пауза сделана нарочно: увиденное в&nbsp;зале должно осесть в&nbsp;обычной жизни, среди тех&nbsp;же людей и&nbsp;дел.</p></div>
<div class="box"><div class="lbl">В&nbsp;зале</div><div class="big">10-20</div><p>Столько человек в&nbsp;группе. Больше не&nbsp;берём: на&nbsp;двадцать первом сцена перестаёт доходить до&nbsp;всех.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Откуда это&nbsp;взялось</p>
<h2>Почему школа устроена именно&nbsp;так</h2>
<p>Шестнадцать лет люди приходят сюда по&nbsp;рекомендации, почти без рекламы. Выпускник зовёт друга, сестру, партнёра по&nbsp;делу. В&nbsp;плохое место близких не&nbsp;приводят, поэтому репутация здесь дороже любого набора: одна группа, собранная «лишь бы&nbsp;заполнить», стоила бы&nbsp;школе больше, чем несколько пустых мест.</p>
<p>Отсюда всё остальное. Отбор через разговор появился раньше сайта. Малые группы держатся потому, что в&nbsp;зале работают двое ведущих и&nbsp;каждый участник должен быть у&nbsp;них на&nbsp;виду. Правила зала мы&nbsp;называем до&nbsp;первого процесса, чтобы человек знал свои права раньше, чем станет&nbsp;уязвимым.</p>
<p>И поэтому&nbsp;же мы&nbsp;осторожны с&nbsp;обещаниями. Обещаем ровно то, что в&nbsp;наших руках: процесс, группу, сопровождение и&nbsp;опыт шестнадцати лет. Дальше метод срабатывает настолько, насколько в&nbsp;него включается сам человек, и&nbsp;поэтому результат у каждого&nbsp;свой.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Главный&nbsp;канал</div><div class="big">Сарафан</div><p>Большинство участников пришли по&nbsp;рекомендации выпускников. Так школа набирает с первого&nbsp;года.</p></div>
</aside>
</div></div></section>




{FINCTA}
""")

# ================= БЕЗОПАСНОСТЬ =================
P["bezopasnost/index.html"] = ("Безопасность и границы · Настоящие отношения",
"Честные рамки работы: кому школа не подойдёт, правила группы, добровольность глубины.", "voprosy", f"""
<div class="hero short"><div class="veil"></div>
<div class="in"><p class="eyebrow">Безопасность и&nbsp;границы</p><h1>Сначала правила, потом глубина</h1>
<p class="lead">Работать всерьёз можно только там, где безопасно. Поэтому у&nbsp;школы есть правила, и&nbsp;мы называем их&nbsp;до начала, а&nbsp;не после.</p></div></div>

<section><div class="narrow">
<h2>Что делает зал безопасным</h2>
<div class="card white" style="margin:20px 0 12px">{icon('route')}<h3>Глубину выбираешь сам</h3><p>Никто не&nbsp;вытаскивает силой: темп и&nbsp;меру открытости каждый выбирает сам. Сцена начинается, когда ты&nbsp;готов.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('shield','var(--sage-deep)')}<h3>Личное остаётся в&nbsp;зале</h3><p>Истории участников не&nbsp;выносятся из&nbsp;группы, это базовое правило. Публикуем только то, на&nbsp;что автор дал согласие, и&nbsp;спрашиваем каждый&nbsp;раз.</p></div>
<div class="card white">{icon('speech','var(--sand)')}<h3>Честность с первого дня</h3><p>Собеседование для того и&nbsp;нужно, чтобы решить с&nbsp;двух сторон, твоё&nbsp;ли это место. Если видим, что нет, говорим об этом&nbsp;сразу.</p></div>

<h2 style="margin-top:34px">Кому школа не&nbsp;подойдёт</h2>
<p>Тем, кто ищет волшебную таблетку за&nbsp;вечер. Тем, кто пока не&nbsp;готов работать в&nbsp;группе. И&nbsp;тем, кому сейчас нужна медицинская помощь: тренинг её не&nbsp;заменяет. Об&nbsp;этом мы&nbsp;говорим прямо на первом&nbsp;разговоре и&nbsp;подсказываем, куда идти, потому что погружение требует сил, а в&nbsp;остром состоянии оно скорее нагрузит, чем&nbsp;поможет.</p>
<p>Остальное про формат разобрано на&nbsp;странице <a href="/chizhovy2/voprosy/">вопросов и&nbsp;ответов</a>.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Правила зала</p>
<h2>О чём договариваемся на&nbsp;старте</h2>
<p class="sub">Эти договорённости озвучиваются в&nbsp;первый вечер, действуют все дни модуля и&nbsp;распространяются на&nbsp;всех, кто в&nbsp;зале, включая&nbsp;ведущих.</p>
<div class="grid3" style="margin-top:26px">
<div class="card">{icon('shield')}<h3>Конфиденциальность</h3><p>Всё, что прозвучало в&nbsp;зале, остаётся в&nbsp;зале. Своим опытом делиться можно, чужими историями&nbsp;нет.</p></div>
<div class="card">{icon('speech','var(--sage-deep)')}<h3>Говорим о&nbsp;себе</h3><p>Без советов, диагнозов и&nbsp;оценок в&nbsp;адрес других участников. Только свой опыт и свои&nbsp;чувства.</p></div>
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
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Если накрыло</p>
<h2>Что происходит, когда человеку&nbsp;тяжело</h2>
<p>Так бывает, и к этому здесь готовы. Слёзы в зале обычное дело, злость на ведущих тоже.</p>
<p>Главное правило: процесс не бросают на середине. Если человека накрыло, работу доводят до точки, где он снова стоит на ногах. Из роли выводят вслух и по имени, возвращают в сегодняшний день, дают спокойно посидеть. Второй ведущий в это время держит весь зал. Без внимания не остаётся никто.</p>
<p>Вечером человек тоже не&nbsp;один: команда, общий ужин, чат. Помогает и&nbsp;то, что рядом люди с&nbsp;похожими историями, а не&nbsp;наблюдатели.</p>
<p>Отдельный страх, который называют на&nbsp;собеседовании: «вдруг там окажется кто-то знакомый». Иногда так и&nbsp;бывает. Договорённость снимает вопрос: всё, что прозвучало, остаётся здесь. В&nbsp;одной группе двое коллег узнали друг друга в&nbsp;первый вечер, и&nbsp;работать это никому не&nbsp;помешало.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Договорённостей зала</div><div class="big">6</div><p>Их называют в&nbsp;первый вечер. Действуют они все дни работы и на&nbsp;всех, включая&nbsp;ведущих.</p></div>
<div class="box"><div class="lbl">Слово, которое повторяют чаще&nbsp;всего</div><div class="big">128 раз</div><p>Столько раз в&nbsp;одном командном чате встретилось «пространство». Так участники называют условия, в&nbsp;которых можно быть честным.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Границы</p>
<h2>Когда мы говорим «сейчас не&nbsp;время»</h2>
<p>Собеседование существует и&nbsp;для этого тоже. Есть ситуации, в&nbsp;которых погружение забирает больше, чем&nbsp;даёт. Мы&nbsp;называем их&nbsp;прямо, до&nbsp;всякой оплаты.</p>
<p>Первое: острое состояние, назначенные врачом препараты, свежая потеря близкого, зависимость в активной фазе. Пять дней подряд психика работает на пределе. В таком месте это лишняя нагрузка, и правильнее сначала получить помощь, которая лечит.</p>
<p>Второе: решение принял кто-то другой. Жена записала мужа, друг уговорил, начальник оплатил. Человек приезжает выполнить обязательство и&nbsp;все дни держит оборону. Группа в&nbsp;это время работает по-настоящему. Такому мы&nbsp;предлагаем сначала прийти на&nbsp;разговор одному.</p>
<p>Третье: запрос «скажите, что мне делать». Человек заранее ждёт, что за него решат: разводиться или терпеть, увольняться или остаться, прощать или закрыть тему навсегда. Таких ответов здесь не выдают ни ведущие, ни группа. Мы помогаем увидеть свою часть сюжета. Дальше выбирает сам человек, и делает это уже без тумана.</p>
<p>Отказ не&nbsp;значит «до&nbsp;свидания». Мы&nbsp;говорим, куда имеет смысл пойти сейчас, и&nbsp;оставляем дверь открытой: часть людей возвращается через полгода, кто-то спустя&nbsp;год.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Кто принимает решение</div><p>Обе стороны. По&nbsp;итогам часового разговора мы&nbsp;говорим своё «да» или «не&nbsp;сейчас», человек своё, и&nbsp;оба ответа&nbsp;равны.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-bezopasnost.jpg" alt="Что делает зал безопасным" loading="lazy"></div>
<div>
<p class="eyebrow">Границы</p>
<h2 style="font-size:1.9rem">Правила известны заранее</h2>
<p>Правила проговариваются до&nbsp;начала, а&nbsp;не&nbsp;после. Глубину каждый выбирает сам.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Когда становится тяжело</p>
<h2>Что делают ведущие</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('shield','var(--copper)')}<h3>Останавливают</h3><p>Работа прекращается в&nbsp;ту&nbsp;минуту, когда человек говорит «стоп». Это правило зала, записанное в&nbsp;договорённостях.</p></div>
<div class="card">{icon('people')}<h3>Остаются рядом</h3><p>После тяжёлой сцены человека не&nbsp;оставляют одного. Рядом сидит кто-то из&nbsp;группы или ведущий, пока не&nbsp;отпустит.</p></div>
<div class="card">{icon('route','var(--sage-deep)')}<h3>Отправляют дальше</h3><p>Если видно, что нужна другая помощь, говорим прямо и&nbsp;подсказываем, к&nbsp;кому идти. Брать человека ради заполненной группы не&nbsp;будем.</p></div>
</div>
</div></section>

{FINCTA}
""")

# ================= СООБЩЕСТВО =================
P["soobshchestvo/index.html"] = ("Сообщество выпускников · Настоящие отношения",
"Команды, забеги, поддержка после модулей: во что превращается группа после тренинга.", "otzyvy", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/real/real-12.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Сообщество</p><h1>Группа остаётся вместе</h1>
<p class="lead">Модуль заканчивается, а&nbsp;люди остаются рядом: общие практики, встречи, забеги и&nbsp;поддержка, которая работает даже в&nbsp;два часа ночи.</p></div></div>

<section><div class="narrow">
<h2>Во что превращается группа</h2>
</div>
<div class="wrap"><div class="grid3" style="margin-top:24px">
<div class="card">{icon('people')}<h3>Команда</h3><p>На&nbsp;Марафоне группа собирается вокруг общей цели, у&nbsp;каждого свой напарник. Такой уровень окружения многим встречается&nbsp;впервые.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Забеги</h3><p>Команды выходят на&nbsp;старты вместе с&nbsp;Алексеем: тело быстро выдаёт, где ты&nbsp;себя обманываешь, и&nbsp;честно радуется, когда ты&nbsp;настоящий.</p></div>
<div class="card">{icon('cups','var(--sage-deep)')}<h3>Свои люди</h3><p>Выпускники дружат домами, делают дела вместе и&nbsp;приводят в&nbsp;школу близких: сарафан у&nbsp;нас главный канал с первого&nbsp;года.</p></div>
</div></div></section>

<section><div class="wrap">
<p class="eyebrow">Живые кадры</p>
<div class="mosaic">
<div class="ph"><img src="/chizhovy2/images/real/real-01.jpg" alt="Группа у камина с сертификатами" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-09.jpg" alt="Участники тренинга" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-12.jpg" alt="Команда на забеге" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-03.jpg" alt="Выпуск группы" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-13.jpg" alt="Финал модуля" loading="lazy"></div>
<div class="ph"><img src="/chizhovy2/images/real/real-08.jpg" alt="Разбор в кругу" loading="lazy"></div>
</div>
<p style="margin-top:26px"><a class="btn btn-ghost" href="/chizhovy2/istorii/">Истории людей с&nbsp;этих фото</a></p>
</div></section>

<section><div class="narrow">
<h2>Что происходит после выпуска</h2>
<p>Формально сопровождение заканчивается через три месяца. Фактически люди остаются рядом: чаты команд живут годами. Один каждое утро продолжает писать намерение, другой собирает своих на&nbsp;пробежку, третий зовёт на&nbsp;день рождения половину группы.</p>
<p>Это не&nbsp;клуб по&nbsp;расписанию, а&nbsp;живая среда. Она держится на&nbsp;простой вещи: люди прошли вместе то, чего обычно не&nbsp;проходят даже с&nbsp;близкими, и&nbsp;после такого общение идёт сразу по&nbsp;сути.</p>
<div class="grid2" style="margin-top:24px">
<div class="card">{icon('speech')}<h3>Разговор без предисловий</h3><p>Не&nbsp;нужно объяснять контекст и&nbsp;подбирать слова: все говорят на&nbsp;одном языке и&nbsp;помнят свою точку&nbsp;А.</p></div>
<div class="card">{icon('people','var(--sage-deep)')}<h3>Поддержка, когда сорвался</h3><p>Когда старая запись берёт своё, рядом есть те, кто это уже проходил и не&nbsp;станет утешать общими словами.</p></div>
<div class="card">{icon('target','var(--sand)')}<h3>Общие дела</h3><p>Совместные проекты, партнёрства, найм внутри среды. Похожие ценности сводят людей&nbsp;быстро.</p></div>
<div class="card">{icon('flame')}<h3>Новые приходят через своих</h3><p>Большинство участников школы пришли по&nbsp;рекомендации выпускников. Это главный канал набора с&nbsp;первого года.</p></div>
</div>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Изнутри</p>
<h2>Что происходит в&nbsp;чате</h2>
<p>На&nbsp;втором модуле группа делится на&nbsp;команды, и&nbsp;каждая берёт себе имя. За&nbsp;последние потоки через школу прошли «Творцы», «Волшебники», «13&nbsp;звёзд» и&nbsp;«МИР». У&nbsp;команды общие цели на&nbsp;три месяца, свой чат и напарник у&nbsp;каждого.</p>
<p>Чат живёт по&nbsp;часам. Утром до&nbsp;десяти каждый пишет намерение на&nbsp;день, вечером до&nbsp;двадцати двух открытия и&nbsp;благодарности. Как только время выходит, появляется строка ведущей: «Спасибо всем, кто вовремя». Если человека второй день не&nbsp;слышно, звучит короткое «Кого&nbsp;потеряли?».</p>
<p>Опоздал один, отметку получают все: «не вовремя как команда». Выглядит строго, работает быстро: за три месяца люди перестают путать «я забыл» и «я подвёл своих». А отвечает опоздавший сам, вслух и тем же вечером.</p>
<p>Ещё команда пишет намерения друг за друга, чаще всего про самочувствие: «Все здоровы», «Семья добралась до дома», «полна сил». В одном чате мы насчитали 256 таких сообщений: взрослые занятые люди держат в голове чужих детей и чужие перелёты, и это довольно быстро меняет их самих.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Один чат</div><div class="big">92 дня</div><p>От&nbsp;первой встречи до&nbsp;выпуска. Мы&nbsp;посчитали: 3115&nbsp;сообщений от&nbsp;двадцати человек, каждый день утром и&nbsp;вечером.</p></div>
<div class="box"><div class="lbl">Кому говорят спасибо</div><div class="big">966</div><p>Столько сообщений в&nbsp;этом чате с&nbsp;благодарностями поимённо: команде, близким, бариста, себе.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Разница</p>
<h2>Чем это отличается от&nbsp;чата выпускников</h2>
<p>Обычный чат после курса живёт мемами и&nbsp;затихает к&nbsp;третьей неделе. Здесь у&nbsp;чата есть дело, и&nbsp;правило звучит прямым текстом. «Если в&nbsp;чате работать не&nbsp;будете, удалю», написала ведущая утром перед модулем. Никто не&nbsp;обиделся: место рабочее, и&nbsp;это понятно на&nbsp;входе.</p>
<p>Когда три месяца заканчиваются, чат закрывают, и&nbsp;последний вечер отдают благодарностям: «Завтра в&nbsp;двадцать два чат закроется. Успейте поблагодарить». Дальше команда остаётся сама, без ведущих, и держится&nbsp;годами.</p>
<p>Как выглядит поддержка, видно по&nbsp;одной ночи. Вечером участница написала две строки: «мои дни рождения стали самыми грустными днями» и&nbsp;«безразличие хуже всего». Ровно в&nbsp;полночь пришёл первый ответ: «Ты чудесная, всё наладится». В&nbsp;двадцать пять минут первого второй: «Так. Давай созвон! С&nbsp;утра прям. Будем возвращать тебя в&nbsp;строй!».</p>
<p>Общие дела начинаются так&nbsp;же буднично. Команды выходят на&nbsp;старты вместе с&nbsp;Алексеем, и в&nbsp;день забега половина людей на&nbsp;дистанции, а&nbsp;намерение за&nbsp;них пишет Ирина. Новые участники приходят через своих: выпускник часто заходит на&nbsp;первый модуль ещё раз, уже рядом с&nbsp;тем, кого привёл. В&nbsp;чате это звучит без пафоса: «Очень круто заходить на&nbsp;первый модуль со&nbsp;своими людьми. Приглашайте, идите с&nbsp;ними».</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Ночью</div><div class="big">00:25</div><p>Время второго ответа на тяжёлое сообщение в чате. Первый пришёл ровно в полночь, и никто об этом не просил.</p></div>
<div class="box"><div class="lbl">Забеги</div><div class="big">половина</div><p>Столько людей из команды вышло на старт в один из ноябрьских забегов. Остальные в то утро писали им в чат «Лёгких ног».</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<p class="eyebrow">Из чего состоит жизнь команды</p>
<h2>Четыре опоры сообщества</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('calendar','var(--copper)')}<h3>Ежедневная перекличка</h3><p>Утреннее намерение и&nbsp;вечерний разбор в&nbsp;общем чате. Не&nbsp;ради отчётности: по&nbsp;этим записям видно, кто выпал и&nbsp;кого пора вытаскивать.</p></div>
<div class="card">{icon('people')}<h3>Разборы с&nbsp;ведущими</h3><p>Раз в&nbsp;неделю вся команда встречается с&nbsp;Алексеем и&nbsp;Ириной. Разбирают конкретные места, где человек откатился в&nbsp;старое.</p></div>
<div class="card">{icon('mountain','var(--sage-deep)')}<h3>Общие затеи</h3><p>Забеги, поездки, совместные проекты. Тело быстро показывает, где человек себя обманывает, и&nbsp;честно радуется, когда он&nbsp;настоящий.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Поддержка ночью</h3><p>Написать в&nbsp;два часа ночи и&nbsp;получить ответ здесь нормально. Это не&nbsp;вежливость, а&nbsp;договорённость команды.</p></div>
</div>
</div></section>

{FINCTA}
""")

# ================= С ЧЕГО НАЧАТЬ =================
P["start/index.html"] = ("С чего начать · Настоящие отношения",
"Маршрут новичка: гайд, собеседование, первый модуль. Три шага для тех, кто решил менять.", "", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/site-hero.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Новичку</p><h1>С чего начать</h1>
<p class="lead">Не&nbsp;нужно сразу решаться на&nbsp;модуль. Вот короткий маршрут. Каждый шаг бесплатный и добровольный, и&nbsp;после каждого становится понятнее.</p></div></div>

<section><div class="narrow">
<div class="card white" style="margin-bottom:12px"><span class="bignum">01</span>{icon('book')}<h3>Прочитай гайд</h3><p>«Кто пишет сценарий твоей&nbsp;жизни»: главное ядро метода в&nbsp;одном выпуске, с&nbsp;самодиагностикой. Полчаса чтения, чтобы примерить механику на&nbsp;себя. <a href="/chizhovy2/gid/">Читать&nbsp;гайд</a></p></div>
<div class="card white" style="margin-bottom:12px"><span class="bignum">02</span>{icon('lens','var(--sage-deep)')}<h3>Осмотрись</h3><p>Как устроен <a href="/chizhovy2/metod/">метод</a> и&nbsp;<a href="/chizhovy2/kak-prohodit/">путь ученика</a>, из&nbsp;чего <a href="/chizhovy2/istoki/">собран подход</a>, что говорят <a href="/chizhovy2/istorii/">люди в&nbsp;историях</a>. Всё открыто, без&nbsp;«узнаете на&nbsp;вебинаре».</p></div>
<div class="card white"><span class="bignum">03</span>{icon('speech','var(--sand)')}<h3>Приходи на&nbsp;собеседование</h3><p>Живой разговор о&nbsp;твоей ситуации: честный взгляд со&nbsp;стороны и&nbsp;понятный следующий шаг. Для&nbsp;читателей сайта бесплатно. <a href="/chizhovy2/sessiya/">Записаться</a></p></div>
<p class="note" style="margin-top:18px">Дальше всё по&nbsp;порядку: <a href="/chizhovy2/programma/">программа из&nbsp;трёх модулей</a>, между ними интеграция, после: Марафон и&nbsp;сообщество.</p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Маршрут&nbsp;подробно</p>
<h2>Сколько занимает каждый шаг и чем&nbsp;заканчивается</h2>
<p>Сверху эти три шага выглядят коротко. Вот что стоит за&nbsp;каждым на&nbsp;самом деле: сколько времени он&nbsp;занимает и с&nbsp;чем ты из него&nbsp;выходишь.</p>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Гайд: полчаса&nbsp;чтения</h3><p>Механика повтора, четыре самых частых записи наших групп и&nbsp;короткий словарь. Заканчивается цифрой: сколько пунктов из&nbsp;десяти в&nbsp;самодиагностике оказались про&nbsp;тебя.</p></div>
<div class="card"><h3>Собеседование: один&nbsp;час</h3><p>Разговор о&nbsp;твоей ситуации, онлайн или очно. Из&nbsp;него выходишь с&nbsp;двумя вещами: свой круг видно со&nbsp;стороны, и&nbsp;понятно, чем школа может помочь именно&nbsp;тебе.</p></div>
<div class="card"><h3>Первый модуль: два с половиной&nbsp;дня</h3><p>Пятничный вечер и&nbsp;выходные, в&nbsp;зале от&nbsp;десяти до&nbsp;двадцати человек. К&nbsp;последнему дню ты&nbsp;видишь свою запись целиком и&nbsp;понимаешь, в&nbsp;каком возрасте она&nbsp;появилась.</p></div>
<div class="card"><h3>Пауза: три-пять&nbsp;недель</h3><p>Перерыв между модулями сделан нарочно: увиденное должно осесть в&nbsp;обычной жизни, среди тех&nbsp;же людей и тех&nbsp;же дел. Дальше пять дней второго модуля и&nbsp;три месяца&nbsp;Марафона.</p></div>
</div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Фора&nbsp;записи</div><div class="big">12 мс</div><p>За&nbsp;столько сигнал доходит до&nbsp;миндалины, аварийного центра мозга. Думающая кора получает его позже (ЛеДу). Столько времени у&nbsp;старой записи, чтобы успеть раньше&nbsp;тебя.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Без&nbsp;сроков</p>
<h2>Как понять, что пора на следующий&nbsp;шаг</h2>
<p>Мы&nbsp;никого не&nbsp;торопим. Один читает гайд за&nbsp;вечер и&nbsp;пишет в ту&nbsp;же ночь, другой возвращается на&nbsp;сайт через полгода. Оба варианта рабочие. Есть простые признаки, по&nbsp;которым видно, что шаг&nbsp;созрел.</p>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>После&nbsp;гайда</h3><p>В&nbsp;самодиагностике набралось три пункта и&nbsp;больше. Дома ловишь себя на&nbsp;том, что называешь свои сцены словами гайда. Вопрос поменялся: раньше было «работает ли это вообще», стало «как это выглядит в моём&nbsp;случае».</p></div>
<div class="card"><h3>После&nbsp;разговора</h3><p>Понятно, с&nbsp;какого модуля заходить и&nbsp;какие даты держать в&nbsp;календаре. Внутри стало спокойнее: спор с&nbsp;собой закончился, осталось решение и&nbsp;дата.</p></div>
<div class="card"><h3>Что чаще всего&nbsp;останавливает</h3><p>Расписание. Два с&nbsp;половиной дня и&nbsp;пять дней трудно вынуть из&nbsp;года. На&nbsp;собеседовании мы&nbsp;задаём встречный вопрос: сколько времени уже съел повторяющийся круг. Счёт обычно идёт на&nbsp;годы.</p></div>
<div class="card"><h3>Если решение пока не&nbsp;складывается</h3><p>Восемь самых частых сомнений разобраны начистоту на&nbsp;<a href="/chizhovy2/somneniya/">отдельной странице</a>: от&nbsp;недоверия к&nbsp;тренингам до&nbsp;страха групповой работы. Своё сомнение можно принести и на&nbsp;встречу.</p></div>
</div>
</div>
<aside class="side">
<div class="box"><div class="lbl">С чем приходят</div><p>С&nbsp;решением что-то менять. Разговор нужен тому, кто уже дозрел, а&nbsp;не&nbsp;тому, кто зашёл посмотреть.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Тихий&nbsp;вариант</p>
<h2>Если писать и говорить пока не&nbsp;хочется</h2>
<p>Тогда читай. Метод выложен на&nbsp;сайте целиком, до&nbsp;последнего инструмента: мы&nbsp;ничего не&nbsp;оставляем «на узнаете в&nbsp;зале». Порядок для тех, кто заходит с холодной&nbsp;головой:</p>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Язык&nbsp;школы</h3><p><a href="/chizhovy2/slovar/">Словарь</a> из&nbsp;четырнадцати слов: точка&nbsp;А, старая запись, важность, вклад. Короткие слова, за&nbsp;которыми стоят большие механизмы.</p></div>
<div class="card"><h3>Инструменты&nbsp;зала</h3><p><a href="/chizhovy2/tehniki-sceny/">Техники сцены</a>: обмен ролями, дублирование, зеркало, пустой стул. И&nbsp;одна сцена, разобранная от&nbsp;запроса до возвращения в&nbsp;день.</p></div>
<div class="card"><h3>Откуда всё&nbsp;это</h3><p><a href="/chizhovy2/istoki/">Пять источников метода</a> названы открыто, вместе с&nbsp;<a href="/chizhovy2/istoki/nauka/">наукой</a>, на&nbsp;которую опираются: ЛеДу, Гоулман, Болте&nbsp;Тейлор.</p></div>
<div class="card"><h3>Правила и&nbsp;границы</h3><p><a href="/chizhovy2/bezopasnost/">Договорённости зала</a> целиком: конфиденциальность, право сказать «стоп» в&nbsp;любой момент, кому школа сейчас не&nbsp;подойдёт.</p></div>
</div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Открыто</div><div class="big">5 истоков</div><p>Морено и&nbsp;психодрама, трансерфинг, тренинг est и&nbsp;«Трансформация», Годдард, наука. Каждый разобран отдельной страницей.</p></div>
</aside>
</div></div></section>





<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-start.jpg" alt="Отсюда начинают все" loading="lazy"></div>
<div>
<p class="eyebrow">Первый шаг</p>
<h2 style="font-size:1.9rem">Отсюда начинают все</h2>
<p>Три ступени, но&nbsp;идти сразу на&nbsp;модуль не&nbsp;нужно. Сначала разговор, потом решение.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Маршрут целиком</p>
<h2>Три шага и&nbsp;что даёт каждый</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('book','var(--copper)')}<h3>1 · Гайд</h3><p>Полчаса чтения. Разбор механики повтора и&nbsp;самопроверка: сколько пунктов про тебя. После него становится понятно, о&nbsp;чём вообще речь.</p></div>
<div class="card">{icon('speech')}<h3>2 · Собеседование</h3><p>Живой разговор о&nbsp;твоей ситуации. Смотрим, наша&nbsp;ли это задача, и&nbsp;отвечаем на&nbsp;вопросы прямо, включая неудобные.</p></div>
<div class="card">{icon('mountain','var(--sage-deep)')}<h3>3 · Первый модуль</h3><p>2,5&nbsp;дня очно в&nbsp;малой группе. Дальше решение принимается заново: никто не&nbsp;обязан идти во&nbsp;второй.</p></div>
</div>
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
<div class="card white">{icon('speech')}<h3>Telegram</h3><p>Канал школы: анонсы наборов, живые тексты пары, ответы на&nbsp;вопросы. Там&nbsp;же видно, как мы&nbsp;говорим и о&nbsp;чём думаем, задолго до&nbsp;всякого собеседования: самый простой способ понять, свои мы&nbsp;люди или&nbsp;нет.</p><p style="margin-top:12px"><a href="https://t.me/+LVptSH6Mt4hhYmFi">Открыть Telegram</a></p></div>
<div class="card white">{icon('calendar','var(--sage-deep)')}<h3>Собеседование</h3><p>Разговор о&nbsp;твоей ситуации, онлайн или очно. Для читателей сайта&nbsp;бесплатно.</p><p style="margin-top:12px"><a href="/chizhovy2/sessiya/">Записаться</a></p></div>
</div>
<p class="note" style="margin-top:20px">Реквизиты и&nbsp;документы для оплаты появятся здесь вместе с&nbsp;онлайн-оплатой.</p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Первое&nbsp;сообщение</p>
<h2>Что написать, чтобы разговор начался&nbsp;быстрее</h2>
<p>Хватит одного слова: «собеседование». По&nbsp;нему мы&nbsp;поймём, зачем ты&nbsp;пишешь, и&nbsp;сразу предложим время. Если хочется к&nbsp;делу, добавь три вещи: что происходит сейчас, сколько это уже длится и&nbsp;как тебе удобнее говорить, онлайн или очно. Красивых формулировок не&nbsp;нужно: мы&nbsp;читаем не&nbsp;стиль, а&nbsp;ситуацию.</p>
<p>Дальше короткая переписка про время, и&nbsp;всё. Никаких анкет, опросников и&nbsp;автоматических приветствий: ответ пишет живой человек. Днём в&nbsp;зале идут группы, поэтому сообщение может полежать несколько часов и&nbsp;получить ответ вечером. Телефоны на&nbsp;время работы группы лежат в&nbsp;стороне, это правило зала, и на&nbsp;ведущих оно распространяется&nbsp;тоже.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Первый&nbsp;шаг</div><div class="big">Собеседование</div><p>Одно слово в&nbsp;Telegram, и мы&nbsp;согласуем время. Для читателей сайта бесплатно.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">По&nbsp;шагам</p>
<h2>Что происходит после твоего&nbsp;сообщения</h2>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Согласуем&nbsp;время</h3><p>Спросим город и&nbsp;часовой пояс, предложим свободные окна на&nbsp;ближайшие дни. Если удобнее очно, скажем, когда ведущие будут в твоём&nbsp;городе.</p></div>
<div class="card"><h3>Говорим&nbsp;час</h3><p>О&nbsp;твоей ситуации, о&nbsp;том, что уже пробовал и к&nbsp;чему хочешь прийти. Как проходит этот час, расписано на&nbsp;странице&nbsp;<a href="/chizhovy2/sessiya/">собеседования</a>.</p></div>
<div class="card"><h3>Решаем&nbsp;вдвоём</h3><p>Годится ли тебе школа и с&nbsp;какого модуля заходить. Условия обсуждаем там&nbsp;же, спокойно. Думать после разговора можно сколько&nbsp;угодно.</p></div>
<div class="card"><h3>Кто с тобой&nbsp;говорит</h3><p>Один из&nbsp;ведущих: тот самый человек, который потом будет стоять рядом с&nbsp;тобой в&nbsp;зале. Скриптов и&nbsp;менеджеров по&nbsp;продажам у школы&nbsp;нет.</p></div>
</div>
<p style="margin-top:22px">Личные ситуации в&nbsp;переписке мы не&nbsp;разбираем. В&nbsp;чате видны только слова, а&nbsp;работа держится на&nbsp;голосе: где человек запнулся, о&nbsp;чём сказал вскользь, после какого вопроса стало трудно говорить. Живой разговор даёт больше, чем месяц сообщений, поэтому мы&nbsp;сразу зовём&nbsp;говорить.</p>
<p>Если сейчас тяжело настолько, что нужна помощь врача, скажем об&nbsp;этом прямо и&nbsp;подскажем, куда смотреть. Погружение требует сил, и в&nbsp;остром состоянии оно скорее нагрузит. Границы работы описаны&nbsp;на&nbsp;<a href="/chizhovy2/bezopasnost/">отдельной&nbsp;странице</a>.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Разговор</div><div class="big">60 минут</div><p>Онлайн или очно. Обязательств после него ноль: решение принимаешь потом и&nbsp;сам.</p></div>
<div class="box"><div class="lbl">Набор</div><div class="big">10-20</div><p>Столько человек в&nbsp;группе. Школа растёт через рекомендации, поэтому места расходятся тихо и&nbsp;заранее.</p></div>
</aside>
</div></div></section>


<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Прежде чем писать</p>
<h2>Что полезно знать заранее</h2>
<p>Мы&nbsp;не&nbsp;консультируем в&nbsp;переписке. Разобрать ситуацию в&nbsp;сообщениях невозможно: нужен живой разговор, где слышно интонацию и&nbsp;видно, где человек замолкает. Поэтому на&nbsp;длинное письмо ответим коротко и&nbsp;предложим созвон.</p>
<p>Отвечают Алексей и&nbsp;Ирина, не&nbsp;администратор. Если ведём модуль, сообщение может полежать несколько часов: в&nbsp;зале телефоны выключены у&nbsp;всех, включая нас.</p>
<h3>Что написать в&nbsp;первом сообщении</h3>
<p>Достаточно одной фразы о&nbsp;том, что беспокоит, и&nbsp;слова «собеседование». Формулировать красиво не&nbsp;нужно, разберёмся вместе. Если удобнее говорить голосом, так и&nbsp;напиши, перезвоним.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Отвечаем</div><p>В&nbsp;течение дня, обычно быстрее. Вечером и&nbsp;в&nbsp;выходные тоже читаем.</p></div>
<div class="box"><div class="lbl">Не&nbsp;делаем</div><p>Не&nbsp;консультируем в&nbsp;переписке и&nbsp;не&nbsp;ставим диагнозов по&nbsp;сообщению.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/p-kontakty.jpg" alt="Пиши, как удобно" loading="lazy"></div>
<div>
<p class="eyebrow">Как связаться</p>
<h2 style="font-size:1.9rem">Пиши, как удобно</h2>
<p>Телефон, мессенджер, почта: подойдёт любой канал. Отвечают Алексей и&nbsp;Ирина, а&nbsp;не&nbsp;администратор, поэтому иногда с&nbsp;задержкой в&nbsp;пару часов.</p>
</div>
</div>
</div></section>


<section><div class="wrap">
<p class="eyebrow">Как проще связаться</p>
<h2>Три канала, любой рабочий</h2>
<div class="grid3" style="margin-top:30px">
<div class="card">{icon('speech','var(--copper)')}<h3>Telegram</h3><p>Самый быстрый способ. Напиши слово «собеседование» и&nbsp;пару строк о&nbsp;том, что беспокоит. Отвечаем в&nbsp;течение дня.</p></div>
<div class="card">{icon('people')}<h3>Канал школы</h3><p>Анонсы наборов, разборы и&nbsp;живые истории. Там видно, как школа разговаривает, ещё до&nbsp;личного знакомства.</p></div>
<div class="card">{icon('calendar','var(--sage-deep)')}<h3>Созвон</h3><p>Если писать неудобно, скажи об&nbsp;этом, и&nbsp;мы&nbsp;согласуем время для&nbsp;разговора голосом.</p></div>
</div>
</div></section>

{FINCTA}
""")

# ================= ТЕХНИКИ СЦЕНЫ =================
P["tehniki-sceny/index.html"] = ("Техники сцены · Настоящие отношения",
"Обмен ролями, дублирование, зеркало, пустой стул: инструменты живой сцены с разбором.", "metod", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/metod-stul.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Инструменты в зале</p><h1>Техники живой сцены</h1>
<p class="lead">Со&nbsp;стороны сцена похожа на&nbsp;театр без сценария. На&nbsp;самом деле всё устроено точно: вот инструменты, которыми ведущие меняют старую запись, и&nbsp;вот что&nbsp;делает каждый.</p></div></div>

<section><div class="narrow">
<div class="card white" style="margin-bottom:12px">{icon('people')}<h3>Обмен ролями</h3><p>Встаёшь на&nbsp;место другого человека из&nbsp;своей сцены и&nbsp;отвечаешь себе его словами. Пять минут в&nbsp;чужой роли показывают то, что годами не&nbsp;видно из&nbsp;своей: почему он&nbsp;молчит, чего она боится, что на&nbsp;самом деле стоит за&nbsp;фразой, которая тебя ранит.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('speech','var(--sage-deep)')}<h3>Дублирование</h3><p>Человек из&nbsp;группы становится рядом и&nbsp;договаривает то, что ты&nbsp;чувствуешь, но не&nbsp;решаешься произнести. Когда невысказанное впервые звучит вслух, тело отзывается сразу. Значит,&nbsp;попали.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('mirror','var(--sand)')}<h3>Зеркало</h3><p>Выходишь из&nbsp;собственной сцены и&nbsp;смотришь её со&nbsp;стороны, как зритель. Так впервые видно сценарий целиком: где включилась старая запись, в&nbsp;какой момент финал стал предрешён и&nbsp;что каждый из&nbsp;участников делал, чтобы всё закончилось именно&nbsp;так.</p></div>
<div class="card white" style="margin-bottom:12px">{icon('cups')}<h3>Пустой стул</h3><p>Напротив ставится стул, и на&nbsp;нём «сидит» тот, с&nbsp;кем так и не&nbsp;поговорили: отец, бывший, ты&nbsp;сам из&nbsp;прошлого. Отложенный на&nbsp;годы разговор происходит здесь, и у&nbsp;него наконец появляется финал.</p></div>
<div class="card white">{icon('sunrise','var(--sage-deep)')}<h3>Новое решение</h3><p>Кульминация сцены: там, где когда-то был сделан старый выбор, ты&nbsp;делаешь другой. Новое пишется так&nbsp;же глубоко, как прежнее, телом и&nbsp;эмоцией. Поэтому и&nbsp;держится.</p></div>
<p style="margin-top:22px">Откуда эти инструменты и&nbsp;почему им&nbsp;сто лет: <a href="/chizhovy2/istoki/moreno-psihodrama/">Морено и&nbsp;психодрама</a>. Как сцена встроена в&nbsp;общую работу: <a href="/chizhovy2/metod/">метод целиком</a>.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Как это выглядит</p>
<h2>Одна сцена от&nbsp;начала до&nbsp;конца</h2>
<p class="sub">Условный случай, собранный из&nbsp;типичных ситуаций зала. Живые сцены идут по-разному, но&nbsp;порядок примерно такой.</p>
<div class="grid3" style="margin-top:26px">
<div class="card"><span class="bignum">1</span><h3>Запрос</h3><p>Мужчина говорит: с&nbsp;отцом двадцать лет холодно, разговора не&nbsp;выходит. Обозначаем сцену: кухня родительской квартиры, ему пятнадцать.</p></div>
<div class="card"><span class="bignum">2</span><h3>Разогрев</h3><p>Участник группы становится отцом, ещё один занимает место самого героя. Обстановка собирается из&nbsp;деталей: где стоял стол, кто где сидел.</p></div>
<div class="card"><span class="bignum">3</span><h3>Действие</h3><p>Звучит то, что тогда осталось внутри. Тело включается раньше слов: голос садится, руки дрожат, это нормальный ход процесса.</p></div>
<div class="card"><span class="bignum">4</span><h3>Обмен ролями</h3><p>Он встаёт на&nbsp;место отца и&nbsp;отвечает себе его словами. Часто именно тут впервые становится видно, что отец тоже не&nbsp;умел иначе.</p></div>
<div class="card"><span class="bignum">5</span><h3>Новое решение</h3><p>В точке, где когда-то было принято «своих чувств не&nbsp;показывать», принимается другое. Ведущий помогает произнести его вслух.</p></div>
<div class="card linen"><span class="bignum">6</span><h3>Возвращение</h3><p>Группа делится тем, что откликнулось в их&nbsp;историях. Герой выходит из&nbsp;роли и&nbsp;возвращается в&nbsp;сегодняшний день.</p></div>
</div>
<p class="note" style="margin-top:20px">Кто отвечает за&nbsp;безопасность процесса, описано на&nbsp;странице <a href="/chizhovy2/bezopasnost/">границ работы</a>.</p>
</div></section>

<section><div class="wrap">
<p class="eyebrow">Кто где стоит</p>
<h2>Роли в&nbsp;сцене</h2>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('target','var(--copper)')}<h3>Герой</h3><p>Тот, чью ситуацию разбирают. Он&nbsp;выбирает эпизод, расставляет людей и&nbsp;в&nbsp;конце принимает другое решение.</p></div>
<div class="card">{icon('people')}<h3>Участники в&nbsp;ролях</h3><p>Встают на&nbsp;места людей из&nbsp;сцены и&nbsp;говорят их&nbsp;словами. Ничего не&nbsp;играют: повторяют то, что описал герой.</p></div>
<div class="card">{icon('mountain','var(--sage-deep)')}<h3>Ведущий, который держит</h3><p>Следит за&nbsp;порядком и&nbsp;временем, останавливает, когда пора, и&nbsp;не&nbsp;даёт залу свалиться в&nbsp;советы.</p></div>
<div class="card">{icon('flame','var(--sand)')}<h3>Ведущая, которая ведёт вглубь</h3><p>Чувствует, где живое, и&nbsp;идёт туда. Остаётся рядом с&nbsp;человеком до&nbsp;конца процесса.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Ещё инструменты</p>
<h2>Чем работают, кроме&nbsp;сцены</h2>
<div class="card white" style="margin-bottom:12px"><h3>Расстановка</h3><p>Цель и всё, что стоит вокруг неё, человек собирает из живых людей: себя, дело, партнёра, страх, деньги. Потом отходит и смотрит со стороны. Видно быстро: кто кому загораживает дорогу и почему цель третий год на том же месте. Намерение перед этим днём участник записывает так: «помочь команде в расстановках, быть честным и открытым на своей».</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Работа с&nbsp;образами</h3><p>У&nbsp;каждого внутри живут несколько фигур, снятых с&nbsp;близких: мать, отец, бабушка, первая учительница. В&nbsp;зале их&nbsp;достают по&nbsp;одной и&nbsp;сверяют с&nbsp;тем, как человек живёт сегодня. «Даже подумать не&nbsp;могла, что копирую её&nbsp;мир полностью», написала участница про бабушку. Другой в тот&nbsp;же вечер: «Очень был удивлён, что все образы точно совпали с неработающими&nbsp;стратегиями».</p></div>
<div class="card white" style="margin-bottom:12px"><h3>Разрушение клятв</h3><p>Такое обещание человек даёт себе однажды и держит десятилетиями. «Нашла клятву: больно будет всегда, это никогда не закончится», записала участница второго модуля. В работе находят первопричину, отпускают обещание и сразу ставят на его место новое решение. Иначе туда возвращается старое.</p></div>
<div class="card white"><h3>Вопрос про цель</h3><p>Короткий инструмент на&nbsp;каждый день. В&nbsp;середине спора человек спрашивает себя: какая у&nbsp;меня здесь цель. Правота отваливается почти сразу. Доказать и&nbsp;договориться это разные задачи. Формулировка группы звучит так: «Уходим из&nbsp;правоты, задавая вопрос „какая&nbsp;цель?“».</p></div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Что она показывает</div><p>Ту часть картины, которую из своей роли не разглядеть. Люди в ролях делают её видимой за минуты.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Роли в&nbsp;зале</p>
<h2>Кто что делает, пока идёт&nbsp;сцена</h2>
<p>Герой называет ситуацию и&nbsp;входит в&nbsp;неё. Он&nbsp;задаёт обстановку, выбирает, кто кого играет, и&nbsp;может остановить работу в&nbsp;любую минуту. Темп держит он.</p>
<p>Ведущих двое. Один ведёт процесс и&nbsp;видит карту целиком. Вторая чувствует состояние человека раньше слов и&nbsp;идёт туда, где живое. Поэтому в&nbsp;тяжёлом месте рядом всегда есть тот, кто смотрит на&nbsp;происходящее со&nbsp;стороны.</p>
<p>Участники в&nbsp;ролях говорят словами героя, а не&nbsp;своими. Задача одна: вернуть ту самую интонацию, от&nbsp;которой в&nbsp;груди становится тесно. Дублёр встаёт рядом и&nbsp;договаривает вслух то, что герой чувствует и&nbsp;произнести пока не&nbsp;может.</p>
<p>Остальные держат тишину. В&nbsp;конце круг говорит, что откликнулось в их&nbsp;собственных историях. Советы и&nbsp;оценки сюда не&nbsp;берут: работает узнавание, а&nbsp;чужая инструкция только выбивает из&nbsp;состояния. За 16&nbsp;лет через такую работу прошли десятки групп по 10-20&nbsp;человек.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Ведущих</div><div class="big">2</div><p>Одному такое не&nbsp;удержать: пока первый ведёт процесс, вторая остаётся рядом с человеком до&nbsp;конца.</p></div>
</aside>
</div></div></section>


<section><div class="wrap">
<div class="split">
<div class="ph"><img src="/chizhovy2/images/ob-krug-sverhu.jpg" alt="Круг стульев сверху" loading="lazy"></div>
<div>
<p class="eyebrow">Где это происходит</p>
<h2 style="font-size:1.9rem">Как устроен зал</h2>
<p>Ни&nbsp;сцены, ни&nbsp;рядов, ни&nbsp;кафедры. Стулья по&nbsp;кругу, свободная середина и&nbsp;двое ведущих. Всё, что описано выше, разворачивается вот в&nbsp;таком зале, за&nbsp;несколько шагов от&nbsp;остальных участников.</p>
</div>
</div>
</div></section>







{FINCTA}
""")

# ================= ТРИ СОМНЕНИЯ =================
P["somneniya/index.html"] = ("Частые сомнения · Настоящие отношения",
"«Не верю, что поможет», «боюсь группы», «нет времени», «а вдруг станет хуже»: восемь честных разборов перед решением.", "somneniya", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/somneniya-hero.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Перед решением</p><h1>Сомнения перед первым шагом</h1>
<p class="lead">Мы&nbsp;слышим их на&nbsp;каждом собеседовании и&nbsp;считаем хорошим знаком: сомневается тот, кто относится к&nbsp;делу серьёзно. Ниже восемь самых частых. Разбираем каждое начистоту, и&nbsp;если ты&nbsp;прав в&nbsp;своих опасениях, так&nbsp;и скажем.</p></div></div>

<section style="padding-bottom:40px"><div class="wrap">
<p class="eyebrow">Коротко</p>
<h2>О чём чаще всего думают</h2>
<div class="chiplist" style="margin-top:18px">
<span>Не&nbsp;верю, что поможет</span><span>У&nbsp;меня особый случай</span><span>Уже был у&nbsp;психолога</span><span>Боюсь группы</span><span>Нет времени</span><span>А вдруг станет хуже</span><span>Эффект пройдёт через неделю</span><span>Мужчине такое не&nbsp;нужно</span>
</div>
</div></section>

<section><div class="narrow">
<h2>1. «Просто не&nbsp;верю, что поможет»</h2>
<p>Самое прямое из&nbsp;всех, и мы&nbsp;его уважаем. Рынок тренингов приучил людей к&nbsp;обещаниям, после которых ничего не&nbsp;меняется. Недоверие тут здоровая реакция психики, признак осторожности, которая не&nbsp;раз тебя спасала.</p>
<p>Единственный честный ответ: проверяемость. Мы&nbsp;открыто показываем, <a href="/chizhovy2/istoki/">из&nbsp;чего собран метод</a> и на&nbsp;какой <a href="/chizhovy2/istoki/nauka/">науке</a> он&nbsp;стоит, публикуем <a href="/chizhovy2/istorii/">истории учеников</a> без глянца и не&nbsp;обещаем гарантированных перемен. Первый шаг ни к&nbsp;чему не&nbsp;обязывает: разговор, после которого ты&nbsp;решаешь сам.</p>
<div class="pull"><div class="q">«Что останавливало? Просто недоверие, что поможет.»</div><div class="who">Ученик, который пришёл в&nbsp;кризисе и&nbsp;остался на&nbsp;все три модуля</div></div>

<h2 style="margin-top:36px">2. «У&nbsp;меня особый случай»</h2>
<p>Отчасти правда. Биографии у&nbsp;всех разные, и на&nbsp;сцене твоя разбирается индивидуально, без единого шаблона. Но&nbsp;механика повтора у&nbsp;людей общая: событие, эмоция, старое решение, знакомый финал. Поэтому в&nbsp;чужой истории на&nbsp;группе ты&nbsp;так часто узнаёшь свою: случаи особые, а&nbsp;<a href="/chizhovy2/metod/">круг один</a>.</p>
<p>За шестнадцать лет через зал прошли предприниматели после банкротства, пары на&nbsp;грани развода, руководители в&nbsp;выгорании, женщины, которые годами не&nbsp;слышали себя. Каждый заходил со&nbsp;словами «у&nbsp;меня всё сложнее». И&nbsp;все находили свою запись.</p>

<h2 style="margin-top:36px">3. «Я уже был у&nbsp;психолога»</h2>
<p>И&nbsp;это хорошо. Терапия и&nbsp;тренинг не&nbsp;соперники. Кабинетный формат идёт словами, по&nbsp;часу в&nbsp;неделю. Понимание он&nbsp;собирает отлично. Здесь всё держится на&nbsp;теле и&nbsp;эмоции, в&nbsp;живой сцене, в&nbsp;погружении на&nbsp;несколько дней: другой инструмент для другого слоя.</p>
<p>То, что ты&nbsp;накопил у&nbsp;психолога, здесь превращается в&nbsp;пережитый опыт. Многие наши ученики продолжают терапию параллельно. Мы это&nbsp;поддерживаем.</p>
</div></section>

<section style="padding:0"><div class="wrap">
<div class="ph" style="aspect-ratio:16/7"><img src="/chizhovy2/images/somneniya-gruppa.jpg" alt="Круг участников в зале тренинга" loading="lazy"></div>
</div></section>

<section><div class="narrow">
<h2>4. «Боюсь группы. Придётся раскрываться перед чужими»</h2>
<p>Звучит чаще остальных, и&nbsp;по-человечески понятно. Правда такая: глубина всегда добровольна, никто не&nbsp;вытаскивает силой, темп выбираешь ты. Можно первый день просто смотреть.</p>
<p>Обычно уже к&nbsp;вечеру первого дня чужих в&nbsp;зале не&nbsp;остаётся: у&nbsp;людей одинаковые боли, и&nbsp;это выясняется быстро. А&nbsp;ещё именно группа делает работу такой сильной: <a href="/chizhovy2/tehniki-sceny/">сцене нужны люди</a>, чужая история включает твою, и&nbsp;поддержка держит там, где одному тяжело. Все рамки описаны на&nbsp;странице <a href="/chizhovy2/bezopasnost/">безопасности</a>: личное остаётся в&nbsp;зале.</p>

<h2 style="margin-top:36px">5. «Нет времени: работа, дети, проекты»</h2>
<p>Его действительно нужно немало: два с&nbsp;половиной дня на&nbsp;первом модуле, пять дней на&nbsp;втором, дальше три месяца практики внутри обычной жизни. Мы не&nbsp;делаем вид, что это можно пройти между делом.</p>
<p>Встречный вопрос, который мы&nbsp;задаём на&nbsp;собеседовании: сколько времени уже съел повторяющийся круг? Ссоры по&nbsp;одному сценарию, решения, отложенные на&nbsp;годы, вечера в&nbsp;тяжёлом состоянии. Обычно счёт идёт не на&nbsp;дни, а на&nbsp;годы, и на&nbsp;этом фоне неделя погружения выглядит иначе.</p>

<h2 style="margin-top:36px">6. «А вдруг станет хуже: разведусь, поссорюсь, всё развалится»</h2>
<p>Страх понятный, и&nbsp;основание у&nbsp;него есть. Когда человек выходит из&nbsp;привычной роли, отношения вокруг перестраиваются. Но&nbsp;направление перемен задаёшь ты, а не&nbsp;тренинг. Мы не&nbsp;ведём к&nbsp;решениям «уходи» или «оставайся»: мы&nbsp;возвращаем способность видеть ситуацию ясно и&nbsp;выбирать спокойно.</p>
<p>По опыту групп чаще происходит обратное. То, что держалось на&nbsp;тяжёлом молчании, оживает. Пары нередко приходят вторым заходом уже <a href="/chizhovy2/para/">вдвоём</a>, потому что одному из&nbsp;двоих стало тесно молчать.</p>
</div></section>

<section style="padding:0"><div class="wrap">
<div class="ph" style="aspect-ratio:16/7"><img src="/chizhovy2/images/somneniya-nedoverie.jpg" alt="Мужчина у окна утром, решение принимается" style="object-position:center 8%" loading="lazy"></div>
</div></section>

<section><div class="narrow">
<h2>7. «Уже пробовал тренинги. Эффект держался неделю»</h2>
<p>Знакомо, и&nbsp;причина обычно одна: работа шла на&nbsp;верхнем этаже. Вдохновение, конспект, новые слова, а&nbsp;запись осталась там&nbsp;же, где была, в&nbsp;эмоции и&nbsp;теле. Первый стресс возвращает старую реакцию, и&nbsp;человек решает, что дело в&nbsp;нём.</p>
<p>Поэтому у&nbsp;нас формат длинный: погружение, недели на проверку в жизни между модулями и&nbsp;три месяца сопровождения. За&nbsp;девяносто дней новое поведение перестаёт быть праздничным и&nbsp;становится обычным. Как это выглядит день за&nbsp;днём: <a href="/chizhovy2/praktiki/">ежедневные практики</a> и&nbsp;<a href="/chizhovy2/istorii/komanda-mir/">история команды «МИР»</a>.</p>

<h2 style="margin-top:36px">8. «Мужчине такое не&nbsp;нужно»</h2>
<p>В зале примерно поровну тех и&nbsp;других. Мужская часть обычно упрямее всех на&nbsp;входе и&nbsp;благодарнее всех на&nbsp;выходе. Приходят за&nbsp;ясностью в&nbsp;решениях, за&nbsp;потолком в&nbsp;деле, за&nbsp;отношениями, которые перестали работать.</p>
<p>Школу ведёт пара. Алексей говорит на&nbsp;понятном языке: структура, дисциплина, дистанция, результат. <a href="/chizhovy2/dlya-predprinimatelej/">Отдельная страница для тех, кто привык тащить сам</a>.</p>
<div class="pull"><div class="q">«На тренинге я&nbsp;долго сопротивлялся, как баран. Труднее всего было принять точку&nbsp;А.»</div><div class="who">Из истории ученика-предпринимателя</div></div>
</div></section>

<section class="dark"><div class="wrap">
<p class="eyebrow">Честно</p>
<h2>Когда мы говорим «не сейчас»</h2>
<p class="lead" style="color:rgba(242,237,228,.75)">Бывают ситуации, когда правильный ответ «не&nbsp;сейчас» или «не&nbsp;сюда». Мы&nbsp;говорим об&nbsp;этом прямо на&nbsp;собеседовании и не&nbsp;берём человека ради заполненной группы.</p>
<div class="grid3" style="margin-top:24px">
<div class="card">{icon('shield','var(--copper)')}<h3>Нужна медицинская помощь</h3><p>Острое состояние, психиатрический диагноз в&nbsp;обострении: тренинг не&nbsp;заменяет врача. Подскажем, куда идти.</p></div>
<div class="card">{icon('calendar','var(--copper)')}<h3>Нет сил именно сейчас</h3><p>Переезд, роды, похороны, аврал на&nbsp;работе. Погружение требует сил, лучше прийти через полгода в&nbsp;своём темпе.</p></div>
<div class="card">{icon('target','var(--copper)')}<h3>Ищешь быстрый рецепт</h3><p>Если нужен готовый скрипт «как заставить его измениться», мы не&nbsp;поможем: работа идёт с&nbsp;тем, кто пришёл.</p></div>
</div>
<p style="margin-top:24px"><a class="btn btn-ghost" href="/chizhovy2/bezopasnost/">Все границы работы</a></p>
</div></section>

<section><div class="narrow">
<h2>Где всё это можно спросить вслух</h2>
<p>Собеседование и&nbsp;существует для сомнений. Живой разговор: ты&nbsp;рассказываешь свою ситуацию, мы&nbsp;разбираем механику и&nbsp;честно говорим, поможет&nbsp;ли здесь школа. Отговорить можем так&nbsp;же спокойно, как&nbsp;пригласить.</p>
<div class="nails nails3" style="margin-top:22px">
<div class="nail"><b>60&nbsp;минут</b><span>онлайн или очно, без подготовки и правильных&nbsp;слов</span></div>
<div class="nail"><b>Бесплатно</b><span>для тех, кто пришёл с этого&nbsp;сайта</span></div>
<div class="nail"><b>1</b><span>честный разговор о&nbsp;твоей&nbsp;задаче</span></div>
</div>
<p style="margin-top:24px">Осталось сомнение, которого здесь нет? Принеси его на&nbsp;разговор: это ровно то&nbsp;место, где на&nbsp;него ответят прямо. Что ещё спрашивают о&nbsp;формате, собрано в&nbsp;разделе <a href="/chizhovy2/voprosy/">вопросов и&nbsp;ответов</a>.</p>
</div></section>

<section style="padding:0"><div class="wrap">
<div class="ph" style="aspect-ratio:16/7"><img src="/chizhovy2/images/somneniya-posle.jpg" alt="Осенняя дорожка в парке на закате" loading="lazy"></div>
</div></section>
{FINCTA}
""")

# ================= СТАТЬИ (ХАБ) =================
P["stati/index.html"] = ("Статьи школы · Настоящие отношения",
"Библиотека школы: разборы про отношения, состояние, сценарии, трансерфинг и психодраму языком метода.", "stati", f"""
<div class="hero short"><div class="bg" style="background-image:url('/chizhovy2/images/stati-hero.jpg')"></div><div class="veil"></div>
<div class="in"><p class="eyebrow">Библиотека школы</p><h1 style="font-size:clamp(1.75rem,5.5vw,3.7rem)">Статьи школы</h1>
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

<section><div class="narrow">
<h2>Пока библиотека растёт</h2>
<p class="sub" style="margin:0 0 26px">Главное ядро школы уже собрано в&nbsp;бесплатном гайде «Кто пишет сценарий твоей&nbsp;жизни». Полчаса чтения. А&nbsp;живые вопросы можно принести на&nbsp;собеседование: для&nbsp;читателей сайта оно бесплатное.</p>
<p class="btns"><a class="btn btn-wine" href="/chizhovy2/gid/">Читать гайд</a> <a class="btn btn-ghost" href="/chizhovy2/sessiya/" style="margin-left:8px">Записаться на&nbsp;собеседование</a></p>
</div></section>
<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Живой&nbsp;спрос</p>
<h2>На какие вопросы ответят статьи</h2>
<p>Темы мы не&nbsp;придумывали за&nbsp;столом. Двадцать шесть разборов собраны из&nbsp;того, что люди приносят на&nbsp;собеседования и в&nbsp;зал год за&nbsp;годом. Вот вопросы, которые звучат чаще&nbsp;всего.</p>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Почему ссора идёт по&nbsp;кругу</h3><p>Реплики повторяются почти дословно, повод каждый раз новый, финал один. Разберём, что запускает сцену и в&nbsp;какой момент её&nbsp;ещё можно остановить.</p></div>
<div class="card"><h3>Сил нет, хотя снаружи&nbsp;порядок</h3><p>Дело, семья, спорт, всё по&nbsp;списку. Внутри пусто, и&nbsp;утром тяжелее, чем вечером. Разберём, откуда берётся эта пустота и&nbsp;почему её&nbsp;принимают за&nbsp;усталость от&nbsp;работы.</p></div>
<div class="card"><h3>Доход годами у одной&nbsp;цифры</h3><p>Рывок вверх есть, а&nbsp;через месяц всё возвращается к&nbsp;привычной сумме. Разберём, какое детское решение держит эту планку.</p></div>
<div class="card"><h3>Что такое важность</h3><p>Где вцепился, там и&nbsp;заклинило: раздутая ставка сжимает выбор до&nbsp;одного варианта. Как это выглядит в&nbsp;переговорах, на&nbsp;первом свидании и в&nbsp;большом решении.</p></div>
<div class="card"><h3>Психодрама и&nbsp;разговор с&nbsp;психологом</h3><p>Один инструмент работает словами, другой живой сценой. Чем они отличаются по&nbsp;глубине, по&nbsp;скорости и по&nbsp;тому, что остаётся после.</p></div>
<div class="card"><h3>Аффирмации держатся&nbsp;неделю</h3><p>Слова повторяются на&nbsp;верхнем этаже, запись живёт на&nbsp;нижнем. Что вместо них делают на&nbsp;Марафоне каждое утро и&nbsp;почему это срабатывает.</p></div>
</div>
</div>
<aside class="side">
<div class="box"><div class="lbl">Библиотека</div><div class="big">26 тем</div><p>Пять разделов, темы расписаны заранее. Каждая готовая статья появится здесь ссылкой.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Формат</p>
<h2>Как устроен каждый&nbsp;разбор</h2>
<p>Статьи школы идут по&nbsp;одному порядку. Сначала живая сцена, в&nbsp;которой узнаёшь свой вечер. Потом механика: что срабатывает и в&nbsp;какой последовательности. Дальше имена и&nbsp;цифры, на&nbsp;которых это стоит: двенадцать миллисекунд форы у&nbsp;миндалины, девяносто секунд жизни эмоции, спонтанность по&nbsp;Морено. В&nbsp;конце то,&nbsp;что можно сделать самому, и&nbsp;честная граница: где чтения хватит, а&nbsp;где нужна живая&nbsp;работа.</p>
<p>Заказных текстов и&nbsp;пересказов чужих книг здесь не&nbsp;будет. Каждый разбор пишется на&nbsp;материале групп: реальные сцены зала, слова учеников, случаи, которые повторяются из набора в&nbsp;набор.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Волна</div><div class="big">90 сек</div><p>Столько живёт химия эмоции, если не&nbsp;кормить её&nbsp;мыслями по&nbsp;кругу (Болте&nbsp;Тейлор). Дальше решается уже&nbsp;ясно.</p></div>
</aside>
</div></div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Пока статьи&nbsp;пишутся</p>
<h2>Что можно читать прямо&nbsp;сейчас</h2>
<div class="grid2" style="margin-top:22px">
<div class="card"><h3>Гайд&nbsp;школы</h3><p>«Кто пишет сценарий твоей&nbsp;жизни»: полчаса чтения, механика повтора, четыре частых записи наших групп и&nbsp;самодиагностика на&nbsp;десять пунктов.&nbsp;<a href="/chizhovy2/gid/">Читать</a></p></div>
<div class="card"><h3>Словарь&nbsp;школы</h3><p>Четырнадцать слов, на&nbsp;которых говорит группа: точка&nbsp;А, старая запись, захват, важность, вклад.&nbsp;<a href="/chizhovy2/slovar/">Открыть словарь</a></p></div>
<div class="card"><h3>Истоки&nbsp;метода</h3><p>Пять источников с&nbsp;разбором каждого: психодрама Морено, трансерфинг, тренинг est, Годдард и&nbsp;<a href="/chizhovy2/istoki/nauka/">наука</a>.&nbsp;<a href="/chizhovy2/istoki/">Смотреть истоки</a></p></div>
<div class="card"><h3>Живые&nbsp;истории</h3><p>Путь предпринимателя от&nbsp;кассового разрыва до&nbsp;новых целей и&nbsp;девяносто дней команды изнутри.&nbsp;<a href="/chizhovy2/istorii/">Читать истории</a></p></div>
</div>
</div>
<aside class="side">
</aside>
</div></div></section>







<section><div class="wrap">
<p class="eyebrow">Как будут устроены разборы</p>
<h2>Один разбор, четыре части</h2>
<p class="sub">Каждая статья строится одинаково, чтобы можно было читать с&nbsp;любого места.</p>
<div class="grid2" style="margin-top:30px">
<div class="card">{icon('lens')}<h3>Сцена из&nbsp;жизни</h3><p>Начинаем с&nbsp;конкретного эпизода: вечер, разговор, реплика. Без общих слов про «непонимание в&nbsp;паре».</p></div>
<div class="card">{icon('loop','var(--copper)')}<h3>Механика повтора</h3><p>Разбираем, где включается старая запись и&nbsp;почему круг замыкается именно так.</p></div>
<div class="card">{icon('layers','var(--sage-deep)')}<h3>Что говорит наука</h3><p>Там, где есть исследование, называем его: автор, год, суть. Где нет, честно пишем, что это опыт зала.</p></div>
<div class="card">{icon('route','var(--sand)')}<h3>Что с&nbsp;этим делать</h3><p>Конкретный шаг, который можно попробовать сегодня. Не&nbsp;«полюби себя», а&nbsp;действие с&nbsp;понятным результатом.</p></div>
</div>
</div></section>

<section><div class="wrap"><div class="tside">
<div class="col">
<p class="eyebrow">Что разберём первым</p>
<h2>Пять тем, с&nbsp;которых начнём</h2>
<h3>Ссоры по&nbsp;одному кругу</h3>
<p>Почему один и&nbsp;тот&nbsp;же спор повторяется годами с&nbsp;разными людьми и&nbsp;в&nbsp;разных декорациях. Что запускает круг и&nbsp;в&nbsp;какой точке его можно разомкнуть.</p>
<h3>Близость ушла в&nbsp;быт</h3>
<p>Общий календарь есть, разговоров нет. Разбираем, куда девается близость и&nbsp;почему её&nbsp;не&nbsp;вернуть уговорами и&nbsp;свиданиями по&nbsp;расписанию.</p>
<h3>Всё понимаю, ничего не&nbsp;меняется</h3>
<p>Самая частая боль тех, кто прочитал книги и&nbsp;прошёл курсы. Где именно понимание перестаёт работать и&nbsp;что включается вместо него.</p>
<h3>Маятники простыми словами</h3>
<p>Что такое структуры, тянущие тебя в&nbsp;чужие сценарии, и&nbsp;как выходить из&nbsp;них, не&nbsp;уходя в&nbsp;лес.</p>
<h3>Что такое психодрама</h3>
<p>Метод, которому сто лет, объяснённый по-человечески: что происходит в&nbsp;сцене и&nbsp;почему тело верит этому больше, чем словам.</p>
</div>
<aside class="side">
<div class="box"><div class="lbl">Формат</div><p>Разбор на&nbsp;10-15 минут чтения. Без воды и&nbsp;без обязательной регистрации.</p></div>
<div class="box"><div class="lbl">Пока их&nbsp;нет</div><p>Основа метода уже разобрана на&nbsp;<a href="/chizhovy2/metod/">странице метода</a> и&nbsp;в&nbsp;<a href="/chizhovy2/slovar/">словаре школы</a>.</p></div>
</aside>
</div></div></section>

""")

css_path = ROOT / "site.css"
css_path.write_text(CSS.strip() + "\n", encoding="utf-8")
n = 0
import hashlib as _h
CSS_VER = _h.md5(CSS.encode()).hexdigest()[:8]

for rel, (title, desc, active, body) in P.items():
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(btns_class(page(title, desc, active, body)), encoding="utf-8")
    n += 1
print(f"OK v2: site.css + {n} страниц (иконки, диаграмма, таймлайн, мозаика, фавикон)")
