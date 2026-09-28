# Design note (spine, idea 051: novelist / author)
# Direction: "the whole site is a paperback". Owner's brief: Penguin aesthetics. The page is built on the classic horizontal three-band grid:
# a colour band (header), a white panel (content), a colour band (footer), and the band colour follows the genre: orange fiction, green crime,
# dark blue memoir, cerise travel. Book pages switch to their genre's colour through template parts, no custom code.
# Fonts: Cabin (humanist sans in the Johnston and Gill lineage, the registry face for 051) for titles and labels; Literata for reading.
# Layout idea: flat typographic covers (band, panel, band) on a strict shelf, and book pages that use the later photo-cover grid:
# a genre band with the title over a duotone photograph. No logo, no penguin, no trade dress beyond the grid and the colour code.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('spine')
import blocks as _b
def group(inner, tag='div', layout='constrained', **attrs):
    # WordPress drops the layout of a <div> group that has align + padding when it re-serialises; <section> keeps it.
    if tag == 'div' and 'padding' in json.dumps(attrs.get('style', {})):
        tag = 'section'
    return _b.group(inner, tag=tag, layout=layout, **attrs)
D = THEME['dir']
import re as _re
def split_css(css):
    """Block and section 'css' only scopes the first selector of a comma list, so write one rule per selector."""
    out = []
    for sel, body in _re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        parts = [p.strip() for p in _re.split(r',(?![^()]*\))', sel)]
        out += ['%s{%s}' % (p, body) for p in parts if p]
    return ''.join(out)


GENRES = {'fiction': ('accent', 'Fiction', 'on-accent'), 'crime': ('accent-2', 'Crime', 'base'),
          'memoir': ('memoir', 'Memoir', 'base'), 'travel': ('travel', 'Travel', 'base')}
PALETTE = [
    ('base', '#FFFFFF', 'Page'), ('contrast', '#1C1C1C', 'Ink'), ('accent', '#EA6A1E', 'Fiction orange'),
    ('accent-2', '#0B7446', 'Crime green'), ('memoir', '#1E3C78', 'Memoir blue'), ('travel', '#BE1A58', 'Travel cerise'),
    ('surface', '#F3F0E8', 'Cover panel'), ('line', '#1C1C1C', 'Rule'), ('muted', '#595753', 'Grey'), ('on-accent', '#1C1C1C', 'Text on orange'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
disp = next(f for f in fonts if f['slug'] == 'display')
body = next(f for f in fonts if f['slug'] == 'body')

def pal(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d

focus = {'outline': {'color': 'var:preset|color|contrast', 'offset': '3px', 'style': 'solid', 'width': '3px'}}
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '680px', 'wideSize': '1240px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE),
                  'duotone': [{'slug': 'crime', 'colors': ['#07301F', '#F3F0E8'], 'name': 'Crime green'},
                              {'slug': 'fiction', 'colors': ['#3A1A06', '#F6E3D2'], 'name': 'Fiction orange'},
                              {'slug': 'memoir', 'colors': ['#0E1C3A', '#E8ECF4'], 'name': 'Memoir blue'},
                              {'slug': 'travel', 'colors': ['#3D0A1E', '#F6E4EC'], 'name': 'Travel cerise'},
                              {'slug': 'ink', 'colors': ['#1C1C1C', '#F3F0E8'], 'name': 'Ink'}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': [disp, body],
            'fontSizes': [fs('x-small', '0.875rem', 'Caption'), fs('small', '1rem', 'Small'), fs('medium', '1.1875rem', 'Body'),
                          fs('large', '1.5rem', 'Large', '1.25rem'), fs('x-large', '2.25rem', 'Section', '1.75rem'),
                          fs('xx-large', '4rem', 'Title', '2.5rem'), fs('display', '6.5rem', 'Cover', '3rem')],
        },
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 7rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.62'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|accent-2'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '1.05', 'letterSpacing': '0'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}},
            'button': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                       'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                       'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.7em', 'bottom': '0.7em', 'left': '1.4em', 'right': '1.4em'}},
                       ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|contrast'}, 'border': {'color': 'var:preset|color|accent'}},
                       ':focus': focus},
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'currentColor'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/heading': {'elements': {'link': {'color': {'text': 'currentColor'}, 'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'currentColor'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'}},
            'core/image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.4', 'fontStyle': 'italic'},
                           'border': {'width': '0'}, 'spacing': {'padding': {'left': '0'}},
                           'css': '& cite{font-family:var(--wp--preset--font-family--display);font-style:normal;font-size:var(--wp--preset--font-size--small)}'},
            'core/details': {'border': {'top': {'color': 'var:preset|color|line', 'width': '2px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-weight:700;cursor:pointer}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table.has-fixed-layout{table-layout:auto}& table th{text-align:left;font-family:var(--wp--preset--font-family--display);font-weight:700}& table td,& table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.6em 1em .6em 0;vertical-align:top}& table thead{border:0;border-bottom:2px solid var(--wp--preset--color--line)}'},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small'}},
        },
        'css': ('.wp-block-column>.wp-block-group:only-child{height:100%}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                'body{font-synthesis:none;font-variant-numeric:lining-nums tabular-nums}'
                'a{text-decoration-color:var(--wp--preset--color--accent);text-decoration-thickness:2px;text-underline-offset:.2em}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--contrast);outline-offset:3px}'
                ':where(.wp-block-post-content)>:where(h2,h3){margin-top:var(--wp--preset--spacing--60)}'),
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header (fiction orange)'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer (fiction orange)'}]
                     + [{'area': 'header', 'name': 'header-%s' % g, 'title': 'Header (%s)' % g} for g in ('crime', 'memoir', 'travel')]
                     + [{'area': 'footer', 'name': 'footer-%s' % g, 'title': 'Footer (%s)' % g} for g in ('crime', 'memoir', 'travel')],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}]
                       + [{'name': 'single-book-%s' % g, 'title': 'Book: %s' % GENRES[g][1].lower(), 'postTypes': ['post']} for g in GENRES],
}
_t = theme['styles']['blocks'].get('core/table', {}).pop('css', None)
if _t:
    # Block-level css loses to core's table borders, so the table rules go in the global stylesheet.
    theme['styles']['css'] += _t.replace('& ', '.wp-block-table ').replace('&.', '.wp-block-table.')
for _b_ in theme['styles']['blocks'].values():
    if 'css' in _b_:
        _b_['css'] = split_css(_b_['css'])
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

def variation(title, p):
    return json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(p)}}}, indent='\t', ensure_ascii=False)

write('styles/hardback.json', variation('Hardback', [
    ('base', '#DCD8CF', 'Page'), ('contrast', '#1F1D1A', 'Ink'), ('accent', '#86611F', 'Fiction orange'),
    ('accent-2', '#20513A', 'Crime green'), ('memoir', '#23385F', 'Memoir blue'), ('travel', '#7E2342', 'Travel cerise'),
    ('surface', '#EEEAE1', 'Cover panel'), ('line', '#1F1D1A', 'Rule'), ('muted', '#4F4B44', 'Grey'), ('on-accent', '#FFFFFF', 'Text on orange')]))
write('styles/pulp.json', variation('Pulp', [
    ('base', '#F8E45C', 'Page'), ('contrast', '#1A1A1A', 'Ink'), ('accent', '#C8321E', 'Fiction orange'),
    ('accent-2', '#1A1A1A', 'Crime green'), ('memoir', '#1D3A73', 'Memoir blue'), ('travel', '#A4124A', 'Travel cerise'),
    ('surface', '#FFF6C4', 'Cover panel'), ('line', '#1A1A1A', 'Rule'), ('muted', '#4A4418', 'Grey'), ('on-accent', '#FFFFFF', 'Text on orange')]))
write('styles/crime-night.json', variation('Crime at night', [
    ('base', '#121412', 'Page'), ('contrast', '#F0EEE8', 'Ink'), ('accent', '#F08A3E', 'Fiction orange'),
    ('accent-2', '#2FA46B', 'Crime green'), ('memoir', '#5C84D6', 'Memoir blue'), ('travel', '#E4538A', 'Travel cerise'),
    ('surface', '#1E211E', 'Cover panel'), ('line', '#F0EEE8', 'Rule'), ('muted', '#B4B1A8', 'Grey'), ('on-accent', '#121412', 'Text on orange')]))

def section(slug, title, types, styles):
    if 'css' in styles:
        styles = dict(styles, css=split_css(styles['css']))
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                                        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))

for g, (col, name, txt) in GENRES.items():
    section('band-' + g, 'Band: %s' % name.lower(), ['core/group', 'core/column', 'core/columns'],
            {'color': {'background': 'var:preset|color|' + col, 'text': 'var:preset|color|' + txt},
             'elements': {'link': {'color': {'text': 'currentColor'}}, 'heading': {'color': {'text': 'currentColor'}},
                          'button': {'color': {'background': 'var:preset|color|' + txt, 'text': 'var:preset|color|' + col}, 'border': {'color': 'var:preset|color|' + txt}}},
             'css': '& a{text-decoration-color:currentColor}'})
section('paperback', 'Paperback cover', ['core/group'],
        {'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|line'},
         'css': '&{aspect-ratio:2/3;gap:0!important;overflow:hidden}& > *{margin:0!important}& > :first-child,& > :last-child{flex:1 1 0;display:flex;align-items:center;justify-content:center;padding:.75rem}& > :nth-child(2){flex:1.25 1 0;display:flex;flex-direction:column;justify-content:center;padding:1rem;text-align:center}'})
section('cover-panel', 'Cover panel', ['core/group'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
         'css': '& h3,& h2,& p{text-align:center}& .wp-block-separator{width:40%;margin:.6rem auto!important;border-top-width:1px}'})
section('retailers', 'Retailer list (ruled)', ['core/list'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|medium'},
         'css': '&{list-style:none;padding-left:0!important;border-top:2px solid var(--wp--preset--color--line)}& li{padding:.7rem 0;border-bottom:1px solid var(--wp--preset--color--line)}& li:first-child{font-weight:700}& li a{text-decoration-thickness:2px}'})
section('colophon', 'Colophon line', ['core/paragraph'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small'}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'],
        {'border': {'top': {'color': 'var:preset|color|line', 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})
section('chips', 'Chips', ['core/list'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding:0!important;display:flex;flex-wrap:wrap;gap:.5rem}& li{padding:.3rem .8rem;border:2px solid var(--wp--preset--color--line);border-radius:999px}& li:nth-child(4n+1){background:var(--wp--preset--color--accent);color:var(--wp--preset--color--on-accent);border-color:transparent}& li:nth-child(4n+3){background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--base);border-color:transparent}'})
section('shelf', 'Shelf', ['core/group'],
        {'css': '&{row-gap:var(--wp--preset--spacing--50)!important}'})

# ---------------------------------------------------------------- books
BOOKS = [  # slug, title, genre, year, publisher line, image, blurb, isbn
    ('the-wash-in-winter', 'The Wash in Winter', 'crime', '2026', 'wash.jpg', 'The third Fenland novel. A body in a pumping station, three days before the sluice gates are opened.', '978-1-9160-4412-8'),
    ('my-fathers-boats', 'My Father’s Boats', 'memoir', '2023', 'boats.jpg', 'A memoir of a fisherman’s daughter, told through the seven boats her father owned and lost.', '978-1-9160-4409-8'),
    ('harbour-lights', 'Harbour Lights', 'fiction', '2022', 'harbour.jpg', 'Two sisters, one pub on the quay, and the summer the harbour was sold.', '978-1-9160-4406-7'),
    ('a-drowned-parish', 'A Drowned Parish', 'crime', '2020', 'parish.jpg', 'The second Fenland novel. A church reappears in a drought, and so does a missing girl’s bicycle.', '978-1-9160-4403-6'),
    ('seven-trams-in-lisbon', 'Seven Trams in Lisbon', 'travel', '2019', 'lisbon.jpg', 'Essays from a winter spent riding every tram line in Lisbon with a notebook and bad Portuguese.', '978-1-9160-4401-2'),
    ('low-country', 'Low Country', 'crime', '2018', 'fens.jpg', 'The first Fenland novel. DS Ruth Ambler comes home to Wisbech and a case her father never closed.', '978-1-9160-4398-5'),
    ('the-salt-road', 'The Salt Road', 'fiction', '2016', 'saltroad.jpg', 'A debut about a salt marsh, a family farm and the year the sea wall failed.', '978-1-9160-4395-4'),
]
ORDER = list(reversed(BOOKS))

def paperback(slug, title, genre, series='', size='medium'):
    col, name, _ = GENRES[genre]
    return group(J(
        group(para(name + (', ' + series if series else ''), fontFamily='display', fontSize='small', style={'typography': {'fontWeight': '600'}}), className='is-style-band-' + genre, layout={'type': 'default'}),
        group(J(heading('<a href="/%s/">%s</a>' % (slug, title), 3, fontSize=size), separator(), para('Tamsin Rourke', fontFamily='display', fontSize='small')), className='is-style-cover-panel', layout={'type': 'default'}),
        group(para('Harrow &amp; Lane', fontFamily='display', fontSize='x-small'), className='is-style-band-' + genre, layout={'type': 'default'})),
        className='is-style-paperback', layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'stretch'})

SERIES = {'low-country': 'Fenland 1', 'a-drowned-parish': 'Fenland 2', 'the-wash-in-winter': 'Fenland 3'}

# ---------------------------------------------------------------- round 2: patterns, collage and play
import urllib.parse as _up
def _svg(body, w=24, h=24):
    return "url(\"data:image/svg+xml," + _up.quote('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s</svg>' % (w, h, w, h, body), safe=' =:/"') + "\")"
MOTIFS = {
    'waves': (_svg('<path d="M0 12 Q6 5 12 12 T24 12" fill="none" stroke="black" stroke-width="2.4"/>'), '24px 14px', 'Fen water'),
    'dots': (_svg('<circle cx="6" cy="6" r="3.2"/><circle cx="18" cy="18" r="3.2"/>'), '22px 22px', 'Half-drop dots'),
    'scales': (_svg('<path d="M0 12 A12 12 0 0 1 24 12 M-12 24 A12 12 0 0 1 12 24 M12 24 A12 12 0 0 1 36 24" fill="none" stroke="black" stroke-width="2"/>', 24, 24), '26px 26px', 'Boat scales'),
    'tiles': (_svg('<path d="M12 2 L22 12 L12 22 L2 12Z" fill="none" stroke="black" stroke-width="2"/><circle cx="12" cy="12" r="2.6"/>'), '26px 26px', 'Lisbon tiles'),
    'reeds': (_svg('<path d="M12 23 C11 15 8 9 12 1 C16 9 13 15 12 23Z"/><path d="M0 23 C0 18 -2 14 0 9 C2 14 0 18 0 23Z M24 23 C24 18 22 14 24 9 C26 14 24 18 24 23Z"/>'), '18px 24px', 'Reeds'),
    'stripes': (_svg('<path d="M-2 26 L26 -2 M-14 14 L14 -14 M10 38 L38 10" stroke="black" stroke-width="3"/>'), '16px 16px', 'Diagonal stripes'),
}
GENRE_MOTIF = {'crime': 'waves', 'fiction': 'dots', 'memoir': 'scales', 'travel': 'tiles'}
for k, (url, size, title) in MOTIFS.items():
    section('pattern-' + k, 'Pattern: %s' % title.lower(), ['core/group', 'core/column', 'core/cover'],
            {'css': '&{position:relative;isolation:isolate}&::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;background-color:currentColor;opacity:.3;'
                    '-webkit-mask:%s 0 0/%s repeat;mask:%s 0 0/%s repeat}' % (url, size, url, size)})
section('label-plate', 'Label plate', ['core/group'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
         'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
         'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
         'css': '&{text-align:center;width:78%;margin-inline:auto!important}& h2,& h3,& p{text-align:center}& .wp-block-separator{width:40%;margin:.5rem auto!important;border-top-width:1px}'})
section('clothbound', 'Clothbound cover', ['core/group'],
        {'css': '&{aspect-ratio:2/3;display:flex!important;flex-direction:column;justify-content:center;overflow:hidden}'})
section('collage', 'Collage shapes', ['core/group', 'core/columns'],
        {'css': '&{position:relative;isolation:isolate}&::before{content:"";position:absolute;z-index:-1;width:min(34vw,420px);aspect-ratio:1;border-radius:50%;background:var(--wp--preset--color--travel);top:-2rem;left:-3rem;opacity:.9}'
                '&::after{content:"";position:absolute;z-index:-1;width:min(26vw,300px);aspect-ratio:1;background:var(--wp--preset--color--accent);clip-path:polygon(0 0,100% 30%,70% 100%);bottom:-2.5rem;left:24%;opacity:.95}'})
section('tile', 'Patchwork tile', ['core/group'],
        {'css': '&{min-height:12rem;display:flex!important;flex-direction:column;justify-content:flex-end}& a{text-decoration:none}& a:hover{text-decoration:underline}'})
section('tilt-left', 'Tilted left', ['core/group'], {'css': '&{transform:rotate(-2deg)}'})
section('tilt-right', 'Tilted right', ['core/group'], {'css': '&{transform:rotate(1.6deg)}'})

def clothbound(slug, title, genre, series='', size='large'):
    return group(group(J(para(GENRES[genre][1] + (', ' + series if series else ''), fontFamily='display', fontSize='x-small', style={'typography': {'fontWeight': '600'}}),
                         heading('<a href="/%s/">%s</a>' % (slug, title), 3, fontSize=size), separator(), para('Tamsin Rourke', fontFamily='display', fontSize='small')),
                       className='is-style-label-plate', layout={'type': 'default'}),
                 className='is-style-band-%s is-style-pattern-%s is-style-clothbound' % (genre, GENRE_MOTIF[genre]), layout={'type': 'default'})

pattern('clothbound-cover', 'Patterned cover (clothbound style)', 'featured,gallery', clothbound('the-wash-in-winter', 'The Wash in Winter', 'crime', 'Fenland 3', 'x-large'),
        description='A cover with a repeating motif and a label plate. The motif follows the genre: waves for crime, dots for fiction, scales for memoir, tiles for travel.')

pattern('collage-hero', 'New book, collage opener', 'featured', group(columns(
    ('42%', group(clothbound('the-wash-in-winter', 'The Wash in Winter', 'crime', 'Fenland 3', 'x-large'), className='is-style-tilt-left', layout={'type': 'default'})),
    ('58%', J(para('New in hardback, 8 October 2026', fontFamily='display', style={'typography': {'fontWeight': '600'}}),
              heading('The Wash in Winter', 1, fontSize='display'),
              para('A man is found in the Hundred Foot pumping station three days before the sluice gates are opened for the winter. DS Ruth Ambler knew him at school. So did half of Wisbech. The third Fenland novel.', fontSize='large'),
              buttons(('Buy the book', '/buy/'), ('Read the first page', '/book-groups/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|70'}}}),
    align='wide', className='is-style-collage', layout={'type': 'default'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}),
    description='The new book, tilted like a cover on a table, over cut-paper shapes in the genre colours.')

def tile(genre, motif, label, sub, href):
    return group(J(para('<a href="%s">%s</a>' % (href, label), fontFamily='display', fontSize='x-large', style={'typography': {'fontWeight': '700', 'lineHeight': '1'}}), para(sub, fontSize='small')),
                 className='is-style-band-%s is-style-pattern-%s is-style-tile' % (genre, motif), layout={'type': 'default'},
                 style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})

pattern('series-patchwork', 'Series patchwork (colour-coded)', 'featured', group(J(
    heading('Pick a shelf', 2),
    grid(J(tile('crime', 'waves', 'Fenland crime', 'Three novels with DS Ruth Ambler. Read in order.', '/category/crime/'),
           tile('fiction', 'dots', 'Fiction', 'Two stand-alone novels about the coast.', '/category/fiction/'),
           tile('memoir', 'scales', 'Memoir', 'My father and the seven boats he lost.', '/category/memoir/'),
           tile('travel', 'tiles', 'Travel', 'A winter of Lisbon trams.', '/category/travel/'),
           tile('crime', 'reeds', 'Book groups', 'Questions, maps and a video visit.', '/book-groups/'),
           tile('fiction', 'stripes', 'Events', 'Launch in King’s Lynn on 8 October.', '/events/')), min_width='15rem')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}),
    description='A patchwork of colour-coded tiles, one per shelf, each with its own motif.')

for k in ('waves', 'dots', 'scales', 'tiles'):
    g = {v: kk for kk, v in GENRE_MOTIF.items()}[k]
    pattern('band-' + k, 'Pattern band: %s' % MOTIFS[k][2].lower(), 'design', group(para('&nbsp;', fontSize='x-small'), align='full', className='is-style-band-%s is-style-pattern-%s' % (g, k),
                                                                              style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0', 'bottom': '0'}}}),
            description='A full-width band of %s, for breaks between sections.' % MOTIFS[k][2].lower())

pattern('great-ideas-quote', 'A line from the book, on a pattern', 'testimonials', group(group(J(
    para('“The Fens keep everything and forgive nothing.”', fontFamily='display', fontSize='x-large', style={'typography': {'fontWeight': '700', 'lineHeight': '1.15'}}),
    para('The Wash in Winter, page 41', fontSize='small')), className='is-style-label-plate', layout={'type': 'default'}),
    className='is-style-band-memoir is-style-pattern-reeds', align='wide', layout={'type': 'default'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))

pattern('reading-order', 'The Fenland novels, in order', 'featured', group(J(
    heading('The Fenland novels, in order', 2),
    grid(J(clothbound('low-country', 'Low Country', 'crime', 'Fenland 1', 'medium'), clothbound('a-drowned-parish', 'A Drowned Parish', 'crime', 'Fenland 2', 'medium'),
           clothbound('the-wash-in-winter', 'The Wash in Winter', 'crime', 'Fenland 3', 'medium')), min_width='10rem'),
    para('Each one works alone, but Ruth’s father’s case runs through all three and is only closed in the last one.', fontSize='small')),
    align='wide', layout={'type': 'default'}))

pattern('events-rows', 'Events (ruled rows)', 'text', J(
    heading('Events', 2),
    *[group(columns(('30%', para(d, fontFamily='display', style={'typography': {'fontWeight': '700'}})), ('70%', para(t)), isStackedOnMobile=False,
                    style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}}}), className='is-style-rule-top', layout={'type': 'default'})
      for d, t in [('Thu 8 Oct', 'Launch of The Wash in Winter, Old Custom House Books, King’s Lynn. Free, <a href="https://example.com/tickets">book a place</a>.'),
                   ('Sat 17 Oct', 'In conversation with Martin Hale, Norwich Arts Centre. <a href="https://example.com/tickets">£10</a>.'),
                   ('Wed 4 Nov', 'Fenland crime evening, Wisbech Library. Free, no booking.'),
                   ('Sun 15 Nov', 'Signing at Riverside Books, Ely, 11am to 1pm.')]],
    para('I can’t do school visits this year, sorry.', fontSize='small')))

pattern('audiobook-sample', 'Audiobook sample', 'media,audio', J(
    heading('Hear the first chapter', 3),
    audio('https://upload.wikimedia.org/wikipedia/commons/a/a7/Trialofsusanbanthony_18_anonymous_128kb.ogg', 'Stand-in audio: a CC0 LibriVox reading from Wikimedia Commons. Replace with your audiobook sample.'),
    para('The full audiobook is read by Joanne Pell, 11 hours 40 minutes, from Libro.fm and every other audiobook shop.', fontSize='small')))

pattern('places', 'Where the books happen', 'gallery,media', J(
    heading('Where the books happen', 2),
    gallery([('fens.jpg', 'A painting of drainage windmills on flat fenland under a stormy sky', 'Low Country: the drains'),
             ('saltroad.jpg', 'A tidal creek winding across a salt marsh at low water', 'The Salt Road: Stiffkey marsh'),
             ('harbour.jpg', 'A floodlit harbour fort reflected in black water at night', 'Harbour Lights: the quay at night'),
             ('lisbon.jpg', 'A yellow tram turning a corner beside scaffolded buildings in Lisbon', 'Seven Trams in Lisbon: the 28')], columns=4, align='wide'),
    para('Photographs from Wikimedia Commons, public domain or CC0. Click one to see it large.', fontSize='x-small', textColor='muted')))

pattern('author-note', 'A note from the author', 'about', group(group(J(
    heading('A note on the covers', 3),
    para('I asked for covers that look like the books I bought second-hand as a teenager: a colour for the shelf, a pattern you could pick out across a room, the title on a plate. Crime is green with water, because everything in the Fens comes back to the drains. Fiction is orange and dotted. My dad’s book has fish scales.'),
    para('Tamsin', fontFamily='display', style={'typography': {'fontWeight': '700'}})), className='is-style-label-plate', layout={'type': 'default'}),
    className='is-style-band-fiction is-style-pattern-dots', align='wide', layout={'type': 'default'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}))

pattern('translations', 'Translations (chips)', 'text', J(
    heading('In other languages', 3),
    lst(['Dutch, Uitgeverij Kade', 'German, Nordlicht Verlag', 'Danish, Forlaget Hav', 'Polish, Wydawnictwo Mokradła', 'Italian, Edizioni Laguna',
         'Czech, Nakladatelství Rákos', 'Swedish, Bokförlaget Kärr', 'French, Éditions Marais', 'Portuguese, Elétrico Editora'], className='is-style-chips')))

pattern('short-stories', 'Short stories and essays', 'text', J(
    heading('Short pieces', 3),
    lst(['“The Sluice Keeper”, a short story, Fenland Quarterly, spring 2025. <a href="/newsletter/">Sent to newsletter readers</a>.',
         '“My Father’s Radio”, an essay, The Northern Review, 2023.',
         '“Night Bus to Hessle”, a story written for a charity anthology, 2021.'])))

pattern('prizes', 'Prizes and shortlists', 'text', J(
    heading('Prizes', 3),
    lst(['Low Country: shortlisted, East Anglian Crime Writing Prize, 2019.', 'My Father’s Boats: longlisted, Norfolk Nonfiction Award, 2024.', 'The Salt Road: winner, Lynn Literary Festival debut prize, 2016.'])))

pattern('book-group-faq', 'Questions from book groups', 'text', J(
    heading('Questions groups ask', 3),
    details('Will you join our meeting?', para('By video, for 30 minutes, about twice a month. Email my publicist with two dates.')),
    details('Is Wisbech really like that?', para('Partly. The pumping station is real. The murders are not.')),
    details('Can we have more copies at a discount?', para('Old Custom House Books does 10% off for groups ordering six or more.'))))

def buy_list(title, signed=True):
    items = []
    if signed:
        items.append('<a href="https://example.com/old-custom-house-books">Old Custom House Books, King’s Lynn</a>: signed and dedicated copies, posted anywhere in the UK')
    items += ['<a href="https://uk.bookshop.org/">Bookshop.org</a>: pays a share to an independent shop you choose',
              '<a href="https://www.waterstones.com/">Waterstones</a>', '<a href="https://www.amazon.co.uk/">Amazon</a>',
              '<a href="https://books.apple.com/">Apple Books</a> (ebook)', '<a href="https://www.kobo.com/">Kobo</a> (ebook)',
              '<a href="https://libro.fm/">Libro.fm</a> (audiobook, read by Joanne Pell)']
    return lst(items, className='is-style-retailers')

# ---------------------------------------------------------------- patterns
pattern('new-book-hero', 'New book with cover and one buy button', 'featured', columns(
    ('36%', paperback('the-wash-in-winter', 'The Wash in Winter', 'crime', 'Fenland 3', size='x-large')),
    ('64%', J(para('New in hardback, 8 October 2026', fontFamily='display', style={'typography': {'fontWeight': '600'}}),
              heading('The Wash in Winter', 1, fontSize='display'),
              para('A man is found in the Hundred Foot pumping station three days before the sluice gates are opened for the winter. DS Ruth Ambler knew him at school. So did half of Wisbech. The third Fenland novel, and the one that finally explains what happened to her father.', fontSize='large'),
              buttons(('Buy the book', '/buy/')),
              quote('Rourke writes the Fens like other people write the sea: flat, cold and full of things that don’t stay buried.', 'Hannah Okoro, Fenland Quarterly, August 2026'))),
    align='wide', verticalAlignment='center', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'blockGap': {'left': 'var:preset|spacing|70'}}}),
    description='The new book, as a flat paperback cover, with exactly one action.')

pattern('shelf', 'Books in order (shelf of covers)', 'featured,gallery', group(J(
    row(J(heading('Books, in the order they came out', 2), para('<a href="/books/">Which one to read first</a>', fontSize='small')), justify='space-between'),
    grid(J(*[(clothbound(s, t, g, SERIES.get(s, ''), 'medium') if i % 2 else paperback(s, t, g, SERIES.get(s, ''))) for i, (s, t, g, *_) in enumerate(ORDER)]), min_width='9.5rem', className='is-style-shelf')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}),
    description='A strict shelf of flat covers. Colour tells the genre: orange fiction, green crime, blue memoir, cerise travel.')

pattern('buy-block', 'Buy block (independent shops first)', 'call-to-action', J(
    heading('Buy The Wash in Winter', 2),
    para('Hardback, £18.99. Ebook and audiobook on the same day. If you can, buy from an independent shop: it is where my first readers came from.'),
    buy_list('The Wash in Winter'),
    para('Signed copies: Old Custom House Books on Purfleet Quay will post a signed and dedicated copy anywhere in the UK for £3.20. Tell them who it’s for in the order notes.', fontSize='small')),
    description='The signature: the local bookshop and Bookshop.org come first, then the big retailers.')

pattern('editions', 'International editions and translations', 'text', J(
    heading('Editions', 3),
    table([['UK and Ireland', 'Harrow &amp; Lane', 'Hardback, ebook, audio', '8 Oct 2026'],
           ['USA and Canada', 'Northgate Press', 'Hardback, ebook', '3 Feb 2027'],
           ['Australia and New Zealand', 'Harrow &amp; Lane ANZ', 'Trade paperback', '5 Nov 2026'],
           ['Netherlands', 'Uitgeverij Kade (tr. Anne Visser)', 'Paperback', 'Spring 2027'],
           ['Germany', 'Nordlicht Verlag (tr. Jonas Feld)', 'Paperback', 'Autumn 2027']],
          head=['Where', 'Publisher', 'Formats', 'Out'])))

pattern('books-in-order', 'Books in order (list for readers who ask)', 'text', J(
    heading('Where to start', 2),
    para('The three Fenland novels are a series and work best in order. Everything else stands alone.'),
    table([['2016', '<a href="/the-salt-road/">The Salt Road</a>', 'Fiction', 'Stand-alone. My first book.'],
           ['2018', '<a href="/low-country/">Low Country</a>', 'Crime', 'Fenland 1. Start here for the series.'],
           ['2019', '<a href="/seven-trams-in-lisbon/">Seven Trams in Lisbon</a>', 'Travel', 'Essays.'],
           ['2020', '<a href="/a-drowned-parish/">A Drowned Parish</a>', 'Crime', 'Fenland 2.'],
           ['2022', '<a href="/harbour-lights/">Harbour Lights</a>', 'Fiction', 'Stand-alone.'],
           ['2023', '<a href="/my-fathers-boats/">My Father’s Boats</a>', 'Memoir', 'About my dad. Read it whenever.'],
           ['2026', '<a href="/the-wash-in-winter/">The Wash in Winter</a>', 'Crime', 'Fenland 3.']],
          head=['Year', 'Title', 'Shelf', 'Notes'])))

pattern('praise', 'Praise quotes with sources', 'testimonials', columns(
    (None, quote('The best sense of place in British crime writing since the early Ruth Rendell.', 'Hannah Okoro, Fenland Quarterly, on Low Country, 2018')),
    (None, quote('I read it in one sitting on a train and missed my stop at Ely.', 'Nadia Karim, bookseller, Riverside Books, Ely')),
    (None, quote('Quietly furious and very funny about money.', 'The Northern Review, on Harbour Lights, 2022')), align='wide'))

pattern('excerpt', 'Read an excerpt', 'text', J(
    heading('Read the first page', 3),
    details('Chapter one, The Wash in Winter', J(
        para('The pumps at Hundred Foot start at six, whether anyone is there or not. Dennis Cole had told Ruth that when they were eleven, standing on the bank in their school coats, as if it were a secret the Fens had trusted him with.'),
        para('Thirty years later he was in the intake channel, face down, and the pumps had started at six regardless.'),
        para('“You knew him,” said Okafor. It was not a question. In Wisbech it rarely was.'))),
    para('Copyright Tamsin Rourke 2026. Reproduced with permission from Harrow &amp; Lane.', fontSize='x-small', textColor='muted')))

pattern('book-group-guide', 'Book-group guide with questions', 'text', J(
    heading('For book groups', 2),
    para('A guide to <em>The Wash in Winter</em> for reading groups: ten questions, a map of the places in the book and a note from me about the parts I found hardest to write. It contains spoilers from page 180 on.'),
    lst(['Ruth says the Fens “keep everything and forgive nothing”. Is that true of the people in the book as well as the land?',
         'Why do you think Dennis never left Wisbech when everyone else did?',
         'The sluice gates open on the last page. What changes, and for whom?',
         'Did you guess who wrote the letters? When?',
         'Okafor is the only character who isn’t from the Fens. What does he see that Ruth can’t?'], ordered=True),
    buttons(('Download the guide (PDF, 6 pages)', '/book-groups/')),
    para('If your group would like me to join by video for 30 minutes, email my publicist. I do about two a month and I don’t charge.', fontSize='small')))

pattern('events', 'Events list', 'text', J(
    heading('Events', 2),
    table([['Thu 8 Oct 2026', 'Launch of The Wash in Winter', 'Old Custom House Books, King’s Lynn', '<a href="https://example.com/tickets">Free, book a place</a>'],
           ['Sat 17 Oct 2026', 'In conversation with Martin Hale', 'Norwich Arts Centre', '<a href="https://example.com/tickets">£10</a>'],
           ['Wed 4 Nov 2026', 'Fenland crime evening', 'Wisbech Library', 'Free, no booking'],
           ['Sun 15 Nov 2026', 'Signing', 'Riverside Books, Ely', '11am to 1pm']],
          head=['When', 'What', 'Where', 'Tickets']),
    para('Past events are in the <a href="/newsletter/">newsletter archive</a>. I can’t do school visits this year, sorry.', fontSize='small')))

pattern('newsletter-signup', 'Newsletter sign-up with past issues', 'call-to-action', group(J(
    heading('A letter every six weeks or so', 2),
    para('What I’m writing, what I’m reading, one photograph of the Wash and the dates of events before anyone else gets them. About 800 words. You can read the old ones before you sign up.'),
    buttons(('Sign up by email', 'mailto:letters@tamsinrourke.example?subject=Newsletter')),
    heading('Recent letters', 4),
    lst(['<a href="/newsletter/">September 2026: proofs, a heron and the launch date</a>', '<a href="/newsletter/">July 2026: why the third book took three years</a>',
         '<a href="/newsletter/">May 2026: the cover, and the argument about the cover</a>'])),
    className='is-style-band-fiction', style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}}))

pattern('contacts', 'Contacts by role (agent, publicist, rights)', 'contact', columns(
    (None, J(heading('Literary agent', 4), para('Priya Chaudhry, Lantern Street Agency. For publishing, translation and permissions.', fontSize='small'), para('<a href="mailto:priya@lanternstreet.example">priya@lanternstreet.example</a>', fontSize='small'))),
    (None, J(heading('Publicity', 4), para('Owen Maddox, Harrow &amp; Lane. For reviews, interviews, festivals and book groups.', fontSize='small'), para('<a href="mailto:owen@harrowlane.example">owen@harrowlane.example</a>', fontSize='small'))),
    (None, J(heading('Film and TV', 4), para('Sofia Lindgren, Lantern Street Agency. The Fenland rights are optioned until 2027.', fontSize='small'), para('<a href="mailto:sofia@lanternstreet.example">sofia@lanternstreet.example</a>', fontSize='small'))),
    (None, J(heading('Me', 4), para('Readers’ letters to the agency are forwarded to me every month. I read all of them and reply to some.', fontSize='small'))),
    align='wide', className='is-style-rule-top'))

pattern('bio', 'Short bio', 'about', columns(
    ('40%', image('desk.jpg', 'An old wooden desk with a manual typewriter, two telephones and a swivel chair', caption='Not my desk. Mine is messier.')),
    ('60%', J(heading('About', 2),
              para('Tamsin Rourke was born in King’s Lynn in 1974, the daughter of a shrimp fisherman. She worked for twelve years as a court clerk in Peterborough before her first novel, <em>The Salt Road</em>, was published in 2016.'),
              para('She has written three Fenland crime novels, two stand-alone novels, a book of travel essays and a memoir about her father. Her books are translated into nine languages. She lives in King’s Lynn with her husband and a lurcher called Pike.'),
              para('I write in the mornings and walk the sea wall in the afternoons. I don’t do book blurbs for strangers, and I don’t write about real murders. There are enough invented ones.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('colophon', 'Colophon', 'text', para('Set in Cabin and Literata. Covers on this site are drawn in the page, not scanned. Photographs from Wikimedia Commons, in the public domain or CC0.', className='is-style-colophon'))

pattern('signed-copies', 'Signed copies from one shop', 'call-to-action', group(J(
    heading('Signed copies', 3),
    para('Old Custom House Books on Purfleet Quay, King’s Lynn, keeps signed copies of every book. They post anywhere in the UK for £3.20 and I will dedicate one if you ask by the 1st of the month. Their number is 01553 760 214, and they open Tuesday to Saturday, 10am to 5pm.'),
    buttons(('Order a signed copy', 'https://example.com/old-custom-house-books'))),
    className='is-style-band-crime', style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('series-note', 'Series note', 'text', para('<strong>The Fenland novels:</strong> <a href="/low-country/">Low Country</a> (2018), <a href="/a-drowned-parish/">A Drowned Parish</a> (2020), <a href="/the-wash-in-winter/">The Wash in Winter</a> (2026). Read them in that order.', fontSize='small'))

pattern('isbn-line', 'Book details line', 'text', table([['Hardback', '384 pages', 'ISBN 978-1-9160-4412-8', '£18.99']], className='is-style-regular'))

pattern('buy-page', 'Page: buy (every book, every edition)', 'call-to-action', J(
    para('Every book, every format. Independent shops are listed first on purpose.', fontSize='large'),
    pattern_ref('buy-block'), pattern_ref('signed-copies'), pattern_ref('audiobook-sample'), pattern_ref('editions'), pattern_ref('translations'),
    heading('The other books', 2),
    table([['<a href="/my-fathers-boats/">My Father’s Boats</a>', 'Paperback £10.99', '<a href="https://uk.bookshop.org/">Bookshop.org</a>, <a href="https://www.waterstones.com/">Waterstones</a>'],
           ['<a href="/harbour-lights/">Harbour Lights</a>', 'Paperback £9.99', '<a href="https://uk.bookshop.org/">Bookshop.org</a>, <a href="https://www.waterstones.com/">Waterstones</a>'],
           ['<a href="/a-drowned-parish/">A Drowned Parish</a>', 'Paperback £9.99', '<a href="https://uk.bookshop.org/">Bookshop.org</a>, <a href="https://www.waterstones.com/">Waterstones</a>'],
           ['<a href="/seven-trams-in-lisbon/">Seven Trams in Lisbon</a>', 'Paperback £12.99', '<a href="https://uk.bookshop.org/">Bookshop.org</a>'],
           ['<a href="/low-country/">Low Country</a>', 'Paperback £9.99', '<a href="https://uk.bookshop.org/">Bookshop.org</a>, <a href="https://www.waterstones.com/">Waterstones</a>'],
           ['<a href="/the-salt-road/">The Salt Road</a>', 'Paperback £8.99', '<a href="https://uk.bookshop.org/">Bookshop.org</a>']],
          head=['Book', 'Format', 'Where'])), block_types='core/post-content')

pattern('book-groups-page', 'Page: book groups', 'text', J(pattern_ref('book-group-guide'), pattern_ref('excerpt'), pattern_ref('book-group-faq'),
    heading('Guides for the other books', 3),
    lst(['<a href="/my-fathers-boats/">My Father’s Boats</a>: eight questions, and photographs of the boats', '<a href="/harbour-lights/">Harbour Lights</a>: ten questions', '<a href="/low-country/">Low Country</a>: eight questions and a map of Wisbech'])),
    block_types='core/post-content')
pattern('events-page', 'Page: events', 'text', J(pattern_ref('events-rows'), pattern_ref('band-tiles'), pattern_ref('signed-copies')), block_types='core/post-content')
pattern('newsletter-page', 'Page: newsletter and archive', 'call-to-action', J(pattern_ref('newsletter-signup'), pattern_ref('band-dots'),
    heading('All letters', 3),
    table([['Sep 2026', 'Proofs, a heron and the launch date'], ['Jul 2026', 'Why the third book took three years'], ['May 2026', 'The cover, and the argument about the cover'],
           ['Mar 2026', 'Wisbech in the rain, and the first draft is done'], ['Jan 2026', 'What I read in 2025 (41 books, 9 abandoned)']], head=['Sent', 'Letter'])),
    block_types='core/post-content')
pattern('about-page', 'Page: about', 'about', J(pattern_ref('bio'), pattern_ref('author-note'), pattern_ref('places'), pattern_ref('prizes'), pattern_ref('short-stories'), pattern_ref('praise')), block_types='core/post-content')
pattern('contact-page', 'Page: contact', 'contact', J(
    para('Please use the right person below. I don’t publish my own email because of the post it attracts, but letters to the agency reach me every month.', fontSize='large'),
    pattern_ref('contacts')), block_types='core/post-content')
pattern('books-page', 'Page: books in order', 'text', J(pattern_ref('shelf'), pattern_ref('reading-order'), pattern_ref('band-scales'), pattern_ref('books-in-order'), pattern_ref('clothbound-cover')), block_types='core/post-content')

pattern('front-page-layout', 'Home: collage opener, patchwork, shelf, buy, events', 'featured', J(
    pattern_ref('collage-hero'), pattern_ref('band-waves'), pattern_ref('series-patchwork'), pattern_ref('shelf'),
    columns(('55%', pattern_ref('buy-block')), ('45%', J(pattern_ref('events-rows'))), align='wide', className='is-style-rule-top',
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'bottom': 'var:preset|spacing|60'}}}),
    pattern_ref('great-ideas-quote'),
    columns(('55%', pattern_ref('newsletter-signup')), ('45%', pattern_ref('praise-single')), align='wide',
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}})), inserter=False)
pattern('praise-single', 'One praise quote', 'testimonials', J(
    quote('The best sense of place in British crime writing since the early Ruth Rendell.', 'Hannah Okoro, Fenland Quarterly, on Low Country, 2018'),
    quote('I read it in one sitting on a train and missed my stop at Ely.', 'Nadia Karim, bookseller, Riverside Books, Ely')))

# ---------------------------------------------------------------- parts
def header(g):
    return group(row(J(dyn('site-title', level=0), dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'})),
                     justify='space-between', align='wide'),
                 tag='header', align='full', className='is-style-band-' + g,
                 style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40'}}})

def footer(g):
    return group(J(
        columns(('40%', J(para('Tamsin Rourke', fontSize='x-large', fontFamily='display', style={'typography': {'fontWeight': '700', 'lineHeight': '1'}}),
                         para('Novels, crime and one memoir, written in King’s Lynn, Norfolk.', fontSize='small'))),
                (None, J(heading('Books', 6), para('<a href="/books/">In order</a><br><a href="/buy/">Buy</a><br><a href="/book-groups/">Book groups</a>', fontSize='small'))),
                (None, J(heading('News', 6), para('<a href="/events/">Events</a><br><a href="/newsletter/">Newsletter</a><br><a href="/about/">About</a>', fontSize='small'))),
                (None, J(heading('Contact', 6), para('<a href="/contact/">Agent, publicist and film rights</a>', fontSize='small'))),
                align='wide'),
        group(pattern_ref('colophon'), align='wide', layout={'type': 'default'})),
        tag='footer', align='full', className='is-style-band-' + g,
        style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}})

write('parts/header.html', header('fiction'))
write('parts/footer.html', footer('fiction'))
for g in ('crime', 'memoir', 'travel'):
    write('parts/header-%s.html' % g, header(g))
    write('parts/footer-%s.html' % g, footer(g))

# ---------------------------------------------------------------- templates
PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(pattern_ref('front-page-layout')))
BOOK_ITEM = group(J(dyn('post-featured-image', isLink=True, aspectRatio='2/3', style={'color': {'duotone': 'var:preset|duotone|ink'}}),
                    dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-terms', term='category'), dyn('post-date', format='Y')), layout={'type': 'default'})
pattern('book-grid-archive', 'Books (inherits the page query)', 'posts,query', inherit_query(BOOK_ITEM, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}, align='wide'), inserter=False)
write('templates/home.html', page_template(J(
    heading('Books', 1, fontSize='display', align='wide'),
    pattern_ref('shelf'), pattern_ref('reading-order'), pattern_ref('books-in-order')), style=PAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('book-grid-archive')), style=PAD))

def cat_tpl(g):
    return J(template_part('header' if g == 'fiction' else 'header-' + g, 'header'),
             group(J(dyn('query-title', type='archive', showPrefix=False, fontSize='display', align='wide'), dyn('term-description', align='wide', fontSize='large'),
                     pattern_ref('book-grid-archive')), tag='main', style=PAD),
             template_part('footer' if g == 'fiction' else 'footer-' + g, 'footer'))
write('templates/archive.html', cat_tpl('fiction'))
for g in ('crime', 'memoir', 'travel'):
    write('templates/category-%s.html' % g, cat_tpl(g))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='A title, a place, a character', buttonText='Search'), pattern_ref('book-grid-archive')), style=PAD))
write('templates/404.html', page_template(J(heading('This page has gone out of print', 1),
    para('The link may be to an old edition of the site. The <a href="/books/">books page</a> has everything in order.'),
    dyn('search', label='Search', showLabel=False, placeholder='A title, a place, a character', buttonText='Search')), style=PAD))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), separator(), dyn('post-content', align='wide', layout={'type': 'constrained'})), style=PAD))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large', align='wide'), separator(align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})), style=PAD))

def single_book(g):
    col, name, txt = GENRES[g]
    hdr = 'header' if g == 'fiction' else 'header-' + g
    ftr = 'footer' if g == 'fiction' else 'footer-' + g
    cover = group(J(
        group(J(para(name, fontFamily='display', fontSize='small', style={'typography': {'fontWeight': '600'}}),
                dyn('post-title', level=1, fontSize='xx-large'), para('Tamsin Rourke', fontFamily='display', fontSize='large')),
              className='is-style-band-' + g, layout={'type': 'default'},
              style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
        dyn('post-featured-image', aspectRatio='4/3', style={'color': {'duotone': 'var:preset|duotone|' + g}})),
        layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}})
    return J(template_part(hdr, 'header'),
             group(J(columns(('40%', J(cover, dyn('post-terms', term='category', prefix='On the shelf: '), dyn('post-date', format='Y', textColor='muted'))),
                             ('60%', dyn('post-content', layout={'type': 'default'})),
                             align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|70'}}}),
                     group(J(dyn('post-navigation-link', type='previous', label='Earlier book', showTitle=True), dyn('post-navigation-link', label='Later book', showTitle=True)),
                           align='wide', className='is-style-rule-top', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'})),
                   tag='main', style=PAD),
             template_part(ftr, 'footer'))
for g in GENRES:
    write('templates/single-book-%s.html' % g, single_book(g))
write('templates/single.html', single_book('fiction'))

write('style.css', '''/*
Theme Name: Spine
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: An author website for novelists with a handful of books, built on the colour-banded paperback grid, with a buy block that lists independent shops first.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: spine
Tags: blog, book, entertainment, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout, two-columns
*/''')

# ---------------------------------------------------------------- demo content
PRAISE = {
    'the-wash-in-winter': ('Rourke writes the Fens like other people write the sea: flat, cold and full of things that don’t stay buried.', 'Hannah Okoro, Fenland Quarterly, August 2026'),
    'my-fathers-boats': ('A book about a man who never said much, written by a daughter who finally does.', 'Alice Brandt, The Northern Review, 2023'),
    'harbour-lights': ('Quietly furious and very funny about money.', 'The Northern Review, 2022'),
    'a-drowned-parish': ('The drought chapter is as frightening as anything in the genre this year.', 'Crime Time Quarterly, 2020'),
    'seven-trams-in-lisbon': ('The number 28 has never been this interesting, or this crowded.', 'Sam Ferreira, Slow Travel Letters, 2019'),
    'low-country': ('The best sense of place in British crime writing since the early Ruth Rendell.', 'Fenland Quarterly, 2018'),
    'the-salt-road': ('A first novel that smells of the marsh.', 'Norfolk Book Club, 2016'),
}
posts = []
for slug, title, g, year, img, blurb, isbn in BOOKS:
    pq, ps = PRAISE[slug]
    content = J(para(blurb, fontSize='large'),
                quote(pq, ps),
                heading('Buy', 3), buy_list(title, signed=True),
                heading('Details', 3), table([['Paperback' if year != '2026' else 'Hardback', ('%d pages' % (300 + int(year[-2:]) * 3)), 'ISBN ' + isbn, '£9.99' if year != '2026' else '£18.99'], ['Publisher', 'Harrow &amp; Lane', 'First published', year]]),
                para('<a href="/book-groups/">Book-group questions</a> and <a href="/buy/">all editions</a>.', fontSize='small'))
    if slug in SERIES:
        content = J(para('<strong>%s.</strong> The Fenland novels: <a href="/low-country/">Low Country</a>, <a href="/a-drowned-parish/">A Drowned Parish</a>, <a href="/the-wash-in-winter/">The Wash in Winter</a>.' % SERIES[slug], fontSize='small'), content)
    posts.append({'title': title, 'slug': slug, 'category': g, 'image': img, 'excerpt': blurb, 'date': year + ('-10-08' if year == '2026' else '-05-14'),
                  'template': 'single-book-' + g, 'content': content})

demo = {
    'site': {'title': 'Tamsin Rourke', 'tagline': 'Novels, Fenland crime and one memoir, from King’s Lynn'},
    'categories': [{'slug': 'fiction', 'name': 'Fiction', 'description': 'The stand-alone novels. Orange, as fiction always was.'},
                   {'slug': 'crime', 'name': 'Crime', 'description': 'The Fenland novels, with DS Ruth Ambler. Read them in order.'},
                   {'slug': 'memoir', 'name': 'Memoir', 'description': 'My Father’s Boats, about my dad and the seven boats he lost.'},
                   {'slug': 'travel', 'name': 'Travel', 'description': 'Seven Trams in Lisbon, essays from one winter.'}],
    'front_page': 'home', 'posts_page': 'books',
    'pages': [{'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'books', 'title': 'Books', 'content': ''},
              {'slug': 'buy', 'title': 'Buy the books', 'pattern': 'spine/buy-page'},
              {'slug': 'events', 'title': 'Events', 'pattern': 'spine/events-page', 'template': 'page-wide'},
              {'slug': 'book-groups', 'title': 'For book groups', 'pattern': 'spine/book-groups-page'},
              {'slug': 'newsletter', 'title': 'Newsletter', 'pattern': 'spine/newsletter-page'},
              {'slug': 'about', 'title': 'About', 'pattern': 'spine/about-page', 'template': 'page-wide'},
              {'slug': 'contact', 'title': 'Contact', 'pattern': 'spine/contact-page', 'template': 'page-wide'}],
    'posts': posts,
    'nav': [{'label': 'Books', 'url': '/books/'}, {'label': 'Buy', 'url': '/buy/'}, {'label': 'Events', 'url': '/events/'},
            {'label': 'Book groups', 'url': '/book-groups/'}, {'label': 'Newsletter', 'url': '/newsletter/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/spine', exist_ok=True)
json.dump(demo, open('demos/spine/content.json', 'w'), indent=1, ensure_ascii=False)
print('built spine')
