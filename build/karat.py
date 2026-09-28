# Design note (karat, idea 032, jewellery maker)
# Direction: "bench specimen". Each piece is shown like a museum specimen on a flat steel-grey ground,
#   one object per frame, with a small caption label (metal, size, price) set in small caps.
# Fonts: Italiana (display, one weight, thin high-contrast feel) and Petrona (body, true italics).
# Palette: #EEF0F0 bench plate, #1D1B18 text, #7A5A22 18ct gold for prices and the primary action, #E4E2DC wax-grey, #BDB8AE rule.
# Layout idea: centred wordmark header, then asymmetric 5/7 splits (text left, specimen right, image larger);
#   the bespoke page is a vertical ledger of stages, each a ruled row with week, stage name, text and one photo.
import sys, json, os, shutil
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('karat')

_image = image
def image(filename, alt, caption='', **kw):
    """blocks.image plus the inline aspect-ratio/object-fit style core saves, so the ratio survives normalising."""
    out = _image(filename, alt, caption, **kw)
    if kw.get('aspectRatio'):
        st = 'aspect-ratio:%s' % kw['aspectRatio'] + (';object-fit:%s' % kw['scale'] if kw.get('scale') else '')
        out = out.replace('<img ', '<img style="%s" ' % st, 1)
    return out
D = THEME['dir']
for sub in ('patterns', 'templates', 'parts', 'styles'):
    shutil.rmtree(os.path.join(D, sub), ignore_errors=True)

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

P = lambda s: 'var:preset|spacing|%s' % s
pad = lambda t, b=None: {'spacing': {'padding': {'top': P(t), 'bottom': P(b or t)}}}
pal = lambda rows: [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
palette = [('base', '#EEF0F0', 'Bench plate'), ('contrast', '#1D1B18', 'Loupe black'), ('accent', '#7A5A22', '18ct gold'),
           ('surface', '#E4E2DC', 'Wax grey'), ('line', '#BDB8AE', 'Rule'), ('muted', '#55524C', 'Pumice')]

C = lambda slug: 'var:preset|color|%s' % slug
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1280px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(palette), 'duotone': []},
        'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False, 'fontFamilies': fonts, 'fontSizes': [
            {'slug': 'x-small', 'size': '0.875rem', 'name': 'Label', 'fluid': False},
            {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
            {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
            {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.3rem', 'max': '1.5rem'}},
            {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
            {'slug': 'xx-large', 'size': '3.5rem', 'name': 'Title', 'fluid': {'min': '2.4rem', 'max': '3.5rem'}},
            {'slug': 'display', 'size': '5rem', 'name': 'Display', 'fluid': {'min': '2.9rem', 'max': '5rem'}}]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2.5vw, 2rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.75rem, 4vw, 3rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.5rem, 6vw, 4.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3.5rem, 8vw, 6.5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4.5rem, 11vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': C('base'), 'text': C('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': P(40), 'right': P(40)}, 'blockGap': P(30)},
        'elements': {
            'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': C('accent')}},
                     ':focus': {'outline': {'color': C('accent'), 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '1.08', 'letterSpacing': '0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500', 'lineHeight': '1.4', 'letterSpacing': '0.02em'}},
            'button': {'color': {'background': C('accent'), 'text': C('base')},
                       'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': C('accent')},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small', 'letterSpacing': '0.02em'},
                       'spacing': {'padding': {'top': '0.8em', 'bottom': '0.8em', 'left': '1.6em', 'right': '1.6em'}},
                       ':hover': {'color': {'background': C('contrast'), 'text': C('base')}, 'border': {'color': C('contrast')}},
                       ':focus': {'outline': {'color': C('contrast'), 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': C('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'letterSpacing': '0.06em', 'lineHeight': '1'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}}}},
            'core/site-tagline': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'italic'}, 'color': {'text': C('muted')}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'letterSpacing': '0.02em'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}, ':hover': {'color': {'text': C('accent')}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'italic'}, 'color': {'text': C('muted')}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': C('line')}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontStyle': 'italic', 'lineHeight': '1.4'},
                           'border': {'left': {'color': C('accent'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'left': P(40)}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large'},
                               'border': {'top': {'color': C('line'), 'width': '1px', 'style': 'solid'}, 'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(20), 'bottom': P(20)}}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': (':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}html{font-synthesis:none}'
                'table,.wc-block-components-product-price,.woocommerce-Price-amount{font-variant-numeric:tabular-nums lining-nums}'
                '.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.55rem .9rem .55rem 0;text-align:left;vertical-align:top}'
                '.wp-block-table thead th{border-bottom:1px solid var(--wp--preset--color--contrast);font-weight:500;font-variant-caps:all-small-caps;letter-spacing:.04em}'
                '.wp-block-details summary{cursor:pointer;font-weight:500}'
                '.wp-block-quote cite{font-style:normal;font-size:var(--wp--preset--font-size--x-small);display:block;margin-top:.6rem}'
                '.wc-block-components-product-price,.wc-block-grid__product-price,.woocommerce-Price-amount{color:var(--wp--preset--color--accent)}'
                '.wc-block-components-product-image img,.woocommerce-product-gallery img{background:var(--wp--preset--color--surface)}'
                '.wp-block-button__link,.wc-block-components-button{border-radius:0}'
                '.is-style-ledger-row{border-bottom:1px solid var(--wp--preset--color--line);padding:.55rem 0;gap:.2rem 1.5rem!important}.is-style-ledger-row>p{margin:0}'
                '.is-style-ledger-row>p:first-child{flex:0 0 12rem;font-variant-caps:all-small-caps;letter-spacing:.04em}.is-style-ledger-row>p:last-child{flex:1 1 16rem}'
                '.woocommerce-ordering select,.wc-block-components-select select{font:inherit;font-size:var(--wp--preset--font-size--small);border:1px solid var(--wp--preset--color--line);background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast);padding:.4em .6em;border-radius:0}'
                '@media (max-width:600px){.wp-block-table.is-style-ledger thead{display:none}.wp-block-table.is-style-ledger tr{display:block;border-bottom:1px solid var(--wp--preset--color--line);padding:.5rem 0}.wp-block-table.is-style-ledger td{display:block;border:0;padding:0}}'),
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Karat
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A shop and commission site for independent jewellers and goldsmiths who sell a small collection and make bespoke rings.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: karat
Tags: e-commerce, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column
*/''')

def variation(name, title, rows, styles=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}}
    if styles:
        d['styles'] = styles
    jdump('styles/%s.json' % name, d)

variation('silver', 'Silver', [('base', '#EDEFF1', 'Bench plate'), ('contrast', '#1C2026', 'Loupe black'), ('accent', '#4A5560', 'Sterling'),
                               ('surface', '#E0E4E8', 'Polish cloth'), ('line', '#B8BFC6', 'Rule'), ('muted', '#505862', 'Pumice')])
variation('oxblood', 'Oxblood', [('base', '#3A1418', 'Oxblood'), ('contrast', '#E9DCC9', 'Ivory'), ('accent', '#D9B36A', 'Yellow gold'),
                                 ('surface', '#4A1D22', 'Velvet'), ('line', '#6E3A3F', 'Rule'), ('muted', '#CDBBA6', 'Chamois')])
variation('wax', 'Wax', [('base', '#D9D6CC', 'Carving wax'), ('contrast', '#1D1B18', 'Loupe black'), ('accent', '#5E4518', 'Old gold'),
                         ('surface', '#CECABE', 'Sprue'), ('line', '#A9A497', 'Rule'), ('muted', '#47443E', 'Pumice')])

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('rule-bottom', 'Hairline below', ['core/group'], {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}})
section('rule-top', 'Hairline above', ['core/group', 'core/columns'], {'border': {'top': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(40)}, 'margin': {'top': P(60)}}})
section('specimen', 'Specimen ground', ['core/group', 'core/column', 'core/image'], {'color': {'background': C('surface')}, 'spacing': {'padding': {'top': P(30), 'bottom': P(30), 'left': P(30), 'right': P(30)}}, 'css': '& .wp-block-image{margin:0}& img{display:block;width:100%}'})
section('label', 'Specimen label', ['core/paragraph'], {
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45', 'letterSpacing': '0.03em'},
    'css': '&{font-variant-caps:all-small-caps;font-variant-numeric:lining-nums tabular-nums}'})
section('price', 'Price', ['core/paragraph'], {'color': {'text': C('accent')}, 'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}, 'css': '&{font-variant-numeric:lining-nums tabular-nums}'})
section('sold', 'Sold', ['core/paragraph'], {'color': {'text': C('muted')}, 'typography': {'fontSize': 'var:preset|font-size|small', 'fontStyle': 'italic'}})
section('stage', 'Bespoke stage row', ['core/columns'], {
    'border': {'top': {'color': C('contrast'), 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': P(40), 'bottom': P(50)}, 'margin': {'top': '0', 'bottom': '0'}}})
section('ledger-row', 'Ledger row', ['core/group'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('ledger', 'Ledger table', ['core/table'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('velvet', 'Velvet panel', ['core/group'], {
    'color': {'background': C('contrast'), 'text': C('base')},
    'elements': {'link': {'color': {'text': C('base')}}, 'heading': {'color': {'text': C('base')}},
                 'button': {'color': {'background': C('base'), 'text': C('contrast')}, 'border': {'color': C('base')}}},
    'spacing': {'padding': {'top': P(60), 'bottom': P(60)}}})
section('notice', 'Notice line', ['core/group'], {'color': {'background': C('accent'), 'text': C('base')}, 'elements': {'link': {'color': {'text': C('base')}}},
                                                  'typography': {'fontSize': 'var:preset|font-size|x-small', 'letterSpacing': '0.02em'}})

# ---------------------------------------------------------------- patterns
IMG = {
    'hero': ('hero.jpg', 'Yellow gold signet ring with an engraved oval face, photographed alone on a grey ground'),
    'ring-1': ('ring-1.jpg', 'Carnelian intaglio set in gold on a blackened silver ring, beside a small metric scale'),
    'ring-2': ('ring-2.jpg', 'Thin gold ring set with a rectangular red carnelian, on a pale grey ground'),
    'ring-3': ('ring-3.jpg', 'Wide silver ring with a rosette of red garnet cells around a central boss'),
    'ring-4': ('ring-4.jpg', 'Silver bangle with a knotted top and granulated band, beside a thin silver ring set with a pearl'),
    'earring-1': ('earring-1.jpg', 'Pair of plain gold hoop earrings on a light grey ground'),
    'pendant-1': ('pendant-1.jpg', 'Teardrop garnet pendant in gold beside three gold beaded drops'),
    'necklace-1': ('necklace-1.jpg', 'Fine gold chain necklace strung with small green emerald and variscite beads'),
    'stone-1': ('stone-1.jpg', 'Rough blue and yellow sapphire crystals scattered on a white tray'),
    'sketch-1': ('sketch-1.jpg', 'Watercolour design drawing of an ornate gold cup with scrolled handles, on grey paper'),
    'bench-2': ('bench-2.jpg', 'Wooden jeweller\'s bench with an angled lamp, a leather catch skin, pliers and a pull-out drawer'),
    'bench-3': ('bench-3.jpg', 'A wooden tray full of worn goldsmith\'s punches, gravers and small hammers'),
    'tools-1': ('tools-1.jpg', 'Patent drawing of a stepped ring mandrel, front view and cross-section'),
}
def img(key, caption='', **kw):
    f, alt = IMG[key]
    return image(f, alt, caption, **kw)

def specimen(key, name, metal, price, sold=False, href='/shop/'):
    return group(J(group(img(key, href=href, aspectRatio='1', scale='cover'), className='is-style-specimen', layout={'type': 'default'}),
                   para('<a href="%s">%s</a>' % (href, name), fontSize='small'),
                   para(metal, className='is-style-label'),
                   para(price, className='is-style-sold' if sold else 'is-style-price')),
                 layout={'type': 'default'}, style={'spacing': {'blockGap': P(10)}})

pattern('hero-specimen', 'Hero: one specimen and what the workshop makes', 'hero', columns(
    ('42%', J(heading('Rings and small gold things, made at one bench on Magdalen Street', 1),
              para('I\'m Edie Achterberg, a goldsmith in Norwich. I make a short collection in recycled 18ct and 9ct gold and silver, and about forty commissions a year, most of them engagement and wedding rings.'),
              buttons(('Book a free consultation', '/bespoke/#consultation'), ('See the shop', '/shop/', {'className': 'is-style-outline'})))),
    ('58%', J(group(img('hero'), className='is-style-specimen', layout={'type': 'default'}),
              para('Signet ring, hand-engraved oval face. 18ct yellow gold, size N. £1,480', className='is-style-label'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(60)}, 'padding': {'top': P(50), 'bottom': P(60)}}}, verticalAlignment='center'))

pattern('specimen-tray', 'Specimen tray: pieces in the shop with metal and price', 'shop', group(J(
    row(J(heading('In the shop now', 2, fontSize='x-large'), para('<a href="/shop/">Everything in the shop</a>', fontSize='small')), justify='space-between'),
    group(J(specimen('ring-2', 'Carnelian bar ring', '18ct yellow gold, carnelian', '£1,250'),
           specimen('earring-1', 'Plain hoops, pair', '9ct yellow gold, 18 mm', '£395'),
           specimen('pendant-1', 'Garnet drop and three tassels', '18ct yellow gold, garnet', '£720'),
           specimen('ring-4', 'Knot bangle and pearl stacker', 'Recycled silver, freshwater pearl', '£310')), layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'bottom': P(60)}}}))

pattern('one-of-one-grid', 'One of one: single pieces with a sold state', 'shop', group(J(
    heading('One of one', 2, fontSize='x-large'),
    para('Pieces made from old stones and offcuts. There is only one of each. When it has gone, it has gone.'),
    group(J(specimen('ring-1', 'Carnelian seal ring', 'Intaglio in 18ct, oxidised silver shank', '£640'),
           specimen('ring-3', 'Garnet rosette ring', 'Silver-gilt, eight garnet cells', '£880'),
           specimen('necklace-1', 'Emerald and variscite chain', '18ct yellow gold, 44 cm', 'Sold, March 2026', sold=True)), layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'})),
    align='wide', layout={'type': 'default'}))

stages = [
    ('Week 1', 'Consultation', 'We sit at the bench or talk on a video call for about 45 minutes. Bring anything you like: photos, your grandmother\'s ring, a budget. It is free and you are under no obligation.', 'stone-1', 'Stones on the tray at a first consultation'),
    ('Week 1 to 2', 'Sketch and a fixed quote', 'I draw two or three versions to scale and send them with a fixed price. When you pick one, a 40% deposit books your slot at the bench.', 'sketch-1', 'Designs are drawn in pencil and watercolour, at twice real size'),
    ('Week 2 to 4', 'Wax model', 'I carve the ring in jeweller\'s wax. You can come in and try the wax on before it is cast. It is the cheapest moment to change your mind about width or height.', 'bench-3', 'Carving tools and gravers, most of them older than me'),
    ('Week 4 to 5', 'Casting', 'The wax goes to a family casting house in Birmingham\'s Jewellery Quarter and comes back in your metal a week later. For plain bands I skip the wax and forge the ring from wire at the bench.', None, None),
    ('Week 5 to 8', 'Setting and finishing', 'Stones are set by hand under the lamp. Then the ring is filed, sanded and polished, or left with a satin finish if you prefer.', 'bench-2', 'The bench, the lamp and the catch skin that collects every filing'),
    ('Week 8 to 9', 'Hallmarking', 'Every piece over the legal weight is sent to the Birmingham Assay Office, tested and hallmarked with my maker\'s mark, the fineness and the Birmingham anchor. It takes four to six working days.', None, None),
    ('Week 9 to 10', 'Collection', 'You collect from the workshop or I post it insured with Royal Mail Special Delivery. The remaining 60% is due before it leaves.', 'ring-2', 'A finished ring, photographed before collection'),
]
def stage_row(when, name, text, key, cap):
    left = J(para(when, className='is-style-label'), heading(name, 3), para(text))
    right = img(key, cap, aspectRatio='3/2', scale='cover') if key else para('No photo for this stage. It happens somewhere else.', className='is-style-sold')
    return columns(('42%', left), ('58%', right), align='wide', className='is-style-stage', style={'spacing': {'blockGap': {'left': P(60)}}})

pattern('bespoke-stages', 'Bespoke: the stages, one row each with a photo', 'services', group(J(
    heading('How a commission goes', 2, align='wide'),
    J(*[stage_row(*s) for s in stages])), align='wide', layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}}),
    description='The signature pattern: every real stage of a commission with week numbers, text and one photo.')

def ledger(rows):
    return group(J(*[row(J(para(k), para(v)), className='is-style-ledger-row') for k, v in rows]), layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}})

pattern('bespoke-terms', 'Bespoke: deposit and payment terms', 'services', group(J(
    heading('Money and time', 3),
    ledger([('Deposit', '40% when you approve the sketch. Non-refundable once I start the wax.'),
            ('Balance', '60% before collection or posting'),
            ('Bands', '3 to 4 weeks, from £300'),
            ('Engagement rings', '8 to 10 weeks, from £1,400 plus the stone'),
            ('Remodelling old gold', 'Your gold is credited by weight at the day\'s scrap price, or melted into the new ring if there is enough'),
            ('Minimum commission', '£300')])), layout={'type': 'constrained'}))

pattern('lead-time-line', 'Lead time and minimum, in one line', 'services', group(
    para('Bands take 3 to 4 weeks, engagement rings 8 to 10. The minimum commission is £300.', fontSize='x-large', fontFamily='display', style={'typography': {'textAlign': 'center'}}),
    className='is-style-rule-bottom', style=pad(40)), description='The one line most people are looking for.')

pattern('wax-try-on', 'Try on the wax before casting', 'services', columns(
    ('42%', heading('Try it on in wax first', 3)),
    ('58%', para('Before anything is cast, you can come to the workshop and wear the wax model for ten minutes. Rings look bigger on the bench than on a hand. If it needs to be narrower, I carve a new wax at no charge.')),
    align='wide', className='is-style-rule-top'))

pattern('hallmarking-note', 'Hallmarking explained', 'services', columns(
    ('42%', heading('Hallmarking', 3)),
    ('58%', J(para('UK law says gold over 1 gram, silver over 7.78 grams and platinum over 0.5 grams must be hallmarked before it is sold as such. Mine go to the Birmingham Assay Office.'),
              para('The mark has four parts: EA for me, the fineness (750 for 18ct, 375 for 9ct), the Birmingham anchor and a year letter. Ask to see it through the loupe when you collect.', fontSize='small'))),
    align='wide', className='is-style-rule-top'))

pattern('visit-workshop', 'Visit the workshop while your ring is made', 'services', group(J(
    heading('Watch it being made', 3),
    para('You are welcome to visit twice during a commission: once for the wax and once when the stone goes in. Tuesdays and Thursdays, by appointment. There are two steep steps at the door and I have a dog called Brass.')),
    className='is-style-specimen', layout={'type': 'constrained'}))

pattern('consultation-cta', 'Book a free consultation', 'call-to-action', group(J(
    heading('Book a free consultation', 2, style={'typography': {'textAlign': 'center'}}),
    para('45 minutes at the bench on Magdalen Street, or on a video call. Email me two or three dates that suit you and a line about what you have in mind.', align='center'),
    buttons(('Email to book a time', 'mailto:edie@example.com?subject=Consultation'), layout={'type': 'flex', 'justifyContent': 'center'})),
    tag='section', align='full', className='is-style-velvet', anchor='consultation', layout={'type': 'constrained'}))

pattern('pricing-guide', 'Pricing guide in prose', 'services', J(
    heading('What things usually cost', 3),
    para('Plain wedding bands start at £300 in silver, £480 in 9ct and £950 in 18ct gold for a 3 mm court profile. Engagement rings start at £1,400 in 18ct before the stone. Stones vary most: a 0.5 carat old-cut diamond is usually between £900 and £2,000, a Sri Lankan sapphire of the same size £600 to £1,500.'),
    para('Remodelling costs less than you think if the gold is already yours. Resizing is £45 for a plain band.', fontSize='small')))

pattern('metal-options', 'Metal options', 'shop', group(J(
    heading('Metals', 3),
    table([['Platinum 950', 'Grey-white, heavy, never needs replating', 'From £1,100 for a band'],
           ['18ct yellow gold', 'Warm and soft enough to set stones well', 'From £950 for a band'],
           ['9ct yellow gold', 'Paler and harder, good for everyday hoops', 'From £480 for a band'],
           ['Recycled silver', 'Oxidised or polished', 'From £300 for a band']], head=['Metal', 'What it is like', 'Price'], className='is-style-ledger'),
    para('All metal is recycled and bought from a UK refiner. I don\'t work in rose or white gold: white gold needs rhodium plating every year or two, and I would rather sell you platinum once.', fontSize='small')),
    layout={'type': 'default'}))

sizes = [('F', '3', '44.2', '14.1'), ('H', '4', '46.8', '14.9'), ('J', '5', '49.3', '15.7'), ('L', '6', '51.9', '16.5'), ('N', '7', '54.4', '17.3'),
         ('P', '8', '57.0', '18.1'), ('R', '9', '59.5', '18.9'), ('T', '10', '62.1', '19.8'), ('V', '11', '64.6', '20.6')]
pattern('ring-size-table', 'Ring size table', 'shop', group(J(
    heading('UK, US and European sizes', 3),
    table([list(s) for s in sizes], head=['UK', 'US', 'Circumference, mm', 'Inside diameter, mm'], className='is-style-ledger'),
    para('Half sizes are made on request. Print this page at 100% if you want to check a ring you own against the diameters.', fontSize='small')),
    layout={'type': 'default'}))

pattern('measure-at-home', 'How to measure at home', 'shop', columns(
    ('30%', img('tools-1', 'A ring mandrel, the tapered steel stick jewellers size rings on')),
    ('70%', J(heading('Measuring at home', 3), lst([
        'Wrap a strip of paper round the base of the finger, not too tight.',
        'Mark where it overlaps and measure the length in millimetres.',
        'Find the nearest circumference in the table. If you are between two sizes, pick the larger.',
        'Measure at the end of the day when fingers are warm. Cold fingers shrink by half a size.'], ordered=True),
        para('If the knuckle is much bigger than the finger, size for the knuckle and ask me about a slightly squared inside.', fontSize='small'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('free-ring-sizer', 'Ask for a free ring sizer', 'call-to-action', group(J(
    heading('Free ring sizer by post', 4),
    para('I post a plastic sizer anywhere in the UK for free. Email your address to <a href="mailto:edie@example.com?subject=Ring%20sizer">edie@example.com</a> with "ring sizer" in the subject. It arrives in two or three days and you can keep it.')),
    className='is-style-specimen', layout={'type': 'default'}))

pattern('care-guide', 'Care guide', 'text', J(
    heading('Looking after your ring', 3),
    lst(['Take it off for the gym, gardening and bleach. Gold scratches, stones chip.',
         'Clean it in warm water with a drop of washing-up liquid and a soft toothbrush.',
         'Bring it back once a year and I will check the claws and polish it for free.',
         'Silver darkens. That is normal. A silver cloth fixes it in a minute.'])))

pattern('sustainability-note', 'Sustainability, briefly', 'text', J(
    heading('Where the materials come from', 3),
    para('All my gold and silver is recycled, bought from a UK refiner that melts down old jewellery and dental gold. Diamonds are old cut stones bought from dealers in Hatton Garden, or ones you already own. Coloured stones come from two cutters I know by name, in Sri Lanka and Idar-Oberstein.'),
    para('My opinion: the greenest ring is the one already in your drawer. Remodelling it is my favourite kind of work.', fontSize='small')))

pattern('delivery-guide', 'Delivery and returns', 'shop', group(J(
    heading('Delivery and returns', 4),
    ledger([('UK', 'Royal Mail Special Delivery, insured, £8, next working day'), ('Europe', 'DHL Express, insured, £28, 2 to 4 days'), ('Elsewhere', 'Ask first, quoted per parcel')]),
    para('Shop pieces can be returned within 14 days, unworn. Commissions and resized rings can\'t be returned, because they were made for one finger.', fontSize='small')),
    layout={'type': 'default'}))

pattern('faq', 'Questions people ask', 'text', J(
    details('Can I bring my own stone or gold?', para('Yes. I check stones under the loupe first and tell you honestly if one is too soft or too chipped for daily wear.')),
    details('Can you copy a ring I saw online?', para('No. I will make something with the same feeling, drawn from scratch, but I won\'t copy another maker\'s design.')),
    details('Do you do lab-grown diamonds?', para('Not at the moment. I use old cut diamonds, coloured stones, or stones you bring.')),
    details('How do I pay?', para('Bank transfer or card. The deposit and balance can be split into three payments for engagement rings.')),
    details('Is there parking?', para('Two pay-and-display spaces on Magdalen Street and the Anglia Square car park five minutes away. The 501 bus stops outside.'))))

pattern('about-bio', 'About the maker', 'about', columns(
    ('58%', J(para('Edie Achterberg (b. 1988, Groningen) trained at the School of Jewellery in Birmingham and spent six years at a Hatton Garden workshop setting other people\'s diamonds. She opened her own bench on Magdalen Street, Norwich, in 2019.', fontSize='large'),
              para('She works alone, with Brass the whippet, in a first-floor room above a violin repairer. Most of her work is wedding and engagement rings, and remodelling family jewellery into something people will actually wear.'),
              para('She makes everything by hand, except the casting. She does not sell other people\'s work, does not work in rose gold and closes the workshop for the whole of August.'))),
    ('42%', J(group(img('bench-2'), className='is-style-specimen', layout={'type': 'default'}), para('The bench at 14 Magdalen Street', className='is-style-label'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('find-us', 'Find the workshop', 'contact', columns(
    (None, J(heading('Workshop', 5), para('14 Magdalen Street, first floor<br>Norwich NR3 1HU<br>Ring the top bell'))),
    (None, J(heading('Opening', 5), para('Tuesday to Saturday, 10 to 5<br>Consultations by appointment<br>Closed in August'))),
    (None, J(heading('Get in touch', 5), para('<a href="mailto:edie@example.com">edie@example.com</a><br><a href="tel:+441603496211">01603 496211</a><br>I answer after 4pm, when the torch is off'))),
    align='wide', className='is-style-rule-top'))

pattern('journal-strip', 'Journal: three recent commission stories', 'posts,query', group(J(
    row(J(heading('From the bench', 2, fontSize='x-large'), para('<a href="/journal/">The whole journal</a>', fontSize='small')), justify='space-between'),
    query(J(group(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), className='is-style-specimen', layout={'type': 'default'}),
            dyn('post-date'), dyn('post-title', isLink=True, level=3, fontSize='large')),
          per_page=3, layout={'type': 'grid', 'columnCount': 3}, align='wide')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': P(60), 'bottom': P(60)}}}))

pattern('post-list', 'Journal list', 'posts,query', inherit_query(
    columns(('33%', group(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), className='is-style-specimen', layout={'type': 'default'})),
            ('67%', J(dyn('post-date'), dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', excerptLength=30, moreText='Read on'))),
            className='is-style-stage', style={'spacing': {'blockGap': {'left': P(50)}}}),
    align='wide'), inserter=False)

pattern('journal-making-photos', 'Journal post: making photos in order', 'posts', J(
    para('This one started with a stone the client had carried around in a matchbox for eleven years.'),
    gallery([('stone-1.jpg', IMG['stone-1'][1], 'Choosing the stone'), ('sketch-1.jpg', IMG['sketch-1'][1], 'Drawing at twice size'),
             ('bench-3.jpg', IMG['bench-3'][1], 'Carving the wax'), ('bench-2.jpg', IMG['bench-2'][1], 'Setting at the bench')], columns=2, align='wide'),
    para('The wax was carved twice. The first was 1 mm too tall and caught on her gloves. The second one is the ring.')),
    block_types='core/post-content', description='A commission story told through bench photos, one per stage.')

pattern('engagement-note', 'Engagement rings, briefly', 'services', columns(
    ('42%', J(group(img('ring-2'), className='is-style-specimen', layout={'type': 'default'}), para('Carnelian bar ring, a plain alternative to a solitaire', className='is-style-label'))),
    ('58%', J(heading('Engagement rings', 2), para('Most of my commissions are engagement rings. You don\'t need to know what you want. Most people arrive with a budget, a photo of a hand and a sense that they don\'t want a big claw-set solitaire.'),
              para('Engagement rings start at £1,400 in 18ct gold before the stone and take 8 to 10 weeks. If there is a date in mind, tell me at the start.'),
              buttons(('Book a free consultation', '/bespoke/#consultation')))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('notice-christmas', 'Notice: Christmas order dates', 'banner', group(
    para('Last dates for Christmas: shop orders by 18 December, resizing by 5 December. New commissions booked now are ready from February.', style={'typography': {'textAlign': 'center'}}),
    tag='aside', align='full', className='is-style-notice', style=pad(20), layout={'type': 'constrained'}),
    description='Seasonal notice bar. Change the dates each year and remove it in January.')

pattern('pullquote-client', 'Client quote', 'testimonials', J(
    quote('I brought in my mother\'s wedding ring and a garnet from a brooch nobody wore. Edie made one ring out of both. I have not taken it off since.', 'Hannah Okoro, Wymondham, commissioned in May 2025')))


# ---------------------------------------------------------------- commission stories and services (round 2)
pattern('story-brought-in', 'Commission story: what they brought in', 'commission-story', columns(
    ('42%', group(img('ring-3'), className='is-style-specimen', layout={'type': 'default'})),
    ('58%', J(heading('What came in', 3), para('A silver-gilt ring with eight garnet cells, two of them empty, and a bent shank. It had been in a biscuit tin since 1974.'),
              para('Brought in by Priya Shah, Eaton, in February 2026', className='is-style-label'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('story-before-after', 'Commission story: before and after', 'commission-story', columns(
    (None, J(group(img('ring-3', aspectRatio='1', scale='cover'), className='is-style-specimen', layout={'type': 'default'}), para('Before: two empty cells, shank bent at the back', className='is-style-label'))),
    (None, J(group(img('ring-1', aspectRatio='1', scale='cover'), className='is-style-specimen', layout={'type': 'default'}), para('After: a new seal ring from the best stone', className='is-style-label'))),
    align='wide'))

pattern('story-specs', 'Commission story: metal, stone and size', 'commission-story', group(J(
    heading('The ring', 5),
    ledger([('Metal', '18ct yellow gold, recycled, 4.8 g'), ('Stone', 'Carnelian intaglio, re-polished, 11 x 9 mm'), ('Size', 'M and a half, squared inside'), ('Hallmark', 'Birmingham, 2026'), ('Time', 'Six weeks from consultation to collection')])),
    layout={'type': 'constrained'}))

pattern('story-cost', 'Commission story: what it cost', 'commission-story', group(J(
    heading('What it cost', 5),
    ledger([('Design and making', '£620'), ('New gold, net of the old', '£180'), ('Hallmarking', '£18'), ('Total', '£818, paid 40% at the sketch and 60% at collection')])),
    layout={'type': 'constrained'}), description='The price broken down plainly, as people ask for it.')

pattern('story-quote', 'Commission story: the client, quoted', 'commission-story', group(
    quote('My grandmother wore it to every wedding in the family. Now I do, and it fits.', 'Priya Shah, Eaton, collected in April 2026'), layout={'type': 'constrained'}))

pattern('story-stages', 'Commission story: three stages in pictures', 'commission-story', gallery([
    ('sketch-1.jpg', IMG['sketch-1'][1], 'The drawing'), ('bench-3.jpg', IMG['bench-3'][1], 'The wax'), ('bench-2.jpg', IMG['bench-2'][1], 'Setting at the bench')], columns=3, align='wide'))

pattern('story-garnet-seal', 'Commission story layout: the garnet ring', 'commission-story', J(
    pattern_ref('story-brought-in'), pattern_ref('story-before-after'), pattern_ref('story-stages'), pattern_ref('story-specs'), pattern_ref('story-cost'), pattern_ref('story-quote')),
    block_types='core/post-content', description='A complete commission story built from the story patterns.')

pattern('story-signet', 'Commission story layout: a signet ring', 'commission-story', J(
    para('Tom\'s partner wanted a signet ring for his fortieth, engraved with the outline of the Norfolk coast rather than a crest.', fontSize='large'),
    columns(('42%', group(img('hero'), className='is-style-specimen', layout={'type': 'default'})),
            ('58%', J(heading('The engraving', 3), para('The coastline was traced from an Ordnance Survey map, reduced to 14 mm and cut by hand with a flat graver. Cromer is the small dot on the top edge.'))),
            align='wide', verticalAlignment='center'),
    group(J(heading('The ring', 5), ledger([('Metal', '18ct yellow gold, 9.2 g'), ('Face', 'Oval, 14 x 10 mm, hand engraved'), ('Time', 'Four weeks'), ('Cost', '£1,480')])), layout={'type': 'constrained'}),
    pattern_ref('story-quote')), block_types='core/post-content')

pattern('story-bands', 'Commission story layout: two bands from one ring', 'commission-story', J(
    para('Sam and Joe had one ring between them: Sam\'s grandmother\'s wedding band, 22ct and very thin. They wanted two.', fontSize='large'),
    columns((None, J(group(img('earring-1', aspectRatio='1', scale='cover'), className='is-style-specimen', layout={'type': 'default'}), para('Two plain hoops in the same gold, for scale', className='is-style-label'))),
            (None, J(heading('How', 4), para('I melted the old band with new recycled 18ct and drew two 2 mm court bands from the same ingot, so both rings hold some of the original. The grandmother\'s ring weighed 2.9 g. Each new band weighs 3.4 g.'))), align='wide'),
    pattern_ref('story-cost')), block_types='core/post-content')

pattern('repairs-prices', 'Repairs, resizing and restringing (price list)', 'services', group(J(
    heading('Repairs and resizing', 3),
    table([['Resize a plain band, up or down two sizes', '£45', '1 week'], ['Resize a stone-set ring', 'from £75', '2 weeks'], ['Re-tip a worn claw', '£35 per claw', '1 week'], ['Restring pearls, knotted', '£4 per inch', '2 weeks'], ['Solder a broken chain', '£25', 'While you wait, most days']], head=['Job', 'Price', 'Usually takes']),
    para('I only repair things I can hallmark or identify. I don\'t repair watches, costume jewellery or plated silver.', fontSize='small')),
    layout={'type': 'default'}), description='A real price list, so it is a table.')

pattern('valuations', 'Insurance valuations', 'services', columns(
    ('42%', heading('Valuations', 3)),
    ('58%', J(para('Written valuations for insurance, £60 for the first piece and £25 for each piece after that, done at the bench while you wait. I photograph and weigh everything and send a PDF the same day.'),
              para('For probate I refer you to a registered valuer. It needs a different licence.', fontSize='small'))),
    align='wide', className='is-style-rule-top'))

pattern('engraving', 'Engraving options', 'shop', columns(
    ('42%', group(img('hero'), className='is-style-specimen', layout={'type': 'default'})),
    ('58%', J(heading('Engraving', 3), para('Hand engraving inside a band costs £30 for up to 20 letters. Outside, on a signet face, from £120. I engrave in a plain roman or an upright script, and I will tell you if a name is too long to read.'))),
    align='wide', verticalAlignment='center'))

pattern('gift-voucher', 'Gift vouchers', 'shop', group(J(
    heading('Gift vouchers', 4),
    para('From £50, on a printed card posted in a small box. They can be spent on anything, including a commission, and last two years.')),
    className='is-style-specimen', layout={'type': 'default'}))

pattern('appointment-card', 'Book an appointment (card)', 'call-to-action', group(J(
    heading('Come to the bench', 4),
    para('Tuesdays and Thursdays, 45 minutes, free. Email two dates to <a href="mailto:edie@example.com?subject=Appointment">edie@example.com</a>.'),
    buttons(('Email to book', 'mailto:edie@example.com?subject=Appointment'))),
    className='is-style-rule-top', layout={'type': 'default'}))

pattern('gold-guide', 'Which gold? A short guide', 'text', group(J(
    heading('Which gold?', 3),
    columns((None, J(heading('9ct', 5), para('37.5% gold. Paler, harder, cheaper. Good for hoops and chains that get knocked about.'))),
            (None, J(heading('18ct', 5), para('75% gold. Warmer and softer, the one most engagement rings are made in. Holds stones well.'))),
            (None, J(heading('22ct', 5), para('91.6% gold. Very yellow and soft. I use it only for bands that won\'t be worn every day.'))), align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('new-in', 'New in the shop (single piece, large)', 'shop', columns(
    ('58%', group(img('necklace-1'), className='is-style-specimen', layout={'type': 'default'})),
    ('42%', J(para('New this month', className='is-style-label'), heading('Emerald and variscite chain', 2), para('A fine 18ct chain with small green beads, 44 cm, one of one. It sold in March, but I have enough stones for two more like it.'),
              buttons(('Ask about the next one', 'mailto:edie@example.com?subject=Chain')))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': P(60)}}}))

# page layouts
pattern('page-bespoke', 'Page: bespoke commissions', 'services', J(
    para('A commission is a ring or pendant made for one person, from a first chat to the hallmark. It takes 3 to 10 weeks depending on what it is. Here is every step, with what it costs and when you pay.', fontSize='large'),
    pattern_ref('lead-time-line'), pattern_ref('bespoke-stages'), pattern_ref('bespoke-terms'), pattern_ref('wax-try-on'), pattern_ref('hallmarking-note'),
    pattern_ref('pricing-guide'), pattern_ref('visit-workshop'), pattern_ref('pullquote-client'), pattern_ref('consultation-cta')), block_types='core/post-content')
pattern('page-ring-sizes', 'Page: ring sizes', 'shop', J(
    para('Getting the size right the first time saves a resize and a week. Here are three ways.', fontSize='large'),
    pattern_ref('free-ring-sizer'), pattern_ref('ring-size-table'), pattern_ref('measure-at-home')), block_types='core/post-content')
pattern('page-care', 'Page: care and materials', 'text', J(pattern_ref('care-guide'), pattern_ref('gold-guide'), pattern_ref('metal-options'), pattern_ref('sustainability-note'), pattern_ref('delivery-guide')), block_types='core/post-content')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('about-bio'), pattern_ref('pullquote-client'), pattern_ref('find-us')), block_types='core/post-content')
pattern('page-contact', 'Page: contact', 'contact', J(
    para('Email is best. I answer after 4pm on working days, when the torch is off and my hands are clean.', fontSize='large'),
    pattern_ref('find-us'), heading('Questions people ask', 3), pattern_ref('faq')), block_types='core/post-content')

pattern('page-repairs', 'Page: repairs and valuations', 'services', J(para('Most repairs are done at the bench in a week. Bring the piece in on a Tuesday or Thursday, or post it insured.', fontSize='large'),
    pattern_ref('repairs-prices'), pattern_ref('valuations'), pattern_ref('engraving'), pattern_ref('gift-voucher'), pattern_ref('appointment-card')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(J(
    group(J(dyn('site-title', level=0, textAlign='center'), dyn('site-tagline', textAlign='center')), layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'center'}, style={'spacing': {'blockGap': P(10)}}),
    row(dyn('navigation', layout={'type': 'flex', 'justifyContent': 'center'}, overlayMenu='mobile'), justify='center')),
    tag='header', align='full', className='is-style-rule-bottom', style={'spacing': {'padding': {'top': P(40), 'bottom': P(20)}, 'blockGap': P(30)}}, layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'center'}))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0), para('Rings, earrings and pendants made by hand in recycled gold and silver. Commissions from £300.', fontSize='small'))),
        (None, J(heading('Workshop', 6), para('14 Magdalen Street, first floor<br>Norwich NR3 1HU<br>Tuesday to Saturday, 10 to 5', fontSize='small'))),
        (None, J(heading('Write or call', 6), para('<a href="mailto:edie@example.com">edie@example.com</a><br><a href="tel:+441603496211">01603 496211</a><br><a href="https://www.instagram.com/">Instagram</a>', fontSize='small'))),
        align='wide'),
    para('Demo photographs are public domain objects from the Metropolitan Museum of Art and pictures from Wikimedia Commons, standing in for the maker\'s own work.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-rule-top', style={'spacing': {'padding': {'top': P(50), 'bottom': P(40)}, 'margin': {'top': '0'}}}))

write('parts/notice.html', pattern_ref('notice-christmas'))

# ---------------------------------------------------------------- templates
def tpl(name, inner, top=60, bottom=70):
    write('templates/%s.html' % name, page_template(inner, style=pad(top, bottom)))

write('templates/front-page.html', page_template(J(
    pattern_ref('hero-specimen'), pattern_ref('specimen-tray'), pattern_ref('lead-time-line'), pattern_ref('engagement-note'), pattern_ref('new-in'),
    pattern_ref('journal-strip'), pattern_ref('consultation-cta')), style={'spacing': {'padding': {'bottom': '0'}}}))
tpl('home', J(heading('Journal', 1, align='wide'), para('Commission stories, stones, and what happens at the bench.', align='wide'), pattern_ref('post-list')))
tpl('archive', J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('post-list')))
tpl('index', J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')))
tpl('search', J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Signet, garnet, resizing', buttonText='Search', align='wide'), pattern_ref('post-list')))
tpl('404', J(heading('That page has been melted down', 1), para('The link is old or mistyped. The <a href="/shop/">shop</a> and the <a href="/bespoke/">bespoke page</a> are the two places most people want.'),
             dyn('search', label='Search', showLabel=False, placeholder='Signet, garnet, resizing', buttonText='Search')))
tpl('page', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained'})))
tpl('page-wide', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1280px'})))
tpl('single', J(
    columns(('42%', J(dyn('post-date'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-terms', term='category'))),
            ('58%', group(dyn('post-featured-image', aspectRatio='4/3'), className='is-style-specimen', layout={'type': 'default'})),
            align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': P(60)}}}),
    dyn('post-content', align='wide', layout={'type': 'constrained'}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Older', showTitle=True), dyn('post-navigation-link', label='Newer', showTitle=True)), justify='space-between'),
          align='wide', className='is-style-rule-top', layout={'type': 'default'})), top=50)
print('karat built')

# ---------------------------------------------------------------- demo content
P_ = lambda *ps: J(*[para(p) for p in ps])
posts = [
    {'title': 'Anna\'s grandmother\'s garnets, remade', 'category': 'commissions', 'image': 'pendant-1.jpg', 'excerpt': 'A Victorian brooch nobody wore became a drop pendant and three tassels.',
     'content': P_('Anna brought in a brooch with eleven garnets, two of them loose, and a broken pin. We kept the best stone for a drop pendant and used the gold from the brooch frame for three small tassels.', 'It took five weeks. The brooch gold was 15ct, so the new parts are 15ct too, hallmarked in Birmingham with the old mark noted on the certificate.')},
    {'title': 'A seal ring from a biscuit-tin garnet ring', 'category': 'commissions', 'image': 'ring-1.jpg', 'excerpt': 'Eight garnet cells, two missing, one very good carnelian underneath.', 'pattern': 'karat/story-garnet-seal'},
    {'title': 'A signet with the Norfolk coast on it', 'category': 'commissions', 'image': 'hero.jpg', 'excerpt': 'A fortieth birthday present, engraved by hand at 14 mm.', 'pattern': 'karat/story-signet'},
    {'title': 'Two wedding bands from one grandmother\'s ring', 'category': 'commissions', 'image': 'earring-1.jpg', 'excerpt': 'One thin 22ct band, melted and drawn into two.', 'pattern': 'karat/story-bands'},
    {'title': 'An engagement ring in recycled platinum, from wax to hallmark', 'category': 'commissions', 'image': 'bench-2.jpg', 'excerpt': 'Nine weeks, two waxes and one very patient client.', 'pattern': 'karat/journal-making-photos'},
    {'title': 'Choosing a sapphire from a tray of rough', 'category': 'stones', 'image': 'stone-1.jpg', 'excerpt': 'Why I buy some stones uncut, and what you can tell before they are polished.',
     'content': P_('Twice a year a cutter in Ratnapura sends me a tray of rough sapphires. Most are grey and cloudy. A few are the colour of the sea off Cromer in February, which is the colour people ask for.', 'Buying rough is cheaper and I know where the stone came from. It is also slower: cutting adds four weeks to a commission.')},
    {'title': 'Why most of my diamonds are old', 'category': 'stones', 'image': 'ring-2.jpg', 'excerpt': 'Old cut stones sparkle differently, cost less and are already in the world.',
     'content': P_('An old European cut diamond has a small table and a tall crown. Under candlelight it looks like a fire. Under a shop spotlight it looks a bit sleepy, which is why the trade underprices them.', 'I buy them loose from two dealers in Hatton Garden. For most rings they cost 20 to 40 percent less than a new stone of the same size. That is my opinion and I am sticking to it.')},
    {'title': 'Sizing a ring for a big knuckle', 'category': 'workshop', 'image': 'tools-1.jpg', 'excerpt': 'When the knuckle is two sizes bigger than the finger.',
     'content': P_('If a ring fits the knuckle it spins on the finger. If it fits the finger it will not go over the knuckle. The fix is a slightly squared inside, or two small beads of gold at the bottom of the shank.', 'Either way, measure the knuckle and the base of the finger and send me both numbers.')},
    {'title': 'Workshop open day, Saturday 13 December', 'category': 'workshop', 'image': 'bench-3.jpg', 'excerpt': 'Come and try the tools. Mince pies, no hard sell.',
     'content': P_('The workshop is open from 11 to 4 on Saturday 13 December. You can file a bit of silver, look at stones under the microscope and see waxes for rings that are on the bench now.', 'The stairs are steep and there is no lift, sorry. Brass will be there.')},
]
content = {
    'site': {'title': 'Edie Achterberg', 'tagline': 'Goldsmith, Magdalen Street, Norwich'},
    'categories': [{'slug': 'commissions', 'name': 'Commissions'}, {'slug': 'stones', 'name': 'Stones'}, {'slug': 'workshop', 'name': 'Workshop'}],
    'front_page': 'home', 'posts_page': 'journal',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'journal', 'title': 'Journal', 'content': ''},
        {'slug': 'bespoke', 'title': 'Bespoke', 'pattern': 'karat/page-bespoke'},
        {'slug': 'ring-sizes', 'title': 'Ring sizes', 'pattern': 'karat/page-ring-sizes'},
        {'slug': 'care', 'title': 'Care and materials', 'pattern': 'karat/page-care'},
        {'slug': 'repairs', 'title': 'Repairs and valuations', 'pattern': 'karat/page-repairs'},
        {'slug': 'about', 'title': 'About', 'pattern': 'karat/page-about'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'karat/page-contact'},
    ],
    'posts': posts,
    'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'Bespoke', 'url': '/bespoke/'}, {'label': 'Ring sizes', 'url': '/ring-sizes/'},
            {'label': 'Journal', 'url': '/journal/'}, {'label': 'Repairs', 'url': '/repairs/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}],
    'currency': 'GBP',
    'products': [
        {'name': 'Signet ring, engraved oval', 'price': '1480', 'image': 'hero.jpg', 'category': 'Rings', 'sku': 'EA-R01', 'stock': 2, 'short': '18ct yellow gold, hand-engraved face. Made to order in your size in 3 weeks.'},
        {'name': 'Carnelian bar ring', 'price': '1250', 'image': 'ring-2.jpg', 'category': 'Rings', 'sku': 'EA-R02', 'stock': 3, 'short': '18ct yellow gold, 2 mm band, carnelian set east to west.'},
        {'name': 'Knot bangle and pearl stacker', 'price': '310', 'image': 'ring-4.jpg', 'category': 'Rings', 'sku': 'EA-R03', 'stock': 6, 'short': 'Recycled silver. The bangle fits wrists up to 17 cm.'},
        {'name': 'Plain hoops, pair', 'price': '395', 'image': 'earring-1.jpg', 'category': 'Earrings', 'sku': 'EA-E01', 'stock': 8, 'short': '9ct yellow gold, 18 mm across, hinged at the back.'},
        {'name': 'Garnet drop pendant', 'price': '720', 'image': 'pendant-1.jpg', 'category': 'Pendants', 'sku': 'EA-P01', 'stock': 1, 'short': '18ct yellow gold bezel, on a 45 cm trace chain.'},
        {'name': 'Carnelian seal ring', 'price': '640', 'image': 'ring-1.jpg', 'category': 'One of one', 'sku': 'EA-O01', 'stock': 1, 'short': 'An old carved carnelian in 18ct, on an oxidised silver shank. Size M.'},
        {'name': 'Garnet rosette ring', 'price': '880', 'image': 'ring-3.jpg', 'category': 'One of one', 'sku': 'EA-O02', 'stock': 1, 'short': 'Silver-gilt with eight garnet cells. Size P, can be sized by one.'},
        {'name': 'Emerald and variscite chain', 'price': '1900', 'image': 'necklace-1.jpg', 'category': 'One of one', 'sku': 'EA-O03', 'stock': 0, 'short': 'Sold. Ask about a similar chain.'},
    ],
}
os.makedirs('demos/karat', exist_ok=True)
json.dump(content, open('demos/karat/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
