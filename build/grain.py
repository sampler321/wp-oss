# grain: Brink & Oduya, a two-person furniture workshop on the Houtmarkt in Zutphen (new idea: independent furniture
#   maker, built from ideas 021 and 099 but as a maker's workshop site: commissions, timber, lead times, visits).
# Direction: the order book. Dark oiled-walnut pages with shavings-pale type, because solid wood looks best against a
#   dark ground and a commission site should feel like the workshop at dusk, not a showroom. Deliberately unlike `joint`
#   (pale ash, grotesk, green): a serif, a dark ground, amber linseed accent.
# Fonts: Sentient (display, Fontshare serif, light weight at large sizes) and General Sans (body, Fontshare).
# Palette: walnut #231A13 base, shavings #EFE6D8 text, linseed amber #D9A05B accent, a darker board surface, and a pale
#   "cut-list paper" band for tables.
# Layout idea: the front page opens with what is on the two benches right now and when the next slot is free; every
#   finished piece carries a cut list (part, number, timber, finished size in mm); the commission process is a week-by-week
#   timeline, not a numbered card row.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('grain')


def grid(inner, min_width='16rem', layout=None, **attrs):
    """Grid group; pass layout to fix the column count."""
    return group(inner, layout=layout or {'type': 'grid', 'minimumColumnWidth': min_width}, **attrs)

S = 'grain'
D = THEME['dir']

PALETTE = [
    ('base', '#231A13', 'Oiled walnut'),
    ('contrast', '#EFE6D8', 'Shavings'),
    ('accent', '#D9A05B', 'Linseed'),
    ('surface', '#2E2319', 'End grain'),
    ('line', '#5C4A39', 'Pencil line'),
    ('muted', '#BDAE98', 'Sawdust'),
    ('paper', '#EFE6D8', 'Cut-list paper'),
    ('ink', '#231A13', 'Carpenter\'s pencil'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
FOCUS = {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}
PAD = lambda t, b: {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1360px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.8125rem', 'name': 'Note', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.3rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '1.9rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.6rem', 'max': '4rem'}},
                {'slug': 'display', 'size': '7rem', 'name': 'Display', 'fluid': {'min': '3.2rem', 'max': '7rem'}},
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
                   'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}, {'slug': 'button', 'size': '999px', 'name': 'Round-over'}]},
        'custom': {'measure': '64ch'},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.65'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': FOCUS},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '300', 'lineHeight': '1.04', 'letterSpacing': '-0.015em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '400', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '500'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600'}, 'color': {'text': 'var:preset|color|muted'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|ink'},
                'border': {'radius': '999px', 'width': '0'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.8em', 'bottom': '0.8em', 'left': '1.5em', 'right': '1.5em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|ink'}},
                ':focus': FOCUS,
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.5'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'fontSize': 'var:preset|font-size|large'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-excerpt': {'color': {'text': 'var:preset|color|muted'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/image': {'border': {'radius': '0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '300', 'lineHeight': '1.2'},
                           'border': {'width': '0'},
                           'elements': {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontStyle': 'normal'}, 'color': {'text': 'var:preset|color|muted'}}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '&{font-variant-numeric:tabular-nums lining-nums}& th{text-align:left;font-weight:600;border-width:0 0 1px 0!important;border-color:currentColor}& td{border-width:0 0 1px 0!important;border-color:var(--wp--preset--color--line);padding:.6em .6em .6em 0}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);cursor:pointer}'},
            'core/search': {'css': '& .wp-block-search__input{border:1px solid var(--wp--preset--color--line);border-radius:999px;background:var(--wp--preset--color--surface);color:var(--wp--preset--color--contrast);padding-inline:1em}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': '.wp-block-post-content > * + :is(h2,h3,.wp-block-columns,.wp-block-media-text,.wp-block-group,.wp-block-image,.wp-block-table){margin-block-start:var(--wp--preset--spacing--60)}'
               ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none}'
               'a:focus-visible,summary:focus-visible,input:focus-visible,button:focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
               '.is-style-paper a{color:var(--wp--preset--color--ink)}'
               '.is-style-bench-row{border-top:1px solid var(--wp--preset--color--line)}',
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
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


with open(os.path.join(D, 'theme.json'), 'w') as f:
    json.dump(theme, f, indent='\t', ensure_ascii=False)

write('style.css', '''/*
Theme Name: Grain
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A theme for small furniture workshops that make solid-wood pieces to commission, with an order book, cut lists, timber notes and workshop visits.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: grain
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column
*/''')


def variation(name, title, changes):
    pal = [(s, changes.get(s, c), n) for s, c, n in PALETTE]
    write('styles/%s.json' % name, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                               'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}, indent='\t', ensure_ascii=False))


variation('limed-oak', 'Limed oak', {'base': '#EEE8DC', 'contrast': '#2A2119', 'accent': '#8A5A1E', 'surface': '#E2D9C8', 'line': '#B3A58D', 'muted': '#5E5243', 'paper': '#FFFFFF', 'ink': '#2A2119'})
variation('bog-oak', 'Bog oak', {'base': '#151515', 'contrast': '#E6E1D8', 'accent': '#C9B27C', 'surface': '#1F1F1E', 'line': '#474540', 'muted': '#ADA698'})
variation('cherry', 'Cherry', {'base': '#3A1F17', 'contrast': '#F3E7DA', 'accent': '#F0B27A', 'surface': '#46271D', 'line': '#6E4636', 'muted': '#D8BFA9', 'ink': '#3A1F17'})


def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))


section('paper', 'Cut-list paper', ['core/group', 'core/table'], {
    'color': {'background': 'var:preset|color|paper', 'text': 'var:preset|color|ink'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
    'elements': {'link': {'color': {'text': 'var:preset|color|ink'}}, 'heading': {'color': {'text': 'var:preset|color|ink'}}},
})
section('board', 'Board', ['core/group', 'core/column'], {
    'color': {'background': 'var:preset|color|surface'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
})
section('pad-lg', 'Roomy section', ['core/group'], {'spacing': {'padding': PAD(70, 70)}})
section('page-main', 'Page body', ['core/group'], {'spacing': {'padding': PAD(60, 70)}})
section('site-header', 'Site header', ['core/group'], {'spacing': {'padding': PAD(40, 30)}})
section('site-footer', 'Site footer', ['core/group'], {'color': {'background': 'var:preset|color|surface'},
                                                     'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                                                     'spacing': {'padding': PAD(70, 50)}})
section('bench-row', 'Bench row', ['core/columns'], {'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40'}}})
section('rule-top', 'Rule above', ['core/group'], {'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('week', 'Timeline week', ['core/columns'], {'border': {'top': {'color': 'var:preset|color|accent', 'width': '1px', 'style': 'solid'}},
                                                   'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})

EMAIL = 'werkplaats@example.com'
PHONE = '+31 575 000 482'
TEL = 'tel:+31575000482'
ADDR = 'Houtmarkt 71, 7201 KL Zutphen'
LEAD = 'Next free bench slot: February 2027. Tables take 10 to 12 weeks from the day we start, chairs about 3 weeks each.'


def cutlist(rows):
    return table(rows, head=['Part', 'No.', 'Timber', 'Finished size (mm)'], className='is-style-paper')


# ---------------------------------------------------------------- front page
pattern('order-book', 'Hero: name, the order book and a finished piece', 'hero,featured', group(J(
    columns(
        ('44%', J(heading('Brink &amp; Oduya, furniture makers in Zutphen', 1, fontSize='xx-large'),
                  para('Sanne Brink and Kofi Oduya make tables, chairs and cabinets to commission in a former tannery on the Houtmarkt. Oak, elm, ash and walnut, mostly from trees felled within 60 km.'),
                  buttons(('Start a commission', '/commissions/'), ('Book a workshop visit', '/workshop/')),
                  heading('On the benches this week', 6),
                 columns((None, para('Bench one', fontFamily='display', fontSize='large')),
                         ('70%', para('Oak dining table, 2400 × 950 mm, for a family in Deventer. Second coat of soap finish on Thursday.')), className='is-style-bench-row'),
                 columns((None, para('Bench two', fontFamily='display', fontSize='large')),
                         ('70%', para('Six ladder-back chairs in ash with rush seats. Chair four of six, back legs steam-bent on Monday.')), className='is-style-bench-row'),
                 columns((None, para('Next slot', fontFamily='display', fontSize='large')),
                         ('70%', para(LEAD)), className='is-style-bench-row'))),
        (None, image('chest.jpg', 'A dark carved oak chest with three panels of stylised flowers on the front', 'Joined chest in riven oak, finished in May. The original it copies is 350 years older.')),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|70'}}})),
    align='full', className='is-style-pad-lg', layout={'type': 'constrained'}), description='The signature opening: what is on each bench right now and when the next slot is free. Edit it each week or two.')

pattern('pieces-feature', 'Recent pieces (large alternating)', 'portfolio,query', group(J(
    row(J(heading('Recent pieces', 2), para('<a href="/pieces/">Everything we have made since 2016</a>', fontSize='small')), justify='space-between', align='wide'),
    query(columns(('55%', dyn('post-featured-image', isLink=True, aspectRatio='4/3')),
                  (None, J(dyn('post-terms', term='category'), dyn('post-title', isLink=True, level=3, fontSize='x-large'), dyn('post-excerpt', moreText='Read the cut list', excerptLength=40)))),
          per_page=3, align='wide')),
    align='wide', layout={'type': 'default'}), keywords='pieces, portfolio, furniture')

pattern('pieces-archive', 'Pieces archive (inherits the query)', 'portfolio,query', inherit_query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='4/5'), dyn('post-terms', term='category'), dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=22)),
    align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '17rem'}), inserter=False)

pattern('post-list', 'Post list', 'posts,query', inherit_query(
    J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', moreText='')), align='wide'), inserter=False)

# ---------------------------------------------------------------- signature: cut list
pattern('cut-list', 'Cut list for a piece', 'portfolio,featured', J(
    heading('Cut list', 4),
    cutlist([['Top boards', '4', 'Oak, quarter-sawn', '2400 × 240 × 32'], ['Legs', '4', 'Oak', '720 × 90 × 90'], ['Long rails', '2', 'Oak', '2050 × 110 × 28'],
             ['Short rails', '2', 'Oak', '640 × 110 × 28'], ['Buttons', '12', 'Oak offcuts', '50 × 30 × 20']]),
    para('Joints: through mortise and tenon, drawbored with oak pegs. Top fixed with buttons so it can move with the seasons.', fontSize='small')),
    description='Every finished piece gets its cut list: part, number, timber and finished size in millimetres.')

pattern('piece-facts', 'Piece facts (size, timber, finish, time, price)', 'portfolio', specs([
    ('Size', 'L 2400, W 950, H 745 mm'), ('Timber', 'Oak from the Achterhoek, air-dried three years'), ('Finish', 'Soap flakes, four coats'),
    ('Time on the bench', '11 weeks'), ('Price', '€6,200 including delivery within 100 km')]))

# ---------------------------------------------------------------- commissions
WEEKS = [
    ('Week 0', 'A conversation', 'At the workshop, at your house or on the phone. Bring the room\'s measurements and a photo. We sketch while we talk.'),
    ('Weeks 1 to 2', 'Drawings and a price', 'Scale drawings at 1:5 and a fixed price. If you want changes, we redraw once for free. A 40% deposit books a bench slot.'),
    ('When your slot comes', 'Choosing the boards', 'Come and pick the boards from our timber store, or leave it to us. Most people come; it takes an hour.'),
    ('The making', 'Six to ten weeks', 'We send a photo every Friday. You are welcome to visit on a Saturday and see it half-made.'),
    ('The last week', 'Finishing', 'Oil or soap, three to four coats, and a week to cure before it leaves.'),
    ('Delivery', 'We bring it', 'Two of us, a van and blankets. We set it up, level it and show you how to look after it. The balance is due on the day.'),
]
pattern('commission-timeline', 'Commission timeline, week by week', 'services', J(
    heading('How a commission goes', 2),
    *[columns(('24%', para(w, fontFamily='display', fontSize='large', textColor='accent')), (None, J(heading(t, 4), para(d))), className='is-style-week') for w, t, d in WEEKS]),
    description='The commission process as a timeline in weeks, from first conversation to delivery.')

pattern('price-guide', 'What things cost', 'prices,services', J(
    heading('What things cost', 3),
    table([['Dining table in oak, seats six', 'from €4,800'], ['Dining chair, ash or oak', 'from €1,150 each'], ['Blanket chest', 'from €2,900'],
           ['Sideboard or cabinet', 'from €6,500'], ['Small pieces: stools, side tables, shelves', 'from €650'], ['Drawings and design, if you don\'t go ahead', '€150']],
          head=['Piece', 'Price'], className='is-style-paper'),
    para('Prices include VAT and delivery within 100 km of Zutphen. Walnut adds about 45%, elm about 10%.', fontSize='small')))

pattern('lead-time', 'Current lead time', 'banner', group(para(LEAD, fontFamily='display', fontSize='x-large'), className='is-style-board'),
        description='Change this line whenever the order book moves.')

pattern('what-we-dont-make', 'What we don\'t make', 'text', group(J(
    heading('What we don\'t make', 4),
    para('Kitchens, fitted wardrobes and staircases: that is joinery, and we can recommend two good joiners in the Achterhoek. We also don\'t copy a named designer\'s piece. We will happily make something that does the same job.')),
    className='is-style-board'))

pattern('commission-faq', 'Commission questions', 'text', J(
    heading('Questions people ask', 3),
    details('Can you make it to fit an odd space?', para('That is most of what we do. Send measurements and a photo with a tape measure in it.')),
    details('Can I supply my own timber?', para('Sometimes. If it is a tree from your garden, it needs felling, milling and at least two years of drying before we can use it. We can arrange all three.')),
    details('What if the wood moves or cracks?', para('Solid wood moves with the seasons and we build for that. Joints are guaranteed for ten years. If a top splits because of how we made it, we repair it.')),
    details('Do you deliver abroad?', para('Belgium and Germany, yes, at cost. Further than that we crate it and a carrier takes it.'))))

pattern('commissions-page', 'Page: commissions', 'services', J(
    pattern_ref('lead-time'), pattern_ref('commission-timeline'), pattern_ref('drawing-sheet'), pattern_ref('price-guide'), pattern_ref('payment-terms'), pattern_ref('delivery-note'), pattern_ref('sizes-guide'), pattern_ref('what-we-dont-make'), pattern_ref('commission-faq')),
    block_types='core/post-content')

# ---------------------------------------------------------------- timber and finishes
pattern('timber-table', 'Timber we use', 'text', J(
    heading('Timber we use', 2),
    pattern_ref('timber-swatches'),
    columns(('35%', image('grain.jpg', 'Sixteen small squares of different pale and golden woods arranged in a grid')),
            (None, J(heading('Samples by post', 4), para('A set of five sample boards, 150 × 100 mm, oiled on one half and bare on the other. €12 by post, refunded when you order. Or come on a Saturday and handle the real boards.'))),
            verticalAlignment='center')))

pattern('finishes', 'Finishes', 'text', J(
    heading('Finishes', 2),
    columns(
        (None, J(heading('Soap', 4), para('Soap flakes and water, four coats. Keeps oak pale and matt. The finish we like best, and the easiest to repair: you wash it with soap.'))),
        (None, J(heading('Hardwax oil', 4), para('Two coats, a satin sheen, good against wine and water rings. What most dining tables get.'))),
        (None, J(heading('Linseed oil', 4), para('Slow, traditional, darkens the wood. Needs a fresh coat once a year. Good on chairs.'))),
        (None, J(heading('Shellac', 4), para('For cabinets and small boxes only. Beautiful, and it hates hot mugs, so never on a table.'))),
        align='wide')))

pattern('timber-store', 'The timber store', 'about', media_text('timber.jpg', 'Black and white photo of boards stacked in a sawmill yard with men standing on the stacks',
    J(heading('Where the boards wait', 3),
      para('We buy logs, have them milled into boards, then stack them with spacers in the old tannery shed for a year per 25 mm of thickness. There are about 30 cubic metres out there now.'),
      para('The photo is a sawmill yard from 1900, used as a stand-in. Ours is smaller and has a cat.', fontSize='small')),
    width=50, align='wide'))

pattern('elm-note', 'Elm note', 'text', columns(
    ('35%', image('elm.jpg', 'Botanical drawing of elm leaves, flowers and seeds')),
    (None, J(heading('Why elm', 3), para('Dutch elm disease still kills trees along the IJssel every summer. The wood is sound, interlocked and hard to split, which made it the chair-seat timber for centuries. We buy as much as the council will sell us.')))))

pattern('timber-page', 'Page: timber and finishes', 'text', J(pattern_ref('timber-table'), pattern_ref('finishes'), pattern_ref('timber-store'), pattern_ref('elm-note')), block_types='core/post-content')

# ---------------------------------------------------------------- workshop
pattern('workshop-visits', 'Workshop visits', 'call-to-action', group(J(
    heading('Come to the workshop', 2),
    para('Saturdays 10:00 to 13:00, by appointment. See pieces half-made, choose your boards, sit on the chairs. The kettle is on and the floor is not clean.'),
    para(ADDR + '. Ten minutes\' walk from the station. The workshop door is in the courtyard behind the tannery, not on the street.'),
    buttons(('Book a Saturday visit', 'mailto:%s?subject=Workshop%%20visit' % EMAIL))),
    className='is-style-paper'))

pattern('makers', 'The two makers', 'about', columns(
    (None, J(heading('Sanne Brink', 3), para('Trained at the Hout- en Meubileringscollege in Rotterdam, then six years restoring church furniture. Tables, cabinets and anything with drawers. Opinion: soap finish on oak is underrated.'))),
    (None, J(heading('Kofi Oduya', 3), para('Came to furniture from boatbuilding in Enkhuizen. Chairs, steam-bending and the band saw. Makes one stool a month for himself and gives it away.'))),
    align='wide'))

pattern('workshop-photo', 'Workshop photo', 'gallery', image('bench.jpg', 'An old woodworking workshop with hand tools and wooden planes hanging on plank walls above a workbench', 'A workshop much like ours, with fewer power tools. Stand-in photo.'))

pattern('workshop-page', 'Page: workshop', 'about', J(pattern_ref('makers'), pattern_ref('workshop-photo'), pattern_ref('making-steps'), pattern_ref('open-days'), pattern_ref('workshop-visits'), pattern_ref('makers-mark'), pattern_ref('repairs-service'),
    image('zutphen.jpg', 'A narrow brick street in Zutphen with old gabled houses and a shop sign', 'Zutphen, five minutes from the workshop.')), block_types='core/post-content')

# ---------------------------------------------------------------- care, contact
pattern('care', 'Care and guarantee', 'text', J(
    heading('Looking after solid wood', 2),
    lst(['Wipe spills. Water left overnight leaves a ring on oil and soap finishes; a damp cloth and a little soap takes most of them out.',
         'Keep it at least a metre from radiators and out of full sun for the first summer.',
         'Soap finish: wash monthly with soap flakes dissolved in warm water, the same way we finished it.',
         'Oil finish: a thin coat of the oil we give you, once a year.']),
    group(J(heading('Ten-year guarantee', 4), para('Joints are guaranteed for ten years. We refinish tables we made for the cost of the oil and a day\'s work, about €350, whenever you want.')), className='is-style-board')))

pattern('care-page', 'Page: care', 'text', J(pattern_ref('care'), pattern_ref('makers-mark')), block_types='core/post-content')

pattern('contact-details', 'Contact details', 'contact', columns(
    (None, J(heading('Write, ring or visit', 2),
             para('<a href="mailto:%s">%s</a><br><a href="%s">%s</a>' % (EMAIL, EMAIL, TEL, PHONE), fontSize='large'),
             para('We answer email in the evening. The phone rings in a room full of machines, so leave a message and we ring back after five.'))),
    (None, J(heading('Workshop', 4), para(ADDR + '<br>Courtyard entrance, behind the tannery'),
             para('Visits on Saturdays 10:00 to 13:00, by appointment.', fontSize='small'))),
    align='wide'))

pattern('commission-brief', 'What to tell us when you write', 'call-to-action', J(
    heading('When you write, tell us', 3),
    lst(['What it is for, and in which room.', 'Rough sizes, or the space it has to fit.', 'Which timber, if you know.', 'When you would like it, and roughly what you want to spend.'])))

pattern('contact-page', 'Page: contact', 'contact', J(pattern_ref('contact-details'), pattern_ref('commission-brief'), pattern_ref('lead-time')), block_types='core/post-content')

pattern('dovetail-note', 'Hand-cut joints', 'text', media_text('dovetail.jpg', 'Engraved drawing of through and lapped dovetail joints in two pieces of wood',
    J(heading('Joints you can see', 3), para('Drawers are dovetailed by hand, carcasses are jointed, and nothing is held together with screws you can\'t get at. That is why a chest from us can be taken apart and repaired in a hundred years.')),
    width=40, right=True, align='wide'))
# ---------------------------------------------------------------- round 2 patterns
TIMBERS = [('Oak', 'Estates in the Achterhoek, air-dried three years', 'Pale honey, darkens to amber', 'Base price'),
           ('Elm', 'Trees felled for Dutch elm disease along the IJssel', 'Wild grain, brown with green streaks', 'Plus 10%'),
           ('Ash', 'Local, from ash dieback felling', 'Pale, bends well, good for chairs', 'Less 10%'),
           ('Walnut', 'Garden and park trees, when we can get them', 'Chocolate brown, purple when fresh', 'Plus 45%'),
           ('Cherry', 'A sawmill near Gent', 'Pink at first, red-brown within a year', 'Plus 20%')]
pattern('timber-swatches', 'Timber cards (where from, how it looks, price)', 'text', grid(J(*[
    stack(J(para(t, fontFamily='display', fontSize='x-large'), para(src, fontSize='small'), para(look, fontSize='small', textColor='muted'), para(price, fontSize='small', textColor='accent')), className='is-style-board')
    for t, src, look, price in TIMBERS]), align='wide', layout={'type': 'grid', 'columnCount': 5, 'minimumColumnWidth': '11rem'}), description='One card per timber, instead of a comparison table.')

pattern('three-ways', 'Three ways in: commission, pieces, visit', 'hero', columns(
    (None, J(heading('<a href="/commissions/">Commission</a>', 3), para('A piece drawn and made for your room. From drawings to delivery in about three months.'))),
    (None, J(heading('<a href="/ready-now/">Ready now</a>', 3), para('Two or three finished pieces that can leave the workshop this month.'))),
    (None, J(heading('<a href="/workshop/">Visit</a>', 3), para('Saturday mornings, by appointment. Sit on the chairs, choose the boards.'))),
    align='wide', className='is-style-bench-row'), description='Three entry points, like a maker\'s shop, a commission form and an open door.')

pattern('pieces-gallery', 'Pieces gallery (lightbox)', 'gallery', gallery([
    ('chair2.jpg', 'A ladder-back chair with a woven rush seat', 'Ladder-back chair, ash and rush'),
    ('chair.jpg', 'A ladder-back rocking chair with a woven tape seat', 'Rocking chair, cherry'),
    ('chest.jpg', 'A carved oak chest with flower panels', 'Joined chest, riven oak'),
    ('cabinet.jpg', 'A large two-part cupboard in ash and oak with carved panels', 'The Nuremberg cupboard, study trip'),
    ('stool.jpg', 'A walnut piano stool on a turned pedestal', 'Piano stool, rebuilt'),
    ('dovetail.jpg', 'Engraved drawing of dovetail joints', 'Dovetails, for the drawers')], columns=3, align='wide'),
    description='Six pieces. Click any to see it large.')

pattern('making-steps', 'From board to piece (gallery)', 'gallery', J(
    heading('From board to piece', 3),
    gallery([('timber.jpg', 'Boards stacked with spacers in a timber yard', 'The boards dry, a year per 25 mm'),
             ('shavings.jpg', 'A small hand plane lying among curled wood shavings', 'Planed by hand'),
             ('clamps.jpg', 'A row of clamps holding a glued frame on a workshop floor', 'Glued up'),
             ('joinery.jpg', 'Old log wall with notched corner joints', 'Jointed, not screwed')], columns=4, align='wide')))

pattern('drawing-sheet', 'The drawings you get', 'services', media_text('dovetail.jpg', 'Engraved drawing of through and lapped dovetail joints, labelled A and B',
    J(heading('Drawings before anything is cut', 3),
      para('You get scale drawings at 1:5 of every view, with the joints drawn in, and a price that doesn\'t move. We redraw once for free. The drawings are yours, even if you don\'t go ahead.')),
    width=40, align='wide'))

pattern('payment-terms', 'Deposit and payment', 'text', J(
    heading('Paying for a commission', 4),
    specs([('To book a bench slot', '40% deposit'), ('On delivery', 'The balance, by bank transfer'), ('Drawings only', '€150, taken off the price if you go ahead'), ('Cancelling', 'Deposit returned in full until we cut the first board')])))

pattern('delivery-note', 'Delivery', 'text', J(
    heading('Delivery', 4),
    para('We deliver ourselves, two of us and a van, within 100 km of Zutphen for free. Further than that in the Netherlands, Belgium and western Germany we charge the fuel. We carry it in, set it up, level it and take the blankets away.')))

pattern('open-days', 'Open workshop days', 'posts', J(
    heading('Open workshop days', 3),
    specs([('Saturday 7 November', '10:00 to 16:00, with Kofi steam-bending chair backs at 11:00'), ('Saturday 12 December', '10:00 to 16:00, the last day to order for spring'),
           ('Saturday 13 March', 'Timber day: the new elm boards come out of the shed')]),
    para('No booking needed on open days. Other Saturdays are by appointment.', fontSize='small')))

pattern('newsletter', 'A letter from the workshop', 'call-to-action', group(J(
    heading('A letter from the workshop, four times a year', 4),
    para('What we made, what timber came in and when the next bench slot is free. No offers, because there aren\'t any.'),
    buttons(('Ask to be on the list', 'mailto:%s?subject=Letter' % EMAIL))),
    className='is-style-board'))

pattern('ready-now', 'Ready now: pieces in stock', 'portfolio', J(
    para('Sometimes a commission is cancelled or we make a second one while the jig is set up. These can leave the workshop this month.', fontSize='large'),
    columns(
        (None, J(image('stool.jpg', 'A walnut piano stool on a turned pedestal with three carved feet'), heading('Walnut stool', 4), specs([('Size', 'Seat 360 mm, height 460 to 560 mm'), ('Price', '€890')]))),
        (None, J(image('chair2.jpg', 'A ladder-back chair with a woven rush seat'), heading('Ladder-back chair, ash', 4), specs([('Size', 'Seat height 450 mm'), ('Price', '€1,150, one only')]))),
        align='wide')), description='The handful of finished pieces available straight away.')

pattern('repairs-service', 'Repairs we take on', 'services', J(
    heading('Repairs', 3),
    para('One or two a season, when the piece deserves it and the fix is joinery rather than a new finish: loose chairs reglued with hide glue, split tops, new drawer runners. From €180. We don\'t do French polishing or upholstery.')))

pattern('testimonials', 'What clients say', 'testimonials', columns(
    (None, quote('We visited three times while the table was being made. The third time our daughter was allowed to plane the underside.', 'Marieke and Joost, Deventer, 2026')),
    (None, quote('The chairs are the only things in the house nobody is allowed to stand on.', 'Hanneke, Lochem, 2025')),
    align='wide'))

pattern('makers-mark', 'Signed and dated', 'about', group(J(
    heading('Signed and dated', 4),
    para('Every piece is signed and dated under the top or inside a drawer, with the timber\'s origin burned in beside it. If it ever comes back for repair in fifty years, whoever opens it will know where it came from.')),
    className='is-style-board'))

pattern('sizes-guide', 'Sizes that work', 'text', J(
    heading('Sizes that work', 3),
    specs([('Dining table height', '740 to 760 mm'), ('Chair seat height', '440 to 460 mm'), ('Width per diner', '600 mm, 700 if you like elbows'),
           ('Space behind a chair', '900 mm to get up without scraping the wall')])))

pattern('hero-piece', 'Hero: one piece, large, with a caption', 'hero', group(J(
    image('cabinet.jpg', 'A tall two-part cupboard in golden ash and oak with carved panels and pilasters', 'The cupboard in Nuremberg that taught us how panels should float. About 1600, Stadtmuseum Fembohaus.', align='wide'),
    row(J(heading('Pieces made to last longer than the house', 2, fontSize='x-large'), buttons(('See our pieces', '/pieces/'))), justify='space-between', align='wide')),
    align='full', layout={'type': 'constrained'}), description='An alternative opening: one big photograph with a caption and a single link.')


print('patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

# ---------------------------------------------------------------- parts
write('parts/header.html', group(group(J(
    dyn('site-title', level=0),
    dyn('navigation', overlayBackgroundColor='base', overlayTextColor='contrast', layout={'type': 'flex', 'justifyContent': 'right'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
    align='wide', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}),
    tag='header', align='full', className='is-style-site-header', layout={'type': 'constrained'}))

write('parts/footer.html', group(J(
    columns(
        ('45%', J(para('Brink &amp; Oduya', fontFamily='display', fontSize='x-large'), para('Furniture makers. Solid wood, to commission, since 2016.', fontSize='small'),
                  para(LEAD, fontSize='small', textColor='accent'))),
        (None, J(heading('Workshop', 6), para('Houtmarkt 71<br>7201 KL Zutphen<br>Saturdays by appointment', fontSize='small'))),
        (None, J(heading('Contact', 6), para('<a href="mailto:%s">%s</a><br><a href="%s">%s</a>' % (EMAIL, EMAIL, TEL, PHONE), fontSize='small'))),
        align='wide'),
    para('Demo images are public domain or CC0 photographs and drawings from Wikimedia Commons, the Metropolitan Museum of Art and the National Gallery of Art, used as stand-ins for the makers\' own photos.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-site-footer', layout={'type': 'constrained'}))

# ---------------------------------------------------------------- templates
M = {'className': 'is-style-page-main'}
write('templates/front-page.html', page_template(J(
    pattern_ref('order-book'),
    pattern_ref('three-ways'),
    group(pattern_ref('pieces-feature'), align='wide', layout={'type': 'default'}),
    group(pattern_ref('making-steps'), align='wide', layout={'type': 'default'}),
    group(pattern_ref('commission-timeline'), align='wide', className='is-style-pad-lg', layout={'type': 'default'}),
    group(pattern_ref('dovetail-note'), align='wide', layout={'type': 'default'}),
    group(J(heading('Timber we use', 2), pattern_ref('timber-swatches'), para('<a href="/timber/">Timber and finishes in detail</a>', fontSize='small')), align='full', className='is-style-pad-lg', layout={'type': 'constrained'}),
    pattern_ref('testimonials'),
    group(columns(('60%', pattern_ref('workshop-visits')), (None, pattern_ref('newsletter'))), align='wide', layout={'type': 'default'})),
    layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|60'}}))

write('templates/home.html', page_template(J(
    heading('Pieces', 1, align='wide', fontSize='xx-large'),
    pattern_ref('pieces-gallery'),
    para('Everything here was made on our two benches. Each piece has its cut list, timber and finish.', align='wide'),
    dyn('categories', align='wide'),
    pattern_ref('pieces-archive')), **M))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'), dyn('term-description', align='wide'), pattern_ref('pieces-archive')), **M))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), **M))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Oak table, elm, chair', buttonText='Search'), pattern_ref('post-list')), **M))
write('templates/404.html', page_template(J(heading('Nothing on this bench', 1, fontSize='xx-large'), para('The page may have moved. Try the <a href="/pieces/">pieces</a> or the <a href="/commissions/">commissions page</a>.'),
                                            dyn('search', label='Search', showLabel=False, placeholder='Oak table, elm, chair', buttonText='Search')), **M))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), **M))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide', fontSize='xx-large'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1360px'})), **M))
write('templates/single.html', page_template(J(
    group(J(dyn('post-terms', term='category'), dyn('post-title', level=1, fontSize='xx-large')), align='wide', layout={'type': 'default'}),
    dyn('post-featured-image', align='wide', aspectRatio='16/9'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous piece', showTitle=True), dyn('post-navigation-link', label='Next piece', showTitle=True)),
          align='wide', layout={'type': 'flex', 'justifyContent': 'space-between'}, className='is-style-rule-top')), **M))
pattern_categories([('hero', 'Hero'), ('prices', 'Prices')])
print('theme written')

# ---------------------------------------------------------------- demo
def piece(title, cat, img, excerpt, story, facts, cut, date):
    body = J(para(story, fontSize='large'), specs([tuple(f) for f in facts]))
    if cut:
        body = J(body, heading('Cut list', 4), cutlist(cut),
                 heading('In the workshop', 4),
                 gallery([('shavings.jpg', 'A hand plane among curled shavings', 'Planed by hand'), ('clamps.jpg', 'Clamps holding a glued frame', 'Glue-up'),
                          ('timber.jpg', 'Boards stacked with spacers in a yard', 'The boards before')], columns=3),
                 buttons(('Ask about a piece like this', '/commissions/')))
    return {'title': title, 'category': cat, 'image': img, 'excerpt': excerpt, 'date': date, 'content': body}


POSTS = [
    piece('Six ladder-back chairs, ash and rush', 'chairs', 'chair2.jpg', 'For a kitchen table in Deventer. Steam-bent back legs, hand-woven rush seats.',
          'The drawing we worked from, a 1937 study of a country ladder-back, belongs to the owner\'s grandmother. We kept the proportions and made the back slats a little wider for modern backs.',
          [['Timber', 'Ash from a dieback felling near Lochem'], ['Seat', 'Rush, woven by Hanneke Vos in Epe'], ['Finish', 'Linseed oil'], ['Time', '3 weeks a chair'], ['Price', '€1,150 each']],
          [['Back legs, steam-bent', '2', 'Ash', '1020 × 38 × 38'], ['Front legs', '2', 'Ash', '450 × 38 × 38'], ['Back slats', '4', 'Ash', '400 × 60 × 10'], ['Stretchers', '8', 'Ash', '420 × 22 dia.']], '2026-09-05'),
    piece('Rocking chair, cherry', 'chairs', 'chair.jpg', 'A Shaker-pattern rocker with a woven tape seat.',
          'Kofi drew it full size on a sheet of plywood first, rockers included, because a rocker that is a few degrees off tips you out or rocks you to sleep too fast.',
          [['Timber', 'Cherry from a sawmill near Gent'], ['Seat', 'Cotton tape, woven in the workshop'], ['Finish', 'Hardwax oil'], ['Time', '5 weeks'], ['Price', '€2,300']],
          [['Rockers', '2', 'Cherry', '820 × 110 × 28'], ['Back posts', '2', 'Cherry', '1080 × 38 × 38'], ['Slats', '3', 'Cherry', '390 × 70 × 9']], '2026-07-18'),
    piece('Joined chest, after a 1670s original', 'cabinets-and-chests', 'chest.jpg', 'A copy of a carved oak chest the client saw in a museum.',
          'The client fell for a 17th-century chest from Ipswich, Massachusetts, in a museum and asked whether it could be made again. It could, slowly: the carving alone took Sanne four weeks. The photo shows the original.',
          [['Timber', 'Riven oak from a single Achterhoek log'], ['Joints', 'Mortise and tenon, pegged, no glue'], ['Finish', 'Linseed oil and wax'], ['Time', '12 weeks'], ['Price', '€7,800']],
          [['Stiles', '4', 'Oak, riven', '760 × 90 × 45'], ['Rails', '6', 'Oak', '1150 × 100 × 28'], ['Panels', '6', 'Oak, riven', '360 × 280 × 15'], ['Lid boards', '2', 'Oak', '1250 × 270 × 20']], '2026-05-30'),
    piece('Piano stool, rebuilt', 'repairs', 'stool.jpg', 'A 1900s adjustable piano stool with a split top and a stripped thread.',
          'We take in one or two repairs a season, when the piece deserves it. This one needed a new walnut top glued up from three boards and a new wooden screw cut on the lathe.',
          [['Work', 'New top, new screw thread, legs reglued'], ['Timber', 'Walnut for the top'], ['Finish', 'Shellac, as the original'], ['Price', '€480']], None, '2026-04-12'),
    piece('A glue-up, in pictures', 'workshop-notes', 'clamps.jpg', 'Twelve clamps, a timer and ten minutes before the glue skins over.',
          'Gluing up a door frame or a table top is the one part of the job where nobody talks. Everything is dry-fitted twice, clamps are set to width, and then it is ten minutes of work and a day of waiting.',
          [['Glue', 'Hide glue for chairs, so they can be taken apart; PVA for tops'], ['Clamps', 'We own 64 and it is never enough']], None, '2026-03-20'),
    piece('The cupboard in Nuremberg', 'workshop-notes', 'cabinet.jpg', 'A study trip to look at an ash and oak cupboard from about 1600.',
          'Sanne spent two days in the Fembohaus in Nuremberg drawing this cupboard. The panels float in their frames exactly as ours do. Four hundred years later, none of them has split.',
          [['Where', 'Stadtmuseum Fembohaus, Nuremberg'], ['Date of the cupboard', 'About 1600'], ['Timber', 'Ash and oak']], None, '2026-02-02'),
    piece('Buying elm on the IJssel', 'workshop-notes', 'timber.jpg', 'How a diseased tree becomes a chair seat, and why it takes three years.',
          'Every winter the council fells the elms that died of Dutch elm disease over the summer. We buy the best butts, have them milled at a sawmill in Voorst and stack the boards in the shed. The photo is a much bigger yard, a century ago.',
          [['Bought this winter', '4 logs, about 6 cubic metres'], ['Ready to use', 'Winter 2029']], None, '2026-01-10'),
    piece('Why we still cut dovetails by hand', 'workshop-notes', 'shavings.jpg', 'A router is faster. We use one for grooves. Drawers get hand-cut dovetails.',
          'A hand-cut dovetail can be spaced to suit the drawer, and the pins can be as thin as a pencil line. It takes Sanne about 40 minutes a corner. We think drawers are the one place people really look.',
          [['Time per drawer', 'About three hours, four corners'], ['Tools', 'A dovetail saw, chisels, a marking gauge and a block plane']], None, '2025-11-15'),
]

content = {
    'site': {'title': 'Brink & Oduya', 'tagline': 'Furniture makers in Zutphen'},
    'categories': [{'slug': 'chairs', 'name': 'Chairs'}, {'slug': 'cabinets-and-chests', 'name': 'Cabinets and chests'},
                   {'slug': 'repairs', 'name': 'Repairs'}, {'slug': 'workshop-notes', 'name': 'Workshop notes'}],
    'front_page': 'home', 'posts_page': 'pieces',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'pieces', 'title': 'Pieces', 'content': ''},
        {'slug': 'commissions', 'title': 'Commissions', 'pattern': 'grain/commissions-page'},
        {'slug': 'timber', 'title': 'Timber and finishes', 'pattern': 'grain/timber-page', 'template': 'page-wide'},
        {'slug': 'workshop', 'title': 'The workshop', 'pattern': 'grain/workshop-page', 'template': 'page-wide'},
        {'slug': 'care', 'title': 'Care and guarantee', 'pattern': 'grain/care-page'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'grain/contact-page', 'template': 'page-wide'},
        {'slug': 'ready-now', 'title': 'Ready now', 'pattern': 'grain/ready-now', 'template': 'page-wide'},
    ],
    'posts': POSTS,
    'nav': [{'label': 'Pieces', 'url': '/pieces/'}, {'label': 'Commissions', 'url': '/commissions/'}, {'label': 'Timber and finishes', 'url': '/timber/'},
            {'label': 'Workshop', 'url': '/workshop/'}, {'label': 'Care', 'url': '/care/'}, {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/grain', exist_ok=True)
with open('demos/grain/content.json', 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
with open('demos/grain/fonts-claim.txt', 'w') as f:
    f.write('display: Sentient (Fontshare)\n')
with open('demos/grain/readme-extra.md', 'w') as f:
    f.write('''Grain is for one- or two-person workshops that make solid-wood furniture to commission. The front page opens with the order book: what is on each bench this week and when the next slot is free. Edit the "Order book" pattern every week or two, and the "Current lead time" pattern whenever the date moves.

Finished pieces are posts in the categories Chairs, Cabinets and chests, Repairs and Workshop notes. Give each a featured image, a short excerpt and a cut list (the "Cut list for a piece" pattern). Page patterns cover the commission timeline, prices, timber and finishes, the workshop and visits, care and the guarantee.''')
print('demo written')
