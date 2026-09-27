# Amp: notes

- Brief: "make it duotone". The site uses exactly two inks. The page is the highlight colour (signal orange #FF4F1F), text, rules and buttons are the shadow colour (#141414), and every core/image, core/cover and core/post-featured-image runs through a theme.json duotone preset (`band`) built from the same pair, set in styles.blocks. Reversed sections (black ground) switch images to the reversed preset (`band-reverse`). The three style variations swap the palette and the duotone pair together: Night (navy/sodium yellow), Folk (peat/cream), Punk (black/hi-vis yellow).
- Fonts: Karrik (Velvetyne, OFL, from Phantom Foundry's GitLab; fetch-fonts can't reach Velvetyne so the woff2 files were copied by hand) for titles and dates; Figtree for text with tabular figures. No mono.
- Band: Heysham Ferry, three people from Morecambe; album Slack Water on Saltpan Records.
- Signature: the Live page. Full-width dates table (date in a fixed first column, venue, town, support, one ticket link), grouped by tour and in-stores, with Low tickets and Sold out flags. It stacks into two-column cards on phones. The home page shows the next five as rows instead of a table.
- WooCommerce: 6 products (LP, CD, cassette, reissue, poster, tote). Woo product images can't take a theme.json duotone, so root CSS greys them and multiplies them onto the page colour to match.
- Core-block limits: past dates don't move to the archive automatically (the copy says monthly by hand). Videos are stills linking out, so nothing autoplays.

## Round 2

- Image lightbox on globally; 41 patterns including hero-as-poster, band members, listen and buy, how the record was made, photo pair, big press quote, ticket FAQ, radio sessions, videos, merch shipping, next show band, support-act note, setlist, lyric sheet, access and guest list, tour diary, stockists and a one-line mailing list.
- Tables cut to 3 of 41 patterns (live dates, workshops dates, formats); played-before and booking contacts are now ruled rows.
- 6 releases as posts; the album post uses the release-page pattern (tracklist, formats, credits, lyric sheet, setlist).
- Fixed a thin orange gap above the black footer (template-part top margin).
