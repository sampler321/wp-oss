# Design note (confidante, idea 047a: women-led conversation podcast)
# Direction: "kitchen-table magazine". Two women talking, set like a warm, loud women's-magazine spread, not a tech player page.
# Why: shows like this sell on the hosts' voices and on quotable lines, so the biggest thing on the page is a sentence someone said.
# Fonts: Yeseva One (display, the 047 face) at huge sizes for pulled quotes and episode numbers; Figtree for everything else.
# Palette: blush ground, oxblood text, tomato red for Ama, bottle green for Roisin (each host keeps her colour in transcripts and bios).
# Layout idea: a full-bleed tomato "overheard" quote opens the site; transcripts are two-colour conversations; host portraits sit in arches.
import sys, json, os, datetime
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('confidante')
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


# ---------------------------------------------------------------- tokens
PALETTE = [
    ('base', '#FBE4DC', 'Blush'), ('contrast', '#2B1215', 'Oxblood'), ('accent', '#AA2219', 'Tomato (Ama)'),
    ('accent-2', '#1E5B47', 'Bottle green (Roisin)'), ('surface', '#F5CDBF', 'Deep blush'), ('line', '#2B1215', 'Rule'),
    ('muted', '#6E3B37', 'Cocoa'), ('paper', '#FFF4EF', 'Paper'),
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

link_focus = {'outline': {'color': 'var:preset|color|contrast', 'offset': '3px', 'style': 'solid', 'width': '3px'}}
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '680px', 'wideSize': '1280px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE),
                  'duotone': [{'slug': 'oxblood-blush', 'colors': ['#2B1215', '#FBE4DC'], 'name': 'Oxblood and blush'}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': [disp, body],
            'fontSizes': [fs('x-small', '0.875rem', 'Caption'), fs('small', '1rem', 'Small'), fs('medium', '1.1875rem', 'Body'),
                          fs('large', '1.625rem', 'Large', '1.3rem'), fs('x-large', '2.5rem', 'Section', '1.9rem'),
                          fs('xx-large', '4.25rem', 'Title', '2.75rem'), fs('display', '8rem', 'Overheard', '3.4rem')],
        },
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2.2vw, 1.75rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2.25rem, 5.5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 9rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
        'custom': {'radius': {'image': '22px', 'button': '999px', 'box': '14px'}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': link_focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'lineHeight': '1.04', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'letterSpacing': '0'}},
            'button': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                       'border': {'radius': '999px', 'width': '0', 'style': 'solid'},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.8em', 'bottom': '0.8em', 'left': '1.5em', 'right': '1.5em'}},
                       ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}},
                       ':focus': link_focus},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'},
                                                      ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '700'}},
            'core/heading': {'elements': {'link': {'color': {'text': 'currentColor'}, 'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/image': {'border': {'radius': '22px'}},
            'core/post-featured-image': {'border': {'radius': '22px'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1.5px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.25'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '4px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.1'},
                               'border': {'width': '0'}},
            'core/details': {'color': {'background': 'var:preset|color|paper'}, 'border': {'radius': '14px'},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table.has-fixed-layout{table-layout:auto}& th{text-align:left;font-weight:700}& thead{border-bottom:1.5px solid var(--wp--preset--color--line)}& td,& th{padding:.7em .8em .7em 0;border:0;border-bottom:1px solid var(--wp--preset--color--surface)}&.is-style-stripes tbody tr:nth-child(odd){background:var(--wp--preset--color--paper)}&.is-style-stripes td:first-child{padding-left:.8em}&.is-style-stripes{border-bottom:0}'},
            'core/search': {'border': {'radius': '999px'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
            'core/audio': {'css': '& audio{width:100%;min-width:0}& figcaption{text-align:left}'},
            'core/list': {'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
        },
        'css': ('.wp-block-column>.wp-block-group:only-child{height:100%}:where(h1,h2,h3,.has-display-font-size){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                'body{font-synthesis:none;font-variant-numeric:tabular-nums lining-nums}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--contrast);outline-offset:3px}'
                ':where(.wp-block-post-content)>:where(h2,h3){margin-top:var(--wp--preset--spacing--60)}'
                'details>summary{cursor:pointer;font-weight:700}details[open]>summary{margin-bottom:var(--wp--preset--spacing--30)}'
                '@media (prefers-reduced-motion:no-preference){a{transition:color .15s}}'),
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'break-notice', 'title': 'Recording break notice'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
                        {'name': 'single-letter', 'title': 'Listener letter episode', 'postTypes': ['post']}],
}
_t = theme['styles']['blocks'].get('core/table', {}).pop('css', None)
if _t:
    theme['styles']['css'] += _t.replace('& ', '.wp-block-table ').replace('&.', '.wp-block-table.')
for _b_ in theme['styles']['blocks'].values():
    if 'css' in _b_:
        _b_['css'] = split_css(_b_['css'])
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

# ---------------------------------------------------------------- style variations
def variation(title, p, extra=None):
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(p)}}}
    if extra:
        d['styles'] = extra
    return json.dumps(d, indent='\t', ensure_ascii=False)

write('styles/late-night.json', variation('Late night', [
    ('base', '#2B1215', 'Blush'), ('contrast', '#FBE4DC', 'Oxblood'), ('accent', '#FF8A73', 'Tomato (Ama)'),
    ('accent-2', '#7FD3B0', 'Bottle green (Roisin)'), ('surface', '#3D1C1F', 'Deep blush'), ('line', '#FBE4DC', 'Rule'),
    ('muted', '#E2B7AC', 'Cocoa'), ('paper', '#361719', 'Paper')]))
write('styles/mint-tea.json', variation('Mint tea', [
    ('base', '#DDEFE4', 'Blush'), ('contrast', '#10261D', 'Oxblood'), ('accent', '#A12A1D', 'Tomato (Ama)'),
    ('accent-2', '#1D5A45', 'Bottle green (Roisin)'), ('surface', '#C4E3D1', 'Deep blush'), ('line', '#10261D', 'Rule'),
    ('muted', '#34574A', 'Cocoa'), ('paper', '#F1FAF4', 'Paper')]))
write('styles/talk.json', variation('Talk', [
    ('base', '#FFFFFF', 'Blush'), ('contrast', '#141414', 'Oxblood'), ('accent', '#D1241A', 'Tomato (Ama)'),
    ('accent-2', '#0F5A8A', 'Bottle green (Roisin)'), ('surface', '#F1EFEC', 'Deep blush'), ('line', '#141414', 'Rule'),
    ('muted', '#555049', 'Cocoa'), ('paper', '#F7F6F4', 'Paper')]))

# ---------------------------------------------------------------- section styles
def section(slug, title, types, styles):
    if 'css' in styles:
        styles = dict(styles, css=split_css(styles['css']))
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                                        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))

inv_links = {'link': {'color': {'text': 'currentColor'}, ':hover': {'color': {'text': 'currentColor'}}},
             'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
                        ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}}}}
section('tomato', 'Tomato (Ama)', ['core/group', 'core/columns', 'core/column'],
        {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'elements': inv_links})
section('bottle', 'Bottle green (Roisin)', ['core/group', 'core/columns', 'core/column'],
        {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|base'}, 'elements': inv_links})
section('oxblood', 'Oxblood', ['core/group'],
        {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}, 'elements': inv_links})
section('deep-blush', 'Deep blush', ['core/group', 'core/columns', 'core/column'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'border': {'radius': '14px'}})
section('band', 'Blush band', ['core/group'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}})
section('paper-box', 'Paper box', ['core/group'],
        {'color': {'background': 'var:preset|color|paper', 'text': 'var:preset|color|contrast'}, 'border': {'radius': '14px'},
         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('arch', 'Arch', ['core/image', 'core/post-featured-image'],
        {'css': '& img{border-radius:999px 999px 22px 22px;aspect-ratio:4/5;object-fit:cover;width:100%}'})
section('square', 'Square artwork', ['core/image', 'core/post-featured-image'],
        {'css': '& img{aspect-ratio:1;object-fit:cover;width:100%;border-radius:14px}'})
section('avatar-small', 'Small round portrait', ['core/image'],
        {'css': '&{flex:0 0 auto;margin:0!important}& img{width:56px;height:56px;aspect-ratio:1;object-fit:cover;border-radius:50%}'})
section('avatar', 'Round portrait', ['core/image'],
        {'css': '& img{aspect-ratio:1;object-fit:cover;border-radius:50%;width:100%}'})
section('speaker-a', 'Speaker: Ama', ['core/paragraph'],
        {'border': {'left': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}},
         'spacing': {'padding': {'left': 'var:preset|spacing|30'}}, 'css': '& strong{color:var(--wp--preset--color--accent)}'})
section('speaker-b', 'Speaker: Roisin', ['core/paragraph'],
        {'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '3px', 'style': 'solid'}},
         'spacing': {'padding': {'left': 'var:preset|spacing|30'}}, 'css': '& strong{color:var(--wp--preset--color--accent-2)}'})
section('speaker-guest', 'Speaker: guest', ['core/paragraph'],
        {'border': {'left': {'color': 'var:preset|color|muted', 'width': '3px', 'style': 'dotted'}},
         'spacing': {'padding': {'left': 'var:preset|spacing|30'}}})
section('chapters', 'Chapter list', ['core/list'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding-left:0!important}& li{display:flex;gap:1rem;padding:.55rem 0;border-top:1.5px solid var(--wp--preset--color--line)}& li:last-child{border-bottom:1.5px solid var(--wp--preset--color--line)}& li a{min-width:3.6rem;font-weight:700;text-decoration:none}& li a:hover{text-decoration:underline}'})
section('content-note', 'Content note', ['core/paragraph'],
        {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'},
         'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'border': {'radius': '14px'},
         'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}}})
section('episode-row', 'Episode row', ['core/group'],
        {'border': {'top': {'color': 'var:preset|color|line', 'width': '1.5px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})
section('topic-list', 'Topic list', ['core/categories'],
        {'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.5rem}& li a{display:inline-block;padding:.35rem .9rem;border:1.5px solid currentColor;border-radius:999px;text-decoration:none}& li a:hover{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'})
section('listen-row', 'Listen links', ['core/list'],
        {'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding:0!important;display:flex;flex-wrap:wrap;gap:.4rem 1.4rem}& li a{text-decoration-thickness:1.5px;text-underline-offset:.25em}'})

# ---------------------------------------------------------------- content helpers
A1 = 'https://upload.wikimedia.org/wikipedia/commons/a/a0/The_Mercury_13_%28As_Told_By_U.S._Chief_Technology_Officer_Megan_Smith%29.ogg'
A2 = 'https://upload.wikimedia.org/wikipedia/commons/1/13/Sally_Ride_%28As_Told_By_NASA_Chief_Scientist_Dr._Ellen_Stofan%29.ogg'
A1_CAP = 'Stand-in audio: "The Mercury 13", told by Megan Smith for the White House (public domain). Swap in your episode file.'
A2_CAP = 'Stand-in audio: "Sally Ride", told by Dr Ellen Stofan for the White House (public domain). Swap in your episode file.'

def ts(sec):
    return '%02d:%02d' % (sec // 60, sec % 60) if sec < 3600 else '%d:%02d:%02d' % (sec // 3600, sec % 3600 // 60, sec % 60)

def chapters(audio_url, items):
    return lst(['<a href="%s#t=%d">%s</a> %s' % (audio_url, s, ts(s), t) for s, t in items], className='is-style-chapters')

def listen_row():
    return lst(['<a href="https://podcasts.apple.com/">Apple Podcasts</a>', '<a href="https://open.spotify.com/">Spotify</a>',
                '<a href="https://pocketcasts.com/">Pocket Casts</a>', '<a href="https://overcast.fm/">Overcast</a>',
                '<a href="https://www.youtube.com/">YouTube</a>', '<a href="/feed/">RSS</a>'], className='is-style-listen-row')

def say(who, text):
    cls = {'Ama': 'is-style-speaker-a', 'Roisin': 'is-style-speaker-b'}.get(who, 'is-style-speaker-guest')
    return para('<strong>%s</strong> %s' % (who, text), className=cls)

# ---------------------------------------------------------------- patterns
pattern('overheard-hero', 'Overheard: a line from this week, full width', 'featured', group(group(J(
    para('Ama, episode 63', fontSize='small', style={'typography': {'fontWeight': '700'}}),
    para('“I earn more than my dad ever did, and I still check my balance before I buy a coffee.”', fontSize='display', fontFamily='display',
         style={'typography': {'lineHeight': '0.98'}}),
    row(J(buttons(('Play episode 63', '/asking-for-more-money/'), ('All episodes', '/episodes/', {'className': 'is-style-outline'})),
          para('Every Tuesday, about 50 minutes', fontSize='small')), justify='space-between')), align='wide', layout={'type': 'default'}, style={'spacing': {'blockGap': 'var:preset|spacing|50'}}),
    align='full', className='is-style-tomato',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|60'}, 'blockGap': 'var:preset|spacing|50', 'margin': {'top': '0'}}}),
    description='The signature opener: one sentence from the latest episode, set as big as it will go. Change it every week.')

pattern('latest-episode', 'Latest episode with player', 'featured,audio', columns(
    ('40%', image('ep-money.jpg', 'Ceramic piggy banks shaped like a cow, an elephant and two pigs on a supermarket shelf, with price tags', className='is-style-arch')),
    ('60%', J(
        para('New this week, 52 minutes, filed under Money', fontSize='small', style={'typography': {'fontWeight': '700'}}),
        heading('<a href="/asking-for-more-money/">63. Asking for more money</a>', 2, fontSize='xx-large'),
        para('Ama asked for a pay rise in March and got a “let’s revisit in the autumn”. It is now the autumn. We go through her notes line by line with Folake Adeyemi, who has sat on the other side of that table for 15 years.'),
        para('Content note: frank talk about debt and one bereavement (from 31:40).', className='is-style-content-note'),
        audio(A1, A1_CAP),
        listen_row())),
    align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|40'}, 'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('listen-on', 'Listen on (apps and RSS)', 'call-to-action', J(
    heading('Listen wherever you already listen', 3), listen_row(),
    para('Or paste this into any podcast app: <strong>saymore.example/feed</strong>', fontSize='x-small')))

ep_row = group(J(
    dyn('post-title', isLink=True, level=3, fontSize='x-large'),
    row(J(dyn('post-terms', term='category', separator=', '), dyn('post-date', format='j F Y')), style={'spacing': {'blockGap': 'var:preset|spacing|30'}})),
    className='is-style-episode-row', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between', 'verticalAlignment': 'bottom'})

pattern('episode-list', 'Recent episodes (numbered list)', 'posts,query', group(J(
    row(J(heading('Recent episodes', 2), para('<a href="/episode-index/">Every episode on one page</a>', fontSize='small')), justify='space-between', align='wide'),
    query(ep_row, per_page=7, align='wide')), align='wide', layout={'type': 'default'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|60'}}}), keywords='episodes, list, archive')

pattern('episode-list-archive', 'Episode list (inherits the page query)', 'posts,query', inherit_query(ep_row, align='wide'), inserter=False)

pattern('hosts', 'Hosts, side by side', 'team,about', columns(
    (None, J(image('host-1.jpg', 'Ama Boateng laughing on a porch, wearing a pink top and a silver necklace', className='is-style-arch'),
             heading('Ama Boateng', 3, textColor='accent'),
             para('Ran HR at a housing association for eleven years, now does payroll for a theatre. Lives in Levenshulme with her partner and a cat called Cedric. Keeps a spreadsheet of everything, including the show.'))),
    (None, J(image('host-2.jpg', 'Roisin Keane laughing in front of a whitewashed window, in a black band t-shirt and denim shorts', className='is-style-arch'),
             heading('Roisin Keane', 3, textColor='accent-2'),
             para('Physio from Derry, in Manchester since 2015. Swims at Arcadia three mornings a week and will tell you about it. Hates a voice note, sends them anyway.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('dear-say-more', 'Dear Say More: a listener letter', 'call-to-action,text', group(J(
    columns(('38%', heading('Dear Say More', 2, fontSize='xx-large')),
            ('62%', J(para('“My sister borrowed £4,000 for a deposit two years ago. She’s just booked a week in Crete. Do I say something or do I let it go?”', fontSize='large', fontFamily='display'),
                     para('Hannah, Stockport. We answered this one in episode 59, and Roisin changed her mind halfway through.', fontSize='small'),
                     buttons(('Send us your question', '/write-to-us/')))), align='wide')),
    align='full', className='is-style-bottle',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'margin': {'top': '0'}}}))

pattern('topics', 'Four topics', 'text,posts', group(J(
    heading('What we talk about', 2),
    para('Four things, over and over, because they never stop being complicated.'),
    dyn('categories', className='is-style-topic-list', showPostCounts=False)), align='wide', layout={'type': 'default'}))

pattern('content-note', 'Content note line', 'text,audio', para('Content note: this episode talks about pregnancy loss (12:05 to 19:40). The chapter list lets you skip it.', className='is-style-content-note'),
        description='A plain warning under the player. Say what it is and where it is, so people can skip.')

pattern('chapters-list', 'Chapters with timestamps', 'text,audio', J(
    heading('Chapters', 3),
    chapters(A1, [(0, 'Hello, and what Roisin had for breakfast'), (190, 'The email Ama sent in March'), (820, 'Folake on salary bands'),
                  (1510, 'Writing the one-page case'), (1900, 'Debt, and why it was hard to say out loud'), (2710, 'What happened on Thursday')]),
    para('Timestamps open the audio file at that point. In most podcast apps the chapters are built in.', fontSize='x-small', textColor='muted')),
    description='Each time links to the audio file with a #t= fragment, which starts playback there in the browser.')

pattern('show-notes', 'Show notes with links', 'text', J(
    heading('Show notes', 3),
    lst(['<a href="https://www.gov.uk/employment-rights-pay">GOV.UK on pay and your rights</a>, the page Folake made us read out.',
         '<a href="https://www.acas.org.uk/">Acas</a> has a free helpline for workplace questions: 0300 123 1100.',
         'The salary survey Ama used came from her union. If you are in one, ask yours.',
         'Roisin’s pool timetable is on the Arcadia website and she would like you to stop taking lane 3.'])))

pattern('transcript', 'Transcript in a fold', 'text,audio', J(
    heading('Transcript', 3),
    details('Read the full transcript', J(
        say('Ama', 'Right. We’re recording. Roisin, you’ve got a face on.'),
        say('Roisin', 'I have not got a face on. This is my face.'),
        say('Ama', 'So. The pay rise. I promised I’d report back and I’m reporting back.'),
        say('Folake', 'Can I ask what you actually wrote? Word for word, if you have it.'),
        say('Ama', 'I have it. I have everything. “Hi Mark, I’d like to discuss my salary at my review.” That was it.'),
        say('Folake', 'That’s fine as an opener. The problem is nothing came after it.'),
        para('Transcripts are made with software and checked by Roisin, who is slow but thorough. Spot a mistake? Email transcripts@saymore.example.', fontSize='x-small', textColor='muted'))),
    para('<a href="/transcripts/">All transcripts, including large-print PDFs</a>', fontSize='small')),
    description='Speakers keep their colour: Ama in tomato, Roisin in green, guests with a dotted rule.')

pattern('guest-card', 'Guest card', 'team', group(J(
    para('This week’s guest', fontSize='x-small', style={'typography': {'fontWeight': '700'}}),
    heading('Folake Adeyemi', 3),
    para('Payroll auditor and union rep in Salford. Has negotiated around 400 pay reviews, most of them for other people. Runs a Tuesday-night drop-in at the library on Chapel Street.'),
    para('<a href="https://www.instagram.com/">@folake.counts</a> on Instagram', fontSize='small')), className='is-style-deep-blush',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('phrase-of-the-week', 'Phrase of the week', 'text', group(J(
    para('Phrase of the week', fontSize='small', style={'typography': {'fontWeight': '700'}}),
    para('Salary band', fontSize='xx-large', fontFamily='display', style={'typography': {'lineHeight': '1'}}),
    para('The range a company has already agreed to pay for a job. Ask for it before the interview. If they won’t say, that tells you something too.')),
    className='is-style-paper-box'), description='A small glossary box. One word or phrase from the episode, explained plainly.')

pattern('sponsor-read', 'Sponsor read with code', 'call-to-action', group(J(
    para('This episode is supported by', fontSize='x-small', style={'typography': {'fontWeight': '700'}}),
    heading('Bread & Butter, Chorlton', 4),
    para('A bakery on Beech Road that delivers on Fridays across south Manchester. Use the code <strong>SAYMORE</strong> for £5 off your first loaf box. Ama gets the seeded rye. Roisin says the rye is too serious.'),
    para('We only read ads for things one of us has paid for with our own money.', fontSize='x-small', textColor='muted')),
    className='is-style-paper-box'))

pattern('support-tiers', 'Support tiers', 'call-to-action,services', J(
    heading('Chip in', 2),
    para('The show pays for itself through two ad slots and the people below. Everything goes through Patreon and you can stop any month.'),
    columns(*[(None, group(J(para(n, fontSize='small', style={'typography': {'fontWeight': '700'}}), para(pr, fontSize='xx-large', fontFamily='display', style={'typography': {'lineHeight': '1'}}),
                              para('a month', fontSize='small'), para(t)), className=c,
                              style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))
              for n, pr, t, c in [('Friend of the show', '£3', 'The ad-free feed, out at the same time as everyone else’s.', 'is-style-deep-blush'),
                                  ('Regular', '£6', 'Ad-free feed, plus a bonus episode on the last Friday of the month.', 'is-style-tomato'),
                                  ('Front row', '£12', 'All of that, two live tapings a year in Manchester and your name in the credits.', 'is-style-bottle')]],
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|30'}}}),
    buttons(('Join on Patreon', 'https://www.patreon.com/'), ('Buy us one coffee instead', 'https://ko-fi.com/', {'className': 'is-style-outline'}))))

pattern('sponsor-us', 'Advertise on the show', 'services', J(
    heading('Advertising', 3),
    para('Two slots per episode, read by one of us, recorded fresh. £240 per slot for four episodes. We sell six months ahead, so write in by the first of the month.'),
    para('We don’t take ads from diet brands, payday lenders, betting companies or anyone selling supplements. Please don’t ask.'),
    para('<a href="mailto:ads@saymore.example">ads@saymore.example</a>')))

pattern('break-notice', 'Notice: recording break', 'banner', group(
    para('We’re off for half term. New episodes are back on Tuesday 3 November. The back catalogue is all still there.', fontSize='small', style={'typography': {'fontWeight': '700'}}),
    className='is-style-tomato', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='A bar for a hiatus. Put the date you are back in it and remove the bar on that day.')

pattern('live-taping', 'Live taping notice', 'call-to-action', columns(
    ('60%', J(heading('Come and watch us record', 2),
              para('Thursday 26 November, 7.30pm, at the Klondyke Club in Levenshulme. £8, or free for the front-row tier. We’ll take questions from the room, which is always a mistake.'))),
    ('40%', J(buttons(('Get a ticket', 'https://www.ticketsource.co.uk/')), para('Step-free entry through the side door on Burnage Range. BSL interpreter booked.', fontSize='small'))),
    align='wide', className='is-style-deep-blush', style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}}))

pattern('transcript-download', 'Transcript download', 'text', para('Transcript: <a href="/transcripts/">read on the site</a> or download the large-print PDF (18 pages).', fontSize='small'))

pattern('episode-index-table', 'Episode index by season', 'text', J(
    heading('Season 3 (2026)', 3),
    table([['63', '<a href="/asking-for-more-money/">Asking for more money</a>', 'Money', '52 min'],
           ['62', '<a href="/the-friend-who-moved-to-lisbon/">The friend who moved to Lisbon</a>', 'Friendship', '47 min'],
           ['61', '<a href="/swimming-through-the-menopause/">Swimming through the menopause</a>', 'Bodies', '55 min'],
           ['60', '<a href="/leaving-the-job-youre-good-at/">Leaving the job you’re good at</a>', 'Work', '49 min'],
           ['59', '<a href="/my-sister-owes-me-4000/">Dear Say More: my sister owes me £4,000</a>', 'Letters', '38 min'],
           ['58', '<a href="/deciding-about-kids-at-38/">Deciding about kids at 38</a>', 'Bodies', '61 min'],
           ['57', '<a href="/who-pays-for-the-hen-do/">Who pays for the hen do</a>', 'Money', '44 min'],
           ['56', '<a href="/tea-with-our-mums/">Tea with our mums</a>', 'Friendship', '58 min']],
          head=['No.', 'Episode', 'Topic', 'Length']),
    heading('Seasons 1 and 2 (2024 to 2025)', 3),
    para('Episodes 1 to 55 are in every podcast app and in the <a href="/episodes/">episode list</a>. The first ten were recorded on a phone in Ama’s kitchen. We have left them as they are.')))

pattern('episode-index-page', 'Page: episode index', 'text', J(
    para('One line per episode, newest first. Transcripts are linked from each episode page.', fontSize='large'),
    pattern_ref('episode-index-table')), block_types='core/post-content')

pattern('hosts-page', 'Page: hosts and the show', 'about', J(
    pattern_ref('hosts'),
    group(J(heading('How the show started', 2),
        para('We met in 2019 at an antenatal class that neither of us needed. Ama was there with her sister, Roisin was there with a friend. We went for a drink after and talked until the pub shut.'),
        para('Say More started in January 2024 with a phone propped on a fruit bowl. We record on Sunday afternoons at Ama’s kitchen table in Levenshulme, edit on Monday night and put it out on Tuesday at 6am.'),
        para('We talk about work, bodies, money and friendship, because those are the things we text each other about. Neither of us is an expert. When a question needs one, we ask one in.'),
        para('We don’t give medical, legal or financial advice. If you need that, the show notes have somewhere to start.')),
        style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}}}),
    pattern_ref('season-intro'), pattern_ref('recommendations'), pattern_ref('live-dates'), pattern_ref('live-taping')), block_types='core/post-content')

pattern('subscribe-page', 'Page: subscribe', 'call-to-action', J(
    para('New episodes come out every Tuesday at 6am UK time. Pick the app you already use.', fontSize='large'),
    table([['<a href="https://podcasts.apple.com/">Apple Podcasts</a>', 'iPhone, iPad, Mac', 'Tap Follow, then turn on automatic downloads'],
           ['<a href="https://open.spotify.com/">Spotify</a>', 'Everywhere', 'Tap the bell to get a notification'],
           ['<a href="https://pocketcasts.com/">Pocket Casts</a>', 'Android and iPhone', 'Our favourite, for the record'],
           ['<a href="https://overcast.fm/">Overcast</a>', 'iPhone', 'Voice Boost helps on the older episodes'],
           ['<a href="https://www.youtube.com/">YouTube</a>', 'Browser and TV', 'Audio with a still picture, and captions'],
           ['<a href="/feed/">RSS feed</a>', 'Any podcast app', 'Paste the link into your app’s “add by URL” box']],
          head=['Where', 'Works on', 'Tip']),
    group(J(heading('The ad-free feed', 3),
        para('Supporters get a private feed with no ads. Patreon sends you a link that works in Apple Podcasts, Pocket Casts and Overcast. Spotify can’t play private feeds yet.'),
        buttons(('See the support tiers', '/support/'))), className='is-style-paper-box'),
    pattern_ref('newsletter')), block_types='core/post-content')

pattern('support-page', 'Page: support and sponsors', 'call-to-action', J(
    pattern_ref('support-tiers'), pattern_ref('sponsor-us'), pattern_ref('sponsor-read')), block_types='core/post-content')

pattern('write-to-us-page', 'Page: write to us', 'contact', J(pattern_ref('voice-notes'),
    para('We read every letter out loud to each other on a Sunday. About one in ten ends up on the show.', fontSize='large'),
    heading('How to send one', 3),
    lst(['Email <a href="mailto:dear@saymore.example">dear@saymore.example</a>. A paragraph is plenty.',
         'Tell us your first name and your town, or ask us to change them. We always change details that could identify someone else.',
         'Voice notes are welcome, up to two minutes. We only play them on air if you say yes in writing.'], ordered=True),
    heading('What we won’t do', 3),
    para('We won’t answer medical or legal questions on air, and we won’t read out letters about someone who could recognise themselves without their say-so.'),
    pattern_ref('dear-say-more-quotes')), block_types='core/post-content')

pattern('dear-say-more-quotes', 'Listener letters (short quotes)', 'testimonials', columns(
    (None, quote('I listened to the pay rise one in the car park before my review and went in with a number. Got most of it.', 'Priya, Bolton, October 2026')),
    (None, quote('Thank you for saying “I don’t know” out loud on episode 58. I thought everyone else knew.', 'Megan, Cardiff, September 2026')),
    align='wide'))

pattern('transcripts-page', 'Page: transcripts', 'text', J(
    para('Every episode has a transcript on its page, under the show notes. Large-print PDFs are listed below and take about a week to appear.', fontSize='large'),
    table([['63', 'Asking for more money', '<a href="/asking-for-more-money/">On the page</a>', 'Coming Tuesday'],
           ['62', 'The friend who moved to Lisbon', '<a href="/the-friend-who-moved-to-lisbon/">On the page</a>', 'PDF, 16 pages'],
           ['61', 'Swimming through the menopause', '<a href="/swimming-through-the-menopause/">On the page</a>', 'PDF, 19 pages'],
           ['60', 'Leaving the job you’re good at', '<a href="/leaving-the-job-youre-good-at/">On the page</a>', 'PDF, 17 pages']],
          head=['No.', 'Episode', 'Web', 'Large print']),
    para('If you need a transcript in another format, email transcripts@saymore.example and Roisin will sort it.', fontSize='small')),
    block_types='core/post-content')

pattern('newsletter', 'Newsletter', 'call-to-action', group(J(
    heading('One email on Tuesdays', 3),
    para('The new episode, the links from the show notes, and whatever Ama put in the group chat that week. Nothing else.'),
    buttons(('Sign up by email', 'mailto:hello@saymore.example?subject=Tuesday%20email'))), className='is-style-deep-blush', anchor='newsletter',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))

pattern('guest-pitch', 'Be a guest (how to pitch)', 'contact', J(
    heading('Want to come on?', 3),
    para('We have one guest a month, usually someone who does the thing we are confused about. We don’t book authors on book tours or anyone with a product launch that week.'),
    para('Send two lines about you and one question you think we would get wrong: <a href="mailto:guests@saymore.example">guests@saymore.example</a>')))

pattern('faq', 'Questions people ask', 'text', J(
    heading('Questions people ask', 2),
    details('Are you two actually friends?', para('Yes. Since 2019. We fall out about once a season, usually on air.')),
    details('Why did you stop the video version?', para('Nobody watched it and Roisin had to wear mascara on a Sunday.')),
    details('Can I use a clip for my class or group?', para('Yes, up to five minutes, with a credit and a link. Email us if it’s for anything paid.')),
    details('Is there a transcript?', para('Every episode, on its own page. <a href="/transcripts/">Large-print PDFs are here.</a>'))))

pattern('episode-full', 'Episode: full layout (player, chapters, notes, transcript)', 'audio,featured', J(
    audio(A1, A1_CAP), pattern_ref('content-note'), pattern_ref('chapters-list'), pattern_ref('show-notes'),
    pattern_ref('guest-card'), pattern_ref('phrase-of-the-week'), pattern_ref('sponsor-read'), pattern_ref('transcript')),
    block_types='core/post-content', description='Everything an episode page needs, in the order people use it.')

# ---------------------------------------------------------------- round 2: images, a smaller quote, more of the kit
def avatar(img, alt, small=False, **kw):
    return image(img, alt, className='is-style-avatar-small' if small else 'is-style-avatar', **kw)

pattern('latest-hero', 'Latest episode first: artwork, title, player', 'featured,audio', columns(
    ('44%', image('ep-money.jpg', 'Ceramic piggy banks shaped like a cow, an elephant and two pigs on a supermarket shelf, with price tags', caption='Episode 63 artwork', className='is-style-square')),
    ('56%', J(
        para('New this Tuesday, episode 63, 52 minutes', fontSize='small', style={'typography': {'fontWeight': '700'}}),
        heading('<a href="/asking-for-more-money/">Asking for more money</a>', 1, fontSize='xx-large'),
        para('Ama asked for a pay rise in March and got a “let’s revisit in the autumn”. It is now the autumn. Folake Adeyemi, who has sat on the other side of that table for 15 years, goes through Ama’s notes line by line.', fontSize='large'),
        para('Content note: frank talk about debt and one bereavement (from 31:40).', className='is-style-content-note'),
        audio(A1, A1_CAP), listen_row(), pattern_ref('host-avatars'))),
    align='wide', verticalAlignment='center', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'blockGap': {'left': 'var:preset|spacing|60'}}}),
    description='The home page opens on the newest episode: square artwork, title, player and who is on it.')

pattern('host-avatars', 'Who is on this episode (portraits)', 'team', row(J(
    avatar('host-1.jpg', 'Ama Boateng, smiling, in a pink top', lightbox=False, small=True),
    avatar('host-2.jpg', 'Roisin Keane, laughing, in a black t-shirt', lightbox=False, small=True),
    avatar('guest-2.jpg', 'Folake Adeyemi, smiling, in a red jumper', lightbox=False, small=True),
    para('Ama, Roisin and guest <strong>Folake Adeyemi</strong>', fontSize='small')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}))

pattern('overheard-photo', 'Overheard: a line from this week, with the speaker', 'featured,testimonials', group(columns(
    ('26%', image('host-1.jpg', 'Ama Boateng laughing on a porch, in a pink top', className='is-style-arch', lightbox=False)),
    ('74%', J(para('Overheard in episode 63', fontSize='small', style={'typography': {'fontWeight': '700'}}),
              para('“I earn more than my dad ever did, and I still check my balance before I buy a coffee.”', fontSize='x-large', fontFamily='display', style={'typography': {'lineHeight': '1.1'}}),
              para('Ama Boateng, 23 minutes in', fontSize='small'),
              buttons(('Play from 23:10', A1 + '#t=1390'), ('All episodes', '/episodes/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    align='full', className='is-style-tomato',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'margin': {'top': '0'}}}),
    description='One line from the week, at a readable size, next to the person who said it.')

ep_card = group(J(
    dyn('post-featured-image', isLink=True, aspectRatio='1', className='is-style-square'),
    row(J(dyn('post-terms', term='category', separator=', '), dyn('post-date', format='j M Y')), style={'spacing': {'blockGap': 'var:preset|spacing|20'}}),
    dyn('post-title', isLink=True, level=3, fontSize='large')), layout={'type': 'default'}, style={'spacing': {'blockGap': 'var:preset|spacing|20'}})

pattern('episode-cards', 'Recent episodes with artwork', 'posts,query', group(J(
    row(J(heading('Recent episodes', 2), para('<a href="/episode-index/">Every episode on one page</a>', fontSize='small')), justify='space-between'),
    query(ep_card, per_page=8, query_id=5, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '9.5rem'})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}))

pattern('episode-cards-archive', 'Episodes with artwork (inherits the page query)', 'posts,query',
        inherit_query(ep_card, layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '9.5rem'}, align='wide'), inserter=False)

GUESTS = [('guest-2.jpg', 'Folake Adeyemi smiling in a red jumper', 'Folake Adeyemi', 'Payroll auditor and union rep, Salford', 'asking-for-more-money', 'Asking for more money'),
          ('guest-3.jpg', 'Dr Nadia Rahman lying on a concrete step in a patterned coat, looking at the camera', 'Dr Nadia Rahman', 'GP in Longsight', 'swimming-through-the-menopause', 'Swimming through the menopause'),
          ('guest-1.jpg', 'Black and white portrait of Hannah with glitter stars on one cheek', 'Hannah, Stockport', 'Wrote in about her sister', 'my-sister-owes-me-4000', 'My sister owes me £4,000')]

pattern('guest-strip', 'Guests, with portraits', 'team', group(J(
    heading('Recent guests', 2),
    columns(*[(None, J(image(i, a, className='is-style-arch'), heading(n, 4), para(w, fontSize='small'), para('<a href="/%s/">%s</a>' % (s, t), fontSize='small'))) for i, a, n, w, s, t in GUESTS],
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}))

pattern('guest-quote', 'Guest quote with portrait', 'testimonials', columns(
    ('22%', avatar('guest-3.jpg', 'Dr Nadia Rahman lying on a concrete step in a patterned coat', lightbox=False)),
    ('78%', J(para('“The first thing people tell me is that they thought they were going mad. They weren’t.”', fontSize='large', fontFamily='display'),
              para('Dr Nadia Rahman, GP, in episode 61', fontSize='small'))),
    verticalAlignment='center', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}))

pattern('season-intro', 'Season introduction', 'text', group(columns(
    ('40%', heading('Season 3', 2, fontSize='xx-large')),
    ('60%', J(para('Twelve episodes, September to December. More guests this time, one live taping in November, and an episode where our mums take over the microphones.', fontSize='large'),
              para('<a href="/episode-index/">The full episode list</a>', fontSize='small')))),
    className='is-style-deep-blush', style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}}))

pattern('recommendations', 'What we’re into this week', 'text', J(
    heading('What we’re into', 3),
    lst(['Ama: <em>Big Friendship</em> by Aminatou Sow and Ann Friedman, for the third time.', 'Roisin: the 7am women-only swim at Arcadia, Wednesdays.',
         'Both of us: the bakery on Beech Road that sponsors us, and we’d say so anyway.'])))

pattern('voice-notes', 'Listener voice notes', 'audio,testimonials', J(
    heading('Voice notes from you', 3),
    para('Played on air with permission. Send yours to dear@saymore.example, two minutes at most.', fontSize='small'),
    columns((None, J(audio(A2, 'Megan in Cardiff, on episode 58. Stand-in audio.'))), (None, J(audio(A1, 'Priya in Bolton, on the pay-rise episode. Stand-in audio.'))))))

pattern('live-dates', 'Live dates', 'text', J(
    heading('Live dates', 3),
    lst(['<strong>Thursday 26 November</strong>, Klondyke Club, Levenshulme. Recording episode 72. £8.', '<strong>Saturday 23 January</strong>, Leeds Library, as part of the book festival. Free, book ahead.']),
    buttons(('Get a ticket', 'https://www.ticketsource.co.uk/'))))

pattern('guests-page', 'Page: guests', 'team', J(
    para('One guest a month, usually someone who does the thing we are confused about. These are the most recent.', fontSize='large'),
    pattern_ref('guest-strip'), pattern_ref('guest-quote'), pattern_ref('guest-pitch')), block_types='core/post-content')

pattern('front-page-layout', 'Home: latest episode, overheard, episodes, guests, hosts', 'featured', J(
    pattern_ref('latest-hero'), pattern_ref('overheard-photo'), pattern_ref('episode-cards'), pattern_ref('guest-strip'), pattern_ref('dear-say-more'),
    columns(('30%', J(heading('Who’s talking', 2, fontSize='xx-large'),
                      para('Two friends at a kitchen table in Levenshulme. One keeps spreadsheets, one sends voice notes. We record on Sunday afternoons and it goes out on Tuesday at 6am.'),
                      para('<a href="/hosts/">How the show started</a>', fontSize='small'))),
            ('70%', pattern_ref('hosts')), align='wide',
            style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|60'}, 'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('topics')), inserter=False)

pattern('episode-sidebar', 'Episode sidebar: hosts and listening', 'audio', J(
    group(J(para('Your hosts', fontSize='x-small', style={'typography': {'fontWeight': '700'}}),
            para('<strong>Ama Boateng</strong> and <strong>Roisin Keane</strong>, from a kitchen table in Levenshulme.', fontSize='small'),
            para('<a href="/hosts/">About the show</a>', fontSize='small')), className='is-style-paper-box'),
    group(J(para('Listen in an app', fontSize='x-small', style={'typography': {'fontWeight': '700'}}), listen_row()), className='is-style-paper-box'),
    group(J(para('No ads, bonus episodes', fontSize='x-small', style={'typography': {'fontWeight': '700'}}),
            para('From £3 a month. <a href="/support/">Support the show</a>', fontSize='small')), className='is-style-paper-box')), inserter=False)

# ---------------------------------------------------------------- parts
write('parts/header.html', group(row(J(
    dyn('site-title', level=0),
    row(J(dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'}),
          buttons(('Listen', '/subscribe/'))), justify='right', style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
    justify='space-between', align='wide'), tag='header', align='full',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
           'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1.5px', 'style': 'solid'}}}))

write('parts/footer.html', group(J(
    columns(('46%', J(para('Say More', fontSize='xx-large', fontFamily='display', style={'typography': {'lineHeight': '1'}}),
                     para('Two friends talking about work, bodies, money and friendship. New every Tuesday at 6am, recorded in Levenshulme, Manchester.', fontSize='small'))),
            (None, J(heading('Listen', 6), listen_row())),
            (None, J(heading('The show', 6), para('<a href="/episode-index/">Episode index</a><br><a href="/transcripts/">Transcripts</a><br><a href="/write-to-us/">Write to us</a><br><a href="/support/">Support and advertising</a>', fontSize='small'))),
            (None, J(heading('Email', 6), para('<a href="mailto:hello@saymore.example">hello@saymore.example</a><br>We read everything and answer about half.', fontSize='small'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
    para('Demo photos are CC0 from Wikimedia Commons (mostly Unsplash uploads). Demo audio is public domain, from the White House “As Told By” series.', fontSize='x-small', align='wide')),
    tag='footer', align='full', className='is-style-oxblood',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

write('parts/break-notice.html', pattern_ref('break-notice'))

# ---------------------------------------------------------------- templates
PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(pattern_ref('front-page-layout'), style={'spacing': {'margin': {'top': '0'}}}))
write('templates/home.html', page_template(J(
    heading('Episodes', 1, fontSize='display', align='wide'),
    row(J(para('Newest first. Pick a topic, or see <a href="/episode-index/">every episode on one page</a>.'),
          dyn('categories', className='is-style-topic-list')), justify='space-between', align='wide'),
    pattern_ref('episode-cards-archive')), style=PAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('episode-list-archive')), style=PAD))
write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='display'),
    dyn('term-description', align='wide'),
    dyn('categories', className='is-style-topic-list', align='wide'),
    pattern_ref('episode-list-archive')), style=PAD))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Pay rise, swimming, sisters', buttonText='Search'),
    pattern_ref('episode-list-archive')), style=PAD))
write('templates/404.html', page_template(J(
    heading('We lost that one', 1),
    para('The link might be to an old episode page from before we moved the site. Search for a word from the title, or look through the <a href="/episode-index/">episode index</a>.'),
    dyn('search', label='Search', showLabel=False, placeholder='Pay rise, swimming, sisters', buttonText='Search')), style=PAD))
def title_band():
    return group(group(dyn('post-title', level=1, fontSize='display'), align='wide', layout={'type': 'default'}), align='full', className='is-style-band',
                 style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}})
NOTOP = {'spacing': {'margin': {'top': '0'}, 'padding': {'bottom': 'var:preset|spacing|70'}}}
write('templates/page.html', page_template(J(title_band(), group(dyn('post-content', align='wide', layout={'type': 'constrained'}), align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}}})), style=NOTOP))
write('templates/page-wide.html', page_template(J(title_band(), group(dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1280px'}), align='wide', layout={'type': 'default'},
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}}})), style=NOTOP))

def single_tpl(label_prev, label_next):
    return page_template(J(
        group(J(row(J(dyn('post-terms', term='category', separator=', '), dyn('post-date', format='l j F Y')), style={'spacing': {'blockGap': 'var:preset|spacing|30'}}),
                dyn('post-title', level=1, fontSize='xx-large')), align='wide', layout={'type': 'default'}),
        columns(('62%', dyn('post-content', layout={'type': 'default'})),
                ('38%', J(dyn('post-featured-image', aspectRatio='4/5', className='is-style-arch'), pattern_ref('episode-sidebar'))),
                align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|70'}}}),
        group(J(dyn('post-navigation-link', type='previous', label=label_prev, showTitle=True),
                dyn('post-navigation-link', label=label_next, showTitle=True)),
              align='wide', className='is-style-episode-row', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'})),
        style=PAD)
write('templates/single.html', single_tpl('Older episode', 'Newer episode'))
write('templates/single-letter.html', page_template(J(
    group(J(para('Dear Say More', fontSize='large', fontFamily='display'), dyn('post-title', level=1, fontSize='xx-large'), dyn('post-date', format='l j F Y', textColor='base')),
          align='full', className='is-style-bottle', layout={'type': 'constrained'},
          style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'margin': {'top': '0'}}}),
    group(dyn('post-content', layout={'type': 'constrained'}), style={'spacing': {'padding': {'top': 'var:preset|spacing|50'}}}),
    group(J(dyn('post-navigation-link', type='previous', label='Older episode', showTitle=True), dyn('post-navigation-link', label='Newer episode', showTitle=True)),
          className='is-style-episode-row', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'})),
    style={'spacing': {'padding': {'bottom': 'var:preset|spacing|70'}, 'margin': {'top': '0'}}}))

write('style.css', '''/*
Theme Name: Confidante
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A podcast theme for conversation shows with two or three hosts, with episode pages that carry the player, chapters, show notes and a two-colour transcript.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: confidante
Tags: blog, podcast, entertainment, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column, two-columns
*/''')

# ---------------------------------------------------------------- demo content
def episode_body(audio_url, cap, note, chaps, notes, transcript, guest=None, extra=None):
    parts = [audio(audio_url, cap), para(note, className='is-style-content-note') if note else '',
             heading('Chapters', 3), chapters(audio_url, chaps), heading('Show notes', 3)]
    parts += notes
    if guest:
        parts.append(group(J(para('Guest', fontSize='x-small', style={'typography': {'fontWeight': '700'}}), heading(guest[0], 4), para(guest[1])), className='is-style-deep-blush',
                           style={'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}))
    if extra:
        parts.append(extra)
    parts += [heading('Transcript', 3), details('Read the full transcript', J(*[say(w, t) for w, t in transcript],
              para('Checked by Roisin. Spot a mistake? Email transcripts@saymore.example.', fontSize='x-small')))]
    return J(*parts)

EPS = [
 dict(n=63, slug='asking-for-more-money', title='63. Asking for more money', cat='money', img='ep-money.jpg', a=(A1, A1_CAP), mins=52,
      ex='Ama asked for a pay rise in March. It is now the autumn. Folake Adeyemi goes through her notes line by line.',
      note='Content note: frank talk about debt, and one bereavement (from 31:40).',
      ch=[(0, 'Hello, and what Roisin had for breakfast'), (190, 'The email Ama sent in March'), (820, 'Folake on salary bands'), (1510, 'Writing the one-page case'), (1900, 'Debt, and why it was hard to say out loud'), (2710, 'What happened on Thursday')],
      notes=[lst(['<a href="https://www.acas.org.uk/">Acas</a> runs a free helpline for workplace questions: 0300 123 1100.', '<a href="https://www.gov.uk/employment-rights-pay">GOV.UK on pay and your rights</a>.', 'The salary survey Ama used came from her union. If you are in one, ask yours.'])],
      guest=('Folake Adeyemi', 'Payroll auditor and union rep in Salford. Runs a Tuesday-night drop-in at the library on Chapel Street.'),
      extra=group(J(para('Phrase of the week', fontSize='small', style={'typography': {'fontWeight': '700'}}), para('Salary band', fontSize='x-large', fontFamily='display'),
                    para('The range a company has already agreed to pay for a job. Ask for it before the interview.')), className='is-style-paper-box'),
      tr=[('Ama', 'Right. We’re recording. Roisin, you’ve got a face on.'), ('Roisin', 'I have not got a face on. This is my face.'), ('Ama', 'So. The pay rise. I said I’d report back and I’m reporting back.'),
          ('Folake', 'Can I ask what you actually wrote? Word for word, if you have it.'), ('Ama', 'I have everything. “Hi Mark, I’d like to discuss my salary at my review.” That was it.'),
          ('Folake', 'That’s a fine opener. The problem is nothing came after it.')]),
 dict(n=62, slug='the-friend-who-moved-to-lisbon', title='62. The friend who moved to Lisbon', cat='friendship', img='ep-friends.jpg', a=(A2, A2_CAP), mins=47,
      ex='Roisin’s oldest friend moved abroad in January. They have spoken four times since. Whose job is it to ring?',
      note='', ch=[(0, 'Hello'), (240, 'The leaving do'), (905, 'Voice notes versus actual phone calls'), (1620, 'Ama’s rule about birthdays'), (2400, 'Booking the flight')],
      notes=[para('Roisin mentioned the study on how many friends people keep after 30. We couldn’t find the original, so we are not linking a newspaper summary of it.'),
             lst(['Ryanair to Lisbon from Manchester, Tuesdays and Saturdays, since you asked.', 'The book Ama keeps recommending is <em>Big Friendship</em> by Aminatou Sow and Ann Friedman.'])],
      tr=[('Roisin', 'She sent me a photo of a custard tart and I didn’t reply for nine days.'), ('Ama', 'Nine days.'), ('Roisin', 'I was thinking of something good to say.'), ('Ama', 'To a custard tart.')]),
 dict(n=61, slug='swimming-through-the-menopause', title='61. Swimming through the menopause', cat='bodies', img='ep-body.jpg', a=(A2, A2_CAP), mins=55,
      ex='Dr Nadia Rahman, a GP in Longsight, answers the questions we were too embarrassed to ask at 44.',
      note='Content note: periods, HRT and a short part about fertility (22:10 to 26:00).',
      ch=[(0, 'Hello, and the cold-water thing'), (420, 'Nadia on what perimenopause actually is'), (1330, 'HRT, and the shortage in 2022'), (2230, 'Fertility, briefly'), (2800, 'Questions from the Patreon')],
      notes=[lst(['<a href="https://www.nhs.uk/conditions/menopause/">NHS pages on menopause</a>, which Nadia says are good now.', 'Arcadia’s women-only swim is Wednesday 7pm.']),
             para('This episode is general information. Please talk to your own GP about your own body.')],
      guest=('Dr Nadia Rahman', 'GP at a practice in Longsight for twelve years. Does a menopause clinic on Thursday afternoons.'),
      tr=[('Nadia', 'The first thing people tell me is that they thought they were going mad.'), ('Roisin', 'That was me in the car park at Asda.'), ('Nadia', 'You weren’t going mad.')]),
 dict(n=60, slug='leaving-the-job-youre-good-at', title='60. Leaving the job you’re good at', cat='work', img='ep-work.jpg', a=(A1, A1_CAP), mins=49,
      ex='Ama left HR after eleven years. She was good at it and she was miserable. We talk about the week she handed in her notice.',
      note='', ch=[(0, 'Hello'), (300, 'The Sunday-night feeling'), (1100, 'Telling her mum'), (1850, 'The pay cut, in actual numbers'), (2600, 'Six months on')],
      notes=[para('Ama’s pay went from £41,000 to £33,500. She says it’s worth it on most days and not on the day the boiler went.')],
      tr=[('Ama', 'I was good at it. That was the problem. Nobody tells you that being good at something can keep you there.'), ('Roisin', 'I’d have told you. You didn’t ask.')]),
 dict(n=59, slug='my-sister-owes-me-4000', title='59. Dear Say More: my sister owes me £4,000', cat='letters', img='ep-letters.jpg', a=(A1, A1_CAP), mins=38, tpl='single-letter',
      ex='Hannah lent her sister a deposit. Her sister has booked a week in Crete. We read the letter and argue about it.',
      note='', ch=[(0, 'The letter'), (360, 'Roisin’s first answer'), (980, 'Ama’s spreadsheet'), (1700, 'Roisin changes her mind'), (2100, 'What we would actually say')],
      notes=[para('Hannah, if you’re listening: we hope it went all right. Tell us.')],
      extra=quote('My sister borrowed £4,000 for a deposit two years ago. We agreed she’d pay it back at £200 a month. She paid three months. She’s just booked a week in Crete and posted the villa in the family chat. Do I say something or do I let it go? I love her and I don’t want to be the sister who counts.', 'Hannah, Stockport, by email'),
      tr=[('Roisin', 'Let it go. It’s family.'), ('Ama', 'It’s four thousand pounds.'), ('Roisin', 'Okay, say something.')]),
 dict(n=58, slug='deciding-about-kids-at-38', title='58. Deciding about kids at 38', cat='bodies', img='ep-kids.jpg', a=(A2, A2_CAP), mins=61,
      ex='Roisin doesn’t know if she wants children and is tired of being asked. A long one, and a careful one.',
      note='Content note: pregnancy loss (12:05 to 19:40). Use the chapters to skip it.',
      ch=[(0, 'Hello'), (725, 'Ama’s miscarriage in 2021'), (1180, 'Roisin at the family wedding'), (2300, 'Egg freezing costs in Manchester'), (3300, 'What we still don’t know')],
      notes=[lst(['<a href="https://www.miscarriageassociation.org.uk/">The Miscarriage Association</a>, helpline 01924 200799.', 'Egg freezing in the UK usually costs £3,000 to £5,000 per cycle, plus storage.'])],
      tr=[('Roisin', 'I don’t know. I keep saying that like it’s a placeholder, but it might just be the answer.')]),
 dict(n=57, slug='who-pays-for-the-hen-do', title='57. Who pays for the hen do', cat='money', img='ep-money2.jpg', a=(A1, A1_CAP), mins=44,
      ex='A £640 weekend in Albufeira, for a bride Ama has met twice. Is it all right to say no?',
      note='', ch=[(0, 'Hello'), (280, 'The WhatsApp group'), (960, 'What people actually spend'), (1700, 'How to say no in one message')],
      notes=[para('The message Ama sent in the end: “I can’t do Albufeira, but I’d love to take you for dinner before the wedding.” It worked.')],
      tr=[('Ama', 'I have met her twice. Once was at a funeral.')]),
 dict(n=56, slug='tea-with-our-mums', title='56. Tea with our mums', cat='friendship', img='ep-kitchen.jpg', a=(A2, A2_CAP), mins=58,
      ex='Grace Boateng and Siobhan Keane come to the kitchen table. They have opinions about the show.',
      note='', ch=[(0, 'Hello, mums'), (500, 'What Grace thinks of the name'), (1400, 'Siobhan on Derry in 1985'), (2600, 'Their friends, and how they kept them')],
      notes=[para('Grace would like it known that she did not “storm off” in 2019. She went to get the bus.')],
      tr=[('Grace', 'Why is it called Say More? You already say plenty.')]),
]
start = datetime.date(2026, 9, 22)
posts = []
for i, e in enumerate(EPS):
    p = {'title': e['title'], 'slug': e['slug'], 'category': e['cat'], 'image': e['img'], 'excerpt': e['ex'],
         'date': (start - datetime.timedelta(days=7 * i)).isoformat(),
         'content': episode_body(e['a'][0], e['a'][1], e['note'], e['ch'], e['notes'], e['tr'], e.get('guest'), e.get('extra'))}
    if e.get('tpl'):
        p['template'] = e['tpl']
    posts.append(p)

demo = {
    'site': {'title': 'Say More', 'tagline': 'Two friends on work, bodies, money and friendship. Every Tuesday.'},
    'categories': [{'slug': 'work', 'name': 'Work'}, {'slug': 'bodies', 'name': 'Bodies'}, {'slug': 'money', 'name': 'Money'},
                   {'slug': 'friendship', 'name': 'Friendship'}, {'slug': 'letters', 'name': 'Letters', 'description': 'Episodes built around one listener letter.'}],
    'front_page': 'home', 'posts_page': 'episodes',
    'pages': [{'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'episodes', 'title': 'Episodes', 'content': ''},
              {'slug': 'hosts', 'title': 'Hosts', 'pattern': 'confidante/hosts-page'},
              {'slug': 'guests', 'title': 'Guests', 'pattern': 'confidante/guests-page'},
              {'slug': 'write-to-us', 'title': 'Write to us', 'pattern': 'confidante/write-to-us-page'},
              {'slug': 'support', 'title': 'Support the show', 'pattern': 'confidante/support-page'},
              {'slug': 'subscribe', 'title': 'Subscribe', 'pattern': 'confidante/subscribe-page'},
              {'slug': 'episode-index', 'title': 'Episode index', 'pattern': 'confidante/episode-index-page'},
              {'slug': 'transcripts', 'title': 'Transcripts', 'pattern': 'confidante/transcripts-page'}],
    'posts': posts,
    'nav': [{'label': 'Episodes', 'url': '/episodes/'}, {'label': 'Hosts', 'url': '/hosts/'}, {'label': 'Guests', 'url': '/guests/'}, {'label': 'Write to us', 'url': '/write-to-us/'},
            {'label': 'Support', 'url': '/support/'}, {'label': 'Subscribe', 'url': '/subscribe/'}],
}
os.makedirs('demos/confidante', exist_ok=True)
json.dump(demo, open('demos/confidante/content.json', 'w'), indent=1, ensure_ascii=False)
print('built confidante')
