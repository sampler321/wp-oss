
---

## Part 5: Shared companion blocks (from the nice-to-haves)

The 310 ideas list 1,574 nice-to-haves between them. The same small touches keep coming back across unrelated trades: a plumber and a bakery both need a "closed for the holidays" bar, and a tattoo studio and a therapist both need "books open / closed". Building each one once, in the `wp-oss-companion` plugin, gives every theme these features at no extra cost and keeps the themes free of functionality code (which the WordPress.org rules require anyway).

Counts are how many nice-to-haves across the 310 ideas each block would cover, from a keyword pass over every Nice-to-haves list. They are approximate, and there is overlap between rows.

| Block | Covers | Count | How it works |
|---|---|---|---|
| **Printable view** | printable menus, price lists, CVs, programmes, care sheets, PDFs | 156 | Print stylesheet per template plus a "Print / Save as PDF" button. No PDF library: the browser does it. |
| **Access info** | step-free access, BSL and captioned sessions, relaxed performances, sensory-friendly hours | 66 | Structured fields (step-free, toilet, hearing loop, quiet hours) rendered as a plain list, with schema.org `accessibilityFeature`. |
| **Customer / community wall** | customer photos, member galleries, "happy tails" | 60 | Query Loop over a `submission` type with moderation, fed by a Jetpack Form with file upload. |
| **Scheduled notice** | holiday closures, announcements, sale notices | 54 | Group block with start and end dates; server-side render skips it outside the window, so no flash of stale content. |
| **FAQ per item** | product and service FAQs | 52 | Core Details blocks in a pattern plus FAQPage schema. |
| **Find us** | directions, parking, bus stops, photo directions | 43 | Pattern: address, OpenStreetMap block, numbered photo steps, transport lines. |
| **Gift options** | gift cards, vouchers, gift notes | 35 | WooCommerce gift note field on checkout and a voucher product pattern. |
| **Credentials row** | registration numbers, insurance, licences | 34 | Repeater of name + number + verify link (e.g. Gas Safe, BACP, Ofsted) rendered as text, not badge images. |
| **Policies** | deposits, cancellations, returns in one paragraph | 28 | Bindable fields shown on booking and product templates. |
| **Aftercare / first visit** | aftercare guides, "what to expect" | 28 | Numbered steps pattern with a printable view. |
| **Stockists / map** | stockists, locations, murals | 28 | `place` type + OpenStreetMap + Query Filter by region. |
| **Structured data** | LocalBusiness, Product, Event, Recipe, Course | 24 | One schema generator reading the same fields the blocks use. |
| **Availability state** | commissions, books, new clients, places, waitlist | 22 | One toggle (open / closed / waitlist) in Site Editor settings. Any block can bind to it, e.g. to swap a form for a waitlist line. |
| **Price list** | rate cards, fee tables, service menus | 19 | Table pattern with tabular figures and a printable view. |
| **Cut-off banner** | "Order by 15 Dec for Christmas", per-region dates | 18 | Scheduled notice with a list of region + date rows; hides each row after its date. |
| **Stock state** | sold out, low stock, back in stock, "N left" | 14 | Woo stock status bound to labels, with honest "Sold out" kept visible. |
| **Lead time** | "booking 3 days ahead", turnaround | 14 | One editable field, shown in header or near forms. |
| **Local units** | cm/in, currency note, time zones for livestreams | 14 | Interactivity API toggle stored in localStorage. |
| **Open now** | hours today, open/closed now | 14 | Hours table with holiday exceptions; the "open now" label is computed in the browser in the site's time zone. |

Nine of these (scheduled notice, cut-off banner, availability state, lead time, open now, stock state, local units, printable view, credentials row) cover roughly a third of all nice-to-haves. **Build those first.**

---

## Part 6: How the library fits together

### Structure
- **Standalone block themes**, one per idea, as Automattic ships them. No parent-child chain, so each can be submitted to WordPress.org on its own.
- **One companion plugin** (`wp-oss-companion`): opt-in content types (Work, Project, Exhibition, Event, Release, Episode, Book, Place, Person, Listing…), the shared blocks above, Block Bindings sources, and schema. Themes check for it and degrade gracefully without it.
- **A shared pattern source**, maintained in the monorepo and copied into each theme at build time, not loaded at runtime. It covers roughly 40% of each theme's patterns: FAQ, find us, price list, policies, credentials, legal pages. Each theme restyles them through its own `theme.json`, so shared structure never means shared look.
- **Monorepo**: `/themes/<slug>`, `/companion`, `/shared-patterns`, `/research`, `/tools`.

### Release gates (CI)
Every theme must pass all of these before release:
1. `copylint` (see `ANTI-AI-WRITING.md`): zero severity-5 findings in patterns, templates, demo content and readme.
2. Anti-vibe lint (see `ANTI-VIBE.md` and the field study): banned fonts, banned hex ranges near Tailwind indigo/violet, gradient text, one global radius, banned section order.
3. **Font registry check** (`FONT-REGISTRY.md`): the display font is unique across the library.
4. The 53-question sniff test, answered in the theme's README by a person.
5. WordPress Theme Check plus the theme review requirements (no functionality in themes, escaping, i18n).
6. Accessibility: axe on every template, keyboard pass, 4.5:1 contrast on every surface token pair, `prefers-reduced-motion` honoured.
7. Performance: no render-blocking web fonts over 2 families, images lazy-loaded, LCP under 2.5s on the demo.
8. Screenshot diff of the demo against the style brief (catches accidental default styling).

### Per-theme build steps
1. Claim a display font in `FONT-REGISTRY.md`.
2. Fill in `docs/voice.md` (the voice sheet in `ANTI-AI-WRITING.md`, section 6).
3. Study the Real-world basis sites and screenshots in `research/screenshots/`.
4. Build `theme.json` tokens from the Style block, then the templates, then the patterns.
5. Write demo content in the owner's voice, then run copylint.
6. Run the release gates.

---

## Part 7: Suggested first wave (20 themes)

Chosen to cover the widest spread of sectors, plugins and companion blocks early, so the shared layer gets tested by very different businesses before scaling up.

| # | Idea | Why in the first wave |
|---|---|---|
| 001 | Illustrator: portfolio + shop | The founding example; WooCommerce, originals with RESERVED state, cut-off banner |
| 016 | Architecture studio | Index/table views, Query Filter, the most typographic of the set |
| 022 | UX designer case studies | Pattern overrides for case-study blocks |
| 038 | Band / solo musician | Events via Advanced Query Loop, EPK, embeds |
| 053 | Hyperlocal news | Editorial layouts, donations, heavy Query Loop use |
| 059 | Coffee roaster | Subscriptions, product attributes, filters |
| 066 | Bakery pre-order | Pickup dates, cut-off timer, allergen matrix |
| 083 | Neighbourhood restaurant | Menu patterns, printable view, open now |
| 091 | Guesthouse / B&B | Booking plugin, rooms, find us |
| 097 | Plumber & heating engineer | Trades pattern set: credentials row, lead time, quote form with photos |
| 111 | Therapist / counsellor | Availability state, calm style, crisis footer |
| 113 | Independent dental practice | Health and trust patterns, access info |
| 119 | Yoga studio | Timetable, class booking |
| 141 | Forest school | Education: term dates, inspection report, parent pages |
| 151 | Indie SaaS | Tests the anti-vibe rules where they are most at risk |
| 168 | Food bank / community pantry | Civic: plain-language, multilingual, "what we need this week" |
| 173 | Amateur football club | Fixtures and results, league tables |
| 205 | Wedding (couple's site) | RSVP, countdown, personal voice |
| 219 | Small museum | Heritage: collections, visit info, accessibility |
| 233 | Niche job board | Directory/board mechanics and front-end submissions |

Once these 20 ship, the shared blocks and patterns will have been used by a shop, a restaurant, a tradesperson, a clinic, a school, a club, a charity, a newsroom, a museum and a person. The next 290 are mostly new content models and new styles on top of a proven base.

---

## Open follow-ups

- **Web search budget.** The session hit its 200-search cap partway through the research. Later batches found sites by following links from verified sites, so some ideas rest on fewer or larger reference sites than intended (noted per batch). Raising `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` and re-running a grounding pass on the thinner entries (pets 245–248, handyman 108, reunion 210, cookbook fundraiser 306) would help.
- **Repeated style direction names.** A few direction names were copied from the spec's examples and appear up to five times ("Warm Scandi minimal", "Soft neo-brutalism"). The briefs underneath differ, but the names should be made unique when each theme is built.
- **Shared accent colours.** 171 unique accents across 201 parsed palettes. `#C8102E` appears seven times. With unique display fonts no two themes share the font + accent + radius combination, but a colour registry alongside the font registry is worth adding.
- **Warm off-white grounds.** The field study found warm off-white + serif heading is now the most common AI-built look. The 310 ideas were checked: Fraunces (018) and Cormorant (019) were replaced, and the four ideas pairing a warm off-white ground with a serif display face (002, 032, 119, 223) were moved to cooler grounds. 57 ideas still use a warm off-white background with a sans or slab display face. That is fine on its own, but each should have a reason in the brief (paper stock, plaster, stone), not a default.
- **Fonts.** `FONT-REGISTRY.md` gives every idea a unique display family (310 of 310, checked by family, not only by name; 213 ideas were reassigned). Before building, look at specimens for the 17 Fontshare faces picked by category tag (listed in the registry notes), and reconsider the weaker fits (146 Press Start 2P, 206 Yanone Kaffeesatz, 175 BenchNine, 298 Aldrich). Another theme's display face still appears as a body or label face in 86 places; that is allowed, but should be reduced where a theme's look depends on it.
- **Screenshots.** A few reference pages sit behind bot checks or age gates. Those captures are marked as blocked in `screenshots/manifest.json` and left out of this document.
