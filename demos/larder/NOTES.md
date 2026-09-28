# Larder (Spiżarnia)

- Direction: the owner asked for "an independent one too, like jadlonomia.com". It's one person's plant-based blog from Łódź, written in the first person: a "Tastes best right now" produce strip under the header (Jadłonomia's "Teraz najlepiej smakują"), a dense photo mosaic with titles on pale bands, and recipes told as a short story, then a "What you need" box, then "How I do it" in paragraphs. It's deliberately unlike pantry: no recipe card, no pills, serif type, cool grey paper.
- Fonts: Vollkorn (display, claimed in demos/larder/fonts-claim.txt) and Work Sans (body), plus Caveat as the optional accent face, used only for short handwritten asides (is-style-note). Captions and the tagline use Vollkorn italic. The fetched Caveat subset is Latin only, so asides avoid Polish letters such as ł and ę.
- Palette: paper grey #F3F4F1, forest #143A22, beet #9C1848, dill #2F6B3A, sky #E3ECF7 for the strip and the letter panel, mustard #E0A526. Variations: Beetroot, Dill, Winter jar (dark).
- Signature: the seasonal calendar (months by produce table with dots) on the front page and the Seasons page, and the produce strip, which is a template part so it can be swapped each month.
- Mosaic: a Query Loop with Cover blocks using the featured image. Every sixth tile spans two columns and two rows on desktop. The span rules sit in theme.json global CSS, because @media inside a section style's css gets flattened by WordPress (the rule lost its media query and applied everywhere).
- Core-block limits: no ingredient scaling or print view; this is a blog, and the "What you need" box is a styled group.

## Round 2

- "Needs a recipe page with all the blocks": a new Recipe (full) template (single-recipe) with the category, title and byline, a wide key photo, the recipe body, tags, "More from the same shelf" and a comments section ("Did you cook it? Tell me how it went").
- The recipe kit, each block also a pattern: intro story, servings and times line, ingredients in named groups, method with numbered steps and step photos beside them, a handwritten aside, notes from my kitchen, swaps that work, keeping it (storage), jump link and a "Recipe: the whole recipe" page-layout pattern that stacks them all.
- All 8 recipes were rewritten to use the full template, plus a kitchen-diary post on the plain single template. A "How a recipe page works" page shows the kit with placeholder copy.
- Home page: the seasonal calendar table moved to the Seasons page; the home now has "Good at the market this month" produce cards and a kitchen diary. No table on the home page. Nav trimmed to one line, contact moved to the footer.
- Image lightbox on globally. 46 patterns, adding a kitchen photo gallery, Polish kitchen words, workshop card, short about, recipes by vegetable, printing note and a contact block.
- Step photos in post content point at /wp-content/themes/larder/assets/images/ because theme PHP doesn't run in saved post content.
