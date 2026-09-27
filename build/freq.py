# freq: Radio Havik, a volunteer-run online and DAB+ station in Katendrecht, Rotterdam.
# Direction: Swiss neo-grotesk index, as researched and confirmed by the owner ("YEAH THAT RADIO STATION").
#   White page, 1px black rules, a strict grid, text indexes instead of cards, show art in black and white
#   squares, and a black live player bar fixed to the bottom of every page. Unlike bpm (black, condensed
#   capitals, a DJ's archive) this is a daytime station guide in sentence case, blue on white.
# Fonts: Radio Canada only (the registry face for 046), 700 for headings, 400 for text, tabular figures for times.
# Palette: #FFFFFF, #000000, signal blue #0038FF for links and the support block, live red #FF3B00 for the
#   on-air square only. Layout idea: the week as a seven-column schedule grid with the station timezone on it.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('freq')
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
    if a.get('isStackedOnMobile') is False:
        va += ' is-not-stacked-on-mobile'
    return '<!-- wp:columns%s -->\n<div class="%s">%s</div>\n<!-- /wp:columns -->' % ((' ' + json.dumps(a, separators=(',', ':'))) if a else '', ' '.join(filter(None, ['wp-block-columns', 'align' + a['align'] if a.get('align') else '', va, a.get('className', '')])), '\n\n'.join(out))

# ------------------------------------------------------------------ theme.json
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
display = next(f for f in fonts if f['slug'] == 'display')
PAL = [
    ('base', '#FFFFFF', 'Paper'),
    ('contrast', '#000000', 'Ink'),
    ('accent', '#0038FF', 'Signal blue'),
    ('live', '#FF3B00', 'Live red'),
    ('surface', '#F2F2F2', 'Grey card'),
    ('line', '#000000', 'Rule'),
    ('muted', '#555555', 'Pencil'),
]
def palette(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1440px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True,
            'fontFamilies': [display, {'fontFamily': display['fontFamily'], 'name': 'Radio Canada (text)', 'slug': 'body'}],
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Small print', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '4rem', 'name': 'Title', 'fluid': {'min': '2.5rem', 'max': '4rem'}},
                {'slug': 'display', 'size': '7.5rem', 'name': 'Display', 'fluid': {'min': '3rem', 'max': '7.5rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': V('base'), 'text': V('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.5', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': V('accent')}, 'typography': {'textDecoration': 'none'},
                     ':hover': {'typography': {'textDecoration': 'underline'}},
                     ':focus': {'outline': {'color': V('accent'), 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '1', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'letterSpacing': '-0.035em', 'lineHeight': '0.95'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'letterSpacing': '-0.03em'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15', 'letterSpacing': '-0.01em'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'button': {'color': {'background': V('contrast'), 'text': V('base')},
                       'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': V('contrast')},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '1em', 'right': '1em'}},
                       ':hover': {'color': {'background': V('accent'), 'text': V('base')}, 'border': {'color': V('accent')}},
                       ':focus': {'outline': {'color': V('accent'), 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': V('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|x-large', 'letterSpacing': '-0.03em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '400'},
                                'elements': {'link': {'color': {'text': V('contrast')}, ':hover': {'color': {'text': V('accent')}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': V('contrast')}, ':hover': {'color': {'text': V('accent')}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small'}, 'color': {'text': V('contrast')}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': V('line')}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.3'},
                           'border': {'left': {'color': V('accent'), 'width': '3px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|30'}},
                           'elements': {'cite': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontStyle': 'normal'}}}},
            'core/pullquote': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '700', 'lineHeight': '1.1'},
                               'border': {'top': {'color': V('line'), 'width': '1px', 'style': 'solid'}, 'bottom': {'color': V('line'), 'width': '1px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}},
            'core/audio': {'spacing': {'margin': {'top': '0', 'bottom': '0'}}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/search': {'border': {'radius': '0'}},
        },
        'css': ('body{font-synthesis:none;font-variant-numeric:tabular-nums;padding-bottom:5.5rem}'
                ':where(h1,h2,h3,h4){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                '.wp-block-table td,.wp-block-table th{border:0;border-top:1px solid var(--wp--preset--color--line);padding:.45em .75em .45em 0;text-align:left;vertical-align:top}'
                '.wp-block-table th{font-weight:700;border-top:0}.wp-block-table tr:last-child td{border-bottom:1px solid var(--wp--preset--color--line)}'
                '.wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:0}'
                '.wp-block-navigation .current-menu-item>a,.wp-block-navigation a[aria-current]{color:var(--wp--preset--color--accent)}'
                '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base)}'
                ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:2px}'
                '.is-style-player-bar{position:fixed;left:0;right:0;bottom:0;z-index:50;margin:0!important}'
                '.is-style-player-bar audio{height:36px;width:100%;min-width:12rem}'
                '.wp-element-button{white-space:nowrap}'
                '@media (max-width:781px){.is-hide-mobile{display:none!important}body{padding-bottom:7rem}.is-style-player-bar .wp-block-column{flex-basis:auto!important}.is-style-player-bar .wp-block-column:last-child{flex:1 1 40%!important}'
                '.is-style-shows-table td:nth-child(3),.is-style-shows-table th:nth-child(3){display:none}}'
                '@media (prefers-reduced-motion:no-preference){.is-style-bw-tiles img,.is-style-bw img{transition:filter .2s}}'),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'player', 'title': 'Live player bar'},
        {'area': 'uncategorized', 'name': 'off-air', 'title': 'Off-air notice'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-episode', 'title': 'Episode (player, tracklist)', 'postTypes': ['post']},
    ],
}
wjson('theme.json', theme)

write('style.css', '''/*
Theme Name: Freq
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A theme for community and online radio stations run by volunteers, with a live player bar, a weekly schedule, shows, residents, an episode archive and a support page.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: freq
Tags: entertainment, news, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def variation(name, title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': palette(pal)}}}
    if extra:
        d['styles'] = extra
    wjson('styles/%s.json' % name, d)
variation('pirate', 'Pirate', [('base', '#000000', 'Paper'), ('contrast', '#FFFFFF', 'Ink'), ('accent', '#FF2A1A', 'Signal blue'),
    ('live', '#FF2A1A', 'Live red'), ('surface', '#141414', 'Grey card'), ('line', '#FFFFFF', 'Rule'), ('muted', '#B3B3B3', 'Pencil')])
variation('fm', 'FM', [('base', '#F5F0E4', 'Paper'), ('contrast', '#1A1A1A', 'Ink'), ('accent', '#1C4DFF', 'Signal blue'),
    ('live', '#E03A12', 'Live red'), ('surface', '#EAE3D2', 'Grey card'), ('line', '#1A1A1A', 'Rule'), ('muted', '#57524A', 'Pencil')])
variation('late-night', 'Late night', [('base', '#0F1B33', 'Paper'), ('contrast', '#F2EEE6', 'Ink'), ('accent', '#FFB547', 'Signal blue'),
    ('live', '#FFB547', 'Live red'), ('surface', '#172746', 'Grey card'), ('line', '#F2EEE6', 'Rule'), ('muted', '#B7BDCB', 'Pencil')])

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('player-bar', 'Live player bar', ['core/group'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('base')}, 'typography': {'textDecoration': 'underline'}}},
    'typography': {'fontSize': 'var:preset|font-size|small'},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
    'css': '& p{margin:0}'})
section('live-dot', 'Live marker', ['core/paragraph'], {
    'typography': {'fontWeight': '700'},
    'css': '&::before{content:"";display:inline-block;width:.7em;height:.7em;background:var(--wp--preset--color--live);margin-right:.45em;vertical-align:-.02em}'})
section('schedule-day', 'Schedule day', ['core/column'], {
    'border': {'top': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20'}},
    'css': '& h3,& h4{font-size:var(--wp--preset--font-size--large)}& p{margin:0;padding:.35em 0;border-top:1px solid color-mix(in srgb,var(--wp--preset--color--line) 25%,transparent);font-size:var(--wp--preset--font-size--small)}& .is-style-live-dot{color:inherit}'})
section('bw-tiles', 'Black and white tiles', ['core/post-template', 'core/gallery', 'core/columns', 'core/group'], {
    'css': '& img{filter:grayscale(1)}& img:hover,& a:focus img{filter:none}'})
section('bw', 'Black and white', ['core/image', 'core/post-featured-image'], {
    'css': '& img{filter:grayscale(1)}'})
section('index-row', 'Index row', ['core/group', 'core/columns'], {
    'border': {'top': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
    'css': '& p,& h3,& .wp-block-post-title{margin:0}'})
section('signal', 'Signal blue block', ['core/group', 'core/column'], {
    'color': {'background': V('accent'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('base')}, 'typography': {'textDecoration': 'underline'}}, 'heading': {'color': {'text': V('base')}},
                 'button': {'color': {'background': V('base'), 'text': V('accent')}, 'border': {'color': V('base')}}},
    'css': '& .wp-block-table td,& .wp-block-table th{border-color:var(--wp--preset--color--base)}'})
section('grey', 'Grey card', ['core/group', 'core/column'], {
    'color': {'background': V('surface')},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('rule-top', 'Rule above', ['core/group', 'core/columns', 'core/heading'], {
    'border': {'top': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20'}}})
section('off-air', 'Off-air notice', ['core/group'], {
    'color': {'background': V('live'), 'text': V('contrast')},
    'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'underline'}}},
    'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'}})

# ------------------------------------------------------------------ parts
write('parts/header.html', group(J(
    row(J(row(J(dyn('site-title', level=0), para('Katendrecht, Rotterdam. Online and DAB+ 11C', fontSize='x-small', textColor='muted', className='is-hide-mobile'))),
          row(J(dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}, overlayMenu='mobile'),
                buttons(('Listen live', '#player'))), wrap=False, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
        justify='space-between', wrap=False, align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})),
    tag='header', align='full', className='is-style-index-row', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': '0', 'bottom': '0'}}}))

player = group(cols(
    ('14%', para('Live now', className='is-style-live-dot'), {'verticalAlignment': 'center'}),
    ('32%', para('<strong>Kapsalon</strong> with DJ Yasmina, 20:00 to 22:00'), {'verticalAlignment': 'center'}),
    ('24%', para('Next: Klankkast with Sem van Dijk, 22:00', className='is-hide-mobile'), {'verticalAlignment': 'center', 'className': 'is-hide-mobile'}),
    (None, audio('https://stream.example.com/radiohavik-128.mp3'), {'verticalAlignment': 'center'}),
    align='full', verticalAlignment='center', isStackedOnMobile=False, style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}}}),
    className='is-style-player-bar', align='full', anchor='player', layout={'type': 'constrained'})
pattern('player-bar', 'Live player bar (fixed to the bottom)', 'banner', player,
        description='The black bar with the live stream. Paste your stream URL into the audio block and update now/next each day.')
write('parts/player.html', pattern_ref('player-bar'))
write('parts/off-air.html', pattern_ref('off-air-notice'))
write('parts/footer.html', group(J(
    cols((None, J(heading('Radio Havik', 4), para('A volunteer station in a former bike shop on the Deliplein, Katendrecht. On air since 2018, 24 hours a day, with 61 presenters and nobody paid.', fontSize='small'))),
         (None, J(heading('Studio', 6), para('Deliplein 14, 3072 CT Rotterdam<br>Studio phone during shows: 010 555 0199<br><a href="mailto:studio@example.com">studio@example.com</a>', fontSize='small'))),
         (None, J(heading('Listen', 6), para('Online stream, 128 and 320 kbps<br>DAB+ block 11C in Rotterdam<br><a href="/schedule/">Schedule</a>, <a href="/archive/">Listen back</a>', fontSize='small'))),
         (None, J(heading('Help', 6), para('<a href="/support/">Support the station</a><br><a href="/submit-a-show/">Submit a show</a><br><a href="https://www.instagram.com/">Instagram</a>', fontSize='small'))),
         align='wide'),
    para('Demo photos are CC0 and public domain images from Wikimedia Commons, used as stand-ins for show art.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-rule-top',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ------------------------------------------------------------------ data
SHOWS = {
    'ochtend-op-de-kade': ('Ochtend op de Kade', 'Fenna Bos and Ruud Kraaijeveld', 'Breakfast, talk and new music', 'drummer.jpg'),
    'tweede-hands': ('Tweede Hands', 'Jaap Mulder', 'Records from the charity shop', 'records.jpg'),
    'maashaven-dub': ('Maashaven Dub', 'Kofi Mensah', 'Dub, steppers, roots', 'turntable.jpg'),
    'klankkast': ('Klankkast', 'Sem van Dijk', 'Experimental, live electronics', 'laptop.jpg'),
    'kapsalon': ('Kapsalon', 'DJ Yasmina', 'Rotterdam rap and hip-hop', 'headphones.jpg'),
    'nachtbus': ('Nachtbus', 'Iris de Wit', 'Ambient for the night shift', 'cello.jpg'),
    'zondagse-kaseko': ('Zondagse Kaseko', 'Ramona Kasanpawiro', 'Kaseko and Surinamese pop', 'sax.jpg'),
    'buurtpraat': ('Buurtpraat', 'Volunteers from Katendrecht', 'Neighbourhood talk', 'accordion.jpg'),
}
WEEK = [
    ('Monday', [('08:00', 'ochtend-op-de-kade'), ('12:00', None, 'Non-stop from the archive'), ('20:00', 'tweede-hands'), ('23:00', 'nachtbus')]),
    ('Tuesday', [('08:00', 'ochtend-op-de-kade'), ('14:00', None, 'Guest mix'), ('21:00', 'maashaven-dub')]),
    ('Wednesday', [('08:00', 'ochtend-op-de-kade'), ('18:00', None, 'Student hour, Codarts'), ('22:00', 'klankkast')]),
    ('Thursday', [('08:00', 'ochtend-op-de-kade'), ('17:00', None, 'Guest mix'), ('20:00', 'kapsalon', True), ('22:00', 'klankkast')]),
    ('Friday', [('08:00', 'ochtend-op-de-kade'), ('16:00', None, 'Friday selector'), ('23:00', 'nachtbus')]),
    ('Saturday', [('11:00', 'buurtpraat'), ('13:00', None, 'Live from the Deliplein'), ('21:00', None, 'Guest mix')]),
    ('Sunday', [('14:00', 'zondagse-kaseko'), ('16:00', None, 'Non-stop from the archive'), ('23:00', 'nachtbus')]),
]
def slot_para(slot):
    t, slug = slot[0], slot[1]
    live = len(slot) > 2 and slot[2] is True
    if slug:
        name = '<a href="/category/%s/">%s</a>' % (slug, SHOWS[slug][0])
    else:
        name = slot[2]
    return para('<strong>%s</strong><br>%s' % (t, name), className='is-style-live-dot') if live else para('<strong>%s</strong><br>%s' % (t, name))

# ------------------------------------------------------------------ patterns
pattern('schedule-week', 'Weekly schedule grid with station timezone', 'featured', group(J(
    row(J(heading('This week on Havik', 2), para('All times Rotterdam, CET (CEST in summer). The red square is on air now.', fontSize='small')), justify='space-between', align='wide'),
    cols(*[(None, J(heading(day, 3, fontSize='large'), *[slot_para(s) for s in slots]), {'className': 'is-style-schedule-day'}) for day, slots in WEEK],
         align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|20'}}})), align='wide', layout={'type': 'default'}),
    description='Seven days side by side. On phones each day stacks. Move the red square to the show that is on air.')

pattern('now-next', 'On air now and up next', 'featured', cols(
    ('62%', J(para('On air now', className='is-style-live-dot'),
              heading('Kapsalon with DJ Yasmina', 1),
              para('Rotterdam rap old and new, a guest verse live from the studio every week, and the phone line open from 21:00. Thursday 20:00 to 22:00.', fontSize='large'),
              buttons(('Listen live', '#player'), ('Past episodes of Kapsalon', '/category/kapsalon/', {'className': 'is-style-outline'})))),
    (None, J(heading('Today, Thursday', 4),
             table([['08:00', 'Ochtend op de Kade'], ['17:00', 'Guest mix: Lotte Ploeg'], ['20:00', '<strong>Kapsalon</strong>, live now'], ['22:00', 'Klankkast'], ['00:00', 'Non-stop from the archive']]),
             para('<a href="/schedule/">The whole week</a>', fontSize='small'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

row_tpl = cols(('12%', dyn('post-date', format='D j M')), ('20%', dyn('post-terms', term='category')), (None, dyn('post-title', isLink=True, level=3, fontSize='large')), ('24%', dyn('post-terms', term='post_tag', separator=', ')),
               verticalAlignment='top', className='is-style-index-row', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}}})
pattern('episode-index', 'Latest episodes as a text index', 'query', group(J(
    row(J(heading('Listen back', 2), para('<a href="/archive/">Every episode</a>')), justify='space-between', align='wide'),
    query(row_tpl, per_page=8, query_id=41, align='wide')), align='wide', layout={'type': 'default'}), description='Date, show, episode and genres. No cards.')
pattern('episode-index-archive', 'Episode index (inherits the page query)', 'query', inherit_query(row_tpl, align='wide'), inserter=False)
pattern('post-list', 'Post list', 'query', inherit_query(row_tpl, align='wide'), inserter=False)

tile = J(dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover'), dyn('post-terms', term='category'), dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-date', format='j M Y'))
pattern('episode-tiles', 'Episode tiles (black and white squares)', 'query', query(tile, per_page=6, query_id=42, align='wide', template_class='is-style-bw-tiles',
        layout={'type': 'grid', 'columnCount': 6, 'minimumColumnWidth': '10rem'}))

res = [(slug, *SHOWS[slug]) for slug in ['kapsalon', 'maashaven-dub', 'klankkast', 'zondagse-kaseko', 'tweede-hands', 'nachtbus', 'buurtpraat', 'ochtend-op-de-kade']]
pattern('residents-grid', 'Residents grid', 'about', group(J(
    heading('Residents', 2, align='wide'),
    group(J(*[group(J(image(img, 'Show art for %s: %s' % (name, alt), lightbox=False, href='/category/%s/' % slug, aspectRatio='1', scale='cover'),
                      heading('<a href="/category/%s/">%s</a>' % (slug, name), 4), para(host, fontSize='small'), para(genre, fontSize='small', textColor='muted')),
                    layout={'type': 'flex', 'orientation': 'vertical'}, style={'spacing': {'blockGap': 'var:preset|spacing|10'}})
              for slug, name, host, genre, img, alt in [(r[0], r[1], r[2], r[3], r[4], {'drummer.jpg': 'a drummer in a patterned shirt', 'records.jpg': 'rows of LP sleeves in a crate',
                'turntable.jpg': 'a turntable with a record playing, from above', 'laptop.jpg': 'a musician at a keyboard under stage lights', 'headphones.jpg': 'a man with red headphones round his neck',
                'cello.jpg': 'a woman playing the cello, old photograph', 'sax.jpg': 'a saxophonist in a hat and bow tie', 'accordion.jpg': 'two accordion players at a stall'}[r[4]]) for r in res]]),
          layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}, className='is-style-bw-tiles', align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('shows-index', 'Shows index (name, host, slot)', 'text', J(
    heading('Shows', 2),
    table([['<a href="/category/%s/">%s</a>' % (k, v[0]), v[1], v[2], {'ochtend-op-de-kade': 'Mon to Fri 08:00', 'tweede-hands': 'Mon 20:00', 'maashaven-dub': 'Tue 21:00', 'klankkast': 'Wed and Thu 22:00',
            'kapsalon': 'Thu 20:00', 'nachtbus': 'Mon and Fri 23:00', 'zondagse-kaseko': 'Sun 14:00', 'buurtpraat': 'Sat 11:00'}[k]] for k, v in SHOWS.items()],
          head=['Show', 'Presented by', 'What it is', 'When'], className='is-style-shows-table'),
    para('All times Rotterdam, CET or CEST.', fontSize='x-small', textColor='muted')))

pattern('tracklist', 'Tracklist', 'text', J(heading('Tracklist', 3), table([
    ['20:02', 'Opgezwolle', 'Het is weer tijd'], ['20:07', 'Winne', 'Top of the Pops'], ['20:15', 'Kempi', 'Dromen'], ['20:21', 'Yasmina, live in the studio with Mikey Blanco', 'Katendrecht freestyle'],
    ['20:34', 'Lange Frans', 'Zinloos'], ['20:40', 'Adje', 'Rotterdam']], head=['Time', 'Artist', 'Track'])))

pattern('episode-body', 'Episode body (player, notes, tracklist)', 'featured', J(
    audio('https://stream.example.com/archive/kapsalon-2026-09-25.mp3', caption='Kapsalon, 25 September, 1 hour 58 minutes'),
    para('Mikey Blanco came in to do a verse live at 20:21 and stayed for the whole show. The phone line was busy for once. Two tracks from the new Winne record, and Yasmina finally played the Opgezwolle tune everyone texts in for.'),
    pattern_ref('tracklist'),
    table([['Presented by', 'DJ Yasmina'], ['Guest', 'Mikey Blanco'], ['Studio', 'Deliplein 14, studio 1']])), block_types='core/post-content', post_types='post')

pattern('support-costs', 'Support: what your money pays for', 'call-to-action', group(cols(
    ('45%', J(heading('Radio Havik costs €2,140 a month to run', 2),
              para('Nobody is paid. The money goes on things we cannot get for free. 412 people give us a few euros a month, and that covers about two thirds of it.', fontSize='large'))),
    (None, J(table([['Music licences (Buma/Stemra and Sena)', '€690'], ['Rent for the studio on the Deliplein', '€850'], ['DAB+ transmission, block 11C', '€380'],
                    ['Stream hosting and the archive', '€140'], ['Insurance, electricity, coffee', '€80']], head=['Each month', ''], className='is-style-costs'),
             buttons(('Give €5 a month', 'https://example.com/support/5'), ('Give once', 'https://example.com/support/once')),
             para('We are a stichting (foundation) registered in Rotterdam, KvK 71234567. Gifts are tax-deductible in the Netherlands because we have ANBI status.', fontSize='x-small'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    className='is-style-signal', align='full', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}), description='Says exactly what the donations pay for.')
section('costs', 'Costs table', ['core/table'], {'css': '& td:last-child{text-align:right;font-weight:700}'})

pattern('membership-levels', 'Membership levels', 'call-to-action', J(
    heading('Become a member', 3),
    table([['€3 a month', 'Your name read out on the first Sunday of the month, if you want'],
           ['€6 a month', 'That, plus a Havik tote bag and 10% off at the Deliplein record fair'],
           ['€12 a month', 'All of that, plus one hour in studio 2 a year to record whatever you like']], head=['Amount', 'What you get']),
    para('Every level pays for the same radio. Pick whatever you can manage and change it any time.', fontSize='small')))

pattern('submit-a-show', 'Submit a show', 'call-to-action', J(
    heading('Submit a show', 2),
    para('We take new shows twice a year, in March and September. Send a pilot of 60 minutes, a paragraph about the idea, and when you could be here every week or every month. Most of our presenters had never been on radio before.'),
    lst(['Record the pilot at home, it does not have to sound perfect.', 'Upload it somewhere private and send the link to <a href="mailto:shows@example.com">shows@example.com</a>.', 'The programme group listens on the first Tuesday of April and October and replies to everyone.', 'New presenters get two training sessions on the desk with Ruud before going live.'], ordered=True),
    para('We do not take shows that are mostly adverts for a club night, and we cannot pay presenters.', fontSize='small')), block_types='core/post-content')

pattern('submit-callout', 'Submit a show (short call-out)', 'call-to-action', group(J(
    heading('Want a show?', 3), para('The next round of new shows starts in March. Send us a 60 minute pilot before 1 February.'),
    buttons(('How to submit a show', '/submit-a-show/'))), className='is-style-grey'))

pattern('newsletter', 'Newsletter', 'call-to-action', group(J(
    heading('The Sunday email', 3), para('Next week\'s guests, which shows moved, and one episode from the archive worth your time. Sent Sunday morning.'),
    buttons(('Get the Sunday email', 'mailto:studio@example.com?subject=Sunday%20email'))), className='is-style-grey'))

pattern('off-air-notice', 'Off-air notice with end time', 'banner', group(
    para('Off air for maintenance on Tuesday 7 October from 10:00 to 14:00 while the DAB+ transmitter is moved. The online stream plays the archive in the meantime.'),
    className='is-style-off-air', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='Put this part at the top of the templates when you are off air. Always give the end time.')

pattern('genre-index', 'Genre index', 'text', J(heading('Genres', 3), dyn('tag-cloud', smallestFontSize='1rem', largestFontSize='1.5rem', className='is-style-genres')))
section('genres', 'Genre list', ['core/tag-cloud'], {'css': '& a{margin:0 .8em .3em 0!important;color:var(--wp--preset--color--contrast)}& a:hover{color:var(--wp--preset--color--accent)}'})

pattern('guest-mix-series', 'Guest mix series', 'text', cols(
    ('30%', image('dj.jpg', 'A DJ controller with jog wheels and lit pads, photographed at an angle', lightbox=False, aspectRatio='1', scale='cover', className='is-style-bw')),
    (None, J(heading('Guest mix', 3),
             para('Three slots a week go to people who are not residents: DJs passing through, students from Codarts, and once a Rotterdam alderman who played only Doe Maar. One hour, sent to us as a file by Monday.'),
             para('<a href="mailto:shows@example.com?subject=Guest%20mix">Send a guest mix</a>'))), align='wide'))

pattern('find-the-studio', 'Find the studio', 'contact', cols(
    ('50%', image('rotterdam.jpg', 'Black and white aerial photo of Rotterdam harbour with Katendrecht on the peninsula', 'Katendrecht is the peninsula in the middle. The studio is at the end nearest the bridge.', lightbox=False)),
    (None, J(heading('Come by the studio', 3),
             table([['Address', 'Deliplein 14, 3072 CT Rotterdam'], ['Getting here', 'Metro to Rijnhaven, then 8 minutes on foot, or the water taxi to Hotel New York'],
                    ['Open', 'The window is open whenever someone is on air. Knock during the songs, not the talking'], ['Step-free', 'Yes, one small ramp at the door']]),
             para('The record fair on the Deliplein, first Saturday of the month, is when most of us are around.', fontSize='small'))), align='wide'))

pattern('about-station', 'About the station', 'about', cols(
    ('55%', J(heading('Radio for Rotterdam, made by people who live here', 2),
              para('Radio Havik started in 2018 in the back of Fietsen Bram, a bike shop on the Deliplein that closed the year before. Bram left us the counter, which is now the desk. We are on the internet and DAB+, 24 hours a day, with 61 presenters who all have other jobs.'),
              para('We play what the presenters love and we try to sound like the city, which means a lot of Dutch rap, dub, kaseko and records nobody else would play. We do not run adverts. We do run a lot of fundraisers.'))),
    (None, image('studio.jpg', 'A presenter in a knitted hat and scarf sitting beside two studio microphones, resting his head on his hand', 'Sem van Dijk before Klankkast', lightbox=False, className='is-style-bw')), align='wide'))

pattern('listen-options', 'Ways to listen', 'text', J(
    heading('Ways to listen', 3),
    table([['In the browser', 'The player at the bottom of every page'], ['Stream for apps and smart speakers', 'stream.example.com/radiohavik-128.mp3 (or -320 for high quality)'],
           ['DAB+', 'Block 11C, Rotterdam and Schiedam. Search for "Havik"'], ['Old episodes', 'The <a href="/archive/">Listen back</a> page, back to 2019']]),
    para('Studio phone during live shows: 010 555 0199. Texts are read out, calls sometimes go on air.', fontSize='small')))

pattern('page-schedule', 'Page: schedule', 'featured', J(pattern_ref('schedule-week'), pattern_ref('shows-index')), block_types='core/post-content')
pattern('page-shows', 'Page: shows and residents', 'about', J(pattern_ref('residents-grid'), pattern_ref('shows-index'), pattern_ref('guest-mix-series')), block_types='core/post-content')
pattern('page-support', 'Page: support', 'call-to-action', J(pattern_ref('support-costs'), pattern_ref('membership-levels')), block_types='core/post-content')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('about-station'), pattern_ref('listen-options'), pattern_ref('find-the-studio'), pattern_ref('newsletter')), block_types='core/post-content')

# ------------------------------------------------------------------ templates
main_pad = {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}
def tpl(main):
    return J(template_part('header', 'header'), group(main, tag='main', style=main_pad), template_part('footer', 'footer'), template_part('player'))
sp = lambda x, cls=None, sz='70': group(x, align='wide', className=cls, layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|' + sz}}})
write('templates/front-page.html', tpl(J(
    pattern_ref('now-next'),
    sp(pattern_ref('schedule-week')),
    sp(pattern_ref('episode-index')),
    sp(pattern_ref('episode-tiles'), sz='50'),
    group(pattern_ref('support-costs'), align='full', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    sp(pattern_ref('residents-grid')),
    sp(cols((None, pattern_ref('submit-callout')), (None, pattern_ref('newsletter')), align='wide'), sz='60'))))
write('templates/home.html', tpl(J(heading('Listen back', 1, align='wide'), para('Every episode from every show, newest first. Filter by show from the <a href="/shows/">shows page</a>.', align='wide'),
    pattern_ref('episode-index-archive'), pattern_ref('genre-index'))))
cat_tpl = J(
    cols(('30%', J(dyn('query-title', type='archive', showPrefix=False, level=1, fontSize='xx-large'), dyn('term-description'),
                   para('<a href="/schedule/">When it is on</a>', fontSize='small'))),
         (None, pattern_ref('episode-index-archive')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))
write('templates/archive.html', tpl(cat_tpl))
write('templates/category.html', tpl(cat_tpl))
write('templates/index.html', tpl(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list'))))
write('templates/search.html', tpl(J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, buttonText='Search', placeholder='A show, an artist, a track', align='wide'), pattern_ref('post-list'))))
write('templates/404.html', tpl(J(heading('Nothing on this frequency', 1), para('That page does not exist. The live stream is still playing at the bottom of the screen.'),
    dyn('search', label='Search', showLabel=False, buttonText='Search'), para('<a href="/schedule/">See the schedule</a>'))))
write('templates/page.html', tpl(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', tpl(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1440px'}))))
write('templates/single.html', tpl(J(dyn('post-date', format='l j F Y'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/single-episode.html', tpl(J(
    cols(('30%', J(dyn('post-featured-image', aspectRatio='1', scale='cover', className='is-style-bw'),
                   dyn('post-terms', term='category', fontSize='large'), dyn('post-date', format='l j F Y, H:i'),
                   dyn('post-terms', term='post_tag', separator=', '))),
         (None, J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', moreText='', fontSize='large'), dyn('post-content', layout={'type': 'default'}))),
         align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Earlier', showTitle=True, taxonomy='category'), dyn('post-navigation-link', label='Later', showTitle=True, taxonomy='category')), justify='space-between'),
          className='is-style-rule-top', align='wide'))))

# ------------------------------------------------------------------ demo content
def ep(intro, rows, url, cap):
    return J(audio(url, caption=cap), para(intro), heading('Tracklist', 3), table([list(r) for r in rows], head=['Time', 'Artist', 'Track']))
posts = [
    {'title': 'Mikey Blanco live in the studio', 'category': 'kapsalon', 'tags': ['Hip-hop', 'Nederrap'], 'image': 'headphones.jpg', 'template': 'single-episode',
     'excerpt': 'A live verse at 20:21, two new Winne tracks and a busy phone line.', 'pattern': 'freq/episode-body'},
    {'title': 'Dub from the Maashaven, with Kofi', 'category': 'maashaven-dub', 'tags': ['Dub', 'Roots'], 'image': 'turntable.jpg', 'template': 'single-episode',
     'excerpt': 'Two hours of steppers and one very long King Tubby version.',
     'content': ep('Kofi brought a box of Jah Shaka pressings and played them in order of how scratched they are.', [('21:00', 'Jah Shaka', 'Commandments of Dub'), ('21:12', 'King Tubby', 'Declaration of Rights (version)'), ('21:30', 'Mad Professor', 'Kunta Kinte Dub')],
                   'https://stream.example.com/archive/maashaven-dub-2026-09-23.mp3', 'Maashaven Dub, 23 September, 2 hours')},
    {'title': 'Live electronics from Codarts students', 'category': 'klankkast', 'tags': ['Experimental', 'Live'], 'image': 'laptop.jpg', 'template': 'single-episode',
     'excerpt': 'Three students from the sonology course played live on the desk.',
     'content': ep('Sem invited three second-year students from Codarts. Each played 30 minutes live. Nobody knew what the others were going to do, including Sem.', [('22:00', 'Anouk Veld', 'Sine study, live'), ('22:30', 'Tariq Haddou', 'Feedback in C'), ('23:00', 'Mei Lin', 'Havenkraan, live')],
                   'https://stream.example.com/archive/klankkast-2026-09-24.mp3', 'Klankkast, 24 September, 1 hour 30 minutes')},
    {'title': 'Charity shop finds from Crooswijk', 'category': 'tweede-hands', 'tags': ['Soul', 'Nederpop'], 'image': 'records.jpg', 'template': 'single-episode',
     'excerpt': 'Everything tonight cost €1 or less at the Leger des Heils shop.',
     'content': ep('Jaap spent €14 at the charity shop in Crooswijk and plays all of it, including the one with a coffee ring on side B.', [('20:00', 'Earth and Fire', 'Weekend'), ('20:08', 'Cuby and the Blizzards', 'Window of my Eyes'), ('20:15', 'Anita Meyer', 'Why Tell Me Why')],
                   'https://stream.example.com/archive/tweede-hands-2026-09-22.mp3', 'Tweede Hands, 22 September, 2 hours')},
    {'title': 'Kaseko for a wet Sunday', 'category': 'zondagse-kaseko', 'tags': ['Kaseko', 'Surinamese pop'], 'image': 'sax.jpg', 'template': 'single-episode',
     'excerpt': 'Ramona plays the records her father brought from Paramaribo in 1975.',
     'content': ep('It rained all afternoon, so Ramona played her father\'s records in the order he packed them in 1975.', [('14:00', 'Lieve Hugo', 'Na Mi Na Yu'), ('14:09', 'Max Nijman', 'Wan Bon'), ('14:20', 'Trafassi', 'Kaseko Medley')],
                   'https://stream.example.com/archive/kaseko-2026-09-21.mp3', 'Zondagse Kaseko, 21 September, 2 hours')},
    {'title': 'Nachtbus, the 3am special', 'category': 'nachtbus', 'tags': ['Ambient', 'Classical'], 'image': 'cello.jpg', 'template': 'single-episode',
     'excerpt': 'For the night shift at the port. Slow cello, rain and the BN bus announcements.',
     'content': ep('Iris does this one for the people working nights at the port. Slow music and the odd announcement from the night bus.', [('23:00', 'Arthur Russell', 'Tower of Meaning'), ('23:20', 'Hildur Guðnadóttir', 'Bathroom Dance'), ('23:40', 'Joep Beving', 'Sleeping Lotus')],
                   'https://stream.example.com/archive/nachtbus-2026-09-19.mp3', 'Nachtbus, 19 September, 2 hours')},
    {'title': 'Buurtpraat: the new ferry timetable', 'category': 'buurtpraat', 'tags': ['Talk', 'Katendrecht'], 'image': 'accordion.jpg', 'template': 'single-episode',
     'excerpt': 'Neighbours on the Watertaxi changes and what the market is doing about Saturday parking.',
     'content': ep('Four neighbours on the new water taxi timetable, the Saturday market and the plan to close the Rechthuislaan to cars.', [('11:00', 'Talk', 'The water taxi, with Henk from the Kaapse Maria'), ('11:25', 'Doe Maar', 'Sinds 1 dag of 2'), ('11:30', 'Talk', 'Market parking, with the Deliplein traders')],
                   'https://stream.example.com/archive/buurtpraat-2026-09-20.mp3', 'Buurtpraat, 20 September, 1 hour')},
    {'title': 'Fenna and Ruud with the Feyenoord kit man', 'category': 'ochtend-op-de-kade', 'tags': ['Talk', 'New music'], 'image': 'drummer.jpg', 'template': 'single-episode',
     'excerpt': 'Breakfast with the man who washes 400 shirts a week, and six new Dutch releases.',
     'content': ep('Two hours of breakfast radio. Ruud interviewed the kit man at Feyenoord about washing 400 shirts a week, and Fenna played six new Dutch releases.', [('08:05', 'Froukje', 'Groter Dan Ik'), ('08:30', 'Talk', 'The kit man'), ('09:10', 'Goldband', 'Noodgeval')],
                   'https://stream.example.com/archive/ochtend-2026-09-25.mp3', 'Ochtend op de Kade, 25 September, 2 hours')},
]
content = {
    'site': {'title': 'Radio Havik', 'tagline': 'Community radio from Katendrecht, Rotterdam'},
    'categories': [{'slug': k, 'name': v[0], 'description': '%s. Presented by %s.' % (v[2], v[1])} for k, v in SHOWS.items()],
    'front_page': 'home', 'posts_page': 'archive',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'schedule', 'title': 'Schedule', 'pattern': 'freq/page-schedule', 'template': 'page-wide'},
        {'slug': 'shows', 'title': 'Shows', 'pattern': 'freq/page-shows', 'template': 'page-wide'},
        {'slug': 'archive', 'title': 'Listen back', 'content': ''},
        {'slug': 'support', 'title': 'Support', 'pattern': 'freq/page-support', 'template': 'page-wide'},
        {'slug': 'submit-a-show', 'title': 'Submit a show', 'pattern': 'freq/submit-a-show'},
        {'slug': 'about', 'title': 'About', 'pattern': 'freq/page-about', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Schedule', 'url': '/schedule/'}, {'label': 'Shows', 'url': '/shows/'}, {'label': 'Listen back', 'url': '/archive/'},
            {'label': 'Support', 'url': '/support/'}, {'label': 'Submit a show', 'url': '/submit-a-show/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs('demos/freq', exist_ok=True)
json.dump(content, open('demos/freq/content.json', 'w'), indent=1, ensure_ascii=False)
open('demos/freq/fonts-claim.txt', 'w').write('display: Radio Canada (registry face for 046, unchanged)\n')
print('freq built')
