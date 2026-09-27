# taproom: notes

- Direction: the research's utility label system, as briefed. Cooperage Brewing (Aoife Brennan and Tadhg Moran, Smithfield, Dublin 7) looks like the bar wall: brown paper ground, black type, white paper labels with a ruled inner frame, one stamp red, 0 radius everywhere.
- Fonts: Economica 700 (as registered for 088; uppercase for beer names only) and Public Sans with tabular figures for everything else. Two families. The research's Courier Prime tap list was dropped under the no-monospace rule; the tap list now gets its stock-sheet feel from Economica beer names, tabular Public Sans figures and hairline rules.
- Palette: brown paper #D9C3A0, ink #1A1A1A, stamp red #B3241A (prices and the "updated" stamp only), label white #FFFFFF. Variations: Cask, Stout (dark), Hop.
- Signature: the tap list at the top of the home page and the taproom page: line, beer, style, hops, ABV, half and pint, under a rotated red "Draught menu updated" stamp, with an allergen line. On phones it drops to beer, ABV and pint, and it prints on A4 without header, photos or buttons.
- Content: beers are posts in Beers with a "Beer (paper label)" template; events and news are posts; taproom, book a table, beer club, trade and about are page-layout patterns. WooCommerce sells cans, a mixed case and merch. Nice-to-haves built: booking rules, beer club, collect and delivery with costs shown before checkout, printable tap list, allergen line, guest line.
- Images: CC0 Commons photos of the counter, canning line, cans, taps and tacos. Can labels and merch (glass, tote, T-shirt) were drawn for this theme by build/taproom_draw.py (CC0), so no other brewery's branding appears as a product.
- Age: no pop-up. The age rule is written in the footer, on the hours panel and next to the shop.
- Core-block limits: "on tap" is a set of rows the staff edit by hand; there is no per-beer on/off switch without custom fields.

## Round 2

- Tap list rebuilt as rows of groups (number, beer, style and hops, ABV, prices) instead of a table, so the home page has no table; on phones it drops to beer, style, ABV and price. A plain-table version stays as "Printable tap sheet" for A4.
- Opening hours and the kitchen menu are ruled label/value rows. Tables remain only where the data is tabular (tap sheet, beer club terms, trade formats, delivery costs, beer spec): 5 of 48 patterns.
- Image lightbox enabled in theme.json and used on can labels, merch and photos.
- 21 new patterns from The Kernel, Cloudwater and Other Half: in the tanks, next can release, kitchen menu, house rules, event types, quiz night, brewery tours, team, collaborations, spent grain, jobs, private hire, gift membership, stockists, keg returns, merch strip, release emails, allergen key, printable tap sheet, plus page layouts for about and tours. New "Tours and events" page; about, taproom, booking, beer club and trade pages use the new patterns in context.
- Home: tap list first (the current thing), then the name, hours and bookings, kitchen, next release, events, cans, merch and the beer club.
