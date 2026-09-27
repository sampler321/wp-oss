#!/usr/bin/env python3
"""Aggregate field-study measurements. Usage: aggregate.py <av-dir> <ctl-dir> > summary.json"""
import json, sys, re, glob, os, math, collections, colorsys

AV, CTL = sys.argv[1], sys.argv[2]

def load(d):
    out = []
    for f in sorted(glob.glob(os.path.join(d, 'data', '*.json'))):
        j = json.load(open(f))
        tf = os.path.join(d, 'text', j['id'] + '.txt')
        j['_text'] = open(tf).read() if os.path.exists(tf) else ''
        # strip the injected 'Edit with Lovable' badge artefacts
        for k in ('text', 'bg', 'border', 'buttonBg', 'link'):
            j['colours'][k] = [x for x in j['colours'][k] if x[0] != '#C5C1B9' and not (j['id'].startswith('lov-') and x[0] == '#1B1B1B')]
        j['shadows'] = [x for x in j.get('shadows', []) if '0.88 0px 0px 0px 1px' not in x[0]]
        j['faceTally'] = [x for x in j.get('faceTally', []) if not (x[0] == 'CameraPlainVariable' and x[1] <= 12)]
        out.append(j)
    return out

TW = {  # Tailwind v3 default palette (subset used in UI work)
 'gray': ['#F9FAFB','#F3F4F6','#E5E7EB','#D1D5DB','#9CA3AF','#6B7280','#4B5563','#374151','#1F2937','#111827','#030712'],
 'slate': ['#F8FAFC','#F1F5F9','#E2E8F0','#CBD5E1','#94A3B8','#64748B','#475569','#334155','#1E293B','#0F172A','#020617'],
 'zinc': ['#FAFAFA','#F4F4F5','#E4E4E7','#D4D4D8','#A1A1AA','#71717A','#52525B','#3F3F46','#27272A','#18181B','#09090B'],
 'neutral': ['#F5F5F5','#E5E5E5','#D4D4D4','#A3A3A3','#737373','#525252','#404040','#262626','#171717','#0A0A0A'],
 'stone': ['#FAFAF9','#F5F5F4','#E7E5E4','#D6D3D1','#A8A29E','#78716C','#57534E','#44403C','#292524','#1C1917','#0C0A09'],
 'indigo': ['#EEF2FF','#E0E7FF','#C7D2FE','#A5B4FC','#818CF8','#6366F1','#4F46E5','#4338CA','#3730A3','#312E81'],
 'violet': ['#F5F3FF','#EDE9FE','#DDD6FE','#C4B5FD','#A78BFA','#8B5CF6','#7C3AED','#6D28D9','#5B21B6','#4C1D95'],
 'purple': ['#FAF5FF','#F3E8FF','#E9D5FF','#D8B4FE','#C084FC','#A855F7','#9333EA','#7E22CE','#6B21A8','#581C87'],
 'blue': ['#EFF6FF','#DBEAFE','#BFDBFE','#93C5FD','#60A5FA','#3B82F6','#2563EB','#1D4ED8','#1E40AF','#1E3A8A'],
 'sky': ['#0EA5E9','#0284C7'], 'cyan': ['#06B6D4','#0891B2'], 'teal': ['#14B8A6','#0D9488'],
 'emerald': ['#ECFDF5','#D1FAE5','#34D399','#10B981','#059669','#047857'], 'green': ['#22C55E','#16A34A','#15803D'],
 'amber': ['#FEF3C7','#FCD34D','#FBBF24','#F59E0B','#D97706','#B45309'], 'yellow': ['#FACC15','#EAB308'],
 'orange': ['#FB923C','#F97316','#EA580C'], 'red': ['#EF4444','#DC2626','#B91C1C'], 'rose': ['#F43F5E','#E11D48'], 'pink': ['#EC4899','#DB2777'],
}
TWFLAT = [(k, i, h) for k, v in TW.items() for i, h in enumerate(v)]
NAMED = {'#6366F1': 'indigo-500', '#4F46E5': 'indigo-600', '#8B5CF6': 'violet-500', '#7C3AED': 'violet-600', '#A855F7': 'purple-500', '#3B82F6': 'blue-500', '#2563EB': 'blue-600'}

def rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
def lab(h):
    def lin(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = map(lin, rgb(h))
    x = (r*0.4124 + g*0.3576 + b*0.1805) / 0.95047; y = r*0.2126 + g*0.7152 + b*0.0722; z = (r*0.0193 + g*0.1192 + b*0.9505) / 1.08883
    f = lambda t: t ** (1/3) if t > 0.008856 else 7.787*t + 16/116
    return (116*f(y) - 16, 500*(f(x) - f(y)), 200*(f(y) - f(z)))
def de2000(h1, h2):
    L1, a1, b1 = lab(h1); L2, a2, b2 = lab(h2)
    C1, C2 = math.hypot(a1, b1), math.hypot(a2, b2); Cb = (C1 + C2) / 2
    G = 0.5 * (1 - math.sqrt(Cb**7 / (Cb**7 + 25**7))); a1p, a2p = a1*(1+G), a2*(1+G)
    C1p, C2p = math.hypot(a1p, b1), math.hypot(a2p, b2)
    h1p = math.degrees(math.atan2(b1, a1p)) % 360; h2p = math.degrees(math.atan2(b2, a2p)) % 360
    dL, dC = L2 - L1, C2p - C1p
    dh = 0 if C1p*C2p == 0 else (h2p - h1p if abs(h2p - h1p) <= 180 else (h2p - h1p - 360 if h2p > h1p else h2p - h1p + 360))
    dH = 2*math.sqrt(C1p*C2p)*math.sin(math.radians(dh/2))
    Lb, Cbp = (L1 + L2)/2, (C1p + C2p)/2
    hb = h1p + h2p if C1p*C2p == 0 else ((h1p + h2p)/2 if abs(h1p - h2p) <= 180 else ((h1p + h2p + 360)/2 if h1p + h2p < 360 else (h1p + h2p - 360)/2))
    T = 1 - 0.17*math.cos(math.radians(hb - 30)) + 0.24*math.cos(math.radians(2*hb)) + 0.32*math.cos(math.radians(3*hb + 6)) - 0.20*math.cos(math.radians(4*hb - 63))
    Sl = 1 + 0.015*(Lb - 50)**2 / math.sqrt(20 + (Lb - 50)**2); Sc = 1 + 0.045*Cbp; Sh = 1 + 0.015*Cbp*T
    Rt = -2*math.sqrt(Cbp**7/(Cbp**7 + 25**7)) * math.sin(math.radians(60*math.exp(-((hb - 275)/25)**2)))
    return math.sqrt((dL/Sl)**2 + (dC/Sc)**2 + (dH/Sh)**2 + Rt*(dC/Sc)*(dH/Sh))
def hsl(h): r, g, b = rgb(h); hh, l, s = colorsys.rgb_to_hls(r, g, b); return hh*360, s, l
def lum(h):
    def lin(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = map(lin, rgb(h)); return 0.2126*r + 0.7152*g + 0.0722*b
def chromatic(h): _, s, l = hsl(h); return s > 0.25 and 0.12 < l < 0.9

def norm_font(f):
    if not f: return None
    f = re.sub(r'^__', '', f); f = re.sub(r'_[0-9a-f]{5,}$', '', f); f = re.sub(r'(_Fallback| Fallback|Variable| Variable|var\(.*)$', '', f).strip()
    f = f.replace('GeistSans', 'Geist').replace('Geist Sans', 'Geist').replace('GeistMono', 'Geist Mono')
    if f.lower() in ('ui-sans-serif', 'system-ui', '-apple-system', 'blinkmacsystemfont', 'segoe ui', 'sans-serif'): return 'system-ui stack'
    return f
SERIF = re.compile(r'playfair|cormorant|instrument serif|dm serif|fraunces|lora|baskerville|garamond|merriweather|newsreader|crimson|source serif|georgia|times|quattrocento|ovo|bodoni|prata|marcellus|cinzel|serif display|libre caslon|noto serif|pt serif|spectral|young serif|gloock|italiana|bellefair|tenor|rozha|abril|yeseva|dm serif|eb garamond|cardo|alegreya|literata|gilda|forum|castoro|besley|roboto serif|bitter|zilla|domine|vollkorn|petrona|brygada|sorts mill|marcellus|la belle', re.I)

def px(v):
    try: return float(str(v).replace('px', ''))
    except: return None

def shadow_kind(s):
    m = []
    for k, g in [('tw shadow-sm', '0px 1px 2px 0px'), ('tw shadow (base)', '0px 1px 3px 0px'), ('tw shadow-md', '0px 4px 6px -1px'), ('tw shadow-lg', '0px 10px 15px -3px'), ('tw shadow-xl', '0px 20px 25px -5px'), ('tw shadow-2xl', '0px 25px 50px -12px')]:
        if g in s: m.append(k)
    return m

PHRASES = ['get started', 'learn more', 'book now', 'contact us', 'get in touch', 'trusted by', 'ready to', 'why choose', 'our services', 'elevate', 'seamless', 'transform', 'unlock', 'effortless', 'crafted', 'passion', 'experience the', 'discover', 'journey', 'peace of mind', 'state-of-the-art', 'tailored', 'every detail', 'quality', '24/7', 'free quote', 'free estimate', 'book an appointment', 'curated', 'premium', 'timeless', 'sanctuary', 'artisan', 'handcrafted', 'bespoke', 'excellence', 'precision', 'we believe', 'your trusted', 'years of experience', 'satisfaction', 'join our', 'newsletter', 'all rights reserved', 'made with', 'lorem ipsum', 'expert', 'seamlessly', 'nestled', 'vibrant', 'meticulous', 'elevated', 'world-class', 'cutting-edge', 'not just', 'more than just', 'whether you', 'look no further', 'your vision', 'bring your', 'to life', 'from concept to', 'every step', 'the art of', 'where .{1,20} meets', 'built for', 'designed for', 'simple, transparent', 'no hidden fees', 'what our clients say', 'what our customers say', 'frequently asked', 'watch demo', 'start free', 'most popular']

def feats(d):
    t = d['_text']; words = max(1, len(t.split()))
    f = {}
    fp = d.get('fp', {})
    f['tailwind'] = fp.get('tailwindClasses', 0) >= 50
    v = d.get('vars', {})
    f['shadcn tokens'] = bool(v.get('--radius') or v.get('--primary') or v.get('--muted-foreground')) or fp.get('shadcnClasses', 0) >= 5
    f['lucide'] = fp.get('lucide', 0) > 0
    f['vite'] = fp.get('vite'); f['next'] = fp.get('next'); f['wordpress'] = fp.get('wordpress'); f['elementor'] = fp.get('elementor')
    faces = [norm_font(x[0]) for x in d.get('faceTally', [])]
    f['_primary_face'] = faces[0] if faces else None
    ty = d.get('type', {})
    f['_heading_face'] = norm_font(d['fonts'].get('h1') or d['fonts'].get('h2'))
    f['_body_face'] = norm_font(d['fonts'].get('body'))
    f['serif heading'] = bool(f['_heading_face'] and SERIF.search(f['_heading_face']))
    f['same face heading+body'] = f['_heading_face'] == f['_primary_face']
    # colours
    cols = d['colours']
    btn = [c for c, n in cols['buttonBg'] if chromatic(c)]
    txt = [c for c, n in cols['text'] + cols['link'] if chromatic(c)]
    bgc = [c for c, n in cols['bg'] if chromatic(c)]
    acc = (btn or txt or bgc or [None])[0]
    f['_accent'] = acc
    if acc:
        hue = hsl(acc)[0]; f['_accent_hue'] = round(hue)
        f['accent hue 245-275 (indigo/violet)'] = 245 <= hue <= 275 and hsl(acc)[1] > 0.3
        f['accent hue 200-290 (blue to violet)'] = 200 <= hue <= 290 and hsl(acc)[1] > 0.3
        near = min(((de2000(acc, h), n) for h, n in NAMED.items()), default=(99, None))
        f['_accent_nearest_tw'] = (round(near[0], 1), near[1])
    allhex = set(c for k in ('text', 'bg', 'border', 'buttonBg', 'link') for c, n in cols[k])
    twm = set()
    for h in allhex:
        for k, i, th in TWFLAT:
            if de2000(h, th) < 2.5: twm.add((h, k)); break
    f['_tw_matches'] = sorted(twm)
    f['>=2 chromatic/tinted colours within dE2.5 of Tailwind v3 defaults'] = len([x for x in twm if x[1] != 'neutral' and chromatic(x[0]) or x[1] in ('slate','gray','zinc') and x[0] not in ('#FFFFFF','#000000') and 0.03 < lum(x[0]) < 0.9]) >= 2
    f['any indigo/violet/purple within dE10 of 500/600'] = any(de2000(h, n) < 10 for h in set(c for k in ('bg','buttonBg','border') for c, n in cols[k]) for n in ('#6366F1', '#4F46E5', '#8B5CF6', '#7C3AED', '#A855F7') if chromatic(h))
    bg0 = cols['bg'][0][0] if cols['bg'] else '#FFFFFF'
    f['_page_bg'] = d.get('bodyBg') or bg0
    f['dark-dominant page'] = lum(bg0) < 0.05
    f['near-black text not #000'] = any(c in ('#0A0A0A', '#09090B', '#111827', '#0F172A', '#171717', '#18181B', '#1F2937', '#111111', '#1A1A1A') for c, n in cols['text'][:3])
    # type
    f['h1 centred'] = ty.get('h1Align') == 'center'
    trk = px(ty.get('h1Tracking')) if ty.get('h1Tracking') not in (None, 'normal') else 0
    f['h1 negative tracking'] = bool(trk and trk < 0)
    f['_h1_tracking_em'] = round(trk / ty['h1Size'], 3) if trk and ty.get('h1Size') else 0
    f['h1 single word/phrase styled differently'] = bool(ty.get('h1ColouredSpan') or ty.get('h1MixedFaces'))
    f['gradient headline text'] = bool(ty.get('h1Gradient')) or d.get('gradientText', 0) > 0
    f['_h1_size'] = ty.get('h1Size'); f['_body_size'] = ty.get('bodySize')
    f['display:body ratio < 4'] = bool(ty.get('h1Size') and ty.get('bodySize') and ty['h1Size'] / ty['bodySize'] < 4)
    f['body text 16px or smaller'] = bool(ty.get('bodySize') and ty['bodySize'] <= 16)
    # radius
    r = d['radius']
    bmode = r['button'][0][0] if r['button'] else None; cmode = r['card'][0][0] if r['card'] else None
    f['_button_radius'] = bmode; f['_card_radius'] = cmode; f['_image_radius'] = r['image'][0][0] if r['image'] else None
    f['pill buttons'] = bool(bmode and (px(bmode) or 0) >= 100)
    f['card radius 12-16px'] = bool(cmode and 12 <= (px(cmode) or 0) <= 16)
    f['card radius 8-24px'] = bool(cmode and 8 <= (px(cmode) or 0) <= 24)
    f['rounded images'] = bool(f['_image_radius'] and (px(f['_image_radius']) or 0) >= 8)
    f['_distinct_radii'] = len([x for x in r['all']])
    # effects
    sk = set(k for s, n in d.get('shadows', []) for k in shadow_kind(s))
    f['_tw_shadows'] = sorted(sk)
    f['Tailwind stock box-shadow'] = bool(sk)
    f['any gradient'] = d.get('gradients', 0) > 0
    f['radial gradient'] = d.get('radialGlow', 0) > 0
    f['backdrop blur'] = d.get('backdrop', 0) > 0
    f['blurred decorative element'] = d.get('blurDeco', 0) > 0
    f['uppercase tracked eyebrows (>=2)'] = d.get('eyebrows', 0) >= 2
    f['pill badges'] = d.get('pills', 0) >= 1
    f['emoji in copy'] = bool(d.get('emojiList'))
    f['icon tiles (>=3)'] = d.get('iconTiles', 0) >= 3
    f['equal card grid'] = d.get('cardGrids', 0) >= 1
    f['card grid with icon tiles'] = d.get('cardGridsWithTiles', 0) >= 1
    f['star ratings'] = d.get('stars', 0) >= 3
    f['hover lift/scale classes'] = d.get('classSignals', {}).get('hoverLift', 0) > 0
    f['scroll-reveal (text hidden below fold at load)'] = d.get('hiddenBelowFoldAtLoad', 0) >= 3
    tr = [x[0] for x in d.get('transitions', [])]
    f['_transitions'] = tr[:3]
    f['transition: all'] = any(x.startswith('all ') for x in tr)
    f['font awesome'] = fp.get('fontAwesome', 0) > 0
    # sections
    o = [x for x in d.get('order', [])]
    f['_order'] = o
    for k in ('testimonials', 'faq', 'pricing', 'logos', 'stats', 'how-it-works', 'cta', 'features', 'team', 'gallery', 'contact', 'about', 'blog'):
        f['section: ' + k] = k in o
    body = [x for x in o if x not in ('footer',)]
    f['closes on CTA/contact band'] = bool(body) and body[-1] in ('cta', 'contact')
    # copy
    f['_words'] = words
    f['_emdash'] = d.get('emDash', 0); f['_emdash_per_1k'] = round(1000 * d.get('emDash', 0) / words, 2)
    f['em dash in copy'] = d.get('emDash', 0) > 0
    lt = t.lower()
    f['_phrases'] = [p for p in PHRASES if re.search(r'\b' + p + r'\b', lt)]
    heads = d.get('headings', [])
    f['fragment headline ("X. Y. Z.")'] = any(re.fullmatch(r'(?:[A-Z][\w\'’-]*(?: [\w\'’-]+){0,2}\.\s*){2,4}', h.strip()) for h in heads)

    # class-based fingerprints
    cm = d.get('classMap', {}) or {}
    base = set(re.sub(r'^(?:[a-z0-9\[\]&_>=*()\'"-]+:)+', '', c) for c in cm)
    has = lambda *xs: any(x in base for x in xs)
    f['shadcn Button signature ([&_svg]:size-4 / has-[>svg])'] = any(c.startswith('[&_svg') or c.startswith('has-[>svg]') for c in cm)
    f['shadcn/Radix toast viewport shipped (md:max-w-[420px])'] = 'md:max-w-[420px]' in cm
    f['tracking-[0.2em]+ micro-label classes'] = any(re.fullmatch(r'tracking-\[0\.(1[5-9]|[2-5]\d?)em\]', c) for c in base) or has('tracking-widest')
    f['arbitrary 9-11px text (text-[10px] etc.)'] = any(re.fullmatch(r'text-\[(9|10|11)px\]', c) for c in base)
    f['crushed display leading (leading-[<=1.05] / leading-none)'] = any(re.fullmatch(r'leading-\[(0\.\d+|1(\.0[0-5]?)?)\]', c) for c in base) or has('leading-none')
    f['viewport-width display type (text-[Nvw])'] = any(re.fullmatch(r'text-\[\d+(\.\d+)?vw\]', c) for c in base)
    f['marquee animation class'] = any('marquee' in c for c in base)
    f['arrow nudge on hover (group-hover:translate-x-*)'] = any(re.fullmatch(r'-?translate-x-(0\.5|1|1\.5|2)', re.sub(r'^group-hover:', '', c)) and c.startswith('group-hover:') for c in cm)
    f['image zoom on hover (group-hover:scale-*)'] = any(re.match(r'group-hover:scale-1', c) for c in cm)
    f['hairline decorative rule (h-px / w-px / w-8 h-px)'] = has('h-px', 'w-px')
    f['text-balance'] = has('text-balance')
    f['rounded-full used'] = has('rounded-full'); f['rounded-xl/2xl used'] = has('rounded-xl', 'rounded-2xl')
    f['backdrop-blur class'] = any(c.startswith('backdrop-blur') for c in base)
    f['font-mono used for labels'] = has('font-mono') or any('Mono' in (x[0] or '') for x in d.get('faceTally', []))
    pal = set()
    for c in base:
        m = re.fullmatch(r'(?:bg|text|border|from|to|via|ring|fill|stroke|outline|divide|shadow|decoration)-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-(50|[1-9]00|950)(/\d+)?', c)
        if m: pal.add(m.group(1))
    f['_palette_families'] = sorted(pal)
    f['Tailwind default palette classes used'] = bool(pal)
    f['indigo/violet/purple default classes used'] = bool(pal & {'indigo', 'violet', 'purple'})
    f['gradient utility (bg-gradient-to-*)'] = any(c.startswith('bg-gradient-to-') or c.startswith('bg-linear-to-') for c in base)
    f['lucide icons'] = f['lucide']
    # text-based
    f['fake heritage label ("Est. 2014", "Since 1996")'] = bool(re.search(r'\b(est\.?|established|since)\s*(in\s*)?(19|20)\d\d\b', lt))
    f['numbered section labels ("01 —", "№ 01")'] = bool(re.search(r'(^|\n|\s)(№\s?)?0[1-9]\s*[—–/.:-]\s*\S', t)) or bool(re.search(r'\n0[1-9]\n', t))
    f['"The Art of" headline'] = any(re.search(r'\bthe art of\b', h.lower()) for h in heads)
    f['"Where X meets Y"'] = bool(re.search(r'\bwhere [\w\s-]{1,25} meets?\b', lt))
    f['snake_case / bracket UI labels ("OUR_STORY", "[ CONTACT ]")'] = bool(re.search(r'\b[A-Z]{2,}_[A-Z]{2,}\b', t)) or bool(re.search(r'\[\s?[A-Z][A-Z ]{2,}\s?\]', t))
    f['"Scroll" cue in hero'] = bool(re.search(r'(^|\n)\s*scroll( to (explore|discover))?( down)?\s*[↓]?\s*(\n|$)', lt))
    f['social-proof count ("4,300+ clients", "10k+")'] = bool(re.search(r'\b\d[\d,.]*\s?(k|m)?\+\s*(happy|satisfied|clients|customers|users|members|families|couples|reviews|students|businesses|teams|companies|creators|pets|patients|projects|events)', lt))
    f['rating string ("4.9/5", "5.0 ★")'] = bool(re.search(r'\b[45]\.\d\s?(/\s?5|★|stars?|rating|from)', lt))
    f['fake testimonial name "Sarah"'] = bool(re.search(r'\bsarah\b', lt))
    f['placeholder phone/address (555, 123 Main St)'] = bool(re.search(r'\b555[-.\s]\d{3,4}|\b123 [a-z]+ (st|street|ave|avenue|road|lane)\b|\(111\)|hello@example|@example\.com', lt))
    f['"Book" or "Get" + noun CTA'] = any(re.match(r'(book|get|start|schedule|request|reserve)\b', c.lower()) for c in d.get('ctas', []))

    f['_ctas'] = d.get('ctas', [])
    f['_h1'] = ty.get('h1Text')
    f['_eyebrows'] = d.get('eyebrowTexts', [])
    f['_lucide_names'] = fp.get('lucideNames', [])
    return f

av = [d for d in load(AV) if d.get('ok') and d['id'] != 'dur-obp']
ctl = [d for d in load(CTL) if d.get('ok')]
avf = {d['id']: feats(d) for d in av}; ctf = {d['id']: feats(d) for d in ctl}
bool_keys = [k for k in next(iter(avf.values())) if not k.startswith('_') and isinstance(next(iter(avf.values()))[k], (bool, type(None)))]
freq = []
for k in bool_keys:
    a = sum(1 for f in avf.values() if f.get(k)); c = sum(1 for f in ctf.values() if f.get(k))
    freq.append((k, a, len(avf), c, len(ctf)))
freq.sort(key=lambda x: -x[1])
by_tool = collections.defaultdict(list)
for d in av: by_tool[d['tool']].append(d['id'])
tool_freq = {}
for k in bool_keys:
    tool_freq[k] = {t: sum(1 for i in ids if avf[i].get(k)) for t, ids in by_tool.items()}

C = collections.Counter
def site_counter(key, src=avf):
    c = C()
    for f in src.values():
        v = f.get(key)
        if isinstance(v, list): c.update(set(map(str, v)))
        elif v is not None: c[str(v)] += 1
    return c.most_common(25)

# n-grams by site frequency
def grams(t, n):
    w = re.findall(r"[a-z][a-z'’-]*", t.lower())
    return set(' '.join(w[i:i+n]) for i in range(len(w) - n + 1))
STOP = set('the a an and or of to in for on with your our you we is are be it this that at by from as us can'.split())
ng = C(); ngc = C()
for d in av:
    for n in (2, 3, 4): ng.update(g for g in grams(d['_text'], n) if not all(x in STOP for x in g.split()))
for d in ctl:
    for n in (2, 3, 4): ngc.update(g for g in grams(d['_text'], n) if not all(x in STOP for x in g.split()))
top_ng = [(g, n, ngc.get(g, 0)) for g, n in ng.most_common(400) if n >= 8][:80]

em_av = [avf[i]['_emdash_per_1k'] for i in avf if avf[i]['_words'] >= 100]; em_ct = [ctf[i]['_emdash_per_1k'] for i in ctf if ctf[i]['_words'] >= 100]
def stats(xs):
    xs = sorted(xs); n = len(xs)
    return {'n': n, 'mean': round(sum(xs)/n, 2) if n else None, 'median': xs[n//2] if n else None, 'max': xs[-1] if n else None, 'zero': sum(1 for x in xs if x == 0)}

# global token tallies
shadow_raw = C(); radius_raw = {k: C() for k in ('button', 'card', 'input', 'image', 'badge')}; tw_cls = C(); maxw = C(); secpad = C(); trans = C(); lucide = C(); track = C()
for d in av:
    shadow_raw.update(set(s for s, n in d.get('shadows', [])))
    for k in radius_raw: radius_raw[k].update(set(x for x, n in d['radius'].get(k, [])[:2]))
    tw_cls.update(set(c for c, n in d.get('twTop', [])))
    maxw.update(set(x for x, n in d.get('maxW', [])))
    secpad.update(set(x for x, n in d.get('secPad', [])[:2]))
    trans.update(set(x for x, n in d.get('transitions', [])[:3]))
    lucide.update(set(d.get('fp', {}).get('lucideNames', [])))
hexes = C(); hexes_c = C()
for d in av: hexes.update(set(c for k in ('text', 'bg', 'buttonBg', 'border') for c, n in d['colours'][k][:6]))
for d in ctl: hexes_c.update(set(c for k in ('text', 'bg', 'buttonBg', 'border') for c, n in d['colours'][k][:6]))
ordr = C(' > '.join(x for x in f['_order']) for f in avf.values())
# pairwise transitions
pairs = C()
for f in avf.values():
    o = [x for x in f['_order'] if x != 'other']
    comp = [x for i, x in enumerate(o) if i == 0 or x != o[i-1]]
    pairs.update(set(zip(comp, comp[1:])))

out = {
 'n_av': len(avf), 'n_ctl': len(ctf), 'excluded_av': [(d['id'], d.get('words'), d.get('error')) for d in load(AV) if not d.get('ok')],
 'by_tool': {t: len(v) for t, v in by_tool.items()},
 'freq': freq, 'tool_freq': tool_freq,
 'primary_face': site_counter('_primary_face'), 'heading_face': site_counter('_heading_face'),
 'primary_face_ctl': site_counter('_primary_face', ctf), 'heading_face_ctl': site_counter('_heading_face', ctf),
 'accent': site_counter('_accent'), 'accent_hue': sorted((f['_accent_hue'], i) for i, f in avf.items() if f.get('_accent_hue') is not None),
 'button_radius': site_counter('_button_radius'), 'card_radius': site_counter('_card_radius'), 'image_radius': site_counter('_image_radius'),
 'button_radius_ctl': site_counter('_button_radius', ctf), 'card_radius_ctl': site_counter('_card_radius', ctf),
 'tw_shadows': site_counter('_tw_shadows'), 'shadow_raw': shadow_raw.most_common(15), 'radius_raw': {k: v.most_common(8) for k, v in radius_raw.items()},
 'tw_classes': tw_cls.most_common(40), 'maxw': maxw.most_common(10), 'secpad': secpad.most_common(10), 'transitions': trans.most_common(10), 'lucide': lucide.most_common(40),
 'hexes': hexes.most_common(40), 'hexes_ctl': hexes_c.most_common(20), 'tw_matches': site_counter('_tw_matches'),
 'h1_tracking_em': sorted(f['_h1_tracking_em'] for f in avf.values()), 'h1_size': sorted(f['_h1_size'] or 0 for f in avf.values()), 'body_size': sorted(f['_body_size'] or 0 for f in avf.values()),
 'order_full': ordr.most_common(), 'pairs': pairs.most_common(25),
 'phrases': site_counter('_phrases'), 'phrases_ctl': site_counter('_phrases', ctf),
 'ctas': site_counter('_ctas'), 'eyebrows': site_counter('_eyebrows'),
 'ngrams': top_ng, 'emdash_av': stats(em_av), 'emdash_ctl': stats(em_ct),
 'per_site': {i: {k: v for k, v in f.items() if k.startswith('_') and k not in ('_phrases',)} for i, f in list(avf.items()) + list(ctf.items())},
 'per_site_bool': {i: [k for k in bool_keys if f.get(k)] for i, f in list(avf.items()) + list(ctf.items())},
}
json.dump(out, sys.stdout, indent=1, default=str)
