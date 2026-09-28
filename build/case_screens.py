# Draws the demo UI screens, wireframes and sketches for the `case` theme (original CC0 work, credited in readme).
# Run: python3 build/case_screens.py  -> themes/case/assets/images/{ui-*,wf-*,sk-*}.jpg and credits in .images.json
import json, os, random
from PIL import Image, ImageDraw, ImageFont

OUT = 'themes/case/assets/images'
F = '/System/Library/Fonts/HelveticaNeue.ttc'
def font(size, bold=False):
    return ImageFont.truetype(F, size, index=1 if bold else 0)

INK, PAPER, BLUE, LIME, GREY, LINE = (14, 14, 14), (255, 255, 255), (31, 59, 255), (215, 255, 58), (110, 110, 105), (200, 200, 194)
made = {}


def save(im, name, title):
    im.convert('RGB').save(os.path.join(OUT, name + '.jpg'), quality=82, optimize=True)
    made[name] = {'title': title, 'creator': 'WP-OSS, drawn for the Case theme demo', 'license': 'CC0', 'source': 'Original work',
                  'url': 'https://github.com/sampler321/wp-oss/tree/main/build/case_screens.py', 'query': ''}


def frame(w, h, bg=(241, 241, 238)):
    im = Image.new('RGB', (w, h), bg)
    return im, ImageDraw.Draw(im)


def kiosk(d, x, y, w, h, title, body):
    """A 9:16 touchscreen panel."""
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=INK, width=4)
    d.rectangle([x, y, x + w, y + 90], fill=(0, 51, 102))
    d.text((x + 28, y + 26), title, font=font(34, True), fill=PAPER)
    body(d, x, y + 90, w, h - 90)


# ---------- before: fare grid first ----------
im, d = frame(1600, 1000)
def old_body(d, x, y, w, h):
    d.text((x + 28, y + 24), 'Choose your fare zone', font=font(30, True), fill=INK)
    prices = ['A £2.40', 'B £2.90', 'C £3.40', 'D £3.80', 'E £4.20', 'F £4.90', 'G £5.60', 'H £6.10', 'J £6.80', 'K £7.40', 'L £8.20', 'M £9.10']
    for i, p in enumerate(prices):
        cx, cy = x + 28 + (i % 3) * ((w - 56) // 3), y + 90 + (i // 3) * 120
        d.rectangle([cx, cy, cx + (w - 56) // 3 - 16, cy + 100], fill=(200, 30, 40) if i % 2 else (40, 70, 170))
        d.text((cx + 18, cy + 32), p, font=font(30, True), fill=PAPER)
    d.text((x + 28, y + h - 150), 'Railcard?   Yes   No', font=font(28), fill=INK)
    d.text((x + 28, y + h - 90), 'Destination not listed? Ask at the ticket office', font=font(22), fill=GREY)
kiosk(d, 520, 40, 560, 920, 'Buy a ticket', old_body)
save(im, 'ui-kiosk-before', 'Ticket machine, fare grid first (before)')

# ---------- after: destination first ----------
im, d = frame(1600, 1000)
def new_body(d, x, y, w, h):
    d.text((x + 28, y + 24), 'Where are you going?', font=font(34, True), fill=INK)
    d.rectangle([x + 28, y + 84, x + w - 28, y + 150], outline=INK, width=3)
    d.text((x + 46, y + 100), 'Type a station', font=font(28), fill=GREY)
    for i, s in enumerate(['Partick', 'Hyndland', 'Glasgow Central', 'Paisley Gilmour St', 'Dalmuir', 'Milngavie']):
        yy = y + 180 + i * 78
        d.rectangle([x + 28, yy, x + w - 28, yy + 64], fill=(236, 240, 255) if i else LIME)
        d.text((x + 46, yy + 16), s, font=font(28, i == 0), fill=INK)
        d.text((x + w - 150, yy + 18), ['12 min', '15 min', '4 min', '14 min', '22 min', '26 min'][i], font=font(22), fill=GREY)
    d.rectangle([x + 28, y + h - 120, x + w - 28, y + h - 40], fill=BLUE)
    d.text((x + 46, y + h - 98), 'Show me the price', font=font(30, True), fill=PAPER)
kiosk(d, 520, 40, 560, 920, 'Buy a ticket', new_body)
save(im, 'ui-kiosk-after', 'Ticket machine, destination first (after)')

# ---------- price with railcard beside it ----------
im, d = frame(1600, 1000)
def price_body(d, x, y, w, h):
    d.text((x + 28, y + 24), 'Queen Street to Partick', font=font(30, True), fill=INK)
    rows = [('Single', '£2.90', '£1.90 with a railcard'), ('Return today', '£4.40', '£2.90 with a railcard'), ('Day ticket, all zones', '£9.10', '£6.00 with a railcard')]
    for i, (a, b, c) in enumerate(rows):
        yy = y + 100 + i * 150
        d.rectangle([x + 28, yy, x + w - 28, yy + 126], outline=INK, width=3)
        d.text((x + 46, yy + 18), a, font=font(28, True), fill=INK)
        d.text((x + w - 150, yy + 18), b, font=font(30, True), fill=INK)
        d.rectangle([x + 46, yy + 72, x + 46 + 310, yy + 108], fill=LIME)
        d.text((x + 56, yy + 78), c, font=font(22), fill=INK)
    d.text((x + 28, y + h - 90), 'Tap a ticket to pay by card or cash', font=font(24), fill=GREY)
kiosk(d, 520, 40, 560, 920, 'Your ticket', price_body)
save(im, 'ui-kiosk-price', 'Ticket machine, price with railcard saving beside it')

# ---------- wireframes (lo-fi) ----------
def wire(name, title, labels):
    im, d = frame(1600, 1000, (250, 250, 247))
    for i, lab in enumerate(labels):
        x = 60 + i * 380
        d.rectangle([x, 120, x + 320, 860], outline=INK, width=3)
        d.text((x, 70), lab[0], font=font(26, True), fill=INK)
        yy = 150
        for kind in lab[1]:
            if kind == 'h':
                d.rectangle([x + 24, yy, x + 250, yy + 28], fill=(60, 60, 60)); yy += 50
            elif kind == 'i':
                d.rectangle([x + 24, yy, x + 296, yy + 56], outline=INK, width=2); yy += 76
            elif kind == 'l':
                for k in range(4):
                    d.line([x + 24, yy + 12, x + 296, yy + 12], fill=LINE, width=2); d.rectangle([x + 24, yy, x + 180, yy + 24], fill=(210, 210, 204)); yy += 52
            elif kind == 'b':
                d.rectangle([x + 24, yy, x + 296, yy + 60], fill=INK); yy += 80
            elif kind == 'm':
                d.rectangle([x + 24, yy, x + 296, yy + 200], fill=(228, 228, 222)); d.line([x + 24, yy, x + 296, yy + 200], fill=LINE, width=2); d.line([x + 296, yy, x + 24, yy + 200], fill=LINE, width=2); yy += 220
            elif kind == 'g':
                for k in range(6):
                    cx, cy = x + 24 + (k % 2) * 140, yy + (k // 2) * 76
                    d.rectangle([cx, cy, cx + 128, cy + 64], outline=INK, width=2)
                yy += 240
        if i < len(labels) - 1:
            d.line([x + 330, 490, x + 370, 490], fill=BLUE, width=5); d.polygon([(x + 372, 490), (x + 358, 480), (x + 358, 500)], fill=BLUE)
    save(im, name, title)

wire('wf-kiosk', 'Wireframes, ticket machine flow', [('Destination', 'hilb'), ('Map', 'hmb'), ('Ticket and price', 'hlbb'), ('Pay', 'higb')])
wire('wf-parking', 'Wireframes, parking by street name', [('Street', 'hil'), ('How long', 'hgb'), ('Pay', 'hib'), ('Reminder', 'hlb')])
wire('wf-checkout', 'Wireframes, self-checkout with tag step first', [('Scan', 'hmb'), ('Remove tags', 'hlb'), ('Bag', 'hmb'), ('Pay', 'higb')])

# ---------- phone app: parking ----------
im, d = frame(1600, 1000)
for i, (head, lines, hi) in enumerate([
        ('Where are you parked?', ['Causeyside Street', 'Gauze Street', 'Lawn Street', 'New Street'], 0),
        ('How long?', ['30 min, £0.80', '1 hour, £1.60', '2 hours, £3.20', 'Until 6pm, £4.80'], 1),
        ('Paid until 13:40', ['Causeyside Street, zone P4', 'Text reminder at 13:30', 'Extend by text: 1H to 60070'], 0)]):
    x = 230 + i * 400
    d.rounded_rectangle([x, 80, x + 330, 920], radius=44, fill=INK)
    d.rounded_rectangle([x + 14, 110, x + 316, 890], radius=30, fill=PAPER)
    d.text((x + 36, 150), head, font=font(24, True), fill=INK)
    for k, l in enumerate(lines):
        yy = 220 + k * 92
        d.rectangle([x + 36, yy, x + 294, yy + 72], fill=LIME if (k == hi and i < 2) else (238, 238, 234))
        d.text((x + 52, yy + 22), l, font=font(20), fill=INK)
    d.rectangle([x + 36, 780, x + 294, 846], fill=BLUE)
    d.text((x + 52, 800), ['Next', 'Pay £1.60', 'Extend'][i], font=font(22, True), fill=PAPER)
save(im, 'ui-parking', 'Parking app, three screens: street, time, confirmation')

# ---------- self-checkout ----------
im, d = frame(1600, 1000)
d.rectangle([300, 80, 1300, 900], fill=PAPER, outline=INK, width=4)
d.rectangle([300, 80, 1300, 170], fill=INK)
d.text((340, 108), 'Step 2 of 4: take the tags off', font=font(36, True), fill=PAPER)
for k, (item, st) in enumerate([('Wool jumper, navy, M', 'Tag removed'), ('Kilt pin, silver', 'No tag'), ('Scarf, Ancient tartan', 'Put it on the pad')]):
    yy = 220 + k * 150
    d.rectangle([340, yy, 1260, yy + 120], outline=INK, width=3)
    d.text((370, yy + 40), item, font=font(32), fill=INK)
    d.rectangle([980, yy + 30, 1230, yy + 90], fill=LIME if k == 2 else (236, 236, 232))
    d.text((1000, yy + 46), st, font=font(24, k == 2), fill=INK)
d.rectangle([340, 740, 1260, 850], fill=BLUE)
d.text((380, 776), 'All tags off? Go to bagging', font=font(34, True), fill=PAPER)
save(im, 'ui-checkout', 'Self-checkout screen with the tag step before payment')

# ---------- stop display ----------
im, d = frame(1600, 1000, (20, 20, 20))
d.rectangle([160, 140, 1440, 860], fill=(0, 0, 0), outline=(90, 90, 90), width=6)
d.text((220, 190), 'Paisley Road Toll, stop G', font=font(44, True), fill=(255, 190, 0))
for k, (r, dest, t) in enumerate([('4', 'Braehead', '2 min'), ('9', 'Govan Cross', '6 min'), ('4', 'Braehead', '14 min'), ('26', 'Glasgow Airport', '21 min')]):
    yy = 300 + k * 120
    d.text((220, yy), r, font=font(56, True), fill=(255, 190, 0))
    d.text((400, yy), dest, font=font(56), fill=(255, 190, 0))
    d.text((1200, yy), t, font=font(56, True), fill=(255, 190, 0))
d.text((220, 790), 'Times are live. Same as the app.', font=font(30), fill=(200, 160, 0))
save(im, 'ui-departures', 'Bus stop display showing the next four buses with live times')

# ---------- journey sketch (pencil look) ----------
random.seed(4)
im, d = frame(1600, 1000, (248, 246, 238))
def wobbly(pts, w=3):
    q = [(x + random.uniform(-2, 2), y + random.uniform(-2, 2)) for x, y in pts]
    d.line(q, fill=(60, 60, 60), width=w)
stages = ['Arrive', 'Find machine', 'Pick destination', 'See price', 'Pay', 'Board']
mood = [0, -1, -2, -3, 0, 1]
for i, s in enumerate(stages):
    x = 100 + i * 240
    wobbly([(x, 140), (x + 200, 140), (x + 200, 230), (x, 230), (x, 140)])
    d.text((x + 16, 170), s, font=font(26), fill=(40, 40, 40))
    y = 560 - mood[i] * 80
    d.ellipse([x + 90, y - 14, x + 118, y + 14], outline=(40, 40, 40), width=3)
    if i:
        px, py = 100 + (i - 1) * 240 + 104, 560 - mood[i - 1] * 80
        wobbly([(px, py), (x + 104, y)], 3)
d.line([(80, 560), (1520, 560)], fill=(170, 170, 160), width=2)
d.text((100, 880), 'Journey sketch from platform interviews, Partick, April 2025', font=font(24), fill=(90, 90, 90))
d.rectangle([700, 760, 1000, 810], fill=LIME)
d.text((712, 770), 'Most people give up here', font=font(24, True), fill=INK)
save(im, 'sk-journey', 'Pencil sketch of the ticket buying journey with the low point at the price screen')

# ---------- design system sheet ----------
im, d = frame(1600, 1000, PAPER)
d.text((80, 60), 'Machine UI kit, v2', font=font(44, True), fill=INK)
for k, (c, n) in enumerate([((0, 51, 102), 'Operator navy'), (BLUE, 'Action blue'), (LIME, 'Highlight'), (INK, 'Ink'), ((236, 240, 255), 'Row tint')]):
    x = 80 + k * 280
    d.rectangle([x, 150, x + 240, 330], fill=c, outline=INK, width=2)
    d.text((x, 345), n, font=font(24), fill=INK)
d.text((80, 430), 'Station name 28/36', font=font(36, True), fill=INK)
d.text((80, 490), 'Supporting text 22/30, never below 20 on a machine', font=font(26), fill=INK)
for k, (lab, fill, fg) in enumerate([('Primary', BLUE, PAPER), ('Secondary', PAPER, INK), ('Highlight', LIME, INK)]):
    x = 80 + k * 420
    d.rectangle([x, 600, x + 360, 690], fill=fill, outline=INK, width=3)
    d.text((x + 30, 628), lab + ' button', font=font(30, True), fill=fg)
d.rectangle([80, 760, 1500, 840], outline=INK, width=3)
d.text((110, 784), 'Search field, 64 px tall, full width, keyboard opens on tap', font=font(28), fill=GREY)
save(im, 'ui-kit', 'Design system sheet for the ticket machines: colours, type sizes, buttons and the search field')

cp = 'themes/case/.images.json'
c = json.load(open(cp)) if os.path.exists(cp) else {}
c.update(made)
json.dump(c, open(cp, 'w'), indent=2)
print('drew', len(made))
