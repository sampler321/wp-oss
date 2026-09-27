# commons: notes

- Direction: "daylight on the gallery floor". The owner asked for prettier, less brutal and image heavy, so the researched photocopied notice board became a picture-led programme. Installation views run big, the current show sits under a full-bleed photo with a soft peach label card (like vinyl wall text by the door), and the programme grid is staggered.
- Fonts: Funnel Display (the registry face, used light at 400 to 500 instead of 800) and Funnel Sans for text. No mono; running numbers ("No. 184") use the display face with tabular figures.
- Palette: limewash #F4F3EE, soot #1F201C, kiln orange #B23A17 for links and numbers, peach #F5CDB9 label cards, sage #E3E7DC panels. 14 to 18px radii on photos and cards, 6px on buttons.
- Signature: the numbered programme. The front-page hero is a Query Loop of the newest post with a featured-image Cover, so "What's on" updates itself. Programme archive has category and year filter chips, and a static table for shows from before the website.
- Nice-to-haves built: closed-for-install notice (parts/notice.html), membership card with a flat fee, committee with terms and past members, access page, funders and credits table for grant reports, donate block, publications.
- Core-block limits: running numbers live in post tags (no custom fields). "Now / next / past" by date is not possible without a plugin, so "Coming up" is a pattern the committee edits by hand.
- Shared-tool notes: the normaliser drops `layout` from a plain div Group that also has a `style` attribute (worked around by using a section tag), drops `aspectRatio` on core/image, and single posts redirect to the home page in Playground until permalinks are re-saved, so official single-post screenshots show the front page.
