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
import shutil
for _d in ('patterns', 'templates', 'parts', 'styles'):
    shutil.rmtree(os.path.join(D, _d), ignore_errors=True)  # rebuilt below; drops stale files


group = _b.group


def columns(*cols, **attrs):
    """core/columns with the classes WordPress saves for verticalAlignment and isStackedOnMobile."""
    extra = []
    if attrs.get('verticalAlignment'):
        extra.append('are-vertically-aligned-' + attrs['verticalAlignment'])
    if attrs.get('isStackedOnMobile') is False:
        extra.append('is-not-stacked-on-mobile')
    out = _b.columns(*cols, **attrs)
    return out.replace('class="wp-block-columns', 'class="wp-block-columns ' + ' '.join(extra), 1) if extra else out


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
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
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


section('dimension', 'Dimension callout', ['core/group'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20'}},
    'css': '& .is-style-big-number{margin:0}'})
section('big-number', 'Big number', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '700', 'lineHeight': '1', 'letterSpacing': '-0.03em'},
    'css': '&{font-variant-numeric:tabular-nums lining-nums}'})
section('spec-row', 'Spec row', ['core/group', 'core/columns'], {
    'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}})
section('step', 'Making step', ['core/group'], {
    'css': '&{counter-increment:step}& > .wp-block-heading::before{content:counter(step) ". ";color:var(--wp--preset--color--accent)}'})
section('steps', 'Making steps', ['core/group'], {'css': '&{counter-reset:step}'})
section('chip', 'Timber chip', ['core/image'], {
    'css': '&{margin:0}& img{width:3rem;height:3rem;object-fit:cover;border-radius:50%;outline:1px solid var(--wp--preset--color--contrast)}'})


def label(t, **kw):
    return para(t, className='is-style-label', **kw)



# ---------------------------------------------------------------- functions.php (pattern categories only)
CATS = [('object', 'Object pages'), ('pieces', 'Pieces and shop'), ('hero', 'Heroes'), ('making', 'Materials and making'), ('services', 'Commissions and trade'),
        ('about', 'Workshop and makers'), ('projects', 'Projects'), ('contact', 'Visit and contact'), ('page', 'Page layouts')]
write('functions.php', "<?php\n/**\n * Joint: registers the pattern categories used by the theme's patterns.\n *\n * @package joint\n */\n\nadd_action(\n\t'init',\n\tfunction () {\n"
      + ''.join("\t\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', 'joint' ) ) );\n" % c for c in CATS) + "\t}\n);\n")

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
    label('Demo images are CC0 drawings from the National Gallery of Art Index of American Design, public domain engravings and photos from Wikimedia Commons, used as stand-ins.', align='wide')),
    tag='footer', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': 'var:preset|spacing|70'}},
                                        'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}}))

# ---------------------------------------------------------------- data
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
    'dovetail': 'Engraving of the two halves of a dovetail joint, pulled apart to show the tails and pins',
    'shavings': 'A hand plane lying on a board with curled wood shavings around it',
    'lathe': 'Old photograph of a wood turner working at a low lathe, surrounded by shavings',
    'inuse': 'A sitting room from 1905 with a spindle-back Windsor chair beside a window and a table with a lamp',
    'planes': 'Engraved plate of wooden hand planes of different lengths and shapes',
    'holdfast': 'Engraving of an iron bench holdfast, the clamp that holds wood to the bench',
}
IMGPATH = '/wp-content/themes/joint/assets/images/'
TIMBERS = [('oak', 'English oak', 'Quartersawn, from Herefordshire', 'Our default. Goes honey-coloured in a year.'),
           ('ash', 'Ash', 'From a sawmill in Settle', 'Pale and springy. Good for chair spindles.'),
           ('cherry', 'Cherry', 'Kent, air-dried four years', 'Darkens to red-brown in sunlight.'),
           ('elm', 'Elm', 'Salvaged, Yorkshire Dales', 'Wild grain, every board different.'),
           ('sycamore', 'Sycamore', 'Calderdale, felled for safety', 'Nearly white. Takes soap finish well.'),
           ('beech', 'Beech', 'Chilterns', 'Hard, plain, used for drawer runners.'),
           ('larch', 'Larch', 'Kielder', 'Knotty softwood for outdoor benches.'),
           ('chestnut', 'Sweet chestnut', 'Sussex coppice', 'Outdoor use, weathers silver.')]
TNAME = {t[0]: t[1] for t in TIMBERS}

PIECES = [
    dict(slug='calder-chair', name='Calder chair', kind='Chair', img='chair-2.jpg', price='From £1,450', short='A spindle-back dining chair with a carved saddle seat. Seven spindles, a steam-bent back rail, no screws or metal anywhere.',
         dims=[('W', '480', '18.9'), ('D', '520', '20.5'), ('H', '800', '31.5'), ('Seat', '450', '17.7')], weight='5.8 kg',
         timbers=[('oak', '£1,450', 'In stock, ships in 1 to 5 days'), ('cherry', '£1,650', 'Made to order, 8 to 10 weeks'), ('elm', '£1,720', 'Two in stock')],
         story='Tamsin drew the Calder in 2019 for a dining table that already had six bad chairs round it. The seat is carved by hand with an adze and a travisher, so it fits the way people actually sit: slightly forward, elbows on the table.',
         details=[('dovetail.jpg', 'The seat is joined to the legs with wedged through-tenons, not dovetails, but it is the same idea: wood holding wood.'), ('shavings.jpg', 'Spindles are shaved from riven ash, following the grain.'), ('oak.jpg', 'Quartersawn English oak seat, oiled.')],
         specs=[('Joints', 'Wedged through-tenons, no glue blocks'), ('Finish', 'Hardwax oil or soap'), ('Spindles', 'Riven ash, shaved by hand'), ('Guarantee', 'Ten years on every joint')],
         inuse=('inuse.jpg', 'A Calder by the window. Chairs this plain look best in a room that is not.')),
    dict(slug='aire-writing-desk', name='Aire writing desk', kind='Desk', img='desk.jpg', price='From £2,950', short='A narrow desk for a gap between two windows. One drawer, a fall-front for letters, legs tapered on the inside faces only.',
         dims=[('W', '1000', '39.4'), ('D', '550', '21.7'), ('H', '760', '29.9')], weight='31 kg',
         timbers=[('oak', '£2,950', 'Made to order, 8 to 10 weeks'), ('cherry', '£3,250', 'Made to order, 10 to 12 weeks')],
         story='The Aire started as a commission for a flat in Leeds and we liked it too much to make only one. It can be made up to 150 mm narrower or wider without changing the proportions much.',
         details=[('dovetail.jpg', 'The drawer is hand dovetailed at the front and back.'), ('planes.jpg', 'Every surface is finished with a smoothing plane before oiling.'), ('cherry.jpg', 'Cherry, air-dried for four years in Kent.')],
         specs=[('Drawer', 'Hand dovetailed, lined in undyed felt'), ('Finish', 'Hardwax oil'), ('Made to size', 'From 850 to 1,150 mm wide'), ('Guarantee', 'Ten years on every joint')],
         inuse=('workshop.jpg', 'The second Aire, waiting for its drawer in the bench room')),
    dict(slug='heptonstall-side-table', name='Heptonstall side table', kind='Table', img='table.jpg', price='From £890', short='A small table with one drawer and a shaped stretcher, sized to sit beside a chair and hold a lamp, a book and a cup.',
         dims=[('W', '450', '17.7'), ('D', '450', '17.7'), ('H', '560', '22')], weight='7 kg',
         timbers=[('oak', '£890', 'Made to order, 6 weeks'), ('cherry', '£940', 'One in stock')],
         story='Named after the village on the hill above the workshop. The stretcher shape is traced from an old table in the Heptonstall Museum, which somebody had mended with a biscuit tin lid.',
         details=[('holdfast.jpg', 'The stretcher is sawn and spokeshaved with the leg held in a holdfast.'), ('shavings.jpg', 'Top planed by hand, then oiled.'), ('elm.jpg', 'Also made in elm on request.')],
         specs=[('Drawer', 'One, with a turned knob'), ('Finish', 'Hardwax oil'), ('Top', '22 mm solid, sanded back five times over its life')],
         inuse=('inuse.jpg', 'Side tables live next to chairs. This one sits beside a Calder.')),
    dict(slug='crag-bench', name='Crag bench', kind='Bench', img='bench.jpg', price='From £1,100', short='A long plank bench on trestle ends for gardens, halls and moorland footpaths. Left unfinished to weather silver.',
         dims=[('W', '1800', '70.9'), ('D', '380', '15'), ('H', '450', '17.7')], weight='24 kg',
         timbers=[('larch', '£1,100', 'One in stock'), ('chestnut', '£1,240', 'Made to order, 6 weeks'), ('oak', '£1,380', 'Made to order, 8 weeks')],
         story='We made thirty of these for footpaths above Heptonstall in 2023. People kept asking for one for their garden, so it is now in the collection, in three lengths.',
         details=[('larch.jpg', 'Kielder larch, knots and all.'), ('sawmill.jpg', 'Boards come straight from the sawmill and air-dry for a year.'), ('chestnut.jpg', 'Sweet chestnut, for benches that stay outside.')],
         specs=[('Lengths', '1.2, 1.8 and 2.4 m'), ('Finish', 'None, it weathers silver'), ('Fixings', 'Oak pegs, no metal')],
         inuse=('sawmill.jpg', 'Where Crag benches start: larch at the sawmill in Kielder')),
]
P1 = PIECES[0]


def img_(f, cap='', **kw):
    alt = IMG.get(f[:-4]) or ('Square sample of planed %s, showing its grain' % TNAME.get(f[:-4], 'timber').lower())
    return image(f, alt, cap, **kw)


# ---------------------------------------------------------------- object page blocks (functions + patterns)
def obj_hero(o, level=1):
    return J(img_(o['img'], '%s, drawn at 1:5 before the first one was made' % o['name'], align='wide', className='is-style-plate'),
             columns(('58%', J(label(o['kind']), heading(o['name'], level, fontSize='xx-large'), para(o['short'], fontSize='large'))),
                     (None, J(para(o['price'], fontSize='x-large', fontFamily='display'), buttons(('Buy or order it', '/shop/'), ('Ask for another size', '/commission/', {'className': 'is-style-outline'})),
                              group(para('Ten-year guarantee on every joint. Delivery by our own van within 60 miles.', fontSize='small'), className='is-style-lead-time'))),
                     align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))


def obj_callouts(o):
    cells = [group(J(label({'W': 'Width', 'D': 'Depth', 'H': 'Height', 'Seat': 'Seat height'}[k]), para(mm, className='is-style-big-number'), para('mm, %s in' % inch, fontSize='small')),
                   className='is-style-dimension') for k, mm, inch in o['dims']]
    cells.append(group(J(label('Weight'), para(o['weight'].split()[0], className='is-style-big-number'), para(o['weight'].split()[1], fontSize='small')), className='is-style-dimension'))
    return J(heading('Sizes', 3), group(J(*cells), align='wide', layout={'type': 'grid', 'minimumColumnWidth': '9rem'}))


def obj_details(o):
    return J(heading('Details', 3), gallery([(f, IMG.get(f[:-4]) or ('Square sample of %s' % TNAME.get(f[:-4], 'timber').lower()), c) for f, c in o['details']], columns=3, align='wide'))


def obj_inuse(o):
    f, cap = o['inuse']
    return img_(f, cap, align='full', className='is-style-plate')


def obj_timbers(o):
    rows = [columns(('10%', image(t + '.jpg', 'Sample of %s' % TNAME[t].lower(), className='is-style-chip', lightbox=False)), (None, J(heading(TNAME[t], 4), para(lead, fontSize='small'))),
                    ('22%', para(pr, fontSize='large', fontFamily='display')), className='is-style-spec-row', verticalAlignment='center', isStackedOnMobile=False) for t, pr, lead in o['timbers']]
    return J(heading('Timbers and prices', 3), group(J(*rows), layout={'type': 'default'}), para('<a href="/materials/">About each timber</a>', fontSize='small'))


def obj_specs(o):
    rows = [columns(('35%', label(a)), (None, para(b)), className='is-style-spec-row', isStackedOnMobile=False) for a, b in o['specs']]
    return J(heading('How it is made', 3), group(J(*rows), layout={'type': 'default'}))


def obj_story(o):
    return columns(('40%', heading('The story', 3)), (None, para(o['story'], fontSize='large')), align='wide')


def object_page(o, refs=False):
    if refs:
        return J(*[pattern_ref(x) for x in ['obj-hero', 'obj-details', 'obj-story', 'obj-in-use', 'obj-sizes', 'obj-timbers', 'obj-specs', 'making-strip', 'care', 'pieces-index']])
    return J(obj_hero(o), obj_details(o), obj_story(o), obj_inuse(o), obj_callouts(o),
             columns((None, obj_timbers(o)), (None, obj_specs(o)), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
             pattern_ref('care'), pattern_ref('pieces-index'))


OP = 'object'
pattern('obj-hero', 'Object: drawing first, then name and price', OP, obj_hero(P1), description='The object opens with the drawing or photo at full width. Name, price and actions follow.')
pattern('obj-details', 'Object: three details (lightbox)', OP, obj_details(P1))
pattern('obj-story', 'Object: the story of the piece', OP, obj_story(P1))
pattern('obj-in-use', 'Object: in use, full width', OP, obj_inuse(P1))
pattern('obj-sizes', 'Object: sizes as big dimension callouts', OP, obj_callouts(P1), description='Width, depth, height and weight set large, in mm with inches below.')
pattern('obj-timbers', 'Object: timbers and prices with samples', OP, obj_timbers(P1))
pattern('obj-specs', 'Object: how it is made', OP, obj_specs(P1))
pattern('obj-page', 'Page: object (full)', 'page', object_page(P1, refs=True), block_types='core/post-content',
        description='Drawing, details, story, in use, sizes, timbers, making, care and other pieces.')
pattern('obj-page-short', 'Page: object (short)', 'page', J(pattern_ref('obj-hero'), pattern_ref('obj-sizes'), pattern_ref('obj-timbers')), block_types='core/post-content')

pattern('dimensions', 'Spec sheet table (mm and inches)', OP, table(
    [['Width', '480 mm', '18.9 in'], ['Depth', '520 mm', '20.5 in'], ['Height', '800 mm', '31.5 in'], ['Seat height', '450 mm', '17.7 in'], ['Weight', '5.8 kg', '12.8 lb']],
    head=['', 'mm', 'inches']), description='A plain table for when a spec sheet is all you need, for example on a trade price list.')

pattern('lead-time', 'Lead time: in stock and made to order', OP, J(
    group(para('<strong>In stock.</strong> Ships in 1 to 5 working days from Hebden Bridge.'), className='is-style-lead-time'),
    group(para('<strong>Made to order.</strong> 6 to 12 weeks, depending on the timber. We send photos when it is glued up.'), className='is-style-lead-time')))

pattern('made-to-size', 'Can be made to your size', OP, group(J(
    heading('Made to your size', 4),
    para('Most of our pieces can be made to your size. Tables and desks up to 2.4 metres long, benches up to 3 metres. It usually costs 10 to 15% more than the standard size.'),
    buttons(('Ask for a size', '/commission/'))), className='is-style-sheet'))

pattern('care', 'Care and guarantee', OP, group(J(
    columns((None, J(heading('Care', 4),
                     lst(['Wipe with a damp cloth. No sprays with silicone in them.', 'Oiled pieces: a thin coat of hardwax oil once a year.',
                          'Soaped pieces: a flake soap wash twice a year. We send the soap.', 'Keep it a metre from radiators for the first month.']))),
            (None, J(heading('Ten years, and after that', 4),
                     para('Every joint is guaranteed for ten years. If one loosens, we fix it at the workshop for free. After ten years we still repair our own furniture at cost.'),
                     para('<a href="/aftercare/">Aftercare and refinishing</a>'))), align='wide')), className='is-style-rule-top', align='wide', layout={'type': 'default'}))

# ---------------------------------------------------------------- pieces and heroes
def piece_card(o, href=None):
    href = href or '/pieces/%s/' % o['slug']
    return stack(J(img_(o['img'], href=href, className='is-style-plate-portrait'),
                   row(J(heading('<a href="%s">%s</a>' % (href, o['name']), 4), para(o['price'], fontSize='small', fontFamily='display')), justify='space-between'),
                   label(', '.join(TNAME[t] for t, _, _ in o['timbers']))), style={'spacing': {'blockGap': 'var:preset|spacing|20'}})


EXTRA = [dict(slug='mytholm-cupboard', name='Mytholm cupboard', img='cabinet.jpg', price='£4,800', timbers=[('oak', '', '')]),
         dict(slug='pecket-stool', name='Pecket stool', img='stool.jpg', price='£280', timbers=[('ash', '', ''), ('sycamore', '', '')])]

pattern('pieces-index', 'Pieces: drawings with names and prices', 'pieces', group(J(
    row(J(heading('Pieces', 2), para('<a href="/shop/">Buy online</a>')), justify='space-between', align='wide'),
    grid(J(*[piece_card(o) for o in PIECES], *[piece_card(o, '/shop/') for o in EXTRA]), min_width='17rem', align='wide', className='is-style-two-up-mobile')),
    align='wide', layout={'type': 'default'}))

pattern('hero-piece', 'Hero: the newest piece, drawing first', 'hero', columns(
    ('62%', img_(P1['img'], 'Calder chair, 1:5 drawing, 2019', className='is-style-plate', lightbox=True)),
    (None, J(label('New in oak and elm this autumn'), heading('Calder chair', 1, fontSize='display'),
             para('Tamsin Hale and Olek Brzeziński make chairs, tables and cabinets in British hardwood in Hebden Bridge. This is the newest.'),
             group(J(*[group(J(label(k), para('%s mm' % mm, fontSize='large', fontFamily='display')), className='is-style-dimension') for k, mm, _ in P1['dims']]),
                   layout={'type': 'grid', 'minimumColumnWidth': '6rem'}),
             buttons(('See the Calder chair', '/pieces/calder-chair/'), ('All pieces', '/pieces/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|50'}}}),
    description='Opens with a piece: the drawing large, the name, one line about the workshop and its sizes.')

pattern('hero-workshop', 'Hero: the workshop at work', 'hero', J(
    img_('hero.jpg', 'Olek fitting a back rail on a Calder frame, October 2026', align='wide', className='is-style-plate'),
    columns(('50%', heading('Brook &amp; Lathe, Hebden Bridge', 1, fontSize='xx-large')),
            (None, para('Two people, one weaving shed and eight British timbers. Pieces in stock ship this week. Everything else takes 6 to 12 weeks.', fontSize='large')), align='wide')))

pattern('in-use-band', 'In use: a room with a piece in it', 'pieces', J(
    img_('inuse.jpg', 'A Calder by the window. Chairs this plain look best in a room that is not.', align='full', className='is-style-plate')))

pattern('making-strip', 'Making: four steps with pictures', 'making', group(J(
    heading('How a chair gets made', 2),
    group(J(*[group(J(img_(f, lightbox=True), heading(h, 4), para(t, fontSize='small')), className='is-style-step') for f, h, t in [
        ('sawmill.jpg', 'Boards', 'We pick boards at the sawmill and air-dry them for a year per inch.'),
        ('lathe.jpg', 'Legs and spindles', 'Legs are turned, spindles are riven and shaved along the grain.'),
        ('holdfast.jpg', 'Joints', 'Mortises are chopped with the part held down by a holdfast.'),
        ('shavings.jpg', 'Finish', 'Every surface is planed, not sanded, then oiled or soaped.')]]),
        className='is-style-steps', align='wide', layout={'type': 'grid', 'minimumColumnWidth': '14rem'})), align='wide', layout={'type': 'default'}))

pattern('joint-detail', 'Detail: one joint explained', 'making', columns(
    ('45%', img_('dovetail.jpg', 'A dovetail, pulled apart')),
    (None, J(heading('Wood holding wood', 3),
             para('Our drawers are dovetailed by hand and our chairs are held together with wedged tenons. There is no metal in any of our furniture except a hinge where a hinge is needed.'),
             para('A good joint gets tighter as the wood moves with the seasons. A screw gets looser.'))), align='wide', verticalAlignment='center'))

pattern('guarantee-band', 'Band: ten-year guarantee', 'pieces', group(J(
    para('10 years', className='is-style-big-number'),
    para('on every joint, and repairs at cost after that. Most of our furniture will outlast its first owner.', fontSize='large')),
    className='is-style-shaving', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('product-sheet', 'Product sheet: drawing first, facts below', 'pieces', J(pattern_ref('obj-hero'), pattern_ref('obj-sizes')),
        description='A shortcut for a shop page: the object hero and its sizes.')

# ---------------------------------------------------------------- materials
pattern('source-book', 'Material source book (timber swatches)', 'making', group(J(
    row(J(heading('Timbers we use', 2), para('Every board comes from a named sawmill within about 250 miles of the workshop.', fontSize='small')), justify='space-between', align='wide'),
    grid(J(*[stack(J(image(f + '.jpg', 'Square sample of planed %s, showing its grain' % n.lower(), className='is-style-swatch'),
                     heading(n, 4), label(src), para(note, fontSize='small')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}})
             for f, n, src, note in TIMBERS]), min_width='15rem', align='wide', className='is-style-two-up-mobile')),
    align='wide', layout={'type': 'default'}), description='The signature swatch library: each timber as a square sample with its source and one line on how it behaves.')

pattern('finishes', 'Finishes', 'making', group(J(
    heading('Finishes', 3),
    *[columns(('25%', heading(a, 4)), (None, para(b)), ('25%', label(c)), className='is-style-spec-row', verticalAlignment='center') for a, b, c in [
        ('Hardwax oil', 'Matt and easy to touch up. Our default.', 'All timbers'), ('Soap', 'Very pale and dry to the touch. Needs a wash twice a year.', 'Oak, ash, sycamore'),
        ('Fumed', 'Oak darkened with ammonia to a deep brown, then oiled.', 'Oak only'), ('Ebonised', 'Iron and vinegar on oak. Near black, grain still visible.', 'Oak only, plus £180')]]),
    align='wide', layout={'type': 'constrained', 'contentSize': '960px'}))

pattern('complementary-materials', 'Complementary materials', 'making', group(J(
    heading('Also in the workshop', 4),
    para('Seat rush from the Somerset Levels, Danish cord, undyed wool webbing from Laxtons in Guiseley, vegetable-tanned leather for drawer pulls, and brass only where a hinge has to be brass.')),
    className='is-style-rule-top'))

pattern('tools', 'The tools we use', 'making', columns(
    ('45%', img_('planes.jpg', 'Some of the planes on the wall above the bench')),
    (None, J(heading('Hand tools first', 3),
             para('We use a bandsaw and a planer-thicknesser to get boards to size. After that nearly everything is done with hand planes, spokeshaves, chisels and a travisher for seats.'),
             para('It is slower. It also leaves a surface you can feel, which a sander cannot.'))), align='wide', verticalAlignment='center'))

pattern('visit-to-see-timbers', 'Visit the workshop to see the timbers', 'contact', group(J(
    heading('Come and see the wood', 3),
    para('Pictures of timber are nearly useless. Book an hour on a Thursday or Friday and handle every species, sit on the chairs and see offcuts of the boards your piece would come from.'),
    buttons(('Book a workshop visit', 'mailto:workshop@example.com?subject=Workshop%20visit'))), className='is-style-shaving', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('materials-page', 'Page: materials', 'page', J(
    pattern_ref('source-book'), spacer('var:preset|spacing|60'), pattern_ref('finishes'), pattern_ref('tools'), pattern_ref('joint-detail'), pattern_ref('complementary-materials'), pattern_ref('visit-to-see-timbers')),
    block_types='core/post-content')

# ---------------------------------------------------------------- stock, shop, delivery
pattern('in-stock', 'In stock now (table)', 'pieces', group(J(
    heading('In stock now', 2),
    para('Finished pieces waiting in the workshop. They ship in 1 to 5 working days, or you can collect.'),
    table([['<a href="/pieces/calder-chair/">Calder chair</a>', 'English oak, hardwax oil', '£1,450', '4 left'],
           ['<a href="/pieces/calder-chair/">Calder chair</a>', 'Elm, soap finish', '£1,720', '2 left'],
           ['Pecket stool', 'Ash and sycamore', '£280', '6 left'],
           ['<a href="/pieces/heptonstall-side-table/">Heptonstall side table</a>', 'Cherry, hardwax oil', '£890', '1 left'],
           ['<a href="/pieces/crag-bench/">Crag bench, 1.8 m</a>', 'Larch, unfinished for outdoors', '£1,100', '1 left']],
          head=['Piece', 'Timber and finish', 'Price', 'Stock']),
    pattern_ref('lead-time')), align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}))

pattern('in-stock-cards', 'In stock now (drawings)', 'pieces', group(J(
    heading('Ready to ship', 3),
    grid(J(*[stack(J(img_(f, className='is-style-plate-portrait'), heading(n, 5), label(t))) for f, n, t in [
        ('chair-2.jpg', 'Calder chair, oak', '£1,450, 4 left'), ('stool.jpg', 'Pecket stool', '£280, 6 left'), ('table.jpg', 'Heptonstall table, cherry', '£890, 1 left'), ('bench.jpg', 'Crag bench, larch', '£1,100, 1 left')]]),
         min_width='12rem', className='is-style-two-up-mobile')), align='wide', layout={'type': 'default'}))

pattern('in-stock-page', 'Page: in stock', 'page', J(pattern_ref('in-stock-cards'), spacer('var:preset|spacing|50'), pattern_ref('in-stock'), spacer('var:preset|spacing|60'), pattern_ref('shipping-rates')), block_types='core/post-content')

pattern('shipping-rates', 'Delivery rates (table)', 'pieces', group(J(
    heading('Delivery', 3),
    table([['Collect from the workshop', 'Free'], ['Our van, within 60 miles', '£60'], ['Two-person courier, mainland UK', '£120 to £240'], ['EU, crated', 'Quoted, usually £380 to £650']], head=['How', 'Cost']),
    para('Delivery costs are shown in the basket before you pay. We do not ship outside the UK and EU.', fontSize='small')), layout={'type': 'constrained'}))

pattern('pieces-page', 'Page: pieces', 'page', J(pattern_ref('pieces-index'), pattern_ref('in-use-band'), pattern_ref('made-to-size'), pattern_ref('guarantee-band')), block_types='core/post-content')

# ---------------------------------------------------------------- commissions, trade
pattern('commission-process', 'Commission process', 'services', group(J(
    heading('How a commission works', 2),
    group(J(*[group(J(img_(f), heading(h, 4), para(t), label(d)), className='is-style-step') for f, h, t, d in [
        ('desk.jpg', 'Concept', 'We talk, measure the room and look at what you already own. Then we send sketches and a fixed price.', 'Free, about two weeks'),
        ('table.jpg', 'Development', 'We draw it properly at 1:5 and, for chairs, make a mock-up in pine for you to sit in. A 40% deposit starts this.', 'Two to four weeks'),
        ('hero.jpg', 'Fabrication', 'We choose the boards with you if you want, then make it. Photos at glue-up and before finishing.', 'Six to ten weeks')]]),
        className='is-style-steps', align='wide', layout={'type': 'grid', 'minimumColumnWidth': '16rem'})), align='wide', layout={'type': 'default'}))

pattern('commission-faq', 'Commission questions', 'services', J(
    heading('Questions', 4),
    details('What does a commission cost?', para('A dining table starts around £3,800 and a set of six chairs around £9,000. Small cabinets from £2,400. We give a fixed price after the first meeting.')),
    details('Can you copy a piece I have seen elsewhere?', para('No. We are happy to start from something you like, but we will not copy another maker’s design.')),
    details('Do you work with interior designers?', para('Yes, about a third of our work comes through designers. See trade enquiries.')),
    details('Can I supply my own timber?', para('Sometimes. If it is a tree from your own land, we can arrange milling and two years of drying.'))))

pattern('trade-enquiries', 'Trade enquiries', 'services', group(J(
    heading('Trade enquiries', 3),
    para('Designers, architects and shops get 12% off the collection and a named contact in the workshop. We make up to twelve chairs of one design a month, or one long table.'),
    lst(['Send the project name, the pieces and quantities, and your deadline.', 'We reply with prices, lead times and CAD blocks within three working days.',
         'Samples of each timber and finish are free for trade, posted in a wooden box.']),
    buttons(('Email a trade enquiry', 'mailto:trade@example.com?subject=Trade%20enquiry'))), className='is-style-sheet'))

pattern('commission-page', 'Page: commission', 'page', J(
    pattern_ref('commission-process'), spacer('var:preset|spacing|60'),
    columns((None, pattern_ref('trade-enquiries')), (None, pattern_ref('commission-faq')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('client-quote')), block_types='core/post-content')

pattern('client-quote', 'Client quote', 'services', pullquote(
    'We asked for a table for twelve that would fit through a cottage door. They made it in three pieces and it has not moved in four years.', 'Rhiannon and Dev, Mankinholes, 2022'))

pattern('green-cta', 'Band: commissions open', 'services', group(J(
    heading('Commission slots for spring 2027 are open', 2, fontSize='x-large'),
    para('We take on about fourteen commissions a year. Three spring slots are left, and one of them is probably a long table.'),
    buttons(('Start a commission', '/commission/'))), className='is-style-green', align='full', layout={'type': 'constrained'}))

# ---------------------------------------------------------------- workshop, about
pattern('workshop-courses', 'Workshop courses', 'about', columns(
    ('45%', img_('workshop.jpg', 'The bench room, where the courses run')),
    (None, J(heading('Make a stool in two days', 3),
             para('Four people at a time, Saturday and Sunday, 9.30am to 5pm. You make a three-legged ash stool with a riven seat and go home with it. Lunch is soup from the café next door.'),
             *[columns(('35%', label(a)), (None, para(b)), className='is-style-spec-row', isStackedOnMobile=False) for a, b in [
                 ('Next dates', '18 and 19 October, 15 and 16 November 2026'), ('Price', '£340, timber and tools included'), ('Places', 'Four per course'), ('Who for', 'Anyone over 16. No experience needed.')]],
             buttons(('Book a place', '/shop/')))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('about-makers', 'About the makers', 'about', columns(
    (None, J(heading('Two people and a weaving shed', 2),
             para('Tamsin Hale trained at Rycotewood and spent six years making chairs for other people. Olek Brzeziński grew up in his father’s joinery in Nowy Targ and came to Yorkshire to build boats. They set up in Mytholm Works in 2014, in a shed that used to hold forty looms.'),
             para('Tamsin draws everything by hand at 1:5 before any wood is cut. Olek says this is slower. He is right, and we still do it.'))),
    (None, img_('hero.jpg', 'Olek fitting a back rail on a chair frame')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('sustainability', 'Where the wood comes from', 'about', media_text('sawmill.jpg', IMG['sawmill'], J(
    heading('Where the wood comes from', 3),
    para('We buy from four small sawmills and one tree surgeon, all named on the materials page. Nothing comes from further than 250 miles. Offcuts go to the stool course, then to a wood-burning bakery in Todmorden.'),
    para('<a href="/materials/">See every timber we use</a>')), width=45, className='is-style-shaving', align='wide'))

pattern('find-us', 'Visit the workshop', 'contact', columns(
    (None, J(heading('Visit the workshop', 3),
             para('Unit 3, Mytholm Works, Hebden Bridge HX7 6DL. Ten minutes’ walk from Hebden Bridge station along the canal towpath, past the marina. Parking in the yard.'),
             para('Visits by appointment on Thursdays and Fridays, 10am to 4pm. The workshop is on the ground floor with a level entrance.'))),
    (None, J(heading('Ask', 3),
             *[columns(('30%', label(a)), (None, para(b)), className='is-style-spec-row', isStackedOnMobile=False) for a, b in [
                 ('Email', '<a href="mailto:workshop@example.com">workshop@example.com</a>'), ('Phone', '01422 555 014'), ('Trade', '<a href="mailto:trade@example.com">trade@example.com</a>')]])),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('workshop-page', 'Page: workshop', 'page', J(
    pattern_ref('about-makers'), spacer('var:preset|spacing|60'), pattern_ref('making-strip'), spacer('var:preset|spacing|60'), pattern_ref('workshop-courses'),
    spacer('var:preset|spacing|60'), pattern_ref('sustainability'), pattern_ref('find-us')), block_types='core/post-content')

pattern('refinishing', 'Refinishing service', 'services', group(J(
    heading('Refinishing', 4),
    para('Ring marks, dog scratches, a chair that has been sat on backwards for ten years: bring it in and we sand, refinish and re-glue it. From £90 for a chair, £240 for a dining table top.')),
    className='is-style-rule-top'))

pattern('aftercare-page', 'Page: aftercare', 'page', J(pattern_ref('care'), pattern_ref('refinishing'), pattern_ref('shipping-rates')), block_types='core/post-content')

# ---------------------------------------------------------------- projects
def proj_body(img, intro, facts, text, quote_=None):
    parts = [img_(img, align='wide', className='is-style-plate'),
             columns(('58%', J(para(intro, fontSize='large'), para(text))),
                     (None, group(J(*[columns(('40%', label(a)), (None, para(b, fontSize='small')), className='is-style-spec-row', isStackedOnMobile=False) for a, b in facts]), className='is-style-title-block')),
                     align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})]
    if quote_:
        parts.append(pullquote(*quote_))
    return J(*parts)


pattern('project-sheet', 'Project: drawing, story and facts', 'projects', proj_body(
    'table.jpg', 'Eight reading tables for the reference room of Todmorden library, replacing laminate desks from 1978. Built in cherry so they would darken to match the old oak panelling.',
    [('Client', 'Calderdale Council'), ('Timber', 'Cherry, hardwax oil'), ('Size', '1800 / 900 / 740 mm each'), ('Finished', 'May 2024')],
    'The brief said the tables had to survive schoolchildren. We used drawbored mortise and tenons, no metal fixings, and a thick top that can be sanded back at least five times.',
    ('They are the first library tables in thirty years that nobody has carved their name into. Yet.', 'Joanne Pickles, Todmorden library, 2025')))

pattern('collaborations', 'Collaborations list', 'projects', group(J(
    heading('Made with other people', 3),
    *[columns(('14%', label(y)), (None, heading(w, 4)), ('34%', para(c, fontSize='small')), className='is-style-spec-row', verticalAlignment='center') for y, w, c in [
        ('2025', 'Twelve chairs for a gallery learning studio', 'With the Hepworth Wakefield'), ('2024', 'Reading-room tables for Todmorden library', 'With Calderdale Council'),
        ('2023', 'The Crag bench, a run of thirty', 'With Pennine Prospects'), ('2022', 'Rush-seated stools', 'With Felicity Irons, rush weaver')]]),
    align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}))

PROJECT_ITEM = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='contain', className='is-style-plate'),
                 row(J(dyn('post-terms', term='category'), dyn('post-date', format='Y')), justify='space-between'),
                 dyn('post-title', isLink=True, level=3, fontSize='large'))

pattern('projects-grid', 'Projects: latest', 'projects', group(J(
    row(J(heading('Recent projects', 2), para('<a href="/projects/">All projects</a>')), justify='space-between', align='wide'),
    query(PROJECT_ITEM, per_page=3, query_id=31, align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70'}}}))

pattern('projects-archive', 'Projects archive (inherits the page query)', 'projects', inherit_query(PROJECT_ITEM, align='wide',
        layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}), inserter=False)

pattern('newsletter', 'Workshop letter', 'contact', group(J(
    heading('A letter from the workshop, four times a year', 3),
    para('New pieces, what is in stock, course dates and whatever we found at the sawmill.'),
    buttons(('Sign up by email', 'mailto:workshop@example.com?subject=Workshop%20letter'))), className='is-style-sheet', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('post-list', 'Search results list', 'projects', inherit_query(
    group(columns(('22%', dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='contain')), (None, J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30)))),
          className='is-style-rule-top'), align='wide'), inserter=False)

# ---------------------------------------------------------------- templates
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('hero-piece'), pattern_ref('pieces-index'), pattern_ref('in-use-band'), pattern_ref('making-strip'), pattern_ref('source-book'), pattern_ref('projects-grid')),
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
    buttons(('See the pieces', '/pieces/'))), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/single.html', J(template_part('header', 'header'), group(J(
    group(J(dyn('post-terms', term='category'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', showMoreOnPage=False, fontSize='large')), align='wide', layout={'type': 'constrained', 'contentSize': '860px', 'justifyContent': 'left'}),
    dyn('post-content', align='full', layout={'type': 'constrained'}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous project', showTitle=True),
            dyn('post-navigation-link', label='Next project', showTitle=True)),
          align='wide', className='is-style-rule-top', layout={'type': 'flex', 'justifyContent': 'space-between'})),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|50', 'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|60'}}}),
    template_part('footer', 'footer')))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1),
    dyn('post-content', layout={'type': 'constrained'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1, align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1000px'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-object.html', page_template(dyn('post-content', align='full', layout={'type': 'constrained'}), layout={'type': 'constrained'}, style=MAINPAD))
theme['customTemplates'].append({'name': 'page-object', 'title': 'Object (no title, full width)', 'postTypes': ['page']})
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

# ---------------------------------------------------------------- demo content
import re
PHPIMG = re.compile(r"<\?php echo esc_url\( get_theme_file_uri\( 'assets/images/([\w.-]+)' \) \); \?>")
def as_post(markup):
    return PHPIMG.sub(lambda m: IMGPATH + m.group(1), markup)


posts = [
    dict(title='Reading tables for Todmorden library', category='commissions', image='table.jpg', date='2024-05-20', excerpt='Eight cherry tables for the reference room, built to outlast the schoolchildren.', pattern='joint/project-sheet'),
    dict(title='Twelve Calder chairs for a learning studio', category='collaborations', image='chair-2.jpg', date='2025-03-14', excerpt='A run of twelve chairs in oak, for a gallery education room in Wakefield.',
         content=as_post(proj_body('chair-2.jpg', 'The learning team wanted chairs that children and adults could both use, and that could be stacked two high on a trolley.',
                                   [('Client', 'The Hepworth Wakefield'), ('Timber', 'English oak, soap finish'), ('Quantity', '12 chairs'), ('Finished', 'March 2025')],
                                   'We lowered the Calder seat to 430 mm and added a back rail you can grip. The soap finish is the only one that survives poster paint.'))),
    dict(title='A writing desk for a flat in Leeds', category='commissions', image='desk.jpg', date='2025-06-02', excerpt='The Aire desk, made 150 mm narrower to fit between two windows.',
         content=as_post(proj_body('desk.jpg', 'The client measured the gap between the windows three times before she wrote to us.',
                                   [('Client', 'Private, Chapel Allerton'), ('Timber', 'Cherry, hardwax oil'), ('Size', '850 / 550 / 760 mm'), ('Finished', 'June 2025')],
                                   'The desk is 850 mm wide, in cherry, with one drawer lined in undyed felt. It became the Aire, which is now in the collection.',
                                   ('It fits the gap with a finger’s width either side. Exactly as drawn.', 'Harriet, Chapel Allerton, 2025')))),
    dict(title='The Crag bench, a run of thirty', category='collaborations', image='bench.jpg', date='2023-09-10', excerpt='Larch benches for footpaths on the moor above Heptonstall.',
         content=as_post(proj_body('bench.jpg', 'Thirty benches in Kielder larch for Pennine Prospects, left unfinished so they weather silver.',
                                   [('Client', 'Pennine Prospects'), ('Timber', 'Larch, unfinished'), ('Quantity', '30 benches'), ('Finished', 'September 2023')],
                                   'Each one has the grid reference of where it sits cut into the end. We carried the last six up the hill on a borrowed quad bike.'))),
    dict(title='A court cupboard in fumed oak', category='commissions', image='cabinet.jpg', date='2024-11-18', excerpt='A cupboard for a farmhouse kitchen, darkened with ammonia to match the beams.',
         content=as_post(proj_body('cabinet.jpg', 'A cupboard for a farmhouse kitchen near Heptonstall, where everything else is 300 years old.',
                                   [('Client', 'Private, Heptonstall'), ('Timber', 'Fumed English oak'), ('Size', '1200 / 480 / 1350 mm'), ('Finished', 'November 2024')],
                                   'Fuming takes two days in a sealed tent in the yard. The oak goes from honey to a deep brown and the carving shows up more than it did when pale.'))),
    dict(title='Rush-seated stools with Felicity Irons', category='collaborations', image='stool.jpg', date='2022-07-01', excerpt='We made the frames, Felicity wove the seats from Somerset rush.',
         content=as_post(proj_body('stool.jpg', 'Forty stools over one summer.', [('With', 'Felicity Irons, rush weaver'), ('Timber', 'Ash and sycamore'), ('Quantity', '40 stools'), ('Finished', 'July 2022')],
                                   'Felicity cut the rush on the River Ouse and wove the seats in her barn. We made the frames and drove them down to Bedfordshire in two loads.'))),
]
pages = [{'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'projects', 'title': 'Projects', 'content': ''},
         {'slug': 'pieces', 'title': 'Pieces', 'pattern': 'joint/pieces-page', 'template': 'page-wide'}]
for i, o in enumerate(PIECES):
    pg = {'slug': o['slug'], 'title': o['name'], 'parent': 'pieces', 'template': 'page-object'}
    if i == 0:
        pg['pattern'] = 'joint/obj-page'
    else:
        pg['content'] = as_post(object_page(o))
    pages.append(pg)
pages += [{'slug': 'in-stock', 'title': 'In stock', 'pattern': 'joint/in-stock-page', 'template': 'page-wide'},
          {'slug': 'materials', 'title': 'Materials', 'pattern': 'joint/materials-page', 'template': 'page-wide'},
          {'slug': 'commission', 'title': 'Commission', 'pattern': 'joint/commission-page', 'template': 'page-wide'},
          {'slug': 'workshop', 'title': 'Workshop', 'pattern': 'joint/workshop-page', 'template': 'page-wide'},
          {'slug': 'aftercare', 'title': 'Aftercare', 'pattern': 'joint/aftercare-page'}]
old = json.load(open('demos/joint/content.json'))
demo = {'site': {'title': 'Brook & Lathe', 'tagline': 'Furniture made to order in Hebden Bridge'},
        'categories': [{'slug': 'commissions', 'name': 'Commissions'}, {'slug': 'collaborations', 'name': 'Collaborations'}],
        'front_page': 'home', 'posts_page': 'projects', 'pages': pages, 'posts': posts,
        'nav': [{'label': 'Pieces', 'url': '/pieces/'}, {'label': 'In stock', 'url': '/in-stock/'}, {'label': 'Materials', 'url': '/materials/'},
                {'label': 'Commission', 'url': '/commission/'}, {'label': 'Workshop', 'url': '/workshop/'}, {'label': 'Projects', 'url': '/projects/'}, {'label': 'Shop', 'url': '/shop/'}],
        'currency': 'GBP', 'products': old['products']}
json.dump(demo, open('demos/joint/content.json', 'w'), indent=1, ensure_ascii=False)
print('joint built')
