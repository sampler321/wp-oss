# Design note (kiln, idea 006, ceramicist: shop updates and kiln openings, WooCommerce)
# Direction: "glaze-test catalogue". The site is a noticeboard for the next shop update: the page opens on a
# full-bleed celadon slab with the next update date set huge, and the glazes are shown as square test tiles.
# Why: studio potters sell in scheduled drops, so the useful thing is "when can I buy", then what sold last time.
# Fonts: Zodiak 700 (display, registry) + General Sans (body, tabular figures for dates and prices). Two families only.
# Palette: porcelain #F4F3EF, clay black #23211E, celadon #2F5E6E (links, buttons, the status slab), tenmoku footer
# #3A2418, plus glaze tile colours (shino, ash, tenmoku, cobalt) as palette tokens.
# Layout idea: colour slabs instead of cards. Celadon status slab on top, square pots in a 3-up grid with sold ones
# dimmed and still listed, a row of square glaze tiles, a big per-day kiln opening timetable, tenmoku footer.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('kiln')
S = THEME['slug']


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

PALETTE = [
    ('base', '#F4F3EF', 'Porcelain'), ('contrast', '#23211E', 'Clay black'), ('accent', '#2F5E6E', 'Celadon'),
    ('accent-2', '#3A2418', 'Tenmoku'), ('surface', '#E6E2DA', 'Biscuit'), ('line', '#C8C1B4', 'Kiln shelf'),
    ('muted', '#5F5A52', 'Iron wash'), ('shino', '#E8D3B9', 'Shino'), ('ash', '#A3A283', 'Ash glaze'),
    ('cobalt', '#1D3F8C', 'Cobalt'), ('celadon-pale', '#BFD3C9', 'Pale celadon'),
]
focus = {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}

CSS = (
    ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
    '.wp-block-table,.is-style-price,.wc-block-components-product-price,.woocommerce-Price-amount{font-variant-numeric:tabular-nums lining-nums}'
    '.wp-block-table table.has-fixed-layout{table-layout:auto}'
    '.wp-block-table table td,.wp-block-table table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.7em 1.4em .7em 0;text-align:left;vertical-align:top;word-break:normal;overflow-wrap:break-word}'
    '.wp-block-table table.has-fixed-layout td,.wp-block-table table.has-fixed-layout th{word-break:normal;overflow-wrap:normal}.wp-site-blocks>footer{margin-block-start:0}'
    '.wc-block-product.outofstock .wc-block-components-product-price::after,li.product.outofstock .price::after{content:", sold out";font-weight:600}'
    '.wp-block-table table thead{border-bottom:0}.wp-block-table table thead th{border-bottom:2px solid currentColor;font-weight:600}'
    '.wp-block-group.is-style-glaze-tile{aspect-ratio:1;display:flex;flex-direction:column;justify-content:space-between}'
    '.wc-block-product.outofstock img,.wc-block-grid__product.is-sold-out img,li.product.outofstock img,.is-style-sold-out img{opacity:.6}'
    '.wc-block-product img,li.product img{aspect-ratio:1;object-fit:cover;background:var(--wp--preset--color--surface)}'
    '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-underline-offset:.35em;text-decoration-thickness:2px}'
    '@media (max-width:600px){.wp-block-group.is-style-glaze-tile{aspect-ratio:auto;min-height:9rem}}'
)

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1280px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': FONTS,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Small print', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Measurements', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.5rem', 'name': 'Title', 'fluid': {'min': '2.5rem', 'max': '3.5rem'}},
                {'slug': 'display', 'size': '5.25rem', 'name': 'Display', 'fluid': {'min': '3rem', 'max': '5.25rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6'},
        'spacing': {'padding': {'left': sp(40), 'right': sp(40)}, 'blockGap': sp(30)},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '1', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.1'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0', 'lineHeight': '1.35'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0', 'lineHeight': '1.4'}},
            'button': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                       'border': {'radius': '2px', 'width': '0', 'style': 'none'},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.85em', 'bottom': '0.85em', 'left': '1.4em', 'right': '1.4em'}},
                       ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}},
                       ':focus': focus},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.01em'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.3'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'left': sp(40)}},
                           'css': '& cite{display:block;margin-top:.8em;font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--small);font-style:normal;color:var(--wp--preset--color--muted)}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': sp(30), 'bottom': sp(30)}},
                             'css': '& summary{font-weight:600}'},
            'core/search': {'typography': {'fontSize': 'var:preset|font-size|small'},
                            'css': '& .wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:2px;background:var(--wp--preset--color--base)}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'header', 'name': 'header-plain', 'title': 'Header without the shop status bar'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-firing', 'title': 'Kiln log entry (wide photo)', 'postTypes': ['post']},
    ],
}
wjson('theme.json', theme)


def variation(title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}
    if extra:
        d['styles'] = extra
    return d

GLAZES = [('shino', '#E8D3B9', 'Shino'), ('ash', '#A3A283', 'Ash glaze'), ('cobalt', '#1D3F8C', 'Cobalt'), ('celadon-pale', '#BFD3C9', 'Pale celadon')]
wjson('styles/tenmoku.json', variation('Tenmoku', [
    ('base', '#3A2418', 'Tenmoku'), ('contrast', '#F1E9DC', 'Porcelain'), ('accent', '#9CC9C2', 'Celadon'),
    ('accent-2', '#23150E', 'Dark tenmoku'), ('surface', '#4A3124', 'Iron'), ('line', '#6B5040', 'Kiln shelf'),
    ('muted', '#D4C6B2', 'Oatmeal')] + GLAZES,
    {'elements': {'button': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}}}}))
wjson('styles/ash.json', variation('Ash', [
    ('base', '#D9D4C7', 'Wood ash'), ('contrast', '#2A2724', 'Clay black'), ('accent', '#2F5E6E', 'Celadon'),
    ('accent-2', '#3A2418', 'Tenmoku'), ('surface', '#CBC5B6', 'Biscuit'), ('line', '#A9A293', 'Kiln shelf'),
    ('muted', '#4F4A43', 'Iron wash')] + GLAZES))
wjson('styles/cobalt.json', variation('Cobalt', [
    ('base', '#FFFFFF', 'White slip'), ('contrast', '#1E1D1B', 'Clay black'), ('accent', '#1D3F8C', 'Cobalt'),
    ('accent-2', '#14295C', 'Deep cobalt'), ('surface', '#EEF0F4', 'Blue-white'), ('line', '#C6CBD6', 'Kiln shelf'),
    ('muted', '#545863', 'Slate')] + GLAZES))


def section(slug, title, blocks, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                             'title': title, 'slug': slug, 'blockTypes': blocks, 'styles': styles})

section('celadon-slab', 'Celadon slab', ['core/group', 'core/columns', 'core/cover'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'caption': {'color': {'text': 'var:preset|color|base'}},
                 'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|accent'},
                            ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}}}},
    'spacing': {'padding': {'top': sp(70), 'bottom': sp(70)}}})
section('tenmoku', 'Tenmoku (dark)', ['core/group'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}}}})
section('biscuit', 'Biscuit panel', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': sp(60), 'bottom': sp(60), 'left': sp(50), 'right': sp(50)}}})
section('glaze-tile', 'Glaze test tile', ['core/group'], {
    'spacing': {'padding': {'top': sp(30), 'bottom': sp(30), 'left': sp(30), 'right': sp(30)}},
    'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.35'}})
section('status-bar', 'Shop status bar', ['core/group'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}},
    'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
    'spacing': {'padding': {'top': sp(20), 'bottom': sp(20)}}})
section('square', 'Square crop', ['core/image'], {'css': '& img{aspect-ratio:1;object-fit:cover;width:100%}'})
section('sold-out', 'Sold out (dimmed photo)', ['core/group'], {'css': '& img{opacity:.6}'})
section('price', 'Price line', ['core/paragraph'], {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': sp(40)}}})

write('style.css', '''/*
Theme Name: Kiln
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A shop and kiln log for potters who sell in scheduled shop updates and at kiln-opening sales, and keep sold pots on show.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: kiln
Tags: e-commerce, portfolio, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

# ------------------------------------------------------------------ parts
NEXT = 'Sunday 18 October, 7pm UK time'
header_row = group(row(J(dyn('site-title', level=0),
                           row(dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}), justify='right', style={'spacing': {'blockGap': sp(30)}})),
                       justify='space-between', align='full'), align='full', layout={'type': 'default'}, style=pad(40, 40, 40, 40))
status_bar = group(para(align='wide', text='Shop closed apart from seconds. Next update: <strong>%s</strong>. Newsletter readers get the list two days before. <a href="/newsletter/">Get the email</a>' % NEXT),
                   className='is-style-status-bar', align='full')
write('parts/header.html', J(status_bar, header_row))
write('parts/header-plain.html', header_row)

write('parts/footer.html', group(J(
    columns(
        ('40%', J(heading('Lowfold Pottery', 2, fontSize='x-large'),
                  para('Nell Rigby makes wood-fired and gas-fired stoneware in a converted byre at the top of Dentdale. The shop opens four times a year, and the kiln opening is every spring and autumn.'))),
        (None, J(heading('Find the pottery', 6),
                 para('Lowfold, Cowgill<br>Dent, Cumbria LA10 5RL<br>Visits by appointment, phone first.<br>015396 25518'))),
        (None, J(heading('Orders and post', 6),
                 para('<a href="mailto:nell@example.com">nell@example.com</a><br>Pots are packed on Tuesdays and sent by Parcelforce. UK post £9.50 per order.<br><a href="/newsletter/">Newsletter</a>'))),
        align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}),
    para('Demo photographs are public domain and CC0 museum pieces from Wikimedia Commons, standing in for Nell\'s pots.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-tenmoku', style=pad(70, 50)))

# ------------------------------------------------------------------ data
POTS = [
    dict(n='Moon jar, white slip', img='moon-jar.jpg', p='640', stock=0, fir='41', size='H 38 cm, W 36 cm',
         clay='Stoneware, thrown in two halves and joined', glaze='White slip under a clear ash glaze', care='Holds dried flowers. Not watertight at the join, so no water.',
         alt='A large round white jar with a small neck, slightly lopsided, on a grey plinth'),
    dict(n='Tenmoku tea bowl', img='tea-bowl.jpg', p='85', stock=0, fir='41', size='H 7 cm, W 15 cm',
         clay='Iron-rich stoneware', glaze='Tenmoku breaking rust and brown at the rim', care='Dishwasher and microwave safe.',
         alt='A wide conical tea bowl in dark brown glaze with rust streaks and a pale foot ring'),
    dict(n='Stamped bowl, buncheong slip', img='bowl-stamped.jpg', p='120', stock=0, fir='40', size='H 8 cm, W 22 cm',
         clay='Grey stoneware, stamped and slip-inlaid', glaze='Clear celadon over white slip', care='Dishwasher safe. The crackle is part of the glaze and will darken with tea.',
         alt='A shallow bowl covered in tiny stamped white dots around a central stamped motif'),
    dict(n='Ash jar with lid', img='jar-ash.jpg', p='340', stock=0, fir='40', size='H 24 cm, W 25 cm',
         clay='Stoneware with deep throwing rings', glaze='Natural wood ash, runs green and amber', care='Food safe inside. Hand wash.',
         alt='A round ribbed jar with streaky tan and green glaze and a red lid'),
    dict(n='Tall mug, oak band', img='mug.jpg', p='42', stock=0, fir='41', size='H 12 cm, holds 350 ml',
         clay='Buff stoneware, pulled handle', glaze='Green ash over a carved band of trees', care='Dishwasher and microwave safe.',
         alt='A tall mug with a looped handle, glazed green-grey with a carved band of trees near the base'),
    dict(n='Teapot, brushed iron', img='teapot.jpg', p='190', stock=0, fir='40', size='H 13 cm, holds 800 ml',
         clay='Porcelain stoneware', glaze='White glaze with brushed iron decoration', care='Dishwasher safe. Pours clean, I test every one.',
         alt='A squat white teapot with loose brushed grey lines and a short spout'),
    dict(n='Bottle vase, wood-fired', img='vase-ash.jpg', p='220', stock=0, fir='41', size='H 22 cm, W 10 cm',
         clay='Unglazed stoneware', glaze='No glaze. Flashing from the fire only', care='Watertight. Wipe clean.',
         alt='A tall cylindrical unglazed vase, flashed red-brown and green where the flames hit it'),
    dict(n='Celadon bowl, carved', img='bowl-celadon.jpg', p='95', stock=2, fir='41', size='H 9 cm, W 19 cm',
         clay='Porcelain stoneware, carved at leather hard', glaze='Celadon, pooled green in the carving', care='Dishwasher safe.',
         alt='A deep bowl in grey-green celadon with carved leaves around the outside'),
    dict(n='Small cup, blue glaze', img='cup-jun.jpg', p='38', stock=5, fir='41', size='H 5 cm, holds 120 ml',
         clay='Stoneware', glaze='Pale blue chun, thick at the rim', care='Dishwasher safe. Seconds: a small glaze skip on the foot.',
         alt='A small pale blue cup with a scalloped rim and a little handle'),
]

def pot_desc(p):
    return ('<p>Firing %s. %s.</p><p>Size: %s.<br>Clay: %s.<br>Glaze: %s.<br>%s</p><p>Every pot is photographed on the same board, so the colour you see is close to the colour you get.</p>'
            % (p['fir'], p['n'], p['size'], p['clay'], p['glaze'], p['care']))

def pot_card(p, link='/shop/'):
    sold = p['stock'] == 0
    price = '£%s, sold out' % p['p'] if sold else '£%s, %d left' % (p['p'], p['stock'])
    return group(J(image(p['img'], p['alt'], href=link, className='is-style-square'),
                   heading('<a href="%s">%s</a>' % (link, p['n']), 3, fontSize='medium', fontFamily='body', style={'typography': {'fontWeight': '600', 'letterSpacing': '0'}}),
                   para(price, className='is-style-price')),
                 layout={'type': 'flex', 'orientation': 'vertical'}, style={'spacing': {'blockGap': sp(20)}},
                 **({'className': 'is-style-sold-out'} if sold else {}))

# ------------------------------------------------------------------ patterns
pattern('shop-closed-slab', 'Shop closed: next update (signature)', 'featured,shop', group(columns(
    ('58%', J(para('The shop is closed', fontSize='large', style={'typography': {'fontWeight': '600'}}),
              heading('Next update: Sunday 18 October, 7pm', 1),
              para('About forty pots from firing 41: mugs, tea bowls, three moon jars and a few big ash jars. The list goes to the newsletter on Friday, so you can plan what you want before the shop opens.', fontSize='large'),
              buttons(('Get the list by email', '/newsletter/'), ('See what sold last time', '/shop/')))),
    ('42%', image('moon-jar.jpg', 'A large round white jar with a small neck, slightly lopsided, on a grey plinth', 'Moon jar, firing 41. Sold in the September update.')),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(70), 'top': sp(50)}}}),
    className='is-style-celadon-slab', align='full'),
    description='The front-page notice for the time between shop updates. Change the date after each update.')

pattern('shop-open-slab', 'Shop open now', 'featured,shop', group(columns(
    (None, J(para('The shop is open', fontSize='large', style={'typography': {'fontWeight': '600'}}),
             heading('Firing 41 is in the shop until it sells out', 1),
             para('One of each per household, please, so more people get a pot. Orders are packed on Tuesdays.', fontSize='large'),
             buttons(('Go to the shop', '/shop/')))),
    (None, image('tea-bowl.jpg', 'A wide conical tea bowl in dark brown glaze with rust streaks and a pale foot ring')),
    align='wide', verticalAlignment='center'), className='is-style-celadon-slab', align='full'),
    description='Swap this in for the closed slab on the day of a shop update.')

pattern('status-bar', 'Shop status bar', 'banner', status_bar, description='A thin notice for the top of every page between updates.')

pattern('last-update-grid', 'Last update, sold pots still listed', 'shop,portfolio', group(J(
    row(J(heading('What sold on 20 September', 2, fontSize='x-large'),
          para('<a href="/shop/">All pots, sold ones included</a>')), justify='space-between', align='wide'),
    para('Forty-six pots, gone in just under two hours. Sold ones stay listed so you can see prices and sizes before the next update.', align='wide', textColor='muted'),
    group(J(*[pot_card(p) for p in POTS[:6]]), layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '9rem'}, align='wide', style={'spacing': {'blockGap': sp(50)}})),
    align='wide', layout={'type': 'default'}))

pattern('product-card', 'Pot card (sold out, dimmed)', 'shop', pot_card(POTS[1]),
        description='A square photo, name and price. Sold pots keep their card and the photo is dimmed.')

pattern('product-detail', 'Pot details (size, clay, glaze, care)', 'shop', J(
    table([['Size', POTS[1]['size']], ['Clay', POTS[1]['clay']], ['Glaze', POTS[1]['glaze']], ['Firing', 'Number %s, wood kiln, 3 to 5 October 2026' % POTS[1]['fir']], ['Care', POTS[1]['care']]]),
    pattern_ref('firing-number')))

pattern('firing-number', 'Firing number note', 'shop', para(
    'Every pot has the firing number scratched into the foot next to my stamp. Firing 41 was the autumn wood firing: 52 hours, 11 tonnes of larch and spruce offcuts from the sawmill in Sedbergh.', fontSize='small', textColor='muted'))

pattern('care-card', 'Care card', 'shop', group(J(
    heading('Looking after stoneware', 3),
    lst(['Everything with a glazed inside is food safe. Unglazed wood-fired pieces are for flowers and looking at.',
         'Mugs, bowls and plates go in the dishwasher and microwave. Jars with lids and the moon jars do not.',
         'Crazing is the fine web of cracks in some glazes. On celadon it is on purpose. It is sealed underneath, and tea will slowly stain it darker.',
         'Don\'t put a cold pot in a hot oven. Oven-to-table dishes are marked as such in the listing.']),
    para('<a href="mailto:nell@example.com?subject=Care%20card%20PDF">Ask for the care card as a PDF</a>. One comes in the box with every order.', fontSize='small')),
    className='is-style-biscuit'))

pattern('notify-back', 'Notify me when this form is back', 'shop,call-to-action', group(J(
    para('Mugs, tea bowls and the small cups come back in every update. Sign up and I\'ll email you the evening before they go up.'),
    buttons(('Email me when mugs are back', 'mailto:nell@example.com?subject=Notify%20me%3A%20mugs'))),
    className='is-style-rule-top'))

pattern('kiln-opening-dates', 'Kiln opening dates with hours per day', 'featured', group(J(
    columns(
        ('40%', J(para('Autumn kiln opening', fontSize='large', style={'typography': {'fontWeight': '600'}}), heading('Saturday 7 and Sunday 8 November', 2), para('Two days at the pottery, straight after the autumn wood firing. About 200 pots, a lot of them only sold here.', fontSize='large'))),
        (None, J(table([['Saturday 7 November', '10am to 5pm', 'Doors open at 10. No queueing before 9, the lane is narrow.'],
                        ['Sunday 8 November', '11am to 4pm', 'Quieter. Seconds table goes out at 2pm.']], head=['Day', 'Open', 'Notes']),
                 para('Lowfold, Cowgill, Dent LA10 5RL. Parking in the field opposite, wellies advised. Card and cash.', fontSize='small'))),
        align='wide', style={'spacing': {'blockGap': {'left': sp(70)}}})),
    className='is-style-biscuit', align='full'),
    description='Dates and hours for each day of the sale. Remove this block after the last day.')

pattern('kiln-opening-expect', 'What to expect at a kiln opening', 'text', J(
    heading('What happens on the day', 3),
    lst(['Pots are laid out on boards in the byre by type. Pick up what you like and bring it to the table by the door.',
         'At 11 and at 2, I open the wood kiln door and you can look inside. Children welcome, dogs on leads.',
         'You can walk round the workshop and see the wheel, the glaze buckets and the next batch drying.',
         'Tea and parkin from the Cowgill Institute ladies, money goes to the village hall roof.'])))

pattern('firing-log', 'Kiln log (latest firing notes)', 'posts,query', group(J(
    row(J(heading('Kiln log', 2, fontSize='x-large'), para('<a href="/kiln-log/">All firings</a>')), justify='space-between', align='wide'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), dyn('post-date'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=22)),
          per_page=3, layout={'type': 'grid', 'columnCount': 3}, align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('firing-archive', 'Kiln log archive (inherits the page query)', 'posts,query', inherit_query(
    columns(('35%', dyn('post-featured-image', isLink=True, aspectRatio='4/3')),
            (None, J(dyn('post-date'), dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', excerptLength=40))),
            style={'spacing': {'blockGap': {'left': sp(50)}}}),
    align='wide'), inserter=False)

pattern('newsletter-signup', 'Newsletter for early notice', 'call-to-action', group(columns(
    (None, J(heading('The shop list arrives two days early', 2, fontSize='x-large'),
             para('Four emails a year, one before each shop update, with every pot, its size and its price. Plus the kiln opening dates in autumn and spring. Nothing else.'))),
    (None, J(para('Send a blank email and I add you by hand. To leave, reply "stop".'),
             buttons(('Join the list by email', 'mailto:nell@example.com?subject=Add%20me%20to%20the%20shop%20list')))),
    align='wide', verticalAlignment='bottom'), className='is-style-celadon-slab', align='full'))

GLZ = [('accent', 'base', 'Celadon', 'Cone 10 reduction. Pools green in carving. Bowls, cups.'),
       ('shino', 'contrast', 'Shino', 'Cone 10 reduction. Orange where thin, white where thick. Tea bowls.'),
       ('ash', 'contrast', 'Ash glaze', 'Wood ash from the kiln, washed and sieved. Jars, mugs.'),
       ('accent-2', 'base', 'Tenmoku', 'Iron glaze, breaks rust on edges. Tea bowls, bottles.'),
       ('cobalt', 'base', 'Cobalt', 'Only on inside rims of small cups. Very little goes a long way.')]
pattern('glaze-tiles', 'Glaze test tiles (glaze key)', 'featured,text', group(J(
    heading('The five glazes', 2, fontSize='x-large'),
    para('Every pot in the shop uses one or two of these. They look different on every firing, so treat the tiles as a guide.', textColor='muted'),
    group(J(*[group(J(heading(n, 3, fontSize='large'), para(d)), backgroundColor=bg, textColor=tc, className='is-style-glaze-tile') for bg, tc, n, d in GLZ]),
          layout={'type': 'grid', 'columnCount': 5, 'minimumColumnWidth': '10rem'}, style={'spacing': {'blockGap': sp(20)}})),
    align='wide', layout={'type': 'default'}), description='A row of square test tiles, one per glaze, in the palette colours.')

pattern('process-sequence', 'Process: throwing, trimming, firing', 'portfolio,gallery', J(
    heading('How a mug gets made', 2, fontSize='x-large'),
    columns(
        (None, J(image('wheel.jpg', 'Three potter\'s wheels in a workshop with stools upturned on the splash pans'), heading('Throwing', 3, fontSize='large'),
                 para('Six hundred grams of clay per mug, thrown in batches of forty on a Monday.'))),
        (None, J(image('trimming.jpg', 'A leather-hard unglazed mug seen from above next to lumps of clay and a stamp'), heading('Trimming and stamping', 3, fontSize='large'),
                 para('Next day, at leather hard, I trim the foot, pull the handle and stamp the base.'))),
        (None, J(image('jar-ash.jpg', 'A round ribbed jar with streaky tan and green glaze and a red lid'), heading('Firing', 3, fontSize='large'),
                 para('Bisque at 1000°C, then glaze and a second firing to about 1300°C. Wood firings take three days and two helpers.'))),
        align='wide')))

pattern('stockists', 'Stockists (shops and galleries)', 'about', J(
    heading('Where to see the pots in person', 2, fontSize='x-large'),
    table([['Sedbergh', 'Rawthey Mill Makers', 'Mugs and bowls, restocked after each firing'],
           ['Kendal', 'Stricklandgate Craft Shop', 'Tea bowls and small cups'],
           ['Leeds', 'Briggate Clay Gallery', 'Moon jars, when there are any'],
           ['Edinburgh', 'Leith Street Makers', 'Wood-fired bottles and jars']], head=['Town', 'Shop', 'Usually has'])))

pattern('exhibitions', 'Exhibitions list', 'about', J(
    heading('Exhibitions', 3),
    table([['2026', 'Fire and Ash, group show', 'Rawthey Mill Makers, Sedbergh'],
           ['2025', 'Northern potters\' fair', 'York'],
           ['2024', 'Midlands pottery fair', 'Nottinghamshire'],
           ['2023', 'Moon jars, solo', 'Briggate Clay Gallery, Leeds']])))

pattern('appointment-line', 'Shop by appointment line', 'contact', para(
    'Local? You can buy from the workshop shelves any time of year by appointment. Phone 015396 25518 the day before, and if nobody answers I\'m probably in the kiln.',
    fontSize='large'))

pattern('video-block', 'Process film', 'media', columns(
    ('35%', image('vase-ash.jpg', 'A tall cylindrical unglazed vase, flashed red-brown and green where the flames hit it', 'Still from the film: the bottle vase coming out of the fire mouth.')),
    (None, J(heading('A wood firing in eleven minutes', 3),
             para('Filmed by Tom Iredale over the three days of firing 41, from loading to the door coming off.'),
             para('<a href="https://example.com/firing-41">Watch it on the film page</a>'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('about-potter', 'About the potter', 'about', columns(
    ('45%', image('wheel.jpg', 'Three potter\'s wheels in a workshop with stools upturned on the splash pans')),
    (None, J(heading('Nell Rigby, potter', 2, fontSize='x-large'),
             para('I trained for two years at a country pottery in north Devon, then spent five years making standard ware at a pottery in Mashiko, Japan. I came back to Dentdale in 2017 and built the wood kiln with my brother over two summers.'),
             para('I make functional pots: things to drink from, eat from and store things in. I don\'t do commissions for dinner services, because I can\'t promise that forty plates will match, and I\'d rather not try.'),
             pattern_ref('appointment-line'))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('press-quote', 'Quote from a buyer', 'testimonials', quote(
    'I bought a tea bowl at the kiln opening in 2023 and it has been used every single day. The rust on the rim is my favourite colour in the house.',
    'Aoife, Kendal, bought at the November 2023 kiln opening'))

pattern('postage-note', 'Postage and returns', 'shop', group(J(
    heading('Postage', 3),
    table([['UK mainland', '£9.50 per order', '2 to 3 working days'], ['Highlands, islands, Northern Ireland', '£16', '3 to 5 working days'],
           ['Europe', 'From £28, quoted by weight', '5 to 10 working days']], head=['Where', 'Cost', 'Usually takes']),
    para('Every pot is wrapped in paper and packed in a double-wall box with wood wool. If something arrives broken, send a photo within 7 days and I refund it in full. Moon jars are collection only.', fontSize='small')),
    className='is-style-rule-top'))

pattern('notice-holiday', 'Notice: workshop closed', 'banner', group(
    para('The workshop is closed 20 December to 6 January. Orders placed then go out on 7 January. Take this down on 7 January.'),
    className='is-style-status-bar', align='full'), description='A one-line closure notice for holidays.')

# page layouts
pattern('kiln-opening-page', 'Page: kiln opening', 'featured', J(
    pattern_ref('kiln-opening-dates'), spacer(), pattern_ref('kiln-opening-expect'), pattern_ref('video-block'), pattern_ref('press-quote')),
    block_types='core/post-content')
pattern('process-page', 'Page: process and about', 'about', J(
    pattern_ref('process-sequence'), spacer(), pattern_ref('glaze-tiles'), spacer(), pattern_ref('about-potter'), pattern_ref('care-card')),
    block_types='core/post-content')
pattern('stockists-page', 'Page: stockists and exhibitions', 'about', J(
    pattern_ref('stockists'), pattern_ref('exhibitions'), pattern_ref('appointment-line')), block_types='core/post-content')
pattern('newsletter-page', 'Page: newsletter', 'call-to-action', J(
    para('The shop opens four times a year and usually sells out in an evening. The newsletter is the fair way to hear first: everyone on it gets the full list at the same time, two days before the update.', fontSize='large'),
    pattern_ref('newsletter-signup'), pattern_ref('notify-back'), pattern_ref('postage-note')), block_types='core/post-content')

# ------------------------------------------------------------------ templates
mp = {'spacing': {'padding': {'top': sp(50), 'bottom': sp(70)}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('shop-closed-slab'), spacer('var:preset|spacing|70'), pattern_ref('last-update-grid'), spacer('var:preset|spacing|70'),
    pattern_ref('kiln-opening-dates'), spacer('var:preset|spacing|70'), pattern_ref('glaze-tiles'), spacer('var:preset|spacing|70'),
    pattern_ref('firing-log'), spacer('var:preset|spacing|70'), pattern_ref('newsletter-signup')),
    header='header-plain', style={'spacing': {'blockGap': '0'}}))
write('templates/home.html', page_template(J(
    heading('Kiln log', 1, align='wide'),
    para('One entry per firing: what went in, what came out, and what went wrong.', align='wide', fontSize='large'),
    pattern_ref('firing-archive')), style=mp))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('firing-archive')), style=mp))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('firing-archive')), style=mp))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide', fontSize='xx-large'),
    dyn('search', label='Search', showLabel=False, placeholder='Mugs, tea bowls, firing 41', buttonText='Search', align='wide'),
    pattern_ref('firing-archive')), style=mp))
write('templates/404.html', page_template(J(
    heading('This one cracked in the kiln', 1),
    para('The page isn\'t here. It might have been a listing from an old shop update. The <a href="/shop/">shop</a> keeps every pot, sold ones included.'),
    dyn('search', label='Search', showLabel=False, placeholder='Mugs, tea bowls, firing 41', buttonText='Search')), style=mp))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), style=mp))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide', fontSize='xx-large'),
                                                   dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1280px'})), style=mp))
single = J(dyn('post-date'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image', align='wide', aspectRatio='16/9'),
           dyn('post-content', layout={'type': 'constrained'}),
           row(J(dyn('post-navigation-link', type='previous', label='Earlier firing', showTitle=True), dyn('post-navigation-link', label='Later firing', showTitle=True)),
               justify='space-between', className='is-style-rule-top'))
write('templates/single.html', page_template(single, style=mp))
write('templates/single-firing.html', page_template(single, style=mp))

# ------------------------------------------------------------------ demo content
FIRINGS = [
    ('Firing 41: autumn wood firing', '2026-10-06', 'vase-ash.jpg', 'Fifty-two hours, eleven tonnes of offcuts, three of us on shifts. The front of the kiln went hotter than ever, so the bottles near the fire mouth are the best I have made.',
     ['We loaded on the Wednesday and lit on Thursday morning. By Friday night the front was at cone 12 and the back at cone 9, which is a bigger gap than I like.',
      'The bottle vases in the front row came out with thick green ash on the shoulders and red flashing below. The mugs at the back are paler than usual. About one in twelve pots is a second, mostly from shelf wads sticking.',
      'Everything from this firing goes up in the shop on 18 October, apart from what I keep back for the kiln opening.']),
    ('Firing 40: gas kiln, celadon test', '2026-08-21', 'bowl-celadon.jpg', 'A new celadon recipe with less iron. Greener, clearer, and it pools in carving the way I wanted. Thirty bowls, four lost to dunting.',
     ['I changed the celadon from 1.5% to 1% red iron oxide and held the reduction longer. The result is a grey-green that shows the carving much better.',
      'Four bowls cracked in cooling. I think the kiln cooled too fast below 600°C, so next time I will close the damper earlier.']),
    ('Firing 39: shino tea bowls', '2026-06-02', 'tea-bowl.jpg', 'Shino only behaves at the back of the kiln. Eleven good tea bowls out of twenty, which is about normal for me.',
     ['Carbon trapping gave grey patches on half of them. I like those, but they are marked as such in the shop so nobody is surprised.']),
    ('Firing 38: spring kiln opening pots', '2026-03-28', 'jar-ash.jpg', 'Big jars for the spring kiln opening. The ash glaze ran further than planned and glued two lids on for good.',
     ['Two jars will be sold as sculptures now, lids fixed. The rest went at the kiln opening on 18 and 19 April.']),
    ('Firing 37: moon jars', '2026-01-17', 'moon-jar.jpg', 'Three moon jars attempted, two survived. They take two days to join and a week to dry.',
     ['The white slip was applied at leather hard and the clear ash glaze sprayed on. Both surviving jars sold to the newsletter list within the hour.']),
    ('Firing 36: stamped bowls', '2025-11-02', 'bowl-stamped.jpg', 'Stamps carved from old broom handles. The dots take a whole afternoon per bowl.',
     ['I inlaid white slip into the stamped dots and scraped it back. The glaze crackle came out finer than before.']),
]
posts = []
for t, d, img, ex, paras in FIRINGS:
    posts.append({'title': t, 'date': d, 'category': 'firings', 'image': img, 'excerpt': ex, 'template': 'single-firing',
                  'content': J(para(ex, fontSize='large'), *[para(x) for x in paras])})

products = []
for p in POTS:
    products.append({'name': p['n'], 'price': p['p'], 'image': p['img'], 'category': 'Firing ' + p['fir'], 'sku': 'LF-%s-%02d' % (p['fir'], POTS.index(p) + 1),
                     'stock': p['stock'], 'short': '%s. %s. Firing %s.' % (p['size'], p['glaze'], p['fir']), 'description': pot_desc(p)})

demo = {
    'site': {'title': 'Lowfold Pottery', 'tagline': 'Wood-fired stoneware by Nell Rigby, Dentdale'},
    'categories': [{'slug': 'firings', 'name': 'Firings', 'description': 'One entry per kiln firing.'}],
    'front_page': 'home', 'posts_page': 'kiln-log',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'kiln-log', 'title': 'Kiln log', 'content': ''},
        {'slug': 'kiln-opening', 'title': 'Kiln opening', 'pattern': 'kiln/kiln-opening-page', 'template': 'page-wide'},
        {'slug': 'process', 'title': 'Process', 'pattern': 'kiln/process-page', 'template': 'page-wide'},
        {'slug': 'stockists', 'title': 'Stockists', 'pattern': 'kiln/stockists-page', 'template': 'page-wide'},
        {'slug': 'newsletter', 'title': 'Newsletter', 'pattern': 'kiln/newsletter-page', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'Kiln opening', 'url': '/kiln-opening/'}, {'label': 'Process', 'url': '/process/'},
            {'label': 'Kiln log', 'url': '/kiln-log/'}, {'label': 'Stockists', 'url': '/stockists/'}, {'label': 'Newsletter', 'url': '/newsletter/'}],
    'currency': 'GBP',
    'products': products,
}
os.makedirs('demos/kiln', exist_ok=True)
with open('demos/kiln/content.json', 'w', encoding='utf-8') as f:
    json.dump(demo, f, indent=1, ensure_ascii=False)
print('kiln built')
