# good-dog: design note
# Direction: "rainbow sweet shop for dogs". A Margate workshop that sews beds, collars and leads in six loud colours,
#   and says so with jokes. The owner asked for more rainbows, more fun and funny, so the saddlery look in the research is dropped.
# Why: dogs see mostly blue and yellow, so the rainbow is for the humans. That joke drives the palette and the copy.
# Fonts: Cherry Bomb One (display, bubbly and loud), Mulish (body, with tabular figures for sizes and prices).
# Palette: white and navy ink, six bright sticker colours (coral, orange, yellow, green, sky, pink) that all carry navy text.
# Layout idea: a six-stripe rainbow ribbon under the header and above the footer, and the shop split into
#   colour-swatch tiles, one colour per product type. Stickers: thick navy outlines and hard offset shadows, no blur.
import sys, json, os, re; sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('good-dog')
S = THEME['slug']

# Round 2: map inserter categories so the pattern library groups well (first category = library page).
CATMAP = {'featured': 'hero', 'shop': 'products', 'query': 'dog-wall', 'gallery': 'dog-wall', 'testimonials': 'reviews', 'text': 'info',
          'call-to-action': 'signup', 'banner': 'notices', 'good-dog-guides': 'guides'}
_pattern = pattern
def pattern(slug, title, categories, body, **kw):
    cats = [CATMAP.get(c.strip(), c.strip()) for c in categories.split(',') if c.strip() and c.strip() != 'good-dog'] or ['pages']
    return _pattern(slug, title, ','.join(dict.fromkeys(cats)), body, **kw)
D = THEME['dir']


def wjson(rel, data):
    p = os.path.join(D, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent='\t', ensure_ascii=False)
        f.write('\n')


fonts = [f for f in json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies'] if f['slug'] != 'mono']
for f in fonts:
    if f['slug'] == 'body':
        f['name'] = 'Mulish'

PAL = [
    ('base', '#FFFFFF', 'Clean towel'),
    ('contrast', '#17213A', 'Navy ink'),
    ('accent', '#C8321C', 'Tomato'),
    ('accent-2', '#1D5FB8', 'Lead blue'),
    ('surface', '#FFF3C2', 'Butter'),
    ('line', '#17213A', 'Stitch line'),
    ('muted', '#4A5369', 'Slate'),
    ('coral', '#FF7A5C', 'Coral'),
    ('orange', '#FFA531', 'Orange'),
    ('yellow', '#FFD93D', 'Yellow'),
    ('green', '#5FCB7D', 'Grass'),
    ('sky', '#6FB0F5', 'Sky'),
    ('pink', '#F79BC8', 'Bubblegum'),
]
RAINBOW = ['coral', 'orange', 'yellow', 'green', 'sky', 'pink']


def palette(over=None):
    over = over or {}
    return [{'slug': s, 'color': over.get(s, c), 'name': n} for s, c, n in PAL]


V = lambda s: 'var(--wp--preset--color--%s)' % s
stripes = ','.join('%s %.2f%% %.2f%%' % (V(c), i * 100 / 6, (i + 1) * 100 / 6) for i, c in enumerate(RAINBOW))

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette()},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Tag', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.625rem', 'name': 'Large', 'fluid': {'min': '1.3rem', 'max': '1.625rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '1.9rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.6rem', 'max': '4rem'}},
                {'slug': 'display', 'size': '7rem', 'name': 'Display', 'fluid': {'min': '3.2rem', 'max': '7rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3.5vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': [
            {'slug': 'sticker', 'name': 'Sticker', 'shadow': '6px 6px 0 0 var(--wp--preset--color--contrast)'},
            {'slug': 'sticker-small', 'name': 'Sticker, small', 'shadow': '3px 3px 0 0 var(--wp--preset--color--contrast)'}]},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True,
                   'radiusSizes': [{'slug': 'image', 'size': '22px', 'name': 'Image'}, {'slug': 'tile', 'size': '28px', 'name': 'Tile'}, {'slug': 'pill', 'size': '999px', 'name': 'Pill'}]},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
        'custom': {'rainbow': 'linear-gradient(90deg,%s)' % stripes},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '450'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent-2', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '1.02', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'lineHeight': '0.95'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '900', 'lineHeight': '1.4'}},
            'button': {
                'color': {'background': 'var:preset|color|yellow', 'text': 'var:preset|color|contrast'},
                'border': {'radius': '999px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'shadow': 'var:preset|shadow|sticker-small',
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.4em', 'right': '1.4em'}},
                ':hover': {'color': {'background': 'var:preset|color|pink', 'text': 'var:preset|color|contrast'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent-2', 'offset': '3px', 'style': 'solid', 'width': '3px'}},
                ':active': {'shadow': 'none'}},
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'italic', 'fontWeight': '600', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '800'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}},
                                'css': '& .wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--yellow);padding:var(--wp--preset--spacing--50)}& .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large);font-weight:400}& .current-menu-item > a{text-decoration:underline wavy;text-underline-offset:6px}'},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}},
            'core/image': {'border': {'radius': '22px'}, 'css': '& img{border:3px solid var(--wp--preset--color--contrast)}'},
            'core/post-featured-image': {'border': {'radius': '22px'}, 'css': '& img{border:3px solid var(--wp--preset--color--contrast);border-radius:22px}'},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '3px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.35'},
                           'border': {'left': {'color': 'var:preset|color|pink', 'width': '10px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large'}, 'border': {'width': '0'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table{border-collapse:separate;border-spacing:0;border:3px solid var(--wp--preset--color--contrast);border-radius:18px;overflow:hidden}& th{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);text-align:left;font-family:var(--wp--preset--font-family--body);font-weight:400}& td,& th{border:0;border-top:2px solid var(--wp--preset--color--contrast);padding:.7em .9em}& td{font-variant-numeric:tabular-nums}@media (max-width:600px){& td,& th{padding:.5em .45em;font-size:var(--wp--preset--font-size--x-small)}}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'dotted'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-weight:800;font-size:var(--wp--preset--font-size--large)}'},
            'core/code': {'typography': {'fontFamily': 'var:preset|font-family|body'}},
            'core/search': {'css': '& .wp-block-search__input{border:3px solid var(--wp--preset--color--contrast);border-radius:999px;padding:.6em 1em}& .wp-block-search__button{margin-left:.5em}'},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'}},
            'core/list': {'css': '&.is-style-default li::marker{color:var(--wp--preset--color--accent)}'},
        },
        'css': ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty;max-width:72ch}:where(.wp-block-group.has-text-align-center p){margin-inline:auto}body{font-synthesis:none}a:focus-visible,button:focus-visible{outline:3px solid var(--wp--preset--color--accent-2);outline-offset:3px}.wc-block-components-product-image img,.woocommerce-loop-product__link img,.wc-block-grid__product-image img{border:3px solid var(--wp--preset--color--contrast);border-radius:22px}.wc-block-components-product-price,.woocommerce-Price-amount{font-family:var(--wp--preset--font-family--body)}.wc-block-components-product-sale-badge{background:var(--wp--preset--color--pink);color:var(--wp--preset--color--contrast);border:3px solid var(--wp--preset--color--contrast);border-radius:999px}.woocommerce .products .product .woocommerce-loop-product__title,.wc-block-components-product-name,.wp-block-post-title a{font-family:var(--wp--preset--font-family--display);font-weight:400}@media (prefers-reduced-motion:no-preference){.wp-element-button{transition:transform .12s,box-shadow .12s}.wp-element-button:active{transform:translate(3px,3px)}}',
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Lead time bar'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
                        {'name': 'page-guide', 'title': 'Guide page (yellow title band)', 'postTypes': ['page']}],
}
wjson('theme.json', theme)

# ---------- variations ----------
wjson('styles/park.json', {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': 'Park',
    'settings': {'color': {'palette': palette({'base': '#F4FBEF', 'contrast': '#12301F', 'accent': '#A2361C', 'surface': '#DDF2CF', 'line': '#12301F', 'muted': '#3E5446', 'accent-2': '#1D5F8A'})}}})
wjson('styles/bath-time.json', {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': 'Bath time',
    'settings': {'color': {'palette': palette({'base': '#EAF4FF', 'contrast': '#0E2446', 'accent': '#B3261E', 'surface': '#FFFFFF', 'muted': '#3B4C66', 'line': '#0E2446'})}},
    'styles': {'elements': {'button': {'color': {'background': 'var:preset|color|sky'}}}}})
wjson('styles/midnight-zoomies.json', {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': 'Midnight zoomies',
    'settings': {'color': {'palette': palette({'base': '#17213A', 'contrast': '#FFF7E0', 'accent': '#FFD93D', 'accent-2': '#8CC4FF', 'surface': '#223055', 'line': '#FFF7E0', 'muted': '#C9CFDD'})}},
    'styles': {'blocks': {'core/image': {'css': '& img{border:3px solid var(--wp--preset--color--yellow)}'}}}})

# ---------- section styles ----------
def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

PAD = {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}
for c in RAINBOW:
    section('swatch-' + c, 'Swatch: ' + c, ['core/group', 'core/column', 'core/columns'],
            {'color': {'background': 'var:preset|color|' + c, 'text': 'var:preset|color|contrast'},
             'border': {'radius': '28px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
             'shadow': 'var:preset|shadow|sticker', 'spacing': {'padding': PAD},
             'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}})
section('sticker', 'Sticker', ['core/group', 'core/column'],
        {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
         'border': {'radius': '28px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
         'shadow': 'var:preset|shadow|sticker', 'spacing': {'padding': PAD}})
section('butter', 'Butter band', ['core/group'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
         'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}})
section('rainbow', 'Rainbow ribbon', ['core/separator'],
        {'css': '&{border:0!important;height:14px!important;max-width:none!important;opacity:1;background:var(--wp--custom--rainbow)}'})
section('rainbow-edge', 'Rainbow edge', ['core/group'],
        {'css': '&{border-top:14px solid transparent;border-image:var(--wp--custom--rainbow) 1}'})
section('tilt-left', 'Tilted left', ['core/image', 'core/group'], {'css': '&{transform:rotate(-2.5deg)}'})
section('tilt-right', 'Tilted right', ['core/image', 'core/group'], {'css': '&{transform:rotate(2deg)}'})
section('size-tag', 'Size tag', ['core/paragraph'],
        {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'},
         'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
         'border': {'radius': '999px', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
         'css': '&{display:inline-block;padding:.2em .8em}'})
section('rainbow-rows', 'Rainbow rows', ['core/table'],
        {'css': ''.join('& tbody tr:nth-child(6n+%d) td:first-child{box-shadow:inset 12px 0 0 %s;padding-left:1.6em!important}' % (i + 1, V(c)) for i, c in enumerate(RAINBOW))
                + '& tbody tr.is-pick td, & tbody mark{background:var(--wp--preset--color--yellow);color:var(--wp--preset--color--contrast)}'})
section('dog-wall', 'Dog wall', ['core/post-template', 'core/gallery'],
        {'css': '& img{aspect-ratio:1;object-fit:cover}'})
section('notice', 'Notice bar', ['core/group'],
        {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
         'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'},
         'elements': {'link': {'color': {'text': 'var:preset|color|yellow'}}}})
section('inline-list', 'Inline list', ['core/categories'],
        {'typography': {'fontWeight': '800', 'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.6rem}& li a{display:inline-block;padding:.35em 1em;border:3px solid var(--wp--preset--color--contrast);border-radius:999px;text-decoration:none;color:var(--wp--preset--color--contrast)}& li:nth-child(6n+1) a{background:var(--wp--preset--color--coral)}& li:nth-child(6n+2) a{background:var(--wp--preset--color--orange)}& li:nth-child(6n+3) a{background:var(--wp--preset--color--yellow)}& li:nth-child(6n+4) a{background:var(--wp--preset--color--green)}& li:nth-child(6n+5) a{background:var(--wp--preset--color--sky)}& li:nth-child(6n) a{background:var(--wp--preset--color--pink)}'})

# ---------- style.css, functions.php ----------
write('style.css', '''/*
Theme Name: Good Dog
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A loud, colourful shop theme for small makers of dog beds, collars, leads and blankets, with measuring guides that turn a dog's own size into a product size.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: good-dog
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')
write('functions.php', '''<?php
/**
 * Good Dog: pattern category only.
 *
 * @package good-dog
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'good-dog', array( 'label' => __( 'Good Dog', 'good-dog' ) ) );
		register_block_pattern_category( 'good-dog-guides', array( 'label' => __( 'Good Dog: size and care guides', 'good-dog' ) ) );
	}
);''')

# ---------- parts ----------
P3 = {'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}
write('parts/notice.html', group(
    para('Beds are sewn to order. Right now we post them <strong>6 working days</strong> after you order. Collars and leads go out in 2.', align='center'),
    align='full', className='is-style-notice', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))
write('parts/header.html', J(
    template_part('notice'),
    group(row(J(dyn('site-title', level=0), dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'})),
              justify='space-between', align='wide'),
          tag='div', align='full', style=P3),
    separator(className='is-style-rainbow', align='full')))
write('parts/footer.html', group(J(
    separator(className='is-style-rainbow', align='full'),
    columns(
        ('45%', J(heading('Good Dog', 2, fontSize='display'),
                  para('Dog beds, collars, leads and blankets, sewn by four people and one supervising terrier in Margate.', fontSize='small'))),
        (None, J(heading('Workshop', 6),
                 para('Unit 3, Cliftonville Mews<br>Northdown Road, Margate CT9 2QT<br>Shop hours Thursday to Saturday, 10am to 4pm', fontSize='small'))),
        (None, J(heading('Ask us', 6),
                 para('<a href="mailto:woof@example.com">woof@example.com</a><br>01843 000 417, weekdays 9 to 5<br><a href="/size-guide/">Which size?</a><br><a href="/delivery/">Delivery and returns</a>', fontSize='small'))),
        align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}}}),
    para('Demo photos are public domain and CC0 images from Wikimedia Commons, standing in for real customer dogs.', align='wide', className='alignwide', textColor='muted', fontSize='x-small')),
    tag='footer', align='full', style={'spacing': {'padding': {'bottom': 'var:preset|spacing|50'}, 'margin': {'top': 'var:preset|spacing|70'}}}))

# ---------- templates ----------
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero'), pattern_ref('shop-swatches'), pattern_ref('size-guide-teaser'), pattern_ref('dog-wall-latest'),
    pattern_ref('workshop-strip'), pattern_ref('newsletter')), style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}))
write('templates/page.html', page_template(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'})), style=MAINPAD))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})), style=MAINPAD))
write('templates/page-guide.html', page_template(J(
    group(dyn('post-title', level=1, align='wide'), tag='section', align='full', className='is-style-butter', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})), style={'spacing': {'padding': {'bottom': 'var:preset|spacing|70'}}}))
wall_item = J(dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=16, fontSize='small'))
write('templates/home.html', page_template(J(
    heading('The dog wall', 1, align='wide'),
    para('Customers send us photos of their dogs in our stuff. We put the best ones up here, plus a few where the dog has clearly chosen a different bed.', align='wide', className='alignwide'),
    pattern_ref('dog-wall-archive')), style=MAINPAD))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('dog-wall-archive')), style=MAINPAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), style=MAINPAD))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Beds, collars, whippets', buttonText='Search'), pattern_ref('post-list')), style=MAINPAD))
write('templates/404.html', page_template(J(
    heading('This page ran off after a squirrel', 1),
    para('The link might be old, or we moved something. Try the <a href="/shop/">shop</a>, the <a href="/size-guide/">size guide</a>, or search below.'),
    dyn('search', label='Search', showLabel=False, placeholder='Beds, collars, whippets', buttonText='Search')), style=MAINPAD))
write('templates/single.html', page_template(J(
    columns(('55%', dyn('post-featured-image', aspectRatio='1', scale='cover')),
            (None, J(dyn('post-terms', term='category'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'default'}),
                     dyn('post-date'))), align='wide', verticalAlignment='center'),
    group(J(dyn('post-navigation-link', type='previous', label='Previous dog', showTitle=True), dyn('post-navigation-link', label='Next dog', showTitle=True)),
          align='wide', layout={'type': 'flex', 'justifyContent': 'space-between'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}})), style=MAINPAD))

# ---------- patterns ----------
img = image

pattern('hero', 'Hero: rainbow beds and a terrier', 'good-dog,featured', group(columns(
    ('58%', J(heading('Dog beds in every colour a dog can barely see.', 1),
              para('Dogs see mostly blue and yellow. We sew the other colours in anyway, for you. Beds, collars, leads and blankets, made in our Margate workshop and posted in a box your dog will also want to sleep in.', fontSize='large'),
              buttons(('Find your bed size', '/size-guide/'), ('Shop everything', '/shop/', {'className': 'is-style-outline'})))),
    (None, J(img('terrier.jpg', 'A Jack Russell terrier sitting very still and looking straight at the camera', 'Pickle, head of quality control. Has never approved anything.', className='is-style-tilt-right'))),
    align='wide', verticalAlignment='center'), align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}),
    description='Front page opener with the headline, two buttons and a tilted dog photo.')

def swatch(color, title, line, href):
    return group(J(heading('<a href="%s">%s</a>' % (href, title), 3, fontSize='xx-large'), para(line)), className='is-style-swatch-' + color, layout={'type': 'default'})

pattern('shop-swatches', 'Shop by thing (colour swatches)', 'good-dog,shop', group(J(
    heading('What we make', 2),
    grid(J(swatch('coral', 'Beds', 'Five sizes, removable covers, six colours. From £64.', '/shop/'),
           swatch('orange', 'Collars', 'Cotton webbing with a brass buckle. Neck 24 to 62 cm. £22.', '/shop/'),
           swatch('yellow', 'Leads', '1.2 m or 1.8 m, with a handle you can hold in the rain. £26.', '/shop/'),
           swatch('green', 'Crate mats', 'Cut to named crates, so they sit flat in the corners. From £38.', '/size-guide/#crate'),
           swatch('sky', 'Blankets', 'Fleece on one side, cotton on the other. Survives the washing machine. £34.', '/shop/'),
           swatch('pink', 'Name tags', 'Engraved brass, up to 14 letters a line. Made in 5 working days. £12.', '/shop/')), min_width='22rem')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|60'}}}))

BED_ROWS = [['XS', '50 × 40 cm', 'up to 40 cm', 'Chihuahua, Yorkie', '£64'],
            ['S', '70 × 55 cm', '41 to 56 cm', 'Dachshund, Jack Russell', '£78'],
            ['M', '90 × 70 cm', '57 to 72 cm', 'Whippet, Cocker spaniel', '£96'],
            ['L', '110 × 85 cm', '73 to 88 cm', 'Labrador, Border collie', '£118'],
            ['XL', '130 × 100 cm', '89 to 104 cm', 'Greyhound, Lurcher', '£142']]
pattern('bed-size-table', 'Bed size table', 'good-dog-guides', table(
    [r[:1] + ['<mark>%s</mark>' % c if r[0] == 'S' else c for c in r[1:]] for r in BED_ROWS],
    head=['Size', 'Bed (inside)', 'Your dog, nose to tail', 'Usually fits', 'Price'], className='is-style-rainbow-rows',
    caption='The highlighted row is Mabel\'s size in the worked example above. Covers come off and go in at 40°C.'))

pattern('bed-size-guide', 'Bed size guide (measure your dog)', 'good-dog-guides,featured', group(J(
    heading('Measure the dog, then the bed picks itself', 2),
    columns(
        (None, J(heading('1. Nose to tail', 4), para('With the dog standing, measure from the tip of the nose to the base of the tail. Leave the tail out. It has its own plans.'))),
        (None, J(heading('2. Top of head to floor', 4), para('Measure the dog standing, from the top of the head to the floor. This tells you how tall the raised edge should be for a chin rest.'))),
        (None, J(heading('3. Times 1.25', 4), para('Multiply the nose-to-tail number by 1.25. That is the smallest inside length that lets your dog stretch out fully.'))),
        align='wide'),
    group(J(heading('Worked example: Mabel, a dachshund', 4),
            para('Nose to base of tail: 52 cm. 52 × 1.25 = <strong>65 cm</strong>. The small bed is 70 cm inside, so Mabel gets a small. She also sleeps curled up most nights, but she likes the option.', fontSize='small')),
          className='is-style-swatch-yellow', layout={'type': 'default'}),
    pattern_ref('bed-size-table'),
    para('Between two sizes? Go up. We have never had a complaint that a bed was too big, and we have had a lot of photos of dogs overhanging a small one.', fontSize='small')),
    align='wide', layout={'type': 'constrained', 'contentSize': '1080px'}, anchor='beds'),
    description='The signature: a three-step method that turns the dog\'s own measurements into a bed size.')

pattern('size-guide-teaser', 'Size guide teaser', 'good-dog-guides,call-to-action', group(columns(
    ('40%', img('dachshund.jpg', 'A long-haired dachshund lying across a folded cream blanket on a patterned rug', 'Mabel. 52 cm nose to tail, small bed.', className='is-style-tilt-left')),
    (None, J(heading('Nose to tail, times 1.25', 2),
             para('That is the whole bed size guide. Measure your dog standing, leave the tail out, and multiply by 1.25 to get the smallest bed your dog can stretch out in. For collars, measure the collar you already have from the buckle to the hole you use.'),
             buttons(('Measure your dog', '/size-guide/')))), align='wide', verticalAlignment='center'),
    align='full', className='is-style-butter', layout={'type': 'constrained'}))

pattern('collar-guide', 'Collar measuring guide', 'good-dog-guides', group(J(
    heading('Collars: two ways to measure', 2, anchor='collars'),
    columns(
        (None, group(J(heading('If your dog already has a collar', 4),
                        para('Lay it flat. Measure from the end of the buckle to the hole you use now. Buy the size whose range has that number near the middle.')), className='is-style-swatch-orange', layout={'type': 'default'})),
        (None, group(J(heading('If they don\'t', 4),
                        para('Measure around the neck where a collar sits, with a soft tape. Add 5 cm, or two fingers flat under the tape. That is your collar length.')), className='is-style-swatch-sky', layout={'type': 'default'})),
        align='wide'),
    table([['XS', '24 to 30 cm', '15 mm', 'Toy breeds, puppies'], ['S', '29 to 37 cm', '20 mm', 'Jack Russell, Pug'],
           ['M', '36 to 46 cm', '25 mm', 'Cocker spaniel, Beagle'], ['L', '44 to 54 cm', '25 mm', 'Labrador, Collie'], ['XL', '52 to 62 cm', '30 mm', 'Shepherd, Bernese']],
          head=['Size', 'Fits neck', 'Width', 'Usually'], className='is-style-rainbow-rows')),
    align='wide', layout={'type': 'constrained', 'contentSize': '1080px'}))

pattern('sighthound-collars', 'Sighthound collars', 'good-dog-guides', columns(
    ('45%', img('whippet.jpg', 'A white whippet lying on a lawn with its mouth open, looking pleased with itself')),
    (None, J(heading('Whippets, greyhounds and lurchers', 3),
             para('Sighthounds have heads narrower than their necks, so a normal collar slides straight off. Our sighthound collar is 50 mm wide at the front, tapers to 25 mm at the buckle, and has a martingale loop that tightens a little if they pull backwards.'),
             para('Measure around the widest part of the head, over the ears. The collar must not pass over that number when tightened.', fontSize='small'),
             buttons(('Shop sighthound collars', '/shop/')))), align='wide', verticalAlignment='center'))

pattern('crate-bedding', 'Crate bedding by crate', 'good-dog-guides', group(J(
    heading('Crate mats, cut to the crate you own', 2, anchor='crate'),
    para('A mat that is 2 cm too big rides up the sides. A mat that is 2 cm too small slides around. We cut to these crates, measured in our workshop with the crate in front of us.'),
    table([['Ellie-Bo 24"', '61 × 45 cm', '£38'], ['Ellie-Bo 30"', '76 × 49 cm', '£44'], ['Ellie-Bo 36"', '91 × 58 cm', '£52'],
           ['MidWest iCrate 42"', '104 × 69 cm', '£58'], ['Savic Dog Residence 91 cm', '89 × 59 cm', '£52']],
          head=['Crate', 'Mat', 'Price'], className='is-style-rainbow-rows'),
    para('Crate not on the list? Email us the inside floor size and we will cut one for £6 extra.', fontSize='small')),
    align='wide', layout={'type': 'constrained', 'contentSize': '1080px'}))

pattern('washing-guide', 'Washing guide for beds and covers', 'good-dog-guides', group(J(
    heading('Washing', 2, anchor='washing'),
    columns(
        (None, img('wash.jpg', 'A black and white photo of a puppy standing in a tin bath while someone dries it with a towel')),
        (None, J(lst(['Unzip the cover and shake it out outside. Then shake it out again.',
                      'Wash at 40°C with a normal non-bio powder. Skip fabric softener: it makes the cotton hold on to hair.',
                      'Tumble dry low, or line dry. The cover goes back on easier while it is still slightly damp.',
                      'The inner cushion is wipe clean. If it needs a proper wash, take it to a launderette with a big machine.'], ordered=True),
                 para('Your dog will roll in something within the hour. That part is outside our warranty.', fontSize='small'))), align='wide')),
    align='wide', layout={'type': 'constrained', 'contentSize': '1080px'}))

pattern('fabric-colours', 'Fabric colours', 'good-dog,shop', group(J(
    heading('Six colours, all washable', 2),
    para('Every bed, collar and lead comes in the same six colours, so they match whether you like it or not. The cotton canvas is 12 oz, woven in Lancashire and dyed in small batches, so a new batch can be a shade off the last one.'),
    grid(J(*[group(J(para('<strong>%s</strong>' % n), para(d, fontSize='x-small')), className='is-style-swatch-' + c, layout={'type': 'default'})
            for c, n, d in [('coral', 'Coral', 'Hides mud poorly'), ('orange', 'Marmalade', 'Hides ginger hair'), ('yellow', 'Custard', 'Visible from space'),
                            ('green', 'Tennis ball', 'Hides grass stains'), ('sky', 'Pool', 'Hides nothing, looks great'), ('pink', 'Bubblegum', 'Most popular with greyhounds')]]), min_width='10rem')),
    align='wide', layout={'type': 'default'}))

pattern('name-tag', 'Engraved name tag', 'good-dog,shop', group(columns(
    (None, J(heading('Name tags', 3),
             para('Solid brass, 32 mm across, engraved on both sides in our workshop. Front: the name, up to 10 letters. Back: two lines of up to 14 letters each, usually a phone number and a postcode.'),
             para('Made and posted in 5 working days. UK law says the tag needs your name and address, so put at least a postcode on the back.', fontSize='small'),
             buttons(('Order a tag', '/shop/')))),
    (None, group(J(para('KEVIN', fontSize='xx-large', align='center'),
                   para('07700 900 417<br>CT9 2QT', fontSize='small', align='center'),
                   para('This is what 10 and 14 letters look like on a real tag.', fontSize='x-small', align='center')),
                 className='is-style-swatch-yellow', layout={'type': 'constrained'})), align='wide', verticalAlignment='center'), align='wide', layout={'type': 'default'}))

pattern('dog-wall-latest', 'Dog wall (latest six)', 'good-dog,query', group(J(
    row(J(heading('The dog wall', 2), para('<a href="/dog-wall/">All the dogs</a>', fontSize='small')), justify='space-between', align='wide'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover'), dyn('post-title', isLink=True, level=3, fontSize='large')),
          per_page=6, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}, align='wide', template_class='is-style-dog-wall')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|40'}}}))

pattern('dog-wall-archive', 'Dog wall grid (inherits the page query)', 'good-dog,query', inherit_query(wall_item,
    layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '14rem'}, template_class='is-style-dog-wall', align='wide'), inserter=False)

pattern('post-list', 'Post list', 'good-dog,query', inherit_query(J(
    row(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-date')), justify='space-between')), align='wide'), inserter=False)

pattern('dog-wall-photos', 'Dog wall (photo grid with names)', 'good-dog,gallery', group(J(
    heading('Sent in this month', 2),
    gallery([('ball.jpg', 'A fluffy Shih Tzu lying on grass next to a tennis ball', 'Otis, Shih Tzu. Blue collar, size S.'),
             ('crate.jpg', 'A tan dog asleep in a wire crate on a blue mat with a green spotted cushion', 'Bramble, lurcher cross. Green crate mat.'),
             ('pug.jpg', 'A pug lying flat on warm concrete by a river, wearing a brown collar and a round tag', 'Kevin, pug. Name tag, obviously.'),
             ('collie.jpg', 'A black and white border collie lying on short grass, ears up', 'Nell, border collie. Orange lead.'),
             ('blanket.jpg', 'A dog asleep on a sofa under a blanket printed to look like a lettuce', 'Doris, whippet. Not our blanket. We are jealous.'),
             ('hero.jpg', 'A small white dog in a green walking vest tucked into a duvet next to soft toys', 'Biscuit, rescue. Medium bed, never uses it.')], columns=3, align='wide', className='is-style-dog-wall')),
    align='wide', layout={'type': 'default'}))

pattern('reviews', 'Customer reviews (named)', 'good-dog,testimonials', group(J(
    heading('What the humans said', 2),
    columns(
        (None, quote('The XL bed arrived, and our greyhound got in it before we had the box open. Six months and two washes later, the pink is still pink.', 'Aoife, Ramsgate, about Moose, May 2026')),
        (None, quote('Measured Mabel like the guide said, felt silly, got the small. It fits her exactly, with room for one sock she has stolen.', 'Harriet, Leeds, June 2026')),
        (None, quote('The sighthound collar is the first one Jupiter has not backed out of in the park. I have stopped doing the sprint of shame.', 'Tomasz, Walthamstow, August 2026')), align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('reviews-page', 'Page: dog wall and reviews', 'good-dog', J(pattern_ref('reviews'), pattern_ref('dog-wall-photos'), pattern_ref('send-a-photo')), block_types='core/post-content')

pattern('send-a-photo', 'Send us your dog', 'good-dog,call-to-action', group(J(
    heading('Send us your dog', 3),
    para('Email a photo of your dog using something of ours to <a href="mailto:woof@example.com?subject=Dog%20wall">woof@example.com</a> with their name and breed. If we put it on the wall, you get a free name tag. We will ask before we post it.')),
    className='is-style-swatch-green', layout={'type': 'constrained'}))

pattern('team', 'Meet the team', 'good-dog,about', group(J(
    heading('Who sews what', 2),
    columns(
        ('45%', img('workshop.jpg', 'A woman smiling as she sews bright red fabric on a black Singer sewing machine', 'Grace on the Singer, which is older than all of us put together.')),
        (None, J(para('We started Good Dog in 2019 because Hana\'s lurcher kept eating beds that cost £90 and looked like a hotel lobby. The first one we made was bright orange, because that was the only canvas left in the shop. The lurcher kept it for six years.'),
                 lst(['<strong>Hana Kowalczyk</strong> cuts the patterns and answers most of your emails.',
                      '<strong>Dele Adeyemi</strong> does collars, leads and the engraving machine, which he talks to.',
                      '<strong>Grace Achieng</strong> sews the beds. She can do an XL cover in 40 minutes.',
                      '<strong>Sam Pryce</strong> packs, posts and handles returns on Mondays and Thursdays.',
                      '<strong>Pickle</strong>, a Jack Russell, tests everything by lying on it.']),
                 para('We don\'t make dog clothes. Your dog already has a coat.'))), align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('press', 'Press', 'good-dog,about', group(J(
    heading('Where we have turned up', 3),
    table([['Kent Life', 'Makers of the month', 'March 2025'], ['Your Dog magazine', 'Best beds for sighthounds', 'October 2025'],
           ['BBC Radio Kent', 'Breakfast show, five minutes about Pickle', 'January 2026']], head=['Where', 'What', 'When'])),
    layout={'type': 'constrained'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))

pattern('about-page', 'Page: about us', 'good-dog', J(pattern_ref('team'), pattern_ref('workshop-strip'), pattern_ref('press')), block_types='core/post-content')

pattern('workshop-strip', 'Workshop visits', 'good-dog,about', group(columns(
    (None, J(heading('Come to the workshop', 2),
             para('Unit 3, Cliftonville Mews, off Northdown Road, Margate. Thursday to Saturday, 10am to 4pm. The 8A stops outside the Co-op, two minutes away. Dogs welcome, obviously. There is a water bowl and a jar of biscuits by the door.'),
             para('You can try beds with your actual dog. Please do. It saves a return.', fontSize='small'))),
    (None, img('lead.jpg', 'A black Labrador in a padded walking vest sitting beside its handler on a dusty path', 'Fitting a walking vest on a Saturday morning.', className='is-style-tilt-left')),
    align='wide', verticalAlignment='center'), align='full', className='is-style-swatch-sky', layout={'type': 'constrained'},
    style={'border': {'radius': '0', 'width': '0'}, 'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))

pattern('shipping', 'Delivery by region', 'good-dog,shop', group(J(
    heading('Delivery', 2),
    table([['UK mainland', '£4.50, free on beds', '2 to 3 working days after it leaves us'], ['Highlands, islands, Northern Ireland', '£9', '3 to 5 working days'],
           ['EU', '£14, beds £24', '5 to 8 working days, duties paid by us'], ['USA and Canada', '£22, beds £38', '7 to 12 working days'],
           ['Rest of the world', 'Email us first', 'Depends, honestly']], head=['Where', 'Cost', 'Usually takes']),
    para('Beds are made to order, so add the lead time in the black bar at the top of the page. Collars, leads and blankets are in stock.', fontSize='small')),
    layout={'type': 'constrained'}))

pattern('returns', 'Returns and exchanges', 'good-dog,shop', group(J(
    heading('Returns and swaps', 3),
    lst(['Wrong size? Send it back within 30 days, unwashed, and we swap it. We pay the return postage for size swaps in the UK.',
         'Changed your mind? Same 30 days, you pay the postage, we refund the lot.',
         'Engraved tags and custom crate mats can\'t be returned, because they have your dog\'s name on them or your crate\'s shape.',
         'Chewed it? Send us a photo. We repair seams for £8 and we will probably laugh.'])),
    className='is-style-sticker', layout={'type': 'constrained'}))

pattern('delivery-page', 'Page: delivery and returns', 'good-dog', J(pattern_ref('shipping'), pattern_ref('returns'), pattern_ref('faq')), block_types='core/post-content')

pattern('faq', 'Questions people email us', 'good-dog,text', group(J(
    heading('Questions people actually email', 3),
    details('Can I order a colour that is not on the site?', para('Once or twice a year we do a limited run. Sign up to the newsletter and you will hear first. We can\'t do one-off colours.')),
    details('My dog chews everything. Will this survive?', para('Probably not forever. The canvas is heavy, and the zips are hidden, but a determined dog will win. Our repair service is £8 a seam.')),
    details('Do you do waterproof beds?', para('The inner cushion has a waterproof liner. The cover is cotton, so it breathes and it washes.')),
    details('Can I collect?', para('Yes, from the workshop, Thursday to Saturday. Choose "collect" at checkout and we email you when it is ready.'))),
    layout={'type': 'constrained'}))

pattern('care-page', 'Page: care', 'good-dog', J(pattern_ref('washing-guide'), pattern_ref('care-leather')), block_types='core/post-content')

pattern('care-leather', 'Collar and lead care', 'good-dog-guides', group(J(
    heading('Collars and leads', 3),
    para('Webbing collars go in the washing machine inside a pillowcase, so the buckle doesn\'t bang around the drum. Brass goes darker with time. Rub it with a little ketchup on a cloth if you want it shiny again. Yes, ketchup.'),
    para('Check the stitching near the D-ring every few months. If it looks fluffy, send it to us and we will restitch it for free in the first two years.')),
    layout={'type': 'constrained'}))

pattern('size-guide-page', 'Page: size guide', 'good-dog', J(pattern_ref('bed-size-guide'), pattern_ref('collar-guide'), pattern_ref('sighthound-collars'), pattern_ref('crate-bedding')), block_types='core/post-content')

pattern('notice-closed', 'Notice: workshop closed', 'good-dog,banner', group(
    para('The workshop closes 21 December to 5 January. Order beds by 12 December for Christmas. Take this bar out on 6 January.', align='center'),
    align='full', className='is-style-notice', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
    description='A seasonal notice. Put it in the Lead time bar template part and remove it when the dates pass.')

pattern('newsletter', 'Newsletter', 'good-dog,call-to-action', group(columns(
    (None, J(heading('New colours, about four times a year', 2, fontSize='x-large'),
             para('We email when a limited colour run goes on sale, when the Christmas cut-off is near, and when Pickle does something. That is it.'))),
    ('30%', buttons(('Sign up by email', 'mailto:woof@example.com?subject=Newsletter'))), align='wide', verticalAlignment='center'),
    align='wide', className='is-style-swatch-pink', layout={'type': 'constrained'}, anchor='newsletter'))

pattern('contact-page', 'Page: contact', 'good-dog', J(columns(
    (None, J(heading('Email', 3), para('<a href="mailto:woof@example.com">woof@example.com</a>. Hana replies within two working days. Send a photo of your dog, it speeds things up.'))),
    (None, J(heading('Phone', 3), para('01843 000 417, Monday to Friday, 9am to 5pm. The phone is in the workshop, so there may be sewing noises.'))),
    (None, J(heading('Visit', 3), para('Unit 3, Cliftonville Mews, Northdown Road, Margate CT9 2QT. Thursday to Saturday, 10am to 4pm.'))), align='wide'),
    pattern_ref('newsletter')), block_types='core/post-content')

pattern('bundle', 'Starter bundle', 'good-dog,shop', group(columns(
    ('40%', img('ball.jpg', 'A fluffy Shih Tzu lying on grass next to a tennis ball')),
    (None, J(heading('New dog bundle', 3),
             para('A bed, a collar, a lead and a name tag, all in one colour, for £142 instead of £152. Tell us the dog\'s name and measurements at checkout and we check the sizes before we cut.'),
             para('Most people buy this in the week they bring a rescue home, which is lovely and also why we check the sizes.', fontSize='small'),
             buttons(('Build a bundle', '/shop/')))), align='wide', verticalAlignment='center'), align='wide', className='is-style-sticker', layout={'type': 'constrained'}))



# =====================================================================================
# Round 2: a proper shop kit. New-colour opener, favourites, shop by size and breed, gift guide,
# bed anatomy, repairs, stockists, timeline. Fewer tables. Demo content written here.
# =====================================================================================
section('spec-row', 'Label and value row', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'dotted'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
         'css': '&{display:flex!important;justify-content:space-between;gap:1rem;flex-wrap:wrap}& > *{margin:0!important}& > *:first-child{font-weight:800}'})
section('card', 'Product card', ['core/group'],
        {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
         'border': {'radius': '22px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
         'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
         'css': '& figure{margin:0 0 .75rem}& img{aspect-ratio:1;object-fit:cover;width:100%}& h3,& h4{margin:0}& p{margin:.35rem 0 0}'})

def rows(pairs):
    return J(*[group(J(para(a), para(b)), className='is-style-spec-row', layout={'type': 'default'}) for a, b in pairs])

pattern('hero', 'Opener: this month\'s colour', 'hero', group(columns(
    ('55%', J(para('New this month', fontSize='large'),
              heading('Sherbet, in beds, collars and leads', 1),
              para('Our seventh colour: a pale orange with a pink stitch, woven in one batch of 400 metres. When it is gone, it is gone until next spring. Everything else still comes in the usual six.', fontSize='large'),
              buttons(('Shop Sherbet', '/shop/'), ('Find your bed size', '/size-guide/', {'className': 'is-style-outline'})))),
    (None, image('terrier.jpg', 'A Jack Russell terrier sitting very still and looking straight at the camera', 'Pickle, testing the Sherbet bed. He approved it by lying down.', className='is-style-tilt-right')),
    align='wide', verticalAlignment='center'), align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}),
    description='Opener with the current thing: this month\'s limited colour, two buttons and a tilted dog photo.')

def card(f, alt, name, price, note, href='/shop/'):
    return group(J(image(f, alt), heading('<a href="%s">%s</a>' % (href, name), 4), para(price + ', ' + note, fontSize='small')), className='is-style-card', layout={'type': 'default'})

pattern('favourites', 'Favourites (product cards)', 'products', group(J(
    row(J(heading('What people buy most', 2), para('<a href="/shop/">The whole shop</a>')), justify='space-between', align='wide'),
    grid(J(card('dachshund.jpg', 'A dachshund asleep on a cream bed', 'Stripe bed, small', '£78', 'made to order'),
           card('whippet.jpg', 'A whippet lying on grass', 'Sighthound collar', '£28', 'in stock'),
           card('pug.jpg', 'A pug wearing a collar and round brass tag', 'Brass name tag', '£12', '5 working days'),
           card('collie.jpg', 'A border collie lying on grass', 'Lead, 1.8 m', '£26', 'in stock')), min_width='14rem')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50'}}}))

def size_tile(c, size, dims, dogs):
    return group(J(heading(size, 3, fontSize='xx-large'), para(dims, fontSize='small'), para(dogs)), className='is-style-swatch-' + c, layout={'type': 'default'})

pattern('shop-by-size', 'Shop by bed size', 'products', group(J(
    heading('Beds by size', 2),
    para('Not sure? Measure nose to base of tail and times it by 1.25. <a href="/size-guide/">The size guide</a> has the rest.'),
    grid(J(size_tile('coral', 'XS', '50 × 40 cm, £64', 'Chihuahua, Yorkie'), size_tile('orange', 'S', '70 × 55 cm, £78', 'Dachshund, Jack Russell'),
           size_tile('yellow', 'M', '90 × 70 cm, £96', 'Whippet, Cocker spaniel'), size_tile('green', 'L', '110 × 85 cm, £118', 'Labrador, Collie'),
           size_tile('sky', 'XL', '130 × 100 cm, £142', 'Greyhound, Lurcher')), min_width='12rem')),
    align='wide', layout={'type': 'default'}))

BREEDS = [('Whippet and greyhound', 'Sighthound collar, XL bed for greyhounds, M for whippets, a blanket because they are always cold'),
          ('Dachshund', 'Small bed with the raised edge, S collar, a 1.2 m lead for pavements'),
          ('Labrador', 'Large bed, L collar, the 1.8 m lead, and the chew-proof repair service on speed dial'),
          ('French bulldog and pug', 'Small bed, S collar, a name tag, because they wander'),
          ('Border collie', 'Large bed or a crate mat, M or L collar, a long lead for the fields'),
          ('Rescue of unknown origin', 'Measure first. Then the new dog bundle, which we size-check before we cut')]
pattern('shop-by-breed', 'Shop by breed', 'products', group(J(
    heading('What we would get for your breed', 3),
    rows(BREEDS), para('Breed is a guide. Your actual dog, measured, is better.', fontSize='small')),
    layout={'type': 'constrained'}))

pattern('gift-guide', 'Gift guide by price', 'products', group(J(
    heading('Presents for dogs (and the people who own them)', 2),
    columns(
        (None, group(J(heading('Under £15', 4), lst(['Brass name tag, £12', 'Poo bag holder in any colour, £9', 'A gift card for £10'])), className='is-style-swatch-yellow', layout={'type': 'default'})),
        (None, group(J(heading('Under £40', 4), lst(['Webbing collar, £22', 'Lead, £26', 'Two-sided blanket, £34'])), className='is-style-swatch-green', layout={'type': 'default'})),
        (None, group(J(heading('The big one', 4), lst(['Any bed, from £64', 'New dog bundle, £142', 'A crate mat cut to their crate, from £38'])), className='is-style-swatch-pink', layout={'type': 'default'})),
        align='wide'),
    para('Order by 12 December for Christmas. Gift notes are free: write yours in the order notes and Hana copies it out by hand.', fontSize='small')),
    align='wide', layout={'type': 'default'}))

pattern('gifts-page', 'Page: gifts', 'pages', J(pattern_ref('gift-guide'), pattern_ref('gift-card'), pattern_ref('bundle'), pattern_ref('name-tag')), block_types='core/post-content')

pattern('gift-card', 'Gift card', 'products', group(columns(
    (None, J(heading('Gift cards', 3), para('£10, £25 or £50, emailed as a PDF with your message on it, or posted on a card for £1.50. Valid for two years on anything in the shop.'))),
    ('30%', buttons(('Buy a gift card', '/shop/'))), verticalAlignment='center'),
    className='is-style-sticker', layout={'type': 'constrained'}))

pattern('new-dog-checklist', 'New dog checklist', 'guides', group(J(
    heading('The first week with a new dog', 3),
    lst(['A bed in a quiet corner, not in the middle of the kitchen. Measure them standing.', 'A collar with a tag on day one. The law says name and address, we say phone number too.',
         'A short lead for pavements. Long leads can wait until recall is solid.', 'A blanket that smells of their old place, if the rescue can give you one.',
         'Nothing else. They need a lot less than the internet says.'], ordered=True)),
    className='is-style-swatch-orange', layout={'type': 'constrained'}))

pattern('bed-anatomy', 'What is inside a bed', 'guides', group(J(
    heading('What is inside a Good Dog bed', 2),
    columns(
        (None, J(heading('The cover', 4), para('12 oz cotton canvas, zipped on three sides so it comes off in one go. The zip is hidden under a flap so it doesn\'t get chewed first.'))),
        (None, J(heading('The cushion', 4), para('Recycled fibre in a waterproof liner, split into three chambers so it doesn\'t all slide to one end. Top it up with our refill bag, £14.'))),
        (None, J(heading('The base', 4), para('Non-slip dotted cotton, so the bed stays put on floorboards when a dog lands on it from a run-up.'))),
        align='wide'),
    image('dachshund.jpg', 'A long-haired dachshund lying across a folded cream bed on a patterned rug', 'Small bed, cover on, dog in', align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('repairs', 'Repair service', 'info', group(columns(
    ('40%', image('workshop.jpg', 'A woman sewing red fabric on a black Singer sewing machine', 'Grace mending a chewed corner')),
    (None, J(heading('Chewed it? We fix it', 3),
             para('Post it back with a note. We restitch seams for £8, replace a zip for £12, and make a new cover for any bed for half the price of a new bed. Free for the first two years if the stitching fails on its own.'),
             para('We keep every colour in stock for repairs, including the ones we have stopped selling.', fontSize='small'))), align='wide', verticalAlignment='center'),
    align='wide', layout={'type': 'default'}))

pattern('stockists', 'Shops that stock us', 'about', group(J(
    heading('In real shops', 3),
    rows([('Fetch, Margate', 'Beds and collars, King Street'), ('The Dog House, Whitstable', 'Collars, leads, tags'),
          ('Barking Mad, Brighton', 'Beds to order, samples in store'), ('Hound Lounge, Leeds', 'Collars and blankets')]),
    para('Run a shop? We do wholesale on collars, leads and blankets. Email Hana for the price list.', fontSize='small')),
    layout={'type': 'constrained'}))

pattern('timeline', 'How we got here', 'about', group(J(
    heading('How we got here', 3),
    rows([('2019', 'Hana sews an orange bed for her lurcher because the shop ones kept getting eaten.'), ('2020', 'Six friends ask for one. Dele starts doing collars on the kitchen table.'),
          ('2021', 'Unit 3, Cliftonville Mews. A second sewing machine. Pickle arrives.'), ('2023', 'Grace joins. XL covers now take 40 minutes instead of two hours.'),
          ('2025', 'The sighthound collar. The dog wall passes 500 photos.'), ('2026', 'Sherbet, our first limited colour.')])),
    layout={'type': 'constrained'}))

pattern('dog-of-the-month', 'Dog of the month', 'dog-wall', group(columns(
    (None, image('blanket.jpg', 'A dog asleep on a sofa under a blanket printed to look like a lettuce', 'Doris, under a lettuce')),
    (None, J(para('Dog of the month', fontSize='large'), heading('Doris, who is a whippet under a lettuce', 2),
             para('Doris\'s owner sent us this in September with the message "not your blanket, sorry". We gave her dog of the month anyway, because look at her. She gets a free name tag, which she will ignore.'),
             buttons(('See the dog wall', '/dog-wall/')))), align='wide', verticalAlignment='center'),
    align='full', className='is-style-butter', layout={'type': 'constrained'}))

pattern('workshop-gallery', 'Workshop photos', 'about', group(J(
    heading('In the workshop', 3),
    gallery([('workshop.jpg', 'A woman sewing red fabric on a black Singer machine', 'The Singer'), ('terrier.jpg', 'A Jack Russell terrier sitting still', 'Pickle, on duty'),
             ('wash.jpg', 'A puppy being dried with a towel in a tin bath', 'Testing the washing guide'), ('crate.jpg', 'A dog asleep in a wire crate on a blue mat', 'Crate mat fitting')], columns=4, align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('press', 'Press', 'about', group(J(
    heading('Where we have turned up', 3),
    rows([('Kent Life, March 2025', 'Makers of the month'), ('Your Dog magazine, October 2025', 'Best beds for sighthounds'), ('BBC Radio Kent, January 2026', 'Five minutes about Pickle on the breakfast show')])),
    layout={'type': 'constrained'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))

pattern('shipping', 'Delivery by region', 'info', group(J(
    heading('Delivery', 2),
    rows([('UK mainland', '£4.50, free on beds, 2 to 3 working days'), ('Highlands, islands, Northern Ireland', '£9, 3 to 5 working days'),
          ('EU', '£14, beds £24, duties paid by us, 5 to 8 days'), ('USA and Canada', '£22, beds £38, 7 to 12 days'), ('Anywhere else', 'Email us first')]),
    para('Beds are made to order, so add the lead time in the black bar at the top of the page. Collars, leads and blankets are in stock.', fontSize='small')),
    layout={'type': 'constrained'}))

pattern('faq-sizing', 'Sizing questions', 'guides', group(J(
    heading('Sizing questions', 3),
    details('My dog is between sizes', para('Go up. A bed that is too big is never a problem. A bed that is too small becomes a pillow.')),
    details('My dog sleeps curled up', para('Most dogs sleep curled up and stretch out when it is warm. Size for the stretch.')),
    details('Can I swap if it is wrong?', para('Yes, within 30 days if it is unwashed. We pay the postage for size swaps in the UK.')),
    details('Puppy, still growing?', para('Buy for the adult size and fold a blanket in the bed for now. It is cheaper than two beds.'))),
    layout={'type': 'constrained'}))

pattern('stockists-page', 'Page: stockists and wholesale', 'pages', J(pattern_ref('stockists'), pattern_ref('timeline'), pattern_ref('workshop-gallery')), block_types='core/post-content')

def wall_post(name, text, pairs, extra):
    return J(para(text), rows(pairs), para(extra, className='is-style-size-tag'))

# ---- functions.php categories ----
CATS = [('hero', 'Good Dog: openers'), ('products', 'Good Dog: shop'), ('guides', 'Good Dog: size and care guides'), ('dog-wall', 'Good Dog: dog wall'),
        ('reviews', 'Good Dog: reviews'), ('about', 'Good Dog: about'), ('info', 'Good Dog: delivery and repairs'), ('signup', 'Good Dog: sign-ups'),
        ('notices', 'Good Dog: notices'), ('pages', 'Good Dog: page layouts')]
write('functions.php', """<?php
/**
 * Good Dog: pattern categories only.
 *
 * @package good-dog
 */

add_action(
	'init',
	function () {
%s
	}
);""" % '\n'.join("\t\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', 'good-dog' ) ) );" % c for c in CATS))

write('templates/front-page.html', page_template(J(
    pattern_ref('hero'), pattern_ref('shop-swatches'), pattern_ref('favourites'), pattern_ref('size-guide-teaser'), pattern_ref('shop-by-size'),
    pattern_ref('dog-wall-latest'), pattern_ref('dog-of-the-month'), pattern_ref('workshop-strip'), pattern_ref('newsletter')),
    style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}))

pattern('about-page', 'Page: about us', 'pages', J(pattern_ref('team'), pattern_ref('timeline'), pattern_ref('workshop-strip'), pattern_ref('repairs'), pattern_ref('press')), block_types='core/post-content')
pattern('size-guide-page', 'Page: size guide', 'pages', J(pattern_ref('bed-size-guide'), pattern_ref('shop-by-size'), pattern_ref('collar-guide'), pattern_ref('sighthound-collars'),
    pattern_ref('crate-bedding'), pattern_ref('shop-by-breed'), pattern_ref('faq-sizing')), block_types='core/post-content')
pattern('care-page', 'Page: care', 'pages', J(pattern_ref('washing-guide'), pattern_ref('bed-anatomy'), pattern_ref('care-leather'), pattern_ref('repairs'), pattern_ref('new-dog-checklist')), block_types='core/post-content')

# ---- demo content ----
CJ = 'demos/good-dog/content.json'
C = json.load(open(CJ))
EXTRA = {
    'Mabel': [('Bed', 'Stripe bed, small, Custard'), ('Measured', '52 cm nose to tail'), ('Lives in', 'Leeds')],
    'Kevin': [('Tag', 'Brass, KEVIN on the front'), ('Collar', 'Webbing, S, Coral'), ('Lives in', 'Faversham')],
    'Doris': [('Blanket', 'Not ours, a lettuce'), ('Collar', 'Sighthound, Bubblegum'), ('Lives in', 'Deal')],
    'Otis': [('Collar', 'Webbing, XS, Pool'), ('Lead', '1.2 m, Pool'), ('Lives in', 'Whitstable')],
    'Bramble': [('Crate mat', 'Ellie-Bo 36 inch, Tennis ball'), ('Size', '91 × 58 cm'), ('Lives in', 'Canterbury')],
    'Nell': [('Lead', '1.8 m, Marmalade'), ('Collar', 'Webbing, M, Marmalade'), ('Lives in', 'Tavistock')],
    'Biscuit': [('Bed', 'Stripe bed, medium, Bubblegum'), ('Uses it', 'Rarely'), ('Lives in', 'Ramsgate')],
    'Moose': [('Collar', 'Sighthound, Pool'), ('Bed', 'Extra large, Custard'), ('Lives in', 'Ramsgate')],
}
for po in C['posts']:
    name = po['title'].split(',')[0]
    body = po.setdefault('src', re.match(r'<!-- wp:paragraph -->[\s\S]*?<!-- /wp:paragraph -->', po['content']).group(0))
    po['content'] = J(body, rows(EXTRA.get(name, [])), para('<a href="/shop/">Shop what %s has</a>' % name))
pages = {p['slug']: p for p in C['pages']}
pages['gifts'] = {'slug': 'gifts', 'title': 'Gifts', 'pattern': 'good-dog/gifts-page', 'template': 'page-wide'}
pages['stockists'] = {'slug': 'stockists', 'title': 'Stockists', 'pattern': 'good-dog/stockists-page'}
C['pages'] = list(pages.values())
C['nav'] = [{'label': l, 'url': u} for l, u in [('Shop', '/shop/'), ('Size guide', '/size-guide/'), ('Dog wall', '/dog-wall/'), ('Gifts', '/gifts/'), ('Reviews', '/reviews/'),
            ('Care', '/care/'), ('About', '/about/'), ('Delivery', '/delivery/'), ('Stockists', '/stockists/')]]
json.dump(C, open(CJ, 'w'), indent=1, ensure_ascii=False)
print('good-dog: build done')
