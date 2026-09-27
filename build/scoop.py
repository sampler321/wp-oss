# scoop: design note
# Direction: a gelato lab's spec sheet. The owner asked for professional, toned-down, clean and technical, so the research's
#   shop-sign colour blocks are dropped for white space, hairlines and numbers.
# Why: a serious gelateria sells on method (churned at 7am, 24 pans, served at -12 °C) as much as on flavour. Showing the
#   sugar, fat and serving temperature of each flavour is what makes it look like people who know what they are doing.
# Fonts: Newsreader (display, light optical sizes, italic for flavour notes), Hanken Grotesk (body, tabular figures).
# Palette: white, green-black ink, a cool pistachio-grey surface, amarena cherry for links, dark pistachio for vegan marks.
# Layout idea: the cabinet map. The 24 pans of the display cabinet drawn as a numbered plan, specials marked, with the
#   monthly menu set as two columns of flavour lines and a spec row under each name.
import sys, json, os; sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('scoop')
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
    ('base', '#FFFFFF', 'Fior di latte'),
    ('contrast', '#1C2521', 'Ink'),
    ('accent', '#7A2233', 'Amarena'),
    ('accent-2', '#4E6B3A', 'Pistachio'),
    ('surface', '#F0F3EE', 'Pistachio mist'),
    ('line', '#1C2521', 'Hairline'),
    ('muted', '#56605A', 'Grey note'),
    ('rule', '#C8CFC6', 'Light rule'),
]


def palette(over=None):
    over = over or {}
    return [{'slug': s, 'color': over.get(s, c), 'name': n} for s, c, n in PAL]


theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1240px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette()},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Spec', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.625rem', 'name': 'Flavour', 'fluid': {'min': '1.35rem', 'max': '1.625rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '1.9rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.6rem', 'max': '4rem'}},
                {'slug': 'display', 'size': '7rem', 'name': 'Display', 'fluid': {'min': '3.2rem', 'max': '7rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.5rem, 6vw, 4.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3.5rem, 9vw, 7rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(5rem, 12vw, 10rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '300', 'lineHeight': '1.05', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'lineHeight': '0.95', 'fontWeight': '250'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '400', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0', 'lineHeight': '1.3'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                'border': {'radius': '999px', 'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.65em', 'bottom': '0.65em', 'left': '1.5em', 'right': '1.5em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'border': {'color': 'var:preset|color|accent'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '400', 'fontStyle': 'italic', 'letterSpacing': '-0.01em'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}},
                                'css': '& .wp-block-navigation__responsive-container.is-menu-open{padding:var(--wp--preset--spacing--50)}& .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large);font-weight:300}& .current-menu-item > a{text-decoration:underline;text-underline-offset:.35em;text-decoration-thickness:1px}'},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}},
            'core/image': {'border': {'radius': '2px'}},
            'core/separator': {'color': {'text': 'var:preset|color|rule'}, 'border': {'width': '1px 0 0 0'}, 'css': '&{border-bottom:0!important}'},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontStyle': 'italic', 'fontWeight': '300', 'lineHeight': '1.35'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                           'css': '& cite{font-family:var(--wp--preset--font-family--body);font-style:normal;font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--muted)}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table{border-collapse:collapse}& th{text-align:left;font-weight:500;color:var(--wp--preset--color--muted);border:0!important;border-bottom:1px solid var(--wp--preset--color--line)!important}& td{border:0!important;border-bottom:1px solid var(--wp--preset--color--rule)!important;font-variant-numeric:tabular-nums}& td,& th{padding:.65em 1em .65em 0}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|rule', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);font-weight:300}'},
            'core/search': {'css': '& .wp-block-search__input{border:1px solid var(--wp--preset--color--line);border-radius:999px;padding:.55em 1.1em}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/gallery': {'css': '& figcaption.wp-element-caption{background:none!important;position:static!important;color:var(--wp--preset--color--muted)!important;text-align:left!important;padding:.4em 0 0!important;font-size:var(--wp--preset--font-size--x-small)}& .wp-block-image{flex-direction:column}'},
        },
        'css': ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none;font-variant-numeric:tabular-nums lining-nums}h1,h2,h3{font-variation-settings:"opsz" 72}a:focus-visible,button:focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}',
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Weather and hours note'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
                        {'name': 'page-sheet', 'title': 'Spec sheet (title left, content right)', 'postTypes': ['page']}],
}
wjson('theme.json', theme)

V3 = lambda title, pal: {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': palette(pal)}}}
wjson('styles/stracciatella.json', V3('Stracciatella', {'accent': '#1C2521', 'accent-2': '#1C2521', 'surface': '#F2F2F2', 'rule': '#D0D0D0', 'contrast': '#111111', 'line': '#111111', 'muted': '#5A5A5A'}))
wjson('styles/notte.json', V3('Notte', {'base': '#1C2521', 'contrast': '#EEF1EC', 'accent': '#E6A3AE', 'accent-2': '#B7D39A', 'surface': '#26312C', 'line': '#EEF1EC', 'muted': '#B4BDB6', 'rule': '#3C4842'}))
wjson('styles/limone.json', V3('Limone', {'base': '#FBFAF1', 'surface': '#F1EFD6', 'accent': '#5E5410', 'accent-2': '#4E6B3A', 'rule': '#D8D5B8', 'contrast': '#1E1D14', 'line': '#1E1D14', 'muted': '#5A5846'}))

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('mist', 'Pistachio mist', ['core/group', 'core/columns', 'core/column'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
         'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}})
section('hairline-top', 'Hairline above', ['core/group', 'core/columns'],
        {'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})
section('hairline-bottom', 'Hairline below', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}})
section('flavour', 'Flavour line', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|rule', 'width': '1px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}, 'blockGap': 'var:preset|spacing|10'},
         'css': '& h4{margin:0}& .is-note{font-family:var(--wp--preset--font-family--display);font-style:italic;font-weight:300;font-size:var(--wp--preset--font-size--medium);margin:0}& .is-spec{font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--muted);margin:0}'})
section('spec', 'Spec line', ['core/paragraph'],
        {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}})
section('note', 'Italic note', ['core/paragraph'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontStyle': 'italic', 'fontWeight': '300', 'fontSize': 'var:preset|font-size|medium'}})
section('cabinet', 'Cabinet plan', ['core/group'],
        {'css': '&{display:grid!important;grid-template-columns:repeat(auto-fill,minmax(7.5rem,1fr));gap:0!important;outline:1px solid var(--wp--preset--color--line);outline-offset:-1px;border-top:1px solid var(--wp--preset--color--rule);border-left:1px solid var(--wp--preset--color--rule)}& > *{margin:0!important;border-right:1px solid var(--wp--preset--color--rule);border-bottom:1px solid var(--wp--preset--color--rule);padding:.75rem .8rem 1rem;min-height:7rem}'})
section('pan', 'Cabinet pan', ['core/group'],
        {'spacing': {'blockGap': 'var:preset|spacing|10'},
         'css': '& p{margin:0}& p:first-child{font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--muted)}& p:nth-child(2){font-family:var(--wp--preset--font-family--display);font-size:1.15rem;line-height:1.15}'})
section('pan-special', 'Cabinet pan, special', ['core/group'],
        {'color': {'background': 'var:preset|color|surface'}, 'spacing': {'blockGap': 'var:preset|spacing|10'},
         'css': '&{box-shadow:inset 0 3px 0 var(--wp--preset--color--accent)}& p{margin:0}& p:first-child{font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--accent)}& p:nth-child(2){font-family:var(--wp--preset--font-family--display);font-size:1.15rem;line-height:1.15}'})
section('notice', 'Notice line', ['core/group'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'typography': {'fontSize': 'var:preset|font-size|x-small'}})

write('style.css', '''/*
Theme Name: Scoop
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A clean, technical theme for a one- or two-shop gelateria that churns daily, publishes a monthly menu with the spec of every flavour, and sells tubs to take home.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: scoop
Tags: food-and-drink, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column
*/''')
write('functions.php', '''<?php
/**
 * Scoop: pattern category only.
 *
 * @package scoop
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'scoop', array( 'label' => __( 'Scoop: gelateria', 'scoop' ) ) );
	}
);''')

PX = {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}
write('parts/notice.html', group(
    para('Open until 10pm while it stays over 20 °C. Otherwise we close at 7pm.', align='center'),
    tag='section', align='full', className='is-style-notice', style={'spacing': {'padding': dict(top='var:preset|spacing|20', bottom='var:preset|spacing|20', **PX)}}))
write('parts/header.html', J(template_part('notice'),
    group(row(J(stack(J(dyn('site-title', level=0), dyn('site-tagline')), style={'spacing': {'blockGap': '0'}}),
                dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'})),
              justify='space-between', align='wide'),
          tag='section', align='full', className='is-style-hairline-bottom', style={'spacing': {'padding': dict(top='var:preset|spacing|40', bottom='var:preset|spacing|40', **PX)}})))
write('parts/footer.html', group(J(
    columns(
        ('40%', J(para('Latteria Nord', fontSize='x-large', fontFamily='display'),
                  para('Gelato churned every morning at 7 on Raeburn Place, Stockbridge. 24 pans, 8 of them changing each month.', fontSize='small', textColor='muted'))),
        (None, J(heading('Shop', 6), para('41 Raeburn Place<br>Edinburgh EH4 1HX<br>Tuesday to Sunday, 12 to 7pm<br>Closed Mondays', fontSize='small'))),
        (None, J(heading('Orders and events', 6), para('<a href="mailto:ciao@example.com">ciao@example.com</a><br>0131 496 0724<br><a href="/tubs/">Tubs to take home</a><br><a href="/allergens/">Allergen sheet</a>', fontSize='small'))),
        align='wide'),
    para('Demo photos are CC0 images from Wikimedia Commons, standing in for our own.', align='wide', className='alignwide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-hairline-top', style={'spacing': {'padding': dict(top='var:preset|spacing|60', bottom='var:preset|spacing|50', **PX), 'margin': {'top': 'var:preset|spacing|70'}}}))

MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero'), pattern_ref('monthly-menu'), pattern_ref('cabinet-map'), pattern_ref('method'), pattern_ref('tubs'), pattern_ref('vote-back'), pattern_ref('find-us'))))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), style=MAINPAD))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide', fontSize='xx-large'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})), style=MAINPAD))
write('templates/page-sheet.html', page_template(columns(
    ('30%', dyn('post-title', level=1, fontSize='xx-large')), (None, dyn('post-content', layout={'type': 'default'})), align='wide', className='is-style-hairline-top'), style=MAINPAD))
menu_item = J(dyn('post-date'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=24, fontSize='small'))
write('templates/home.html', page_template(J(
    heading('Past menus', 1, align='wide', fontSize='xx-large'),
    para('Every month\'s list since we opened, with notes on what worked. Ask for any of these back with the vote on the front page.', align='wide', className='alignwide', textColor='muted'),
    pattern_ref('menu-archive')), style=MAINPAD))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'), dyn('term-description', align='wide'), pattern_ref('menu-archive')), style=MAINPAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('menu-archive')), style=MAINPAD))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='pistachio, sorbet, August', buttonText='Search'), pattern_ref('menu-archive')), style=MAINPAD))
write('templates/404.html', page_template(J(
    heading('Melted', 1),
    para('This page is no longer in the cabinet. The <a href="/menu/">current menu</a> and <a href="/find-us/">opening hours</a> are where they always are.'),
    dyn('search', label='Search', showLabel=False, placeholder='pistachio, sorbet, August', buttonText='Search')), style=MAINPAD))
write('templates/single.html', page_template(J(
    columns(('30%', J(dyn('post-date'), dyn('post-terms', term='category'))),
            (None, J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image', aspectRatio='3/2', scale='cover'), dyn('post-content', layout={'type': 'default'}))),
            align='wide', className='is-style-hairline-top'),
    group(J(dyn('post-navigation-link', type='previous', label='Earlier', showTitle=True), dyn('post-navigation-link', label='Later', showTitle=True)),
          align='wide', className='is-style-hairline-top', layout={'type': 'flex', 'justifyContent': 'space-between'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}})), style=MAINPAD))

img = image
SEC = {'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|40'}}}

def spec_table(rows):
    return table(rows, head=['', ''])

pattern('hero', 'Hero: this month and the numbers', 'scoop,featured', group(J(
    columns(
        ('62%', J(heading('October, in 24 pans', 1),
                  para('Gelato made every morning in Stockbridge from Scottish whole milk, Sicilian pistachios and fruit bought that week. Sixteen classics stay all year. Eight specials change on the first Tuesday of the month.', fontSize='large'))),
        (None, table([['Churned', 'Daily, 7 to 11am'], ['Pans in the cabinet', '24'], ['Served at', '−12 °C'], ['Base', '3.8% fat whole milk'], ['Open', 'Tue to Sun, 12 to 7pm']],
                     className='is-style-default')),
        align='wide', verticalAlignment='bottom'),
    img('hero.jpg', 'Steel gelato pans in a shop cabinet, filled with strawberry, lemon, pistachio and stracciatella, with scoop spades standing in them', 'The cabinet at 11:40, just before we open', lightbox=False, align='wide')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}}}),
    description='Opener: the month as a headline, one paragraph, a small table of numbers and a wide photo of the cabinet.')

def flavour(name, note, spec, vegan=False):
    n = name + (' <sup>vg</sup>' if vegan else '')
    return group(J(heading(n, 4), para(note, className='is-note'), para(spec, className='is-spec')), className='is-style-flavour', layout={'type': 'default'})

SPECIALS = [
    ('Fig leaf and honey', 'milk infused with fig leaves from the Botanic Garden\'s neighbour', 'Milk base, 17% sugar, 7.5% fat. Allergens: milk', False),
    ('Roast pumpkin, brown butter', 'Crown Prince squash from East Lothian', 'Milk base, 18% sugar, 9% fat. Allergens: milk', False),
    ('Bramble sorbet', 'hand-picked in the Pentlands, a lot of seeds, sorry', 'Water base, 26% sugar, 0% fat. Allergens: none', True),
    ('Tablet', 'the Scottish sweet, crumbled in at the end', 'Milk base, 22% sugar, 10% fat. Allergens: milk', False),
    ('Pear and bay', 'Conference pears, poached, with one bay leaf per litre', 'Water base, 24% sugar, 0% fat. Allergens: none', True),
    ('Chestnut and rum', 'Italian chestnut paste, Scottish rum', 'Milk base, 19% sugar, 8% fat. Allergens: milk, sulphites', False),
    ('Black sesame', 'toasted and ground here, very grey', 'Milk base, 17% sugar, 11% fat. Allergens: milk, sesame', False),
    ('Apple and oat crumble', 'Discovery apples, oat crumble folded through', 'Milk base, 18% sugar, 8% fat. Allergens: milk, gluten (oats)', False),
]
CLASSICS = [
    ('Fior di latte', 'milk, sugar, nothing else', 'Milk base, 16% sugar, 8% fat. Allergens: milk', False),
    ('Pistachio', 'Bronte pistachios, 12% of the weight', 'Milk base, 17% sugar, 13% fat. Allergens: milk, nuts', False),
    ('Hazelnut', 'Piedmont IGP hazelnuts, roasted dark', 'Milk base, 17% sugar, 13% fat. Allergens: milk, nuts', False),
    ('Dark chocolate sorbet', '70% Ecuadorian chocolate and water', 'Water base, 22% sugar, 5% fat. Allergens: none', True),
    ('Stracciatella', 'fior di latte with chocolate drizzled in as it churns', 'Milk base, 17% sugar, 10% fat. Allergens: milk', False),
    ('Lemon sorbet', 'Amalfi lemons, zest and juice', 'Water base, 27% sugar, 0% fat. Allergens: none', True),
    ('Coffee', 'espresso from Machina, three shots a litre', 'Milk base, 17% sugar, 8% fat. Allergens: milk', False),
    ('Vanilla', 'Madagascar pods, split and scraped', 'Custard base, 18% sugar, 12% fat. Allergens: milk, egg', False),
]
pattern('monthly-menu', 'Monthly menu: specials and classics', 'scoop,menu', group(J(
    row(J(heading('The October menu', 2), para('<sup>vg</sup> vegan. Full allergen sheet on the <a href="/allergens/">allergens page</a>.', className='is-style-spec')), justify='space-between', align='wide'),
    columns(
        (None, J(heading('Specials, until 4 November', 5), *[flavour(*f) for f in SPECIALS])),
        (None, J(heading('Classics, all year', 5), *[flavour(*f) for f in CLASSICS[:8]])),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    buttons(('Order a tub of any of these', '/tubs/'), align='wide')),
    align='wide', layout={'type': 'default'}, style=SEC),
    description='The signature: this month\'s specials and the classics, each with a one-line note and a spec line, linked to tub orders.')

PANS = [('1', 'Fior di latte', 0), ('2', 'Stracciatella', 0), ('3', 'Pistachio', 0), ('4', 'Hazelnut', 0), ('5', 'Fig leaf and honey', 1), ('6', 'Tablet', 1),
        ('7', 'Coffee', 0), ('8', 'Vanilla', 0), ('9', 'Gianduja', 0), ('10', 'Salted caramel', 0), ('11', 'Roast pumpkin', 1), ('12', 'Black sesame', 1),
        ('13', 'Ricotta and fig', 0), ('14', 'Yoghurt', 0), ('15', 'Chestnut and rum', 1), ('16', 'Apple crumble', 1), ('17', 'Mint choc', 0), ('18', 'Malaga', 0),
        ('19', 'Lemon sorbet', 0), ('20', 'Chocolate sorbet', 0), ('21', 'Raspberry sorbet', 0), ('22', 'Mango sorbet', 0), ('23', 'Bramble sorbet', 1), ('24', 'Pear and bay', 1)]
pattern('cabinet-map', 'Cabinet map (24 pans)', 'scoop,menu', group(J(
    columns(('38%', J(heading('Where to look in the cabinet', 3),
                      para('Twenty-four pans in two rows of twelve. Milk bases on the left, sorbets on the right, specials marked with a red line. If a pan is empty, it sold out today and comes back tomorrow at noon.', fontSize='small'))),
            (None, group(J(*[group(J(para('Pan %s' % n + (', special' if s else '')), para(name)), className='is-style-pan-special' if s else 'is-style-pan', layout={'type': 'default'}) for n, name, s in PANS]),
                         className='is-style-cabinet', layout={'type': 'default'})), align='wide')),
    align='wide', layout={'type': 'default'}, style=SEC))

pattern('method', 'Method: how a batch is made', 'scoop,about', group(columns(
    ('38%', img('pistachios.jpg', 'A heap of shelled and unshelled pistachio nuts', 'Bronte pistachios, before we roast and grind them', lightbox=False)),
    (None, J(heading('How a batch is made', 3),
             table([['Pasteurise', '85 °C for 15 seconds, then cooled to 4 °C'], ['Age', '6 hours at 4 °C, overnight for nut bases'],
                    ['Churn', 'Batch freezer, 10 minutes, out at −8 °C'], ['Harden', '40 minutes at −25 °C'],
                    ['Serve', 'Cabinet at −12 °C, sorbets at −14 °C'], ['Keep', 'We throw away what is left after 3 days']], head=['Step', 'What we do']),
             para('We make every base from scratch. There are no pre-mixed bases or paste flavourings in the kitchen, except for the chestnut paste, which comes from a single producer in Cuneo.', fontSize='small'))),
    align='wide'), align='full', className='is-style-mist', layout={'type': 'constrained'}))

pattern('tubs', 'Tubs to take home', 'scoop,shop', group(columns(
    (None, J(heading('Tubs to take home', 3),
             para('Any flavour from the cabinet, packed to order in insulated tubs. Collect from the shop, or we deliver in Edinburgh on Friday and Saturday afternoons.'),
             table([['500 ml', '1 or 2 flavours', '£9.50'], ['1 litre', 'up to 3 flavours', '£17'], ['2.5 litre', 'for events, up to 3 flavours', '£38']], head=['Size', 'Flavours', 'Price']),
             para('Order by 5pm Thursday for Friday delivery, £4 inside the bypass. It keeps 3 weeks at −18 °C. Take it out of the freezer 10 minutes before serving.', className='is-style-spec'),
             buttons(('Order tubs by email', 'mailto:ciao@example.com?subject=Tub%20order')))),
    ('40%', img('tubs.jpg', 'A paper cup of chocolate and blackcurrant ripple gelato with three wooden spoons', lightbox=False)), align='wide'),
    align='wide', layout={'type': 'default'}, style=SEC))

pattern('vote-back', 'Vote a flavour back', 'scoop,call-to-action', group(J(
    heading('Vote a special back', 3),
    para('Reply to the newsletter, or tell whoever is serving, with the name of a past special. The one with most votes on the last day of the month goes back in the cabinet the month after.'),
    table([['Blood orange sorbet', 'February', '41 votes'], ['Olive oil and sea salt', 'June', '37 votes'], ['Rhubarb and custard', 'April', '29 votes']],
          head=['Leading this month', 'Last made', 'So far'])),
    layout={'type': 'constrained'}, style=SEC))

pattern('find-us', 'Find us', 'scoop,contact', group(columns(
    (None, J(heading('Find us', 3), para('41 Raeburn Place, Stockbridge, Edinburgh EH4 1HX. The 24 and 29 buses stop outside. One step at the door and a ramp we put down if you ask.'))),
    (None, table([['Tuesday to Friday', '12 to 7pm'], ['Saturday and Sunday', '11am to 7pm'], ['Monday', 'Closed, we clean the machines'], ['Over 20 °C', 'Open until 10pm']], head=['Day', 'Hours'])),
    align='wide'), align='wide', className='is-style-hairline-top', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))

pattern('allergen-sheet', 'Allergen sheet', 'scoop,menu', group(J(
    para('Every flavour, the 14 allergens we are required to declare, and which ones apply. Updated on the first Tuesday of each month. We use shared scoops rinsed between flavours, so traces of milk and nuts are possible in everything.', fontSize='small'),
    table([['Fior di latte', 'milk'], ['Pistachio', 'milk, nuts'], ['Hazelnut', 'milk, nuts'], ['Dark chocolate sorbet', 'none'], ['Stracciatella', 'milk'],
           ['Lemon sorbet', 'none'], ['Coffee', 'milk'], ['Vanilla', 'milk, egg'], ['Fig leaf and honey', 'milk'], ['Roast pumpkin, brown butter', 'milk'],
           ['Bramble sorbet', 'none'], ['Tablet', 'milk'], ['Pear and bay', 'none'], ['Chestnut and rum', 'milk, sulphites'], ['Black sesame', 'milk, sesame'],
           ['Apple and oat crumble', 'milk, gluten']], head=['Flavour', 'Contains']),
    para('Cones contain gluten, egg and soya. Ask for a cup if that matters.', className='is-style-spec')),
    layout={'type': 'constrained'}))

pattern('allergens-page', 'Page: allergens', 'scoop', J(pattern_ref('allergen-sheet')), block_types='core/post-content')

pattern('menu-page', 'Page: menu', 'scoop', J(pattern_ref('monthly-menu'), pattern_ref('tasting'), pattern_ref('affogato'), pattern_ref('cabinet-map'), pattern_ref('print-board')), block_types='core/post-content')

pattern('print-board', 'Printable flavour board', 'scoop,menu', group(J(
    heading('The window board', 4),
    para('We print the month\'s list on A4 for the window. To make yours, open the menu page, print, and choose "background graphics off". The layout drops the photos and keeps the two columns.', fontSize='small')),
    className='is-style-hairline-top', layout={'type': 'constrained'}))

pattern('events', 'Events and catering', 'scoop,services', group(columns(
    ('40%', img('cone.jpg', 'A hand holding a waffle cone with two scoops, one pale fig and one pistachio, and a white spoon', lightbox=False)),
    (None, J(heading('Events and catering', 3),
             para('We bring a four-pan cabinet on a trolley, one person to serve, cones, cups and spoons. It needs a normal plug and 2 metres of floor.'),
             table([['Up to 80 guests', '4 flavours, 2 hours', '£480'], ['80 to 150 guests', '4 flavours, 3 hours', '£720'], ['Tubs only, delivered', '2.5 litre tubs', '£38 each']],
                   head=['Size', 'What', 'Price']),
             para('Within 20 miles of Stockbridge. We book one event per weekend, so ask early for June.', fontSize='small'),
             buttons(('Ask about a date', 'mailto:ciao@example.com?subject=Event')))), align='wide'),
    align='wide', layout={'type': 'default'}))

pattern('events-page', 'Page: events', 'scoop', J(pattern_ref('events'), pattern_ref('wholesale'), pattern_ref('faq')), block_types='core/post-content')

pattern('faq', 'Questions', 'scoop,text', group(J(
    heading('Questions', 3),
    details('Why is the pistachio brown-green?', para('Because it is only pistachios. Bright green pistachio gelato has colouring in it.')),
    details('Do you do dairy-free?', para('Every sorbet is dairy-free and vegan, and there are always at least five. They share a freezer and scoops with milk flavours.')),
    details('Can I bring my dog?', para('Yes. There is a free dog cup of plain yoghurt gelato, one per dog, no sugar added.')),
    details('Do you take cards?', para('Cards and phones only, no cash, since 2022.'))),
    layout={'type': 'constrained'}))

pattern('story', 'Story of the maker', 'scoop,about', group(columns(
    ('30%', heading('Who makes it', 3)),
    (None, J(para('Chiara Benedetti trained at the Carpigiani Gelato University in Bologna and worked six summers at a gelateria in Parma before moving to Edinburgh in 2017. She opened Latteria Nord in 2020 with her partner Callum Reid, who does the books, the deliveries and, now, the tablet flavour.'),
             para('Chiara makes every batch herself between 7 and 11. Two people serve in the afternoons: Ines on weekdays and Oskar at weekends.'),
             para('One opinion she will give you unasked: gelato should be served soft enough to bend the spade. If it is piled up high like a mountain, it has stabilisers in it.'),
             para('We don\'t do milkshakes. The cabinet is the whole menu.', className='is-style-note'))), align='wide', className='is-style-hairline-top'),
    align='wide', layout={'type': 'default'}))

pattern('suppliers', 'Where the ingredients come from', 'scoop,about', group(J(
    heading('Where it comes from', 4),
    table([['Whole milk and cream', 'Mansfield\'s dairy, East Lothian', '18 miles'], ['Pistachios', 'Bronte, Sicily, via Valvona and Crolla', 'by road'],
           ['Hazelnuts', 'Piedmont IGP, same importer', 'by road'], ['Chocolate', 'Ecuador, 70%, from a Glasgow wholesaler', ''],
           ['Fruit', 'Whatever is good at the Saturday farmers\' market on Castle Terrace', '2 miles']], head=['What', 'Who', 'Distance'])),
    layout={'type': 'constrained'}))

pattern('about-page', 'Page: story', 'scoop', J(pattern_ref('story'), pattern_ref('method'), pattern_ref('suppliers')), block_types='core/post-content')

pattern('tubs-page', 'Page: tubs', 'scoop', J(pattern_ref('tubs'), pattern_ref('gift-voucher')), block_types='core/post-content')

pattern('gift-voucher', 'Gift vouchers', 'scoop,shop', group(J(
    heading('Gift vouchers', 4),
    para('£10, £20 or £40, printed on card and posted, or emailed as a PDF. Valid for a year in the shop or on tubs. Email us with the amount and where to send it.'),
    buttons(('Order a voucher by email', 'mailto:ciao@example.com?subject=Voucher'))),
    className='is-style-mist', layout={'type': 'constrained'}, style={'spacing': {'padding': {'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}}))

pattern('find-us-page', 'Page: find us', 'scoop', J(pattern_ref('find-us'), pattern_ref('newsletter')), block_types='core/post-content')

pattern('newsletter', 'Newsletter', 'scoop,call-to-action', group(J(
    heading('The first Tuesday email', 4),
    para('One email a month, the morning the specials change, with the list and the vote. Sign up by sending a blank email to <a href="mailto:list@example.com?subject=Subscribe">list@example.com</a>.')),
    className='is-style-hairline-top', layout={'type': 'constrained'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))

pattern('ingredient-strip', 'Ingredient photos', 'scoop,gallery', gallery([
    ('hazelnuts.jpg', 'Green hazelnuts still in their husks on a branch', 'Hazelnuts, before Piedmont gets to them'),
    ('lemons.jpg', 'A green lemon hanging from a lemon tree among dark leaves', 'Lemons, a month too early'),
    ('chocolate.jpg', 'Two squares of dark chocolate on a white surface', '70% Ecuador'),
    ('vanilla.jpg', 'Dried vanilla pods tied in a bundle', 'Madagascar vanilla')], columns=4, align='wide'))

pattern('affogato', 'Affogato', 'scoop,menu', group(columns(
    (None, J(heading('Affogato', 4), para('A scoop of fior di latte or hazelnut with a double espresso poured over at the counter. £4.80. Coffee from Machina on Nicolson Street.'),
             para('Served from 12 until 5pm, when the coffee machine goes off.', className='is-style-spec'))),
    ('34%', img('affogato.jpg', 'Espresso being poured from a small jug over a scoop of gelato in a copper cup', lightbox=False, aspectRatio='4/3', scale='cover')), align='wide', verticalAlignment='center', className='is-style-hairline-top'),
    align='wide', layout={'type': 'default'}))


pattern('notice-heat', 'Notice: warm-weather hours', 'scoop,banner', group(
    para('Open until 10pm today. The forecast says 23 °C. Take this line out when it drops below 20.', align='center'),
    tag='section', align='full', className='is-style-notice', style={'spacing': {'padding': dict(top='var:preset|spacing|20', bottom='var:preset|spacing|20', **PX)}}),
    description='The weather-aware hours note. Swap it into the Weather and hours note template part on warm days.')

pattern('tasting', 'Three small scoops', 'scoop,menu', group(columns(
    ('30%', heading('Assaggio', 4)),
    (None, J(para('Three small scoops in a cup, any flavours, £5.20. The best way to try the specials without committing. We will also give you a taste on a spoon first, as many as you like within reason.'),
             para('Small cup £3.80, one flavour. Medium £4.90, two. Large £5.90, three.', className='is-style-spec'))), align='wide', className='is-style-hairline-top'),
    align='wide', layout={'type': 'default'}))

pattern('wholesale', 'Gelato for restaurants', 'scoop,services', group(columns(
    ('30%', heading('For restaurants', 4)),
    (None, J(para('We make 5-litre pans for eleven restaurants in Edinburgh, delivered on Tuesday and Friday mornings. Fior di latte, pistachio, one sorbet and a flavour made for your menu.'),
             table([['5 litre pan, classic', '£48'], ['5 litre pan, made for you', '£56, minimum 3 pans a month']], head=['What', 'Price']),
             para('We are full until January. Email to go on the list.', className='is-style-spec'))), align='wide', className='is-style-hairline-top'),
    align='wide', layout={'type': 'default'}))

print('scoop: build done')
