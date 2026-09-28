# Design note (shelf, idea 060, owner's brief: "penguin!!! or something more illustration-ish, style heavy. Branding of
#   Plato Rotterdam". Penguin is taken by spine, so this leans on Plato: a Rotterdam record-and-book shop look.)
# Direction: De Inktvis, an independent bookshop on the Nieuwe Binnenweg. Loud black-and-white with one signal red, a round
#   sticker logo like Plato's avatar, and old engravings run through a red duotone as the shop's house illustrations.
# Fonts: Luckiest Guy (display, hand-cut poster capitals), DM Sans (body). Two families, no monospace.
# Palette: white, ink #111111, signal red #D7261E, sticker yellow #FFD23F, newsprint #F3EEE4.
# Layout idea: staff picks as yellow shelf-talker cards, tilted a degree or two each way with a hard black offset shadow,
#   events set like a gig poster (huge dates), and every illustration in red-and-paper duotone so the site feels printed.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('shelf')
S = THEME['slug']
D = THEME['dir']
ROOT = os.path.abspath(os.path.join(D, '..', '..'))

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Luckiest Guy", "Arial Black", sans-serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"DM Sans", "Helvetica Neue", Arial, sans-serif'

PAL = [
    ('base', '#FFFFFF', 'Paper'),
    ('contrast', '#111111', 'Ink'),
    ('accent', '#D7261E', 'Signal red'),
    ('accent-2', '#FFD23F', 'Sticker yellow'),
    ('surface', '#F3EEE4', 'Newsprint'),
    ('line', '#111111', 'Rule'),
    ('muted', '#4A4A4A', 'Pencil'),
]
pal = lambda p: [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL),
                  'duotone': [{'slug': 'red-print', 'name': 'Red print', 'colors': ['#9E0F0A', '#FFF4E6']},
                              {'slug': 'ink-print', 'name': 'Ink print', 'colors': ['#111111', '#F3EEE4']}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Tiny', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '1.8rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.5rem', 'max': '4rem'}},
                {'slug': 'display', 'size': '8rem', 'name': 'Display', 'fluid': {'min': '3.2rem', 'max': '8rem'}},
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'},
                {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'},
                {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5.5rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': [{'slug': 'print', 'name': 'Hard print shadow', 'shadow': '6px 6px 0 0 #111111'}]},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|accent'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '0.95', 'letterSpacing': '0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0', 'lineHeight': '1.3'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                'border': {'radius': '999px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|medium', 'letterSpacing': '0.03em'},
                'spacing': {'padding': {'top': '0.55em', 'bottom': '0.45em', 'left': '1.3em', 'right': '1.3em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'border': {'color': 'var:preset|color|contrast'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}},
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '0.9'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|base'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '0.02em'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '800'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'filter': {'duotone': 'var:preset|duotone|red-print'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '3px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.35'}, 'color': {'background': 'var:preset|color|accent-2'},
                           'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'shadow': 'var:preset|shadow|print',
                           'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large'}, 'border': {'width': '0'}, 'color': {'text': 'var:preset|color|accent'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/search': {'border': {'radius': '999px'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large'}},
        },
        'css': (
            'body{font-synthesis:none}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
            'table{font-variant-numeric:tabular-nums}.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:0;border-bottom:2px solid var(--wp--preset--color--contrast);padding:.55em .8em .55em 0;text-align:left}'
            '.wp-block-table thead{border-bottom:4px solid var(--wp--preset--color--contrast)}.wp-block-table th{font-weight:800}'
            '.wp-block-search__input{border:3px solid var(--wp--preset--color--contrast);border-radius:999px;padding:.6em 1.1em}.wp-block-search__button{border-radius:999px}'
            ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'
            '.wp-block-navigation .current-menu-item>a{color:var(--wp--preset--color--accent)}'
            '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--accent-2)!important;font-size:var(--wp--preset--font-size--x-large)}'
            '.wc-block-components-product-name,.wp-block-woocommerce-product-template .wp-block-post-title,.product_title{font-family:var(--wp--preset--font-family--display)!important;font-weight:400!important}'
            '.wc-block-components-product-image img,.wp-block-woocommerce-product-image img,.woocommerce-product-gallery img{border:3px solid var(--wp--preset--color--contrast);filter:none}'
            '.wc-block-components-button:not(.is-link),.single_add_to_cart_button,.wp-block-button.wc-block-components-product-button .wp-block-button__link{border-radius:999px!important;background:var(--wp--preset--color--contrast)!important;color:var(--wp--preset--color--base)!important;font-family:var(--wp--preset--font-family--display)!important}'
            '.wc-block-components-product-sale-badge,.onsale{border-radius:999px!important;background:var(--wp--preset--color--accent)!important;color:var(--wp--preset--color--base)!important;border:0!important}'
            '@media (prefers-reduced-motion:no-preference){.is-style-talker{transition:transform .2s}.is-style-talker:hover{transform:rotate(0)!important}}'
        ),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-event', 'title': 'Event', 'postTypes': ['post']},
    ],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Shelf
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A loud, illustrated site for independent bookshops that sell online, run events and send a hand-picked book a month.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: shelf
Tags: e-commerce, entertainment, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

P = lambda n: {'top': 'var:preset|spacing|%s' % n, 'bottom': 'var:preset|spacing|%s' % n, 'left': 'var:preset|spacing|%s' % n, 'right': 'var:preset|spacing|%s' % n}
section('talker', 'Shelf-talker card', ['core/group', 'core/column'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'}, 'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'shadow': 'var:preset|shadow|print', 'spacing': {'padding': P(40)}, 'css': '&{transform:rotate(-1.2deg)}&:nth-child(even){transform:rotate(1.4deg)}'})
section('talker-list', 'Shelf-talker list', ['core/post-template'], {
    'css': ('&{gap:var(--wp--preset--spacing--50)!important}&>li{background:var(--wp--preset--color--accent-2);border:3px solid var(--wp--preset--color--contrast);box-shadow:6px 6px 0 0 var(--wp--preset--color--contrast);padding:var(--wp--preset--spacing--40);transform:rotate(-1.2deg)}'
            '&>li:nth-child(even){transform:rotate(1.3deg)}&>li:nth-child(3n){background:var(--wp--preset--color--base)}')})
section('sticker', 'Round sticker', ['core/group'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'border': {'radius': '50%'},
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'},
    'css': '&{aspect-ratio:1;width:9.5rem;display:flex;align-items:center;justify-content:center;text-align:center;transform:rotate(-12deg);padding:1rem}& p{margin:0}'})
section('logo-badge', 'Logo badge', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}, 'border': {'radius': '50%'},
    'css': '&{aspect-ratio:1;width:6.2rem;display:flex!important;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(-8deg);gap:0!important}& p{margin:0}'})
section('ink', 'Ink panel', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}, 'spacing': {'padding': P(60)},
    'elements': {'link': {'color': {'text': 'var:preset|color|accent-2'}}, 'button': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'}}, 'heading': {'color': {'text': 'var:preset|color|base'}}}})
section('red', 'Red panel', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'spacing': {'padding': P(60)},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}}}})
section('newsprint', 'Newsprint panel', ['core/group', 'core/columns'], {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'spacing': {'padding': P(60)}})
section('gig-list', 'Gig poster list', ['core/table'], {
    'css': ('& td{border-bottom:3px solid var(--wp--preset--color--contrast)!important;vertical-align:middle!important;padding:.8em 1em .8em 0!important}'
            '& td:first-child{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large);line-height:.9;color:var(--wp--preset--color--accent);white-space:nowrap;width:1%}'
            '& td:nth-child(2){font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);line-height:1}')})
section('framed', 'Framed illustration', ['core/image', 'core/group'], {
    'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'shadow': 'var:preset|shadow|print'})
section('steps', 'Big steps', ['core/list'], {
    'css': ('&{list-style:none;padding:0;counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:var(--wp--preset--spacing--50)}'
            '&>li{counter-increment:s;border-top:3px solid currentColor;padding-top:.8rem}&>li::before{content:counter(s);display:block;font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--xx-large);line-height:1;color:var(--wp--preset--color--accent)}')})
section('notice', 'Notice bar', ['core/group'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'elements': {'link': {'color': {'text': 'var:preset|color|base'}}},
    'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'}})
section('rule-top', 'Thick rule above', ['core/group'], {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '4px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})

def variation(fname, title, over, extra=None):
    p = {s: [c, n] for s, c, n in PAL}
    for s, c, n in over:
        p[s] = [c, n]
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': [{'slug': s, 'color': v[0], 'name': v[1]} for s, v in p.items()]}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)

variation('stacks', 'Stacks', [('accent', '#7A1E2C', 'Bookcloth maroon'), ('accent-2', '#F4E3B5', 'Bookplate'), ('surface', '#F5F1EA', 'Endpaper')])
variation('basement', 'Basement', [('base', '#12261E', 'Basement green'), ('contrast', '#F3EBD8', 'Cream'), ('accent', '#FF6B4A', 'Exit sign'), ('accent-2', '#F2C14E', 'Bulb'),
                                   ('surface', '#1B3429', 'Shelf'), ('line', '#F3EBD8', 'Rule'), ('muted', '#C9C3B3', 'Dust')],
          {'elements': {'button': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|base'}}}})
variation('childrens', 'Children\'s corner', [('base', '#FFF5CC', 'Custard'), ('accent', '#C2185B', 'Bubblegum'), ('accent-2', '#8BD3F7', 'Sky'), ('surface', '#FFE27A', 'Yolk')])

# ---------------- helpers
def q(inner, per_page=6, qid=1, pt_class=None, layout=None, **attrs):
    qq = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'post', 'order': 'desc', 'orderBy': 'date', 'inherit': False}
    a = {'queryId': qid, 'query': qq, **attrs}
    pta = {}
    if pt_class: pta['className'] = pt_class
    if layout: pta['layout'] = layout
    return ('<!-- wp:query%s -->\n<div class="wp-block-query"><!-- wp:post-template%s -->\n%s\n<!-- /wp:post-template -->\n\n'
            '<!-- wp:query-no-results -->\n%s\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->') % (
        ' ' + json.dumps(a, separators=(',', ':')), (' ' + json.dumps(pta, separators=(',', ':'))) if pta else '', inner, para('No picks on the shelf yet.'))

PAD = lambda t, b: {'spacing': {'padding': {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}}}
GRID = lambda n, w='16rem': {'type': 'grid', 'columnCount': n, 'minimumColumnWidth': w}
DUO = {'color': {'duotone': 'var:preset|duotone|red-print'}}

def art(f, alt, cap='', **kw):
    return image(f, alt, cap, style=DUO, className='is-style-framed', **kw)

pick_card = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3'),
              dyn('post-title', isLink=True, level=3, fontSize='large'),
              dyn('post-excerpt', excerptLength=30, moreText='Read the whole note'),
              dyn('post-terms', term='post_tag', separator=', '))

# ---------------- parts
write('parts/notice.html', pattern_ref('notice-christmas'))
write('parts/header.html', J(
    template_part('notice'),
    group(row(J(
        group(J(dyn('site-title', level=0), para('Rotterdam', fontSize='x-small', style={'typography': {'fontWeight': '800'}})), className='is-style-logo-badge', layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'center'}),
        dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
        justify='space-between', align='wide'), tag='header', align='full', style=PAD(30, 30))))
write('parts/footer.html', group(J(
    columns(
        ('36%', J(heading('De Inktvis', 2, fontSize='xx-large', textColor='base'),
                  para('An independent bookshop on the Nieuwe Binnenweg since 2011. New books, some second-hand, a lot of comics and a children\'s corner at the back.', fontSize='small'))),
        (None, J(heading('Come in', 6), para('Nieuwe Binnenweg 112<br>3015 BH Rotterdam<br>Tram 4, stop Heemraadsplein<br>010 234 56 78', fontSize='small'))),
        (None, J(heading('Open', 6), para('Tue to Sat 10:00 to 18:00<br>Thursday until 21:00<br>Sunday 12:00 to 17:00<br>Monday closed', fontSize='small'))),
        (None, J(heading('Elsewhere', 6), para('<a href="mailto:winkel@example.com">winkel@example.com</a><br><a href="https://www.instagram.com/">Instagram</a><br><a href="#newsletter">The Friday email</a>', fontSize='small'))),
        align='wide'),
    para('Illustrations are public domain engravings and paintings from Wikimedia Commons, printed here in red. They stand in for the shop\'s own.', fontSize='x-small', align='wide')),
    tag='footer', align='full', className='is-style-ink', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ---------------- templates
T = lambda inner, t=50, b=70: page_template(inner, style=PAD(t, b))
write('templates/front-page.html', T(J(
    pattern_ref('hero-this-month'), pattern_ref('staff-picks'), pattern_ref('new-in'), pattern_ref('events-gig-list'), pattern_ref('print-band'), pattern_ref('subscription-explainer'), pattern_ref('visit-us')), 20, 0))
pattern('picks-archive', 'Staff picks (inherits the page query)', 'query', inherit_query(pick_card, layout=GRID(3), template_class='is-style-talker-list', align='wide'), inserter=False)
write('templates/home.html', T(J(
    heading('Staff picks', 1, align='wide', fontSize='display'),
    para('Every bookseller picks one book a month and writes the note on a yellow card in the shop. These are those cards. Older months are further down.', align='wide', fontSize='large'),
    pattern_ref('picks-archive'))))
write('templates/index.html', T(J(dyn('query-title', type='archive', align='wide'), pattern_ref('picks-archive'))))
write('templates/archive.html', T(J(dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='display'), dyn('term-description', align='wide'), pattern_ref('picks-archive'))))
write('templates/search.html', T(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='An author, a title, a feeling', buttonText='Search', align='wide'), pattern_ref('picks-archive'))))
write('templates/404.html', T(J(heading('This shelf is empty', 1, fontSize='display'),
    para('The page has gone, or it was never there. Ask at the till, or search: we\'re better at finding books than pages.'),
    dyn('search', label='Search', showLabel=False, placeholder='An author, a title, a feeling', buttonText='Search')), 70, 80))
write('templates/page.html', T(J(dyn('post-title', level=1, fontSize='display'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', T(J(dyn('post-title', level=1, align='wide', fontSize='display'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'}))))
single = lambda label: T(J(
    columns(('45%', dyn('post-featured-image', aspectRatio='4/5')),
            (None, J(dyn('post-terms', term='category', textColor='accent'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'default'}),
                     dyn('post-terms', term='post_tag', prefix='Shelved under: '))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    group(J(heading(label, 2), q(pick_card, per_page=3, qid=6, layout=GRID(3), pt_class='is-style-talker-list')), align='wide', className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}})), 40, 70)
write('templates/single.html', single('More from the yellow cards'))
write('templates/single-event.html', single('Also on the shelf'))

# ---------------- patterns
pattern('hero-kraken', 'Hero: kraken and big type', 'hero', columns(
    ('55%', J(heading('Books with teeth', 2, fontSize='display'),
              para('De Inktvis is an independent bookshop on the Nieuwe Binnenweg. Eleven thousand books, four booksellers, one shop cat called Pim. We pick what we stock, and we\'ll order anything else by the next day.', fontSize='large'),
              buttons(('See this month\'s picks', '/picks/'), ('Get a book a month', '/subscriptions/', {'className': 'is-style-outline'})))),
    (None, J(art('kraken.jpg', 'Engraving of a giant octopus rising from a rough sea beside a steamship'),
             group(para('Open till 9 on Thursdays'), className='is-style-sticker'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}))

pattern('staff-picks', 'Staff picks (shelf-talker cards)', 'featured,posts', group(J(
    row(J(heading('This month\'s yellow cards', 2, fontSize='xx-large'), para('<a href="/picks/">Every pick, every month</a>')), justify='space-between'),
    q(pick_card, per_page=6, qid=2, layout=GRID(3), pt_class='is-style-talker-list')),
    align='wide', layout={'type': 'default'}, className='is-style-newsprint'), description='The signature: staff picks as tilted yellow shelf-talkers with the bookseller\'s note.')

def talker(title, author, note, who, price, img, alt):
    return group(J(art(img, alt), heading(title, 3), para(author, style={'typography': {'fontWeight': '800'}}), para(note), para('%s, %s' % (who, price), fontSize='x-small')), className='is-style-talker')

pattern('talker-card', 'Single shelf-talker (static)', 'featured', talker('The Squid Who Couldn\'t Swim', 'Lotte van Dijk', 'I read this to my nephew four times in one weekend and I laughed every time. The page with the jellyfish choir is the best spread I\'ve seen this year.', 'Picked by Samira', '€16.95', 'kraken.jpg', 'Engraving of a giant octopus beside a steamship'))

pattern('talker-row', 'Shelf-talkers (static row of three)', 'featured', grid(J(
    talker('Paper Harbour', 'Joris Pieters', 'A novel about the Rotterdam docks in 1940, told by a crane operator. Slow for fifty pages and then you won\'t put it down.', 'Picked by Bram', '€22.50', 'rotterdam.jpg', 'An old hand-coloured map of Rotterdam with canals and polders'),
    talker('The Owl Year', 'Freya Marsh', 'Twelve months of watching one pair of owls. I cried at April. It\'s that kind of book.', 'Picked by Noor', '€19.99', 'owl.jpg', 'Plate of several small owls perched on branches'),
    talker('Fox Weather', 'Tomás Reyes', 'Short stories, all set on the same wet night. The fox is only in one of them, which annoyed me and then didn\'t.', 'Picked by Samira', '€18.50', 'fox.jpg', 'A painted fox trotting past palm fronds')), min_width='16rem', align='wide', style={'spacing': {'blockGap': 'var:preset|spacing|50'}}))

pattern('booksellers-choice', 'Bookseller\'s choice of the month', 'featured', columns(
    ('40%', art('portrait.jpg', 'Woodcut portrait of an old man with a long curling beard')),
    (None, J(heading('October\'s big one', 2, fontSize='xx-large'),
             para('<strong>The Long Beard of Doctor Visser</strong>, by Anna Kruit. €24.95, hardback, signed copies at the till.', fontSize='large'),
             para('Bram has pushed this into the hands of eleven customers so far. A retired doctor in Delfshaven decides to grow the longest beard in the Netherlands and the whole street gets involved. It\'s very funny and then it isn\'t.'),
             buttons(('Buy it', '/shop/'), ('Past choices', '/picks/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

# Events
EVENTS = [['8 Oct', 'Lotte van Dijk reads The Squid Who Couldn\'t Swim', 'Sat 11:00, for ages 4 to 8, free', '<a href="/events/">Book a place</a>'],
          ['16 Oct', 'Anna Kruit in conversation with Bram', 'Thu 20:00, €7.50 or free with the book', '<a href="/events/">Tickets</a>'],
          ['24 Oct', 'Comics swap and drawing night', 'Fri 19:00, bring two comics, take two home', '<a href="/events/">Just come</a>'],
          ['6 Nov', 'Reading group: Paper Harbour', 'Thu 19:30, €5 with a drink', '<a href="/events/">Sign up</a>']]
pattern('events-gig-list', 'Events (gig poster list)', 'events', group(J(
    heading('On in the shop', 2, fontSize='xx-large'),
    table(EVENTS, className='is-style-gig-list'),
    para('Events are in the shop, upstairs is not accessible, so we do everything on the ground floor. Chairs for 40. Tickets at the till or by email.', fontSize='small')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|60'}}}))

pattern('event-detail', 'Event detail (when, where, ticket)', 'events', J(
    table([['When', 'Thursday 16 October, 20:00 to 21:30. Doors 19:30.'], ['Where', 'In the shop, ground floor, step-free'], ['Tickets', '€7.50, or free if you buy the book that night'], ['Signing', 'After the talk. Bring any of Anna\'s books.']]),
    buttons(('Email for a ticket', 'mailto:winkel@example.com?subject=Anna%20Kruit%20tickets'))))

pattern('events-page', 'Page: events', 'events', J(pattern_ref('events-gig-list'), pattern_ref('event-detail'), pattern_ref('reading-group'), pattern_ref('story-hour')), block_types='core/post-content')

pattern('reading-group', 'Reading group', 'events', group(J(
    heading('The Thursday reading group', 3),
    para('First Thursday of the month, 19:30, around the big table. We read one novel a month, chosen by vote at the meeting before. Members get 10% off the book. Twelve seats; there\'s usually one free.'),
    buttons(('Ask for a seat', 'mailto:winkel@example.com?subject=Reading%20group'))), className='is-style-talker'))

# Subscriptions (signature from research)
pattern('subscription-explainer', 'Book-a-month subscription (how it works)', 'shop,featured', group(J(
    heading('A book a month, picked for you', 2, fontSize='xx-large'),
    lst(['You fill in a short questionnaire: three books you loved, one you gave up on, and anything you\'ve read too much of lately.',
         'One of us, usually Noor, reads your answers and picks a book. We write why on a yellow card and tuck it inside.',
         'It\'s wrapped in our red paper and posted on the first Tuesday of the month. If you already have it, send it back and we\'ll swap it.'], ordered=True, className='is-style-steps'),
    buttons(('Start a subscription', '/subscriptions/'))),
    align='full', className='is-style-red', layout={'type': 'constrained', 'contentSize': '1320px'}))

pattern('subscription-lengths', 'Subscription lengths and formats', 'shop', table(
    [['3 months', '€60', '€84'], ['6 months', '€114', '€162'], ['11 months (a year, we skip August)', '€199', '€289']],
    head=['Length', 'Paperback', 'Hardback'], caption='Prices include post in the Netherlands. Belgium and Germany add €4 a month.'))

pattern('themed-subscriptions', 'Themed subscriptions', 'shop', grid(J(
    group(J(art('crocodile.jpg', 'Old engraving of a crocodile in a rocky landscape'), heading('Whodunit', 3), para('Crime, old and new. Nothing too gory unless you ask.')), className='is-style-talker'),
    group(J(art('cat.jpg', 'Painted illustration of a cat drinking from a dish while a woman watches'), heading('Bedtime', 3), para('Picture books for ages 2 to 6, picked for reading aloud.')), className='is-style-talker'),
    group(J(art('bicycle.jpg', 'Catalogue engraving of an old racing bicycle'), heading('Non-fiction nerd', 3), para('One odd, true book a month. Last month: a history of the bicycle bell.')), className='is-style-talker')),
    min_width='16rem', align='wide', style={'spacing': {'blockGap': 'var:preset|spacing|50'}}))

pattern('questionnaire', 'The questionnaire (what we ask)', 'shop', J(
    heading('What we\'ll ask you', 3),
    lst(['Three books you loved, and why in a sentence.', 'One book you gave up on.', 'What you\'ve read too much of lately.', 'Anything you never want: war, dogs dying, second person.', 'Paperback or hardback, and do you read in Dutch, English, or both?'])))

pattern('gift-voucher', 'Gift subscription (recipient fills it in later)', 'shop', group(J(
    heading('Giving it as a present?', 3),
    para('You only need their name and country. We send them a card with a link to the questionnaire, and the first book goes out once they\'ve filled it in. If they never do, we pick anyway.')),
    className='is-style-newsprint'))

pattern('subscriptions-page', 'Page: subscriptions', 'shop', J(
    pattern_ref('subscription-explainer'), pattern_ref('subscription-lengths'), pattern_ref('themed-subscriptions'), pattern_ref('questionnaire'), pattern_ref('gift-voucher'),
    buttons(('Email us to start one', 'mailto:winkel@example.com?subject=Book%20a%20month'))), block_types='core/post-content')

pattern('signed-club', 'Signed first editions club', 'shop', columns(
    ('40%', art('tulips.jpg', 'Botanical drawing of two orange tulips on a long stem')),
    (None, J(heading('Signed first editions club', 2), para('One signed hardback first edition a month, Dutch or English fiction. €32 a month, 12 months minimum. We have 60 places and 9 are free.'),
             para('Kids\' version, 8 to 12: a signed children\'s hardback every other month, €20.'),
             buttons(('Join the club', 'mailto:winkel@example.com?subject=Signed%20club')))), align='wide', verticalAlignment='center'))

pattern('signed-shelf', 'Signed books shelf', 'shop', J(
    heading('Signed on the shelf now', 3),
    table([['The Long Beard of Doctor Visser', 'Anna Kruit', 'Hardback', '€24.95'], ['Paper Harbour', 'Joris Pieters', 'Hardback', '€22.50'], ['The Squid Who Couldn\'t Swim', 'Lotte van Dijk', 'Hardback', '€16.95']],
          head=['Title', 'Author', 'Format', 'Price'], caption='Signed in the shop. They go fast after an event.')))

pattern('shipping-times', 'Shipping times table', 'shop', J(
    heading('Where we post to', 3),
    table([['Netherlands', '€3.95, free over €30', '1 to 2 days'], ['Belgium, Germany', '€7.50', '2 to 4 days'], ['Rest of the EU', '€12.50', '4 to 8 days'], ['UK and everywhere else', '€18', '7 to 14 days']],
          head=['Where', 'Postage', 'Usually takes']),
    para('Ordered before 15:00 on a weekday? It goes out that day. Books not in the shop take one more day.', fontSize='small')))

pattern('notice-christmas', 'Notice: Christmas cut-off and wrapping', 'banner', group(
    para('Order by 18 December for Christmas in the Netherlands. In the shop we wrap for free in red paper, tell us at the till.', align='center'),
    align='full', className='is-style-notice', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
    description='Christmas cut-off date and the free gift-wrapping note. Remove after 18 December.')

pattern('visit-us', 'Visit us (address, hours, map)', 'contact', group(columns(
    ('45%', art('rotterdam.jpg', 'Old hand-coloured map of Rotterdam with canals and polders', 'Rotterdam in 1340, roughly. The shop is off the map, to the west.')),
    (None, J(heading('Come in', 2, fontSize='xx-large'),
             table([['Tuesday to Saturday', '10:00 to 18:00'], ['Thursday', 'until 21:00'], ['Sunday', '12:00 to 17:00'], ['Monday', 'Closed']]),
             para('Nieuwe Binnenweg 112, 3015 BH Rotterdam. Tram 4 to Heemraadsplein, or ten minutes\' walk from Rotterdam Centraal. Step-free on the ground floor, which is where most of the books are.'),
             para('Pim the cat sleeps in the travel section. Please don\'t pick him up.', style={'typography': {'fontWeight': '800'}}))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}), align='full', className='is-style-newsprint', layout={'type': 'constrained', 'contentSize': '1320px'}))

pattern('sell-us-books', 'Sell us your books', 'services', J(
    para('We buy second-hand books on Wednesday afternoons, 14:00 to 17:00. Bring up to two bags. We pay in cash or in shop credit, and credit is worth 30% more.', fontSize='large'),
    heading('What we buy', 4), lst(['Fiction and non-fiction in good condition, Dutch or English', 'Comics and graphic novels', 'Art, design and Rotterdam history']),
    heading('What we don\'t', 4), lst(['Textbooks and old encyclopaedias', 'Books with water damage or smells', 'Reader\'s Digest anything'])))

pattern('sell-page', 'Page: sell us your books', 'services', J(pattern_ref('sell-us-books'), art('bookstack.jpg', 'A tall stack of well-read books on a table')), block_types='core/post-content')

pattern('booksellers', 'The booksellers', 'about', grid(J(
    group(J(heading('Samira', 3), para('Picture books, comics, anything with a monster in it. Runs the Saturday story hour.')), className='is-style-talker'),
    group(J(heading('Bram', 3), para('Owner since 2011. Crime, Rotterdam history and long novels about ships.')), className='is-style-talker'),
    group(J(heading('Noor', 3), para('Runs the book-a-month subscriptions. Reads about 200 books a year and remembers all of them.')), className='is-style-talker'),
    group(J(heading('Wessel', 3), para('Saturdays and the second-hand buying. Poetry and anything translated from Polish.')), className='is-style-talker')),
    min_width='14rem', align='wide', style={'spacing': {'blockGap': 'var:preset|spacing|50'}}))

pattern('about-page', 'Page: about the shop', 'about', J(
    columns(('45%', art('shop.jpg', 'Inside a bookshop, wooden shelves floor to ceiling and a table of books in the middle')),
            (None, J(para('Bram de Wit opened De Inktvis in 2011 in a former fishmonger\'s, which is where the name and the tiled back wall come from.', fontSize='large'),
                     para('We\'re four booksellers and a cat. We stock about 11,000 books, choose every one of them, and we\'ll order anything we don\'t have by the next day. Half our customers come in for one book and leave with three, which is the plan.'),
                     para('We don\'t sell e-readers and we don\'t price-match. We do wrap presents for free.'))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('booksellers'), pattern_ref('bookseller-profile'), pattern_ref('signed-club'), pattern_ref('signed-shelf')), block_types='core/post-content')

pattern('visit-page', 'Page: visit', 'visit', J(pattern_ref('visit-us'), pattern_ref('contact-block'), pattern_ref('faq'), pattern_ref('newsletter')), block_types='core/post-content')

pattern('newsletter', 'Friday email', 'call-to-action', group(columns(
    ('60%', J(heading('The Friday email', 2), para('New yellow cards, this week\'s events and one thing we\'re annoyed about. Every Friday at 8. From Noor, not a machine.'))),
    (None, buttons(('Email us to sign up', 'mailto:winkel@example.com?subject=Friday%20email'))), verticalAlignment='center'),
    anchor='newsletter', align='wide', className='is-style-ink', layout={'type': 'default'}))

pattern('kids-corner', 'Children\'s corner', 'featured', columns(
    (None, J(heading('The back room is for kids', 2, fontSize='xx-large'), para('Two sofas, a rug and about 2,000 children\'s books sorted by age, not by publisher. Story hour on Saturdays at 11:00, free, no booking. Parents get coffee.'))),
    ('40%', art('hare.jpg', 'Old nursery illustration of a hare with a rifle chasing a hunter')), align='wide', verticalAlignment='center'))

pattern('shop-sections', 'Shop sections (links)', 'shop', grid(J(
    group(J(heading('<a href="/shop/">Fiction</a>', 3), para('Dutch and English, new in every Tuesday.')), className='is-style-talker'),
    group(J(heading('<a href="/shop/">Comics</a>', 3), para('Bandes dessinées, manga and small-press zines.')), className='is-style-talker'),
    group(J(heading('<a href="/shop/">Kids</a>', 3), para('Sorted by age, 0 to 14.')), className='is-style-talker'),
    group(J(heading('<a href="/shop/">Second-hand</a>', 3), para('Upstairs by the window. Everything €5 or less.')), className='is-style-talker')),
    min_width='12rem', align='wide', style={'spacing': {'blockGap': 'var:preset|spacing|50'}}))

# ---------------- round 2: fewer tables, a bigger kit, a hero that opens on the book of the month
section('ruled', 'Ruled row', ['core/columns', 'core/group'], {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}, 'css': '& p{margin:0}'})
section('gig-date', 'Gig date', ['core/paragraph'], {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '0.9'}, 'color': {'text': 'var:preset|color|accent'}})

def rrow(cells, widths, first_bold=True):
    return columns(*[(w, para(c, style={'typography': {'fontWeight': '800'}} if (i == 0 and first_bold) else {})) for i, (w, c) in enumerate(zip(widths, cells))], className='is-style-ruled', isStackedOnMobile=False, style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}, 'margin': {'top': '0', 'bottom': '0'}}})

HOURS = [['Tuesday to Saturday', '10:00 to 18:00'], ['Thursday', 'until 21:00'], ['Sunday', '12:00 to 17:00'], ['Monday', 'Closed']]
pattern('opening-hours', 'Opening hours (ruled rows)', 'visit', group(J(*[rrow(h, [None, '9rem']) for h in HOURS]), style={'spacing': {'blockGap': '0'}}))

pattern('visit-us', 'Visit us (address, hours, map)', 'visit', group(columns(
    ('45%', art('rotterdam.jpg', 'Old hand-coloured map of Rotterdam with canals and polders', 'Rotterdam in 1340, roughly. The shop is off the map, to the west.')),
    (None, J(heading('Come in', 2, fontSize='xx-large'), pattern_ref('opening-hours'),
             para('Nieuwe Binnenweg 112, 3015 BH Rotterdam. Tram 4 to Heemraadsplein, or ten minutes\' walk from Rotterdam Centraal. Step-free on the ground floor, which is where most of the books are.'),
             para('Pim the cat sleeps in the travel section. Please don\'t pick him up.', style={'typography': {'fontWeight': '800'}}))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}), align='full', className='is-style-newsprint', layout={'type': 'constrained', 'contentSize': '1320px'}))

def gig(date, what, when, link):
    return columns(('8rem', para(date, className='is-style-gig-date')), (None, J(para(what, fontFamily='display', fontSize='large'), para(when, fontSize='small'))), ('9rem', para(link, style={'typography': {'fontWeight': '800'}})),
                   className='is-style-ruled', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}, 'margin': {'top': '0', 'bottom': '0'}}})
pattern('events-gig-list', 'Events (gig poster list)', 'events', group(J(
    heading('On in the shop', 2, fontSize='xx-large'),
    group(J(*[gig(*e) for e in EVENTS]), style={'spacing': {'blockGap': '0'}}),
    para('Events are on the ground floor, step-free. Chairs for 40. Tickets at the till or by email.', fontSize='small')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|60'}}}))

pattern('event-detail', 'Event detail (when, where, ticket)', 'events', J(
    group(J(*[rrow(r, ['8rem', None]) for r in [['When', 'Thursday 16 October, 20:00 to 21:30. Doors 19:30.'], ['Where', 'In the shop, ground floor, step-free'], ['Tickets', '€7.50, or free if you buy the book that night'], ['Signing', 'After the talk. Bring any of Anna\'s books.']]]), style={'spacing': {'blockGap': '0'}}),
    buttons(('Email for a ticket', 'mailto:winkel@example.com?subject=Anna%20Kruit%20tickets'))))

SIGNED = [('portrait.jpg', 'Woodcut portrait of a bearded man', 'The Long Beard of Doctor Visser', 'Anna Kruit, hardback', '€24.95'), ('rotterdam.jpg', 'Old map of Rotterdam', 'Paper Harbour', 'Joris Pieters, hardback', '€22.50'), ('kraken.jpg', 'Engraving of a giant octopus', 'The Squid Who Couldn\'t Swim', 'Lotte van Dijk, hardback', '€16.95')]
def book_card(img, alt, t, a, p_):
    return group(J(art(img, alt), heading(t, 3, fontSize='large'), para(a, fontSize='small'), para(p_, style={'typography': {'fontWeight': '800'}}, textColor='accent')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}})
pattern('signed-shelf', 'Signed books shelf', 'shop', J(heading('Signed on the shelf now', 3), grid(J(*[book_card(*b) for b in SIGNED]), min_width='14rem', style={'spacing': {'blockGap': 'var:preset|spacing|50'}}), para('Signed in the shop. They go fast after an event.', fontSize='small')))

pattern('hero-this-month', 'Hero: the book of the month', 'hero', columns(
    ('42%', J(art('portrait.jpg', 'Woodcut portrait of an old man with a long curling beard'), group(para('Anna Kruit in the shop, 16 Oct'), className='is-style-sticker'))),
    (None, J(para('October\'s big one, picked by Bram', fontSize='small', style={'typography': {'fontWeight': '800'}}, textColor='accent'),
             heading('The Long Beard of Doctor Visser', 1, fontSize='display'),
             para('A retired doctor in Delfshaven grows the longest beard in the Netherlands and his whole street gets involved. Very funny, then it isn\'t. Anna Kruit, hardback, €24.95, signed copies at the till.', fontSize='large'),
             buttons(('Buy it', '/shop/'), ('Book for the reading', '/anna-kruit-event/', {'className': 'is-style-outline'})),
             para('De Inktvis, independent bookshop, Nieuwe Binnenweg 112. Open today until 18:00.', fontSize='small'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}))

pattern('new-in', 'New in this week', 'shop', group(J(
    row(J(heading('New in this week', 2), para('<a href="/shop/">Everything in the shop</a>')), justify='space-between'),
    grid(J(*[book_card(*b) for b in [('owl.jpg', 'Plate of small owls on branches', 'The Owl Year', 'Freya Marsh, paperback', '€19.99'), ('fox.jpg', 'A painted fox', 'Fox Weather', 'Tomás Reyes, paperback', '€18.50'),
                                     ('crocodile.jpg', 'Engraving of a crocodile', 'The Crocodile in the Cellar', 'Mei Tanaka, paperback', '€14.99'), ('cat.jpg', 'Illustration of a cat drinking from a dish', 'Pim Reads', 'Our own zine', '€12.50')]]),
         min_width='12rem', style={'spacing': {'blockGap': 'var:preset|spacing|40'}})), align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}))

pattern('print-band', 'Print band (engravings, open large)', 'gallery', grid(J(art('kraken.jpg', 'Engraving of a giant octopus'), art('owl.jpg', 'Owls on branches'), art('crocodile.jpg', 'Engraving of a crocodile'), art('fox.jpg', 'A painted fox')), min_width='12rem', align='wide', style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
        description='A strip of house illustrations in red print. Click any one to see it large.')

pattern('bookseller-profile', 'Bookseller profile', 'about', columns(
    ('35%', art('portrait.jpg', 'Woodcut portrait of a bearded man')),
    (None, J(heading('Bram de Wit', 3), para('Owner since 2011', fontSize='small', textColor='accent', style={'typography': {'fontWeight': '800'}}),
             para('Reads crime, Rotterdam history and long novels about ships. Will talk to you about Simenon for as long as you let him. His yellow cards are the ones with the bad handwriting.'),
             para('<a href="/picks/">Bram\'s picks</a>'))), verticalAlignment='center'))

pattern('loyalty-card', 'Stamp card', 'shop', group(J(
    heading('The stamp card', 3), para('One stamp per book, in the shop or online. Ten stamps and the next book is 20% off. The card is red, it lives in your wallet, and yes, we\'ll look up your stamps if you lose it.')), className='is-style-talker'))

pattern('order-anything', 'We order any book', 'shop', group(columns(
    ('60%', J(heading('Not on the shelf? We\'ll get it tomorrow', 2), para('Any book in print from a Dutch or English publisher, in the shop the next working day if you order before 15:00. Same price as online, and you can pick it up or have it posted.'))),
    (None, buttons(('Ask us for a book', 'mailto:winkel@example.com?subject=Order'))), verticalAlignment='center'), align='wide', className='is-style-red', layout={'type': 'default'}))

pattern('gift-wrap', 'Free gift wrapping', 'shop', group(J(heading('We wrap for free', 3), para('In our red paper with a black sticker, at the till or on online orders if you tick the box. Takes two minutes. We don\'t do bows.')), className='is-style-newsprint'))

pattern('school-orders', 'Schools and book clubs', 'services', columns(
    (None, J(heading('Schools', 3), para('Class sets at 15% off, delivered to the school by bike within Rotterdam. Samira visits for a reading once a term if you ask nicely.'))),
    (None, J(heading('Book clubs', 3), para('Eight or more copies of one title: 10% off, and we\'ll hold them until your club collects.')))))

pattern('story-hour', 'Saturday story hour', 'events', group(columns(
    ('35%', art('hare.jpg', 'Nursery illustration of a hare chasing a hunter')),
    (None, J(heading('Story hour, Saturdays 11:00', 3), para('Samira reads three picture books in the back room, then everyone draws. Ages 3 to 7, free, no booking. Parents get coffee.'))), verticalAlignment='center'), className='is-style-talker'))

pattern('comics-shelf', 'Comics and zines', 'shop', group(J(
    heading('The comics wall', 2),
    para('Bandes dessinées, manga, small-press zines and a box of Rotterdam risograph comics by the door. Wessel orders two new small-press titles every week. Zines from €3.'),
    buttons(('See the comics in the shop', '/shop/'))), className='is-style-ink', align='wide', layout={'type': 'constrained'}))

pattern('faq', 'Questions people ask at the till', 'faq', J(
    heading('Questions people ask at the till', 3),
    details('Can I return a book?', para('Within 14 days with the receipt, if it\'s unread. Signed copies can\'t be returned.')),
    details('Do you buy second-hand books?', para('Wednesdays 14:00 to 17:00. See <a href="/sell-us-your-books/">Sell us your books</a>.')),
    details('Can I pay by card?', para('Card, phone or cash. No minimum.')),
    details('Is the shop accessible?', para('The ground floor is step-free and has most of the books. Upstairs is second-hand only, and we\'ll bring things down for you.'))))

pattern('contact-block', 'Contact (address, phone, email)', 'visit', columns(
    (None, J(heading('Address', 4), para('Nieuwe Binnenweg 112<br>3015 BH Rotterdam'))),
    (None, J(heading('Phone', 4), para('010 234 56 78<br>During opening hours'))),
    (None, J(heading('Email', 4), para('<a href="mailto:winkel@example.com">winkel@example.com</a><br>We answer within a day')))))

pattern('ordering-page', 'Page: ordering and delivery', 'shop', J(
    pattern_ref('order-anything'), pattern_ref('shipping-times'), columns((None, pattern_ref('gift-wrap')), (None, pattern_ref('loyalty-card')), align='wide'), pattern_ref('school-orders'), pattern_ref('faq')), block_types='core/post-content')

print('shelf: patterns written')

# ---------------- demo content
def pick(title, slug, author, note, who, img, tags, cat='picks', template=None):
    d = dict(title=title, slug=slug, category=cat, tags=tags, image=img,
             excerpt=note.split('. ')[0] + '.',
             content=J(para('<strong>%s</strong>' % author, fontSize='large'), para(note), quote(note.split('. ')[-1], '%s, bookseller' % who) if '. ' in note else '',
                       buttons(('Buy it from the shop', '/shop/'))))
    if template:
        d['template'] = template
    return d

posts = [
    pick('The Long Beard of Doctor Visser', 'long-beard-doctor-visser', 'Anna Kruit, €24.95, hardback', 'A retired doctor in Delfshaven decides to grow the longest beard in the country, and his whole street gets involved. It is very funny for two hundred pages and then it isn\'t. I\'ve sold eleven and I want to sell a hundred.', 'Bram', 'portrait.jpg', ['Fiction', 'Rotterdam']),
    pick('The Squid Who Couldn\'t Swim', 'squid-who-couldnt-swim', 'Lotte van Dijk, €16.95, ages 4 to 8', 'I read this to my nephew four times in one weekend. The jellyfish choir spread is the best page I\'ve seen this year. Lotte reads it in the shop on 8 October.', 'Samira', 'kraken.jpg', ['Kids', 'Picture books']),
    pick('The Owl Year', 'the-owl-year', 'Freya Marsh, €19.99, paperback', 'Twelve months watching one pair of owls in a Norfolk barn. I cried at April. It\'s that kind of book, but it earns it.', 'Noor', 'owl.jpg', ['Nature', 'Non-fiction']),
    pick('Fox Weather', 'fox-weather', 'Tomás Reyes, €18.50, paperback', 'Short stories, all set on the same rainy night in one town. The fox is only in one of them. That annoyed me and then it didn\'t.', 'Samira', 'fox.jpg', ['Fiction', 'Short stories']),
    pick('Paper Harbour', 'paper-harbour', 'Joris Pieters, €22.50, hardback, signed', 'The Rotterdam docks in 1940, told by a crane operator. Slow for fifty pages, then you won\'t put it down. This is the reading group book for November.', 'Bram', 'rotterdam.jpg', ['Fiction', 'Rotterdam', 'Signed']),
    pick('The Crocodile in the Cellar', 'crocodile-in-the-cellar', 'Mei Tanaka, €14.99, paperback', 'A crime novel set in a Leiden museum after closing time. The crocodile is stuffed. The detective is not as clever as she thinks. Neither was I.', 'Wessel', 'crocodile.jpg', ['Crime']),
    pick('Pim Reads: A Cat\'s Guide to Bookshops', 'pim-reads', 'Written by Samira, drawn by Kees Bos, €12.50', 'Our own zine, about our own cat. Sixteen pages, risograph printed in red. All profits go to the Rotterdam cat shelter on Kleiweg.', 'Samira', 'cat.jpg', ['Kids', 'Zines']),
    pick('Anna Kruit in conversation, 16 October', 'anna-kruit-event', 'Thursday 16 October, 20:00, €7.50 or free with the book', 'Anna talks to Bram about beards, Delfshaven and writing a funny book about grief. Signing after. Chairs for 40. Book at the till or by email.', 'Bram', 'portrait.jpg', ['Events'], cat='events', template='single-event'),
]

EXTRA = {'anna-kruit-event': ['event-detail'], 'long-beard-doctor-visser': ['bookseller-profile'], 'paper-harbour': ['reading-group'], 'squid-who-couldnt-swim': ['story-hour'], 'pim-reads': ['loyalty-card']}
for p_ in posts:
    p_['content'] = J(p_['content'], *[pattern_ref(x) for x in EXTRA.get(p_['slug'], [])])

products = [
    {'name': 'The Long Beard of Doctor Visser, Anna Kruit (signed hardback)', 'price': '24.95', 'image': 'portrait.jpg', 'category': 'Fiction', 'sku': 'INK-9789000001', 'stock': 11, 'short': 'Signed at the shop. Hardback, 312 pages.'},
    {'name': 'Paper Harbour, Joris Pieters (hardback)', 'price': '22.50', 'image': 'rotterdam.jpg', 'category': 'Fiction', 'sku': 'INK-9789000002', 'stock': 6, 'short': 'Novel of the Rotterdam docks, 1940. November\'s reading group book.'},
    {'name': 'The Squid Who Couldn\'t Swim, Lotte van Dijk', 'price': '16.95', 'image': 'kraken.jpg', 'category': 'Kids', 'sku': 'INK-9789000003', 'stock': 14, 'short': 'Picture book, ages 4 to 8. Hardback, 32 pages.'},
    {'name': 'The Owl Year, Freya Marsh (paperback)', 'price': '19.99', 'image': 'owl.jpg', 'category': 'Non-fiction', 'sku': 'INK-9789000004', 'stock': 9, 'short': 'A year watching one pair of barn owls.'},
    {'name': 'Fox Weather, Tomás Reyes (paperback)', 'price': '18.50', 'image': 'fox.jpg', 'category': 'Fiction', 'sku': 'INK-9789000005', 'stock': 0, 'short': 'Out of stock. We can order it by tomorrow.'},
    {'name': 'Book a month, 3 months (paperback)', 'price': '60.00', 'image': 'bookstack.jpg', 'category': 'Subscriptions', 'sku': 'INK-SUB-3P', 'stock': 50, 'short': 'Three hand-picked books, one a month, posted in the Netherlands.'},
    {'name': 'Pim Reads (zine)', 'price': '12.50', 'image': 'cat.jpg', 'category': 'Kids', 'sku': 'INK-ZINE-01', 'stock': 30, 'short': 'Our own risograph zine about the shop cat.'},
    {'name': 'Gift voucher, €25', 'price': '25.00', 'image': 'tulips.jpg', 'category': 'Vouchers', 'sku': 'INK-GV-25', 'stock': 100, 'short': 'Printed on a card, or sent by email. Never expires.'},
]

content = {
    'site': {'title': 'De Inktvis', 'tagline': 'Independent bookshop, Nieuwe Binnenweg, Rotterdam'},
    'categories': [{'slug': 'picks', 'name': 'Staff picks'}, {'slug': 'events', 'name': 'Events'}],
    'front_page': 'home', 'posts_page': 'picks',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'picks', 'title': 'Staff picks', 'content': ''},
        {'slug': 'subscriptions', 'title': 'Book a month', 'pattern': 'shelf/subscriptions-page', 'template': 'page-wide'},
        {'slug': 'events', 'title': 'Events', 'pattern': 'shelf/events-page', 'template': 'page-wide'},
        {'slug': 'sell-us-your-books', 'title': 'Sell us your books', 'pattern': 'shelf/sell-page'},
        {'slug': 'visit', 'title': 'Visit', 'pattern': 'shelf/visit-page', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About the shop', 'pattern': 'shelf/about-page', 'template': 'page-wide'},
        {'slug': 'ordering', 'title': 'Ordering and delivery', 'pattern': 'shelf/ordering-page', 'template': 'page-wide'},
        {'slug': 'kids', 'title': 'Kids and schools', 'content': J(pattern_ref('kids-corner'), pattern_ref('story-hour'), pattern_ref('school-orders'), pattern_ref('talker-card')), 'template': 'page-wide'},
        {'slug': 'comics', 'title': 'Comics and zines', 'content': J(pattern_ref('comics-shelf'), pattern_ref('hero-kraken'), pattern_ref('talker-row')), 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'Picks', 'url': '/picks/'}, {'label': 'Book a month', 'url': '/subscriptions/'},
            {'label': 'Events', 'url': '/events/'}, {'label': 'Kids', 'url': '/kids/'}, {'label': 'Ordering', 'url': '/ordering/'}, {'label': 'Visit', 'url': '/visit/'}, {'label': 'About', 'url': '/about/'}],
    'currency': 'EUR',
    'products': products,
}
os.makedirs(os.path.join(ROOT, 'demos', S), exist_ok=True)
with open(os.path.join(ROOT, 'demos', S, 'content.json'), 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
print('shelf: content.json written')
