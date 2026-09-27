# Build status

Source of truth for the theme build loop. Update after every step.

Legend: `todo` → `building` → `built` → `tested` → `deployed`

| # | Slug | Idea | Brief from the owner | Status | Demo |
|---|---|---|---|---|---|
| 1 | ink | 001 Illustrator portfolio + shop | as researched | deployed | https://wposs-ink.b-j-kapica.workers.dev |
| 2 | oil | 002 Painter, studio and available works | as researched | todo | |
| 3 | kiln | 006 Ceramicist, shop updates and kiln openings | as researched | todo | |
| 4 | wall | 009 Muralist / street artist | more edgy, cargo.site-like, inspired by All Caps festival Rotterdam | todo | |
| 5 | drum | 010 Riso and printmaking studio | definitely neo-brutalist | todo | |
| 6 | seed | 011 Generative / creative-code artist | as researched | todo | |
| 7 | commons | 012 Artist-run space / collective | prettier, less brutal, image heavy | todo | |
| 8 | room | 019 Interior designer + shop | as researched | todo | |
| 9 | joint | 021 Furniture and object designer | as researched | todo | |
| 10 | case | 022 UX / product designer case studies | inspired by kapicadesign.com, a bit more edgy | todo | |
| 11 | glyph | 024 Independent type foundry | as researched | todo | |
| 12 | studio | 025 Small branding studio | as researched | todo | |
| 13 | karat | 032 Jewelry maker | as researched | todo | |
| 14 | rep | 033 Illustration / artist representation agency | as researched | todo | |
| 15 | reel | 034 Independent filmmaker / film site | heavily inspired by International Film Festival Rotterdam | todo | |
| 16 | amp | 038 Band / solo musician | duotone | todo | |
| 17 | catalog | 039 Independent record label | inspired by a cassette label | todo | |
| 18 | bpm | 040 DJ / producer, also works for independent radio | NTS-inspired, could be inspired by Radio Kapitał Warsaw | todo | |
| 19 | booth | 044 Recording studio | actually modern, like studionagrywarka.pl | todo | |
| 20 | freq | 046 Community / online radio station | yes, that radio station | todo | |
| 21 | wavelength | 046b Second radio station | another radio station, different direction | todo | |
| 22 | confidante | 047a Podcast: women's conversation show | podcast variant: women | todo | |
| 23 | evidence | 047b Podcast: true crime | podcast variant: true crime | todo | |
| 24 | patchnotes | 047c Podcast: tech | podcast variant: tech | todo | |
| 25 | spine | 051 Novelist / author | Penguin aesthetics | todo | |
| 26 | dispatch | 052 Independent journalist / paid newsletter | cutting-edge news, sharper | todo | |
| 27 | local | 053 Hyperlocal news | more scientific looking | todo | |
| 28 | pantry | 058 Recipe site / cookbook author | like ottolenghi.co.uk or mob.co.uk | todo | |
| 29 | larder | 058b Independent recipe blog | like jadlonomia.com | todo | |
| 30 | roast | 059 Specialty coffee roaster | as researched | todo | |
| 31 | shelf | 060 Independent bookshop | Penguin or illustration-ish, style heavy; branding of Plato Rotterdam | todo | |
| 32 | crate | 061 Record shop | more Balenciaga-like or Zara-like | todo | |
| 33 | thrift | 062 Vintage clothing | as researched | todo | |
| 34 | paper | 067 Stationery and paper goods | as researched | todo | |
| 35 | deck | 076 Skate / surf shop | more edgy, Thrasher-like | todo | |
| 36 | stem | 077 Florist | more style and colour heavy | todo | |
| 37 | good-dog | 078 Pet goods maker | more rainbows, more fun and funny | todo | |
| 38 | drop | 082 Creator merch drop store | Nirvana-style grunge, Julie (band) for reference | todo | |
| 39 | platter | 095 Catering company | more tasty, less elegant, more fun | todo | |
| 40 | scoop | 096 Gelateria | more professional, toned-down elegant, clean, technical | todo | |
| 41 | pipe | 097 Plumber and heating engineer | professional, toned-down elegant, clean, technical | todo | |
| 42 | coat | 101 Painter and decorator | more colours and fun | todo | |
| 43 | lingua | 132 Translator / interpreter | as researched | todo | |
| 44 | tick | 261 Watchmaker (zegarmistrz) | as researched | todo | |
| 45 | key | 105 Locksmith (ślusarz) | as researched | todo | |
| 46 | grain | new: Independent furniture maker | workshop maker, commissions | todo | |
| 47 | bind | 262 Bookbinder (introligator) | as researched | todo | |
| 48 | patchbay | 264 DIY guitar pedals | inspired by jhspedals.info | todo | |
| 49 | cityguide | 238 Independent city guide | inspired by thisiseindhoven.com | todo | |
| 50 | taproom | 088 Craft brewery | as researched | todo | |

## Pipeline
1. Reference theme `ink` + tools (fonts, images, demo builder, test harness, static export, deploy).
2. Fan out the remaining 49 to agents in batches.
3. Test every theme (`tools/test-theme.mjs`), fix, re-test.
4. Push to GitHub, deploy each demo to Cloudflare Pages.

## Log
- 2026-09-27: tooling done (fonts, images, blocks lib, normaliser, test harness, static export, deploy). `ink` passes 30/30 and is live. Repo: https://github.com/sampler321/wp-oss. 49 themes sent to 10 builders.
