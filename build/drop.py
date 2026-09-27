# drop: design note
# Direction: a 90s photocopied zine taped to a wall. The owner asked for Nirvana-style grunge with the band Julie as reference:
#   blown-out xerox photos, handwritten scrawl, typewriter type, cut paper scraps. The streetwear-mono look in the research is dropped.
# Why: a band selling its own merch from a spare room reads truer as a flyer than as a fashion shop, and the real scarcity
#   ("6 left", "first batch ships 26 to 31 Oct") looks natural handwritten next to a typed list.
# Fonts: Reenie Beanie (display, ballpoint scrawl), Cutive (body, a proportional typewriter-style serif). Two families only.
# Palette: sage photocopy grey, toner black, off-white paper scraps, ballpoint blue for handwriting, stamp red only for sold out.
# Layout idea: every section is a paper scrap taped to a grey wall at a slight angle; photos are forced to high-contrast
#   greyscale and multiplied onto the paper; the current drop is a typed stock sheet with handwritten counts.
import sys, json, os; sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('drop')
S = THEME['slug']
D = THEME['dir']


def wjson(rel, data):
    p = os.path.join(D, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent='\t', ensure_ascii=False)
        f.write('\n')


fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
PAL = [
    ('base', '#C5CBBE', 'Photocopy grey'),
    ('contrast', '#111111', 'Toner'),
    ('accent', '#23338F', 'Ballpoint'),
    ('accent-2', '#A3211B', 'Stamp red'),
    ('surface', '#EFEDE6', 'Paper scrap'),
    ('line', '#111111', 'Toner line'),
    ('muted', '#3A3D38', 'Faded toner'),
    ('tape', '#E4DCC2', 'Masking tape'),
]


def palette(over=None):
    over = over or {}
    return [{'slug': s, 'color': over.get(s, c), 'name': n} for s, c, n in PAL]


XEROX = 'grayscale(1) contrast(1.9) brightness(1.08)'
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1280px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette(),
                  'duotone': [{'slug': 'toner', 'colors': ['#111111', '#EFEDE6'], 'name': 'Toner on paper'}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.9375rem', 'name': 'Tiny type', 'fluid': False},
                {'slug': 'small', 'size': '1.0625rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Typed', 'fluid': False},
                {'slug': 'large', 'size': '2rem', 'name': 'Scribble', 'fluid': {'min': '1.6rem', 'max': '2rem'}},
                {'slug': 'x-large', 'size': '3.25rem', 'name': 'Section', 'fluid': {'min': '2.4rem', 'max': '3.25rem'}},
                {'slug': 'xx-large', 'size': '5rem', 'name': 'Title', 'fluid': {'min': '3.2rem', 'max': '5rem'}},
                {'slug': 'display', 'size': '10rem', 'name': 'Wall', 'fluid': {'min': '4.5rem', 'max': '10rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3.5vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': [
            {'slug': 'paper', 'name': 'Paper lift', 'shadow': '2px 3px 0 0 var(--wp--preset--color--muted)'}]},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'custom': {'xerox': XEROX},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|accent'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'dashed', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '0.9', 'textTransform': 'lowercase'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'lineHeight': '0.8'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'textTransform': 'none', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'textTransform': 'none', 'lineHeight': '1.3', 'textDecoration': 'underline'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|surface'},
                'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium'},
                'spacing': {'padding': {'top': '0.55em', 'bottom': '0.55em', 'left': '1.1em', 'right': '1.1em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|surface'}, 'border': {'color': 'var:preset|color|accent'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'dashed', 'width': '3px'}}},
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'}, 'color': {'text': 'var:preset|color|accent'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large', 'lineHeight': '0.8', 'textTransform': 'lowercase'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontSize': 'var:preset|font-size|x-small'}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'line-through'}}}},
                                'css': '& .wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--surface);padding:var(--wp--preset--spacing--50)}& .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large)}& .current-menu-item > a{text-decoration:underline;text-decoration-thickness:2px}'},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}},
            'core/image': {'border': {'radius': '0'}, 'css': '& img{filter:var(--wp--custom--xerox);mix-blend-mode:multiply}'},
            'core/post-featured-image': {'css': '& img{filter:var(--wp--custom--xerox);mix-blend-mode:multiply}'},
            'core/cover': {'css': '& img.wp-block-cover__image-background{filter:var(--wp--custom--xerox)}'},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '2px 0 0 0', 'style': 'dashed'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1'},
                           'color': {'text': 'var:preset|color|accent'}, 'border': {'width': '0'}, 'spacing': {'padding': {'left': '0'}},
                           'css': '& cite{font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--contrast)}'},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large'}, 'border': {'width': '0'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table{border-collapse:collapse}& th{text-align:left;font-weight:400;text-decoration:underline;border:0!important;border-bottom:2px solid var(--wp--preset--color--contrast)!important}& td{border:0!important;border-bottom:1px dashed var(--wp--preset--color--contrast)!important;vertical-align:top;font-variant-numeric:tabular-nums}& td,& th{padding:.55em .7em .55em 0}& s{color:var(--wp--preset--color--muted)}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'dashed'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{text-decoration:underline}'},
            'core/search': {'css': '& .wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0;background:var(--wp--preset--color--surface);font-family:inherit}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/list': {'css': '&{padding-left:1.2em}'},
        },
        'css': 'html,body{overflow-x:clip}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none}a:focus-visible,button:focus-visible{outline:3px dashed var(--wp--preset--color--accent);outline-offset:3px}.wc-block-components-product-image img,.woocommerce-loop-product__link img,.wc-block-grid__product-image img,.woocommerce-product-gallery img{filter:var(--wp--custom--xerox);mix-blend-mode:multiply}.wc-block-components-product-sale-badge{background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--surface);border-radius:0}.woocommerce .products .product .woocommerce-loop-product__title,.wc-block-components-product-name,.wp-block-post-title{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large)!important;text-transform:lowercase;font-weight:400}.wc-block-components-product-price{font-variant-numeric:tabular-nums}.stock.out-of-stock{color:var(--wp--preset--color--accent-2);font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large)}',
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Drop notice'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide wall', 'postTypes': ['page']}],
}
wjson('theme.json', theme)

V3 = lambda title, pal, extra=None: dict({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': palette(pal)}}}, **(extra or {}))
wjson('styles/night-shift.json', V3('Night shift', {'base': '#161616', 'contrast': '#ECEAE2', 'surface': '#262624', 'muted': '#B9B7AF', 'accent': '#9DB2FF', 'accent-2': '#FF7B6B', 'line': '#ECEAE2', 'tape': '#5A5648'},
    {'styles': {'blocks': {'core/image': {'css': '& img{filter:var(--wp--custom--xerox);mix-blend-mode:screen}'}}}}))
wjson('styles/kraft.json', V3('Kraft', {'base': '#C9A97E', 'surface': '#F1E7D2', 'muted': '#3E3223', 'contrast': '#1A140C', 'accent': '#1F2E7A', 'tape': '#EDE3C5'}))
wjson('styles/pink-flyer.json', V3('Pink flyer', {'base': '#E7B9C4', 'surface': '#FBF3F4', 'muted': '#3F2A30', 'accent': '#1F2A80', 'tape': '#F3E4C8'}))

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

TAPE = '&{position:relative}&::before{content:"";position:absolute;top:-14px;left:50%%;width:120px;height:28px;margin-left:-60px;background:color-mix(in srgb,var(--wp--preset--color--tape) 80%%,transparent);transform:rotate(%s);pointer-events:none}'
SCRAP_PAD = {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}
for slug, title, rot, tape in [('scrap', 'Paper scrap, taped', '-0.6deg', '-3deg'), ('scrap-right', 'Paper scrap, leaning right', '0.8deg', '4deg'), ('scrap-flat', 'Paper scrap, flat', '0deg', '-2deg')]:
    section(slug, title, ['core/group', 'core/column', 'core/columns'],
            {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'shadow': 'var:preset|shadow|paper',
             'spacing': {'padding': SCRAP_PAD},
             'css': (TAPE % tape) + '&{transform:rotate(%s)}' % rot})
section('toner', 'Toner block (black)', ['core/group', 'core/columns'],
        {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|surface'},
         'elements': {'link': {'color': {'text': 'var:preset|color|surface'}}, 'heading': {'color': {'text': 'var:preset|color|surface'}}},
         'spacing': {'padding': SCRAP_PAD}, 'css': '& img{mix-blend-mode:screen!important;aspect-ratio:4/5;object-fit:cover;object-position:50% 85%}& .wp-element-button{background:var(--wp--preset--color--surface);color:var(--wp--preset--color--contrast);border-color:var(--wp--preset--color--surface)}& .wp-element-button:hover{background:var(--wp--preset--color--accent);color:var(--wp--preset--color--surface)}'})
section('scrawl', 'Scrawl (ballpoint note)', ['core/paragraph', 'core/heading'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'},
         'color': {'text': 'var:preset|color|accent'}, 'css': '&{transform:rotate(-2deg)}'})
section('stamp', 'Stamp (sold out)', ['core/paragraph'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1', 'textTransform': 'lowercase'},
         'color': {'text': 'var:preset|color|accent-2'},
         'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|accent-2'},
         'css': '&{display:inline-block;padding:.05em .35em .15em;transform:rotate(-6deg)}'})
section('typed-list', 'Typed stock sheet', ['core/table'],
        {'css': '& td:last-child{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);color:var(--wp--preset--color--accent);line-height:1;white-space:nowrap}'})
section('ransom', 'Ransom note heading', ['core/heading'],
        {'css': '&{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--surface)!important;display:inline-block;padding:.05em .2em .15em;transform:rotate(-1.5deg)}'})
section('xerox-grid', 'Xerox contact sheet', ['core/post-template', 'core/gallery'],
        {'css': '& img{aspect-ratio:4/5;object-fit:cover}& > li:nth-child(odd){transform:rotate(-0.8deg)}& > li:nth-child(even){transform:rotate(0.9deg)}'})
section('notice', 'Notice strip', ['core/group'],
        {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|surface'},
         'typography': {'fontSize': 'var:preset|font-size|x-small'},
         'elements': {'link': {'color': {'text': 'var:preset|color|surface'}}}})
section('rule-bottom', 'Dashed rule below', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'dashed'}}})

write('style.css', '''/*
Theme Name: Drop
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A photocopied-zine merch shop for bands, podcasters and streamers who sell limited runs and pre-orders, with real stock counts and batch ship dates.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: drop
Tags: e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')
write('functions.php', '''<?php
/**
 * Drop: pattern category only.
 *
 * @package drop
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'drop', array( 'label' => __( 'Drop: merch table', 'drop' ) ) );
	}
);''')

# ---------- parts ----------
PAD_X = {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}
write('parts/notice.html', group(
    para('Drop seven closes Sunday 2 November at midnight, UK time. Everything left after that goes in the past drops pile.', align='center'),
    tag='section', align='full', className='is-style-notice', style={'spacing': {'padding': dict(top='var:preset|spacing|20', bottom='var:preset|spacing|20', **PAD_X)}}))
write('parts/header.html', J(
    template_part('notice'),
    group(row(J(stack(J(dyn('site-title', level=0), dyn('site-tagline', fontSize='x-small')), style={'spacing': {'blockGap': 'var:preset|spacing|10'}}),
                dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'})),
              justify='space-between', align='wide'),
          tag='section', align='full', className='is-style-rule-bottom', style={'spacing': {'padding': dict(top='var:preset|spacing|40', bottom='var:preset|spacing|30', **PAD_X)}})))
write('parts/footer.html', group(J(
    columns(
        ('50%', J(para('wet static', className='is-style-scrawl', fontSize='xx-large'),
                  para('Merch packed by the band in a back bedroom in Chapeltown, Leeds. Orders go out on Tuesdays and Saturdays, because those are the days nobody has work.', fontSize='small'))),
        (None, J(heading('Write to us', 6),
                 para('Wet Static merch<br>PO Box 4471<br>Leeds LS7 9ZX<br><a href="mailto:merch@example.com">merch@example.com</a>', fontSize='small'))),
        (None, J(heading('Before you email', 6),
                 para('<a href="/size-guide/">Size guide</a><br><a href="/shipping/">Shipping and returns</a><br><a href="/faq/">Questions</a><br><a href="/in-production/">In production</a>', fontSize='small'))),
        align='wide'),
    para('Demo photos are CC0 images from Wikimedia Commons, photocopied by the theme. No real band artwork is used.', align='wide', className='alignwide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', style={'spacing': {'padding': dict(top='var:preset|spacing|60', bottom='var:preset|spacing|50', **PAD_X), 'margin': {'top': 'var:preset|spacing|70'}},
                                       'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'dashed'}}}))

# ---------- templates ----------
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('drop-hero'), pattern_ref('drop-sheet'), pattern_ref('drop-feature'), pattern_ref('in-production-strip'),
    pattern_ref('past-drops-latest'), pattern_ref('restock-signup'))))
write('templates/page.html', page_template(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'})), style=MAINPAD))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1280px'})), style=MAINPAD))
drop_item = J(dyn('post-featured-image', isLink=True, aspectRatio='4/5', scale='cover'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=18, fontSize='small'))
write('templates/home.html', page_template(J(
    heading('Past drops', 1, align='wide'),
    para('Everything we have ever made, sold out or not. Some of it comes back as a second batch if enough people ask. Most of it does not.', align='wide', className='alignwide'),
    dyn('categories', className='is-style-default', showPostCounts=False),
    pattern_ref('drop-archive')), style=MAINPAD))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('drop-archive')), style=MAINPAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), style=MAINPAD))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='tees, tapes, drop four', buttonText='Search'), pattern_ref('post-list')), style=MAINPAD))
write('templates/404.html', page_template(J(
    heading('Lost in the post', 1),
    para('This page is gone, or it was never printed. Try the <a href="/shop/">shop</a> or the <a href="/past-drops/">past drops pile</a>.'),
    dyn('search', label='Search', showLabel=False, placeholder='tees, tapes, drop four', buttonText='Search')), style=MAINPAD))
write('templates/single.html', page_template(J(
    columns(('50%', dyn('post-featured-image', aspectRatio='4/5', scale='cover')),
            (None, J(dyn('post-terms', term='category'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-date'), dyn('post-content', layout={'type': 'default'}))),
            align='wide'),
    group(J(dyn('post-navigation-link', type='previous', label='Older drop', showTitle=True), dyn('post-navigation-link', label='Newer drop', showTitle=True)),
          align='wide', layout={'type': 'flex', 'justifyContent': 'space-between'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}})), style=MAINPAD))

# ---------- patterns ----------
img = image
SEC = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

pattern('drop-hero', 'Current drop: the wall', 'drop,featured', group(J(
    heading('drop seven: the car park session', 1, align='wide'),
    columns(
        ('58%', img('hero.jpg', 'A guitarist with pale hair playing under a single stage light, photographed in black and white', 'Leeds Brudenell, back room, September', lightbox=False)),
        (None, group(J(
            para('Six things, printed and dubbed by us, on sale until Sunday 2 November. Tees and tapes are limited and the numbers below are real. The hoodie is a pre-order: we print it once the drop closes, so you get it in the last week of November.'),
            para('When a number hits zero, it is gone. We might do a second batch of the tape. We will not do a second batch of the longsleeve, because Priya hated screen-printing the sleeves.', fontSize='small'),
            para('6 longsleeves left', className='is-style-scrawl'),
            buttons(('See the stock sheet', '#sheet'), ('Go to the shop', '/shop/'))), className='is-style-scrap', layout={'type': 'default'})),
        align='wide')), align='wide', layout={'type': 'default'}, style=SEC),
    description='Front page opener for the current drop: title, a photocopied photo and a taped note with the close date.')

SHEET = [['Car park tee, black', 'Screen print, one colour, S to XXL', '£22', '38 left'],
         ['Static bloom longsleeve', 'Two colours, printed sleeves, S to XL', '£30', '6 left'],
         ['Heavy hoodie, washed black', 'Pre-order, in production', '£45', 'ships 24 to 29 Nov'],
         ['Songs for the car park, tape', 'C40, chrome, 100 dubbed', '£8', '<s>sold out</s>'],
         ['Soft engine, 12" LP', 'Black vinyl, printed inner sleeve', '£24', 'in stock'],
         ['Zine, issue three', '40 pages, photocopied, stapled', '£5', '22 left']]
pattern('drop-sheet', 'Drop stock sheet (typed list with counts)', 'drop,shop', group(J(
    heading('stock sheet, typed on 12 October', 2, anchor='sheet'),
    table(SHEET, head=['What', 'Details', 'Price', 'Left'], className='is-style-typed-list'),
    para('We update these numbers by hand when we pack, so they can be a day behind. If the shop lets you buy it, it exists.', fontSize='small')),
    className='is-style-scrap-right', align='wide', layout={'type': 'constrained', 'contentSize': '980px'}),
    description='The signature: a typed list of this drop with real counts, a batch window for pre-orders, and sold-out items kept visible.')

pattern('drop-feature', 'One item, one screen', 'drop,shop', group(columns(
    ('55%', img('tee.jpg', 'A rail of cotton t-shirts on wooden hangers in a shop, in black, grey, green and orange', lightbox=False)),
    (None, J(heading('car park tee', 2),
             para('Heavy cotton, black, one-colour screen print on the front: a photo of our van in the Brudenell car park at 2am, photocopied three times until it went strange. Sizes S to XXL. Printed by Priya at Hyde Park Print Club.'),
             para('£22', fontSize='xx-large', className='is-style-scrawl'),
             para('38 left out of 200', fontSize='large'),
             buttons(('Buy the tee', '/shop/')))), align='wide', verticalAlignment='center'),
    align='full', className='is-style-toner', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))

pattern('in-production-strip', 'In production (pre-orders)', 'drop,shop', group(columns(
    (None, group(J(
        heading('in production', 3),
        para('<strong>Heavy hoodie, washed black.</strong> Pre-order until 2 November. We order the blanks the next morning, print the week after, and post the first batch between 24 and 29 November.'),
        para('Pre-orders ship on their own. If you order a tee with it, the tee comes now and the hoodie comes later, and you only pay postage once.', fontSize='small'),
        buttons(('Pre-order the hoodie', '/shop/'))), className='is-style-scrap', layout={'type': 'default'})),
    (None, group(J(
        heading('missed the tape?', 3),
        para('<strong>Songs for the car park</strong> sold out in four days. If 50 people put their name down, Mags will dub a second batch of 100 in December. Right now 31 have.'),
        para('Put your name down', className='is-style-scrawl'),
        buttons(('Email us about batch two', 'mailto:merch@example.com?subject=Tape%20batch%20two'))), className='is-style-scrap-right', layout={'type': 'default'})),
    align='wide'), align='wide', layout={'type': 'default'}, style=SEC))

pattern('in-production-page', 'Page: in production', 'drop', J(
    para('Some things we only make once we know how many to make. Those are listed here with the week they will ship. We never charge you and then go quiet: if a batch slips, we email everyone who ordered with a new date.'),
    table([['Heavy hoodie, washed black', 'Pre-order until 2 Nov', 'Ships 24 to 29 Nov'],
           ['Songs for the car park, tape, batch two', 'Waiting list, 31 of 50', 'December, if it happens'],
           ['Soft engine, 12" LP, second press', 'Pressing plant queue', 'Late January']], head=['What', 'Where it is', 'When'], className='is-style-typed-list'),
    pattern_ref('ships-separately'), pattern_ref('second-batch')), block_types='core/post-content')

pattern('ships-separately', 'Pre-orders ship separately', 'drop,shop', group(J(
    heading('pre-orders ship on their own', 4),
    para('If your basket has a pre-order and something in stock, we send the in-stock part now and the pre-order when it is made. You pay postage once. Your order page says which parcel is which.')),
    className='is-style-scrap-flat', layout={'type': 'constrained'}))

pattern('second-batch', 'Missed out: second batch note', 'drop,shop', group(J(
    para('sold out', className='is-style-stamp'),
    para('Missed it? Email <a href="mailto:merch@example.com?subject=Second%20batch">merch@example.com</a> with the item name. If enough people ask, we make a second batch and email you first. Asking is free, and we only use your email for this.')),
    className='is-style-scrap-right', layout={'type': 'constrained'}))

pattern('past-drops-latest', 'Past drops (latest four)', 'drop,query', group(J(
    heading('the past drops pile', 2),
    para('Sold out stays up. It is the closest thing we have to a discography of t-shirts. <a href="/past-drops/">See every drop</a>'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='4/5', scale='cover'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-date')),
          per_page=4, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}, align='wide', template_class='is-style-xerox-grid')),
    align='wide', layout={'type': 'default'}, style=SEC))

pattern('drop-archive', 'Drops archive (inherits the page query)', 'drop,query', inherit_query(drop_item,
    layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}, template_class='is-style-xerox-grid', align='wide'), inserter=False)

pattern('post-list', 'Post list', 'drop,query', inherit_query(J(
    row(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-date')), justify='space-between')), align='wide'), inserter=False)

pattern('sold-out-record', 'Sold out, kept on the wall', 'drop,shop', group(J(
    heading('what already went', 3),
    table([['Drop six', 'Flood tee, white', '<s>150</s>', 'sold out in 9 days'],
           ['Drop five', 'Tour tote', '<s>80</s>', 'sold out at the Glasgow show'],
           ['Drop four', 'Lighthouse longsleeve', '<s>60</s>', 'sold out'],
           ['Drop three', 'Demo tape, C30', '<s>50</s>', 'sold out, mostly to our mums']], head=['Drop', 'What', 'Made', 'What happened'], className='is-style-typed-list')),
    className='is-style-scrap-flat', layout={'type': 'constrained', 'contentSize': '980px'}))

pattern('size-guide', 'Size guide (flat measurements)', 'drop,shop', group(J(
    heading('tees, measured flat', 3),
    table([['S', '48 cm / 19 in', '71 cm / 28 in'], ['M', '53 cm / 21 in', '74 cm / 29 in'], ['L', '58 cm / 23 in', '76 cm / 30 in'],
           ['XL', '63 cm / 25 in', '79 cm / 31 in'], ['XXL', '68 cm / 27 in', '81 cm / 32 in']],
          head=['Size', 'Chest, armpit to armpit', 'Length, collar to hem'], className='is-style-typed-list'),
    heading('hoodie, measured flat', 3),
    table([['S', '56 cm / 22 in', '68 cm / 27 in'], ['M', '60 cm / 23.5 in', '71 cm / 28 in'], ['L', '64 cm / 25 in', '74 cm / 29 in'], ['XL', '68 cm / 27 in', '76 cm / 30 in']],
          head=['Size', 'Chest', 'Length'], className='is-style-typed-list')),
    layout={'type': 'constrained'}))

pattern('size-compare', 'Compare with a tee you own', 'drop,shop', group(J(
    heading('the tee in your drawer trick', 4),
    lst(['Take a tee that fits how you like.', 'Lay it flat on the floor, smooth it out.', 'Measure straight across, armpit to armpit. That is the chest number.', 'Pick our size with the closest chest number. Between two? Go up. They shrink about 3% on a hot wash.'], ordered=True)),
    className='is-style-scrap', layout={'type': 'constrained'}))

pattern('size-guide-page', 'Page: size guide', 'drop', J(pattern_ref('size-compare'), pattern_ref('size-guide'), pattern_ref('care')), block_types='core/post-content')

pattern('care', 'Washing', 'drop,text', group(J(
    heading('washing', 4),
    para('Inside out, 30°C, no tumble dryer. The print will crack a little over the years. That is how it is supposed to look.')),
    layout={'type': 'constrained'}))

pattern('shipping', 'Shipping by region', 'drop,shop', group(J(
    heading('where it goes and how long', 3),
    table([['UK', '£3.50, free over £40', '2 to 4 days after we post'], ['Europe', '£8', '5 to 10 days, we pay the VAT'],
           ['USA and Canada', '£12', '8 to 15 days'], ['Australia and NZ', '£14', '10 to 20 days'], ['Everywhere else', '£14', '10 to 25 days']],
          head=['Where', 'Postage', 'Usually takes'], className='is-style-typed-list'),
    para('We post on Tuesdays and Saturdays from the Chapeltown post office. You get a tracking number when it leaves.', fontSize='small')),
    layout={'type': 'constrained'}))

pattern('region-edition', 'Region-only edition note', 'drop,shop', group(J(
    para('UK and Europe only', className='is-style-stamp'),
    para('The LP is pressed in Czechia, and posting a single record to the US now costs more than the record. Our US label, Dead Letter Office in Portland, sells it over there.')),
    className='is-style-scrap-flat', layout={'type': 'constrained'}))

pattern('returns', 'Returns', 'drop,text', group(J(
    heading('returns', 3),
    lst(['Wrong size? Send it back unworn within 30 days and we swap it, if we still have your size.',
         'Faulty print or a hole? Email a photo. We send a new one and you keep the old one.',
         'Tapes and zines can\'t be returned once opened, unless they are faulty.',
         'Sold-out items can only be refunded, since there is nothing left to swap for.'])),
    layout={'type': 'constrained'}))

pattern('shipping-page', 'Page: shipping and returns', 'drop', J(pattern_ref('shipping'), pattern_ref('ships-separately'), pattern_ref('region-edition'), pattern_ref('returns')), block_types='core/post-content')

pattern('faq', 'Questions', 'drop,text', group(J(
    details('Do the numbers on the stock sheet go down live?', para('The shop numbers do. The typed sheet on the front page is updated when we pack, so it can be a day behind.')),
    details('Can I pick up at a show?', para('Yes. Choose "collect at a show" at checkout and pick the date. Your order is in a bag with your name on it at the merch table.')),
    details('Will you make the longsleeve again?', para('No. Priya has asked us not to say the word sleeve near her.')),
    details('Where are the blanks from?', para('Tees and hoodies are organic cotton blanks from a supplier in Leicester. We print them ourselves at Hyde Park Print Club, Leeds.')),
    details('Do you do wholesale?', para('For record shops, yes, LPs and tapes only. Email us with the shop name.'))),
    layout={'type': 'constrained'}))

pattern('faq-page', 'Page: questions', 'drop', J(pattern_ref('faq'), pattern_ref('who-packs')), block_types='core/post-content')

pattern('who-packs', 'Who packs your order', 'drop,about', group(columns(
    ('40%', img('live.jpg', 'A drummer playing a full kit under two bright stage lights, black and white', 'Tom, drums and parcels', lightbox=False)),
    (None, J(heading('who packs your order', 3),
             para('Wet Static is Mags Obi (guitar, voice), Priya Rana (bass, the screen) and Tom Keane (drums, the parcel tape). We started selling tees out of a holdall at shows in 2021 and never stopped.'),
             para('We pack every order ourselves and write the address by hand, so if your parcel says "LS7" in huge letters, that was Tom.'),
             para('The drop ends when the notice bar says it ends, and the numbers on the sheet are the ones on our shelf.', fontSize='small'))), align='wide'),
    align='wide', className='is-style-scrap-flat', layout={'type': 'constrained'}))

pattern('restock-signup', 'Drop alerts sign-up', 'drop,call-to-action', group(J(
    heading('get the next drop first', 2),
    para('One email when a drop opens and one when a sold-out thing comes back. Around six emails a year. Mags writes them on her phone, so expect typos.'),
    buttons(('Email us to join the list', 'mailto:merch@example.com?subject=Drop%20list'))),
    className='is-style-scrap', align='wide', layout={'type': 'constrained'}, anchor='list', style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))

pattern('bundle', 'Bundle: tee and record', 'drop,shop', group(columns(
    (None, img('vinyl.jpg', 'A person sliding a record out of its sleeve next to a turntable', lightbox=False)),
    (None, J(heading('tee and LP', 3), para('The car park tee and the Soft engine LP for £40 instead of £46. Pick your size at checkout. The record is UK and Europe only, see below.'),
             para('£40', className='is-style-scrawl', fontSize='xx-large'), buttons(('Buy the bundle', '/shop/')))), align='wide', verticalAlignment='center'),
    align='wide', className='is-style-scrap-right', layout={'type': 'constrained'}))

pattern('shows', 'Merch at shows', 'drop,text', group(J(
    heading('merch table dates', 3),
    table([['Thu 30 Oct', 'Hyde Park Book Club, Leeds', 'Collection point'], ['Sat 8 Nov', 'The Hug and Pint, Glasgow', 'Collection point'],
           ['Fri 14 Nov', 'Moth Club, London', 'Card only at the table'], ['Sat 22 Nov', 'Gullivers, Manchester', 'Last show of the year']],
          head=['Date', 'Where', 'Note'], className='is-style-typed-list')),
    layout={'type': 'constrained'}))

pattern('print-process', 'How we print', 'drop,about', group(columns(
    (None, img('print.jpg', 'Two pairs of hands pulling a squeegee across a screen-printing frame with red ink', 'Hyde Park Print Club, Thursday night', lightbox=False)),
    (None, J(heading('printed on a Thursday', 3),
             para('Priya prints every tee on the club\'s four-colour press, 30 an hour on a good night. One colour costs us about £6 a shirt including the blank. The price on the sheet pays for that, the postage bags and the van\'s MOT.'))),
    align='wide', verticalAlignment='center'), align='wide', layout={'type': 'default'}, style=SEC))

pattern('tape-feature', 'Tape feature', 'drop,shop', group(J(
    img('tape.jpg', 'Two cassette tapes side by side on a dark table', lightbox=False),
    para('dubbed in real time on a Tascam, one side at a time, 100 copies. Each one took 20 minutes. Please play it.', className='is-style-scrawl')),
    className='is-style-scrap', layout={'type': 'constrained'}))

pattern('notice-post-dates', 'Notice: last posting dates', 'drop,banner', group(
    para('Last UK posting day before Christmas is Saturday 20 December. Anything ordered after that goes out on 6 January.', align='center'),
    tag='section', align='full', className='is-style-notice', style={'spacing': {'padding': dict(top='var:preset|spacing|20', bottom='var:preset|spacing|20', **PAD_X)}}),
    description='Swap into the Drop notice template part in December and remove it after.')

pattern('about-page', 'Page: the band', 'drop', J(pattern_ref('who-packs'), pattern_ref('print-process'), pattern_ref('shows')), block_types='core/post-content')

pattern('contact', 'Contact', 'drop,contact', group(J(
    para('Email <a href="mailto:merch@example.com">merch@example.com</a> with your order number. Mags answers on Mondays and Thursdays. Please don\'t DM the band account about orders: nobody checks it sober.'),
    para('Post: Wet Static merch, PO Box 4471, Leeds LS7 9ZX.')), layout={'type': 'constrained'}))

print('drop: build done')
