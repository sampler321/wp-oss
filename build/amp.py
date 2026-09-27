# Design note (amp, idea 038, band / solo musician; owner's brief: "make it duotone")
# Direction: a two-colour gig flyer. The whole site uses exactly two inks: the page is the highlight colour,
#   type and rules are the shadow colour, and every photo runs through a matching duotone preset, so pictures
#   print into the page like a photocopied poster. Style variations swap the ink pair and the duotone together.
# Fonts: Karrik (Velvetyne, OFL) for the band name, titles and dates; Figtree for text, with tabular figures in the dates.
# Palette: shadow #141414 and highlight #FF4F1F (Signal). Variations: Night (navy/yellow), Folk (brown/cream), Punk (black/yellow).
# Layout idea: the live page is the centre of the site, a full-width dates table with the date in a fixed first column,
#   grouped by tour, with sold out and low tickets flags and one ticket link per row.
import sys, json, os, shutil
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('amp')

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
C = lambda slug: 'var:preset|color|%s' % slug
pad = lambda t, b=None: {'spacing': {'padding': {'top': P(t), 'bottom': P(b or t)}}}

def two_ink(shadow, highlight, surface, names=('Ink', 'Paper')):
    """A palette of exactly two inks, with surface a tint of the paper and line/accent the ink."""
    return [{'slug': 'base', 'color': highlight, 'name': names[1]}, {'slug': 'contrast', 'color': shadow, 'name': names[0]},
            {'slug': 'accent', 'color': shadow, 'name': names[0] + ' (accent)'}, {'slug': 'surface', 'color': surface, 'name': names[1] + ' tint'},
            {'slug': 'line', 'color': shadow, 'name': 'Rule'}]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
DUO = lambda shadow, highlight, name: [{'slug': 'band', 'colors': [shadow, highlight], 'name': name},
                                       {'slug': 'band-reverse', 'colors': [highlight, shadow], 'name': name + ', reversed'}]
DUOTONE = 'var(--wp--preset--duotone--band)'

CSS = (
    '.wp-site-blocks>footer,.wp-site-blocks>.wp-block-template-part:last-child{margin-block-start:0}'
    ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}html{font-synthesis:none}'
    'table,.wp-block-post-date{font-variant-numeric:tabular-nums lining-nums}'
    '::selection{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'
    # live dates table
    '.wp-block-table.is-style-dates table{border-collapse:collapse;width:100%}'
    '.wp-block-table.is-style-dates td,.wp-block-table.is-style-dates th{border:0;border-bottom:2px solid var(--wp--preset--color--line);padding:.8rem 1rem .8rem 0;text-align:left;vertical-align:baseline}'
    '.wp-block-table.is-style-dates thead th{font-size:var(--wp--preset--font-size--small);font-weight:600;border-bottom-width:2px}'
    '.wp-block-table.is-style-dates td:first-child{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);white-space:nowrap;width:9.5rem}'
    '.wp-block-table.is-style-dates td:nth-child(2){font-weight:700;font-size:var(--wp--preset--font-size--large)}'
    '.wp-block-table.is-style-dates td:nth-child(4){font-size:var(--wp--preset--font-size--small)}'
    '.wp-block-table.is-style-dates td:last-child{text-align:right;white-space:nowrap}'
    '.wp-block-table.is-style-dates td:last-child a{display:inline-block;border:2px solid var(--wp--preset--color--contrast);padding:.3em .8em;font-weight:700;text-decoration:none}'
    '.wp-block-table.is-style-dates td:last-child a:hover{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'
    '.wp-block-table.is-style-dates td:last-child strong{display:inline-block;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);padding:.3em .8em}'
    '.wp-block-table.is-style-dates td:last-child em{font-style:normal;font-weight:700;margin-right:.6em}'
    '.wp-block-table td,.wp-block-table th{border-color:var(--wp--preset--color--line)}'
    # date rows (home page, no table)
    '.is-style-date-row{border-bottom:2px solid var(--wp--preset--color--line);padding:.7rem 0;align-items:baseline!important}'
    '.is-style-date-row>p{margin:0}.is-style-date-row>p:first-child{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);min-width:9rem}'
    '.is-style-date-row>p:nth-child(2){font-weight:700;font-size:var(--wp--preset--font-size--large);flex:0 1 17rem}.is-style-date-row>p:nth-child(3){flex:0 1 9rem}.is-style-date-row>p:nth-child(4){flex:1 1 12rem}'
    '.is-style-ink-row{border-bottom:2px solid var(--wp--preset--color--line);padding:.6rem 0;gap:.2rem 1.5rem!important}.is-style-ink-row>p{margin:0;flex:1 1 12rem}.is-style-ink-row>p:first-child{flex:0 1 13rem;font-weight:700}'
    '.is-style-date-row>p:last-child{margin-left:auto}.is-style-date-row>p:last-child a{display:inline-block;border:2px solid var(--wp--preset--color--contrast);padding:.3em .8em;font-weight:700;text-decoration:none}'
    '.is-style-date-row>p:last-child strong{display:inline-block;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);padding:.3em .8em}.is-style-date-row em{font-style:normal;font-weight:700;margin-right:.6em}'
    '.is-style-poster-towns{font-family:var(--wp--preset--font-family--display);line-height:.95}'
    # WooCommerce product images: fake the duotone with greyscale multiplied onto the paper colour
    '.wc-block-components-product-image img,.woocommerce-product-gallery img,.wc-block-grid__product-image img{filter:grayscale(1) contrast(1.15);mix-blend-mode:multiply}'
    '.wc-block-components-product-price,.woocommerce-Price-amount{font-weight:700}'
    '.wp-block-quote cite{display:block;margin-top:.6rem;font-size:var(--wp--preset--font-size--small);font-style:normal;font-weight:600}'
    '.wp-block-details summary{font-weight:700;cursor:pointer}'
    '@media (max-width:700px){.wp-block-table.is-style-dates thead{display:none}.wp-block-table.is-style-dates tr{display:grid;grid-template-columns:1fr auto;border-bottom:2px solid var(--wp--preset--color--line);padding:.6rem 0}'
    '.wp-block-table.is-style-dates td{border:0;padding:.1rem 0}.wp-block-table.is-style-dates td:first-child{grid-column:1/-1;width:auto}'
    '.wp-block-table.is-style-dates td:nth-child(3),.wp-block-table.is-style-dates td:nth-child(4){grid-column:1}.wp-block-table.is-style-dates td:last-child{grid-row:2;grid-column:2;align-self:center}}'
)

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '740px', 'wideSize': '1360px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': two_ink('#141414', '#FF4F1F', '#FF6B40', ('Ink', 'Signal orange')),
                  'duotone': DUO('#141414', '#FF4F1F', 'Ink on signal orange')},
        'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False, 'fontFamilies': fonts, 'fontSizes': [
            {'slug': 'x-small', 'size': '0.875rem', 'name': 'Small print', 'fluid': False},
            {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
            {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
            {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
            {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '1.8rem', 'max': '2.5rem'}},
            {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.5rem', 'max': '4rem'}},
            {'slug': 'display', 'size': '7.5rem', 'name': 'Display', 'fluid': {'min': '3.4rem', 'max': '7.5rem'}}]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.75rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5.5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': C('base'), 'text': C('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '450'},
        'spacing': {'padding': {'left': P(40), 'right': P(40)}, 'blockGap': P(30)},
        'elements': {
            'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'typography': {'textDecoration': 'none'}},
                     ':focus': {'outline': {'color': C('contrast'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '0.95', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.1'}},
            'h5': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '700', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {'color': {'background': C('contrast'), 'text': C('base')}, 'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': C('contrast')},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.3em', 'right': '1.3em'}},
                       ':hover': {'color': {'background': C('base'), 'text': C('contrast')}},
                       ':focus': {'outline': {'color': C('contrast'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': C('contrast')}},
        },
        'blocks': {
            'core/image': {'filter': {'duotone': DUOTONE}, 'border': {'radius': '0'}},
            'core/cover': {'filter': {'duotone': DUOTONE}},
            'core/post-featured-image': {'filter': {'duotone': DUOTONE}, 'border': {'radius': '0'}},
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '0.9'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '700'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'}},
            'core/separator': {'color': {'text': C('line')}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.05'},
                           'border': {'left': {'color': C('line'), 'width': '4px', 'style': 'solid'}}, 'spacing': {'padding': {'left': P(30)}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|medium'}},
            'core/details': {'border': {'bottom': {'color': C('line'), 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(20), 'bottom': P(20)}}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
        },
        'css': CSS,
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Amp
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A two-colour duotone site for independent bands and solo musicians, built around a live dates page, releases and a small merch shop.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: amp
Tags: e-commerce, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column
*/''')

def variation(slug, title, shadow, highlight, surface, names):
    jdump('styles/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
        'settings': {'color': {'palette': two_ink(shadow, highlight, surface, names), 'duotone': DUO(shadow, highlight, '%s on %s' % names)}}})
variation('night', 'Night (navy and yellow)', '#0E1C36', '#F4DD4B', '#F6E46E', ('Navy', 'Sodium yellow'))
variation('folk', 'Folk (brown and cream)', '#3B2412', '#F1E6CF', '#E8DABD', ('Peat', 'Cream'))
variation('punk', 'Punk (black and yellow)', '#111111', '#FFE600', '#FFEC40', ('Black', 'Hi-vis yellow'))

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})
section('reverse', 'Reversed (ink ground)', ['core/group', 'core/columns'], {
    'color': {'background': C('contrast'), 'text': C('base')},
    'elements': {'link': {'color': {'text': C('base')}}, 'heading': {'color': {'text': C('base')}},
                 'button': {'color': {'background': C('base'), 'text': C('contrast')}, 'border': {'color': C('base')}, ':hover': {'color': {'background': C('contrast'), 'text': C('base')}}}},
    'blocks': {'core/image': {'filter': {'duotone': 'var(--wp--preset--duotone--band-reverse)'}}, 'core/table': {'css': '& td{border-color:var(--wp--preset--color--base)!important}'}},
    'spacing': {'padding': {'top': P(60), 'bottom': P(60)}}})
section('rule-top', 'Thick rule above', ['core/group', 'core/columns'], {'border': {'top': {'color': C('line'), 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(30)}, 'margin': {'top': P(60)}}})
section('rule-bottom', 'Thick rule below', ['core/group'], {'border': {'bottom': {'color': C('line'), 'width': '2px', 'style': 'solid'}}})
section('ink-row', 'Ruled row', ['core/group'], {'typography': {'fontSize': 'var:preset|font-size|medium'}})
section('date-row', 'Date row', ['core/group'], {'typography': {'fontSize': 'var:preset|font-size|medium'}})
section('poster-towns', 'Poster towns', ['core/paragraph'], {'typography': {'fontSize': 'var:preset|font-size|xx-large'}})
section('dates', 'Live dates', ['core/table'], {'typography': {'fontSize': 'var:preset|font-size|medium'}})
section('boxed', 'Boxed', ['core/group', 'core/column'], {'border': {'color': C('line'), 'width': '2px', 'style': 'solid'}, 'spacing': {'padding': {'top': P(40), 'bottom': P(40), 'left': P(40), 'right': P(40)}}})
section('stamp', 'Stamp (sold out, low tickets)', ['core/paragraph'], {
    'color': {'background': C('contrast'), 'text': C('base')}, 'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
    'spacing': {'padding': {'top': P(10), 'bottom': P(10), 'left': P(20), 'right': P(20)}}, 'css': '&{display:inline-block}'})

# ---------------------------------------------------------------- patterns
IMG = {
    'venue-1': ('venue-1.jpg', 'A three-piece band playing on a small stage with fairy lights and a painted sign behind them'),
    'live-1': ('live-1.jpg', 'Two guitarists on a cramped stage, one kneeling over his guitar next to a pedal board'),
    'live-2': ('live-2.jpg', 'A drummer behind cymbals and a floor tom, lit from the side'),
    'live-3': ('live-3.jpg', 'Someone crowd-surfing over raised hands in front of a lit stage'),
    'live-4': ('live-4.jpg', 'A singer in sunglasses and a leather jacket at a microphone stand'),
    'gear-1': ('gear-1.jpg', 'Close-up of a small valve guitar amplifier with its row of knobs'),
    'gear-2': ('gear-2.jpg', 'Two cassette tapes lying side by side on a black table'),
    'sleeve-1': ('sleeve-1.jpg', 'Crates of second-hand records in a record shop'),
    'sleeve-3': ('sleeve-3.jpg', 'A tall square lighthouse against a blue sky with white clouds'),
    'sleeve-4': ('sleeve-4.jpg', 'Etching of a line of people marching down a road between tall bare trees at night'),
    'town-1': ('town-1.jpg', 'A long wooden seaside pier with lamp posts, under a big sky'),
    'van-1': ('van-1.jpg', 'A row of white vans parked under plane trees on a city street'),
}
def img(key, caption='', **kw):
    f, alt = IMG[key]
    return image(f, alt, caption, **kw)

REL = 'Slack Water'
pattern('current-release', 'Current release: sleeve, title, buy and listen links', 'featured', columns(
    ('50%', img('sleeve-3', aspectRatio='1', scale='cover')),
    ('50%', J(para('New album, out 14 November', style={'typography': {'fontWeight': '700'}}),
              heading(REL, 1),
              para('Ten songs recorded in a week at a chapel in Heysham, on Saltpan Records. LP, CD and cassette. The LP comes on sea-green vinyl because Dev lost an argument.'),
              buttons(('Buy the LP, £24', '/shop/'), ('Listen on Bandcamp', 'https://bandcamp.com/'), ('Tour dates', '/live/')))),
    align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': P(50)}, 'padding': {'top': P(50), 'bottom': P(60)}}}))

tour = [
    ('Thu 12 Nov', 'Brudenell Social Club', 'Leeds', 'with Gilly Hart', '<a href="https://example.com/tickets/leeds">Tickets</a>'),
    ('Fri 13 Nov', 'Gorilla', 'Manchester', 'with Gilly Hart', '<em>Low tickets</em><a href="https://example.com/tickets/manchester">Tickets</a>'),
    ('Sat 14 Nov', 'The Platform', 'Morecambe', 'Album launch, with The Ribble Valley Brass Band', '<strong>Sold out</strong>'),
    ('Tue 17 Nov', 'Stereo', 'Glasgow', 'with Mhairi Fyfe', '<a href="https://example.com/tickets/glasgow">Tickets</a>'),
    ('Wed 18 Nov', 'Sneaky Pete\'s', 'Edinburgh', 'with Mhairi Fyfe', '<a href="https://example.com/tickets/edinburgh">Tickets</a>'),
    ('Fri 20 Nov', 'Whelan\'s', 'Dublin', 'with Aoife Kerr', '<a href="https://example.com/tickets/dublin">Tickets</a>'),
    ('Sat 21 Nov', 'Ulster Sports Club', 'Belfast', 'with Aoife Kerr', '<em>Low tickets</em><a href="https://example.com/tickets/belfast">Tickets</a>'),
    ('Tue 24 Nov', 'The Louisiana', 'Bristol', 'with Gilly Hart', '<a href="https://example.com/tickets/bristol">Tickets</a>'),
    ('Wed 25 Nov', 'Oslo Hackney', 'London', 'with Gilly Hart', '<a href="https://example.com/tickets/london">Tickets</a>'),
]
instores = [
    ('Sat 14 Nov, 1pm', 'Vinyl Revival', 'Morecambe', 'Acoustic, four songs, signing after', 'Free entry'),
    ('Sun 15 Nov, 3pm', 'Crash Records', 'Leeds', 'Acoustic, with a wristband when you buy the LP', '<a href="https://example.com/instore/leeds">Wristbands</a>'),
    ('Sat 28 Nov, 2pm', 'Rough Trade East', 'London', 'Acoustic', '<a href="https://example.com/instore/london">Wristbands</a>'),
]
def dates_table(rows):
    return table([list(r) for r in rows], head=['Date', 'Venue', 'Town', 'Support', ''], className='is-style-dates', align='wide')

pattern('live-dates', 'Live dates: every show with support and one ticket link', 'featured', group(J(
    heading('Slack Water tour, UK and Ireland', 2, align='wide'),
    dates_table(tour),
    heading('In-stores, acoustic', 3, align='wide'),
    dates_table(instores),
    para('Doors 7pm unless it says otherwise. All shows are 14+ with an adult. Past dates move to the <a href="/live/#past">list below</a> at the end of each month.', fontSize='small', align='wide')),
    align='wide', layout={'type': 'default'}), description='The signature: dates grouped by tour and by type, with support acts, low tickets and sold out flags, and one ticket link per row.')

def ink_rows(data):
    return group(J(*[row(J(*[para(c) for c in r]), className='is-style-ink-row') for r in data]), layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}})

def date_rows(rows):
    return J(*[row(J(para(d), para(v), para(t), para(n, fontSize='small'), para(tk)), className='is-style-date-row', align='wide', style={'spacing': {'blockGap': P(30)}}) for d, v, t, n, tk in rows])

pattern('live-dates-short', 'Next five dates (front page, no table)', 'featured', group(J(
    row(J(heading('Live', 2), para('<a href="/live/">All dates and in-stores</a>', style={'typography': {'fontWeight': '700'}})), justify='space-between', align='wide'),
    group(date_rows(tour[:5]), align='wide', layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}})), align='wide', layout={'type': 'default'}))

pattern('past-dates', 'Past dates (archive)', 'text', group(J(
    heading('Played', 3),
    ink_rows([['Aug 2026', 'Beautiful Days festival', 'Devon'], ['Jul 2026', 'Deershed', 'North Yorkshire'], ['May 2026', 'The Castle Hotel', 'Manchester'],
              ['Apr 2026', 'Hug and Pint', 'Glasgow'], ['Mar 2026', 'The Victoria', 'London']])),
    align='wide', layout={'type': 'default'}, anchor='past'))

pattern('tracklist', 'Tracklist, formats and credits', 'text', columns(
    ('50%', J(heading('Tracklist', 4), lst(['Slack Water', 'The Ferry Doesn\'t Wait', 'Half Past Low Tide', 'Winter Gardens', 'Bare Arms', 'Heysham Heads',
                                             'Ribble', 'Promenade Lights', 'Cockle Pickers', 'Last Boat Out'], ordered=True))),
    ('50%', J(heading('Formats', 4), table([['LP', 'Sea-green vinyl, gatefold, lyric sheet', '£24'], ['CD', 'Card wallet', '£12'], ['Cassette', 'Edition of 150', '£8'], ['Download', 'Bandcamp, pay what you like', 'from £7']]),
              heading('Credits', 4), para('Recorded at St Peter\'s Church, Heysham, by Jonny Rees. Mixed by Ellen Mawdsley. Cover photograph by Sam Hutchins. Catalogue number SALT014.', fontSize='small'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(50)}}}))

pattern('release-grid', 'Releases grid (square sleeves)', 'posts,query', group(J(
    row(J(heading('Records', 2), para('<a href="/records/">Every release</a>', style={'typography': {'fontWeight': '700'}})), justify='space-between', align='wide'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=12, moreText='')),
          per_page=4, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}, align='wide')),
    align='wide', layout={'type': 'default'}))
pattern('release-archive', 'Releases (inherits the page query)', 'posts,query', inherit_query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover'), dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', excerptLength=20, moreText='')),
    layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'}, align='wide'), inserter=False)

pattern('photo-strip', 'Photo strip (duotone live photos)', 'gallery', gallery([
    ('live-3.jpg', IMG['live-3'][1], ''), ('live-2.jpg', IMG['live-2'][1], ''), ('live-4.jpg', IMG['live-4'][1], ''), ('gear-1.jpg', IMG['gear-1'][1], '')], columns=4, align='full'))

merch = [('sleeve-3', 'Slack Water LP', '£24'), ('gear-2', 'Slack Water cassette', '£8'), ('sleeve-4', 'Tour poster, A2, screenprint', '£15'), ('town-1', 'Pier tote bag', '£12')]
pattern('merch-rail', 'Merch rail', 'shop', group(J(
    row(J(heading('Merch', 2), para('<a href="/shop/">The whole shop</a>', style={'typography': {'fontWeight': '700'}})), justify='space-between', align='wide'),
    group(J(*[stack(J(img(k, href='/shop/', aspectRatio='1', scale='cover'), para('<a href="/shop/">%s</a>' % n, style={'typography': {'fontWeight': '700'}}), para(p_, fontSize='small')), style={'spacing': {'blockGap': P(10)}}) for k, n, p_ in merch]),
          layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '11rem'}, align='wide'),
    para('Orders placed during the tour ship on 30 November, because we pack them ourselves.', fontSize='small', align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('mailing-list', 'Mailing list', 'call-to-action', group(J(
    columns(('60%', J(heading('Tell me when you play near me', 2), para('One email per tour and one per record. Send your town to <a href="mailto:list@example.com?subject=Mailing%20list">list@example.com</a> and we will only write when we are coming.'))),
            ('40%', buttons(('Join the list by email', 'mailto:list@example.com?subject=Mailing%20list'))), align='wide', verticalAlignment='center')),
    tag='section', align='full', className='is-style-reverse', layout={'type': 'constrained'}, anchor='list'))

pattern('booking-contacts', 'Booking and management by territory', 'contact', group(J(
    heading('Booking and management', 3),
    ink_rows([['Booking, UK, Ireland and Europe', 'Nadia Farouk, Lowlight Agency', '<a href="mailto:nadia@example.com">nadia@example.com</a>'],
              ['Booking, North America', 'Sam Okafor, Far Shore Touring', '<a href="mailto:sam@example.com">sam@example.com</a>'],
              ['Management', 'Kirsty Doyle', '<a href="mailto:kirsty@example.com">kirsty@example.com</a>'],
              ['Label', 'Saltpan Records', '<a href="mailto:hello@example.com">hello@example.com</a>'],
              ['Press', 'Owen Pryce, Flat Calm PR', '<a href="mailto:owen@example.com">owen@example.com</a>']])),
    align='wide', layout={'type': 'default'}), description='Contacts split by territory, the way promoters look for them.')

pattern('band-bio', 'Band bio (short)', 'about', columns(
    ('58%', J(para('Heysham Ferry are three people from Morecambe who play loud songs about the sea not quite reaching the promenade. Cat Lomax sings and plays guitar, Dev Mistry plays bass, Ollie Brannan plays drums and drives the van.', fontSize='large'),
              para('They met at the Platform in 2018, put out Promenade in 2021 and have played 214 shows since, most of them in rooms that hold under 300 people. Slack Water, their second album, is out on 14 November on Saltpan Records.'),
              para('They don\'t play festivals that don\'t pay the support acts.'))),
    ('42%', img('venue-1', 'Live, 2026. Photograph by Sam Hutchins')),
    align='wide', style={'spacing': {'blockGap': {'left': P(50)}}}))

pattern('press-photos', 'Press photos with photographer credit', 'gallery', group(J(
    heading('Press photos', 3),
    para('Free to use with the photographer\'s credit. Ask Owen for full-size files.', fontSize='small'),
    gallery([('venue-1.jpg', IMG['venue-1'][1], 'Sam Hutchins'), ('live-1.jpg', IMG['live-1'][1], 'Priya Dhillon'), ('van-1.jpg', IMG['van-1'][1], 'Ollie Brannan')], columns=3)),
    layout={'type': 'default'}))

pattern('press-quotes', 'Press quotes', 'testimonials', columns(
    (None, quote('The loudest band ever to write a song about cockle picking.', 'The Skinny, 4 out of 5')),
    (None, quote('Promenade Lights is the best British guitar single of the year.', 'Loud and Quiet')), align='wide'))

pattern('epk-rider', 'Technical needs (short rider)', 'text', group(J(
    heading('What we need', 4),
    lst(['Three vocal mics, one for the drums', 'DI for bass, we bring our own amps', 'Two wedges, or one if the stage is small', 'Room for a merch table near the door', 'A vegetarian meal for three, or £30 buyout']),
    para('Stage plot and input list on request from Kirsty.', fontSize='small')), className='is-style-boxed', layout={'type': 'default'}))

pattern('workshops', 'Workshops and extra events', 'text', J(
    para('Between tours we run songwriting afternoons for 14 to 18 year olds. Three hours, one song, a recording of it to take home.', fontSize='large'),
    table([['Sat 10 Jan', 'Morecambe Library', 'Free, 12 places, book at the desk'], ['Sat 7 Feb', 'The Platform, Morecambe', '£5, 20 places'], ['Sat 7 Mar', 'Brewery Arts, Kendal', '£5, 16 places']], className='is-style-dates'),
    para('Schools and youth clubs can book a session for their own group. Email Kirsty with a date and how many people.', fontSize='small')))

pattern('notice-tour', 'Notice: tour on sale', 'banner', group(
    para('Tour tickets on sale now. Morecambe is sold out, Manchester and Belfast are nearly there.', style={'typography': {'fontWeight': '700'}}, fontSize='small'),
    tag='aside', align='full', className='is-style-reverse', style=pad(20), layout={'type': 'constrained'}), description='A one-line bar for on-sale news. Remove it when the tour ends.')

pattern('town-feature', 'Where we are from (full width picture)', 'featured', group(J(
    img('town-1', aspectRatio='21/9', scale='cover', align='full'),
    group(J(heading('Morecambe, the end of the line', 2),
            para('The band practise in a room under the Winter Gardens, next to the stores for the pantomime.', fontSize='large')), layout={'type': 'constrained'}, align='wide')),
    tag='section', align='full', layout={'type': 'constrained'}, style={'spacing': {'blockGap': P(40)}}))


pattern('setlist', 'Last night\'s setlist', 'text', group(J(
    heading('Last night\'s setlist', 4), para('Gorilla, Manchester, Friday 13 November', fontSize='small'),
    lst(['The Ferry Doesn\'t Wait', 'Slack Water', 'Heysham Heads', 'Half Past Low Tide', 'Bare Arms', 'Winter Gardens', 'Promenade Lights', 'Cockle Pickers', 'Last Boat Out'], ordered=True),
    para('Encore: Hail Smiling Morn, played badly on purpose.', fontSize='small')), className='is-style-boxed', layout={'type': 'default'}))

pattern('lyric-sheet', 'Lyric sheet (verse)', 'text', J(
    heading('Slack Water', 4),
    verse('The tide goes out as far as Grange\nand leaves the boats on their sides\nwe walked out after it for miles\nand nobody asked us why'),
    para('Words by Cat Lomax. Printed in full on the LP inner sleeve.', fontSize='small')))

pattern('access-guestlist', 'Access, age limits and guest list', 'text', columns(
    (None, J(heading('Access', 5), para('Every venue on this tour has step-free access except Sneaky Pete\'s in Edinburgh. If you need a companion ticket, email the venue first, then tell us and we will chase it.'))),
    (None, J(heading('Ages', 5), para('14+ with an adult unless the venue says 18+. The Morecambe launch is all ages, under-14s with a parent.'))),
    (None, J(heading('Guest list', 5), para('It is small and it is for family. We can\'t add you, sorry. Returns for sold-out shows go on Twickets at face value.'))),
    align='wide', className='is-style-rule-top'))

pattern('tour-diary', 'Tour diary entry', 'posts', columns(
    ('42%', img('van-1', 'Parked on the wrong side of the road in Dublin, 2025')),
    ('58%', J(heading('Day six: the van gets a name', 3),
              para('Ollie has named the van Brenda. It has done 212,000 miles and it pulls to the left when it is sad. We drove from Glasgow to Holyhead in nine hours with one stop for chips and one to fix the wing mirror with gaffer tape.'),
              para('Dublin was the best crowd of the tour so far. Someone asked for a song from the first EP and we could not remember the words, so they sang it.'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(50)}}}))

pattern('release-page', 'Release page: tracklist, lyrics and setlist', 'posts', J(pattern_ref('tracklist'), columns((None, pattern_ref('lyric-sheet')), (None, pattern_ref('setlist')), align='wide')), block_types='core/post-content')

pattern('hero-poster', 'Hero: gig poster (band name and towns)', 'featured', group(J(
    heading('Heysham Ferry', 1, fontSize='display'),
    para('Leeds, Manchester, Morecambe, Glasgow, Edinburgh, Dublin, Belfast, Bristol, London', className='is-style-poster-towns'),
    row(J(para('12 to 25 November 2026, with Gilly Hart, Mhairi Fyfe and Aoife Kerr', style={'typography': {'fontWeight': '700'}}), buttons(('Tickets and dates', '/live/'))), justify='space-between')),
    tag='section', align='full', className='is-style-rule-bottom', layout={'type': 'constrained', 'contentSize': '1360px'}, style=pad(60)),
    description='An alternative front-page opener set like a tour poster.')

pattern('band-members', 'Who is in the band', 'about', columns(
    (None, J(img('live-4', aspectRatio='4/5', scale='cover'), heading('Cat Lomax', 4), para('Voice, guitar, most of the words. Works mornings at the Winter Gardens box office.', fontSize='small'))),
    (None, J(img('live-1', aspectRatio='4/5', scale='cover'), heading('Dev Mistry', 4), para('Bass, the other guitar on the record, the tour spreadsheet.', fontSize='small'))),
    (None, J(img('live-2', aspectRatio='4/5', scale='cover'), heading('Ollie Brannan', 4), para('Drums, the van, the merch table. Once played a whole set with a broken wrist.', fontSize='small'))),
    align='wide'))

pattern('listen-links', 'Where to listen and buy', 'call-to-action', group(J(
    heading('Listen and buy', 4),
    para('<a href="https://bandcamp.com/">Bandcamp</a> (best for us), <a href="https://www.spotify.com/">Spotify</a>, <a href="https://music.apple.com/">Apple Music</a>, <a href="/shop/">our shop</a> for the LP, or any record shop that orders from Cargo.'),
    para('Buying on Bandcamp on the first Friday of the month means they take no cut.', fontSize='small')), className='is-style-boxed', layout={'type': 'default'}))

pattern('album-story', 'How the record was made', 'text', columns(
    ('42%', img('gear-1', 'The amp that ran the whole album, borrowed from the chapel caretaker')),
    ('58%', J(heading('A week in a chapel', 3),
              para('We recorded Slack Water in seven days at St Peter\'s, Heysham, with the pews pushed back and the amps pointing at the organ. Jonny Rees brought two microphones and a tape machine. Most songs are the third take.'),
              para('The church charged us £40 a day and asked us to stop at 6pm for choir practice. You can hear the tide on Last Boat Out if you turn it up.'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(50)}}}))

pattern('photo-pair', 'Two photos side by side', 'gallery', gallery([('venue-1.jpg', IMG['venue-1'][1], ''), ('live-3.jpg', IMG['live-3'][1], '')], columns=2, align='wide'))

pattern('big-quote', 'Big press quote', 'testimonials', group(
    quote('Three people making the noise of a pier in a storm.', 'The Quietus, on Promenade'), align='wide', layout={'type': 'constrained'}, style=pad(50)))

pattern('ticket-faq', 'Ticket questions', 'text', group(J(
    heading('Tickets, briefly', 3),
    details('The show is sold out. Is there a waiting list?', para('Returns go on Twickets at face value. We never release extra tickets on the day.')),
    details('Can I bring my kid?', para('14+ with an adult at most venues. The Morecambe launch is all ages.')),
    details('What time are we on?', para('Usually 9pm, support at 8. Venues post stage times on the day.')),
    details('Do you sell merch at shows?', para('Yes, card only. Cat does the table after the set.'))), layout={'type': 'constrained'}))

pattern('radio-sessions', 'Radio sessions', 'text', group(J(
    heading('Sessions', 4),
    lst(['BBC Radio Lancashire, Introducing session, March 2026', 'Soho Radio, live in the window, October 2025', 'Radio Buena Vida, Salford, two songs and a quiz, June 2025'])),
    layout={'type': 'default'}))

pattern('watch-videos', 'Videos (stills linking out)', 'gallery', group(J(
    heading('Watch', 3),
    columns((None, J(img('live-3', href='https://www.youtube.com/', aspectRatio='16/9', scale='cover'), para('<a href="https://www.youtube.com/">Promenade Lights, live at Gorilla</a>', style={'typography': {'fontWeight': '700'}}))),
            (None, J(img('town-1', href='https://www.youtube.com/', aspectRatio='16/9', scale='cover'), para('<a href="https://www.youtube.com/">Slack Water, filmed on the pier</a>', style={'typography': {'fontWeight': '700'}}))), align='wide')),
    align='wide', layout={'type': 'default'}), description='Stills that link to the videos, so nothing autoplays.')

pattern('merch-shipping', 'Merch shipping note', 'shop', group(
    para('UK postage £3.50 for one record, £5 for anything bigger. Europe from £9. Tote bags and posters are printed in Lancaster and posted in a tube or a board-backed envelope. Returns within 14 days if it arrives broken, just send a photo.', fontSize='small'),
    className='is-style-rule-top', layout={'type': 'default'}))

pattern('next-show', 'Next show (single big line)', 'featured', group(J(
    para('Next show', style={'typography': {'fontWeight': '700'}}),
    heading('Thu 12 Nov, Brudenell Social Club, Leeds', 2),
    buttons(('Tickets for Leeds', 'https://example.com/tickets/leeds'), ('All dates', '/live/'))),
    tag='section', align='full', className='is-style-reverse', layout={'type': 'constrained'}))

pattern('support-note', 'About the support acts', 'text', group(J(
    heading('Support', 4),
    para('We pick every support act ourselves and pay them the same flat fee, £150 a night, plus a share of merch space. This tour: Gilly Hart in England, Mhairi Fyfe in Scotland, Aoife Kerr in Ireland.')),
    layout={'type': 'default'}))

pattern('stockists', 'Record shops that stock us', 'shop', group(J(
    heading('In shops', 4),
    para('Vinyl Revival, Morecambe. Crash Records, Leeds. Piccadilly Records, Manchester. Monorail, Glasgow. Rough Trade, London and Bristol. If your local shop wants copies, they can order from Cargo, or email the label.')),
    layout={'type': 'default'}))

pattern('mailing-list-inline', 'Mailing list (one line)', 'call-to-action', group(
    para('Tour dates by email, about four a year: send your town to <a href="mailto:list@example.com?subject=Mailing%20list">list@example.com</a>.', style={'typography': {'fontWeight': '700'}}),
    className='is-style-boxed', layout={'type': 'default'}))

# pages
pattern('page-live', 'Page: live', 'featured', J(pattern_ref('live-dates'), pattern_ref('support-note'), pattern_ref('access-guestlist'), pattern_ref('ticket-faq'), pattern_ref('past-dates'), pattern_ref('booking-contacts')), block_types='core/post-content')
pattern('page-epk', 'Page: EPK', 'about', J(pattern_ref('band-bio'), pattern_ref('band-members'), pattern_ref('radio-sessions'), pattern_ref('press-quotes'), pattern_ref('press-photos'),
    para('Press kit, one page PDF with the album details and links: ask Owen at <a href="mailto:owen@example.com">owen@example.com</a>.'), pattern_ref('epk-rider'), pattern_ref('booking-contacts')), block_types='core/post-content')
pattern('page-workshops', 'Page: workshops', 'text', J(pattern_ref('workshops')), block_types='core/post-content')
pattern('page-contact', 'Page: contact', 'contact', J(pattern_ref('mailing-list-inline'), para('Email the right person below. For anything else, write to the band at <a href="mailto:band@example.com">band@example.com</a>. Cat answers on Sundays.', fontSize='large'),
    pattern_ref('booking-contacts')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')), justify='space-between', align='wide'),
    tag='header', align='full', className='is-style-rule-bottom', style=pad(30)))
write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0, fontSize='xx-large'), para('Three people from Morecambe. New album Slack Water out 14 November on Saltpan Records.', fontSize='small'))),
        (None, J(heading('Booking', 6), para('UK and Europe: <a href="mailto:nadia@example.com">nadia@example.com</a><br>North America: <a href="mailto:sam@example.com">sam@example.com</a>', fontSize='small'))),
        (None, J(heading('Elsewhere', 6), para('<a href="https://bandcamp.com/">Bandcamp</a><br><a href="https://www.instagram.com/">Instagram</a><br><a href="/contact/#list">Mailing list</a>', fontSize='small'))),
        align='wide'),
    para('Demo photographs are public domain pictures of other bands, venues and places from Wikimedia Commons and the Royal Academy, standing in for the band. The band is invented.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-reverse', style={'spacing': {'padding': {'top': P(60), 'bottom': P(40)}, 'margin': {'top': '0'}}}, layout={'type': 'constrained'}))
write('parts/notice.html', pattern_ref('notice-tour'))

# ---------------------------------------------------------------- templates
def tpl(name, inner, top=50, bottom=70):
    write('templates/%s.html' % name, page_template(inner, style=pad(top, bottom)))

write('templates/front-page.html', page_template(J(
    pattern_ref('current-release'), pattern_ref('live-dates-short'), spacer(), pattern_ref('photo-strip'),
    group(pattern_ref('album-story'), align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    group(pattern_ref('release-grid'), align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    group(pattern_ref('merch-rail'), align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    spacer(), pattern_ref('mailing-list')), style={'spacing': {'padding': {'bottom': '0'}}}))
tpl('home', J(heading('Records', 1, align='wide'), pattern_ref('release-archive')))
tpl('archive', J(dyn('query-title', type='archive', showPrefix=False, align='wide'), pattern_ref('release-archive')))
tpl('index', J(dyn('query-title', type='archive', align='wide'), pattern_ref('release-archive')))
tpl('search', J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='A song, a town, a record', buttonText='Search', align='wide'), pattern_ref('release-archive')))
tpl('404', J(heading('Wrong venue', 1), para('Nothing here. The <a href="/live/">live dates</a> are where most people are trying to get to.'),
             dyn('search', label='Search', showLabel=False, placeholder='A song, a town, a record', buttonText='Search')))
tpl('page', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained'})))
tpl('page-wide', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1360px'})))
tpl('single', J(
    columns(('50%', dyn('post-featured-image', aspectRatio='1', scale='cover')),
            ('50%', J(dyn('post-terms', term='category', style={'typography': {'fontWeight': '700'}}), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', moreText='', fontSize='large'),
                      buttons(('Buy it in the shop', '/shop/'), ('Tour dates', '/live/')))),
            align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': P(50)}}}),
    dyn('post-content', align='wide', layout={'type': 'constrained'}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Older record', showTitle=True), dyn('post-navigation-link', label='Newer record', showTitle=True)), justify='space-between'),
          align='wide', className='is-style-rule-top', layout={'type': 'default'})), top=40)
print('amp built')

# ---------------------------------------------------------------- demo content
posts = [
    {'title': 'Slack Water', 'category': 'albums', 'image': 'sleeve-3.jpg', 'excerpt': 'Second album. LP, CD, cassette. SALT014, 14 November 2026.', 'pattern': 'amp/release-page', 'date': '2026-09-20'},
    {'title': 'Promenade Lights', 'category': 'singles', 'image': 'sleeve-4.jpg', 'excerpt': 'Single, 7 inch and download. SALT012, June 2026.',
     'content': J(para('Three minutes and eleven seconds about walking home along the front after the last train has gone. B-side: a cover of a brass band march, played badly on purpose.'), lst(['Promenade Lights', 'Hail Smiling Morn'], ordered=True)), 'date': '2026-06-05'},
    {'title': 'Live at the Platform', 'category': 'live', 'image': 'venue-1.jpg', 'excerpt': 'Live album, recorded on the last night of the 2025 tour. Download only.',
     'content': para('Fourteen songs, one broken string, recorded straight to tape by the venue\'s sound engineer. Pay what you like on Bandcamp. All money goes to the Platform\'s roof fund.'), 'date': '2025-12-10'},
    {'title': 'Ferry Songs', 'category': 'eps', 'image': 'gear-2.jpg', 'excerpt': 'EP, cassette and download. SALT009, 2024.',
     'content': J(para('Four songs recorded in Ollie\'s mum\'s garage on a borrowed eight-track. The cassettes sold out in a week and we are not making more.'), lst(['Heysham Heads', 'Bare Arms', 'Low Water', 'The Ferry Doesn\'t Wait (demo)'], ordered=True)), 'date': '2024-04-19'},
    {'title': 'Winter Gardens', 'category': 'singles', 'image': 'sleeve-1.jpg', 'excerpt': 'Single, download only. SALT013, September 2026.',
     'content': para('The second song from Slack Water, about the theatre on the front that has been closing for as long as we have been alive and is still open. Recorded live in one take.'), 'date': '2026-09-05'},
    {'title': 'Promenade', 'category': 'albums', 'image': 'town-1.jpg', 'excerpt': 'Debut album. LP and CD. SALT004, 2021.',
     'content': para('The first record. Nine songs about the town, the pier that isn\'t there any more and the one that is. Second pressing on black vinyl, still available.'), 'date': '2021-10-01'},
]
content = {
    'site': {'title': 'Heysham Ferry', 'tagline': 'Loud songs about the sea, from Morecambe'},
    'categories': [{'slug': 'albums', 'name': 'Albums'}, {'slug': 'eps', 'name': 'EPs'}, {'slug': 'singles', 'name': 'Singles'}, {'slug': 'live', 'name': 'Live'}],
    'front_page': 'home', 'posts_page': 'records',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'records', 'title': 'Records', 'content': ''},
        {'slug': 'live', 'title': 'Live', 'pattern': 'amp/page-live'},
        {'slug': 'epk', 'title': 'EPK', 'pattern': 'amp/page-epk'},
        {'slug': 'workshops', 'title': 'Workshops', 'pattern': 'amp/page-workshops'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'amp/page-contact'},
    ],
    'posts': posts,
    'nav': [{'label': 'Live', 'url': '/live/'}, {'label': 'Records', 'url': '/records/'}, {'label': 'Shop', 'url': '/shop/'}, {'label': 'EPK', 'url': '/epk/'},
            {'label': 'Workshops', 'url': '/workshops/'}, {'label': 'Contact', 'url': '/contact/'}],
    'currency': 'GBP',
    'products': [
        {'name': 'Slack Water, LP', 'price': '24', 'image': 'sleeve-3.jpg', 'category': 'Records', 'sku': 'SALT014-LP', 'stock': 300, 'short': 'Sea-green vinyl, gatefold, lyric sheet. Ships 14 November.'},
        {'name': 'Slack Water, CD', 'price': '12', 'image': 'sleeve-3.jpg', 'category': 'Records', 'sku': 'SALT014-CD', 'stock': 200, 'short': 'Card wallet. Ships 14 November.'},
        {'name': 'Slack Water, cassette', 'price': '8', 'image': 'gear-2.jpg', 'category': 'Records', 'sku': 'SALT014-MC', 'stock': 150, 'short': 'Edition of 150, with a download code.'},
        {'name': 'Promenade, LP (second pressing)', 'price': '20', 'image': 'town-1.jpg', 'category': 'Records', 'sku': 'SALT004-LP', 'stock': 40, 'short': 'Black vinyl.'},
        {'name': 'Tour poster, A2 screenprint', 'price': '15', 'image': 'sleeve-4.jpg', 'category': 'Posters', 'sku': 'HF-P01', 'stock': 60, 'short': 'Two colours on 170gsm paper, signed by all three of us.'},
        {'name': 'Pier tote bag', 'price': '12', 'image': 'town-1.jpg', 'category': 'Clothes and bags', 'sku': 'HF-T01', 'stock': 80, 'short': 'Heavy cotton, printed one colour in Lancaster.'},
    ],
}
os.makedirs('demos/amp', exist_ok=True)
json.dump(content, open('demos/amp/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
