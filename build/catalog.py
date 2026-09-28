# catalog: Hiss Tapes, a cassette label in Leith.
# Direction: the site is laid out like a cassette J-card. Every release has a spine (cat no, artist, title
#   running up the side), a square front panel and a flap with the tracklist, and the TDK-style stripe band
#   under the header. Owner's brief ("a cassette label") beats the research's plain sleeve grid.
# Fonts: Be Vietnam Pro only (registry face for idea 039): 900 for titles, 800 tracked for catalogue numbers, 400 body.
# Palette: J-card stock #EFEBE1, shell black #151412, label red #B52B15 (cat nos and buy actions only),
#   stripe yellow and orange used only in the stripe band. Layout idea: the J-card (spine + front + flap).
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('catalog')
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

def wjson(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

# ------------------------------------------------------------------ theme.json
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
display = next(f for f in fonts if f['slug'] == 'display')
PAL = [
    ('base', '#EFEBE1', 'J-card stock'),
    ('contrast', '#151412', 'Shell black'),
    ('accent', '#B52B15', 'Label red'),
    ('accent-2', '#E9A800', 'Stripe yellow'),
    ('accent-3', '#E0661C', 'Stripe orange'),
    ('surface', '#E2DDD0', 'Inlay'),
    ('line', '#151412', 'Rule'),
    ('muted', '#57524A', 'Pencil'),
    ('shell', '#262320', 'Smoked shell'),
]
def palette(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

V = lambda k: 'var:preset|color|' + k
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'writingMode': True,
            'fontFamilies': [
                display,
                {'fontFamily': display['fontFamily'], 'name': 'Be Vietnam Pro (text)', 'slug': 'body'}],
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Spine', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '1.875rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.5rem', 'max': '4rem'}},
                {'slug': 'display', 'size': '7.5rem', 'name': 'Display', 'fluid': {'min': '3.25rem', 'max': '7.5rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': V('base'), 'text': V('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': V('accent')}},
                     ':focus': {'outline': {'color': V('accent'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'lineHeight': '0.98', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '800'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '800', 'lineHeight': '1.15', 'letterSpacing': '0'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '800', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {'color': {'background': V('accent'), 'text': V('base')},
                       'border': {'radius': '2px', 'width': '2px', 'style': 'solid', 'color': V('accent')},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.25em', 'right': '1.25em'}},
                       ':hover': {'color': {'background': V('contrast'), 'text': V('base')}, 'border': {'color': V('contrast')}},
                       ':focus': {'outline': {'color': V('contrast'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': V('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|x-large', 'letterSpacing': '-0.03em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': V('accent')}}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': V('muted')}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500'},
                                'elements': {'link': {'color': {'text': V('accent')}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.45'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': V('contrast')}},
            'core/separator': {'color': {'text': V('contrast')}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '600', 'lineHeight': '1.3'},
                           'border': {'left': {'color': V('contrast'), 'width': '6px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                           'elements': {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '400'}}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.05'},
                               'border': {'top': {'color': V('contrast'), 'width': '6px', 'style': 'solid'}, 'bottom': {'color': V('contrast'), 'width': '2px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': V('line'), 'width': '2px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/code': {'typography': {'fontFamily': 'var:preset|font-family|body'}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/comments': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': (':where(h1,h2,h3,h4){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none;font-variant-numeric:tabular-nums}'
                '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.55em .6em .55em 0;text-align:left;vertical-align:top;font-variant-numeric:tabular-nums}'
                '.wp-block-table thead{border-bottom:2px solid var(--wp--preset--color--line)}.wp-block-table th{font-family:var(--wp--preset--font-family--body);font-weight:500}'
                '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0;background:transparent}'
                '.wp-block-navigation .current-menu-item>a,.wp-block-navigation a[aria-current]{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:.3em}'
                '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base)}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:2px}'
                '.is-style-jcard .wp-block-column+.wp-block-column{border-left:2px dashed var(--wp--preset--color--contrast)}'
                '.is-style-flap{display:flex;flex-direction:column;justify-content:space-between}'
                '@media (max-width:781px){.is-style-jcard .wp-block-column+.wp-block-column{border-left:0;border-top:2px dashed var(--wp--preset--color--contrast)}'
                '.is-style-catalogue td:nth-child(4),.is-style-catalogue th:nth-child(4),.is-style-catalogue td:nth-child(5),.is-style-catalogue th:nth-child(5){display:none}}'
                '@media (min-width:782px){.is-style-spine{background-size:10px 100%!important;background-position:0 0,10px 0,20px 0!important;padding-top:var(--wp--preset--spacing--30)!important;padding-left:calc(30px + var(--wp--preset--spacing--20))!important}'
                '.is-style-spine{position:relative;min-height:22rem}.is-style-spine>.wp-block-group{writing-mode:vertical-rl;transform:rotate(180deg);position:absolute;top:var(--wp--preset--spacing--30);bottom:var(--wp--preset--spacing--30);left:calc(30px + var(--wp--preset--spacing--20));right:var(--wp--preset--spacing--20);flex-wrap:nowrap!important;justify-content:space-between!important;align-items:center}'
                '.is-style-spine .wp-block-post-title,.is-style-spine h2,.is-style-spine h3{white-space:nowrap;flex:0 1 auto;min-height:0;overflow:hidden;text-overflow:ellipsis}''.is-style-jcard .wp-block-post-featured-image{position:sticky;top:0}}'
                '@media (prefers-reduced-motion:no-preference){.wp-block-post-featured-image img{transition:transform .2s}.wp-block-post-featured-image a:hover img{transform:translate(-3px,-3px)}}'),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Pre-order notice'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-release', 'title': 'Release (J-card)', 'postTypes': ['post']},
    ],
}
wjson('theme.json', theme)

write('style.css', '''/*
Theme Name: Catalog
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A theme for small cassette and record labels that sell editions from their own shop, with catalogue numbers, J-card release pages and sold-out states.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: catalog
Tags: e-commerce, entertainment, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

# ------------------------------------------------------------------ style variations
def variation(name, title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': palette(pal)}}}
    if extra:
        d['styles'] = extra
    wjson('styles/%s.json' % name, d)

variation('dub', 'Dub', [('base', '#0F1A14', 'J-card stock'), ('contrast', '#E8E3D3', 'Shell black'), ('accent', '#F07A52', 'Label red'),
    ('accent-2', '#D9B44A', 'Stripe yellow'), ('accent-3', '#7FA36B', 'Stripe orange'), ('surface', '#18261E', 'Inlay'), ('line', '#E8E3D3', 'Rule'),
    ('muted', '#B3AE9E', 'Pencil'), ('shell', '#08100B', 'Smoked shell')])
variation('tape', 'Tape', [('base', '#F2E7C9', 'J-card stock'), ('contrast', '#3A2A1A', 'Shell black'), ('accent', '#A1361B', 'Label red'),
    ('accent-2', '#D69A2D', 'Stripe yellow'), ('accent-3', '#B8562A', 'Stripe orange'), ('surface', '#E8DAB4', 'Inlay'), ('line', '#3A2A1A', 'Rule'),
    ('muted', '#65513A', 'Pencil'), ('shell', '#3A2A1A', 'Smoked shell')])
variation('factory', 'Factory', [('base', '#FFFFFF', 'J-card stock'), ('contrast', '#000000', 'Shell black'), ('accent', '#D42A14', 'Label red'),
    ('accent-2', '#000000', 'Stripe yellow'), ('accent-3', '#D42A14', 'Stripe orange'), ('surface', '#EDEDED', 'Inlay'), ('line', '#000000', 'Rule'),
    ('muted', '#4D4D4D', 'Pencil'), ('shell', '#000000', 'Smoked shell')],
    {'elements': {'heading': {'typography': {'fontWeight': '800', 'letterSpacing': '-0.035em'}}}})

# ------------------------------------------------------------------ section styles
def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('jcard', 'J-card', ['core/group', 'core/columns'], {
    'color': {'background': V('base'), 'text': V('contrast')},
    'border': {'color': V('contrast'), 'width': '2px', 'style': 'solid', 'radius': '4px'},
    'css': '&{overflow:hidden}& > .wp-block-columns{gap:0!important;margin:0}'})
section('spine', 'Spine', ['core/column', 'core/group'], {
    'color': {'background': V('surface'), 'text': V('contrast')},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500'},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
    'css': '&{background-image:linear-gradient(var(--wp--preset--color--accent) 0 0),linear-gradient(var(--wp--preset--color--accent-3) 0 0),linear-gradient(var(--wp--preset--color--accent-2) 0 0);'
           'background-size:100% 10px;background-repeat:no-repeat;background-position:0 0,0 10px,0 20px;padding-top:calc(30px + var(--wp--preset--spacing--30))!important}'
           '& .wp-block-post-title,& h2,& h3{font-size:var(--wp--preset--font-size--large)!important;letter-spacing:0;line-height:1.1;margin:0}'
           '& > .wp-block-group{gap:var(--wp--preset--spacing--30)}'})
section('tape-stripes', 'Tape stripes', ['core/separator'], {
    'border': {'width': '0'},
    'css': '&{height:30px;opacity:1;border:0!important;margin:0!important;max-width:none!important;background:linear-gradient(to bottom,var(--wp--preset--color--accent) 0 33.4%,var(--wp--preset--color--accent-3) 33.4% 66.7%,var(--wp--preset--color--accent-2) 66.7% 100%)}'})
section('catno', 'Catalogue number', ['core/paragraph', 'core/post-terms', 'core/heading'], {
    'color': {'text': V('accent')},
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'letterSpacing': '0.04em'},
    'elements': {'link': {'color': {'text': V('accent')}, 'typography': {'textDecoration': 'none'}}}})
section('sold-out', 'Sold out stamp', ['core/paragraph'], {
    'color': {'text': V('accent')},
    'border': {'color': V('accent'), 'width': '2px', 'style': 'solid', 'radius': '2px'},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500', 'textTransform': 'uppercase'},
    'spacing': {'padding': {'top': '0', 'bottom': '0', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
    'css': '&{display:inline-block;transform:rotate(-2deg)}'})
section('shell', 'Smoked shell', ['core/group', 'core/columns'], {
    'color': {'background': V('shell'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('base')}}, 'heading': {'color': {'text': V('base')}}, 'caption': {'color': {'text': V('base')}}},
    'css': '& .wp-block-table td,& .wp-block-table th,& .wp-block-table thead{border-color:var(--wp--preset--color--base)}& .has-muted-color{color:var(--wp--preset--color--surface)!important}'})
section('inlay', 'Inlay card', ['core/group', 'core/columns'], {
    'color': {'background': V('surface'), 'text': V('contrast')},
    'border': {'radius': '4px'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': V('contrast'), 'width': '2px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})
section('rule-bottom', 'Rule below', ['core/group'], {
    'border': {'bottom': {'color': V('contrast'), 'width': '2px', 'style': 'solid'}}})
section('notice', 'Notice bar', ['core/group'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('base')}}},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}})
section('side-label', 'Side label', ['core/heading'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500', 'letterSpacing': '0'},
    'spacing': {'padding': {'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
    'css': '&{display:inline-block}'})
section('buy', 'Buy link', ['core/read-more'], {
    'color': {'background': V('accent'), 'text': V('base')},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500', 'textDecoration': 'none'},
    'border': {'radius': '2px'},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
    'css': '&{display:inline-block}&:hover{background:var(--wp--preset--color--contrast)}'})
section('flap', 'Flap', ['core/column'], {
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('formats', 'Formats table', ['core/table'], {
    'css': '& td:first-child{width:60%}& em{font-style:normal;font-weight:800;color:var(--wp--preset--color--accent)}'})
section('sleeve-grid', 'Sleeve grid', ['core/post-template'], {
    'css': '& > li{border-top:2px solid var(--wp--preset--color--contrast);padding-top:var(--wp--preset--spacing--20)}'})

# ------------------------------------------------------------------ parts
write('parts/header.html', group(J(
    row(J(stack(J(dyn('site-title', level=0), para('Cassettes, dubbed in Leith', fontSize='x-small', textColor='muted')),
                style={'spacing': {'blockGap': '0'}}),
          dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}, overlayMenu='mobile')),
        justify='space-between', wrap=False, align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})),
    tag='header', align='full', layout={'type': 'constrained'}) + '\n\n' + separator(className='is-style-tape-stripes', align='full'))

write('parts/notice.html', pattern_ref('notice-preorder'))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0),
                  para('A cassette label in Leith. Four or five releases a year, in editions of 100 to 150, dubbed in real time on two decks in the back room.', fontSize='small'))),
        (None, J(heading('Post and pick-up', 6),
                 para('2F1, 14 Great Junction Street<br>Leith, Edinburgh EH6 5LA<br><a href="mailto:hello@example.com">hello@example.com</a>', fontSize='small'),
                 para('Collect from our table at the Leith Walk record fair, first Saturday of the month, 10am to 3pm.', fontSize='small'))),
        (None, J(heading('Elsewhere', 6),
                 para('<a href="https://bandcamp.com/">Bandcamp</a><br><a href="https://www.instagram.com/">Instagram</a><br><a href="/about/#newsletter">Mailing list, about once a month</a><br><a href="/demos/">Sending us a demo</a>', fontSize='small'))),
        align='wide'),
    para('Sleeve art on this demo is public domain painting from the Met, Cincinnati Art Museum and Wikimedia Commons, used as stand-ins for real artwork.',
         align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-shell',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ------------------------------------------------------------------ patterns
IMG = {'041': 'cover-7.jpg', '040': 'cover-3.jpg', '039': 'cover-1.jpg', '038': 'cover-5.jpg', '037': 'cover-4.jpg', '036': 'cover-6.jpg', '035': 'cover-8.jpg'}
ALT = {
    'cover-7.jpg': 'Sleeve art: a grid of black lines with a large red square and pale blue panels',
    'cover-3.jpg': 'Sleeve art: circles, triangles and thin crossing lines on a cream ground',
    'cover-1.jpg': 'Sleeve art: a yellow sun inside a blue and pink flower shape on brown paper',
    'cover-5.jpg': 'Sleeve art: red, blue and yellow rectangles scattered on a white ground',
    'cover-4.jpg': 'Sleeve art: a thin ink drawing of four birds on a wire over a pink and blue wash',
    'cover-6.jpg': 'Sleeve art: a black ink drawing of a man pushing a huge gear wheel',
    'cover-8.jpg': 'Sleeve art: a sepia double-exposure portrait of a man in a white cap',
}

def jcard_static(cat, artist, title, img, sides, formats_rows, align='wide'):
    spine = row(J(para(cat, className='is-style-catno'), heading(title, 3), para(artist)), wrap=False, justify='space-between')
    flap = J(heading('Side A', 4, className='is-style-side-label'), lst(sides[0], ordered=True),
             heading('Side B', 4, className='is-style-side-label'), lst(sides[1], ordered=True))
    return group(columns(
        ('84px', spine),
        ('46%', image(img, ALT[img], lightbox=False, aspectRatio='1', scale='cover')),
        (None, flap)),
        className='is-style-jcard', align=align, layout={'type': 'default'})

# Signature: the latest release as a J-card, straight from the posts.
def jcard_query(per_page=1, qid=11, offset=0):
    spine_inner = row(J(dyn('post-terms', term='post_tag', className='is-style-catno'), dyn('post-title', level=2)), wrap=False, justify='space-between')
    return query(group(columns(
        ('84px', spine_inner),
        ('46%', dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover', style={'border': {'width': '0'}})),
        (None, J(stack(J(dyn('post-terms', term='post_tag', className='is-style-catno', fontSize='large'),
                 dyn('post-title', level=2, isLink=True, fontSize='display'))),
                 stack(J(dyn('post-excerpt', moreText='', excerptLength=40, fontSize='large'),
                 row(J(dyn('read-more', content='Listen and buy this tape', className='is-style-buy'), dyn('post-date', format='j F Y')), style={'spacing': {'blockGap': 'var:preset|spacing|40'}}))))),
        ), className='is-style-jcard', layout={'type': 'default'}),
        per_page=per_page, query_id=qid, align='wide')


# fix the spine column class after the fact (columns() helper cannot set per-column classes)
def spine_cols(markup):
    markup = markup.replace('<!-- wp:column -->\n<div class="wp-block-column">', '<!-- wp:column {"className":"is-style-flap"} -->\n<div class="wp-block-column is-style-flap">')
    return markup.replace('<!-- wp:column {"width":"84px"} -->\n<div class="wp-block-column" style="flex-basis:84px">',
                          '<!-- wp:column {"width":"84px","className":"is-style-spine"} -->\n<div class="wp-block-column is-style-spine" style="flex-basis:84px">')

pattern('jcard-latest', 'J-card: latest release', 'featured,query', spine_cols(jcard_query()),
        description='The newest release laid out as an unfolded J-card: spine, front panel and flap. Reads from your latest post.')

pattern('jcard-insert', 'J-card insert (static, for one release)', 'featured', spine_cols(jcard_static(
    'HISS 041', 'Mira Oduya', 'Salt rooms', 'cover-7.jpg',
    (['Salt rooms (part one) 11:40', 'Harbour lamp 4:12', 'Kelp, drying 6:03'], ['Salt rooms (part two) 14:55', 'The shore at 5am 5:31']), [])),
    description='An unfolded J-card with spine, front and a side A / side B tracklist.')

CATALOGUE = [
    ('HISS 041', 'Mira Oduya', 'Salt rooms', 'C46 tape', '100', 'In stock'),
    ('HISS 040', 'Low Fold', 'Pylons at dusk', 'C60 tape, 12" LP', '150 / 300', '12 tapes left'),
    ('HISS 039', 'Kasia Wren', 'Paper boat radio', 'C46 tape', '100', 'Sold out'),
    ('HISS 038', 'Tam Boyd', 'Organ for an empty church', 'C60 tape', '100', 'In stock'),
    ('HISS 037', 'Bonnie Rigg', 'Twelve songs for the night bus', 'C46 tape, 12" LP', '100 / 250', 'Tape sold out'),
    ('HISS 036', 'Various', 'Leith Walk tapes, volume two', 'C90 tape', '150', 'Sold out'),
    ('HISS 035', 'Harbour Choir', 'Hymns for the ferry', 'C46 tape', '100', 'Sold out'),
    ('HISS 034', 'Low Fold', 'Two rooms', 'C46 tape', '75', 'Sold out'),
    ('HISS 033', 'Mira Oduya', 'Cold frame', 'C60 tape', '100', 'Repress due March'),
]
def status_cell(s):
    return '<strong>%s</strong>' % s if 'Sold out' in s or 'sold out' in s else s

pattern('catalogue-table', 'Catalogue table (cat no, artist, title, format, edition)', 'text,featured', group(J(
    row(J(heading('The catalogue, newest first', 2, fontSize='x-large'), para('<a href="/catalogue/">Every release with sleeves</a>', fontSize='small')), justify='space-between', align='wide'),
    table([[c, a, '<em>%s</em>' % t, f, e, status_cell(s)] for c, a, t, f, e, s in CATALOGUE],
          head=['Cat no', 'Artist', 'Title', 'Format', 'Edition', 'Status'], align='wide', className='is-style-catalogue')),
    align='wide', layout={'type': 'default'}),
    description='The whole catalogue as a table. Cat numbers run newest first, like the shelf.')

section('catalogue', 'Catalogue table', ['core/table'], {
    'css': '& td:first-child{color:var(--wp--preset--color--accent);font-weight:800;white-space:nowrap}'
           '& td:nth-child(3) em{font-style:normal;font-weight:800}& strong{font-family:var(--wp--preset--font-family--body);font-weight:500;color:var(--wp--preset--color--accent);font-size:.85em}'
})

grid_item = J(dyn('post-terms', term='post_tag', className='is-style-catno', fontSize='small'),
              dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover'),
              dyn('post-title', isLink=True, level=3, fontSize='large'),
              dyn('post-excerpt', moreText='', excerptLength=12, fontSize='small'))
pattern('release-grid', 'Release grid: cat no above each sleeve', 'featured,query', group(J(
    row(J(heading('Recent tapes', 2, fontSize='x-large'), para('<a href="/catalogue/">Full catalogue</a>', fontSize='small')), justify='space-between', align='wide'),
    query(grid_item, per_page=8, query_id=12, align='wide', template_class='is-style-sleeve-grid',
          layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'})), align='wide', layout={'type': 'default'}), keywords='releases, sleeves, catalogue')

pattern('release-grid-archive', 'Release grid (inherits the page query)', 'query', inherit_query(grid_item, align='wide', template_class='is-style-sleeve-grid',
        layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '13rem'}), inserter=False)

pattern('post-list', 'News list', 'posts,query', inherit_query(
    group(J(dyn('post-date', format='j M Y'), dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', moreText='', excerptLength=30)),
          className='is-style-rule-top'), align='wide'), inserter=False)

pattern('tracklist', 'Tracklist, side A and side B', 'text', columns(
    (None, J(heading('Side A', 4, className='is-style-side-label'), lst(['Salt rooms (part one), 11:40', 'Harbour lamp, 4:12', 'Kelp, drying, 6:03'], ordered=True))),
    (None, J(heading('Side B', 4, className='is-style-side-label'), lst(['Salt rooms (part two), 14:55', 'The shore at 5am, 5:31'], ordered=True)))), description='Two sides with running times. C46 means 23 minutes a side, so keep an eye on the totals.')

pattern('formats-editions', 'Formats and editions, with sold-out states', 'shop', J(
    heading('Formats', 3),
    table([
        ['<strong>C46 cassette</strong><br>Chrome tape, clear shell, riso J-card, download code', '100', '£8<br><a href="/shop/">Buy the tape</a>'],
        ['<strong>12" LP</strong><br>Black vinyl, printed inner sleeve', '300', '£22<br><a href="/shop/">Buy the LP</a>'],
        ['<strong>First run, orange shell</strong><br>Hand-stamped, numbered on the spine', '30', '£10<br><em>Sold out</em>'],
        ['<strong>Download</strong><br>FLAC, MP3, 24-bit WAV', 'No limit', '£6<br><a href="https://bandcamp.com/">Bandcamp</a>'],
    ], head=['Format', 'Copies', 'Price'], className='is-style-formats'),
    para('Tapes are dubbed to order in batches of twelve, so allow a week before they post.', fontSize='small', textColor='muted')))

pattern('sold-out-state', 'Sold out stamp with repress note', 'shop', group(J(
    para('Sold out', className='is-style-sold-out'),
    para('All 100 copies of HISS 039 have gone. We do not repress tapes as a rule, but Kasia has said yes to a second run of 50 in March. <a href="/about/#newsletter">Join the list</a> and you will hear first.', fontSize='small')),
    layout={'type': 'flex', 'orientation': 'vertical'}))

pattern('eu-shop-note', 'Note for EU customers', 'shop', group(J(
    heading('Ordering from the EU?', 4),
    para('Since 2021 a £8 tape can pick up £12 of customs fees on the way to Berlin. Our EU stock sits with Kassettenkeller in Leipzig, who post within the EU with no customs charges. Same price, in euros. <a href="https://example.com/kassettenkeller">Order from Kassettenkeller</a>.', fontSize='small')),
    className='is-style-inlay'), description='Points EU customers to a European stockist to avoid customs charges.')

pattern('notice-preorder', 'Notice: pre-order bar', 'banner', group(
    para('HISS 042, Low Fold <em>Night ferry</em>, is up for pre-order. Tapes post on 14 November. <a href="/shop/">Pre-order the tape</a>'),
    className='is-style-notice', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='A one-line bar for pre-orders. Change the cat no and date, or remove the part once it ships.')

pattern('artist-index', 'Artists, A to Z', 'text', group(J(
    heading('Everyone on the label, A to Z', 2, fontSize='x-large'),
    columns(
        (None, J(heading('B', 4, className='is-style-catno'), para('<a href="/artists/">Bonnie Rigg</a>'),
                 heading('H', 4, className='is-style-catno'), para('<a href="/artists/">Harbour Choir</a>'))),
        (None, J(heading('K', 4, className='is-style-catno'), para('<a href="/artists/">Kasia Wren</a>'),
                 heading('L', 4, className='is-style-catno'), para('<a href="/artists/">Low Fold</a>'))),
        (None, J(heading('M', 4, className='is-style-catno'), para('<a href="/artists/mira-oduya/">Mira Oduya</a>'),
                 heading('T', 4, className='is-style-catno'), para('<a href="/artists/">Tam Boyd</a>'))),
        className='is-style-rule-top')), align='wide', layout={'type': 'default'}))

pattern('artist-photos', 'Artist photos with captions', 'gallery', columns(
    (None, image('artist-4.jpg', 'Black and white photo of a grey-haired musician in sunglasses, sitting with arms crossed', 'Mira Oduya at home in Portobello')),
    (None, image('artist-2.jpg', 'Two guitarists playing on the floor of a small venue, one kneeling over his guitar', 'Low Fold at Leith Depot, launch night for HISS 040')),
    (None, image('synth.jpg', 'A wall of modular synthesizer modules patched with red, yellow and blue cables', 'Kasia Wren\'s shortwave rig, borrowed from Summerhall')),
    align='wide'))

pattern('artist-roster', 'Artist roster with cat nos', 'text', J(
    table([['Bonnie Rigg', 'Songs for guitar and a bad Casio', 'HISS 037'],
           ['Harbour Choir', 'Eleven singers from Newhaven', 'HISS 035'],
           ['Kasia Wren', 'Shortwave recordings and piano', 'HISS 039'],
           ['Low Fold', 'Three-piece, drones and drums', 'HISS 034, 040, 042'],
           ['Mira Oduya', 'Tape loops made at the seaside', 'HISS 033, 041'],
           ['Tam Boyd', 'Church organs, mostly out of tune', 'HISS 038']],
          head=['Artist', 'What they do', 'On Hiss'], className='is-style-catalogue')))

pattern('artist-page', 'Artist page: bio, releases, dates', 'about', J(
    columns(('40%', image('artist-4.jpg', 'Black and white photo of a grey-haired musician in sunglasses, sitting on a chair with arms crossed', 'Mira Oduya, photographed by Ruth Mackie')),
            (None, J(heading('Mira Oduya', 1, fontSize='xx-large'),
                     para('Mira Oduya (b. 1968, Aberdeen) makes long pieces from tape loops recorded along the Forth. She has two tapes on Hiss and one LP on a label in Ghent. She plays live about six times a year, always seated.'),
                     heading('On Hiss', 4),
                     table([['HISS 041', '<em>Salt rooms</em>', '2025'], ['HISS 033', '<em>Cold frame</em>', '2023']], className='is-style-catalogue'),
                     heading('Live', 4),
                     table([['8 Nov', 'Leith Depot, Edinburgh', '<a href="https://example.com/tickets">Tickets</a>'], ['29 Nov', 'The Old Hairdressers, Glasgow', '<a href="https://example.com/tickets">Tickets</a>']]),
                     buttons(('Read the press kit', '/artists/mira-oduya/press-kit/')))), align='wide')), block_types='core/post-content')

pattern('artist-epk', 'Artist press kit (EPK)', 'about', J(
    heading('Mira Oduya, press kit', 1, fontSize='xx-large'),
    para('For promoters and press. Everything here can be used without asking, with the photographer credited.'),
    heading('Short bio, 60 words', 4),
    para('Mira Oduya is a Scottish musician who makes long pieces from tape loops recorded along the Forth estuary. Her second tape for Hiss, <em>Salt rooms</em>, was dubbed onto chrome tape in an edition of 100. She plays live seated, with two Walkmans, a mixer and a borrowed PA.'),
    heading('Photos', 4),
    gallery([('artist-4.jpg', 'Black and white portrait of Mira Oduya sitting with arms crossed', 'Ruth Mackie, 3000 px'),
             ('reel.jpg', 'A grey reel-to-reel tape recorder with one spool loaded', 'Mira\'s loop machine, 2400 px')], columns=2),
    heading('Tech rider', 4),
    lst(['One table, 1.5 m, at the front of the stage, not on it', 'Two DI boxes and a stereo feed to the PA', 'One chair with no arms', 'Set length 40 to 50 minutes']),
    pattern_ref('press-quotes')), block_types='core/post-content')

pattern('press-quotes', 'Press quotes (named)', 'testimonials', columns(
    (None, quote('Forty minutes of sea noise and tape wobble, and I have played it every morning this month.', 'Aisha Grant, The Skinny, October 2025')),
    (None, quote('The J-card is printed on the same risograph as the Leith Walk food bank flyers, and it looks better than most LP sleeves I get sent.', 'Tom Riddell, Tape Op zine, issue 12')), align='wide'))

pattern('dubbing-process', 'How the tapes are made', 'about', columns(
    ('40%', image('dubbing.jpg', 'A beige Telex Copyette tape duplicator with its lid open', 'The Copyette, used for test copies only')),
    (None, J(heading('Dubbed in real time', 3),
             para('Every tape is copied at normal speed from a master on two Nakamichi decks, twelve at a time. It takes a Saturday to do a run of 100. High-speed duplicators are quicker and we have one, but the top end suffers, so it only makes test copies.'),
             para('J-cards are printed on a risograph at Out of the Blue on Dalmeny Street, two colours, on 170gsm card. Shells come from a factory in Poland in six colours.'),
             para('We use chrome (Type II) tape. It costs us 40p more per copy and it is worth it.', fontSize='small', textColor='muted'))), align='wide'))

pattern('tape-formats-explained', 'What C46, C60 and chrome mean', 'text', J(
    heading('Tape lengths, in case you were wondering', 3),
    table([['C46', '23 minutes a side', 'Most of our albums'], ['C60', '30 minutes a side', 'Longer records and compilations'], ['C90', '45 minutes a side', 'Compilations only. Thinner tape, more wobble']],
          head=['Length', 'Per side', 'What we use it for']),
    para('All our tapes play on any normal cassette deck. Set it to chrome or Type II if it has the switch. If it does not, they still sound fine.', fontSize='small')))

pattern('tape-care', 'Looking after a tape', 'text', J(
    heading('Looking after a tape', 4),
    lst(['Keep it out of cars in summer. Shells warp at about 50 °C.', 'Wind it to one end before storing, so the tape sits evenly.', 'Clean the heads on your deck every 30 hours or so with a cotton bud and isopropyl alcohol.', 'If a tape gets chewed, send it back. We will re-shell it for the price of postage.'])))

pattern('postage-table', 'Postage by region', 'shop', J(
    heading('Postage', 3),
    table([['UK', '£2.20 for up to three tapes', '£4.50 per LP', '2 to 4 days'],
           ['EU', 'Order from Kassettenkeller, Leipzig', 'Kassettenkeller', '3 to 6 days'],
           ['USA and Canada', '£6', '£16', '7 to 14 days'],
           ['Everywhere else', '£7', '£19', '10 to 21 days']], head=['Where', 'Tapes', 'LPs', 'Usually takes']),
    para('We post on Tuesdays and Fridays from the Leith post office on Great Junction Street.', fontSize='small', textColor='muted')))

pattern('release-schedule', 'Coming up: release schedule', 'text', J(
    heading('Coming up', 3),
    table([['HISS 042', 'Low Fold', '<em>Night ferry</em>', '14 November', '<a href="/shop/">Pre-order</a>'],
           ['HISS 043', 'Harbour Choir', '<em>Winter hymns</em>', 'December', 'Mastering'],
           ['HISS 044', 'Kasia Wren', '<em>Long wave</em>', 'February', 'Being recorded']],
          head=['Cat no', 'Artist', 'Title', 'Out', ''], className='is-style-catalogue')))

pattern('demo-policy', 'Sending us a demo', 'text', J(
    heading('Sending us a demo', 2),
    para('We listen to demos on the first Monday of the month, with tea, all the way through. Send a private Bandcamp or SoundCloud link to <a href="mailto:demos@example.com">demos@example.com</a>. Please do not attach files.'),
    para('We release four or five tapes a year, so most of what we hear we cannot put out, even when we love it. We reply to everyone, eventually. It can take two months.'),
    heading('What we tend to put out', 4),
    lst(['Long pieces, drones, loops, field recordings', 'Songs, if they sound like they were recorded in a kitchen', 'Anything that makes sense on a C46']),
    heading('What we do not put out', 4),
    lst(['Digital-only releases', 'Anything over 90 minutes', 'Records by people who have not heard any of ours'])), block_types='core/post-content')

pattern('stockists', 'Where to find our tapes', 'text', J(
    heading('Shops that stock us', 4),
    table([['Edinburgh', 'Vinyl Villains, Elm Row'], ['Glasgow', 'Monorail, King Street'], ['Leipzig', 'Kassettenkeller (all EU orders)'], ['London', 'Low Tide Tapes, Deptford'], ['Tokyo', 'Meditations, Kyoto (yes, Kyoto)']], head=['City', 'Shop'])))

pattern('label-about', 'About the label', 'about', columns(
    ('45%', image('hero.jpg', 'A Maxell UDII 46 chrome cassette in its case, on an orange cloth', 'Our first tapes were on Maxell UDII. Now we buy blank chrome in bulk.')),
    (None, J(heading('A label in a spare room', 2),
             para('Hiss Tapes started in 2016 when Ailsa Kerr dubbed 40 copies of her friend Mira\'s loop recordings for a gig at Leith Depot and sold all of them. Now there are two of us: Ailsa runs the label and Callum Frew does the J-cards, the post and the shop.'),
             para('We put out tapes because they are cheap enough to take a chance on, and because people actually keep them. We do some vinyl when a record is selling well enough to pay for a pressing, which is roughly one in four.'),
             para('Nobody here is paid for it, yet. Artists get half of what their tape makes after costs, paid every June.'))), align='wide'))

pattern('newsletter', 'Mailing list', 'call-to-action', group(J(
    heading('The mailing list', 3),
    para('One email about a month: what is out, what is left, and when pre-orders open. Editions of 100 go in about a week, so this is how most people get one.'),
    buttons(('Join by email', 'mailto:hello@example.com?subject=Mailing%20list'))),
    className='is-style-inlay', anchor='newsletter'))

pattern('find-us', 'Pick-up and contact', 'contact', columns(
    (None, J(heading('Write to us', 3),
             para('<a href="mailto:hello@example.com">hello@example.com</a> for orders and anything else. Demos go to <a href="mailto:demos@example.com">demos@example.com</a>.'),
             para('We answer email on Tuesday and Friday evenings, when we pack orders.'))),
    (None, J(heading('Pick up in person', 3),
             para('We are a flat, so there is no shop to visit. You can collect orders from our table at the Leith Walk record fair, first Saturday of the month, 10am to 3pm, at the Leith Theatre on Ferry Road. Choose "Collect at the fair" at checkout.'))),
    (None, J(heading('Address for returns', 3),
             para('Hiss Tapes<br>2F1, 14 Great Junction Street<br>Leith, Edinburgh EH6 5LA'))), align='wide'))

pattern('shop-split', 'Shop: tapes and vinyl', 'shop', group(J(
    heading('In the shop', 2, fontSize='x-large'),
    columns(
        (None, J(image('tapes-5.jpg', 'Two cassettes, a Sony and a clear TDK, lying on a wooden table', href='/shop/'),
                 heading('<a href="/shop/">Tapes</a>', 3), para('C46 and C60 on chrome, £8 to £9. Most runs are 100 copies.', fontSize='small'))),
        (None, J(image('vinyl.jpg', 'A stack of old LP sleeves photographed from the side, with labels showing', href='/shop/'),
                 heading('<a href="/shop/">Vinyl</a>', 3), para('12" LPs when a tape does well enough to pay for a pressing. £22.', fontSize='small'))),
        (None, J(image('walkman.jpg', 'A black GE personal cassette player with an AM/FM radio', href='/shop/'),
                 heading('<a href="/shop/">Bundles</a>', 3), para('Any three tapes for £21, plus a secondhand Walkman when we find working ones.', fontSize='small'))),
        align='wide')), align='wide', layout={'type': 'default'}))

pattern('release-credits', 'Release credits', 'text', J(
    heading('Credits', 4),
    table([['Recorded', 'Portobello beach and a flat on Duke Street, winter 2024'], ['Mastered for tape', 'Rafe Lindsay at Chamber Studio'], ['J-card', 'Callum Frew, riso printed at Out of the Blue'], ['Photo', 'Ruth Mackie']])))

pattern('page-catalogue', 'Page: catalogue', 'featured', J(pattern_ref('catalogue-table'), pattern_ref('release-schedule')), block_types='core/post-content')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('label-about'), pattern_ref('dubbing-process'), pattern_ref('tape-formats-explained'), pattern_ref('stockists'), pattern_ref('newsletter')), block_types='core/post-content')
pattern('page-artists', 'Page: artists', 'about', J(pattern_ref('artist-photos'), pattern_ref('artist-index'), pattern_ref('artist-roster')), block_types='core/post-content')
pattern('page-contact', 'Page: contact', 'contact', J(pattern_ref('find-us'), pattern_ref('postage-table'), pattern_ref('eu-shop-note')), block_types='core/post-content')
pattern('page-release', 'Release page body (tracklist, formats, credits)', 'featured', J(
    para('Two long pieces recorded at low tide on Portobello beach, looped on a Revox and played back through a borrowed church PA. Side A was made in January, side B in March, when the wind dropped.'),
    pattern_ref('tracklist'), pattern_ref('formats-editions'), pattern_ref('release-credits')), block_types='core/post-content', post_types='post')

# ------------------------------------------------------------------ templates
main_pad = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', J(
    template_part('notice'), template_part('header', 'header'),
    group(J(pattern_ref('jcard-latest'),
            group(pattern_ref('catalogue-table'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            group(pattern_ref('release-grid'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            group(pattern_ref('dubbing-process'), align='wide', className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            columns((None, pattern_ref('newsletter')), (None, pattern_ref('eu-shop-note')), align='wide', style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}})),
          tag='main', style=main_pad),
    template_part('footer', 'footer')))

write('templates/home.html', J(template_part('header', 'header'), group(J(
    row(J(heading('Catalogue', 1), para('Every Hiss release, newest first. Red numbers are catalogue numbers, which is how we file them and how shops order them.', fontSize='small')), justify='space-between', align='wide'),
    pattern_ref('release-grid-archive')), tag='main', style=main_pad), template_part('footer', 'footer')))

write('templates/index.html', J(template_part('header', 'header'), group(J(
    dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), tag='main', style=main_pad), template_part('footer', 'footer')))

write('templates/archive.html', J(template_part('header', 'header'), group(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'),
    pattern_ref('release-grid-archive')), tag='main', style=main_pad), template_part('footer', 'footer')))

write('templates/search.html', J(template_part('header', 'header'), group(J(
    dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, buttonText='Search', placeholder='Cat no, artist or title', align='wide'),
    pattern_ref('post-list')), tag='main', style=main_pad), template_part('footer', 'footer')))

write('templates/404.html', J(template_part('header', 'header'), group(J(
    heading('Side C does not exist', 1),
    para('That page is not here. It may have been a release that sold out and got tidied away. Try the catalogue, or search by cat no.'),
    dyn('search', label='Search', showLabel=False, buttonText='Search', placeholder='HISS 041'),
    buttons(('Go to the catalogue', '/catalogue/'))), tag='main', style=main_pad), template_part('footer', 'footer')))

write('templates/page.html', J(template_part('header', 'header'), group(J(
    dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image'), dyn('post-content', layout={'type': 'constrained'})),
    tag='main', style=main_pad), template_part('footer', 'footer')))

write('templates/page-wide.html', J(template_part('header', 'header'), group(J(
    dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})),
    tag='main', style=main_pad), template_part('footer', 'footer')))

single_meta = J(dyn('post-date', format='j F Y'), dyn('post-terms', term='category'))
write('templates/single.html', J(template_part('header', 'header'), group(J(
    row(single_meta), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image', aspectRatio='3/2', scale='cover'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Older', showTitle=True), dyn('post-navigation-link', label='Newer', showTitle=True)), justify='space-between'),
          className='is-style-rule-top')), tag='main', style=main_pad), template_part('footer', 'footer')))

# single release: the J-card as a page
spine_single = row(J(dyn('post-terms', term='post_tag', className='is-style-catno'), dyn('post-title', level=2), para('Hiss Tapes')), wrap=False, justify='space-between')
single_release = group(columns(
    ('84px', spine_single),
    ('42%', J(dyn('post-featured-image', aspectRatio='1', scale='cover', style={'border': {'width': '0'}}))),
    (None, J(dyn('post-terms', term='post_tag', className='is-style-catno', fontSize='large'),
             dyn('post-title', level=1, fontSize='xx-large'),
             dyn('post-excerpt', moreText=''),
             dyn('post-content', layout={'type': 'default'})))),
    className='is-style-jcard', align='wide', layout={'type': 'default'})
write('templates/single-release.html', J(template_part('header', 'header'), group(J(
    spine_cols(single_release),
    group(row(J(dyn('post-navigation-link', type='previous', label='Previous release', showTitle=True, taxonomy='category'),
                dyn('post-navigation-link', label='Next release', showTitle=True, taxonomy='category')), justify='space-between'),
          className='is-style-rule-top', align='wide')), tag='main', style=main_pad), template_part('footer', 'footer')))


# ------------------------------------------------------------------ demo content
releases = [
    ('Salt rooms', 'HISS 041', 'Mira Oduya', 'C46 on chrome, clear shell, edition of 100.', '041', True),
    ('Pylons at dusk', 'HISS 040', 'Low Fold', 'C60 in a grey shell, edition of 150. Also on 12" LP, 300 copies.', '040', False),
    ('Paper boat radio', 'HISS 039', 'Kasia Wren', 'C46, white shell, edition of 100. Sold out.', '039', False),
    ('Organ for an empty church', 'HISS 038', 'Tam Boyd', 'C60, smoke shell, edition of 100.', '038', False),
    ('Twelve songs for the night bus', 'HISS 037', 'Bonnie Rigg', 'C46, edition of 100, sold out. 12" LP still in stock.', '037', False),
    ('Leith Walk tapes, volume two', 'HISS 036', 'Various artists', 'C90 compilation, 18 tracks, edition of 150. Sold out.', '036', False),
    ('Hymns for the ferry', 'HISS 035', 'Harbour Choir', 'C46, edition of 100. Sold out.', '035', False),
]
def release_body(title, cat, artist, fmt, n):
    sa = {'040': (['Pylons at dusk 7:20', 'Kirkcaldy 5:02', 'Sub-station 9:40'], ['Grid 12:11', 'Dusk again 6:30']),
          '039': (['Paper boat radio 8:01', 'Shipping forecast, slowed 6:44', 'Lighthouse keeper 7:10'], ['Long wave 11:32', 'Static, with piano 9:00']),
          '038': (['Voluntary in C 9:15', 'Empty pews 12:40', 'Bellows 6:00'], ['Hymn 441 14:20', 'Vestry 13:02']),
          '037': (['Night bus 3:10', 'Waverley 2:48', 'The 22 to Ocean Terminal 4:01', 'Chips 2:30'], ['Seafield 3:44', 'Last orders 3:20', 'Walking home 5:12']),
          '036': (['Nine artists from Leith Walk, 45 minutes'], ['Nine more, 45 minutes']),
          '035': (['Abide with me 5:40', 'Crimond 3:55', 'Ferry hymn 7:30'], ['Eternal father 4:40', 'Harbour 8:00'])}
    if n == '041':
        return None
    a, b = sa[n]
    return J(columns((None, J(heading('Side A', 4, className='is-style-side-label'), lst(a, ordered=True))),
                     (None, J(heading('Side B', 4, className='is-style-side-label'), lst(b, ordered=True)))),
             buttons(('Buy the tape', '/shop/'), ('Listen on Bandcamp', 'https://bandcamp.com/', {'className': 'is-style-outline'})))

posts = []
for title, cat, artist, fmt, n, use_pattern in releases:
    p = {'title': title, 'category': 'releases', 'tags': [cat], 'image': IMG[n], 'template': 'single-release',
         'excerpt': '%s. %s' % (artist, fmt)}
    if use_pattern:
        p['pattern'] = 'catalog/page-release'
    else:
        p['content'] = release_body(title, cat, artist, fmt, n)
    posts.append(p)
content = {
    'site': {'title': 'Hiss Tapes', 'tagline': 'Cassettes and the odd record, dubbed in real time in Leith'},
    'categories': [{'slug': 'releases', 'name': 'Releases'}],
    'front_page': 'home', 'posts_page': 'catalogue',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'catalogue', 'title': 'Catalogue', 'content': ''},
        {'slug': 'artists', 'title': 'Artists', 'pattern': 'catalog/page-artists', 'template': 'page-wide'},
        {'slug': 'mira-oduya', 'title': 'Mira Oduya', 'parent': 'artists', 'pattern': 'catalog/artist-page', 'template': 'page-wide'},
        {'slug': 'press-kit', 'title': 'Mira Oduya, press kit', 'parent': 'mira-oduya', 'pattern': 'catalog/artist-epk'},
        {'slug': 'about', 'title': 'About', 'pattern': 'catalog/page-about', 'template': 'page-wide'},
        {'slug': 'demos', 'title': 'Demos', 'pattern': 'catalog/demo-policy'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'catalog/page-contact', 'template': 'page-wide'},
        {'slug': 'shipping', 'title': 'Shipping', 'content': J(pattern_ref('postage-table'), pattern_ref('eu-shop-note'), pattern_ref('tape-care'))},
    ],
    'posts': posts,
    'nav': [{'label': 'Catalogue', 'url': '/catalogue/'}, {'label': 'Artists', 'url': '/artists/'}, {'label': 'Shop', 'url': '/shop/'},
            {'label': 'About', 'url': '/about/'}, {'label': 'Demos', 'url': '/demos/'}, {'label': 'Contact', 'url': '/contact/'}],
    'currency': 'GBP',
    'products': [
        {'name': 'HISS 041 Mira Oduya, Salt rooms (C46)', 'price': '8', 'image': 'cover-7.jpg', 'category': 'Tapes', 'sku': 'HISS041-C', 'stock': 38, 'short': 'Chrome tape, clear shell, riso J-card. Edition of 100.'},
        {'name': 'HISS 040 Low Fold, Pylons at dusk (C60)', 'price': '9', 'image': 'cover-3.jpg', 'category': 'Tapes', 'sku': 'HISS040-C', 'stock': 12, 'short': 'Grey shell. Edition of 150, twelve left.'},
        {'name': 'HISS 040 Low Fold, Pylons at dusk (12" LP)', 'price': '22', 'image': 'cover-3.jpg', 'category': 'Vinyl', 'sku': 'HISS040-LP', 'stock': 140, 'short': 'Black vinyl, printed inner sleeve. 300 copies.'},
        {'name': 'HISS 039 Kasia Wren, Paper boat radio (C46)', 'price': '8', 'image': 'cover-1.jpg', 'category': 'Tapes', 'sku': 'HISS039-C', 'stock': 0, 'short': 'Sold out. A second run of 50 is planned for March.'},
        {'name': 'HISS 038 Tam Boyd, Organ for an empty church (C60)', 'price': '9', 'image': 'cover-5.jpg', 'category': 'Tapes', 'sku': 'HISS038-C', 'stock': 44, 'short': 'Smoke shell. Edition of 100.'},
        {'name': 'HISS 037 Bonnie Rigg, Twelve songs for the night bus (12" LP)', 'price': '22', 'image': 'cover-4.jpg', 'category': 'Vinyl', 'sku': 'HISS037-LP', 'stock': 61, 'short': 'The tape is gone. The LP is not. 250 copies.'},
        {'name': 'HISS 042 Low Fold, Night ferry (C46, pre-order)', 'price': '8', 'image': 'hero.jpg', 'category': 'Tapes', 'sku': 'HISS042-C', 'stock': 100, 'short': 'Posts on 14 November. Edition of 100.'},
    ],
}
os.makedirs('demos/catalog', exist_ok=True)
json.dump(content, open('demos/catalog/content.json', 'w'), indent=1, ensure_ascii=False)
open('demos/catalog/fonts-claim.txt', 'w').write('display: Be Vietnam Pro (registry face for 039, unchanged)\n')
print('catalog built')

# ====================================================================== ROUND 2
# Owner's review: fewer tables, lightbox on work, 40+ patterns, a home page with no table, and a demo that uses the kit.
# Sections studied on Planet Mu, Clay Pipe Music, Fire Records, NNA Tapes and Bandcamp label pages.
theme['settings']['blocks'] = {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}}
theme['styles']['css'] += ('.is-style-defs>.wp-block-group{border-top:1px solid var(--wp--preset--color--line);padding:.6em 0;gap:.4rem 1.5rem;margin:0!important}'
                           '.is-style-defs>.wp-block-group:last-child{border-bottom:1px solid var(--wp--preset--color--line)}.is-style-defs p{margin:0}'
                           '.is-style-defs>.wp-block-group>p:first-child{flex:0 0 9rem;font-weight:800}.is-style-defs>.wp-block-group>p:nth-child(2){flex:1 1 12rem}'
                           '.is-style-cat-rows>.wp-block-group>p:first-child{color:var(--wp--preset--color--accent);letter-spacing:.04em}'
                           '.is-style-cat-rows>.wp-block-group>p:nth-child(3){flex:1 1 14rem;font-weight:800}.is-style-cat-rows>.wp-block-group>p:nth-child(4){flex:0 0 11rem}'
                           '@media (max-width:781px){.is-style-cat-rows>.wp-block-group>p:nth-child(4){display:none}}')
wjson('theme.json', theme)

def defs(rows, extra_cls=''):
    """Definition-style rows made from groups (label, value, ...)."""
    return group(J(*[row(J(*[para(c) for c in r]), wrap=True) for r in rows]), className=('is-style-defs ' + extra_cls).strip(), layout={'type': 'default'})

# ---- tables replaced by designed rows
pattern('artist-roster', 'Artist roster with cat nos', 'about', defs([
    ['Bonnie Rigg', 'Songs for guitar and a bad Casio', 'HISS 037'], ['Harbour Choir', 'Eleven singers from Newhaven', 'HISS 035'],
    ['Kasia Wren', 'Shortwave recordings and piano', 'HISS 039'], ['Low Fold', 'Three-piece, drones and drums', 'HISS 034, 040, 042'],
    ['Mira Oduya', 'Tape loops made at the seaside', 'HISS 033, 041'], ['Tam Boyd', 'Church organs, mostly out of tune', 'HISS 038']]))
pattern('artist-page', 'Artist page: bio, releases, dates', 'about', J(
    columns(('40%', image('artist-4.jpg', 'Black and white photo of a grey-haired musician in sunglasses, sitting on a chair with arms crossed', 'Mira Oduya, photographed by Ruth Mackie')),
            (None, J(heading('Mira Oduya', 1, fontSize='xx-large'),
                     para('Mira Oduya (b. 1968, Aberdeen) makes long pieces from tape loops recorded along the Forth. She has two tapes on Hiss and one LP on a label in Ghent. She plays live about six times a year, always seated.'),
                     heading('On Hiss', 4),
                     defs([['HISS 041', '<a href="/salt-rooms/">Salt rooms</a>, 2025'], ['HISS 033', 'Cold frame, 2023, repress due March']], 'is-style-cat-rows'),
                     heading('Live', 4),
                     defs([['8 Nov', 'Leith Depot, Edinburgh', '<a href="/live/">Details</a>'], ['29 Nov', 'The Old Hairdressers, Glasgow', '<a href="/live/">Details</a>']]),
                     buttons(('Read the press kit', '/artists/mira-oduya/press-kit/')))), align='wide')), block_types='core/post-content')
pattern('release-credits', 'Release credits', 'release', J(heading('Credits', 4), defs([
    ['Recorded', 'Portobello beach and a flat on Duke Street, winter 2024'], ['Mastered for tape', 'Rafe Lindsay at Chamber Studio'],
    ['J-card', 'Callum Frew, riso printed at Out of the Blue'], ['Photo', 'Ruth Mackie']])))
pattern('stockists', 'Where to find our tapes', 'shop', J(heading('Shops that stock us', 4), defs([
    ['Edinburgh', 'Vinyl Villains, Elm Row'], ['Glasgow', 'Monorail, King Street'], ['Leipzig', 'Kassettenkeller (all EU orders)'],
    ['London', 'Low Tide Tapes, Deptford'], ['Kyoto', 'Meditations, near Demachiyanagi']])))
pattern('tape-formats-explained', 'What C46, C60 and C90 mean', 'text', J(
    heading('Tape lengths, in case you were wondering', 3),
    columns(*[(None, group(J(heading(n, 2, fontSize='xx-large'), para(side, fontSize='large'), para(use, fontSize='small')), className='is-style-inlay'))
              for n, side, use in [('C46', '23 minutes a side', 'Most of our albums.'), ('C60', '30 minutes a side', 'Longer records and compilations.'), ('C90', '45 minutes a side', 'Compilations only. Thinner tape, more wobble.')]], align='wide'),
    para('All our tapes play on any normal cassette deck. Set it to chrome or Type II if it has the switch. If it does not, they still sound fine.', fontSize='small')))
pattern('release-schedule', 'Coming up: release schedule', 'release', J(heading('Coming up', 3), defs([
    ['HISS 042', 'Low Fold', 'Night ferry', 'Out 14 November. <a href="/shop/">Pre-order</a>'], ['HISS 043', 'Harbour Choir', 'Winter hymns', 'December, being mastered'],
    ['HISS 044', 'Kasia Wren', 'Long wave', 'February, being recorded']], 'is-style-cat-rows')))

pattern('catalogue-list', 'Catalogue as ruled rows (no table)', 'release', group(J(
    row(J(heading('The catalogue, newest first', 2, fontSize='x-large'), para('<a href="/catalogue/">Every release with sleeves</a>', fontSize='small')), justify='space-between'),
    defs([[c, a, t, s] for c, a, t, f, e, s in CATALOGUE], 'is-style-cat-rows')), align='wide', layout={'type': 'default'}),
    description='The catalogue as ruled rows: cat no, artist, title, status. Lighter than the full table.')

# ---- new patterns
pattern('release-feature', 'New release with pre-order', 'hero', columns(
    ('45%', image('hero.jpg', 'A Maxell UDII 46 chrome cassette in its case on an orange cloth', 'Test pressing of HISS 042 on chrome tape')),
    (None, J(para('HISS 042', className='is-style-catno', fontSize='large'), heading('Night ferry', 2), para('Low Fold', fontSize='large'),
             para('Recorded on the Rosyth to Zeebrugge ferry the month before it stopped running. Drums in the car deck, guitars in a cabin. C46 in a grey shell, edition of 100, posting on 14 November.'),
             buttons(('Pre-order the tape, £8', '/shop/'), ('Hear a track', '/salt-rooms/', {'className': 'is-style-outline'})))), align='wide'))

pattern('formats-cards', 'Formats as cards with stamps', 'shop', columns(
    (None, J(image('tapes-5.jpg', 'Two cassettes, a Sony and a clear TDK, on a wooden table', aspectRatio='4/3', scale='cover'), heading('C46 cassette', 4), para('Chrome tape, clear shell, riso J-card, download code. 100 copies.', fontSize='small'), para('£8', fontSize='large', className='is-style-catno'))),
    (None, J(image('vinyl.jpg', 'A stack of LP sleeves seen from the side', aspectRatio='4/3', scale='cover'), heading('12" LP', 4), para('Black vinyl, printed inner sleeve. 300 copies.', fontSize='small'), para('£22', fontSize='large', className='is-style-catno'))),
    (None, J(image('walkman.jpg', 'A black GE personal cassette player', aspectRatio='4/3', scale='cover'), heading('First run, orange shell', 4), para('Hand-stamped, numbered on the spine. 30 copies.', fontSize='small'), para('Sold out', className='is-style-sold-out'))),
    align='wide'))

pattern('listen-player', 'Listen: a track and a Bandcamp link', 'release', group(J(
    heading('Listen', 4), audio('https://example.com/audio/hiss-041-harbour-lamp.mp3', caption='Harbour lamp, from HISS 041, 4:12'),
    para('The whole album streams on <a href="https://bandcamp.com/">Bandcamp</a>. Buying the tape gets you the download too.', fontSize='small')), className='is-style-inlay'))

pattern('physical-gallery', 'The physical tape, photographed', 'gallery', J(
    heading('What arrives in the post', 4),
    gallery([('tapes.jpg', 'Two cassettes side by side on a dark table', 'Shells come in six colours'), ('dubbing.jpg', 'A tape duplicator with its lid open', 'Test copies on the Copyette'),
             ('deck.jpg', 'A portable Nakamichi cassette deck with two VU meters', 'One of the two decks we dub on')], columns=3, align='wide')))

pattern('press-release', 'Press text for a release', 'release', group(J(
    heading('Press text', 4),
    para('Salt rooms is Mira Oduya\'s second tape for Hiss: two long pieces recorded at low tide on Portobello beach, looped on a Revox A77 and played back through a borrowed church PA. It follows Cold frame (HISS 033), which sold out in nine days.'),
    para('For review copies and interviews, email <a href="mailto:press@example.com">press@example.com</a>. We send MP3s, not tapes, to press.', fontSize='small')), className='is-style-rule-top'))

pattern('artist-cards', 'Artist cards with photos', 'about', columns(
    (None, J(image('artist-4.jpg', 'Black and white portrait of Mira Oduya sitting with arms crossed'), heading('<a href="/artists/mira-oduya/">Mira Oduya</a>', 4), para('Tape loops, Portobello', fontSize='small'))),
    (None, J(image('artist-2.jpg', 'Two guitarists playing on the floor of a small venue'), heading('<a href="/artists/">Low Fold</a>', 4), para('Drones and drums, Leith', fontSize='small'))),
    (None, J(image('synth.jpg', 'A wall of modular synthesizer modules with patch cables'), heading('<a href="/artists/">Kasia Wren</a>', 4), para('Shortwave and piano, Glasgow', fontSize='small'))),
    (None, J(image('reel.jpg', 'A grey reel-to-reel tape recorder with one spool loaded'), heading('<a href="/artists/">Tam Boyd</a>', 4), para('Church organs, Fife', fontSize='small'))),
    align='wide'))

pattern('label-night', 'Label night (event)', 'events', columns(
    ('55%', image('crowd.jpg', 'A crowd at a concert with hands in the air under stage lights', 'The last Hiss night, March, Leith Depot')),
    (None, J(para('Saturday 8 November, 7pm', className='is-style-catno', fontSize='large'), heading('Hiss at Leith Depot', 2),
             para('Mira Oduya, Low Fold and a DJ set from the Harbour Choir\'s alto section. We launch HISS 042 on the night and the tape table opens at 7.'),
             para('£8 on the door, £6 in advance. Step-free, bar till midnight.', fontSize='small'), buttons(('Get tickets', 'https://example.com/tickets')))),
    align='wide'))

pattern('live-dates', 'Live dates for label artists', 'events', J(heading('Live', 3), defs([
    ['8 Nov', 'Hiss night: Mira Oduya, Low Fold', 'Leith Depot, Edinburgh'], ['15 Nov', 'Kasia Wren', 'Summerhall, Edinburgh'],
    ['29 Nov', 'Mira Oduya', 'The Old Hairdressers, Glasgow'], ['6 Dec', 'Harbour Choir', 'Newhaven Parish Church, free']])))

pattern('tape-club', 'Tape club subscription', 'shop', group(columns(
    ('55%', J(heading('Every release, posted to you', 2), para('£30 a year and every new Hiss tape is posted to you on release day, before it goes on sale. That is usually five tapes, so it saves you £10 and the postage.', fontSize='large'),
              buttons(('Join the tape club', '/shop/')))),
    (None, lst(['Every release posted on the day it comes out', 'A download of everything in the back catalogue', 'First go at represses and the orange first runs', 'Cancel any time, no questions'])),
    align='wide'), className='is-style-shell', align='full', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}))

pattern('order-faq', 'Ordering questions', 'shop', J(heading('Questions about orders', 3),
    details('When will my tape arrive?', para('We post on Tuesdays and Fridays. In the UK that is two to four days after. Pre-orders post on release day.')),
    details('Can I return a tape?', para('If it arrives broken or chewed, yes: send a photo and we post another. We cannot take back opened tapes otherwise, because we dub them to order.')),
    details('Do you ship to the US?', para('Yes, £6 for up to three tapes. It takes one to two weeks and you may pay a small import fee.')),
    details('Why is my download code on the J-card?', para('So it still works if you give the tape away. Redeem it on Bandcamp.'))))

pattern('label-history', 'Label history by year', 'about', J(heading('How it went', 3), defs([
    ['2016', '40 copies of Mira\'s loops for a gig. All sold.'], ['2018', 'First vinyl, HISS 012, Low Fold. Took a year to sell 300.'],
    ['2021', 'Bought the second Nakamichi deck. Runs went from 50 to 100.'], ['2024', 'Kassettenkeller in Leipzig starts handling EU orders.'],
    ['2025', 'Forty-one releases. Still in the spare room.']])))

pattern('bundle', 'Back catalogue bundle', 'shop', columns(
    ('35%', image('tapes-5.jpg', 'Two cassettes on a wooden table')),
    (None, J(heading('Any three tapes for £21', 3), para('Pick any three from what is in stock and we post them together. Add a secondhand Walkman for £15 when we have working ones. Right now we have four.'),
             buttons(('Choose three tapes', '/shop/')))), align='wide'))

pattern('quote-single', 'One quote, big', 'testimonials', pullquote('Forty minutes of sea noise and tape wobble, and I have played it every morning this month.', 'Aisha Grant, The Skinny, October 2025'))

# ---- pages that use the kit
pattern('page-live', 'Page: live', 'events', J(pattern_ref('label-night'), pattern_ref('live-dates')), block_types='core/post-content')
pattern('page-tape-club', 'Page: tape club', 'shop', J(pattern_ref('tape-club'), pattern_ref('formats-cards'), pattern_ref('bundle'), pattern_ref('order-faq')), block_types='core/post-content')
pattern('page-release', 'Release page body (tracklist, formats, credits)', 'release', J(
    para('Two long pieces recorded at low tide on Portobello beach, looped on a Revox and played back through a borrowed church PA. Side A was made in January, side B in March, when the wind dropped.'),
    pattern_ref('tracklist'), pattern_ref('listen-player'), pattern_ref('formats-editions'), pattern_ref('physical-gallery'), pattern_ref('press-release'), pattern_ref('release-credits'), pattern_ref('quote-single')),
    block_types='core/post-content', post_types='post')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('label-about'), pattern_ref('dubbing-process'), pattern_ref('label-history'), pattern_ref('tape-formats-explained'), pattern_ref('stockists'), pattern_ref('newsletter')), block_types='core/post-content')
pattern('page-artists', 'Page: artists', 'about', J(pattern_ref('artist-cards'), pattern_ref('artist-index'), pattern_ref('artist-roster')), block_types='core/post-content')

write('templates/front-page.html', J(
    template_part('notice'), template_part('header', 'header'),
    group(J(pattern_ref('jcard-latest'),
            group(pattern_ref('release-grid'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            group(pattern_ref('catalogue-list'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            group(pattern_ref('release-feature'), align='wide', className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            group(pattern_ref('tape-club'), align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            group(pattern_ref('label-night'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
            columns((None, pattern_ref('newsletter')), (None, pattern_ref('eu-shop-note')), align='wide', style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}})),
          tag='main', style=main_pad),
    template_part('footer', 'footer')))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0),
                  para('A cassette label in Leith. Four or five releases a year, in editions of 100 to 150, dubbed in real time on two decks in the back room.', fontSize='small'))),
        (None, J(heading('Post and pick-up', 6),
                 para('2F1, 14 Great Junction Street<br>Leith, Edinburgh EH6 5LA<br><a href="mailto:hello@example.com">hello@example.com</a>', fontSize='small'),
                 para('<a href="/shipping/">Shipping and postage</a><br><a href="/demos/">Sending us a demo</a>', fontSize='small'))),
        (None, J(heading('Elsewhere', 6),
                 para('<a href="https://bandcamp.com/">Bandcamp</a><br><a href="https://www.instagram.com/">Instagram</a><br><a href="/about/#newsletter">Mailing list</a>', fontSize='small'),
                 dyn('search', label='Search the catalogue', showLabel=False, buttonText='Search', placeholder='Cat no or artist'))),
        align='wide'),
    para('Sleeve art on this demo is public domain painting from the Met, Cincinnati Art Museum and Wikimedia Commons, used as stand-ins for real artwork.',
         align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-shell',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ---- demo: pages that use the new patterns, release bodies with more of the kit
for p in content['posts']:
    if 'content' in p and p['content']:
        p['content'] = J(p['content'], gallery([('tapes.jpg', 'Two cassettes side by side on a dark table', 'The tape'), (p['image'], 'Sleeve art for %s' % p['title'], 'The J-card front')], columns=2),
                         para('Tapes are dubbed to order in batches of twelve, so allow a week before they post.', fontSize='small', textColor='muted'))
content['pages'] += [
    {'slug': 'live', 'title': 'Live', 'pattern': 'catalog/page-live', 'template': 'page-wide'},
    {'slug': 'tape-club', 'title': 'Tape club', 'pattern': 'catalog/page-tape-club', 'template': 'page-wide'},
]
content['nav'] = [{'label': 'Catalogue', 'url': '/catalogue/'}, {'label': 'Artists', 'url': '/artists/'}, {'label': 'Shop', 'url': '/shop/'},
                  {'label': 'Tape club', 'url': '/tape-club/'}, {'label': 'Live', 'url': '/live/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}]
json.dump(content, open('demos/catalog/content.json', 'w'), indent=1, ensure_ascii=False)
theme['styles']['blocks']['core/pullquote']['elements'] = {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontStyle': 'normal', 'fontWeight': '400', 'letterSpacing': '0', 'textTransform': 'none'}}}
theme['styles']['css'] += '.wp-block-pullquote{text-align:left;padding-left:0;padding-right:0}.wp-block-pullquote blockquote{margin:0}'
wjson('theme.json', theme)
print('catalog round 2 built')
