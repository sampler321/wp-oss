# Revision brief (round 2, from the owner's review)

The owner reviewed the first live demos. Everything below applies to **every** theme, on top of `THEME-CONTRACT.md` and `BUILD-WORKFLOW.md`. The test harness enforces the parts marked (tested).

## General rules

1. **Far fewer tables.** Tables are for real tabular data only: a price list on a price-list page, a timetable, a spec sheet on a product page. They are not a layout tool. Replace table-heavy patterns with designed layouts: lists with rules, cards, media and text, columns, definition-style rows made from groups. (tested: the home page renders no `<table>`, and at most 20% of patterns contain a table.)

2. **Lightboxes everywhere images are shown as work.** Enable the core image lightbox globally in `theme.json` (`settings.blocks["core/image"].lightbox = { "enabled": true, "allowEditing": true }`), and use it on portfolio images, galleries and product shots. Reference: zosiapaszkiet.com, where clicking any work opens it large. (tested)

3. **A large, usable block library.** Each theme is a kit, not a landing page plus a few side pages. **At least 40 patterns** (tested), studied from real sites of that type: open 3–5 real sites (research entry's Real-world basis, `node tools/peek.mjs <url>`), list every distinct section they use, and build the ones that make sense. Group patterns in the inserter with clear names and categories. Include page-layout patterns for every page type the business needs.

4. **No dead promises.** Every section, menu item, link and call to action must lead to real demo content (tested: no internal link on the demo site returns 404):
   - A journal or blog has **at least 6 real posts** with featured images and proper body content.
   - "Case studies", "projects", "episodes", "recipes" and similar each have **at least 4 full examples**, built from the theme's own patterns so the demo shows off the kit.
   - No link to a page that doesn't exist.

5. **Heroes are not mottos.** Don't default to one big sentence ending in a full stop. Real sites open with the work itself, a current thing (this week's menu, the next show, the new release), a name and a single fact, a big image with a caption, or a list. Each theme picks the opening that suits its trade. (tested: the home page's first h1 doesn't end in a full stop)

6. **Home page composition.** Never open with a huge single image followed by a price table. The first screen should show what the business is and make the owner's main thing easy to reach (work, shop, booking, the next event).

7. **Proportion and scale.** Check type sizes against real sites in the trade. Body text 17–19px, not larger. Display sizes should suit the content: huge type for a skate shop, not for a recipe index. Check every page at 390px and 1440px.

8. **Layout details.** No awkwardly centred blocks in otherwise left-aligned pages (contact and visit sections especially). Align to the theme's grid.

9. Keep everything that already works: tokens in theme.json, core blocks only, owner's voice, no em dashes, no monospace, no middle dots, no zero-padded labels.

10. **The demo shows the whole kit.** The owner: "the demo has to show all of the patterns and functionalities, not be very limited." Two parts:
    - Automatic: the demo builder now generates a **Pattern library** (an index page, one page per pattern category, and every pattern rendered with its name) and adds "Patterns" to the menu. Give patterns sensible `Categories:` so the library pages group well (e.g. `hero`, `portfolio`, `case-study`, `shop`, `events`, `about`, `contact`, `footer`). (tested: every pattern appears in the demo)
    - By hand: the demo's real pages and posts must *use* the patterns too, so a visitor sees them in context: case studies built from case-study patterns, recipes built from recipe patterns, and so on. Every template the theme ships (single, archive, category, page variants, 404, search, shop templates) should be reachable from the demo.

## Per-theme notes from the owner

- **ink (001 illustrator)**: "why does it have such a giant image on page 1 and start with a pricing table". Redesign the home page around the work: a lightboxed portfolio grid and recent pieces, with shop and commission entry points. Move prices off the home page.
- **case (022 UX designer)**: "zero case studies. The core idea is not to make a landing and a few side pages but actually all blocks for case studies." Build a full case-study block kit (at least 20 case-study patterns: overview and role, problem, constraints, research and insights, personas, journey map, flows, wireframes, before and after, design system, prototype embed, testing results, metrics, quotes, learnings, next project) and **at least 4 complete case studies** as posts using them. Reference: kapicadesign.com (study its case-study pages).
- **oil (002 painter)**: the journal has no posts, so write 6+. The "Visit the studio" contact section is awkwardly centred; align it to the grid.
- **joint (021 furniture designer)**: "image first and then table, think outside the box more." Rework object pages and the home page. Show pieces in use, details, materials and making, with specs designed as part of the layout rather than a table.
- **confidante (047 women's podcast)**: "too huge quote, no image". Scale the pull quote down; add host photos, episode artwork and guest images.
- **patchnotes (047 tech podcast)**: "should be hacker themed, looks pretty bad". Rebuild the direction: terminal and demoscene culture, BBS/ANSI art, phosphor colours, scanlines. Use a pixel or bitmap *proportional* display face (monospace is still banned). Design episodes like changelogs or commit logs.
- **spine (051 Penguin)**: "too dull, could be more playful. Penguin does a lot of patchwork-ish illustrations, study their covers more, not just the classic ones." Look at Penguin Modern Classics, the Penguin Great Ideas series, the Penguin clothbound classics (Coralie Bickford-Smith's repeating patterns) and Penguin's collage and illustrated covers. Add patterned, collage-like cover treatments using CSS and SVG patterns in section styles, colour-coded series, and more play.
- **pantry (058 recipes, Ottolenghi/Mob)**: "too big text". Bring body and heading sizes down to match mob.co.uk and ottolenghi.co.uk.
- **larder (058b, Jadłonomia-style)**: "needs a recipe page with all the blocks": a full recipe template (intro story, key photo, servings and times, ingredients with groups, method steps with photos, notes, substitutions, storage, related recipes, comments), and 6+ recipes using it.
- **bind (262 bookbinder)**: "advertises case studies that are non-existent". Write 4+ restoration case studies as posts, or remove every mention.
- **deck (076 skate) and drop (082 grunge merch)**: "AMAZING design". Keep the look; add many more blocks and usage areas (team pages, video parts, lookbooks, drops, events, stockists, zine pages, tour dates).
- **patchbay (264 DIY pedals)**: "great design". Keep it; the general rules apply.

## Done means
`node tools/test-theme.mjs <slug>` passes (including the new round-2 checks), the screenshots were reviewed against this brief, and `demos/<slug>/NOTES.md` has a "Round 2" section listing what changed.
