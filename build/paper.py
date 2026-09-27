# paper: stationery and paper goods (idea 067), owner's brief "as researched".
# Direction: a Tokyo stationery-shop catalogue. White fields ruled with a 5mm cyan graph grid, objects photographed small
#   in the middle of large pale fields, Mincho product names and hairline spec tables with paper weight and ruling in millimetres.
# Why: stationery buyers choose by ruling, gsm and size; the page itself is drawn on the paper they are buying.
# Fonts: Zen Old Mincho 500/700/900 (display, registry) + Zen Kaku Gothic New 400/500/700 (body). Two families, tabular figures for specs.
# Palette: white #FFFFFF / graphite #222222 / graph cyan #1A7A98 / pale field #F4F7F8 / cyan hairline #BFD3DA.
# Layout idea: a spacing scale in millimetres and a ruling selector (dot grid, ruled, blank) that swaps the page photo with plain links, no script.
import sys, json, os, re, unicodedata
sys.path.insert(0, 'tools/lib')
from blocks import *
import blocks as _b
set_theme('paper')
D = THEME['dir']


def image(filename, alt, caption='', lightbox=True, href=None, **attrs):
    out = _b.image(filename, alt, caption, lightbox, href, **attrs)
    if attrs.get('aspectRatio'):
        st = 'aspect-ratio:%s;object-fit:%s' % (attrs['aspectRatio'], attrs.get('scale', 'cover'))
        out = out.replace('" alt="%s"/>' % alt, '" alt="%s" style="%s"/>' % (alt, st), 1)
    if attrs.get('anchor'):
        out = out.replace('<figure class="', '<figure id="%s" class="' % attrs['anchor'], 1)
    return out


def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))


def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9 _-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')


fonts = json.load(open(os.path.join(D, '.fonts.json')))
fam = {f['slug']: f for f in fonts['fontFamilies']}
fam['display']['fontFamily'] = '"Zen Old Mincho", "Hiragino Mincho ProN", serif'  # the fetch tool labels it sans-serif
pal = lambda rows: [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]
V = lambda k, v: 'var:preset|%s|%s' % (k, v)
C = lambda s: V('color', s)
FS = lambda s: V('font-size', s)
SP = lambda s: V('spacing', s)

PALETTE = [('base', '#FFFFFF', 'Paper white'), ('contrast', '#222222', 'Graphite'), ('accent', '#1A7A98', 'Graph cyan'),
           ('surface', '#F4F7F8', 'Pale field'), ('line', '#BFD3DA', 'Cyan hairline'), ('muted', '#56646A', 'Pencil grey'), ('accent-2', '#C0392B', 'Correction red')]
GRID = ('background-image:linear-gradient(var(--wp--preset--color--line) 1px,transparent 1px),linear-gradient(90deg,var(--wp--preset--color--line) 1px,transparent 1px);'
        'background-size:5mm 5mm;background-position:-1px -1px')

theme = {
 '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
 'settings': {
  'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
  'layout': {'contentSize': '660px', 'wideSize': '1240px'},
  'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE)},
  'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': True,
   'fontFamilies': [{**fam['display'], 'slug': 'display'}, {**fam['body'], 'slug': 'body'}],
   'fontSizes': [
     {'slug': 'x-small', 'size': '0.8125rem', 'name': 'Spec', 'fluid': False},
     {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
     {'slug': 'medium', 'size': '1.0625rem', 'name': 'Body', 'fluid': False},
     {'slug': 'large', 'size': '1.375rem', 'name': 'Product name', 'fluid': {'min': '1.1875rem', 'max': '1.375rem'}},
     {'slug': 'x-large', 'size': '2rem', 'name': 'Section', 'fluid': {'min': '1.5rem', 'max': '2rem'}},
     {'slug': 'xx-large', 'size': '3.25rem', 'name': 'Title', 'fluid': {'min': '2.25rem', 'max': '3.25rem'}},
     {'slug': 'display', 'size': '4.75rem', 'name': 'Display', 'fluid': {'min': '2.75rem', 'max': '4.75rem'}}]},
  'spacing': {'defaultSpacingSizes': False, 'units': ['mm', 'px', 'rem', '%', 'vw'], 'spacingSizes': [
     {'slug': '10', 'size': '1.25mm', 'name': '1.25mm'}, {'slug': '20', 'size': '2.5mm', 'name': '2.5mm'},
     {'slug': '30', 'size': '5mm', 'name': '5mm'}, {'slug': '40', 'size': 'clamp(5mm, 2vw, 7.5mm)', 'name': '5 to 7.5mm'},
     {'slug': '50', 'size': 'clamp(7.5mm, 3vw, 10mm)', 'name': '7.5 to 10mm'}, {'slug': '60', 'size': 'clamp(10mm, 5vw, 20mm)', 'name': '10 to 20mm'},
     {'slug': '70', 'size': 'clamp(15mm, 7vw, 30mm)', 'name': '15 to 30mm'}, {'slug': '80', 'size': 'clamp(20mm, 10vw, 40mm)', 'name': '20 to 40mm'}]},
  'shadow': {'defaultPresets': False, 'presets': []},
  'border': {'color': True, 'radius': True, 'style': True, 'width': True,
             'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}, {'slug': 'corner', 'size': '2mm', 'name': 'Rounded corner'}]},
 },
 'styles': {
  'color': {'background': C('base'), 'text': C('contrast')},
  'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('medium'), 'lineHeight': '1.75', 'fontWeight': '400'},
  'spacing': {'padding': {'left': SP('40'), 'right': SP('40')}, 'blockGap': SP('30')},
  'elements': {
   'link': {'color': {'text': C('accent')}, 'typography': {'textDecoration': 'underline'},
            ':hover': {'color': {'text': C('contrast')}},
            ':focus': {'outline': {'color': C('accent'), 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
   'heading': {'typography': {'fontFamily': V('font-family', 'display'), 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0.02em'}},
   'h1': {'typography': {'fontSize': FS('xx-large'), 'lineHeight': '1.2'}},
   'h2': {'typography': {'fontSize': FS('x-large')}},
   'h3': {'typography': {'fontSize': FS('large')}},
   'h4': {'typography': {'fontSize': FS('medium')}},
   'h5': {'typography': {'fontSize': FS('small'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '700'}},
   'h6': {'typography': {'fontSize': FS('x-small'), 'fontFamily': V('font-family', 'body'), 'fontWeight': '700'}},
   'button': {'color': {'background': C('base'), 'text': C('contrast')},
              'border': {'radius': '2mm', 'width': '1px', 'style': 'solid', 'color': C('contrast')},
              'typography': {'fontFamily': V('font-family', 'body'), 'fontWeight': '500', 'fontSize': FS('small')},
              'spacing': {'padding': {'top': '2.5mm', 'bottom': '2.5mm', 'left': '6mm', 'right': '6mm'}},
              ':hover': {'color': {'background': C('contrast'), 'text': C('base')}},
              ':focus': {'outline': {'color': C('accent'), 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
   'caption': {'typography': {'fontSize': FS('x-small')}, 'color': {'text': C('muted')}},
  },
  'blocks': {
   'core/site-title': {'typography': {'fontFamily': V('font-family', 'display'), 'fontWeight': '900', 'fontSize': FS('x-large'), 'letterSpacing': '0.08em'},
                       'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}}}},
   'core/site-tagline': {'typography': {'fontSize': FS('x-small')}, 'color': {'text': C('muted')}},
   'core/navigation': {'typography': {'fontSize': FS('small'), 'fontWeight': '500'},
                       'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}, 'color': {'text': C('accent')}}}}},
   'core/post-title': {'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}}}},
   'core/post-date': {'typography': {'fontSize': FS('x-small')}, 'color': {'text': C('muted')}},
   'core/post-terms': {'typography': {'fontSize': FS('x-small')}},
   'core/image': {'border': {'radius': '0'}},
   'core/separator': {'color': {'text': C('line')}, 'border': {'width': '1px 0 0 0'}},
   'core/quote': {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('large'), 'lineHeight': '1.6'},
                  'border': {'left': {'color': C('accent'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'left': SP('40')}},
                  'elements': {'cite': {'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('x-small'), 'fontStyle': 'normal'}}}},
   'core/pullquote': {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('x-large')}, 'border': {'top': {'color': C('accent'), 'width': '1px', 'style': 'solid'}, 'bottom': {'color': C('accent'), 'width': '1px', 'style': 'solid'}}},
   'core/table': {'typography': {'fontSize': FS('small')}},
   'core/details': {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}}},
   'core/query-pagination': {'typography': {'fontSize': FS('small')}},
   'core/search': {'border': {'radius': '2mm'}, 'typography': {'fontSize': FS('small')}},
   'core/categories': {'typography': {'fontSize': FS('small')}},
   'core/comments': {'typography': {'fontSize': FS('small')}},
   'core/query-title': {'typography': {'fontSize': FS('xx-large')}},
   'core/list': {'spacing': {'padding': {'left': SP('40')}}},
  },
  'css': (
   ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none;font-feature-settings:"palt"}'
   '.wp-block-heading a,.wp-block-post-title a{color:inherit;text-decoration:none}.wp-block-heading a:hover{color:var(--wp--preset--color--accent)}'
   'table,.is-style-spec,.wc-block-components-product-price{font-variant-numeric:tabular-nums}'
   ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:2px}'
   '.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:2.5mm 5mm 2.5mm 0;text-align:left;vertical-align:top}'
   '.wp-block-table thead{border-bottom:1px solid var(--wp--preset--color--accent)}.wp-block-table th{font-weight:500;color:var(--wp--preset--color--muted)}'
   '.wp-block-search__input{border:1px solid var(--wp--preset--color--line);border-radius:2mm}'
   '.wp-block-navigation__responsive-container.is-menu-open{' + GRID + '}'
   # ruling selector: first photo shows until a ruling link is chosen, then :target shows that one
   '.is-style-ruling-preview > .wp-block-image{display:none;margin:0}.is-style-ruling-preview > .wp-block-image:first-child{display:block}'
   '.is-style-ruling-preview:has(> :target) > .wp-block-image{display:none}.is-style-ruling-preview > .wp-block-image:target{display:block}'
   '@media (prefers-reduced-motion:no-preference){.is-style-ruling-preview > .wp-block-image:target{animation:paperfade .15s ease-out}}@keyframes paperfade{from{opacity:.4}}'
   # objects small on large fields
   '.is-style-field .wp-block-image{background:var(--wp--preset--color--surface);aspect-ratio:1;display:flex;align-items:center;justify-content:center;margin:0}'
   '.is-style-field .wp-block-image img{width:64%;aspect-ratio:1;object-fit:cover}'
   # WooCommerce
   '.wc-block-product-template{gap:10mm 5mm!important}'
   '.wc-block-product-template .wc-block-components-product-image{background:var(--wp--preset--color--surface);aspect-ratio:1;display:flex!important;align-items:center;justify-content:center}'
   '.wc-block-product-template .wc-block-components-product-image a,.wc-block-product-template .wc-block-components-product-image img{width:64%!important;aspect-ratio:1;object-fit:cover}'
   '.wc-block-product-template .wp-block-post-title{font-family:var(--wp--preset--font-family--display);font-weight:700;text-align:left!important;font-size:var(--wp--preset--font-size--medium)!important}'
   '.wc-block-product-template .wc-block-components-product-price{text-align:left!important;font-size:var(--wp--preset--font-size--small)}'
   '.wc-block-components-product-sale-badge{border-radius:2mm;border-color:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--accent-2)}'
   '.woocommerce div.product form.cart .button,.wc-block-components-button:not(.is-link){border-radius:2mm;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'
   '.wc-block-components-text-input input,.wc-block-components-select select,.woocommerce .quantity .qty{border-radius:2mm!important;border-color:var(--wp--preset--color--line)!important}'
   '.woocommerce-tabs .tabs{display:none}'
  ),
 },
 'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                   {'area': 'uncategorized', 'name': 'notice', 'title': 'Seasonal diaries bar'}],
 'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Paper
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A catalogue shop theme for independent stationery shops and notebook makers who sell by ruling, paper weight and size.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: paper
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')


def variation(fname, title, rows, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)


variation('kraft', 'Kraft', [('base', '#D8C3A0', 'Kraft'), ('contrast', '#1A1A1A', 'Black label'), ('accent', '#1A1A1A', 'Black'),
    ('surface', '#E6D6BA', 'Light kraft'), ('line', '#9C8663', 'Kraft fold'), ('muted', '#4A3F30', 'Brown pencil'), ('accent-2', '#8E2A1E', 'Stamp red')])
variation('letterpress', 'Letterpress', [('base', '#FAF6EE', 'Warm white'), ('contrast', '#2A1F1A', 'Press black'), ('accent', '#9B1B30', 'Impression red'),
    ('surface', '#F1EADC', 'Cotton card'), ('line', '#D8C8B0', 'Deckle'), ('muted', '#62544A', 'Faded ink'), ('accent-2', '#9B1B30', 'Impression red')],
    {'blocks': {'core/site-title': {'color': {'text': C('accent')}, 'elements': {'link': {'color': {'text': C('accent')}}}}}})
variation('dot-grid', 'Dot grid', [('base', '#F2F3F3', 'Pale grey'), ('contrast', '#1F2426', 'Graphite'), ('accent', '#0F6F8A', 'Cyan dot'),
    ('surface', '#FFFFFF', 'White field'), ('line', '#9ED0DE', 'Cyan dots'), ('muted', '#4E5A5F', 'Pencil grey'), ('accent-2', '#C0392B', 'Correction red')])


def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})


section('graph', 'Graph paper (5mm)', ['core/group', 'core/columns', 'core/cover'],
        {'color': {'background': C('base')}, 'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60'), 'left': SP('40'), 'right': SP('40')}},
         'css': '&{' + GRID + '}'})
section('dots', 'Dot grid (5mm)', ['core/group', 'core/columns'],
        {'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60'), 'left': SP('40'), 'right': SP('40')}},
         'css': '&{background-image:radial-gradient(circle,var(--wp--preset--color--accent) .5px,transparent .9px);background-size:5mm 5mm}'})
section('field', 'Object on a field', ['core/group'], {'spacing': {'blockGap': SP('20')}})
section('ruling-preview', 'Ruling preview', ['core/group'], {'spacing': {'blockGap': '0'}})
section('spec', 'Spec table', ['core/table', 'core/paragraph', 'core/list'],
        {'typography': {'fontSize': FS('x-small')}, 'color': {'text': C('contrast')},
         'css': '& td:first-child{color:var(--wp--preset--color--muted);width:40%}& table{border-top:1px solid var(--wp--preset--color--accent)}'})
section('pale', 'Pale field', ['core/group', 'core/columns'],
        {'color': {'background': C('surface')}, 'spacing': {'padding': {'top': SP('50'), 'bottom': SP('50'), 'left': SP('40'), 'right': SP('40')}}})
section('hairline', 'Cyan hairline above', ['core/group', 'core/columns'],
        {'border': {'top': {'color': C('accent'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': SP('30')}}})
section('margin-rule', 'Notebook margin rule', ['core/group'],
        {'border': {'left': {'color': C('accent-2'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'left': SP('50')}}})
section('seasonal', 'Seasonal bar', ['core/group'],
        {'color': {'background': C('accent'), 'text': C('base')}, 'typography': {'fontSize': FS('small')},
         'elements': {'link': {'color': {'text': C('base')}}}, 'spacing': {'padding': {'top': SP('20'), 'bottom': SP('20')}}})
section('index-list', 'Category index list', ['core/list'],
        {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('large'), 'fontWeight': '500'},
         'css': '&{list-style:none;padding:0!important;columns:2 14rem;column-gap:10mm}& li{border-bottom:1px solid var(--wp--preset--color--line);padding:2.5mm 0;break-inside:avoid;display:flex;justify-content:space-between;gap:5mm}& li a{text-decoration:none;color:inherit}& li a:hover{color:var(--wp--preset--color--accent)}'})
section('vertical', 'Vertical label', ['core/paragraph'],
        {'typography': {'fontFamily': V('font-family', 'display'), 'fontSize': FS('large'), 'letterSpacing': '0.3em', 'writingMode': 'vertical-rl'}})

# ---------------------------------------------------------------- content
SHOP = {'name': 'Margin', 'addr': '14 Bruntsfield Place, Edinburgh EH10 4HN', 'email': 'shop@example.com', 'phone': '0131 496 0281'}

# name, image, category, price, stock, specs (list of pairs), short, desc, alt
P = [
 ('A5 notebook, dot grid 5mm', 'dot-grid.jpg', 'Notebooks', '16', 30,
  [('Size', '148 × 210 mm'), ('Ruling', 'Dot grid, 5mm'), ('Paper', '100gsm cream, acid-free'), ('Pages', '192 (96 sheets)'), ('Binding', 'Thread-sewn, lies flat'), ('Fountain pen friendly', 'Yes, no bleed with a medium nib')],
  'Dot grid 5mm, 100gsm cream, 192 pages. Fountain pen friendly.', 'Our own A5 notebook, sewn in Leith in batches of 200. The dots are pale enough to disappear under ink and firm enough to rule against.',
  'Open dot grid notebook with a handwritten shopping list in pen and highlighter'),
 ('A5 notebook, ruled 7mm', 'ruled-page.jpg', 'Notebooks', '16', 24,
  [('Size', '148 × 210 mm'), ('Ruling', 'Ruled, 7mm'), ('Paper', '100gsm cream, acid-free'), ('Pages', '192 (96 sheets)'), ('Binding', 'Thread-sewn, lies flat'), ('Fountain pen friendly', 'Yes')],
  'Ruled 7mm, 100gsm cream, 192 pages. Fountain pen friendly.', 'The same notebook with 7mm lines, which suits most handwriting at a normal pace. If you write small, the dot grid is kinder.',
  'Ruled notebook page with pencil shavings and a yellow pencil'),
 ('Pocket notebook, blank, tan leather', 'pocket-notebook.jpg', 'Notebooks', '28', 8,
  [('Size', '90 × 140 mm'), ('Ruling', 'Blank'), ('Paper', '80gsm white'), ('Pages', '128'), ('Cover', 'Vegetable-tanned leather, refillable'), ('Fountain pen friendly', 'Fine nibs only')],
  'Blank, 90 × 140 mm, refillable leather cover.', 'A leather cover that takes our pocket refills. The leather darkens where your hand holds it. Each cover is cut by hand, so the grain and edges vary.',
  'Tan leather pocket notebook with a binder clip and a silver pen on white'),
 ('Graph exercise books, pack of 2', 'graph-books.jpg', 'Notebooks', '7', 40,
  [('Size', '170 × 205 mm'), ('Ruling', 'Squared, 5mm'), ('Paper', '60gsm white'), ('Pages', '24 each'), ('Binding', 'Two staples'), ('Fountain pen friendly', 'No, it will feather')],
  'Squared 5mm school exercise books, two covers.', 'Thin school exercise books with a printed times table on the back. Cheap, good for pencil, and bad for fountain pens. We sell them anyway because people keep asking.',
  'Two school exercise books, green and red, on squared paper with a ruler'),
 ('A5 notebook, black cloth, blank', 'black-notebook.jpg', 'Notebooks', '22', 12,
  [('Size', '148 × 210 mm'), ('Ruling', 'Blank'), ('Paper', '120gsm white, acid-free'), ('Pages', '160'), ('Binding', 'Case-bound, cloth cover'), ('Fountain pen friendly', 'Yes')],
  'Blank, 120gsm, cloth-bound.', 'Heavier paper for drawing and wet ink. The cloth cover scuffs slowly and looks better for it.',
  'Black cloth-bound notebook with a pen lying on the cover'),
 ('Brass dip pen with a medium nib', 'nib-brass.jpg', 'Pens and ink', '14', 15,
  [('Holder', 'Brass'), ('Nib', 'Medium steel, spare included'), ('Length', '165 mm')],
  'Brass holder, medium steel nib and a spare.', 'A plain brass holder that warms up in the hand. Dip it, write four or five words, dip again.', 'Close-up of a brass dip pen nib on cream paper'),
 ('Steel fountain pen, fine nib', 'nib-steel.jpg', 'Pens and ink', '38', 9,
  [('Nib', 'Fine, steel'), ('Filling', 'Cartridge or converter, both included'), ('Weight', '21 g')],
  'Fine steel nib, cartridge or converter.', 'The pen we write every till receipt with. Smooth enough for long letters, cheap enough to lose.', 'Macro photo of a steel fountain pen nib against a dark background'),
 ('Blue-black gall ink, 50ml', 'ink.jpg', 'Pens and ink', '12', 20,
  [('Volume', '50 ml'), ('Colour', 'Writes blue, dries darker'), ('Use', 'Dip and fountain pens, flush pens monthly')],
  'Writes blue, dries blue-black. 50ml.', 'Iron gall ink that goes on blue and darkens on the page over a day. Waterproof once dry. Flush your pen once a month.', 'Square glass bottle of blue-black writing ink with a blue label'),
 ('Coloured pencils, tin of 12', 'pencils.jpg', 'Pencils and erasers', '18', 14,
  [('Count', '12'), ('Core', '3.8 mm, soft'), ('Barrel', 'Round cedar')],
  'Twelve soft cedar pencils in a tin.', 'Soft cores that layer well on smooth paper. The tin keeps the points intact in a bag.', 'A fan of rainbow coloured pencils with water droplets'),
 ('Two-hole pencil sharpener, pink', 'sharpener.jpg', 'Pencils and erasers', '4.50', 30,
  [('Holes', 'Standard and jumbo'), ('Body', 'Plastic, with shavings pot')],
  'Two holes, catches its shavings.', 'Sharpens standard and jumbo pencils, keeps the shavings off your desk.', 'Pink two-hole pencil sharpener held between finger and thumb'),
 ('Pencil-top eraser', 'eraser.jpg', 'Pencils and erasers', '3', 60,
  [('Fits', 'Standard round and hex pencils'), ('Rubber', 'Grey, latex-free')],
  'Grey latex-free eraser that fits on a pencil.', 'Clean erasing on graphite without tearing thin paper.', 'Grey eraser in a pink plastic sleeve'),
 ('Laid envelopes, C6, pack of 20', 'envelopes.jpg', 'Mail', '6', 45,
  [('Size', 'C6, 114 × 162 mm'), ('Paper', '100gsm white laid'), ('Seal', 'Gummed, lick to close')],
  'C6, 100gsm laid, gummed.', 'Fits an A6 card or an A4 sheet folded twice. The laid texture takes fountain pen without feathering.', 'White envelopes tied with grey ribbon, a pencil and eucalyptus leaves on white'),
 ('2026 diary, A5, week to view', 'journal-pen.jpg', 'Diaries', '24', 50,
  [('Size', '148 × 210 mm'), ('Layout', 'Week on the left, ruled 6mm notes on the right'), ('Dates', '29 December 2025 to 3 January 2027'), ('Paper', '80gsm cream'), ('Fountain pen friendly', 'Yes')],
  'Week to view, starts 29 December 2025.', 'Printed in Glasgow with UK bank holidays and moon phases. A ribbon, a back pocket, and nothing else.', 'Open journal with handwriting and a fountain pen resting on the page'),
]


def purl(p):
    return '/product/%s/' % slugify(p[0])


def spec(p, cls='is-style-spec'):
    return table([[k, v] for k, v in p[5]], className=cls)


ALT = {p[1]: p[8] for p in P}
ALT.update({'desk-clips.jpg': 'Paper clips, a black mug, a pencil and an eraser on a white desk', 'stamped-book.jpg': 'An old passbook with pages of rubber stamps in blue and violet',
            'ruled-macro.jpg': 'Macro photo of blue horizontal lines on notebook paper', 'sketchbook.jpg': 'An old notebook page with handwriting and pen drawings of vases',
            'stamps.jpg': 'A stockbook page of 1960s British postage stamps', 'shop.jpg': 'A busy stationery shop with shelves of pens and notebooks'})

# ---------------------------------------------------------------- patterns
pattern('hero-graph', 'Hero on graph paper', 'featured,banner', group(columns(
  ('55%', J(heading('Notebooks, pens and paper, tested with a wet nib before we stock them.', 1),
     para('A small shop on Bruntsfield Place, since 2014. Every paper on these shelves has been written on with a wet fountain pen by one of us, and the spec on the label says honestly what happened to the ink. Some feather.'),
     buttons(('See the notebooks', '/product-category/notebooks/'), ('Download ruling samples', '/ruling-samples/', {'className': 'is-style-outline'})))),
  (None, group(image('desk-clips.jpg', ALT['desk-clips.jpg'], aspectRatio='1', scale='cover'), className='is-style-field', layout={'type': 'default'})), align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': SP('80')}}}),
  align='full', className='is-style-graph', layout={'type': 'constrained'}),
  description='The home hero, set on a 5mm graph-paper field.')


def field_tile(p):
    return group(J(
        group(image(p[1], ALT[p[1]], href=purl(p), aspectRatio='1', scale='cover'), className='is-style-field', layout={'type': 'default'}),
        heading('<a href="%s">%s</a>' % (purl(p), p[0]), 3, fontSize='medium'),
        para('%s, %s' % (p[5][0][1], p[5][1][1].lower() if len(p[5]) > 1 else ''), className='is-style-spec', textColor='muted'),
        para('£%s' % p[3], fontSize='small')), layout={'type': 'default'}, style={'spacing': {'blockGap': SP('20')}})


def grid_of(idx, title, link):
    return group(J(
      row(J(heading(title, 2), para('<a href="%s">%s</a>' % link, fontSize='small')), justify='space-between', align='wide', className='is-style-hairline'),
      group(J(*[field_tile(P[i]) for i in idx]), align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '10rem'},
            style={'spacing': {'blockGap': SP('50')}})), align='wide', layout={'type': 'default'})


pattern('new-arrivals', 'New arrivals (objects on fields)', 'shop,featured', grid_of([0, 7, 2, 11, 5, 8, 12, 3], 'New arrivals', ('/new-arrivals/', 'All new arrivals')),
  description='Products photographed small in the middle of a pale square, 4 across.')
pattern('pens-grid', 'Pens and ink (4 tiles)', 'shop', grid_of([6, 5, 7, 9], 'Pens and ink', ('/product-category/pens-and-ink/', 'All pens and ink')))

CATS = [('Notebooks', 'notebooks', 42), ('Pens and ink', 'pens-and-ink', 31), ('Pencils and erasers', 'pencils-and-erasers', 26),
        ('Mail', 'mail', 18), ('Diaries', 'diaries', 9), ('Clips and pins', 'notebooks', 14), ('Perpetual calendars', 'diaries', 4), ('Gift wrap', 'mail', 7)]
pattern('category-index', 'Category index (two columns)', 'shop,featured', group(J(
  heading('The shelves', 2),
  lst(['<a href="/product-category/%s/">%s</a><span>%d</span>' % (s, n, c) for n, s, c in CATS], className='is-style-index-list')),
  align='wide', layout={'type': 'default'}), description='A plain two-column list of categories with the number of things on each shelf.')

RULINGS = [('ruling-dot', 'Dot grid 5mm', 'dot-grid.jpg'), ('ruling-ruled', 'Ruled 7mm', 'ruled-page.jpg'), ('ruling-squared', 'Squared 5mm', 'graph-books.jpg'), ('ruling-blank', 'Blank', 'sketchbook.jpg')]
pattern('ruling-selector', 'Notebook with ruling selector', 'shop,featured', columns(
  ('44%', group(J(*[image(f, ALT.get(f, n), caption=n, lightbox=False, anchor=a, aspectRatio='1', scale='cover') for a, n, f in RULINGS]),
               className='is-style-ruling-preview', layout={'type': 'default'})),
  (None, J(heading('A5 notebook, in four rulings', 2),
     para('Choose a ruling to see the page.', fontSize='small', textColor='muted'),
     row(J(*[para('<a href="#%s">%s</a>' % (a, n)) for a, n, f in RULINGS]), style={'spacing': {'blockGap': SP('40')}}, className='is-style-hairline'),
     table([['Dot grid', '5mm pitch, 0.3mm dots, pale grey'], ['Ruled', '7mm lines, no margin'], ['Squared', '5mm squares'], ['Blank', 'Nothing printed']], head=['Ruling', 'Spacing'], className='is-style-spec'),
     table([['Size', '148 × 210 mm'], ['Paper', '100gsm cream, acid-free'], ['Pages', '192'], ['Fountain pen friendly', 'Yes, no bleed with a medium nib']], className='is-style-spec'),
     para('Each notebook is sewn by hand in Leith, so the thread colour and the squareness of the corners vary a little from one to the next.', fontSize='small'),
     buttons(('Buy the dot grid', purl(P[0])), ('Buy the ruled', purl(P[1]), {'className': 'is-style-outline'})))),
  align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}),
  description='The signature: links for each ruling swap the photo of the page, with spacing in millimetres and paper weight beside it.')

pattern('paper-spec', 'Paper spec line', 'shop', para('148 × 210 mm, 100gsm cream, acid-free, 192 pages, dot grid 5mm. Fountain pen friendly: yes.', className='is-style-spec'))
pattern('fountain-pen-friendly', 'Fountain pen friendly: yes or no', 'shop', table([
  ['A5 notebooks', 'Yes', 'No bleed, slight show-through with broad nibs'], ['Pocket refills', 'Fine nibs', 'Feathers with a broad nib'],
  ['Exercise books', 'No', 'Pencil and ballpoint only'], ['Laid envelopes', 'Yes', 'Let it dry before posting']], head=['Paper', 'Fountain pen friendly', 'What we saw'], className='is-style-spec'),
  description='Every paper product with a plain yes or no, and what happened when we tested it.')
pattern('handmade-note', 'Handmade variation note', 'shop', group(para('Each notebook is sewn by hand, so the thread colour and the squareness of the corners vary a little. We think that is part of it.', fontSize='small'),
  className='is-style-margin-rule', layout={'type': 'default'}))

pattern('ruling-samples', 'Printable ruling samples', 'shop,text', group(J(
  heading('Test the paper with your own pen', 2),
  para('Print these A5 sheets on plain paper to try the ruling at home. To test our actual paper, ask for a sample pack in the shop or add a free one to any order.'),
  lst(['<a href="/ruling-samples/#dot">Dot grid 5mm (A5)</a>', '<a href="/ruling-samples/#ruled">Ruled 7mm (A5)</a>', '<a href="/ruling-samples/#squared">Squared 5mm (A5)</a>'], className='is-style-spec')),
  className='is-style-dots', align='wide', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('diaries-notice', 'Notice: next year\'s diaries are in', 'banner', group(
  para('Next year\'s diaries are in. Week to view and day to a page, all starting 29 December. <a href="/diaries/">See the diaries</a>. Take this bar down in February.'),
  className='is-style-seasonal', align='full', layout={'type': 'constrained'}), description='Switch on in September, off in February.')

pattern('diaries-page-intro', 'Dated diaries (seasonal)', 'shop', columns(
  (None, image('journal-pen.jpg', ALT['journal-pen.jpg'], aspectRatio='4/3', scale='cover')),
  (None, J(heading('2026 diaries', 2),
     para('Three layouts, all A5, all starting on Monday 29 December 2025. Printed in Glasgow on 80gsm cream that takes a fountain pen.'),
     table([['Week to view', 'Week left, notes right', '£24'], ['Day to a page', 'One page a day, Sundays shared', '£28'], ['Month to view', 'Twelve spreads and 60 blank pages', '£18']], head=['Layout', 'Page', 'Price'], className='is-style-spec'),
     para('Once they sell out we do not reprint. Last year the day-to-a-page went by early November.', fontSize='small'))), align='wide'))

pattern('perpetual-calendar', 'Perpetual calendar', 'shop', group(J(
  heading('Perpetual calendar', 3),
  para('A wooden block calendar with tiles for day, date and month. Change the tiles each morning; it works for any year.'),
  para('£32, beech, 130 × 90 mm', className='is-style-spec')), className='is-style-pale', layout={'type': 'default'}))

pattern('gift-wrap', 'Gift wrapping', 'shop', para('We wrap in plain kraft with a paper band and a handwritten tag for £2. Say who it is for in the order note and we will write it on the tag.'))

pattern('visit', 'Shop visit and hours', 'contact', columns(
  ('55%', image('shop.jpg', ALT['shop.jpg'], aspectRatio='3/2', scale='cover', caption='Stand-in photo. Our shop is smaller and quieter than this.')),
  (None, J(heading('Visit', 2),
     para('%s. Between the bakery and the bike shop, opposite the Links. The 11, 15 and 16 buses stop outside.' % SHOP['addr']),
     table([['Monday', 'Closed'], ['Tuesday to Friday', '10am to 5.30pm'], ['Saturday', '10am to 5pm'], ['Sunday', '12pm to 4pm']], className='is-style-spec'),
     para('There is a testing desk by the window with every pen and ink we sell. Please try them. We ask you not to test on the notebooks themselves.', fontSize='small'),
     para('<a href="tel:01314960281">%s</a>, <a href="mailto:%s">%s</a>' % (SHOP['phone'], SHOP['email'], SHOP['email']), fontSize='small'))), align='wide', style={'spacing': {'blockGap': {'left': SP('60')}}}))

pattern('wholesale', 'Wholesale terms and price list', 'shop,text', J(
  heading('Wholesale', 2),
  para('Our own notebooks are available to other independent shops. We do not sell wholesale to online marketplaces.'),
  table([['A5 notebook, any ruling', '£8.00', '£16'], ['Pocket refill, 3 pack', '£5.50', '£11'], ['2026 diary, week to view', '£12.00', '£24']], head=['Product', 'Trade', 'Retail'], className='is-style-spec'),
  para('Minimum first order £150, then £80. Net 30 days after the first order. Email <a href="mailto:%s?subject=Wholesale">%s</a> with your shop name and address for the full price list.' % (SHOP['email'], SHOP['email']))))

pattern('about', 'About the shop', 'about', columns(
  (None, J(heading('About Margin', 2),
     para('Mei Takahashi opened Margin in 2014 after ten years buying for a department store stationery floor. Callum Reid joined in 2018 and started sewing our own notebooks in a back room in Leith.'),
     para('We stock things we use. If a paper feathers under a fountain pen, we either say so on the label or we do not sell it. We would rather have forty good notebooks than four hundred.'),
     para('We do not do personalised printing, and we do not offer next-day delivery.'))),
  ('40%', image('stamped-book.jpg', ALT['stamped-book.jpg'], aspectRatio='4/5', scale='cover')), align='wide'))

pattern('shipping', 'Shipping and returns', 'shop', J(
  heading('Postage', 2),
  table([['UK, letter size (pens, ink, envelopes)', '£2.40'], ['UK, parcel', '£4.20'], ['UK, orders over £45', 'Included'], ['Europe', '£11'], ['Rest of the world', '£16']], className='is-style-spec'),
  para('Orders go out Tuesday to Saturday, wrapped in paper and sealed with paper tape. Ink goes in a sealed bag, just in case.'),
  heading('Returns', 2),
  para('Unused items within 30 days, refunded in full. Opened ink and written-in notebooks cannot come back, so ask us about the paper before you buy.')))

pattern('quote', 'A customer note', 'testimonials', quote('Asked which notebook would take my broad italic nib and Mei tested three in front of me. Bought the black cloth one.', 'Ruaridh, Marchmont, August 2025'))

pattern('notes-list', 'Notes from the shop (latest posts)', 'posts,query', group(J(
  row(J(heading('Notes from the shop', 2), para('<a href="/notes/">All notes</a>', fontSize='small')), justify='space-between', align='wide', className='is-style-hairline'),
  query(J(dyn('post-date'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=16, fontSize='small')),
        per_page=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'}, align='wide')), align='wide', layout={'type': 'default'}))

pattern('post-grid', 'Notes grid (inherits query)', 'posts,query', inherit_query(
  J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover'), dyn('post-date'), dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', excerptLength=20, fontSize='small')),
  layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '15rem'}, align='wide'), inserter=False)
pattern('post-list', 'Results list', 'posts,query', inherit_query(
  group(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-date')), className='is-style-hairline', layout={'type': 'default'}), align='wide'), inserter=False)

# pages
pattern('page-new-arrivals', 'Page: new arrivals', 'shop', J(para('What came in over the last month, newest first. Paper goods sell out slowly; pens and ink quickly.'), pattern_ref('new-arrivals'), pattern_ref('pens-grid')), block_types='core/post-content')
pattern('page-diaries', 'Page: diaries', 'shop', J(pattern_ref('diaries-page-intro'), pattern_ref('perpetual-calendar'), pattern_ref('gift-wrap')), block_types='core/post-content')
pattern('page-ruling-samples', 'Page: ruling samples', 'shop', J(pattern_ref('ruling-selector'), pattern_ref('ruling-samples'), pattern_ref('fountain-pen-friendly')), block_types='core/post-content')
pattern('page-visit', 'Page: visit', 'contact', J(pattern_ref('visit'), pattern_ref('about'), pattern_ref('quote')), block_types='core/post-content')
pattern('page-wholesale', 'Page: wholesale', 'shop', J(pattern_ref('wholesale'), pattern_ref('shipping')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(J(
  row(J(row(J(dyn('site-title', level=0), dyn('site-tagline')), style={'spacing': {'blockGap': SP('40')}}, wrap=True),
        dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile', style={'spacing': {'blockGap': SP('40')}})),
      justify='space-between', align='wide', wrap=False)),
  tag='header', align='full', layout={'type': 'constrained'},
  style={'spacing': {'padding': {'top': SP('40'), 'bottom': SP('40')}}, 'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}}))
write('parts/notice.html', pattern_ref('diaries-notice'))
write('parts/footer.html', group(J(
  columns(
    ('40%', J(dyn('site-title', level=0), para('Paper, pens and desk things. %s.' % SHOP['addr'], fontSize='small'))),
    (None, J(heading('Hours', 5), para('Tue to Fri 10 to 5.30<br>Sat 10 to 5, Sun 12 to 4<br>Closed Mondays', fontSize='small'))),
    (None, J(heading('Help', 5), para('<a href="/wholesale/">Wholesale and postage</a><br><a href="/ruling-samples/">Ruling samples</a><br><a href="mailto:%s">%s</a>' % (SHOP['email'], SHOP['email']), fontSize='small'))),
    align='wide'),
  para('Demo photographs are CC0 and public domain images from Wikimedia Commons and Unsplash, used as stand-ins for our own product photos.', fontSize='x-small', textColor='muted', align='wide')),
  tag='footer', align='full', className='is-style-graph', layout={'type': 'constrained'}))


# ---------------------------------------------------------------- templates
def main(inner, pad_top='60', **kw):
    return group(inner, tag='main', style={'spacing': {'padding': {'top': SP(pad_top), 'bottom': SP('80')}}}, layout={'type': 'constrained'}, **kw)


def tpl(name, inner):
    write('templates/%s.html' % name, J(template_part('header', 'header'), inner, template_part('footer', 'footer')))


tpl('front-page', group(J(pattern_ref('hero-graph'), pattern_ref('category-index'), pattern_ref('new-arrivals'), pattern_ref('ruling-selector'),
    pattern_ref('diaries-page-intro'), pattern_ref('notes-list'), pattern_ref('visit')), tag='main', layout={'type': 'constrained'},
    style={'spacing': {'blockGap': SP('80'), 'padding': {'bottom': SP('80')}}}))
tpl('page', main(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'}))))
tpl('page-wide', main(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'}))))
tpl('single', main(J(dyn('post-date'), dyn('post-title', level=1), dyn('post-featured-image', aspectRatio='3/2', scale='cover'),
    group(dyn('post-content', layout={'type': 'constrained'}), className='is-style-margin-rule', layout={'type': 'default'}),
    dyn('post-terms', term='category', prefix='Filed under '),
    row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)), justify='space-between', className='is-style-hairline'))))
tpl('home', main(J(heading('Notes from the shop', 1, align='wide'), pattern_ref('post-grid'))))
tpl('index', main(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-grid'))))
tpl('archive', main(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('post-grid'))))
tpl('search', main(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Dot grid, blue-black, A5', buttonText='Search'), pattern_ref('post-list'))))
tpl('404', main(J(heading('This page is blank', 1), para('The link may be old, or the item has left the shelves. Try the <a href="/shop/">shop</a> or search.'),
    dyn('search', label='Search', showLabel=False, placeholder='Dot grid, blue-black, A5', buttonText='Search'))))


def product_collection(per_page=16, cols=4):
    q = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'product', 'order': 'desc', 'orderBy': 'date', 'search': '', 'exclude': [],
         'inherit': True, 'taxQuery': {}, 'isProductCollectionBlock': True, 'woocommerceOnSale': False,
         'woocommerceStockStatus': ['instock', 'outofstock', 'onbackorder'], 'woocommerceAttributes': [], 'woocommerceHandPickedProducts': []}
    a = {'queryId': 0, 'query': q, 'tagName': 'div', 'displayLayout': {'type': 'flex', 'columns': cols, 'shrinkColumns': True},
         'dimensions': {'widthType': 'fill'}, 'queryContextIncludes': ['collection'], 'align': 'wide'}
    tmpl = J(dyn('woocommerce/product-image', showSaleBadge=True, imageSizing='single', isDescendentOfQueryLoop=True, aspectRatio='1', scale='cover'),
             dyn('post-title', level=2, isLink=True, __woocommerceNamespace='woocommerce/product-collection/product-title'),
             dyn('post-excerpt', excerptLength=12, fontSize='x-small', textColor='muted', __woocommerceNamespace='woocommerce/product-collection/product-summary'),
             dyn('woocommerce/product-price', isDescendentOfQueryLoop=True))
    return ('<!-- wp:woocommerce/product-collection %s -->\n<div class="wp-block-woocommerce-product-collection alignwide">'
            '<!-- wp:woocommerce/product-template -->\n%s\n<!-- /wp:woocommerce/product-template -->\n\n'
            '<!-- wp:query-pagination {"layout":{"type":"flex","justifyContent":"center"}} -->\n<!-- wp:query-pagination-previous /-->\n\n<!-- wp:query-pagination-numbers /-->\n\n<!-- wp:query-pagination-next /-->\n<!-- /wp:query-pagination -->\n\n'
            '<!-- wp:woocommerce/product-collection-no-results -->\n%s\n<!-- /wp:woocommerce/product-collection-no-results --></div>\n<!-- /wp:woocommerce/product-collection -->') % (
        json.dumps(a, separators=(',', ':')), tmpl, para('Nothing on this shelf at the moment. Ask in the shop, we may have one in the back.'))


cat_row = row(J(*[para('<a href="/product-category/%s/">%s</a>' % (s, n), fontSize='small') for n, s, c in CATS[:5]]), style={'spacing': {'blockGap': SP('40')}}, align='wide', className='is-style-hairline')
for name in ('archive-product', 'taxonomy-product_cat', 'product-search-results'):
    tpl(name, main(J(dyn('woocommerce/store-notices'), dyn('query-title', type='archive', showPrefix=False, align='wide'), cat_row,
                     dyn('term-description', align='wide'), product_collection()), pad_top='50'))

tpl('single-product', main(J(
  dyn('woocommerce/store-notices'),
  columns(('50%', group(dyn('woocommerce/product-image', showProductLink=False, showSaleBadge=True, imageSizing='single', isDescendentOfSingleProductTemplate=True, aspectRatio='1', scale='cover'),
                        className='is-style-graph', layout={'type': 'default'})),
          (None, J(dyn('post-title', level=1, fontSize='x-large', __woocommerceNamespace='woocommerce/product-query/product-title'),
                   dyn('woocommerce/product-price', isDescendentOfSingleProductTemplate=True, fontSize='large'),
                   dyn('post-excerpt', __woocommerceNamespace='woocommerce/product-query/product-summary', fontSize='small'),
                   dyn('woocommerce/add-to-cart-form'),
                   pattern_ref('handmade-note'),
                   dyn('woocommerce/product-details'))),
          align='wide', style={'spacing': {'blockGap': {'left': SP('70')}}}),
  pattern_ref('gift-wrap')), pad_top='50'))

print('paper built:', len(os.listdir(os.path.join(D, 'patterns'))), 'patterns')


# ---------------------------------------------------------------- demo
def pdesc(p):
    return J(para(p[7]), spec(p))


demo = {
 'site': {'title': 'Margin', 'tagline': 'Paper, pens and desk things, Bruntsfield'},
 'categories': [{'slug': 'paper-tests', 'name': 'Paper tests'}, {'slug': 'shop-notes', 'name': 'Shop notes'}],
 'front_page': 'home', 'posts_page': 'notes',
 'pages': [
  {'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'notes', 'title': 'Notes', 'content': ''},
  {'slug': 'new-arrivals', 'title': 'New arrivals', 'pattern': 'paper/page-new-arrivals', 'template': 'page-wide'},
  {'slug': 'diaries', 'title': 'Diaries', 'pattern': 'paper/page-diaries', 'template': 'page-wide'},
  {'slug': 'ruling-samples', 'title': 'Rulings', 'pattern': 'paper/page-ruling-samples', 'template': 'page-wide'},
  {'slug': 'wholesale', 'title': 'Wholesale', 'pattern': 'paper/page-wholesale'},
  {'slug': 'visit', 'title': 'Visit', 'pattern': 'paper/page-visit', 'template': 'page-wide'},
 ],
 'posts': [
  {'title': 'Nine inks on our 100gsm cream, side by side', 'category': 'paper-tests', 'image': 'ink.jpg', 'content': J(
     para('We wrote the same sentence in nine inks with a medium steel nib and left the page for a day. Two showed through, none bled. The gall ink darkened most.'))},
  {'title': 'Why the dot grid is 5mm and not 4mm', 'category': 'paper-tests', 'image': 'dot-grid.jpg', 'content': J(
     para('At 4mm most people write two dots per line and the page looks crowded. At 5mm it lines up with a relaxed hand and still works for small drawings.'))},
  {'title': 'The 2026 diaries are in', 'category': 'shop-notes', 'image': 'journal-pen.jpg', 'content': J(
     para('Week to view, day to a page and month to view, all starting 29 December. We printed the same number as last year, which ran out in November.'))},
  {'title': 'Sewing a batch of 200 notebooks', 'category': 'shop-notes', 'image': 'black-notebook.jpg', 'content': J(
     para('Callum sews on Mondays when the shop is closed. A batch of 200 takes three Mondays, and the thread colour depends on what the supplier has that month.'))},
  {'title': 'Exercise books and why we still sell them', 'category': 'shop-notes', 'image': 'graph-books.jpg', 'content': J(
     para('They feather under a fountain pen and the paper is thin. They are also £3.50 each and perfect for maths homework, so they stay.'))},
  {'title': 'Testing envelopes in the rain', 'category': 'paper-tests', 'image': 'envelopes.jpg', 'content': J(
     para('We posted ten laid envelopes to ourselves during a wet week. The addresses in gall ink arrived sharp; the ones in a dye ink had run on two.'))},
 ],
 'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'New arrivals', 'url': '/new-arrivals/'}, {'label': 'Rulings', 'url': '/ruling-samples/'},
         {'label': 'Diaries', 'url': '/diaries/'}, {'label': 'Wholesale', 'url': '/wholesale/'}, {'label': 'Notes', 'url': '/notes/'}, {'label': 'Visit', 'url': '/visit/'}],
 'currency': 'GBP',
 'products': [{'name': p[0], 'price': p[3], 'image': p[1], 'category': p[2], 'sku': 'MGN-%d' % (100 + i), 'stock': p[4], 'short': p[6], 'description': pdesc(p)} for i, p in enumerate(P)],
}
os.makedirs('demos/paper', exist_ok=True)
json.dump(demo, open('demos/paper/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
