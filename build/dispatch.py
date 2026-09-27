# Design note (dispatch, idea 052: independent journalist / paid newsletter)
# Direction: "live wire". Owner's brief: cutting-edge news, sharper. A black-on-white news page with a huge condensed nameplate,
# a timestamped wire beside the lead story, hairline rules instead of boxes, and one acid highlight that marks what is members-only.
# Why: reader-funded newsrooms (404 Media, Aftermath) win on speed, clarity and showing their numbers; the design should feel like it was filed an hour ago.
# Fonts: Mona Sans (variable width; condensed 900 for headlines and the nameplate, normal width for labels); Newsreader for the reading column.
# Palette: paper white, near-black, signal red for links and breaking labels, acid lime for the members marker and the goals bar. No cards, no radius.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('dispatch')
import blocks as _b
def group(inner, tag='div', layout='constrained', **attrs):
    # WordPress drops the layout of a <div> group that has align + padding when it re-serialises; <section> keeps it.
    if tag == 'div' and 'padding' in json.dumps(attrs.get('style', {})):
        tag = 'section'
    return _b.group(inner, tag=tag, layout=layout, **attrs)
D = THEME['dir']
import re as _re
def split_css(css):
    """Block and section 'css' only scopes the first selector of a comma list, so write one rule per selector."""
    out = []
    for sel, body in _re.findall(r'([^{}]+)\{([^{}]*)\}', css):
        parts = [p.strip() for p in _re.split(r',(?![^()]*\))', sel)]
        out += ['%s{%s}' % (p, body) for p in parts if p]
    return ''.join(out)


PALETTE = [
    ('base', '#FAFAF7', 'Paper'), ('contrast', '#0B0B0B', 'Ink'), ('accent', '#C4201A', 'Signal red'),
    ('accent-2', '#D4FF3A', 'Acid'), ('surface', '#EEEEEA', 'Grey paper'), ('line', '#0B0B0B', 'Rule'),
    ('muted', '#56564F', 'Grey'), ('hairline', '#C9C9C2', 'Hairline'), ('on-acid', '#0B0B0B', 'Text on acid'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
disp = next(f for f in fonts if f['slug'] == 'display')
body = next(f for f in fonts if f['slug'] == 'body')

def pal(p):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in p]

def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d

focus = {'outline': {'color': 'var:preset|color|accent', 'offset': '2px', 'style': 'solid', 'width': '3px'}}
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '660px', 'wideSize': '1360px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': [disp, body],
            'fontSizes': [fs('x-small', '0.8125rem', 'Caption'), fs('small', '0.9375rem', 'Small'), fs('medium', '1.1875rem', 'Body'),
                          fs('large', '1.5rem', 'Large', '1.25rem'), fs('x-large', '2.5rem', 'Section', '1.8rem'),
                          fs('xx-large', '4.75rem', 'Headline', '2.6rem'), fs('display', '11rem', 'Nameplate', '4rem')],
        },
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 7rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '850', 'lineHeight': '0.94', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.02'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.15', 'fontWeight': '750'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '750'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700', 'letterSpacing': '0'}},
            'button': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                       'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                       'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '750', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.65em', 'bottom': '0.65em', 'left': '1.1em', 'right': '1.1em'}},
                       ':hover': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|on-acid'}, 'border': {'color': 'var:preset|color|accent-2'}}, ':focus': focus},
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '900', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.02em', 'lineHeight': '0.85'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '650'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/heading': {'elements': {'link': {'color': {'text': 'currentColor'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.45'}},
            'core/post-author-name': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.15'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '4px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|30'}},
                           'css': '& cite{font-weight:500;font-size:var(--wp--preset--font-size--x-small);font-style:normal}'},
            'core/details': {'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-weight:750;cursor:pointer}'},
            'core/table': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small'},
                           'css': '& table.has-fixed-layout{table-layout:auto}& table th{text-align:left;font-weight:800}& table td,& table th{border:0;border-bottom:1px solid var(--wp--preset--color--hairline);padding:.6em 1em .6em 0;vertical-align:top}& table thead{border:0;border-bottom:3px solid var(--wp--preset--color--line)}'},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
        },
        'css': ('.wp-block-column>.wp-block-group:only-child{height:100%}:where(h1,h2,h3,.wp-block-site-title,.has-display-font-size,.has-display-font-family.has-xx-large-font-size){font-stretch:75%;text-wrap:balance}:where(p,li){text-wrap:pretty}'
                'body{font-synthesis:none;font-variant-numeric:lining-nums tabular-nums}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:2px}'
                ':where(.wp-block-post-content)>:where(h2,h3){margin-top:var(--wp--preset--spacing--50)}'
                '.wp-block-table td,.wp-block-table th{overflow-wrap:normal;word-break:normal}'
                '::selection{background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--on-acid)}'),
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header (nameplate)'}, {'area': 'header', 'name': 'header-compact', 'title': 'Header (compact, for articles)'},
                      {'area': 'footer', 'name': 'footer', 'title': 'Footer'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
                        {'name': 'single-members', 'title': 'Members-only story', 'postTypes': ['post']}],
}
_t = theme['styles']['blocks'].get('core/table', {}).pop('css', None)
if _t:
    # Block-level css loses to core's table borders, so the table rules go in the global stylesheet.
    theme['styles']['css'] += _t.replace('& ', '.wp-block-table ').replace('&.', '.wp-block-table.')
for _b_ in theme['styles']['blocks'].values():
    if 'css' in _b_:
        _b_['css'] = split_css(_b_['css'])
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

def variation(title, p):
    return json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(p)}}}, indent='\t', ensure_ascii=False)

write('styles/wire-blue.json', variation('Wire blue', [
    ('base', '#FFFFFF', 'Paper'), ('contrast', '#0E1116', 'Ink'), ('accent', '#0A5C8A', 'Signal red'),
    ('accent-2', '#FFE14D', 'Acid'), ('surface', '#EEF1F4', 'Grey paper'), ('line', '#0E1116', 'Rule'),
    ('muted', '#4F5661', 'Grey'), ('hairline', '#C7CDD5', 'Hairline'), ('on-acid', '#0B0B0B', 'Text on acid')]))
write('styles/telex.json', variation('Telex', [
    ('base', '#F3E6A6', 'Paper'), ('contrast', '#161308', 'Ink'), ('accent', '#9B1D12', 'Signal red'),
    ('accent-2', '#FFFFFF', 'Acid'), ('surface', '#EADB90', 'Grey paper'), ('line', '#161308', 'Rule'),
    ('muted', '#4E4518', 'Grey'), ('hairline', '#BFAE5E', 'Hairline'), ('on-acid', '#0B0B0B', 'Text on acid')]))
write('styles/night-desk.json', variation('Night desk', [
    ('base', '#0B0B0B', 'Paper'), ('contrast', '#F2F2EC', 'Ink'), ('accent', '#FF5A4E', 'Signal red'),
    ('accent-2', '#D4FF3A', 'Acid'), ('surface', '#18181A', 'Grey paper'), ('line', '#F2F2EC', 'Rule'),
    ('muted', '#A9A9A0', 'Grey'), ('hairline', '#34342F', 'Hairline'), ('on-acid', '#0B0B0B', 'Text on acid')]))

def section(slug, title, types, styles):
    if 'css' in styles:
        styles = dict(styles, css=split_css(styles['css']))
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                                        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))

section('inverse', 'Inverse', ['core/group', 'core/columns'],
        {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
         'elements': {'link': {'color': {'text': 'var:preset|color|accent-2'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                      'button': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|on-acid'}, 'border': {'color': 'var:preset|color|accent-2'}}},
         'css': '& .wp-block-post-title a{color:inherit}& table td,& table th{border-bottom-color:currentColor}'})
section('acid', 'Acid highlight', ['core/group', 'core/paragraph'],
        {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|on-acid'},
         'elements': {'link': {'color': {'text': 'var:preset|color|on-acid'}}, 'heading': {'color': {'text': 'var:preset|color|on-acid'}},
                      'button': {'color': {'background': 'var:preset|color|on-acid', 'text': 'var:preset|color|accent-2'}, 'border': {'color': 'var:preset|color|on-acid'}}}})
section('members-tag', 'Members tag', ['core/post-terms', 'core/paragraph'],
        {'css': '& a,&:not(.wp-block-post-terms){background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--on-acid)!important;text-decoration:none;padding:.05em .35em;font-family:var(--wp--preset--font-family--display);font-weight:800}'})
section('rule-top', 'Rule above (heavy)', ['core/group', 'core/columns', 'core/column'],
        {'border': {'top': {'color': 'var:preset|color|line', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('acid-top', 'Acid rule above', ['core/group', 'core/column'],
        {'border': {'top': {'color': 'var:preset|color|accent-2', 'width': '8px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('rule-bottom', 'Rule below (heavy)', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '3px', 'style': 'solid'}}})
section('hairline-top', 'Hairline above', ['core/group'],
        {'border': {'top': {'color': 'var:preset|color|hairline', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}})
section('wire', 'Wire list', ['core/post-template'],
        {'css': '& > li{border-bottom:1px solid var(--wp--preset--color--hairline);padding:.7rem 0;margin:0!important}'})
section('members-break', 'Members-only break', ['core/group'],
        {'border': {'top': {'color': 'var:preset|color|line', 'width': '3px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40'}}})
section('dateline', 'Dateline', ['core/paragraph'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|small'}})
section('photo', 'News photo (ruled, 3:2)', ['core/image', 'core/post-featured-image', 'core/gallery'],
        {'css': '& img{aspect-ratio:3/2;object-fit:cover;width:100%;border-bottom:1px solid var(--wp--preset--color--line)}'})

# ---------------------------------------------------------------- helpers
def members_tag():
    return para('Members', className='is-style-members-tag', fontSize='x-small')

def label(t, **kw):
    return para(t, fontFamily='display', fontSize='x-small', style={'typography': {'fontWeight': '800'}}, **kw)

def goal_rows(rows):
    return J(*[group(columns(('18%', para(a, fontSize='x-large', fontFamily='display', style={'typography': {'fontWeight': '900', 'lineHeight': '1'}})),
                             ('58%', para(b)), ('24%', para(c, fontSize='small', fontFamily='display', style={'typography': {'fontWeight': '700'}})),
                             isStackedOnMobile=False, style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}),
                     className='is-style-hairline-top', align='wide', layout={'type': 'default'}) for a, b, c in rows])

TIERS = [['Free', '€0', 'The Friday briefing by email, about half the stories, the corrections log'],
         ['Member', '€8 a month or €80 a year', 'Every story, full-text RSS, comments, the ad-free podcast a day early, the document archive'],
         ['Founding member', '€20 a month or €200 a year', 'All of that, a quarterly call where I take questions on the next investigation, your name on the masthead page']]

# ---------------------------------------------------------------- patterns
WIRE_ITEM = group(J(
    row(J(dyn('post-date', format='D j M'), dyn('post-terms', term='post_tag', className='is-style-members-tag')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}),
    dyn('post-title', isLink=True, level=4, fontSize='medium')), layout={'type': 'default'}, style={'spacing': {'blockGap': 'var:preset|spacing|10'}})

pattern('lead-and-wire', 'Lead story with the wire beside it', 'featured,posts', columns(
    ('68%', J(
        row(J(para('Investigation', className='is-style-dateline', textColor='accent'), members_tag()), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}),
        heading('<a href="/ad-exchange-hospital-location-data/">An ad exchange sold location data from 41 hospitals</a>', 1, fontSize='xx-large'),
        para('Bid requests from a Dutch exchange carried the precise location of phones inside cancer wards and fertility clinics. Three data brokers bought the stream. Two of them sell to insurers.', fontSize='large'),
        row(J(para('By Lena Varga', fontSize='small', fontFamily='display', style={'typography': {'fontWeight': '800'}}),
              para('Brussels, 24 September 2026, 07:10', fontSize='small', fontFamily='display'),
              para('14 min read', fontSize='small', fontFamily='display', textColor='muted')), style={'spacing': {'blockGap': 'var:preset|spacing|30'}}),
        image('phones.jpg', 'A phone, an open notebook, a pencil and glasses on a white desk', caption='The test phone we used for six weeks, running eleven free apps. Photo: stand-in, CC0.', className='is-style-photo'))),
    ('32%', group(J(row(J(heading('The wire', 2, fontSize='large'), para('<a href="/latest/">All</a>', fontSize='small')), justify='space-between'),
              query(WIRE_ITEM, per_page=7, template_class='is-style-wire')), className='is-style-rule-top', layout={'type': 'default'})),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    description='The home page opener: the lead story on the left, a timestamped wire of everything else on the right.')

pattern('nameplate', 'Nameplate (masthead)', 'header', group(J(
    row(J(para('Independent reporting on data brokers, ad tech and the people they track. By Lena Varga, from Brussels.', fontSize='small', fontFamily='display', style={'typography': {'fontWeight': '600'}}),
          buttons(('Become a member', '/membership/'), ('Sign in', '/signup/', {'className': 'is-style-outline'}))), justify='space-between'),
    dyn('site-title', level=0, fontSize='display', style={'typography': {'lineHeight': '0.8', 'letterSpacing': '-0.035em'}}),
    dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'left'}, className='is-style-rule-top')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'blockGap': 'var:preset|spacing|20'}}), inserter=False)

pattern('membership-tiers', 'Membership tiers (ruled comparison)', 'call-to-action,services', J(
    heading('Three ways to read', 2),
    para('Readout has no ads and no investors. About 2,400 people pay for it, and that is the whole budget.', fontSize='large'),
    pattern_ref('tier-columns'),
    buttons(('Give a year as a gift', '/membership/#gift', {'className': 'is-style-outline'})),
    para('Students, unemployed readers and anyone in a country where €8 is a lot: email me and I will set you up for €2. No questions.', fontSize='small')),
    description='The signature: every tier with its monthly and yearly price and concrete perks, as a ruled table.')

pattern('what-you-get', 'What members get', 'text', J(
    heading('What members get', 3),
    lst(['Every story in full, including the investigations, usually 2 to 3 a month.', 'Full-text RSS, so you can read in your own reader.',
         'Comments, which I read and sometimes answer in the next story.', 'The podcast without ads, a day before everyone else.',
         'The document archive: every contract, filing and FOI response I cite, as PDFs.'])))

pattern('members-break', 'Members-only break inside a story', 'call-to-action', group(J(
    row(J(members_tag(), label('The rest of this story is for members')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}),
    para('Members read the full investigation, including the list of 41 hospitals and the brokers’ replies. From €8 a month, or €2 if that is too much.'),
    buttons(('Become a member', '/signup/'), ('I’m already a member', '/signup/', {'className': 'is-style-outline'})))),
    description='Put this where the free preview ends. Jetpack Paid Content or your membership plugin hides what comes after it.')

pattern('corrections-note', 'Corrections line at the foot of a story', 'text', group(para(
    '<strong>Correction, 25 September 2026, 16:40.</strong> An earlier version said the Dutch data protection authority fined the exchange €1.2m in 2023. The fine was €525,000. We regret the error.', fontSize='small'),
    className='is-style-hairline-top'), description='Dated, specific, and at the foot of the story it corrects.')

pattern('byline-dateline', 'Byline and dateline', 'text', row(J(
    para('By Lena Varga', fontSize='small', fontFamily='display', style={'typography': {'fontWeight': '800'}}),
    para('Brussels, 24 September 2026, 07:10', fontSize='small', fontFamily='display'),
    para('Updated 25 September, 16:40', fontSize='small', fontFamily='display', textColor='muted')), style={'spacing': {'blockGap': 'var:preset|spacing|30'}}))

pattern('signup-box', 'Sign-up box (one per page)', 'call-to-action', group(J(
    heading('Get the Friday briefing', 3),
    para('One email on Friday mornings: what I published, what I’m chasing and one document worth reading. Free. About 1,200 words.'),
    buttons(('Sign up with your email', '/signup/'))), className='is-style-acid',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('goals', 'Subscriber goals (public)', 'text', group(J(
    columns(('38%', J(heading('Where the money goes', 2), para('I publish the numbers every quarter. Last updated 1 September 2026.', fontSize='small'))),
            ('62%', J(
                para('2,412 paying members', fontSize='xx-large', fontFamily='display', style={'typography': {'fontWeight': '900', 'lineHeight': '0.95'}}),
                row(group(para('&nbsp;', fontSize='x-small'), className='is-style-acid', style={'layout': {'selfStretch': 'fixed', 'flexSize': '80%'}}), wrap=False,
                    style={'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|base'}}),
                para('80% of the way to 3,000, which pays for a part-time researcher.', fontSize='small'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    goal_rows([('2,000', 'Pays me a full-time salary, legal insurance and hosting', 'Reached, March 2026'),
               ('3,000', 'A researcher, three days a week. Daan has already said yes', '2,412 now'),
               ('4,500', 'A lawyer reads every investigation before it runs', 'Next'),
               ('6,000', 'A second reporter, covering the Baltic states', 'Later')])),
    align='full', className='is-style-inverse',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'margin': {'top': '0'}}}),
    description='A public goals block: how many readers pay, what each milestone pays for, and where things stand.')

pattern('group-subscriptions', 'Group and institutional subscriptions', 'services', group(J(
    heading('For libraries, newsrooms and universities', 3),
    para('Ten seats for €600 a year, or unlimited access by IP range for €1,400. Invoices in euros with a VAT number. Most university libraries pay by bank transfer and that is fine.'),
    para('<a href="mailto:groups@readout.example">groups@readout.example</a>')), anchor='groups', layout={'type': 'default'}))

pattern('gift', 'Gift a membership', 'call-to-action', group(J(
    heading('Give a year', 3),
    para('€80 for a year of Readout. You pick the start date and I send the recipient a short note from me on that morning. It does not renew.'),
    buttons(('Give a year', '/signup/'))), anchor='gift'))

pattern('podcast-feed', 'Members’ podcast feed', 'text', J(
    heading('The podcast', 3),
    para('Twenty minutes every other Wednesday: me and one source, usually someone who used to work at the companies I write about. Free with ads, or ad-free and a day early for members through a private feed.')))

pattern('archive-by-year', 'Archive by year', 'text', J(
    heading('Archive', 2),
    goal_rows([('2026', '41 stories. Hospital location data, border drone contracts, transit cards.', '<a href="/latest/">Read them</a>'),
               ('2025', '58 stories. The AI Act lobby register, the ad tech consent fines.', '<a href="/latest/">Read them</a>'),
               ('2024', '22 stories. The first year, from May.', '<a href="/latest/">Read them</a>')])))

pattern('tips', 'Send a tip, safely', 'contact', J(
    heading('Send me something', 2),
    para('If you work at an ad tech company, a data broker or a public body that buys from one, I would like to hear from you. I protect sources. I have never named one without their permission.'),
    lst(['Signal: +32 470 12 34 56 (use a phone that isn’t your work phone).', 'Proton Mail: lena.varga@proton.example', 'Post: Readout, Rue de la Loi 155, box 12, 1040 Brussels. No return address needed.']),
    para('Don’t use a work device or a work network, even for reading this page.', fontSize='small')))

pattern('about-bio', 'About the reporter', 'about', columns(
    ('36%', image('berlaymont.jpg', 'The curved glass front of the Berlaymont building in Brussels with a row of EU flags', caption='The Berlaymont, where most of my freedom-of-information requests end up.', className='is-style-photo')),
    ('64%', J(
        para('I’m Lena Varga. I covered EU tech policy for eight years at a Brussels trade publication, until it was bought by a lobbying firm in 2024. I left the week after and started Readout in May.'),
        para('I report on the companies that buy and sell information about where people are and what they do, and on the officials who are supposed to regulate them. I read the filings so you don’t have to, and I publish them so you can check.'),
        para('Readout does not take advertising, sponsorship or money from foundations funded by tech companies. It is paid for by readers. I don’t do paid speaking for industry events.'),
        para('Hungarian by birth, Belgian by paperwork. I live in Saint-Gilles.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('investigations-grid', 'Investigations (text grid)', 'posts,query', group(J(
    row(J(heading('Investigations', 2), para('<a href="/category/investigations/">All investigations</a>', fontSize='small')), justify='space-between', className='is-style-rule-top'),
    query(group(J(dyn('post-featured-image', isLink=True, className='is-style-photo'), dyn('post-date', format='j F Y'),
                  dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=22)), layout={'type': 'default'}),
          per_page=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}))

pattern('latest-list-archive', 'Latest (inherits the page query)', 'posts,query', inherit_query(group(columns(
    ('18%', J(dyn('post-date', format='j M Y, H:i'), dyn('post-terms', term='category'))),
    ('82%', J(dyn('post-title', isLink=True, level=2, fontSize='x-large'), dyn('post-excerpt', excerptLength=34), dyn('post-terms', term='post_tag', className='is-style-members-tag'))),
    style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}), className='is-style-hairline-top', layout={'type': 'default'}), align='wide'), inserter=False)

pattern('membership-page', 'Page: membership', 'call-to-action', J(pattern_ref('membership-tiers'), pattern_ref('what-you-get'), pattern_ref('gift'), pattern_ref('group-subscriptions'), pattern_ref('membership-faq')),
        block_types='core/post-content')
pattern('signup-page', 'Page: sign up', 'call-to-action', J(
    para('Enter your email on the next screen and pick Free or a paid tier. Card payments go through Stripe. You can cancel from any email footer in two clicks.', fontSize='large'),
    pattern_ref('tier-columns'), pattern_ref('newsletter-archive'),
    pattern_ref('signup-box')), block_types='core/post-content')
pattern('goals-page', 'Page: subscriber goals', 'text', J(
    para('Every quarter I publish how many people pay for Readout and what the money is for. This is the September 2026 update.', fontSize='large'),
    pattern_ref('goals'),
    heading('Costs, per month', 3),
    table([['My salary, before tax', '€3,900'], ['Legal insurance', '€310'], ['Newsletter and site hosting', '€240'], ['FOI fees and document costs', '€90, on average'], ['Accountant', '€150']], head=['Item', 'Cost'])),
    block_types='core/post-content')
pattern('about-page', 'Page: about', 'about', J(pattern_ref('about-bio'), pattern_ref('funding'), pattern_ref('archive-by-year'), pattern_ref('byline-dateline')), block_types='core/post-content')
pattern('tips-page', 'Page: tips', 'contact', J(pattern_ref('tips'), pattern_ref('republish')), block_types='core/post-content')
pattern('corrections-page', 'Page: corrections', 'text', J(pattern_ref('corrections-policy'), pattern_ref('corrections-note'),
    para('Every correction since Readout started, newest first. Each one is also at the foot of the story it corrects.', fontSize='large'),
    table([['25 Sep 2026', '<a href="/ad-exchange-hospital-location-data/">Hospital location data</a>', 'Fine amount was €525,000, not €1.2m.'],
           ['2 Jul 2026', '<a href="/transit-cards-location-history/">Transit cards</a>', 'STIB keeps tap records for 12 months, not 18.'],
           ['14 Nov 2025', 'The AI Act lobby register', 'A meeting we dated 3 October was on 13 October.']], head=['Date', 'Story', 'What was wrong'])),
    block_types='core/post-content')

pattern('front-page-layout', 'Home: lead, wire, goals, investigations, membership', 'featured', J(
    pattern_ref('breaking-bar'), pattern_ref('lead-and-wire'), pattern_ref('goals'), pattern_ref('investigations-grid'),
    columns(('40%', pattern_ref('top-stories')), ('30%', pattern_ref('behind-the-story')), ('30%', pattern_ref('podcast-episode')), align='wide',
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}, 'padding': {'bottom': 'var:preset|spacing|60'}}}),
    group(J(heading('Membership', 2), para('Readout has no advertising and no investors. About 2,400 people pay for Readout, and that is the whole budget.', fontSize='large'), pattern_ref('tier-columns')),
          align='wide', className='is-style-rule-top', layout={'type': 'default'}, style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}),
    columns(('50%', pattern_ref('signup-box')), ('50%', pattern_ref('tips')), align='wide',
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'padding': {'bottom': 'var:preset|spacing|70'}}})), inserter=False)

# ---------------------------------------------------------------- round 2: the rest of the kit
def tier(name, price, year, perks, cta, url, acid=False):
    return group(J(
        para(name, fontFamily='display', fontSize='large', style={'typography': {'fontWeight': '800'}}),
        para(price, fontFamily='display', fontSize='xx-large', style={'typography': {'fontWeight': '900', 'lineHeight': '0.9'}}),
        para(year, fontSize='small', textColor='muted'),
        lst(perks),
        buttons((cta, url, {} if acid else {'className': 'is-style-outline'}))),
        className='is-style-acid-top' if acid else 'is-style-rule-top', layout={'type': 'default'})

pattern('tier-columns', 'Membership tiers (three columns)', 'call-to-action,services', columns(
    (None, tier('Free', '€0', 'Always', ['The Friday briefing by email', 'About half the stories', 'The corrections log'], 'Get the briefing', '/signup/')),
    (None, tier('Member', '€8', 'a month, or €80 a year', ['Every story, including investigations', 'Full-text RSS and comments', 'The podcast without ads, a day early', 'The document archive'], 'Become a member', '/signup/', acid=True)),
    (None, tier('Founding member', '€20', 'a month, or €200 a year', ['Everything members get', 'A quarterly call about the next investigation', 'Your name on the masthead page'], 'Become a founding member', '/signup/')),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
    description='The signature tiers as three ruled columns: monthly and yearly price, concrete perks, one button each.')

pattern('breaking-bar', 'Developing story bar', 'banner', group(row(J(
    para('Developing', fontFamily='display', fontSize='small', style={'typography': {'fontWeight': '900'}}),
    para('Parliament votes on the data broker amendments at 12:00 Brussels time. <a href="/live/">Follow the live notes</a>', fontSize='small')),
    style={'spacing': {'blockGap': 'var:preset|spacing|30'}}, align='wide'), align='full', className='is-style-acid',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='A one-line bar for a developing story. Remove it when the story settles.')

pattern('podcast-bar', 'Podcast announcement bar', 'banner', group(
    para('New episode: <a href="/podcast/">the man who built the hospital geofences</a>, 24 minutes. Members hear it without ads.', fontSize='small', fontFamily='display', style={'typography': {'fontWeight': '600'}}),
    align='full', className='is-style-inverse', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}))

def update(t, text):
    return group(columns(('16%', para(t, fontFamily='display', fontSize='large', style={'typography': {'fontWeight': '900'}})), ('84%', para(text)),
                         isStackedOnMobile=False, style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}), className='is-style-hairline-top', layout={'type': 'default'})

pattern('live-updates', 'Live updates (timestamped)', 'text', J(
    heading('Live notes', 2),
    update('12:41', 'Passed, 402 to 188. Amendment 14, which would have exempted “anonymised” location data, fell by nine votes.'),
    update('12:20', 'The EPP asked for a split vote on amendment 14. That is the one the brokers lobbied hardest on: 31 meetings since January.'),
    update('11:55', 'In the hemicycle. The vote is the fourth item on the list, so expect it around 12:20.'),
    update('09:10', 'Background: <a href="/parliament-lobby-register/">who lobbied on this, meeting by meeting</a>.')),
    description='Newest first. One row per update, with the time on the left.')

pattern('key-findings', 'What we found (numbered)', 'text', group(J(
    heading('What we found', 3),
    lst(['1,904 ad requests from a test phone carried a location precise to about four metres.',
         '41 hospitals in the Netherlands and Belgium appear in that data, including eleven requests from one oncology ward.',
         'Three data brokers bought the stream. Two of them sell audience segments to insurers.',
         'None of the apps involved mention hospitals in their privacy policies.'], ordered=True)),
    className='is-style-rule-top', layout={'type': 'default'}), description='The findings of an investigation, as a real ordered list.')

pattern('document', 'Document shown flat, with source', 'media,text', J(
    image('laptop.jpg', 'A laptop open on a bed in a dark room, its screen showing an email inbox', caption='Page 3 of the exchange’s bid-request specification, obtained by Readout. Stand-in photo.', className='is-style-photo'),
    para('<a href="/documents/">Read the full document (PDF, 14 pages)</a>. Members can download every file cited in this story.', fontSize='small')),
    description='A document or screenshot shown flat with a rule and a caption, and a link to the full file.')

pattern('methodology', 'How we did this', 'text', group(J(
    heading('How we did this', 3),
    para('We bought a mid-range Android phone, installed eleven of the most downloaded free apps in the Netherlands and ran them for six weeks. All traffic went through a proxy we control. We matched coordinates to hospital footprints from OpenStreetMap and checked each match by hand.'),
    para('The code and the anonymised request logs are in the <a href="/documents/">document archive</a>. The phone never left Brussels; the hospital locations were set with a location spoofing app.', fontSize='small')),
    className='is-style-rule-top', layout={'type': 'default'}))

pattern('series-nav', 'Series navigation', 'text', group(J(
    label('The location brokers, a series'),
    lst(['<a href="/ad-exchange-hospital-location-data/">Part 1: an ad exchange sold location data from 41 hospitals</a>',
         '<a href="/transit-cards-location-history/">Part 2: your transit card is a location history</a>',
         'Part 3: the insurers, coming in October'], ordered=True)),
    className='is-style-hairline-top', layout={'type': 'default'}))

pattern('pull-figure', 'One number, with context', 'text', group(J(
    para('€525,000', fontFamily='display', fontSize='xx-large', style={'typography': {'fontWeight': '900', 'lineHeight': '0.9'}}),
    para('The fine the Dutch regulator gave the exchange in 2023. Its revenue that year was €41m.', fontSize='large')),
    className='is-style-rule-top', layout={'type': 'default'}), description='A single figure that carries the story, with the sentence that explains it.')

pattern('editors-note', 'Note at the top of a story', 'text', group(para(
    '<strong>Note.</strong> This story names two data brokers and describes their products. It does not name any patient, and we destroyed the raw location data after the analysis.', fontSize='small'),
    className='is-style-acid', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}}}))

pattern('read-next', 'Read next', 'posts,query', group(J(
    heading('Read next', 3),
    query(group(J(dyn('post-date', format='j M'), dyn('post-title', isLink=True, level=4, fontSize='medium')), layout={'type': 'default'}),
          per_page=3, query_id=3, layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '12rem'})),
    className='is-style-rule-top', align='wide', layout={'type': 'default'}))

pattern('top-stories', 'Top stories, text only', 'posts,query', group(J(
    heading('Most read this week', 3),
    query(group(J(dyn('post-title', isLink=True, level=4, fontSize='large'), dyn('post-date', format='j M')), className='is-style-hairline-top', layout={'type': 'default'}),
          per_page=4, query_id=4)), layout={'type': 'default'}))

pattern('behind-the-story', 'Behind the story (weekly column)', 'text', group(J(
    label('Behind the story, for members'),
    heading('Why I didn’t name the exchange yet', 3),
    para('Every Friday I write about how the week’s reporting went, including the bits that went wrong. This week: a lawyer’s letter, a second phone, and why I waited.'),
    para('<a href="/latest/">Read this week’s note</a>', fontSize='small')), className='is-style-rule-top', layout={'type': 'default'}))

pattern('podcast-episode', 'Podcast episode', 'media,audio', group(J(
    label('The Readout podcast, episode 31'),
    heading('The man who built the hospital geofences', 3),
    para('A former ad tech engineer explains, in his own words, how a geofence around a hospital gets drawn and who buys it. 24 minutes.'),
    audio('https://upload.wikimedia.org/wikipedia/commons/1/15/The_ENIAC_Programmers_%28As_Told_By_U.S._Chief_Technology_Officer_Megan_Smith%29.ogg',
          'Stand-in audio: public-domain recording from Wikimedia Commons. Replace with your episode file.'),
    para('Free with ads in any app. Members get the private feed without ads, a day early.', fontSize='small')), className='is-style-rule-top', layout={'type': 'default'}))

pattern('newsletter-archive', 'Past Friday briefings', 'posts,text', J(
    heading('Recent briefings', 3),
    goal_rows([('25 Sep', 'Hospitals, a lawyer’s letter and one very long procurement file', '<a href="/latest/">Read</a>'),
               ('18 Sep', 'The drone contract, and what the agency sent back', '<a href="/latest/">Read</a>'),
               ('11 Sep', 'Twenty-three questions from the Commission', '<a href="/latest/">Read</a>')])))

pattern('membership-faq', 'Membership questions', 'text', J(
    heading('Questions', 2),
    details('Can I cancel?', para('Yes, from the link at the foot of any email, in two clicks. You keep access until the end of the period you paid for.')),
    details('Do you offer refunds?', para('If you forgot to cancel a yearly renewal, email me within 14 days and I will refund it.')),
    details('How does full-text RSS work?', para('Members get a private feed address on their account page. Paste it into any reader. Please don’t share it; it is tied to your account.')),
    details('Is there a student price?', para('€2 a month for students and anyone else who needs it. Email me, no proof needed.')),
    details('Can my company pay?', para('Yes. <a href="/membership/#groups">Group subscriptions</a> come with an invoice and a VAT number.'))))

pattern('masthead-names', 'Masthead and founding members', 'about,team', J(
    heading('Masthead', 2),
    goal_rows([('Lena Varga', 'Reporter, editor and publisher', 'Brussels'), ('Daan Mertens', 'Researcher, from October if we reach 3,000', 'Ghent'),
               ('Sofie Claes', 'Copy editor, freelance, two days a month', 'Antwerp')]),
    heading('Founding members', 3),
    para('Ana Popescu, Bram de Wit, Chiara Lombardi, Dmitri Volkov, Elif Kaya, Fenna Bakker, Grzegorz Nowicki, Hannah Richter, Ines Moreau, Jonas Lindqvist, Karim Haddad, Laura Sánchez, Mikkel Holm, Nora Fischer, Oisín Byrne, and 211 others who asked not to be listed.', fontSize='small')))

pattern('funding', 'Who pays for this', 'about,text', group(J(
    heading('Who pays for this', 3),
    para('Readers. In the last quarter 94% of income came from memberships and 6% from institutional subscriptions. Readout does not take advertising, sponsorship or grants from foundations funded by technology companies. If that ever changes, it will be on this page first.')),
    className='is-style-rule-top', layout={'type': 'default'}))

pattern('republish', 'Republishing policy', 'text', J(
    heading('Republishing', 3),
    para('Free stories can be republished in full by non-profit newsrooms, with a credit and a link. Members-only stories can be quoted up to 150 words. Commercial outlets, please email first.')))

pattern('photo-pair', 'Two photos side by side', 'media,gallery', gallery([
    ('parliament.jpg', 'The European Parliament hemicycle in Brussels, seen from the public gallery', 'The hemicycle before the vote.'),
    ('mast.jpg', 'A phone mast on a steel pole beside a fenced building site under a blue sky', 'The “temporary” mast in Mechelen.')], columns=2, align='wide', className='is-style-photo'))

pattern('documents-archive', 'Document archive list', 'text', J(
    heading('Document archive', 2),
    para('Every contract, filing and access-to-documents response I cite, as PDFs. Members can download them; everyone can see the list.', fontSize='large'),
    goal_rows([('Sep 2026', 'Bid-request specification, Dutch ad exchange, 14 pages', 'Members'),
               ('Sep 2026', 'Tender evaluation report, border surveillance contract, 62 pages', 'Members'),
               ('Jul 2026', 'Transit operator replies to data requests, three cities', 'Free'),
               ('Nov 2025', 'Parliament lobby register export, AI Act, 1,380 rows', 'Free')])))

pattern('corrections-policy', 'Corrections policy', 'text', J(
    heading('How corrections work', 3),
    para('When something I published is wrong, I fix it, add a dated line at the foot of the story saying what changed, and list it on this page. I don’t quietly edit. Send errors to corrections@readout.example.')))

pattern('live-page', 'Page: live notes', 'text', J(pattern_ref('editors-note'), pattern_ref('live-updates'), pattern_ref('pull-figure'), pattern_ref('photo-pair'), pattern_ref('read-next')), block_types='core/post-content')
pattern('methods-page', 'Page: how we report', 'about', J(pattern_ref('key-findings'), pattern_ref('methodology'), pattern_ref('document'), pattern_ref('series-nav'), pattern_ref('corrections-policy'), pattern_ref('republish')), block_types='core/post-content')
pattern('masthead-page', 'Page: masthead', 'about', J(pattern_ref('masthead-names'), pattern_ref('funding')), block_types='core/post-content')
pattern('documents-page', 'Page: documents', 'text', J(pattern_ref('documents-archive')), block_types='core/post-content')
pattern('podcast-page', 'Page: podcast', 'media', J(pattern_ref('podcast-episode'), pattern_ref('podcast-feed'), pattern_ref('behind-the-story')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', group(pattern_ref('nameplate'), tag='header', align='full',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}))
write('parts/header-compact.html', group(row(J(
    dyn('site-title', level=0, fontSize='x-large'),
    dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'}),
    buttons(('Become a member', '/membership/'))), justify='space-between', align='wide'), tag='header', align='full', className='is-style-rule-bottom',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}))
write('parts/footer.html', group(J(
    group(dyn('site-title', level=0, fontSize='xx-large'), align='wide', layout={'type': 'default'}),
    columns(('40%', para('Independent reporting on data brokers, ad tech and the people they track. Paid for by about 2,400 readers, with no advertising and no investors.', fontSize='small')),
            (None, J(heading('Read', 6), para('<a href="/latest/">Latest</a><br><a href="/category/investigations/">Investigations</a><br><a href="/about/">Archive by year</a>', fontSize='small'))),
            (None, J(heading('Pay', 6), para('<a href="/membership/">Membership</a><br><a href="/goals/">Subscriber goals</a><br><a href="/membership/#gift">Gift a year</a>', fontSize='small'))),
            (None, J(heading('Trust', 6), para('<a href="/corrections/">Corrections</a><br><a href="/how-we-report/">How we report</a><br><a href="/documents/">Document archive</a><br><a href="/masthead/">Masthead</a><br><a href="/tips/">Send a tip</a>', fontSize='small'))),
            align='wide'),
    para('Readout, Rue de la Loi 155, box 12, 1040 Brussels. Demo photos are CC0 or public domain from Wikimedia Commons.', fontSize='x-small', align='wide')),
    tag='footer', align='full', className='is-style-inverse',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ---------------------------------------------------------------- templates
PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(pattern_ref('front-page-layout'), style={'spacing': {'padding': {'top': 'var:preset|spacing|40'}}}))
write('templates/home.html', page_template(J(heading('Latest', 1, fontSize='xx-large', align='wide'), pattern_ref('latest-list-archive')), style=PAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('latest-list-archive')), style=PAD))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, fontSize='xx-large', align='wide'),
    dyn('term-description', align='wide'), pattern_ref('latest-list-archive')), style=PAD))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search Readout', showLabel=False, placeholder='A company, a regulator, a place', buttonText='Search'), pattern_ref('latest-list-archive')), style=PAD))
write('templates/404.html', page_template(J(heading('No story at this address', 1),
    para('It may have moved when we changed the URL format in 2025, or it never existed. Search, or start at <a href="/latest/">Latest</a>.'),
    dyn('search', label='Search Readout', showLabel=False, placeholder='A company, a regulator, a place', buttonText='Search')), style=PAD))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large', align='wide'), separator(align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained'})), style=PAD))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large', align='wide'), separator(align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1360px'})), style=PAD))

def single(members):
    return J(template_part('header-compact', 'header'), group(J(
        group(J(row(J(dyn('post-terms', term='category'), dyn('post-terms', term='post_tag', className='is-style-members-tag')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}),
                dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', fontSize='large')), align='wide', layout={'type': 'default'},
              style={'spacing': {'padding': {'bottom': 'var:preset|spacing|30'}}}),
        columns(('22%', group(J(label('Filed'), dyn('post-date', format='l j F Y'), label('Section'), dyn('post-terms', term='category'),
                                para('<a href="/corrections/">Corrections policy</a><br><a href="/tips/">Send a tip</a>', fontSize='x-small')), className='is-style-rule-top', layout={'type': 'default'},
                              style={'spacing': {'blockGap': 'var:preset|spacing|10'}})),
                ('78%', J(dyn('post-featured-image', className='is-style-photo'), dyn('post-content', layout={'type': 'constrained', 'justifyContent': 'left'}),
                          '' if members else pattern_ref('signup-box'))),
                align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
        group(J(dyn('post-navigation-link', type='previous', label='Earlier', showTitle=True), dyn('post-navigation-link', label='Later', showTitle=True)),
              align='wide', className='is-style-rule-top', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'})),
        tag='main', style=PAD), template_part('footer', 'footer'))
write('templates/single.html', single(False))
write('templates/single-members.html', single(True))

write('style.css', '''/*
Theme Name: Dispatch
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A news theme for independent reporters who run a paid publication on their own domain, with a timestamped wire, membership tiers, a members-only break and public subscriber goals.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: dispatch
Tags: news, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, two-columns, grid-layout
*/''')

# ---------------------------------------------------------------- demo content
def story(dateline, paras, members=False, correction=None, extra=None, top=None, bottom=None):
    out = [para('By Lena Varga, ' + dateline, className='is-style-dateline')]
    if top:
        out.append(top)
    out += [para(p) for p in paras[:2]]
    if extra:
        out.append(extra)
    if members:
        out.append(pattern_ref('members-break'))
    out += [para(p) for p in paras[2:]]
    if bottom:
        out.append(bottom)
    if correction:
        out.append(group(para(correction, fontSize='small'), className='is-style-hairline-top'))
    return J(*out)

POSTS = [
 ('An ad exchange sold location data from 41 hospitals', 'ad-exchange-hospital-location-data', 'investigations', ['Members'], 'phones.jpg', '2026-09-24',
  'Bid requests from a Dutch exchange carried the precise location of phones inside cancer wards and fertility clinics. Three data brokers bought the stream.',
  story('Brussels', ['For six weeks this summer, a phone on my desk ran eleven free apps and logged every ad request they made. Of the 212,000 requests, 1,904 carried a latitude and longitude precise to about four metres.',
                     'When I matched those coordinates against hospital footprints in the Netherlands and Belgium, 41 hospitals came up. Eleven of the requests came from inside a single oncology ward in Leuven.',
                     'The exchange, which I am not naming until its lawyers reply to a second set of questions, says it “does not knowingly process health data”.',
                     'Two of the three brokers that bought the stream sell audience segments to insurers. Both declined to say whether hospital visits were among them.'],
        members=True, top=J(pattern_ref('editors-note'), pattern_ref('key-findings')), bottom=J(pattern_ref('methodology'), pattern_ref('document'), pattern_ref('series-nav')), correction='<strong>Correction, 25 September 2026, 16:40.</strong> An earlier version said the Dutch data protection authority fined the exchange €1.2m in 2023. The fine was €525,000.',
        extra=quote('We treat location as location. What is at that location is not our concern.', 'Head of partnerships at one of the brokers, on a recorded call, 9 September 2026'))),
 ('Parliament’s lobby register, read line by line', 'parliament-lobby-register', 'briefings', [], 'parliament.jpg', '2026-09-22',
  'I read all 1,380 meetings logged on the AI Act since January. Four companies account for a third of them.',
  story('Brussels', ['The European Parliament’s transparency register lists 1,380 meetings about the AI Act between 1 January and 31 August. I put all of them into a spreadsheet, which members can download.',
                     'Four companies account for 471 of the meetings. Civil society groups, all of them together, account for 212.', 'The spreadsheet has one row per meeting, with the MEP, the date, the organisation and the stated topic.'])),
 ('A drone contractor won €12m in border contracts. Its director sat on the tender panel.', 'drone-contractor-border-contracts', 'investigations', ['Members'], 'lead.jpg', '2026-09-18',
  'Procurement files show the director of a surveillance drone supplier scored his own company’s bid in 2024.',
  story('Brussels', ['The contract, for aerial surveillance along the Union’s eastern border, was awarded in March 2024. The tender documents, released to me under the access-to-documents rules, list five evaluators.',
                     'One of them was, at the time, a non-executive director of the company that won.', 'The agency says the evaluator declared the conflict. The declaration is not in the file it sent me.'], members=True)),
 ('Your transit card is a location history. Here is who can ask for it.', 'transit-cards-location-history', 'explainers', [], 'crowd.jpg', '2026-09-15',
  'Brussels, Amsterdam and Warsaw keep card tap records for between 6 and 24 months. Police can get them without a judge in two of the three.',
  story('Brussels', ['Every time you tap in, the operator logs the card number, the station and the time. If the card is registered, that log has your name on it.',
                     'I asked the three operators how long they keep the logs and who has asked for them. Two answered in full.', 'If you want to see your own record, the GDPR lets you ask. The template letter is at the end of this story.'],
        correction='<strong>Correction, 2 July 2026.</strong> An earlier version said STIB keeps tap records for 18 months. It is 12.')),
 ('What the Commission’s data broker consultation actually asks', 'commission-data-broker-consultation', 'briefings', [], 'berlaymont.jpg', '2026-09-11',
  'Twenty-three questions, closing 30 October. Seven of them are about definitions, and the definitions matter most.',
  story('Brussels', ['The consultation runs until 30 October. It has 23 questions, and anyone can answer.', 'The questions that will decide what the rules cover are numbers 4 to 10, which ask what a “data broker” is.'])),
 ('Undersea cable maps are public. The repair schedules are not.', 'undersea-cable-repair-schedules', 'investigations', ['Members'], 'cables.jpg', '2026-09-04',
  'Four companies repair most of the cables under the North Sea. One of them shares its schedule with a defence contractor.',
  story('Brussels', ['The routes of undersea data cables are on public maps. When and where they are being repaired is not, and for good reason.', 'A leaked planning document shows one repair company sends its schedule to a private intelligence firm every week.'], members=True)),
 ('Phone masts, planning law and one very annoyed council', 'phone-masts-planning-council', 'briefings', [], 'mast.jpg', '2026-08-28',
  'A council in Flanders refused a mast. The operator put a “temporary” one up anyway, eighteen months ago.',
  story('Mechelen', ['The mast is 25 metres tall and stands on a car park behind a supermarket. It has been “temporary” since February 2025.', 'The council has written to the operator eleven times. I have all eleven letters.'])),
 ('Readout’s numbers, September 2026', 'readout-numbers-september-2026', 'notes', [], 'laptop.jpg', '2026-08-25',
  '2,412 paying members, €19,140 a month, and what happens at 3,000.',
  story('Saint-Gilles', ['Every quarter I publish what Readout earns and spends. This quarter: 2,412 paying members, up from 2,080 in June.', 'At 3,000 I can hire Daan, a researcher I have worked with for three years, for three days a week.'])),
]
posts = [{'title': t, 'slug': s, 'category': c, 'tags': tags, 'image': img, 'date': d, 'excerpt': ex, 'content': body_,
          **({'template': 'single-members'} if 'Members' in tags else {})} for t, s, c, tags, img, d, ex, body_ in POSTS]

demo = {
    'site': {'title': 'Readout', 'tagline': 'Independent reporting on data brokers, ad tech and the people they track'},
    'categories': [{'slug': 'investigations', 'name': 'Investigations', 'description': 'Long stories built on documents. Two or three a month, mostly for members.'},
                   {'slug': 'briefings', 'name': 'Briefings', 'description': 'Short reads on what regulators and companies did this week. Free.'},
                   {'slug': 'explainers', 'name': 'Explainers', 'description': 'How a system works and what you can do about it. Free.'},
                   {'slug': 'notes', 'name': 'Notes', 'description': 'Numbers, corrections and news about Readout itself.'}],
    'front_page': 'home', 'posts_page': 'latest',
    'pages': [{'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'latest', 'title': 'Latest', 'content': ''},
              {'slug': 'membership', 'title': 'Membership', 'pattern': 'dispatch/membership-page'},
              {'slug': 'signup', 'title': 'Sign up', 'pattern': 'dispatch/signup-page'},
              {'slug': 'goals', 'title': 'Subscriber goals', 'pattern': 'dispatch/goals-page', 'template': 'page-wide'},
              {'slug': 'about', 'title': 'About', 'pattern': 'dispatch/about-page', 'template': 'page-wide'},
              {'slug': 'tips', 'title': 'Send a tip', 'pattern': 'dispatch/tips-page'},
              {'slug': 'corrections', 'title': 'Corrections', 'pattern': 'dispatch/corrections-page'},
              {'slug': 'live', 'title': 'Live notes from the data broker vote', 'pattern': 'dispatch/live-page'},
              {'slug': 'how-we-report', 'title': 'How we report', 'pattern': 'dispatch/methods-page'},
              {'slug': 'masthead', 'title': 'Masthead', 'pattern': 'dispatch/masthead-page'},
              {'slug': 'documents', 'title': 'Document archive', 'pattern': 'dispatch/documents-page'},
              {'slug': 'podcast', 'title': 'Podcast', 'pattern': 'dispatch/podcast-page'}],
    'posts': posts,
    'nav': [{'label': 'Latest', 'url': '/latest/'}, {'label': 'Investigations', 'url': '/category/investigations/'}, {'label': 'Live', 'url': '/live/'},
            {'label': 'Podcast', 'url': '/podcast/'}, {'label': 'Membership', 'url': '/membership/'}, {'label': 'Goals', 'url': '/goals/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs('demos/dispatch', exist_ok=True)
json.dump(demo, open('demos/dispatch/content.json', 'w'), indent=1, ensure_ascii=False)
print('built dispatch')
