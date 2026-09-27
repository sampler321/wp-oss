# Design note (reel, idea 034, independent filmmaker; owner's brief: heavily inspired by IFFR)
# Direction: a festival programme for one filmmaker's slate. A black utility strip over a bright teal band header,
#   a grey dates tab hanging under the name, grey rounded programme cards with an arrow notch, colour-coded category
#   chips and a bold facts line (director | runtime | countries | premiere) on every film.
# Fonts: Rethink Sans only (claimed in demos/reel/fonts-claim.txt; the brief replaces the research face), 800 for titles, 400 for text.
# Palette: #FFFFFF, #111111, teal band #00C2A8 (accent-2, always with black text), deep teal #00705F for links (accent),
#   #E8E8E8 card grey, chip colours for Documentary (blue), Fiction (pink), Shorts (lime) and In development (yellow).
# Layout idea: the front page is a festival home: lead film as a rounded still with a white card overlapping it,
#   a news column beside it, then a screenings list and the programme grid.
import sys, json, os, shutil
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('reel')

_image = image
def image(filename, alt, caption='', **kw):
    """blocks.image plus the inline aspect-ratio/object-fit style core saves, so the ratio survives normalising."""
    out = _image(filename, alt, caption, **kw)
    if kw.get('aspectRatio'):
        st = 'aspect-ratio:%s' % kw['aspectRatio'] + (';object-fit:%s' % kw['scale'] if kw.get('scale') else '')
        out = out.replace('<img ', '<img style="%s" ' % st, 1)
    return out
D = THEME['dir']
for sub in ('patterns', 'templates', 'parts', 'styles'):
    shutil.rmtree(os.path.join(D, sub), ignore_errors=True)

def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))

P = lambda s: 'var:preset|spacing|%s' % s
C = lambda slug: 'var:preset|color|%s' % slug
pad = lambda t, b=None: {'spacing': {'padding': {'top': P(t), 'bottom': P(b or t)}}}
pal = lambda rows: [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
fonts.append({'fontFamily': '"Rethink Sans", sans-serif', 'name': 'Rethink Sans (text)', 'slug': 'body'})
BASE = [('base', '#FFFFFF', 'Screen white'), ('contrast', '#111111', 'Projection black'), ('accent', '#00705F', 'Deep teal'),
        ('accent-2', '#00C2A8', 'Festival teal'), ('surface', '#E8E8E8', 'Programme grey'), ('line', '#111111', 'Rule'),
        ('muted', '#4F4F4F', 'Caption grey'), ('chip-doc', '#5AB0EA', 'Documentary blue'), ('chip-fiction', '#F2648D', 'Fiction pink'),
        ('chip-short', '#B7E34A', 'Shorts lime'), ('chip-dev', '#FFD43B', 'Development yellow')]

CSS = (
    ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}html{font-synthesis:none}'
    '.wp-block-post-excerpt,table{font-variant-numeric:tabular-nums}'
    '.wp-block-site-title{text-transform:uppercase;line-height:.95;max-width:12ch}'
    # date tab under the header
    '.is-style-date-tab{display:inline-block;border-radius:0 0 8px 8px}'
    # programme cards (post template)
    '.wp-block-post-template.is-style-programme{display:grid;grid-template-columns:repeat(auto-fill,minmax(16rem,1fr));gap:var(--wp--preset--spacing--40);list-style:none;padding:0}'
    '.is-style-programme>li{background:var(--wp--preset--color--surface);border-radius:8px;overflow:hidden;position:relative;margin:0;padding-bottom:3rem}'
    '.is-style-programme>li>*{margin-inline:1.25rem}.is-style-programme>li>.wp-block-post-featured-image{margin:0 0 1rem}'
    '.is-style-programme .wp-block-post-featured-image img{aspect-ratio:16/9;object-fit:cover;width:100%;height:auto;display:block}'
    '.is-style-programme>li::after,.is-style-notch::after{content:"\\2197";position:absolute;right:0;bottom:0;width:2.4rem;height:2.4rem;display:grid;place-items:center;background:var(--wp--preset--color--base);color:var(--wp--preset--color--contrast);border-top-left-radius:10px;font-weight:700;font-size:1.2rem}'
    '.is-style-notch{position:relative}'
    # also-in list (horizontal cards)
    '.wp-block-post-template.is-style-also-list{list-style:none;padding:0;display:grid;gap:var(--wp--preset--spacing--30)}'
    '.is-style-also-list>li{background:var(--wp--preset--color--surface);border-radius:8px;padding:1.25rem;margin:0;position:relative}'
    '.is-style-also-list .wp-block-post-featured-image img{border-radius:6px;aspect-ratio:16/9;object-fit:cover}'
    '.is-style-also-list>li::after{content:"\\2197";position:absolute;right:0;bottom:0;width:2.4rem;height:2.4rem;display:grid;place-items:center;background:var(--wp--preset--color--base);border-top-left-radius:10px;font-weight:700}'
    # chips: category links coloured by slug
    '.is-style-chip a{display:inline-block;padding:.1em .45em;border-radius:3px;font-weight:700;font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--contrast);background:var(--wp--preset--color--accent-2);text-decoration:underline}'
    '.is-style-chip a[href*="documentary"]{background:var(--wp--preset--color--chip-doc)}.is-style-chip a[href*="fiction"]{background:var(--wp--preset--color--chip-fiction)}'
    '.is-style-chip a[href*="shorts"]{background:var(--wp--preset--color--chip-short)}.is-style-chip a[href*="in-development"]{background:var(--wp--preset--color--chip-dev)}'
    '.is-style-chip .wp-block-post-terms__separator{display:none}'
    '.wp-block-categories.is-style-chip-list{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.6rem}.is-style-chip-list li{margin:0}'
    '.is-style-chip-list a{display:inline-block;padding:.35em .8em;border-radius:6px;font-weight:700;color:var(--wp--preset--color--contrast);background:var(--wp--preset--color--base);text-decoration:none;border:2px solid var(--wp--preset--color--contrast)}'
    '.is-style-chip-list .current-cat a{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'
    # outlined tags
    '.is-style-tag-outline{display:flex;flex-wrap:wrap;gap:.4rem}.is-style-tag-outline>p{margin:0;border:1.5px solid currentColor;border-radius:3px;padding:.05em .4em;font-weight:700;font-size:var(--wp--preset--font-size--x-small)}'
    # screenings table
    '.wp-block-table.is-style-screenings table{border-collapse:separate;border-spacing:0 .5rem;width:100%}'
    '.wp-block-table.is-style-screenings td,.wp-block-table.is-style-screenings th{border:0;padding:.9rem 1rem;text-align:left;vertical-align:middle}'
    '.wp-block-table.is-style-screenings tbody td{background:var(--wp--preset--color--surface)}'
    '.wp-block-table.is-style-screenings tbody td:first-child{border-radius:8px 0 0 8px;font-weight:800;white-space:nowrap}.wp-block-table.is-style-screenings tbody td:last-child{border-radius:0 8px 8px 0;text-align:right}'
    '.wp-block-table.is-style-screenings thead th{font-weight:700;font-size:var(--wp--preset--font-size--small);padding-bottom:0}'
    '.wp-block-table.is-style-screenings td:last-child a{display:inline-block;background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base);text-decoration:none;font-weight:700;padding:.45em .9em;border-radius:6px;white-space:nowrap}'
    '.wp-block-table.is-style-screenings td:last-child a::after{content:" \\2197"}'
    '.wp-block-table.is-style-screenings .past td{opacity:.55}'
    '.wp-block-table:not(.is-style-screenings) table{border-collapse:collapse}.wp-block-table:not(.is-style-screenings) td,.wp-block-table:not(.is-style-screenings) th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.45rem .8rem .45rem 0;text-align:left}'
    '.wp-block-table:not(.is-style-screenings) td:first-child{font-weight:700}'
    '@media (max-width:700px){.reel-hide-mobile{display:none!important}}'
    '.wp-block-quote cite{display:block;margin-top:.6rem;font-size:var(--wp--preset--font-size--small);font-style:normal;font-weight:700}'
    '.wp-block-button__link::after{content:" \\2197"}'
    '@media (max-width:700px){.wp-block-table.is-style-screenings thead{display:none}.wp-block-table.is-style-screenings tr{display:block;background:var(--wp--preset--color--surface);border-radius:8px;margin-bottom:.5rem;padding:.6rem 0}'
    '.wp-block-table.is-style-screenings tbody td{display:block;background:none;padding:.15rem 1rem;text-align:left!important;border-radius:0!important}}'
)

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1320px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(BASE), 'duotone': []},
        'typography': {'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False, 'fontFamilies': fonts, 'fontSizes': [
            {'slug': 'x-small', 'size': '0.875rem', 'name': 'Chip', 'fluid': False},
            {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
            {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
            {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.25rem', 'max': '1.5rem'}},
            {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.7rem', 'max': '2.25rem'}},
            {'slug': 'xx-large', 'size': '3.5rem', 'name': 'Title', 'fluid': {'min': '2.3rem', 'max': '3.5rem'}},
            {'slug': 'display', 'size': '6rem', 'name': 'Display', 'fluid': {'min': '2.8rem', 'max': '6rem'}}]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1rem, 2vw, 2rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 7vw, 5.5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'}]},
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
    },
    'styles': {
        'color': {'background': C('base'), 'text': C('contrast')},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '400'},
        'spacing': {'padding': {'left': P(40), 'right': P(40)}, 'blockGap': P(30)},
        'elements': {
            'link': {'color': {'text': C('contrast')}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': C('accent')}},
                     ':focus': {'outline': {'color': C('contrast'), 'offset': '2px', 'style': 'solid', 'width': '3px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '1.02', 'letterSpacing': '-0.025em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {'color': {'background': C('contrast'), 'text': C('base')}, 'border': {'radius': '6px', 'width': '0', 'style': 'solid'},
                       'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
                       'spacing': {'padding': {'top': '0.8em', 'bottom': '0.8em', 'left': '1.3em', 'right': '1.3em'}},
                       ':hover': {'color': {'background': C('accent'), 'text': C('base')}},
                       ':focus': {'outline': {'color': C('contrast'), 'offset': '3px', 'style': 'solid', 'width': '3px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.4'}, 'color': {'text': C('muted')}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '0'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '700'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'typography': {'textDecoration': 'none'}, 'color': {'text': C('contrast')}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-excerpt': {'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.45'}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/image': {'border': {'radius': '8px'}},
            'core/post-featured-image': {'border': {'radius': '8px'}},
            'core/cover': {'border': {'radius': '8px'}},
            'core/separator': {'color': {'text': C('line')}, 'border': {'width': '2px 0 0 0'}},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '700', 'lineHeight': '1.3'},
                           'border': {'left': {'color': C('accent-2'), 'width': '6px', 'style': 'solid'}}, 'spacing': {'padding': {'left': P(30)}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '800'},
                               'border': {'radius': '8px'}, 'color': {'background': C('surface')}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(20), 'bottom': P(20)}}},
            'core/search': {'border': {'radius': '6px'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '700'}},
        },
        'css': CSS,
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'}],
    'customTemplates': [{'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
jdump('theme.json', theme)

write('style.css', '''/*
Theme Name: Reel
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A festival-style site for independent filmmakers and small producers, with a film programme, screenings lists, a press page and host-a-screening details.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: reel
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')

def variation(name, title, changes):
    rows = [(s, changes.get(s, c), n) for s, c, n in BASE]
    jdump('styles/%s.json' % name, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': pal(rows)}}})
variation('harbour', 'Harbour blue', {'accent': '#0E3B5C', 'accent-2': '#7FC4F2', 'surface': '#E6ECF1', 'chip-doc': '#FFB347'})
variation('midnight', 'Midnight', {'base': '#121212', 'contrast': '#F5F3EF', 'accent': '#3FE0C8', 'accent-2': '#00C2A8', 'surface': '#222222', 'line': '#F5F3EF', 'muted': '#BDBDBD'})
variation('tiger', 'Tiger yellow', {'accent': '#7A5C00', 'accent-2': '#F2D300', 'surface': '#EFEDE4', 'chip-dev': '#00C2A8'})

def section(slug, title, types, styles):
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})
section('band', 'Festival band (teal)', ['core/group'], {'color': {'background': C('accent-2'), 'text': C('contrast')},
    'elements': {'link': {'color': {'text': C('contrast')}}, 'heading': {'color': {'text': C('contrast')}}}})
section('utility', 'Utility strip (black)', ['core/group'], {'color': {'background': C('contrast'), 'text': C('base')},
    'elements': {'link': {'color': {'text': C('base')}, 'typography': {'textDecoration': 'none'}}}, 'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'}})
section('date-tab', 'Date tab', ['core/paragraph'], {'color': {'background': C('surface'), 'text': C('contrast')}, 'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small'},
    'spacing': {'padding': {'top': P(20), 'bottom': P(20), 'left': P(40), 'right': P(40)}}})
section('card', 'Programme card (grey)', ['core/group', 'core/column'], {'color': {'background': C('surface'), 'text': C('contrast')}, 'border': {'radius': '8px'},
    'spacing': {'padding': {'top': P(40), 'bottom': P(40), 'left': P(40), 'right': P(40)}}})
section('white-card', 'White card', ['core/group'], {'color': {'background': C('base'), 'text': C('contrast')}, 'border': {'radius': '8px'},
    'spacing': {'padding': {'top': P(40), 'bottom': P(40), 'left': P(40), 'right': P(40)}}})
section('overlap-card', 'Card over the picture', ['core/group'], {'color': {'background': C('base'), 'text': C('contrast')}, 'border': {'radius': '8px'},
    'spacing': {'padding': {'top': P(40), 'bottom': P(40), 'left': P(40), 'right': P(40)}},
    'css': '&{position:relative;margin-top:-7rem!important;margin-left:var(--wp--preset--spacing--40);margin-right:var(--wp--preset--spacing--40)}'})
section('notch', 'Arrow notch', ['core/group', 'core/column'], {'spacing': {'padding': {'bottom': P(50)}}})
section('programme', 'Programme cards', ['core/post-template'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('also-list', 'Also in the programme', ['core/post-template'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('chip', 'Programme chip', ['core/post-terms', 'core/paragraph'], {'typography': {'fontSize': 'var:preset|font-size|x-small'}})
section('chip-list', 'Chip list', ['core/categories'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('tag-outline', 'Outlined tags', ['core/group'], {'spacing': {'blockGap': P(10)}})
section('screenings', 'Screenings list', ['core/table'], {'typography': {'fontSize': 'var:preset|font-size|small'}})
section('laurel', 'Laurel (text)', ['core/paragraph'], {
    'typography': {'fontWeight': '700', 'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.25', 'textAlign': 'center'},
    'border': {'left': {'color': C('contrast'), 'width': '3px', 'style': 'double'}, 'right': {'color': C('contrast'), 'width': '3px', 'style': 'double'}},
    'spacing': {'padding': {'top': P(10), 'bottom': P(10), 'left': P(30), 'right': P(30)}}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {'border': {'top': {'color': C('line'), 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(30)}, 'margin': {'top': P(60)}}})

# ---------------------------------------------------------------- patterns
IMG = {
    'still-1': ('still-1.jpg', 'A container ship lit up at night under the cranes of a harbour, reflected in black water'),
    'still-2': ('still-2.jpg', 'Morning fog lying in a river valley between wooded hills'),
    'still-4': ('still-4.jpg', 'Black and white night street in the rain, with a tram, wet tracks and a lit cigarette sign'),
    'still-5': ('still-5.jpg', 'Black and white portrait of an old man with a long white beard smoking a pipe'),
    'still-6': ('still-6.jpg', 'Snow on tall fir trees in a dense forest'),
    'still-7': ('still-7.jpg', 'A grey beach with dune grass and a breakwater on a new island'),
    'still-8': ('still-8.jpg', 'Satellite view of a coastline covered in thousands of greenhouse roofs'),
    'still-9': ('still-9.jpg', 'Inside a long old glasshouse with a tiled floor, rocks and plants'),
    'cinema-1': ('cinema-1.jpg', 'Black and white photo of an ornate cinema auditorium with a painted safety curtain'),
    'cinema-2': ('cinema-2.jpg', 'Three women threading reels on a large film projector in a projection room'),
    'set-1': ('set-1.jpg', 'A film crew with a camera and boom microphone filming two people sitting on a beach'),
}
def img(key, caption='', **kw):
    f, alt = IMG[key]
    return image(f, alt, caption, **kw)

FILM = 'Glasland'
FACTS = 'Noor Verbeek | 94\' | Netherlands, Belgium | 2026 | Dutch and Polish with English subtitles'

pattern('lead-film', 'Lead film: still with an overlapping card, and news beside it', 'featured', columns(
    ('72%', group(J(
        img('still-9', aspectRatio='16/10', scale='cover'),
        group(J(heading(FILM, 1, fontSize='xx-large'),
                para('Every tomato in a Dutch supermarket in February was picked by someone who lives in a caravan behind a greenhouse. Noor Verbeek spent two winters in the Westland with four of them.'),
                buttons(('Dates and tickets', '/screenings/'))), className='is-style-overlap-card', layout={'type': 'default'}, style={'spacing': {'blockGap': P(30)}})),
        layout={'type': 'default'}, style={'spacing': {'blockGap': '0'}})),
    ('28%', pattern_ref('news-cards')),
    align='wide', style={'spacing': {'blockGap': {'left': P(40)}, 'padding': {'top': P(50)}}}))

def news(title, date, tags, href):
    return group(J(heading('<a href="%s">%s</a>' % (href, title), 3, fontSize='medium'), para(date, fontSize='small'),
                   group(J(*[para(t) for t in tags]), className='is-style-tag-outline', layout={'type': 'flex', 'flexWrap': 'wrap'})),
                 className='is-style-card is-style-notch', layout={'type': 'default'}, style={'spacing': {'blockGap': P(20)}})
pattern('news-cards', 'News cards (date and outlined tags)', 'posts', group(J(
    news('Glasland opens in 14 Dutch and Belgian cinemas on 9 October', '22 September 2026', ['News', 'Release'], '/screenings/'),
    news('Noor Verbeek on filming at 4am, in the dark, with the lights off', '4 September 2026', ['Interview'], '/about/'),
    news('Community screenings: now booking for spring 2027', '28 August 2026', ['Host a screening'], '/host-a-screening/')),
    layout={'type': 'default'}, style={'spacing': {'blockGap': P(30)}}))

screenings = [
    ('Thu 9 Oct', 'Rotterdam', 'LantarenVenster', 'Premiere, Q&A with Noor Verbeek and Youssef Tahiri', 'https://www.lantarenvenster.nl/'),
    ('Fri 10 Oct', 'Amsterdam', 'Eye Filmmuseum', 'Q&A with Noor Verbeek', 'https://www.eyefilm.nl/'),
    ('Sat 11 Oct', 'Utrecht', 'Louis Hartlooper Complex', '', 'https://www.louishartlooper.nl/'),
    ('Sun 12 Oct', 'Naaldwijk', 'Theater de Naald', 'Screening with the people in the film', 'https://www.theaterdenaald.nl/'),
    ('Thu 16 Oct', 'Nijmegen', 'LUX', '', 'https://www.lux-nijmegen.nl/'),
    ('Fri 17 Oct', 'Ghent', 'Studio Skoop', 'Dutch with French subtitles', 'https://www.studioskoop.be/'),
    ('Sat 25 Oct', 'Groningen', 'Forum Groningen', 'Q&A with editor Kasia Nowicka', 'https://forum.nl/'),
    ('Thu 6 Nov', 'Antwerp', 'De Cinema', '', 'https://www.decinema.be/'),
]
pattern('screenings-list', 'Screenings: date, city, venue and a ticket link per row', 'films', group(J(
    heading('Screenings of %s' % FILM, 2, fontSize='x-large'),
    table([[d, c, v + (('<br><small>%s</small>' % n) if n else ''), '<a href="%s">Tickets</a>' % u] for d, c, v, n, u in screenings],
          head=['Date', 'City', 'Venue', 'Tickets'], className='is-style-screenings', align='wide'),
    para('Past dates move to the archive at the end of each month. Venues set their own ticket prices, usually €9 to €12.', fontSize='small', textColor='muted')),
    align='wide', layout={'type': 'default'}), description='The signature pattern: every screening with city, venue, a note and one ticket link.')

pattern('screenings-archive', 'Past screenings (festivals)', 'films', group(J(
    heading('Where it has played', 4),
    table([['Jan 2026', 'Rotterdam', 'World premiere, Harbour Screens programme'], ['Mar 2026', 'Copenhagen', 'Nordic Docs, competition'],
           ['Apr 2026', 'Kraków', 'Wisła Film Days, special screening'], ['Jun 2026', 'Middelburg', 'Zeeland Doc Days, best documentary']], className='is-style-screenings')),
    align='wide', layout={'type': 'default'}))

def facts_line(text):
    return para(text, style={'typography': {'fontWeight': '800'}})
pattern('film-header', 'Film header (title, chip, facts line)', 'films', group(J(
    img('still-8', aspectRatio='2.39', scale='cover', align='wide'),
    heading(FILM, 1, align='wide'),
    row(J(para('<a href="/category/documentary/">Documentary</a>', className='is-style-chip'), para('<a href="/category/documentary/">Feature</a>', className='is-style-chip')), align='wide'),
    group(facts_line(FACTS), align='wide', layout={'type': 'default'})), align='wide', layout={'type': 'default'}))

pattern('laurels', 'Festival laurels as text', 'films', row(J(
    para('World premiere<br>Harbour Screens<br>Rotterdam 2026', className='is-style-laurel'),
    para('Competition<br>Nordic Docs<br>Copenhagen 2026', className='is-style-laurel'),
    para('Best documentary<br>Zeeland Doc Days<br>2026', className='is-style-laurel')), style={'spacing': {'blockGap': P(30)}}),
    description='Laurels set as text, so a new selection is a new paragraph, not a new image.')

pattern('press-quotes', 'Press quotes with outlet and rating', 'testimonials', columns(
    (None, quote('Verbeek films the greenhouses like cathedrals and the workers like the only people awake in the world.', 'de Volkskrant, 4 out of 5, Joost Mulder')),
    (None, quote('Ninety-four minutes, almost no talking, and I could not look away.', 'Filmkrant, Anna Wiśniewska')),
    (None, quote('The best Dutch documentary of the year so far.', 'NRC, 4 out of 5, Bram de Wit')), align='wide'))

pattern('synopsis', 'Synopsis and credits', 'films', columns(
    ('62%', J(heading('Synopsis', 3),
              para('The Westland, south of The Hague, is 2,000 hectares of glass. At night it glows orange and can be seen from space. Marta, Piotr, Oleksandra and Dawid pick, pack and sleep there on eight-month contracts.'),
              para('Filmed over two winters with a small crew and no extra light, Glasland follows them from the first harvest in December to the day in August when the contracts end.'))),
    ('38%', J(heading('Credits', 3), table([['Director', 'Noor Verbeek'], ['Producer', 'Youssef Tahiri'], ['Camera', 'Jonas Leemans'], ['Editor', 'Kasia Nowicka'],
                                               ['Sound', 'Femke Oudshoorn'], ['Music', 'Ilya Marchenko'], ['Co-production', 'Lumen Doc, Ghent']]))),
    align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('stills-gallery', 'Stills gallery', 'films,gallery', J(
    heading('Stills', 3),
    gallery([('still-9.jpg', IMG['still-9'][1], 'The old glasshouse in Poeldijk, used as a canteen'), ('still-8.jpg', IMG['still-8'][1], 'The Westland from above, Landsat, 2019'),
             ('still-2.jpg', IMG['still-2'][1], 'Fog over the Maas, the drive to work at 5am')], columns=3, align='wide')))

pattern('where-to-watch', 'Where to watch', 'films', group(J(
    heading('Where to watch', 4),
    para('In cinemas in the Netherlands and Belgium from 9 October. On streaming from spring 2027. We will post the platform here when the contract is signed, not before.')),
    className='is-style-card', layout={'type': 'default'}))

pattern('press-kit', 'Press kit and screener request', 'films', group(J(
    heading('Press', 3),
    para('The press kit (PDF, 6 MB), high-resolution stills and a screener link are sent on request, the same working day. Write to Lotte at <a href="mailto:press@example.com">press@example.com</a> with the outlet you write for.'),
    para('The press page on this site can be password protected. In WordPress, open the page, set Visibility to Password protected, and send journalists the password with the screener.', fontSize='small', textColor='muted')),
    className='is-style-card is-style-notch', layout={'type': 'default'}), description='Replaces a public download link. The press page itself can be password protected in WordPress.')

pattern('host-screening', 'Host a screening: what it costs and what we need', 'call-to-action', columns(
    ('50%', J(heading('Host a screening', 2), para('Film clubs, libraries, universities and unions can show any of our films. We send a DCP or a ProRes file, a poster file and, if you like, one of us for a Q&A.'),
              buttons(('Email to book a screening', 'mailto:screenings@example.com?subject=Screening')))),
    ('50%', J(table([['Community group or library', '€150'], ['University or school', '€300'], ['Cinema, single screening', '60% of box office, minimum €100'], ['Q&A with Noor, in the Netherlands', 'Travel costs only']], head=['Who', 'Fee']),
              para('Tell us your name, organisation, city, the film, the date and roughly how many people. We answer within a week. We don\'t do screenings on phones or laptops for more than ten people, sorry.', fontSize='small'))),
    align='wide', className='is-style-card', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('host-band', 'Host a screening (teal band)', 'call-to-action', group(J(
    columns(('60%', J(heading('Show Glasland in your town', 2), para('Community screenings from €150, with a DCP, a poster and a Q&A if you want one.', fontSize='large'))),
            ('40%', buttons(('How to host a screening', '/host-a-screening/'))), align='wide', verticalAlignment='center')),
    tag='section', align='full', className='is-style-band', style=pad(60), layout={'type': 'constrained'}))

pattern('programme-grid', 'Programme: all films as cards', 'films,query', group(J(
    row(J(heading('Films', 2), para('<a href="/films/">Programme A to Z</a>', style={'typography': {'fontWeight': '700'}})), justify='space-between', align='wide'),
    query(J(dyn('post-featured-image', isLink=True), dyn('post-title', isLink=True, level=3, fontSize='large'),
            dyn('post-terms', term='category', className='is-style-chip'), dyn('post-excerpt', excerptLength=16, moreText='')),
          per_page=8, template_class='is-style-programme', align='wide')),
    align='wide', layout={'type': 'default'}), keywords='films, programme, grid')
pattern('programme-archive', 'Programme cards (inherits the page query)', 'films,query', inherit_query(
    J(dyn('post-featured-image', isLink=True), dyn('post-title', isLink=True, level=3, fontSize='large'),
      dyn('post-terms', term='category', className='is-style-chip'), dyn('post-excerpt', excerptLength=16, moreText='')),
    template_class='is-style-programme', align='wide'), inserter=False)
pattern('also-in-programme', 'Also in the programme (horizontal cards)', 'films,query', group(J(
    heading('Also in the programme', 3),
    query(columns(('34%', dyn('post-featured-image', isLink=True)),
                  ('66%', J(dyn('post-title', isLink=True, level=4, fontSize='large'), dyn('post-terms', term='category', className='is-style-chip'), dyn('post-excerpt', excerptLength=18, moreText=''))),
                  style={'spacing': {'blockGap': {'left': P(30)}}}),
          per_page=3, template_class='is-style-also-list', query_id=4).replace('"offset":0', '"offset":1')),
    align='wide', layout={'type': 'default'}), inserter=False)

pattern('category-filter', 'Programme filter (chips)', 'films', group(
    dyn('categories', className='is-style-chip-list'), align='wide', className='is-style-card', layout={'type': 'default'}, style={'spacing': {'padding': {'top': P(30), 'bottom': P(30)}}}))

pattern('about-maker', 'About the filmmaker', 'about', columns(
    ('58%', J(para('Noor Verbeek (b. 1986, Schiedam) makes documentaries and short fiction about people who work at night. She studied at the Netherlands Film Academy and lives in Delfshaven, Rotterdam.', fontSize='large'),
              para('She runs Verbeek & Tahiri Films with producer Youssef Tahiri from a former ship chandler\'s office on the Voorhaven. They make one feature every three years and a short in between. They finance through the Netherlands Film Fund, the Flanders Audiovisual Fund and whoever else will listen.'),
              para('She shoots without added light whenever she can, which is why most of her films look like 4am. She does not make commercials.'))),
    ('42%', img('set-1', 'On set for Marker Wadden, 2020')),
    align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('contact-cards', 'Contacts (sales, press, screenings)', 'contact', columns(
    (None, group(J(heading('Production', 5), para('Verbeek & Tahiri Films<br>Voorhaven 22, 3024 RM Rotterdam<br><a href="mailto:office@example.com">office@example.com</a><br>+31 10 123 4567')), className='is-style-card', layout={'type': 'default'})),
    (None, group(J(heading('Press', 5), para('Lotte Brandsma<br><a href="mailto:press@example.com">press@example.com</a><br>+31 6 1234 5678')), className='is-style-card', layout={'type': 'default'})),
    (None, group(J(heading('Screenings and sales', 5), para('Youssef Tahiri<br><a href="mailto:screenings@example.com">screenings@example.com</a><br>Festivals, community screenings, broadcasters')), className='is-style-card', layout={'type': 'default'})),
    align='wide'))

pattern('newsletter', 'Newsletter', 'call-to-action', group(J(
    heading('Screening dates by email', 4),
    para('One email when a film opens and one when it comes to a town near you. Send your city to <a href="mailto:dates@example.com?subject=Dates">dates@example.com</a>. About six emails a year.')),
    className='is-style-card is-style-notch', layout={'type': 'default'}, anchor='newsletter'))

pattern('notice-premiere', 'Notice: premiere date', 'banner', group(
    para('Glasland opens in cinemas on 9 October. The Rotterdam premiere at LantarenVenster is sold out, a second screening is added on 12 October.', fontSize='small', style={'typography': {'fontWeight': '700'}}),
    tag='aside', align='full', className='is-style-utility', style=pad(20), layout={'type': 'constrained'}), description='A one-line notice. Remove it after the premiere.')

pattern('film-page-glasland', 'Film page: Glasland (full)', 'films', J(
    pattern_ref('laurels'), pattern_ref('synopsis'), pattern_ref('press-quotes'), pattern_ref('screenings-list'), pattern_ref('stills-gallery'),
    columns((None, pattern_ref('where-to-watch')), (None, pattern_ref('press-kit')), align='wide'), pattern_ref('screenings-archive')),
    block_types='core/post-content', description='Everything for one film: laurels, synopsis, credits, quotes, screenings, stills and press.')

# pages
pattern('page-screenings', 'Page: screenings', 'films', J(para('Where our films are on now, in cinemas and at festivals. Every row has its own ticket link. Past dates move to the archive at the end of the month.', fontSize='large'),
    pattern_ref('screenings-list'), pattern_ref('screenings-archive'), pattern_ref('newsletter')), block_types='core/post-content')
pattern('page-host', 'Page: host a screening', 'call-to-action', J(pattern_ref('host-screening'), heading('Questions hosts ask', 3),
    details('Do we need a cinema projector?', para('No. A good beamer and a proper sound system are fine for up to 150 people. We send a ProRes file on a USB stick or by download.')),
    details('Can we charge for tickets?', para('Yes. Keep what you take. The fee stays the same.')),
    details('Can Noor come?', para('Usually, in the Netherlands and Flanders, if you cover the train. Abroad, ask us.'))), block_types='core/post-content')
pattern('page-press', 'Page: press', 'films', J(para('For journalists and programmers. Stills, the press kit and screener links are sent by email on request, the same working day.', fontSize='large'),
    pattern_ref('press-kit'), pattern_ref('press-quotes'), pattern_ref('stills-gallery')), block_types='core/post-content')
pattern('page-about', 'Page: about', 'about', J(pattern_ref('about-maker'), pattern_ref('contact-cards')), block_types='core/post-content')

# ---------------------------------------------------------------- parts
write('parts/header.html', J(
    group(row(J(para('<a href="/press/">Press</a>'), para('<a href="/screenings/#newsletter">Screening dates by email</a>'), para('<a href="https://www.instagram.com/">Instagram</a>', className='reel-hide-mobile')), justify='right', style={'spacing': {'blockGap': P(40)}}, align='wide'),
          tag='div', align='full', className='is-style-utility', style=pad(10), layout={'type': 'constrained'}),
    group(row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile'),
                buttons(('Host a screening', '/host-a-screening/'), className='reel-hide-mobile')), justify='space-between', align='wide', wrap=False),
          tag='header', align='full', className='is-style-band', style=pad(30), layout={'type': 'constrained'}),
    group(para('On tour: 9 October to 6 November 2026', className='is-style-date-tab'), align='full', layout={'type': 'constrained'}, tag='div',
          style={'spacing': {'margin': {'top': '0'}}})))

write('parts/footer.html', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0, fontSize='x-large'), para('Documentaries and short fiction from a small production company on the Voorhaven, Rotterdam.', fontSize='small'))),
        (None, J(heading('Visit', 6), para('Voorhaven 22<br>3024 RM Rotterdam<br>By appointment, weekdays', fontSize='small'))),
        (None, J(heading('Write', 6), para('<a href="mailto:office@example.com">office@example.com</a><br><a href="mailto:press@example.com">press@example.com</a><br><a href="mailto:screenings@example.com">screenings@example.com</a><br><a href="https://www.instagram.com/">Instagram</a>', fontSize='small'))),
        align='wide'),
    para('Demo stills are public domain photographs from Wikimedia Commons and NASA, standing in for the films. The films, people and festivals named are invented.', align='wide', fontSize='x-small')),
    tag='footer', align='full', className='is-style-utility', style={'spacing': {'padding': {'top': P(60), 'bottom': P(40)}, 'margin': {'top': P(70)}}}, layout={'type': 'constrained'}))
write('parts/notice.html', pattern_ref('notice-premiere'))

# ---------------------------------------------------------------- templates
def tpl(name, inner, top=50, bottom=70):
    write('templates/%s.html' % name, page_template(inner, style=pad(top, bottom)))

write('templates/front-page.html', page_template(J(
    pattern_ref('lead-film'),
    group(pattern_ref('screenings-list'), align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    group(pattern_ref('programme-grid'), align='wide', className='is-style-rule-top', layout={'type': 'default'}),
    spacer(), pattern_ref('host-band')), style={'spacing': {'padding': {'bottom': '0'}}}))
tpl('home', J(heading('Programme A to Z', 1, align='wide'), pattern_ref('category-filter'), pattern_ref('programme-archive')))
tpl('archive', J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('category-filter'), pattern_ref('programme-archive')))
tpl('index', J(dyn('query-title', type='archive', align='wide'), pattern_ref('programme-archive')))
tpl('search', J(dyn('query-title', type='search', align='wide'), dyn('search', label='Search', showLabel=False, placeholder='A film, a town, a name', buttonText='Search', align='wide'), pattern_ref('programme-archive')))
tpl('404', J(heading('This reel is missing', 1), para('The page moved or never existed. The <a href="/films/">programme</a> and the <a href="/screenings/">screenings list</a> are up to date.'),
             dyn('search', label='Search', showLabel=False, placeholder='A film, a town, a name', buttonText='Search')))
tpl('page', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained'})))
tpl('page-wide', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'})))
tpl('single', J(
    para('<a href="/">Home</a> / <a href="/films/">Films</a>', fontSize='small', align='wide'),
    dyn('post-featured-image', align='wide', aspectRatio='2.39'),
    group(J(dyn('post-title', level=1), dyn('post-terms', term='category', className='is-style-chip'), dyn('post-excerpt', moreText='', fontSize='large')),
          align='wide', layout={'type': 'default'}),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1320px'}),
    pattern_ref('also-in-programme')), top=30)
print('reel built')

# ---------------------------------------------------------------- demo content
def film(title, cat, img_, facts, paras, date, pattern_=None):
    d = {'title': title, 'category': cat, 'image': img_, 'excerpt': facts, 'date': date}
    if pattern_:
        d['pattern'] = pattern_
    else:
        d['content'] = J(*[para(p) for p in paras])
    return d
posts = [
    film('Glasland', 'documentary', 'still-8.jpg', FACTS, [], '2026-09-20', 'reel/film-page-glasland'),
    film('Wit woud', 'in-development', 'still-6.jpg', 'Noor Verbeek | feature, about 90\' | Netherlands, Poland | shooting winter 2027', ['A forest ranger in the Białowieża forest counts bison in the snow for the last season before she retires. In development with support from the Netherlands Film Fund.', 'We are looking for a Polish co-producer. Write to Youssef.'], '2026-06-12'),
    film('Nachttram', 'fiction', 'still-4.jpg', 'Noor Verbeek | 18\' | Netherlands | 2024 | Dutch with English subtitles', ['A tram driver on the last line of the night lets a boy ride to the depot and back, twice. Shot in black and white on the number 8.', 'Screened at 22 festivals. Available for community screenings.'], '2024-11-02'),
    film('Mist boven de Maas', 'shorts', 'still-2.jpg', 'Noor Verbeek | 22\' | Netherlands | 2023 | no dialogue', ['Five mornings of fog on the river, filmed from the same bridge at the same minute. A short about waiting for something to become visible.'], '2023-10-08'),
    film('Amazonehaven', 'fiction', 'still-1.jpg', 'Noor Verbeek | 101\' | Netherlands, Belgium | 2022 | Dutch and Tagalog with English subtitles', ['A Filipino cook on a container ship has 36 hours in Rotterdam and one address. Her first feature, produced with Youssef Tahiri.', 'Released in Dutch and Flemish cinemas. Streaming on a Dutch public platform until 2027.'], '2022-09-15'),
    film('De oude visser', 'documentary', 'still-5.jpg', 'Noor Verbeek | 14\' | Netherlands | 2021 | Dutch with English subtitles', ['Arie Kooiman fished out of Scheveningen for 51 years. He smokes one pipe a day and tells one story per pipe.'], '2021-05-20'),
    film('Marker Wadden', 'shorts', 'still-7.jpg', 'Noor Verbeek | 11\' | Netherlands | 2020 | no dialogue', ['An island built from mud in the Markermeer, three years after it was made. The birds found it before the people did.'], '2020-08-01'),
    film('Het doek', 'documentary', 'cinema-1.jpg', 'Youssef Tahiri | 52\' | Netherlands | 2019 | Dutch with English subtitles', ['The last projectionists of a Rotterdam cinema before it went digital. Directed by Youssef, produced by Noor, for once the other way round.'], '2019-03-11'),
]
content = {
    'site': {'title': 'Verbeek & Tahiri Films', 'tagline': 'Documentaries and short fiction, Rotterdam'},
    'categories': [{'slug': 'documentary', 'name': 'Documentary'}, {'slug': 'fiction', 'name': 'Fiction'}, {'slug': 'shorts', 'name': 'Shorts'}, {'slug': 'in-development', 'name': 'In development'}],
    'front_page': 'home', 'posts_page': 'films',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'films', 'title': 'Films', 'content': ''},
        {'slug': 'screenings', 'title': 'Screenings', 'pattern': 'reel/page-screenings'},
        {'slug': 'host-a-screening', 'title': 'Host a screening', 'pattern': 'reel/page-host'},
        {'slug': 'press', 'title': 'Press', 'pattern': 'reel/page-press'},
        {'slug': 'about', 'title': 'About', 'pattern': 'reel/page-about'},
    ],
    'posts': posts,
    'nav': [{'label': 'Films', 'url': '/films/'}, {'label': 'Screenings', 'url': '/screenings/'}, {'label': 'Press', 'url': '/press/'}, {'label': 'About', 'url': '/about/'}],
}
os.makedirs('demos/reel', exist_ok=True)
json.dump(content, open('demos/reel/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written')
