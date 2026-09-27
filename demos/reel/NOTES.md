# Reel: notes

- Brief: "heavily inspired by IFFR". Studied iffr.com (home, Programme A-Z, a film page) and built the site as a festival programme for one small Rotterdam production company (Verbeek & Tahiri Films): a black utility strip over a bright teal band header, a grey dates tab hanging under the name ("On tour: 9 October to 6 November 2026"), grey rounded programme cards with a white arrow notch, colour-coded category chips, outlined tag boxes on news, black buttons with an arrow, and a bold facts line on every film (director | runtime | countries | year | language).
- Fonts: Rethink Sans only (800 for titles, 400 for text), claimed in demos/reel/fonts-claim.txt because the brief replaces the research's Bellefair. No mono.
- Palette: white, black, festival teal #00C2A8 (always with black text), deep teal #00705F for link hover, programme grey #E8E8E8, plus four chip colours (Documentary blue, Fiction pink, Shorts lime, In development yellow). Variations: Harbour blue, Midnight, Tiger yellow.
- Content model: films are posts, categories are programme strands (the chip colour comes from the category slug). The film page leads with a 2.39:1 still, then laurels set as text, synopsis and credits, press quotes with outlet and rating, the screenings list, stills, where to watch, press kit, festival history and "Also in the programme".
- Signature: the screenings list, one grey rounded row per date with city, venue, a note and a black Tickets button; it becomes stacked cards on phones.
- Also: host-a-screening page with fees, press page (the copy tells owners to password-protect it in WordPress), newsletter, notice bar.
- Core-block limits: past screenings can't drop off automatically without a plugin, so the copy says they move to the archive monthly. The arrow notch and chip colours are CSS in theme.json; the lead card overlapping the still uses a section style with a negative margin.

## Round 2

- Image lightbox enabled globally in theme.json.
- 41 patterns (was 26). New: screenings as rows of grey cards for the home page (no table there now), trailer still linking out, 2:3 poster beside a synopsis, director's statement, funders as text, subtitles and access, study guide, year-round film club, awards, programme colour key, Q&A booking, co-producer call, crew call, single large press quote and film facts as rows.
- Tables are down to 4 of 41 patterns (screenings list on the film and screenings pages, festival history, credits, host fees).
- Home h1 is the lead film's title. Home shows the next five screenings as rows, not a table.
- Film pages use the full film-page pattern; Host, Press and About pages now use the new patterns so the demo shows the kit in context. The automatic Pattern library covers the rest.
- Mobile: the utility strip drops the Instagram link below 700px (it is in the footer), and the header button hides on phones.
