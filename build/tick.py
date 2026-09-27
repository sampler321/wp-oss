# tick: Wróblewski, watch and clock repair in Łódź since 1961 (idea 261, zegarmistrz, as researched).
# Direction: the bench ledger. A technical-drawing page (drafting-film grey, graphite ink, brass rules, hairline
#   column guides on the front page) set in a classic Polish book face, because a watchmaker's world is small
#   measurements written down neatly, and the shop is Polish.
# Fonts: Poltawski Nowy (display, a revival of Adam Półtawski's 1928 Polish book type; claimed as new, since the
#   registry face Azeret Mono is now banned as a monospace) and Public Sans (body). Both with latin-ext for Polish.
# Palette: drafting film #F2F3EF, graphite #1B2430, brass #A57A2C (rules, buttons with ink text), plate grey, hairline,
#   oxblood for sold flags only.
# Layout idea: price lists as ruled lines with dotted leaders; a front page that opens with "what are you bringing
#   in?" over 12 hairline guides; the send-in slip with packing steps per item as the signature page.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('tick')
S = 'tick'
D = THEME['dir']

PALETTE = [
    ('base', '#F2F3EF', 'Drafting film'),
    ('contrast', '#1B2430', 'Graphite'),
    ('accent', '#A57A2C', 'Brass'),
    ('accent-2', '#7A1F1F', 'Case oxblood'),
    ('surface', '#E3E5DF', 'Plate grey'),
    ('line', '#8E989E', 'Hairline'),
    ('muted', '#4E5963', 'Pencil'),
    ('paper', '#FFFFFF', 'Slip paper'),
]
LATIN = 'U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD'
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    for ff in f['fontFace']:
        ff.setdefault('unicodeRange', LATIN)
FOCUS = {'outline': {'color': 'var:preset|color|contrast', 'offset': '3px', 'style': 'solid', 'width': '2px'}}
PAD = lambda t, b: {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1280px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.8125rem', 'name': 'Label', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.3rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.5rem', 'name': 'Title', 'fluid': {'min': '2.4rem', 'max': '3.5rem'}},
                {'slug': 'display', 'size': '5.5rem', 'name': 'Display', 'fluid': {'min': '2.9rem', 'max': '5.5rem'}},
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
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True,
                   'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Plate'}, {'slug': 'dial', 'size': '50%', 'name': 'Dial'}]},
        'custom': {'measure': '66ch'},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|accent-2'}}, ':focus': FOCUS},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'lineHeight': '1.05'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'fontWeight': '400'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '400'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.4', 'letterSpacing': '0.02em'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|contrast'},
                'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.7em', 'bottom': '0.7em', 'left': '1.2em', 'right': '1.2em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}},
                ':focus': FOCUS,
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.5'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|large'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/image': {'border': {'radius': '0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontStyle': 'italic'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '2px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '&{font-variant-numeric:tabular-nums lining-nums}& th{text-align:left;font-weight:600;border-width:0 0 1px 0!important;border-color:var(--wp--preset--color--contrast)}& td{border-width:0 0 1px 0!important;border-color:var(--wp--preset--color--line);padding:.55em .4em .55em 0}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);cursor:pointer}'},
            'core/search': {'css': '& .wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:0;background:var(--wp--preset--color--paper)}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': '.wp-block-post-content > * + :is(h2,h3,.wp-block-columns,.wp-block-media-text,.wp-block-group,.wp-block-image,.wp-block-details){margin-block-start:var(--wp--preset--spacing--60)}'
               ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none;font-variant-numeric:lining-nums}'
               'a:focus-visible,summary:focus-visible,input:focus-visible,button:focus-visible{outline:2px solid var(--wp--preset--color--contrast);outline-offset:3px;box-shadow:0 0 0 5px var(--wp--preset--color--accent)}'
               '.is-style-leaders li{display:flex;align-items:baseline;gap:.4em;padding:.45em 0;border-bottom:1px solid var(--wp--preset--color--line)}'
               '.is-style-leaders li strong{order:2;white-space:nowrap;font-variant-numeric:tabular-nums lining-nums}'
               '.is-style-leaders li::after{content:"";order:1;flex:1 1 2rem;border-bottom:1px dotted var(--wp--preset--color--contrast);transform:translateY(-.3em)}'
               '@media (min-width:782px){.is-style-guides{background-image:repeating-linear-gradient(to right,var(--wp--preset--color--surface) 0 1px,transparent 1px calc(100% / 12))}}'
               '@media print{header.wp-block-template-part,footer.wp-block-template-part,.no-print{display:none!important}.is-style-slip{border-style:dashed}}',
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    ],
}
with open(os.path.join(D, 'theme.json'), 'w') as f:
    json.dump(theme, f, indent='\t', ensure_ascii=False)

write('style.css', '''/*
Theme Name: Tick
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A theme for small watch and clock repair workshops, with ruled price lists, a send-in slip with packing steps and restored clocks for sale.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: tick
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column, grid-layout
*/''')


def variation(name, title, changes):
    pal = [(s, changes.get(s, c), n) for s, c, n in PALETTE]
    write('styles/%s.json' % name, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                               'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}, indent='\t', ensure_ascii=False))


variation('enamel-dial', 'Enamel dial', {'base': '#FBFAF6', 'contrast': '#14213D', 'surface': '#EFEDE6', 'line': '#9AA0AC', 'muted': '#4A5160'})
variation('longcase', 'Longcase', {'base': '#2E2118', 'contrast': '#EBDDBE', 'accent': '#C9A15B', 'accent-2': '#E7A08A', 'surface': '#3B2C21', 'line': '#6E5B48', 'muted': '#CDBF9F', 'paper': '#3B2C21'})
variation('bench-lamp', 'Bench lamp', {'base': '#FFFDF7', 'surface': '#F3EEDF', 'line': '#B9AE95', 'muted': '#55595E'})


def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))


section('leaders', 'Price leaders', ['core/list'], {'spacing': {'padding': {'left': '0'}}, 'css': '&{list-style:none}'})
section('guides', 'Column guides', ['core/group'], {'spacing': {'padding': PAD(70, 70)}})
section('page-main', 'Page body', ['core/group'], {'spacing': {'padding': PAD(60, 70)}})
section('pad-lg', 'Roomy section', ['core/group'], {'spacing': {'padding': PAD(70, 70)}})
section('ruled-strip', 'Ruled strip', ['core/group'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': PAD(20, 20)}})
section('site-header', 'Site header', ['core/group'], {'spacing': {'padding': PAD(30, 0)}})
section('site-footer', 'Site footer', ['core/group'], {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                                                     'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}}},
                                                     'spacing': {'padding': PAD(70, 50)}})
section('plate', 'Plate', ['core/group', 'core/column'], {'color': {'background': 'var:preset|color|surface'},
                                                         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('slip', 'Send-in slip', ['core/group'], {
    'color': {'background': 'var:preset|color|paper', 'text': 'var:preset|color|contrast'},
    'border': {'width': '1px', 'style': 'dashed', 'color': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
})
section('notice', 'Intake notice', ['core/group', 'core/paragraph'], {
    'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '3px', 'style': 'solid'}},
    'spacing': {'padding': {'left': 'var:preset|spacing|30', 'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10'}},
    'typography': {'fontSize': 'var:preset|font-size|small'},
})
section('dial', 'Dial status', ['core/paragraph'], {
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'},
    'css': '&{display:inline-flex;align-items:center;gap:.5em}&::before{content:"";width:1.1em;height:1.1em;border-radius:50%;border:2px solid var(--wp--preset--color--accent);background:radial-gradient(circle,var(--wp--preset--color--contrast) 0 2px,transparent 3px)}',
})
section('dial-sold', 'Dial status, sold', ['core/paragraph'], {
    'color': {'text': 'var:preset|color|accent-2'},
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'},
    'css': '&{display:inline-flex;align-items:center;gap:.5em}&::before{content:"";width:1.1em;height:1.1em;border-radius:50%;background:var(--wp--preset--color--accent-2)}',
})
section('timepiece-grid', 'Timepiece grid', ['core/post-template'], {
    'css': '& .wp-block-post-featured-image{background:var(--wp--preset--color--surface)}& .wp-block-post-featured-image img{object-fit:contain!important}',
})
section('rule-top', 'Rule above', ['core/group'], {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})

PHONE = '+48 42 630 18 61'
TEL = 'tel:+48426301861'
EMAIL = 'zegarmistrz@example.com'
ADDR = 'ul. Piotrkowska 118, courtyard building, first floor, 90-006 Łódź'
WARRANTY = '12 months warranty on every overhaul, 6 months on quartz movements.'


def leaders(items, **attrs):
    return lst(['%s <strong>%s</strong>' % (a, b) for a, b in items], className='is-style-leaders', **attrs)


# ---------------------------------------------------------------- front page
pattern('hero-chooser', 'Hero: what are you bringing in?', 'featured', group(J(
    columns(
        ('58%', J(heading('Watch and clock repair on Piotrkowska since 1961.', 1),
                  para('What are you bringing in?', fontFamily='display', fontSize='x-large'),
                  leaders([('A wristwatch, battery while you wait', 'from 35 zł'),
                           ('A mechanical watch, full service', 'from 450 zł'),
                           ('A pocket watch', 'from 520 zł'),
                           ('A mantel or wall clock', 'from 600 zł'),
                           ('A longcase clock, we come to you', 'from 150 zł a visit')]),
                  para('Full lists for <a href="/watch-repairs/">watches</a> and <a href="/clock-repairs/">clocks</a>. <a href="/send-in/">Sending by post?</a>', fontSize='small'),
                  para('Estimates are free. Nothing is done without your say-so.', fontSize='small'))),
        (None, J(image('pocket.jpg', 'A gold open-face pocket watch with its case open, showing the movement', 'Swiss pocket watch, about 1880, after a full service.', lightbox=False),
                 pattern_ref('hours'))),
        align='wide')),
    align='full', className='is-style-guides'), description='The opening screen: a chooser by what the customer is bringing in, with prices, over hairline column guides.')

pattern('hours', 'Opening hours', 'text', group(J(
    heading('Opening hours', 6),
    table([['Monday to Friday', '10:00 to 18:00'], ['Saturday', '10:00 to 14:00, every other week, ring first'], ['Sunday', 'Closed']]),
    para('Batteries and straps are done while you wait during opening hours.', fontSize='x-small')),
    layout={'type': 'default'}))

pattern('intake-notice', 'Notice: watch intake closed', 'banner', group(
    para('We are not taking new mechanical watch services until 2 February. The waiting list is about ten weeks. Batteries, straps and clocks are accepted as usual.'),
    className='is-style-notice', layout={'type': 'default'}), description='Swap the text when intake reopens, or delete the block.')

pattern('family-strip', 'Since 1961, as a sentence', 'about', group(
    para('Józef Wróblewski started mending watches at a folding table on Bałuty market in 1961, moved indoors to Piotrkowska in 1968, and taught his son Tadeusz, who taught his daughter Magda. The three of them have worked at the same bench, by the same window, for 57 years.', fontFamily='display', fontSize='x-large'),
    className='is-style-ruled-strip', align='wide'))

pattern('for-sale-grid', 'Restored clocks and watches for sale', 'portfolio,query', group(J(
    row(J(heading('Restored, for sale', 2), para('<a href="/for-sale/">Everything on the wall</a>', fontSize='small')), justify='space-between', align='wide'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='2/3', scale='contain'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=18)),
          per_page=4, align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '14rem'}, template_class='is-style-timepiece-grid')),
    align='wide', layout={'type': 'default'}))

pattern('timepiece-archive', 'Timepiece archive (inherits the query)', 'portfolio,query', inherit_query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='2/3', scale='contain'), dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=18)),
    align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '15rem'}, template_class='is-style-timepiece-grid'), inserter=False)

pattern('post-list', 'Post list', 'posts,query', inherit_query(
    J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', moreText='')), align='wide'), inserter=False)

pattern('timepiece-card', 'Timepiece for sale (facts and status)', 'portfolio', J(
    para('Available', className='is-style-dial'),
    table([['Maker', 'Unsigned, London'], ['Case', 'Burr walnut veneer on oak'], ['Date', 'About 1720'], ['Height', '218 cm'],
           ['Movement', '8-day, anchor escapement, brass dial with date'], ['Strike', 'Hours, on a bell'], ['Price', '18,500 zł, including delivery and setting up within 100 km']]),
    para(WARRANTY, fontSize='x-small')), description='Facts in the order people ask, with a dial status marker above. Use the "Dial status, sold" style when it goes.')

# ---------------------------------------------------------------- watches
pattern('watch-prices', 'Watch service price list', 'services', J(
    heading('Watches', 2),
    leaders([('Battery fitted, while you wait', '35 zł'), ('Strap fitted, or bracelet shortened', '20 zł'), ('Water-resistance test, with new seals', '60 zł'),
             ('Mineral crystal replaced', 'from 90 zł'), ('Sapphire crystal replaced', 'from 240 zł'), ('Mechanical watch, full service', 'from 450 zł'),
             ('Automatic or with date', 'from 550 zł'), ('Chronograph', 'from 900 zł'), ('Dial refinishing, by a specialist in Kraków', 'quoted')]),
    para('A full service means the movement is taken apart, cleaned, checked for wear, oiled, put back together and timed in six positions. Worn parts are extra and we always ask first. ' + WARRANTY, fontSize='small')))

pattern('watch-page', 'Page: watch repairs', 'services', J(
    pattern_ref('intake-notice'), pattern_ref('watch-prices'), pattern_ref('while-you-wait'),
    media_text('movement.jpg', 'The back of an automatic wristwatch with the case open, showing the rotor and a red jewel in the movement',
               J(heading('What we won\'t touch', 4), para('Smartwatches, and watches still under the maker\'s warranty, because opening them voids it. Send those back to the brand. We will happily look at anything older than you are.')), width=40)),
    block_types='core/post-content')

# ---------------------------------------------------------------- clocks
pattern('clock-prices', 'Clock repair price list', 'services', J(
    heading('Clocks', 2),
    leaders([('Quartz movement replaced, any wall clock', '120 zł'), ('Mantel clock, 8-day, time only, strip-down', '600 zł'),
             ('Mantel or bracket clock, striking', '800 zł'), ('Vienna regulator or wall clock with pendulum', '700 zł'),
             ('Carriage clock', '650 zł'), ('Longcase movement, full strip-down', '1,200 zł'), ('New suspension spring', '40 zł')]),
    para('Prices include cleaning, new bushes where the pivot holes are worn, oiling and a week on the test stand. Hand-made parts, such as a new wheel or pinion, are quoted separately before we cut them. ' + WARRANTY, fontSize='small')))

pattern('clock-page', 'Page: clock repairs', 'services', J(
    pattern_ref('clock-prices'),
    columns((None, image('carriage.jpg', 'A brass carriage clock with a white enamel dial and a handle on top, photographed in black and white', 'Carriage clock, French, about 1890.')),
            (None, image('gears.jpg', 'Engraved technical drawing of a clock movement showing gear trains and a pendulum from two sides', 'The same idea, drawn in 1771.'))),
    pattern_ref('estimate-statement')), block_types='core/post-content')

pattern('estimate-statement', 'Free estimate statement', 'text', group(J(
    heading('Free estimate, your decision', 4),
    para('We open the clock or watch, find what is wrong and phone you with a price. If you say no, you take it back and pay nothing, unless it came by post, in which case you pay the return postage.')),
    className='is-style-plate'))

# ---------------------------------------------------------------- house calls
pattern('house-calls', 'House calls for longcase and large wall clocks', 'services', columns(
    ('34%', image('longcase.jpg', 'A tall longcase clock in figured walnut with a brass dial and a hood with a carved top', lightbox=False, aspectRatio='4/5', scale='contain')),
    (None, J(heading('We come to the clock', 2),
             para('Longcase clocks and big wall regulators don\'t travel well. Tadeusz comes to you, sets the clock in beat, checks the weights and cords and oils what can be oiled in place.'),
             leaders([('Visit within Łódź', '150 zł'), ('Visit up to 50 km', '250 zł'), ('Collecting a movement for the workshop', '+100 zł')]),
             para('After 20 to 25 years without a strip-down, a visit is not enough. We will tell you honestly and take the movement to the workshop, leaving the case at home.', fontSize='small'),
             buttons(('Ring to book a visit', TEL)))),
    align='wide', verticalAlignment='top'))

pattern('house-call-questions', 'Before we visit (questionnaire)', 'text', J(
    heading('Before we visit, tell us', 4),
    lst(['The height of the clock and what is painted or engraved on the dial.',
         'Whether it has weights (and how many) or a spring.',
         'When it stopped, and whether anyone has moved it since.',
         'Which floor it is on, and whether there is a lift.'], ordered=True),
    para('A photo of the dial and one of the inside of the trunk, with the door open, saves a second trip.', fontSize='small')))

pattern('house-calls-page', 'Page: house calls', 'services', J(pattern_ref('house-calls'), pattern_ref('house-call-questions')), block_types='core/post-content')

# ---------------------------------------------------------------- send in (signature)
STEPS = {
    'A wristwatch': ['Wrap it in a soft cloth, then bubble wrap.', 'Put it in a small box so it can\'t move, with the slip.', 'Send it by registered post or courier, insured for its value.'],
    'A pocket watch': ['Close the case and the dust cover. If it has a key, send the key.', 'Wrap it in cloth and bubble wrap, in a small box.', 'Registered post or courier, insured.'],
    'A mantel clock': ['Take the pendulum off (it hangs behind the movement) and wrap it separately.', 'Send the key. Keep the case glass and anything loose at home if you can.', 'Two boxes: the clock in one with 8 to 10 cm of packing all round, that box inside a bigger one.'],
    'A wall clock with a pendulum': ['Stop the pendulum, lift it off its hook and wrap it separately.', 'Take the weights off and keep them at home, labelled left, middle and right.', 'Wrap the case, then use two boxes as for a mantel clock.'],
    'A longcase movement': ['Don\'t post a whole longcase clock. Book a house call, or ask us to collect the movement.', 'If you are sending only the movement and dial: take the hands off, wrap the dial face-up and keep weights and pendulum at home.', 'Courier only, two boxes, insured.'],
}
pattern('packing-steps', 'Packing steps by what you are sending', 'text', J(
    heading('What are you sending?', 2),
    para('Open the one that matches. Each has its own packing steps.'),
    *[details(k, lst(v, ordered=True)) for k, v in STEPS.items()]), description='One details block per kind of timepiece, so customers see only the steps for theirs.')

pattern('send-in-slip', 'Send-in slip (print and put in the box)', 'text', group(J(
    row(J(para('Wróblewski, zegarmistrz', fontFamily='display', fontSize='large'), para('Send-in slip', fontSize='small')), justify='space-between'),
    table([['Your name', ''], ['Address for return', ''], ['Phone', ''], ['Email', ''], ['What it is (maker, if known)', ''], ['What is wrong with it', ''], ['Its value, roughly', '']]),
    para('Send to: ' + ADDR + '. We ring you with a free estimate before any work is done. If you decline, we return it and you pay only the return postage.', fontSize='x-small')),
    className='is-style-slip'), description='A printable slip. Customers print the page and fill it in by hand; header and footer are hidden in print.')

pattern('send-in-page', 'Page: send it in', 'text', J(
    para('Most repairs come to us in person, but about a third arrive by post from the rest of Poland. It works if you pack it properly.', fontSize='large'),
    pattern_ref('packing-steps'),
    heading('Print this slip and put it in the box', 3),
    pattern_ref('send-in-slip'),
    para('Print this page (Ctrl+P, or Cmd+P on a Mac). The header and footer are left off the printout.', fontSize='small', className='no-print')), block_types='core/post-content')

# ---------------------------------------------------------------- glossary, about, directions
GLOSS = [
    ('Bush', 'A brass tube pressed into a worn pivot hole so the wheel runs true again. Included in our clock prices.'),
    ('Escapement', 'The part that lets the gear train move on one tooth at a time. It makes the tick.'),
    ('In beat', 'When the tick and the tock are evenly spaced. A clock out of beat stops within a day.'),
    ('Mainspring', 'The coiled spring that stores the power in a watch or spring-driven clock.'),
    ('Suspension spring', 'The thin strip the pendulum hangs from. It breaks more often than anything else, and costs 40 zł.'),
    ('Grande sonnerie', 'A clock or watch that strikes the hours and quarters at every quarter. Loud, and rare.'),
]
pattern('glossary', 'Glossary, A to Z', 'text', J(
    heading('Words we use in estimates', 2),
    *[J(heading(t, 4), para(d)) for t, d in GLOSS]), description='Glossary entries as headings, so each can be linked from a price list.')

pattern('about-history', 'About: the workshop', 'about', J(
    columns((None, image('shopfront.jpg', 'Black and white photo of a watchmaker with a loupe on his head working at a folding table on the street', 'A street watchmaker at his folding table. Józef started the same way.')),
            (None, J(heading('Three generations, one bench', 3),
                     para('Tadeusz Wróblewski has a master\'s certificate in watchmaking from the Łódź Chamber of Crafts (1984). Magda qualified in 2012 and does most of the watches now. Tadeusz does the clocks and the house calls.'),
                     para('We don\'t sell new watches. We have no opinion on your Rolex except that it needs a service every seven years, like everything else.'))), align='wide')))

pattern('directions', 'Directions and parking', 'contact', columns(
    (None, J(heading('Finding us', 2),
             para(ADDR),
             para('Go through the gate next to the pharmacy, cross the courtyard, and take the left-hand staircase. We are the first door on the first floor. Ring the bell marked Wróblewski.'),
             para('Trams stop at Piotrkowska Centrum, three minutes away. Parking on Piotrkowska itself is for residents, so use the paid car park on Sienkiewicza.', fontSize='small'),
             para('Phone <a href="%s">%s</a><br>Email <a href="mailto:%s">%s</a>' % (TEL, PHONE, EMAIL, EMAIL)))),
    (None, image('tenement.jpg', 'The ground floor stairwell of an old Łódź tenement, with a brown door and worn stone steps', 'The stairwell. It looks worse than the workshop.')),
    align='wide'))

pattern('directions-page', 'Page: directions', 'contact', J(pattern_ref('directions'), pattern_ref('hours'), image('street.jpg', 'Piotrkowska Street in Łódź seen along the tram tracks, with tenement houses on both sides', 'Piotrkowska, looking south.')), block_types='core/post-content')

pattern('guild-line', 'Trade membership line', 'about', para(
    'Members of the Cech Rzemiosł Różnych w Łodzi, the Łódź guild of craftsmen. Master\'s certificate in watchmaking, 1984.', fontSize='x-small'))

pattern('about-page', 'Page: about', 'about', J(pattern_ref('about-history'), pattern_ref('family-strip'), pattern_ref('guild-line')), block_types='core/post-content')

pattern('warranty-line', 'Warranty line', 'text', para(WARRANTY + ' Keep the ticket; it has the date on it.', fontSize='x-small'), description='One line to put under any service list.')

pattern('while-you-wait', 'Batteries while you wait', 'banner', group(J(
    heading('Batteries and straps while you wait', 4),
    para('About ten minutes, any time we are open. On the Saturdays we open, ring first: if Magda is alone at the bench, she may ask you to come back after lunch.', fontSize='small')),
    className='is-style-plate'))

print('patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

# ---------------------------------------------------------------- parts
write('parts/header.html', group(J(
    row(J(dyn('site-title', level=0), para('Piotrkowska 118, Łódź', fontSize='x-small', textColor='muted'),
          para('<a href="%s">%s</a>' % (TEL, PHONE), fontSize='small')), justify='space-between', align='wide'),
    group(dyn('navigation', overlayBackgroundColor='base', overlayTextColor='contrast', layout={'type': 'flex', 'justifyContent': 'space-between'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
          align='wide', className='is-style-ruled-strip', layout={'type': 'default'})),
    tag='header', align='full', className='is-style-site-header', layout={'type': 'constrained'}))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(para('Wróblewski, zegarmistrz', fontFamily='display', fontSize='x-large'), para('Watch and clock repair on Piotrkowska since 1961.', fontSize='small'))),
        (None, J(heading('Workshop', 6), para('ul. Piotrkowska 118<br>courtyard, first floor<br>90-006 Łódź', fontSize='small'))),
        (None, J(heading('Hours', 6), para('Mon to Fri 10:00 to 18:00<br>Every other Saturday 10:00 to 14:00', fontSize='small'))),
        (None, J(heading('Ring or write', 6), para('<a href="%s">%s</a><br><a href="mailto:%s">%s</a>' % (TEL, PHONE, EMAIL, EMAIL), fontSize='small'))),
        align='wide'),
    para(WARRANTY + ' Estimates are free.', align='wide', fontSize='small'),
    para('Demo photos are CC0 or public domain images from Wikimedia Commons and the Metropolitan Museum of Art, used as stand-ins.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-site-footer', layout={'type': 'constrained'}))

# ---------------------------------------------------------------- templates
M = {'className': 'is-style-page-main'}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero-chooser'),
    pattern_ref('intake-notice'),
    group(pattern_ref('for-sale-grid'), align='wide', layout={'type': 'default'}, className='is-style-pad-lg'),
    pattern_ref('family-strip'),
    group(columns((None, J(pattern_ref('watch-prices'))), (None, J(pattern_ref('clock-prices'))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
          align='full', layout={'type': 'constrained'}, className='is-style-pad-lg'),
    group(pattern_ref('house-calls'), align='full', backgroundColor='surface', className='is-style-pad-lg', layout={'type': 'constrained'})),
    layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|50'}}))

write('templates/home.html', page_template(J(
    heading('For sale', 1, align='wide', fontSize='xx-large'),
    para('Everything here has been through the workshop and carries our 12-month warranty. Call to see a clock before you buy; most hang on the workshop wall.', align='wide'),
    dyn('categories', align='wide'),
    pattern_ref('timepiece-archive')), **M))
write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'), dyn('term-description', align='wide'),
    pattern_ref('timepiece-archive')), **M))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), **M))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
                                               dyn('search', label='Search', showLabel=False, placeholder='Longcase, pocket watch, battery', buttonText='Search'), pattern_ref('post-list')), **M))
write('templates/404.html', page_template(J(heading('This page has stopped', 1, fontSize='xx-large'),
                                            para('Possibly a broken suspension spring. Try the <a href="/for-sale/">clocks for sale</a> or the price lists for <a href="/watch-repairs/">watches</a> and <a href="/clock-repairs/">clocks</a>.'),
                                            dyn('search', label='Search', showLabel=False, placeholder='Longcase, pocket watch, battery', buttonText='Search')), **M))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), **M))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide', fontSize='xx-large'),
                                                  dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1280px'})), **M))
write('templates/single.html', page_template(J(
    columns(('45%', dyn('post-featured-image', aspectRatio='2/3', scale='contain')),
            (None, J(dyn('post-terms', term='category'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'default'}))), align='wide'),
    group(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)),
          align='wide', layout={'type': 'flex', 'justifyContent': 'space-between'}, className='is-style-rule-top')), **M))
print('theme written')

# ---------------------------------------------------------------- demo
def piece(title, cat, img, excerpt, status, facts, story, date):
    body = J(para(status, className='is-style-dial-sold' if status == 'Sold' else 'is-style-dial'), para(story), table(facts), para(WARRANTY, fontSize='x-small'))
    return {'title': title, 'category': cat, 'image': img, 'excerpt': excerpt, 'date': date, 'content': body}


POSTS = [
    piece('Longcase clock, walnut, London, about 1720', 'longcase', 'longcase.jpg', '8-day, brass dial with date. 218 cm. 18,500 zł.', 'Available',
          [['Maker', 'Unsigned, London'], ['Case', 'Burr walnut veneer on oak'], ['Height', '218 cm'], ['Movement', '8-day, anchor escapement, strikes the hours on a bell'], ['Price', '18,500 zł, delivered and set up within 100 km']],
          'Came to us from a house in Zgierz with a cracked seatboard and one weight missing. New seatboard in oak, a replacement weight cast to match, full strip-down, twelve bushes.', '2026-09-12'),
    piece('Carriage clock, France, about 1890', 'mantel-and-carriage', 'carriage.jpg', 'Brass case, enamel dial, 8-day. 3,200 zł.', 'Reserved',
          [['Case', 'Brass, bevelled glass on five sides'], ['Height', '16 cm with handle up'], ['Movement', '8-day, platform lever escapement'], ['Price', '3,200 zł']],
          'A plain one, which is why it is affordable. Keeps time to about a minute a week.', '2026-08-30'),
    piece('Gold pocket watch, Switzerland, about 1880', 'watches', 'pocket.jpg', 'Open face, key-wound. 4,800 zł.', 'Available',
          [['Case', '14 ct gold, open face, hinged dust cover'], ['Movement', 'Key-wound cylinder movement'], ['Size', '42 mm'], ['Price', '4,800 zł, key included']],
          'Serviced, new mainspring and a new crystal. The key is original.', '2026-08-14'),
    piece('Mantel clock with Orpheus, Paris, about 1810', 'mantel-and-carriage', 'mantel.jpg', 'Gilt bronze, dial signed Le Roy. Sold.', 'Sold',
          [['Case', 'Gilt bronze figure of Orpheus with a lyre'], ['Dial', 'White enamel, signed Le Roy, Paris'], ['Movement', '8-day, silk suspension converted to spring']],
          'Sold to a collector in Poznań in July. We have a second, smaller one coming in the autumn.', '2026-07-22'),
    piece('Urn clock with rotating hours, France, about 1790', 'from-the-bench', 'workshop.jpg', 'Serviced for a private collector. Not for sale.', 'Not for sale',
          [['Type', 'Rotating-band clock: the hours turn past a fixed pointer'], ['Work', 'Strip-down, two new pivots, band re-tensioned'], ['Time on the bench', '3 weeks']],
          'The owner lives in Warsaw and drove it down on the back seat of a Škoda wrapped in a duvet. It survived.', '2026-06-30'),
    piece('Steel dress watch, serviced', 'watches', 'wristwatch.jpg', 'Automatic, 40 mm, leather strap. 2,400 zł.', 'Available',
          [['Case', 'Steel, 40 mm'], ['Movement', 'Automatic, with date'], ['Work', 'Full service, new crown seal, strap'], ['Price', '2,400 zł']],
          'Traded in by a customer who wanted something smaller. Service done by Magda in May.', '2026-06-02'),
    piece('An automatic, open on the bench', 'from-the-bench', 'movement.jpg', 'What a full service of an automatic watch involves, in order.', 'Not for sale',
          [['Parts', 'About 130 in an automatic with date'], ['Time', 'Five to six hours of bench work, spread over a week'], ['Price', 'from 550 zł']],
          'Taken apart, every part cleaned in three baths, the mainspring checked, jewels oiled with four different oils, reassembled, then timed in six positions over five days.', '2026-05-10'),
    piece('Where Józef started', 'from-the-bench', 'shopfront.jpg', 'A folding table, a loupe and a tin of parts. Bałuty market, 1961.', 'Not for sale',
          [['1961', 'Bałuty market, a folding table'], ['1968', 'Piotrkowska 118, the courtyard workshop'], ['1984', 'Tadeusz\'s master\'s certificate'], ['2012', 'Magda qualifies']],
          'This is not Józef in the photo, but it could be. He worked outdoors for seven years, winter included, with fingerless gloves.', '2026-03-01'),
]

content = {
    'site': {'title': 'Wróblewski, zegarmistrz', 'tagline': 'Watch and clock repair in Łódź since 1961'},
    'categories': [{'slug': 'longcase', 'name': 'Longcase'}, {'slug': 'mantel-and-carriage', 'name': 'Mantel and carriage'},
                   {'slug': 'watches', 'name': 'Watches'}, {'slug': 'from-the-bench', 'name': 'From the bench'}],
    'front_page': 'home', 'posts_page': 'for-sale',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'for-sale', 'title': 'For sale', 'content': ''},
        {'slug': 'watch-repairs', 'title': 'Watch repairs', 'pattern': 'tick/watch-page'},
        {'slug': 'clock-repairs', 'title': 'Clock repairs', 'pattern': 'tick/clock-page'},
        {'slug': 'house-calls', 'title': 'House calls', 'pattern': 'tick/house-calls-page', 'template': 'page-wide'},
        {'slug': 'send-in', 'title': 'Send it in', 'pattern': 'tick/send-in-page'},
        {'slug': 'directions', 'title': 'Directions', 'pattern': 'tick/directions-page', 'template': 'page-wide'},
        {'slug': 'glossary', 'title': 'Glossary', 'pattern': 'tick/glossary'},
        {'slug': 'about', 'title': 'About the workshop', 'pattern': 'tick/about-page', 'template': 'page-wide'},
    ],
    'posts': POSTS,
    'nav': [{'label': 'Watches', 'url': '/watch-repairs/'}, {'label': 'Clocks', 'url': '/clock-repairs/'}, {'label': 'House calls', 'url': '/house-calls/'},
            {'label': 'Send it in', 'url': '/send-in/'}, {'label': 'For sale', 'url': '/for-sale/'}, {'label': 'Glossary', 'url': '/glossary/'},
            {'label': 'Directions', 'url': '/directions/'}],
}
os.makedirs('demos/tick', exist_ok=True)
with open('demos/tick/content.json', 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
with open('demos/tick/fonts-claim.txt', 'w') as f:
    f.write('display: Poltawski Nowy (replaces Azeret Mono, which is now banned as a monospace)\n')
with open('demos/tick/readme-extra.md', 'w') as f:
    f.write('''Tick is for one- to three-person watch and clock repair shops. Price lists are plain lists with the "Price leaders" style: write the service, then the price in bold, and a dotted leader joins them. The Send it in page shows packing steps for each kind of timepiece and a slip customers print and put in the box.

Restored clocks and watches for sale are posts. Give each one a featured image, a short excerpt with the price, and use the "Timepiece for sale" pattern for the facts. Mark a sold piece with the "Dial status, sold" paragraph style. The fonts include the Latin Extended range, so Polish, Czech and Hungarian place names display correctly.''')
print('demo written')
