# case: notes

- Direction: the owner asked for kapicadesign.com "but a bit more edgy". Kept from Kapica: the ruled header, a two-column hero, case studies as wide image-left / text-right cards on a grey page, and a case page that opens with a facts row under a rule and runs in stages (research, design, results). Made edgier: square corners, 2px black frames, condensed heavy headings, full-bleed black stage bands, signal blue buttons and a lime marker used only for the one fact that matters on a screen.
- Fonts: Hubot Sans (registry face) set condensed with font-stretch 80% at weight 800 to 900; Atkinson Hyperlegible Next for text.
- Palette: fog #F1F1EE, ink #0E0E0E, signal blue #1F3BFF, lime #D7FF3A (marker only, always with ink text), white cards.
- Case study patterns: case-hero (role, timeline, team, platforms, tools + lead screen), stage-band, case-problem, research-insights, before-after (labelled screens with a "what changed" line), results (a sourced before/after table, not a stat row), client-quote, what-id-change, next-case (Query Loop, offset 1), and case-study-full which chains them.
- Signature from research: work-list, a table where published case studies link through and NDA projects show a lime "Under NDA" marker and no link; nda-entry for a single card.
- Also: capacity note, engagement models with "when this fits", process, what I do not take on, one-page CV, talks, newsletter.
- Images: CC0 photos of ticket machines, parking meters, self-checkouts and station concourses stand in for project screens; no device mock-ups.

## Round 2
- Rebuilt as a case-study kit: 29 case-study blocks (category "Case study blocks"), each generated from one data function so every study uses the same markup: overview facts, intro and contents, stage band, problem, hypothesis, constraints, research methods, insights, research quote, field photo, personas, journey map, user flow with arrows, wireframes, options considered, before and after, design system, prototype, usability testing, metrics with sources, client quote, learnings, credits, screens gallery, timeline, annotated screen, NDA note, next case study. 54 patterns in total.
- Four complete case studies as posts (ticket machines, parking, self-checkout, stop displays), each composed from the kit with its own content; the first uses the pattern references directly. Two writing posts added (6 posts).
- Screens, wireframes, a journey sketch and a UI kit sheet were drawn for the demo (`build/case_screens.py`, CC0, credited) so studies show real flows instead of stock photos.
- Home now opens with a name, one line and the latest case study (Query Loop), not a motto. The work list is ruled rows, not a table; only the CV is a table.
- Image lightbox on globally. Pattern categories registered in functions.php.
