# booth: Dzwig, a two-room recording studio in the old Gdansk shipyard.
# Direction: "actually modern", after studionagrywarka.pl. Pale concrete grey page, one huge black headline in a
#   heavy geometric sans with studio photos collaged underneath it, then a full-bleed record-light orange block
#   for the rooms. The research's industrial gear list stays, restyled as a clean inventory with a sticky index.
# Fonts: Figtree only (claimed for 044; the brief moves away from Tektur): 900 for headlines, 400/600 for text.
# Palette: #F3F3F1 concrete, #0A0A0A black, #FF5B24 record light (full-bleed blocks, black text on it),
#   #D63F0B for links and small accents on grey. Layout idea: the headline sits on top of a loose photo collage.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('booth')
import blocks as _B
_orig_image = _B.image
def _image_ratio(filename, alt, caption='', lightbox=True, href=None, **attrs):
    out = _orig_image(filename, alt, caption, lightbox, href, **attrs)
    if attrs.get('aspectRatio'):
        out = out.replace('" alt="%s"/>' % alt, '" alt="%s" style="aspect-ratio:%s;object-fit:%s"/>' % (alt, attrs['aspectRatio'], attrs.get('scale', 'cover')), 1)
    return out
_B.image = _image_ratio
image = _image_ratio
S = THEME['slug']
D = THEME['dir']
V = lambda k: 'var:preset|color|' + k

def wjson(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

def cols(*cs, **attrs):
    """cs: (width or None, inner, {column attrs})."""
    out = []
    for c in cs:
        w, inner = c[0], c[1]
        ca = dict(c[2]) if len(c) > 2 else {}
        if w:
            ca = {'width': w, **ca}
        cls = 'wp-block-column' + ((' is-vertically-aligned-' + ca['verticalAlignment']) if ca.get('verticalAlignment') else '') + ((' ' + ca['className']) if ca.get('className') else '')
        st = (' style="flex-basis:%s"' % w) if w else ''
        out.append('<!-- wp:column%s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:column -->' % ((' ' + json.dumps(ca, separators=(',', ':'), ensure_ascii=False)) if ca else '', cls, st, inner))
    a = attrs
    va = ('are-vertically-aligned-' + a['verticalAlignment']) if a.get('verticalAlignment') else ''
    return '<!-- wp:columns%s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:columns -->' % ((' ' + json.dumps(a, separators=(',', ':'))) if a else '', ' '.join(filter(None, ['wp-block-columns', 'align' + a['align'] if a.get('align') else '', va, a.get('className', '')])), _B._style(a), '\n\n'.join(out))

# ------------------------------------------------------------------ theme.json
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
display = next(f for f in fonts if f['slug'] == 'display')
PAL = [
    ('base', '#F3F3F1', 'Concrete'),
    ('contrast', '#0A0A0A', 'Black'),
    ('accent', '#D63F0B', 'Record light, dark'),
    ('signal', '#FF5B24', 'Record light'),
    ('surface', '#E6E6E2', 'Foam'),
    ('line', '#0A0A0A', 'Rule'),
    ('muted', '#5F5F5B', 'Cable grey'),
]
def palette(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1360px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True,
            'fontFamilies': [display, {'fontFamily': display['fontFamily'], 'name': 'Figtree (text)', 'slug': 'body'}],
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Caption', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.75rem', 'name': 'Lead', 'fluid': {'min': '1.375rem', 'max': '1.75rem'}},
                {'slug': 'x-large', 'size': '3rem', 'name': 'Section', 'fluid': {'min': '2.125rem', 'max': '3rem'}},
                {'slug': 'xx-large', 'size': '5.5rem', 'name': 'Title', 'fluid': {'min': '3rem', 'max': '5.5rem'}},
                {'slug': 'display', 'size': '10rem', 'name': 'Display', 'fluid': {'min': '3.4rem', 'max': '10rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.5rem, 6vw, 4.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3.5rem, 9vw, 7rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(5rem, 13vw, 11rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': V('base'), 'text': V('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': V('accent')}},
                     ':focus': {'outline': {'color': V('accent'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'lineHeight': '0.95', 'letterSpacing': '-0.035em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'lineHeight': '0.9'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'letterSpacing': '-0.025em'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '800', 'lineHeight': '1.1', 'letterSpacing': '-0.01em'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '800', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'button': {'color': {'background': V('contrast'), 'text': V('base')},
                       'border': {'radius': '8px', 'width': '2px', 'style': 'solid', 'color': V('contrast')},
                       'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|medium'},
                       'spacing': {'padding': {'top': '0.8em', 'bottom': '0.8em', 'left': '1.4em', 'right': '1.4em'}},
                       ':hover': {'color': {'background': V('signal'), 'text': V('contrast')}, 'border': {'color': V('signal')}},
                       ':focus': {'outline': {'color': V('accent'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': V('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.03em'},
                                'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '600'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': V('accent')}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'}, 'color': {'text': V('muted')}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'}},
            'core/image': {'border': {'radius': '18px'}},
            'core/post-featured-image': {'border': {'radius': '18px'}},
            'core/media-text': {'border': {'radius': '18px'}},
            'core/separator': {'color': {'text': V('line')}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '800', 'lineHeight': '1.05', 'letterSpacing': '-0.02em'},
                           'border': {'width': '0'}, 'spacing': {'padding': {'left': '0'}},
                           'elements': {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '400', 'letterSpacing': '0', 'fontStyle': 'normal'}}}},
            'core/pullquote': {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '900', 'lineHeight': '0.95'}, 'border': {'width': '0'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'top': {'color': V('line'), 'width': '2px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/query-pagination': {'typography': {'fontWeight': '700'}},
            'core/search': {'border': {'radius': '8px'}},
        },
        'css': ('body{font-synthesis:none}:where(h1,h2,h3,h4){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid color-mix(in srgb,currentColor 35%,transparent);padding:.65em 1em .65em 0;text-align:left;vertical-align:top;font-variant-numeric:tabular-nums}'
                '.wp-block-table thead{border-bottom:2px solid currentColor}.wp-block-table th{font-weight:700}'
                '.wp-block-details summary{font-family:var(--wp--preset--font-family--display);font-weight:800;font-size:var(--wp--preset--font-size--large);letter-spacing:-.01em;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:1rem}'
                '.wp-block-details summary::-webkit-details-marker{display:none}.wp-block-details summary::after{content:"+";font-weight:400}.wp-block-details[open] summary::after{content:"\\2212"}'
                '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:8px;background:transparent}'
                '.wp-block-navigation .current-menu-item>a,.wp-block-navigation a[aria-current]{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:.35em}'
                '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base)}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'
                '@media (min-width:782px){.is-style-collage{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--wp--preset--spacing--40)}'
                '.is-style-collage>h1{grid-area:1/1/2/13;position:relative;z-index:2}.is-style-collage>figure{margin:0!important}'
                '.is-style-collage>figure:nth-of-type(1){grid-area:1/7/2/11;margin-top:15vw!important}'
                '.is-style-collage>figure:nth-of-type(2){grid-area:1/1/2/5;margin-top:34vw!important}'
                '.is-style-collage>figure:nth-of-type(3){grid-area:1/10/2/13;margin-top:44vw!important}}'
                '@media (max-width:781px){.is-style-collage>figure img{aspect-ratio:3/2!important}.is-style-collage>figure:nth-of-type(3){display:none}}'
                '@media (min-width:782px){.is-style-sticky-index{position:sticky;top:var(--wp--preset--spacing--40);align-self:flex-start}}'
                '@media (prefers-reduced-motion:no-preference){.wp-block-post-featured-image img,.is-style-collage img{transition:transform .3s ease}.wp-block-post-featured-image a:hover img{transform:scale(1.02)}}'),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'next-dates', 'title': 'Next free dates'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'page-room', 'title': 'Room (big title, full-width photo)', 'postTypes': ['page']},
    ],
}
wjson('theme.json', theme)

write('style.css', '''/*
Theme Name: Booth
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A modern theme for independent recording and rehearsal studios, with room pages, a gear inventory, day rates, engineers and load-in directions.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: booth
Tags: portfolio, entertainment, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def variation(name, title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': palette(pal)}}}
    if extra:
        d['styles'] = extra
    wjson('styles/%s.json' % name, d)
variation('console', 'Console', [('base', '#1C1D1F', 'Concrete'), ('contrast', '#EDEDEA', 'Black'), ('accent', '#8FE37A', 'Record light, dark'),
    ('signal', '#8FE37A', 'Record light'), ('surface', '#26282B', 'Foam'), ('line', '#EDEDEA', 'Rule'), ('muted', '#A9ABA6', 'Cable grey')])
variation('tape', 'Tape', [('base', '#F1E9D6', 'Concrete'), ('contrast', '#1D1A15', 'Black'), ('accent', '#A8391A', 'Record light, dark'),
    ('signal', '#E9B949', 'Record light'), ('surface', '#E6DBC2', 'Foam'), ('line', '#1D1A15', 'Rule'), ('muted', '#5C554A', 'Cable grey')])
variation('live-room', 'Live room', [('base', '#EFE7DD', 'Concrete'), ('contrast', '#231A14', 'Black'), ('accent', '#8A4B24', 'Record light, dark'),
    ('signal', '#C98B5B', 'Record light'), ('surface', '#E2D5C6', 'Foam'), ('line', '#231A14', 'Rule'), ('muted', '#62544A', 'Cable grey')],
    {'elements': {'heading': {'typography': {'fontWeight': '700', 'letterSpacing': '-0.02em'}}}})

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('collage', 'Headline collage', ['core/group'], {
    'css': '&{position:relative}& > h1,& > h2{position:relative;z-index:2;margin:0}& > figure{position:relative;z-index:1;margin:var(--wp--preset--spacing--30) 0 0}'
           '& > figure img{width:100%;aspect-ratio:4/5;object-fit:cover}'})
section('signal', 'Record light block', ['core/group', 'core/columns', 'core/column'], {
    'color': {'background': V('signal'), 'text': V('contrast')},
    'elements': {'link': {'color': {'text': V('contrast')}}},
    'css': '& .wp-element-button:hover{background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast);border-color:var(--wp--preset--color--base)}'})
section('dark', 'Black block', ['core/group', 'core/columns', 'core/column'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('base')}}, 'heading': {'color': {'text': V('base')}}, 'button': {'color': {'background': V('base'), 'text': V('contrast')}}},
    'css': '& .has-muted-color{color:var(--wp--preset--color--surface)!important}'})
section('panel', 'Foam panel', ['core/group', 'core/column'], {
    'color': {'background': V('surface'), 'text': V('contrast')},
    'border': {'radius': '24px'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('lead', 'Lead paragraph', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '-0.01em'}})
section('chip-list', 'Category buttons', ['core/buttons'], {
    'css': '& .wp-element-button{background:transparent;color:inherit;border-color:currentColor}& .wp-element-button:hover{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);border-color:var(--wp--preset--color--contrast)}'})
section('room-tag', 'Room tag', ['core/paragraph'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'border': {'radius': '6px'},
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'},
    'spacing': {'padding': {'top': '0', 'bottom': '0', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
    'css': '&{display:inline-block}'})
section('gear-table', 'Gear table', ['core/table'], {
    'css': '& td:first-child{font-weight:700;width:34%}& td:last-child{width:6.5em;white-space:nowrap}& td:last-child em{font-style:normal;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);border-radius:6px;padding:.1em .5em;font-size:.85em;font-weight:700}'
           '& td:last-child strong{font-weight:700;background:var(--wp--preset--color--signal);border-radius:6px;padding:.1em .5em;font-size:.85em}'})
section('rates', 'Rate table', ['core/table'], {
    'css': '& td:first-child{font-family:var(--wp--preset--font-family--display);font-weight:800;font-size:1.2em}& td:not(:first-child){white-space:nowrap}'})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': V('line'), 'width': '2px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})

# ------------------------------------------------------------------ parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0),
          row(J(dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}, overlayMenu='mobile'),
                buttons(('Book a session', '/rates/#booking'))), wrap=False, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
        justify='space-between', wrap=False, align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40'}}}),
    tag='header', align='full', layout={'type': 'constrained'}))
write('parts/next-dates.html', pattern_ref('next-free-dates'))
write('parts/footer.html', group(J(
    heading('Hala 3, ul. Narzędziowców 9, Gdańsk', 2, fontSize='x-large', align='wide'),
    cols((None, J(heading('Studio', 6), para('Dźwig<br>Hala 3, ul. Narzędziowców 9<br>80-863 Gdańsk, Młode Miasto', fontSize='small'))),
         (None, J(heading('Bookings', 6), para('<a href="mailto:studio@example.com">studio@example.com</a><br>+48 58 555 01 90, weekdays 10:00 to 18:00', fontSize='small'))),
         (None, J(heading('Elsewhere', 6), para('<a href="https://www.instagram.com/">Instagram</a><br><a href="https://www.youtube.com/">Live session videos</a><br><a href="/visit/">Load-in and parking</a>', fontSize='small'))),
         align='wide', style={'spacing': {'margin': {'top': 'var:preset|spacing|50'}}}),
    para('Demo photos are CC0 images from Wikimedia Commons, Unsplash and pxhere, used as stand-ins for the real rooms.', align='wide', fontSize='x-small', className='has-muted-color')),
    tag='footer', align='full', className='is-style-dark',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ------------------------------------------------------------------ patterns
# Signature look: headline over a photo collage (grid positions set in theme.json css for wide screens)
collage = group(J(
    heading('A big room for bands who want to play together', 1),
    image('console.jpg', 'The Studio A control room: a large console, five speakers on stands and acoustic panels on the walls', lightbox=False),
    image('drums.jpg', 'A four-piece drum kit seen from above, with cymbals on stands', lightbox=False),
    image('vocal.jpg', 'A black and white photo of a large-diaphragm microphone with a pop filter', lightbox=False)),
    className='is-style-collage', align='wide', layout={'type': 'default'})
pattern('hero-collage', 'Hero: headline over a photo collage', 'featured', collage,
        description='One very large headline with three photos behind it. Swap in your own rooms.')

pattern('intro-lead', 'Intro in large type', 'text', cols(
    ('58%', para('Dźwig is two recording rooms and a rehearsal room in a former shipyard hall in Gdańsk. The live room is 64 m² with a 7 metre ceiling, big enough to track a whole band with sightlines, and the control room was built around a 32-channel console we rescued from Polish Radio in Szczecin.', className='is-style-lead')),
    (None, J(para('We record bands, choirs, jazz trios and the odd theatre soundtrack. We are not the place for a quick vocal overdub on a laptop session, and we will tell you if a smaller room would suit you better.'),
             buttons(('See the rooms', '/rooms/'), ('Check the rates', '/rates/', {'className': 'is-style-outline'})))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

room_block = lambda img, alt, name, size, desc, rows, link: J(
    image(img, alt, lightbox=False, aspectRatio='4/3', scale='cover'),
    heading(name, 3), para(size, className='is-style-room-tag'), para(desc),
    table(rows), buttons(('Look inside ' + name, link)))
pattern('rooms-signal', 'Rooms on a record-light block', 'featured', group(J(
    heading('Two rooms and a rehearsal space', 2, align='wide'),
    cols(
        (None, room_block('hero.jpg', 'Studio A control room with a wooden ceiling, leather chairs and the console in front of a window into the live room', 'Studio A', '64 m² live room, 7 m ceiling',
                          'Tracking room with three isolation booths and a Yamaha C7 grand. The control room looks into all of it.',
                          [['Console', 'Neve-style 32-channel, rebuilt 2021'], ['Tape', 'Studer A827 24-track, 2 inch'], ['Day with engineer', '2,400 zł']], '/rooms/studio-a/')),
        (None, room_block('band.jpg', 'Studio B: two monitors, a keyboard and outboard gear against a wall of black acoustic foam', 'Studio B', '22 m² mix room',
                          'Mixing, overdubs and vocals. Treated for mixing first, so it is quiet and a bit dead to sing in, on purpose.',
                          [['Desk', 'SSL XLogic X-Desk, 16 channels'], ['Monitors', 'ATC SCM25A, Yamaha NS-10M'], ['Day with engineer', '1,100 zł']], '/rooms/studio-b/')),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    className='is-style-signal', align='full', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))

pattern('next-free-dates', 'Next free dates (update weekly)', 'banner', group(row(J(
    para('<strong>Next free days in Studio A:</strong> 14 and 15 October, 3 to 7 November, 1 December. Studio B has most weekdays free.'),
    para('<a href="/rates/#booking">Hold a date</a>')), justify='space-between'), className='is-style-dark', align='full',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}),
    description='Marta updates this every Monday. Delete the part from the template if you would rather not show it.')

GEAR = [
    ('consoles', 'Consoles and monitoring', [
        ('Polish Radio console, Neve-style', '32 channels, 1084-style EQ, rebuilt by Tonmeister Szczecin in 2021', 'A'),
        ('SSL XLogic X-Desk', '16-channel summing mixer with SuperAnalogue preamps', 'B'),
        ('ATC SCM45A', 'Main monitors in Studio A', 'A'),
        ('ATC SCM25A, Yamaha NS-10M', 'Mix monitors in Studio B', 'B'),
        ('Hear Back PRO', 'Six headphone mixes, 12 pairs of Beyerdynamic DT 770', 'Shared')]),
    ('microphones', 'Microphones', [
        ('Neumann U 87 Ai (x2)', 'Large-diaphragm condenser', 'Shared'), ('AKG C414 XLS (x2)', 'Multi-pattern condenser', 'Shared'),
        ('Coles 4038 (pair)', 'Ribbon, our favourite on drum overheads', 'A'), ('Royer R-121 (x2)', 'Ribbon, guitar cabs', 'Shared'),
        ('Tonsil MD 263', 'Polish dynamic from the 70s. Sounds like a telephone, in a good way', 'Shared'),
        ('Shure SM57 (x8), SM7B (x2), Beta 52A', 'Dynamics', 'Shared')]),
    ('recorders', 'Recorders', [
        ('Studer A827', '24-track, 2 inch. Tape is 1,150 zł a reel, bring your own if you like', 'A'),
        ('Pro Tools HDX', '64 inputs through Avid HD I/O and Burl B2 converters', 'Shared'), ('Otari MX-5050', '1/4 inch half-track for mixdown', 'B')]),
    ('outboard', 'Outboard', [
        ('Universal Audio 1176LN (x2)', 'Compressor', 'Shared'), ('Teletronix LA-2A', 'Compressor', 'A'),
        ('Chandler TG1', 'Limiter', 'B'), ('EMT 140', 'Plate reverb, in the old paint store next door', 'Shared'),
        ('Roland RE-201 Space Echo', 'Tape echo. Works most days', 'Shared')]),
    ('instruments', 'Instruments and amps', [
        ('Yamaha C7 grand', 'Tuned before every booking, included in the rate', 'A'), ('Hammond A-100 with Leslie 147', '', 'A'),
        ('Ludwig Classic Maple kit', '22, 13, 16, with a Supraphonic snare', 'A'), ('Fender Twin Reverb, Vox AC30, Ampeg B-15', 'Amps', 'Shared'),
        ('Fender Champion II 50', 'Small practice combo, lives in the rehearsal room', 'Rehearsal')]),
]
def gear_rows(items):
    return [[n, d, ('<strong>Shared</strong>' if r == 'Shared' else '<em>%s</em>' % r)] for n, d, r in items]

index_links = lst(['<a href="#%s">%s</a>' % (k, t) for k, t, _ in GEAR] + ['<a href="%s">Text-only list for engineers</a>' % "<?php echo esc_url( get_theme_file_uri( 'assets/gear-list.txt' ) ); ?>"])
inventory = cols(
    ('26%', J(heading('Jump to', 4), index_links,
              para('<strong>A</strong> and <strong>B</strong> mean the item stays in that room. Shared gear moves to whichever room needs it, so ask if you need two of something on the same day.', fontSize='x-small', className='has-muted-color')),
     {'className': 'is-style-sticky-index'}),
    (None, J(*[details(t, table(gear_rows(items), head=['Item', 'Notes', 'Room'], className='is-style-gear-table'), anchor=k, showContent=True)
               .replace('<details class="wp-block-details">', '<details id="%s" class="wp-block-details" open>' % k) for k, t, items in GEAR],
             para('Need something that is not here? We can usually hire it from Nord Rental in Gdynia with a day\'s notice, at cost.', className='is-style-lead'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})
pattern('gear-inventory', 'Gear inventory: by category, per room and shared', 'featured', inventory,
        description='Equipment grouped by category with a sticky index. Each item says whether it stays in one room or is shared.')

open(os.path.join(D, 'assets', 'gear-list.txt'), 'w').write('DZWIG STUDIO, GEAR LIST (text only)\nUpdated September 2026. A = Studio A, B = Studio B.\n\n' + '\n\n'.join(
    t.upper() + '\n' + '\n'.join('%s  [%s]  %s' % (n, r, d) for n, d, r in items) for k, t, items in GEAR) + '\n')

pattern('gear-categories', 'Gear categories as buttons', 'featured', group(J(
    heading('What is in the rooms', 3),
    buttons(*[(t, '/gear/#' + k) for k, t, _ in GEAR], className='is-style-chip-list')), align='wide', layout={'type': 'default'}))

pattern('rates-table', 'Day and half-day rates', 'featured', J(
    heading('Rates', 2),
    table([['Studio A, day (10 hours)', '2,400 zł', '1,600 zł'], ['Studio A, half day (5 hours)', '1,300 zł', '900 zł'],
           ['Studio B, day (10 hours)', '1,100 zł', '700 zł'], ['Studio B, half day (5 hours)', '600 zł', '400 zł'],
           ['Rehearsal room', '60 zł an hour', 'No engineer']],
          head=['', 'With engineer', 'Without engineer'], className='is-style-rates'),
    para('Prices include VAT, the piano tuning and a runner for coffee. Without an engineer means a Dźwig assistant sets up and stays in the building, and you drive the desk. Tape and hard drives are extra.', fontSize='small')), description='Rates with engineer included and not included.')

pattern('deposit-terms', 'Deposit and cancellation', 'text', group(J(
    heading('Deposit and cancelling', 4),
    lst(['A 30% deposit holds your dates. We send an invoice the day you book.', 'Cancel 14 days or more ahead and we refund the deposit in full.',
         'Cancel 7 to 13 days ahead and we keep the deposit, or move it to new dates within six months.', 'Cancel less than 7 days ahead and the full day rate is due. If someone else books the day, we refund you.',
         'Illness in the band is the one exception. Send us a note and we will move you.'])), className='is-style-panel'))

pattern('booking-enquiry', 'Booking enquiry', 'call-to-action', group(J(
    heading('Book a session', 2),
    para('Email us with the dates you want, how many people are playing, and a link to something you have recorded before. Marta replies within a working day with a quote.', className='is-style-lead'),
    buttons(('Email Marta about dates', 'mailto:studio@example.com?subject=Booking'), ('Call +48 58 555 01 90', 'tel:+48585550190', {'className': 'is-style-outline'}))),
    className='is-style-signal', align='full', anchor='booking', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))

pattern('engineers', 'Engineers with credits', 'about', group(J(
    heading('Who you will work with', 2),
    cols(
        (None, J(image('headphones.jpg', 'Black and white photo of an engineer in headphones at a desk in a small studio', lightbox=False, aspectRatio='4/5', scale='cover'),
                 heading('Marta Kołodziej', 4), para('Owner, engineer. Recorded the first two Rzeka albums and most of the Gdańsk jazz festival live releases. Likes ribbons, dislikes click tracks.', fontSize='small'))),
        (None, J(image('piano.jpg', 'Black and white photo of a man in a suit playing an upright piano, seen from behind', lightbox=False, aspectRatio='4/5', scale='cover'),
                 heading('Bartek Szulc', 4), para('Engineer and drum tech. Twelve years at Polish Radio. Does the tuning on every kit that comes in, including yours.', fontSize='small'))),
        (None, J(image('engineer.jpg', 'Close-up of a small analogue mixing desk with rows of faders and lit buttons', lightbox=False, aspectRatio='4/5', scale='cover'),
                 heading('Iga Dąbrowska', 4), para('Assistant engineer and our mastering room on Thursdays. Runs the rehearsal room bookings.', fontSize='small'))),
        align='wide')), align='wide', layout={'type': 'default'}))

pattern('credits-list', 'Recent credits', 'text', J(
    heading('Recorded here recently', 3),
    table([['Rzeka', '<em>Ujście</em>', 'LP, Nowy Świat Dźwięku', '2026'], ['Gdańsk Chamber Choir', '<em>Kolędy z Oliwy</em>', 'CD', '2025'],
           ['Mała Orkiestra Portowa', '<em>Doki</em>', 'LP', '2025'], ['Teatr Wybrzeże', '<em>Burza</em>, stage music', 'Soundtrack', '2024']],
          head=['Artist', 'Title', 'Format', 'Year'])))

pattern('sessions-grid', 'Recent sessions (posts)', 'query', group(J(
    row(J(heading('Recent sessions', 2), para('<a href="/sessions/">All sessions</a>')), justify='space-between', align='wide', style={'spacing': {'margin': {'bottom': 'var:preset|spacing|40'}}}),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover'), dyn('post-date', format='F Y'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=22)),
          per_page=3, query_id=31, align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '18rem'})),
    align='wide', layout={'type': 'default'}))
pattern('sessions-archive', 'Sessions (inherits the page query)', 'query', inherit_query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover'), dyn('post-date', format='F Y'), dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', moreText='', excerptLength=30)),
    align='wide', layout={'type': 'grid', 'columnCount': 2, 'minimumColumnWidth': '20rem'}), inserter=False)
pattern('post-list', 'Post list', 'query', inherit_query(J(dyn('post-date', format='j F Y'), dyn('post-title', isLink=True, level=2, fontSize='x-large')), align='wide'), inserter=False)

pattern('load-in', 'Load-in, parking and getting here', 'contact', cols(
    ('45%', image('shipyard.jpg', 'View over the old Gdańsk shipyard with cranes along the water and brick halls', 'Hala 3 is the long brick hall on the right, by the blue crane', lightbox=False)),
    (None, J(heading('Getting here and loading in', 3),
             table([['Address', 'Hala 3, ul. Narzędziowców 9, 80-863 Gdańsk'], ['Tram', '8 or 10 to Stocznia SKM, then 6 minutes on foot'],
                    ['Parking', 'Two spaces for vans at the loading door, free. Cars park on ul. Popiełuszki, 4 zł an hour'],
                    ['Load-in', 'Ground floor, double doors 2.4 m wide, no steps. The trolley is by the door'],
                    ['Hardware shop', 'Castorama on ul. Kartuska, 12 minutes by car, open till 21:00'],
                    ['Food', 'Pierogarnia Stary Młyn delivers to the hall. Menu on the fridge']]),
             para('The hall is cold in winter until the heating catches up. Bring a jumper for the first hour.', fontSize='small', className='has-muted-color'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('rehearsal-room', 'Rehearsal room', 'text', cols(
    (None, image('amp.jpg', 'A Fender Champion guitar amp with its control knobs, close up', lightbox=False, aspectRatio='4/3', scale='cover')),
    (None, J(heading('Rehearsal room', 3), para('30 m², a house kit, two guitar amps, a bass amp and a PA with four mics. 60 zł an hour, three hours minimum at weekends. Book by text on +48 600 555 219, Iga answers.'),
             para('Bands who rehearse here get 10% off a recording day in Studio A.', className='is-style-lead'))), align='wide', verticalAlignment='center'))

pattern('client-quotes', 'Client quotes (named)', 'testimonials', cols(
    (None, quote('We tracked the whole record live in three days, drums in the room with everyone. Bartek tuned my snare better than I ever have.', 'Ola Kruk, drummer, Rzeka, 2026')),
    (None, quote('Thirty-two singers and the room still had space. The plate reverb next door is on every track.', 'Paweł Sowa, conductor, Gdańsk Chamber Choir')), align='wide',
    style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('studio-numbers', 'Room specs table', 'text', table([
    ['Live room', '64 m², 7 m ceiling, three isolation booths (6, 8 and 9 m²)'], ['Control room A', '28 m², window into the live room and booths'],
    ['Studio B', '22 m², treated for mixing'], ['Rehearsal room', '30 m², separate entrance from the yard'], ['Power', 'Isolated technical earth, 3-phase for touring rigs']]))

pattern('studio-a-page', 'Page: Studio A', 'featured', J(
    image('console.jpg', 'Studio A control room with the console, five monitors and acoustic panels', lightbox=False, align='wide', aspectRatio='21/9', scale='cover'),
    para('The live room was a shipyard tool store until 2016. We kept the brick and the height, built three booths along one wall, and hung clouds from the roof beams. Bands set up in a circle and can see each other and the control room.', className='is-style-lead'),
    pattern_ref('studio-numbers'),
    image('drums.jpg', 'A drum kit in the live room, seen from above', 'The house kit, a Ludwig Classic Maple, set up for the Rzeka sessions', lightbox=False),
    pattern_ref('rates-table')), block_types='core/post-content')
pattern('studio-b-page', 'Page: Studio B', 'featured', J(
    image('band.jpg', 'Studio B with two monitors, a keyboard and outboard gear on a wall of acoustic foam', lightbox=False, align='wide', aspectRatio='21/9', scale='cover'),
    para('Studio B is where records get mixed. It is small and quiet, with a 16-channel summing desk and a sofa at the back that is exactly the right distance from the speakers.', className='is-style-lead'),
    table([['Desk', 'SSL XLogic X-Desk'], ['Monitors', 'ATC SCM25A, Yamaha NS-10M, one Auratone'], ['Vocal booth', '4 m², window to the desk']]),
    pattern_ref('rates-table')), block_types='core/post-content')
pattern('page-rooms', 'Page: rooms', 'featured', J(pattern_ref('rooms-signal'), pattern_ref('rehearsal-room'), pattern_ref('studio-numbers')), block_types='core/post-content')
pattern('page-gear', 'Page: gear', 'featured', J(pattern_ref('gear-inventory')), block_types='core/post-content')
pattern('page-rates', 'Page: rates and booking', 'featured', J(cols((None, pattern_ref('rates-table')), ('38%', pattern_ref('deposit-terms')), align='wide'), pattern_ref('booking-enquiry')), block_types='core/post-content')
pattern('page-engineers', 'Page: engineers', 'about', J(pattern_ref('engineers'), pattern_ref('credits-list'), pattern_ref('client-quotes')), block_types='core/post-content')
pattern('page-visit', 'Page: visit', 'contact', J(pattern_ref('load-in'), pattern_ref('rehearsal-room')), block_types='core/post-content')

# ------------------------------------------------------------------ templates
main_pad = {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}
def tpl(main, pad=True):
    return J(template_part('header', 'header'), group(main, tag='main', style=main_pad if pad else {'spacing': {'padding': {'top': 'var:preset|spacing|40'}}}), template_part('footer', 'footer'))
gap = lambda x, cls=None, sz='80': group(x, align='wide' if cls is None else 'full', className=cls, layout={'type': 'default'} if cls is None else {'type': 'constrained'},
                                        style={'spacing': {'margin': {'top': 'var:preset|spacing|' + sz}}})
write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('hero-collage'),
    gap(pattern_ref('intro-lead'), sz='70'),
    group(pattern_ref('rooms-signal'), align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|80'}}}),
    template_part('next-dates'),
    gap(pattern_ref('gear-categories'), sz='70'),
    gap(cols((None, pattern_ref('rates-table')), ('38%', pattern_ref('deposit-terms')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}), sz='70'),
    gap(pattern_ref('engineers')),
    gap(pattern_ref('sessions-grid')),
    gap(pattern_ref('client-quotes'), sz='70'),
    group(pattern_ref('booking-enquiry'), align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|80'}}})),
    tag='main', style={'spacing': {'padding': {'top': 'var:preset|spacing|40'}}}), template_part('footer', 'footer')))

write('templates/home.html', tpl(J(heading('Sessions', 1, align='wide'), para('What has been recorded, mixed and rehearsed here lately, with the gear we used.', className='is-style-lead', align='wide'), pattern_ref('sessions-archive'))))
write('templates/archive.html', tpl(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('sessions-archive'))))
write('templates/index.html', tpl(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list'))))
write('templates/search.html', tpl(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, buttonText='Search', placeholder='A band, a microphone, a date', align='wide'), pattern_ref('post-list'))))
write('templates/404.html', tpl(J(heading('Nothing on this channel', 1), para('That page is not here. The rooms, gear and rates are one click away.', className='is-style-lead'),
    dyn('search', label='Search', showLabel=False, buttonText='Search'), buttons(('See the rooms', '/rooms/')))))
write('templates/page.html', tpl(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', tpl(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1360px'}))))
write('templates/page-room.html', tpl(J(dyn('post-title', level=1, align='wide', fontSize='display'), dyn('post-content', align='wide', layout={'type': 'constrained'}))))
write('templates/single.html', tpl(J(
    group(J(dyn('post-date', format='F Y'), dyn('post-title', level=1, fontSize='xx-large')), align='wide', layout={'type': 'default'}),
    dyn('post-featured-image', align='wide', aspectRatio='21/9', scale='cover'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Earlier session', showTitle=True), dyn('post-navigation-link', label='Later session', showTitle=True)), justify='space-between'),
          className='is-style-rule-top', align='wide'))))

# ------------------------------------------------------------------ demo content
def sess(p1, rows):
    return J(para(p1), table(rows))
posts = [
    {'title': 'Rzeka, four days live in Studio A', 'category': 'sessions', 'image': 'drums.jpg', 'excerpt': 'Six players in the room, no click, three Coles ribbons on the kit. The album is out in spring.',
     'content': sess('Rzeka tracked their third album live, all six of them in the room at once, with the singer in booth 2. Bartek miked the kit with a pair of Coles 4038s and a Tonsil MD 263 on the kick, which nobody believed would work.', [['Room', 'Studio A'], ['Days', '4 tracking, 3 mixing in Studio B'], ['Engineer', 'Marta Kołodziej'], ['Tape', 'Two reels on the Studer, then Pro Tools']])},
    {'title': 'Gdańsk Chamber Choir, Christmas record', 'category': 'sessions', 'image': 'vocal.jpg', 'excerpt': 'Thirty-two singers, one pair of U 87s and the plate reverb next door.',
     'content': sess('Thirty-two singers stood in a horseshoe in the live room. We used a spaced pair of U 87s and almost nothing else, and sent a little to the EMT plate in the old paint store.', [['Room', 'Studio A'], ['Days', '2'], ['Engineer', 'Bartek Szulc']])},
    {'title': 'Mixing Doki for Mała Orkiestra Portowa', 'category': 'sessions', 'image': 'band.jpg', 'excerpt': 'Eleven songs mixed in Studio B through the X-Desk, with a half-inch copy for the vinyl cut.',
     'content': sess('The band recorded at home and brought us 11 songs to mix. Iga ran everything through the X-Desk and printed a half-inch copy on the Otari for the vinyl master.', [['Room', 'Studio B'], ['Days', '6'], ['Engineer', 'Iga Dąbrowska']])},
    {'title': 'Burza, stage music for Teatr Wybrzeże', 'category': 'sessions', 'image': 'piano.jpg', 'excerpt': 'Prepared piano, a string quartet and a lot of thunder sheet.',
     'content': sess('Music for a new production of The Tempest. Prepared piano on the C7, a string quartet, and a thunder sheet borrowed from the theatre that was louder than anything else we have recorded.', [['Room', 'Studio A'], ['Days', '3'], ['Engineer', 'Marta Kołodziej']])},
    {'title': 'New tape machine, same old tape', 'category': 'news', 'image': 'tape.jpg', 'excerpt': 'The Studer is back from service with new heads. Tape prices went up again.',
     'content': sess('The Studer A827 is back from two months at the service shop in Łódź, with new heads and a lot of cleaning. A reel of 2 inch tape now costs 1,150 zł, so most bands record to tape for the basic tracks and then move to Pro Tools. You are welcome to bring your own reels.', [['Turnaround', 'We need a week to align it for a new tape formula']])},
    {'title': 'Rehearsal room open on Sundays', 'category': 'news', 'image': 'amp.jpg', 'excerpt': 'From October the rehearsal room opens Sundays 12:00 to 22:00.',
     'content': sess('From October the rehearsal room is open on Sundays too, 12:00 to 22:00. Book by text with Iga. Three hours minimum at weekends.', [['Price', '60 zł an hour'], ['Book', '+48 600 555 219, by text']])},
]
content = {
    'site': {'title': 'Dźwig', 'tagline': 'Recording studio in the old Gdańsk shipyard'},
    'categories': [{'slug': 'sessions', 'name': 'Sessions'}, {'slug': 'news', 'name': 'News'}],
    'front_page': 'home', 'posts_page': 'sessions',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'rooms', 'title': 'Rooms', 'pattern': 'booth/page-rooms', 'template': 'page-wide'},
        {'slug': 'studio-a', 'title': 'Studio A', 'parent': 'rooms', 'pattern': 'booth/studio-a-page', 'template': 'page-room'},
        {'slug': 'studio-b', 'title': 'Studio B', 'parent': 'rooms', 'pattern': 'booth/studio-b-page', 'template': 'page-room'},
        {'slug': 'gear', 'title': 'Gear', 'pattern': 'booth/page-gear', 'template': 'page-wide'},
        {'slug': 'rates', 'title': 'Rates', 'pattern': 'booth/page-rates', 'template': 'page-wide'},
        {'slug': 'engineers', 'title': 'Engineers', 'pattern': 'booth/page-engineers', 'template': 'page-wide'},
        {'slug': 'sessions', 'title': 'Sessions', 'content': ''},
        {'slug': 'visit', 'title': 'Visit', 'pattern': 'booth/page-visit', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Rooms', 'url': '/rooms/'}, {'label': 'Gear', 'url': '/gear/'}, {'label': 'Rates', 'url': '/rates/'},
            {'label': 'Engineers', 'url': '/engineers/'}, {'label': 'Sessions', 'url': '/sessions/'}, {'label': 'Visit', 'url': '/visit/'}],
}
os.makedirs('demos/booth', exist_ok=True)
json.dump(content, open('demos/booth/content.json', 'w'), indent=1, ensure_ascii=False)
open('demos/booth/fonts-claim.txt', 'w').write('display: Figtree\n')
print('booth built')

# ====================================================================== ROUND 2
# Owner's review: fewer tables, lightbox on, 40+ patterns, no table on the home page, the demo uses the kit.
# Sections studied on studionagrywarka.pl (big headline, room pages, services), Electrical Audio (rates, policies,
# gear, text list), The Bunker (room gear), Tarbox Road (discography) and Abbey Road (packages, FAQ, getting here).
theme['settings']['blocks'] = {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}}
theme['styles']['css'] += ('.is-style-defs>.wp-block-group{border-top:1px solid color-mix(in srgb,currentColor 35%,transparent);padding:.65em 0;gap:.3rem 1.5rem;margin:0!important}'
                           '.is-style-defs>.wp-block-group:last-child{border-bottom:1px solid color-mix(in srgb,currentColor 35%,transparent)}.is-style-defs p{margin:0}'
                           '.is-style-defs>.wp-block-group>p:first-child{flex:0 0 10rem;font-weight:700}.is-style-defs>.wp-block-group>p:nth-child(2){flex:1 1 14rem}'
                           '.is-style-price-card{display:flex;flex-direction:column;gap:.5rem}.is-style-price-card .is-style-big-price{font-family:var(--wp--preset--font-family--display);font-weight:900;font-size:var(--wp--preset--font-size--xx-large);letter-spacing:-.03em;line-height:1;margin:0}')
wjson('theme.json', theme)

def defs(data):
    return group(J(*[row(J(*[para(c) for c in r]), wrap=True) for r in data]), className='is-style-defs', layout={'type': 'default'})

room_block = lambda img, alt, name, size, desc, rows_, link: J(
    image(img, alt, aspectRatio='4/3', scale='cover'),
    heading(name, 3), para(size, className='is-style-room-tag'), para(desc), defs(rows_), buttons(('Look inside ' + name, link)))
pattern('rooms-signal', 'Rooms on a record-light block', 'featured', group(J(
    heading('Two rooms and a rehearsal space', 2, align='wide'),
    cols(
        (None, room_block('hero.jpg', 'Studio A control room with a wooden ceiling, leather chairs and the console in front of a window into the live room', 'Studio A', '64 m² live room, 7 m ceiling',
                          'Tracking room with three isolation booths and a Yamaha C7 grand. The control room looks into all of it.',
                          [['Console', 'Neve-style 32-channel, rebuilt 2021'], ['Tape', 'Studer A827 24-track, 2 inch'], ['Day, engineer', '2,400 zł']], '/rooms/studio-a/')),
        (None, room_block('band.jpg', 'Studio B: two monitors, a keyboard and outboard gear against a wall of black acoustic foam', 'Studio B', '22 m² mix room',
                          'Mixing, overdubs and vocals. Treated for mixing first, so it is quiet and a bit dead to sing in, on purpose.',
                          [['Desk', 'SSL XLogic X-Desk, 16 channels'], ['Monitors', 'ATC SCM25A, Yamaha NS-10M'], ['Day, engineer', '1,100 zł']], '/rooms/studio-b/')),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    className='is-style-signal', align='full', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))
pattern('studio-numbers', 'Room specs', 'rooms', defs([
    ['Live room', '64 m², 7 m ceiling, three isolation booths (6, 8 and 9 m²)'], ['Control room A', '28 m², window into the live room and booths'],
    ['Studio B', '22 m², treated for mixing'], ['Rehearsal room', '30 m², separate entrance from the yard'], ['Power', 'Isolated technical earth, 3-phase for touring rigs']]))
pattern('load-in', 'Load-in, parking and getting here', 'contact', cols(
    ('45%', image('shipyard.jpg', 'View over the old Gdańsk shipyard with cranes along the water and brick halls', 'Hala 3 is the long brick hall on the right, by the blue crane')),
    (None, J(heading('Getting here and loading in', 3),
             defs([['Address', 'Hala 3, ul. Narzędziowców 9, 80-863 Gdańsk'], ['Tram', '8 or 10 to Stocznia SKM, then 6 minutes on foot'],
                   ['Parking', 'Two spaces for vans at the loading door, free. Cars park on ul. Popiełuszki, 4 zł an hour'],
                   ['Load-in', 'Ground floor, double doors 2.4 m wide, no steps. The trolley is by the door'],
                   ['Hardware', 'Castorama on ul. Kartuska, 12 minutes by car, open till 21:00'], ['Food', 'Pierogarnia Stary Młyn delivers to the hall. Menu on the fridge']]),
             para('The hall is cold in winter until the heating catches up. Bring a jumper for the first hour.', fontSize='small', className='has-muted-color'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))
pattern('studio-b-page', 'Page: Studio B', 'rooms', J(
    image('band.jpg', 'Studio B with two monitors, a keyboard and outboard gear on a wall of acoustic foam', align='wide', aspectRatio='21/9', scale='cover'),
    para('Studio B is where records get mixed. It is small and quiet, with a 16-channel summing desk and a sofa at the back that is exactly the right distance from the speakers.', className='is-style-lead'),
    defs([['Desk', 'SSL XLogic X-Desk'], ['Monitors', 'ATC SCM25A, Yamaha NS-10M, one Auratone'], ['Vocal booth', '4 m², window to the desk']]),
    pattern_ref('rate-cards')), block_types='core/post-content')
CREDITS = [('Rzeka', 'Ujście', 'LP, 2026', 'drums.jpg'), ('Gdańsk Chamber Choir', 'Kolędy z Oliwy', 'CD, 2025', 'vocal.jpg'),
           ('Mała Orkiestra Portowa', 'Doki', 'LP, 2025', 'band.jpg'), ('Teatr Wybrzeże', 'Burza, stage music', '2024', 'piano.jpg'),
           ('Hania Sokół', 'Wolska 40, mastering', '12", 2026', 'engineer.jpg'), ('Ola Kruk', 'Solo drums', 'Cassette, 2024', 'tape.jpg')]
pattern('credits-list', 'Recorded here: cover grid', 'portfolio', J(
    heading('Recorded here recently', 3),
    group(J(*[group(J(image(img, 'Photo from the %s session' % a, aspectRatio='1', scale='cover'), heading(t, 5), para('%s. %s' % (a, f), fontSize='small', className='has-muted-color')),
                    layout={'type': 'flex', 'orientation': 'vertical'}, style={'spacing': {'blockGap': 'var:preset|spacing|10'}}) for a, t, f, img in CREDITS]),
          layout={'type': 'grid', 'columnCount': 6, 'minimumColumnWidth': '10rem'})))

# ---- new patterns
def price_card(name, price, note, link, cls='is-style-panel'):
    return group(J(heading(name, 4), para(price, className='is-style-big-price'), para(note, fontSize='small'), buttons(('Book ' + name, link))), className=cls + ' is-style-price-card', layout={'type': 'default'})
pattern('rate-cards', 'Rates as cards', 'pricing', cols(
    (None, price_card('Studio A', '2,400 zł', 'A 10-hour day with an engineer. 1,600 zł without. Half day 1,300 zł.', '/rates/#booking')),
    (None, price_card('Studio B', '1,100 zł', 'A 10-hour day with an engineer. 700 zł without. Half day 600 zł.', '/rates/#booking')),
    (None, price_card('Rehearsal', '60 zł', 'An hour, no engineer. Three hours minimum at weekends.', '/visit/')),
    align='wide'))
PACKS = [('One song in a day', '2,900 zł', 'Studio A for ten hours, tracked live, mixed in Studio B the next morning. For a single or a session video.'),
         ('EP weekend', '6,200 zł', 'Saturday and Sunday in Studio A, one day of mixing, four songs. Tape is extra.'),
         ('Album fortnight', 'From 21,000 zł', 'Ten days tracking, four days mixing, a room to sleep in upstairs if you are from out of town.')]
pattern('packages', 'Session packages', 'pricing', J(heading('Packages', 2),
    cols(*[(None, group(J(heading(n, 4), para(p, className='is-style-big-price'), para(d, fontSize='small')), className='is-style-panel is-style-price-card', layout={'type': 'default'})) for n, p, d in PACKS], align='wide'),
    para('Every package includes the piano, the house kit and our engineers. Prices include VAT.', fontSize='small')))
SERV = [('Recording', 'Bands tracked live in Studio A, overdubs in B. Tape or Pro Tools, usually both.'), ('Mixing', 'In Studio B, on the X-Desk, with recalls free for a month.'),
        ('Mastering', 'Thursdays with Iga. 250 zł a track, 1,800 zł an album, one round of changes.'), ('Live session videos', 'Four cameras, multitrack audio, edited in a week. From 3,500 zł.'),
        ('Rehearsal', 'By the hour, with a house kit and a PA. Book by text.')]
pattern('services', 'Services list', 'services', J(heading('What we do', 2),
    group(J(*[row(J(heading(n, 3, fontSize='large'), para(d)), wrap=True) for n, d in SERV]), className='is-style-defs', layout={'type': 'default'})))
pattern('live-session', 'Live session video', 'media', cols(
    ('62%', embed('https://www.youtube.com/watch?v=dzwig-session-rzeka', provider='youtube', type_='video')),
    (None, J(heading('Dźwig sessions', 3), para('One band, one take, four cameras in the live room. Rzeka played Ujście for us the day after they finished the album.'),
             para('<a href="/sessions/">All sessions</a>'))), align='wide', verticalAlignment='center'))
pattern('booking-faq', 'Booking questions', 'services', J(heading('Questions bands ask', 2),
    details('Can we use our own engineer?', para('Yes. Book a day without an engineer and one of us stays in the building to help with the patchbay and the tape machine.')),
    details('Can we leave gear overnight?', para('Yes, in the live room, on a booking that runs over several days. The hall is alarmed and insured.')),
    details('Do you have somewhere to sleep?', para('One room upstairs with four beds, 120 zł a night for the room. Otherwise the Hotel Stocznia is a five-minute walk.')),
    details('How do we pay?', para('A 30% deposit by bank transfer, the rest on the last day, by card or transfer.'))))
pattern('what-to-bring', 'What to bring', 'services', group(J(heading('What to bring', 4), lst([
    'New strings, fitted two days before, not the morning of', 'Drum heads if yours are older than the last tour', 'Your own sticks, picks and cables you trust',
    'Lyrics printed out, for the singer and for us', 'A hard drive if you want to take the multitracks home']), para('We have tea, coffee and a kettle. Bring your own milk if you are fussy.', fontSize='small')), className='is-style-panel'))
pattern('gear-story', 'One piece of gear, told properly', 'rooms', cols(
    (None, image('console.jpg', 'The control room console with speakers and acoustic panels', 'The console in 2021, the week it came back from Szczecin')),
    (None, J(heading('The console from Polish Radio', 3),
             para('It was built in 1979 for studio S1 at Polish Radio Szczecin and ran live broadcasts until 2009. We bought it for the price of scrap, then Tonmeister Szczecin spent eight months rebuilding every channel.'),
             para('It has 32 channels of 1084-style EQ, and a talkback microphone that still says "Radio Szczecin" on the switch.', className='is-style-lead'))), align='wide', verticalAlignment='center'))
pattern('room-gallery', 'Room photos', 'gallery', gallery([
    ('console.jpg', 'The Studio A control room with a large console and speakers', 'Studio A control room'), ('drums.jpg', 'A drum kit seen from above', 'The house kit in the live room'),
    ('vocal.jpg', 'A large-diaphragm microphone with a pop filter', 'Booth 2'), ('tape.jpg', 'A reel-to-reel tape deck in the dark', 'The Otari'),
    ('engineer.jpg', 'A small mixing desk with lit buttons', 'Studio B desk'), ('amp.jpg', 'A Fender guitar amp close up', 'Rehearsal room')], columns=3, align='wide'))
pattern('quote-big', 'One big client quote', 'testimonials', pullquote('The room sounds like a room. That is harder to find than it should be.', 'Paweł Sowa, conductor, Gdańsk Chamber Choir'))
pattern('opening-hours', 'Office hours and contact card', 'contact', group(J(heading('The office', 4), defs([
    ['Phone', '+48 58 555 01 90'], ['Hours', 'Monday to Friday, 10:00 to 18:00'], ['Email', '<a href="mailto:studio@example.com">studio@example.com</a>'],
    ['Sessions', 'Any day, 10:00 to 20:00, longer by arrangement']])), className='is-style-panel'))
pattern('travel-options', 'Getting here by train, tram or van', 'contact', cols(
    (None, J(heading('By train', 4), para('Gdańsk Główny is 15 minutes on foot, or two stops to Stocznia on the SKM.'))),
    (None, J(heading('By tram', 4), para('Lines 8 and 10 to Stocznia SKM, then 6 minutes towards the cranes.'))),
    (None, J(heading('By van', 4), para('From the S7, exit Gdańsk Centrum, then follow ul. Popiełuszki to the red gate. Two spaces at the loading door.'))), align='wide'))
pattern('stay-nearby', 'Staying nearby', 'contact', group(J(heading('If you are from out of town', 4),
    para('We have one room upstairs with four beds, 120 zł a night for the room, and a kitchen. Hotel Stocznia on ul. Jana z Kolna is a five-minute walk and gives bands 15% off if you say Dźwig.', fontSize='small')), className='is-style-panel'))
pattern('mastering', 'Mastering', 'services', cols(
    ('40%', image('engineer.jpg', 'Close-up of a small mixing desk with rows of faders and lit buttons', aspectRatio='4/5', scale='cover')),
    (None, J(heading('Mastering on Thursdays', 3), para('Iga masters in Studio B every Thursday. Send us your mixes as 24-bit WAVs and a reference track you like. We send the masters back within a week.'),
             defs([['Single', '250 zł a track'], ['EP', '900 zł, up to five tracks'], ['Album', '1,800 zł, with a vinyl master']]),
             buttons(('Send mixes to Iga', 'mailto:iga@example.com?subject=Mastering')))), align='wide', verticalAlignment='center'))
pattern('hero-room', 'Hero: a room and one fact', 'hero', group(J(
    image('hero.jpg', 'Studio A control room with a wooden ceiling and the console facing the live room window', align='wide', aspectRatio='21/9', scale='cover'),
    row(J(heading('Studio A', 1), para('64 m², 7 metre ceiling, three booths, one grand piano', className='is-style-lead')), justify='space-between', align='wide')),
    align='wide', layout={'type': 'default'}))

# ---- pages that use the kit
pattern('page-rooms', 'Page: rooms', 'rooms', J(pattern_ref('rooms-signal'), pattern_ref('room-gallery'), pattern_ref('gear-story'), pattern_ref('rehearsal-room'), pattern_ref('studio-numbers')), block_types='core/post-content')
pattern('page-rates', 'Page: rates and booking', 'pricing', J(cols((None, pattern_ref('rates-table')), ('38%', pattern_ref('deposit-terms')), align='wide'), pattern_ref('packages'), pattern_ref('booking-faq'), pattern_ref('booking-enquiry')), block_types='core/post-content')
pattern('page-services', 'Page: services', 'services', J(pattern_ref('services'), pattern_ref('mastering'), pattern_ref('live-session'), pattern_ref('what-to-bring')), block_types='core/post-content')
pattern('page-engineers', 'Page: engineers', 'about', J(pattern_ref('engineers'), pattern_ref('credits-list'), pattern_ref('quote-big'), pattern_ref('client-quotes')), block_types='core/post-content')
pattern('page-visit', 'Page: visit', 'contact', J(pattern_ref('load-in'), pattern_ref('travel-options'), cols((None, pattern_ref('opening-hours')), (None, pattern_ref('stay-nearby')), align='wide'), pattern_ref('rehearsal-room')), block_types='core/post-content')
pattern('studio-a-page', 'Page: Studio A', 'rooms', J(
    image('console.jpg', 'Studio A control room with the console, five monitors and acoustic panels', align='wide', aspectRatio='21/9', scale='cover'),
    para('The live room was a shipyard tool store until 2016. We kept the brick and the height, built three booths along one wall, and hung clouds from the roof beams. Bands set up in a circle and can see each other and the control room.', className='is-style-lead'),
    pattern_ref('studio-numbers'), pattern_ref('gear-story'),
    image('drums.jpg', 'A drum kit in the live room, seen from above', 'The house kit, a Ludwig Classic Maple, set up for the Rzeka sessions'),
    pattern_ref('rate-cards')), block_types='core/post-content')
pattern('page-studio-a-hero', 'Page: room with a big photo opening', 'rooms', J(pattern_ref('hero-room'), pattern_ref('studio-numbers'), pattern_ref('room-gallery')), block_types='core/post-content')

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('hero-collage'),
    gap(pattern_ref('intro-lead'), sz='70'),
    group(pattern_ref('rooms-signal'), align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|80'}}}),
    template_part('next-dates'),
    gap(pattern_ref('gear-categories'), sz='70'),
    gap(J(heading('Rates', 2), pattern_ref('rate-cards')), sz='70'),
    gap(pattern_ref('credits-list')),
    gap(pattern_ref('engineers')),
    gap(pattern_ref('sessions-grid')),
    gap(pattern_ref('quote-big'), sz='70'),
    group(pattern_ref('booking-enquiry'), align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|80'}}})),
    tag='main', style={'spacing': {'padding': {'top': 'var:preset|spacing|40'}}}), template_part('footer', 'footer')))

for p in content['posts']:
    if p['category'] == 'sessions':
        p['content'] = J(p['content'], gallery([(p['image'], 'Photo from the session: %s' % p['title'], 'On the day'), ('console.jpg', 'The Studio A control room', 'In the control room')], columns=2),
                         quote('We booked four days and finished in three. We used the fourth to play pool.', 'From the band, afterwards'))
content['posts'].append({'title': 'Ola Kruk, a solo drum record in one day', 'category': 'sessions', 'image': 'tape.jpg',
    'excerpt': 'Twelve improvisations on the house kit, straight to half-inch tape, no edits.',
    'content': J(para('Ola booked the "one song in a day" package and recorded twelve instead. Everything went straight to the Otari at 15 ips, no edits and no overdubs.'),
                 defs([['Room', 'Studio A'], ['Days', '1'], ['Engineer', 'Bartek Szulc'], ['Tape', 'One reel of half-inch']]),
                 gallery([('tape.jpg', 'A reel-to-reel tape deck in the dark', 'The Otari'), ('drums.jpg', 'A drum kit from above', 'The house kit')], columns=2))})
content['pages'].append({'slug': 'services', 'title': 'Services', 'pattern': 'booth/page-services', 'template': 'page-wide'})
content['nav'] = [{'label': 'Rooms', 'url': '/rooms/'}, {'label': 'Services', 'url': '/services/'}, {'label': 'Gear', 'url': '/gear/'}, {'label': 'Rates', 'url': '/rates/'},
                  {'label': 'Engineers', 'url': '/engineers/'}, {'label': 'Sessions', 'url': '/sessions/'}, {'label': 'Visit', 'url': '/visit/'}]
json.dump(content, open('demos/booth/content.json', 'w'), indent=1, ensure_ascii=False)
theme['styles']['blocks']['core/pullquote']['elements'] = {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontStyle': 'normal', 'fontWeight': '400', 'letterSpacing': '0', 'textTransform': 'none'}}}
theme['styles']['css'] += '.wp-block-pullquote{text-align:left;padding-left:0;padding-right:0}.wp-block-pullquote blockquote{margin:0}'
wjson('theme.json', theme)
print('booth round 2 built')
