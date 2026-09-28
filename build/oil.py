# Design note (oil, idea 002, painter: studio and available works)
# Direction: a catalogue raisonne on a cool gallery-white wall. The whole output is the site; there is no hero.
# Why: painters with a long body of work need a searchable record (medium, year, availability) more than a pitch.
# Fonts: Gloock (display, one weight, used big and sparingly) + Libre Franklin (body, captions with tabular figures).
# Palette: #F4F5F5 wall white, #1C1B19 text, #8C2F23 red-dot oxide used only for links and the "Sold" dot.
# Layout idea: a 3/12 index column (big "Work" title, medium / year / availability lists, sticky on desktop) beside
# a dense 9/12 grid of uncropped paintings; each sold work keeps its gallery red dot, and every work page gives
# size in cm and inches with a plain availability line.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('oil')
S = THEME['slug']

# Round 2: works and journal notes are both posts. Work queries are limited to the medium categories
# (ids 2, 3, 4 in the demo: paintings, drawings, monotypes); journal notes live in category 5 and use their own templates.
WORK_CATS = [2, 3, 4]
JOURNAL_CAT = 5
CATS = {'oil-catalogue': 'Painter: catalogue and works', 'oil-work-page': 'Painter: work page details', 'oil-exhibitions': 'Painter: exhibitions and gallery',
        'oil-cv': 'Painter: CV and press', 'oil-journal': 'Painter: journal', 'oil-contact': 'Painter: visits, buying and contact',
        'oil-pages': 'Painter: page layouts'}
CATMAP = {'portfolio': 'oil-catalogue', 'featured': 'oil-exhibitions', 'about': 'oil-cv', 'testimonials': 'oil-cv', 'text': 'oil-journal',
          'posts': 'oil-journal', 'contact': 'oil-contact', 'call-to-action': 'oil-contact', 'banner': 'oil-contact', 'shop': 'oil-contact',
          'work-caption': 'oil-work-page', 'work-detail': 'oil-work-page', 'dimensions-line': 'oil-work-page', 'price-on-request': 'oil-work-page',
          'sold-marker': 'oil-work-page', 'describe-work': 'oil-work-page', 'enquire-button': 'oil-work-page', 'now-showing': 'oil-exhibitions',
          'representation': 'oil-exhibitions', 'exhibitions-list': 'oil-exhibitions', 'studio-strip': 'oil-journal'}
_query = query
def query(inner, category=None, **kw):
    m = _query(inner, **kw)
    if category:
        m = m.replace('"inherit":false}', '"inherit":false,"taxQuery":{"category":%s}}' % json.dumps(category, separators=(',', ':')), 1)
    return m

_pattern = pattern
def pattern(slug, title, cats, body, **kw):
    first = cats.split(',')[0]
    c = 'oil-pages' if kw.get('block_types') == 'core/post-content' else CATMAP.get(slug) or CATMAP.get(first, 'oil-catalogue')
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
        f['name'] = 'Gloock'
    if f['slug'] == 'body':
        f['name'] = 'Libre Franklin'

# ------------------------------------------------------------------ theme.json
PALETTE = [
    ('base', '#F4F5F5', 'Gallery wall'), ('contrast', '#1C1B19', 'Lamp black'), ('accent', '#8C2F23', 'Red dot'),
    ('surface', '#ECEAE3', 'Primed linen'), ('line', '#C9C5BA', 'Pencil line'), ('muted', '#5B5954', 'Payne\'s grey'),
]
link = lambda c='accent', h='contrast': {'color': {'text': 'var:preset|color|' + c}, ':hover': {'color': {'text': 'var:preset|color|' + h}}}
focus = {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}

CSS = (
    ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}'
    'body{font-synthesis:none}'
    '.wp-block-table,.wp-block-post-date,.wp-block-archives,.wp-block-categories,.is-style-caption-line{font-variant-numeric:tabular-nums lining-nums}'
    '.wp-block-post-terms a[href*="/tag/sold"]::before,.is-style-red-dot::before{content:"";display:inline-block;width:.62em;height:.62em;border-radius:50%;background:var(--wp--preset--color--accent);margin-right:.45em;vertical-align:.02em}'
    '.wp-block-post-terms a[href*="/tag/sold"]{color:var(--wp--preset--color--accent)}'
    '@media (min-width:782px){.wp-block-column.is-style-index-column{position:sticky;top:var(--wp--preset--spacing--50);align-self:flex-start}}'
    '@media (max-width:600px){.wp-block-post-template.is-style-catalogue.is-layout-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}'
    '.wp-block-post-template.is-style-catalogue{align-items:start}'
    '.wp-block-table table.has-fixed-layout{table-layout:auto}.wp-block-table table td,.wp-block-table table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.6em 1.2em .6em 0;text-align:left;vertical-align:top}'
    '.wp-block-table table td:first-child{white-space:nowrap;width:1%}.wp-block-table table td{word-break:normal;overflow-wrap:break-word}.wp-block-table table thead{border-bottom:0}.wp-block-table table thead th{border-bottom:1px solid var(--wp--preset--color--contrast);font-weight:600}'
    'p.is-style-caption-line{margin-block-start:.25rem}'
    '.wp-block-post-featured-image img{background:var(--wp--preset--color--surface)}'
    '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-underline-offset:.3em}'
    '@media (prefers-reduced-motion:no-preference){.wp-block-post-featured-image a img{transition:opacity .15s}.wp-block-post-featured-image a:hover img{opacity:.86}}'
)

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '680px', 'wideSize': '1400px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': FONTS,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Caption', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Dimensions', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.375rem', 'name': 'Large', 'fluid': {'min': '1.2rem', 'max': '1.375rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Title', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.25rem', 'name': 'Section', 'fluid': {'min': '2.25rem', 'max': '3.25rem'}},
                {'slug': 'display', 'size': '5rem', 'name': 'Display', 'fluid': {'min': '3.25rem', 'max': '5rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': sp(40), 'right': sp(40)}, 'blockGap': sp(30)},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '1.05', 'letterSpacing': '-0.015em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.15'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {'color': {'background': 'transparent', 'text': 'var:preset|color|contrast'},
                       'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.25em', 'right': '1.25em'}},
                       ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}},
                       ':focus': focus},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '400', 'letterSpacing': '-0.01em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|muted'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.35'},
                           'border': {'left': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'left': sp(40)}},
                           'css': '& cite{display:block;margin-top:.8em;font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--x-small);font-style:normal;color:var(--wp--preset--color--muted)}'},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large'},
                               'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '&{table-layout:auto}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': sp(20), 'bottom': sp(20)}},
                             'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'},
                            'css': '& .wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:0;background:transparent}'},
            'core/categories': {'typography': {'fontSize': 'var:preset|font-size|small'}, 'css': '&{list-style:none;padding:0}& li{margin:.15em 0}'},
            'core/archives': {'typography': {'fontSize': 'var:preset|font-size|small'}, 'css': '&{list-style:none;padding:0}& li{margin:.15em 0}'},
            'core/tag-cloud': {'css': '& a{font-size:var(--wp--preset--font-size--small)!important;margin-right:.9em;display:inline-block}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-title': {'typography': {'fontSize': 'var:preset|font-size|display'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'single-work', 'title': 'Work (painting and caption)', 'postTypes': ['post']},
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    ],
}
wjson('theme.json', theme)

# ------------------------------------------------------------------ style variations
def variation(title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}
    if extra:
        d['styles'] = extra
    return d

wjson('styles/salon.json', variation('Salon', [
    ('base', '#2D2A26', 'Salon wall'), ('contrast', '#F2EEE6', 'Chalk'), ('accent', '#E3917A', 'Red dot'),
    ('surface', '#39352F', 'Dark linen'), ('line', '#5C564D', 'Rule'), ('muted', '#BDB5A8', 'Warm grey')]))
wjson('styles/linen.json', variation('Linen', [
    ('base', '#EDE8DC', 'Raw linen'), ('contrast', '#3D3A33', 'Umber'), ('accent', '#8C2F23', 'Red dot'),
    ('surface', '#E2DCCD', 'Primed linen'), ('line', '#C4BCA9', 'Pencil line'), ('muted', '#5E5A52', 'Grey umber')],
    {'typography': {'fontFamily': 'var:preset|font-family|body'}}))
wjson('styles/ultramarine.json', variation('Ultramarine', [
    ('base', '#FFFFFF', 'White'), ('contrast', '#1C1B19', 'Lamp black'), ('accent', '#1F3A8A', 'Ultramarine'),
    ('surface', '#F0F1F4', 'Cool white'), ('line', '#C9CCD4', 'Blue-grey line'), ('muted', '#55585F', 'Slate')]))

# ------------------------------------------------------------------ section styles
def section(slug, title, blocks, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                             'title': title, 'slug': slug, 'blockTypes': blocks, 'styles': styles})

section('wall-label', 'Wall label', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': sp(60), 'bottom': sp(60), 'left': sp(40), 'right': sp(40)}}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': sp(40)}}})
section('rule-bottom', 'Rule below', ['core/group'], {
    'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}})
section('catalogue', 'Catalogue grid', ['core/post-template'], {'spacing': {'blockGap': sp(50)}})
section('index-column', 'Index column (sticky on desktop)', ['core/column'], {})
section('red-dot', 'Sold (red dot)', ['core/paragraph'], {'color': {'text': 'var:preset|color|accent'}})
section('caption-line', 'Caption line', ['core/paragraph'], {'typography': {'fontSize': 'var:preset|font-size|small'}, 'color': {'text': 'var:preset|color|muted'}})
section('open-notice', 'Open studio notice', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}},
    'typography': {'fontSize': 'var:preset|font-size|small'}})

# ------------------------------------------------------------------ style.css
write('style.css', '''/*
Theme Name: Oil
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A catalogue of a painter's whole output, with every work's size, medium, year and availability, for painters who sell from the studio and through galleries.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: oil
Tags: portfolio, photography, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout, two-columns
*/''')

# ------------------------------------------------------------------ parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'},
                                       style={'spacing': {'blockGap': sp(40)}})),
        justify='space-between', align='wide'),
    tag='header', align='full', style=pad(50, 40)))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0),
                  para('Paintings, drawings and monotypes by Agnes Brekke. Studio visits by appointment on Thursdays.', fontSize='small'))),
        (None, J(heading('Studio', 6),
                 para('Top floor, 3 Couper Street<br>Leith, Edinburgh EH6 6HH<br><a href="mailto:studio@example.com">studio@example.com</a><br>0131 496 0724', fontSize='small'))),
        (None, J(heading('Represented by', 6),
                 para('Fairlie Gallery, 14 Dundas Street, Edinburgh, for Scotland and the north of England. Everything else, email the studio.', fontSize='small'))),
        align='wide'),
    para('The demo paintings are by Vilhelm Hammershøi (1864 to 1916) and other public domain works from Wikimedia Commons, used as stand-ins.', align='wide', textColor='muted', fontSize='x-small')),
    tag='footer', align='full', className='is-style-rule-top', style=pad(60, 50)))

# ------------------------------------------------------------------ works data (also used for demo content)
def inches(cm):
    v = round(cm / 2.54 * 4) / 4
    whole = int(v)
    frac = {0: '', 0.25: '¼', 0.5: '½', 0.75: '¾'}[v - whole]
    return '%d%s' % (whole, frac)

def dims(h, w):
    fmt = lambda x: ('%g' % x)
    return '%s × %s cm / %s × %s in' % (fmt(h), fmt(w), inches(h), inches(w))

WORKS = [
    dict(t='Sunlight on the floor, Couper Street', img='hero.jpg', date='2026-08-14', cat='paintings', mat='Oil on linen', h=61, w=51,
         st='available', price='£4,800', tags=['Interiors', 'Available'],
         desc='The front room at nine in the morning in August. Two tall windows on the left throw squares of light across bare boards towards a closed panelled door. The walls are a warm brown grey. There is nobody in the room.'),
    dict(t='White door and yellow cupboard', img='work-9.jpg', date='2026-06-02', cat='paintings', mat='Oil on panel', h=40, w=38,
         st='available', price='£2,600', tags=['Interiors', 'Available'],
         desc='A small, loosely painted panel. A pale door stands half open on the left; on the right, a tall cupboard in ochre catches the light from the hall.'),
    dict(t='Music room, afternoon', img='work-1.jpg', date='2026-03-20', cat='paintings', mat='Oil on linen', h=90, w=80,
         st='sold', price='£7,200', tags=['Interiors', 'Sold'],
         desc='A grey panelled room with a square piano under a framed print, a white chair pulled out and a cello leaning on the wall. Soft light from a door on the left.'),
    dict(t='Moonlight, Couper Street', img='work-5.jpg', date='2025-11-03', cat='monotypes', mat='Oil-based monotype on Somerset Satin 300gsm', h=50, w=62,
         st='loan', price='', tags=['Interiors', 'On loan'],
         desc='The same front room at night, printed in violet greys. Moonlight makes pale rectangles on the floor under the window. The door is shut.'),
    dict(t='Bookcase and Windsor chair', img='work-2.jpg', date='2025-08-19', cat='paintings', mat='Oil on linen', h=70, w=60,
         st='sold', price='£5,900', tags=['Interiors', 'Sold'],
         desc='A narrow bookcase against a mottled grey wall with a small painting hung above it. A Windsor chair on the left and a dark table with a white bowl on the right.'),
    dict(t='Two sisters reading', img='work-6.jpg', date='2025-05-07', cat='paintings', mat='Oil on canvas', h=64, w=84,
         st='available', price='£6,400', tags=['Portraits', 'Available'],
         desc='Two women at a table, one facing us and reading with her head bowed, the other seen from behind in shadow. Olive and brown, lit from the left.'),
    dict(t='The old exchange from the Water of Leith', img='work-7.jpg', date='2024-10-12', cat='paintings', mat='Oil on linen', h=60, w=78,
         st='sold', price='£5,200', tags=['The city', 'Sold'],
         desc='A long pale civic building across still green water, under a flat grey sky. A stone bridge on the right. Painted on site over four mornings in October.'),
    dict(t='Field above Gullane', img='work-3.jpg', date='2024-07-01', cat='paintings', mat='Oil on board', h=36, w=62,
         st='available', price='£2,900', tags=['Landscape', 'Available'],
         desc='A wide sheep field rising to a low ridge with three dark clumps of trees, under a blue sky with small, even clouds.'),
    dict(t='Trees on Leith Links, study', img='work-8.jpg', date='2024-02-15', cat='drawings', mat='Graphite on cartridge paper', h=30, w=40,
         st='available', price='£850', tags=['Landscape', 'Available'],
         desc='A quick pencil study of thin bare trees along a path, drawn standing up in February. Loose hatching, lots of white paper.'),
    dict(t='Prince Albert, Charlotte Square', img='work-4.jpg', date='2023-09-28', cat='paintings', mat='Oil on linen', h=120, w=80,
         st='sold', price='£9,500', tags=['The city', 'Sold'],
         desc='An equestrian statue on a high stone plinth, seen from below against the pale stone front of a Georgian terrace. Nearly monochrome, grey and cream.'),
]
YEAR = lambda w: w['date'][:4]

def status_line(w):
    if w['st'] == 'available':
        return para('Available, %s' % w['price'])
    if w['st'] == 'sold':
        return para('Sold, %s. Last price %s' % (YEAR(w), w['price']), className='is-style-red-dot')
    return para('Unavailable. On loan to the Leith Civic Collection until March 2027.')

def work_caption_blocks(w):
    subj = 'Enquiry: %s (%s)' % (w['t'], YEAR(w))
    mail = 'mailto:studio@example.com?subject=' + subj.replace(' ', '%20').replace(',', '%2C').replace('(', '%28').replace(')', '%29')
    label = 'Enquire about this work' if w['st'] == 'available' else 'Ask about similar work'
    return J(
        para(w['mat'], className='is-style-caption-line'),
        para(dims(w['h'], w['w']), className='is-style-caption-line'),
        status_line(w),
        buttons((label, mail)),
        details('Describe this work', para(w['desc'])))

# ------------------------------------------------------------------ patterns
card = J(dyn('post-featured-image', isLink=True),
         group(J(dyn('post-title', isLink=True, level=3, fontSize='small', fontFamily='body', style={'typography': {'fontWeight': '500', 'lineHeight': '1.35'}}),
                 row(J(dyn('post-date', format='Y'), dyn('post-terms', term='post_tag', separator=', ')), style={'spacing': {'blockGap': sp(20)}})),
               layout={'type': 'flex', 'orientation': 'vertical'}, style={'spacing': {'blockGap': sp(10)}}))

pattern('filter-panel', 'Index: medium, year and availability', 'portfolio', J(
    heading('Medium and journal', 2, fontSize='small', fontFamily='body', style={'typography': {'fontWeight': '600'}}),
    dyn('categories', showPostCounts=True),
    heading('Year', 2, fontSize='small', fontFamily='body', style={'typography': {'fontWeight': '600'}}),
    dyn('archives', type='yearly', showPostCounts=True),
    heading('Availability and subject', 2, fontSize='small', fontFamily='body', style={'typography': {'fontWeight': '600'}}),
    dyn('tag-cloud', smallestFontSize='15px', largestFontSize='15px')),
    description='The filter column: lists of mediums, years and tags that link to their archives.')

# The index column carries the sticky section style, so columns are written by hand.
def index_columns(left, right):
    return ('<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60","top":"var:preset|spacing|50"}}}} -->\n'
            '<div class="wp-block-columns alignwide"><!-- wp:column {"width":"25%%","className":"is-style-index-column"} -->\n'
            '<div class="wp-block-column is-style-index-column" style="flex-basis:25%%">%s</div>\n<!-- /wp:column -->\n\n'
            '<!-- wp:column {"width":"75%%"} -->\n<div class="wp-block-column" style="flex-basis:75%%">%s</div>\n<!-- /wp:column --></div>\n<!-- /wp:columns -->') % (left, right)

pattern('catalogue-index', 'Catalogue index (front page)', 'portfolio,featured,query', index_columns(
    J(heading('Work', 1),
      para('Agnes Brekke paints the rooms she lives in, the city around them and the people who visit, mostly in oil on linen, in a top-floor studio in Leith.'),
      pattern_ref('filter-panel')),
    query(card, per_page=12, category=WORK_CATS, layout={'type': 'grid', 'columnCount': 4}, template_class='is-style-catalogue')),
    description='Signature: the index column beside a grid of every work, newest first, with sold works marked by a red dot.')

pattern('catalogue-archive', 'Catalogue archive (inherits the page query)', 'portfolio,query', index_columns(
    J(dyn('query-title', type='archive', showPrefix=False), dyn('term-description'), pattern_ref('filter-panel')),
    inherit_query(card, layout={'type': 'grid', 'columnCount': 4}, template_class='is-style-catalogue')), inserter=False)

pattern('catalogue-all', 'Catalogue, all work (posts page)', 'portfolio,query', index_columns(
    J(heading('All work', 1),
      para('Every finished painting, drawing and monotype since 2014, sold ones included, so the prices here double as a record.', fontSize='small'),
      pattern_ref('filter-panel')),
    query(card, per_page=48, category=WORK_CATS, query_id=2, layout={'type': 'grid', 'columnCount': 4}, template_class='is-style-catalogue')),
    description='The whole catalogue. Choose your medium categories in the Query Loop settings.')

pattern('post-list', 'Plain list of results', 'posts,query', inherit_query(
    row(J(dyn('post-date', format='Y'), dyn('post-title', isLink=True, level=2, fontSize='large', fontFamily='body')), wrap=True,
        className='is-style-rule-bottom', style={'spacing': {'padding': {'bottom': sp(30)}}}),
    align='wide'), inserter=False)

W0 = WORKS[0]

def label_rows(rows):
    return group(J(*[columns(('30%', para(k, textColor='muted', fontSize='small')), (None, para(v, fontSize='small')), isStackedOnMobile=False,
                             className='is-style-rule-bottom', style={'spacing': {'blockGap': {'left': sp(30)}, 'padding': {'bottom': sp(10)}}}) for k, v in rows]),
                 layout={'type': 'default'}, style={'spacing': {'blockGap': sp(20)}})
pattern('work-caption', 'Work caption (medium, size in cm and inches, availability)', 'portfolio', J(
    work_caption_blocks(W0)),
    description='Put this in each work post. Size is given once in cm and once in inches, then a plain availability line.')

pattern('work-detail', 'Work detail (painting 8/12, caption 4/12)', 'portfolio', columns(
    ('66.66%', image(W0['img'], 'Oil painting of an empty room with sunlight falling in squares across bare floorboards, 61 × 51 cm')),
    ('33.33%', J(heading(W0['t'], 2, fontSize='x-large'), para(YEAR(W0), textColor='muted', fontSize='small'), work_caption_blocks(W0))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('dimensions-line', 'Size in cm and inches', 'portfolio', para(dims(61, 51), className='is-style-caption-line'),
        description='Type the size once in each unit, height first.')

pattern('price-on-request', 'Price on request', 'portfolio', J(
    para('Price on request. Large works are shown at Fairlie Gallery before they are offered from the studio.'),
    buttons(('Ask the gallery for the price', 'mailto:hello@example.com?subject=Price%20request'))))

pattern('sold-marker', 'Sold marker with last price', 'portfolio', para('Sold, 2025. Last price £5,900', className='is-style-red-dot'),
        description='A red dot and the price it sold for. Leave sold works online so the archive keeps a price record.')

pattern('available-list', 'Available works (list with prices)', 'portfolio,shop', J(
    heading('Available now', 2, fontSize='x-large'),
    table([[w['t'], '%s, %s' % (w['mat'], YEAR(w)), dims(w['h'], w['w']), w['price']] for w in WORKS if w['st'] == 'available'],
          head=['Title', 'Medium and year', 'Size', 'Price']),
    para('Prices include a plain oak float frame and delivery in mainland Britain. Elsewhere, I quote for a crate.', fontSize='small')))

pattern('price-record', 'Sold works and last prices', 'portfolio', J(
    heading('Sold, with last prices', 3),
    table([[w['t'], YEAR(w), dims(w['h'], w['w']), w['price']] for w in WORKS if w['st'] == 'sold'], head=['Title', 'Year', 'Size', 'Sold for']),
    para('I keep this list public so collectors and insurers can see what the work has sold for.', fontSize='small', textColor='muted')))

EXH = [
    ('2026', 'Rooms without us', 'Fairlie Gallery, Edinburgh', 'Solo', '12 September to 1 November'),
    ('2025', 'Open painting show, annual', 'Mound Galleries, Edinburgh', 'Group', '8 to 30 March'),
    ('2024', 'Harbour paintings', 'Harbour Rooms, Dumfries', 'Solo', '3 May to 15 June'),
    ('2023', 'Small works', 'Fairlie Gallery, Edinburgh', 'Group', '1 to 23 December'),
    ('2022', 'Two floors', 'Nordnes Kunstrom, Bergen', 'Solo', '14 January to 20 February'),
    ('2019', 'New Contemporaries', 'Edinburgh College of Art', 'Group', '4 to 26 August'),
]
pattern('exhibitions-list', 'Exhibitions (solo and group, venue, dates)', 'about', J(
    heading('Exhibitions', 2, fontSize='x-large'),
    table([[y, '<em>%s</em>, %s' % (t, k.lower()), '%s<br>%s' % (v, d)] for y, t, v, k, d in EXH], head=['Year', 'Show', 'Venue and dates'])))

pattern('now-showing', 'Now showing (current exhibition)', 'featured', group(columns(
    ('50%', image('work-7.jpg', 'Oil painting of a long pale building across still green water under a grey sky, 60 × 78 cm')),
    (None, J(para('Now showing', fontSize='small', style={'typography': {'fontWeight': '600'}}),
             heading('<em>Rooms without us</em>', 2),
             para('Fourteen new paintings of the flat on Couper Street and the streets down to the shore. Nine are for sale.', fontSize='large'),
             label_rows([['Where', 'Fairlie Gallery, 14 Dundas Street, Edinburgh EH3 6HZ'], ['When', '12 September to 1 November 2026'],
                         ['Open', 'Tuesday to Saturday, 10am to 5pm'], ['Talk', 'Saturday 10 October, 2pm. Free, no need to book.']]),
             buttons(('See the works in the show', '/tag/available/')))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}, verticalAlignment='center'),
    className='is-style-wall-label', align='full'))

pattern('representation', 'Gallery representation line', 'about', para(
    'Represented in Scotland and the north of England by <a href="https://example.com/">Fairlie Gallery</a>, Edinburgh. For everything else, including studio sales, email <a href="mailto:studio@example.com">studio@example.com</a>.',
    fontSize='large'))

pattern('studio-visit', 'Studio visit enquiry', 'contact,call-to-action', group(J(
    heading('Visit the studio', 3),
    para('Thursdays, by appointment, 11am to 5pm. Top floor of 3 Couper Street, Leith. Four flights of stairs and no lift, so tell me if that is a problem and I will bring work down to Fairlie Gallery instead.'),
    buttons(('Book a Thursday visit', 'mailto:studio@example.com?subject=Studio%20visit'))),
    className='is-style-rule-top', layout={'type': 'default'}))

pattern('describe-work', 'Describe this work (image description toggle)', 'portfolio,text', details(
    'Describe this work', para(W0['desc'])),
    description='A description of the painting written by the artist, for people using screen readers and anyone who wants it.')

pattern('enquire-button', 'Enquire about this work', 'call-to-action', buttons(
    ('Enquire about this work', 'mailto:studio@example.com?subject=Enquiry%3A%20Sunlight%20on%20the%20floor%20%282026%29')),
    description='Change the subject line to the title and year of the work.')

CV = {
    'Education': [['2004 to 2006', 'MFA Painting, Glasgow School of Art'], ['1998 to 2002', 'BA (Hons) Painting, Edinburgh College of Art'], ['1997', 'Foundation, Bergen Academy of Art and Design']],
    'Awards and residencies': [['2023', 'Kirkhill summer residency, Arbroath'], ['2018', 'Dundas Street Painting Prize, shortlisted'], ['2011', 'Visual Arts Scotland, Open award']],
    'Collections': [['', 'Leith Civic Collection'], ['', 'Leith Hospital Trust'], ['', 'Private collections in Scotland, Norway, Canada and Japan']],
}
pattern('cv-education', 'CV: education', 'about', J(heading('Education', 3, fontSize='large'), label_rows(CV['Education'])))
pattern('cv-awards', 'CV: awards and residencies', 'about', J(heading('Awards and residencies', 3, fontSize='large'), label_rows(CV['Awards and residencies'])))
pattern('cv-collections', 'CV: collections', 'about', J(heading('Collections', 3, fontSize='large'), lst([r[1] for r in CV['Collections']])))
pattern('cv-solo', 'CV: solo shows', 'about', J(heading('Solo shows', 3, fontSize='large'), label_rows([[y, '<em>%s</em>, %s' % (t, v)] for y, t, v, k, d in EXH if k == 'Solo'])))
pattern('cv-group', 'CV: group shows', 'about', J(heading('Group shows', 3, fontSize='large'), label_rows([[y, '<em>%s</em>, %s' % (t, v)] for y, t, v, k, d in EXH if k == 'Group'])))

pattern('bibliography', 'Bibliography', 'about', J(
    heading('Bibliography', 3, fontSize='large'),
    lst(['Ailsa Munro, "Empty rooms, full light", <em>The Leither</em>, 20 September 2026',
         'Anders Lie, <em>Agnes Brekke: Two floors</em>, exhibition booklet, Nordnes Kunstrom, 2022, 24 pages',
         'Callum Reid, "A painter of weather indoors", <em>Scottish Art Notes</em>, 11 May 2024'])))

pattern('reviews', 'Articles and reviews (quotes)', 'testimonials', columns(
    (None, quote('She paints a Leith front room the way other people paint the sea: as something that changes every hour.', 'Ailsa Munro, The Leither, September 2026')),
    (None, quote('The best thing in the open show this year is a small grey room with a cello in it.', 'Callum Reid, Scottish Art Notes, March 2025')),
    align='wide'))

pattern('cv-download', 'CV as a PDF', 'about', para(
    'The full CV is also a two-page PDF: <a href="mailto:studio@example.com?subject=CV">ask for the PDF</a> and I send it the same day. Galleries can use it without asking.',
    fontSize='small'), description='Link a PDF of your CV here once you have uploaded it to the media library.')

pattern('about-bio', 'About: short bio', 'about', columns(
    ('40%', image('studio.jpg', 'Painting of a woman in a dark blue dress seated at an easel in a small studio with a red curtain behind her')),
    (None, J(
        para('Agnes Brekke (b. 1979, Bergen) is a painter. She has lived in Edinburgh since 1998 and works in a top-floor studio in Leith, in the flat she also lives in.', fontSize='large'),
        para('She paints rooms, mostly the same four, at different times of day, and the streets between her flat and the shore. Everything starts from life. She does not paint from photographs, which is also why she turns down house portraits of places she can\'t sit in.'),
        para('Her paintings are in the Leith Civic Collection and in private collections in Scotland, Norway, Canada and Japan. She teaches a drawing class at Leith School of Art on Tuesday evenings in term time.'),
        pattern_ref('representation'))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('about-page', 'Page: about and CV', 'about', J(
    pattern_ref('about-bio'),
    columns((None, J(pattern_ref('cv-education'), pattern_ref('cv-awards'), pattern_ref('cv-collections'))),
            (None, J(pattern_ref('cv-solo'), pattern_ref('cv-group'), pattern_ref('bibliography'), pattern_ref('cv-download'))),
            align='wide', className='is-style-rule-top', style={'spacing': {'blockGap': {'left': sp(60)}}}),
    pattern_ref('reviews'), pattern_ref('series-intro'), pattern_ref('materials'), pattern_ref('studio-photo')), block_types='core/post-content')

pattern('exhibitions-page', 'Page: exhibitions', 'about', J(
    pattern_ref('now-showing'), pattern_ref('exhibitions-list'), pattern_ref('gallery-card'),
    para('Photographs of past shows are on each painting\'s page. For loans, write to Fairlie Gallery.', fontSize='small', textColor='muted')),
    block_types='core/post-content')

JOURNAL = [
    ('18 September 2026', 'Hanging day', 'Fourteen paintings, one spirit level and Morag from the gallery, who hangs everything 2 cm lower than I would. She is right every time. The show opens on Saturday and the biggest painting still smells of linseed.'),
    ('2 August 2026', 'Why the floor is always bare', 'People ask where the rug went. It went to my sister in Bergen in 2019, and the light on bare boards turned out to be the whole subject. I will paint a rug when I own one again.'),
    ('30 May 2026', 'A new batch of linen', 'Twelve metres of Belgian linen, sized with rabbit-skin glue and primed with lead-free oil ground. It takes three weeks to cure before I can use it, so the next paintings start in late June.'),
]
pattern('journal-entry', 'Journal entry', 'text', group(J(
    para(JOURNAL[0][0], fontSize='small', textColor='muted'), heading(JOURNAL[0][1], 3), para(JOURNAL[0][2])), className='is-style-rule-top'))

pattern('journal-list', 'Journal (dated studio notes)', 'text', J(*[
    group(columns(('25%', para(d, fontSize='small', textColor='muted')), (None, J(heading(t, 3), para(b)))), className='is-style-rule-top', align='wide')
    for d, t, b in JOURNAL]))

pattern('journal-page', 'Page: journal', 'text', J(
    para('Notes from the studio, a few times a year. Mostly about paint, sometimes about the stairs.', fontSize='large'),
    pattern_ref('journal-list')), block_types='core/post-content')

pattern('contact-details', 'Contact details', 'contact', columns(
    (None, J(heading('Write to the studio', 2, fontSize='x-large'),
             para('Email <a href="mailto:studio@example.com">studio@example.com</a>. I answer on Mondays and Thursdays, so give it a few days.'),
             para('Phone 0131 496 0724, Thursdays only, 10am to 5pm.'),
             para('Top floor, 3 Couper Street, Leith, Edinburgh EH6 6HH. The 16 and 22 buses stop on Great Junction Street, five minutes away.'))),
    (None, J(heading('Buying a painting', 3),
             para('Works marked available can be bought from the studio. I send a payment link, hold the painting for seven days and deliver it myself anywhere between Aberdeen and Newcastle. Further away, it goes by fine-art courier at cost.'),
             para('Works at Fairlie Gallery are sold by the gallery. Prices are the same either way.'))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('contact-page', 'Page: contact', 'contact', J(pattern_ref('contact-details'), pattern_ref('visit-and-find'), pattern_ref('studio-visit'), pattern_ref('open-studio')), block_types='core/post-content')

pattern('notice-open-studio', 'Notice: open studio weekend', 'banner', group(
    para('Open studio on Saturday 7 and Sunday 8 November, 11am to 5pm. Unframed drawings from £250. Take this bar down on 9 November.'),
    className='is-style-open-notice', align='full', style=pad(20, 20)),
    description='A one-line notice for open studio dates. Remove it after the weekend.')

pattern('studio-strip', 'Studio and journal strip (front page)', 'featured', columns(
    (None, J(heading('From the journal', 2, fontSize='x-large'),
             query(J(dyn('post-date', fontSize='small'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=24)),
                   per_page=3, category=[JOURNAL_CAT], query_id=3),
             para('<a href="/category/journal/">All journal notes</a>', fontSize='small'))),
    (None, J(pattern_ref('representation'), pattern_ref('studio-visit'))),
    align='wide', className='is-style-rule-top', style={'spacing': {'blockGap': {'left': sp(70)}}}))

pattern('year-heading', 'Year heading with works', 'portfolio', J(
    columns(('25%', heading('2026', 2, fontSize='display')),
            (None, gallery([(w['img'], '%s, %s, %s' % (w['t'], w['mat'].lower(), dims(w['h'], w['w'])), w['t']) for w in WORKS if YEAR(w) == '2026'], columns=3)),
            align='wide')),
    description='A hand-picked year: big year numeral at the left, the year\'s works on the right.')


# ------------------------------------------------------------------ round 2: journal posts and more of the kit
journal_card = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3'), dyn('post-date', fontSize='small'),
                 dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=26))
pattern('journal-latest', 'Journal: latest three notes', 'posts,query', J(
    row(J(heading('Journal', 2, fontSize='x-large'), para('<a href="/category/journal/">All notes</a>', fontSize='small')), justify='space-between', align='wide'),
    query(journal_card, per_page=3, category=[JOURNAL_CAT], query_id=4, layout={'type': 'grid', 'columnCount': 3}, align='wide')),
    description='The three newest journal notes. Set the Journal category in the Query Loop settings.')

pattern('journal-archive', 'Journal archive (inherits the page query)', 'posts,query', inherit_query(
    columns(('33%', dyn('post-featured-image', isLink=True, aspectRatio='4/3')),
            (None, J(dyn('post-date', fontSize='small'), dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', excerptLength=40))),
            className='is-style-rule-top', style={'spacing': {'blockGap': {'left': sp(50)}, 'padding': {'top': sp(40)}}}),
    align='wide'), inserter=False)

pattern('journal-feature', 'Journal: newest note, large', 'posts,query', query(
    columns(('58%', dyn('post-featured-image', isLink=True)),
            (None, J(dyn('post-date', fontSize='small'), dyn('post-title', isLink=True, level=2, fontSize='xx-large'), dyn('post-excerpt', excerptLength=50, moreText='Read the note'))),
            verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(60)}}}),
    per_page=1, category=[JOURNAL_CAT], query_id=5, align='wide'))

pattern('studio-photo', 'Studio photo with caption', 'text', image('j-easel.jpg', 'Etching of a painter sitting back in a chair in front of a tall studio window', 'The studio window faces north over the rooftops, which is why the paintings are grey.'))

pattern('series-intro', 'Series: Couper Street rooms', 'portfolio', J(
    columns(('33%', J(heading('Couper Street rooms', 2, fontSize='x-large'),
                      para('Since 2019 I have painted the same four rooms of the flat at different hours. Twenty-two paintings so far; these are the ones still in the studio or on loan.'))),
            (None, gallery([('hero.jpg', 'Oil painting of an empty room with sunlight on the floorboards', 'Sunlight on the floor'),
                            ('work-9.jpg', 'Oil painting of a pale door and an ochre cupboard', 'White door and yellow cupboard'),
                            ('work-1.jpg', 'Oil painting of a grey room with a piano and a cello', 'Music room, afternoon'),
                            ('work-5.jpg', 'Monotype of the same room at night in violet greys', 'Moonlight')], columns=2)),
            align='wide', style={'spacing': {'blockGap': {'left': sp(60)}}})))

pattern('available-cards', 'Available now (cards with prices)', 'portfolio,shop', J(
    heading('Available from the studio', 2, fontSize='x-large'),
    group(J(*[group(J(image(w['img'], '%s, %s, %s' % (w['t'], w['mat'].lower(), dims(w['h'], w['w']))),
                      heading(w['t'], 3, fontSize='medium', fontFamily='body', style={'typography': {'fontWeight': '500'}}),
                      para('%s, %s' % (w['mat'], dims(w['h'], w['w'])), className='is-style-caption-line'),
                      para(w['price'])), layout={'type': 'flex', 'orientation': 'vertical'}, style={'spacing': {'blockGap': sp(10)}})
              for w in WORKS if w['st'] == 'available'][:4]),
          layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}, style={'spacing': {'blockGap': sp(50)}})))

pattern('buying-steps', 'How to buy a painting', 'call-to-action', J(
    heading('Buying a painting from the studio', 3),
    lst(['Email me the title. I reply the same week with more photos, including one on the wall for scale.',
         'If you want it, I send a payment link and hold the painting for seven days.',
         'I deliver it myself between Aberdeen and Newcastle, usually on a Sunday. Further away, a fine-art courier at cost.',
         'If it looks wrong on your wall, you have 14 days to send it back.'], ordered=True)))

pattern('framing-note', 'Framing and hanging', 'text', J(
    heading('Frames', 3),
    para('Paintings come in a plain oak float frame, 2 cm deep, with a D-ring on each side and wire. Works on paper come unframed in a card mount; I can recommend two framers in Leith.')))

pattern('materials', 'Materials', 'text', J(
    heading('What the paintings are made of', 3),
    lst(['Belgian linen, primed in the studio with oil ground.', 'Oil paint from Michael Harding and Williamsburg, mostly earth colours and one cadmium red.', 'Cold-wax medium for the matt surfaces.', 'Monotypes printed on the etching press at Edinburgh Printmakers.'])))

pattern('collector-quote', 'Collector quote', 'testimonials', quote(
    'It hangs opposite our kitchen window, and it is a different painting at seven in the morning and at five in the afternoon.',
    'Ingrid and Tom, Portobello, bought <em>Two sisters reading</em> in 2025'))

pattern('gallery-card', 'Representing gallery', 'featured', columns(
    ('40%', image('j-leith.jpg', 'A two-storey stone and white-rendered corner building on a sunny street')),
    (None, J(heading('Fairlie Gallery', 3), para('14 Dundas Street, Edinburgh EH3 6HZ. Tuesday to Saturday, 10am to 5pm. Morag Fairlie has shown my work since 2017 and handles loans and exhibitions.'),
             para('<a href="mailto:hello@example.com">hello@example.com</a>, 0131 496 0990'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('open-studio', 'Open studio weekend', 'call-to-action', columns(
    ('40%', image('j-palette.jpg', 'An open paint box with a small oil sketch in the lid and a crusted palette below')),
    (None, J(heading('Open studio, 7 and 8 November', 3),
             lst(['Saturday and Sunday, 11am to 5pm', 'Unframed drawings and oil sketches from £250', 'Tea at 3pm, bring your own cup if you like']),
             para('No booking needed. The door is the green one next to the barber.'))),
    align='wide', style={'spacing': {'blockGap': {'left': sp(50)}}}))

pattern('visit-and-find', 'Visit and find the studio', 'contact', columns(
    (None, J(heading('Find the studio', 3), para('Top floor, 3 Couper Street, Leith, Edinburgh EH6 6HH. Green door next to the barber. The 16 and 22 buses stop on Great Junction Street.'))),
    (None, J(heading('When', 3), lst(['Thursdays, 11am to 5pm, by appointment', 'Open studio twice a year', 'Four flights of stairs, no lift']))),
    align='wide', className='is-style-rule-top', style={'spacing': {'blockGap': {'left': sp(60)}}}))

pattern('journal-page-layout', 'Page: journal index', 'posts', J(
    pattern_ref('journal-feature'), spacer(), pattern_ref('journal-latest')), block_types='core/post-content')
pattern('buying-page', 'Page: buying a painting', 'shop', J(
    pattern_ref('available-cards'), spacer(), pattern_ref('buying-steps'), pattern_ref('framing-note'), pattern_ref('collector-quote'), pattern_ref('price-record')), block_types='core/post-content')

# ------------------------------------------------------------------ templates
main_pad = {'spacing': {'padding': {'top': sp(40), 'bottom': sp(70)}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('catalogue-index'), spacer('var:preset|spacing|70'), pattern_ref('now-showing'), spacer('var:preset|spacing|70'), pattern_ref('journal-latest'),
    spacer('var:preset|spacing|60'), pattern_ref('visit-and-find')),
    layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': sp(40), 'bottom': sp(70)}, 'blockGap': '0'}}))
write('templates/home.html', page_template(pattern_ref('catalogue-all'), style=main_pad))
write('templates/archive.html', page_template(pattern_ref('catalogue-archive'), style=main_pad))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), style=main_pad))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide', fontSize='xx-large'),
    dyn('search', label='Search', showLabel=False, placeholder='Titles, rooms, years', buttonText='Search', align='wide'),
    pattern_ref('post-list')), style=main_pad))
write('templates/404.html', page_template(J(
    heading('Nothing hangs here', 1),
    para('The page may have moved when the catalogue was renumbered. The <a href="/work/">full list of work</a> has everything, sold paintings included.'),
    dyn('search', label='Search', showLabel=False, placeholder='Titles, rooms, years', buttonText='Search')), style=main_pad))
write('templates/page.html', page_template(J(
    dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'justifyContent': 'left'})), style=main_pad))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1400px'})), style=main_pad))

single_work = J(
    columns(
        ('66.66%', dyn('post-featured-image')),
        ('33.33%', J(dyn('post-title', level=1, fontSize='x-large'), dyn('post-date', format='Y', fontSize='small'),
                     dyn('post-content', layout={'type': 'default'}),
                     dyn('post-terms', term='category', prefix='Filed under '),
                     dyn('post-terms', term='post_tag', separator=', '))),
        align='wide', style={'spacing': {'blockGap': {'left': sp(60), 'top': sp(40)}}}),
    row(J(dyn('post-navigation-link', type='previous', label='Newer', showTitle=True),
          dyn('post-navigation-link', label='Older', showTitle=True)), justify='space-between', align='wide', className='is-style-rule-top'))
write('templates/single-work.html', page_template(single_work, style=main_pad))
write('templates/single.html', page_template(J(
    dyn('post-date', fontSize='small'), dyn('post-title', level=1, fontSize='xx-large'),
    dyn('post-featured-image', align='wide'),
    dyn('post-content', layout={'type': 'constrained'}),
    dyn('post-terms', term='category', prefix='Filed under '),
    row(J(dyn('post-navigation-link', type='previous', label='Newer note', showTitle=True, taxonomy='category'),
          dyn('post-navigation-link', label='Older note', showTitle=True, taxonomy='category')), justify='space-between', className='is-style-rule-top')),
    style=main_pad))
write('templates/category-journal.html', page_template(J(
    heading('Journal', 1, align='wide'),
    para('Notes from the studio, a few times a year. Mostly about paint, sometimes about the stairs.', align='wide', fontSize='large'),
    pattern_ref('journal-archive')), style=main_pad))

# ------------------------------------------------------------------ demo content
posts = []
for w in WORKS:
    posts.append({'title': w['t'], 'category': w['cat'], 'tags': w['tags'], 'image': w['img'], 'date': w['date'],
                  'template': 'single-work', 'content': work_caption_blocks(w)})
JPOSTS = [
    ('Hanging day', '2026-09-18', 'work-7.jpg', 'Fourteen paintings, one spirit level and Morag from the gallery, who hangs everything 2 cm lower than I would.',
     ['She is right every time. Lower paintings pull you closer, and my rooms need you close.',
      'We hung the big harbour painting last, on its own wall, so you see it through the doorway from the street. The biggest painting still smells of linseed. The show opens on Saturday at 2pm.'],
     ('Hanging runs on tea and pencil marks.', 'Morag Fairlie, twenty minutes in')),
    ('Why the floor is always bare', '2026-08-02', 'hero.jpg', 'People ask where the rug went. It went to my sister in Bergen in 2019.',
     ['I meant to buy another one. Then the light came in across the bare boards one August morning and it turned out to be the whole subject.',
      'Boards take light like water: every gap, every knot, every place where someone dragged a chair. A rug would hide all of it. I will paint a rug when I own one again.'], None),
    ('A new batch of linen', '2026-05-30', 'j-canvas.jpg', 'Twelve metres of Belgian linen arrived on Tuesday, which is about eighteen paintings.',
     ['I size it with rabbit-skin glue, two thin coats, then prime it with an oil ground. It takes three weeks to cure before I can paint on it, so the next paintings start in late June.',
      'The back of a finished canvas is as good a record as any: the stretcher keys, the date in pencil, the gallery label. I photograph every one before it leaves.'], None),
    ('The paint box', '2026-04-11', 'j-palette.jpg', 'I paint outside with a box my grandfather used, and the palette has not been cleaned since 2009.',
     ['It holds six colours and a small panel in the lid. That limit is the point: outside, I have twenty minutes before the light moves, and six colours is all I can think about.',
      'The small panels are for me. A few go to the open studio in November, unframed, from £250.'], None),
    ('Cleaning brushes', '2026-02-20', 'j-brushes.jpg', 'Every Friday I clean every brush, whether I used it or not.',
     ['Safflower oil first, then soap, then shaped with my fingers and left upright in the jar to dry. A good hog brush lasts two years this way.',
      'It is also the hour where I decide what I am painting next week, which is why Friday is not a visiting day.'], None),
    ('A walk up Leith Walk', '2026-01-09', 'j-leith.jpg', 'In January I draw outside instead of painting, because the light in the flat is gone by three.',
     ['This week: the corner buildings up Leith Walk, white render and stone. Low sun makes them look like stage sets.',
      'Two drawings from these walks are in the catalogue now. The rest stay in the sketchbook.'], ('Drawing in January is a way of waiting.', '')),
    ('Studio visits start again', '2025-11-14', 'j-easel.jpg', 'From next Thursday the studio is open again for visits, by appointment.',
     ['The stairs have not got shorter. There are four flights and no lift, and a chair on every landing.',
      'If you are coming to see a particular painting, tell me when you book, so it is on the easel and not in the rack.'], None),
]
for t, d, img, lead, paras, q in JPOSTS:
    body = [para(lead, fontSize='large'), para(paras[0]), image(img, 'Studio photo for the note: ' + t.lower(), lightbox=True)]
    if q:
        body.append(quote(q[0], q[1]) if q[1] else pullquote(q[0]))
    body += [para(x) for x in paras[1:]]
    posts.append({'title': t, 'category': 'journal', 'image': img, 'date': d, 'excerpt': lead, 'content': J(*body)})
demo = {
    'site': {'title': 'Agnes Brekke', 'tagline': 'Paintings from a top-floor studio in Leith'},
    'categories': [{'slug': 'paintings', 'name': 'Paintings', 'description': 'Oil on linen, canvas and panel.'},
                   {'slug': 'drawings', 'name': 'Drawings', 'description': 'Pencil and charcoal, mostly drawn standing up outside.'},
                   {'slug': 'monotypes', 'name': 'Monotypes', 'description': 'One-off prints pulled from a painted plate on the etching press at Edinburgh Printmakers.'},
                   {'slug': 'journal', 'name': 'Journal', 'description': 'Notes from the studio.'}],
    'front_page': 'home', 'posts_page': 'work',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'work', 'title': 'Work', 'content': ''},
        {'slug': 'exhibitions', 'title': 'Exhibitions', 'pattern': 'oil/exhibitions-page', 'template': 'page-wide'},
        {'slug': 'journal', 'title': 'Journal', 'pattern': 'oil/journal-page-layout', 'template': 'page-wide'},
        {'slug': 'buying', 'title': 'Buying a painting', 'pattern': 'oil/buying-page', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About', 'pattern': 'oil/about-page', 'template': 'page-wide'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'oil/contact-page', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Work', 'url': '/work/'}, {'label': 'Exhibitions', 'url': '/exhibitions/'}, {'label': 'Journal', 'url': '/journal/'},
            {'label': 'Buying', 'url': '/buying/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/oil', exist_ok=True)
with open('demos/oil/content.json', 'w', encoding='utf-8') as f:
    json.dump(demo, f, indent=1, ensure_ascii=False)
write('functions.php', """<?php
/**
 * Oil: pattern categories only.
 *
 * @package oil
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
print('oil built')
