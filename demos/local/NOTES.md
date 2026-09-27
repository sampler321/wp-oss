# Local (Frome Survey)

- Direction: the owner asked for "more scientific looking", so the hyperlocal paper is set like a journal issue and a lab report. Each report opens with an abstract box, numbers its sections, and ends with a numbered source list. Tables and figures are captioned "Table 1", "Fig. 2" automatically by CSS counters in theme.json, so editors never number them by hand.
- Fonts: Newsreader (display, journal-title serif, claimed in demos/local/fonts-claim.txt because the brief moved away from the researched Francois One) and Public Sans for everything else, with tabular figures in tables and dates. No monospace.
- Palette: white paper, ink #111417, figure red #B8321A for figure and table labels, chart blue #1D5A85 for links and bars, graph-paper surface #F2F5F7 with a 20px grid drawn in CSS from the line colour.
- Signature: the public meetings tracker (date, body, topic, in person / remote / both with ● ○ ◐ markers, agenda, our notes) and a "Public meetings this week" rail next to the lead report on the front page.
- Also: "Figure of the week" bar chart built from a core Table with block characters (is-style-bars), funding and spending tables, corrections log, IMPRESS complaints procedure, newsletter chooser, membership amounts, tips, stockists, election results table, explainer series.
- Core-block limits: no real charts (bars are block characters in a table cell), no live meeting filter (the tracker is a table; Query Filter would do it with a plugin), meetings are a pattern, not a post type.
- Known tool issue: in the local Playground, pretty post permalinks (/post-slug/) redirect to the home page because the demo builder changes permalink_structure without re-initialising $wp_rewrite before flushing. Pages and category archives are fine. Singles render correctly via /index.php?name=slug.

## Round 2

- Tables cut from 16 patterns to 5 (meetings tracker, funders, spending, corrections log, election results: all real tabular data). The meetings rail, newsletter chooser, membership amounts, tips, newsroom, stockists, events and explainer series are now ruled rows, cards and ordered lists. The bar figures are rows of block characters, so the home page has no table.
- Image lightbox on globally. 55 patterns, with new ones for a reporter box, an update log, a quote from a meeting, how to attend a meeting, areas covered, a photo figure, a photo essay gallery, membership questions and newsroom contact.
- Posts now pull in the story furniture (pull figure, photo figure, limits note, data download, update log, reporter box, meeting quote, method note, sources), and pages use the new patterns. The automatic pattern library shows the rest.
- Lead story h1 is the latest report's headline, which doesn't end in a full stop.
