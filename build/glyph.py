# glyph: independent type foundry (idea 024)
# Direction: "specimen sheet". White paper, black type, and proof-mark red used only for the notes a printer would
#   write in the margin (sizes, features, prices). The site is mostly the typefaces themselves, set very large.
# Fonts: Ronzino (Collletttivo, OFL; registry face) for UI, headings and the grotesk specimen, and Petrona as the
#   foundry's serif with a nine-weight waterfall. In the demo they stand in for the foundry's own files.
# Palette: paper #FFFFFF, type black #0D0D0D, proof red #CC2A17, galley #F1F0EC, rule #D5D3CC.
# Layout idea: each typeface page runs specimen, styles as ruled rows with the price at the right, a glyph grid of
#   single characters in square cells, a weight waterfall and the licence table, in that order, on a strict grid.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
from blocks import _a
import blocks as _b
set_theme('glyph')
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
    ('base', '#FFFFFF', 'Paper'),
    ('contrast', '#0D0D0D', 'Type black'),
    ('accent', '#CC2A17', 'Proof red'),
    ('surface', '#F1F0EC', 'Galley'),
    ('line', '#D5D3CC', 'Rule'),
    ('muted', '#5A5A55', 'Grey'),
]
fonts = json.load(open(os.path.join(D, '.fonts.json')))
fams = fonts['fontFamilies']


def pal(rows):
    return [{'slug': s, 'color': c, 'name': n} for s, c, n in rows]


def fs(slug, size, name, mn=None):
    d = {'slug': slug, 'size': size, 'name': name}
    d['fluid'] = {'min': mn, 'max': size} if mn else False
    return d


CSS = (':where(h1,h2,h3,h4){text-wrap:balance}:where(p){text-wrap:pretty}body{font-synthesis:none;font-kerning:normal}'
       '.wp-block-table{font-variant-numeric:tabular-nums lining-nums}'
       '.wp-block-table td,.wp-block-table th{border:0;border-bottom:1px solid var(--wp--preset--color--line);padding:.7em .8em .7em 0;text-align:left;vertical-align:baseline}'
       '.wp-block-table td:last-child,.wp-block-table th:last-child{text-align:right;padding-right:0}'
       '.wp-block-table thead{border:0;border-bottom:1px solid var(--wp--preset--color--contrast)}.wp-block-table th{font-weight:500;font-size:var(--wp--preset--font-size--x-small);color:var(--wp--preset--color--muted)}'
       '.wp-block-navigation__responsive-container.is-menu-open{background:var(--wp--preset--color--base)}'
       '.wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-size:var(--wp--preset--font-size--x-large)}'
       '.wp-block-navigation .current-menu-item>a{color:var(--wp--preset--color--accent)}'
       ':focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}'
       '.wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:0}'
       '.wc-block-components-product-price,.woocommerce-Price-amount{font-variant-numeric:tabular-nums}'
       '.wc-block-components-button:not(.is-link),.wp-block-button__link.add_to_cart_button,.single_add_to_cart_button{background:var(--wp--preset--color--contrast)!important;color:var(--wp--preset--color--base)!important;border-radius:0!important}'
       '.wc-block-components-product-sale-badge{border-radius:0;background:var(--wp--preset--color--accent);color:var(--wp--preset--color--base);border:0}')

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '680px', 'wideSize': '1440px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': pal(PAL)},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'writingMode': False,
            'fontFamilies': fams,
            'fontSizes': [
                fs('x-small', '0.875rem', 'Label'),
                fs('small', '1rem', 'Small'),
                fs('medium', '1.125rem', 'Body'),
                fs('large', '1.5rem', 'Large', '1.25rem'),
                fs('x-large', '2.25rem', 'Section', '1.75rem'),
                fs('xx-large', '4.5rem', 'Title', '2.75rem'),
                fs('display', '8rem', 'Display', '3.5rem'),
                fs('specimen', '15rem', 'Specimen', '5rem'),
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
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'},
                {'slug': '60', 'size': 'clamp(2.25rem, 5vw, 3.5rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'},
                {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True},
        'blocks': {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.5', 'fontWeight': '400'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|accent'}},
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'lineHeight': '1', 'letterSpacing': '-0.02em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|xx-large'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|large', 'letterSpacing': '-0.01em'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '500', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500', 'lineHeight': '1.4', 'letterSpacing': '0'}, 'color': {'text': 'var:preset|color|accent'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                'border': {'radius': '0', 'width': '1px', 'style': 'solid', 'color': 'var:preset|color|contrast'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.6em', 'bottom': '0.6em', 'left': '1em', 'right': '1em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}, 'border': {'color': 'var:preset|color|accent'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}},
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.45'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '700', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '400'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'elements': {'link': {'color': {'text': 'var:preset|color|accent'}, 'typography': {'textDecoration': 'none'}}}},
            'core/image': {'border': {'radius': '0'}},
            'core/post-featured-image': {'border': {'radius': '0'}},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|accent', 'fontSize': 'var:preset|font-size|large', 'fontStyle': 'italic', 'lineHeight': '1.3'},
                           'border': {'width': '0', 'style': 'none'}, 'spacing': {'padding': {'left': '0'}}},
            'core/pullquote': {'typography': {'fontFamily': 'var:preset|font-family|accent', 'fontSize': 'var:preset|font-size|x-large', 'fontStyle': 'italic', 'lineHeight': '1.15'},
                               'border': {'width': '0', 'style': 'none'}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}},
            'core/search': {'border': {'radius': '0'}},
        },
        'css': CSS,
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
        {'name': 'page-typeface', 'title': 'Typeface (no title, full width)', 'postTypes': ['page']},
    ],
}
write('theme.json', json.dumps(theme, indent='\t', ensure_ascii=False))

write('style.css', '''/*
Theme Name: Glyph
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A specimen site and licence shop for small independent type foundries, built from large type, glyph grids, weight waterfalls and a plain licence table.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: glyph
Tags: portfolio, e-commerce, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, grid-layout
*/''')


def variation(fname, title, rows):
    write('styles/%s.json' % fname, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
                                                'settings': {'color': {'palette': pal(rows)}}}, indent='\t', ensure_ascii=False))


variation('proof', 'Proof', [('base', '#F4F1E8', 'Paper'), ('contrast', '#141210', 'Type black'), ('accent', '#C2291A', 'Proof red'),
                             ('surface', '#EAE5D8', 'Galley'), ('line', '#D2CBBB', 'Rule'), ('muted', '#58544C', 'Grey')])
variation('inverse', 'Inverse', [('base', '#0D0D0D', 'Paper'), ('contrast', '#FFFFFF', 'Type black'), ('accent', '#FF6A55', 'Proof red'),
                                 ('surface', '#1C1C1C', 'Galley'), ('line', '#3A3A3A', 'Rule'), ('muted', '#B4B4AE', 'Grey')])
variation('galley', 'Galley', [('base', '#E9EEF2', 'Paper'), ('contrast', '#10345C', 'Type black'), ('accent', '#B8321F', 'Proof red'),
                               ('surface', '#DAE2E9', 'Galley'), ('line', '#B6C4D1', 'Rule'), ('muted', '#3F5670', 'Grey')])


def section(slug, title, block_types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug,
                                                        'blockTypes': block_types, 'styles': styles}, indent='\t', ensure_ascii=False))


section('glyph-cell', 'Glyph cell', ['core/paragraph'], {
    'typography': {'lineHeight': '1'},
    'css': '&{aspect-ratio:1;display:flex;align-items:center;justify-content:center;text-align:center;border:1px solid var(--wp--preset--color--line);margin:0!important}&:hover{background:var(--wp--preset--color--contrast);color:var(--wp--preset--color--base)}'})
section('glyph-grid', 'Glyph grid', ['core/group'], {
    'css': '&{gap:0!important}& > p{margin:-1px 0 0 -1px!important}@media (max-width:600px){&{grid-template-columns:repeat(4,1fr)!important}}'})
section('specimen', 'Specimen line', ['core/paragraph', 'core/heading'], {
    'typography': {'lineHeight': '0.9', 'letterSpacing': '-0.03em'},
    'css': '&{overflow-wrap:anywhere}& a{text-decoration:none;color:inherit}& a:hover{color:var(--wp--preset--color--accent)}'})
section('proof-note', 'Proof note', ['core/paragraph'], {
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'lineHeight': '1.3'},
    'color': {'text': 'var:preset|color|accent'}})
section('rule-top', 'Rule above', ['core/group', 'core/columns'], {
    'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('style-row', 'Style row', ['core/group'], {
    'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}})
section('galley', 'Galley panel', ['core/group', 'core/columns'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}}})
section('ink', 'Black panel', ['core/group'], {
    'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
    'elements': {'link': {'color': {'text': 'var:preset|color|base'}}, 'heading': {'color': {'text': 'var:preset|color|base'}},
                 'button': {'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'}, 'border': {'color': 'var:preset|color|base'}}},
    'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}}})


CATS = [('specimen', 'Specimen'), ('typefaces', 'Typefaces'), ('licensing', 'Licensing and shop'), ('trials', 'Trials and free fonts'), ('in-use', 'In use'), ('about', 'Foundry'), ('page', 'Page layouts')]
CATMAP = {'specimen-hero': 'specimen', 'specimen-sizes': 'specimen', 'styles-list': 'specimen', 'glyph-grid': 'specimen', 'glyph-grid-serif': 'specimen', 'weight-waterfall': 'specimen',
          'weight-waterfall-grotesk': 'specimen', 'opentype-features': 'specimen', 'language-support': 'specimen', 'details': 'typefaces', 'pairing': 'specimen',
          'specimen-paragraphs': 'specimen', 'specimen-inverse': 'specimen', 'alternates': 'specimen', 'figures-currency': 'specimen', 'punctuation-grid': 'specimen', 'specimen-poster': 'specimen',
          'typefaces-list': 'typefaces', 'typeface-cards': 'typefaces', 'family-overview': 'typefaces', 'release-notes': 'typefaces', 'front-intro': 'typefaces', 'foundry-news': 'typefaces',
          'licence-table': 'licensing', 'company-size': 'licensing', 'licensing-faq': 'licensing', 'education-licence': 'licensing',
          'trials': 'trials', 'trials-terms': 'trials', 'free-font-donate': 'trials',
          'in-use': 'in-use', 'in-use-grid': 'in-use', 'in-use-archive': 'in-use', 'in-use-feature': 'in-use', 'post-list': 'in-use',
          'custom-type': 'about', 'about-foundry': 'about', 'help-contact': 'about', 'designer-profile': 'about'}
_pattern = pattern


def pattern(slug, title, categories, body, **kw):
    return _pattern(slug, title, CATMAP.get(slug, 'page' if kw.get('block_types') else categories), body, **kw)


write('functions.php', "<?php\n/**\n * Glyph: registers the pattern categories used by the theme's patterns.\n *\n * @package glyph\n */\n\nadd_action(\n\t'init',\n\tfunction () {\n"
      + ''.join("\t\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', 'glyph' ) ) );\n" % c for c in CATS) + "\t}\n);\n")


def ruled(pairs):
    return group(J(*[columns(('32%', para(a, fontSize='small', textColor='muted')), (None, para(b)), className='is-style-style-row', isStackedOnMobile=False) for a, b in pairs]), layout={'type': 'default'})


# ---------------------------------------------------------------- parts
write('parts/header.html', group(
    row(J(dyn('site-title', level=0), dyn('navigation', layout={'type': 'flex', 'justifyContent': 'right'}, overlayMenu='mobile')), justify='space-between', align='wide'),
    tag='header', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}}}))

write('parts/footer.html', group(J(
    columns(
        ('50%', J(para('Sawtooth Type', fontSize='xx-large', className='is-style-specimen', style={'typography': {'fontWeight': '700'}}),
                  para('Two typefaces, drawn slowly in Margate by Ines Moretti and Kwabena Owusu. Trials are free. Licences are sold by use and company size.', fontSize='small'))),
        (None, J(heading('Ask', 6),
                 para('<a href="mailto:type@example.com">type@example.com</a><br>Licensing questions answered within two working days.', fontSize='small'))),
        (None, J(heading('Studio', 6),
                 para('Unit 7, Tracey Emin Studios<br>Union Crescent, Margate CT9 1NR<br>Visits by appointment', fontSize='small'))),
        align='wide'),
    para('The demo sets Margo Grotesk in Ronzino by Collletttivo and Harbour Serif in Petrona by Ringo R. Seeber, both under the SIL Open Font License, as stand-ins for a foundry’s own files. In-use photos are CC0 stand-ins from Wikimedia Commons.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-rule-top', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|50'}, 'margin': {'top': 'var:preset|spacing|70'}}}))

# ---------------------------------------------------------------- patterns
IMG = {
    'enamel': 'A round yellow enamel road sign in bold black condensed capitals, with distances to Gainsborough and Retford',
    'shopfront': 'A stone shop front with the name Wards the Florist in raised gilt serif letters above the windows',
    'type': 'Close-up of metal letterpress type sorts sitting in a wooden type case',
    'wood-type': 'Loose wooden type blocks piled together, some letters facing up',
    'print': 'The drum of an old printing press with a printed newspaper sheet wrapped around it',
    'books': 'Two old dark blue cloth book covers with gilt lettering and ornament on the spine',
    'menu': 'A printed hotel menu cover from 1900 with a serif title, an engraving of the building and condensed capitals',
}
NOTE = lambda t: para(t, className='is-style-proof-note')
GROT = {}  # Ronzino via display family
SERIF = {'fontFamily': 'accent'}


def spec(text, size='display', family=None, weight=None, italic=False, level=None, **kw):
    st = {}
    if weight:
        st.setdefault('typography', {})['fontWeight'] = str(weight)
    if italic:
        st.setdefault('typography', {})['fontStyle'] = 'italic'
    a = dict(className='is-style-specimen', fontSize=size, **kw)
    if family:
        a['fontFamily'] = family
    if st:
        a['style'] = st
    if level:
        return heading(text, level, **a)
    return para(text, **a)


# Signature: typeface page, specimen first
pattern('specimen-hero', 'Specimen: the family name, very large', 'featured', group(J(
    row(J(NOTE('Margo Grotesk, Bold, 240 pt'), NOTE('6 styles, 3 weights, 612 glyphs')), justify='space-between', align='wide'),
    spec('Margo', size='specimen', weight=700),
    spec('Grotesk, a working sans for signs and small print', size='xx-large', weight=500),
    row(J(buttons(('Buy a licence', '/shop/'), ('Download free trials', '/trials/', {'className': 'is-style-outline'})), NOTE('From £60 for one desktop user')), justify='space-between', align='wide')),
    align='wide', layout={'type': 'default'}), description='Opens a typeface page: the name set as large as the screen allows, with proof notes above.')

pattern('specimen-sizes', 'Specimen: one text at four sizes', 'featured', group(J(
    group(J(NOTE('96 pt'), spec('Harbour lights at 4am', size='display', weight=500)), className='is-style-rule-top', layout={'type': 'default'}),
    group(J(NOTE('48 pt'), spec('Tide tables, ferry times and the price of whelks on Tuesday', size='xx-large', weight=400)), className='is-style-rule-top', layout={'type': 'default'}),
    group(J(NOTE('24 pt'), para('Margo started as lettering for a fish market sign in 2019. The capitals are narrow so a long word fits on a short board. The lowercase is wider than you expect, so it still reads at 9 pt on a receipt.', fontSize='large')), className='is-style-rule-top', layout={'type': 'default'}),
    group(J(NOTE('16 pt'), para('Sixteen point is where most people will meet it: on menus, timetables and the back of a jar. We spaced the figures for tables first and adjusted the letters around them. Every weight has tabular and proportional numbers, small caps, and a single-storey a in stylistic set 1.')), className='is-style-rule-top', layout={'type': 'default'})),
    align='wide', layout={'type': 'default'}), description='A static stand-in for a type tester: the same voice at 96, 48, 24 and 16 point.')

STYLES = [('Regular', 400, False, '£60'), ('Oblique', 400, True, '£60'), ('Medium', 500, False, '£60'), ('Medium Oblique', 500, True, '£60'), ('Bold', 700, False, '£60'), ('Bold Oblique', 700, True, '£60')]

pattern('styles-list', 'Styles as ruled rows with prices', 'shop', group(J(
    row(J(heading('Styles', 2), NOTE('Prices for one desktop user. Whole family £280.')), justify='space-between', align='wide'),
    *[group(row(J(spec('Margo %s' % n, size='x-large', weight=w, italic=it), para(p, fontSize='small')), justify='space-between', wrap=False), className='is-style-style-row', align='wide', layout={'type': 'default'})
      for n, w, it, p in STYLES]),
    align='wide', layout={'type': 'default'}), description='Each style set in itself, with its single-style price at the right.')

GLYPHS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + list('abcdefghijklmnopqrstuvwxyz') + list('0123456789') + ['&amp;', '?', '!', '@', '£', '€', 'ß', 'æ', 'ø', 'ł', 'ğ', 'ñ']


def glyph_grid(chars, family=None, size='xx-large', cols='7.5rem'):
    cells = [para(c, className='is-style-glyph-cell', fontSize=size, **({'fontFamily': family} if family else {})) for c in chars]
    return group(J(*cells), className='is-style-glyph-grid', align='wide', layout={'type': 'grid', 'minimumColumnWidth': cols})


pattern('glyph-grid', 'Glyph grid (single characters)', 'featured', group(J(
    row(J(heading('Glyph set', 2), NOTE('Latin Extended A, 612 glyphs. Showing the basics.')), justify='space-between', align='wide'),
    glyph_grid(GLYPHS)), align='wide', layout={'type': 'default'}),
    description='A grid of large single characters in square cells. Add or remove cells to suit the family.')

pattern('glyph-grid-serif', 'Glyph grid, serif (figures and accents)', 'featured', group(J(
    row(J(heading('Figures and accents', 2), NOTE('Harbour Serif Regular. Oldstyle figures by default.')), justify='space-between', align='wide'),
    glyph_grid(list('0123456789') + ['Á', 'Ç', 'Ě', 'Ğ', 'Ł', 'Ñ', 'Ø', 'Ş', 'Ů', 'Ž', 'á', 'ç', 'ě', 'ğ', 'ł', 'ñ', 'ø', 'ş'], family='accent', cols='8rem')), align='wide', layout={'type': 'default'}))

pattern('weight-waterfall', 'Weight waterfall (nine weights)', 'featured', group(J(
    row(J(heading('Nine weights', 2), NOTE('Harbour Serif, 100 to 900, variable')), justify='space-between', align='wide'),
    *[group(row(J(NOTE(str(w)), spec('Harbour %s' % n, size='xx-large', family='accent', weight=w)), wrap=False, style={'spacing': {'blockGap': 'var:preset|spacing|40'}}),
            className='is-style-style-row', align='wide', layout={'type': 'default'})
      for w, n in [(100, 'Thin'), (200, 'Extra Light'), (300, 'Light'), (400, 'Regular'), (500, 'Medium'), (600, 'Semibold'), (700, 'Bold'), (800, 'Extra Bold'), (900, 'Black')]]),
    align='wide', layout={'type': 'default'}), description='The same line in every weight, from Thin to Black.')

pattern('weight-waterfall-grotesk', 'Weight waterfall (grotesk, three weights and obliques)', 'featured', group(J(
    row(J(heading('Weights', 2), NOTE('Regular 400, Oblique, Medium 500, Bold 700, Bold Oblique')), justify='space-between', align='wide'),
    *[spec('Hamburgefonstiv', size='display', weight=w, italic=it) for w, it in [(400, False), (400, True), (500, False), (700, False), (700, True)]]),
    align='wide', layout={'type': 'default'}))

LICENCES = [['Desktop', 'Install on computers to make print, images and logos. Counted per user.', '£60 a style<br>£280 family'],
            ['Web', 'Self-host WOFF2 files on one domain. Counted by monthly page views.', 'From £60 for 50,000 views'],
            ['App and game', 'Embed in one app or game. Counted per title.', 'From £320'],
            ['Video and social', 'Titles and captions in video, posts and ads. Per company.', '£120 a year'],
            ['Logo', 'Use the letters as the basis of a logo or wordmark. One mark.', '£450, includes desktop']]

pattern('licence-table', 'Licensing table', 'shop', group(J(
    heading('Licences', 2),
    table(LICENCES, head=['Licence', 'What it covers', 'Price']),
    NOTE('Prices are for companies with up to 10 people. 11 to 50 people pay double. Students and charities pay half. Email us.')),
    align='wide', layout={'type': 'constrained', 'contentSize': '1100px'}), description='A plain table of licence types with what each covers and what it costs.')

pattern('company-size', 'Company-size pricing', 'shop', table(
    [['1 to 10 people', 'Listed price'], ['11 to 50 people', '2 × listed price'], ['51 to 250 people', '4 × listed price'], ['Over 250', 'Email us'], ['Students, charities, co-ops', 'Half the listed price']],
    head=['Company size', 'Desktop and web price']))

pattern('licensing-faq', 'Licensing questions', 'text', J(
    heading('Questions', 3),
    details('Can a freelancer use a client’s licence?', para('No. The licence belongs to whoever pays for it. If you are designing for a client, the client should buy it, or you buy it and transfer it to them. Transfers are free.')),
    details('Do I need a web licence for images of text?', para('No. A JPEG or PNG of the type is covered by the desktop licence. You need a web licence when the font file is served to browsers.')),
    details('Can I edit the fonts?', para('You may edit them for your own use, for example to draw a custom ligature for a logo. You may not sell or share the edited files.')),
    details('What if I go over my page views?', para('Upgrade when you notice. We do not audit anyone and we do not charge back-dated fees.'))))

pattern('licensing-page', 'Page: licensing', 'shop', J(
    pattern_ref('licence-table'), spacer('var:preset|spacing|60'),
    columns((None, J(heading('By company size', 3), pattern_ref('company-size'), pattern_ref('education-licence'))), (None, pattern_ref('licensing-faq')), align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    block_types='core/post-content')

pattern('details', 'Typeface details (designer, version, formats)', 'text', group(J(
    heading('Details', 3),
    ruled([('Designers', 'Ines Moretti, with Kwabena Owusu (figures and spacing)'), ('Released', 'March 2024'), ('Version', '1.3, updated 2 September 2026'), ('Formats', 'OTF, TTF, WOFF2, variable TTF'),
           ('Styles', '6 (3 weights with obliques)'), ('Languages', '218 Latin-script languages, including Polish, Turkish, Vietnamese and Welsh'),
           ('Features', 'Small caps, tabular and oldstyle figures, fractions, case-sensitive forms, ss01 single-storey a')])),
    className='is-style-rule-top', align='wide', layout={'type': 'constrained', 'contentSize': '1100px'}))

pattern('opentype-features', 'OpenType features demo', 'text', group(J(
    heading('Features', 2),
    columns(
        (None, J(NOTE('Default'), spec('Glasgow at 10:45', size='x-large', weight=500))),
        (None, J(NOTE('ss01, single-storey a'), spec('Glɑsgow ɑt 10:45', size='x-large', weight=500))),
        (None, J(NOTE('Tabular figures'), spec('10:45 11:10 12:05', size='x-large', weight=500)))),
    NOTE('Stylistic sets are switched on in your design app or with font-feature-settings in CSS.')),
    align='wide', layout={'type': 'default'}))

pattern('language-support', 'Language support', 'text', group(J(
    heading('Languages', 3),
    para('Afrikaans, Albanian, Basque, Bosnian, Breton, Catalan, Croatian, Czech, Danish, Dutch, English, Estonian, Faroese, Finnish, French, Frisian, Galician, German, Hungarian, Icelandic, Irish, Italian, Latvian, Lithuanian, Luxembourgish, Maltese, Norwegian, Polish, Portuguese, Romanian, Scottish Gaelic, Slovak, Slovenian, Spanish, Swahili, Swedish, Turkish, Vietnamese, Welsh, Yoruba and 178 more.', fontSize='large')),
    className='is-style-rule-top', align='wide', layout={'type': 'constrained', 'contentSize': '1100px'}))

pattern('in-use', 'In use (photographs)', 'gallery', group(J(
    row(J(heading('In use', 2), para('<a href="/in-use/">More in use</a>')), justify='space-between', align='wide'),
    columns((None, image('shopfront.jpg', IMG['shopfront'], 'Signage for a florist in York, 2025')),
            (None, image('enamel.jpg', IMG['enamel'], 'Replacement village signs, Nottinghamshire County Council, 2024')),
            (None, image('menu.jpg', IMG['menu'], 'Menus for a hotel restaurant in Folkestone, 2025')), align='wide')),
    align='wide', layout={'type': 'default'}), description='Real projects that use the typeface, uncropped, with who and when.')

pattern('pairing', 'Pairing suggestion', 'text', columns(
    (None, J(NOTE('Headings: Margo Bold'), spec('Low tide walks, every Sunday', size='x-large', weight=700))),
    (None, J(NOTE('Text: Harbour Serif Regular'), para('Meet at the Harbour Arm at 9am. Bring boots. We walk out to the chalk reef and back before the water turns, about two hours.', fontFamily='accent', fontSize='large'))),
    align='wide', className='is-style-galley'))

pattern('trials', 'Trial fonts', 'call-to-action', group(J(
    heading('Free trial fonts', 2),
    para('Full character sets, every style, for testing and pitching. Trials cannot be used in anything published. Email us the families you want and we send a download link, usually the same day.'),
    buttons(('Ask for trial fonts', 'mailto:type@example.com?subject=Trial%20fonts')),
    NOTE('Trial files last updated 2 September 2026, version 1.3.')), className='is-style-galley', layout={'type': 'constrained', 'justifyContent': 'left'}))

pattern('trials-page', 'Page: trials', 'call-to-action', J(pattern_ref('trials'), spacer('var:preset|spacing|50'), pattern_ref('trials-terms')), block_types='core/post-content')

pattern('trials-terms', 'Trial terms', 'text', group(J(
    heading('What you can do with trials', 3),
    lst(['Test the fonts in layouts, mock-ups and pitches.', 'Show pitches to clients.', 'Keep them for as long as you are testing.']),
    heading('What you cannot do', 3),
    lst(['Publish, print or broadcast anything set in a trial font.', 'Share the files outside your team.'])), layout={'type': 'constrained'}))

pattern('free-font-donate', 'Free font with a donation', 'call-to-action', group(J(
    spec('Tern Stencil', size='display', weight=700),
    para('A small free typeface we drew for our own price tags, released under the SIL Open Font License. Use it for anything.'),
    buttons(('Download Tern Stencil', 'https://github.com/'), ('Buy us a coffee, £3', 'mailto:type@example.com?subject=Donation', {'className': 'is-style-outline'}))),
    className='is-style-ink', align='full', layout={'type': 'constrained'}), description='For free OFL releases: a download button and an optional donation.')

pattern('custom-type', 'Custom type', 'services', columns(
    ('45%', image('wood-type.jpg', IMG['wood-type'])),
    (None, J(heading('Custom type', 2),
             para('We draw custom typefaces and adapt ours for brands, signage and publications. Recent work: a condensed Margo for Margate Harbour Arm signage, and Welsh and Scottish Gaelic support for a museum.'),
             para('Projects start at £6,000 and take 8 to 16 weeks. We take two a year.'),
             buttons(('Email about custom work', 'mailto:type@example.com?subject=Custom%20type')))),
    align='wide'))

pattern('about-foundry', 'About the foundry', 'about', columns(
    (None, J(heading('Two people, two typefaces', 2),
             para('Ines Moretti trained as a sign painter in Bologna and drew lettering for Margate market stalls before she drew a font. Kwabena Owusu came from software and does the spacing, the kerning and the files.'),
             para('We release slowly. Margo took four years. Harbour took three. We would rather have two families that work than twelve that nearly do.'))),
    (None, image('type.jpg', IMG['type'], 'The type case we started with, bought at a house clearance in Ramsgate')),
    align='wide'))

pattern('info-page', 'Page: info', 'about', J(pattern_ref('about-foundry'), spacer('var:preset|spacing|60'), pattern_ref('designer-profile'), spacer('var:preset|spacing|60'), pattern_ref('custom-type'), spacer('var:preset|spacing|60'), pattern_ref('help-contact')), block_types='core/post-content')

pattern('help-contact', 'Help and contact', 'contact', group(J(
    heading('Help', 3),
    ruled([('Licensing questions', '<a href="mailto:type@example.com">type@example.com</a>'), ('Invoices and VAT', '<a href="mailto:accounts@example.com">accounts@example.com</a>'),
           ('Missing a character?', 'Tell us. We add most requests in the next release.'), ('Discounts', 'Half price for students, charities and co-ops')])),
    className='is-style-rule-top', align='wide', layout={'type': 'constrained', 'contentSize': '1100px'}))

pattern('family-overview', 'Family overview', 'typefaces', group(J(
    *[group(row(J(spec(a, size='x-large', weight=500), para(b, fontSize='small')), justify='space-between'), className='is-style-style-row', align='wide', layout={'type': 'default'}) for a, b in [
        ('6 styles', 'Regular, Medium and Bold, each with an oblique'), ('612 glyphs', 'Latin Extended A, Vietnamese, arrows and fractions'),
        ('218 languages', 'Every Latin-script language we could test'), ('4 formats', 'OTF, TTF, WOFF2 and a variable TTF')]]), align='wide', layout={'type': 'default'}))

pattern('specimen-paragraphs', 'Specimen: text at reading sizes', 'specimen', columns(
    *[(None, J(NOTE(n), para('Margo was drawn for fish market boards, then for receipts, then for timetables. At reading sizes the wide lowercase and open counters keep it clear, and the figures line up in columns without being told to.', fontSize=f))) for n, f in [('14 pt', 'small'), ('18 pt', 'medium'), ('24 pt', 'large')]],
    align='wide'))

pattern('specimen-inverse', 'Specimen: white on black', 'specimen', group(J(
    NOTE('Margo Bold, 240 pt, inverse'), spec('Whelks £3', size='specimen', weight=700)), className='is-style-ink', align='full', layout={'type': 'constrained', 'contentSize': '1440px'}))

pattern('alternates', 'Alternates and stylistic sets', 'specimen', group(J(
    heading('Alternates', 2),
    columns(*[(None, J(NOTE(n), spec(t, size='xx-large', weight=500))) for n, t in [('Default a and g', 'agate'), ('ss01 single-storey a', '\u0251g\u0251te'), ('Default figures', '1470'), ('Small caps', 'ᴍᴀʀɢᴀᴛᴇ')]], align='wide')),
    align='wide', layout={'type': 'default'}))

pattern('figures-currency', 'Figures and currency', 'specimen', group(J(
    row(J(heading('Figures and currency', 2), NOTE('Tabular by default in Margo, oldstyle by default in Harbour')), justify='space-between', align='wide'),
    glyph_grid(list('0123456789') + ['£', '€', '$', '¥', '%', '½', '¼', '¾'])), align='wide', layout={'type': 'default'}))

pattern('punctuation-grid', 'Punctuation and symbols', 'specimen', group(J(
    heading('Punctuation', 3),
    glyph_grid(['.', ',', ':', ';', '!', '?', '\u2018', '\u2019', '\u201c', '\u201d', '(', ')', '[', ']', '/', '\u2192', '\u2190', '\u2191', '\u2193', '#', '*', '+', '='], cols='6rem')),
    align='wide', layout={'type': 'default'}))

pattern('specimen-poster', 'Specimen poster (sizes and pairing)', 'specimen', group(J(
    spec('Tide', size='specimen', weight=700),
    spec('tables and ferry times', size='display', family='accent', italic=True),
    columns((None, para('Margo Bold at 240 pt with Harbour Serif Italic at 128 pt. Printed as an A2 poster for the Margate Harbour Arm in 2025.', fontSize='small')), (None, NOTE('Poster available as a free PDF on request.')), align='wide')),
    className='is-style-galley', align='wide', layout={'type': 'default'}))

pattern('release-notes', 'Release notes', 'typefaces', group(J(
    heading('Release notes', 3),
    *[group(columns(('18%', NOTE(v)), (None, para(t))), className='is-style-style-row', layout={'type': 'default'}) for v, t in [
        ('1.3, Sep 2026', 'Vietnamese, a Black weight for Harbour, better kerning for W and Y with punctuation.'),
        ('1.2, Mar 2025', 'Small caps in every style. Fixed the Ł in Bold Oblique.'),
        ('1.1, Oct 2024', 'Variable font for Harbour. Tabular figures in Margo by default.'),
        ('1.0, Mar 2024', 'First release of Margo Grotesk.')]]), layout={'type': 'constrained'}), description='Every version, newest first. Buyers get updates free.')

pattern('designer-profile', 'Designer profile', 'about', columns(
    ('35%', image('type.jpg', IMG['type'])),
    (None, J(heading('Ines Moretti', 3), para('Ines trained as a sign painter in Bologna and moved to Margate in 2016. She draws every letter first with a brush, then on paper at 10 cm high, and only then on screen.'),
             para('Margo started as lettering for a fish stall on the harbour. The stall has gone but the sign is still there.', fontSize='small'))), align='wide', verticalAlignment='center'))

pattern('education-licence', 'Education and student licences', 'licensing', group(J(
    heading('Students and teachers', 4),
    para('Students get free desktop licences for coursework. Schools and universities pay half price for teaching licences. Email us from your college address.')),
    className='is-style-rule-top'))

pattern('typeface-cards', 'Typefaces as cards with a sample', 'typefaces', grid(J(*[group(J(
    NOTE(meta), spec(name, size='x-large', family=fam, weight=w), para(sample, fontSize='large', **({'fontFamily': fam} if fam else {})), para('<a href="%s">See the specimen</a>' % href, fontSize='small')),
    className='is-style-galley') for name, fam, w, meta, href, sample in [
        ('Margo Grotesk', None, 700, '6 styles, from £60', '/typefaces/margo-grotesk/', 'Fish, chips and a 4am tide.'),
        ('Harbour Serif', 'accent', 500, '18 styles, variable', '/typefaces/harbour-serif/', 'Long reading and short tempers.')]]), min_width='20rem', align='wide'))

pattern('foundry-news', 'Foundry news strip', 'typefaces', group(row(J(
    NOTE('News'), para('Harbour Serif 1.3 is out with Vietnamese support. Existing buyers can download it from their account.', fontSize='small'), para('<a href="/typefaces/harbour-serif/">See what changed</a>', fontSize='small')), justify='space-between'),
    className='is-style-rule-top', align='wide', layout={'type': 'default'}))

pattern('in-use-feature', 'In use: one project', 'in-use', columns(
    ('58%', image('shopfront.jpg', IMG['shopfront'], 'Wards the Florist, York, 2025')),
    (None, J(NOTE('Margo Grotesk Bold'), heading('Wards the Florist, York', 3),
             para('Fascia letters cut from brass by a sign maker in Leeds. The florist wanted the name to read from the other side of Clifford Street, and it does.'),
             para('<a href="/wards-the-florist-york/">More about this project</a>', fontSize='small'))), align='wide', verticalAlignment='center'))

TYPEFACES = [('Margo Grotesk', None, 700, '6 styles, from £60', '/typefaces/margo-grotesk/'), ('Harbour Serif', 'accent', 500, '18 styles, variable, from £60', '/typefaces/harbour-serif/')]

pattern('typefaces-list', 'Typefaces (large specimens as links)', 'featured', group(J(
    *[group(J(row(J(NOTE(meta), para('<a href="%s">See the specimen</a>' % href, fontSize='small')), justify='space-between'),
              spec('<a href="%s">%s</a>' % (href, name), size='display', family=fam, weight=w)),
            className='is-style-rule-top', align='wide', layout={'type': 'default'}) for name, fam, w, meta, href in TYPEFACES]),
    align='wide', layout={'type': 'default'}), description='Every family set in itself, as big as it goes, each a link to its page.')

GAP = spacer('var:preset|spacing|70')
pattern('typeface-page', 'Page: typeface (full specimen order)', 'featured', J(
    pattern_ref('specimen-hero'), GAP, pattern_ref('specimen-sizes'), GAP, pattern_ref('styles-list'), GAP, pattern_ref('opentype-features'), GAP,
    pattern_ref('glyph-grid'), GAP, pattern_ref('alternates'), GAP, pattern_ref('figures-currency'), GAP, pattern_ref('weight-waterfall-grotesk'), GAP, pattern_ref('specimen-paragraphs'), GAP,
    pattern_ref('specimen-inverse'), GAP, pattern_ref('family-overview'), pattern_ref('language-support'), pattern_ref('details'), GAP, pattern_ref('in-use'), GAP, pattern_ref('pairing'), GAP, pattern_ref('release-notes')),
    block_types='core/post-content', description='Specimen, sizes, styles, features, glyph set, weights, languages, credits and in-use, in that order.')

pattern('typeface-page-serif', 'Page: serif typeface', 'featured', J(
    group(J(row(J(NOTE('Harbour Serif, Medium, 240 pt'), NOTE('18 styles, variable 100 to 900')), justify='space-between', align='wide'),
            spec('Harbour', size='specimen', family='accent', weight=500),
            spec('Serif, for long reading and short tempers', size='xx-large', family='accent', italic=True),
            buttons(('Buy a licence', '/shop/'), ('Download free trials', '/trials/', {'className': 'is-style-outline'}))), align='wide', layout={'type': 'default'}),
    spacer('var:preset|spacing|70'), pattern_ref('weight-waterfall'), spacer('var:preset|spacing|70'), pattern_ref('glyph-grid-serif'), spacer('var:preset|spacing|70'), pattern_ref('punctuation-grid'), spacer('var:preset|spacing|70'), pattern_ref('licence-table')), block_types='core/post-content')

pattern('front-intro', 'Front page intro', 'featured', group(J(
    spec('Sawtooth Type', size='specimen', weight=700),
    columns(('60%', para('An independent type foundry in Margate. Two typefaces, both drawn for signs first and pages second. Trial fonts are free and licences are sold by use.', fontSize='large')),
            (None, J(NOTE('New in September'), para('Harbour Serif 1.3 adds Vietnamese and a Black weight. <a href="/typefaces/harbour-serif/">See the specimen</a>'))), align='wide')),
    align='wide', layout={'type': 'default'}))

INUSE_ITEM = J(dyn('post-featured-image', isLink=True, aspectRatio='3/2', scale='cover'), dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-terms', term='post_tag'))

pattern('in-use-grid', 'In use (latest posts)', 'query', group(J(
    row(J(heading('In use', 2), para('<a href="/in-use/">Everything in use</a>')), justify='space-between', align='wide'),
    query(INUSE_ITEM, per_page=4, query_id=51, align='wide', layout={'type': 'grid', 'columnCount': 4, 'minimumColumnWidth': '14rem'})),
    align='wide', layout={'type': 'default'}))

pattern('in-use-archive', 'In use archive (inherits the page query)', 'query', inherit_query(INUSE_ITEM, align='wide', layout={'type': 'grid', 'columnCount': 3, 'minimumColumnWidth': '16rem'}), inserter=False)

pattern('post-list', 'Search results list', 'query', inherit_query(
    group(J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', excerptLength=30)), className='is-style-rule-top'), align='wide'), inserter=False)

# ---------------------------------------------------------------- templates
MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|60'}}}

write('templates/front-page.html', J(template_part('header', 'header'), group(J(
    pattern_ref('front-intro'), pattern_ref('foundry-news'), pattern_ref('typefaces-list'), pattern_ref('glyph-grid'), pattern_ref('specimen-poster'), pattern_ref('in-use-feature'), pattern_ref('in-use-grid'), pattern_ref('trials')),
    tag='main', layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|70', 'padding': {'top': 'var:preset|spacing|40'}}}),
    template_part('footer', 'footer')))

write('templates/home.html', page_template(J(
    heading('In use', 1, align='wide'),
    para('Signs, books, menus and packaging set in our typefaces. Send us yours and we will add it.', align='wide', fontSize='large'),
    pattern_ref('in-use-archive')), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/index.html', open(os.path.join(D, 'templates/home.html')).read())
write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', level=1), pattern_ref('in-use-archive')), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide', level=1),
    dyn('search', label='Search', showLabel=False, buttonText='Search', align='wide'), pattern_ref('post-list')), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/404.html', page_template(J(
    spec('404', size='specimen', weight=700),
    para('Missing glyph. The page you asked for is not in this font.', fontSize='large'),
    buttons(('See the typefaces', '/typefaces/'))), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/single.html', J(template_part('header', 'header'), group(J(
    dyn('post-title', level=1, align='wide'), dyn('post-terms', term='post_tag', align='wide'),
    dyn('post-featured-image', align='wide'),
    dyn('post-content', layout={'type': 'constrained'}),
    group(J(dyn('post-navigation-link', type='previous', showTitle=True, label='Previous'), dyn('post-navigation-link', showTitle=True, label='Next')),
          align='wide', className='is-style-rule-top', layout={'type': 'flex', 'justifyContent': 'space-between'})),
    tag='main', layout={'type': 'constrained'}, style=MAINPAD), template_part('footer', 'footer')))
write('templates/page.html', page_template(J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'})), layout={'type': 'constrained'}, style=MAINPAD))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1), spacer('var:preset|spacing|40'), dyn('post-content', layout={'type': 'constrained', 'contentSize': '1100px'})),
                                                layout={'type': 'constrained', 'contentSize': '1100px'}, style=MAINPAD))
write('templates/page-typeface.html', page_template(dyn('post-content', align='full', layout={'type': 'constrained'}), layout={'type': 'constrained'}, style=MAINPAD))

print('glyph built')
