# Studio: notes

- Direction: "wide-set studio sheet" for a seven-person branding studio in Leeds (Sandvik Ogunleye). White sheet, black type, studio orange (#FF5A1F) used only as fills for the active filter and as link underlines, so the client work carries the colour.
- Fonts: Anybody only (variable width, OFL). Headings at font-stretch 125% / 800, body at 100%, labels and captions at 75%. No mono.
- Signature: the work index. A Selected / All switch plus two ruled filter bars (Services = categories, Industry = tags) above a 12-column sheet where cards run 8+4, 4+8, 4+4+4 (16:10 lead cards sit level with 4:5 tiles). "Selected" is a category with its own template (`category-selected.html`); the current service is highlighted through core's `current-cat` class.
- Case studies: full-width featured image, title and one-line tagline (excerpt) with a three-line facts block (year, services, industry), credits table, next project link.
- Variations: Mono, Pastel (blush + ballpoint blue), Night.
- Core-block limits: the grid spans, aspect ratios and mobile table stacking live in theme.json root CSS because section-style CSS can't hold media queries or selector lists. The Industry filter uses the tag cloud, which has no "current" state, so only the Services row shows the active filter.
- Demo images are public-domain stand-ins (Wikimedia Commons, the Met), credited in readme.txt and the footer.

## Round 2

- Hero is no longer a motto: it opens with the studio name, one fact and what is on the desk this month, then goes straight into the work sheet and a selected-work-by-year list. The old statement stays as an alternative hero pattern without the full stop.
- Image lightbox on globally.
- 53 patterns (was 34). New case-study kit: brief and answer, full-width image, image pair, before and after, client quote, big type sample, deliverables, step-by-step process, what changed, moving version; plus studio photos, press and awards, client FAQ, what to send before a first meeting and selected work by year.
- Four case studies are built from the kit: Casa Ribeiro, Kirkgate Law Library, Leeds Print Fair and Ardsley Tea Merchants, plus Marché Couvert. The rest keep shorter write-ups.
- Tables down to one (the services price list). People and credits are ruled rows.
