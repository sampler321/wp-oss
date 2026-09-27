# joint: furniture and object designer, editions and trade enquiries (idea 021)
# Direction: "workshop drawing sheet". Every page reads like a sheet from the makers' plan chest: measured drawings as
#   the product images, thin ruled frames, and a title block in the corner that carries timber, size and lead time.
# Fonts: Familjen Grotesk (registry face) for headings and labels, Newsreader for text. Two families only.
# Palette: planed ash #F5F1EA, pencil black #231F1A, oiled green #3E5641 for links and actions, shaving #E8E1D5, rule #BFB3A0.
# Layout idea: product and project pages split 7/5, drawing left and a boxed title block right (timber, W / D / H in
#   mm and inches, lead time, price), and the materials page is a swatch library of square timber samples.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
from blocks import _a
import blocks as _b
set_theme('joint')
S = THEME['slug']
D = THEME['dir']


def group(inner, tag='div', layout='constrained', **attrs):
    # The normaliser drops `layout` from a plain div group that also carries `style`; a section tag keeps it.
    if tag == 'div' and attrs.get('style') and layout and layout != {'type': 'default'}:
        tag = 'section'
    return _b.group(inner, tag=tag, layout=layout, **attrs)


PAL = [
    ('base', '#F5F1EA', 'Planed ash'),
    ('contrast', '#231F1A', 'Pencil'),
    ('accent', '#3E5641', 'Oiled green'),
    ('surface', '#E8E1D5', 'Shaving'),
    ('line', '#BFB3A0', 'Rule'),
    ('muted', '#5E564B', 'Graphite'),
    ('white', '#FFFFFF', 'Paper'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))
fam = {f['slug']: f for f in fonts['fontFamilies']}
fam['body']['fontFamily'] = '"Newsreader", serif'


def pal(rows):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]


def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d


LBL = 'font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-small);letter-spacing:.02em'
CSS = (':where(h1,h2,h3,h4){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
       '.wp-block-table,.is-style-label,.wc-block-components-product-price,.woocommerce-Price-amount{font-variant-numeric:tabular-nums lining-nums}'
       '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.55em .8em .55em 0;text-align:left;vertical-align:top}'
       '.wp-block-table thead{border:0}.wp-block-table th{' + LBL + ';font-weight:500;color:var(--wp--preset--color--muted)}'
       '.wp-block-table td:first-child{' + LBL + ';color:var(--wp--preset--color--muted)}'
       '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base)}'
       '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-underline-offset:.35em}'
       ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
       '.wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:0;background:var(--wp--preset--color--white)}'
       '.wc-block-components-button:not(.is-link),.wp-block-button__link.add_to_cart_button,.single_add_to_cart_button{background:var(--wp--preset--color--accent)!important;color:var(--wp--preset--color--white)!important;border-radius:0!important}'
       '.wc-block-components-product-sale-badge{border-radius:0;border:1px solid var(--wp--preset--color--contrast);background:var(--wp--preset--color--base)}'
       '.woocommerce-product-gallery img,.wc-block-components-product-image img{outline:1px solid var(--wp--preset--color--line);outline-offset:-1px}')

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '660px', 'wideSize': '1280px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'writingMode': False,
            'fontFamilies': [fam['display'], fam['body']],
            'fontSizes': [
                fs('x-small', '0.875rem', 'Label'),
                fs('small', '1rem', 'Small'),
                fs('medium', '1.1875rem', 'Body'),
                fs('large', '1.5rem', 'Large', '1.25rem'),
                fs('x-large', '2.25rem', 'Section', '1.75rem'),
                fs('xx-large', '3.25rem', 'Title', '2.3rem'),
                fs('display', '4.5rem', 'Display', '2.75rem'),
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False,
            'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'},
                {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'},
                {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2.25rem, 5vw, 3.5rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4rem, 10vw, 7.5rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'lineHeight': '1.05', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'fontWeight': '700'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2', 'letterSpacing': '-0.01em'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500', 'lineHeight': '1.4', 'letterSpacing': '0.02em'}, 'color': {'text': 'var:preset|color|muted'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|white'},
                'border': {'radius': '0', 'width': '0', 'style': 'none'},
                'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.7em', 'bottom': '0.7em', 'left': '1.2em', 'right': '1.2em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|white'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}},
            },
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.02em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small'}, 'elements': {'link': {'color': {'text': 'var:preset|color|muted'}}}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontStyle': 'italic', 'lineHeight': '1.35'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'fontStyle': 'italic', 'lineHeight': '1.2'},
                               'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    ],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Joint
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A shop and portfolio for furniture and object makers who sell small editions, take commissions and answer trade enquiries.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: joint
Tags: portfolio, e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')


def variation(fname, title, rows):
    write('styles/%s.json' % fname, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                                'settings': {'color': {'palette': pal(rows)}}}, indent='\t', ensure_ascii=False))


variation('oak', 'Oak', [('base', '#EFE7DA', 'Planed ash'), ('contrast', '#2A2016', 'Pencil'), ('accent', '#5A3E1B', 'Oiled green'),
                         ('surface', '#E2D7C4', 'Shaving'), ('line', '#BCA98C', 'Rule'), ('muted', '#5C4F3F', 'Graphite'), ('white', '#FFFFFF', 'Paper')])
variation('steel', 'Steel', [('base', '#E6E8EA', 'Planed ash'), ('contrast', '#2A2E33', 'Pencil'), ('accent', '#2F4A66', 'Oiled green'),
                             ('surface', '#D8DCE0', 'Shaving'), ('line', '#AEB5BC', 'Rule'), ('muted', '#4F565E', 'Graphite'), ('white', '#FFFFFF', 'Paper')])
variation('ebonised', 'Ebonised', [('base', '#1C1B19', 'Planed ash'), ('contrast', '#E9E2D6', 'Pencil'), ('accent', '#A8C29A', 'Oiled green'),
                                   ('surface', '#28261F', 'Shaving'), ('line', '#4A463D', 'Rule'), ('muted', '#B8AE9E', 'Graphite'), ('white', '#1C1B19', 'Paper')])


def section(slug, title, block_types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug,
                                                        'blockTypes': block_types, 'styles': styles}, indent='\t', ensure_ascii=False))


section('sheet', 'Drawing sheet frame', ['core/group', 'core/columns'], {
    'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('plate', 'Drawing plate', ['core/image', 'core/post-featured-image'], {
    'css': '&{border:1px solid var(--wp--preset--color--contrast);background:var(--wp--preset--color--white);padding:clamp(.5rem,1.5vw,1rem)}& img{display:block;width:100%}& figcaption{margin-bottom:0}'})
section('plate-portrait', 'Drawing plate, portrait', ['core/image'], {
    'css': '&{border:1px solid var(--wp--preset--color--contrast);background:var(--wp--preset--color--white);padding:clamp(.5rem,1.5vw,1rem)}& img{display:block;width:100%;aspect-ratio:4/5;object-fit:contain}'})
section('title-block', 'Title block', ['core/group', 'core/table'], {
    'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'color': {'background': 'var:preset|color|white'},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
    'css': '& .wp-block-table td{border-bottom:1px solid var(--wp--preset--color--line)}& .wp-block-table tr:last-child td{border-bottom:0}'})
section('shaving', 'Shaving panel', ['core/group', 'core/columns', 'core/media-text'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('green', 'Oiled green band', ['core/group'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|white'},
    'elements': {'link': {'color': {'text': 'var:preset|color|white'}}, 'heading': {'color': {'text': 'var:preset|color|white'}},
                 'button': {'color': {'background': 'var:preset|color|white', 'text': 'var:preset|color|accent'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}})
section('label', 'Drawing label', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'letterSpacing': '0.02em', 'lineHeight': '1.4'},
    'color': {'text': 'var:preset|color|muted'}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('swatch', 'Timber swatch', ['core/image'], {
    'css': '& img{aspect-ratio:1;object-fit:cover;outline:1px solid var(--wp--preset--color--contrast);outline-offset:-1px}'})
section('two-up-mobile', 'Two columns on phones', ['core/group'], {
    'css': '@media (max-width:600px){&{grid-template-columns:1fr 1fr!important}}'})
section('lead-time', 'Lead time note', ['core/group'], {
    'border': {'left': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}},
    'spacing': {'padding': {'left': 'var:preset|spacing|30', 'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10'}},
    'typography': {'fontSize': 'var:preset|font-size|small'}})


def label(t, **kw):
    return para(t, className='is-style-label', **kw)


# ---------------------------------------------------------------- parts
write('parts/header.html', group(
    row(J(row(J(dyn('site-title', level=0), label('Furniture workshop, Hebden Bridge')), style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
          dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')), justify='space-between', align='wide'),
    tag='header', align='full',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}, 'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}}))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(para('Brook &amp; Lathe', fontSize='x-large', fontFamily='display'),
                  para('Chairs, tables and cabinets made to order in British hardwood by Tamsin Hale and Olek Brzeziński, in a weaving shed on the Rochdale Canal.', fontSize='small'))),
        (None, J(heading('Workshop', 6),
                 para('Unit 3, Mytholm Works<br>Hebden Bridge HX7 6DL<br>Visits by appointment, Thursday and Friday', fontSize='small'))),
        (None, J(heading('Ask', 6),
                 para('<a href="mailto:workshop@example.com">workshop@example.com</a><br>01422 555 014<br><a href="/commission/">Commissions and trade</a><br><a href="/aftercare/">Aftercare and guarantee</a>', fontSize='small'))),
        align='wide'),
    label('Demo images are CC0 drawings from the National Gallery of Art Index of American Design and photos from Wikimedia Commons, used as stand-ins.', align='wide')),
    tag='footer', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': 'var:preset|spacing|70'}},
                                        'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}}))

# ---------------------------------------------------------------- patterns
IMG = {
    'desk': 'Measured drawing of a writing desk, front and side elevations with dimension lines',
    'table': 'Measured drawing of a small table from above, from the side and from the end, with dimensions in inches',
    'chair': 'Watercolour drawing of a green painted spindle-back chair',
    'chair-2': 'Watercolour drawing of a spindle-back chair in pale wood with a saddle seat',
    'bench': 'Drawing of a long plank bench with shaped trestle ends',
    'cabinet': 'Drawing of an oak court cupboard with turned columns and carved panels',
    'stool': 'Drawing of a one-legged milking stool with a worn wooden seat and a green painted leg',
    'hero': 'A maker fixing the back rail of a wooden chair frame in an open workshop',
    'workshop': 'An old joinery workshop with hand planes on shelves above a long bench and a chest of drawers',
    'sawmill': 'Black and white photograph of stacked timber planks in a sawmill yard, with men standing on a stack',
}
TIMBERS = [('oak', 'English oak', 'Quartersawn, from Herefordshire', 'Our default. Goes honey-coloured in a year.'),
           ('ash', 'Ash', 'From a sawmill in Settle', 'Pale and springy. Good for chair spindles.'),
           ('cherry', 'Cherry', 'Kent, air-dried four years', 'Darkens to red-brown in sunlight.'),
           ('elm', 'Elm', 'Salvaged, Yorkshire Dales', 'Wild grain, every board different.'),
           ('sycamore', 'Sycamore', 'Calderdale, felled for safety', 'Nearly white. Takes soap finish well.'),
           ('beech', 'Beech', 'Chilterns', 'Hard, plain, used for drawer runners.'),
           ('larch', 'Larch', 'Kielder', 'Knotty softwood for outdoor benches.'),
           ('chestnut', 'Sweet chestnut', 'Sussex coppice', 'Outdoor use, weathers silver.')]


def title_block(rows, price=None):
    t = table(rows)
    return group(J(t, para(price, fontSize='large', fontFamily='display')) if price else t, className='is-style-title-block')


CALDER = [['Timber', 'English oak, cherry or elm'], ['W / D / H', '480 / 520 / 800 mm<br>18.9 / 20.5 / 31.5 in'], ['Seat height', '450 mm, 17.7 in'],
          ['Finish', 'Hardwax oil or soap'], ['Lead time', 'Made to order, 8 to 10 weeks']]

# Signature: product sheet
pattern('product-sheet', 'Product sheet: drawing and title block', 'featured,shop', columns(
    ('58%', image('chair-2.jpg', IMG['chair-2'], 'Calder chair, drawn at 1:5 before the first one was made', className='is-style-plate')),
    (None, J(label('Chairs'), heading('Calder chair', 1, fontSize='xx-large'),
             para('A spindle-back dining chair with a carved saddle seat. Seven spindles, steam-bent back rail, no screws or metal anywhere.'),
             title_block(CALDER),
             pattern_ref('timber-prices'),
             buttons(('Order a Calder chair', '/shop/'), ('Ask about another size', '/commission/', {'className': 'is-style-outline'})))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    description='The product page layout: a drawing or photo at 7/12, and the facts in a boxed title block at 5/12.')

pattern('timber-prices', 'Price per timber', 'shop', table(
    [['English oak', '£1,450'], ['Cherry', '£1,650'], ['Elm', '£1,720']], head=['Timber', 'Price each']))

pattern('dimensions', 'Dimensions in mm and inches', 'shop', table(
    [['Width', '480 mm', '18.9 in'], ['Depth', '520 mm', '20.5 in'], ['Height', '800 mm', '31.5 in'], ['Seat height', '450 mm', '17.7 in'], ['Weight', '5.8 kg', '12.8 lb']],
    head=['', 'mm', 'inches']))

pattern('lead-time', 'Lead time: in stock and made to order', 'shop', J(
    group(para('<strong>In stock.</strong> Ships in 1 to 5 working days from Hebden Bridge.'), className='is-style-lead-time'),
    group(para('<strong>Made to order.</strong> 6 to 12 weeks, depending on the timber. We send photos when it is glued up.'), className='is-style-lead-time')),
    description='Use the first line for pieces in the in-stock list and the second for everything else.')

pattern('made-to-size', 'Can be made to your size', 'shop', para('Most of our pieces can be made to your size. Tables and desks up to 2.4 metres long, benches up to 3 metres. Ask for a price; it is usually 10 to 15% more than the standard size.', fontSize='small'))

pattern('care', 'Care and guarantee', 'text', group(J(
    heading('Care', 4),
    lst(['Wipe with a damp cloth. No sprays with silicone in them.',
         'Oiled pieces: a thin coat of hardwax oil once a year, or when water stops beading.',
         'Soaped pieces: a flake soap wash twice a year. We send a bag of soap flakes with every soaped piece.',
         'Keep it a metre from radiators and out of all-day sun for the first month.']),
    heading('Ten years, and after that', 4),
    para('Every joint is guaranteed for ten years. If one loosens, we fix it at the workshop for free. After ten years we still refinish and repair our own furniture at cost.')),
    className='is-style-rule-top'))

pattern('source-book', 'Material source book (timber swatch library)', 'featured', group(J(
    row(J(heading('Timbers we use', 2), para('Every board comes from a named sawmill within about 250 miles of the workshop.', fontSize='small')), justify='space-between', align='wide'),
    grid(J(*[stack(J(image(f + '.jpg', 'Square sample of planed %s, showing its grain' % n.lower(), className='is-style-swatch', lightbox=False),
                     heading(n, 4), label(src), para(note, fontSize='small')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}})
             for f, n, src, note in TIMBERS]), min_width='15rem', align='wide', className='is-style-two-up-mobile')),
    align='wide', layout={'type': 'default'}), description='The signature swatch library: each timber as a square sample with its source and one line on how it behaves.')

pattern('finishes', 'Finishes', 'text', group(J(
    heading('Finishes', 3),
    table([['Hardwax oil', 'Matt, easy to touch up. Our default.', 'All timbers'],
           ['Soap', 'Very pale and dry to the touch. Needs a wash twice a year.', 'Oak, ash, sycamore'],
           ['Fumed', 'Oak darkened with ammonia to a deep brown, then oiled.', 'Oak only'],
           ['Ebonised', 'Iron and vinegar on oak. Near black, grain still visible.', 'Oak only, plus £180']],
          head=['Finish', 'What it looks like', 'On'])), align='wide', layout={'type': 'constrained', 'contentSize': '960px'}))

pattern('complementary-materials', 'Complementary materials', 'text', group(J(
    heading('Also in the workshop', 4),
    para('Seat rush from the Somerset Levels, Danish cord, undyed wool webbing from Laxtons in Guiseley, vegetable-tanned leather for drawer pulls, and brass only where a hinge has to be brass.')),
    className='is-style-rule-top'))

pattern('visit-to-see-timbers', 'Visit the workshop to see the timbers', 'call-to-action', group(J(
    heading('Come and see the wood', 3),
    para('Pictures of timber are nearly useless. Book an hour at the workshop on a Thursday or Friday and you can handle every species, sit on the chairs and see offcuts of the boards your piece would come from.'),
    buttons(('Book a workshop visit', 'mailto:workshop@example.com?subject=Workshop%20visit'))), className='is-style-shaving', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('materials-page', 'Page: materials', 'featured', J(
    pattern_ref('source-book'), spacer('var:preset|spacing|60'), pattern_ref('finishes'), pattern_ref('complementary-materials'), pattern_ref('visit-to-see-timbers')),
    block_types='core/post-content')

pattern('hero-drawing', 'Hero: measured drawing and title block', 'featured', columns(
    ('62%', image('desk.jpg', IMG['desk'], 'Aire writing desk, front and side elevations, drawn by Tamsin, 2024', className='is-style-plate', lightbox=False)),
    (None, J(heading('Furniture drawn, then made, in Hebden Bridge', 1, fontSize='xx-large'),
             para('Tamsin Hale and Olek Brzeziński make chairs, tables and cabinets from British hardwood. A few pieces are always in stock. Everything else is made to order in 6 to 12 weeks.'),
             title_block([['Workshop', 'Mytholm Works, Hebden Bridge'], ['Made since', '2014'], ['Timbers', 'Eight, all British'], ['Guarantee', 'Ten years on every joint']]),
             buttons(('See what is in stock', '/in-stock/'), ('How commissions work', '/commission/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|50'}}}))

COLLECTION = [('chair-2.jpg', 'Calder chair', 'Oak, cherry or elm', 'From £1,450'), ('table.jpg', 'Heptonstall side table', 'Oak or cherry', 'From £890'),
              ('bench.jpg', 'Crag bench', 'Elm or larch', 'From £1,100'), ('cabinet.jpg', 'Mytholm cupboard', 'Fumed oak', '£4,800'),
              ('desk.jpg', 'Aire writing desk', 'Oak or cherry', 'From £2,950'), ('stool.jpg', 'Pecket stool', 'Ash and sycamore', '£280')]

pattern('collection', 'Collection (drawing grid with prices)', 'shop', group(J(
    row(J(heading('The collection', 2), para('<a href="/shop/">Shop everything</a>')), justify='space-between', align='wide'),
    grid(J(*[stack(J(image(f, IMG[f[:-4]], href='/shop/', className='is-style-plate-portrait'),
                     row(J(heading('<a href="/shop/">%s</a>' % n, 4), para(p, fontSize='small', fontFamily='display')), justify='space-between'),
                     label(t)), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}) for f, n, t, p in COLLECTION]), min_width='22rem', align='wide', className='is-style-two-up-mobile')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70'}}}))

pattern('in-stock', 'In stock now (ruled list)', 'shop', group(J(
    heading('In stock now', 2),
    para('Finished pieces waiting in the workshop. They ship in 1 to 5 working days, or you can collect.'),
    table([['Calder chair', 'English oak, hardwax oil', '480 / 520 / 800 mm', '£1,450', '4 left'],
           ['Calder chair', 'Elm, soap finish', '480 / 520 / 800 mm', '£1,720', '2 left'],
           ['Pecket stool', 'Ash and sycamore', '300 / 300 / 460 mm', '£280', '6 left'],
           ['Heptonstall side table', 'Cherry, hardwax oil', '450 / 450 / 560 mm', '£890', '1 left'],
           ['Crag bench, 1.8 m', 'Larch, unfinished for outdoors', '1800 / 380 / 450 mm', '£1,100', '1 left']],
          head=['Piece', 'Timber and finish', 'W / D / H', 'Price', 'Stock']),
    pattern_ref('lead-time')), align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}))

pattern('in-stock-page', 'Page: in stock', 'shop', J(pattern_ref('in-stock'), spacer('var:preset|spacing|60'), pattern_ref('shipping-rates')), block_types='core/post-content')

pattern('shipping-rates', 'Delivery rates', 'shop', group(J(
    heading('Delivery', 3),
    table([['Collect from the workshop', 'Free'], ['Our van, within 60 miles', '£60'], ['Two-person courier, mainland UK', '£120 to £240'], ['EU, crated', 'Quoted, usually £380 to £650']], head=['How', 'Cost']),
    para('Delivery costs are shown in the basket before you pay. We do not ship outside the UK and EU.', fontSize='small')), layout={'type': 'constrained'}))

pattern('commission-process', 'Commission process', 'services', group(J(
    heading('How a commission works', 2),
    columns(*[(None, J(heading(h, 4), para(t), label(d))) for h, t, d in [
        ('Concept', 'We talk, measure the room and look at what you already own. Then we send sketches and a fixed price.', 'Free, about two weeks'),
        ('Development', 'We draw it properly at 1:5 and, for chairs, make a rough mock-up in pine for you to sit in. A 40% deposit starts this.', 'Two to four weeks'),
        ('Fabrication', 'We choose the boards with you if you want, then make it. You get photos at glue-up and before finishing.', 'Six to ten weeks')]],
        align='wide', className='is-style-rule-top')), align='wide', layout={'type': 'default'}))

pattern('commission-page', 'Page: commission', 'services', J(
    pattern_ref('commission-process'), spacer('var:preset|spacing|60'),
    columns((None, pattern_ref('trade-enquiries')), (None, pattern_ref('commission-faq')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    block_types='core/post-content')

pattern('commission-faq', 'Commission questions', 'text', J(
    heading('Questions', 4),
    details('What does a commission cost?', para('A dining table starts around £3,800 and a set of six chairs around £9,000. Small cabinets from £2,400. We give a fixed price after the first meeting.')),
    details('Can you copy a piece I have seen elsewhere?', para('No. We are happy to start from something you like, but we will not copy another maker’s design.')),
    details('Do you work with interior designers?', para('Yes, about a third of our work comes through designers. See trade enquiries.')),
    details('Can I supply my own timber?', para('Sometimes. If it is a tree from your own land, we can arrange milling and two years of drying.'))))

pattern('trade-enquiries', 'Trade enquiries', 'services', group(J(
    heading('Trade enquiries', 3),
    para('Designers, architects and shops get 12% off the collection and a named contact in the workshop. We make up to twelve chairs of one design a month, or one long table.'),
    lst(['Send the project name, the pieces and quantities, and your deadline.',
         'We reply with prices, lead times and CAD blocks within three working days.',
         'Samples of each timber and finish are free for trade, posted in a wooden box.']),
    buttons(('Email a trade enquiry', 'mailto:trade@example.com?subject=Trade%20enquiry'))), className='is-style-sheet'))

pattern('workshop-courses', 'Workshop courses', 'services', columns(
    ('45%', image('workshop.jpg', IMG['workshop'], 'The bench room, where the courses run')),
    (None, J(heading('Make a stool in two days', 3),
             para('Four people at a time, Saturday and Sunday, 9.30am to 5pm. You make a three-legged ash stool with a riven seat and go home with it. Lunch is soup from the café next door.'),
             table([['Next dates', '18 and 19 October, 15 and 16 November 2026'], ['Price', '£340, all timber and tools included'], ['Places', '4 per course'], ['Suitable for', 'Anyone over 16. No experience needed.']]),
             buttons(('Book a place by email', 'mailto:workshop@example.com?subject=Stool%20course')))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('workshop-page', 'Page: workshop', 'about', J(
    pattern_ref('about-makers'), spacer('var:preset|spacing|60'), pattern_ref('workshop-courses'), spacer('var:preset|spacing|60'), pattern_ref('sustainability')), block_types='core/post-content')

pattern('about-makers', 'About the makers', 'about', columns(
    (None, J(heading('Two people and a weaving shed', 2),
             para('Tamsin Hale trained at Rycotewood and spent six years making chairs for other people. Olek Brzeziński grew up in his father’s joinery in Nowy Targ and came to Yorkshire to build boats. They set up in Mytholm Works in 2014, in a shed that used to hold forty looms.'),
             para('Tamsin draws everything by hand at 1:5 before any wood is cut. Olek says this is slower. He is right, and we still do it.'))),
    (None, image('hero.jpg', IMG['hero'], 'Olek fitting a back rail on a chair frame')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('sustainability', 'Where the wood comes from', 'about', media_text('sawmill.jpg', IMG['sawmill'], J(
    heading('Where the wood comes from', 3),
    para('We buy from four small sawmills and one tree surgeon, all named on the materials page. Nothing comes from further than 250 miles. Offcuts go to the stool course, then to a wood-burning bakery in Todmorden.'),
    para('<a href="/materials/">See every timber we use</a>')), width=45, className='is-style-shaving', align='wide'))

pattern('aftercare-page', 'Page: aftercare and shipping', 'text', J(pattern_ref('care'), pattern_ref('refinishing'), pattern_ref('shipping-rates')), block_types='core/post-content')

pattern('refinishing', 'Refinishing service', 'services', group(J(
    heading('Refinishing', 4),
    para('Ring marks, dog scratches, a chair that has been sat on backwards for ten years: bring it in and we sand, refinish and re-glue it. From £90 for a chair, £240 for a dining table top.')),
    className='is-style-rule-top'))

pattern('collaborations', 'Collaborations list', 'about', group(J(
    heading('Made with other people', 3),
    table([['2025', 'Twelve chairs for Hepworth Wakefield learning studio', 'With Hepworth Wakefield'],
           ['2024', 'Reading-room tables for Todmorden library', 'With Calderdale Council'],
           ['2023', 'The Crag bench, a limited run of 30', 'With Pennine Prospects'],
           ['2022', 'Rush-seated stools', 'With Felicity Irons, rush weaver']], head=['Year', 'What', 'With']))))

pattern('project-sheet', 'Project page: drawing, story and credits', 'featured', J(
    columns(('58%', J(para('Eight reading tables for the reference room of Todmorden library, replacing laminate desks from 1978. Built in cherry so they would darken to match the old oak panelling.', fontSize='large'),
                      para('The brief said the tables had to survive schoolchildren. We used drawbored mortise and tenons, no metal fixings, and a thick top that can be sanded back at least five times.'))),
            (None, title_block([['Client', 'Calderdale Council'], ['Timber', 'Cherry, hardwax oil'], ['Size', '1800 / 900 / 740 mm each'], ['Finished', 'May 2024']])),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})))

PROJECT_ITEM = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='contain', className='is-style-plate'),
                 row(J(dyn('post-terms', term='category'), dyn('post-date', format='Y')), justify='space-between'),
                 dyn('post-title', isLink=True, level=3, fontSize='large'))

pattern('projects-grid', 'Projects: latest', 'query', group(J(
    row(J(heading('Recent projects', 2), para('<a href="/projects/">All projects</a>')), justify='space-between', align='wide'),
    query(PROJECT_ITEM, per_page=3, query_id=31, align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70'}}}))

pattern('projects-archive', 'Projects archive (inherits the page query)', 'query', inherit_query(PROJECT_ITEM, align='wide',
        layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}), inserter=False)

pattern('green-cta', 'Band: commissions open', 'call-to-action', group(J(
    heading('Commission slots for spring 2027 are open', 2, fontSize='x-large'),
    para('We take on about fourteen commissions a year. Three spring slots are left, and one of them is probably a long table.'),
    buttons(('Start a commission', '/commission/'))), className='is-style-green', align='full', layout={'type': 'constrained'}))

pattern('post-list', 'Search results list', 'query', inherit_query(
    group(columns(('22%', dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover')), (None, J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30)))),
          className='is-style-rule-top'), align='wide'), inserter=False)

# ---------------------------------------------------------------- templates
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('hero-drawing'), pattern_ref('collection'), pattern_ref('source-book'), pattern_ref('projects-grid')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|70'}}),
    spacer('var:preset|spacing|70'), pattern_ref('green-cta'), template_part('footer', 'footer')))

write('templates/home.html', page_template(J(
    heading('Projects', 1, align='wide'),
    para('Commissions and collaborations, newest first. Each one has the drawing, the timber and who it was for.', align='wide', fontSize='large'),
    spacer('var:preset|spacing|40'), pattern_ref('projects-archive'), spacer('var:preset|spacing|60'), pattern_ref('collaborations')),
    layout={'type': 'constrained'}, style=MAINPAD))
write('templates/index.html', open(os.path.join(D, 'templates/home.html')).read())

write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', level=1),
    dyn('term-description', align='wide'), pattern_ref('projects-archive')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide', level=1),
    dyn('search', label='Search', showLabel=False, buttonText='Search', align='wide'),
    pattern_ref('post-list')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/404.html', page_template(J(
    heading('Not on this sheet', 1),
    para('That page is not here. It may have been a piece we no longer make.', fontSize='large'),
    dyn('search', label='Search', showLabel=False, buttonText='Search'),
    buttons(('Go to the shop', '/shop/'))), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/single.html', J(template_part('header', 'header'), group(J(
    columns(('58%', dyn('post-featured-image', aspectRatio='4/3', scale='contain', className='is-style-plate')),
            (None, J(dyn('post-terms', term='category'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', showMoreOnPage=False), dyn('post-date', format='F Y'))),
            align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    dyn('post-content', layout={'type': 'constrained'}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous project', showTitle=True),
            dyn('post-navigation-link', label='Next project', showTitle=True)),
          align='wide', className='is-style-rule-top', layout={'type': 'flex', 'justifyContent': 'space-between'})),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|50', 'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|60'}}}),
    template_part('footer', 'footer')))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1),
    dyn('post-content', layout={'type': 'constrained'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1),
    spacer('var:preset|spacing|40'),
    dyn('post-content', layout={'type': 'constrained', 'contentSize': '1000px'})), layout={'type': 'constrained', 'contentSize': '1000px'}, style=MAINPAD))

print('joint built')
