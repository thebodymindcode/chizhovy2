#!/bin/zsh
set -u
GEN=~/.claude/skills/site-panel/scripts/gen_image.py
OUT="/Users/q8111706yandex.ru/Documents/Чижовы-Настоящие-отношения/chizhovy2/images"
SLAV="distinctly Slavic Russian appearance, fair skin, light brown or dark blond hair, blue or grey eyes, clearly European facial features, absolutely no Asian features"
STYLE="photorealistic, cinematic, warm golden light, premium expensive location, muted warm palette with deep plum and sage green accents, subtle film grain, professional editorial photography, natural candid emotion, no text, no watermark"
typeset -a jobs
jobs=(
"gid-hero|1920:1080|A married couple in their early 40s, $SLAV, sitting apart on a sofa in an elegant evening living room after a difficult conversation, tense silence, both looking away in different directions, warm lamp glow, deep shadows, $STYLE"
"gid-posle|1360:768|A married couple in their 40s, $SLAV, laughing together at a bright breakfast table by a large window, real warm connection, morning golden light, fresh bread and coffee, $STYLE"
"site-m1|1168:880|A woman in her mid 30s, $SLAV, writing in a paper journal by a large window in the early morning, focused and calm, premium apartment, warm light, $STYLE"
"site-para-itog|1360:768|A couple in their 40s, $SLAV, cooking dinner together in a premium kitchen, genuine laughter, she hands him a plate, warm golden evening light, $STYLE"
"site-sessiya|1360:768|A man and a woman in their 40s, $SLAV, in a deep calm one-on-one conversation over two cups of tea at a small wooden table, cozy premium office corner, warm lamp, $STYLE"
)
i=0; total=${#jobs[@]}
for job in "${jobs[@]}"; do
  i=$((i+1)); name="${job%%|*}"; rest="${job#*|}"; ratio="${rest%%|*}"; prompt="${rest#*|}"
  echo "[$i/$total] перегенерация $name..."
  python3 "$GEN" --prompt "$prompt" --ratio "$ratio" --out "$OUT/$name.png" >>"$OUT/genlog.txt" 2>&1
  [ -s "$OUT/$name.png" ] && echo "[$i/$total] $name OK" || echo "[$i/$total] $name ПРОВАЛ"
done
echo ГОТОВО
