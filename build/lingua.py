# lingua: Joanna Pryce, translator from Portuguese and Spanish into English, Porto (idea 132, as researched).
# Direction: a parallel text. Every important statement is set twice, English left and Portuguese right, the way a
#   translator works, so the site itself is the writing sample. Proofreader's red is the only colour.
# Fonts: Noto Serif Display (display, registry face, high contrast, covers every Latin accent) and Noto Sans (body).
#   Two families, no mono.
# Palette: paper white, ink black, proof red #B5121B, galley grey surface, pencil line.
# Layout idea: split columns with a hairline between them, the Portuguese side in italic; a proof sheet on the front page
#   where a machine translation is struck through and corrected in red; published work as a bibliography list.
import sys, json, os
sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('lingua')
S = 'lingua'
D = THEME['dir']

PALETTE = [
    ('base', '#FFFFFF', 'Paper'),
    ('contrast', '#111111', 'Ink'),
    ('accent', '#B5121B', 'Proof red'),
    ('surface', '#F2F0EB', 'Galley'),
    ('line', '#CFCBC3', 'Pencil line'),
    ('muted', '#5B5853', 'Graphite'),
    ('highlight', '#FBE7A6', 'Highlighter'),
]

fonts = json.load(open(os.path.join(D, '.fonts.json')))['fontFamilies']
FOCUS = {'outline': {'color': 'var:preset|color|accent', 'offset': '3px', 'style': 'solid', 'width': '2px'}}
PAD = lambda t, b: {'top': 'var:preset|spacing|%s' % t, 'bottom': 'var:preset|spacing|%s' % b}

theme = {
    '$schema': 'https://schemas.wp.org/trunk/theme.json',
    'version': 3,
    'settings': {
        'appearanceTools': True,
        'useRootPaddingAwareAlignments': True,
        'layout': {'contentSize': '700px', 'wideSize': '1240px'},
        'color': {'defaultPalette': False, 'defaultGradients': False, 'defaultDuotone': False,
                  'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in PALETTE]},
        'typography': {
            'defaultFontSizes': False, 'fluid': True, 'textAlign': True, 'writingMode': False,
            'fontFamilies': fonts,
            'fontSizes': [
                {'slug': 'x-small', 'size': '0.8125rem', 'name': 'Note', 'fluid': False},
                {'slug': 'small', 'size': '0.9375rem', 'name': 'Small', 'fluid': False},
                {'slug': 'medium', 'size': '1.1875rem', 'name': 'Body', 'fluid': False},
                {'slug': 'large', 'size': '1.5rem', 'name': 'Large', 'fluid': {'min': '1.3rem', 'max': '1.5rem'}},
                {'slug': 'x-large', 'size': '2.25rem', 'name': 'Section', 'fluid': {'min': '1.75rem', 'max': '2.25rem'}},
                {'slug': 'xx-large', 'size': '3.5rem', 'name': 'Title', 'fluid': {'min': '2.4rem', 'max': '3.5rem'}},
                {'slug': 'display', 'size': '5rem', 'name': 'Display', 'fluid': {'min': '2.75rem', 'max': '5rem'}},
            ],
        },
        'spacing': {
            'defaultSpacingSizes': False, 'units': ['px', 'rem', '%', 'vw', 'vh'],
            'spacingSizes': [
                {'slug': '10', 'size': '0.25rem', 'name': '1'}, {'slug': '20', 'size': '0.5rem', 'name': '2'},
                {'slug': '30', 'size': '1rem', 'name': '3'}, {'slug': '40', 'size': 'clamp(1.25rem, 2vw, 1.5rem)', 'name': '4'},
                {'slug': '50', 'size': 'clamp(1.5rem, 3vw, 2.25rem)', 'name': '5'}, {'slug': '60', 'size': 'clamp(2rem, 5vw, 3.5rem)', 'name': '6'},
                {'slug': '70', 'size': 'clamp(3rem, 7vw, 5rem)', 'name': '7'}, {'slug': '80', 'size': 'clamp(4rem, 10vw, 8rem)', 'name': '8'},
            ],
        },
        'shadow': {'defaultPresets': False, 'presets': []},
        'border': {'color': True, 'radius': True, 'style': True, 'width': True,
                   'radiusSizes': [{'slug': 'none', 'size': '0', 'name': 'Square'}, {'slug': 'input', 'size': '2px', 'name': 'Input'}]},
        'custom': {'measure': '64ch'},
    },
    'styles': {
        'color': {'background': 'var:preset|color|base', 'text': 'var:preset|color|contrast'},
        'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.6'},
        'spacing': {'padding': {'left': 'var:preset|spacing|40', 'right': 'var:preset|spacing|40'}, 'blockGap': 'var:preset|spacing|30'},
        'elements': {
            'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'underline'},
                     ':hover': {'color': {'text': 'var:preset|color|accent'}}, ':focus': FOCUS},
            'heading': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'lineHeight': '1.08', 'letterSpacing': '-0.01em'}},
            'h1': {'typography': {'fontSize': 'var:preset|font-size|display', 'fontWeight': '400'}},
            'h2': {'typography': {'fontSize': 'var:preset|font-size|xx-large', 'fontWeight': '400'}},
            'h3': {'typography': {'fontSize': 'var:preset|font-size|x-large'}},
            'h4': {'typography': {'fontSize': 'var:preset|font-size|large', 'lineHeight': '1.25'}},
            'h5': {'typography': {'fontSize': 'var:preset|font-size|medium', 'lineHeight': '1.3'}},
            'h6': {'typography': {'fontSize': 'var:preset|font-size|small', 'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'lineHeight': '1.4'}},
            'button': {
                'color': {'background': 'var:preset|color|accent', 'text': 'var:preset|color|base'},
                'border': {'radius': '0', 'width': '0'},
                'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600', 'fontSize': 'var:preset|font-size|small'},
                'spacing': {'padding': {'top': '0.75em', 'bottom': '0.75em', 'left': '1.3em', 'right': '1.3em'}},
                ':hover': {'color': {'background': 'var:preset|color|contrast', 'text': 'var:preset|color|base'}},
                ':focus': FOCUS,
            },
            'caption': {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'italic', 'lineHeight': '1.5'}, 'color': {'text': 'var:preset|color|muted'}},
        },
        'blocks': {
            'core/site-title': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '500', 'fontSize': 'var:preset|font-size|large'},
                                'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}}}},
            'core/navigation': {'typography': {'fontSize': 'var:preset|font-size|small'},
                                'elements': {'link': {'typography': {'textDecoration': 'none'}, ':hover': {'typography': {'textDecoration': 'underline'}}}}},
            'core/post-title': {'elements': {'link': {'color': {'text': 'var:preset|color|contrast'}, 'typography': {'textDecoration': 'none'}, ':hover': {'color': {'text': 'var:preset|color|accent'}}}}},
            'core/post-date': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-terms': {'typography': {'fontSize': 'var:preset|font-size|x-small'}, 'color': {'text': 'var:preset|color|muted'}},
            'core/post-excerpt': {'typography': {'fontSize': 'var:preset|font-size|small'}},
            'core/separator': {'color': {'text': 'var:preset|color|line'}, 'border': {'width': '1px 0 0 0'}},
            'core/quote': {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|large', 'fontStyle': 'italic', 'lineHeight': '1.35'},
                           'border': {'left': {'color': 'var:preset|color|accent', 'width': '2px', 'style': 'solid'}},
                           'spacing': {'padding': {'left': 'var:preset|spacing|40'}},
                           'elements': {'cite': {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'normal'}}}},
            'core/table': {'typography': {'fontSize': 'var:preset|font-size|small'},
                           'css': '&{font-variant-numeric:tabular-nums}& th{text-align:left;font-weight:600}& td{border-width:0 0 1px 0!important;border-color:var(--wp--preset--color--line);padding:.6em .4em}& th{border-width:0 0 1px 0!important;border-color:var(--wp--preset--color--contrast);padding:.6em .4em}'},
            'core/details': {'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
                             'spacing': {'padding': {'top': 'var:preset|spacing|30', 'bottom': 'var:preset|spacing|30'}},
                             'css': '& summary{font-family:var(--wp--preset--font-family--display);font-size:var(--wp--preset--font-size--large);cursor:pointer}'},
            'core/search': {'css': '& .wp-block-search__input{border:1px solid var(--wp--preset--color--contrast);border-radius:2px}'},
            'core/query-pagination': {'typography': {'fontSize': 'var:preset|font-size|small'}},
        },
        'css': '.is-style-parallel{gap:0!important}.is-style-parallel > .wp-block-column{padding-block:var(--wp--preset--spacing--20)}.is-style-parallel > .wp-block-column + .wp-block-column{font-style:italic;border-top:1px solid var(--wp--preset--color--line);padding-top:var(--wp--preset--spacing--40)}@media (min-width:782px){.is-style-parallel > .wp-block-column + .wp-block-column{border-top:0;border-left:1px solid var(--wp--preset--color--line);padding-top:var(--wp--preset--spacing--20);padding-left:var(--wp--preset--spacing--50)}.is-style-parallel > .wp-block-column:first-child{padding-right:var(--wp--preset--spacing--50)}}.wp-block-post-content > * + :is(h2,h3,.wp-block-columns,.wp-block-media-text,.wp-block-group,.wp-block-image){margin-block-start:var(--wp--preset--spacing--60)}:where(h1,h2,h3){text-wrap:balance}:where(p,li){text-wrap:pretty}body{font-synthesis:none;font-variant-numeric:oldstyle-nums}'
               ':where(.wp-block-post-content) > p{max-width:var(--wp--custom--measure)}'
               'mark.has-accent-color{font-weight:600}s{text-decoration-color:var(--wp--preset--color--accent);text-decoration-thickness:2px;color:var(--wp--preset--color--muted)}'
               'a:focus-visible,summary:focus-visible,input:focus-visible,button:focus-visible{outline:2px solid var(--wp--preset--color--accent);outline-offset:3px}',
    },
    'templateParts': [
        {'area': 'header', 'name': 'header', 'title': 'Header'},
        {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    ],
    'customTemplates': [
        {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    ],
}
with open(os.path.join(D, 'theme.json'), 'w') as f:
    json.dump(theme, f, indent='\t', ensure_ascii=False)

write('style.css', '''/*
Theme Name: Lingua
Theme URI: https://github.com/sampler321/wp-oss
Author: WP-OSS
Author URI: https://github.com/sampler321/wp-oss
Description: A two-language theme for freelance translators, with parallel columns for source and target text and a bibliography of published translations.
Version: 1.0.0
Requires at least: 6.7
Tested up to: 6.9
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: lingua
Tags: portfolio, blog, full-site-editing, block-patterns, block-styles, style-variations, custom-colors, editor-style, wide-blocks, two-columns, translation-ready
*/''')


def variation(name, title, changes, extra=None):
    pal = [(s, changes.get(s, c), n) for s, c, n in PALETTE]
    d = {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title,
         'settings': {'color': {'palette': [{'slug': s, 'color': c, 'name': n} for s, c, n in pal]}}}
    if extra:
        d['styles'] = extra
    write('styles/%s.json' % name, json.dumps(d, indent='\t', ensure_ascii=False))


variation('specimen', 'Specimen', {'surface': '#F6F6F4', 'line': '#D9D9D6'})
variation('galley-proof', 'Galley proof', {'base': '#F0EEE9', 'surface': '#E4E1D9', 'line': '#BDB8AE', 'muted': '#55524D'})
variation('night-desk', 'Night desk', {'base': '#1A1A1A', 'contrast': '#F0EEE9', 'accent': '#F0717A', 'surface': '#262625', 'line': '#4A4845', 'muted': '#B9B5AD', 'highlight': '#5A4A12'})


def section(slug, title, types, styles):
    write('styles/sections/%s.json' % slug, json.dumps({'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles}, indent='\t'))


section('parallel', 'Parallel text', ['core/columns'], {'spacing': {'blockGap': '0'}})
section('lang-tag', 'Language tag', ['core/paragraph'], {
    'color': {'text': 'var:preset|color|accent'},
    'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontStyle': 'normal', 'fontWeight': '600'},
})
section('pad-lg', 'Roomy section', ['core/group'], {'spacing': {'padding': PAD(70, 70)}})
section('page-main', 'Page body', ['core/group'], {'spacing': {'padding': PAD(60, 70)}})
section('site-header', 'Site header', ['core/group'], {'border': {'bottom': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': PAD(30, 30)}})
section('site-footer', 'Site footer', ['core/group'], {'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'}, 'spacing': {'padding': PAD(70, 50)}})
section('proof', 'Proof sheet', ['core/group'], {
    'color': {'background': 'var:preset|color|surface', 'text': 'var:preset|color|contrast'},
    'border': {'left': {'color': 'var:preset|color|accent', 'width': '3px', 'style': 'solid'}},
    'spacing': {'padding': {'top': 'var:preset|spacing|50', 'bottom': 'var:preset|spacing|50', 'left': 'var:preset|spacing|50', 'right': 'var:preset|spacing|50'}},
})
section('rule-top', 'Rule above', ['core/group'], {'border': {'top': {'color': 'var:preset|color|contrast', 'width': '1px', 'style': 'solid'}}, 'spacing': {'padding': {'top': 'var:preset|spacing|30'}}})
section('bibliography', 'Bibliography list', ['core/post-template'], {
    'css': '& > li{border-top:1px solid var(--wp--preset--color--line);padding-block:var(--wp--preset--spacing--40);margin:0!important}& > li:last-child{border-bottom:1px solid var(--wp--preset--color--line)}',
})
section('status', 'Status line', ['core/paragraph', 'core/group'], {
    'color': {'background': 'var:preset|color|highlight', 'text': 'var:preset|color|contrast'},
    'spacing': {'padding': {'top': 'var:preset|spacing|10', 'bottom': 'var:preset|spacing|10', 'left': 'var:preset|spacing|20', 'right': 'var:preset|spacing|20'}},
    'typography': {'fontSize': 'var:preset|font-size|small'},
    'css': '&{display:inline-block}',
})
section('pair', 'Language pair line', ['core/paragraph'], {
    'typography': {'fontFamily': 'var:preset|font-family|display', 'fontSize': 'var:preset|font-size|xx-large', 'lineHeight': '1.1'},
    'border': {'bottom': {'color': 'var:preset|color|line', 'width': '1px', 'style': 'solid'}},
    'spacing': {'padding': {'bottom': 'var:preset|spacing|30'}},
})


def parallel(en, pt, tag_en='English', tag_pt='Português', **attrs):
    """en, pt: block strings for each side."""
    return columns((None, J(para(tag_en, className='is-style-lang-tag'), en)),
                   (None, J(para(tag_pt, className='is-style-lang-tag'), pt)),
                   className='is-style-parallel', **attrs)


EMAIL = 'joanna@example.com'
PHONE = '+351 912 000 471'
BOOKED = 'Booked until 14 November. The next free slot for a short academic paper is 3 November.'

# ---------------------------------------------------------------- front page
pattern('hero-parallel', 'Hero: the same statement in two languages', 'featured', group(J(
    parallel(heading('I translate Portuguese and Spanish books, papers and exhibitions into English.', 1, fontSize='xx-large'),
             heading('Traduzo livros, artigos e exposições do português e do espanhol para inglês.', 2, fontSize='xx-large'),
             align='wide'),
    columns(('58%', para('I\'m Joanna Pryce. I grew up in Swansea and have lived in Porto since 2011. I translate literary fiction, history and social science, and the texts on museum walls. English is my first language, and the only one I translate into.', fontSize='large')),
            (None, J(para(BOOKED, className='is-style-status'),
                     buttons(('Send me the file for a quote', '/contact/')))), align='wide', verticalAlignment='bottom')),
    align='full', className='is-style-pad-lg'), description='The signature opening: an English statement and its Portuguese version side by side.')

pattern('language-pairs', 'Language pairs and direction', 'text', group(J(
    para('Portuguese <span aria-hidden="true">→</span> English', className='is-style-pair'),
    para('Spanish <span aria-hidden="true">→</span> English', className='is-style-pair'),
    para('Into English only, my first language. European and Brazilian Portuguese both, and Spanish from Spain and the Río de la Plata. I don\'t translate out of English.', fontSize='small')),
    align='wide', layout={'type': 'default'}), description='The pairs in large type with the direction spelled out.')

pattern('proof-sheet', 'Proof sheet: a machine translation, corrected', 'featured,text', group(J(
    heading('What the machine gets wrong', 2, fontSize='x-large'),
    para('From a label for the river-boat room at Casa do Rio, Vila Nova de Gaia.', fontSize='small'),
    parallel(
        para('<s>The rabelo boats transported the wine of the Douro until the caves of Gaia.</s> <mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-accent-color">Rabelo boats carried wine down the Douro to the lodges in Gaia.</mark> <s>The voyage could delay three days and, in the return, the boats were pulled river above by pairs of oxen.</s> <mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-accent-color">The trip could take three days, and on the way back oxen towed the boats upriver.</mark>', fontSize='large'),
        para('Os barcos rabelos transportavam o vinho do Douro até às caves de Gaia. A viagem podia demorar três dias e, na volta, os barcos eram puxados rio acima por juntas de bois.', fontSize='large'),
        tag_en='Machine output, with my corrections', tag_pt='Original label'),
    para('Caves are cellars here, and a port lodge is never a cave. That is the sort of thing a free tool gets wrong on a museum wall, where two hundred thousand people a year will read it.', fontSize='small')),
    className='is-style-proof', align='wide', layout={'type': 'default'}), description='Machine output struck through, with the human translation in red beside the source.')

pattern('recent-translations', 'Recent translations (bibliography)', 'portfolio,query', group(J(
    row(J(heading('Recent translations', 2, fontSize='x-large'), para('<a href="/translations/">Full list since 2012</a>', fontSize='small')), justify='space-between', align='wide'),
    query(group(J(dyn('post-featured-image', isLink=True, width='5.5rem', aspectRatio='3/4'),
                stack(J(dyn('post-title', isLink=True, level=3, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=30), dyn('post-terms', term='category')))), layout={'type': 'flex', 'flexWrap': 'nowrap', 'verticalAlignment': 'top'}),
          per_page=4, align='wide', template_class='is-style-bibliography')),
    align='wide', layout={'type': 'default'}))

pattern('bibliography-archive', 'Bibliography archive (inherits the query)', 'portfolio,query', inherit_query(
    group(J(dyn('post-featured-image', isLink=True, width='5.5rem', aspectRatio='3/4'),
          stack(J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', moreText='', excerptLength=40), dyn('post-terms', term='category')))), layout={'type': 'flex', 'flexWrap': 'nowrap', 'verticalAlignment': 'top'}),
    align='wide', template_class='is-style-bibliography'), inserter=False)

pattern('post-list', 'Post list', 'posts,query', inherit_query(
    J(dyn('post-title', isLink=True, level=2, fontSize='large'), dyn('post-excerpt', moreText='')), template_class='is-style-bibliography'), inserter=False)

pattern('fields', 'Fields I work in', 'services', J(
    heading('Fields', 2, fontSize='x-large'),
    columns(
        (None, J(heading('Fiction and memoir', 4), para('Novels, short stories and the occasional memoir. Sample chapters for publishers and agents, and full books once a publisher has bought the rights.', fontSize='small'))),
        (None, J(heading('History and social science', 4), para('Articles for journals, book chapters and whole monographs, mostly on land, labour and migration in Portugal and Spain since 1850.', fontSize='small'))),
        (None, J(heading('Museums and exhibitions', 4), para('Wall texts, labels, audio-guide scripts and catalogues. I write to the character count you give me.', fontSize='small'))),
        (None, J(heading('Wine and the Douro', 4), para('Back labels, tasting notes and quinta websites. I have lived next to the lodges long enough to know a lagar from a tonel.', fontSize='small'))),
        align='wide')))

pattern('credentials-line', 'Memberships line', 'about', para(
    'Member of the Institute of Translation and Interpreting (MITI, no. 21437) and of the Associação Portuguesa de Tradutores. I work to the <a href="https://www.iti.org.uk/">ITI Code of Professional Conduct</a>.',
    fontSize='small'))

# ---------------------------------------------------------------- services
pattern('rates', 'Services and rates', 'services', J(
    heading('Services and rates', 2),
    table([['Literary translation', 'per 1,000 source words', 'from €100'],
           ['Academic articles and books', 'per 1,000 source words', '€120'],
           ['Exhibition and museum texts', 'per 1,000 source words', '€130'],
           ['Revision of an English translation', 'per hour', '€45'],
           ['Reader\'s report for a publisher (sample and report)', 'per book', '€280']],
          head=['What', 'Charged', 'Rate']),
    para('The minimum fee is €60. Work needed in under 48 hours costs 40% more, if I can take it at all. Prices exclude VAT, which applies inside Portugal only.', fontSize='small')))

pattern('what-i-dont-do', 'What I don\'t take on', 'text', group(J(
    heading('What I don\'t take on', 4),
    para('Certified translations of birth certificates, court papers and medical records. Those need a sworn translator, and the APT directory lists them. I also don\'t post-edit machine translations of fiction: it takes longer than translating, and the result is worse.')),
    className='is-style-proof'))

pattern('quote-what-to-send', 'Asking for a quote (what to send)', 'call-to-action', J(
    heading('Asking for a quote', 3),
    lst(['The file, or a representative sample of it. Word or a PDF with selectable text is best.',
         'The word count, if you have it. I charge on the source text.',
         'When you need it back, and whether that date is fixed.',
         'Who will read it: a journal, an editor, visitors to a gallery.'], ordered=True),
    para('I reply within one working day with a price and a date. Email <a href="mailto:%s">%s</a>.' % (EMAIL, EMAIL))))

pattern('turnaround', 'Turnaround', 'services', J(
    heading('How long it takes', 3),
    para('About 2,000 words a day for academic and museum texts, 1,200 for fiction, plus a day for revision at the end. A 90,000-word novel takes me four to five months, and I book those a year ahead.')))

pattern('services-page', 'Page: services', 'services', J(
    pattern_ref('language-pairs'), pattern_ref('rates'), pattern_ref('turnaround'), pattern_ref('what-i-dont-do'), pattern_ref('quote-what-to-send')), block_types='core/post-content')

# ---------------------------------------------------------------- examples
EX = [
    ('Fiction', 'From <em>The Salt Year</em> by Rita Cordeiro (Small Hours Books, 2025)',
     'My grandmother salted the cod in the yard, on her knees, like someone praying. She said salt was the only thing the sea gave back without asking for anything in return.',
     'A minha avó salgava o bacalhau no quintal, de joelhos, como quem reza. Dizia que o sal era a única coisa que o mar nos devolvia sem pedir nada em troca.'),
    ('History', 'From <em>Cork Oak Country</em> by Helena Sarmento (Tamar University Press, 2023)',
     'Between 1890 and 1975 the area of cork-oak woodland in the Alentejo grew by about a third, mostly on estates of more than five hundred hectares.',
     'Entre 1890 e 1975, a área de montado no Alentejo aumentou cerca de um terço, sobretudo em propriedades com mais de quinhentos hectares.'),
    ('Museum label', 'Casa do Rio, Vila Nova de Gaia, 2025',
     'Rabelo boats carried wine down the Douro to the lodges in Gaia. The trip could take three days, and on the way back oxen towed the boats upriver.',
     'Os barcos rabelos transportavam o vinho do Douro até às caves de Gaia. A viagem podia demorar três dias e, na volta, os barcos eram puxados rio acima por juntas de bois.'),
]
for i, (field, src, en, pt) in enumerate(EX):
    slug = ['example-fiction', 'example-history', 'example-museum'][i]
    pattern(slug, 'Example: %s (source and translation)' % field.lower(), 'text', group(J(
        heading(field, 3), para(src, fontSize='small'),
        parallel(para(en, fontSize='large'), para(pt, fontSize='large'), tag_en='My English', tag_pt='Original')),
        align='wide', layout={'type': 'default'}))

pattern('example-spanish', 'Example: Spanish street sign', 'text', media_text('azulejo.jpg', 'A painted tile street sign reading Calle Divina Pastora, with a blue and yellow border and a figure of a shepherdess',
    J(heading('Spanish, too', 3),
      para('Calle Divina Pastora is not "Divine Shepherdess Street" in an English guidebook. It stays Calle Divina Pastora, with a note if the reader needs one. Most of translating place names is knowing when to leave them alone.')),
    width=40, align='wide'))

pattern('examples-page', 'Page: examples', 'text', J(
    para('Three short passages from published work, with the original beside each one. Publishers and authors gave permission for these to appear here.'),
    pattern_ref('example-fiction'), pattern_ref('example-history'), pattern_ref('example-museum'), pattern_ref('proof-sheet'), pattern_ref('example-spanish')), block_types='core/post-content')

# ---------------------------------------------------------------- credentials, about, faq, contact
pattern('credentials', 'Credentials', 'about', J(
    heading('Training and memberships', 2),
    table([['2006', 'BA Spanish and Portuguese, Cardiff University'],
           ['2008', 'MA Translation Studies, University of Bristol'],
           ['2008 to 2011', 'In-house translator and reviser at a translation company in Lisbon'],
           ['Since 2012', 'Freelance, from Porto'],
           ['Since 2014', 'MITI, Institute of Translation and Interpreting, no. 21437'],
           ['Since 2016', 'Member, Associação Portuguesa de Tradutores']]),
    pattern_ref('credentials-line'),
    para('Profiles: <a href="https://www.proz.com/">ProZ</a> and <a href="https://orcid.org/">ORCID</a>, where the academic translations are listed with their DOIs.', fontSize='small')))

pattern('about-desk', 'About: desk and working hours', 'about', media_text('desk2.jpg', 'A desk lamp lighting a pile of old leather-bound books on a dark table',
    J(heading('Where I work', 3),
      para('A desk in a shared studio on Rua do Heroísmo in Bonfim, eight minutes from Campanhã station, with four dictionaries I still open and one I keep for sentimental reasons.'),
      para('Porto is on UK time, so a call at ten in London is ten here. I work Monday to Friday and answer email twice a day.', fontSize='small')),
    width=45, align='wide'))

pattern('credentials-page', 'Page: credentials', 'about', J(pattern_ref('credentials'), pattern_ref('about-desk'), pattern_ref('clients')), block_types='core/post-content')

pattern('clients', 'People I translate for', 'about', J(
    heading('People I translate for', 3),
    para('Small Hours Books, Afton Press, Tamar University Press, the <em>Journal of Iberian Social History</em>, Casa do Rio in Gaia, four Douro quintas and a lot of individual academics who need their article in English by Friday.')))

pattern('faq', 'Questions translators get asked', 'text', J(
    details('Do you charge on the source or the target word count?', para('Source. You know the price before I start, and it doesn\'t change because English came out longer.')),
    details('Can you work in InDesign?', para('I can translate from an IDML export and give you back a file your designer can flow in. I don\'t do the layout.')),
    details('Will my name or the author\'s be credited?', para('For books I ask for a credit on the title page, which is normal practice. For academic articles, a line in the acknowledgements is enough.')),
    details('Is my manuscript kept confidential?', para('Yes. I don\'t upload clients\' texts to online translation tools, and I will sign your NDA.')),
    details('How do I pay?', para('Bank transfer in euros or sterling, within 30 days of the invoice. Publishers usually pay half on signing and half on delivery.')),
    details('Can you interpret at a meeting?', para('Occasionally, for small academic events in Porto, and only from Portuguese into English. For conferences you need a booth team, and I can recommend two.'))))

pattern('faq-page', 'Page: FAQ', 'text', J(pattern_ref('faq'), pattern_ref('what-i-dont-do')), block_types='core/post-content')

pattern('contact-details', 'Contact details', 'contact', columns(
    (None, J(heading('Email is best', 2, fontSize='x-large'),
             para('<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL), fontSize='large'),
             para('Phone or WhatsApp %s, weekdays 9:30 to 18:00, Porto time (the same as London).' % PHONE),
             para(BOOKED, className='is-style-status'))),
    (None, J(heading('Studio', 4), para('Rua do Heroísmo 240, 2.º<br>4300-256 Porto, Portugal'),
             para('Visits by appointment. The studio is on the second floor and there is no lift.', fontSize='small'))),
    align='wide'))

pattern('contact-page', 'Page: contact', 'contact', J(pattern_ref('contact-details'), pattern_ref('quote-what-to-send')), block_types='core/post-content')

# ---------------------------------------------------------------- Portuguese mirror
pattern('portugues-page', 'Page: the site in Portuguese', 'text', J(
    heading('Tradução do português e do espanhol para inglês', 2, fontSize='xx-large'),
    para('Chamo-me Joanna Pryce. Nasci em Swansea, no País de Gales, e vivo no Porto desde 2011. Traduzo ficção, história e ciências sociais, e os textos das paredes dos museus. Traduzo apenas para inglês, a minha língua materna.'),
    para(BOOKED.replace('Booked until 14 November. The next free slot for a short academic paper is 3 November.', 'Tenho a agenda preenchida até 14 de novembro. A próxima vaga para um artigo académico curto é a 3 de novembro.'), className='is-style-status'),
    heading('Preços', 3),
    table([['Tradução literária', 'por 1000 palavras do original', 'a partir de 100 €'],
           ['Artigos e livros académicos', 'por 1000 palavras do original', '120 €'],
           ['Textos de exposições e museus', 'por 1000 palavras do original', '130 €'],
           ['Revisão de tradução para inglês', 'por hora', '45 €']], head=['Serviço', 'Base', 'Preço']),
    para('O valor mínimo é de 60 €. Trabalhos urgentes, com menos de 48 horas, têm um acréscimo de 40%. Não faço traduções certificadas.'),
    heading('Contacto', 3),
    para('Escreva para <a href="mailto:%s">%s</a> e envie o ficheiro ou uma amostra, o número de palavras e a data de entrega. Respondo no prazo de um dia útil.' % (EMAIL, EMAIL))), block_types='core/post-content')

pattern('city-note', 'Porto note with photo', 'about', image('porto2.jpg', 'Two wooden rabelo boats moored on the Douro below the steep houses of Porto and the iron arch of the Dom Luís bridge', 'Rabelo boats below the Dom Luís I bridge. The museum label on this page is about them.'))

print('patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

# ---------------------------------------------------------------- parts
write('parts/header.html', group(group(J(
    row(J(dyn('site-title', level=0), para('Portuguese and Spanish into English', fontSize='x-small', textColor='muted')), style={'spacing': {'blockGap': 'var:preset|spacing|30'}}),
    row(J(dyn('navigation', overlayBackgroundColor='base', overlayTextColor='contrast', layout={'type': 'flex', 'justifyContent': 'right'}),
          para('<strong>EN</strong> / <a href="/portugues/" lang="pt">PT</a>', fontSize='small')), style={'spacing': {'blockGap': 'var:preset|spacing|40'}})),
    align='wide', layout={'type': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}),
    tag='header', align='full', className='is-style-site-header', layout={'type': 'constrained'}))

write('parts/footer.html', group(J(
    columns(
        ('50%', J(para('Joanna Pryce', fontFamily='display', fontSize='x-large'),
                  para('Translator from Portuguese and Spanish into English. Porto, since 2011.', fontSize='small'))),
        (None, J(heading('Contact', 6), para('<a href="mailto:%s">%s</a><br>%s<br>Weekdays, UK and Porto time' % (EMAIL, EMAIL, PHONE), fontSize='small'))),
        (None, J(heading('Studio', 6), para('Rua do Heroísmo 240<br>4300-256 Porto<br><a href="/portugues/" lang="pt">Esta página em português</a>', fontSize='small'))),
        align='wide'),
    pattern_ref('credentials-line'),
    para('Demo photos are CC0 or public domain images from Wikimedia Commons, used as stand-ins. Book titles, authors and publishers in the demo are invented.', align='wide', fontSize='x-small', textColor='muted')),
    tag='footer', align='full', className='is-style-site-footer', layout={'type': 'constrained'}))

# ---------------------------------------------------------------- templates
M = {'className': 'is-style-page-main'}
write('templates/front-page.html', page_template(J(
    pattern_ref('hero-parallel'),
    group(pattern_ref('language-pairs'), align='wide', layout={'type': 'default'}),
    group(pattern_ref('recent-translations'), align='wide', layout={'type': 'default'}, className='is-style-pad-lg'),
    pattern_ref('proof-sheet'),
    group(pattern_ref('fields'), align='wide', layout={'type': 'default'}, className='is-style-pad-lg'),
    group(pattern_ref('quote-what-to-send'), align='full', backgroundColor='surface', className='is-style-pad-lg', layout={'type': 'constrained'})),
    layout={'type': 'constrained'}, style={'spacing': {'blockGap': 'var:preset|spacing|60'}}))

write('templates/home.html', page_template(J(
    heading('Published translations', 1, align='wide', fontSize='xx-large'),
    para('Books, academic work and exhibitions, newest first. Filter by kind:', align='wide'),
    dyn('categories', align='wide', className='is-style-default'),
    pattern_ref('bibliography-archive')), **M))

write('templates/archive.html', page_template(J(
    dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'),
    dyn('term-description', align='wide'),
    pattern_ref('bibliography-archive')), **M))

write('templates/index.html', page_template(J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')), **M))
write('templates/search.html', page_template(J(
    dyn('query-title', type='search', align='wide'),
    dyn('search', label='Search', showLabel=False, placeholder='Author, title or field', buttonText='Search'),
    pattern_ref('post-list')), **M))
write('templates/404.html', page_template(J(
    parallel(heading('Page not found', 1, fontSize='xx-large'), heading('Página não encontrada', 2, fontSize='xx-large'), align='wide'),
    para('The link may be old. The <a href="/translations/">list of translations</a> is complete, or search below.'),
    dyn('search', label='Search', showLabel=False, placeholder='Author, title or field', buttonText='Search')), **M))
write('templates/page.html', page_template(J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'constrained'})), **M))
write('templates/page-wide.html', page_template(J(dyn('post-title', level=1, align='wide', fontSize='xx-large'),
                                                  dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1240px'})), **M))
write('templates/single.html', page_template(J(
    columns(('30%', J(dyn('post-featured-image', aspectRatio='3/4'), dyn('post-terms', term='category'), dyn('post-date'))),
            (None, J(dyn('post-title', level=1, fontSize='xx-large'), dyn('post-content', layout={'type': 'default'}))), align='wide'),
    group(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)),
          align='wide', layout={'type': 'flex', 'justifyContent': 'space-between'}, className='is-style-rule-top')), **M))
print('theme written')

# ---------------------------------------------------------------- demo
def book(title, cat, img, excerpt, en, pt, facts, date, tag_pt='Original'):
    body = J(para(excerpt, fontSize='large'),
             parallel(para(en), para(pt), tag_en='My English', tag_pt=tag_pt),
             table(facts))
    return {'title': title, 'category': cat, 'image': img, 'excerpt': excerpt, 'date': date, 'content': body}


POSTS = [
    book('The Salt Year, by Rita Cordeiro', 'books', 'books.jpg',
         'Novel, from Portuguese. Small Hours Books, London, 2025. Original title: O Ano do Sal.',
         'My grandmother salted the cod in the yard, on her knees, like someone praying.', 'A minha avó salgava o bacalhau no quintal, de joelhos, como quem reza.',
         [['Original', '<em>O Ano do Sal</em>, 2021'], ['Length', '84,000 words'], ['Publisher', 'Small Hours Books, London'], ['Support', 'Translation grant from DGLAB']], '2025-10-02'),
    book('River Workers, exhibition texts for Casa do Rio', 'exhibitions', 'porto2.jpg',
         'Wall texts and 64 labels, from Portuguese. Casa do Rio, Vila Nova de Gaia, 2025.',
         'Rabelo boats carried wine down the Douro to the lodges in Gaia.', 'Os barcos rabelos transportavam o vinho do Douro até às caves de Gaia.',
         [['Words', '9,200'], ['Character limit', '400 per label, including spaces'], ['Time', 'Five weeks, with two rounds of curator comments']], '2025-06-12'),
    book('Tram 28 and Other Stories, by Duarte Mesquita', 'books', 'lisbon.jpg',
         'Short stories, from Portuguese. Afton Press, 2024. Original title: O 28 e Outras Histórias.',
         'The tram stopped where it always stopped, and nobody got off.', 'O elétrico parou onde parava sempre, e ninguém saiu.',
         [['Original', '<em>O 28 e Outras Histórias</em>, 2019'], ['Length', '11 stories, 52,000 words'], ['Publisher', 'Afton Press']], '2024-09-20'),
    book('Cork Oak Country, by Helena Sarmento', 'academic', 'library.jpg',
         'History monograph, from Portuguese. Tamar University Press, 2023.',
         'Between 1890 and 1975 the area of cork-oak woodland in the Alentejo grew by about a third.', 'Entre 1890 e 1975, a área de montado no Alentejo aumentou cerca de um terço.',
         [['Length', '112,000 words and 40 tables'], ['Terms', 'A 300-entry glossary, agreed with the author before chapter one'], ['Funding', 'Paid from the author\'s research grant']], '2023-11-05'),
    book('A House of Tiles, by Carmen Olmedo', 'books', 'tiles.jpg',
         'Novel, from Spanish. Small Hours Books, 2022. Original title: La casa de los azulejos.',
         'Every tile on the front of the house had been painted by someone who was dead.', 'Cada azulejo de la fachada lo había pintado alguien que ya estaba muerto.',
         [['Original', '<em>La casa de los azulejos</em>, 2018'], ['Length', '71,000 words'], ['Publisher', 'Small Hours Books']], '2022-04-18', tag_pt='Original (Spanish)'),
    book('Street names in two scripts', 'notes', 'sign.jpg',
         'A note from a week in Macau, where every street sign is in Chinese and Portuguese and neither is a translation of the other.',
         'Avenida de Carlos da Maia keeps its Portuguese name in English. The Chinese name beside it sounds it out.', 'A Avenida de Carlos da Maia mantém o nome português em inglês. O nome chinês ao lado reproduz o som.',
         [['Written', 'For the ITI Bulletin, spring issue']], '2024-03-02'),
    book('The ij key on a Dutch typewriter', 'notes', 'typewriter.jpg',
         'I bought a typewriter at the Feira da Vandoma for €15 and it turned out to be Dutch. It has a key for the letter ij and a florin sign.',
         'One key, one letter, two strokes. Portuguese has nothing like it, which is probably why the seller let it go.', 'Uma tecla, uma letra, dois traços. O português não tem nada parecido.',
         [['Where', 'Feira da Vandoma, Porto, Saturday mornings']], '2023-06-10'),
    book('A word list copied by hand', 'notes', 'dictionary.jpg',
         'Notes on a Persian word list in the British Library, and why bilingual glossaries are still written by hand in my notebooks.',
         'Every long job starts with a glossary. For Cork Oak Country it ran to 300 entries, and the author and I argued about eleven of them.', 'Todos os trabalhos longos começam com um glossário.',
         [['Tool', 'A spreadsheet, then a notebook, then the spreadsheet again']], '2023-01-15'),
]

content = {
    'site': {'title': 'Joanna Pryce', 'tagline': 'Translator, Portuguese and Spanish into English'},
    'categories': [{'slug': 'books', 'name': 'Books'}, {'slug': 'academic', 'name': 'Academic'},
                   {'slug': 'exhibitions', 'name': 'Exhibitions'}, {'slug': 'notes', 'name': 'Notes'}],
    'front_page': 'home', 'posts_page': 'translations',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'translations', 'title': 'Translations', 'content': ''},
        {'slug': 'services', 'title': 'Services and rates', 'pattern': 'lingua/services-page'},
        {'slug': 'examples', 'title': 'Examples', 'pattern': 'lingua/examples-page', 'template': 'page-wide'},
        {'slug': 'credentials', 'title': 'Credentials', 'pattern': 'lingua/credentials-page', 'template': 'page-wide'},
        {'slug': 'faq', 'title': 'Questions', 'pattern': 'lingua/faq-page'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'lingua/contact-page', 'template': 'page-wide'},
        {'slug': 'portugues', 'title': 'Em português', 'pattern': 'lingua/portugues-page'},
    ],
    'posts': POSTS,
    'nav': [{'label': 'Translations', 'url': '/translations/'}, {'label': 'Services', 'url': '/services/'}, {'label': 'Examples', 'url': '/examples/'},
            {'label': 'Credentials', 'url': '/credentials/'}, {'label': 'Questions', 'url': '/faq/'}, {'label': 'Contact', 'url': '/contact/'},
            ],
}
os.makedirs('demos/lingua', exist_ok=True)
with open('demos/lingua/content.json', 'w') as f:
    json.dump(content, f, indent=1, ensure_ascii=False)
with open('demos/lingua/readme-extra.md', 'w') as f:
    f.write('''Lingua sets important text twice, source and target side by side, with a hairline between the columns and the second language in italic. Use the "Parallel text" style on any Columns block to get the same look.

Published translations are posts in the categories Books, Academic, Exhibitions and Notes. The posts page lists them as a bibliography with a small cover image, so set a featured image and write the author, publisher and year in the excerpt. Page patterns cover services and rates, examples, credentials, questions, contact and a page in the second language.''')
print('demo written')
