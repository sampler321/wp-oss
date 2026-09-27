# bind: notes

- Direction: private-press book typography for a two-person bindery (Wójcik Bindery, Kazimierz, Kraków; the owner's "introligator"). The home page opens on a bottle-green buckram "front board" with a gold-tooled double frame, then paper pages with running heads, a contents page with dot leaders, side-notes in the outer margin, and a colophon for a footer.
- Fonts: Goudy Bookletter 1911 (display, as registered for 262) and EB Garamond with true italics. After the no-monospace rule, running heads, captions, labels and side-notes use EB Garamond italic or small roman with lining tabular figures, the way a printed book sets them. Two families.
- Palette: laid paper #F4F1EA, ink #1E1B18, buckram green #1F4D3A, gold foil #D6B56E (only on green), gold rule #8C6D2A (hairlines), board #E8E1D1. Eight cloth swatch colours live in the palette so a bindery can rename and retune them in Styles.
- Signature: the cloth swatch library (swatch squares, maker codes, stock notes such as "mill closed 2022", "Use this cloth" starting an email with the code) plus the "colours are indicative" note and a free sample offer.
- Case studies are posts in Conservation, Bindings, Boxes and Theses, each with a before/after pair at the same 4:5 crop and a spec table. Price guide, services, workshops, swatches and visit are page-layout patterns.
- Core-block limits: "Use this cloth" cannot fill a form field without JavaScript, so it opens an email with the code in the subject. Swatch filtering by line is not possible with core blocks; swatches are grouped in one grid.
- Tables and dot leaders needed top-level CSS: block-level `css` on core/table is scoped to `.wp-block-table > table` at zero specificity and loses to core's borders.

## Round 2

- Case studies: the owner saw "case studies that don't exist" (single posts redirected to the home page on the demo build). There are now eight case studies; four are full write-ups built from a new case-study kit: before and after pair, what came in (with a side-note), what we did (steps and bench time), what we left alone, a closer look, spec rows and a note from the client. The same builders make the patterns and the posts, and "Case study: full layout" assembles them.
- Seven new case-study patterns (48 in all). Spec sheets are ruled label/value rows; tables stay only for genuinely tabular price lists (7 of 48 patterns).
- Home h1 is now the bindery's name with one line of fact under it, on the green front board; the old two-sentence motto is gone.
- Image lightbox enabled in theme.json and on before/after pairs, detail photos and materials.
