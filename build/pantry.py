# Design note (pantry, idea 058, owner's brief: "make it more like ottolenghi.co.uk or mob.co.uk")
# Direction: a loud, hungry recipe site for a cookbook author. Big overhead food photos with soft corners, a heavy
#   extended grotesk for headlines (Mob), white pages with pomegranate red and a lime panel (Ottolenghi's plates, Mob's colour).
# Fonts: Mona Sans (display, set at 125% width and 800 weight), Figtree (body). Two families, no monospace.
# Palette: white #FFFFFF, ink #16140F, pomegranate #C8102E, herb green #1E6B52, lime #E9F0A6, saffron #F4C542, line #E4E1D8.
# Layout idea: the recipe card is the page. Times and servings sit in a big four-cell strip, ingredients (grams first, cups
#   after) run in a narrow ruled column beside huge numbered steps, and a scaling table replaces the servings slider.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('pantry')
S = THEME['slug']
D = THEME['dir']
ROOT = os.path.abspath(os.path.join(D, '..', '..'))

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Mona Sans", "Arial Black", sans-serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"Figtree", "Helvetica Neue", Arial, sans-serif'

PAL = [
    ('base', '#FFFFFF', 'Plate'),
    ('contrast', '#16140F', 'Burnt'),
    ('accent', '#C8102E', 'Pomegranate'),
    ('accent-2', '#1E6B52', 'Herb'),
    ('surface', '#E9F0A6', 'Lime'),
    ('line', '#E4E1D8', 'Tahini'),
    ('muted', '#58544B', 'Pepper'),
    ('highlight', '#F4C542', 'Saffron'),
]
pal = lambda p: [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1380px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Tiny', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.6rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.5rem', 'name': 'Title', 'fluid': {'min': '2.3rem', 'max': '3.5rem'}},
                {'slug': 'display', 'size': '6rem', 'name': 'Display', 'fluid': {'min': '2.3rem', 'max': '6rem'}},
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'},
                {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'},
                {'slug': '40', 'size': 'clamp(1rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5.5rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|accent'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '0.98', 'letterSpacing': '-0.025em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.1'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.2', 'letterSpacing': '-0.01em'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                'border': {'radius': '999px', 'width': '0'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.85em', 'bottom': '0.85em', 'left': '1.5em', 'right': '1.5em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}},
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.03em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/image': {'border': {'radius': '18px'}},
            'core/post-featured-image': {'border': {'radius': '18px'}},
            'core/cover': {'border': {'radius': '24px'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.2'},
                           'border': {'width': '0'}, 'color': {'background': 'var:preset|color|surface'}, 'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '800'}, 'border': {'width': '0'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/search': {'border': {'radius': '999px'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/categories': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
            'core/tag-cloud': {'typography': {'fontWeight': '700'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
        },
        'css': (
            'body{font-synthesis:none}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
            ':where(h1,h2,h3,.wp-block-site-title,.wp-block-post-title){font-stretch:125%}'
            'table,.wp-block-table td{font-variant-numeric:tabular-nums}'
            '.wp-block-table table{border-collapse:collapse}.wp-block-table td,.wp-block-table th{border:0;border-bottom:2px solid var(--wp--preset--color--line);padding:.6em .8em .6em 0;text-align:left}'
            '.wp-block-table thead{border-bottom:3px solid var(--wp--preset--color--contrast)}.wp-block-table th{font-weight:800}'
            '.wp-block-search__input{border-radius:999px;border:2px solid var(--wp--preset--color--contrast);padding:.7em 1.2em}.wp-block-search__button{border-radius:999px}'
            ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'
            '.wp-block-navigation .current-menu-item>a{color:var(--wp--preset--color--accent)}@media (max-width:600px){:where(h1,h2,.wp-block-post-title){font-stretch:108%}header .wp-block-search{display:none}}'
            '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--surface)!important;font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large);font-weight:800}'
            '@media print{header,footer,.wp-block-post-featured-image,.wp-block-comments,.no-print{display:none!important}body{font-size:11pt}}'
            '@media (prefers-reduced-motion:no-preference){.wp-block-post-featured-image img,.wp-block-image img{transition:transform .3s ease}.wp-block-post-featured-image a:hover img{transform:scale(1.02)}}'
        ),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'single-plain', 'title': 'Post without the big photo', 'postTypes': ['post']},
    ],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Pantry
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A recipe site for cookbook authors and home cooks, with a recipe card that puts times, gram weights and a scaling table before any story.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: pantry
Tags: food-and-drink, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

# ---------------- section styles
def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

P = lambda n: {'top': 'var:preset|spacing|%s' % n, 'bottom': 'var:preset|spacing|%s' % n, 'left': 'var:preset|spacing|%s' % n, 'right': 'var:preset|spacing|%s' % n}
section('lime', 'Lime panel', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'border': {'radius': '28px'}, 'spacing': {'padding': P(60)}})
section('saffron', 'Saffron panel', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|highlight', 'text': 'var:preset|color|contrast'}, 'border': {'radius': '28px'}, 'spacing': {'padding': P(60)}})
section('pomegranate', 'Pomegranate panel', ['core/group', 'core/columns', 'core/media-text'], {
    'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'border': {'radius': '28px'}, 'spacing': {'padding': P(60)},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}}}})
section('recipe-card', 'Recipe card', ['core/group'], {
    'color': {'background': 'var:preset|color|base'}, 'border': {'radius': '28px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'spacing': {'padding': P(50)}})
section('facts', 'Recipe facts strip', ['core/group'], {
    'color': {'background': 'var:preset|color|surface'}, 'border': {'radius': '18px'}, 'spacing': {'padding': P(40)},
    'css': '& p:first-child{font-size:var(--wp--preset--font-size--x-small);font-weight:700;margin:0}& p:last-child{font-family:var(--wp--preset--font-family--display);font-weight:800;font-stretch:125%;font-size:var(--wp--preset--font-size--large);margin:0;line-height:1.1}'})
section('ingredients', 'Ingredient list', ['core/list'], {
    'css': '&{list-style:none;padding-left:0}&>li{border-bottom:2px dotted var(--wp--preset--color--line);padding:.45em 0}& strong{font-variant-numeric:tabular-nums}'})
section('steps', 'Big numbered steps', ['core/list'], {
    'css': '&{list-style:none;padding-left:0;counter-reset:step}&>li{counter-increment:step;position:relative;padding-left:3.2em;margin-bottom:1.1em;min-height:2.4em}&>li::before{content:counter(step);position:absolute;left:0;top:-.1em;font-family:var(--wp--preset--font-family--display);font-weight:900;font-stretch:125%;font-size:2em;line-height:1;color:var(--wp--preset--color--accent)}'})
section('chips', 'Chips', ['core/categories', 'core/tag-cloud', 'core/list'], {
    'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.5rem}& li,&>a{margin:0}& a{display:inline-block;text-decoration:none;border:2px solid var(--wp--preset--color--contrast);border-radius:999px;padding:.45em 1em;font-weight:700;color:var(--wp--preset--color--contrast);font-size:var(--wp--preset--font-size--small)!important}& a:hover{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'})
section('big-chips', 'Big ingredient chips', ['core/list', 'core/tag-cloud'], {
    'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.6rem}& a{display:inline-block;text-decoration:none;border-radius:999px;padding:.3em .8em;background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast);font-family:var(--wp--preset--font-family--display);font-weight:800;font-stretch:125%;font-size:var(--wp--preset--font-size--large)!important;letter-spacing:-.02em}& a:hover{background:var(--wp--preset--color--accent);color:var(--wp--preset--color--base)}'})
section('recipe-grid', 'Recipe grid', ['core/post-template'], {
    'css': '& .wp-block-post-featured-image{margin-bottom:.6rem}& .wp-block-post-title{margin-top:.4rem}'})
section('photo-grid', 'Photo grid (square crops)', ['core/group'], {
    'css': '&{grid-template-columns:repeat(2,minmax(0,1fr))!important}& img{aspect-ratio:1;object-fit:cover;width:100%;height:auto}& figure{margin:0}'})
section('outlined', 'Outlined panel', ['core/group', 'core/columns'], {
    'border': {'radius': '28px', 'width': '3px', 'style': 'solid', 'color': 'var:preset|color|contrast'}, 'spacing': {'padding': P(60)}})
section('notice', 'Notice bar', ['core/group'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}})
section('rule-top', 'Thick rule above', ['core/group'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|40'}}})

# ---------------- variations
def variation(fname, title, over, extra=None):
    p = {s: [c, n] for s, c, n in PAL}
    for s, c, n in over:
        p[s] = [c, n]
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': v[0], 'name': v[1]} for s, v in p.items()]}}}
    if extra:
        d['styles'] = extra
    jdump('styles/%s.json' % fname, d)

variation('diner', 'Diner', [('accent', '#B3121F', 'Ketchup'), ('surface', '#FFE3E0', 'Gingham'), ('highlight', '#FFD447', 'Mustard')])
variation('test-kitchen', 'Test kitchen', [('base', '#F1F2F0', 'Steel'), ('contrast', '#101412', 'Ink'), ('accent', '#0F6E5B', 'Mint'), ('accent-2', '#0A4F42', 'Bottle'),
          ('surface', '#FFFFFF', 'Card'), ('line', '#CFD4D0', 'Rule'), ('muted', '#4D5550', 'Pencil'), ('highlight', '#CDEBD9', 'Mint wash')],
          {'elements': {'heading': {'typography': {'fontWeight': '700', 'letterSpacing': '-0.01em'}}}})
variation('larder', 'Larder', [('base', '#F4F1E6', 'Parchment'), ('contrast', '#1E2116', 'Olive black'), ('accent', '#6B7A1E', 'Olive'), ('accent-2', '#4A5412', 'Caper'),
          ('surface', '#DDE3B8', 'Olive wash'), ('line', '#CFCAB6', 'Rule'), ('muted', '#50533F', 'Pepper'), ('highlight', '#E7C66A', 'Honey')])

# ---------------- helpers
def q(inner, per_page=6, offset=0, qid=1, pt_class=None, layout=None, **attrs):
    qq = {'perPage': per_page, 'pages': 0, 'offset': offset, 'postType': 'post', 'order': 'desc', 'orderBy': 'date', 'inherit': False}
    a = {'queryId': qid, 'query': qq, **attrs}
    pta = {}
    if pt_class: pta['className'] = pt_class
    if layout: pta['layout'] = layout
    return ('<!-- wp:query%s -->\n<div class="wp-block-query"><!-- wp:post-template%s -->\n%s\n<!-- /wp:post-template -->\n\n'
            '<!-- wp:query-no-results -->\n%s\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->') % (
        ' ' + json.dumps(a, separators=(',', ':')), (' ' + json.dumps(pta, separators=(',', ':'))) if pta else '', inner, para('No recipes here yet.'))

PAD = lambda t, b: {'spacing': {'padding': {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}}}
GRID = lambda n: {'type': 'grid', 'columnCount': n, 'minimumColumnWidth': '10rem'}

card = J(dyn('post-featured-image', isLink=True, aspectRatio='4/5'),
         dyn('post-terms', term='category', separator=', ', textColor='accent'),
         dyn('post-title', isLink=True, level=3, fontSize='large'),
         dyn('post-excerpt', excerptLength=24, moreText=''))

# ---------------- parts
write('parts/notice.html', pattern_ref('notice-book-tour'))
write('parts/header.html', J(
    template_part('notice'),
    group(row(J(
        dyn('site-title', level=0, fontSize='x-large'),
        dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'center'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
        dyn('search', label='Search recipes', showLabel=False, placeholder='Search', buttonText='Search', buttonPosition='button-inside', buttonUseIcon=True, width=220, widthUnit='px')),
        justify='space-between', align='wide'), tag='header', align='full', style=PAD(40, 40))))
write('parts/footer.html', group(J(
    group(J(
        heading('Hana Qasem', 2, fontSize='display', textColor='base'),
        columns(
            (None, para('Recipes from a small kitchen in Walthamstow, tested at least three times each, weighed in grams and written for a normal oven. New recipes on Thursdays.', fontSize='small')),
            (None, para('<a href="/cookbooks/">Cookbooks</a><br><a href="/conversions/">Weights and temperatures</a><br><a href="/about/">About Hana</a><br><a href="mailto:hello@example.com">hello@example.com</a>', fontSize='small')),
            (None, para('Recipe questions go in the comments, and Hana reads them on Mondays. For events and press, email Priya at <a href="mailto:priya@example.com">priya@example.com</a>.', fontSize='small')),
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
        para('Demo photographs are CC0 images from Wikimedia Commons, used as stand-ins for the author\'s own.', fontSize='x-small')),
        align='wide', backgroundColor='contrast', textColor='base', style={'border': {'radius': '28px'}, 'spacing': {'padding': P(60)}, 'elements': {'link': {'color': {'text': 'var:preset|color|base'}}}}, layout={'type': 'default'})),
    tag='footer', align='full', style=PAD(60, 40)))

# ---------------- templates
T = lambda inner, t=40, b=70: page_template(inner, style=PAD(t, b))
write('templates/front-page.html', T(J(
    pattern_ref('hero-lime'), pattern_ref('course-chips'), pattern_ref('new-recipes'), pattern_ref('cookbook-promo'),
    pattern_ref('cook-this-weekend'), pattern_ref('ingredient-index'), pattern_ref('newsletter')), 20, 60))
archive_grid = inherit_query(card, layout=GRID(4), template_class='is-style-recipe-grid', align='wide')
pattern('recipe-grid-archive', 'Recipe grid (inherits the page query)', 'query', archive_grid, inserter=False)
write('templates/home.html', T(J(
    heading('All the recipes', 1, align='wide', fontSize='display'),
    columns((None, J(heading('By course', 6), dyn('categories', className='is-style-chips'))),
            (None, J(heading('By diet or ingredient', 6), dyn('tag-cloud', className='is-style-chips', smallestFontSize='1rem', largestFontSize='1rem'))), align='wide'),
    pattern_ref('recipe-grid-archive'))))
write('templates/index.html', T(J(dyn('query-title', type='archive', align='wide'), pattern_ref('recipe-grid-archive'))))
write('templates/archive.html', T(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='display'),
    dyn('term-description', align='wide'),
    dyn('categories', className='is-style-chips', align='wide'),
    pattern_ref('recipe-grid-archive'))))
write('templates/search.html', T(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search recipes', showLabel=False, placeholder='Try lemon, or 30 minutes', buttonText='Search', align='wide'),
    pattern_ref('recipe-grid-archive'))))
write('templates/404.html', T(J(
    heading('That recipe isn\'t here', 1, fontSize='display'),
    para('It may have moved when the recipes were sorted into courses. Search for the main ingredient, it\'s usually quicker.'),
    dyn('search', label='Search recipes', showLabel=False, placeholder='Search recipes or an ingredient', buttonText='Search')), 70, 80))
write('templates/page.html', T(J(dyn('post-title', level=1, fontSize='display'), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', T(J(dyn('post-title', level=1, fontSize='display', align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1380px'}))))

def single(img=True):
    head = columns(
        ('55%', J(dyn('post-terms', term='category', separator=', ', textColor='accent'),
                  dyn('post-title', level=1, fontSize='display'),
                  dyn('post-excerpt', fontSize='large'),
                  row(J(buttons(('Jump to recipe', '#recipe')), dyn('post-date', format='j F Y')), style={'spacing': {'blockGap': 'var:preset|spacing|40'}}))),
        (None, dyn('post-featured-image', aspectRatio='4/5') if img else ''),
        align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})
    return T(J(head,
               dyn('post-content', layout={'type': 'constrained'}),
               group(J(heading('Tags', 6), dyn('post-terms', term='post_tag', className='is-style-chips')), className='no-print'),
               group(J(heading('Cook something else', 2), q(card, per_page=4, qid=5, layout=GRID(4), pt_class='is-style-recipe-grid')), align='wide', className='is-style-rule-top no-print', layout={'type': 'default'}),
               ), 40, 70)
write('templates/single.html', single())
write('templates/single-plain.html', single(False))

# ---------------- patterns
pattern('hero-lime', 'Hero: lime panel with photos', 'featured', columns(
    ('52%', J(heading('Mostly vegetables, a lot of lemon, dinner by eight.', 1, fontSize='display'),
              para('I\'m Hana Qasem. I write recipes for people who cook after work: one tray, one pot, weights in grams, and a note on what to do with the leftovers. New recipes every Thursday.', fontSize='large'),
              buttons(('See this week\'s recipes', '/recipes/'), ('Browse by ingredient', '#ingredients', {'className': 'is-style-outline'})))),
    (None, grid(J(image('hero.jpg', 'Shakshuka in a black pan, four eggs set in tomato sauce, with bread and cutlery on a dark table'),
                  image('cauliflower.jpg', 'Roast cauliflower with turmeric on a white plate'),
                  image('salad.jpg', 'A chopped salad of tomato, carrot and herbs in a terracotta bowl'),
                  image('chickpea.jpg', 'A bowl of chickpeas in tomato sauce with flatbread on a yellow table')), min_width='8rem', style={'spacing': {'blockGap': 'var:preset|spacing|20'}}, className='is-style-photo-grid')),
    align='wide', verticalAlignment='center', className='is-style-lime', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('course-chips', 'Browse by course (chips)', 'posts', group(J(
    dyn('categories', className='is-style-chips')), align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|30'}}}))

pattern('new-recipes', 'New recipes (grid)', 'posts,query', group(J(
    row(J(heading('New this month', 2, fontSize='xx-large'), para('<a href="/recipes/">All recipes</a>', fontSize='small')), justify='space-between'),
    q(card, per_page=8, qid=2, layout=GRID(4), pt_class='is-style-recipe-grid')), align='wide', layout={'type': 'default'}))

pattern('cookbook-promo', 'Cookbook promo', 'featured,shop', columns(
    ('45%', image('flatbread.jpg', 'Hummus topped with falafel and pickled carrot, with flatbread in a basket behind')),
    (None, J(heading('One Tray, Most Nights', 2, fontSize='xx-large'),
             para('My second book is 80 traybakes that go in the oven at 200°C and come out as dinner. Out 2 October from Kestrel Press, 288 pages, £26.'),
             para('Independent shops get signed bookplates while they last. I\'ll sign anything you bring to an event, including the first book.', fontSize='small'),
             buttons(('Buy from Bookshop.org', 'https://uk.bookshop.org/'), ('Where I\'m signing', '/cookbooks/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='center', className='is-style-saffron', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'margin': {'top': 'var:preset|spacing|70'}}}))

pattern('cook-this-weekend', 'Cook this weekend (big photo)', 'featured', media_text('rice.jpg', 'Saffron rice with a golden crust next to a tray of dark braised meat, on foil', J(
    heading('Weekend project: saffron rice with a crust', 2, fontSize='xx-large'),
    para('Two hours, mostly waiting. The crust on the bottom is the point, and it comes out in one piece if you\'re brave with the flip.'),
    buttons(('Get the recipe', '/saffron-rice-crust/'))), width=62, align='wide', className='is-style-pomegranate', style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

pattern('ingredient-index', 'Recipe index by ingredient', 'posts', group(J(
    heading('What\'s in your fridge?', 2, fontSize='xx-large'),
    para('Recipes by the ingredient you need to use up. Tap one.'),
    dyn('tag-cloud', className='is-style-big-chips', smallestFontSize='1.5rem', largestFontSize='1.5rem')),
    align='wide', anchor='ingredients', className='is-style-lime', layout={'type': 'constrained', 'contentSize': '980px', 'justifyContent': 'left'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

pattern('newsletter', 'Newsletter', 'call-to-action', group(columns(
    ('55%', J(heading('Thursday recipes, by email', 2, fontSize='xx-large'), para('One new recipe a week, what I\'m cooking at home, and the odd event date. It comes from me, it\'s free, and you can unsubscribe from any email.'))),
    (None, J(buttons(('Email me to sign up', 'mailto:hello@example.com?subject=Thursday%20recipes')), para('About 1 email a week. Never more than 2.', fontSize='x-small'))),
    verticalAlignment='center'), align='wide', className='is-style-outlined', anchor='newsletter', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

pattern('notice-book-tour', 'Notice: book tour', 'banner', group(
    para('Signing One Tray, Most Nights at Pages of Hackney on 4 October, 2pm. Free, no ticket. <a href="/cookbooks/">All dates</a>', align='center'),
    align='full', className='is-style-notice', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
    description='A notice bar for a book launch or a posting cut-off. Take it out when the date passes.')

# --- Signature: recipe card
def recipe_card(name, facts, ingredients, steps, scale=None, notes=None, subs=None):
    fx = grid(J(*[group(J(para(k), para(v)), className='is-style-facts', style={'spacing': {'blockGap': 'var:preset|spacing|10'}}) for k, v in facts]), min_width='9rem', style={'spacing': {'blockGap': 'var:preset|spacing|20'}})
    parts = [row(J(heading(name, 2, fontSize='xx-large'), para('Print it and the photos and comments drop out.', fontSize='x-small', textColor='muted', className='no-print')), justify='space-between'),
             fx,
             columns(('36%', J(heading('Ingredients', 3), lst(ingredients, className='is-style-ingredients'))),
                     (None, J(heading('Method', 3), lst(steps, ordered=True, className='is-style-steps'))),
                     style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})]
    if scale:
        parts.append(details('Cooking for more or fewer people?', table(scale[1], head=scale[0])))
    if notes:
        parts.append(details('Make ahead and storage', para(notes)))
    if subs:
        parts.append(details('Swaps that work', lst(subs)))
    return group(J(*parts), anchor='recipe', className='is-style-recipe-card')

SHAK = recipe_card('Shakshuka with preserved lemon and feta',
    [('Serves', '4'), ('Prep', '10 min'), ('Cook', '25 min'), ('Total', '35 min')],
    ['<strong>3 tbsp</strong> olive oil', '<strong>2</strong> onions, thinly sliced', '<strong>2</strong> red peppers, sliced', '<strong>3</strong> garlic cloves, crushed',
     '<strong>2 tsp</strong> cumin seeds', '<strong>1 tbsp</strong> rose harissa', '<strong>800g</strong> tinned plum tomatoes (2 tins)', '<strong>½</strong> preserved lemon, rind only, chopped',
     '<strong>6</strong> eggs', '<strong>100g</strong> feta (¾ cup crumbled)', 'A small bunch of coriander'],
    ['Heat the oil in a 28cm frying pan over a medium heat. Cook the onions and peppers with ½ tsp salt for 12 minutes, until soft and just catching.',
     'Add the garlic, cumin and harissa and cook for 1 minute. Tip in the tomatoes, crush them with a spoon, add the preserved lemon and simmer for 10 minutes.',
     'Make six hollows in the sauce and crack an egg into each. Cover and cook for 6 to 8 minutes, until the whites are set and the yolks still move.',
     'Crumble over the feta, tear over the coriander and bring the pan to the table.'],
    scale=(['Ingredient', 'Serves 2', 'Serves 4', 'Serves 6'], [['Tinned tomatoes', '400g', '800g', '1.2kg'], ['Eggs', '3', '6', '9'], ['Feta', '50g', '100g', '150g'], ['Pan', '20cm', '28cm', 'Two 24cm']]),
    notes='The sauce keeps for 3 days in the fridge and freezes for 2 months. Reheat it until bubbling before you add the eggs. Cooked eggs don\'t reheat well.',
    subs=['No preserved lemon: the zest of a whole lemon and a pinch more salt.', 'No harissa: 1 tsp chilli flakes and 1 tsp sweet paprika.', 'Vegan: leave out the eggs and feta, add a drained tin of butter beans at step 2.'])

pattern('recipe-card', 'Recipe card (the signature)', 'recipe,featured', SHAK,
        description='Facts strip, ingredients in grams with cups after, numbered method, a scaling table, storage and swaps. Anchored as #recipe for the Jump to recipe button.')

pattern('headnote', 'Headnote (short)', 'recipe', J(
    para('This is what we eat on Mondays, because everything in it keeps: tins, eggs, a jar of preserved lemons. The lemon is the thing people ask about. It makes the sauce taste like it cooked for longer than it did.'),
    buttons(('Jump to recipe', '#recipe'))))

pattern('jump-link', 'Jump to recipe button', 'recipe', buttons(('Jump to recipe', '#recipe')),
        description='Put this at the top of a recipe post. It scrolls to the recipe card, which carries the #recipe anchor.')

pattern('recipe-facts', 'Recipe facts strip (times and servings)', 'recipe', grid(J(*[group(J(para(k), para(v)), className='is-style-facts') for k, v in [('Serves', '4'), ('Prep', '15 min'), ('Cook', '40 min'), ('Total', '55 min')]]), min_width='9rem'))

pattern('ingredients-list', 'Ingredients (grams, then cups)', 'recipe', J(heading('Ingredients', 3), lst(
    ['<strong>250g</strong> plain flour (2 cups)', '<strong>200g</strong> caster sugar (1 cup)', '<strong>3</strong> eggs', '<strong>150ml</strong> olive oil (⅔ cup)', '<strong>2</strong> lemons, zest and juice'], className='is-style-ingredients')))

pattern('method-steps', 'Method (big numbered steps)', 'recipe', J(heading('Method', 3), lst(
    ['Heat the oven to 180°C (160°C fan, 350°F). Line a 900g loaf tin.', 'Whisk the sugar, eggs and zest for 2 minutes, then whisk in the oil.', 'Fold in the flour and a pinch of salt. Pour into the tin.', 'Bake for 50 minutes, until a skewer comes out clean. Pour over the lemon juice while it\'s hot.'], ordered=True, className='is-style-steps')))

pattern('scaling-table', 'Scaling table (servings)', 'recipe', J(
    heading('Cooking for more or fewer?', 4),
    table([['Chickpeas (drained)', '240g', '480g', '720g'], ['Tinned tomatoes', '400g', '800g', '1.2kg'], ['Pan', '24cm', '28cm', 'Casserole']], head=['Ingredient', 'Serves 2', 'Serves 4', 'Serves 6']),
    para('Spices don\'t scale in a straight line. For 6, use one and a half times the spice, then taste.', fontSize='small')),
    description='Stands in for a servings slider: the quantities that change, at three sizes.')

pattern('storage-notes', 'Make ahead and storage', 'recipe', J(
    heading('Make ahead and storage', 4),
    lst(['Fridge: 3 days in a lidded box.', 'Freezer: 2 months. Thaw overnight in the fridge.', 'Make ahead: cook to the end of step 2 the day before.'])))

pattern('substitutions', 'Swaps that work', 'recipe', J(
    heading('Swaps that work', 4),
    lst(['Feta: ricotta salata, or a firm goat\'s cheese.', 'Coriander: parsley and mint, half and half.', 'Gluten-free: serve with rice instead of bread. Nothing else in the recipe has gluten.'])))

pattern('pan-size-note', 'Pan size note', 'recipe', group(para('<strong>Pan size matters here.</strong> A 28cm frying pan fits six eggs with room between them. In a smaller pan the whites run together and take 3 minutes longer.', fontSize='small'),
    className='is-style-lime', style={'spacing': {'padding': P(40)}}))

pattern('reader-notes', 'Reader notes ("I made it")', 'recipe,testimonials', J(
    heading('People who made it', 3),
    columns(
        (None, quote('Made it with the preserved lemon from the corner shop. My kids ate the sauce with a spoon.', 'Tomasz, Leyton, September 2026')),
        (None, quote('Halved it for two in a 20cm pan and it worked exactly, 7 minutes for the eggs.', 'Aoife, Galway, August 2026')), align='wide')))

pattern('diet-labels', 'Diet labels row', 'recipe', group(lst(['<a href="/tag/vegetarian/">Vegetarian</a>', '<a href="/tag/gluten-free/">Gluten-free</a>', '<a href="/tag/under-30-minutes/">Under 30 minutes</a>'], className='is-style-chips')))

pattern('recipe-post', 'Recipe post (headnote and card)', 'recipe', J(pattern_ref('headnote'), SHAK, pattern_ref('reader-notes')), block_types='core/post-content', post_types='post')

# Conversions
pattern('conversions-oven', 'Oven temperatures', 'reference', J(
    heading('Oven temperatures', 2),
    table([['Low', '150°C', '130°C', '300°F', '2'], ['Moderate', '180°C', '160°C', '350°F', '4'], ['Hot', '200°C', '180°C', '400°F', '6'], ['Very hot', '220°C', '200°C', '425°F', '7'], ['Grill-hot', '240°C', '220°C', '475°F', '9']],
          head=['', 'Conventional', 'Fan', 'Fahrenheit', 'Gas mark'], caption='My recipes give the conventional temperature first. If your oven runs hot, trust your nose.')))
pattern('conversions-weights', 'Cups to grams', 'reference', J(
    heading('Cups to grams', 2),
    table([['Plain flour', '1 cup', '125g'], ['Caster sugar', '1 cup', '200g'], ['Butter', '1 stick', '113g'], ['Rice (uncooked)', '1 cup', '190g'], ['Red lentils', '1 cup', '200g'], ['Feta, crumbled', '1 cup', '135g'], ['Olive oil', '1 cup', '240ml']],
          head=['Ingredient', 'US cup', 'Weight']),
    para('Cups are a guess for flour, which is why I weigh. A £12 scale will change your baking more than any recipe.', fontSize='small')))
pattern('conversions-spoons', 'Spoons and small amounts', 'reference', J(
    heading('Spoons', 2),
    table([['1 tsp', '5ml'], ['1 tbsp', '15ml (3 tsp)'], ['A pinch', 'Less than ⅛ tsp, between two fingers'], ['A knob of butter', 'About 15g']], head=['Measure', 'What it means'])))
pattern('conversions-page', 'Page: weights and temperatures', 'reference', J(
    para('Every recipe here is written in grams and conventional oven temperatures, with cups in brackets where it helps. These tables are the ones I keep taped inside a cupboard door.', fontSize='large'),
    columns((None, pattern_ref('conversions-oven')), (None, pattern_ref('conversions-weights')), align='wide'),
    pattern_ref('conversions-spoons')), block_types='core/post-content')

# Cookbooks and events
pattern('cookbooks-list', 'Cookbooks', 'shop', J(
    columns(
        (None, J(image('flatbread.jpg', 'Hummus with falafel and pickled carrots on a white plate'), heading('One Tray, Most Nights', 3), para('Kestrel Press, 2 October 2026. 80 traybakes, 288 pages, £26.'),
                 buttons(('Buy from Bookshop.org', 'https://uk.bookshop.org/')))),
        (None, J(image('lentils.jpg', 'Red lentil soup with carrot in a pale blue bowl, a spoon resting in it'), heading('A Tin of Chickpeas', 3), para('Kestrel Press, 2023. 100 recipes built on tins and jars, 256 pages, £22. Now in paperback at £14.99.'),
                 buttons(('Buy from Bookshop.org', 'https://uk.bookshop.org/')))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})))
pattern('events-list', 'Book events', 'events', J(
    heading('Where I\'m signing', 2),
    table([['Sat 4 Oct, 2pm', 'Pages of Hackney, London E5', 'Free, just turn up'], ['Thu 9 Oct, 7pm', 'Toppings, Bath', '£8, includes a glass of wine'], ['Sat 18 Oct, 11am', 'Leeds Kirkgate Market, demo kitchen', 'Free'], ['Wed 5 Nov, 6:30pm', 'Waterstones Walthamstow', 'Free, book a seat']],
          head=['When', 'Where', 'Tickets'])))
pattern('cookbooks-page', 'Page: cookbooks', 'shop', J(pattern_ref('cookbooks-list'), pattern_ref('events-list'),
    para('Signed copies by post: order from Pages of Hackney and write "signed" in the note. They\'ll send it once I\'ve been in, usually within a week.', fontSize='small')), block_types='core/post-content')

# About
pattern('about-page', 'Page: about', 'about', J(
    columns(('40%', image('herbs.jpg', 'Bunches of fresh herbs and a red pepper on a wooden board')),
            (None, J(para('I\'m Hana Qasem. I grew up in Amman and Leicester, trained as a pharmacist, and started writing recipes in 2016 when I got tired of reading about someone\'s holiday before finding out how long the chicken goes in for.', fontSize='large'),
                     para('Every recipe here is tested at least three times in my kitchen in Walthamstow, on a normal electric oven that runs about 10 degrees hot. My neighbour Olu tests the baking in his gas oven, which is how the gas marks got in.'),
                     para('I write two recipes a week, one quick and one for the weekend. I don\'t do sponsored posts for supermarkets, and I don\'t use air fryers, though I\'m told I should.'),
                     para('For press and events, email Priya Shah at <a href="mailto:priya@example.com">priya@example.com</a>. For recipe questions, the comments are best.'))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('cookbooks-list')), block_types='core/post-content')

pattern('recipe-index-course', 'Recipe index by course (text)', 'posts', columns(
    (None, J(heading('Weeknight', 4), lst(['<a href="/category/dinner/">Shakshuka with preserved lemon</a>', '<a href="/category/dinner/">Chickpeas with cumin and flatbread</a>', '<a href="/category/dinner/">Pappardelle with sage butter</a>']))),
    (None, J(heading('Traybakes', 4), lst(['<a href="/category/traybakes/">Roast cauliflower, turmeric butter</a>', '<a href="/category/traybakes/">Aubergine with miso and tomato</a>']))),
    (None, J(heading('Baking', 4), lst(['<a href="/category/baking/">Lemon and olive oil loaf</a>']))),
    (None, J(heading('Soups', 4), lst(['<a href="/category/soups/">Red lentil soup, crispy onions</a>', '<a href="/category/soups/">Miso broth with greens</a>']))), align='wide'))

pattern('page-landing', 'Page: recipe landing', 'posts', J(pattern_ref('course-chips'), pattern_ref('new-recipes'), pattern_ref('ingredient-index')), block_types='core/post-content')

print('pantry: patterns written')

# ---------------- demo content
def post_body(headnote, card_):
    return J(para(headnote), card_)

R = []
def recipe(title, slug, cat, tags, img, excerpt, headnote, **card_kw):
    R.append(dict(title=title, slug=slug, category=cat, tags=tags, image=img, excerpt=excerpt, content=post_body(headnote, recipe_card(title, **card_kw))))

R.append(dict(title='Shakshuka with preserved lemon and feta', slug='shakshuka-preserved-lemon', category='dinner', tags=['Vegetarian', 'Eggs', 'Under 30 minutes', 'Tins'], image='hero.jpg',
              excerpt='35 minutes, serves 4. Everything in it keeps, which is why we have it on Mondays.',
              content=J(pattern_ref('headnote').replace(pattern_ref('headnote'), para('This is what we eat on Mondays, because everything in it keeps: tins, eggs, a jar of preserved lemons. The lemon is the thing people ask about. It makes the sauce taste like it cooked for longer than it did.')),
                        SHAK)))
recipe('Roast cauliflower with turmeric butter and dates', 'roast-cauliflower-turmeric', 'traybakes', ['Vegetarian', 'Gluten-free', 'Cauliflower'], 'cauliflower.jpg',
       '50 minutes, serves 4 as a side or 2 as dinner.', 'Roast the whole head, leaves and all. The leaves go crisp like crisps and people fight over them.',
       facts=[('Serves', '4'), ('Prep', '10 min'), ('Cook', '40 min'), ('Total', '50 min')],
       ingredients=['<strong>1</strong> large cauliflower, about 1kg', '<strong>60g</strong> butter (4 tbsp)', '<strong>1 tsp</strong> ground turmeric', '<strong>1 tsp</strong> cumin seeds', '<strong>6</strong> Medjool dates, torn', '<strong>30g</strong> toasted almonds (¼ cup)', 'Parsley and a lemon, to finish'],
       steps=['Heat the oven to 220°C (200°C fan). Cut the cauliflower into 8 wedges through the stalk, keeping the leaves on.', 'Melt the butter with the turmeric and cumin. Toss the cauliflower in it with 1 tsp salt and spread on a large tray.', 'Roast for 30 minutes, turn, add the dates and roast for 10 more.', 'Scatter over almonds, parsley and a squeeze of lemon.'],
       notes='Best straight from the oven. Leftovers are good cold the next day, chopped into a grain salad.')
recipe('Chickpeas with tomato, cumin and warm flatbread', 'chickpeas-tomato-cumin', 'dinner', ['Vegan', 'Chickpeas', 'Tins', 'Under 30 minutes'], 'chickpea.jpg',
       '25 minutes, serves 4. Two tins and a spice drawer.', 'The recipe that the first book was named after, more or less. Mash some of the chickpeas against the side of the pan and the sauce thickens by itself.',
       facts=[('Serves', '4'), ('Prep', '5 min'), ('Cook', '20 min'), ('Total', '25 min')],
       ingredients=['<strong>3 tbsp</strong> olive oil', '<strong>1</strong> onion, chopped', '<strong>2 tsp</strong> ground cumin', '<strong>1 tsp</strong> smoked paprika', '<strong>2 × 400g</strong> tins chickpeas, drained', '<strong>400g</strong> tinned chopped tomatoes', '<strong>4</strong> flatbreads'],
       steps=['Soften the onion in the oil for 8 minutes.', 'Add the spices for 1 minute, then the chickpeas, tomatoes and 150ml water.', 'Simmer for 10 minutes, mashing a third of the chickpeas as you go.', 'Warm the flatbreads in a dry pan and serve.'],
       scale=(['Ingredient', 'Serves 2', 'Serves 4', 'Serves 6'], [['Chickpeas', '1 tin', '2 tins', '3 tins'], ['Tomatoes', '200g', '400g', '600g']]))
recipe('Hummus with crispy chickpeas and chilli butter', 'hummus-chilli-butter', 'sides', ['Vegetarian', 'Gluten-free', 'Chickpeas'], 'hummus.jpg',
       '20 minutes, serves 6 as a starter.', 'The trick is ice-cold water and more tahini than feels right. Don\'t bother peeling the chickpeas.',
       facts=[('Serves', '6'), ('Prep', '15 min'), ('Cook', '5 min'), ('Total', '20 min')],
       ingredients=['<strong>2 × 400g</strong> tins chickpeas', '<strong>120g</strong> tahini (½ cup)', '<strong>1</strong> lemon, juiced', '<strong>1</strong> small garlic clove', '<strong>4 tbsp</strong> iced water', '<strong>40g</strong> butter', '<strong>1 tsp</strong> Aleppo chilli'],
       steps=['Keep a handful of chickpeas back. Blend the rest with the tahini, lemon, garlic and 1 tsp salt for 2 minutes.', 'With the motor running, add the iced water a spoon at a time until pale and smooth.', 'Fry the reserved chickpeas in the butter until crisp, then add the chilli.', 'Spread the hummus in a wide bowl and pour the butter over.'])
recipe('Red lentil soup with lemon and crispy onions', 'red-lentil-soup', 'soups', ['Vegan', 'Gluten-free', 'Lentils'], 'lentils.jpg',
       '40 minutes, serves 4. Freezes well.', 'My mum\'s soup, with more lemon than she\'d use. The crispy onions are optional but they make it dinner.',
       facts=[('Serves', '4'), ('Prep', '10 min'), ('Cook', '30 min'), ('Total', '40 min')],
       ingredients=['<strong>250g</strong> red lentils (1¼ cups)', '<strong>1</strong> onion, chopped', '<strong>1</strong> carrot, grated', '<strong>2 tsp</strong> cumin', '<strong>1.2 litres</strong> stock (5 cups)', '<strong>1</strong> lemon', '<strong>2</strong> onions, sliced, for frying'],
       steps=['Soften the chopped onion and carrot in oil for 8 minutes.', 'Add the cumin, lentils and stock. Simmer for 20 minutes until the lentils collapse.', 'Blend half, stir back in, and season with lemon juice and salt.', 'Fry the sliced onions slowly until dark and crisp, and pile on top.'],
       notes='Keeps 4 days in the fridge and 3 months in the freezer. It thickens as it sits, so add water when you reheat.')
recipe('Lemon and olive oil loaf', 'lemon-olive-oil-loaf', 'baking', ['Vegetarian', 'Dairy-free', 'Lemon', 'Baking'], 'cake.jpg',
       '1 hour 5 minutes, makes 10 slices.', 'No butter, no mixer. It keeps for a week and gets better on day two.',
       facts=[('Makes', '10 slices'), ('Prep', '15 min'), ('Bake', '50 min'), ('Total', '1 hr 5 min')],
       ingredients=['<strong>250g</strong> plain flour (2 cups)', '<strong>2 tsp</strong> baking powder', '<strong>200g</strong> caster sugar (1 cup)', '<strong>3</strong> eggs', '<strong>150ml</strong> olive oil (⅔ cup)', '<strong>2</strong> lemons, zest and juice'],
       steps=['Heat the oven to 180°C (160°C fan, 350°F). Line a 900g loaf tin.', 'Whisk the sugar, eggs and zest for 2 minutes, then whisk in the oil.', 'Fold in the flour, baking powder and a pinch of salt.', 'Bake for 50 minutes, until a skewer comes out clean. Pour over the lemon juice while it\'s hot.'])
recipe('Saffron rice with a crust', 'saffron-rice-crust', 'sides', ['Gluten-free', 'Vegetarian', 'Rice', 'Weekend'], 'rice.jpg',
       '2 hours, mostly waiting. Serves 6.', 'The weekend project. The crust on the bottom is the point, and it comes out in one piece if you\'re brave with the flip.',
       facts=[('Serves', '6'), ('Prep', '20 min'), ('Cook', '1 hr 40 min'), ('Total', '2 hr')],
       ingredients=['<strong>400g</strong> basmati rice (2 cups)', '<strong>½ tsp</strong> saffron threads', '<strong>60g</strong> butter', '<strong>3 tbsp</strong> yoghurt', '<strong>40g</strong> barberries or cranberries'],
       steps=['Soak the rice for 1 hour. Steep the saffron in 4 tbsp hot water.', 'Boil the rice for 6 minutes in well-salted water and drain.', 'Mix a third of the rice with the yoghurt and half the saffron and press into a buttered non-stick pan.', 'Pile in the rest, poke holes, add the butter, cover tightly and cook on low for 45 minutes. Flip onto a plate.'])
recipe('Aubergine with miso and tomato', 'aubergine-miso-tomato', 'traybakes', ['Vegan', 'Aubergine'], 'aubergine.jpg',
       '45 minutes, serves 4.', 'Salty, sweet and soft all the way through. Score the aubergine deeply so the miso gets in.',
       facts=[('Serves', '4'), ('Prep', '10 min'), ('Cook', '35 min'), ('Total', '45 min')],
       ingredients=['<strong>3</strong> aubergines', '<strong>3 tbsp</strong> white miso', '<strong>1 tbsp</strong> maple syrup', '<strong>4 tbsp</strong> olive oil', '<strong>300g</strong> cherry tomatoes'],
       steps=['Heat the oven to 220°C (200°C fan). Halve the aubergines and score the flesh in a criss-cross.', 'Mix the miso, maple syrup and oil and brush it over.', 'Roast cut side up for 25 minutes, add the tomatoes and roast for 10 more.'])
recipe('Pappardelle with brown butter, sage and lemon', 'pappardelle-brown-butter', 'dinner', ['Vegetarian', 'Pasta', 'Under 30 minutes'], 'pasta.jpg',
       '20 minutes, serves 2.', 'A two-person dinner for when the fridge is empty and there\'s a lemon rolling around.',
       facts=[('Serves', '2'), ('Prep', '5 min'), ('Cook', '15 min'), ('Total', '20 min')],
       ingredients=['<strong>200g</strong> pappardelle', '<strong>60g</strong> butter', '<strong>12</strong> sage leaves', '<strong>1</strong> lemon, zest only', '<strong>40g</strong> parmesan'],
       steps=['Cook the pasta in well-salted water.', 'Meanwhile, cook the butter and sage until the butter smells nutty and the sage crisps.', 'Toss the pasta with the butter, zest, parmesan and a splash of pasta water.'])

content = {
    'site': {'title': 'Hana Qasem', 'tagline': 'Recipes for weeknights, weighed in grams'},
    'categories': [{'slug': 'dinner', 'name': 'Weeknight dinners'}, {'slug': 'traybakes', 'name': 'Traybakes'}, {'slug': 'soups', 'name': 'Soups'},
                   {'slug': 'sides', 'name': 'Sides and dips'}, {'slug': 'baking', 'name': 'Baking'}],
    'front_page': 'home', 'posts_page': 'recipes',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'recipes', 'title': 'Recipes', 'content': ''},
        {'slug': 'cookbooks', 'title': 'Cookbooks and events', 'pattern': 'pantry/cookbooks-page', 'template': 'page-wide'},
        {'slug': 'conversions', 'title': 'Weights and temperatures', 'pattern': 'pantry/conversions-page', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About Hana', 'pattern': 'pantry/about-page', 'template': 'page-wide'},
    ],
    'posts': R,
    'nav': [{'label': 'Recipes', 'url': '/recipes/'}, {'label': 'Weeknight', 'url': '/category/dinner/'}, {'label': 'Traybakes', 'url': '/category/traybakes/'},
            {'label': 'Baking', 'url': '/category/baking/'}, {'label': 'Cookbooks', 'url': '/cookbooks/'}, {'label': 'Conversions', 'url': '/conversions/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs(os.path.join(ROOT, 'demos', S), exist_ok=True)
with open(os.path.join(ROOT, 'demos', S, 'content.json'), 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
print('pantry: content.json written, %d posts' % len(R))
