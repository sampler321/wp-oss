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


def group(inner, tag='div', layout='constrained', **attrs):
    # The normaliser drops `layout` from a plain div group that also carries `style`; a section tag keeps it.
    if tag == 'div' and attrs.get('style') and layout and layout != {'type': 'default'}:
        tag = 'section'
    return _b.group(inner, tag=tag, layout=layout, **attrs)


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
                fs('display', '6.5rem', 'Display', '3.2rem'),
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
section('tag', 'Tag', ['core/paragraph', 'core/post-terms'], {
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'},
    'css': '&{display:inline-block;align-self:flex-start;border:2px solid var(--wp--preset--color--contrast);padding:.2em .6em;width:fit-content}& a{text-decoration:none;color:inherit}'})

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
                 para('<a href="https://www.linkedin.com/">LinkedIn</a><br><a href="/about/#cv">CV, one page</a><br><a href="mailto:nadia@example.com">nadia@example.com</a>', fontSize='small'))),
        (None, J(heading('Based in', 6),
                 para('Glasgow, working with teams in the UK and the Netherlands. In the office at the Whisky Bond on Tuesdays.', fontSize='small'))),
        align='wide'),
    para('Demo photographs are CC0 images from Wikimedia Commons, used as stand-ins for real project screens.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-ink', style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}))

# ---------------------------------------------------------------- patterns
IMG = {
    'kiosk-3': 'A blue and yellow ticket machine on a station platform, with a route map on its touchscreen and a card reader below',
    'kiosk-2': 'A row of ticket machines under a large fare map in a station hall',
    'kiosk': 'A ticket machine touchscreen showing a grid of fare prices in red and blue buttons',
    'departures': 'A station concourse with a departure board, people walking past and a bicycle',
    'phone-2': 'Three passengers on a station platform, each looking at their phone',
    'phone': 'A hand holding up a phone with a music app open, over a cafe table',
    'selfcheckout': 'A self-checkout screen beside a bin for scanning clothes, with the total shown in yen',
    'parking': 'Two parking meters on a pavement next to concrete road barriers',
    'laptop': 'A laptop on a white desk next to a lamp and stacks of books',
    'postit': 'A wall covered in pastel sticky notes written by customers',
    'map': 'A paper timetable notice taped behind scratched plastic at a bus stop',
}


def tag(t):
    return para(t, className='is-style-tag')


def facts(rows):
    return group(columns(*[(None, J(heading(k, 6), para(v, fontSize='small'))) for k, v in rows], isStackedOnMobile=False,
                         style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}),
                 className='is-style-rule-top', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})


# Signature cluster: the case study page
pattern('case-hero', 'Case study: hero with role, timeline and team', 'featured', J(
    facts([('Role', 'Lead product designer, research and UI'), ('Timeline', 'March to October 2025, 30 weeks'), ('Team', 'Me, two developers, a PM and the operator’s station staff'),
           ('Platforms', 'Ticket machines, 1080 × 1920 touchscreen'), ('Tools', 'Figma, FigJam, Maze, a lot of platform time')]),
    image('kiosk-3.jpg', IMG['kiosk-3'], 'The new flow running on a machine at Glasgow Queen Street, September 2025', align='wide', className='is-style-framed-wide')),
    description='Put this first in every case study: the facts row, then the lead image.')

pattern('stage-band', 'Stage band', 'text', group(
    row(J(para('Stage 1 of 3', fontSize='small'), heading('Research', 2, fontSize='xx-large')), justify='space-between', align='wide'),
    className='is-style-stage', align='full'), description='A black band that starts each stage of a case study. Change the stage name and number.')

pattern('case-problem', 'Case study: the problem', 'text', J(
    heading('The problem', 3),
    para('<mark>A third of people who started buying a ticket at a machine gave up before paying.</mark> The operator’s own logs showed it. Most of them then queued at the ticket office, which closes at 7pm at 22 of the 38 stations.'),
    para('The machines ask for the destination last. If your station was not in the first screen of twelve, you had to know the name of the fare zone. Nobody knows the name of the fare zone.')))

pattern('research-insights', 'Research insights', 'text', J(
    heading('What we learned on the platforms', 3),
    para('Four weeks, 11 stations, 46 short interviews and 20 hours of watching people use the machines. Station staff let us stand next to the machines in hi-vis.'),
    lst(['<strong>People start with where they are going, not with the ticket type.</strong> 41 of 46 said the destination first when we asked what they wanted.',
         '<strong>The railcard question lost the most people.</strong> It came before the price, so people could not see what a railcard would save them.',
         '<strong>Card readers were fine. Cash was the problem.</strong> Only 6% paid in cash, but those journeys took three times as long.',
         '<strong>Staff already had a workaround.</strong> They taped a list of fare zones to the side of the machine at Partick.'], ordered=True)))

pattern('before-after', 'Before and after screens', 'gallery', J(
    columns(
        (None, J(tag('Before'), image('kiosk.jpg', IMG['kiosk'], 'Fare grid first. You had to pick a price before a place.', className='is-style-framed'))),
        (None, J(tag('After'), image('kiosk-3.jpg', IMG['kiosk-3'], 'Destination first, with the map and a search box. Price comes last, railcard next to it.', className='is-style-framed'))),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
    para('What changed: the order of the questions. The visual design barely moved, because the operator’s brand rules fix the colours and the type on the machines.', fontSize='small')),
    description='Two screens side by side with a label and a caption that says what changed in words.')

pattern('results', 'Results with sources', 'text', J(
    heading('What happened', 3),
    table([['Journeys started but not paid for', '33%', '14%', 'Machine logs, 8 weeks before and after'],
           ['Median time to buy a single', '71 s', '38 s', 'Session timings, 2,400 sessions'],
           ['Ticket office queue after 5pm, Partick', '12 people', '5 people', 'Staff head counts, 20 evenings']],
          head=['Measure', 'Before', 'After', 'Source']),
    para('The operator paused the rollout at 12 stations while they replace the card readers, so the full numbers are not in yet.', fontSize='small')))

pattern('client-quote', 'Client quote', 'testimonials', quote(
    'Nadia spent more time on our platforms than some of our managers. The change looks small on a screen, and it cut the evening queues at Partick in half.',
    'Callum Ross, head of retail, Clyde Valley Rail'))

pattern('what-id-change', 'What I would do differently', 'text', group(J(
    heading('What I would do differently', 4),
    para('I tested with commuters first because they were easy to find at 8am. They were also the people who needed the machines least. Next time I start with the Saturday afternoon crowd.')),
    className='is-style-lime'))

pattern('next-case', 'Next case study', 'query', group(J(
    para('Next case study', fontSize='small'),
    query(columns(('40%', dyn('post-featured-image', isLink=True, aspectRatio='16/10', scale='cover', className='is-style-framed')),
                  (None, J(dyn('post-title', isLink=True, level=2, fontSize='xx-large'), dyn('post-excerpt', showMoreOnPage=False)))),
          per_page=1, query_id=41).replace('"offset":0', '"offset":1', 1)),
    className='is-style-rule-top', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'}), description='Shows the second-newest case study as a link to read next.')

pattern('case-study-full', 'Case study: full page', 'featured', J(
    pattern_ref('case-hero'), pattern_ref('stage-band'), pattern_ref('case-problem'), pattern_ref('research-insights'),
    group(row(J(para('Stage 2 of 3', fontSize='small'), heading('Design', 2, fontSize='xx-large')), justify='space-between', align='wide'), className='is-style-stage', align='full'),
    pattern_ref('before-after'),
    group(row(J(para('Stage 3 of 3', fontSize='small'), heading('Results', 2, fontSize='xx-large')), justify='space-between', align='wide'), className='is-style-stage', align='full'),
    pattern_ref('results'), pattern_ref('client-quote'), pattern_ref('what-id-change')),
    description='Every section of a case study in order: hero, problem, research, before and after, results, quote.')

pattern('nda-entry', 'Short NDA entry', 'text', group(J(
    row(J(tag('Under NDA'), para('2024, 5 months', fontSize='small')), justify='space-between'),
    heading('Onboarding for a Dutch pension provider', 4),
    para('Redesigned the first 15 minutes of joining a workplace pension, for 400,000 members. Details are limited by the contract, but I am happy to talk it through on a call.')),
    className='is-style-case-card'))

# The signature work list: full studies and NDA entries side by side
pattern('work-list', 'Work list: full case studies and NDA entries', 'featured', group(J(
    heading('Everything, briefly', 3),
    table([['<a href="/ticket-machines-that-ask-where-you-are-going/">Clyde Valley Rail</a><br>2025', 'Ticket machines that ask where you are going first', 'Case study'],
           ['<a href="/parking-without-the-meter/">Renfrew Council</a><br>2024', 'Paying for parking by text, app or card at the kerb', 'Case study'],
           ['Dutch pension provider<br>2024', 'Onboarding for workplace pension members', '<mark>Under NDA</mark>'],
           ['<a href="/self-checkout-for-a-clothing-chain/">Kilt &amp; Co.</a><br>2023', 'Self-checkout that handles security tags', 'Case study'],
           ['UK neobank<br>2023', 'Card freeze and dispute flow', '<mark>Under NDA</mark>'],
           ['<a href="/live-departures-on-the-platform/">Strathclyde bus partnership</a><br>2022', 'Live departures on stop displays and phones', 'Case study']],
          head=['Client and year', 'What', ''])), align='wide', layout={'type': 'constrained', 'contentSize': '1240px'}),
    description='A table of every project: full case studies link through, NDA work shows a marker and no link.')

CASE_CARD = columns(
    ('58%', dyn('post-featured-image', isLink=True, aspectRatio='16/10', scale='cover', className='is-style-framed')),
    (None, J(dyn('post-terms', term='category', className='is-style-tag'), dyn('post-title', isLink=True, level=2, fontSize='x-large'),
             dyn('post-excerpt', showMoreOnPage=False), dyn('read-more', content='Read the case study'))),
    verticalAlignment='center', className='is-style-case-card', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}})

pattern('case-cards', 'Case studies (big cards)', 'featured,query', group(J(
    row(J(heading('Case studies', 2), para('<a href="/work/">All work, including NDA projects</a>')), justify='space-between', align='wide'),
    query(CASE_CARD, per_page=3, query_id=42, align='wide', layout={'type': 'default'})),
    align='wide', layout={'type': 'default'}), keywords='case studies, work')

pattern('case-archive', 'Case studies archive (inherits the page query)', 'query', inherit_query(CASE_CARD, align='wide', layout={'type': 'default'}), inserter=False)

pattern('hero-intro', 'Hero: who I am and what I fix', 'featured', columns(
    ('55%', J(heading('I redesign the machines you queue at.', 1),
              para('Nadia Branković, product designer in Glasgow. Ticket machines, parking, self-checkout and the phone apps that sit next to them. I start on the platform, not in Figma.', fontSize='large'),
              buttons(('See the case studies', '/work/'), ('How I work with teams', '/working-together/', {'className': 'is-style-outline'})))),
    (None, image('kiosk-2.jpg', IMG['kiosk-2'], 'Ticket hall, Clyde Valley Rail, where the research started', className='is-style-framed', lightbox=False)),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}))

pattern('capacity-note', 'Capacity note', 'call-to-action', para(
    '<strong>One project at a time.</strong> Booked until January 2027. I take enquiries now for February starts.', className='is-style-lime'),
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
    lst(['<strong>Two weeks on site.</strong> I watch the service being used and talk to the people who run it.',
         '<strong>One problem statement.</strong> Written down, agreed with you, with the number we are trying to move.',
         '<strong>Prototypes in the real place.</strong> Paper first, then clickable, tested where people actually use the thing.',
         '<strong>Ship, measure, write it up.</strong> You get the case study too, and you can use it internally.'], ordered=True)),
    className='is-style-rule-top'))

pattern('what-i-dont-do', 'What I do not take on', 'text', group(J(
    heading('What I do not take on', 4),
    para('Dark patterns, gambling and payday lending. Brand identity and logos, which other people do much better. Projects where nobody on your side can talk to users.')),
    className='is-style-rule-top'))

pattern('working-together-page', 'Page: working together', 'services', J(
    pattern_ref('engagements'), spacer('var:preset|spacing|60'), pattern_ref('process'), pattern_ref('what-i-dont-do'), pattern_ref('testimonials')), block_types='core/post-content')

pattern('testimonials', 'Testimonials (named)', 'testimonials', columns(
    (None, quote('She found the railcard problem in her first week. We had been looking at the wrong screen for two years.', 'Callum Ross, head of retail, Clyde Valley Rail, 2025')),
    (None, quote('Nadia is the only designer who asked to see our complaint letters. Half the redesign came out of that folder.', 'Aoife Byrne, parking services manager, Renfrew Council, 2024')),
    align='wide'))

pattern('about-bio', 'About: bio', 'about', columns(
    ('40%', image('departures.jpg', IMG['departures'], 'Where I do most of my research: a station concourse at 5.40pm', className='is-style-framed')),
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

pattern('about-page', 'Page: about', 'about', J(pattern_ref('about-bio'), spacer('var:preset|spacing|60'), pattern_ref('cv'), pattern_ref('talks')), block_types='core/post-content')

pattern('talks', 'Talks and writing', 'about', group(J(
    heading('Talks and writing', 4),
    lst(['<a href="https://example.com/">The order of questions</a>, UX Scotland, Edinburgh, June 2024',
         '<a href="https://example.com/">Research on a platform in the rain</a>, Service Design in Government, 2023',
         '<a href="https://example.com/">Why nobody knows their fare zone</a>, essay, 2022'])), className='is-style-rule-top'))

pattern('contact-page', 'Page: contact', 'contact', J(
    columns((None, J(heading('Tell me what is broken', 2, fontSize='x-large'),
                     para('Email <a href="mailto:nadia@example.com">nadia@example.com</a> with the service, who uses it and what you have tried. A number helps, even a rough one.'),
                     para('I reply within two working days. If I am not the right person, I will say so and suggest someone.'))),
            (None, J(pattern_ref('capacity-note'),
                     table([['Email', '<a href="mailto:nadia@example.com">nadia@example.com</a>'], ['Phone', '07700 900 418, weekdays 9 to 5'], ['Office', 'The Whisky Bond, 2 Dawson Road, Glasgow G4 9SS'], ['Days in', 'Tuesdays, and by arrangement']]))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})), block_types='core/post-content')

pattern('newsletter', 'Newsletter', 'call-to-action', group(J(
    heading('Notes from the platform', 3),
    para('One email every six weeks: what I saw people struggle with, and what we changed. About 900 designers and product managers read it.'),
    buttons(('Subscribe by email', 'mailto:nadia@example.com?subject=Subscribe'))), className='is-style-ink', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('screens-caption', 'Screenshot with a text description', 'gallery', J(
    image('selfcheckout.jpg', IMG['selfcheckout'], 'Scan screen with the tag-removal step moved above the total', align='wide', className='is-style-framed'),
    para('<strong>What changed:</strong> the security tag step used to appear after payment, so people paid, then waited for staff. It now comes first, while the bag is still open.', fontSize='small')))

pattern('post-list', 'Search results list', 'query', inherit_query(
    group(J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30)), className='is-style-rule-top'), align='wide'), inserter=False)

# ---------------------------------------------------------------- templates
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('hero-intro'), pattern_ref('case-cards'), pattern_ref('work-list'), pattern_ref('testimonials')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|70'}}),
    template_part('footer', 'footer')))

write('templates/home.html', page_template(J(
    heading('Work', 1, align='wide'),
    para('Case studies I can publish, and short entries for the ones I cannot.', align='wide', fontSize='large'),
    pattern_ref('case-archive'), spacer('var:preset|spacing|60'), pattern_ref('work-list')),
    layout={'type': 'constrained'}, style=dict(MAINPAD, **{'spacing': {'blockGap': 'var:preset|spacing|50', 'padding': MAINPAD['spacing']['padding']}})))
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
    pattern_ref('next-case')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|50', 'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}),
    template_part('footer', 'footer')))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1),
    dyn('post-content', layout={'type': 'constrained'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1, align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})), layout={'type': 'constrained'}, style=MAINPAD))

print('case built')
