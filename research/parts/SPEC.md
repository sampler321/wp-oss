# Spec for writer agents

Project: a large library of open-source **native WordPress block themes** (FSE: theme.json, templates/*.html, parts/*.html, patterns/*.php, styles/*.json). The style is modelled on Automattic's own block themes. NO classic editor, NO page builders (Elementor/Divi etc.), NO shortcode-heavy plugins.
Audience: small, independent people and organisations, not enterprise.
Aesthetic: art-school / cutting-edge brutalist, applied to *ordinary* businesses too (e.g. a plumber in a Swiss grid, a food bank with protest-poster type).

Read these first for context and exact format:
- /Users/borys/Desktop/wp-oss/research/parts/01-foundations.md (core capabilities + the approved plugin toolkit)
- /Users/borys/Desktop/wp-oss/research/parts/04-ideas-51-84.md (format examples)

## Entry format (copy exactly)

```
#### NNN, Name (`slug`)
**For:** who exactly uses it (one line, specific).
**Templates:** front-page, archive-x, single-x, page-y, ... (list 5–10; include Woo templates if commerce)
**Patterns (~NN):** 6–12 concrete pattern names, comma-separated
**Content model:** CPTs/taxonomies/meta (from the `wp-oss-companion` plugin, shown via Block Bindings), or "posts + pages only"
**Plugins:** only what's essential. Prefer the Part 2 toolkit. Write "none" if core is enough
**Signature:** ONE concrete killer feature, implementable with core/Interactivity API/listed plugins
**Flare:** the brutalist/art-school twist, specific and visual
**Style variations:** three names
**Refs:**
- [Site name](https://url): one line on what it does well that this theme should learn from
- [Site name](https://url): …
```

## UPDATE (applies to everything; supersedes anything above)

1. **Replace the `**Flare:**` line with a full `**Style:**` block**, deliberate and explicit, for EVERY idea:
```
**Style: <Named direction>** (e.g. "Swiss neo-grotesk index", "Soft neo-brutalism (hard shadows, pastel fills)", "Editorial serif revival", "Warm Scandi minimal", "Kinetic variable-type maximalism", "Dither / 1-bit bitmap", "Grainy-gradient organic", "Web 1.0 revival", "Tactile skeuo 2.0", "Bento-grid product", "Riso zine", "Y2K chrome", "Quiet luxury mono", "Utility/industrial signage")
- Type: exact FREE/OFL fonts (Google Fonts / Fontshare / Velvetyne / Collletttivo), e.g. "Headings: Bricolage Grotesque 800, tight -0.04em; body: Inter 400/16px; labels: JetBrains Mono 500 uppercase"
- Palette: 4–6 hex values with roles (bg / text / accent / surface / line)
- Layout: grid, density, borders/radius, nav pattern, how the home page is composed
- Imagery: photo/illustration treatment (duotone, grain, cut-outs, crops, aspect ratios)
- Motion: specific interactions (View Transitions, scroll-driven animation, hover states); always respect prefers-reduced-motion
- Why it fits now: one line on why this is CURRENT (2025–26) for this audience, with a live example URL of the style (godly.website, siteinspire.com, fontsinuse.com, a real studio site, etc.)
```
   The style does NOT have to be brutalist. Pick whatever is most current and right for the audience; a dentist should not look like a riso zine. The whole library still needs a recognisable edge: confident type, strong grids, no generic stock template look. Vary styles across your batch and don't repeat the same direction twice in a row. The `**Style variations:**` line stays: three variations, each described in about five words (e.g. "Signal: #F2F2EE bg, #1F3BFF ink-blue links, #111 type").

2. **Refs must be SPECIFIC DEEP LINKS**: the exact page showing the feature (e.g. the actual /work/project-x case study page, the /menu page, the /timetable), not just the homepage. Format:
   `- [Site name: page](https://exact/url): what to learn (layout/feature/style)`
   Give 2–3 per idea. Verify each with WebFetch (a 200 response with relevant content). Do NOT take screenshots; the orchestrator will batch-capture every URL you list.

3. **FORBIDDEN: anything that looks vibe-coded or AI-generated.** This is a hard rule. Full catalogue: `/Users/borys/Desktop/wp-oss/research/ANTI-VIBE.md` (COMPLETE: read it and run its sniff test on every Style you write). Baseline bans:
   - Purple/indigo→blue/pink gradients, gradient text in headlines, glowing orbs/blobs/aurora backgrounds, glassmorphism blur cards, gradient borders, neon glow on dark
   - Default shadcn/Tailwind look: `rounded-2xl` cards + soft grey shadow + 1px slate border, everything the same radius, zinc/slate greys, `max-w-7xl mx-auto` centered-everything
   - Hero formula: pill badge ("✨ New") → big centered headline → grey subline → two buttons (solid + outline) → screenshot in a browser frame
   - 3-column feature cards with an icon in a tinted circle/square (Lucide/Heroicons), emoji as icons, sparkle icons
   - Generic "Trusted by" grey logo row, 5-star testimonial cards with circle avatars, fake metric strips ("10k+ users"), 3-tier pricing with a highlighted "Most popular" middle column, stock FAQ-accordion → gradient CTA band → 4-column footer formula
   - Inter/Geist-only typography with no typographic idea, uniform section padding, fade-up-on-scroll on every section, bento grids as the default layout
   - Copy: "Elevate", "Unlock", "Seamless", "Supercharge", "Effortless", "Built for X, by X", "Your all-in-one…"; em-dash-heavy marketing voice; placeholder names like "Sarah Johnson"
   - Instead: real typographic hierarchy (use at least one distinctive typeface), asymmetric/editorial grids, a considered and limited palette, real content structures from the domain (menus, fixtures, catalogue numbers, timetables), specific photography direction, deliberate interaction ideas, and honest copy in the voice of the business.
   Every idea's Style must be checked against this list. Don't use the banned names in your examples (the "Bento-grid product" example above is withdrawn, and Inter is only allowed as a secondary UI font next to a distinctive primary).

4. **GROUNDED IN REALITY: this is the most important rule.** Start from real sites and don't imagine features. Workflow per idea: first find 3–5 real, live, well-made sites of that exact type (small/independent), study what they actually have, then write the entry from what you observed.
   - Every item in **Patterns** must be something that real sites of this type actually have. Use the real vocabulary they use (e.g. a real restaurant has "Lunch / Dinner / Wine" menus with a "Last updated" date, not an invented "flavour explorer").
   - **Signature** must name a feature that EXISTS on a real site. Add `(seen on: [Site](deep-url))`. If you can't find it in the wild, don't propose it; pick a proven feature instead.
   - **Templates** should mirror the real site maps of the reference sites (the pages they actually have).
   - The Style's "Why it fits now" example must be a real site in that style.
   - No speculative gimmicks, no "AI-powered" anything, and no features that need custom backend engineering beyond the companion plugin plus listed plugins.
   - Add one line `**Real-world basis:**` listing the 3–5 sites (deep links) you studied, separate from the 2–3 best Refs.

5. **Nice-to-haves: every idea needs this line.** After Signature, add:
```
**Nice-to-haves:**
- <small, practical, operational value-add> (seen on: [Site](url) if found)
- … (3–5 items)
```
   These are the small touches that make a theme feel made by someone who knows the business: things the owner would otherwise hack together or pay for. They must be real-world and ideally observed on a real site. Examples of the right kind:
   - Illustrator shop: "Order by 15 Dec for Christmas delivery" banner with per-region cut-off dates that switches itself off after the date; shipping-times-by-country table; "gift note" option; "print ships rolled in a tube" packaging note.
   - Restaurant: "Closed for summer holidays 4–18 Aug" notice bar with start/end dates; allergen PDF; "last updated" date on the menu; printable A4 menu.
   - Plumber: "Currently booking 3 days ahead" lead-time indicator; bank-holiday emergency rates notice; "What to do while you wait" (stopcock) guide.
   - Band: "Low tickets" / "Sold out" flags on tour dates; timezone-aware livestream times; merch "ships after tour" note.
   - Therapist: "Currently accepting new clients: yes/no" toggle; sliding-scale fees note; out-of-hours crisis numbers in the footer.
   **Nice-to-haves are NOT just dates/notices.** Cover a MIX across these categories (at least 3 different categories per idea):
   - **Buying confidence:** print-size comparison against an A4 sheet/hand/sofa; "what's in the box" and packaging photos; paper/fabric sample packs; a frame guide; ring-size printable; "how it's made" process strip; material and care cards.
   - **Trust & proof:** real customer photos; press kit/press quotes download; accreditation/insurance badges with numbers; "meet who'll be in your home" staff cards; transparent price lists; guarantees and repair promises.
   - **Conversion helpers:** gift cards; "notify me when back in stock"; wishlists; "commissions open/closed" states; waitlists; "book a free 15-min call"; bundles; "complete the set".
   - **Content & tools the owner gets for free:** printable price list/menu/rate card; one-click press kit/EPK page; downloadable CV PDF; care-guide PDFs; embeddable "as seen at" widgets; a newsletter archive page.
   - **Local & practical:** open-now and hours; parking/access/step-free info; "how to find us" photo directions; cm/in units toggle; multi-currency note; shipping-times-by-country table; returns explained in one paragraph.
   - **Operational/seasonal:** Christmas cut-offs, holiday closures, lead times, capacity states, sold-out flags, scheduled announcement bars.
   - **Care & aftercare:** aftercare guides (tattoo, plants, ceramics); "what to expect at your first visit"; preparation checklists; FAQs per product or service.
   - **Community & loyalty:** customer gallery; "studio diary" or behind-the-scenes; referral note; local stockists; events and meetups.
   - **Accessibility & inclusion:** plain-language versions; BSL/captioned info; sensory-friendly hours; image descriptions on artworks; pronouns on staff cards.
   - **Owner-side quality of life:** realistic demo content for the trade; ready-made legal pages (T&Cs for commissions, returns, privacy); social share image (OG) patterns; schema.org markup (LocalBusiness, Product, Event, Recipe).
   Implement with core blocks, block bindings, and small shared companion blocks (not heavy plugins).

6. **NO EM DASHES. Zero, anywhere.** Not in your entries, not in example copy, not in pattern names, not in refs. The em dash (U+2014) is the most recognised AI-writing tell. Use a colon, a full stop, a comma, brackets, or rewrite the sentence. En dashes (–) are allowed only for number ranges (3–5, 2025–26). Also avoid the other AI-writing tells: "not just X, it's Y", reflexive lists of three, "whether you're…", "elevate / seamless / curated / vibrant / nestled / delve", and bolded lead-ins on every bullet. Also no **emphasis by negation** (denying something nobody said so the positive sounds bigger: "Not a template. A system.", "We're not your average plumber", "No fluff, no filler"). Real limits that inform the reader ("We don't do gluten-free") are fine and encouraged. Full guide: /Users/borys/Desktop/wp-oss/research/ANTI-AI-WRITING.md, section 3.2b. Before finishing, run `grep -c "U+2014" <yourfile>` and make sure it returns 0.

## Rules
- Be SPECIFIC. No generic "hero, about, contact" lists without domain detail. Every pattern list must include domain-specific patterns (e.g. plumber: "emergency call-out bar", "Gas Safe badge row", "boiler service price table").
- Plugins: free/OSS and block-compatible only. If you name a plugin that is not in the toolkit, verify it exists on wordpress.org (WebSearch/WebFetch) and that it is active in 2025/2026. Paid-only plugins are not allowed. External embeds (Cal.com, Bandcamp, Strava, etc.) are fine.
- Refs: 2 per idea, REAL live sites found with WebSearch and checked with WebFetch where possible. Prefer small independent sites, and prefer sites built on WordPress where possible (don't force it). NEVER invent a URL. If you truly cannot verify one, write `(unverified)` after it. Automattic/wordpress.org theme pages are OK as a secondary ref.
- Use exactly the numbers, names, slugs and section headers given in your assignment. Write in plain English (British/US mix is fine). No emoji.
- Write your output file with the Write tool (overwrite if exists). Only write your assigned file.
- When done, reply with a 3-line summary: file path, count of entries, count of refs marked unverified.
