# coat: Two Coats, painters and decorators in Dublin 7 (idea 101, owner's brief: "more colours and fun").
# Direction: the paint chart. The site is a fan deck of real colour chips taken from real jobs, loud and cheerful,
#   because the owner asked for colour and fun and a decorator's stock in trade is named colours.
# Fonts: Rowdies (display, chunky sign-writer sans, claimed as new: the brief moved away from Gambetta's restraint),
#   Figtree (body, also colour codes at small size with tabular figures). Two families only.
# Palette: primer white, railings black, Bamboozle red accent, primrose surface, plus ten chip colours named after the paint.
# Layout idea: a full-width run of tall paint chips as the hero, a stripe of chips across the header, and every job page
#   opening with its colour card (chip, colour name, maker's number, where it went) before the photos.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('coat')


def grid(inner, min_width='16rem', layout=None, **attrs):
    """Grid group; pass layout to fix the column count."""
    return group(inner, layout=layout or {'type': 'grid', 'minimumColumnWidth': min_width}, **attrs)

S = 'coat'
D = THEME['dir']

# ---------------------------------------------------------------- tokens
PALETTE = [
    ('base', '#FFFFFF', 'Primer white'),
    ('contrast', '#1B1A1F', 'Railings'),
    ('accent', '#B8372E', 'Bamboozle red'),
    ('surface', '#FFF0B0', 'Primrose'),
    ('line', '#1B1A1F', 'Cutting-in line'),
    ('muted', '#56525C', 'Undercoat grey'),
    ('hague', '#2E3B4E', 'Hague blue'),
    ('locks', '#D9612E', 'Charlotte\'s locks'),
    ('babouche', '#EDC65A', 'Babouche'),
    ('arsenic', '#6FA396', 'Arsenic'),
    ('sulking', '#D8A7A0', 'Sulking pink'),
    ('calke', '#4E6A45', 'Calke green'),
    ('stiffkey', '#3E5468', 'Stiffkey blue'),
    ('plaster', '#EBCBB8', 'Setting plaster'),
    ('yellowcake', '#F5DA62', 'Yellowcake'),
    ('mint', '#BFE6D1', 'Mint'),
    ('door-blue', '#1D4FB8', 'Door blue'),
]
PAL = {s: c for s, c, _ in PALETTE}


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


# Text colour for each chip, checked at 4.5:1.
CHIP_TEXT = {}
for s in ['hague', 'locks', 'babouche', 'arsenic', 'sulking', 'calke', 'stiffkey', 'plaster', 'yellowcake', 'mint', 'door-blue', 'accent', 'contrast', 'surface', 'base']:
    t = 'base' if ratio(PAL[s], PAL['base']) >= ratio(PAL[s], PAL['contrast']) else 'contrast'
    CHIP_TEXT[s] = t
    assert ratio(PAL[s], PAL[t]) >= 4.5, (s, t, ratio(PAL[s], PAL[t]))

fonts = [f for f in json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies'] if f['slug'] != 'mono']
for f in fonts:
    if f['slug'] == 'body':
        f['name'] = 'Figtree'

FOCUS = {'outline': {'color': 'var:preset|color|contrast', 'offset': '3px', 'style': 'solid', 'width': '3px'}}

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.8125rem', 'name': 'Code', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.75rem', 'name': 'Title', 'fluid': {'min': '2.5rem', 'max': '3.75rem'}},
                {'slug': 'display', 'size': '6.5rem', 'name': 'Display', 'fluid': {'min': '3.1rem', 'max': '6.5rem'}},
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': [
            {'slug': 'chip', 'name': 'Chip (hard offset)', 'shadow': '5px 5px 0 0 var(--wp--preset--color--contrast)'},
        ]},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True,
                   'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Chip'}, {'slug': 'button', 'size': '0.5rem', 'name': 'Button'}, {'slug': 'input', 'size': '0.25rem', 'name': 'Input'}]},
        'custom': {'measure': '66ch'},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': FOCUS},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '1.02', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.4'}},
            'button': {
                'color': {'background': 'var:preset|color|yellowcake', 'text': 'var:preset|color|contrast'},
                'border': {'radius': '0.5rem', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'shadow': 'var:preset|shadow|chip',
                'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'fontSize': 'var:preset|font-size|medium'},
                'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '1.1em', 'right': '1.1em'}},
                ':hover': {'color': {'background': 'var:preset|color|mint', 'text': 'var:preset|color|contrast'}},
                ':focus': FOCUS,
            },
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.5'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|medium', 'fontWeight': '400'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}},
            'core/post-featured-image': {'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
            'core/image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '3px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.3'},
                           'color': {'background': 'var:preset|color|mint'},
                           'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                           'shadow': 'var:preset|shadow|chip',
                           'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
                           'elements': {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'normal'}}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}, 'css': '& th{text-align:left;font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--x-small);font-weight:500}& td{border-color:var(--wp--preset--color--contrast)}& th{border-color:var(--wp--preset--color--contrast)}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);cursor:pointer}'},
            'core/code': {'typography': {'fontFamily': 'var:preset|font-family|body'}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'}},
            'core/search': {'border': {'radius': '0.25rem'}, 'typography': {'fontSize': 'var:preset|font-size|small'},
                            'css': '& .wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0.25rem}'},
            'core/list': {'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
        },
        'css': '.wp-block-post-content > * + :is(h2,h3,.wp-block-columns,.wp-block-media-text,.wp-block-group,.wp-block-image){margin-block-start:var(--wp--preset--spacing--60)}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none}table,.is-style-chip,.is-style-chip-short{font-variant-numeric:tabular-nums}'
               ':where(.wp-block-post-content) p{max-width:var(--wp--custom--measure)}'
               'a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid var(--wp--preset--color--contrast);outline-offset:3px;box-shadow:0 0 0 6px var(--wp--preset--color--yellowcake)}'
               '@media (prefers-reduced-motion:no-preference){.is-style-chip{transition:transform .15s}.is-style-chip:hover{transform:translateY(-6px)}.wp-element-button{transition:transform .12s,box-shadow .12s}.wp-element-button:hover{transform:translate(2px,2px);box-shadow:3px 3px 0 0 var(--wp--preset--color--contrast)}}',
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Season notice'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-job', 'title': 'Job with colour card', 'postTypes': ['post']},
    ],
}

# ---------------------------------------------------------------- round 2: lightbox, spec rows, pattern categories
R2_CSS = ('.is-style-specs > .wp-block-group{padding-block:.55em;border-bottom:1px solid var(--wp--preset--color--line);gap:.2rem 1.25rem!important;margin:0!important}'
          '.is-style-specs > .wp-block-group > :first-child{flex:0 0 min(36%,12rem);font-weight:600;margin:0}'
          '.is-style-specs > .wp-block-group > :last-child{flex:1 1 14rem;margin:0}')
theme['settings']['blocks'] = {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}}
theme['styles']['css'] += R2_CSS + '.is-style-chip a,.is-style-chip-short a,.is-style-card[class*=-background-color] a:not(.wp-element-button){color:inherit}'


def specs(pairs, **attrs):
    """Label and value rows made from groups, instead of a two-column table."""
    return group(J(*[row(J(para(k), para(v))) for k, v in pairs]), className='is-style-specs', layout={'type': 'default'}, **attrs)


def pattern_categories(cats):
    lines = ["<?php", "/**", " * Registers this theme's block pattern categories. Nothing else.", " */", "add_action( 'init', function () {"]
    for slug, label in cats:
        lines.append("\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', '%s' ) ) );" % (slug, label, THEME['slug']))
    lines.append('} );')
    write('functions.php', '\n'.join(lines))


os.makedirs(D, exist_ok=True)
with open(os.path.join(D, 'theme.json'), 'w') as f:
    json.dump(theme, f, indent='\t', ensure_ascii=False)

write('style.css', '''/*
Theme Name: Coat
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A bright, colour-card theme for painters and decorators who want customers to see the actual paint colours used on every job.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: coat
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column, grid-layout
*/''')

# ---------------------------------------------------------------- style variations
def variation(name, title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}
    if extra:
        d['styles'] = extra
    write('styles/%s.json' % name, json.dumps(d, indent='\t', ensure_ascii=False))


def swap(**changes):
    return [(s, changes.get(s.replace('-', '_'), c), n) for s, c, n in PALETTE]


variation('limewash', 'Limewash', swap(base='#F1ECE2', surface='#E4EDE6', accent='#2E4F7A', muted='#524E57'))
variation('dark-room', 'Dark room', swap(base='#1B1A1F', contrast='#FFFFFF', surface='#2E3B4E', line='#FFFFFF', muted='#C9C6CF', accent='#F5DA62'),
          {'elements': {'button': {'border': {'color': 'var:preset|color|base'}}}})
variation('primer', 'Primer', swap(surface='#EDEBE7', accent='#1D4FB8', line='#8C8990', muted='#56525C'))

# ---------------------------------------------------------------- section styles
def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))


section('chip', 'Paint chip', ['core/group'], {
    'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}, 'blockGap': '0'},
    'css': '&{aspect-ratio:4/5;justify-content:flex-end!important}& p{margin:0}& p:first-child{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);line-height:1.1}&:nth-child(3n+1){rotate:-1.5deg}&:nth-child(4n+2){rotate:1.2deg}',
})
section('chip-short', 'Paint chip (short)', ['core/group'], {
    'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}, 'blockGap': '0'},
    'css': '&{min-height:7.5rem;justify-content:flex-end!important}& p{margin:0}& p:first-child{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--medium);line-height:1.15}',
})
section('pad-lg', 'Roomy section', ['core/group'], {'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}})
section('page-main', 'Page body', ['core/group'], {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}})
section('site-header', 'Site header', ['core/group'], {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'bottom': 'var:preset|spacing|30'}}})
section('site-footer', 'Site footer', ['core/group'], {'color': {'background': 'var:preset|color|calke', 'text': 'var:preset|color|base'}, 'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}}}, 'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|50'}}})
section('rule-top', 'Rule above', ['core/group'], {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('stripe', 'Chip stripe', ['core/group'], {
    'spacing': {'blockGap': '0', 'padding': {'top': '0', 'bottom': '0'}},
    'css': '&{gap:0!important}& > *{flex:1 1 0;min-height:0.75rem;margin:0!important}',
})
section('card', 'Taped card', ['core/group', 'core/columns', 'core/column'], {
    'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
    'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'shadow': 'var:preset|shadow|chip',
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
})
section('band', 'Colour band', ['core/group'], {
    'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}},
    'border': {'top': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'bottom': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
})
section('notice', 'Notice bar', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|yellowcake'},
    'elements': {'link': {'color': {'text': 'var:preset|color|yellowcake'}}},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
})
section('price-list', 'Price list', ['core/table'], {
    'typography': {'fontSize': 'var:preset|font-size|medium'},
    'css': '&{font-variant-numeric:tabular-nums}& td{padding:.7em .5em;border-width:0 0 2px 0!important}& th{border-width:0 0 3px 0!important}& td:last-child{text-align:right;white-space:nowrap}& th:last-child{text-align:right;white-space:nowrap}& thead{border:0}',
})
section('inline-list', 'Inline list', ['core/categories', 'core/list'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|medium'},
    'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.5rem}& li{border:2px solid var(--wp--preset--color--contrast);padding:.2em .8em;border-radius:.5rem}& a{text-decoration:none;color:var(--wp--preset--color--contrast)}',
})
section('job-grid', 'Job grid', ['core/post-template'], {
    'css': '& > li{border:2px solid var(--wp--preset--color--contrast);background:var(--wp--preset--color--base);padding:0 0 var(--wp--preset--spacing--30)}& > li > *:not(.wp-block-post-featured-image){padding-left:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30)}& .wp-block-post-featured-image{border-width:0 0 2px 0!important}& > li:nth-child(3n+1){background:var(--wp--preset--color--mint)}& > li:nth-child(3n+2){background:var(--wp--preset--color--yellowcake)}& > li:nth-child(3n){background:var(--wp--preset--color--plaster)}',
})

# ---------------------------------------------------------------- helpers
def chip(slug, name, code, where='', short=False):
    t = CHIP_TEXT[slug]
    inner = [para(name), para(code, fontSize='x-small')]
    if where:
        inner.append(para(where, fontSize='x-small'))
    return stack(J(*inner), backgroundColor=slug, textColor=t, className='is-style-chip-short' if short else 'is-style-chip')


def chips(items, min_width='9.5rem', short=False, **attrs):
    return grid(J(*[chip(*i, short=short) for i in items]), min_width=min_width, **attrs)


WIDE_PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}
PHONE = '087 555 0142'
EMAIL = 'hello@example.com'

# ---------------------------------------------------------------- patterns: front page
HERO_CHIPS = [
    ('calke', 'Calke Green', 'F&amp;B No. 34', 'Front door, Prussia St'),
    ('locks', 'Charlotte\'s Locks', 'F&amp;B No. 268', 'Sitting room, Drumcondra'),
    ('yellowcake', 'Yellowcake', 'F&amp;B No. 279', 'Box room, Cabra'),
    ('hague', 'Hague Blue', 'F&amp;B No. 30', 'Kitchen island, Glasnevin'),
    ('sulking', 'Sulking Room Pink', 'F&amp;B No. 295', 'Bedroom, Stoneybatter'),
    ('arsenic', 'Arsenic', 'F&amp;B No. 214', 'Bathroom, Phibsborough'),
    ('accent', 'Bamboozle', 'F&amp;B No. 304', 'Shop door, Manor St'),
    ('babouche', 'Babouche', 'F&amp;B No. 223', 'Hall and stairs, Smithfield'),
]

pattern('hero-colour-chart', 'Hero: colour chart from real jobs', 'hero,featured', group(J(
    heading('Two Coats, painters and decorators in Dublin 7', 1, align='wide', fontSize='xx-large'),
    para('Every chip is a colour we put on a wall, a door or a kitchen this year, with the street it went on.', align='wide', fontSize='large'),
    chips(HERO_CHIPS, min_width='8.5rem', align='wide'),
    columns(
        ('58%', para('Aoife Byrne and Tunde Adeyemi, plus Marek and Ciara when the job needs four. Interiors, front doors, hand-painted kitchens and old sash windows between the canal and the Tolka, mostly in colours people were nervous about.')),
        (None, J(buttons(('Send us photos for a quote', '/contact/')),
                 para('Or ring Aoife on <a href="tel:0875550142">%s</a>, 8am to 6pm, Monday to Friday.' % PHONE, fontSize='small'))),
        align='wide', verticalAlignment='bottom')),
    align='full', className='is-style-pad-lg'), description='The signature hero: a fan of tall paint chips, each one a colour from a real job.')

pattern('recent-jobs', 'Recent jobs (grid)', 'portfolio,query', group(J(
    row(J(heading('Recent jobs', 2), para('<a href="/jobs/">Every job, by type</a>', fontSize='small')), justify='space-between', align='wide'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), dyn('post-terms', term='category', separator=' / '), dyn('post-title', isLink=True, level=3, fontSize='large')),
          per_page=6, align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '17rem'}, template_class='is-style-job-grid')),
    align='wide', layout={'type': 'default'}, className='is-style-pad-lg'), keywords='jobs, projects, portfolio')

pattern('jobs-archive', 'Jobs archive (inherits the query)', 'portfolio,query', inherit_query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), dyn('post-terms', term='category', separator=' / '), dyn('post-title', isLink=True, level=2, fontSize='large')),
    align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '17rem'}, template_class='is-style-job-grid'), inserter=False)

pattern('post-list', 'Post list', 'posts,query', inherit_query(
    J(row(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-terms', term='category')), justify='space-between')),
    align='wide'), inserter=False)

# ---------------------------------------------------------------- signature: colour card for a job
pattern('colour-card', 'Colour card: paints used on this job', 'portfolio,featured', group(J(
    heading('Colours on this job', 2, fontSize='x-large'),
    chips([('locks', 'Charlotte\'s Locks', 'F&amp;B No. 268', 'Walls, estate emulsion'),
           ('contrast', 'Railings', 'F&amp;B No. 31', 'Skirting and panels, eggshell'),
           ('plaster', 'Setting Plaster', 'F&amp;B No. 231', 'Ceiling, estate emulsion'),
           ('babouche', 'Babouche', 'F&amp;B No. 223', 'Inside the alcove shelves')], min_width='10rem'),
    para('Ask us for the exact tins if you want to match them. We keep a note of every colour and finish per room for ten years.', fontSize='small')),
    align='wide', layout={'type': 'default'}), description='A row of chips with colour name, maker\'s number and where each paint went. Edit each chip\'s background to match the paint.')

pattern('job-facts', 'Job facts (rooms, prep, paint, time)', 'portfolio', specs([
    ('Rooms', 'Front room and back room, knocked through'),
    ('Before', 'Magnolia over woodchip, gloss on the skirting'),
    ('Prep', 'Woodchip steamed off, walls skimmed by Declan Murray, two mist coats'),
    ('Paint', 'Farrow &amp; Ball Estate Emulsion and Estate Eggshell'),
    ('Time on site', '9 working days, two painters'),
    ('Cost', '€3,950 including paint and plastering')]))

pattern('before-after', 'Before and after (two photos)', 'portfolio,gallery', columns(
    (None, image('bedroom.jpg', 'Watercolour of a pale 1820s bedroom with a four-poster bed and a chest of drawers', 'Before: pale, polite and a bit tired')),
    (None, image('decorator.jpg', 'A room painted deep orange with black panels, wicker chairs and a desk', 'After: Charlotte\'s Locks with Railings panels')),
    align='wide'), description='Two images side by side with Before and After captions. Swap in your own photos taken from the same spot.')

pattern('colour-schedule', 'Colour schedule (printable, room by room)', 'portfolio,text', J(
    heading('Your colour schedule', 3),
    para('We leave a printed copy of this in the meter cupboard. Keep it for touch-ups, or give it to the next painter.', fontSize='small'),
    table([['Hall', 'Walls', 'Babouche No. 223', 'Estate Emulsion'],
           ['Hall', 'Stairs, spindles, skirting', 'Railings No. 31', 'Estate Eggshell'],
           ['Front room', 'Walls', 'Charlotte\'s Locks No. 268', 'Estate Emulsion'],
           ['Front room', 'Ceiling', 'Setting Plaster No. 231', 'Estate Emulsion'],
           ['Kitchen', 'Units', 'Hague Blue No. 30', 'Modern Eggshell, brushed'],
           ['Front door', 'Outside face', 'Calke Green No. 34', 'Exterior Eggshell']],
          head=['Room', 'Surface', 'Colour', 'Finish'])), description='The room-by-room list the client keeps for touch-ups.')

# ---------------------------------------------------------------- prices
pattern('price-guide', 'What painters charge in Dublin (price guide)', 'prices,services', J(
    heading('What painting costs in Dublin, roughly', 2),
    para('These are our prices for 2026, including paint, prep and VAT. Other decent painters in Dublin charge about the same. If a quote is half this, ask what they are leaving out.'),
    table([['Box room, walls and ceiling', '2 days', '€650'],
           ['Double bedroom, walls, ceiling, woodwork', '3 days', '€1,100'],
           ['Hall, stairs and landing (terraced house)', '5 to 6 days', '€2,400'],
           ['Front door, both sides, with prep', '1 to 2 days', '€480'],
           ['Hand-painted kitchen, up to 20 doors', '6 to 7 days', '€3,200'],
           ['Sash window, strip and repaint, each', 'half a day', '€380'],
           ['Day rate, one painter', '8am to 4:30pm', '€290']],
          head=['Job', 'Usually takes', 'From'], className='is-style-price-list'),
    para('Paint is the good stuff unless you tell us otherwise. Wallpaper hanging is quoted per roll. We charge €60 for a colour visit, which comes off the job if you book us.', fontSize='small')))

pattern('prices-page', 'Page: prices', 'prices', J(
    pattern_ref('booking-now'), pattern_ref('price-guide'), pattern_ref('whats-included'), pattern_ref('guarantee'), pattern_ref('what-we-dont-do'), pattern_ref('faq'), pattern_ref('quote-request')), block_types='core/post-content')

pattern('whats-included', 'What a quote includes', 'services', group(J(
    heading('Every quote includes', 3),
    lst(['Moving and covering furniture, and putting it back.',
         'Dust sheets on every floor we walk on, including the stairs.',
         'Filling, sanding and a mist coat on new plaster.',
         'Two finish coats. Three for reds and yellows, which cover badly.',
         'A printed colour schedule and the leftover paint, labelled.'])),
    className='is-style-card'))

pattern('what-we-dont-do', 'What we don\'t do', 'text', group(J(
    heading('What we don\'t do', 3),
    para('We don\'t spray kitchens. Every door is brushed and rolled on site, which takes longer and looks like a painted kitchen should. We don\'t work above three storeys outside, and we don\'t do new-build snagging for developers. Grey is allowed, but we will try to talk you out of it once.')),
    backgroundColor='sulking', textColor=CHIP_TEXT['sulking'], className='is-style-card'))

# ---------------------------------------------------------------- process
STEPS = [('Visit', 'We come round, look at the walls and the woodwork, and talk colour. Takes about 40 minutes. Free within Dublin 7, 9 and 11.'),
         ('Quote', 'A written quote within three working days, room by room, with the paint named.'),
         ('Prep', 'The boring bit, and most of the job. Filling, sanding, caulking, sugar-soaping, knotting.'),
         ('Protect', 'Floors sheeted, furniture wrapped, handles taped. Your cat stays in the kitchen.'),
         ('Paint', 'Cutting in by hand, no tape on walls. Two coats minimum, drying times kept.'),
         ('Snag', 'We walk round with you and a torch before we pack up, and fix what you point at.')]
COLS6 = ['yellowcake', 'mint', 'plaster', 'arsenic', 'sulking', 'babouche']
pattern('process', 'Process: visit, quote, prep, protect, paint, snag', 'services', J(
    heading('How a job goes', 2),
    grid(J(*[stack(J(para('%d' % (i + 1), fontFamily='display', fontSize='xx-large'), heading(t, 3, fontSize='large'), para(d, fontSize='small')),
                    backgroundColor=COLS6[i], textColor=CHIP_TEXT[COLS6[i]], className='is-style-card') for i, (t, d) in enumerate(STEPS)]),
         min_width='15rem', align='wide')), description='Six numbered steps, each on its own colour.')

pattern('team', 'Who will be in your home', 'about', J(
    heading('Who will be in your home', 2),
    columns(
        (None, group(J(heading('Aoife Byrne', 3, fontSize='large'), para('Started Two Coats in 2012 after eight years with a firm in Rathmines. Does the colour visits, the quotes and most of the cutting in. Will not stop talking about Babouche.'),
                       para('Ask for her on sash windows.', fontSize='small')), className='is-style-card', backgroundColor='yellowcake', textColor=CHIP_TEXT['yellowcake'])),
        (None, group(J(heading('Tunde Adeyemi', 3, fontSize='large'), para('Joined in 2015 and became a partner in 2019. Kitchens, doors and anything that needs a steady brush on a flat panel. Grew up in Ibadan and Cabra, in that order.'),
                       para('Ask for him on kitchens.', fontSize='small')), className='is-style-card', backgroundColor='mint', textColor=CHIP_TEXT['mint'])),
        (None, group(J(heading('Marek and Ciara', 3, fontSize='large'), para('Marek Wróbel does prep and wallpaper. Ciara Lynch is in her third year of the painting and decorating apprenticeship at Bolton Street. On bigger jobs you will meet both.'),
                       para('Both Safe Pass certified.', fontSize='small')), className='is-style-card', backgroundColor='plaster', textColor=CHIP_TEXT['plaster'])),
        align='wide')))

pattern('process-page', 'Page: how we work', 'services', J(
    pattern_ref('process'), pattern_ref('team'), pattern_ref('wallpaper'), pattern_ref('whats-included'), pattern_ref('guarantee'), pattern_ref('colour-schedule'), pattern_ref('insurance-line')), block_types='core/post-content')

pattern('insurance-line', 'Insurance and membership line', 'about', para(
    'Public liability insurance to €6.5 million with Allianz. Tax cleared. Members of the Painting and Decorating Contractors of Ireland. Lead-safe working on pre-1970 paintwork.',
    fontSize='x-small', className='is-style-default'))

# ---------------------------------------------------------------- kitchens
pattern('kitchen-intro', 'Hand-painted kitchens', 'services', media_text('kitchen.jpg', 'A small kitchen with mint green cabinets, a red and white table and a green wooden chair',
    J(heading('Your kitchen, brushed by hand', 2),
      para('Most kitchen doors are solid enough to outlive three colour schemes. We degrease, key and prime them, then brush two coats of eggshell by hand in your kitchen. No doors go off to a spray shop, and you can still use the sink.'),
      para('Six to seven days for a normal Dublin kitchen. From €3,200 for up to 20 doors, drawer fronts included.'),
      buttons(('See the kitchens we have painted', '/category/kitchens/'))), width=50, align='wide', backgroundColor='mint', textColor=CHIP_TEXT['mint']))

pattern('kitchen-steps', 'Kitchen painting steps', 'services', J(
    heading('What happens to your kitchen', 3),
    lst(['Day 1: doors and drawers labelled, hinges bagged, everything degreased twice.',
         'Day 2: sanded, scuffs filled, primed with a bonding primer for laminate or oil primer for timber.',
         'Days 3 to 5: two coats of eggshell by brush, a light sand between them.',
         'Day 6: handles back on, doors rehung and lined up, touch-ups done.',
         'Day 7 (sometimes): the island, if it gets a different colour.'], ordered=True)))

pattern('kitchen-colours', 'Kitchen colours people chose this year', 'portfolio', J(
    heading('Kitchen colours this year', 3),
    chips([('hague', 'Hague Blue', 'F&amp;B No. 30', 'Glasnevin'),
           ('calke', 'Calke Green', 'F&amp;B No. 34', 'Cabra'),
           ('mint', 'Mint (mixed to match)', 'Colortrend match', 'Phibsborough'),
           ('sulking', 'Sulking Room Pink', 'F&amp;B No. 295', 'Stoneybatter')], min_width='9rem', short=True)))

pattern('kitchens-page', 'Page: hand-painted kitchens', 'services', J(
    pattern_ref('kitchen-intro'), pattern_ref('kitchen-steps'), pattern_ref('kitchen-colours'), pattern_ref('review-quotes')), block_types='core/post-content')

# ---------------------------------------------------------------- heritage
pattern('heritage-intro', 'Heritage and listed buildings', 'services', columns(
    ('45%', image('livingroom.jpg', 'Design drawing for a painted wall in pale mint green with white swags and borders', 'Design for painted wall decoration, about 1800. Cooper Hewitt collection.')),
    (None, J(heading('Old houses, old paint', 2),
             para('Half of Dublin 7 was built before 1900, and a lot of it is protected. We strip sashes back to the timber, re-putty the glass, and paint with linseed oil paint where the conservation officer asks for it.'),
             para('Anything painted before 1970 probably has lead in it. We test first, then wet-sand or use a heat gun at low temperature with extraction. No dry sanding, ever, and we tell you before we start.'),
             para('We have worked on protected structures in Blessington Street and on the North Circular Road. We can send references from both owners.'))),
    align='wide'))

pattern('lead-paint-note', 'Lead paint note', 'text', group(J(
    heading('Is there lead in my paint?', 4),
    para('If the house is older than 1970, assume yes until tested. The test kit costs €12 and we do it at the colour visit. If it is positive, the job takes about a day longer per room.')),
    className='is-style-card', backgroundColor='babouche', textColor=CHIP_TEXT['babouche']))

pattern('heritage-archive', 'Decorators before us (archive print)', 'about', media_text('ladder.jpg', 'An 18th-century engraving of a man on a ladder pasting a printed notice onto a wall, with a paste pot at the foot of the ladder',
    J(heading('People have been up ladders for a while', 3),
      para('Paris, 1742. A bill-sticker with a pot of paste, a brush and no dust sheets. We brought the dust sheets.', fontSize='small')),
    right=True, width=40, align='wide'))

pattern('heritage-page', 'Page: heritage', 'services', J(
    pattern_ref('heritage-intro'), pattern_ref('lead-paint-note'), pattern_ref('heritage-archive')), block_types='core/post-content')

# ---------------------------------------------------------------- outside
pattern('exterior-season', 'Notice: exterior season', 'banner', group(
    para('Outside work runs April to September. We are booking exteriors for spring now. Front doors can be done any dry week of the year.'),
    className='is-style-notice', align='full'),
    description='A bar for the header. Change the words for the season.')

pattern('front-doors', 'Front doors', 'services', columns(
    ('40%', image('frontdoor.jpg', 'A green six-panel Georgian front door with a brass knocker, set between white columns in a brick wall')),
    (None, J(heading('Paint the door', 2, fontSize='xx-large'),
             para('The front door is the one thing on the street you get to choose. We strip, fill and prime, then lay off two coats of exterior eggshell so there are no brush marks under the knocker. One day if it is dry, two if it is Dublin.'),
             chips([('calke', 'Calke Green', 'No. 34'), ('accent', 'Bamboozle', 'No. 304'), ('door-blue', 'Door blue', 'Mixed'), ('babouche', 'Babouche', 'No. 223')], min_width='7rem', short=True),
             para('From €480, both sides, brass taken off and polished.', fontSize='small'))),
    align='wide', verticalAlignment='center'))

pattern('outside-page', 'Page: outside', 'services', J(
    pattern_ref('front-doors'),
    heading('Render, railings and windows', 3),
    para('Masonry paint on render and pebbledash up to three storeys, from a tower scaffold. Railings wire-brushed and painted in two coats of metal paint. Timber windows scraped, primed and painted in oil, never in masonry paint.'),
    image('sash.jpg', 'A cream-rendered thatched cottage with a white sash window and dark green sills', 'A cottage in Skerries: limewash walls, green sills, the sash in white oil paint.')), block_types='core/post-content')

# ---------------------------------------------------------------- areas
AREAS = ['Stoneybatter', 'Phibsborough', 'Cabra', 'Smithfield', 'Glasnevin', 'Drumcondra', 'Arbour Hill', 'Grangegorman', 'Navan Road', 'Ashtown', 'Marino', 'Clontarf']
pattern('areas-list', 'Areas we cover', 'text', J(
    heading('Where we work', 2),
    para('We start from our lock-up off Prussia Street, so north of the Liffey is quickest. We cover:'),
    lst(AREAS, className='is-style-inline-list'),
    para('South of the canal we only take kitchens and heritage work, because we lose an hour a day in traffic and you would pay for it.', fontSize='small')))

pattern('area-note', 'Area note (one neighbourhood)', 'text', group(J(
    heading('Stoneybatter', 3),
    para('Red-brick artisan cottages, mostly two rooms up and two down. Front doors are small, sashes are original about half the time, and parking is on the street with a permit. We have painted 41 houses here since 2012 and still get lost in the Manor Street back lanes.')),
    className='is-style-card'))

pattern('areas-page', 'Page: areas', 'text', J(pattern_ref('areas-list'), pattern_ref('area-note')), block_types='core/post-content')

# ---------------------------------------------------------------- reviews, quote, contact
pattern('review-quotes', 'Reviews from named customers', 'testimonials', columns(
    (None, quote('They talked us out of grey and into Hague Blue. Every visitor now asks about the kitchen before they ask how we are.', 'Niamh and Pádraig, kitchen in Glasnevin, March 2026')),
    (None, quote('Tunde rehung twenty doors so straight my father-in-law checked them with a level. They were straight.', 'Olusegun, kitchen in Cabra, January 2026')),
    align='wide'))

pattern('quote-request', 'Ask for a quote (what to send)', 'call-to-action', group(J(
    heading('Ask for a quote', 2),
    para('Send three or four photos of each room, taken from the doorway, to <a href="mailto:%s">%s</a> or WhatsApp to %s. Tell us the rough size, what is wrong with it now, and when you would like it done.' % (EMAIL, EMAIL, PHONE)),
    para('We reply within two working days. For kitchens and old windows we will want to come and look.'),
    buttons(('Email your photos', 'mailto:%s?subject=Quote' % EMAIL), ('Call Aoife', 'tel:0875550142'))),
    backgroundColor='yellowcake', textColor=CHIP_TEXT['yellowcake'], className='is-style-card', align='wide', layout={'type': 'default'}))

pattern('contact-details', 'Contact details and hours', 'contact', columns(
    (None, J(heading('Ring, text or email', 2),
             para('<a href="tel:0875550142">%s</a><br><a href="mailto:%s">%s</a>' % (PHONE, EMAIL, EMAIL), fontSize='large'),
             para('Phones are answered 8am to 6pm, Monday to Friday. We are up ladders the rest of the time, so a text is quicker than a voicemail.'))),
    (None, J(heading('Lock-up', 3),
             para('Unit 6, Kirwan Street Yard<br>Stoneybatter, Dublin 7, D07 X2Y4'),
             para('This is where we keep the ladders, not an office. Paint collection by appointment, weekdays after 4:30pm.', fontSize='small'))),
    align='wide'))

pattern('contact-page', 'Page: contact', 'contact', J(pattern_ref('contact-details'), pattern_ref('quote-request'), pattern_ref('areas-list')), block_types='core/post-content')

pattern('colour-visit', 'Colour visit', 'services', columns(
    ('40%', image('brush.jpg', 'A worn paintbrush with white paint on its bristles and red paint on the handle, held against a pale wall')),
    (None, J(heading('Stuck on a colour?', 2),
             para('Book a colour visit. Aoife comes with the fan deck and a bag of sample pots, paints A3 boards and leaves them for you to look at in daylight and at night. €60, taken off the job if we paint it.'),
             para('She will be honest. If the north-facing room wants a warm white, she will say so, even though it is less fun.'),
             buttons(('Book a colour visit', 'mailto:%s?subject=Colour%%20visit' % EMAIL)))),
    align='wide', verticalAlignment='center'))

pattern('brochure-architects', 'For architects and designers (brochure)', 'services', J(
    heading('For architects and interior designers', 2),
    para('We work to a specification, keep to the paint schedule you issue, and photograph every room before handover. On heritage jobs we will attend the conservation officer\'s site visit.'),
    specs([('Crew', 'Two to four painters, all directly employed'),
           ('Insurance', 'Public liability €6.5m, employer\'s liability €13m'),
           ('Heritage', 'Linseed oil paint, lime wash, lead-safe prep'),
           ('Paperwork', 'Method statements and RAMS on request'),
           ('Lead time', 'Currently 5 weeks for interiors')]),
    buttons(('Email for our one-page PDF', 'mailto:%s?subject=Brochure' % EMAIL))))

pattern('architects-page', 'Page: for architects', 'services', J(pattern_ref('brochure-architects'), pattern_ref('insurance-line')), block_types='core/post-content')

pattern('holiday-colours', 'Colours stolen from holidays', 'portfolio', J(
    columns((None, image('exterior.jpg', 'A Greek harbour town of yellow, cream and terracotta houses climbing a hill above the sea', 'Symi, Greece. Aoife, August.')),
            (None, image('doorred.jpg', 'A small mint green house with a red door and red window bars under a blue sky', 'Isla Margarita. Tunde, February.')), align='wide'),
    para('Mint walls with a red door is now booked for a house in Marino. The Symi yellow is still waiting for someone brave.')))

# ---------------------------------------------------------------- round 2 patterns
pattern('hero-job', 'Hero: one finished job, large, with its colours', 'hero', columns(
    ('60%', image('decorator.jpg', 'A room painted deep orange with black panels, wicker chairs and a desk', 'Sitting room in Drumcondra, finished in July.')),
    (None, J(heading('This month: an orange sitting room in Drumcondra', 1, fontSize='xx-large'),
             chips([('locks', 'Charlotte\'s Locks', 'No. 268', 'Walls'), ('contrast', 'Railings', 'No. 31', 'Panels')], min_width='7rem', short=True),
             para('Three coats of orange, because oranges cover badly. Four days, €1,450.'),
             buttons(('See the whole job', '/orange-sitting-room-with-black-panels-drumcondra/')))),
    align='wide', verticalAlignment='center'), description='An alternative opening: the latest finished job, big, with its colour chips beside it.')

pattern('prices-teaser', 'Prices at a glance (three chips and a link)', 'prices', group(J(
    row(J(heading('Roughly what it costs', 2), para('<a href="/prices/">Full price list</a>', fontSize='small')), justify='space-between', align='wide'),
    grid(J(
        stack(J(para('Box room', fontFamily='display', fontSize='large'), para('from €650', fontFamily='display', fontSize='x-large'), para('2 days, walls and ceiling', fontSize='small')), className='is-style-card', backgroundColor='mint', textColor=CHIP_TEXT['mint']),
        stack(J(para('Front door', fontFamily='display', fontSize='large'), para('from €480', fontFamily='display', fontSize='x-large'), para('Both sides, brass polished', fontSize='small')), className='is-style-card', backgroundColor='yellowcake', textColor=CHIP_TEXT['yellowcake']),
        stack(J(para('Hand-painted kitchen', fontFamily='display', fontSize='large'), para('from €3,200', fontFamily='display', fontSize='x-large'), para('Up to 20 doors, brushed on site', fontSize='small')), className='is-style-card', backgroundColor='plaster', textColor=CHIP_TEXT['plaster'])),
        min_width='15rem', align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'}),
    para('Prices include paint, prep and VAT.', align='wide', fontSize='small')),
    align='wide', layout={'type': 'default'}), description='Three headline prices as cards, linking to the full list. Use this on the home page instead of the price table.')

pattern('guarantee', 'Two-year guarantee', 'about', group(J(
    heading('If it peels, we come back', 3),
    para('Two years on interior work and one year outside. If paint lifts, cracks or flakes because of how we prepared or painted it, we fix it free. Knocks from a hoover are not covered, but we will touch them up for the cost of a visit.')),
    className='is-style-card', backgroundColor='arsenic', textColor=CHIP_TEXT['arsenic']))

pattern('faq', 'Questions people ask before booking', 'text', J(
    heading('Questions people ask', 2),
    details('Do we need to move out?', para('No. We do one room at a time and put it back before we start the next. Kitchens are the exception: you will cook on a camping stove for about a week, or eat out.')),
    details('How long does the smell last?', para('A day with the windows open. We use water-based paint indoors unless an old surface needs oil.')),
    details('Do you supply the paint?', para('Yes, at trade price, and it is in the quote. If you already have tins, we will use them.')),
    details('Do you take a deposit?', para('Only for kitchens and jobs over €3,000: 20% to book the dates, the rest when we finish.')),
    details('Can the dog stay?', para('Of course. Wet paint and tails don\'t mix, so we will ask you to keep doors shut.'))))

pattern('job-gallery', 'Job details gallery (lightbox)', 'gallery', J(
    heading('Close up', 3),
    gallery([('brush.jpg', 'A worn paintbrush with white paint on the bristles held against a pale wall', 'Cutting in by hand'),
             ('frontdoor.jpg', 'A green six-panel front door with a brass knocker between white columns', 'Laid-off eggshell, no brush marks'),
             ('sash.jpg', 'A white sash window with dark green sills in a cream wall', 'Oil paint on an old sash')], columns=3, align='wide')),
    description='Three detail photos from one job. Click any to see it large.')

pattern('wallpaper', 'Wallpaper hanging', 'services', media_text('hero.jpg', 'A front room papered in a red trellis print with green curtains and a dark wood fireplace',
    J(heading('Wallpaper', 3),
      para('Marek hangs paper: lining paper, plain, patterned and the odd hand-printed roll that costs more than the rest of the room. Patterned paper is quoted per roll, from €38 a roll to hang.'),
      para('Tell us the repeat before you buy. A 53 cm repeat wastes about one roll in four.', fontSize='small')),
    width=45, align='wide'))

pattern('booking-now', 'How far ahead we are booking', 'banner', group(J(
    heading('Booking now', 4),
    chips([('mint', 'Interiors', '5 weeks ahead'), ('yellowcake', 'Kitchens', '7 weeks ahead'), ('sulking', 'Outside', 'from April'), ('babouche', 'Front doors', 'any dry week')], min_width='8rem', short=True)),
    align='wide', layout={'type': 'default'}), description='Current lead times as chips. Change them as the diary fills.')

pattern('job-quote', 'One customer quote for a job page', 'testimonials', quote('Aoife held a sample board against the wall at nine at night to prove the orange would still look right with the lamps on. It does.', 'Gráinne, sitting room in Drumcondra, July 2026'))

pattern('jobs-by-type', 'Jobs by type (links as chips)', 'portfolio', group(J(
    heading('Look through jobs by type', 3),
    grid(J(*[stack(J(para('<a href="/category/%s/">%s</a>' % (slug, name), fontFamily='display', fontSize='large'), para(note, fontSize='small')), className='is-style-chip-short', backgroundColor=c, textColor=CHIP_TEXT[c])
            for slug, name, note, c in [('interiors', 'Interiors', 'Rooms, halls and stairs', 'mint'), ('kitchens', 'Kitchens', 'Brushed on site', 'hague'),
                                        ('heritage', 'Heritage', 'Old houses, oil paint', 'accent'), ('outside', 'Outside', 'Doors, render, railings', 'calke'),
                                        ('notes', 'Colour notes', 'Colours we stole', 'yellowcake')]]), min_width='10rem', layout={'type': 'grid', 'columnCount': 5, 'minimumColumnWidth': '9rem'})),
    layout={'type': 'default'}))


print('patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

# ---------------------------------------------------------------- parts
STRIPE = group(J(*[group('', backgroundColor=c, layout=None) for c in ['calke', 'locks', 'yellowcake', 'hague', 'sulking', 'arsenic', 'accent', 'babouche', 'door-blue', 'mint']]),
               layout={'type': 'flex', 'flexWrap': 'nowrap'}, align='full', className='is-style-stripe')

write('parts/header.html', group(J(
    pattern_ref('exterior-season'),
    STRIPE,
    group(J(
        row(J(dyn('site-title', level=0), para('Painters and decorators, Dublin 7', fontSize='x-small')), wrap=True, style={'spacing': {'blockGap': 'var:preset|spacing|30'}}),
        dyn('navigation', overlayBackgroundColor='yellowcake', overlayTextColor='contrast', layout={'type': 'flex', 'justifyContent': 'right'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
        align='wide', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'})),
    tag='header', align='full', layout={'type': 'constrained'}, className='is-style-site-header', style={'spacing': {'blockGap': 'var:preset|spacing|30'}}))

write('parts/notice.html', pattern_ref('exterior-season'))

write('parts/footer.html', group(J(
    heading('Paint the door.', 2, align='wide', fontSize='display'),
    columns(
        ('40%', J(para('Two Coats, painters and decorators. Interiors, front doors, hand-painted kitchens and old windows in Dublin 7 and around.', fontSize='small'))),
        (None, J(heading('Call or text', 6), para('<a href="tel:0875550142">%s</a><br><a href="mailto:%s">%s</a><br>Mon to Fri, 8am to 6pm' % (PHONE, EMAIL, EMAIL), fontSize='small'))),
        (None, J(heading('Lock-up', 6), para('Unit 6, Kirwan Street Yard<br>Stoneybatter, Dublin 7<br>Visits by appointment', fontSize='small'))),
        (None, J(heading('Also', 6), para('<a href="/outside/">Outside work</a><br><a href="/for-architects/">For architects</a><br><a href="https://www.instagram.com/">Instagram, mostly doors</a>', fontSize='small'))),
        align='wide'),
    para('Demo photos are public domain or CC0 images from Wikimedia Commons and museum collections, used as stand-ins. Paint names belong to their makers.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-site-footer'))

# ---------------------------------------------------------------- templates
MAIN_PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero-colour-chart'),
    pattern_ref('recent-jobs'),
    group(J(pattern_ref('prices-teaser'), pattern_ref('booking-now')), align='full', backgroundColor='surface', className='is-style-band', layout={'type': 'constrained'}),
    group(pattern_ref('kitchen-intro'), align='full', layout={'type': 'constrained'}, className='is-style-pad-lg'),
    group(pattern_ref('team'), align='wide', layout={'type': 'default'}, className='is-style-pad-lg'),
    group(pattern_ref('review-quotes'), align='full', backgroundColor='sulking', className='is-style-band', layout={'type': 'constrained'}),
    group(J(pattern_ref('jobs-by-type'), pattern_ref('quote-request')), align='wide', layout={'type': 'default'}, className='is-style-pad-lg')),
    layout={'type': 'constrained'}, style={'spacing': {'blockGap': '0'}}))

write('templates/home.html', page_template(J(
    heading('Jobs', 1, align='wide'),
    para('Every job we photograph goes here, with the colours we used. Filter by type:', align='wide'),
    dyn('categories', className='is-style-inline-list', align='wide'),
    spacer('var:preset|spacing|40'),
    pattern_ref('jobs-archive')), className='is-style-page-main'))

write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide'),
    dyn('term-description', align='wide'),
    dyn('categories', className='is-style-inline-list', align='wide'),
    spacer('var:preset|spacing|40'),
    pattern_ref('jobs-archive')), className='is-style-page-main'))

write('templates/index.html', page_template(J(
    dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), className='is-style-page-main'))

write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Kitchen, sash, Hague Blue', buttonText='Search'),
    pattern_ref('post-list')), className='is-style-page-main'))

write('templates/404.html', page_template(J(
    heading('Missed a bit', 1),
    para('That page is not here. It may have been painted over. Try the <a href="/jobs/">jobs</a>, or search for a colour or a street.'),
    dyn('search', label='Search', showLabel=False, placeholder='Kitchen, sash, Hague Blue', buttonText='Search')), className='is-style-page-main'))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1),
    dyn('post-content', layout={'type': 'constrained'})), className='is-style-page-main'))

write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1, align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})), className='is-style-page-main'))

SINGLE = J(
    group(J(dyn('post-terms', term='category', separator=' / '), dyn('post-title', level=1, fontSize='xx-large')), align='wide', layout={'type': 'default'}),
    dyn('post-featured-image', align='wide', aspectRatio='16/9'),
    dyn('post-content', align='wide', layout={'type': 'constrained'}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous job', showTitle=True), dyn('post-navigation-link', label='Next job', showTitle=True)),
          align='wide', layout={'type': 'flex', 'justifyContent': 'space-between'}, className='is-style-rule-top'))
write('templates/single.html', page_template(SINGLE, className='is-style-page-main'))
write('templates/single-job.html', page_template(SINGLE, className='is-style-page-main'))
pattern_categories([('hero', 'Hero'), ('prices', 'Prices')])
print('theme written')

# ---------------------------------------------------------------- demo content
QUOTES = [('They sent a photo every evening, including the evening the dog walked through the primer.', 'Emer, Prussia Street, September 2026'),
          ('Marek matched the pattern round the chimney breast so well I can\'t find the join.', 'Lucy, Oxmantown Road, August 2026'),
          ('The kitchen looks like we bought a new one, and we still have the money.', 'Declan and Joy, Cabra, July 2026'),
          ('Aoife held a sample board up at nine at night to prove the orange worked by lamplight.', 'Gráinne, Drumcondra, July 2026'),
          ('The conservation officer asked who did the putty. We gave her Aoife\'s number.', 'Muireann, Glasnevin, June 2026'),
          ('Worth the drive out, they said. We agree.', 'Seán, Skerries, June 2026'),
          ('Our yard doors are now the most photographed thing on Kirwan Street.', 'Pat, Kirwan Street, May 2026'),
          ('We came for the holiday photos and stayed for the colour visit.', 'Nadia, Marino, February 2026')]


def job(title, cat, img, chips_, facts, story, date):
    q = QUOTES[len(POSTS_BUILT)]
    POSTS_BUILT.append(title)
    body = J(para(story, fontSize='large'),
             heading('Colours on this job', 2, fontSize='x-large'),
             chips(chips_, min_width='9.5rem'),
             heading('What we did', 3),
             specs(facts),
             quote(q[0], q[1]),
             buttons(('Ask for a quote like this', '/contact/')))
    return {'title': title, 'category': cat, 'image': img, 'template': 'single-job', 'date': date, 'content': body}


POSTS_BUILT = []
POSTS = [
    job('Green front door, Prussia Street', 'outside', 'frontdoor.jpg',
        [('calke', 'Calke Green', 'F&amp;B No. 34', 'Door, exterior eggshell'), ('base', 'All White', 'F&amp;B No. 2005', 'Columns and fanlight frame'), ('contrast', 'Railings', 'F&amp;B No. 31', 'Railings, metal paint')],
        [('Before', 'Brown woodstain, peeling at the bottom rail'), ('Prep', 'Stripped to bare timber, filled, knotted, primed'), ('Time', '2 days, one painter'), ('Cost', '€560 with the railings')],
        'The owners wanted the door the colour of the one in the photo their grandmother kept. We never saw the photo, but we got close with Calke Green and a lot of squinting.', '2026-09-10'),
    job('Wallpapered front room, Oxmantown Road', 'interiors', 'hero.jpg',
        [('accent', 'Bamboozle', 'F&amp;B No. 304', 'Skirting and doors, eggshell'), ('calke', 'Calke Green', 'F&amp;B No. 34', 'Window shutters'), ('plaster', 'Setting Plaster', 'F&amp;B No. 231', 'Ceiling')],
        [('Paper', 'Customer\'s own, a red trellis print, 11 rolls'), ('Prep', 'Lining paper hung first, crossways'), ('Time', '6 days, two of us'), ('Cost', '€2,700 plus the paper')],
        'A patterned paper with a 53 cm repeat, which wastes about a roll in every four. Marek hung it. The red woodwork was the owner\'s idea and she was right.', '2026-08-22'),
    job('Mint kitchen with red trim, Cabra', 'kitchens', 'kitchen.jpg',
        [('mint', 'Mint', 'Colortrend match', 'Cabinets, eggshell, brushed'), ('accent', 'Bamboozle', 'F&amp;B No. 304', 'Window frame'), ('babouche', 'Babouche', 'F&amp;B No. 223', 'Inside the dresser')],
        [('Before', '1980s oak-effect laminate doors'), ('Prep', 'Degreased twice, keyed, bonding primer'), ('Time', '6 days'), ('Cost', '€2,900 for 16 doors and 6 drawers')],
        'Laminate doors can be painted if you prime them properly. These had 40 years of frying on them, so day one was mostly sugar soap and patience.', '2026-07-30'),
    job('Orange sitting room with black panels, Drumcondra', 'interiors', 'decorator.jpg',
        [('locks', 'Charlotte\'s Locks', 'F&amp;B No. 268', 'Walls'), ('contrast', 'Railings', 'F&amp;B No. 31', 'Panels and skirting'), ('plaster', 'Setting Plaster', 'F&amp;B No. 231', 'Ceiling')],
        [('Rooms', 'Sitting room, 4.2 × 5.1 m'), ('Coats', 'Three on the walls, oranges cover badly'), ('Time', '4 days'), ('Cost', '€1,450')],
        'The owner sent us a photo of a museum room and asked for that. Three coats of orange later, it looks like that, minus the rope barrier.', '2026-07-12'),
    job('Red drawing room and gothic windows, Glasnevin', 'heritage', 'stairs.jpg',
        [('accent', 'Bamboozle', 'F&amp;B No. 304', 'Walls, limewash-friendly emulsion'), ('plaster', 'Setting Plaster', 'F&amp;B No. 231', 'Window reveals'), ('stiffkey', 'Stiffkey Blue', 'F&amp;B No. 281', 'Inside the shutters')],
        [('Building', 'Protected structure, 1860s'), ('Windows', 'Three gothic sashes stripped and re-puttied'), ('Paint', 'Linseed oil paint on the timber'), ('Time', '3 weeks')],
        'The conservation officer came twice. The second visit was to look at the putty, which she said was fine, and which Aoife has mentioned every day since.', '2026-06-18'),
    job('Cottage, render and sash, Skerries', 'outside', 'sash.jpg',
        [('base', 'Limewash, white', 'Mixed on site', 'Walls, four coats'), ('calke', 'Calke Green', 'F&amp;B No. 34', 'Sills and door'), ('base', 'Pure white oil', 'Linseed paint', 'Sash window')],
        [('Walls', 'Lime render, so limewash, never masonry paint'), ('Time', '5 days in June'), ('Travel', 'Outside our area, so we charged mileage'), ('Cost', '€3,300')],
        'Outside our usual patch, but a thatched cottage does not come along often. Limewash goes on thin and looks awful for an hour, then dries perfectly.', '2026-06-02'),
    job('Blue steel yard doors, Kirwan Street', 'outside', 'door.jpg',
        [('door-blue', 'Door blue', 'Mixed to sample', 'Steel doors, two coats'), ('contrast', 'Railings', 'F&amp;B No. 31', 'Hinges and frame')],
        [('Surface', 'Galvanised steel'), ('Prep', 'Wire-brushed, T-washed, etch primer'), ('Time', '1 day'), ('Cost', '€420')],
        'Our own neighbour\'s yard doors. The blue was matched to a bottle top he gave us.', '2026-05-15'),
    job('Colours we stole from holidays', 'notes', 'exterior.jpg',
        [('yellowcake', 'Yellowcake', 'F&amp;B No. 279', 'Symi harbour yellow, near enough'), ('mint', 'Mint', 'Colortrend match', 'Isla Margarita walls'), ('accent', 'Bamboozle', 'F&amp;B No. 304', 'Isla Margarita door')],
        [('Photos', 'Aoife in Symi, Tunde on Isla Margarita'), ('Used so far', 'Mint and red, on a house in Marino')],
        'Every winter we each bring back one colour from somewhere warm and try to match it. Dublin light makes everything greyer, so we mix a shade brighter than the photo.', '2026-02-20'),
]

content = {
    'site': {'title': 'Two Coats', 'tagline': 'Painters and decorators in Dublin 7'},
    'categories': [{'slug': 'interiors', 'name': 'Interiors'}, {'slug': 'kitchens', 'name': 'Kitchens'},
                   {'slug': 'heritage', 'name': 'Heritage'}, {'slug': 'outside', 'name': 'Outside'}, {'slug': 'notes', 'name': 'Colour notes'}],
    'front_page': 'home', 'posts_page': 'jobs',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'jobs', 'title': 'Jobs', 'content': ''},
        {'slug': 'kitchens', 'title': 'Hand-painted kitchens', 'pattern': 'coat/kitchens-page', 'template': 'page-wide'},
        {'slug': 'heritage', 'title': 'Heritage', 'pattern': 'coat/heritage-page', 'template': 'page-wide'},
        {'slug': 'prices', 'title': 'Prices', 'pattern': 'coat/prices-page'},
        {'slug': 'how-we-work', 'title': 'How we work', 'pattern': 'coat/process-page', 'template': 'page-wide'},
        {'slug': 'areas', 'title': 'Areas', 'pattern': 'coat/areas-page'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'coat/contact-page', 'template': 'page-wide'},
        {'slug': 'outside', 'title': 'Outside', 'pattern': 'coat/outside-page', 'template': 'page-wide'},
        {'slug': 'for-architects', 'title': 'For architects', 'pattern': 'coat/architects-page'},
        {'slug': 'colour-visit', 'title': 'Colour visits', 'pattern': 'coat/colour-visit', 'template': 'page-wide'},
    ],
    'posts': POSTS,
    'nav': [{'label': 'Jobs', 'url': '/jobs/'}, {'label': 'Kitchens', 'url': '/kitchens/'}, {'label': 'Heritage', 'url': '/heritage/'},
            {'label': 'Prices', 'url': '/prices/'}, {'label': 'How we work', 'url': '/how-we-work/'}, {'label': 'Areas', 'url': '/areas/'},
            {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/coat', exist_ok=True)
with open('demos/coat/content.json', 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
with open('demos/coat/fonts-claim.txt', 'w') as f:
    f.write('display: Rowdies\n')
print('demo written')
