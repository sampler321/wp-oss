# Design note (ink, idea 001, illustrator portfolio and shop; round 2)
# Direction: a plain, fast illustrator's site where the drawings do the talking, like ellensurrey.com and zosiapaszkiet.com:
#   a small name line, then straight into a masonry wall of work that opens in the core lightbox, with shop, originals
#   and commissions one click away. Prices live on the shop, art-for-sale and commissions pages, never on the home page.
# Fonts: Bricolage Grotesque only (800 for headings, 400 for text). Palette: paper white, ballpen black, correction red
#   for links and prices, sketchbook grey-beige surface, pencil-line rules.
# Layout idea: captions sit under every picture (client, year, link to the project) and data is set as hairline
#   "spec rows" made from groups, so tables are kept for the two places that are really tabular (postage, price list).
import sys, json, os, shutil
sys.path.insert(0, 'tools/lib')
import blocks
from blocks import *
set_theme('ink')
S_ = THEME['slug']
D = THEME['dir']
for sub in ('patterns', 'templates', 'parts', os.path.join('styles', 'sections')):
    shutil.rmtree(os.path.join(D, sub), ignore_errors=True)

P = lambda s: 'var:preset|spacing|%s' % s
pad = lambda t, b=None: {'spacing': {'padding': {'top': P(t), 'bottom': P(b if b is not None else t)}}}
U = lambda f: '/wp-content/themes/ink/assets/images/' + f
SRC = lambda f, pm=True: f if pm else U(f)


def jdump(rel, data):
    write(rel, json.dumps(data, indent='\t', ensure_ascii=False))


_image = image
def image(filename, alt, caption='', **kw):
    """blocks.image plus the inline aspect-ratio/object-fit style core saves."""
    out = _image(filename, alt, caption, **kw)
    if kw.get('aspectRatio'):
        st = 'aspect-ratio:%s' % kw['aspectRatio'] + (';object-fit:%s' % kw['scale'] if kw.get('scale') else '')
        out = out.replace('<img ', '<img style="%s" ' % st, 1)
    return out


def gal(imgs, cols=3, crop=True, pm=True, **attrs):
    """Gallery of lightboxed images. imgs: (file, alt, caption)."""
    a = {'columns': cols, 'linkTo': 'none', **attrs}
    if not crop:
        a['imageCrop'] = False
    inner = '\n\n'.join(image(SRC(f, pm), alt, cap) for f, alt, cap in imgs)
    cls = 'wp-block-gallery has-nested-images columns-%d%s' % (cols, ' is-cropped' if crop else '')
    return '<!-- wp:gallery%s -->\n<figure class="%s">%s</figure>\n<!-- /wp:gallery -->' % (blocks._a(a), blocks._cls(cls, a), inner)


def vstack(inner, **kw):
    return group(inner, layout={'type': 'flex', 'orientation': 'vertical', 'justifyContent': 'stretch'}, **kw)


def gridn(inner, n, min_width='12rem', **kw):
    return group(inner, layout={'type': 'grid', 'columnCount': n, 'minimumColumnWidth': min_width}, **kw)


def spec(rows, **kw):
    """Definition-style rows made from groups: label left, value right, hairline under each."""
    return vstack(J(*[row(J(para(k, textColor='muted', fontSize='small'), para(v, fontSize='small')),
                         justify='space-between', className='is-style-hairline') for k, v in rows]),
                 style={'spacing': {'blockGap': '0'}}, **kw)


def head_row(title, link_text=None, href=None, level=2, size='x-large'):
    items = [heading(title, level, fontSize=size)]
    if link_text:
        items.append(para('<a href="%s">%s</a>' % (href, link_text), fontSize='small'))
    return row(J(*items), justify='space-between', align='wide', style={'spacing': {'margin': {'bottom': P(40)}}})


def section(inner, top=60, bottom=0, cls=None, **kw):
    sp = lambda v: P(v) if v else '0'
    a = dict(align='wide', layout={'type': 'default'}, style={'spacing': {'padding': {'top': sp(top), 'bottom': sp(bottom)}}})
    if cls:
        a['className'] = cls
    a.update(kw)
    return group(inner, **a)


# ------------------------------------------------------------------ images and works
A = {
    'hero.jpg': 'Two blue birds on a thin branch, painted in blue and rust on cream paper',
    'work-7.jpg': 'A barred owl with spread wings on a branch, a grey squirrel below it',
    'work-8.jpg': 'Jellyfish in blue, orange and red with long trailing tentacles',
    'work-9.jpg': 'A black crow on a branch of white blossom against a dark olive ground',
    'work-12.jpg': 'Hummingbirds in green, red and blue feeding around a nest among leaves',
    'work-3.jpg': 'A white heron standing in reeds at the edge of a marsh',
    'work-6.jpg': 'A red mountain against a blue sky with rows of white clouds',
    'work-1.jpg': 'A dense botanical chart of medicinal plants with small labels',
    'map-1.jpg': "A bird's-eye view of a city and its harbour, drawn in green and grey",
    'work-11.jpg': 'A puffin with an orange beak standing beside a burrow on a grassy cliff',
    'work-13.jpg': 'A long-tailed bird on a plum branch against a pale pink sky',
    'work-16.jpg': 'A crowded plate of orchids in pink, white and yellow',
    'work-4.jpg': 'A yellow radiolarian drawn as a spiky star with fine hatching',
    'work-5.jpg': 'Two ducks in snow, painted in soft grey washes across an open book',
    'work-14.jpg': 'Blue waves curling over long wooden boats',
    'work-2.jpg': 'Engraving of camels, elephants and other animals gathered in a rocky landscape',
    'prints.jpg': 'Woodblock print of a snowy street and canal under a pale sky',
    'work-10.jpg': 'A tall white flower spike rising from long green leaves',
    'work-15.jpg': 'Three blue jays on a flowering branch',
    'sketch-1.jpg': 'A page of ink sketches of men climbing a rope and wrestling',
    'sketch-2.jpg': 'Faint pencil lines of a figure study on old paper',
    'studio.jpg': 'A cluttered studio with a stove, plaster casts and a workbench',
}

# slug, title, category, image, client, used for, year, medium, tags
WORKS = [
    ('bluebirds-for-garden-letters', 'Bluebirds for Garden Letters', 'editorial', 'hero.jpg', 'Garden Letters magazine', 'Spring issue cover', '2025', 'Gouache, finished digitally', ['Birds', 'Cover']),
    ('barred-owl-the-night-walk', 'Barred owl, cover for The Night Walk', 'books', 'work-7.jpg', 'Little Toller Books', 'Hardback cover and endpapers', '2025', 'Gouache and pencil', ['Birds', 'Book cover']),
    ('jellyfish-aquarium-lates', 'Jellyfish, poster for Aquarium Lates', 'posters', 'work-8.jpg', 'Bristol Aquarium', 'Poster series for late openings', '2025', 'Ink and gouache, printed in four spot colours', ['Poster', 'Sea']),
    ('crow-and-blossom-kinoko-tea', 'Crow and blossom, tea tins for Kinoko', 'packaging', 'work-9.jpg', 'Kinoko Tea, Stokes Croft', 'Tin wrap for a spring green tea', '2025', 'Gouache on toned paper', ['Birds', 'Packaging']),
    ('hummingbirds-six-plates', 'Hummingbirds, a series of six plates', 'editorial', 'work-12.jpg', 'The Guardian Saturday', 'Six plates for a nature supplement', '2024', 'Gouache, scanned at 600dpi', ['Birds', 'Series']),
    ('totterdown-from-the-air', 'Totterdown from the air, a house map', 'maps', 'map-1.jpg', 'Priya and Sam, private commission', 'A map of their street and the view from it', '2025', 'Pen, ink and watercolour, 50 x 70 cm', ['Map', 'Commission']),
    ('heron-at-low-tide', 'Heron at low tide', 'editorial', 'work-3.jpg', 'Garden Letters magazine', 'Feature on the Severn estuary', '2024', 'Gouache, drawn on location', ['Birds', 'Editorial']),
    ('red-mountain-book-cover', 'Red mountain, book cover', 'books', 'work-6.jpg', 'Harbour Press', 'Cover for a travel memoir', '2024', 'Gouache and coloured pencil', ['Book cover']),
    ('puffin-wild-bird-trust', 'Puffin for the Wild Bird Trust', 'editorial', 'work-11.jpg', 'Wild Bird Trust', 'Members magazine and a fundraising print', '2024', 'Gouache', ['Birds', 'Charity']),
    ('plum-branch-harbourside-market', 'Plum branch, poster for Harbourside Market', 'posters', 'work-13.jpg', 'Harbourside Market', 'Spring market poster', '2024', 'Screenprint in three colours, edition of 80', ['Poster', 'Birds']),
    ('orchid-wallpaper-ostra', 'Orchid wallpaper for Ostra, Clifton', 'packaging', 'work-16.jpg', 'Ostra restaurant', 'Wallpaper for the back room and the menus', '2023', 'Gouache, repeated as a half-drop pattern', ['Pattern', 'Interiors']),
    ('medicinal-plants-chart', 'Medicinal plants chart', 'packaging', 'work-1.jpg', 'Hedgerow Apothecary', 'Tea box wrap', '2023', 'Pen and gouache, 42 plants', ['Packaging', 'Plants']),
    ('radiolarian-science-festival', 'Radiolarian, science festival poster', 'posters', 'work-4.jpg', 'Bristol Science Festival', 'Festival poster', '2023', 'Pencil and gouache, printed in yellow and black', ['Poster', 'Science']),
    ('two-ducks-picture-book', 'Two ducks, spread for a picture book', 'books', 'work-5.jpg', 'Puddle Books', 'Picture book, The Pond in Winter', '2023', 'Gouache, painted at 120% of print size', ['Picture book', 'Birds']),
    ('ocean-waves-surf-shop-mural', 'Ocean waves, mural for a surf shop', 'posters', 'work-14.jpg', 'Saltwater Surf, Weston', 'A 6 metre wall behind the till', '2022', 'Exterior paint over a projected pencil drawing', ['Mural']),
    ('eucomis-seed-packet', 'Eucomis, seed packet', 'packaging', 'work-10.jpg', 'Bramble Seeds', 'Seed packet front, one of twelve', '2022', 'Gouache', ['Packaging', 'Plants']),
    ('animal-parade-mural-study', 'Animal parade, mural study', 'posters', 'work-2.jpg', 'St Werburgh\'s Primary', 'Study for a school hall mural', '2022', 'Pencil on layout paper', ['Mural', 'Study']),
    ('snowy-street-winter-poster', 'Snowy street, winter poster', 'posters', 'prints.jpg', 'Harbourside Market', 'Christmas market poster', '2021', 'Two-colour screenprint, edition of 60', ['Poster']),
]
W = {w[0]: w for w in WORKS}
link = lambda slug: '/%s/' % slug


def cap_for(slug, short=None):
    w = W[slug]
    return '<a href="%s">%s</a>, %s' % (link(slug), short or w[1], w[6])


# ------------------------------------------------------------------ portfolio patterns
MASONRY = [('plum-branch-harbourside-market', 'Plum branch'), ('puffin-wild-bird-trust', 'Puffin'), ('orchid-wallpaper-ostra', 'Orchid wallpaper'),
           ('red-mountain-book-cover', 'Red mountain'), ('heron-at-low-tide', 'Heron at low tide'), ('eucomis-seed-packet', 'Eucomis'),
           ('radiolarian-science-festival', 'Radiolarian'), ('two-ducks-picture-book', 'Two ducks'), ('medicinal-plants-chart', 'Medicinal plants'),
           ('ocean-waves-surf-shop-mural', 'Ocean waves'), ('snowy-street-winter-poster', 'Snowy street'), ('animal-parade-mural-study', 'Animal parade')]


def masonry(items, pm=True):
    return group(J(*[image(SRC(W[s][3], pm), A[W[s][3]], cap_for(s, t)) for s, t in items]),
                 align='wide', className='is-style-masonry', layout={'type': 'default'})


pattern('home-intro', 'Intro: name, one fact and where to go next', 'featured,text', group(columns(
    ('55%', heading('Illustration by Joon Park', 1, fontSize='xx-large')),
    (None, J(para('Gouache and pencil from a desk on Jamaica Street, Bristol. Editorial, books, packaging and the odd pub sign since 2014. Click any drawing to see it large.'),
             row(J(para('<a href="/shop/">Prints and books</a>', fontSize='small'), para('<a href="/art-for-sale/">Originals for sale</a>', fontSize='small'),
                   para('<a href="/commissions/">Commissions, open until 31 October</a>', fontSize='small')), style={'spacing': {'blockGap': P(40)}}))),
    align='wide', verticalAlignment='bottom'), align='wide', layout={'type': 'default'}, style=pad(50, 40)),
    description='A short opening for the home page: a name, one fact about the work and three links. Keep it small so the drawings show on the first screen.')

pattern('portfolio-masonry', 'Portfolio: masonry wall with lightbox', 'portfolio,gallery', J(
    masonry(MASONRY)), keywords='work, portfolio, masonry, lightbox',
    description='Hand-picked drawings in a ragged masonry wall. Each opens large in the lightbox; the caption links to the project.')

pattern('portfolio-even-grid', 'Portfolio: even grid of squares', 'portfolio,gallery', section(J(
    head_row('Posters', 'All posters', '/category/posters/'),
    gal([(W[s][3], A[W[s][3]], '') for s in ['jellyfish-aquarium-lates', 'plum-branch-harbourside-market', 'radiolarian-science-festival', 'snowy-street-winter-poster',
                                             'ocean-waves-surf-shop-mural', 'animal-parade-mural-study', 'hummingbirds-six-plates', 'orchid-wallpaper-ostra']], cols=4, align='wide')), top=0))

pattern('portfolio-large-column', 'Portfolio: one column, large', 'portfolio', group(J(
    *[image(W[s][3], A[W[s][3]], cap_for(s)) for s in ['barred-owl-the-night-walk', 'totterdown-from-the-air', 'hummingbirds-six-plates', 'crow-and-blossom-kinoko-tea']]),
    layout={'type': 'constrained', 'contentSize': '880px'}, style={'spacing': {'blockGap': P(60)}}),
    description='One drawing after another at a size you can read, the way Tom Gauld lays out his portfolio.')

pattern('portfolio-two-up', 'Portfolio: two large side by side', 'portfolio', columns(
    (None, image('work-9.jpg', A['work-9.jpg'], cap_for('crow-and-blossom-kinoko-tea'))),
    (None, image('work-13.jpg', A['work-13.jpg'], cap_for('plum-branch-harbourside-market'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(40)}}}))

pattern('recent-work', 'Recent pieces (latest posts)', 'portfolio,query', section(J(
    head_row('Recent pieces', 'Everything, by category', '/work/'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='4/5', scale='cover'),
            dyn('post-title', isLink=True, level=3, fontSize='medium'),
            dyn('post-terms', term='category', separator=', ')),
          per_page=6, layout={'type': 'grid', 'columnCount': 3}, align='wide')), top=70), keywords='latest, recent, work')

pattern('work-grid-archive', 'Work archive (masonry, follows the page query)', 'portfolio,query', inherit_query(
    J(dyn('post-featured-image', isLink=True), dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-terms', term='category', separator=', ')),
    align='wide', template_class='is-style-masonry'), inserter=False)

pattern('category-links', 'Work categories, as a row of links', 'portfolio', row(J(
    para('<a href="/work/">All work</a>', fontSize='small'),
    dyn('categories', className='is-style-inline-list', showEmpty=False)), align='wide', style={'spacing': {'blockGap': P(40)}}))

pattern('featured-work', 'One piece, large, with its details', 'portfolio', columns(
    ('62%', image('work-7.jpg', A['work-7.jpg'])),
    (None, J(heading('Barred owl', 2, fontSize='x-large'),
             para('The cover and endpapers for <em>The Night Walk</em>, a book about walking the Mendips after dark. The owl took eleven roughs. The squirrel took one.'),
             spec([('Client', 'Little Toller Books'), ('Used for', 'Hardback cover'), ('Year', '2025'), ('Medium', 'Gouache and pencil')]),
             para('<a href="/barred-owl-the-night-walk/">Roughs and the finished book</a>', fontSize='small'))),
    align='wide', verticalAlignment='bottom', style={'spacing': {'blockGap': {'left': P(60)}}}))


def work_caption(slug, pm=True):
    w = W[slug]
    return spec([('Client', w[4]), ('Used for', w[5]), ('Year', w[6]), ('Medium', w[7])])


pattern('work-caption', 'Work details (client, use, year, medium)', 'portfolio', work_caption('bluebirds-for-garden-letters'),
        description='Set as hairline rows, not a table. Put it beside or under a drawing.')


def series_plates(title, intro, imgs, pm=True):
    return J(heading(title, 2, fontSize='x-large'), para(intro),
             gal(imgs, cols=3, crop=False, pm=pm, align='wide'))


PLATES = [('work-12.jpg', A['work-12.jpg'], 'Plate 1, the nest'), ('work-15.jpg', A['work-15.jpg'], 'Plate 2, blue jays for scale'),
          ('hero.jpg', A['hero.jpg'], 'Plate 3, bluebirds'), ('work-13.jpg', A['work-13.jpg'], 'Plate 4, long tail'),
          ('work-11.jpg', A['work-11.jpg'], 'Plate 5, the odd one out'), ('work-7.jpg', A['work-7.jpg'], 'Plate 6, night')]
pattern('series-plates', 'Series: a set of plates with captions', 'portfolio,gallery', series_plates(
    'Six plates', 'A series is easier to judge together. Each plate opens large; the caption says what it was for.', PLATES))


def project_brief(brief, did):
    return columns((None, J(heading('The brief', 3, fontSize='large'), para(brief))),
                   (None, J(heading('What I did', 3, fontSize='large'), para(did))), align='wide', className='is-style-rule-top')


pattern('project-brief', 'Project: the brief and what I did', 'portfolio', project_brief(
    'Garden Letters wanted a spring cover that felt like the first warm Saturday. Two birds, lots of air, room for the masthead at the top.',
    'Four pencil roughs, one colour study in blue and rust, then the final in gouache at A3. The magazine chose the second rough; I still prefer the fourth.'))


def project_result(quote_text, who, result, credits):
    return columns(('55%', quote(quote_text, who)),
                   (None, J(heading('What happened next', 3, fontSize='large'), para(result), spec(credits))),
                   align='wide', style={'spacing': {'blockGap': {'left': P(60)}}})


pattern('project-result', 'Project: result, client quote and credits', 'portfolio,testimonials', project_result(
    'The cover sold out in the shops in nine days. People wrote in asking for the birds as a print, so we let Joon sell one.',
    'Tomasz Nowak, art editor, Garden Letters',
    'The magazine printed 400 extra copies. The print is now the best seller in the shop, which I did not see coming.',
    [('Art direction', 'Tomasz Nowak'), ('Printed by', 'Park Lane Press, Bristol'), ('Print edition', 'A3, 150 copies')]))


def process_strip(imgs, pm=True):
    return J(heading('From rough to final', 3, fontSize='large'), gal(imgs, cols=3, crop=False, pm=pm, align='wide'))


pattern('process-strip', 'Process: rough, colour study, final', 'portfolio,gallery', process_strip([
    ('sketch-2.jpg', A['sketch-2.jpg'], 'Pencil rough, the size of a stamp'), ('work-15.jpg', A['work-15.jpg'], 'Colour study'), ('hero.jpg', A['hero.jpg'], 'Final')]))

pattern('sketchbook-strip', 'Sketchbook strip', 'portfolio,gallery', section(J(
    head_row('From the sketchbook', 'More pages', '/sketchbook/', size='large'),
    gal([('sketch-1.jpg', A['sketch-1.jpg'], ''), ('sketch-2.jpg', A['sketch-2.jpg'], ''), ('work-4.jpg', A['work-4.jpg'], ''),
         ('work-5.jpg', A['work-5.jpg'], ''), ('studio.jpg', A['studio.jpg'], '')], cols=5, align='wide')), top=70),
    description='Five small pages from the sketchbook in a row. They open large in the lightbox.')


def detail_crops(main, d1, d2, pm=True):
    return columns(('62%', image(SRC(main[0], pm), main[1], main[2])),
                   (None, J(image(SRC(d1[0], pm), d1[1], d1[2], aspectRatio='1', scale='cover'),
                            image(SRC(d2[0], pm), d2[1], d2[2], aspectRatio='1', scale='cover'))), align='wide')


pattern('detail-crops', 'One drawing with two details', 'portfolio', detail_crops(
    ('work-12.jpg', A['work-12.jpg'], 'The whole plate'), ('work-15.jpg', A['work-15.jpg'], 'Detail, feathers'), ('work-11.jpg', A['work-11.jpg'], 'Detail, the nest')))

# ------------------------------------------------------------------ shop
pattern('shop-entry-points', 'Shop, originals and commissions (three ways in)', 'shop,call-to-action', section(J(
    columns(
        (None, J(image('prints.jpg', A['prints.jpg'], href='/shop/', aspectRatio='4/3', scale='cover'), heading('<a href="/shop/">Prints and books</a>', 3, fontSize='large'),
                 para('A4 and A3 giclee prints on cotton rag, two zines and one proper hardback. Posted within three working days.', fontSize='small'))),
        (None, J(image('work-9.jpg', A['work-9.jpg'], href='/art-for-sale/', aspectRatio='4/3', scale='cover'), heading('<a href="/art-for-sale/">Originals for sale</a>', 3, fontSize='large'),
                 para('The actual painted sheets. One of each, sold by email, some already reserved.', fontSize='small'))),
        (None, J(image('work-15.jpg', A['work-15.jpg'], href='/commissions/', aspectRatio='4/3', scale='cover'), heading('<a href="/commissions/">Commissions</a>', 3, fontSize='large'),
                 para('House portraits, maps of your street and birds for people who love one bird in particular.', fontSize='small'))),
        align='wide', style={'spacing': {'blockGap': {'left': P(40)}}})), top=70, cls='is-style-rule-top'))

PRODUCTS = [('prints.jpg', 'Snowy street', 'A3 print', '£38', ''), ('work-7.jpg', 'Barred owl', 'A3 print', '£38', 'Three left'),
            ('hero.jpg', 'Bluebirds', 'A4 print', '£28', ''), ('work-1.jpg', 'Medicinal plants', 'A3 print', '£38', 'Sold out')]


def product_card(img, title, fmt, price, flag):
    parts = [image(img, A[img], href='/shop/', aspectRatio='4/5', scale='cover'),
             heading('<a href="/shop/">%s</a>' % title, 3, fontSize='medium'),
             row(J(para('%s, %s' % (fmt, price), fontSize='small', className='is-style-price-tag'),
                   para(flag, className='is-style-tag') if flag else ''), style={'spacing': {'blockGap': P(20)}})]
    return stack(J(*parts), style={'spacing': {'blockGap': P(20)}})


pattern('shop-highlights', 'Shop highlights (four prints)', 'shop', section(J(
    head_row('In the shop', 'All prints and books', '/shop/'),
    gridn(J(*[product_card(*p) for p in PRODUCTS]), 4, '13rem', align='wide')), top=0),
    description='Four print cards with format, price and an honest sold out or low stock label.')

pattern('print-detail', 'Print detail', 'shop', columns(
    ('55%', image('work-7.jpg', A['work-7.jpg'], 'Click to see it large. The print has a 2 cm white border not shown here.')),
    (None, J(heading('Barred owl, A3 print', 2, fontSize='x-large'),
             para('£38, postage included in the UK', className='is-style-price-tag', fontSize='medium'),
             para('The owl from <em>The Night Walk</em> cover, printed from a 600dpi scan of the painting. The colours are checked against the original under daylight.'),
             spec([('Size', 'A3, 29.7 x 42 cm'), ('Paper', '300gsm Hahnemuhle cotton rag'), ('Edition', 'Open, signed on the back'), ('Ships', 'Rolled in a tube, within three working days')]),
             buttons(('Buy in the shop', '/shop/')))),
    align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('print-scale', 'Print shown at scale', 'shop', columns(
    (None, image('prints.jpg', A['prints.jpg'])),
    (None, J(heading('How big is an A3 print?', 3, fontSize='large'),
             para('A3 is 29.7 x 42 cm, about the size of two sheets of printer paper side by side. A4 is one sheet. Both are printed on 300gsm cotton rag with a 2 cm white border for framing.'),
             para('A3 prints ship rolled in a tube. A4 prints ship flat between boards.', fontSize='small'))), align='wide', verticalAlignment='center'))

ORIGINALS = [('hero.jpg', 'Bluebirds on a thin branch', 'Gouache on Arches, 21 x 28 cm on a 30 x 40 cm sheet', '£420'),
             ('work-2.jpg', 'Animal parade, study', 'Pencil and correction fluid, 30 x 40 cm', 'Reserved'),
             ('work-3.jpg', 'Heron, low tide', 'Gouache, 24 x 32 cm on a 30 x 40 cm sheet', '£380'),
             ('work-10.jpg', 'Eucomis', 'Gouache, 18 x 24 cm', '£240'),
             ('work-9.jpg', 'Crow and blossom', 'Gouache on toned paper, 28 x 38 cm', '£460'),
             ('work-4.jpg', 'Radiolarian', 'Pencil and gouache, 25 x 25 cm', 'Sold')]


def original_card(img, title, med, price):
    tag = para(price, className='is-style-tag') if price in ('Reserved', 'Sold') else para(price, className='is-style-price-tag', fontSize='medium')
    return stack(J(image(img, A[img]), heading(title, 3, fontSize='medium'), para(med, fontSize='x-small', textColor='muted'), tag),
                 style={'spacing': {'blockGap': P(20)}})


pattern('originals-grid', 'Originals for sale: cards with medium, size and price', 'shop,portfolio', gridn(
    J(*[original_card(*o) for o in ORIGINALS]), 3, '16rem', align='wide', style={'spacing': {'blockGap': P(50)}}),
    description='The signature: every original with medium, drawing and sheet size, one flat price, or reserved.')

pattern('originals-list', 'Originals for sale: short list', 'shop', J(
    vstack(J(*[row(J(para('<strong>%s</strong>' % t), para(m, fontSize='small', textColor='muted'), para(p, className='is-style-price-tag' if p[0] == '£' else 'is-style-tag')),
                  justify='space-between', className='is-style-hairline') for _, t, m, p in ORIGINALS[:4]]), style={'spacing': {'blockGap': '0'}}),
    para('<a href="/art-for-sale/">All originals, and how to buy one</a>', fontSize='small')))

pattern('how-to-buy-original', 'How to buy an original', 'shop,text', group(J(
    heading('How to buy an original', 3, fontSize='large'),
    lst(['Email <a href="mailto:hello@example.com">hello@example.com</a> with the title and your postal address.',
         'I reply within two working days with a payment link. I hold the drawing for you for a week.',
         'Once paid, it is mounted, wrapped flat between boards and posted with tracking.',
         'It arrives within 21 days. Outside the UK, add the postage below.'], ordered=True)),
    className='is-style-sketchbook', layout={'type': 'default'}))

pattern('postage-by-region', 'Postage by region (table)', 'shop', J(
    heading('Postage', 3, fontSize='large'),
    table([['UK', 'Included', '2 to 4 working days'], ['EU', '£9', '5 to 10 working days'], ['USA and Canada', '£14', '7 to 14 working days'], ['Rest of the world', '£18', '10 to 21 working days']],
          head=['Where', 'Prints', 'Usually takes']),
    para('Prints ship rolled in a tube. Originals and A4 prints ship flat between boards. Import duties outside the UK are yours to pay, sorry.', fontSize='small')))

pattern('shipping-note', 'Shipping and returns, one paragraph', 'shop,text', group(para(
    'Prints ship within three working days in a tube or between boards, tracked. If a print arrives damaged, send me a photo within 14 days and I\'ll send another. Originals can\'t be returned, so ask me for more photos before you buy.', fontSize='small'),
    className='is-style-rule-top', layout={'type': 'default'}))

pattern('shop-categories', 'Shop: prints and publications', 'shop', columns(
    (None, group(J(heading('<a href="/shop/">Prints</a>', 3, fontSize='large'), para('Giclee prints on cotton rag. A4 from £28, A3 from £38. Signed on the back in pencil.', fontSize='small')), className='is-style-sketchbook')),
    (None, group(J(heading('<a href="/shop/">Publications</a>', 3, fontSize='large'), para('Two risograph zines, a colouring book of Bristol pubs and <em>Birds of the Avon</em>, signed if you ask.', fontSize='small')), className='is-style-sketchbook')),
    align='wide'))

BOOKS = [('work-7.jpg', '<em>The Night Walk</em>', 'Little Toller Books, 2025. Cover and 12 drawings.', 'https://example.com/night-walk', 'From the publisher'),
         ('hero.jpg', '<em>Birds of the Avon</em>', 'Little Toller Books, 2023. 96 pages, written and drawn by me.', '/shop/', 'Signed, in the shop'),
         ('work-5.jpg', '<em>The Pond in Winter</em>', 'Puddle Books, 2023. Picture book, words by Mari Evans.', 'https://example.com/pond', 'From the publisher'),
         ('map-1.jpg', '<em>Small Maps</em>', 'Self-published zine, 2021. 24 pages, risograph.', '/shop/', 'In the shop')]
pattern('books-list', 'Books, with covers and where to buy', 'shop,about', J(
    heading('Books', 2, fontSize='x-large'),
    gridn(J(*[stack(J(image(i, A[i], aspectRatio='3/4', scale='cover'), heading(t, 3, fontSize='medium'), para(d, fontSize='small'), para('<a href="%s">%s</a>' % (h, l), fontSize='small')),
                   style={'spacing': {'blockGap': P(20)}}) for i, t, d, h, l in BOOKS]), 4, '11rem', align='wide')))

pattern('notice-christmas-cutoff', 'Notice: Christmas posting dates', 'banner', group(
    para('Order by <strong>15 December</strong> for UK Christmas delivery, <strong>8 December</strong> for the EU and <strong>1 December</strong> for everywhere else.'),
    className='is-style-red-notice', align='full', style=pad(20), layout={'type': 'default'}),
    description='A notice bar for posting deadlines. Edit the dates each year and remove it when they pass.')

# ------------------------------------------------------------------ commissions
pattern('commissions-status', 'Commissions open (with dates)', 'commissions,call-to-action', group(columns(
    (None, J(heading('Commissions are open until 31 October', 2, fontSize='x-large'),
             para('After that I am drawing a book and won\'t take new work until March. Bird portraits, house portraits and maps of your street.'))),
    ('30%', buttons(('Ask about a commission', '/commissions/'))), align='wide', verticalAlignment='center'),
    className='is-style-sketchbook', align='wide', layout={'type': 'default'}),
    description='Swap for the closed version when you stop taking work.')

pattern('commissions-closed', 'Commissions closed (waiting list)', 'commissions,call-to-action', group(J(
    heading('Commissions are closed until March', 2, fontSize='x-large'),
    para('I\'m drawing a book this winter. To be first in line when I reopen, email me with "waiting list" in the subject. No deposit needed.'),
    para('<a href="mailto:hello@example.com?subject=Waiting%20list">Join the waiting list</a>')),
    className='is-style-sketchbook', align='wide', layout={'type': 'default'}))

OPTIONS = [('work-15.jpg', 'A bird, or an animal', 'From £180', 'A4 print of a digital painting, or £320 for the painted original. Your bird, your dog, your neighbour\'s cat.'),
           ('studio.jpg', 'A house portrait', 'From £450', 'Painted original at A3, front elevation plus whatever is in the garden. Good as a moving-out present.'),
           ('map-1.jpg', 'A map', 'From £900', 'Your street, your wedding walk or your whole town. Delivered as print-ready files and one A2 print.')]
pattern('commission-options', 'Commission options (three cards with prices)', 'commissions,services', gridn(J(
    *[stack(J(image(i, A[i], aspectRatio='4/3', scale='cover'), heading(t, 3, fontSize='large'), para(p, className='is-style-price-tag', fontSize='medium'), para(d, fontSize='small')),
            style={'spacing': {'blockGap': P(20)}}) for i, t, p, d in OPTIONS]), 3, '15rem', align='wide'))

pattern('commission-price-list', 'Commission price list (table)', 'commissions', J(
    heading('Price list', 3, fontSize='large'),
    table([['Single bird or animal', 'Digital, A4 print', '£180'], ['Single bird or animal', 'Painted original, A4', '£320'],
           ['House portrait', 'Painted original, A3', '£450 to £600'], ['Illustrated map', 'Print-ready files and one A2 print', 'From £900'],
           ['Wedding or event stationery', 'Files for invitations and a menu', 'From £650']], head=['What', 'Format', 'Price']),
    para('Prices include one framed-size print and postage in the UK. Commercial use is quoted separately.', fontSize='small')),
    description='A printable price list for the commissions page.')

STEPS = [('1. Tell me what you want', 'Email or fill in the form: what, how big and by when. Phone photos are fine.'),
         ('2. Contract and deposit', 'A one-page contract. A 40% deposit books your slot in the calendar.'),
         ('3. Sketch and colour study', 'You get a pencil sketch and a colour study. Two rounds of changes are included.'),
         ('4. Final', 'I paint the final. You pay the balance, then it ships or the files arrive.')]
pattern('commission-steps', 'Commission steps (four columns)', 'commissions', section(J(
    heading('How a commission works', 2, fontSize='x-large'),
    columns(*[(None, J(heading(t, 3, fontSize='medium'), para(d, fontSize='small'))) for t, d in STEPS], align='wide', className='is-style-rule-top')), top=0))

pattern('commission-process', 'Commission process (short list)', 'commissions,text', J(
    heading('The short version', 3, fontSize='large'),
    lst(['Fill in the form or email me.', 'Sign the contract and pay a 40% deposit.', 'Approve a sketch and a colour study.', 'Pay the balance when the final is done.'], ordered=True)))

pattern('commission-faq', 'Commission FAQ', 'commissions,text', J(
    heading('Questions people ask', 3, fontSize='large'),
    details('How long does it take?', para('Three to five weeks from deposit to delivery. Christmas slots fill by mid-October.')),
    details('Can I send reference photos?', para('Yes, please. Phone photos are fine. Several angles help more than one perfect shot.')),
    details('Who owns the copyright?', para('I keep the copyright. You get the original or print to keep, and a licence for personal use. Commercial use is quoted separately.')),
    details('Can you draw my dog?', para('Yes, but I draw dogs the same way I draw birds: slightly stern and very still.'))))

pattern('commission-terms', 'Commission terms (plain words)', 'commissions,text', J(
    heading('Terms, in plain words', 3, fontSize='large'),
    lst(['The 40% deposit is non-refundable once I start the sketch.',
         'Two rounds of changes are included at sketch stage. Changes after the final is painted cost extra.',
         'I keep the copyright and may show the work here unless you ask me not to.',
         'If I can\'t finish for any reason, I refund everything you\'ve paid.'])))

pattern('commission-past-work', 'Past commissions (gallery)', 'commissions,gallery', J(
    heading('Some commissions from last year', 3, fontSize='large'),
    gal([('map-1.jpg', A['map-1.jpg'], '<a href="/totterdown-from-the-air/">Totterdown, for Priya and Sam</a>'),
         ('work-15.jpg', A['work-15.jpg'], 'Three blue jays, a 40th birthday'),
         ('work-10.jpg', A['work-10.jpg'], 'Eucomis, for a garden designer')], cols=3, crop=False, align='wide')))

# ------------------------------------------------------------------ about
pattern('about-bio', 'About: bio with picture', 'about', columns(
    ('40%', image('studio.jpg', A['studio.jpg'], 'Not my studio. Mine has fewer statues and more tea.')),
    (None, J(heading('Hello, I\'m Joon', 2, fontSize='x-large'),
             para('I\'m Joon Park, an illustrator in Bristol. I grew up in Busan, studied illustration at Falmouth and have drawn for magazines, publishers and one very patient pub company since 2014.'),
             para('I work in gouache and pencil at a desk that faces a wall on purpose. I don\'t use AI tools and I don\'t do logo design. I will draw your dog, but it will look slightly stern.'),
             para('Represented for editorial work by Northern Lights Agency. For everything else, email me directly.'))), align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('about-short', 'About: short intro with two buttons', 'about,call-to-action', columns(
    ('35%', image('work-5.jpg', A['work-5.jpg'])),
    (None, J(heading('I\'m Joon Park', 2, fontSize='x-large'),
             para('I draw birds, maps and the occasional pub sign, mostly in gouache, for magazines, publishers and people who want a drawing of their street.'),
             buttons(('About me', '/about/'), ('See the work', '/work/', {'className': 'is-style-outline'})))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('about-practical', 'About: practical information', 'about', columns(
    (None, J(heading('Practical information', 3, fontSize='large'),
             para('I paint in gouache on Arches hot-pressed paper, then scan at 600dpi and tidy up digitally. Files come as layered TIFFs in CMYK or RGB, whichever your printer asks for.'),
             para('Lead times are three weeks for a spot illustration and ten for a cover with roughs. I can turn an editorial piece around in four days if the brief is clear and nobody changes it on day three.'))),
    ('38%', image('work-10.jpg', A['work-10.jpg'])), align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

pattern('about-desk', 'About: what is on the desk', 'about,text', J(
    heading('On the desk', 3, fontSize='large'),
    lst(['Winsor and Newton designer gouache, mostly Prussian blue, burnt sienna and a white I buy by the big tube', 'Arches hot-pressed 300gsm, cut to A3',
         'A Caran d\'Ache Prismalo pencil in blue for roughs', 'A Pentel correction pen, which does more drawing than it should', 'An Epson scanner that is older than my nephew'])))

pattern('clients-list', 'Clients (text list)', 'about', J(
    heading('People I\'ve drawn for', 3, fontSize='large'),
    para('Garden Letters, The Guardian Saturday, Little Toller Books, Bristol Old Vic, Bristol Aquarium, Wild Bird Trust, Harbourside Market, Kinoko Tea, Ostra, Clifton Pub Company, Penguin Random House (one cover, very proud)', fontSize='large')))

EXHIBITIONS = [('2025', 'Paper Birds, group show', 'Spike Island, Bristol'), ('2024', 'Small Maps, solo', 'The Letterpress Room, Bath'),
               ('2023', 'Night Walk drawings', 'Little Toller shop, Beaminster'), ('2022', 'Illustrators\' Fair', 'Old Truman Brewery, London')]
pattern('exhibitions-list', 'Exhibitions', 'about,events', J(
    heading('Shown at', 3, fontSize='large'),
    vstack(J(*[row(J(para(y, textColor='muted', fontSize='small'), para('<strong>%s</strong>, %s' % (t, p))), className='is-style-hairline', style={'spacing': {'blockGap': P(40)}})
              for y, t, p in EXHIBITIONS]), style={'spacing': {'blockGap': '0'}})))

# ------------------------------------------------------------------ testimonials and press
pattern('testimonial', 'Testimonial with the drawing', 'testimonials', section(columns(
    ('30%', image('map-1.jpg', A['map-1.jpg'])),
    (None, J(quote('The map is on our kitchen wall and we still find new things in it. Joon put our cat in the window of number 14 and didn\'t tell us.',
                   'Priya and Sam, commissioned a map of Totterdown, 2025'),
             para('<a href="/totterdown-from-the-air/">How the map was made</a>', fontSize='small'))),
    align='wide', verticalAlignment='center', style={'spacing': {'blockGap': {'left': P(60)}}}), top=70))

pattern('press-quotes', 'Press quotes (named)', 'testimonials', columns(
    (None, quote('Joon draws birds like they owe him money.', 'Tomasz Nowak, art editor, Garden Letters, 2024')),
    (None, quote('The best cover we have printed in years, and the only one people asked to buy.', 'Ellie Gray, Little Toller Books, 2025')), align='wide'))

PRESS = [('Creative Review', 'Five illustrators drawing the natural world', '2025'), ('It\'s Nice That', 'Joon Park\'s birds are slightly stern', '2024'),
         ('Bristol Post', 'The man who paints the city from above', '2025'), ('Varoom', 'Interview: gouache, deadlines and one correction pen', '2023')]
pattern('press-list', 'Press: written about in', 'testimonials,text', J(
    heading('Written about in', 3, fontSize='large'),
    vstack(J(*[row(J(para('<strong>%s</strong>' % pub), para('<a href="https://example.com/">%s</a>' % h), para(y, textColor='muted', fontSize='small')),
                  justify='space-between', className='is-style-hairline') for pub, h, y in PRESS]), style={'spacing': {'blockGap': '0'}}),
    para('Press pictures and a short bio are on request: <a href="mailto:hello@example.com?subject=Press">hello@example.com</a>.', fontSize='small')))

# ------------------------------------------------------------------ events
EVENTS = [('Sat 1 November', 'Open studio', 'Jamaica Street Studios, Bristol', 'Drop in, 11am to 4pm'),
          ('Sat 8 November', 'Drawing birds in gouache, workshop', 'Spike Island, Bristol', '8 places, £65'),
          ('29 and 30 November', 'Bristol Illustration Fair', 'The Passenger Shed, Bristol', 'Table 32, prints and originals'),
          ('6 December', 'Christmas market', 'Harbourside, Bristol', 'Prints, zines and the colouring book')]
pattern('events-list', 'Events: fairs, markets and open studios', 'events', J(
    heading('Where to find me', 2, fontSize='x-large'),
    vstack(J(*[columns(('24%', para('<strong>%s</strong>' % d)), (None, J(para(t, fontSize='large'), para(p, fontSize='small', textColor='muted'))), ('28%', para(n, fontSize='small')),
                      className='is-style-hairline', isStackedOnMobile=True) for d, t, p, n in EVENTS]), style={'spacing': {'blockGap': '0'}})))

WORKSHOPS = [('work-3.jpg', 'Drawing birds in gouache', 'Saturday 8 November, 10am to 4pm, Spike Island', '£65 with paper and paint. 8 places.',
              'You paint one bird from a photograph and one from a stuffed specimen the museum lends us. Beginners welcome; bring a packed lunch.'),
             ('map-1.jpg', 'Draw a map of your street', 'Saturday 17 January, 10am to 1pm, online', '£30. 20 places.',
              'A morning on how I plan a map: walking it, what to leave out, and how to make a car park look nice. You finish with a pencil rough.')]
pattern('workshops', 'Workshops (cards with booking)', 'events,call-to-action', gridn(J(
    *[stack(J(image(i, A[i], aspectRatio='3/2', scale='cover'), heading(t, 3, fontSize='large'), para(w, fontSize='small'), para(p, className='is-style-price-tag'), para(d, fontSize='small'),
              buttons(('Book a place', 'mailto:hello@example.com?subject=Workshop'))), style={'spacing': {'blockGap': P(20)}}) for i, t, w, p, d in WORKSHOPS]),
    2, '18rem', align='wide', style={'spacing': {'blockGap': P(60)}}))

pattern('open-studio', 'Open studio (next date)', 'events,call-to-action', group(J(
    heading('Open studio, Saturday 1 November', 3, fontSize='large'),
    para('11am to 4pm at Unit 4, Jamaica Street Studios, Bristol BS2 8JP. Originals, seconds and the plan chest of roughs. Two flights of stairs, no lift, sorry.'),
    para('<a href="/events/">All dates</a>', fontSize='small')), className='is-style-sketchbook', layout={'type': 'default'}))

# ------------------------------------------------------------------ contact
pattern('contact-details', 'Contact details', 'contact', columns(
    (None, J(heading('Say hello', 2, fontSize='x-large'), para('Email is best: <a href="mailto:hello@example.com">hello@example.com</a>. I reply within two working days, not at weekends.'),
             para('For editorial work, contact Asha at Northern Lights Agency: <a href="mailto:asha@example.com">asha@example.com</a>.'))),
    (None, J(heading('Studio visits', 3, fontSize='large'), para('Open studio on the first Saturday of the month, 11am to 4pm. Unit 4, Jamaica Street Studios, Bristol BS2 8JP. Two flights of stairs, no lift, sorry.'))), align='wide'))

pattern('contact-big-email', 'Contact: big email line', 'contact', group(J(
    para('Write to me at', fontSize='small', textColor='muted'),
    para('<a href="mailto:hello@example.com">hello@example.com</a>', fontSize='xx-large', className='is-style-big-link'),
    para('Say what it is, how big and when you need it. I answer within two working days and I say no quickly if I\'m not the right person.'),
    social([('instagram', 'https://www.instagram.com/'), ('mail', 'mailto:hello@example.com')], className='is-style-logos-only')),
    align='wide', layout={'type': 'default'}))

pattern('contact-agent', 'Contact: agent card', 'contact', group(J(
    heading('Editorial and advertising', 3, fontSize='large'),
    para('Asha Mensah, Northern Lights Agency<br><a href="mailto:asha@example.com">asha@example.com</a><br>+44 20 7946 0321'),
    para('Asha handles fees and usage for magazines, advertising and anything with a media plan. Books, prints and private commissions come to me.', fontSize='small')),
    layout={'type': 'default'}))

pattern('contact-visit', 'Contact: visit the studio', 'contact', columns(
    ('45%', image('studio.jpg', A['studio.jpg'])),
    (None, J(heading('Visit the studio', 3, fontSize='large'),
             para('Unit 4, Jamaica Street Studios<br>37 Jamaica Street, Bristol BS2 8JP'),
             para('Open studio on the first Saturday of the month, 11am to 4pm. Other days by appointment. From Temple Meads it is a 20 minute walk or the number 72 bus to Stokes Croft.'),
             para('<a href="https://www.openstreetmap.org/">Open the map</a>', fontSize='small'))),
    align='wide', style={'spacing': {'blockGap': {'left': P(60)}}}))

# ------------------------------------------------------------------ newsletter, posts
NEWS_COPY = 'New prints, which originals are left, and when commissions open. Four emails a year, one of them about birds I saw on holiday.'
pattern('newsletter', 'Newsletter (box)', 'call-to-action', group(J(
    heading('A newsletter four times a year', 3, fontSize='large'), para(NEWS_COPY),
    buttons(('Sign up by email', 'mailto:hello@example.com?subject=Newsletter'))), className='is-style-sketchbook', anchor='newsletter', layout={'type': 'default'}))

pattern('newsletter-band', 'Newsletter (full-width band)', 'call-to-action', group(row(J(
    stack(J(heading('Four emails a year', 3, fontSize='large'), para(NEWS_COPY, fontSize='small')), style={'spacing': {'blockGap': P(10)}}),
    buttons(('Sign up by email', 'mailto:hello@example.com?subject=Newsletter'))), justify='space-between', align='wide'),
    align='full', className='is-style-sketchbook', layout={'type': 'constrained'}))

pattern('studio-diary', 'Studio diary (latest three posts)', 'posts,query', section(J(
    head_row('Studio diary', 'All posts', '/category/diary/', size='large'),
    query(J(dyn('post-featured-image', isLink=True, aspectRatio='3/2', scale='cover'), dyn('post-date'), dyn('post-title', isLink=True, level=3, fontSize='medium')),
          per_page=3, layout={'type': 'grid', 'columnCount': 3}, align='wide')), top=60))

pattern('post-list', 'Post list', 'posts,query', inherit_query(
    J(row(J(dyn('post-date'), dyn('post-title', isLink=True, level=2, fontSize='large')), justify='space-between', wrap=True)), align='wide'), inserter=False)

# ------------------------------------------------------------------ footers and 404
CREDIT = para('Demo images are public domain prints and plates by Audubon, Haeckel, Hokusai, Hiroshige, Ohara Koson and Redoute, from the Met, the National Gallery of Art and Wikimedia Commons, standing in for Joon\'s drawings.', align='wide', textColor='muted', fontSize='x-small')
pattern('footer-studio', 'Footer: studio, links and credit', 'footer', group(J(
    columns(
        ('40%', J(dyn('site-title', level=0), para('Drawings, prints and commissions from a small studio in Bristol. Prints ship within three working days.', fontSize='small'))),
        (None, J(heading('Studio', 6), para('Unit 4, Jamaica Street Studios<br>Bristol BS2 8JP<br><a href="mailto:hello@example.com">hello@example.com</a>', fontSize='small'))),
        (None, J(heading('Around here', 6), para('<a href="/events/">Events and workshops</a><br><a href="/press/">Press</a><br><a href="/sketchbook/">Sketchbook</a><br><a href="/?s=bird">Search the work</a>', fontSize='small'))),
        (None, J(heading('Elsewhere', 6), para('<a href="https://www.instagram.com/">Instagram</a><br><a href="/contact/#newsletter">Newsletter, four a year</a><br>Represented by Northern Lights Agency', fontSize='small'))),
        align='wide'),
    CREDIT), tag='div', align='full', className='is-style-rule-top', style=pad(60, 50), layout={'type': 'constrained'}), block_types='core/template-part/footer')

pattern('footer-newsletter', 'Footer: newsletter band first', 'footer', group(J(
    pattern_ref('newsletter-band'),
    group(J(row(J(dyn('site-title', level=0), para('<a href="/work/">Work</a>&nbsp;&nbsp; <a href="/shop/">Shop</a>&nbsp;&nbsp; <a href="/commissions/">Commissions</a>&nbsp;&nbsp; <a href="/contact/">Contact</a>&nbsp;&nbsp; <a href="https://www.instagram.com/">Instagram</a>', fontSize='small')),
                justify='space-between', align='wide'), CREDIT), align='full', style=pad(50, 50), layout={'type': 'constrained'})),
    tag='div', align='full', style={'spacing': {'margin': {'top': P(70)}, 'blockGap': '0'}}, layout={'type': 'constrained'}), block_types='core/template-part/footer')

pattern('footer-minimal', 'Footer: one line', 'footer', group(row(J(
    para('Joon Park, illustration, Bristol', fontSize='small'),
    para('<a href="mailto:hello@example.com">hello@example.com</a>&nbsp;&nbsp; <a href="https://www.instagram.com/">Instagram</a>', fontSize='small')), justify='space-between', align='wide'),
    tag='div', align='full', className='is-style-rule-top', style=pad(40), layout={'type': 'constrained'}), block_types='core/template-part/footer')

pattern('page-404', '404: page not found', 'text', J(
    columns(
        (None, J(heading('This page got rubbed out', 1, fontSize='xx-large'),
                 para('The link might be old, or I moved the drawing into a different folder. Try the <a href="/work/">work page</a>, the <a href="/shop/">shop</a>, or search below.'),
                 dyn('search', label='Search', showLabel=False, placeholder='Birds, maps, pub signs', buttonText='Search'))),
        ('40%', image('sketch-2.jpg', A['sketch-2.jpg'], 'A rough that went the same way.')), align='wide')), template_types='404')

# ------------------------------------------------------------------ page layouts
def page_pattern(slug, title, body, description=''):
    pattern(slug, title, 'pages', body, block_types='core/post-content', description=description)


page_pattern('page-art-for-sale', 'Page: art for sale', J(
    para('Originals are one-offs, so there is no cart for them. Email me the title and your postal address and I will send a payment link. Prices include mounting and postage in the UK, and every drawing is signed in pencil on the front.'),
    pattern_ref('originals-grid'), spacer(), columns((None, pattern_ref('how-to-buy-original')), (None, pattern_ref('postage-by-region')), align='wide'),
    pattern_ref('originals-list'), pattern_ref('notice-christmas-cutoff')),
    'The signature page: every original with medium, size, one price or reserved, then how to buy.')

page_pattern('page-commissions', 'Page: commissions', J(
    pattern_ref('commissions-status'), spacer(), pattern_ref('commission-options'), spacer(), pattern_ref('commission-steps'), spacer(),
    pattern_ref('commission-past-work'), spacer(), columns((None, pattern_ref('commission-price-list')), (None, J(pattern_ref('commission-faq'), pattern_ref('commission-process'))), align='wide'),
    pattern_ref('commission-terms'), spacer(), para('When the calendar is full, swap the box at the top of this page for this one:', fontSize='small', textColor='muted'), pattern_ref('commissions-closed')))

page_pattern('page-about', 'Page: about', J(
    pattern_ref('about-bio'), spacer(), pattern_ref('about-practical'), spacer(),
    columns((None, pattern_ref('about-desk')), (None, pattern_ref('clients-list')), align='wide'),
    spacer(), pattern_ref('books-list'), spacer(), pattern_ref('exhibitions-list'), spacer(), pattern_ref('press-quotes'), pattern_ref('about-short')))

page_pattern('page-contact', 'Page: contact', J(
    pattern_ref('contact-big-email'), spacer(), columns((None, pattern_ref('contact-agent')), (None, pattern_ref('contact-details')), align='wide'),
    spacer(), pattern_ref('contact-visit'), spacer(), pattern_ref('newsletter')))

page_pattern('page-events', 'Page: events and workshops', J(
    pattern_ref('events-list'), spacer(), pattern_ref('workshops'), spacer(), pattern_ref('open-studio'), spacer(), pattern_ref('exhibitions-list')))

page_pattern('page-press', 'Page: press', J(
    pattern_ref('press-list'), spacer(), pattern_ref('press-quotes'), spacer(), pattern_ref('clients-list'), spacer(), pattern_ref('testimonial')))

page_pattern('page-selected', 'Page: selected work, large', J(
    para('A short selection at a size you can read. For everything, by category, see <a href="/work/">Work</a>.'),
    pattern_ref('portfolio-two-up'), spacer(), pattern_ref('featured-work'), spacer(), pattern_ref('portfolio-large-column'), spacer(), pattern_ref('portfolio-even-grid'), pattern_ref('detail-crops')))

page_pattern('page-sketchbook', 'Page: sketchbook and process', J(
    para('Roughs, colour studies and pages I would normally keep in a drawer. Click any page to see it large.'),
    pattern_ref('process-strip'), spacer(), pattern_ref('series-plates'), pattern_ref('sketchbook-strip'), spacer(), pattern_ref('studio-diary')))

page_pattern('page-shop-front', 'Page: shop front (prints, books and postage)', J(
    pattern_ref('shop-highlights'), spacer(), pattern_ref('print-detail'), spacer(), pattern_ref('print-scale'), spacer(),
    pattern_ref('shop-categories'), spacer(), pattern_ref('shipping-note')),
    'A content page for the shop: highlights, one print in detail, the scale guide and shipping.')

print('patterns written:', len(os.listdir(os.path.join(D, 'patterns'))))

# ------------------------------------------------------------------ functions.php (pattern categories only)
write('functions.php', '''<?php
/**
 * Ink: pattern categories only.
 *
 * @package ink
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'shop'        => __( 'Shop and originals', 'ink' ),
			'commissions' => __( 'Commissions', 'ink' ),
			'events'      => __( 'Events and workshops', 'ink' ),
			'pages'       => __( 'Page layouts', 'ink' ),
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);''')

# ------------------------------------------------------------------ theme.json
tj = json.load(open(os.path.join(D, 'theme.json')))
st = tj['settings']
st['blocks'] = {'core/image': {'lightbox': {'enabled': True, 'allowEditing': True}}}
sizes = {s['slug']: s for s in st['typography']['fontSizes']}
sizes['x-large'].update(size='2rem', fluid={'min': '1.5rem', 'max': '2rem'})
sizes['xx-large'].update(size='3rem', fluid={'min': '2.125rem', 'max': '3rem'})
sizes['display'].update(size='4.5rem', fluid={'min': '2.75rem', 'max': '4.5rem'})
els = tj['styles']['elements']
els['h1']['typography']['fontSize'] = 'var:preset|font-size|xx-large'
els['h2']['typography']['fontSize'] = 'var:preset|font-size|x-large'
els['h3']['typography']['fontSize'] = 'var:preset|font-size|large'
els['h4']['typography']['fontSize'] = 'var:preset|font-size|medium'
bl = tj['styles']['blocks']
bl['core/quote']['typography']['fontSize'] = 'var:preset|font-size|large'
bl['core/navigation']['typography']['fontSize'] = 'var:preset|font-size|small'
tj['styles']['css'] = (
    ':where(h1,h2,h3){text-wrap:balance}:where(p){text-wrap:pretty}'
    '@media (prefers-reduced-motion:no-preference){a{transition:text-decoration-thickness .15s}a:hover{text-decoration-thickness:2px}}'
    ':where(table,.wp-block-post-date,.is-style-price-tag){font-variant-numeric:tabular-nums}'
    # captions under gallery images, not over them
    '.wp-block-gallery.has-nested-images figure.wp-block-image:has(figcaption):before{display:none}'
    '.wp-block-gallery.has-nested-images figure.wp-block-image figcaption{position:static;background:none;color:var(--wp--preset--color--muted);text-shadow:none;'
    'padding:.5rem 0 0;margin:0;text-align:left;font-size:var(--wp--preset--font-size--x-small);max-height:none;overflow:visible;flex-basis:auto}'
    '.wp-block-gallery.has-nested-images figure.wp-block-image figcaption a{color:inherit}'
    '.wp-block-gallery.has-nested-images:not(.is-cropped) figure.wp-block-image{flex-direction:column;justify-content:flex-start}'
    '.wp-block-image figcaption a,.wp-block-gallery figcaption a{color:var(--wp--preset--color--contrast)}'
    '.wp-block-image img,.wp-block-post-featured-image img{background:var(--wp--preset--color--surface)}'
    '@media (max-width:599px){.is-style-masonry{columns:2!important;column-gap:.75rem!important}.is-style-masonry>*{margin-bottom:1.25rem!important}}'
    '.wp-block-quote cite{font-size:var(--wp--preset--font-size--small);font-style:normal;font-weight:400;color:var(--wp--preset--color--muted)}'
    '.wp-lightbox-overlay .scrim{background-color:var(--wp--preset--color--base)!important}'
)
tj['templateParts'] = [
    {'area': 'header', 'name': 'header', 'title': 'Header'},
    {'area': 'footer', 'name': 'footer', 'title': 'Footer'},
    {'area': 'footer', 'name': 'footer-newsletter', 'title': 'Footer with newsletter'},
    {'area': 'footer', 'name': 'footer-minimal', 'title': 'Footer, one line'},
    {'area': 'uncategorized', 'name': 'notice', 'title': 'Notice bar'},
]
tj['customTemplates'] = [
    {'name': 'page-wide', 'title': 'Page, wide', 'postTypes': ['page']},
    {'name': 'single-work', 'title': 'Work (large picture, details beside)', 'postTypes': ['post']},
]
jdump('theme.json', tj)

# ------------------------------------------------------------------ section styles
C = lambda s: 'var:preset|color|%s' % s
SECTIONS = {
    'rule-top': ('Rule above', ['core/group', 'core/columns'], {'border': {'top': {'color': C('contrast'), 'width': '2px', 'style': 'solid'}}, 'spacing': {'padding': {'top': P(30)}}}),
    'rule-bottom': ('Rule below', ['core/group'], {'border': {'bottom': {'color': C('contrast'), 'width': '2px', 'style': 'solid'}}}),
    'hairline': ('Hairline row', ['core/group', 'core/columns'], {'border': {'bottom': {'color': C('line'), 'width': '1px', 'style': 'solid'}},
                                                                  'spacing': {'padding': {'top': P(20), 'bottom': P(20)}}, 'css': '&{margin-block:0!important}&>*{margin-block:0}'}),
    'sketchbook': ('Sketchbook', ['core/group', 'core/columns', 'core/cover'], {'color': {'background': C('surface'), 'text': C('contrast')},
                                                                               'spacing': {'padding': {'top': P(50), 'bottom': P(50), 'left': P(40), 'right': P(40)}}}),
    'red-notice': ('Red notice', ['core/group'], {'color': {'background': C('accent'), 'text': C('base')}, 'elements': {'link': {'color': {'text': C('base')}}},
                                                  'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'}}),
    'price-tag': ('Price', ['core/paragraph'], {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontWeight': '600'}, 'color': {'text': C('accent')}}),
    'tag': ('Label (sold, reserved)', ['core/paragraph'], {'typography': {'fontSize': 'var:preset|font-size|x-small', 'fontWeight': '600'},
                                                           'border': {'width': '1.5px', 'style': 'solid', 'color': C('contrast')},
                                                           'css': '&{display:inline-block;padding:.1em .55em;line-height:1.5}'}),
    'big-link': ('Big link', ['core/paragraph'], {'typography': {'fontFamily': 'var:preset|font-family|display', 'fontWeight': '800', 'lineHeight': '1.05', 'letterSpacing': '-0.01em'},
                                                  'css': '&{overflow-wrap:anywhere}'}),
    'inline-list': ('Inline list', ['core/categories'], {'typography': {'fontFamily': 'var:preset|font-family|body', 'fontSize': 'var:preset|font-size|small'},
                                                         'css': '&{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:.5rem 1.5rem}'}),
    'masonry': ('Masonry', ['core/post-template', 'core/gallery', 'core/group'], {
        'css': '&{display:block!important;columns:3 18rem;column-gap:var(--wp--preset--spacing--40)}'
               '&>*{break-inside:avoid;margin:0 0 var(--wp--preset--spacing--50)!important;width:100%!important;display:block}'
               '&>*>figcaption{margin-top:.5rem}'}),
}
for slug, (title, types, styles) in SECTIONS.items():
    jdump('styles/sections/%s.json' % slug, {'$schema': 'https://schemas.wp.org/trunk/theme.json', 'version': 3, 'title': title, 'slug': slug, 'blockTypes': types, 'styles': styles})

# ------------------------------------------------------------------ parts
write('parts/header.html', group(row(J(
    dyn('site-title', level=0),
    row(dyn('navigation', overlayMenu='mobile', layout={'type': 'flex', 'justifyContent': 'right'}), justify='right', style={'spacing': {'blockGap': P(40)}})),
    justify='space-between', align='wide', wrap=False),
    tag='header', align='full', className='is-style-rule-bottom', style=pad(30), layout={'type': 'constrained'}))
write('parts/footer.html', pattern_ref('footer-studio'))
write('parts/footer-newsletter.html', pattern_ref('footer-newsletter'))
write('parts/footer-minimal.html', pattern_ref('footer-minimal'))
write('parts/notice.html', pattern_ref('notice-christmas-cutoff'))

# ------------------------------------------------------------------ templates
def tpl(name, inner, top=60, bottom=70, footer='footer'):
    write('templates/%s.html' % name, page_template(inner, footer=footer, style=pad(top, bottom)))


write('templates/front-page.html', page_template(J(
    pattern_ref('home-intro'), pattern_ref('portfolio-masonry'), pattern_ref('recent-work'), pattern_ref('shop-entry-points'),
    pattern_ref('sketchbook-strip'), pattern_ref('testimonial'), spacer(), pattern_ref('commissions-status')),
    footer='footer-newsletter', style={'spacing': {'padding': {'bottom': '0'}}}))
tpl('home', J(row(J(heading('Work', 1, fontSize='xx-large'), para('<a href="/selected/">Or a short selection, large</a>', fontSize='small')), justify='space-between', align='wide'),
              pattern_ref('category-links'), spacer('var:preset|spacing|40'), pattern_ref('work-grid-archive')), top=50)
tpl('archive', J(dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'), dyn('term-description', align='wide'),
                 pattern_ref('category-links'), spacer('var:preset|spacing|40'), pattern_ref('work-grid-archive')), top=50)
tpl('category', J(dyn('query-title', type='archive', showPrefix=False, align='wide', fontSize='xx-large'), dyn('term-description', align='wide'),
                  pattern_ref('category-links'), spacer('var:preset|spacing|40'), pattern_ref('work-grid-archive'), spacer(), pattern_ref('commissions-status')), top=50)
tpl('index', J(dyn('query-title', type='archive', align='wide'), pattern_ref('post-list')))
tpl('search', J(dyn('query-title', type='search', align='wide', fontSize='xx-large'),
                dyn('search', label='Search', showLabel=False, placeholder='Birds, maps, pub signs', buttonText='Search', align='wide'),
                spacer('var:preset|spacing|40'), pattern_ref('work-grid-archive')), top=50)
tpl('404', pattern_ref('page-404'), top=70, footer='footer-minimal')
tpl('page', J(dyn('post-title', level=1), dyn('post-content', layout={'type': 'constrained'})))
tpl('page-wide', J(dyn('post-title', level=1, align='wide'), dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1360px'})))
tpl('single-work', J(
    group(J(para('<a href="/work/">Work</a> /', fontSize='small'), dyn('post-terms', term='category', separator=', ', fontSize='small')),
          align='wide', layout={'type': 'flex', 'flexWrap': 'wrap'}, style={'spacing': {'blockGap': P(10)}}),
    dyn('post-title', level=1, align='wide', fontSize='xx-large'),
    dyn('post-featured-image', align='wide'),
    dyn('post-content', align='wide', layout={'type': 'constrained', 'contentSize': '1360px'}),
    dyn('post-terms', term='post_tag', separator=', ', prefix='Tagged ', align='wide'),
    group(J(dyn('post-navigation-link', type='previous', label='Previous drawing', showTitle=True, taxonomy='category'),
            dyn('post-navigation-link', label='Next drawing', showTitle=True, taxonomy='category')),
          align='wide', className='is-style-rule-top', layout={'type': 'flex', 'justifyContent': 'space-between'}),
    pattern_ref('recent-work')), top=40)
tpl('single', J(
    dyn('post-date'), dyn('post-title', level=1),
    dyn('post-featured-image', align='wide'),
    dyn('post-content', layout={'type': 'constrained'}),
    dyn('post-terms', term='category', prefix='Filed under '),
    group(J(dyn('post-navigation-link', type='previous', label='Previous', showTitle=True), dyn('post-navigation-link', label='Next', showTitle=True)),
          className='is-style-rule-top', layout={'type': 'flex', 'justifyContent': 'space-between'}),
    pattern_ref('studio-diary')))
print('templates written')

# ------------------------------------------------------------------ demo content (posts use the kit's blocks)
STORIES = {
    'bluebirds-for-garden-letters': dict(
        brief=('Garden Letters wanted a spring cover that felt like the first warm Saturday. Two birds, lots of air, room for the masthead at the top.',
               'Four pencil roughs, one colour study in blue and rust, then the final in gouache at A3. The magazine chose the second rough; I still prefer the fourth.'),
        process=[('sketch-2.jpg', 'Pencil rough, the size of a stamp'), ('work-15.jpg', 'Colour study with too many birds'), ('hero.jpg', 'Final, two birds')],
        result=('The cover sold out in the shops in nine days. People wrote in asking for the birds as a print, so we let Joon sell one.', 'Tomasz Nowak, art editor, Garden Letters',
                'The magazine printed 400 extra copies. The print is now the best seller in the shop, which I did not see coming.',
                [('Art direction', 'Tomasz Nowak'), ('Print edition', 'A3, 150 copies')])),
    'barred-owl-the-night-walk': dict(
        brief=('Little Toller wanted a cover that worked at thumbnail size on a phone and full size on a table in a bookshop. The book is about walking at night, so: dark, but not gloomy.',
               'Eleven roughs of the owl, one of the squirrel. The final is gouache on a mid-grey ground so the pale feathers do the work. The endpapers are the same branch, empty.'),
        process=[('sketch-1.jpg', 'Roughs, mostly wrong'), ('work-7.jpg', 'Final cover painting'), ('work-3.jpg', 'Endpaper study, later dropped')],
        result=('The best cover we have printed in years, and the only one people asked to buy.', 'Ellie Gray, Little Toller Books',
                'It went to a second printing in the first month. The owl is now an A3 print.', [('Designer', 'Ellie Gray'), ('Format', 'Hardback, 216 pages')])),
    'totterdown-from-the-air': dict(
        brief=('Priya and Sam were leaving Totterdown after eleven years and wanted their street, the view from their bedroom window and the walk to the pub on one sheet.',
               'I walked it twice with a sketchbook, drew the plan in pencil at A2, then inked and painted it. Their cat is in the window of number 14. I didn\'t tell them.'),
        process=[('sketch-2.jpg', 'Walking sketch, very rough'), ('map-1.jpg', 'The finished map'), ('work-14.jpg', 'Colour reference for the river')],
        result=('The map is on our kitchen wall and we still find new things in it.', 'Priya and Sam',
                'They ordered two more prints for their parents. A neighbour on the same street asked for one of hers.', [('Size', '50 x 70 cm'), ('Time', 'Five weeks, with one round of changes')])),
    'crow-and-blossom-kinoko-tea': dict(
        brief=('Kinoko Tea in Stokes Croft needed a tin wrap for a spring green tea. The tin is small and round, so the drawing had to work in a strip 7 cm tall.',
               'One crow, one branch, painted on toned paper so the blossom could be pure white gouache. The branch wraps all the way round so the tin has no front.'),
        process=[('work-13.jpg', 'First idea, a long-tailed bird, too tall'), ('work-9.jpg', 'Final painting'), ('work-10.jpg', 'Leaf study for the lid')],
        result=('People buy the tin for the tin. We have started selling it empty.', 'Hana Mori, Kinoko Tea',
                'The second tin, for a roasted tea, is on my desk now.', [('Printed by', 'A tin maker in Leicester'), ('Run', '2,000 tins')])),
}


def post_body(slug):
    w = W[slug]
    parts = []
    if slug == 'hummingbirds-six-plates':
        parts += [columns(('60%', para('Six plates for a Saturday nature supplement, one bird a week through May and June. Each one had to sit in a column 9 cm wide and still read from across a kitchen.')),
                          (None, work_caption(slug)), align='wide'),
                  series_plates('The six plates', 'Click any plate to see it large.', PLATES, pm=False),
                  detail_crops(('work-12.jpg', A['work-12.jpg'], 'Plate 1, whole'), ('work-15.jpg', A['work-15.jpg'], 'Plate 2, detail'), ('work-11.jpg', A['work-11.jpg'], 'Plate 5, detail'), pm=False)]
    elif slug in STORIES:
        s = STORIES[slug]
        parts += [columns(('60%', para(s['brief'][0])), (None, work_caption(slug)), align='wide'),
                  project_brief(*s['brief']),
                  process_strip([(f, A[f], c) for f, c in s['process']], pm=False),
                  project_result(*s['result'])]
    else:
        parts += [columns(('60%', para(SHORT[slug])), (None, work_caption(slug)), align='wide')]
        if slug in EXTRA:
            f, c = EXTRA[slug]
            parts.append(image(U(f), A[f], c, align='wide'))
    parts.append(pattern_ref('commissions-status'))
    return J(*parts)


SHORT = {
    'jellyfish-aquarium-lates': 'Four posters for the aquarium\'s late openings, one sea creature each. The jellyfish was the first and the one that went on the buses.',
    'heron-at-low-tide': 'For a feature on the Severn estuary. Drawn on location over two cold mornings, then painted at the desk from the pencil drawings.',
    'red-mountain-book-cover': 'Cover for a travel memoir. The publisher wanted "a mountain that looks warm", so it is red.',
    'puffin-wild-bird-trust': 'A puffin for the Wild Bird Trust members magazine. The trust sold 300 prints of it at £25 and kept the money for a seabird survey.',
    'plum-branch-harbourside-market': 'Spring poster for Harbourside Market, printed as a three-colour screenprint in an edition of 80. The pink is one ink, overprinted to get the sky.',
    'orchid-wallpaper-ostra': 'A wallpaper for the back room at Ostra in Clifton, repeated as a half-drop so the orchids never line up. The menus use the same drawing, cropped.',
    'medicinal-plants-chart': 'Tea box wrap for Hedgerow Apothecary. 42 plants, each labelled by hand, which took longer than the drawing.',
    'radiolarian-science-festival': 'Poster for the Bristol Science Festival. A single-celled sea creature drawn 4,000 times its real size, printed in yellow and black on uncoated stock.',
    'two-ducks-picture-book': 'One spread from <em>The Pond in Winter</em>, words by Mari Evans. Gouache, painted at 120% of print size so the texture survives the printer.',
    'ocean-waves-surf-shop-mural': 'A 6 metre wall behind the till at Saltwater Surf in Weston. Projected from a pencil drawing, painted over four evenings after closing.',
    'eucomis-seed-packet': 'One of twelve seed packets for Bramble Seeds. The eucomis is the one that sold out first, which the grower says has nothing to do with the drawing.',
    'animal-parade-mural-study': 'Study for a school hall mural. The final wall is 11 metres long and has a camel that the children named Steve.',
    'snowy-street-winter-poster': 'A winter poster for the Christmas market, printed as a two-colour screenprint in an edition of 60.',
}
EXTRA = {'jellyfish-aquarium-lates': ('work-4.jpg', 'The next poster in the series, a radiolarian.'),
         'orchid-wallpaper-ostra': ('work-10.jpg', 'A leaf study for the pattern repeat.'),
         'heron-at-low-tide': ('sketch-2.jpg', 'Pencil drawing from the second morning.')}

posts = []
for i, w in enumerate(WORKS):
    slug, title, cat, img_, *_rest = w
    posts.append({'title': title, 'slug': slug, 'category': cat, 'tags': w[8], 'image': img_, 'template': 'single-work',
                  'excerpt': w[5] + ', ' + w[6], 'date': '2026-%02d-%02d' % (9 - i // 3, 25 - (i % 3) * 7), 'content': post_body(slug)})

DIARY = [
    ('open-studio-dates', 'Open studio dates for the year', 'studio.jpg', '2026-03-20',
     [para('The studio is open on the first Saturday of every month. The big one is Saturday 1 November, 11am to 4pm. I\'ll have the plan chest open, so you can look through roughs that never made it, and a box of seconds at £10 each.'),
      para('Unit 4, Jamaica Street Studios. Two flights of stairs, no lift. If the stairs are a problem, email me and I\'ll bring things down to the courtyard.'),
      pattern_ref('open-studio')]),
    ('a-page-from-the-sketchbook', 'A page from the sketchbook', 'sketch-1.jpg', '2026-03-06',
     [para('I keep one sketchbook for work and one for nothing in particular. This page is from the second one, drawn on a train to Cardiff while someone slept on my shoulder.'),
      gal([('sketch-1.jpg', A['sketch-1.jpg'], 'Train page'), ('sketch-2.jpg', A['sketch-2.jpg'], 'The page after, abandoned')], cols=2, crop=False, pm=False),
      para('Neither page will ever be a print. That is what the second sketchbook is for.')]),
    ('prints-back-in-stock', 'The owl is back in stock', 'work-7.jpg', '2026-02-24',
     [para('The barred owl A3 print sold out in a week in January. The reprint arrived on Tuesday: 100 copies on the same Hahnemuhle paper, checked one by one against the painting.'),
      pattern_ref('shop-highlights')]),
]
for slug, title, img_, date, body in DIARY:
    posts.append({'title': title, 'slug': slug, 'category': 'diary', 'image': img_, 'date': date, 'content': J(*body)})

content = {
    'site': {'title': 'Joon Park', 'tagline': 'Illustration, prints and commissions from Bristol'},
    'categories': [{'slug': 'editorial', 'name': 'Editorial', 'description': 'Magazines and newspapers, mostly birds.'},
                   {'slug': 'books', 'name': 'Books', 'description': 'Covers, picture books and one book of my own.'},
                   {'slug': 'posters', 'name': 'Posters and murals', 'description': 'Screenprints, festival posters and a few walls.'},
                   {'slug': 'packaging', 'name': 'Packaging and pattern', 'description': 'Tins, seed packets, wallpaper.'},
                   {'slug': 'maps', 'name': 'Maps', 'description': 'Streets, towns and wedding walks, drawn from above.'},
                   {'slug': 'diary', 'name': 'Studio diary', 'description': 'News from the desk: open studios, reprints and sketchbook pages.'}],
    'front_page': 'home', 'posts_page': 'work',
    'pages': [
        {'slug': 'home', 'title': 'Home', 'content': ''},
        {'slug': 'work', 'title': 'Work', 'content': ''},
        {'slug': 'selected', 'title': 'Selected work', 'pattern': 'ink/page-selected', 'template': 'page-wide'},
        {'slug': 'sketchbook', 'title': 'Sketchbook', 'pattern': 'ink/page-sketchbook', 'template': 'page-wide'},
        {'slug': 'art-for-sale', 'title': 'Art for sale', 'pattern': 'ink/page-art-for-sale', 'template': 'page-wide'},
        {'slug': 'prints', 'title': 'Prints', 'pattern': 'ink/page-shop-front', 'template': 'page-wide'},
        {'slug': 'commissions', 'title': 'Commissions', 'pattern': 'ink/page-commissions', 'template': 'page-wide'},
        {'slug': 'events', 'title': 'Events and workshops', 'pattern': 'ink/page-events', 'template': 'page-wide'},
        {'slug': 'press', 'title': 'Press', 'pattern': 'ink/page-press', 'template': 'page-wide'},
        {'slug': 'about', 'title': 'About', 'pattern': 'ink/page-about', 'template': 'page-wide'},
        {'slug': 'contact', 'title': 'Contact', 'pattern': 'ink/page-contact', 'template': 'page-wide'},
    ],
    'posts': posts,
    'nav': [{'label': 'Work', 'url': '/work/'}, {'label': 'Shop', 'url': '/shop/'}, {'label': 'Art for sale', 'url': '/art-for-sale/'},
            {'label': 'Commissions', 'url': '/commissions/'}, {'label': 'Events', 'url': '/events/'}, {'label': 'About', 'url': '/about/'}, {'label': 'Contact', 'url': '/contact/'}],
    'currency': 'GBP',
    'products': [
        {'name': 'Snowy street, A3 print', 'price': '38', 'image': 'prints.jpg', 'category': 'Prints', 'sku': 'INK-P01', 'stock': 24, 'short': 'A3 on 300gsm cotton rag. Ships rolled in a tube.'},
        {'name': 'Barred owl, A3 print', 'price': '38', 'image': 'work-7.jpg', 'category': 'Prints', 'sku': 'INK-P05', 'stock': 3, 'short': 'A3 on 300gsm cotton rag. Three left.'},
        {'name': 'Bluebirds, A4 print', 'price': '28', 'image': 'hero.jpg', 'category': 'Prints', 'sku': 'INK-P06', 'stock': 40, 'short': 'A4 on 300gsm cotton rag. Ships flat between boards.'},
        {'name': 'Red mountain, A3 print', 'price': '38', 'image': 'work-6.jpg', 'category': 'Prints', 'sku': 'INK-P02', 'stock': 12, 'short': 'A3 on 300gsm cotton rag.'},
        {'name': 'Jellyfish, A3 print', 'price': '38', 'image': 'work-8.jpg', 'category': 'Prints', 'sku': 'INK-P07', 'stock': 18, 'short': 'A3 on 300gsm cotton rag. From the Aquarium Lates poster.'},
        {'name': 'Heron, A4 print', 'price': '28', 'image': 'work-3.jpg', 'category': 'Prints', 'sku': 'INK-P03', 'stock': 40, 'short': 'A4 on 300gsm cotton rag. Ships flat between boards.'},
        {'name': 'Medicinal plants, A3 print', 'price': '38', 'image': 'work-1.jpg', 'category': 'Prints', 'sku': 'INK-P04', 'stock': 0, 'short': 'Sold out. A reprint is planned for spring.'},
        {'name': 'Small Maps (zine)', 'price': '8', 'image': 'map-1.jpg', 'category': 'Publications', 'sku': 'INK-Z01', 'stock': 60, 'short': '24 pages, risograph printed in two colours.'},
        {'name': 'Birds of the Avon (hardback)', 'price': '22', 'image': 'work-15.jpg', 'category': 'Publications', 'sku': 'INK-B01', 'stock': 15, 'short': 'Signed on request. 96 pages.'},
    ],
}
json.dump(content, open('demos/ink/content.json', 'w'), indent=1, ensure_ascii=False)
print('demo written:', len(posts), 'posts')
