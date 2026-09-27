# Design note (larder, idea 058b, owner's brief: "an independent one too, like jadlonomia.com")
# Direction: one person's plant-based kitchen blog from Łódź, Spiżarnia. Personal, seasonal and a bit chatty, the way
#   Jadłonomia reads: a "tastes best right now" strip under the header, a photo mosaic of recipes with titles on pale bands,
#   and recipes written as a story with a short "what you need" list, plus handwritten asides.
# Fonts: Vollkorn (display, sturdy book serif with Polish diacritics), Work Sans (body), Caveat (accent, only for asides).
# Palette: cool paper grey #F3F4F1, forest green #143A22 for text, beet #9C1848, sky strip #E3ECF7, mustard #E0A526.
# Layout idea: the home page is a dense mosaic (every sixth tile twice the size) under a seasonal produce strip, next to
#   a month-by-month seasonal calendar table. Clearly different from pantry: no recipe card, no pills, serif, grey paper.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('larder')
S = THEME['slug']
D = THEME['dir']
ROOT = os.path.abspath(os.path.join(D, '..', '..'))

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Vollkorn", Georgia, serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"Work Sans", "Helvetica Neue", Arial, sans-serif'
    if f['slug'] == 'accent':
        f['fontFamily'] = '"Caveat", "Comic Sans MS", cursive'
        f['name'] = 'Caveat (handwriting)'

PAL = [
    ('base', '#F3F4F1', 'Paper grey'),
    ('contrast', '#143A22', 'Forest'),
    ('accent', '#9C1848', 'Beet'),
    ('accent-2', '#2F6B3A', 'Dill'),
    ('surface', '#E3ECF7', 'Sky'),
    ('line', '#CBD1C8', 'Pencil'),
    ('muted', '#4B5A4F', 'Moss'),
    ('highlight', '#E0A526', 'Mustard'),
    ('white', '#FFFFFF', 'White'),
]
pal = lambda p: [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '680px', 'wideSize': '1120px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Tiny', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.7rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.25rem', 'name': 'Title', 'fluid': {'min': '2.3rem', 'max': '3.25rem'}},
                {'slug': 'display', 'size': '5rem', 'name': 'Display', 'fluid': {'min': '2.9rem', 'max': '5rem'}},
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'},
                {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'},
                {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4rem, 9vw, 7rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.7', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '2px', 'style': 'dashed', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '1.08', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '700'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '700'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|white'},
                'border': {'radius': '6px 18px 6px 18px', 'width': '0'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.7em', 'bottom': '0.7em', 'left': '1.3em', 'right': '1.3em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|white'}},
                ':focus': {'outline': {'color': 'var:preset|color|contrast', 'offset': '2px', 'style': 'dashed', 'width': '2px'}},
            },
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.4'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|xx-large', 'letterSpacing': '-0.02em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|medium'}, 'color': {'text': 'var:preset|color|accent'}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'}},
            'core/image': {'border': {'radius': '4px'}},
            'core/post-featured-image': {'border': {'radius': '4px'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontStyle': 'italic', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.35'}, 'color': {'text': 'var:preset|color|accent'},
                           'border': {'width': '0'}, 'spacing': {'padding': {'left': '0'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|accent', 'fontSize': 'var:preset|font-size|xx-large'}, 'border': {'width': '0'}, 'color': {'text': 'var:preset|color|accent'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'dashed'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}},
            'core/search': {'border': {'radius': '6px'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/list': {'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': (
            'body{font-synthesis:none}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
            'table{font-variant-numeric:tabular-nums}.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px dashed var(--wp--preset--color--line);padding:.45em .6em .45em 0;text-align:left}'
            '.wp-block-table thead{border-bottom:2px solid var(--wp--preset--color--contrast)}'
            '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:6px;background:var(--wp--preset--color--white)}'
            ':focus-visible{outline:2px dashed var(--wp--preset--color--accent);outline-offset:2px}'
            '.wp-block-navigation .current-menu-item>a{text-decoration:underline wavy var(--wp--preset--color--accent);text-underline-offset:.35em}'
            '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--surface)!important;font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large)}'
            '[class*="is-style-calendar"] table{table-layout:auto!important;min-width:40rem}[class*="is-style-calendar"] th{white-space:nowrap}[class*="is-style-calendar"] td:first-child{white-space:nowrap}'
            '@media (min-width:782px){[class*="is-style-mosaic"]>li:nth-child(6n+1){grid-column:span 2;grid-row:span 2}[class*="is-style-mosaic"]>li:nth-child(6n+1) .wp-block-cover{min-height:100%!important}}'
            '@media (prefers-reduced-motion:no-preference){a{transition:color .15s}}'
        ),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'season-strip', 'title': 'Tastes best right now'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-recipe', 'title': 'Recipe (full)', 'postTypes': ['post']},
    ],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Larder
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A personal recipe blog for one independent home cook, built around the seasons, with a produce strip, a recipe mosaic and a seasonal calendar.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: larder
Tags: food-and-drink, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

P = lambda n: {'top': 'var:preset|spacing|%s' % n, 'bottom': 'var:preset|spacing|%s' % n, 'left': 'var:preset|spacing|%s' % n, 'right': 'var:preset|spacing|%s' % n}
section('sky', 'Sky strip', ['core/group'], {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}})
section('note', 'Handwritten aside', ['core/paragraph', 'core/group'], {
    'typography': {'fontFamily': 'var:preset|font-family|accent', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}, 'color': {'text': 'var:preset|color|accent'},
    'css': '&{transform:rotate(-1.5deg)}'})
section('card', 'White card', ['core/group', 'core/column'], {
    'color': {'background': 'var:preset|color|white'}, 'border': {'radius': '4px'}, 'spacing': {'padding': P(50)}})
section('needs', 'What you need', ['core/group'], {
    'color': {'background': 'var:preset|color|white'}, 'border': {'radius': '4px', 'width': '2px', 'style': 'dashed', 'color': 'var:preset|color|line'}, 'spacing': {'padding': P(40)}})
section('mosaic', 'Mosaic', ['core/post-template'], {
    'css': ('&{grid-auto-flow:dense;gap:12px!important}'
            '& .wp-block-cover{height:100%;padding:0!important;border-radius:4px;overflow:hidden}& .wp-block-cover__inner-container{width:100%!important}'
            '& .wp-block-cover .wp-block-post-title{background:color-mix(in srgb,var(--wp--preset--color--white) 88%,transparent);margin:0;padding:.6em .8em;font-size:var(--wp--preset--font-size--medium)}'
            '& .wp-block-cover .wp-block-post-title a{color:var(--wp--preset--color--contrast)}')})
section('tiles', 'Tiles (even)', ['core/post-template'], {
    'css': ('&{gap:12px!important}& .wp-block-cover{height:100%;padding:0!important;border-radius:4px;overflow:hidden}& .wp-block-cover__inner-container{width:100%!important}'
            '& .wp-block-cover .wp-block-post-title{background:color-mix(in srgb,var(--wp--preset--color--white) 88%,transparent);margin:0;padding:.6em .8em;font-size:var(--wp--preset--font-size--medium)}'
            '& .wp-block-cover .wp-block-post-title a{color:var(--wp--preset--color--contrast)}')})
section('produce', 'Produce links', ['core/list', 'core/tag-cloud'], {
    'typography': {'fontSize': 'var:preset|font-size|small'},
    'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.2rem 1.2rem}& li{margin:0}& a{text-decoration:none;font-weight:600;color:var(--wp--preset--color--contrast);font-size:var(--wp--preset--font-size--small)!important}& a:hover{color:var(--wp--preset--color--accent);text-decoration:underline wavy}'})
section('calendar', 'Seasonal calendar table', ['core/table'], {
    'css': '& table{table-layout:auto!important}& td:first-child{min-width:11em}& td:not(:first-child),& th:not(:first-child){text-align:center!important;color:var(--wp--preset--color--accent-2)}& td:first-child{font-weight:600}& th{font-size:var(--wp--preset--font-size--x-small)}'})
section('wavy-top', 'Wavy rule above', ['core/group'], {
    'css': '&{background-image:radial-gradient(circle at 10px -4px,transparent 12px,var(--wp--preset--color--line) 13px,transparent 14px);background-size:20px 12px;background-repeat:repeat-x;padding-top:var(--wp--preset--spacing--50)}'})

def variation(fname, title, over, extra=None):
    p = {s: [c, n] for s, c, n in PAL}
    for s, c, n in over:
        p[s] = [c, n]
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': v[0], 'name': v[1]} for s, v in p.items()]}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)

variation('beetroot', 'Beetroot', [('base', '#F7EEF1', 'Pink paper'), ('contrast', '#3A0D1E', 'Beet black'), ('accent', '#A0144B', 'Beet'), ('surface', '#F2D7E1', 'Pink wash'), ('line', '#DDBFCA', 'Rule'), ('muted', '#6B3A4B', 'Muted beet')])
variation('dill', 'Dill', [('base', '#EEF3EA', 'Pale dill'), ('contrast', '#11301B', 'Pine'), ('accent', '#3B6E1F', 'Dill'), ('accent-2', '#274E14', 'Deep dill'), ('surface', '#FFF4C8', 'Butter'), ('line', '#C5D2BD', 'Rule'), ('muted', '#445441', 'Moss')])
variation('winter-jar', 'Winter jar', [('base', '#1C2320', 'Cellar'), ('contrast', '#F1EEE2', 'Candle'), ('accent', '#F2A93B', 'Apricot'), ('accent-2', '#9CC49A', 'Pickle'), ('surface', '#26312C', 'Shelf'),
                                         ('line', '#3D4A43', 'Rule'), ('muted', '#C3C8BD', 'Frost'), ('white', '#2A332F', 'Jar'), ('highlight', '#F2A93B', 'Apricot')],
          {'elements': {'button': {'color': {'text': 'var:preset|color|base'}}}})

# ---------------- helpers
def q(inner, per_page=6, offset=0, qid=1, pt_class=None, layout=None, **attrs):
    qq = {'perPage': per_page, 'pages': 0, 'offset': offset, 'postType': 'post', 'order': 'desc', 'orderBy': 'date', 'inherit': False}
    a = {'queryId': qid, 'query': qq, **attrs}
    pta = {}
    if pt_class: pta['className'] = pt_class
    if layout: pta['layout'] = layout
    return ('<!-- wp:query%s -->\n<div class="wp-block-query"><!-- wp:post-template%s -->\n%s\n<!-- /wp:post-template -->\n\n'
            '<!-- wp:query-no-results -->\n%s\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->') % (
        ' ' + json.dumps(a, separators=(',', ':')), (' ' + json.dumps(pta, separators=(',', ':'))) if pta else '', inner, para('Nothing cooked here yet.'))

PAD = lambda t, b: {'spacing': {'padding': {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}}}

def tile():
    a = {'useFeaturedImage': True, 'dimRatio': 0, 'minHeight': 260, 'minHeightUnit': 'px', 'contentPosition': 'bottom left', 'isDark': False}
    return ('<!-- wp:cover %s -->\n<div class="wp-block-cover is-light has-custom-content-position is-position-bottom-left" style="min-height:260px"><span aria-hidden="true" class="wp-block-cover__background has-background-dim-0 has-background-dim"></span>'
            '<div class="wp-block-cover__inner-container">%s</div></div>\n<!-- /wp:cover -->') % (json.dumps(a, separators=(',', ':')), dyn('post-title', isLink=True, level=3))

MOSAIC = {'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '12rem'}

# ---------------- parts
write('parts/season-strip.html', pattern_ref('season-strip'))
write('parts/header.html', J(
    group(J(
        row(J(para('<a href="https://www.instagram.com/">Instagram</a> / <a href="#letter">The monthly letter</a>', fontSize='x-small')), justify='right', align='wide'),
        group(J(dyn('site-title', level=0, textAlign='center'), dyn('site-tagline', textAlign='center')), style={'spacing': {'blockGap': 'var:preset|spacing|10'}}, layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'center'}),
        dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'center'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
        tag='header', align='full', style=PAD(30, 30)),
    template_part('season-strip')))
write('parts/footer.html', group(J(
    columns(
        (None, J(para('Spiżarnia', fontFamily='display', fontSize='x-large'), para('A plant-based kitchen in Łódź, one person and one oven. Recipes use what\'s at the Zielony Rynek market that week.', fontSize='small'))),
        (None, J(heading('Get in touch', 6), para('<a href="mailto:ola@example.com">ola@example.com</a><br>I answer on Fridays, slowly.<br>Workshops: ul. Piotrkowska 138, back courtyard, 2nd floor.', fontSize='small'))),
        (None, J(heading('Around here', 6), para('<a href="/seasons/">What\'s in season</a><br><a href="/pantry-staples/">What\'s in my larder</a><br><a href="/workshops/">Cooking workshops</a><br><a href="/book/">The book</a><br><a href="/contact/">Get in touch</a>', fontSize='small'))),
        align='wide'),
    para('Photos in this demo are CC0 and public domain images from Wikimedia Commons, standing in for my own.', fontSize='x-small', align='wide', textColor='muted')),
    tag='footer', align='full', className='is-style-wavy-top', style=PAD(60, 50)))

# ---------------- templates
COMMENTS = ('<!-- wp:comments -->\n<div class="wp-block-comments"><!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">Did you cook it? Tell me how it went</h3>\n<!-- /wp:heading -->\n\n'
            '<!-- wp:comments-title {"level":4} /-->\n\n<!-- wp:comment-template -->\n<!-- wp:comment-author-name /-->\n\n<!-- wp:comment-date /-->\n\n<!-- wp:comment-content /-->\n\n<!-- wp:comment-reply-link /-->\n<!-- /wp:comment-template -->\n\n'
            '<!-- wp:comments-pagination -->\n<!-- wp:comments-pagination-previous /-->\n\n<!-- wp:comments-pagination-numbers /-->\n\n<!-- wp:comments-pagination-next /-->\n<!-- /wp:comments-pagination -->\n\n'
            '<!-- wp:post-comments-form /--></div>\n<!-- /wp:comments -->')
T = lambda inner, t=50, b=70: page_template(inner, style=PAD(t, b))
write('templates/front-page.html', T(J(
    pattern_ref('hello-ola'), pattern_ref('recipe-mosaic'), pattern_ref('produce-of-the-month'), pattern_ref('kitchen-diary'), pattern_ref('monthly-letter')), 40, 70))
arch = inherit_query(tile(), layout=MOSAIC, template_class='is-style-mosaic', align='wide')
pattern('mosaic-archive', 'Recipe mosaic (inherits the page query)', 'query', arch, inserter=False)
write('templates/home.html', T(J(
    heading('All the recipes', 1, align='wide', textAlign='center'),
    para('Newest first. Looking for something to do with a cabbage? Try the <a href="/seasons/">season pages</a>.', align='center'),
    dyn('categories', className='is-style-produce', align='wide', style={'typography': {'textAlign': 'center'}}),
    pattern_ref('mosaic-archive'))))
write('templates/index.html', T(J(dyn('query-title', type='archive', align='wide'), pattern_ref('mosaic-archive'))))
write('templates/archive.html', T(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', textAlign='center', fontSize='xx-large'),
    dyn('term-description', align='wide', textAlign='center'),
    pattern_ref('mosaic-archive'))))
write('templates/search.html', T(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Beetroot, pierogi, jars', buttonText='Search', align='wide'),
    pattern_ref('mosaic-archive'))))
write('templates/404.html', T(J(
    heading('Nothing on this shelf', 1),
    para('The page you wanted isn\'t here. I reorganised the recipes by season in spring, so some old links broke. Search for the vegetable and you\'ll probably find it.'),
    dyn('search', label='Search', showLabel=False, placeholder='Beetroot, pierogi, jars', buttonText='Search')), 70, 80))
write('templates/page.html', T(J(dyn('post-title', level=1, textAlign='center'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', T(J(dyn('post-title', level=1, textAlign='center', align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1120px'}))))
write('templates/single.html', T(J(
    group(J(dyn('post-terms', term='category', separator=' / ', textAlign='center'),
            dyn('post-title', level=1, textAlign='center', fontSize='display'),
            dyn('post-date', textAlign='center', format='j F Y')), layout={'type': 'constrained'}),
    dyn('post-featured-image', align='wide', aspectRatio='3/2'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(J(heading('More from the same shelf', 3, textAlign='center'), q(tile(), per_page=4, qid=7, layout=MOSAIC, pt_class='is-style-tiles')), align='wide', layout={'type': 'default'}, className='is-style-wavy-top'),
    group(COMMENTS, layout={'type': 'constrained'})), 40, 70))

write('templates/single-recipe.html', T(J(
    group(J(dyn('post-terms', term='category', separator=' / ', textAlign='center'),
            dyn('post-title', level=1, textAlign='center', fontSize='xx-large'),
            para('by Ola Wróbel', align='center', fontSize='small', textColor='muted'),
            dyn('post-date', textAlign='center', format='j F Y')), layout={'type': 'constrained'}),
    dyn('post-featured-image', align='wide', aspectRatio='16/9'),
    dyn('post-content', layout={'type': 'constrained', 'contentSize': '720px'}),
    group(J(heading('Tagged', 6), dyn('post-terms', term='post_tag', className='is-style-produce')), layout={'type': 'constrained', 'contentSize': '720px'}),
    group(J(heading('More from the same shelf', 3, textAlign='center'), q(tile(), per_page=4, qid=8, layout=MOSAIC, pt_class='is-style-tiles')), align='wide', layout={'type': 'default'}, className='is-style-wavy-top'),
    group(COMMENTS, layout={'type': 'constrained', 'contentSize': '720px'})), 40, 70))

# ---------------- patterns
pattern('season-strip', 'Tastes best right now (strip)', 'featured', group(
    row(J(para('Tastes best right now:', fontFamily='display', fontSize='large'),
          lst(['<a href="/tag/plums/">Plums</a>', '<a href="/tag/mushrooms/">Wild mushrooms</a>', '<a href="/tag/cabbage/">Cabbage</a>', '<a href="/tag/beetroot/">Beetroot</a>', '<a href="/tag/apples/">Apples</a>', '<a href="/tag/pickles/">Last cucumbers for pickling</a>'], className='is-style-produce')),
        justify='center', align='wide'),
    align='full', className='is-style-sky', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}),
    description='Change the produce each month. It sits under the header on every page.')

pattern('hello-ola', 'Hello from the kitchen (intro)', 'featured', columns(
    ('58%', J(heading('Late September, and the plums won\'t stop', 1, fontSize='display'),
              para('Cześć, I\'m Ola. This is my kitchen in Łódź, where I\'ve been cooking without meat or dairy since 2014 and writing it down here since 2016. Everything on this blog is plant-based and most of it is Polish, or Polish-ish.'),
              para('This week: a plum cake that uses a whole kilo, and my grandmother\'s beetroot soup with one change she would argue with.'),
              para('psst, the workshop on 11 October still has 3 places', className='is-style-note'))),
    (None, image('plums.jpg', 'One whole red plum and one cut in half showing the yellow flesh and stone', 'węgierki, the small dark plums that are everywhere this month')),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'bottom': 'var:preset|spacing|60'}}}))

pattern('recipe-mosaic', 'Recipe mosaic', 'posts,query', group(J(
    q(tile(), per_page=10, qid=2, layout=MOSAIC, pt_class='is-style-mosaic'),
    buttons(('See all the recipes', '/recipes/'), layout={'type': 'flex', 'justifyContent': 'center'})),
    align='wide', layout={'type': 'default'}))

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
def cal_row(name, months):
    return [name] + ['●' if m in months else '' for m in range(1, 13)]
CAL = [cal_row('Rhubarb', [4, 5, 6]), cal_row('Broad beans (bób)', [6, 7, 8]), cal_row('Cucumbers for pickling', [7, 8, 9]), cal_row('Wild mushrooms', [8, 9, 10]),
       cal_row('Plums (węgierki)', [8, 9, 10]), cal_row('Beetroot', [7, 8, 9, 10, 11, 12, 1, 2]), cal_row('Cabbage', [9, 10, 11, 12, 1, 2, 3]), cal_row('Apples', [8, 9, 10, 11, 12]),
       cal_row('Dill', [5, 6, 7, 8, 9])]
pattern('season-calendar', 'Seasonal calendar (month by month)', 'featured,reference', table(CAL, head=['What'] + MONTHS, caption='When it tastes best at the market in Łódź. Stored beetroot and cabbage keep us going until March.', className='is-style-calendar'))

pattern('season-calendar-front', 'Seasonal calendar with note', 'featured', columns(
    ('34%', J(heading('What to cook when', 2), para('I shop at Zielony Rynek on Saturday mornings and cook from what\'s there. This is roughly when things turn up. The dots move by a week or two each year.'),
              para('I don\'t buy tomatoes in January. They taste of water.', className='is-style-note'))),
    (None, pattern_ref('season-calendar')),
    align='wide', className='is-style-card', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'margin': {'top': 'var:preset|spacing|70'}}}))

pattern('monthly-letter', 'The monthly letter (newsletter)', 'call-to-action', group(J(
    heading('A letter from the kitchen, once a month', 2, textAlign='center'),
    para('What\'s at the market, what I\'m cooking and one recipe that isn\'t on the blog yet. First Sunday of the month. I write every one myself.', align='center'),
    buttons(('Email me to join the list', 'mailto:ola@example.com?subject=The%20monthly%20letter'), layout={'type': 'flex', 'justifyContent': 'center'})),
    anchor='letter', className='is-style-sky', style={'spacing': {'padding': P(60), 'margin': {'top': 'var:preset|spacing|70'}}, 'border': {'radius': '4px'}}, layout={'type': 'constrained', 'contentSize': '620px'}))

def needs(items, serves):
    return group(J(heading('What you need', 4), para(serves, fontSize='x-small', textColor='muted'), lst(items)), className='is-style-needs')

pattern('what-you-need', 'What you need (ingredients box)', 'recipe', needs(
    ['1kg plums, halved and stoned', '200g plain flour', '100g sugar, plus 2 tbsp for the top', '120ml sunflower oil', '200ml oat milk', '2 tsp baking powder', 'A pinch of cinnamon'],
    'For a 24 × 30 cm tin, about 12 pieces'))

pattern('how-to', 'How I do it (method as paragraphs)', 'recipe', J(
    heading('How I do it', 3),
    para('Heat the oven to 180°C. Oil the tin and line the bottom with paper, because plum juice glues everything.'),
    para('Whisk the flour, sugar, baking powder and cinnamon. Pour in the oil and oat milk and stir until there are no dry bits. It will be thick, like porridge you forgot about.'),
    para('Spread it in the tin, push the plums in skin side down, close together, and scatter the extra sugar over. Bake for 50 minutes, until the edges are brown and the plums have slumped.'),
    para('it\'s better the next day, if it lasts', className='is-style-note')))

pattern('aside-note', 'Handwritten aside', 'text', para('psst, this works with frozen plums too', className='is-style-note'),
        description='A short note in handwriting. One or two per post at most.')

pattern('ingredient-story', 'About an ingredient (photo and story)', 'text', media_text('beetroot.jpg', 'A pile of red beetroot with long thin roots at a market stall', J(
    heading('About beetroot', 3),
    para('At the market in October you can buy beetroot by the crate, and I do. It keeps in a cool box on the balcony until March. Roast the small ones, grate the big ones into soup, and pickle whatever\'s left in March.'),
    para('<a href="/tag/beetroot/">Every beetroot recipe here</a>')), width=45))

pattern('from-the-archive', 'This time last year', 'posts', group(J(
    heading('This time last year', 3),
    lst(['<a href="/tag/mushrooms/">Chanterelles on toast, the only way I like them</a>', '<a href="/tag/pickles/">Dill pickles in a 3-litre jar</a>', '<a href="/tag/apples/">Szarlotka with too much cinnamon</a>'])), className='is-style-card'))

pattern('pantry-staples', 'What\'s in my larder (list)', 'reference', J(
    columns(
        (None, J(heading('Jars and tins', 4), lst(['Beans: white, borlotti, butter', 'Tomato passata, 700g bottles', 'Sauerkraut from the market, in its brine', 'Pickled cucumbers, my own', 'Plum powidła (a thick plum butter)']))),
        (None, J(heading('Dry things', 4), lst(['Buckwheat, roasted (kasza gryczana)', 'Pearl barley', 'Red and brown lentils', 'Dried porcini, from the woods near Spała', 'Rye flour type 2000']))),
        (None, J(heading('Always in the fridge', 4), lst(['Oat milk', 'Miso, the brown one', 'Horseradish, grated', 'Dill, a lot', 'Smoked tofu']))), align='wide')))

pattern('pantry-staples-page', 'Page: what\'s in my larder', 'reference', J(
    para('People ask what I keep in. This is it. If you have half of this, you can cook most of the blog on a Tuesday without shopping.', fontSize='large', align='center'),
    pattern_ref('pantry-staples'),
    image('buckwheat.jpg', 'A close view of roasted buckwheat groats', 'kasza gryczana, roasted. Buy it roasted, it tastes of toast'),
    para('I buy dry things from Bio Bazar on Kopernika in 5 kg bags and keep them in old jam jars. It\'s cheaper and I can see when they\'re running out.'),
    pattern_ref('preserving-timetable'), pattern_ref('abroad-swaps'), pattern_ref('glossary')), block_types='core/post-content')

pattern('season-page', 'Page: seasons', 'reference', J(
    para('This is the calendar I cook by. Tap a vegetable in the strip at the top of any page to see every recipe that uses it.', fontSize='large'),
    pattern_ref('season-calendar'),
    pattern_ref('ingredient-story'),
    media_text('mushrooms.jpg', 'Chanterelle mushrooms piled in a woven basket', J(heading('About mushrooms', 3), para('I pick chanterelles and ceps near Spała in September, and I only pick what I know. If you\'re not sure, take it to the sanepid mushroom inspector at the market. It\'s free.')), right=True, width=45),
    pattern_ref('market-day'), pattern_ref('recipe-index-ingredient')),
    block_types='core/post-content')

pattern('workshops-list', 'Cooking workshops', 'events', J(
    table([['Sat 11 Oct, 11:00', 'Pierogi without eggs', '3 places left', '180 zł'], ['Sat 25 Oct, 11:00', 'Fermenting: cabbage, beetroot, cucumbers', '6 places', '160 zł'],
           ['Sat 15 Nov, 11:00', 'A plant-based Wigilia, 12 dishes, 4 of them properly', 'Full, waiting list', '220 zł']],
          head=['When', 'What', 'Places', 'Price']),
    para('Workshops are in my kitchen studio at ul. Piotrkowska 138, back courtyard, second floor, no lift. Eight people at most. We cook for three hours and then eat everything. Book by email and I\'ll send bank details.'),
    buttons(('Book a place by email', 'mailto:ola@example.com?subject=Workshop'))))

pattern('workshops-page', 'Page: workshops', 'events', J(
    image('pierogi.jpg', 'Hands rolling out circles of pierogi dough on a floured wooden board', 'rolling pierogi dough, the bit everyone wants to do'),
    pattern_ref('workshops-list'),
    details('Do I need to bring anything?', para('An apron if you have one, and a box for leftovers. There are always leftovers.')),
    details('Can I cancel?', para('Up to 7 days before, I refund everything. After that I can move you to another date, once.')),
    details('Is it in English?', para('In Polish, with English when anyone needs it. My English is better than my Italian.')), pattern_ref('workshop-card')), block_types='core/post-content')

pattern('book-promo', 'The book', 'shop', columns(
    ('40%', image('apples.jpg', 'An old botanical plate of two apples, one red and one yellow-green, in a paper-lined box', 'the cover is not apples, but it should be')),
    (None, J(heading('Zupa na cały tydzień', 2),
             para('My first book, "Soup for the whole week", is 52 soups, one for every week of the year, from sorrel soup in April to beetroot barszcz for Wigilia. Published in Polish by Wydawnictwo Ogród, 2024, 240 pages, 69 zł.'),
             para('An English edition is coming in 2027. I\'m translating it myself, so it\'s taking a while.'),
             buttons(('Buy it from Bookfarm, Łódź', 'https://example.com/bookfarm'), ('Ask for a signed copy', 'mailto:ola@example.com?subject=Signed%20book')))),
    align='wide', verticalAlignment='center'))

pattern('book-page', 'Page: the book', 'shop', J(pattern_ref('book-promo'), pattern_ref('reader-letters')), block_types='core/post-content')

pattern('reader-letters', 'Letters from readers', 'testimonials', J(
    heading('What people cooked', 3),
    quote('I made the barszcz for my dad, who has eaten meat every day of his life. He had seconds and asked what was in it.', 'Kasia, Poznań, December 2025'),
    quote('The plum cake with frozen plums in February. It worked. My flatmate ate half the tin.', 'Jonas, Berlin, February 2026')))

pattern('about-page', 'Page: about', 'about', J(
    columns(('42%', J(image('dill.jpg', 'Bunches of fresh dill for sale at a market'), para('dill, which I put in almost everything', className='is-style-note'))),
            (None, J(para('I\'m Ola Wróbel. I grew up in Tomaszów Mazowiecki, moved to Łódź for university, and stayed for the tenement kitchens with high ceilings and terrible ovens.', fontSize='large'),
                     para('I stopped eating meat in 2014, and dairy a year later, after my sister got ill and we both started reading labels. My family took it badly for about two Christmases. Now my mum makes the mushroom uszka.'),
                     para('This blog is just me. I cook, photograph and write everything, and I pay for it with the workshops and the book. There are no sponsored posts. If a recipe mentions a shop, it\'s because I go there.'),
                     para('One opinion: kasza is better than rice. I will not be taking questions.'))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('from-the-archive')), block_types='core/post-content')


pattern('recipe-post', 'Recipe post (story, what you need, how)', 'recipe', J(
    para('Start with why you made it, who you made it for, or what was at the market. Two short paragraphs is plenty.'),
    pattern_ref('what-you-need'), pattern_ref('how-to')), block_types='core/post-content', post_types='post')

pattern('preserving-timetable', 'Preserving timetable (jars)', 'reference', J(
    heading('When to fill which jar', 3),
    table([['Rhubarb kompot', 'May', 'Drink within a week'], ['Dill pickles', 'August', 'Until spring, somewhere cool'], ['Plum powidła', 'September', 'A year, unopened'],
           ['Sauerkraut', 'October', 'All winter in the brine'], ['Beetroot for barszcz', 'November', '3 months, pickled']], head=['Jar', 'Make it in', 'Keeps'])))

pattern('abroad-swaps', 'Polish ingredients abroad (swaps)', 'reference', J(
    heading('Cooking this outside Poland?', 3),
    lst(['Twaróg: a firm silken tofu, pressed and crumbled, is closer than ricotta.', 'Kasza gryczana: sold as "kasha" or "roasted buckwheat" in Eastern European shops.', 'Węgierki plums: any small dark plum. Big juicy ones make the cake wet.', 'Sauerkraut brine: the liquid from any unpasteurised jar.'])))

pattern('market-day', 'Saturday market list', 'text', group(J(
    heading('Saturday at Zielony Rynek', 3),
    para('I go at 8, before it gets busy. Pan Marek at the third stall from the tram stop has the best cucumbers. The mushroom lady is only there in September and October, and she takes cash only.'),
    para('bring your own bags, they\'ll thank you', className='is-style-note')), className='is-style-card'))

pattern('notice-pause', 'Notice: blog on pause', 'banner', group(
    para('No new recipes until 20 October, I\'m finishing the English book. The monthly letter still goes out.', align='center'),
    align='full', className='is-style-sky', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='Swap this into the Tastes best right now part when you take a break.')

pattern('contact-page', 'Page: contact', 'contact', J(
    para('Email is best: <a href="mailto:ola@example.com">ola@example.com</a>. I read everything and answer on Fridays. I don\'t do sponsored posts or product reviews, so please don\'t send samples.', fontSize='large'),
    pattern_ref('market-day'), pattern_ref('contact-card')), block_types='core/post-content')

print('larder: patterns written')

# ---------------- round 2: the full recipe kit
def facts_line(serves, prep, cook, extra=''):
    items = [('Serves', serves), ('Prep', prep), ('Cook', cook)] + ([('Good to know', extra)] if extra else [])
    return group(J(*[group(J(para(k, fontSize='x-small', textColor='muted'), para(v, fontFamily='display', fontSize='large')), style={'spacing': {'blockGap': '0'}}) for k, v in items]),
                 className='is-style-facts', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'})

def ingredient_groups(groups):
    out = []
    for name, items in groups:
        out += [heading(name, 5, textColor='accent'), lst(items, className='is-style-ingredients')]
    return group(J(heading('Ingredients', 3), *out), className='is-style-needs', anchor='ingredients')

def method(steps, live=False):
    out = [heading('Method', 3)]
    for i, st in enumerate(steps, 1):
        text, img = st if isinstance(st, tuple) else (st, None)
        body = J(para(str(i), fontFamily='display', fontSize='x-large', textColor='accent', className='is-style-step-number'), para(text))
        if img:
            out.append(columns((None, body), ('42%', image(('/wp-content/themes/larder/assets/images/' + img[0]) if live else img[0], img[1])), verticalAlignment='top', className='is-style-step', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}))
        else:
            out.append(group(body, className='is-style-step'))
    return J(*out)

def notes_block(title, items, cls='is-style-card'):
    return group(J(heading(title, 4), lst(items)), className=cls)

def full_recipe(story, facts, groups, steps, notes, swaps, storage, aside='', live=True):
    return J(*[para(x) for x in story],
             facts_line(*facts),
             buttons(('Jump to the recipe', '#ingredients')),
             ingredient_groups(groups),
             method(steps, live),
             para(aside, className='is-style-note') if aside else '',
             notes_block('Notes from my kitchen', notes),
             notes_block('Swaps that work', swaps, 'is-style-needs'),
             notes_block('Keeping it', storage, 'is-style-sky-box'))

section('facts', 'Recipe facts line', ['core/group'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}, 'css': '& p{margin:0}'})
section('ingredients', 'Ingredient list', ['core/list'], {
    'css': '&{list-style:none;padding-left:0}&>li{border-bottom:1px dashed var(--wp--preset--color--line);padding:.35em 0}'})
section('step', 'Method step', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}},
    'css': '& .is-style-step-number{margin:0 0 .2em;line-height:1}'})
section('step-number', 'Step number', ['core/paragraph'], {'typography': {'lineHeight': '1'}})
section('sky-box', 'Sky box', ['core/group'], {'color': {'background': 'var:preset|color|surface'}, 'border': {'radius': '4px'}, 'spacing': {'padding': P(40)}})
section('produce-card', 'Produce card', ['core/group'], {
    'color': {'background': 'var:preset|color|white'}, 'border': {'radius': '4px'}, 'spacing': {'padding': P(30)}, 'css': '& img{aspect-ratio:4/3;object-fit:cover}'})

KIT_STORY = ['Two or three short paragraphs about why this recipe exists: who you cooked it for, what was at the market, what went wrong the first time.', 'Keep it short. People scroll past long stories to get to the ingredients, and they\'re right to.']
pattern('recipe-intro', 'Recipe: intro story', 'recipe', J(*[para(x) for x in KIT_STORY], para('psst, one line in handwriting for the thing you most want them to remember', className='is-style-note')))
pattern('recipe-facts', 'Recipe: servings and times', 'recipe', facts_line('4', '20 min', '40 min', 'Freezes well'))
pattern('recipe-ingredients', 'Recipe: ingredients in groups', 'recipe', ingredient_groups([
    ('For the dough', ['500g plain flour', '250ml just-boiled water', '3 tbsp oil', 'A pinch of salt']),
    ('For the filling', ['150g roasted buckwheat', '300g mushrooms', '2 onions', 'Marjoram, salt and a lot of pepper'])]))
pattern('recipe-method-photos', 'Recipe: method with step photos', 'recipe', method([
    ('Mix the flour, hot water, oil and salt with a spoon, then knead for 5 minutes. Rest it under an upturned bowl for 30 minutes.', ('pierogi.jpg', 'Hands rolling pierogi dough on a floured board')),
    'Cook the buckwheat. Fry the onions and mushrooms until dark, then chop everything together.',
    ('Roll thin, cut circles, fill and pinch shut. Boil until they float, then 1 minute more.', ('mushrooms.jpg', 'Chanterelles in a woven basket'))]))
pattern('recipe-notes', 'Recipe: notes from my kitchen', 'recipe', notes_block('Notes from my kitchen', ['The dough should feel like an earlobe. Too sticky: more flour, a spoon at a time.', 'Make the filling the day before. It tastes better cold.']))
pattern('recipe-swaps', 'Recipe: swaps that work', 'recipe', notes_block('Swaps that work', ['No buckwheat: pearl barley, cooked soft.', 'No fresh mushrooms: 30g dried porcini, soaked.', 'Gluten-free: this one doesn\'t work, sorry. Try the kopytka instead.'], 'is-style-needs'))
pattern('recipe-storage', 'Recipe: storage and freezing', 'recipe', notes_block('Keeping it', ['Fridge: 3 days, covered.', 'Freezer: 3 months. Freeze on a tray first so they don\'t stick.', 'From frozen: straight into boiling water, 2 minutes longer.'], 'is-style-sky-box'))
pattern('recipe-jump', 'Recipe: jump to the recipe', 'recipe', buttons(('Jump to the recipe', '#ingredients')))
pattern('recipe-full', 'Recipe: the whole recipe (all blocks)', 'recipe', J(
    pattern_ref('recipe-intro'), pattern_ref('recipe-facts'), pattern_ref('recipe-jump'), pattern_ref('recipe-ingredients'), pattern_ref('recipe-method-photos'),
    pattern_ref('recipe-notes'), pattern_ref('recipe-swaps'), pattern_ref('recipe-storage')), block_types='core/post-content', post_types='post',
    description='Every recipe block in order: story, servings and times, ingredients in groups, method with photos, notes, swaps and storage.')
pattern('related-recipes', 'Recipe: more from the same shelf', 'posts', group(J(heading('More from the same shelf', 3), q(tile(), per_page=4, qid=9, layout=MOSAIC, pt_class='is-style-tiles')), align='wide', layout={'type': 'default'}))

def produce(img, alt, name, line, href):
    return group(J(image(img, alt, href=href), heading('<a href="%s">%s</a>' % (href, name), 3, fontSize='large'), para(line, fontSize='small')), className='is-style-produce-card')
pattern('produce-of-the-month', 'Good this month (produce cards)', 'seasons', group(J(
    row(J(heading('Good at the market this month', 2), para('<a href="/seasons/">The whole calendar</a>')), justify='space-between'),
    grid(J(produce('plums.jpg', 'A red plum, whole and halved', 'Plums', 'Węgierki, small and dark. Cake, powidła, compote.', '/tag/plums/'),
           produce('mushrooms.jpg', 'Chanterelles in a basket', 'Wild mushrooms', 'Chanterelles and ceps, from the woods near Spała.', '/tag/mushrooms/'),
           produce('cabbage.jpg', 'Savoy cabbages on a shelf', 'Cabbage', 'Braise it, or start a crock of sauerkraut.', '/tag/cabbage/'),
           produce('beetroot.jpg', 'A pile of beetroot', 'Beetroot', 'Buy a crate. It keeps on the balcony till March.', '/tag/beetroot/')), min_width='13rem', style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

pattern('kitchen-diary', 'Kitchen diary (short dated notes)', 'posts', group(J(
    heading('From the kitchen this week', 2),
    columns((None, J(para('Monday', fontFamily='display', fontSize='large', textColor='accent'), para('Made 4 litres of barszcz for the freezer. The flat smells of beetroot and I\'m fine with that.'))),
            (None, J(para('Wednesday', fontFamily='display', fontSize='large', textColor='accent'), para('Tested the plum cake with spelt flour. Denser, better. Recipe updated.'))),
            (None, J(para('Saturday', fontFamily='display', fontSize='large', textColor='accent'), para('Market at 8. Last cucumbers for pickling. <a href="/notes-from-the-market/">Notes from the market</a>'))))),
    align='wide', className='is-style-card', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

pattern('kitchen-gallery', 'From my kitchen (photo grid, opens large)', 'gallery', J(
    heading('From my kitchen this month', 3),
    gallery([('pickles.jpg', 'Jars of pickled cucumbers with dill', ''), ('rhubarb.jpg', 'Chopped rhubarb with sugar in a pot', ''), ('soup.jpg', 'Beetroot soup in a scalloped bowl', ''),
             ('beans.jpg', 'Dried broad beans', ''), ('dill.jpg', 'Bunches of dill at a market', ''), ('buckwheat.jpg', 'Roasted buckwheat groats', '')], columns=3, align='wide')))

pattern('glossary', 'Polish kitchen words', 'reference', group(J(
    heading('A few Polish kitchen words', 3),
    *[columns(('11rem', para('<strong>%s</strong>' % w)), (None, para(d)), isStackedOnMobile=False, className='is-style-dl-row', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}) for w, d in [
        ('Kasza', 'Any cooked grain. Kasza gryczana is buckwheat, usually roasted.'), ('Powidła', 'Plum butter, cooked for hours until nearly black. No pectin.'),
        ('Kompot', 'Fruit simmered in water and sugar, served cold as a drink.'), ('Kiszonki', 'Anything fermented in salt brine: cucumbers, cabbage, beetroot.'),
        ('Bób', 'Broad beans, sold boiled in paper cones in July.')]]), className='is-style-card'))
section('dl-row', 'Definition row', ['core/columns'], {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'dashed'}}, 'spacing': {'padding': {'bottom': 'var:preset|spacing|20'}}, 'css': '& p{margin:0}'})

pattern('workshop-card', 'Next workshop (card)', 'events', columns(
    ('40%', image('pierogi.jpg', 'Hands rolling out pierogi dough')),
    (None, J(heading('Pierogi without eggs, Saturday 11 October', 3), para('Three hours in my kitchen studio on Piotrkowska. Eight people, 180 zł, and you take home a box of pierogi. 3 places left.'), buttons(('Book a place by email', 'mailto:ola@example.com?subject=Workshop')))),
    verticalAlignment='center', className='is-style-card'))

pattern('about-short', 'About Ola (short, with photo)', 'about', columns(
    ('30%', image('dill.jpg', 'Bunches of dill at a market')),
    (None, J(heading('Cześć, I\'m Ola', 3), para('I cook plant-based Polish food in a tenement kitchen in Łódź and write it down here. One person, one oven, since 2016.'), para('<a href="/about/">More about me</a>'))),
    verticalAlignment='center'))

pattern('recipe-index-ingredient', 'Recipe index by vegetable', 'posts', group(J(
    heading('Recipes by vegetable', 3),
    lst(['<a href="/tag/beetroot/">Beetroot</a>', '<a href="/tag/cabbage/">Cabbage</a>', '<a href="/tag/mushrooms/">Mushrooms</a>', '<a href="/tag/plums/">Plums</a>', '<a href="/tag/dill/">Dill</a>', '<a href="/tag/rhubarb/">Rhubarb</a>', '<a href="/tag/broad-beans/">Broad beans</a>', '<a href="/tag/buckwheat/">Buckwheat</a>'], className='is-style-produce')),
    className='is-style-sky-box'))

pattern('print-note', 'Printing a recipe', 'recipe', para('Printing? Use your browser\'s print button. The photos stay, so choose "Background graphics off" to save ink.', fontSize='x-small', textColor='muted'))

pattern('contact-card', 'Contact (email and studio)', 'contact', columns(
    (None, J(heading('Email', 4), para('<a href="mailto:ola@example.com">ola@example.com</a><br>Answered on Fridays.'))),
    (None, J(heading('Kitchen studio', 4), para('ul. Piotrkowska 138, back courtyard, 2nd floor, Łódź. No lift. Only open for workshops.'))),
    (None, J(heading('Press and book', 4), para('Wydawnictwo Ogród, Magda Lis, <a href="mailto:magda@example.com">magda@example.com</a>')))))

print('larder: round 2 patterns written')

# ---------------- demo content (round 2: every recipe uses the full template)
R = []
def recipe(title, slug, cat, tags, img, excerpt, **kw):
    R.append(dict(title=title, slug=slug, category=cat, tags=tags, image=img, excerpt=excerpt, template='single-recipe', content=full_recipe(**kw)))

recipe('Plum cake that uses a whole kilo', 'plum-cake-whole-kilo', 'cakes', ['Plums', 'Baking'], 'plums.jpg', 'A kilo of węgierki in one tin. Oil, oat milk, no eggs, 1 hour.',
    story=['Every September my neighbour Pani Halina leaves a bag of węgierki on my door handle. Every September I make this.', 'It\'s the simplest cake I know. The plums sink a little and go jammy at the bottom. That\'s correct.'],
    facts=('12 pieces', '15 min', '50 min', 'Better on day two'),
    groups=[('For the batter', ['200g plain flour (or spelt)', '100g sugar', '2 tsp baking powder', 'A pinch of cinnamon', '120ml sunflower oil', '200ml oat milk']), ('For the top', ['1kg plums, halved and stoned', '2 tbsp sugar', 'A handful of flaked almonds'])],
    steps=['Heat the oven to 180°C. Oil a 24 × 30 cm tin and line the bottom with paper, because plum juice glues everything.',
           ('Whisk the dry things, then stir in the oil and oat milk until there are no dry bits. It will be thick, like porridge you forgot about.', ('buckwheat.jpg', 'Close view of grains')),
           ('Spread it in the tin, push the plums in skin side down, close together, and scatter the sugar and almonds over.', ('plums.jpg', 'Halved plum showing the stone')),
           'Bake for 50 minutes, until the edges are brown and the plums have slumped. Cool in the tin.'],
    notes=['Węgierki are drier than big plums. With juicy plums, add 2 tbsp flour to the batter.', 'Spelt flour makes it denser and nuttier. I prefer it now.'],
    swaps=['Frozen plums: straight from the freezer, 10 minutes longer.', 'Apples in October: thin slices, and more cinnamon.'],
    storage=['Room temperature: 3 days under a tea towel.', 'Freezer: in pieces, 2 months.'], aside='it works with frozen plums too')
recipe('Grandma Zosia\'s barszcz, with one change', 'barszcz-one-change', 'soups', ['Beetroot', 'Soup', 'Wigilia'], 'soup.jpg', 'Clear beetroot soup with sauerkraut brine in place of the starter. Makes 2 litres.',
    story=['Babcia Zosia made barszcz with a sour starter she kept going for weeks. I don\'t have the patience, so I use the brine from a jar of sauerkraut. She would say that\'s cheating. It is.', 'Serve it clear in a cup, or with cashew cream swirled in, like in the photo.'],
    facts=('Makes 2 litres', '20 min', '50 min', 'Better on day three'),
    groups=[('For the broth', ['1kg beetroot, peeled and sliced', '1 carrot, 1 parsley root', '4 dried porcini', '2 bay leaves, 4 allspice berries']), ('To finish', ['200ml sauerkraut brine', '2 garlic cloves, crushed', 'Salt, sugar, marjoram'])],
    steps=['Soak the porcini in a cup of hot water for 20 minutes.', ('Simmer the beetroot, roots, bay and allspice in 2 litres of water for 40 minutes. Don\'t let it boil hard or it goes brown.', ('beetroot.jpg', 'Beetroot at a market stall')),
           ('Strain, add the mushroom water, the brine and the garlic. Season until it\'s sour, sweet and salty all at once.', ('soup.jpg', 'A bowl of clear beetroot soup'))],
    notes=['Taste after every addition. The balance is the whole recipe.', 'Keep the cooked beetroot for a salad with horseradish.'],
    swaps=['No brine: juice of 1 lemon and 2 tbsp cider vinegar.', 'No porcini: 1 tbsp brown miso.'],
    storage=['Fridge: a week in a jar.', 'Freezer: 3 months, but don\'t freeze it with the cream in.'], aside='keeps a week, and tastes best on day three')
recipe('Pierogi with buckwheat and mushrooms', 'pierogi-buckwheat-mushrooms', 'mains', ['Pierogi', 'Mushrooms', 'Buckwheat'], 'pierogi.jpg', 'Egg-free dough, a kasza and mushroom filling, about 50 pierogi.',
    story=['The dough has no egg and nobody at my workshops has ever noticed. The trick is hot water and a rest.', 'The filling is kasza, fried onion and whatever mushrooms you found. Dried porcini make it taste like Christmas.'],
    facts=('Makes 50', '1 hr', '30 min', 'Freezes well'),
    groups=[('For the dough', ['500g plain flour', '250ml just-boiled water', '3 tbsp oil', 'A pinch of salt']), ('For the filling', ['150g roasted buckwheat', '300g mushrooms', '2 onions', 'Salt, pepper, marjoram']), ('To serve', ['1 onion, fried dark', 'Dill'])],
    steps=[('Mix the flour, hot water, oil and salt. Knead for 5 minutes and rest it under a bowl for 30.', ('pierogi.jpg', 'Hands rolling pierogi dough')),
           ('Cook the buckwheat. Fry the onions and mushrooms until dark, then chop everything together and season hard.', ('mushrooms.jpg', 'Chanterelles in a basket')),
           'Roll thin, cut circles, fill and pinch shut. Boil in batches until they float, then 1 minute more.', 'Serve with the fried onion and a lot of dill.'],
    notes=['Season the filling more than you think. The dough is plain.', 'A glass is fine for cutting circles. Mine is 8 cm.'],
    swaps=['Pearl barley for buckwheat.', 'Smoked tofu, crumbled, instead of half the mushrooms.'],
    storage=['Freeze on a tray, then in a bag. 3 months.', 'Cook from frozen, 2 minutes longer.'], aside='they freeze well, on a tray first')
recipe('Dill pickles in a 3-litre jar', 'dill-pickles', 'preserves', ['Pickles', 'Dill', 'Fermenting'], 'pickles.jpg', 'Salt-brine ogórki kiszone. No vinegar, a week on the counter.',
    story=['Ogórki kiszone, the salt-brine kind. No vinegar. They\'re sour because of time and nothing else.', 'Use small, firm cucumbers from the market in August, the ones with bumps. Big smooth ones go hollow.'],
    facts=('One 3-litre jar', '20 min', '7 days', 'Lasts until spring'),
    groups=[('In the jar', ['2kg small pickling cucumbers', '1 big bunch of dill with flowers', '6 garlic cloves', '2 horseradish leaves or a piece of root']), ('For the brine', ['2 litres water', '60g salt (not iodised)'])],
    steps=[('Wash the cucumbers in cold water. Pack them upright into the jar with the dill, garlic and horseradish.', ('dill.jpg', 'Bunches of dill')),
           'Dissolve the salt in the water and pour over until everything is covered. Weigh down with a small plate.',
           ('Leave on the counter for 3 days, then somewhere cool. Ready in a week.', ('pickles.jpg', 'Jars of pickles with dill'))],
    notes=['Cloudy brine is normal. White film on top: skim it off.', 'Horseradish leaves keep them crunchy. Oak or cherry leaves work too.'],
    swaps=['No horseradish: 2 bay leaves.'], storage=['Cellar or fridge: until spring.', 'Once opened: fridge, 2 weeks.'], aside='drink the brine, it\'s good for you')
recipe('Braised cabbage with smoked tofu and apple', 'braised-cabbage-tofu', 'mains', ['Cabbage', 'Apples'], 'cabbage.jpg', 'Bigos without the three days. One pan, 50 minutes.',
    story=['A winter pan of food that tastes of bigos without the three days.', 'Savoy or white cabbage, both fine. The apple goes soft and disappears, which is the point.'],
    facts=('4', '10 min', '40 min', 'Better next day'),
    groups=[('Vegetables', ['1 small cabbage, shredded', '2 apples, grated', '1 onion']), ('Everything else', ['200g smoked tofu, cubed', '2 tbsp tomato paste', '1 tsp caraway, 2 bay leaves'])],
    steps=['Fry the onion and tofu until brown.', ('Add the cabbage, apple, paste, caraway, bay and a cup of water. Cover.', ('cabbage.jpg', 'Savoy cabbages')), 'Cook gently for 40 minutes, stirring now and then. Season with salt and a lot of pepper.'],
    notes=['Add a handful of sauerkraut at the end for the full bigos taste.'], swaps=['Smoked tofu: 150g fried mushrooms and 1 tsp smoked paprika.'],
    storage=['Fridge: 4 days.', 'Freezer: 3 months.'], aside='eat it with potatoes and a pickle')
recipe('Broad beans with dill butter', 'broad-beans-dill', 'sides', ['Broad beans', 'Dill', 'Quick'], 'beans.jpg', 'July bób from a paper cone, on a plate. 10 minutes.',
    story=['Bób from a paper cone at the market in July, eaten warm, squeezed out of their skins. This is the same thing on a plate.'],
    facts=('2 as a snack', '2 min', '5 min'),
    groups=[('You need', ['500g broad beans in their skins', '2 tbsp plant butter', 'A big handful of dill', 'Flaky salt'])],
    steps=['Boil the beans in salted water for 4 minutes and drain.', ('Toss with the butter, chopped dill and salt.', ('dill.jpg', 'Fresh dill')), 'Eat with your hands. Pop them out of the skins as you go.'],
    notes=['Only in July. Frozen broad beans are fine in a stew but not here.'], swaps=['Good olive oil instead of butter.'], storage=['Eat them now.'], aside='only in July')
recipe('Rhubarb compote for May', 'rhubarb-compote', 'preserves', ['Rhubarb', 'Drinks'], 'rhubarb.jpg', 'The first kompot of the year. 3 litres, 10 minutes of cooking.',
    story=['Kompot is the drink of every Polish summer lunch: fruit, water, sugar, cooled. Rhubarb is the first one of the year.'],
    facts=('3 litres', '5 min', '10 min', 'Serve cold'),
    groups=[('You need', ['600g rhubarb, chopped', '3 litres water', '120g sugar', '1 strip of lemon peel'])],
    steps=['Bring the water to the boil with the sugar and peel.', ('Add the rhubarb and simmer for 5 minutes, no longer.', ('rhubarb.jpg', 'Chopped rhubarb with sugar')), 'Cool completely and serve cold with the fruit in.'],
    notes=['Strawberries go in from June.'], swaps=['Honey is not vegan, so I use sugar. Maple syrup works.'], storage=['Fridge: 4 days in a big jar.'], aside='make a big pot, it goes fast')
recipe('Chanterelles on toast', 'chanterelles-on-toast', 'mains', ['Mushrooms', 'Quick'], 'mushrooms.jpg', 'Brushed, fried dry, then onion and dill on rye. 15 minutes.',
    story=['Cleaned with a brush, not washed. Fried hot and dry first so they squeak, and only then the oil and onion.', 'This is breakfast after a morning in the woods near Spała.'],
    facts=('2', '5 min', '10 min'),
    groups=[('Mushrooms', ['300g chanterelles, brushed clean', '1 small onion', '2 tbsp oil']), ('To serve', ['4 slices rye bread', 'Dill, salt, pepper'])],
    steps=[('Fry the mushrooms in a dry hot pan until their water cooks off.', ('mushrooms.jpg', 'Chanterelles in a basket')), 'Add the oil and chopped onion and fry until golden.', 'Pile onto toasted rye and cover with dill.'],
    notes=['If you\'re not sure it\'s a chanterelle, take it to the sanepid inspector at the market. It\'s free.'], swaps=['Any firm wild mushroom, or oyster mushrooms from a shop.'], storage=['Eat it straight away.'], aside='don\'t wash them')

R.append(dict(title='Notes from the market, September', slug='notes-from-the-market', category='diary', tags=['Market'], image='cabbage.jpg', excerpt='Last cucumbers, first cabbages and the mushroom lady is back.',
              content=J(para('Saturday at Zielony Rynek, 8am. The cucumber crates are half the size they were a fortnight ago, which means pickling season is nearly over. The first white cabbages are in, huge and cheap.'),
                        para('The mushroom lady is back at her folding table by the tram stop. Chanterelles at 60 zł a kilo, ceps at 90. Cash only, as always.'),
                        pattern_ref('kitchen-gallery'), pattern_ref('market-day'), pattern_ref('about-short'))))
posts = R

content = {
    'site': {'title': 'Spiżarnia', 'tagline': 'Ola Wróbel\'s plant-based kitchen in Łódź'},
    'categories': [{'slug': 'soups', 'name': 'Soups'}, {'slug': 'mains', 'name': 'Mains'}, {'slug': 'sides', 'name': 'Sides'},
                   {'slug': 'cakes', 'name': 'Cakes'}, {'slug': 'preserves', 'name': 'Preserves and pickles'}, {'slug': 'diary', 'name': 'Kitchen diary'}],
    'front_page': 'home', 'posts_page': 'recipes',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'recipes', 'title': 'Recipes', 'content': ''},
        {'slug': 'seasons', 'title': 'What\'s in season', 'pattern': 'larder/season-page', 'template': 'page-wide'},
        {'slug': 'pantry-staples', 'title': 'What\'s in my larder', 'pattern': 'larder/pantry-staples-page', 'template': 'page-wide'},
        {'slug': 'workshops', 'title': 'Cooking workshops', 'pattern': 'larder/workshops-page'},
        {'slug': 'book', 'title': 'The book', 'pattern': 'larder/book-page', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'Hello, I\'m Ola', 'pattern': 'larder/about-page', 'template': 'page-wide'},
        {'slug': 'contact', 'title': 'Get in touch', 'pattern': 'larder/contact-page'},
        {'slug': 'how-a-recipe-works', 'title': 'How a recipe page works', 'pattern': 'larder/recipe-full'},
    ],
    'posts': posts,
    'nav': [{'label': 'Recipes', 'url': '/recipes/'}, {'label': 'Seasons', 'url': '/seasons/'}, {'label': 'My larder', 'url': '/pantry-staples/'},
            {'label': 'Workshops', 'url': '/workshops/'}, {'label': 'The book', 'url': '/book/'}, {'label': 'About me', 'url': '/about/'}],
}
os.makedirs(os.path.join(ROOT, 'demos', S), exist_ok=True)
with open(os.path.join(ROOT, 'demos', S, 'content.json'), 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
print('larder: content.json written')
