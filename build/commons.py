# commons: artist-run space / collective (idea 012)
# Direction: "daylight on the gallery floor". The owner asked for prettier, less brutal and image heavy, so the
#   photocopied notice board becomes a picture-led programme: installation views run big and full bleed, and the
#   running show numbers stay as the one archival habit.
# Fonts: Funnel Display (registry face, used light at 400 to 500 rather than 800) and Funnel Sans for text, with tabular figures for numbers.
# Palette: pale limewash #F4F3EE, soot #1F201C, kiln orange #B23A17 for links, peach #F5CDB9 for the "now on" card, sage #E3E7DC.
# Layout idea: the current show is a full-bleed photograph with a soft peach label card sitting in its bottom corner,
#   like the vinyl wall text at the door; everything after it is image first, with big running numbers.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
from blocks import _a
import blocks as _b


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
set_theme('commons')
S = THEME['slug']
D = THEME['dir']
import shutil
for _d in ('patterns', 'templates', 'parts', 'styles'):
    shutil.rmtree(os.path.join(D, _d), ignore_errors=True)  # rebuilt below; drops stale files

# ---------------------------------------------------------------- tokens
PAL = [
    ('base', '#F4F3EE', 'Limewash'),
    ('contrast', '#1F201C', 'Soot'),
    ('accent', '#B23A17', 'Kiln orange'),
    ('accent-2', '#F5CDB9', 'Peach label'),
    ('surface', '#E3E7DC', 'Sage wall'),
    ('line', '#C9CBC0', 'Pencil line'),
    ('muted', '#5B5C54', 'Graphite'),
    ('white', '#FFFFFF', 'White'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))
fam = {f['slug']: f for f in fonts['fontFamilies']}
fam['display']['name'] = 'Funnel Display'
fam['body']['name'] = 'Funnel Sans'


def pal(rows):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]


def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d


theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1400px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'writingMode': False,
            'fontFamilies': [fam['display'], fam['body']],
            'fontSizes': [
                fs('x-small', '0.875rem', 'Label'),
                fs('small', '1rem', 'Small'),
                fs('medium', '1.1875rem', 'Body'),
                fs('large', '1.625rem', 'Large', '1.3rem'),
                fs('x-large', '2.5rem', 'Section', '1.9rem'),
                fs('xx-large', '4rem', 'Title', '2.6rem'),
                fs('display', '7.5rem', 'Display', '2.6rem'),
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False,
            'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'},
                {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'},
                {'slug': '40', 'size': 'clamp(1.25rem, 2.2vw, 1.75rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.75rem, 3.5vw, 2.75rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2.5rem, 6vw, 4.5rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3.5rem, 8vw, 7rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(5rem, 12vw, 10rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True,
                   'radiusSizes': [{'slug': 'image', 'size': '14px', 'name': 'Image'}, {'slug': 'card', 'size': '18px', 'name': 'Card'}, {'slug': 'button', 'size': '6px', 'name': 'Button'}]},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.55', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|contrast'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'lineHeight': '1', 'letterSpacing': '-0.025em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'fontWeight': '400', 'lineHeight': '0.92'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large', 'lineHeight': '1.05'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.15', 'letterSpacing': '-0.01em'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '600', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '400', 'lineHeight': '1.4', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                'border': {'radius': '6px', 'width': '0', 'style': 'none'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.8em', 'bottom': '0.8em', 'left': '1.3em', 'right': '1.3em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|white'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}},
            },
            'caption': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.02em', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/image': {'border': {'radius': '14px'}},
            'core/post-featured-image': {'border': {'radius': '14px'}},
            'core/cover': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '400', 'lineHeight': '1.25'},
                           'border': {'left': {'color': 'var:preset|color|accent-2', 'width': '6px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|x-large', 'fontWeight': '400', 'lineHeight': '1.1'},
                               'border': {'width': '0', 'style': 'none'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/query-pagination': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'}},
            'core/search': {'border': {'radius': '6px'}, 'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/categories': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/archives': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': (':where(h1,h2,h3,h4){text-wrap:balance}.wp-block-table,.is-style-running-number,.wp-block-post-date,.wp-block-post-excerpt{font-variant-numeric:tabular-nums lining-nums}:where(p){text-wrap:pretty}body{font-synthesis:none}'
                '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.7em .6em .7em 0;text-align:left;vertical-align:top}'
                '.wp-block-table thead{border:0}.wp-block-table th{font-family:var(--wp--preset--font-family--body);font-weight:400;font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--muted)}'
                '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--accent-2);color:var(--wp--preset--color--contrast)}'
                '.wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--x-large)}'
                '.wp-block-navigation .current-menu-item>a{text-decoration:underline;text-underline-offset:.3em}'
                '.wp-block-post-featured-image img,.wp-block-image img{transition:none}'
                '@media (prefers-reduced-motion:no-preference){.wp-block-post-featured-image a img{transition:opacity .2s}.wp-block-post-featured-image a:hover img{opacity:.88}}'
                '.wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:6px;background:var(--wp--preset--color--white)}'
                ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'),
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
        {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'page-plain', 'title': 'Page, no title', 'postTypes': ['page']},
    ],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Commons
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A picture-led site for artist-run spaces and collectives, with a numbered programme archive, membership, opportunities and a committee page.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: commons
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, one-column, grid-layout
*/''')


def variation(fname, title, rows):
    write('styles/%s.json' % fname, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                                'settings': {'color': {'palette': pal(rows)}}}, indent='\t', ensure_ascii=False))


variation('green-room', 'Green room', [
    ('base', '#F2F4EF', 'Limewash'), ('contrast', '#18221B', 'Soot'), ('accent', '#1E5631', 'Kiln orange'),
    ('accent-2', '#C9DFC8', 'Peach label'), ('surface', '#DDE7DA', 'Sage wall'), ('line', '#BFCBBB', 'Pencil line'),
    ('muted', '#4E5A50', 'Graphite'), ('white', '#FFFFFF', 'White')])
variation('carbon', 'Carbon', [
    ('base', '#161614', 'Limewash'), ('contrast', '#F1F0EA', 'Soot'), ('accent', '#FF8A5C', 'Kiln orange'),
    ('accent-2', '#3B2A22', 'Peach label'), ('surface', '#23241F', 'Sage wall'), ('line', '#3A3B35', 'Pencil line'),
    ('muted', '#B3B2A8', 'Graphite'), ('white', '#161614', 'White')])
variation('pastel', 'Pastel', [
    ('base', '#FBF8EC', 'Limewash'), ('contrast', '#1B1B1B', 'Soot'), ('accent', '#8A4B00', 'Kiln orange'),
    ('accent-2', '#F7E9A0', 'Peach label'), ('surface', '#EAE4F2', 'Sage wall'), ('line', '#D7D1C2', 'Pencil line'),
    ('muted', '#58564F', 'Graphite'), ('white', '#FFFFFF', 'White')])


def section(slug, title, block_types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug,
                                                        'blockTypes': block_types, 'styles': styles}, indent='\t', ensure_ascii=False))


PAD = {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}
section('label-card', 'Label card', ['core/group', 'core/column'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
    'border': {'radius': '18px'},
    'spacing': {'padding': PAD},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}}})
section('overlap-card', 'Overlapping label card', ['core/group'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
    'border': {'radius': '18px'},
    'spacing': {'padding': PAD},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}},
    'css': '&{position:relative;margin-top:calc(-1 * var(--wp--preset--spacing--80))!important;max-width:34rem;margin-left:0!important}'})
section('crop-wide', 'Wide crop', ['core/image'], {'css': '& img{aspect-ratio:21/9;object-fit:cover;width:100%;border-radius:0}'})
section('sage', 'Sage wall', ['core/group', 'core/columns', 'core/media-text'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'border': {'radius': '18px'},
    'spacing': {'padding': PAD}})
section('soot', 'Soot', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|accent-2'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                 'button': {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}})
section('running-number', 'Running number', ['core/post-terms', 'core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '400', 'fontSize': 'var:preset|font-size|large', 'lineHeight': '1', 'letterSpacing': '-0.02em'},
    'color': {'text': 'var:preset|color|accent'},
    'elements': {'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'none'}}}})
section('ruled', 'Ruled rows', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}})
section('pill-list', 'Filter chips', ['core/categories', 'core/archives'], {
    'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small'},
    'css': '&{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.5rem}& li a{display:inline-block;padding:.45em .9em;border:1px solid var(--wp--preset--color--contrast);border-radius:6px;text-decoration:none;color:var(--wp--preset--color--contrast)}& li a:hover{background:var(--wp--preset--color--accent-2)}& li.current-cat a{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'})
section('stagger', 'Stagger', ['core/post-template'], {
    'css': '@media (min-width:782px){& > li:nth-child(3n+2){margin-top:var(--wp--preset--spacing--70)!important}}'})
section('notice', 'Notice bar', ['core/group'], {
    'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|contrast'},
    'typography': {'fontSize': 'var:preset|font-size|small'},
    'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}}}})


CATS = [('whats-on', "What's on"), ('programme', 'Programme'), ('show', 'Show pages'), ('membership', 'Membership'), ('opportunities', 'Opportunities'),
        ('about', 'About and committee'), ('visit', 'Visit and access'), ('page', 'Page layouts')]
CATMAP = {
    'whats-on-hero': 'whats-on', 'whats-on-still': 'whats-on', 'whats-on-band': 'whats-on', 'coming-up': 'whats-on', 'coming-up-list': 'whats-on', 'notice-closed-for-install': 'whats-on',
    'event-row': 'whats-on', 'opening-night': 'whats-on', 'events-past': 'whats-on',
    'programme-grid': 'programme', 'programme-archive': 'programme', 'programme-filters': 'programme', 'programme-table': 'programme', 'post-list': 'programme',
    'exhibition-text': 'show', 'installation-views': 'show', 'show-credits': 'show', 'funders-line': 'show', 'installation-mosaic': 'show', 'artist-bio': 'show', 'room-sheet': 'show',
    'membership-card': 'membership', 'membership-band': 'membership', 'membership-how': 'membership', 'membership-faq': 'membership', 'donate': 'membership', 'members-quote': 'membership', 'mailing-list': 'membership',
    'opportunities-list': 'opportunities', 'opportunity-callout': 'opportunities', 'volunteer-call': 'opportunities', 'residency-info': 'opportunities', 'hire-the-space': 'opportunities',
    'studios-list': 'about', 'studio-holders': 'about', 'committee-list': 'about', 'past-committee': 'about', 'about-history': 'about', 'publications-list': 'about', 'writing-commission': 'about',
    'access-info': 'visit', 'find-us': 'visit',
}
_pattern = pattern


def pattern(slug, title, categories, body, **kw):
    return _pattern(slug, title, CATMAP.get(slug, 'page' if slug.endswith('-page') or kw.get('block_types') else categories), body, **kw)


write('functions.php', "<?php\n/**\n * Commons: registers the pattern categories used by the theme's patterns.\n *\n * @package commons\n */\n\nadd_action(\n\t'init',\n\tfunction () {\n"
      + ''.join("\t\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', 'commons' ) ) );\n" % (a, b.replace("'", "\\'")) for a, b in CATS) + "\t}\n);\n")

# ---------------------------------------------------------------- parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')),
        justify='space-between', align='wide'),
    tag='header', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}))
write('parts/notice.html', pattern_ref('notice-closed-for-install'))
write('parts/footer.html', group(J(
    columns(
        ('50%', J(heading('Mabgate Commons', 2, fontSize='xx-large'),
                  para('An artist-run space and 14 studios in a former dye works. Run by a volunteer committee since 2011, funded by members and the odd grant.'))),
        (None, J(heading('Visit', 6),
                 para('41 Mabgate, Leeds LS9 7DR<br>Thursday to Sunday, 12 to 6pm<br>Free, step-free on the ground floor', fontSize='small'),
                 para('<a href="/visit/">Access and directions</a>', fontSize='small'))),
        (None, J(heading('Keep up', 6),
                 para('<a href="mailto:post@example.com?subject=Mailing%20list">Mailing list, once a month</a><br><a href="https://www.instagram.com/">Instagram</a><br><a href="/membership/">Become a member, £25 a year</a>', fontSize='small'))),
        align='wide'),
    para('Supported by Leeds Inspired and our 212 members. Demo photographs are CC0 and public domain images from Wikimedia Commons, used as stand-ins.', align='wide', textColor='muted', fontSize='x-small')),
    tag='footer', align='full', className='is-style-sage', style={'border': {'radius': '0'}, 'spacing': {'padding': {'top': 'var:preset|spacing|70', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': 'var:preset|spacing|70'}}}))

# ---------------------------------------------------------------- patterns
IMG = {
    'hero': 'A narrow gallery corridor with a wooden partition wall, a photograph in a cut-out window and drawings on white cloth to the left',
    'show-1': 'Three woven fibre sculptures hanging on fine wires in front of a large brown panel',
    'show-3': 'Embroidered banners and printed textiles hung on a red wall, with the word radical repeated in white letters',
    'show-4': 'Black and white photograph of two men in suits looking at small clay figures on a plinth',
    'show-6': 'A timber-lined gallery with framed landscape paintings in a row and a low table in the middle',
    'show-7': 'A large flower arrangement on a twisting branch, set on a red cloth in front of tall windows',
    'event': 'A bronze torso on a white plinth beside a tall window, with a small carved stone figure in front',
    'residency': 'Black and white photograph of a painter sitting on the studio floor in front of a large canvas of pale figures',
    'studio': 'An artist in a dark coat in a studio, with a large unfinished canvas and a ladder behind her',
    'opening': 'Old photograph of a small gallery room with a vessel on a plinth and framed drawings on the wall',
    'publication': 'Ten painted tiles in a grid, each showing a figure and the name of a period in the history of ceramics',
    'zine': 'Engraving of a crowded print workshop, with people pulling prints and hanging sheets to dry',
}


def num(text):
    return para(text, className='is-style-running-number')


# Signature, front of house: what's on
def fcover(inner, dim=10, min_height=88, **attrs):
    """Cover that uses the post's featured image (no theme URL, so it stays valid in the editor)."""
    a = {'useFeaturedImage': True, 'dimRatio': dim, 'overlayColor': 'contrast', 'isUserOverlayColor': True, 'minHeight': min_height, 'minHeightUnit': 'vh', **attrs}
    return ('<!-- wp:cover%s -->\n<div class="wp-block-cover"><span aria-hidden="true" class="wp-block-cover__background has-contrast-background-color has-background-dim-%d has-background-dim"></span>'
            '<div class="wp-block-cover__inner-container">%s</div></div>\n<!-- /wp:cover -->') % (_a(a), dim, inner)


HOURS = para('Thursday to Sunday, 12 to 6pm. Free, no booking.', fontSize='x-small')
pattern('whats-on-hero', "What's on: newest show over a full-bleed photo", 'featured,query', query(
    fcover(group(J(
        dyn('post-terms', term='post_tag', className='is-style-running-number'),
        dyn('post-title', level=1, isLink=True, fontSize='xx-large'),
        dyn('post-excerpt', showMoreOnPage=False),
        HOURS,
        buttons(('Plan a visit', '/visit/'))),
        className='is-style-label-card', layout={'type': 'constrained', 'contentSize': '30rem', 'justifyContent': 'left'}),
        contentPosition='bottom left', align='full',
        style={'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}}),
    per_page=1, query_id=11, align='full'),
    description='The newest show in the programme, as a full-width installation photo with a label card: number, title, artists and dates, opening hours.')

pattern('whats-on-still', "What's on: photo with an overlapping label", 'featured', J(
    image('hero.jpg', IMG['hero'], lightbox=False, align='full', className='is-style-crop-wide'),
    group(J(
        para('No. 184', className='is-style-running-number'),
        heading('Soft borders', 2, fontSize='xx-large'),
        para('Hana Mirza and Ciarán Doyle. 12 September to 25 October 2026.'),
        HOURS,
        buttons(('Read about the show', '/soft-borders/'))),
        className='is-style-overlap-card', align='wide', layout={'type': 'constrained', 'contentSize': '30rem', 'justifyContent': 'left'})),
    description='A fixed version of the current show for any page: a wide photo with the label card overlapping its bottom edge.')

pattern('whats-on-band', "What's on: text band (no photo)", 'featured', group(columns(
    ('22%', J(num('No. 184'), para('Now on', fontSize='x-small'))),
    (None, J(heading('<a href="/soft-borders/">Soft borders</a>', 2, fontSize='x-large'), para('Hana Mirza and Ciarán Doyle. Textile, video and a lot of fishing line.'))),
    ('28%', para('12 September to 25 October 2026<br>Thursday to Sunday, 12 to 6pm<br>Free, no booking', fontSize='small')), align='wide'),
    className='is-style-label-card', align='wide'), description='A smaller version of the current show for inner pages.')

pattern('coming-up', 'Coming up (two shows, image led)', 'featured,query', group(J(
    row(J(heading('Coming up', 2), para('<a href="/programme/">The whole programme, numbered</a>', fontSize='small')), justify='space-between', align='wide'),
    columns(
        ('58%', J(image('publication.jpg', 'Ten painted tiles by members, each a figure from a different period of ceramics, hung in a grid', lightbox=False),
                  row(J(num('No. 185'), para('7 November to 20 December 2026', fontSize='x-small')), justify='space-between'),
                  heading('Weft, the members’ show', 3),
                  para('Open to every member, one work each, hung by lottery on the Friday before. Hand-in is 31 October, 11am to 3pm.'))),
        (None, J(spacer('var:preset|spacing|70'),
                 image('studio.jpg', IMG['studio'], lightbox=False),
                 row(J(num('No. 186'), para('January to March 2027', fontSize='x-small')), justify='space-between'),
                 heading('Winter residency: Oyelaran Bello', 3),
                 para('Twelve weeks in the back studio. Open studio every last Saturday, 2 to 5pm.'))),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70'}}}))

pattern('coming-up-list', 'Coming up (ruled list)', 'text', group(J(
    heading('Also on the calendar', 4),
    *[group(columns(('14%', num(n)), (None, heading(t, 5)), ('34%', para(d, fontSize='x-small'))), className='is-style-ruled')
      for n, t, d in [('E.61', 'Reading group: Lucy Lippard, Six Years', 'Tues 7 Oct, 7pm, free'),
                      ('E.62', 'Crit night for members', 'Thurs 23 Oct, 6.30pm'),
                      ('E.63', 'Risograph afternoon with Plumb Press', 'Sat 1 Nov, 1 to 5pm, £12'),
                      ('E.64', 'Committee AGM, open to all members', 'Weds 26 Nov, 7pm')]]),
    align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}), description='Events and talks as ruled rows with their own running numbers.')

GRID_ITEM = J(dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover'),
              row(J(dyn('post-terms', term='post_tag', className='is-style-running-number'), dyn('post-terms', term='category', separator=', ')), justify='space-between'),
              dyn('post-title', isLink=True, level=3, fontSize='large'),
              dyn('post-excerpt', showMoreOnPage=False, excerptLength=24))

pattern('programme-grid', 'Programme: recent shows (image grid)', 'featured,query', group(J(
    row(J(heading('From the programme', 2), para('<a href="/programme/">All 184 shows</a>', fontSize='small')), justify='space-between', align='wide'),
    query(GRID_ITEM, per_page=6, query_id=12, align='wide', template_class='is-style-stagger',
          layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '18rem'}).replace('"offset":0', '"offset":1', 1)),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|70'}}}), keywords='programme, archive, shows')

pattern('programme-archive', 'Programme archive (inherits the page query)', 'query', inherit_query(GRID_ITEM, align='wide',
        layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '18rem'}), inserter=False)

pattern('programme-filters', 'Programme filters: by type and by year', 'query', group(J(
    row(J(para('Type', fontSize='x-small', textColor='muted'), dyn('categories', className='is-style-pill-list'))),
    row(J(para('Year', fontSize='x-small', textColor='muted'), dyn('archives', type='yearly', className='is-style-pill-list')))),
    align='wide', layout={'type': 'flex', 'orientation': 'vertical'}), description='Category and year filters for the programme archive.')

pattern('programme-table', 'Programme index before 2019 (table)', 'text', group(J(
    heading('Before the website', 3),
    para('Shows 1 to 150 were listed on paper in the front window. Rhiannon typed them up from the committee minutes in 2023. If you showed here and your name is spelt wrong, tell us.'),
    table([['150', 'Lodestar', 'Priti Rao', '03/11/2018', 'Solo show'],
           ['149', 'Members’ show 2018', '61 members', '14/09/2018', 'Members’ show'],
           ['148', 'Ground water', 'Ewan McLeish, Nnedi Ike', '06/07/2018', 'Two-person show'],
           ['147', 'Bread and roses night', 'Mabgate choir', '01/05/2018', 'Event'],
           ['146', 'Soft furnishings', 'Agnieszka Kurek', '09/03/2018', 'Solo show'],
           ['12', 'Opening show', 'The first 9 studio holders', '17/06/2011', 'Group show']],
          head=['No.', 'Title', 'Artists', 'Opened', 'Type'])), align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}))

pattern('exhibition-text', 'Show page: text, installation views and credits', 'text', J(
    para('Hana Mirza weaves on a floor loom she built from a bed frame. Ciarán Doyle films rivers at the point where they stop being counted as rivers. For six weeks the two of them share the long room, with a curtain of monofilament down the middle that you can walk through.', fontSize='large'),
    para('The show started as a conversation at a members’ crit in 2024. Hana wanted to hang something that you could not see from the door. Ciarán wanted a screen you had to walk round. The curtain does both, badly and on purpose.'),
    pattern_ref('installation-views'),
    pattern_ref('show-credits')), description='Body copy for one show, with installation photos and a credits line.')

pattern('installation-views', 'Installation views (large, then two-up)', 'gallery', J(
    gallery([('show-1.jpg', IMG['show-1'], 'Hana Mirza, Bedframe weavings 1 to 3, 2026'),
             ('event.jpg', IMG['event'], 'The back room, with the plinth left over from show 183')], columns=2, align='wide')))

def ruled(pairs):
    return group(J(*[columns(('32%', para(a, fontSize='small', textColor='muted')), (None, para(b)), className='is-style-ruled', isStackedOnMobile=False) for a, b in pairs]), layout={'type': 'default'})


pattern('show-credits', 'Show credits and funders', 'text', J(
    ruled([('Artists', 'Hana Mirza, Ciarán Doyle'), ('Curated by', 'Rhiannon Price for the committee'), ('Install', 'Tomasz Wrona, Kofi Mensah-Hart and six members'),
           ('Photography', 'Aiko Tanabe'), ('Funded by', 'Leeds Inspired small grant (£1,800) and members\u2019 fees')]),
    para('Copy these lines into the grant report. They already have what funders ask for.', fontSize='x-small', textColor='muted')))

pattern('funders-line', 'Funders line', 'text', para('This show was made with a Leeds Inspired small grant, members’ fees and 40 hours of volunteer install time.', fontSize='small'))

pattern('notice-closed-for-install', 'Notice: closed for install', 'banner', group(
    para('Closed for install from 26 October. We reopen with the members’ show on Friday 7 November at 6pm. <a href="/programme/">See what’s next</a>'),
    className='is-style-notice', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
    description='Put this in the header part between shows, and take it out once the next one opens.')

pattern('membership-card', 'Membership card', 'call-to-action', group(J(
    row(J(para('£25', className='is-style-running-number', fontSize='xx-large'), para('a year, or £10 if you are a student or out of work', fontSize='small')), wrap=True),
    heading('Become a member', 3),
    lst(['A work in the members’ show every autumn, no selection panel',
         'First go at the winter residency and paid writing commissions (£150 each)',
         'Crit nights once a month, with tea',
         'A vote at the AGM and a turn on the committee if you want one']),
    buttons(('Join by bank transfer', '/membership/#join'))),
    className='is-style-label-card', layout={'type': 'constrained', 'justifyContent': 'left'}), description='A flat yearly fee and the concrete things members get.')

pattern('membership-band', 'Membership band with photo', 'call-to-action', media_text('zine.jpg', IMG['zine'], J(
    heading('212 members keep the doors open', 2, fontSize='x-large'),
    para('Membership pays the rent on the gallery floor. It costs £25 a year and anyone can join. You get a wall in the members’ show, a vote, and first go at the residency.'),
    buttons(('See what members get', '/membership/'))), width=55, align='wide', className='is-style-sage',
    style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}), description='Image and text band pointing to the membership page.')

pattern('membership-how', 'Membership: how to join', 'text', group(J(
    heading('How to join', 3, anchor='join'),
    lst(['Send £25 (or £10 concession) to Mabgate Commons, sort code 08-92-99, account 65871234. Use your surname as the reference.',
         'Email <a href="mailto:members@example.com">members@example.com</a> with your name and whether you make work, write, or just like coming to openings.',
         'Saoirse adds you to the list within a week and sends the members’ show call-out in September.'], ordered=True),
    para('Membership runs from 1 September. If you join after March we carry you over to the next year.', fontSize='small'))))

pattern('membership-faq', 'Membership questions', 'text', J(
    heading('Questions people ask', 3),
    details('Do I have to be an artist?', para('No. About a third of members come to openings and never show anything. They still get a vote.')),
    details('Is the members’ show selected?', para('No. Every member who hands in one work gets it hung. The lottery only decides where it goes.')),
    details('Can I pay by card?', para('Not yet. Bank transfer or cash at an opening. We are not paying card fees on £25.')),
    details('Can I get a refund?', para('We refund in the first 14 days. After that the money has gone on rent.'))))

pattern('membership-page', 'Page: membership', 'call-to-action', J(
    columns(('45%', pattern_ref('membership-card')), (None, J(image('show-3.jpg', IMG['show-3'], 'Members’ show 2025, the red wall. Photo: Aiko Tanabe'), pattern_ref('membership-how'))), align='wide'),
    pattern_ref('membership-faq'), pattern_ref('donate')), block_types='core/post-content')

pattern('opportunities-list', 'Opportunities with deadlines', 'text', group(J(
    *[group(columns(('18%', para(dl, fontSize='small')), (None, J(heading(t, 4), para(d))), ('16%', para(fee, fontSize='small'))),
            className='is-style-ruled')
      for dl, t, d, fee in [
          ('Deadline<br>12 Oct 2026', 'Winter residency 2027', 'Twelve weeks in the back studio, January to March. £1,200 fee, £300 materials, a key and the kettle. For artists living in Yorkshire.', 'Free to apply'),
          ('Deadline<br>31 Oct 2026', 'Members’ show hand-in', 'One work per member, any medium, up to 120 cm on the longest side. Bring it to the gallery between 11am and 3pm.', 'Members'),
          ('Deadline<br>15 Nov 2026', 'Writing commission', 'We pay two writers £150 each to write about a show in the 2027 programme. 800 to 1,200 words.', 'Free to apply'),
          ('Rolling', 'Studio waiting list', 'Studios are 9 to 22 square metres, £95 to £210 a month. About two come free a year.', 'Free')]]),
    align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}), description='Open calls as ruled rows with deadline, detail and fee.')

pattern('opportunity-callout', 'Open call callout', 'call-to-action', group(J(
    num('Deadline 12 Oct'),
    heading('The winter residency is open', 3),
    para('Twelve weeks, a paid fee of £1,200 and a key to the back studio. Send ten images, 300 words and a rough budget. We read every one as a committee.'),
    buttons(('Read the call and apply', '/opportunities/'))), className='is-style-label-card', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('opportunities-page', 'Page: opportunities', 'text', J(
    para('Every call we run is free to enter. We pay artists and writers at or above the a-n guidance rates, and we say what the fee is before you apply.', fontSize='large'),
    pattern_ref('opportunities-list'), pattern_ref('studios-list')), block_types='core/post-content')

pattern('studios-list', 'Studios and who is in them', 'about', group(J(
    heading('The studios', 3),
    columns((None, image('residency.jpg', IMG['residency'], 'Studio 9, Oyelaran Bello, 2025')),
            (None, J(para('Fourteen studios over two floors of the old dye works. Rent includes heat, light and wifi. There is a shared sink on each floor and a goods lift that works most days.'),
                     table([['Studio 1 to 6', 'Ground floor, 9 to 12 m²', '£95 to £120 a month'], ['Studio 7 to 12', 'First floor, 14 to 18 m²', '£140 to £175 a month'], ['Studio 13 and 14', 'First floor, 22 m², north light', '£210 a month']])))),
    ), align='wide', layout={'type': 'default'}))

pattern('committee-list', 'Committee with roles and terms', 'about', group(J(
    heading('The committee', 3),
    para('Six volunteers, each serving two years. Nobody stands for a third year in a row. That rule is why the programme keeps changing.'),
    grid(J(*[group(J(heading(n, 4), para(r), para(t, fontSize='small', textColor='muted')), className='is-style-sage') for n, r, t in [
        ('Ife Adeyemi', 'Chair', '2025 to 2027'), ('Tomasz Wrona', 'Treasurer and install', '2025 to 2027'), ('Rhiannon Price', 'Programme', '2024 to 2026'),
        ('Kofi Mensah-Hart', 'Access and building', '2025 to 2027'), ('Saoirse Duggan', 'Membership', '2024 to 2026'), ('Aiko Tanabe', 'Studios and photography', '2026 to 2028')]]),
         min_width='15rem')), align='wide', layout={'type': 'constrained', 'contentSize': '1000px'}))

pattern('past-committee', 'Everyone who served before', 'about', group(J(
    heading('Committee members since 2011', 4),
    para('Maeve Kilbride, Josh Oyelaran, Priti Rao, Ewan McLeish, Agnieszka Kurek, Dev Patel, Holly Marsden, Nnedi Ike, Jonny Bairstow, Farah Qureshi, Sam Ashworth, Lotte van Beek, Gethin Morgan, Rosa Delgado, Kwame Asante, Ellie Fenwick, Bilal Hussain', fontSize='large')),
    className='is-style-sage'))

pattern('about-history', 'About: how the space started', 'about', columns(
    ('45%', image('opening.jpg', IMG['opening'], 'The front room before the 2011 opening, as the landlord left it')),
    (None, J(heading('A dye works, then a gallery', 2, fontSize='x-large'),
             para('Nine artists took the lease on 41 Mabgate in 2011 because it was cheap and had a big room with no pillars. They painted it, called the first show No. 1, and kept counting.'),
             para('Fifteen years on there are 14 studios upstairs, a gallery downstairs and 184 shows behind us. We still have no director and no paid staff. Everything is done by a committee of six who change every two years.'),
             para('We would rather show one odd thing well than six safe things. That has cost us two grants and we would do it again.'))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('about-page', 'Page: about and committee', 'about', J(
    pattern_ref('about-history'), pattern_ref('committee-list'), pattern_ref('past-committee'), pattern_ref('publications-list')), block_types='core/post-content')

pattern('access-info', 'Access information', 'text', J(
    heading('Access', 3),
    lst(['The gallery is on the ground floor with a level entrance from Mabgate. The door is 94 cm wide.',
         'There is an accessible toilet on the ground floor with a grab rail and an alarm cord.',
         'The studios upstairs are up 22 stairs. The goods lift is not safe for people, sorry.',
         'Seats are in every show. Ask and we will bring one to wherever you want to sit.',
         'Large-print room sheets are by the door. Kofi can send them in advance by email.',
         'Quiet hour on Thursdays from 12 to 1pm, with the video sound off.']),
    para('Questions about access go to Kofi: <a href="mailto:access@example.com">access@example.com</a> or 0113 496 0582.')))

pattern('find-us', 'Find us and opening hours', 'contact', columns(
    (None, J(heading('Find us', 3), para('41 Mabgate, Leeds LS9 7DR. Ten minutes\u2019 walk from Leeds bus station, past the Hope Inn. The 19 and 19A stop at Mabgate Green.'),
             para('Bike racks outside. No car park, but there is on-street parking after 6pm.', fontSize='small'))),
    (None, J(heading('Opening hours', 3),
             ruled([('Thursday to Sunday', '12 to 6pm'), ('Monday to Wednesday', 'Closed, studios only'), ('Opening nights', 'Friday, 6 to 9pm'), ('Between shows', 'Closed for install')]))),
    align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}}))

pattern('visit-page', 'Page: visit', 'contact', J(
    image('show-6.jpg', IMG['show-6'], 'The long room, looking towards the back studio', align='wide', lightbox=False),
    pattern_ref('find-us'), pattern_ref('access-info')), block_types='core/post-content')

pattern('donate', 'Donate', 'call-to-action', group(J(
    heading('Give the space a hand', 3),
    para('£5 buys a bag of screws for install. £40 pays the electric for a week of video. £300 pays an artist’s fee for a one-night event. Anything helps.'),
    buttons(('Donate by bank transfer', 'mailto:treasurer@example.com?subject=Donation'), ('Leave something in the tin', '/visit/', {'className': 'is-style-outline'}))),
    className='is-style-sage', layout={'type': 'constrained', 'justifyContent': 'left'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|60'}}}))

pattern('publications-list', 'Publications', 'text', group(J(
    heading('Things we printed', 3),
    columns(('35%', image('zine.jpg', IMG['zine'], 'Cover of Commons Reader 3, which used an old engraving of a print shop')),
            (None, J(table([['<em>Commons Reader 3</em>', 'Six writing commissions, riso, 48 pp', '2025', '£8'],
                          ['<em>No. 1 to 150</em>', 'The first programme index, stapled', '2023', '£4'],
                          ['<em>Soft borders</em>', 'Room sheet and essay by Nell Achterberg', '2026', 'Free']], head=['Title', 'What', 'Year', 'Price']),
                     para('Buy them at the front desk, or email <a href="mailto:post@example.com">post@example.com</a> and we post them for £2.', fontSize='small'))))), align='wide', layout={'type': 'default'}))

pattern('mailing-list', 'Mailing list', 'call-to-action', group(J(
    heading('One email a month', 3),
    para('What’s on, what’s coming, and open calls a month before their deadline. Written by whoever is on the committee that month.'),
    buttons(('Join the mailing list', 'mailto:post@example.com?subject=Mailing%20list'))),
    className='is-style-soot', align='full', layout={'type': 'constrained'}, style={'spacing': {'margin': {'top': 'var:preset|spacing|70'}}}), keywords='newsletter, email')

pattern('members-quote', 'A member on the space', 'testimonials', pullquote(
    'I hung my first work here in 2019 and I have been on the committee twice since. It is the only room in Leeds where I have seen a choir and a welding demo in the same week.',
    'Farah Qureshi, member since 2019', align='wide'))

pattern('event-row', 'Events and talks (photo and text)', 'featured', media_text('zine.jpg', IMG['zine'], J(
    num('E.63'), heading('Risograph afternoon with Plumb Press', 3),
    para('Bring a drawing, leave with 30 copies in two colours. Paper and ink included. Twelve places, £12, or free for members on a low income.'),
    para('Saturday 1 November, 1 to 5pm', fontSize='x-small'),
    buttons(('Book a place by email', 'mailto:post@example.com?subject=Riso%20afternoon'))), right=True, width=45, align='wide'))

pattern('opening-night', 'Opening night', 'featured', media_text('event.jpg', IMG['event'], J(
    para('Friday 7 November, 6 to 9pm', fontSize='small'),
    heading('Opening: Weft, the members\u2019 show', 3),
    para('Sixty-odd works, one bar run by the committee, and a short speech from whoever loses the coin toss. Free, everyone welcome, children too until 8pm.'),
    buttons(('Add it to your calendar', '/programme/'))), width=50, align='wide', className='is-style-sage'))

pattern('events-past', 'Events that happened (list)', 'text', group(J(
    heading('Recent events', 4),
    *[group(columns(('14%', para(n, className='is-style-running-number')), (None, J(heading(t, 5), para(d, fontSize='small')))), className='is-style-ruled')
      for n, t, d in [('E.60', 'Artists\u2019 talk: Dele Okafor', 'Saturday 16 August 2026, 45 people'), ('E.59', 'Zine fair in the long room', 'Sunday 13 July 2026, 22 tables'),
                      ('E.58', 'Life drawing, summer term', 'Six Tuesdays, June and July 2026')]]), layout={'type': 'constrained'}))

pattern('installation-mosaic', 'Installation views, mosaic of five', 'gallery', group(J(
    columns(('62%', image('show-3.jpg', IMG['show-3'], 'Radical threads, the red wall')),
            (None, J(image('show-1.jpg', IMG['show-1'], 'The Prince\u2019s Seat'), image('show-7.jpg', IMG['show-7'], 'Flower piece for a long table'))), align='wide'),
    columns((None, image('show-6.jpg', IMG['show-6'], 'Late landscapes')), (None, image('event.jpg', IMG['event'], 'A figure by the window')), align='wide')),
    align='wide', layout={'type': 'default'}), description='Five installation views in two rows. Every image opens large.')

pattern('artist-bio', 'Artist in the show', 'text', columns(
    ('30%', image('residency.jpg', IMG['residency'])),
    (None, J(heading('Oyelaran Bello', 4),
             para('Oyelaran Bello (b. 1994, Lagos) paints large figure groups in black and white. He studied at Leeds Arts University and was our winter resident in 2026. He lives in Chapeltown.'),
             para('<a href="/winter-residency-oyelaran-bello/">His residency show, No. 180</a>', fontSize='small'))), verticalAlignment='center'))

pattern('room-sheet', 'Room sheet: list of works', 'text', group(J(
    heading('In the room', 4),
    lst(['Hana Mirza, <em>Bedframe weaving 1</em>, 2026. Wool and nylon on a bed frame loom.',
         'Hana Mirza, <em>Bedframe weaving 2</em>, 2026. Wool, jute and fishing line.',
         'Ciarán Doyle, <em>Where the Aire stops</em>, 2025. Video, 14 minutes, looped.',
         'Hana Mirza and Ciarán Doyle, <em>Curtain</em>, 2026. Monofilament, 9 m.'], ordered=True),
    para('Large-print copies are by the door.', fontSize='small')), className='is-style-sage'))

pattern('studio-holders', 'Studio holders', 'about', group(J(
    heading('Who is upstairs', 3),
    grid(J(*[stack(J(image(f, IMG[f[:-4]]), heading(n, 5), para(d, fontSize='small'))) for f, n, d in [
        ('residency.jpg', 'Oyelaran Bello, studio 9', 'Painting'), ('studio.jpg', 'Maeve Kilbride, studio 13', 'Painting and bronze'),
        ('zine.jpg', 'Plumb Press, studio 4', 'Risograph and letterpress'), ('publication.jpg', 'Agnieszka Kurek, studio 7', 'Ceramics and tiles')]]), min_width='13rem')),
    align='wide', layout={'type': 'default'}))

pattern('hire-the-space', 'Hire the long room', 'call-to-action', group(J(
    heading('Hire the long room', 3),
    para('The gallery is free to hire on Mondays to Wednesdays for crits, rehearsals, reading groups and small launches. £40 a day for members, £90 for everyone else. Up to 60 people standing.'),
    buttons(('Ask about a date', 'mailto:post@example.com?subject=Hire'))), className='is-style-label-card', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('volunteer-call', 'Volunteer with us', 'call-to-action', group(J(
    heading('Help us install', 4),
    para('We need six people for four days before each show: painting walls, filling holes, carrying plinths. Lunch is on us and you learn how to hang a show. No experience needed.'),
    para('<a href="mailto:post@example.com?subject=Install%20crew">Join the install list</a>')), className='is-style-ruled'))

pattern('residency-info', 'Winter residency', 'text', columns(
    (None, image('residency.jpg', IMG['residency'], 'Oyelaran Bello in the back studio, 2026')),
    (None, J(heading('The winter residency', 3),
             para('Twelve weeks in the back studio every January to March, with a £1,200 fee, £300 for materials and a show at the end. Open to artists living in Yorkshire, chosen by the committee from an open call.'),
             para('<a href="/opportunities/">This year\u2019s call closes 12 October</a>'))), align='wide', verticalAlignment='center'))

pattern('writing-commission', 'Commissioned writing (excerpt)', 'text', group(J(
    heading('On Soft borders', 4),
    para('\u201cYou hear the curtain before you see it: a dry sound, like rain on a tent. By the time you find the gap, you are already on the other side.\u201d', fontSize='large'),
    para('Nell Achterberg, from the room sheet essay, September 2026. Paid at £150 through our writing commissions.', fontSize='small', textColor='muted')),
    className='is-style-ruled'))

pattern('exhibition-page', 'Page: one exhibition', 'featured', J(
    pattern_ref('whats-on-still'), pattern_ref('exhibition-text'), pattern_ref('room-sheet'), pattern_ref('writing-commission'), pattern_ref('installation-mosaic'), pattern_ref('show-credits')),
    block_types='core/post-content')

pattern('studios-page', 'Page: studios', 'about', J(
    pattern_ref('studio-holders'), spacer('var:preset|spacing|60'), pattern_ref('studios-list'), pattern_ref('hire-the-space'), pattern_ref('volunteer-call')), block_types='core/post-content')

pattern('page-home-extra', 'Page: whole front page (for a page, not the template)', 'featured', J(
    pattern_ref('whats-on-hero'), pattern_ref('coming-up'), pattern_ref('programme-grid'), pattern_ref('membership-band'), pattern_ref('mailing-list')),
    block_types='core/post-content')

pattern('post-list', 'Search results list', 'query', inherit_query(
    group(columns(('20%', dyn('post-featured-image', isLink=True, aspectRatio='4/3', scale='cover')), (None, J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30)))),
          className='is-style-ruled'), align='wide'), inserter=False)

# ---------------------------------------------------------------- templates
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}}

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('whats-on-hero'), pattern_ref('coming-up'), pattern_ref('programme-grid'), pattern_ref('membership-band'), pattern_ref('coming-up-list')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|60'}}), pattern_ref('mailing-list'),
    template_part('footer', 'footer')))

write('templates/home.html', page_template(J(
    heading('Programme', 1, align='wide'),
    para('Every show, event and residency since 2011, newest first. The number goes up by one each time, whatever the show is.', align='wide', fontSize='large'),
    pattern_ref('programme-filters'), spacer('var:preset|spacing|40'),
    pattern_ref('programme-archive'), spacer('var:preset|spacing|60'), pattern_ref('programme-table')),
    layout={'type': 'constrained'}, style=MAINPAD))
write('templates/index.html', open(os.path.join(D, 'templates/home.html')).read())

write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', level=1),
    dyn('term-description', align='wide'),
    pattern_ref('programme-filters'), spacer('var:preset|spacing|40'),
    pattern_ref('programme-archive')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide', level=1),
    dyn('search', label='Search', showLabel=False, buttonText='Search', align='wide'),
    pattern_ref('post-list')), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/404.html', page_template(J(
    heading('Nothing on this wall', 1, align='wide'),
    para('That page has been taken down or never went up. Try the programme, or search for an artist.', fontSize='large'),
    dyn('search', label='Search', showLabel=False, buttonText='Search'),
    buttons(('Go to the programme', '/programme/'))), layout={'type': 'constrained'}, style=MAINPAD))

write('templates/single.html', J(template_part('header', 'header'), group(J(
    dyn('post-featured-image', align='full', aspectRatio='16/9', scale='cover', style={'border': {'radius': '0'}}),
    columns(
        ('34%', J(dyn('post-terms', term='post_tag', className='is-style-running-number'),
                  dyn('post-title', level=1, fontSize='xx-large'),
                  dyn('post-excerpt', showMoreOnPage=False),
                  dyn('post-terms', term='category', prefix='Filed under '),
                  para('<a href="/visit/">Opening hours and access</a>', fontSize='small'))),
        (None, dyn('post-content', layout={'type': 'constrained', 'contentSize': '680px', 'justifyContent': 'left'})),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}, 'margin': {'top': 'var:preset|spacing|50'}}}),
    group(J(dyn('post-navigation-link', type='previous', label='Previous show', showTitle=True),
            dyn('post-navigation-link', label='Next show', showTitle=True)),
          align='wide', className='is-style-ruled', layout={'type': 'flex', 'justifyContent': 'space-between'})),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'padding': {'bottom': 'var:preset|spacing|60'}}}),
    template_part('footer', 'footer')))

write('templates/page.html', page_template(J(
    dyn('post-title', level=1, align='wide'),
    dyn('post-featured-image', align='wide', aspectRatio='21/9', scale='cover'),
    dyn('post-content', layout={'type': 'constrained'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-wide.html', page_template(J(
    dyn('post-title', level=1),
    spacer('var:preset|spacing|40'),
    dyn('post-content', layout={'type': 'constrained', 'contentSize': '1000px'})), layout={'type': 'constrained', 'contentSize': '1000px'}, style=MAINPAD))
write('templates/page-plain.html', page_template(dyn('post-content', layout={'type': 'constrained'}), layout={'type': 'constrained'}))

print('commons built')
