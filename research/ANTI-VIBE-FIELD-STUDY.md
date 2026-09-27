# ANTI-VIBE field study: what AI-built sites actually look like

An empirical companion to [ANTI-VIBE.md](./ANTI-VIBE.md). That document catalogues tells reported by designers and writers. This one measures them. I loaded 65 live pages built with AI site builders, plus 12 hand-built small-business pages as a control, and counted what the browser actually renders: computed fonts, colours, radii, shadows, class names, section order and visible copy.

Research date: 26 and 27 September 2026. All counts below come from the scripts in `research/tools/antivibe/` and can be re-run.

---

## 1. Headline findings

1. **The stack is the fingerprint, not the colour.** 61 of 65 pages ship Tailwind utility classes, 55 ship shadcn/ui tokens, 45 ship Lucide icons. The control group: 0, 1 and 0 of 12. Even the WordPress builder (10Web) now outputs React, Tailwind, shadcn and Lucide inside a WordPress theme.
2. **Indigo is no longer the default AI accent.** Only 3 of 65 pages have a primary accent in the 245 to 275 degree hue band, and only 7 use `indigo-*`, `violet-*` or `purple-*` classes at all. The most common accent family is amber, gold and orange (12 of 54 pages with a chromatic accent). The 2026 "tasteful" default is a warm off-white ground (22 of 65, control 3 of 12), a serif display face (Fraunces, Playfair Display, Cormorant Garamond, Instrument Serif) and a gold or dark green button.
3. **Inter is still everywhere.** Inter is the dominant text face on 31 of 65 pages (33 with Inter Tight). No control page uses it.
4. **Typography micro-tokens are the most reliable visual tell.** Negative H1 tracking (40 of 65, control 0), and 18 of those at exactly -0.025em, which is Tailwind `tracking-tight`. Small uppercase labels with positive tracking (computed: 39 of 65, control 5 of 12), set with `tracking-[0.15em]` or wider classes on 39 of 65. Arbitrary 9 to 11px label text (26 of 65, control 0).
5. **Motion is near universal.** Scroll-reveal (text hidden at opacity 0 until scrolled into view) on 40 of 65, hover lift or scale classes on 36, `transition: all` on 51.
6. **The page skeleton is fixed.** Of 47 multi-section pages, 34 end on a CTA band or contact block, 24 put services second, and 20 place testimonials immediately before the closing CTA.
7. **Em dashes are an AI copy marker in this sample.** 33 of 60 AI pages with 100+ words contain at least one em dash (pooled 6.56 per 1,000 words; Bolt 17.58). The 12 hand-built pages contain none; three of them use a spaced en dash instead.
8. **Exact hex values barely repeat.** Apart from white and black, no hex appears on more than 4 of the 65 pages. A hex blacklist catches little. Lint rules must target class names, token *patterns* (tracking, leading, label size, shadow geometry) and copy.

---

## 2. Method

### 2.1 Where the sample came from

WebSearch was unavailable in this session (the per-session search quota was already spent), so every site was discovered by crawling the builders' own public galleries with Playwright and following their outbound "Preview" or "Visit website" links. Nothing was taken from memory.

| Source | What it is | How AI-built status is demonstrated | Pages |
|---|---|---|---|
| lovable.dev/templates (websites: services, landing page, ecommerce) | Lovable's template gallery; each template embeds a live `*.lovable.app` preview | Hosted on `lovable.app`, "Edit with Lovable" badge in the DOM, Vite asset paths | 16 |
| lovable-partner-directory.lovable.app, community.lovable.app | Lovable's own sites, linked from lovable.dev | Same | 2 |
| bolt.new/resources/templates | Bolt's template gallery; each has a `template-*.bolt.host` preview | Hosted on `bolt.host`, Vite build | 14 |
| v0.app/templates (landing pages category) | v0 community templates, each with a live preview | Rendered from the v0 template page's preview iframe (`*.vusercontent.net`) or its `*.vercel.app` deploy; 2 carry `<meta name="generator" content="v0.app">` | 14 |
| 10web.io/website-templates (9 categories) | 10Web AI builder demo sites on `*.10web.cloud` | `<meta name="generator" content="10Web \| WVC_v 1.27.36 \| WordPress 7.1.2">`, theme `wvc-theme` | 12 |
| durable.com/customer-stories | Real small businesses that Durable features as customers | `cdn.durable.co` assets present on the live site | 7 |

One Durable customer (ONEBIGPARTY, onebigparty.co) was **excluded**: it now runs WordPress with Elementor and has no Durable fingerprint, so it is no longer demonstrably AI-built. That leaves **65 pages**.

**Not sampled, and why.** Framer AI, Relume, Wix ADI, ZipWP/Astra AI, the WordPress.com AI site builder and Elementor AI all market an AI builder, but none of their pages I could reach linked to live generated sites (ZipWP's "Creators" page, WordPress.com's AI builder page and Elementor's AI Site Planner page have no outbound example links; durable.com and 10web.io did). Relume's gallery links to people, not sites. Without web search I could not find "made with" badges for these tools, and I did not guess URLs. Product Hunt was not sampled for the same reason.

**Sampling bias.** Gallery templates (Lovable, Bolt, v0, 10Web) are the vendors' best output, curated and often hand-polished by their authors. Durable customer sites are real businesses and may have been edited by hand after generation. So this sample shows *what polished AI output looks like*, which is the bar our themes compete with, not the average user's first draft.

### 2.2 Control group

12 hand-built small-business pages taken from links already in `research/parts/` (a pottery studio, a clock repairer, two tree surgeons, a surf school, an interior designer, an ice-cream shop, a cleaner, a cidery, a speech therapist, a physio clinic, a removals firm). None carries an AI-builder fingerprint. Several are inner pages rather than home pages, so the control is used for rates of tokens and copy habits, not for section order.

### 2.3 Measurement

- **Playwright (Chromium) at 1440x900**, one page per site: load, dismiss cookie banners, wait 4 s, record which text blocks below the fold are at `opacity: 0` (scroll-reveal), take the first-viewport screenshot, scroll the whole page in 700px steps to trigger lazy content, then run an in-page script (`analyze.mjs`) that reads **computed** styles, not source CSS. v0 previews were measured inside the preview iframe, resized to 1440x900.
- Per page it records: dominant text face by character count, H1 face, size, tracking, alignment and styled spans; text, background, border and button colours (oklch values converted to sRGB hex); border radius per element class (button, card, input, image, badge); every box-shadow and transition; gradients, backdrop filters and blur filters; uppercase tracked labels; icon tiles; equal-width card grids; Lucide icon names; the full list of class names; visible text.
- **WebFetch** was used on 7 pages (AquaFix, Kern Studio, Current Pulse Electric, NaturePure, SmileDent, South Okanagan Tree Works, Optimus) as a cross-check of headings, CTAs and platform fingerprints. WebFetch's summariser drops class names and styles, so it cannot provide the token counts; those come from Playwright. One useful WebFetch finding: Bolt pages return an empty SPA shell with only a `<title>` (nothing for crawlers), while Lovable template pages are prerendered with full text.
- **Section order** was first classified automatically, then corrected by hand from each page's section headings (`order-manual.json`). Codes: H hero, S services or features, A about or story, W work or gallery, T testimonials, L logos or trust strip, N stats, Pr process or "how it works", P pricing, F FAQ, C CTA band, K contact or location, B blog, M marquee or ticker strip, V values or "why us", Q pull quote, Aw awards, Tm team, X other or app content.
- **Copy** was saved as plain text per page and run through `research/tools/copylint.mjs --research`. Em dashes were counted per 1,000 words on pages with 100 or more words.
- **Lovable badge artefacts removed.** The injected "Edit with Lovable" badge adds its own font (Camera Plain), colours (#C5C1B9, #1B1B1B) and a ring shadow; these were filtered out before counting.

Reproduce: `node tools/antivibe/analyze.mjs tools/antivibe/sites.json OUT && node tools/antivibe/analyze.mjs tools/antivibe/control.json CTL && python3 tools/antivibe/aggregate.py OUT CTL > summary.json`.

---

## 3. Sample

Button colour is the first chromatic filled-button colour found (or the first chromatic link, text or surface colour if no button is chromatic); it is the "accent" used in the hue counts. Radius is the most common computed value for buttons and cards; "full (v4 infinity)" is Tailwind v4's `rounded-full`, which computes to `calc(infinity * 1px)`. Tells are the measured booleans from section 4 that are true for the page. Em dash rate is per 1,000 visible words (n/a under 100 words). The last column lists copylint tier-A words found.

<!-- copylint-off -->
| # | Site | URL | Tool | Heading / body face | Button colour | Button / card radius | Section order | Measured tells | Words | Em dash /1k | Tier-A words |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Golden Crust Bakery | <https://golden-crust-bakery.10web.cloud/> | 10Web | Cormorant Garamond / Inter | #D19F47 | 10px / 12px | H S S M S | shadcn tokens, Lucide, neg. H1 tracking, eyebrows, backdrop-blur, one styled H1 word, equal card grid, icon tiles, serif display, blur orb, crushed leading | 196 | 0.0 |  |
| 2 | Current Pulse Electric | <https://current-pulse-electric.10web.cloud/> | 10Web | Inter Tight / Geist | #14253D | 0px / 0px | H A S S V L | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, icon tiles, marquee, numbered labels, Est./Since label, blur orb, mono labels, crushed leading, "Sarah" | 635 | 6.3 |  |
| 3 | Harvest Table Events (catering) | <https://harvest-table-events.10web.cloud/> | 10Web | Inter | none | 2px / 2px | H W A M T C | shadcn tokens, Lucide, neg. H1 tracking, eyebrows, backdrop-blur, equal card grid, icon tiles, radial glow, crushed leading, "Sarah", placeholder contact | 366 | 0.0 |  |
| 4 | IvoryLens (photography) | <https://ivorylens.10web.cloud/> | 10Web | Cormorant Garamond / Inter | #367D65 | 6px / 0px | H S A Q T C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, serif display, blur orb, radial glow, crushed leading | 509 | 3.93 | interplay, meticulously |
| 5 | Joanne Glow Studio (beauty) | <https://joanne-glow-studio.10web.cloud/> | 10Web | Inter | #C9A082 | 0px / 0px | H A S S T C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, equal card grid, icon tiles, numbered labels, Est./Since label, radial glow, mono labels, crushed leading, "Sarah" | 592 | 8.45 | unveiling |
| 6 | Happy Paws Hospital (vet) | <https://happy-paws-hospital.10web.cloud/> | 10Web | Outfit | #3B78CE | 20px / 0px | H S V T W C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, backdrop-blur, one styled H1 word, equal card grid, blur orb, radial glow, crushed leading, "Sarah" | 388 | 0.0 |  |
| 7 | SmileDent (dentist) | <https://smiledent.10web.cloud/> | 10Web | Inter | #132639 | full (v4 infinity) / 32px | H L S Pr V C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, icon tiles, pill buttons, blur orb, radial glow, mono labels, crushed leading, "Sarah", placeholder contact | 562 | 0.0 |  |
| 8 | Sparkle and Shine Maids | <https://sparkle-and-shine-maids.10web.cloud/> | 10Web | Inter | #247EA8 | 2px / 2px | H A S T C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, one styled H1 word, equal card grid, numbered labels, Est./Since label, blur orb, mono labels, crushed leading, "Sarah", placeholder contact | 656 | 7.62 | meticulous, seamless |
| 9 | Sterling Law Associates | <https://sterling-law-associates.10web.cloud/> | 10Web | Inter | #BD284D | 0px / 0px | H S N T K | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, equal card grid, icon tiles, blur orb, dark page, mono labels, crushed leading, placeholder contact, gradient text | 508 | 0.0 | realm |
| 10 | Timbercraft Artisans (carpenter) | <https://timbercraft-artisans.10web.cloud/> | 10Web | Inter | #EE9D2B | 0px / 0px | H A Pr A M C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, numbered labels, Est./Since label, blur orb, mono labels, crushed leading | 597 | 35.18 | elevate |
| 11 | Velvet Shears (salon) | <https://velvet-shears.10web.cloud/> | 10Web | Inter Tight | #AC3960 | 0px / 0px | H A V Pr M P | shadcn tokens, Lucide, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, icon tiles, numbered labels, Est./Since label, radial glow, mono labels, crushed leading, "Sarah", placeholder contact | 797 | 3.76 | elevate, seamless, unparalleled, vibrant |
| 12 | Vow Venue (wedding) | <https://vow-venue.10web.cloud/> | 10Web | Cormorant Garamond / Inter | #CEB27E | 0px / 0px | H A S V T K | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, equal card grid, serif display, blur orb, mono labels | 411 | 0.0 | meticulous, seamless, unparalleled |
| 13 | Minimalist architect portfolio | <https://template-minimalist-architect-portfolio.bolt.host/> | Bolt | Inter | none | 0px / None | H W A | shadcn tokens, neg. H1 tracking, scroll-reveal, eyebrows, numbered labels, crushed leading | 179 | 27.93 |  |
| 14 | Astralis (space tourism) | <https://template-astralis-space-tourism.bolt.host/> | Bolt | Cormorant Garamond / Space Grotesk | #D9B76B | full (9999px) / 16px | H S Pr V T C | shadcn tokens, Lucide, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, icon tiles, marquee, pill buttons, serif display, blur orb, radial glow, dark page, crushed leading, gradient text | 682 | 16.13 | showcase |
| 15 | Harvest Guide (market directory) | <https://template-harvest-guide.bolt.host/> | Bolt | Fraunces / Inter | #1E6745 | 8px / 14px | H X | shadcn tokens, Lucide, neg. H1 tracking, eyebrows, backdrop-blur, serif display, Est./Since label, crushed leading | 920 | 6.52 | in the heart of |
| 16 | Kern Studio (agency) | <https://template-kern-studio.bolt.host/> | Bolt | Syne | #FF4D00 | None / None | H M W S Aw B | neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, marquee, numbered labels, Est./Since label, dark page, mono labels, crushed leading | 418 | 19.14 |  |
| 17 | Lumiere Skin (skincare) | <https://template-lumiere-skin.bolt.host/> | Bolt | Cormorant Garamond / Inter | #A98F63 | 0px / 0px | H M S Pr C | shadcn tokens, neg. H1 tracking, eyebrows, backdrop-blur, one styled H1 word, equal card grid, marquee, serif display, numbered labels, blur orb, dark page, crushed leading | 364 | 27.47 |  |
| 18 | Maison Voyage (travel) | <https://template-maison-voyage.bolt.host/> | Bolt | Fraunces / Inter | #0B6B5C | 0px / 16px | H S V T C | shadcn tokens, Lucide, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, serif display, Est./Since label, radial glow, crushed leading | 424 | 11.79 |  |
| 19 | Meridian Capital (VC) | <https://template-meridian-capital.bolt.host/> | Bolt | Fraunces / Inter | #98563E | 0px / 0px | H A W X | shadcn tokens, neg. H1 tracking, scroll-reveal, eyebrows, one styled H1 word, equal card grid, marquee, serif display, numbered labels, crushed leading | 500 | 14.0 |  |
| 20 | Nestora (real estate) | <https://template-nestora-real-estate.bolt.host/> | Bolt | Plus Jakarta Sans / Inter | #144233 | full (9999px) / 16px | H X | shadcn tokens, Lucide, neg. H1 tracking, eyebrows, backdrop-blur, icon tiles, pill buttons, crushed leading, placeholder contact | 461 | 2.17 |  |
| 21 | Noir Agency | <https://template-noir-agency.bolt.host/> | Bolt | Clash Display / Satoshi | #D7FF3F | 0px / 0px | H M W S Aw | neg. H1 tracking, scroll-reveal, eyebrows, one styled H1 word, marquee, numbered labels, Est./Since label, blur orb, dark page, crushed leading | 361 | 47.09 |  |
| 22 | Nonprofit site | <https://template-nonprofit-website.bolt.host/> | Bolt | Fraunces / Inter | #265141 | full (9999px) / 16px | H A W Q S N B C | shadcn tokens, Lucide, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, icon tiles, pill buttons, serif display, Est./Since label, radial glow, "Sarah", placeholder contact | 1582 | 15.17 |  |
| 23 | Premium SaaS landing | <https://template-premium-saas-dashboard-lp.bolt.host/> | Bolt | Inter | #3B5BFF | 6px / 0px | H S X T P C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, one styled H1 word, equal card grid, marquee, numbered labels, radial glow, dark page, crushed leading | 640 | 12.5 |  |
| 24 | Still (meditation retail) | <https://template-still-meditation.bolt.host/> | Bolt | Fraunces / Inter | #E6DCCB | full (9999px) / 24px | H S S X T C | shadcn tokens, neg. H1 tracking, scroll-reveal, eyebrows, one styled H1 word, equal card grid, pill buttons, serif display, numbered labels, radial glow | 303 | 13.2 |  |
| 25 | Townhall Events | <https://template-townhall-events.bolt.host/> | Bolt | Instrument Serif / Inter | #047857 | full (9999px) / None | X | shadcn tokens, Lucide, neg. H1 tracking, backdrop-blur, one styled H1 word, equal card grid, pill buttons, serif display, crushed leading | 985 | 4.06 |  |
| 26 | Vestige (fashion editorial) | <https://template-vestige-fashion.bolt.host/> | Bolt | Italiana / Space Mono | none | None / None | H Q W X | scroll-reveal, marquee, serif display, numbered labels, radial glow, dark page, mono labels | 259 | 123.55 |  |
| 27 | Color Wonder Balloon Co. | <https://colorwonderballoons.com/> | Durable | Libre Franklin | #B40CC0 | full (9999px) / None | H W A K | pill buttons | 618 | 0.0 |  |
| 28 | Bowen Island Boat Charters | <https://bowenboatcharter.ca/> | Durable | Playfair Display / Source Sans 3 | #0B3D4A | 8px / None | H S T W C | equal card grid, serif display | 324 | 3.09 |  |
| 29 | Little Cooks Club | <https://littlecooksclub.ca/> | Durable | Nunito / Raleway | #EA9999 | 8px / 32px | H S |  | 125 | 0.0 | empower |
| 30 | Digital Natives Media | <https://dnm-nyc.com/> | Durable | Roboto / Poppins | none | 8px / 16px | H S A W A L K | scroll-reveal, dark page | 439 | 0.0 | elevate |
| 31 | NaturePure Cleaning Co. | <https://naturepurecleaning.com/> | Durable | Ovo / Quattrocento | none | 8px / 16px | H A S K T C | scroll-reveal, serif display | 289 | 3.46 | elevate |
| 32 | Prolific Pours (bar catering) | <https://www.prolificpours.com/> | Durable | Playfair Display | #D4AF37 | 0px / None | H S V X V T L C | scroll-reveal, serif display | 1111 | 1.8 | seamless, seamlessly |
| 33 | South Okanagan Tree Works | <https://southokanagantreeworks.com/> | Durable | Playfair Display / Source Sans 3 | #91C09F | 8px / None | H S A L C | equal card grid, serif display, Est./Since label | 339 | 2.95 |  |
| 34 | Apex (injury law firm) | <https://amiable-arc-archive.lovable.app/> | Lovable | Playfair Display / Inter | #2E405C | full (9999px) / 16px | H A C V B | shadcn tokens, Lucide, eyebrows, one styled H1 word, equal card grid, pill buttons, serif display, unused toaster, "Sarah" | 359 | 0.0 |  |
| 35 | AquaFix (plumbing) | <https://aquafix-flow.lovable.app/> | Lovable | system-ui stack | #00378F | full (9999px) / 24px | H A S W A S T B K | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, backdrop-blur, one styled H1 word, equal card grid, icon tiles, marquee, pill buttons, numbered labels, Est./Since label, unused toaster, placeholder contact | 1421 | 0.0 |  |
| 36 | Bakery order page | <https://bakery-order-page-fa48c2b2.lovable.app/> | Lovable | Fredoka / Inter | #1B3422 | full (9999px) / 12px | H S S T K | shadcn tokens, neg. H1 tracking, backdrop-blur, pill buttons, placeholder contact | 144 | 34.72 |  |
| 37 | Bellanova template (preview is a gallery "Coming Soon" page) | <https://kind-bloom-box.lovable.app/> | Lovable | Playfair Display / system-ui stack | none | 0px / None | H | shadcn tokens, neg. H1 tracking, eyebrows, serif display, dark page, unused toaster, crushed leading | 26 | n/a |  |
| 38 | BuildRight (construction estimator) | <https://swift-build-cost.lovable.app/> | Lovable | Inter | #FBBD23 | 0px / 12px | H Pr T F | shadcn tokens, Lucide, scroll-reveal, backdrop-blur, one styled H1 word, equal card grid, mono labels, unused toaster | 299 | 3.34 |  |
| 39 | Coffee shop order page | <https://coffee-shop-order-page-7ee25194.lovable.app/> | Lovable | Fredoka | #ADCBE1 | full (9999px) / 0px | H X T | shadcn tokens, neg. H1 tracking, equal card grid, pill buttons, dark page | 278 | 3.6 |  |
| 40 | Lovable community hub | <https://community.lovable.app/> | Lovable | Camera Plain | none | full (v4 infinity) / 0px | H S X | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, marquee, pill buttons, blur orb, radial glow, mono labels, crushed leading | 435 | 0.0 |  |
| 41 | Launchpad (waitlist) | <https://earlybird-spot.lovable.app/> | Lovable | DM Sans | none | 14px / 18px | H | shadcn tokens, Lucide, neg. H1 tracking, eyebrows, blur orb, radial glow, dark page, gradient text | 48 | n/a |  |
| 42 | Life coach site | <https://life-coach-website-cms-190c61e3.lovable.app/> | Lovable | Fraunces / Inter | #FF8E8D | 0px / None | H S A P C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, equal card grid, serif display, crushed leading | 224 | 17.86 |  |
| 43 | Lovable partner directory | <https://lovable-partner-directory.lovable.app/> | Lovable | Camera Plain | none | full (v4 infinity) / 16px | H X F | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, equal card grid, marquee, pill buttons, radial glow, mono labels | 765 | 3.92 |  |
| 44 | Prism (product launch) | <https://echo-kindness-lab.lovable.app/> | Lovable | SF Pro Display / SF Pro Text | #ED712C | 1.75px / 0px | H | shadcn tokens | 60 | n/a |  |
| 45 | Raum Studio (agency) | <https://raum-studio-landing-page-b13e8bd4.lovable.app/> | Lovable | Inter | #E2A4A7 | 0px / None | H W Pr C | shadcn tokens, Lucide, scroll-reveal, backdrop-blur, equal card grid, unused toaster, crushed leading, gradient text | 227 | 0.0 |  |
| 46 | Revio (fintech SaaS) | <https://revio-landing-page-9f7ffd26.lovable.app/> | Lovable | Inter Tight | #6142FF | 10px / 16px | H S S S L L A V B | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, backdrop-blur, equal card grid, unused toaster, "Sarah" | 519 | 13.49 | seamless, seamlessly |
| 47 | Thrive (movement studio) | <https://cozy-gleam-logic.lovable.app/> | Lovable | Inter | #C97A63 | 0px / None | H A X | shadcn tokens, Lucide, neg. H1 tracking, backdrop-blur, unused toaster, crushed leading | 90 | n/a | empower |
| 48 | TrimSync (barbershop) | <https://trim-tune-appointments.lovable.app/> | Lovable | Bebas Neue / Inter | #C1A05C | 0px / 0px | H S C W T K | shadcn tokens, Lucide, neg. H1 tracking, eyebrows, backdrop-blur, equal card grid, marquee, dark page, unused toaster, crushed leading, placeholder contact | 470 | 0.0 |  |
| 49 | Velvet (beauty salon) | <https://my-place-booking.lovable.app/> | Lovable | Inter | #2478FF | full (9999px) / 12px | X | shadcn tokens, Lucide, icon tiles, pill buttons, unused toaster, placeholder contact | 114 | 0.0 |  |
| 50 | VitalPath (yoga studio) | <https://huggy-data-play.lovable.app/> | Lovable | DM Serif Display | #D39797 | 20px / 24px | H X S X Tm S X B C | shadcn tokens, Lucide, eyebrows, equal card grid, marquee, serif display, unused toaster, "Sarah" | 454 | 4.41 | empowers, unlock |
| 51 | Wildhaven (glamping) | <https://tranquil-treks-reserve.lovable.app/> | Lovable | DM Sans | none | 6px / 8px | H S A C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, icon tiles, unused toaster | 229 | 0.0 |  |
| 52 | Auralink SaaS landing | <https://v0.app/templates/zoQPxUaTqvE> | v0 | Figtree | #156D95 | full (v4 infinity) / 40px | H P F | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, backdrop-blur, icon tiles, pill buttons, mono labels, "Sarah" | 380 | 2.63 | leverages, seamlessly |
| 53 | Brillance SaaS landing | <https://v0.app/templates/zdiN8dHwaaT> | v0 | Inter | #581C87 | 0px / 0px | H S L S N S T P X | shadcn tokens, scroll-reveal, backdrop-blur, icon tiles, blur orb | 724 | 0.0 | seamless, seamlessly |
| 54 | COMPUTE AI agents | <https://v0-compute-11.vercel.app/> | v0 | Instrument Sans / JetBrains Mono | #ECA8D6 | 0px / 0px | H S Pr X N X X X T P C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, equal card grid, numbered labels, blur orb, radial glow, dark page, mono labels, crushed leading | 1883 | 0.0 |  |
| 55 | Flowly SaaS landing | <https://v0.app/templates/8Y9E0cStKrW> | v0 | Onest | #EEBAC1 | 0px / 12px | H S Pr L P F | shadcn tokens, Lucide, one styled H1 word, equal card grid, icon tiles, dark page | 378 | 0.0 | seamlessly |
| 56 | Foodie Wagon | <https://v0.app/templates/GN3Z2rw5BZz> | v0 | Oswald | #F5BA14 | 16px / 16px | H S K | shadcn tokens, backdrop-blur, equal card grid, icon tiles, blur orb, dark page | 442 | 0.0 |  |
| 57 | Homie | <https://v0.app/templates/aAiqtWslee0> | v0 | Playfair Display / Inter | #007A55 | 16px / 16px | H S X N S T F | shadcn tokens, Lucide, scroll-reveal, eyebrows, backdrop-blur, one styled H1 word, equal card grid, icon tiles, serif display, crushed leading | 1313 | 0.0 | seamless |
| 58 | Hously (architecture studio) | <https://v0.app/templates/8o7jKw7qwlb> | v0 | Satoshi | #FFD6A8 | 0px / None | H A W S F C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, one styled H1 word, equal card grid, numbered labels, crushed leading | 545 | 1.83 | elevate |
| 59 | Liquid Glass agency | <https://v0.app/templates/cbQ1carSbPX> | v0 | Inter | #1C398E | full (v4 infinity) / 24px | H S W C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, backdrop-blur, equal card grid, icon tiles, pill buttons, blur orb, dark page, gradient text | 231 | 0.0 | seamless, showcase |
| 60 | MindSpace SaaS landing | <https://v0.app/templates/8QhCJAwn16K> | v0 | Onest | #F95E16 | 10px / 14px | H L S Pr N P F | shadcn tokens, Lucide, neg. H1 tracking, equal card grid, icon tiles | 446 | 0.0 |  |
| 61 | Optimus AI platform | <https://v0-optimus-delta.vercel.app/> | v0 | Instrument Sans | #00A63E | 0px / 0px | H S Pr X N X X X T P C | shadcn tokens, Lucide, neg. H1 tracking, scroll-reveal, eyebrows, equal card grid, marquee, numbered labels, radial glow, dark page, mono labels, crushed leading | 968 | 0.0 | seamless, seamlessly |
| 62 | Opus landing page | <https://v0.app/templates/XyHhjIjd6Y2> | v0 | Instrument Serif / Geist | #5B21B6 | 12px / 16px | H A S X L X P | shadcn tokens, Lucide, scroll-reveal, eyebrows, one styled H1 word, equal card grid, serif display, blur orb, gradient text | 138 | 0.0 | showcase |
| 63 | Pointer AI landing | <https://v0.app/templates/XQxxv76lK5w> | v0 | system-ui stack | #6EFCD9 | 40px / 16px | H L S P T F C | shadcn tokens, Lucide, scroll-reveal, backdrop-blur, blur orb, dark page, mono labels | 1083 | 0.0 | empower, seamless, seamlessly |
| 64 | Skal Ventures | <https://v0.app/templates/tnZGzubtsTc> | v0 | Sentient / Geist Mono | #FFC700 | 0px / None | H | shadcn tokens, Lucide, backdrop-blur, one styled H1 word, dark page, mono labels | 22 | n/a | unlock |
| 65 | Son Doong landing | <https://v0.app/templates/ydltQUzdKLK> | v0 | Inter | none | full (v4 infinity) / 16px | H S F K | shadcn tokens, Lucide, neg. H1 tracking, eyebrows, backdrop-blur, equal card grid, icon tiles, pill buttons, numbered labels, dark page | 332 | 0.0 |  |
<!-- copylint-on -->

Excluded: ONEBIGPARTY, <https://onebigparty.co/> (Durable customer story, but the live site is now WordPress plus Elementor).

Control pages: <https://ayumihorie.com/>, <https://www.bowerswatchandclockrepair.com/clockandwatchrepair.htm>, <https://www.acmetreeservices.co.uk/bio-security/>, <https://www.bigbluesurfschool.com/surf-lessons/>, <https://beataheuman.com/pages/how-we-work>, <https://biritemarket.com/creamery/ice-cream/>, <https://www.angelasgreencleaning.com/green-cleaning-services>, <https://www.albemarleciderworks.com/>, <https://appletreeslt.co.uk/fees/>, <https://bodytonicclinic.co.uk/prices/>, <https://www.artemistreeservices.com/areas-covered/>, <https://www.berkshire-removals.co.uk/van-hire/>. Their faces: Cabin, Alegreya, Avenir with Brandon Grotesque, Open Sans (2), Darker Grotesque with Bricolage Grotesque, Garamond with Raleway, Tahoma, Jost, GT Eesti with Oskar One, Lato, Arial.

---

## 4. Frequency table, sorted by prevalence

Per-tool columns are raw counts out of that tool's n. Manual section-order rows use the 47 pages with at least four identified blocks (10Web 12, Bolt 8, Durable 6, Lovable 10, v0 11). "Control" is out of 12 hand-built pages. Rows that detect a Tailwind class name are 0 for the control by construction (no control page uses Tailwind); the computed-style rows are the fair comparison.

<!-- copylint-off -->
| Trait (measured) | AI sample | 10Web | Bolt | Durable | Lovable | v0 | Control (hand-built) |
|---|---|---|---|---|---|---|---|
| *n per group* | 65 | 12 | 14 | 7 | 18 | 14 | 12 |
| Tailwind utility classes in markup (50 or more) | **61/65** | 12 | 13 | 7 | 16 | 13 | 0/12 |
| shadcn/ui CSS variables or semantic classes (--radius, --primary, text-muted-foreground) | **55/65** | 12 | 11 | 0 | 18 | 14 | 1/12 |
| transition-property: all on some element | **51/65** | 12 | 10 | 7 | 9 | 13 | 6/12 |
| Page ends on a CTA band or contact block (manual, of 47 multi-section pages) | **34/47** | 9 | 6 | 6 | 7 | 6 | not coded |
| Any CSS gradient on an element | **46/65** | 12 | 10 | 4 | 10 | 10 | 2/12 |
| Lucide SVG icons (svg.lucide) | **45/65** | 12 | 7 | 0 | 14 | 12 | 0/12 |
| Grid of 3+ equal-width cards, each with a heading and text | **42/65** | 11 | 9 | 2 | 10 | 10 | 3/12 |
| rounded-full class present | **42/65** | 2 | 12 | 3 | 13 | 12 | 0/12 |
| Negative letter-spacing on the H1 | **40/65** | 11 | 10 | 0 | 12 | 7 | 0/12 |
| Scroll-reveal: 3+ text blocks below the fold at opacity 0 on load | **40/65** | 10 | 10 | 3 | 8 | 9 | 1/12 |
| A Tailwind stock box-shadow geometry (shadow-sm to shadow-2xl) | **39/65** | 12 | 6 | 0 | 10 | 11 | 1/12 |
| 2+ small (15px or less) uppercase labels with positive tracking | **39/65** | 11 | 12 | 0 | 9 | 7 | 5/12 |
| tracking-[0.15em] to [0.5em] or tracking-widest class | **39/65** | 11 | 12 | 0 | 8 | 8 | 0/12 |
| Filled CTA starting Book, Get, Start, Schedule, Request or Reserve | **38/65** | 12 | 3 | 5 | 8 | 10 | 5/12 |
| backdrop-filter in use | **36/65** | 10 | 8 | 0 | 10 | 8 | 0/12 |
| hover:-translate-y-* or hover:scale-* classes | **36/65** | 12 | 11 | 1 | 8 | 4 | 0/12 |
| H1 face is the dominant text face | **34/65** | 8 | 3 | 2 | 12 | 9 | 5/12 |
| 1+ em dash in visible copy | **34/65** | 6 | 14 | 4 | 8 | 2 | 0/12 |
| Second block is services/features (manual, of 47) | **24/47** | 4 | 4 | 4 | 5 | 7 | not coded |
| shadcn Button signature classes ([&_svg]:size-4, has-[>svg]:px-3) | **33/65** | 12 | 3 | 2 | 9 | 7 | 0/12 |
| Display leading 1.05 or less via arbitrary class or leading-none | **32/65** | 11 | 11 | 0 | 6 | 4 | 0/12 |
| bg-gradient-to-* utility | **31/65** | 9 | 7 | 0 | 6 | 9 | 0/12 |
| Hero, then services, then testimonials, in that order (manual, of 47) | **21/47** | 6 | 4 | 3 | 3 | 5 | not coded |
| rounded-xl or rounded-2xl present | **29/65** | 2 | 6 | 4 | 8 | 9 | 0/12 |
| Testimonials directly before the closing CTA/contact (manual, of 47) | **20/47** | 7 | 4 | 3 | 3 | 3 | not coded |
| Most common card radius 8 to 24px | **27/65** | 1 | 6 | 2 | 10 | 8 | 2/12 |
| One word or phrase in the H1 in another colour, face or italic | **26/65** | 8 | 10 | 0 | 3 | 5 | 2/12 |
| Body paragraph 16px or smaller | **26/65** | 0 | 8 | 0 | 14 | 4 | 6/12 |
| Arbitrary 9 to 11px text classes (text-[10px]) | **26/65** | 10 | 11 | 0 | 4 | 1 | 0/12 |
| copylint tier-A word in visible copy | **26/65** | 7 | 2 | 4 | 3 | 10 | 1/12 |
| 1px decorative rule elements (h-px, w-px) | **25/65** | 11 | 7 | 0 | 2 | 5 | 0/12 |
| H1 to body size ratio under 4 | **23/65** | 2 | 7 | 4 | 5 | 5 | 8/12 |
| Logo or 'trusted by' strip (automatic heuristic) | **23/65** | 3 | 4 | 6 | 6 | 4 | 1/12 |
| Serif display face on the H1 | **22/65** | 3 | 9 | 4 | 4 | 2 | 1/12 |
| Image zoom on hover (group-hover:scale-*) | **22/65** | 9 | 6 | 1 | 4 | 2 | 0/12 |
| Centred H1 | **21/65** | 3 | 4 | 1 | 6 | 7 | 4/12 |
| Most common card radius 12 to 16px | **21/65** | 1 | 5 | 2 | 6 | 7 | 0/12 |
| 3+ icon tiles (32 to 72px filled square holding one icon) | **21/65** | 7 | 3 | 0 | 3 | 8 | 0/12 |
| Default-palette colour classes (bg-gray-900, text-amber-500 ...) | **21/65** | 1 | 3 | 3 | 3 | 11 | 0/12 |
| Dark-dominant page (largest surface luminance under 0.05) | **20/65** | 1 | 6 | 1 | 4 | 8 | 1/12 |
| Element with filter: blur(3px or more) | **20/65** | 9 | 3 | 0 | 2 | 6 | 0/12 |
| Arrow nudge on hover (group-hover:translate-x-1) | **19/65** | 7 | 4 | 0 | 1 | 7 | 0/12 |
| Monospace face used for labels | **18/65** | 8 | 2 | 0 | 3 | 5 | 0/12 |
| Numbered section labels (01, No. 01, followed by a dash) | **18/65** | 5 | 8 | 0 | 1 | 4 | 0/12 |
| Pill-shaped primary buttons | **17/65** | 1 | 5 | 1 | 7 | 3 | 0/12 |
| Radial gradient (glow, halo) | **17/65** | 6 | 6 | 0 | 3 | 2 | 0/12 |
| Marquee or ticker animation class | **14/65** | 1 | 7 | 0 | 5 | 1 | 0/12 |
| Pill badge (34px tall or less, fully rounded) | **13/65** | 2 | 4 | 0 | 2 | 5 | 2/12 |
| 'Est. YYYY' or 'Since YYYY' label | **12/65** | 5 | 5 | 1 | 1 | 0 | 3/12 |
| Testimonial or team name 'Sarah' | **12/65** | 7 | 1 | 0 | 3 | 1 | 0/12 |
| Star ratings (3+ stars) | **11/65** | 4 | 1 | 0 | 5 | 1 | 1/12 |
| Empty shadcn toast viewport shipped (md:max-w-[420px]) | **11/65** | 0 | 0 | 0 | 11 | 0 | 0/12 |
| text-balance class | **11/65** | 0 | 2 | 0 | 5 | 4 | 0/12 |
| Placeholder phone or address (555, 123 Main St, (111)) | **11/65** | 5 | 2 | 0 | 4 | 0 | 0/12 |
| Card grid whose cards each start with an icon tile | **9/65** | 2 | 1 | 0 | 1 | 5 | 0/12 |
| Surface or button colour within dE2000 10 of Tailwind indigo/violet/purple 500 or 600 | **8/65** | 0 | 3 | 0 | 3 | 2 | 4/12 |
| Viewport-width display type (text-[13vw]) | **7/65** | 1 | 5 | 0 | 0 | 1 | 0/12 |
| indigo-*, violet-* or purple-* classes | **7/65** | 0 | 1 | 0 | 1 | 5 | 0/12 |
| 'Scroll' cue text | **7/65** | 4 | 2 | 0 | 0 | 1 | 0/12 |
| Gradient text (background-clip: text) | **6/65** | 1 | 1 | 0 | 2 | 2 | 0/12 |
| Fragment headline ('Precision. Power. Protection.') | **6/65** | 1 | 1 | 0 | 0 | 4 | 0/12 |
| Heading 'The Art of ...' | **5/65** | 3 | 0 | 0 | 1 | 1 | 0/12 |
| Social-proof count ('4,300+ satisfied clients') | **5/65** | 1 | 1 | 0 | 2 | 1 | 0/12 |
| Emoji in visible copy | **4/65** | 0 | 0 | 0 | 2 | 2 | 1/12 |
| 'Where X meets Y' | **4/65** | 3 | 1 | 0 | 0 | 0 | 0/12 |
| Primary button hue 245 to 275 deg (indigo/violet) | **3/65** | 0 | 0 | 0 | 1 | 2 | 0/12 |
| Rounded images (8px or more) | **3/65** | 0 | 0 | 1 | 2 | 0 | 1/12 |
| snake_case or bracketed UI labels ('OUR_STORY') | **3/65** | 2 | 0 | 0 | 0 | 1 | 0/12 |
| Font Awesome icons | **0/65** | 0 | 0 | 0 | 0 | 0 | 6/12 |
<!-- copylint-on -->

Supporting numbers:

- **Stack**: 32 of 65 are Vite builds (all Lovable and Bolt), 21 are Next.js (all v0 and all current Durable sites), 12 are WordPress (all 10Web).
- **Accent hue** (54 pages with a chromatic accent): 0 to 30 deg 9, 30 to 60 deg 12, 60 to 90 deg 1, 120 to 150 deg 3, 150 to 180 deg 8, 180 to 210 deg 4, 210 to 240 deg 8, 240 to 270 deg 2, 270 to 300 deg 2, 300 to 330 deg 1, 330 to 360 deg 4.
- **Warm off-white ground** (a top-three surface colour with hue 20 to 60 deg, saturation 0.12 or more, lightness 0.88 or more): 22 of 65; control 3 of 12 (a cidery, a potter and an interior designer, all of whom have a material reason).
- **Gold primary button** (hue 25 to 50 deg, saturation 0.25 to 0.75, lightness 0.35 to 0.75): 7 of 65.
- **Em dashes**: 212 em dashes in 32,341 words across 60 AI pages with 100+ words, pooled 6.56 per 1,000. By tool: Bolt 17.58 (14 of 14 pages have one), 10Web 6.43 (6 of 12), Lovable 3.87 (7 of 14), Durable 1.54 (4 of 7), v0 0.23 (2 of 13). Control: 0 in 6,362 words; spaced en dashes appear on 3 control pages. The highest AI rates: Vestige 123.6, Noir 47.1, Timbercraft 35.2, Bakery order page 34.7, architect portfolio 27.9, Lumiere 27.5. Much of it is decorative: an em dash used as a separator inside labels ("EST. 2015" then a dash then the brand name, or "Selected Works" repeated either side of a dash).
- **Emoji** (Unicode emoji presentation only, not symbols like the copyright sign): 4 of 65. copylint's broader emoji rule reports 48 of 65 in research mode because it also matches symbols such as arrows and stars; the stricter count is the honest one.

---

## 5. Most common exact tokens

### 5.1 Fonts

| Role | AI sample (65) | Control (12) |
|---|---|---|
| Dominant text face | Inter 31, Inter Tight 2, system-ui stack (Tailwind default `ui-sans-serif`) 3, Geist 2, Satoshi 2, Source Sans 3 2, DM Sans 2, Onest 2, Camera Plain 2 (Lovable's own brand face on its community and partner sites), then 17 faces used once (Outfit, Space Grotesk, Syne, Poppins, Raleway, Figtree, Instrument Sans, Libre Franklin ...) | No face repeats except Open Sans (2). No Inter. |
| H1 face | Inter 14, Fraunces 6, Playfair Display 6, Cormorant Garamond 5, Inter Tight 3, Instrument Serif 2, DM Sans 2, Instrument Sans 2, Onest 2, Fredoka 2 | All different |
| Serif display on H1 | 22 of 65 (Fraunces, Playfair Display, Cormorant Garamond, Instrument Serif, DM Serif Display, Ovo, Italiana) | 1 of 12 |
| Monospace label face | 18 of 65 (JetBrains Mono on 6 of 12 10Web sites; Geist Mono, Space Mono, `font-mono`) | 0 |

The 10Web trio is almost fixed: **Inter body, Cormorant Garamond or Playfair Display display, JetBrains Mono labels** (Inter dominant on 9 of 12 plus Inter Tight on 1, Cormorant Garamond or Playfair Display on 8, JetBrains Mono on 6).

### 5.2 Colour

- Exact hex values are dispersed. Most repeated non-white values: `#FBFAF9` (4, all 10Web), `#111827` Tailwind gray-900 (4), `#737373` neutral-500 (4), `#F8FAFC` slate-50 (3), `#E3E6E8` (3), `#141414` (3). The full Tailwind **stone** ramp (`#1C1917`, `#57534E`, `#78716C`, `#E7E5E4`, `#F5F5F4`) appears together on 2 pages. Two Durable sites use Tailwind gray-600 `#4B5563` and gray-900 `#111827` as secondary button fills.
- Gold primaries observed: `#D4AF37`, `#D19F47`, `#C9A082`, `#CEB27E`, `#D9B76B`, `#A98F63`, `#C1A05C`.
- Indigo/violet: only Revio (`#6142FF`), Brillance (`#581C87`, Tailwind purple-900) and Opus (`#5B21B6`, violet-800) have an accent in the 245 to 275 deg band. 8 pages have *some* surface within dE2000 10 of indigo/violet/purple 500 or 600.

### 5.3 Radius

| Element | Most common computed values (pages) |
|---|---|
| Button | 0px 24, fully rounded 17 (9999px 11, v4 infinity 6), 8px 6, 10px 3, 6px 3 |
| Card | 0px 19, 16px 14, 12px 5, 24px 4, 32px 2, 14px 2 |
| Image | 0px 51, 8px 2, 20px 1 |
| Input | 0px 8, 10px 4, 8px 4, fully rounded 3 |

Square images are the norm (51 of 65). The "sharp editorial" look (0px buttons and cards) is now as common as the rounded SaaS look, so a radius *value* is not a tell by itself; the tell is one radius shared by buttons, cards, badges and inputs.

### 5.4 Shadows (computed, pages using each)

| Tailwind name | Computed value | Pages |
|---|---|---|
| `shadow` | `0 1px 3px 0 rgb(0 0 0 / .1), 0 1px 2px -1px rgb(0 0 0 / .1)` | 17 |
| `shadow-sm` | `0 1px 2px 0 rgb(0 0 0 / .05)` | 16 |
| `shadow-md` | `0 4px 6px -1px rgb(0 0 0 / .1), 0 2px 4px -2px rgb(0 0 0 / .1)` | 13 |
| `shadow-2xl` | `0 25px 50px -12px rgb(0 0 0 / .25)` | 9 |
| `shadow-lg` | `0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1)` | 6 |
| `shadow-xl` | `0 20px 25px -5px rgb(0 0 0 / .1), 0 8px 10px -6px rgb(0 0 0 / .1)` | 2 |

39 of 65 pages use at least one of these exact geometries; 1 of 12 control pages does.

### 5.5 Type scale and tracking

- H1 size: median 80px (58 pages with an H1 of 30px or more); 72px on 11 pages, 96px on 6, 128px on 4. Control H1 median 40px (11 pages with an H1).
- H1 tracking: -0.025em on 18 pages (exactly Tailwind `tracking-tight`), -0.02em 4, -0.04em 4, -0.05em 3, -0.035em 3; zero on 21.
- Body: 18px on 20 pages, 16px on 16, 20px on 12, 14px on 6. Median H1 to body ratio 4.4.
- Most common arbitrary classes on the 46 v0, Lovable and Bolt pages: `tracking-[0.2em]` 16, `text-[10px]` 13, `text-[11px]` 11, `leading-[0.95]` 7, `tracking-[0.3em]` 6, `leading-[0.85]` 6, `leading-[1.05]` 8, `leading-[0.9]` 5, `text-[13vw]` 5.

### 5.6 Spacing and layout

- Container max-width (element wider than 900px): 1280px (`max-w-7xl`) on 36 pages, 1024px (`max-w-5xl`) 22, 1152px (`max-w-6xl`) 18, 1400px (shadcn `container` at 2xl) 9, 1440px 9.
- Section vertical padding on `<section>` elements: 128px (`py-32`) 15, 96px (`py-24`) 10, 160px 6, 112px 5, 144px 5.
- Common layout classes (of 46 v0/Lovable/Bolt pages): `min-h-screen` 39, `md:grid-cols-3` 22, `md:grid-cols-2` 22, `max-w-7xl` 18, `gap-8` 32, `gap-12` 25.

### 5.7 Motion

Transitions (pages): `color 150ms cubic-bezier(0.4, 0, 0.2, 1)` 42 (Tailwind `transition-colors` default), `all 150ms` 22, `all 300ms` 15, `all 500ms` 14, `transform 300ms` 7. Classes (of the 46 v0, Lovable and Bolt pages): `duration-300` 30, `duration-500` 21, `duration-700` 11, `opacity-0` 18, `group-hover:translate-x-1` 10, `group-hover:scale-105` 7, `animate-marquee` 7, `animate-pulse` 6.

### 5.8 Icons

Lucide on 45 of 65 pages. Most used (pages): `menu` 34, `arrow-right` 27, `instagram` 18, `mail` 16, `map-pin` 15, `phone` 14, `arrow-up-right` 13, `chevron-down` 13, `facebook` 11, `twitter` 11, `users` 10, `star` 10, `check` 10, `clock` 9, `quote` 9, `shield-check` 6, `sparkles` 4. Font Awesome: 0 of 65 but 6 of 12 control pages.

### 5.9 Copy phrases (pages containing the phrase)

<!-- copylint-off -->
| Phrase | AI (65) | Control (12) |
|---|---|---|
| "all rights reserved" | 24 | 4 |
| "ready to" (almost always a closing heading, "Ready to ...?") | 14 | 0 |
| "precision" | 11 | 0 |
| "curated" | 11 | 0 |
| "get started" | 11 | 2 |
| "for every" | 11 | 0 |
| "designed for" / "designed to" | 10 / 11 | 0 / 0 |
| "tailored" | 10 | 1 |
| "transform" | 10 | 0 |
| "seamless" (plus "seamlessly" 7) | 10 | 0 |
| "24/7" | 10 | 1 |
| "journey" | 9 | 0 |
| "we believe" | 9 | 0 |
| "New York" (placeholder city on non-NY businesses) | 9 | 0 |
| "attention to detail" | 8 | 1 |
| "bespoke" | 8 | 0 |
| "begins with" | 8 | 0 |
| "start free" | 8 | 0 |
| "your vision" | 7 | 0 |
| "crafted" | 7 | 0 |
| "trusted by" | 7 | 0 |
| "The Art of ..." as a heading | 5 | 0 |
| "Where X meets Y" | 4 | 0 |

copylint tier-A words (occurrences across the AI sample): seamless 20, seamlessly 15, elevate 7, vibrant 4, showcase 4, bespoke 4, meticulous 3, empower 3, interplay 2, unparalleled 2, unlock 2, effortless 2, plus single hits of realm, unveiling, in the heart of, look no further, in today's, leverages. Control: one hit ("in the heart of").

Most frequent filled CTAs: "Book Now" 4, "Book Appointment" 4, "Get started" 5, "Subscribe" 4, "Start free trial" 3, "Get a Free Quote" 2, "Order now" 2. Most frequent tracked labels: "SCROLL" 5, "CONTACT" 4, "BOOK" 3, "OUR STORY", "GET IN TOUCH", "WHAT WE DO", "OUR MISSION", "MOST POPULAR" 2 each.

Headline shapes seen repeatedly: fragment triplets ("Precision. Power. Protection.", "Define. Deploy. Scale.", "Smart. Simple. Brilliant."), the "The Art of the ..." formula ("The Art of the Daily Loaf", "The Art of the Gathering", "THE ART OF THE CUT", "The Art of Visual Storytelling", "The art of woodworking"), and "Your X deserve(s) Y" ("Your Guests Deserve a Bar Worth Talking About", "Every child deserves ...").
<!-- copylint-on -->

---

## 6. Common section orders

From the hand-corrected section codes of the 47 multi-section pages.

**Local-service skeleton (10Web, Durable, Lovable services templates):** `H > A or S > S > (W) > T > C`. Examples: Joanne Glow Studio `H A S S T C`, Sparkle and Shine `H A S T C`, NaturePure `H A S K T C`, Happy Paws `H S V T W C`, Sterling Law `H S N T K`, Vow Venue `H A S V T K`, TrimSync `H S C W T K`, Bakery order page `H S S T K`. 20 of 47 pages put testimonials directly before the closing CTA or contact block.

**SaaS skeleton (v0, Bolt SaaS, Lovable fintech):** `H > (L) > S > Pr > (N) > (T) > P > F or C`. Optimus and COMPUTE are identical in shape (`H S Pr X N X X X T P C`); Flowly `H S Pr L P F`; MindSpace `H L S Pr N P F`; Pointer `H L S P T F C`; Premium SaaS `H S X T P C`. 9 of the 11 pricing blocks are on pages of this type; the other two are a life coach's packages and a salon's price-list download.

**Editorial portfolio skeleton (Bolt agency and fashion templates):** `H > M > W > S > Awards or Journal`. Kern `H M W S Aw B`, Noir `H M W S Aw`.

Positional counts (of 47): last block is a CTA band 26, contact 8, FAQ 4, blog 3, pricing 2. Second block is services 24, about 12. Blocks present anywhere (of 65): hero 63, services 43, CTA 28, testimonials 24, about 23, work or gallery 16, logos 11, process 11, pricing 11, values 10, contact 10, FAQ 9.

The canonical order in ANTI-VIBE L1 (hero, logos, features, how it works, stats, testimonials, pricing, FAQ, CTA) appears only on SaaS-type pages. For small-business pages the observed default is shorter and just as fixed: **hero, one line of "about", a services grid, testimonials, a "Ready to ...?" band, footer.**

---

## 7. WordPress AI builder specifics

<!-- copylint-off -->
Directly relevant because these are the sites our themes compete with.

**10Web AI builder (12 of 12 demo sites measured).**

- Generator meta: `10Web | WVC_v 1.27.36 | WordPress 7.1.2`. Body class `wp-theme-wvc-theme`. Elementor assets are still loaded on all 12.
- The page content is a compiled React build styled with Tailwind and shadcn/ui: 12 of 12 have shadcn tokens and the shadcn Button signature classes, 12 of 12 use Lucide (the `lucide-menu` hamburger on every one), 12 of 12 use Tailwind stock shadows and `transition: all`. The 10Web output is technically a v0-style page wrapped in a WordPress theme, not blocks.
- Type: Inter dominant on 9 of 12 (Inter Tight on 1 more), Cormorant Garamond or Playfair Display on 8, JetBrains Mono labels on 6. Negative H1 tracking 11 of 12. Tiny tracked caps labels 11 of 12. Crushed display leading 11 of 12.
- Decoration: blurred decorative elements 9 of 12, radial glows 6, backdrop blur 10, image zoom on hover 9, hover lift 12, scroll-reveal 10.
- Copy: "Sarah" as a testimonial name 7 of 12 (SmileDent's "Sarah Jenkins, Invisalign Patient"), placeholder phone or address 5, "Est. YYYY" labels 5, "The Art of ..." headings 3, "Where X meets Y" 3, fake editorial metadata such as `№ 01` followed by an em dash and `MASTER CRAFT` and `[01 // 03] · OUR EXPERTISE`, and snake_case nav labels (`OUR_EXPERTISE`, `LET_S_TALK`, `REQUEST_SERVICE`) on Current Pulse Electric.
- Palette: warm off-white grounds on 5 (`#FBFAF9` or `#FBFAF8` on 4), gold or brass primaries on 3 (`#D19F47`, `#C9A082`, `#CEB27E`).

**Durable (7 customer sites).** Next.js with Tailwind but no shadcn or Lucide. Google font pairs are varied (Source Sans 3 with Playfair Display twice, Quattrocento with Ovo, Poppins with Roboto, Raleway with Nunito, Libre Franklin with Libre Baskerville). Durable pages are the least "vibe-coded" by our measures: 0 of 7 negative tracking, 0 of 7 tracked eyebrows. Their tells are structural (6 of 6 multi-section pages end on a CTA or contact block) and copy-level ("Look no further" on Digital Natives Media).

**ZipWP, WordPress.com AI builder, Elementor AI.** Not measured; no public examples were reachable (see 2.1).

**Implication for us.** A block theme that avoids Tailwind, shadcn and Lucide is already structurally different from the leading WordPress AI builder. The visual overlap risk is in type tokens (Inter, Cormorant, JetBrains Mono, tight tracking, 10px tracked caps) and in the page skeleton.

---

<!-- copylint-on -->

## 8. New tells not in ANTI-VIBE.md

Each item is measured above and is not already covered by an ANTI-VIBE rule (or it adds a measurable threshold to one).

<!-- copylint-off -->
1. **Micro-label token: 9 to 11px uppercase at 0.2em to 0.3em tracking.** Computed: 2+ such labels on 39 of 65 pages, control 5 of 12; the arbitrary 9 to 11px size alone on 26 of 65, control 0. ANTI-VIBE T5 bans eyebrows above headings; the observed pattern is broader: the same token is applied to nav links, buttons, meta lines, captions, footers and "SCROLL" cues. Exact classes: `text-[10px] tracking-[0.2em] uppercase`.
2. **Monospace meta labels.** A mono face (JetBrains Mono, Geist Mono, Space Mono) used for small labels on non-technical businesses: 18 of 65, control 0. On a bakery or a wedding venue this is pure decoration.
3. **Fake editorial metadata.** "Est. 2015", "No. 01" section numbers, `[01 // 03]`, a live local clock in the header ("PAR" plus the current time on Kern), coordinates, "Vol." and issue numbers. "Est. or Since YYYY" on 12 of 65 (control 3 of 12, all genuine); numbered labels 18 of 65 (control 0).
4. **snake_case or bracketed UI labels.** `OUR_STORY`, `LET_S_TALK`, `[ CONTACT US ]`: 3 of 65. Developer syntax leaking into customer-facing UI.
5. **Hairline rule ornaments.** A 1px line before or after a label (`w-8 h-px`), often paired with item 1: 25 of 65, control 0.
6. **Arrow nudge on hover.** `group-hover:translate-x-1` on an `arrow-right` or `arrow-up-right` icon inside every link: 19 of 65. Lucide `arrow-right` appears on 27 pages and `arrow-up-right` on 13.
7. **Shipped but unused UI infrastructure.** An empty shadcn toast viewport (`md:max-w-[420px]`, `z-[100]`) on 11 of 18 Lovable pages; shadcn Button signature classes on 33 of 65 pages. Machine-detectable and meaningless on a brochure site.
8. **The warm-luxury escape hatch, gold variant.** ANTI-VIBE C10 names cream, serif and terracotta. The observed 2026 variant is warm off-white (22 of 65), a serif display face (22 of 65: Fraunces, Playfair Display, Cormorant Garamond, Instrument Serif) and a **gold or brass** button (7 of 65), often with italic words in the headline.
9. **Indigo is no longer the discriminator.** Only 3 of 65 pages have an indigo/violet primary. Rules that only ban indigo would pass most AI pages in this sample. Hue alone should not be the colour test; see the lint section for pattern-based tests.
10. **Crushed display leading below 0.95.** `leading-[0.85]` on 6 and `leading-[0.9]` on 5 of the 46 v0, Lovable and Bolt pages. ANTI-VIBE T13 recommends 0.95 to 1.15, which the AI pages also use, so only values under 0.95 discriminate.
11. **Viewport-width wordmark heroes.** A single word or brand name at 13 to 16vw filling the first screen (`text-[13vw]`): 7 of 65, 5 of them Bolt.
12. **Floating "live" chip over the hero photo.** A small white card overlapping the hero image showing fake live data: "Next Available: Today at 2:00 PM" (SmileDent), a "LIVE" fundraising card with a progress bar (BrightRoots), an avatar stack with "4,300+ Satisfied Clients" (AquaFix), an estimate card (BuildRight), a services card (Joanne). Seen in 5 of the 20 screenshots below. ANTI-VIBE L11 covers the SaaS dashboard mockup; this is the small-business version.
13. **Fragment-triplet headlines.** Three one-word sentences with full stops ("Precision. Power. Protection."): 6 of 65, control 0. A three-beat variant of ANTI-VIBE V3.
14. **"The Art of the ..." and "Where X meets Y" headings.** 5 and 4 of 65, control 0.
15. **Placeholder geography.** "New York" on 9 of 65 pages, including businesses with no New York link, and placeholder contact details (555 numbers, "123 Main Street", "(111)222-333-444") on 11 of 65. ANTI-VIBE P1 covers lorem ipsum but not placeholder contact data.
16. **"Sarah" as the default testimonial name.** 12 of 65 (7 of 12 on 10Web). ANTI-VIBE P3 names "Sarah Johnson"; the measured pattern is any Sarah.
17. **Em dash as a label ornament.** Not in prose but inside tiny labels and marquees, pushing Bolt pages to 17.6 em dashes per 1,000 words. Hand-built pages in the control used none.
18. **Template scaffolding leaking into copy.** Section-type names left in visible text ("Social Proof", "Bento grid" on Brillance) and H1s that name the template ("Bakery Order Page", "Revio Landing Page", "RAUM Studio Landing Page", "Life Coach Website + CMS"): 5 of 65.
19. **Tailwind v4 fingerprint.** `rounded-full` in v4 computes to `calc(infinity * 1px)` (reported as 33554400px); seen on the buttons of 9 pages. A CSS or computed-style check can detect it.
20. **SEO-empty shells.** All 14 Bolt pages serve an empty HTML body to non-JS clients (only `<title>`). A block theme renders server-side, which is a real advantage worth keeping.
<!-- copylint-on -->

Traits ANTI-VIBE lists that were **rare** in this sample (useful for prioritising): emoji (4 of 65), gradient text (6), indigo/violet primary (3), rounded images (3), stat row as its own section (4), FAQ (9), pricing (11, all SaaS).

---

## 9. Screenshots

<!-- copylint-off -->
First viewport at 1440x900, captured 27 September 2026.

| | |
|---|---|
| ![AquaFix, Lovable](./screenshots/anti-vibe/01-lov-aquafix.jpg) **01 AquaFix (Lovable).** Coloured last line of H1, pill buttons, avatar stack "4,300+ Satisfied Clients", rounded photo tiles. | ![TrimSync, Lovable](./screenshots/anti-vibe/02-lov-trimsync.jpg) **02 TrimSync (Lovable).** "THE ART OF THE CUT", condensed caps, gold button, dark photo. |
| ![VitalPath, Lovable](./screenshots/anti-vibe/03-lov-vitalpath.jpg) **03 VitalPath (Lovable).** Serif H1 over a pink radial glow, pill buttons, tracked caps nav. | ![BuildRight, Lovable](./screenshots/anti-vibe/04-lov-buildright.jpg) **04 BuildRight (Lovable).** Coloured second line, grid background, floating estimate card, numbered "How It Works". |
| ![Apex, Lovable](./screenshots/anti-vibe/05-lov-apex.jpg) **05 Apex (Lovable).** Italic serif "Injured?", lilac pill button, stock portrait collage, 5-star strip in the top bar. | ![Lumiere, Bolt](./screenshots/anti-vibe/06-bolt-lumiere.jpg) **06 Lumiere (Bolt).** Cream ground, light serif with the last word in gold, hairline plus tracked micro-label, vertical side text, italic ingredient ticker. |
| ![Maison Voyage, Bolt](./screenshots/anti-vibe/07-bolt-maison.jpg) **07 Maison Voyage (Bolt).** One italic word in a centred serif H1, "EST. 1998" label, "SCROLL" cue. | ![Kern Studio, Bolt](./screenshots/anti-vibe/08-bolt-kern.jpg) **08 Kern Studio (Bolt).** Viewport-width wordmark, mono meta line with local clock, "AVAILABLE Q3". |
| ![BrightRoots, Bolt](./screenshots/anti-vibe/09-bolt-nonprofit.jpg) **09 BrightRoots (Bolt).** Italic coloured words mid-H1, floating "LIVE" fund card, "Est. 2014" pill. | ![Nexal, Bolt](./screenshots/anti-vibe/10-bolt-saas.jpg) **10 Nexal (Bolt).** Dark page, blue last phrase, eyebrow, dashboard mockup. |
| ![Meridian, Bolt](./screenshots/anti-vibe/11-bolt-meridian.jpg) **11 Meridian (Bolt).** Cream, thin serif, one terracotta word, stat row with "$850M". | ![Optimus, v0](./screenshots/anti-vibe/12-v0-optimus.jpg) **12 Optimus (v0).** Stat row in the hero ("98%", "300%", "6x"), mono eyebrow, dot-field graphic. |
| ![Hously, v0](./screenshots/anti-vibe/13-v0-hously.jpg) **13 Hously (v0).** "We design spaces that elevate living", gold second line, marble kitchen render, eyebrow over the H1. | ![Lumina, v0](./screenshots/anti-vibe/14-v0-liquid.jpg) **14 Lumina (v0).** "Digital Alchemy", violet-navy radial glow, pill badge, two pill CTAs, "SCROLL". |
| ![Current Pulse Electric, 10Web](./screenshots/anti-vibe/15-10w-electric.jpg) **15 Current Pulse Electric (10Web).** Yellow word in a crushed H1, snake_case nav, ghost "01" watermark. | ![SmileDent, 10Web](./screenshots/anti-vibe/16-10w-smiledent.jpg) **16 SmileDent (10Web).** Italic serif words inside a sans H1, floating "Next Available" chip. |
| ![Joanne Glow Studio, 10Web](./screenshots/anti-vibe/17-10w-joanne.jpg) **17 Joanne Glow Studio (10Web).** "UNVEILING YOUR RADIANCE", bracketed mono "EST. 2020" label, floating services card. | ![Vow Venue, 10Web](./screenshots/anti-vibe/18-10w-vowvenue.jpg) **18 Vow Venue (10Web).** "Where Forever Begins", centred Cormorant, white wash over the photo. |
| ![Harvest Table Events, 10Web](./screenshots/anti-vibe/19-10w-harvest.jpg) **19 Harvest Table Events (10Web).** "The Art of the Gathering", centred on a darkened photo, two CTAs. | ![Prolific Pours, Durable](./screenshots/anti-vibe/20-dur-pours.jpg) **20 Prolific Pours (Durable).** Real business: Playfair on green, gold circular logo, "Your Guests Deserve a Bar Worth Talking About". |

---

<!-- copylint-on -->

## 10. Machine-checkable lint rules

Proposed checks for `theme.json`, `style.css`, `styles/*.json`, `patterns/*.php`, `parts/*.html` and `templates/*.html`. Each rule cites the measurement that motivates it. Severity: **block** fails CI, **warn** needs a written exception in the theme README.

<!-- copylint-off -->
### 10.1 Stack and markup

| ID | Check | Severity | Evidence |
|---|---|---|---|
| FS-01 | No Tailwind-shaped class names in pattern markup: regex `\b(?:[a-z]+:)*(?:p[xytrbl]?|m[xytrbl]?|gap|text|bg|rounded|shadow|tracking|leading|max-w)-(?:\d|\[|xs|sm|md|lg|xl|2xl|full|none|tight|wide)` | block | 61 of 65 AI, 0 of 12 control |
| FS-02 | No shadcn token names anywhere: `--radius`, `--primary-foreground`, `--muted-foreground`, `--card-foreground`, `text-muted-foreground`, `bg-background` | block | 55 of 65 AI, 1 of 12 control |
| FS-03 | No Lucide SVGs: `class="lucide`, or an inline `<svg viewBox="0 0 24 24" ... stroke-width="2" stroke-linecap="round" stroke-linejoin="round">` in patterns | block | 45 of 65 AI, 0 control |
| FS-04 | No empty toast or notification regions (`aria-live` containers with no content, `data-sonner-toaster`, `max-width:420px` fixed bottom-right lists) | block | 11 of 18 Lovable |
| FS-05 | No `calc(infinity * 1px)` radius | warn | Tailwind v4 fingerprint, 9 pages |

### 10.2 Typography (theme.json `typography`, `styles.elements`, block styles)

| ID | Check | Severity | Evidence |
|---|---|---|---|
| FS-10 | `fontFamilies` must not include Inter, Inter Tight or Geist as any slug; must not include Fraunces, Playfair Display, Cormorant Garamond, Instrument Serif or DM Serif Display as the heading face | block / warn | Inter 33 of 65 AI, 0 control; those five serifs are 20 of 22 AI serif H1s |
| FS-11 | No monospace face in a theme whose declared trade is not technical (Space Mono, JetBrains Mono, Geist Mono, IBM Plex Mono, `ui-monospace`) | warn | 18 of 65 AI, 0 control |
| FS-12 | Heading `letterSpacing` must not be negative below -0.01em; `-0.025em` exactly is blocked | block | 40 of 65 AI negative, 18 at -0.025em; 0 control |
| FS-13 | Any style with `textTransform: uppercase` and `fontSize` 12px or less must not have `letterSpacing` of 0.15em or more; at most 1 such style per theme | block | 39 of 65 AI, 5 of 12 control (computed) |
| FS-14 | No font-size preset below 12px; no `fontSize` using `vw` units above 10vw | block | text-[9..11px] on 26 of 65; `text-[13vw]` on 7 |
| FS-15 | Heading `lineHeight` must be 0.95 or more | warn | `leading-[0.85]` on 6 and `leading-[0.9]` on 5 of 46 Tailwind-class pages |
| FS-16 | An `h1` in any pattern must not contain `<em>`, `<i>`, `<span style` or `has-*-color` inner markup | block | 26 of 65 AI, 2 of 12 control |

### 10.3 Colour (theme.json `color.palette`, `color.gradients`, CSS)

| ID | Check | Severity | Evidence |
|---|---|---|---|
| FS-20 | No palette colour within dE2000 10 of #6366F1, #4F46E5, #8B5CF6, #7C3AED or #A855F7 | block | ANTI-VIBE C1; 8 of 65 AI pages still hit it |
| FS-21 | No 3 or more palette colours within dE2000 2.5 of one Tailwind v3 ramp (slate, gray, zinc, stone), and no exact `#111827`, `#4B5563`, `#737373`, `#FBFAF9`, `#F8FAFC` | block | repeated exact values in 5.2 |
| FS-22 | Warm off-white base (hue 20 to 60 deg, saturation 0.12 or more, lightness 0.88 or more) together with a gold accent (hue 25 to 50 deg, saturation 0.25 to 0.75, lightness 0.35 to 0.75) | warn, requires a material reason | 22 of 65 cream, 7 of 65 gold |
| FS-23 | `color.gradients` may not contain `radial-gradient`; no gradient on text (`background-clip: text`) | block | radial 17 of 65; gradient text 6 |
| FS-24 | No two themes in the library may share the (base, accent, heading face) triple | block | ANTI-VIBE X2, extended |

### 10.4 Shape, depth and motion (CSS and theme.json `custom`)

| ID | Check | Severity | Evidence |
|---|---|---|---|
| FS-30 | The same `border-radius` value may be used on at most 2 of: button, card or group, input, badge, image | block | ANTI-VIBE K1; pill buttons 17 of 65 |
| FS-31 | No box-shadow whose geometry equals a Tailwind stock shadow: `0 1px 2px 0`, `0 1px 3px 0 ... 0 1px 2px -1px`, `0 4px 6px -1px ... 0 2px 4px -2px`, `0 10px 15px -3px ... 0 4px 6px -4px`, `0 20px 25px -5px ... 0 8px 10px -6px`, `0 25px 50px -12px` | block | 39 of 65 AI, 1 control |
| FS-32 | No `transition: all` or `transition-property: all` | block | 51 of 65 AI, 6 of 12 control |
| FS-33 | No `backdrop-filter` outside a sticky header template part; no `filter: blur()` of 3px or more | block | 36 and 20 of 65 AI, 0 control |
| FS-34 | No CSS that sets `opacity: 0` on content blocks as an initial state; no `@keyframes` named or containing marquee, ticker, scroll-x | block | scroll-reveal 40 of 65, marquee 14 |
| FS-35 | No `transform` on `:hover` for images or for icons inside links (`translateX` nudge, `scale`) | warn | arrow nudge 19, image zoom 22 |
| FS-36 | Transition durations of 300ms or more on hover | warn | `duration-300/500/700` on 30, 21, 11 pages |

### 10.5 Pattern structure (parse block markup)

| ID | Check | Severity | Evidence |
|---|---|---|---|
| FS-40 | No `core/columns` or grid with 3 or more children that each contain (icon or image under 72px) + heading + paragraph | block | card grids 42 of 65; with icon tiles 9 |
| FS-41 | A front-page template must not end with a full-width group whose heading matches `/^(ready to|let'?s|start|book your|join)\b/i` directly after a quote or testimonial pattern | block | 20 of 47 multi-section AI pages |
| FS-42 | No pattern with 3 or more sibling blocks each holding a large number (`/\d[\d,.]*\s?(\+|%|x|k)/`) plus a short label | block | stats in hero or section on Optimus, COMPUTE, Nestora, Meridian, Harvest Guide |
| FS-43 | No decorative 1px separators before labels (`core/separator` under 64px wide next to a paragraph under 30 characters) | warn | hairline rules 25 of 65 |
| FS-44 | No text block rotated 90 degrees (`writing-mode: vertical-*`, `rotate(90deg)` / `rotate(-90deg)`) used as a side label | warn | Lumiere, Timbercraft, Kern, 10Web templates |

### 10.6 Pattern copy (plain text extracted from patterns, run through copylint plus these)

| ID | Check | Severity | Evidence |
|---|---|---|---|
| FS-50 | Zero em dashes (U+2014) in pattern and template text, including labels | block | 33 of 60 AI pages, 0 of 12 control |
| FS-51 | Banned words: `elevate|unlock|seamless(ly)?|curated|bespoke|tailored|journey|precision|transform(ative)?|vibrant|meticulous(ly)?|empower(s)?|unparalleled|effortless(ly)?|showcase|interplay|unveil(ing)?` | block | 5.9 |
| FS-52 | Banned phrases: `attention to detail`, `designed (for|to)`, `we believe`, `your vision`, `begins with`, `for every`, `where .{1,25} meets`, `^the art of`, `^ready to .*\?$`, `look no further`, `in the heart of` | block | 5.9 |
| FS-53 | Fragment triplets: `^([A-Z][a-z]+\.\s?){3}$` in any heading | block | 6 of 65 |
| FS-54 | Placeholder data: `\bNew York\b` (unless the persona is in New York), `555[-. ]\d`, `123 Main`, `\(111\)`, `example\.com`, `\bSarah\b` in testimonials, `Lorem` | block | 9, 11 and 12 of 65 |
| FS-55 | Fake metadata: `\b(Est\.?|Established|Since)\s+(19|20)\d\d\b`, `№`, `\[\s?\d\d\s?/+\s?\d\d\s?\]`, `\b0[1-9]\s?[/.:]`, `[A-Z]{2,}_[A-Z]{2,}`, standalone `Scroll` | warn (block for snake_case) | 12, 18, 3 and 7 of 65 |
| FS-56 | Visible scaffolding words: `Social Proof`, `Bento`, `Landing Page`, `Template`, `Hero`, `CTA` in rendered text | block | 5 of 65 |
<!-- copylint-on -->

Suggested implementation: one Node script beside `copylint.mjs` that (a) parses `theme.json` and computes dE2000 on palette entries, (b) regex-scans CSS and block markup for FS-01 to FS-05 and FS-30 to FS-36, (c) walks the block tree of each pattern with `@wordpress/block-serialization-default-parser` for FS-40 to FS-44, and (d) strips markup and runs FS-50 to FS-56 on the text. `analyze.mjs` can be reused unchanged on a local WordPress install to check the rendered front end against the same thresholds.

---

## 11. Limits

- **n is modest and uneven by tool** (Durable 7, v0 14). Per-tool counts are descriptive, not statistically compared.
- **Galleries are curated.** They show polished AI output, not typical first drafts. Durable sites may have been hand-edited after generation.
- **Heuristic detectors.** Card grids, icon tiles, eyebrows and section kinds are detected by rules in `analyze.mjs`; section order was then corrected by hand from headings, and the correction is in `order-manual.json`. Numbers for those traits are approximate to within a page or two.
- **Control pages are sometimes inner pages** and several predate modern CSS, so traits like shadows or tracking may be absent for reasons of age as much as of taste.
- **Five tools are missing** (Framer AI, Relume, Wix ADI, ZipWP, WordPress.com AI, Elementor AI); see 2.1.

Files: `research/tools/antivibe/` holds `sites.json`, `control.json`, `analyze.mjs`, `aggregate.py`, `freqtable.py`, `names.json`, `order-manual.json`, `shoot20.mjs` and the gallery crawlers `links.mjs`, `frames.mjs` and `html.mjs`.
