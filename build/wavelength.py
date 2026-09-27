# wavelength: Calder Valley Radio 104.6 FM, a licensed local community station for Hebden Bridge and Todmorden.
# Direction: the second radio theme, deliberately unlike freq (a music station's Swiss index) and bpm (a DJ's night
#   archive). This is civic, warm, plain-language local radio: talk, news bulletins, a community noticeboard read
#   on air, and volunteer presenters. It reads like a good council leaflet: big answers first, large text, underlined
#   links, a bus-timetable schedule and a yellow noticeboard.
# Fonts: Parkinsans (display, claimed; designed for a health charity, friendly and very legible) and Atkinson
#   Hyperlegible Next for text at 19px, both chosen because a lot of the audience is over 65.
# Palette: warm paper #FFFBF0, moor green #1F3A2E, brick red #B83A1A for links and the dial needle, sun yellow
#   #F5C542 as a background only. Layout idea: an FM tuning dial across the top with the needle on 104.6.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('wavelength')
# Groups with padding/margin get their inline style (and anchors their id) written out, so the editor sees valid markup.
import blocks as _B
_orig_group = _B.group
def _css_var(v):
    return v.replace('var:preset|spacing|', 'var(--wp--preset--spacing--') + ')' if v.startswith('var:preset|spacing|') else v
def _group_inline(inner, tag='div', layout='constrained', **attrs):
    out = _orig_group(inner, tag=tag, layout=layout, **attrs)
    sp = (attrs.get('style') or {}).get('spacing') or {}
    decl = []
    for prop in ('padding', 'margin'):
        v = sp.get(prop)
        if isinstance(v, dict):
            for side in ('top', 'right', 'bottom', 'left'):
                if side in v:
                    decl.append('%s-%s:%s' % (prop, side, _css_var(v[side])))
    if attrs.get('anchor'):
        k = out.index('<%s class="' % tag)
        out = out[:k] + '<%s id="%s" class="' % (tag, attrs['anchor']) + out[k + len('<%s class="' % tag):]
    if decl:
        i = out.index(' class="', out.index('<%s ' % tag))
        j = out.index('>', i)
        out = out[:j] + ' style="%s"' % ';'.join(decl) + out[j:]
    return out
_B.group = _group_inline
group = _group_inline
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
    return '<!-- wp:columns%s -->\n<div class="%s">%s</div>\n<!-- /wp:columns -->' % ((' ' + json.dumps(a, separators=(',', ':'))) if a else '', ' '.join(filter(None, ['wp-block-columns', 'align' + a['align'] if a.get('align') else '', va, a.get('className', '')])), '\n\n'.join(out))

# ------------------------------------------------------------------ theme.json
F = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
display = next(f for f in F if f['slug'] == 'display')
body = next(f for f in F if f['slug'] == 'body')
PAL = [
    ('base', '#FFFBF0', 'Warm paper'),
    ('contrast', '#1F3A2E', 'Moor green'),
    ('accent', '#B83A1A', 'Brick red'),
    ('accent-2', '#F5C542', 'Sun yellow'),
    ('surface', '#F4EBD3', 'Noticeboard'),
    ('line', '#1F3A2E', 'Rule'),
    ('muted', '#52614F', 'Lichen'),
]
def palette(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '740px', 'wideSize': '1240px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True,
            'fontFamilies': [display, body],
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.9375rem', 'name': 'Small print', 'fluid': False},
                {'slug': 'small', 'size': '1.0625rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.3125rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.5rem', 'name': 'Title', 'fluid': {'min': '2.375rem', 'max': '3.5rem'}},
                {'slug': 'display', 'size': '5.25rem', 'name': 'Display', 'fluid': {'min': '2.875rem', 'max': '5.25rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 7rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': V('base'), 'text': V('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': V('accent')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': V('contrast')}},
                     ':focus': {'outline': {'color': V('contrast'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '1.08', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'fontWeight': '800', 'lineHeight': '1'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2', 'letterSpacing': '0'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'button': {'color': {'background': V('contrast'), 'text': V('base')},
                       'border': {'radius': '999px', 'width': '2px', 'style': 'solid', 'color': V('contrast')},
                       'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|medium'},
                       'spacing': {'padding': {'top': '0.7em', 'bottom': '0.7em', 'left': '1.4em', 'right': '1.4em'}},
                       ':hover': {'color': {'background': V('accent'), 'text': V('base')}, 'border': {'color': V('accent')}},
                       ':focus': {'outline': {'color': V('accent'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': V('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.1'},
                                'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': V('muted')}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '600'},
                                'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'}, 'color': {'text': V('muted')}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/post-featured-image': {'border': {'radius': '12px'}},
            'core/image': {'border': {'radius': '12px'}},
            'core/separator': {'color': {'text': V('line')}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '500', 'lineHeight': '1.35'},
                           'color': {'background': V('surface')}, 'border': {'radius': '12px'},
                           'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
                           'elements': {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontStyle': 'normal', 'fontWeight': '400'}}}},
            'core/pullquote': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '700'}, 'border': {'top': {'color': V('accent'), 'width': '4px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|medium'}},
            'core/details': {'border': {'bottom': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/list': {'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/search': {'border': {'radius': '999px'}},
        },
        'css': ('body{font-synthesis:none}:where(h1,h2,h3,h4){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                'a{text-underline-offset:.2em;text-decoration-thickness:2px}'
                '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.6em 1em .6em 0;text-align:left;vertical-align:top;font-variant-numeric:tabular-nums}'
                '.wp-block-table thead{border-bottom:3px solid var(--wp--preset--color--line)}.wp-block-table th{font-family:var(--wp--preset--font-family--display);font-weight:600}'
                '.wp-block-details summary{font-family:var(--wp--preset--font-family--display);font-weight:600;font-size:var(--wp--preset--font-size--large);cursor:pointer}'
                '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:999px;padding-left:1em;background:var(--wp--preset--color--base)}'
                '.wp-block-navigation .current-menu-item>a,.wp-block-navigation a[aria-current]{text-decoration:underline;text-decoration-thickness:3px;text-decoration-color:var(--wp--preset--color--accent)}'
                '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base)}'
                '@media (max-width:781px){.is-style-timetable td:nth-child(3){display:none}}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header with tuning dial'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'transmitter-notice', 'title': 'Transmitter work notice'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    ],
}
wjson('theme.json', theme)

write('style.css', '''/*
Theme Name: Wavelength
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A plain, large-print theme for local community FM stations with talk, news bulletins, a community noticeboard and volunteer presenters.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: wavelength
Tags: news, blog, entertainment, accessibility-ready, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks
*/''')

def variation(name, title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title}
    if pal:
        d['settings'] = {'color': {'palette': palette(pal)}}
    if extra:
        d.update(extra)
    wjson('styles/%s.json' % name, d)
variation('evening', 'Evening', [('base', '#16271F', 'Warm paper'), ('contrast', '#EFE6CF', 'Moor green'), ('accent', '#F5C542', 'Brick red'),
    ('accent-2', '#F5C542', 'Sun yellow'), ('surface', '#1F3A2E', 'Noticeboard'), ('line', '#EFE6CF', 'Rule'), ('muted', '#C3C9B8', 'Lichen')])
variation('mill-town', 'Mill town', [('base', '#F7F7F4', 'Warm paper'), ('contrast', '#22303A', 'Moor green'), ('accent', '#1F4E79', 'Brick red'),
    ('accent-2', '#9CC3D5', 'Sun yellow'), ('surface', '#E6E8E3', 'Noticeboard'), ('line', '#22303A', 'Rule'), ('muted', '#4F5A60', 'Lichen')])
variation('large-print', 'Large print', [('base', '#FFFFFF', 'Warm paper'), ('contrast', '#000000', 'Moor green'), ('accent', '#A12A0E', 'Brick red'),
    ('accent-2', '#FFD84D', 'Sun yellow'), ('surface', '#F2F2F2', 'Noticeboard'), ('line', '#000000', 'Rule'), ('muted', '#333333', 'Lichen')],
    {'settings': {'color': {'palette': palette([('base', '#FFFFFF', 'Warm paper'), ('contrast', '#000000', 'Moor green'), ('accent', '#A12A0E', 'Brick red'),
    ('accent-2', '#FFD84D', 'Sun yellow'), ('surface', '#F2F2F2', 'Noticeboard'), ('line', '#000000', 'Rule'), ('muted', '#333333', 'Lichen')])},
     'typography': {'fontSizes': [
        {'slug': 'x-small', 'size': '1.0625rem', 'name': 'Small print', 'fluid': False}, {'slug': 'small', 'size': '1.1875rem', 'name': 'Small', 'fluid': False},
        {'slug': 'medium', 'size': '1.375rem', 'name': 'Body', 'fluid': False}, {'slug': 'large', 'size': '1.75rem', 'name': 'Large', 'fluid': False},
        {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '2rem', 'max': '2.5rem'}},
        {'slug': 'xx-large', 'size': '3.75rem', 'name': 'Title', 'fluid': {'min': '2.75rem', 'max': '3.75rem'}},
        {'slug': 'display', 'size': '5.5rem', 'name': 'Display', 'fluid': {'min': '3.25rem', 'max': '5.5rem'}}]}}})

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('dial', 'Tuning dial', ['core/group'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
    'css': '&{position:relative;background-image:repeating-linear-gradient(to right,var(--wp--preset--color--base) 0 1px,transparent 1px 1%),repeating-linear-gradient(to right,var(--wp--preset--color--base) 0 2px,transparent 2px 5%);'
           'background-size:100% 10px,100% 18px;background-repeat:no-repeat;background-position:0 0,0 0}'
           '&::after{content:"";position:absolute;top:0;bottom:0;left:83%;width:4px;background:var(--wp--preset--color--accent-2)}& p{margin:0}'})
section('noticeboard', 'Noticeboard', ['core/group', 'core/column'], {
    'color': {'background': V('accent-2'), 'text': V('contrast')},
    'border': {'radius': '16px'},
    'elements': {'link': {'color': {'text': V('contrast')}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
    'css': '& .wp-element-button:hover{background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast);border-color:var(--wp--preset--color--base)}'})
section('notice-card', 'Pinned notice', ['core/group'], {
    'color': {'background': V('base'), 'text': V('contrast')},
    'border': {'radius': '6px', 'width': '2px', 'style': 'solid', 'color': V('contrast')},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
    'css': '& p{margin:0}& h4{margin:0 0 .3em}'})
section('green', 'Moor green block', ['core/group', 'core/column'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('accent-2')}}, 'heading': {'color': {'text': V('base')}}, 'caption': {'color': {'text': V('surface')}}, 'button': {'color': {'background': V('accent-2'), 'text': V('contrast')}, 'border': {'color': V('accent-2')}}},
    'css': '& .has-muted-color{color:var(--wp--preset--color--surface)!important}& .wp-block-table td,& .wp-block-table th,& .wp-block-table thead{border-color:var(--wp--preset--color--base)}'})
section('paper', 'Noticeboard paper', ['core/group', 'core/column'], {
    'color': {'background': V('surface'), 'text': V('contrast')},
    'border': {'radius': '16px'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('answer', 'Plain answer', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '500', 'lineHeight': '1.35'}})
section('timetable', 'Timetable', ['core/table'], {
    'css': '& td:first-child{font-family:var(--wp--preset--font-family--display);font-weight:700;width:5.5em;white-space:nowrap}& tr.is-now td,& td strong{color:var(--wp--preset--color--accent)}& td:last-child{color:var(--wp--preset--color--muted)}'})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': V('line'), 'width': '2px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})
section('red-bar', 'Red notice bar', ['core/group'], {
    'color': {'background': V('accent'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('base')}}},
    'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'}})

# ------------------------------------------------------------------ parts
dial = group(row(J(*[para(str(n)) for n in (88, 92, 96, 100, 104, 108)]), justify='space-between', wrap=False, align='full',
                 style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
             className='is-style-dial', align='full', layout={'type': 'constrained'})
write('parts/header.html', group(J(
    dial,
    row(J(stack(J(dyn('site-title', level=0), dyn('site-tagline')), style={'spacing': {'blockGap': '0'}}),
          dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}, overlayMenu='mobile')),
        justify='space-between', wrap=False, align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40'}}})),
    tag='header', align='full', layout={'type': 'constrained'}, style={'spacing': {'blockGap': '0'}}))
write('parts/transmitter-notice.html', pattern_ref('transmitter-notice'))
write('parts/footer.html', group(J(
    cols((None, J(heading('Calder Valley Radio', 4), para('104.6 FM in Hebden Bridge, Todmorden, Mytholmroyd and the tops. Online everywhere else. Run by 70 volunteers since 2011.', fontSize='small'))),
         (None, J(heading('Studio', 5), para('The Old Co-op, 22 Market Street<br>Hebden Bridge HX7 6AA<br>Studio: 01422 555 104<br>Text: 07700 900 104<br><a href="mailto:studio@example.com">studio@example.com</a>', fontSize='small'))),
         (None, J(heading('Useful', 5), para('<a href="/listen/">How to listen</a><br><a href="/noticeboard/">Send a notice</a><br><a href="/volunteer/">Volunteer</a><br><a href="/contact/">Complaints and corrections</a>', fontSize='small'))),
         align='wide'),
    para('Calder Valley Radio is a community radio station licensed by Ofcom (licence CR000123) and a registered charity (1150000). Demo photos are CC0 images from Wikimedia Commons, used as stand-ins.', align='wide', fontSize='x-small', className='has-muted-color')),
    tag='footer', align='full', className='is-style-green',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ------------------------------------------------------------------ patterns
pattern('dial-strip', 'Tuning dial strip', 'banner', dial, description='An FM scale from 88 to 108 with the needle on 104.6. Change the needle position in the section style CSS if your frequency is different.')

pattern('on-now', 'On now, next, and how to listen', 'featured', cols(
    ('60%', J(para('On now until 10am', className='is-style-answer', textColor='accent'),
              heading('The Valley Breakfast with Sue Whitaker and Ade Okoro', 1),
              para('Local news at 8 and 9, the roads and the weather at quarter past, and today Sue talks to the people running the Mytholmroyd flood defence consultation.', fontSize='large'),
              buttons(('Listen now online', 'https://stream.example.com/cvr'), ('Ring the studio: 01422 555 104', 'tel:01422555104', {'className': 'is-style-outline'})))),
    (None, J(heading('Three ways to listen', 4),
             lst(['Tune any FM radio to 104.6. It is strong in the valley bottom and weaker on the tops.', 'Press "Listen now online" on this page.', 'Ask a smart speaker to "play Calder Valley Radio".'], ordered=True),
             para('<a href="/listen/">Help with listening</a>')), {'className': 'is-style-paper'}),
    align='wide', verticalAlignment='top', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

TODAY = [('7am', 'The Valley Breakfast', 'Sue Whitaker and Ade Okoro'), ('10am', 'Local news, then The Morning Table', 'Mags Heywood, with a guest every day'),
         ('12pm', 'Lunchtime news and What\'s On', 'The news team'), ('1pm', 'Afternoon Music', 'Dev Patel, requests by text'),
         ('4pm', 'The School Run', 'Pupils from Calder High, Thursdays'), ('5pm', 'Noticeboard, then Teatime', 'Jo Lumb'),
         ('7pm', 'Calder Folk', 'Harry Greenwood'), ('9pm', 'Late Valley', 'Rotating volunteers'), ('11pm', 'Overnight music', 'No presenter')]
pattern('today-timetable', 'Today\'s programmes (timetable)', 'text', J(
    heading('On today, Thursday', 3),
    table([[t, '<strong>%s</strong>' % p if i == 0 else p, w] for i, (t, p, w) in enumerate(TODAY)], className='is-style-timetable'),
    para('The programme in red is on now. News is on the hour from 7am to 6pm, weekdays.', fontSize='small', textColor='muted')))

WEEK = {'Monday to Friday': [('7am', 'The Valley Breakfast'), ('10am', 'The Morning Table'), ('12pm', 'Lunchtime news and What\'s On'), ('1pm', 'Afternoon Music'), ('5pm', 'Noticeboard, then Teatime')],
        'Monday evening': [('7pm', 'Brass on a Monday, with Colin Firth (not that one)'), ('9pm', 'Late Valley')],
        'Tuesday evening': [('7pm', 'Town Hall Talk, live from Todmorden Town Hall on the first Tuesday'), ('9pm', 'Late Valley')],
        'Wednesday evening': [('7pm', 'Valley Voices, oral history from the Pennine Heritage archive'), ('8pm', 'Local bands, with Kirsty')],
        'Thursday evening': [('7pm', 'Calder Folk'), ('9pm', 'Late Valley')],
        'Friday evening': [('6pm', 'The Weekend Starts Here'), ('9pm', 'Northern soul, with Dave and Lynn')],
        'Saturday': [('9am', 'Garden Hour, with the allotment society'), ('11am', 'Sport, with results from the Calder Valley league'), ('2pm', 'Saturday Requests')],
        'Sunday': [('8am', 'Songs of Praise, from a different chapel each week'), ('10am', 'The Week in the Valley'), ('12pm', 'Sunday Lunch'), ('6pm', 'Talking Books, read by volunteers')]}
pattern('week-timetable', 'Week timetable', 'text', J(
    heading('The week', 2),
    *[details(day, table([list(r) for r in rows], className='is-style-timetable')) for day, rows in WEEK.items()],
    para('The weekday programmes run every weekday. Click a day to open it.', fontSize='small', textColor='muted')))

news_item = group(J(dyn('post-date', format='l j F, g:ia'), dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=30)),
                  className='is-style-rule-top', layout={'type': 'default'})
pattern('news-list', 'Local news (latest four)', 'query', group(J(
    heading('Local news', 2),
    query(news_item, per_page=4, query_id=51, layout={'type': 'grid', 'columnCount': 2, 'minimumColumnWidth': '18rem'}),
    para('<a href="/news/">All local news</a>')), align='wide', layout={'type': 'default'}))
pattern('news-archive', 'News (inherits the page query)', 'query', inherit_query(news_item, layout={'type': 'default'}), inserter=False)
pattern('post-list', 'Post list', 'query', inherit_query(news_item), inserter=False)

NOTICES = [('Lost: grey cat, Birchcliffe', 'Answers to Pickle. Microchipped. Ring Ann on 01422 555 381.'),
           ('Jumble sale, Saturday 10am', 'St James\' Church hall, Mytholmroyd. 20p entry, tea and cake.'),
           ('Road closed', 'Burnley Road at Callis Bridge, 9am to 3pm Tuesday, for gas works. Buses divert via Heptonstall Road.'),
           ('Free sandbags', 'From the Todmorden fire station yard, Mondays and Thursdays, 5pm to 7pm. Bring ID with your address.')]
pattern('noticeboard', 'Community noticeboard', 'featured', group(J(
    row(J(heading('Noticeboard', 2), para('We read these out at 9am and 5pm, Monday to Saturday.', fontSize='small')), justify='space-between'),
    group(J(*[group(J(heading(t, 4), para(b, fontSize='small')), className='is-style-notice-card', layout={'type': 'default'}) for t, b in NOTICES]),
          layout={'type': 'grid', 'columnCount': 2, 'minimumColumnWidth': '16rem'}),
    buttons(('Send us a notice', '/noticeboard/#send'))), className='is-style-noticeboard', align='wide', layout={'type': 'default'}),
    description='Notices read out on air. Keep them short: what, where, when, and a phone number.')

pattern('send-a-notice', 'How to send a notice', 'contact', group(J(
    heading('Send a notice', 3),
    para('Notices are free for anything not-for-profit in the valley. Keep it under 50 words and tell us who to ring.', className='is-style-answer'),
    lst(['Text it to 07700 900 104.', 'Email <a href="mailto:notices@example.com">notices@example.com</a>.', 'Put it through the letterbox at the Old Co-op, 22 Market Street.']),
    para('We read each notice for up to two weeks. We do not read adverts for businesses or anything to do with elections.', fontSize='small')),
    anchor='send', layout={'type': 'default'}))

pattern('volunteer-call', 'Volunteer: get on air', 'call-to-action', group(cols(
    ('55%', J(heading('Want to be on the radio?', 2),
              para('Most of our presenters had never touched a microphone before they came in. You do not need a good voice or any experience. You need two hours a week and a bit of patience with the desk.', fontSize='large'),
              buttons(('Come to a Tuesday open evening', '/volunteer/')))),
    (None, J(image('podcast.jpg', 'A young presenter in a white shirt and tie sitting in an armchair with a microphone in front of him', 'Kwame, 16, presents The School Run on Thursdays', lightbox=False, aspectRatio='4/5', scale='cover'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    className='is-style-green', align='full', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|70'}}}))

pattern('volunteer-roles', 'Volunteer roles and time needed', 'text', J(
    heading('What you could do', 3),
    table([['Presenter', 'A weekly or monthly programme', '2 to 4 hours a week'], ['Newsreader', 'Read the hourly bulletin, one morning a week', '3 hours a week'],
           ['Noticeboard', 'Answer the notices phone and type them up', '2 hours a week, from home'], ['Talking Books', 'Read a local book for Sunday evening', 'At your own pace'],
           ['Tech and transmitter', 'Look after the kit on Heptonstall Road', 'On call, one weekend a month'], ['Fundraising', 'Run the stall at the Hebden Bridge market', 'One Thursday a month']],
          head=['Role', 'What it involves', 'Time']),
    para('We pay travel expenses and there is always tea. Presenters need a DBS check for programmes with children, which we arrange and pay for.', fontSize='small')))

pattern('training-dates', 'Training and open evenings', 'text', group(J(
    heading('Open evenings', 4),
    table([['Tuesday 7 October', '7pm to 8.30pm', 'Look round the studio, meet presenters'], ['Tuesday 4 November', '7pm to 8.30pm', 'Same again'], ['Saturday 15 November', '10am to 4pm', 'First day of presenter training']]),
    para('Just turn up. The studio is on the first floor and there is a lift from the market side.', fontSize='small')), className='is-style-paper'))

PEOPLE = [('reading.jpg', 'A person reading a newspaper, face hidden behind the pages', 'Mags Heywood', 'The Morning Table, weekdays 10am. Retired teacher, reads every local paper so you do not have to.'),
          ('headphones.jpg', 'A woman with her hair in a bun, seen from behind, looking at a painting', 'Jo Lumb', 'Noticeboard and Teatime, weekdays 5pm. Knows everyone\'s cat.'),
          ('choir.jpg', 'A black and white photo of a large group singing from printed sheets', 'Harry Greenwood', 'Calder Folk, Thursdays 7pm. Sings with the Todmorden choir and will tell you about it.'),
          ('studio.jpg', 'A black and white photo of an old radio studio with a desk, chairs and a window into the control room', 'The news team', 'Six volunteers who write and read the hourly bulletin, from 6am.')]
pattern('presenters', 'Presenters', 'about', group(J(
    heading('Some of the people you hear', 2),
    group(J(*[group(J(image(img, alt, lightbox=False, aspectRatio='1', scale='cover'), heading(n, 4), para(d, fontSize='small')), layout={'type': 'flex', 'orientation': 'vertical'},
                    style={'spacing': {'blockGap': 'var:preset|spacing|20'}}) for img, alt, n, d in PEOPLE]),
          layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'})), align='wide', layout={'type': 'default'}))

pattern('programmes-list', 'Programmes list', 'text', J(
    heading('Programmes', 2),
    table([['The Valley Breakfast', 'Weekdays 7am', 'Local news, roads, weather and chat'], ['The Morning Table', 'Weekdays 10am', 'One guest from the valley every day'],
           ['Town Hall Talk', 'First Tuesday, 7pm', 'Live questions to councillors from Todmorden Town Hall'], ['Valley Voices', 'Wednesdays 7pm', 'Oral history from the Pennine Heritage archive'],
           ['Garden Hour', 'Saturdays 9am', 'The allotment society answers your questions'], ['Talking Books', 'Sundays 6pm', 'Local books read aloud by volunteers']],
          head=['Programme', 'When', 'What it is'])))

pattern('town-hall-talk', 'Town Hall Talk feature', 'featured', cols(
    ('50%', image('townhall.jpg', 'The ballroom of Todmorden Town Hall with a painted ceiling, tall windows and a wooden floor', 'Todmorden Town Hall, where Town Hall Talk goes out live', lightbox=False)),
    (None, J(heading('Town Hall Talk', 3),
             para('On the first Tuesday of the month we broadcast live from Todmorden Town Hall. Two councillors, one officer, and questions from whoever turns up or rings in. Nobody gets to make a speech.'),
             para('Next one: Tuesday 7 October, 7pm, on bin collections and the Walsden bus. Doors at 6.30pm, free, step-free entrance on Rochdale Road.'),
             buttons(('Send a question', 'mailto:studio@example.com?subject=Town%20Hall%20Talk')))), align='wide', verticalAlignment='center'))

pattern('listen-help', 'Help with listening (questions)', 'text', J(
    heading('Help with listening', 2),
    details('I can\'t get 104.6 FM in my house.', para('The signal comes from a mast on Heptonstall Road, so it is strong in the valley bottom and weak on the tops and behind Stoodley Pike. Try the radio near a window facing the valley, or listen online.')),
    details('Are you on DAB?', para('Not yet. DAB for small stations in the valley is planned for 2027. We will say on air when it happens.')),
    details('How do I listen on a smart speaker?', para('Say "play Calder Valley Radio". If it plays something else, say "play Calder Valley Radio on TuneIn".')),
    details('I missed a programme. Can I hear it again?', para('Most talk programmes go on the <a href="/news/">news and programmes page</a> the next day, for four weeks. Music programmes do not, because of music licences.')),
    details('My neighbour has no internet. Can they still listen?', para('Yes, on any FM radio. We have ten donated radios to lend. Ring the studio and a volunteer will bring one round.'))))

pattern('funding', 'How the station is paid for', 'text', group(J(
    heading('How we pay for it', 3),
    para('It costs about £24,000 a year to keep Calder Valley Radio on air. Nobody is paid. This is where the money comes from.', className='is-style-answer'),
    table([['Friends of the station, £3 a month', '£11,800'], ['Local adverts (up to 6 minutes an hour, Ofcom\'s limit)', '£6,200'], ['Grants from Calderdale Council and the National Lottery', '£4,500'], ['Market stall, quiz nights and the duck race', '£1,500']],
          head=['Where it comes from', 'Last year']),
    buttons(('Become a Friend for £3 a month', 'https://example.com/friends'))), className='is-style-paper'))

pattern('contact-us', 'Contact, complaints and corrections', 'contact', cols(
    (None, J(heading('Ring, text or call in', 3),
             table([['Studio phone', '01422 555 104, when we are live'], ['Text', '07700 900 104, read out on air if you like'], ['Email', '<a href="mailto:studio@example.com">studio@example.com</a>'], ['Post', 'The Old Co-op, 22 Market Street, Hebden Bridge HX7 6AA']]),
             para('The studio is open to visitors Monday to Friday, 9am to 1pm. First floor, lift from the market side.'))),
    (None, J(heading('Complaints and corrections', 3),
             para('If we got something wrong in the news, tell us and we will correct it on air in the next bulletin and on this website. Write to Rachel Sutcliffe, the station manager, at <a href="mailto:manager@example.com">manager@example.com</a>.'),
             para('If you are not happy with our answer, you can complain to Ofcom. We will tell you how.', fontSize='small'))), align='wide'))

pattern('transmitter-notice', 'Notice: transmitter work', 'banner', group(
    para('Transmitter work on Sunday 12 October: 104.6 FM will be off from 6am to about 11am. The online stream stays on.'),
    className='is-style-red-bar', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='Tell listeners when FM will be off, and when it comes back.')

pattern('local-music', 'Send us your music', 'call-to-action', group(J(
    heading('In a band in the valley?', 4),
    para('Kirsty plays local bands every Wednesday at 8pm. Send one song as an MP3 to <a href="mailto:music@example.com">music@example.com</a> with your band name, where you are from and when your next gig is.'),
    para('We only play music by people who live or gig in the Calder Valley.', fontSize='small')), className='is-style-paper'))

pattern('valley-photo', 'Valley photo with caption', 'media', image('canal.jpg', 'The Rochdale Canal in Hebden Bridge in summer, with narrowboats moored under trees and a stone bridge', 'The Rochdale Canal at Hebden Bridge. Our studio is two minutes up Market Street.', lightbox=False, align='wide', aspectRatio='21/9', scale='cover'))

pattern('page-listen', 'Page: how to listen', 'text', J(pattern_ref('on-now'), pattern_ref('listen-help')), block_types='core/post-content')
pattern('page-schedule', 'Page: schedule', 'text', J(pattern_ref('today-timetable'), pattern_ref('week-timetable')), block_types='core/post-content')
pattern('page-programmes', 'Page: programmes', 'text', J(pattern_ref('programmes-list'), pattern_ref('town-hall-talk'), pattern_ref('presenters')), block_types='core/post-content')
pattern('page-noticeboard', 'Page: noticeboard', 'text', J(pattern_ref('noticeboard'), pattern_ref('send-a-notice')), block_types='core/post-content')
pattern('page-volunteer', 'Page: volunteer', 'text', J(pattern_ref('volunteer-roles'), pattern_ref('training-dates'), pattern_ref('local-music')), block_types='core/post-content')
pattern('page-contact', 'Page: contact', 'contact', J(pattern_ref('contact-us'), pattern_ref('funding')), block_types='core/post-content')

# ------------------------------------------------------------------ templates
main_pad = {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}
def tpl(main, notice=False):
    return J(template_part('transmitter-notice') if notice else '', template_part('header', 'header'), group(main, tag='main', style=main_pad), template_part('footer', 'footer'))
sp = lambda x, sz='70': group(x, align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|' + sz}}})
write('templates/front-page.html', tpl(J(
    pattern_ref('on-now'),
    sp(cols((None, pattern_ref('today-timetable')), ('45%', pattern_ref('noticeboard')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    sp(pattern_ref('news-list')),
    group(pattern_ref('volunteer-call'), align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    sp(pattern_ref('town-hall-talk')),
    sp(pattern_ref('presenters')),
    sp(pattern_ref('valley-photo'), '60')), notice=True))
write('templates/home.html', tpl(J(heading('News and programmes', 1), para('Local news from the hourly bulletins, and talk programmes you can hear again for four weeks.', className='is-style-answer'), pattern_ref('news-archive'))))
write('templates/archive.html', tpl(J(dyn('query-title', type='archive', showPrefix=False), dyn('term-description'), pattern_ref('news-archive'))))
write('templates/index.html', tpl(J(dyn('query-title', type='archive'), pattern_ref('post-list'))))
write('templates/search.html', tpl(J(dyn('query-title', type='search'), dyn('search', label='Search this website', showLabel=True, buttonText='Search'), pattern_ref('post-list'))))
write('templates/404.html', tpl(J(heading('We can\'t find that page', 1), para('It may have moved, or the link may be wrong. You can search, or go back to the home page. If you were looking for something we said on air, ring the studio on 01422 555 104.', className='is-style-answer'),
    dyn('search', label='Search this website', showLabel=True, buttonText='Search'), buttons(('Go to the home page', '/')))))
write('templates/page.html', tpl(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', tpl(J(dyn('post-title', level=1, fontSize='xx-large', align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'}))))
write('templates/single.html', tpl(J(
    row(J(dyn('post-terms', term='category'), dyn('post-date', format='l j F Y, g:ia'))),
    dyn('post-title', level=1, fontSize='xx-large'),
    dyn('post-excerpt', moreText='', className='is-style-answer'),
    dyn('post-featured-image', aspectRatio='16/9', scale='cover'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(J(heading('Is this story about you?', 5), para('If something here is wrong, ring 01422 555 104 or email <a href="mailto:manager@example.com">manager@example.com</a> and we will correct it on air.', fontSize='small')), className='is-style-paper'),
    group(row(J(dyn('post-navigation-link', type='previous', label='Older', showTitle=True), dyn('post-navigation-link', label='Newer', showTitle=True)), justify='space-between'),
          className='is-style-rule-top'))))

# ------------------------------------------------------------------ demo content
def story(paras, audio_cap=None):
    out = [para(p) for p in paras]
    if audio_cap:
        out.insert(0, audio('https://stream.example.com/hear-again/%s.mp3' % audio_cap[0], caption=audio_cap[1]))
    return J(*out)
posts = [
    {'title': 'Flood defence drop-in moves to the Mytholmroyd Institute', 'category': 'news', 'image': 'canal.jpg',
     'excerpt': 'The Environment Agency drop-in on the new walls is now on Wednesday, 2pm to 7pm, at the Institute on Caldene Avenue.',
     'content': story(['The Environment Agency drop-in about the new flood walls along the Calder has moved to the Mytholmroyd Institute on Caldene Avenue. It is now on Wednesday 8 October, 2pm to 7pm.',
                       'The plans show a wall of up to 1.4 metres along Burnley Road. Engineers will be there to answer questions. You can also see the plans at Hebden Bridge library.',
                       'Sue Whitaker talked to two of the engineers on The Valley Breakfast on Thursday. That interview is on the Hear again page for four weeks.'])},
    {'title': 'Hear again: Town Hall Talk on bins and the Walsden bus', 'category': 'programmes', 'image': 'townhall.jpg',
     'excerpt': 'Questions from the floor to two councillors and the head of waste services. 58 minutes.',
     'content': story(['Live from Todmorden Town Hall on the first Tuesday of September. Forty people came, and twelve rang in.', 'Most questions were about the change to fortnightly black bin collections and the 590 bus to Walsden, which is being cut back after 7pm.'],
                      ('town-hall-talk-september', 'Town Hall Talk, 2 September, 58 minutes'))},
    {'title': 'Hebden Bridge market moves to Thursdays and Saturdays only', 'category': 'news', 'image': 'market.jpg',
     'excerpt': 'The Wednesday market ends on 29 October. Traders say footfall has halved since the car park charges went up.',
     'content': story(['The Wednesday market in Hebden Bridge will stop at the end of October. It will still run on Thursdays and Saturdays, 9am to 4pm.', 'Traders told our news team that footfall on Wednesdays has halved since car park charges went up in the spring. The council says it will review the charges in January.'])},
    {'title': 'Hear again: Valley Voices, the mill girls of Walsden', 'category': 'programmes', 'image': 'choir.jpg',
     'excerpt': 'Recordings from the Pennine Heritage archive of women who worked at the Walsden cotton mills in the 1950s.',
     'content': story(['This week\'s Valley Voices uses recordings made in 1987 of women who worked at the Walsden cotton mills in the 1950s. They talk about the noise, the lunch breaks and the dances at the Co-op hall.'],
                      ('valley-voices-walsden', 'Valley Voices, 17 September, 55 minutes'))},
    {'title': 'Library opening hours cut on Mondays', 'category': 'news', 'image': 'library.jpg',
     'excerpt': 'Todmorden library will open at 1pm on Mondays from November, to save £9,000 a year.',
     'content': story(['From 3 November Todmorden library will open at 1pm on Mondays instead of 9.30am. Calderdale Council says this saves £9,000 a year. The Friends of Todmorden Library are collecting signatures against the change at the front desk.'])},
    {'title': 'We need newsreaders for the 7am bulletin', 'category': 'station', 'image': 'studio.jpg',
     'excerpt': 'Two of our early newsreaders are moving away. Training starts in November.',
     'content': story(['Two of our early-morning newsreaders are moving away this autumn, so we need people for the 7am and 8am bulletins, one morning a week.', 'You will be in the studio from 6am to write and read the bulletin. We train you. Come to the open evening on Tuesday 7 October, 7pm.'])},
    {'title': 'Hear again: Garden Hour on slugs and wet summers', 'category': 'programmes', 'image': 'moor.jpg',
     'excerpt': 'The allotment society on what to do after the wettest August since 2012.',
     'content': story(['The allotment society panel took calls about blight, slugs and what to plant after the wettest August since 2012. Joan from Charlestown recommends beer traps. Brian does not.'],
                      ('garden-hour-slugs', 'Garden Hour, 20 September, 1 hour'))},
    {'title': 'Free radios for people who cannot get online', 'category': 'station', 'image': 'radio.jpg',
     'excerpt': 'We have ten donated FM radios to lend. A volunteer will bring one round.',
     'content': story(['Listeners have donated ten FM radios. If you, or someone you know, cannot get online and has no radio, ring the studio on 01422 555 104 and a volunteer will bring one round and tune it in.'])},
]
content = {
    'site': {'title': 'Calder Valley Radio', 'tagline': '104.6 FM for Hebden Bridge, Todmorden and the tops'},
    'categories': [{'slug': 'news', 'name': 'Local news'}, {'slug': 'programmes', 'name': 'Hear again'}, {'slug': 'station', 'name': 'Station news'}],
    'front_page': 'home', 'posts_page': 'news',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'listen', 'title': 'How to listen', 'pattern': 'wavelength/page-listen', 'template': 'page-wide'},
        {'slug': 'schedule', 'title': 'Schedule', 'pattern': 'wavelength/page-schedule'},
        {'slug': 'programmes', 'title': 'Programmes', 'pattern': 'wavelength/page-programmes', 'template': 'page-wide'},
        {'slug': 'news', 'title': 'News', 'content': ''},
        {'slug': 'noticeboard', 'title': 'Noticeboard', 'pattern': 'wavelength/page-noticeboard', 'template': 'page-wide'},
        {'slug': 'volunteer', 'title': 'Volunteer', 'pattern': 'wavelength/page-volunteer'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'wavelength/page-contact', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Listen', 'url': '/listen/'}, {'label': 'Schedule', 'url': '/schedule/'}, {'label': 'Programmes', 'url': '/programmes/'},
            {'label': 'News', 'url': '/news/'}, {'label': 'Noticeboard', 'url': '/noticeboard/'}, {'label': 'Volunteer', 'url': '/volunteer/'}, {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/wavelength', exist_ok=True)
json.dump(content, open('demos/wavelength/content.json', 'w'), indent=1, ensure_ascii=False)
open('demos/wavelength/fonts-claim.txt', 'w').write('display: Parkinsans\n')
print('wavelength built')
