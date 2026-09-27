# Design note (studio, idea 025, small branding studio)
# Direction: "wide-set studio sheet". A white sheet, black type and one studio orange used only for
#   the active filter and link underlines, so the client work carries all the colour.
# Fonts: Anybody (variable width). Headings at width 125 / weight 800, body at width 100, labels at width 75.
# Palette: #FFFFFF paper, #111111 type, #FF5A1F studio orange (fills, underlines), #F3F3F1 surface, #D9D9D6 rules.
# Layout idea: the work index is a 12-column sheet where cards alternate 8/4 and 4/8 spans (16:10 lead
#   next to 4:5 tiles, same height), under two ruled filter bars (Services, Industry) and a Selected / All switch.
import sys, json, os, shutil
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('studio')
S = THEME['slug']
D = THEME['dir']
for sub in ('patterns', 'templates', 'parts', 'styles'):
    shutil.rmtree(os.path.join(D, sub), ignore_errors=True)

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

P = lambda s: 'var:preset|spacing|%s' % s
pad = lambda t, b=None: {'spacing': {'padding': {'top': P(t), 'bottom': P(b or t)}}}

# ---------------------------------------------------------------- theme.json
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
fonts.append({'fontFamily': '"Anybody", sans-serif', 'name': 'Anybody (text)', 'slug': 'body'})

palette = [
    ('base', '#FFFFFF', 'Paper'), ('contrast', '#111111', 'Type'), ('accent', '#FF5A1F', 'Studio orange'),
    ('surface', '#F3F3F1', 'Proof'), ('line', '#D9D9D6', 'Rule'), ('muted', '#5C5C58', 'Pencil'),
]
pal = lambda rows: [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1440px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(palette),
                  'duotone': [{'slug': 'type-on-paper', 'colors': ['#111111', '#FFFFFF'], 'name': 'Type on paper'},
                              {'slug': 'orange-proof', 'colors': ['#111111', '#FF5A1F'], 'name': 'Orange proof'}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False, 'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Caption', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Label', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.6rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.75rem', 'name': 'Title', 'fluid': {'min': '2.2rem', 'max': '3.75rem'}},
                {'slug': 'display', 'size': '6.5rem', 'name': 'Display', 'fluid': {'min': '2.5rem', 'max': '6.5rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '400'},
        'spacing': {'padding': {'left': P(40), 'right': P(40)}, 'blockGap': P(30)},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '0.98', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '700', 'lineHeight': '1.05'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.15'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '700', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                       'border': {'radius': '0', 'width': '0', 'style': 'solid'},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.85em', 'bottom': '0.85em', 'left': '1.4em', 'right': '1.4em'}},
                       ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|contrast'}},
                       ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.02em', 'lineHeight': '1'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': 'var:preset|color|contrast'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': 'var:preset|color|contrast'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '700', 'lineHeight': '1.1'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '6px', 'style': 'solid'}}, 'spacing': {'padding': {'left': P(40)}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '800'},
                               'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(30), 'bottom': P(30)}}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'}},
            'core/social-links': {'css': '& a{color:inherit}'},
        },
        'css': (':where(h1,h2,h3,h4,.wp-block-site-title){font-stretch:125%;text-wrap:balance;overflow-wrap:break-word}'
                ':where(p){text-wrap:pretty}:where(h5,h6,figcaption,.wp-block-post-date,.wp-block-post-terms){font-stretch:75%}'
                'a{text-decoration-color:var(--wp--preset--color--accent);text-decoration-thickness:2px;text-underline-offset:.18em}'
                '.wp-block-navigation .current-menu-item>a{text-decoration:underline}'
                'html{font-synthesis:none}'
                '.is-style-person-row{border-top:1px solid var(--wp--preset--color--line);padding:.6rem 0;gap:.2rem 1.5rem!important}.is-style-person-row:last-child{border-bottom:1px solid var(--wp--preset--color--line)}'
                '.is-style-person-row>p{margin:0;flex:1 1 14rem}'
                '.is-style-type-sample{font-stretch:125%;line-height:.95;letter-spacing:-.02em;overflow-wrap:anywhere}'
                '.is-style-ruled-table table{border-collapse:collapse;width:100%}.wp-block-table.is-style-ruled-table td,.wp-block-table.is-style-ruled-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.6rem .75rem .6rem 0;text-align:left;vertical-align:top}'
                '.wp-block-table.is-style-ruled-table thead th{border-bottom:1px solid var(--wp--preset--color--contrast);font-stretch:75%;font-weight:500}.is-style-ruled-table td:first-child{font-weight:600}'
                '.wp-block-quote cite,.wp-block-pullquote cite{display:block;margin-top:.8rem;font-family:var(--wp--preset--font-family--body);font-size:var(--wp--preset--font-size--small);font-style:normal;font-weight:400;font-stretch:100%;letter-spacing:0}'
                '@media (max-width:600px){.wp-block-table.is-style-ruled-table thead{display:none}.wp-block-table.is-style-ruled-table tr{display:block;border-bottom:1px solid var(--wp--preset--color--line);padding:.5rem 0}.wp-block-table.is-style-ruled-table td{display:block;border:0;padding:0}.is-email{font-size:var(--wp--preset--font-size--large)!important}}'
                '.wp-block-post-template.is-style-work-sheet{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:var(--wp--preset--spacing--60) var(--wp--preset--spacing--40)}'
                '.is-style-work-sheet>li{grid-column:span 12;margin:0;min-width:0}'
                '.is-style-work-sheet .wp-block-post-featured-image{margin:0 0 .8rem}.is-style-work-sheet .wp-block-post-featured-image img{width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;display:block}'
                '@media (min-width:782px){.is-style-work-sheet>li{grid-column:span 4}.is-style-work-sheet>li:nth-child(7n+1),.is-style-work-sheet>li:nth-child(7n+4){grid-column:span 8}'
                '.is-style-work-sheet>li:nth-child(7n+1) .wp-block-post-featured-image img,.is-style-work-sheet>li:nth-child(7n+4) .wp-block-post-featured-image img{aspect-ratio:16/10}}'),
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, full sheet', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Studio
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A work index and case-study site for small branding and graphic design studios, with work filtered by service and industry.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: studio
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout, one-column
*/''')

# ---------------------------------------------------------------- variations + sections
def variation(name, title, rows, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % name, d)

variation('mono', 'Mono', [('base', '#FFFFFF', 'Paper'), ('contrast', '#111111', 'Type'), ('accent', '#111111', 'Type'),
                           ('surface', '#F1F1F1', 'Proof'), ('line', '#111111', 'Rule'), ('muted', '#4D4D4D', 'Pencil')])
variation('pastel', 'Pastel', [('base', '#F3E9F0', 'Blush'), ('contrast', '#1B1B24', 'Type'), ('accent', '#1F4E8C', 'Ballpoint blue'),
                               ('surface', '#EADCE6', 'Proof'), ('line', '#CDBFC9', 'Rule'), ('muted', '#56505A', 'Pencil')],
          {'elements': {'button': {':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}}}}})
variation('night', 'Night', [('base', '#121212', 'Night'), ('contrast', '#F5F5F0', 'Chalk'), ('accent', '#FF5A1F', 'Studio orange'),
                             ('surface', '#1E1E1C', 'Proof'), ('line', '#3A3A37', 'Rule'), ('muted', '#B4B4AC', 'Pencil')])

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('rule-bottom', 'Rule below', ['core/group'], {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(30)}, 'margin': {'top': P(60)}}})
section('filter-bar', 'Filter bar', ['core/group'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': P(20), 'bottom': P(20)}},
    'css': '&{align-items:baseline}& > p:first-child{min-width:7.5rem;font-stretch:75%;font-weight:500;margin:0}'})
section('switch', 'Selected or all switch', ['core/paragraph'], {
    'typography': {'fontWeight': '600'},
    'css': '& a{text-decoration:none;padding:.1em .45em;margin-right:.35em;color:inherit}& a:hover{text-decoration:underline}& strong{background:var(--wp--preset--color--accent);color:var(--wp--preset--color--contrast);padding:.1em .45em;margin-right:.35em;font-weight:600}'})
section('inline-terms', 'Inline terms', ['core/categories', 'core/tag-cloud'], {
    'typography': {'fontWeight': '500'},
    'css': '&{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.2rem .35rem;flex:1 1 0;min-width:0}& li{margin:0}& a{font-size:inherit!important;margin:0!important;text-decoration:none;color:inherit;padding:.1em .45em;display:inline-block}& a:hover{text-decoration:underline;text-decoration-color:var(--wp--preset--color--accent)}& .current-cat>a{background:var(--wp--preset--color--accent);color:var(--wp--preset--color--contrast)}'})
section('work-sheet', 'Work sheet (8/4 spans)', ['core/post-template'], {
    'css': '&{list-style:none;padding:0}& .wp-block-post-excerpt__more-text{display:none}'})
section('work-list', 'Work list (text index)', ['core/post-template'], {
    'css': '&{list-style:none;padding:0}& > li{border-top:1px solid var(--wp--preset--color--contrast);padding:.6rem 0;margin:0!important}& > li:last-child{border-bottom:1px solid var(--wp--preset--color--contrast)}'})
section('facts', 'Facts block', ['core/group'], {
    'typography': {'fontSize': 'var:preset|font-size|small'},
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': P(20)}, 'blockGap': P(10)},
    'css': '& > *{margin:0}& .wp-block-group{display:flex;gap:1rem;border-bottom:1px solid var(--wp--preset--color--line);padding-bottom:.4rem}& .wp-block-group > p:first-child{font-stretch:75%;min-width:6.5rem;color:var(--wp--preset--color--muted)}'})
section('sheet-invert', 'Inverted sheet', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                 'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}}},
    'css': '& .wp-block-site-title a{color:inherit}& .has-muted-color{color:var(--wp--preset--color--line)!important}'})
section('orange-bar', 'Orange bar', ['core/group'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|contrast'},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}},
    'typography': {'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
    'css': '& a{text-decoration-color:currentColor}'})
section('proof', 'Proof sheet', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': P(50), 'bottom': P(50), 'left': P(40), 'right': P(40)}, 'margin': {'top': P(60)}}})
section('person-row', 'Person row', ['core/group'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('type-sample', 'Type sample', ['core/paragraph'], {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|display', 'fontWeight': '800'}})
section('ruled-table', 'Ruled table', ['core/table'], {'typography': {'fontSize': 'var:preset|font-size|small'}})

# ---------------------------------------------------------------- patterns

pattern('hero-name-fact', 'Hero: studio name, one fact and what is on the desk', 'hero', group(J(
    heading('Sandvik Ogunleye', 1, align='wide'),
    columns(
        ('58%', para('Seven designers in a former print works on Mabgate, Leeds. Identities, packaging and signs for people who sell things you can hold or visit, since 2014.', fontSize='large')),
        ('42%', J(heading('On the desk this month', 6),
                  lst(['Six beer labels for a brewery in Kirkstall', 'Wayfinding for a library in Pudsey', 'The 2026 Leeds Print Fair poster']),
                  para('New work: <a href="mailto:work@example.com">work@example.com</a> or 0113 496 0721', fontSize='small'))),
        align='wide', style={'spacing': {'blockGap': {'left': P(60)}}})), tag='section', align='full', style=pad(60, 40), layout={'type': 'constrained'}),
    description='Opens with the name and one fact, then the current jobs. The work sheet follows directly below.')

pattern('hero-studio-line', 'Hero: what the studio does, in one wide line', 'hero', group(J(
    heading('Names, packs, signs and printed things for food, culture and public places', 1, align='wide'),
    columns(
        ('66.66%', ''),
        ('33.33%', J(para('Sandvik Ogunleye is seven people in a former print works on Mabgate, Leeds. We started in 2014 and still set most of our own type.'),
                     para('New work: <a href="mailto:work@example.com">work@example.com</a>, or call Ingrid on 0113 496 0721.', fontSize='small'))),
        align='wide')), tag='section', align='full', style=pad(70, 50), layout={'type': 'constrained'}))

def filter_bar(active):
    sw = ('<strong>Selected</strong><a href="/work/">All</a>' if active == 'selected' else
          '<a href="/category/selected/">Selected</a><strong>All</strong>' if active == 'all' else
          '<a href="/category/selected/">Selected</a><a href="/work/">All</a>')
    return group(J(
        row(J(para('Show'), para(sw, className='is-style-switch')), className='is-style-filter-bar', style={'spacing': {'blockGap': P(20)}}),
        row(J(para('Services'), dyn('categories', className='is-style-inline-terms')), className='is-style-filter-bar', wrap=False, style={'spacing': {'blockGap': P(20)}}),
        row(J(para('Industry'), dyn('tag-cloud', className='is-style-inline-terms')), className='is-style-filter-bar is-style-rule-bottom', wrap=False, style={'spacing': {'blockGap': P(20)}})),
        align='wide', layout={'type': 'default'}, style={'spacing': {'blockGap': '0', 'margin': {'bottom': P(50)}}})

pattern('filter-bar-all', 'Work filters (All active)', 'portfolio', filter_bar('all'), description='Selected / All switch plus Services and Industry filter rows. Services are categories, industries are tags.')
pattern('filter-bar-selected', 'Work filters (Selected active)', 'portfolio', filter_bar('selected'))
pattern('filter-bar', 'Work filters (neutral)', 'portfolio', filter_bar(None))

card = J(dyn('post-featured-image', isLink=True, sizeSlug='large'),
         dyn('post-title', isLink=True, level=3, fontSize='large'),
         dyn('post-excerpt', excerptLength=22, moreText=''))
pattern('work-sheet', 'Work sheet: latest seven projects in 8/4 spans', 'portfolio,query', group(J(
    pattern_ref('filter-bar'),
    query(card, per_page=7, template_class='is-style-work-sheet', align='wide', no_results='No projects yet.')),
    align='wide', layout={'type': 'default'}), keywords='work, grid, index')
pattern('work-sheet-archive', 'Work sheet (inherits the page query)', 'portfolio,query',
        inherit_query(card, template_class='is-style-work-sheet', align='wide'), inserter=False)
pattern('work-list', 'Work as a text index (title and one line)', 'portfolio,query', group(J(
    heading('Everything, as a list', 2, fontSize='x-large'),
    query(row(J(dyn('post-title', isLink=True, level=4, fontSize='medium'), dyn('post-excerpt', excerptLength=14, moreText=''), dyn('post-date', format='Y')), justify='space-between', wrap=True),
          per_page=30, query_id=3, template_class='is-style-work-list', align='wide')), align='wide', layout={'type': 'default'}))
pattern('post-list', 'Post list (search results)', 'posts,query', inherit_query(
    row(J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-date', format='Y')), justify='space-between'), template_class='is-style-work-list', align='wide'), inserter=False)

def facts_row(label, value):
    return row(J(para(label), value), wrap=False)
pattern('case-facts', 'Case study facts (year, services, industry)', 'portfolio', group(J(
    facts_row('Year', dyn('post-date', format='Y')),
    facts_row('Services', dyn('post-terms', term='category', separator=', ')),
    facts_row('Industry', dyn('post-terms', term='post_tag', separator=', '))),
    className='is-style-facts', layout={'type': 'default'}), inserter=False)

def fact_rows(rows, **kw):
    return group(J(*[row(J(para(k), para(v)), wrap=False) for k, v in rows]), className='is-style-facts', layout={'type': 'default'}, **kw)

pattern('case-credits', 'Case study credits', 'case-study', group(J(
    heading('Credits', 6),
    fact_rows([('Photography', 'Ade Okafor'), ('Sign painting', 'Beth Wray, Wray Letters'), ('Print', 'Footprint Workers Co-op, Leeds'), ('Studio team', 'Tunde Ogunleye, Maud Kessler, Rahim Chowdhury')])),
    layout={'type': 'constrained'}), description='Photographer, stylist, printer and partners on each project, as ruled rows.')

pattern('next-project', 'Next project link', 'portfolio', group(
    row(J(dyn('post-navigation-link', type='previous', label='Next project', showTitle=True, linkLabel=True, fontSize='x-large'),
          para('<a href="/work/">Back to all work</a>', fontSize='small')), justify='space-between'),
    align='wide', className='is-style-rule-top', layout={'type': 'default'}), inserter=False)

pattern('case-image-led', 'Case study: image-led with short text', 'portfolio', J(
    columns(
        ('58%', J(para('Casa Ribeiro has sold bifanas and soup on Harrogate Road since 1998. The awning had faded to pink and the menu was a laminated A3 sheet. Luis Ribeiro wanted it to look like the place his father opened, only readable from the bus stop.', fontSize='large'),
                  para('We drew the lettering from a 1960s Lisbon price board Luis kept in the cellar, then handed the drawings to Beth Wray, who painted the awning and the pillars on site over three days in March. The paper menu is printed on 120gsm uncoated stock and replaced every Monday.'),
                  para('What we would change: the pillar lists prices, and prices change. Next time the prices go on a chalk panel and only the dishes stay painted.'))),
        ('42%', image('menu-1.jpg', 'Printed café menu with a crest at the top and a dotted list of coffees in Portuguese and English', 'Weekly paper menu, two languages')),
        align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}),
    pattern_ref('case-credits')), block_types='core/post-content', description='A case study that leads with pictures and keeps text short, beside the printed piece.')

pattern('case-text-first', 'Case study: problem, constraints, what changed', 'portfolio', J(
    heading('The brief', 3), para('Kirkgate Law Library had 140 red volumes of court reports and no way to find year 2009 without pulling six of them out. The budget covered new spine labels, nothing else.'),
    heading('What we did', 3), para('A spine system set in one weight, with the year at 60pt so it reads from the reading tables. Volume numbers sit in the same place on every spine. The labels are printed on self-adhesive book cloth by a binder in Otley.'),
    heading('What we would do differently', 3), para('Test the gold foil under the library lights first. Two shelves glare at 4pm in winter.'),
    pattern_ref('case-credits')), block_types='core/post-content')

pattern('services-index', 'Services index', 'services', group(J(
    heading('Prices and lead times', 2, fontSize='x-large', align='wide'),
    table([
        ['<a href="/category/identity/">Identity</a>', 'Names, marks, typefaces and the first printed things', 'From £6,500', '10 to 14 weeks'],
        ['<a href="/category/packaging/">Packaging</a>', 'Labels, tins, boxes, bags, with the printer in the room', 'From £4,000 per range', '8 to 12 weeks'],
        ['<a href="/category/editorial/">Editorial</a>', 'Books, catalogues, programmes, annual reports', 'Quoted per page count', 'Depends on the text'],
        ['<a href="/category/signage/">Signage</a>', 'Shop fronts, wayfinding, painted and enamel signs', 'From £3,000 plus making', '6 to 10 weeks'],
        ['<a href="/category/motion/">Motion</a>', 'Idents, animated posters, screens in foyers', 'From £2,500', '4 to 6 weeks'],
        ['<a href="/category/web/">Web</a>', 'Small sites we can build in WordPress and hand over', 'From £5,000', '8 weeks'],
    ], head=['Service', 'What it covers', 'Usually costs', 'Takes'], className='is-style-ruled-table', align='wide'),
    para('Prices are for a small business or a single venue, before VAT. We don\'t pitch for free and we don\'t design a logo on its own: the smallest job is a name, a mark and one printed thing.', fontSize='small')),
    align='wide', layout={'type': 'default'}))

pattern('industries-index', 'Industries we know', 'services', columns(
    ('33.33%', heading('Who we usually work for', 3)),
    ('66.66%', J(para('<a href="/tag/food-and-drink/">Food and drink</a>, <a href="/tag/arts-and-culture/">arts and culture</a>, <a href="/tag/public-sector/">libraries and councils</a>, <a href="/tag/retail/">independent shops</a> and <a href="/tag/non-profit/">small charities</a>. About a third of our work is in Leeds and Bradford, the rest is anywhere with a train station.', fontSize='large'))),
    align='wide', className='is-style-rule-top'))

pattern('how-we-work', 'How a project runs', 'services', columns(
    ('33.33%', heading('How a project runs', 3)),
    ('66.66%', lst([
        'A first meeting at the studio or on site. Free, about an hour, tea included.',
        'A written proposal with a fixed fee, a timeline and who will do the work.',
        'Half the fee up front, then two rounds of design with printed proofs, never only PDFs.',
        'We go to the printer or the sign maker with you. The second half is due on delivery.'], ordered=True)),
    align='wide', className='is-style-rule-top'))

pattern('studio-intro', 'Studio: who we are', 'about', columns(
    ('58%', J(para('Ingrid Sandvik and Tunde Ogunleye met at a letterpress workshop in 2011 and started the studio three years later in a back room of the old Moorhouse print works on Mabgate. There are seven of us now, one dog on Wednesdays and a Heidelberg platen that still runs.', fontSize='large'),
              para('Most of our clients sell something you can hold or visit: coffee, beer, books, tickets, soup. We like working with the people who make the thing, and with the printers and sign painters who finish the job. Our opinion, for what it is worth: one well printed menu does more for a café than a 60-page brand guidelines PDF, so we make the menu first.'),
              para('We don\'t take on crypto, gambling or oil companies. We close for two weeks at Christmas and for most of August.'))),
    ('42%', image('print-2.jpg', 'Engraved nineteenth-century business card with flourished script lettering for an engraver in Vienna', 'On the studio wall: an 1840s engraver\'s card, the reason Maud took up lettering')),
    align='wide'))

people = [('Ingrid Sandvik', 'Co-founder, new business', 'ingrid@example.com'), ('Tunde Ogunleye', 'Co-founder, creative director', 'tunde@example.com'),
          ('Maud Kessler', 'Designer, lettering and type', 'maud@example.com'), ('Rahim Chowdhury', 'Designer, packaging and print', 'rahim@example.com'),
          ('Joss Adeyemi', 'Motion designer', 'joss@example.com'), ('Ellie Brannigan', 'Studio manager, invoices and jobs', 'ellie@example.com'),
          ('Nika Horvat', 'Junior designer, Thursdays and Fridays', 'nika@example.com')]
pattern('people-list', 'People: named team with roles and emails', 'about', group(J(
    heading('People', 2, fontSize='x-large'),
    group(J(*[row(J(para(n, style={'typography': {'fontWeight': '700'}}), para(r), para('<a href="mailto:%s">%s</a>' % (e, e))), className='is-style-person-row') for n, r, e in people]),
          layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}})),
    layout={'type': 'default'}), description='A named team list with roles, used on the studio and contact pages instead of a generic form.')

pattern('clients-list', 'Clients (text list)', 'about', columns(
    ('33.33%', heading('Some people we have worked for', 3)),
    ('66.66%', para('Casa Ribeiro, Kirkgate Law Library, Leeds Print Fair, Ardsley Tea Merchants, the Esperanto Society of Leeds, Northern Tile Company, Marché Couvert Roubaix, Lindqvist Matches, Stockhamer Engraving, Café Coroa, Otley Science Festival', fontSize='large')),
    align='wide', className='is-style-rule-top'))

pattern('client-quotes', 'Client quotes (named)', 'testimonials', columns(
    (None, quote('They made us go and stand at the bus stop to read the awning. Then they made it bigger.', 'Luis Ribeiro, Casa Ribeiro, April 2025')),
    (None, quote('The spines work. Students stopped asking the desk where 2009 is.', 'Hannah Pryce, librarian, Kirkgate Law Library, January 2025')),
    align='wide'))

pattern('new-business', 'New business email', 'call-to-action', group(J(
    para('Starting something?', fontSize='small', align='wide'),
    heading('<a href="mailto:work@example.com">work@example.com</a>', 2, fontSize='xx-large', align='wide', className='is-email'),
    para('Tell us what you sell, where, and when it needs to be in people\'s hands. Ingrid replies within two working days.', align='wide')),
    tag='section', align='full', className='is-style-sheet-invert', style=pad(70), layout={'type': 'constrained'}),
    description='A big email address for new work, on a black sheet.')

pattern('jobs-note', 'Jobs email', 'call-to-action', group(J(
    heading('Jobs and placements', 4),
    para('We are not hiring right now. We take one paid placement each summer, four weeks, £480 a week. Send a PDF of up to 12 pages to <a href="mailto:jobs@example.com">jobs@example.com</a> by 31 March. Ellie reads every one.')),
    layout={'type': 'default'}))

pattern('pdf-request', 'Ask for a PDF of relevant case studies', 'call-to-action', group(
    para('Want to see work close to yours? Email <a href="mailto:work@example.com?subject=Case%20studies%20PDF">work@example.com</a> with your trade and we\'ll send a PDF of the three case studies most like it, with costs.'),
    className='is-style-proof', layout={'type': 'default'}))

pattern('newsletter', 'Newsletter sign-up', 'call-to-action', group(J(
    heading('Studio letter', 4),
    para('Four emails a year: new work, what we printed and what went wrong. Send a blank email to <a href="mailto:letter@example.com?subject=Subscribe">letter@example.com</a> to join.')),
    layout={'type': 'default'}, anchor='letter'))

pattern('shop-link', 'Studio shop link', 'call-to-action', columns(
    ('30%', image('tote-1.jpg', 'Red lithograph poster titled The Poster, with two women in long robes drawn in black line', href='https://shop.example.com/')),
    ('70%', J(heading('The shop', 3), para('We print a few things for ourselves between jobs: letterpress calendars, the Mabgate type specimen and posters from the print fair. Everything is printed in the studio and posted on Fridays.'),
              buttons(('Go to the shop', 'https://shop.example.com/')))),
    align='wide', className='is-style-proof', style={'spacing': {'blockGap': {'left': P(50)}}}))

pattern('find-us', 'Find the studio', 'contact', columns(
    (None, J(heading('Find us', 4), para('Unit 3, Moorhouse Works<br>Mabgate, Leeds LS9 7DZ'),
             para('Ten minutes from Leeds station, or the 16 to Mabgate Green. Buzz twice, the bell is slow. The studio is on the first floor, with a lift.', fontSize='small'))),
    (None, J(heading('Hours', 4), para('Monday to Thursday 9.30 to 6<br>Friday 9.30 to 4<br>Closed weekends, most of August and two weeks at Christmas'))),
    (None, J(heading('Phone', 4), para('<a href="tel:+441134960721">0113 496 0721</a><br>Ellie answers. Ask for Ingrid for new work.'))),
    align='wide', className='is-style-rule-top'))

pattern('now-on-desk', 'On the desk now', 'text', columns(
    ('33.33%', heading('On the desk', 3)),
    ('66.66%', lst(['A range of six beer labels for a brewery in Kirkstall, due at the printer 14 November.',
                    'Wayfinding for a library extension in Pudsey. Signs go up in February.',
                    'The 2026 Leeds Print Fair poster. Two colours again, blue this time.'])),
    align='wide', className='is-style-rule-top'))

pattern('notice-closed', 'Notice: studio closed dates', 'banner', group(
    para('The studio is closed from 20 December to 5 January. Emails sent in that time get answered on 6 January, in the order they came in.'),
    tag='aside', align='full', className='is-style-orange-bar', style=pad(20), layout={'type': 'constrained'}), description='A notice bar for closures. Edit the dates each year and remove it afterwards.')

pattern('lead-project', 'Lead project, one wide image and its line', 'portfolio', columns(
    ('66.66%', image('book-1.jpg', 'Rows of red bound law reports on a shelf, with gold lettering on the spines', href='/kirkgate-law-library/')),
    ('33.33%', J(heading('<a href="/kirkgate-law-library/">Kirkgate Law Library</a>', 3), para('A spine system for 140 volumes of court reports, readable from across the room.'),
                 para('Editorial, public sector, 2025', fontSize='small', textColor='muted'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(40)}}}))

pattern('process-proofs', 'Process: proofs next to the finished thing', 'portfolio,gallery', J(
    heading('From proof to shelf', 3),
    gallery([('poster-1.jpg', 'Printed catalogue sheet of 36 black and white tile designs in a grid, each with a code number', 'Catalogue proof, black only'),
             ('print-1.jpg', 'Four matchbox labels on an orange ground, with a ship, a woman with a fan and a flower', 'Label set, four designs per box'),
             ('shop-1.jpg', 'Blue enamel sign with yellow capitals about paying cash, fixed to a stone wall', 'Enamel sign, as fitted')], columns=3, align='wide')))

pattern('pullquote-opinion', 'Studio opinion (pull quote)', 'text', pullquote('Print one good menu before you write a single brand value.', 'Tunde Ogunleye', align='wide'))


# ---------------------------------------------------------------- case study kit (round 2)
pattern('case-intro', 'Case study: the brief and our answer, side by side', 'case-study', columns(
    ('50%', J(heading('The brief', 5), para('Leeds Print Fair wanted one image that could be the poster, the programme cover, the tote bag and the screen by the door, on a budget that covered two print colours.'))),
    ('50%', J(heading('What we made', 5), para('One drawn figure, set against a single red. It prints in two colours, it cuts down to a square for Instagram, and it moves for the foyer screen.'))),
    align='wide', className='is-style-rule-top', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('case-image-full', 'Case study: one image, full width, with a caption', 'case-study', image('tote-1.jpg', 'Red lithograph poster titled The Poster, with two women in long robes drawn in black line', 'The poster, A1, two colours on Munken Pure 150gsm', align='full'))

pattern('case-image-pair', 'Case study: two images side by side', 'case-study', gallery([
    ('print-1.jpg', 'Four matchbox labels on an orange ground, with a ship, a woman with a fan and a flower', 'Label set, four per box'),
    ('pack-2.jpg', 'Orange tin box with a hinged lid and a black printed label', 'The tin, kept from 1931, with the new stamp')], columns=2, align='wide'))

pattern('case-before-after', 'Case study: before and after', 'case-study', columns(
    (None, J(image('shop-1.jpg', 'Blue enamel sign with yellow capitals about paying cash, fixed to a stone wall'), para('After: fired enamel, blue and yellow', fontSize='small'))),
    (None, J(image('hero.jpg', 'Hand-painted awning and window lettering on a small lunch bar'), para('Before: hand lettering, repainted every few years', fontSize='small'))),
    align='wide'), description='Two images with short captions. Put the old version on the right so the new one is read first.')

pattern('case-quote', 'Case study: the client, quoted', 'case-study', group(
    quote('The tins sold out in a fortnight and people keep the price list in their kitchen drawers.', 'Margaret Ardsley, Ardsley Tea Merchants, October 2025'),
    align='wide', layout={'type': 'constrained'}, style=pad(50)))

pattern('case-type-sample', 'Case study: the typeface or lettering, set big', 'case-study', group(J(
    heading('The lettering', 6),
    para('Pecco Souchong 1931', className='is-style-type-sample'),
    para('Maud redrew the old tin lettering as a full alphabet so the counter staff can stamp any tea name. It has capitals, figures and a pound sign.', fontSize='small')),
    align='wide', layout={'type': 'default'}))

pattern('case-deliverables', 'Case study: what we made (list)', 'case-study', columns(
    ('33%', heading('What we made', 5)),
    ('67%', lst(['A new stamp and ink pad for the counter', 'Forty tea labels, filled in by hand', 'A folded price list, reprinted when prices change', 'Shop window lettering, gold leaf on glass', 'Paper bags in two sizes'])),
    align='wide', className='is-style-rule-top'))

pattern('case-process', 'Case study: how it went, step by step', 'case-study', columns(
    ('33%', heading('How it went', 5)),
    ('67%', lst(['Two mornings behind the counter, watching what people asked for.', 'A week of lettering sketches from the old tins.', 'Proofs on the shop\'s own paper bags, printed in the studio.', 'A stamp made by a rubber-stamp maker in Dewsbury.', 'Launch on a Saturday, with the old tins in the window.'], ordered=True)),
    align='wide', className='is-style-rule-top'))

pattern('case-outcome', 'Case study: what changed afterwards', 'case-study', group(J(
    heading('What changed', 5),
    para('The counter staff stopped writing labels in biro. The tins went back on sale for the first time since 2008. Margaret says the price list is the thing customers comment on, which we did not expect.')),
    className='is-style-proof', layout={'type': 'default'}), description='Operational outcomes in the client\'s words. No invented statistics.')

pattern('case-video', 'Case study: moving version (still linking out)', 'case-study', columns(
    ('58%', image('sign-1.jpg', 'Neon signs on tall buildings at night', href='https://vimeo.com/')),
    ('42%', J(heading('The foyer loop', 5), para('Twelve seconds, no sound, on a loop by the door. <a href="https://vimeo.com/">Watch it on Vimeo</a>.'))),
    align='wide', verticalAlignment='center'))

pattern('case-study-print-fair', 'Case study layout: Leeds Print Fair', 'case-study', J(
    pattern_ref('case-intro'), pattern_ref('case-image-full'), pattern_ref('case-video'), pattern_ref('case-deliverables'), pattern_ref('case-credits')),
    block_types='core/post-content', description='A complete case study assembled from the case-study patterns.')

pattern('case-study-ardsley', 'Case study layout: Ardsley Tea Merchants', 'case-study', J(
    pattern_ref('case-image-pair'), pattern_ref('case-process'), pattern_ref('case-type-sample'), pattern_ref('case-quote'), pattern_ref('case-outcome'), pattern_ref('case-credits')),
    block_types='core/post-content')

pattern('case-study-roubaix', 'Case study layout: Marché Couvert', 'case-study', J(
    para('Roubaix\'s covered market wanted rules on the wall that nobody could peel off. We set them in one condensed capital, in French and Flemish, and had twelve signs fired in enamel in Lyon.', fontSize='large'),
    pattern_ref('case-before-after'), pattern_ref('case-deliverables'), pattern_ref('case-credits')), block_types='core/post-content')

# ---------------------------------------------------------------- more studio patterns (round 2)
pattern('studio-photos', 'The studio, in pictures', 'about', gallery([
    ('print-2.jpg', 'Engraved nineteenth-century business card with flourished script lettering', 'On the wall by the door'),
    ('poster-1.jpg', 'Printed catalogue sheet of 36 black and white tile designs', 'Proofs pinned up for a week'),
    ('book-1.jpg', 'Rows of red bound law reports on a shelf', 'The reference shelf')], columns=3, align='wide'))

pattern('recognition', 'Press and awards (text list)', 'about', columns(
    ('33%', heading('Written about', 5)),
    ('67%', lst(['Eye on Design, "Leeds studios to watch", March 2026', 'Creative Review Annual, packaging, for Ardsley Tea Merchants, 2025', 'Yorkshire Design Awards, signage, Marché Couvert, 2024'])),
    align='wide', className='is-style-rule-top'))

pattern('client-faq', 'Questions new clients ask', 'services', group(J(
    heading('Questions new clients ask', 3),
    details('Do you only work in Leeds?', para('No. About two thirds of our clients are elsewhere. We visit at the start and at the printer, and use video calls in between.')),
    details('Can you just design a logo?', para('We don\'t. The smallest job is a name, a mark and one printed thing, from £6,500.')),
    details('Who owns the work?', para('You do, once the final invoice is paid. We keep the right to show it here.')),
    details('Do you pitch?', para('Not for free. A paid first stage, usually £1,200, gets you two directions and a printed proof of each.'))),
    layout={'type': 'constrained'}))

pattern('what-to-send', 'What to send us before a first meeting', 'services', group(J(
    heading('Before we meet, send us', 4),
    lst(['What you sell and where', 'Three things you have printed before, good or bad', 'A date something needs to be in people\'s hands', 'A rough budget, even if it is a range'])),
    className='is-style-proof', layout={'type': 'default'}))

pattern('selected-work-list', 'Selected work, as a year list', 'portfolio', group(J(
    heading('Selected work by year', 3),
    group(J(*[row(J(para(y, style={'typography': {'fontWeight': '700'}}), para('<a href="%s">%s</a>' % (u, t)), para(d)), className='is-style-person-row') for y, t, u, d in [
        ('2025', 'Leeds Print Fair', '/leeds-print-fair-2025/', 'Poster, programme, foyer loop'),
        ('2025', 'Ardsley Tea Merchants', '/ardsley-tea-merchants/', 'Tins, stamp, price list'),
        ('2025', 'Kirkgate Law Library', '/kirkgate-law-library/', 'Spine system'),
        ('2025', 'Casa Ribeiro', '/casa-ribeiro/', 'Painted signs and menus'),
        ('2025', 'Marché Couvert, Roubaix', '/marche-couvert-roubaix/', 'Enamel signs')]]), layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}})),
    align='wide', layout={'type': 'default'}))

# page layouts
pattern('page-studio', 'Page: studio', 'about', J(pattern_ref('studio-intro'), pattern_ref('studio-photos'), pattern_ref('now-on-desk'), pattern_ref('recognition'), pattern_ref('people-list'), pattern_ref('clients-list'), pattern_ref('client-quotes'), pattern_ref('shop-link')), block_types='core/post-content')
pattern('page-services', 'Page: services and prices', 'services', J(pattern_ref('services-index'), pattern_ref('how-we-work'), pattern_ref('what-to-send'), pattern_ref('client-faq'), pattern_ref('industries-index'), pattern_ref('pdf-request')), block_types='core/post-content')
pattern('page-contact', 'Page: contact', 'contact', J(
    para('Email the person you need. There is no form, and a phone call is fine.', fontSize='large'),
    pattern_ref('people-list'), pattern_ref('pdf-request'), pattern_ref('find-us'),
    columns((None, pattern_ref('jobs-note')), (None, pattern_ref('newsletter')), align='wide')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')), justify='space-between', align='wide'),
    tag='header', align='full', className='is-style-rule-bottom', style=pad(30)))

write('parts/footer.html', group(J(
    columns(
        ('50%', J(dyn('site-title', level=0, fontSize='x-large'), para('Identities, packaging, signs and printed things. Seven people on Mabgate, Leeds, since 2014.', fontSize='small'))),
        (None, J(heading('Studio', 6), para('Unit 3, Moorhouse Works<br>Mabgate, Leeds LS9 7DZ<br><a href="tel:+441134960721">0113 496 0721</a>', fontSize='small'))),
        (None, J(heading('Write to', 6), para('New work: <a href="mailto:work@example.com">work@example.com</a><br>Jobs: <a href="mailto:jobs@example.com">jobs@example.com</a><br><a href="https://www.instagram.com/">Instagram</a>', fontSize='small'))),
        align='wide'),
    para('Demo images are public domain photographs and prints from Wikimedia Commons and the Metropolitan Museum of Art, standing in for client work.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-sheet-invert', style=pad(60, 50)))

write('parts/notice.html', pattern_ref('notice-closed'))

# ---------------------------------------------------------------- templates
def tpl(name, inner, top=60, bottom=70, **kw):
    write('templates/%s.html' % name, page_template(inner, style=pad(top, bottom), **kw))

write('templates/front-page.html', page_template(J(
    pattern_ref('hero-name-fact'),
    group(pattern_ref('work-sheet'), align='wide', layout={'type': 'default'}),
    group(pattern_ref('selected-work-list'), align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    pattern_ref('new-business')), style={'spacing': {'padding': {'bottom': '0'}}}))

tpl('home', J(heading('Work', 1, align='wide'), pattern_ref('filter-bar-all'), pattern_ref('work-sheet-archive')))
tpl('category-selected', J(heading('Selected work', 1, align='wide'), pattern_ref('filter-bar-selected'), pattern_ref('work-sheet-archive')))
tpl('archive', J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('filter-bar'), pattern_ref('work-sheet-archive')))
tpl('index', J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')))
tpl('search', J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='Packaging, signs, tea', buttonText='Search'), pattern_ref('post-list')))
tpl('404', J(heading('Nothing at this address', 1), para('The project might have moved when we tidied the work index. Try <a href="/work/">all work</a> or search below.'),
             dyn('search', label='Search', showLabel=False, placeholder='Packaging, signs, tea', buttonText='Search')), top=70, bottom=80)
tpl('page', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1440px'})))
tpl('page-wide', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1440px'})))
tpl('single', J(
    dyn('post-featured-image', align='wide', aspectRatio='16/9'),
    columns(('66.66%', J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', fontSize='large', moreText=''))),
            ('33.33%', pattern_ref('case-facts')), align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}),
    dyn('post-content', align='wide', layout={'type': 'constrained'}),
    pattern_ref('next-project')), top=40)
print('studio built')

# ---------------------------------------------------------------- demo content
def case(p1, p2, credits):
    return J(para(p1), para(p2), heading('Credits', 6), para(credits, fontSize='small'))

works = [
    ('Casa Ribeiro', 'Hand-painted signs and a paper menu for a lunch bar on Harrogate Road.', ['identity', 'signage', 'selected'], ['Food and drink'], 'hero.jpg', {'pattern': 'studio/case-image-led'}),
    ('Kirkgate Law Library', 'A spine system for 140 volumes of court reports, readable from across the room.', ['editorial', 'selected'], ['Public sector'], 'book-1.jpg', {'pattern': 'studio/case-text-first'}),
    ('Leeds Print Fair 2025', 'Poster, programme and a looping foyer screen, printed in two colours on Munken.', ['identity', 'editorial', 'motion', 'selected'], ['Arts and culture'], 'tote-1.jpg',
     {'pattern': 'studio/case-study-print-fair'}),
    ('Ardsley Tea Merchants', 'A tin, a rubber stamp and a price list for a tea shop open since 1931.', ['packaging', 'identity', 'selected'], ['Food and drink', 'Retail'], 'pack-2.jpg',
     {'pattern': 'studio/case-study-ardsley'}),
    ('Esperanto Society of Leeds', 'Carrier bags and a membership card for a society that meets above the Victoria pub.', ['identity'], ['Non-profit'], 'pack-1.jpg',
     case('The society has 63 members and a budget of £900. We set their motto in a script Maud drew from a 1920s congress badge and printed it on paper bags they hand out at the Leeds Library book sale.', 'The membership card is the same design, one colour, on grey board.', 'Lettering: Maud Kessler. Bags: Bagfactory Bradford.')),
    ('Marché Couvert, Roubaix', 'Twelve enamel signs for a covered market, in French and Flemish.', ['signage', 'selected'], ['Public sector', 'Retail'], 'shop-1.jpg',
     {'pattern': 'studio/case-study-roubaix'}),
    ('Northern Tile Company', 'A catalogue that shows 36 tile designs at real size, and the online version of it.', ['editorial', 'web'], ['Retail'], 'poster-1.jpg',
     case('The old catalogue printed tiles at 40 percent. Customers ordered the wrong ones. The new one prints every design at 1:1, two sheets per spread, and the website uses the same codes.', 'We built the site in WordPress and the shop staff update stock themselves.', 'Photography: Ade Okafor. Print: Pureprint.')),
    ('Lindqvist Matches', 'Labels for a Swedish match reissue, four designs per box.', ['packaging'], ['Retail'], 'print-1.jpg',
     case('A reissue of labels from the Vänersborg factory archive. We redrew four of them, fixed the spelling and moved the safety text where Swedish law now wants it.', 'Printed in two spot colours on kraft. The boxes sell in sets of four for £6.', 'Archive research: Karin Lindqvist.')),
    ('Neon survey, Osaka', 'A week photographing lit signs for the Leeds Light Night programme.', ['motion'], ['Arts and culture'], 'sign-1.jpg',
     case('Light Night paid for Joss and Tunde to spend a week on Dotonbori photographing signs after dark. The footage became the festival idents.', 'We are not sure this counts as a project. It paid, so it is in here.', 'Photography and edit: Joss Adeyemi.')),
    ('Stockhamer Engraving', 'Letterheads and cards for an engraver, printed by the client on her own press.', ['identity'], ['Retail'], 'print-2.jpg',
     case('Josefa Stockhamer engraves trophies and signet rings in Headingley. She wanted cards that looked like her grandfather\'s, so we copied the layout and redrew the script.', 'She prints them herself on a proof press in the back of the shop, 50 at a time.', 'Lettering: Maud Kessler.')),
    ('Café Coroa', 'A menu board and a two-page menu for a Portuguese café on Harehills Lane.', ['identity'], ['Food and drink'], 'menu-1.jpg',
     case('Two languages, one page, and prices that line up. We set the menu in the café\'s own crest colours and left space for the daily soup.', 'The board is painted. The paper menu is printed on the studio laser every Monday.', 'Photography: Ade Okafor.')),
]
posts = []
for i, (title, tagline, cats, tags, img, body) in enumerate(works):
    p = {'title': title, 'category': cats, 'tags': tags, 'image': img, 'excerpt': tagline, 'date': '2025-%02d-10' % (11 - i)}
    if isinstance(body, dict):
        p.update(body)
    else:
        p['content'] = body
    posts.append(p)

content = {
    'site': {'title': 'Sandvik Ogunleye', 'tagline': 'Design studio, Mabgate, Leeds'},
    'categories': [{'slug': 'selected', 'name': 'Selected'}] + [{'slug': s, 'name': s.capitalize()} for s in ['identity', 'packaging', 'editorial', 'signage', 'motion', 'web']],
    'front_page': 'home', 'posts_page': 'work',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'work', 'title': 'Work', 'content': ''},
        {'slug': 'services', 'title': 'Services', 'pattern': 'studio/page-services'},
        {'slug': 'studio', 'title': 'Studio', 'pattern': 'studio/page-studio'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'studio/page-contact'},
    ],
    'posts': posts,
    'nav': [{'label': 'Work', 'url': '/work/'}, {'label': 'Services', 'url': '/services/'}, {'label': 'Studio', 'url': '/studio/'}, {'label': 'Contact', 'url': '/contact/'}],
}
os.makedirs('demos/studio', exist_ok=True)
json.dump(content, open('demos/studio/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
