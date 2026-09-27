# taproom: Cooperage Brewing, a small brewery and taproom in Smithfield, Dublin 7. Cans and merch through WooCommerce.
# Direction: the utility label system from the research. Brown paper, black type, one stamp red. The tap list is the
#   hero: a printed stock sheet with line number, beer, style, hops, ABV and prices, and a dated "updated" stamp.
# Why: the best small-brewery sites are the plainest (The Kernel). Staff change the list from a phone; the page just shows it.
# Fonts: Economica 700 (condensed, uppercase for beer names only) and Public Sans with tabular figures for everything else.
#   Two families, no monospace.
# Palette: brown paper #D9C3A0, ink #1A1A1A, stamp red #B3241A (prices and the updated date), label white #FFFFFF.
# Layout idea: every beer is shown as a white paper label stuck on brown paper, with 0 radius; the page itself is the bar wall.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('taproom')
D = THEME['dir']
IMG = '/wp-content/themes/taproom/assets/images/'

def palette(base, contrast, accent, surface, line, muted, dark):
    p = [('base', base, 'Brown paper'), ('contrast', contrast, 'Ink'), ('accent', accent, 'Stamp red'),
         ('surface', surface, 'Label'), ('line', line, 'Rule'), ('muted', muted, 'Pencil'), ('dark', dark, 'Stout')]
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Economica", "Arial Narrow", sans-serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"Public Sans", Arial, sans-serif'

def fs(slug, size, name, mn=None):
    return {'slug': slug, 'size': size, 'name': name, 'fluid': {'min': mn, 'max': size} if mn else False}

CSS = ('body{font-synthesis:none;font-variant-numeric:tabular-nums}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
       '.wp-block-table table td,.wp-block-table table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.55em .9em .55em 0;text-align:left;vertical-align:baseline}'
       '.wp-block-table table thead{border-bottom:0}.wp-block-table table th{font-weight:700;font-size:var(--wp--preset--font-size--x-small);border-bottom:2px solid var(--wp--preset--color--contrast)}'
       '.wp-block-table figcaption{text-align:left}'
       '.is-style-tap-list table{table-layout:auto}.is-style-tap-list table td{word-break:normal;overflow-wrap:normal}.is-style-tap-list table td:nth-child(2){white-space:nowrap;font-family:var(--wp--preset--font-family--display);font-weight:700;font-size:var(--wp--preset--font-size--large);text-transform:uppercase;letter-spacing:.02em;line-height:1.05}'
       '.is-style-tap-list table td:last-child,.is-style-tap-list table th:last-child,.is-style-tap-list table td:nth-last-child(2),.is-style-tap-list table th:nth-last-child(2){text-align:right;white-space:nowrap}'
       '.is-style-tap-list table td:last-child{color:var(--wp--preset--color--accent);font-weight:700}'
       '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:.3em}'
       ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:2px}'
       '@media (max-width:700px){.is-style-tap-list table th:nth-child(1),.is-style-tap-list table td:nth-child(1),.is-style-tap-list table th:nth-child(3),.is-style-tap-list table td:nth-child(3),.is-style-tap-list table th:nth-child(4),.is-style-tap-list table td:nth-child(4),.is-style-tap-list table th:nth-child(6),.is-style-tap-list table td:nth-child(6){display:none}.is-style-tap-list table td:nth-child(2){font-size:var(--wp--preset--font-size--medium)}}'
       '.is-style-tap-row{display:grid;grid-template-columns:1.5rem minmax(9rem,1.1fr) 1.7fr 3.5rem 7rem;gap:.2rem 1rem;align-items:baseline;border-bottom:1px solid var(--wp--preset--color--line);padding:.6em 0}'
       '.is-style-tap-row>*{margin:0!important}.is-style-tap-row .tap-name{font-size:var(--wp--preset--font-size--large);text-transform:uppercase;letter-spacing:.02em;line-height:1.05}'
       '.is-style-tap-row .tap-no,.is-style-tap-row .tap-style{font-size:var(--wp--preset--font-size--small)}.is-style-tap-row .tap-price{text-align:right;font-size:var(--wp--preset--font-size--small)}'
       '.is-style-tap-row .tap-price strong{color:var(--wp--preset--color--accent);font-size:var(--wp--preset--font-size--medium)}'
       '.is-style-tap-head{border-bottom:2px solid var(--wp--preset--color--contrast);font-weight:700;font-size:var(--wp--preset--font-size--x-small);padding-top:0}.is-style-tap-head .tap-name{font-family:inherit;font-size:inherit;text-transform:none;letter-spacing:0}'
       '@media (max-width:700px){.is-style-tap-row{grid-template-columns:1fr auto}.is-style-tap-row .tap-no{display:none}.is-style-tap-row .tap-name,.is-style-tap-row .tap-style,.is-style-tap-row .tap-abv{grid-column:1}.is-style-tap-row .tap-price{grid-column:2;grid-row:1 / span 3}.is-style-tap-head{display:none}}'
       '.is-style-rule-row{border-bottom:1px solid var(--wp--preset--color--line);padding:.5em 0}.is-style-rule-row>*{margin:0!important}'
       '@media print{header,footer,.wp-block-buttons,.wp-block-image{display:none!important}body{background:#fff}}')

theme = {
  '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
  'settings': {
    'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
    'layout': {'contentSize': '760px', 'wideSize': '1240px'},
    'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
              'palette': palette('#D9C3A0', '#1A1A1A', '#B3241A', '#FFFFFF', '#1A1A1A', '#4A3F31', '#1A1A1A')},
    'typography': {'defaultFontSizes': False, 'fluid': True, 'fontFamilies': fonts, 'fontSizes': [
        fs('x-small', '0.875rem', 'Small print'), fs('small', '1rem', 'Small'), fs('medium', '1.125rem', 'Body'),
        fs('large', '1.625rem', 'Beer name', '1.35rem'), fs('x-large', '2.75rem', 'Section', '2rem'),
        fs('xx-large', '4.5rem', 'Title', '3rem'), fs('display', '8rem', 'Display', '3.75rem')]},
    'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
        {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
        {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2.2vw, 1.75rem)', 'name': '4'},
        {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.25rem, 5.5vw, 4rem)', 'name': '6'},
        {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 8.5rem)', 'name': '8'}]},
    'shadow': {'defaultPresets': False, 'presets': []},
    'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
  },
  'styles': {
    'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55'},
    'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
    'elements': {
      'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
               ':hover': {'color': {'text': 'var:preset|color|accent'}}},
      'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '0.95', 'letterSpacing': '0.01em'}},
      'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
      'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
      'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.05'}},
      'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0'}},
      'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'letterSpacing': '0'}},
      'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'letterSpacing': '0'}},
      'button': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|surface'},
                 'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                 'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                 'spacing': {'padding': {'top': '0.7em', 'bottom': '0.7em', 'left': '1.2em', 'right': '1.2em'}},
                 ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|surface'}, 'border': {'color': 'var:preset|color|accent'}},
                 ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '2px', 'style': 'solid', 'width': '3px'}}},
      'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
    },
    'blocks': {
      'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|x-large', 'textTransform': 'uppercase', 'lineHeight': '1'},
                          'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
      'core/navigation': {'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                          'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
      'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
      'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}, 'color': {'text': 'var:preset|color|accent'}},
      'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
      'core/image': {'border': {'radius': '0'}},
      'core/post-featured-image': {'border': {'radius': '0'}},
      'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '2px 0 0 0'}},
      'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontFamily': 'var:preset|font-family|display', 'lineHeight': '1.15'},
                     'border': {'left': {'color': 'var:preset|color|accent', 'width': '4px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                     'css': '& cite{display:block;font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--small);font-style:normal;margin-top:.5em}'},
      'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
                       'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}, 'css': '& summary{font-weight:700;cursor:pointer}'},
      'core/search': {'css': '& .wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0;background:var(--wp--preset--color--surface)}'},
    },
    'css': CSS,
  },
  'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                    {'area': 'uncategorized', 'name': 'notice', 'title': 'Bank holiday notice'}],
  'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
                      {'name': 'single-beer', 'title': 'Beer (paper label)', 'postTypes': ['post']}],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Taproom
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A plain paper-label theme for small breweries with a taproom, a changing tap list, cans to go and events.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: taproom
Tags: e-commerce, food-and-drink, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks
*/''')

def variation(title, pal):
    return json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal}}}, indent='\t')
write('styles/cask.json', variation('Cask', palette('#F5F1E8', '#1A1A1A', '#B3241A', '#FFFFFF', '#1A1A1A', '#4E473C', '#1A1A1A')))
write('styles/stout.json', variation('Stout', palette('#1A1A1A', '#EFE6D6', '#FF6B57', '#2A2724', '#EFE6D6', '#C2B8A6', '#0E0E0E')))
write('styles/hop.json', variation('Hop', palette('#DDE8C3', '#141414', '#9E1F14', '#FFFFFF', '#141414', '#3F4633', '#141414')))

def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t', ensure_ascii=False))

section('label', 'Paper label (white, ruled)', ['core/group', 'core/column'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast', 'radius': '0'},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
    'css': '&{outline:1px solid var(--wp--preset--color--contrast);outline-offset:-10px}'})
section('tap-list', 'Tap list (stock sheet)', ['core/table'], {'typography': {'fontSize': 'var:preset|font-size|medium'}})
section('stamp', 'Red stamp', ['core/paragraph'], {
    'color': {'text': 'var:preset|color|accent'},
    'border': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|accent', 'radius': '0'},
    'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
    'spacing': {'padding': {'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
    'css': '&{display:inline-block;transform:rotate(-2deg)}'})
section('dark', 'Stout (black band)', ['core/group'], {
    'color': {'background': 'var:preset|color|dark', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                 'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|dark'}, 'border': {'color': 'var:preset|color|base'}}}})
section('ruled', 'Ruled above', ['core/group', 'core/columns'], {
    'border': {'top': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('tap-row', 'Tap list row', ['core/group'], {})
section('tap-head', 'Tap list header row', ['core/group'], {})
section('rule-row', 'Ruled row (label and value)', ['core/group'], {})
section('dated-list', 'Dated list', ['core/post-template'], {
    'css': '&>li{border-top:2px solid var(--wp--preset--color--contrast);padding-top:var(--wp--preset--spacing--20);margin:0!important}'})

PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}
def sect(inner, **a):
    return group(inner, align='wide', layout={'type': 'default'}, style=PAD, **a)
def hid(text, anchor, level=2, **a):
    return heading(text, level, **a).replace('<h%d class="' % level, '<h%d id="%s" class="' % (level, anchor), 1)
def stamp(t):
    return para(t, className='is-style-stamp')

# ------------------------------------------------------------------ parts
write('parts/header.html', group(J(
    row(J(dyn('site-title', level=0), dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'})),
        justify='space-between', align='wide')),
    tag='header', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                                       'border': {'bottom': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'}}}))

write('parts/footer.html', group(J(
    columns((None, J(heading('Cooperage Brewing', 3), para('Unit 3, Red Cow Lane, Smithfield, Dublin 7. Brewed here since 2017 by Aoife Brennan and Tadhg Moran.'))),
            (None, J(heading('Taproom hours', 6), para('Wednesday and Thursday 16:00 to 23:00<br>Friday 14:00 to 00:00<br>Saturday 12:00 to 00:00<br>Sunday 12:00 to 21:00'))),
            (None, J(heading('Questions', 6), para('<a href="mailto:taproom@example.com">taproom@example.com</a><br>01 555 0147, Wednesday to Sunday<br><a href="/tours/">Brewery tours</a><br><a href="/trade/">Trade and wholesale</a>'))),
            align='wide'),
    para('Over 18s only at the bar. Under 18s welcome with an adult until 19:00. Please drink responsibly: <a href="https://www.drinkaware.ie/">drinkaware.ie</a>.', align='wide', fontSize='small'),
    para('Photos are CC0 stand-ins from Wikimedia Commons. Labels and merch drawings were made for this theme.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-dark',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}}}))

write('parts/notice.html', pattern_ref('bank-holiday-notice'))

# ------------------------------------------------------------------ templates
MAIN = {'style': {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}}

write('templates/front-page.html', page_template(J(
    pattern_ref('on-tap-now'), pattern_ref('hours-and-bookings'), pattern_ref('kitchen-residency'),
    pattern_ref('next-release'), pattern_ref('events-list'), pattern_ref('cans-to-go'), pattern_ref('merch-strip'), pattern_ref('beer-club')), **MAIN))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), **MAIN))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large', align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})), **MAIN))

write('templates/single.html', page_template(J(
    group(J(dyn('post-terms', term='category'), dyn('post-date')), layout={'type': 'flex', 'flexWrap': 'wrap'}),
    dyn('post-title', level=1, fontSize='xx-large'),
    dyn('post-featured-image', aspectRatio='3/2', scale='cover'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)), justify='space-between'),
          className='is-style-ruled', layout={'type': 'default'})), **MAIN))

write('templates/single-beer.html', page_template(J(
    columns(('45%', dyn('post-featured-image', aspectRatio='1', scale='cover')),
            ('55%', group(J(dyn('post-terms', term='category'),
                            dyn('post-title', level=1, fontSize='xx-large', style={'typography': {'textTransform': 'uppercase'}}),
                            dyn('post-content', layout={'type': 'default'}),
                            para('<a href="/taproom/">Is it on tap today?</a> <a href="/shop/">Cans to go</a>')),
                      className='is-style-label', layout={'type': 'default'})),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Previous beer', showTitle=True, taxonomy='category'), dyn('post-navigation-link', label='Next beer', showTitle=True, taxonomy='category')), justify='space-between'),
          align='wide', className='is-style-ruled', layout={'type': 'default'})), **MAIN))

LIST_ITEM = group(J(dyn('post-title', isLink=True, level=3), dyn('post-terms', term='category')),
                  layout={'type': 'flex', 'flexWrap': 'wrap', 'verticalAlignment': 'center', 'justifyContent': 'space-between'})
pattern('post-list', 'Dated list (inherits the page query)', 'taproom-events,query', inherit_query(LIST_ITEM, template_class='is-style-dated-list', align='wide'), inserter=False)
pattern('beer-grid', 'Beer labels grid (inherits the page query)', 'taproom-beers,query', inherit_query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='1', scale='cover'), dyn('post-title', isLink=True, level=3, style={'typography': {'textTransform': 'uppercase'}}), dyn('post-excerpt', excerptLength=14, moreText='')),
    layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}, align='wide'), inserter=False)

write('templates/home.html', page_template(J(heading('Events and news', 1, fontSize='xx-large', align='wide'), pattern_ref('events-page-intro'), pattern_ref('event-types'), pattern_ref('post-list'), pattern_ref('quiz-night')), **MAIN))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'), dyn('term-description', align='wide'), pattern_ref('post-list')), **MAIN))
write('templates/category-beers.html', page_template(J(heading('Our beers', 1, fontSize='xx-large', align='wide'),
    para('The core range is always on in the taproom. Specials come and go; the tap list says what is pouring today.', align='wide'), pattern_ref('beer-grid')), **MAIN))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), **MAIN))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Stout, quiz, Haymarket', buttonText='Search'), pattern_ref('post-list')), **MAIN))
write('templates/404.html', page_template(J(heading('That keg is empty', 1, fontSize='xx-large'),
    para('The page has moved or never existed. Try the <a href="/taproom/">tap list</a>, <a href="/shop/">the shop</a> or a search.'),
    dyn('search', label='Search', showLabel=False, placeholder='Stout, quiz, Haymarket', buttonText='Search')), **MAIN))

# ------------------------------------------------------------------ signature: tap list
TAPS = [
    ('1', 'Haymarket', 'Pale ale', 'Citra, Mosaic', '4.6%', '€3.60', '€6.80'),
    ('2', 'Stoneybatter', 'Table beer', 'Saaz, Goldings', '2.8%', '€3.00', '€5.60'),
    ('3', 'Arran Quay', 'IPA', 'Nelson Sauvin, Motueka', '6.2%', '€4.20', '€7.80'),
    ('4', 'Phoenix', 'Pilsner', 'Hallertau Mittelfrüh', '4.8%', '€3.60', '€6.80'),
    ('5', 'Bow Street', 'Stout, lactose', 'Fuggles', '5.0%', '€3.60', '€6.80'),
    ('6', 'Luas', 'Session IPA', 'Simcoe, Amarillo', '4.2%', '€3.40', '€6.40'),
    ('7', 'Red Cow', 'Raspberry sour', 'none', '4.2%', '€3.80', '€7.20'),
    ('8', 'Four Courts', 'Imperial stout, rum barrel', 'Magnum', '10.5%', '€4.50 a third', 'n/a'),
]
def tap_row(no, name, style, hops, abv, half, pint, cls='is-style-tap-row'):
    price = '%s half<br><strong>%s</strong> pint' % (half, pint) if pint != 'n/a' else '<strong>%s</strong>' % half
    return group(J(para(no, className='tap-no'), heading(name, 3, className='tap-name'), para('%s<br>%s' % (style, hops), className='tap-style'),
                   para(abv, className='tap-abv'), para(price, className='tap-price')), className=cls, layout={'type': 'default'})
TAP_ROWS = J(group(J(para('No.', className='tap-no'), para('Beer', className='tap-name'), para('Style and hops', className='tap-style'), para('ABV', className='tap-abv'), para('Price', className='tap-price')),
                   className='is-style-tap-row is-style-tap-head', layout={'type': 'default'}),
             *[tap_row(*t) for t in TAPS])
TAP_TABLE = table([list(t) for t in TAPS], head=['Line', 'Beer', 'Style', 'Hops', 'ABV', 'Half', 'Pint'], className='is-style-tap-list')
pattern('tap-list', 'Tap list (stock sheet)', 'taproom-taproom', group(J(
    row(J(heading('On tap now', 2), stamp('Draught menu updated Friday 25 September, 16:40')), justify='space-between'),
    TAP_ROWS,
    para('Allergens: every beer contains barley and wheat (gluten). Bow Street contains lactose. All others are vegan. Ask for a taster before you order.', fontSize='x-small')),
    className='is-style-label', layout={'type': 'default'}),
    description='Edit the rows when lines change and the date in the stamp. Print this page for the bar wall.')

pattern('on-tap-now', 'Home: on tap now with the room', 'featured,taproom-taproom', group(J(
    pattern_ref('tap-list'),
    columns(('45%', J(heading('Cooperage Brewing', 1, fontSize='display'),
                      para('A small brewery with a taproom in a Smithfield yard. Eight lines, all ours, poured three metres from where they were brewed.', fontSize='large'),
                      buttons(('Find the taproom', '/taproom/#find-us'), ('Buy cans to go', '/shop/', {'className': 'is-style-outline'})))),
            ('55%', image('hero.jpg', 'A brewery taproom counter with steel fermenters behind it and a painted mural along the wall', 'The counter on a Friday afternoon, before the rush.', lightbox=False)),
            align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}, 'padding': {'top': 'var:preset|spacing|60'}}})),
    align='wide', layout={'type': 'default'}), description='The tap list as the first thing on the page, then the room.')

HOURS = [['Monday and Tuesday', 'Closed, we are brewing'], ['Wednesday and Thursday', '16:00 to 23:00'], ['Friday', '14:00 to 00:00'],
         ['Saturday', '12:00 to 00:00'], ['Sunday', '12:00 to 21:00'], ['Bank holiday Mondays', '12:00 to 21:00']]
pattern('opening-hours', 'Opening hours with bank holidays', 'taproom-taproom', J(heading('Taproom hours', 3),
    *[row(J(para(d), para('<strong>%s</strong>' % t)), justify='space-between', className='is-style-rule-row') for d, t in HOURS]))

pattern('booking-rules', 'Booking rules', 'taproom-taproom', J(
    heading('Bookings', 3),
    lst(['Walk-ins for groups up to five. We keep most tables free.',
         'Six or more: book with the form below, at least two days ahead.',
         'The back room holds 20 to 30 people, Saturdays only, €150 deposit taken off the bar bill.',
         'Tables are held for 15 minutes after the booking time.']),
    buttons(('Book a table', '/book-a-table/'))))

pattern('hours-and-bookings', 'Hours and bookings panel', 'taproom-taproom', sect(columns(
    (None, pattern_ref('opening-hours')), (None, pattern_ref('booking-rules')),
    (None, J(heading('Age', 3), para('Over 18s only at the bar, with ID if you look under 25. Under 18s are welcome with an adult until 19:00, and dogs all day.'))),
    align='wide', className='is-style-ruled')))

pattern('kitchen-residency', 'Kitchen residency card', 'taproom-taproom', sect(columns(
    ('40%', image('food.jpg', 'Two paper-lined baskets of soft tacos with salsa pots on a tray', lightbox=False)),
    ('60%', group(J(heading('In the kitchen: Masa Loca', 2),
                    para('Tacos from Inés Ortega, Thursday to Sunday until October. Blue corn tortillas pressed in the yard, three for €12, and a mushroom al pastor that goes well with Bow Street.'),
                    para('Kitchen closes an hour before the bar. You are welcome to bring your own food on Wednesdays.', fontSize='small')),
                  className='is-style-label', layout={'type': 'default'})),
    align='wide', verticalAlignment='center')))

pattern('events-list', 'Events list (latest posts)', 'taproom-events,query', sect(J(
    row(J(heading('Coming up', 2), para('<a href="/events/">All events and news</a>')), justify='space-between'),
    query(LIST_ITEM, per_page=5, template_class='is-style-dated-list'))))

def can_tile(img, name, style, price, alt):
    return stack(J(image(img, alt), heading('<a href="/shop/">%s</a>' % name, 3, style={'typography': {'textTransform': 'uppercase'}}),
                   para('%s<br><strong>%s</strong>' % (style, price), fontSize='small')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}})

pattern('cans-to-go', 'Cans to go', 'taproom-shop', sect(J(
    row(J(heading('Cans to go', 2), para('Order online and collect at the bar, or we deliver in Dublin 1 to 8 on Fridays for €5.')), justify='space-between'),
    grid(J(can_tile('label-haymarket.jpg', 'Haymarket', 'Pale ale, 4.6%', '€4.20', 'Paper can label for Haymarket pale ale, 4.6%, with a red batch stamp'),
           can_tile('label-arran-quay.jpg', 'Arran Quay', 'IPA, 6.2%', '€5.00', 'Paper can label for Arran Quay IPA, 6.2%'),
           can_tile('label-bow-street.jpg', 'Bow Street', 'Stout, 5.0%', '€4.40', 'Paper can label for Bow Street stout, 5.0%'),
           can_tile('label-four-courts.jpg', 'Four Courts', 'Imperial stout, 10.5%', '€9.00', 'Paper can label for Four Courts imperial stout, 10.5%')), min_width='13rem'),
    buttons(('See every can and the merch', '/shop/')))))

pattern('beer-club', 'Beer club subscription', 'taproom-shop', group(group(J(
    heading('The beer club', 2),
    para('Twelve cans a month: two new beers before anyone else gets them, plus whatever Tadhg is proud of that month. €48, collected or delivered anywhere in Ireland.'),
    lst(['Collect from the bar on the first Friday, or delivery for €8', 'Skip a month by email, no questions', 'Members get 10% off at the bar']),
    buttons(('Join the beer club', '/beer-club/'))), layout={'type': 'constrained', 'contentSize': '1240px'}),
    align='full', className='is-style-dark', layout={'type': 'constrained', 'contentSize': '760px', 'wideSize': '1240px'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('find-us', 'Find the taproom', 'taproom-taproom', columns(
    (None, J(hid('Find us', 'find-us', 2), para('Unit 3, Red Cow Lane, Smithfield, Dublin 7. Through the green gate by the bike shop; follow the smell of mash on brew days.'),
             para('Luas Red Line to Smithfield, then three minutes on foot. Bike racks in the yard. No parking, sorry.'))),
    (None, J(heading('Accessibility', 3), para('Step-free from the gate to the bar and the toilet. The back room is up one step; we have a ramp, ask at the bar.'))),
    align='wide'))

pattern('taproom-page', 'Page: taproom', 'taproom-taproom', J(
    pattern_ref('tap-list'), pattern_ref('guest-beer'), pattern_ref('in-the-tanks'), pattern_ref('hours-and-bookings'), pattern_ref('kitchen-residency'), pattern_ref('kitchen-menu'),
    pattern_ref('find-us'), pattern_ref('house-rules'), pattern_ref('taproom-faq'), pattern_ref('allergen-key'), pattern_ref('print-tap-list')), block_types='core/post-content')

pattern('print-tap-list', 'Print the tap list', 'taproom-taproom', para(
    'Behind the bar: print this page on A4 and pin it up. The print version drops the header, photos and buttons and keeps the list and the date.', fontSize='small'))

pattern('bank-holiday-notice', 'Bank holiday notice', 'banner', group(
    para('<strong>Bank holiday Monday 26 October:</strong> open 12:00 to 21:00, kitchen until 20:00.', style={'typography': {'textAlign': 'center'}}),
    align='full', className='is-style-label', layout={'type': 'constrained'}))

pattern('age-note', 'Age note (no pop-up)', 'taproom-shop', para(
    'You must be 18 or over to buy beer from us. We check ID on delivery and at collection. We do not ask for your date of birth on the way in; we ask at the door.', fontSize='small'))

pattern('booking-page', 'Page: book a table', 'taproom-taproom', J(
    pattern_ref('booking-rules'),
    pattern_ref('private-hire'),
    group(J(heading('Book by email', 3), para('Send the date, the time, how many of you and a phone number. We confirm within a day.'),
            buttons(('Email a booking', 'mailto:taproom@example.com?subject=Table%20booking'))), className='is-style-label', layout={'type': 'default'}),
    pattern_ref('opening-hours')), block_types='core/post-content')

pattern('core-range', 'Core range grid', 'taproom-beers', sect(J(
    heading('Always on', 2),
    columns((None, J(image('label-haymarket.jpg', 'Paper label for Haymarket pale ale', lightbox=False), para('<strong>HAYMARKET</strong>, pale ale, 4.6%. The one most people start with.'))),
            (None, J(image('label-phoenix.jpg', 'Paper label for Phoenix pilsner', lightbox=False), para('<strong>PHOENIX</strong>, pilsner, 4.8%. Lagered for six weeks, which is why it runs out.'))),
            (None, J(image('label-bow-street.jpg', 'Paper label for Bow Street stout', lightbox=False), para('<strong>BOW STREET</strong>, stout, 5.0%. Lactose makes it rounder; not vegan.'))),
            (None, J(image('label-stoneybatter.jpg', 'Paper label for Stoneybatter table beer', lightbox=False), para('<strong>STONEYBATTER</strong>, table beer, 2.8%. For the second half of a long afternoon.'))),
            align='wide'))))

pattern('beer-club-page', 'Page: beer club', 'taproom-shop', J(
    para('Twelve cans a month, picked by the brewers. Cancel or skip whenever you like.', fontSize='large'),
    table([['What', '12 cans, at least two unreleased'], ['Price', '€48 a month'], ['Delivery', 'Collect free on the first Friday, or €8 anywhere in Ireland'],
           ['Skipping', 'Email us before the 25th'], ['Bar discount', '10% for members']]),
    buttons(('Join from the shop', '/shop/')), pattern_ref('gift-membership'), pattern_ref('collect-delivery'), pattern_ref('newsletter-release'), pattern_ref('age-note')), block_types='core/post-content')

pattern('trade-enquiry', 'Trade enquiry', 'taproom-shop', J(
    para('We supply about thirty pubs and off-licences in Dublin, Cork and Galway with kegs and cans.', fontSize='large'),
    table([['Kegs', '30 litre KeyKeg and 50 litre steel', 'Weekly delivery in Dublin'], ['Cans', 'Cases of 24', 'Pallet or mixed case'], ['Minimum', 'Two kegs or four cases', 'Free delivery over that']],
          head=['Format', 'Sizes', 'Delivery']),
    para('Write to Tadhg at <a href="mailto:trade@example.com">trade@example.com</a> with your venue and how many lines you have. We do not do exclusives.'),
    pattern_ref('keg-returns'), pattern_ref('stockists')), block_types='core/post-content')

pattern('events-page-intro', 'Events intro', 'taproom-events', para(
    'Quiz on the first Wednesday, tap takeovers and launches most months, a tasting with the brewers every other Sunday. Free unless it says otherwise.', fontSize='large'))

pattern('beer-spec', 'Beer spec table (for a beer post)', 'taproom-beers', table(
    [['Style', 'Pale ale'], ['ABV', '4.6%'], ['Hops', 'Citra, Mosaic'], ['Malt', 'Irish pale, oats, a little wheat'], ['Formats', 'Keg, 440 ml can'], ['Allergens', 'Barley, wheat, oats (gluten). Vegan.']]))

pattern('about-brewery', 'About the brewery', 'taproom-about', sect(columns(
    ('58%', J(para('Aoife Brennan and Tadhg Moran started Cooperage in 2017 in a unit that used to make barrels for the Jameson distillery down the road.', fontSize='large'),
              para('We brew twice a week on a ten-barrel kit, can on Thursdays and open the taproom from Wednesday. Everything on the bar is ours; we pour one guest beer a month, from a brewery we like.'),
              para('We do not make beer with sweets or cereal in it. Ask Tadhg why if you have twenty minutes.'),
              pattern_ref('quote-regular'))),
    ('42%', image('canning.jpg', 'A small canning line with filling heads and a row of empty cans moving along it', 'Thursday is canning day.')),
    align='wide')))

pattern('taproom-faq', 'Questions people ask at the bar', 'taproom-taproom', sect(J(
    heading('Questions people ask', 2),
    details('Can I bring my dog?', para('Yes, inside and out. Water bowl by the door.')),
    details('Do you take cash?', para('Card only at the bar. The taco hatch takes both.')),
    details('Can I get a taster first?', para('Always. Up to two, free, before you order.')),
    details('Do you fill growlers?', para('Yes, 1 litre or 2 litres, from any line except Four Courts. Bring it clean.')),
    details('Is there food on Wednesdays?', para('No kitchen on Wednesdays. Bring your own, or order in; we have plates.')))))

pattern('collect-delivery', 'Click and collect, delivery', 'taproom-shop', table(
    [['Collect at the bar', 'Free', 'Ready in two hours during taproom hours'], ['Dublin 1 to 8', '€5', 'Fridays, 12:00 to 18:00'],
     ['Rest of Ireland', '€8', '2 to 3 working days, ID checked on delivery']], head=['How', 'Cost', 'When'],
    caption='Delivery costs are shown before checkout. We do not ship outside Ireland.'))

pattern('quote-regular', 'Quote from a regular', 'taproom-about', quote(
    'I came for the quiz in 2019 and never really left. Bow Street on nitro on a Sunday is the best pint in Dublin 7.',
    'Ciarán Doyle, Stoneybatter, quiz team captain'))

pattern('guest-beer', 'Guest beer of the month', 'taproom-beers', group(J(
    heading('Guest line, October', 3),
    para('One guest beer a month on line 8, from a brewery we would drink at. This month: a smoked porter from Hazel Row in Wexford, 5.4%.')),
    className='is-style-label', layout={'type': 'default'}))


# ------------------------------------------------------------------ round 2: more of the kit, from real brewery sites
pattern('printable-tap-sheet', 'Printable tap sheet (A4, table)', 'taproom-taproom', group(J(
    row(J(heading('Cooperage Brewing, on tap', 3), stamp('Updated Friday 25 September, 16:40')), justify='space-between'),
    TAP_TABLE), className='is-style-label', layout={'type': 'default'}),
    description='The same list as a plain table, for printing on A4 and pinning behind the bar.')

TANKS = [('FV1', 'Phoenix pilsner', 'Lagering, day 23 of 42', 'On tap mid-October'),
         ('FV2', 'Red Cow raspberry sour', 'Conditioning on fruit', 'Launches Friday 2 October'),
         ('FV3', 'Haymarket pale ale', 'Fermenting, day 4', 'Canning Thursday 8 October'),
         ('FV4', 'Fresh hop pale, Kilkenny hops', 'Dry hopping', 'On tap 10 October')]
pattern('in-the-tanks', 'In the tanks this week', 'taproom-beers', sect(J(
    heading('In the tanks', 2),
    para('What Tadhg has brewing right now, so you know what is coming to the bar.'),
    grid(J(*[group(J(para('<strong>%s</strong>' % t, fontSize='small'), heading(b, 3), para(st, fontSize='small'), para(w, fontSize='small', textColor='accent')),
                   className='is-style-label', layout={'type': 'default'}) for t, b, st, w in TANKS]), min_width='14rem'))))

pattern('next-release', 'Next can release', 'featured,taproom-shop', sect(columns(
    ('40%', image('cans.jpg', 'A wall of red and black beer cans stacked on shelves', 'The can store on a canning Thursday.')),
    ('60%', J(heading('Next release: Red Cow raspberry sour', 2),
              para('Friday 2 October, 17:00, on line 7 and in cans at the bar. Online the same evening at 20:00.', fontSize='large'),
              para('Four cans a person until Sunday. €4.80 a can. Contains barley and wheat; vegan.'),
              buttons(('Buy cans online', '/shop/'), ('See the tap list', '/taproom/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='center')))

KITCHEN = [('Three tacos, mushroom al pastor', '€12'), ('Three tacos, beef barbacoa', '€13'), ('Quesadilla, Oaxaca cheese and chorizo', '€9'),
           ('Totopos with salsa verde', '€5'), ('Elote, grilled corn with lime', '€5')]
pattern('kitchen-menu', 'Kitchen menu (Masa Loca)', 'taproom-taproom', group(J(
    heading('Masa Loca menu', 3),
    *[row(J(para(n), para('<strong>%s</strong>' % pr)), justify='space-between', className='is-style-rule-row') for n, pr in KITCHEN],
    para('Gluten-free tortillas on request. Tell Inés about allergies before you order.', fontSize='small')),
    className='is-style-label', layout={'type': 'default'}))

pattern('house-rules', 'House rules', 'taproom-taproom', sect(columns(
    (None, J(heading('Dogs', 4), para('Welcome inside and out. Water bowl by the door, biscuits at the bar.'))),
    (None, J(heading('Children', 4), para('With an adult until 19:00. There is a box of board games under the stairs.'))),
    (None, J(heading('Payment', 4), para('Card only at the bar. The taco hatch takes cash too.'))),
    (None, J(heading('Last orders', 4), para('Thirty minutes before closing. We ring the bell twice.'))),
    align='wide', className='is-style-ruled')))

pattern('event-types', 'What happens at the taproom', 'taproom-events', sect(columns(
    (None, J(heading('Quiz', 3), para('First Wednesday of the month, 20:00. Teams of up to six, €2 each.'))),
    (None, J(heading('Launches', 3), para('New beers go on at 17:00 on a Friday, with cans at the bar the same hour.'))),
    (None, J(heading('Tastings', 3), para('Every other Sunday at 14:00 with a brewer. Six thirds, €22, twelve places.'))),
    (None, J(heading('Takeovers', 3), para('One Friday a month, four lines go to a brewery we like.'))),
    align='wide', className='is-style-ruled')))

pattern('quiz-night', 'Quiz night card', 'taproom-events', group(J(
    heading('Pub quiz with Síle', 2),
    para('First Wednesday of every month, 20:00. Teams of up to six, €2 a head, cash prize and a €50 bar tab for the winners. Picture round, music round, no phones.'),
    buttons(('Book a table for the quiz', '/book-a-table/'))),
    className='is-style-label', layout={'type': 'default'}))

pattern('brewery-tours', 'Brewery tours', 'taproom-events', sect(columns(
    ('55%', J(heading('Brewery tours', 2),
              para('Saturdays at 13:00, about 45 minutes. Tadhg walks you through the brewhouse, the tanks and the canning line, then four thirds at the bar.'),
              lst(['€18 a person, over 18s only', 'Twelve places, book by email', 'Closed-toe shoes, please; the floor is wet']),
              buttons(('Email to book a tour', 'mailto:taproom@example.com?subject=Brewery%20tour')))),
    ('45%', image('hero.jpg', 'Steel fermenters and a conical tank beside the taproom counter', 'The tanks you will walk past on the tour.')),
    align='wide', verticalAlignment='center')))

TEAM = [('Aoife Brennan', 'Brewer and co-owner. Writes the recipes and the tap list.'), ('Tadhg Moran', 'Head brewer and co-owner. Runs the brewhouse and the tours.'),
        ('Síle Nic Aodha', 'Bar manager. Quiz master. Keeps the lines clean.'), ('Inés Ortega', 'Masa Loca, in the kitchen Thursday to Sunday.')]
pattern('brewery-team', 'The people behind the bar', 'taproom-about', sect(J(
    heading('Who you will meet', 2),
    grid(J(*[group(J(heading(n, 3), para(r, fontSize='small')), className='is-style-ruled', layout={'type': 'default'}) for n, r in TEAM]), min_width='14rem'))))

pattern('collaborations', 'Beers brewed with friends', 'taproom-beers', sect(J(
    heading('Brewed with friends', 2),
    lst(['<strong>Hazel Row, Wexford</strong>: a smoked porter, October 2026', '<strong>Rye River apprentices</strong>: a table beer for their graduation, 2025',
         '<strong>The Bernard Shaw</strong>: a house lager for their tenth birthday, 2024']))))

pattern('spent-grain', 'Where the spent grain goes', 'taproom-about', group(J(
    heading('Spent grain and returns', 3),
    para('Every brew leaves about 400 kg of wet grain. A farmer from Ratoath collects it on Tuesdays for his cattle. Bring your cans back for recycling and your 1 litre growler for a €1 refill discount.')),
    className='is-style-label', layout={'type': 'default'}))

pattern('jobs', 'We are hiring', 'taproom-about', group(J(
    heading('Bar staff, part-time', 3),
    para('Thursday to Saturday evenings, €15.50 an hour plus tips. You like talking about beer and you do not mind a quiz. Email Síle with two lines about yourself.'),
    buttons(('Email Síle', 'mailto:taproom@example.com?subject=Bar%20job'))),
    className='is-style-ruled', layout={'type': 'default'}), description='Delete when the job is filled.')

pattern('private-hire', 'Private hire: the back room', 'taproom-taproom', sect(columns(
    ('55%', J(heading('Hire the back room', 2),
              para('Saturdays only, 20 to 30 people, from 13:00 or 19:00 for four hours. €150 deposit, taken off the bar bill on the night. Tacos for the group from Masa Loca at €10 a head.'),
              buttons(('Ask about a date', 'mailto:taproom@example.com?subject=Back%20room')))),
    ('45%', image('bar.jpg', 'A long wooden bar with brass fittings and taps along the counter', 'Not our back room, but the same idea.')),
    align='wide', verticalAlignment='center')))

pattern('gift-membership', 'Beer club as a gift', 'taproom-shop', group(J(
    heading('Give three months of the beer club', 3),
    para('€144 for three boxes, with a printed card in the first one. The person you give it to picks collection or delivery.'),
    buttons(('Email to order a gift', 'mailto:taproom@example.com?subject=Beer%20club%20gift'))),
    className='is-style-label', layout={'type': 'default'}))

STOCK = [('Dublin 7', 'Blackrock Off-licence, Manor Street', 'Cans'), ('Dublin 8', 'The Liberty Bottle Shop, Thomas Street', 'Cans and kegs'),
         ('Cork', 'Bradley\'s, North Main Street', 'Cans'), ('Galway', 'Salthill Wine and Beer', 'Cans')]
pattern('stockists', 'Where to buy our cans', 'taproom-shop', sect(J(
    heading('Where else to buy them', 2),
    *[row(J(para('<strong>%s</strong>' % a), para(b), para(c, fontSize='small')), justify='space-between', className='is-style-rule-row') for a, b, c in STOCK],
    para('Call ahead; stock moves fast on a Friday.', fontSize='small'))))

pattern('keg-returns', 'Keg returns for trade', 'taproom-shop', group(J(
    heading('Keg returns', 3),
    para('Steel kegs carry a €40 deposit, refunded when we collect them on the next delivery. KeyKegs are recyclable; we take them back free.')),
    className='is-style-ruled', layout={'type': 'default'}))

pattern('merch-strip', 'Merch strip', 'taproom-shop', sect(J(
    row(J(heading('Glass, bag, shirt', 2), para('<a href="/shop/">All merch in the shop</a>')), justify='space-between'),
    grid(J(stack(J(image('merch-glass.jpg', 'Drawing of a straight-sided pint glass with the Cooperage label printed on it'), para('Pint glass, 568 ml, <strong>€8</strong>'))),
           stack(J(image('merch-tote.jpg', 'Drawing of an unbleached cotton tote bag with the Cooperage label'), para('Tote bag, holds twelve cans, <strong>€12</strong>'))),
           stack(J(image('merch-tee.jpg', 'Drawing of a black T-shirt with a white Cooperage label on the chest'), para('T-shirt, black, S to XXL, <strong>€25</strong>')))), min_width='14rem'))))

pattern('newsletter-release', 'Release emails', 'taproom-shop', group(J(
    heading('One email per release', 3),
    para('A short email when a new beer goes on and when cans go online. About two a month.'),
    buttons(('Get release emails', 'mailto:taproom@example.com?subject=Release%20emails'))),
    className='is-style-label', layout={'type': 'default'}))

pattern('allergen-key', 'Allergen key', 'taproom-beers', group(J(
    heading('Allergens', 4),
    lst(['Every beer contains barley (gluten). Most contain wheat or oats too.', 'Bow Street contains lactose (milk).', 'Red Cow contains raspberries.', 'All others are vegan. Finings are not used.']),
    ), layout={'type': 'default'}))

pattern('about-page', 'Page: about', 'taproom-about', J(pattern_ref('about-brewery'), pattern_ref('brewery-team'), pattern_ref('collaborations'), pattern_ref('spent-grain'), pattern_ref('jobs')), block_types='core/post-content')
pattern('tours-page', 'Page: tours and events', 'taproom-events', J(pattern_ref('brewery-tours'), pattern_ref('event-types'), pattern_ref('quiz-night'), pattern_ref('printable-tap-sheet')), block_types='core/post-content')

print('taproom: patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

write('functions.php', '''<?php
/**
 * Taproom: pattern categories only.
 *
 * @package taproom
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'taproom-taproom' => 'Taproom: tap list and visiting',
			'taproom-beers'   => 'Taproom: beers',
			'taproom-events'  => 'Taproom: events',
			'taproom-shop'    => 'Taproom: shop and beer club',
			'taproom-about'   => 'Taproom: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);''')

# ------------------------------------------------------------------ demo content
def beer_post(style, abv, hops, malt, note, allergens, formats):
    return J(para(note), table([['Style', style], ['ABV', abv], ['Hops', hops], ['Malt', malt], ['Formats', formats], ['Allergens', allergens]]))

BEER_POSTS = [
  ('Haymarket', 'label-haymarket.jpg', '2026-03-02', beer_post('Pale ale', '4.6%', 'Citra, Mosaic', 'Irish pale, oats, wheat', 'Our first beer and still the one we sell most of. Soft, orangey, dry at the end.', 'Barley, wheat, oats (gluten). Vegan.', 'Keg, 440 ml can')),
  ('Arran Quay', 'label-arran-quay.jpg', '2026-02-20', beer_post('IPA', '6.2%', 'Nelson Sauvin, Motueka', 'Irish pale, wheat', 'White grape and lime from the Nelson. Brewed every six weeks, gone in four.', 'Barley, wheat (gluten). Vegan.', 'Keg, 440 ml can')),
  ('Bow Street', 'label-bow-street.jpg', '2026-02-10', beer_post('Stout', '5.0%', 'Fuggles', 'Pale, roast barley, chocolate malt', 'Roast, cocoa and a little lactose to round it off. On nitro on Sundays.', 'Barley, wheat (gluten), lactose (milk).', 'Keg, nitro, 440 ml can')),
  ('Phoenix', 'label-phoenix.jpg', '2026-01-28', beer_post('Pilsner', '4.8%', 'Hallertau Mittelfrüh', 'Pilsner malt', 'Six weeks of lagering at one degree. Crisp, bready, a little floral.', 'Barley (gluten). Vegan.', 'Keg, 440 ml can')),
  ('Stoneybatter', 'label-stoneybatter.jpg', '2026-01-15', beer_post('Table beer', '2.8%', 'Saaz, East Kent Goldings', 'Pale, oats', 'A light, hoppy beer for the second half of a long afternoon.', 'Barley, oats (gluten). Vegan.', 'Keg, 440 ml can')),
  ('Four Courts', 'label-four-courts.jpg', '2025-12-01', beer_post('Imperial stout, rum barrel', '10.5%', 'Magnum', 'Pale, roast, crystal, oats', 'Eleven months in a Jamaican rum barrel. Poured in thirds only, and only in winter.', 'Barley, oats (gluten). Vegan.', 'Keg (thirds only), 440 ml can')),
]
BEER_NOTES = {'Haymarket': 'Pale ale, 4.6%. The one most people start with.', 'Arran Quay': 'IPA, 6.2%. White grape and lime from the Nelson.',
              'Bow Street': 'Stout, 5.0%. Roast, cocoa and a little lactose.', 'Phoenix': 'Pilsner, 4.8%. Six weeks of lagering.',
              'Stoneybatter': 'Table beer, 2.8%. Light and hoppy.', 'Four Courts': 'Imperial stout, 10.5%. Rum barrel, thirds only.'}
EVENT_POSTS = [
  ('Pub quiz, Wednesday 7 October', 'events', 'bar.jpg', '2026-09-26', J(para('Teams of up to six, €2 each, cash prize and a bar tab for the winners. Starts 20:00; Síle asks the questions and takes no appeals.'), para('Book a table if you are more than five.'))),
  ('Launch: Red Cow raspberry sour, Friday 2 October', 'events', 'cans.jpg', '2026-09-24', J(para('Our first sour in two years goes on line 7 at 17:00, and cans go on sale at the same time. Limit four cans a person until Sunday.'))),
  ('Tasting with the brewers, Sunday 4 October', 'events', 'taps.jpg', '2026-09-22', J(para('Six thirds, one of each core beer and two from the tanks, with Aoife talking you through them. 14:00, €22, twelve places.'), buttons(('Email to book a place', 'mailto:taproom@example.com?subject=Tasting')))),
  ('Tap takeover: Hazel Row from Wexford, Friday 9 October', 'events', 'glass.jpg', '2026-09-18', J(para('Four lines of Hazel Row Brewing on Friday from 16:00. Our own beers stay on the other four.'))),
  ('Canning day, and why the Pilsner runs out', 'news', 'canning.jpg', '2026-09-10', J(para('Phoenix sits in the tank for six weeks before we can it. When it sells faster than that, it runs out. We are adding a tank in November.'))),
  ('Hop harvest brew with fresh Irish hops', 'news', 'hops.jpg', '2026-09-03', J(para('We drove to a farm in Kilkenny on Tuesday morning and had the hops in the kettle by 15:00. The beer is on in three weeks.'))),
]
content = {
  'site': {'title': 'Cooperage Brewing', 'tagline': 'Brewery and taproom in Smithfield, Dublin 7'},
  'categories': [{'slug': 'beers', 'name': 'Beers', 'description': 'The core range and the specials.'},
                 {'slug': 'events', 'name': 'Events', 'description': 'Quiz, tastings, launches and takeovers.'},
                 {'slug': 'news', 'name': 'News', 'description': 'From the brewhouse.'}],
  'front_page': 'home', 'posts_page': 'events',
  'pages': [
    {'slug': 'home', 'title': 'Home', 'content': ''},
    {'slug': 'events', 'title': 'Events and news', 'content': ''},
    {'slug': 'taproom', 'title': 'Taproom', 'pattern': 'taproom/taproom-page', 'template': 'page-wide'},
    {'slug': 'book-a-table', 'title': 'Book a table', 'pattern': 'taproom/booking-page'},
    {'slug': 'beer-club', 'title': 'Beer club', 'pattern': 'taproom/beer-club-page'},
    {'slug': 'trade', 'title': 'Trade', 'pattern': 'taproom/trade-enquiry'},
    {'slug': 'about', 'title': 'About', 'pattern': 'taproom/about-page', 'template': 'page-wide'},
    {'slug': 'tours', 'title': 'Tours and events', 'pattern': 'taproom/tours-page', 'template': 'page-wide'},
  ],
  'posts': [{'title': t, 'category': 'beers', 'image': img, 'date': d, 'content': body, 'template': 'single-beer', 'excerpt': BEER_NOTES[t]} for t, img, d, body in BEER_POSTS] +
           [{'title': t, 'category': c, 'image': img, 'date': d, 'content': body} for t, c, img, d, body in EVENT_POSTS],
  'nav': [{'label': 'On tap', 'url': '/taproom/'}, {'label': 'Beers', 'url': '/category/beers/'}, {'label': 'Events', 'url': '/events/'},
          {'label': 'Shop', 'url': '/shop/'}, {'label': 'Beer club', 'url': '/beer-club/'}, {'label': 'Book a table', 'url': '/book-a-table/'}, {'label': 'About', 'url': '/about/'}],
  'currency': 'EUR',
  'products': [
    {'name': 'Haymarket pale ale, 440 ml can', 'price': '4.20', 'image': 'label-haymarket.jpg', 'category': 'Cans', 'sku': 'CB-HAY', 'stock': 180, 'short': 'Pale ale, 4.6%. Citra and Mosaic. Vegan.', 'description': 'Canned on Thursdays. Best within three months; keep it in the fridge.'},
    {'name': 'Arran Quay IPA, 440 ml can', 'price': '5.00', 'image': 'label-arran-quay.jpg', 'category': 'Cans', 'sku': 'CB-ARQ', 'stock': 64, 'short': 'IPA, 6.2%. Nelson Sauvin and Motueka. Vegan.', 'description': 'Drink it fresh. The hops fade after eight weeks.'},
    {'name': 'Bow Street stout, 440 ml can', 'price': '4.40', 'image': 'label-bow-street.jpg', 'category': 'Cans', 'sku': 'CB-BOW', 'stock': 96, 'short': 'Stout, 5.0%. Contains lactose.', 'description': 'Roast, cocoa and a round finish from lactose. Not vegan.'},
    {'name': 'Phoenix pilsner, 440 ml can', 'price': '4.20', 'image': 'label-phoenix.jpg', 'category': 'Cans', 'sku': 'CB-PHX', 'stock': 0, 'short': 'Pilsner, 4.8%. Sold out; next canning 8 October.', 'description': 'Six weeks lagered. Vegan.'},
    {'name': 'Four Courts imperial stout, 440 ml can', 'price': '9.00', 'image': 'label-four-courts.jpg', 'category': 'Cans', 'sku': 'CB-4CT', 'stock': 40, 'short': 'Rum barrel-aged imperial stout, 10.5%. Two per order.', 'description': 'Eleven months in a Jamaican rum barrel. Keeps for years in a dark cupboard.'},
    {'name': 'Mixed case, 12 cans', 'price': '48', 'image': 'cans.jpg', 'category': 'Cases', 'sku': 'CB-MIX12', 'stock': 30, 'short': 'Three each of four core beers, picked by us.', 'description': 'Collect at the bar or delivery in Dublin 1 to 8 on Fridays for €5.'},
    {'name': 'Pint glass, 568 ml', 'price': '8', 'image': 'merch-glass.jpg', 'category': 'Merch', 'sku': 'CB-GLASS', 'stock': 50, 'short': 'Straight-sided pint glass with the label printed on.', 'description': 'Dishwasher safe, but it lasts longer by hand.'},
    {'name': 'Tote bag', 'price': '12', 'image': 'merch-tote.jpg', 'category': 'Merch', 'sku': 'CB-TOTE', 'stock': 35, 'short': 'Unbleached cotton. Holds twelve cans.', 'description': 'Printed in Dublin 8.'},
    {'name': 'T-shirt, black', 'price': '25', 'image': 'merch-tee.jpg', 'category': 'Merch', 'sku': 'CB-TEE', 'stock': 22, 'short': 'Organic cotton, sizes S to XXL.', 'description': 'Sizes run slightly large. Swap by email within 30 days if it does not fit.'},
  ],
}
os.makedirs('demos/taproom', exist_ok=True)
json.dump(content, open('demos/taproom/content.json', 'w'), indent=1, ensure_ascii=False)
print('taproom: demo content written')
