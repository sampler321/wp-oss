# crate: record shop (idea 061), owner's brief "more Balenciaga-like or Zara-like".
# Direction: fashion-house e-commerce minimalism applied to a used-record shop. White field, black type,
#   one cold grey behind every product photo, so records sit in the grid the way garments do on a luxury PLP.
# Why: the owner wants the stark fashion look; the research's data layer (grade pairs, cat nos, the latest-100 list) survives as tiny uppercase tables.
# Fonts: Arimo only (display claim, replaces Urbanist): one plain neo-grotesque at two extremes, 12px uppercase UI and a 30vw wordmark.
# Palette: #FFFFFF / #000000 / grey #EFEFEF tiles / hairline #000 / red #D70015 kept for SOLD and the Record Store Day bar.
# Layout idea: edge-to-edge 4-up product grid with 2px gutters and no cards, and a single gigantic CRATE wordmark over the hero photo; everything else is small.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('crate')
S = 'crate'
D = THEME['dir']

import blocks as _b
def image(filename, alt, caption='', lightbox=True, href=None, **attrs):
    out = _b.image(filename, alt, caption, lightbox, href, **attrs)
    if attrs.get('aspectRatio'):
        st = 'aspect-ratio:%s;object-fit:%s' % (attrs['aspectRatio'], attrs.get('scale', 'cover'))
        out = out.replace('" alt="%s"/>' % alt, '" alt="%s" style="%s"/>' % (alt, st), 1)
    return out

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

fonts = json.load(open(os.path.join(D, '.fonts.json')))
arimo = fonts['fontFamilies'][0]

# ---------------------------------------------------------------- theme.json
PALETTE = [
    ('base', '#FFFFFF', 'White'), ('contrast', '#000000', 'Black'), ('accent', '#D70015', 'Sold red'),
    ('surface', '#EFEFEF', 'Tile grey'), ('line', '#000000', 'Hairline'), ('muted', '#595959', 'Grey text'),
    ('accent-2', '#FFE600', 'Sticker yellow'),
]
pal = lambda rows: [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]
V = lambda k, v: 'var:preset|%s|%s' % (k, v)
C = lambda s: V('color', s)
FS = lambda s: V('font-size', s)
SP = lambda s: V('spacing', s)

caps = {'textTransform': 'uppercase', 'letterSpacing': '0.06em'}
theme = {
 '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
 'settings': {
  'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
  'layout': {'contentSize': '640px', 'wideSize': '1600px'},
  'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE),
            'duotone': [{'slug': 'mono', 'colors': ['#000000', '#EFEFEF'], 'name': 'Black on grey'}]},
  'typography': {
   'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
   'fontFamilies': [
     {**arimo, 'name': 'Arimo', 'slug': 'display'},
     {'fontFamily': arimo['fontFamily'], 'name': 'Arimo (text)', 'slug': 'body'},
   ],
   'fontSizes': [
     {'slug': 'x-small', 'size': '0.6875rem', 'name': 'Label', 'fluid': False},
     {'slug': 'small', 'size': '0.75rem', 'name': 'Small caps', 'fluid': False},
     {'slug': 'medium', 'size': '0.9375rem', 'name': 'Body', 'fluid': False},
     {'slug': 'large', 'size': '1.25rem', 'name': 'Large', 'fluid': {'min': '1.0625rem', 'max': '1.25rem'}},
     {'slug': 'x-large', 'size': '2.25rem', 'name': 'Title', 'fluid': {'min': '1.5rem', 'max': '2.25rem'}},
     {'slug': 'xx-large', 'size': '5rem', 'name': 'Poster', 'fluid': {'min': '2.75rem', 'max': '5rem'}},
     {'slug': 'display', 'size': 'clamp(5.5rem, 29vw, 30rem)', 'name': 'Wordmark', 'fluid': False},
   ]},
  'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
     {'slug': '10', 'size': '2px', 'name': 'Gutter'},
     {'slug': '20', 'size': '0.5rem', 'name': '2'},
     {'slug': '30', 'size': '1rem', 'name': '3'},
     {'slug': '40', 'size': 'clamp(1rem, 1.6vw, 1.5rem)', 'name': '4'},
     {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'},
     {'slug': '60', 'size': 'clamp(2.5rem, 5vw, 4.5rem)', 'name': '6'},
     {'slug': '70', 'size': 'clamp(4rem, 8vw, 7rem)', 'name': '7'},
     {'slug': '80', 'size': 'clamp(5rem, 12vw, 11rem)', 'name': '8'},
  ]},
  'shadow': {'defaultPresets': False, 'presets': []},
  'border': {'color': True, 'radius': True, 'style': True, 'width': True,
             'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}]},
  'custom': {'measure': '62ch'},
 },
 'styles': {
  'color': {'background': C('base'), 'text': C('contrast')},
  'typography': {'fontFamily': V('font-family', 'body'), 'fontSize': FS('medium'), 'lineHeight': '1.5', 'fontWeight': '400'},
  'spacing': {'padding': {'left': SP('30'), 'right': SP('30')}, 'blockGap': SP('30')},
  'elements': {
   'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'},
            ':hover': {'typography': {'textDecoration': 'underline'}},
            ':focus': {'outline': {'color': C('contrast'), 'offset': '2px', 'style': 'solid', 'width': '1px'}}},
   'heading': {'typography': {'fontFamily': V('font-family', 'display'), 'fontWeight': '700', 'lineHeight': '1.05', 'textTransform': 'uppercase', 'letterSpacing': '0.04em'}},
   'h1': {'typography': {'fontSize': FS('x-large'), 'letterSpacing': '-0.01em', 'lineHeight': '0.95'}},
   'h2': {'typography': {'fontSize': FS('small'), 'letterSpacing': '0.08em'}},
   'h3': {'typography': {'fontSize': FS('small'), 'letterSpacing': '0.08em'}},
   'h4': {'typography': {'fontSize': FS('small')}},
   'h5': {'typography': {'fontSize': FS('x-small')}},
   'h6': {'typography': {'fontSize': FS('x-small'), 'fontWeight': '400'}},
   'button': {'color': {'background': C('contrast'), 'text': C('base')},
              'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': C('contrast')},
              'typography': {'fontFamily': V('font-family', 'body'), 'fontWeight': '700', 'fontSize': FS('small'), **caps},
              'spacing': {'padding': {'top': '1.05em', 'bottom': '1.05em', 'left': '2.6em', 'right': '2.6em'}},
              ':hover': {'color': {'background': C('base'), 'text': C('contrast')}},
              ':focus': {'outline': {'color': C('contrast'), 'offset': '3px', 'style': 'solid', 'width': '1px'}}},
   'caption': {'typography': {'fontSize': FS('x-small'), **caps}, 'color': {'text': C('contrast')}},
  },
  'blocks': {
   'core/site-title': {'typography': {'fontFamily': V('font-family', 'display'), 'fontWeight': '700', 'fontSize': FS('large'), 'textTransform': 'uppercase', 'letterSpacing': '0.32em'},
                       'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}}}},
   'core/navigation': {'typography': {'fontSize': FS('small'), 'fontWeight': '400', **caps},
                       'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
   'core/post-title': {'elements': {'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'none'}}}},
   'core/post-date': {'typography': {'fontSize': FS('x-small'), **caps}, 'color': {'text': C('muted')}},
   'core/post-terms': {'typography': {'fontSize': FS('x-small'), **caps}},
   'core/image': {'border': {'radius': '0'}, 'color': {'background': C('surface')}},
   'core/post-featured-image': {'border': {'radius': '0'}, 'color': {'background': C('surface')}},
   'core/separator': {'color': {'text': C('contrast')}, 'border': {'width': '1px 0 0 0'}},
   'core/quote': {'typography': {'fontSize': FS('large'), 'fontWeight': '400', 'lineHeight': '1.3'},
                  'border': {'left': {'color': C('contrast'), 'width': '1px', 'style': 'solid'}},
                  'spacing': {'padding': {'left': SP('40')}},
                  'elements': {'cite': {'typography': {'fontSize': FS('x-small'), 'fontStyle': 'normal', **caps}}}},
   'core/pullquote': {'typography': {'fontSize': FS('x-large'), 'textTransform': 'uppercase', 'fontWeight': '700', 'lineHeight': '1'},
                      'border': {'width': '0'}},
   'core/table': {'typography': {'fontSize': FS('small'), **caps}},
   'core/details': {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}},
                    'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30')}},
                    'typography': {'fontSize': FS('medium')}},
   'core/list': {'typography': {'fontSize': FS('medium')}},
   'core/query-pagination': {'typography': {'fontSize': FS('small'), **caps}},
   'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': FS('small'), **caps}},
   'core/categories': {'typography': {'fontSize': FS('small'), **caps}},
   'core/comments': {'typography': {'fontSize': FS('small')}},
   'core/post-comments-form': {'typography': {'fontSize': FS('small')}},
   'core/term-description': {'typography': {'fontSize': FS('small')}},
   'core/query-title': {'typography': {'fontSize': FS('x-large')}},
   'woocommerce/product-price': {'typography': {'fontSize': FS('small'), **caps}},
   'woocommerce/breadcrumbs': {'typography': {'fontSize': FS('x-small'), **caps}},
  },
  'css': (
   ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}'
   'table,.wc-block-components-product-price,.is-style-tile{font-variant-numeric:tabular-nums}'
   'body{font-synthesis:none;-webkit-font-smoothing:antialiased}'
   ':focus-visible{outline:1px solid currentColor;outline-offset:3px}'
   '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.55em .8em .55em 0;text-align:left;vertical-align:top}'
   '.wp-block-table thead{border-bottom:0}.wp-block-table th{font-weight:700}'
   '.wp-block-navigation__responsive-container.is-menu-open{padding:var(--wp--preset--spacing--30);font-size:var(--wp--preset--font-size--large)}'
   '.wp-block-search__input{border:0;border-bottom:1px solid currentColor;border-radius:0;padding:.6em 0}'
   '.wp-block-search__button{margin-left:0}'
   # WooCommerce: fashion product grid, grey tiles, no buttons, tiny caps
   '.wc-block-product-template{gap:var(--wp--preset--spacing--50) var(--wp--preset--spacing--10)!important}'
   '.wc-block-product-template .wc-block-components-product-image{background:var(--wp--preset--color--surface);margin-bottom:.6rem!important}'
   '.wc-block-product-template .wp-block-post-title,.wc-block-product-template .wc-block-components-product-price{font-size:var(--wp--preset--font-size--small)!important;text-transform:uppercase;letter-spacing:.06em;text-align:left!important;margin:0 .5rem .15rem!important;font-weight:400}'
   '.wc-block-components-product-sale-badge,.wc-block-components-product-badge{border-radius:0;text-transform:uppercase;font-size:var(--wp--preset--font-size--x-small);background:var(--wp--preset--color--accent);color:var(--wp--preset--color--base);border:0}'
   '.wp-block-woocommerce-product-image-gallery img{background:var(--wp--preset--color--surface)}'
   '.wc-block-components-button,.single_add_to_cart_button{border-radius:0!important;text-transform:uppercase;letter-spacing:.06em;width:100%}'
   '.woocommerce div.product form.cart .button{width:100%;padding:1.1em;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);border-radius:0}'
   '.wc-block-components-text-input input,.wc-block-components-textarea,.wc-block-components-select select,.woocommerce .quantity .qty{border-radius:0!important;border-color:var(--wp--preset--color--contrast)!important}'
   '.woocommerce-tabs .tabs{display:none}'
   '.crate-hero{margin-top:0!important;margin-bottom:0!important}.crate-hero img{width:100%;height:84vh;min-height:22rem;object-fit:cover;object-position:50% 70%}'
   '.crate-pull{margin-top:-.52em!important;position:relative;z-index:1;padding-left:var(--wp--preset--spacing--20)}'
   '.is-style-arrivals-list td:first-child{font-weight:700}'
   '@media (max-width:700px){.is-style-arrivals-list :is(td,th):is(:nth-child(3),:nth-child(4),:nth-child(5)){display:none}}'
   'ul.is-style-label{list-style:none;padding-left:0}'
  ),
 },
 'templateParts': [
  {'area': 'header', 'name': 'header', 'title': 'Header'},
  {'area': 'header', 'name': 'header-home', 'title': 'Header (home, no wordmark)'},
  {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
  {'area': 'uncategorized', 'name': 'notice', 'title': 'Record Store Day bar'},
 ],
 'customTemplates': [
  {'name': 'page-wide', 'title': 'Page, full width', 'postTypes': ['page']},
  {'name': 'page-no-title', 'title': 'Page, no title (edge to edge)', 'postTypes': ['page']},
 ],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Crate
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A stark, image-first shop theme for independent record shops that sell new and graded second-hand vinyl online and over the counter.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: crate
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout, one-column
*/''')

# ---------------------------------------------------------------- style variations
def variation(fname, title, rows, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': pal(rows)}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)

variation('import', 'Import', [
    ('base', '#FFFFFF', 'White'), ('contrast', '#111111', 'Black'), ('accent', '#C8102E', 'Obi red'),
    ('surface', '#F3EFE8', 'Rice paper'), ('line', '#C8102E', 'Obi line'), ('muted', '#5A5A5A', 'Grey text'), ('accent-2', '#FFE600', 'Sticker yellow')],
    {'blocks': {'core/site-title': {'color': {'text': C('accent')}, 'elements': {'link': {'color': {'text': C('accent')}}}}}})
variation('soul', 'Soul', [
    ('base', '#F2E8D8', 'Sleeve card'), ('contrast', '#2A170C', 'Brown ink'), ('accent', '#A63A00', 'Burnt orange'),
    ('surface', '#E4D3B8', 'Cardboard'), ('line', '#2A170C', 'Brown line'), ('muted', '#664A36', 'Faded brown'), ('accent-2', '#F6C443', 'Sticker yellow')])
variation('dub', 'Dub', [
    ('base', '#D8D9D4', 'Concrete grey'), ('contrast', '#0B0B0B', 'Black ink'), ('accent', '#0A5C31', 'Grade green'),
    ('surface', '#C6C8C1', 'Darker grey'), ('line', '#0B0B0B', 'Black line'), ('muted', '#3C3E3A', 'Soot'), ('accent-2', '#E7FF00', 'Sticker lime')])

# ---------------------------------------------------------------- section styles
def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('label', 'Small caps label', ['core/paragraph', 'core/heading', 'core/list'],
        {'typography': {'fontSize': FS('small'), **caps}})
section('wordmark', 'Wordmark', ['core/site-title', 'core/heading', 'core/paragraph'],
        {'typography': {'fontSize': FS('display'), 'fontWeight': '700', 'lineHeight': '0.76', 'letterSpacing': '-0.065em', 'textTransform': 'uppercase'},
         'css': '&{margin-left:-0.04em!important;white-space:nowrap}& a{color:inherit}'})
section('tile-grid', 'Tile grid (2px gutters)', ['core/group'],
        {'spacing': {'blockGap': SP('10')}, 'css': '&{row-gap:var(--wp--preset--spacing--50)!important}& figure{margin-bottom:.55rem}'})
section('tile', 'Product tile', ['core/group'],
        {'typography': {'fontSize': FS('small'), **caps}, 'spacing': {'blockGap': '0'},
         'css': '& > p{margin:0 .5rem!important}& img{aspect-ratio:4/5;object-fit:cover;width:100%}'})
section('spec-table', 'Spec table', ['core/table'],
        {'typography': {'fontSize': FS('small'), **caps},
         'css': '& td:first-child{color:var(--wp--preset--color--muted);width:38%}& table{border-top:1px solid var(--wp--preset--color--line)}'})
section('arrivals-list', 'Arrivals list', ['core/table'],
        {'typography': {'fontSize': FS('small'), **caps},
         'css': '& thead th{border-bottom:1px solid var(--wp--preset--color--line);color:var(--wp--preset--color--muted);font-weight:400}& tr:hover td{background:var(--wp--preset--color--surface)}& td:last-child,& th:last-child{text-align:right;padding-right:0}'})
section('sold', 'Sold / notice red', ['core/paragraph', 'core/group'],
        {'color': {'background': C('accent'), 'text': C('base')},
         'typography': {'fontSize': FS('x-small'), **caps},
         'elements': {'link': {'color': {'text': C('base')}, 'typography': {'textDecoration': 'underline'}}},
         'spacing': {'padding': {'top': SP('20'), 'bottom': SP('20'), 'left': SP('30'), 'right': SP('30')}}})
section('grade', 'Grade sticker', ['core/paragraph'],
        {'color': {'background': C('accent-2'), 'text': C('contrast')},
         'typography': {'fontSize': FS('x-small'), 'fontWeight': '700', **caps},
         'css': '&{display:inline-block;padding:.35em .6em}'})
section('inverse', 'Black', ['core/group', 'core/columns', 'core/cover'],
        {'color': {'background': C('contrast'), 'text': C('base')},
         'elements': {'link': {'color': {'text': C('base')}}, 'heading': {'color': {'text': C('base')}},
                      'button': {'color': {'background': C('base'), 'text': C('contrast')}}},
         'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60'), 'left': SP('30'), 'right': SP('30')}}})
section('grey', 'Grey field', ['core/group', 'core/columns'],
        {'color': {'background': C('surface'), 'text': C('contrast')},
         'spacing': {'padding': {'top': SP('50'), 'bottom': SP('50'), 'left': SP('30'), 'right': SP('30')}}})
section('rule-top', 'Hairline above', ['core/group', 'core/columns'],
        {'border': {'top': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': SP('30')}}})
section('outline-button', 'Outline', ['core/button'],
        {'color': {'background': 'transparent', 'text': C('contrast')},
         'css': '& .wp-block-button__link{background:transparent;color:inherit;border:1px solid currentColor}'})

# ---------------------------------------------------------------- copy data
SHOP = {'addr': '41 Call Lane, Leeds LS1 7BT', 'addr2': '12 Market Street, Hebden Bridge HX7 6AA',
        'email': 'shop@example.com', 'phone': '0113 496 0418'}

# name, artist, title, format, label, catno, country, year, media, sleeve, price, image, notes, stock, category
RECORDS = [
 ('Commodores, Nightshift (7-inch)', 'Commodores', 'Nightshift', '7-inch', 'Motown', 'TMG 1371', 'UK', '1985', 'VG+', 'VG', '6', 'single-motown.jpg', 'Company sleeve with a small tear at the top seam. Plays clean, light surface marks on the B side.', 1, 'Used 7-inch'),
 ('Alice Coltrane, Journey in Satchidananda (LP)', 'Alice Coltrane', 'Journey in Satchidananda', 'LP', 'Impulse!', 'AS-9203', 'US', '1971', 'VG', 'VG+', '48', 'spinning.jpg', 'Gatefold, Van Gelder stamp in the run-out. Some crackle in the lead-in of side one, quiet after that.', 1, 'Used LP'),
 ('Grace Jones, Nightclubbing (LP)', 'Grace Jones', 'Nightclubbing', 'LP', 'Island', 'ILPS 9624', 'UK', '1981', 'NM', 'VG+', '32', 'orange-vinyl.jpg', 'Original inner sleeve. Faint ring wear on the back cover only.', 1, 'Used LP'),
 ('Arthur Russell, World of Echo (LP)', 'Arthur Russell', 'World of Echo', 'LP', 'Audika', 'AU-1004-1', 'US', '2024', 'New', 'New', '27', 'stack.jpg', 'Sealed reissue, 180g, from the 2024 pressing.', 6, 'New LP'),
 ('Talking Heads, Remain in Light (LP)', 'Talking Heads', 'Remain in Light', 'LP', 'Sire', 'SRK 6095', 'UK', '1980', 'VG+', 'VG', '22', 'sleeve-hands.jpg', 'Printed inner with lyrics. Sleeve has a price sticker residue on the front.', 1, 'Used LP'),
 ('Portishead, Dummy (LP)', 'Portishead', 'Dummy', 'LP', 'Go! Beat', '828 553-1', 'UK', '1994', 'VG+', 'VG+', '95', 'shelf.jpg', 'First pressing. Sold on the Saturday it went up, kept here for reference.', 0, 'Used LP'),
 ('Studio One Rockers (LP)', 'Various', 'Studio One Rockers', 'LP', 'Soul Jazz', 'SJR LP48', 'UK', '2023', 'New', 'New', '26', 'crates.jpg', 'Double LP repress, sealed.', 4, 'New LP'),
 ('Kate Bush, Hounds of Love (cassette)', 'Kate Bush', 'Hounds of Love', 'Cassette', 'EMI', 'TC-KAB 1', 'UK', '1985', 'VG', 'VG', '9', 'cassette.jpg', 'Paper J-card, a little faded on the spine. Tape plays evenly, no drop-outs.', 1, 'Used cassette'),
 ('Sade, Diamond Life (LP)', 'Sade', 'Diamond Life', 'LP', 'Epic', 'EPC 26044', 'UK', '1984', 'VG', 'VG', '14', 'digging.jpg', 'Light surface noise between tracks. Sleeve has a name written in biro on the back.', 1, 'Used LP'),
 ('Nina Simone, Wild Is the Wind (LP)', 'Nina Simone', 'Wild Is the Wind', 'LP', 'Philips', 'BL 7738', 'UK', '1966', 'G+', 'VG', '40', 'portable.jpg', 'Mono. Plays through with steady crackle, no skips. Priced for the crackle.', 1, 'Used LP'),
 ('Soul 45s, box of 50 (7-inch)', 'Various', 'Soul 45s, box of 50', '7-inch', 'Various', 'CRATE-BOX-07', 'UK and US', '1964 to 1979', 'VG', 'Company', '60', 'singles-case.jpg', 'Fifty northern soul and funk 45s from one collection, bought in Otley. List inside the lid.', 1, 'Used 7-inch'),
 ('Crate gift card', 'Crate', 'Gift card', 'Card', 'Crate', 'GIFT-25', 'UK', '', 'New', 'New', '25', 'mailer.jpg', 'Spend it online or in either shop. Posted in a card mailer, or emailed.', 50, 'Gift cards'),
]

def slugify(s):
    import re, unicodedata
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9 _-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')

def purl(r):
    return '/product/%s/' % slugify(r[0])

def rec(i):
    return RECORDS[i]

# ---------------------------------------------------------------- patterns
PAD0 = {'spacing': {'padding': {'left': '0', 'right': '0'}}}

def tile(r, alt, extra_line=None):
    name, artist, title, fmt = r[0], r[1], r[2], r[3]
    grade = 'New' if r[8] == 'New' else '%s / %s' % (r[8], r[9])
    price = 'Sold' if r[13] == 0 else '£%s' % r[10]
    return group(J(
        image(r[11], alt, href=purl(r), aspectRatio='4/5', scale='cover'),
        para('<a href="%s">%s</a>' % (purl(r), artist)),
        para(title),
        para('%s, %s, %s' % (fmt, grade, price), textColor='muted' if r[13] else 'accent')),
        className='is-style-tile', layout={'type': 'default'})

ALTS = {
 'single-motown.jpg': 'A Motown 7-inch single with a purple label, lying on grey card',
 'spinning.jpg': 'A black LP with a teal label turning on a dark turntable, seen from above',
 'orange-vinyl.jpg': 'Orange vinyl under a turntable stylus, lit from below',
 'stack.jpg': 'A tall stack of LPs on their sides, spines showing catalogue numbers',
 'sleeve-hands.jpg': 'Hands lifting an LP sleeve above a turntable on a white counter',
 'shelf.jpg': 'A row of LP spines on a shelf next to a pair of headphones',
 'crates.jpg': 'Rows of used LPs packed tight in wooden crates',
 'cassette.jpg': 'Two cassette tapes side by side on a black cloth',
 'digging.jpg': 'A woman flicking through a crate of records by a shop window',
 'portable.jpg': 'A portable record player with a pink-label single on the platter, under a clear lid',
 'singles-case.jpg': 'An open carry case of 7-inch singles on a wooden floor',
 'mailer.jpg': 'A brown 1940s record mailer marked phonograph record, do not bend',
 'hero.jpg': 'A black LP playing on a white turntable, the tone arm in the groove',
 'console.jpg': 'A wooden record console with a black LP on the platter and a row of dials',
 'shop-floor.jpg': 'Customers flicking through racks of LPs in a busy record shop',
}

pattern('hero-wordmark', 'Hero: full-bleed photo with the wordmark', 'featured,banner', J(
  image('hero.jpg', ALTS['hero.jpg'], align='full', className='crate-hero', lightbox=False),
  dyn('site-title', level=1, className='is-style-wordmark crate-pull', isLink=False),
  row(J(para('Used and new records, graded by ear', className='is-style-label'),
        para('<a href="/latest-arrivals/">Latest 100 arrivals</a>', className='is-style-label'),
        para('Call Lane, Leeds. Open today 11 to 7', className='is-style-label')),
      justify='space-between', align='full', style={'spacing': {'padding': {'top': SP('20'), 'bottom': SP('20'), 'left': SP('30'), 'right': SP('30')}}})),
  description='The home hero: one photograph, the shop name as big as the screen allows, and three small lines.')

pattern('campaign-split', 'Two photographs, edge to edge', 'featured,gallery', group(J(
  columns(
    (None, J(image('crates.jpg', ALTS['crates.jpg'], href='/product-category/used-lp/', aspectRatio='4/5', scale='cover'),
             para('<a href="/product-category/used-lp/">Used LPs, in this week</a>', className='is-style-label', style={'spacing': {'padding': {'left': SP('30')}}}))),
    (None, J(image('singles-case.jpg', ALTS['singles-case.jpg'], href='/product-category/used-7-inch/', aspectRatio='4/5', scale='cover'),
             para('<a href="/product-category/used-7-inch/">Seven-inch singles</a>', className='is-style-label', style={'spacing': {'padding': {'left': SP('30')}}}))),
    style={'spacing': {'blockGap': {'left': SP('10'), 'top': SP('40')}}}, align='full')),
  align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': SP('10')}}}))

def arrivals_grid(idx, heading_text='New this week', link=('/shop/', 'All records')):
    return group(J(
      row(J(heading(heading_text, 2), para('<a href="%s">%s</a>' % link, className='is-style-label')), justify='space-between', align='full',
          style={'spacing': {'padding': {'left': SP('30'), 'right': SP('30')}}}),
      group(J(*[tile(rec(i), ALTS[rec(i)[11]]) for i in idx]),
            className='is-style-tile-grid', align='full', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '10rem'})),
      align='full', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('60')}}})

pattern('arrivals-grid', 'Latest arrivals grid (4 across, edge to edge)', 'shop,featured', arrivals_grid([1, 2, 4, 0, 9, 7, 3, 5]),
        description='Records as tiles: photo on grey, artist, title, format, grade pair and price in small caps. Edit links to match your products.')

pattern('staff-picks-grid', 'Staff picks (4 tiles)', 'shop', arrivals_grid([6, 3, 8, 10], 'Picked by Ines this month', ('/shop/', 'Shop everything')))

ARRIVALS = [
 ('Alice Coltrane', 'Journey in Satchidananda', 'Impulse!', 'AS-9203', 'LP', 'VG / VG+', '£48'),
 ('Grace Jones', 'Nightclubbing', 'Island', 'ILPS 9624', 'LP', 'NM / VG+', '£32'),
 ('Talking Heads', 'Remain in Light', 'Sire', 'SRK 6095', 'LP', 'VG+ / VG', '£22'),
 ('Commodores', 'Nightshift', 'Motown', 'TMG 1371', '7"', 'VG+ / VG', '£6'),
 ('Nina Simone', 'Wild Is the Wind', 'Philips', 'BL 7738', 'LP', 'G+ / VG', '£40'),
 ('Arthur Russell', 'World of Echo', 'Audika', 'AU-1004-1', 'LP', 'New', '£27'),
 ('Kate Bush', 'Hounds of Love', 'EMI', 'TC-KAB 1', 'Cass', 'VG / VG', '£9'),
 ('Sade', 'Diamond Life', 'Epic', 'EPC 26044', 'LP', 'VG / VG', '£14'),
 ('Various', 'Studio One Rockers', 'Soul Jazz', 'SJR LP48', '2LP', 'New', '£26'),
 ('Linton Kwesi Johnson', 'Forces of Victory', 'Island', 'ILPS 9566', 'LP', 'VG+ / VG+', '£28'),
 ('Pharoah Sanders', 'Thembi', 'Impulse!', 'AS-9206', 'LP', 'VG / VG', '£35'),
 ('Cocteau Twins', 'Treasure', '4AD', 'CAD 412', 'LP', 'VG+ / VG', '£38'),
 ('Joni Mitchell', 'Hejira', 'Asylum', 'K 53053', 'LP', 'VG+ / VG+', '£18'),
 ('The Specials', 'Ghost Town', '2 Tone', 'CHS TT 17', '7"', 'VG / VG', '£5'),
]

def arrivals_table(n=14):
    rows = [[a, t, l, c, f, g, p] for a, t, l, c, f, g, p in ARRIVALS[:n]]
    return table(rows, head=['Artist', 'Title', 'Label', 'Cat no', 'Format', 'Media / sleeve', 'Price'], className='is-style-arrivals-list', align='wide')

pattern('latest-arrivals-list', 'Latest arrivals (dense list)', 'shop,text', J(
  row(J(heading('Latest 100', 2), para('Updated Tuesday and Friday at 10am', className='is-style-label', textColor='muted')), justify='space-between', align='wide'),
  arrivals_table()), description='The digger\'s list: artist, title, label, cat no, format, grade pair and price in one line per record.')

GENRES = [
 ('Jazz', [('New LP', 'new-lp'), ('Used LP', 'used-lp'), ('Used 7-inch', 'used-7-inch')]),
 ('Soul and funk', [('New LP', 'new-lp'), ('Used LP', 'used-lp'), ('Used 7-inch', 'used-7-inch')]),
 ('Reggae and dub', [('New LP', 'new-lp'), ('Used LP', 'used-lp'), ('Used 7-inch', 'used-7-inch')]),
 ('Rock and pop', [('Used LP', 'used-lp'), ('Used 7-inch', 'used-7-inch'), ('Cassette', 'used-cassette')]),
 ('Electronic', [('New LP', 'new-lp'), ('Used LP', 'used-lp')]),
 ('Folk', [('Used LP', 'used-lp'), ('Cassette', 'used-cassette')]),
 ('Soundtracks', [('Used LP', 'used-lp')]),
 ('Under £5', [('Used LP', 'used-lp'), ('Used 7-inch', 'used-7-inch')]),
]

def genre_block(g, links):
    return group(J(heading('<a href="/?s=%s&amp;post_type=product">%s</a>' % (slugify(g).split('-')[0], g), 3),
                   lst(['<a href="/product-category/%s/">%s</a>' % (s, n) for n, s in links], className='is-style-label')),
                 className='is-style-rule-top', layout={'type': 'default'})

pattern('genre-crates', 'Genre crates, split new and used', 'shop,featured', group(J(
  heading('Crates', 2),
  group(J(*[genre_block(g, l) for g, l in GENRES]), align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '9rem'},
        style={'spacing': {'blockGap': SP('40')}})),
  align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60')}}}),
  description='The shop floor as an index: each genre is a divider, split by format and by new or used.')

pattern('format-index', 'Shop by format', 'shop', row(J(*[
   para('<a href="/product-category/%s/">%s</a>' % (s, n), className='is-style-label') for n, s in
   [('New LP', 'new-lp'), ('Used LP', 'used-lp'), ('Used 7-inch', 'used-7-inch'), ('Cassettes', 'used-cassette'), ('Gift cards', 'gift-cards')]]),
  align='wide', className='is-style-rule-top', style={'spacing': {'blockGap': SP('50')}}))

pattern('crate-divider', 'Crate divider (genre page header)', 'shop', group(J(
  heading('Jazz', 1, className='is-style-wordmark', fontSize='xx-large'),
  row(J(*[para('<a href="/product-category/%s/">%s</a>' % (s, n), className='is-style-label') for n, s in [('New LP', 'new-lp'), ('Used LP', 'used-lp'), ('Used 7-inch', 'used-7-inch')]]),
      style={'spacing': {'blockGap': SP('40')}}),
  para('Spiritual jazz, hard bop and the odd bit of library music. Ines prices the jazz, so blame her for the Impulse! gatefolds.')),
  align='wide', layout={'type': 'default'}), description='Put this at the top of a genre page. Change the heading and the format links.')

def spec(r):
    rows = [['Artist', r[1]], ['Title', r[2]], ['Format', r[3]], ['Label', r[4]], ['Cat no', r[5]], ['Country', r[6]], ['Year', r[7]],
            ['Media', r[8]], ['Sleeve', r[9]]]
    return table(rows, className='is-style-spec-table')

pattern('used-record-spec', 'Used record: grade pair and pressing details', 'shop', J(
  row(J(para('Media VG', className='is-style-grade'), para('Sleeve VG+', className='is-style-grade')), style={'spacing': {'blockGap': SP('20')}}),
  spec(rec(1)),
  para('<a href="/grading/">How we grade</a>', className='is-style-label')),
  description='The signature block for a used copy: the two grades first, then label, cat no, country and year.')

pattern('grading-notes', 'Grading notes for one copy', 'shop', group(J(
  heading('Notes on this copy', 3),
  para('Gatefold, Van Gelder stamp in the run-out. Some crackle in the lead-in of side one, quiet after that. Play-graded on the shop deck by Delroy on 12 September.')),
  className='is-style-rule-top', layout={'type': 'default'}))

pattern('copy-photos', 'Photos of the actual copy (front, back, label)', 'shop,gallery', gallery([
  ('spinning.jpg', 'The record itself on the platter, teal label showing', 'Label'),
  ('stack.jpg', 'The copy in a stack of Impulse! LPs, spine showing', 'Spine'),
  ('sleeve-hands.jpg', 'The front sleeve held above the turntable', 'Sleeve')], columns=3, align='wide'),
  description='Three photos of the copy you will get. Replace them with your own; shoot them flat and square.')

pattern('staff-note', 'Staff note on a record', 'text,testimonials', quote(
  'Side two is the one. If you only know the title track, put the needle on Stopover Bombay and turn it up.',
  'Ines Barros, jazz and soul buyer'))

pattern('grading-guide', 'Grading guide (M to G)', 'text', J(
  heading('How we grade', 2),
  para('Every used record is played on the shop deck before it goes online. We grade the record (media) and the sleeve separately, and we grade down when we are unsure.'),
  table([['M', 'Mint', 'Sealed or never played. We almost never use it for used stock.'],
         ['NM', 'Near mint', 'Played a few times, no marks you can see or hear.'],
         ['VG+', 'Very good plus', 'Light marks under a lamp, silent in play. Most people are happy here.'],
         ['VG', 'Very good', 'Surface noise between tracks and in quiet passages. Music comes first.'],
         ['G+', 'Good plus', 'Constant crackle, still plays through without skips. Priced to match.'],
         ['G', 'Good', 'For completists and DJs who need the one break. Tell us if you want a clip.']],
        head=['Grade', 'Name', 'What it sounds like'], className='is-style-spec-table')))

pattern('sell-what-we-buy', 'Sell to us: what we buy', 'text', columns(
  (None, J(heading('What we buy', 2),
     lst(['LPs and 7-inch singles in jazz, soul, reggae, funk, folk, electronic and good rock', 'Whole collections, from 50 records to a garage full', 'Cassettes if they have their inlays', 'Turntables and amps in working order, by appointment']))),
  (None, J(heading('What we pass on', 2),
     lst(['Compilations from the 80s and 90s, especially the numbered ones', 'Classical box sets', 'Anything water-damaged or mouldy', 'CDs, for now. We ran out of room.']))),
  align='wide'))

pattern('sell-bring-it-in', 'Sell to us: bring it in', 'text', group(J(
  heading('Bring it in', 2),
  para('Tuesday to Thursday, 11am to 4pm, at Call Lane. No appointment needed for up to three boxes. We look through while you wait, usually 20 minutes a box, and offer cash or 25% more in shop credit.'),
  para('Photo ID is required for every sale, even if we know you. It is a condition of our second-hand dealer licence.', className='is-style-label')),
  className='is-style-grey', align='wide', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('sell-collection-visits', 'Sell to us: collection visits', 'text', J(
  heading('Collection visits', 2),
  para('For more than 500 records we come to you, anywhere within about an hour of Leeds. Send a few phone photos of the shelves and some spines to <a href="mailto:%s">%s</a>. Delroy replies within three working days.' % (SHOP['email'], SHOP['email']))))

pattern('stores-list', 'Two shops, addresses and hours', 'contact', columns(
  (None, J(image('shop-floor.jpg', ALTS['shop-floor.jpg'], aspectRatio='4/5', scale='cover'),
     heading('Call Lane, Leeds', 3),
     para('%s. Five minutes from the station, next to the tile shop. One step at the door, we have a ramp.' % SHOP['addr']),
     table([['Mon', 'Closed'], ['Tue to Sat', '11am to 7pm'], ['Sun', '12pm to 5pm']], className='is-style-spec-table'))),
  (None, J(image('digging.jpg', ALTS['digging.jpg'], aspectRatio='4/5', scale='cover'),
     heading('Market Street, Hebden Bridge', 3),
     para('%s. Smaller, mostly used LPs and all the folk. Card only, no buying at this shop.' % SHOP['addr2']),
     table([['Mon to Thu', 'Closed'], ['Fri and Sat', '10am to 6pm'], ['Sun', '11am to 4pm']], className='is-style-spec-table'))),
  align='wide', style={'spacing': {'blockGap': {'left': SP('10')}}}))

pattern('find-us-line', 'Contact line (phone and email)', 'contact', para(
  'Call <a href="tel:01134960418">%s</a> or email <a href="mailto:%s">%s</a>. We answer the phone when the shop is open and nobody is at the till.' % (SHOP['phone'], SHOP['email'], SHOP['email'])))

pattern('shipping-rates', 'Shipping rates', 'shop', J(
  heading('Shipping', 2),
  table([['UK, 1 to 3 LPs', '£4.95', '2 to 3 working days'], ['UK, 4 or more LPs', '£7.50', '2 to 3 working days'], ['UK, 7-inch only', '£2.80', '2 to 3 working days'],
         ['EU', '£14', '5 to 9 working days'], ['Rest of the world', '£22', '7 to 15 working days']], head=['Where', 'Cost', 'Usually takes'], className='is-style-spec-table'),
  para('LPs travel out of their sleeves to stop seam splits, in a stiff mailer with card corners. Orders placed by 1pm go out the same day.')))

pattern('returns-policy', 'Returns', 'shop', J(
  heading('Returns', 2),
  para('New records: send them back unopened within 30 days for a full refund. Used records: if a copy plays worse than the grade we gave it, tell us within 14 days and we refund it and the postage. We do not take returns on used records because you changed your mind.')))

pattern('notice-record-store-day', 'Notice: Record Store Day rules', 'banner', group(
  para('Record Store Day, Saturday 18 April. Doors at 8am, queue on Call Lane, one copy of each title per person, nothing goes online until Monday. Take this bar out on Sunday.'),
  className='is-style-sold', align='full', layout={'type': 'constrained'}),
  description='A red bar for the day only. Edit the date and rules, then remove it.')

pattern('wants-list', 'Wants list', 'shop,text', group(J(
  heading('On our wants list', 2),
  lst(['Any Blue Note first pressings, even rough ones', 'UK 2 Tone singles in picture sleeves', 'Studio One LPs with the original labels', 'Folk on Topic, Transatlantic and Village Thing', 'Working Technics decks for the shop counter']),
  para('Got one? Bring it in Tuesday to Thursday or email a photo of the label.', className='is-style-label')),
  className='is-style-rule-top', layout={'type': 'default'}))

pattern('sold-note', 'Sold item note', 'shop', para(
  'Sold. We keep sold records on the site so you can see what comes through and what it went for. Add it to your wants list and we will email you if another copy turns up.', className='is-style-sold'))

pattern('newsletter', 'Newsletter (Friday list)', 'call-to-action', group(J(
  heading('The Friday list', 2),
  para('Every Friday at 10am, the week\'s best used arrivals in one plain email. Around 40 records, with grades and prices, before they go on the site.'),
  buttons(('Get the Friday list', 'mailto:%s?subject=Friday%%20list' % SHOP['email']))),
  className='is-style-inverse', align='full', layout={'type': 'constrained'}, anchor='newsletter'))

pattern('lookbook-full', 'Full-bleed photograph with a caption', 'featured,gallery', J(
  image('console.jpg', ALTS['console.jpg'], align='full', aspectRatio='16/9', scale='cover', style={'spacing': {'margin': {'top': SP('70')}}}),
  para('The listening console at Call Lane. Ask and we will play any used record before you buy it.', className='is-style-label', style={'spacing': {'padding': {'left': SP('30')}}})))

pattern('mail-order-note', 'Mail order note', 'shop', columns(
  ('40%', image('mailer.jpg', ALTS['mailer.jpg'], aspectRatio='4/5', scale='cover')),
  (None, J(heading('Posting records since 2011', 2),
     para('Delroy packs every order himself at the back of Call Lane. Records go out of the sleeve, into a rigid mailer with card corners, and he writes the grade on the dispatch note so you can check it against the record.'),
     para('<a href="/shipping/">Rates and times</a>', className='is-style-label'))), align='wide'))

pattern('events-list', 'In-store events (latest posts)', 'posts,query', group(J(
  row(J(heading('In the shop', 2), para('<a href="/events/">All events</a>', className='is-style-label')), justify='space-between', align='wide'),
  query(J(dyn('post-featured-image', isLink=True, aspectRatio='4/5', scale='cover'), dyn('post-date', format='j M'), dyn('post-title', isLink=True, level=3)),
        per_page=4, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '10rem'}, align='wide')),
  align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': SP('60'), 'bottom': SP('60')}}}))

pattern('post-grid', 'Event grid (inherits the page query)', 'posts,query', inherit_query(
  J(dyn('post-featured-image', isLink=True, aspectRatio='4/5', scale='cover'), dyn('post-date', format='j M Y'), dyn('post-title', isLink=True, level=2), dyn('post-excerpt', excerptLength=18, fontSize='small')),
  layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}, align='wide'), inserter=False)

pattern('post-list', 'Search results list', 'posts,query', inherit_query(
  row(J(dyn('post-date', format='d.m.y'), dyn('post-title', isLink=True, level=2, fontSize='small')), wrap=True, className='is-style-rule-top'), align='wide'), inserter=False)

pattern('about-shop', 'About the shop', 'about', columns(
  ('50%', image('shop-floor.jpg', ALTS['shop-floor.jpg'], aspectRatio='4/5', scale='cover')),
  (None, J(heading('Crate', 2),
     para('Delroy Mensah opened Crate on Call Lane in 2011 with his own collection and a borrowed till. Ines Barros joined in 2016 to run the jazz and soul, and opened the Hebden Bridge shop in 2021.'),
     para('We sell used records, mostly, with a wall of new pressings from labels we like. Every used copy is played before it is priced. We think grading by eye is how people end up with a VG+ that sounds like frying bacon.'),
     para('We do not do online auctions, and we do not hold records without payment.'))), align='wide'))

# Page layouts
pattern('page-latest-arrivals', 'Page: latest arrivals', 'shop', J(
  para('The last 100 records to go on the shelves, newest first. Used copies are one-offs, so if you want it, buy it or come in.'),
  arrivals_table(), pattern_ref('arrivals-grid')), block_types='core/post-content', description='The list-first arrivals page.')

pattern('page-crates', 'Page: genre crates', 'shop', J(
  para('Every genre is split the way the racks are: new LPs, used LPs, used singles. Tap a format to see what is in that crate today.'),
  pattern_ref('genre-crates'), pattern_ref('format-index'), pattern_ref('crate-divider')), block_types='core/post-content')

pattern('page-sell-to-us', 'Page: sell to us', 'text', J(
  para('We buy records every week, from single LPs to whole houses. Cash or shop credit, paid on the spot.', fontSize='large'),
  pattern_ref('sell-what-we-buy'), pattern_ref('sell-bring-it-in'), pattern_ref('sell-collection-visits'), pattern_ref('wants-list')), block_types='core/post-content')

pattern('page-grading', 'Page: grading guide', 'text', J(pattern_ref('grading-guide'), pattern_ref('used-record-spec'), pattern_ref('staff-note')), block_types='core/post-content')

pattern('page-stores', 'Page: shops and hours', 'contact', J(pattern_ref('stores-list'), pattern_ref('find-us-line'), pattern_ref('about-shop')), block_types='core/post-content')

pattern('page-shipping', 'Page: shipping and returns', 'shop', J(pattern_ref('shipping-rates'), pattern_ref('returns-policy'), pattern_ref('mail-order-note')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
HEADER_PAD = {'spacing': {'padding': {'top': SP('30'), 'bottom': SP('30'), 'left': SP('30'), 'right': SP('30')}}}
write('parts/header.html', group(J(
  dyn('site-title', level=0, textAlign='center'),
  row(dyn('navigation', layout={'type': 'flex', 'justifyContent': 'center'}, overlayMenu='mobile'), justify='center')),
  tag='header', align='full', layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'center'},
  style={**HEADER_PAD, 'spacing': {**HEADER_PAD['spacing'], 'blockGap': SP('20')}}))

write('parts/header-home.html', group(
  dyn('navigation', layout={'type': 'flex', 'justifyContent': 'center'}, overlayMenu='mobile'),
  tag='header', align='full', layout={'type': 'flex', 'justifyContent': 'center'}, style=HEADER_PAD))

write('parts/notice.html', pattern_ref('notice-record-store-day'))

write('parts/footer.html', group(J(
  group(J(
    group(J(heading('Call Lane', 2), para('%s<br>Tue to Sat 11 to 7, Sun 12 to 5<br><a href="tel:01134960418">%s</a>' % (SHOP['addr'], SHOP['phone']), className='is-style-label')), layout={'type': 'default'}),
    group(J(heading('Hebden Bridge', 2), para('%s<br>Fri and Sat 10 to 6, Sun 11 to 4<br>Card only' % SHOP['addr2'], className='is-style-label')), layout={'type': 'default'}),
    group(J(heading('Help', 2), para('<a href="/shipping/">Shipping and returns</a><br><a href="/grading/">Grading</a><br><a href="/sell-to-us/">Sell to us</a><br><a href="mailto:%s">%s</a>' % (SHOP['email'], SHOP['email']), className='is-style-label')), layout={'type': 'default'}),
    group(J(heading('Friday list', 2), para('The week\'s used arrivals by email, before they go online. <a href="mailto:%s?subject=Friday%%20list">Sign up</a>' % SHOP['email'], className='is-style-label')), layout={'type': 'default'})),
    align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '10rem'}),
  row(J(dyn('site-title', level=0), para('Demo photographs are CC0 and public domain images from Wikimedia Commons and Unsplash, used as stand-ins for real copies.', className='is-style-label', textColor='muted')),
      justify='space-between', align='wide', className='is-style-rule-top')),
  tag='footer', align='full', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': SP('70'), 'bottom': SP('40')}, 'blockGap': SP('60')}}))

# ---------------------------------------------------------------- templates
def main(inner, pad_top='50', **kw):
    return group(inner, tag='main', style={'spacing': {'padding': {'top': SP(pad_top), 'bottom': SP('70')}}}, **kw)

def tpl(name, inner, header='header'):
    write('templates/%s.html' % name, J(template_part(header, 'header'), inner, template_part('footer', 'footer')))

tpl('front-page', group(J(pattern_ref('hero-wordmark'), pattern_ref('arrivals-grid'), pattern_ref('campaign-split'),
    pattern_ref('genre-crates'), pattern_ref('latest-arrivals-list'), pattern_ref('lookbook-full'), pattern_ref('newsletter')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': '0'}}), header='header-home')

tpl('page', main(J(dyn('post-title', level=1, align='wide'), dyn('post-content', layout={'type': 'constrained'}, align='wide')), layout={'type': 'constrained'}))
tpl('page-wide', main(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1600px'})), layout={'type': 'constrained'}))
tpl('page-no-title', group(dyn('post-content', align='full', layout={'type': 'constrained'}), tag='main', layout={'type': 'constrained'}))

tpl('single', main(J(
  columns(('58%', dyn('post-featured-image', aspectRatio='4/5', scale='cover')),
          (None, J(dyn('post-date', format='l j F Y'), dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained', 'justifyContent': 'left'}),
                   dyn('post-terms', term='category', prefix='Filed under '))), align='wide', style={'spacing': {'blockGap': {'left': SP('50')}}}),
  row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)),
      justify='space-between', align='wide', className='is-style-rule-top')), layout={'type': 'constrained'}))

tpl('home', main(J(heading('Events', 1, align='wide'), dyn('categories', className='is-style-label'), pattern_ref('post-grid')), layout={'type': 'constrained'}))
tpl('index', main(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-grid')), layout={'type': 'constrained'}))
tpl('archive', main(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('post-grid')), layout={'type': 'constrained'}))
tpl('search', main(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Artist, title or cat no', buttonText='Search', align='wide'),
    pattern_ref('post-list')), layout={'type': 'constrained'}))
tpl('404', main(J(heading('Not in the racks', 1),
    para('That page has gone, or the record sold and we took the link down. Try the <a href="/latest-arrivals/">latest 100</a> or search by artist or cat no.'),
    dyn('search', label='Search', showLabel=False, placeholder='Artist, title or cat no', buttonText='Search')), pad_top='70', layout={'type': 'constrained'}))

# WooCommerce templates
def product_collection(per_page=16, cols=4):
    q = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'product', 'order': 'desc', 'orderBy': 'date', 'search': '', 'exclude': [],
         'inherit': True, 'taxQuery': {}, 'isProductCollectionBlock': True, 'woocommerceOnSale': False,
         'woocommerceStockStatus': ['instock', 'outofstock', 'onbackorder'], 'woocommerceAttributes': [], 'woocommerceHandPickedProducts': []}
    a = {'queryId': 0, 'query': q, 'tagName': 'div', 'displayLayout': {'type': 'flex', 'columns': cols, 'shrinkColumns': True},
         'dimensions': {'widthType': 'fill'}, 'queryContextIncludes': ['collection'], 'align': 'full'}
    tmpl = J(dyn('woocommerce/product-image', showSaleBadge=True, imageSizing='single', isDescendentOfQueryLoop=True, aspectRatio='4/5', scale='cover'),
             dyn('post-title', level=2, isLink=True, fontSize='small', __woocommerceNamespace='woocommerce/product-collection/product-title'),
             dyn('woocommerce/product-price', isDescendentOfQueryLoop=True, fontSize='small'))
    return ('<!-- wp:woocommerce/product-collection %s -->\n<div class="wp-block-woocommerce-product-collection alignfull">'
            '<!-- wp:woocommerce/product-template -->\n%s\n<!-- /wp:woocommerce/product-template -->\n\n'
            '<!-- wp:query-pagination {"layout":{"type":"flex","justifyContent":"center"}} -->\n<!-- wp:query-pagination-previous /-->\n\n<!-- wp:query-pagination-numbers /-->\n\n<!-- wp:query-pagination-next /-->\n<!-- /wp:query-pagination -->\n\n'
            '<!-- wp:woocommerce/product-collection-no-results -->\n%s\n<!-- /wp:woocommerce/product-collection-no-results --></div>\n<!-- /wp:woocommerce/product-collection -->') % (
        json.dumps(a, separators=(',', ':')), tmpl, para('Nothing in this crate right now. New stock goes up Tuesday and Friday at 10am.'))

shop_head = J(
  row(J(dyn('query-title', type='archive', showPrefix=False), para('<a href="/latest-arrivals/">Latest 100 as a list</a>', className='is-style-label')), justify='space-between', align='wide'),
  dyn('term-description', align='wide'),
  pattern_ref('format-index'))
for name in ('archive-product', 'taxonomy-product_cat', 'product-search-results'):
    tpl(name, main(J(dyn('woocommerce/store-notices'), shop_head, product_collection()), pad_top='40', layout={'type': 'constrained'}))

tpl('single-product', main(J(
  dyn('woocommerce/store-notices'),
  columns(('62%', dyn('woocommerce/product-image', showProductLink=False, showSaleBadge=True, imageSizing='single', isDescendentOfSingleProductTemplate=True, aspectRatio='4/5', scale='cover')),
          (None, group(J(dyn('post-title', level=1, fontSize='large', __woocommerceNamespace='woocommerce/product-query/product-title'),
                   dyn('woocommerce/product-price', isDescendentOfSingleProductTemplate=True, fontSize='small'),
                   dyn('post-excerpt', __woocommerceNamespace='woocommerce/product-query/product-summary', fontSize='small'),
                   dyn('woocommerce/add-to-cart-form'),
                   para('UK orders placed by 1pm go out the same day. Used records are one-offs: once it is in someone\'s basket, it is gone.', className='is-style-label', textColor='muted'),
                   dyn('woocommerce/product-details')),
                   layout={'type': 'default'}, style={'position': {'type': 'sticky', 'top': '0px'}, 'spacing': {'padding': {'top': SP('30'), 'right': SP('30'), 'left': SP('30')}}})),
          align='full', style={'spacing': {'blockGap': {'left': SP('50')}}}),
  group(J(heading('How we grade', 2), para('We play every used record before we price it, and grade the media and the sleeve separately. <a href="/grading/">Read the grading guide</a>.')),
        className='is-style-rule-top', align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': SP('70')}}})), pad_top='10', layout={'type': 'constrained'}))

print('crate built:', len(os.listdir(os.path.join(D, 'patterns'))), 'patterns')

# ---------------------------------------------------------------- demo content
def product_desc(r):
    return J(para(r[12]), spec(r))

demo = {
 'site': {'title': 'Crate', 'tagline': 'Used and new records, Call Lane, Leeds'},
 'categories': [{'slug': 'events', 'name': 'Events'}, {'slug': 'shop-news', 'name': 'Shop news'}],
 'front_page': 'home', 'posts_page': 'events',
 'pages': [
  {'slug': 'home', 'title': 'Home', 'content': ''},
  {'slug': 'events', 'title': 'Events', 'content': ''},
  {'slug': 'latest-arrivals', 'title': 'Latest 100', 'pattern': 'crate/page-latest-arrivals', 'template': 'page-wide'},
  {'slug': 'crates', 'title': 'Crates', 'pattern': 'crate/page-crates', 'template': 'page-wide'},
  {'slug': 'sell-to-us', 'title': 'Sell to us', 'pattern': 'crate/page-sell-to-us', 'template': 'page-wide'},
  {'slug': 'grading', 'title': 'Grading', 'pattern': 'crate/page-grading'},
  {'slug': 'stores', 'title': 'Shops', 'pattern': 'crate/page-stores', 'template': 'page-wide'},
  {'slug': 'shipping', 'title': 'Shipping and returns', 'pattern': 'crate/page-shipping', 'template': 'page-wide'},
 ],
 'posts': [
  {'title': 'Record Store Day: queue from 8am on Call Lane', 'category': 'events', 'image': 'shop-floor.jpg', 'content': J(
     para('Doors open at 8am on Saturday 18 April. One copy of each title per person, and nothing from the day goes online until Monday at 10am.'),
     para('Bring a flask. We will have tea from 7.30 for the front of the queue.'))},
  {'title': 'Listening night: Impulse! gatefolds, side two only', 'category': 'events', 'image': 'spinning.jpg', 'content': J(
     para('Thursday 2 October, 7pm to 9pm at Call Lane. Ines plays the second sides of eight Impulse! records on the shop console. Free, 30 places, first come.'))},
  {'title': 'Buying trip to Otley: 1,400 soul and funk 45s', 'category': 'shop-news', 'image': 'singles-case.jpg', 'content': J(
     para('We bought a collection of singles from a former DJ in Otley. They go out in boxes of 50 and on the singles wall from next Tuesday.'))},
  {'title': 'Folk crate moves to Hebden Bridge', 'category': 'shop-news', 'image': 'digging.jpg', 'content': J(
     para('From October the folk section lives at Market Street. Call Lane keeps a small crate of new folk pressings by the counter.'))},
  {'title': 'Cassette table, every Sunday in October', 'category': 'events', 'image': 'cassette.jpg', 'content': J(
     para('A table of used tapes at £2 each by the door on Sundays. Inlays included, no cases for the ones that arrived without.'))},
  {'title': 'Why we play every used record before it is priced', 'category': 'shop-news', 'image': 'hero.jpg', 'content': J(
     para('Grading by eye misses pressing faults, warps you can only hear, and the long scratch that looks like a hairline. So every used record goes on the shop deck for at least a minute a side.'),
     para('It is slower. It is also why our returns pile is small.'))},
 ],
 'nav': [
  {'label': 'Shop', 'url': '/shop/'}, {'label': 'Latest 100', 'url': '/latest-arrivals/'}, {'label': 'Crates', 'url': '/crates/'},
  {'label': 'Sell to us', 'url': '/sell-to-us/'}, {'label': 'Grading', 'url': '/grading/'}, {'label': 'Events', 'url': '/events/'}, {'label': 'Shops', 'url': '/stores/'},
 ],
 'currency': 'GBP',
 'products': [
  {'name': r[0], 'price': r[10], 'image': r[11], 'category': r[14], 'sku': r[5].replace(' ', '-'), 'stock': r[13],
   'short': ('Media %s, sleeve %s. %s %s, %s %s.' % (r[8], r[9], r[4], r[5], r[6], r[7])) if r[8] != 'New' else ('New, sealed. %s %s.' % (r[4], r[5])),
   'description': product_desc(r)} for r in RECORDS],
}
os.makedirs('demos/crate', exist_ok=True)
json.dump(demo, open('demos/crate/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
