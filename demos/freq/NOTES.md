# Freq (Radio Havik)

- Direction: the full community radio station theme, as researched ("Swiss neo-grotesk index") and confirmed by the owner. White page, 1px black rules, a strict grid, text indexes instead of cards, show art as black and white squares that turn colour on hover, and a black live player bar fixed to the bottom of every page. It is a daytime station guide in sentence case and blue on white, so it reads nothing like bpm (black, condensed capitals, one DJ's archive).
- Fonts: Radio Canada only (the registry face for 046): 700 for headings, 400 for text, tabular figures for all times. DM Mono from the research was dropped under the no-mono rule.
- Palette: #FFFFFF, #000000, signal blue #0038FF for links and the support block, live red #FF3B00 used only for the on-air square. Variations: Pirate, FM, Late night.
- Signature: a seven-column weekly schedule with the station timezone printed on it and a red square on the slot that is live, plus a "live now / next" player bar (core Audio block with the stream URL) as a template part.
- Content model: shows are categories (the description is the show intro, category.html shows it beside the episode index); episodes are posts with an Audio or Embed block and a tracklist.
- Nice-to-haves as patterns: today's schedule, off-air notice with an end time, support block that says what the money pays for (licences, rent, DAB+, streaming), membership levels, submit a show, guest mix series, genre index, ways to listen.
- Core-block limits: "live now" cannot be computed from the schedule without a plugin, so the red square and the player bar text are edited by hand each day. Demo stream and archive URLs are placeholders.

## Round 2
- Image lightbox on globally.
- 41 patterns (was 26). New: one day of the schedule, show intro (art, host, slot), residents A to Z, genres as big links, picked from the archive, this week's guest mix, station events, merch, studio camera, station FAQ, hero with today as a list, contact cards, volunteer roles, episode credits. Studied on Kiosk Radio, Resonance FM, Noods Radio, Refuge Worldwide and Cashmere Radio.
- Tables cut from 8 patterns to 2 (tracklist and the shows index). Now/next, support costs, studio directions, ways to listen and membership are rows or cards.
- Home page has no table: today's list and the support costs are ruled rows. Added picks and station events to the home page.
- New demo page: Today. Episode posts now end with a show-art gallery.
