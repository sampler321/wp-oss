# Design note (rep, idea 033, illustration and artist representation agency)
# Direction: "index catalogue". A white page ruled in 1px black lines, a dense six-up grid of small captioned
#   tiles (work, artist, client, year) and a roster that is a list of names set large, like an agency's printed index.
# Fonts: Clash Grotesk only (Fontshare, variable 200 to 700): 600 for the index and headings, 400 for text, 500 small for captions.
# Palette: #FFFFFF, #121212 text and rules, #E24E1B vermilion only for hover on names and the enquiry band, #F2F2F0 surface.
# Layout idea: artists are categories nested under disciplines, so core's Categories block becomes the roster and the
#   discipline filter; styles are tags, so every style page pulls credited work from the whole roster.
import sys, json, os, shutil
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('rep')

_image = image
def image(filename, alt, caption='', **kw):
    """blocks.image plus the inline aspect-ratio/object-fit style core saves, so the ratio survives normalising."""
    out = _image(filename, alt, caption, **kw)
    if kw.get('aspectRatio'):
        st = 'aspect-ratio:%s' % kw['aspectRatio'] + (';object-fit:%s' % kw['scale'] if kw.get('scale') else '')
        out = out.replace('<img ', '<img style="%s" ' % st, 1)
    return out
D = THEME['dir']
for sub in ('patterns', 'templates', 'parts', 'styles'):
    shutil.rmtree(os.path.join(D, sub), ignore_errors=True)

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

P = lambda s: 'var:preset|spacing|%s' % s
C = lambda slug: 'var:preset|color|%s' % slug
pad = lambda t, b=None: {'spacing': {'padding': {'top': P(t), 'bottom': P(b or t)}}}
pal = lambda rows: [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
fonts.append({'fontFamily': '"Clash Grotesk", sans-serif', 'name': 'Clash Grotesk (text)', 'slug': 'body'})
palette = [('base', '#FFFFFF', 'Paper'), ('contrast', '#121212', 'Index black'), ('accent', '#E24E1B', 'Vermilion'),
           ('surface', '#F2F2F0', 'Proof'), ('line', '#121212', 'Rule'), ('muted', '#5A5A57', 'Caption grey')]

CSS = (
    ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}html{font-synthesis:none}'
    '.wp-block-post-date,.wp-block-post-excerpt,table{font-variant-numeric:tabular-nums}'
    # dense index grid
    '.wp-block-post-template.is-style-index-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(10.5rem,1fr));gap:var(--wp--preset--spacing--50) var(--wp--preset--spacing--30);list-style:none;padding:0}'
    '.is-style-index-grid>li{margin:0;min-width:0}.is-style-index-grid .wp-block-post-featured-image{margin:0 0 .5rem}'
    '.is-style-index-grid .wp-block-post-featured-image img{aspect-ratio:4/5;object-fit:cover;width:100%;height:auto;display:block}'
    '.is-style-index-grid>li>*{margin-block:0}.is-style-index-grid .wp-block-post-excerpt__excerpt{margin:0}'
    # native-ratio grid for artist pages
    '.wp-block-post-template.is-style-native-grid{display:block;columns:4 14rem;column-gap:var(--wp--preset--spacing--30);list-style:none;padding:0}'
    '.is-style-native-grid>li{break-inside:avoid;margin:0 0 var(--wp--preset--spacing--50)}.is-style-native-grid .wp-block-post-featured-image{margin:0 0 .5rem}'
    '.is-style-native-grid .wp-block-post-featured-image img{width:100%;height:auto;display:block}.is-style-native-grid>li>*{margin-block:0}'
    # roster list (categories block, flat)
    '.wp-block-categories.is-style-roster{list-style:none;padding:0;margin:0;border-top:1px solid var(--wp--preset--color--line);columns:2 22rem;column-gap:var(--wp--preset--spacing--50)}'
    '.is-style-roster li{list-style:none;margin:0;break-inside:avoid;border-bottom:1px solid var(--wp--preset--color--line);padding:.35rem 0 .45rem;font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--xx-large);font-weight:600;letter-spacing:-.03em;line-height:1.05}'
    '.is-style-roster a{color:var(--wp--preset--color--contrast);text-decoration:none}.is-style-roster a:hover,.is-style-roster a:focus{color:var(--wp--preset--color--accent)}'
    '.is-style-roster .current-cat>a{color:var(--wp--preset--color--accent)}'
    # discipline filter (links)
    '.is-style-filter-row a{text-decoration:none;font-weight:500}.is-style-filter-row a:hover{color:var(--wp--preset--color--accent)}'
    # tag cloud as style index
    '.wp-block-tag-cloud.is-style-style-index{display:flex;flex-wrap:wrap;gap:.2rem 1.2rem;margin:0}'
    '.is-style-style-index a{font-size:var(--wp--preset--font-size--x-large)!important;font-weight:500;letter-spacing:-.02em;text-decoration:none;color:inherit;margin:0!important}'
    '.is-style-style-index a:hover{color:var(--wp--preset--color--accent)}'
    # ruled rows (instead of tables)
    '.is-style-ruled-row{border-bottom:1px solid var(--wp--preset--color--line);padding:.5rem 0;gap:.15rem 1.5rem!important}.is-style-ruled-row>p{margin:0;flex:1 1 12rem}'
    '.is-style-ruled-row>p:first-child{flex:0 1 11rem;font-weight:500}'
    # ruled tables
    '.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.5rem 1rem .5rem 0;text-align:left;vertical-align:top}'
    '.wp-block-table thead th{font-weight:500;color:var(--wp--preset--color--muted)}'
    '.wp-block-quote cite{display:block;margin-top:.6rem;font-size:var(--wp--preset--font-size--small);font-style:normal;color:var(--wp--preset--color--muted)}'
    '.wp-block-details summary{font-weight:500;cursor:pointer}'
    '@media (max-width:600px){.wp-block-post-template.is-style-index-grid{grid-template-columns:repeat(2,minmax(0,1fr))}'
    '.wp-block-table.is-style-stack thead{display:none}.wp-block-table.is-style-stack tr{display:block;border-bottom:1px solid var(--wp--preset--color--line);padding:.5rem 0}.wp-block-table.is-style-stack td{display:block;border:0;padding:0}}'
)

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '740px', 'wideSize': '1480px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(palette), 'duotone': []},
        'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False, 'fontFamilies': fonts, 'fontSizes': [
            {'slug': 'x-small', 'size': '0.875rem', 'name': 'Caption', 'fluid': False},
            {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
            {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
            {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
            {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.6rem', 'max': '2.25rem'}},
            {'slug': 'xx-large', 'size': '3.75rem', 'name': 'Index', 'fluid': {'min': '2.1rem', 'max': '3.75rem'}},
            {'slug': 'display', 'size': '5.5rem', 'name': 'Display', 'fluid': {'min': '2.6rem', 'max': '5.5rem'}}]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': C('base'), 'text': C('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '400'},
        'spacing': {'padding': {'left': P(40), 'right': P(40)}, 'blockGap': P(30)},
        'elements': {
            'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': C('accent')}},
                     ':focus': {'outline': {'color': C('accent'), 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'lineHeight': '1', 'letterSpacing': '-0.03em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '500'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '500', 'lineHeight': '1.15'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500', 'lineHeight': '1.4', 'letterSpacing': '0'}, 'color': {'text': C('muted')}},
            'button': {'color': {'background': C('contrast'), 'text': C('base')}, 'border': {'radius': '0', 'width': '0', 'style': 'solid'},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.25em', 'right': '1.25em'}},
                       ':hover': {'color': {'background': C('accent'), 'text': C('contrast')}},
                       ':focus': {'outline': {'color': C('accent'), 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': C('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.02em', 'lineHeight': '1'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent')}}}}},
            'core/post-title': {'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}, ':hover': {'color': {'text': C('accent')}}}}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small'}, 'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': C('accent')}}}}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': C('muted')}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': C('muted')}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': C('line')}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '500', 'lineHeight': '1.3'},
                           'border': {'left': {'color': C('accent'), 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'left': P(30)}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(20), 'bottom': P(20)}}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-title': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}},
        },
        'css': CSS,
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Rep
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A roster and portfolio site for small agencies that represent illustrators, animators and photographers and pitch them to publishers and brands.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: rep
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def variation(name, title, rows):
    jdump('styles/%s.json' % name, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}})
variation('salon', 'Salon', [('base', '#F4F0E8', 'Salon paper'), ('contrast', '#121212', 'Index black'), ('accent', '#B8391A', 'Vermilion'),
                             ('surface', '#EAE4D8', 'Proof'), ('line', '#121212', 'Rule'), ('muted', '#595650', 'Caption grey')])
variation('black-book', 'Black book', [('base', '#111111', 'Black book'), ('contrast', '#F2F2F0', 'Paper'), ('accent', '#FF6A3D', 'Vermilion'),
                                       ('surface', '#1C1C1B', 'Proof'), ('line', '#F2F2F0', 'Rule'), ('muted', '#B3B3AE', 'Caption grey')])
variation('primary', 'Primary', [('base', '#FFFFFF', 'Paper'), ('contrast', '#121212', 'Index black'), ('accent', '#1E3FD0', 'Primary blue'),
                                 ('surface', '#EEF1FB', 'Proof'), ('line', '#121212', 'Rule'), ('muted', '#55565C', 'Caption grey')])

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})
section('index-grid', 'Index grid (dense, 4:5 tiles)', ['core/post-template'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('native-grid', 'Native-ratio grid', ['core/post-template'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('roster', 'Roster (names list)', ['core/categories'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('filter-row', 'Filter link', ['core/paragraph'], {'typography': {'fontSize': 'var:preset|font-size|medium'}})
section('style-index', 'Style index', ['core/tag-cloud'], {'typography': {'fontWeight': '500'}})
section('ruled-row', 'Ruled row', ['core/group'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('stack', 'Stacks on phones', ['core/table'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {'border': {'top': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(20)}, 'margin': {'top': P(60)}}})
section('rule-bottom', 'Rule below', ['core/group'], {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}})
section('enquire', 'Enquiry band', ['core/group'], {'color': {'background': C('accent'), 'text': C('contrast')},
    'elements': {'link': {'color': {'text': C('contrast')}}, 'heading': {'color': {'text': C('contrast')}},
                 'button': {'color': {'background': C('contrast'), 'text': C('base')}, ':hover': {'color': {'background': C('base'), 'text': C('contrast')}}}},
    'spacing': {'padding': {'top': P(60), 'bottom': P(60)}}})
section('proof', 'Proof panel', ['core/group'], {'color': {'background': C('surface'), 'text': C('contrast')}, 'spacing': {'padding': {'top': P(40), 'bottom': P(40), 'left': P(40), 'right': P(40)}}})

# ---------------------------------------------------------------- patterns
tile = J(dyn('post-featured-image', isLink=True, sizeSlug='medium'),
         dyn('post-title', isLink=True, level=3, fontSize='small', style={'typography': {'fontWeight': '500', 'letterSpacing': '0'}}),
         dyn('post-terms', term='category', separator=', ', fontSize='x-small'),
         dyn('post-excerpt', excerptLength=8, moreText=''))
ntile = tile.replace('"sizeSlug":"medium"', '"sizeSlug":"large"')

def rows(data, top=True):
    return group(J(*[row(J(*[para(c) for c in r]), className='is-style-ruled-row') for r in data]), layout={'type': 'default'},
                 style={'spacing': {'blockGap': '0'}, 'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}} if top else {'spacing': {'blockGap': '0'}})

pattern('intro-line', 'Hero: agency name and one fact', 'hero', group(J(
    row(J(heading('Holloway Pask', 1, fontSize='xx-large'),
          para('Agents for seven illustrators, one animator and one photographer. Tabernacle Street, London, since 2009. <a href="/contact/">Commission an artist</a>', fontSize='small', style={'layout': {'selfStretch': 'fixed', 'flexSize': '32rem'}})),
        justify='space-between', align='wide', style={'spacing': {'blockGap': P(40)}})),
    tag='section', align='full', layout={'type': 'constrained'}, style=pad(50, 30)),
    description='A name and one fact, then straight into the work.')

pattern('intro-statement', 'Hero: what the agency does, in one line', 'hero', group(J(
    heading('Illustration, animation and photography for books, packaging, editorial and advertising', 1, fontSize='xx-large', align='wide'),
    para('Holloway Pask, Tabernacle Street, London', fontSize='small', textColor='muted', align='wide')),
    tag='section', align='full', layout={'type': 'constrained'}, style=pad(60, 50)))

pattern('discipline-filter', 'Discipline filter (Illustration, Animation, Photography)', 'portfolio', group(
    row(J(para('Show', textColor='muted'), para('<a href="/work/">All work</a>', className='is-style-filter-row'), para('<a href="/tag/illustration/">Illustration</a>', className='is-style-filter-row'),
          para('<a href="/tag/animation/">Animation</a>', className='is-style-filter-row'), para('<a href="/tag/photography/">Photography</a>', className='is-style-filter-row'),
          para('<a href="/styles/">By style</a>', className='is-style-filter-row')), justify='left', style={'spacing': {'blockGap': P(40)}}),
    align='wide', className='is-style-rule-bottom', layout={'type': 'default'}, style={'spacing': {'padding': {'bottom': P(20)}, 'margin': {'bottom': P(40)}}}),
    description='Disciplines are tags (Illustration, Animation, Photography), so each link opens a tag page.')

pattern('works-index', 'Works index: latest fourteen, each credited', 'portfolio,query', group(J(
    pattern_ref('discipline-filter'),
    query(tile, per_page=14, template_class='is-style-index-grid', align='wide', no_results='No work yet.')),
    align='wide', layout={'type': 'default'}), keywords='work, grid, index')
pattern('works-index-archive', 'Works index (inherits the page query)', 'portfolio,query', inherit_query(tile, template_class='is-style-index-grid', align='wide'), inserter=False)
pattern('works-native-archive', 'Artist works at their own ratio (inherits the page query)', 'portfolio,query', inherit_query(ntile, template_class='is-style-native-grid', align='wide'), inserter=False)

pattern('roster-names', 'Roster: artist names as a list, grouped by discipline', 'portfolio', group(J(
    heading('The roster', 6),
    dyn('categories', className='is-style-roster')),
    align='wide', layout={'type': 'default'}), description='The names double as the filter: each opens that artist\'s page.')

roster = [('Ines Carvalho', 'map-2.jpg', 'Bird\'s-eye engraving of Venice with its canals, islands and lagoon', '/category/ines-carvalho/'),
          ('Tomasz Wrona', 'arch-1.jpg', 'Etching of an Egyptian obelisk in a Roman square under a cloudy sky', '/category/tomasz-wrona/'),
          ('Hattie Blume', 'bot-1.jpg', 'Hand-coloured botanical plate of yellow loosestrife with leaves and seed heads', '/category/hattie-blume/'),
          ('Kenji Arai', 'poster-1.jpg', 'Travel poster of white sea cliffs and pine trees with red and blue Japanese lettering', '/category/kenji-arai/')]
pattern('roster-grid', 'Roster grid: one image and a name per artist', 'portfolio', group(J(
    heading('Some of the roster', 3),
    group(J(*[stack(J(image(f, alt, href=u, aspectRatio='4/5', scale='cover'), para('<a href="%s">%s</a>' % (u, n), style={'typography': {'fontWeight': '500'}})), style={'spacing': {'blockGap': P(20)}})
              for n, f, alt, u in roster]), layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '10rem'})),
    align='wide', layout={'type': 'default'}))

styles_list = [('Maps', 'maps', 'map-1.jpg', 'Picture map of the Baltic Sea with small drawings of ports and ships'),
               ('Architecture', 'architecture', 'arch-2.jpg', 'Ink and wash drawing of a domed chapel with plan, section and elevation'),
               ('Botanical', 'botanical', 'bot-1.jpg', 'Hand-coloured botanical plate of yellow loosestrife'),
               ('Characters', 'characters', 'char-1.jpg', 'Woodblock triptych of figures in patterned robes on a rocky shore'),
               ('Black and white', 'black-and-white', 'bw-2.jpg', 'Bold black and white linocut of a stylised figure in striped patterns'),
               ('Posters', 'posters', 'poster-2.jpg', 'Lithograph poster of a dancer in a crowded hall with red lettering')]
pattern('style-index', 'Browse by style (image index)', 'portfolio', group(J(
    row(J(heading('Browse by style', 2, fontSize='x-large'), para('<a href="/styles/">Every style and subject</a>', fontSize='small')), justify='space-between'),
    group(J(*[stack(J(image(f, alt, href='/tag/%s/' % s, aspectRatio='1', scale='cover'), para('<a href="/tag/%s/">%s</a>' % (s, n), fontSize='large', style={'typography': {'fontWeight': '500'}})), style={'spacing': {'blockGap': P(20)}})
              for n, s, f, alt in styles_list]), layout={'type': 'grid', 'columnCount': 6, 'minimumColumnWidth': '9rem'})),
    align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    description='The signature: every style page pulls work from the whole roster, credited to its artist.')

pattern('style-cloud', 'Every style and subject (text index)', 'portfolio', group(J(
    heading('Styles and subjects', 6), dyn('tag-cloud', className='is-style-style-index', smallestFontSize='1rem', largestFontSize='1rem')),
    align='wide', layout={'type': 'default'}))

pattern('quote-checklist', 'What we need to quote', 'services', columns(
    ('33%', J(heading('What we need to quote', 3), para('Send these five things and we can come back with a price and availability within a day.', fontSize='small'))),
    ('67%', rows([['Usage', 'Where it will appear: cover, packaging, social, outdoor, film'],
                  ['Territory', 'UK only, Europe, worldwide'],
                  ['Duration', 'How long you want to use it: one year, five years, in perpetuity'],
                  ['Deadline', 'When you need roughs and when you need finals'],
                  ['Budget', 'A range is fine. It tells us which artists to suggest']])),
    align='wide', className='is-style-rule-top'), description='The five things an agent needs before quoting a commission.')

agents = [('Priya Raman', 'Books, publishing and editorial', 'priya@example.com', '020 7946 0321'),
          ('Jonah Feld', 'Advertising, packaging and animation', 'jonah@example.com', '020 7946 0322'),
          ('Marta Kowalczyk', 'Licensing, Europe, and anything in Polish or German', 'marta@example.com', '020 7946 0323')]
pattern('agent-contacts', 'Agents with direct email and phone', 'contact', group(J(
    heading('Talk to an agent', 3),
    rows([[n, r, '<a href="mailto:%s">%s</a>' % (e, e), '<a href="tel:+44%s">%s</a>' % (t.replace(' ', '')[1:], t)] for n, r, e, t in agents])),
    layout={'type': 'default'}), description='Named agents with a direct email and phone number, for the foot of every artist page.')

pattern('commission-artist', 'Commission this artist (enquiry band)', 'call-to-action', group(J(
    heading('Commission an artist', 2, fontSize='x-large'),
    columns((None, para('Tell us the artist, the job and the deadline. Priya handles books and editorial, Jonah handles advertising, packaging and animation. We answer the same day, London time.')),
            (None, J(para('<a href="mailto:priya@example.com">priya@example.com</a><br><a href="tel:+442079460321">020 7946 0321</a>'),
                     para('<a href="mailto:jonah@example.com">jonah@example.com</a><br><a href="tel:+442079460322">020 7946 0322</a>'))))),
    tag='section', align='full', className='is-style-enquire', layout={'type': 'constrained', 'wideSize': '1480px'}))

pattern('artist-hero', 'Artist introduction', 'portfolio', columns(
    ('58%', J(heading('Ines Carvalho', 2, fontSize='display'),
              para('Ines Carvalho (b. 1987, Porto) draws maps and bird\'s-eye views of towns, mostly in ink with a flat second colour. She lives in Lisbon and has worked with us since 2016.', fontSize='large'))),
    ('42%', rows([['Disciplines', 'Illustration, maps'], ['Based', 'Lisbon, one hour ahead of London'], ['Clients', 'Faber, The Financial Times, Porto Tourism, Monocle'], ['Agent', 'Priya Raman']])),
    align='wide', verticalAlignment='bottom'))

pattern('recent-commissions', 'Recent commissions list (client, artist, year)', 'portfolio', group(J(
    heading('Recent commissions', 3),
    rows([['Faber', 'Ines Carvalho', 'Endpaper map for a novel set in the Azores', '2026'],
          ['Kew Gardens shop', 'Hattie Blume', 'Seed packet range, twelve plants', '2026'],
          ['The Guardian Weekend', 'Tomasz Wrona', 'Cover, the new Kraków tram depot', '2025'],
          ['Muji Europe', 'Kenji Arai', 'Christmas window characters', '2025'],
          ['BBC Four', 'Leo Hartigan', 'Title sequence, twelve seconds of galloping', '2025']])),
    align='wide', className='is-style-rule-top', layout={'type': 'default'}))

pattern('about-agency', 'About the agency', 'about', columns(
    ('58%', J(para('Holloway Pask was started in 2009 by Ruth Holloway, who had been an art buyer at a publisher for twelve years, and Daniel Pask, an illustrator who hated doing his own invoices.', fontSize='large'),
              para('We represent nine artists and turn down about forty a year. We would rather have a short roster we can keep busy than a long one we can\'t. Every artist has one agent who knows their work, their rates and when they are on holiday.'),
              para('We take 25% on commissions and 30% on licensing. We do not charge artists to join and we don\'t run competitions.'))),
    ('42%', J(heading('Office', 6), para('3rd floor, 21 Tabernacle Street<br>London EC2A 4DE<br>Monday to Friday, 9.30 to 6'), heading('Languages', 6), para('English, Polish, German, Portuguese and some French'))),
    align='wide'))

pattern('about-languages', 'About in other languages', 'about', group(J(
    heading('In other languages', 3),
    details('Deutsch', para('Holloway Pask ist eine Illustrationsagentur in London. Wir vertreten sieben Illustratorinnen und Illustratoren, einen Animator und eine Fotografin. Anfragen auf Deutsch beantwortet Marta Kowalczyk: marta@example.com.')),
    details('Français', para('Holloway Pask est une agence d\'illustrateurs basée à Londres. Nous représentons neuf artistes pour l\'édition, la presse, l\'emballage et la publicité. Écrivez à priya@example.com, nous répondons en anglais ou en français.')),
    details('Português', para('A Holloway Pask é uma agência de ilustração em Londres. Representamos nove artistas, entre eles a Ines Carvalho, de Lisboa. Pedidos em português: priya@example.com.')),
    details('Polski', para('Holloway Pask to agencja ilustratorów w Londynie. Reprezentujemy dziewięcioro artystów. Zapytania po polsku: marta@example.com, tel. 020 7946 0323.'))),
    layout={'type': 'default'}), description='A short version of the about page for international clients.')

pattern('interview', 'Studio visit (interview)', 'text', group(J(
    heading('Studio visit: Tomasz Wrona', 3),
    para('Tomasz draws buildings in Kraków from a desk that faces a tram depot. We asked him three things.', fontSize='large'),
    heading('How long does a cover take?', 5), para('Two days of drawing and a week of looking. I walk past the building at different times before I start.'),
    heading('Do you use photos?', 5), para('For proportions, yes. For light, never. Photos flatten everything.'),
    heading('What would you never draw?', 5), para('Shopping centres. I have tried twice.')),
    layout={'type': 'constrained'}))

pattern('news-list', 'Agency news (text list)', 'text', group(J(
    heading('News', 3),
    rows([['September 2026', 'Hattie Blume\'s seed packets are in every Kew Gardens shop.'],
          ['August 2026', 'Leo Hartigan joins the roster for animation and title sequences.'],
          ['June 2026', 'Ines Carvalho wins the V&A Illustration Award for book illustration.']])),
    align='wide', className='is-style-rule-top', layout={'type': 'default'}))

pattern('notice-portfolio-review', 'Notice: portfolio reviews', 'banner', group(
    para('We review new portfolios twice a year. The next window is 1 to 14 November. Send a PDF of up to 15 images to <a href="mailto:new@example.com">new@example.com</a>. We reply to everyone by 15 December.', fontSize='small'),
    tag='aside', align='full', className='is-style-proof', layout={'type': 'constrained'}, style=pad(20)),
    description='Change the dates each round and remove it when the window closes.')

pattern('work-facts', 'Work facts (artist, client, styles)', 'portfolio', group(J(
    row(J(para('Artist', textColor='muted', fontSize='small'), dyn('post-terms', term='category', separator=', ')), wrap=False),
    row(J(para('Client and year', textColor='muted', fontSize='small'), dyn('post-excerpt', moreText='')), wrap=False),
    row(J(para('Styles', textColor='muted', fontSize='small'), dyn('post-terms', term='post_tag', separator=', ')), wrap=False)),
    className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'blockGap': P(10), 'margin': {'top': '0'}}}), inserter=False)

pattern('animation-intro', 'Animation roster intro', 'portfolio', group(J(
    para('Animation is a separate roster with its own agent, Jonah Feld. Our animators work on title sequences, idents and short social films, usually 6 to 30 seconds. Budgets start at £4,000 for a looping ident.', fontSize='large')),
    layout={'type': 'constrained'}))

pattern('rates-note', 'How fees work', 'services', columns(
    ('33%', heading('How fees work', 3)),
    ('67%', J(para('Every fee has two parts: a design fee for the time, and a licence for the use. A book cover in the UK for seven years usually costs £900 to £1,800. A packaging range is quoted per design. We send a written quote before anyone starts drawing.'),
              para('Roughs are included. If a job is cancelled after roughs, we charge 25% of the fee. After finals, 100%.', fontSize='small'))),
    align='wide', className='is-style-rule-top'))

pattern('animator-profile', 'Animator profile with rates', 'portfolio', columns(
    ('50%', image('anim-1.jpg', 'Sequence of sixteen photographs of a horse and rider galloping, in three rows', 'Galloping, sixteen frames, BBC Four titles, 2025')),
    ('50%', J(heading('<a href="/category/leo-hartigan/">Leo Hartigan</a>', 2, fontSize='x-large'),
              para('Leo animates frame by frame from photographs and drawings, usually at 12 frames a second. He works from a shed in Bristol and delivers ProRes and looping MP4s.'),
              rows([['Clients', 'BBC Four, Aardman shop, Bristol Old Vic'], ['Ident, up to 10 seconds', 'From £4,000'], ['Title sequence', 'From £9,000'], ['Lead time', 'Four to eight weeks']]),
              para('<a href="/tag/animation/">All animation work</a>', style={'typography': {'fontWeight': '500'}}))),
    align='wide', style={'spacing': {'blockGap': {'left': P(50)}}}))


# ---------------------------------------------------------------- project stories and more (round 2)
pattern('project-brief', 'Project: the brief', 'project', columns(
    ('33%', heading('The brief', 4)),
    ('67%', J(para('Faber wanted an endpaper map for a novel that moves between nine Baltic ports over forty years. It had to work in black only for the paperback and in two colours for the hardback.'),
              para('Deadline: roughs in two weeks, finals in five. Licence: world, all editions, seven years.', fontSize='small'))),
    align='wide', className='is-style-rule-top'))

pattern('project-roughs', 'Project: roughs next to the final', 'project', gallery([
    ('map-2.jpg', "Bird's-eye engraving of Venice with its canals, islands and lagoon", 'Style reference Ines sent with the roughs'),
    ('map-1.jpg', 'Picture map of the Baltic Sea with small drawings of ports and ships', 'Final, two colours')], columns=2, align='wide'))

pattern('project-in-use', 'Project: the work in use', 'project', columns(
    ('58%', image('bot-1.jpg', 'Hand-coloured botanical plate of yellow loosestrife with leaves and seed heads', 'The painting, at twice print size')),
    ('42%', J(heading('On the shelf', 4), para('Printed at 85 mm wide on uncoated card, twelve plants, sold in every Kew Gardens shop from March. Hattie painted each plant from specimens in the herbarium.'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': P(50)}}}))

pattern('project-credits', 'Project: credits and licence', 'project', group(J(
    heading('Credits', 6),
    rows([['Artist', 'Ines Carvalho'], ['Client', 'Faber'], ['Art director', 'Hannah Moore'], ['Agent', 'Priya Raman'], ['Licence', 'World, all editions, seven years']])),
    layout={'type': 'constrained'}))

pattern('project-quote', 'Project: the art director, quoted', 'project', group(
    quote('We sent a list of nine ports and got back a map people photograph in bookshops.', 'Hannah Moore, art director, Faber, 2026'), layout={'type': 'constrained'}))

pattern('project-baltic', 'Project layout: Baltic ports endpaper', 'project', J(
    pattern_ref('project-brief'), pattern_ref('project-roughs'), pattern_ref('project-quote'), pattern_ref('project-credits')),
    block_types='core/post-content', description='A complete project page built from the project patterns.')

pattern('project-seed-packets', 'Project layout: seed packets', 'project', J(
    para('Twelve seed packets for the Kew Gardens shops, painted in watercolour from herbarium specimens.', fontSize='large'),
    pattern_ref('project-in-use'),
    group(J(heading('Credits', 6), rows([['Artist', 'Hattie Blume'], ['Client', 'Kew Gardens shop'], ['Agent', 'Jonah Feld'], ['Licence', 'Packaging, UK and EU, five years']])), layout={'type': 'constrained'})),
    block_types='core/post-content')

pattern('project-titles', 'Project layout: title sequence', 'project', J(
    para('Twelve seconds of galloping for a BBC Four history series, sixteen frames on a loop.', fontSize='large'),
    image('anim-1.jpg', 'Sequence of sixteen photographs of a horse and rider galloping, in three rows', 'The reference sequence Leo animated over', align='wide'),
    columns((None, J(heading('How', 5), para('Leo traced each frame by hand at 12 frames a second, then scanned the drawings and cleaned them on a lightbox app.'))),
            (None, J(heading('Delivered', 5), para('ProRes 4444 with alpha, a 1080 square loop for social, and the sixteen drawings, which the director bought.'))), align='wide'),
    group(J(heading('Credits', 6), rows([['Animator', 'Leo Hartigan'], ['Client', 'BBC Four'], ['Agent', 'Jonah Feld']])), layout={'type': 'constrained'})),
    block_types='core/post-content')

pattern('project-cover', 'Project layout: a book cover', 'project', J(
    columns(('42%', image('bw-2.jpg', 'Bold black and white linocut of a stylised figure in striped patterns')),
            ('58%', J(heading('Cut at 1:1', 3), para('Sade cut the cover at the size it prints, 129 x 198 mm, so every mark on the book is a mark on the block. It took nine days and one new blade.'),
                      pattern_ref('project-quote'))), align='wide', verticalAlignment='center'),
    group(J(heading('Credits', 6), rows([['Artist', 'Sade Olatunji'], ['Client', 'Penguin Modern Classics'], ['Agent', 'Priya Raman'], ['Licence', 'World, all editions, ten years']])), layout={'type': 'constrained'})),
    block_types='core/post-content')

pattern('artist-feature', 'Featured artist (large image and short bio)', 'portfolio', columns(
    ('58%', image('char-1.jpg', 'Woodblock triptych of figures in patterned robes on a rocky shore', 'Sunrise at the bay, Muji Europe windows, 2025')),
    ('42%', J(para('Artist of the month', textColor='muted', fontSize='small'), heading('<a href="/category/kenji-arai/">Kenji Arai</a>', 2),
              para('Characters and landscapes in flat colour, for packaging and posters. Manchester. Available from November.'),
              para('<a href="/category/kenji-arai/">See Kenji\'s work</a>', style={'typography': {'fontWeight': '500'}}))),
    align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': P(50)}}}))

pattern('licensing-note', 'Licensing existing work', 'services', columns(
    ('33%', heading('Licensing existing work', 3)),
    ('67%', J(para('Most of the work on this site can be licensed as it is, for a cover, a print run or a campaign. It is quicker and usually cheaper than a commission. Marta handles licensing and replies within a day.'),
              para('<a href="mailto:marta@example.com?subject=Licensing">marta@example.com</a>', style={'typography': {'fontWeight': '500'}}))),
    align='wide', className='is-style-rule-top'))

pattern('art-buyer-letter', 'Newsletter for art buyers', 'call-to-action', group(J(
    heading('Six new pieces a month, by email', 4),
    para('For art directors and buyers only. One email on the first Monday of the month. Ask Priya to add you at <a href="mailto:priya@example.com?subject=Monthly%20email">priya@example.com</a>.')),
    className='is-style-proof', layout={'type': 'default'}))

pattern('availability', 'Who is free this month', 'portfolio', group(J(
    heading('Free to start in October', 4),
    rows([['<a href="/category/kenji-arai/">Kenji Arai</a>', 'From 6 October'], ['<a href="/category/sade-olatunji/">Sade Olatunji</a>', 'From 13 October'], ['<a href="/category/leo-hartigan/">Leo Hartigan</a>', 'Short jobs only until December']])),
    layout={'type': 'default'}), description='A short availability list, updated monthly by the agents.')

pattern('pdf-portfolio', 'Ask for a PDF portfolio', 'call-to-action', group(
    para('Want a PDF of one artist, or of every map we have ever made? Ask Priya and it arrives the same day, sized for email.', fontSize='large'),
    className='is-style-rule-top', layout={'type': 'default'}))

# pages
pattern('page-animation', 'Page: animation roster', 'portfolio', J(pattern_ref('animation-intro'), pattern_ref('animator-profile'), pattern_ref('quote-checklist'), pattern_ref('commission-artist')), block_types='core/post-content')
pattern('page-artists', 'Page: artists (roster)', 'portfolio', J(pattern_ref('roster-names'), pattern_ref('availability'), pattern_ref('artist-feature'), pattern_ref('roster-grid'), pattern_ref('commission-artist')), block_types='core/post-content')
pattern('page-styles', 'Page: styles and subjects', 'portfolio', J(para('Every style page pulls work from the whole roster, with the artist and client under each image.', fontSize='large'), pattern_ref('style-cloud'), pattern_ref('style-index')), block_types='core/post-content')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('about-agency'), pattern_ref('rates-note'), pattern_ref('licensing-note'), pattern_ref('art-buyer-letter'), pattern_ref('news-list'), pattern_ref('interview'), pattern_ref('about-languages')), block_types='core/post-content')
pattern('page-contact', 'Page: contact', 'contact', J(para('Ring or email the agent for the kind of job you have. We don\'t use a contact form.', fontSize='large'), pattern_ref('agent-contacts'), pattern_ref('quote-checklist'),
    columns((None, J(heading('Office', 5), para('3rd floor, 21 Tabernacle Street<br>London EC2A 4DE<br>Old Street station, exit 4, then five minutes south'))),
            (None, J(heading('Artists who want representing', 5), para('Portfolio reviews twice a year. Send a PDF of up to 15 images to <a href="mailto:new@example.com">new@example.com</a> in May or November.'))), align='wide', className='is-style-rule-top')),
    block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')), justify='space-between', align='wide'),
    tag='header', align='full', className='is-style-rule-bottom', style=pad(30)))
write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0, fontSize='x-large'), para('An agency for illustrators, animators and photographers. Tabernacle Street, London, since 2009.', fontSize='small'))),
        (None, J(heading('Books and editorial', 6), para('Priya Raman<br><a href="mailto:priya@example.com">priya@example.com</a><br>020 7946 0321', fontSize='small'))),
        (None, J(heading('Advertising and animation', 6), para('Jonah Feld<br><a href="mailto:jonah@example.com">jonah@example.com</a><br>020 7946 0322', fontSize='small'))),
        align='wide'),
    para('Demo images are public domain prints, drawings and photographs from the Metropolitan Museum of Art, the National Gallery of Art and Wikimedia Commons, standing in for the artists\' work. The artists are invented.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-rule-top', style={'spacing': {'padding': {'top': P(40), 'bottom': P(40)}, 'margin': {'top': '0'}}}))
write('parts/notice.html', pattern_ref('notice-portfolio-review'))

# ---------------------------------------------------------------- templates
def tpl(name, inner, top=50, bottom=70):
    write('templates/%s.html' % name, page_template(inner, style=pad(top, bottom)))

write('templates/front-page.html', page_template(J(
    pattern_ref('intro-line'), pattern_ref('works-index'),
    group(pattern_ref('roster-names'), align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    pattern_ref('style-index'), pattern_ref('artist-feature'), pattern_ref('recent-commissions'), spacer(), pattern_ref('commission-artist')), style={'spacing': {'padding': {'bottom': '0'}}}))
tpl('home', J(heading('All work', 1, align='wide'), pattern_ref('discipline-filter'), pattern_ref('works-index-archive')))
tpl('category', J(
    dyn('query-title', type='archive', showPrefix=False, align='wide'),
    dyn('term-description', align='wide', fontSize='large'),
    pattern_ref('discipline-filter'),
    pattern_ref('works-native-archive'),
    pattern_ref('agent-contacts'), pattern_ref('quote-checklist')))
tpl('tag', J(
    row(J(para('Style, subject or discipline', textColor='muted'), para('<a href="/styles/">All styles</a>', fontSize='small')), justify='space-between', align='wide'),
    dyn('query-title', type='archive', showPrefix=False, align='wide'),
    dyn('term-description', align='wide', fontSize='large'),
    pattern_ref('works-index-archive'), pattern_ref('style-cloud'), pattern_ref('quote-checklist')))
tpl('archive', J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('works-index-archive')))
tpl('index', J(dyn('query-title', type='archive', align='wide'), pattern_ref('works-index-archive')))
tpl('search', J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Maps, botanical, a name', buttonText='Search', align='wide'), pattern_ref('works-index-archive')))
tpl('404', J(heading('Nobody here by that name', 1), para('The artist may have moved on, or the link is old. The <a href="/artists/">roster</a> has everyone we represent now.'),
             dyn('search', label='Search', showLabel=False, placeholder='Maps, botanical, a name', buttonText='Search')))
tpl('page', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained'})))
tpl('page-wide', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1480px'})))
tpl('single', J(
    columns(('66%', dyn('post-featured-image', sizeSlug='full')),
            ('34%', J(dyn('post-title', level=1, fontSize='xx-large'), pattern_ref('work-facts'), dyn('post-content'),
                      para('<a href="/contact/">Ask about this artist</a>', style={'typography': {'fontWeight': '500'}}))),
            align='wide', style={'spacing': {'blockGap': {'left': P(50)}}}),
    group(row(J(dyn('post-navigation-link', type='previous', label='Previous by this artist', showTitle=True, taxonomy='category'),
                dyn('post-navigation-link', label='Next by this artist', showTitle=True, taxonomy='category')), justify='space-between'),
          align='wide', className='is-style-rule-top', layout={'type': 'default'})), top=40)
print('rep built')

# ---------------------------------------------------------------- demo content
artists = [
    ('ines-carvalho', 'Ines Carvalho', 'illustration', 'Maps and bird\'s-eye views of towns, in ink with a flat second colour. Lisbon. Agent: Priya Raman.'),
    ('tomasz-wrona', 'Tomasz Wrona', 'illustration', 'Buildings, drawn from the street in etching-style line. Kraków. Agent: Priya Raman.'),
    ('hattie-blume', 'Hattie Blume', 'illustration', 'Plants, seeds and ornament in watercolour. Glasgow. Agent: Jonah Feld.'),
    ('kenji-arai', 'Kenji Arai', 'illustration', 'Characters and landscapes in flat colour, for packaging and posters. Manchester. Agent: Jonah Feld.'),
    ('odile-marchetti', 'Odile Marchetti', 'illustration', 'Crowds, cats and nightlife in loose lithographic line. Marseille. Agent: Marta Kowalczyk.'),
    ('sade-olatunji', 'Sade Olatunji', 'illustration', 'Black and white linocut, pattern-heavy portraits. London. Agent: Priya Raman.'),
    ('pim-de-groot', 'Pim de Groot', 'illustration', 'Painted city streets at night. Rotterdam. Agent: Marta Kowalczyk.'),
    ('leo-hartigan', 'Leo Hartigan', 'animation', 'Frame-by-frame motion studies and title sequences. Bristol. Agent: Jonah Feld.'),
    ('maeve-doherty', 'Maeve Doherty', 'photography', 'Documentary photography of work and weather, in black and white. Belfast. Agent: Jonah Feld.'),
]
works = [
    ('Baltic ports, endpaper map', 'ines-carvalho', 'map-1.jpg', 'Faber, 2026', ['Maps'], 'Endpaper for a novel that moves between nine Baltic ports. Each port is drawn from its harbour side.'),
    ('Venice from above', 'ines-carvalho', 'map-2.jpg', 'Monocle, 2025', ['Maps', 'Architecture'], 'A fold-out for the Venice city guide, drawn at 1:2,500 and printed on uncoated stock.'),
    ('Obelisk, Piazza del Popolo', 'tomasz-wrona', 'arch-1.jpg', 'The Guardian Weekend, 2025', ['Architecture', 'Black and white'], 'Cover for a travel feature. Drawn on site over three mornings.'),
    ('Chapel and hospital, plan and section', 'tomasz-wrona', 'arch-2.jpg', 'RIBA Journal, 2025', ['Architecture'], 'Plan, section and elevation on one sheet, for a feature on hospital chapels.'),
    ('Loosestrife, seed packet', 'hattie-blume', 'bot-1.jpg', 'Kew Gardens shop, 2026', ['Botanical'], 'One of twelve seed packets. Painted at twice size, printed at 85 mm wide.'),
    ('Catalogue cover frame', 'hattie-blume', 'book-1.jpg', 'Hirsch Books, 2024', ['Botanical', 'Black and white'], 'An ornamental frame for an antiquarian bookseller\'s catalogue, left empty for the title.'),
    ('Sunrise at the bay, window triptych', 'kenji-arai', 'char-1.jpg', 'Muji Europe, 2025', ['Characters'], 'Three window panels for the Christmas display, 2.4 metres wide in total.'),
    ('Sea cliffs, rail poster', 'kenji-arai', 'poster-1.jpg', 'Osaka Railway Heritage Trust, 2024', ['Posters', 'Characters'], 'A poster for a reopened coastal line. Four colours, screenprinted.'),
    ('Dance hall, festival poster', 'odile-marchetti', 'poster-2.jpg', 'Fiesta des Suds, 2025', ['Posters', 'Characters'], 'Main poster for the festival. The crowd is drawn from photos of the 2024 edition.'),
    ('The cat on the sofa, exhibition poster', 'odile-marchetti', 'char-2.jpg', 'Cercle des Arts, 2024', ['Posters', 'Characters'], 'Poster for an exhibition of animal artists. The cat belongs to the curator.'),
    ('Pattern portrait', 'sade-olatunji', 'bw-2.jpg', 'Penguin Modern Classics, 2026', ['Black and white', 'Characters'], 'Cover linocut, cut at 1:1 and scanned at 1,200 dpi.'),
    ('Night street, full moon', 'pim-de-groot', 'photo-1.jpg', 'Het Parool, 2025', ['Architecture'], 'Painted illustration for a long read about the city after midnight.'),
    ('Galloping, sixteen frames', 'leo-hartigan', 'anim-1.jpg', 'BBC Four, 2025', ['Animation', 'Black and white'], 'Title sequence for a history series. Twelve seconds, sixteen frames on a loop.'),
    ('Pea picker\'s camp', 'maeve-doherty', 'photo-2.jpg', 'Harvest Aid, 2024', ['Photography', 'Black and white'], 'Annual report cover for a farmworkers\' charity. Shot on film.'),
]
disc = {s_: p_.capitalize() for s_, n_, p_, d_ in artists}
posts = []
for i, (title, a, img_, client, tags, body) in enumerate(works):
    pat = {'Baltic ports, endpaper map': 'rep/project-baltic', 'Loosestrife, seed packet': 'rep/project-seed-packets', 'Galloping, sixteen frames': 'rep/project-titles', 'Pattern portrait': 'rep/project-cover'}.get(title)
    posts.append({'title': title, 'category': [a], 'tags': [disc[a]] + [t for t in tags if t not in ('Animation', 'Photography')], 'image': img_, 'excerpt': client, **({'pattern': pat} if pat else {'content': para(body)}), 'date': '2026-%02d-%02d' % (9 - i // 4, 20 - (i % 4) * 4)})

cats = [{'slug': s, 'name': n, 'description': d} for s, n, p, d in artists]
content = {
    'site': {'title': 'Holloway Pask', 'tagline': 'Illustration, animation and photography agents, London'},
    'categories': cats,
    'front_page': 'home', 'posts_page': 'work',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'work', 'title': 'Work', 'content': ''},
        {'slug': 'artists', 'title': 'Artists', 'pattern': 'rep/page-artists'},
        {'slug': 'styles', 'title': 'Styles', 'pattern': 'rep/page-styles'},
        {'slug': 'animation', 'title': 'Animation', 'pattern': 'rep/page-animation'},
        {'slug': 'about', 'title': 'About', 'pattern': 'rep/page-about'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'rep/page-contact'},
    ],
    'posts': posts,
    'nav': [{'label': 'Artists', 'url': '/artists/'}, {'label': 'Work', 'url': '/work/'}, {'label': 'Styles', 'url': '/styles/'},
            {'label': 'Animation', 'url': '/animation/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/rep', exist_ok=True)
json.dump(content, open('demos/rep/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
