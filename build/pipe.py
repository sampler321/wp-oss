# pipe: design note
# Direction: a Swiss price index for a heating engineer. The owner asked for professional, toned-down elegant, clean and
#   technical, which fits the research's Swiss neo-grotesk idea; the mono face is gone and the red is kept for emergencies only.
# Why: people choosing a plumber want a phone number, a price and proof of registration, fast. A strict grid with a
#   numbered left index reads like a price list you can trust, and the phone number is set as large as the name.
# Fonts: Bespoke Sans only (light 300 for big headings, 400 body, 500 labels, 700 phone numbers).
# Palette: white, near-black, pale grey rows; hot red only for the emergency bar and call button, cold blue for links and booking.
# Layout idea: every section has a narrow left index column (label and number) and a wide right column; photos are
#   greyscale; the quote section triages urgency in the customer's own words before the phone rings.
import sys, json, os; sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('pipe')
S = THEME['slug']

# Round 2: map inserter categories so the pattern library groups well (first category = library page).
CATMAP = {'featured': 'hero', 'call-to-action': 'quote', 'contact': 'areas', 'testimonials': 'about', 'text': 'info', 'query': 'areas', 'banner': 'notices'}
_pattern = pattern
def pattern(slug, title, categories, body, **kw):
    cats = [CATMAP.get(c.strip(), c.strip()) for c in categories.split(',') if c.strip() and c.strip() != 'pipe'] or ['pages']
    return _pattern(slug, title, ','.join(dict.fromkeys(cats)), body, **kw)
D = THEME['dir']


def wjson(rel, data):
    p = os.path.join(D, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent='\t', ensure_ascii=False)
        f.write('\n')


fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
fonts.append({'fontFamily': '"Bespoke Sans", sans-serif', 'name': 'Bespoke Sans (text)', 'slug': 'body'})
PAL = [
    ('base', '#FFFFFF', 'White'),
    ('contrast', '#0E0E0E', 'Black'),
    ('accent', '#0057B8', 'Cold feed'),
    ('accent-2', '#C8101B', 'Hot feed'),
    ('surface', '#F2F2F2', 'Row grey'),
    ('line', '#0E0E0E', 'Rule'),
    ('muted', '#595959', 'Grey'),
    ('rule-light', '#D4D4D4', 'Light rule'),
]


def palette(over=None):
    over = over or {}
    return [{'slug': s, 'color': over.get(s, c), 'name': n} for s, c, n in PAL]


theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3,
    'settings': {
        'appearanceTools': True, 'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '760px', 'wideSize': '1400px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False, 'palette': palette()},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.875rem', 'name': 'Label', 'fluid': False},
                {'slug': 'small', 'size': '1rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.125rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.75rem', 'name': 'Large', 'fluid': {'min': '1.4rem', 'max': '1.75rem'}},
                {'slug': 'x-large', 'size': '2.75rem', 'name': 'Section', 'fluid': {'min': '2rem', 'max': '2.75rem'}},
                {'slug': 'xx-large', 'size': '4.5rem', 'name': 'Phone', 'fluid': {'min': '2.4rem', 'max': '4.5rem'}},
                {'slug': 'display', 'size': '9rem', 'name': 'Display', 'fluid': {'min': '3.3rem', 'max': '9rem'}},
            ]},
        'spacing': {'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'], 'spacingSizes': [
            {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
            {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
            {'slug': '50', 'size': 'clamp(1.5rem, 3.5vw, 2.5rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 4rem)', 'name': '6'},
            {'slug': '70', 'size': 'clamp(3rem, 8vw, 6rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 11vw, 9rem)', 'name': '8'}]},
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
                     ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '300', 'lineHeight': '1', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'lineHeight': '0.92', 'letterSpacing': '-0.03em'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'letterSpacing': '-0.02em'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'fontWeight': '400', 'lineHeight': '1.2'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '500', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500', 'lineHeight': '1.3', 'letterSpacing': '0'}},
            'button': {
                'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'},
                'border': {'radius': '0', 'width': '0'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.9em', 'bottom': '0.9em', 'left': '1.4em', 'right': '1.4em'}},
                ':hover': {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}},
                ':focus': {'outline': {'color': 'var:preset|color|accent', 'offset': '2px', 'style': 'solid', 'width': '2px'}}},
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontWeight': '500', 'letterSpacing': '-0.01em'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/site-tagline': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontWeight': '500'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}},
                                'css': '& .wp-block-navigation__responsive-container.is-menu-open{padding:var(--wp--preset--spacing--50)}& .wp-block-navigation__responsive-container.is-menu-open .wp-block-navigation-item{font-size:var(--wp--preset--font-size--x-large);font-weight:300}& .current-menu-item > a{box-shadow:inset 0 -2px 0 var(--wp--preset--color--contrast)}'},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/image': {'border': {'radius': '0'}, 'css': '& img{filter:grayscale(1) contrast(1.05)}'},
            'core/post-featured-image': {'css': '& img{filter:grayscale(1) contrast(1.05)}'},
            'core/separator': {'color': {'text': 'var:preset|color|contrast'}, 'border': {'width': '1px 0 0 0'}, 'css': '&{border-bottom:0!important;max-width:none}'},
            'core/quote': {'typography': {'fontSize': 'var:preset|font-size|medium', 'fontWeight': '400', 'lineHeight': '1.45'},
                           'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}, 'left': {'width': '0'}},
                           'spacing': {'padding': {'top': 'var:preset|spacing|30', 'left': '0'}},
                           'css': '& cite{font-size:var(--wp--preset--font-size--x-small);font-style:normal;color:var(--wp--preset--color--muted)}'},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '& table{border-collapse:collapse;border-top:1px solid var(--wp--preset--color--contrast)!important}& th{text-align:left;font-weight:500;border:0!important;border-bottom:1px solid var(--wp--preset--color--contrast)!important}& td{border:0!important;border-bottom:1px solid var(--wp--preset--color--rule-light)!important;font-variant-numeric:tabular-nums}& td,& th{padding:.75em 1em .75em 0}& tbody tr:nth-child(even){background:var(--wp--preset--color--surface)}& td:last-child{font-weight:500}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|rule-light', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-weight:500}'},
            'core/search': {'css': '& .wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:2px}'},
            'core/list': {'css': '&{padding-left:1.2em}'},
        },
        'css': ':where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none;font-variant-numeric:tabular-nums lining-nums}a[href^="tel:"]{white-space:nowrap}a:focus-visible,button:focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:2px}',
    },
    'templateParts': [{'area': 'header', 'name': 'header', 'title': 'Header'}, {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
                      {'area': 'uncategorized', 'name': 'emergency-bar', 'title': 'Emergency bar'}],
    'customTemplates': [{'name': 'page-index', 'title': 'Page with left index column', 'postTypes': ['page']}, {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']}],
}
wjson('theme.json', theme)

V3 = lambda title, pal: {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'settings': {'color': {'palette': palette(pal)}}}
wjson('styles/night-rate.json', V3('Night rate', {'base': '#0E0E0E', 'contrast': '#F2F2F2', 'accent': '#7FB2FF', 'accent-2': '#FF4D57', 'surface': '#1C1C1C', 'line': '#F2F2F2', 'muted': '#B3B3B3', 'rule-light': '#333333'}))
wjson('styles/copper.json', V3('Copper', {'accent': '#9A4A12', 'accent-2': '#B3141C', 'surface': '#F5EFEA', 'rule-light': '#E0D6CE'}))
wjson('styles/cold-feed.json', V3('Cold feed', {'base': '#E8F0FA', 'surface': '#D8E4F3', 'accent': '#00458F', 'rule-light': '#BFD0E6', 'muted': '#4A5566'}))

def section(slug, title, types, styles):
    wjson('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

section('emergency', 'Emergency bar (hot)', ['core/group'],
        {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|base'},
         'elements': {'link': {'color': {'text': 'var:preset|color|base'}, 'typography': {'fontWeight': '700'}}},
         'typography': {'fontSize': 'var:preset|font-size|small'}})
section('index-row', 'Index row (rule above)', ['core/columns', 'core/group'],
        {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|40'}, 'margin': {'top': 'var:preset|spacing|70'}}})
section('rule-bottom', 'Rule below', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}})
section('grey-panel', 'Grey panel', ['core/group', 'core/column'],
        {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
         'spacing': {'padding': {'top': 'var:preset|spacing|40', 'bottom': 'var:preset|spacing|40', 'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}}})
section('call-button', 'Call button (hot)', ['core/button'],
        {'color': {'background': 'var:preset|color|accent-2', 'text': 'var:preset|color|base'},
         'css': '& .wp-block-button__link:active{background:var(--wp--preset--color--base);color:var(--wp--preset--color--accent-2);box-shadow:inset 0 0 0 2px var(--wp--preset--color--accent-2)}'})
section('book-button', 'Booking button (cold)', ['core/button'],
        {'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'}})
section('service-index', 'Numbered service index', ['core/list'],
        {'typography': {'fontSize': 'var:preset|font-size|small'},
         'css': '&{list-style:none;padding:0!important;counter-reset:svc;border-top:1px solid var(--wp--preset--color--contrast)}& li{counter-increment:svc;display:grid;grid-template-columns:2.2rem 1fr;padding:.6rem 0;border-bottom:1px solid var(--wp--preset--color--rule-light)}& li::before{content:counter(svc);font-weight:500;color:var(--wp--preset--color--muted)}'})
section('phone', 'Phone number', ['core/paragraph'],
        {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '700', 'lineHeight': '1', 'letterSpacing': '-0.02em'},
         'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}})
section('label', 'Index label', ['core/paragraph', 'core/heading'],
        {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '500'}, 'color': {'text': 'var:preset|color|muted'}})

write('style.css', '''/*
Theme Name: Pipe
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A clean, grid-based theme for Gas Safe registered plumbers and heating engineers, with a price index, area pages and a quote section that sorts emergencies from routine jobs.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: pipe
Tags: business, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, two-columns
*/''')
write('functions.php', '''<?php
/**
 * Pipe: pattern category only.
 *
 * @package pipe
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'pipe', array( 'label' => __( 'Pipe: heating and plumbing', 'pipe' ) ) );
	}
);''')

PX = {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}
TEL = '<a href="tel:+441144960831">0114 496 0831</a>'
write('parts/emergency-bar.html', group(row(J(
    para('No heating or hot water? Call %s, 7am to 10pm every day.' % TEL),
    para('Smell gas? Leave the house and call the gas emergency line on <a href="tel:0800111999">0800 111 999</a> first.')), justify='space-between', align='wide'),
    tag='section', align='full', className='is-style-emergency', style={'spacing': {'padding': dict(top='var:preset|spacing|20', bottom='var:preset|spacing|20', **PX)}}))
write('parts/header.html', J(template_part('emergency-bar'),
    group(row(J(stack(J(dyn('site-title', level=0), dyn('site-tagline')), style={'spacing': {'blockGap': '0'}}),
                dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right', 'flexWrap': 'wrap'}),
                para(TEL, className='is-style-phone', fontSize='large')), justify='space-between', align='wide'),
          tag='section', align='full', className='is-style-rule-bottom', style={'spacing': {'padding': dict(top='var:preset|spacing|30', bottom='var:preset|spacing|30', **PX)}})))
write('parts/footer.html', group(J(
    columns(
        ('25%', J(para('Brennan Heating', fontSize='large'), para('Gas Safe register no. 612884', className='is-style-label'))),
        (None, J(heading('Office', 6), para('Unit 9, Mowbray Street<br>Sheffield S3 8EN<br>Office hours 8am to 5pm, Monday to Friday', fontSize='small'))),
        (None, J(heading('Phone and email', 6), para('%s<br><a href="mailto:jobs@example.com">jobs@example.com</a><br>Text 07700 900 312 with a photo' % TEL, fontSize='small'))),
        (None, J(heading('Check us', 6), para('<a href="https://www.gassaferegister.co.uk/">Gas Safe Register</a>, search 612884<br>Worcester Bosch accredited installer<br>Public liability cover £5m', fontSize='small'))),
        align='wide'),
    para('Demo photos are CC0 and public domain images from Wikimedia Commons, standing in for our own jobs.', align='wide', className='alignwide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', style={'spacing': {'padding': dict(top='var:preset|spacing|50', bottom='var:preset|spacing|50', **PX), 'margin': {'top': 'var:preset|spacing|70'}},
                                       'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}}))

MAINPAD = {'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|70'}}}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero'), pattern_ref('price-guide'), pattern_ref('urgency'), pattern_ref('service-included'), pattern_ref('areas-table'), pattern_ref('credentials'), pattern_ref('reviews'))))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), style=MAINPAD))
write('templates/page-index.html', page_template(J(
    dyn('post-title', level=1, align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1400px'})), style=MAINPAD))
area_row = J(columns(('25%', dyn('post-title', isLink=True, level=3, fontSize='large')), (None, dyn('post-excerpt', excerptLength=40)), className='is-style-index-row'))
write('templates/home.html', page_template(J(
    heading('Areas we cover', 1, align='wide'),
    para('Sheffield and about 12 miles out. Each area page lists the postcode districts, how quickly we usually get there, and a recent job nearby.', align='wide', className='alignwide'),
    pattern_ref('area-archive')), style=MAINPAD))
write('templates/archive.html', page_template(J(dyn('query-title', type='archive', showPrefix=False, align='wide'), dyn('term-description', align='wide'), pattern_ref('area-archive')), style=MAINPAD))
write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('area-archive')), style=MAINPAD))
write('templates/search.html', page_template(J(dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='S10, boiler service, CP12', buttonText='Search'), pattern_ref('area-archive')), style=MAINPAD))
write('templates/404.html', page_template(J(
    heading('No page here', 1),
    para('The address may be old. The <a href="/prices/">price guide</a> and <a href="/areas/">areas we cover</a> are the pages most people want. If it is urgent, call %s.' % TEL),
    dyn('search', label='Search', showLabel=False, placeholder='S10, boiler service, CP12', buttonText='Search')), style=MAINPAD))
write('templates/single.html', page_template(J(
    columns(('25%', J(para('Area', className='is-style-label'), dyn('post-terms', term='category'))),
            (None, J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'default'}))), align='wide'),
    columns(('25%', para('Photo', className='is-style-label')), (None, dyn('post-featured-image', aspectRatio='16/9', scale='cover')), align='wide', className='is-style-index-row'),
    columns(('25%', para('Next', className='is-style-label')),
            (None, J(dyn('post-navigation-link', type='previous', label='Previous area', showTitle=True), dyn('post-navigation-link', label='Next area', showTitle=True))), align='wide', className='is-style-index-row')), style=MAINPAD))

img = image
def idx(label, body, **kw):
    """A Swiss index row: small label in a narrow left column, content on the right."""
    return columns(('25%', para(label, className='is-style-label')), (None, body), align='wide', className='is-style-index-row', **kw)

SERVICES = ['Annual boiler service, from £72', 'Boiler repair, call-out £85 including the first hour', 'Boiler replacement, fixed quote after a free survey',
            'Landlord gas safety certificate (CP12), from £65', 'Radiators, valves and power flushing', 'Leaks, burst pipes and stopcocks',
            'Hot water cylinders and immersion heaters', 'Underfloor heating manifolds and controls']
pattern('hero', 'Hero: name, phone and service index', 'pipe,featured', group(J(
    heading('Boilers, heating and plumbing in Sheffield.', 1, align='wide'),
    columns(
        ('50%', J(para('Services and prices', className='is-style-label'), lst(SERVICES, className='is-style-service-index'), para('<a href="/prices/">The full price guide</a>', fontSize='small'))),
        (None, J(para('Call or text', className='is-style-label'), para(TEL, className='is-style-phone'),
                 para('Niall, Aisha and two engineers, all Gas Safe registered. We cover S1 to S14, S17, S35 and S60. Right now we are booking non-urgent work <strong>3 working days ahead</strong>.'),
                 buttons(('Call now', 'tel:+441144960831', {'className': 'is-style-call-button'}), ('Get a quote', '/quote/', {'className': 'is-style-book-button'})),
                 img('manifold.jpg', 'A brass underfloor heating manifold with six white and grey thermal actuators on top', 'Manifold with new actuators, Crookes, last week'))),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|50'}}}),
    description='Opener: the trade and the town as the headline, a numbered service index with prices, and the phone number at full size.')

pattern('price-guide', 'Price guide', 'pipe,services', idx('Price guide', J(
    heading('What things cost', 2),
    table([['Annual boiler service, gas', '45 to 60 minutes', '£72'], ['Service and landlord certificate (CP12) together', '1 hour 15', '£110'],
           ['Landlord gas safety certificate only, up to 3 appliances', '45 minutes', '£65'], ['Call-out, weekdays 8am to 6pm', 'includes first hour', '£85'],
           ['Call-out, evenings and weekends until 10pm', 'includes first hour', '£120'], ['Each extra half hour', '', '£32'],
           ['Power flush, up to 10 radiators', 'most of a day', '£450'], ['New combi boiler, like for like, fitted', '1 to 2 days', 'from £2,350']],
          head=['Job', 'Time on site', 'Price']),
    para('These are guide prices including VAT. For anything over £200 we confirm the price in writing before we start, and we stick to it unless we find something we have shown you and you have agreed to.', fontSize='small'))))

pattern('urgency', 'Quote: how urgent is it?', 'pipe,call-to-action', idx('Get a quote', J(
    heading('How urgent is it?', 2),
    para('Pick the line that sounds like you. It tells us whether to ring you back in ten minutes or book you in next week.'),
    columns(
        (None, group(J(heading('ASAP: I have no heating or hot water', 4),
                       para('Call us. If nobody picks up, text 07700 900 312 with your postcode and we ring back within 30 minutes, 7am to 10pm.', fontSize='small'),
                       buttons(('Call 0114 496 0831', 'tel:+441144960831', {'className': 'is-style-call-button'}))), className='is-style-grey-panel', layout={'type': 'default'})),
        (None, group(J(heading('Within 7 days: something is wrong but working', 4),
                       para('Dripping valve, noisy boiler, one cold radiator. Email the details and a photo and we book you in with a two-hour arrival window.', fontSize='small'),
                       buttons(('Email a job', 'mailto:jobs@example.com?subject=Within%207%20days', {'className': 'is-style-book-button'}))), className='is-style-grey-panel', layout={'type': 'default'})),
        (None, group(J(heading('Within a month: planned work', 4),
                       para('A service, a certificate, a new boiler or radiators. Email and we send dates and a fixed price, or arrange a free survey.', fontSize='small'),
                       buttons(('Book planned work', 'mailto:jobs@example.com?subject=Planned%20work', {'className': 'is-style-book-button'}))), className='is-style-grey-panel', layout={'type': 'default'}))),
    heading('Please tell us', 5),
    lst(['What kind of property: flat, terrace, semi, detached or a shop', 'The boiler make and model, from the sticker on the front or underneath',
         'Any fault code on the display', 'Whether you are a tenant or the owner (landlords pay, not tenants)'])),
    ), description='The signature: the quote section asks how urgent the job is in the customer\'s own words and what property it is.')

pattern('service-included', 'What a service includes', 'pipe,services', idx('Boiler service', J(
    heading('What a service includes', 3),
    columns(
        (None, lst(['Flue gas analysis with a calibrated analyser, printed', 'Gas pressure and flow rate checked against the manufacturer\'s figures',
                    'Burner, heat exchanger and condensate trap cleaned', 'Seals and flue joints checked', 'Expansion vessel pressure topped up'])),
        (None, J(lst(['Controls and thermostat tested', 'Carbon monoxide alarm tested, or fitted for £28 if you have none', 'Service record filled in, so your warranty stays valid',
                      'A written report emailed the same day']),
                 para('We service Worcester Bosch, Vaillant, Ideal, Baxi, Viessmann, Glow-worm and Potterton. We don\'t work on oil or LPG boilers.', fontSize='small')))))))

pattern('areas-table', 'Areas and response times', 'pipe,contact', idx('Areas', J(
    heading('Where we go and how fast', 3),
    table([['Sheffield city centre and Kelham', 'S1, S3', 'Same day, usually within 2 hours'], ['Crookes, Walkley, Broomhill', 'S6, S10', 'Same day'],
           ['Sharrow, Nether Edge, Ecclesall', 'S7, S11', 'Same day'], ['Hillsborough, Stannington', 'S6, S35', 'Same or next day'],
           ['Dronfield and Totley', 'S17, S18', 'Next day'], ['Rotherham', 'S60, S65', 'Next day']], head=['Area', 'Postcodes', 'Emergency response']),
    para('Postcode not listed? We are probably too far to get there quickly. The <a href="https://www.gassaferegister.co.uk/">Gas Safe Register</a> lists engineers near you.', fontSize='small'))))

pattern('credentials', 'Registration and cover', 'pipe,about', idx('Registration', J(
    columns(
        (None, J(heading('Gas Safe 612884', 4), para('Check it on the <a href="https://www.gassaferegister.co.uk/">Gas Safe Register</a>. Every engineer carries their own card. Ask to see it at the door.', fontSize='small'))),
        (None, J(heading('City & Guilds', 4), para('Niall and Aisha hold City & Guilds 6035 in plumbing and heating. Kacper is finishing his in 2027.', fontSize='small'))),
        (None, J(heading('Accredited installer', 4), para('Worcester Bosch and Vaillant, so their boilers come with up to 10 years\' guarantee when we fit them.', fontSize='small'))),
        (None, J(heading('Insured', 4), para('£5m public liability with Hiscox. Certificate sent on request, which letting agents usually want.', fontSize='small')))))))

pattern('reviews', 'Reviews (named)', 'pipe,testimonials', idx('Reviews', columns(
    (None, quote('Boiler died on a Sunday in January. Aisha was here by 3, had it going by 4, and charged exactly what the website said.', 'Hannah, Walkley, January 2026')),
    (None, quote('Five rental flats, five certificates, one visit, one invoice. That is all I ask of anyone.', 'Tariq, landlord, Kelham Island, March 2026')),
    (None, quote('Quoted £2,450 for the new combi, invoiced £2,450. Took the old one away and hoovered.', 'Pat and Jim, Nether Edge, May 2026')))))

pattern('while-you-wait', 'What to do while you wait', 'pipe,text', idx('While you wait', J(
    heading('What to do while you wait', 3),
    columns(
        (None, J(heading('Water coming through', 5), lst(['Turn off the stopcock. It is usually under the kitchen sink, sometimes where the pipe comes into the house.',
                                                       'Turn off the electrics at the fuse box if water is near lights or sockets.',
                                                       'Open the cold taps to drain the pipes.'], ordered=True))),
        (None, J(heading('Smell of gas', 5), lst(['Open doors and windows. Don\'t use switches or anything that sparks.',
                                                  'Turn off the gas at the meter: the lever goes across the pipe.',
                                                  'Leave the house and call 0800 111 999. Then call us.'], ordered=True))),
        (None, img('stopcock.jpg', 'A small cast-iron plate on a red brick wall marked S.V., showing where the stop valve is', 'An S.V. plate marks the outside stop valve'))))))

pattern('emergency-page', 'Page: emergency', 'pipe', J(pattern_ref('urgency'), pattern_ref('while-you-wait'), pattern_ref('call-out-prices')), block_types='core/post-content')

pattern('call-out-prices', 'Call-out prices', 'pipe,services', idx('Call-out', J(
    table([['Weekdays 8am to 6pm', '£85, includes the first hour'], ['Evenings until 10pm and weekends', '£120, includes the first hour'], ['After 10pm', 'We don\'t go out. Call the gas emergency line for gas, and turn off the stopcock for water.']],
          head=['When', 'Price']))))

pattern('servicing-page', 'Page: boiler servicing', 'pipe', J(pattern_ref('service-included'), pattern_ref('brands'), pattern_ref('service-reminder')), block_types='core/post-content')

pattern('brands', 'Brands we work on', 'pipe,services', idx('Brands', J(
    para('Worcester Bosch, Vaillant, Ideal, Baxi, Viessmann, Glow-worm, Potterton, Alpha, Intergas. Parts for the first four are on the van most days.'),
    img('boiler.jpg', 'Black and white photo of gas engineers kneeling around a floor-standing boiler during a training session', 'Training day, a long time before any of us'))))

pattern('service-reminder', 'Service reminder', 'pipe,call-to-action', idx('Reminders', J(
    para('We text you 11 months after your service. Reply YES and we book you in. Reply STOP and we never text again.'),
    buttons(('Book a service', 'mailto:jobs@example.com?subject=Service', {'className': 'is-style-book-button'})))))

pattern('replacement', 'Boiler replacement', 'pipe,services', idx('New boilers', J(
    heading('Replacing a boiler', 3),
    columns(
        (None, J(para('We survey first, for free, and it takes about 40 minutes. You get a written fixed price with the boiler model, flue, controls and any pipe changes listed line by line.'),
                 para('Most like-for-like combi swaps take a day. Moving the boiler or converting from a system with a tank takes two.'),
                 para('Finance is available through V12 Retail Finance on jobs over £1,000, if you want it.', fontSize='small'))),
        (None, img('cylinder.jpg', 'A white hot water cylinder mounted on a tiled wall with pipes underneath', 'Cylinder we took out in Broomhill. It had done 22 years.'))))))

pattern('boilers-page', 'Page: boilers', 'pipe', J(pattern_ref('replacement'), pattern_ref('price-guide'), pattern_ref('radiators')), block_types='core/post-content')

pattern('radiators', 'Radiators and controls', 'pipe,services', idx('Radiators', columns(
    (None, J(heading('Radiators and valves', 4), para('New radiator, same size, fitted and bled: £240 including a standard double convector. Thermostatic valves: £45 each fitted, less if we are there anyway.'))),
    (None, img('radiator.jpg', 'Close-up of a white panel radiator with a thermostatic valve head')))))

pattern('landlords', 'Landlords', 'pipe,services', idx('Landlords', J(
    heading('Landlord gas safety', 3),
    para('A CP12 certificate every 12 months is a legal requirement for any rented home with gas. We check every gas appliance, flue and alarm, and email the certificate the same day.'),
    table([['First property', '£65'], ['Each extra property, same visit day', '£50'], ['With a boiler service', '£110 total'], ['Portfolio of 10 or more', 'Ask for a yearly rate']], head=['What', 'Price']),
    para('We arrange access with tenants directly, give them a two-hour window and send you a text when the certificate is done.', fontSize='small'))))

pattern('landlords-page', 'Page: landlords', 'pipe', J(pattern_ref('landlords'), pattern_ref('credentials')), block_types='core/post-content')

pattern('prices-page', 'Page: prices', 'pipe', J(pattern_ref('price-guide'), pattern_ref('call-out-prices'), pattern_ref('payment')), block_types='core/post-content')

pattern('payment', 'Paying', 'pipe,text', idx('Paying', J(
    para('Card, bank transfer or phone payment on the day. We invoice landlords and letting agents with 14 days to pay. We don\'t take cash, so nobody carries it in the van.'))))

pattern('quote-page', 'Page: get a quote', 'pipe', J(pattern_ref('urgency'), pattern_ref('photo-tip'), pattern_ref('faq')), block_types='core/post-content')

pattern('photo-tip', 'Photo tip', 'pipe,text', idx('Photos help', columns(
    (None, J(para('Send three photos: the whole boiler, the sticker with the model, and the pipes underneath. It saves a visit about half the time.'),
             para('Text them to 07700 900 312 or attach them to your email.', fontSize='small'))),
    (None, img('solder.jpg', 'Racks of copper pipe fittings in labelled bins at a plumbing merchant', 'The fittings aisle at the merchant on Mowbray Street')))))

pattern('faq', 'Questions', 'pipe,text', idx('Questions', J(
    details('Do you charge for quotes?', para('No, for planned work. Emergency call-outs are charged from arrival.')),
    details('Can you come on a Sunday?', para('For no heating or hot water, yes, until 10pm, at the evening rate. Planned work is weekdays only.')),
    details('Do you do bathrooms?', para('We do the plumbing for bathroom fitters. We don\'t tile or plaster.')),
    details('How long is the guarantee?', para('12 months on our labour. New boilers carry the manufacturer\'s guarantee on top, up to 10 years.')))))

pattern('area-archive', 'Area list (inherits the page query)', 'pipe,query', inherit_query(area_row, align='wide'), inserter=False)

pattern('lead-time', 'Lead time line', 'pipe,banner', group(
    para('Booking non-urgent work <strong>3 working days ahead</strong>. Updated Monday 29 September.', align='left'),
    className='is-style-grey-panel', layout={'type': 'constrained'}),
    description='A one-line status the owner edits from a phone. Change the number and the date.')

pattern('tools', 'Tools of the trade (illustration)', 'pipe,about', idx('Since 1940', J(
    img('wrench.jpg', 'A watercolour drawing of an old pipe wrench on cream paper', 'Pipe wrench, drawn for the Index of American Design, 1940'),
    para('Some tools have not changed much. We still carry one of these, next to the flue gas analyser that costs more than the van\'s tyres.', fontSize='small'))))

pattern('about-page', 'Page: about', 'pipe', J(pattern_ref('team'), pattern_ref('credentials'), pattern_ref('tools')), block_types='core/post-content')

pattern('team', 'Who comes to your house', 'pipe,about', idx('People', J(
    heading('Who comes to your house', 3),
    table([['Niall Brennan', 'Boilers, installs, surveys', 'Gas Safe since 2009'], ['Aisha Siddiqui', 'Repairs, landlords, the difficult ones', 'Gas Safe since 2014'],
           ['Kacper Wróbel', 'Servicing and radiators', 'Gas Safe since 2021'], ['Dom Hollis', 'Plumbing, leaks, cylinders', 'Plumber, not gas registered']],
          head=['Name', 'Does', 'Registered']),
    para('Niall started Brennan Heating in 2013 in a Transit with no shelves. Aisha joined in 2016 and runs the diary. Both still do jobs every day.'))))



# =====================================================================================
# Round 2: no tables on the home page (price rows), a name-and-fact opener, fault codes,
# tenants, winter checklist, job photos, contact, guarantee. Area posts use the kit.
# =====================================================================================
section('price-row', 'Index row: job and price', ['core/group'],
        {'border': {'bottom': {'color': 'var:preset|color|rule-light', 'width': '1px', 'style': 'solid'}},
         'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}},
         'css': '&{display:flex!important;justify-content:space-between;align-items:baseline;gap:1rem;flex-wrap:wrap}& > *{margin:0!important}& > *:last-child{font-weight:500;font-variant-numeric:tabular-nums}&:nth-child(even){background:var(--wp--preset--color--surface)}'})

def rows(pairs):
    return J(*[group(J(para(a), para(b)), className='is-style-price-row', layout={'type': 'default'}) for a, b in pairs])

write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1400px'})), style=MAINPAD))

pattern('hero', 'Opener: name, phone and service index', 'hero', group(J(
    heading('Brennan Heating, Sheffield', 1, align='wide'),
    columns(
        ('50%', J(para('Services and prices', className='is-style-label'), lst(SERVICES, className='is-style-service-index'), para('<a href="/prices/">The full price guide</a>', fontSize='small'))),
        (None, J(para('Call or text', className='is-style-label'), para(TEL, className='is-style-phone'),
                 para('Gas Safe register 612884. Niall, Aisha and two engineers covering S1 to S14, S17, S35 and S60. Right now we are booking non-urgent work <strong>3 working days ahead</strong>.'),
                 buttons(('Call now', 'tel:+441144960831', {'className': 'is-style-call-button'}), ('Get a quote', '/quote/', {'className': 'is-style-book-button'})),
                 image('manifold.jpg', 'A brass underfloor heating manifold with six white and grey thermal actuators on top', 'Manifold with new actuators, Crookes, last week'))),
        align='wide', style={'spacing': {'blockGap': {'left': 'var:preset|spacing|60'}}})),
    align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': 'var:preset|spacing|50'}}}),
    description='Opener: the name and the town, the Gas Safe number and lead time, a numbered service index with prices, and the phone number at full size.')

PRICES = [('Annual boiler service, gas', '£72'), ('Service and landlord certificate (CP12) together', '£110'), ('Landlord certificate only, up to 3 appliances', '£65'),
          ('Call-out, weekdays 8am to 6pm, first hour', '£85'), ('Call-out, evenings and weekends, first hour', '£120'), ('Each extra half hour', '£32'),
          ('Power flush, up to 10 radiators', '£450'), ('New combi boiler, like for like, fitted', 'from £2,350')]
pattern('price-guide', 'Price guide (rows)', 'services', idx('Price guide', J(
    heading('What things cost', 2), rows(PRICES),
    para('Guide prices including VAT. For anything over £200 we confirm the price in writing before we start, and we stick to it. <a href="/prices/">Full price list with times</a>', fontSize='small'))))

pattern('price-list-table', 'Price list with time on site (table)', 'services', idx('Price list', J(
    table([['Annual boiler service, gas', '45 to 60 minutes', '£72'], ['Service and CP12 together', '1 hour 15', '£110'], ['Landlord certificate only', '45 minutes', '£65'],
           ['Call-out, weekdays', 'first hour included', '£85'], ['Call-out, evenings and weekends', 'first hour included', '£120'], ['Each extra half hour', '', '£32'],
           ['Power flush, up to 10 radiators', 'most of a day', '£450'], ['Radiator swap, same size', '2 hours', '£240'], ['New combi boiler, like for like', '1 to 2 days', 'from £2,350']],
          head=['Job', 'Time on site', 'Price']),
    para('Prices include VAT and parts listed. Parts not listed are charged at cost, shown on the invoice with the merchant\'s receipt.', fontSize='small'))))

pattern('areas-table', 'Areas and response times', 'areas', idx('Areas', J(
    heading('Where we go and how fast', 3),
    rows([('City centre and Kelham, S1 and S3', 'Same day, usually within 2 hours'), ('Crookes, Walkley, Broomhill, S6 and S10', 'Same day'),
          ('Sharrow, Nether Edge, Ecclesall, S7 and S11', 'Same day'), ('Hillsborough, Stannington, S6 and S35', 'Same or next day'),
          ('Dronfield and Totley, S17 and S18', 'Next day'), ('Rotherham, S60 and S65', 'Next day')]),
    para('Postcode not listed? We are probably too far to get there quickly. The <a href="https://www.gassaferegister.co.uk/">Gas Safe Register</a> lists engineers near you. <a href="/areas/">Every area</a>', fontSize='small'))))

pattern('call-out-prices', 'Call-out prices', 'services', idx('Call-out', rows([('Weekdays 8am to 6pm', '£85, includes the first hour'), ('Evenings until 10pm and weekends', '£120, includes the first hour'),
    ('After 10pm', 'We don\'t go out. Gas: call 0800 111 999. Water: turn off the stopcock.')])))

pattern('landlords', 'Landlords', 'services', idx('Landlords', J(
    heading('Landlord gas safety', 3),
    para('A CP12 certificate every 12 months is a legal requirement for any rented home with gas. We check every gas appliance, flue and alarm, and email the certificate the same day.'),
    rows([('First property', '£65'), ('Each extra property, same visit day', '£50'), ('With a boiler service', '£110 total'), ('Portfolio of 10 or more', 'Ask for a yearly rate')]),
    para('We arrange access with tenants directly, give them a two-hour window and text you when the certificate is done.', fontSize='small'))))

pattern('team', 'Who comes to your house', 'about', idx('People', J(
    heading('Who comes to your house', 3),
    rows([('Niall Brennan, boilers, installs, surveys', 'Gas Safe since 2009'), ('Aisha Siddiqui, repairs, landlords, the difficult ones', 'Gas Safe since 2014'),
          ('Kacper Wróbel, servicing and radiators', 'Gas Safe since 2021'), ('Dom Hollis, plumbing, leaks, cylinders', 'Plumber, not gas registered')]),
    para('Niall started Brennan Heating in 2013 in a Transit with no shelves. Aisha joined in 2016 and runs the diary. Both still do jobs every day.'))))

pattern('fault-codes', 'Common boiler fault codes', 'info', idx('Fault codes', J(
    heading('What the code on your boiler means', 3),
    rows([('Worcester EA 227', 'No flame detected. Check the gas is on at the meter, then reset once.'), ('Vaillant F.22', 'Low water pressure. Top up to 1.2 bar with the filling loop.'),
          ('Ideal F1', 'Low water pressure. Same fix as above.'), ('Baxi E133', 'Gas supply or ignition. Check other gas appliances work.'),
          ('Worcester D5', 'Outside sensor fault. Heating still works, call us in office hours.')]),
    para('Reset once. If the code comes back, stop and call us. Resetting over and over can lock the boiler out.', fontSize='small'))))

pattern('on-the-day', 'What happens on the day', 'info', idx('On the day', lst([
    'We text when we are 20 minutes away, with the engineer\'s name and Gas Safe card number.', 'Shoe covers on at the door, dust sheet down under the boiler.',
    'We tell you what we found before we fix anything that costs more than the quote.', 'We test, show you the readings, and clear up.',
    'The report and invoice arrive by email the same day.'], ordered=True)))

pattern('guarantee', 'Guarantee', 'about', idx('Guarantee', columns(
    (None, J(heading('12 months on our work', 4), para('If something we fixed fails within a year, we come back and fix it free.', fontSize='small'))),
    (None, J(heading('Up to 10 years on new boilers', 4), para('Worcester Bosch and Vaillant guarantees, registered by us on the day we fit.', fontSize='small'))),
    (None, J(heading('Fixed prices', 4), para('Over £200, the price is agreed in writing before we start.', fontSize='small'))))))

pattern('finance', 'Finance note', 'services', idx('Finance', para('New boilers over £1,000 can be spread over 1 to 5 years through V12 Retail Finance. The survey is free either way, and the fixed price is the same whether you pay now or monthly.')))

pattern('tenants', 'For tenants', 'info', idx('Tenants', J(
    heading('Renting? Here is what to do', 3),
    lst(['Tell your landlord or letting agent first. They pay for repairs to the boiler and pipes.', 'If they use us, we contact you to arrange a time. You don\'t pay us.',
         'No heating or hot water for more than 24 hours? That is urgent. Chase them, then call us if they agree.', 'Your landlord must give you a copy of the gas safety certificate every year.']))))

pattern('tenants-page', 'Page: tenants', 'pages', J(pattern_ref('tenants'), pattern_ref('fault-codes'), pattern_ref('while-you-wait')), block_types='core/post-content')

pattern('winter-checklist', 'Before winter', 'info', idx('Before winter', J(
    heading('Five things to check in October', 3),
    lst(['Put the heating on for an hour before you need it. Better to find a fault now.', 'Bleed any radiator that is cold at the top.', 'Check the pressure gauge reads 1 to 1.5 bar when cold.',
         'Lag the condensate pipe if it runs outside. A frozen one stops the boiler.', 'Book the service before November, when everyone else does.'], ordered=True))))

pattern('job-photos', 'Recent jobs in photos', 'about', idx('Recent jobs', gallery([
    ('manifold.jpg', 'A brass underfloor manifold with thermal actuators', 'Manifold, Crookes'), ('cylinder.jpg', 'A white hot water cylinder on a tiled wall', 'Old cylinder out, Broomhill'),
    ('radiator.jpg', 'A white panel radiator with a thermostatic valve', 'New radiator and TRV, Walkley'), ('gauge.jpg', 'An old pressure gauge on a stand', 'Not ours, but we like it')], columns=4)))

pattern('contact-details', 'Contact details', 'areas', idx('Contact', columns(
    (None, J(heading('Phone', 5), para(TEL + '<br>7am to 10pm every day for no heating or hot water. Office hours 8 to 5 for everything else.', fontSize='small'))),
    (None, J(heading('Text or WhatsApp', 5), para('07700 900 312. Send a photo of the boiler and the fault code.', fontSize='small'))),
    (None, J(heading('Email and post', 5), para('<a href="mailto:jobs@example.com">jobs@example.com</a><br>Unit 9, Mowbray Street, Sheffield S3 8EN', fontSize='small'))))))

pattern('co-alarm', 'Carbon monoxide alarm', 'info', idx('CO alarms', para('Every room with a gas appliance should have a carbon monoxide alarm. If yours is missing or over 7 years old, we fit a new one for £28 at any visit. Test it monthly with the button.')))

pattern('power-flush', 'Power flushing', 'services', idx('Power flush', columns(
    (None, J(heading('When a power flush helps', 4), para('Radiators cold at the bottom, a boiler that bangs, or black water when you bleed a radiator. It takes most of a day and costs £450 for up to 10 radiators.'))),
    (None, J(heading('When it doesn\'t', 4), para('One cold radiator is usually a valve. A cold radiator upstairs is usually balancing. We check those first, so you don\'t pay for a flush you don\'t need.'))))))

pattern('partners', 'Who we work with', 'about', idx('Partners', rows([('Totley Tiling', 'We do the plumbing, they tile'), ('Hillsborough Electrical', 'For boiler wiring and controls'),
    ('Mowbray Street merchants', 'Parts, same day'), ('Sheffield letting agents', 'Certificates for four agencies')])))

pattern('contact-page', 'Page: contact', 'pages', J(pattern_ref('contact-details'), pattern_ref('lead-time'), pattern_ref('areas-table')), block_types='core/post-content')
pattern('prices-page', 'Page: prices', 'pages', J(pattern_ref('price-list-table'), pattern_ref('call-out-prices'), pattern_ref('finance'), pattern_ref('payment'), pattern_ref('guarantee')), block_types='core/post-content')
pattern('servicing-page', 'Page: boiler servicing', 'pages', J(pattern_ref('service-included'), pattern_ref('on-the-day'), pattern_ref('brands'), pattern_ref('fault-codes'), pattern_ref('winter-checklist'), pattern_ref('service-reminder')), block_types='core/post-content')
pattern('boilers-page', 'Page: boilers', 'pages', J(pattern_ref('replacement'), pattern_ref('price-guide'), pattern_ref('finance'), pattern_ref('guarantee'), pattern_ref('radiators'), pattern_ref('power-flush')), block_types='core/post-content')
pattern('about-page', 'Page: about', 'pages', J(pattern_ref('team'), pattern_ref('credentials'), pattern_ref('job-photos'), pattern_ref('partners'), pattern_ref('tools'), pattern_ref('reviews')), block_types='core/post-content')
pattern('emergency-page', 'Page: emergency', 'pages', J(pattern_ref('urgency'), pattern_ref('while-you-wait'), pattern_ref('call-out-prices'), pattern_ref('co-alarm')), block_types='core/post-content')
pattern('landlords-page', 'Page: landlords', 'pages', J(pattern_ref('landlords'), pattern_ref('credentials'), pattern_ref('tenants')), block_types='core/post-content')

CATS = [('hero', 'Pipe: openers'), ('services', 'Pipe: services and prices'), ('quote', 'Pipe: quotes and urgency'), ('areas', 'Pipe: areas and contact'), ('about', 'Pipe: people and registration'),
        ('info', 'Pipe: help and advice'), ('notices', 'Pipe: notices'), ('pages', 'Pipe: page layouts')]
write('functions.php', """<?php
/**
 * Pipe: pattern categories only.
 *
 * @package pipe
 */

add_action(
	'init',
	function () {
%s
	}
);""" % '\n'.join("\t\tregister_block_pattern_category( '%s', array( 'label' => __( '%s', 'pipe' ) ) );" % c for c in CATS))

write('templates/front-page.html', page_template(J(
    pattern_ref('hero'), pattern_ref('price-guide'), pattern_ref('urgency'), pattern_ref('service-included'), pattern_ref('areas-table'), pattern_ref('credentials'), pattern_ref('job-photos'), pattern_ref('reviews'))))

# ---- demo content: area posts built from index rows ----
CJ = 'demos/pipe/content.json'
C = json.load(open(CJ))
import re as _re
for po in C['posts']:
    src = po.setdefault('src', po['content'])
    paras = _re.findall(r'<p>(.*?)</p>', src)
    cells = _re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td></tr>', src)
    po['content'] = J(para(paras[0], fontSize='large'), idx('At a glance', rows(cells)), idx('Recent job', para(paras[-1])),
                      idx('Book', buttons(('Call 0114 496 0831', 'tel:+441144960831', {'className': 'is-style-call-button'}), ('Get a quote', '/quote/', {'className': 'is-style-book-button'}))))
pages = {p['slug']: p for p in C['pages']}
pages['tenants'] = {'slug': 'tenants', 'title': 'Tenants', 'pattern': 'pipe/tenants-page', 'template': 'page-index'}
pages['contact'] = {'slug': 'contact', 'title': 'Contact', 'pattern': 'pipe/contact-page', 'template': 'page-index'}
C['pages'] = list(pages.values())
C['nav'] = [{'label': l, 'url': u} for l, u in [('Emergency', '/emergency/'), ('Servicing', '/servicing/'), ('New boilers', '/boilers/'), ('Landlords', '/landlords/'),
            ('Tenants', '/tenants/'), ('Prices', '/prices/'), ('Areas', '/areas/'), ('Contact', '/contact/'), ('Get a quote', '/quote/')]]
json.dump(C, open(CJ, 'w'), indent=1, ensure_ascii=False)
print('pipe: build done')
