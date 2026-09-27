# Patchnotes

- Direction: a developer podcast ("Minor Version", Ghent) laid out as release notes. The newest episode sits on a pale "hunk" band like the top entry of a changelog: a fact rail on the left (episode, date, length, hosts, guest), title and player on the right.
- Technical through structure, not a terminal costume: show notes are sorted into Added, Changed, Fixed and Removed list styles, with +, ~, check and minus markers drawn in CSS. "Fixed" is where last week's mistakes are corrected on the record.
- Fonts: SUSE only (800 for headings, 400 for text), tabular and slashed-zero figures everywhere. No mono (owner rule).
- Palette: cool paper, graphite, commit green links, removal red, change blue for focus, hunk yellow for the latest release. Small radii (2 to 6px), hairline rules.
- Pages: release log (posts page with a topic list), guests table, a show changelog for changes to the podcast itself, support tiers with a sponsor policy, subscribe (which apps support chapters), about with a recording-setup table.
- Episode numbers are tags ("Episode 88") and topics are categories, both shown in the rail and the log.
- Variations: Night build (dark), Blueprint (blue), Release day (white and orange).
- Core-block limits: chapter timestamps open the audio file at that time (#t= fragment). Demo audio is public-domain White House "As Told By" recordings about Grace Hopper, Ada Lovelace and the ENIAC programmers.

## Round 2

- Owner: "should be hacker themed, looks pretty bad". New direction: a BBS and demoscene screen. Phosphor green on near-black, amber for highlights and episode numbers, grey 16colors-style title bars on ANSI boxes, a stepped dither band (CSS conic-gradient checker, masked), static scanlines over the whole page (a fixed repeating gradient, no animation), and a green phosphor duotone on every photo.
- Display face is now Bitcount Prop Single, a proportional pixel font (monospace stays banned). SUSE moved to body text. Claimed in fonts-claim.txt.
- The home page opens like a BBS login: a prompt line, the newest episode as the h1, a dither band, the player and an episode.nfo box. Episodes read as a commit log (episode number in amber, date, topics, message). Show notes keep the Added / Changed / Fixed / Removed diff lists.
- 42 patterns (was 30): title screen, commit log, sysops, oneliners, greetz, parties (meetups), BBS main menu, episode files, dither band, release-day log, tier boxes, guest lines, phosphor screenshot. Tables are gone from the home page and down to two patterns.
- Variations: Amber monitor, Cyan BBS, Teletype paper.
