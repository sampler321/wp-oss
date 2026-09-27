# Design note (local, idea 053, owner's brief: "make it more scientific looking")
# Direction: a town newspaper set like a journal issue and a lab report. Every story has an abstract, a method note,
#   numbered figures and tables, and a numbered source list. Why: readers trust local news that shows its working.
# Fonts: Newsreader (display, journal-title serif at optical size), Public Sans (body, labels and tables, tabular figures).
# Palette: white paper, near-black ink #111417, vermilion #B8321A for figure marks, chart blue #1D5A85, graph-paper #F2F5F7.
# Layout idea: the front page is an issue contents sheet: lead report with abstract, a "Table 1" meetings rail, a hand-set
#   bar figure on graph paper, and a news log with dated entries. Tables and figures are auto-numbered by CSS counters.
import sys, json, os, datetime
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('local')
S = THEME['slug']
D = THEME['dir']
ROOT = os.path.abspath(os.path.join(D, '..', '..'))

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

# ------------------------------------------------------------------ theme.json
fonts = [f for f in json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies'] if f['slug'] != 'mono']
for f in fonts:
    if f['slug'] == 'display':
        f['fontFamily'] = '"Newsreader", "Iowan Old Style", Georgia, serif'
    if f['slug'] == 'body':
        f['fontFamily'] = '"Public Sans", "Helvetica Neue", Arial, sans-serif'
        f['name'] = 'Public Sans'

PAL = [
    ('base', '#FFFFFF', 'Paper'),
    ('contrast', '#111417', 'Ink'),
    ('accent', '#B8321A', 'Figure red'),
    ('accent-2', '#1D5A85', 'Chart blue'),
    ('surface', '#F2F5F7', 'Graph paper'),
    ('line', '#C9D3DA', 'Grid line'),
    ('muted', '#4F5A63', 'Pencil'),
    ('highlight', '#FFF1A8', 'Marker'),
]

def palette(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.8125rem', 'name': 'Label', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.375rem', 'name': 'Large', 'fluid': {'min': '1.2rem', 'max': '1.375rem'}},
                {'slug': 'x-large', 'size': '2rem', 'name': 'Section', 'fluid': {'min': '1.6rem', 'max': '2rem'}},
                {'slug': 'xx-large', 'size': '3rem', 'name': 'Title', 'fluid': {'min': '2.2rem', 'max': '3rem'}},
                {'slug': 'display', 'size': '5.25rem', 'name': 'Display', 'fluid': {'min': '2.75rem', 'max': '5.25rem'}},
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
                {'slug': '60', 'size': 'clamp(2rem, 4.5vw, 3.25rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(2.75rem, 6vw, 4.5rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(3.5rem, 9vw, 7rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'custom': {'measure': '66ch'},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {
                'color': {'text': 'var:preset|color|accent-2'},
                'typography': {'textDecoration': 'underline'},
                ':hover': {'color': {'text': 'var:preset|color|accent'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent-2', 'offset': '2px', 'style': 'solid', 'width': '2px'}},
            },
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'lineHeight': '1.08', 'letterSpacing': '-0.015em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '500'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '600', 'lineHeight': '1.2'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                'border': {'radius': '2px', 'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '1em', 'right': '1em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|base'}, 'border': {'color': 'var:preset|color|accent-2'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent-2', 'offset': '2px', 'style': 'solid', 'width': '2px'}},
            },
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.5'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|x-large', 'letterSpacing': '-0.02em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent-2'}}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}},
            'core/post-author-name': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.55'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.4'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.25'},
                               'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}},
            'core/categories': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'}},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/list': {'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
        },
        'css': (
            ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none}'
            'table,.wp-block-table td,.wp-block-post-date,.wp-block-categories{font-variant-numeric:tabular-nums lining-nums}'
            '.wp-block-table table{border-collapse:collapse}.wp-block-table thead{border-bottom:1.5px solid var(--wp--preset--color--contrast)}'
            '.wp-block-table th{font-family:var(--wp--preset--font-family--body);font-weight:500;text-align:left;font-size:var(--wp--preset--font-size--x-small)}'
            '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.55em .8em .55em 0;vertical-align:top}'
            '.wp-block-table{border-top:1.5px solid var(--wp--preset--color--contrast)}'
            'main{counter-reset:fig tab}main .wp-block-image figcaption::before,main .wp-block-post-featured-image+.wp-block-post-featured-image figcaption::before{counter-increment:fig;content:"Fig. " counter(fig) "  ";color:var(--wp--preset--color--accent);font-weight:600}'
            'main .wp-block-table figcaption{caption-side:top;text-align:left}main .wp-block-table figcaption::before{counter-increment:tab;content:"Table " counter(tab) ".  ";color:var(--wp--preset--color--accent);font-weight:600}'
            '.single .wp-block-post-content{counter-reset:sec}.single .wp-block-post-content>h2::before{counter-increment:sec;content:counter(sec) ". ";color:var(--wp--preset--color--accent);font-family:var(--wp--preset--font-family--body);font-size:.6em;vertical-align:.35em;margin-right:.4em}'
            ':focus-visible{outline:2px solid var(--wp--preset--color--accent-2);outline-offset:2px}'
            'mark{background:var(--wp--preset--color--highlight);color:inherit;padding:0 .1em}'
            '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:.3em}'
            '.wp-block-navigation__responsive-container.is-menu-open{font-family:var(--wp--preset--font-family--body);background:var(--wp--preset--color--surface)!important}'
            '@media (prefers-reduced-motion:no-preference){a{transition:color .15s}}'
        ),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Masthead'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide (tables and trackers)', 'postTypes': ['page']},
        {'name': 'single-explainer', 'title': 'Explainer (numbered parts)', 'postTypes': ['post']},
    ],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Local
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A news site for one-town newsrooms and reader-owned papers that show their working, with a public meetings tracker, funding and corrections pages.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: local
Tags: news, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column, two-columns
*/''')

# ------------------------------------------------------------------ section styles
def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

GRID_CSS = ('&{background-color:var(--wp--preset--color--surface);background-image:linear-gradient(color-mix(in srgb,var(--wp--preset--color--line) 60%,transparent) 1px,transparent 1px),'
            'linear-gradient(90deg,color-mix(in srgb,var(--wp--preset--color--line) 60%,transparent) 1px,transparent 1px);background-size:20px 20px;background-position:-1px -1px}')
section('graph-paper', 'Graph paper', ['core/group', 'core/columns'], {
    'color': {'text': 'var:preset|color|contrast'},
    'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|line'},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
    'css': GRID_CSS})
section('abstract', 'Abstract box', ['core/group'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'border': {'left': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
    'typography': {'fontSize': 'var:preset|font-size|small'}})
section('rule-top', 'Hairline above', ['core/group', 'core/columns', 'core/post-template'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('rule-thick', 'Section rule (thick)', ['core/group'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '3px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('rule-bottom', 'Hairline below', ['core/group'], {
    'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}})
section('boxed', 'Figure box', ['core/group', 'core/column'], {
    'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('notice', 'Notice bar', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}},
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}})
section('bars', 'Bar figure (table)', ['core/table'], {
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'},
    'css': '& td:nth-child(2){color:var(--wp--preset--color--accent-2);letter-spacing:-0.12em;white-space:nowrap;width:55%}& td:last-child{text-align:right}& td{border-bottom-style:dotted!important}'})
section('log', 'News log', ['core/post-template'], {
    'css': '&>li{border-top:1px solid var(--wp--preset--color--line);padding-top:var(--wp--preset--spacing--30);margin-block-start:var(--wp--preset--spacing--30)!important}'})
section('data-list', 'Data list', ['core/list'], {
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'},
    'css': '&{list-style:none;padding-left:0}&>li{border-bottom:1px dotted var(--wp--preset--color--line);padding:.35em 0}'})
section('refs', 'Numbered sources', ['core/list'], {
    'typography': {'fontSize': 'var:preset|font-size|small'},
    'css': '&{counter-reset:ref;list-style:none;padding-left:0}&>li{counter-increment:ref;padding-left:2.6em;position:relative;margin-bottom:.4em}&>li::before{content:"[" counter(ref) "]";position:absolute;left:0;font-family:var(--wp--preset--font-family--body);color:var(--wp--preset--color--accent)}'})

section('topic-index', 'Topic index', ['core/categories'], {
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'},
    'css': '&{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(12rem,1fr));gap:0 var(--wp--preset--spacing--40)}&>li{border-bottom:1px solid var(--wp--preset--color--line);padding:.5em 0}& a{text-decoration:none;color:var(--wp--preset--color--contrast)}& a:hover{color:var(--wp--preset--color--accent-2)}'})

# ------------------------------------------------------------------ style variations
def variation(fname, title, pal_over, typo=None, extra=None):
    p = dict((s, [c, n]) for s, c, n in PAL)
    for s, c, n in pal_over:
        p[s] = [c, n]
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': v[0], 'name': v[1]} for s, v in p.items()]}}}
    if typo or extra:
        d['styles'] = {}
        if typo:
            d['styles']['elements'] = {'heading': {'typography': typo}}
        if extra:
            d['styles'].update(extra)
    jdump('styles/%s.json' % fname, d)

variation('gazette', 'Gazette', [('accent', '#9E1B1B', 'Rubric red'), ('accent-2', '#111417', 'Black'), ('surface', '#F4F4F2', 'Proof'), ('line', '#BDBDB8', 'Rule')],
          typo={'fontWeight': '700', 'letterSpacing': '-0.02em'})
variation('civic', 'Civic', [('base', '#EEF3EF', 'Pale green'), ('contrast', '#0E1A14', 'Ink'), ('accent', '#00704A', 'Street-sign green'), ('accent-2', '#00563A', 'Deep green'),
          ('surface', '#FFFFFF', 'Card'), ('line', '#B8C9BE', 'Rule'), ('muted', '#3F5249', 'Pencil'), ('highlight', '#DDEFC4', 'Marker')])
variation('weekly', 'Weekly', [('base', '#E9E8E4', 'Newsprint'), ('contrast', '#161514', 'Ink'), ('accent', '#C4221A', 'Section flag'), ('accent-2', '#8A1A14', 'Oxblood'),
          ('surface', '#F6F5F2', 'Page'), ('line', '#B3B0A8', 'Rule'), ('muted', '#4A4843', 'Pencil'), ('highlight', '#FFE08A', 'Marker')],
          typo={'fontWeight': '600'})

# ------------------------------------------------------------------ helpers
def small_note(text, **a):
    return para(text, fontFamily='body', fontSize='x-small', **a)

def label(text, **a):
    return small_note(text, textColor='muted', **a)

def q(inner, per_page=6, offset=0, qid=1, pt_class=None, layout=None, **attrs):
    qq = {'perPage': per_page, 'pages': 0, 'offset': offset, 'postType': 'post', 'order': 'desc', 'orderBy': 'date', 'inherit': False}
    a = {'queryId': qid, 'query': qq, **attrs}
    pta = {}
    if pt_class: pta['className'] = pt_class
    if layout: pta['layout'] = layout
    return ('<!-- wp:query%s -->\n<div class="wp-block-query"><!-- wp:post-template%s -->\n%s\n<!-- /wp:post-template -->\n\n'
            '<!-- wp:query-no-results -->\n%s\n<!-- /wp:query-no-results --></div>\n<!-- /wp:query -->') % (
        (' ' + json.dumps(a, separators=(',', ':'))), (' ' + json.dumps(pta, separators=(',', ':'))) if pta else '', inner, para('No reports filed yet.'))

PAD = lambda t, b: {'spacing': {'padding': {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}}}

# ------------------------------------------------------------------ parts
write('parts/header.html', J(
    template_part('notice'),
    group(J(
        columns(
            ('70%', stack(J(dyn('site-title', level=0, fontSize='xx-large'), dyn('site-tagline')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}})),
            (None, small_note('Vol. 6, no. 214<br>Frome, Somerset, BA11<br>Updated weekdays, 7am', textColor='muted', align='right')),
            align='wide', isStackedOnMobile=False, style={'spacing': {'padding': {'bottom': 'var:preset|spacing|30'}}}),
        group(dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'left', 'flexWrap': 'wrap'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
              align='wide', className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|20'}}})),
        tag='header', align='full', className='is-style-rule-bottom', style=PAD(40, 20))))

write('parts/notice.html', pattern_ref('notice-election'))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0),
                  para('Local news for Frome, with the numbers and where they came from. Owned by its members since 2021. Every figure we publish links to its source or says why it can\'t.', fontSize='small'))),
        (None, J(heading('Newsroom', 6), para('First floor, 14 Catherine Hill<br>Frome BA11 1BY<br><a href="mailto:desk@example.com">desk@example.com</a><br>01373 900 214, weekdays 9am to 5pm', fontSize='small'))),
        (None, J(heading('Accountability', 6), para('<a href="/corrections/">Corrections and complaints</a><br><a href="/funding/">Who funds us</a><br>Regulated by IMPRESS<br>Editor: Ruth Adebayo', fontSize='small'))),
        (None, J(heading('Read it elsewhere', 6), para('<a href="/newsletters/">Newsletters</a><br><a href="/join/">Become a member</a><br>Print edition on the first Friday of the month', fontSize='small'))),
        align='wide'),
    label('Set in Newsreader and Public Sans. Demo photographs are public domain or CC0 images from Wikimedia Commons, used as stand-ins for local photography.', align='wide')),
    tag='footer', align='full', className='is-style-rule-thick', style=PAD(60, 50)))

# ------------------------------------------------------------------ templates
MAIN = lambda inner, t=60, b=70: page_template(inner, style=PAD(t, b))

river_item = J(
    columns(('9rem', J(dyn('post-date', format='j M Y'), dyn('post-terms', term='category', separator=', '))),
            (None, J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=28, moreText=''))),
            ('220px', dyn('post-featured-image', isLink=True, aspectRatio='3/2', sizeSlug='medium')),
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}))

pattern('post-log', 'News log (inherits the page query)', 'posts,query', inherit_query(river_item, template_class='is-style-log', align='wide'), inserter=False)

write('templates/index.html', MAIN(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-log'))))
write('templates/home.html', MAIN(J(
    heading('The news log', 1, align='wide'),
    para('Every report we have published, newest first. Filter by topic below. The number after each topic is how many reports it holds.', align='wide', fontSize='small'),
    dyn('categories', showPostCounts=True, className='is-style-topic-index', align='wide'),
    pattern_ref('post-log'))))
write('templates/archive.html', MAIN(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide'),
    dyn('term-description', align='wide'),
    pattern_ref('post-log'))))
write('templates/search.html', MAIN(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search the archive', showLabel=False, placeholder='A street, a school, a planning number', buttonText='Search', align='wide'),
    pattern_ref('post-log'))))
write('templates/404.html', MAIN(J(
    heading('No page at this address', 1),
    para('The link may be old, or the story may have moved when we changed topics in 2024. Search the archive, or email the desk and we\'ll find it for you.'),
    dyn('search', label='Search', showLabel=False, placeholder='A street, a school, a planning number', buttonText='Search')), 70, 80))
write('templates/page.html', MAIN(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'}))))
write('templates/page-wide.html', MAIN(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'}))))

def single_body(extra_side=''):
    return J(
        group(J(
            dyn('post-terms', term='category', separator=', ', textColor='accent'),
            dyn('post-title', level=1, fontSize='xx-large'),
            dyn('post-excerpt', fontSize='large'),
            dyn('post-date', format='j F Y')), align='wide', layout={'type': 'constrained', 'contentSize': '900px', 'justifyContent': 'left'}),
        dyn('post-featured-image', align='wide', aspectRatio='16/9'),
        columns(
            ('68%', dyn('post-content', layout={'type': 'constrained', 'justifyContent': 'left'})),
            (None, group(J(
                heading('Report details', 6),
                list_meta(),
                extra_side,
                para('Spotted a mistake? Email <a href="mailto:corrections@example.com">corrections@example.com</a> with the headline. We log every correction on the <a href="/corrections/">corrections page</a>.', fontSize='x-small')),
                className='is-style-boxed', style={'position': {'type': 'sticky', 'top': '0px'}})),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
        group(row(J(dyn('post-navigation-link', type='previous', label='Previous report', showTitle=True), dyn('post-navigation-link', label='Next report', showTitle=True)), justify='space-between'),
              align='wide', className='is-style-rule-top', layout={'type': 'default'}))

def list_meta():
    return J(
        group(J(label('Published'), dyn('post-date', format='j F Y, H:i')), layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}}),
        group(J(label('Filed under'), dyn('post-terms', term='category', separator=', ')), layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}}),
        group(J(label('Keywords'), dyn('post-terms', term='post_tag', separator=', ')), layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}}))

write('templates/single.html', MAIN(single_body(), 50, 70))
write('templates/single-explainer.html', MAIN(single_body(J(label('Part of a series'), para('<a href="/category/explainers/">All explainers</a>', fontSize='small'))), 50, 70))

write('templates/front-page.html', page_template(J(
    pattern_ref('lead-with-meetings'),
    pattern_ref('news-log-front'),
    pattern_ref('figure-of-the-week'),
    pattern_ref('topic-index'),
    pattern_ref('newsletter-chooser-short')), style=PAD(50, 70)))

# ------------------------------------------------------------------ patterns
# Signature: public meetings tracker
MEETINGS = [
    ['Mon 28 Sep, 7pm', 'Frome Town Council, planning committee', 'Housing', '● In person, Council Chamber', '<a href="https://example.com/agenda/pc-0928">Agenda (14 pp)</a>', 'Due Thu'],
    ['Tue 29 Sep, 10am', 'Somerset Council, licensing sub-committee', 'Business', '○ Remote, YouTube', '<a href="https://example.com/agenda/lsc-0929">Agenda (6 pp)</a>', 'Due Fri'],
    ['Wed 30 Sep, 6:30pm', 'Frome Town Council, full council', 'Budget', '◐ In person and streamed', '<a href="https://example.com/agenda/fc-0930">Agenda (38 pp)</a>', 'Due Fri'],
    ['Thu 1 Oct, 2pm', 'Somerset Council, executive', 'Schools, budget', '● In person, Taunton', '<a href="https://example.com/agenda/ex-1001">Agenda (112 pp)</a>', 'Due Mon'],
    ['Thu 1 Oct, 7pm', 'Frome Medical Centre, patient group', 'Health', '● In person, Enos Way', 'Not published', 'We are attending'],
]
PAST = [
    ['Wed 23 Sep', 'Frome Town Council, environment committee', 'Environment', '● In person', '<a href="https://example.com/agenda/ec-0923">Agenda</a>', '<a href="https://example.com/notes/ec-0923">Our notes</a>'],
    ['Tue 22 Sep', 'Somerset Council, scrutiny (children)', 'Schools', '○ Remote', '<a href="https://example.com/agenda/sc-0922">Agenda</a>', '<a href="https://example.com/notes/sc-0922">Our notes</a>'],
    ['Mon 14 Sep', 'Frome Town Council, planning committee', 'Housing', '● In person', '<a href="https://example.com/agenda/pc-0914">Agenda</a>', '<a href="https://example.com/notes/pc-0914">Our notes</a>'],
]
HEAD = ['When', 'Body', 'Topic', 'Format', 'Papers', 'Our notes']

pattern('meetings-rail', 'Meetings this week (rail table)', 'meetings,featured', J(
    heading('Public meetings this week', 3),
    table([[m[0], m[1], m[3].split(',')[0]] for m in MEETINGS], head=['When', 'Body', 'Format'], caption='Meetings open to the public, 28 September to 2 October. We attend the ones marked in the tracker.'),
    para('<a href="/meetings/">Full tracker with agendas and notes</a>', fontSize='small')))

pattern('meetings-tracker', 'Public meetings tracker', 'meetings', J(
    table(MEETINGS, head=HEAD, caption='Upcoming meetings, week 40. Format is in person, remote, or both. Notes go up within two working days.'),
    heading('Last three weeks', 3),
    table(PAST, head=HEAD, caption='Recent meetings with our published notes.')),
    description='The signature pattern: every public meeting by date, body, topic and format, with agenda and our notes.')

pattern('meetings-legend', 'How to read the tracker', 'meetings', group(J(
    heading('How to read the tracker', 4),
    lst(['<strong>● In person</strong> means you can walk in. The Council Chamber is at the back of Frome Town Hall, step-free from Christchurch Street West.',
         '<strong>○ Remote</strong> means streamed only. Somerset Council posts the link on its YouTube channel about an hour before.',
         '<strong>◐ Both</strong> means you can attend or watch the stream.', '<strong>Our notes</strong> are written by the reporter or volunteer who attended. They are notes, and a vote count, and they are not a full minute.',
         'Official minutes usually appear four to six weeks later. We link them when they do.'], className='is-style-data-list')),
    className='is-style-abstract'))

pattern('meetings-volunteer', 'Volunteer to take notes', 'meetings,call-to-action', group(J(
    heading('Take notes at a meeting', 3),
    para('We pay £20 a meeting to members who sit in and send us notes. You\'ll get a two-hour training session at the newsroom first, and a template. The planning committee needs the most help. It runs long.'),
    buttons(('Email Tomasz to book training', 'mailto:tomasz@example.com?subject=Meeting%20notes'))),
    className='is-style-boxed'))

pattern('meetings-page', 'Page: public meetings', 'meetings', J(
    para('This is every public meeting in Frome and the parts of Somerset Council that decide things about Frome. We add meetings as soon as the agenda is published, usually five working days before.', fontSize='large'),
    pattern_ref('meetings-tracker'),
    columns((None, pattern_ref('meetings-legend')), (None, pattern_ref('meetings-volunteer')), align='wide')),
    block_types='core/post-content')

# Lead story + rail (front page)
pattern('lead-with-meetings', 'Lead report with meetings rail', 'featured', columns(
    ('66%', q(J(
        dyn('post-featured-image', isLink=True, aspectRatio='3/2'),
        dyn('post-terms', term='category', separator=', ', textColor='accent'),
        dyn('post-title', isLink=True, level=1, fontSize='display'),
        group(J(heading('Abstract', 6), dyn('post-excerpt', excerptLength=60, moreText='Read the full report', fontSize='medium')), className='is-style-abstract'),
        dyn('post-date', format='j F Y')), per_page=1, qid=2)),
    (None, J(pattern_ref('meetings-rail'), pattern_ref('correction-latest'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'bottom': 'var:preset|spacing|60'}}}))

pattern('news-log-front', 'News log (latest, after the lead)', 'posts,query', group(J(
    row(J(heading('News log', 2), para('<a href="/news/">All reports</a>', fontFamily='body', fontSize='x-small')), justify='space-between'),
    q(river_item, per_page=6, offset=1, qid=3, pt_class='is-style-log')),
    align='wide', className='is-style-rule-thick', layout={'type': 'default'}, style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}))

pattern('lead-static', 'Lead story (static, with abstract)', 'featured', columns(
    ('60%', image('river.jpg', 'Brown floodwater running high between trees along a river bank', 'The river at Welshmill, 06:40 on 14 September. Archive photograph used as a stand-in.')),
    (None, J(heading('The Frome rose 2.1 metres in 30 hours. Here is what the gauge recorded', 1, fontSize='xx-large'),
             group(J(heading('Abstract', 6), para('We took the Environment Agency\'s 15-minute readings for the Welshmill gauge and set them against the rain gauge on the allotments at Critchill. The river peaked at 2.46 m at 04:15 on 14 September, 38 cm below the 2012 record.')), className='is-style-abstract'),
             buttons(('Read the full report', '/news/')))), align='wide'))

pattern('figure-of-the-week', 'Figure of the week (bar chart on graph paper)', 'featured,data', group(J(
    columns(
        ('38%', J(heading('Figure of the week', 2),
                  para('Missed bin collections reported to Somerset Council, June to August, for the six Frome streets with the most reports. Most misses on Vallis Road were on the same Thursday round.', fontSize='small'),
                  label('Source: Somerset Council FOI response 2026/1147, received 11 September. n = 212 reports across Frome.'),
                  para('<a href="/news/">Read the report</a>', fontSize='small'))),
        (None, table([
            ['Vallis Road', '████████████████████', '41'],
            ['Nunney Road', '██████████████', '29'],
            ['Butts Hill', '███████████', '23'],
            ['Portway', '█████████', '19'],
            ['Styles Hill', '███████', '14'],
            ['Welshmill Lane', '█████', '11'],
        ], head=['Street', 'Reports', 'n'], caption='Missed collections by street, 1 June to 31 August 2026.', className='is-style-bars')),
        style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    align='wide', className='is-style-graph-paper', layout={'type': 'default'}))

pattern('figure-bars', 'Bar figure (edit the numbers)', 'data', table([
    ['Grants', '█████████████', '£41,300'], ['Members', '███████████████████', '£62,800'], ['Advertising', '████', '£11,200'], ['Events and print sales', '██', '£5,900']],
    head=['Income', 'Share', '£'], caption='Income, April 2025 to March 2026. One block is roughly £3,000.', className='is-style-bars'),
    description='A bar chart made from a table. Each full block stands for a fixed amount; say what it is in the caption.')

pattern('topic-index', 'Topic index with counts', 'posts', group(J(
    columns(
        ('38%', J(heading('Topics', 2), para('Reports by beat. The number is how many reports each one holds.', fontSize='small'))),
        (None, dyn('categories', showPostCounts=True, className='is-style-topic-index'))),
    ), align='wide', className='is-style-rule-thick', layout={'type': 'default'}, style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}, 'margin': {'top': 'var:preset|spacing|60'}}}))

# Story furniture
pattern('abstract-box', 'Abstract (top of a report)', 'text,data', group(J(
    heading('Abstract', 6),
    para('Three sentences. What we measured, what we found, and the one number that matters. Keep it under 80 words so it fits on the front page.')),
    className='is-style-abstract'))

pattern('key-findings', 'Key findings (numbered)', 'text,data', J(
    heading('What we found', 2),
    lst(['The river peaked at 2.46 m at 04:15 on 14 September, 38 cm below the 2012 record of 2.84 m.',
         'It rose 2.1 m in 30 hours. In 2012 the same rise took 41 hours.',
         '58 mm of rain fell at Critchill in the 24 hours to 09:00 on 13 September.',
         'Four homes on Willow Vale reported water in cellars. None reported water above floor level.'], ordered=True)))

pattern('method-note', 'How we reported this', 'text,data', group(J(
    heading('How we reported this', 4),
    para('Readings come from the Environment Agency\'s open flood-monitoring data, station 52119. We checked two of them against the staff gauge by the bridge at 07:00 on 14 September. The rain figure is from a volunteer gauge; it is not a Met Office station. We did not model flood risk, and we don\'t say what caused the rise.', fontSize='small')),
    className='is-style-boxed'))

pattern('limits-note', 'What we could not check', 'text,data', J(
    heading('What we could not check', 4),
    para('Somerset Council would not say how many drains on Willow Vale were cleared this year. We have asked under the Freedom of Information Act (reference 2026/1203). The answer is due by 12 October and we will add it here.', fontSize='small')))

pattern('data-sources', 'Sources (numbered)', 'text,data', J(
    heading('Sources', 4),
    lst(['Environment Agency, flood-monitoring API, station 52119 (Frome at Welshmill), 15-minute readings, 10 to 16 September 2026.',
         'Critchill allotments rain gauge, daily readings kept by Gwen Harcourt since 2009. Spreadsheet on request.',
         'Somerset Council, Section 19 flood investigation report, Frome, July 2012.',
         'Interviews with four residents of Willow Vale, 14 and 15 September.'], className='is-style-refs')))

pattern('data-download', 'Download the data', 'data', group(row(J(
    para('The spreadsheet behind this report is free to reuse under CC BY 4.0. Please link back.', fontSize='small'),
    buttons(('Download the data (CSV, 18 KB)', 'https://example.com/data/frome-gauge-2026.csv')))), className='is-style-rule-top'))

pattern('pull-figure', 'Pull figure (one number)', 'data', group(J(
    para('2.46 m', fontFamily='display', fontSize='display', textColor='accent'),
    small_note('Peak level at the Welshmill gauge, 04:15 on 14 September. The 2012 record is 2.84 m.')), style={'spacing': {'blockGap': 'var:preset|spacing|10'}}))

pattern('correction-latest', 'Latest correction (rail)', 'accountability', group(J(
    heading('Latest correction', 4),
    small_note('Filed 24 September'),
    para('Our report on the Saxonvale scheme said 150 homes. The approved number is 125. We corrected it at 11:20 the same day.', fontSize='small'),
    para('<a href="/corrections/">All corrections</a>', fontSize='small')), className='is-style-boxed', style={'spacing': {'blockGap': 'var:preset|spacing|20'}}))

# Explainer series
pattern('explainer-series', 'Explainer series (numbered parts)', 'posts,data', J(
    heading('Somerset Council\'s budget, explained in five parts', 2),
    table([['1', '<a href="/category/explainers/">Why the council said it could go bust</a>', '6 min'],
           ['2', '<a href="/category/explainers/">What a section 114 notice does and doesn\'t do</a>', '4 min'],
           ['3', '<a href="/category/explainers/">Where the money goes, by service</a>', '7 min'],
           ['4', '<a href="/category/explainers/">What has been cut in Frome so far</a>', '5 min'],
           ['5', '<a href="/category/explainers/">The town council\'s reserves and what they\'re for</a>', '6 min']],
          head=['Part', 'Title', 'Reading time'], caption='The series so far. Part 6, on council tax, is due in November.')))

# Newsletters
NEWSL = [['The 7am', 'Weekdays, 7am', 'Five links and the meetings on today. About 400 words.'],
         ['The Weekly Measure', 'Fridays, 5pm', 'One chart, the week\'s reports, and what\'s coming. About 900 words.'],
         ['Planning Watch', 'When applications are lodged', 'Every planning application in the BA11 postcode, with a map link. Can be busy.'],
         ['Schools', 'Twice a term', 'Admissions dates, governors\' meetings, and our schools reporting.']]
pattern('newsletter-chooser', 'Newsletter chooser', 'call-to-action', J(
    table(NEWSL, head=['List', 'Sent', 'What\'s in it'], caption='Our email lists. All free, all written by the newsroom, never sold on.'),
    para('To sign up, email <a href="mailto:lists@example.com?subject=Sign%20me%20up">lists@example.com</a> with the names of the lists you want. We add you by hand within a working day, and every email has a one-click unsubscribe.'),
    buttons(('Email us to sign up', 'mailto:lists@example.com?subject=Sign%20me%20up'))))

pattern('newsletter-chooser-short', 'Newsletter sign-up (short)', 'call-to-action', group(columns(
    ('38%', J(heading('Get it by email', 2), para('Four lists. Pick one or all of them.', fontSize='small'))),
    (None, J(table([n[:2] for n in NEWSL], head=['List', 'Sent']), buttons(('Choose your newsletters', '/newsletters/'))))),
    align='wide', className='is-style-rule-thick', layout={'type': 'default'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))

pattern('newsletters-page', 'Page: newsletters', 'call-to-action', J(
    para('We send four newsletters. The 7am is the one most people read; Planning Watch is the one councillors read.', fontSize='large'),
    pattern_ref('newsletter-chooser')), block_types='core/post-content')

# Membership
pattern('membership-join', 'Membership: monthly amounts', 'call-to-action,accountability', J(
    table([['£3 a month', 'Pays for about one hour of meeting reporting'], ['£5 a month', 'Our suggested amount. Most members pay this.'],
           ['£10 a month', 'Covers a reader who can\'t pay'], ['Any amount', 'Set your own, from £1']], head=['Amount', 'What it does'], caption='Membership amounts. You can change or cancel any time by email.'),
    para('Members own the paper. Each member gets one vote at the annual general meeting, whatever they pay, and can stand for the board. The website stays free to read: membership pays for it to exist.'),
    buttons(('Join with a monthly payment', 'https://example.com/join'), ('Ask about paying by standing order', 'mailto:members@example.com', {'className': 'is-style-outline'}))))

pattern('membership-goal', 'Membership goal (one sentence)', 'call-to-action', group(J(
    para('We need 400 more members paying £5 a month to hire a second full-time reporter for Somerset Council meetings.', fontFamily='display', fontSize='x-large'),
    buttons(('Become a member', '/join/')))), description='One plain sentence about what the next members pay for.')

pattern('join-page', 'Page: join', 'call-to-action', J(
    pattern_ref('membership-goal'), pattern_ref('membership-join'),
    details('Is this a donation or a share?', para('A membership of a community benefit society. It isn\'t a donation and it isn\'t tax-deductible. You get one vote at the AGM.')),
    details('Can I pay yearly?', para('Yes. Email us and we\'ll send a yearly payment link at twelve times the monthly amount.')),
    details('Do members get a say in what you cover?', para('Members vote on the board and on one reporting priority each year. They don\'t see stories before they are published.'))),
    block_types='core/post-content')

# Transparency
pattern('funders-table', 'Who funds us (table)', 'accountability', table([
    ['Member payments', '812 members', '£62,800', '52%'],
    ['Somerset Community Foundation', 'Grant, 2025 to 2027', '£24,000', '20%'],
    ['Local News Fund (national)', 'Grant, one year', '£17,300', '14%'],
    ['Advertising', '23 local businesses', '£11,200', '9%'],
    ['Print sales and events', '', '£5,900', '5%']],
    head=['Source', 'Detail', 'Amount', 'Share'], caption='Income for April 2025 to March 2026, from our filed accounts. Anyone giving over £1,000 is named.'))

pattern('spending-table', 'Where the money goes', 'accountability', table([
    ['Salaries (2.6 full-time staff)', '£84,200'], ['Freelance and meeting notes', '£14,100'], ['Printing (monthly edition)', '£9,800'], ['Rent and office', '£6,300'], ['Software, insurance, IMPRESS', '£4,400']],
    head=['Cost', 'Amount'], caption='Spending for the same year. We ended the year £2,400 over budget, paid from reserves.'))

pattern('transparency-page', 'Page: who funds us', 'accountability', J(
    para('Frome Survey is a community benefit society (FCA number 8814) owned by its members. We publish every source of income over £1,000 and what we spend it on. No funder sees a story before publication.', fontSize='large'),
    pattern_ref('funders-table'), pattern_ref('figure-bars'), pattern_ref('spending-table'),
    para('Full accounts: <a href="https://example.com/accounts-2026.pdf">2025 to 2026 (PDF, 22 pages)</a>. Board minutes are on request.', fontSize='small')),
    block_types='core/post-content')

# Complaints and corrections
pattern('complaints-procedure', 'Complaints procedure (with regulator)', 'accountability', J(
    heading('How to complain', 2),
    lst(['Email <a href="mailto:corrections@example.com">corrections@example.com</a> or write to the newsroom. Say which report, and what you think is wrong.',
         'The editor, Ruth Adebayo, replies within seven days. Factual errors are fixed the same day, with a note at the foot of the report.',
         'If you\'re not happy with our answer after 28 days, you can take it to our regulator, IMPRESS, at impressorg.com or 020 3325 4288.'], ordered=True),
    para('We follow the IMPRESS Standards Code. We don\'t remove reports because someone asks us to, but we do update them when the facts change.', fontSize='small')))

pattern('corrections-log', 'Corrections log', 'accountability', table([
    ['24 Sep 2026', 'Saxonvale scheme gets approval', 'Said 150 homes. The approved number is 125.', 'Same day'],
    ['9 Sep 2026', 'The 51 bus, timed for a week', 'Chart labelled Tuesday as Wednesday.', 'Next day'],
    ['28 Aug 2026', 'School places by year group', 'Oakfield Academy\'s reception number was 60, not 90.', 'Same day'],
    ['2 Aug 2026', 'Town council reserves', 'Wrong councillor named as proposer. It was Cllr Okafor.', '3 days']],
    head=['Filed', 'Report', 'What was wrong', 'Fixed'], caption='Every correction since January. Spelling and typing errors are fixed without a note.'))

pattern('corrections-page', 'Page: corrections and complaints', 'accountability', J(
    para('We get things wrong about once a month. This page lists every time.', fontSize='large'),
    pattern_ref('corrections-log'), pattern_ref('complaints-procedure')), block_types='core/post-content')

# Tips
pattern('tip-options', 'Send us a tip', 'contact', J(
    table([['Email', '<a href="mailto:tips@example.com">tips@example.com</a>', 'Read by the editor and the data reporter'],
           ['Signal', '07700 900 214', 'Messages set to disappear after a week'],
           ['Post', '14 Catherine Hill, Frome BA11 1BY', 'No return address needed'],
           ['In person', 'Thursday drop-in, 10am to noon', 'At the newsroom, first floor, no lift']],
          head=['How', 'Where', 'Notes'], caption='Ways to reach the newsroom. Signal is the most private.'),
    para('Tell us what you know, how you know it, and whether we can quote you. We check everything before we publish and we never name a source who asked us not to.')))

pattern('tips-page', 'Page: tips', 'contact', J(
    para('Most of our best stories started with a reader noticing something odd. A planning notice on a lamp post, a school letter, a bus that stopped coming.', fontSize='large'),
    pattern_ref('tip-options')), block_types='core/post-content')

# People
def reporter(name, role, beat, email, img, alt):
    return columns(('30%', image(img, alt)), (None, J(heading(name, 3), small_note(role), para(beat), para('<a href="mailto:%s">%s</a>' % (email, email), fontSize='small'))))

pattern('reporter-profile', 'Reporter profile', 'about', reporter('Tomasz Wiśniewski', 'Data reporter, since 2022', 'Tomasz covers planning, transport and anything that comes with a spreadsheet. He built the meetings tracker and keeps the rain gauge readings. Before this he was a surveyor for Wessex Water for eleven years.', 'tomasz@example.com', 'rain.jpg', 'A yellow rain gauge funnel strapped to a railing above grass'))

pattern('newsroom-list', 'Newsroom (people and beats)', 'about', table([
    ['Ruth Adebayo', 'Editor', 'Council, courts, complaints', '<a href="mailto:ruth@example.com">ruth@example.com</a>'],
    ['Tomasz Wiśniewski', 'Data reporter', 'Planning, transport, data', '<a href="mailto:tomasz@example.com">tomasz@example.com</a>'],
    ['Gwen Harcourt', 'Reporter (3 days)', 'Schools, health, environment', '<a href="mailto:gwen@example.com">gwen@example.com</a>'],
    ['Imran Siddiqui', 'Membership and print', 'Stockists, AGM, events', '<a href="mailto:members@example.com">members@example.com</a>']],
    head=['Name', 'Role', 'Beat', 'Email'], caption='Who works here. Volunteers who take meeting notes are credited on each set of notes.'))

pattern('about-page', 'Page: about', 'about', J(
    para('Frome Survey started in 2021 after the town\'s weekly paper stopped covering council meetings. Three of us began by sitting in on the planning committee and posting what was decided. There are now four staff and about 30 volunteers who take notes.', fontSize='large'),
    para('We report on Frome and the parts of Somerset Council that affect it. We don\'t cover national news, and we don\'t run press releases unchecked. Our house rule is that every number links to where it came from, and if we can\'t show the source, we say why.'),
    para('We think the planning committee is the most important meeting in town and the least attended. If you only read one thing we publish, make it the planning notes.'),
    pattern_ref('newsroom-list'), pattern_ref('reporter-profile'), pattern_ref('print-stockists')), block_types='core/post-content')

# Print and events
pattern('print-stockists', 'Print edition stockists', 'about', J(
    heading('Where to pick up the print edition', 3),
    para('Sixteen pages, free, on the first Friday of the month. 3,000 copies.', fontSize='small'),
    table([['Frome Library', 'Justice Lane', 'Tue to Sat'], ['Hunting Raven Books', 'Cheap Street', 'Mon to Sat'], ['The Grain café', 'Market Yard', 'Every day'],
           ['Selwood Medical Centre', 'Berkley Road', 'Weekdays'], ['Fromefield Co-op', 'Fromefield', 'Every day']], head=['Stockist', 'Where', 'Open'])))

pattern('events-listing', 'Events listing', 'events', table([
    ['Thu 8 Oct, 7pm', 'Reading a planning application, a workshop', 'Newsroom, 14 Catherine Hill', 'Free, 12 places'],
    ['Sat 17 Oct, 10am', 'Members\' AGM', 'Wesley Methodist Church hall', 'Members only'],
    ['Wed 4 Nov, 6:30pm', 'Ask the editor', 'Frome Library', 'Free, drop in']],
    head=['When', 'What', 'Where', 'Cost'], caption='Our events this autumn. Email events@example.com to book a place.'))

pattern('notice-election', 'Notice: election night', 'banner', group(
    para('By-election, Frome North, Thursday 15 October. Our results table goes live at 10pm, updated as each box is counted. <a href="/meetings/">Hustings dates</a>', align='center'),
    align='full', className='is-style-notice', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
    description='A notice bar for polling day or a road closure. Edit the text, and take it out when the date passes.')

pattern('results-table', 'Election results table', 'data', table([
    ['Hannah Pryce', 'Liberal Democrats', '1,204', '41.8%'], ['Dev Mistry', 'Independents for Frome', '1,031', '35.8%'], ['Colin Rees', 'Conservative', '402', '14.0%'], ['Aisling Byrne', 'Green', '243', '8.4%']],
    head=['Candidate', 'Party', 'Votes', 'Share'], caption='Frome North by-election. Turnout 31.2%. Update this table as boxes are counted.'))

pattern('page-landing', 'Page: news landing (log with topics)', 'posts', J(
    pattern_ref('topic-index'), pattern_ref('news-log-front')), block_types='core/post-content')

print('local: patterns written')

# ------------------------------------------------------------------ demo content
def story(abstract, found, method, tbl=None, sources=None, bars=None, quote_=None):
    parts = [group(J(heading('Abstract', 6), para(abstract)), className='is-style-abstract'),
             heading('What we found', 2), lst(found, ordered=True)]
    if bars:
        parts.append(table(bars[0], head=bars[1], caption=bars[2], className='is-style-bars'))
    if tbl:
        parts.append(table(tbl[0], head=tbl[1], caption=tbl[2]))
    if quote_:
        parts.append(quote(quote_[0], quote_[1]))
    parts += [heading('How we reported this', 2), para(method)]
    if sources:
        parts += [heading('Sources', 2), lst(sources, className='is-style-refs')]
    return J(*parts)

posts = [
    dict(title='The Frome rose 2.1 metres in 30 hours. Here is what the gauge recorded', slug='river-gauge-september', category='environment', tags=['Flooding', 'Data'], image='river.jpg',
         excerpt='We set the Environment Agency\'s 15-minute readings at Welshmill against a volunteer rain gauge. The river peaked at 2.46 m at 04:15 on 14 September, 38 cm below the 2012 record.',
         content=story('We set the Environment Agency\'s 15-minute readings at Welshmill against a volunteer rain gauge on the Critchill allotments. The river peaked at 2.46 m at 04:15 on 14 September, 38 cm below the 2012 record, and rose faster than it did then.',
                       ['The river peaked at 2.46 m at 04:15 on 14 September.', 'It rose 2.1 m in 30 hours. In 2012 the same rise took 41 hours.', '58 mm of rain fell at Critchill in the 24 hours to 09:00 on 13 September.', 'Four homes on Willow Vale reported water in cellars. None reported water above floor level.'],
                       'We downloaded readings for station 52119 from the Environment Agency\'s open flood-monitoring service and checked two against the staff gauge by the bridge. The rain figures come from Gwen Harcourt\'s gauge, which she has read every morning since 2009. It is not a Met Office station and we say so.',
                       tbl=([['12 Sep, 22:00', '0.36 m', '4 mm'], ['13 Sep, 09:00', '0.92 m', '58 mm'], ['13 Sep, 18:00', '1.71 m', '11 mm'], ['14 Sep, 04:15', '2.46 m', '2 mm'], ['15 Sep, 09:00', '1.08 m', '0 mm']], ['Time', 'River level', 'Rain since last reading'], 'Selected readings, Welshmill gauge and Critchill rain gauge.'),
                       sources=['Environment Agency flood-monitoring API, station 52119, 10 to 16 September 2026.', 'Critchill allotments rain gauge, daily readings, G. Harcourt.', 'Somerset Council, Section 19 flood investigation, Frome, July 2012.'])),
    dict(title='Half the homes approved in Frome since 2021 have not been started', slug='homes-approved-not-built', category='housing', tags=['Planning', 'Data'], image='housing.jpg',
         excerpt='Of 1,012 homes given planning permission in Frome between 2021 and 2025, 497 had not been started by August. We checked every application by hand.',
         content=story('Of 1,012 homes given planning permission in Frome between January 2021 and December 2025, 497 had not been started by the end of August 2026. Most of them are on three large sites.',
                       ['497 of 1,012 approved homes (49%) had no building control notice by 31 August.', 'Three sites account for 402 of the unstarted homes.', 'Permission lapses after three years if work hasn\'t started. 88 homes are due to lapse before March.'],
                       'Tomasz read every decision notice for BA11 on the Somerset Council planning portal from 2021 to 2025, then matched each site against building control notices and council tax records. Two developers confirmed their start dates by email. One did not reply.',
                       bars=([['Saxonvale', '███████████████', '125'], ['Selwood Garden Community', '█████████████████████', '171'], ['Land off Rodden Road', '█████████████', '106'], ['Smaller sites (41)', '████████████', '95']], ['Site', 'Unstarted homes', 'n'], 'Unstarted homes by site, 31 August 2026. One block is about eight homes.'),
                       sources=['Somerset Council planning portal, decision notices, 2021 to 2025.', 'Somerset Council building control register, extract of 31 August 2026.'])),
    dict(title='The 51 bus is timetabled every 40 minutes. We rode it for a week', slug='the-51-bus-timed', category='transport', tags=['Buses', 'Data'], image='bus.jpg',
         excerpt='Three volunteers logged 64 departures from the Market Place stop. 41 left within five minutes of the timetable; 9 did not come at all.',
         content=story('Three volunteers logged 64 scheduled departures of the 51 from the Market Place stop between 7 and 13 September. 41 left within five minutes of the timetable. Nine did not arrive.',
                       ['41 of 64 departures (64%) were within five minutes of the timetable.', '14 were between six and 25 minutes late.', '9 did not arrive. Seven of those were after 6pm.'],
                       'Volunteers stood at the stop and wrote down the time each bus pulled away, using a phone clock set to network time. We sent the log to the operator, which said two of the missed runs were driver sickness and did not comment on the rest.',
                       tbl=([['On time (0 to 5 min)', '41', '64%'], ['Late (6 to 25 min)', '14', '22%'], ['Did not arrive', '9', '14%']], ['Outcome', 'Departures', 'Share'], 'Departures of the 51 from Market Place, 7 to 13 September, n = 64.'),
                       quote_=('I stopped taking it after six in the evening. You just don\'t know if it\'s coming.', 'Maureen Tilley, who takes the 51 to work at the Fromefield Co-op'))),
    dict(title='Which Frome primary schools are full, by year group', slug='primary-school-places', category='schools', tags=['Schools', 'Data'], image='school.jpg',
         excerpt='Five of Frome\'s nine primary schools are at or over capacity in reception. We asked each school for its numbers and four answered.',
         content=story('Five of Frome\'s nine primary schools are at or over their published admission number in reception this September. Year 3 has the most spare places.',
                       ['Five of nine schools are full in reception.', 'Across the town there are 31 spare reception places, mostly at two schools.', 'Year 3 has 58 spare places.'],
                       'Admission numbers come from Somerset Council\'s 2026 admissions booklet. Pupil numbers come from the January census, published in June. Four schools also sent us their September figures, which we used where we had them.',
                       tbl=([['Oakfield Academy', '60', '60', 'Full'], ['St John\'s CE', '30', '31', 'Over by 1'], ['Hayesdown First', '45', '38', '7 spare'], ['Trinity CE', '30', '30', 'Full'], ['Christchurch CE', '30', '22', '8 spare']], ['School', 'Admission number', 'On roll', 'Status'], 'Reception places, September 2026.'))),
    dict(title='What the town council keeps £1.2 million in reserve for', slug='town-council-reserves', category='explainers', tags=['Council', 'Budget', 'Explainer'], image='townhall.jpg', template='single-explainer',
         excerpt='Part 5 of our budget explainer. Frome Town Council holds £1.23m in reserves. About £880,000 is set aside for named projects.',
         content=story('Frome Town Council holds £1.23m in reserves, according to its audited accounts for 2025 to 2026. About £880,000 is earmarked for named projects; the rest is a general reserve.',
                       ['£880,000 is earmarked, the largest part (£310,000) for the Cattle Market car park resurfacing.', '£350,000 is general reserve, about five months of running costs.', 'Guidance for councils of this size suggests three to twelve months.'],
                       'We read the annual governance and accountability return and the reserves policy, and asked the town clerk two questions by email. Both were answered within a day.',
                       bars=([['Car park resurfacing', '████████████████', '£310k'], ['Play areas', '███████████', '£205k'], ['Building repairs', '█████████', '£170k'], ['Other named projects', '██████████', '£195k'], ['General reserve', '██████████████████', '£350k']], ['Reserve', 'Amount', '£'], 'Reserves at 31 March 2026. One block is about £20,000.'))),
    dict(title='Missed bin collections, street by street, June to August', slug='missed-bins-by-street', category='council', tags=['Waste', 'FOI', 'Data'], image='bins.jpg',
         excerpt='Somerset Council logged 212 missed collections in Frome over the summer. A fifth were on Vallis Road, and most of those on one Thursday round.',
         content=story('Somerset Council logged 212 missed collections in Frome from 1 June to 31 August, according to figures released to us under the Freedom of Information Act. 41 were on Vallis Road.',
                       ['212 missed collections were logged across Frome.', '41 were on Vallis Road, 33 of them on Thursdays.', 'The council says a replacement lorry was used on that round for six weeks.'],
                       'We asked for every missed-collection report with a BA11 postcode. The council sent a spreadsheet, which we cleaned by merging duplicate street names. Our cleaned file is on the data page.',
                       sources=['Somerset Council, FOI response 2026/1147, 11 September 2026.'])),
    dict(title='A361 resurfacing, the dates, the diversion and who pays', slug='a361-resurfacing', category='transport', tags=['Roads'], image='roadworks.jpg',
         excerpt='The A361 between the Garston roundabout and Beckington closes overnight for nine nights from 12 October. The diversion adds about 6 miles.',
         content=story('The A361 between the Garston roundabout and Beckington will close from 8pm to 6am for nine nights from Monday 12 October. The work is paid for from the national pothole fund.',
                       ['Closed 8pm to 6am, 12 to 22 October, not on the weekend.', 'The signed diversion runs via Rudge and adds about 6 miles.', 'Cost £640,000, from the Department for Transport\'s allocation to Somerset.'],
                       'Dates are from the traffic regulation order published on 21 September. The cost is from Somerset Council\'s highways programme for 2026 to 2027.')),
    dict(title='Saturday market footfall, counted by hand for a month', slug='market-footfall', category='business', tags=['Market', 'Data'], image='market.jpg',
         excerpt='Volunteers with clickers counted people entering the Market Place on four Saturdays. The busiest hour was 11am to noon every time.',
         content=story('Volunteers counted people entering the Market Place between 9am and 3pm on four Saturdays in August. The average was 3,140 a day, and the busiest hour was 11am to noon every time.',
                       ['Average 3,140 people a day, from 2,610 (rain) to 3,720.', '11am to noon was the busiest hour on all four days.', 'Traders say they sell most between 10am and 1pm, which fits.'],
                       'Two volunteers stood at the Cork Street and Bath Street entrances with clickers. People who left and came back were counted twice, so these are entries, not people.')),
]

content = {
    'site': {'title': 'Frome Survey', 'tagline': 'Local news for Frome, with the numbers and the sources'},
    'categories': [{'slug': 'council', 'name': 'Council'}, {'slug': 'housing', 'name': 'Housing'}, {'slug': 'transport', 'name': 'Transport'},
                   {'slug': 'schools', 'name': 'Schools'}, {'slug': 'environment', 'name': 'Environment'}, {'slug': 'business', 'name': 'Business'},
                   {'slug': 'explainers', 'name': 'Explainers'}],
    'front_page': 'home', 'posts_page': 'news',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'news', 'title': 'News', 'content': ''},
        {'slug': 'meetings', 'title': 'Public meetings', 'pattern': 'local/meetings-page', 'template': 'page-wide'},
        {'slug': 'newsletters', 'title': 'Newsletters', 'pattern': 'local/newsletters-page'},
        {'slug': 'join', 'title': 'Become a member', 'pattern': 'local/join-page'},
        {'slug': 'funding', 'title': 'Who funds us', 'pattern': 'local/transparency-page'},
        {'slug': 'corrections', 'title': 'Corrections and complaints', 'pattern': 'local/corrections-page'},
        {'slug': 'tips', 'title': 'Send us a tip', 'pattern': 'local/tips-page'},
        {'slug': 'about', 'title': 'About the newsroom', 'pattern': 'local/about-page', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'News', 'url': '/news/'}, {'label': 'Meetings', 'url': '/meetings/'}, {'label': 'Newsletters', 'url': '/newsletters/'},
            {'label': 'Join', 'url': '/join/'}, {'label': 'Funding', 'url': '/funding/'}, {'label': 'Corrections', 'url': '/corrections/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs(os.path.join(ROOT, 'demos', S), exist_ok=True)
with open(os.path.join(ROOT, 'demos', S, 'content.json'), 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
print('local: content.json written')
