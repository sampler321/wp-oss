# paper: notes

- Direction: a Tokyo stationery-shop catalogue for a small Edinburgh shop. White pages ruled with a 5mm cyan graph grid (drawn in CSS), objects photographed small in the middle of large pale squares, Mincho product names, hairline spec tables with sizes in millimetres and paper weight in gsm.
- Signature: the ruling selector. Links for dot grid 5mm, ruled 7mm, squared 5mm and blank swap the photo of the page using anchors and the CSS `:target` selector, so it works with core blocks and no script. Spacing, gsm, pages and "fountain pen friendly" sit beside it, with the handmade-variation note.
- The spacing scale is in millimetres (1.25mm to 40mm), so the page layout matches the paper it sells.
- Fonts: Zen Old Mincho 500/700/900 (display, from the registry) and Zen Kaku Gothic New 400/500/700 (body). No mono; tabular figures in specs.
- Palette: white #FFFFFF, graphite #222222, graph cyan #1A7A98, pale field #F4F7F8, cyan hairline #BFD3DA, correction red #C0392B for the notebook margin rule. Variations: Kraft, Letterpress, Dot grid.
- Nice-to-haves built: fountain-pen-friendly yes/no table, handmade note, printable ruling samples, next year's diaries bar (September to February), wholesale price list, perpetual calendar, gift wrap.
- Tool issue: `tools/fetch-fonts.mjs` keeps a random CJK subset (about 1KB) for Japanese families because Google labels those subsets with numbers, not "latin". The Latin faces were fetched by hand into the same file names; re-running fetch-fonts for this theme would break the type again.
- Ruling variants are separate simple products because the demo builder makes simple products only.

## Round 2

- The home h1 was a sentence ending in a full stop; it now opens on the current thing: "New in: the A5 notebook, sewn in Leith, in four rulings".
- Kit grew from 26 to 44 patterns, from sections on Present & Correct and Choosing Keeping: ink swatches (four ink colours added to the palette), a gsm guide on a dot-grid field, bindings compared, pencil grades, the testing desk, evening classes, pen repair, gift sets, a monthly letter box, a paper sample pack, desk objects, how the notebooks are sewn (lightbox photos), what the staff use, a school list, a contact line and an alternative hero that opens on the category list.
- Tables cut from six patterns to three (fountain-pen test results, wholesale price list, postage). The ruling selector, diaries, hours, classes and guides use hairline rows built from groups. No table on the home page.
- New pages: Classes and repairs, Paper guides, Gifts. Seven notes posts, each using the kit.
- Image lightbox on globally.
