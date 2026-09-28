# stem: florist (idea 077), owner's brief "more style and colour heavy".
# Direction: colour-blocked still lifes. Every bouquet sits on its own saturated field (poppy, marigold, cobalt, mint, petal pink),
#   like a seasonal paper backdrop in a studio shoot, and the type is a fat flared serif set big and tight like a flower-market poster.
# Why: the owner wants style and colour; the research's service rules (cut-off, zones, substitutions, subscriptions) stay in plain words on every product.
# Fonts: Chonburi (display, claimed: Alice was too gentle for the brief) + Rethink Sans 400 to 800 (body). Two families.
# Palette: petal pink #FFE3EA / aubergine #2B0B1E / poppy #D6281F / marigold #FFC72C / cobalt #1D4ED8 / mint #BFEBD6 / leaf #1F6B3A.
# Layout idea: the same-day cut-off is the home headline, and bouquets are shown two across, each on a different colour field with name, size and price in one line.
import sys, json, os, re, unicodedata
sys.path.insert(0, 'tools/lib')
from blocks import *
import blocks as _b
set_theme('stem')
D = THEME['dir']


def image(filename, alt, caption='', lightbox=True, href=None, **attrs):
    out = _b.image(filename, alt, caption, lightbox, href, **attrs)
    if attrs.get('aspectRatio'):
        st = 'aspect-ratio:%s;object-fit:%s' % (attrs['aspectRatio'], attrs.get('scale', 'cover'))
        out = out.replace('" alt="%s"/>' % alt, '" alt="%s" style="%s"/>' % (alt, st), 1)
    return out


def columns(*cols, **attrs):
    """Like blocks.columns, but a column may be (width, inner, {column attrs})."""
    out = []
    for c in cols:
        w, inner = c[0], c[1]
        ca = dict(c[2]) if len(c) > 2 else {}
        if w:
            ca = {'width': w, **ca}
        cls = 'wp-block-column' + ((' ' + ca['className']) if ca.get('className') else '')
        st = (' style="flex-basis:%s"' % w) if w else ''
        out.append('<!-- wp:column%s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:column -->' % (_b._a(ca), cls, st, inner))
    return '<!-- wp:columns%s -->\n<div class="%s">%s</div>\n<!-- /wp:columns -->' % (_b._a(attrs), _b._cls('wp-block-columns', attrs), '\n\n'.join(out))


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

PALETTE = [('base', '#FFE3EA', 'Petal pink'), ('contrast', '#2B0B1E', 'Aubergine'), ('accent', '#C4221B', 'Poppy'),
           ('surface', '#FFC72C', 'Marigold'), ('line', '#2B0B1E', 'Aubergine line'), ('muted', '#6A2E4C', 'Dried rose'),
           ('accent-2', '#1D4ED8', 'Cobalt'), ('mint', '#BFEBD6', 'Mint'), ('leaf', '#1F6B3A', 'Leaf'), ('cream', '#FFF6E9', 'Cream')]

theme = {
 '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
 'settings': {
  'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
  'layout': {'contentSize': '700px', 'wideSize': '1360px'},
  'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE)},
  'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
   'fontFamilies': [{**fam['display'], 'slug': 'display'}, {**fam['body'], 'slug': 'body'}],
   'fontSizes': [
     {'slug': 'x-small', 'size': '0.9375rem', 'name': 'Small print', 'fluid': False},
     {'slug': 'small', 'size': '1.0625rem', 'name': 'Small', 'fluid': False},
     {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
     {'slug': 'large', 'size': '1.625rem', 'name': 'Large', 'fluid': {'min': '1.3125rem', 'max': '1.625rem'}},
     {'slug': 'x-large', 'size': '2.75rem', 'name': 'Section', 'fluid': {'min': '1.875rem', 'max': '2.75rem'}},
     {'slug': 'xx-large', 'size': '4.75rem', 'name': 'Poster', 'fluid': {'min': '2.75rem', 'max': '4.75rem'}},
     {'slug': 'display', 'size': '7.5rem', 'name': 'Display', 'fluid': {'min': '3.5rem', 'max': '7.5rem'}}]},
  'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
     {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'}, {'slug': '30', 'size': '1rem', 'name': '3'},
     {'slug': '40', 'size': 'clamp(1.25rem, 2.5vw, 2rem)', 'name': '4'}, {'slug': '50', 'size': 'clamp(1.75rem, 4vw, 3rem)', 'name': '5'},
     {'slug': '60', 'size': 'clamp(2.5rem, 6vw, 5rem)', 'name': '6'}, {'slug': '70', 'size': 'clamp(3.5rem, 8vw, 7rem)', 'name': '7'},
     {'slug': '80', 'size': 'clamp(5rem, 12vw, 10rem)', 'name': '8'}]},
  'shadow': {'defaultPresets': False, 'presets': []},
  'border': {'color': True, 'radius': True, 'style': True, 'width': True,
             'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}, {'slug': 'pill', 'size': '999px', 'name': 'Pill'}, {'slug': 'arch', 'size': '50% 50% 0 0 / 30% 30% 0 0', 'name': 'Arch'}]},
  'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
 },
 'styles': {
  'color': {'background': C('base'), 'text': C('contrast')},
  'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('medium'), 'lineHeight': '1.55'},
  'spacing': {'padding': {'left': SP('40'), 'right': SP('40')}, 'blockGap': SP('30')},
  'elements': {
   'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'underline'},
            ':hover': {'color': {'text': C('accent')}},
            ':focus': {'outline': {'color': C('accent-2'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
   'heading': {'typography': {'fontFamily': V('font-family', 'display'), 'fontWeight': '400', 'lineHeight': '0.98', 'letterSpacing': '-0.015em'}},
   'h1': {'typography': {'fontSize': FS('display')}},
   'h2': {'typography': {'fontSize': FS('xx-large')}},
   'h3': {'typography': {'fontSize': FS('large'), 'lineHeight': '1.1'}},
   'h4': {'typography': {'fontSize': FS('medium'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '800', 'letterSpacing': '0'}},
   'h5': {'typography': {'fontSize': FS('small'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '800', 'letterSpacing': '0'}},
   'h6': {'typography': {'fontSize': FS('small'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '700', 'letterSpacing': '0'}},
   'button': {'color': {'background': C('contrast'), 'text': C('base')}, 'border': {'radius': '999px', 'width': '0', 'style': 'solid'},
              'typography': {'fontFamily': V('font-family', 'body'), 'fontWeight': '800', 'fontSize': FS('small')},
              'spacing': {'padding': {'top': '0.85em', 'bottom': '0.85em', 'left': '1.6em', 'right': '1.6em'}},
              ':hover': {'color': {'background': C('accent'), 'text': C('cream')}},
              ':focus': {'outline': {'color': C('accent-2'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
   'caption': {'typography': {'fontSize': FS('x-small')}, 'color': {'text': C('contrast')}},
  },
  'blocks': {
   'core/site-title': {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('x-large'), 'lineHeight': '1', 'letterSpacing': '-0.02em'},
                       'elements': {'link': {'color': {'text': C('base')}, 'typography': {'textDecoration': 'none'}}}},
   'core/navigation': {'typography': {'fontSize': FS('small'), 'fontWeight': '700'},
                       'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
   'core/post-title': {'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent')}}}}},
   'core/post-date': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '700'}, 'color': {'text': C('muted')}},
   'core/post-terms': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '700'}},
   'core/image': {'border': {'radius': '0'}},
   'core/separator': {'color': {'text': C('accent')}, 'border': {'width': '4px 0 0 0'}},
   'core/quote': {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('x-large'), 'lineHeight': '1.05'},
                  'border': {'width': '0'}, 'spacing': {'padding': {'left': '0'}},
                  'elements': {'cite': {'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('small'), 'fontStyle': 'normal', 'fontWeight': '700'}}}},
   'core/pullquote': {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('xx-large')}, 'border': {'width': '0'}},
   'core/table': {'typography': {'fontSize': FS('small')}},
   'core/details': {'border': {'bottom': {'color': C('line'), 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}},
                    'typography': {'fontWeight': '500'}},
   'core/query-pagination': {'typography': {'fontWeight': '800'}},
   'core/search': {'border': {'radius': '999px'}},
   'core/categories': {'typography': {'fontWeight': '800'}},
   'core/comments': {'typography': {'fontSize': FS('small')}},
   'core/query-title': {'typography': {'fontSize': FS('xx-large')}},
   'woocommerce/product-price': {'typography': {'fontWeight': '800'}},
  },
  'css': (
   ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
   'table,.wc-block-components-product-price,.is-style-price-line{font-variant-numeric:tabular-nums}'
   ':focus-visible{outline:3px solid var(--wp--preset--color--accent-2);outline-offset:3px}'
   '.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:0;border-bottom:2px solid currentColor;padding:.6em .8em .6em 0;text-align:left}'
   '.wp-block-table thead{border:0}.wp-block-table th{font-weight:800}'
   '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:999px;padding-left:1em}'
   '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--accent-2)!important;color:var(--wp--preset--color--base)!important}'
   '.wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item__content{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large)}'
   '.is-style-still-life img{mix-blend-mode:normal}'
   # WooCommerce
   '.wc-block-product-template{gap:var(--wp--preset--spacing--50) var(--wp--preset--spacing--40)!important}'
   '.wc-block-product-template > li:nth-child(5n+1) .wc-block-components-product-image{background:var(--wp--preset--color--surface)}'
   '.wc-block-product-template > li:nth-child(5n+2) .wc-block-components-product-image{background:var(--wp--preset--color--accent-2)}'
   '.wc-block-product-template > li:nth-child(5n+3) .wc-block-components-product-image{background:var(--wp--preset--color--mint)}'
   '.wc-block-product-template > li:nth-child(5n+4) .wc-block-components-product-image{background:var(--wp--preset--color--accent)}'
   '.wc-block-product-template > li:nth-child(5n) .wc-block-components-product-image{background:var(--wp--preset--color--leaf)}'
   '.wc-block-product-template .wc-block-components-product-image{padding:var(--wp--preset--spacing--40)}'
   '.wc-block-product-template .wp-block-post-title{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large)!important;text-align:left!important;line-height:1.05}'
   '.wc-block-product-template .wc-block-components-product-price{text-align:left!important}'
   '.wc-block-components-product-sale-badge{border-radius:999px;background:var(--wp--preset--color--accent);color:var(--wp--preset--color--cream);border:0}'
   '.woocommerce div.product form.cart .button,.wc-block-components-button:not(.is-link){border-radius:999px;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);font-weight:800}'
   '.wc-block-components-text-input input,.wc-block-components-textarea,.wc-block-components-select select,.woocommerce .quantity .qty{border-radius:12px!important;border:2px solid var(--wp--preset--color--contrast)!important}'
   '.woocommerce-tabs .tabs{display:none}'
  ),
 },
 'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                   {'area': 'uncategorized', 'name': 'notice', 'title': 'Occasion cut-off bar'}],
 'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Stem
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A colour-blocked shop theme for independent florists who deliver same day, take subscriptions and do weddings and workshops.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: stem
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')


def variation(fname, title, rows, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)


variation('dried', 'Dried', [('base', '#EADCC3', 'Sand'), ('contrast', '#3A2414', 'Brown ink'), ('accent', '#9A4A16', 'Rust'),
    ('surface', '#D9B77A', 'Wheat'), ('line', '#3A2414', 'Brown line'), ('muted', '#5E4330', 'Dried stem'), ('accent-2', '#5C3A21', 'Bark'),
    ('mint', '#C9C3A2', 'Sage'), ('leaf', '#5B5A2E', 'Olive'), ('cream', '#F7EEDD', 'Linen')])
variation('studio', 'Studio', [('base', '#FFFFFF', 'White'), ('contrast', '#111111', 'Black'), ('accent', '#D6281F', 'Poppy'),
    ('surface', '#F2F2F2', 'Backdrop grey'), ('line', '#111111', 'Black line'), ('muted', '#555555', 'Grey'), ('accent-2', '#111111', 'Black'),
    ('mint', '#F2F2F2', 'Backdrop grey'), ('leaf', '#D6281F', 'Poppy'), ('cream', '#FFFFFF', 'White')])
variation('night', 'Night', [('base', '#15110F', 'Night'), ('contrast', '#F6EEDC', 'Ivory'), ('accent', '#FF6B5B', 'Coral'),
    ('surface', '#2A211C', 'Candlelit'), ('line', '#F6EEDC', 'Ivory line'), ('muted', '#C9BBA5', 'Faded ivory'), ('accent-2', '#6E8BFF', 'Night blue'),
    ('mint', '#1F2B26', 'Dark sage'), ('leaf', '#2F4A36', 'Dark leaf'), ('cream', '#15110F', 'Night')])


def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})


PADS = {'padding': {'top': SP('60'), 'bottom': SP('60'), 'left': SP('40'), 'right': SP('40')}}
def colour_field(slug, title, bg, fg, link=None):
    section(slug, title, ['core/group', 'core/columns', 'core/column'],
            {'color': {'background': C(bg), 'text': C(fg)}, 'spacing': PADS,
             'elements': {'link': {'color': {'text': C(link or fg)}}, 'heading': {'color': {'text': C(fg)}},
                          'button': {'color': {'background': C(fg), 'text': C(bg)}}}})


colour_field('poppy', 'Poppy field', 'accent', 'cream')
colour_field('marigold', 'Marigold field', 'surface', 'contrast')
colour_field('cobalt', 'Cobalt field', 'accent-2', 'base')
colour_field('mint-field', 'Mint field', 'mint', 'contrast')
colour_field('leaf-field', 'Leaf field', 'leaf', 'cream')
colour_field('aubergine', 'Aubergine field', 'contrast', 'base')
section('still-life', 'Still life (photo on a colour field)', ['core/group'],
        {'spacing': {'padding': {'top': SP('40'), 'bottom': SP('40'), 'left': SP('40'), 'right': SP('40')}, 'blockGap': SP('30')},
         'elements': {'link': {'color': {'text': 'currentColor'}}},
         'css': '& img{aspect-ratio:4/5;object-fit:cover;width:100%}& a{color:inherit}'})
section('arch', 'Arched photo', ['core/image'], {'css': '& img{border-radius:50% 50% 0 0/30% 30% 0 0}'})
section('price-line', 'Name, size and price line', ['core/paragraph'], {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('large')}, 'css': '&{white-space:nowrap}'})
section('cutoff', 'Cut-off line', ['core/paragraph'],
        {'typography': {'fontSize': FS('x-small'), 'fontWeight': '600'},
         'css': '&{border-top:2px solid currentColor;padding-top:.5em!important}'})
section('flower-list', 'Flower list', ['core/paragraph'],
        {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('x-large'), 'lineHeight': '1.12'}})
section('pill', 'Pill label', ['core/paragraph'],
        {'color': {'background': C('cream'), 'text': C('contrast')}, 'typography': {'fontWeight': '800', 'fontSize': FS('x-small')},
         'border': {'radius': '999px'}, 'css': '&{display:inline-block;padding:.35em 1em!important}'})
section('care-card', 'Care card (printable)', ['core/group'],
        {'color': {'background': C('cream'), 'text': C('contrast')}, 'border': {'width': '2px', 'style': 'dashed', 'color': C('contrast')},
         'spacing': {'padding': {'top': SP('50'), 'bottom': SP('50'), 'left': SP('50'), 'right': SP('50')}}})

section('rows', 'Rows (instead of a table)', ['core/group'],
        {'css': ('& > .wp-block-group{border-bottom:2px solid currentColor;padding:.6em 0!important;margin:0!important;column-gap:1rem!important;row-gap:.15rem!important}'
                 '& > .wp-block-group > p{margin:0!important}& > .wp-block-group > p:first-child{font-weight:800}'
                 '& > .wp-block-group > p:last-child:not(:first-child){text-align:right;font-variant-numeric:tabular-nums}')})


def rows(items, head=None, min_w='8rem', cls='is-style-rows', **kw):
    n = max(len(r) for r in items)
    return group(J(*[group(J(*[para(c) for c in r]), layout={'type': 'grid', 'columnCount': n, 'minimumColumnWidth': min_w}) for r in items]),
                 className=cls, layout={'type': 'default'}, **kw)


# ---------------------------------------------------------------- content
SHOP = {'name': 'Hollyhock', 'addr': '3 Chatsworth Road, London E5 0LH', 'email': 'flowers@example.com', 'phone': '020 7946 0319'}
CUTOFF = 'Order by 2pm for same-day delivery in E5, E8, E9, N16 and N4. Next day everywhere else in the UK.'
SUBS = 'Florist\'s choice: we use what is best at the market that morning, and swap like for like if something runs out.'

ALT = {
 'posy.jpg': 'A small posy of roses, yarrow and wildflowers held against a white top',
 'roses-held.jpg': 'A bouquet of cream and orange roses held in front of a dark red dress',
 'gerbera-mint.jpg': 'Pink gerberas and berries in a glass jar against a mint green wall',
 'bridal.jpg': 'A bridal bouquet of pink roses, lisianthus and astrantia',
 'peony-vase.jpg': 'Two pink peonies in a stoneware jug against a grey plaster wall',
 'tulips.jpg': 'Red tulips standing close together, soft focus',
 'peonies.jpg': 'A dense mass of frilly pink carnations filling the frame',
 'dahlia.jpg': 'A single white dahlia on a dark slate background',
 'dried.jpg': 'Dried sea lavender stems against green',
 'wedding.jpg': 'A bride holding a round bouquet of pink roses, freesias and silver brunia',
 'hero-man.jpg': 'A man in a trench coat smelling a bunch of pink roses on a city street',
 'market.jpg': 'Flower stalls under arches at a busy street market',
 'vendor-print.jpg': 'An eighteenth-century engraving of a woman selling carnations from a basket',
 'bouquet-sandals.jpg': 'A pink and white bouquet on a wooden bench next to a pair of sandals',
}

# name, image, category, price, stock, short, desc
P = [
 ('Florist\'s choice, small', 'posy.jpg', 'Bouquets', '40', 50, 'Around 15 stems, hand-tied. For a bedside or a kitchen table.', 'Whatever is best that morning. In autumn that means dahlias, rosehips and the last garden roses.'),
 ('Florist\'s choice, medium', 'roses-held.jpg', 'Bouquets', '60', 50, 'Around 25 stems. The one most people send.', 'Hand-tied, in water, wrapped in paper with a ribbon. Enough for a big jug.'),
 ('Florist\'s choice, large', 'gerbera-mint.jpg', 'Bouquets', '85', 50, 'Around 35 stems, with branches and foliage. Needs a tall vase.', 'Built for a hallway or a birthday that matters. We add branches from the market when there are good ones.'),
 ('Florist\'s choice, showy', 'bridal.jpg', 'Bouquets', '120', 20, 'Two armfuls. Delivered in a water box so it can stay wrapped.', 'The biggest thing we will put on a bike. Tell us the colour you want and we will lean that way.'),
 ('Pink peonies, 10 stems', 'peony-vase.jpg', 'Seasonal', '48', 0, 'May and June only. Sold out until next spring.', 'Sarah Bernhardt peonies from a grower in Lincolnshire. Sent in tight bud; they open in two days.'),
 ('Red tulips, 20 stems', 'tulips.jpg', 'Seasonal', '32', 30, 'Dutch tulips, straight from the Tuesday market.', 'Tulips keep growing in the vase. Cut them shorter than you think.'),
 ('Pink carnations, 25 stems', 'peonies.jpg', 'Seasonal', '30', 25, 'Frilly, long-lasting, unfashionable, and we love them.', 'Carnations last two weeks with clean water. Colombian-grown, bought at New Covent Garden.'),
 ('White dahlias, 7 stems', 'dahlia.jpg', 'Seasonal', '36', 12, 'August to October. From Rosa\'s allotment in Walthamstow.', 'Dahlias do not last long, about five days, but no one complains.'),
 ('Dried sea lavender bunch', 'dried.jpg', 'Dried', '28', 20, 'Lasts a year or more. Keep it out of direct sun.', 'Grown and dried in Norfolk. Sheds a little when you first unwrap it.'),
 ('Weekly bouquet, 4 weeks prepaid', 'bouquet-sandals.jpg', 'Subscriptions', '216', 100, 'Four medium bouquets, one a week. Saves £24 against paying each time.', 'Pick your delivery day at checkout. Pause any week by emailing us before Monday.'),
 ('Workshop gift voucher', 'market.jpg', 'Workshops', '95', 100, 'A place on any evening workshop. Valid for a year.', 'Posted in a card, or emailed straight away.'),
]


def purl(p):
    return '/product/%s/' % slugify(p[0])


# ---------------------------------------------------------------- patterns
pattern('hero-cutoff', 'Hero: the cut-off as the headline', 'featured,banner', columns(
  ('52%', J(heading('This week: dahlias, rosehips and the last garden roses', 1, fontSize='xx-large'),
     para('Order by 2pm, on the table by 6. Same day across Hackney by cargo bike.', fontSize='large'),
     para('Hand-tied bouquets from a small shop on Chatsworth Road, delivered by cargo bike across Hackney the same day. Next day everywhere else.', fontSize='large'),
     buttons(('Choose a bouquet', '/product-category/bouquets/'), ('Delivery areas', '/delivery/', {'className': 'is-style-outline'})),
     para('Missed it? Call <a href="tel:02079460319">%s</a> and we will see what the bike can do.' % SHOP['phone'], fontSize='small')), {'className': 'is-style-poppy', 'verticalAlignment': 'center'}),
  (None, image('hero-man.jpg', ALT['hero-man.jpg'], aspectRatio='4/5', scale='cover')),
  align='full', style={'spacing': {'blockGap': {'left': '0', 'top': '0'}}}),
  description='The signature cut-off rule as the page headline, on a poppy field next to a photo.')

pattern('this-week', 'What is in this week (flower names in colour)', 'text,featured', group(J(
  heading('At the market this week', 3),
  para('<mark style="background-color:rgba(0,0,0,0)" class="has-inline-color has-accent-color">Dahlias</mark>, '
       '<mark style="background-color:rgba(0,0,0,0)" class="has-inline-color has-accent-2-color">cornflowers</mark>, '
       '<mark style="background-color:rgba(0,0,0,0)" class="has-inline-color has-leaf-color">eucalyptus</mark>, '
       '<mark style="background-color:rgba(0,0,0,0)" class="has-inline-color has-muted-color">rosehips</mark>, '
       'late garden roses, '
       '<mark style="background-color:rgba(0,0,0,0)" class="has-inline-color has-accent-color">crocosmia</mark>, '
       'scabious and the first '
       '<mark style="background-color:rgba(0,0,0,0)" class="has-inline-color has-accent-2-color">hydrangeas</mark> turning green.', className='is-style-flower-list'),
  para('Rosa goes to New Covent Garden on Tuesday and Friday at 4am. This list changes after each trip.', fontSize='small')),
  align='wide', layout={'type': 'constrained', 'contentSize': '1100px', 'justifyContent': 'left'}, style={'spacing': {'padding': {'top': SP('70'), 'bottom': SP('60')}}}))

FIELDS = [('surface', 'contrast'), ('accent-2', 'base'), ('mint', 'contrast'), ('leaf', 'cream'), ('accent', 'cream')]


def bouquet(p, field):
    sold = p[4] == 0
    return group(J(
        image(p[1], ALT[p[1]], href=purl(p), aspectRatio='4/5', scale='cover'),
        row(J(heading('<a href="%s">%s</a>' % (purl(p), p[0]), 3), para('Sold out' if sold else '£%s' % p[3], className='is-style-price-line')), justify='space-between', wrap=False),
        para(p[5], fontSize='small'),
        para('Order by 2pm for same-day delivery in east London. Next day nationwide.', className='is-style-cutoff')),
        className='is-style-still-life', backgroundColor=field[0], textColor=field[1], layout={'type': 'default'})


pattern('bouquets', 'Bouquets, two across on colour fields', 'shop,featured', group(J(
  row(J(heading('Bouquets', 2), para('<a href="/shop/">Everything we deliver</a>', fontSize='large')), justify='space-between', align='wide'),
  group(J(*[bouquet(P[i], FIELDS[n % 5]) for n, i in enumerate([0, 1, 2, 3])]), align='wide',
        layout={'type': 'grid', 'columnCount': 2, 'minimumColumnWidth': '18rem'}, style={'spacing': {'blockGap': SP('40')}}),
  para(SUBS, fontSize='small', align='wide')),
  align='wide', layout={'type': 'default'}),
  description='Large portrait bouquets, each on its own colour field, with name, size and price in one line and the cut-off beneath.')

pattern('seasonal', 'Seasonal stems (four across)', 'shop', group(J(
  heading('By the bunch', 2),
  group(J(*[bouquet(P[i], FIELDS[(n + 2) % 5]) for n, i in enumerate([5, 6, 7, 4])]), align='wide',
        layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}, style={'spacing': {'blockGap': SP('30')}})),
  align='wide', layout={'type': 'default'}))

pattern('delivery-zones', 'Delivery zones and charges', 'shop,featured', group(J(
  heading('Where we deliver', 2),
  rows([['E5, E8, E9, N16, N4', 'Same day if ordered by 2pm', '£7'], ['Rest of east and north London', 'Same day if ordered by 12pm', '£12'],
         ['Anywhere in London', 'Next day, 9am to 6pm', '£12'], ['Rest of the UK', 'Next day by courier, in a water box', '£14'],
         ['Collect from the shop', 'From 11am the same day', 'Free']], head=['Area', 'When', 'Cost']),
  para('No deliveries on Sundays or Mondays. We cannot promise a time, but we can promise a morning or an afternoon.'),
  para('Missed the cut-off? Call <a href="tel:02079460319">%s</a>. If the bike is still out, we will try.' % SHOP['phone'], fontSize='large')),
  className='is-style-cobalt', align='full', layout={'type': 'constrained', 'contentSize': '900px'}),
  description='Delivery charges by zone, the cut-off times, and the phone number for late orders.')

pattern('cutoff-line', 'Cut-off line (for products)', 'shop', para(CUTOFF, className='is-style-cutoff'))
pattern('substitution-note', 'Substitution note', 'shop', para(SUBS, fontSize='small'))
pattern('gift-message', 'Gift message note', 'shop', group(J(
  heading('Gift message', 4),
  para('Add a message at checkout and we will write it by hand on a card. Up to 40 words. We do not put prices or receipts in with the flowers.')),
  className='is-style-mint-field', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('40'), 'bottom': SP('40')}}}))

pattern('subscriptions', 'Flower subscriptions', 'shop,featured', columns(
  ('45%', image('bouquet-sandals.jpg', ALT['bouquet-sandals.jpg'], aspectRatio='4/5', scale='cover', className='is-style-arch')),
  (None, J(heading('A bouquet every week, or every month', 2),
     rows([['Weekly, rolling', '£60 a week', 'Cancel any time'], ['Weekly, 4 weeks prepaid', '£216', 'Saves £24'], ['Monthly, rolling', '£60 a month', 'Cancel any time'],
            ['Monthly, 6 months prepaid', '£330', 'Saves £30']], head=['Plan', 'Price', '']),
     para('Every subscription is a medium florist\'s choice, delivered on the day you pick. Pause for holidays by emailing us before Monday.'),
     buttons(('Start a subscription', purl(P[9])))), {'className': 'is-style-marigold', 'verticalAlignment': 'center'}),
  align='full', style={'spacing': {'blockGap': {'left': '0', 'top': '0'}}}),
  description='Weekly and monthly plans, prepaid or rolling, with the saving stated.')

pattern('weddings-intro', 'Weddings intro and enquiry', 'services', columns(
  (None, image('wedding.jpg', ALT['wedding.jpg'], aspectRatio='3/4', scale='cover')),
  (None, J(heading('Weddings', 2),
     para('Bea Oyelaran does our weddings, about twenty a year, mostly in east London and Essex. She likes a loose, garden look and will talk you out of a flower wall.'),
     table([['Bridal bouquet', 'from £150'], ['Buttonholes', '£14 each'], ['Table arrangements', 'from £45 each'], ['Ceremony urns', 'from £280 each']], head=['Piece', 'Price']),
     para('Minimum spend £900. We book up to 18 months ahead and take four weddings a month at most.'),
     buttons(('Email Bea about your wedding', 'mailto:%s?subject=Wedding%%20enquiry' % SHOP['email'])))), align='wide', className='is-style-leaf-field',
  style={'spacing': {'blockGap': {'left': SP('60')}}}))

pattern('real-weddings', 'Real weddings (latest posts)', 'posts,query', group(J(
  row(J(heading('Real weddings', 2), para('<a href="/weddings/">All of them</a>', fontSize='large')), justify='space-between', align='wide'),
  query(J(dyn('post-featured-image', isLink=True, aspectRatio='3/4', scale='cover'), dyn('post-title', isLink=True, level=3), dyn('post-excerpt', excerptLength=16, fontSize='small')),
        per_page=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '15rem'}, align='wide')),
  align='wide', layout={'type': 'default'}))

pattern('wedding-flowers-used', 'Flowers used (wedding caption)', 'text', rows([
  ['Bouquet', 'Garden roses, sweet peas, astrantia, jasmine trails'], ['Tables', 'Dahlias, scabious and cosmos in jam jars'], ['Venue', 'Round Chapel, Clapton'], ['Photographs', 'Ama Boateng']], head=['', 'Flowers']))

pattern('workshops', 'Workshops calendar', 'services', group(J(
  heading('Workshops', 2),
  para('Evening classes in the shop, eight people at most. Wine, flowers and a jar to take home are included.'),
  rows([['Thu 9 Oct', 'Autumn hand-tied bouquet', '3 places left', '£95'], ['Thu 23 Oct', 'Dried flower wreath', '5 places left', '£85'],
         ['Thu 27 Nov', 'Christmas door wreath', 'Full, waiting list open', '£95'], ['Thu 4 Dec', 'Christmas door wreath', '6 places left', '£95'],
         ['Thu 11 Dec', 'Table centrepiece', '8 places left', '£85']], head=['Date', 'Workshop', 'Places', 'Price']),
  buttons(('Buy a workshop voucher', purl(P[10])))),
  className='is-style-mint-field', align='full', layout={'type': 'constrained', 'contentSize': '900px'}))

pattern('occasion-cutoff', 'Notice: occasion cut-off (Mother\'s Day, Valentine\'s)', 'banner', group(
  para('Mother\'s Day is Sunday 15 March. Order by Thursday 12 March for Saturday delivery; we do not deliver on the Sunday itself. Take this bar down on Monday.'),
  className='is-style-aubergine', align='full', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}}}),
  description='Switch on a fortnight before Mother\'s Day or Valentine\'s, then off.')

pattern('care-card', 'Flower care card (printable)', 'text', group(J(
  heading('Keeping them going', 3),
  lst(['Cut 2cm off the stems at an angle before they go in water.', 'Clean vase, cool water, and change it every two days.',
       'Pull off any leaves that sit below the water line.', 'Keep them away from radiators, sunny windows and the fruit bowl.',
       'Tulips keep growing. Dahlias drink a lot. Peonies open fast in warm rooms.'], ordered=True),
  para('Print this and keep it by the sink. From Hollyhock, %s.' % SHOP['addr'], fontSize='x-small')),
  className='is-style-care-card', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('visit', 'Visit the shop', 'contact', columns(
  (None, J(heading('Come and choose', 2),
     para('%s. On the corner by the cheese shop; the 242 stops at the end of the road. Buckets out front from 9am.' % SHOP['addr']),
     rows([['Mon', 'Closed'], ['Tue to Fri', '9am to 6pm'], ['Sat', '9am to 5pm'], ['Sun', '10am to 2pm']], head=['Day', 'Open']),
     para('<a href="tel:02079460319">%s</a>, <a href="mailto:%s">%s</a>' % (SHOP['phone'], SHOP['email'], SHOP['email'])))),
  (None, image('market.jpg', ALT['market.jpg'], aspectRatio='4/3', scale='cover')), align='wide', className='is-style-marigold'))

pattern('about', 'About the shop', 'about', columns(
  ('40%', image('vendor-print.jpg', ALT['vendor-print.jpg'], caption='A carnation seller in Paris, about 1740. The job has not changed much.')),
  (None, J(heading('Hollyhock', 2),
     para('Rosa Mendes opened Hollyhock in 2016 after eight years working for other florists in the West End. She grew up above her aunt\'s flower stall in Porto and still buys like her: early, in cash, and with an opinion.'),
     para('We buy British flowers from May to October and import the rest from the Dutch auctions. We do not use floral foam; everything sits in water, moss or chicken wire.'),
     para('We do not do funeral tributes with lettering. For that, try Ferns on Well Street, who do it beautifully.'))), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}))

pattern('quote', 'A customer note', 'testimonials', group(quote('The bike turned up at 5.40 with the biggest thing I have ever been sent. My mum still talks about it.', 'Leila, Stoke Newington, sent for a 70th, June 2025'),
  className='is-style-poppy', layout={'type': 'constrained'}))

pattern('sizes', 'Bouquet sizes explained', 'shop', group(J(
  heading('Which size', 3),
  rows([['Small, £40', 'About 15 stems', 'A jam jar or a bedside'], ['Medium, £60', 'About 25 stems', 'A big jug, the one most people send'],
         ['Large, £85', 'About 35 stems and branches', 'A tall vase on the floor or a hall table'], ['Showy, £120', 'Two armfuls', 'Delivered in a water box, no vase needed']],
        head=['Size', 'Stems', 'Fits'])), className='is-style-marigold', layout={'type': 'default'}))

pattern('late-order', 'Missed the cut-off? Call us', 'call-to-action', group(J(
  heading('Missed the 2pm cut-off?', 3),
  para('Call <a href="tel:02079460319">%s</a> before 4pm. If the bike is still out in your direction, we will add you to the round. If not, we will say so straight away.' % SHOP['phone'])),
  className='is-style-poppy', layout={'type': 'default'}))

pattern('dried-corner', 'Dried flowers', 'shop', columns(
  (None, image('dried.jpg', ALT['dried.jpg'], aspectRatio='4/3', scale='cover')),
  (None, J(heading('Dried, for the long haul', 3),
     para('Sea lavender, bunny tails, honesty and wheat, grown and dried in Norfolk. They last a year or more out of direct sun. No bleached or dyed stems.'),
     buttons(('Shop dried flowers', '/product-category/dried/')))), align='wide', className='is-style-leaf-field'))

pattern('post-grid', 'Weddings grid (inherits query)', 'posts,query', inherit_query(
  J(dyn('post-featured-image', isLink=True, aspectRatio='3/4', scale='cover'), dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', excerptLength=20, fontSize='small')),
  layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}, align='wide'), inserter=False)
pattern('post-list', 'Results list', 'posts,query', inherit_query(
  group(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-date')), layout={'type': 'default'}, style={'border': {'bottom': {'color': C('line'), 'width': '2px', 'style': 'solid'}}}), align='wide'), inserter=False)


# ---------------------------------------------------------------- round 2
OCC = [('Birthdays', 'roses-held.jpg', 'Loud colour, a big jug\'s worth.', 'accent'), ('Thank you', 'posy.jpg', 'A small posy that fits on a desk.', 'surface'),
       ('New baby', 'gerbera-mint.jpg', 'Soft colours, nothing that sheds pollen.', 'mint'), ('Sympathy', 'dahlia.jpg', 'White and green, hand-tied, delivered quietly.', 'leaf')]
pattern('occasions', 'Flowers by occasion', 'shop,featured', group(J(
  heading('For the occasion', 2),
  group(J(*[group(J(image(img, ALT[img], href='/product-category/bouquets/', aspectRatio='4/5', scale='cover'), heading('<a href="/product-category/bouquets/">%s</a>' % n, 3), para(d, fontSize='small')),
                  className='is-style-still-life', backgroundColor=bg, textColor='cream' if bg in ('accent', 'leaf') else 'contrast', layout={'type': 'default'}) for n, img, d, bg in OCC]),
        align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}, style={'spacing': {'blockGap': SP('30')}})),
  align='wide', layout={'type': 'default'}), description='Four occasions, each on its own colour field.')
pattern('sympathy', 'Sympathy flowers', 'shop', columns(
  (None, image('dahlia.jpg', ALT['dahlia.jpg'], aspectRatio='4/5', scale='cover')),
  (None, J(heading('Sympathy flowers', 2), para('White, cream and green, hand-tied or in a low arrangement for a home. We deliver to funeral directors in Hackney and Walthamstow the day before a service if we have the address by noon.'),
     para('We do not make lettered tributes. Ferns on Well Street does them beautifully.', fontSize='small'),
     buttons(('Call Rosa to talk it through', 'tel:02079460319')))), align='wide', className='is-style-leaf-field', verticalAlignment='center'))
pattern('office-flowers', 'Weekly flowers for offices and restaurants', 'services', group(J(
  heading('Flowers for a front desk or a restaurant', 2),
  para('A weekly or fortnightly arrangement, delivered Monday morning, old ones taken away. We keep your vases.'),
  rows([['Reception arrangement', 'from £75 a week'], ['Restaurant bud vases, 10 tables', 'from £60 a week'], ['Fortnightly', 'same prices, every other Monday']]),
  buttons(('Email about office flowers', 'mailto:%s?subject=Office%%20flowers' % SHOP['email']))),
  className='is-style-cobalt', align='full', layout={'type': 'constrained', 'contentSize': '900px'}), description='Weekly arrangements for businesses, with prices.')
pattern('events-installations', 'Events and installations', 'services', columns(
  ('60%', gallery([('peonies.jpg', ALT['peonies.jpg'], 'Carnation wall, gallery opening'), ('tulips.jpg', ALT['tulips.jpg'], 'Tulip tables, supper club'), ('market.jpg', ALT['market.jpg'], 'Market stall, summer fair')], columns=3)),
  (None, J(heading('Parties, launches and long tables', 2), para('We make one-off installations for events in east London: tables, doorways, hanging clouds of dried flowers. From £600, quoted after a site visit.'),
     buttons(('Email about an event', 'mailto:%s?subject=Event' % SHOP['email'])))), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  description='Event work with three photos you can open large.')
MONTHS = [('January', 'Tulips, anemones, hellebores'), ('March', 'Ranunculus, narcissi, blossom branches'), ('May', 'Peonies, lilac, alliums'), ('July', 'Sweet peas, cornflowers, garden roses'),
          ('September', 'Dahlias, rosehips, crocosmia'), ('November', 'Dried flowers, eucalyptus, winter berries')]
pattern('seasonal-calendar', 'What is in season, month by month', 'text', group(J(
  heading('The year in flowers', 2),
  rows([list(m) for m in MONTHS], min_w='9rem')),
  className='is-style-marigold', align='full', layout={'type': 'constrained', 'contentSize': '900px'}), description='Every other month and what we are buying.')
pattern('colour-lean', 'Choose a colour lean', 'shop', group(J(
  heading('Tell us a colour and we will lean that way', 3),
  row(J(*[para(n, className='is-style-pill', backgroundColor=bg, textColor=fg) for n, bg, fg in [('Hot pink and red', 'accent', 'cream'), ('Sunshine', 'surface', 'contrast'), ('Blue and white', 'accent-2', 'base'), ('Green and white', 'mint', 'contrast'), ('Dark and moody', 'contrast', 'base')]]), style={'spacing': {'blockGap': SP('20')}}),
  para('Add it in the order note. Florist\'s choice still applies, but we will follow the colour.', fontSize='small')),
  layout={'type': 'default'}), description='Colour choices as pills, for the order note.')
pattern('add-ons', 'Add-ons', 'shop', columns(
  (None, J(heading('A vase, £18', 4), para('Recycled glass, the right size for a medium bouquet.'))),
  (None, J(heading('A handwritten card, free', 4), para('Up to 40 words, in Rosa\'s handwriting.'))),
  (None, J(heading('A water box, included', 4), para('Every courier delivery travels upright in water.'))), align='wide', className='is-style-mint-field'), description='Extras at checkout, none ticked by default.')
pattern('wedding-process', 'How a wedding works with us', 'services', group(J(
  heading('How a wedding works', 2),
  lst(['Email Bea with the date, the venue and a rough budget.', 'A 45-minute chat at the shop, with flowers on the table so you can see colours.', 'A written quote with a flower list. A 30% deposit books the date.', 'Final numbers six weeks before. We buy at the market that week and set up on the day.'], ordered=True, fontSize='large')),
  className='is-style-poppy', align='full', layout={'type': 'constrained', 'contentSize': '900px'}))
pattern('wedding-gallery', 'Wedding gallery', 'gallery', gallery([
  ('wedding.jpg', ALT['wedding.jpg'], 'Round Chapel, June'), ('bridal.jpg', ALT['bridal.jpg'], 'Walthamstow, July'), ('roses-held.jpg', ALT['roses-held.jpg'], 'Clapton, September'), ('bouquet-sandals.jpg', ALT['bouquet-sandals.jpg'], 'Epping, August')], columns=4, align='wide'),
  description='Four wedding photos. Click to open.')
pattern('bouquet-styles', 'Bridal bouquet styles', 'services', columns(
  (None, J(heading('Garden', 4), para('Loose, a bit wild, with trailing stems. Our favourite.'))), (None, J(heading('Posy', 4), para('Round and small. Good for a registry office.'))),
  (None, J(heading('Single variety', 4), para('All peonies, or all sweet peas. Seasonal and striking.'))), align='wide', className='is-style-marigold'))
pattern('private-workshops', 'Private workshops', 'services', columns(
  (None, J(heading('Private workshops', 2), para('Hen parties, team evenings and birthdays, for six to twelve people, in the shop after hours. Everyone goes home with a bouquet.'), rows([['Six people', '£540'], ['Each extra person', '£85']]))),
  (None, image('market.jpg', ALT['market.jpg'], aspectRatio='4/3', scale='cover')), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}))
pattern('workshop-detail', 'What you make at a workshop', 'services', group(J(
  heading('What you will make', 3),
  lst(['A hand-tied spiral bouquet of about 25 stems', 'Wrapping it in paper and ribbon so it survives the bus home', 'How to condition flowers so they last a week longer']),
  para('Two hours, wine and snacks included. All flowers and tools provided.', fontSize='small')), className='is-style-mint-field', layout={'type': 'default'}))
pattern('team', 'Who we are', 'about', columns(
  (None, J(heading('Rosa Mendes', 3), para('Owner. Goes to the market at 4am on Tuesdays and Fridays. Grows the dahlias.'))),
  (None, J(heading('Bea Oyelaran', 3), para('Weddings and events. Will talk you out of a flower wall.'))),
  (None, J(heading('Tunde Bakare', 3), para('Rides the cargo bike. Knows every buzzer in E5.'))), align='wide', className='is-style-cobalt'))
pattern('delivery-bike', 'Delivered by bike', 'shop', columns(
  (None, J(heading('On a bike by 3, at the door by 6', 2), para('Tunde leaves the shop at 3pm with the day\'s orders in a cargo bike with a water tray. If nobody is in, he tries a neighbour, then texts you a photo of where he left them.'))),
  (None, image('hero-man.jpg', ALT['hero-man.jpg'], aspectRatio='4/3', scale='cover')), align='wide', className='is-style-poppy', verticalAlignment='center'))
pattern('faq', 'Questions people ask', 'text', group(J(
  heading('Questions', 2),
  details('Can I choose a delivery time?', para('Morning or afternoon, not an exact time.')),
  details('What if nobody is in?', para('We try a neighbour, then a safe place, and text you a photo.')),
  details('Do you deliver on Sundays?', para('No. Order by Saturday 2pm for Saturday delivery.')),
  details('Are your flowers British?', para('From May to October mostly, yes. The rest comes from the Dutch auctions.'))),
  layout={'type': 'constrained', 'justifyContent': 'left'}))
pattern('hero-bouquets', 'Hero: today\'s bouquets', 'featured,banner', group(J(
  heading('Today\'s bouquets', 1, fontSize='xx-large'),
  gallery([('posy.jpg', ALT['posy.jpg'], 'Small, £40'), ('roses-held.jpg', ALT['roses-held.jpg'], 'Medium, £60'), ('gerbera-mint.jpg', ALT['gerbera-mint.jpg'], 'Large, £85')], columns=3, align='wide'),
  para(CUTOFF, className='is-style-cutoff')), className='is-style-marigold', align='full', layout={'type': 'constrained', 'contentSize': '1360px'}),
  description='An alternative opening: today\'s three sizes with the cut-off.')
pattern('photo-strip', 'Photo strip', 'gallery', gallery([('tulips.jpg', ALT['tulips.jpg'], ''), ('peony-vase.jpg', ALT['peony-vase.jpg'], ''), ('dahlia.jpg', ALT['dahlia.jpg'], ''), ('dried.jpg', ALT['dried.jpg'], ''), ('peonies.jpg', ALT['peonies.jpg'], '')], columns=5, align='full'))

# pages
pattern('page-delivery', 'Page: delivery', 'shop', J(pattern_ref('delivery-zones'), pattern_ref('late-order'), pattern_ref('sizes'), pattern_ref('gift-message'), pattern_ref('substitution-note'), pattern_ref('care-card')), block_types='core/post-content')
pattern('page-subscriptions', 'Page: subscriptions', 'shop', J(pattern_ref('subscriptions'), pattern_ref('this-week'), pattern_ref('dried-corner'), pattern_ref('quote')), block_types='core/post-content')
pattern('page-workshops', 'Page: workshops', 'services', J(pattern_ref('workshops'), pattern_ref('workshop-detail'), pattern_ref('private-workshops'), pattern_ref('about')), block_types='core/post-content')
pattern('page-weddings-events', 'Page: weddings and events', 'services', J(pattern_ref('weddings-intro'), pattern_ref('wedding-process'), pattern_ref('bouquet-styles'), pattern_ref('wedding-gallery'), pattern_ref('events-installations'), pattern_ref('office-flowers')), block_types='core/post-content')
pattern('page-occasions', 'Page: occasions', 'shop', J(pattern_ref('occasions'), pattern_ref('colour-lean'), pattern_ref('add-ons'), pattern_ref('sympathy'), pattern_ref('seasonal-calendar')), block_types='core/post-content')
pattern('page-visit', 'Page: visit', 'contact', J(pattern_ref('visit'), pattern_ref('team'), pattern_ref('delivery-bike'), pattern_ref('faq'), pattern_ref('photo-strip')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(
  row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile', textColor='base', style={'spacing': {'blockGap': SP('40')}})),
      justify='space-between', align='wide', wrap=False),
  tag='header', align='full', backgroundColor='accent-2', textColor='base', layout={'type': 'constrained'},
  style={'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}}, 'elements': {'link': {'color': {'text': C('base')}}}}))
write('parts/notice.html', pattern_ref('occasion-cutoff'))
write('parts/footer.html', group(J(
  heading('Order by 2pm, on the table by 6', 2, fontSize='xx-large', align='wide'),
  columns(
    (None, J(heading('Hollyhock', 4), para('%s<br>Tue to Fri 9 to 6, Sat 9 to 5, Sun 10 to 2<br><a href="tel:02079460319">%s</a>' % (SHOP['addr'], SHOP['phone'])))),
    (None, J(heading('Ordering', 4), para('<a href="/delivery/">Delivery areas and charges</a><br><a href="/subscriptions/">Subscriptions</a><br><a href="mailto:%s">%s</a>' % (SHOP['email'], SHOP['email'])))),
    (None, J(heading('Weddings and workshops', 4), para('<a href="/weddings/">Real weddings</a><br><a href="/weddings-and-events/">Weddings and events</a><br><a href="/workshops/">Evening workshops</a><br><a href="/occasions/">Occasions</a>'))),
    align='wide'),
  para('Demo photographs are CC0 and public domain images from Wikimedia Commons and Unsplash, used as stand-ins.', fontSize='x-small', align='wide')),
  tag='footer', align='full', className='is-style-aubergine', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': SP('70'), 'bottom': SP('50')}}}))


# ---------------------------------------------------------------- templates
def main(inner, pad_top='60', **kw):
    return group(inner, tag='main', style={'spacing': {'padding': {'top': SP(pad_top), 'bottom': SP('80')}}}, layout={'type': 'constrained'}, **kw)


def tpl(name, inner):
    write('templates/%s.html' % name, J(template_part('header', 'header'), inner, template_part('footer', 'footer')))


tpl('front-page', group(J(pattern_ref('hero-cutoff'), pattern_ref('bouquets'), pattern_ref('occasions'), pattern_ref('delivery-bike'), pattern_ref('this-week'),
    pattern_ref('seasonal'), pattern_ref('subscriptions'), pattern_ref('real-weddings'), pattern_ref('workshops'), pattern_ref('visit')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': SP('70'), 'padding': {'bottom': SP('70')}}}))
tpl('page', main(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'}))))
tpl('page-wide', main(J(dyn('post-title', level=1, align='wide', fontSize='xx-large'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1360px'}))))
tpl('single', main(J(
  columns(('45%', dyn('post-featured-image', aspectRatio='3/4', scale='cover')),
          (None, J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-date'), dyn('post-content', layout={'type': 'constrained', 'justifyContent': 'left'}),
                   dyn('post-terms', term='category', prefix='Filed under '))), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)), justify='space-between', align='wide'))))
tpl('home', main(J(heading('Real weddings', 1, align='wide', fontSize='xx-large'), para('Weddings Bea has done, with the flowers we used and who took the photographs.', align='wide', fontSize='large'), pattern_ref('post-grid'))))
tpl('index', main(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-grid'))))
tpl('archive', main(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('post-grid'))))
tpl('search', main(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Peonies, dried, subscription', buttonText='Search'), pattern_ref('post-list'))))
tpl('404', main(J(heading('Wilted', 1), para('That page has gone over. Try the <a href="/shop/">shop</a> or search.'),
    dyn('search', label='Search', showLabel=False, placeholder='Peonies, dried, subscription', buttonText='Search'))))


def product_collection(per_page=16, cols=3):
    q = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'product', 'order': 'asc', 'orderBy': 'date', 'search': '', 'exclude': [],
         'inherit': True, 'taxQuery': {}, 'isProductCollectionBlock': True, 'woocommerceOnSale': False,
         'woocommerceStockStatus': ['instock', 'outofstock', 'onbackorder'], 'woocommerceAttributes': [], 'woocommerceHandPickedProducts': []}
    a = {'queryId': 0, 'query': q, 'tagName': 'div', 'displayLayout': {'type': 'flex', 'columns': cols, 'shrinkColumns': True},
         'dimensions': {'widthType': 'fill'}, 'queryContextIncludes': ['collection'], 'align': 'wide'}
    tmpl = J(dyn('woocommerce/product-image', showSaleBadge=True, imageSizing='single', isDescendentOfQueryLoop=True, aspectRatio='4/5', scale='cover'),
             dyn('post-title', level=2, isLink=True, __woocommerceNamespace='woocommerce/product-collection/product-title'),
             dyn('woocommerce/product-price', isDescendentOfQueryLoop=True))
    return ('<!-- wp:woocommerce/product-collection %s -->\n<div class="wp-block-woocommerce-product-collection alignwide">'
            '<!-- wp:woocommerce/product-template -->\n%s\n<!-- /wp:woocommerce/product-template -->\n\n'
            '<!-- wp:query-pagination {"layout":{"type":"flex","justifyContent":"center"}} -->\n<!-- wp:query-pagination-previous /-->\n\n<!-- wp:query-pagination-numbers /-->\n\n<!-- wp:query-pagination-next /-->\n<!-- /wp:query-pagination -->\n\n'
            '<!-- wp:woocommerce/product-collection-no-results -->\n%s\n<!-- /wp:woocommerce/product-collection-no-results --></div>\n<!-- /wp:woocommerce/product-collection -->') % (
        json.dumps(a, separators=(',', ':')), tmpl, para('Nothing here today. Call the shop and ask what came in this morning.'))


cat_row = row(J(*[para('<a href="/product-category/%s/">%s</a>' % (slugify(n), n), className='is-style-pill') for n in ['Bouquets', 'Seasonal', 'Dried', 'Subscriptions', 'Workshops']]),
              style={'spacing': {'blockGap': SP('20')}}, align='wide')
for name in ('archive-product', 'taxonomy-product_cat', 'product-search-results'):
    tpl(name, main(J(dyn('woocommerce/store-notices'), dyn('query-title', type='archive', showPrefix=False, align='wide'), cat_row,
                     para(CUTOFF, className='is-style-cutoff', align='wide'), dyn('term-description', align='wide'), product_collection()), pad_top='60'))

tpl('single-product', main(J(
  dyn('woocommerce/store-notices'),
  columns(('50%', group(dyn('woocommerce/product-image', showProductLink=False, showSaleBadge=True, imageSizing='single', isDescendentOfSingleProductTemplate=True, aspectRatio='4/5', scale='cover'),
                        className='is-style-marigold', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('40'), 'bottom': SP('40'), 'left': SP('40'), 'right': SP('40')}}})),
          (None, J(dyn('post-title', level=1, fontSize='xx-large', __woocommerceNamespace='woocommerce/product-query/product-title'),
                   dyn('woocommerce/product-price', isDescendentOfSingleProductTemplate=True, fontSize='large'),
                   dyn('post-excerpt', __woocommerceNamespace='woocommerce/product-query/product-summary'),
                   pattern_ref('cutoff-line'),
                   dyn('woocommerce/add-to-cart-form'),
                   pattern_ref('substitution-note'),
                   dyn('woocommerce/product-details'),
                   pattern_ref('gift-message'))),
          align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}})), pad_top='60'))

print('stem built:', len(os.listdir(os.path.join(D, 'patterns'))), 'patterns')

# ---------------------------------------------------------------- demo
demo = {
 'site': {'title': 'Hollyhock', 'tagline': 'Flowers from Chatsworth Road, delivered by bike'},
 'categories': [{'slug': 'weddings', 'name': 'Real weddings'}, {'slug': 'shop', 'name': 'From the shop'}],
 'front_page': 'home', 'posts_page': 'weddings',
 'pages': [
  {'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'weddings', 'title': 'Weddings', 'content': ''},
  {'slug': 'delivery', 'title': 'Delivery', 'pattern': 'stem/page-delivery', 'template': 'page-wide'},
  {'slug': 'subscriptions', 'title': 'Subscriptions', 'pattern': 'stem/page-subscriptions', 'template': 'page-wide'},
  {'slug': 'workshops', 'title': 'Workshops', 'pattern': 'stem/page-workshops', 'template': 'page-wide'},
  {'slug': 'visit', 'title': 'Visit', 'pattern': 'stem/page-visit', 'template': 'page-wide'},
  {'slug': 'weddings-and-events', 'title': 'Weddings and events', 'pattern': 'stem/page-weddings-events', 'template': 'page-wide'},
  {'slug': 'occasions', 'title': 'Occasions', 'pattern': 'stem/page-occasions', 'template': 'page-wide'},
 ],
 'posts': [
  {'title': 'Nkechi and Tom, Round Chapel, June', 'category': 'weddings', 'image': 'wedding.jpg', 'content': J(
     para('A pink and silver bouquet with garden roses, freesias and brunia, and jam jars of sweet peas down two long tables. Photographs by Ama Boateng.'),
     pattern_ref('wedding-flowers-used'), pattern_ref('wedding-gallery'), pattern_ref('bouquet-styles'))},
  {'title': 'Priya and Joe, a pub garden in Walthamstow', 'category': 'weddings', 'image': 'bridal.jpg', 'content': J(
     para('Forty guests, one very old apple tree and a bouquet of lisianthus, astrantia and roses. Photographs by Marek Zielinski.'), pattern_ref('wedding-process'), pattern_ref('wedding-gallery'))},
  {'title': 'Carnations are back and we are not sorry', 'category': 'shop', 'image': 'peonies.jpg', 'content': J(
     para('They last two weeks, they come in colours nobody else sells, and they cost less than a coffee a stem. We have 300 in the shop this week.'), pattern_ref('seasonal'), pattern_ref('colour-lean'))},
  {'title': 'Ellie and Sam, Clapton, September', 'category': 'weddings', 'image': 'roses-held.jpg', 'content': J(
     para('Orange and cream roses with rosehips and dahlias from Rosa\'s allotment. Photographs by Ama Boateng.'), pattern_ref('wedding-flowers-used'), pattern_ref('photo-strip'))},
  {'title': 'Why we stopped using floral foam', 'category': 'shop', 'image': 'gerbera-mint.jpg', 'content': J(
     para('Foam is a plastic that breaks into dust and never goes away. Everything we make now sits in water, moss or scrunched chicken wire. It takes longer. It is worth it.'), pattern_ref('care-card'), pattern_ref('events-installations'))},
  {'title': 'Dahlias from the allotment, August to October', 'category': 'shop', 'image': 'dahlia.jpg', 'content': J(
     para('Rosa grows about 60 dahlia plants on a plot in Walthamstow. They go into bouquets from August until the first frost.'), pattern_ref('seasonal-calendar'), pattern_ref('this-week'))},
  {'title': 'Maya and Chidi, Hackney Town Hall, October', 'category': 'weddings', 'image': 'bouquet-sandals.jpg', 'content': J(
     para('A registry-office wedding with a posy of dahlias and rosehips and six buttonholes. Lunch after at a Turkish place on Mare Street. Photographs by Marek Zielinski.'), pattern_ref('bouquet-styles'), pattern_ref('wedding-flowers-used'))},
 ],
 'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'Delivery', 'url': '/delivery/'}, {'label': 'Subscriptions', 'url': '/subscriptions/'},
         {'label': 'Occasions', 'url': '/occasions/'}, {'label': 'Weddings', 'url': '/weddings-and-events/'}, {'label': 'Real weddings', 'url': '/weddings/'}, {'label': 'Workshops', 'url': '/workshops/'}, {'label': 'Visit', 'url': '/visit/'}],
 'currency': 'GBP',
 'products': [{'name': p[0], 'price': p[3], 'image': p[1], 'category': p[2], 'sku': 'HLH-%d' % (300 + i), 'stock': p[4], 'short': p[5],
               'description': J(para(p[6]), para(CUTOFF), para(SUBS))} for i, p in enumerate(P)],
}
os.makedirs('demos/stem', exist_ok=True)
json.dump(demo, open('demos/stem/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
