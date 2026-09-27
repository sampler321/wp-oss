import sys; sys.path.insert(0, 'tools/lib')
from blocks import *
set_theme('ink')
S = THEME['slug']

# ---------- Front page hero ----------
pattern('hero-recent-commission', 'Hero: latest commission and what is for sale', 'featured,portfolio', columns(
  ('66.66%', image('hero.jpg', 'Two blue birds on a thin branch, painted in blue and rust on cream paper', 'Two bluebirds, for the spring issue of Garden Letters, 2025')),
  ('33.33%', J(heading('Joon Park draws birds, maps and the occasional pub sign.', 1, fontSize='xx-large'),
     para('Illustrator in Bristol, mostly gouache. Editorial, packaging, books and posters since 2014.'),
     heading('For sale now', 6),
     pattern_ref('for-sale-list'))),
  align='wide', style={'spacing': {'padding': {'top': 'var:preset|spacing|60', 'bottom': 'var:preset|spacing|60'}, 'blockGap': {'left': 'var:preset|spacing|60'}}}))

# ---------- Signature: art for sale ----------
pattern('for-sale-list', 'Originals for sale (list)', 'portfolio,shop', J(
  table([
    ['Bluebirds on a thin branch', 'Gouache on Arches, 21 × 28 cm', '£420'],
    ['Hackney Marshes, redrawn', 'Pen and correction fluid, 30 × 40 cm', '<strong>Reserved</strong>'],
    ['Heron, low tide', 'Gouache, 24 × 32 cm', '£380'],
    ['The Coach and Horses sign, study', 'Pencil and gouache, 18 × 24 cm', '£240'],
  ], head=['Drawing', 'Medium and size', 'Price'], className='is-style-stripes'),
  para('<a href="/art-for-sale/">All originals and how to buy one</a>', fontSize='small')))

pattern('art-for-sale-page', 'Page: art for sale', 'portfolio', J(
  para('Originals are one-offs, so there is no shop cart for them. Email me the title and your postal address and I will send a payment link. Prices include framing-ready mounting and postage in the UK. Originals arrive within 21 days.'),
  pattern_ref('for-sale-grid'),
  pattern_ref('how-to-buy-original'),
  pattern_ref('postage-by-region')), block_types='core/post-content', description='The signature page: every original with medium, size, one price and a reserved state.')

pattern('for-sale-grid', 'Originals for sale (grid with prices)', 'portfolio,shop', grid(J(
  stack(J(image('hero.jpg', 'Two blue birds on a thin branch, painted in blue and rust on cream paper'),
          heading('Bluebirds on a thin branch', 3, fontSize='large'),
          para('Gouache on Arches, 21 × 28 cm on a 30 × 40 cm sheet', fontSize='x-small'),
          para('£420', className='is-style-price-tag'))),
  stack(J(image('work-2.jpg', 'Engraving of camels, elephants and other animals gathered in a rocky landscape'),
          heading('Hackney Marshes, redrawn', 3, fontSize='large'),
          para('Pen and correction fluid, 30 × 40 cm', fontSize='x-small'),
          para('Reserved', className='is-style-price-tag'))),
  stack(J(image('work-3.jpg', 'A white heron standing in reeds at the edge of a marsh'),
          heading('Heron, low tide', 3, fontSize='large'),
          para('Gouache, 24 × 32 cm on a 30 × 40 cm sheet', fontSize='x-small'),
          para('£380', className='is-style-price-tag'))),
), min_width='18rem', align='wide'))

pattern('how-to-buy-original', 'How to buy an original', 'text', group(J(
  heading('How to buy an original', 3),
  lst(['Email <a href="mailto:hello@example.com">hello@example.com</a> with the title and your postal address.',
       'I reply within two working days with a payment link. I hold the drawing for you for a week.',
       'Once paid, it is mounted, wrapped flat between boards and posted with tracking.',
       'It arrives within 21 days. Outside the UK, add the postage shown below.'], ordered=True)),
  className='is-style-sketchbook'))

pattern('postage-by-region', 'Postage by region', 'shop', J(
  heading('Postage', 3),
  table([['UK', 'Included', '2 to 4 working days'], ['EU', '£9', '5 to 10 working days'], ['USA and Canada', '£14', '7 to 14 working days'], ['Rest of the world', '£18', '10 to 21 working days']],
        head=['Where', 'Prints', 'Usually takes']),
  para('Prints ship rolled in a tube. Originals and A4 prints ship flat between boards.', fontSize='small')))

# ---------- Nice-to-haves ----------
pattern('notice-christmas-cutoff', 'Notice: Christmas posting dates', 'banner', group(
  para('Order by <strong>15 December</strong> for UK Christmas delivery, <strong>8 December</strong> for the EU and <strong>1 December</strong> for everywhere else. Take this bar out on 16 December.'),
  className='is-style-red-notice', align='full', style={'spacing': {'padding': {'top': 'var:preset|spacing|20', 'bottom': 'var:preset|spacing|20'}}}),
  description='A notice bar for posting deadlines. Edit the dates each year and remove it when they pass.')

pattern('print-scale', 'Print shown at scale', 'shop', columns(
  (None, image('prints.jpg', 'Woodblock print of a snowy street and canal under a pale sky')),
  (None, J(heading('How big is an A3 print?', 3),
    para('A3 is 29.7 × 42 cm, about the size of two sheets of printer paper side by side. A4 is one sheet. Both are printed on 300gsm cotton rag with a 2 cm white border for framing.'),
    para('A3 prints ship rolled in a tube. A4 prints ship flat between boards.', fontSize='small'))), align='wide'))

pattern('commissions-status', 'Commissions open or closed', 'call-to-action', group(J(
  heading('Commissions are open until 31 October', 2),
  para('After that I am drawing a book and won\'t take new work until March. Bird portraits start at £180. Maps and house portraits are quoted after a short chat.'),
  buttons(('Ask about a commission', '/commissions/'))),
  className='is-style-sketchbook', align='wide'), description='Swap the heading and button for a waiting-list line when commissions close.')

pattern('commissions-closed', 'Commissions closed (waiting list)', 'call-to-action', group(J(
  heading('Commissions are closed until March', 2),
  para('I\'m drawing a book this winter. If you\'d like to be first in line when I reopen, email me with "waiting list" in the subject. No deposit needed.')),
  className='is-style-sketchbook', align='wide'))

pattern('commission-options', 'Commission options and prices', 'services', table([
  ['Single bird or animal', 'Digital print, A4', '£180'],
  ['Single bird or animal', 'Painted original, A4', '£320'],
  ['House portrait', 'Painted original, A3', '£450 to £600'],
  ['Illustrated map', 'Digital, print-ready', 'From £900']], head=['What', 'Format', 'Price']))

pattern('commission-process', 'Commission process', 'services', J(
  heading('How a commission works', 3),
  lst(['Fill in the form or email me. Tell me what, how big, and when you need it.',
       'I send a short contract. A 40% deposit books your slot.',
       'You get a pencil sketch and a colour study. Two rounds of changes are included.',
       'I paint the final. You pay the balance, then it ships or I send the files.'], ordered=True)))

pattern('commission-faq', 'Commission FAQ', 'text', J(
  heading('Questions people ask', 3),
  details('How long does it take?', para('Three to five weeks from deposit to delivery. Christmas slots fill by mid-October.')),
  details('Can I send reference photos?', para('Yes, please. Phone photos are fine. Several angles help more than one perfect shot.')),
  details('Who owns the copyright?', para('I keep the copyright. You get the original or print to keep, and a licence for personal use. Commercial use is quoted separately.')),
  details('Can you draw my dog?', para('Yes, but I draw dogs the same way I draw birds: slightly stern and very still.'))))

pattern('commission-terms', 'Commission terms (short)', 'text', J(
  heading('Terms, in plain words', 3),
  lst(['The 40% deposit is non-refundable once I start the sketch.',
       'Two rounds of changes are included at sketch stage. Changes after the final is painted cost extra.',
       'I keep the copyright and may show the work in my portfolio unless you ask me not to.',
       'If I can\'t finish for any reason, I refund everything you\'ve paid.'])))

pattern('commissions-page', 'Page: commissions', 'services', J(
  pattern_ref('commissions-status'), pattern_ref('commission-options'), pattern_ref('commission-process'),
  pattern_ref('commission-faq'), pattern_ref('commission-terms')), block_types='core/post-content')

# ---------- Portfolio ----------
pattern('work-grid', 'Latest work (masonry)', 'portfolio,query', group(J(
  row(J(heading('Recent work', 2), para('<a href="/work/">Everything, by category</a>', fontSize='small')), justify='space-between', align='wide'),
  query(J(dyn('post-featured-image', isLink=True), dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-terms', term='post_tag', separator=' / ')),
        per_page=9, align='wide', template_class='is-style-masonry')), align='wide', layout={'type': 'default'}), keywords='work, portfolio, grid')

pattern('work-grid-archive', 'Work archive (masonry, inherits the page query)', 'portfolio,query', inherit_query(
  J(dyn('post-featured-image', isLink=True), dyn('post-title', isLink=True, level=3, fontSize='medium'), dyn('post-terms', term='post_tag', separator=' / ')),
  align='wide', template_class='is-style-masonry'), inserter=False)

pattern('post-list', 'Post list', 'posts,query', inherit_query(
  J(row(J(dyn('post-date'), dyn('post-title', isLink=True, level=2, fontSize='large')), justify='space-between', wrap=True)),
  align='wide'), inserter=False)

pattern('work-caption', 'Work caption (client, publication, year)', 'portfolio', table(
  [['Client', 'Garden Letters magazine'], ['Used for', 'Spring issue cover'], ['Year', '2025'], ['Medium', 'Gouache, finished digitally']]))

pattern('process-strip', 'Roughs next to finals', 'portfolio,gallery', J(
  heading('From rough to final', 3),
  gallery([('work-4.jpg', 'A yellow radiolarian drawn as a spiky star with fine hatching', 'Pencil rough'),
           ('work-5.jpg', 'Two ducks swimming, painted in soft grey and green washes', 'Colour study'),
           ('work-6.jpg', 'A red mountain against a blue sky with rows of white clouds', 'Final')], columns=3, align='wide')))

pattern('shop-categories', 'Shop: prints and publications', 'shop', group(J(
  heading('Shop', 2),
  columns(
    (None, J(image('prints.jpg', 'Woodblock print of a snowy street and canal under a pale sky', href='/shop/'), heading('<a href="/shop/">Prints</a>', 3), para('A4 and A3 on cotton rag, from £28.'))),
    (None, J(image('work-1.jpg', 'A dense botanical chart of medicinal plants with small numbered labels', href='/shop/'), heading('<a href="/shop/">Publications</a>', 3), para('Zines, a colouring book and one proper hardback.'))),
    (None, J(image('work-2.jpg', 'Engraving of camels, elephants and other animals gathered in a rocky landscape', href='/art-for-sale/'), heading('<a href="/art-for-sale/">Originals</a>', 3), para('One-offs, sold by email. Some are reserved.'))), align='wide')), align='wide', layout={'type': 'default'}))

pattern('books-list', 'Books', 'text', J(
  heading('Books', 3),
  table([['<em>Birds of the Avon</em>', 'Little Toller Books', '2023', '<a href="https://example.com/">Buy from the publisher</a>'],
         ['<em>Small Maps</em>', 'self-published zine', '2021', '<a href="/shop/">In the shop</a>']], head=['Title', 'Publisher', 'Year', 'Where'])))

pattern('clients-list', 'Clients (text list)', 'about', J(
  heading('People I\'ve drawn for', 3),
  para('Garden Letters, The Guardian Saturday, Little Toller Books, Bristol Old Vic, Wild Bird Trust, Harbourside Market, Clifton Pub Company, Penguin Random House (one cover, very proud)', fontSize='large')))

pattern('press-quotes', 'Press quotes (named)', 'testimonials', columns(
  (None, quote('Joon draws birds like they owe him money.', 'Tomasz Nowak, art editor, Garden Letters, 2024')),
  (None, quote('The map is on our kitchen wall and we still find new things in it.', 'Priya and Sam, commissioned a map of Totterdown, 2025')), align='wide'))

pattern('about-bio', 'About: bio', 'about', columns(
  ('40%', image('work-5.jpg', 'Two ducks swimming, painted in soft grey and green washes')),
  (None, J(heading('About', 2),
    para('I\'m Joon Park, an illustrator in Bristol. I grew up in Busan, studied illustration at Falmouth and have drawn for magazines, publishers and one very patient pub company since 2014.'),
    para('I work in gouache and pencil at a desk that faces a wall on purpose. I don\'t use AI tools and I don\'t do logo design. I will draw your dog, but it will look slightly stern.'),
    para('Represented for editorial work by Northern Lights Agency. For everything else, email me directly.'))), align='wide'))

pattern('about-page', 'Page: about', 'about', J(pattern_ref('about-bio'), pattern_ref('clients-list'), pattern_ref('books-list'), pattern_ref('exhibitions-list'), pattern_ref('press-quotes')), block_types='core/post-content')

pattern('exhibitions-list', 'Exhibitions', 'about', J(
  heading('Shown at', 3),
  table([['2025', 'Paper Birds, group show', 'Spike Island, Bristol'], ['2024', 'Small Maps, solo', 'The Letterpress Room, Bath'], ['2022', 'Illustrators\' Fair', 'Old Truman Brewery, London']])))

pattern('contact-details', 'Contact details', 'contact', columns(
  (None, J(heading('Say hello', 2), para('Email is best: <a href="mailto:hello@example.com">hello@example.com</a>. I reply within two working days, not at weekends.'),
    para('For editorial work, contact Asha at Northern Lights Agency: <a href="mailto:asha@example.com">asha@example.com</a>.'))),
  (None, J(heading('Studio visits', 3), para('Open studio on the first Saturday of the month, 11am to 4pm. Unit 4, Jamaica Street Studios, Bristol BS2 8JP. Two flights of stairs, no lift, sorry.'))), align='wide'))

pattern('contact-page', 'Page: contact', 'contact', J(pattern_ref('contact-details'), pattern_ref('newsletter')), block_types='core/post-content')

pattern('newsletter', 'Newsletter', 'call-to-action', group(J(
  heading('A newsletter four times a year', 3),
  para('New prints, which originals are left, and when commissions open. No more than four emails a year, one of them about birds I saw on holiday.'),
  buttons(('Sign up by email', 'mailto:hello@example.com?subject=Newsletter'))), className='is-style-sketchbook', anchor='newsletter'))

pattern('studio-diary', 'Studio diary strip', 'posts', J(
  heading('Studio diary', 3),
  query(J(dyn('post-date'), dyn('post-title', isLink=True, level=4)), per_page=3, layout={'type': 'grid', 'columnCount': 3}, align='wide')))

pattern('shipping-note', 'Shipping and returns, one paragraph', 'shop', group(para(
  'Prints ship within three working days in a tube or between boards, tracked. If a print arrives damaged, send me a photo within 14 days and I\'ll send another. Originals can\'t be returned, so ask me for more photos before you buy.', fontSize='small'),
  className='is-style-rule-top'))

pattern('page-landing-wide', 'Page: portfolio landing', 'portfolio', J(pattern_ref('work-grid'), pattern_ref('process-strip')), block_types='core/post-content')
print('patterns written')
