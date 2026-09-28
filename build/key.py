# key: Nowicki, ślusarz, a locksmith in Wrocław (idea 105, as researched).
# Direction: public-information utility. A locked-out person on a phone at night needs the number, the price and proof
#   that this is a real, insured locksmith, in that order, so the site borrows the plainness of government service pages.
# Fonts: Ruda (display, registry face, heavy for the phone number and titles) and Atkinson Hyperlegible Next (body,
#   designed for low-vision readers). Both with latin-ext for Polish.
# Palette: white, near-black #0B0C0C, link blue accent, key-cutting yellow #FFDD00 (signal) for the call bar and focus, light grey surface,
#   brass #8A6A36 for the credentials row only.
# Layout idea: one 70ch column, no hero image; a yellow call bar with the phone number and the insurance line in the
#   header (sticky on mobile, the only sticky thing); prices and arrival times as plain tables.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('key')
S = 'key'
D = THEME['dir']

PALETTE = [
    ('base', '#FFFFFF', 'White'),
    ('contrast', '#0B0C0C', 'Black'),
    ('signal', '#FFDD00', 'Key-cutting yellow'),
    ('surface', '#F3F2F1', 'Light grey'),
    ('line', '#0B0C0C', 'Rule'),
    ('muted', '#505A5F', 'Secondary text'),
    ('brass', '#8A6A36', 'Brass'),
    ('accent', '#1D5AA0', 'Link blue'),
]
LATIN = 'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD'
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    for ff in f['fontFace']:
        ff.setdefault('unicodeRange', LATIN)
PAD = lambda t, b: {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1100px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Small print', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.3rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.25rem', 'name': 'Title', 'fluid': {'min': '2.25rem', 'max': '3.25rem'}},
                {'slug': 'display', 'size': '7.5rem', 'name': 'Phone number', 'fluid': {'min': '3.1rem', 'max': '7.5rem'}},
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
        'shadow': {'defaultPresets': False, 'presets': [{'slug': 'button', 'name': 'Button base', 'shadow': '0 3px 0 0 var(--wp--preset--color--contrast)'}]},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True,
                   'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}]},
        'custom': {'measure': '70ch'},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '1.1'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '900'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700'}},
            'button': {
                'color': {'background': 'var:preset|color|signal', 'text': 'var:preset|color|contrast'},
                'border': {'radius': '0', 'width': '0'},
                'shadow': 'var:preset|shadow|button',
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|medium'},
                'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '1em', 'right': '1em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|signal'}},
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|large'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'}}}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'border': {'left': {'color': 'var:preset|color|contrast', 'width': '5px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                           'typography': {'fontSize': 'var:preset|font-size|medium', 'fontStyle': 'normal'}},
            'core/table': {'css': '&{font-variant-numeric:tabular-nums}& th{text-align:left;font-weight:700;border-width:0 0 2px 0!important;border-color:var(--wp--preset--color--contrast)}& td{border-width:0 0 1px 0!important;border-color:var(--wp--preset--color--muted);padding:.6em .5em .6em 0;vertical-align:top}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|muted', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-weight:700;color:var(--wp--preset--color--link);text-decoration:underline;cursor:pointer}'},
            'core/search': {'css': '& .wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0}'},
            'core/list': {'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
        },
        'css': '.wp-block-post-content > * + :is(h2,h3,.wp-block-columns,.wp-block-group,.wp-block-image,.wp-block-table){margin-block-start:var(--wp--preset--spacing--60)}'
               ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none}'
               'a:focus-visible,summary:focus-visible,button:focus-visible,input:focus-visible,.wp-element-button:focus-visible{outline:3px solid transparent;background-color:var(--wp--preset--color--signal)!important;color:var(--wp--preset--color--contrast)!important;box-shadow:0 -2px var(--wp--preset--color--signal),0 4px var(--wp--preset--color--contrast);text-decoration:none}'
               '@media (max-width:781px){.call-bar-part{position:sticky;top:0;z-index:20}}'
               '.phone-big{font-weight:800;line-height:1}.phone-big a{color:var(--wp--preset--color--contrast);text-decoration:none;font-variant-numeric:tabular-nums}.phone-big a:hover{text-decoration:underline}',
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'uncategorized', 'name': 'call-bar', 'title': 'Call bar'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}

# ---------------------------------------------------------------- round 2: lightbox, spec rows, pattern categories
R2_CSS = ('.is-style-specs > .wp-block-group{padding-block:.55em;border-bottom:1px solid var(--wp--preset--color--line);gap:.2rem 1.25rem!important;margin:0!important}'
          '.is-style-specs > .wp-block-group > :first-child{flex:0 0 min(36%,12rem);font-weight:600;margin:0}'
          '.is-style-specs > .wp-block-group > :last-child{flex:1 1 14rem;margin:0}')
theme['settings']['blocks'] = {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}}
theme['styles']['css'] += R2_CSS


def specs(pairs, **attrs):
    """Label and value rows made from groups, instead of a two-column table."""
    return group(J(*[row(J(para(k), para(v))) for k, v in pairs]), className='is-style-specs', layout={'type': 'default'}, **attrs)


def pattern_categories(cats):
    lines = ["<?php", "/**", " * Registers this theme's block pattern categories. Nothing else.", " */", "add_action( 'init', function () {"]
    for slug, label in cats:
        lines.append("\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', '%s' ) ) );" % (slug, label, THEME['slug']))
    lines.append('} );')
    write('functions.php', '\n'.join(lines))

theme['styles']['css'] += ('.is-style-leaders{list-style:none;padding-left:0}.is-style-leaders li{display:flex;align-items:baseline;gap:.4em;padding:.5em 0;border-bottom:1px solid var(--wp--preset--color--muted)}'
                           '.is-style-leaders li strong{order:2;white-space:nowrap;font-variant-numeric:tabular-nums}'
                           '.is-style-leaders li::after{content:"";order:1;flex:1 1 1.5rem;border-bottom:2px dotted var(--wp--preset--color--contrast);transform:translateY(-.3em)}')


def leaders(items, **attrs):
    return lst(['%s <strong>%s</strong>' % (a, b) for a, b in items], className='is-style-leaders', **attrs)


with open(os.path.join(D, 'theme.json'), 'w') as f:
    json.dump(theme, f, indent='\t', ensure_ascii=False)

write('style.css', '''/*
Theme Name: Key
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A plain, fast theme for independent locksmiths, with the phone number, insurance and prices where a locked-out caller looks first.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: key
Tags: blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, one-column, accessibility-ready
*/''')


def variation(name, title, changes):
    pal = [(s, changes.get(s, c), n) for s, c, n in PALETTE]
    write('styles/%s.json' % name, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                               'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}, indent='\t', ensure_ascii=False))


variation('night-call', 'Night call', {'base': '#0B0C0C', 'contrast': '#FFDD00', 'signal': '#FFDD00', 'surface': '#1E1F1F', 'line': '#FFDD00', 'muted': '#D6D3C4', 'accent': '#FFFFFF', 'brass': '#D2B27A'})
variation('brass', 'Brass', {'signal': '#E9C46A', 'surface': '#F6F1E7', 'brass': '#7A5C2A'})
variation('steel', 'Steel', {'base': '#D9DCDF', 'surface': '#EEF0F2', 'muted': '#3E474C', 'accent': '#12457F'})


def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))


section('call-bar', 'Call bar', ['core/group'], {
    'color': {'background': 'var:preset|color|signal', 'text': 'var:preset|color|contrast'},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}},
    'spacing': {'padding': PAD(20, 20)},
    'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}},
})
section('site-header', 'Site header', ['core/group'], {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                                                     'elements': {'link': {'color': {'text': 'var:preset|color|base'}}},
                                                     'spacing': {'padding': PAD(30, 30)}})
section('site-footer', 'Site footer', ['core/group'], {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
                                                     'border': {'top': {'color': 'var:preset|color|signal', 'width': '10px', 'style': 'solid'}},
                                                     'spacing': {'padding': PAD(60, 50)}})
section('page-main', 'Page body', ['core/group'], {'spacing': {'padding': PAD(50, 70)}})
section('pad-lg', 'Roomy section', ['core/group'], {'spacing': {'padding': PAD(60, 60)}})
section('inset', 'Inset text', ['core/group'], {'border': {'left': {'color': 'var:preset|color|muted', 'width': '10px', 'style': 'solid'}},
                                              'spacing': {'padding': {'left': 'var:preset|spacing|40', 'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}})
section('warning', 'Warning panel', ['core/group'], {'border': {'width': '5px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                                                   'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('credentials', 'Credentials row', ['core/group', 'core/columns'], {'border': {'top': {'color': 'var:preset|color|brass', 'width': '3px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|brass', 'width': '3px', 'style': 'solid'}},
                                                                         'spacing': {'padding': PAD(30, 30)}, 'typography': {'fontSize': 'var:preset|font-size|small'}})
section('rule-top', 'Rule above', ['core/group'], {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})

PHONE = '698 000 412'
TEL = 'tel:+48698000412'
EMAIL = 'slusarz@example.com'
INSURE = 'Insured: OC liability cover 500,000 zł with PZU. Master locksmith\'s certificate, Wrocław Chamber of Crafts, no. 1187/2009.'


def call(label='Call %s' % PHONE):
    return buttons((label, TEL))


# ---------------------------------------------------------------- patterns
pattern('call-bar', 'Call bar with insurance line', 'banner', group(J(
    row(J(para('<strong>Locked out? Call <a href="%s">%s</a></strong>, day and night' % (TEL, PHONE), fontSize='medium'),
          para(INSURE, fontSize='x-small')), justify='space-between', align='wide')),
    align='full', className='is-style-call-bar', layout={'type': 'constrained'}),
    description='The signature: phone number with the insurance and certificate line right next to it, so a caller sees proof before calling. Sticky on phones.')

pattern('big-phone', 'Giant tap-to-call number', 'call-to-action', J(
    heading('Locked out in Wrocław?', 1),
    para('<a href="%s">%s</a>' % (TEL, PHONE), fontFamily='display', fontSize='display', className='phone-big'),
    para('Usually with you in 20 to 40 minutes. Opening a door without damage costs 200 zł in the day and 350 zł at night, and I tell you the price on the phone before I set off. English and Polish.', fontSize='large')))

pattern('before-you-call', 'Before you call', 'text', group(J(
    heading('Have these ready', 2),
    lst(['The full address, with the gate or intercom code if there is one.',
         'Photo ID. I need to see that you live there before I open the door, or a rental agreement with your name on it.',
         'The make of the lock if you can see it, for example Gerda or Lob. It is printed on the cylinder.']),
    para('If there is a child or a pet alone inside, or a pan on the stove, call 112 first. Firefighters open doors too.')),
    className='is-style-warning'))

SERVICES = [
    ('Opening a door without damage, 7:00 to 20:00', '200 zł'),
    ('Opening a door without damage, 20:00 to 7:00', '350 zł'),
    ('Sundays and public holidays', '+100 zł'),
    ('New cylinder, class B, fitted', 'from 180 zł'),
    ('New cylinder, class C, fitted', 'from 320 zł'),
    ('uPVC door or window mechanism repaired', 'from 250 zł'),
    ('Boarding up after a break-in', 'from 300 zł'),
    ('Lock change between tenants, per door', 'from 220 zł'),
    ('Key cut while you wait (at the workshop)', 'from 15 zł'),
]
pattern('price-table', 'Typical prices (table)', 'prices', J(
    heading('Typical prices', 2),
    table([list(x) for x in SERVICES], head=['Job', 'Price']),
    para('Prices include getting to you anywhere in Wrocław, and VAT. Parts are extra only where it says "from". If someone quotes you "from 49 zł" on the phone, ask what the final bill will be. The Wrocław average for a daytime lockout is about 200 to 250 zł.', fontSize='small')))

pattern('services-list', 'Services (plain list)', 'services', J(
    heading('What I do', 2),
    lst(['<a href="/lockouts/">Lockouts</a>: opening doors without damage, day and night.',
         '<a href="/lock-changes/">Lock changes</a>: new cylinders and locks, including class C cylinders for insurers.',
         '<a href="/upvc-repairs/">uPVC doors and windows</a>: handles, gearboxes and multi-point locks that have stopped working.',
         '<a href="/burglary-repairs/">After a break-in</a>: boarding up, new locks and a written note for the police and your insurer.',
         '<a href="/landlords/">Landlords and agents</a>: lock changes between tenants and key records.']),
    para('I don\'t open cars, safes or post boxes. For a car, call the assistance number on your insurance.', fontSize='small')))

AREAS = [('Stare Miasto, Nadodrze, Ołbin', '15 to 25 min'), ('Śródmieście, Plac Grunwaldzki, Biskupin', '20 to 30 min'),
         ('Krzyki, Gaj, Borek, Huby', '25 to 35 min'), ('Fabryczna, Muchobór, Nowy Dwór', '30 to 40 min'),
         ('Psie Pole, Karłowice, Sołtysowice', '30 to 45 min'), ('Siechnice, Kiełczów, Smolec', 'about 45 min, +50 zł')]
pattern('areas-table', 'Areas and arrival times', 'text', J(
    heading('Where I cover, and how long it takes', 2),
    table([list(a) for a in AREAS], head=['Area', 'Usually there in']),
    para('Times are for calls between 7:00 and 20:00. At night it is often quicker, because the roads are empty.', fontSize='small')))

pattern('real-locksmith', 'Is this really your locksmith?', 'text', group(J(
    heading('How to know it is me at your door', 2),
    para('I drive a white Ford Transit Connect with NOWICKI ŚLUSARZ and %s on both sides, registration DW 4K118. I am 51, grey-haired and usually in a navy fleece. I will show you my ID before I touch the lock.' % PHONE),
    para('If someone arrives in an unmarked car and says they are from me, they are not. Don\'t let them start, and call me.')),
    className='is-style-inset'))

pattern('credentials-row', 'Credentials row', 'about', columns(
    (None, J(heading('Master locksmith', 6), para('Certificate no. 1187/2009, Wrocław Chamber of Crafts'))),
    (None, J(heading('Insured', 6), para('OC liability cover 500,000 zł, PZU, renewed every March'))),
    (None, J(heading('Registered business', 6), para('Krzysztof Nowicki, NIP 897-000-41-12'))),
    (None, J(heading('Receipts', 6), para('A VAT invoice or receipt for every job, card or cash'))),
    className='is-style-credentials', align='wide'))

pattern('landlords', 'Landlords and letting agents', 'services', J(
    heading('For landlords and letting agents', 2),
    para('Between tenants I change the cylinders on every door, cut the number of keys you ask for and send you a key record: which key opens what, and how many copies exist. Same week for most flats in Wrocław.'),
    leaders([('Cylinder change, per door, class B', '220 zł'), ('Extra keys, per key', '15 zł'), ('Key record and invoice to the agency', 'included')]),
    group(J(heading('Evictions', 4), para('I only open a door for an eviction when a bailiff (komornik) is present with the court order. Please don\'t ask me to do it otherwise.')), className='is-style-inset')))

pattern('burglary', 'After a break-in', 'services', J(
    heading('After a break-in', 2),
    lst(['Call the police on 112 and get the incident number.',
         'Call me. I can board up a door or window the same night and fit a new cylinder the next morning.',
         'I write a short note of the damage and the work done, with photos, for your insurer.'], ordered=True),
    para('Boarding up from 300 zł. New class C cylinder from 320 zł fitted.')))

pattern('cylinder-advice', 'Cylinder classes, explained', 'text', J(
    heading('Which cylinder do I need?', 2),
    columns((None, J(heading('Class A', 4), para('Cheapest. Easy to pick. Fine for an internal door.'))),
            (None, J(heading('Class B', 4), para('The usual front-door cylinder in Wrocław flats. Most insurers accept it.'))),
            (None, J(heading('Class C', 4), para('Resists picking and drilling for longer. Some insurers ask for it for houses and ground-floor flats.'))), className='is-style-credentials'),
    para('A cylinder that sticks out more than 3 mm from the door furniture can be snapped. That is how most break-ins through front doors happen here. I check this for free when I am there for something else.')))

pattern('upvc', 'uPVC doors and windows', 'services', J(
    heading('uPVC doors and windows', 2),
    para('If the handle goes down but the door won\'t lock, the gearbox inside the door is usually worn. I carry the common Roto, Winkhaus and GU gearboxes in the van and fit them in about an hour.'),
    media_text('mortise.jpg', 'The inside of an old iron mortise lock with its levers and springs exposed', para('Locks haven\'t changed much in 300 years. This one is in the Metropolitan Museum.', fontSize='small'), width=40)))

pattern('lock-changes', 'Lock changes', 'services', J(
    heading('Lost keys, new flat, or an ex with a key', 2),
    para('A cylinder change takes 15 minutes per door. I bring class B and class C cylinders from Gerda and Lob in the common sizes. For unusual doors I measure first and come back the next day.'),
    image('euro.jpg', 'A brass pin tumbler lock cylinder with a key partly inserted', 'A cheap cylinder after being picked in under a minute.')))

pattern('contact-details', 'Contact details', 'contact', J(
    heading('Ring any time', 2),
    para('<a href="%s">%s</a>' % (TEL, PHONE), fontFamily='display', fontSize='xx-large', className='phone-big'),
    para('For non-urgent jobs, email <a href="mailto:%s">%s</a> or send a text. I reply the same day.' % (EMAIL, EMAIL)),
    heading('Workshop', 3),
    para('ul. Jedności Narodowej 71, Wrocław (Nadodrze), in the courtyard.<br>Key cutting Monday to Friday 9:00 to 17:00, Saturday 9:00 to 13:00.'),
    para('The workshop is closed while I am out on a call. Ring before you come for keys.', fontSize='small')))

pattern('advice-list', 'Security advice (latest posts)', 'posts,query', J(
    heading('Security advice', 2),
    query(J(dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-excerpt', moreText='')), per_page=4)))

pattern('post-list', 'Post list', 'posts,query', inherit_query(
    J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', moreText=''), dyn('post-terms', term='category')), className='is-style-default'), inserter=False)

pattern('no-callout-fee-note', 'Price on the phone note', 'text', group(para(
    'I tell you the full price on the phone before I set off. If the job turns out to be different when I get there, I tell you before I start, and you can say no and pay nothing.'),
    className='is-style-inset'))

pattern('workshop-hours', 'Workshop hours (key cutting)', 'text', J(
    heading('Workshop hours', 3),
    specs([('Monday to Friday', '9:00 to 17:00'), ('Saturday', '9:00 to 13:00'), ('Sunday', 'Closed, but I answer the phone for lockouts')]),
    para('Key cutting only. Lockouts are day and night, seven days a week.', fontSize='small')))

pattern('what-i-dont-do', 'What I don\'t do', 'text', group(J(
    heading('What I don\'t do', 3),
    lst(['Open cars. Call the assistance number on your car insurance.', 'Open safes or post boxes.', 'Open a door for someone who can\'t show they live there.', 'Evictions without a bailiff present.'])),
    className='is-style-inset'))

pattern('door-check', 'Free door check', 'call-to-action', group(J(
    heading('Free check while I am there', 3),
    para('On any job I will look at your front door and tell you, in two minutes, whether the cylinder can be snapped and whether the hinges or frame are the weak point. No charge and no hard sell.')),
    className='is-style-warning'))


# ---------------------------------------------------------------- round 2 patterns
pattern('price-list-short', 'Typical prices (short list)', 'prices', J(
    heading('What it usually costs', 2),
    leaders([('Door opened without damage, day', '200 zł'), ('Door opened without damage, night', '350 zł'), ('New cylinder, class B, fitted', 'from 180 zł'), ('uPVC mechanism repaired', 'from 250 zł')]),
    para('Getting to you in Wrocław and VAT included. <a href="/prices/">All prices</a>', fontSize='small')), description='Four prices with dotted leaders. For the home page; the full table lives on the prices page.')

pattern('areas-list', 'Areas and arrival times (list)', 'text', J(
    heading('How long until I am there', 2),
    leaders([(a, t) for a, t in AREAS[:4]]),
    para('<a href="/areas/">Every district and the night times</a>', fontSize='small')))

def job_report(where, happened, did, time, cost):
    return J(columns((None, J(heading('What happened', 4), para(happened))), (None, J(heading('What I did', 4), para(did))), className='is-style-credentials'),
             specs([('Where', where), ('Time on site', time), ('Cost', cost)]))

pattern('job-report', 'Job report: what happened, what I did, cost', 'posts', job_report(
    'Ołbin, third floor, tenement', 'Tenant locked out at 23:40 with the key inside, pan still on the hob.',
    'Opened the Gerda cylinder with a bypass tool in six minutes. No damage. Turned off the hob first.', '20 minutes', '350 zł, night rate'),
    description='The layout used for every job write-up in the Jobs category.')

pattern('right-now', 'Locked out right now: the next five minutes', 'text', group(J(
    heading('Locked out right now?', 2),
    lst(['Check every door and window you could open without breaking anything. Back doors and balcony doors are often only on the latch.',
         'If someone else has a key, ringing them is cheaper than ringing me.',
         'If not, call me. Tell me the address and what the lock looks like.',
         'Wait somewhere warm. I will ring when I am five minutes away.'], ordered=True)),
    className='is-style-warning'))

pattern('keys-we-cut', 'Keys I cut', 'services', columns(
    (None, J(heading('Flat and cylinder keys', 4), para('While you wait, from 15 zł.'))),
    (None, J(heading('Security keys with a card', 4), para('Bring the card. From 60 zł, two working days.'))),
    (None, J(heading('Old mortise keys', 4), para('Cut from a blank by hand, from 40 zł. Bring the lock if you have lost every key.'))),
    align='wide', className='is-style-credentials'))

pattern('night-rates', 'Why nights cost more', 'text', J(
    heading('Why nights cost more', 3),
    para('Between 20:00 and 7:00 I am the only one on call, and I get out of bed for it. That is the 150 zł difference. I tell you which rate applies before I set off.')))

pattern('lost-keys', 'Lost your keys?', 'text', J(
    heading('Lost your keys?', 3),
    para('If the keys had your address on them, or were in a bag with your ID, change the cylinder the same day. If they were lost somewhere with no clue to where you live, you have more time, but I would still change it within the week.'),
    para('A class B cylinder, fitted, is from 180 zł.', fontSize='small')))

pattern('testimonials', 'What customers say', 'testimonials', J(
    quote('Rang at 2am from the stairwell in my socks. He was there in fifteen minutes and told me the price before he picked up the tools.', 'Agnieszka, Nadodrze, March 2026'),
    quote('We manage 40 flats and Krzysztof has done the changeovers on all of them for six years. The key records alone save us a day a month.', 'Tomasz, letting agency, Krzyki, January 2026')))

pattern('payment', 'How to pay', 'text', specs([
    ('Card', 'Contactless in the van, any card'), ('BLIK', 'To my phone number'), ('Cash', 'Złoty only'), ('Invoice', 'VAT invoice for every job, emailed the same day')]))

pattern('insurer-note', 'A note for your insurer', 'services', group(J(
    heading('A note for your insurer', 4),
    para('After a break-in I write a one-page note: what was damaged, what I fitted, the cylinder class and photos before and after. Insurers in Poland usually ask for exactly this, and it is included in the price.')),
    className='is-style-inset'))

pattern('commercial', 'Shops and offices', 'services', J(
    heading('Shops and offices', 2),
    para('Master key systems for small offices, shutters that stick, and lock changes the evening someone leaves. I have looked after about thirty shops on Świdnicka and in the Rynek since 2012.'),
    buttons(('Email about a master key system', 'mailto:%s?subject=Master%%20key%%20system' % EMAIL))))

pattern('faq', 'Questions people ask', 'text', J(
    heading('Questions people ask', 2),
    details('Will you damage the door?', para('Almost never. I open about nine in ten doors with picks or bypass tools. If I have to drill, it is the cylinder, not the door, and I fit a new one.')),
    details('Do I need ID?', para('Yes. I need to see that you live there before I open anything. If your ID is inside, I open the door, then you show me.')),
    details('Can you come to Oleśnica?', para('Yes, with 50 zł for travel. Further than 30 km, ring and ask.')),
    details('Do you fit smart locks?', para('I fit them if you have bought one, but I would rather sell you a good class C cylinder. Batteries go flat at night too.'))))

pattern('call-strip', 'Call strip (phone and one line)', 'call-to-action', group(J(
    para('<a href="%s">%s</a>' % (TEL, PHONE), fontFamily='display', fontSize='xx-large', className='phone-big'),
    para('Day and night. The price on the phone before I set off.')),
    className='is-style-warning', layout={'type': 'default'}))

pattern('recent-jobs', 'Recent jobs (latest posts)', 'posts,query', J(
    heading('Recent jobs', 2),
    query(J(dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-excerpt', moreText='')), per_page=3),
    para('<a href="/category/jobs/">All job reports</a>', fontSize='small')))

# page patterns
pattern('lockouts-page', 'Page: lockouts', 'services', J(
    pattern_ref('right-now'),
    para('I open most front doors in Wrocław without damage in under ten minutes, using picks and bypass tools. If a lock can\'t be opened that way, I drill the cylinder and fit a new one, and you pay for the cylinder.', fontSize='large'),
    pattern_ref('before-you-call'), pattern_ref('no-callout-fee-note'), pattern_ref('price-table'), pattern_ref('night-rates'), pattern_ref('real-locksmith'), pattern_ref('faq')), block_types='core/post-content')
pattern('lock-changes-page', 'Page: lock changes', 'services', J(pattern_ref('lock-changes'), pattern_ref('lost-keys'), pattern_ref('cylinder-advice'), pattern_ref('keys-we-cut'), pattern_ref('door-check'), call()), block_types='core/post-content')
pattern('upvc-page', 'Page: uPVC repairs', 'services', J(pattern_ref('upvc'), call()), block_types='core/post-content')
pattern('landlords-page', 'Page: landlords', 'services', J(pattern_ref('landlords'), pattern_ref('commercial'), pattern_ref('credentials-row'), pattern_ref('testimonials')), block_types='core/post-content')
pattern('prices-page', 'Page: prices', 'services', J(pattern_ref('price-table'), pattern_ref('no-callout-fee-note'), pattern_ref('night-rates'), pattern_ref('payment'), pattern_ref('services-list'), pattern_ref('what-i-dont-do')), block_types='core/post-content')
pattern('areas-page', 'Page: areas', 'text', J(pattern_ref('areas-table'), image('wroclaw.jpg', 'A blue Wrocław tram at the Świdnicka stop at night, with street lamps behind', 'Świdnicka at night. After 22:00 I can usually be anywhere in the centre in 15 minutes.')), block_types='core/post-content')
pattern('burglary-page', 'Page: after a break-in', 'services', J(pattern_ref('burglary'), pattern_ref('insurer-note'), pattern_ref('call-strip')), block_types='core/post-content')
pattern('contact-page', 'Page: contact', 'contact', J(pattern_ref('contact-details'), pattern_ref('workshop-hours'), pattern_ref('payment'), pattern_ref('real-locksmith'), pattern_ref('credentials-row')), block_types='core/post-content')
print('patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

# ---------------------------------------------------------------- parts
write('parts/call-bar.html', pattern_ref('call-bar'))
write('parts/header.html', J(
    group(group(J(
        dyn('site-title', level=0),
        dyn('navigation', overlayBackgroundColor='contrast', overlayTextColor='base', layout={'type': 'flex', 'justifyContent': 'right'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
        align='wide', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}),
        tag='header', align='full', className='is-style-site-header', layout={'type': 'constrained'})))

write('parts/footer.html', group(J(
    columns(
        (None, J(para('Nowicki, ślusarz', fontFamily='display', fontSize='large'),
                 para('Locksmith in Wrocław. Lockouts, lock changes and uPVC repairs, day and night.', fontSize='small'))),
        (None, J(heading('Phone', 6), para('<a href="%s">%s</a>, day and night<br><a href="mailto:%s">%s</a>' % (TEL, PHONE, EMAIL, EMAIL), fontSize='small'))),
        (None, J(heading('Workshop', 6), para('ul. Jedności Narodowej 71, Wrocław<br>Keys Mon to Fri 9:00 to 17:00, Sat 9:00 to 13:00', fontSize='small'))),
        align='wide'),
    para(INSURE, align='wide', fontSize='x-small'),
    para('Demo photos are CC0 images from Wikimedia Commons and the Metropolitan Museum of Art, used as stand-ins.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-site-footer', layout={'type': 'constrained'}))

# ---------------------------------------------------------------- templates
def page_template(main_inner, **main_attrs):
    return J(dyn('template-part', slug='call-bar', className='call-bar-part'), template_part('header', 'header'), group(main_inner, tag='main', **main_attrs), template_part('footer', 'footer'))


M = {'className': 'is-style-page-main'}
write('templates/front-page.html', page_template(J(
    pattern_ref('big-phone'),
    pattern_ref('before-you-call'),
    pattern_ref('price-list-short'),
    pattern_ref('real-locksmith'),
    pattern_ref('credentials-row'),
    pattern_ref('services-list'),
    pattern_ref('areas-list'),
    pattern_ref('testimonials'),
    pattern_ref('recent-jobs')), className='is-style-page-main', style={'spacing': {'blockGap': 'var:preset|spacing|60'}}))
write('templates/home.html', page_template(J(heading('Jobs and advice', 1), para('Write-ups of recent jobs, and short practical notes. Nothing here is sponsored by a lock maker.'), dyn('categories'), pattern_ref('post-list')), **M))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False), dyn('term-description'), pattern_ref('post-list')), **M))
write('templates/index.html', page_template(J(dyn('query-title', type='archive'), pattern_ref('post-list')), **M))
write('templates/search.html', page_template(J(dyn('query-title', type='search'), dyn('search', label='Search', showLabel=False, placeholder='Cylinder, uPVC, lockout', buttonText='Search'), pattern_ref('post-list')), **M))
write('templates/404.html', page_template(J(heading('Page not found', 1), para('If you are locked out, you don\'t need this page. Call <a href="%s">%s</a>.' % (TEL, PHONE), fontSize='large'),
                                            dyn('search', label='Search', showLabel=False, placeholder='Cylinder, uPVC, lockout', buttonText='Search')), **M))
write('templates/page.html', page_template(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'})), **M))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1100px'})), **M))
write('templates/single.html', page_template(J(
    dyn('post-terms', term='category'), dyn('post-title', level=1), dyn('post-featured-image'), dyn('post-content', layout={'type': 'constrained'}),
    group(J(para('Locked out now? Call <a href="%s">%s</a>.' % (TEL, PHONE), fontSize='large')), className='is-style-rule-top', layout={'type': 'default'})), **M))
pattern_categories([('prices', 'Prices')])
print('theme written')

# ---------------------------------------------------------------- demo
def post(title, cat, img, excerpt, body, date):
    return {'title': title, 'category': cat, 'image': img, 'excerpt': excerpt, 'date': date, 'content': body}


POSTS = [
    post('Night lockout in Ołbin, pan on the hob', 'jobs', 'lock.jpg', 'Opened in six minutes at 23:40, no damage. The hob went off first.',
         J(para('The call came from a neighbour\'s phone: tenant locked out, keys inside, and a pan of potatoes on the hob. Ołbin, third floor, no lift.'),
           job_report('Ołbin, third floor, tenement', 'Tenant locked out at 23:40 with the key inside and the hob on.', 'Opened the Gerda cylinder with a bypass tool in six minutes. No damage. Hob off, potatoes saved.', '20 minutes', '350 zł, night rate')), '2026-09-24'),
    post('Cylinder change after a break-in, Krzyki', 'jobs', 'euro.jpg', 'A snapped cylinder, a boarded door overnight and a class C cylinder the next morning.',
         J(para('The burglars snapped the old cylinder, which stuck out 8 mm from the handle plate. The police were done by midnight and I boarded the door until morning.'),
           job_report('Krzyki, ground-floor flat', 'Front door forced overnight by snapping a class A cylinder.', 'Boarded up at 00:30. At 8:00 fitted a class C anti-snap cylinder and a new handle set, and wrote the note for the insurer.', '1 hour at night, 40 minutes in the morning', '300 zł boarding, 420 zł cylinder and handles')), '2026-09-02'),
    post('Twelve flats in a day, Nadodrze', 'jobs', 'keys.jpg', 'A block changing management company. New cylinders, 36 keys, one key record.',
         J(para('A housing co-operative changed its managing agent and wanted every flat door and the street door on new cylinders the same day.'),
           job_report('Nadodrze, a 1905 tenement with twelve flats', 'Change of managing agent. Nobody knew how many keys to the old locks were out there.', 'Twelve class B cylinders, a new street-door lock, 36 keys cut and a key record sent to the co-operative.', 'One long day', '3,100 zł including parts')), '2026-08-12'),
    post('A uPVC balcony door that would not lock, Fabryczna', 'jobs', 'padlock2.jpg', 'A worn gearbox, replaced in an hour. The door had been wedged shut with a chair for a month.',
         J(para('The handle went down, but the hooks never came out, so the balcony door had been held shut with a kitchen chair since July.'),
           job_report('Fabryczna, fourth-floor flat', 'Balcony door handle turned but the door would not lock.', 'Replaced the Winkhaus gearbox and adjusted the keeps. The chair went back to the kitchen.', '1 hour', '280 zł including the gearbox')), '2026-07-28'),
    post('Why cheap cylinders get picked', 'advice', 'euro.jpg', 'A 40 zł cylinder and a 200 zł one look the same from outside. Here is the difference.',
         J(para('Most flat doors in Wrocław have a class A or B cylinder that came with the door. Class A ones can be picked in under a minute by anyone who has watched a few videos.'),
           para('A class C cylinder has more pins, anti-drill plates and usually a snap line, so if someone breaks off the outer half, the lock still holds. It costs from 320 zł fitted.'),
           para('If you rent, ask your landlord first. Most say yes if you leave the new cylinder behind.')), '2026-09-18'),
    post('Please don\'t ask us to cut the love locks', 'advice', 'padlock.jpg', 'The padlocks on Tumski Bridge belong to the city. So does the job of removing them.',
         J(para('About once a month someone asks me to cut a padlock off Most Tumski, usually after a break-up. I can\'t. The bridge railings belong to the city, and cutting anything off them needs the city\'s permission.'),
           para('If you want it gone, email the district office. If you want it back, I\'m afraid you needed to keep the key.')), '2026-08-29'),
    post('Seized padlocks on garages and cellars', 'advice', 'padlock2.jpg', 'A rusty padlock usually needs cutting, not picking. It takes five minutes.',
         J(para('Cellar and garage padlocks in old Wrocław courtyards rust shut after a few winters. Oil rarely helps once the shackle is seized.'),
           para('I cut it with a disc cutter, fit a new closed-shackle padlock and give you three keys. From 150 zł including the padlock.')), '2026-08-02'),
    post('Keys, and who has them', 'advice', 'keys.jpg', 'For landlords: a key record takes ten minutes and saves a lock change.',
         J(para('Every time a flat changes hands, write down how many keys exist for each door and who has them. I send landlords a key record after every cylinder change.'),
           para('If a tenant leaves with one key missing, the record tells you whether you need a new cylinder or just a new copy.')), '2026-07-10'),
    post('Nadodrze and Ołbin', 'areas', 'street.jpg', 'My own area. Usually there in 15 to 25 minutes.',
         J(para('The workshop is on Jedności Narodowej, so Nadodrze, Ołbin and the streets around Nadodrze station are the quickest for me to reach.'),
           para('Many tenements here still have their original entrance doors with old mortise locks. I carry parts for the common ones, and I can usually save the old lock instead of replacing it.')), '2026-06-20'),
    post('Stare Miasto at night', 'areas', 'wroclaw.jpg', 'Most of my night calls are in the old town, between midnight and 4am.',
         J(para('Night call-outs in the centre are usually quicker than daytime ones, because I can park. Expect 15 minutes after 22:00.'),
           para('Night rate is 350 zł for opening a door without damage. I tell you the price on the phone.')), '2026-06-01'),
    post('Key cutting at the workshop', 'advice', 'keycutting.jpg', 'Most house keys, while you wait, from 15 zł. Ring first.',
         J(para('I cut flat keys, cylinder keys and most security keys with a card, if you bring the card. I don\'t copy keys marked "do not duplicate" for blocks of flats without a letter from the building manager.'),
           para('Workshop hours are Monday to Friday 9:00 to 17:00 and Saturday 9:00 to 13:00, but I close it when I go out to a lockout.')), '2026-05-12'),
    post('An old door, an old lock', 'advice', 'lock.jpg', 'Before you replace a tenement door lock, check whether it can be serviced.',
         J(para('Old mortise locks in tenement doors are often better made than new ones. They stop working because of dirt and a tired spring.'),
           para('A service costs about 150 zł and takes half an hour. A new lock and a new hole in a hundred-year-old door costs a lot more.')), '2026-04-20'),
]

content = {
    'site': {'title': 'Nowicki, ślusarz', 'tagline': 'Locksmith in Wrocław, day and night'},
    'categories': [{'slug': 'jobs', 'name': 'Jobs'}, {'slug': 'advice', 'name': 'Advice'}, {'slug': 'areas', 'name': 'Areas'}],
    'front_page': 'home', 'posts_page': 'advice',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'advice', 'title': 'Advice', 'content': ''},
        {'slug': 'lockouts', 'title': 'Locked out', 'pattern': 'key/lockouts-page'},
        {'slug': 'lock-changes', 'title': 'Lock changes', 'pattern': 'key/lock-changes-page'},
        {'slug': 'upvc-repairs', 'title': 'uPVC doors and windows', 'pattern': 'key/upvc-page'},
        {'slug': 'burglary-repairs', 'title': 'After a break-in', 'pattern': 'key/burglary-page'},
        {'slug': 'landlords', 'title': 'Landlords and agents', 'pattern': 'key/landlords-page'},
        {'slug': 'prices', 'title': 'Prices', 'pattern': 'key/prices-page'},
        {'slug': 'areas', 'title': 'Areas', 'pattern': 'key/areas-page'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'key/contact-page'},
    ],
    'posts': POSTS,
    'nav': [{'label': 'Locked out', 'url': '/lockouts/'}, {'label': 'Prices', 'url': '/prices/'}, {'label': 'Lock changes', 'url': '/lock-changes/'},
            {'label': 'uPVC', 'url': '/upvc-repairs/'}, {'label': 'Landlords', 'url': '/landlords/'}, {'label': 'Areas', 'url': '/areas/'},
            {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/key', exist_ok=True)
with open('demos/key/content.json', 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
with open('demos/key/readme-extra.md', 'w') as f:
    f.write('''Key is for independent locksmiths. The header carries a yellow call bar with the phone number and your insurance and certificate line, so people see proof before they ring; on phones it stays at the top of the screen. The front page is one column: the number in very large type, what to have ready, typical prices, how to recognise you, credentials, services and arrival times.

To change the number, edit the "Call bar" and "Giant tap-to-call number" patterns. Advice notes and area pages are posts in the Advice and Areas categories. The fonts include the Latin Extended range for Polish and other Central European languages.''')
print('demo written')
