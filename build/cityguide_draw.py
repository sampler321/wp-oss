"""Draw the numbered sketch map for cityguide (Lampje, an independent guide to Eindhoven).

Run from the repo root: python3 build/cityguide_draw.py
Writes themes/cityguide/assets/images/sketch-map.jpg and credits it (CC0) in themes/cityguide/.images.json.
A schematic, not-to-scale map: ring road, the Dommel, the railway, neighbourhood names and red numbered pins that match
the numbered list in the map pattern.
"""
import json, os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

T = 'themes/cityguide'
CACHE = '.cache/cityguide-fonts'
os.makedirs(CACHE, exist_ok=True)
for src, dst in [('mona-sans-normal-800_900.woff2', 'mona.ttf'), ('work-sans-normal-400_600.woff2', 'work.ttf')]:
    if not os.path.exists(os.path.join(CACHE, dst)):
        f = TTFont(os.path.join(T, 'assets/fonts', src)); f.flavor = None; f.save(os.path.join(CACHE, dst))

S = 2
W = H = 1200 * S
INK, RED, BLUE, PINK, PAPER, GREEN = (17, 17, 17), (216, 0, 40), (28, 63, 214), (242, 184, 207), (255, 255, 255), (206, 226, 196)

def F(name, size):
    f = ImageFont.truetype(os.path.join(CACHE, name), size * S)
    try:
        axes = f.get_variation_axes()
        f.set_variation_by_axes([900 if a.get('name', b'') in (b'Weight', 'Weight') else a['default'] for a in axes] if 'mona' in name else [a['default'] for a in axes])
    except Exception:
        pass
    return f

im = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(im)
P = lambda x, y: (x * S, y * S)

# parks
for box in [(840, 780, 1120, 1010), (120, 860, 330, 1080), (700, 120, 900, 260)]:
    d.rounded_rectangle([P(*box[:2]), P(*box[2:])], radius=40 * S, fill=GREEN)
# the Dommel, north to south, east of centre
river = [P(760, -20), P(720, 180), P(690, 360), P(640, 520), P(660, 660), P(720, 800), P(760, 980), P(800, 1220)]
d.line(river, fill=BLUE, width=14 * S, joint='curve')
# ring road
d.rounded_rectangle([P(300, 300), P(900, 880)], radius=220 * S, outline=INK, width=12 * S)
# railway, west to east across the north of the centre
d.line([P(-20, 430), P(1220, 470)], fill=INK, width=5 * S)
for x in range(0, 1220, 36):
    y = 430 + 40 * x / 1240
    d.line([P(x, y - 10), P(x, y + 10)], fill=INK, width=3 * S)
d.rectangle([P(560, 420), P(640, 470)], fill=INK)
fl = F('work.ttf', 22)
d.text(P(560, 372), 'Station', font=fl, fill=INK)

fn = F('mona.ttf', 34)
for x, y, name in [(60, 250, 'Strijp'), (470, 90, 'Woensel'), (960, 500, 'Tongelre'), (430, 1040, 'Stratum'),
                   (70, 640, 'Gestel'), (470, 600, 'Centrum')]:
    d.text(P(x, y), name, font=fn, fill=INK)
d.text(P(850, 1030), 'Genneper Parken', font=fl, fill=INK)
d.text(P(640, 70), 'Dommel', font=F('work.ttf', 22), fill=BLUE)

PINS = [(170, 340), (560, 700), (700, 760), (860, 560), (380, 520), (960, 880), (250, 160), (560, 230)]
fp = F('mona.ttf', 30)
for i, (x, y) in enumerate(PINS, 1):
    r = 34
    d.ellipse([P(x - r, y - r), P(x + r, y + r)], fill=RED, outline=INK, width=4 * S)
    t = str(i)
    tw = d.textlength(t, font=fp)
    d.text((x * S - tw / 2, (y - 22) * S), t, font=fp, fill=PAPER)

d.rectangle([P(0, 1130), P(1200, 1200)], fill=PINK)
d.text(P(40, 1146), 'Lampje sketch map. Not to scale. North is up.', font=F('work.ttf', 24), fill=INK)
im = im.resize((1200, 1200), Image.LANCZOS)
im.save(os.path.join(T, 'assets/images/sketch-map.jpg'), 'JPEG', quality=84, optimize=True)

cp = os.path.join(T, '.images.json')
c = json.load(open(cp))
c['sketch-map'] = {'title': 'Sketch map of Eindhoven with numbered pins', 'creator': 'WP-OSS, drawn for this theme with Pillow', 'license': 'CC0',
                   'source': 'generated', 'url': 'https://github.com/sampler321/wp-oss/blob/main/build/cityguide_draw.py', 'query': ''}
json.dump(c, open(cp, 'w'), indent=2)
print('map drawn')
