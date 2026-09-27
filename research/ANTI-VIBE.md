# ANTI-VIBE: forbidden traits for our block themes

A catalogue of what makes a website look "vibe-coded", meaning built by prompting v0, Lovable, Bolt, Cursor, Claude and similar tools and shipping the defaults. It also covers the older, non-AI kinds of sameness that trigger the same reaction: template stores, default WordPress and dark-pattern e-commerce. Each trait is banned from every theme in this library unless a written exception is filed for that theme.

Research date: September 2026. The sources are listed at the bottom.

Companion document: `ANTI-AI-WRITING.md` covers AI writing tells in depth. Section 2.11 here is only a short summary for reviewers.

---

## 1. Why this matters

**Trust.** Our buyers are independent creatives and small businesses: a ceramicist, a physio practice, a two-person architecture studio, a bakery. Their site is often the first thing a stranger judges them by. By 2026 most visitors have seen hundreds of AI-generated landing pages, and they recognise the pattern before they read a word. One writer put it this way: a visitor "has already seen forty sites with the same gradient and the same three cards, and the recognition arrives before they read a single word" (CodeMySpec). If a site looks AI-made, visitors assume the business is low-effort, new, or not real. For a small business that assumption costs enquiries. The same reflex fires on fake urgency and fake reviews in shops, and regulators now treat those as unlawful, not just tacky (FTC 2024 rule on fake reviews and testimonials).

**Distinctiveness.** These tells do not come from bad craft. Most vibe-coded sites are "competently built: the spacing is even, the contrast mostly works, nothing is broken" (CodeMySpec). The problem is *sameness*. Models "converge toward generic, 'on distribution' outputs" (Anthropic cookbook, Prompting for frontend aesthetics). They produce "the median of every Tailwind CSS tutorial scraped from GitHub between 2019 and 2024" (DEV, Tailwind indigo-500 piece). Anthropic's own evaluation criteria fail designs showing "unmodified stock components... or telltale signs of AI generation like purple gradients over white cards", and add that "a human designer should recognize deliberate creative choices." That is the bar we set: **every visible decision must look chosen, not defaulted.**

**A fair counterpoint.** Frank Chimero argues that some consistency on the web is healthy: shared patterns "are proof of design patterns that play off of the needs of a common medium, and not evidence of a visual monoculture" (The Web's Grain). We agree. This document does not ban conventions that help people, such as a visible nav, a logo top-left or links that look like links. It bans *defaults that carry no decision*, and patterns borrowed from SaaS that do not fit a bakery.

**The WordPress angle.** Block themes fall into the same trap. A `theme.json` that leaves `defaultPalette`, `defaultGradients` and the default spacing and shadow presets switched on, with one radius, Inter and a violet accent, plus patterns shaped as "hero, three cards, stats, testimonials, pricing, FAQ", is a v0 page in PHP. Over a million sites run Twenty Twenty-Five, and cloning it takes one click in Create Block Theme. Our advantage over generated sites should be the thing they can't fake: a point of view tied to a trade.

**How to use this document.** Each trait uses the form **Trait** `Sx` → Why it reads as AI or generic → Do instead. "Do instead" is written for block-theme authors: `theme.json` tokens, patterns, block styles and template parts.

**Severity scale.**

| | Meaning | Release rule |
|---|---|---|
| `S5` | Instant tell. One of these alone makes a visitor think "AI" or "scam". | Blocks release. No exceptions. |
| `S4` | Strong tell. Two together read as AI. | Blocks release unless a written exception is filed. |
| `S3` | Generic. Adds to the "template" feeling. | Allowed at most twice per theme, and each one must be justified. |
| `S2` | Polish. Noticed by designers, felt by others. | Fix before 1.0. |
| `S1` | Nitpick. | Fix when touching that area. |

---

## 2. Forbidden traits

> **Field study update (Sept 2026, see `ANTI-VIBE-FIELD-STUDY.md`).** Measured on 65 live AI-built pages: purple has faded (3/65 use an indigo or violet accent). The current AI default is a **warm off-white background with a serif heading face** (22/65: Fraunces, Playfair Display, Cormorant Garamond, Instrument Serif), often with a gold button, Tailwind (61/65), shadcn tokens (55/65), Lucide icons (45/65), Inter body text (31/65), H1 tracking of exactly -0.025em (18/65) and content hidden until scroll (40/65). Em dashes appear at 6.56 per 1,000 words (17.6 on Bolt) against 0 on the 12 hand-built control pages. A hex blacklist alone catches little; the combination is the tell.

### 2.1 Colour

**C1. Indigo/violet as the primary accent (Tailwind `indigo-500` #6366F1, `violet-500` #8B5CF6, shadcn violet).** `S5`
→ This is the loudest single AI tell. Tailwind UI shipped indigo buttons, and that choice spread through tutorials into training data. Adam Wathan publicly apologised for it in 2025. Developers Digest calls the lavender version "VibeCode Purple."
→ Derive the accent from the trade's materials: kiln-fired oxide red, surgical teal, chalkboard green, brass. Write the reason next to the hex in `theme.json` (`"slug":"accent","name":"Oxide"`). Every theme's accent must be at least 30° of hue away from 245–275°, or the theme needs a written exception.

**C2. Purple-to-blue or purple-to-pink gradients (hero backgrounds, buttons, headline text).** `S5`
→ These came from Notion, Linear and Vercel marketing plus Tailwind's `from-indigo-500 to-purple-600`. Anthropic's skill blog names "purple gradients on white backgrounds" as the canonical cliché.
→ Use flat colour fields. If a theme truly needs a gradient, make it a two-stop gradient between adjacent hues from its own palette, used in one place only, never on text.

**C3. Gradient text on headlines or big numbers (`bg-clip-text text-transparent`).** `S5`
→ Impeccable lists it as decoration that carries no information, and it appears on nearly every generated hero.
→ Headline text is one solid colour. Create emphasis with size, weight or placement.

**C4. Radial glow / "halo" / spotlight behind the hero on a dark page.** `S4`
→ "A bright halo on a dark page is a familiar AI background effect" (Impeccable). It is the "Linear effect" formula of dark background, blurred gradient and glow.
→ If a surface needs atmosphere, use a real photograph, a paper/print texture, or a flat colour block with a strong edge.

**C5. Blurred colour orbs/blobs floating behind content.** `S4`
→ This is decoration standing in for an idea (VibeMole: "blurred orbs, neon borders as shortcuts for 'modern'").
→ Ban `filter: blur()` on decorative elements. Empty space stays empty, or holds real content.

**C6. Coloured glows and coloured box-shadows (`shadow-purple-500/50`, neon borders).** `S4`
→ Developers Digest #8 and Fountain Institute #2 trace this to crypto and gaming sites in the training data.
→ Shadows, when used, are neutral: a tinted near-black at low opacity, one elevation level, and only on things that actually float (menus, modals).

**C7. Default permanent dark mode with neon accents (cyan/violet on #0A0A0A).** `S4`
→ Dark mode is used to hide weak structure: "gradients and glow create drama without explaining the product" (VibeMole). Impeccable lists "dark mode with glowing accents."
→ Default to light for nearly all small-business themes. A dark theme needs a trade reason, such as a tattoo studio, cinema or night bar, and must get its depth from type and surface steps, not glow.

**C8. Untouched zinc/slate neutral ramp.** `S3`
→ This is the stock shadcn neutral scale from background to border to muted text. It is instantly generic (ux-skill).
→ Tint neutrals toward the accent's temperature: warm greys for craft and food, cool greys for clinical and technical. Each theme defines its own 5–7 neutrals.

**C9. Mid-grey body text on dark, or light-grey text on white (fails WCAG AA).** `S4`
→ Developers Digest #6 and Sinton both list this. Generated themes pick grey for "sophistication" and never measure it.
→ Body text contrast must be 7:1 or higher (AAA). Secondary text must be 4.5:1 or higher. Check every palette combination the theme exposes in `theme.json`, not only the defaults.

**C10. Cream #F4F1EA + serif + terracotta #D97757 as the "tasteful" escape hatch.** `S4`
→ Anthropic's frontend-design skill names this exact combination as one of five clustering AI defaults. It is what models produce once they are told "not purple." Impeccable separately flags "cream / beige palette" as a substitute for a considered palette.
→ Cream is allowed only if the theme's brief names a physical reason, such as paper stock or unbleached linen. It must not be paired with terracotta unless the business actually works in clay.

**C11. Near-black background with one acid-green or vermilion accent.** `S3`
→ This is another of Anthropic's five named defaults. It is the "edgy" fallback.
→ See C7. If a theme is dark, its accent comes from its subject matter, not from being loud.

**C12. Rainbow of equal-weight accent colours (each card a different hue).** `S3`
→ "Everything is shouting at equal volume" (Fountain Institute #1, #6).
→ Use one dominant colour, one accent and neutrals. The accent marks one kind of thing, such as links and primary actions, and never decorates.

**C13. Grey text on a coloured background.** `S2`
→ Impeccable: neutral grey reads as washed out on coloured surfaces.
→ On a coloured band, text is either the palette's darkest ink or pure base (white or paper). Define `color.duotone`-style pairs per section style.

**C14. Colour-coded "status dots" with no status behind them.** `S3`
→ "The model extracted 'colored dot equals status' from developer tools but lost the functional context" (Fountain Institute #7).
→ No dots unless they encode a real state, such as "Open now" driven by real opening hours. Pair a dot with a text label.

**C15. Timid, evenly distributed palette (five colours used in equal amounts).** `S3`
→ Anthropic's cookbook: "Dominant colors with sharp accents outperform timid, evenly-distributed palettes."
→ Pick a dominant field colour that covers most of the page, and keep the accent to under about 5% of the pixels.

**C16. Untinted pure #FFFFFF page with #000 or #111 text and nothing in between.** `S2`
→ This is the zero-decision default of every scaffold.
→ Tint the base and ink by a few percent toward the palette's temperature. Even "white" themes pick a specific white.

**C17. Links that aren't distinguishable from body text (same colour, no underline).** `S3`
→ NN/g: with weak signifiers users spent "22% more time" on pages. Links are recognised as long as they are "presented in a contrasting color."
→ Links in prose are underlined, with `text-underline-offset` tuned to the face, or are a contrasting colour at 3:1 against the body text.

### 2.2 Typography

**T1. Inter for everything (body, display, logo).** `S5`
→ This is the most-cited tell in every source. Anthropic's skill blog: "Never use: Inter, Roboto, Open Sans, Lato, default system fonts." CodeMySpec: "Anything other than Inter clears the most common tell in a single move."
→ Inter, Roboto, Open Sans, Lato, Arial, Poppins, Montserrat and bare `system-ui` are banned as the primary face. Each theme bundles one or two faces chosen for its trade and records the reason in the theme README.

**T2. The second-tier AI font kit: Geist, Space Grotesk, Instrument Serif, Playfair Display, DM Sans.** `S4`
→ Developers Digest #2: these pairings "appear constantly." Anthropic's cookbook admits Claude tends "to converge on common choices (Space Grotesk, for example) across generations."
→ No two themes in the library share a display face. Keep a registry in `research/FONT-REGISTRY.md`. Prefer less-seen, properly licensed OFL faces, and check each one has real italics and figures.

**T3. One italic serif word inside a sans headline ("Build *beautiful* websites").** `S5`
→ Anthropic's skill: "Accenting just a single word or phrase in a headline, like putting one word in italic/bold or a different color." Developers Digest #3.
→ Headlines are typographically uniform. If emphasis is needed, rewrite the sentence.

**T4. Oversized italic serif display headline as the shortcut to "editorial."** `S3`
→ Impeccable: "a familiar shortcut to an editorial look."
→ An editorial theme earns the look through a real grid, captions, bylines, pull-quotes and running heads, not only a big italic.

**T5. Tracked-out ALL-CAPS eyebrow label above every heading ("FEATURES", "HOW IT WORKS").** `S5`
→ Anthropic names "a tracked-out ALL-CAPS eyebrow label above every heading" as template chrome. Impeccable: "Label above a heading." Developers Digest #16.
→ No eyebrows by default. If a pattern uses one, it must carry information the heading does not, such as a date, category or location. At most one per page.

<!-- copylint-off -->
**T6. Pill badge above the hero H1 ("✨ New: v2.0 is here →").** `S5`
<!-- copylint-on -->
→ Developers Digest #10, Impeccable "Badge above the main headline", CodeMySpec #2.
→ Remove it from every hero pattern. Put real news, such as "Booking now for spring", in body copy or in a dated notice block.

**T7. Centred hero H1 in a geometric sans, two lines, with a grey subline and two buttons underneath.** `S4`
→ Developers Digest #9: "the default layout for AI-generated pages."
→ Hero patterns should be left-aligned or asymmetric, lead with an image or work sample, and have one action. Any centred hero must be justified by the content, for example a single wordmark over a full-bleed photo.

**T8. Flat hierarchy: H1 through H3 at 1.2–1.5× steps, weights 400 vs 600.** `S3`
→ Anthropic's skill blog recommends "extremes: 100/200 weight vs 800/900, not 400 vs 600. Size jumps of 3x+, not 1.5x." Impeccable lists "Flat type hierarchy."
→ Every theme defines a deliberate `fontSizes` scale with at least one dramatic jump (display to body of 4× or more), plus a distinct small-text style for captions and meta.

**T9. Crushed negative tracking on big headings (`tracking-tighter` everywhere).** `S2`
→ Impeccable: "Crushed letter spacing." It is the default Tailwind/Vercel look.
→ Set tracking per face and per size, based on the face's own spacing. Do not apply `-0.04em` globally.

**T10. One font family for everything with no second voice.** `S3`
→ Impeccable: "Single font for everything."
→ Pair two faces, or use one superfamily that includes a real contrasting cut (a mono, condensed or serif). Anthropic suggests "display + monospace, serif + geometric sans."

**T11. Tiny UI text (12–13px nav and buttons) and body under 16px.** `S3`
→ Impeccable: "Tiny interface text", "Tiny body text."
→ Body text is 17–20px minimum, depending on the face's x-height. Nav and buttons are 15px or larger.

**T12. Line length running full container width (100+ characters).** `S3`
→ Impeccable: over 75 characters. Sinton: "awkward line lengths." The WordPress layout docs recommend about 45–75 characters.
→ Set `contentSize` so prose runs 60–72ch. Wide layouts are for images, not paragraphs.

**T13. Tight line-height on body, or loose line-height on display.** `S2`
→ Impeccable "Tight line height." Generated CSS leaves `leading-normal` everywhere.
→ Body line-height is 1.5–1.7. Display line-height is 0.95–1.15, tuned per face.

**T14. Justified text.** `S2`
→ Impeccable: it leaves "distracting word gaps."
→ Ragged-right only.

**T15. Em-dash-heavy headings and taglines.** `S4`
→ Impeccable: "A dash in every sentence is a familiar AI writing habit." Wikipedia's Signs of AI writing lists "overuse of em dashes."
→ No em dashes in pattern demo copy. Use full stops, commas or colons.

**T16. A Google Fonts top-10 face as the primary voice (Roboto, Open Sans, Poppins, Montserrat, Lato).** `S3`
→ The 2024 Web Almanac puts Roboto on 15.2% of desktop sites, Open Sans on 5.6–6.8%, Poppins on 4.7–5.8% and Montserrat and Lato on over 3% each. Inter was at about 1% and "expected to rise into the top 10" because frameworks default to it. A face on every twentieth site cannot carry a brand.
→ See T1 and T2. Check any candidate face against the Web Almanac top list before adopting it.

**T17. Icon fonts (Font Awesome, Material Icons) for UI glyphs.** `S3`
→ Icon fonts are about 18% of all web fonts, and Font Awesome is on 10–12% of sites (Web Almanac 2024). The glyph shapes are instantly familiar, and they fail when the font fails to load.
→ Use inline SVG, drawn to the theme's stroke weight, with `aria-hidden` and a text label.

**T18. Faux bold and faux italic (browser-synthesised styles because the weight or italic file was not bundled).** `S3`
→ A scaffold only loads 400 and 700. Synthesised italics slant the roman and look cheap to anyone who reads type.
→ Bundle a true italic for every text weight in use, and set `font-synthesis: none` in the theme's global styles.

**T19. Headings are just the body face in bold.** `S3`
→ This is what a theme looks like when nobody set heading styles. WordPress's own developer blog argues typography should be the site's "statement piece."
→ `styles.elements.heading` (and `h1`–`h6`) gets a display face or cut, its own tracking and its own line-height.

**T20. Title Case On Every Heading And Button.** `S2`
→ Wikipedia's Signs of AI writing lists "title case in headings" as a tell. It also reads as American SaaS house style for European small businesses.
→ Sentence case for headings and buttons, unless the brand voice explicitly calls for otherwise.

**T21. Inline bold scattered through body copy for "scannability".** `S2`
→ Wikipedia lists "overuse of boldface" as a sign of AI writing.
→ At most one bolded phrase per section, and only for a fact people are scanning for, such as a price, a date or a deadline.

**T22. Unbalanced headline wraps (one-word last lines, orphaned "a" or "&").** `S2`
→ Generated CSS never sets wrapping, so every heading has a widow.
→ Set `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs in global styles, and review every pattern at three widths.

### 2.3 Layout & composition

**L1. The canonical page sequence: hero → logo strip → features grid → how it works → stats → testimonials → pricing → FAQ → CTA band → footer.** `S5`
→ CodeMySpec #4 and VibeMole #2: "Identical layout rhythm... with equal visual weight."
→ Each theme's front page is built from the trade's real questions. A florist's page is orders, seasons and delivery area. A therapist's is approach, fees and first-session logistics. No theme ships all of these sections in this order.

**L2. Three (or six) identical feature cards: icon tile, bold title, two grey lines.** `S5`
→ This is the single most-cited layout tell (925 Studios Tell 3, Developers Digest #12, Impeccable "Identical card grids", VibeMole #8).
→ Use lists with real hierarchy, where one item leads and the others support it. Alternatives are a definition list, a two-column prose block, or an image-led row. If a grid is truly needed, vary the spans.

**L3. Bento grid of rounded boxes.** `S4`
→ This has been the default "modern" layout since Apple keynotes.
→ Use a real editorial grid with columns and gutters where content spans it naturally. No rounded tiles.

**L4. "01 / 02 / 03" numbered steps or section numbers when the content isn't a sequence.** `S4`
→ Anthropic's skill: numbered markers are "only appropriate if the content actually is a sequence." Developers Digest #13, Impeccable "Tiny numbered section labels."
→ Number only real procedures, such as "How a commission works." Otherwise use no numbers.

**L5. Stat banner: "10k+ customers · 99.9% uptime · 24/7 support · 5★".** `S5`
→ Developers Digest #14, Impeccable "Hero metric layout." For small businesses these numbers are usually invented.
→ No stat-row pattern ships in the library. If a real figure matters ("Since 1987", "412 weddings"), set it inside a sentence.

**L6. Cards nested in cards (section card → glass panel → feature card → icon square).** `S4`
→ Fountain Institute #5, VibeMole #1, Impeccable "Nested cards."
→ Maximum one level of container. Group with whitespace, rules and alignment.

**L7. Everything chopped into cards ("SaaS-card kit").** `S4`
→ Anthropic names "content chopped into identical rounded cards, one border-radius on everything" as a default cluster.
→ Default to uncontained content on the page ground. Cards are for independently actionable items only, such as a product or an event.

**L8. Monotonous spacing: identical gap between every section and every element.** `S3`
→ Impeccable "Monotonous spacing." Generated sections are all `py-24`.
→ Define a spacing scale with purpose. Related items sit tight and section breaks vary. Headings sit closer to what follows them than to what came before (Impeccable: "Heading closer to the previous section").

**L9. Everything centred.** `S3`
→ Centred text is the "safe" choice and reads as having no opinion.
→ Use a left-aligned default reading axis. Centre only short, standalone moments.

**L10. Symmetric max-width column with nothing breaking out.** `S3`
→ It is predictable. Anthropic's skill asks for "unexpected spatial composition."
→ Each theme uses at least one deliberate break: full-bleed image, hanging captions, off-grid pull quote, or asymmetric columns such as 5/7 or 3/9.

**L11. Split hero: text left, floating dashboard/mockup screenshot right, tilted in 3D.** `S4`
→ This is SaaS default. Small businesses have no dashboard, so it gets faked.
→ Hero shows the actual work: a product, a space, a face, a plate.

**L12. Logo cloud "Trusted by" row of greyscale logos.** `S4`
→ It is fake proof for a small business (VibeMole #11).
→ No logo-cloud pattern. Clients can be named in running text with a link.

**L13. Pricing as three cards with the middle one "Most popular" and scaled up.** `S4`
→ This is SaaS template chrome, and it looks wrong for a hairdresser or a photographer.
→ Pricing patterns are a price list, a menu, a table of rates, or "from €X" in prose, which is what the trades actually use.

**L14. FAQ accordion with chevrons as the default closer.** `S3`
→ It is on every generated page and hides content from search and skimming.
→ FAQ is optional. When used, render questions as visible `h3` headings with answers, or use `details` styled in the theme's own voice.

**L15. Full-width gradient "Ready to get started?" CTA band before the footer.** `S4`
→ This is one of the most predictable section shapes.
→ End pages with the actual next step inline: address and hours, booking link, email.

**L16. Mega footer with four link columns for a five-page site.** `S3`
→ It copies SaaS scale that a small business doesn't have.
→ The footer holds what people look for there: address, hours, phone, email, social links and legal. One or two rows.

**L17. Hamburger menu on desktop.** `S4`
→ NN/g measured desktop users as "at least 39% slower" with hidden navigation, with more than a 20% drop in discoverability. "The hamburger menu is not appropriate for desktop websites."
→ Visible nav at desktop widths. On mobile, hide the nav only when there are more than about four top-level links, and label the toggle "Menu".

**L18. Auto-rotating hero slider/carousel.** `S4`
→ NN/g: an offer in a rotating carousel was visible 20% of the time, and "because it moves, users automatically assume that it might be an advertisement."
→ One hero image or a static grid. If a gallery is needed, it is user-driven, with visible controls.

**L19. Scrolljacking: pinned "scroll-to-experience" storytelling, horizontal-scroll sections.** `S4`
→ NN/g found most participants were disoriented, and some took the scrolljack for a bug. Their advice: never change scroll direction, and skip it on mobile.
→ Native scroll only. Stories are told with image and caption sequences in normal flow.

**L20. Everything sticky: header, announcement bar, CTA bar, chat bubble and cookie bar all fixed.** `S3`
→ On a phone this can leave a third of the viewport for content. It is a sign of stacked plugins rather than design.
→ At most one sticky element (usually a compact header), and it must shrink or hide on scroll down.

**L21. 100vh hero holding only a slogan and a button, with nothing useful above the fold.** `S3`
→ NN/g: users ignore "big feel-good images that are purely decorative."
→ The first screen shows what the business is, where it is and one real piece of work. Let the next section peek above the fold.

**L22. Zig-zag "image left, text right, then swap" sections repeated three or more times.** `S3`
→ This is the default rhythm of page builders and AI generators alike.
→ Vary the section shapes: a full-bleed image, a text-only section, a two-up, a list. No two consecutive sections share a structure.

### 2.4 Components

**K1. One border radius on everything (`rounded-xl`, 12–16px, on buttons, cards, inputs, images).** `S4`
→ Anthropic's "one border-radius on everything", CodeMySpec "Soft everything", Impeccable "Extreme border-radius on cards."
→ Radius is a decision per element class, recorded in `settings.border.radiusSizes` (WordPress 6.9+). Many themes should use 0–2px. Images are never rounded by default.

**K2. Pill-shaped buttons plus a ghost secondary button beside them.** `S3`
→ This is the stock hero CTA pair.
→ One primary action per view. Button shape follows the theme's geometry. A secondary action is a text link.

**K3. Glassmorphism cards (`backdrop-blur`, white/10 fill, 1px white/20 border).** `S5`
→ Developers Digest calls it an LLM default that "persists despite losing contemporary relevance." Impeccable lists "Glassmorphism everywhere."
→ Banned outright except for a sticky header over imagery, where it has a legibility job.

**K4. Coloured left/top border stripe on cards.** `S5`
→ "The colored-left-border card is almost as reliable a sign of AI-generated design as em-dashes for text" (Developers Digest #11). Impeccable: it "turns an ordinary card into something that looks like an alert."
→ Stripes are reserved for real notices, such as a closure alert, and are defined as a single `core/group` block style.

**K5. Hairline border plus wide soft shadow on the same card.** `S3`
→ Impeccable: two treatments defining one edge.
→ Pick one edge treatment per theme: rule, fill or shadow.

**K6. Icon in a rounded square tile above a heading.** `S4`
→ Impeccable "Icon tile stacked above heading." It is the atom of the L2 grid.
→ No icon tiles. If an icon helps, it sits inline with the text at text size.

**K7. Hover lift on every card (`hover:-translate-y-1 hover:shadow-xl`).** `S4`
→ Anthropic: "hover transitions on every card are the generic default." SmoothUI: "a bounce on every hover."
→ Hover changes only things that are clickable, and only in ways that confirm clickability, such as an underline, a colour shift or a cursor change.

**K8. Stock shadcn/Radix-looking inputs: 40px tall, zinc border, violet ring on focus.** `S3`
→ This is recognisable at a glance (ux-skill, freedesignmd).
→ Style forms in the theme's voice, such as underline-only fields, a heavier border, or a paper-form look. Labels always sit visibly above fields. Theme the error and required states (925 Studios / prg.sh: missing validation states).

**K9. Toggle for dark/light mode on a brochure site.** `S3`
→ It is a developer habit shipped to people who never asked for it.
→ No theme toggle. Themes may respect `prefers-color-scheme` if they ship a designed dark palette.

<!-- copylint-off -->
**K10. Announcement bar with an arrow ("🎉 We just launched X →").** `S3`
<!-- copylint-on -->
→ It is template chrome, and for a small business it usually says nothing.
→ Only provide a notice-bar pattern that is clearly for operational info (holiday closure) and is off by default.

**K11. Testimonial carousel with avatar circle, five yellow stars, name and title.** `S4`
→ It is shared by every template, and the content is usually invented (see P3).
→ Testimonials are set as quotations with full attribution and context ("Marta, commissioned a dining table, 2025"). No carousels.

**K12. Tabs or segmented controls on marketing pages.** `S2`
→ This is app UI imported into brochure content, and it hides content.
→ Show content in sequence.

**K13. Floating round "back to top" button.** `S2`
→ It is a plugin default that competes with the chat bubble and the cookie bar in the same corner.
→ Put a plain "Back to top" text link in the footer, if one is needed at all.

**K14. Overlapping avatar stack with "Join 2,000+ happy customers".** `S4`
→ This is a SaaS social-proof widget, and the faces are usually stock or AI.
→ Banned. Real proof is a named quote or a photo of a real client, used with permission.

**K15. Command-K search palette or site search on a five-page site.** `S3`
→ It is app chrome on a brochure site.
→ No search UI unless the site has a blog or shop with more than about 30 items.

**K16. "Stay in the loop" newsletter box: one pill input, one button, a line of fine print.** `S3`
→ It is on every template, whether or not the business sends newsletters.
→ The newsletter pattern is opt-in, and it says what arrives and how often: "A letter when the kiln opens, about four times a year."

### 2.5 Iconography & imagery

**I1. Lucide (or Heroicons outline) icons everywhere, 24px, 2px stroke.** `S4`
→ It is part of the fingerprint stack "Next.js + Tailwind + shadcn + Lucide + Radix" (AI Website Detector). 925 Studios calls the result "interchangeable thin-line icons."
→ Default to no icons. Where icons are functional (phone, map pin, cart), use a set drawn or chosen to match the typeface's stroke and terminals, and document it per theme.

<!-- copylint-off -->
**I2. Emoji as icons or in headings (🚀 ✨ ⚡ 🔥 💡).** `S5`
<!-- copylint-on -->
→ Anthropic's skill lists "emojis as icons". Fountain Institute #3, Developers Digest #15, CodeMySpec #6.
→ No emoji in any pattern, template, heading, nav or demo content.

**I3. Sparkles icon to mean "AI" or "magic".** `S5`
→ It is the universal AI-product glyph.
→ Never used.

**I4. Abstract 3D renders: glossy blobs, isometric glass shapes, gradient spheres.** `S4`
→ These are decoration with no subject.
→ Imagery is photographic or illustrative of the trade.

**I5. AI-generated stock people.** `S5`
→ Visitors increasingly read these as fake, and for a business built on real people that destroys trust. See section 2.10 for the specific tells.
→ Demo content uses real, licensed photography of the kind of work the trade does (hands, tools, materials, spaces). Every pattern's image slot is sized for a real photo aspect ratio.

**I6. Unsplash cliché stock: laptop-and-latte flatlay, mountain at dawn, handshake.** `S4`
→ NN/g: users "ignore stock photos of generic people," but spend more time on real staff portraits than on the bios next to them.
→ See I5. Curate demo photography per theme around one trade.

**I7. Rough or placeholder SVG illustrations: circles and blocks, "undraw"-style people, crude mascots.** `S4`
→ Impeccable: "Placeholder-style illustrations," "Rough SVG illustrations."
→ No generic spot illustrations. If a theme uses illustration, it is one coherent commissioned or hand-made style.

**I8. Decorative dot-grid or line-grid backgrounds.** `S4`
→ Impeccable: "A decorative grid adds lines without helping people use the page."
→ Banned. Backgrounds are flat, textured with purpose (paper, linen), or photographic.

**I9. Repeating diagonal stripes or noise to fill empty space.** `S3`
→ Impeccable "Repeating-gradient stripes."
→ Empty space is allowed to be empty.

**I10. Images under near-opaque overlays so text can sit on them.** `S3`
→ Impeccable "Images hidden under overlays." It is also the default WordPress Cover block look (see WP16).
→ Put text beside images, or choose images with a genuinely calm area. Overlay opacity must be 40% or less.

**I11. Jagged/torn/blob image masks.** `S3`
→ Impeccable "Jagged image masks."
→ Rectangular images, or one deliberate shape that belongs to the brand.

**I12. Rounded-corner images with drop shadows.** `S3`
→ These are cards in disguise.
→ Images sit flat, with square corners by default.

**I13. Default favicon (Vite, Next, WordPress "W") or emoji favicon.** `S4`
→ It is an instant "nobody finished this" signal.
→ Every theme ships a site-icon placeholder that looks designed and prompts replacement in onboarding.

### 2.6 Motion

**M1. Fade-and-slide-up on every section as it scrolls into view.** `S4`
→ Anthropic: "fade-and-slide-up entrances on each section... are the generic default."
→ No scroll-reveal by default. If a theme has motion, use one orchestrated moment, such as the page-load sequence Anthropic's cookbook recommends ("one well-orchestrated page load with staggered reveals").

**M2. Content hidden until JS animation fires (`opacity:0` in CSS).** `S5`
→ Impeccable: "Content stuck waiting to appear." It breaks without JS, in print, and for crawlers.
→ Content must be visible with JS off. Motion only enhances.

**M3. Bounce/elastic/overshoot easing on routine UI.** `S3`
→ Impeccable "Bounce or elastic easing."
→ Use short ease-out (150–250ms) for state changes. No springs on menus or modals.

**M4. Pulsing status dot or pulsing "Live" badge.** `S4`
→ Impeccable: it "draws attention even when nothing changes." VibeMole #12.
→ Banned.

**M5. Infinite animated gradient borders / shimmer / "beam" effects.** `S5`
→ VibeMole #12: "motion to prove the site is alive."
→ Banned.

**M6. Auto-scrolling logo marquee or testimonial marquee.** `S4`
→ Impeccable "Auto-scrolling marquee."
→ Banned.

**M7. Typewriter headline with a blinking cursor.** `S4`
→ Impeccable "Decorative blinking cursor."
→ Banned.

**M8. Image zoom/rotate on hover.** `S3`
→ Impeccable "Images that move on hover."
→ Images do not move on hover unless they open a larger view, and then the cursor says so.

**M9. Animations that shift layout (animating height, padding, margin).** `S3`
→ Impeccable "Animation that changes layout." It causes CLS.
→ Animate only `opacity` and `transform`.

**M10. Ignoring `prefers-reduced-motion`.** `S4`
→ This is a code-level tell of shipping defaults.
→ Every motion rule sits inside `@media (prefers-reduced-motion: no-preference)`.

**M11. Count-up animation on numbers ("0 → 1,200 happy clients").** `S4`
→ It is the motion partner of the stat row (L5), and it makes invented numbers look even more invented.
→ Banned. Numbers appear as text.

**M12. Custom cursor, cursor-follower blob, or magnetic buttons.** `S3`
→ It is agency-showreel motion copied onto sites where it gets in the way.
→ Native cursor. A portfolio theme may add one cursor behaviour, only if it has a job, such as a "View" label over project images.

**M13. Parallax on every image.** `S3`
→ It is a template default that makes pages feel floaty and triggers motion sickness.
→ No parallax by default. At most one image per page may use it, and only when `prefers-reduced-motion` allows it.

**M14. Preloader or splash animation before the site appears.** `S3`
→ It spends the visitor's time on the site's vanity.
→ No preloaders. Fonts use `font-display: swap`, and pages render progressively.

<!-- copylint-off -->

### 2.7 Copy / voice

**V1. Verb-soup hero: "Unlock / Empower / Supercharge / Transform / Elevate your ___".** `S5`
→ CodeMySpec #7, VibeMole #5, Impeccable "Generic marketing claims."
→ Pattern demo copy must name a trade, a place and a concrete offer: "Hand-thrown tableware from a studio in Ghent. Commissions open in March."

**V2. Formulaic section headers: "Everything you need to…", "Built for…", "Simple, fast, reliable".** `S4`
→ VibeMole #6: read it aloud, and if it fits any business, rewrite it.
→ Headings state facts: "Opening hours", "What a first session costs", "Where to find us".

**V3. Two-beat slogans: "Build faster. Ship smarter." / "Not a tool. A platform."** `S4`
→ 925 Studios Tell 4, Impeccable "Forced contrast."
→ No slogan patterns. Write one plain sentence.

**V4. Rule-of-three adjectives ("fast, beautiful, and reliable").** `S3`
→ This is an LLM cadence (Wikipedia, Signs of AI writing: "Rule of three").
→ Pick the one claim you can prove.

**V5. "Seamless", "robust", "cutting-edge", "world-class", "next-level", "game-changer", "effortless".** `S4`
→ These are the house words of generated copy.
→ Maintain a banned-words list in the demo-content lint (see checklist and `ANTI-AI-WRITING.md`).

**V6. Vague CTAs: "Get started", "Learn more", "Explore".** `S4`
→ Sinton: "Buttons that do not say what happens next." NN/g: "users don't know what to expect if they click." Screen-reader users hear a list of identical "Learn more" links.
→ CTAs name the action and its result: "Book a fitting", "Order by Thursday for Saturday", "Email the studio".

**V7. Features named as abstractions ("Seamless Integration", "Smart Analytics").** `S3`
→ CodeMySpec #7.
→ Name the thing: "We deliver within 10 km of Utrecht", "Invoices in English and Dutch".

**V8. Calling things "theater", "the real magic", "here's the thing".** `S3`
→ Impeccable lists "theater". These are LLM rhetorical tics.
→ Cut them.

**V9. Apologetic or cute error and empty-state messages ("Oops! Something went wrong 😅").** `S3`
→ Anthropic's skill warns against errors that "apologize" and "vague" failure messaging.
→ State what happened and what to do: "That page moved. Try the shop or search below."

**V10. Same text repeated inside one container (label, heading and button all say "Contact").** `S2`
→ Impeccable "Same text repeated inside one container."
→ Each line of copy does "exactly one job" (Anthropic).

### 2.8 Content / placeholder

**P1. Lorem ipsum, "Your headline here", "Feature one", "Acme Inc."** `S5`
→ Sinton: placeholder text is a vibe-coded tell.
→ All demo content is written for the theme's named persona (a real-sounding but clearly fictional business in the target trade).

**P2. Invented metrics ("10,000+ happy customers", "98% satisfaction").** `S5`
→ VibeMole #11: fake evidence erodes credibility.
→ Demo content contains no statistics.

**P3. Fabricated testimonials ("Sarah Johnson, Marketing Lead").** `S5`
→ "Sarah Johnson" has become a meme for AI testimonials (Alibaba insights piece). Since 2024 the FTC rule bans testimonials that "misrepresent that they are by someone who does not exist."
→ Testimonial demo content is marked plainly as sample text in the editor. It is specific and modest, with no job titles for B2C trades.

**P4. "Trusted by" logos of fictional companies.** `S5`
→ This is fake proof.
→ See L12.

**P5. Links to `#`, social icons pointing nowhere, the old Twitter bird.** `S4`
→ Sinton: "non-functional sample links."
→ Social-links block ships empty with an editor hint. No dead links in any template.

**P6. "© 2024 Company Name. All rights reserved." hard-coded.** `S3`
→ It is stale the moment it ships.
→ Use a dynamic year via block binding or a simple shortcode-free pattern. Use the site title, not "Company."

**P7. "Made with ❤️ by…" footers.** `S3`
→ Emoji plus the generator's voice.
→ Banned.

**P8. Nav that reads "Features · Pricing · About · Contact" on a non-software business.** `S4`
→ These are SaaS nav defaults.
→ Nav demo uses the trade's words: "Work · Commissions · Studio · Visit".

**P9. Blank or broken image slots.** `S4`
→ Impeccable "Broken or placeholder image."
→ Every image slot in every pattern has a real demo image and a sensible `alt` placeholder instruction.

<!-- copylint-on -->

### 2.9 Code-level tells visible to users

**X1. Default browser or Tailwind focus ring (blue glow, or `ring-2 ring-offset-2` violet).** `S4`
→ It shows nobody designed the keyboard state. Missing focus states are also an accessibility tell (SmoothUI, Sinton).
→ Each theme designs a focus style in its own palette: a 2px or thicker outline with offset, and 3:1 contrast or better against adjacent colours. Test it on every surface colour.

**X2. Identical radius/shadow tokens across all themes in the library.** `S4`
→ The library itself becomes the new "shadcn look."
→ CI check: no two themes may share the same (display font, accent hex, radius scale) triple.

**X3. `transition: all 0.3s` on everything.** `S2`
→ It produces sluggish, generic motion and repaint-heavy hovers.
→ Transition named properties only, with durations per interaction type.

**X4. Hover = `opacity: 0.8`.** `S2`
→ This is the cheapest possible hover.
→ Design hover states per component.

**X5. Horizontal scroll or overflow on mobile; cards flush to the viewport edge.** `S4`
→ Sinton "Shaky mobile layouts", Impeccable "Content overflowing its container", "Body text touching the page edge."
→ Test at 320px. Root padding must use `useRootPaddingAwareAlignments`.

**X6. Skipped heading levels (hero H1 → card H3) and multiple H1s.** `S3`
→ Impeccable "Skipped heading level." Sinton "thin heading structure."
→ Patterns declare heading levels intentionally. One H1 per template.

**X7. Buttons that are `div`s, icons with no labels, images without alt.** `S4`
→ Sinton "Accessibility gaps."
→ Use core blocks. Icon-only controls get `aria-label`. Every pattern image has an alt-text strategy.

**X8. Heavy JS for a brochure site (animation libraries, carousels, client-side everything).** `S3`
→ Sinton: "AI-generated code is often heavier than necessary."
→ Block themes ship zero front-end JS by default. Interactivity API only where core blocks need it.

**X9. Web fonts loaded from Google's CDN with FOUT on every visit, or 6+ weights.** `S3`
→ Slow and privacy-hostile (GDPR matters for our EU buyers). The Web Almanac shows self-hosting has become the majority practice.
→ Self-host via `theme.json` `fontFace`, subset, and keep to 4 or fewer files.

**X10. Default selection colour, default scrollbar, default `<hr>`, default blockquote.** `S2`
→ These small defaults add up to "unfinished."
→ Style `::selection`, `core/separator`, `core/quote`, `core/pullquote`, `core/table` and `core/code` in every theme.

**X11. Unstyled empty/404/search-no-results templates.** `S3`
→ SmoothUI: "undesigned states."
→ Every theme ships designed `404.html`, `search.html`, and empty-archive states with voice-appropriate copy.

**X12. Missing meta basics: identical titles, missing meta descriptions, missing OG images.** `S3`
→ Sinton "Missing SEO basics."
→ Theme docs specify the OG image pattern. Templates output sensible title parts. Don't hard-code SEO; leave room for plugins.

### 2.9b Additions from Hacker News and Reddit

Adrian Krebs ran a DOM and computed-style scanner over about 1,590 Show HN submissions. **22% showed four or more AI design patterns** and a further 32% showed two or three. The HN thread on it (235 comments) and an earlier "Tell HN" thread on "LLM house style" added the tells below. His line: "There is a difference between trying to craft your own design and just shipping with whatever defaults the LLMs output."

**H1. The "console-ish" monospace as the default "technical" voice.** `S3`
→ HN commenter toraway on "the console-ish font Claude seems to love as a default". It has become the third AI font default after Inter and the italic serif.
→ A monospace is only used for real code, data or tabular figures. It is never the display face of a non-technical business.

**H2. Tiny text crammed into every visible inch.** `S3`
→ toraway again, on generated pages cramming "tiny text into every visible inch of the page". Models fill space instead of editing.
→ Every pattern has a word budget (a hero of 25 words or fewer, a section intro of 60 words or fewer), and whitespace is treated as a feature.

**H3. Superfluous tags, chips and numbers on everything.** `S3`
→ joegibbs: AI wants "to add coloured left borders, tags and superfluous numbers."
→ A tag or chip must be filterable or clickable, or carry data the reader needs. Otherwise delete it.

**H4. Beige is the new purple.** `S4`
→ ChrisArchitect notes the recent shift to a "beige scheme" as the new default. This matches Anthropic's cream-and-terracotta cluster (C10) and Impeccable's "cream / beige palette."
→ Treat any base colour between #EFE6D8 and #F7F2EA as needing a written reason (see C10).

**H5. The design gives away the model, and sometimes the version.** `S4`
→ sen: "you can tell which LLM provider was used... sometimes even model and version." Each model family has a house look that practitioners recognise.
→ Never ship a model's first pass. Every pattern is redrawn by a human against the theme's brief.

**H6. Detectable by an automated DOM/CSS scan.** `S4`
→ Krebs's scanner needs no vision model. Computed styles alone (font-family, gradients, `backdrop-filter`, border-left colour, radius uniformity) flag these sites.
→ Run a similar Playwright scan over every template and style variation in CI. Each theme must score in the "low" band (0–1 patterns).

<!-- copylint-off -->
**H7. Buzzword-compliant copy with scare quotes and three-item lists whose items don't belong together.** `S3`
→ The "Tell HN" thread on LLM house style: "flowery prose that possibly makes gratuitous use of 'quotation marks'", lists of "exactly three items", some of which "don't all seem to belong". Another commenter adds "Drop language that sounds like marketing."
→ See `ANTI-AI-WRITING.md`. In patterns, lists have as many items as the content has, and quotation marks are only for quotations.
<!-- copylint-on -->


<!-- copylint-off -->
**H8. Non-concentric border radii (inner radius equal to the outer one on nested elements).** `S3`
→ A designer on r/web_design lists "non-concentric border radii" among the giveaways. Generated CSS reuses one token at every depth.
→ Inner radius = outer radius minus padding, computed in the radius scale.

**H9. Too many type sizes on one page (10 or more).** `S3`
→ One HN checklist counts "15 different text sizes". The ai-design-convergence study measured 10–13 sizes on AI pages against a human median of 8.
→ The type scale has 5–7 steps, enforced through `fontSizes` with custom sizes disabled.

**H10. Too many families, weights and heading styles.** `S3`
→ HN, on an obviously generated essay site: "Just how many fonts were hurt creating this page?!"
→ One family, or two at most, with a documented set of weights.

**H11. Huge headline wrapped at 2–3 words per line with dead space beside it.** `S3`
→ HN: "Many lines with just 2-3 words, massive font, and tons of unused whitespace to the right."
→ Size display type for a 20–35 character line, and fill the space beside it with something real.

**H12. Fonts declared in CSS but never shipped, so the site renders in fallbacks.** `S4`
→ tailthemes: "Declaring is not shipping." Generated code names a face without the `@font-face` files.
→ Fonts ship through `fontFace` in theme.json. CI checks the computed font on every template.

**H13. Mixed icon sets and weights (a filled icon beside outline icons, strokes that don't match the text).** `S3`
→ Reddit: "AI tends to pull from different icon sets per component". HN: icon stroke "should be the same as the letters".
→ One set, one stroke, sized to the cap height and matched to the body weight.

**H14. Icon plus text on every button.** `S2`
→ Reddit lists it among the giveaways.
→ Text-only buttons. Icons only where they aid recognition (cart, search, phone).

**H15. `//` separators and random ornamental glyphs (lightning bolts, arrow-in-square) in headings and labels.** `S3`
→ HN: "AI loves to separate headers with //", plus "random and seemingly inappropriate symbols".
→ Normal punctuation. No glyph without a job.

**H16. The long dash (U+2014) as filler in empty table cells and meta slots.** `S2`
→ Reddit calls it out "especially when used in lieu of a blank space like an empty table cell."
→ Write real empty states ("No events this month"), and hide empty meta rows.

**H17. Fake terminal or code window with traffic-light dots on a non-developer product.** `S4`
→ febbhav's "signs of AI design" taxonomy lists it. The retro-terminal look is also noted on HN as Claude's newer default after purple.
→ Terminal styling only for real CLI or code content, and never as a small-business hero.

**H18. Shimmer or "thinking" text effects, and skeleton loaders on static content.** `S4`
→ HN and Jim Nielsen: "Shimmer effect is <marquee> for AI."
→ Static pages render content directly. No shimmer text in any theme.

**H19. Emerald/green as the reflex replacement for banned purple.** `S3`
→ febbhav: when purple is banned, "models default to green".
→ Colour comes from the brief (see C1). A green accent must name its source (sage leaves, bottle glass, a shop front).

**H20. Primary and accent less than 20° of hue apart ("one hue pretending to be two").** `S2`
→ tailthemes quality gate.
→ Compare hues in OKLCH. Each palette colour has a distinct functional role, or it is dropped.

**H21. Happy-path demo data: names that all fit, six tidy rows, every card the same length.** `S4`
→ Reddit: "Every screen looks like a happy-path marketing screenshot… Nothing has an edge case, no long label wrapping weird."
→ Demo content deliberately includes a long product name, a two-line title, a missing image and an empty archive, and every pattern must still look right.

**H22. Interchangeable modules: every card, menu item or service laid out identically whatever it holds.** `S3`
→ Reddit: "Every card feels interchangeable, none of them designed around what the specific metric needed to communicate."
→ Design each pattern around its content. A menu, a price list and a portfolio index are different shapes.

**H23. Anthropomorphised objects and staccato fragments in copy ("Your laptop stays private. The URL goes everywhere." / "Bold flavors. Fast pickup.").** `S3`
→ HN calls both "an LLM smell", and notes that "Everything comes in punchy threes".
→ Literal subjects and full sentences. See `ANTI-AI-WRITING.md`.

**H24. Fabricated editorial chrome: invented bylines, an "editor who reviews every figure", made-up compliance badges.** `S5`
→ An HN thread picked apart a pen-name editor box. febbhav lists invented badges and user counts.
→ Demo bylines are the clearly fictional persona, and no invented credentials or certifications appear anywhere.

**H25. One endless single-page scroll for a business with distinct topics.** `S2`
→ Reddit: "And then they're all one long single-page scroll."
→ Real pages for menu, visit and shop. Our templates include them by default.

**H26. Untested states: broken dark mode, hamburger overlapping the logo, content vanishing after jump links.** `S4`
→ HN, on a one-shot Claude landing page: "Looks broken in dark mode on Firefox", "the hamburger menu icon overlaps with the site icon".
→ A release QA pass over all style variations, 320–1920px widths, keyboard use, and forced dark mode in the browser.

**H27. "Everything is busy": polish plus clutter, with no understatement.** `S3`
→ HN: "Polish + consistency but also with busy-ness is a hallmark… AI isn't good at understatement." The convergence study: "The machine output is not bad. It is central."
→ Before release, remove one element from every section and keep the removal if nobody misses it.
<!-- copylint-on -->

### 2.10 AI-generated imagery tells

This covers photos and illustrations that users upload into our themes, and above all the demo imagery we ship. Rule of thumb: **no AI-generated images in any theme demo, screenshot or pattern preview.** The traits below also go into the customer-facing guide "Choosing photos for your site".

**A1. Waxy, poreless skin with airbrushed highlights.** `S5`
→ MIT Detect Fakes lists skin that "appears excessively smooth or wrinkled", or ageing that doesn't match the hair and eyes, as a primary cue.
→ Real portraits with visible texture, shot in the business's own space. The demo persona's "owner" photo is a real photo licensed for the demo.

**A2. Wrong hands, fingers, teeth, earrings and glasses (merged, extra, asymmetric).** `S5`
→ The Wikipedia AI slop article lists "anatomically incorrect features (extra fingers, disconnected hands)". MIT flags glasses glare that doesn't behave.
→ Reviewers zoom to 200% on every hand and face in demo imagery. Any doubt means reject.

**A3. Garbled text on signs, packaging, book spines and shop fronts.** `S5`
→ Wikipedia lists "distorted text and misspellings" as a common flaw.
→ Demo shop-front and product images must have legible, real text, or none at all.

**A4. Background objects melting into each other; smudged faces in crowds.** `S5`
→ Wikipedia: "morphing shapes and blended elements", "poorly rendered or 'smudged' faces."
→ Prefer images with simple, real backgrounds (a workshop wall, a counter) over busy generated scenes.

**A5. Light that disagrees with the scene: rim light in an office, shadows falling in two directions, eyes lit with no source.** `S4`
→ MIT: fakes "may fail to accurately render natural lighting effects" around eyes and eyebrows.
→ Use documentary light: window light, overhead shop light, the light the place actually has.

**A6. Cinematic teal-and-orange grade on mundane subjects.** `S4`
→ This is the default "epic" look of image models, and it makes a bakery look like a movie poster.
→ Grade demo photos neutrally. Each theme's photo guide names one grade direction that fits the trade.

**A7. Everything at golden hour with perfect creamy bokeh.** `S3`
→ It is a generator's idea of "beautiful", and real businesses aren't photographed like that every day.
→ Mix light conditions, and include plain overcast and interior daylight shots.

**A8. Dead-centre, symmetric "hero subject" compositions.** `S3`
→ Generators centre the subject by default. Real photographers crop, cut off and lean.
→ Demo photography uses off-centre crops and partial subjects (hands at work, the edge of a table).

**A9. "3D clay" / Pixar-style characters and mascots.** `S4`
→ It is the signature style of generator-made brand assets from 2024 to 2026.
→ No 3D character illustration in any theme. If a theme is playful, commission flat or hand-drawn work with a single hand.

**A10. Glossy isometric 3D scenes and icons (floating phones, coins, shields).** `S4`
→ They carry no information about a real business.
→ Banned. See I4.

**A11. Corporate Memphis / "Alegria" flat people (long limbs, tiny heads, purple skin).** `S4`
→ Wikipedia: criticised as "simple shapes [and] untextured colours", "a universe... where problems have already been resolved," and in decline by 2023 from "uninspired design" and oversaturation.
→ No flat-people illustrations. Illustration, if any, depicts the trade's objects, drawn by one hand.

**A12. The stock diversity composite: a perfectly balanced group, all smiling at camera, in a spotless office.** `S4`
→ NN/g: users "ignore stock photos of generic people." AI generators produce this composition by default when asked for "a team."
→ Show the actual team, even if that is one person, at work rather than posing.

**A13. "In the style of" filtered portraits (Ghibli, anime, watercolour-filter headshots of the owner).** `S4`
→ Wikipedia records strong public and professional "backlash" against AI in creative spaces. For a creative business especially, it signals that the business doesn't pay artists.
→ Banned in demos. The docs advise against it.

**A14. AI headshots: same pose, same blurred office bokeh, same blazer.** `S4`
→ They are uncanny and identical across companies.
→ Team patterns are designed for mixed, informal real photos (different backgrounds and crops) and still look good that way.

**A15. Over-saturated HDR "clarity" look.** `S3`
→ It is a generator and phone-filter default.
→ Natural saturation. Our demo images must pass a quick histogram check with no clipped channels.

**A16. Products placed in impossible settings (a candle on a rock at sea, sneakers floating in clouds).** `S3`
→ It is the stock AI "lifestyle composite".
→ Products are shown where they are used, or on a plain surface in real light.

**A17. Decorative feel-good hero photos that say nothing about the business.** `S3`
→ NN/g: "users pay attention to information-carrying images... and ignore purely decorative images."
→ Every hero image must show the product, the place, the people or the work.

**A18. Mixed image species: an AI photo, a stock photo, a 3D render and an illustration on one page.** `S3`
→ It signals images were collected, not directed.
→ Each theme's photo guide defines one image family: a subject range, a light, a crop logic and a grade.

<!-- copylint-off -->

### 2.11 AI copywriting tells (summary)

The full study is in `ANTI-AI-WRITING.md`. This section only lists what a design reviewer should catch in pattern demo copy. It does not repeat V1–V10. Source for most items: Wikipedia, "Signs of AI writing".

**W1. "Not just X, it's Y" / "not a mirror but a portal" (negative parallelism).** `S5`
→ This is the most recognisable LLM sentence shape.
→ Say what it is.

**W2. The AI vocabulary: delve, tapestry, testament, vibrant, nestled, boasts, showcase, pivotal, crucial, foster, elevate, landscape.** `S5`
→ Wikipedia's list of "AI vocabulary" words, plus "promotional and advertisement-like language."
→ These words are on the demo-content lint list.

**W3. Scene-setting openers: "In today's fast-paced world…", "In a world where…".** `S5`
→ This is a stock LLM throat-clear.
→ Start with the fact.

**W4. Avoiding "is": "serves as", "stands as", "represents", "boasts".** `S3`
→ Wikipedia: "avoidance of basic copulatives."
→ "The studio is in Leith." Not "The studio serves as a creative hub nestled in Leith."

**W5. Superficial "-ing" tails: "…highlighting our commitment to quality."** `S3`
→ Wikipedia: "superficial analyses" with -ing phrase endings.
→ Delete the tail.

**W6. Colon titles: "Craft: The Art of Slow Living".** `S3`
→ This is an LLM headline template.
→ One plain heading.

**W7. A heading on every paragraph; headings that only contain other headings.** `S3`
→ Wikipedia lists "headings only containing other headings." It is the outline structure of LLM output.
→ A heading introduces at least two paragraphs, or a list.

**W8. Bolded inline-header bullets ("**Fast:** we deliver quickly").** `S4`
→ Wikipedia: "inline-header vertical lists."
→ Plain sentences, or a real definition list.

**W9. Emoji bullets and checkmark lists (✅ 🔸 ✨).** `S5`
→ Wikipedia: "emoji as formatting."
→ See I2.

**W10. Fake specificity: oddly precise numbers with no source ("trusted by 2,347 clients", "98.6% satisfaction").** `S5`
→ Precision is being used to fake evidence.
→ No numbers in demo copy that the persona couldn't plausibly know and prove.

**W11. Vague attributions: "experts agree", "industry-leading", "award-winning" with no award.** `S4`
→ Wikipedia: "vague attributions and overgeneralization."
→ Name the award and the year, or cut it.

**W12. Leftover markup and chat residue: literal `**`, "Certainly! Here's…", "[Insert name]", "As of my last update".** `S5`
→ Wikipedia: "phrasal templates and placeholder text", markdown in the wrong context, "knowledge-cutoff disclaimers."
→ The lint rejects `**`, `[`, `]` and "As an AI" in demo content.

**W13. Uniform cadence: every sentence 12–18 words long, and every paragraph three sentences.** `S2`
→ It is a statistical fingerprint of generated prose.
→ Vary the rhythm on purpose. Short sentences are allowed, and so are long ones.

**W14. "Let's dive in", "we'll explore", "whether you're a… or a…".** `S3`
→ Wikipedia: "collaborative communication."
→ Cut the preamble.

<!-- copylint-on -->

### 2.12 WordPress / block-theme-specific tells

This section is the WordPress version of "shipping the defaults". Setting names are from the theme.json v3 reference and the Theme Handbook (see sources). Where no source was read, the item is marked *(from WordPress core knowledge)*.

**WP1. The core 12-colour palette leaking into the editor and front end ("Vivid cyan blue", "Luminous vivid amber").** `S4`
→ `settings.color.defaultPalette` is `true` unless turned off, and blocks coloured with it output classes like `has-vivid-cyan-blue-background-color`.
→ `"defaultPalette": false`. Define 5–8 palette colours with semantic slugs (`base`, `contrast`, `accent`, …).

**WP2. The core gradient presets ("Vivid cyan blue to vivid purple" and similar).** `S5`
→ `settings.color.defaultGradients` is on by default. These gradients look like WordPress around 2019, and one of them is literally a purple gradient.
→ `"defaultGradients": false` and `"customGradient": false`, or ship at most one gradient made from the theme's palette.

**WP3. The core duotone presets ("Dark grayscale", "Purple and yellow") offered on images.** `S3`
→ `settings.color.defaultDuotone` is on by default.
→ `"defaultDuotone": false`. Define one or two duotones from the palette, as Rich Tabor's Wei does to blend images into their backgrounds.

**WP4. The core font-size presets (Small, Medium, Large, X-Large) with no fluid scale.** `S3`
→ WordPress ships these unless the theme overrides them. They aren't fluid and give every site the same type rhythm.
→ `"defaultFontSizes": false`, a custom `fontSizes` scale with `fluid` min/max, and `"fluid": true` under `typography`.

**WP5. The core spacing scale (2X-Small to 2X-Large, 0.44–5.06rem) used as-is.** `S3`
→ The default 7-step scale around 1.5rem gives every site the same vertical rhythm.
→ `"defaultSpacingSizes": false` and your own `spacingSizes`, including a genuinely large step for section breaks.

**WP6. The five core shadow presets (Natural, Deep, Sharp, Outlined, Crisp).** `S3`
→ `settings.shadow.defaultPresets` is on by default. It is the same drop shadow as everyone else.
→ `"defaultPresets": false` under `shadow`, and 0–2 shadow presets tuned to the palette.

**WP7. Core aspect-ratio and text-shadow presets shown in the UI.** `S1`
→ This is editor noise that invites off-brand choices.
→ `dimensions.defaultAspectRatios: false` with your own `aspectRatios`, and `typography.defaultTextShadowPresets: false`.

**WP8. `appearanceTools: true` with no presets, so every control is on and nothing is constrained.** `S3`
→ Each page drifts toward whatever the editor clicked, so the site ends up looking assembled.
→ Keep `appearanceTools`, but define presets. Consider `custom: false`, `customFontSize: false`, `customSpacingSize: false` and per-block `settings.blocks` for tight themes.

**WP9. The default Button: dark grey pill with the stock padding.** `S4`
→ It is the most recognisable core default *(from WordPress core knowledge)*.
→ `styles.elements.button` with colour, typography, radius, padding, `:hover` and `:focus` states, and an outline variation under `styles.blocks["core/button"].variations`.

**WP10. The grey left bar on Quote blocks from `wp-block-styles`.** `S3`
→ The Theme Handbook notes `wp-block-styles` adds "the default color bar to the left of blockquotes" and should not be used in theme.json themes.
→ Don't add `wp-block-styles`. Design `core/quote` and `core/pullquote` in `styles.blocks`, together with `styles.elements.cite`.

**WP11. Separator as the default thin grey hairline.** `S2`
→ *(from WordPress core knowledge)*
→ Style `core/separator` from the palette, or register block styles (a short rule, a dinkus, an ornament).

**WP12. The default navigation overlay: stock hamburger icon opening a white panel with left-aligned links.** `S4`
→ *(from WordPress core knowledge)* Theme authors on WP Tavern complain about how little design control the mobile menu gives them.
→ Set overlay colours from the palette and style `core/navigation` typography and gap. Add custom CSS for `.wp-block-navigation__responsive-container`, and use a text "Menu" toggle or a custom icon.

**WP13. The default Search block: visible "Search" label, bordered input, "Search" button.** `S2`
→ *(from WordPress core knowledge)*
→ Hide the label visually (keep it for screen readers), put the button inside or use an icon plus label, and style it from presets.

**WP14. The default comments area ("Leave a Reply", stock textarea, stock submit button).** `S3`
→ *(from WordPress core knowledge)*
→ Design the comments template part. Rewrite the heading in the theme's voice, and style the inputs to match K8.

**WP15. Twenty Twenty-Four/Twenty Twenty-Five fonts (Manrope, Fira Code, Inter, Cardo) carried into new themes.** `S4`
→ Twenty Twenty-Five alone has over a million active installs, and its announcement names Manrope as the default font. These faces now read as "default WordPress".
→ None of the fonts bundled with default themes may be a theme's primary face.

**WP16. Default Cover-block hero: dimmed photo, centred white H1, one button.** `S4`
→ This is the stock Cover pattern and the most common Pattern Directory hero.
→ An asymmetric layout, text beside the image, a palette duotone, or no hero image at all.

**WP17. A Twenty Twenty-X clone made with Create Block Theme ("Clone theme"): same header, same footer, same patterns, new colours.** `S5`
→ The Theme Directory rules state "Cloning of designs is not acceptable", yet cloning is a one-click action in the plugin.
→ Build `parts/header.html`, `parts/footer.html`, `templates/` and `patterns/` from scratch. No file may start as a copy of a core theme file.

**WP18. Inherited style variations (eight or sixteen palettes and font pairings from the parent default theme).** `S4`
→ They show another brand's choices in the Styles panel.
→ Ship 0–4 curated variations of your own. Each one must pass this whole document on its own.

**WP19. Footer credit "Proudly powered by WordPress" / "Designed with WordPress".** `S4`
<!-- copylint-off -->
→ It is the WordPress version of "Made with ❤️" (see P7).
<!-- copylint-on -->
→ Remove it. The footer carries the business's details.

**WP20. Plain-text site title top-left, with the tagline underneath and the nav to the right.** `S3`
→ This is the default header of every core theme since 2010 *(from WordPress core knowledge)*.
→ Use a designed `core/site-title` treatment (display face, size, case) or a logo slot. Drop `core/site-tagline` from the default header.

**WP21. Leftover install content: "Hello world!", "Sample Page", "A WordPress Commenter", "Uncategorized", "Just another WordPress site".** `S5`
→ These announce "nobody finished this" *(from WordPress core knowledge)*.
→ Theme onboarding checks for these and prompts cleanup. Starter content comes from patterns, not core samples.

**WP22. The default Query Loop: three equal columns with featured image, title, date and "Read more".** `S4`
→ This is the Pattern Directory "Posts" look, and the WordPress version of L2.
→ Custom `core/query` patterns: one lead post, list-style archives, or an image-led index, with a set `aspectRatio` on featured images and styled date and term blocks.

**WP23. Core and remote Pattern Directory patterns left in the inserter.** `S4`
→ Editors keep inserting generic patterns (gradient CTA banners, "Fullwidth, vertically aligned headline…"), and the site regresses to the directory's look.
→ `remove_theme_support( 'core-block-patterns' )`, `add_filter( 'should_load_remote_block_patterns', '__return_false' )`, and theme-specific pattern categories.

**WP24. Unstyled WooCommerce blocks: default product grid, grey "Sale!" badge, stock add-to-cart button, generic cart/checkout sidebar.** `S4`
→ This is the WooCommerce version of an unfinished site *(default look from WordPress core knowledge)*.
→ Style `woocommerce/*` blocks through `styles.blocks` in theme.json, as the WooCommerce theming docs recommend. Buttons inherit from `styles.elements.button`.

**WP25. One narrow content column (about 620–650px) everywhere, with no wide or full-width moments.** `S3`
→ It is the default-theme blog look applied to a business site.
→ Set `contentSize` and `wideSize` deliberately, use `useRootPaddingAwareAlignments`, and give each template at least one `alignwide` or `alignfull` moment.

**WP26. Per-block CSS so specific that users can't override it, so they give up and restyle with defaults.** `S2`
→ Justin Tadlock recommends `wp_enqueue_block_style()` and `:root :where()` selectors to keep user styles overridable.
→ Follow that pattern. Our CSS must lose to user choices in Global Styles.

**WP27. The "starter site" look (Astra/Kadence/Hello Elementor demo imports): hero with an overlay, three icon boxes, a counter row, a testimonial slider, a CTA band.** `S5`
→ It is the pre-AI template monoculture that AI sites learned from. *(No source read. Based on direct familiarity with these demos.)*
→ Nothing in our library may resemble a starter-site import. Test by putting the theme screenshot next to the top five starter sites.

**WP28. Border radius set per block ad hoc (pill buttons, 8px images, 4px inputs) with no scale.** `S3`
→ Mixed radii look assembled from parts.
→ `settings.border.radiusSizes` (WordPress 6.9+) as a named scale, reused through block style variations.

**WP29. Theme screenshot (`screenshot.png`) showing a default-looking hero with a gradient and three cards.** `S4`
→ The screenshot is the first thing buyers see in the directory and the admin, and it sets expectations for the whole theme.
→ The screenshot shows the theme's most distinctive template (often not the home page), with real demo photography.

### 2.13 Information architecture & UX tells

**U1. Generic nav labels: "Solutions", "Resources", "Platform", "Company", "Why us".** `S4`
→ NN/g: "Menus are not the place to get cute with made-up words, internal jargon, or abstract high-level categorization."
→ Nav labels are the nouns customers search for: "Menu", "Prices", "Commissions", "Visit", "Shop".

**U2. Newsletter modal on page load.** `S5`
→ NN/g lists "requesting email addresses before any interaction" as a top popup mistake. Their core principle: "Give value to your visitors before asking them anything."
→ No modal newsletter patterns. The signup lives inline at the end of relevant content.

**U3. Exit-intent popups ("Wait! Before you go…").** `S4`
→ This is "nagging" in the deceptive.design taxonomy.
→ Banned.

**U4. Cookie wall: a full-screen modal blocking content, with no "Reject" at the first layer.** `S4`
→ NN/g: offer "Accept all," "Deny all" and "Manage settings" immediately, and don't cover the page. One participant said: "I definitely don't want it to cover the page."
→ Themes style consent plugins as small, non-modal bars with equal-weight Accept and Reject buttons. There is no cookie banner at all if the theme sets no cookies.

<!-- copylint-off -->
**U5. Fake chat bubble: "Hi 👋 How can we help?" opening a bot, or a form pretending to be chat.** `S4`
<!-- copylint-on -->
→ NN/g found chatbots break "as soon as users deviated from the prescribed script". Users want transparency about bots and a route to a human.
→ No chat launcher in any pattern. Contact means a real phone number, an email and opening hours.

**U6. Stacked overlays: cookie bar, newsletter modal, chat bubble and promo bar at the same time.** `S5`
→ NN/g lists "stacking multiple popups consecutively". One participant "tossed his phone across the table".
→ At most one overlay is visible at any moment, and none on first paint.

**U7. Push-notification or location permission prompt on first visit.** `S4`
→ NN/g: popups before users have done anything.
→ Banned.

**U8. "Book a demo" / "Get started" / "Start free trial" as the primary CTA on a non-software business.** `S5`
→ SaaS vocabulary pasted onto a florist's site.
→ The primary CTA is the trade's own action (see V6).

**U9. Mega menu or multi-level dropdowns for a site with fewer than 20 pages.** `S3`
→ NN/g: "multi-level cascading menus become frustrating with two tiers."
→ One level of nav. Deeper content gets a landing page, not a dropdown.

**U10. No current-page indicator in the nav.** `S2`
→ NN/g calls it "probably the single most common mistake" in menus.
→ Style `current-menu-item` / `aria-current="page"` in every theme.

**U11. Contact only through a form, with no phone, address or hours visible.** `S4`
→ Sinton: "a site with no obvious way to get in touch." A form-only contact page reads as a lead-gen funnel, not a business.
→ The footer and contact template show the address, hours, phone and email as text. A form is optional.

**U12. Opening hours and address in an image, or missing entirely.** `S3`
→ They can't be copied, translated or read by search engines and screen readers.
→ Provide an hours and address pattern as real text, with guidance on LocalBusiness structured data (via plugin).

**U13. Login/"Sign in" or "Account" in the header of a site with no accounts.** `S3`
→ SaaS chrome.
→ Show it only when WooCommerce accounts are enabled, and then as a text link.

**U14. Confirmshaming: "No thanks, I don't like good coffee."** `S5`
→ deceptive.design: "The user is emotionally manipulated into doing something that they would not otherwise have done."
→ Decline options are neutral: "No thanks."

**U15. Feedback or survey prompts before the visitor has done anything.** `S3`
→ NN/g lists "asking for feedback before users accomplish anything meaningful."
→ Put a feedback link in the footer if needed.

**U16. App-download interstitials or "Get our app" modals.** `S3`
→ NN/g lists them as a popup anti-pattern.
→ Banned in themes.

**U17. Language or region switcher with a flag for a single-market business.** `S2`
→ Template chrome, and flags aren't languages.
→ Only show it when a multilingual plugin is active, labelled with language names.

**U18. Social icons in the header of every page (eight networks, most dormant).** `S2`
→ It pushes visitors off-site before they've seen anything.
→ Social links go in the footer, and only the channels that are actually used.

**U19. Weak signifiers: buttons that look like labels, and labels that look like buttons.** `S3`
→ NN/g: pages with weak signifiers needed "22% more time" and "25% more fixations"; users "don't feel confident."
→ Clickable things look clickable. Non-clickable tags and badges must not look like buttons.

**U20. Modal lightboxes for everything (bios, menus, prices opening in overlays).** `S3`
→ NN/g: modals cause "context loss" and add "an extra goal: to dismiss the dialog."
→ Content lives on pages. The core Image lightbox is fine for photos.

### 2.14 E-commerce tells

This section applies to every WooCommerce-ready theme. Several items here are illegal in the EU, the UK or the US, not only in poor taste.

**E1. Countdown timers that reset on reload, or "Sale ends in 04:59".** `S5`
→ The Princeton "Dark Patterns at Scale" study found countdown timers on hundreds of shopping sites, often still valid after "expiry". deceptive.design: "fake urgency."
→ No countdown patterns. A real sale states its end date as text.

**E2. "Only 3 left!" low-stock messages on everything.** `S5`
→ Low-stock messages were the most common dark pattern in the Princeton study (632 instances). deceptive.design: "fake scarcity."
→ Show stock only when it is real and actually low, using WooCommerce's own stock data and a neutral style.

**E3. Activity pop-ups: "Anna from Berlin just bought…"** `S5`
→ Princeton found 313 fake activity notifications, mostly served by third-party plugins. deceptive.design: "fake social proof."
→ Banned. Themes must not style or leave space for these widgets.

**E4. "17 people are viewing this right now."** `S5`
→ Same category as E3.
→ Banned.

**E5. A strip of generic trust badges under Add to Cart ("Secure checkout", "100% satisfaction guaranteed", "Money-back").** `S4`
→ Baymard found users judge checkout security by visual cues, and even "homemade seals" moved perception. That is why dropshipping stores stack them. On a real shop they read as overcompensating.
→ Instead, visually group the payment fields (Baymard's "visual encapsulation") and state the real return policy in one line near the price.

**E6. A review widget with a perfect 4.9★ average and AI-sounding five-star reviews.** `S5`
→ Since 2024 the FTC rule bans fake and AI-generated reviews and testimonials, and suppressing negative ones.
→ Style WooCommerce's native reviews. Show the count, and show that low ratings exist. Demo content has no fake reviews (see P3).

**E7. Free-shipping progress bar or "Free shipping over €50" announcement bar on every page.** `S3`
→ This is Shopify-template chrome.
→ Put shipping terms on the product and cart pages as text. The announcement bar is optional and off by default.

**E8. Pre-ticked add-ons, insurance or "gift wrap" in the basket.** `S5`
→ deceptive.design: "preselection" and "sneaking."
→ All options are unticked by default. Themes never style extras to look already included.

**E9. Costs that appear only at checkout (handling fees, "service charge").** `S5`
→ deceptive.design: "hidden costs." The Princeton study groups these under "sneaking."
→ Product pages show the delivery cost, or link to it, near the price.

**E10. Permanent strikethrough "was" prices.** `S4`
→ A reference price that was never charged is fake urgency by another name.
→ The sale style is only used with WooCommerce scheduled sales. Demo products are shown at full price.

**E11. Spin-to-win or scratch-card discount popups.** `S5`
→ This is the dropshipping store signature (nagging plus gamified email capture).
→ Banned.

**E12. Shopify-Dawn sameness: centred logo with search/account/cart icons, "Image banner", "Collection list", "Multicolumn", "Image with text" in that order.** `S4`
→ Dawn is Shopify's free default "minimalist theme that lets product images take center stage", so a huge number of small shops share its structure. Buyers who come to WooCommerce from Shopify recognise it instantly.
→ Shop home templates are built around how the trade actually sells: a seasonal list, a menu, an edition, a studio note.

<!-- copylint-off -->
**E13. AI product descriptions: "Elevate your everyday with this versatile, timeless piece…"** `S5`
<!-- copylint-on -->
→ See W2 and V1.
→ Demo product copy states material, size, origin, care and who made it.

**E14. White-background supplier photos next to AI "lifestyle" composites of the same product.** `S4`
→ This is the dropshipping catalogue look (see A16, A18).
→ Product image slots are designed for consistent, real photography with a set aspect ratio per theme.

**E15. "As seen in" press-logo row (Forbes, Vogue, BBC) with no links.** `S4`
→ Wikipedia's AI-writing guide lists "canned emphasis on notability... media coverage". Unlinked logos are unverifiable.
→ Press is a list of linked headlines with dates.

**E16. Stacked mobile chrome: sticky add-to-cart bar, floating cart button, chat bubble and cookie bar.** `S3`
→ See L20 and U6.
→ At most one sticky commerce element on mobile.

**E17. Payment-icon row showing a dozen card and wallet logos in the footer.** `S2`
→ Template filler, often including methods the shop doesn't accept.
→ List accepted methods as text on the checkout or shipping page.

**E18. Hard-to-cancel "subscribe and save", preselected on product pages.** `S5`
→ deceptive.design: "hidden subscription", "hard to cancel". Princeton: "obstruction."
→ One-off purchase is the default. Any subscription option is clearly labelled with the cancellation terms.

**E19. An upsell modal after Add to Cart ("Complete the look!").** `S4`
→ NN/g: never interrupt checkout with modals.
→ "You might also like" belongs inline on the cart page, or nowhere.

**E20. A checkout that looks different from the rest of the shop (unstyled fields, broken spacing).** `S4`
→ Baymard: layout quirks at payment ("This looks a bit strange. Especially when you are about to pay") make users suspect the site was hacked.
→ Checkout blocks are styled with the same tokens as the rest of the theme, and tested on every style variation.

---

## 3. Sniff test (run before every release)

A theme ships only if every answer matches the one in brackets. Questions tagged `[S5]` block release outright. Any other mismatch needs a written exception in the theme's README.

**First look**
1. Squint at the front page from 2 m away. Could it be mistaken for another theme in the library, a v0/Lovable demo, a Twenty Twenty-Five clone or a starter-site import? **[no]** `[S5]`
2. Can the author state in one sentence what trade the theme is for, and name one visual decision that comes from that trade? **[yes]** `[S5]`
3. Does the theme screenshot show real photography and the theme's most distinctive template? **[yes]**
4. With every image blurred, is it still obvious what kind of business this is from the type, layout and copy alone? **[yes]**

**Colour**

5. Is the primary accent in the violet/indigo band (hue 245–275°) or a stock Tailwind/shadcn hex? **[no]** `[S5]`
6. Is there any gradient on text, or any purple/blue/pink gradient anywhere? **[no]** `[S5]`
7. Is there any glow, blurred orb, halo or coloured shadow? **[no]**
8. Are `defaultPalette`, `defaultGradients` and `defaultDuotone` all set to false? **[yes]**
9. Does one dominant colour cover most of the page, with the accent kept to a small share? **[yes]**
10. Is body text at 7:1 or better, and secondary text at 4.5:1 or better, on every surface in every style variation? **[yes]**

**Type**

11. Is the display or body face Inter, Roboto, Open Sans, Lato, Poppins, Montserrat, Geist, Space Grotesk, Instrument Serif, Manrope or bare system-ui? **[no]** `[S5]`
12. Is the display face unique within the library (checked against `FONT-REGISTRY.md`)? **[yes]**
13. Does any headline italicise or recolour a single word? **[no]** `[S5]`
14. Are there all-caps eyebrow labels above headings, or a pill badge above the H1? **[no]** `[S5]`
15. Is the display-to-body size ratio at least 4×, with true italics bundled and `font-synthesis` off? **[yes]**
16. Is body text at least 17px, prose at most 72ch, and headings balanced with `text-wrap`? **[yes]**

**Layout**

17. Does any pattern contain three or more identical cards with an icon tile, title and two lines? **[no]** `[S5]`
18. Is there a stat row, logo cloud, "Most popular" pricing card, bento grid or gradient "Ready to get started?" band? **[no]**
19. Is the front-page order something other than hero → features → stats → testimonials → pricing → FAQ → CTA? **[yes]**
20. Is there at least one deliberate break from the centred max-width column? **[yes]**
21. Is the nav visible (not a hamburger) at desktop widths? **[yes]**
22. Is there an auto-rotating carousel, scrolljacking or horizontal-scroll section? **[no]**
23. Is at most one element sticky on mobile? **[yes]**

**Components**

24. Does every element class (button, input, card, image) have its own intentionally chosen radius from `radiusSizes`, rather than one global radius? **[yes]**
25. Are cards nested in cards anywhere, or is there glassmorphism outside a sticky header? **[no]**
26. Are Button, Quote, Separator, Search, Navigation overlay and Comments all restyled from core defaults? **[yes]**
27. Are all WooCommerce blocks (grid, price, sale badge, cart, checkout) styled with the theme's tokens? **[yes]**
28. Is the focus ring custom-designed and at 3:1 contrast or better on every surface colour? **[yes]**

**Imagery & icons**

29. Is there any emoji, sparkles icon, default Lucide/Heroicons outline set or icon font? **[no]** `[S5]`
30. Is every demo image a real, licensed photo of the target trade, with no AI people, 3D clay, Memphis figures, isometric renders or laptop flatlays? **[yes]** `[S5]`
31. Zoom to 200% on every hand, face and sign in the demo imagery. Is anything melted, garbled or extra? **[no]** `[S5]`
32. Does every image slot carry information (product, place, people, work) rather than mood alone? **[yes]**

**Motion**

33. Does anything fade or slide in on scroll, pulse, shimmer, marquee, count up, parallax or bounce? **[no]**
34. With JS disabled and `prefers-reduced-motion: reduce`, is all content visible and static? **[yes]** `[S5]`

**Copy & content**

<!-- copylint-off -->
35. Does any demo copy contain a word from the lint list (unlock, empower, supercharge, seamless, elevate, delve, tapestry, testament, vibrant, nestled, boasts, world-class, cutting-edge, game-changer, "everything you need", "in today's fast-paced world")? **[no]** `[S5]`
<!-- copylint-on -->
<!-- copylint-off -->
36. Is there any "not just X, it's Y", colon-title, two-beat slogan or rule-of-three adjective run? **[no]**
<!-- copylint-on -->
37. Does a search for the em dash character (U+2014) over the demo content and patterns return 0 hits? **[yes]**
38. Does every CTA say what happens next ("Book a fitting", not "Get started", "Learn more" or "Book a demo")? **[yes]**
39. Does the demo content contain invented statistics, fictional client logos, press logos or "Sarah Johnson"-style testimonials? **[no]** `[S5]`
40. Could you swap the hero sentence onto a competitor's site and have it still make sense? **[no]**
41. Is there any dead link (`#`), placeholder image, lorem ipsum, "Hello world!", "Powered by WordPress" credit or hard-coded copyright year? **[no]** `[S5]`

**UX & IA**

42. Are the nav labels the trade's own nouns (no "Solutions", "Resources" or "Platform")? **[yes]**
43. Does anything open a modal, popup or permission prompt on page load or on exit? **[no]** `[S5]`
44. Are the address, hours, phone and email visible as text without submitting a form? **[yes]**
45. Is there a chat launcher, "back to top" bubble, dark-mode toggle or login link on a site with no accounts? **[no]**
46. Does the nav show the current page? **[yes]**

**Commerce (WooCommerce themes)**

47. Are there countdown timers, "only X left" styling, "X people viewing", recent-purchase popups or spin-to-win? **[no]** `[S5]`
48. Is there a generic trust-badge strip, a payment-logo wall or a "Free shipping over…" bar enabled by default? **[no]**
49. Are all add-ons unticked by default, and delivery costs visible before checkout? **[yes]** `[S5]`
50. Does the checkout look like the same theme as the product page, in every style variation? **[yes]**

**Library-level**

51. Does this theme's (display font, accent hex, radius scale) triple differ from every other theme in the library? **[yes]**
52. Were core and remote Pattern Directory patterns removed from the inserter, and were the parent default theme's variations and patterns deleted? **[yes]**
53. Does the automated DOM/CSS slop scan (H6) put every template and style variation in the low band (0–1 patterns)? **[yes]**

---

## 4. Sources

### 4.1 Read in full

**Anthropic**
- Anthropic, "Improving frontend design through Skills": https://claude.com/blog/improving-frontend-design-through-skills
- Anthropic, frontend-design SKILL.md (anthropics/skills): https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md (read via https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md)
<!-- copylint-off -->
- Anthropic Engineering, "Harness design for long-running application development": https://www.anthropic.com/engineering/harness-design-long-running-apps
<!-- copylint-on -->
- Anthropic Cookbook, "Prompting for frontend aesthetics": https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb (read via https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/coding/prompting_for_frontend_aesthetics.ipynb)

**Vibe-coded / AI slop design**
- Impeccable, "The missing design vocabulary for agents" (slop pattern catalogue): https://impeccable.style/slop/
- Developers Digest, "AI Design Slop: 16 Patterns That Out Your App as Vibe-Coded": https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it
- The Fountain Institute, "7 Signs a UI Has Been Vibe Coded": https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui
- Sinton Agency, "How to Spot a Vibe Coded Website (and Fix It)": https://www.sinton.agency/blog/how-to-spot-a-vibe-coded-website
- VibeMole, "How to Avoid Building Apps That Look Vibe Coded": https://vibemole.com/resources/avoid-vibecoded-app-design
- CodeMySpec, "Why Vibe Coded Websites All Look the Same": https://codemyspec.com/blog/vibe-coded-websites-look-the-same
- 925 Studios, "AI Slop Fonts and Gradients: The Tells That Give Away AI Design": https://www.925studios.co/blog/ai-slop-design-tells
- prg.sh, "Why Your AI Keeps Building the Same Purple Gradient Website": https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website
- DEV Community, "Why Every AI-Built Website Looks the Same (Blame Tailwind's Indigo-500)": https://dev.to/alanwest/why-every-ai-built-website-looks-the-same-blame-tailwinds-indigo-500-3h2p
- SmoothUI, "AI Design Slop: Why AI-Generated UI Looks Generic, and the Fix": https://smoothui.dev/blog/ai-design-slop
- ux-skill, "Everything built with shadcn/ui looks the same": https://uxskill.laithjunaidy.com/blog/shadcn-ui-looks-generic.html
- LogRocket, "Linear design: The SaaS design trend that's boring and bettering UI": https://blog.logrocket.com/ux-design/linear-design/
- Rectangle, "The Linear effect": https://rectangle.substack.com/p/the-linear-effect

**Designer essays**
- Frank Chimero, "The Web's Grain": https://frankchimero.com/blog/2015/the-webs-grain/
- Frank Chimero, "Everything Easy is Hard Again": https://frankchimero.com/blog/2018/everything-easy/
- Brad Frost, "Things you could be doing instead of designing & building that card component for the umpteenth time": https://bradfrost.com/blog/post/things-you-could-be-doing-instead-of-designing-building-that-card-component-for-the-umpteenth-time/
- Brad Frost, "A Designer's Thoughts About This Moment in AI" (ethics, not aesthetics; background only): https://bradfrost.com/blog/post/a-designers-thoughts-about-this-moment-in-ai/

**Typography data**
- HTTP Archive, Web Almanac 2024, Fonts chapter: https://almanac.httparchive.org/en/2024/fonts

**Imagery**
- Wikipedia, "AI slop": https://en.wikipedia.org/wiki/AI_slop
- Wikipedia, "Corporate Memphis": https://en.wikipedia.org/wiki/Corporate_Memphis
- Wikipedia, "Artificial intelligence visual art": https://en.wikipedia.org/wiki/Artificial_intelligence_visual_art
- Wikipedia, "Flat design": https://en.wikipedia.org/wiki/Flat_design
- MIT Media Lab, "Detect Fakes": https://www.media.mit.edu/projects/detect-fakes/overview/
- Nielsen Norman Group, "Photos as Web Content": https://www.nngroup.com/articles/photos-as-web-content/

**Writing**
- Wikipedia, "Signs of AI writing": https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

**UX / IA**
- Nielsen Norman Group, "Popups: 10 Problematic Trends and Alternatives": https://www.nngroup.com/articles/popups/
- Nielsen Norman Group, "Modal & Nonmodal Dialogs: When (& When Not) to Use Them": https://www.nngroup.com/articles/modal-nonmodal-dialog/
- Nielsen Norman Group, "Cookie Permissions 101": https://www.nngroup.com/articles/cookie-permissions/
- Nielsen Norman Group, "Auto-Forwarding Carousels and Accordions Annoy Users and Reduce Visibility": https://www.nngroup.com/articles/auto-forwarding/
- Nielsen Norman Group, "Menu-Design Checklist: 17 UX Guidelines": https://www.nngroup.com/articles/menu-design/
- Nielsen Norman Group, "Hamburger Menus and Hidden Navigation Hurt UX Metrics": https://www.nngroup.com/articles/hamburger-menus/
- Nielsen Norman Group, "Scrolljacking 101": https://www.nngroup.com/articles/scrolljacking-101/
- Nielsen Norman Group, "'Learn More' Links: You Can Do Better": https://www.nngroup.com/articles/learn-more-links/
- Nielsen Norman Group, "Flat UI Elements Attract Less Attention and Cause Uncertainty": https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/
- Nielsen Norman Group, "The User Experience of Chatbots": https://www.nngroup.com/articles/chatbots/

**E-commerce / dark patterns**
- deceptive.design, "Types of deceptive pattern": https://www.deceptive.design/types
- Princeton WebTAP, "Dark Patterns at Scale": https://webtransparency.cs.princeton.edu/dark-patterns/
- US FTC, "Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials" (Aug 2024): https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials
- Baymard Institute, "How Users Perceive Security During the Checkout Flow (Incl. New 'Trust Seal' Study 2023)": https://baymard.com/blog/perceived-security-of-payment-form
- Shopify Theme Store, Dawn: https://themes.shopify.com/themes/dawn/styles/default

**WordPress**
- WordPress Developer Resources, Color settings: https://developer.wordpress.org/themes/global-settings-and-styles/settings/color/
- WordPress Developer Resources, Typography settings: https://developer.wordpress.org/themes/global-settings-and-styles/settings/typography/
- WordPress Developer Resources, Spacing settings: https://developer.wordpress.org/themes/global-settings-and-styles/settings/spacing/
- WordPress Developer Resources, Shadow settings: https://developer.wordpress.org/themes/global-settings-and-styles/settings/shadow/
- WordPress Developer Resources, Layout settings: https://developer.wordpress.org/themes/global-settings-and-styles/settings/layout/
- Block Editor Handbook, theme.json reference (living): https://developer.wordpress.org/block-editor/reference-guides/theme-json-reference/theme-json-living/
- Block Editor Handbook, Theme support: https://developer.wordpress.org/block-editor/how-to-guides/themes/theme-support/
- Theme Handbook, Registering patterns: https://developer.wordpress.org/themes/patterns/registering-patterns/
- Make WordPress Themes, Required review guidelines: https://make.wordpress.org/themes/handbook/review/required/
- Make WordPress Core, "Introducing Twenty Twenty-Five": https://make.wordpress.org/core/2024/08/15/introducing-twenty-twenty-five/
- WordPress.org, Twenty Twenty-Five: https://wordpress.org/themes/twentytwentyfive/
- WordPress.org, Twenty Twenty-Four: https://wordpress.org/themes/twentytwentyfour/
- WordPress.org, Pattern Directory: https://wordpress.org/patterns/
- WordPress.org, Create Block Theme plugin: https://wordpress.org/plugins/create-block-theme/
- WP Tavern, "WordPress Themes Repository Now Houses 1000 Block Themes": https://wptavern.com/wordpress-themes-repository-now-houses-1000-block-themes
- WP Tavern, "Why Aren't More WordPress Theme Authors Creating Block Themes?": https://wptavern.com/what-arent-more-wordpress-theme-authors-creating-block-themes
- WP Tavern, "Wei: A Free Minimalist WordPress Theme From Rich Tabor": https://wptavern.com/wei-a-free-minimalist-wordpress-theme-from-rich-tabor
- WordPress Developer Blog, "Make your site's typography make a statement": https://developer.wordpress.org/news/2023/07/make-your-sites-typography-make-a-statement/
- WordPress Developer Blog (Justin Tadlock), "You don't need theme.json for block theme styles": https://developer.wordpress.org/news/2025/07/you-dont-need-theme-json-for-block-theme-styles/
- WordPress Developer Blog, "Border radius size presets in WordPress 6.9": https://developer.wordpress.org/news/2025/09/border-radius-size-presets-in-wordpress-6-9/
- WooCommerce Developer Docs, "Theming Woo blocks": https://developer.woocommerce.com/docs/theming/block-theme-development/theming-woo-blocks/

**Hacker News**
- Adrian Krebs, "Scoring Show HN submissions for AI design patterns": https://www.adriankrebs.ch/blog/design-slop/
- Hacker News discussion of the above (235 comments, read via the Algolia API): https://news.ycombinator.com/item?id=47864393 (https://hn.algolia.com/api/v1/items/47864393)
- Hacker News, "Tell HN: I'm tired of formulaic, 'LLM house style' Show HN submissions" (read via the Algolia API): https://news.ycombinator.com/item?id=44780249 (https://hn.algolia.com/api/v1/items/44780249)


**Hacker News and Reddit (via the Algolia API and Reddit RSS; the large threads were read through keyword filters)**
- HN, Cloudflare Quick Tunnels thread (critique of a one-shot Claude landing page): https://news.ycombinator.com/item?id=49754785
- HN, Noodle Gallery thread ("typical front-end tells of Fable and Opus"): https://news.ycombinator.com/item?id=49787684
- HN, "The asteroid hitting front-end web dev": https://news.ycombinator.com/item?id=49555233
- HN, "Is AI causing a repeat of frontend's lost decade?": https://news.ycombinator.com/item?id=48321631
- HN, LearnVector thread: https://news.ycombinator.com/item?id=49092499
- HN, "Why Addresses Have Numbers" thread: https://news.ycombinator.com/item?id=49245646
- HN, "The AI Aesthetic": https://news.ycombinator.com/item?id=49117099
- HN, "Slightly reducing the sloppiness of AI front end": https://news.ycombinator.com/item?id=48504912
- HN, streaming-price Show HN: https://news.ycombinator.com/item?id=49641215
- HN, interview-prep Show HN: https://news.ycombinator.com/item?id=49643992
- HN, Hallmark anti-slop skill: https://news.ycombinator.com/item?id=49058547
- HN, "Ask HN: Wargames-like UX": https://news.ycombinator.com/item?id=47774003
- HN, "How much of HN is about AI": https://news.ycombinator.com/item?id=49449648
- HN, AI lawn diagnosis Show HN: https://news.ycombinator.com/item?id=48544823
- HN, "Laws of Software Engineering": https://news.ycombinator.com/item?id=47847179
- HN, combustion engine simulator (quotes Claude Code's frontend-design clusters): https://news.ycombinator.com/item?id=48795900
- HN, Apache Iggy / "Every Claude-based vibe coded app looks identical" / Discovery Loop / 2018 "Why do all websites look the same?": https://news.ycombinator.com/item?id=49510540 , https://news.ycombinator.com/item?id=48942000 , https://news.ycombinator.com/item?id=49184960 , https://news.ycombinator.com/item?id=18414001
- Reddit r/web_design, "What makes a UI look AI generated": https://www.reddit.com/r/web_design/comments/1wkwns6/what_makes_a_ui_look_ai_generated/
- Reddit r/web_design, "Designer in our company regressed too much with…": https://www.reddit.com/r/web_design/comments/1w2308l/designer_in_our_company_regressed_too_much_with/
- Reddit r/web_design, "Is this design AI generated?": https://www.reddit.com/r/web_design/comments/1v5iocm/is_this_design_ai_generated/

**More articles**
- febbhav, "signs-of-ai-design" (GitHub taxonomy): https://github.com/febbhav/signs-of-ai-design
- tailthemes, "AI design slop quality gate": https://tailthemes.com/blog/ai-design-slop-quality-gate
- volpe, "Reduce slop": https://envs.net/~volpe/blog/posts/reduce-slop.html
- Jim Nielsen, "The AI aesthetic": https://blog.jim-nielsen.com/2026/ai-aesthetic/
- "AI design convergence" study: https://ai-design-convergence.vercel.app
- vibecheck.fail: https://www.vibecheck.fail/

**Directories used to find the section 5 sites**
- Siteinspire home: https://www.siteinspire.com/ ; E-commerce category: https://www.siteinspire.com/websites/category/e-commerce ; Food & drink category: https://www.siteinspire.com/websites/category/food-and-drink
- Minimal Gallery: https://minimal.gallery/
- Hoverstat.es: https://www.hoverstat.es/

### 4.2 Seen but not read (search results or failed fetches; used only for search-summary claims or not at all)

- Hacker News, "AI Keeps Building the Same Purple Gradient Website" (no readable comments when fetched): https://news.ycombinator.com/item?id=46532362
- Yuwen Lu, "Signs of vibe coded UI" (X article, HTTP 402 when fetched): https://x.com/yuwen_lu_/article/2041187936738447565
- Kai Ni, "Why Do AI-Generated Websites Always Favour Blue-Purple Gradients?" (Medium, 403): https://medium.com/@kai.ni/design-observation-why-do-ai-generated-websites-always-favour-blue-purple-gradients-ea91bf038d4c
- Boris Müller, "On the visual weariness of the web" (Medium, 403): https://medium.com/@borism/on-the-visual-weariness-of-the-web-8af1c94e4ee2
- freedesignmd, "why shadcn looks generic and how to fix it": https://freedesignmd.com/blog/shadcn-looks-generic
- AI Website Detector (stack fingerprint: Next.js + Tailwind + shadcn + Lucide + Radix): https://aiwebsitedetector.com/
- Alibaba Product Insights, "How to spot AI-generated 'real person' testimonials": https://www.alibaba.com/product-insights/how-to-spot-ai-generated-real-person-testimonials-on-tech-product-pages.html
- Overpass Studio, "Why SaaS Websites Look The Same": https://www.overpass.studio/blog/why-saas-websites-look-the-same
- Vanszs/Anti-AI-UI (GitHub): https://github.com/Vanszs/Anti-AI-UI
- Typewolf, Google Fonts guide and Typography cheatsheet (fetched, but neither discusses overuse, so not used): https://www.typewolf.com/google-fonts , https://www.typewolf.com/cheatsheet
- Northwestern Kellogg "Detect Fakes" study page (fetched, but gives no cues): https://detectfakes.kellogg.northwestern.edu/
- UK CMA, "Online choice architecture" landing page (the taxonomy is in PDFs that weren't read): https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers
- Make WordPress Core, Default Theme Chat summary: https://make.wordpress.org/core/2024/09/13/default-theme-chat-summary-september-11-2024/
- WP Tavern, "WordPress contributors propose improving block themes visibility in the directory": https://wptavern.com/wordpress-contributors-propose-improving-block-themes-visibility-in-the-directory

**Coverage gaps.** WebSearch hit its session limit partway through this extension, so some requested angles were only partly covered. Reddit was reachable only through RSS for three threads (old.reddit and .json returned 403/429), and no Bluesky thread was read. No page was read on Fonts In Use or Typewolf overuse, Elizabeth Goodspeed, Eye on Design, Figma or Framer community posts, or Awwwards/Godly commentary. Nor did we read Hello Elementor/Astra/Kadence starter-site critiques; WP27 comes from direct familiarity with those demos. The font-overuse claims rest on Web Almanac usage data instead.

---

## 5. What good looks like

These are live, hand-made sites of small businesses and independent creatives that pass the sniff test. Each deep URL was fetched and returned real, current content in September 2026. The one-liners describe the decisions that make each site feel human. Use these as reference, not as templates to copy.

### 5.1 Small businesses

| # | Business | Trade, place | Verified deep URL | What makes it feel human |
|---|---|---|---|---|
| 1 | House of Honey | Interior design studio, South Pasadena and Montecito, US | https://houseofhoney.com/studio | The voice has a point of view ("elegance flirts with eccentricity"). There's a letters column ("Dear Honey") instead of a blog. Real project photography carries the page. |
| 2 | Coming Soon | Home goods and furniture shop, New York, US | https://comingsoonnewyork.com/pages/about | Named owners who "play house seven days a week". Dry, funny copy ("Avoid the void"). Two real addresses with opening hours in plain text. |
| 3 | Huey Lightshop | Handmade lighting, Blue Mountains, Ontario, Canada | https://www.hueylightshop.com/pages/about | Images are captioned like a catalogue raisonné ("FIG 01.", "FIG 02."). Palette names come from the materials (chalk, parchment). Named maker, founding year. |
| 4 | In Common With | Lighting and furniture studio, New York, US | https://www.incommonwith.com/pages/showroom | Describes a real place (square footage, floor, street) and a separate Brooklyn production studio. Restrained copy with no superlatives. |
| 5 | Coutumes | Men's jewellery, France | https://www.coutumes.com/pages/savoir-faire | Bracketed section markers used for a real sequence (the making process). Copy about patina and wear instead of "timeless". Collections named by season ("September Edition"). |
| 6 | PACKBAGS | Modular bags, Amsterdam, Netherlands | https://packbags.nl/pages/about | Specific users (the designer with a sketchbook, the photographer with a camera). Repairable components explained plainly. A real warehouse address. |
| 7 | Little Sesame | Hummus maker and restaurant, Washington DC, US | https://www.eatlittlesesame.com/pages/our-story | A founder story with dates (2016 pop-up to national retail). A house phrase repeated as a signature ("sunny vibes"). Food photography of their actual product. |
| 8 | Potluck | Korean pantry staples, US | https://potluckmarket.com/pages/about | Opens with "Hi there" from the named founder. The heritage story is specific (fermentation, family). Recipes are content, not a "Resources" menu. |
| 9 | Touchy Coffee | Specialty roaster, Troy, New York, US | https://touchycoffee.com/pages/about-us | Tasting notes written with humour ("pool-party neon", "cocoa-dusted brownies"). A real street address. Small asides ("careful not to spill your coffee"). |
| 10 | Miche Coffee | Coffee roaster, Cap Ferret, France | https://michecoffee.com/pages/artists | Each bag is illustrated by a named artist, profiled with their own coffee habit. It is the brand's real point of difference, and it is on the page. |
| 11 | The Daughter | Natural wine bar and bottle shop, Toronto, Canada | https://www.thedaughter.ca/pages/bar | Nav in the trade's own nouns (Bar, Wine, Wine club, Events). "Walk-ins are always welcome" in plain words. Photos of the actual room. |
| 12 | LUCA | Italian restaurant, Clerkenwell, London, UK | https://luca.restaurant/people | A "People" page carrying real job openings and opening hours. Copy about relationships, not "culinary excellence". |
| 13 | L'Enclume | Restaurant with its own farm, Cartmel, Cumbria, UK | https://www.lenclume.co.uk/our-farm | Proof is the farm itself: distance from the kitchen, tour months, what grows there. Nav includes "Our Farm" and "Sample menu". |
| 14 | Laceys Hill Distilling Co. | Small-batch distillery, Australia | https://laceyshill.com.au/pages/process | A numbered sequence used honestly, for a five-step distilling process (rainwater wash to botanicals). |
| 15 | ARENSBAK | Alcohol-free fermented tea, Copenhagen, Denmark | https://arensbak.com/process | The process page names the teas, the 40-day fermentation and the whole botanicals. Lyrical but concrete. |
| 16 | ESR Bespoke | Prestige car repair and restoration, Sydney, Australia | https://www.esrbespoke.au/services | A trade site that avoids SaaS chrome: two real workshop addresses, "since 1989", and services named as the trade names them (insurance repair, detailing, restoration). |

### 5.2 Independent creatives and small studios

| # | Name | Discipline, place | Verified deep URL | What makes it feel human |
|---|---|---|---|---|
| 17 | Scullion Architects | Architecture, Dublin, Ireland | https://scullion.ie/projects | Victor Serif with Founders Grotesk in black and white, one hot orange-red accent, a dated news column, and a gentle "Tell us a little about your project" enquiry instead of "Book a call". |
| 18 | TaylorHare Architects | Landscape-led architecture, UK / Denmark / US | https://taylorhare.com/projects/clausholm-slot/ | Isola in book and slanted cuts on warm paper and forest green. Projects are grouped by landscape type (Fields, Hills, Shorelines), not by service. |
| 19 | Tekt | Prefab residential design, Australia | https://tekt.com.au/process/ | Earth-brown on pale blue-grey. A numbered process (Groundwork, Concept…) used for a real sequence, in plain language. |
| 20 | Studio Gerosa | Architecture (father and son), Lambrugo, Italy | https://www.studio-gerosa.it/it/progetti/casa-in-brianza/source:home | Italian first, a "Regesto" archive, data-sheet project facts (area, year, status). Text-led with no decoration. |
| 21 | Atlason | Furniture and industrial design, New York, US | https://atlason.com/works/akur-table-collection | Neue Haas Grotesk in pure black, writing about materials ("a lens that transforms with light"), and a repeated "A product must be…" manifesto line. |
| 22 | WWAKE | Fine jewellery studio, New York, US | https://wwake.com/blogs/continuum-journal-series/from-reference-to-ring-how-a-custom-piece-begins | A long-form journal about their archive of textile books and mineral specimens. Near-black with pale sage and sky accents. The process is shown, not claimed. |
| 23 | Emi Takahashi | Visual artist and glyph designer, Montréal, Canada | https://emitakahashi.ca/kaze-exhibition | Her name in two scripts, a land acknowledgement, inline glyph footnotes, and travel notes on washi papermaking. Built on Cargo, but unmistakably hers. |
| 24 | Serena Congiu | Makeup artist, Milan, Italy | https://www.serenacongiu.com/information | Arno Pro in strict black and white, bracket-checkbox navigation ("[ ] Information"), and a bio going back to the La Scala academy. |
| 25 | E.F.Productions (Erin Fee) | Creative production and casting, London, UK | https://www.erinfeeproductions.com/info/ | Archivo Narrow throughout, a single rust accent, a two-item nav (Info, Projects) and a three-sentence info page. Proof of restraint. |
| 26 | Lift Type | Independent type foundry, Montpellier, France | https://www.lift-type.fr/pages/about | Every typeface in the menu is set in itself. The copy is a two-person foundry voice, with "since 2014". |
| 27 | Jasper Sharp | Art director, Sydney, Australia | https://www.jaspersharp.co/information/ | A custom typeface, an odd glyph in the nav, stark black and white, and an explicit credit to the web designer. |
| 28 | Metamorphoses | Collectible design gallery | https://metamorphosesobjects.com/about/ | Styrene and a monospace on off-white with muted sage. Curatorial copy built around Ovid's *Metamorphoses*, a real idea rather than a tagline. |
| 29 | Willett | Furniture and spatial design studio | https://willettspace.com/catalogue/popo-chair | Unica77 in dark brown on cream with an oxblood "Willett Red". The catalogue is a spec table (image, product number, sizing, construction, price). |
| 30 | Focal Glow | Lighting design studio, Brisbane and Noosa, Australia | https://focalglow.co/project/sjohavn-house/ | Unica with the Bradford serif, and a live local clock in the header, a fitting detail for a studio that works with light. |

**Also verified, not listed above:** RÙADH (https://www.ruadh.com/pages/studio), Abel (https://abelfragrance.com/pages/about), Eternal Blue (https://eternalblue.co.nz/pages/about), Lafour Studios (https://lafour.com/info), Grapa Studio (https://studiograpa.com/sobre/), and the Chapel of St Thérèse of Lisieux (https://thereseoflisieux.co.nz/visit). The chapel isn't a business, but its visitor page is a model of plain, courteous practical copy.

**What these 30 have in common.** Not one uses a purple accent, an icon-card row, a stat banner, a pill badge or an AI image. Most set one or two non-default typefaces and one accent. Each names real people, places, dates and materials, and uses the trade's own words for its navigation. Numbered sequences appear only where there is a real process (Laceys Hill, Tekt, Coutumes). Several are built on hosted builders (Shopify, Cargo): the tool doesn't determine the look, the decisions do.
