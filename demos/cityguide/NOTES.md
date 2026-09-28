# cityguide: notes

- Direction: the owner pointed at thisiseindhoven.com, which overrides the research's pocket-map serif look. Lampje is an independent weekly guide to Eindhoven (Sanne Verhoeven and Joost Bakker): white pages, a heavy expanded grotesk, signal red and tram blue, big rose sections. Its own local mark is the sawtooth factory roof of Philips' Strijp, used as the top edge of every coloured section and as the two red teeth of the logotype.
- Fonts: Mona Sans (expanded, 900) for headings, Work Sans for text. Two families, no monospace. The research face (Recia) is dropped because the brief changed direction; Mona Sans is claimed in demos/cityguide/fonts-claim.txt.
- Palette: white #FFFFFF, ink #111111, signal red #D80028 (pins, buttons, footer), tram blue #1C3FD6 (category labels, sentence case), rose #F2B8CF as section ground only.
- Signature: the map list. Numbered place entries (neighbourhood, one-paragraph review, address, hours, price band, "last visited") next to a sticky sketch map whose red pins carry the same numbers. The sketch map was drawn for this theme by build/cityguide_draw.py (CC0) and says "not to scale".
- Content: stories are posts in What's on, Eat and drink, Culture, Neighbourhoods, Day trips and Practical. This week (a timetable with day, time, place and price), the map, neighbourhoods, about and tips are page-layout patterns. Nice-to-haves built: closed-place flag, last-visited dates, accommodation by type, a print stylesheet so a list prints on one A4 sheet, corrections note.
- Core-block limits: pins do not highlight list items on hover (no JS). The sawtooth edge and sticky map use section-style and top-level CSS. Linked images lose aspectRatio in the editor round-trip, so the build writes the crop style onto the img itself.

## Round 2

- Sixteen new patterns (43 in all) from This is Eindhoven, Herb Lester, Tokyo Cheapo and The List: list cards by category, featured story, four things this autumn, a day in Strijp, the Dommel walking route, the printed folded map, delivery times, commissioned guides, parking and bikes, just opened, words you will hear, contributors, support Lampje, and a GLOW event highlight, plus page layouts.
- New pages: "Plan your visit" (in the menu) and "The printed map" (in the footer), so the Herb Lester-style printed guide and the practical sections are real pages. This week, the map, neighbourhoods and about now use the new patterns in context.
- Image lightbox enabled in theme.json. Tables stay only for tabular data (4 of 43 patterns); new practical lists are ruled rows.
