# case: UX / product designer case studies (idea 022)
# Direction: the owner asked for kapicadesign.com "but a bit more edgy". Kept from Kapica: the ruled header, a big
#   two-column hero, case studies as wide image-left / text-right cards on a grey page, and a case page that opens with
#   a facts row under a rule and then runs in stages. Made edgier: square corners, 2px black frames, condensed heavy
#   headings, full-bleed black stage bands, and a lime marker colour for the one thing on each screen that matters.
# Fonts: Hubot Sans (registry face, condensed with font-stretch) and Atkinson Hyperlegible Next for text.
# Palette: fog #F1F1EE, ink #0E0E0E, signal blue #1F3BFF for links and buttons, lime #D7FF3A as a marker only, white cards.
# Layout idea: every case study is a black-framed card that splits 7/5 (screens left, role, timeline and outcome right),
#   and the case page is cut into stages by black bands with the stage name in lime.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
from blocks import _a
import blocks as _b
set_theme('case')
S = THEME['slug']
D = THEME['dir']
import shutil
for _d in ('patterns', 'templates', 'parts', 'styles'):
    shutil.rmtree(os.path.join(D, _d), ignore_errors=True)  # rebuilt below; drops stale files


group = _b.group


def columns(*cols, **attrs):
    """core/columns with the classes WordPress saves for verticalAlignment and isStackedOnMobile."""
    extra = []
    if attrs.get('verticalAlignment'):
        extra.append('are-vertically-aligned-' + attrs['verticalAlignment'])
    if attrs.get('isStackedOnMobile') is False:
        extra.append('is-not-stacked-on-mobile')
    out = _b.columns(*cols, **attrs)
    return out.replace('class="wp-block-columns', 'class="wp-block-columns ' + ' '.join(extra), 1) if extra else out


PAL = [
    ('base', '#F1F1EE', 'Fog'),
    ('contrast', '#0E0E0E', 'Ink'),
    ('accent', '#1F3BFF', 'Signal blue'),
    ('accent-2', '#D7FF3A', 'Lime marker'),
    ('surface', '#FFFFFF', 'Card white'),
    ('line', '#C8C8C2', 'Rule'),
    ('muted', '#50504B', 'Graphite'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))
fam = {f['slug']: f for f in fonts['fontFamilies']}


def pal(rows):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]


def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d


CSS = (':where(h1,h2,h3,h4){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none}'
       ':where(h1,h2,h3,h4,.wp-block-site-title,.wp-block-post-title){font-stretch:80%}'
       '.wp-block-table{font-variant-numeric:tabular-nums lining-nums}'
       '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.6em .8em .6em 0;text-align:left;vertical-align:top}'
       '.wp-block-table thead{border:0;border-bottom:2px solid var(--wp--preset--color--contrast)}.wp-block-table th{font-weight:700;font-size:var(--wp--preset--font-size--x-small)}'
       'mark,.has-accent-2-background-color{color:var(--wp--preset--color--contrast)}'
       'mark{background:var(--wp--preset--color--accent-2);padding:0 .15em}'
       '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'
       '.wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-family:var(--wp--preset--font-family--display);font-stretch:80%;font-weight:800;font-size:var(--wp--preset--font-size--xx-large)}'
       '.wp-block-navigation .current-menu-item>a{background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--contrast)}'
       ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'
       '.wp-block-search__input{border:2px solid var(--wp--preset--color--contrast);border-radius:0}'
       '.wp-block-image img[style*=aspect-ratio]{width:100%}'
       '.wp-block-quote cite{display:block;margin-top:.8em;font-family:var(--wp--preset--font-family--body);font-stretch:100%;font-weight:400;font-size:var(--wp--preset--font-size--small);font-style:normal}')

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1240px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'writingMode': False,
            'fontFamilies': [fam['display'], fam['body']],
            'fontSizes': [
                fs('x-small', '0.875rem', 'Label'),
                fs('small', '1rem', 'Small'),
                fs('medium', '1.1875rem', 'Body'),
                fs('large', '1.5rem', 'Large', '1.25rem'),
                fs('x-large', '2.5rem', 'Section', '1.9rem'),
                fs('xx-large', '4rem', 'Title', '2.6rem'),
                fs('display', '6.5rem', 'Display', '2.6rem'),
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False,
            'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'},
                {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'},
                {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.5rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2.5rem, 5.5vw, 4rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3.5rem, 8vw, 6rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4.5rem, 11vw, 9rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '0.98', 'letterSpacing': '-0.015em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'fontWeight': '900'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.1', 'fontWeight': '700'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.25', 'fontWeight': '700', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|surface'},
                'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|accent'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.85em', 'bottom': '0.85em', 'left': '1.4em', 'right': '1.4em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|accent-2'}, 'border': {'color': 'var:preset|color|contrast'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}},
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.01em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|medium'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.2'},
                           'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '8px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '800', 'lineHeight': '1.05'},
                               'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/search': {'border': {'radius': '0'}},
            'core/query-pagination': {'typography': {'fontWeight': '700'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    ],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Case
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A portfolio for independent UX and product designers who write long case studies with research, before and after screens, and results.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: case
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column
*/''')


def variation(fname, title, rows):
    write('styles/%s.json' % fname, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                                'settings': {'color': {'palette': pal(rows)}}}, indent='\t', ensure_ascii=False))


variation('memo', 'Memo', [('base', '#FFFFFF', 'Fog'), ('contrast', '#16181A', 'Ink'), ('accent', '#0A6E5C', 'Signal blue'), ('accent-2', '#D7FF3A', 'Lime marker'),
                           ('surface', '#F3F4F1', 'Card white'), ('line', '#C9CEC6', 'Rule'), ('muted', '#50544F', 'Graphite')])
variation('blueprint', 'Blueprint', [('base', '#EAF1F7', 'Fog'), ('contrast', '#0B1E2E', 'Ink'), ('accent', '#0B4A7A', 'Signal blue'), ('accent-2', '#FFD23F', 'Lime marker'),
                                     ('surface', '#FFFFFF', 'Card white'), ('line', '#B7C8D6', 'Rule'), ('muted', '#3E5566', 'Graphite')])
variation('dim', 'Dim', [('base', '#1B1D1E', 'Fog'), ('contrast', '#E7E9E4', 'Ink'), ('accent', '#8FA2FF', 'Signal blue'), ('accent-2', '#D7FF3A', 'Lime marker'),
                         ('surface', '#232628', 'Card white'), ('line', '#3A3E40', 'Rule'), ('muted', '#B0B4AE', 'Graphite')])


def section(slug, title, block_types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug,
                                                        'blockTypes': block_types, 'styles': styles}, indent='\t', ensure_ascii=False))


section('case-card', 'Case card (black frame)', ['core/group', 'core/columns', 'core/post-template'], {
    'color': {'background': 'var:preset|color|surface'},
    'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('stage', 'Stage band', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'heading': {'color': {'text': 'var:preset|color|accent-2'}}, 'link': {'color': {'text': 'var:preset|color|accent-2'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50'}}})
section('ink', 'Ink panel', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'heading': {'color': {'text': 'var:preset|color|base'}}, 'link': {'color': {'text': 'var:preset|color|accent-2'}},
                 'button': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'}, 'border': {'color': 'var:preset|color|accent-2'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('lime', 'Lime marker panel', ['core/group', 'core/paragraph'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('rule-top', 'Thick rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('rule-bottom', 'Thick rule below', ['core/group'], {
    'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}}})
section('framed', 'Framed screen', ['core/image', 'core/post-featured-image'], {
    'css': '& img{border:2px solid var(--wp--preset--color--contrast);display:block}'})
section('framed-wide', 'Framed screen, wide crop', ['core/image'], {
    'css': '& img{border:2px solid var(--wp--preset--color--contrast);display:block;width:100%;aspect-ratio:16/9;object-fit:cover}'})
section('box', 'Diagram box', ['core/group'], {
    'color': {'background': 'var:preset|color|surface'},
    'border': {'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}}})
section('arrow-row', 'Flow with arrows', ['core/group'], {
    'css': '& > .wp-block-group{position:relative}@media (min-width:782px){& > .wp-block-group:not(:last-child)::after{content:"\\2192";position:absolute;right:-1.15em;top:50%;transform:translateY(-50%);font-weight:800;font-size:1.4em;color:var(--wp--preset--color--accent)}}'})
section('row-rule', 'Ruled row', ['core/group', 'core/columns'], {
    'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})
section('big-figure', 'Big figure', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '900', 'lineHeight': '1'},
    'css': '&{font-stretch:80%;font-variant-numeric:tabular-nums}'})
section('tag', 'Tag', ['core/paragraph', 'core/post-terms'], {
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'},
    'css': '&{display:inline-block;align-self:flex-start;border:2px solid var(--wp--preset--color--contrast);padding:.2em .6em;width:fit-content}& a{text-decoration:none;color:inherit}'})


# ---------------------------------------------------------------- functions.php (pattern categories only)
CATS = [('case-study', 'Case study blocks'), ('case-page', 'Case study pages'), ('hero', 'Heroes'), ('work', 'Work lists'),
        ('services', 'Working together'), ('about', 'About'), ('contact', 'Contact'), ('writing', 'Writing')]
write('functions.php', "<?php\n/**\n * Case: registers the pattern categories used by the theme's patterns.\n *\n * @package case\n */\n\nadd_action(\n\t'init',\n\tfunction () {\n"
      + ''.join("\t\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', 'case' ) ) );\n" % c for c in CATS) + "\t}\n);\n")

# ---------------------------------------------------------------- parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')), justify='space-between', align='wide'),
    tag='header', align='full', className='is-style-rule-bottom',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}))

write('parts/footer.html', group(J(
    columns(
        ('55%', J(heading('Got a service people queue for?', 2, fontSize='x-large'),
                  para('I am booked until January 2027 and take on one new project at a time. Tell me what is broken and who it is broken for.'),
                  buttons(('Email Nadia', 'mailto:nadia@example.com?subject=Project')))),
        (None, J(heading('Elsewhere', 6),
                 para('<a href="https://www.linkedin.com/">LinkedIn</a><br><a href="/about/#cv">CV, one page</a><br><a href="/pattern-library/">Case study blocks</a>', fontSize='small'))),
        (None, J(heading('Based in', 6),
                 para('Glasgow, working with teams in the UK and the Netherlands. In the office at the Whisky Bond on Tuesdays.', fontSize='small'))),
        align='wide'),
    para('Photographs are CC0 images from Wikimedia Commons. Screens and wireframes were drawn for this demo.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-ink', style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

# ---------------------------------------------------------------- the case study kit
IMG = {
    'kiosk-3': 'A blue and yellow ticket machine on a station platform, with a route map on its touchscreen and a card reader below',
    'kiosk-2': 'A row of ticket machines under a large fare map in a station hall',
    'kiosk': 'A ticket machine touchscreen showing a grid of fare prices in red and blue buttons',
    'departures': 'A station concourse with a departure board, people walking past and a bicycle',
    'phone-2': 'Three passengers on a station platform, each looking at their phone',
    'selfcheckout': 'A self-checkout screen beside a bin for scanning clothes, with the total shown in yen',
    'parking': 'Two parking meters on a pavement next to concrete road barriers',
    'laptop': 'A laptop on a white desk next to a lamp and stacks of books',
    'postit': 'A wall covered in pastel sticky notes written by customers',
    'map': 'A paper timetable notice taped behind scratched plastic at a bus stop',
    'ui-kiosk-before': 'Old ticket machine screen: a grid of twelve fare zone buttons, with the railcard question below',
    'ui-kiosk-after': 'New ticket machine screen: a search box, then a list of nearby stations with journey times, Partick highlighted',
    'ui-kiosk-price': 'Price screen: three ticket types, each with the railcard price highlighted beside the full price',
    'wf-kiosk': 'Four lo-fi wireframes in a row: destination, map, ticket and price, pay, joined by arrows',
    'wf-parking': 'Four lo-fi wireframes: street, how long, pay, reminder',
    'wf-checkout': 'Four lo-fi wireframes: scan, remove tags, bag, pay',
    'ui-parking': 'Three phone screens: choose the street, choose how long, and a confirmation with a text reminder',
    'ui-checkout': 'Self-checkout screen titled step 2 of 4, take the tags off, listing three items and their tag status',
    'ui-departures': 'A bus stop display in amber showing the next four buses and minutes until each arrives',
    'sk-journey': 'Pencil sketch of the ticket journey in six steps, with a line dipping lowest at the price screen',
    'ui-kit': 'Design system sheet: five colour swatches, two type sizes, three button styles and the search field',
}
IMGPATH = '/wp-content/themes/case/assets/images/'


def tag(t):
    return para(t, className='is-style-tag')


def fig(f, cap='', **kw):
    kw.setdefault('className', 'is-style-framed')
    return image(f, IMG[f[:-4]], cap, **kw)


def h3(t, anchor=None):
    return heading(t, 3, anchor=anchor) if anchor else heading(t, 3)


def cs_facts(rows):
    return group(J(*[stack(J(heading(k, 6), para(v, fontSize='small')), style={'spacing': {'blockGap': 'var:preset|spacing|10'}}) for k, v in rows]),
                 className='is-style-rule-top', align='wide', layout={'type': 'grid', 'minimumColumnWidth': '11rem'})


def cs_hero(s):
    return J(cs_facts(s['facts']), fig(s['lead'], s['lead_cap'], align='wide'))


def cs_intro(s):
    return J(para(s['intro'], fontSize='large'), cs_toc(s))


def cs_toc(s):
    items = ['<a href="#%s">%s</a>' % (a, t) for a, t in s['toc']]
    return group(J(heading('In this case study', 6), lst(items, ordered=True)), className='is-style-rule-top')


def stage(n, of, name, anchor):
    return group(row(J(para('Stage %d of %d' % (n, of), fontSize='small'), heading(name, 2, fontSize='xx-large', anchor=anchor)), justify='space-between', align='wide'),
                 className='is-style-stage', align='full')


def cs_problem(s):
    return J(h3('The problem', 'problem'), para('<mark>%s</mark> %s' % (s['problem'][0], s['problem'][1])), para(s['problem'][2]))


def cs_hypothesis(s):
    return group(J(heading('Hypothesis', 6), para(s['hypothesis'], fontSize='large')), className='is-style-lime')


def cs_constraints(s):
    return J(h3('Constraints', 'constraints'),
             group(J(*[group(J(heading(a, 5), para(b, fontSize='small')), className='is-style-box') for a, b in s['constraints']]),
                   layout={'type': 'grid', 'minimumColumnWidth': '13rem'}))


def cs_methods(s):
    return J(h3('How we researched it', 'research'),
             group(J(*[columns(('30%', heading(a, 5)), (None, para(b)), className='is-style-row-rule') for a, b in s['methods']]), layout={'type': 'default'}))


def cs_insights(s):
    return J(h3('What we learned'), lst(['<strong>%s</strong> %s' % (a, b) for a, b in s['insights']], ordered=True))


def cs_voice(s):
    q, who = s['voice']
    return group(J(para('“%s”' % q, fontSize='x-large', fontFamily='display', style={'typography': {'fontWeight': '800', 'lineHeight': '1.1'}}), para(who, fontSize='small')),
                 className='is-style-rule-top')


def cs_personas(s):
    cards = []
    for name, meta, need, quote_ in s['personas']:
        cards.append(group(J(heading(name, 4), para(meta, fontSize='small'), heading('Needs', 6), para(need, fontSize='small'),
                             para('“%s”' % quote_, className='is-style-lime', fontSize='small')), className='is-style-case-card'))
    return J(h3('Who we designed for', 'personas'), group(J(*cards), layout={'type': 'grid', 'minimumColumnWidth': '16rem'}))


def cs_journey(s):
    cols = []
    for st, doing, pain in s['journey']:
        extra = {'className': 'is-style-lime'} if pain.startswith('!') else {}
        cols.append(group(J(heading(st, 5), para(doing, fontSize='small'), para(pain.lstrip('!'), fontSize='small', **extra)), className='is-style-box'))
    return J(h3('Journey map', 'journey'), group(J(*cols), align='wide', layout={'type': 'grid', 'minimumColumnWidth': '10rem'}),
             para('Rows: what people do, then what goes wrong. The lime cell is where most people gave up.', fontSize='x-small'))


def cs_flow(s):
    boxes = [group(J(heading(a, 5), para(b, fontSize='small')), className='is-style-box') for a, b in s['flow']]
    return J(h3('The new flow', 'flow'), group(J(*boxes), align='wide', className='is-style-arrow-row', layout={'type': 'grid', 'minimumColumnWidth': '10rem'}))


def cs_wireframes(s):
    return J(h3('Wireframes', 'wireframes'), para(s['wire_note']), fig(s['wire'], s['wire_cap'], align='wide'))


def cs_decisions(s):
    rows = []
    for opt, verdict, why in s['decisions']:
        rows.append(columns(('32%', heading(opt, 5)), ('18%', tag(verdict)), (None, para(why, fontSize='small')), className='is-style-row-rule', verticalAlignment='top'))
    return J(h3('Options we tried', 'decisions'), group(J(*rows), layout={'type': 'default'}))


def cs_before_after(s):
    b, bc, a, ac, what = s['ba']
    return J(h3('Before and after', 'before-after'),
             columns((None, J(tag('Before'), fig(b, bc))), (None, J(tag('After'), fig(a, ac))), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
             para('<strong>What changed:</strong> %s' % what, fontSize='small'))


def cs_system(s):
    return J(h3('Design system', 'system'), para(s['system']), fig('ui-kit.jpg', 'The machine UI kit we handed over, version 2', align='wide'))


def cs_prototype(s):
    img, text, url = s['prototype']
    return columns(('58%', fig(img)), (None, J(h3('Prototype', 'prototype'), para(text), buttons(('Open the clickable prototype', url)))), align='wide', verticalAlignment='center',
                   style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}})


def cs_testing(s):
    rows = [columns(('50%', para(t)), (None, para(b, className='is-style-big-figure')), (None, para(a, className='is-style-big-figure')), className='is-style-row-rule', isStackedOnMobile=False)
            for t, b, a in s['testing']]
    head = columns(('50%', heading('Task', 6)), (None, heading('Old flow', 6)), (None, heading('New flow', 6)), isStackedOnMobile=False)
    return J(h3('Usability testing', 'testing'), para(s['testing_note']), group(J(head, *rows), layout={'type': 'default'}))


def cs_metrics(s):
    rows = [columns(('40%', J(heading(lab, 5), para(src, fontSize='x-small'))), (None, J(heading('Before', 6), para(b, className='is-style-big-figure'))),
                    (None, J(heading('After', 6), para(a, className='is-style-big-figure'))), className='is-style-row-rule', isStackedOnMobile=False)
            for lab, b, a, src in s['metrics']]
    return J(h3('What happened', 'results'), group(J(*rows), layout={'type': 'default'}), para(s['metrics_note'], fontSize='small'))


def cs_client(s):
    return quote(s['client'][0], s['client'][1])


def cs_learnings(s):
    return group(J(heading('What I would do differently', 4), para(s['learning'])), className='is-style-lime')


def cs_credits(s):
    return group(J(heading('Credits', 6), para(s['credits'], fontSize='small')), className='is-style-rule-top')


def cs_gallery(s):
    return J(h3('Screens', 'screens'), gallery([(f, IMG[f[:-4]], c) for f, c in s['gallery']], columns=len(s['gallery']), align='wide'))


def cs_research_photo(s):
    f, cap = s['field']
    return fig(f, cap, align='wide', className='is-style-framed-wide')


def cs_timeline(s):
    return J(h3('Timeline', 'timeline'),
             group(J(*[group(J(heading(w, 6), heading(t, 5), para(d, fontSize='small')), className='is-style-rule-top') for w, t, d in s['timeline']]),
                   align='wide', layout={'type': 'grid', 'minimumColumnWidth': '12rem'}))


# ---------------------------------------------------------------- case studies (data)
STUDIES = [
    dict(slug='ticket-machines-that-ask-where-you-are-going', title='Ticket machines that ask where you are going', cat='transport', featured='ui-kiosk-after.jpg',
         excerpt='Clyde Valley Rail lost a third of ticket sales at the machine. Moving one question to the front halved that.',
         facts=[('Client', 'Clyde Valley Rail'), ('Role', 'Lead product designer, research and UI'), ('Timeline', 'March to October 2025, 30 weeks'),
                ('Team', 'Me, two developers, a PM and station staff'), ('Platform', 'Ticket machines, 1080 × 1920 touchscreen')],
         lead='ui-kiosk-after.jpg', lead_cap='The new first screen: where are you going, with the nearest stations listed',
         intro='The operator’s ticket machines asked for a fare zone before a destination. Most people do not know their fare zone. This is how we found that out on the platforms and what we changed.',
         toc=[('problem', 'The problem'), ('research', 'Research'), ('personas', 'Who we designed for'), ('journey', 'Journey map'), ('flow', 'The new flow'), ('before-after', 'Before and after'), ('testing', 'Testing'), ('results', 'Results')],
         problem=('A third of people who started buying a ticket at a machine gave up before paying.', 'The operator’s own logs showed it. Most of them then queued at the ticket office, which closes at 7pm at 22 of the 38 stations.',
                  'The machines ask for the fare zone first. If your station was not on the first screen of twelve, you had to know the name of the zone.'),
         hypothesis='If the machine asks where you are going first and shows the price last, fewer people will give up before paying.',
         constraints=[('Brand rules', 'Colours and the typeface on the machines were fixed by the operator’s brand team.'), ('Old hardware', 'The screens are nine years old and take 300 ms to draw each new screen, so every screen stays still.'),
                      ('Cash', 'Six percent of people pay in cash and the coin slot is at knee height.'), ('Two languages', 'Everything had to work in English and Scottish Gaelic.')],
         methods=[('Platform observation', '20 hours at 11 stations, standing next to the machines in hi-vis, morning and evening peaks and a Saturday afternoon.'),
                  ('Short interviews', '46 interviews of about four minutes, straight after people bought a ticket or gave up.'),
                  ('Log analysis', 'Eight weeks of machine logs: which screen each session ended on.'), ('Staff sessions', 'Two workshops with ticket office staff, who knew most of the answers already.')],
         insights=[('People start with where they are going.', '41 of 46 said the destination first when we asked what they wanted.'), ('The railcard question lost the most people.', 'It came before the price, so nobody could see what a railcard would save them.'),
                   ('Card readers were fine. Cash was the problem.', 'Cash journeys took three times as long.'), ('Staff already had a workaround.', 'They taped a list of fare zones to the side of the machine at Partick.')],
         voice=('I know I am going to Partick. I do not know what zone Partick is in and I should not have to.', 'Passenger at Glasgow Queen Street, April 2025'),
         personas=[('The evening commuter', 'Travels daily, has a railcard, buys a return after 5pm when the office is shut', 'To buy the same ticket in under 30 seconds', 'Just let me press Partick.'),
                   ('The Saturday visitor', 'Comes into town twice a month with family, pays by card, unsure of the fares', 'To see the price before committing', 'Is the day ticket cheaper or not?')],
         journey=[('Arrive', 'Walk to the machine, check the queue', 'Queue of three at 5.40pm'), ('Start', 'Tap the screen', 'Screen asks for a fare zone'),
                  ('Choose', 'Scroll the fare grid', '!Most people give up here'), ('Railcard', 'Answer the railcard question', 'No price shown yet'), ('Pay', 'Card or cash', 'Coin slot at knee height')],
         flow=[('Destination', 'Search or pick from nearby stations'), ('Ticket', 'Single, return or day, with prices'), ('Railcard', 'Saving shown next to each price'), ('Pay', 'Card, phone or cash')],
         wire='wf-kiosk.jpg', wire_cap='Lo-fi flow we tested on paper taped over a real machine', wire_note='We tested the first versions on paper taped over the screen. Station staff held the clipboard.',
         decisions=[('Map-first screen', 'Dropped', 'People liked it but it took 11 seconds longer. Kept as a secondary route for visitors.'),
                    ('Search box first', 'Kept', 'Fastest for regulars. The list of nearest stations covers people who do not want to type.'),
                    ('Railcard after price', 'Kept', 'Showing the saving next to the price doubled railcard sales in testing.')],
         ba=('ui-kiosk-before.jpg', 'Fare grid first. You had to pick a zone before a place.', 'ui-kiosk-after.jpg', 'Destination first, with the nearest stations listed.',
             'the order of the questions. The visual design barely moved, because the brand rules fix colours and type on the machines.'),
         system='The operator had no design system for machines, only for the website. We wrote a small one: five colours, two type sizes, three buttons and one search field, all tested at arm’s length.',
         prototype=('ui-kiosk-price.jpg', 'The clickable prototype ran on a tablet clamped to a real machine at Partick for two weeks.', 'https://www.figma.com/'),
         testing_note='Twelve people per round, three rounds, all recruited on the platform with a £10 coffee voucher.',
         testing=[('Buy a single to Partick', '48%', '92%'), ('Buy a return with a railcard', '31%', '83%'), ('Find the cheapest day ticket', '22%', '75%')],
         metrics=[('Journeys started but not paid for', '33%', '14%', 'Machine logs, 8 weeks before and after'), ('Median time to buy a single', '71 s', '38 s', 'Session timings, 2,400 sessions'),
                  ('Ticket office queue after 5pm, Partick', '12', '5', 'Staff head counts, 20 evenings')],
         metrics_note='The operator paused the rollout at 12 stations while they replace the card readers, so the full numbers are not in yet.',
         client=('Nadia spent more time on our platforms than some of our managers. The change looks small on a screen, and it cut the evening queues at Partick in half.', 'Callum Ross, head of retail, Clyde Valley Rail'),
         learning='I tested with commuters first because they were easy to find at 8am. They were also the people who needed the machines least. Next time I start with the Saturday afternoon crowd.',
         credits='Research and design: Nadia Branković. Development: Priya Nair and Tom Kerr. Product: Jamie Walsh. Station staff at Partick, Queen Street and Paisley.',
         gallery=[('ui-kiosk-after.jpg', 'Destination'), ('ui-kiosk-price.jpg', 'Price with railcard'), ('ui-kit.jpg', 'UI kit')],
         field=('kiosk-3.jpg', 'Testing on a live machine, September 2025'),
         timeline=[('Weeks 1 to 4', 'On the platforms', 'Observation, interviews, logs'), ('Weeks 5 to 10', 'Paper prototypes', 'Three rounds of testing'),
                   ('Weeks 11 to 22', 'Build', 'Two developers, weekly releases to one machine'), ('Weeks 23 to 30', 'Rollout', '26 of 38 stations so far')]),
    dict(slug='parking-without-the-meter', title='Parking without the meter', cat='public-services', featured='ui-parking.jpg',
         excerpt='Renfrew Council wanted to remove 300 meters. We made sure nobody got a fine because of it.',
         facts=[('Client', 'Renfrew Council'), ('Role', 'Service designer, then UI for the app and texts'), ('Timeline', 'January to August 2024'), ('Team', 'Me, a council product owner, an agency developer'), ('Platform', 'SMS, iOS and Android, street signs')],
         lead='ui-parking.jpg', lead_cap='The three app screens: street, time, confirmation',
         intro='The council was removing coin meters in Paisley town centre. Two thirds of parking fines were already for people who had paid, but for the wrong zone.',
         toc=[('problem', 'The problem'), ('research', 'Research'), ('flow', 'The new flow'), ('decisions', 'Options'), ('results', 'Results')],
         problem=('Two thirds of fines in the town centre went to people who had paid.', 'They had paid for the wrong zone. The zone number was on a sticker on the meter.', 'The meters were about to be removed, and with them the stickers.'),
         hypothesis='If people pay by street name instead of zone number, wrong-zone fines will mostly disappear.',
         constraints=[('Existing supplier', 'The payment back end was a national supplier we could not replace.'), ('Older drivers', 'A third of permit holders are over 65 and pay by text.'), ('Signs', 'New street signs had to go through a council committee.')],
         methods=[('Fine appeals', 'We read 400 appeal letters from 2023. Half named a street, none named a zone.'), ('Car park interviews', '38 drivers in the Lagoon Centre car park and on Causeyside Street.'), ('Text diary', '12 permit holders texted us every time they parked for two weeks.')],
         insights=[('Nobody knows their zone.', 'Every appeal letter describes a street.'), ('Texts beat the app.', 'People over 50 preferred a text they could send without unlocking anything.'), ('Reminders matter more than payment.', 'Most fines were for overstaying by under ten minutes.')],
         voice=('I paid. I have the receipt. It just says P4 and I parked on Gauze Street.', 'Appeal letter, October 2023'),
         flow=[('Street', 'Type or pick the street'), ('Time', 'Pick how long, price shown'), ('Pay', 'Card, Apple Pay or text'), ('Reminder', 'Text ten minutes before it runs out')],
         wire='wf-parking.jpg', wire_cap='Lo-fi screens for the street-first flow', wire_note='The same four steps work by text: send the street name and the hours to 60070.',
         decisions=[('Zone map in the app', 'Dropped', 'Tested badly. People could not find themselves on it.'), ('Street name search', 'Kept', 'Matches how people describe where they parked.'), ('Pay by text', 'Kept', 'Cheapest to run and most used by older drivers.')],
         ba=('parking.jpg', 'The old meters, with the zone sticker most people never read', 'ui-parking.jpg', 'Street first, time second, reminder by default',
             'the unit people pay for. It is now a street, which the council maps to a zone behind the scenes.'),
         testing_note='Two rounds with 10 drivers each, in their own cars.',
         testing=[('Pay for one hour on Gauze Street', '6 of 10', '10 of 10'), ('Extend by 30 minutes', '4 of 10', '9 of 10')],
         metrics=[('Fines for wrong zone, per month', '312', '41', 'Council enforcement data, first three months'), ('Appeals upheld', '58%', '12%', 'Council appeals team')],
         metrics_note='Numbers are for the town centre only. The rest of Renfrewshire switches in 2026.',
         client=('Nadia is the only designer who asked to see our complaint letters. Half the redesign came out of that folder.', 'Aoife Byrne, parking services manager, Renfrew Council'),
         learning='I left the street signs until last. They took the longest to approve, and the app was ready months before the signs were up.',
         credits='Service design and UI: Nadia Branković. Product owner: Aoife Byrne. Development: Kelvin Digital.',
         field=('parking.jpg', 'One of the 300 meters that came out in 2024')),
    dict(slug='self-checkout-for-a-clothing-chain', title='Self-checkout for a clothing chain', cat='retail', featured='ui-checkout.jpg',
         excerpt='Kilt & Co. customers paid, then waited for staff to remove tags. We moved the tag step first.',
         facts=[('Client', 'Kilt & Co., 14 stores'), ('Role', 'Product designer, research and UI'), ('Timeline', 'May to November 2023'), ('Team', 'Me, a retail operations lead, the till software vendor'), ('Platform', 'Self-checkout kiosks, 21 inch')],
         lead='ui-checkout.jpg', lead_cap='Step 2 of 4, before payment: take the tags off',
         intro='Self-checkouts at Kilt & Co. were meant to shorten queues. They made new ones, at the security desk.',
         toc=[('problem', 'The problem'), ('journey', 'Journey map'), ('before-after', 'Before and after'), ('results', 'Results')],
         problem=('Customers paid, then waited for staff to remove security tags.', 'The tag step came after payment, so every customer ended up at the staffed desk anyway.', 'At weekends the queue for tags was longer than the old till queue.'),
         hypothesis='If tag removal comes before payment, while the basket is still open, most customers will never need staff.',
         constraints=[('Vendor software', 'We could change the order of screens but not add new hardware.'), ('Tag types', 'Three kinds of tag, only one removable by the customer.')],
         methods=[('Store observation', 'Four weeks in eight stores, Saturdays included.'), ('Staff diary', 'Floor staff logged every call to the kiosk for a week.')],
         insights=[('Most items had the easy tag.', '80% of items used the magnetic tag that the kiosk pad can release.'), ('Staff calls were about tags.', '7 of 10 calls to the kiosk were for tags.')],
         voice=('I have paid. Why am I in another queue?', 'Customer, Princes Street store, June 2023'),
         journey=[('Scan', 'Scan each item', 'Fine'), ('Pay', 'Card', 'Fine'), ('Bag', 'Bag the items', '!Alarm goes off at the door'), ('Wait', 'Queue at the desk for tags', 'Up to 9 minutes on Saturdays')],
         flow=[('Scan', 'Items go on the pad'), ('Tags', 'Pad releases magnetic tags'), ('Bag', 'Items into the bag'), ('Pay', 'Card or phone')],
         wire='wf-checkout.jpg', wire_cap='Lo-fi order of screens with the tag step moved to second', wire_note='We tried three orders on paper at the Princes Street store before touching the software.',
         ba=('selfcheckout.jpg', 'The old kiosk: pay first, tags later', 'ui-checkout.jpg', 'The new step 2: tags off before you pay', 'one step moved from after payment to before it.'),
         metrics=[('Median wait for staff at the kiosk', '2 min 40 s', '52 s', 'Store timings, 8 stores'), ('Calls to staff per 100 sales', '64', '19', 'Kiosk logs, 4 weeks')],
         metrics_note='Two stores with the older tag system are excluded.',
         client=('We moved one screen and the Saturday queue went away. I wish every project was that cheap.', 'Morag Sinclair, head of stores, Kilt & Co.'),
         learning='I should have asked the vendor about screen order in week one. We spent two weeks assuming it was fixed.',
         credits='Research and design: Nadia Branković. Operations: Morag Sinclair. Software: the till vendor’s Glasgow team.',
         gallery=[('ui-checkout.jpg', 'Tag step'), ('wf-checkout.jpg', 'Wireframes')]),
    dict(slug='live-departures-on-the-platform', title='Live departures on the platform', cat='transport', featured='ui-departures.jpg',
         excerpt='Bus stop displays and a phone view that agree with each other, for the first time.',
         facts=[('Client', 'Strathclyde bus partnership'), ('Role', 'Product designer, displays and app'), ('Timeline', 'September 2021 to June 2022'), ('Team', 'Me, two operators, a data engineer'), ('Platform', 'LED stop displays, phone web view')],
         lead='ui-departures.jpg', lead_cap='The stop display at Paisley Road Toll, stop G',
         intro='The stop displays and the app used two different data feeds, so they often disagreed by several minutes. People trusted neither.',
         toc=[('problem', 'The problem'), ('research', 'Research'), ('flow', 'The new flow'), ('results', 'Results')],
         problem=('The display and the app disagreed at 4 in 10 stops.', 'Displays used the timetable, the app used live GPS.', 'People at the stop checked both and believed the worse one.'),
         hypothesis='If the display and the phone show the same live times in the same words, people will trust them and stop checking both.',
         constraints=[('LED displays', 'Four lines of amber text, 24 characters each.'), ('Two operators', 'Two bus companies, two data formats.')],
         methods=[('Stop interviews', '30 people at six stops, evenings and in the rain.'), ('Feed comparison', 'Two weeks of both feeds side by side for 40 stops.')],
         insights=[('People read the first line only.', 'Almost nobody read past the next bus.'), ('Minutes beat clock times.', '2 min was understood faster than 17:42.')],
         voice=('The sign says 4 minutes, the app says 11. I just stand here.', 'Passenger at Paisley Road Toll, November 2021'),
         flow=[('Feed', 'One merged live feed'), ('Stop display', 'Next four buses in minutes'), ('Phone', 'Same list, same words'), ('Fallback', 'Timetable time marked as scheduled')],
         ba=('map.jpg', 'Before: a paper timetable behind scratched plastic', 'ui-departures.jpg', 'After: live minutes on the display, same as the phone', 'one feed, one wording, minutes instead of clock times.'),
         metrics=[('Stops where display and app disagree', '41%', '3%', 'Feed comparison, 40 stops'), ('People who said they trust the display', '28%', '71%', 'Stop survey, 120 people')],
         metrics_note='Survey numbers are from the six stops in the pilot.',
         client=('We had spent years arguing about whose data was right. Nadia made us agree on one list.', 'Graham Doyle, network manager, Strathclyde bus partnership'),
         learning='We designed for sunny screenshots. The first night of rain showed the amber was too dim at two stops.',
         credits='Design: Nadia Branković. Data: Fiona Clark. Operators: two Strathclyde bus companies.',
         gallery=[('ui-departures.jpg', 'Stop display'), ('departures.jpg', 'Concourse test')]),
]
S1 = STUDIES[0]

# ---------------------------------------------------------------- case study patterns (instances use the first study)
CP = 'case-study'
pattern('cs-overview', 'Case study: overview with role, timeline and team', CP, cs_hero(S1), description='Facts row (client, role, timeline, team, platform) and the lead screen.')
pattern('cs-intro', 'Case study: intro and contents', CP, cs_intro(S1), description='A one-paragraph summary and a numbered list of links to each section.')
pattern('cs-stage-band', 'Case study: stage band', CP, stage(1, 3, 'Research', 'stage-research'), description='A black band that starts each stage. Change the name and the number.')
pattern('cs-problem', 'Case study: the problem', CP, cs_problem(S1))
pattern('cs-hypothesis', 'Case study: hypothesis', CP, cs_hypothesis(S1))
pattern('cs-constraints', 'Case study: constraints', CP, cs_constraints(S1))
pattern('cs-research-methods', 'Case study: research methods', CP, cs_methods(S1))
pattern('cs-insights', 'Case study: research insights', CP, cs_insights(S1))
pattern('cs-user-quote', 'Case study: quote from research', CP, cs_voice(S1))
pattern('cs-field-photo', 'Case study: field photo, wide', CP, cs_research_photo(S1))
pattern('cs-personas', 'Case study: personas', CP, cs_personas(S1))
pattern('cs-journey-map', 'Case study: journey map', CP, cs_journey(S1))
pattern('cs-flow', 'Case study: user flow', CP, cs_flow(S1))
pattern('cs-wireframes', 'Case study: wireframes', CP, cs_wireframes(S1))
pattern('cs-decisions', 'Case study: options considered', CP, cs_decisions(S1))
pattern('cs-before-after', 'Case study: before and after', CP, cs_before_after(S1))
pattern('cs-design-system', 'Case study: design system', CP, cs_system(S1))
pattern('cs-prototype', 'Case study: prototype', CP, cs_prototype(S1))
pattern('cs-testing', 'Case study: usability testing', CP, cs_testing(S1))
pattern('cs-metrics', 'Case study: results and metrics', CP, cs_metrics(S1), description='Before and after figures with their source, as ruled rows.')
pattern('cs-client-quote', 'Case study: client quote', CP, cs_client(S1))
pattern('cs-learnings', 'Case study: what I would do differently', CP, cs_learnings(S1))
pattern('cs-credits', 'Case study: credits', CP, cs_credits(S1))
pattern('cs-screens-gallery', 'Case study: screens gallery (lightbox)', CP, cs_gallery(S1))
pattern('cs-timeline', 'Case study: project timeline', CP, cs_timeline(S1))
pattern('cs-screen-caption', 'Case study: screen with a text description', CP, J(
    fig('ui-kiosk-price.jpg', 'Price screen with the railcard saving beside each price', align='wide'),
    para('<strong>What changed:</strong> the railcard question used to come before the price. Now the saving sits next to each price, so people can see if a railcard is worth it.', fontSize='small')))
pattern('cs-nda-note', 'Case study: NDA note', CP, group(J(
    row(J(tag('Under NDA'), para('2024, 5 months', fontSize='small')), justify='space-between'),
    heading('Onboarding for a Dutch pension provider', 4),
    para('Redesigned the first 15 minutes of joining a workplace pension, for 400,000 members. Details are limited by the contract, but I am happy to talk it through on a call.')),
    className='is-style-case-card'))
pattern('cs-next', 'Case study: next case study', CP, group(J(
    para('Next case study', fontSize='small'),
    query(columns(('40%', dyn('post-featured-image', isLink=True, aspectRatio='16/10', scale='cover', className='is-style-framed')),
                  (None, J(dyn('post-title', isLink=True, level=2, fontSize='xx-large'), dyn('post-excerpt', showMoreOnPage=False)))),
          per_page=1, query_id=41).replace('"offset":0', '"offset":1', 1)),
    className='is-style-rule-top', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'}))


def full_study(s, refs=False):
    """Compose a complete case study. refs=True uses pattern references (for the first study, so the post shows the kit)."""
    R = (lambda slug, fn: pattern_ref(slug)) if refs else (lambda slug, fn: fn(s))
    parts = [R('cs-overview', cs_hero), R('cs-intro', cs_intro)]
    n = 3
    parts.append(pattern_ref('cs-stage-band') if refs else stage(1, n, 'Research', 'stage-research'))
    parts += [R('cs-problem', cs_problem), R('cs-hypothesis', cs_hypothesis)]
    if 'constraints' in s: parts.append(R('cs-constraints', cs_constraints))
    if 'methods' in s: parts.append(R('cs-research-methods', cs_methods))
    if 'field' in s: parts.append(R('cs-field-photo', cs_research_photo))
    if 'insights' in s: parts.append(R('cs-insights', cs_insights))
    if 'voice' in s: parts.append(R('cs-user-quote', cs_voice))
    if 'personas' in s: parts.append(R('cs-personas', cs_personas))
    if 'journey' in s: parts.append(R('cs-journey-map', cs_journey))
    parts.append(stage(2, n, 'Design', 'stage-design'))
    if 'flow' in s: parts.append(R('cs-flow', cs_flow))
    if 'wire' in s: parts.append(R('cs-wireframes', cs_wireframes))
    if 'decisions' in s: parts.append(R('cs-decisions', cs_decisions))
    parts.append(R('cs-before-after', cs_before_after))
    if 'system' in s: parts.append(R('cs-design-system', cs_system))
    if 'prototype' in s: parts.append(R('cs-prototype', cs_prototype))
    if 'gallery' in s: parts.append(R('cs-screens-gallery', cs_gallery))
    parts.append(stage(3, n, 'Results', 'stage-results'))
    if 'testing' in s: parts.append(R('cs-testing', cs_testing))
    parts += [R('cs-metrics', cs_metrics), R('cs-client-quote', cs_client)]
    if 'timeline' in s: parts.append(R('cs-timeline', cs_timeline))
    parts += [R('cs-learnings', cs_learnings), R('cs-credits', cs_credits)]
    return J(*parts)


pattern('case-study-full', 'Page: complete case study', 'case-page', full_study(S1, refs=True), block_types='core/post-content',
        description='Every case study block in order: overview, contents, research, design, results, learnings and credits.')
pattern('case-study-short', 'Page: short case study (one screen)', 'case-page', J(
    pattern_ref('cs-overview'), pattern_ref('cs-problem'), pattern_ref('cs-screen-caption'), pattern_ref('cs-metrics'), pattern_ref('cs-client-quote')), block_types='core/post-content',
    description='For smaller projects: overview, problem, one annotated screen, results and a quote.')

# ---------------------------------------------------------------- work lists, hero, services, about
WORK_ROWS = [('/ticket-machines-that-ask-where-you-are-going/', 'Clyde Valley Rail', '2025', 'Ticket machines that ask where you are going first', False),
             ('/parking-without-the-meter/', 'Renfrew Council', '2024', 'Paying for parking by street name, by text or app', False),
             (None, 'Dutch pension provider', '2024', 'Onboarding for workplace pension members', True),
             ('/self-checkout-for-a-clothing-chain/', 'Kilt & Co.', '2023', 'Self-checkout that handles security tags', False),
             (None, 'UK neobank', '2023', 'Card freeze and dispute flow', True),
             ('/live-departures-on-the-platform/', 'Strathclyde bus partnership', '2022', 'Live departures on stop displays and phones', False)]


def work_row(href, client, year, what, nda):
    name = ('<a href="%s">%s</a>' % (href, client.replace('&', '&amp;'))) if href else client.replace('&', '&amp;')
    return columns(('30%', heading(name, 4)), ('12%', para(year, fontSize='small')), (None, para(what)),
                   ('16%', tag('Under NDA') if nda else para('<a href="%s">Read it</a>' % href, fontSize='small')),
                   className='is-style-row-rule', verticalAlignment='center')


pattern('work-list', 'Work list: case studies and NDA entries', 'work', group(J(
    heading('Everything, briefly', 3), *[work_row(*r) for r in WORK_ROWS]), align='wide', layout={'type': 'constrained', 'contentSize': '1240px'}),
    description='Every project as a ruled row: published case studies link through, NDA work shows a marker and no link.')

CASE_CARD = columns(
    ('58%', dyn('post-featured-image', isLink=True, aspectRatio='16/10', scale='cover', className='is-style-framed')),
    (None, J(dyn('post-terms', term='category', className='is-style-tag'), dyn('post-title', isLink=True, level=2, fontSize='x-large'),
             dyn('post-excerpt', showMoreOnPage=False), dyn('read-more', content='Read the case study'))),
    verticalAlignment='center', className='is-style-case-card', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}})

pattern('case-cards', 'Case studies as big cards', 'work', group(J(
    row(J(heading('More case studies', 2), para('<a href="/work/">All work, including NDA projects</a>')), justify='space-between', align='wide'),
    query(CASE_CARD, per_page=3, query_id=42, align='wide', layout={'type': 'default'}).replace('"offset":0', '"offset":1', 1)),
    align='wide', layout={'type': 'default'}), keywords='case studies, work')

pattern('case-grid', 'Case studies as a two-column grid', 'work', query(
    J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover', className='is-style-framed'), dyn('post-terms', term='category', className='is-style-tag'),
      dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', showMoreOnPage=False, excerptLength=20)),
    per_page=4, query_id=43, align='wide', layout={'type': 'grid', 'columnCount': 2, 'minimumColumnWidth': '18rem'}))

pattern('case-archive', 'Case studies archive (inherits the page query)', 'work', inherit_query(CASE_CARD, align='wide', layout={'type': 'default'}), inserter=False)

pattern('hero-latest', 'Hero: name, one fact and the latest case study', 'hero', J(
    columns(('38%', J(heading('Nadia Branković', 1, fontSize='xx-large'),
                      para('Product designer in Glasgow. I work on ticket machines, parking, self-checkout and the apps next to them, and I start on the platform, not in Figma.'),
                      pattern_ref('capacity-note'),
                      buttons(('All case studies', '/work/'), ('Working together', '/working-together/', {'className': 'is-style-outline'})))),
            (None, query(J(dyn('post-featured-image', isLink=True, aspectRatio='16/10', scale='cover', className='is-style-framed'),
                           row(J(para('Latest case study', fontSize='small'), dyn('post-terms', term='category', className='is-style-tag')), justify='space-between'),
                           dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', showMoreOnPage=False)), per_page=1, query_id=44)),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|50'}}})),
    description='Opens with the work: the newest case study, beside a name and one line.')

pattern('hero-screens', 'Hero: three screens and a name', 'hero', J(
    heading('Nadia Branković, product designer', 1, fontSize='x-large'),
    gallery([('ui-kiosk-after.jpg', IMG['ui-kiosk-after'], 'Ticket machines, 2025'), ('ui-parking.jpg', IMG['ui-parking'], 'Parking, 2024'), ('ui-checkout.jpg', IMG['ui-checkout'], 'Self-checkout, 2023')], columns=3, align='wide')))

pattern('sectors', 'Sectors I work in', 'about', group(J(
    heading('Where I have worked', 4),
    group(J(*[group(J(heading(a, 5), para(b, fontSize='small')), className='is-style-box') for a, b in [
        ('Transport', 'Ticket machines, stop displays, journey planners'), ('Local councils', 'Parking, permits, bin collections'), ('Retail', 'Self-checkout, click and collect'), ('Finance', 'Onboarding, card controls, under NDA')]]),
        layout={'type': 'grid', 'minimumColumnWidth': '13rem'})), align='wide', layout={'type': 'default'}))

pattern('capacity-note', 'Capacity note', 'services', para(
    '<strong>One project at a time.</strong> Booked until January 2027. Enquiries open for February starts.', className='is-style-lime'),
    description='Update this line when your availability changes.')

pattern('engagements', 'Ways to work together', 'services', group(J(
    heading('Two ways to hire me', 2, fontSize='x-large'),
    columns(
        (None, group(J(heading('Design partner', 3), para('Three to nine months, three or four days a week, inside your team. Research, flows, UI and handover to your developers.'),
                       heading('When this fits', 6), para('You have a service with a measurable problem and a team that can ship changes every few weeks.', fontSize='small'),
                       para('From £3,900 a week', fontSize='large')), className='is-style-case-card')),
        (None, group(J(heading('Advisory', 3), para('Two days a month. I review research plans and designs, sit in on crits and help your designers argue for the change.'),
                       heading('When this fits', 6), para('You already have designers and want a second opinion from someone who has done this in public services.', fontSize='small'),
                       para('£2,200 a month', fontSize='large')), className='is-style-case-card')),
        align='wide'),
    pattern_ref('capacity-note')), align='wide', layout={'type': 'default'}))

pattern('process', 'How a project runs', 'services', group(J(
    heading('How a project runs', 3),
    group(J(*[group(J(heading(a, 5), para(b, fontSize='small')), className='is-style-box') for a, b in [
        ('Two weeks on site', 'I watch the service being used and talk to the people who run it.'),
        ('One problem statement', 'Written down and agreed, with the number we are trying to move.'),
        ('Prototypes in place', 'Paper first, then clickable, tested where people use the thing.'),
        ('Ship and write it up', 'You get the case study too, to use inside your organisation.')]]),
        className='is-style-arrow-row', layout={'type': 'grid', 'minimumColumnWidth': '12rem'})), align='wide', layout={'type': 'default'}))

pattern('what-i-dont-do', 'What I do not take on', 'services', group(J(
    heading('What I do not take on', 4),
    para('Dark patterns, gambling and payday lending. Brand identity and logos, which other people do much better. Projects where nobody on your side can talk to users.')),
    className='is-style-rule-top'))

pattern('faq', 'Questions teams ask', 'services', J(
    heading('Questions teams ask', 3),
    details('Do you work remotely?', para('Mostly, but research happens where the service is. Budget for two weeks on site.')),
    details('Can you work with our design system?', para('Yes. If there is none for the thing we are designing, I write a small one and hand it over.')),
    details('Who owns the work?', para('You do, once the invoice is paid. I ask to publish a case study, and I will show you the draft first.')),
    details('Do you sign NDAs?', para('Yes. Two of my last six projects are under one, and they appear on my site as a short note with no details.'))))

pattern('working-together-page', 'Page: working together', 'services', J(
    pattern_ref('engagements'), spacer('var:preset|spacing|60'), pattern_ref('process'), pattern_ref('what-i-dont-do'), pattern_ref('faq'), pattern_ref('testimonials')), block_types='core/post-content')

pattern('testimonials', 'Testimonials (named)', 'about', columns(
    (None, quote('She found the railcard problem in her first week. We had been looking at the wrong screen for two years.', 'Callum Ross, head of retail, Clyde Valley Rail, 2025')),
    (None, quote('Nadia is the only designer who asked to see our complaint letters. Half the redesign came out of that folder.', 'Aoife Byrne, parking services manager, Renfrew Council, 2024')),
    align='wide'))

pattern('about-bio', 'About: bio', 'about', columns(
    ('40%', fig('departures.jpg', 'Where I do most of my research: a station concourse at 5.40pm')),
    (None, J(heading('About', 2),
             para('I am Nadia Branković. I grew up in Sarajevo and Paisley, studied interaction design at Glasgow School of Art and spent seven years at a transport software company before going independent in 2021.'),
             para('I work on services that people use standing up, in a hurry, often in the rain. I think most UX problems in public services are ordering problems: the right questions asked in the wrong order.'),
             para('I do not do visual branding and I will not design anything that tricks people into paying more.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('cv', 'One-page CV', 'about', group(J(
    heading('CV', 3, anchor='cv'),
    table([['2021 to now', 'Independent product designer', 'Clyde Valley Rail, Renfrew Council, Kilt &amp; Co., two clients under NDA'],
           ['2014 to 2021', 'Senior designer, then design lead, Tramline Software', 'Journey planners and ticketing for 14 UK operators'],
           ['2013', 'MDes Interaction Design', 'Glasgow School of Art'],
           ['Speaking', 'UX Scotland 2024, Service Design in Government 2023', '']], head=['When', 'What', 'Where'])),
    align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}), description='A one-page CV that prints cleanly.')

pattern('talks', 'Talks and writing', 'writing', group(J(
    heading('Talks and writing', 4),
    lst(['<a href="/the-order-of-questions/">The order of questions</a>, UX Scotland, Edinburgh, June 2024',
         '<a href="/research-on-a-platform-in-the-rain/">Research on a platform in the rain</a>, Service Design in Government, 2023'])), className='is-style-rule-top'))

pattern('toolkit', 'Tools I use', 'about', group(J(
    heading('Tools', 4),
    para('Paper, a clipboard and a hi-vis vest. Then Figma and FigJam, Maze for remote tests, and a spreadsheet for the logs. I write everything up in plain documents that the client keeps.')),
    className='is-style-rule-top'))

pattern('about-page', 'Page: about', 'about', J(pattern_ref('about-bio'), spacer('var:preset|spacing|60'), pattern_ref('sectors'), pattern_ref('cv'), pattern_ref('toolkit'), pattern_ref('talks')), block_types='core/post-content')

pattern('contact-page', 'Page: contact', 'contact', J(
    columns((None, J(heading('Tell me what is broken', 2, fontSize='x-large'),
                     para('Email <a href="mailto:nadia@example.com">nadia@example.com</a> with the service, who uses it and what you have tried. A number helps, even a rough one.'),
                     para('I reply within two working days. If I am not the right person, I will say so and suggest someone.'))),
            (None, J(pattern_ref('capacity-note'), pattern_ref('contact-details'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})), block_types='core/post-content')

pattern('contact-details', 'Contact details', 'contact', group(J(
    *[columns(('30%', heading(a, 6)), (None, para(b)), className='is-style-row-rule', isStackedOnMobile=False) for a, b in [
        ('Email', '<a href="mailto:nadia@example.com">nadia@example.com</a>'), ('Phone', '07700 900 418, weekdays 9 to 5'),
        ('Office', 'The Whisky Bond, 2 Dawson Road, Glasgow G4 9SS'), ('Days in', 'Tuesdays, and by arrangement')]]), layout={'type': 'default'}))

pattern('newsletter', 'Newsletter', 'writing', group(J(
    heading('Notes from the platform', 3),
    para('One email every six weeks: what I saw people struggle with, and what we changed.'),
    buttons(('Subscribe by email', 'mailto:nadia@example.com?subject=Subscribe'))), className='is-style-ink', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('article-intro', 'Article: standfirst and notes', 'writing', J(
    para('A talk I gave at UX Scotland in June 2024, written up. About twelve minutes to read.', fontSize='large'),
    group(J(heading('Short version', 6), para('Most public service forms ask the right questions in the wrong order. Reorder them before you redesign them.')), className='is-style-lime')))

pattern('post-list', 'Search results list', 'work', inherit_query(
    group(J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30)), className='is-style-rule-top'), align='wide'), inserter=False)

# ---------------------------------------------------------------- templates
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('hero-latest'), pattern_ref('case-cards'), pattern_ref('work-list'), pattern_ref('sectors'), pattern_ref('testimonials')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|70'}}),
    template_part('footer', 'footer')))

write('templates/home.html', page_template(J(
    heading('Work', 1, align='wide'),
    para('Case studies I can publish, and short entries for the ones I cannot.', align='wide', fontSize='large'),
    pattern_ref('case-archive'), spacer('var:preset|spacing|60'), pattern_ref('work-list')),
    layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|50', 'padding': MAINPAD['spacing']['padding']}}))
write('templates/index.html', open(os.path.join(D, 'templates/home.html')).read())

write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', level=1),
    dyn('term-description', align='wide'), pattern_ref('case-archive')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide', level=1),
    dyn('search', label='Search', showLabel=False, buttonText='Search', align='wide'),
    pattern_ref('post-list')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/404.html', page_template(J(
    heading('Dead end', 1),
    para('This page does not exist. It is the kind of thing I get paid to fix.', fontSize='large'),
    dyn('search', label='Search', showLabel=False, buttonText='Search'),
    buttons(('Back to the work', '/work/'))), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/single.html', J(template_part('header', 'header'), group(J(
    group(J(dyn('post-terms', term='category', className='is-style-tag'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', showMoreOnPage=False, fontSize='large')),
          align='wide', layout={'type': 'constrained', 'contentSize': '900px', 'justifyContent': 'left'}),
    dyn('post-content', align='full', layout={'type': 'constrained'}),
    pattern_ref('cs-next')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|50', 'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}),
    template_part('footer', 'footer')))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1),
    dyn('post-content', layout={'type': 'constrained'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1, align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})), layout={'type': 'constrained'}, style=MAINPAD))

# ---------------------------------------------------------------- demo content (case studies are built from the kit)
import re
PHPIMG = re.compile(r"<\?php echo esc_url\( get_theme_file_uri\( 'assets/images/([\w.-]+)' \) \); \?>")
def as_post(markup):
    return PHPIMG.sub(lambda m: IMGPATH + m.group(1), markup)


def P(t):
    return para(t)


posts = []
for i, s in enumerate(STUDIES):
    item = dict(title=s['title'], slug=s['slug'], category=s['cat'], image=s['featured'], excerpt=s['excerpt'], date=['2025-10-20', '2024-09-12', '2023-11-02', '2022-06-15'][i])
    if i == 0:
        item['pattern'] = 'case/case-study-full'
    else:
        item['content'] = as_post(full_study(s))
    posts.append(item)
posts += [
    dict(title='The order of questions', slug='the-order-of-questions', category='writing', image='postit.jpg', date='2024-06-20', excerpt='A talk from UX Scotland 2024: reorder a form before you redesign it.',
         content=as_post(J(pattern_ref('article-intro'),
                           P('Every service I have worked on had a form that asked the right questions in the wrong order. The ticket machine asked for a fare zone before a destination. The parking app asked for a zone before a street. The pension onboarding asked for a salary before explaining why.'),
                           heading('Why order matters more than layout', 2, fontSize='x-large'),
                           P('People answer the question they came with first. If the first screen asks something else, they either guess or leave. On a ticket machine, a third of people left.'),
                           fig('ui-kiosk-before.jpg', 'The old first screen asked for a fare zone'),
                           P('Before you touch the visual design, write down the questions in the order a person would say them out loud. Then build the screens in that order.'),
                           pattern_ref('newsletter')))),
    dict(title='Research on a platform in the rain', slug='research-on-a-platform-in-the-rain', category='writing', image='phone-2.jpg', date='2023-03-02', excerpt='Notes on doing four-minute interviews next to a ticket machine, and why a hi-vis vest helps.',
         content=as_post(J(P('Most of my research happens on platforms and pavements. People are in a hurry, it is often raining, and nobody wants to sign a consent form.'),
                           heading('What works', 2, fontSize='x-large'),
                           lst(['Wear a hi-vis vest and stand next to station staff. People assume you are official and helpful, which you are.',
                                'Ask one question: what were you trying to do just now? Then listen for four minutes.',
                                'Write the answer on a card straight away, with the time and the station.',
                                'Offer a coffee voucher after, not before.']),
                           fig('departures.jpg', 'A concourse at 5.40pm, the busiest time and the best time to watch'),
                           P('You will get fewer words than in a lab. You will get the real problem much faster.')))),
]
demo = {'site': {'title': 'Nadia Branković', 'tagline': 'Product designer for services people queue for'},
        'categories': [{'slug': 'transport', 'name': 'Transport'}, {'slug': 'public-services', 'name': 'Public services'}, {'slug': 'retail', 'name': 'Retail'}, {'slug': 'writing', 'name': 'Writing'}],
        'front_page': 'home', 'posts_page': 'work',
        'pages': [{'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'work', 'title': 'Work', 'content': ''},
                  {'slug': 'working-together', 'title': 'Working together', 'pattern': 'case/working-together-page', 'template': 'page-wide'},
                  {'slug': 'about', 'title': 'About', 'pattern': 'case/about-page', 'template': 'page-wide'},
                  {'slug': 'contact', 'title': 'Contact', 'pattern': 'case/contact-page', 'template': 'page-wide'},
                  {'slug': 'short-case-study', 'title': 'A short case study', 'pattern': 'case/case-study-short', 'template': 'page-wide'}],
        'posts': posts,
        'nav': [{'label': 'Work', 'url': '/work/'}, {'label': 'Writing', 'url': '/category/writing/'}, {'label': 'Working together', 'url': '/working-together/'},
                {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}]}
os.makedirs('demos/case', exist_ok=True)
json.dump(demo, open('demos/case/content.json', 'w'), indent=1, ensure_ascii=False)

print('case built')
