# cityguide: Lampje, an independent weekly guide to Eindhoven by two locals, with places, events, neighbourhoods and lists.
# Direction: the owner pointed at thisiseindhoven.com: white pages, a heavy black grotesk, red and blue, big pink sections.
#   Lampje keeps that energy and makes it its own with the city's sawtooth factory roofs (Philips' Strijp) as the edge of
#   every coloured section and as the two red teeth of its logotype.
# Fonts: Mona Sans (expanded, 900) for headings, Work Sans for text. Two families, no monospace.
# Palette: white #FFFFFF, ink #111111, signal red #D80028 (pins, buttons), tram blue #1C3FD6 (category labels),
#   rose #F2B8CF for section grounds only.
# Layout idea: a numbered list next to a sticky sketch map whose red pins carry the same numbers, and a weekly
#   "what's on" set as a timetable with day, time, place and price.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('cityguide')
D = THEME['dir']
IMG = '/wp-content/themes/cityguide/assets/images/'

def palette(base, contrast, accent, blue, surface, line, muted, pink):
    p = [('base', base, 'White'), ('contrast', contrast, 'Ink'), ('accent', accent, 'Signal red'), ('accent-2', blue, 'Tram blue'),
         ('surface', surface, 'Pavement'), ('line', line, 'Line'), ('muted', muted, 'Grey'), ('pink', pink, 'Rose')]
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Mona Sans", "Work Sans", Arial, sans-serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"Work Sans", Arial, sans-serif'

def fs(slug, size, name, mn=None):
    return {'slug': slug, 'size': size, 'name': name, 'fluid': {'min': mn, 'max': size} if mn else False}

TEETH = 'linear-gradient(to top right,var(--wp--preset--color--%s) 50%%,transparent 50%%) 0 100%%/56px 28px repeat-x'
CSS = ('body{font-synthesis:none}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
       ':where(h1,h2,h3,h4,.wp-block-site-title){font-stretch:112.5%}'
       '.wp-block-site-title a{display:inline-flex;align-items:center;gap:.35em}'
       '.wp-block-site-title a::before{content:"";width:1.3em;height:.62em;background:linear-gradient(to top right,var(--wp--preset--color--accent) 50%,transparent 50%) 0 100%/.65em .62em repeat-x}'
       '.wp-block-table table td,.wp-block-table table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.7em 1em .7em 0;text-align:left;vertical-align:top}'
       '.wp-block-table table thead{border-bottom:0}.wp-block-table table th{font-weight:600;border-bottom:3px solid var(--wp--preset--color--contrast)}'
       '.wp-block-table table td{font-variant-numeric:tabular-nums}.wp-block-table figcaption{text-align:left}'
       '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:.3em;text-decoration-color:var(--wp--preset--color--accent)}'
       ':focus-visible{outline:3px solid var(--wp--preset--color--accent-2);outline-offset:3px}'
       '@media (min-width:782px){.is-style-sticky-map{position:sticky;top:var(--wp--preset--spacing--40)}}@media (max-width:781px){header .wp-block-search{display:none}}'
       '@media print{header,footer,.wp-block-image,.wp-block-cover,.wp-block-buttons{display:none!important}body{font-size:11pt}}')

theme = {
  '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
  'settings': {
    'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
    'layout': {'contentSize': '700px', 'wideSize': '1280px'},
    'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
              'palette': palette('#FFFFFF', '#111111', '#D80028', '#1C3FD6', '#F6F3EF', '#111111', '#555555', '#F2B8CF')},
    'typography': {'defaultFontSizes': False, 'fluid': True, 'fontFamilies': fonts, 'fontSizes': [
        fs('x-small', '0.875rem', 'Label'), fs('small', '1rem', 'Small'), fs('medium', '1.125rem', 'Body'),
        fs('large', '1.5rem', 'Large', '1.3rem'), fs('x-large', '2.375rem', 'Section', '1.8rem'),
        fs('xx-large', '3.75rem', 'Title', '2.5rem'), fs('display', '6rem', 'Display', '3.1rem')]},
    'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
        {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
        {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2.2vw, 1.75rem)', 'name': '4'},
        {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.25rem, 5.5vw, 4rem)', 'name': '6'},
        {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 8.5rem)', 'name': '8'}]},
    'shadow': {'defaultPresets': False, 'presets': []},
    'border': {'color': True, 'radius': True, 'style': True, 'width': True},
  },
  'styles': {
    'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55'},
    'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
    'elements': {
      'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
               ':hover': {'color': {'text': 'var:preset|color|accent'}}},
      'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'lineHeight': '1.02', 'letterSpacing': '-0.02em'}},
      'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
      'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
      'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.12', 'letterSpacing': '-0.01em'}},
      'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.25', 'letterSpacing': '0'}},
      'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'letterSpacing': '0'}},
      'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0'},
             'color': {'text': 'var:preset|color|accent-2'}},
      'button': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                 'border': {'radius': '2px'},
                 'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|small'},
                 'spacing': {'padding': {'top': '0.85em', 'bottom': '0.85em', 'left': '1.3em', 'right': '1.3em'}},
                 ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}},
                 ':focus': {'outline': {'color': 'var:preset|color|accent-2', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
      'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
    },
    'blocks': {
      'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.01em'},
                          'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
      'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|small'},
                          'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
      'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
      'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
                          'elements': {'link': {'color': {'text': 'var:preset|color|accent-2'}, 'typography': {'textDecoration': 'none'}}}},
      'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
      'core/image': {'border': {'radius': '0'}},
      'core/post-featured-image': {'border': {'radius': '0'}},
      'core/cover': {'border': {'radius': '0'}},
      'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '3px 0 0 0'}},
      'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'},
                     'border': {'left': {'color': 'var:preset|color|accent', 'width': '6px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                     'css': '& cite{display:block;font-family:var(--wp--preset--font-family--body);font-weight:400;font-size:var(--wp--preset--font-size--small);margin-top:.6em;font-style:normal}'},
      'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
                       'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}, 'css': '& summary{font-weight:600;cursor:pointer}'},
      'core/search': {'css': '& .wp-block-search__inside-wrapper{border:0;padding:0;background:var(--wp--preset--color--surface)}& .wp-block-search__input{border:0;border-bottom:2px solid var(--wp--preset--color--contrast);border-radius:0;background:transparent}'},
      'core/query-pagination': {'typography': {'fontWeight': '600'}},
    },
    'css': CSS,
  },
  'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                    {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice'}],
  'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Cityguide
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A bold, colour-blocked theme for independent city guides that publish what's on, places, neighbourhoods and lists every week.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: cityguide
Tags: blog, news, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def variation(title, pal):
    return json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal}}}, indent='\t')
write('styles/glow.json', variation('Glow night', palette('#141019', '#F7F3EE', '#FF5470', '#8FB0FF', '#221C2A', '#F7F3EE', '#BDB4C4', '#5A2440')))
write('styles/canal.json', variation('Canal', palette('#E3F1F4', '#0F1E26', '#C8102E', '#1B4FA8', '#FFFFFF', '#0F1E26', '#3F535C', '#FFD3DC')))
write('styles/market-day.json', variation('Market day', palette('#FFF4D6', '#1B1B12', '#1F6B3A', '#8A2B0B', '#FFFFFF', '#1B1B12', '#55523F', '#F5C95B')))

def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
          'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t', ensure_ascii=False))

def sawtooth(slug, title, bg, text, link):
    section(slug, title, ['core/group'], {
        'color': {'background': 'var:preset|color|%s' % bg, 'text': 'var:preset|color|%s' % text},
        'elements': {'link': {'color': {'text': 'var:preset|color|%s' % link}}, 'heading': {'color': {'text': 'var:preset|color|%s' % text}}},
        'spacing': {'margin': {'top': 'var:preset|spacing|70'}},
        'css': '&{position:relative}&::before{content:"";position:absolute;left:0;right:0;bottom:100%%;height:28px;background:%s}' % (TEETH % bg)})
sawtooth('sawtooth-rose', 'Sawtooth roof: rose', 'pink', 'contrast', 'contrast')
sawtooth('sawtooth-red', 'Sawtooth roof: red', 'accent', 'base', 'base')
sawtooth('sawtooth-ink', 'Sawtooth roof: ink', 'contrast', 'base', 'base')
section('label', 'Category label (blue)', ['core/paragraph', 'core/post-terms'], {
    'color': {'text': 'var:preset|color|accent-2'}, 'typography': {'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
    'elements': {'link': {'color': {'text': 'var:preset|color|accent-2'}}}})
section('pin', 'Map pin number', ['core/paragraph'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1'},
    'border': {'radius': '999px', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'css': '&{display:grid;place-items:center;width:2.4em;height:2.4em;flex:0 0 auto;margin:0}'})
section('timetable', 'Timetable row', ['core/group', 'core/columns'], {
    'border': {'top': {'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})
section('photo-hero', 'Photo behind text', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'css': '&{position:relative;overflow:hidden;min-height:78vh;display:flex;flex-direction:column;justify-content:flex-end}&>.wp-block-image{position:absolute;inset:0;margin:0!important;max-width:none!important}&>.wp-block-image img{width:100%;height:100%!important;object-fit:cover;filter:brightness(.45)}&>*:not(.wp-block-image){position:relative;z-index:1}'})
section('sticky-map', 'Sticky map column', ['core/column', 'core/group'], {})
section('closed', 'Closed place', ['core/group'], {
    'color': {'background': 'var:preset|color|surface'},
    'border': {'left': {'width': '6px', 'style': 'solid', 'color': 'var:preset|color|contrast'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
    'css': '& h3{text-decoration:line-through;text-decoration-thickness:3px}'})
section('note', 'Note box', ['core/group', 'core/paragraph'], {
    'color': {'background': 'var:preset|color|surface'},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})

PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}
FULLPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}
FULL = {'type': 'constrained', 'contentSize': '700px', 'wideSize': '1280px'}
def crop(block, ratio='4/3'):
    return block.replace('<img ', '<img style="aspect-ratio:%s;object-fit:cover" ' % ratio, 1)
def sect(inner, **a):
    return group(inner, align='wide', layout={'type': 'default'}, style=PAD, **a)
def hid(text, anchor, level=2, **a):
    return heading(text, level, **a).replace('<h%d class="' % level, '<h%d id="%s" class="' % (level, anchor), 1)
def label(t):
    return para(t, className='is-style-label')

# ------------------------------------------------------------------ parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}),
          dyn('search', label='Search', showLabel=False, placeholder='Search', buttonText='Search', buttonUseIcon=True, buttonPosition='button-inside', width=12, widthUnit='rem')),
        justify='space-between', align='wide'),
    tag='header', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}))

write('parts/footer.html', group(J(
    columns(('40%', J(para('Lampje', fontSize='xx-large', fontFamily='display', style={'typography': {'fontWeight': '900', 'lineHeight': '1'}}),
                      para('An independent guide to Eindhoven by Sanne Verhoeven and Joost Bakker. Nobody pays to be in it. We pay for our own coffee.'))),
            (None, J(heading('The guide', 6, textColor='base'), para('<a href="/this-week/">This week</a><br><a href="/map/">The map</a><br><a href="/neighbourhoods/">Neighbourhoods</a><br><a href="/guide/">All stories</a>'))),
            (None, J(heading('Write to us', 6, textColor='base'), para('Tips, corrections and closures: <a href="mailto:tips@example.com">tips@example.com</a>'),
                     para('We read everything and reply on Mondays.'))),
            (None, J(heading('The Thursday list', 6, textColor='base'), para('Six things for the weekend, every Thursday at 7:00.'),
                     buttons(('Get the Thursday list', 'mailto:hello@example.com?subject=Thursday%20list'), className='is-style-inverse'))),
            align='wide'),
    para('Photos are CC0 and public-domain images from Wikimedia Commons and the Nationaal Archief, used as stand-ins. The sketch map was drawn for this theme.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-sawtooth-red',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}}}))
section('inverse', 'Inverse buttons', ['core/buttons'], {'elements': {'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}}}})

write('parts/notice.html', pattern_ref('corrections-note'))

# ------------------------------------------------------------------ templates
MAIN = {'style': {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|60'}}}}
CARD = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover'),
         dyn('post-terms', term='category'),
         dyn('post-title', isLink=True, level=3, fontSize='large'))

write('templates/front-page.html', page_template(J(
    pattern_ref('hero-this-week'), pattern_ref('this-week-list'), pattern_ref('latest-lists'),
    pattern_ref('neighbourhood-tiles'), pattern_ref('map-list'), pattern_ref('weekend-picks'), pattern_ref('strijp-night-strip')),
    **{'style': {'spacing': {'padding': {'top': '0', 'bottom': '0'}}}}))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1, fontSize='display', align='wide'),
    dyn('post-content', layout={'type': 'constrained'})), **MAIN))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1, fontSize='display', align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1280px'})), **MAIN))

write('templates/single.html', page_template(J(
    group(J(dyn('post-terms', term='category'), dyn('post-date')), layout={'type': 'flex', 'flexWrap': 'wrap'}),
    dyn('post-title', level=1, fontSize='xx-large'),
    dyn('post-featured-image', align='wide', aspectRatio='16/9', scale='cover'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(J(para('Something changed? A place closed, the hours moved, the price went up? Tell us at <a href="mailto:tips@example.com">tips@example.com</a> and we fix it within a week.')), className='is-style-note'),
    group(row(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)), justify='space-between'),
          align='wide', className='is-style-timetable', layout={'type': 'default'})), **MAIN))

pattern('post-grid', 'Stories grid (inherits the page query)', 'cityguide-lists,query', inherit_query(
    CARD, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '15rem'}, align='wide'), inserter=False)
pattern('post-list', 'Stories list', 'cityguide-lists,query', inherit_query(
    J(dyn('post-terms', term='category'), dyn('post-title', isLink=True, level=2, fontSize='large')), template_class='is-style-timetable'), inserter=False)

write('templates/home.html', page_template(J(
    heading('Everything in the guide', 1, fontSize='display', align='wide'),
    dyn('categories', className='is-style-label', align='wide'),
    pattern_ref('post-grid')), **MAIN))
write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='display'),
    dyn('term-description', align='wide'), pattern_ref('post-grid')), **MAIN))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), **MAIN))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Coffee, Strijp, GLOW', buttonText='Search'),
    pattern_ref('post-list')), **MAIN))
write('templates/404.html', page_template(J(
    heading('This street does not exist', 1, fontSize='xx-large'),
    para('The link may be old, or the place closed and we took the page down. Try <a href="/this-week/">this week</a>, <a href="/map/">the map</a> or a search.'),
    dyn('search', label='Search', showLabel=False, placeholder='Coffee, Strijp, GLOW', buttonText='Search')), **MAIN))

# ------------------------------------------------------------------ patterns
pattern('hero-this-week', 'Hero: this week in Eindhoven', 'featured', group(J(
    image('dynamo.jpg', 'A band on a dark stage under white spotlights, with the crowd in silhouette in front', lightbox=False),
    heading('What\'s on in Eindhoven, 28 September to 4 October', 1, fontSize='display', textColor='base'),
    para('Picked by Sanne and Joost, updated every Monday morning. Gigs, markets, openings and one very good soup.', fontSize='large', textColor='base'),
    buttons(('See the whole week', '/this-week/'))),
    align='full', className='is-style-photo-hero', layout={'type': 'constrained', 'contentSize': '1280px', 'wideSize': '1280px'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|80', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
    description='Full-bleed photo with the week in the headline. Swap the image for this week\'s best photo.')

EVENTS = [
    ('Mon 28', '20:00', 'Open mic, all instruments', 'Café Wilhelmina, Wilhelminaplein', 'Free'),
    ('Wed 30', '19:30', 'Film: Paris, Texas, on 35 mm', 'Natlab, Kastanjelaan', '€10.50'),
    ('Thu 1', '17:00', 'Late opening with a talk on the Proun room', 'Van Abbemuseum, Stratumsedijk', '€17.50'),
    ('Fri 2', '21:00', 'Inferum and two support bands', 'Dynamo, Catharinaplein', '€14'),
    ('Sat 3', '08:00', 'Saturday market, cheese and stroopwafels', 'Woenselse Markt', 'Free'),
    ('Sun 4', '11:00', 'Guided walk along the Dommel', 'Start at the Genneper Parken café', '€6'),
]
def event_rows(evts):
    out = []
    for day, time, what, where, price in evts:
        out.append(columns(('14%', para('<strong>%s</strong><br>%s' % (day, time))),
                           ('50%', heading(what, 3, fontSize='large')),
                           ('24%', para(where)),
                           ('12%', para('<strong>%s</strong>' % price, style={'typography': {'textAlign': 'right'}})),
                           className='is-style-timetable', isStackedOnMobile=False, style={'spacing': {'margin': {'top': '0', 'bottom': '0'}}}))
    return J(*out)

pattern('this-week-list', 'This week: timetable', 'featured,cityguide-events', group(group(J(
    row(J(heading('This week', 2, fontSize='xx-large'), para('<a href="/this-week/">The full list, with tickets</a>')), justify='space-between'),
    event_rows(EVENTS)), layout={'type': 'constrained', 'contentSize': '1280px'}),
    align='full', className='is-style-sawtooth-rose', layout=FULL, style=FULLPAD),
    description='Day, time, what, where and price, on a rose section with a sawtooth-roof top edge.')

pattern('latest-lists', 'Latest lists and stories', 'cityguide-lists,query', sect(J(
    row(J(heading('Lists and stories', 2), para('<a href="/guide/">Everything in the guide</a>')), justify='space-between'),
    query(CARD, per_page=4, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '14rem'}))))

HOODS = [('Strijp', 'ontdekfabriek.jpg', 'The old Philips factory town west of the centre. Lofts, the Ontdekfabriek, a Saturday flea market in the Klokgebouw.', 'strijp',
          'A long white Philips factory block with rows of windows and arched doors on the ground floor'),
         ('Centrum', 'stratumseind.jpg', 'Shopping streets, the Catharinakerk and Stratumseind, the longest bar street in the country. Go early.', 'centrum',
          'Three stone statues in pointed brick niches on the front of the Catharinakerk'),
         ('Stratum', 'dommel.jpg', 'Quieter, greener, south along the Dommel. The Van Abbemuseum, the Genneper Parken and good Turkish bakeries.', 'stratum',
          'A concrete bridge over the Dommel river, photographed in black and white when it was new'),
         ('Woensel', 'bikeparking.jpg', 'The big north, where most people actually live. The Woenselse Markt on Saturdays is the best market in town.', 'woensel',
          'Rows of parked bicycles crammed together in a bike rack'),
         ('Kruisstraat', 'kruisstraat.jpg', 'One long street north of the centre with bakeries, grocers and snack bars from about thirty countries.', 'kruisstraat',
          'An old sandstone house on a corner of a quiet street with red brick paving'),
         ('Tongelre', 'psv.jpg', 'East, past the station, with the PSV stadium in view from the train. Allotments, the canal and cheap rent, for now.', 'tongelre',
          'The PSV stadium seen from a passing train, with overhead wires in the foreground')]

pattern('neighbourhood-tiles', 'Neighbourhood tiles', 'cityguide-places', sect(J(
    heading('Six neighbourhoods', 2),
    grid(J(*[stack(J(crop(image(img, alt, href='/neighbourhoods/#%s' % a, aspectRatio='4/3', scale='cover')),
                     heading('<a href="/neighbourhoods/#%s">%s</a>' % (a, n), 3), para(t, fontSize='small')),
                   style={'spacing': {'blockGap': 'var:preset|spacing|20'}}) for n, img, t, a, alt in HOODS]), min_width='19rem'))))

PLACES = [
    ('Koffiebar Haring', 'Strijp', 'A long counter in a former Philips lab. The flat white is €3.40 and worth it; the cake is fine.', 'Torenallee 22', 'Tue to Sun, 8:00 to 17:00', '€', 'September 2026'),
    ('Soepbar Kaat', 'Centrum', 'Three soups a day, bread from Bakkerij Leenders, and a queue at 12:15. Go at 11:45.', 'Kleine Berg 41', 'Mon to Sat, 11:30 to 16:00', '€', 'August 2026'),
    ('Van Abbemuseum', 'Stratum', 'Picasso, Kandinsky and the Proun room. Thursday evenings are quieter and cheaper after 17:00.', 'Stratumsedijk 2', 'Tue to Sun, 11:00 to 17:00', '€€', 'September 2026'),
    ('Pâtisserie Mimi', 'Tongelre', 'French pastry by a woman from Lyon who moved here for a Philips engineer. Tarte au citron, €4.80.', 'Tongelresestraat 190', 'Wed to Sun, 9:00 to 17:00', '€€', 'July 2026'),
    ('Platenzaak Rondje', 'Centrum', 'Records, mostly second-hand, sorted by a man who will tell you what you actually want.', 'Bergstraat 12', 'Tue to Sat, 11:00 to 18:00', '€€', 'September 2026'),
    ('Genneper Parken', 'Stratum', 'Three rivers, a watermill, and the flattest long walk you will ever enjoy. Café at the Genneper Hoeve.', 'Genneperweg', 'Always open', 'Free', 'June 2026'),
    ('Fırın Anadolu', 'Kruisstraat', 'Turkish bakery, open early. Simit at 7:00, still warm. Cash is quicker.', 'Kruisstraat 88', 'Daily, 6:30 to 20:00', '€', 'September 2026'),
    ('Woenselse Markt', 'Woensel', 'The Saturday market. Fish at the north end, cheese in the middle, flowers by the church.', 'Woenselse Markt', 'Sat, 8:00 to 16:00', 'Free', 'September 2026'),
]

def place_entry(i, name, hood, review, addr, hours, band, visited):
    return group(J(
        row(J(para(str(i), className='is-style-pin'), heading(name, 3)), wrap=False, style={'spacing': {'blockGap': 'var:preset|spacing|30'}}),
        label(hood),
        para(review),
        para('%s<br>%s<br>Price: %s. Last visited %s.' % (addr, hours, band, visited), fontSize='small', textColor='muted')),
        layout={'type': 'default'}, className='is-style-timetable')

pattern('map-list', 'The map: numbered list and sketch map', 'featured,cityguide-places', sect(J(
    heading('Eight places we keep going back to', 2),
    columns(('50%', J(*[place_entry(i, *p) for i, p in enumerate(PLACES, 1)])),
            ('50%', group(image('sketch-map.jpg', 'Sketch map of Eindhoven with the ring road, the Dommel and the railway, and eight red numbered pins that match the list', 'Numbers match the list. Not to scale.', lightbox=False),
                          className='is-style-sticky-map', layout={'type': 'default'})),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))),
    description='The signature pattern: each numbered entry on the list matches a numbered pin on the map.')

pattern('place-entry', 'Place entry', 'cityguide-places', place_entry(1, *PLACES[0]))

pattern('place-closed', 'Closed place (kept on the list)', 'cityguide-places', group(J(
    heading('Café De Tuinzaal', 3), label('Centrum'),
    para('<strong>Closed in August 2026.</strong> The owners retired. We keep the entry so nobody walks there for nothing. The terrace is now a phone shop.')),
    className='is-style-closed', layout={'type': 'default'}), description='Use when a place closes. Keep it up for a few months.')

pattern('price-band-key', 'Price band key', 'cityguide-places', table(
    [['€', 'Under €10 a head'], ['€€', '€10 to €25'], ['€€€', '€25 to €50'], ['€€€€', 'More than €50, and we will say why']], head=['Band', 'What it means']))

pattern('strijp-night-strip', 'Strijp at night, archive strip', 'cityguide-places', group(J(
    image('strijp.jpg', 'Philips factory buildings at night with every window lit, a long black-and-white panorama', 'Philips factories lit at night, 1950s. Nationaal Archief, public domain.', lightbox=False, align='wide'),
    para('Eindhoven was built around light bulbs. Most of the factories in this photo are flats, studios and restaurants now; the sawtooth roofs are still there if you look up in Strijp.', align='wide')),
    align='full', className='is-style-sawtooth-ink', layout=FULL, style=FULLPAD))

pattern('themed-lists', 'Themed lists index', 'cityguide-lists', sect(columns(
    (None, J(heading('Cheap eats', 3), lst(['Soup at Soepbar Kaat, €6.50', 'Simit at Fırın Anadolu, €1.20', 'Frites at the Woenselse Markt, €3.50', 'Lunch bowls near the station, under €12']))),
    (None, J(heading('Late', 3), lst(['Dynamo, gigs until 01:00', 'Stratumseind, if you must, on a Thursday', 'Night shop on the Kruisstraat until 23:00', 'The 24-hour bike park at the station']))),
    (None, J(heading('Rainy days', 3), lst(['Van Abbemuseum, the Proun room', 'Evoluon open days', 'Natlab, three films a night', 'Record digging on the Bergstraat']))),
    align='wide')))

pattern('newsletter-thursday', 'The Thursday list newsletter', 'call-to-action', group(J(
    heading('The Thursday list', 2),
    para('Six things for the weekend in one email, every Thursday at 7:00. Joost writes it on the train from Den Bosch, so the spelling is his problem.'),
    buttons(('Get the Thursday list', 'mailto:hello@example.com?subject=Thursday%20list'))),
    align='full', className='is-style-sawtooth-rose', layout=FULL, style=FULLPAD))

pattern('corrections-note', 'Corrections note', 'cityguide-about', para(
    'Correction, 22 September: Soepbar Kaat is closed on Sundays, not Mondays. Thanks, Marieke.', className='is-style-note'))

pattern('getting-here', 'Getting here and around', 'cityguide-practical', sect(columns(
    ('50%', J(heading('Getting here', 3),
              table([['Train from Amsterdam', '1 h 20 min, every 15 minutes'], ['Train from Utrecht', '50 min'], ['Eindhoven Airport', 'Bus 400 or 401, 25 min, €4.30'],
                     ['Düsseldorf', '1 h 35 min by train via Venlo']]))),
    ('50%', J(heading('Getting around', 3),
              para('Rent a bike at the station. The centre is flat and small; nothing on our map is more than 20 minutes by bike from Stratumseind.'),
              para('Bottles have a deposit. Return them at the statiegeld machines in any supermarket or at the station for 15 or 25 cents.'))),
    align='wide')))

pattern('accommodation-types', 'Where to stay, by type', 'cityguide-practical', sect(J(
    heading('Where to stay', 2),
    table([['Hostel', 'Strijp', 'Dorms from €32, a kitchen, bike hire downstairs'],
           ['Small hotel', 'Centrum', 'From €95, walkable to everything, noisy on Thursdays'],
           ['Apartment', 'Stratum', 'From €110, quiet streets, 10 minutes by bike'],
           ['Camping', 'Genneper Parken edge', 'Pitches from €22, April to October']], head=['Type', 'Area', 'What to expect']),
    para('We are not paid for any of these and we do not link to booking sites. Search the area and pick what fits.', fontSize='small'))))

pattern('printable-list', 'Print this list', 'cityguide-places', group(
    para('<strong>Going offline?</strong> Print this page. The print version drops the photos, the header and the footer, and fits the list on one A4 sheet.'),
    className='is-style-note', layout={'type': 'default'}))

pattern('event-calendar', 'Coming up this autumn', 'cityguide-events', sect(J(
    heading('Coming up this autumn', 2),
    table([['17 to 25 October', 'Dutch Design Week', 'All over town, Strijp busiest', 'Most shows free'],
           ['8 to 15 November', 'GLOW light festival', 'A walking route through the centre', 'Free'],
           ['22 November', 'Record fair', 'Klokgebouw, Strijp', '€3'],
           ['From 28 November', 'Winter market', 'Catharinaplein', 'Free']],
          head=['When', 'What', 'Where', 'Price']))))

pattern('this-week-page', 'Page: this week', 'cityguide-events', J(
    para('Everything we would go to this week, in order. Prices are at the door unless we say otherwise.', fontSize='large'),
    group(event_rows(EVENTS + [('Sun 4', '15:00', 'Record fair, second-hand only', 'Klokgebouw, Strijp', '€3')]), layout={'type': 'default'}),
    pattern_ref('event-calendar'), pattern_ref('newsletter-thursday')), block_types='core/post-content')

pattern('map-page', 'Page: the map', 'cityguide-places', J(
    para('Our eight favourite places right now, numbered on a map you can print. We update the list at the start of each month.', fontSize='large'),
    pattern_ref('printable-list'), pattern_ref('map-list'), pattern_ref('place-closed'), pattern_ref('price-band-key')), block_types='core/post-content')

def hood_section(n, img, t, a, alt, extra):
    return sect(columns(('45%', crop(image(img, alt, aspectRatio='4/3', scale='cover'))),
                        ('55%', J(hid(n, a), para(t, fontSize='large'), lst(extra))),
                        verticalAlignment='top', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}), className='is-style-timetable')

EXTRAS = {
    'strijp': ['Flea market in the Klokgebouw, first Sunday of the month', 'Koffiebar Haring for the long counter', 'Look up: the sawtooth roofs on Torenallee'],
    'centrum': ['Catharinakerk, free to enter, Tuesday to Saturday', 'Soepbar Kaat for lunch', 'Stratumseind, earlier in the evening than you think'],
    'stratum': ['Van Abbemuseum', 'The Genneper Parken walk, 6 km', 'Bakeries on the Leenderweg'],
    'woensel': ['Saturday market', 'The Karpendonkse Plas for a swim in summer', 'Cheap Surinamese food on the Kruisstraat edge'],
    'kruisstraat': ['Fırın Anadolu at 7:00', 'Polish, Syrian and Moroccan grocers side by side', 'Park at the north end; the street is one-way'],
    'tongelre': ['Pâtisserie Mimi', 'PSV home games: avoid the 400 bus after 22:00', 'The Eindhovens Kanaal towpath by bike'],
}
pattern('neighbourhoods-page', 'Page: neighbourhoods', 'cityguide-places', J(
    para('Six parts of town, each with what we would do there on a free afternoon.', fontSize='large'),
    *[hood_section(n, img, t, a, alt, EXTRAS[a]) for n, img, t, a, alt in HOODS]), block_types='core/post-content')

pattern('about-us', 'About the guide', 'cityguide-about', sect(columns(
    ('58%', J(para('Lampje is Sanne Verhoeven and Joost Bakker. Sanne grew up in Woensel and runs a bike repair shop in Strijp; Joost moved here in 2017 for a job at the TU/e and stayed for the soup.', fontSize='large'),
              para('We started Lampje in 2021 because the official guides only covered the things with marketing budgets. Everything here is somewhere we have been, paid for ourselves, in the last six months.'),
              para('We do not take money for listings, free meals or press trips. If a place pays for an ad in the Thursday list, it says "advert" in red at the top.'),
              para('We skip Stratumseind after midnight. You will not miss much.'))),
    ('42%', image('bikes.jpg', 'Inside a small bike shop with bikes hanging from the ceiling, a wooden counter and a map on the wall', 'The bike shop where half of Lampje gets written.')),
    align='wide')))

pattern('how-we-choose', 'How we choose places', 'cityguide-about', group(J(
    heading('How we choose', 3),
    lst(['We visit twice, at different times, before a place goes in.', 'We write down the date of the last visit on every entry.', 'Closed places stay up with a note for three months.',
         'Readers\' tips get checked in person. Send them anyway.'], ordered=True)), layout={'type': 'constrained'}, style=PAD))

pattern('about-page', 'Page: about', 'cityguide-about', J(pattern_ref('about-us'), pattern_ref('how-we-choose'), pattern_ref('getting-here'), pattern_ref('accommodation-types')), block_types='core/post-content')

pattern('quote-reader', 'Quote from a reader', 'cityguide-about', quote(
    'Moved here in March, knew nobody. Went to every place on the map in order. Number 7 is now my Saturday.',
    'Priya Raman, Woensel, reader since April 2026'))

pattern('weekend-picks', 'Weekend picks, three columns', 'cityguide-events', sect(columns(
    (None, J(label('Saturday morning'), heading('Woenselse Markt, then simit on the Kruisstraat', 3), para('Market from 8:00. Walk south for breakfast. Back by 11:00 before the crowds.'))),
    (None, J(label('Saturday night'), heading('Inferum at Dynamo', 3), para('Doors 20:30, first band 21:00, done by 23:00. €14 at the door, cash or card.'))),
    (None, J(label('Sunday'), heading('The Dommel walk', 3), para('6 km through the Genneper Parken. Start at 11:00 with the guide, or alone whenever you like.'))),
    align='wide')))

pattern('tips-page', 'Page: tips and corrections', 'cityguide-about', J(
    para('Found a place we should know about? Spotted something wrong? Write to us. We read everything and reply on Mondays.', fontSize='large'),
    columns((None, J(heading('Send a tip', 3), para('Tell us the name, the street and why you go there. One good reason is enough.'),
                     buttons(('Email a tip', 'mailto:tips@example.com?subject=Tip')))),
            (None, J(heading('Report a change', 3), para('Closed, moved, new hours, new prices. We check it and fix the page within a week, with a dated note.'),
                     buttons(('Email a correction', 'mailto:tips@example.com?subject=Correction'))))),
    pattern_ref('corrections-note'), pattern_ref('quote-reader')), block_types='core/post-content')

print('cityguide: patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

write('functions.php', '''<?php
/**
 * Cityguide: pattern categories only.
 *
 * @package cityguide
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'cityguide-events'    => 'City guide: events',
			'cityguide-places'    => 'City guide: places and map',
			'cityguide-lists'     => 'City guide: lists and stories',
			'cityguide-practical' => 'City guide: practical',
			'cityguide-about'     => 'City guide: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);''')

# ------------------------------------------------------------------ demo content
def story(paras, extra=None):
    out = [para(p) for p in paras]
    if extra:
        out.append(extra)
    return J(*out)

def numbered(items):
    return J(*[group(J(row(J(para(str(i), className='is-style-pin'), heading(n, 3)), wrap=False, style={'spacing': {'blockGap': 'var:preset|spacing|30'}}), para(t)),
                     layout={'type': 'default'}, className='is-style-timetable') for i, (n, t) in enumerate(items, 1)])

POSTS = [
  ('What\'s on: 28 September to 4 October', 'whats-on', 'dynamo.jpg', '2026-09-27',
   story(['A quiet week before Dutch Design Week eats the city. Our pick is Friday at Dynamo: Inferum are loud, short and done by 23:00.'],
         table([[d, t, w, p] for d, t, w, _, p in EVENTS], head=['Day', 'Time', 'What', 'Price']))),
  ('Six lunches under €12 near the station', 'eat-drink', 'lunch.jpg', '2026-09-24',
   numbered([('Soepbar Kaat', 'Soup and bread, €6.50. Three soups a day, one always vegan.'), ('Poké on the Vestdijk', 'A big bowl for €11.50. The steak one is heavier than it looks.'),
             ('Fırın Anadolu', 'Pide with cheese, €5. A ten-minute walk, and you get simit for later.'), ('Broodje Bert', 'Kroket on white bread, €3.80. The mustard is the point.'),
             ('The station food hall', 'Fine if you have eight minutes. Skip the sushi.'), ('Lunchroom Heuvel', 'Uitsmijter with three eggs, €9.50, and a window seat if you are lucky.')])),
  ('Dutch Design Week, a survival list', 'whats-on', 'ontdekfabriek.jpg', '2026-09-20',
   story(['DDW runs from 17 to 25 October and brings about 350,000 visitors to a city of 240,000. You can still enjoy it.',
          'Go to Strijp on weekday mornings. Take a bike, not the shuttle bus. Eat in Stratum, where nobody from DDW goes.',
          'The graduation show at the Design Academy is the one thing we would queue for.'])),
  ('The Proun room at the Van Abbe', 'culture', 'vanabbe.jpg', '2026-09-15',
   story(['El Lissitzky built the first Proun room in Berlin in 1923. The Van Abbemuseum reconstructed it in 1965 and it has been one of the best rooms in the city since.',
          'It takes three minutes to walk through and about twenty to stop looking. Thursday after 17:00 is €11 instead of €17.50.'])),
  ('Kruisstraat, the long street', 'neighbourhoods', 'kruisstraat.jpg', '2026-09-08',
   story(['The Kruisstraat runs about two kilometres north from the centre and has more bakeries per metre than anywhere else in Eindhoven.',
          'Start at the south end at 7:00 for simit, walk north, stop for Syrian sweets at the corner of the Hoogstraat, and end at the park.'])),
  ('Nuenen by bike, where Van Gogh painted the potato eaters', 'day-trips', 'nuenen.jpg', '2026-08-30',
   story(['Nuenen is 8 km east of the centre, about 30 minutes by bike along the Dommel and then the long straight Dreef.',
          'The Vincentre is small and good. The vicarage where Van Gogh lived is private, so look from the street.'])),
  ('The Evoluon, open again for one weekend', 'culture', 'evoluon.jpg', '2026-08-21',
   story(['The flying saucer on the Noord Brabantlaan opened in 1966 as Philips\' science museum. It is a conference centre now and opens to the public twice a year.',
          'Next open days: 7 and 8 November, 10:00 to 16:00, free. Go up to the ring gallery; the view down is the reason to come.'])),
  ('Arriving: trains, the airport bus and statiegeld', 'practical', 'station.jpg', '2026-08-10',
   story(['Most visitors arrive at the central station. Bike hire is under the tracks on the north side; bring ID.',
          'From the airport, buses 400 and 401 run every ten minutes to the station and take 25 minutes. Pay by card at the door.',
          'Every plastic bottle and can has a deposit, 15 or 25 cents. The statiegeld machines at the station give you a voucher for the shop.'])),
  ('Coffee in Strijp, ranked by how long we stayed', 'eat-drink', 'cafe.jpg', '2026-07-30',
   numbered([('Koffiebar Haring', 'Three hours. A long counter, sockets everywhere, nobody hurries you.'), ('Kiosk op het plein', 'Forty minutes, standing. The best espresso and no chairs.'),
             ('The Klokgebouw café', 'An hour. Fine coffee, but you will stay for the building.')])),
]

content = {
  'site': {'title': 'Lampje', 'tagline': 'An independent guide to Eindhoven, updated every Monday'},
  'categories': [{'slug': 'whats-on', 'name': 'What\'s on', 'description': 'The week ahead and the big events.'},
                 {'slug': 'eat-drink', 'name': 'Eat and drink', 'description': 'Places we have eaten and paid for.'},
                 {'slug': 'culture', 'name': 'Culture', 'description': 'Museums, films, gigs and buildings.'},
                 {'slug': 'neighbourhoods', 'name': 'Neighbourhoods', 'description': 'One part of town at a time.'},
                 {'slug': 'day-trips', 'name': 'Day trips', 'description': 'Half an hour away by bike or train.'},
                 {'slug': 'practical', 'name': 'Practical', 'description': 'Getting here, getting around.'}],
  'front_page': 'home', 'posts_page': 'guide',
  'pages': [
    {'slug': 'home', 'title': 'Home', 'content': ''},
    {'slug': 'guide', 'title': 'All stories', 'content': ''},
    {'slug': 'this-week', 'title': 'This week', 'pattern': 'cityguide/this-week-page', 'template': 'page-wide'},
    {'slug': 'map', 'title': 'The map', 'pattern': 'cityguide/map-page', 'template': 'page-wide'},
    {'slug': 'neighbourhoods', 'title': 'Neighbourhoods', 'pattern': 'cityguide/neighbourhoods-page', 'template': 'page-wide'},
    {'slug': 'about', 'title': 'About Lampje', 'pattern': 'cityguide/about-page', 'template': 'page-wide'},
    {'slug': 'tips', 'title': 'Tips and corrections', 'pattern': 'cityguide/tips-page'},
  ],
  'posts': [{'title': t, 'category': c, 'image': img, 'date': d, 'content': body} for t, c, img, d, body in POSTS],
  'nav': [{'label': 'This week', 'url': '/this-week/'}, {'label': 'Eat and drink', 'url': '/category/eat-drink/'},
          {'label': 'Culture', 'url': '/category/culture/'}, {'label': 'Neighbourhoods', 'url': '/neighbourhoods/'},
          {'label': 'The map', 'url': '/map/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs('demos/cityguide', exist_ok=True)
json.dump(content, open('demos/cityguide/content.json', 'w'), indent=1, ensure_ascii=False)
print('cityguide: demo content written')
