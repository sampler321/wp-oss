# deck: notes

- Direction: the owner asked for edgy and Thrasher-like, so the shop is a skate magazine. Black and red, a masthead as wide as the screen, a flame strip (an SVG drawn in CSS) hanging off the header on every page, halftone black-and-white photos, torn photocopy edges, grip-tape texture behind the deck wall, and red price stickers stuck on at an angle.
- Signature: the home page is a magazine cover built from core blocks (an Image and a Group stacked in one CSS grid cell): halftone photo, giant red masthead, ransom-note cover lines. The truck size guide (deck width to truck axle to wheel size) links to undercarriage kits, as in the research.
- Ransom-note type: headings use `<mark>`, `<strong>` and `<em>` around words, which the `is-style-ransom` section style turns into cut-out boxes in black, red, yellow and white, mixing Staatliches with Sofia Sans Condensed black italic. On photos every word is boxed so it stays readable.
- Fonts: Staatliches (display, from the registry; it already reads as a condensed magazine headline, so no new claim) and Sofia Sans Condensed 400 to 900 with italics (body). Two families, no mono.
- Palette: newsprint #F1EFE8, black #0A0A0A, red #D7140F, white #FFFFFF, cover yellow #FFD400 (only on black). Variations: Zine (grey and black), Beach (sand and sea green), Concrete park (grey and cone orange).
- No logos or trade dress from real magazines or brands: the masthead is the shop name in Staatliches, and the flames are generic hot-rod tongues.
- Sniff-test note: the ransom headings recolour words by design (the brief asks for ransom-note mixing); every word or several words are treated, never a single highlighted word.

## Round 2

- Look kept exactly (masthead cover, flames, halftone, ransom type, stickers, grip tape). The owner asked for more blocks and more usage areas, so the kit went from 26 to 66 patterns.
- New page types and patterns: rider profiles (one per rider, used in four rider posts in a Team category with its own `category-team` template), video parts (hero still, credits, lightbox stills, tracklist, video night; four video posts in a Videos category with `category-videos`), shop-built completes with parts lists, how we build a board, sale rack, drop announcement and drop-day rules, gift cards, a local spot guide, a spot map list with an OpenStreetMap link, spot etiquette, zine cover, zine spread, back issues, lookbook and photo wall (lightbox), contest entry and results, tour dates, stockists, counter FAQ, named customer notes, crew email, an alternative red hero.
- New pages: Completes, Spot guide, Zine, Drops and sale, Stockists, plus the automatic pattern library. Nav and footer link to every page and both category archives. News is now the posts page.
- Tables: only the three real price lists remain (counter jobs, surf rental, post and returns). Events, hours, the truck guide, kids' sizes, credits, stockists and setups are ruled rows built from groups (`is-style-rows`), so the home page has no table.
- Image lightbox is on globally; galleries and lookbook photos open large. Linked product images still go to the product.
- Three extra CC0 photos (Venice Beach park at sunset, a flip down stairs, a cruiser against a wall).
