# Coat: notes

- Direction: a paint chart. The owner asked for "more colours and fun", so the restrained colour-card look in the research became a loud fan deck: the front page opens with eight tall paint chips, each a real paint (maker's name and number) and the street it went on. Chips sit at slight angles, like cards fanned on a table, and straighten on hover.
- Fonts: Rowdies (display, chunky sign-writer sans, newly claimed because the brief moved away from Gambetta) and Figtree (body, also used small with tabular figures for colour codes and prices). Two families, no monospace.
- Palette: primer white, railings black, Bamboozle red accent, primrose surface, plus eleven chip colours named after the paints. Every chip's text colour is checked at 4.5:1 in the build script.
- Signature: every job post opens with a colour card (chips with colour name, number and where the paint went) and a facts table. The "Colour card" pattern lets owners add their own; chip colours are palette presets.
- Also: printable room-by-room colour schedule, an honest Dublin price guide, "who will be in your home", heritage and lead-paint notes, a season notice bar in the header, and a one-page brief for architects.
- Core-block limits: no before/after slider (the "Before and after" pattern puts two captioned photos side by side instead). Chip colours per job are chosen by hand from the palette, since posts have no colour fields.
- Tooling notes: the normaliser strips `layout` from any Group that also has padding or border in `style`, so all padded or bordered layout groups use section styles instead. Section-style CSS drops the first selector of a comma list and flattens `@media`, so responsive and motion rules live in theme.json `styles.css`.
