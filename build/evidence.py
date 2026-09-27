# Design note (evidence, idea 047b: true-crime podcast)
# Direction: "the case file". A documentary title card over a grey archive photo, then the file itself: dates, exhibits, sources, corrections.
# Why: the honest true-crime shows sell trust, not gore. Showing the paperwork (sources, dated corrections, who was harmed) is the design.
# Fonts: Mozilla Headline, condensed and upper case for documentary titles and exhibit tags; Source Serif 4 for the reading voice. No third face.
# Palette: near-black ground, bone text, manila folder panels with black ink, one signal red for warnings and links. Every photo shown in greyscale.
# Layout idea: an evidence board of tagged exhibits on the home page, and episode pages that open with a manila file card and end with numbered sources.
import sys, json, os, datetime
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('evidence')
import blocks as _b
def group(inner, tag='div', layout='constrained', **attrs):
    # WordPress drops the layout of a <div> group that has align + padding when it re-serialises; <section> keeps it.
    if tag == 'div' and 'padding' in json.dumps(attrs.get('style', {})):
        tag = 'section'
    return _b.group(inner, tag=tag, layout=layout, **attrs)
S = THEME['slug']
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
    ('base', '#121212', 'Night'), ('contrast', '#ECE6DA', 'Bone'), ('accent', '#F06449', 'Signal red'),
    ('accent-2', '#D9C79F', 'Manila'), ('surface', '#1D1C1A', 'Case board'), ('line', '#45423D', 'Rule'),
    ('muted', '#ABA59A', 'Ash'), ('folder', '#D9C79F', 'Folder'), ('ink', '#141311', 'Ink'),
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

focus = {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '3px'}}
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE),
                  'duotone': [{'slug': 'archive', 'colors': ['#121212', '#ECE6DA'], 'name': 'Archive print'}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': [disp, body],
            'fontSizes': [fs('x-small', '0.875rem', 'Caption'), fs('small', '1rem', 'Small'), fs('medium', '1.1875rem', 'Body'),
                          fs('large', '1.625rem', 'Large', '1.35rem'), fs('x-large', '2.75rem', 'Section', '2rem'),
                          fs('xx-large', '4.5rem', 'Title', '2.9rem'), fs('display', '9.5rem', 'Title card', '3.8rem')],
        },
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2.2vw, 1.75rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.25rem, 5.5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.62'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '0.95', 'letterSpacing': '0', 'textTransform': 'uppercase'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.05'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.3', 'textTransform': 'none', 'fontWeight': '600'}},
            'button': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                       'border': {'radius': '0', 'width': '0', 'style': 'solid'},
                       'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small', 'textTransform': 'uppercase', 'letterSpacing': '0.02em'},
                       'spacing': {'padding': {'top': '0.75em', 'bottom': '0.7em', 'left': '1.2em', 'right': '1.2em'}},
                       ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}}, ':focus': focus},
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|large', 'textTransform': 'uppercase', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/heading': {'elements': {'link': {'color': {'text': 'currentColor'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
            'core/image': {'border': {'radius': '0'}, 'css': '& img{filter:grayscale(1) contrast(1.08)}'},
            'core/post-featured-image': {'border': {'radius': '0'}, 'css': '& img{filter:grayscale(1) contrast(1.08)}'},
            'core/cover': {'css': '& .wp-block-cover__image-background{filter:grayscale(1) contrast(1.1)}'},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontStyle': 'italic', 'lineHeight': '1.4'},
                           'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '2px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'textTransform': 'uppercase', 'lineHeight': '1'},
                               'border': {'top': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}}},
            'core/details': {'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;font-weight:700;cursor:pointer}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table.has-fixed-layout{table-layout:auto}& table th{text-align:left;font-family:var(--wp--preset--font-family--display);font-weight:600}& table td,& table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.6em .9em .6em 0;vertical-align:top}& table thead{border:0;border-bottom:2px solid currentColor}'},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'},
                            'css': '& input{background:var(--wp--preset--color--surface);color:var(--wp--preset--color--contrast);border-color:var(--wp--preset--color--line)}'},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small'}},
            'core/audio': {'css': '& audio{width:100%;min-width:0;filter:invert(1) grayscale(1)}'},
        },
        'css': ('.wp-block-column>.wp-block-group:only-child{height:100%}:where(h1,h2,h3,.has-display-font-family,.wp-block-site-title){font-stretch:75%}'
                ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                'body{font-synthesis:none;font-variant-numeric:tabular-nums lining-nums}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--accent);outline-offset:3px}'
                ':where(.wp-block-post-content)>:where(h2,h3){margin-top:var(--wp--preset--spacing--60)}'),
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'season-break', 'title': 'Season break notice'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
                        {'name': 'single-update', 'title': 'Update or correction episode', 'postTypes': ['post']}],
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

write('styles/daylight-file.json', variation('Daylight file', [
    ('base', '#EFE9DC', 'Night'), ('contrast', '#161514', 'Bone'), ('accent', '#A8321D', 'Signal red'),
    ('accent-2', '#6B5A33', 'Manila'), ('surface', '#E4DCC9', 'Case board'), ('line', '#B9AF99', 'Rule'),
    ('muted', '#5A554C', 'Ash'), ('folder', '#D6C498', 'Folder'), ('ink', '#141311', 'Ink')]))
write('styles/night-shift.json', variation('Night shift', [
    ('base', '#0D1622', 'Night'), ('contrast', '#E6EAF0', 'Bone'), ('accent', '#FFB547', 'Signal red'),
    ('accent-2', '#C9D3DF', 'Manila'), ('surface', '#15212F', 'Case board'), ('line', '#34465C', 'Rule'),
    ('muted', '#A1AEBF', 'Ash'), ('folder', '#C9D3DF', 'Folder'), ('ink', '#0D1622', 'Ink')]))
write('styles/newsprint.json', variation('Newsprint', [
    ('base', '#DCDAD5', 'Night'), ('contrast', '#111111', 'Bone'), ('accent', '#9E1B12', 'Signal red'),
    ('accent-2', '#3B3B3B', 'Manila'), ('surface', '#CFCDC7', 'Case board'), ('line', '#8F8C85', 'Rule'),
    ('muted', '#45433F', 'Ash'), ('folder', '#F2F0EA', 'Folder'), ('ink', '#111111', 'Ink')]))

def section(slug, title, types, styles):
    if 'css' in styles:
        styles = dict(styles, css=split_css(styles['css']))
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                                        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))

section('file-card', 'Manila file card', ['core/group', 'core/column'],
        {'color': {'background': 'var:preset|color|folder', 'text': 'var:preset|color|ink'},
         'elements': {'link': {'color': {'text': 'var:preset|color|ink'}}, 'heading': {'color': {'text': 'var:preset|color|ink'}},
                      'button': {'color': {'background': 'var:preset|color|ink', 'text': 'var:preset|color|folder'}}},
         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
         'css': '& table td,& table th{border-bottom-color:currentColor!important}& table td:first-child{font-family:var(--wp--preset--font-family--display);font-weight:600;width:38%}'})
section('board', 'Case board', ['core/group', 'core/columns'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
         'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}, 'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}})
section('warning', 'Content warning', ['core/paragraph', 'core/group'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'border': {'left': {'color': 'var:preset|color|accent', 'width': '4px', 'style': 'solid'}},
         'spacing': {'padding': {'left': 'var:preset|spacing|30', 'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10'}},
         'css': '& strong{font-family:var(--wp--preset--font-family--display);text-transform:uppercase;color:var(--wp--preset--color--accent)}'})
section('exhibit-tag', 'Exhibit tag', ['core/paragraph'],
        {'color': {'background': 'var:preset|color|folder', 'text': 'var:preset|color|ink'},
         'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600', 'lineHeight': '1.3'},
         'spacing': {'padding': {'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
         'css': '&{display:inline-block;transform:rotate(-1.2deg);margin-top:-1.4rem!important;position:relative;margin-left:.75rem!important}'})
section('timeline', 'Case timeline', ['core/table'],
        {'css': '& td:first-child{font-family:var(--wp--preset--font-family--display);font-weight:700;white-space:nowrap;width:9.5rem;color:var(--wp--preset--color--accent-2)}& td{padding-top:.85em;padding-bottom:.85em}'})
section('sources', 'Numbered sources', ['core/list'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'css': '& li{padding:.45rem 0;border-bottom:1px solid var(--wp--preset--color--line)}& li::marker{font-family:var(--wp--preset--font-family--display);font-weight:700;color:var(--wp--preset--color--accent-2)}'})
section('chapters', 'Chapter list', ['core/list'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding-left:0!important}& li{display:flex;gap:1.1rem;padding:.5rem 0;border-bottom:1px solid var(--wp--preset--color--line)}& li a{min-width:3.4rem;font-family:var(--wp--preset--font-family--display);font-weight:700;text-decoration:none}& li a:hover{text-decoration:underline}'})
section('redacted', 'Document with redactions', ['core/paragraph', 'core/quote'],
        {'color': {'background': 'var:preset|color|folder', 'text': 'var:preset|color|ink'},
         'typography': {'fontSize': 'var:preset|font-size|small', 'fontStyle': 'normal'},
         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}},
         'css': '& strong{background:var(--wp--preset--color--ink);color:var(--wp--preset--color--ink);padding:0 .2em;user-select:none}& cite{color:var(--wp--preset--color--ink);font-family:var(--wp--preset--font-family--display)}'})
section('episode-row', 'Episode row', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})
section('listen-row', 'Listen links', ['core/list'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding:0!important;display:flex;flex-wrap:wrap;gap:.3rem 1.3rem}'})
section('case-list', 'Case list', ['core/categories'],
        {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small', 'textTransform': 'uppercase'},
         'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.4rem 1.6rem}'})

# ---------------------------------------------------------------- content helpers
AUD = 'https://upload.wikimedia.org/wikipedia/commons/a/a7/Trialofsusanbanthony_18_anonymous_128kb.ogg'
CAP = 'Stand-in audio: a LibriVox reading from “An Account of the Proceedings on the Trial of Susan B. Anthony” (CC0, Wikimedia Commons). Replace with your episode file.'

def ts(sec):
    return '%02d:%02d' % (sec // 60, sec % 60) if sec < 3600 else '%d:%02d:%02d' % (sec // 3600, sec % 3600 // 60, sec % 60)

def chapters(items):
    return lst(['<a href="%s#t=%d">%s</a> %s' % (AUD, s, ts(s), t) for s, t in items], className='is-style-chapters')

def listen_row():
    return lst(['<a href="https://podcasts.apple.com/">Apple Podcasts</a>', '<a href="https://open.spotify.com/">Spotify</a>',
                '<a href="https://pocketcasts.com/">Pocket Casts</a>', '<a href="https://overcast.fm/">Overcast</a>',
                '<a href="/feed/">RSS</a>'], className='is-style-listen-row')

def file_card(rows, title='Case file'):
    return group(J(heading(title, 4), table([[a, b] for a, b in rows])), className='is-style-file-card')

def label(t, **kw):
    return para(t, fontSize='x-small', fontFamily='display', style={'typography': {'fontWeight': '700'}}, **kw)

# ---------------------------------------------------------------- patterns
pattern('title-card', 'Title card: this season, with an archive photo strip', 'featured', group(J(
    group(J(
        label('Low Water, season 2, part 4 out now'),
        heading('Who started the fire at Wagstaff’s Yard?', 1, fontSize='display'),
        columns(('62%', para('On 11 March 1994 a timber yard on the Hull docks burned down and Arthur Kell, the night watchman, died. Lee Pryce served fourteen years for it. He says he wasn’t there. We spent a year with the paperwork.', fontSize='large', style={'typography': {'lineHeight': '1.4'}})),
                ('38%', buttons(('Start with part 1', '/the-night-of-11-march-1994/'), ('Hear part 4', '/the-second-fire-report/', {'className': 'is-style-outline'}))),
                verticalAlignment='bottom')), align='wide', layout={'type': 'default'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
    image('docks.jpg', 'Sepia photograph of a dock basin with sailing ships and a tall brick tower', caption='Alexandra Dock area, early 1900s. Archive photograph, public domain.', lightbox=False, align='wide', aspectRatio='21/9', scale='cover')),
    align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|40'}, 'margin': {'top': '0'}}}),
    description='Documentary opener: the season’s question, set big over a greyscale archive photo.')

pattern('latest-file', 'Latest episode: file card and player', 'featured,audio', columns(
    ('34%', file_card([['Case', 'Wagstaff’s Yard'], ['Part', '4 of 6'], ['Released', 'Thursday 24 September 2026'], ['Length', '48 minutes'], ['Warning', 'Death in a fire, described without detail']])),
    ('66%', J(label('Latest episode', textColor='muted'),
              heading('<a href="/the-second-fire-report/">The second fire report</a>', 2, fontSize='xx-large'),
              para('Eight days after the fire, a second investigator wrote a report that never reached the jury. We found it in a box at the Hull History Centre. Brian Oduya, who spent 30 years investigating fires, reads it with us.'),
              para('<strong>Content warning</strong> This episode describes how Arthur Kell died. There are no recordings of emergency calls in this series, and there never will be.', className='is-style-warning'),
              audio(AUD, CAP), listen_row())),
    align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('content-warning', 'Content warning line', 'text,audio', para('<strong>Content warning</strong> Discussion of a death in a fire, and of a suicide attempt in prison (31:20 to 34:05). Help is listed at the end of the show notes.', className='is-style-warning'),
        description='Say what the episode contains and where, so people can skip or stop.')

pattern('timeline', 'The case so far (timeline)', 'text', J(
    heading('The case so far', 2),
    table([['11 Mar 1994', 'Fire at Wagstaff’s timber yard, Alexandra Dock. Arthur Kell, 63, the night watchman, dies.'],
           ['19 Mar 1994', 'A second fire report is written by an investigator from Leeds. It is filed and not disclosed.'],
           ['2 Jun 1994', 'Lee Pryce, 22, is arrested after a witness places him on Hedon Road that night.'],
           ['Feb 1995', 'Convicted of manslaughter and arson at Hull Crown Court. Sentenced to 16 years.'],
           ['2009', 'Released on licence. Has applied twice to the Criminal Cases Review Commission.'],
           ['May 2025', 'Arthur’s daughter Janet writes to us. She wants to know what happened to her dad.']], className='is-style-timeline'),
    para('<a href="/cases/">Both cases, from the beginning</a>', fontSize='small')))

def exhibit(img, alt, tag):
    return group(J(image(img, alt, lightbox=True, aspectRatio='4/3', scale='cover'), para(tag, className='is-style-exhibit-tag')), layout={'type': 'default'})

pattern('evidence-board', 'Evidence board (tagged exhibits)', 'gallery,featured', group(J(
    row(J(heading('On the board', 2), para('Everything we show is from a public archive or given to us with permission.', fontSize='small', textColor='muted')), justify='space-between', align='wide'),
    grid(J(
        exhibit('court.jpg', 'The old Crown Court building in Wakefield: a stone portico with columns and a clock tower', 'Exhibit 1. The court building. The trial moved here in 1995.'),
        exhibit('archive.jpg', 'Shelves of labelled grey archive boxes', 'Exhibit 2. Box 14 of 31, where the second report was filed'),
        exhibit('newspaper.jpg', 'A printing press with newspapers coming off it and a sign reading next press run at 1.00', 'Exhibit 3. The evening paper, 12 March 1994'),
        exhibit('tape.jpg', 'Close-up of the metal plate on an old cassette tape recorder listing its tape speed and power', 'Exhibit 4. Janet’s tapes of her dad, recorded in 1989')),
        min_width='15rem', align='wide')), align='full', className='is-style-board', layout={'type': 'constrained'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'margin': {'top': '0'}}}),
    description='Four greyscale exhibits, each with a manila tag. Swap the photos for your own documents.')

ep_row = group(J(
    group(J(dyn('post-terms', term='category', separator=', '), dyn('post-date', format='j M Y')), layout={'type': 'flex', 'orientation': 'vertical'}, style={'spacing': {'blockGap': 'var:preset|spacing|10'}}),
    dyn('post-title', isLink=True, level=3, fontSize='x-large'),
    dyn('post-excerpt', excerptLength=24, fontSize='small')),
    className='is-style-episode-row', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '14rem'})

pattern('episode-list', 'Episodes, newest first', 'posts,query', group(J(
    row(J(heading('Episodes', 2), dyn('categories', className='is-style-case-list')), justify='space-between'),
    query(ep_row, per_page=8)), align='wide', layout={'type': 'default'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}), keywords='episodes, list')

pattern('episode-list-archive', 'Episode list (inherits the page query)', 'posts,query', inherit_query(ep_row, align='wide'), inserter=False)

pattern('cases-index', 'Both cases', 'featured,text', columns(
    (None, J(image('docks.jpg', 'Sepia photograph of a dock with sailing ships and a tall brick tower', href='/category/wagstaffs-yard/'),
             label('Season 2, 2026, six parts'), heading('<a href="/category/wagstaffs-yard/">Wagstaff’s Yard</a>', 2),
             para('A fire, a watchman who died, and a conviction that rested on one witness. Arthur Kell’s daughter asked us to look again.'))),
    (None, J(image('road.jpg', 'A street lined with bare trees disappearing into thick fog', href='/category/the-ferry-inn/'),
             label('Season 1, 2025, five parts'), heading('<a href="/category/the-ferry-inn/">The Ferry Inn</a>', 2),
             para('Carol Denby, 29, left the Ferry Inn at Hessle on 2 November 1987 and was not seen again. Her brother Mark asked us to make this series. The case is still open.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('chapters-list', 'Chapters with timestamps', 'text,audio', J(
    heading('Chapters', 3),
    chapters([(0, 'Previously'), (215, 'Box 14'), (870, 'Brian reads the report'), (1640, 'What “point of origin” means'), (2310, 'Why the jury never saw it'), (2740, 'Janet hears it for the first time')]),
    para('Each time opens the audio file at that point. Most podcast apps show these chapters too.', fontSize='x-small', textColor='muted')))

pattern('sources-list', 'Sources for an episode', 'text', J(
    heading('Sources', 3),
    lst(['West Yorkshire Fire Service, investigation report, 19 March 1994. Hull History Centre, ref. C DPF/4/14.',
         'R v Pryce, Hull Crown Court, February 1995. Trial transcript bought from the court transcription service, 2025.',
         'Interview with Brian Oduya, retired fire investigator, recorded in Leeds on 3 July 2026.',
         'Hull evening paper, 12 and 14 March 1994, read on microfilm at Hull Central Library.',
         'Letter from the Criminal Cases Review Commission to Lee Pryce, 2017, shared by Lee.'], ordered=True, className='is-style-sources'),
    para('We link every source we can. Where we can’t (court papers, private letters), we say where it is kept. <a href="/sources-and-corrections/">All sources and corrections</a>', fontSize='small')))

pattern('transcript', 'Transcript in a fold', 'text,audio', J(
    heading('Transcript', 3),
    details('Read the transcript', J(
        para('<strong>Maren</strong> The box is labelled “Wagstaff’s, misc.” Nobody has signed it out since 1996.'),
        para('<strong>Brian</strong> Misc. That’s where things go when nobody wants to decide about them.'),
        para('<strong>Maren</strong> Can you read the first line?'),
        para('<strong>Brian</strong> “The seat of the fire is not consistent with the account given.” That’s a sentence you notice.'),
        para('Transcripts are typed by Dev and checked against the audio. Names of people who asked not to be named are withheld in both.', fontSize='x-small', textColor='muted'))),
    para('<a href="/transcripts/">All transcripts, with PDF downloads</a>', fontSize='small')))

pattern('redacted-statement', 'Document quote with redactions', 'text', J(
    quote('I saw a lad on Hedon Road at about ten past one. He had a <strong>green</strong> jacket on and he was walking fast towards <strong>Marfleet Lane</strong>. I did not see his face properly because of <strong>the lorry</strong>.',
          'Witness statement, 2 June 1994. Words blacked out by Humberside Police before release.', className='is-style-redacted'),
    para('Redactions are shown as they appear in the released document. We never add our own.', fontSize='x-small', textColor='muted')),
    description='A document excerpt. Bold words render as black bars; screen readers still read them, so only bold words that are already public.')

pattern('in-memory', 'In memory of the person harmed', 'text,about', group(J(
    label('Arthur Kell, 1931 to 1994'),
    para('Arthur worked on the docks for 41 years, the last nine as a night watchman at Wagstaff’s. He kept pigeons in Marfleet, was a steward at the Hull KR ground and taught his granddaughter to play crib. His daughter Janet chose these words.', fontSize='large'),
    para('We use Arthur’s name, not “the victim”. We don’t describe his injuries.', fontSize='small', textColor='muted')),
    className='is-style-board', style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}}))

pattern('how-we-report', 'How we report', 'about,text', J(
    heading('How we report', 2),
    lst(['We only make a series when a family member of the person harmed has agreed to it, and we tell them before each episode goes out.',
         'We don’t play 999 calls, crime scene audio or post-mortem details. We say that a person died and how that affected people.',
         'We name people who were convicted. We don’t name people who were only suspected, arrested or questioned.',
         'Every claim has a source listed under the episode. When we get something wrong, we fix the audio and the transcript and log it with a date.',
         'We don’t sell merchandise about real crimes.']),
    para('<a href="/sources-and-corrections/">Read the corrections log</a>', fontSize='small')))

pattern('tip-line', 'If you know something', 'contact,call-to-action', group(J(
    heading('If you know something', 2),
    para('If you were on Alexandra Dock or Hedon Road on the night of 10 to 11 March 1994, or you knew Carol Denby in 1987, we would like to hear from you. You can stay anonymous. We will never pass your details on without your permission.'),
    para('Email <a href="mailto:tips@lowwater.example">tips@lowwater.example</a>, or use Signal on 07700 900417.'),
    para('To give information to the police anonymously, call Crimestoppers on 0800 555 111. If it is an emergency, call 999.', fontSize='small')),
    className='is-style-file-card'))

pattern('support-tiers', 'Support the show', 'call-to-action,services', J(
    heading('Paying for a year of paperwork', 2),
    para('One series takes about a year. Court transcripts alone cost us £1,860 for season 2. Listeners pay for most of it.'),
    table([['Listener', '£4 a month', 'Ad-free feed and episodes a week early'],
           ['Researcher', '£9 a month', 'All of the above, plus the monthly behind-the-files episode and our document notes'],
           ['Library or newsroom', '£120 a year', 'A licence to use clips in teaching or journalism, with transcripts']],
          head=['Tier', 'Price', 'What it pays for']),
    buttons(('Support on Patreon', 'https://www.patreon.com/'), ('Email about a licence', 'mailto:hello@lowwater.example?subject=Licence', {'className': 'is-style-outline'})),
    para('We don’t take sponsors who sell home security, legal services or anything else that profits from fear.', fontSize='small', textColor='muted')))

pattern('sponsor-read', 'Sponsor read', 'call-to-action', group(J(
    label('This episode is supported by'),
    heading('Hull History Centre Friends', 4),
    para('The volunteers who keep the searchroom open on Saturday mornings. Membership is £15 a year and gets you into the talks. We only read for things we use.')),
    className='is-style-board', style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('hosts', 'Who makes the show', 'team,about', columns(
    (None, J(heading('Maren Holt', 3), label('Reporter and host', textColor='muted'),
             para('Covered Hull Crown Court for a local paper for 14 years, until the paper stopped sending anyone. Lives in Hessle. Reads every page of every file, including the ones stapled upside down.'))),
    (None, J(heading('Dev Ramsay', 3), label('Producer', textColor='muted'),
             para('Sound engineer who used to record brass bands. Edits the show in a shed in Cottingham and types the transcripts. Is the one who says “we can’t prove that” in every meeting.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('corrections-log', 'Corrections log', 'text', J(
    heading('Corrections', 2),
    para('Newest first. We fix the audio and the transcript, then log it here.'),
    table([['25 Sep 2026', 'Wagstaff’s Yard, part 3', 'We said the second fire report was dated 14 March. It is dated 19 March. Audio re-edited at 22:14.'],
           ['4 Sep 2026', 'Wagstaff’s Yard, part 1', 'We gave Arthur Kell’s age as 64. He was 63. Janet Kell spotted it.'],
           ['12 Dec 2025', 'The Ferry Inn, part 2', 'The bus Carol would have caught was the 350, not the 155. Thanks to a listener who drove it.'],
           ['30 Oct 2025', 'The Ferry Inn, part 1', 'We named a man who was questioned in 1987 but never charged. We have removed his name and apologised to him.']],
          head=['Date', 'Episode', 'What changed'])))

pattern('glossary', 'Term used in this episode', 'text', group(J(
    label('Term used in this episode'),
    heading('Non-disclosure', 3),
    para('When the prosecution has material that could help the defence and doesn’t hand it over. It is one of the most common reasons the Criminal Cases Review Commission sends a case back to appeal.')),
    className='is-style-board', style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('guest-card', 'Interviewee card', 'team', group(J(
    label('Interviewed in this episode'), heading('Brian Oduya', 3),
    para('Fire investigator for 30 years, mostly in West Yorkshire. Retired in 2019. Gave evidence in around 200 cases and says he got at least two of them wrong.')),
    className='is-style-file-card'))

pattern('season-break', 'Notice: between seasons', 'banner', group(
    para('Season 3 is in production. New episodes from Thursday 14 January. Updates on the Wagstaff’s Yard case will go out in the feed as they happen.', fontSize='small', fontFamily='display', style={'typography': {'fontWeight': '600'}}),
    className='is-style-file-card', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='A bar for the gap between seasons. Put the return date in it.')

pattern('help-lines', 'Help lines', 'text', J(
    heading('If this episode affected you', 4),
    para('Samaritans: 116 123, any time. Victim Support: 08 08 16 89 111. Support After Murder and Manslaughter (SAMM): 0121 472 2912.', fontSize='small')))

pattern('transcript-download', 'Transcript download line', 'text', para('Transcript: on this page, or as a <a href="/transcripts/">PDF with page numbers for citing</a>.', fontSize='small'))

pattern('subscribe-page', 'Page: subscribe', 'call-to-action', J(
    para('New parts come out on Thursdays at 5am while a season is running. Between seasons the feed is quiet, apart from updates.', fontSize='large'),
    table([['<a href="https://podcasts.apple.com/">Apple Podcasts</a>', 'Tap Follow. Turn on downloads if you listen on the train.'],
           ['<a href="https://open.spotify.com/">Spotify</a>', 'Tap Follow and the bell.'],
           ['<a href="https://pocketcasts.com/">Pocket Casts</a>', 'Chapters and transcripts both work here.'],
           ['<a href="https://overcast.fm/">Overcast</a>', 'Chapters work. Smart Speed makes Dev sad but go ahead.'],
           ['<a href="/feed/">RSS</a>', 'Paste the link into any podcast app.']], head=['App', 'Notes']),
    para('Start each case at part 1. The parts are not standalone and we don’t recap much.'),
    pattern_ref('support-tiers')), block_types='core/post-content')

pattern('sources-page', 'Page: sources and corrections', 'text', J(
    para('This page lists what we used and what we got wrong. Sources for each part are also under that episode.', fontSize='large'),
    pattern_ref('corrections-log'),
    heading('Archives we used', 2),
    lst(['Hull History Centre, Worship Street. Fire service and police records released under the 30-year rule.',
         'Hull Crown Court and the court transcription service, for the 1995 trial transcript.',
         'Hull Central Library, for microfilm of the local papers from 1987 and 1994.',
         'The National Archives at Kew, for the 1995 appeal papers.'], className='is-style-sources', ordered=True),
    heading('Found a mistake?', 3),
    para('Email <a href="mailto:corrections@lowwater.example">corrections@lowwater.example</a> with the episode and the time. We reply within a week and credit you if you want.')),
    block_types='core/post-content')

pattern('about-page', 'Page: about and how we report', 'about', J(
    para('Low Water is an independent true-crime podcast about cases from the Humber estuary, made by two people in Hessle and Cottingham. Each season is one case. We work from court records, archive files and people who were there.', fontSize='large'),
    pattern_ref('hosts'), pattern_ref('how-we-report'), pattern_ref('in-memory')), block_types='core/post-content')

pattern('tips-page', 'Page: tips', 'contact', J(pattern_ref('tip-line'), pattern_ref('help-lines')), block_types='core/post-content')

pattern('support-page', 'Page: support', 'call-to-action', J(pattern_ref('support-tiers'), pattern_ref('sponsor-read')), block_types='core/post-content')

pattern('cases-page', 'Page: cases', 'featured', J(pattern_ref('cases-index'), pattern_ref('timeline')), block_types='core/post-content')

pattern('transcripts-page', 'Page: transcripts', 'text', J(
    para('Every part has a transcript on its page. PDFs have page and line numbers so students and journalists can cite them.', fontSize='large'),
    table([['Wagstaff’s Yard', 'Parts 1 to 4', '<a href="/category/wagstaffs-yard/">On each episode page</a>'],
           ['The Ferry Inn', 'Parts 1 to 5', '<a href="/category/the-ferry-inn/">On each episode page</a>']], head=['Case', 'Parts', 'Where'])),
    block_types='core/post-content')

pattern('episode-full', 'Episode: full layout (file card, player, chapters, sources, transcript)', 'audio,featured', J(
    file_card([['Case', 'Wagstaff’s Yard'], ['Part', '4 of 6'], ['Released', 'Thursday 24 September 2026'], ['Length', '48 minutes']]),
    audio(AUD, CAP), pattern_ref('content-warning'), pattern_ref('chapters-list'), pattern_ref('sources-list'),
    pattern_ref('guest-card'), pattern_ref('transcript'), pattern_ref('help-lines')),
    block_types='core/post-content', description='Every part in the same order: file card, player, warning, chapters, sources, transcript.')

pattern('front-page-layout', 'Home: title card, latest file, board, episodes', 'featured', J(
    pattern_ref('title-card'), pattern_ref('latest-file'), pattern_ref('evidence-board'),
    columns(('58%', pattern_ref('timeline')), ('42%', J(pattern_ref('in-memory'))), align='wide',
            style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}, 'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('episode-list'),
    columns(('58%', pattern_ref('how-we-report')), ('42%', pattern_ref('tip-line')), align='wide',
            style={'spacing': {'padding': {'bottom': 'var:preset|spacing|70'}, 'blockGap': {'left': 'var:preset|spacing|60'}}})), inserter=False)

pattern('episode-rail', 'Episode rail: case and help', 'audio', J(
    group(J(label('Case'), dyn('post-terms', term='category', separator=', '), label('Released'), dyn('post-date', format='l j F Y', textColor='ink')), className='is-style-file-card'),
    dyn('post-featured-image', aspectRatio='4/3'),
    group(J(label('Heard something that’s wrong?'), para('Tell us and we’ll fix it and log it. <a href="/sources-and-corrections/">Corrections</a>', fontSize='small'))),
    group(J(label('Know something?'), para('<a href="/tips/">How to reach us safely</a>', fontSize='small')))), inserter=False)

# ---------------------------------------------------------------- parts
write('parts/header.html', group(row(J(
    dyn('site-title', level=0),
    row(J(dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'}), buttons(('Subscribe', '/subscribe/'))),
        justify='right', style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
    justify='space-between', align='wide'), tag='header', align='full',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
           'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}}))

write('parts/footer.html', group(J(
    columns(('44%', J(para('Low Water', fontSize='xx-large', fontFamily='display', style={'typography': {'fontWeight': '700', 'textTransform': 'uppercase', 'lineHeight': '0.9'}}),
                     para('Independent true crime from the Humber estuary. One case a season, built on court records and archive files. Made in Hessle and Cottingham.', fontSize='small'))),
            (None, J(heading('Listen', 6), listen_row())),
            (None, J(heading('The file', 6), para('<a href="/sources-and-corrections/">Sources and corrections</a><br><a href="/transcripts/">Transcripts</a><br><a href="/about/">How we report</a><br><a href="/tips/">Tips, safely</a>', fontSize='small'))),
            (None, J(heading('Help', 6), para('Samaritans 116 123<br>Victim Support 08 08 16 89 111<br>Crimestoppers 0800 555 111', fontSize='small'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
    para('The cases, people and places in this demo are invented. Photos are CC0 or public domain from Wikimedia Commons, shown in greyscale. Stand-in audio is a CC0 LibriVox reading.', fontSize='x-small', textColor='muted', align='wide')),
    tag='footer', align='full', className='is-style-board',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

write('parts/season-break.html', pattern_ref('season-break'))

# ---------------------------------------------------------------- templates
PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
NOTOP = {'spacing': {'margin': {'top': '0'}, 'padding': {'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(pattern_ref('front-page-layout'), style={'spacing': {'margin': {'top': '0'}}}))
write('templates/home.html', page_template(J(
    heading('Episodes', 1, fontSize='display', align='wide'),
    row(J(para('Start each case at part 1. <a href="/cases/">The cases</a> and <a href="/transcripts/">transcripts</a>.'), dyn('categories', className='is-style-case-list')), justify='space-between', align='wide'),
    pattern_ref('episode-list-archive')), style=PAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('episode-list-archive')), style=PAD))
write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='display'),
    dyn('term-description', align='wide', fontSize='large'),
    pattern_ref('episode-list-archive')), style=PAD))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='A name, a place, a date', buttonText='Search'),
    pattern_ref('episode-list-archive')), style=PAD))
write('templates/404.html', page_template(J(
    heading('Not in the file', 1),
    para('That page doesn’t exist, or it moved when we split the seasons into cases. Search for a name or a place, or go to <a href="/cases/">the cases</a>.'),
    dyn('search', label='Search', showLabel=False, placeholder='A name, a place, a date', buttonText='Search')), style=PAD))

def title_band():
    return group(group(dyn('post-title', level=1, fontSize='display'), align='wide', layout={'type': 'default'}), align='full',
                 style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|40'}, 'margin': {'top': '0'}},
                        'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}})
write('templates/page.html', page_template(J(title_band(), group(dyn('post-content', align='wide', layout={'type': 'constrained'}), align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}}})), style=NOTOP))
write('templates/page-wide.html', page_template(J(title_band(), group(dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'}), align='wide', layout={'type': 'default'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}}})), style=NOTOP))

write('templates/single.html', page_template(J(
    group(J(dyn('post-terms', term='category', separator=', '), dyn('post-title', level=1, fontSize='xx-large')), align='wide', layout={'type': 'default'}),
    columns(('64%', dyn('post-content', layout={'type': 'default'})),
            ('36%', pattern_ref('episode-rail')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|70'}}}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous part', showTitle=True, taxonomy='category'),
            dyn('post-navigation-link', label='Next part', showTitle=True, taxonomy='category')),
          align='wide', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'},
          style={'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})),
    style=PAD))
write('templates/single-update.html', page_template(J(
    group(J(para('Update', fontSize='small', fontFamily='display', style={'typography': {'fontWeight': '700', 'textTransform': 'uppercase'}}),
            dyn('post-title', level=1, fontSize='xx-large'), dyn('post-date', format='l j F Y')), className='is-style-file-card'),
    dyn('post-content', layout={'type': 'constrained'})), style=PAD))

write('style.css', '''/*
Theme Name: Evidence
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A podcast theme for investigative and true-crime series, with case archives, episode file cards, sources, a dated corrections log and content warnings.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: evidence
Tags: blog, podcast, news, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, two-columns
*/''')

# ---------------------------------------------------------------- demo content
def ep(case, part, of, date_s, mins, warning, chaps, sources, tr, extra=None):
    blocks_ = [file_card([['Case', case], ['Part', '%d of %d' % (part, of)], ['Released', date_s], ['Length', '%d minutes' % mins]]),
               audio(AUD, CAP)]
    if warning:
        blocks_.append(para('<strong>Content warning</strong> ' + warning, className='is-style-warning'))
    blocks_ += [heading('Chapters', 3), chapters(chaps)]
    if extra:
        blocks_.append(extra)
    blocks_ += [heading('Sources', 3), lst(sources, ordered=True, className='is-style-sources'),
                heading('Transcript', 3), details('Read the transcript', J(*[para('<strong>%s</strong> %s' % (w, t)) for w, t in tr],
                    para('Typed by Dev and checked against the audio.', fontSize='x-small'))),
                heading('If this episode affected you', 4), para('Samaritans: 116 123, any time. Victim Support: 08 08 16 89 111.', fontSize='small')]
    return J(*blocks_)

W, F = 'Wagstaff’s Yard', 'The Ferry Inn'
EPS = [
 ('The second fire report', 'the-second-fire-report', 'wagstaffs-yard', 'archive.jpg',
  'Eight days after the fire, an investigator from Leeds wrote a report the jury never saw. Brian Oduya reads it with us.',
  (W, 4, 6, 48, 'This episode describes how Arthur Kell died, without detail.',
   [(0, 'Previously'), (215, 'Box 14'), (870, 'Brian reads the report'), (1640, 'What “point of origin” means'), (2310, 'Why the jury never saw it'), (2740, 'Janet hears it for the first time')],
   ['West Yorkshire Fire Service, investigation report, 19 March 1994. Hull History Centre, ref. C DPF/4/14.', 'Interview with Brian Oduya, recorded in Leeds on 3 July 2026.', 'R v Pryce trial transcript, day 3, pages 41 to 58.'],
   [('Maren', 'The box is labelled “Wagstaff’s, misc.” Nobody has signed it out since 1996.'), ('Brian', 'Misc. That’s where things go when nobody wants to decide about them.'), ('Brian', '“The seat of the fire is not consistent with the account given.” That’s a sentence you notice.')],
   group(J(para('Non-disclosure', fontSize='large', fontFamily='display', style={'typography': {'fontWeight': '700', 'textTransform': 'uppercase'}}),
           para('When the prosecution holds material that could help the defence and doesn’t hand it over.')), className='is-style-board',
         style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))),
 ('The witness on Hedon Road', 'the-witness-on-hedon-road', 'wagstaffs-yard', 'road.jpg',
  'One man said he saw Lee Pryce walking away from the docks at ten past one. We read his statement, with the police redactions still in.',
  (W, 3, 6, 51, '',
   [(0, 'Previously'), (300, 'The statement'), (1150, 'Street lights on Hedon Road in 1994'), (2000, 'The witness today'), (2700, 'Lee listens back')],
   ['Witness statement, 2 June 1994, released with redactions in 2024.', 'Hull City Council street lighting records, 1993 to 1995.'],
   [('Maren', 'He asked us not to use his name, and we won’t. He still lives about a mile from the dock.')],
   quote('I saw a lad on Hedon Road at about ten past one. He had a <strong>green</strong> jacket on and he was walking fast towards <strong>Marfleet Lane</strong>.', 'Witness statement, 2 June 1994, as released', className='is-style-redacted'))),
 ('Lee', 'lee', 'wagstaffs-yard', 'station.jpg',
  'Lee Pryce was 22 when he was arrested. He is 54 now. He talks to us for the first time about the interview room.',
  (W, 2, 6, 57, 'Discussion of a suicide attempt in prison (31:20 to 34:05).',
   [(0, 'Previously'), (240, 'Meeting Lee in Goole'), (1100, 'The interview, 2 June 1994'), (1880, 'Prison, briefly'), (2600, 'What he wants now')],
   ['Police interview record, 2 June 1994, obtained by Lee’s solicitor.', 'Interviews with Lee Pryce, recorded April to June 2026.'],
   [('Lee', 'I said I was at my mam’s. My mam said I was at my mam’s. That was it, that was my alibi, and it wasn’t enough.')])),
 ('The night of 11 March 1994', 'the-night-of-11-march-1994', 'wagstaffs-yard', 'docks.jpg',
  'Start here. Arthur Kell’s daughter Janet tells us about her dad, and about the night the yard burned.',
  (W, 1, 6, 45, 'Discussion of a death in a fire.',
   [(0, 'Janet’s letter'), (420, 'Arthur'), (1300, 'The yard'), (2010, 'The phone call at 3am'), (2500, 'Why now')],
   ['Letter from Janet Kell to the show, May 2025.', 'Hull evening paper, 12 March 1994.'],
   [('Janet', 'He used to bring me the offcuts. I had a doll’s house made of Wagstaff’s timber.')])),
 ('A correction to part 3', 'a-correction-to-part-3', 'updates', 'newspaper.jpg',
  'We got a date wrong in part 3. Here is what we said, what is right, and what we changed.',
  None),
 ('Carol', 'carol', 'the-ferry-inn', 'phonebox.jpg',
  'The last part of season 1. Carol’s brother Mark reads the letter he wrote to her in 2017.',
  (F, 5, 5, 43, 'Discussion of a missing person and of grief.',
   [(0, 'Previously'), (500, 'What the police told Mark in 2024'), (1500, 'The letter'), (2200, 'What we still don’t know')],
   ['Humberside Police, letter to the Denby family, March 2024.', 'Interview with Mark Denby, recorded in Hessle, October 2025.'],
   [('Mark', 'She’d be 67. I keep doing that sum.')])),
 ('The last bus to Hessle', 'the-last-bus-to-hessle', 'the-ferry-inn', 'bridge.jpg',
  'Carol left the Ferry Inn at 10.40pm. Where did she go? A retired bus driver helps us check the timetable.',
  (F, 2, 5, 49, '',
   [(0, 'Previously'), (330, 'The 350'), (1210, 'The driver who called in'), (2120, 'The footpath by the bridge')],
   ['East Yorkshire Motor Services timetable, winter 1987, Hull History Centre.', 'Interview with Ray Halliday, retired bus driver, recorded October 2025.'],
   [('Ray', 'The 350 went at 10.52 from the Square. If she was on it, I’d have seen her. I wasn’t driving it that night, though.')])),
]
base = datetime.date(2026, 9, 24)
posts = []
for i, (title, slug, cat, img, ex, spec) in enumerate(EPS):
    d = base - datetime.timedelta(days=7 * i) if i < 5 else base - datetime.timedelta(days=7 * i + 220)
    p = {'title': title, 'slug': slug, 'category': cat, 'image': img, 'excerpt': ex, 'date': d.isoformat()}
    if spec is None:
        p['template'] = 'single-update'
        p['date'] = '2026-09-25'
        p['content'] = J(para('In part 3 we said the second fire report was dated 14 March 1994. It is dated 19 March. Maren read the date off a photocopy with a stamp over it.'),
                         para('It matters because on 14 March the police had not yet named anyone. By 19 March they had. The report was written after Lee Pryce became a suspect, and it still said the fire did not start where the police thought it did.'),
                         para('We have re-edited part 3 at 22:14 and corrected the transcript. The change is in the <a href="/sources-and-corrections/">corrections log</a>.'),
                         para('Thanks to Janet Kell, who checked the stamp with a magnifying glass.', fontSize='small'))
    else:
        case, part, of, mins, warn, ch, src, tr = spec[:8]
        extra = spec[8] if len(spec) > 8 else None
        p['content'] = ep(case, part, of, d.strftime('%A %-d %B %Y'), mins, warn, ch, src, tr, extra)
    posts.append(p)

demo = {
    'site': {'title': 'Low Water', 'tagline': 'True crime from the Humber estuary, built on the paperwork'},
    'categories': [{'slug': 'wagstaffs-yard', 'name': 'Wagstaff’s Yard', 'description': 'Season 2, 2026. A fire on the Hull docks in 1994, the night watchman who died, and the man who says he wasn’t there.'},
                   {'slug': 'the-ferry-inn', 'name': 'The Ferry Inn', 'description': 'Season 1, 2025. Carol Denby left a pub in Hessle on 2 November 1987 and was not seen again.'},
                   {'slug': 'updates', 'name': 'Updates', 'description': 'Corrections and news between parts.'}],
    'front_page': 'home', 'posts_page': 'episodes',
    'pages': [{'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'episodes', 'title': 'Episodes', 'content': ''},
              {'slug': 'cases', 'title': 'Cases', 'pattern': 'evidence/cases-page'},
              {'slug': 'sources-and-corrections', 'title': 'Sources and corrections', 'pattern': 'evidence/sources-page'},
              {'slug': 'about', 'title': 'How we report', 'pattern': 'evidence/about-page'},
              {'slug': 'support', 'title': 'Support', 'pattern': 'evidence/support-page'},
              {'slug': 'tips', 'title': 'Tips', 'pattern': 'evidence/tips-page'},
              {'slug': 'subscribe', 'title': 'Subscribe', 'pattern': 'evidence/subscribe-page'},
              {'slug': 'transcripts', 'title': 'Transcripts', 'pattern': 'evidence/transcripts-page'}],
    'posts': posts,
    'nav': [{'label': 'Episodes', 'url': '/episodes/'}, {'label': 'Cases', 'url': '/cases/'}, {'label': 'Sources and corrections', 'url': '/sources-and-corrections/'},
            {'label': 'How we report', 'url': '/about/'}, {'label': 'Support', 'url': '/support/'}, {'label': 'Tips', 'url': '/tips/'}],
}
os.makedirs('demos/evidence', exist_ok=True)
json.dump(demo, open('demos/evidence/content.json', 'w'), indent=1, ensure_ascii=False)
print('built evidence')
