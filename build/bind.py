# bind: Wójcik Bindery, a two-person conservation bindery in Kazimierz, Kraków ("introligatornia").
# Direction: private-press book typography. The site reads like a book: a bottle-green buckram "front board" with a
#   gold-tooled double frame opens the home page, then paper pages with running heads, a contents page with dot leaders,
#   side-notes in the outer margin and a colophon for a footer. Why: a bindery's own material is the page and the cover.
# Fonts: Goudy Bookletter 1911 (display, metal-type private-press face), EB Garamond with true italics (body, and
#   in italic for running heads, captions and side-notes, the way a printed book does it). Two families, no mono.
# Palette: laid paper #F4F1EA, ink #1E1B18, buckram green #1F4D3A (links, boards), gold foil #D6B56E only on green,
#   gold rule #8C6D2A for hairlines on paper, board surface #E8E1D1. Plus eight cloth swatches as palette colours.
# Layout idea: before/after pairs at identical 4:5 crops with a side-note column, and every price list set as a contents
#   page with dot leaders, instead of cards.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('bind')
S = 'bind'
D = THEME['dir']
IMG = '/wp-content/themes/bind/assets/images/'

# ------------------------------------------------------------------ tokens
SWATCHES = [
    ('sw-bottle', '#1F4D3A', 'Cloth: bottle green'), ('sw-oxblood', '#6B1E22', 'Cloth: oxblood'),
    ('sw-navy', '#1C2A48', 'Cloth: navy'), ('sw-ochre', '#B7862E', 'Cloth: ochre'),
    ('sw-dove', '#96948C', 'Cloth: dove grey'), ('sw-black', '#1A1A1A', 'Cloth: black'),
    ('sw-linen', '#D9CEB4', 'Cloth: natural linen'), ('sw-tan', '#8A5A34', 'Leather: tan goatskin'),
]

def palette(base, contrast, accent, rule, surface, line, muted, board, foil):
    p = [('base', base, 'Paper'), ('contrast', contrast, 'Ink'), ('accent', accent, 'Buckram'),
         ('accent-2', rule, 'Gold rule'), ('surface', surface, 'Board'), ('line', line, 'Line'),
         ('muted', muted, 'Pencil'), ('board', board, 'Front board'), ('foil', foil, 'Gold foil')]
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p] + [{'slug': s, 'color': c, 'name': n} for s, c, n in SWATCHES]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Goudy Bookletter 1911", "EB Garamond", serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"EB Garamond", Georgia, serif'

def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d

theme = {
  '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
  'settings': {
    'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
    'layout': {'contentSize': '640px', 'wideSize': '1180px'},
    'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
              'palette': palette('#F4F1EA', '#1E1B18', '#1F4D3A', '#8C6D2A', '#E8E1D1', '#CFC4AF', '#5A5247', '#1F4D3A', '#D6B56E')},
    'typography': {'defaultFontSizes': False, 'fluid': True, 'fontFamilies': fonts, 'fontSizes': [
        fs('x-small', '0.875rem', 'Running head'), fs('small', '1rem', 'Note'), fs('medium', '1.1875rem', 'Text'),
        fs('large', '1.5rem', 'Large', '1.3rem'), fs('x-large', '2.125rem', 'Section', '1.7rem'),
        fs('xx-large', '3.25rem', 'Title', '2.4rem'), fs('display', '5.25rem', 'Display', '3rem')]},
    'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh', 'ch'], 'spacingSizes': [
        {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
        {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2.2vw, 1.75rem)', 'name': '4'},
        {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.25rem, 5.5vw, 4rem)', 'name': '6'},
        {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 8.5rem)', 'name': '8'}]},
    'shadow': {'defaultPresets': False, 'presets': []},
    'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    'custom': {'measure': '62ch'},
    'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
  },
  'styles': {
    'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6'},
    'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
    'elements': {
      'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
               ':hover': {'color': {'text': 'var:preset|color|contrast'}},
               ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
      'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '1.08'}},
      'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
      'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
      'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}},
      'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontStyle': 'italic', 'lineHeight': '1.3'}},
      'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600'}},
      'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontStyle': 'italic', 'lineHeight': '1.4'}},
      'button': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                 'border': {'radius': '2px', 'width': '1px', 'style': 'solid', 'color': 'var:preset|color|accent'},
                 'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                 'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.4em', 'right': '1.4em'}},
                 ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}, 'border': {'color': 'var:preset|color|contrast'}},
                 ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
      'caption': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'},
                  'color': {'text': 'var:preset|color|muted'}},
    },
    'blocks': {
      'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large'},
                          'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
      'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'},
                          'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
      'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
      'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
      'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|x-small'}},
      'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small'}},
      'core/image': {'border': {'radius': '0'}},
      'core/post-featured-image': {'border': {'radius': '0'}},
      'core/separator': {'color': {'text': 'var:preset|color|accent-2'}, 'border': {'width': '1px 0 0 0'}},
      'core/quote': {'typography': {'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.4'},
                     'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '1px', 'style': 'solid'}},
                     'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                     'css': '& cite{display:block;font-style:normal;font-size:var(--wp--preset--font-size--small);color:var(--wp--preset--color--muted);margin-top:.75em}'},
      'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large'},
                         'border': {'top': {'color': 'var:preset|color|accent-2', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|accent-2', 'width': '1px', 'style': 'solid'}}},
      'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
      'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                       'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
                       'css': '& summary{font-style:italic;cursor:pointer}'},
      'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'},
                      'css': '& .wp-block-search__input{border:0;border-bottom:1px solid var(--wp--preset--color--contrast);background:transparent;font-family:inherit}'},
      'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}},
      'core/code': {'typography': {'fontFamily': 'var:preset|font-family|body'}},
      'core/list': {'css': '& li{margin-bottom:.35em}'},
    },
    'css': '.wp-block-table table td,.wp-block-table table th{border:0;padding:.55em .75em .55em 0;vertical-align:top;text-align:left}.wp-block-table table thead{border-bottom:1px solid var(--wp--preset--color--contrast)}.wp-block-table table th{font-style:italic;font-weight:400}.wp-block-table table td{border-bottom:1px solid var(--wp--preset--color--line);font-variant-numeric:lining-nums tabular-nums}.wp-block-table table td:last-child{text-align:right}.wp-block-table figcaption{text-align:left}'
           ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty;hanging-punctuation:first}body{font-synthesis:none;font-variant-numeric:oldstyle-nums}'
           ':where(.wp-block-post-content,.entry-content)>p{max-width:62ch}'
           '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-decoration-color:var(--wp--preset--color--accent-2);text-underline-offset:.35em}'
           ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
           '@media (prefers-reduced-motion:no-preference){a{transition:color .15s}}',
  },
  'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header (running head)'},
                    {'area': 'footer', 'name': 'footer', 'title': 'Footer (colophon)'},
                    {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice line'}],
  'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide (tables and swatches)', 'postTypes': ['page']}],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Bind
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A book-page theme for small binderies that repair old books, bind theses and new editions, and run a few workshops a year.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: bind
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column
*/''')

# ------------------------------------------------------------------ variations
def variation(title, pal, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal}}}
    if extra:
        d['styles'] = extra
    return d
write('styles/goatskin.json', json.dumps(variation('Goatskin', palette('#2E1913', '#EADFC8', '#D6B56E', '#B8974F', '#3B221A', '#5C4034', '#C7B89C', '#1F4D3A', '#E0C27E')), indent='\t'))
write('styles/vellum.json', json.dumps(variation('Vellum', palette('#FBF8F1', '#3A3122', '#6B5A3A', '#9C8454', '#F1EBDD', '#DDD2BC', '#6A5E4A', '#6B5A3A', '#F1E2B8')), indent='\t'))
write('styles/oxblood.json', json.dumps(variation('Oxblood', palette('#F3F0EC', '#1C1818', '#6B1E22', '#8E6B2C', '#E6DED8', '#CDBFB6', '#5A504C', '#6B1E22', '#E2C07A'),
      {'typography': {'lineHeight': '1.65'}}), indent='\t'))

# ------------------------------------------------------------------ section styles
def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t', ensure_ascii=False))

section('board', 'Front board (buckram with gold frame)', ['core/group', 'core/cover'], {
    'color': {'background': 'var:preset|color|board', 'text': 'var:preset|color|foil'},
    'elements': {'link': {'color': {'text': 'var:preset|color|foil'}}, 'heading': {'color': {'text': 'var:preset|color|foil'}},
                 'button': {'color': {'background': 'var:preset|color|foil', 'text': 'var:preset|color|board'}, 'border': {'color': 'var:preset|color|foil'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|80', 'bottom': 'var:preset|spacing|80', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
    'css': '& .is-style-folio{color:var(--wp--preset--color--foil)}&{position:relative;outline:1px solid var(--wp--preset--color--foil);outline-offset:calc(-1 * var(--wp--preset--spacing--30));'
           'box-shadow:inset 0 0 0 calc(var(--wp--preset--spacing--30) + 5px) var(--wp--preset--color--board),inset 0 0 0 calc(var(--wp--preset--spacing--30) + 6px) var(--wp--preset--color--foil)}'})
section('leader', 'Dot leader line', ['core/paragraph'], {
    'css': '&{display:flex;align-items:baseline;gap:.5em;margin-block:0;padding-block:.3em}& .leader{flex:1 1 2em;border-bottom:1px dotted currentColor;transform:translateY(-.3em);min-width:1.5em}& .folio{font-variant-numeric:lining-nums tabular-nums;font-size:var(--wp--preset--font-size--small);white-space:nowrap}'})
section('leader-row', 'Dot leader row', ['core/group'], {
    'css': '&{display:flex;align-items:baseline;gap:.5em;flex-wrap:nowrap}&::after{content:"";flex:1 1 2em;order:1;border-bottom:1px dotted currentColor;transform:translateY(-.3em)}&>:first-child{order:0}&>:last-child{order:2;white-space:nowrap}'})
section('sidenote', 'Side-note (outer margin)', ['core/column', 'core/group', 'core/paragraph', 'core/categories'], {
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.5'},
    'color': {'text': 'var:preset|color|muted'},
    'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'left': 'var:preset|spacing|30'}},
    'css': '&.wp-block-categories{list-style:none;margin:0}'})
section('running-head', 'Running head', ['core/group'], {
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|x-small'},
    'color': {'text': 'var:preset|color|muted'},
    'border': {'bottom': {'color': 'var:preset|color|accent-2', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'bottom': 'var:preset|spacing|20'}}})
section('folio', 'Folio', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|small'},
    'color': {'text': 'var:preset|color|muted'}})
section('swatch', 'Cloth swatch', ['core/group'], {
    'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|line', 'radius': '0'},
    'css': '&{aspect-ratio:1/1;min-height:0;width:100%;align-self:stretch}'})
section('notice', 'Notice (gold rule)', ['core/group', 'core/paragraph'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '3px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('pair', 'Before and after pair', ['core/columns', 'core/gallery'], {
    'css': '& img{aspect-ratio:4/5;object-fit:cover;width:100%;height:auto}& figcaption{text-align:left}'})
section('contents', 'Contents list', ['core/post-template'], {
    'css': '&>li{border-bottom:1px solid var(--wp--preset--color--line);padding-block:.5em;margin:0!important}'})
section('rule-top', 'Gold hairline above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|accent-2', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})
section('rule-row', 'Ruled row (label and value)', ['core/group'], {
    'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
    'css': '&>*{margin:0!important}&>:last-child{text-align:right;font-variant-numeric:lining-nums tabular-nums}'})
section('plate', 'Plate (image on board)', ['core/group', 'core/image'], {
    'color': {'background': 'var:preset|color|surface'},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}}})

# ------------------------------------------------------------------ helpers
def hid(text, anchor, level=2, **a):
    h = heading(text, level, **a)
    return h.replace('<h%d class="' % level, '<h%d id="%s" class="' % (level, anchor), 1)

def leader(name, price, **a):
    return para('%s<span class="leader"></span><span class="folio">%s</span>' % (name, price), className='is-style-leader', **a)

def sidenote(*ps):
    return J(*[para(p) for p in ps])

CENTER = {'typography': {'textAlign': 'center'}}
PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

# ------------------------------------------------------------------ parts
write('parts/header.html', group(J(
    row(J(dyn('site-title', level=0), dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'})),
        justify='space-between', align='wide'),
    ), tag='header', align='full', className='is-style-running-head',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}))

write('parts/footer.html', group(J(
    columns(('38%', J(heading('Colophon', 2, fontSize='large'),
                      para('This site is set in Goudy Bookletter 1911, drawn by Barry Schwartz after Frederic Goudy\'s Kennerley, with EB Garamond for the text, the running heads and the measurements. The paper colour is a guess at our laid stock, and so is every cloth swatch on your screen.', fontSize='small'))),
            (None, J(heading('Bindery', 6), para('ul. Józefa 14, courtyard, first floor<br>31-056 Kraków, Kazimierz<br>By appointment only', fontSize='small'))),
            (None, J(heading('Hours', 6), para('Tuesday to Friday, 10:00 to 17:00<br>Saturday, 10:00 to 13:00<br>Closed in August', fontSize='small'))),
            (None, J(heading('Write or call', 6), para('<a href="mailto:pracownia@example.com">pracownia@example.com</a><br>+48 601 234 567, texts are fine<br><a href="https://www.instagram.com/">Instagram</a>', fontSize='small'))),
            align='wide'),
    para('Demo images are public-domain and CC0 photographs of historical bindings from the British Library, the Walters Art Museum and Wikimedia Commons, used as stand-ins for our own work.', align='wide', textColor='foil', fontSize='x-small'),
    ), tag='footer', align='full', className='is-style-board',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|60'}}}))

write('parts/notice.html', pattern_ref('turnaround-line'))

# ------------------------------------------------------------------ templates
def running_head(right):
    return row(J(para('Wójcik Bindery, Kraków', className='is-style-folio'), right), justify='space-between', align='wide')

MAIN = {'style': {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|80'}}}}

write('templates/front-page.html', page_template(J(
    pattern_ref('cover-board'), pattern_ref('before-after'), pattern_ref('contents-services'),
    pattern_ref('recent-case-studies'), pattern_ref('workshops-teaser'), pattern_ref('visit-strip')), **{'style': {'spacing': {'padding': {'top': '0', 'bottom': 'var:preset|spacing|70'}}}}))

write('templates/page.html', page_template(J(
    running_head(dyn('post-title', level=0, fontSize='small', textColor='muted', style={'typography': {'fontStyle': 'italic'}})),
    dyn('post-title', level=1, fontSize='display', style={'spacing': {'margin': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}}}),
    dyn('post-content', layout={'type': 'constrained'})), **MAIN))

write('templates/page-wide.html', page_template(J(
    running_head(dyn('post-title', level=0, fontSize='small', textColor='muted', style={'typography': {'fontStyle': 'italic'}})),
    dyn('post-title', level=1, fontSize='display', align='wide', style={'spacing': {'margin': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}}}),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1180px'})), **MAIN))

write('templates/single.html', page_template(J(
    running_head(dyn('post-terms', term='category')),
    dyn('post-title', level=1, fontSize='xx-large', align='wide', style={'spacing': {'margin': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|40'}}}),
    columns(('68%', dyn('post-content', layout={'type': 'default'})),
            ('32%', group(J(
                heading('Case note', 6),
                dyn('post-date', format='F Y'),
                para('Every job starts with an estimate. Send three photos: the spine, the front board and the worst page.'),
                para('<a href="/visit/#estimate">How to ask for an estimate</a>')), className='is-style-sidenote', layout={'type': 'default'})),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Previous case', showTitle=True),
                dyn('post-navigation-link', label='Next case', showTitle=True)), justify='space-between'),
          align='wide', className='is-style-rule-top', layout={'type': 'default'})), **MAIN))

CASE_CARD = J(dyn('post-featured-image', isLink=True, aspectRatio='4/5', scale='cover'),
              dyn('post-terms', term='category'),
              dyn('post-title', isLink=True, level=2, fontSize='large'),
              dyn('post-excerpt', excerptLength=22, moreText=''))

pattern('case-study-grid', 'Case studies (grid, inherits the page query)', 'bind-cases,query', inherit_query(
    CASE_CARD, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}, align='wide'), inserter=False)

pattern('post-list', 'Post list (contents style)', 'bind-cases,query', inherit_query(
    group(J(dyn('post-title', isLink=True, level=2, fontSize='medium'), dyn('post-date', format='Y')), className='is-style-leader-row', layout={'type': 'flex', 'flexWrap': 'nowrap'}),
    template_class='is-style-contents'), inserter=False)

write('templates/home.html', page_template(J(
    running_head(para('Case studies', className='is-style-folio')),
    heading('Case studies', 1, fontSize='display', align='wide', style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}),
    columns(('62%', para('Each job written up the way we write it in the bench book: what came in, what we did, what we left alone and why. The photos are taken under the same lamp before and after, at the same crop.')),
            ('38%', dyn('categories', className='is-style-sidenote')), align='wide'),
    pattern_ref('case-study-grid')), **MAIN))

write('templates/archive.html', page_template(J(
    running_head(para('Case studies', className='is-style-folio')),
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='display'),
    dyn('term-description', align='wide'),
    pattern_ref('case-study-grid')), **MAIN))

write('templates/index.html', page_template(J(
    dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), **MAIN))

write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Thesis, rebacking, clamshell', buttonText='Search'),
    pattern_ref('post-list')), **MAIN))

write('templates/404.html', page_template(J(
    running_head(para('Page missing', className='is-style-folio')),
    heading('This leaf has come loose', 1, fontSize='xx-large', style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}),
    para('The address may be old, or we moved the page when we reorganised the price guide. Try the <a href="/services/">services contents</a>, or search.'),
    dyn('search', label='Search', showLabel=False, placeholder='Thesis, rebacking, clamshell', buttonText='Search')), **MAIN))

# ------------------------------------------------------------------ patterns: home
pattern('cover-board', 'Front board: bindery name stamped in gold', 'featured', group(J(
    para('Introligatornia in Kazimierz, Kraków, since 1998', className='is-style-folio', textColor='foil', style=CENTER),
    heading('Wójcik Bindery', 1, fontSize='display', style=CENTER),
    para('Old books repaired and new books bound by hand, at two benches in a Kazimierz courtyard', fontSize='large', style=CENTER),
    para('Agnieszka Wójcik and Tomasz Lis. Conservation, theses, small editions, and boxes for books that should not be rebound.', style=CENTER),
    buttons(('Ask for an estimate', '/visit/#estimate'), ('See the price guide', '/price-guide/', {'className': 'is-style-outline'}), layout={'type': 'flex', 'justifyContent': 'center'})),
    align='full', className='is-style-board', layout={'type': 'constrained', 'contentSize': '860px'}),
    description='The home page opener, set like the front board of a cloth binding with a tooled double frame.')

pattern('before-after', 'Before and after pair with side-note', 'featured,bind-cases', group(J(
    columns(('40%', image('damaged.jpg', 'Worn brown calf binding with a split spine, rubbed corners and a paper shelf label, a ruler along the right edge', 'Before: calf, spine split, both joints gone')),
            ('40%', image('restored.jpg', 'Brown calf binding with tooled borders and a sound spine, photographed flat with a ruler below', 'After: rebacked, original boards and label kept')),
            ('20%', group(J(heading('Case 41', 6),
                            para('Sermons, Venice 1492. Owned by a parish in Nowy Sącz.'),
                            para('Rebacked in dyed calf. Joints lined with Japanese tissue. Wheat starch paste only.'),
                            para('31 bench hours, spread over five weeks while the paste dried.'),
                            para('<a href="/case-studies/">All case studies</a>')), className='is-style-sidenote', layout={'type': 'default'})),
            align='wide', className='is-style-pair', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}})),
    align='wide', layout={'type': 'default'}, style=PAD),
    description='Two photos at the same 4:5 crop, side by side, with the job details in the outer margin.')

pattern('contents-services', 'Contents page: services with dot leaders', 'bind-services', group(J(
    columns(('30%', J(heading('Contents', 2), para('What we do, with starting prices. Every job gets a written estimate first.', fontSize='small', textColor='muted'))),
            ('70%', J(
                leader('<a href="/services/#conservation">Conservation and repair</a>', 'from 180 zł'),
                leader('<a href="/services/#bindings">Custom bindings in cloth and leather</a>', 'from 420 zł'),
                leader('<a href="/services/#boxes">Clamshell boxes and slipcases</a>', 'from 290 zł'),
                leader('<a href="/price-guide/#theses">Theses and dissertations</a>', 'from 45 zł'),
                leader('<a href="/price-guide/#scripts">Scripts, logbooks and small editions</a>', 'from 140 zł'),
                leader('<a href="/price-guide/#dies">Stamping dies and custom artwork</a>', 'from 260 zł'),
                leader('<a href="/workshops/">Workshops at the bench</a>', '380 zł a day'))),
            align='wide', className='is-style-rule-top')),
    align='wide', layout={'type': 'default'}, style=PAD))

pattern('recent-case-studies', 'Recent case studies (contents list)', 'bind-cases,query', group(J(
    columns(('30%', J(heading('From the bench book', 2), para('<a href="/case-studies/">Every case study</a>', fontSize='small'))),
            ('70%', query(group(J(dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-terms', term='category')), className='is-style-leader-row', layout={'type': 'flex', 'flexWrap': 'nowrap'}),
                          per_page=6, template_class='is-style-contents')),
            align='wide', className='is-style-rule-top')),
    align='wide', layout={'type': 'default'}, style=PAD))

pattern('workshops-teaser', 'Workshops teaser with photo', 'bind-workshops', group(
    media_text('sewing.jpg', 'Brown leather binding with two brass clasps and a paper request slip tucked in the top', J(
        heading('Workshops, eight places at a time', 2),
        para('One-day classes on Saturdays. You sew a book on tapes, cover it in cloth and take it home. Materials are included and we provide the tea.'),
        para('Next date: Saturday 14 November, coptic stitch notebooks. Four places left.', className='is-style-notice'),
        buttons(('See the workshop dates', '/workshops/'))), width=42),
    align='wide', layout={'type': 'default'}, style=PAD))

pattern('visit-strip', 'Visit: appointment only strip', 'bind-visit', group(
    columns((None, J(heading('By appointment only', 3), para('No walk-ins. The door to the courtyard is locked and we are usually up to the elbows in paste. Write or text first and we will give you a time.'))),
            (None, J(heading('Where', 3), para('ul. Józefa 14, courtyard, first floor. Tram 3 or 24 to Miodowa, then two minutes on foot. Ring the bell marked Introligatornia.'))),
            (None, J(heading('How to reach us', 3), para('<a href="mailto:pracownia@example.com">pracownia@example.com</a><br>+48 601 234 567<br>We reply within two working days.'))),
            align='wide', className='is-style-rule-top'),
    align='wide', layout={'type': 'default'}, style=PAD))

# ------------------------------------------------------------------ services
pattern('conservation-services', 'Conservation service list', 'bind-services', group(J(
    hid('Conservation and repair', 'conservation'),
    para('We repair books so they can be read and handled again, and we keep as much of the original as we can. Every step is written down and the notes go back with the book.'),
    columns(('66%', J(
        heading('Re-hinging and rebacking', 4), para('Loose boards reattached with linen and Japanese tissue. Where the spine leather has gone, a new spine in dyed calf or goat, with the old spine laid back on top if it survives. From 380 zł.'),
        heading('Red rot consolidation', 4), para('Powdery, crumbling leather treated with Klucel G in ethanol so it stops coming off on your hands. It will not look new. From 180 zł per volume.'),
        heading('Page repair with toned Japanese tissue', 4), para('Tears and losses filled with kozo tissue toned to the page with acrylics. Starch paste, reversible. From 12 zł per repair, quoted per book.'),
        heading('Maps and documents', 4), para('Folded maps, deeds and certificates flattened, repaired along the folds and rehoused in a folder or box. From 220 zł.'))),
        ('34%', sidenote('We do not wash or bleach paper unless there is a conservation reason, and we will say so in the estimate.', 'No PVA on anything printed before 1900. Wheat starch paste and time.', 'Insurance valuations: ask an antiquarian bookseller, not us.')),
        align='wide')), align='wide', layout={'type': 'default'}))

pattern('bindings-service', 'Custom bindings', 'bind-services', group(J(
    hid('Custom bindings', 'bindings'),
    columns(('50%', image('leather.jpg', 'Blind-tooled pale leather binding with an interlaced strapwork panel, photographed flat with a ruler', 'Blind-tooled goatskin, the kind of panel we can match')),
            ('50%', J(para('Case bindings in bookcloth, quarter and full leather, and limp vellum for the occasional brave client. We bind new books from your printed sheets or from a PDF we print on archival paper.'),
                      lst(['Cloth case binding, from 420 zł', 'Quarter leather with cloth sides, from 780 zł', 'Full goatskin with gold-tooled spine, from 1,600 zł', 'Limp vellum, quoted after a conversation']),
                      para('Four to eight weeks. Gold titling on the spine is included in every price.', className='is-style-sidenote'))), align='wide')),
    align='wide', layout={'type': 'default'}, style=PAD))

pattern('clamshell-spec', 'Clamshell box spec card', 'bind-services', group(J(
    hid('Clamshell boxes and slipcases', 'boxes'),
    para('A box is the right answer for a book that is too fragile or too important to rebind. It keeps out light and dust and takes the weight off the spine.'),
    table([['Structure', 'Two trays, hinged, with a cloth-covered spine'], ['Boards', '2 mm grey board, acid-free'], ['Covering', 'Any cloth from the swatch library'],
           ['Lining', 'Unbuffered paper or felt for leather'], ['Label', 'Gold-stamped leather label on the spine'], ['Price', 'from 290 zł up to 30 cm tall']],
          head=['Clamshell box', 'Specification'], className='is-style-regular')),
    className='is-style-notice', layout={'type': 'constrained'}))

pattern('materials', 'Materials: cloth, leather and endpapers', 'bind-services', group(J(
    heading('Materials we keep', 2),
    columns((None, J(image('marbled.jpg', 'Open book with a printed prize certificate pasted inside and dark swirled marbled endpapers', 'Marbled endpaper, 19th century, from a book we rebacked', aspectRatio='4/3', scale='cover'),
                     heading('Endpapers', 4), para('Plain Canson, Japanese Tosa Washi, and marbled papers by Anna Łoś, marbled in Tarnów in small runs.'))),
            (None, J(image('endpapers.jpg', 'Two pages of stone-marbled paper in pink, red, violet and cream', 'Hand-marbled paper, one sheet of 12 we have left', aspectRatio='4/3', scale='cover'),
                     heading('Bookcloth', 4), para('Library buckram for theses, Asahi and Brillianta for bindings. <a href="/cloth-swatches/">Every colour in stock</a>.'))),
            (None, J(image('gilding.jpg', 'Narrow leather spine gold-tooled with small repeated flowers, a ruler beside it', 'Gold-tooled spine with a small floral tool', aspectRatio='4/3', scale='cover'),
                     heading('Leather and foil', 4), para('Harmatan goatskin in eleven colours, calf for repairs, genuine 23-carat gold leaf and foil in gold, silver and black.'))),
            align='wide')), align='wide', layout={'type': 'default'}, style=PAD))

pattern('credentials-line', 'Conservator credentials line', 'bind-about', para(
    'Agnieszka Wójcik, MA in paper and leather conservation, Academy of Fine Arts in Kraków, 2004. Member of the Polish Association of Conservators of Works of Art.',
    className='is-style-sidenote'))

pattern('services-page', 'Page: services', 'bind-services', J(
    pattern_ref('contents-services'), pattern_ref('conservation-services'), pattern_ref('bindings-service'),
    pattern_ref('clamshell-spec'), pattern_ref('materials'), pattern_ref('order-process')), block_types='core/post-content')

# ------------------------------------------------------------------ price guide
pattern('thesis-options', 'Thesis binding options table', 'bind-prices', group(J(
    hid('Theses and dissertations', 'theses'),
    para('Check your faculty rules before you choose. Most Kraków universities want a hard case in dark cloth with gold lettering on the spine; some accept soft covers for the library copy.'),
    table([['Wire binding', 'Clear front, card back', 'same day', '45 zł'],
           ['Channel binding', 'Cloth-effect card cover', 'next day', '60 zł'],
           ['Soft buckram', 'Buckram over card, lettered on the front', '2 days', '75 zł'],
           ['Thermal', 'Glued, card cover', 'same day', '40 zł'],
           ['Hard case', 'Library buckram over 2.5 mm board, sewn', '3 days', '110 zł']],
          head=['Binding', 'What you get', 'Ready in', 'Per copy']),
    para('Maximum 7 cm per volume. Title, initials and surname in gold on the spine are included on hard cases. Extra copies of the same thesis are 90 zł each.', className='is-style-sidenote')),
    align='wide', layout={'type': 'constrained', 'contentSize': '860px'}, style=PAD))

pattern('script-prices', 'Script and small edition price table', 'bind-prices', group(J(
    hid('Scripts, logbooks and small editions', 'scripts'),
    table([['Cloth hardcover', 'Sewn, any colour from the swatch library', '140 zł'],
           ['Leather hardcover', 'Goatskin, gold-tooled spine', '420 zł'],
           ['Stamping die', 'Brass, made to your artwork, kept for reorders', '260 zł once'],
           ['Printing', 'Archival 100 g paper, double-sided', '0.40 zł per page']],
          head=['Item', 'Details', 'Price'])),
    align='wide', layout={'type': 'constrained', 'contentSize': '860px'}, style=PAD))

pattern('turnaround-line', 'Turnaround line (rush not available)', 'bind-prices', group(
    para('Turnaround right now: <strong>2 to 3 weeks</strong> for bindings, 6 to 10 weeks for conservation. Rush jobs are not available in May and June, which is thesis season.'),
    align='wide', className='is-style-notice', layout={'type': 'default'}),
    description='Change this line when the queue changes. One place, used on the price guide and the notice part.')

pattern('conservation-bands', 'Conservation price bands', 'bind-prices', group(J(
    heading('Conservation, roughly', 2),
    para('Conservation is priced per book after we have seen it. These are the ranges most jobs fall into.'),
    leader('Board reattached, one joint', '180 to 300 zł'),
    leader('Rebacked in leather, original spine laid down', '450 to 900 zł'),
    leader('Resewn and rebound, original covers kept', '900 to 1,800 zł'),
    leader('Red rot consolidation, per volume', '180 to 260 zł'),
    leader('Map or document, repaired and folded into a folder', '220 to 480 zł'),
    para('Estimates are free if you bring the book in. By email we can only give a range.', className='is-style-sidenote')),
    layout={'type': 'constrained', 'contentSize': '860px'}, style=PAD))

pattern('stamping-dies', 'Stamping dies and artwork specs', 'bind-prices', group(J(
    hid('Stamping dies and custom artwork', 'dies'),
    columns(('60%', lst(['Send vector artwork: PDF, SVG or EPS, with text converted to outlines.',
                         'Lines no thinner than 0.3 mm, gaps no smaller than 0.4 mm. Anything finer fills in.',
                         'Maximum die size 12 × 18 cm.',
                         'Foils in stock: gold, silver, copper, black, white and blind (no foil).',
                         'The die is yours. We keep it in a labelled drawer for reorders.'])),
            ('40%', J(image('tools.jpg', 'Printed catalogue page of brass bookbinding ornaments, borders and corner pieces', 'A 19th-century catalogue of finishing tools. We own eleven of these.'),
                      para('Die from 260 zł, made in Bielsko-Biała in about ten days.', className='is-style-sidenote'))), align='wide')),
    align='wide', layout={'type': 'default'}, style=PAD))

pattern('trade-terms', 'Small press trade terms table', 'bind-prices', group(J(
    heading('Trade terms for authors and small presses', 2),
    table([['Cloth case binding, same design', '3 to 9 copies', '25% off'],
           ['Cloth case binding, same design', '10 copies or more', '40% off'],
           ['Slipcases for a numbered edition', '10 copies or more', '30% off'],
           ['Stamping die', 'any edition', 'kept free for reorders']],
          head=['Work', 'Quantity', 'Discount']),
    para('Minimum three copies. Invoices on 14 days for publishers we have worked with before.', className='is-style-sidenote')),
    layout={'type': 'constrained', 'contentSize': '860px'}, style=PAD))

pattern('price-guide-page', 'Page: price guide', 'bind-prices', J(
    pattern_ref('turnaround-line'), pattern_ref('thesis-options'), pattern_ref('script-prices'),
    pattern_ref('conservation-bands'), pattern_ref('stamping-dies'), pattern_ref('trade-terms')), block_types='core/post-content')

# ------------------------------------------------------------------ order, estimate, visit
pattern('order-process', 'Order process steps', 'bind-visit', group(J(
    heading('How an order works', 2),
    lst(['Send your deadline, the PDF or a photo of the book, its size in centimetres, the page count and how many copies.',
         'We reply within two working days with an itemised estimate and, for new bindings, a mock-up in the cloth you picked.',
         'A 30% deposit books the bench time. For theses there is no deposit; you pay on collection.',
         'We write when it is ready. Collect from the bindery or we post it with InPost, 18 zł within Poland.'], ordered=True)),
    layout={'type': 'constrained'}, style=PAD))

pattern('estimate-request', 'Estimate request with photos', 'bind-visit', group(J(
    hid('Ask for an estimate', 'estimate'),
    para('Email three photos: the spine, the front board and the worst page. Add the size in centimetres, what the book means to you, and whether you want it usable or just stable.'),
    para('We answer with a price range and a date. If the book is valuable, bring it in instead; we do not quote finals from photos.'),
    buttons(('Email the photos', 'mailto:pracownia@example.com?subject=Estimate%20request'))),
    className='is-style-notice', layout={'type': 'constrained'}))

pattern('appointment-only', 'Appointment only header', 'bind-visit', group(J(
    para('<strong>By appointment only, no walk-ins.</strong> Email <a href="mailto:pracownia@example.com">pracownia@example.com</a> or text +48 601 234 567 and we will give you a time.')),
    className='is-style-notice', layout={'type': 'constrained'}))

pattern('visit-details', 'Visit details: address, hours, directions', 'bind-visit', columns(
    ('60%', J(heading('Finding the bindery', 2),
              para('ul. Józefa 14, 31-056 Kraków. Go through the gate into the courtyard; our door is on the left, first floor, with a brass plate that says Introligatornia. There are 22 stairs and no lift. If stairs are a problem, tell us and we will come down to you.'),
              para('Tram 3 or 24 to Miodowa. Paid parking on Starowiślna, none in the courtyard.'),
              image('workbench.jpg', 'An older binder at a cluttered workbench surrounded by tied stacks of loose printed sheets', 'A bench in a bindery much like ours, with sheets tied up waiting for sewing'))),
    ('40%', J(heading('Hours', 6),
              table([['Tuesday to Friday', '10:00 to 17:00'], ['Saturday', '10:00 to 13:00'], ['Sunday, Monday', 'closed'], ['August', 'closed']]),
              heading('Collection', 6),
              para('Theses can be collected without an appointment on weekdays from 15:00 to 17:00 in May and June.', fontSize='small'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('visit-page', 'Page: visit and estimates', 'bind-visit', J(
    pattern_ref('appointment-only'), pattern_ref('visit-details'), pattern_ref('estimate-request'), pattern_ref('faq')), block_types='core/post-content')

pattern('faq', 'Questions people email us', 'bind-visit', group(J(
    heading('Questions people email us', 2),
    details('Can you make my book look new?', para('We can, but we usually advise against it. A rebacked book with its old boards keeps its history and most of its value.')),
    details('Do you buy or value old books?', para('No. For valuations, ask an antiquarian bookseller. Antykwariat Rara on Szewska is a good start.')),
    details('Can you bind my thesis today?', para('Wire and thermal bindings, yes, if the PDF reaches us by noon. Hard cases take three days.')),
    details('Will you post a book back to me?', para('Yes, within Poland with InPost, packed between boards. Outside Poland by courier, quoted per parcel.')),
    details('Do you take card?', para('Yes, and BLIK. No card payments under 20 zł.'))),
    layout={'type': 'constrained'}, style=PAD))

# ------------------------------------------------------------------ workshops
pattern('workshops-panel', 'Workshops panel with dates', 'bind-workshops', group(J(
    para('Saturdays from 10:00 to 16:00, at the big bench. Eight places. Materials, tools and lunch from Bar Mleczny Pod Temidą are included. You go home with the book you made.'),
    table([['14 November', 'Coptic stitch notebooks', 'Beginners', '4 places left'],
           ['28 November', 'Case binding in cloth', 'Beginners', 'Full'],
           ['12 December', 'Paper repair with Japanese tissue', 'Some experience', '6 places left'],
           ['16 January', 'Leather paring and quarter leather', 'Some experience', 'Temporarily unavailable']],
          head=['Date', 'Workshop', 'Level', 'Places']),
    para('380 zł a day. Book by email; we hold your place for three days while you pay.'),
    buttons(('Email to book a place', 'mailto:pracownia@example.com?subject=Workshop'))),
    layout={'type': 'constrained', 'contentSize': '860px'}))

pattern('classes-unavailable', 'Classes: temporarily unavailable', 'bind-workshops', group(J(
    heading('Leather classes are paused', 3),
    para('Tomasz is rebuilding the paring bench this winter, so leather workshops start again in February. Write if you want to hear first.')),
    className='is-style-notice', layout={'type': 'constrained'}),
    description='Use when a class series is paused.')

pattern('workshop-kit', 'What to bring to a workshop', 'bind-workshops', columns(
    ('55%', J(heading('What to bring', 3), lst(['An apron or a shirt you do not mind getting paste on', 'Reading glasses if you use them', 'Nothing else. We have the bone folders.']))),
    ('45%', image('press.jpg', 'Heavy cast-iron nipping press with a threaded screw, standing on a wooden pallet', 'Our nipping press is older than both of us put together')),
    align='wide'))

pattern('workshops-page', 'Page: workshops', 'bind-workshops', J(
    pattern_ref('workshops-panel'), pattern_ref('workshop-kit'), pattern_ref('classes-unavailable')), block_types='core/post-content')

# ------------------------------------------------------------------ swatches (signature)
SW = [('sw-bottle', 'AS-311', 'Asahi, bottle green', 'In stock'), ('sw-oxblood', 'BR-4531', 'Brillianta, oxblood', 'In stock'),
      ('sw-navy', 'LB-120', 'Library buckram, navy', 'Thesis cloth, in stock'), ('sw-ochre', 'AS-204', 'Asahi, ochre', 'Limited stock, mill closed 2022'),
      ('sw-dove', 'BR-4526', 'Brillianta, dove grey', 'In stock'), ('sw-black', 'LB-100', 'Library buckram, black', 'Thesis cloth, in stock'),
      ('sw-linen', 'LN-01', 'Natural linen, unbleached', 'Two rolls left'), ('sw-tan', 'HG-07', 'Harmatan goatskin, tan', 'Leather, per half skin')]

def swatch(slug, code, name, stock):
    return stack(J(group('', backgroundColor=slug, className='is-style-swatch', layout={'type': 'default'}),
                   para('<strong>%s</strong>' % code, className='is-style-folio'),
                   para(name, fontSize='small'),
                   para(stock, className='is-style-folio'),
                   para('<a href="mailto:pracownia@example.com?subject=Use%%20cloth%%20%s">Use this cloth</a>' % code, fontSize='small')),
                 style={'spacing': {'blockGap': 'var:preset|spacing|10'}})

pattern('swatch-library', 'Cloth swatch library', 'featured,bind-services', group(J(
    grid(J(*[swatch(*s) for s in SW]), min_width='11rem', align='wide'),
    pattern_ref('swatch-note')), align='wide', layout={'type': 'default'}),
    description='Every cloth and leather in stock, with the maker code. "Use this cloth" starts an email with the code in the subject.')

pattern('swatch-note', 'Swatch note: colours are indicative', 'bind-services', para(
    'Colours are indicative only and subject to availability. Screens vary; our cloths do not. If the colour matters, ask and we will post you a 5 × 5 cm sample free within Poland.',
    className='is-style-notice'))

pattern('swatches-page', 'Page: cloth swatches', 'bind-services', J(
    para('Every bookcloth and leather we have on the shelf, with the maker\'s code. Quote the code in your order, or click the link under a swatch to start an email with it.'),
    pattern_ref('swatch-library'),
    pattern_ref('materials')), block_types='core/post-content')

# ------------------------------------------------------------------ case study pieces and about
pattern('case-spec', 'Case study specification table', 'bind-cases', table(
    [['Structure', 'Sewn on five raised cords, laced-in boards'], ['Covering', 'Original calf, new calf spine'], ['Endpapers', 'Original, one leaf guarded'],
     ['Tooling', 'Blind, original; new spine left plain'], ['Size', '21 × 15 × 4 cm'], ['Year of work', '2025']],
    head=['Case note', ''], className='is-style-regular'))

pattern('before-after-simple', 'Before and after pair (no side-note)', 'bind-cases', columns(
    (None, image('boards.jpg', 'Dark leather-covered book with a torn and replaced corner patch, photographed flat', 'Before')),
    (None, image('restored.jpg', 'Brown calf binding with tooled borders and a sound spine, photographed flat with a ruler below', 'After')),
    align='wide', className='is-style-pair'))

pattern('about-bindery', 'About the bindery', 'bind-about', group(J(
    columns(('60%', J(
        para('The bindery opened in 1998 as Tomasz\'s uncle\'s thesis shop in Tarnów. It moved to Kazimierz in 2011, when Agnieszka finished her conservation training and the rent in Tarnów doubled.', fontSize='large'),
        para('Agnieszka does the conservation: repairs, rebacks, boxes and anything with a museum number on it. Tomasz does the new bindings, the theses and the gold finishing. Both of us teach.'),
        para('We turn down about one job in ten, usually because the kindest thing for the book is a box and a dry shelf. We would rather tell you that than take the money.'),
        pattern_ref('credentials-line'))),
            ('40%', image('repair.jpg', 'A conservator\'s hands lifting a torn fragment of an old manuscript with tweezers on a white board', 'Repairing a torn leaf; we use tissue and paste, never tape')),
            align='wide')), align='wide', layout={'type': 'default'}, style=PAD))

pattern('care-notes', 'Looking after old books', 'bind-about', group(J(
    heading('Looking after old books at home', 3),
    lst(['Shelve them upright, not too tight, away from radiators and south windows.',
         'Pull a book out by its sides, never by the top of the spine.',
         'Do not tape anything. Put loose leaves in an envelope inside the front cover and bring it to us.',
         'Leather dressing does more harm than good on old leather. Leave it dry.'])),
    layout={'type': 'constrained'}, style=PAD))

pattern('quote-client', 'Quote from a client', 'bind-about', quote(
    'They told me not to rebind my grandfather\'s prayer book and made a box for it instead. It sits on the shelf and nobody has to be careful with it any more.',
    'Ewa Kozłowska, Podgórze, box made in March 2025'))

pattern('workshop-notice', 'Notice: next workshop', 'bind-workshops', para(
    'Next workshop: Saturday 14 November, coptic stitch notebooks, four places left. <a href="/workshops/">Dates and booking</a>',
    className='is-style-notice'))

write('functions.php', '''<?php
/**
 * Bind: pattern categories only.
 *
 * @package bind
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'bind-services'  => 'Bindery: services',
			'bind-prices'    => 'Bindery: price guide',
			'bind-cases'     => 'Bindery: case studies',
			'bind-workshops' => 'Bindery: workshops',
			'bind-visit'     => 'Bindery: visit and orders',
			'bind-about'     => 'Bindery: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);''')

print('bind: patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

# ------------------------------------------------------------------ demo content
# ---- case-study kit: the same builders make the patterns and the demo posts
def cs_pair(before, before_alt, after, after_alt, cap_b='Before', cap_a='After', src=''):
    return columns((None, image(src + before, before_alt, cap_b)), (None, image(src + after, after_alt, cap_a)), className='is-style-pair', align='wide')

def cs_came_in(text, note):
    return columns(('66%', J(heading('What came in', 2), para(text))), ('34%', group(para(note), className='is-style-sidenote', layout={'type': 'default'})))

def cs_steps(steps, hours):
    return columns(('66%', J(heading('What we did', 2), lst(steps, ordered=True))),
                   ('34%', group(J(para('<strong>Bench time</strong>'), para(hours)), className='is-style-sidenote', layout={'type': 'default'})))

def cs_left_alone(text):
    return group(J(heading('What we left alone', 3), para(text)), className='is-style-notice', layout={'type': 'default'})

def cs_spec(rows):
    return group(J(heading('Case note', 6), *[row(J(para(k), para(v)), justify='space-between', className='is-style-rule-row') for k, v in rows]),
                 layout={'type': 'default'})

def cs_detail(img, alt, cap, text, src=''):
    return columns(('45%', image(src + img, alt, cap)), ('55%', J(heading('A closer look', 3), para(text))), verticalAlignment='center')

def cs_client(text, who):
    return quote(text, who)

def post_body(before, before_alt, after, after_alt, paras, spec):
    return J(cs_pair(before, before_alt, after, after_alt, src=IMG), *[para(p) for p in paras], cs_spec(spec))

def full_case(pair, came, note, steps, hours, alone, spec, detail, client):
    return J(cs_pair(*pair, src=IMG), cs_came_in(came, note), cs_steps(steps, hours), cs_left_alone(alone),
             cs_detail(*detail, src=IMG), cs_spec(spec), cs_client(*client))


D1 = ('damaged.jpg', 'Worn brown calf binding with a split spine and rubbed corners, a ruler along the edge', 'restored.jpg', 'Brown calf binding with tooled borders and a sound spine, photographed flat with a ruler below')
pattern('case-pair', 'Case study: before and after pair', 'bind-cases', cs_pair(*D1))
pattern('case-came-in', 'Case study: what came in, with a side-note', 'bind-cases', cs_came_in(
    'A parish register, 1788 to 1811, carried in a plastic bag. The front board was hanging by the cords and the first gathering had come loose.',
    'Brought in by the parish office in Wieliczka, March 2026.'))
pattern('case-steps', 'Case study: what we did, with bench time', 'bind-cases', cs_steps(
    ['Photographed every page before we touched it.', 'Lifted the spine leather and cleaned the old animal glue off the spine.', 'Resewed the loose gathering on the original cords.',
     'Lined the joints with Japanese tissue and reattached the board.', 'Laid the old spine back down with wheat starch paste.'], '18 hours over three weeks'))
pattern('case-left-alone', 'Case study: what we left alone', 'bind-cases', cs_left_alone(
    'The water stain across the lower corner of every page. It is two hundred years old, it is stable, and washing the paper would risk the ink.'))
pattern('case-spec-rows', 'Case study: spec rows', 'bind-cases', cs_spec([['Structure', 'Sewn on five raised cords'], ['Covering', 'Original calf, new calf spine'], ['Adhesive', 'Wheat starch paste'], ['Size', '31 × 20 × 6 cm'], ['Year of work', '2026']]))
pattern('case-detail', 'Case study: a closer look', 'bind-cases', cs_detail('gilding.jpg', 'Narrow leather spine gold-tooled with small repeated flowers, a ruler beside it', 'Spine panels after cleaning',
    'The spine tools were a small flower and a double fillet. We found a close match in our drawer, so the new panel on volume four sits next to the others.'))
pattern('case-client', 'Case study: note from the client', 'bind-cases', cs_client('It opens flat again and nobody has to hold the front board on with one hand.', 'Fr Marek Zając, parish of St Clement, Wieliczka, March 2026'))
pattern('case-full', 'Case study: full layout', 'bind-cases', J(pattern_ref('case-pair'), pattern_ref('case-came-in'), pattern_ref('case-steps'), pattern_ref('case-left-alone'),
    pattern_ref('case-detail'), pattern_ref('case-spec-rows'), pattern_ref('case-client')), post_types='post', description='A whole restoration case study built from the case-study patterns.')

CASES = [
  ('Sermons, Venice 1492: rebacked in calf', 'conservation', 'restored.jpg', '2025-09-12',
   ('damaged.jpg', 'Worn brown calf binding with a split spine and rubbed corners, a ruler along the edge', 'restored.jpg', 'Brown calf binding with tooled borders and a sound spine, photographed flat with a ruler below'),
   ['The parish in Nowy Sącz brought this in a shopping bag. Both joints had gone and the spine leather came off in three pieces.',
    'We lifted the old spine, lined the joints with Japanese tissue and put on a new spine in dyed calf. The old leather went back on top. The boards, clasps and shelf label are original.',
    'We did not clean the text block. The staining is 500 years old and tells you where people held it.'],
   [['Structure', 'Sewn on five raised cords'], ['Covering', 'Original calf, new calf spine'], ['Adhesive', 'Wheat starch paste'], ['Size', '21 × 15 × 4 cm'], ['Hours', '31']]),
  ('A thesis in navy buckram, 42 copies', 'theses', 'thesis.jpg', '2025-06-20',
   ('shelf.jpg', 'Title page of a 19th-century book of poems, yellowed, open flat', 'thesis.jpg', 'Decorated 19th-century cloth binding with gilt lettering and a lily on the front'),
   ['Forty-two hard-case theses for the Faculty of Chemistry, all in LB-120 navy with gold on the spine. The faculty wants the surname first, so we set it that way.',
    'The PDFs came in on a Monday and the copies went out on Thursday. In June that is about as fast as we go.'],
   [['Binding', 'Hard case, sewn'], ['Cloth', 'LB-120 library buckram, navy'], ['Lettering', 'Gold foil, spine and front'], ['Copies', '42'], ['Turnaround', '3 working days']]),
  ('A clamshell box for a family prayer book', 'boxes', 'boards.jpg', '2025-03-18',
   ('boards.jpg', 'Dark leather-covered book with a torn and replaced corner patch', 'sewing.jpg', 'Brown leather binding with brass clasps resting on a light wooden table'),
   ['Ewa wanted the prayer book rebound. We talked her out of it. The binding is weak but complete, and a new one would have thrown away the old repairs her grandfather made with shoe leather.',
    'Instead we made a clamshell box in AS-311 bottle green, lined with felt, with her grandfather\'s name stamped on the spine label.'],
   [['Box', 'Clamshell, two trays'], ['Cloth', 'AS-311 Asahi, bottle green'], ['Lining', 'Grey felt'], ['Label', 'Goatskin, gold-stamped'], ['Price', '340 zł']]),
  ('A 1730 map of Europe, flattened and mended along the folds', 'conservation', 'map.jpg', '2024-11-04',
   ('map.jpg', 'Hand-coloured 1730 map of Europe with a decorative border and text panels on either side', 'map.jpg', 'The same map after flattening, with the fold lines repaired'),
   ['Folded into sixteenths for about two hundred years, so every fold had split. We humidified it, flattened it between felts for a week and mended each fold from the back with thin kozo tissue.',
    'It now lives flat in a folder of unbuffered card, which the owner has promised to keep in a drawer and not on the wall.'],
   [['Object', 'Engraved map, hand-coloured'], ['Repair', 'Kozo tissue, wheat starch paste'], ['Housing', 'Folder, unbuffered card'], ['Size', '62 × 48 cm'], ['Hours', '14']]),
  ('Red rot on a set of law reports', 'conservation', 'damaged.jpg', '2024-09-15',
   ('damaged.jpg', 'Brown calf binding with powdery, rubbed leather and worn corners', 'leather.jpg', 'Pale tooled leather binding after consolidation, surface stable'),
   ['Twenty-two volumes from a law office on Grodzka. The leather came off as orange dust on every hand that touched it.',
    'We consolidated each volume with Klucel G in ethanol. It does not make the leather look new, and we said so in the estimate. It makes it stop crumbling.'],
   [['Volumes', '22'], ['Treatment', 'Klucel G, 2% in ethanol'], ['Time per volume', 'about 40 minutes'], ['Price', '180 zł per volume']]),
  ('A small edition of poems in quarter goatskin', 'bindings', 'leather.jpg', '2024-06-02',
   ('tools.jpg', 'Catalogue page of brass finishing tools and ornaments', 'leather.jpg', 'Blind-tooled pale leather binding with an interlaced panel'),
   ['Wydawnictwo Pod Wiatr printed 26 copies of Marta Nowicka\'s poems by letterpress and brought us the folded sheets.',
    'We sewed them on tapes and bound them in quarter tan goatskin with ochre Asahi sides. Ochre is AS-204, which the mill no longer makes, so we used half of our last roll.'],
   [['Copies', '26, numbered'], ['Binding', 'Quarter leather'], ['Materials', 'HG-07 goatskin, AS-204 cloth'], ['Tooling', 'Gold, spine only'], ['Trade terms', '25% off']]),
  ('Gold tooling a spine to match its neighbours', 'bindings', 'gilding.jpg', '2024-02-10',
   ('shelf.jpg', 'Title page of a worn 19th-century book', 'gilding.jpg', 'Narrow leather spine with gold-tooled small flowers'),
   ['One volume of a twelve-volume set had lost its spine in a flood. The owner wanted it to sit on the shelf without anyone noticing.',
    'Tomasz matched the flower tool from our drawer of old finishing tools and tooled the new spine in 23-carat gold leaf. The panels are a millimetre off. We told the owner which one it is.'],
   [['Covering', 'New calf spine'], ['Tooling', '23-carat gold leaf'], ['Tools', 'Small flower, two fillets'], ['Hours', '9']]),
  ('Marbled endpapers for a rebound cookbook', 'bindings', 'marbled.jpg', '2023-12-05',
   ('marbled.jpg', 'Open book showing a prize certificate and dark marbled endpapers', 'endpapers.jpg', 'Stone-marbled paper in pink, red and violet'),
   ['A handwritten family cookbook from Lwów, 1934, falling apart from use and butter. We resewed it and bound it in oxblood cloth.',
    'For the endpapers we used a sheet of marbled paper by Anna Łoś. The owner\'s daughter chose it because it looked like beetroot soup.'],
   [['Structure', 'Resewn, rounded and backed'], ['Cloth', 'BR-4531 Brillianta, oxblood'], ['Endpapers', 'Hand-marbled, Anna Łoś'], ['Hours', '12']]),
]

FULL = {
 'Sermons, Venice 1492: rebacked in calf': full_case(
    ('damaged.jpg', 'Worn brown calf binding with a split spine and rubbed corners, a ruler along the edge', 'restored.jpg', 'Brown calf binding with tooled borders and a sound spine, photographed flat with a ruler below'),
    'The parish in Nowy Sącz brought this in a shopping bag. Both joints had gone and the spine leather came off in three pieces when we lifted the book out.',
    'Incunable, printed in Venice in 1492. Owned by the parish since at least 1740, according to the inscription.',
    ['Photographed and collated every leaf.', 'Lifted the three pieces of spine leather and kept them in order.', 'Cleaned the old glue off the spine with methyl cellulose poultices.',
     'Lined the joints with Japanese tissue toned to the leather.', 'Put on a new spine in dyed calf and laid the old leather back on top.', 'Consolidated the corners with Klucel G.'],
    '31 hours over five weeks, most of it waiting for paste to dry',
    'The text block. The staining is five hundred years old and tells you where people held it. We did not wash, flatten or bleach a single leaf.',
    [['Structure', 'Sewn on five raised cords, laced-in boards'], ['Covering', 'Original calf, new calf spine'], ['Adhesive', 'Wheat starch paste'], ['Size', '21 × 15 × 4 cm'], ['Price', '1,480 zł']],
    ('leather.jpg', 'Blind-tooled pale leather binding with an interlaced strapwork panel', 'A similar blind-tooled panel from our reference shelf',
     'The front board has a blind-tooled strapwork panel. We did not re-tool it. The new spine is plain on purpose, so anyone can see where the old binding ends.'),
    ('We expected a bill for a new binding. We got our own book back, and it opens.', 'Ks. Andrzej Nowak, parish of St Margaret, Nowy Sącz, October 2025')),
 'A clamshell box for a family prayer book': full_case(
    ('boards.jpg', 'Dark leather-covered book with a torn and replaced corner patch, photographed flat', 'sewing.jpg', 'Brown leather binding with brass clasps resting in its new felt-lined tray', 'Before', 'After, in the box'),
    'Ewa wanted her grandfather\'s prayer book rebound. The binding is weak but complete, and he had mended the corners himself with shoe leather.',
    'Printed in Kraków in 1896. Pages clean, sewing sound, covers tired.',
    ['Talked Ewa out of a rebind.', 'Measured the book at six points, since it is not square.', 'Built a two-tray clamshell in 2 mm board.', 'Covered it in AS-311 bottle green cloth and lined the trays with grey felt.',
     'Stamped her grandfather\'s name in gold on a goatskin spine label.'],
    '9 hours',
    'The shoe-leather corner repairs. They are ugly and they are his, and they will outlast us.',
    [['Box', 'Clamshell, two trays'], ['Cloth', 'AS-311 Asahi, bottle green'], ['Lining', 'Grey felt'], ['Label', 'Goatskin, gold-stamped'], ['Price', '340 zł']],
    ('marbled.jpg', 'Open book showing a pasted certificate and dark marbled endpapers', 'The inside of the front cover',
     'The endpapers are marbled and the front one carries a First Communion certificate from 1931. The box keeps the cover closed without any pressure on it.'),
    ('It sits on the shelf and nobody has to be careful with it any more.', 'Ewa Kozłowska, Podgórze, March 2025')),
 'A 1730 map of Europe, flattened and mended along the folds': full_case(
    ('map.jpg', 'Hand-coloured 1730 map of Europe with a decorative border, folded creases visible', 'map.jpg', 'The same map after flattening, with the fold lines repaired from the back', 'Before, folded', 'After, flat'),
    'Folded into sixteenths for about two hundred years, so every fold had split and two corners were missing.',
    'Engraved and hand-coloured, 62 × 48 cm. Bought at a flea market in Wrocław for 40 zł.',
    ['Tested the colours for water sensitivity. They held.', 'Humidified the map in a chamber for two hours.', 'Flattened it between felts under light weight for a week.',
     'Mended every fold from the back with thin kozo tissue.', 'Filled the two corner losses with toned paper.', 'Made a folder of unbuffered card.'],
    '14 hours',
    'The foxing. It is stable, and bleaching it out would have taken the hand-colouring with it.',
    [['Object', 'Engraved map, hand-coloured'], ['Repair', 'Kozo tissue, wheat starch paste'], ['Housing', 'Folder, unbuffered card'], ['Size', '62 × 48 cm'], ['Price', '620 zł']],
    ('repair.jpg', 'A conservator lifting a torn fragment with tweezers on a white board', 'Mending a fold from the back',
     'Each fold gets a strip of tissue about 4 mm wide, torn, not cut, so the edge feathers into the paper and does not leave a line.'),
    ('It is in a drawer now, as promised. I take it out on Sundays.', 'Paweł Grzyb, Kazimierz, November 2024')),
 'Red rot on a set of law reports': full_case(
    ('damaged.jpg', 'Brown calf binding with powdery, rubbed leather and worn corners', 'leather.jpg', 'Leather binding after consolidation, surface stable'),
    'Twenty-two volumes from a law office on Grodzka. The leather came off as orange dust on every hand that touched it.',
    'Law reports, 1902 to 1924, still used by the office every month.',
    ['Vacuumed each volume through a screen.', 'Tested Klucel G at 1% and 2% on the worst spine.', 'Brushed 2% Klucel G in ethanol on every leather surface.',
     'Let each volume dry standing, fanned open, overnight.', 'Wrapped the three worst in protective jackets.'],
    'About 40 minutes per volume, 15 hours in all',
    'The appearance. Consolidation makes red rot stop coming off; it does not make the leather look new, and we said so in the estimate.',
    [['Volumes', '22'], ['Treatment', 'Klucel G, 2% in ethanol'], ['Jackets', '3, in Melinex'], ['Price', '180 zł per volume']],
    ('shelf.jpg', 'Title page of a worn 19th-century book open flat', 'One of the title pages',
     'The paper inside is in good shape. It was only ever the leather that was falling apart.'),
    ('The shelf no longer leaves orange on my suit.', 'Mec. Joanna Wrona, Grodzka Street, September 2024')),
}

content = {
  'site': {'title': 'Wójcik Bindery', 'tagline': 'Introligatornia: book conservation and hand binding in Kraków'},
  'categories': [{'slug': 'conservation', 'name': 'Conservation', 'description': 'Repairs to old books, maps and documents.'},
                 {'slug': 'bindings', 'name': 'Bindings', 'description': 'New bindings in cloth and leather.'},
                 {'slug': 'boxes', 'name': 'Boxes', 'description': 'Clamshells and slipcases.'},
                 {'slug': 'theses', 'name': 'Theses', 'description': 'Theses and dissertations.'}],
  'front_page': 'home', 'posts_page': 'case-studies',
  'pages': [
    {'slug': 'home', 'title': 'Home', 'content': ''},
    {'slug': 'case-studies', 'title': 'Case studies', 'content': ''},
    {'slug': 'services', 'title': 'Services', 'pattern': 'bind/services-page', 'template': 'page-wide'},
    {'slug': 'price-guide', 'title': 'Price guide', 'pattern': 'bind/price-guide-page', 'template': 'page-wide'},
    {'slug': 'workshops', 'title': 'Workshops', 'pattern': 'bind/workshops-page'},
    {'slug': 'cloth-swatches', 'title': 'Cloth swatches', 'pattern': 'bind/swatches-page', 'template': 'page-wide'},
    {'slug': 'about', 'title': 'About', 'content': J(pattern_ref('about-bindery'), pattern_ref('quote-client'), pattern_ref('care-notes')), 'template': 'page-wide'},
    {'slug': 'visit', 'title': 'Visit', 'pattern': 'bind/visit-page'},
  ],
  'posts': [{'title': t, 'category': c, 'image': img, 'date': d, 'excerpt': ps[0],
             'content': FULL.get(t) or post_body(*pair, ps, spec)} for t, c, img, d, pair, ps, spec in CASES],
  'nav': [{'label': 'Services', 'url': '/services/'}, {'label': 'Case studies', 'url': '/case-studies/'},
          {'label': 'Price guide', 'url': '/price-guide/'}, {'label': 'Workshops', 'url': '/workshops/'},
          {'label': 'Cloth', 'url': '/cloth-swatches/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Visit', 'url': '/visit/'}],
}
os.makedirs('demos/bind', exist_ok=True)
json.dump(content, open('demos/bind/content.json', 'w'), indent=1, ensure_ascii=False)
open('demos/bind/fonts-claim.txt', 'w').write('display: Goudy Bookletter 1911 (as registered for 262)\n')
print('bind: demo content written')
