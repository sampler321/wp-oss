# bpm: Hania Sokol, a DJ and producer in Warsaw with a monthly radio residency.
# Direction: NTS-style night utility. Black page, white 1px rules, everything that is a label set in Mona Sans
#   squeezed to 75% width and uppercase, like a station schedule; body text in the same family at normal width.
#   From Radio Kapital: stacked offset frames behind artwork and an orange "on air" strip under the header.
# Fonts: Mona Sans only (claimed for 040; the brief moves away from the registry's Audiowide), wdth 75 for display.
# Palette: #0C0C0C night, #F1F1EE type, #FF6A13 sodium orange for play, live and tickets only, #1B1B1B surface.
# Layout idea: the mix page is a broadcast record, player first, then a three-column timestamped tracklist.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('bpm')
import blocks as _B
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
        out.append('<!-- wp:column%s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:column -->' % ((' ' + json.dumps(ca, separators=(',', ':'))) if ca else '', cls, st, inner))
    a = attrs
    va = ('are-vertically-aligned-' + a['verticalAlignment']) if a.get('verticalAlignment') else ''
    return '<!-- wp:columns%s -->\n<div class="%s"%s>%s</div>\n<!-- /wp:columns -->' % ((' ' + json.dumps(a, separators=(',', ':'))) if a else '', ' '.join(filter(None, ['wp-block-columns', 'align' + a['align'] if a.get('align') else '', va, a.get('className', '')])), _B._style(a), '\n\n'.join(out))

def cover_featured(inner, min_vh=70, dim=30, position='bottom left', **attrs):
    a = {'useFeaturedImage': True, 'dimRatio': dim, 'overlayColor': 'base', 'isUserOverlayColor': True, 'minHeight': min_vh, 'minHeightUnit': 'vh',
         'contentPosition': position, **attrs}
    pos = position.replace(' ', '-')
    cls = 'wp-block-cover has-custom-content-position is-position-%s' % pos + ((' ' + attrs['className']) if attrs.get('className') else '')
    return ('<!-- wp:cover %s -->\n<div class="%s" style="min-height:%dvh"><span aria-hidden="true" class="wp-block-cover__background has-base-background-color has-background-dim-%d has-background-dim"></span>'
            '<div class="wp-block-cover__inner-container">%s</div></div>\n<!-- /wp:cover -->') % (json.dumps(a, separators=(',', ':')), cls, min_vh, dim, inner)

# ------------------------------------------------------------------ theme.json
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
display = next(f for f in fonts if f['slug'] == 'display')
PAL = [
    ('base', '#0C0C0C', 'Night'),
    ('contrast', '#F1F1EE', 'Strip light'),
    ('accent', '#FF6A13', 'Sodium orange'),
    ('surface', '#1B1B1B', 'Booth'),
    ('line', '#F1F1EE', 'Rule'),
    ('muted', '#A3A3A3', 'Smoke'),
]
def palette(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1400px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True,
            'fontFamilies': [display, {'fontFamily': display['fontFamily'], 'name': 'Mona Sans (text)', 'slug': 'body'}],
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Tag', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.625rem', 'name': 'Large', 'fluid': {'min': '1.375rem', 'max': '1.625rem'}},
                {'slug': 'x-large', 'size': '2.5rem', 'name': 'Section', 'fluid': {'min': '2rem', 'max': '2.5rem'}},
                {'slug': 'xx-large', 'size': '4.5rem', 'name': 'Title', 'fluid': {'min': '2.75rem', 'max': '4.5rem'}},
                {'slug': 'display', 'size': '9rem', 'name': 'Display', 'fluid': {'min': '3.5rem', 'max': '9rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': [
            {'slug': 'stack', 'name': 'Stacked frames', 'shadow': '8px 8px 0 -1px var(--wp--preset--color--base), 8px 8px 0 0 var(--wp--preset--color--contrast), 16px 16px 0 -1px var(--wp--preset--color--base), 16px 16px 0 0 var(--wp--preset--color--contrast)'},
        ]},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': V('base'), 'text': V('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': V('accent')}},
                     ':focus': {'outline': {'color': V('accent'), 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '0.92', 'letterSpacing': '0', 'textTransform': 'uppercase'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.2'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.2'}},
            'button': {'color': {'background': V('contrast'), 'text': V('base')},
                       'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': V('contrast')},
                       'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|medium', 'textTransform': 'uppercase', 'lineHeight': '1'},
                       'spacing': {'padding': {'top': '0.7em', 'bottom': '0.65em', 'left': '1em', 'right': '1em'}},
                       ':hover': {'color': {'background': V('accent'), 'text': V('base')}, 'border': {'color': V('accent')}},
                       ':focus': {'outline': {'color': V('accent'), 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': V('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|large', 'textTransform': 'uppercase', 'lineHeight': '1'},
                                'border': {'width': '1px', 'style': 'solid', 'color': V('contrast')},
                                'spacing': {'padding': {'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
                                'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|medium', 'fontWeight': '600', 'textTransform': 'uppercase'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': V('accent')}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': V('contrast')}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': V('accent')}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'textTransform': 'uppercase', 'fontWeight': '600'}, 'color': {'text': V('muted')}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'textTransform': 'uppercase', 'fontWeight': '600'}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.45'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/image': {'border': {'radius': '0'}},
            'core/cover': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': V('line')}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '700', 'lineHeight': '1', 'textTransform': 'uppercase'},
                           'border': {'width': '1px', 'style': 'solid', 'color': V('contrast')},
                           'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
                           'elements': {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '400', 'textTransform': 'none'}}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '800', 'textTransform': 'uppercase', 'lineHeight': '0.95'},
                               'border': {'top': {'color': V('accent'), 'width': '4px', 'style': 'solid'}, 'bottom': {'color': V('accent'), 'width': '4px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/embed': {'border': {'width': '1px', 'style': 'solid', 'color': V('contrast')}},
            'core/audio': {'border': {'width': '1px', 'style': 'solid', 'color': V('contrast')}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'textTransform': 'uppercase'}},
            'core/search': {'border': {'radius': '0'}},
        },
        'css': ('body{font-synthesis:none;font-variant-numeric:tabular-nums}'
                ':where(h1,h2,h3,h4,h5,h6),.wp-block-site-title,.wp-block-navigation,.wp-element-button,.wp-block-post-terms,.wp-block-post-date,.wp-block-query-pagination,.wp-block-quote,.wp-block-pullquote,.wp-block-table th{font-stretch:75%}'
                ':where(h1,h2,h3,h4){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.6em .8em .6em 0;text-align:left;vertical-align:top}'
                '.wp-block-table thead{border-bottom:1px solid var(--wp--preset--color--line)}.wp-block-table th{font-family:var(--wp--preset--font-family--display);font-weight:700;text-transform:uppercase}'
                '.wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:0;background:transparent;color:inherit}'
                '.wp-block-navigation .current-menu-item>a,.wp-block-navigation a[aria-current]{color:var(--wp--preset--color--accent)}'
                '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast)}'
                ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
                '.wp-block-embed a{color:var(--wp--preset--color--accent)}.wp-block-embed__wrapper{padding:1rem;font-weight:600}'
                '@media (min-width:782px){.is-style-sticky-col{position:sticky;top:var(--wp--preset--spacing--40);align-self:flex-start}}'),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header with on-air strip'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Show moved notice'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-mix', 'title': 'Mix or episode (player and tracklist)', 'postTypes': ['post']},
    ],
}
wjson('theme.json', theme)

write('style.css', '''/*
Theme Name: BPM
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A dark, tabular theme for DJs, producers and small radio shows that publish numbered mixes with timestamped tracklists, dates and booking contacts.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: bpm
Tags: dark, entertainment, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def variation(name, title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': palette(pal)}}}
    if extra:
        d['styles'] = extra
    wjson('styles/%s.json' % name, d)

variation('daytime', 'Daytime', [('base', '#F2F2EE', 'Night'), ('contrast', '#121212', 'Strip light'), ('accent', '#B8430A', 'Sodium orange'),
    ('surface', '#E4E4DE', 'Booth'), ('line', '#121212', 'Rule'), ('muted', '#5E5E5E', 'Smoke')])
variation('dub', 'Dub', [('base', '#0E1B16', 'Night'), ('contrast', '#E6EFE4', 'Strip light'), ('accent', '#9FD4A3', 'Sodium orange'),
    ('surface', '#15271F', 'Booth'), ('line', '#E6EFE4', 'Rule'), ('muted', '#A9BBAE', 'Smoke')])
variation('warehouse', 'Warehouse', [('base', '#1A1A1A', 'Night'), ('contrast', '#FFFFFF', 'Strip light'), ('accent', '#FFFFFF', 'Sodium orange'),
    ('surface', '#262626', 'Booth'), ('line', '#FFFFFF', 'Rule'), ('muted', '#BDBDBD', 'Smoke')],
    {'elements': {'heading': {'typography': {'fontWeight': '900'}}}})

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('tag-boxes', 'Tag boxes', ['core/post-terms'], {
    'css': '& a{display:inline-block;border:1px solid currentColor;padding:.2em .5em .15em;margin:0 .4em .4em 0;text-decoration:none;color:inherit}& a:hover{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}& .wp-block-post-terms__separator{display:none}'})
section('stacked', 'Stacked frames', ['core/post-featured-image', 'core/image', 'core/group', 'core/embed'], {
    'shadow': 'var:preset|shadow|stack',
    'border': {'width': '1px', 'style': 'solid', 'color': V('contrast')},
    'css': '&{margin-right:16px;margin-bottom:16px}'})
section('on-air', 'On-air strip', ['core/group'], {
    'border': {'top': {'width': '1px', 'style': 'solid', 'color': V('contrast')}, 'bottom': {'width': '1px', 'style': 'solid', 'color': V('contrast')}},
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'textTransform': 'uppercase', 'fontSize': 'var:preset|font-size|medium'},
    'css': '&{font-stretch:75%}& p{margin:0}'})
section('live-box', 'Live box', ['core/paragraph'], {
    'color': {'background': V('accent'), 'text': V('base')},
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'textTransform': 'uppercase'},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
    'elements': {'link': {'color': {'text': V('base')}}},
    'css': '&{font-stretch:75%}'})
section('plate', 'Title plate', ['core/group'], {
    'color': {'background': V('base'), 'text': V('contrast')},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
    'css': '&{max-width:36rem}'})
section('tracklist', 'Tracklist', ['core/table'], {
    'css': '& td:first-child{color:var(--wp--preset--color--accent);font-weight:700;width:5.5em;white-space:nowrap}& td:nth-child(2){font-weight:700;text-transform:uppercase;font-stretch:75%;font-family:var(--wp--preset--font-family--display);font-size:1.15em;width:38%}'})
section('dates', 'Dates table', ['core/table'], {
    'css': '& td:first-child{font-family:var(--wp--preset--font-family--display);font-weight:800;text-transform:uppercase;font-stretch:75%;font-size:1.4em;line-height:1;white-space:nowrap}& td:last-child a{color:var(--wp--preset--color--accent)}& del{color:var(--wp--preset--color--muted)}'})
section('boxed', 'Boxed', ['core/group', 'core/column'], {
    'border': {'width': '1px', 'style': 'solid', 'color': V('contrast')},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('inverse', 'Inverse', ['core/group', 'core/column'], {
    'color': {'background': V('contrast'), 'text': V('base')},
    'elements': {'link': {'color': {'text': V('base')}}, 'heading': {'color': {'text': V('base')}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
    'css': '& .wp-block-table td,& .wp-block-table th,& .wp-block-table thead{border-color:var(--wp--preset--color--base)}& .wp-element-button{background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast);border-color:var(--wp--preset--color--base)}'})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('index-row', 'Archive index row', ['core/group'], {
    'border': {'bottom': {'color': V('line'), 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
    'css': '&:hover{background:var(--wp--preset--color--surface)}'})
section('grid-tile', 'Mix tile', ['core/post-template'], {
    'css': '& > li{border-top:1px solid var(--wp--preset--color--line);padding-top:var(--wp--preset--spacing--30)}'})

# ------------------------------------------------------------------ parts
onair = group(row(J(
    para('On air Thursday 21:00', className='is-style-live-box'),
    para('Szum, monthly on Radio Wola 98.4 FM, Warsaw. Next: 2 October with Kaja Ptak'),
    para('<a href="/radio/">Schedule and listen live</a>')), justify='space-between', align='wide',
    style={'spacing': {'blockGap': 'var:preset|spacing|30'}}),
    className='is-style-on-air', align='full', layout={'type': 'constrained'})
write('parts/header.html', group(J(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}, overlayMenu='mobile')),
        justify='space-between', wrap=False, align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}),
    pattern_ref('on-air-strip')), tag='header', align='full', layout={'type': 'constrained'},
    style={'spacing': {'blockGap': '0'}}))
write('parts/notice.html', pattern_ref('notice-show-moved'))
write('parts/footer.html', group(J(
    cols(('40%', J(heading('Hania Sokół', 3), para('DJ and producer in Warsaw. Szum on Radio Wola, first Thursday of the month, 21:00 to 23:00 Warsaw time. Records on Nowy Świat Dźwięku and her own label, Szum Nagrania.', fontSize='small'))),
         (None, J(heading('Booking', 6), para('Europe: <a href="mailto:lena@example.com">Lena Hartmann</a><br>Poland and the Baltics: <a href="mailto:kuba@example.com">Kuba Wrona</a><br>Radio and press: <a href="mailto:hania@example.com">Hania directly</a>', fontSize='small'))),
         (None, J(heading('Elsewhere', 6), para('<a href="https://www.mixcloud.com/">Mixcloud</a><br><a href="https://soundcloud.com/">SoundCloud</a><br><a href="https://bandcamp.com/">Bandcamp</a><br><a href="https://www.instagram.com/">Instagram</a>', fontSize='small'))),
         align='wide'),
    para('Demo photos are CC0 images from Wikimedia Commons and Unsplash, used as stand-ins.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-rule-top',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ------------------------------------------------------------------ patterns
pattern('on-air-strip', 'On-air strip (next broadcast)', 'banner', onair, description='A strip under the header with the next broadcast. Change the day, time and guest each month.')

pattern('notice-show-moved', 'Notice: show moved', 'banner', group(
    para('This month Szum moves to Friday 3 October, 22:00, because of the station\'s fundraiser night. Same frequency, same stream.', fontSize='small'),
    className='is-style-inverse', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}))

hero_plate = group(J(
    row(J(dyn('post-terms', term='category', className='is-style-tag-boxes'), dyn('post-date', format='j M Y'))),
    dyn('post-title', level=2, isLink=True, fontSize='xx-large'),
    dyn('post-terms', term='post_tag', className='is-style-tag-boxes'),
    dyn('post-excerpt', moreText='', excerptLength=30)), className='is-style-plate', layout={'type': 'default'})
pattern('hero-latest-mix', 'Hero: latest mix on a full image', 'featured,query', cols(
    ('66%', query(cover_featured(hero_plate, min_vh=72, dim=20), per_page=1, query_id=21)),
    (None, J(heading('Coming up', 4), pattern_ref('dates-compact'), para('<a href="/dates/">All dates</a>', fontSize='small'),
             group(J(heading('Szum 058 is up', 4), para('Two hours with Kaja Ptak: Polish jazz on 45, broken beat, one Komeda edit that took three weeks to get right.', fontSize='small'),
                     buttons(('Play the latest mix', '/mixes/'))), className='is-style-boxed'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}), description='The newest mix fills the left, with its tags on a black plate. Dates sit on the right.')

tile = J(dyn('post-featured-image', isLink=True, aspectRatio='4/5', scale='cover', className='is-style-stacked'),
         row(J(dyn('post-terms', term='category'), dyn('post-date', format='j M Y')), justify='space-between'),
         dyn('post-title', isLink=True, level=3, fontSize='large'),
         dyn('post-terms', term='post_tag', className='is-style-tag-boxes'))
pattern('mix-grid', 'Mix grid (latest 8)', 'featured,query', group(J(
    row(J(heading('Mixes', 2), para('<a href="/mixes/">Archive index, every mix by date</a>', fontSize='small')), justify='space-between', align='wide'),
    query(tile, per_page=8, query_id=22, align='wide', template_class='is-style-grid-tile', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '15rem'})),
    align='wide', layout={'type': 'default'}), keywords='mixes, episodes, archive')
pattern('mix-grid-archive', 'Mix grid (inherits the page query)', 'query', inherit_query(tile, align='wide', template_class='is-style-grid-tile',
        layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '15rem'}), inserter=False)

index_row = group(cols(
    ('14%', dyn('post-date', format='d.m.Y')),
    ('46%', dyn('post-title', isLink=True, level=3, fontSize='large')),
    (None, dyn('post-terms', term='post_tag', className='is-style-tag-boxes')),
    ('12%', dyn('post-terms', term='category')), style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}}}, verticalAlignment='center'),
    className='is-style-index-row', layout={'type': 'default'})
pattern('mix-index', 'Archive index: every mix by date', 'query', inherit_query(index_row, align='wide'), inserter=False,
        description='A dense list for crate-digging: date, title, genres, show.')
pattern('post-list', 'Post list', 'posts,query', inherit_query(index_row, align='wide'), inserter=False)

TRACKS_058 = [('00:00', 'Krzysztof Komeda', 'Svantetic (Hania edit)'), ('06:12', 'Skalpel', 'Break Out'), ('11:40', 'Marek Biliński', 'Ogród Króla Świtu'),
              ('17:05', 'Tomasz Stańko Quartet', 'Suspended Night Variation IV'), ('24:30', 'Kaja Ptak', 'Tramwaj 18 (unreleased)'),
              ('31:15', 'Sadar Bahar', 'Soul Sides'), ('38:02', 'Kaja Ptak and Hania Sokół', 'Praga, 4am (live on air)'), ('46:50', 'Novika', 'Tricks of the Light')]
def tracklist(rows):
    return table([list(r) for r in rows], head=['Time', 'Artist', 'Title'], className='is-style-tracklist')
pattern('tracklist', 'Tracklist with timestamps', 'text', J(heading('Tracklist', 3), tracklist(TRACKS_058),
        para('Times are from the start of the Mixcloud upload. The radio broadcast starts four minutes later because of the news.', fontSize='x-small', textColor='muted')),
        description='Three columns: time, artist, title. Put your own edits in brackets.')

pattern('mix-meta', 'Mix details (broadcast, location, length)', 'text', table([
    ['Broadcast', 'Radio Wola 98.4 FM, Thursday 4 September, 21:00 Warsaw time'], ['Recorded', 'Studio 2, ul. Wolska 40, Warsaw'],
    ['Length', '1 hour 58 minutes'], ['Guest', 'Kaja Ptak, producer, Kraków']], className='is-style-dates'))

pattern('mix-qa', 'Short Q&A with the mix', 'text', J(
    heading('Five questions for Kaja', 3),
    details('Where did you record your half?', para('At home in Podgórze, on two Technics and a mixer I borrowed from my brother in 2019 and never gave back.')),
    details('What is the Komeda edit?', para('Hania looped the piano intro for three minutes before the band comes in. It took her three weeks and she is still not happy with the joins.')),
    details('One record you would never play out?', para('My dad\'s copy of Czesław Niemen. It skips in the one place you want it not to.')),
    details('What are you working on?', para('An EP for Nowy Świat Dźwięku, out in spring, all made on a broken Casio CZ-101.')),
    details('Best place to eat after a set in Warsaw?', para('Bar Prasowy on Marszałkowska. Open at 6am, pierogi for 18 zł.'))))

pattern('mix-player', 'Mix player (Mixcloud embed)', 'media', J(
    embed('https://www.mixcloud.com/radiowola/szum-058-w-kaja-ptak/', provider='mixcloud', type_='rich'),
    para('Also on <a href="https://soundcloud.com/">SoundCloud</a>. Downloads for Bandcamp supporters only.', fontSize='x-small', textColor='muted')),
    description='Paste a Mixcloud or SoundCloud URL into the embed. It sits at the top of the mix page.')

pattern('series-note', 'About the numbered series', 'text', group(J(
    heading('Why the numbers', 4),
    para('Every Szum show gets a number, so you can ask for "the one with the Komeda edit" as 058 and I will know. The numbers started in 2019. 001 to 012 were on a pirate stream and are lost, sorry.', fontSize='small')),
    className='is-style-boxed'))

DATES = [('Fri 3 Oct', 'Jasna 1', 'Warsaw', '<a href="https://example.com/tickets">Tickets</a>'),
         ('Sat 11 Oct', 'Hala Koszyki, Unsound opening', 'Kraków', '<a href="https://example.com/tickets">Tickets</a>'),
         ('Fri 24 Oct', 'Tresor, Globus floor', 'Berlin', '<a href="https://example.com/tickets">Tickets</a>'),
         ('Sat 8 Nov', 'Pogłos', 'Warsaw', 'Free before midnight'),
         ('Sat 22 Nov', 'De School', 'Amsterdam', '<del>Cancelled</del>'),
         ('Fri 12 Dec', 'Ptaszarnia', 'Wrocław', '<a href="https://example.com/tickets">Tickets</a>')]
pattern('dates-table', 'Dates (date, venue, city, tickets)', 'text', J(
    heading('Dates', 2), table([list(d) for d in DATES], head=['Date', 'Venue', 'City', ''], className='is-style-dates'),
    para('Dates marked cancelled stay on the list for a month, so people who bought tickets can find them.', fontSize='x-small', textColor='muted')))
pattern('dates-compact', 'Dates (compact, next four)', 'text', table([[d[0], '%s, %s' % (d[1], d[2])] for d in DATES[:4]], className='is-style-dates'))
pattern('dates-past', 'Past dates', 'text', J(heading('Played this year', 4), para(
    'Instytut Dźwięku, Warsaw. Garage, Tbilisi. Łaźnia Nowa, Kraków. Radio Wola summer marathon, 11 hours. Club To Tu, Szczecin. Nowe Miasto rooftop, Łódź. Rote Sonne, Munich.', fontSize='small')))

pattern('radio-today', 'Radio: today\'s schedule with timezone', 'text', J(
    heading('Thursday on Radio Wola', 3),
    table([['18:00', '20:00', 'Rzeka, with Ola Zawada', 'Ambient and field recordings'],
           ['20:00', '21:00', 'News in Polish and Ukrainian', ''],
           ['21:00', '23:00', '<strong>Szum, with Hania Sokół</strong>', 'Live from Studio 2'],
           ['23:00', '01:00', 'Nocny Autobus, with DJ Jola', 'Italo and cold wave']], head=['From', 'To', 'Show', ''], className='is-style-tracklist'),
    para('All times are Warsaw time (CET, or CEST in summer). Listen on 98.4 FM in Warsaw or on the stream everywhere else.', fontSize='small')),
    description='Today\'s schedule for a radio residency. Always state the timezone.')

pattern('residency', 'Radio residency', 'text', cols(
    ('45%', image('warsaw.jpg', 'The Palace of Culture and Science lit blue at night, with office towers on the left', 'Radio Wola broadcasts from Wola, ten minutes from here by tram 22')),
    (None, J(heading('Szum on Radio Wola', 2),
             para('First Thursday of every month since 2019, 21:00 to 23:00. Two hours, usually with a guest for the second hour. Radio Wola is a volunteer station on 98.4 FM with a stream, run out of an old print works on ul. Wolska.'),
             para('I play what I cannot play in clubs: Polish jazz, library records, dub, and whatever the guest brings. No requests, but you can send me a record if you really want me to hear it.'),
             buttons(('Listen live on Thursday', 'https://example.com/radiowola-stream'), ('Every past show', '/mixes/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='center'))

pattern('releases-table', 'Releases', 'text', J(
    heading('Releases', 2),
    table([['SZUM003', '<em>Wolska 40</em> EP', 'Szum Nagrania', '2026', '12", digital'],
           ['NSD017', '<em>Tramwaj</em> with Kaja Ptak', 'Nowy Świat Dźwięku', '2025', '12", digital'],
           ['SZUM002', '<em>Niskie Częstotliwości</em>', 'Szum Nagrania', '2024', 'Cassette, digital'],
           ['SZUM001', '<em>Pierwsza</em> EP', 'Szum Nagrania', '2022', 'Digital']],
          head=['Cat no', 'Title', 'Label', 'Year', 'Formats'], className='is-style-dates'),
    buttons(('Buy on Bandcamp', 'https://bandcamp.com/'))))
pattern('release-feature', 'Release feature', 'featured', cols(
    ('45%', image('records.jpg', 'Rows of LP sleeves in a record shop crate, photographed at an angle', lightbox=False, className='is-style-stacked')),
    (None, J(heading('Wolska 40', 2), para('New EP, out 17 October on Szum Nagrania. Four tracks made in the radio studio after hours, on the station\'s Roland MC-909 and a Juno borrowed from the breakfast show.'),
             table([['A1', 'Wolska 40', '6:40'], ['A2', 'Studio 2', '5:12'], ['B1', 'Po wiadomościach', '7:03'], ['B2', 'Nadajnik', '8:20']], className='is-style-tracklist'),
             buttons(('Pre-order the 12"', 'https://bandcamp.com/')))), align='wide', verticalAlignment='top'))

pattern('booking-territories', 'Booking contacts by territory', 'contact', J(
    heading('Booking', 2),
    table([['Europe (not Poland)', 'Lena Hartmann, Fluss Agency, Berlin', '<a href="mailto:lena@example.com">lena@example.com</a>'],
           ['Poland and the Baltics', 'Kuba Wrona, Dźwięk Agency, Warsaw', '<a href="mailto:kuba@example.com">kuba@example.com</a>'],
           ['Everywhere else', 'Hania directly', '<a href="mailto:hania@example.com">hania@example.com</a>'],
           ['Radio, press, podcasts', 'Hania directly', '<a href="mailto:hania@example.com">hania@example.com</a>']],
          head=['Where', 'Who', 'Email'], className='is-style-dates'),
    para('Please give us six weeks for club dates and three months for festivals. I play four hours or less, and I do not play before 23:00 unless it is a radio show or a record shop.', fontSize='small')))

pattern('tech-rider', 'Technical rider', 'text', J(
    heading('Rider', 4),
    lst(['Two Technics SL-1210 MK2 with good needles, or I bring my own Ortofons', 'Two Pioneer CDJ-3000 or CDJ-2000NXS2, linked', 'Allen & Heath Xone:92 or Pioneer DJM-900', 'Booth monitors at head height, not on the floor', 'A table that does not wobble']),
    para('No smoke machine in the booth. It gets in the records.', fontSize='small')))

pattern('press-pack', 'Press photos and bio download', 'media', J(
    heading('Press pack', 2),
    gallery([('dj-4.jpg', 'A DJ playing to a packed outdoor crowd at night under blue light', 'Closing set, summer 2025. Photo: Marta Nowak'),
             ('headphones.jpg', 'A DJ in headphones at a lit-up booth with a city skyline behind', 'Rooftop set, Łódź. Photo: Piotr Rak'),
             ('mixer.jpg', 'A black DJ mixer with rows of knobs, photographed close up', 'The booth at Jasna 1. Photo: Hania Sokół')], columns=3),
    para('All photos are free to use for press with the photographer credited. Each is 3000 px on the long side.', fontSize='small'),
    buttons(('Download photos and bio (ZIP, 48 MB)', 'https://example.com/hania-sokol-press.zip'))))

pattern('bio', 'Bio (short and long)', 'about', cols(
    ('40%', image('dj-3.jpg', 'Two DJs at a festival booth under purple light, one with a microphone', 'Hania at Koktebel jazz festival, 2015, when she still played with a partner', lightbox=False, className='is-style-stacked')),
    (None, J(heading('Hania Sokół', 1, fontSize='xx-large'),
             para('Hania Sokół (b. 1989, Białystok) is a DJ and producer in Warsaw. She has hosted Szum on Radio Wola every month since 2019, and runs a small label, Szum Nagrania, from a flat in Praga.'),
             para('Her sets move between Polish jazz, dub and slow electro, usually around 110 BPM. She plays records and USB, and takes a long time to get to the loud bit. She has played Tresor, Unsound, De School and a lot of basements.'),
             para('She does not play b2b with people she has not met, and she does not do wedding requests, even for friends.', fontSize='small', textColor='muted'))),
    align='wide'))

pattern('press-quotes', 'Press quotes (named)', 'testimonials', cols(
    (None, quote('Two hours on Szum and you forget it is a Thursday.', 'Agata Lis, Radio Wola programme notes, 2024')),
    (None, quote('She played a Komeda edit at 2am and the room went quiet in the right way.', 'Tomasz Kępa, Resident Advisor review of Unsound 2025')), align='wide'))

pattern('newsletter', 'Mailing list', 'call-to-action', group(J(
    heading('One email a month', 3),
    para('The next Szum guest, new dates, and a download link for the mix before it goes on Mixcloud. That is all.', fontSize='small'),
    buttons(('Sign up by email', 'mailto:hania@example.com?subject=Mailing%20list'))), className='is-style-inverse'))

pattern('guest-mix-call', 'Guest mix call-out', 'call-to-action', group(J(
    heading('Guest slots on Szum', 3),
    para('I invite one guest a month. If you make music in Poland or nearby and want to do the second hour, send me one mix you are proud of (a link, not a file) and two lines about yourself. I listen to everything, it just takes a while.', fontSize='small'),
    para('<a href="mailto:hania@example.com?subject=Szum%20guest">hania@example.com</a>', fontSize='small')), className='is-style-boxed'))

pattern('page-dates', 'Page: dates', 'text', J(pattern_ref('dates-table'), pattern_ref('dates-past')), block_types='core/post-content')
pattern('page-radio', 'Page: radio', 'text', J(pattern_ref('residency'), pattern_ref('radio-today'), pattern_ref('series-note'), pattern_ref('guest-mix-call')), block_types='core/post-content')
pattern('page-releases', 'Page: releases', 'text', J(pattern_ref('release-feature'), pattern_ref('releases-table')), block_types='core/post-content')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('bio'), pattern_ref('press-quotes'), pattern_ref('press-pack')), block_types='core/post-content')
pattern('page-booking', 'Page: booking', 'contact', J(pattern_ref('booking-territories'), cols((None, pattern_ref('tech-rider')), (None, pattern_ref('newsletter')))), block_types='core/post-content')
pattern('page-mix', 'Mix page body (player, notes, tracklist, Q&A)', 'featured', J(
    pattern_ref('mix-player'),
    para('Kaja came up from Kraków with a bag of 45s and a cold. First hour is me, mostly Polish jazz and library records. Second hour is Kaja, live on the desk, including two of her own tracks that are not out yet.'),
    pattern_ref('mix-meta'), pattern_ref('tracklist'), pattern_ref('mix-qa')), block_types='core/post-content', post_types='post')

# ------------------------------------------------------------------ templates
main_pad = {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}
def tpl(main, notice=False):
    return J(template_part('notice') if notice else '', template_part('header', 'header'), group(main, tag='main', style=main_pad), template_part('footer', 'footer'))

write('templates/front-page.html', tpl(J(
    pattern_ref('hero-latest-mix'),
    group(pattern_ref('mix-grid'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    group(cols((None, pattern_ref('dates-table')), ('40%', J(pattern_ref('radio-today')))), align='wide', className='is-style-rule-top', layout={'type': 'default'},
          style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    group(pattern_ref('release-feature'), align='wide', className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    group(cols((None, pattern_ref('newsletter')), (None, pattern_ref('guest-mix-call'))), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))))

write('templates/home.html', tpl(J(
    row(J(heading('Mixes', 1), para('Every Szum show and guest mix since 013, newest first. The first twelve were lost with the pirate stream.', fontSize='small')), justify='space-between', align='wide'),
    pattern_ref('mix-index'))))
write('templates/archive.html', tpl(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('mix-grid-archive'))))
write('templates/index.html', tpl(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list'))))
write('templates/search.html', tpl(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, buttonText='Search', placeholder='Artist, track or mix number', align='wide'), pattern_ref('post-list'))))
write('templates/404.html', tpl(J(heading('Dead air', 1), para('Nothing is broadcasting at this address. Try the archive index, or search for an artist from a tracklist.'),
    dyn('search', label='Search', showLabel=False, buttonText='Search', placeholder='Komeda'), buttons(('Go to the archive index', '/mixes/')))))
write('templates/page.html', tpl(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', tpl(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1400px'}))))
write('templates/single.html', tpl(J(
    row(J(dyn('post-date', format='j F Y'), dyn('post-terms', term='category', className='is-style-tag-boxes'))),
    dyn('post-title', level=1, fontSize='xx-large'), dyn('post-featured-image', aspectRatio='16/9', scale='cover'), dyn('post-content', layout={'type': 'constrained'}))))

single_mix = J(
    group(row(J(dyn('post-terms', term='category', className='is-style-tag-boxes'), dyn('post-date', format='l j F Y'), para('Warsaw', fontSize='x-small')),
              style={'spacing': {'blockGap': 'var:preset|spacing|30'}}), align='wide', className='is-style-index-row', layout={'type': 'default'}),
    cols(('40%', J(dyn('post-featured-image', aspectRatio='1', scale='cover', className='is-style-stacked'),
                   dyn('post-title', level=1, fontSize='xx-large'),
                   dyn('post-terms', term='post_tag', className='is-style-tag-boxes'),
                   dyn('post-excerpt', moreText='')), {'className': 'is-style-sticky-col'}),
         (None, dyn('post-content', layout={'type': 'default'})),
         align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|70'}}}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Older mix', showTitle=True), dyn('post-navigation-link', label='Newer mix', showTitle=True)), justify='space-between'),
          className='is-style-rule-top', align='wide'))
write('templates/single-mix.html', tpl(single_mix))

# ------------------------------------------------------------------ demo content
def mix_body(intro, rows, meta):
    return J(embed('https://www.mixcloud.com/radiowola/%s/' % meta[0], provider='mixcloud', type_='rich'),
             para(intro),
             table([['Broadcast', meta[1]], ['Length', meta[2]]], className='is-style-dates'),
             heading('Tracklist', 3), tracklist(rows))
posts = [
    {'title': 'Szum 058 w/ Kaja Ptak', 'category': 'szum', 'tags': ['Polish jazz', 'Broken beat', 'Library'], 'image': 'hero.jpg', 'template': 'single-mix',
     'excerpt': 'Two hours from Studio 2. Polish jazz on 45, broken beat and a Komeda edit.', 'pattern': 'bpm/page-mix'},
    {'title': 'Szum 057, three hours of dub', 'category': 'szum', 'tags': ['Dub', 'Steppers'], 'image': 'records.jpg', 'template': 'single-mix',
     'excerpt': 'No guest this month. Dub from the Praga flat, all on vinyl, one skip left in on purpose.',
     'content': mix_body('No guest this month, so I did three hours instead of two. All vinyl, all dub, recorded in the flat because the studio had a leak. There is one skip at 1:12:40. I left it in.',
                         [('00:00', 'Augustus Pablo', 'King Tubby Meets Rockers Uptown'), ('07:30', 'Rhythm & Sound', 'Mango Drive'), ('15:02', 'Vivian Jackson', 'Conquering Lion'), ('24:18', 'Dub Syndicate', 'Ravi Shankar Pt. 1'), ('33:40', 'Mala', 'Alicia')],
                         ('szum-057', 'Radio Wola 98.4 FM, 7 August, 21:00 Warsaw time', '2 hours 58 minutes'))},
    {'title': 'Live at Jasna 1, closing set', 'category': 'live', 'tags': ['Electro', 'Techno'], 'image': 'dj-4.jpg', 'template': 'single-mix',
     'excerpt': 'Four hours, 2am to 6am, recorded from the desk. The last hour is the good one.',
     'content': mix_body('Recorded from the desk at Jasna 1 on 19 July. I played from 2am until they turned the lights on. The first hour is warm-up, skip to 3:00:00 if you want the loud part.',
                         [('00:00', 'Drexciya', 'Bubble Metropolis'), ('09:10', 'DJ Stingray', 'Sentient Laser'), ('18:45', 'Heinrich Mueller', 'Continuum'), ('31:20', 'Aux 88', 'Electro Tech'), ('45:00', 'Hania Sokół', 'Nadajnik (dub)')],
                         ('live-jasna-1', 'Not broadcast. Recorded 19 July, Jasna 1, Warsaw', '3 hours 56 minutes'))},
    {'title': 'Szum 056 w/ Olek Rybak', 'category': 'szum', 'tags': ['Ambient', 'Field recordings'], 'image': 'cables.jpg', 'template': 'single-mix',
     'excerpt': 'Olek brought a modular case and a recording of the Vistula freezing.',
     'content': mix_body('Olek Rybak played live for his hour, on a small modular case, over a recording he made of the Vistula freezing in January.',
                         [('00:00', 'Hania Sokół', 'Intro over the news jingle'), ('04:12', 'Laurie Spiegel', 'Patchwork'), ('12:40', 'Eliane Radigue', 'Jetsun Mila excerpt'), ('61:00', 'Olek Rybak', 'Wisła, live')],
                         ('szum-056', 'Radio Wola 98.4 FM, 3 July, 21:00 Warsaw time', '1 hour 59 minutes'))},
    {'title': 'Szum 055, synth-pop from both Germanies', 'category': 'szum', 'tags': ['Synth-pop', 'Cold wave'], 'image': 'synth.jpg', 'template': 'single-mix',
     'excerpt': 'East and West German synth records from 1979 to 1986, played side by side.',
     'content': mix_body('A theory I have had for years: you cannot tell East and West German synth-pop apart without the sleeve. Two hours testing it. I was mostly wrong.',
                         [('00:00', 'Kraftwerk', 'Computerliebe'), ('05:30', 'Pond', 'Planetenwind'), ('12:14', 'Deutsch Amerikanische Freundschaft', 'Kebabträume'), ('18:00', 'Servi', 'Ruhezone')],
                         ('szum-055', 'Radio Wola 98.4 FM, 5 June, 21:00 Warsaw time', '2 hours'))},
    {'title': 'Szum 054 w/ Maja Lis', 'category': 'szum', 'tags': ['Italo', 'Disco'], 'image': 'headphones.jpg', 'template': 'single-mix',
     'excerpt': 'Maja from Łódź plays Italo from a single suitcase of records.',
     'content': mix_body('Maja Lis runs the Tuesday night at Ptaszarnia and owns more Italo than anyone I know. She brought one suitcase and would not tell me how she chose.',
                         [('00:00', 'Gino Soccio', 'Dancer'), ('06:40', 'Klein & MBO', 'Dirty Talk'), ('13:20', 'Casco', 'Cybernetic Love'), ('20:05', 'Charlie', 'Spacer Woman')],
                         ('szum-054', 'Radio Wola 98.4 FM, 1 May, 21:00 Warsaw time', '1 hour 57 minutes'))},
    {'title': 'Guest mix for Dźwięki Miasta', 'category': 'guest-mixes', 'tags': ['Polish jazz', 'Library'], 'image': 'mixer.jpg', 'template': 'single-mix',
     'excerpt': 'One hour for the Dźwięki Miasta podcast, all Polskie Nagrania library records.',
     'content': mix_body('One hour for the Dźwięki Miasta podcast. Every record is from the Polskie Nagrania library series, bought at the Koło flea market over about six years.',
                         [('00:00', 'Andrzej Korzyński', 'Dziewczyny, bądźcie ładne'), ('08:15', 'Czesław Niemen', 'Kwiaty ojczyste'), ('15:40', 'Novi Singers', 'Torpeda')],
                         ('dzwieki-miasta', 'Dźwięki Miasta podcast, episode 112', '59 minutes'))},
    {'title': 'Szum 053, the long one', 'category': 'szum', 'tags': ['Ambient', 'Dub'], 'image': 'crowd.jpg', 'template': 'single-mix',
     'excerpt': 'The station ran an all-night fundraiser and I took the 1am to 5am slot.',
     'content': mix_body('Radio Wola\'s spring fundraiser ran all night and I took 1am to 5am. We raised 14,200 zł for the new transmitter. This is the whole four hours.',
                         [('00:00', 'The Orb', 'Blue Room'), ('17:00', 'Basic Channel', 'Q-Loop'), ('33:30', 'Grouper', 'Heavy Water')],
                         ('szum-053', 'Radio Wola 98.4 FM, fundraiser night, 4 April, 01:00 Warsaw time', '4 hours'))},
]
content = {
    'site': {'title': 'Hania Sokół', 'tagline': 'DJ, producer and Szum on Radio Wola, Warsaw'},
    'categories': [{'slug': 'szum', 'name': 'Szum'}, {'slug': 'live', 'name': 'Live'}, {'slug': 'guest-mixes', 'name': 'Guest mixes'}],
    'front_page': 'home', 'posts_page': 'mixes',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'mixes', 'title': 'Mixes', 'content': ''},
        {'slug': 'radio', 'title': 'Radio', 'pattern': 'bpm/page-radio', 'template': 'page-wide'},
        {'slug': 'dates', 'title': 'Dates', 'pattern': 'bpm/page-dates', 'template': 'page-wide'},
        {'slug': 'releases', 'title': 'Releases', 'pattern': 'bpm/page-releases', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About', 'pattern': 'bpm/page-about', 'template': 'page-wide'},
        {'slug': 'booking', 'title': 'Booking', 'pattern': 'bpm/page-booking', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Mixes', 'url': '/mixes/'}, {'label': 'Radio', 'url': '/radio/'}, {'label': 'Dates', 'url': '/dates/'},
            {'label': 'Releases', 'url': '/releases/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Booking', 'url': '/booking/'}],
}
os.makedirs('demos/bpm', exist_ok=True)
json.dump(content, open('demos/bpm/content.json', 'w'), indent=1, ensure_ascii=False)
open('demos/bpm/fonts-claim.txt', 'w').write('display: Mona Sans\n')
print('bpm built')

# ====================================================================== ROUND 2
# Owner's review: fewer tables, lightbox on, 40+ patterns, no table on the home page, the demo uses the kit.
# Sections studied on NTS (live channels, moods, picks, genre tags), RA Podcast (numbered series, Q&A),
# The Lot Radio (today, archive index) and LYL Radio (resident pages).
theme['settings']['blocks'] = {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}}
theme['styles']['css'] += ('.is-style-rows>.wp-block-group{border-top:1px solid var(--wp--preset--color--line);padding:.55em 0;gap:.3rem 1.5rem;margin:0!important;align-items:baseline}'
                           '.is-style-rows>.wp-block-group:last-child{border-bottom:1px solid var(--wp--preset--color--line)}.is-style-rows p{margin:0}'
                           '.is-style-rows>.wp-block-group>p:first-child{flex:0 0 7.5rem;font-family:var(--wp--preset--font-family--display);font-weight:800;text-transform:uppercase;font-stretch:75%;font-size:1.25em;line-height:1}'
                           '.is-style-rows>.wp-block-group>p:nth-child(2){flex:1 1 12rem}.is-style-rows>.wp-block-group>p:nth-child(3){flex:0 1 auto}.is-style-rows a{color:var(--wp--preset--color--accent)}'
                           '.is-style-mood .wp-block-cover__inner-container h3{font-size:var(--wp--preset--font-size--x-large)}')
wjson('theme.json', theme)

def rows(data):
    return group(J(*[row(J(*[para(c) for c in r]), wrap=True) for r in data]), className='is-style-rows', layout={'type': 'default'})

# ---- tables replaced by designed rows
pattern('dates-compact', 'Dates (compact, next four)', 'events', rows([[d[0], '%s, %s' % (d[1], d[2])] for d in DATES[:4]]))
pattern('dates-table', 'Dates (date, venue, city, tickets)', 'events', J(
    heading('Dates', 2), rows([list(d) for d in DATES]),
    para('Dates marked cancelled stay on the list for a month, so people who bought tickets can find them.', fontSize='x-small', textColor='muted')))
pattern('mix-meta', 'Mix details (broadcast, location, length)', 'episode', rows([
    ['Broadcast', 'Radio Wola 98.4 FM, Thursday 4 September, 21:00 Warsaw time'], ['Recorded', 'Studio 2, ul. Wolska 40, Warsaw'],
    ['Length', '1 hour 58 minutes'], ['Guest', 'Kaja Ptak, producer, Kraków']]))
pattern('booking-territories', 'Booking contacts by territory', 'contact', J(
    heading('Booking', 2),
    rows([['Europe', 'Lena Hartmann, Fluss Agency, Berlin', '<a href="mailto:lena@example.com">lena@example.com</a>'],
          ['Poland', 'Kuba Wrona, Dźwięk Agency, Warsaw. Also the Baltics', '<a href="mailto:kuba@example.com">kuba@example.com</a>'],
          ['Elsewhere', 'Hania directly', '<a href="mailto:hania@example.com">hania@example.com</a>'],
          ['Press', 'Radio, press and podcasts: Hania directly', '<a href="mailto:hania@example.com">hania@example.com</a>']]),
    para('Please give us six weeks for club dates and three months for festivals. I play four hours or less, and I do not play before 23:00 unless it is a radio show or a record shop.', fontSize='small')))
REL = [('SZUM003', 'Wolska 40 EP', 'Szum Nagrania, 2026. 12" and digital', 'records.jpg'), ('NSD017', 'Tramwaj, with Kaja Ptak', 'Nowy Świat Dźwięku, 2025. 12" and digital', 'mixer.jpg'),
       ('SZUM002', 'Niskie Częstotliwości', 'Szum Nagrania, 2024. Cassette and digital', 'cables.jpg'), ('SZUM001', 'Pierwsza EP', 'Szum Nagrania, 2022. Digital only', 'synth.jpg')]
pattern('releases-table', 'Releases (sleeve cards)', 'release', J(
    heading('Releases', 2),
    group(J(*[group(J(image(img, 'Artwork for %s' % t, aspectRatio='1', scale='cover', className='is-style-stacked'), para(c, fontSize='x-small', textColor='muted'),
                      heading(t, 4), para(d, fontSize='small')), layout={'type': 'flex', 'orientation': 'vertical'}) for c, t, d, img in REL]),
          layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}),
    buttons(('Buy on Bandcamp', 'https://bandcamp.com/'))))
pattern('release-feature', 'Release feature', 'release', cols(
    ('45%', image('records.jpg', 'Rows of LP sleeves in a record shop crate, photographed at an angle', className='is-style-stacked')),
    (None, J(heading('Wolska 40', 2), para('New EP, out 17 October on Szum Nagrania. Four tracks made in the radio studio after hours, on the station\'s Roland MC-909 and a Juno borrowed from the breakfast show.'),
             lst(['A1 Wolska 40, 6:40', 'A2 Studio 2, 5:12', 'B1 Po wiadomościach, 7:03', 'B2 Nadajnik, 8:20']),
             buttons(('Pre-order the 12"', 'https://bandcamp.com/')))), align='wide', verticalAlignment='top'))

# ---- new patterns
pattern('live-channels', 'Live strip: station and next show', 'hero', group(cols(
    (None, row(J(para('Live', className='is-style-live-box'), para('<strong>Radio Wola</strong> Rzeka, with Ola Zawada, until 20:00'))), {'verticalAlignment': 'center'}),
    (None, row(J(para('Next', className='is-style-live-box'), para('<strong>Szum 059</strong> Thursday 2 October, 21:00, with Kaja Ptak'))), {'verticalAlignment': 'center'}),
    align='wide', verticalAlignment='center'), className='is-style-on-air', align='full', layout={'type': 'constrained'}))

TAGS = [('Polish jazz', 'polish-jazz', 'records.jpg'), ('Dub', 'dub', 'decks.jpg'), ('Ambient', 'ambient', 'cables.jpg'), ('Electro', 'electro', 'dj-4.jpg')]
pattern('moods', 'Moods: mixes by genre', 'featured', group(J(
    heading('By mood', 3),
    group(J(*[cover(img, J(heading('<a href="/tag/%s/">%s</a>' % (slug, name), 3)), dim=50, overlay='base', min_height=28, className='is-style-mood') for name, slug, img in TAGS]),
          layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'})), align='wide', layout={'type': 'default'}))

pattern('shows-by-series', 'Mixes by series', 'featured', group(J(
    heading('Series', 3),
    columns(*[(None, J(image(img, alt, aspectRatio='4/3', scale='cover', className='is-style-stacked'), heading('<a href="/category/%s/">%s</a>' % (slug, name), 4), para(d, fontSize='small')))
              for name, slug, img, alt, d in [('Szum', 'szum', 'hero.jpg', 'Hands on a DJ mixer under blue light', 'Monthly on Radio Wola since 2019, two hours, usually a guest.'),
                                              ('Live', 'live', 'dj-4.jpg', 'A DJ playing to a packed outdoor crowd', 'Club sets recorded from the desk.'),
                                              ('Guest mixes', 'guest-mixes', 'mixer.jpg', 'A black DJ mixer close up', 'For podcasts, other stations and festivals.')]], align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('upcoming-broadcasts', 'Next broadcasts', 'events', J(heading('Next on Szum', 3), rows([
    ['2 Oct', 'Szum 059 with Kaja Ptak, part two', 'Radio Wola, 21:00'], ['6 Nov', 'Szum 060, Hania solo, records from Łódź', 'Radio Wola, 21:00'],
    ['4 Dec', 'Szum 061 with Maja Lis', 'Radio Wola, 21:00'], ['31 Dec', 'New year, four hours', 'Radio Wola, 22:00']])))

pattern('hero-next-show', 'Hero: the next show', 'hero', cols(
    ('60%', J(para('Thursday 2 October, 21:00 Warsaw time', className='is-style-live-box'),
              heading('Szum 059 with Kaja Ptak', 1),
              para('Part two. Kaja brings the rest of the 45s, and plays two tracks from her EP a month before it comes out.', fontSize='large'),
              buttons(('Listen live on Thursday', 'https://example.com/radiowola-stream'), ('Hear part one', '/szum-058-w-kaja-ptak/', {'className': 'is-style-outline'})))),
    (None, image('headphones.jpg', 'A DJ in headphones at a lit-up booth with a city skyline behind', className='is-style-stacked')), align='wide', verticalAlignment='center'))

pattern('guest-profile', 'Guest profile', 'episode', group(cols(
    ('30%', image('dj-3.jpg', 'A DJ at a festival booth under purple light', aspectRatio='1', scale='cover')),
    (None, J(heading('Kaja Ptak', 4), para('Producer and DJ from Podgórze, Kraków. Runs the Wednesday at Hala Koszyki and has an EP coming on Nowy Świat Dźwięku in spring. Plays mostly 45s.', fontSize='small'),
             para('<a href="https://soundcloud.com/">SoundCloud</a>, <a href="https://www.instagram.com/">Instagram</a>', fontSize='small'))), verticalAlignment='center'), className='is-style-boxed'))

pattern('record-of-the-month', 'Ten records this month', 'text', J(heading('Ten records I keep playing', 3), lst([
    'Skalpel, Konfusion (2004)', 'Sadar Bahar, Soul Sides', 'Kaja Ptak, Tramwaj 18 (not out yet)', 'Novika, Tricks of the Light', 'Marek Biliński, Ogród Króla Świtu',
    'Rhythm & Sound, Mango Drive', 'Laurie Spiegel, Patchwork', 'Drexciya, Bubble Metropolis', 'Andrzej Korzyński, Dziewczyny, bądźcie ładne', 'Grouper, Heavy Water'], ordered=True)))

pattern('set-video', 'Filmed set', 'media', J(heading('Filmed at Jasna 1', 4),
    embed('https://www.youtube.com/watch?v=hania-sokol-jasna', provider='youtube', type_='video'),
    para('The last hour of the July closing set, filmed from the booth by Piotr Rak.', fontSize='x-small', textColor='muted')))

pattern('photo-strip', 'Photos from the booth', 'gallery', gallery([
    ('dj-4.jpg', 'A DJ playing to a packed outdoor crowd at night under blue light', 'Closing set, summer'), ('crowd.jpg', 'People dancing in a club under pink light', 'Pogłos, March'),
    ('decks.jpg', 'A turntable with a record on it', 'The Praga flat'), ('headphones.jpg', 'A DJ in headphones at a lit booth', 'Rooftop, Łódź')], columns=4, align='wide'))

pattern('setup', 'What I play on', 'about', group(J(heading('Setup at home', 4), rows([
    ['Decks', 'Two Technics SL-1210 MK2, Ortofon Concorde needles'], ['Mixer', 'Allen & Heath Xone:92, bought from a closing club in 2018'],
    ['Records', 'About 4,000, a third of them Polish'], ['Studio', 'Roland MC-909, Juno-60, a Mac Mini and patience']])), className='is-style-boxed'))

pattern('support-station', 'Support the station', 'call-to-action', group(J(
    heading('Radio Wola runs on donations', 3),
    para('Szum is free to make because Radio Wola is run by volunteers. If you like the show, give the station 20 zł a month. It pays for the transmitter and the music licences.', fontSize='small'),
    buttons(('Support Radio Wola', 'https://example.com/radiowola-support'))), className='is-style-inverse'))

pattern('series-index', 'Numbered series index', 'text', J(heading('Szum, by number', 3), rows([
    ['058', '<a href="/szum-058-w-kaja-ptak/">with Kaja Ptak</a>', 'September'], ['057', '<a href="/szum-057-three-hours-of-dub/">three hours of dub</a>', 'August'],
    ['056', '<a href="/szum-056-w-olek-rybak/">with Olek Rybak</a>', 'July'], ['055', '<a href="/szum-055-synth-pop-from-both-germanies/">synth-pop from both Germanies</a>', 'June'],
    ['054', '<a href="/szum-054-w-maja-lis/">with Maja Lis</a>', 'May'], ['053', '<a href="/szum-053-the-long-one/">the long one</a>', 'April']])))

# ---- pages that use the kit
pattern('page-radio', 'Page: radio', 'text', J(pattern_ref('live-channels'), pattern_ref('residency'), pattern_ref('radio-today'), pattern_ref('upcoming-broadcasts'), pattern_ref('series-index'), pattern_ref('series-note'), pattern_ref('guest-mix-call'), pattern_ref('support-station')), block_types='core/post-content')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('bio'), pattern_ref('photo-strip'), pattern_ref('record-of-the-month'), pattern_ref('setup'), pattern_ref('press-quotes'), pattern_ref('press-pack')), block_types='core/post-content')
pattern('page-dates', 'Page: dates', 'events', J(pattern_ref('dates-table'), pattern_ref('set-video'), pattern_ref('dates-past')), block_types='core/post-content')
pattern('page-mix', 'Mix page body (player, notes, tracklist, Q&A)', 'episode', J(
    pattern_ref('mix-player'),
    para('Kaja came up from Kraków with a bag of 45s and a cold. First hour is me, mostly Polish jazz and library records. Second hour is Kaja, live on the desk, including two of her own tracks that are not out yet.'),
    pattern_ref('mix-meta'), pattern_ref('tracklist'), pattern_ref('guest-profile'), pattern_ref('mix-qa')), block_types='core/post-content', post_types='post')
pattern('page-explore', 'Page: explore', 'featured', J(pattern_ref('hero-next-show'), pattern_ref('moods'), pattern_ref('shows-by-series')), block_types='core/post-content')

write('templates/front-page.html', tpl(J(
    pattern_ref('hero-latest-mix'),
    group(pattern_ref('mix-grid'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    group(pattern_ref('moods'), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}),
    group(cols((None, pattern_ref('dates-table')), ('40%', pattern_ref('upcoming-broadcasts'))), align='wide', className='is-style-rule-top', layout={'type': 'default'},
          style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    group(pattern_ref('release-feature'), align='wide', className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}),
    group(cols((None, pattern_ref('newsletter')), (None, pattern_ref('guest-mix-call'))), align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))))

content['pages'].append({'slug': 'explore', 'title': 'Explore', 'pattern': 'bpm/page-explore', 'template': 'page-wide'})
content['nav'] = [{'label': 'Mixes', 'url': '/mixes/'}, {'label': 'Explore', 'url': '/explore/'}, {'label': 'Radio', 'url': '/radio/'}, {'label': 'Dates', 'url': '/dates/'},
                  {'label': 'Releases', 'url': '/releases/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Booking', 'url': '/booking/'}]
for p in content['posts']:
    if p.get('content'):
        p['content'] = p['content'].replace('<!-- wp:table {"className":"is-style-dates"}', '<!-- wp:table {"className":"is-style-dates"}')
json.dump(content, open('demos/bpm/content.json', 'w'), indent=1, ensure_ascii=False)
print('bpm round 2 built')
