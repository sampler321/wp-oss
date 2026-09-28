# thrift: vintage and second-hand clothing (idea 062), owner's brief "as researched".
# Direction: a 1950s workwear mail-order catalogue. Canvas-grey pages, black condensed caps, ruled measurement tables,
#   and prices on red swing tags with a punched hole. Garments are catalogued like archive pieces: decade, label size, four measurements.
# Why: vintage buyers shop by decade and by measurement, never by label size; the catalogue format makes those two things the interface.
# Fonts: Barlow Condensed 500/700/800 (display, registry) + Barlow 400/500/600 (body). Two families, no mono; tabular figures in tables.
# Palette: canvas #EDEDE8 / ink #1D1F1C / swing-tag red #B5471B / white #FFFFFF card / khaki #C9BB93 for rules on dark.
# Layout idea: the decade index as a row of huge condensed numerals (40s to Y2K) that fills the width of the page and is the home hero.
import sys, json, os, re, unicodedata
sys.path.insert(0, 'tools/lib')
from blocks import *
import blocks as _b
set_theme('thrift')
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

PALETTE = [('base', '#EDEDE8', 'Canvas'), ('contrast', '#1D1F1C', 'Ink'), ('accent', '#B5471B', 'Swing-tag red'),
           ('surface', '#FFFFFF', 'Card'), ('line', '#1D1F1C', 'Rule'), ('muted', '#55574F', 'Faded ink'), ('accent-2', '#C9BB93', 'Khaki')]
cond = {'fontFamily': V('font-family', 'display'), 'textTransform': 'uppercase', 'letterSpacing': '0.01em'}

theme = {
 '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
 'settings': {
  'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
  'layout': {'contentSize': '700px', 'wideSize': '1320px'},
  'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE),
            'duotone': [{'slug': 'catalogue', 'colors': ['#1D1F1C', '#EDEDE8'], 'name': 'Catalogue print'}]},
  'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
   'fontFamilies': [{**fam['display'], 'slug': 'display'}, {**fam['body'], 'slug': 'body'}],
   'fontSizes': [
     {'slug': 'x-small', 'size': '0.875rem', 'name': 'Tag', 'fluid': False},
     {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
     {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
     {'slug': 'large', 'size': '1.625rem', 'name': 'Large', 'fluid': {'min': '1.375rem', 'max': '1.625rem'}},
     {'slug': 'x-large', 'size': '2.75rem', 'name': 'Section', 'fluid': {'min': '2rem', 'max': '2.75rem'}},
     {'slug': 'xx-large', 'size': '5rem', 'name': 'Title', 'fluid': {'min': '3rem', 'max': '5rem'}},
     {'slug': 'display', 'size': 'clamp(4.25rem, 8.7vw, 10rem)', 'name': 'Decade numerals', 'fluid': False}]},
  'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
     {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
     {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.75rem)', 'name': '4'},
     {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.5rem, 5vw, 4rem)', 'name': '6'},
     {'slug': '70', 'size': 'clamp(3.5rem, 8vw, 6.5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(5rem, 11vw, 9rem)', 'name': '8'}]},
  'shadow': {'defaultPresets': False, 'presets': []},
  'border': {'color': True, 'radius': True, 'style': True, 'width': True,
             'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}, {'slug': 'tag', 'size': '3px', 'name': 'Tag corner'}]},
  'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
 },
 'styles': {
  'color': {'background': C('base'), 'text': C('contrast')},
  'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('medium'), 'lineHeight': '1.55'},
  'spacing': {'padding': {'left': SP('40'), 'right': SP('40')}, 'blockGap': SP('30')},
  'elements': {
   'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'underline'},
            ':hover': {'color': {'text': C('accent')}},
            ':focus': {'outline': {'color': C('accent'), 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
   'heading': {'typography': {**cond, 'fontWeight': '800', 'lineHeight': '0.92'}},
   'h1': {'typography': {'fontSize': FS('xx-large')}},
   'h2': {'typography': {'fontSize': FS('x-large')}},
   'h3': {'typography': {'fontSize': FS('large'), 'fontWeight': '700', 'lineHeight': '1'}},
   'h4': {'typography': {'fontSize': FS('medium'), 'fontWeight': '700', 'lineHeight': '1.1', 'letterSpacing': '0.03em'}},
   'h5': {'typography': {'fontSize': FS('small'), 'fontWeight': '700', 'letterSpacing': '0.04em'}},
   'h6': {'typography': {'fontSize': FS('small'), 'fontWeight': '700', 'letterSpacing': '0.04em'}},
   'button': {'color': {'background': C('contrast'), 'text': C('base')}, 'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': C('contrast')},
              'typography': {**cond, 'fontWeight': '700', 'fontSize': FS('medium'), 'letterSpacing': '0.05em'},
              'spacing': {'padding': {'top': '0.55em', 'bottom': '0.5em', 'left': '1.3em', 'right': '1.3em'}},
              ':hover': {'color': {'background': C('accent'), 'text': C('surface')}, 'border': {'color': C('accent')}},
              ':focus': {'outline': {'color': C('accent'), 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
   'caption': {'typography': {'fontSize': FS('x-small')}, 'color': {'text': C('muted')}},
  },
  'blocks': {
   'core/site-title': {'typography': {**cond, 'fontWeight': '800', 'fontSize': FS('x-large'), 'lineHeight': '0.9'},
                       'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}}}},
   'core/site-tagline': {'typography': {'fontSize': FS('x-small')}, 'color': {'text': C('muted')}},
   'core/navigation': {'typography': {**cond, 'fontWeight': '700', 'fontSize': FS('large'), 'lineHeight': '1'},
                       'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent')}}}}},
   'core/post-title': {'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}}}},
   'core/post-date': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '600'}, 'color': {'text': C('muted')}},
   'core/post-terms': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '600'}},
   'core/image': {'border': {'radius': '0'}},
   'core/separator': {'color': {'text': C('contrast')}, 'border': {'width': '3px 0 0 0'}},
   'core/quote': {'typography': {**cond, 'fontSize': FS('x-large'), 'fontWeight': '700', 'lineHeight': '0.95'},
                  'border': {'left': {'color': C('accent'), 'width': '6px', 'style': 'solid'}}, 'spacing': {'padding': {'left': SP('40')}},
                  'elements': {'cite': {'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('x-small'), 'textTransform': 'none', 'fontStyle': 'normal', 'fontWeight': '600'}}}},
   'core/pullquote': {'typography': {**cond, 'fontSize': FS('xx-large'), 'fontWeight': '800'}, 'border': {'width': '0'}},
   'core/table': {'typography': {'fontSize': FS('small')}},
   'core/details': {'border': {'top': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': SP('30'), 'bottom': SP('20')}}},
   'core/query-pagination': {'typography': {**cond, 'fontSize': FS('large'), 'fontWeight': '700'}},
   'core/search': {'border': {'radius': '0'}},
   'core/categories': {'typography': {**cond, 'fontWeight': '700', 'fontSize': FS('large')}},
   'core/comments': {'typography': {'fontSize': FS('small')}},
   'core/query-title': {'typography': {'fontSize': FS('xx-large'), 'textTransform': 'none'}},
   'core/term-description': {'typography': {'fontSize': FS('medium')}},
   'woocommerce/product-price': {'typography': {'fontWeight': '700'}},
  },
  'css': (
   ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
   'table,.wc-block-components-product-price,.is-style-swing-tag{font-variant-numeric:tabular-nums lining-nums}'
   ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
   '.wp-block-table table{border-collapse:collapse;border-top:3px solid var(--wp--preset--color--line)}'
   '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.5em .75em .5em 0;text-align:left}'
   '.wp-block-table thead{border:0}.wp-block-table th{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-weight:700;letter-spacing:.03em;font-size:1.05em}'
   '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0;background:var(--wp--preset--color--surface)}'
   '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base);padding:var(--wp--preset--spacing--40)}'
   # flip tile: the back view replaces the front on hover (a real second photo, no zoom)
   '.is-style-flip-tile .flip{position:relative;margin:0}.is-style-flip-tile .flip > figure + figure{position:absolute;inset:0;opacity:0;margin:0}'
   '.is-style-flip-tile:hover .flip > figure + figure,.is-style-flip-tile:focus-within .flip > figure + figure{opacity:1}'
   '.is-style-flip-tile img{aspect-ratio:4/5;object-fit:cover;width:100%;background:var(--wp--preset--color--surface)}'
   # WooCommerce
   '.wc-block-product-template{gap:var(--wp--preset--spacing--50) var(--wp--preset--spacing--40)!important}'
   '.wc-block-product-template .wc-block-components-product-image{background:var(--wp--preset--color--surface);border-bottom:3px solid var(--wp--preset--color--contrast)}'
   '.wc-block-product-template .wp-block-post-title{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-weight:700;font-size:var(--wp--preset--font-size--large)!important;line-height:1;text-align:left!important}'
   '.wc-block-product-template .wc-block-components-product-price,.wp-block-woocommerce-product-price .wc-block-components-product-price{display:inline-block;background:radial-gradient(circle at .75em 50%,var(--wp--preset--color--base) .22em,transparent .25em),var(--wp--preset--color--accent);color:var(--wp--preset--color--surface);padding:.2em .7em .2em 1.5em;font-weight:700;border-radius:3px;text-align:left}'
   '.wc-block-components-product-sale-badge{border-radius:0;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);text-transform:uppercase;border:0}'
   '.woocommerce div.product form.cart .button,.wc-block-components-button:not(.is-link){border-radius:0;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);text-transform:uppercase;font-family:var(--wp--preset--font-family--display);font-weight:700;letter-spacing:.05em}'
   '.wc-block-components-text-input input,.wc-block-components-select select,.woocommerce .quantity .qty{border-radius:0!important;border:2px solid var(--wp--preset--color--contrast)!important}'
   '.woocommerce-tabs .tabs{display:none}.thrift-decade{text-transform:none!important}'
  ),
 },
 'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                   {'area': 'uncategorized', 'name': 'notice', 'title': 'Buying day bar'}],
 'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Thrift
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A catalogue-style shop theme for vintage clothing sellers who list one-off pieces by decade, label size and flat measurements.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: thrift
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')


def variation(fname, title, rows, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)


variation('y2k', 'Y2K', [('base', '#D9DCE0', 'Silver'), ('contrast', '#16171A', 'Ink'), ('accent', '#C2185B', 'Tag pink'),
    ('surface', '#F4F5F7', 'Card'), ('line', '#16171A', 'Rule'), ('muted', '#4A4D55', 'Faded ink'), ('accent-2', '#9FA6B2', 'Chrome')])
variation('seventies', '70s', [('base', '#EFE3C8', 'Mustard paper'), ('contrast', '#3B2314', 'Brown'), ('accent', '#A0520F', 'Rust'),
    ('surface', '#FAF4E6', 'Card'), ('line', '#3B2314', 'Rule'), ('muted', '#6B4E36', 'Faded brown'), ('accent-2', '#D9A441', 'Mustard')],
    {'elements': {'heading': {'typography': {'fontWeight': '700', 'letterSpacing': '0.02em'}}}})
variation('military', 'Military', [('base', '#C9C6A8', 'Olive drab paper'), ('contrast', '#1E2116', 'Ink'), ('accent', '#6A3A12', 'Leather'),
    ('surface', '#E7E4CC', 'Card'), ('line', '#1E2116', 'Rule'), ('muted', '#3F4230', 'Faded olive'), ('accent-2', '#6B6B3F', 'Olive')],
    {'elements': {'heading': {'typography': {'letterSpacing': '0.08em', 'fontWeight': '700'}}}})


def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})


section('decades', 'Decade numerals', ['core/paragraph', 'core/group'],
        {'typography': {**cond, 'textTransform': 'none', 'fontSize': FS('display'), 'fontWeight': '800', 'lineHeight': '0.82', 'letterSpacing': '-0.02em'},
         'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent')}}}},
         'css': '&{display:flex;flex-wrap:wrap;justify-content:space-between;column-gap:.2em}& a:hover{text-decoration:underline;text-decoration-thickness:.06em;text-underline-offset:.08em}'})
section('swing-tag', 'Swing tag', ['core/paragraph'],
        {'color': {'background': C('accent'), 'text': C('surface')},
         'typography': {'fontWeight': '700', 'fontSize': FS('small')}, 'border': {'radius': '3px'},
         'elements': {'link': {'color': {'text': C('surface')}}},
         'css': '&{display:inline-block;padding:.2em .8em .2em 1.6em!important;background:radial-gradient(circle at .8em 50%,var(--wp--preset--color--base) .24em,transparent .27em),var(--wp--preset--color--accent)!important}'})
section('sold-tag', 'Sold tag', ['core/paragraph'],
        {'color': {'background': C('contrast'), 'text': C('base')}, 'typography': {'fontWeight': '700', 'fontSize': FS('small'), 'textTransform': 'uppercase', 'letterSpacing': '0.06em'},
         'css': '&{display:inline-block;padding:.2em .7em!important}'})
section('flip-tile', 'Product tile with back view', ['core/group'], {'spacing': {'blockGap': SP('20')}})
section('catalogue-rule', 'Catalogue rule (double line)', ['core/group', 'core/columns'],
        {'border': {'top': {'color': C('line'), 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'top': SP('30')}},
         'css': '&{box-shadow:inset 0 5px 0 -3px var(--wp--preset--color--base),inset 0 6px 0 -3px var(--wp--preset--color--line)}'})
section('card', 'White card', ['core/group', 'core/columns'],
        {'color': {'background': C('surface'), 'text': C('contrast')},
         'spacing': {'padding': {'top': SP('50'), 'bottom': SP('50'), 'left': SP('40'), 'right': SP('40')}}})
section('ink', 'Ink panel', ['core/group', 'core/columns'],
        {'color': {'background': C('contrast'), 'text': C('base')},
         'elements': {'link': {'color': {'text': C('base')}}, 'heading': {'color': {'text': C('base')}},
                      'button': {'color': {'background': C('accent'), 'text': C('surface')}, 'border': {'color': C('accent')}}},
         'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60'), 'left': SP('40'), 'right': SP('40')}}})
section('red-bar', 'Red notice bar', ['core/group'],
        {'color': {'background': C('accent'), 'text': C('surface')}, 'typography': {'fontWeight': '600', 'fontSize': FS('small')},
         'elements': {'link': {'color': {'text': C('surface')}}},
         'spacing': {'padding': {'top': SP('20'), 'bottom': SP('20')}}})
section('measure-table', 'Measurement table', ['core/table'],
        {'typography': {'fontSize': FS('medium')}, 'css': '& td:not(:first-child),& th:not(:first-child){text-align:right}& td:first-child{font-weight:600}'})
section('brand-list', 'Brand list', ['core/paragraph'],
        {'typography': {**cond, 'fontSize': FS('x-large'), 'fontWeight': '700', 'lineHeight': '1.05'},
         'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent')}}}}})

section('rows', 'Catalogue rows (instead of a table)', ['core/group'],
        {'css': ('& > .wp-block-group{border-bottom:1px solid var(--wp--preset--color--line);padding:.5em 0!important;margin:0!important;column-gap:1rem!important;row-gap:.1rem!important}'
                 '& > .wp-block-group:first-child{border-top:3px solid var(--wp--preset--color--line)}& > .wp-block-group > p{margin:0!important}'
                 '& > .wp-block-group > p:first-child{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-weight:700;font-size:1.1em;letter-spacing:.02em}'
                 '& > .wp-block-group > p:last-child:not(:first-child){text-align:right;font-variant-numeric:tabular-nums}')})


def rows(items, min_w='7rem', cls='is-style-rows', **kw):
    n = max(len(r) for r in items)
    return group(J(*[group(J(*[para(c) for c in r]), layout={'type': 'grid', 'columnCount': n, 'minimumColumnWidth': min_w}) for r in items]),
                 className=cls, layout={'type': 'default'}, **kw)


# ---------------------------------------------------------------- content data
SHOP = {'name': 'Second Floor Vintage', 'addr': '61 Oldham Street, second floor, Manchester M1 1JR', 'email': 'rail@example.com', 'phone': '0161 496 0733'}
DECADES = [('40s', '40s'), ('50s', '50s'), ('60s', '60s'), ('70s', '70s'), ('80s', '80s'), ('90s', '90s'), ('Y2K', 'y2k')]

# name, image, back image, decade cat, price, stock, label size, chest, shoulder, length, sleeve, condition, flaw, desc, alt
P = [
 ('1940s US Army wool flannel shirt, label size 15.5', 'shirt-front.jpg', 'shirt-back.jpg', '40s', '85', 1, '15.5 neck', 58, 46, 76, 60,
  'Very good', 'Two moth nips on the left cuff, darned. Faint stamp inside the yoke.', 'Olive drab wool flannel with two flap pockets and a coat-style front. Soft from washing, still heavy. Fits a modern men\'s medium or a loose women\'s large.',
  'Olive wool flannel army shirt laid flat on grey, front view'),
 ('1950s US Army M-1943 field jacket, label size 38R', 'field-jacket.jpg', 'jacket-od.jpg', '50s', '140', 1, '38 regular', 60, 47, 74, 62,
  'Good', 'Fraying at both cuff edges and one replaced button on the storm flap.', 'Four-pocket cotton sateen field jacket with the drawstring waist intact. Shoulders are narrow for the chest, so check the shoulder measurement against a jacket you own.',
  'Olive M-1943 field jacket on a black dress form'),
 ('1960s French work jacket, bleu de travail, label size 44', 'chore-jacket.jpg', 'chore-jacket.jpg', '60s', '75', 1, '44 French', 59, 48, 72, 61,
  'Good', 'Pale patch on the right elbow where it was worn thin. No holes.', 'Cotton moleskin chore jacket faded to that washed blue. Wrap front, three patch pockets, original buttons.',
  'Faded blue French work jacket on a wooden hanger against a white door'),
 ('1940s US Army field jacket, second type, label size 36', 'jacket-od.jpg', 'field-jacket.jpg', '40s', '120', 1, '36', 56, 44, 66, 60,
  'Fair', 'Stain on the lower back panel, set in. Zip replaced with a period zip.', 'Short olive cotton jacket with slash pockets and button cuffs. Cropped at the waist, so it suits a smaller frame or a tucked shirt.',
  'Short olive army jacket laid flat on a pale grey ground'),
 ('1950s ivory silk blouse with pintucks, label size 14', 'blouse.jpg', 'blouse.jpg', '50s', '58', 1, '14 (1950s UK)', 48, 38, 62, 57,
  'Very good', 'Small yellowed mark under the left arm, only visible up close.', 'Heavy silk crepe with a pintucked front panel and a Peter Pan collar. A 1950s 14 is closer to a modern 10.',
  'Ivory silk blouse with a pintucked front on a dress form'),
 ('1970s embroidered cotton smock dress, label size 12', 'dress.jpg', 'dress.jpg', '70s', '68', 1, '12 (1970s UK)', 50, 37, 104, 22,
  'Very good', 'One embroidered flower on the collar has a loose thread.', 'Unbleached cotton with red cross-stitch on the yoke and a button front to the hem. Short sleeves, loose through the body.',
  'Cream cotton smock dress with embroidered yoke on a dark dress form'),
 ('1990s hooded shell jacket, label size L', 'shell-jacket.jpg', 'shell-jacket.jpg', '90s', '45', 1, 'L', 66, 52, 74, 64,
  'Excellent', 'None we can find.', 'Stone nylon shell with a stowaway hood and taped seams. Roomy, fits a modern large with a jumper under.',
  'Stone-coloured hooded shell jacket laid flat on blue carpet'),
 ('1980s Levi\'s 501 jeans, W32 L30', 'jeans-pocket.jpg', 'jeans-pocket.jpg', '80s', '90', 0, 'W32 L30 (measures W31)', 0, 0, 0, 0,
  'Good', 'Knee blowout repaired from inside.', 'Button fly, grey-black wash. Sold in two days, kept here for the record.',
  'Back pocket of grey 501 jeans with a red tab and arcuate stitching'),
 ('1980s blanket wrap coat, label size M', 'outfit.jpg', 'outfit.jpg', '80s', '72', 1, 'M', 64, 50, 88, 58,
  'Very good', 'Fringe is uneven on the left front, as it came.', 'Wool blend in rust, teal and pink with a fringed hem. One button at the neck, wraps loose.',
  'Woman wearing a patterned blanket wrap coat in rust and teal'),
 ('Early 2000s leather work boots, UK 9', 'boots.jpg', 'boots.jpg', 'Y2K', '40', 1, 'UK 9', 0, 0, 0, 0,
  'Good', 'Creased across the toes, heels have wear on the outer edge.', 'Black leather lace-up boots with a lugged sole. Resoleable. Insole length 28cm.',
  'Black leather lace-up work boots worn with jeans on wooden decking'),
]


def purl(p):
    return '/product/%s/' % slugify(p[0])


def mrows(p):
    return rows([[label, '%d cm, %.1f in' % (v, v / 2.54)] for label, v in [('Chest, pit to pit', p[7]), ('Shoulder', p[8]), ('Length, nape to hem', p[9]), ('Sleeve', p[10])] if v])


def mtable(p):
    rows = []
    for label, v in [('Chest, pit to pit', p[7]), ('Shoulder seam to seam', p[8]), ('Length, nape to hem', p[9]), ('Sleeve, shoulder to cuff', p[10])]:
        if v:
            rows.append([label, '%d cm' % v, '%.1f in' % (v / 2.54)])
    return table(rows, head=['Measured flat', 'cm', 'in'], className='is-style-measure-table')


ALT = {p[1]: p[14] for p in P}
ALT.update({'shirt-back.jpg': 'Back of the olive wool flannel shirt laid flat', 'stamp-detail.jpg': 'Close-up of an inked size stamp on olive wool',
            'shop-rails.jpg': 'Rails of shirts and jackets in a bright shop with hanging lamps', 'shop-floor.jpg': 'A round rail of second-hand clothes in a tiled shop',
            'factory.jpg': 'A 1910 garment factory floor with long cutting tables, black and white'})

# ---------------------------------------------------------------- patterns
pattern('decade-index', 'Shop by decade (giant numerals)', 'featured,shop', group(J(
  para(''.join('<a href="/product-category/%s/">%s</a>' % (s, n) for n, s in DECADES), className='is-style-decades'),
  row(J(para('Shop by decade. Women\'s and men\'s, every piece measured flat.', fontSize='small'),
        para('<a href="/size-guide/">How we measure</a>', fontSize='small')), justify='space-between', className='is-style-catalogue-rule')),
  align='full', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('50'), 'bottom': SP('50'), 'left': SP('40'), 'right': SP('40')}}}),
  description='The signature index: 40s to Y2K as numerals as wide as the page, each linking to that decade.')

pattern('decade-index-compact', 'Decade links (one line)', 'shop', row(J(*[para('<a href="/product-category/%s/">%s</a>' % (s, n), className='is-style-brand-list thrift-decade', fontSize='large') for n, s in DECADES]),
  style={'spacing': {'blockGap': SP('40')}}, align='wide'))


def flip_tile(p):
    tag = para('Sold', className='is-style-sold-tag') if p[5] == 0 else para('£%s' % p[4], className='is-style-swing-tag')
    return group(J(
        group(J(image(p[1], ALT[p[1]], href=purl(p), aspectRatio='4/5', scale='cover'),
                image(p[2], ALT.get(p[2], ALT[p[1]]) + ', second view', href=purl(p), aspectRatio='4/5', scale='cover')), className='flip', layout={'type': 'default'}),
        heading('<a href="%s">%s</a>' % (purl(p), p[0]), 3, fontSize='medium'),
        row(J(tag, para('%s, chest %s' % (p[3], ('%d cm' % (p[7] * 2)) if p[7] else 'n/a'), fontSize='x-small', textColor='muted')), style={'spacing': {'blockGap': SP('20')}})),
        className='is-style-flip-tile', layout={'type': 'default'})


pattern('new-in-grid', 'New in (4 across, back view on hover)', 'shop,featured', group(J(
  row(J(heading('New in this Friday', 2), para('<a href="/shop/">Everything on the rail</a>')), justify='space-between', align='wide', className='is-style-catalogue-rule'),
  group(J(*[flip_tile(P[i]) for i in [0, 4, 6, 1, 5, 2, 8, 7]]), align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '11rem'},
        style={'spacing': {'blockGap': SP('40')}})),
  align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('60')}}}),
  description='One-off pieces with price tags. Hover or focus a piece to see its back.')

pattern('catalogue-entry', 'Catalogue entry (photo, measurements, tag)', 'shop,featured', columns(
  ('55%', image('field-jacket.jpg', ALT['field-jacket.jpg'], aspectRatio='4/5', scale='cover')),
  (None, J(heading('1950s US Army M-1943 field jacket', 2),
     row(J(para('£140', className='is-style-swing-tag'), para('Label 38R. Measures like a modern M.', fontSize='small')), style={'spacing': {'blockGap': SP('30')}}),
     mrows(P[1]),
     para('Condition: good. Fraying at both cuff edges and one replaced button on the storm flap.'),
     buttons(('Buy this jacket', purl(P[1]))))), align='wide', className='is-style-catalogue-rule', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  description='A single piece laid out like an old workwear catalogue page.')

pattern('intro-split', 'Shop intro with photo', 'about,featured', columns(
  (None, J(heading('Second Floor Vintage', 2),
     para('One-off clothes from the 1940s to the early 2000s, up two flights of stairs on Oldham Street. Aoife buys the workwear and military, Kwame buys womenswear and anything with embroidery.'),
     para('Every piece is washed, mended where it can be, and measured flat. We list the label size because it is on the label, and ignore it when we tell you what fits.'),
     buttons(('See this week\'s rail', '/shop/')))),
  ('58%', image('shop-rails.jpg', ALT['shop-rails.jpg'], aspectRatio='3/2', scale='cover')), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}))

pattern('measurement-table', 'Measurement table (one piece)', 'shop', J(mtable(P[0]), para('All measurements taken flat, seam to seam, in centimetres and rounded to the nearest centimetre.', fontSize='x-small', textColor='muted')),
  description='Chest, shoulder, length and sleeve in cm and inches.')

pattern('measuring-guide', 'How we measure (size guide)', 'text', columns(
  (None, J(heading('How we measure', 2),
     para('We lay every piece flat on the cutting table, buttoned or zipped, and measure seam to seam.'),
     lst(['<strong>Chest:</strong> straight across from armpit to armpit. Double it for the full chest.',
          '<strong>Shoulder:</strong> from one shoulder seam to the other, across the back.',
          '<strong>Length:</strong> from the base of the collar at the back (the nape) to the hem.',
          '<strong>Sleeve:</strong> from the shoulder seam to the end of the cuff.'], ordered=True))),
  (None, J(heading('Label size means very little', 3),
     table([['1950s UK 14', 'Modern UK 10'], ['1970s UK 12', 'Modern UK 8 to 10'], ['1980s UK 12', 'Modern UK 10'], ['US Army 38R', 'Modern men\'s M'], ['French 44', 'Modern men\'s M']],
           head=['Label says', 'Usually fits'], className='is-style-measure-table'),
     para('These are rough. The measurements on each piece are what count.', fontSize='small', textColor='muted'))), align='wide'),
  description='The signature size guide: flat measurements explained, with label sizes against modern sizes.')

pattern('compare-tip', 'Compare with a garment you own', 'text', group(J(
  heading('Compare with something you own', 4),
  para('Take a jacket or shirt that fits you well, lay it flat and measure it the same way. If our numbers are within 2cm of yours, it will fit the way yours does.')),
  className='is-style-card', layout={'type': 'default'}))

pattern('flaw-notes', 'Flaw notes with a close-up', 'shop', columns(
  ('35%', image('stamp-detail.jpg', ALT['stamp-detail.jpg'], aspectRatio='1', scale='cover')),
  (None, J(heading('Flaws', 4),
     para('Two moth nips on the left cuff, darned by us in matching wool. Faint size stamp inside the yoke (shown). The rest of the shirt is clean.'),
     para('Flaw photos are always the last ones in the gallery.', fontSize='x-small', textColor='muted'))), className='is-style-catalogue-rule'))

pattern('one-of-one-note', 'One of one note', 'shop', para(
  'One of one. When it sells it stays on the site marked sold, so you can see what has been through the shop.', fontSize='small', textColor='muted'))

pattern('sold-archive', 'Recently sold', 'shop,gallery', group(J(
  heading('Recently sold', 2),
  group(J(*[group(J(image(p[1], ALT[p[1]], aspectRatio='4/5', scale='cover'), para('Sold', className='is-style-sold-tag'), para(p[0], fontSize='small')),
                  layout={'type': 'default'}) for p in [P[7], P[3], P[5]]]),
        layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '10rem'}, align='wide')),
  align='wide', layout={'type': 'default'}))

BRANDS = ['Carhartt', 'Levi\'s', 'Barbour', 'Pendleton', 'Lee', 'Wrangler', 'Dickies', 'Le Laboureur', 'US Army', 'Laura Ashley', 'St Michael', 'Burberrys']
pattern('brand-index', 'Shop by brand', 'shop', group(J(
  heading('By brand', 2),
  para(', '.join('<a href="/?s=%s&amp;post_type=product">%s</a>' % (slugify(b), b) for b in BRANDS), className='is-style-brand-list')),
  align='wide', className='is-style-catalogue-rule', layout={'type': 'default'}))

pattern('buying-days', 'Buying days', 'text', group(J(
  heading('Buying days', 2),
  para('First Monday of every month, 11am to 3pm. Bring up to two bags, washed. We look while you wait and pay cash or 20% more in credit.'),
  rows([['Monday 6 October', '11am to 3pm'], ['Monday 3 November', '11am to 3pm'], ['Monday 1 December', '11am to 3pm']]),
  para('We need photo ID for every purchase. It is a condition of our dealer licence.', fontSize='small')),
  className='is-style-card', align='wide', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('what-we-buy', 'What we buy and what we pass on', 'text', columns(
  (None, J(heading('We buy', 3), lst(['Workwear, chore jackets and overalls', 'Military clothing with its labels', 'Dresses and blouses from the 40s to the 70s', 'Wool coats and knitwear without moth', 'Denim with a story, any condition']))),
  (None, J(heading('We pass on', 3), lst(['High-street clothes from after 2005', 'Anything that smells of damp', 'Suits, unless they are pre-1970', 'Shoes, except boots']))), align='wide'))

pattern('visit', 'Visit the shop', 'contact', columns(
  ('55%', image('shop-floor.jpg', ALT['shop-floor.jpg'], aspectRatio='16/10', scale='cover')),
  (None, J(heading('Visit', 2),
     para('%s. Buzz 2 at the green door next to the barber. Two flights of stairs and no lift, sorry. If you cannot manage the stairs, call and we will bring rails down on a Wednesday morning.' % SHOP['addr']),
     rows([['Mon and Tue', 'Closed'], ['Wed to Sat', '11am to 6pm'], ['Sun', '12pm to 5pm']]),
     para('<a href="tel:01614960733">%s</a>, <a href="mailto:%s">%s</a>' % (SHOP['phone'], SHOP['email'], SHOP['email'])))), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}))

pattern('shipping-returns', 'Shipping and returns', 'shop', J(
  heading('Shipping', 2),
  table([['UK, tracked 48', '£4.50'], ['UK, next day', '£8'], ['Europe', '£16'], ['USA and Canada', '£24']], head=['Where', 'Cost'], className='is-style-measure-table'),
  para('Orders placed by 2pm Wednesday to Saturday go out the same day, folded in tissue in a recycled mailer.'),
  heading('Returns', 2),
  para('Return within 14 days of delivery if it does not fit. We refund the price, not the postage. Check the measurements before you buy; we will happily measure anything else you need.')))

pattern('gift-card', 'Gift cards', 'shop', columns(
  (None, J(heading('Gift cards', 3), para('For people who are hard to size. £20, £50 or £100, spent online or on the second floor, valid for two years.'), buttons(('Buy a gift card', '/product-category/gift-cards/')))),
  (None, image('stamp-detail.jpg', ALT['stamp-detail.jpg'], aspectRatio='16/10', scale='cover')), align='wide', className='is-style-catalogue-rule'))

pattern('deadstock-note', 'Deadstock label', 'shop', group(J(
  para('Deadstock', className='is-style-sold-tag'),
  para('Never worn. Found in a warehouse or a shop stockroom, still with its original tags or folds. Priced a little higher than worn pieces of the same age.', fontSize='small')),
  layout={'type': 'flex', 'flexWrap': 'wrap', 'verticalAlignment': 'center'}))

pattern('care-notes', 'Care notes', 'text', J(
  heading('Looking after old clothes', 3),
  lst(['Wool: cold hand wash, dry flat, and a cedar block in the wardrobe for moths.', 'Military cotton: 30 degrees, inside out, line dry. It will fade, which is the point.', 'Silk: hand wash cold or dry clean. Never wring it.', 'Leather boots: brush, then wax twice a season.'])))

pattern('notice-buying-day', 'Notice: next buying day', 'banner', group(
  para('Buying day this Monday, 6 October, 11am to 3pm. Two bags per person, washed, with photo ID. Take this bar out on Tuesday.'),
  className='is-style-red-bar', align='full', layout={'type': 'constrained'}),
  description='A bar for the week of a buying day. Edit the date and remove it afterwards.')

pattern('newsletter', 'Friday drop email', 'call-to-action', group(J(
  heading('The Friday drop', 2),
  para('New pieces go up on Friday at noon. The email goes out at 11am with photos and measurements, so subscribers get an hour first.'),
  buttons(('Get the Friday email', 'mailto:%s?subject=Friday%%20drop' % SHOP['email']))),
  className='is-style-ink', align='full', layout={'type': 'constrained'}, anchor='newsletter'))

pattern('about-shop', 'About the shop', 'about', columns(
  ('45%', image('factory.jpg', ALT['factory.jpg'], caption='A garment factory in Allentown, 1910. Most of what we sell was cut on tables like these.')),
  (None, J(heading('About', 2),
     para('Aoife Brennan and Kwame Asante opened Second Floor Vintage in 2017, after five years selling from a market stall on Tib Street. The shop is one long room above a barber, with the cutting table where we measure everything by the window.'),
     para('We would rather sell you one jacket that fits than three that nearly do. That is why every listing has four measurements and a sentence about who it suits.'),
     para('We do not sell reproductions, and we say so when a piece has been altered.'))), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}))

pattern('quote-customer', 'Customer note', 'testimonials', quote(
  'Bought the field jacket off the measurements alone and it fits better than anything I have tried on in a shop.',
  'Rhys, Levenshulme, September 2025'))

pattern('journal-list', 'Journal (latest posts)', 'posts,query', group(J(
  row(J(heading('From the cutting table', 2), para('<a href="/journal/">The journal</a>')), justify='space-between', align='wide', className='is-style-catalogue-rule'),
  query(J(dyn('post-featured-image', isLink=True, aspectRatio='3/2', scale='cover'), dyn('post-date'), dyn('post-title', isLink=True, level=3)),
        per_page=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'}, align='wide')),
  align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60')}}}))

pattern('post-grid', 'Journal grid (inherits query)', 'posts,query', inherit_query(
  J(dyn('post-featured-image', isLink=True, aspectRatio='3/2', scale='cover'), dyn('post-date'), dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', excerptLength=22)),
  layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}, align='wide'), inserter=False)

pattern('post-list', 'Results list', 'posts,query', inherit_query(
  group(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-date')), className='is-style-catalogue-rule', layout={'type': 'default'}), align='wide'), inserter=False)


# ---------------------------------------------------------------- round 2
KINDS = [('Jackets', 'field-jacket.jpg'), ('Shirts', 'shirt-front.jpg'), ('Dresses', 'dress.jpg'), ('Blouses', 'blouse.jpg'), ('Denim', 'jeans-pocket.jpg'), ('Boots', 'boots.jpg')]
pattern('category-tiles', 'Shop by garment', 'shop,featured', group(J(
  heading('By garment', 2),
  group(J(*[group(J(image(img, ALT[img], href='/?s=%s&post_type=product' % k.lower().rstrip('s'), aspectRatio='4/5', scale='cover'), heading('<a href="/?s=%s&amp;post_type=product">%s</a>' % (k.lower().rstrip('s'), k), 3, fontSize='large')), layout={'type': 'default'}) for k, img in KINDS]),
        align='wide', layout={'type': 'grid', 'columnCount': 6, 'minimumColumnWidth': '9rem'}, style={'spacing': {'blockGap': SP('30')}})),
  align='wide', className='is-style-catalogue-rule', layout={'type': 'default'}), description='Six garment types, each a photo and a search link.')
pattern('womens-mens', 'Women\'s and men\'s', 'shop,featured', columns(
  (None, J(image('dress.jpg', ALT['dress.jpg'], aspectRatio='4/5', scale='cover'), heading('<a href="/?s=dress&amp;post_type=product">Women\'s</a>', 2), para('Dresses, blouses, coats and knitwear, 1940s to the early 2000s. Kwame buys it.'))),
  (None, J(image('field-jacket.jpg', ALT['field-jacket.jpg'], aspectRatio='4/5', scale='cover'), heading('<a href="/?s=jacket&amp;post_type=product">Men\'s</a>', 2), para('Workwear, military, shirts and boots. Aoife buys it.'))),
  align='wide', style={'spacing': {'blockGap': {'left': SP('40')}}}), description='Two big photos, women\'s and men\'s, with who buys each.')
pattern('piece-of-the-week', 'Piece of the week', 'shop,featured', columns(
  ('50%', gallery([('shirt-front.jpg', ALT['shirt-front.jpg'], 'Front'), ('shirt-back.jpg', ALT['shirt-back.jpg'], 'Back'), ('stamp-detail.jpg', ALT['stamp-detail.jpg'], 'Size stamp')], columns=2)),
  (None, J(heading('Piece of the week: 1940s army flannel shirt', 2),
     para('Olive wool flannel, coat front, two flap pockets. Heavy, soft from washing, and the moth nips on the cuff are darned in matching wool. Label 15.5, fits a modern men\'s medium.'),
     mrows(P[0]), row(J(para('£85', className='is-style-swing-tag'), para('<a href="%s">See the listing</a>' % purl(P[0]))), style={'spacing': {'blockGap': SP('30')}}))),
  align='wide', className='is-style-catalogue-rule', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  description='One piece shown front, back and detail, with its measurements. Click a photo to open it.')
pattern('dating-guide', 'How we date a garment', 'text', group(J(
  heading('How we date a piece', 2),
  para('Labels and hardware tell you more than the cut. These are the clues we check first.'),
  rows([['Union label', 'A small cloth union tag in US workwear usually means before the late 1980s.'], ['Care label', 'UK care labels became common in the early 1970s. None at all often means older.'],
        ['Zip', 'Metal zips with a maker\'s name on the pull point to the 50s and 60s. Plastic coil zips arrive in the 70s.'], ['Size format', 'Chest sizes in inches on women\'s clothes are usually pre-1970. Dress sizes 10 to 16 take over after that.'],
        ['Stock number', 'Army clothing carries a stock or contract number and a date stamp inside.']], min_w='9rem')),
  layout={'type': 'constrained', 'justifyContent': 'left'}), description='Label, zip and stamp clues used to date clothing.')
pattern('fabric-notes', 'Fabric notes', 'text', columns(
  (None, J(heading('Wool flannel', 4), para('Warm, heavy, forgives creases. Moths love it; keep cedar in the wardrobe.'))),
  (None, J(heading('Cotton sateen', 4), para('The shiny army cotton. Fades to a soft green with every wash.'))),
  (None, J(heading('Moleskin', 4), para('Dense brushed cotton in French work jackets. Wears pale at the elbows and cuffs.'))),
  (None, J(heading('Silk crepe', 4), para('Matte and heavy. Hand wash cold, never wring.'))), align='wide', className='is-style-catalogue-rule'))
pattern('alterations', 'Alterations and repairs', 'services', columns(
  (None, J(heading('Alterations and repairs', 2), para('Kwame takes in, lets out and mends on a 1970s Singer at the back of the shop. Anything bought here gets its first alteration free.'),
     rows([['Take in a waist', '£18'], ['Shorten sleeves', '£22'], ['Darn a moth hole', '£6 each'], ['Replace a zip', '£20']]))),
  (None, image('stamp-detail.jpg', ALT['stamp-detail.jpg'], aspectRatio='4/5', scale='cover')), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  description='Repairs and alterations with prices.')
pattern('costume-hire', 'Hire for film and theatre', 'services', group(J(
  heading('Hire for film, stage and photo shoots', 2),
  para('We hire pieces by the week to costume departments and stylists. Military and workwear are what people ask for most. A deposit of the sale price, returned when it comes back clean.'),
  rows([['One week', '20% of the sale price'], ['Two weeks', '30% of the sale price'], ['Whole rail for a production', 'Ask us']]),
  buttons(('Email about hire', 'mailto:%s?subject=Hire' % SHOP['email']))),
  className='is-style-card', align='wide', layout={'type': 'constrained', 'justifyContent': 'left'}), description='Costume hire terms for productions and shoots.')
pattern('styling-appointment', 'Book a quiet hour', 'services', group(J(
  heading('Book a quiet hour', 2),
  para('Wednesday mornings before we open, we will pull pieces in your size and decade and leave you to try them on. Free, one person at a time, an hour each.'),
  buttons(('Email to book a Wednesday', 'mailto:%s?subject=Quiet%%20hour' % SHOP['email']))),
  className='is-style-ink', align='full', layout={'type': 'constrained'}))
pattern('markets', 'Where we pop up', 'events', group(J(
  heading('Markets and pop-ups', 2),
  rows([['Sat 18 Oct', 'Levenshulme Market', 'Two rails of workwear and knitwear.'], ['Sun 2 Nov', 'Makers Market, Piccadilly', 'Military and outerwear only.'], ['Sat 6 Dec', 'Christmas vintage fair, Victoria Baths', 'The full shop on 12 rails.']], min_w='9rem')),
  layout={'type': 'default'}), description='Market dates and what we bring.')
pattern('wanted', 'Wanted list', 'shop', group(J(
  heading('On our wanted list', 3),
  lst(['French chore jackets in moleskin, any size', 'Barbour Bedale and Beaufort, even worn through', '1970s embroidered smock dresses', 'Wool army shirts with stamps intact']),
  para('Got one? Bring it on a buying day or email a photo.', fontSize='small')), className='is-style-card', layout={'type': 'default'}))
pattern('lookbook', 'Lookbook (photos open large)', 'gallery', J(
  heading('Autumn rail', 2, align='wide'),
  gallery([('outfit.jpg', ALT['outfit.jpg'], 'Blanket wrap coat, 80s'), ('chore-jacket.jpg', ALT['chore-jacket.jpg'], 'Bleu de travail, 60s'),
           ('blouse.jpg', ALT['blouse.jpg'], 'Silk blouse, 50s'), ('shell-jacket.jpg', ALT['shell-jacket.jpg'], 'Shell jacket, 90s')], columns=4, align='wide')),
  description='Four pieces from the current rail. Click to open.')
pattern('detail-strip', 'Details: labels, seams and wear', 'gallery', gallery([
  ('stamp-detail.jpg', ALT['stamp-detail.jpg'], 'Size stamp'), ('jeans-pocket.jpg', ALT['jeans-pocket.jpg'], 'Arcuate stitching'), ('shirt-back.jpg', ALT['shirt-back.jpg'], 'Back yoke')], columns=3, align='wide'),
  description='Close-ups of labels and construction. Click to open.')
pattern('size-finder', 'Size finder: chest to modern size', 'text', group(J(
  heading('From chest to modern size', 3),
  rows([['Chest 48 to 50 cm flat', 'Women\'s UK 8 to 10'], ['Chest 52 to 55 cm flat', 'Women\'s UK 12 to 14, men\'s XS'], ['Chest 56 to 59 cm flat', 'Men\'s S to M'], ['Chest 60 to 63 cm flat', 'Men\'s M to L'], ['Chest 64 cm and up', 'Men\'s L and up']])),
  layout={'type': 'default'}), description='A rough guide from flat chest measurement to modern size.')
pattern('staff', 'Who is behind the rails', 'about', columns(
  (None, J(heading('Aoife Brennan', 3), para('Buys menswear, workwear and military. Knows a stock number by sight. Will talk you out of a jacket that does not fit.'))),
  (None, J(heading('Kwame Asante', 3), para('Buys womenswear and anything embroidered. Does the alterations on a Singer older than both of us.'))), align='wide', className='is-style-catalogue-rule'))
pattern('faq', 'Questions people ask', 'text', group(J(
  heading('Questions', 2),
  details('Can I try things on?', para('Yes, in the shop, behind a curtain made from an old parachute.')),
  details('Do you hold pieces?', para('For 24 hours if you call. One-offs sell fast.')),
  details('Why is the label size different from the fit?', para('Sizes shrank over the decades. Read the measurements and the size guide.')),
  details('Do you clean everything?', para('Yes. Wool is aired and steamed, cotton washed, leather conditioned.'))),
  layout={'type': 'constrained', 'justifyContent': 'left'}))
pattern('hero-piece', 'Hero: one piece with its measurements', 'featured,banner', columns(
  ('45%', image('field-jacket.jpg', ALT['field-jacket.jpg'], aspectRatio='4/5', scale='cover')),
  (None, J(heading('New this Friday: 1950s M-1943 field jacket', 1, fontSize='x-large'), mrows(P[1]), row(J(para('£140', className='is-style-swing-tag'), para('<a href="%s">Buy it</a>' % purl(P[1]))), style={'spacing': {'blockGap': SP('30')}}))),
  align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}), description='An alternative opening: one piece, its measurements and price.')

# page layouts
pattern('page-decades', 'Page: by decade', 'shop', J(
  para('Every piece is filed under the decade it was made, as close as the labels and construction let us date it. When we are guessing, the listing says so.'),
  pattern_ref('decade-index'), pattern_ref('catalogue-entry'), pattern_ref('brand-index'), pattern_ref('sold-archive')), block_types='core/post-content')
pattern('page-size-guide', 'Page: size guide', 'text', J(pattern_ref('measuring-guide'), pattern_ref('size-finder'), pattern_ref('compare-tip'), pattern_ref('measurement-table'), pattern_ref('dating-guide'), pattern_ref('fabric-notes'), pattern_ref('care-notes')), block_types='core/post-content')
pattern('page-buying', 'Page: buying days', 'text', J(
  para('We buy from the public once a month and from house clearances by arrangement.', fontSize='large'),
  pattern_ref('buying-days'), pattern_ref('what-we-buy'), pattern_ref('wanted')), block_types='core/post-content')
pattern('page-visit', 'Page: visit', 'contact', J(pattern_ref('visit'), pattern_ref('markets'), pattern_ref('about-shop'), pattern_ref('staff'), pattern_ref('quote-customer'), pattern_ref('faq')), block_types='core/post-content')
pattern('page-services', 'Page: alterations, hire and quiet hours', 'services', J(pattern_ref('alterations'), pattern_ref('costume-hire'), pattern_ref('styling-appointment')), block_types='core/post-content')
pattern('page-lookbook', 'Page: lookbook', 'gallery', J(pattern_ref('lookbook'), pattern_ref('piece-of-the-week'), pattern_ref('detail-strip'), pattern_ref('womens-mens')), block_types='core/post-content')
pattern('page-shipping', 'Page: shipping and returns', 'shop', J(pattern_ref('shipping-returns'), pattern_ref('gift-card')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(J(
  row(J(stack(J(dyn('site-title', level=0), dyn('site-tagline')), style={'spacing': {'blockGap': SP('10')}}),
        dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}, overlayMenu='mobile', style={'spacing': {'blockGap': SP('40')}})),
      justify='space-between', align='wide', wrap=False)),
  tag='header', align='full', className='is-style-catalogue-rule', layout={'type': 'constrained'},
  style={'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}}}))
write('parts/notice.html', pattern_ref('notice-buying-day'))
write('parts/footer.html', group(J(
  pattern_ref('decade-index-compact'),
  columns(
    (None, J(heading('Second Floor Vintage', 4), para('%s<br>Wed to Sat 11 to 6, Sun 12 to 5<br><a href="tel:01614960733">%s</a>' % (SHOP['addr'], SHOP['phone']), fontSize='small'))),
    (None, J(heading('Help', 4), para('<a href="/size-guide/">Size guide</a><br><a href="/shipping/">Shipping and returns</a><br><a href="/buying-days/">Sell to us</a><br><a href="/services/">Alterations and hire</a><br><a href="/lookbook/">Lookbook</a>', fontSize='small'))),
    (None, J(heading('Friday drop', 4), para('New pieces every Friday at noon, by email an hour earlier. <a href="mailto:%s?subject=Friday%%20drop">Sign up</a>' % SHOP['email'], fontSize='small'))),
    align='wide', className='is-style-catalogue-rule'),
  para('Demo photographs are CC0 and public domain images from Wikimedia Commons, including garments from a French military museum collection, used as stand-ins.', fontSize='x-small', textColor='muted', align='wide')),
  tag='footer', align='full', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': SP('70'), 'bottom': SP('50')}, 'blockGap': SP('50')}}))


# ---------------------------------------------------------------- templates
def main(inner, pad_top='50', **kw):
    return group(inner, tag='main', style={'spacing': {'padding': {'top': SP(pad_top), 'bottom': SP('70')}}}, layout={'type': 'constrained'}, **kw)


def tpl(name, inner):
    write('templates/%s.html' % name, J(template_part('header', 'header'), inner, template_part('footer', 'footer')))


tpl('front-page', group(J(pattern_ref('decade-index'), pattern_ref('new-in-grid'), pattern_ref('category-tiles'), pattern_ref('piece-of-the-week'), pattern_ref('womens-mens'),
    pattern_ref('intro-split'), pattern_ref('brand-index'), pattern_ref('journal-list'), pattern_ref('newsletter')), tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': SP('60')}}))
tpl('page', main(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'}))))
tpl('page-wide', main(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'}))))
tpl('single', main(J(dyn('post-date'), dyn('post-title', level=1, align='wide'), dyn('post-featured-image', align='wide', aspectRatio='16/9', scale='cover'),
    dyn('post-content', layout={'type': 'constrained'}), dyn('post-terms', term='category', prefix='Filed under '),
    row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)), justify='space-between', align='wide', className='is-style-catalogue-rule'))))
tpl('home', main(J(heading('Journal', 1, align='wide'), dyn('categories', className='is-style-brand-list'), pattern_ref('post-grid'))))
tpl('index', main(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-grid'))))
tpl('archive', main(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('post-grid'))))
tpl('search', main(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Barbour, 70s dress, chore jacket', buttonText='Search'), pattern_ref('post-list'))))
tpl('404', main(J(heading('Sold, or never here', 1),
    para('That page is gone. If it was a piece of clothing, it has probably sold. Try the <a href="/shop/">current rail</a> or search.'),
    dyn('search', label='Search', showLabel=False, placeholder='Barbour, 70s dress, chore jacket', buttonText='Search')), pad_top='70'))


def product_collection(per_page=16, cols=4):
    q = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'product', 'order': 'desc', 'orderBy': 'date', 'search': '', 'exclude': [],
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
        json.dumps(a, separators=(',', ':')), tmpl, para('Nothing from this decade on the rail right now. New pieces go up every Friday at noon.'))


for name in ('archive-product', 'taxonomy-product_cat', 'product-search-results'):
    tpl(name, main(J(dyn('woocommerce/store-notices'), dyn('query-title', type='archive', showPrefix=False, align='wide'), pattern_ref('decade-index-compact'),
                     dyn('term-description', align='wide'), product_collection()), pad_top='40'))

tpl('single-product', main(J(
  dyn('woocommerce/store-notices'),
  columns(('55%', dyn('woocommerce/product-image', showProductLink=False, showSaleBadge=True, imageSizing='single', isDescendentOfSingleProductTemplate=True, aspectRatio='4/5', scale='cover')),
          (None, J(dyn('post-title', level=1, fontSize='x-large', __woocommerceNamespace='woocommerce/product-query/product-title'),
                   dyn('woocommerce/product-price', isDescendentOfSingleProductTemplate=True, fontSize='large'),
                   dyn('post-excerpt', __woocommerceNamespace='woocommerce/product-query/product-summary'),
                   dyn('woocommerce/add-to-cart-form'),
                   pattern_ref('one-of-one-note'),
                   dyn('woocommerce/product-details'),
                   pattern_ref('compare-tip'))),
          align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  pattern_ref('decade-index-compact')), pad_top='40'))

print('thrift built:', len(os.listdir(os.path.join(D, 'patterns'))), 'patterns')

# ---------------------------------------------------------------- demo
def pdesc(p):
    parts = [para(p[13])]
    if p[7]:
        parts.append(mtable(p))
    parts.append(para('<strong>Label size:</strong> %s. <strong>Condition:</strong> %s. <strong>Flaws:</strong> %s' % (p[6], p[11].lower(), p[12])))
    return J(*parts)


def pshort(p):
    if p[7]:
        return 'Label %s. Chest %d cm pit to pit, length %d cm. %s condition.' % (p[6], p[7], p[9], p[11])
    return 'Label %s. %s condition.' % (p[6], p[11])


demo = {
 'site': {'title': 'Second Floor Vintage', 'tagline': 'One-off clothes, 1940s to 2000s, measured flat'},
 'categories': [{'slug': 'buying-trips', 'name': 'Buying trips'}, {'slug': 'on-the-table', 'name': 'On the cutting table'}],
 'front_page': 'home', 'posts_page': 'journal',
 'pages': [
  {'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'journal', 'title': 'Journal', 'content': ''},
  {'slug': 'decades', 'title': 'By decade', 'pattern': 'thrift/page-decades', 'template': 'page-wide'},
  {'slug': 'size-guide', 'title': 'Size guide', 'pattern': 'thrift/page-size-guide', 'template': 'page-wide'},
  {'slug': 'buying-days', 'title': 'Buying days', 'pattern': 'thrift/page-buying', 'template': 'page-wide'},
  {'slug': 'visit', 'title': 'Visit', 'pattern': 'thrift/page-visit', 'template': 'page-wide'},
  {'slug': 'shipping', 'title': 'Shipping and returns', 'pattern': 'thrift/page-shipping'},
  {'slug': 'services', 'title': 'Alterations and hire', 'pattern': 'thrift/page-services', 'template': 'page-wide'},
  {'slug': 'lookbook', 'title': 'Lookbook', 'pattern': 'thrift/page-lookbook', 'template': 'page-wide'},
 ],
 'posts': [
  {'title': 'A van full of French work jackets from Lille', 'category': 'buying-trips', 'image': 'chore-jacket.jpg', 'content': J(
     para('Aoife drove back from Lille with 60 bleu de travail jackets from a closing uniform supplier. About half are moleskin, the rest cotton drill. They go on the rail in batches of ten, starting this Friday.'),
     para('The supplier had kept every size from 40 to 56, so for once we have the same jacket in a run of sizes. Measurements differ a little from jacket to jacket because they shrank differently in the wash.'), pattern_ref('fabric-notes'), pattern_ref('lookbook'))},
  {'title': 'Mending moth nips in army flannel', 'category': 'on-the-table', 'image': 'shirt-front.jpg', 'content': J(
     para('Small moth holes in wool flannel darn well with a single strand of matching wool and a lot of patience. We charge nothing extra for mending, and we note every repair in the listing.'), pattern_ref('flaw-notes'), pattern_ref('alterations'))},
  {'title': 'Why a 1950s size 14 fits like a modern 10', 'category': 'on-the-table', 'image': 'blouse.jpg', 'content': J(
     para('UK sizing was redrawn several times after the war, and every redraw made the numbers smaller for the same body. That is why we list the label and then ignore it.'), pattern_ref('size-finder'), pattern_ref('compare-tip'))},
  {'title': 'The field jacket that came with a letter in the pocket', 'category': 'buying-trips', 'image': 'field-jacket.jpg', 'content': J(
     para('A 1950s M-1943 from a house clearance in Stockport had a folded letter in the inside pocket, dated 1954. We gave the letter back to the family and kept the jacket.'), pattern_ref('catalogue-entry'), pattern_ref('dating-guide'))},
  {'title': 'Buying day notes: what we took and what we passed on', 'category': 'buying-trips', 'image': 'shop-floor.jpg', 'content': J(
     para('Forty people came up the stairs last Monday. We bought from 23 of them. Most of the no pile was high-street denim from the last ten years, which we cannot sell for more than you paid.'), pattern_ref('what-we-buy'), pattern_ref('buying-days'))},
  {'title': 'Photographing flaws before anything else', 'category': 'on-the-table', 'image': 'stamp-detail.jpg', 'content': J(
     para('Every piece gets its flaw photos taken first, before the nice ones. It stops us forgetting, and it means the last pictures in each gallery are the honest ones.'), pattern_ref('detail-strip'), pattern_ref('one-of-one-note'))},
  {'title': 'Costume hire for a BBC period drama', 'category': 'buying-trips', 'image': 'jacket-od.jpg', 'content': J(
     para('A costume department borrowed thirty army jackets and shirts for six weeks of filming in Salford. Everything came back, two with extra mud.'), pattern_ref('costume-hire'))},
 ],
 'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'By decade', 'url': '/decades/'}, {'label': 'Size guide', 'url': '/size-guide/'},
         {'label': 'Buying days', 'url': '/buying-days/'}, {'label': 'Lookbook', 'url': '/lookbook/'}, {'label': 'Hire', 'url': '/services/'}, {'label': 'Journal', 'url': '/journal/'}, {'label': 'Visit', 'url': '/visit/'}],
 'currency': 'GBP',
 'products': [{'name': p[0], 'price': p[4], 'image': p[1], 'category': p[3], 'sku': 'SFV-%d' % (400 + i * 7), 'stock': p[5],
               'short': pshort(p), 'description': pdesc(p)} for i, p in enumerate(P)] + [
   {'name': 'Gift card, £50', 'price': '50', 'image': 'stamp-detail.jpg', 'category': 'Gift cards', 'sku': 'SFV-GIFT50', 'stock': 100,
    'short': 'Spend online or in the shop. Valid for two years.', 'description': para('Emailed within an hour, or posted in a card with a handwritten note if you ask at checkout.')}],
}
os.makedirs('demos/thrift', exist_ok=True)
json.dump(demo, open('demos/thrift/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
