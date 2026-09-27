# platter: design note
# Direction: the kitchen pass. Big fat slab type, tomato, mustard and pickle green, food photographed close and hot.
#   The owner asked for tastier, less elegant and more fun, so the research's austere white look is dropped.
# Why: a caterer sells appetite first. Jobs are shown as kitchen order tickets pinned to a rail, because that is how the
#   team actually sees an event: venue, covers, what goes out and when.
# Fonts: Bevan (display, heavy slab like a deli sign, with a real italic), Karla (body, tabular figures for prices and covers).
# Palette: white, espresso brown ink, tomato red, mustard, pickle green. Gingham tablecloth band for the enquiry.
# Layout idea: the ticket rail. Case studies are white tickets with a torn zigzag bottom on a tomato band; prices sit in
#   round tomato stickers; menus are set centred like a printed card but in a loud slab.
import sys, json, os; sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('platter')
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
    ('base', '#FFFFFF', 'Plate'),
    ('contrast', '#2A170E', 'Espresso'),
    ('accent', '#C4301A', 'Tomato'),
    ('accent-2', '#2E6B35', 'Pickle'),
    ('surface', '#FFD35C', 'Mustard'),
    ('line', '#2A170E', 'Espresso line'),
    ('muted', '#5C4638', 'Gravy'),
    ('cream', '#FFF1CF', 'Custard'),
]


def palette(over=None):
    over = over or {}
    return [{'slug': s, 'color': over.get(s, c), 'name': n} for s, c, n in PAL]


V = lambda s: 'var(--wp--preset--color--%s)' % s
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
                {'slug': 'x-small', 'size': '0.9375rem', 'name': 'Allergens', 'fluid': False},
                {'slug': 'small', 'size': '1.0625rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.625rem', 'name': 'Dish', 'fluid': {'min': '1.3rem', 'max': '1.625rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Course', 'fluid': {'min': '1.9rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4.25rem', 'name': 'Title', 'fluid': {'min': '2.6rem', 'max': '4.25rem'}},
                {'slug': 'display', 'size': '7.5rem', 'name': 'Sign', 'fluid': {'min': '3.1rem', 'max': '7.5rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3.5vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': [{'slug': 'ticket', 'name': 'Ticket on the rail', 'shadow': '0 3px 0 0 rgba(42,23,14,.35)'}]},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'custom': {'gingham': 'repeating-linear-gradient(0deg,transparent 0 24px,rgba(196,48,26,.45) 24px 48px),repeating-linear-gradient(90deg,transparent 0 24px,rgba(196,48,26,.45) 24px 48px)'},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent-2', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '1', 'letterSpacing': '-0.015em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'lineHeight': '0.92'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '800', 'lineHeight': '1.3'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                'border': {'radius': '6px', 'width': '0'},
                'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|medium'},
                'spacing': {'padding': {'top': '0.8em', 'bottom': '0.8em', 'left': '1.3em', 'right': '1.3em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|surface'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent-2', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'italic'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '0.95', 'letterSpacing': '-0.02em'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}},
                                'css': '& .wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--surface);padding:var(--wp--preset--spacing--50)}& .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large);font-weight:400}& .current-menu-item > a{text-decoration:underline;text-decoration-thickness:3px;text-decoration-color:var(--wp--preset--color--accent)}'},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
            'core/image': {'border': {'radius': '10px'}, 'css': '& img{border-radius:10px}'},
            'core/post-featured-image': {'css': '& img{border-radius:10px}'},
            'core/separator': {'color': {'text': 'var:preset|color|accent'}, 'border': {'width': '4px 0 0 0', 'style': 'dotted'}, 'css': '&{border-bottom:0!important;max-width:none}'},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.25'},
                           'border': {'width': '0'}, 'spacing': {'padding': {'left': '0'}},
                           'css': '&::before{content:"\\201C";display:block;font-family:var(--wp--preset--font-family--display);font-size:4rem;line-height:.6;color:var(--wp--preset--color--accent)}& cite{font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--x-small);font-style:normal;font-weight:700}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table{border-collapse:collapse}& th{text-align:left;font-family:var(--wp--preset--font-family--display);font-weight:400;border:0!important;border-bottom:3px solid var(--wp--preset--color--contrast)!important}& td{border:0!important;border-bottom:2px dotted var(--wp--preset--color--muted)!important;font-variant-numeric:tabular-nums}& td,& th{padding:.6em .8em .6em 0}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'dotted'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large)}'},
            'core/search': {'css': '& .wp-block-search__input{border:3px solid var(--wp--preset--color--contrast);border-radius:6px}'},
            'core/categories': {'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.6rem}& li a{display:inline-block;padding:.4em 1em;background:var(--wp--preset--color--surface);color:var(--wp--preset--color--contrast);border-radius:6px;text-decoration:none;font-weight:800}& li a:hover{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--surface)}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none}a:focus-visible,button:focus-visible{outline:3px solid var(--wp--preset--color--accent-2);outline-offset:3px}:where(td){font-variant-numeric:tabular-nums}',
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
                        {'name': 'page-menu', 'title': 'Menu page (mustard title, centred menu)', 'postTypes': ['page']}],
}
wjson('theme.json', theme)

V3 = lambda title, pal: {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': palette(pal)}}}
wjson('styles/garden-party.json', V3('Garden party', {'base': '#F3F8EC', 'accent': '#2E6B35', 'accent-2': '#B32E17', 'surface': '#CFE6B0', 'cream': '#FFFFFF', 'contrast': '#17260F', 'muted': '#43533A', 'line': '#17260F'}))
wjson('styles/late-service.json', V3('Late service', {'base': '#2A170E', 'contrast': '#FFF1CF', 'accent': '#FF8A6B', 'accent-2': '#A9D98C', 'surface': '#4A2E1A', 'cream': '#3B2418', 'muted': '#E3CDB6', 'line': '#FFF1CF'}))
wjson('styles/ketchup.json', V3('Ketchup and mayo', {'base': '#FFF8EE', 'accent': '#B3121B', 'surface': '#FFE9B8', 'accent-2': '#1F5C8C', 'cream': '#FFFFFF', 'muted': '#5A3A33', 'contrast': '#2B0F0B'}))

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

BAND = {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}
section('tomato', 'Tomato band', ['core/group', 'core/columns'],
        {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'spacing': {'padding': BAND},
         'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                      'button': {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}}}})
section('mustard', 'Mustard band', ['core/group', 'core/columns', 'core/column'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'spacing': {'padding': BAND},
         'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}}})
section('pickle', 'Pickle band', ['core/group', 'core/columns', 'core/column'],
        {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|base'}, 'spacing': {'padding': BAND},
         'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|surface'}},
                      'button': {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}}}})
section('gingham', 'Gingham tablecloth', ['core/group'],
        {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}, 'spacing': {'padding': BAND},
         'css': '&{background-image:var(--wp--custom--gingham)}'})
ZIG = 'polygon(0 0,100% 0,100% calc(100% - 10px),95% 100%,90% calc(100% - 10px),85% 100%,80% calc(100% - 10px),75% 100%,70% calc(100% - 10px),65% 100%,60% calc(100% - 10px),55% 100%,50% calc(100% - 10px),45% 100%,40% calc(100% - 10px),35% 100%,30% calc(100% - 10px),25% 100%,20% calc(100% - 10px),15% 100%,10% calc(100% - 10px),5% 100%,0 calc(100% - 10px))'
TICKET_CSS = '{background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast);padding:var(--wp--preset--spacing--40) var(--wp--preset--spacing--40) calc(var(--wp--preset--spacing--40) + 12px);clip-path:%s;border-top:10px solid var(--wp--preset--color--contrast)}' % ZIG
section('ticket', 'Order ticket', ['core/group', 'core/column'],
        {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
         'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}, 'heading': {'color': {'text': 'var:preset|color|contrast'}}},
         'css': '&' + TICKET_CSS})
section('ticket-rail', 'Ticket rail', ['core/post-template'],
        {'css': '& > li' + TICKET_CSS + '& > li:nth-child(3n+1){transform:rotate(-1.2deg)}& > li:nth-child(3n+2){transform:rotate(.8deg) translateY(10px)}& > li:nth-child(3n){transform:rotate(-.4deg)}& > li a{color:var(--wp--preset--color--contrast)}& > li h3 a{text-decoration:none}& .wp-block-post-excerpt{font-size:var(--wp--preset--font-size--small)}'})
section('sticker', 'Price sticker', ['core/paragraph'],
        {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
         'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.05'},
         'css': '&{display:inline-flex;align-items:center;justify-content:center;text-align:center;width:8.5rem;height:8.5rem;border-radius:50%;padding:1rem;transform:rotate(-10deg)}'})
section('menu-card', 'Printed menu card', ['core/group'],
        {'color': {'background': 'var:preset|color|cream', 'text': 'var:preset|color|contrast'},
         'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
         'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
         'css': '&{text-align:center;outline:3px solid var(--wp--preset--color--contrast);outline-offset:-12px}& p{margin-inline:auto}'})
section('dish', 'Dish line', ['core/paragraph'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15'}})

write('style.css', '''/*
Theme Name: Platter
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A loud, hungry theme for independent event caterers doing weddings, film crews, private dinners and office lunches, with jobs shown as kitchen order tickets.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: platter
Tags: food-and-drink, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')
write('functions.php', '''<?php
/**
 * Platter: pattern category only.
 *
 * @package platter
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'platter', array( 'label' => __( 'Platter: catering', 'platter' ) ) );
	}
);''')

PX = {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}
write('parts/header.html', J(
    group(para('Christmas parties: two Fridays left in December, 12th and 19th. Office lunch orders by 2pm for next-day delivery.', align='center', fontSize='x-small'),
          tag='section', align='full', className='is-style-mustard', style={'spacing': {'padding': dict(top='var:preset|spacing|20', bottom='var:preset|spacing|20', **PX)}}),
    group(row(J(dyn('site-title', level=0), dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}),
                buttons(('Start your brief', '/enquire/'))), justify='space-between', align='wide'),
          tag='section', align='full', style={'spacing': {'padding': dict(top='var:preset|spacing|30', bottom='var:preset|spacing|30', **PX)}})))
write('parts/footer.html', group(J(
    columns(
        ('45%', J(para('Second Helpings', fontSize='xx-large', fontFamily='display'),
                  para('Event catering from a kitchen under the railway arches in St Werburghs, Bristol. Femi cooks, Rosa runs the day, and eleven more people carry the trays.', fontSize='small'))),
        (None, J(heading('The kitchen', 6),
                 para('Arch 7, Mina Road<br>St Werburghs, Bristol BS2 9YT<br>Tastings by appointment, Tuesday to Thursday', fontSize='small'))),
        (None, J(heading('Get hold of us', 6),
                 para('<a href="mailto:hungry@example.com">hungry@example.com</a><br>0117 496 0382, 9am to 5pm weekdays<br><a href="/enquire/">Start your brief</a>', fontSize='small'))),
        align='wide'),
    para('Demo photos are CC0 images from Wikimedia Commons, standing in for our own.', align='wide', className='alignwide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-pickle', style={'spacing': {'padding': dict(top='var:preset|spacing|60', bottom='var:preset|spacing|50', **PX), 'margin': {'top': '0'}}}))

MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero'), pattern_ref('event-types'), pattern_ref('ticket-rail'), pattern_ref('seasonal-menu'), pattern_ref('suppliers-strip'), pattern_ref('enquiry-brief')),
    style={'spacing': {'padding': {'top': '0', 'bottom': '0'}, 'margin': {'top': '0'}}}))
write('templates/page.html', page_template(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'})), style=MAINPAD))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})), style=MAINPAD))
write('templates/page-menu.html', page_template(J(
    group(dyn('post-title', level=1, align='wide'), tag='section', align='full', className='is-style-mustard'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})), style={'spacing': {'padding': {'bottom': 'var:preset|spacing|70'}}}))
ticket = J(dyn('post-terms', term='category'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30), dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover'))
write('templates/home.html', page_template(J(
    group(J(heading('Recent jobs', 1, align='wide'),
            para('Every event we cater gets a ticket on the rail in the kitchen: where, how many, what went out. These are the recent ones. Pick a type of event to see only those.', align='wide', className='alignwide'),
            dyn('categories', align='wide')), tag='section', align='full', className='is-style-mustard'),
    group(pattern_ref('ticket-archive'), tag='section', align='full', className='is-style-tomato')),
    style={'spacing': {'padding': {'top': '0', 'bottom': '0'}}}))
write('templates/archive.html', page_template(J(
    group(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), dyn('categories', align='wide')), tag='section', align='full', className='is-style-mustard'),
    group(pattern_ref('ticket-archive'), tag='section', align='full', className='is-style-tomato')),
    style={'spacing': {'padding': {'top': '0', 'bottom': '0'}}}))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), style=MAINPAD))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='weddings, paella, crew', buttonText='Search'), pattern_ref('post-list')), style=MAINPAD))
write('templates/404.html', page_template(J(
    heading('This one got dropped on the way out', 1),
    para('The page has moved or never existed. The <a href="/menus/">menus</a> and <a href="/recent-jobs/">recent jobs</a> are still where they should be.'),
    dyn('search', label='Search', showLabel=False, placeholder='weddings, paella, crew', buttonText='Search')), style=MAINPAD))
write('templates/single.html', page_template(J(
    dyn('post-featured-image', align='wide', aspectRatio='21/9', scale='cover'),
    columns(('38%', group(J(dyn('post-terms', term='category'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-date')), className='is-style-ticket', layout={'type': 'default'})),
            (None, dyn('post-content', layout={'type': 'default'})), align='wide', style={'spacing': {'margin': {'top': 'var:preset|spacing|50'}}}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous job', showTitle=True), dyn('post-navigation-link', label='Next job', showTitle=True)),
          align='wide', layout={'type': 'flex', 'justifyContent': 'space-between'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}})), style=MAINPAD))

img = image
pattern('hero', 'Hero: big tray of food', 'platter,featured', group(columns(
    ('46%', J(heading('Big trays of proper food, carried in hot.', 1),
              para('Weddings, film crews, office lunches and birthday dinners for 20 to 300, cooked in our Bristol kitchen and served family-style so people pass things and talk. Femi does the cooking. Rosa makes sure it arrives.', fontSize='large'),
              buttons(('Start your brief', '/enquire/'), ('See the menus', '/menus/', {'className': 'is-style-outline'})))),
    (None, J(img('paella.jpg', 'A wide paella pan over a fire, full of rice, mussels and red peppers, with a wooden spoon going in', lightbox=False),
             para('Paella for 140 from £18 a head', className='is-style-sticker'))),
    align='wide', verticalAlignment='center'), tag='section', align='full', className='is-style-mustard', layout={'type': 'constrained'}),
    description='Opener: headline, one short paragraph, two buttons, a big food photo with a round price sticker.')

pattern('event-types', 'Event types and what is included', 'platter,services', group(J(
    heading('What we cook for', 2),
    columns(
        (None, group(J(img('cake.jpg', 'A couple cutting a two-tier wedding cake covered in strawberries, mango and kiwi', lightbox=False),
                       heading('Weddings', 3), para('Sharing feasts, a late-night snack and the cake if you want it. From £38 a head, 60 to 220 guests.', fontSize='small'),
                       para('<a href="/category/weddings/">Wedding tickets on the rail</a>', fontSize='small')), layout={'type': 'default'})),
        (None, group(J(img('tacos.jpg', 'Four loaded tacos in paper boats lined with red and white checked paper, with three small sauce pots', lightbox=False),
                       heading('Film and TV crews', 3), para('Breakfast at call time, hot lunch, and a 4pm tray of something sweet. £16 a head a day, 20 to 120 crew.', fontSize='small'),
                       para('<a href="/category/crew/">Crew tickets on the rail</a>', fontSize='small')), layout={'type': 'default'})),
        (None, group(J(img('sandwiches.jpg', 'Heart-shaped seeded rolls filled with ham and salad on a silver tray', lightbox=False),
                       heading('Offices', 3), para('Boxed lunches and sharing platters, delivered by 12:30. From £11.50 a head, minimum 10.', fontSize='small'),
                       para('<a href="/office-lunches/">Order office lunches</a>', fontSize='small')), layout={'type': 'default'})),
        (None, group(J(img('roast.jpg', 'A plate of roast chicken with roast potatoes, lettuce and carrots on a table outside', lightbox=False),
                       heading('Dinners at home', 3), para('We cook in your kitchen for 8 to 30, wash up and leave. From £55 a head with two staff.', fontSize='small'),
                       para('<a href="/category/private/">Dinner tickets on the rail</a>', fontSize='small')), layout={'type': 'default'})),
        align='wide'),
    para('Every event includes the food, the staff to serve it, plates and cutlery, and taking the rubbish away. Drinks and styling are extra and quoted on the brief.', align='wide', className='alignwide', fontSize='small')),
    tag='section', align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|60'}}}))

pattern('ticket-rail', 'Recent jobs on the ticket rail', 'platter,query', group(J(
    row(J(heading('On the rail', 2), para('<a href="/recent-jobs/">All the recent jobs</a>')), justify='space-between', align='wide'),
    query(ticket, per_page=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '17rem'}, align='wide', template_class='is-style-ticket-rail')),
    tag='section', align='full', className='is-style-tomato', layout={'type': 'constrained'}),
    description='The signature: case studies as kitchen tickets with venue, guest count and what was served.')

pattern('ticket-archive', 'Ticket rail (inherits the page query)', 'platter,query', inherit_query(ticket,
    layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '17rem'}, template_class='is-style-ticket-rail', align='wide'), inserter=False)

pattern('post-list', 'Post list', 'platter,query', inherit_query(J(
    row(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-date')), justify='space-between')), align='wide'), inserter=False)

pattern('job-record', 'Job record (venue, guests, format, menu)', 'platter,text', J(
    table([['Venue', 'Arnos Vale Cemetery, the Spielman Centre'], ['Guests', '140, plus 12 crew and 2 dogs'], ['Format', 'Family-style sharing feast, three waves'], ['Staff', '11 on the day, 2 in the kitchen'], ['Season', 'June']]),
    heading('What went out', 4),
    lst(['Flatbreads from the wood oven with whipped feta and chilli honey',
         'Paella in two 90 cm pans, one with chicken and chorizo, one with just vegetables',
         'Charred hispi cabbage, anchovy butter',
         'Burnt Basque cheesecake instead of a wedding cake, 6 of them']),
    para('What we would do differently: bring a third pan. The vegetable one went first.', fontSize='small')))

pattern('seasonal-menu', 'Seasonal menu with dates', 'platter,menu', group(columns(
    ('42%', J(img('mezze.jpg', 'A mezze plate of grilled vegetables, feta, flatbread and three dips on a wooden table', lightbox=False),
              para('Autumn menu, 1 October to 31 January', className='is-style-sticker'))),
    (None, J(heading('The autumn sharing feast', 2),
             para('Flatbreads, whipped feta, chilli honey', className='is-style-dish'),
             para('Slow lamb shoulder, pomegranate, herbs, or roast squash with the same', className='is-style-dish'),
             para('Crispy potatoes with too much garlic', className='is-style-dish'),
             para('Bitter leaves, orange, toasted hazelnuts', className='is-style-dish'),
             para('Sticky toffee pudding in trays, clotted cream', className='is-style-dish'),
             para('£42 a head, minimum 40. Vegan version of every dish on request, same price. Allergens on the <a href="/menus/#allergens">menu page</a>.', fontSize='small'),
             buttons(('Ask for this menu', '/enquire/')))), align='wide', verticalAlignment='center'),
    tag='section', align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))

pattern('canape-card', 'Canapé list (printed card)', 'platter,menu', group(J(
    heading('Canapés', 2),
    para('£2.20 each, choose five, minimum 50 of each', fontSize='small'),
    separator(),
    para('Crab on toast, brown butter, dill', className='is-style-dish'),
    para('Beef shin croquette, mustard mayo', className='is-style-dish'),
    para('Beetroot tartare, horseradish, rye (vg)', className='is-style-dish'),
    para('Mini jerk chicken bun, pineapple hot sauce', className='is-style-dish'),
    para('Parmesan custard tart, one anchovy', className='is-style-dish'),
    para('Fried sage leaves with honey, served in a paper cone (vg)', className='is-style-dish'),
    separator(),
    para('Femi says: five is the right number. Seven means nobody tries the last two.', fontSize='small')),
    className='is-style-menu-card', layout={'type': 'constrained'}))

pattern('allergen-matrix', 'Allergen matrix', 'platter,menu', group(J(
    heading('Allergens, autumn feast', 3, anchor='allergens'),
    table([['Flatbreads, whipped feta', 'yes', 'yes', '', '', ''], ['Slow lamb shoulder', '', '', '', '', 'yes'], ['Crispy potatoes', '', '', '', '', ''],
           ['Leaves, orange, hazelnuts', '', '', 'yes', '', 'yes'], ['Sticky toffee pudding', 'yes', 'yes', '', 'yes', '']],
          head=['Dish', 'Gluten', 'Milk', 'Nuts', 'Egg', 'Sulphites']),
    para('The kitchen handles all 14 allergens. We tell you the dietary counts from your guest list on the day, table by table. Print this table from the brochure PDF, which we email with every quote.', fontSize='small')),
    layout={'type': 'constrained'}))

pattern('menus-page', 'Page: menus', 'platter', J(pattern_ref('seasonal-menu'), pattern_ref('canape-card'), pattern_ref('allergen-matrix'), pattern_ref('brochure')), block_types='core/post-content')

pattern('office-lunch', 'Office lunch order list', 'platter,menu', group(J(
    heading('Office lunches', 2),
    para('Order by 2pm for next-day delivery across Bristol inside the ring road. Minimum 10 people. We deliver between 11:45 and 12:30 and collect the trays the next morning.'),
    table([['Boxed lunch: a grain salad, a filled flatbread, a cookie', '£11.50 a head'], ['Sharing platter: sandwiches on sourdough, 3 salads, fruit', '£14 a head'],
           ['Hot tray: chicken or aubergine curry, rice, pickles, flatbreads', '£15 a head'], ['Breakfast box: pastries, yoghurt pots, fruit', '£7.50 a head'],
           ['Tray of brownies, 24 pieces', '£36']], head=['What', 'Price']),
    buttons(('Email a lunch order', 'mailto:lunch@example.com?subject=Lunch%20order')),
    para('Order by email or phone with the date, the number of people, dietary needs and the delivery address. You get a confirmation within an hour.', fontSize='small')),
    layout={'type': 'constrained'}))

pattern('order-cutoff', 'Ordering cut-off note', 'platter,banner', group(
    para('<strong>Order by 2pm</strong> for delivery tomorrow. Orders after 2pm on Friday arrive on Tuesday. We don\'t deliver lunches at weekends.', align='center'),
    className='is-style-mustard', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}))

pattern('office-page', 'Page: office lunches', 'platter', J(pattern_ref('order-cutoff'), pattern_ref('office-lunch'), pattern_ref('lunch-photo')), block_types='core/post-content')

pattern('lunch-photo', 'Lunch photo pair', 'platter,gallery', gallery([
    ('lunchbox.jpg', 'A lunch box tray with grilled salmon, rolled omelette, fried chicken and rice with seaweed', 'A boxed lunch, lid off'),
    ('salad.jpg', 'A white bowl of green leaves on a wooden table outside, next to a bottle of olive oil', 'The grain salad before the grains')], columns=2, align='wide'))

pattern('suppliers-strip', 'Suppliers named', 'platter,about', group(J(
    heading('Who we buy from', 2),
    table([['Hart\'s Bakery', 'Sourdough, flatbread dough', 'Temple Meads, 1.5 miles'], ['Jon Thorner\'s', 'Lamb, beef shin, chicken', 'Pylle, Somerset, 26 miles'],
           ['Wyke Farms', 'Cheddar and butter', 'Bruton, 30 miles'], ['Sims Hill Shared Harvest', 'Leaves, squash, beetroot', 'Frenchay, 4 miles'],
           ['Fish for Thought', 'Crab, mackerel', 'Brixham, 105 miles, twice a week']], head=['Who', 'What', 'Where and how far'])),
    tag='section', align='wide', layout={'type': 'constrained', 'contentSize': '980px'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}))

pattern('suppliers-page', 'Page: suppliers and waste', 'platter', J(pattern_ref('suppliers-strip'), pattern_ref('sustainability')), block_types='core/post-content')

pattern('sustainability', 'Waste and packaging', 'platter,about', group(J(
    heading('What happens to the leftovers', 3),
    lst(['Anything not served goes home with guests in compostable boxes, if you want it to.',
         'What is left after that goes to the St Werburghs community fridge on Mina Road the same night.',
         'Food waste from the kitchen goes to the council\'s anaerobic digester. We weigh it: 38 kg in a normal week.',
         'We use real plates and cutlery for events. Office lunches come in card trays we collect and reuse.'])),
    layout={'type': 'constrained'}))

pattern('venues', 'Venues we know', 'platter,about', group(J(
    heading('Venues we know the back door of', 3),
    table([['Arnos Vale', 'Brislington', '220 seated'], ['The Mount Without', 'St Michael\'s Hill', '120 seated'], ['Paintworks event space', 'Arnos Vale', '180 seated'],
           ['Glastonbury Abbey barn', 'Somerset', '150 seated'], ['Your garden', 'Anywhere within 40 miles', 'As many as fit under the gazebo']],
          head=['Venue', 'Where', 'Capacity'])),
    layout={'type': 'constrained'}))

pattern('enquiry-brief', 'Start your brief (gingham)', 'platter,call-to-action', group(
    group(J(heading('Start your brief', 2),
            para('Email Rosa with the answers to these and she will send a menu, a price and a date to taste within three working days.'),
            lst(['The date, and a second choice if you have one', 'How many people, and how many are children', 'The venue, or the postcode if it is at home',
                 'A rough budget per head', 'Dietary needs you already know about', 'A floor plan if the venue has one'], ordered=True),
            buttons(('Email the brief to Rosa', 'mailto:hungry@example.com?subject=Event%20brief'))),
          className='is-style-ticket', layout={'type': 'constrained'}),
    tag='section', align='full', className='is-style-gingham', layout={'type': 'constrained', 'contentSize': '680px'}, anchor='brief'))

pattern('enquire-page', 'Page: enquire', 'platter', J(pattern_ref('enquiry-brief'), pattern_ref('booking-terms'), pattern_ref('faq')), block_types='core/post-content')

pattern('booking-terms', 'Booking terms, short', 'platter,text', group(J(
    heading('How booking works', 3),
    lst(['A 30% deposit holds the date. It is refundable until 90 days before.', 'Final numbers are due 14 days before. After that you can add people, and we can\'t take them off.',
         'The balance is due 7 days before the event.', 'Tastings are free for weddings over 60 guests and £60 for two otherwise, taken off the final bill.'])),
    layout={'type': 'constrained'}))

pattern('faq', 'Questions people ask', 'platter,text', group(J(
    heading('Questions people ask', 3),
    details('Do you do plated dinners?', para('For up to 80 people, yes. Past that, the food gets cold waiting for the last table, so we serve family-style.')),
    details('Can you bring the bar?', para('We work with Bristol Bar Co for drinks. We quote them on the same brief so you get one invoice.')),
    details('Do you need a kitchen at the venue?', para('A power socket, a trestle table and somewhere to park a van. We bring the ovens.')),
    details('Can you do halal, kosher or gluten-free?', para('Halal and gluten-free, yes, cooked separately. For kosher we recommend Kitchen 26 in Cardiff.'))),
    layout={'type': 'constrained'}))

pattern('brochure', 'Brochure for planners', 'platter,call-to-action', group(columns(
    (None, J(heading('The brochure', 3), para('Twelve pages: every menu, prices, the allergen tables and photos from real events. Planners and venues ask for it most. It comes as a PDF by email, updated each season.'))),
    ('30%', buttons(('Email me the brochure', 'mailto:hungry@example.com?subject=Brochure'))), verticalAlignment='center'),
    className='is-style-mustard', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}}))

pattern('team', 'The team', 'platter,about', group(columns(
    ('42%', img('grill.jpg', 'Chicken and steak cooking on a small charcoal grill set on grass', 'The grill Femi takes to every summer wedding', lightbox=False)),
    (None, J(heading('Who cooks, who carries', 2),
             para('Femi Adebayo cooked at Casamia and then at a lot of festival stalls before starting Second Helpings in 2018 with Rosa Lindqvist, who used to run events at Arnos Vale and knows where every venue keeps its fuse box.'),
             para('There are eleven of us now, plus a list of about thirty people who carry trays at weekends. Everyone who serves your food has eaten it, so they can answer "what\'s in this".'),
             para('Our opinion, for free: a buffet is great when it comes out hot, in waves, and somebody refills it. That is most of what we do.'))), align='wide', verticalAlignment='center'),
    align='wide', layout={'type': 'default'}))

pattern('reviews', 'What people said after', 'platter,testimonials', group(J(
    heading('What people said after', 2),
    columns(
        (None, quote('The lamb came out at 9pm in huge trays and the whole room went quiet. Our uncles still talk about the potatoes.', 'Ama and Joel, wedding at The Mount Without, August 2026')),
        (None, quote('Six weeks of night shoots and nobody complained about the food once, which has never happened.', 'Siân, production manager, crew catering in Avonmouth, March 2026')),
        align='wide')), align='wide', layout={'type': 'default'}))

pattern('about-page', 'Page: about', 'platter', J(pattern_ref('team'), pattern_ref('reviews'), pattern_ref('venues')), block_types='core/post-content')

pattern('events-page', 'Page: events', 'platter', J(pattern_ref('event-types'), pattern_ref('canape-card'), pattern_ref('booking-terms')), block_types='core/post-content')

pattern('pudding', 'Pudding trays', 'platter,menu', group(columns(
    (None, img('pastries.jpg', 'A berry and cinnamon swirl bread cut into slices on a glass tray, with a handwritten label', lightbox=False)),
    (None, J(heading('Pudding comes in trays', 3), para('Sticky toffee, rhubarb crumble, burnt cheesecake or a berry swirl like this one. We bring them out at the table and leave the spoons.'),
             para('£6 a head', className='is-style-sticker'))), align='wide', verticalAlignment='center'), align='wide', layout={'type': 'default'}))

pattern('cheese-course', 'Cheese board add-on', 'platter,menu', group(columns(
    (None, J(heading('Add a cheese board', 3), para('Three West Country cheeses, oat crackers, a sharp chutney and grapes. £7 a head, or £5 if it replaces pudding. Best for groups who stay late.'))),
    (None, img('cheese.jpg', 'A wooden board with blue cheese, a hard cheese, crackers, grapes, bread and two pots of chutney', lightbox=False)), align='wide', verticalAlignment='center'),
    className='is-style-mustard', align='wide', layout={'type': 'constrained'}))

print('platter: build done')
