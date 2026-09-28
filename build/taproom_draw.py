"""Draw the flat paper can labels and merch drawings used as taproom product and beer images.

Run from the repo root: python3 build/taproom_draw.py
Writes themes/taproom/assets/images/label-*.jpg and merch-*.jpg and credits them (CC0) in themes/taproom/.images.json.
The brewery's labels are plain printed paper labels: black type on white, a red batch stamp, on a brown-paper ground.
"""
import json, math, os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

T = 'themes/taproom'
CACHE = '.cache/taproom-fonts'
os.makedirs(CACHE, exist_ok=True)
fonts_dir = os.path.join(T, 'assets/fonts')
for f in os.listdir(fonts_dir):
    if f.endswith('.woff2') and 'italic' not in f:
        dst = os.path.join(CACHE, 'economica.ttf' if f.startswith('economica') else 'public.ttf')
        if not os.path.exists(dst):
            t = TTFont(os.path.join(fonts_dir, f)); t.flavor = None; t.save(dst)

S = 2
KRAFT, INK, RED, WHITE = (217, 195, 160), (26, 26, 26), (196, 40, 28), (255, 255, 255)

def F(name, size, weight=None):
    f = ImageFont.truetype(os.path.join(CACHE, name), int(size * S))
    if weight:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f

def centre(d, y, text, font, fill=INK, cx=600):
    w = d.textlength(text, font=font)
    d.text((cx * S - w / 2, y * S), text, font=font, fill=fill)

def stamp(im, text1, text2, cx, cy, r=92, angle=-14):
    layer = Image.new('RGBA', (r * 2 * S + 20, r * 2 * S + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    c = r * S + 10
    d.ellipse([10, 10, c * 2 - 10, c * 2 - 10], outline=RED + (235,), width=6 * S)
    d.ellipse([28, 28, c * 2 - 28, c * 2 - 28], outline=RED + (235,), width=2 * S)
    f1, f2 = F('economica.ttf', 30), F('public.ttf', 20, 700)
    w = d.textlength(text1, font=f1); d.text((c - w / 2, c - 44 * S), text1, font=f1, fill=RED + (235,))
    w = d.textlength(text2, font=f2); d.text((c - w / 2, c + 6 * S), text2, font=f2, fill=RED + (235,))
    layer = layer.rotate(angle, resample=Image.BICUBIC)
    im.paste(layer, (cx * S - layer.size[0] // 2, cy * S - layer.size[1] // 2), layer)

def label(fname, name, style, abv, hops, batch, note):
    W = H = 1200 * S
    im = Image.new('RGB', (W, H), KRAFT)
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = 170, 150, 1030, 1050
    d.rectangle([x0 * S, y0 * S, x1 * S, y1 * S], fill=WHITE, outline=INK, width=4 * S)
    d.rectangle([(x0 + 22) * S, (y0 + 22) * S, (x1 - 22) * S, (y1 - 22) * S], outline=INK, width=1 * S)
    centre(d, 205, 'COOPERAGE BREWING, SMITHFIELD, DUBLIN 7', F('public.ttf', 22, 700))
    d.line([(x0 + 60) * S, 250 * S, (x1 - 60) * S, 250 * S], fill=INK, width=2 * S)
    fn = F('economica.ttf', 150)
    while d.textlength(name, font=fn) > (x1 - x0 - 120) * S:
        fn = F('economica.ttf', fn.size / S - 8)
    centre(d, 300, name, fn)
    centre(d, 490, style, F('public.ttf', 38, 400))
    centre(d, 560, abv, F('economica.ttf', 110), fill=INK)
    centre(d, 700, 'Hops: ' + hops, F('public.ttf', 26, 400))
    centre(d, 745, note, F('public.ttf', 24, 400))
    d.line([(x0 + 60) * S, 800 * S, (x1 - 60) * S, 800 * S], fill=INK, width=2 * S)
    fs = F('public.ttf', 22, 400)
    d.text(((x0 + 60) * S, 830 * S), '440 ml can', font=fs, fill=INK)
    d.text(((x0 + 60) * S, 870 * S), 'Contains barley and wheat (gluten)', font=fs, fill=INK)
    d.text(((x0 + 60) * S, 910 * S), 'Keep cold. Drink fresh.', font=fs, fill=INK)
    stamp(im, 'BATCH', batch, 860, 900)
    im = im.resize((1200, 1200), Image.LANCZOS)
    im.save(os.path.join(T, 'assets/images', fname), 'JPEG', quality=84, optimize=True)

def merch(fname, kind, caption):
    W = H = 1200 * S
    im = Image.new('RGB', (W, H), KRAFT)
    d = ImageDraw.Draw(im)
    P = lambda pts: [(x * S, y * S) for x, y in pts]
    if kind == 'glass':
        d.polygon(P([(430, 220), (770, 220), (730, 980), (470, 980)]), fill=(250, 236, 200), outline=INK)
        d.line(P([(430, 220), (770, 220), (730, 980), (470, 980), (430, 220)]), fill=INK, width=6 * S)
        d.polygon(P([(440, 300), (760, 300), (732, 960), (468, 960)]), fill=(214, 150, 50))
        d.rectangle(P([(492, 520), (708, 700)]), fill=WHITE, outline=INK, width=3 * S)
        centre(d, 555, 'COOPERAGE', F('economica.ttf', 50))
        centre(d, 625, 'Smithfield', F('public.ttf', 26, 400))
    elif kind == 'tote':
        d.arc(P([(470, 160), (730, 460)]), 180, 360, fill=INK, width=14 * S)
        d.rectangle(P([(330, 320), (870, 1000)]), fill=(240, 232, 214), outline=INK, width=6 * S)
        d.rectangle(P([(420, 520), (780, 780)]), fill=WHITE, outline=INK, width=4 * S)
        centre(d, 560, 'COOPERAGE', F('economica.ttf', 72))
        centre(d, 660, 'Brewing, Dublin 7', F('public.ttf', 30, 400))
    else:
        d.polygon(P([(380, 220), (500, 180), (600, 230), (700, 180), (820, 220), (960, 380), (870, 460), (820, 420), (820, 1000), (380, 1000), (380, 420), (330, 460), (240, 380)]),
                  fill=INK, outline=INK)
        d.rectangle(P([(470, 430), (730, 620)]), fill=WHITE, outline=WHITE)
        centre(d, 455, 'COOPERAGE', F('economica.ttf', 60))
        centre(d, 545, 'Smithfield', F('public.ttf', 28, 400))
    centre(d, 1060, caption, F('public.ttf', 30, 700))
    im = im.resize((1200, 1200), Image.LANCZOS)
    im.save(os.path.join(T, 'assets/images', fname), 'JPEG', quality=84, optimize=True)

BEERS = [
    ('label-haymarket.jpg', 'HAYMARKET', 'Pale ale', '4.6%', 'Citra, Mosaic', '118', 'Vegan'),
    ('label-stoneybatter.jpg', 'STONEYBATTER', 'Table beer', '2.8%', 'Saaz, East Kent Goldings', '121', 'Vegan'),
    ('label-arran-quay.jpg', 'ARRAN QUAY', 'IPA', '6.2%', 'Nelson Sauvin, Motueka', '119', 'Vegan'),
    ('label-bow-street.jpg', 'BOW STREET', 'Stout', '5.0%', 'Fuggles', '117', 'Contains lactose'),
    ('label-phoenix.jpg', 'PHOENIX', 'Pilsner', '4.8%', 'Hallertau Mittelfrüh', '120', 'Vegan'),
    ('label-four-courts.jpg', 'FOUR COURTS', 'Imperial stout, rum barrel', '10.5%', 'Magnum', '96', 'Vegan'),
]

if __name__ == '__main__':
    cp = os.path.join(T, '.images.json')
    c = json.load(open(cp))
    for b in BEERS:
        label(*b)
        c[b[0][:-4]] = {'title': 'Can label: ' + b[1].title(), 'creator': 'WP-OSS, drawn for this theme with Pillow', 'license': 'CC0',
                        'source': 'generated', 'url': 'https://github.com/sampler321/wp-oss/blob/main/build/taproom_draw.py', 'query': ''}
    for fn, kind, cap in [('merch-glass.jpg', 'glass', 'Pint glass, 568 ml'), ('merch-tote.jpg', 'tote', 'Tote bag, unbleached cotton'), ('merch-tee.jpg', 'tee', 'T-shirt, black')]:
        merch(fn, kind, cap)
        c[fn[:-4]] = {'title': 'Merch drawing: ' + cap, 'creator': 'WP-OSS, drawn for this theme with Pillow', 'license': 'CC0',
                      'source': 'generated', 'url': 'https://github.com/sampler321/wp-oss/blob/main/build/taproom_draw.py', 'query': ''}
    json.dump(c, open(cp, 'w'), indent=2)
    print('drawn', len(BEERS) + 3)
