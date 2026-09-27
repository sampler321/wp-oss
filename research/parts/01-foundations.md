# WP-OSS: Research on block themes for independent creatives

> Initial research: what you can build on native WordPress block themes, who would use each one, and **~310 theme ideas across 31 sectors**, each based on real, live sites.
> Scope: **block themes only** (FSE: `theme.json`, `templates/*.html`, `parts/*.html`, `patterns/*.php`, `styles/*.json`). No classic editor or page builders. Every plugin must be free/OSS, block-native, and essential.
> Audience: small independent users (artists, architects, musicians, makers, tiny studios, micro-shops, local businesses, tradespeople, clinics, clubs, co-ops, collectives, schools, campaigns, individuals), not enterprise.
> Aesthetic: **current (2025–26), hand-crafted, and distinctive.** Art-school and brutalist directions are the house accent, not a uniform. Each idea has its own explicit style brief.

### Ground rules (non-negotiable)
1. **Grounded in reality.** Every idea, template list, pattern, and signature feature comes from real live sites of that type. Each entry cites them ("Real-world basis", "seen on"). Nothing speculative.
2. **Nothing vibe-coded.** See `ANTI-VIBE.md` (263 traits, 53-question sniff test), `ANTI-VIBE-FIELD-STUDY.md` (65 measured AI-built sites, 40 lint rules) and `ANTI-AI-WRITING.md` (writing tells, zero em dashes, `copylint`): no purple gradients, no shadcn-default cards, no pill-badge heroes, no icon-in-a-circle feature grids, no filler marketing copy. Every theme is checked against the sniff test before release.
3. **Explicit style per idea.** A named direction, exact free fonts, hex palette, layout, imagery, motion, and a live example of the style.
4. **Native only.** Block themes (like Automattic's), core blocks first, and a plugin only when it is essential.
5. **Screenshots.** Every reference deep link is captured (desktop + mobile) into `screenshots/NNN-k.jpg`.

---

## Part 1: What stock WordPress can do in 2026 (no plugins)

This is the base every theme is built on. If core already does something, don't add a plugin for it.

| Capability | Core feature | What it unlocks for these themes |
|---|---|---|
| Whole-site templating | Site Editor, `templates/`, `parts/` | Every page type ships as an editable HTML template |
| Design tokens | `theme.json` (v3): palette, fluid type, spacing scale, shadows, layout widths | The brutalist system: hard grids, raw colour, huge fluid type |
| Theme variations | `styles/*.json` | 3–5 looks per theme (e.g. "Riso", "Blueprint", "Terminal", "Newsprint") |
| Section styles | Block style variations in `theme.json` (6.6+) | Inverted, outlined, and "exposed grid" sections applied per group |
| Patterns | `patterns/*.php`, synced patterns, pattern overrides (6.6+) | The "50+ pre-made blocks" promise. Overrides let a user reuse one case-study layout with new content |
| Starter page patterns | `Block Types: core/post-content` patterns | "New page → pick a layout" modal (About, CV, Pricing, FAQ, Press…) |
| Dynamic lists | Query Loop, Post Template, pagination, "sticky" handling | Works grids, news lists, exhibition archives |
| Lightbox | Image block "Expand on click" (6.4+) | Enlarged work previews without a plugin |
| Custom fields → blocks | Block Bindings API (6.5+, UI 6.7+) | Bind "Year / Medium / Dimensions / Client" meta to Paragraph/Heading/Image/Button blocks |
| Interactivity | Interactivity API (6.5+) | Filters, type testers, cursor-follow previews, countdowns, audio players, all declarative and server-rendered |
| Fonts | Font Library (6.5+), `fontFace` in theme.json | Self-hosted grotesks and monos. No Google calls (GDPR-friendly) |
| Footnotes | Footnotes block (6.3+) | Essays, poets, academics, curators |
| Details/Accordion | Details block. Accordion block landed in 6.9 | FAQ, CV sections, colophons |
| Navigation | Navigation block + overlay | Index-style menus, full-screen overlay menus |
| Media | Cover (video bg), Video, Audio, Embed (Bandcamp, Vimeo, YouTube, SoundCloud, Mixcloud, Spotify) | Reels, discographies, mixes |
| Access control | Password-protected posts/pages | Client proofing, gallery viewing rooms, press areas |
| Time | Post date + Query Loop order | Newsletter/blog/journal |

**Main gap in core:** no custom post types, no meta-based querying in the UI, and no front-end faceted filtering. Those are the only places we need plugins (see Part 2).

**Rule from the WordPress.org theme directory:** themes may not register CPTs or other functionality. Content models live in either (a) one shared `wp-oss-companion` plugin for the whole library, or (b) Secure Custom Fields JSON that ships with each theme. Recommendation: **one small companion plugin** that registers opt-in CPTs (Work, Project, Exhibition, Event, Release, Episode, Book, Case Study, Person, Stockist) plus meta and bindings sources. It also provides 6–10 custom Interactivity-API blocks that the whole library shares.

---

## Part 2: Essential plugin toolkit (free, OSS, block-native)

Use as few as possible. Each theme lists which of these it needs.

| Need | Plugin | Why this one |
|---|---|---|
| Commerce | **WooCommerce** | Fully block-based cart/checkout, Product Collection, Product Filters, mini-cart, and block templates themes can override. Supports simple/variable/grouped/external/downloadable products |
| Content model (if not using companion) | **Secure Custom Fields** (WordPress.org fork of ACF) | CPTs, taxonomies, fields. Works with Block Bindings |
| Meta/date queries in Query Loop | **Advanced Query Loop** (Ryan Welcher) | "Upcoming vs past" exhibitions, events, and tour dates; order by meta |
| Front-end filtering | **Query Filter** (Human Made) | Taxonomy/post-type filter blocks for Query Loop ("Painting / Drawing / Print") |
| Masonry/mosaic | **Jetpack Tiled Gallery** *or* a theme block style (CSS columns) on Gallery/Post Template | Masonry works grids. Prefer the theme block style to keep zero dependencies |
| Forms | **Jetpack Forms** | Native-feeling contact, commission, and booking-request forms |
| Newsletter / paid posts | **Jetpack Newsletter + Paid Content**, or **MailPoet** | Writers, labels, zines |
| Events & tickets | **The Events Calendar** + **Event Tickets** (RSVP + Woo) | Venues, theatres, supper clubs. Alternative: companion "Event" CPT + Advanced Query Loop for lightweight cases |
| Courses | **Sensei LMS** (Automattic, block-based) | Ateliers, music teachers, online courses |
| Podcast | **Seriously Simple Podcasting** or **PowerPress** | RSS feed + episode blocks |
| Donations | **GiveWP** or Jetpack Donations block | Nonprofits, residencies, artist-run spaces |
| Subscriptions (free) | **Subscriptions for WooCommerce** (WP Swings) or Jetpack recurring payments | Coffee, CSA boxes, zine subscriptions |
| Pickup/delivery dates | WooCommerce Local Pickup (core Woo) + **Order Delivery Date (Lite)** | Bakeries, florists, farm shops |
| Maps | **Out of the Block: OpenStreetMap** | Murals, stockists, food truck spots. No Google API key |
| Code highlighting | **Code Block Pro** | Creative coders, devs |
| Booking | **Cal.com embed** (OSS) or **Simply Schedule Appointments** | Tattoo, music lessons, studios, therapists |
| Age gate | **Age Gate** | Wine, brewery, hot-sauce (sometimes), tattoo |
| Multilingual | **Polylang** | Translators, EU studios |
| Hotel | **MotoPress Hotel Booking Lite** | Guesthouses |
| Theme dev | **Create Block Theme** (Automattic) | Build and export themes from the Site Editor. The main dev tool for this whole project |

---

## Part 3: The full list of site types (granular)

This is the full list to pick from. The 100 ideas in Part 4 are selected from it. Keep the rest as a backlog to reach "5+ templates per type".

### 3.1 Independent e-commerce: 32 types
1. Illustration / art-print shop
2. Limited-edition photography prints
3. Ceramics "drop" shop (small batches, sells out fast)
4. Vintage & second-hand clothing (one-of-one stock)
5. Independent fashion label
6. Handmade jewelry
7. Specialty coffee roaster (subscriptions)
8. Loose-leaf tea merchant
9. Independent bookshop
10. Record shop (new + used vinyl)
11. Record label webstore / band merch
12. Zine & small-press distro
13. Stationery, paper goods, risograph prints
14. Plant shop / nursery
15. Florist (delivery dates)
16. Small-batch skincare & soap
17. Candles & home fragrance
18. Bakery / patisserie pre-order & pickup
19. Hot sauce / pantry / small-batch food
20. Natural wine shop
21. Craft brewery taproom shop
22. Farm shop / CSA veg box
23. Hand-dyed yarn & knitting patterns
24. Wooden / heirloom toy maker
25. Pet accessories maker
26. Skate / surf shop
27. Art supplies store
28. Digital goods: presets, brushes, textures, 3D assets
29. Fonts / type foundry
30. Furniture & object editions
31. Custom bicycles / frame builder
32. Poster & print-on-demand shop

### 3.2 Visual art
Illustrator · painter · fine-art photographer · documentary photographer · wedding/portrait photographer · sculptor · installation artist · performance artist · ceramicist · glass artist · textile/fiber artist · printmaker · muralist/street artist · tattoo artist · comic artist/webcomic · children's-book illustrator · generative/digital artist · video artist · collage artist · art collective · artist-run space · commercial gallery · project space · degree show · art school unit · residency · curator · art writer/critic · art-book fair.

### 3.3 Architecture & spatial
Architecture studio · solo practice · competition/research practice · landscape architect · urbanist/planner · interior designer · exhibition/scenographer · furniture designer · lighting designer · architectural photographer · architecture school unit · architecture magazine.

### 3.4 Design & digital
UX/product designer · graphic designer · typographer · type foundry · branding studio · motion designer · 3D/CGI artist · creative developer · web dev co-op · game studio · UI kit/asset seller · illustration agency (artist reps) · fashion designer · jewelry designer · industrial designer · design conference.

### 3.5 Film & moving image
Filmmaker · documentary project site · cinematographer · editor · colourist · animation studio · micro film festival · micro-cinema · VJ/visual artist.

### 3.6 Music & sound
Band · solo artist · singer-songwriter · independent label · DJ/producer · composer (film/game) · classical ensemble · jazz combo · choir · music teacher · recording studio · mastering engineer · DIY venue · club night/promoter · community radio · online radio · podcast · festival · sound artist · instrument builder (luthier, synth maker).

### 3.7 Performance
Theatre company · dancer/choreographer · stand-up comedian · drag/cabaret performer · circus/acrobatics · magician · spoken word/poet performer · puppetry company.

### 3.8 Writing & publishing
Novelist · poet · literary magazine · zine · small press · paid newsletter · freelance journalist · translator · academic · research lab · digital garden · illustrated-book author · cookbook author · essayist.

### 3.9 Food & hospitality
Restaurant · café · natural wine bar · supper club / pop-up · food truck · bakery · guesthouse/B&B · cabin rental · campsite · cooking school.

### 3.10 Trades & home services
Plumber/heating · electrician · solar/heat-pump installer · carpenter/joiner · kitchen fitter · builder/renovation · loft conversion · painter & decorator · plasterer · tiler · roofer · landscaper · gardener · arborist · fencing · locksmith · glazier · window cleaner · cleaning company · removals · handyman · chimney sweep · stove installer · upholsterer · furniture restorer · pest control · pool maintenance · damp proofing · stonemason · blacksmith · thatcher.

### 3.11 Health, wellbeing & beauty
Therapist/counsellor · psychologist · physio · osteopath · chiropractor · dentist · orthodontist · GP practice · optician · pharmacy · audiologist · podiatrist · midwife · doula · lactation consultant · sleep consultant · dietitian · speech & language therapist · occupational therapist · vet · yoga · pilates · barre · massage · acupuncture · float/sauna/bathhouse · barber · hair salon · nail studio · brow/lash studio · tattoo removal · home care agency · hospice.

### 3.12 Professional services
Bookkeeper · accountant · tax adviser · solicitor/lawyer (tenant, immigration, family, employment) · notary · mediator · financial planner · insurance broker · mortgage broker · estate agent · letting agent · surveyor · architect-technologist · planning consultant · business coach · life coach · career coach · virtual assistant · recruiter · translator · interpreter · sustainability consultant · HR consultant · funeral director · celebrant · private investigator.

### 3.13 Mobility & transport
Independent garage · MOT centre · classic car restorer · motorbike workshop · driving school · motorcycle training · cycle courier · bike repair · e-bike rental · car club · taxi co-op · boat charter · boatyard · marina · flying school · gliding club.

### 3.14 Education & childcare
Forest school · independent/free school · Montessori/Steiner · nursery · childminder · after-school club · tutor · exam coach · language school · coding club · online course creator · homeschool co-op · adult education · art school/atelier · music school · dance school · swim school · driving school · university society · summer camp · holiday club.

### 3.15 Tech & indie software
Indie SaaS · mobile app · WordPress plugin business · browser extension · developer tool/API docs · open-source project · hardware kits · build-in-public founder · freelance developer · product changelog/roadmap · status page · game mod community · Discord/community bot.

### 3.16 Civic, political & nonprofit
Election candidate · councillor · local party branch · tenants' union · trade union branch · mutual aid · community land trust · housing co-op · energy co-op · food bank · community fridge · repair café · library of things · tool library · animal rescue · environmental group · residents' association · neighbourhood plan · petition/single-issue campaign · refugee support · youth club · community centre · village hall · parish council · allotment society · credit union · time bank.

### 3.17 Sport & fitness
Amateur football/rugby/cricket club · running club · cycling club · triathlon club · climbing gym · martial arts dojo · boxing gym · CrossFit box · swim school · rowing/sailing club · surf school · ski school · roller derby · skate park · tennis club · padel club · bowls club · personal trainer · esports team · athlete personal site · local league · tournament.

### 3.18 Faith & spirituality
Church/chapel · mosque · synagogue · temple/gurdwara · Quaker meeting · meditation centre · retreat centre · interfaith group · tarot/astrology practitioner · celebrant.

### 3.19 Travel, tourism & outdoors
Walking tour guide · adventure operator · town/village tourism · heritage trail · overland/bikepacking blog · hiking routes · wild swimming · sauna community · campsite · hostel · B&B · cabin · houseboat · lighthouse stay · vineyard stay.

### 3.20 Hobbies, clubs & fandom
Chess club · TTRPG campaign · board-game group · fan site/wiki · collectors' catalogue · naturalists/birding · model railway · astronomy · beekeeping · ham radio · cosplay · knitting circle · book club · film club · allotment · fishing club · photography club · quiz league · crossword/puzzle site.

### 3.21 Events & occasions
Wedding (couple) · wedding planner · small conference · meetup · hackathon · fundraiser/charity run · reunion · private party · birthday · baby shower · memorial service · village fête · open studios trail · street party.

### 3.22 Personal
Link-in-bio · CV · IndieWeb homepage · memorial · family recipes · genealogy · reading log · photo-a-day · travel journal · baby book · pet site · "now" page · uses page · personal wiki.

### 3.23 Heritage, museums & archives
Small museum · historical society · oral history · heritage railway · "Friends of" group · community archive · listed building/trust · shipwreck/maritime society · industrial heritage site.

### 3.24 Making, manufacturing & small B2B
Laser/CNC cutting · 3D printing · sign maker · print shop · contract workshop · packaging · garment CMT · architectural salvage · foundry · pottery supply · timber yard · picture framer.

### 3.25 Directories, boards & marketplaces
Niche job board · local business directory · classifieds/swap · freelancer directory · what's-on aggregator · city/food guide · makers' market listing · open-studios map · volunteering board.

### 3.26 Farms & land
Vineyard · orchard/PYO · honey · sheep/alpaca wool · market garden · riding stables · dairy/creamery · flower farm · Christmas tree farm · care farm · city farm.

### 3.27 Pets & animals
Dog walker · groomer · trainer · cattery/boarding · pet sitter · breeder (ethical) · equine vet · farrier.

### 3.28 Spaces, hire & unusual services
Makerspace · coworking · escape room · games bar · camera rental · tool hire · party/marquee hire · photo booth · kids' entertainer · magician · wedding band/DJ · piano tuner · watch repair · bookbinder · luthier · synth/pedal maker.

### 3.29 Land, food craft & self-sufficiency
Tiny house builder · van conversion · homestead · permaculture · foraging · mushroom grower · cheesemaker · butcher · fermenter · cidery/meadery · seed library · darkroom co-op · dark-sky site · citizen science · death doula.

### 3.30 Odd formats & single-purpose sites
Documentary impact campaign · crowdfunded pre-order · one-product store · pop-up shop · online exhibition · net-art · manifesto page · activist toolkit · countdown/launch microsite · community cookbook · dialect archive · time bank · community shares offer · street-tree map.
