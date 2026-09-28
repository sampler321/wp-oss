# Design note (drum, idea 010, riso and printmaking studio). Owner's brief: "definitely neo-brutalist!"
# Direction: neo-brutalist riso shop counter. Hard 3px black borders on everything that holds content, flat riso ink
# fills, offset hard shadows (tokenised as theme.json shadow presets), chunky Syne 800, the grid left visible.
# Why: a riso studio sells process: inks, paper, lead times, file rules. Boxes and swatches make that scannable.
# Fonts: Syne 700 to 800 (display, registry) + Rethink Sans (body). Palette: paper white, riso black #1A1A1A,
# riso blue #0078BF (links), fluorescent pink #FF48B0 and yellow #FFE800 as fills, the real ink list as tokens.
# Layout idea: every section is a bordered slab with a hard shadow; columns are split by thick visible rules; the
# signature "overprint" pattern stacks two images with pink and blue ink duotones and multiply blending, offset by
# a few pixels like a mis-registered riso proof.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('drum')
S = THEME['slug']

CATS = {'drum-home': 'Riso: home and heroes', 'drum-print': 'Riso: print services', 'drum-inks': 'Riso: inks and paper',
        'drum-workshops': 'Riso: workshops and club', 'drum-shop': 'Riso: shop', 'drum-jobs': 'Riso: jobs and portfolio',
        'drum-about': 'Riso: about and co-op', 'drum-contact': 'Riso: contact and notices', 'drum-pages': 'Riso: page layouts'}
CATMAP = {'featured': 'drum-home', 'services': 'drum-print', 'text': 'drum-print', 'call-to-action': 'drum-print', 'shop': 'drum-shop',
          'about': 'drum-about', 'banner': 'drum-contact', 'gallery': 'drum-jobs', 'posts': 'drum-jobs', 'testimonials': 'drum-about',
          'contact': 'drum-contact', 'ink-chart': 'drum-inks', 'paper-library': 'drum-inks', 'swatch-cards': 'drum-inks',
          'workshop-dates': 'drum-workshops', 'print-club': 'drum-workshops', 'file-setup': 'drum-print', 'lead-times': 'drum-print'}
_pattern = pattern
def pattern(slug, title, cats, body, **kw):
    first = cats.split(',')[0]
    c = 'drum-pages' if kw.get('block_types') == 'core/post-content' else CATMAP.get(slug) or CATMAP.get(first, 'drum-home')
    return _pattern(slug, title, c + ',' + cats, body, **kw)


def wjson(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))


def sp(n):
    return 'var:preset|spacing|%s' % n


def pad(t=None, b=None, l=None, r=None):
    p = {}
    for k, v in (('top', t), ('bottom', b), ('left', l), ('right', r)):
        if v is not None:
            p[k] = sp(v)
    return {'spacing': {'padding': p}}


FONTS = json.load(open(os.path.join(THEME['dir'], '.fonts.json')))['fontFamilies']

INKS = [  # slug, hex, name, text colour slug, note
    ('contrast', '#1A1A1A', 'Black', 'base', 'The cheapest drum. Use it for text.'),
    ('accent', '#0078BF', 'Blue', 'base', 'Our most used colour. Deep in solids, soft in tints.'),
    ('accent-2', '#FF48B0', 'Fluorescent pink', 'contrast', 'Glows under blue. Fades in a sunny window within a year.'),
    ('ink-yellow', '#FFE800', 'Yellow', 'contrast', 'Barely shows on its own at 30%. Great under blue for green.'),
    ('ink-green', '#00A95C', 'Green', 'contrast', 'A flat grass green. Doesn\'t overprint pink nicely.'),
    ('ink-orange', '#FF6C2F', 'Orange', 'contrast', 'Warm and loud. Over blue it goes brown.'),
    ('ink-purple', '#765BA7', 'Purple', 'base', 'Plus £15 per job: we mix it on the day.'),
    ('ink-mint', '#82D8D5', 'Mint', 'contrast', 'Soft. Needs a second colour to carry text.'),
    ('ink-red', '#FF665E', 'Bright red', 'contrast', 'More coral than red. Over yellow, it glows.'),
]
PALETTE = [('base', '#FFFFFF', 'Paper'), ('surface', '#F1EFE8', 'Recycled paper'), ('line', '#1A1A1A', 'Rule')] + \
          [(s, c, n) for s, c, n, t, x in INKS] + [('muted', '#4D4D4D', 'Half-tone grey')]

SH = lambda x, c='contrast': '%dpx %dpx 0 0 var(--wp--preset--color--%s)' % (x, x, c)
SHADOWS = [
    {'slug': 'hard-sm', 'name': 'Hard, small', 'shadow': SH(3)},
    {'slug': 'hard', 'name': 'Hard', 'shadow': SH(6)},
    {'slug': 'hard-lg', 'name': 'Hard, large', 'shadow': SH(12)},
    {'slug': 'pink', 'name': 'Pink offset', 'shadow': SH(8, 'accent-2')},
    {'slug': 'blue', 'name': 'Blue offset', 'shadow': SH(8, 'accent')},
]
B3 = '3px solid var(--wp--preset--color--contrast)'
focus = {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}

CSS = (
    ':where(h1,h2,h3){text-wrap:balance;overflow-wrap:break-word;hyphens:auto}:where(p){text-wrap:pretty}body{font-synthesis:none}'
    '.wp-block-table{font-variant-numeric:tabular-nums}'
    '.wp-block-table table.has-fixed-layout{table-layout:auto}'
    '.wp-block-table table{border:' + B3 + ';background:var(--wp--preset--color--base);box-shadow:var(--wp--preset--shadow--hard)}'
    '.wp-block-table table td,.wp-block-table table th{border:0;border-bottom:2px solid var(--wp--preset--color--contrast);padding:.65em .9em;text-align:left;vertical-align:top}'
    '.wp-block-table table.has-fixed-layout td,.wp-block-table table.has-fixed-layout th{word-break:normal;overflow-wrap:normal}'
    '.wp-block-table table thead{border-bottom:0}.wp-block-table table thead th{background:var(--wp--preset--color--ink-yellow);border-bottom:' + B3 + ';font-weight:800}'
    '.wp-block-table table tr>*+*{border-left:2px solid var(--wp--preset--color--contrast)}'
    '@media (prefers-reduced-motion:no-preference){.wp-element-button,.wp-block-button__link{transition:transform .08s,box-shadow .08s}}'
    '.wp-element-button:hover,.wp-block-button__link:hover{transform:translate(3px,3px);box-shadow:none!important}'
    '.wp-block-site-title a{text-shadow:2px 2px 0 var(--wp--preset--color--accent-2)}'
    '.wp-block-navigation .current-menu-item>a{background:var(--wp--preset--color--ink-yellow);outline:2px solid var(--wp--preset--color--contrast)}'
    '.wc-block-product img,li.product img{border:' + B3 + ';aspect-ratio:1;object-fit:cover}'
    '.wc-block-product.outofstock img,li.product.outofstock img{filter:grayscale(1)}'
    '.wc-block-product.outofstock .wc-block-components-product-price::after,li.product.outofstock .price::after{content:" sold out";font-weight:800}'
    '@media (min-width:782px){.wp-block-columns.is-style-ruled>.wp-block-column+.wp-block-column{border-left:' + B3 + ';padding-left:var(--wp--preset--spacing--50)}}'
    '@media (max-width:781px){.wp-block-columns.is-style-ruled>.wp-block-column+.wp-block-column{border-top:' + B3 + ';padding-top:var(--wp--preset--spacing--40)}}'
)

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE],
                  'duotone': [{'slug': 'pink-ink', 'name': 'Pink ink on paper', 'colors': ['#FF48B0', '#FFFFFF']},
                              {'slug': 'blue-ink', 'name': 'Blue ink on paper', 'colors': ['#0078BF', '#FFFFFF']},
                              {'slug': 'black-ink', 'name': 'Black ink on paper', 'colors': ['#1A1A1A', '#FFFFFF']}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': FONTS,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Small print', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '1.9rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.2rem', 'max': '4rem'}},
                {'slug': 'display', 'size': '6.5rem', 'name': 'Display', 'fluid': {'min': '2.6rem', 'max': '6.5rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': SHADOWS},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55'},
        'spacing': {'padding': {'left': sp(40), 'right': sp(40)}, 'blockGap': sp(30)},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast', 'background': 'var:preset|color|ink-yellow'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '0.98', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.02'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.1'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0'}},
            'button': {'color': {'background': 'var:preset|color|ink-yellow', 'text': 'var:preset|color|contrast'},
                       'border': {'radius': '0', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                       'shadow': 'var:preset|shadow|hard-sm',
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|medium'},
                       'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '1.1em', 'right': '1.1em'}},
                       ':hover': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'}},
                       ':focus': focus},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'}, 'color': {'text': 'var:preset|color|contrast'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.02em'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '800'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'background': 'var:preset|color|ink-yellow'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '800'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
            'core/image': {'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid', 'radius': '0'}},
            'core/post-featured-image': {'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid', 'radius': '0'}, 'shadow': 'var:preset|shadow|hard'},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '3px 0 0 0'}, 'css': '&{opacity:1}'},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.2'},
                           'color': {'background': 'var:preset|color|accent-2'},
                           'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}, 'shadow': 'var:preset|shadow|hard',
                           'spacing': {'padding': {'top': sp(40), 'bottom': sp(40), 'left': sp(40), 'right': sp(40)}},
                           'css': '& cite{display:block;margin-top:.8em;font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--small);font-style:normal;font-weight:700}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}, 'spacing': {'padding': {'top': sp(30), 'bottom': sp(30), 'left': sp(30), 'right': sp(30)}},
                             'css': '& summary{font-weight:800}'},
            'core/search': {'css': '& .wp-block-search__input{border:3px solid var(--wp--preset--color--contrast);border-radius:0}'},
            'core/code': {'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '800'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-job', 'title': 'Print job (specs beside the photo)', 'postTypes': ['post']},
    ],
}
wjson('theme.json', theme)


def variation(title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}
    if extra:
        d['styles'] = extra
    return d

REST = [(s, c, n) for s, c, n, t, x in INKS if s.startswith('ink-')]
wjson('styles/two-ink.json', variation('Two-ink', [
    ('base', '#FFFFFF', 'Paper'), ('contrast', '#1A1A1A', 'Black'), ('accent', '#0078BF', 'Blue'), ('accent-2', '#FF665E', 'Bright red'),
    ('surface', '#FFE3E1', 'Red tint'), ('line', '#1A1A1A', 'Rule'), ('muted', '#4D4D4D', 'Grey'),
    ('ink-yellow', '#FF665E', 'Bright red')] + [x for x in REST if x[0] != 'ink-yellow'],
    {'elements': {'button': {'color': {'background': 'var:preset|color|accent-2'}}}}))
wjson('styles/kraft.json', variation('Kraft', [
    ('base', '#D9C4A3', 'Kraft'), ('contrast', '#1A1A1A', 'Black'), ('accent', '#003E66', 'Deep blue'), ('accent-2', '#FF48B0', 'Fluorescent pink'),
    ('surface', '#CDB691', 'Dark kraft'), ('line', '#1A1A1A', 'Rule'), ('muted', '#3B3226', 'Brown')] + REST))
wjson('styles/mint.json', variation('Mint', [
    ('base', '#FFFFFF', 'Paper'), ('contrast', '#1A1A1A', 'Black'), ('accent', '#006A66', 'Teal'), ('accent-2', '#82D8D5', 'Mint'),
    ('surface', '#E6F7F6', 'Mint tint'), ('line', '#1A1A1A', 'Rule'), ('muted', '#4D4D4D', 'Grey')] + REST))


def section(slug, title, blocks, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                             'title': title, 'slug': slug, 'blockTypes': blocks, 'styles': styles})

def boxed(bg='base', fg='contrast', shadow='hard'):
    return {'color': {'background': 'var:preset|color|' + bg, 'text': 'var:preset|color|' + fg},
            'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'},
            'shadow': 'var:preset|shadow|' + shadow,
            'spacing': {'padding': {'top': sp(40), 'bottom': sp(40), 'left': sp(40), 'right': sp(40)}}}

section('box', 'Box (border and hard shadow)', ['core/group', 'core/columns', 'core/column'], boxed())
section('box-pink', 'Pink box', ['core/group', 'core/columns', 'core/column'], boxed('accent-2'))
section('box-yellow', 'Yellow box', ['core/group', 'core/columns', 'core/column'], boxed('ink-yellow'))
section('box-blue', 'Blue box', ['core/group', 'core/columns', 'core/column'], {**boxed('accent', 'base'),
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}}}})
section('box-mint', 'Mint box', ['core/group', 'core/columns', 'core/column'], boxed('ink-mint'))
section('ruled', 'Ruled columns (visible dividers)', ['core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}},
    'spacing': {'padding': {'top': sp(40), 'bottom': sp(40)}}})
section('bar', 'Bar (thick rule below)', ['core/group'], {
    'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}}})
section('swatch', 'Ink swatch', ['core/group'], {
    'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}, 'shadow': 'var:preset|shadow|hard-sm',
    'spacing': {'padding': {'top': sp(30), 'bottom': sp(30), 'left': sp(30), 'right': sp(30)}},
    'css': '&{aspect-ratio:1;display:flex;flex-direction:column;justify-content:space-between}'})
section('overprint', 'Overprint (stacked ink layers)', ['core/group'], {
    'border': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}, 'shadow': 'var:preset|shadow|hard-lg',
    'color': {'background': 'var:preset|color|base'},
    'css': '&{display:grid!important;padding:var(--wp--preset--spacing--40)}& > *{grid-area:1/1;margin:0!important}& img{mix-blend-mode:multiply;border:0!important;display:block}& > *:last-child{transform:translate(5px,4px)}'})
section('sticker', 'Sticker label', ['core/paragraph'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
    'border': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'},
    'typography': {'fontWeight': '800', 'fontSize': 'var:preset|font-size|small'},
    'spacing': {'padding': {'top': '0.2em', 'bottom': '0.2em', 'left': '0.5em', 'right': '0.5em'}},
    'css': '&{display:inline-block;transform:rotate(-2deg)}'})

write('style.css', '''/*
Theme Name: Drum
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A loud, boxy site for risograph studios and print co-ops that print for clients, publish their inks and papers, run workshops and sell stationery.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: drum
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

# ------------------------------------------------------------------ parts
write('parts/header.html', group(row(J(
    group(dyn('site-title', level=0), className='is-style-box-pink', style={'spacing': {'padding': {'top': sp(10), 'bottom': sp(10), 'left': sp(30), 'right': sp(30)}}}, layout={'type': 'default'}),
    row(dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}, style={'spacing': {'blockGap': sp(30)}}), justify='right')),
    justify='space-between', align='full'), align='full', className='is-style-bar', layout={'type': 'default'}, style=pad(30, 30, 40, 40)))

write('parts/footer.html', group(J(
    columns(
        (None, J(heading('Two Drums Press', 3), para('A riso studio and workers\' co-op of four, in a railway arch in Ancoats since 2016.'))),
        (None, J(heading('Arch 7', 6), para('Arch 7, Pollard Street East<br>Manchester M40 7FS<br>Tuesday to Friday, 10am to 6pm<br>Saturday 11am to 4pm'))),
        (None, J(heading('Get in touch', 6), para('<a href="mailto:print@example.com">print@example.com</a><br>0161 496 0381<br><a href="/print-with-us/">Ask for a quote</a><br><a href="/questions/">Questions people ask</a><br><a href="/print-club/">Print club</a>'))),
        align='wide', className='is-style-ruled'),
    para('Demo images are public domain and CC0 from Wikimedia Commons, including 1930s WPA screenprint posters, standing in for our own prints.', fontSize='x-small', align='wide')),
    tag='footer', align='full', className='is-style-box-yellow', style={'spacing': {'padding': {'top': sp(60), 'bottom': sp(50)}}}))

# ------------------------------------------------------------------ patterns
def box(inner, style='box', **kw):
    return group(inner, className='is-style-' + style, **kw)

pattern('hero-lead-time', 'Hero: what we print and the current lead time', 'featured', columns(
    ('62%', J(heading('We print zines, posters and art editions on two Riso drums in Ancoats', 1),
              para('Two to five colours, 50 to 5,000 copies, on recycled paper. Send your files, get a proof the same day, collect or get it posted.', fontSize='large'),
              buttons(('Get a quote', '/print-with-us/'), ('See the inks', '/inks/')))),
    (None, J(box(J(heading('Lead time this week', 3, fontSize='large'),
                   para('Files in by <strong>Wednesday 12:00</strong>, collect <strong>Friday after 2pm</strong>. Bigger runs, allow a week.')), 'box-yellow'),
             box(J(heading('Closed 21 Dec to 4 Jan', 3, fontSize='large'), para('Last files for Christmas: Friday 11 December.')), 'box-pink'))),
    align='wide', className='is-style-ruled', style={'spacing': {'blockGap': {'left': sp(50), 'top': sp(40)}}}))

pattern('overprint-proof', 'Overprint proof (signature)', 'featured,gallery', columns(
    ('45%', group(J(image('poster-john.jpg', 'Poster of a woman helping a boy read, printed here as a layer in blue ink', lightbox=False, style={'color': {'duotone': 'var:preset|duotone|blue-ink'}}),
                    image('screen.jpg', 'Hands pulling a squeegee across a screen, printed here as a layer in fluorescent pink', lightbox=False, style={'color': {'duotone': 'var:preset|duotone|pink-ink'}})),
                  className='is-style-overprint', layout={'type': 'default'})),
    (None, J(heading('See two inks before you print', 2),
             para('Riso inks are see-through. Where pink sits on blue you get a deep violet, and every layer lands a hair off the one before. That wobble is the point.', fontSize='large'),
             lst(['Send each colour as its own greyscale file, 100% black where you want full ink.',
                  'Tell us which ink goes on which layer and the paper you want.',
                  'We run a proof on the real machine and email a photo within a working day. Proofs are free on jobs over £60.']),
             para('Two layers, blue and fluorescent pink, overprinted', className='is-style-sticker'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(70), 'top': sp(50)}}}),
    description='Signature: two images tinted with the blue and pink ink duotones and stacked with multiply blending, a hand-made overprint preview. Swap the images for your own layers.')

SERVICES = [('Zines and booklets', 'Stapled or perfect-bound, A6 to A4, 8 to 64 pages', 'from £95 for 100', 'box-pink'),
            ('Posters', 'A3 and A2, up to five colours', 'from £60 for 50'),
            ('Art editions', 'Signed runs for artists, archival paper, numbered sheets', 'quoted'),
            ('Stationery', 'Business cards, notebooks, postcards, wedding bits', 'from £40')]
pattern('services-list', 'Services with one leading item', 'services', J(
    heading('What we print', 2),
    box(columns(('60%', J(heading(SERVICES[0][0], 3, fontSize='xx-large'), para(SERVICES[0][1], fontSize='large'))),
                (None, J(para(SERVICES[0][2], fontSize='x-large', fontFamily='display', style={'typography': {'fontWeight': '800'}}),
                         para('Half our work is zines. We keep 12 standard sizes of paper cut and ready.')))), 'box-pink'),
    group(J(*[box(J(heading(n, 3, fontSize='large'), para(w), para(pr, fontSize='large', style={'typography': {'fontWeight': '800'}})), st)
              for (n, w, pr), st in zip([x[:3] for x in SERVICES[1:]], ['box', 'box-mint', 'box-yellow'])]),
          layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '15rem'}, style={'spacing': {'blockGap': sp(40)}})))

pattern('ink-chart', 'Ink colour chart', 'featured,text', J(
    heading('Our inks', 2),
    para('Nine drums, all soy-based. Colours on screen are close, not exact. Order the swatch card if it matters.', fontSize='large'),
    group(J(*[group(J(heading(n, 3, fontSize='large'), para(x, fontSize='small')), backgroundColor=s, textColor=t, className='is-style-swatch') for s, c, n, t, x in INKS]),
          layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'}, style={'spacing': {'blockGap': sp(30)}})),
    description='The ink list as square swatches. Each swatch uses a palette colour, so a style variation can re-ink the chart.')

PAPERS = [['Munken Print Cream', '90gsm', 'Cream', 'Yes', 'Our default for zines'],
          ['Munken Pure', '120gsm', 'White', 'Yes', 'Posters, flyers'],
          ['Cyclus Offset', '100gsm', 'Grey-white', '100% recycled', 'Takes blue beautifully'],
          ['Gmund Colors Matt', '300gsm', 'Six colours', 'No', 'Covers and postcards, +£10'],
          ['Kraft card', '280gsm', 'Brown', '100% recycled', 'Only dark inks show']]
pattern('paper-library', 'Paper library', 'text', J(
    heading('Paper we keep in stock', 2),
    table(PAPERS, head=['Paper', 'Weight', 'Colour', 'Recycled', 'Good for']),
    para('Anything heavier than 300gsm jams the drum. Bring your own paper and we\'ll test a sheet first, free.', fontSize='small')))

pattern('file-setup', 'File setup guide', 'text', box(J(
    heading('Setting up your files', 3),
    lst(['One file per ink, in greyscale. Black means full ink, 50% grey means 50% ink.',
         'Name each file with the ink colour: <em>zine-cover-blue.pdf</em>, <em>zine-cover-pink.pdf</em>.',
         '3mm bleed on every side. Keep text 5mm from the edge.',
         'Fine lines under 0.3pt disappear. Text under 7pt fills in.',
         'Riso shifts up to 2mm between layers. Don\'t design tight butt registration.'], ordered=True),
    buttons(('Download templates and swatch file', 'mailto:print@example.com?subject=Templates%20please'))), 'box'))

pattern('lead-times', 'Lead times note', 'text', box(J(
    heading('Lead times', 3, fontSize='large'),
    lst(['<strong>3 working days</strong> for up to 500 copies in 2 colours', '<strong>5 working days</strong> for up to 2,000 copies',
         '<strong>Add 2 days</strong> for zines with binding', '<strong>2 weeks</strong> for art editions, proofs first']),
    para('Files in by Wednesday 12:00 for Friday collection. We don\'t do same-day unless we owe you one.')), 'box-mint'))

pattern('quote-request', 'Quote request (what to send)', 'call-to-action', columns(
    (None, J(heading('Get a quote', 2),
             para('No form, just email. We reply within one working day with a price and a date.', fontSize='large'),
             buttons(('Email print@example.com', 'mailto:print@example.com?subject=Quote')))),
    (None, box(J(heading('Put this in the email', 4),
                 lst(['How many copies', 'Size, and pages if it\'s a zine', 'Which inks, or how many colours', 'Which paper, or "you choose"', 'When you need it'])), 'box-yellow')),
    align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('price-note', 'Price calculator note', 'services', para(
    'Rough maths: £30 set-up per colour, then about 4p per sheet per colour. 200 A5 flyers in two colours on 100gsm is about £85. The quote is the real number.',
    fontSize='large', className='is-style-sticker'))

pattern('coop-values', 'Co-op statement and recycled paper', 'about', box(columns(
    (None, J(heading('A workers\' co-op', 3), para('Four of us own the studio and earn the same hourly rate: Aisha, Lewis, Dorota and Ben. We vote on jobs we\'re unsure about, and we turn down anything for gambling or the arms trade.'))),
    (None, J(heading('Recycled paper only', 3), para('Every stock we keep is recycled or FSC certified. Soy inks, and the masters go to a composter in Salford.'))),
    className='is-style-ruled'), 'box-blue', align='wide'))

WORKSHOPS = [['Sat 17 October', 'Two-colour zine in a day', '10am to 4pm', '£75, 8 places'],
             ['Thu 29 October', 'Riso basics (evening)', '6pm to 9pm', '£45, 10 places'],
             ['Sat 14 November', 'Christmas cards', '11am to 3pm', '£55, 8 places'],
             ['Sat 5 December', 'Print your own calendar', '10am to 4pm', '£75, 8 places']]
pattern('workshop-dates', 'Workshop dates', 'featured', J(
    heading('Workshops', 2),
    table(WORKSHOPS, head=['Date', 'Workshop', 'Time', 'Price and places']),
    para('All materials included. Book by email, pay by bank transfer. If a workshop is full, we keep a waiting list.', fontSize='small')))

pattern('print-club', 'Print club membership', 'call-to-action', box(J(
    heading('Print club', 3),
    para('£30 for three months. You get one riso print by a Manchester artist posted every month, 15% off in the shop, and first dibs on workshops. Back issues are in the shop while they last.', fontSize='large'),
    buttons(('Join the print club', '/shop/'))), 'box-pink'))

pattern('shop-categories', 'Shop categories', 'shop', J(
    heading('The shop', 2),
    columns(
        (None, box(J(image('zine-rack.jpg', 'A library wall rack full of colourful zines under a paper banner reading zines', href='/shop/'), heading('<a href="/shop/">Zines and books</a>', 3, fontSize='large')), 'box')),
        (None, box(J(image('prints-table.jpg', 'Pink, blue and green relief prints laid out on a round table', href='/shop/'), heading('<a href="/shop/">Prints and posters</a>', 3, fontSize='large')), 'box-mint')),
        (None, box(J(image('inks-bench.jpg', 'A print bench with red and blue ink tubes, a roller and fresh prints', href='/shop/'), heading('<a href="/shop/">Swatch cards and paper packs</a>', 3, fontSize='large')), 'box-yellow')),
        align='wide', style={'spacing': {'blockGap': {'left': sp(40), 'top': sp(40)}}})))

pattern('swatch-cards', 'Ink swatch cards and paper samples', 'shop', box(J(
    heading('Not sure about a colour?', 3),
    para('The swatch card has every ink at 100%, 70%, 40% and 10%, and every pair overprinted. £12, posted flat. The paper pack has a sheet of each stock, £6.'),
    buttons(('Buy a swatch card', '/shop/'))), 'box-yellow'))

pattern('stockists', 'Stockists', 'about', J(
    heading('Where our stuff is sold', 3),
    lst(['<strong>Plinth Books</strong>, Oldham Street, Manchester', '<strong>Paper &amp; Cup</strong>, Ancoats, Manchester',
         '<strong>Kirkgate Paper Co.</strong>, Leeds', '<strong>Bold Street Zines</strong>, Liverpool'])))

pattern('holiday-notice', 'Holiday closure notice', 'banner', group(
    para('Closed 21 December to 4 January. Last files for Christmas: Friday 11 December. Take this bar down on 5 January.', fontSize='large', style={'typography': {'fontWeight': '800'}}),
    className='is-style-box-pink', align='full'), description='A loud closure notice. Remove it when you reopen.')

pattern('process-strip', 'From file to print', 'gallery', J(
    heading('What happens to your file', 2),
    columns(
        (None, J(image('duplicator.jpg', 'Black-and-white photo of a man feeding paper into a stencil duplicator'), para('<strong>1. Master.</strong> Each colour is burned into a master sheet and wrapped round its drum.'))),
        (None, J(image('drum-machine.jpg', 'An old drum duplicator on a wooden table with trays of paper'), para('<strong>2. Drum.</strong> Paper goes through once per colour. We change drums between layers.'))),
        (None, J(image('prints-table.jpg', 'Pink, blue and green relief prints laid out on a round table'), para('<strong>3. Dry and trim.</strong> Riso ink dries slowly. We rack sheets overnight before trimming.'))),
        align='wide', className='is-style-ruled')))

pattern('job-card-list', 'Recent jobs (query)', 'posts,query', J(
    row(J(heading('Recent jobs', 2), para('<a href="/jobs/">All jobs</a>', fontSize='large')), justify='space-between', align='wide'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-terms', term='post_tag')),
          per_page=3, layout={'type': 'grid', 'columnCount': 3}, align='wide')))

pattern('job-archive', 'Jobs archive (inherits the page query)', 'posts,query', inherit_query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-terms', term='post_tag')),
    layout={'type': 'grid', 'columnCount': 3}, align='wide'), inserter=False)

pattern('job-specs', 'Job specs', 'text', table([['Client', 'Hulme Community Garden Centre'], ['Run', '300 copies, 24 pages, A5'], ['Inks', 'Blue and fluorescent pink'], ['Paper', 'Munken Print Cream 90gsm, Gmund cover'], ['Turnaround', '4 working days']]))

pattern('customer-quote', 'Customer quote', 'testimonials', quote(
    'They told us our blue was too light for the text before we printed 500. Saved the whole run.',
    'Kemi, editor of Salt Water zine, March 2026'))

# page layouts
pattern('print-page', 'Page: print with us', 'services', J(
    pattern_ref('services-list'), spacer(), pattern_ref('example-jobs'), spacer(), pattern_ref('overprint-proof'), spacer(), pattern_ref('quote-request'), pattern_ref('price-note'),
    columns((None, pattern_ref('file-setup')), (None, pattern_ref('lead-times')), align='wide', style={'spacing': {'blockGap': {'left': sp(50)}}}),
    pattern_ref('private-workshop'), pattern_ref('coop-values'), pattern_ref('customer-quote')), block_types='core/post-content')
pattern('inks-page', 'Page: inks', 'text', J(pattern_ref('ink-chart'), spacer(), pattern_ref('ink-of-the-month'), spacer(), pattern_ref('swatch-cards')), block_types='core/post-content')
pattern('paper-page', 'Page: paper library', 'text', J(pattern_ref('paper-samples'), spacer(), pattern_ref('paper-library'), spacer(), pattern_ref('file-setup')), block_types='core/post-content')
pattern('workshops-page', 'Page: workshops', 'featured', J(pattern_ref('workshop-card'), spacer(), pattern_ref('workshop-dates'), spacer(), pattern_ref('private-workshop'), pattern_ref('process-strip')), block_types='core/post-content')


# ------------------------------------------------------------------ round 2: more of the kit
pattern('hero-next-run', 'Hero: next shared print run', 'featured', columns(
    ('50%', image('poster-canyon.jpg', 'Screenprinted poster of a canyon in pink, purple and brown layers', 'Four-ink poster, reprinted in March for a walking group talk')),
    (None, box(J(para('Next shared run', className='is-style-sticker'),
                 heading('Postcards and A5 flyers, Friday 16 October', 1, fontSize='xx-large'),
                 para('Get your artwork onto a shared sheet with four other people and split the set-up cost. Blue and pink only. Files in by Monday 12 October.', fontSize='large'),
                 buttons(('Book a slot on the sheet', 'mailto:print@example.com?subject=Shared%20run'))), 'box-yellow')),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(50), 'top': sp(40)}}}),
    description='Alternative opener: the next shared run, with a date and one action.')

pattern('service-tiles', 'Service tiles (four coloured links)', 'services', group(J(*[
    box(J(heading('<a href="%s">%s</a>' % (u, t), 3, fontSize='large'), para(d)), st) for t, u, d, st in [
        ('Print with us', '/print-with-us/', 'Zines, posters, editions. Quotes in a working day.', 'box-pink'),
        ('Workshops', '/workshops/', 'Evenings and Saturdays, eight people at a time.', 'box-yellow'),
        ('Inks and paper', '/inks/', 'Nine drums and five papers, all listed.', 'box-mint'),
        ('The shop', '/shop/', 'Swatch cards, notebooks and the print club.', 'box-blue')]]),
    layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}, align='wide', style={'spacing': {'blockGap': sp(40)}}))

pattern('example-jobs', 'Example jobs with prices', 'services', J(
    heading('What things cost', 2),
    group(J(*[box(J(para(t, className='is-style-sticker'), heading(price, 3, fontSize='x-large'), para(d)), st) for t, price, d, st in [
        ('Zine', '£168', '100 copies, 24 pages A5, two inks, stapled, cream paper.', 'box'),
        ('Posters', '£74', '50 copies A3, three inks on Munken Pure 120gsm.', 'box-pink'),
        ('Flyers', '£85', '200 copies A5, two inks, both sides, 100gsm.', 'box'),
        ('Cards', '£48', '100 business cards on Gmund 300gsm, one ink.', 'box-mint')]]),
        layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}, style={'spacing': {'blockGap': sp(40)}}),
    para('Prices include VAT and collection from the arch. Posting is at cost.', fontSize='small')))

pattern('coverage-warning', 'Heavy ink coverage warning', 'text', columns(
    ('45%', image('inks-bench.jpg', 'A print bench with red and blue ink tubes, a roller and fresh prints', 'Pink fingers after 300 covers')),
    (None, J(heading('Go easy on solid colour', 3),
             para('Riso ink is soy-based and never fully dries on uncoated paper. Big solid areas cause:'),
             lst(['sheets sticking to the rollers and jamming', 'ink rubbing off onto the back of the next sheet', 'roller marks across flat colour', 'inky fingers for whoever reads it']),
             para('Keep solids under about 70% of the page, or use a tint. We will tell you before we print if a file looks risky.'))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('registration-note', 'Registration explained', 'text', box(J(
    heading('Why the layers wobble', 3),
    para('Each ink goes through the machine separately and paper stretches a little when it is wet. Layers can land up to 2mm apart in any direction. Design with overlaps and chunky borders, and you will like the result. Tight butt registration will look wrong.'),
    para('Two layers, 2mm out, on purpose', className='is-style-sticker')), 'box-mint'))

pattern('faq', 'Questions people ask', 'text', J(
    heading('Questions people ask', 2),
    details('Can you match a Pantone colour?', para('No. We have nine inks and they are what they are. The swatch card shows every tint and overprint so you can pick.')),
    details('Do you print full-colour photos?', para('Not well. Riso does two to five flat inks. For photos, go to a digital printer; we can recommend two in Manchester.')),
    details('Can I come and watch my job?', para('Yes, on Thursdays. Bring a coffee for whoever is on the drum.')),
    details('Do you post?', para('Yes, Royal Mail tracked, at cost. Most zine orders under 2kg are £4.20.')),
    details('What is the smallest run?', para('Twenty copies. Below that the set-up cost makes it silly, and a photocopier is cheaper.'))))

pattern('team', 'The co-op members', 'about', J(
    heading('Who runs the drums', 2),
    group(J(*[box(J(heading(n, 3, fontSize='large'), para(r)), st) for n, r, st in [
        ('Aisha', 'Quotes, colour advice and the blue drum. Started the studio in 2016.', 'box-pink'),
        ('Lewis', 'Binding, trimming, the guillotine and every zine fair in the north.', 'box'),
        ('Dorota', 'Workshops and the print club. Draws most of the club prints herself.', 'box-yellow'),
        ('Ben', 'Accounts, repairs, and knows which drum is about to leak.', 'box-mint')]]),
        layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}, style={'spacing': {'blockGap': sp(40)}})))

pattern('find-us', 'Find the arch (address and hours)', 'contact', columns(
    (None, J(heading('Find us', 2),
             para('Arch 7, Pollard Street East, Manchester M40 7FS. Under the railway, the arch with the pink door. Ten minutes on foot from Piccadilly, or the 216 bus to Pollard Street.', fontSize='large'))),
    (None, box(J(heading('Opening hours', 3, fontSize='large'),
                 lst(['Tuesday to Friday, 10am to 6pm', 'Saturday, 11am to 4pm', 'Sunday and Monday closed']),
                 para('Collections until 5.45pm. Ring the bell twice, the drums are loud.')), 'box-yellow')),
    align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('contact-block', 'Contact details', 'contact', group(J(
    heading('Get in touch', 2),
    columns((None, J(heading('Quotes and jobs', 4), para('<a href="mailto:print@example.com">print@example.com</a><br>Replies within one working day.'))),
            (None, J(heading('Workshops', 4), para('<a href="mailto:workshops@example.com">workshops@example.com</a><br>Dorota answers on Tuesdays and Fridays.'))),
            (None, J(heading('Phone', 4), para('0161 496 0381<br>Tuesday to Saturday, while we are open.'))),
            className='is-style-ruled')), align='wide', layout={'type': 'default'}))

pattern('newsletter', 'Newsletter sign-up', 'call-to-action', box(columns(
    (None, J(heading('One email a month', 3), para('New inks, workshop dates and the next shared run. Sent on the first Tuesday, never more.'))),
    (None, buttons(('Sign up by email', 'mailto:print@example.com?subject=Newsletter'))), verticalAlignment='center'), 'box-pink', align='wide'))

pattern('gift-voucher', 'Gift vouchers', 'shop', box(J(
    heading('Gift vouchers', 3),
    para('£25, £50 or £75, for workshops, print jobs or the shop. Valid for a year. We post a riso-printed card, or email a PDF the same day.'),
    buttons(('Buy a voucher', '/shop/'))), 'box-mint'))

pattern('featured-zine', 'Featured zine', 'shop', columns(
    ('40%', image('zine-rack.jpg', 'A library wall rack full of colourful zines under a paper banner reading zines')),
    (None, J(para('Zine of the month', className='is-style-sticker'),
             heading('Salt Water, issue 7', 3, fontSize='x-large'),
             para('Thirty-two pages of swimming stories from the Irish Sea, printed in blue and fluorescent pink on cream paper. Edition of 500.'),
             para('£6', fontSize='x-large', style={'typography': {'fontWeight': '800'}}),
             buttons(('See it in the shop', '/shop/')))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('ink-of-the-month', 'Ink of the month', 'featured', box(columns(
    ('35%', group(J(heading('Mint', 3, fontSize='xx-large'), para('Drum 8')), backgroundColor='ink-mint', textColor='contrast', className='is-style-swatch')),
    (None, J(heading('Ink of the month: mint', 3), para('Soft on its own, lovely under blue. All jobs using mint in October get the drum change free, which saves £15.'),
             buttons(('Ask for a mint quote', 'mailto:print@example.com?subject=Mint')))),
    verticalAlignment='center'), 'box', align='wide'))

pattern('paper-samples', 'Paper sample cards', 'text', J(
    heading('Papers, side by side', 2),
    group(J(*[box(J(heading(n, 3, fontSize='large'), para(w, style={'typography': {'fontWeight': '800'}}), para(d)), st) for n, w, d, st in [
        ('Munken Print Cream', '90gsm, recycled', 'Our zine default. Warm, soft, blue looks deep on it.', 'box'),
        ('Cyclus Offset', '100gsm, 100% recycled', 'Grey-white with flecks. Pink glows.', 'box'),
        ('Gmund Colors', '300gsm, six colours', 'Covers and cards. Dark colours only take light inks.', 'box-yellow'),
        ('Kraft card', '280gsm, recycled', 'Brown board. Only black, blue and purple show well.', 'box')]]),
        layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}, style={'spacing': {'blockGap': sp(40)}})))

pattern('file-checklist', 'File checklist before sending', 'text', J(
    heading('Before you send', 3),
    lst(['One greyscale PDF per ink, named by colour.', '3mm bleed on all sides.', 'Text at 7pt or bigger.', 'No solid areas over 70%.', 'A flattened colour mock-up as a JPEG, so we can see what you mean.'])))

pattern('workshop-card', 'Workshop detail', 'featured', columns(
    ('45%', image('prints-table.jpg', 'Pink, blue and green relief prints laid out on a round table', 'Last month: 8 people, 64 prints')),
    (None, J(para('Saturday 17 October, 10am to 4pm', className='is-style-sticker'),
             heading('Two-colour zine in a day', 3, fontSize='x-large'),
             para('Draw two layers in the morning, print 30 copies of an 8-page zine in the afternoon, fold and staple before tea. No drawing skills needed, just opinions.'),
             lst(['£75, all materials and lunch included', '8 places, 3 left', 'Suitable from age 14']),
             buttons(('Book a place', 'mailto:workshops@example.com?subject=Zine%20in%20a%20day')))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('private-workshop', 'Private and school workshops', 'services', box(J(
    heading('Groups, schools and teams', 3),
    para('We run workshops at your school or office for up to 15 people. £450 for a half day, plus travel outside Greater Manchester. Everyone leaves with a printed zine.'),
    buttons(('Ask about a group workshop', 'mailto:workshops@example.com?subject=Group%20workshop'))), 'box-blue'))

pattern('club-back-issues', 'Print club back issues', 'shop', J(
    heading('Print club back issues', 3),
    gallery([('poster-john.jpg', 'Poster of a woman helping a boy read', 'September: Reading room'),
             ('poster-canyon.jpg', 'Canyon poster in pink and purple layers', 'August: Canyon'),
             ('screen.jpg', 'Squeegee on a pink screen', 'July: Pull'),
             ('prints-table.jpg', 'Colourful prints on a table', 'June: Table')], columns=4, align='wide'),
    para('Back issues are £12 each in the shop while they last.', fontSize='small')))

pattern('print-gallery', 'Print gallery (lightbox)', 'gallery', gallery([
    ('poster-john.jpg', 'Poster of a woman helping a boy read, in red, black and cream', 'Reading room poster, three inks'),
    ('poster-canyon.jpg', 'Canyon poster in pink, purple and brown', 'Canyon, four inks'),
    ('prints-table.jpg', 'Pink, blue and green prints on a round table', 'Workshop prints'),
    ('screen.jpg', 'Hands pulling a squeegee across a pink screen', 'Pull night flyer')], columns=2, align='wide'))

pattern('job-story', 'Job write-up (what, how, what went wrong)', 'posts', J(
    para('Three hundred copies of a 24-page garden zine for the Hulme Community Garden Centre, printed in blue and pink on cream paper.', fontSize='large'),
    columns((None, J(heading('The brief', 4), para('Planting guides and recipes from the volunteers, cheap enough to give away at the gate.'))),
            (None, J(heading('What we did', 4), para('Blue for text and drawings, pink for tints under the seed packets. Stapled by hand on a Thursday.'))),
            (None, J(heading('What went wrong', 4), para('The pink was set too dark on page 9 and filled in the lettuce. We reprinted that sheet.'))),
            className='is-style-ruled')))

pattern('quote-row', 'Two customer quotes', 'testimonials', columns(
    (None, quote('Aisha talked me out of five colours and into two. It looks better and cost half.', 'Priya, illustrator, first zine, June 2026')),
    (None, quote('We ordered the seed packets on Tuesday and planted them on Saturday.', 'Tom, Hulme Community Garden Centre, April 2026')),
    align='wide', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('closed-sign', 'Studio closed today', 'banner', group(
    para('Studio closed today for a drum repair. Collections move to tomorrow, 10am. Take this bar down tomorrow.', fontSize='large', style={'typography': {'fontWeight': '800'}}),
    className='is-style-box-yellow', align='full'), description='A same-day closure notice.')

# more page layouts
pattern('about-page', 'Page: about the co-op', 'about', J(
    pattern_ref('coop-values'), spacer(), pattern_ref('team'), spacer(), pattern_ref('stockists'), pattern_ref('quote-row')), block_types='core/post-content')
pattern('contact-page', 'Page: contact', 'contact', J(
    pattern_ref('contact-block'), spacer(), pattern_ref('find-us'), spacer(), pattern_ref('newsletter')), block_types='core/post-content')
pattern('faq-page', 'Page: questions', 'text', J(
    pattern_ref('faq'), spacer(), pattern_ref('coverage-warning'), pattern_ref('registration-note'), pattern_ref('file-checklist')), block_types='core/post-content')
pattern('club-page', 'Page: print club', 'shop', J(
    pattern_ref('print-club'), spacer(), pattern_ref('club-back-issues'), pattern_ref('gift-voucher')), block_types='core/post-content')

# ------------------------------------------------------------------ templates
mp = {'spacing': {'padding': {'top': sp(60), 'bottom': sp(70)}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero-lead-time'), spacer('var:preset|spacing|70'), pattern_ref('overprint-proof'), spacer('var:preset|spacing|70'),
    pattern_ref('service-tiles'), spacer('var:preset|spacing|70'), pattern_ref('ink-chart'), spacer('var:preset|spacing|70'),
    pattern_ref('featured-zine'), spacer('var:preset|spacing|70'), pattern_ref('job-card-list'), spacer('var:preset|spacing|70'),
    pattern_ref('quote-row'), spacer('var:preset|spacing|60'), pattern_ref('newsletter')),
    style=mp))
write('templates/home.html', page_template(J(heading('Recent jobs', 1, align='wide'), para('Things we printed for other people, with the inks and paper we used.', align='wide', fontSize='large'),
                                             pattern_ref('job-archive')), style=mp))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('job-archive')), style=mp))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('job-archive')), style=mp))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide', fontSize='xx-large'),
                                               dyn('search', label='Search', showLabel=False, placeholder='Zines, posters, blue', buttonText='Search', align='wide'), pattern_ref('job-archive')), style=mp))
write('templates/404.html', page_template(J(
    heading('Misprint', 1),
    para('This page didn\'t come out of the drum. Try the <a href="/print-with-us/">print services</a> or the <a href="/shop/">shop</a>.', fontSize='large'),
    dyn('search', label='Search', showLabel=False, placeholder='Zines, posters, blue', buttonText='Search')), style=mp))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), style=mp))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide', fontSize='xx-large'),
                                                   dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})), style=mp))
single = J(columns(('55%', dyn('post-featured-image')),
                   (None, J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-terms', term='post_tag'), dyn('post-content', layout={'type': 'default'}))),
                   align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}),
           row(J(dyn('post-navigation-link', type='previous', label='Older job', showTitle=True), dyn('post-navigation-link', label='Newer job', showTitle=True)),
               justify='space-between', align='wide', className='is-style-bar'))
write('templates/single.html', page_template(single, style=mp))
write('templates/single-job.html', page_template(single, style=mp))

# ------------------------------------------------------------------ demo
JOBS = [
    ('Salt Water zine, issue 6', 'poster-john.jpg', ['Zine', 'Blue', 'Pink'], 'Salt Water zine collective', '500 copies, 32 pages, A5', 'Blue and fluorescent pink', 'Munken Print Cream 90gsm'),
    ('Hulme garden centre seed packets', 'prints-table.jpg', ['Stationery', 'Green'], 'Hulme Community Garden Centre', '2,000 packets, die-cut', 'Green and black', 'Cyclus Offset 100gsm'),
    ('Canyon poster reprint for a talk', 'poster-canyon.jpg', ['Poster', 'Four colours'], 'Levenshulme Walking Group', '150 copies, A2', 'Blue, pink, yellow and black', 'Munken Pure 120gsm'),
    ('Pull-a-print night flyers', 'screen.jpg', ['Flyer', 'Pink'], 'The Pint Pot, Ancoats', '400 copies, A6', 'Fluorescent pink and black', 'Kraft card 280gsm'),
    ('Zine library signage', 'zine-rack.jpg', ['Signage', 'Yellow'], 'Central Library zine corner', '20 signs, A3', 'Yellow and blue', 'Gmund Colors Matt 300gsm'),
    ('Lino club edition', 'inks-bench.jpg', ['Art edition', 'Red'], 'Tuesday lino club', '60 sheets, numbered', 'Bright red and blue', 'Munken Pure 120gsm'),
]
JOB_NOTES = [
    ('Issue 6 of a swimming zine, 32 pages, for sale at two fairs.', 'Blue for all text and drawings, pink for the sea tints. Stapled and trimmed in a day.', 'Nothing much. One box got rained on outside Victoria station.', 'A riso-printed poster of a woman helping a boy read, in red and black'),
    ('Seed packets for a garden centre giveaway, 2,000 of them, cut to shape.', 'Green and black on recycled offset, die-cut by a friend with a platen in Stockport.', 'The die was 1mm too big. Lewis hand-trimmed 300 of them.', 'Pink, blue and green prints laid out on a round table'),
    ('A reprint of an old travel poster for a talk about the canyon.', 'Four layers separated by hand from a scan: blue, pink, yellow, black.', 'Yellow under pink went orange. We liked it and kept it.', 'A four-colour canyon poster in pink, purple and brown'),
    ('Flyers for a monthly print night at a pub round the corner.', 'Fluorescent pink and black on brown kraft card, so the pink really glows.', 'Kraft jams if you rush it. We printed at half speed.', 'Hands pulling a squeegee across a pink screen at a print night'),
    ('Signs for the zine corner of the Central Library.', 'Yellow and blue on thick Gmund, big letters, readable from the door.', 'The first proof was too pale in yellow. Second pass on a heavier tint fixed it.', 'A wall rack of colourful zines under a paper zines banner'),
    ('A numbered edition for the Tuesday lino club, cut on lino and re-drawn for riso.', 'Bright red and blue, numbered in pencil, 60 sheets.', 'Two sheets misfed on the blue pass. The club took them as seconds.', 'A bench with red and blue ink tubes and fresh prints'),
]
posts = [{'title': t, 'category': 'jobs', 'tags': tags, 'image': img, 'template': 'single-job',
          'content': J(para('Printed for %s: %s, in %s on %s.' % (who, run.lower() if run[0].isalpha() and not run[0].isupper() else run, inks.lower(), paper), fontSize='large'),
                       columns((None, J(heading('The brief', 4), para(brief))), (None, J(heading('What we did', 4), para(did))), (None, J(heading('What went wrong', 4), para(wrong))), className='is-style-ruled'),
                       table([['Client', who], ['Run', run], ['Inks', inks], ['Paper', paper]]),
                       image(img, alt, 'The finished job'))}
         for (t, img, tags, who, run, inks, paper), (brief, did, wrong, alt) in zip(JOBS, JOB_NOTES)]
products = [
    {'name': 'Ink swatch card', 'price': '12', 'image': 'inks-bench.jpg', 'category': 'Swatches and paper', 'sku': 'TD-SW1', 'stock': 40, 'short': 'Every ink at four tints and every pair overprinted. A5, posted flat.'},
    {'name': 'Paper sample pack', 'price': '6', 'image': 'prints-table.jpg', 'category': 'Swatches and paper', 'sku': 'TD-PP1', 'stock': 25, 'short': 'One sheet of each paper we stock, A5.'},
    {'name': 'Dot grid notebook, blue', 'price': '9', 'image': 'duplicator.jpg', 'category': 'Stationery', 'sku': 'TD-NB1', 'stock': 60, 'short': 'A5, 64 pages, riso-printed cover in blue on kraft.'},
    {'name': 'Postcard set, two inks', 'price': '8', 'image': 'screen.jpg', 'category': 'Stationery', 'sku': 'TD-PC1', 'stock': 30, 'short': 'Six postcards in pink and blue, 300gsm.'},
    {'name': 'Salt Water zine, issue 6', 'price': '6', 'image': 'poster-john.jpg', 'category': 'Zines', 'sku': 'TD-Z06', 'stock': 0, 'short': 'Sold out. Issue 7 is at the printer (us).'},
    {'name': 'Print club, three months', 'price': '30', 'image': 'zine-rack.jpg', 'category': 'Print club', 'sku': 'TD-CL3', 'stock': 50, 'short': 'One riso print a month for three months, posted, plus 15% off the shop.'},
]
demo = {
    'site': {'title': 'Two Drums Press', 'tagline': 'Riso printing co-op, Ancoats, Manchester'},
    'categories': [{'slug': 'jobs', 'name': 'Jobs', 'description': 'Things we printed for other people.'}],
    'front_page': 'home', 'posts_page': 'jobs',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'jobs', 'title': 'Jobs', 'content': ''},
        {'slug': 'print-with-us', 'title': 'Print with us', 'pattern': 'drum/print-page', 'template': 'page-wide'},
        {'slug': 'inks', 'title': 'Inks', 'pattern': 'drum/inks-page', 'template': 'page-wide'},
        {'slug': 'paper', 'title': 'Paper', 'pattern': 'drum/paper-page', 'template': 'page-wide'},
        {'slug': 'workshops', 'title': 'Workshops', 'pattern': 'drum/workshops-page', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About', 'pattern': 'drum/about-page', 'template': 'page-wide'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'drum/contact-page', 'template': 'page-wide'},
        {'slug': 'questions', 'title': 'Questions', 'pattern': 'drum/faq-page', 'template': 'page-wide'},
        {'slug': 'print-club', 'title': 'Print club', 'pattern': 'drum/club-page', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Print with us', 'url': '/print-with-us/'}, {'label': 'Inks', 'url': '/inks/'}, {'label': 'Paper', 'url': '/paper/'},
            {'label': 'Workshops', 'url': '/workshops/'}, {'label': 'Shop', 'url': '/shop/'}, {'label': 'Jobs', 'url': '/jobs/'},
            {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}],
    'currency': 'GBP',
    'products': products,
}
os.makedirs('demos/drum', exist_ok=True)
with open('demos/drum/content.json', 'w', encoding='utf-8') as f:
    json.dump(demo, f, indent=1, ensure_ascii=False)
write('functions.php', """<?php
/**
 * Drum: pattern categories only.
 *
 * @package drum
 */

add_action(
	'init',
	function () {
		foreach ( array(
""" + "\n".join("\t\t\t'%s' => '%s'," % (k, v) for k, v in CATS.items()) + """
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);""")
print('drum built')
