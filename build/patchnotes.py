# Design note (patchnotes, idea 047c: tech podcast)
# Direction: "release notes". Each episode reads like a well-kept changelog entry: a left rail of facts (episode, date, length, guests), a right column of prose,
# and show notes sorted into Added / Changed / Fixed / Removed. Technical through structure and precision; no monospace, no terminal cosplay.
# Why: developers trust changelogs that are dated, specific and admit mistakes. The "Fixed" list is where last week's errors get corrected on the record.
# Fonts: SUSE (display 800 and body 400, one family, drawn for an open-source company) with tabular figures everywhere.
# Palette: cool paper, graphite, commit green for links and "added", removal red for "removed", a pale hunk yellow behind the latest release.
import sys, json, os, datetime
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('patchnotes')
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
    ('base', '#030A05', 'Screen'), ('contrast', '#C8FAD4', 'Phosphor'), ('accent', '#3DFF84', 'Bright green'),
    ('accent-2', '#FF6B5E', 'Removal red'), ('surface', '#0A1A0F', 'Panel'), ('line', '#1F7A40', 'Rule'),
    ('muted', '#86B894', 'Dim phosphor'), ('hunk', '#0E2C19', 'Highlight'), ('changed', '#5CE1E6', 'ANSI cyan'),
    ('amber', '#FFB23E', 'Amber'), ('bar', '#B7C2B7', 'Title bar'), ('ink', '#030A05', 'Ink on bar'),
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

focus = {'outline': {'color': 'var:preset|color|amber', 'offset': '2px', 'style': 'solid', 'width': '3px'}}
theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '720px', 'wideSize': '1240px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PALETTE),
                  'duotone': [{'slug': 'phosphor', 'colors': ['#030A05', '#6DFFA0'], 'name': 'Green phosphor'},
                              {'slug': 'amber', 'colors': ['#0A0600', '#FFC766'], 'name': 'Amber monitor'}]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': [disp, body],
            'fontSizes': [fs('x-small', '0.8125rem', 'Caption'), fs('small', '0.9375rem', 'Small'), fs('medium', '1.125rem', 'Body'),
                          fs('large', '1.5rem', 'Large', '1.25rem'), fs('x-large', '2.25rem', 'Section', '1.7rem'),
                          fs('xx-large', '3.75rem', 'Title', '2.4rem'), fs('display', '7rem', 'Release', '3.2rem')],
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
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.58', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}}, ':focus': focus},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'lineHeight': '1.02', 'letterSpacing': '0'}, 'color': {'text': 'var:preset|color|accent'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15', 'fontWeight': '600'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3', 'fontWeight': '600'}, 'color': {'text': 'var:preset|color|amber'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|small', 'letterSpacing': '0', 'fontWeight': '700'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'letterSpacing': '0', 'fontWeight': '600'}, 'color': {'text': 'var:preset|color|muted'}},
            'button': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|ink'},
                       'border': {'radius': '0', 'width': '2px', 'style': 'solid', 'color': 'var:preset|color|accent'},
                       'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.55em', 'bottom': '0.55em', 'left': '1em', 'right': '1em'}},
                       ':hover': {'color': {'background': 'var:preset|color|amber', 'text': 'var:preset|color|ink'}, 'border': {'color': 'var:preset|color|amber'}},
                       ':focus': focus},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|large'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/heading': {'elements': {'link': {'color': {'text': 'currentColor'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}},
            'core/image': {'border': {'radius': '0'}, 'filter': {'duotone': 'var:preset|duotone|phosphor'}},
            'core/post-featured-image': {'border': {'radius': '0'}, 'filter': {'duotone': 'var:preset|duotone|phosphor'}},
            'core/gallery': {'filter': {'duotone': 'var:preset|duotone|phosphor'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '500', 'lineHeight': '1.35', 'letterSpacing': '-0.01em'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}}, 'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/details': {'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|line', 'radius': '0'},
                             'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
                             'css': '& summary{font-weight:700;cursor:pointer}&[open] summary{margin-bottom:.75rem}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table.has-fixed-layout{table-layout:auto}& table th{text-align:left;font-weight:600;color:var(--wp--preset--color--muted)}& table td,& table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.55em 1em .55em 0;vertical-align:top}& table thead{border:0;border-bottom:1px solid var(--wp--preset--color--contrast)}'},
            'core/search': {'border': {'radius': '0'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'}},
            'core/audio': {'css': '& audio{width:100%;min-width:0;filter:invert(1) hue-rotate(180deg) saturate(.6)}'},
        },
        'css': ('.wp-block-column>.wp-block-group:only-child{height:100%}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}'
                'body{font-synthesis:none;font-variant-numeric:tabular-nums lining-nums slashed-zero}'
                ':focus-visible{outline:3px solid var(--wp--preset--color--amber);outline-offset:2px}'
                'body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:99;background:repeating-linear-gradient(to bottom,rgba(0,0,0,.22) 0 1px,transparent 1px 3px)}'
                '::selection{background:var(--wp--preset--color--amber);color:var(--wp--preset--color--ink)}'
                'strong{color:var(--wp--preset--color--amber)}'
                ':where(.wp-block-post-content)>:where(h2,h3){margin-top:var(--wp--preset--spacing--60)}'),
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'status-line', 'title': 'Status line'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
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

write('styles/amber-monitor.json', variation('Amber monitor', [
    ('base', '#0A0600', 'Screen'), ('contrast', '#FFD9A0', 'Phosphor'), ('accent', '#FFB23E', 'Bright green'),
    ('accent-2', '#FF6B5E', 'Removal red'), ('surface', '#1A1103', 'Panel'), ('line', '#7A4F10', 'Rule'),
    ('muted', '#C9A36A', 'Dim phosphor'), ('hunk', '#2A1B05', 'Highlight'), ('changed', '#FFE08A', 'ANSI cyan'),
    ('amber', '#FFF1C9', 'Amber'), ('bar', '#C9B99A', 'Title bar'), ('ink', '#0A0600', 'Ink on bar')]))
write('styles/cyan-bbs.json', variation('Cyan BBS', [
    ('base', '#00141C', 'Screen'), ('contrast', '#D3F6FA', 'Phosphor'), ('accent', '#5CE1E6', 'Bright green'),
    ('accent-2', '#FF7A70', 'Removal red'), ('surface', '#002433', 'Panel'), ('line', '#1C6B80', 'Rule'),
    ('muted', '#8CC3CE', 'Dim phosphor'), ('hunk', '#003445', 'Highlight'), ('changed', '#FFE066', 'ANSI cyan'),
    ('amber', '#FFE066', 'Amber'), ('bar', '#A9C4CA', 'Title bar'), ('ink', '#00141C', 'Ink on bar')]))
write('styles/teletype.json', variation('Teletype paper', [
    ('base', '#F2EFE4', 'Screen'), ('contrast', '#141412', 'Phosphor'), ('accent', '#0F6B32', 'Bright green'),
    ('accent-2', '#B0271F', 'Removal red'), ('surface', '#E6E1D2', 'Panel'), ('line', '#8C8672', 'Rule'),
    ('muted', '#4E4B40', 'Dim phosphor'), ('hunk', '#FBF0B2', 'Highlight'), ('changed', '#1F5AA6', 'ANSI cyan'),
    ('amber', '#8A4B00', 'Amber'), ('bar', '#141412', 'Title bar'), ('ink', '#F2EFE4', 'Ink on bar')]))

def section(slug, title, types, styles):
    if 'css' in styles:
        styles = dict(styles, css=split_css(styles['css']))
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
                                                        'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))

def diff_list(slug, title, sign, colour):
    section(slug, title, ['core/list'],
            {'css': '&{list-style:none;padding-left:0!important}& li{position:relative;padding:.35rem 0 .35rem 1.6rem;border-bottom:1px solid var(--wp--preset--color--line)}'
                    '& li::before{content:"%s";position:absolute;left:.2rem;top:.3rem;font-weight:800;color:var(--wp--preset--color--%s)}' % (sign, colour)})
diff_list('diff-added', 'Changelog: added', '+', 'accent')
diff_list('diff-changed', 'Changelog: changed', '~', 'changed')
diff_list('diff-fixed', 'Changelog: fixed', '\\2713', 'accent')
diff_list('diff-removed', 'Changelog: removed', '\\2212', 'accent-2')
section('title-bar', 'Title bar', ['core/paragraph', 'core/heading'],
        {'color': {'background': 'var:preset|color|bar', 'text': 'var:preset|color|ink'},
         'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
         'spacing': {'padding': {'top': '0.15em', 'bottom': '0.15em', 'left': '0.6em', 'right': '0.6em'}},
         'elements': {'link': {'color': {'text': 'var:preset|color|ink'}}}})
section('ansi-box', 'ANSI box', ['core/group', 'core/column'],
        {'color': {'background': 'var:preset|color|surface'}, 'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|line'},
         'spacing': {'padding': {'top': '0', 'bottom': 'var:preset|spacing|30', 'left': 'var:preset|spacing|30', 'right': 'var:preset|spacing|30'}},
         'css': '& > .is-style-title-bar:first-child{margin:0 calc(-1 * var(--wp--preset--spacing--30)) var(--wp--preset--spacing--30)!important}'})
section('dither', 'Dither band', ['core/group'],
        {'css': '&{min-height:28px;background:linear-gradient(90deg,var(--wp--preset--color--accent) 0 22%,transparent 22%),repeating-conic-gradient(var(--wp--preset--color--accent) 0 25%,transparent 0 50%) 0 0/6px 6px;-webkit-mask:linear-gradient(90deg,#000 0 55%,transparent 80%);mask:linear-gradient(90deg,#000 0 55%,transparent 80%)}'})
section('commit', 'Commit row', ['core/group'],
        {'border': {'left': {'color': 'var:preset|color|line', 'width': '2px', 'style': 'solid'}},
         'spacing': {'padding': {'left': 'var:preset|spacing|30', 'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
         'css': '&:hover{border-left-color:var(--wp--preset--color--accent)}'})
section('hash', 'Episode hash', ['core/post-terms'],
        {'css': '& a{color:var(--wp--preset--color--amber);text-decoration:none;font-weight:700}'})
section('prompt', 'Prompt line', ['core/paragraph'],
        {'color': {'text': 'var:preset|color|muted'}, 'typography': {'fontFamily': 'var:preset|font-family|display'},
         'css': '&::before{content:"> ";color:var(--wp--preset--color--accent)}'})
section('oneliners', 'Oneliners (ruled lines)', ['core/list'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding-left:0!important}& li{padding:.35rem 0;border-bottom:1px dashed var(--wp--preset--color--line)}& li:last-child{border-bottom:0}'})
section('menu', 'BBS menu', ['core/list'],
        {'typography': {'fontFamily': 'var:preset|font-family|display'},
         'css': '&{list-style:none;padding-left:0!important}& li{padding:.25rem 0}& li a{text-decoration:none;color:var(--wp--preset--color--contrast)}& li a strong{display:inline-block;min-width:1.8em;color:var(--wp--preset--color--amber)}& li a:hover{color:var(--wp--preset--color--accent)}'})
section('statusbar', 'Status bar', ['core/group'],
        {'color': {'background': 'var:preset|color|bar', 'text': 'var:preset|color|ink'}, 'typography': {'fontFamily': 'var:preset|font-family|display'},
         'css': '& strong{color:var(--wp--preset--color--ink)}'})
section('panel-full', 'Panel (full width)', ['core/group'],
        {'color': {'background': 'var:preset|color|surface'}, 'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}})
section('rule-bottom', 'Rule below', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}}})
section('hunk', 'Latest release (hunk)', ['core/group', 'core/columns'],
        {'color': {'background': 'var:preset|color|hunk', 'text': 'var:preset|color|contrast'},
         'border': {'left': {'color': 'var:preset|color|accent', 'width': '4px', 'style': 'solid'}}})
section('panel', 'Panel', ['core/group', 'core/column'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'border': {'width': '1px', 'style': 'solid', 'color': 'var:preset|color|line'},
         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('graphite', 'Graphite', ['core/group'],
        {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
         'elements': {'link': {'color': {'text': 'currentColor'}}, 'h6': {'color': {'text': 'currentColor'}},
                      'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}}}})
section('rail', 'Fact rail', ['core/group', 'core/column'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'border': {'top': {'color': 'var:preset|color|contrast', 'width': '2px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|20'}},
         'css': '& p{margin-block:.15rem}'})
section('release-row', 'Release row', ['core/group'],
        {'border': {'top': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40'}}})
section('chapters', 'Chapter list', ['core/list'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding-left:0!important}& li{display:grid;grid-template-columns:4.2rem 1fr;gap:.75rem;padding:.4rem 0;border-bottom:1px solid var(--wp--preset--color--line)}& li a{font-weight:700;text-decoration:none}& li a:hover{text-decoration:underline}'})
section('listen-row', 'Listen links', ['core/list'],
        {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '600'},
         'css': '&{list-style:none;padding:0!important;display:flex;flex-wrap:wrap;gap:.3rem 1.2rem}'})
section('tag-list', 'Tag list', ['core/tag-cloud', 'core/categories'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.4rem}& a{display:inline-block;padding:.2rem .6rem;border:1px solid var(--wp--preset--color--line);border-radius:0;text-decoration:none;font-size:inherit!important}& a:hover{border-color:currentColor}'})

# ---------------------------------------------------------------- content helpers
A_HOP = 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Grace_Hopper_%28As_Told_By_U.S._Chief_Technology_Officer_Megan_Smith%29.oggvorbis.ogg'
A_ENIAC = 'https://upload.wikimedia.org/wikipedia/commons/1/15/The_ENIAC_Programmers_%28As_Told_By_U.S._Chief_Technology_Officer_Megan_Smith%29.ogg'
A_ADA = 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Ada_Lovelace_%28As_Told_By_U.S._Chief_Technology_Officer_Megan_Smith%29.mp3'
CAPS = {A_HOP: 'Stand-in audio: “Grace Hopper”, told by Megan Smith for the White House (public domain). Replace with your episode file.',
        A_ENIAC: 'Stand-in audio: “The ENIAC Programmers”, told by Megan Smith for the White House (public domain). Replace with your episode file.',
        A_ADA: 'Stand-in audio: “Ada Lovelace”, told by Megan Smith for the White House (public domain). Replace with your episode file.'}

def ts(sec):
    return '%d:%02d' % (sec // 60, sec % 60) if sec < 3600 else '%d:%02d:%02d' % (sec // 3600, sec % 3600 // 60, sec % 60)

def chapters(url, items):
    return lst(['<a href="%s#t=%d">%s</a> %s' % (url, s, ts(s), t) for s, t in items], className='is-style-chapters')

def listen_row():
    return lst(['<a href="https://podcasts.apple.com/">Apple Podcasts</a>', '<a href="https://pocketcasts.com/">Pocket Casts</a>',
                '<a href="https://overcast.fm/">Overcast</a>', '<a href="https://open.spotify.com/">Spotify</a>',
                '<a href="https://antennapod.org/">AntennaPod</a>', '<a href="/feed/">RSS</a>'], className='is-style-listen-row')

def notes(added=None, changed=None, fixed=None, removed=None):
    out = []
    for h, items, cls in [('Added', added, 'is-style-diff-added'), ('Changed', changed, 'is-style-diff-changed'),
                          ('Fixed', fixed, 'is-style-diff-fixed'), ('Removed', removed, 'is-style-diff-removed')]:
        if items:
            out += [heading(h, 4), lst(items, className=cls)]
    return J(*out)

def rail(*lines):
    return group(J(*[para(l) for l in lines]), className='is-style-rail', layout={'type': 'default'})

# ---------------------------------------------------------------- patterns
LATEST_NOTES = notes(
    added=['Sanne Vermeulen, who runs on-call for a payments company in Antwerp, on writing an incident review nobody dreads.',
           '<a href="https://sre.google/sre-book/postmortem-culture/">The postmortem chapter of the Google SRE book</a>, which Sanne says is 80% right.',
           'Kwame’s pager rota spreadsheet, shared by request (<a href="/support/">supporters’ feed</a>).'],
    changed=['Follow-up to episode 85: Jonas moved the last two services off the cloud. The bill went from €1,140 to €310 a month.'],
    fixed=['In episode 87 we said the PDF library had 14 maintainers. It has four. The other ten are bots.'],
    removed=['Twelve minutes of Lieke’s microphone falling off the desk.'])

pattern('latest-release', 'Latest episode as a release note', 'featured,audio', group(columns(
    ('26%', J(para('Episode 88', fontSize='xx-large', fontFamily='display', style={'typography': {'fontWeight': '800', 'letterSpacing': '-0.04em', 'lineHeight': '1'}}),
              rail('<strong>Out</strong> Thursday 24 September 2026', '<strong>Length</strong> 58:12', '<strong>Hosts</strong> Lieke Maes, Kwame Mensah', '<strong>Guest</strong> Sanne Vermeulen'))),
    ('74%', J(heading('<a href="/the-pager-went-off-at-3am/">The pager went off at 3am</a>', 1, fontSize='display'),
              para('Sanne has been on call for eleven years. She explains the incident review template she wrote after the night a payment queue ate 40,000 transfers, and why the first question in it is “what did you have for dinner?”', fontSize='large'),
              audio(A_HOP, CAPS[A_HOP]), listen_row())),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    align='full', className='is-style-hunk', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'margin': {'top': '0'}}}),
    description='The newest episode, laid out like the top entry of a changelog.')

pattern('whats-in-it', 'What changed this episode (Added, Changed, Fixed, Removed)', 'text', columns(
    ('26%', J(heading('In this release', 2, fontSize='large'), para('Show notes, sorted the way we sort commits.', fontSize='small', textColor='muted'))),
    ('74%', LATEST_NOTES), align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|60'}, 'blockGap': {'left': 'var:preset|spacing|60'}}}),
    description='The signature: show notes as a changelog. “Fixed” is where last week’s mistakes are corrected on the record.')

release_row = group(columns(
    ('26%', J(dyn('post-terms', term='post_tag', separator=', ', style={'typography': {'fontWeight': '800'}}), dyn('post-terms', term='category', separator=', '), dyn('post-date', format='j M Y'))),
    ('74%', J(dyn('post-title', isLink=True, level=3, fontSize='x-large'), dyn('post-excerpt', excerptLength=30, moreText=''))),
    style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}), className='is-style-release-row', layout={'type': 'default'})

pattern('release-log', 'Release log (episode list)', 'posts,query', group(J(
    columns(('26%', heading('Release log', 2)), ('74%', para('Every episode, newest first. Numbers only go up. Specials are numbered too, because Kwame insists.', textColor='muted')),
            style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    query(release_row, per_page=6),
    para('<a href="/episodes/">All 88 episodes</a>, or <a href="/guests/">browse by guest</a>', fontSize='small')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|60'}}}))

pattern('release-log-archive', 'Release log (inherits the page query)', 'posts,query', inherit_query(release_row, align='wide'), inserter=False)

GUESTS = [['Sanne Vermeulen', 'On-call and incident reviews at a payments company, Antwerp', '<a href="/the-pager-went-off-at-3am/">88</a>'],
          ['Tomás Ferreira', 'Maintains an image-decoding library used by most of your phone apps', '<a href="/who-maintains-the-pdf-library/">87</a>'],
          ['Hana Novák', 'Accessibility auditor, Brno. Has filed around 3,000 bugs', '<a href="/accessibility-audits-that-get-fixed/">86</a>'],
          ['Jonas Peeters', 'Runs infrastructure for a Ghent newspaper, now mostly on its own servers', '<a href="/leaving-the-cloud-a-bit/">85</a>'],
          ['Ines Duarte', 'Hardware engineer, teaches soldering at a hackerspace in Lisbon', '<a href="/soldering-for-software-people/">82</a>']]
pattern('guest-list', 'Guest list', 'team,text', J(
    heading('Guests', 2),
    lst(['<strong>%s</strong> %s. Episode %s' % (g[0], g[1], g[2]) for g in GUESTS], className='is-style-oneliners'),
    para('<a href="/guests/">Everyone who has been on the show</a>', fontSize='small')))

pattern('chapters-list', 'Chapters with timestamps', 'text,audio', J(
    heading('Chapters', 3),
    chapters(A_HOP, [(0, 'Intro, and what broke this week'), (262, 'Sanne’s first pager, 2014'), (905, 'The 40,000 transfers'), (1690, 'Writing the review template'), (2610, 'Rotas that don’t burn people out'), (3240, 'Picks')]),
    para('Times open the audio at that point. Chapters are embedded in the MP3 for apps that support them.', fontSize='x-small', textColor='muted')))

pattern('show-notes-changelog', 'Show notes as a changelog', 'text', J(heading('Show notes', 3), LATEST_NOTES))

pattern('transcript', 'Transcript in a fold', 'text,audio', J(
    heading('Transcript', 3),
    details('Read the transcript (about 9,400 words)', J(
        para('<strong>Lieke</strong> We are recording. Kwame, is your fan on?'),
        para('<strong>Kwame</strong> My laptop is compiling something. It will stop in about a minute. Or never.'),
        para('<strong>Sanne</strong> I can hear it from here and I’m in Antwerp.'),
        para('<strong>Lieke</strong> Sanne, what did you have for dinner the night of the 40,000 transfers?'),
        para('<strong>Sanne</strong> Nothing. That’s the point. That’s why it’s the first question.'),
        para('Machine transcript, corrected by Lieke. Speaker names are added by hand. Report errors on the <a href="/changelog/">show changelog</a> page.', fontSize='x-small', textColor='muted'))),
    para('<a href="/transcripts/">Transcripts as plain text files</a>, one per episode.', fontSize='small')))

pattern('recording-setup', 'Recording setup (details)', 'text', J(
    heading('How this episode was made', 4),
    details('Recording setup', table([['Microphones', 'Two Shure SM7B, one borrowed Rode PodMic for guests'], ['Interface', 'Zoom PodTrak P4'],
                                       ['Remote guest', 'Recorded locally on their machine, uploaded after'], ['Editing', 'Reaper, about four hours per episode'],
                                       ['Loudness', '-16 LUFS stereo, -19 LUFS mono'], ['File', 'MP3, 128 kbps, with chapters']])),
    para('We publish this because people ask every week.', fontSize='x-small', textColor='muted')))

pattern('guest-card', 'Guest card', 'team', group(J(
    para('Guest', fontSize='x-small', textColor='muted', style={'typography': {'fontWeight': '600'}}),
    heading('Sanne Vermeulen', 3),
    para('Leads on-call for a payments company in Antwerp. Before that, eight years at a hosting company in Ghent. Keeps a paper notebook for every incident since 2014.'),
    para('<a href="https://social.example/@sanne">@sanne on Mastodon</a>', fontSize='small')), className='is-style-panel', layout={'type': 'default'}))

pattern('word-of-the-episode', 'Term of the episode', 'text', group(J(
    para('Term of the episode', fontSize='x-small', textColor='muted', style={'typography': {'fontWeight': '600'}}),
    para('Blameless review', fontSize='x-large', fontFamily='display', style={'typography': {'fontWeight': '800', 'letterSpacing': '-0.03em', 'lineHeight': '1.05'}}),
    para('An incident write-up that asks how the system let a mistake happen, and never who made it. Sanne’s version adds a question about sleep.')),
    className='is-style-panel', layout={'type': 'default'}))

pattern('sponsor-read', 'Sponsor read', 'call-to-action', group(J(
    para('Supported by', fontSize='x-small', textColor='muted', style={'typography': {'fontWeight': '600'}}),
    heading('Hetzner-sized budgets, Belgian support: Kiwik Hosting', 4),
    para('A two-person hosting company in Leuven. Managed Postgres from €9 a month, and a human answers email within four hours. Mention the show for three months free. Kwame has used them since 2021 and pays full price.')),
    className='is-style-panel', layout={'type': 'default'}))

pattern('sponsor-policy', 'Sponsor policy', 'text', J(
    heading('Sponsors', 3),
    para('One sponsor per episode, read by a host, placed after the first chapter. €400 per episode, booked in blocks of four.'),
    notes(added=['Tools we have used for at least a month.', 'Companies that answer our email within a week.'],
          removed=['AI writing tools, crypto, gambling, and anything that tracks users across sites.']),
    para('<a href="mailto:sponsors@minorversion.example">sponsors@minorversion.example</a>')))

pattern('support-tiers', 'Support tiers', 'call-to-action', J(
    heading('Support the show', 2),
    para('Hosting, editing software and the guest microphone cost about €190 a month. Listeners cover most of it.'),
    pattern_ref('tiers-boxes'),
    buttons(('Support on Open Collective', 'https://opencollective.com/'), ('Pay once by bank transfer', '/support/#iban', {'className': 'is-style-outline'})),
    para('Open Collective publishes every euro in and out, so you can see the hosting bill.', fontSize='small', textColor='muted')))

pattern('status-line', 'Status line (next episode, or a break)', 'banner', group(row(J(
    para('<strong>Latest</strong> episode 88, 24 Sep 2026', fontSize='small'),
    para('<strong>Next</strong> Thursday 1 October, about database migrations', fontSize='small'),
    para('<strong>Break</strong> no episodes 24 Dec to 7 Jan', fontSize='small')), justify='space-between', align='wide'),
    align='full', className='is-style-statusbar', style={'spacing': {'padding': {'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10'}}}),
    description='A one-line status bar. Change it every Thursday, or use it for a recording break.')

pattern('show-changelog', 'Show changelog', 'text', J(
    heading('Show changelog', 2),
    para('Changes to the podcast itself, not to software. Newest first.'),
    group(J(heading('Version 3.2, September 2026', 4), notes(added=['Plain-text transcripts for every episode back to episode 1.'], changed=['Moved from Tuesdays to Thursdays. Tuesdays were release day at Lieke’s job.']))),
    group(J(heading('Version 3.0, January 2026', 4), notes(added=['Chapters in every episode.', 'The “Fixed” section in show notes.'], removed=['The intro music. Nobody missed it.']))),
    group(J(heading('Version 2.0, March 2024', 4), notes(changed=['Kwame joined as co-host. The show got 20 minutes longer.'], fixed=['Lieke’s audio. She bought a real microphone.']))),
    group(J(heading('Version 1.0, June 2022', 4), notes(added=['Episode 1: Lieke talks to herself about a PDF bug for 41 minutes.'])))))

pattern('hosts', 'Hosts', 'team,about', columns(
    (None, J(image('mic.jpg', 'A person in headphones speaking into a desk microphone, with a laptop and printed notes'),
             heading('Lieke Maes', 3), para('Backend developer at a public broadcaster in Brussels. Maintains a PDF library that more governments use than she is comfortable with. Started the show in 2022.'))),
    (None, J(image('ghent.jpg', 'Guild houses along the Graslei canal in Ghent, with boats moored in front'),
             heading('Kwame Mensah', 3), para('Frontend developer and accessibility lead at a Ghent agency. Joined in 2024. Owns eleven keyboards and uses one.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('about-page', 'Page: about', 'about', J(
    para('Minor Version is a weekly podcast about software and the people who keep it running: maintainers, on-call engineers, accessibility testers, the person who fixes the printer. We record in Ghent on Wednesday evenings and publish on Thursday mornings.', fontSize='large'),
    pattern_ref('hosts'), pattern_ref('screenshot'),
    heading('What we won’t do', 3),
    para('We don’t cover funding rounds, product launches or anything under embargo. We don’t do episodes about a company while it is paying us. If a guest works for a sponsor, we say so at the top.'),
    pattern_ref('recording-setup')), block_types='core/post-content')

pattern('guests-page', 'Page: guests', 'team', J(
    para('Everyone who has been on the show, newest first. If you would like to come on, read the note at the bottom.', fontSize='large'),
    pattern_ref('guest-list'),
    lst(['<strong>Nadia Haddad</strong> Writes the printer drivers nobody thanks her for, Liège. Episode <a href="/printers/">84</a>',
         '<strong>Lieke and Kwame</strong> The ENIAC six, a history special. Episode <a href="/the-eniac-six/">83</a>'], className='is-style-oneliners'),
    pattern_ref('sysops'),
    heading('Pitch yourself', 3),
    para('We want people who maintain things, fix things or have been on call for them. Send two sentences about what you work on and one thing you think most developers get wrong about it: <a href="mailto:guests@minorversion.example">guests@minorversion.example</a>. We don’t book people who are launching something that month.')),
    block_types='core/post-content')

pattern('changelog-page', 'Page: show changelog', 'text', J(pattern_ref('show-changelog'), pattern_ref('meetups'), pattern_ref('greetz'), pattern_ref('topics')), block_types='core/post-content')

pattern('support-page', 'Page: support and sponsors', 'call-to-action', J(pattern_ref('support-tiers'), pattern_ref('greetz'), pattern_ref('sponsor-policy'), pattern_ref('sponsor-read'),
    group(J(heading('Bank transfer', 4), para('Minor Version VZW, IBAN BE71 0961 2345 6769. Put “support” and your name in the message so we can thank you.', fontSize='small')), anchor='iban')),
    block_types='core/post-content')

pattern('subscribe-page', 'Page: subscribe', 'call-to-action', J(
    para('New episodes every Thursday at 7am Brussels time, about 50 minutes long. Any podcast app works. These are the ones we test chapters in.', fontSize='large'),
    lst(['<a href="https://pocketcasts.com/">Pocket Casts</a>: chapters and transcripts. What Lieke uses.',
         '<a href="https://overcast.fm/">Overcast</a>: chapters. What Kwame uses.',
         '<a href="https://antennapod.org/">AntennaPod</a>: chapters and transcripts, open source, Android.',
         '<a href="https://podcasts.apple.com/">Apple Podcasts</a>: chapters and transcripts.',
         '<a href="https://open.spotify.com/">Spotify</a>: partial, and no private feeds.',
         '<a href="/feed/">RSS</a>: everything. Paste it into your app.'], className='is-style-oneliners'),
    pattern_ref('downloads'), pattern_ref('newsletter'),
    para('The ad-free feed for supporters is a private RSS link. Open Collective sends it after your first payment.')), block_types='core/post-content')

pattern('transcripts-page', 'Page: transcripts', 'text', J(
    para('Every episode has a transcript on its page and as a plain text file. They are machine transcripts corrected by hand, usually within three days of release.', fontSize='large'),
    lst(['<strong>88</strong> <a href="/the-pager-went-off-at-3am/">The pager went off at 3am</a>, corrected',
         '<strong>87</strong> <a href="/who-maintains-the-pdf-library/">Who maintains the PDF library?</a>, corrected',
         '<strong>86</strong> <a href="/accessibility-audits-that-get-fixed/">Accessibility audits that get fixed</a>, corrected'], className='is-style-oneliners'),
    pattern_ref('boot-log')),
    block_types='core/post-content')

pattern('newsletter', 'Episode email', 'call-to-action', group(J(
    heading('One email per episode', 3),
    para('The show notes, in your inbox on Thursday morning. Plain text, no tracking pixels.'),
    buttons(('Subscribe by email', 'mailto:hello@minorversion.example?subject=Episode%20email'))), className='is-style-panel', layout={'type': 'default'}))

pattern('topics', 'Topics', 'text', J(heading('Topics', 3), dyn('categories', className='is-style-tag-list')))

pattern('episode-full', 'Episode: full layout', 'audio,featured', J(
    audio(A_HOP, CAPS[A_HOP]), pattern_ref('chapters-list'), pattern_ref('show-notes-changelog'), pattern_ref('guest-card'),
    pattern_ref('word-of-the-episode'), pattern_ref('transcript'), pattern_ref('recording-setup')),
    block_types='core/post-content', description='Player, chapters, changelog-style notes, guest, transcript and setup, in that order.')

# ---------------------------------------------------------------- round 2: BBS, demoscene and commit logs
def box(title, inner, **kw):
    return group(J(para(title, className='is-style-title-bar'), inner), className='is-style-ansi-box', layout={'type': 'default'}, **kw)

pattern('title-screen', 'Title screen: newest episode as the login banner', 'featured,audio', group(J(
    group(J(
        para('Minor Version BBS, node 1 of 1. Connected at 7:00 on Thursday 24 September. Episode 88 is out.', className='is-style-prompt', fontSize='small'),
        heading('<a href="/the-pager-went-off-at-3am/">The pager went off at 3am</a>', 1, fontSize='display'),
        group('', layout={'type': 'default'}, className='is-style-dither'),
        columns(('58%', J(para('Sanne Vermeulen has been on call for eleven years. She explains the incident review template she wrote after the night a payment queue ate 40,000 transfers, and why its first question is “what did you have for dinner?”', fontSize='large'),
                           audio(A_HOP, CAPS[A_HOP]), listen_row())),
                ('42%', box('episode.nfo', J(rail('<strong>Episode</strong> 88', '<strong>Out</strong> Thursday 24 September 2026', '<strong>Length</strong> 58:12', '<strong>Hosts</strong> Lieke Maes, Kwame Mensah', '<strong>Guest</strong> Sanne Vermeulen'),
                                             buttons(('Read the show notes', '/the-pager-went-off-at-3am/'))))),
                style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
        align='wide', layout={'type': 'default'}, style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
    align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'margin': {'top': '0'}}}),
    description='The home page opens like a BBS login: the newest episode as the headline, a dither band, the player and an .nfo box.')

commit_row = group(J(
    row(J(dyn('post-terms', term='post_tag', separator=', ', className='is-style-hash'), dyn('post-date', format='D j M Y'), dyn('post-terms', term='category', separator=' / ')),
        style={'spacing': {'blockGap': 'var:preset|spacing|30'}}),
    dyn('post-title', isLink=True, level=3, fontSize='large'),
    dyn('post-excerpt', excerptLength=30, moreText='', fontSize='small')),
    className='is-style-commit', layout={'type': 'default'}, style={'spacing': {'blockGap': 'var:preset|spacing|10'}})

pattern('commit-log', 'Episode log (commit log)', 'posts,query', group(J(
    para('git log --episodes', className='is-style-title-bar'),
    query(commit_row, per_page=6, query_id=6),
    para('<a href="/episodes/">All 88 episodes</a> or <a href="/guests/">browse by guest</a>', fontSize='small')),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|40'}}}),
    description='Every episode as a commit: episode number, date, topics, then the message.')

pattern('commit-log-archive', 'Episode log (inherits the page query)', 'posts,query', inherit_query(commit_row, align='wide'), inserter=False)

pattern('sysops', 'Sysops (the hosts)', 'team,about', box('sysops', columns(
    (None, J(image('mic.jpg', 'A person in headphones speaking into a desk microphone, with a laptop and printed notes', aspectRatio='4/3', scale='cover'),
             heading('Lieke Maes', 4), para('Backend developer at a public broadcaster in Brussels. Maintains a PDF library more governments use than she is comfortable with.', fontSize='small'))),
    (None, J(image('keyboard.jpg', 'The row of DIP switches on the back of a mechanical keyboard', aspectRatio='4/3', scale='cover'),
             heading('Kwame Mensah', 4), para('Frontend developer and accessibility lead in Ghent. Owns eleven keyboards and uses one.', fontSize='small'))))))

pattern('oneliners', 'Oneliners from listeners', 'testimonials', box('oneliners', J(
    lst(['<strong>tomas.p</strong> the printers episode made me apologise to our office printer',
         '<strong>ilse</strong> ep 86 is now required listening for our whole QA team',
         '<strong>kofi_b</strong> please do one on DNS. or don’t, i can’t take it',
         '<strong>marta w</strong> the soldering episode got me to buy a kit, 2 burns so far'], className='is-style-oneliners'),
    para('Send yours with the episode email. Printed as written, typos and all.', fontSize='x-small', textColor='muted'))))

pattern('greetz', 'Greetings to supporters', 'text', box('greetz', J(
    para('Thanks to everyone on the Major tier this month: Anneleen, Bart V., the Ghent Linux user group, Hilde, João, Katrien, the night shift at a hospital IT desk in Aalst who asked not to be named, Mehdi, Noor, Pieter-Jan, Sanne (not that Sanne), Wout and Yasmin.', fontSize='small'),
    para('<a href="/support/">Join them</a>', fontSize='small'))))

pattern('meetups', 'Meetups and live recordings', 'text', box('parties', J(
    lst(['<strong>Sat 17 Oct</strong> Live recording at FOSDEM fringe night, Brussels. Free, 80 seats.',
         '<strong>Fri 13 Nov</strong> Listener drinks after the Ghent hackerspace open evening, from 20:00.',
         '<strong>Feb 2027</strong> A table at the demoparty in Aalst. Bring a floppy.'], className='is-style-oneliners'))))

pattern('bbs-menu', 'Main menu (BBS style)', 'text', box('main menu', lst([
    '<a href="/episodes/"><strong>E</strong> Episodes, newest first</a>', '<a href="/guests/"><strong>G</strong> Guests and how to pitch</a>',
    '<a href="/changelog/"><strong>C</strong> Show changelog</a>', '<a href="/transcripts/"><strong>T</strong> Transcripts as text files</a>',
    '<a href="/support/"><strong>S</strong> Support and sponsors</a>', '<a href="/subscribe/"><strong>L</strong> Listen in an app</a>'], className='is-style-menu')))

pattern('downloads', 'Episode files', 'text', box('files', lst([
    '<a href="' + A_HOP + '">episode-88.mp3</a> 55.9 MB, 128 kbps, chapters embedded',
    '<a href="/transcripts/">episode-88.txt</a> 58 KB, corrected transcript',
    '<a href="/feed/">feed.xml</a> RSS, every episode'], className='is-style-oneliners')))

pattern('dither-band', 'Dither band', 'design', group('', layout={'type': 'default'}, className='is-style-dither', align='wide'),
        description='A stepped shading band, like ANSI block shading, to separate sections.')

pattern('boot-log', 'Boot log (what happens on release day)', 'text', box('release.log', lst([
    '<strong>Wed 19:30</strong> Record in Ghent, two microphones, one remote guest.',
    '<strong>Wed 23:00</strong> Rough edit by Lieke. Coffee.',
    '<strong>Thu 05:40</strong> Chapters, loudness, transcript pass.',
    '<strong>Thu 07:00</strong> Publish. RSS pings, email goes out.'], className='is-style-oneliners')))

pattern('tiers-boxes', 'Support tiers (boxes)', 'call-to-action', columns(
    (None, box('patch', J(para('€3', fontFamily='display', fontSize='xx-large'), para('a month. Ad-free feed.', fontSize='small')))),
    (None, box('minor', J(para('€6', fontFamily='display', fontSize='xx-large'), para('a month. Ad-free feed and the monthly “what we cut” episode.', fontSize='small')))),
    (None, box('major', J(para('€15', fontFamily='display', fontSize='xx-large'), para('a month. All of that, the planning Discord and your name in the greetz.', fontSize='small')))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|40'}}}))

pattern('guest-lines', 'Guest list (lines)', 'team,text', box('guests', lst(
    ['<strong>%s</strong> %s, episode %s' % (g[0], g[1], g[2].split('>')[1].split('<')[0]) for g in GUESTS], className='is-style-oneliners')))

pattern('screenshot', 'Screenshot or photo, phosphor treatment', 'media', image('terminal.jpg', 'A Philips telex terminal from 1985 with a small screen and a typewriter keyboard', caption='Philips telex terminal, 1985. Tekniska museet, CC0.'))

pattern('front-page-layout', 'Home: title screen, notes, commit log, boxes', 'featured', J(
    pattern_ref('title-screen'), pattern_ref('whats-in-it'), pattern_ref('commit-log'), pattern_ref('dither-band'),
    columns(('34%', J(pattern_ref('bbs-menu'), pattern_ref('meetups'))), ('33%', J(pattern_ref('guest-lines'), pattern_ref('greetz'))), ('33%', J(pattern_ref('oneliners'), pattern_ref('boot-log'))),
            align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|50'}, 'blockGap': {'left': 'var:preset|spacing|40'}}}),
    group(J(heading('Pay for the bandwidth', 2), para('€190 a month keeps it running. Open Collective shows every euro.', textColor='muted'), pattern_ref('tiers-boxes'),
            buttons(('Support on Open Collective', 'https://opencollective.com/'), ('Sponsor an episode', '/support/', {'className': 'is-style-outline'}))),
          align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}})), inserter=False)

pattern('episode-rail', 'Episode rail', 'audio', J(
    rail(), dyn('post-terms', term='post_tag', separator=', ', fontSize='large', style={'typography': {'fontWeight': '800'}}), dyn('post-date', format='l j F Y'), dyn('post-terms', term='category', separator=', '),
    dyn('post-featured-image', aspectRatio='4/3'),
    group(J(para('Listen in an app', fontSize='x-small', textColor='muted', style={'typography': {'fontWeight': '600'}}), listen_row())),
    group(J(para('Something wrong in this episode?', fontSize='x-small', textColor='muted', style={'typography': {'fontWeight': '600'}}),
            para('Email fixes@minorversion.example. It goes in next week’s “Fixed”.', fontSize='small')))), inserter=False)

# ---------------------------------------------------------------- parts
write('parts/header.html', J(template_part('status-line'), group(row(J(
    dyn('site-title', level=0),
    row(J(dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'}), buttons(('Subscribe', '/subscribe/'))),
        justify='right', style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
    justify='space-between', align='wide'), tag='header', align='full', className='is-style-rule-bottom',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})))
write('parts/status-line.html', pattern_ref('status-line'))

write('parts/footer.html', group(J(
    columns(('40%', J(para('Minor Version', fontSize='xx-large', fontFamily='display', textColor='accent', style={'typography': {'fontWeight': '700', 'lineHeight': '1'}}),
                     para('A weekly podcast about software and the people who keep it running. Recorded in Ghent on Wednesdays, out on Thursdays.', fontSize='small'))),
            (None, J(heading('Listen', 6), listen_row())),
            (None, J(heading('The show', 6), para('<a href="/changelog/">Show changelog</a><br><a href="/transcripts/">Transcripts</a><br><a href="/guests/">Guests</a><br><a href="/about/">About</a>', fontSize='small'))),
            (None, J(heading('Contact', 6), para('<a href="mailto:hello@minorversion.example">hello@minorversion.example</a><br>Corrections: fixes@minorversion.example<br>Minor Version VZW, Ghent', fontSize='small'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|50'}}}),
    para('Demo photos are CC0 or public domain from Wikimedia Commons. Stand-in audio is public domain, from the White House “As Told By” series.', fontSize='x-small', align='wide')),
    tag='footer', align='full', className='is-style-panel-full',
    style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': '0'}}}))

# ---------------------------------------------------------------- templates
PAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(pattern_ref('front-page-layout'), style={'spacing': {'margin': {'top': '0'}}}))
write('templates/home.html', page_template(J(
    columns(('26%', J(para('Every episode', fontSize='small', textColor='muted'), dyn('categories', className='is-style-tag-list'))),
            ('74%', J(heading('Release log', 1, fontSize='display'), para('Newest first. Each entry lists what we added, changed, fixed and cut. Topics are on the left.', fontSize='large'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('commit-log-archive')), style=PAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('commit-log-archive')), style=PAD))
write('templates/archive.html', page_template(J(
    columns(('26%', para('Filtered log', fontSize='small', textColor='muted')),
            ('74%', J(dyn('query-title', type='archive', showPrefix=False, fontSize='xx-large'), dyn('term-description'))),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    pattern_ref('commit-log-archive')), style=PAD))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search episodes', showLabel=False, placeholder='Postgres, on-call, printers', buttonText='Search', align='wide'),
    pattern_ref('commit-log-archive')), style=PAD))
write('templates/404.html', page_template(J(
    heading('404: no episode at this address', 1),
    para('We renamed some episode URLs when we moved off the old host in 2024. Search for a word from the title, or open the <a href="/episodes/">release log</a>.'),
    dyn('search', label='Search episodes', showLabel=False, placeholder='Postgres, on-call, printers', buttonText='Search')), style=PAD))

def page_head():
    return columns(('26%', para('Minor Version', fontSize='small', textColor='muted')), ('74%', dyn('post-title', level=1, fontSize='display')),
                   align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})
write('templates/page.html', page_template(J(page_head(), dyn('post-content', align='wide', layout={'type': 'constrained'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|50'}}})), style=PAD))
write('templates/page-wide.html', page_template(J(page_head(), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})), style=PAD))
write('templates/single.html', page_template(J(
    group(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-excerpt', fontSize='large')), align='wide', layout={'type': 'default'}),
    columns(('26%', pattern_ref('episode-rail')),
            ('74%', dyn('post-content', layout={'type': 'default'})),
            align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous episode', showTitle=True),
            dyn('post-navigation-link', label='Next episode', showTitle=True)),
          align='wide', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'},
          style={'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})),
    style=PAD))

write('style.css', '''/*
Theme Name: Patchnotes
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A podcast theme for technology and developer shows, with episodes laid out as release notes, a guest list and show notes sorted into added, changed, fixed and removed.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: patchnotes
Tags: blog, podcast, technology, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, two-columns
*/''')

# ---------------------------------------------------------------- demo content
def body_(url, chaps, added=None, changed=None, fixed=None, removed=None, guest=None, tr=None):
    parts = [audio(url, CAPS[url]), heading('Chapters', 3), chapters(url, chaps), heading('Show notes', 3), notes(added, changed, fixed, removed)]
    if guest:
        parts.append(group(J(para('Guest', fontSize='x-small', textColor='muted', style={'typography': {'fontWeight': '600'}}), heading(guest[0], 4), para(guest[1])), className='is-style-panel', layout={'type': 'default'}))
    if tr:
        parts += [heading('Transcript', 3), details('Read the transcript', J(*[para('<strong>%s</strong> %s' % (w, t)) for w, t in tr],
                                                                              para('Machine transcript, corrected by Lieke.', fontSize='x-small')))]
    return J(*parts)

EPS = [
 (88, 'The pager went off at 3am', 'the-pager-went-off-at-3am', 'racks.jpg', ['On-call', 'Incidents'],
  'Sanne Vermeulen has been on call for eleven years. She explains the incident review template she wrote after a payment queue ate 40,000 transfers.',
  body_(A_HOP, [(0, 'Intro, and what broke this week'), (262, 'Sanne’s first pager, 2014'), (905, 'The 40,000 transfers'), (1690, 'Writing the review template'), (2610, 'Rotas that don’t burn people out'), (3240, 'Picks')],
        added=['Sanne Vermeulen on writing an incident review nobody dreads.', '<a href="https://sre.google/sre-book/postmortem-culture/">The postmortem chapter of the Google SRE book</a>.'],
        changed=['Follow-up to episode 85: Jonas moved the last two services off the cloud. The bill went from €1,140 to €310 a month.'],
        fixed=['In episode 87 we said the PDF library had 14 maintainers. It has four. The other ten are bots.'],
        removed=['Twelve minutes of Lieke’s microphone falling off the desk.'],
        guest=('Sanne Vermeulen', 'Leads on-call for a payments company in Antwerp. Keeps a paper notebook for every incident since 2014.'),
        tr=[('Lieke', 'Sanne, what did you have for dinner the night of the 40,000 transfers?'), ('Sanne', 'Nothing. That’s the point. That’s why it’s the first question.')])),
 (87, 'Who maintains the PDF library?', 'who-maintains-the-pdf-library', 'cables.jpg', ['Open source', 'Maintenance'],
  'Tomás Ferreira maintains a library on most phones in Europe. He is paid for about six hours a month of it. We talk money, burnout and saying no.',
  body_(A_ENIAC, [(0, 'Intro'), (340, 'How Tomás became a maintainer by accident'), (1320, 'The six paid hours'), (2280, 'Saying no to a bank'), (2900, 'Picks')],
        added=['Tomás on the week a security report arrived during his wedding.', '<a href="https://opencollective.com/">Open Collective</a>, which pays his six hours.'],
        fixed=['Episode 86: the WCAG version is 2.2, not 2.1. Hana wrote in.'], guest=('Tomás Ferreira', 'Maintains an image-decoding library. Lives in Porto. Answers issues on Tuesdays only.'))),
 (86, 'Accessibility audits that get fixed', 'accessibility-audits-that-get-fixed', 'keyboard.jpg', ['Accessibility'],
  'Hana Novák has filed around 3,000 accessibility bugs. Most were never fixed. She explains how she writes the ones that are.',
  body_(A_ADA, [(0, 'Intro'), (410, 'Hana’s first audit'), (1500, 'The bug report template'), (2400, 'Keyboard-only Thursdays')],
        added=['Hana’s bug report template, with her permission.', 'Kwame’s rule: every pull request gets tested with the keyboard only.'],
        changed=['We now publish transcripts before the episode, not after.'], guest=('Hana Novák', 'Accessibility auditor in Brno. Screen reader user since 2009.'))),
 (85, 'Leaving the cloud, a bit', 'leaving-the-cloud-a-bit', 'hero.jpg', ['Infrastructure'],
  'Jonas Peeters moved a newspaper’s websites back onto its own servers. He is not evangelical about it. Here are the numbers.',
  body_(A_HOP, [(0, 'Intro'), (280, 'The €1,140 bill'), (1100, 'What stayed in the cloud and why'), (2200, 'The night the switch died')],
        added=['Jonas’s cost spreadsheet, month by month.'], removed=['The part where Kwame explains Kubernetes. He was wrong and he knows it.'],
        guest=('Jonas Peeters', 'Runs infrastructure for a Ghent newspaper. Has a rack in a basement near Sint-Pieters.'))),
 (84, 'Printers', 'printers', 'terminal.jpg', ['Hardware', 'Drivers'],
  'Nadia Haddad writes printer drivers. Everyone hates printers. Nadia explains why they are hard, and why that is mostly the paper’s fault.',
  body_(A_ENIAC, [(0, 'Intro'), (300, 'What a driver actually does'), (1400, 'Paper is a physical object'), (2500, 'Picks')],
        added=['Nadia’s list of printers she would buy with her own money. It has two entries.'], guest=('Nadia Haddad', 'Driver engineer in Liège. Has fixed a jam with a butter knife in front of a CEO.'))),
 (83, 'The ENIAC six', 'the-eniac-six', 'eniac.jpg', ['History', 'Special'],
  'A history special. Six women programmed the first general-purpose electronic computer in 1945 and were left out of the photos for decades.',
  body_(A_ENIAC, [(0, 'Intro'), (200, 'Philadelphia, 1945'), (1200, 'Programming by plugging cables'), (2100, 'The 1946 demonstration'), (2800, 'What we got wrong in our first draft')],
        added=['<a href="https://en.wikipedia.org/wiki/ENIAC">ENIAC on Wikipedia</a>, with the names: Kay McNulty, Betty Jennings, Betty Snyder, Marlyn Wescoff, Fran Bilas and Ruth Lichterman.'],
        fixed=['The first cut said ENIAC was the first computer. It was the first general-purpose electronic one. Kwame caught it.'])),
 (82, 'Soldering for software people', 'soldering-for-software-people', 'solder.jpg', ['Hardware'],
  'Ines Duarte teaches soldering to developers at a Lisbon hackerspace. She says the fear is the hardest part and the flux is the second.',
  body_(A_ADA, [(0, 'Intro'), (360, 'The first joint'), (1500, 'Kits that are worth it'), (2300, 'Burns, briefly')],
        added=['Ines’s starter kit list, all under €60.'], guest=('Ines Duarte', 'Hardware engineer. Runs a Thursday soldering night in Lisbon.'))),
 (81, 'Pagination is a UX problem', 'pagination-is-a-ux-problem', 'desk.jpg', ['Frontend', 'UX'],
  'Just the two of us, arguing about infinite scroll, cursor pagination and the “load more” button. Kwame wins, narrowly.',
  body_(A_HOP, [(0, 'Intro'), (420, 'Offsets and why they lie'), (1300, 'Load more, the button'), (2000, 'The footer you can never reach')],
        changed=['Lieke changed her mind about infinite scroll, on air, at 27:40.'])),
]
base = datetime.date(2026, 9, 24)
posts = []
for i, (n, title, slug, img, tags, ex, content) in enumerate(EPS):
    posts.append({'title': title, 'slug': slug, 'category': [t.lower().replace(' ', '-') for t in tags], 'tags': ['Episode %d' % n], 'image': img, 'excerpt': ex,
                  'date': (base - datetime.timedelta(days=7 * i)).isoformat(), 'content': content})

demo = {
    'site': {'title': 'Minor Version', 'tagline': 'A weekly podcast about software and the people who keep it running'},
    'categories': [{'slug': 'on-call', 'name': 'On-call'}, {'slug': 'incidents', 'name': 'Incidents'}, {'slug': 'open-source', 'name': 'Open source'}, {'slug': 'maintenance', 'name': 'Maintenance'}, {'slug': 'accessibility', 'name': 'Accessibility'}, {'slug': 'infrastructure', 'name': 'Infrastructure'}, {'slug': 'hardware', 'name': 'Hardware'}, {'slug': 'drivers', 'name': 'Drivers'}, {'slug': 'history', 'name': 'History'}, {'slug': 'special', 'name': 'Special'}, {'slug': 'frontend', 'name': 'Frontend'}, {'slug': 'ux', 'name': 'UX'}],
    'front_page': 'home', 'posts_page': 'episodes',
    'pages': [{'slug': 'home', 'title': 'Home', 'content': ''}, {'slug': 'episodes', 'title': 'Episodes', 'content': ''},
              {'slug': 'guests', 'title': 'Guests', 'pattern': 'patchnotes/guests-page'},
              {'slug': 'changelog', 'title': 'Show changelog', 'pattern': 'patchnotes/changelog-page'},
              {'slug': 'support', 'title': 'Support and sponsors', 'pattern': 'patchnotes/support-page'},
              {'slug': 'subscribe', 'title': 'Subscribe', 'pattern': 'patchnotes/subscribe-page'},
              {'slug': 'about', 'title': 'About', 'pattern': 'patchnotes/about-page'},
              {'slug': 'transcripts', 'title': 'Transcripts', 'pattern': 'patchnotes/transcripts-page'}],
    'posts': posts,
    'nav': [{'label': 'Episodes', 'url': '/episodes/'}, {'label': 'Guests', 'url': '/guests/'}, {'label': 'Show changelog', 'url': '/changelog/'},
            {'label': 'Support', 'url': '/support/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs('demos/patchnotes', exist_ok=True)
json.dump(demo, open('demos/patchnotes/content.json', 'w'), indent=1, ensure_ascii=False)
print('built patchnotes')
