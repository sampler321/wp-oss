# Build workflow (one theme)

Read first: `THEME-CONTRACT.md` (the rules), `BUILD-STATUS.md` (your theme's row: idea number and **the owner's brief**, which overrides the research), and `research/THEME-IDEAS.md` (search for `#### NNN ` to find the entry). Read `research/ANTI-VIBE.md` §3 (sniff test) and `research/ANTI-AI-WRITING.md` §2–5 (em dashes, tells, voice briefs, demo-content rules).

The reference theme is **`ink`**. Build script: `build/ink.py`, theme: `themes/ink/`, demo: `demos/ink/content.json`. Copy its structure, not its look.

All commands run from the repo root `/Users/borys/Desktop/wp-oss`.

## 1. Understand the brief (15 min)
- Read the research entry: For, Templates, Patterns, Signature, Nice-to-haves, Real-world basis, Style.
- If the owner's brief names inspiration (a site, festival, band, brand, aesthetic), study it: `node tools/peek.mjs <url> <name>`, then look at `.cache/peek/<name>-*.jpg` with the Read tool. Also peek at 1–2 of the entry's Real-world basis sites. Web search is not available, so use WebFetch or peek on URLs you know or find in the research.
- Write a 5-line design note at the top of `build/<slug>.py` (as a comment): the direction, why, fonts, palette, and the one layout idea that makes it distinctive. The theme must look clearly different from `ink` and from the other themes in your batch.

## 2. Fonts
- Use the display face from `research/FONT-REGISTRY.md` for your idea unless the owner's brief changes the direction. If it does, pick an unused free family (Google Fonts or Fontshare). Check `grep -i "<family>" research/FONT-REGISTRY.md` returns nothing, and record the choice in `demos/<slug>/fonts-claim.txt` (one line: `display: Family Name`). Don't edit the registry yourself.
- `node tools/fetch-fonts.mjs <slug> "display=<Google family spec>" "body=<spec>" "mono=<spec>"`. Fontshare: `"display=fontshare:<slug>@400,700"`. It writes `themes/<slug>/.fonts.json`, which you load in the build script (see `build/ink.py` pattern in `theme.json` generation). Avoid banned faces (Inter, Geist, Space Grotesk, Instrument Serif, Poppins, Montserrat, Fraunces, Playfair Display, Cormorant) and **all monospace fonts**. Two families maximum (display + body).

## 3. Images
- `node tools/fetch-images.mjs <slug> "hero=<query>|orient=landscape" "name=<query>|pick=2" ...` fetches CC0/public-domain images from Wikimedia Commons. Aim for 8–14 images that fit the trade. Use specific queries ("espresso machine cafe", "welding workshop", "vinyl records shop crates").
- `python3 tools/contact-sheet.py <slug>`, then **look at the sheet** with the Read tool. Replace anything off-brief, ugly, or clearly the wrong trade with `pick=N` or a different query. No AI-generated images, no watermarked images.
- Public-domain art and archive photos are fine when they suit the brief (they carry a footer note, like `ink`).

## 4. Build script `build/<slug>.py`
- `import sys; sys.path.insert(0, 'tools/lib'); from blocks import *; set_theme('<slug>')`
- Generate: `theme.json` (all tokens, see contract §2), `style.css` header, `parts/header.html`, `parts/footer.html` (+ variants), all templates, **25+ patterns** (the research Patterns list, the Signature, and at least 3 Nice-to-haves as patterns), `styles/*.json` (3 variations), `styles/sections/*.json` (section styles you use via `className: is-style-<slug>`).
- Only core blocks. No hex colours, custom font sizes or raw spacing in markup: use presets (`textColor`, `backgroundColor`, `fontSize`, `var:preset|spacing|NN`). Put borders, radii, shadows and special CSS in `theme.json` or section styles.
- Content model: use **posts in categories** for the repeating things (works, projects, episodes, releases, shows, menu items stay in patterns). Query Loop can't filter by a category slug at build time, so give each theme one main post type of content and use category archives (`category-<slug>.html`) for the rest.
- WooCommerce: only if the idea sells products. Add `products` to the demo; don't write Woo block templates unless you need them (the Woo defaults inherit your theme.json).
- Copy: in the owner's voice, following `research/ANTI-AI-WRITING.md`: real-feeling names, places, prices, hours, one opinion, one limit. Zero em dashes. No middle dot `·` separators. No zero-padded `01`/`02` labels. Sentence case. No "Welcome to", no "elevate", no emphasis by negation.
- Run it: `python3 build/<slug>.py`

## 5. Demo content `demos/<slug>/content.json`
Same shape as `demos/ink/content.json`: site title and tagline, categories, `front_page` + `posts_page`, pages built from your page-layout patterns, 6–10 posts with featured images, `nav`, and `products` for shops. Only use images that exist in `assets/images/`.

## 6. Normalise, readme, test, look, repeat
```
node tools/make-readme.mjs <slug>
node tools/normalize-blocks.mjs <slug>
node tools/test-theme.mjs <slug>
```
- Fix every FAIL and re-run until `PASSED all`. If `normalize-blocks` reports `unknown`/`stray-html`, fix the markup in the build script, then re-run the build, readme and normaliser. The normaliser rewrites files in `themes/<slug>/`, so re-running the build script overwrites them; always normalise after building.
- **Look at the screenshots** in `demos/<slug>/screens/` (home, every nav page, desktop and mobile) with the Read tool. Judge them against the brief and the sniff test. If a page looks generic, cramped, broken on mobile, or not like the brief, change the design and repeat. Passing the tests is necessary but not enough.
- `node tools/make-blueprint.mjs <slug>`

## 7. Done
- `demos/<slug>/test-report.json` shows `"passed": true`.
- Write `demos/<slug>/NOTES.md`: 5–10 lines on the design direction, fonts, palette, what's signature, and anything you couldn't do with core blocks.
- Do **not** edit `BUILD-STATUS.md`, `research/FONT-REGISTRY.md`, `tools/`, other themes, or git. Don't export or deploy; the orchestrator does that. If a shared tool has a bug, describe it in your final message rather than editing it.
