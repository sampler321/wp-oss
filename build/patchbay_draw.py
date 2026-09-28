"""Draw the flat pedal panel and PCB drawings used as patchbay product images.

Run from the repo root: python3 build/patchbay_draw.py
Writes themes/patchbay/assets/images/draw-*.jpg and adds CC0 credits to themes/patchbay/.images.json.
The drawings are made here with Pillow, in the theme's own colours and fonts, like the panel drawings and drill
templates small pedal makers publish. No photos of other brands' pedals are used as product images.
"""
import json, math, os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

T = 'themes/patchbay'
CACHE = '.cache/patchbay-fonts'
os.makedirs(CACHE, exist_ok=True)
for src, dst in [('chubbo-normal-700.woff2', 'chubbo.ttf'), ('ibm-plex-sans-normal-400_600.woff2', 'plex.ttf')]:
    if not os.path.exists(os.path.join(CACHE, dst)):
        f = TTFont(os.path.join(T, 'assets/fonts', src)); f.flavor = None; f.save(os.path.join(CACHE, dst))

INK = (20, 20, 20)
WHITE = (250, 250, 247)
COL = {'teal': (14, 156, 154), 'yellow': (242, 185, 15), 'red': (215, 38, 30), 'orange': (232, 98, 44),
       'paper': (237, 234, 226), 'pcb': (31, 111, 74), 'cream': (244, 236, 214), 'blue': (38, 84, 160)}
S = 2  # supersample


def font(name, size):
    return ImageFont.truetype(os.path.join(CACHE, name), size * S)


def arrow_dim(d, x1, y1, x2, y2, label, f, vertical=False):
    w = 3 * S
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)
    a = 14 * S
    if vertical:
        d.polygon([(x1, y1), (x1 - a / 2, y1 + a), (x1 + a / 2, y1 + a)], fill=INK)
        d.polygon([(x2, y2), (x2 - a / 2, y2 - a), (x2 + a / 2, y2 - a)], fill=INK)
        tw = d.textlength(label, font=f)
        txt = Image.new('RGBA', (int(tw) + 10, f.size + 20), (0, 0, 0, 0))
        ImageDraw.Draw(txt).text((5, 0), label, font=f, fill=INK)
        txt = txt.rotate(90, expand=True)
        return txt
    d.polygon([(x1, y1), (x1 + a, y1 - a / 2), (x1 + a, y1 + a / 2)], fill=INK)
    d.polygon([(x2, y2), (x2 - a, y2 - a / 2), (x2 - a, y2 + a / 2)], fill=INK)
    tw = d.textlength(label, font=f)
    d.text(((x1 + x2) / 2 - tw / 2, y1 + 10 * S), label, font=f, fill=INK)


def knob(d, cx, cy, r, angle, label, f, colour=INK):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=colour, outline=INK, width=3 * S)
    a = math.radians(angle)
    d.line([(cx, cy), (cx + math.sin(a) * r * 0.8, cy - math.cos(a) * r * 0.8)], fill=WHITE, width=6 * S)
    tw = d.textlength(label, font=f)
    d.text((cx - tw / 2, cy + r + 12 * S), label, font=f, fill=INK)


def pedal(fname, name, ground, body, knobs, sub, size='Hammond 1590B', led=(255, 60, 40), text=INK):
    W = H = 1200 * S
    im = Image.new('RGB', (W, H), COL[ground])
    d = ImageDraw.Draw(im)
    bw, bh = 470 * S, 800 * S
    x0, y0 = (W - bw) // 2, (H - bh) // 2 + 20 * S
    # jacks
    for jx, side in [(x0 - 34 * S, 0), (x0 + bw, 1)]:
        d.rectangle([jx, y0 + 180 * S, jx + 34 * S, y0 + 260 * S], fill=(190, 190, 185), outline=INK, width=3 * S)
    d.rectangle([W // 2 - 30 * S, y0 - 30 * S, W // 2 + 30 * S, y0], fill=(190, 190, 185), outline=INK, width=3 * S)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=36 * S, fill=COL[body], outline=INK, width=5 * S)
    fl = font('plex.ttf', 22)
    n = len(knobs)
    if n == 1:
        pos = [(W // 2, y0 + 170 * S)]
    elif n == 2:
        pos = [(x0 + 130 * S, y0 + 170 * S), (x0 + bw - 130 * S, y0 + 170 * S)]
    else:
        pos = [(x0 + 110 * S, y0 + 150 * S), (x0 + bw - 110 * S, y0 + 150 * S), (W // 2, y0 + 330 * S)]
    for (cx, cy), (lab, ang) in zip(pos, knobs):
        knob(d, cx, cy, 62 * S, ang, lab, fl)
    ft = font('chubbo.ttf', 64)
    tw = d.textlength(name, font=ft)
    if tw > bw - 40 * S:
        ft = font('chubbo.ttf', 50); tw = d.textlength(name, font=ft)
    d.text((W // 2 - tw / 2, y0 + 440 * S), name, font=ft, fill=text)
    fs = font('plex.ttf', 24)
    tw = d.textlength(sub, font=fs)
    d.text((W // 2 - tw / 2, y0 + 530 * S), sub, font=fs, fill=text)
    d.ellipse([W // 2 - 14 * S, y0 + 590 * S, W // 2 + 14 * S, y0 + 618 * S], fill=led, outline=INK, width=3 * S)
    d.ellipse([W // 2 - 52 * S, y0 + 650 * S, W // 2 + 52 * S, y0 + 754 * S], fill=(205, 205, 200), outline=INK, width=4 * S)
    d.ellipse([W // 2 - 30 * S, y0 + 672 * S, W // 2 + 30 * S, y0 + 732 * S], fill=(170, 170, 165), outline=INK, width=3 * S)
    fd = font('plex.ttf', 24)
    arrow_dim(d, x0, y0 + bh + 40 * S, x0 + bw, y0 + bh + 40 * S, '60 mm', fd)
    lab = arrow_dim(d, x0 + bw + 90 * S, y0, x0 + bw + 90 * S, y0 + bh, '112 mm', fd, vertical=True)
    im.paste(lab, (x0 + bw + 100 * S, y0 + bh // 2 - lab.size[1] // 2), lab)
    d.text((70 * S, 60 * S), size + ', 9V DC centre negative', font=fs, fill=INK)
    im = im.resize((1200, 1200), Image.LANCZOS)
    im.save(os.path.join(T, 'assets/images', fname), 'JPEG', quality=82, optimize=True, progressive=True)


def pcb(fname, name, ground, parts, note):
    W = H = 1200 * S
    im = Image.new('RGB', (W, H), COL[ground])
    d = ImageDraw.Draw(im)
    bw, bh = 760 * S, 620 * S
    x0, y0 = (W - bw) // 2, (H - bh) // 2 - 30 * S
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=22 * S, fill=COL['pcb'], outline=INK, width=5 * S)
    for hx, hy in [(x0 + 34 * S, y0 + 34 * S), (x0 + bw - 34 * S, y0 + 34 * S), (x0 + 34 * S, y0 + bh - 34 * S), (x0 + bw - 34 * S, y0 + bh - 34 * S)]:
        d.ellipse([hx - 16 * S, hy - 16 * S, hx + 16 * S, hy + 16 * S], fill=COL[ground], outline=(230, 200, 90), width=5 * S)
    fl = font('plex.ttf', 24)
    gold = (230, 200, 90)
    silk = (245, 245, 240)
    for i, (lab, kind) in enumerate(parts):
        cx = x0 + 150 * S + (i % 4) * 160 * S
        cy = y0 + 170 * S + (i // 4) * 200 * S
        if kind == 'r':
            d.rectangle([cx - 50 * S, cy - 16 * S, cx + 50 * S, cy + 16 * S], outline=silk, width=3 * S)
            for px in (cx - 70 * S, cx + 70 * S):
                d.ellipse([px - 11 * S, cy - 11 * S, px + 11 * S, cy + 11 * S], fill=gold)
        elif kind == 'c':
            d.ellipse([cx - 36 * S, cy - 36 * S, cx + 36 * S, cy + 36 * S], outline=silk, width=3 * S)
            for px in (cx - 16 * S, cx + 16 * S):
                d.ellipse([px - 9 * S, cy - 9 * S, px + 9 * S, cy + 9 * S], fill=gold)
        else:
            d.chord([cx - 40 * S, cy - 40 * S, cx + 40 * S, cy + 40 * S], 200, 340, outline=silk, width=3 * S)
            for px in (cx - 24 * S, cx, cx + 24 * S):
                d.ellipse([px - 9 * S, cy - 9 * S, px + 9 * S, cy + 9 * S], fill=gold)
        tw = d.textlength(lab, font=fl)
        d.text((cx - tw / 2, cy + 44 * S), lab, font=fl, fill=silk)
    # traces
    for i in range(3):
        yy = y0 + bh - 120 * S + i * 26 * S
        d.line([(x0 + 90 * S, yy), (x0 + bw - 200 * S, yy), (x0 + bw - 160 * S, yy - 40 * S)], fill=(60, 150, 100), width=8 * S)
    ft = font('chubbo.ttf', 60)
    tw = d.textlength(name, font=ft)
    d.text((W // 2 - tw / 2, y0 + bh + 60 * S), name, font=ft, fill=INK)
    fs = font('plex.ttf', 26)
    tw = d.textlength(note, font=fs)
    d.text((W // 2 - tw / 2, y0 + bh + 150 * S), note, font=fs, fill=INK)
    im = im.resize((1200, 1200), Image.LANCZOS)
    im.save(os.path.join(T, 'assets/images', fname), 'JPEG', quality=82, optimize=True, progressive=True)


DRAWINGS = {
  'draw-coal-tit': lambda: pedal('draw-coal-tit.jpg', 'Coal Tit', 'teal', 'orange', [('Level', -40), ('Fuzz', 130)], 'silicon fuzz'),
  'draw-ginnel': lambda: pedal('draw-ginnel.jpg', 'Ginnel', 'yellow', 'teal', [('Gain', 30), ('Level', -20), ('Tone', 0)], 'overdrive'),
  'draw-moor-echo': lambda: pedal('draw-moor-echo.jpg', 'Moor Echo', 'red', 'yellow', [('Time', -60), ('Repeats', 40), ('Mix', -10)], 'delay, 30 to 600 ms'),
  'draw-tram-stop': lambda: pedal('draw-tram-stop.jpg', 'Tram Stop', 'paper', 'red', [('Rate', 50), ('Depth', -30), ('Level', 0)], 'optical tremolo', text=WHITE),
  'draw-mill-boost': lambda: pcb('draw-mill-boost.jpg', 'Mill Boost PCB', 'yellow', [('R1', 'r'), ('R2', 'r'), ('C1', 'c'), ('Q1', 'q'), ('R3', 'r'), ('C2', 'c'), ('R4', 'r'), ('C3', 'c')], '38 × 32 mm, fits a 1590A'),
  'draw-snicket': lambda: pcb('draw-snicket.jpg', 'Snicket PCB', 'orange', [('Q1', 'q'), ('Q2', 'q'), ('D1', 'c'), ('D2', 'c'), ('R1', 'r'), ('R2', 'r'), ('C1', 'c'), ('R3', 'r')], 'octave fuzz, 50 × 40 mm, fits a 1590B'),
}

if __name__ == '__main__':
    cp = os.path.join(T, '.images.json')
    credits = json.load(open(cp))
    for k, fn in DRAWINGS.items():
        fn()
        credits[k] = {'title': 'Panel drawing: ' + k[5:].replace('-', ' '), 'creator': 'WP-OSS, drawn for this theme with Pillow', 'license': 'CC0',
                      'source': 'generated', 'url': 'https://github.com/sampler321/wp-oss/blob/main/build/patchbay_draw.py', 'query': ''}
    json.dump(credits, open(cp, 'w'), indent=2)
    print('drawn', len(DRAWINGS))
