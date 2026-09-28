# deck: skate and surf shop (idea 076), owner's brief "more edgy, Thrasher-like".
# Direction: a skate magazine cover as a shop. Black and red, a masthead as wide as the screen, flame strips drawn in CSS,
#   halftone black-and-white photos, torn photocopy edges and cover lines cut out ransom-note style.
# Why: core skate shops sell on attitude, video and team as much as product; the cover format lets the shop shout and still list widths and prices.
# Fonts: Staatliches (display, registry) + Sofia Sans Condensed 400 to 900 with italics (body). The ransom mix uses those two faces in boxes, weights and tilts.
# Palette: newsprint #F1EFE8 / black #0A0A0A / red #D7140F / white #FFFFFF / yellow #FFD400 for cover lines on black only.
# Layout idea: the home page is a magazine cover: halftone photo, masthead over it, cover lines stacked bottom left, all with core blocks in a CSS grid stack.
import sys, json, os, re, unicodedata
sys.path.insert(0, 'tools/lib')
from blocks import *
import blocks as _b
set_theme('deck')
D = THEME['dir']


def image(filename, alt, caption='', lightbox=True, href=None, **attrs):
    out = _b.image(filename, alt, caption, lightbox, href, **attrs)
    if attrs.get('aspectRatio'):
        st = 'aspect-ratio:%s;object-fit:%s' % (attrs['aspectRatio'], attrs.get('scale', 'cover'))
        out = out.replace('" alt="%s"/>' % alt, '" alt="%s" style="%s"/>' % (alt, st), 1)
    return out


def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))


def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = s.replace('.', '-')
    s = re.sub(r'[^a-z0-9 _-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')


fonts = json.load(open(os.path.join(D, '.fonts.json')))
fam = {f['slug']: f for f in fonts['fontFamilies']}
pal = lambda rows: [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]
V = lambda k, v: 'var:preset|%s|%s' % (k, v)
C = lambda s: V('color', s)
FS = lambda s: V('font-size', s)
SP = lambda s: V('spacing', s)

PALETTE = [('base', '#F1EFE8', 'Newsprint'), ('contrast', '#0A0A0A', 'Black'), ('accent', '#D7140F', 'Red'),
           ('surface', '#FFFFFF', 'White'), ('line', '#0A0A0A', 'Black line'), ('muted', '#484848', 'Photocopy grey'), ('accent-2', '#FFD400', 'Cover yellow')]


# --- CSS textures -------------------------------------------------------------
def flame_svg():
    """A strip of flame tongues hanging from a band, three layers (red, orange, yellow)."""
    W, H = 240, 64
    import random
    rnd = random.Random(7)
    def layer(depth_scale, band, color, jitter):
        x, d = 0, 'M0 0H%dV%d' % (W, band)
        pts = []
        while x < W:
            w = rnd.choice([18, 22, 26, 30])
            x1 = min(W, x + w)
            depth = band + (H - band) * depth_scale * rnd.uniform(0.55, 1.0)
            sk = rnd.uniform(-jitter, jitter)
            xm = (x + x1) / 2
            pts.append((x, x1, xm, depth, sk))
            x = x1
        d = 'M0 0H%d' % W
        for x0, x1, xm, depth, sk in reversed(pts):
            d += 'V%d C%.1f %.1f %.1f %.1f %.1f %.1f C%.1f %.1f %.1f %.1f %.1f %d' % (
                band, x1, band + (depth - band) * 0.55, xm + sk * 0.4, depth * 0.85, xm + sk, depth,
                xm - sk * 0.2, depth * 0.7, x0, band + (depth - band) * 0.35, x0, band)
        return "<path fill='%s' d='%sZ'/>" % (color, d)
    svg = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' preserveAspectRatio='none'>%s%s%s</svg>" % (
        W, H, layer(1.0, 8, '#D7140F', 10), layer(0.62, 6, '#FF6A00', 8), layer(0.32, 4, '#FFD400', 6))
    return 'url("data:image/svg+xml,%s")' % svg.replace('#', '%23').replace('"', "'")


def torn(edge='bottom', n=40, depth=10):
    import random
    rnd = random.Random(3 if edge == 'bottom' else 5)
    pts = []
    for i in range(n + 1):
        x = 100 * i / n
        y = rnd.uniform(0, depth)
        pts.append('%.2f%% calc(100%% - %.1fpx)' % (x, y) if edge == 'bottom' else '%.2f%% %.1fpx' % (100 - x, y))
    if edge == 'bottom':
        return 'polygon(0 0,100% 0,' + ','.join(reversed(pts)) + ')'
    return 'polygon(' + ','.join(pts) + ',0 100%,100% 100%)'


FLAME = flame_svg()
HALFTONE = ('&{position:relative;overflow:hidden}& img{filter:grayscale(1) contrast(1.6) brightness(1.05)}'
            '&::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(circle,rgba(10,10,10,.42) 32%,transparent 36%) 0 0/5px 5px;mix-blend-mode:multiply}')

big = {'fontFamily': V('font-family', 'display'), 'textTransform': 'uppercase'}
theme = {
 '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
 'settings': {
  'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
  'layout': {'contentSize': '720px', 'wideSize': '1400px'},
  'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE),
            'duotone': [{'slug': 'photocopy', 'colors': ['#0A0A0A', '#F1EFE8'], 'name': 'Photocopy'}, {'slug': 'red-ink', 'colors': ['#0A0A0A', '#D7140F'], 'name': 'Red ink'}]},
  'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
   'fontFamilies': [{**fam['display'], 'slug': 'display'}, {**fam['body'], 'slug': 'body'}],
   'fontSizes': [
     {'slug': 'x-small', 'size': '0.9375rem', 'name': 'Caption', 'fluid': False},
     {'slug': 'small', 'size': '1.0625rem', 'name': 'Small', 'fluid': False},
     {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
     {'slug': 'large', 'size': '1.75rem', 'name': 'Large', 'fluid': {'min': '1.4rem', 'max': '1.75rem'}},
     {'slug': 'x-large', 'size': '3.25rem', 'name': 'Section', 'fluid': {'min': '2.25rem', 'max': '3.25rem'}},
     {'slug': 'xx-large', 'size': '6rem', 'name': 'Cover line', 'fluid': {'min': '3rem', 'max': '6rem'}},
     {'slug': 'display', 'size': 'clamp(5.5rem, 31vw, 34rem)', 'name': 'Masthead', 'fluid': False}]},
  'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
     {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'}, {'slug': '30', 'size': '1rem', 'name': '3'},
     {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'}, {'slug': '50', 'size': 'clamp(1.5rem, 3.5vw, 2.5rem)', 'name': '5'},
     {'slug': '60', 'size': 'clamp(2.5rem, 5vw, 4rem)', 'name': '6'}, {'slug': '70', 'size': 'clamp(3.5rem, 8vw, 6rem)', 'name': '7'},
     {'slug': '80', 'size': 'clamp(5rem, 11vw, 9rem)', 'name': '8'}]},
  'shadow': {'defaultPresets': False, 'presets': [{'slug': 'sticker', 'name': 'Sticker', 'shadow': '4px 4px 0 var(--wp--preset--color--contrast)'}]},
  'border': {'color': True, 'radius': True, 'style': True, 'width': True, 'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}]},
  'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
 },
 'styles': {
  'color': {'background': C('base'), 'text': C('contrast')},
  'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('medium'), 'lineHeight': '1.45', 'fontWeight': '500'},
  'spacing': {'padding': {'left': SP('40'), 'right': SP('40')}, 'blockGap': SP('30')},
  'elements': {
   'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'underline'},
            ':hover': {'color': {'text': C('accent')}},
            ':focus': {'outline': {'color': C('accent'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
   'heading': {'typography': {**big, 'fontWeight': '400', 'lineHeight': '0.9', 'letterSpacing': '0.005em'}},
   'h1': {'typography': {'fontSize': FS('xx-large')}},
   'h2': {'typography': {'fontSize': FS('x-large')}},
   'h3': {'typography': {'fontSize': FS('large')}},
   'h4': {'typography': {'fontSize': FS('medium'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '900', 'fontStyle': 'italic', 'textTransform': 'uppercase', 'lineHeight': '1.1'}},
   'h5': {'typography': {'fontSize': FS('small'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '900', 'lineHeight': '1.2'}},
   'h6': {'typography': {'fontSize': FS('small'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '800', 'lineHeight': '1.2'}},
   'button': {'color': {'background': C('accent'), 'text': C('surface')}, 'border': {'radius': '0', 'width': '3px', 'style': 'solid', 'color': C('contrast')},
              'shadow': 'var:preset|shadow|sticker',
              'typography': {**big, 'fontSize': FS('large'), 'lineHeight': '1'},
              'spacing': {'padding': {'top': '0.45em', 'bottom': '0.4em', 'left': '0.8em', 'right': '0.8em'}},
              ':hover': {'color': {'background': C('contrast'), 'text': C('accent-2')}},
              ':focus': {'outline': {'color': C('accent'), 'offset': '4px', 'style': 'solid', 'width': '3px'}}},
   'caption': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '700', 'fontStyle': 'italic'}, 'color': {'text': C('contrast')}},
  },
  'blocks': {
   'core/site-title': {'typography': {**big, 'fontSize': FS('x-large'), 'lineHeight': '0.85'},
                       'color': {'text': C('accent')},
                       'elements': {'link': {'color': {'text': C('accent')}, 'typography': {'textDecoration': 'none'}}}},
   'core/navigation': {'typography': {**big, 'fontSize': FS('large'), 'lineHeight': '1'},
                       'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent-2')}}}}},
   'core/post-title': {'typography': {**big}, 'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent')}}}}},
   'core/post-date': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '900', 'textTransform': 'uppercase'}, 'color': {'text': C('accent')}},
   'core/post-terms': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '800', 'textTransform': 'uppercase'}},
   'core/image': {'border': {'radius': '0'}},
   'core/separator': {'color': {'text': C('contrast')}, 'border': {'width': '6px 0 0 0'}},
   'core/quote': {'typography': {**big, 'fontSize': FS('x-large'), 'lineHeight': '0.95'},
                  'border': {'left': {'color': C('accent'), 'width': '10px', 'style': 'solid'}}, 'spacing': {'padding': {'left': SP('40')}},
                  'elements': {'cite': {'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('small'), 'textTransform': 'none', 'fontStyle': 'italic', 'fontWeight': '800'}}}},
   'core/pullquote': {'typography': {**big, 'fontSize': FS('xx-large')}, 'border': {'top': {'width': '6px', 'style': 'solid', 'color': C('accent')}, 'bottom': {'width': '6px', 'style': 'solid', 'color': C('accent')}}},
   'core/table': {'typography': {'fontSize': FS('medium'), 'fontWeight': '600'}},
   'core/details': {'border': {'bottom': {'color': C('line'), 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}}},
   'core/query-pagination': {'typography': {**big, 'fontSize': FS('large')}},
   'core/search': {'border': {'radius': '0'}},
   'core/categories': {'typography': {**big, 'fontSize': FS('large')}},
   'core/comments': {'typography': {'fontSize': FS('small')}},
   'core/query-title': {'typography': {'fontSize': FS('xx-large')}},
   'woocommerce/product-price': {'typography': {'fontWeight': '900'}},
  },
  'css': (
   ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
   'table,.wc-block-components-product-price,.is-style-sticker{font-variant-numeric:tabular-nums}'
   ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'
   '.wp-block-table table{border-collapse:collapse;border:3px solid var(--wp--preset--color--contrast)}'
   '.wp-block-table td,.wp-block-table th{border:0;border-bottom:2px solid var(--wp--preset--color--contrast);padding:.45em .7em;text-align:left}'
   '.wp-block-table thead{border:0}.wp-block-table th{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);font-family:var(--wp--preset--font-family--display);font-weight:400;text-transform:uppercase;font-size:1.2em;letter-spacing:.02em}'
   '.wp-block-table tr:nth-child(even) td{background:var(--wp--preset--color--surface)}'
   '.wp-block-search__input{border:3px solid var(--wp--preset--color--contrast);border-radius:0}'
   '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--contrast)!important;color:var(--wp--preset--color--base)!important}'
   '.wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item__content{font-size:var(--wp--preset--font-size--x-large)}'
   '.deck-torn{clip-path:' + torn('bottom') + ';padding-bottom:calc(var(--wp--preset--spacing--70) + 12px)!important}'
   '.deck-torn-top{clip-path:' + torn('top') + ';padding-top:calc(var(--wp--preset--spacing--70) + 12px)!important}'
   '.deck-flames{position:relative}.deck-flames::after{content:"";position:absolute;left:0;right:0;top:100%;height:clamp(28px,4vw,56px);background:' + FLAME + ' 0 0/clamp(160px,18vw,300px) 100% repeat-x;pointer-events:none;z-index:2}'
   # WooCommerce
   '.wc-block-product-template{gap:var(--wp--preset--spacing--50) var(--wp--preset--spacing--30)!important}'
   '.wc-block-product-template > li{position:relative}'
   '.wc-block-product-template .wc-block-components-product-image{border:3px solid var(--wp--preset--color--contrast);background:var(--wp--preset--color--contrast)}'
   '.wc-block-product-template .wp-block-post-title{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-size:var(--wp--preset--font-size--large)!important;line-height:.95;text-align:left!important}'
   '.wc-block-product-template .wc-block-components-product-price{position:absolute;top:.6rem;right:.2rem;transform:rotate(6deg);background:var(--wp--preset--color--accent);color:var(--wp--preset--color--surface);border:3px solid var(--wp--preset--color--contrast);padding:.1em .45em;font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);box-shadow:3px 3px 0 var(--wp--preset--color--contrast);z-index:1}'
   '.wc-block-components-product-sale-badge{border-radius:0;background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--contrast);border:3px solid var(--wp--preset--color--contrast);font-family:var(--wp--preset--font-family--display)}'
   '.woocommerce div.product form.cart .button,.wc-block-components-button:not(.is-link){border-radius:0;background:var(--wp--preset--color--accent);color:var(--wp--preset--color--surface);border:3px solid var(--wp--preset--color--contrast);font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-size:1.3em;box-shadow:4px 4px 0 var(--wp--preset--color--contrast)}'
   '.wc-block-components-text-input input,.wc-block-components-select select,.woocommerce .quantity .qty{border-radius:0!important;border:3px solid var(--wp--preset--color--contrast)!important}'
   '.woocommerce-tabs .tabs{display:none}'
   '@media (max-width:600px){.is-style-cover-stack .wp-block-site-title{font-size:30vw!important}}'
  ),
 },
 'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                   {'area': 'uncategorized', 'name': 'notice', 'title': 'Contest bar'}],
 'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Deck
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A loud, magazine-cover shop theme for independent skate and surf shops with a team, a video channel and a counter to set up boards on.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: deck
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')


def variation(fname, title, rows, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)


variation('zine', 'Zine', [('base', '#E4E2DC', 'Photocopy grey'), ('contrast', '#0A0A0A', 'Black ink'), ('accent', '#0A0A0A', 'Black ink'),
    ('surface', '#FFFFFF', 'White'), ('line', '#0A0A0A', 'Black line'), ('muted', '#3E3E3E', 'Toner grey'), ('accent-2', '#FFFFFF', 'White')])
variation('beach', 'Beach', [('base', '#EFE3C6', 'Sand'), ('contrast', '#12302E', 'Deep sea'), ('accent', '#0B7A66', 'Sea green'),
    ('surface', '#FFF8E8', 'Foam'), ('line', '#12302E', 'Deep sea line'), ('muted', '#3F5652', 'Wet sand'), ('accent-2', '#FF8A3D', 'Sunset orange')])
variation('concrete-park', 'Concrete park', [('base', '#C9C8C3', 'Concrete'), ('contrast', '#121212', 'Tarmac'), ('accent', '#B23B00', 'Cone orange'),
    ('surface', '#E6E5E1', 'Fresh concrete'), ('line', '#121212', 'Coping black'), ('muted', '#3A3A38', 'Wet concrete'), ('accent-2', '#FF6A00', 'Cone')])


def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})


section('blackout', 'Blackout', ['core/group', 'core/columns'],
        {'color': {'background': C('contrast'), 'text': C('base')},
         'elements': {'link': {'color': {'text': C('accent-2')}}, 'heading': {'color': {'text': C('base')}}},
         'spacing': {'padding': {'top': SP('70'), 'bottom': SP('70'), 'left': SP('40'), 'right': SP('40')}}})
section('red', 'Red page', ['core/group', 'core/columns'],
        {'color': {'background': C('accent'), 'text': C('surface')},
         'elements': {'link': {'color': {'text': C('surface')}}, 'heading': {'color': {'text': C('surface')}},
                      'button': {'color': {'background': C('contrast'), 'text': C('surface')}}},
         'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60'), 'left': SP('40'), 'right': SP('40')}}})
section('torn', 'Torn edge (bottom)', ['core/group', 'core/columns'], {'css': '&{clip-path:%s;padding-bottom:calc(var(--wp--preset--spacing--70) + 12px)!important}' % torn('bottom')})
section('torn-top', 'Torn edge (top)', ['core/group', 'core/columns'], {'css': '&{clip-path:%s;padding-top:calc(var(--wp--preset--spacing--70) + 12px)!important}' % torn('top')})
section('halftone', 'Halftone photocopy', ['core/image', 'core/post-featured-image'], {'css': HALFTONE})
section('ransom', 'Ransom note', ['core/heading', 'core/paragraph', 'core/site-title'],
        {'typography': {**big, 'lineHeight': '1.12'},
         'css': ('& mark,& strong,& em{display:inline-block;padding:.02em .12em;margin:0 .02em;font-style:normal;line-height:1}'
                 '& mark{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);font-family:var(--wp--preset--font-family--body);font-weight:900;font-style:italic;text-transform:lowercase;transform:rotate(-2.5deg)}'
                 '& strong{background:var(--wp--preset--color--accent);color:var(--wp--preset--color--surface);font-weight:400;transform:rotate(1.8deg)}'
                 '& em{background:var(--wp--preset--color--surface);color:var(--wp--preset--color--contrast);border:3px solid var(--wp--preset--color--contrast);font-family:var(--wp--preset--font-family--body);font-weight:400;transform:rotate(-1deg)}'
                 '& mark:nth-of-type(2n){background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--contrast);transform:rotate(3deg);text-transform:uppercase;font-style:normal}'
                 '& strong:nth-of-type(2n){background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--accent-2);transform:rotate(-3deg)}')})
section('cover-stack', 'Magazine cover stack', ['core/group'],
        {'color': {'background': C('contrast'), 'text': C('surface')},
         'css': ('&{display:grid!important;grid-template:1fr/1fr;overflow:hidden}& > *{grid-area:1/1;margin:0!important;max-width:none!important}'
                 '& > .wp-block-image img{width:100%;height:min(92vh,62rem);min-height:36rem;object-fit:cover;object-position:50% 40%}'
                 '& > .wp-block-group{z-index:1;display:flex;flex-direction:column;justify-content:space-between;padding:var(--wp--preset--spacing--40)}'
                 '& p a{color:var(--wp--preset--color--accent-2);background:var(--wp--preset--color--contrast);padding:0 .25em;text-decoration:none;-webkit-box-decoration-break:clone;box-decoration-break:clone;line-height:1.5}')})
section('masthead', 'Masthead', ['core/site-title', 'core/heading'],
        {'typography': {**big, 'fontSize': FS('display'), 'lineHeight': '0.78', 'letterSpacing': '-0.01em'}, 'color': {'text': C('accent')},
         'css': '&{margin:0!important}& a{color:var(--wp--preset--color--accent)!important;-webkit-text-stroke:3px var(--wp--preset--color--contrast);paint-order:stroke fill}'})
section('sticker', 'Price sticker', ['core/paragraph'],
        {'color': {'background': C('accent'), 'text': C('surface')}, 'typography': {**big, 'fontSize': FS('large'), 'lineHeight': '1'},
         'border': {'width': '3px', 'style': 'solid', 'color': C('contrast')}, 'shadow': 'var:preset|shadow|sticker',
         'css': '&{display:inline-block;padding:.12em .4em!important;transform:rotate(-4deg)}'})
section('grip', 'Grip tape', ['core/group', 'core/columns'],
        {'color': {'background': C('contrast'), 'text': C('base')},
         'elements': {'link': {'color': {'text': C('base')}}, 'heading': {'color': {'text': C('accent-2')}}},
         'spacing': {'padding': {'top': SP('50'), 'bottom': SP('50'), 'left': SP('40'), 'right': SP('40')}},
         'css': '&{background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.4px),radial-gradient(rgba(255,255,255,.06) 1px,transparent 1.4px);background-size:4px 4px,7px 7px;background-position:0 0,2px 3px}'})
section('tape', 'Taped note', ['core/group', 'core/paragraph'],
        {'color': {'background': C('surface'), 'text': C('contrast')}, 'border': {'width': '3px', 'style': 'solid', 'color': C('contrast')},
         'spacing': {'padding': {'top': SP('40'), 'bottom': SP('40'), 'left': SP('40'), 'right': SP('40')}},
         'css': '&{transform:rotate(-.8deg);position:relative}&::before{content:"";position:absolute;top:-14px;left:40%;width:110px;height:28px;background:rgba(255,212,0,.75);transform:rotate(-4deg)}'})

section('rows', 'Ruled rows (instead of a table)', ['core/group'],
        {'css': ('& > .wp-block-group{border-bottom:3px solid var(--wp--preset--color--contrast);padding:.55em 0!important;margin:0!important;column-gap:1rem!important;row-gap:.2rem!important}'
                 '& > .wp-block-group:first-child{border-top:6px solid var(--wp--preset--color--contrast)}'
                 '& > .wp-block-group > p{margin:0!important}'
                 '& > .wp-block-group > p:first-child{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-size:var(--wp--preset--font-size--large);line-height:1}')})
section('rows-inverse', 'Ruled rows on black', ['core/group'],
        {'css': ('& > .wp-block-group{border-bottom:3px solid var(--wp--preset--color--accent);padding:.55em 0!important;margin:0!important;column-gap:1rem!important}'
                 '& > .wp-block-group > p{margin:0!important}'
                 '& > .wp-block-group > p:first-child{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-size:var(--wp--preset--font-size--large);color:var(--wp--preset--color--accent-2);line-height:1}')})


def rows(items, min_w='8rem', cls='is-style-rows', **kw):
    n = max(len(r) for r in items)
    return group(J(*[group(J(*[para(c) for c in r]), layout={'type': 'grid', 'columnCount': n, 'minimumColumnWidth': min_w}) for r in items]),
                 className=cls, layout={'type': 'default'}, **kw)


# ---------------------------------------------------------------- content
SHOP = {'name': 'Coping', 'addr': '22 Gloucester Road, Brighton BN1 4AD', 'email': 'shop@example.com', 'phone': '01273 496 0552'}
ALT = {
 'venice-grind.jpg': 'Black and white photo of a skater grinding the coping of a concrete bowl, palm trees behind',
 'kickflip.jpg': 'A skater mid-kickflip on a city pavement in front of iron railings',
 'couch-ollie.jpg': 'A skater ollies over a pink skateboard in a graffiti-covered room with a sofa',
 'bowl.jpg': 'An empty concrete skate bowl covered in graffiti, trees around it',
 'rail.jpg': 'A flat rail and a concrete bank at an outdoor skatepark',
 'road.jpg': 'A skater pushing down the middle of an empty road through a pine forest',
 'deck-wall.jpg': 'A stack of brightly painted skateboard decks with cartoon graphics',
 'complete-green.jpg': 'A green and black complete skateboard with silver trucks and white wheels, from above',
 'complete-black.jpg': 'A black complete skateboard with yellow wheels on a tiled floor',
 'carry.jpg': 'A man in a denim jacket carrying a patterned longboard past a white fence',
 'surf.jpg': 'A surfer riding the face of a green wave at sunset',
 'surfboards.jpg': 'A rack of colourful surfboards standing outside a surf shop',
 'sunset-board.jpg': 'A skateboard resting on a car roof against a pink sunset sky',
}

# name, image, category, price, stock, short, specs rows
P = [
 ('Coping shop deck, 8.0in, free grip', 'deck-wall.jpg', 'Decks', '55', 12, 'Our own deck. 8.0in wide, 31.6in long, 14.25in wheelbase. Free black grip, fitted if you ask.',
  [('Width', '8.0in'), ('Length', '31.6in'), ('Wheelbase', '14.25in'), ('Concave', 'Medium'), ('Grip', 'Free, fitted in store')]),
 ('Coping shop deck, 8.5in, free grip', 'kickflip.jpg', 'Decks', '55', 8, '8.5in, for bowls and bigger feet. Free grip.',
  [('Width', '8.5in'), ('Length', '32.1in'), ('Wheelbase', '14.5in'), ('Concave', 'Medium'), ('Grip', 'Free, fitted in store')]),
 ('Beginner complete, 7.75in, green', 'complete-green.jpg', 'Completes', '85', 6, 'Set up and ready. Good for riders from about age 10 and UK shoe size 4 up.',
  [('Deck', '7.75in maple'), ('Trucks', '129mm'), ('Wheels', '52mm, 99a'), ('Bearings', 'Standard, pre-greased'), ('Suits', 'Age 10 and up')]),
 ('Street complete, 8.0in, black', 'complete-black.jpg', 'Completes', '110', 5, 'A proper street setup, assembled by us before it leaves the shop.',
  [('Deck', '8.0in shop deck'), ('Trucks', '139mm'), ('Wheels', '53mm, 101a'), ('Bearings', 'Swiss-style'), ('Hardware', '7/8in')]),
 ('Kids complete, 7.25in', 'complete-green.jpg', 'Completes', '65', 4, 'Shorter and narrower for small feet. Ages 5 to 9.',
  [('Deck', '7.25in, 28in long'), ('Trucks', '114mm'), ('Wheels', '50mm, 95a'), ('Suits', 'Ages 5 to 9')]),
 ('Undercarriage kit, 139 trucks and 53mm wheels', 'rail.jpg', 'Undercarriage', '95', 10, 'Everything under an 8.0 to 8.25in deck: trucks, wheels, bearings, bolts. We fit it free.',
  [('Trucks', '139mm, fits 8.0 to 8.25in'), ('Wheels', '53mm, 99a'), ('Bearings', '8 plus spacers'), ('Bolts', '7/8in Allen')]),
 ('Undercarriage kit, 149 trucks and 56mm wheels', 'bowl.jpg', 'Undercarriage', '105', 7, 'For 8.5in decks and transition. Softer, bigger wheels for rough concrete.',
  [('Trucks', '149mm, fits 8.4 to 8.6in'), ('Wheels', '56mm, 95a'), ('Bearings', '8 plus spacers'), ('Bolts', '1in Allen')]),
 ('Cruiser longboard, 36in', 'carry.jpg', 'Completes', '120', 3, 'For getting along the seafront. Soft wheels, loose trucks.',
  [('Length', '36in'), ('Wheels', '65mm, 78a'), ('Trucks', '180mm reverse kingpin')]),
 ('Mid-length surfboard, 7ft 2in', 'surfboards.jpg', 'Surf', '420', 2, 'Easy paddling for Brighton\'s small days. Fins and leash included.',
  [('Length', '7ft 2in'), ('Volume', '48 litres'), ('Fins', '2+1 set included'), ('Leash', 'Included')]),
 ('Surf wax, pack of 3', 'surf.jpg', 'Surf', '7.50', 40, 'Cool water wax for the Channel, April to November.', [('Temperature', 'Cool, 14 to 19C'), ('Count', '3 bars')]),
 ('Coping flame tee', 'couch-ollie.jpg', 'Clothing', '25', 30, 'Heavy black cotton, red flame print front and back, printed in Hove.', [('Fabric', '240gsm cotton'), ('Fit', 'Boxy, size down if between')]),
]


def purl(p):
    return '/product/%s/' % slugify(p[0])


def spec(p):
    return table([[k, v] for k, v in p[6]])


def rn(words, boxed=False):
    """Ransom-note heading text: wrap words in mark/strong/em in turn, leaving some plain (or none when boxed, for use on photos)."""
    out, tags = [], (['mark', 'strong', 'em', 'mark', 'em', 'strong'] if boxed else ['mark', None, 'strong', 'em', None, 'mark', 'strong', None, 'em'])
    for i, w in enumerate(words.split(' ')):
        t = tags[i % len(tags)]
        out.append('<%s>%s</%s>' % (t, w, t) if t else w)
    return ' '.join(out)


# ---------------------------------------------------------------- patterns
pattern('cover', 'Magazine cover (home hero)', 'featured,banner', group(J(
  image('venice-grind.jpg', ALT['venice-grind.jpg'], lightbox=False, className='is-style-halftone'),
  group(J(
    dyn('site-title', level=1, className='is-style-masthead', isLink=False),
    group(J(
      heading(rn('Free grip on every deck', True), 2, className='is-style-ransom', fontSize='x-large'),
      heading(rn('Which trucks fit your deck', True), 2, className='is-style-ransom', fontSize='x-large'),
      para('<a href="/nia-campbell-brighton-part/">Nia Campbell\'s new part is up</a>. <a href="/events/">Bowl jam, Saturday 11 October</a>.', fontSize='large', textColor='accent-2')),
      layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'left'}, style={'spacing': {'blockGap': SP('30')}})),
    layout={'type': 'default'})),
  className='is-style-cover-stack', align='full', layout={'type': 'default'}),
  description='The home hero as a skate magazine cover: halftone photo, masthead over it, ransom-note cover lines.')

pattern('flame-bar', 'Flame bar', 'banner', group(para(rn('Open till 7 Thursday'), className='is-style-ransom', fontSize='large'), className='is-style-blackout deck-flames', align='full', layout={'type': 'constrained'},
  style={'spacing': {'padding': {'top': SP('40'), 'bottom': SP('40')}}}))


def deck_tile(p, i):
    return group(J(
        image(p[1], ALT[p[1]], href=purl(p), aspectRatio='2/3', scale='cover'),
        para('£%s' % p[3], className='is-style-sticker'),
        heading('<a href="%s">%s</a>' % (purl(p), p[0]), 3, fontSize='large')),
        layout={'type': 'default'}, style={'spacing': {'blockGap': SP('20')}})


pattern('deck-wall', 'New decks wall (6 across)', 'shop,featured', group(J(
  heading(rn('New on the wall'), 2, className='is-style-ransom'),
  para('Every deck comes with free grip. Tell us at the till and we fit it while you wait, usually ten minutes.', fontSize='large'),
  group(J(*[deck_tile(P[i], i) for i in [0, 1, 2, 3, 7, 4]]), align='wide', layout={'type': 'grid', 'columnCount': 6, 'minimumColumnWidth': '9rem'},
        style={'spacing': {'blockGap': SP('30')}})),
  align='full', className='is-style-grip deck-torn', layout={'type': 'constrained'}),
  description='A tight wall of decks with red price stickers, on a grip-tape texture.')

pattern('truck-size-guide', 'Truck size guide (deck width to truck)', 'shop,featured', columns(
  ('45%', J(heading(rn('Which trucks fit your deck'), 2, className='is-style-ransom'),
     para('Your truck axle should be about the same width as your deck, give or take a quarter inch. Too narrow and it feels twitchy; too wide and the wheels stick out and catch.'),
     para('Not sure? Bring the deck in. We will measure it and hold the trucks against it.', fontSize='small'),
     buttons(('Shop undercarriage kits', '/product-category/undercarriage/')))),
  (None, rows([['7.25 to 7.5in', '114 to 129mm trucks', '50 to 52mm wheels'], ['7.75 to 8.0in', '129 to 139mm trucks', '52 to 54mm wheels'], ['8.0 to 8.25in', '139mm trucks', '53 to 55mm wheels'],
                ['8.25 to 8.5in', '144 to 149mm trucks', '54 to 56mm wheels'], ['8.5 to 9.0in', '149 to 159mm trucks', '56 to 58mm wheels']])),
  align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  description='The signature: deck width matched to truck axle width and wheel size, linked to the undercarriage kits.')

pattern('undercarriage-kits', 'Undercarriage kits', 'shop', group(J(
  heading(rn('First setup kits'), 2, className='is-style-ransom'),
  para('Trucks, wheels, bearings and bolts in one box, matched to a deck width. We fit them free, and we show you how, so you can do it next time.'),
  columns(*[(None, J(image(P[i][1], ALT[P[i][1]], href=purl(P[i]), aspectRatio='4/3', scale='cover', className='is-style-halftone'),
                     heading('<a href="%s">%s</a>' % (purl(P[i]), P[i][0]), 3), para(P[i][5]), para('£%s' % P[i][3], className='is-style-sticker'))) for i in [5, 6]], align='wide')),
  align='wide', layout={'type': 'default'}))

pattern('completes-kids', 'Completes and a note on sizes for kids', 'shop', columns(
  (None, J(heading('What size for my kid', 3),
     rows([['7.25in', 'Ages 5 to 9, shoe size up to 3'], ['7.75in', 'Ages 10 to 13, shoe size 4 to 7'], ['8.0in and up', 'Teenagers and adults']]),
     para('Wider is more stable, narrower is easier to flip. When in doubt, go a size up; they grow.', fontSize='small'))),
  (None, J(image('complete-green.jpg', ALT['complete-green.jpg'], href=purl(P[2]), aspectRatio='4/3', scale='cover'),
     heading('<a href="%s">Beginner complete, £85</a>' % purl(P[2]), 3), para('Ready to ride out of the door. Helmets and pads are on the <a href="/completes/">completes page</a>.'))), align='wide'))

TEAM = [('Nia Campbell', 'Regular', 'Street, the Level and anything with a ledge', 'kickflip.jpg'),
        ('Jonny Kerr', 'Goofy', 'Bowl, rides for the shop since 2016', 'venice-grind.jpg'),
        ('Sol Rivera', 'Regular', 'Surf in winter, transition in summer', 'surf.jpg'),
        ('Aisha Brown', 'Goofy', 'Tricks off the couch, mostly', 'couch-ollie.jpg')]
pattern('team', 'Team riders', 'about,featured', group(J(
  heading(rn('The shop team'), 2, className='is-style-ransom'),
  group(J(*[group(J(image(f, 'Team rider %s skating' % n, aspectRatio='3/4', scale='cover', className='is-style-halftone'),
                    heading(n, 3), para('%s. %s.' % (s, d), fontSize='small')), layout={'type': 'default'}) for n, s, d, f in TEAM]),
        align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '11rem'})),
  align='full', className='is-style-blackout', layout={'type': 'constrained'}),
  description='Riders in halftone with stance and what they skate.')

pattern('free-grip-note', 'Free grip note', 'shop', para('<strong>Free grip on every deck.</strong> Pick black or clear. We fit it at the counter; bring the deck back any time for a re-grip at £5.', className='is-style-tape'))
pattern('setup-note', 'We set it up for you', 'shop', group(J(
  heading('We set it up for you', 4),
  para('Buy a deck and parts online and pick them up assembled. Choose "collect from the shop" at checkout and give us a day. Online orders to post arrive assembled too, unless you tick the box to leave them in parts.')),
  className='is-style-tape', layout={'type': 'default'}))

pattern('video-archive', 'Video archive (latest posts)', 'posts,query,featured', group(J(
  row(J(heading(rn('Shop videos'), 2, className='is-style-ransom'), para('<a href="/category/videos/">Every video</a>', fontSize='large')), justify='space-between', align='wide'),
  query(J(dyn('post-featured-image', isLink=True, aspectRatio='16/9', scale='cover', className='is-style-halftone'), dyn('post-date'), dyn('post-title', isLink=True, level=3, fontSize='large')),
        per_page=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '15rem'}, align='wide')),
  align='full', className='is-style-red deck-torn', layout={'type': 'constrained'}))

pattern('events', 'Events and contests', 'text', J(
  heading(rn('Next up'), 2, className='is-style-ransom'),
  rows([['Sat 11 Oct', '<strong>Bowl jam</strong>', 'Hove Lagoon bowl, 1pm. Under-16s at 1, open at 3. Free.'],
         ['Thu 23 Oct', '<strong>Video night</strong>', 'The shop, 7pm. New team part and three old ones. Bring a chair.'],
         ['Sun 2 Nov', '<strong>Learn to skate</strong>', 'The Level, 10am. Ages 7 to 12, boards and pads lent. £12.'],
         ['Sat 29 Nov', '<strong>Best trick, flat bar</strong>', 'Outside the shop, 2pm. Prize is a deck and a setup.']], min_w='9rem'),
  para('<a href="/events/">Contests, results and the learn-to-skate dates</a>', fontSize='large')))

pattern('notice-contest', 'Notice: contest day', 'banner', group(para('Bowl jam this Saturday, Hove Lagoon, 1pm. Shop closes at 12 so we can all go. Take this bar out on Sunday.', fontSize='large'),
  className='is-style-red', align='full', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}}}),
  description='A red bar for contest days. Edit it, then remove it.')

pattern('visit', 'Visit the shop', 'contact', columns(
  (None, image('deck-wall.jpg', ALT['deck-wall.jpg'], aspectRatio='4/3', scale='cover')),
  (None, J(heading(rn('Come by the shop'), 2, className='is-style-ransom'),
     para('%s. Two minutes from the Level, five from the station. There is a flat bar outside that the council keeps asking about.' % SHOP['addr']),
     rows([['Mon', 'Closed'], ['Tue, Wed, Fri', '11am to 6pm'], ['Thu', '11am to 7pm'], ['Sat', '10am to 6pm'], ['Sun', '11am to 4pm']]),
     para('<a href="tel:012734960552">%s</a>, <a href="mailto:%s">%s</a>' % (SHOP['phone'], SHOP['email'], SHOP['email'])))), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}))

pattern('about', 'About the shop', 'about', group(J(
  heading(rn('Since 2009, same street'), 2, className='is-style-ransom'),
  para('Tariq Hussain opened Coping in a lock-up behind Gloucester Road with forty decks and a borrowed drill. Lou Okafor runs the surf side from the back room, where the wetsuits drip into a bath.'),
  para('We skate everything we sell. We stock the shop brands we would ride and our own decks, pressed in Portugal. We do not sell toy boards from supermarkets, and we will tell you if the board you brought in is one.'),
  quote('Tariq set up my first board and told me to come back when I could ollie the kerb outside. Took three weeks.', 'Aisha Brown, team rider since 2022')),
  className='is-style-tape', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('shipping', 'Shipping and returns', 'shop', J(
  heading('Post and returns', 2),
  table([['UK, decks and completes', '£6.50', '2 to 3 days'], ['UK, parts and clothing', '£3.50', '2 to 3 days'], ['Surfboards', 'Collect only', 'We will not post boards']], head=['What', 'Cost', 'Time']),
  para('Unridden and unassembled goods can come back within 28 days. Once grip is on a deck, it is yours.')))

pattern('surf-corner', 'Surf corner', 'shop', columns(
  ('55%', image('surf.jpg', ALT['surf.jpg'], aspectRatio='16/10', scale='cover')),
  (None, J(heading(rn('Surf out back'), 2, className='is-style-ransom'),
     para('Boards, wax, leashes and a few second-hand wetsuits in the back room. Lou does board rental on flat-ish days from the seafront hut by the West Pier.'),
     buttons(('See the surf stock', '/product-category/surf/')))), align='wide', className='is-style-blackout'))

pattern('workshop-prices', 'Workshop price list', 'shop,services', J(
  heading(rn('Counter jobs'), 2, className='is-style-ransom'),
  table([['Grip a deck', 'Free with a new deck, £5 otherwise'], ['Set up a complete from parts', 'Free with parts bought here, £10 otherwise'],
         ['Clean and re-lube bearings', '£6 a set'], ['Swap bushings', '£4 plus bushings'], ['Wax and fin swap on a surfboard', '£8']], head=['Job', 'Price']),
  para('Most jobs are done while you wait. Busy Saturdays, leave it and come back after lunch.', fontSize='small')))

pattern('trade-in', 'Board trade-in', 'shop', group(J(
  heading('Trade in your old board', 3),
  para('Bring in a complete you have outgrown and we take £15 off a new one. Old boards get cleaned up and go to the Saturday learn-to-skate sessions at the Level.')),
  className='is-style-tape', layout={'type': 'default'}))

pattern('pads-note', 'Helmets and pads', 'shop', columns(
  (None, J(heading('Helmets and pads', 3), para('Under-16s at our sessions wear a helmet, no arguments. We stock helmets from £35 and knee pads from £25, and you can try them on in the shop.'))),
  (None, image('bowl.jpg', ALT['bowl.jpg'], aspectRatio='16/10', scale='cover', className='is-style-halftone')), align='wide'))

pattern('surf-rental', 'Surf rental prices', 'shop', J(
  heading('Surf rental', 3),
  table([['Soft-top board, 2 hours', '£15'], ['Board and wetsuit, 2 hours', '£25'], ['Full day, board and wetsuit', '£45']], head=['What', 'Price']),
  para('From the hut by the West Pier, April to October. Book by phone the day before if the forecast looks good.', fontSize='small')))


# ---------------------------------------------------------------- round 2: riders
RIDERS = [
 ('nia-campbell', 'Nia Campbell', 'Regular', 'kickflip.jpg', '8.25 shop deck, 144 trucks, 53mm 101a wheels', 'Street. The Level ledges, the seafront rails and anything the council has not skate-stopped yet.', 'Started on a supermarket board in 2015, rode for the shop from 2019. Works Saturdays on the counter.'),
 ('jonny-kerr', 'Jonny Kerr', 'Goofy', 'venice-grind.jpg', '8.5 shop deck, 149 trucks, 56mm 95a wheels', 'Bowl and anything with coping. Hove Lagoon most evenings.', 'Rides for the shop since 2016. Films and edits most of our videos on a camera older than some of the team.'),
 ('sol-rivera', 'Sol Rivera', 'Regular', 'surf.jpg', '8.0 shop deck, 139 trucks, 54mm 99a wheels; 7ft 2in mid-length when it is on', 'Transition in summer, surf in winter. Pushes long distances for fun.', 'Teaches the Sunday learn-to-skate sessions at the Level and runs our surf rental hut.'),
 ('aisha-brown', 'Aisha Brown', 'Goofy', 'couch-ollie.jpg', '8.0 shop deck, 139 trucks, 52mm 101a wheels', 'Flat ground, manuals, and a lot of tricks in small rooms.', 'Joined the team in 2022 after learning to ollie the kerb outside the shop. Filmed her last part entirely indoors.'),
]


def rider_profile(r):
    slug, name, stance, img, setup, skates, bio = r
    return columns(
      ('45%', image(img, 'Team rider %s skating, black and white' % name, aspectRatio='3/4', scale='cover', className='is-style-halftone')),
      (None, J(heading(rn(name + ' rides ' + stance.lower()), 2, className='is-style-ransom'),
         para(bio, fontSize='large'),
         rows([['Stance', stance], ['Skates', skates], ['Setup', setup]], min_w='7rem'),
         buttons(('See %s\'s setup in the shop' % name.split()[0], '/product-category/decks/')))),
      align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}})


for _r in RIDERS:
    pattern('rider-profile-' + _r[0].split('-')[0], 'Rider profile: ' + _r[1], 'team', rider_profile(_r),
            description='One team rider: halftone photo, stance, what they skate and their board setup.')
pattern('rider-setup', 'Rider setup, part by part', 'team', group(J(
  heading(rn('What Jonny rides'), 3, className='is-style-ransom'),
  rows([['Deck', 'Coping shop deck, 8.5in, medium concave'], ['Trucks', '149mm, tightened a quarter turn past loose'], ['Wheels', '56mm, 95a, for rough concrete'],
        ['Bearings', 'Swiss-style, cleaned when they squeak'], ['Grip', 'Black, cut with a razor at the counter']])),
  className='is-style-blackout', layout={'type': 'default'}), description='A rider\'s board setup listed part by part.')
pattern('rider-quote', 'Rider quote', 'team', group(quote('Hove Lagoon at 7am before the scooters wake up. That is the whole secret.', 'Jonny Kerr, team rider since 2016'),
  className='is-style-red', layout={'type': 'constrained'}))
pattern('team-grid-query', 'Team riders (latest posts in Team)', 'team,query', group(J(
  heading(rn('Meet the team'), 2, className='is-style-ransom'),
  query(J(dyn('post-featured-image', isLink=True, aspectRatio='3/4', scale='cover', className='is-style-halftone'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=14, fontSize='small')),
        per_page=4, category=None, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '11rem'}, align='wide')),
  align='wide', layout={'type': 'default'}), inserter=True)
pattern('tour-dates', 'Team trips and tour dates', 'team,events', group(J(
  heading(rn('On the road'), 2, className='is-style-ransom'),
  rows([['18 to 20 Oct', '<strong>Bristol</strong>', 'Team trip. Filming at Lloyds and the Mound, demo at Skate and Ride on Saturday afternoon.'],
        ['8 Nov', '<strong>London</strong>', 'Southbank session with the Hackney shops. Meet at 11 by the undercroft.'],
        ['22 Nov', '<strong>Portsmouth</strong>', 'Bowl jam at the Southsea skatepark. Train from Brighton at 9.08, group ticket if you tell us by Thursday.']], min_w='9rem')),
  className='is-style-blackout', align='full', layout={'type': 'constrained'}), description='Team trips and demos with dates and where to meet.')

# ---------------------------------------------------------------- round 2: videos
pattern('video-hero', 'Video part hero (still and credits)', 'videos,banner', group(J(
  image('stairs.jpg', 'Still from a video part: a skater flips down a set of stairs under trees', aspectRatio='16/9', scale='cover', className='is-style-halftone', align='wide'),
  row(J(heading(rn('Nia Campbell, Brighton part'), 2, className='is-style-ransom'), para('4 min 12 s', className='is-style-sticker')), justify='space-between', align='wide')),
  align='wide', layout={'type': 'default'}), description='The opening of a video post: a still, the title and the running time.')
pattern('video-credits', 'Video credits', 'videos', rows([['Filmed', 'Jonny Kerr, on a VX1000 and a phone'], ['Edited', 'Jonny Kerr, over four evenings'],
  ['Music', 'Two tracks from Brighton bands, used with permission'], ['Spots', 'The Level, the Madeira Drive rails, Hove Lagoon, a car park we will not name'], ['Premiere', 'Coping, Thursday 23 October, 7pm']]),
  description='Who filmed, edited and scored a part, and where it was filmed.')
pattern('video-stills', 'Video stills (lightbox gallery)', 'videos,gallery', gallery([
  ('kickflip.jpg', 'Still: kickflip on a pavement in front of railings', 'Madeira Drive'), ('rail.jpg', 'Still: the flat rail at the Level', 'The Level'),
  ('bowl.jpg', 'Still: the graffiti-covered bowl', 'Hove Lagoon'), ('stairs.jpg', 'Still: a flip down stairs under trees', 'Preston Park steps')], columns=4, align='wide', className='is-style-halftone'),
  description='Four stills from a part. Click any to open it large.')
pattern('video-tracklist', 'Video part tracklist and clips', 'videos', group(J(
  heading(rn('In this part'), 3, className='is-style-ransom'),
  lst(['Opening line down Madeira Drive, three rails in one push', 'The Level ledge, switch crooked to fakie', 'Hove Lagoon, frontside air over the hip', 'Ender: the Preston Park steps, second try after the first went through a hedge'], ordered=True)),
  className='is-style-tape', layout={'type': 'default'}))
pattern('video-night', 'Video night call-out', 'videos,events', columns(
  (None, J(heading(rn('Video night at the shop'), 2, className='is-style-ransom'), para('Thursday 23 October, 7pm. The new part on the wall, three old ones from the tape box, crisps from the corner shop. Free, but bring a chair.', fontSize='large'),
     buttons(('See all events', '/events/')))),
  (None, image('couch-ollie.jpg', ALT['couch-ollie.jpg'], aspectRatio='4/3', scale='cover', className='is-style-halftone')), align='full', className='is-style-red'))

# ---------------------------------------------------------------- round 2: completes and products
COMPLETES = [
 ('Beginner complete, 7.75in', 'complete-green.jpg', '£85', ['7.75in maple deck', '129mm trucks', '52mm, 99a wheels', 'Standard bearings', 'Free black grip'], P[2]),
 ('Street complete, 8.0in', 'complete-black.jpg', '£110', ['8.0in shop deck', '139mm trucks', '53mm, 101a wheels', 'Swiss-style bearings', '7/8in hardware'], P[3]),
 ('Kids complete, 7.25in', 'complete-green.jpg', '£65', ['7.25in deck, 28in long', '114mm trucks', '50mm, 95a wheels', 'For ages 5 to 9'], P[4]),
 ('Cruiser, 36in', 'cruiser-wall.jpg', '£120', ['36in deck', '180mm reverse kingpin trucks', '65mm, 78a soft wheels', 'For the seafront'], P[7]),
]
pattern('shop-built-completes', 'Shop-built completes (with parts lists)', 'shop', group(J(
  heading(rn('Built at the counter'), 2, className='is-style-ransom'),
  para('Every complete is put together by one of us, checked, and ridden round the shop floor before it goes out.', fontSize='large'),
  group(J(*[group(J(image(img, name + ' complete skateboard', href=purl(pp), aspectRatio='4/3', scale='cover'),
                    row(J(heading('<a href="%s">%s</a>' % (purl(pp), name), 3), para(price, className='is-style-sticker')), justify='space-between'),
                    lst(parts, fontSize='small')), layout={'type': 'default'}) for name, img, price, parts, pp in COMPLETES]),
        align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}, style={'spacing': {'blockGap': SP('40')}})),
  align='wide', layout={'type': 'default'}), description='Completes with the parts list for each, built in the shop.')
pattern('build-steps', 'How we build your board', 'shop', group(J(
  heading(rn('How we build it'), 2, className='is-style-ransom'),
  lst(['Grip goes on first, cut with a fresh blade and filed at the edge.', 'Holes punched from underneath with a screwdriver, so the grip does not tear.', 'Trucks on with the kingpins facing in, bolts tightened in a cross.', 'Bearings pressed in with the truck axle, spacers in, nuts a quarter turn back.', 'Ridden across the shop floor. If it pulls to one side, we start again.'], ordered=True, fontSize='large')),
  className='is-style-grip', align='full', layout={'type': 'constrained'}))
pattern('sale-rack', 'Sale rack (was and now)', 'shop,drops', group(J(
  heading(rn('Sale rack'), 2, className='is-style-ransom'),
  group(J(*[group(J(image(img, alt, aspectRatio='3/4', scale='cover'), heading(name, 3, fontSize='large'), para(price, className='is-style-sticker')), layout={'type': 'default'}) for img, alt, name, price in [
     ('carry.jpg', ALT['carry.jpg'], 'Last year\'s cruiser, 34in', 'Was £110, now £75'), ('complete-black.jpg', ALT['complete-black.jpg'], 'Shop-worn street complete', 'Was £110, now £80'),
     ('surfboards.jpg', ALT['surfboards.jpg'], 'Ex-rental soft-top, 8ft', 'Was £220, now £120'), ('couch-ollie.jpg', ALT['couch-ollie.jpg'], 'Flame tee, misprints', 'Was £25, now £12')]]),
        align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '11rem'})),
  align='wide', layout={'type': 'default'}), description='Reduced stock with the old and new price on a sticker.')
pattern('drop-announce', 'Drop announcement', 'drops,banner', group(J(
  heading(rn('New shop decks drop Saturday 10am'), 2, className='is-style-ransom', fontSize='xx-large'),
  para('Three graphics, 8.0, 8.25 and 8.5. Forty of each. In the shop at 10, online at 12, one per person on the day.', fontSize='large'),
  buttons(('See the decks', '/product-category/decks/'))),
  className='is-style-red deck-torn', align='full', layout={'type': 'constrained'}), description='Announce a limited release: what, when, how many and the rules.')
pattern('drop-rules', 'Drop day rules', 'drops', group(J(
  heading('Drop day, in plain words', 4),
  lst(['Queue on Gloucester Road, not across the shop door.', 'One of each graphic per person.', 'Online goes live two hours after the shop opens, so locals get first go.', 'Anything left on Monday goes on the wall at the normal price.'])),
  className='is-style-tape', layout={'type': 'default'}))
pattern('gift-card', 'Gift cards', 'shop', columns(
  (None, J(heading(rn('Gift cards'), 2, className='is-style-ransom'), para('£20, £50 or £100. Spend it on a deck, a setup, a wetsuit rental or a learn-to-skate session. Never runs out.', fontSize='large'))),
  (None, image('deck-wall.jpg', ALT['deck-wall.jpg'], aspectRatio='16/10', scale='cover')), align='wide', className='is-style-grip'))

# ---------------------------------------------------------------- round 2: spots
SPOTS = [('The Level', 'Park, ledges and a flat bar. Busy after school, empty at 8am.', 'rail.jpg'),
         ('Hove Lagoon bowl', 'Concrete bowl by the water, rough surface, bring soft wheels.', 'bowl.jpg'),
         ('Madeira Drive', 'Seafront rails and long flat runs. Wind from the west makes it hard work.', 'kickflip.jpg'),
         ('Preston Park steps', 'Nine stairs under the trees. The park keeper is nice if you are.', 'stairs.jpg')]
pattern('spot-guide', 'Local spot guide', 'spots', group(J(
  heading(rn('Where to skate in Brighton'), 2, className='is-style-ransom'),
  group(J(*[group(J(image(img, name + ', a Brighton skate spot', aspectRatio='4/3', scale='cover', className='is-style-halftone'), heading(name, 3), para(note, fontSize='small')), layout={'type': 'default'}) for name, note, img in SPOTS]),
        align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'})),
  align='wide', layout={'type': 'default'}), description='Local spots with a photo and a line of advice each.')
pattern('spot-map', 'Spot map (numbered list over a map field)', 'spots', columns(
  ('55%', group(J(*[para('<strong>%s</strong> %s' % (n, where)) for n, where in [('The Level', 'five minutes north of the shop'), ('Hove Lagoon', '25 minutes west along the front'), ('Madeira Drive', 'east of the pier'), ('Preston Park', 'ten minutes up the London Road'), ('Shoreham', 'the long push, 7 miles west')]]),
               className='is-style-rows deck-map', layout={'type': 'default'})),
  (None, J(heading(rn('Spot map'), 2, className='is-style-ransom'), para('All within a push or a bus ride of the shop. Ask at the counter for today\'s conditions; we know which ones are wet.', fontSize='large'),
     para('<a href="https://www.openstreetmap.org/#map=13/50.8300/-0.1400">Open the area in OpenStreetMap</a>'))),
  align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}), description='A list of spots on a map-grid background, with a link to OpenStreetMap.')
pattern('spot-etiquette', 'Spot etiquette', 'spots', group(J(
  heading(rn('Do not get us kicked out'), 3, className='is-style-ransom'),
  lst(['Take your rubbish with you, including the tape.', 'If someone asks you to move, move. Come back later.', 'No wax on the war memorial, ever.', 'Little kids at the park get the ramps first before 10am.'])),
  className='is-style-tape', layout={'type': 'default'}))

# ---------------------------------------------------------------- round 2: zine and lookbook
pattern('zine-cover', 'Zine cover', 'zine,banner', group(J(
  dyn('site-title', level=0, className='is-style-masthead', isLink=False),
  heading(rn('Issue 14 out now'), 2, className='is-style-ransom', fontSize='xx-large'),
  para('Twenty-eight pages, photocopied in the back room. Free with any deck, £2 on its own.', fontSize='large')),
  className='is-style-red deck-torn', align='full', layout={'type': 'constrained'}), description='The cover of the shop zine: masthead, issue line, price.')
pattern('zine-spread', 'Zine spread (photo, text, pull quote)', 'zine', columns(
  ('55%', image('sunset-park.jpg', 'A skater on the coping of a concrete park at sunset, silhouetted', aspectRatio='4/3', scale='cover', className='is-style-halftone')),
  (None, J(heading(rn('Ten years of the Lagoon bowl'), 2, className='is-style-ransom'),
     para('The bowl went in with council money and a lot of letters from parents. Jonny was there the day they poured it and still has the concrete splash on his trainers to prove it.'),
     pullquote('Nobody asked for it to be this rough. It is perfect.', 'Jonny Kerr'))),
  align='wide', style={'spacing': {'blockGap': {'left': SP('50')}}}), description='An inside spread from the zine.')
pattern('zine-issues', 'Back issues of the zine', 'zine,shop', group(J(
  heading(rn('Back issues'), 2, className='is-style-ransom'),
  group(J(*[group(J(image(img, 'Cover of zine issue %d' % n, aspectRatio='3/4', scale='cover', className='is-style-halftone'), heading('Issue %d' % n, 3), para(t, fontSize='small')), layout={'type': 'default'}) for n, img, t in [
     (14, 'sunset-park.jpg', 'Ten years of the Lagoon bowl, Nia\'s part in stills'), (13, 'road.jpg', 'Pushing to Shoreham, a map of every kerb'),
     (12, 'couch-ollie.jpg', 'Indoor tricks, Aisha\'s flat'), (11, 'venice-grind.jpg', 'The Bristol trip, in photocopies')]]),
        align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '11rem'})),
  align='wide', layout={'type': 'default'}), description='A grid of past zine covers.')
pattern('lookbook', 'Lookbook (big photos, lightbox)', 'gallery,shop', J(
  heading(rn('Autumn in the shop'), 2, className='is-style-ransom', align='wide'),
  gallery([('stairs.jpg', 'Flame tee on a skater mid-flip down stairs', 'Flame tee, black'), ('carry.jpg', ALT['carry.jpg'], 'Denim, cruiser, no socks'),
           ('sunset-park.jpg', 'Silhouette in the park at sunset', 'The last session'), ('cruiser-wall.jpg', 'A cruiser leaning on a white wall', 'Cruiser, 36in')], columns=2, align='wide')),
  description='Large lookbook photos in pairs. Click to open.')
pattern('photo-wall', 'Photo wall (halftone gallery)', 'gallery', gallery([
  ('venice-grind.jpg', ALT['venice-grind.jpg'], ''), ('kickflip.jpg', ALT['kickflip.jpg'], ''), ('bowl.jpg', ALT['bowl.jpg'], ''),
  ('road.jpg', ALT['road.jpg'], ''), ('stairs.jpg', 'A skater flips down stairs under trees', ''), ('sunset-park.jpg', 'A skater in a concrete park at sunset', '')], columns=3, align='full', className='is-style-halftone'))

# ---------------------------------------------------------------- round 2: contests, stockists, extras
pattern('contest-results', 'Contest results', 'events', group(J(
  heading(rn('Best trick results'), 2, className='is-style-ransom'),
  rows([['First', 'Kai Doherty, 14', 'Kickflip backside lipslide, flat bar. Wins a deck and a setup.'],
        ['Second', 'Maya Osei, 12', 'Frontside boardslide to fakie. Wins a shop deck.'],
        ['Third', 'Leo Brandt, 16', 'Tre flip over the bar. Wins a flame tee.']], min_w='8rem')),
  className='is-style-blackout', align='full', layout={'type': 'constrained'}), description='Placings, names and prizes from a contest.')
pattern('contest-entry', 'Contest entry details', 'events', columns(
  (None, J(heading(rn('Enter the best trick'), 2, className='is-style-ransom'), para('Saturday 29 November, 2pm, on the flat bar outside the shop. Sign up at the counter, free. Under-16s and open. Helmets for under-16s.', fontSize='large'))),
  (None, group(J(heading('Rules', 4), lst(['Three tries each in the first round.', 'Best trick wins, judged by the team.', 'Land it clean or it does not count.', 'Be nice to the neighbours.'])), className='is-style-tape', layout={'type': 'default'})), align='wide'))
STOCK = [('Brighton', 'Coping, 22 Gloucester Road', 'All widths'), ('Hastings', 'Seafront Surf and Skate, George Street', '8.0 and 8.25'),
         ('Worthing', 'Board Room, Montague Street', '8.25 and 8.5'), ('Lewes', 'Harvey\'s Yard pop-up, Saturdays', 'Whatever is left')]
pattern('stockists', 'Stockists of our decks', 'stockists', group(J(
  heading(rn('Where to find our decks'), 2, className='is-style-ransom'),
  rows([[t, '<strong>%s</strong>' % w, sz] for t, w, sz in STOCK], min_w='9rem'),
  para('Want our decks in your shop? Email <a href="mailto:%s?subject=Stocking%%20Coping%%20decks">%s</a>. Minimum order is ten.' % (SHOP['email'], SHOP['email']))),
  align='wide', layout={'type': 'default'}), description='Other shops that carry the shop\'s own decks.')
pattern('faq', 'Questions people ask at the counter', 'text', group(J(
  heading(rn('Asked at the counter'), 2, className='is-style-ransom'),
  details('Can you re-grip my old deck?', para('Yes, £5, while you wait. Bring it clean.')),
  details('What size deck for my kid?', para('Look at the size note on the completes page, or bring them in and let them stand on a few.')),
  details('Do you fix surfboards?', para('Small dings, yes, in about a week. Snapped boards, no.')),
  details('Can I pay in instalments?', para('Not online. In the shop we can hold a deck for two weeks with a £20 deposit.'))),
  align='wide', layout={'type': 'constrained', 'justifyContent': 'left'}))
pattern('reviews', 'Named customer notes', 'testimonials', group(J(
  heading(rn('Overheard at the till'), 2, className='is-style-ransom'),
  columns(*[(None, quote(q, c)) for q, c in [('Sol set up my son\'s board and gave him a ten-minute lesson on the pavement outside. He has not stopped since.', 'Rachel, Kemptown, October 2025'),
     ('Cheapest re-grip in town and they did it while I drank a coffee next door.', 'Dev, Hove, August 2025'),
     ('Told me not to buy the expensive bearings. Respect.', 'Marta, Moulsecoomb, May 2025')]], align='wide')),
  align='wide', layout={'type': 'default'}))
pattern('crew-signup', 'Crew email sign-up', 'call-to-action', group(J(
  heading(rn('Get the crew email'), 2, className='is-style-ransom'),
  para('One email a month: drops, contests, new videos. Nothing else.', fontSize='large'),
  buttons(('Email us to join', 'mailto:%s?subject=Crew%%20email' % SHOP['email']))),
  className='is-style-grip', align='full', layout={'type': 'constrained'}))
pattern('hero-red', 'Hero: red cover with a deck', 'banner', columns(
  (None, J(heading(rn('Fresh shop decks'), 1, className='is-style-ransom', fontSize='xx-large'), para('8.0, 8.25 and 8.5. Free grip. Fitted while you wait.', fontSize='large'), buttons(('See the decks', '/product-category/decks/')))),
  (None, image('deck-wall.jpg', ALT['deck-wall.jpg'], aspectRatio='4/3', scale='cover')), align='full', className='is-style-red', verticalAlignment='center'),
  description='An alternative hero for a page or a drop: red field, ransom headline, one photo.')

pattern('post-grid', 'Video grid (inherits query)', 'posts,query', inherit_query(
  J(dyn('post-featured-image', isLink=True, aspectRatio='16/9', scale='cover', className='is-style-halftone'), dyn('post-date'), dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', excerptLength=20)),
  layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}, align='wide'), inserter=False)
pattern('post-list', 'Results list', 'posts,query', inherit_query(
  group(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-date')), layout={'type': 'default'}, style={'border': {'bottom': {'color': C('line'), 'width': '3px', 'style': 'solid'}}}), align='wide'), inserter=False)

# pages
pattern('page-truck-guide', 'Page: truck size guide', 'shop', J(pattern_ref('truck-size-guide'), pattern_ref('undercarriage-kits'), pattern_ref('completes-kids'), pattern_ref('pads-note'), pattern_ref('trade-in'), pattern_ref('setup-note')), block_types='core/post-content')
pattern('page-team', 'Page: team', 'about', J(pattern_ref('team'), pattern_ref('rider-quote'), pattern_ref('tour-dates'), pattern_ref('about')), block_types='core/post-content')
pattern('page-completes', 'Page: completes', 'shop', J(pattern_ref('shop-built-completes'), pattern_ref('build-steps'), pattern_ref('completes-kids'), pattern_ref('pads-note'), pattern_ref('gift-card')), block_types='core/post-content')
pattern('page-spots', 'Page: spot guide', 'spots', J(pattern_ref('spot-map'), pattern_ref('spot-guide'), pattern_ref('spot-etiquette'), pattern_ref('photo-wall')), block_types='core/post-content')
pattern('page-zine', 'Page: zine', 'zine', J(pattern_ref('zine-cover'), pattern_ref('zine-spread'), pattern_ref('zine-issues'), pattern_ref('lookbook')), block_types='core/post-content')
pattern('page-drops', 'Page: drops and sale', 'drops', J(pattern_ref('drop-announce'), pattern_ref('drop-rules'), pattern_ref('sale-rack'), pattern_ref('crew-signup')), block_types='core/post-content')
pattern('page-stockists', 'Page: stockists', 'stockists', J(pattern_ref('stockists'), pattern_ref('reviews'), pattern_ref('faq')), block_types='core/post-content')
pattern('page-events', 'Page: events', 'events', J(pattern_ref('events'), pattern_ref('contest-entry'), pattern_ref('contest-results'), pattern_ref('video-night'), pattern_ref('flame-bar')), block_types='core/post-content')
pattern('page-visit', 'Page: visit', 'contact', J(pattern_ref('visit'), pattern_ref('workshop-prices'), pattern_ref('surf-corner'), pattern_ref('surf-rental'), pattern_ref('shipping')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(
  row(J(dyn('site-title', level=0, className='is-style-ransom'),
        dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile', textColor='base', style={'spacing': {'blockGap': SP('40')}})),
      justify='space-between', align='wide', wrap=False),
  tag='header', align='full', className='is-style-blackout deck-flames', layout={'type': 'constrained'},
  style={'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}}}))
write('parts/notice.html', pattern_ref('notice-contest'))
write('parts/footer.html', group(J(
  dyn('site-title', level=0, className='is-style-masthead', textAlign='center'),
  columns(
    (None, J(heading('Shop', 4), para('%s<br>Tue to Sat from 11, Thu till 7, Sun 11 to 4<br><a href="tel:012734960552">%s</a>' % (SHOP['addr'], SHOP['phone'])))),
    (None, J(heading('Help', 4), para('<a href="/truck-size-guide/">Truck size guide</a><br><a href="/completes/">Completes and kids\' sizes</a><br><a href="/visit/">Post and returns</a><br><a href="/stockists/">Stockists</a><br><a href="mailto:%s">%s</a>' % (SHOP['email'], SHOP['email'])))),
    (None, J(heading('Read and watch', 4), para('<a href="/category/videos/">Team videos</a><br><a href="/category/team/">The riders</a><br><a href="/zine/">The zine</a><br><a href="/drops/">Drops and sale</a><br><a href="/news/">Shop news</a>'))),
    align='wide'),
  para('Demo photographs are CC0 and public domain images from Wikimedia Commons and Unsplash, used as stand-ins.', fontSize='x-small', align='wide')),
  tag='footer', align='full', className='is-style-blackout deck-torn-top', layout={'type': 'constrained'},
  style={'spacing': {'margin': {'top': '0'}}}))


# ---------------------------------------------------------------- templates
def main(inner, pad_top='70', **kw):
    return group(inner, tag='main', style={'spacing': {'padding': {'top': SP(pad_top), 'bottom': SP('80')}}}, layout={'type': 'constrained'}, **kw)


def tpl(name, inner):
    write('templates/%s.html' % name, J(template_part('header', 'header'), inner, template_part('footer', 'footer')))


tpl('front-page', group(J(pattern_ref('cover'), pattern_ref('deck-wall'), pattern_ref('drop-announce'), pattern_ref('truck-size-guide'), pattern_ref('team'),
    pattern_ref('video-archive'), pattern_ref('spot-guide'), pattern_ref('events'), pattern_ref('zine-cover'), pattern_ref('visit')), tag='main', layout={'type': 'constrained'},
    style={'spacing': {'blockGap': SP('70'), 'padding': {'bottom': SP('80')}}}))
tpl('page', main(J(dyn('post-title', level=1, className='is-style-ransom'), dyn('post-content', layout={'type': 'constrained'}))))
tpl('page-wide', main(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1400px'}))))
tpl('single', main(J(dyn('post-featured-image', align='wide', aspectRatio='16/9', scale='cover', className='is-style-halftone'), dyn('post-date'), dyn('post-title', level=1),
    dyn('post-content', layout={'type': 'constrained'}), dyn('post-terms', term='category', prefix='Filed under '),
    row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)), justify='space-between', align='wide'))))
tpl('home', main(J(heading(rn('Shop news'), 1, align='wide', className='is-style-ransom'), dyn('categories', className='is-style-ransom'), pattern_ref('post-grid'))))
tpl('category-videos', main(J(heading(rn('Shop videos'), 1, align='wide', className='is-style-ransom'), para('Parts, raw files and trips, filmed by the team. New ones premiere at the shop first.', fontSize='large', align='wide'), pattern_ref('post-grid'))))
tpl('category-team', main(J(heading(rn('The team'), 1, align='wide', className='is-style-ransom'), para('Four riders, all regulars at the counter. Click through for their setups and parts.', fontSize='large', align='wide'),
    inherit_query(J(dyn('post-featured-image', isLink=True, aspectRatio='3/4', scale='cover', className='is-style-halftone'), dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', excerptLength=16, fontSize='small')),
                  layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}, align='wide'))))
tpl('index', main(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-grid'))))
tpl('archive', main(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('post-grid'))))
tpl('search', main(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='8.25, bearings, wax', buttonText='Search'), pattern_ref('post-list'))))
tpl('404', main(J(heading(rn('Bailed on this one'), 1, className='is-style-ransom'), para('That page is gone. Try the <a href="/shop/">shop</a>, the <a href="/truck-size-guide/">truck guide</a> or search.'),
    dyn('search', label='Search', showLabel=False, placeholder='8.25, bearings, wax', buttonText='Search'))))


def product_collection(per_page=16, cols=4):
    q = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'product', 'order': 'desc', 'orderBy': 'date', 'search': '', 'exclude': [],
         'inherit': True, 'taxQuery': {}, 'isProductCollectionBlock': True, 'woocommerceOnSale': False,
         'woocommerceStockStatus': ['instock', 'outofstock', 'onbackorder'], 'woocommerceAttributes': [], 'woocommerceHandPickedProducts': []}
    a = {'queryId': 0, 'query': q, 'tagName': 'div', 'displayLayout': {'type': 'flex', 'columns': cols, 'shrinkColumns': True},
         'dimensions': {'widthType': 'fill'}, 'queryContextIncludes': ['collection'], 'align': 'wide'}
    tmpl = J(dyn('woocommerce/product-image', showSaleBadge=True, imageSizing='single', isDescendentOfQueryLoop=True, aspectRatio='3/4', scale='cover'),
             dyn('post-title', level=2, isLink=True, __woocommerceNamespace='woocommerce/product-collection/product-title'),
             dyn('woocommerce/product-price', isDescendentOfQueryLoop=True))
    return ('<!-- wp:woocommerce/product-collection %s -->\n<div class="wp-block-woocommerce-product-collection alignwide">'
            '<!-- wp:woocommerce/product-template -->\n%s\n<!-- /wp:woocommerce/product-template -->\n\n'
            '<!-- wp:query-pagination {"layout":{"type":"flex","justifyContent":"center"}} -->\n<!-- wp:query-pagination-previous /-->\n\n<!-- wp:query-pagination-numbers /-->\n\n<!-- wp:query-pagination-next /-->\n<!-- /wp:query-pagination -->\n\n'
            '<!-- wp:woocommerce/product-collection-no-results -->\n%s\n<!-- /wp:woocommerce/product-collection-no-results --></div>\n<!-- /wp:woocommerce/product-collection -->') % (
        json.dumps(a, separators=(',', ':')), tmpl, para('Sold out on this rack. Ring the shop, there might be one in the back.'))


cat_row = row(J(*[para('<a href="/product-category/%s/">%s</a>' % (slugify(n), n), className='is-style-sticker') for n in ['Decks', 'Completes', 'Undercarriage', 'Surf', 'Clothing']]),
              style={'spacing': {'blockGap': SP('30')}}, align='wide')
for name in ('archive-product', 'taxonomy-product_cat', 'product-search-results'):
    tpl(name, main(J(dyn('woocommerce/store-notices'), dyn('query-title', type='archive', showPrefix=False, align='wide', className='is-style-ransom'), cat_row,
                     dyn('term-description', align='wide'), product_collection()), pad_top='70'))

tpl('single-product', main(J(
  dyn('woocommerce/store-notices'),
  columns(('50%', dyn('woocommerce/product-image', showProductLink=False, showSaleBadge=True, imageSizing='single', isDescendentOfSingleProductTemplate=True, aspectRatio='3/4', scale='cover')),
          (None, J(dyn('post-title', level=1, fontSize='x-large', __woocommerceNamespace='woocommerce/product-query/product-title'),
                   dyn('woocommerce/product-price', isDescendentOfSingleProductTemplate=True, fontSize='x-large'),
                   dyn('post-excerpt', __woocommerceNamespace='woocommerce/product-query/product-summary'),
                   dyn('woocommerce/add-to-cart-form'),
                   pattern_ref('free-grip-note'),
                   dyn('woocommerce/product-details'))),
          align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  pattern_ref('truck-size-guide')), pad_top='70'))

print('deck built:', len(os.listdir(os.path.join(D, 'patterns'))), 'patterns')

# ---------------------------------------------------------------- demo
VIDEOS = [
 ('Nia Campbell, Brighton part', 'stairs.jpg', ['Four minutes, filmed over one summer between the Level and the seafront. Nia wanted every trick on a spot you can reach by bus from the shop, and she got close.',
   'The ender took two sessions. The first try went through a hedge. The second is in the part.'],
   [['Filmed', 'Jonny Kerr, VX1000 and a phone'], ['Edited', 'Jonny Kerr'], ['Music', 'Two tracks by a Brighton band, with permission'], ['Length', '4 min 12 s'], ['Premiere', 'Coping, Thursday 23 October, 7pm']], True),
 ('Jonny Kerr at Hove Lagoon, raw files', 'venice-grind.jpg', ['Twelve minutes of unedited bowl runs, slams included. No music, just wheels on concrete and the odd gull.',
   'Filmed over three mornings at 7am, before the scooters wake up.'],
   [['Filmed', 'Sol Rivera, from the deck of the bowl'], ['Edited', 'Not really'], ['Length', '12 min'], ['Spot', 'Hove Lagoon bowl']], False),
 ('Couch session with Aisha', 'couch-ollie.jpg', ['Aisha filmed a whole part in her flat during the rain in March. Manuals down the hall, ollies over the sofa, a kickflip into the kitchen that her landlord has not seen.',
   'The couch did not survive. The part did.'],
   [['Filmed', 'Aisha Brown and her flatmate Remi'], ['Music', 'Remi, on a keyboard from a charity shop'], ['Length', '2 min 40 s'], ['Spot', 'A flat in Moulsecoomb']], True),
 ('Pushing to Shoreham and back', 'road.jpg', ['Sol pushed a cruiser along the coast road to Shoreham and back, 14 miles. We filmed from a bike. It took most of a Sunday and two stops for chips.',
   'If you want to try it, go west in the morning so the wind is behind you on the way home.'],
   [['Filmed', 'Jonny Kerr, from a borrowed bike'], ['Board', 'Cruiser, 36in, 65mm 78a wheels'], ['Distance', '14 miles'], ['Length', '6 min']], False),
]
RIDER_POSTS = [
 ('Nia Campbell', 'kickflip.jpg', 'nia', ['Nia is the one behind the counter on Saturdays, fitting grip and arguing about wheel sizes. Her new part premieres on 23 October.']),
 ('Jonny Kerr', 'venice-grind.jpg', 'jonny', ['Jonny has ridden for the shop since 2016 and films most of what we put out. If you see a man in a bowl with a camera on a stick, say hello.']),
 ('Sol Rivera', 'surf.jpg', 'sol', ['Sol runs the learn-to-skate sessions at the Level on Sundays and the surf rental hut in summer. Good at explaining things slowly.']),
 ('Aisha Brown', 'couch-ollie.jpg', 'aisha', ['Aisha learned to ollie on the kerb outside the shop and joined the team two years later. She skates flat ground and small rooms better than anyone we know.']),
]
posts = []
for title, img, paras_, credits, stills in VIDEOS:
    posts.append({'title': title, 'category': 'videos', 'image': img, 'excerpt': paras_[0][:140].rsplit(' ', 1)[0] + '.', 'content': J(
        *[para(t) for t in paras_], heading('Credits', 2), rows(credits), pattern_ref('video-stills') if stills else pattern_ref('video-tracklist'), pattern_ref('video-night'))})
for name, img, key, paras_ in RIDER_POSTS:
    posts.append({'title': name, 'category': 'team', 'image': img, 'excerpt': paras_[0], 'content': J(*[para(t) for t in paras_], pattern_ref('rider-profile-' + key), pattern_ref('rider-quote') if key == 'jonny' else pattern_ref('tour-dates'))})
posts += [
  {'title': 'Our own decks are back from the press', 'category': 'shop-news', 'image': 'deck-wall.jpg', 'content': J(
     para('Two widths, 8.0 and 8.5, pressed in Portugal from seven-ply maple. Forty of each graphic, free grip, fitted at the counter.'), pattern_ref('drop-rules'), pattern_ref('lookbook'))},
  {'title': 'Winter surf days, what we rent and when', 'category': 'shop-news', 'image': 'surf.jpg', 'content': J(
     para('Board rental from the seafront hut runs until the end of October, then by appointment. Winter wetsuits are 5/4, and we have eight to lend.'), pattern_ref('surf-rental'), pattern_ref('surf-corner'))},
]
demo = {
 'site': {'title': 'Coping', 'tagline': 'Skate and surf, Gloucester Road, Brighton'},
 'categories': [{'slug': 'videos', 'name': 'Videos', 'description': 'Parts, raw files and trips filmed by the team.'}, {'slug': 'team', 'name': 'Team', 'description': 'The four riders who skate for the shop.'}, {'slug': 'shop-news', 'name': 'Shop news'}],
 'front_page': 'home', 'posts_page': 'news',
 'pages': [
  {'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'news', 'title': 'News', 'content': ''},
  {'slug': 'completes', 'title': 'Completes', 'pattern': 'deck/page-completes', 'template': 'page-wide'},
  {'slug': 'truck-size-guide', 'title': 'Truck size guide', 'pattern': 'deck/page-truck-guide', 'template': 'page-wide'},
  {'slug': 'team', 'title': 'About the team', 'pattern': 'deck/page-team', 'template': 'page-wide'},
  {'slug': 'events', 'title': 'Events', 'pattern': 'deck/page-events', 'template': 'page-wide'},
  {'slug': 'spots', 'title': 'Spot guide', 'pattern': 'deck/page-spots', 'template': 'page-wide'},
  {'slug': 'zine', 'title': 'Zine', 'pattern': 'deck/page-zine', 'template': 'page-wide'},
  {'slug': 'drops', 'title': 'Drops and sale', 'pattern': 'deck/page-drops', 'template': 'page-wide'},
  {'slug': 'stockists', 'title': 'Stockists', 'pattern': 'deck/page-stockists', 'template': 'page-wide'},
  {'slug': 'visit', 'title': 'Visit', 'pattern': 'deck/page-visit', 'template': 'page-wide'},
 ],
 'posts': posts,
 'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'Completes', 'url': '/completes/'}, {'label': 'Truck guide', 'url': '/truck-size-guide/'},
         {'label': 'Team', 'url': '/category/team/'}, {'label': 'Videos', 'url': '/category/videos/'}, {'label': 'Events', 'url': '/events/'},
         {'label': 'Spots', 'url': '/spots/'}, {'label': 'Zine', 'url': '/zine/'}, {'label': 'Drops', 'url': '/drops/'}, {'label': 'Visit', 'url': '/visit/'}],
 'currency': 'GBP',
 'products': [{'name': p[0], 'price': p[3], 'image': p[1], 'category': p[2], 'sku': 'CPG-%d' % (200 + i), 'stock': p[4], 'short': p[5],
               'description': J(para(p[5]), spec(p))} for i, p in enumerate(P)],
}
os.makedirs('demos/deck', exist_ok=True)
json.dump(demo, open('demos/deck/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
