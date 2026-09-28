# Evidence

- Direction: a true-crime podcast ("Low Water", Humber estuary) presented as the case file: a documentary title card over a greyscale archive photo, then dates, exhibits, sources and a dated corrections log. Respect for the person harmed is part of the layout (an "in memory" panel, a "how we report" list, help lines under every episode, no 999 audio).
- Fonts: Mozilla Headline (condensed via font-stretch 75%, upper case) for titles, labels and exhibit tags; Source Serif 4 for reading. Two families, no mono.
- Palette: near-black ground, bone text, manila folder panels with black ink, one signal red for warnings, links and buttons. All photos render in greyscale through block CSS (removable in Styles).
- Signature: the evidence board (tagged exhibits on a darker board), the manila file card that opens every episode, numbered sources, the redacted-statement pattern (bold words render as black bars) and the corrections log.
- Content model: one category per case (season), plus Updates for corrections; the "Update or correction" template frames those posts as a file card.
- Variations: Daylight file (manila paper), Night shift (navy with amber), Newsprint (grey).
- Core-block limits: chapter timestamps open the audio file at that time (#t= fragment) instead of seeking an on-page player.
- Demo cases, people and places are invented; the footer says so. Stand-in audio is a CC0 LibriVox reading.

## Round 2

- Tables out of the case file: the manila file card is now ruled label rows, and the timeline is ruled date rows, so the home page has no table. Tables remain only for the corrections log, support tiers, apps and transcripts.
- 42 patterns (was 34). New: people in this case (named with permission or by a court, everyone else by role), where the case stands, the places (lightbox gallery), season trailer, document with transcription, letters from listeners, further reading, between-seasons card.
- Image lightbox on globally (photos keep the greyscale treatment). Header, title-band and post-navigation borders moved into section styles.
