# Design note (roast, idea 059, "as researched": kraft-label utility)
# Direction: a small specialty roaster whose site reads like the label on its bags: boxed data (producer, region,
#   variety, process, elevation) in hard black rules, big tasting notes, kraft-paper panels and a stamp-green accent.
# Fonts: Krona One (display, wide like a stamped bag label), Karla (body, tabular figures for doses and prices). No mono.
# Palette: white, bean black #1E1A16, stamp green #1F6F4A, kraft #D8C3A0, pale kraft #F1E7D6, rules in #1E1A16.
# Layout idea: the front page opens on "this week's filter" as an actual label: a bordered box split into a data table
#   and a tasting-notes block. Brew guides are timed pour schedules in a two-column timeline (time, then action).
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('roast')
S = THEME['slug']
D = THEME['dir']
ROOT = os.path.abspath(os.path.join(D, '..', '..'))

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Krona One", "Arial Black", sans-serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"Karla", "Helvetica Neue", Arial, sans-serif'

PAL = [
    ('base', '#FFFFFF', 'Label white'),
    ('contrast', '#1E1A16', 'Bean black'),
    ('accent', '#1F6F4A', 'Stamp green'),
    ('accent-2', '#8A3B12', 'Roast brown'),
    ('surface', '#D8C3A0', 'Kraft'),
    ('surface-2', '#F1E7D6', 'Pale kraft'),
    ('line', '#1E1A16', 'Rule'),
    ('muted', '#5A5046', 'Chaff'),
]
pal = lambda p: [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1280px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.8125rem', 'name': 'Tiny', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.375rem', 'name': 'Large', 'fluid': {'min': '1.15rem', 'max': '1.375rem'}},
                {'slug': 'x-large', 'size': '1.875rem', 'name': 'Section', 'fluid': {'min': '1.4rem', 'max': '1.875rem'}},
                {'slug': 'xx-large', 'size': '2.75rem', 'name': 'Title', 'fluid': {'min': '1.8rem', 'max': '2.75rem'}},
                {'slug': 'display', 'size': '4.5rem', 'name': 'Display', 'fluid': {'min': '2.2rem', 'max': '4.5rem'}},
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'},
                {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'},
                {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4rem, 9vw, 7rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
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
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '1.15', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.7em', 'bottom': '0.7em', 'left': '1.2em', 'right': '1.2em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}},
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.02em'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.35'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '6px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large'}, 'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
        },
        'css': (
            'body{font-synthesis:none}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
            'table,.wp-block-table td,.wc-block-components-product-price,.price{font-variant-numeric:tabular-nums}'
            '.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:1.5px solid var(--wp--preset--color--line);padding:.5em .7em;text-align:left;vertical-align:top}'
            '.wp-block-table th{font-weight:800;background:var(--wp--preset--color--surface-2)}'
            '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0}'
            ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
            '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:.3em;text-decoration-color:var(--wp--preset--color--accent)}'
            '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--surface)!important;font-family:var(--wp--preset--font-family--display)}'
            '.wc-block-components-product-name,.wp-block-woocommerce-product-template .wp-block-post-title{font-family:var(--wp--preset--font-family--display)!important;letter-spacing:-.02em}'
            '.wc-block-components-product-image img,.wp-block-woocommerce-product-image img{border:2px solid var(--wp--preset--color--contrast)}'
            '.wc-block-components-button:not(.is-link),.wp-block-woocommerce-cart .wc-block-cart__submit-button{border-radius:0!important;background:var(--wp--preset--color--accent)!important;color:var(--wp--preset--color--base)!important;font-weight:800}'
            '.wc-block-components-product-sale-badge,.onsale{border-radius:0!important;background:var(--wp--preset--color--contrast)!important;color:var(--wp--preset--color--base)!important}'
            '@media (prefers-reduced-motion:no-preference){a{transition:color .15s}}'
        ),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Roast days bar'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-brew-guide', 'title': 'Brew guide', 'postTypes': ['post']},
    ],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Roast
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A shop and brew-guide site for small specialty coffee roasters that sell bags online, run subscriptions and supply a few cafés.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: roast
Tags: e-commerce, food-and-drink, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

P = lambda n: {'top': 'var:preset|spacing|%s' % n, 'bottom': 'var:preset|spacing|%s' % n, 'left': 'var:preset|spacing|%s' % n, 'right': 'var:preset|spacing|%s' % n}
section('kraft', 'Kraft panel', ['core/group', 'core/columns', 'core/column'], {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'spacing': {'padding': P(50)}})
section('pale-kraft', 'Pale kraft panel', ['core/group', 'core/columns', 'core/column'], {'color': {'background': 'var:preset|color|surface-2', 'text': 'var:preset|color|contrast'}, 'spacing': {'padding': P(50)}})
section('label', 'Bag label (boxed)', ['core/group', 'core/columns', 'core/column'], {
    'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}, 'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'spacing': {'padding': P(40)}})
section('stamp', 'Stamp bar', ['core/group'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'elements': {'link': {'color': {'text': 'var:preset|color|base'}}}, 'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'}})
section('data', 'Coffee data table', ['core/table'], {
    'css': '& td:first-child{font-weight:800;width:38%;background:var(--wp--preset--color--surface-2)}'})
section('timeline', 'Pour schedule', ['core/table'], {
    'typography': {'fontSize': 'var:preset|font-size|medium'},
    'css': '& td:first-child{font-family:var(--wp--preset--font-family--display);width:6.5em;white-space:nowrap;color:var(--wp--preset--color--accent)}& td:last-child{font-variant-numeric:tabular-nums}& td{border-left:0!important;border-right:0!important}'})
section('notes-big', 'Tasting notes (big)', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.15', 'letterSpacing': '-0.03em'}, 'css': '&{overflow-wrap:normal;word-break:normal;hyphens:none}'})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})
section('rule-bottom', 'Rule below', ['core/group'], {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}}})
section('inline', 'Inline list', ['core/categories'], {
    'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.5rem 1.5rem;font-weight:700}'})
section('guide-list', 'Brew guide list', ['core/post-template'], {
    'css': '&{gap:0!important}&>li{border:2px solid var(--wp--preset--color--contrast);margin:-1px!important;padding:var(--wp--preset--spacing--40)}&>li:hover{background:var(--wp--preset--color--surface-2)}'})

def variation(fname, title, over, extra=None):
    p = {s: [c, n] for s, c, n in PAL}
    for s, c, n in over:
        p[s] = [c, n]
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': [{'slug': s, 'color': v[0], 'name': v[1]} for s, v in p.items()]}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)

variation('lab', 'Lab', [('surface', '#E6EFEA', 'Lab green'), ('surface-2', '#F4F8F6', 'Pale lab'), ('accent', '#0E6B45', 'Data green')],
          {'elements': {'heading': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'letterSpacing': '-0.01em'}}}})
variation('espresso-bar', 'Espresso bar', [('base', '#2A1D16', 'Dark roast'), ('contrast', '#F3E6D0', 'Crema'), ('accent', '#E0A45A', 'Caramel'), ('accent-2', '#F0B97A', 'Honey'),
          ('surface', '#3D2A20', 'Roasted'), ('surface-2', '#35251C', 'Bean'), ('line', '#F3E6D0', 'Rule'), ('muted', '#D2C1A6', 'Chaff')],
          {'elements': {'button': {'color': {'text': 'var:preset|color|base'}}}})
variation('seasonal', 'Seasonal', [('accent', '#B23A48', 'Harvest red'), ('surface', '#F2C9C3', 'Label pink'), ('surface-2', '#FBEDEA', 'Pale pink')])

# ---------------- helpers
def q(inner, per_page=6, qid=1, pt_class=None, layout=None, **attrs):
    qq = {'perPage': per_page, 'pages': 0, 'offset': 0, 'postType': 'post', 'order': 'desc', 'orderBy': 'date', 'inherit': False}
    a = {'queryId': qid, 'query': qq, **attrs}
    pta = {}
    if pt_class: pta['className'] = pt_class
    if layout: pta['layout'] = layout
    return ('<!-- wp:query%s -->\n<div class="wp-block-query"><!-- wp:post-template%s -->\n%s\n<!-- /wp:post-template -->\n\n'
            '<!-- wp:query-no-results -->\n%s\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->') % (
        ' ' + json.dumps(a, separators=(',', ':')), (' ' + json.dumps(pta, separators=(',', ':'))) if pta else '', inner, para('No guides yet.'))

PAD = lambda t, b: {'spacing': {'padding': {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}}}
GRID = lambda n, w='14rem': {'type': 'grid', 'columnCount': n, 'minimumColumnWidth': w}

def data_table(rows, caption=''):
    return table(rows, caption=caption, className='is-style-data')

def schedule(rows, caption=''):
    return table(rows, head=['Time', 'What to do', 'Scale reads'], caption=caption, className='is-style-timeline')

guide_card = J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=20, moreText='Open the guide', fontSize='small'))

# ---------------- parts
write('parts/notice.html', pattern_ref('roast-days-bar'))
write('parts/header.html', J(
    template_part('notice'),
    group(row(J(dyn('site-title', level=0),
                dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
              justify='space-between', align='wide'), tag='header', align='full', className='is-style-rule-bottom', style=PAD(30, 30))))
write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0), para('Specialty coffee roasted in a 15kg Giesen in Unit 4, Hope Street Yard, Liverpool L1 9BQ. We roast on Tuesdays and Fridays and post the same afternoon.', fontSize='small'))),
        (None, J(heading('Roastery', 6), para('Open to the public Saturdays 9am to 1pm<br>Card only<br><a href="mailto:hello@example.com">hello@example.com</a><br>0151 496 0183', fontSize='small'))),
        (None, J(heading('Buying', 6), para('<a href="/shop/">Shop</a><br><a href="/subscriptions/">Subscriptions</a><br><a href="/wholesale/">Wholesale</a><br>UK post £3.50, free over £30', fontSize='small'))),
        (None, J(heading('Brewing', 6), para('<a href="/brew-guides/">Brew guides</a><br><a href="/prices-we-pay/">Prices we pay</a><br><a href="/cafes/">Where to drink it</a>', fontSize='small'))),
        align='wide'),
    para('Demo photographs are CC0 and public domain images from Wikimedia Commons, standing in for the roaster\'s own.', fontSize='x-small', textColor='muted', align='wide')),
    tag='footer', align='full', className='is-style-kraft', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ---------------- templates
T = lambda inner, t=50, b=70: page_template(inner, style=PAD(t, b))
write('templates/front-page.html', T(J(
    pattern_ref('this-weeks-filter'), pattern_ref('coffee-list'), pattern_ref('brew-guides-grid'), pattern_ref('subscription-builder'), pattern_ref('cafes-and-wholesale')), 40, 0))
pattern('guide-archive', 'Brew guides (inherits the page query)', 'query', inherit_query(guide_card, layout=GRID(3), template_class='is-style-guide-list', align='wide'), inserter=False)
write('templates/home.html', T(J(
    heading('Brew guides', 1, align='wide', fontSize='display'),
    para('One recipe per brewer. Each gives the dose, water, temperature, grind and a timed pour schedule. Use a scale. Volume measures are a guess.', align='wide'),
    dyn('categories', align='wide', className='is-style-inline'),
    pattern_ref('guide-archive'))))
write('templates/index.html', T(J(dyn('query-title', type='archive', align='wide'), pattern_ref('guide-archive'))))
write('templates/archive.html', T(J(dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'), dyn('term-description', align='wide'), pattern_ref('guide-archive'))))
write('templates/search.html', T(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Kenya, V60, decaf', buttonText='Search', align='wide'), pattern_ref('guide-archive'))))
write('templates/404.html', T(J(heading('Nothing on this shelf', 1), para('That page has gone, probably with last season\'s coffee. The shop has what we\'re roasting now.'),
                                  buttons(('Go to the shop', '/shop/'), ('Search the brew guides', '/brew-guides/', {'className': 'is-style-outline'}))), 70, 80))
write('templates/page.html', T(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', T(J(dyn('post-title', level=1, align='wide', fontSize='display'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1280px'}))))
single = T(J(
    columns(('60%', J(dyn('post-terms', term='category', textColor='accent'), dyn('post-title', level=1, fontSize='display'), dyn('post-excerpt', fontSize='large'))),
            (None, dyn('post-featured-image', aspectRatio='4/3')), align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    dyn('post-content', layout={'type': 'constrained', 'contentSize': '860px'}),
    group(J(heading('Other brewers', 3), q(guide_card, per_page=3, qid=4, layout=GRID(3), pt_class='is-style-guide-list')), align='wide', className='is-style-rule-top', layout={'type': 'default'})), 40, 70)
write('templates/single.html', single)
write('templates/single-brew-guide.html', single)

# ---------------- patterns
pattern('roast-days-bar', 'Roast and dispatch days bar', 'banner', group(
    para('We roast Tuesdays and Fridays. Order by 10am on a roast day and it\'s posted that afternoon. Next roast: Tuesday.', align='center'),
    align='full', className='is-style-stamp', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('notice-christmas', 'Notice: Christmas last roast', 'banner', group(
    para('Last roast before Christmas: Friday 18 December, posted the same day. Order by 10am. We roast again on Tuesday 5 January. Take this bar out on 19 December.', align='center'),
    align='full', className='is-style-stamp', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='Swap into the roast days bar in December, then swap back.')

KIRUGA = [['Producer', 'Kiruga Farmers\' Cooperative, Kiruga washing station'], ['Region', 'Nyeri, Kenya'], ['Variety', 'SL28, SL34, Ruiru 11'], ['Process', 'Washed, double fermented'],
          ['Elevation', '1,750 to 1,850 m'], ['Harvest', 'November 2025 to January 2026'], ['We paid', '$6.10/kg FOB, 3.1 times the Fairtrade minimum']]
pattern('coffee-label', 'Coffee label (data box and tasting notes)', 'shop,featured', columns(
    ('55%', J(heading('Kiruga AA', 2, fontSize='xx-large'), data_table(KIRUGA))),
    (None, J(heading('Tastes like', 4), para('Blackcurrant, pink grapefruit, a bit of tomato', className='is-style-notes-big'),
             para('Roasted light for filter. Rest it 7 days after the roast date on the bag.', fontSize='small'),
             table([['250g', '£12.50'], ['1kg', '£44.00']], head=['Bag', 'Price']),
             buttons(('Buy Kiruga AA', '/shop/')))),
    align='wide', className='is-style-label', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    description='The signature coffee page layout: set out like the label on the bag.')

pattern('this-weeks-filter', 'This week\'s filter (front page label)', 'featured', columns(
    ('62%', J(para('This week\'s filter', fontSize='small', style={'typography': {'fontWeight': '800'}}), pattern_ref('coffee-label'))),
    (None, J(image('v60.jpg', 'Water poured from a copper kettle into a pour-over dripper on a white table', 'Kiruga through a V60, 15g to 250g.'),
             para('<a href="/v60-15g-to-250g/">The V60 recipe we use for it</a>', fontSize='small'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}, 'padding': {'bottom': 'var:preset|spacing|60'}}}))

pattern('coffee-list', 'What we\'re roasting (list)', 'shop', group(J(
    heading('What we\'re roasting', 2),
    table([['<a href="/shop/">Kiruga AA</a>', 'Kenya', 'Washed', 'Blackcurrant, grapefruit', '£12.50', 'In stock'],
           ['<a href="/shop/">Hambela Wamena</a>', 'Ethiopia', 'Natural', 'Strawberry, milk chocolate', '£11.00', 'In stock'],
           ['<a href="/shop/">El Puente</a>', 'Honduras', 'Honey', 'Red apple, caramel', '£11.50', '1kg sold out'],
           ['<a href="/shop/">Hope Street espresso</a>', 'Brazil and Colombia', 'Natural and washed', 'Hazelnut, cocoa, orange', '£9.50', 'Always'],
           ['<a href="/shop/">La Palma y El Tucán</a>', 'Colombia', 'Anaerobic', 'Mango, rum, cinnamon', '£16.00', '14 bags left']],
          head=['Coffee', 'Origin', 'Process', 'Notes', '250g', 'Stock'], caption='Prices per 250g bag. The bag fits through a UK letterbox.'),
    para('We don\'t sell decaf. We haven\'t found one we like enough yet, and we\'ve tried.', fontSize='small')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}))

pattern('bag-sizes', 'Bag sizes with sold-out state', 'shop', table(
    [['250g', '£11.50', 'In stock'], ['1kg', '£41.00', '<strong>Sold out</strong>, back after the Tuesday roast']], head=['Size', 'Price', 'Stock']))

pattern('letterbox-note', 'Fits through your letterbox', 'shop', group(para('<strong>250g bags fit through a UK letterbox.</strong> They\'re 16 × 23 × 3.5 cm flat, so they come Royal Mail Large Letter and you don\'t need to be in. 1kg bags need a signature.', fontSize='small'), className='is-style-pale-kraft', style={'spacing': {'padding': P(40)}}))

pattern('roast-day-line', 'Roast-day line (on a product)', 'shop', para('Roasted Tuesdays and Fridays, posted the same afternoon. Roast date printed on the bag.', fontSize='small', textColor='accent'))

pattern('producer-story', 'Producer story', 'about', columns(
    ('45%', image('green.jpg', 'Workers sorting red coffee cherries on blue tarpaulins outside a washing station', 'Hand-sorting cherries at the washing station before pulping.')),
    (None, J(heading('Kiruga washing station, Nyeri', 3),
             para('Kiruga is run by a farmers\' cooperative of about 900 members, most with fewer than 300 trees. Cherries are delivered in the afternoon, sorted by hand, pulped and fermented twice before drying on raised beds for 12 to 18 days.'),
             para('We buy through Falcon Specialty and have bought from Kiruga three years running. The factory manager, Joseph Mwangi, sends us photos of the drying beds, which is how we know the harvest is late this year.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('process-steps', 'Process notes (plain steps)', 'about', J(
    heading('What "washed, double fermented" means', 3),
    lst(['Ripe cherries are picked and sorted by hand.', 'The skin and fruit are pulped off the seed.', 'The seeds ferment in tanks for about 24 hours, are washed, then ferment again under clean water.', 'They dry on raised beds for 12 to 18 days, turned by hand.', 'The dried parchment rests for a month before milling and export.'], ordered=True)))

pattern('prices-we-pay', 'Prices we pay (table)', 'about', J(
    table([['Kiruga AA', 'Kenya', '$6.10', 'Falcon Specialty', '3rd year'], ['Hambela Wamena', 'Ethiopia', '$5.40', 'Osito', '2nd year'], ['El Puente', 'Honduras', '$5.90', 'Direct, with Marysabel Caballero', '4th year'],
           ['Hope Street base (Brazil)', 'Brazil', '$3.85', 'Mercanta', '1st year'], ['La Palma y El Tucán', 'Colombia', '$11.20', 'La Palma y El Tucán', '1st year']],
          head=['Coffee', 'Origin', 'FOB per kg', 'Bought through', 'Relationship'], caption='What we paid per kilo of green coffee, free on board, for this season\'s lots.'),
    para('FOB is the price at the port, before shipping. The Fairtrade minimum for washed arabica is $1.98/kg. We publish every price we pay because we\'d want to know.', fontSize='small')))

pattern('prices-page', 'Page: prices we pay', 'about', J(pattern_ref('prices-we-pay'), pattern_ref('producer-story'), pattern_ref('process-steps')), block_types='core/post-content')

# Signature: brew guide
def guide_facts(dose, water, temp, grind, time_):
    return table([['Dose', dose], ['Water', water], ['Temperature', temp], ['Grind', grind], ['Total time', time_]], className='is-style-data')

V60_SCHED = [['0:00', 'Pour 50g to bloom. Swirl the dripper so everything is wet.', '50g'], ['0:45', 'Pour in slow circles to 150g.', '150g'], ['1:15', 'Pour to 250g, keeping the level steady.', '250g'],
             ['1:45', 'Give it one gentle swirl to flatten the bed.', '250g'], ['3:00', 'Drawdown should finish around here. Much later: grind coarser.', 'Done']]
pattern('brew-guide', 'Brew guide (dose, grind, timed pours)', 'brew,featured', J(
    columns(('38%', J(heading('What you need', 4), guide_facts('15g coffee', '250g water', '94°C, just off the boil', 'Medium-fine, like table salt', '3:00'))),
            (None, J(heading('Pour schedule', 4), schedule(V60_SCHED, 'Start the timer when the first water hits the coffee.')))),
    heading('If it tastes wrong', 4),
    lst(['Sour or thin: grind finer, or pour more slowly.', 'Bitter or dry: grind coarser, or use water a little cooler.', 'Still odd: rinse the paper filter with hot water first. It tastes of paper otherwise.'])),
    description='The signature pattern. Edit the facts and the times; the timeline table keeps the times in the display face.')

pattern('pour-schedule', 'Pour schedule (timeline only)', 'brew', schedule(V60_SCHED))
pattern('brew-guides-grid', 'Brew guides (grid)', 'brew,query', group(J(
    row(J(heading('Brew guides', 2), para('<a href="/brew-guides/">All guides</a>', fontSize='small')), justify='space-between'),
    q(guide_card, per_page=6, qid=2, layout=GRID(3), pt_class='is-style-guide-list')),
    align='wide', layout={'type': 'default'}, className='is-style-rule-top', style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}))

# Subscriptions
pattern('subscription-builder', 'Subscription builder (coffee × frequency)', 'shop,featured', group(J(
    heading('Subscriptions', 2),
    columns(
        (None, J(heading('1. Pick a coffee', 4), table([['Roaster\'s choice filter', 'A different coffee each time', '£11 per 250g'], ['Hope Street espresso', 'Always the same', '£9.50 per 250g'], ['One of each', 'Filter and espresso', '£20 per delivery']], head=['Coffee', 'What you get', 'Price']))),
        (None, J(heading('2. Pick how often', 4), table([['Weekly', 'Every Tuesday'], ['Fortnightly', 'Every other Tuesday'], ['Monthly', 'First Tuesday of the month'], ['Custom', 'Any number of days from 10 to 60']], head=['Frequency', 'Posted']))),
        style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
    para('Postage is included. The first bag goes out on the next roast day.', fontSize='small'),
    buttons(('Start a subscription', '/subscriptions/'))),
    align='wide', className='is-style-kraft', layout={'type': 'default'}))

pattern('subscription-selfservice', 'Pause, skip or add a one-off', 'shop', J(
    heading('Change it whenever', 3),
    lst(['Skip a delivery: reply to the dispatch email before 10am on roast day.', 'Pause: for up to three months, from your account page.', 'Add a one-off: anything from the shop, posted with your next bag, no extra postage.', 'Cancel: from your account page, or email us. No notice period.'])))

pattern('subscriptions-page', 'Page: subscriptions', 'shop', J(
    para('A bag of fresh coffee, on the schedule you choose, through your letterbox. Most people start fortnightly and change it after a month.', fontSize='large'),
    pattern_ref('subscription-builder'), pattern_ref('subscription-selfservice'), pattern_ref('letterbox-note'),
    details('Can I send one as a gift?', para('Yes. Gift subscriptions run for 3, 6 or 12 deliveries and stop on their own. We include a card with your message.')),
    details('Do you post outside the UK?', para('Only to Ireland and the EU, at £7.50 a bag, and only fortnightly or monthly.')), pattern_ref('subscription-steps'), pattern_ref('gift-subscription'), pattern_ref('gift-card')), block_types='core/post-content')

# Wholesale and cafés
pattern('wholesale-prices', 'Wholesale price list', 'shop', J(
    table([['Hope Street espresso', '£21.00', '£19.50', '£18.00'], ['Seasonal filter', '£27.00', '£25.00', 'Ask'], ['Guest espresso', '£26.00', '£24.00', 'Ask']],
          head=['Coffee (per kg)', 'Under 10kg a week', '10 to 25kg', 'Over 25kg'], caption='Autumn 2026 prices, excluding VAT. Updated each season.'),
    para('<a href="https://example.com/lintel-wholesale-autumn-2026.pdf">Download the price list (PDF, 2 pages)</a>', fontSize='small')))

pattern('wholesale-page', 'Page: wholesale', 'shop', J(
    para('We supply eleven cafés and two offices in Merseyside. We\'d like a few more, but not many: we visit every account at least once a month to check grinders and taste.', fontSize='large'),
    pattern_ref('wholesale-prices'),
    lst(['Minimum order 5kg a week, delivered free within 15 miles of the roastery.', 'Free barista training at the roastery, two hours, up to four people.', 'We don\'t lend espresso machines. We\'ll recommend an engineer who services them.']),
    buttons(('Email Ade about wholesale', 'mailto:ade@example.com?subject=Wholesale')), pattern_ref('wholesale-steps'), pattern_ref('training-card'), pattern_ref('cafe-quote')), block_types='core/post-content')

pattern('cafes-list', 'Where to drink it (cafés and hours)', 'contact', table([
    ['The roastery', 'Unit 4, Hope Street Yard, L1 9BQ', 'Sat 9am to 1pm', 'Filter and beans only'],
    ['Bold Street Coffee', 'Bold Street, L1', 'Mon to Sun 8am to 5pm', 'Our espresso'],
    ['Ropewalks Canteen', 'Seel Street, L1', 'Tue to Sat 9am to 4pm', 'Guest filter'],
    ['Lark Lane Bakery', 'Lark Lane, L17', 'Wed to Sun 8am to 2pm', 'Our espresso']],
    head=['Where', 'Address', 'Hours', 'Pouring'], caption='Places that serve our coffee. Hours change; check with them.'))

pattern('cafes-and-wholesale', 'Cafés and wholesale (front page)', 'contact', columns(
    ('55%', J(heading('Drink it before you buy it', 2), pattern_ref('cafes-list'))),
    (None, J(image('roaster.jpg', 'A black drum coffee roaster with a cooling tray in a brick-walled roastery'),
             para('The roastery is open on Saturday mornings. Come and taste whatever we roasted on Friday. Card only, no seating, dogs fine.', fontSize='small'),
             buttons(('Wholesale for cafés', '/wholesale/', {'className': 'is-style-outline'})))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}))

pattern('cafes-page', 'Page: where to drink it', 'visit', J(pattern_ref('cafes-list'), pattern_ref('roastery-visit'), image('cafe.jpg', 'Two baristas working behind a café counter in front of big windows', 'Saturday morning at the roastery bar.')), block_types='core/post-content')

pattern('gift-card', 'Gift card', 'shop', group(J(
    heading('Gift cards', 3), para('£20, £40 or £60, sent by email with your message. They never expire and work on subscriptions too.'),
    buttons(('Buy a gift card', '/shop/'))), className='is-style-label'))

pattern('about-page', 'Page: about the roastery', 'about', J(
    columns(('45%', image('cupping.jpg', 'People in lab coats cupping rows of coffee at a long bench', 'Cupping at the Ethiopian Commodity Exchange lab, 2024.')),
            (None, J(para('Lintel is two people, Ade Okonjo and Freya Lund, and one Giesen W15 in a railway arch off Hope Street. We started in 2019 roasting 5kg batches for friends and now roast about 300kg a week.', fontSize='large'),
                     para('We cup every lot three times before we buy it, and once more after every roast. If a coffee isn\'t tasting right, we take it off the shop rather than blend it away.'),
                     para('We think most coffee is roasted too dark. Ours is light for filter and medium for espresso, and we\'ll tell you if we think you\'d like something else.'))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('team'), pattern_ref('prices-we-pay')), block_types='core/post-content')

# ---------------- round 2: fewer tables, a bigger kit
section('square', 'Square crop', ['core/image'], {'css': '& img{aspect-ratio:1;object-fit:cover;width:100%}'})
section('dl', 'Label data rows', ['core/group'], {
    'border': {'width': '1.5px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'css': '&>*{margin:0!important}&>.wp-block-columns{border-bottom:1.5px solid var(--wp--preset--color--contrast);margin:0!important;gap:0!important}&>.wp-block-columns:last-child{border-bottom:0}& .wp-block-column{padding:.45em .7em}& .wp-block-column:first-child{background:var(--wp--preset--color--surface-2);font-weight:800;border-right:1.5px solid var(--wp--preset--color--contrast)}& p{margin:0}'})
section('card', 'Boxed card', ['core/group'], {'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'spacing': {'padding': P(40)}})
section('ruled', 'Ruled row', ['core/columns', 'core/group'], {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1.5px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}, 'css': '& p{margin:0}'})

def dl(rows):
    return group(J(*[columns(('38%', para(k, fontSize='small')), (None, para(v, fontSize='small')), isStackedOnMobile=False) for k, v in rows]), className='is-style-dl', style={'spacing': {'blockGap': '0'}})

def rrow(cells, widths):
    return columns(*[(w, para(c, fontSize='small', style={'typography': {'fontWeight': '800'}} if i == 0 else {})) for i, (w, c) in enumerate(zip(widths, cells))], className='is-style-ruled', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}, 'margin': {'top': '0', 'bottom': '0'}}})

pattern('coffee-label', 'Coffee label (data box and tasting notes)', 'coffee', columns(
    ('55%', J(heading('Kiruga AA', 2, fontSize='xx-large'), dl(KIRUGA))),
    (None, J(heading('Tastes like', 4), para('Blackcurrant, pink grapefruit, a bit of tomato', className='is-style-notes-big'),
             para('Roasted light for filter. Rest it 7 days after the roast date on the bag.', fontSize='small'),
             pattern_ref('bag-sizes'),
             buttons(('Buy Kiruga AA', '/shop/')))),
    align='wide', className='is-style-label', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    description='The signature coffee layout, set out like the label on the bag.')

pattern('bag-sizes', 'Bag sizes with sold-out state', 'coffee', group(J(rrow(['250g', '£12.50', 'In stock'], ['5rem', '6rem', None]), rrow(['1kg', '£44.00', 'Sold out, back after Tuesday\'s roast'], ['5rem', '6rem', None])), style={'spacing': {'blockGap': '0'}}))

COFFEES = [('roasted.jpg', 'Roasted coffee beans', 'Kiruga AA', 'Kenya, washed', 'Blackcurrant, grapefruit', '£12.50'),
           ('green.jpg', 'Workers sorting coffee cherries', 'Hambela Wamena', 'Ethiopia, natural', 'Strawberry, milk chocolate', '£11.00'),
           ('sacks.jpg', 'Stacked jute coffee sacks', 'El Puente', 'Honduras, honey', 'Red apple, caramel', '£11.50'),
           ('machine.jpg', 'A barista at a lever espresso machine', 'Hope Street espresso', 'Brazil and Colombia', 'Hazelnut, cocoa, orange', '£9.50'),
           ('cupping.jpg', 'Tasters cupping coffee at a bench', 'La Palma y El Tucán', 'Colombia, anaerobic', 'Mango, rum, cinnamon', '£16.00')]
def coffee_card(img, alt, name, origin, notes, price):
    return group(J(image(img, alt, className='is-style-square'), heading(name, 3, fontSize='large'), para(origin, fontSize='x-small', textColor='accent', style={'typography': {'fontWeight': '800'}}), para(notes, fontSize='small'), para('%s per 250g' % price, fontSize='small', style={'typography': {'fontWeight': '800'}})),
                 style={'spacing': {'blockGap': 'var:preset|spacing|20'}})
pattern('coffee-list', 'What we\'re roasting (cards)', 'coffee', group(J(
    row(J(heading('What we\'re roasting', 2), para('<a href="/shop/">Shop all coffee</a>', fontSize='small')), justify='space-between'),
    grid(J(*[coffee_card(*c) for c in COFFEES]), min_width='12rem', style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
    para('Every 250g bag fits through a UK letterbox. We don\'t sell decaf: we haven\'t found one we like enough yet, and we\'ve tried.', fontSize='small')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}))

def option(title, sub, price, cls='is-style-card'):
    return group(J(heading(title, 4), para(sub, fontSize='small'), para(price, style={'typography': {'fontWeight': '800'}}, textColor='accent')), className=cls)
pattern('subscription-options', 'Subscription: pick a coffee', 'subscriptions', J(
    heading('1. Pick a coffee', 4),
    grid(J(option('Roaster\'s choice filter', 'A different coffee each time, light roast.', '£11 per 250g'), option('Hope Street espresso', 'Always the same. Works with milk.', '£9.50 per 250g'), option('One of each', 'Filter and espresso in one box.', '£20 per delivery')), min_width='12rem', style={'spacing': {'blockGap': 'var:preset|spacing|30'}})))
pattern('subscription-frequency', 'Subscription: pick how often', 'subscriptions', J(
    heading('2. Pick how often', 4),
    grid(J(option('Weekly', 'Every Tuesday.', 'Most popular with offices'), option('Fortnightly', 'Every other Tuesday.', 'About a bag a fortnight for two people'), option('Monthly', 'First Tuesday of the month.', 'For the weekend brewer'), option('Custom', 'Any gap from 10 to 60 days.', 'Set it in your account')), min_width='10rem', style={'spacing': {'blockGap': 'var:preset|spacing|30'}})))
pattern('subscription-builder', 'Subscription builder (coffee by frequency)', 'subscriptions', group(J(
    heading('Subscriptions', 2),
    pattern_ref('subscription-options'), pattern_ref('subscription-frequency'),
    para('Postage is included. The first bag goes out on the next roast day.', fontSize='small'),
    buttons(('Start a subscription', '/subscriptions/'))),
    align='wide', className='is-style-kraft', layout={'type': 'default'}))

CAFES = [('The roastery', 'Unit 4, Hope Street Yard, L1 9BQ', 'Sat 9am to 1pm', 'Filter and beans only'), ('Bold Street Coffee', 'Bold Street, L1', 'Every day 8am to 5pm', 'Our espresso'),
         ('Ropewalks Canteen', 'Seel Street, L1', 'Tue to Sat 9am to 4pm', 'Guest filter'), ('Lark Lane Bakery', 'Lark Lane, L17', 'Wed to Sun 8am to 2pm', 'Our espresso')]
pattern('cafes-list', 'Where to drink it (cafés and hours)', 'visit', grid(J(*[group(J(heading(n, 4), para(a, fontSize='small'), para(h, fontSize='small', style={'typography': {'fontWeight': '800'}}), para(p_, fontSize='x-small', textColor='accent')), className='is-style-card') for n, a, h, p_ in CAFES]),
    min_width='10rem', style={'spacing': {'blockGap': 'var:preset|spacing|30'}}))

pattern('roast-log', 'This week\'s roast log', 'coffee', group(J(
    heading('On the roaster this week', 3),
    rrow(['Tuesday', 'Kiruga AA, Hambela Wamena, Hope Street espresso', '86kg'], ['8rem', None, '5rem']),
    rrow(['Friday', 'El Puente, La Palma y El Tucán, Hope Street espresso', '92kg'], ['8rem', None, '5rem']),
    para('Roast dates are printed on every bag. Filter is best from day 7 to day 30.', fontSize='x-small', textColor='muted')), style={'spacing': {'blockGap': '0'}}))

pattern('brewer-picker', 'Pick your brewer (links to guides)', 'brew', grid(J(
    *[group(J(image(img, alt, href=href), heading('<a href="%s">%s</a>' % (href, t), 4)), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}) for img, alt, t, href in [
        ('v60.jpg', 'Pouring water into a pour-over dripper', 'V60', '/v60-15g-to-250g/'), ('aeropress.jpg', 'An AeroPress kit laid out on wood', 'AeroPress', '/aeropress-inverted/'),
        ('moka.jpg', 'A moka pot on a wooden table', 'Moka pot', '/moka-pot/'), ('machine.jpg', 'A lever espresso machine', 'Espresso', '/espresso-hope-street/')]]),
    min_width='10rem', align='wide', style={'spacing': {'blockGap': 'var:preset|spacing|40'}}))

pattern('grind-guide', 'Grind sizes by brewer', 'brew', group(J(
    heading('How fine to grind', 3),
    rrow(['Espresso', 'Fine, like icing sugar with a bit of grit'], ['9rem', None]), rrow(['Moka pot', 'Fine, a bit coarser than espresso'], ['9rem', None]),
    rrow(['AeroPress', 'Medium, like caster sugar'], ['9rem', None]), rrow(['V60', 'Medium-fine, like table salt'], ['9rem', None]),
    rrow(['Batch brewer', 'Medium-coarse, like sand'], ['9rem', None]), rrow(['Cafetière', 'Coarse, like sea salt'], ['9rem', None])), style={'spacing': {'blockGap': '0'}}))

pattern('water-guide', 'Water for brewing', 'brew', group(J(
    heading('Water matters more than you think', 3),
    para('Liverpool tap water is soft, which suits light roasts. If your kettle furs up, use a jug filter or bottled water with low minerals. Don\'t use distilled water: the coffee tastes flat.'),
    para('Use water just off the boil for light roasts and a minute off the boil for darker ones.', fontSize='small')), className='is-style-pale-kraft'))

pattern('equipment-cards', 'Brewing kit (cards)', 'shop', grid(J(
    *[group(J(image(i, a), heading(t, 4), para(d, fontSize='small'), para(p_, style={'typography': {'fontWeight': '800'}})), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}) for i, a, t, d, p_ in [
        ('v60.jpg', 'A ceramic V60 dripper in use', 'V60 02 ceramic', 'One or two cups. Use 02 papers.', '£24'), ('aeropress.jpg', 'An AeroPress with filters', 'AeroPress Original', 'With 350 papers. Hard to break.', '£35'),
        ('moka.jpg', 'An aluminium moka pot', 'Moka pot, 3 cup', 'Aluminium, for gas or electric.', '£28')]]),
    min_width='12rem', align='wide', style={'spacing': {'blockGap': 'var:preset|spacing|40'}}))

pattern('producer-cards', 'Producers we buy from', 'origin', grid(J(
    *[group(J(heading(n, 4), para(w, fontSize='x-small', textColor='accent', style={'typography': {'fontWeight': '800'}}), para(t, fontSize='small')), className='is-style-card') for n, w, t in [
        ('Kiruga cooperative', 'Nyeri, Kenya, 3rd year', 'About 900 members, most with under 300 trees. Double-fermented washed coffees.'),
        ('Marysabel Caballero', 'Marcala, Honduras, 4th year', 'A family farm we buy from directly. Honey and washed lots.'),
        ('Hambela Wamena station', 'Guji, Ethiopia, 2nd year', 'Natural coffees dried on raised beds for about three weeks.')]]),
    min_width='13rem', style={'spacing': {'blockGap': 'var:preset|spacing|30'}}))

pattern('subscription-steps', 'How a subscription works', 'subscriptions', J(
    heading('How it works', 3),
    lst(['Pick a coffee and how often.', 'We roast on Tuesday and post it the same afternoon, Royal Mail Large Letter.', 'It fits through your letterbox. Rest filter coffee for a week before brewing.', 'Change, skip or pause from the dispatch email or your account.'], ordered=True)))

pattern('gift-subscription', 'Gift subscription', 'subscriptions', columns(
    ('40%', image('aeropress.jpg', 'An AeroPress kit laid out with beans on a scale')),
    (None, J(heading('Give it as a present', 3), para('3, 6 or 12 deliveries, then it stops on its own. We add a card with your message and the first bag goes out on the next roast day. From £33 for three bags.'), buttons(('Buy a gift subscription', '/shop/')))),
    verticalAlignment='center'))

pattern('wholesale-steps', 'Wholesale: how we start', 'wholesale', J(
    heading('How we start with a new café', 3),
    lst(['You email Ade with what you pour now and how much a week.', 'We bring two espressos and a filter to taste on your machine.', 'If you like one, we set up a standing order and a delivery day.', 'Freya comes back after a month to check grinders and recipes.'], ordered=True)))

pattern('training-card', 'Barista training', 'wholesale', group(J(
    heading('Barista training', 3), para('Two hours at the roastery for up to four people from a wholesale account: dialling in, milk and cleaning. Free for accounts, £60 a head otherwise.'),
    buttons(('Book training by email', 'mailto:freya@example.com?subject=Training'))), className='is-style-card'))

pattern('cafe-quote', 'A café we supply (quote)', 'wholesale', quote('They came in and fixed our grinder settings before they tried to sell us anything. We switched a month later.', 'Nadia Hussain, Ropewalks Canteen, customer since 2023'))

pattern('faq', 'Questions people email us', 'faq', J(
    heading('Questions people email us', 3),
    details('Whole bean or ground?', para('Whole bean by default. We grind to order for V60, AeroPress, cafetière or espresso if you ask in the order notes.')),
    details('How long does coffee keep?', para('Best from about a week to a month after roasting. Keep the bag sealed, away from light. Not in the fridge.')),
    details('Do you ship abroad?', para('Ireland and the EU only, at £7.50 a bag.')),
    details('Can I visit?', para('Saturdays 9am to 1pm. Card only, no seating, dogs fine.'))))

pattern('roastery-visit', 'Visit the roastery', 'visit', columns(
    ('50%', image('roaster.jpg', 'A black drum coffee roaster in a brick-walled roastery')),
    (None, J(heading('Come to the roastery', 3), para('Unit 4, Hope Street Yard, Liverpool L1 9BQ. Through the gate and it\'s the arch with the green door.'),
             para('Saturdays 9am to 1pm. We pour whatever we roasted on Friday and sell bags at the door. Card only.', style={'typography': {'fontWeight': '800'}}),
             para('Step-free from the yard. The nearest station is Liverpool Central, 8 minutes\' walk.', fontSize='small'))),
    verticalAlignment='center'))

pattern('team', 'The people', 'about', grid(J(
    group(J(heading('Ade Okonjo', 4), para('Roaster and buyer. Cups every lot three times before we buy it. Handles wholesale.', fontSize='small')), className='is-style-card'),
    group(J(heading('Freya Lund', 4), para('Roaster and trainer. Visits every café account once a month with a refractometer.', fontSize='small')), className='is-style-card'),
    group(J(heading('Sam Whitfield', 4), para('Packs and posts every order, Tuesdays and Fridays. Also fixes the roaster.', fontSize='small')), className='is-style-card')), min_width='12rem', style={'spacing': {'blockGap': 'var:preset|spacing|30'}}))

pattern('notice-holiday', 'Notice: roastery closed', 'banner', group(
    para('The roastery is closed 24 December to 4 January. Subscriptions pause automatically and restart on 5 January.', align='center'),
    align='full', className='is-style-stamp', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}))

pattern('brewing-kit-page', 'Page: brewing kit', 'brew', J(
    para('The kit we use at the roastery and sell in the shop. You don\'t need much: a scale, a kettle and one brewer.', fontSize='large'),
    pattern_ref('equipment-cards'), pattern_ref('brewer-picker'), columns((None, pattern_ref('grind-guide')), (None, pattern_ref('water-guide')), align='wide'), pattern_ref('faq')), block_types='core/post-content')

print('roast: patterns written')

# ---------------- demo content
def guide_post(title, slug, img, excerpt, facts, sched, fixes):
    return dict(title=title, slug=slug, category='brew-guides', tags=['Brew guide'], image=img, excerpt=excerpt, template='single-brew-guide',
                content=J(columns(('38%', J(heading('What you need', 4), guide_facts(*facts))), (None, J(heading('Pour schedule', 4), schedule(sched, 'Start the timer when the water first hits the coffee.'))), style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
                          heading('If it tastes wrong', 4), lst(fixes)))

posts = [
    guide_post('V60, 15g to 250g', 'v60-15g-to-250g', 'v60.jpg', 'One cup, three minutes. Our house recipe for light filter coffee.',
               ('15g coffee', '250g water', '94°C', 'Medium-fine, like table salt', '3:00'), V60_SCHED,
               ['Sour or thin: grind finer.', 'Bitter or dry: grind coarser.', 'Rinse the paper first, or it tastes of paper.']),
    guide_post('AeroPress, upside down', 'aeropress-inverted', 'aeropress.jpg', 'Our recipe for one strong cup, and the one we take camping.',
               ('14g coffee', '200g water', '88°C', 'Medium, like caster sugar', '2:00'),
               [['0:00', 'Plunger in at the 4 mark, upside down. Add coffee, pour 200g water.', '200g'], ['0:10', 'Stir three times. Cap on with a rinsed filter.', '200g'], ['1:30', 'Flip onto the cup.', '200g'], ['1:30', 'Press gently for 30 seconds. Stop at the hiss.', 'Done']],
               ['Too strong: add 50g hot water to the cup.', 'Muddy: grind coarser and press more slowly.']),
    guide_post('Moka pot, the way it should be done', 'moka-pot', 'moka.jpg', 'Start with hot water and take it off the heat early. It stops the burnt taste.',
               ('17g coffee (fill the basket, don\'t tamp)', 'Water from the kettle to just under the valve', 'Just boiled', 'Fine, but coarser than espresso', 'About 4:00'),
               [['0:00', 'Fill the base with just-boiled water. Add the basket and coffee, screw on the top with a towel.', ''], ['0:30', 'Medium heat, lid open.', ''], ['3:00', 'Coffee starts to come through, dark and slow.', ''], ['3:45', 'It turns pale and starts to gurgle: take it off and run the base under cold water.', 'Done']],
               ['Burnt taste: take it off sooner.', 'Weak: grind a little finer. Never tamp.']),
    guide_post('Espresso, Hope Street recipe', 'espresso-hope-street', 'machine.jpg', '18g in, 40g out, in 28 to 32 seconds. What we tell our cafés.',
               ('18g coffee', '40g espresso out', '93°C', 'Fine, dial in by time', '0:30'),
               [['0:00', 'Start the shot as soon as the portafilter is in.', '0g'], ['0:07', 'First drops. Much earlier: grind finer.', '2g'], ['0:20', 'Steady flow, like warm honey.', '25g'], ['0:30', 'Stop at 40g in the cup.', '40g']],
               ['Sour and fast: grind finer.', 'Bitter and slow: grind coarser.', 'Rest the beans 10 days after roasting for espresso.']),
    guide_post('Batch brewer, for offices', 'batch-brewer', 'cafe.jpg', 'The recipe our office customers use in a Moccamaster.',
               ('60g coffee', '1 litre water', 'Machine default', 'Medium-coarse', '6:00'),
               [['0:00', 'Rinse the paper, add coffee, fill the tank to 1 litre, switch on.', ''], ['0:40', 'Give the grounds a stir with a spoon once they\'re wet.', ''], ['6:00', 'Brew finishes. Stir the jug before pouring.', 'Done']],
               ['Keep it on the hot plate for 30 minutes at most.', 'Descale monthly. Liverpool water is soft, but not that soft.']),
    guide_post('Cupping at home', 'cupping-at-home', 'cupping.jpg', 'How we taste every roast, scaled down for a kitchen table.',
               ('12g coffee per cup', '200g water', '94°C', 'Medium-coarse', '14:00'),
               [['0:00', 'Pour water over the grounds to the top. Start the timer.', '200g'], ['4:00', 'Break the crust with a spoon and smell it.', ''], ['5:00', 'Skim the foam off with two spoons.', ''], ['10:00', 'Slurp from a spoon. Taste again as it cools.', 'Done']],
               ['Taste two coffees side by side. One on its own tells you very little.']),
    dict(title='The prices we paid this season', slug='prices-this-season', category='journal', tags=['Sourcing'], image='sacks.jpg', excerpt='Five coffees, five prices, and why the Colombian costs almost twice as much.',
         content=J(para('Every autumn we publish what we paid for green coffee. This year the range is $3.85 to $11.20 per kilo, FOB.'), pattern_ref('prices-we-pay'),
                   para('The expensive one is La Palma y El Tucán, an anaerobic lot from Cundinamarca. It\'s a treat coffee and we sell it at £16 a bag with a smaller margin than the others.'))),
    dict(title='Why we roast on Tuesdays and Fridays', slug='roast-days', category='journal', tags=['Roastery'], image='roasted.jpg', excerpt='Two roast days means nothing sits on a shelf for more than three days before it\'s posted.',
         content=J(para('Roasting twice a week means every bag goes out within three days of roasting. Filter coffee tastes best from about day 7 to day 30, so it arrives just before it\'s ready.'), para('The other days we cup, pack wholesale orders and clean the roaster. Friday afternoons are for the chaff collector, which nobody enjoys.'))),
]

EXTRA = {'v60-15g-to-250g': ['grind-guide', 'water-guide'], 'aeropress-inverted': ['equipment-cards'], 'espresso-hope-street': ['roast-log'],
         'prices-this-season': ['producer-cards'], 'roast-days': ['roast-log', 'team']}
for p_ in posts:
    p_['content'] = J(p_['content'], *[pattern_ref(x) for x in EXTRA.get(p_['slug'], [])])

products = [
    {'name': 'Kiruga AA, Kenya, 250g', 'price': '12.50', 'image': 'roasted.jpg', 'category': 'Coffee', 'sku': 'LIN-KIR-250', 'stock': 40, 'short': 'Washed, Nyeri. Blackcurrant, pink grapefruit, a bit of tomato. Roasted for filter.'},
    {'name': 'Hambela Wamena, Ethiopia, 250g', 'price': '11.00', 'image': 'green.jpg', 'category': 'Coffee', 'sku': 'LIN-HAM-250', 'stock': 36, 'short': 'Natural, Guji. Strawberry and milk chocolate. Roasted for filter.'},
    {'name': 'El Puente, Honduras, 1kg', 'price': '41.00', 'image': 'sacks.jpg', 'category': 'Coffee', 'sku': 'LIN-PUE-1K', 'stock': 0, 'short': 'Honey process. Red apple, caramel. Sold out, back after Tuesday\'s roast.'},
    {'name': 'Hope Street espresso, 250g', 'price': '9.50', 'image': 'machine.jpg', 'category': 'Coffee', 'sku': 'LIN-HSE-250', 'stock': 80, 'short': 'Brazil and Colombia. Hazelnut, cocoa, orange. Works with milk.'},
    {'name': 'La Palma y El Tucán, Colombia, 250g', 'price': '16.00', 'image': 'cupping.jpg', 'category': 'Coffee', 'sku': 'LIN-LPT-250', 'stock': 14, 'short': 'Anaerobic. Mango, rum, cinnamon. A treat.'},
    {'name': 'V60 02 ceramic dripper', 'price': '24.00', 'image': 'v60.jpg', 'category': 'Equipment', 'sku': 'LIN-EQ-V60', 'stock': 12, 'short': 'White ceramic, makes one or two cups. Use 02 papers.'},
    {'name': 'V60 02 paper filters, 100', 'price': '6.00', 'image': 'v60.jpg', 'category': 'Equipment', 'sku': 'LIN-EQ-PAP', 'stock': 50, 'short': 'Unbleached. Rinse before use.'},
    {'name': 'AeroPress Original', 'price': '35.00', 'image': 'aeropress.jpg', 'category': 'Equipment', 'sku': 'LIN-EQ-AER', 'stock': 8, 'short': 'Comes with 350 papers. See the upside-down recipe in the brew guides.'},
]

content = {
    'site': {'title': 'Lintel Coffee', 'tagline': 'Roasted in Liverpool on Tuesdays and Fridays'},
    'categories': [{'slug': 'brew-guides', 'name': 'Brew guides'}, {'slug': 'journal', 'name': 'Journal'}],
    'front_page': 'home', 'posts_page': 'brew-guides',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'brew-guides', 'title': 'Brew guides', 'content': ''},
        {'slug': 'subscriptions', 'title': 'Subscriptions', 'pattern': 'roast/subscriptions-page', 'template': 'page-wide'},
        {'slug': 'wholesale', 'title': 'Wholesale', 'pattern': 'roast/wholesale-page'},
        {'slug': 'cafes', 'title': 'Where to drink it', 'pattern': 'roast/cafes-page', 'template': 'page-wide'},
        {'slug': 'prices-we-pay', 'title': 'Prices we pay', 'pattern': 'roast/prices-page', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About the roastery', 'pattern': 'roast/about-page', 'template': 'page-wide'},
        {'slug': 'brewing-kit', 'title': 'Brewing kit', 'pattern': 'roast/brewing-kit-page', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'Subscriptions', 'url': '/subscriptions/'}, {'label': 'Brew guides', 'url': '/brew-guides/'},
            {'label': 'Brewing kit', 'url': '/brewing-kit/'}, {'label': 'Wholesale', 'url': '/wholesale/'}, {'label': 'Prices we pay', 'url': '/prices-we-pay/'}, {'label': 'About', 'url': '/about/'}],
    'currency': 'GBP',
    'products': products,
}
os.makedirs(os.path.join(ROOT, 'demos', S), exist_ok=True)
with open(os.path.join(ROOT, 'demos', S, 'content.json'), 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
print('roast: content.json written')
