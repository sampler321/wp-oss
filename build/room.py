# room: interior designer + shop (idea 019)
# Direction: "decorator's scrapbook". A designer's site where every project is told room by room, and each room
#   opens with the paint chip for its walls, because that is the first thing clients ask ("what colour is that?").
# Fonts: Radio Canada Big (registry face) for headings, Karla for text. No third family.
# Palette: plaster #F4EFE9, umber ink #2B2522, claret #6E2F3A for links, putty #E7DED3, plus four paint-chip colours
#   used only as small swatches. Square corners everywhere except the arched hero photograph.
# Layout idea: project stories run in one 60ch column, with images alternating full width and 2-up, and product
#   names linked inline with the price after them, so the portfolio doubles as the shop.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
from blocks import _a
import blocks as _b
set_theme('room')
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
    ('base', '#F4EFE9', 'Plaster'),
    ('contrast', '#2B2522', 'Umber ink'),
    ('accent', '#6E2F3A', 'Claret'),
    ('surface', '#E7DED3', 'Putty'),
    ('line', '#C9BBAA', 'Linen line'),
    ('muted', '#655A52', 'Taupe'),
    ('chip-green', '#6B7556', 'Chip: Lichen'),
    ('chip-ochre', '#C99A45', 'Chip: Mustard seed'),
    ('chip-pink', '#D9A79A', 'Chip: Setting plaster'),
    ('chip-blue', '#8196A6', 'Chip: Slate sky'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))
fam = {f['slug']: f for f in fonts['fontFamilies']}


def pal(rows):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]


def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d


CSS = (':where(h1,h2,h3,h4){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
       '.wp-block-table,.is-style-price{font-variant-numeric:tabular-nums lining-nums}'
       '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.65em .8em .65em 0;text-align:left;vertical-align:top}'
       '.wp-block-table thead{border:0}.wp-block-table th{font-weight:500;font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--muted)}'
       '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--surface)}'
       '.wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large)}'
       '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-underline-offset:.35em;text-decoration-thickness:1px}'
       ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
       '.wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:0;background:transparent}'
       '.wc-block-components-product-price,.woocommerce-Price-amount{font-variant-numeric:tabular-nums}'
       '.wc-block-components-button:not(.is-link),.wp-block-button__link.add_to_cart_button{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);border-radius:0}'
       '.wc-block-components-product-sale-badge{border-radius:0;background:var(--wp--preset--color--accent);color:var(--wp--preset--color--base);border:0}'
       '.wp-block-image img[style*=aspect-ratio]{width:100%}'
       '.wp-block-pullquote cite{font-family:var(--wp--preset--font-family--body);font-style:normal;font-size:var(--wp--preset--font-size--small);color:var(--wp--preset--color--muted)}'
       '.woocommerce-product-gallery img,.wc-block-components-product-image img{background:var(--wp--preset--color--surface)}')

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '640px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'writingMode': False,
            'fontFamilies': [fam['display'], fam['body']],
            'fontSizes': [
                fs('x-small', '0.875rem', 'Caption'),
                fs('small', '1rem', 'Small'),
                fs('medium', '1.125rem', 'Body'),
                fs('large', '1.5rem', 'Large', '1.25rem'),
                fs('x-large', '2.25rem', 'Section', '1.75rem'),
                fs('xx-large', '3.4rem', 'Title', '2.4rem'),
                fs('display', '4.75rem', 'Display', '2.9rem'),
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
                {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.5rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2.5rem, 5.5vw, 4rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3.5rem, 8vw, 6rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4.5rem, 11vw, 9rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'lineHeight': '1.05', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'lineHeight': '1.4', 'letterSpacing': '0.01em'}, 'color': {'text': 'var:preset|color|muted'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': 'var:preset|color|accent'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small', 'letterSpacing': '0.01em'},
                'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.4em', 'right': '1.4em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}, 'border': {'color': 'var:preset|color|contrast'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}},
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45', 'fontStyle': 'italic'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.01em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'elements': {'link': {'color': {'text': 'var:preset|color|muted'}}}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '400', 'lineHeight': '1.3'},
                           'border': {'width': '0', 'style': 'none'}, 'spacing': {'padding': {'left': '0'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '400', 'lineHeight': '1.2'},
                               'border': {'top': {'color': 'var:preset|color|accent', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|accent', 'width': '1px', 'style': 'solid'}},
                               'color': {'text': 'var:preset|color|accent'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/categories': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-project', 'title': 'Project, room by room', 'postTypes': ['post']},
    ],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Room
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A portfolio and small shop for interior designers who tell each project room by room and sell the lamps, fabric and antiques that went into it.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: room
Tags: portfolio, e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column, grid-layout
*/''')


def variation(fname, title, rows):
    write('styles/%s.json' % fname, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                                'settings': {'color': {'palette': pal(rows)}}}, indent='\t', ensure_ascii=False))


CHIPS = PAL[6:]
variation('terrazzo', 'Terrazzo', [('base', '#F2F0EC', 'Plaster'), ('contrast', '#23282A', 'Umber ink'), ('accent', '#2E5E4E', 'Claret'),
                                   ('surface', '#E3E2DB', 'Putty'), ('line', '#C4C4BA', 'Linen line'), ('muted', '#575C58', 'Taupe')] + CHIPS)
variation('boucle', 'Bouclé', [('base', '#FAF8F5', 'Plaster'), ('contrast', '#3A3A3A', 'Umber ink'), ('accent', '#7A4A2A', 'Claret'),
                               ('surface', '#EFEBE4', 'Putty'), ('line', '#D8D2C8', 'Linen line'), ('muted', '#5F5A55', 'Taupe')] + CHIPS)
variation('lacquer', 'Lacquer', [('base', '#1D1B1A', 'Plaster'), ('contrast', '#E4C9A8', 'Umber ink'), ('accent', '#E89A7E', 'Claret'),
                                 ('surface', '#2A2624', 'Putty'), ('line', '#4A423C', 'Linen line'), ('muted', '#BFAF9C', 'Taupe')] + CHIPS)


def section(slug, title, block_types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug,
                                                        'blockTypes': block_types, 'styles': styles}, indent='\t', ensure_ascii=False))


section('chip', 'Paint chip', ['core/group'], {
    'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|line'},
    'css': '&{width:4.5rem;height:4.5rem;flex:none;padding:0!important}'})
section('putty', 'Putty panel', ['core/group', 'core/columns', 'core/media-text'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('claret', 'Claret band', ['core/group'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                 'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|accent'}, 'border': {'color': 'var:preset|color|base'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('arch', 'Arched photo', ['core/image', 'core/post-featured-image'], {
    'css': '& img{border-radius:999px 999px 0 0;aspect-ratio:4/5;object-fit:cover;width:100%}'})
section('crop-square', 'Square crop', ['core/image'], {'css': '& img{aspect-ratio:1;object-fit:cover;width:100%}'})
section('crop-portrait', 'Portrait crop', ['core/image'], {'css': '& img{aspect-ratio:4/5;object-fit:cover;width:100%}'})
section('price', 'Price after a name', ['core/paragraph'], {
    'typography': {'fontSize': 'var:preset|font-size|small'}, 'color': {'text': 'var:preset|color|muted'}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('text-link', 'Text link button', ['core/button'], {
    'color': {'background': 'transparent', 'text': 'var:preset|color|accent'},
    'border': {'width': '0', 'style': 'none'},
    'css': '& .wp-block-button__link{padding:0;background:transparent;color:var(--wp--preset--color--accent);text-decoration:underline;text-underline-offset:.3em}'})
section('inline-list', 'Inline list', ['core/categories'], {
    'css': '&{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.4rem 1.4rem}'})


CATS = [('project', 'Project stories'), ('shop', 'Shop'), ('fabric', 'Fabric and wallpaper'), ('services', 'Services and fees'), ('about', 'About'), ('contact', 'Contact'), ('hero', 'Heroes'), ('page', 'Page layouts')]
CATMAP = {'project-rooms': 'project', 'room-chapter': 'project', 'paint-chips': 'project', 'project-credits': 'project', 'press-quote': 'about', 'pieces-in-project': 'shop',
          'the-edit': 'shop', 'hero-latest-project': 'hero', 'projects-grid': 'project', 'projects-archive': 'project', 'shop-categories': 'shop', 'fabric-compositions': 'fabric',
          'fabric-samples': 'fabric', 'wallpaper-note': 'fabric', 'philosophy': 'services', 'enquiry-what-to-send': 'services', 'fees': 'services', 'trade-account': 'services',
          'contact-details': 'contact', 'about-studio': 'about', 'shipping-note': 'shop', 'journal-strip': 'project', 'claret-cta': 'services', 'post-list': 'project',
          'project-contents': 'project', 'material-board': 'project', 'project-gallery': 'project', 'before-after-room': 'project', 'designer-note': 'project', 'client-testimonial': 'about',
          'process-steps': 'services', 'services-cards': 'services', 'product-spotlight': 'shop', 'shop-by-room': 'shop', 'sample-box': 'fabric', 'antiques-note': 'shop',
          'press-list': 'about', 'project-intro': 'project', 'room-palette': 'project', 'visit-shop': 'contact'}
_pattern = pattern


def pattern(slug, title, categories, body, **kw):
    return _pattern(slug, title, CATMAP.get(slug, 'page' if kw.get('block_types') else categories), body, **kw)


write('functions.php', "<?php\n/**\n * Room: registers the pattern categories used by the theme's patterns.\n *\n * @package room\n */\n\nadd_action(\n\t'init',\n\tfunction () {\n"
      + ''.join("\t\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', 'room' ) ) );\n" % c for c in CATS) + "\t}\n);\n")

# ---------------------------------------------------------------- parts
write('parts/header.html', group(J(
    row(J(stack(J(dyn('site-title', level=0), dyn('site-tagline')), style={'spacing': {'blockGap': '0'}}),
          dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')),
        justify='space-between', align='wide')),
    tag='header', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40'}}}))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(para('Wren Lamont Studio', fontSize='large', fontFamily='display'),
                  para('Interiors for houses and flats in Scotland and the north of England, and a small shop of the things we keep using.', fontSize='small'))),
        (None, J(heading('Studio and shop', 6),
                 para('14 Hamilton Place, Stockbridge<br>Edinburgh EH3 5AU<br>Shop open Wednesday to Saturday, 10am to 5pm', fontSize='small'))),
        (None, J(heading('Get in touch', 6),
                 para('<a href="mailto:studio@example.com">studio@example.com</a><br>0131 496 0715<br><a href="/trade/">Trade accounts</a>', fontSize='small'))),
        align='wide'),
    para('Demo photographs are public domain and CC0 images from Wikimedia Commons and the Metropolitan Museum of Art, used as stand-ins.', align='wide', textColor='muted', fontSize='x-small')),
    tag='footer', align='full', className='is-style-putty', style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

# ---------------------------------------------------------------- patterns
IMG = {
    'living': 'A drawing room with terracotta walls, a white marble fireplace, a crystal chandelier and green leather sofas',
    'hall': 'An entrance hall with a black and white chequered marble floor and a grey marble table holding red roses',
    'dining': 'A long panelled dining room with a mahogany table laid for twelve and a window at the far end',
    'kitchen': 'A small farmhouse kitchen with red patterned wallpaper, a white dresser and a table set with coloured plates',
    'bedroom': 'A four-poster bed with red hangings and barley-twist posts, next to a window with a small lamp',
    'bath': 'A bathroom with a white enamel bath, a pedestal basin and a leaded window above them',
    'lamp': 'A black lacquered table lamp painted with small figures, under a pleated claret shade with a fringe',
    'chair': 'A carved walnut armchair upholstered in faded floral needlepoint',
    'cushion': 'An oak corner chair with a turned frame and a triangular embroidered cushion',
    'candle': 'A brass pricket candlestick with a pierced round base',
    'stool': 'A low wooden stool with a dipped seat and turned legs, on a grey background',
    'vase': 'A tall oxblood-glazed ceramic vase on a grey background',
    'fabric': 'A woven fabric in red, black and gold with lions and pomegranates',
    'rug': 'A flat-woven kelim runner with red and ochre zigzag stripes',
    'wallpaper': 'A block-printed wallpaper sample with urns, flower sprays and small temples on pale blue',
}


def chip(color, name, where):
    return row(J(group('', className='is-style-chip', backgroundColor=color, layout={'type': 'default'}),
                 stack(J(para(where, fontSize='x-small', textColor='muted'), para(name, fontSize='small')), style={'spacing': {'blockGap': '0'}})),
               wrap=False)


def piece(name, price, href='/shop/'):
    return '<a href="%s">%s</a> (%s)' % (href, name, price)


# Signature: a project told room by room with the pieces linked inline
ROOMS = [
    ('The hall', 'chip-pink', 'Setting plaster, estate emulsion', 'hall.jpg', 'full',
     'The first thing the Mackenzies wanted gone was the magnolia. We took the hall back to a warm pink plaster colour, kept the old chequered floor and put a round marble table in the middle so there is somewhere to drop keys that is not the radiator. The bowl on it is our %s.' % piece('oxblood vase', '£165')),
    ('The drawing room', 'chip-ochre', 'Mustard seed on the walls, Lichen on the woodwork', 'living.jpg', 'full',
     'This room gets light from two sides until about three, so it can take a strong colour. The sofas were theirs and are still theirs, recovered in green leather. We added the %s by the window and a pair of our %s either side of the fireplace.' % (piece('Tay needlepoint armchair', '£2,400'), piece('Ormond lamps', '£340 each'))),
    ('The dining room', 'chip-green', 'Lichen, eggshell, on panelling', 'dining.jpg', 'pair',
     'Twelve chairs, one long table and a lot of panelling. We painted the panels in one green and left the ceiling white. The %s runs the length of the sideboard and the %s came from a sale in Kelso.' % (piece('kelim runner', '£780'), piece('brass pricket candlesticks', '£220 each'))),
    ('The main bedroom', 'chip-blue', 'Slate sky, dead flat', 'bedroom.jpg', 'full',
     'The bed was the one thing nobody was allowed to move. We lined the hangings, rewired the lamp and put a %s at the end of the bed for sitting on to put socks on.' % piece('low ash stool', '£390')),
]


def room_block(title, color, paint, img, mode, text):
    parts = [heading(title, 3), chip(color, paint, 'Walls'), para(text)]
    if mode == 'full':
        parts.append(image(img, IMG[img[:-4]], align='wide'))
    else:
        parts.append(columns((None, image(img, IMG[img[:-4]])), (None, image('rug.jpg', IMG['rug'], 'The kelim runner, 3.2 m long')), align='wide'))
    return J(*parts)


pattern('project-rooms', 'Project story, room by room', 'featured', J(
    pattern_ref('project-contents'),
    para('A Georgian flat on the first floor of a terrace in Stockbridge, for a family of four and a large dog. They wanted it to look as if they had lived there for twenty years by the first Christmas. We had fourteen weeks.', fontSize='large'),
    *[room_block(*r) for r in ROOMS]),
    description='The signature layout: each room gets a heading, the paint chip for its walls, a short story with the pieces linked inline and the price after them, then photos.')

pattern('room-chapter', 'One room, with paint chip and linked pieces', 'text', room_block(*ROOMS[1]),
        description='Copy this for each room in a project. Change the chip colour in the block settings.')

pattern('paint-chips', 'Paint colours used in a project', 'text', group(J(
    heading('Colours in this house', 4),
    grid(J(chip('chip-pink', 'Setting plaster', 'Hall'), chip('chip-ochre', 'Mustard seed', 'Drawing room'),
           chip('chip-green', 'Lichen', 'Dining room'), chip('chip-blue', 'Slate sky', 'Bedroom')), min_width='14rem')),
    className='is-style-rule-top', align='wide', layout={'type': 'default'}))

def ruled(pairs):
    return group(J(*[columns(('38%', para(a, fontSize='small', textColor='muted')), (None, para(b)), className='is-style-rule-top', isStackedOnMobile=False) for a, b in pairs]), layout={'type': 'default'})


pattern('project-credits', 'Project credits', 'text', group(J(
    heading('Credits', 4), ruled([('Where', 'Stockbridge, Edinburgh'), ('Finished', 'December 2025'), ('Photography', 'Callum Fraser'), ('Styling', 'Priya Shah'), ('Builder', 'Leith Joinery Co.')])),
    layout={'type': 'constrained'}), description='Credits line: place, year, photographer, stylist, builder.')

pattern('press-quote', 'Press quote with publication and date', 'testimonials', pullquote(
    'Wren Lamont has a rare habit of leaving the good old things exactly where they were.',
    'Isla McGowan, The Scotsman Magazine, March 2026'))

PIECES = [('lamp.jpg', 'Ormond table lamp', '£340'), ('chair.jpg', 'Tay needlepoint armchair, antique', '£2,400'),
          ('rug.jpg', 'Kelim runner, antique', '£780'), ('candle.jpg', 'Brass pricket candlestick, antique', '£220')]

pattern('pieces-in-project', 'Pieces in this project (shop row)', 'shop', group(J(
    row(J(heading('Pieces in this project', 3), para('<a href="/shop/">The whole shop</a>')), justify='space-between', align='wide'),
    grid(J(*[stack(J(image(f, IMG[f[:-4]], href='/shop/', className='is-style-crop-portrait'), para('<a href="/shop/">%s</a>' % n), para(p, className='is-style-price')),
                   style={'spacing': {'blockGap': 'var:preset|spacing|20'}}) for f, n, p in PIECES]), min_width='14rem', align='wide')),
    align='wide', layout={'type': 'default'}), description='A row of products used in one interior, linking to the shop.')

pattern('the-edit', 'The edit: one project as a collection', 'shop', columns(
    ('38%', J(heading('The Stockbridge edit', 2),
              para('Everything we bought, made or found for the flat on Dean Terrace that you can still buy. Antiques are one-offs, so when they go, they go.'),
              buttons(('Shop the Stockbridge edit', '/shop/')))),
    (None, gallery([('lamp.jpg', IMG['lamp'], 'Ormond lamp, £340'), ('vase.jpg', IMG['vase'], 'Oxblood vase, £165'), ('stool.jpg', IMG['stool'], 'Ash stool, £390')], columns=3)),
    align='wide'), description='Products from one finished interior, as a collection page header.')

pattern('hero-latest-project', 'Hero: latest project with an arched photo', 'featured', columns(
    ('42%', J(heading('Rooms for people who already own too many books', 1),
              para('Wren Lamont Studio designs houses and flats in Edinburgh and the Borders, and runs a small shop on Hamilton Place. We keep what you love, paint the rest and find the lamp you have been missing.', fontSize='large'),
              buttons(('See the Stockbridge flat', '/a-georgian-flat-in-stockbridge/'), ('How we work', '/how-we-work/', {'className': 'is-style-text-link'})))),
    (None, image('living.jpg', IMG['living'], 'The drawing room in Stockbridge, walls in Mustard seed', className='is-style-arch', lightbox=False)),
    align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|70'}, 'padding': {'top': 'var:preset|spacing|50'}}}))

PROJECT_ITEM = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover'),
                 row(J(dyn('post-terms', term='category'), dyn('post-date', format='Y')), justify='space-between'),
                 dyn('post-title', isLink=True, level=3, fontSize='large'))

pattern('projects-grid', 'Interiors: latest projects', 'featured,query', group(J(
    row(J(heading('Interiors', 2), para('<a href="/interiors/">All projects</a>')), justify='space-between', align='wide'),
    query(PROJECT_ITEM, per_page=4, query_id=21, align='wide', layout={'type': 'grid', 'columnCount': 2, 'minimumColumnWidth': '20rem'})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70'}}}), keywords='projects, portfolio')

pattern('projects-archive', 'Interiors archive (inherits the page query)', 'query', inherit_query(PROJECT_ITEM, align='wide',
        layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '18rem'}), inserter=False)

pattern('shop-categories', 'Shop categories', 'shop', group(J(
    heading('The shop', 2),
    para('Our own lamps and fabric, made in small runs in Scotland and Lancashire, and antiques we buy at sales and never manage to keep.'),
    grid(J(*[stack(J(image(f, IMG[f[:-4]], href='/shop/', className='is-style-crop-square'), heading('<a href="/shop/">%s</a>' % n, 4), para(d, fontSize='small')),
                   style={'spacing': {'blockGap': 'var:preset|spacing|20'}})
             for f, n, d in [('chair.jpg', 'Furniture', 'Antique chairs and our ash stool'), ('lamp.jpg', 'Lighting', 'Table lamps and shades, rewired here'),
                             ('fabric.jpg', 'Fabric', 'Linen, wool and mohair by the metre'), ('wallpaper.jpg', 'Wallpaper', 'Block printed, by the roll'),
                             ('vase.jpg', 'Objects', 'Vases, candlesticks, the odd bowl')]]), min_width='12rem', align='wide')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70'}}}))

pattern('fabric-compositions', 'Fabric by composition', 'shop', group(J(
    heading('Fabric, by what it is made of', 3),
    table([['Linen', 'Heavy Irish linen, 330 g/m², six colours', 'Curtains, blinds, loose covers', '£68 to £96 a metre'],
           ['Wool', 'Lambswool plains from a mill in Selkirk', 'Upholstery, cushions', '£84 a metre'],
           ['Mohair', 'Mohair velvet, 60% mohair, 40% cotton', 'Chairs that get sat in', '£165 a metre'],
           ['Hemp and jute', 'Hemp and jute weave, undyed', 'Headboards, blinds, walls', '£58 a metre']],
          head=['Composition', 'What it is', 'Good for', 'Price'])), align='wide', layout={'type': 'constrained', 'contentSize': '960px'}))

pattern('fabric-samples', 'Fabric samples request', 'call-to-action', media_text('fabric.jpg', IMG['fabric'], J(
    heading('Up to five cuttings, free', 3),
    para('Tell us which fabrics and we post cuttings about 15 by 20 cm within three working days. UK only. Colour on a screen is a guess, so please order samples before you order 14 metres.'),
    buttons(('Ask for samples by email', 'mailto:shop@example.com?subject=Fabric%20samples'))), width=45, className='is-style-putty', align='wide'))

pattern('fabric-page', 'Page: fabric', 'shop', J(
    pattern_ref('fabric-samples'), spacer('var:preset|spacing|60'), pattern_ref('fabric-compositions'), pattern_ref('wallpaper-note')), block_types='core/post-content')

pattern('wallpaper-note', 'Wallpaper by the roll', 'shop', columns(
    ('40%', image('wallpaper.jpg', IMG['wallpaper'], 'Temple, block printed, pale blue')),
    (None, J(heading('Wallpaper', 3),
             para('One design for now, called Temple, block printed in Lancashire on 52 cm rolls, 10 metres long. £145 a roll. A small room of 3 by 3.5 metres takes about seven rolls.'),
             para('We send a half-metre sample for £6, refunded when you order.', fontSize='small'))), align='wide'))

pattern('philosophy', 'How we think about a room', 'about', group(J(
    heading('Four things we look at first', 2, fontSize='x-large'),
    grid(J(*[stack(J(heading(h, 4), para(t))) for h, t in [
        ('Personality', 'What you already own and cannot part with. Most rooms start with one chair or one painting.'),
        ('Setting', 'The building, the light and the street. A Georgian flat and a farm cottage want different things.'),
        ('Contrast', 'Something old next to something new, something rough next to something polished.'),
        ('Functionality', 'Where the post lands, where the dog sleeps, where you read. We ask before we draw.')]]), min_width='12rem', align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('enquiry-what-to-send', 'Enquiries: what to send', 'contact', group(J(
    heading('Starting a project', 3),
    para('Email <a href="mailto:studio@example.com">studio@example.com</a> with these four things. It saves a week of back and forth.'),
    lst(['A floor plan, even a hand-drawn one with rough measurements',
         'Phone photos of every room you want us to look at, taken from the doorway',
         'Your budget for the work, including furniture, and when you want to be finished',
         'Anything you are keeping: a sofa, a rug, a painting, a grandmother’s chest'], ordered=True),
    para('We reply within a week. If we are full we say so, and we can usually suggest someone who is not.', fontSize='small')),
    className='is-style-putty', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('fees', 'Fees', 'services', J(
    heading('Fees', 3),
    table([['First visit', 'Two hours at your house, notes and a colour list', '£350'],
           ['Single room', 'Design, drawings, sourcing and one install day', 'From £2,800'],
           ['Whole house', 'Design and project management with your builder', '12% of the build and furnishing budget']]),
    para('We take on four whole-house projects a year. We do not do show homes or rental flips.', fontSize='small')))

pattern('how-we-work-page', 'Page: how we work', 'about', J(
    pattern_ref('about-studio'), pattern_ref('services-cards'), pattern_ref('process-steps'), spacer('var:preset|spacing|60'), pattern_ref('philosophy'), spacer('var:preset|spacing|60'),
    columns((None, pattern_ref('enquiry-what-to-send')), (None, pattern_ref('fees')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('press-quote')), block_types='core/post-content')

pattern('trade-account', 'Trade account', 'shop', J(
    para('Designers, architects and stylists get 15% off our own lamps, fabric and wallpaper, and 10% off antiques. We hold stock for projects for up to four weeks.', fontSize='large'),
    heading('To apply', 3),
    lst(['Email <a href="mailto:trade@example.com">trade@example.com</a> with your company name, address and VAT number.',
         'Send a link to your website or three recent projects.',
         'We open the account within five working days and send you a login.'], ordered=True),
    heading('What trade accounts get', 3),
    ruled([('Own lamps, fabric, wallpaper', '15% off'), ('Antiques', '10% off'), ('Sample cuttings', 'Up to ten at a time, free'), ('Delivery', 'Trade rates on request')])))

pattern('trade-page', 'Page: trade', 'shop', J(pattern_ref('trade-account')), block_types='core/post-content')

pattern('contact-details', 'Contact and shop hours', 'contact', columns(
    (None, J(heading('The studio and shop', 3),
             para('14 Hamilton Place, Stockbridge, Edinburgh EH3 5AU. The shop is on the ground floor, the studio is up the stairs behind it. The 24 and 29 buses stop on Raeburn Place, two minutes away.'),
             ruled([('Wednesday to Friday', '10am to 5pm'), ('Saturday', '10am to 4pm'), ('Sunday to Tuesday', 'Closed, or by appointment')]))),
    (None, J(heading('Ask us', 3),
             para('Projects: <a href="mailto:studio@example.com">studio@example.com</a><br>Shop and orders: <a href="mailto:shop@example.com">shop@example.com</a><br>Phone: 0131 496 0715'),
             para('Wren and Priya are usually out on site on Mondays and Tuesdays. We answer email the same week.', fontSize='small'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('contact-page', 'Page: contact', 'contact', J(pattern_ref('contact-details'), spacer('var:preset|spacing|60'), pattern_ref('visit-shop'), spacer('var:preset|spacing|60'), pattern_ref('enquiry-what-to-send')), block_types='core/post-content')

pattern('about-studio', 'About the studio', 'about', media_text('bedroom.jpg', IMG['bedroom'], J(
    heading('Wren and Priya', 3),
    para('Wren Lamont trained as a paintings conservator and spent eight years at a Mayfair decorator before moving home to Edinburgh in 2016. Priya Shah runs projects and the shop, and is the reason anything arrives on time.'),
    para('We think most houses need fewer new things than their owners think. We would rather reupholster your chair than sell you one.')), width=45, align='wide'))

pattern('shipping-note', 'Delivery and returns', 'shop', group(J(
    heading('Delivery and returns', 4),
    para('Small things go by Royal Mail, tracked, £6.50. Furniture and lamps go by our own van within 60 miles of Edinburgh, from £45, and by courier further away, quoted before you pay. Fabric cut to length and antiques cannot be returned. Everything else can come back within 14 days.', fontSize='small')),
    className='is-style-rule-top'))

pattern('journal-strip', 'From the notebook (latest projects list)', 'posts,query', group(J(
    heading('Recently finished', 4),
    query(row(J(dyn('post-title', isLink=True, level=5), dyn('post-date', format='F Y')), justify='space-between'), per_page=5, query_id=22)),
    className='is-style-rule-top'))

pattern('claret-cta', 'Claret band: start a project', 'call-to-action', group(J(
    heading('We are booking projects for spring 2027', 2, fontSize='x-large'),
    para('Two whole-house slots and a handful of single rooms. Send us a floor plan and some photos and we will tell you if we are the right people.'),
    buttons(('What to send us', '/contact/'))), className='is-style-claret', align='full', layout={'type': 'constrained'}))

pattern('project-intro', 'Project intro: place, brief and time', 'project', columns(
    ('40%', J(heading('The brief', 4), para('A Georgian flat on the first floor of a terrace in Stockbridge, for a family of four and a large dog.'))),
    (None, para('They wanted it to look as if they had lived there for twenty years by the first Christmas. We had fourteen weeks, a builder we trust, and one rule from the client: the piano stays where it is.', fontSize='large')),
    align='wide'))

pattern('project-contents', 'Rooms in this project', 'project', group(J(
    heading('Rooms in this project', 6),
    lst(['The hall', 'The drawing room', 'The dining room', 'The main bedroom'], ordered=True)), className='is-style-rule-top'))

pattern('room-palette', 'Colours in one room', 'project', group(J(
    heading('The drawing room, in three colours', 4),
    row(J(chip('chip-ochre', 'Mustard seed', 'Walls'), chip('chip-green', 'Lichen', 'Woodwork'), chip('chip-pink', 'Setting plaster', 'Ceiling')))), layout={'type': 'constrained'}))

pattern('material-board', 'Material board', 'project', group(J(
    heading('What went into the drawing room', 3),
    gallery([('fabric.jpg', IMG['fabric'], 'Lion and pomegranate linen, curtains'), ('wallpaper.jpg', IMG['wallpaper'], 'Temple wallpaper, the alcoves'),
             ('rug.jpg', IMG['rug'], 'Kelim runner by the window'), ('vase.jpg', IMG['vase'], 'Oxblood vase, mantelpiece')], columns=4, align='wide'),
    row(J(chip('chip-ochre', 'Mustard seed', 'Walls'), chip('chip-green', 'Lichen', 'Woodwork')))), align='wide', layout={'type': 'default'}),
    description='Fabric, paper, rugs and objects from one room, with the paint colours underneath.')

pattern('project-gallery', 'Project gallery (opens large)', 'project', gallery(
    [('living.jpg', IMG['living'], 'Drawing room'), ('hall.jpg', IMG['hall'], 'Hall'), ('dining.jpg', IMG['dining'], 'Dining room'),
     ('bedroom.jpg', IMG['bedroom'], 'Main bedroom'), ('kitchen.jpg', IMG['kitchen'], 'Kitchen'), ('bath.jpg', IMG['bath'], 'Bathroom')], columns=3, align='wide'))

pattern('before-after-room', 'Before and after, one room', 'project', columns(
    (None, image('bath.jpg', IMG['bath'], 'Before: the bathroom as we found it, taps dripping')),
    (None, image('kitchen.jpg', IMG['kitchen'], 'After: the kitchen next door, with the dresser we found in Lauder')), align='wide'))

pattern('designer-note', 'Designer\u2019s note', 'project', group(J(
    heading('Why the ceiling is pink', 5),
    para('North-facing rooms in Edinburgh go grey by three in the afternoon. A warm ceiling puts some of the light back. Nobody notices it is pink until you tell them.')),
    className='is-style-putty'))

pattern('client-testimonial', 'Client testimonial', 'about', quote(
    'We gave Wren a list of what we could not part with and she built the rooms around it. The piano has never looked so good.', 'Fiona and Hamish Mackenzie, Stockbridge, 2025'))

pattern('process-steps', 'How a project runs, with pictures', 'services', group(J(
    heading('How a project runs', 2, fontSize='x-large'),
    grid(J(*[stack(J(image(f, IMG[f[:-4]], className='is-style-crop-square'), heading(h, 4), para(t, fontSize='small'))) for f, h, t in [
        ('hall.jpg', 'First visit', 'Two hours at your house. We look, measure and ask what stays.'),
        ('wallpaper.jpg', 'Scheme', 'Paint, paper, fabric and a furniture plan, room by room.'),
        ('dining.jpg', 'Making it happen', 'We order, chase, supervise the builder and hang the curtains.'),
        ('living.jpg', 'Install day', 'Everything arrives on one day. You come home to finished rooms.')]]), min_width='13rem', align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('services-cards', 'Services, three ways in', 'services', grid(J(*[group(J(heading(h, 3), para(t), para(p_, fontSize='large')), className='is-style-putty') for h, t, p_ in [
    ('First visit', 'Two hours at your house, notes and a colour list you can use without us.', '£350'),
    ('One room', 'Design, drawings, sourcing and one install day.', 'From £2,800'),
    ('Whole house', 'Design and project management with your builder.', '12% of the budget')]]), min_width='16rem', align='wide'))

pattern('product-spotlight', 'Product spotlight', 'shop', media_text('lamp.jpg', IMG['lamp'], J(
    heading('The Ormond lamp', 3),
    para('Lacquered and hand-painted base, pleated silk shade in claret, 68 cm tall. We rewire every one in the studio with a braided flex.'),
    para('£340', fontSize='large'),
    buttons(('See it in the shop', '/shop/'))), width=40, className='is-style-putty', align='wide'))

pattern('shop-by-room', 'Shop by room', 'shop', group(J(
    heading('Shop by room', 3),
    grid(J(*[stack(J(image(f, IMG[f[:-4]], href='/shop/', className='is-style-crop-portrait'), heading('<a href="/shop/">%s</a>' % n, 4))) for f, n in [
        ('hall.jpg', 'Hall'), ('living.jpg', 'Drawing room'), ('dining.jpg', 'Dining room'), ('bedroom.jpg', 'Bedroom')]]), min_width='12rem', align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('sample-box', 'Sample box', 'fabric', group(J(
    heading('A box of cuttings', 3),
    para('Five fabric cuttings, a half-metre of wallpaper and four painted paint cards, posted in a box. £12, refunded on your first order.'),
    buttons(('Order a sample box', '/shop/'))), className='is-style-claret', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('antiques-note', 'How we buy antiques', 'shop', columns(
    ('40%', image('chair.jpg', IMG['chair'])),
    (None, J(heading('How we buy antiques', 3),
             para('We go to about ten sales a year, mostly in the Borders and Northumberland, and buy what we would put in a client\u2019s house. Chairs are reglued and recovered before they go on sale. Lamps are rewired.'),
             para('Antiques are one-offs. If one has gone, ask: we often know where there is another.'))), align='wide', verticalAlignment='center'))

pattern('press-list', 'Press', 'about', group(J(
    heading('Written about in', 4),
    lst(['<em>The Scotsman Magazine</em>, the Stockbridge flat, March 2026', '<em>House &amp; Garden</em>, a Borders dining room, October 2025', '<em>Homes &amp; Interiors Scotland</em>, the shop, May 2024'])),
    className='is-style-rule-top'))

pattern('visit-shop', 'Visit the shop', 'contact', media_text('hall.jpg', IMG['hall'], J(
    heading('Come to the shop', 3),
    para('14 Hamilton Place, Stockbridge. Wednesday to Saturday, 10am to 5pm (4pm on Saturdays). Dogs welcome, and there is usually one asleep under the desk.'),
    para('<a href="/contact/">Directions and contact</a>')), width=45, align='wide', right=True))

pattern('shop-page', 'Page: shop intro', 'shop', J(pattern_ref('shop-by-room'), pattern_ref('product-spotlight'), pattern_ref('antiques-note'), pattern_ref('sample-box')), block_types='core/post-content')

pattern('page-home-extra', 'Page: whole front page', 'featured', J(
    pattern_ref('hero-latest-project'), pattern_ref('projects-grid'), pattern_ref('shop-categories'), pattern_ref('claret-cta')), block_types='core/post-content')

pattern('post-list', 'Search results list', 'query', inherit_query(
    group(columns(('22%', dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover')), (None, J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30)))),
          className='is-style-rule-top'), align='wide'), inserter=False)

# ---------------------------------------------------------------- templates
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('hero-latest-project'), pattern_ref('projects-grid'), pattern_ref('the-edit'), pattern_ref('shop-categories'), pattern_ref('client-testimonial')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|70'}}),
    pattern_ref('claret-cta'), template_part('footer', 'footer')))

write('templates/home.html', page_template(J(
    heading('Interiors', 1, align='wide'),
    para('Houses and flats we have finished since 2017, newest first. Each one is written up room by room, with the paint colours and the pieces you can buy.', align='wide', fontSize='large'),
    dyn('categories', className='is-style-inline-list', align='wide'), spacer('var:preset|spacing|40'),
    pattern_ref('projects-archive')), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/index.html', open(os.path.join(D, 'templates/home.html')).read())

write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', level=1),
    dyn('term-description', align='wide'),
    pattern_ref('projects-archive')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide', level=1),
    dyn('search', label='Search', showLabel=False, buttonText='Search', align='wide'),
    pattern_ref('post-list')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/404.html', page_template(J(
    heading('That room has been knocked through', 1),
    para('The page you wanted is not here any more. The projects and the shop are both still open.', fontSize='large'),
    dyn('search', label='Search', showLabel=False, buttonText='Search'),
    buttons(('See the interiors', '/interiors/'), ('Go to the shop', '/shop/', {'className': 'is-style-text-link'}))), layout={'type': 'constrained'}, style=MAINPAD))

SINGLE = J(template_part('header', 'header'), group(J(
    group(J(dyn('post-terms', term='category'), dyn('post-title', level=1), dyn('post-excerpt', showMoreOnPage=False, fontSize='large')), layout={'type': 'constrained'}),
    dyn('post-featured-image', align='wide', aspectRatio='3/2', scale='cover'),
    dyn('post-content', align='full', layout={'type': 'constrained'}),
    pattern_ref('pieces-in-project'),
    group(J(dyn('post-navigation-link', type='previous', label='Previous project', showTitle=True),
            dyn('post-navigation-link', label='Next project', showTitle=True)),
          align='wide', className='is-style-rule-top', layout={'type': 'flex', 'justifyContent': 'space-between'})),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|60', 'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|60'}}}),
    template_part('footer', 'footer'))
write('templates/single.html', SINGLE)
write('templates/single-project.html', SINGLE)

write('templates/page.html', page_template(J(
    dyn('post-title', level=1),
    dyn('post-content', layout={'type': 'constrained'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1),
    spacer('var:preset|spacing|40'),
    dyn('post-content', layout={'type': 'constrained', 'contentSize': '960px'})), layout={'type': 'constrained', 'contentSize': '960px'}, style=MAINPAD))

print('room built')

# ---------------------------------------------------------------- demo: four projects told room by room
import re
PHPIMG = re.compile(r"<\?php echo esc_url\( get_theme_file_uri\( 'assets/images/([\w.-]+)' \) \); \?>")
def as_post(m):
    return PHPIMG.sub(lambda x: '/wp-content/themes/room/assets/images/' + x.group(1), m)


def credits_(where, when, photo):
    return J(heading('Credits', 4), ruled([('Where', where), ('Finished', when), ('Photography', photo), ('Styling', 'Priya Shah')]))


STORIES = {
    'A townhouse hall in the New Town': J(
        para('A five-storey house on Heriot Row, bought by a couple who had lived with a grey hall for eleven years. They asked for three rooms: the hall, the drawing room and their bedroom.', fontSize='large'),
        room_block('The hall', 'chip-pink', 'Setting plaster, estate emulsion', 'hall.jpg', 'full', 'We took up the runner and had the marble table repolished in the hall itself, because it would not fit through the door. The %s on it came from our shop.' % piece('oxblood vase', '£165')),
        room_block('The drawing room', 'chip-ochre', 'Mustard seed', 'living.jpg', 'full', 'Two sofas kept, one sold. The %s sits by the window where the light is best for reading.' % piece('Tay needlepoint armchair', '£2,400')),
        room_block('The bedroom', 'chip-blue', 'Slate sky, dead flat', 'bedroom.jpg', 'full', 'Heavy interlined curtains in our %s, because the street lamps are right outside.' % piece('lion and pomegranate linen', '£96 a metre')),
        credits_('Heriot Row, Edinburgh', 'September 2025', 'Callum Fraser')),
    'A dining room for twelve in the Borders': J(
        para('A family house near Kelso where Sunday lunch is for whoever turns up. The dining room had to seat twelve and the kitchen had to feed them.', fontSize='large'),
        room_block('The dining room', 'chip-green', 'Lichen, eggshell, on panelling', 'dining.jpg', 'pair', 'The panelling went from brown varnish to green eggshell over two weeks. The %s runs the length of the sideboard.' % piece('kelim runner', '£780')),
        room_block('The kitchen', 'chip-ochre', 'Mustard seed on the dresser', 'kitchen.jpg', 'full', 'We found the dresser at a farm sale in Lauder and painted the inside yellow. Pair of %s on the table.' % piece('brass pricket candlesticks', '£220 each')),
        room_block('A bedroom', 'chip-pink', 'Setting plaster', 'bedroom.jpg', 'full', 'The guest room, for the people who stay after Sunday lunch. A %s at the end of the bed.' % piece('low ash stool', '£390')),
        credits_('Near Kelso, Scottish Borders', 'June 2025', 'Morven Hay')),
    'A farmhouse kitchen near Peebles': J(
        para('The clients asked for a kitchen that looked as if it had not been designed. We did three rooms on the ground floor of a farmhouse on the Tweed.', fontSize='large'),
        room_block('The kitchen', 'chip-pink', 'Setting plaster, and a small red paper', 'kitchen.jpg', 'full', 'Small red print on the walls, the old dresser, a table for eight under the window and a %s for the plants.' % piece('oxblood vase', '£165')),
        room_block('The sitting room', 'chip-ochre', 'Mustard seed', 'living.jpg', 'full', 'The only room with a fire. We added the %s and moved the sofa to face the fire rather than the television.' % piece('Ormond lamp', '£340')),
        room_block('The back hall', 'chip-green', 'Lichen', 'hall.jpg', 'full', 'Boots, dogs, coats. A %s where muddy boots come off.' % piece('corner chair with cushion', '£1,650')),
        credits_('Near Peebles, Tweeddale', 'March 2025', 'Callum Fraser')),
}
content = json.load(open('demos/room/content.json'))
for po in content['posts']:
    if po['title'] in STORIES:
        po.pop('pattern', None)
        po['content'] = as_post(STORIES[po['title']])
if not any(pg['slug'] == 'antiques' for pg in content['pages']):
    content['pages'].insert(3, {'slug': 'antiques', 'title': 'Antiques', 'pattern': 'room/shop-page', 'template': 'page-wide'})
    content['nav'].insert(2, {'label': 'Antiques', 'url': '/antiques/'})
for pg in content['pages']:
    if pg['slug'] == 'contact':
        pg['pattern'] = 'room/contact-page'
json.dump(content, open('demos/room/content.json', 'w'), indent=1, ensure_ascii=False)
print('room demo updated')
