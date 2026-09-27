"""Make a contact sheet of a theme's demo images so they can be checked in one look.

Usage: python3 tools/contact-sheet.py <slug>   ->  prints the path of the sheet JPEG (view it with the Read tool)
"""
import glob, os, sys
from PIL import Image, ImageDraw

slug = sys.argv[1]
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'themes', slug, 'assets', 'images')
files = sorted(glob.glob(os.path.join(root, '*.jpg')) + glob.glob(os.path.join(root, '*.webp')))
if not files:
    sys.exit('no images')
W, COLS = 320, 6
thumbs = []
for f in files:
    im = Image.open(f).convert('RGB')
    im = im.resize((W, int(im.height * W / im.width)))
    thumbs.append((os.path.basename(f), im))
rows = [thumbs[i:i + COLS] for i in range(0, len(thumbs), COLS)]
heights = [max(t[1].height for t in r) + 24 for r in rows]
sheet = Image.new('RGB', (W * COLS, sum(heights)), 'white')
d = ImageDraw.Draw(sheet)
y = 0
for r, h in zip(rows, heights):
    for c, (name, im) in enumerate(r):
        sheet.paste(im, (c * W, y + 20))
        d.text((c * W + 4, y + 4), name, fill='black')
    y += h
cache = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.cache'); os.makedirs(cache, exist_ok=True); out = os.path.abspath(os.path.join(cache, f'contact-{slug}.jpg'))
sheet.save(out, quality=80)
print(out)
