# patchbay: Patchbay Pedals, two people in a Leeds railway-arch unit selling guitar pedals assembled, as DIY kits and as bare PCBs.
# Direction: owner asked for "something DIY, like jhspedals.info". So: loud flat colour blocks (teal, yellow, orange, red), a
#   chunky logotype face and big product squares, crossed with the maker's bench: panel drawings with dimension lines, a
#   signal chain for navigation, spec legends and versioned build docs. The research's 1-bit dither look is dropped for the brief.
# Fonts: Chubbo (Fontshare) for display, chunky like the silkscreen on a pedal; IBM Plex Sans for everything else, small
#   and precise for specs. Two families, no monospace.
# Palette: panel white #FAFAF7, ink #141414, fuzz red #D7261E (links, prices), with teal #0E9C9A, yellow #F2B90F and
#   orange #E8622C used only as flat grounds, never for text. PCB green #1F6F4A in drawings.
# Layout idea: the home page nav is a signal chain (input jack, pedals as coloured enclosures on a wire, output jack), and
#   every product carries a boxed "docs and power" legend like a front-panel label.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('patchbay')
D = THEME['dir']
IMG = '/wp-content/themes/patchbay/assets/images/'

# ------------------------------------------------------------------ tokens
def palette(base, contrast, accent, rule, surface, line, muted, teal='#0E9C9A', yellow='#F2B90F', orange='#E8622C'):
    p = [('base', base, 'Panel white'), ('contrast', contrast, 'Ink'), ('accent', accent, 'Fuzz red'),
         ('accent-2', yellow, 'Enclosure yellow'), ('surface', surface, 'Bench'), ('line', line, 'Wire'),
         ('muted', muted, 'Graphite'), ('teal', teal, 'Enclosure teal'), ('orange', orange, 'Enclosure orange'),
         ('pcb', '#1F6F4A', 'PCB green'), ('rule', rule, 'Solder')]
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'body':
        f['fontFamily'] = '"IBM Plex Sans", "Helvetica Neue", Arial, sans-serif'

def fs(slug, size, name, mn=None):
    return {'slug': slug, 'size': size, 'name': name, 'fluid': {'min': mn, 'max': size} if mn else False}

CSS = ('body{font-synthesis:none}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
       '.wp-block-table table td,.wp-block-table table th{border:0;border-bottom:2px solid var(--wp--preset--color--line);padding:.6em .8em .6em 0;text-align:left;vertical-align:top}'
       '.wp-block-table table thead{border-bottom:0}.wp-block-table table th{font-weight:600;border-bottom:3px solid var(--wp--preset--color--contrast)}'
       '.wp-block-table table td{font-variant-numeric:tabular-nums}.wp-block-table figcaption{text-align:left}'
       '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:.3em;text-decoration-color:var(--wp--preset--color--accent)}'
       ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'
       '.wc-block-components-product-price,.wc-block-grid__product-price,.price{font-variant-numeric:tabular-nums;font-weight:600}'
       '.is-style-signal-chain{position:relative}.is-style-signal-chain::before{content:"";position:absolute;left:0;right:0;top:50%;border-top:3px solid var(--wp--preset--color--contrast)}.is-style-signal-chain>*{position:relative}'
       '@media (max-width:781px){.is-style-signal-chain{flex-direction:column;align-items:stretch!important}.is-style-signal-chain::before{left:50%;right:auto;top:0;bottom:0;border-top:0;border-left:3px solid var(--wp--preset--color--contrast)}.is-style-signal-chain .is-style-jack{align-self:center}}'
       '.is-style-pedal-link:hover{box-shadow:6px 6px 0 0 var(--wp--preset--color--contrast)}'
       '@media (prefers-reduced-motion:no-preference){.wp-element-button{transition:background-color .12s}.is-style-pedal-link:hover{transform:translate(-3px,-3px)}}')

theme = {
  '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
  'settings': {
    'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
    'layout': {'contentSize': '720px', 'wideSize': '1320px'},
    'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
              'palette': palette('#FAFAF7', '#141414', '#C8211A', '#8A6A00', '#EDEAE2', '#141414', '#55524C')},
    'typography': {'defaultFontSizes': False, 'fluid': True, 'fontFamilies': fonts, 'fontSizes': [
        fs('x-small', '0.875rem', 'Legend'), fs('small', '1rem', 'Small'), fs('medium', '1.125rem', 'Body'),
        fs('large', '1.5rem', 'Large', '1.3rem'), fs('x-large', '2.5rem', 'Section', '1.9rem'),
        fs('xx-large', '4rem', 'Title', '2.6rem'), fs('display', '7.5rem', 'Display', '3.4rem')]},
    'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
        {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
        {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2.2vw, 1.75rem)', 'name': '4'},
        {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.25rem, 5.5vw, 4rem)', 'name': '6'},
        {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 8.5rem)', 'name': '8'}]},
    'shadow': {'defaultPresets': False, 'presets': [{'slug': 'hard', 'name': 'Hard offset', 'shadow': '6px 6px 0 0 var(--wp--preset--color--contrast)'}]},
    'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
  },
  'styles': {
    'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55'},
    'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
    'elements': {
      'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
               ':hover': {'color': {'text': 'var:preset|color|contrast'}}},
      'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '0.98', 'letterSpacing': '-0.01em'}},
      'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
      'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
      'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.1'}},
      'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
      'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0'}},
      'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
      'button': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                 'border': {'radius': '6px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                 'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|medium'},
                 'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '1.2em', 'right': '1.2em'}},
                 ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'border': {'color': 'var:preset|color|contrast'}},
                 ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
      'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': 'var:preset|color|muted'}},
    },
    'blocks': {
      'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1'},
                          'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
      'core/navigation': {'typography': {'fontWeight': '600', 'fontSize': 'var:preset|font-size|medium'},
                          'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
      'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
      'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
      'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'}},
      'core/image': {'border': {'radius': '0'}},
      'core/post-featured-image': {'border': {'radius': '0', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
      'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '3px 0 0 0'}},
      'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '600', 'lineHeight': '1.3'},
                     'border': {'left': {'color': 'var:preset|color|accent', 'width': '6px', 'style': 'solid'}},
                     'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                     'css': '& cite{display:block;font-size:var(--wp--preset--font-size--small);font-weight:400;font-style:normal;margin-top:.6em}'},
      'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}},
                       'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
                       'css': '& summary{font-weight:600;cursor:pointer}'},
      'core/search': {'css': '& .wp-block-search__input{border:3px solid var(--wp--preset--color--contrast);border-radius:6px}'},
      'core/query-pagination': {'typography': {'fontWeight': '600'}},
      'core/list': {'css': '& li{margin-bottom:.3em}'},
    },
    'css': CSS,
  },
  'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                    {'area': 'uncategorized', 'name': 'notice', 'title': 'Restock notice'}],
  'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Patchbay
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A loud, flat-coloured shop theme for small guitar pedal makers who sell assembled pedals, DIY kits and PCBs, with build docs and demos.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: patchbay
Tags: e-commerce, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def variation(title, pal):
    return json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal}}}, indent='\t')
write('styles/stompbox.json', variation('Stompbox', palette('#F2C230', '#141414', '#A3160F', '#6B5000', '#FFE08A', '#141414', '#3E3413', yellow='#FAFAF7')))
write('styles/schematic.json', variation('Schematic', palette('#F7F7F2', '#1B3A6B', '#1B3A6B', '#1B3A6B', '#E6EAF2', '#1B3A6B', '#4A5875', teal='#9FC3D6', yellow='#E9E2C0', orange='#F0B8A0')))
write('styles/night-rig.json', variation('Night rig', palette('#141414', '#F4F2EC', '#FF6A55', '#F2B90F', '#26241F', '#F4F2EC', '#B8B2A6')))

# ------------------------------------------------------------------ section styles
def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t', ensure_ascii=False))

BOX = {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}
def enclosure(slug, title, bg, text='var:preset|color|contrast'):
    section(slug, title, ['core/group', 'core/column', 'core/columns'], {
        'color': {'background': bg, 'text': text},
        'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast', 'radius': '18px'},
        'elements': {'link': {'color': {'text': text}}, 'heading': {'color': {'text': text}}},
        'spacing': {'padding': BOX}})
enclosure('enclosure-teal', 'Enclosure: teal', 'var:preset|color|teal')
enclosure('enclosure-yellow', 'Enclosure: yellow', 'var:preset|color|accent-2')
enclosure('enclosure-orange', 'Enclosure: orange', 'var:preset|color|orange')
enclosure('enclosure-ink', 'Enclosure: ink', 'var:preset|color|contrast', 'var:preset|color|base')
section('flat-teal', 'Flat ground: teal', ['core/group'], {'color': {'background': 'var:preset|color|teal', 'text': 'var:preset|color|contrast'},
        'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}},
        'border': {'bottom': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}}})
section('flat-ink', 'Flat ground: ink', ['core/group'], {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
        'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                     'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}, 'border': {'color': 'var:preset|color|base'}}}})
section('legend', 'Panel legend (boxed specs)', ['core/group', 'core/table'], {
    'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
    'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast', 'radius': '6px'},
    'shadow': 'var:preset|shadow|hard',
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
    'typography': {'fontSize': 'var:preset|font-size|small'}})
section('wire', 'Wire with solder joints', ['core/group', 'core/columns', 'core/heading'], {
    'border': {'top': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|40'}},
    'css': '&{position:relative}&::before,&::after{content:"";position:absolute;top:-10px;width:17px;height:17px;border-radius:50%;background:var(--wp--preset--color--contrast)}&::before{left:0}&::after{right:0}'})
section('signal-chain', 'Signal chain (items on a wire)', ['core/group'], {'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}})
section('jack', 'Jack (IN or OUT)', ['core/paragraph'], {
    'color': {'background': 'var:preset|color|surface'},
    'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast', 'radius': '999px'},
    'typography': {'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}}})
section('pedal-link', 'Pedal in the chain', ['core/group'], {
    'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast', 'radius': '14px'},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}},
    'css': '&{min-width:9.5rem;text-align:center}'})
section('tape', 'Sticky note (yellow, ruled)', ['core/group', 'core/paragraph'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}},
    'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast', 'radius': '0'},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('framed', 'Framed image', ['core/image', 'core/post-featured-image'], {
    'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast', 'radius': '14px'},
    'css': '&{overflow:hidden}& img{display:block}'})
section('spec-row', 'Spec row (label and values)', ['core/group'], {
    'border': {'bottom': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}, 'blockGap': 'var:preset|spacing|30'},
    'css': '&>*{margin:0!important}&>:first-child{flex:1 1 9rem}&>:last-child{text-align:right}'})
section('card-list', 'Build doc list', ['core/post-template'], {
    'css': '&>li{border-top:3px solid var(--wp--preset--color--contrast);padding-top:var(--wp--preset--spacing--30)}'})

# ------------------------------------------------------------------ helpers
def srows(rows, bold_first=True):
    out = []
    for r in rows:
        cells = [para('<strong>%s</strong>' % r[0] if bold_first else r[0])] + [para(c) for c in r[1:]]
        out.append(group(J(*cells), className='is-style-spec-row', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}))
    return J(*out)

PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}
def sect(inner, **a):
    return group(inner, align='wide', layout={'type': 'default'}, style=PAD, **a)

def hid(text, anchor, level=2, **a):
    return heading(text, level, **a).replace('<h%d class="' % level, '<h%d id="%s" class="' % (level, anchor), 1)

# ------------------------------------------------------------------ parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0),
          dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'})),
        justify='space-between', align='wide'),
    tag='header', align='full',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
           'border': {'bottom': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}}}))

write('parts/footer.html', group(J(
    columns(('34%', J(para('Patchbay', fontSize='xx-large', fontFamily='display', style={'typography': {'fontWeight': '700', 'lineHeight': '1'}}),
                      para('Pedals, kits and bare boards, built and boxed in Leeds by Kemi Adeyemi and Rob Hartley.'))),
            (None, J(heading('Workshop', 6), para('Arch 14, Crown Point Road<br>Leeds LS9 8AQ<br>Collection Thursday and Friday, 12:00 to 18:00'))),
            (None, J(heading('Help', 6), para('<a href="/repairs/">Repairs and warranty</a><br><a href="/manuals/">Manuals and build docs</a><br><a href="/contact/">Contact and custom work</a>'))),
            (None, J(heading('Restock emails', 6), para('One email when a kit comes back in stock. Nothing else.'),
                     buttons(('Get restock emails', 'mailto:hello@example.com?subject=Restock%20emails')))),
            align='wide'),
    para('Photographs of parts, tools and rigs are CC0 and public-domain stand-ins from Wikimedia Commons. Pedal and PCB drawings were made for this theme.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-flat-ink',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}}}))

write('parts/notice.html', pattern_ref('restock-notice'))

# ------------------------------------------------------------------ templates
MAIN = {'style': {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}}

write('templates/front-page.html', page_template(J(
    pattern_ref('hero-bench'), pattern_ref('signal-chain'), pattern_ref('new-release'),
    pattern_ref('build-docs-list'), pattern_ref('kit-contents'), pattern_ref('help-strip')), **{'style': {'spacing': {'padding': {'top': '0', 'bottom': 'var:preset|spacing|60'}}}}))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1, fontSize='display', align='wide'),
    dyn('post-content', layout={'type': 'constrained'})), **MAIN))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1, fontSize='display', align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})), **MAIN))

write('templates/single.html', page_template(J(
    group(J(dyn('post-terms', term='category'), dyn('post-date')), layout={'type': 'flex', 'flexWrap': 'wrap'}, align='wide'),
    dyn('post-title', level=1, fontSize='xx-large', align='wide'),
    columns(('62%', dyn('post-content', layout={'type': 'default'})),
            ('38%', J(dyn('post-featured-image', className='is-style-framed'),
                      group(J(heading('Stuck on a build?', 4),
                              para('Send a clear photo of both sides of the board and a description of what happens. We answer build questions within two working days, free, even if you bought the kit second-hand.'),
                              para('<a href="mailto:builds@example.com">builds@example.com</a>')), className='is-style-tape', layout={'type': 'default'}))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True),
                dyn('post-navigation-link', label='Next', showTitle=True)), justify='space-between'),
          align='wide', className='is-style-wire', layout={'type': 'default'})), **MAIN))

CARD = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover', className='is-style-framed'),
         dyn('post-terms', term='category'),
         dyn('post-title', isLink=True, level=3, fontSize='large'),
         dyn('post-excerpt', excerptLength=20, moreText=''))
pattern('build-grid', 'Build docs grid (inherits the page query)', 'patchbay-docs,query', inherit_query(
    CARD, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '17rem'}, align='wide'), inserter=False)
pattern('post-list', 'Post list', 'patchbay-docs,query', inherit_query(
    J(dyn('post-terms', term='category'), dyn('post-title', isLink=True, level=2, fontSize='large')), template_class='is-style-card-list'), inserter=False)

write('templates/home.html', page_template(J(
    heading('Build docs and demos', 1, fontSize='display', align='wide'),
    columns(('60%', para('Every kit has a build doc here, written by Kemi at the bench while she builds the first one of each batch. Demos are recorded straight into a small amp with no other pedals on.', fontSize='large')),
            ('40%', dyn('categories')), align='wide'),
    pattern_ref('build-grid')), **MAIN))
write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='display'),
    dyn('term-description', align='wide'), pattern_ref('build-grid')), **MAIN))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), **MAIN))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Fuzz, 2N5088, Moor Echo', buttonText='Search'),
    pattern_ref('post-list')), **MAIN))
write('templates/404.html', page_template(J(
    heading('No signal on this page', 1, fontSize='xx-large'),
    para('Check the cable first, then the address. The page may have moved when we renamed the build docs. Try <a href="/build-docs/">build docs</a>, <a href="/shop/">the shop</a> or a search.'),
    dyn('search', label='Search', showLabel=False, placeholder='Fuzz, 2N5088, Moor Echo', buttonText='Search')), **MAIN))

# ------------------------------------------------------------------ home patterns
pattern('hero-bench', 'Hero: build it or we build it', 'featured', group(
    columns(('55%', J(
        heading('Pedals, kits and bare boards from a Leeds railway arch', 1, fontSize='xx-large'),
        para('Fuzz, drive, delay and tremolo. Every circuit comes assembled, as a full DIY kit you solder yourself, or as a bare board with the parts list. New this month: the Moor Echo delay.', fontSize='large'),
        buttons(('Shop pedals and kits', '/shop/'), ('Read a build doc', '/build-docs/', {'className': 'is-style-outline'})))),
            ('45%', image('draw-coal-tit.jpg', 'Drawing of the Coal Tit fuzz: an orange 1590B enclosure with Level and Fuzz knobs, an LED and a footswitch, on a teal ground with dimension lines')),
            align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    align='full', className='is-style-flat-teal', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
    description='Flat teal opener with a panel drawing of the latest pedal.')

def chain_item(name, sub, url, bg):
    return group(J(heading('<a href="%s">%s</a>' % (url, name), 3, fontSize='large'), para(sub, fontSize='x-small')),
                 className='is-style-pedal-link', backgroundColor=bg, textColor='contrast', layout={'type': 'default'})

pattern('signal-chain', 'Signal chain: shop by effect', 'featured,patchbay-shop', sect(J(
    heading('Plug in here', 2),
    group(J(para('IN', className='is-style-jack'),
            chain_item('Fuzz', 'Coal Tit, Snicket', '/product-category/fuzz/', 'orange'),
            chain_item('Drive', 'Ginnel', '/product-category/drive/', 'teal'),
            chain_item('Delay', 'Moor Echo', '/product-category/delay/', 'accent-2'),
            chain_item('Tremolo', 'Tram Stop', '/product-category/modulation/', 'surface'),
            chain_item('Boards and parts', 'PCBs, knobs, spares', '/product-category/pcbs-and-parts/', 'base'),
            para('OUT', className='is-style-jack')),
          className='is-style-signal-chain', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between', 'verticalAlignment': 'center'})
    )), description='Categories drawn as pedals on a cable, from input jack to output jack.')

LEGEND_ROWS = [['Power', '9V DC, centre negative, 2.1 mm'], ['Current draw', '18 mA'], ['Enclosure', 'Hammond 1590B, 112 × 60 × 31 mm'],
               ['Bypass', 'Buffered, trails off'], ['Build difficulty', 'Intermediate, about 4 hours'], ['Controls', 'Time, Repeats, Mix']]

pattern('spec-legend', 'Docs and power legend', 'patchbay-product', group(J(
    heading('Moor Echo, panel legend', 4),
    srows(LEGEND_ROWS)), className='is-style-legend', layout={'type': 'default'}))

pattern('kit-or-assembled', 'Assembled or DIY kit, with prices', 'patchbay-product', columns(
    (None, group(J(heading('Assembled', 3), para('Built, tested and boxed by Rob. Ships in 3 working days.'), para('<strong>£169</strong>', fontSize='x-large'),
                   buttons(('Buy it assembled', '/shop/'))), className='is-style-enclosure-yellow', layout={'type': 'default'})),
    (None, group(J(heading('DIY kit', 3), para('Board, every part, drilled and painted enclosure, knobs and a printed build doc.'), para('<strong>£79</strong>', fontSize='x-large'),
                   buttons(('Buy the kit', '/shop/'))), className='is-style-enclosure-teal', layout={'type': 'default'})),
    align='wide'))

DOCS = [['Build doc', 'v2.1', 'March 2026', '<a href="/manuals/">PDF, 3.4 MB</a>'],
        ['Schematic', 'v2.0', 'January 2026', '<a href="/manuals/">PDF, 180 KB</a>'],
        ['Bill of materials', 'v2.1', 'March 2026', '<a href="/manuals/">CSV and PDF</a>'],
        ['Drill template', 'v1.0', 'October 2025', '<a href="/manuals/">PDF, print at 100%</a>']]
pattern('docs-list', 'Versioned docs list', 'patchbay-product', J(
    heading('Documents', 4),
    srows([[d, '%s, %s' % (v, dt), f] for d, v, dt, f in DOCS])))

pattern('new-release', 'New release: drawing, legend, prices and docs', 'featured,patchbay-product', sect(
    columns(('46%', J(image('draw-moor-echo.jpg', 'Drawing of the Moor Echo delay: a yellow 1590B enclosure with Time, Repeats and Mix knobs on a red ground', className='is-style-framed'))),
            ('54%', J(
                heading('New this month: Moor Echo', 2),
                para('A PT2399 delay with 30 to 600 ms of repeats that get darker as they go. The Mix knob goes to fully wet, and yes, it will self-oscillate if you push Repeats past three o\'clock.'),
                pattern_ref('spec-legend'),
                pattern_ref('limited-colourway'),
                pattern_ref('kit-or-assembled'),
                pattern_ref('docs-list'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    description='The signature block: panel drawing, the docs and power legend, assembled or kit prices and the versioned build files.')

pattern('build-docs-list', 'Latest build docs and demos', 'patchbay-docs,query', sect(J(
    row(J(heading('From the bench', 2), para('<a href="/build-docs/">All build docs and demos</a>')), justify='space-between', className='is-style-wire'),
    query(CARD, per_page=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '17rem'}))))

pattern('kit-contents', 'What is in a kit', 'patchbay-kits', sect(
    columns(('50%', image('kit.jpg', 'A kit laid out on a white bench: a circuit board, a battery clip, bags of screws and small parts, and laser-cut panels, with a ruler along the bottom', 'A kit before the bags are opened. Ours come with the parts sorted by value.', className='is-style-framed')),
            ('50%', J(heading('What comes in a kit', 2),
                      lst(['The circuit board, silkscreened with every part value',
                           'Every resistor, capacitor, transistor and pot, bagged and labelled',
                           'An enclosure, drilled, painted and printed',
                           'Jacks, footswitch, LED, DC socket, knobs and wire',
                           'A printed build doc. The PDF is always newer, so check the version.']),
                      para('No battery clip and no battery. Batteries leak, and every pedal we sell runs on a 9V supply.', className='is-style-tape'),
                      buttons(('How our kits work', '/kits/')))),
            align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})))

pattern('help-strip', 'Repairs and dealers strip', 'patchbay-support', sect(columns(
    (None, group(J(heading('Something stopped working?', 3), para('Most problems are a flat supply or a cold joint. Work through the fault table first, then ask for a repair number.'),
                   para('<a href="/repairs/">Fault table and repairs</a>')), className='is-style-enclosure-orange', layout={'type': 'default'})),
    (None, group(J(heading('Try one in a shop', 3), para('Eleven shops in the UK and Europe keep a few Patchbay pedals on the wall, mostly Ginnels.'),
                   para('<a href="/dealers/">Find a dealer</a>')), className='is-style-enclosure-yellow', layout={'type': 'default'})),
    (None, group(J(heading('Visit the arch', 3), para('Collect orders or try pedals on Thursday and Friday afternoons. Bring your own guitar; we have a Champion 20 and a lot of cables.'),
                   para('<a href="/contact/">Address and hours</a>')), className='is-style-enclosure-teal', layout={'type': 'default'})),
    align='wide')))

# ------------------------------------------------------------------ build doc pieces
pattern('difficulty-line', 'Build difficulty line', 'patchbay-kits', para(
    '<strong>Difficulty: beginner.</strong> 22 parts, no off-board wiring except jacks and switch. About 2 hours with a 25 W iron.', className='is-style-tape'))

pattern('substitution-note', 'Parts substitution note', 'patchbay-kits', group(J(
    heading('Parts substitution', 4),
    para('The 2N5088 in Q1 went out of production in our supplier\'s range in May. Kits shipped after 1 June use a BC549C with the pins turned: collector, base, emitter reads left to right as the silkscreen says. It sounds the same; we A/B tested it for an afternoon.'),
    para('<a href="/manuals/">Substitutes sheet, v3</a>')), className='is-style-tape', layout={'type': 'default'}))

pattern('bom-table', 'Bill of materials table', 'patchbay-kits', table(
    [['R1, R4', '1k', 'Metal film, 1%', '2'], ['R2', '100k', 'Metal film, 1%', '1'], ['R3', '10k', 'Metal film, 1%', '1'],
     ['C1', '100 nF', 'Film box', '1'], ['C2', '2.2 µF', 'Electrolytic, 25 V', '1'], ['Q1, Q2', 'BC549C', 'NPN, TO-92', '2'],
     ['FUZZ', 'B100k', '16 mm pot, PCB mount', '1'], ['LEVEL', 'A100k', '16 mm pot, PCB mount', '1']],
    head=['Ref', 'Value', 'Type', 'Qty']))

pattern('build-steps', 'Build steps', 'patchbay-kits', J(
    heading('Build order', 3),
    lst(['Resistors first, lowest profile, so the board sits flat on the bench.',
         'Diodes and IC socket next. Check the band on each diode against the silkscreen.',
         'Film capacitors, then electrolytics. Long leg to the square pad.',
         'Transistors last before the pots. Keep the iron on each leg for three seconds at most.',
         'Pots and LED go on after the board is in the enclosure, so everything lines up with the holes.',
         'Before power: check for bridges under a lamp. Then 9V, then a guitar.'], ordered=True)))

pattern('controls-list', 'Controls list', 'patchbay-product', J(
    heading('Controls', 4),
    srows([['Time', '30 ms fully left, 600 ms fully right'], ['Repeats', 'One echo to endless; self-oscillates past three o\'clock'], ['Mix', 'Dry to fully wet']])))

pattern('demo-video', 'Demo video card', 'patchbay-docs', group(
    columns(('40%', image('amp.jpg', 'Black Fender Champion II 50 amplifier with its control panel along the top', className='is-style-framed')),
            ('60%', J(heading('Watch the demo', 3), para('Four minutes, a Telecaster into a Champion with no other pedals. Knobs at noon for the first minute, then Rob turns things.'),
                      buttons(('Play the demo on YouTube', 'https://www.youtube.com/'))) ), verticalAlignment='center'),
    className='is-style-enclosure-yellow', layout={'type': 'default'}),
    description='Paste your video link into the button, or swap the group for an Embed block.')

pattern('tools-you-need', 'Tools you need for a kit', 'patchbay-kits', columns(
    ('55%', J(heading('Tools you need', 3),
              lst(['A temperature-controlled iron, 25 W or more, with a fine chisel tip', '0.7 mm solder. Leaded is easier; lead-free works fine at 350 °C', 'Side cutters and small pliers',
                   'A multimeter. It will save you an hour on the first fault', 'A 9V centre-negative supply to test with']))),
    ('45%', image('solderjoint.jpg', 'A slim soldering iron and its spare tip packed in a white box, with a ruler along the top', 'An iron like this is enough for every kit we sell.', className='is-style-framed')),
    align='wide', verticalAlignment='center'))

pattern('kits-compare', 'Assembled, kit or PCB compared', 'patchbay-kits', table(
    [['What you get', 'A working pedal', 'Everything to build one', 'The board and a parts list'],
     ['Soldering', 'None', 'All of it', 'All of it, and sourcing'],
     ['Enclosure', 'Drilled, painted, printed', 'Drilled, painted, printed', 'Not included; drill template in the docs'],
     ['Warranty', '2 years', 'Parts only, 1 year', 'Board only'],
     ['Coal Tit price', '£129', '£59', '£12']],
    head=['', 'Assembled', 'DIY kit', 'PCB only']))

pattern('kits-page', 'Page: how kits work', 'patchbay-kits', J(
    para('Every Patchbay circuit is sold three ways. The electronics are identical; the difference is who holds the iron.', fontSize='large'),
    pattern_ref('kits-compare'),
    pattern_ref('difficulty-levels'),
    pattern_ref('tools-you-need'),
    pattern_ref('substitution-note'),
    pattern_ref('build-service'),
    pattern_ref('soldering-class'),
    pattern_ref('which-fuzz'),
    group(J(heading('If it does not work', 2),
            para('Write to <a href="mailto:builds@example.com">builds@example.com</a> with photos of both sides of the board. We have never charged for build help. If we cannot find it by email, post it to us and we fix it for £15 plus return postage.')),
          layout={'type': 'default'}, style=PAD)), block_types='core/post-content')

# ------------------------------------------------------------------ manuals, repairs, dealers
pattern('manuals-table', 'Manuals and build docs, versioned', 'patchbay-support', J(
    table([['Moor Echo', 'Build doc v2.1, schematic v2.0, BOM v2.1', 'March 2026', '<a href="mailto:hello@example.com?subject=Moor%20Echo%20docs">Request PDF</a>'],
           ['Ginnel', 'Build doc v3.0, schematic v3.0, BOM v3.0', 'November 2025', '<a href="mailto:hello@example.com?subject=Ginnel%20docs">Request PDF</a>'],
           ['Coal Tit', 'Build doc v1.4, schematic v1.2, BOM v1.4', 'June 2025', '<a href="mailto:hello@example.com?subject=Coal%20Tit%20docs">Request PDF</a>'],
           ['Tram Stop', 'Build doc v1.1, LDR matching sheet', 'April 2025', '<a href="mailto:hello@example.com?subject=Tram%20Stop%20docs">Request PDF</a>'],
           ['Mill Boost', 'Build doc v1.0, drill template 1590A', 'February 2024', '<a href="mailto:hello@example.com?subject=Mill%20Boost%20docs">Request PDF</a>'],
           ['Snicket', 'Build doc v2.0, bias notes', 'January 2024', '<a href="mailto:hello@example.com?subject=Snicket%20docs">Request PDF</a>']],
          head=['Pedal', 'Documents', 'Updated', 'File']),
    para('Replace the request links with your uploaded PDFs. Put the date in the file name, like moor-echo-build-v2.1-2026-03.pdf, so old printouts are easy to spot.', fontSize='small')))

pattern('retired-manuals', 'Retired pedals, docs still online', 'patchbay-support', group(J(
    heading('Retired, still supported', 3),
    srows([['Viaduct reverb', 'sold 2021 to 2023', 'build doc v1.3, February 2023'], ['Back-to-back fuzz', 'sold 2019 to 2022', 'build doc v2.0, May 2022'], ['First Ginnel, version 1', 'sold 2019 to 2021', 'build doc v1.1, January 2021']]),
    para('We keep every manual online. If you bought a retired kit second-hand, it is still covered by build help.')),
    className='is-style-tape', layout={'type': 'default'}))

pattern('manuals-page', 'Page: manuals', 'patchbay-support', J(
    para('Build docs, schematics, parts lists and drill templates for every pedal we have sold, newest version first.', fontSize='large'),
    pattern_ref('manuals-table'), pattern_ref('retired-manuals')), block_types='core/post-content')

pattern('troubleshooting-table', 'Fault table', 'patchbay-support', J(
    heading('Before you ask for a repair', 2),
    table([['No sound, LED off', 'Supply is centre positive, or under 9V', 'Use a centre-negative 9V supply and test it with a meter'],
           ['No sound, LED on', 'Cold joint on a jack or the footswitch', 'Reflow the jack lugs and all nine switch lugs'],
           ['Crackle when turning a knob', 'Dust in the pot, or DC on the pot', 'Turn it end to end twenty times; if it stays, ask us'],
           ['Signal, but weak and thin', 'A transistor in backwards', 'Check the flat side against the silkscreen'],
           ['Loud hum', 'Daisy-chained supply with a digital pedal', 'Try an isolated supply output']],
          head=['Symptom', 'Likely cause', 'Try this'])))

pattern('rma-steps', 'Repair steps', 'patchbay-support', J(
    heading('Asking for a repair', 2),
    lst(['Work through the fault table above.', 'Email hello@example.com with the pedal name, what happens and your order number if you have it.',
         'We reply with a repair number within two working days.', 'Post the pedal with the number written on the box. Tracked post, please.',
         'We fix it and post it back within ten working days.'], ordered=True)))

pattern('warranty-terms', 'Warranty terms by range', 'patchbay-support', group(J(
    heading('Warranty', 3),
    srows([['Assembled pedals', '2 years, parts and labour', 'Extended to 3 years if you register it'], ['DIY kits', '1 year on parts', 'Build help is free for life'], ['PCBs', 'Board faults only', 'Solder mistakes are yours, sorry']])),
    className='is-style-legend', layout={'type': 'default'}))

pattern('repairs-page', 'Page: repairs', 'patchbay-support', J(
    pattern_ref('troubleshooting-table'), pattern_ref('rma-steps'), pattern_ref('warranty-terms'), pattern_ref('repair-prices'), pattern_ref('pedal-faq')), block_types='core/post-content')

pattern('dealers-by-country', 'Dealers by country', 'patchbay-support', J(
    heading('United Kingdom', 3),
    srows([['Leeds', 'Northern Tone Supply, Call Lane', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['Manchester', 'Brick Wall Guitars, Oldham Street', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['Glasgow', 'Saltmarket Music', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['Bristol', 'Stokes Croft Sound', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['London', 'Denmark Street Pedal Room', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>']]),
    heading('Ireland', 3),
    srows([['Dublin', 'Capel Street Pedals', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>']]),
    heading('Netherlands and Germany', 3),
    srows([['Rotterdam', 'Witte de With Gitaren', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['Utrecht', 'Oudegracht Effects', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['Berlin', 'Kreuzberg Tretminen', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['Hamburg', 'Schanze Sound', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>'],
           ['Cologne', 'Ehrenfeld Pedalwerk', '<a href="https://example.com/search?q=patchbay">Their Patchbay stock</a>']])))

pattern('dealers-page', 'Page: dealers', 'patchbay-support', J(
    para('Shops that keep Patchbay pedals in stock. Call before you travel; they sell out of Ginnels before anything else.', fontSize='large'),
    pattern_ref('dealers-by-country'),
    para('Want to stock us? Trade prices start at five pedals. Write to <a href="mailto:trade@example.com">trade@example.com</a>.', className='is-style-tape')), block_types='core/post-content')

# ------------------------------------------------------------------ about, contact, custom
pattern('about-bench', 'About the two of us', 'patchbay-about', sect(columns(
    ('58%', J(para('Kemi Adeyemi designs the circuits and writes the build docs. She started building fuzzes from forum schematics in 2014 and still does most of the first builds of every batch herself.', fontSize='large'),
              para('Rob Hartley drills, paints and prints the enclosures, packs every kit and answers most of the email. He plays in a band that you have not heard of, and the demos are recorded on his Telecaster.'),
              para('We work out of a railway arch on Crown Point Road. Trains go over every six minutes. Hence the gaps in the demos.'),
              para('We do not make boutique clones with a new name on them. Every circuit here has at least one part of the design that is ours, and the build doc tells you which.'))),
    ('42%', image('guitarist.jpg', 'Two guitarists playing on a small stage, one kneeling over a pedal on the floor', 'A Friday night with one of our Moor Echos on the floor, Leeds, 2025.', className='is-style-framed')),
    align='wide')))

pattern('bench-quote', 'Quote from a builder', 'patchbay-about', quote(
    'Built the Ginnel kit with my daughter over two evenings. One transistor in backwards, fixed after one email. It is on my board now and she wants the Moor Echo.',
    'Declan Moss, Sheffield, built in January 2026'))

pattern('about-page', 'Page: about', 'patchbay-about', J(pattern_ref('about-bench'), pattern_ref('bench-quote'), pattern_ref('on-their-boards'), pattern_ref('enclosure-colours'), pattern_ref('settings-recipes'), pattern_ref('help-strip')), block_types='core/post-content')

pattern('custom-artwork', 'Custom artwork request panel', 'patchbay-support', group(J(
    heading('Custom graphics and colours', 3),
    para('For bands, shops and gifts. Any of our pedals in your colours and artwork, from ten units, or one for a present if the artwork is yours.'),
    para('<strong>Lead time: 8 to 12 weeks. Payment upfront.</strong>'),
    buttons(('Email us your artwork', 'mailto:hello@example.com?subject=Custom%20artwork'))),
    className='is-style-enclosure-orange', layout={'type': 'default'}),
    description='Change the lead time line when the queue changes.')

pattern('contact-details', 'Contact details and hours', 'patchbay-support', columns(
    (None, J(heading('Arch 14', 3), para('Crown Point Road, Leeds LS9 8AQ. Under the railway, between the tyre place and the climbing wall. Ring the bell; the music is loud.'),
             srows([['Monday to Wednesday', 'Closed to visitors, we are building'], ['Thursday and Friday', '12:00 to 18:00'], ['Weekends', 'Closed']]))),
    (None, J(heading('Email', 3), para('Orders and questions: <a href="mailto:hello@example.com">hello@example.com</a><br>Build help: <a href="mailto:builds@example.com">builds@example.com</a><br>Trade: <a href="mailto:trade@example.com">trade@example.com</a>'),
             para('We answer within two working days. No phone, sorry; we would never get any soldering done.'))),
    align='wide'))

pattern('contact-page', 'Page: contact', 'patchbay-support', J(pattern_ref('contact-details'), pattern_ref('custom-artwork'), pattern_ref('gift-voucher')), block_types='core/post-content')

pattern('restock-notice', 'Restock notice bar', 'banner', group(
    para('Moor Echo kits are back on 10 October. Assembled Ginnels ship in 3 working days. <a href="/shop/">Shop</a>', style={'typography': {'textAlign': 'center'}}),
    align='full', className='is-style-tape', layout={'type': 'constrained'}))

pattern('shipping-note', 'Postage and returns', 'patchbay-shop', table(
    [['UK', '£4.50 tracked, free over £100', '1 to 2 working days'], ['EU', '£12 tracked, duties paid', '4 to 7 working days'], ['US and Canada', '£18 tracked', '6 to 10 working days']],
    head=['Where', 'Postage', 'Usually takes'], caption='Returns within 30 days on unbuilt kits and unused pedals. Kits you have soldered cannot be returned, but build help is free.'))


# ------------------------------------------------------------------ round 2: more of the kit (JHS, Old Blood Noise, Befaco, Aion FX, ZVEX)
pattern('difficulty-levels', 'Kit difficulty levels', 'patchbay-kits', sect(J(
    heading('Difficulty levels', 2),
    columns((None, group(J(heading('Beginner', 3), para('Under 30 parts, no off-board wiring apart from jacks and switch.'), para('<strong>Coal Tit, Mill Boost</strong>')), className='is-style-enclosure-teal', layout={'type': 'default'})),
            (None, group(J(heading('Intermediate', 3), para('30 to 60 parts, one IC, a few off-board wires.'), para('<strong>Ginnel, Moor Echo</strong>')), className='is-style-enclosure-yellow', layout={'type': 'default'})),
            (None, group(J(heading('Involved', 3), para('Optical parts or a trimmer to set. A scope helps; a meter is a must.'), para('<strong>Tram Stop, Snicket</strong>')), className='is-style-enclosure-orange', layout={'type': 'default'})),
            align='wide'))))

pattern('build-service', 'We build your kit', 'patchbay-kits', group(J(
    heading('Bought a kit and ran out of evenings?', 3),
    para('Post it to us, bagged parts and all, and Rob builds it for £40 plus return postage. Half-built kits too; we charge £25 to finish one.'),
    buttons(('Email about a build', 'mailto:builds@example.com?subject=Build%20service'))),
    className='is-style-tape', layout={'type': 'default'}))

pattern('soldering-class', 'Soldering evening at the arch', 'patchbay-kits', sect(columns(
    ('55%', J(heading('Build a Coal Tit with us', 2),
              para('One evening a month, 18:30 to 21:30, six people at the bench. You leave with a working fuzz. £75 including the kit, irons and tea.'),
              para('Next date: Thursday 22 October. Two places left.'),
              buttons(('Email to book a place', 'mailto:hello@example.com?subject=Soldering%20evening')))),
    ('45%', image('breadboard.jpg', 'Two white breadboards side by side with rows of contact holes', 'We start on a breadboard, then move to the real board.', className='is-style-framed')),
    align='wide', verticalAlignment='center')))

pattern('enclosure-colours', 'Enclosure colours in stock', 'patchbay-product', sect(J(
    heading('Enclosure colours', 2),
    para('Rob mixes the paint in batches of forty. When a colour runs out it may not come back.'),
    grid(J(*[group(J(heading(n, 4), para(note, fontSize='x-small')), backgroundColor=c, textColor='contrast', className='is-style-pedal-link', layout={'type': 'default'})
             for n, c, note in [('Coal orange', 'orange', 'Coal Tit, standard'), ('Canal teal', 'teal', 'Ginnel, standard'), ('Mustard', 'accent-2', 'Moor Echo, standard'),
                                ('Bench grey', 'surface', 'Any pedal, on request'), ('Panel white', 'base', 'Tram Stop, limited')]]), min_width='10rem'))))

pattern('settings-recipes', 'Knob settings people ask for', 'patchbay-product', sect(J(
    heading('Settings to start from', 2),
    columns((None, group(J(heading('Ginnel, always on', 4), para('Gain 9 o\'clock, Tone noon, Level a little past unity. Makes a clean amp sound like it is working harder.')), className='is-style-legend', layout={'type': 'default'})),
            (None, group(J(heading('Moor Echo, slapback', 4), para('Time fully left, Repeats one echo, Mix 10 o\'clock. Rockabilly, or a vocal mic at a gig.')), className='is-style-legend', layout={'type': 'default'})),
            (None, group(J(heading('Coal Tit, into a dirty amp', 4), para('Fuzz 1 o\'clock, Level to taste, guitar volume on 7. Roll the guitar up for the chorus.')), className='is-style-legend', layout={'type': 'default'})),
            align='wide'))))

pattern('limited-colourway', 'Limited colourway note', 'patchbay-product', para(
    '<strong>Limited run:</strong> 30 Moor Echos in panel white with red knobs, numbered inside the lid. Same circuit, same price.', className='is-style-tape'))

pattern('on-their-boards', 'On customers\' boards', 'patchbay-about', sect(columns(
    ('50%', image('rig.jpg', 'A small amp, an electric guitar on a stand and a pedalboard of eight pedals on a wooden floor, seen from above', 'Ana\'s board in Hull, with a Ginnel she built from a kit.', className='is-style-framed')),
    ('50%', J(heading('On your boards', 2),
              para('Send us a photo of your board with a Patchbay pedal on it and we will put it here. Tell us what you play and where.'),
              buttons(('Email a photo of your board', 'mailto:hello@example.com?subject=My%20board')),
              para('<a href="/category/demos/">Customer boards and demos</a>'))),
    align='wide', verticalAlignment='center')))

pattern('repair-prices', 'Repair prices out of warranty', 'patchbay-support', sect(J(
    heading('Out of warranty', 3),
    srows([['Jack, footswitch or DC socket', '£15 plus parts'], ['Pot replacement', '£12 per pot'], ['Finish a half-built kit', '£25'], ['Full diagnosis if nothing else works', '£20, taken off the repair']]))))

pattern('pedal-faq', 'Questions about pedals and kits', 'patchbay-support', sect(J(
    heading('Questions people email us', 2),
    details('Do the pedals take batteries?', para('No. There is no battery clip in any of them. Use a 9V centre-negative supply.')),
    details('True bypass or buffered?', para('Coal Tit, Ginnel and Tram Stop are true bypass. The Moor Echo is buffered so the repeats can trail off.')),
    details('Can I buy just the enclosure?', para('Yes, drilled and painted, £18. Email us with the pedal name.')),
    details('Do you ship outside Europe?', para('Yes, tracked. Postage is shown in the basket before you pay.')),
    details('Can a beginner build the Tram Stop?', para('Build the Coal Tit first. The Tram Stop needs LDR matching and a meter.')))))

pattern('gift-voucher', 'Gift voucher', 'patchbay-shop', group(J(
    heading('Gift vouchers', 3),
    para('£25, £50 or £100, emailed as a code the same day. Good for kits, pedals, the build service and soldering evenings.'),
    buttons(('Email to buy a voucher', 'mailto:hello@example.com?subject=Gift%20voucher'))),
    className='is-style-enclosure-yellow', layout={'type': 'default'}))

pattern('which-fuzz', 'Which fuzz: Coal Tit or Snicket', 'patchbay-product', sect(columns(
    (None, J(image('draw-coal-tit.jpg', 'Drawing of the Coal Tit fuzz in an orange enclosure', className='is-style-framed'), heading('Coal Tit', 3),
             para('Two knobs, silicon, cleans up with the guitar volume. Beginner kit. From £59.'), para('<a href="/product-category/fuzz/">Fuzz pedals and kits</a>'))),
    (None, J(image('draw-snicket.jpg', 'Drawing of the Snicket octave fuzz circuit board on an orange ground', className='is-style-framed'), heading('Snicket', 3),
             para('Octave-up fuzz, loud above the 12th fret. Board only, for people who have built a few. £14.'), para('<a href="/product-category/pcbs-and-parts/">Boards and parts</a>'))),
    align='wide')))

print('patchbay: patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

write('functions.php', '''<?php
/**
 * Patchbay: pattern categories only.
 *
 * @package patchbay
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'patchbay-shop'    => 'Patchbay: shop',
			'patchbay-product' => 'Patchbay: product details',
			'patchbay-kits'    => 'Patchbay: kits and building',
			'patchbay-docs'    => 'Patchbay: build docs',
			'patchbay-support' => 'Patchbay: support',
			'patchbay-about'   => 'Patchbay: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);''')

# ------------------------------------------------------------------ demo content
def build_doc(intro, difficulty, bom, steps, sub=None, demo=True):
    parts = [para(intro), para(difficulty, className='is-style-tape')]
    parts.append(heading('Parts', 3))
    parts.append(table(bom, head=['Ref', 'Value', 'Qty']))
    parts.append(heading('Build order', 3))
    parts.append(lst(steps, ordered=True))
    if sub:
        parts.append(group(J(heading('Parts substitution', 4), para(sub)), className='is-style-tape', layout={'type': 'default'}))
    return J(*parts)

def demo_post(intro, img, alt, notes):
    return J(para(intro),
             group(J(heading('Watch the demo', 3), para(notes), buttons(('Play the demo on YouTube', 'https://www.youtube.com/')), para('Recorded dry: guitar, pedal, amp and one microphone.', fontSize='x-small')),
                   className='is-style-enclosure-yellow', layout={'type': 'default'}))

POSTS = [
  ('Moor Echo build doc, version 2.1', 'build-docs', 'schematic.jpg', '2026-03-12',
   build_doc('The second batch of Moor Echo boards has a trimmer for the delay chip\'s clock, so you can set the maximum time yourself. Version 2.1 of the doc covers it.',
             'Difficulty: intermediate. 48 parts, one IC, six off-board wires. About 4 hours.',
             [['R1 to R12', 'various, see sheet', '12'], ['C1 to C14', 'film and electrolytic', '14'], ['IC1', 'PT2399', '1'], ['IC2', 'TL072', '1'], ['TRIM1', '50k', '1'], ['Pots', 'B50k, B10k, B100k', '3']],
             ['Socket the ICs. Do not solder the PT2399 directly.', 'Resistors, then film caps, then electrolytics.', 'Set TRIM1 to the middle before first power.',
              'With Time fully right, turn TRIM1 until the repeats start to fizz, then back a quarter turn.'])),
  ('Coal Tit fuzz, a beginner build in two hours', 'build-docs', 'breadboard.jpg', '2026-02-20',
   build_doc('The Coal Tit is our first kit for a reason: two transistors, 22 parts, and it sounds good even if you get the bias slightly wrong.',
             'Difficulty: beginner. 22 parts. About 2 hours with a 25 W iron.',
             [['R1, R4', '1k', '2'], ['R2', '100k', '1'], ['R3', '10k', '1'], ['C1', '100 nF', '1'], ['C2', '2.2 µF', '1'], ['Q1, Q2', 'BC549C', '2']],
             ['Resistors first.', 'Capacitors, long leg of C2 to the square pad.', 'Transistors, flat side to the line on the silkscreen.', 'Pots, jacks and switch after the board is in the box.'],
             sub='Kits shipped after 1 June use a BC549C in place of the 2N5088. Mind the pin order: it is printed on the board.')),
  ('Demo: Moor Echo into a Champion, no other pedals', 'demos', 'amp.jpg', '2026-03-20',
   demo_post('Rob recorded this one in the arch after six, when the trains slow down. Telecaster bridge pickup, amp at 3, delay straight in.',
             'amp.jpg', 'Black Fender Champion II 50 amplifier with its control panel along the top', 'Four minutes. Short slapback first, then long repeats, then the self-oscillation at the end that you will want to turn off.')),
  ('Ginnel overdrive build doc, version 3', 'build-docs', 'components.jpg', '2025-11-14',
   build_doc('Version 3 moves the tone control after the clipping diodes, which makes the Tone knob useful across its whole turn.',
             'Difficulty: intermediate. 38 parts, one dual op-amp. About 3 hours.',
             [['R1 to R9', 'various', '9'], ['C1 to C8', 'film and electrolytic', '8'], ['D1, D2', '1N914', '2'], ['IC1', 'JRC4558D', '1'], ['Pots', 'A500k, B25k, A10k', '3']],
             ['Resistors and diodes. Band on the diode to the line.', 'IC socket, notch towards the jacks.', 'Capacitors.', 'Pots on after the board is mounted.'])),
  ('Your boards: a kitchen-floor rig from Hull', 'demos', 'rig.jpg', '2025-10-02',
   demo_post('Ana sent us this photo of her practice set-up with a Ginnel in the middle of the second row. She built it from a kit in April.',
             'rig.jpg', 'A small amp, an electric guitar on a stand and a pedalboard of eight pedals on a wooden floor, seen from above',
             'She runs the Ginnel with Gain at nine o\'clock as an always-on pedal. We asked her to record a short clip; this is it.')),
  ('Why we swapped the 2N5088', 'news', 'knobs.jpg', '2025-06-01',
   J(para('Our supplier stopped carrying the 2N5088 in May. We tested five replacements over an afternoon with the Coal Tit and the Snicket.'),
     para('The BC549C won. It has a different pin order, so we changed the silkscreen on the new boards and added a note to every build doc.'),
     table([['BC549C', 'Chosen', 'Close gain, low noise'], ['2N3904', 'Too thin', 'Lower gain, harsher top'], ['MPSA18', 'Too hot', 'Noisy at full Fuzz']], head=['Part', 'Result', 'Why']))),
  ('Tram Stop: matching the LDR', 'build-docs', 'schematic2.jpg', '2025-04-18',
   build_doc('The Tram Stop uses an LED and a light-dependent resistor to do the tremolo. The LDRs vary a lot, so the kit comes with three and a sheet to pick the right one.',
             'Difficulty: involved. 54 parts and a matching step. A multimeter is not optional for this one.',
             [['LDR1 to LDR3', 'GL5528', '3'], ['LED2', 'Warm white, 5 mm', '1'], ['IC1', 'TL072', '1'], ['Pots', 'B1M, B50k, A10k', '3']],
             ['Build the board, leave LDR1 unsoldered.', 'Measure each LDR in the dark and in room light, write both values down.', 'Fit the one closest to 1M dark and 5k light.', 'Wrap LED and LDR together with the heat-shrink in the bag.'])),
  ('New enclosure colours for autumn', 'news', 'pedalboard.jpg', '2025-09-10',
   J(para('Rob has mixed three new colours for the autumn batch: slate, mustard and the orange the Coal Tit wears.'),
     para('Kits and assembled pedals come in the new colours from the October batch. Old colours stay until we run out of the paint.'))),
]

content = {
  'site': {'title': 'Patchbay', 'tagline': 'Guitar pedals, DIY kits and bare boards from Leeds'},
  'categories': [{'slug': 'build-docs', 'name': 'Build docs', 'description': 'Step-by-step build docs for every kit.'},
                 {'slug': 'demos', 'name': 'Demos', 'description': 'Recorded straight into a small amp.'},
                 {'slug': 'news', 'name': 'News', 'description': 'Restocks, part changes and new colours.'}],
  'front_page': 'home', 'posts_page': 'build-docs',
  'pages': [
    {'slug': 'home', 'title': 'Home', 'content': ''},
    {'slug': 'build-docs', 'title': 'Build docs', 'content': ''},
    {'slug': 'kits', 'title': 'Kits', 'pattern': 'patchbay/kits-page', 'template': 'page-wide'},
    {'slug': 'manuals', 'title': 'Manuals', 'pattern': 'patchbay/manuals-page', 'template': 'page-wide'},
    {'slug': 'repairs', 'title': 'Repairs', 'pattern': 'patchbay/repairs-page'},
    {'slug': 'dealers', 'title': 'Dealers', 'pattern': 'patchbay/dealers-page'},
    {'slug': 'about', 'title': 'About', 'pattern': 'patchbay/about-page', 'template': 'page-wide'},
    {'slug': 'contact', 'title': 'Contact', 'pattern': 'patchbay/contact-page', 'template': 'page-wide'},
  ],
  'posts': [{'title': t, 'category': c, 'image': img, 'date': d, 'content': body} for t, c, img, d, body in POSTS],
  'nav': [{'label': 'Shop', 'url': '/shop/'}, {'label': 'Kits', 'url': '/kits/'}, {'label': 'Build docs', 'url': '/build-docs/'},
          {'label': 'Manuals', 'url': '/manuals/'}, {'label': 'Repairs', 'url': '/repairs/'}, {'label': 'Dealers', 'url': '/dealers/'},
          {'label': 'About', 'url': '/about/'}],
  'currency': 'GBP',
  'products': [
    {'name': 'Coal Tit fuzz, assembled', 'price': '129', 'image': 'draw-coal-tit.jpg', 'category': 'Fuzz', 'sku': 'PB-CT-A', 'stock': 7,
     'short': 'Two-knob silicon fuzz. Built and tested in Leeds. 9V centre negative, 6 mA.',
     'description': 'Level and Fuzz, nothing else. It cleans up when you roll back your guitar volume. Hammond 1590B, true bypass, 2 years warranty.'},
    {'name': 'Coal Tit fuzz, DIY kit', 'price': '59', 'image': 'kit.jpg', 'category': 'Fuzz', 'sku': 'PB-CT-K', 'stock': 23,
     'short': 'Beginner kit, 22 parts, about 2 hours. Drilled and painted enclosure included.',
     'description': 'Everything to build a Coal Tit: board, parts bagged by value, drilled and painted 1590B, jacks, switch, knobs and a printed build doc (v1.4).'},
    {'name': 'Ginnel overdrive, assembled', 'price': '149', 'image': 'draw-ginnel.jpg', 'category': 'Drive', 'sku': 'PB-GN-A', 'stock': 4,
     'short': 'Op-amp overdrive with a Tone knob that works all the way round. 9V, 8 mA.',
     'description': 'Gain, Level and Tone. Symmetrical silicon clipping. Hammond 1590B, true bypass, 2 years warranty.'},
    {'name': 'Ginnel overdrive, DIY kit', 'price': '69', 'image': 'components.jpg', 'category': 'Drive', 'sku': 'PB-GN-K', 'stock': 11,
     'short': 'Intermediate kit, 38 parts, about 3 hours.',
     'description': 'Board, parts, drilled and painted enclosure, JRC4558D op-amp and socket, and the version 3 build doc.'},
    {'name': 'Moor Echo delay, assembled', 'price': '169', 'image': 'draw-moor-echo.jpg', 'category': 'Delay', 'sku': 'PB-ME-A', 'stock': 0,
     'short': 'PT2399 delay, 30 to 600 ms. Sold out; the next batch ships 10 October.',
     'description': 'Time, Repeats and Mix. Buffered bypass so the trails carry on. 9V centre negative, 18 mA.'},
    {'name': 'Tram Stop tremolo, DIY kit', 'price': '75', 'image': 'draw-tram-stop.jpg', 'category': 'Modulation', 'sku': 'PB-TS-K', 'stock': 6,
     'short': 'Optical tremolo kit with three LDRs to match. Involved build.',
     'description': 'Rate, Depth and Level. The kit includes an LDR matching sheet. You will need a multimeter.'},
    {'name': 'Mill Boost PCB', 'price': '12', 'image': 'draw-mill-boost.jpg', 'category': 'PCBs and parts', 'sku': 'PB-MB-P', 'stock': 40,
     'short': 'Bare board for a one-knob clean boost. Fits a 1590A. Parts list in the docs.',
     'description': 'Board only. The build doc and drill template are free on the manuals page.'},
    {'name': 'Snicket octave fuzz PCB', 'price': '14', 'image': 'draw-snicket.jpg', 'category': 'PCBs and parts', 'sku': 'PB-SN-P', 'stock': 18,
     'short': 'Bare board for an octave-up fuzz. Fits a 1590B.',
     'description': 'Board only. Needs two matched germanium diodes, which we do not supply.'},
    {'name': 'Knob and pot set, three of each', 'price': '9', 'image': 'knobs.jpg', 'category': 'PCBs and parts', 'sku': 'PB-KP-3', 'stock': 30,
     'short': 'Three 16 mm pots (A100k, B100k, B50k) and three numbered knobs.',
     'description': 'Spares for when you strip a shaft or want different values. PCB-mount pots.'},
  ],
}
os.makedirs('demos/patchbay', exist_ok=True)
json.dump(content, open('demos/patchbay/content.json', 'w'), indent=1, ensure_ascii=False)
print('patchbay: demo content written')
