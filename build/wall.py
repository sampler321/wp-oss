# Design note (wall, idea 009, muralist / street artist). Owner's brief: "more edgy, cargo.site-like, inspired by
# All Caps festival Rotterdam".
# Direction: a raw, web-native portfolio (Cargo) with festival-poster lettering (All Caps). White page, black
# type, default-web blue links, acid-yellow tape labels. No boxes, no borders, no rounded anything.
# Fonts: Special Gothic Condensed One (display, claimed in demos/wall/fonts-claim.txt), set uppercase and enormous,
# lines touching; Hanken Grotesk for everything else, small and plain like a Cargo text block.
# Palette: #FFFFFF, #0B0B0B, link blue #0019FF, tape yellow #E5FF1A (fills only, black text on it).
# Layout idea: the artist's name painted across the full width like a wall piece, then a freeform wall of photos on a
# 6-column grid where every card has its own span and offset (Cargo freeform), and walls that are gone turn grey
# with a "Painted over" label and get their own archive page instead of disappearing.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('wall')
S = THEME['slug']

CATS = {'wall-hero': 'Walls: openers', 'wall-murals': 'Walls: murals and archive', 'wall-commissions': 'Walls: commissions and prices',
        'wall-process': 'Walls: process', 'wall-shop': 'Walls: prints', 'wall-about': 'Walls: about and press',
        'wall-contact': 'Walls: contact and notices', 'wall-pages': 'Walls: page layouts'}
CATMAP = {'featured': 'wall-hero', 'portfolio': 'wall-murals', 'posts': 'wall-murals', 'call-to-action': 'wall-commissions', 'services': 'wall-commissions',
          'banner': 'wall-contact', 'contact': 'wall-contact', 'shop': 'wall-shop', 'about': 'wall-about', 'testimonials': 'wall-about',
          'process-strip': 'wall-process', 'gallery': 'wall-process'}
_pattern = pattern
def pattern(slug, title, cats, body, **kw):
    first = cats.split(',')[0]
    c = 'wall-pages' if kw.get('block_types') == 'core/post-content' else CATMAP.get(slug) or CATMAP.get(first, 'wall-murals')
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
for f in FONTS:
    if f['slug'] == 'display':
        f['name'] = 'Special Gothic Condensed One'

PALETTE = [
    ('base', '#FFFFFF', 'Primer white'), ('contrast', '#0B0B0B', 'Black'), ('accent', '#0019FF', 'Link blue'),
    ('accent-2', '#E5FF1A', 'Tape yellow'), ('surface', '#EFEFEC', 'Concrete'), ('line', '#0B0B0B', 'Black line'),
    ('muted', '#545454', 'Grey'),
]
focus = {'outline': {'color': 'var:preset|color|accent', 'offset': '2px', 'style': 'solid', 'width': '3px'}}

CSS = (
    ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
    '.wp-block-table{font-variant-numeric:tabular-nums}'
    '.wp-block-table table.has-fixed-layout{table-layout:auto}'
    '.wp-block-table table td,.wp-block-table table th{border:0;border-top:1px solid var(--wp--preset--color--contrast);padding:.45em 1.2em .45em 0;text-align:left;vertical-align:top;word-break:normal}'
    '.wp-block-table table thead{border:0}.wp-block-table table th{font-weight:700}'
    # freeform wall of murals: six columns, each card with its own span and drop
    '@media (min-width:782px){'
    '.wp-block-post-template.is-style-freeform{display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));grid-auto-flow:dense;column-gap:var(--wp--preset--spacing--40);row-gap:var(--wp--preset--spacing--60);align-items:start}'
    '.is-style-freeform>li:nth-child(6n+1){grid-column:1/span 7}'
    '.is-style-freeform>li:nth-child(6n+2){grid-column:9/span 4;margin-top:var(--wp--preset--spacing--70)}'
    '.is-style-freeform>li:nth-child(6n+3){grid-column:2/span 4}'
    '.is-style-freeform>li:nth-child(6n+4){grid-column:7/span 6;margin-top:var(--wp--preset--spacing--50)}'
    '.is-style-freeform>li:nth-child(6n+5){grid-column:1/span 5}'
    '.is-style-freeform>li:nth-child(6n){grid-column:7/span 4;margin-top:var(--wp--preset--spacing--70)}'
    '}'
    '.wp-block-table table.has-fixed-layout td,.wp-block-table table.has-fixed-layout th{word-break:normal;overflow-wrap:normal}'
    '.wp-block-post.tag-gone .wp-block-post-featured-image img{filter:grayscale(1);opacity:.75}'
    '.wp-block-post.tag-gone .wp-block-post-featured-image{position:relative}'
    '.wp-block-post.tag-gone .wp-block-post-featured-image::after{content:"Painted over";position:absolute;left:0;top:0;background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--contrast);font:700 var(--wp--preset--font-size--small)/1.2 var(--wp--preset--font-family--body);padding:.3em .5em}'
    '.wp-block-site-title{text-transform:uppercase}'
    '.wp-block-navigation .current-menu-item>a{background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--contrast)}'
    '@media (prefers-reduced-motion:no-preference){.wp-block-post-featured-image img{transition:filter .12s}}'
    '.wp-block-post-featured-image a:hover img{filter:contrast(1.15) saturate(1.2)}'
)

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1600px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': FONTS,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Small print', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Caption', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.625rem', 'name': 'Large', 'fluid': {'min': '1.3rem', 'max': '1.625rem'}},
                {'slug': 'x-large', 'size': '3rem', 'name': 'City', 'fluid': {'min': '2rem', 'max': '3rem'}},
                {'slug': 'xx-large', 'size': '7rem', 'name': 'Poster', 'fluid': {'min': '3.5rem', 'max': '7rem'}},
                {'slug': 'display', 'size': '17rem', 'name': 'Wall', 'fluid': {'min': '5.5rem', 'max': '17rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1rem, 1.6vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 8vw, 7rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 12vw, 11rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.5'},
        'spacing': {'padding': {'left': sp(40), 'right': sp(40)}, 'blockGap': sp(30)},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast', 'background': 'var:preset|color|accent-2'}, 'typography': {'textDecoration': 'none'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '0.86', 'letterSpacing': '-0.005em', 'textTransform': 'uppercase'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '0.95'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'textTransform': 'none', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'textTransform': 'none', 'lineHeight': '1.3'}},
            'button': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
                       'border': {'radius': '0', 'width': '0', 'style': 'none'},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|medium'},
                       'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '0.9em', 'right': '0.9em'}},
                       ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|accent-2'}},
                       ':focus': focus},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|contrast'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|medium'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '400'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'}}}},
            'core/post-title': {'typography': {'textTransform': 'uppercase'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '0.95', 'textTransform': 'uppercase'},
                           'border': {'width': '0', 'style': 'none'}, 'spacing': {'padding': {'left': '0'}},
                           'css': '& cite{display:block;margin-top:.8em;font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--small);font-style:normal;text-transform:none}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': sp(20), 'bottom': sp(20)}},
                             'css': '& summary{font-weight:700}'},
            'core/search': {'css': '& .wp-block-search__input{border:0;border-bottom:2px solid var(--wp--preset--color--contrast);border-radius:0}'},
            'core/list': {'css': '&{padding-left:1.1em}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|large'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'single-mural', 'title': 'Mural (full-bleed photo, facts)', 'postTypes': ['post']},
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    ],
}
wjson('theme.json', theme)


def variation(title, pal):
    return {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
            'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}

wjson('styles/night-wall.json', variation('Night wall', [
    ('base', '#111111', 'Night'), ('contrast', '#F5F5F0', 'Chalk'), ('accent', '#F2B705', 'Tape yellow'),
    ('accent-2', '#F2B705', 'Tape yellow'), ('surface', '#1E1E1E', 'Tarmac'), ('line', '#F5F5F0', 'Chalk line'), ('muted', '#B5B5B0', 'Grey')]))
wjson('styles/chalk.json', variation('Chalk', [
    ('base', '#E9ECEF', 'Chalk'), ('contrast', '#1B1F23', 'Charcoal'), ('accent', '#C4001A', 'Red oxide'),
    ('accent-2', '#FFFFFF', 'White tape'), ('surface', '#DDE1E5', 'Render'), ('line', '#1B1F23', 'Charcoal line'), ('muted', '#495057', 'Slate')]))
wjson('styles/pink-primer.json', variation('Pink primer', [
    ('base', '#F4C7C3', 'Pink primer'), ('contrast', '#1D1D1B', 'Black'), ('accent', '#1D1D1B', 'Black'),
    ('accent-2', '#FFFFFF', 'White tape'), ('surface', '#EDB5B0', 'Second coat'), ('line', '#1D1D1B', 'Black line'), ('muted', '#4A3634', 'Burnt')]))


def section(slug, title, blocks, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                             'title': title, 'slug': slug, 'blockTypes': blocks, 'styles': styles})

section('freeform', 'Freeform wall (varied spans)', ['core/post-template', 'core/group'], {})
section('gone', 'Painted over (grey photo)', ['core/image'], {'css': '& img{filter:grayscale(1);opacity:.75}'})
section('tape', 'Tape label', ['core/paragraph', 'core/heading', 'core/group'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}},
    'spacing': {'padding': {'top': '0.15em', 'bottom': '0.15em', 'left': '0.35em', 'right': '0.35em'}},
    'css': '&{display:inline-block;width:auto}'})
section('blackout', 'Blackout', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|accent-2'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                 'button': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'}}},
    'spacing': {'padding': {'top': sp(70), 'bottom': sp(70)}}})
section('concrete', 'Concrete', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': sp(60), 'bottom': sp(60), 'left': sp(40), 'right': sp(40)}}})
section('big-links', 'Big text links', ['core/paragraph', 'core/list'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large', 'lineHeight': '0.9', 'textTransform': 'uppercase'},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'},
                          ':hover': {'color': {'background': 'var:preset|color|accent-2'}}}},
    'css': '&{list-style:none;padding-left:0}'})
section('wordmark', 'Wall wordmark', ['core/heading', 'core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|display', 'lineHeight': '0.8', 'letterSpacing': '-0.01em', 'textTransform': 'uppercase'},
    'spacing': {'margin': {'top': '0', 'bottom': '0'}}, 'css': '&{overflow-wrap:anywhere}'})
section('rule-top', 'Black rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': sp(30)}}})

write('style.css', '''/*
Theme Name: Wall
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A loud, plain portfolio for muralists and sign painters, with every wall listed, lost walls kept in their own archive, and quotes for homes, businesses and schools.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: wall
Tags: portfolio, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

# ------------------------------------------------------------------ parts
write('parts/header.html', group(row(J(
    dyn('site-title', level=0),
    dyn('navigation', layout={'type': 'flex', 'justifyContent': 'left', 'flexWrap': 'wrap'}, style={'spacing': {'blockGap': sp(30)}}),
    para('Booking outdoor walls for April 2027', className='is-style-tape', fontSize='small')),
    justify='space-between', align='full', style={'spacing': {'blockGap': sp(40)}}), align='full', style=pad(30, 30, 40, 40), layout={'type': 'default'}))

write('parts/footer.html', group(J(
    heading('Got a wall?', 2, className='is-style-wordmark', align='full'),
    columns(
        (None, para('Nora Bakri<br>Keilestraat 9, studio 2.14<br>3029 BP Rotterdam')),
        (None, para('<a href="mailto:walls@example.com">walls@example.com</a><br>+31 6 1234 5678, weekdays 9 to 5<br><a href="https://www.instagram.com/">Instagram</a>')),
        (None, para('Outdoor walls April to October. Indoor walls, shutters and schools all year.')),
        align='full', style={'spacing': {'blockGap': {'left': sp(40)}}}),
    para('Demo photos are CC0 and public domain pictures of other people\'s murals from Wikimedia Commons, standing in for Nora\'s walls.', fontSize='x-small', align='full')),
    tag='footer', align='full', className='is-style-blackout', style=pad(60, 40, 40, 40), layout={'type': 'default'}))

# ------------------------------------------------------------------ murals
MURALS = [
    dict(t='Viaduct pillar, Hofplein line', city='Rotterdam', year='2026', img='viaduct.jpg', cat='public', tags=['Rotterdam'],
         where='Pillar 14, Hofbogen, Rotterdam-Noord', who='Gemeente Rotterdam, Kunst in de openbare ruimte', fest='Caps Lock weekend', size='4 × 9 m', status='Completed, still there',
         note='Four faces looking up at the trains, painted from a cherry picker over nine days in May. The black-and-white keeps it readable under the viaduct shadow.',
         alt='A concrete viaduct pillar painted with four black-and-white faces, bike path and benches in front'),
    dict(t='Corner block, Witte de With', city='Rotterdam', year='2025', img='corner-block.jpg', cat='businesses', tags=['Rotterdam'],
         where='Corner of Witte de Withstraat and Schiedamse Vest', who='Pantheon Records', fest='', size='11 × 22 m, two facades', status='Completed, still there',
         note='The whole corner in balloons and one big face. Twenty-three colours, all exterior silicate paint. The record shop is on the ground floor.',
         alt='A corner apartment block covered in colourful balloons and a large face, a shop on the ground floor'),
    dict(t='Gable with objects', city='Zaragoza', year='2025', img='gable-objects.jpg', cat='public', tags=['Festival'],
         where='Calle Delicias 41, Zaragoza', who='Barrio Delicias festival', fest='Delicias walls 2025', size='12 × 15 m', status='Completed, still there',
         note='Things people in the street lent me for a morning: a guitar, a key, a ball of wool, their neighbour\'s rabbit. Painted in eleven days in 34 degrees.',
         alt='A tall gable wall painted with a moon, a guitar, a red carnation, a hare, a butterfly and other objects'),
    dict(t='Faces, Colegio Maravillas', city='Málaga', year='2024', img='school-faces.jpg', cat='schools', tags=['School'],
         where='Courtyard, Colegio Maravillas, Málaga', who='The school parents\' association', fest='', size='3 × 14 m', status='Completed, still there',
         note='Five laughing faces made from 4,000 mosaic dots. Year 5 painted the dots, I did the drawing and the edges.',
         alt='A long low courtyard wall with five laughing faces made of small coloured dots'),
    dict(t='Letters, Maashaven hall of fame', city='Rotterdam', year='2024', img='letters.jpg', cat='public', tags=['Rotterdam', 'Lettering', 'Gone'],
         where='Legal wall, Maashaven Zuidzijde', who='Self-initiated', fest='Caps Lock weekend', size='3 × 8 m', status='Gone. Painted over by Kees and Rafi in March 2025, as it should be',
         note='A piece for the legal wall. Legal walls turn over every few months, which is the point.',
         alt='Graffiti lettering in purple, red and yellow with clouds, on a long wall'),
    dict(t='Tunnel, IJ-oever', city='Amsterdam', year='2023', img='tunnel.jpg', cat='public', tags=['Lettering', 'Gone'],
         where='Pedestrian tunnel under the IJ-oever, Amsterdam', who='Stadsdeel Centrum', fest='', size='3 × 40 m', status='Gone. Tunnel repainted grey in 2025',
         note='One continuous brown line for forty metres, with a question mark at the end. People wrote answers on it within a week.',
         alt='A tunnel wall with long looping brown brush lines and the word he with a question mark'),
    dict(t='Garden wall, Afrikaanderwijk', city='Rotterdam', year='2023', img='garden-wall.jpg', cat='homes', tags=['Rotterdam'],
         where='Back garden, Afrikaanderwijk (private address)', who='Private client', fest='', size='3 × 12 m', status='Completed, still there',
         note='Two grandparents, from a photo from 1971. Painted in sepia so it sits quietly next to the vegetable beds.',
         alt='A long white garden wall with a sepia painting of an older couple, vegetable planters in front'),
    dict(t='Window, Nieuwe Binnenweg', city='Rotterdam', year='2022', img='window.jpg', cat='businesses', tags=['Rotterdam', 'Trompe l\'oeil'],
         where='Nieuwe Binnenweg 212, above the bakery', who='Bakkerij Van Olst', fest='', size='2.5 × 4 m', status='Completed, still there',
         note='A painted window where a real one was bricked up in 1962. The table and the loaf are for the bakery downstairs.',
         alt='A painted window on a brick facade with a curtain, a table and a painted plaque below'),
    dict(t='Squat wall, Zuidplein', city='Rotterdam', year='2021', img='ruin.jpg', cat='public', tags=['Rotterdam', 'Gone'],
         where='Former garage, Zuidplein', who='Self-initiated', fest='', size='3 × 6 m', status='Gone. Building demolished in 2023',
         note='Painted in one afternoon with leftover paint. The building came down for 80 flats.',
         alt='A half-ruined wall with faded teal graffiti faces behind dry branches'),
]

def facts(m):
    rows = [['Where', m['where']], ['Commissioned by', m['who']]]
    if m['fest']:
        rows.append(['Festival', m['fest']])
    rows += [['Year', m['year']], ['Wall', m['size']], ['Status', m['status']]]
    return fact_rows(rows)

def fact_rows(rows):
    return group(J(*[row(J(para(k, fontSize='small', style={'typography': {'fontWeight': '700'}}), para(v)),
                         justify='space-between', className='is-style-rule-top', style={'spacing': {'blockGap': sp(30), 'padding': {'top': sp(20)}}})
                     for k, v in rows]), layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'stretch'}, style={'spacing': {'blockGap': sp(20)}})

def mural_content(m):
    return J(para(m['note'], fontSize='large'), facts(m))

card = J(dyn('post-featured-image', isLink=True),
         row(J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-date', format='Y', fontSize='large', fontFamily='display')),
             justify='space-between', wrap=False, style={'spacing': {'blockGap': sp(30), 'margin': {'top': sp(20)}}}))

# ------------------------------------------------------------------ patterns
pattern('wordmark-hero', 'Wordmark across the wall', 'featured', group(J(
    heading('Nora Bakri paints walls', 1, className='is-style-wordmark'),
    columns((None, para('Murals and lettering for streets, schools, shops and back gardens. Based in Rotterdam-Zuid, painting anywhere with a train station and a cherry picker hire nearby.', fontSize='large')),
            (None, para('<a href="/commissions/">Get a quote for your wall</a><br><a href="/map/">Every wall on a map</a>', fontSize='large')),
            (None, ''), style={'spacing': {'blockGap': {'left': sp(40)}}})),
    align='full', layout={'type': 'default'}, style=pad(40, 60)),
    description='Signature opener: the name set across the full width like a wall piece.')

pattern('mural-wall', 'Freeform wall of murals (front page)', 'portfolio,query', group(
    query(card, per_page=6, template_class='is-style-freeform', layout={'type': 'grid', 'columnCount': 2}),
    align='full', layout={'type': 'default'}),
    description='Every mural, newest first, each photo with its own size and drop. Walls tagged Gone turn grey with a label.')

pattern('mural-archive', 'Mural archive (inherits the page query)', 'portfolio,query', inherit_query(
    card, template_class='is-style-freeform', layout={'type': 'grid', 'columnCount': 2}, align='full'), inserter=False)

pattern('post-list', 'Plain list', 'posts,query', inherit_query(
    row(J(dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-date', format='Y')), justify='space-between', className='is-style-rule-top'),
    align='full'), inserter=False)

pattern('mural-card', 'Mural card (photo, title, city and year)', 'portfolio', J(
    image('viaduct.jpg', MURALS[0]['alt'], href='/murals/'),
    row(J(heading(MURALS[0]['t'], 3, fontSize='large'), para('Rotterdam 2026', fontSize='large', fontFamily='display')), justify='space-between', wrap=False)))

pattern('mural-facts', 'Mural facts (location, commissioner, festival, size, status)', 'portfolio', facts(MURALS[0]),
        description='Put this in every mural post. Change the status line when a wall is painted over.')

LIVE = [m for m in MURALS if 'Gone' not in m['tags']]
GONE = [m for m in MURALS if 'Gone' in m['tags']]
osm = lambda q: 'https://www.openstreetmap.org/search?query=' + q.replace(' ', '%20').replace(',', '%2C').replace('\'', '%27')

pattern('map-list', 'Every wall with an address (map list)', 'portfolio', J(
    heading('Still there', 2),
    group(J(*[row(J(heading(m['t'], 3, fontSize='large'), para('%s, %s. <a href="%s">Open on the map</a>' % (m['where'], m['year'], osm(m['where'])))),
                  justify='space-between', className='is-style-rule-top', style={'spacing': {'padding': {'top': sp(20)}}}) for m in LIVE if m['cat'] != 'homes']),
          layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'stretch'}, style={'spacing': {'blockGap': sp(30)}}),
    para('Private walls, like back gardens, are left off the map on purpose.', fontSize='small')),
    description='The list half of the map page. Each row links to OpenStreetMap.')

pattern('archived-walls', 'Archived: walls that are gone (signature)', 'portfolio', group(J(
    heading('Gone', 2),
    para('Walls get painted over, knocked down and repainted grey. They stay on this list with the date and what happened.', fontSize='large'),
    group(J(*[group(J(image(m['img'], m['alt'] + ', now gone', lightbox=True, className='is-style-gone'), heading('%s, %s' % (m['t'], m['year']), 3, fontSize='large'),
                      para(m['status'].replace('Gone. ', ''))), layout={'type': 'flex', 'orientation': 'vertical'}) for m in GONE]),
          layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'}, style={'spacing': {'blockGap': sp(40)}}),
    para('<a href="/tag/gone/">Photos of every wall that is gone</a>')),
    className='is-style-concrete', align='full'),
    description='Signature: lost walls move to their own list instead of disappearing.')

pattern('type-entry-points', 'Homes, businesses, schools, public', 'call-to-action', group(J(
    para('Who is the wall for?', fontSize='large'),
    lst(['<a href="/category/homes/">Homes</a>', '<a href="/category/businesses/">Businesses</a>', '<a href="/category/schools/">Schools</a>', '<a href="/category/public/">Public walls</a>'],
        className='is-style-big-links'),
    para('Each one is quoted differently. Schools include a day of painting with the pupils. <a href="/commissions/">Free quote within a week</a>.')),
    align='full', layout={'type': 'default'}, style=pad(60, 60)))

pattern('free-quote', 'Free quote line', 'call-to-action', para(
    'Quotes are free. Send a photo of the wall, rough measurements and the postcode, and I reply within a week.', className='is-style-tape', fontSize='large'))

pattern('commission-enquiry', 'Commission enquiry: what to send', 'call-to-action', columns(
    (None, J(heading('Ask for a quote', 2),
             para('No form. Email me these five things and a photo, and you get a price and a date within a week.', fontSize='large'),
             buttons(('Email walls@example.com', 'mailto:walls@example.com?subject=Wall%20quote')))),
    (None, lst(['Wall size, height and width, roughly is fine.',
                'Surface: brick, render, concrete, metal shutter, wood.',
                'Indoor or outdoor.',
                'Address or postcode, and whether there is space for a cherry picker.',
                'When it needs to be finished, and why (an opening, a festival, a birthday).'], ordered=True, fontSize='large')),
    align='full', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('wall-size-guide', 'Wall size guide and prices', 'services', J(
    heading('Size and price', 3),
    table([['Up to 10 m²', 'Shutter, garden wall, one door', 'from €1,200', '2 to 3 days'],
           ['10 to 40 m²', 'Shop front, playground wall', 'from €3,500', '4 to 8 days'],
           ['40 to 150 m²', 'Gable end, school hall', 'from €9,000', '8 to 15 days'],
           ['Over 150 m²', 'Whole facade', 'quoted', '3 weeks and up']], head=['Wall', 'Usually', 'Price', 'On the wall']),
    para('Prices include paint, anti-graffiti coat and my travel inside the Randstad. Scaffold or cherry picker hire is on top, usually €180 a day.', fontSize='small')))

pattern('client-provides', 'What the client provides', 'services', J(
    heading('What you sort out', 3),
    lst(['Permission from the building owner, and from the gemeente if the wall faces the street.',
         'Access: a place to park the van, and power within 25 metres.',
         'A dry wall. Fresh render needs four weeks before paint.',
         'If the wall is peeling, I prime it, but the cleaning is quoted separately.'])))

pattern('lead-time', 'Lead-time note (seasons)', 'banner', group(
    para('Outdoor walls are painted April to October. Indoor walls, shutters and school halls all year. Right now I\'m booking outdoor walls for April 2027.', fontSize='large'),
    className='is-style-tape'), description='Change the month when the calendar fills up.')

pattern('process-strip', 'Process: prep, sketch, paint, done', 'portfolio,gallery', J(
    heading('How a wall goes', 2),
    columns(
        (None, J(image('ladder.jpg', 'Black-and-white photo of a painter on a stepladder painting a large abstract wall'), para('<strong>1. Prep and grid.</strong> Clean, prime, chalk a grid. One day.'))),
        (None, J(image('school-archive.jpg', 'Black-and-white photo of a teacher and children on scaffolding painting a mural outline'), para('<strong>2. Sketch on the wall.</strong> Outlines in thinned paint, everyone welcome to argue.'))),
        (None, J(image('gable-objects.jpg', 'A tall gable wall painted with a moon, a guitar, a red carnation, a hare and other objects'), para('<strong>3. Paint and finish.</strong> Rollers for the big areas, brushes for the edges, then the anti-graffiti coat.'))),
        align='full', style={'spacing': {'blockGap': {'left': sp(40)}}})))

pattern('festival-list', 'Festivals', 'about', J(
    heading('Festivals', 3),
    lst(['2026, Caps Lock weekend, Rotterdam', '2025, Delicias walls, Zaragoza', '2024, Caps Lock weekend, Rotterdam', '2023, Kunstroute Afrikaanderwijk, Rotterdam'])))

pattern('walking-route', 'Walking route PDF', 'portfolio', group(J(
    heading('Walk it', 3),
    para('Seven walls in Rotterdam-Noord and the centre, 4.2 km, about 90 minutes with a coffee stop. Starts at Rotterdam Centraal, ends at the Hofbogen.'),
    buttons(('Ask for the route PDF by email', 'mailto:walls@example.com?subject=Walking%20route'))),
    className='is-style-rule-top'), description='Link a printable PDF route here once it is in the media library.')

pattern('prints-row', 'Prints (order by email)', 'shop', J(
    heading('Prints', 2),
    columns(
        (None, J(image('letters.jpg', 'Graffiti lettering in purple, red and yellow with clouds, on a long wall'), para('<strong>Maashaven letters</strong><br>Screenprint, 3 colours, 50 × 70 cm, edition of 40. €85'))),
        (None, J(image('viaduct.jpg', 'A concrete viaduct pillar painted with four black-and-white faces'), para('<strong>Hofbogen faces</strong><br>Risograph, black on grey, A2, edition of 100. €40'))),
        (None, J(image('corner-block.jpg', 'A corner apartment block covered in colourful balloons and a large face'), para('<strong>Balloon corner</strong><br>Giclée on cotton rag, 40 × 50 cm, open edition. €60'))),
        align='full', style={'spacing': {'blockGap': {'left': sp(40)}}}),
    para('No shop cart. Email which print and your address, I send a Tikkie or a PayPal link. Posted in a tube within four working days, €7 in the Netherlands, €14 in Europe.', fontSize='large')))

pattern('press-list', 'Press', 'about', J(
    heading('Press', 3),
    lst(['"Wie schildert die gezichten onder de Hofbogen?", Zuid Krant, June 2026',
         'Radio Maasstad, morning show, interview about the Hofbogen pillar, May 2026',
         '"Letters on the Maas", Muurwerk blog, 2024'])))

pattern('quote-neighbour', 'Quote from a neighbour', 'testimonials', quote(
    'My kids watched it go up from the balcony every day. Now they tell people it is their pillar.',
    'Samira, lives on the Hofplein, May 2026'))

pattern('about-bio', 'About', 'about', columns(
    ('33%', image('ladder.jpg', 'Black-and-white photo of a painter on a stepladder painting a large abstract wall')),
    (None, J(
        para('Nora Bakri (b. 1990, Rotterdam) paints murals and letters. She grew up on the Afrikaanderplein, studied graphic design at the Willem de Kooning Academie and started painting walls when a friend\'s snack bar needed a sign.', fontSize='large'),
        para('Most of her walls are in Rotterdam. Some are in schools, a few are in back gardens, and one is in Zaragoza because a festival there asked twice. She works with exterior silicate paint and a hired cherry picker, and she paints letters freehand.'),
        para('She doesn\'t paint company logos as murals. A sign, yes. A logo the size of a building, no.'),
        pattern_ref('festival-list'), pattern_ref('press-list'))),
    align='full', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('contact-block', 'Contact', 'contact', group(J(
    heading('walls@example.com', 2, fontSize='x-large'),
    columns((None, para('Phone or WhatsApp +31 6 1234 5678, weekdays 9 to 5. On a wall, I answer after 6.', fontSize='large')),
            (None, para('Studio 2.14, Keilestraat 9, 3029 BP Rotterdam. Visits by appointment. The 38 bus stops at Keileweg.', fontSize='large')),
            style={'spacing': {'blockGap': {'left': sp(60)}}})),
    align='full', layout={'type': 'default'}))

pattern('notice-festival', 'Notice: painting live at a festival', 'banner', group(
    para('Painting live at Caps Lock weekend, Hofbogen, 12 to 14 June. Come say hi, bring a hat. Take this notice down on 15 June.'),
    className='is-style-tape', align='full'), description='A tape-yellow notice for live painting dates.')

# page layouts
pattern('commissions-page', 'Page: commissions', 'services', J(
    pattern_ref('lead-time'), pattern_ref('commission-enquiry'), spacer(), pattern_ref('availability'), pattern_ref('wall-size-guide'), pattern_ref('client-provides'), pattern_ref('process-strip'),
    pattern_ref('wall-palette'), pattern_ref('quote-neighbour'), pattern_ref('faq')),
    block_types='core/post-content')
pattern('map-page', 'Page: map and list', 'portfolio', J(
    para('Every public wall I have painted, with an address and a link to the map. The ones that are gone are listed below, with what happened to them.', fontSize='large'),
    pattern_ref('map-list'), pattern_ref('archived-walls'), pattern_ref('walking-route')), block_types='core/post-content')
pattern('prints-page', 'Page: prints', 'shop', J(pattern_ref('prints-row')), block_types='core/post-content')
pattern('about-page', 'Page: about', 'about', J(pattern_ref('about-bio'), pattern_ref('instagram-strip'), pattern_ref('workshop-lettering'), pattern_ref('contact-block')), block_types='core/post-content')


# ------------------------------------------------------------------ round 2: more of the kit
pattern('hero-on-the-wall', 'Opener: on the wall this week', 'featured', group(J(
    para('On the wall this week', className='is-style-tape'),
    heading('Hofbogen pillar 15, Rotterdam-Noord', 1, className='is-style-wordmark'),
    columns(('60%', image('viaduct.jpg', 'A concrete viaduct pillar painted with four black-and-white faces, bike path in front', 'Pillar 14, finished in May. Pillar 15 is next to it.')),
            (None, J(para('Painting from a cherry picker Monday to Friday, 8am to 4pm, until 14 October. Come and look from the bike path, not from under the platform.', fontSize='large'),
                     para('<a href="/viaduct-pillar-hofplein-line/">The first pillar</a><br><a href="/commissions/">Book the next wall</a>', fontSize='large'))),
            style={'spacing': {'blockGap': {'left': sp(50)}}})),
    align='full', layout={'type': 'default'}), description='Alternative opener: the wall being painted right now.')

pattern('featured-mural', 'Featured mural (big photo and facts)', 'portfolio', columns(
    ('66%', image('corner-block.jpg', MURALS[1]['alt'], 'Corner block, Witte de With, 2025')),
    (None, J(heading(MURALS[1]['t'], 2, fontSize='x-large'), para(MURALS[1]['note']), facts(MURALS[1]))),
    align='full', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('detail-gallery', 'Detail shots (lightbox)', 'portfolio,gallery', gallery([
    ('gable-objects.jpg', MURALS[2]['alt'], 'Whole gable'), ('viaduct.jpg', MURALS[0]['alt'], 'Pillar from the bike path'),
    ('letters.jpg', MURALS[4]['alt'], 'Letters, detail'), ('window.jpg', MURALS[7]['alt'], 'Painted window, up close')], columns=4, align='full'))

pattern('before-after', 'Before and after', 'portfolio', columns(
    (None, image('ruin.jpg', 'A grey half-ruined wall with faded graffiti behind branches', 'Before: the Zuidplein garage wall, spring 2021', className='is-style-gone')),
    (None, image('school-faces.jpg', 'A courtyard wall with five laughing faces in coloured dots', 'After: a courtyard wall two weeks later')),
    align='full', style={'spacing': {'blockGap': {'left': sp(40)}}}))

pattern('sketch-proposal', 'Design proposal (sketch to wall)', 'process', columns(
    ('40%', image('ladder.jpg', 'Black-and-white photo of a painter on a stepladder at a large abstract wall')),
    (None, J(heading('What you get before I paint', 3),
             lst(['A photo of your wall with the design drawn on it, to scale.', 'Two colour versions, one quiet, one loud.', 'A price and a painting week.', 'One round of changes. After that, we start.']),
             para('The proposal costs €250, which comes off the final price if you go ahead.'))),
    align='full', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('wall-palette', 'Paint colours used on a wall', 'process', J(
    heading('Paint on the Witte de With corner', 3),
    group(J(*[group(para(n, fontSize='small', style={'typography': {'fontWeight': '700'}}), backgroundColor=bg, textColor=tc, style={'spacing': {'padding': {'top': sp(60), 'bottom': sp(20), 'left': sp(20), 'right': sp(20)}}})
              for n, bg, tc in [('Tape yellow', 'accent-2', 'contrast'), ('Link blue', 'accent', 'base'), ('Black', 'contrast', 'base'), ('Concrete', 'surface', 'contrast'), ('Primer white', 'base', 'contrast')]]),
        layout={'type': 'grid', 'columnCount': 5, 'minimumColumnWidth': '8rem'}, style={'spacing': {'blockGap': '0'}}),
    para('Keim silicate paint, 23 colours in total. These five carry most of the wall.', fontSize='small')))

pattern('schools-entry', 'For schools', 'call-to-action', columns(
    ('45%', image('school-archive.jpg', 'Black-and-white photo of a teacher and children on scaffolding painting a mural')),
    (None, J(heading('Schools', 2), para('Every school wall includes one painting day per class. The pupils draw, we pick the drawings together, and they paint the lower two metres. I do the rest.', fontSize='large'),
             lst(['From €2,800 for a playground wall up to 30 m²', 'Painted in school holidays or on Wednesdays', 'Anti-graffiti coat included']),
             buttons(('Ask about a school wall', 'mailto:walls@example.com?subject=School%20wall')))),
    align='full', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('homes-entry', 'For homes', 'call-to-action', columns(
    (None, J(heading('Homes', 2), para('Back gardens, stairwells, a kid\'s bedroom, once a ceiling. Small walls take two or three days and I clean up every evening.', fontSize='large'),
             buttons(('Send a photo of your wall', 'mailto:walls@example.com?subject=Home%20wall')))),
    ('50%', image('garden-wall.jpg', MURALS[6]['alt'])),
    align='full', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('business-entry', 'For businesses', 'call-to-action', columns(
    ('50%', image('window.jpg', MURALS[7]['alt'])),
    (None, J(heading('Shops and businesses', 2), para('Shop fronts, signs, shutters and gable ends. Hand-lettered, not printed. I work early mornings so you can stay open.', fontSize='large'),
             buttons(('Get a price for your front', 'mailto:walls@example.com?subject=Shop%20front')))),
    align='full', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('faq', 'Questions about murals', 'call-to-action', J(
    heading('Questions', 2),
    details('How long does a mural last?', para('Outdoors, 10 to 15 years with silicate paint and an anti-graffiti coat. Sun on a south wall fades reds first.')),
    details('What if someone tags it?', para('The anti-graffiti coat lets you wash tags off with hot water. For the first year, I come back once for free.')),
    details('Can I choose the design?', para('You choose the subject and the colours you can live with. I draw it. If you have a finished design, I am the wrong painter.')),
    details('Do you need scaffolding?', para('Above 4 metres, a cherry picker, which we hire by the day. You arrange the parking permit with the gemeente.'))))

pattern('availability', 'Availability by month', 'banner', group(J(
    heading('Open weeks', 3, fontSize='large'),
    lst(['October: full', 'November: indoor walls only, two weeks free', 'December: closed', 'January to March: indoor walls and schools', 'April 2027 onwards: outdoor walls, booking now']))),
    description='Update the months as the diary fills.')

pattern('client-quotes', 'Quotes from clients', 'testimonials', columns(
    (None, quote('She painted the shutter at 6am so we could open at 9. Nobody has tagged it since.', 'Joost, Bakkerij Van Olst, 2022')),
    (None, quote('Year 5 still talk about the painting day. The dots are their dots.', 'Mevrouw Aydın, teacher, Colegio Maravillas exchange, 2024')),
    align='full', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('instagram-strip', 'Recent photos strip', 'portfolio,gallery', J(
    para('Recent, from the phone', fontSize='large'),
    gallery([('tunnel.jpg', MURALS[5]['alt'], ''), ('letters.jpg', MURALS[4]['alt'], ''), ('gable-objects.jpg', MURALS[2]['alt'], ''),
             ('school-faces.jpg', MURALS[3]['alt'], ''), ('corner-block.jpg', MURALS[1]['alt'], ''), ('viaduct.jpg', MURALS[0]['alt'], '')], columns=6, align='full')))

pattern('wall-index', 'Every wall, one line each', 'portfolio,query', query(
    row(J(dyn('post-title', isLink=True, level=3, fontSize='x-large'), dyn('post-terms', term='category', fontSize='large'), dyn('post-date', format='Y', fontSize='large')),
        justify='space-between', className='is-style-rule-top', style={'spacing': {'padding': {'top': sp(20)}}}),
    per_page=50, align='full'), description='A text index of every wall, newest first.')

pattern('materials', 'Paint and materials', 'process', J(
    heading('What goes on your wall', 3),
    lst(['Keim silicate paint outside: it bonds with stone and brick and breathes.', 'Acrylic inside, low-odour, so rooms can be used the next day.', 'Montana spray only for lettering edges and small details.', 'An anti-graffiti coat on everything below 3 metres.'])))

pattern('contact-strip', 'Contact strip (black)', 'contact', group(columns(
    (None, heading('walls@example.com', 2, fontSize='x-large')),
    (None, para('+31 6 1234 5678, weekdays 9 to 5. Studio 2.14, Keilestraat 9, Rotterdam. Visits by appointment.', fontSize='large')),
    verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(50)}}}), className='is-style-blackout', align='full'))

pattern('workshop-lettering', 'Lettering workshop', 'call-to-action', group(J(
    heading('Brush lettering, one Saturday a month', 3),
    para('Six people, one long wall in the studio, sign-painter brushes and enamel. 10am to 4pm, €95 with lunch. Next dates: 17 October, 21 November.', fontSize='large'),
    buttons(('Book a place', 'mailto:walls@example.com?subject=Lettering%20workshop'))), className='is-style-concrete', align='full'))

# more page layouts
pattern('schools-page', 'Page: schools', 'call-to-action', J(pattern_ref('schools-entry'), spacer(), pattern_ref('client-quotes'), pattern_ref('faq')), block_types='core/post-content')
pattern('homes-business-page', 'Page: homes and shops', 'call-to-action', J(pattern_ref('homes-entry'), spacer(), pattern_ref('business-entry'), spacer(), pattern_ref('sketch-proposal'), pattern_ref('materials')), block_types='core/post-content')
pattern('index-page', 'Page: index of walls', 'portfolio', J(pattern_ref('wall-index'), spacer(), pattern_ref('archived-walls')), block_types='core/post-content')

# ------------------------------------------------------------------ templates
mp = {'spacing': {'padding': {'top': sp(40), 'bottom': sp(70), 'left': sp(40), 'right': sp(40)}}}
full = {'type': 'default'}
write('templates/front-page.html', page_template(J(
    pattern_ref('wordmark-hero'), pattern_ref('mural-wall'), spacer('var:preset|spacing|70'), pattern_ref('type-entry-points'), pattern_ref('client-quotes'),
    spacer('var:preset|spacing|60'), pattern_ref('archived-walls'), pattern_ref('instagram-strip')),
    layout=full, style={'spacing': {'blockGap': '0', 'padding': {'left': sp(40), 'right': sp(40)}}}))
write('templates/home.html', page_template(J(
    heading('Murals', 1, className='is-style-wordmark'),
    dyn('categories', className='is-style-big-links', showPostCounts=False),
    para('<a href="/index/">Every wall as a list</a> / <a href="/tag/gone/">Walls that are gone</a>', fontSize='large'),
    pattern_ref('mural-archive')), layout=full, style=mp))
archive = J(dyn('query-title', type='archive', showPrefix=False, className='is-style-wordmark'), dyn('term-description'), pattern_ref('mural-archive'))
write('templates/archive.html', page_template(archive, layout=full, style=mp))
write('templates/tag-gone.html', page_template(J(
    heading('Gone', 1, className='is-style-wordmark'),
    para('Painted over, knocked down, or repainted grey. Every wall on this page is gone from the street and stays here.', fontSize='large'),
    pattern_ref('mural-archive')), layout=full, style=mp))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', className='is-style-wordmark'), pattern_ref('post-list')), layout=full, style=mp))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', fontSize='xx-large'),
    dyn('search', label='Search', showLabel=False, placeholder='City, street, school', buttonText='Search'),
    pattern_ref('post-list')), layout=full, style=mp))
write('templates/404.html', page_template(J(
    heading('Painted over', 1, className='is-style-wordmark'),
    para('Nothing on this address any more. Try the <a href="/map/">map of every wall</a> or search.', fontSize='large'),
    dyn('search', label='Search', showLabel=False, placeholder='City, street, school', buttonText='Search')), layout=full, style=mp))
write('templates/page.html', page_template(J(dyn('post-title', level=1, className='is-style-wordmark'), dyn('post-content', layout={'type': 'constrained', 'justifyContent': 'left'})), layout=full, style=mp))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, className='is-style-wordmark'), dyn('post-content', layout={'type': 'default'})), layout=full, style=mp))
single = J(dyn('post-featured-image', align='full'),
           columns(('60%', J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-terms', term='category', fontSize='large'))),
                   (None, J(dyn('post-content', layout={'type': 'default'}), dyn('post-terms', term='post_tag', prefix='Tagged '))),
                   align='full', style={'spacing': {'blockGap': {'left': sp(60)}}}),
           row(J(dyn('post-navigation-link', type='previous', label='Previous wall', showTitle=True), dyn('post-navigation-link', label='Next wall', showTitle=True)),
               justify='space-between', align='full', className='is-style-rule-top'))
write('templates/single.html', page_template(single, layout=full, style={'spacing': {'padding': {'bottom': sp(70), 'left': sp(40), 'right': sp(40)}}}))
write('templates/single-mural.html', page_template(single, layout=full, style={'spacing': {'padding': {'bottom': sp(70), 'left': sp(40), 'right': sp(40)}}}))

# ------------------------------------------------------------------ demo
posts = [{'title': m['t'], 'date': '%s-%02d-10' % (m['year'], 9 - i % 6), 'category': m['cat'], 'tags': m['tags'] + [m['city']], 'image': m['img'],
          'template': 'single-mural', 'content': mural_content(m)} for i, m in enumerate(MURALS)]
demo = {
    'site': {'title': 'Nora Bakri', 'tagline': 'Murals and lettering, Rotterdam'},
    'categories': [{'slug': 'homes', 'name': 'Homes', 'description': 'Back gardens, stairwells, one bedroom ceiling.'},
                   {'slug': 'businesses', 'name': 'Businesses', 'description': 'Shop fronts, signs and shutters.'},
                   {'slug': 'schools', 'name': 'Schools', 'description': 'Painted with the pupils, one day of painting per class included.'},
                   {'slug': 'public', 'name': 'Public walls', 'description': 'Festivals, the gemeente and legal walls.'}],
    'front_page': 'home', 'posts_page': 'murals',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'murals', 'title': 'Murals', 'content': ''},
        {'slug': 'map', 'title': 'Map', 'pattern': 'wall/map-page', 'template': 'page-wide'},
        {'slug': 'commissions', 'title': 'Commissions', 'pattern': 'wall/commissions-page', 'template': 'page-wide'},
        {'slug': 'prints', 'title': 'Prints', 'pattern': 'wall/prints-page', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About', 'pattern': 'wall/about-page', 'template': 'page-wide'},
        {'slug': 'schools', 'title': 'Schools', 'pattern': 'wall/schools-page', 'template': 'page-wide'},
        {'slug': 'homes-and-shops', 'title': 'Homes and shops', 'pattern': 'wall/homes-business-page', 'template': 'page-wide'},
        {'slug': 'index', 'title': 'Index', 'pattern': 'wall/index-page', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Murals', 'url': '/murals/'}, {'label': 'Map', 'url': '/map/'}, {'label': 'Commissions', 'url': '/commissions/'},
            {'label': 'Schools', 'url': '/schools/'}, {'label': 'Homes and shops', 'url': '/homes-and-shops/'},
            {'label': 'Prints', 'url': '/prints/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs('demos/wall', exist_ok=True)
with open('demos/wall/content.json', 'w', encoding='utf-8') as f:
    json.dump(demo, f, indent=1, ensure_ascii=False)
with open('demos/wall/fonts-claim.txt', 'w') as f:
    f.write('display: Special Gothic Condensed One\n')
write('functions.php', """<?php
/**
 * Wall: pattern categories only.
 *
 * @package wall
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
print('wall built')
