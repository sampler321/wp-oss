# Anti-AI writing guide

Rules for every word we ship: pattern placeholder copy, demo content, readme.txt, docs, style variation names, alt text, and this research folder itself.

Companion to `ANTI-VIBE.md` (visual tells). This file covers words.

---

## 1. Why it matters

- **Small businesses sell on voice.** A plumber, a potter and a tenants' union win work because they sound like themselves. If our demo copy sounds like a chatbot, owners keep it (most never rewrite placeholder text), and their site sounds like everyone else's.
- **Readers notice, even when they can't name it.** Wikipedia's AI Cleanup project says untrained readers are close to chance at spotting AI text, but heavy LLM users get it right about 90% of the time. Our audience (designers, artists, developers) is exactly that heavy-user group.
<!-- copylint-off -->
- **The tells are measurable.** Kobak et al. found at least 13.5% of 2024 PubMed abstracts were processed with LLMs, detectable purely by an excess of words like *delves* (28x more frequent than expected), *underscores* (13.8x) and *showcasing* (10.7x). Liang et al. found *meticulous* was 34.7x more common in AI-modified peer reviews. If a lab can count it, a visitor can feel it.
<!-- copylint-on -->
- **Our own tools are part of the risk.** This library will be drafted with Claude. The Wikipedia page cites a July 2026 study finding that, among current models, only Claude uses em dashes more than professional writers. We are writing against our own defaults.

---

<!-- copylint-off -->

## 2. The em dash (hard ban)

### Rule
**No em dashes (U+2014) in anything we ship or write.** Zero. En dashes (–) only for number ranges (3–5, Mon–Fri, 2025–26). Hyphens (-) for compound words.

### Why this one gets a hard ban and not a "use sparingly"
- It is the single most recognised AI tell among the general public in 2025–26. Fair or not, one em dash on a bakery's About page gets the whole site read as AI-generated.
- LLMs use it where people would use a comma, a colon, brackets or a full stop, and in a formulaic "punched up" way: to set up a reveal, to stack a parallelism, to add a dramatic afterthought (Wikipedia, "Overuse of em dashes").
- AI em dashes are usually **spaced** ( -- ), against most typographic style guides, which is a second tell inside the first.
- Claude in particular over-uses it (see section 1), and we use Claude.
- A "sparingly" rule can't be linted. A ban can.

### What an em dash is usually doing, and what to write instead

| The em dash is… | AI version | Human version |
|---|---|---|
| Setting up a reveal | Our bread takes time -- 48 hours, to be exact. | Our bread takes 48 hours. |
| Adding an aside | Every print -- signed and numbered -- ships in a tube. | Every print is signed, numbered and shipped in a tube. |
| Stacking a parallelism | It's not just a haircut -- it's an experience. | (Delete. Say what the haircut costs and how long it takes.) |
| Introducing a list | We fix everything -- boilers, radiators, leaks. | We fix boilers, radiators and leaks. |
| A dramatic afterthought | We opened in 2009 -- and never looked back. | We opened in 2009. |
| Replacing a colon | One rule -- no phones at the table. | One rule: no phones at the table. |
| Attributing a quote | "Best coffee in town." -- Marta K. | "Best coffee in town." Marta K., regular since 2019 (set the name on its own line, no dash) |
| Joining two sentences | Book early -- we fill up fast in December. | Book early. December fills up by mid-November. |

### Watch for the dash's disguises
When a writer (or a model) is told "no em dashes", the habit moves to:
- **Spaced en dashes or hyphens** used the same way ("Book early – we fill up fast", "Book early - we fill up fast"). Also banned. The lint catches ` – ` and ` - ` between words.
- **Colons used for every reveal** ("The secret: time."). Colons are fine, but one reveal-colon per page at most.
- **Ellipses for drama** ("And then… we found it."). Banned in body copy.

The fix is almost never a different punctuation mark. Usually the sentence is doing a sales move, and the real fix is to drop the move and state the fact.

---

## 3. Catalogue of tells

Each entry: **tell** → why it reads as AI → human rewrite. Severity 1 (mild) to 5 (instant giveaway).

### 3.1 Vocabulary

**Tier A: never in shipped copy (severity 5).** Each one is documented as over-represented in LLM text by Wikipedia's AI Cleanup list, Kobak et al. or Liang et al.

delve, tapestry (abstract), testament, realm, landscape (abstract), pivotal, underscore (verb), showcase/showcasing, boasts (meaning "has"), meticulous/meticulously, intricate/intricacies, interplay, bolster/bolstered, garner, foster/fostering, vibrant, nestled, in the heart of, seamless/seamlessly, elevate, unlock/unlocking, unveil, unparalleled, transformative, groundbreaking, commendable, multifaceted, nuanced, embark, navigate (abstract), resonate with, align with, harness, leverage, empower, elucidate, encapsulate, paving the way, uncharted, a rich history, rich tradition, diverse array, enduring legacy, indelible mark, deeply rooted, evolving landscape, stands as, serves as, is a testament to, plays a crucial/pivotal/vital role.

**Tier B: allowed once per page only if literally true and no plainer word works (severity 3).** crucial, key (adjective), enhance, highlight (verb), ensure, robust, valuable, notable, remarkable, innovative, exceptional, compelling, comprehensive, curated, crafted, bespoke, journey (non-travel), passion/passionate, dedicated, commitment to, experience (as a noun for a service), solutions, world-class, cutting-edge, state-of-the-art, next-level, game-changer, effortless, supercharge, streamline, holistic, synergy.

**Tier C: GOV.UK's words to avoid (severity 2).** Use the plain version: agenda → plan, collaborate → work with, deliver → make or provide, deploy → use, empower → allow, facilitate → say what you do, focus → work on, impact (verb) → affect, initiate → start, liaise → work with, progress (verb) → work on, promote → recommend, tackle → fix or stop, transform → say what changes, utilise → use, one-stop shop → say what it is.

**Why a list works and a vibe doesn't:** Wikipedia's editors note that the words shift by model generation (GPT-4 era: *delve, tapestry, testament*; GPT-4o: *align with, fostering, showcasing*; GPT-5: *emphasizing, enhance, highlighting*). Lists need updating every six months. Section 7 has the linter; update its word list on that schedule.

**Opener words (severity 4):** "Additionally," "Furthermore," "Moreover," "Ultimately," "Notably," "Importantly," at the start of sentences. People writing a menu don't use them.

### 3.2 Phrase templates

| Tell | Sev | Why it reads as AI | Rewrite |
|---|---|---|---|
| "It's not just X, it's Y" / "Not only X but also Y" | 5 | Wikipedia's "negative parallelism": pretends to correct a misconception nobody had | State Y. "Tattoos, piercing and laser removal." |
| "No X, no Y, just Z" | 5 | Same pattern, compressed | "Walk-ins welcome." |
| "Whether you're a X or a Y…" | 5 | Audience-hedging opener | Pick the reader. "If you're booking a wedding, start here." |
| "In today's fast-paced world" / "In an age of…" | 5 | Throat-clearing | Delete the sentence. |
| "Welcome to [Name], where…" | 4 | Brochure opener | Start with the thing: "Sourdough, baked daily from 6am." |
| "Look no further" / "Your one-stop shop for" | 4 | Ad-copy cliché | Say what you sell and where. |
| "We believe that…" / "At [Name], we…" | 3 | Corporate distance | "We" plus a verb: "We roast on Tuesdays." |
| "Here's the thing" / "Let's dive in" / "Let's explore" | 4 | Chatbot transitions | Delete. |
| "At its core" / "At the end of the day" | 3 | Filler | Delete. |
| "From X to Y, we…" (From weddings to birthdays…) | 4 | A range that stands in for a list | List the three things you actually do. |
| "…, ensuring…" / "…, making it…" / "…, highlighting…" trailing clause | 4 | Wikipedia's "superficial analysis" via a trailing -ing phrase | End the sentence at the fact. |
| "Discover", "Explore", "Experience" as the first word of a CTA or heading | 4 | Ad verbs with no action behind them | Name the action: "See the menu", "Book a table". |
| "Crafted with love/care/passion" | 4 | Unfalsifiable | Say how: "Thrown on a kick wheel, glazed twice." |
| "Rest assured" / "peace of mind" | 3 | Insurance-speak | Give the guarantee: "If it leaks within a year, we come back free." |
| "Elevate your…" / "Take your X to the next level" | 5 | Peak slop | Say the outcome in numbers or nouns. |
| "Nestled in the heart of…" | 5 | Travel-guide autopilot (Wikipedia names both) | "On Mill Street, opposite the library." |
| "A haven for…" / "a hidden gem" | 4 | Review-site cliché | Describe one real detail of the place. |
| "Our team of dedicated professionals" | 4 | Could be anyone | Names and faces: "Ana and Tomek, both Gas Safe registered." |
| "We pride ourselves on…" | 3 | Self-praise without evidence | Show the evidence. |
| "Embark on a journey" | 5 | Unless it's a boat | Delete. |

### 3.2b Emphasis by negation (severity 5)

The most persistent AI rhetorical habit, and a wider one than the "not just X, it's Y" template. The writer makes a positive claim sound bigger by first denying something nobody said. Wikipedia calls the sentence-level version "negative parallelism". It says the text reads "as though it is clearing up a common misconception" that the reader never had.

**The test:** does the negative give the reader information they can act on? If yes, it's a **real limit** and it stays. If it only exists to make the next phrase land harder, it's **rhetorical negation** and it goes.

| Keep: real limits (useful, human) | Cut: rhetorical negation (AI) |
|---|---|
| We don't do gluten-free. | This isn't just bread. It's a ritual. |
| No card payments under £5. | No shortcuts. No compromises. Just coffee. |
| Commissions closed until March. | We're not your average plumber. |
| Dogs welcome, no under-12s after 7pm. | It's not about the haircut, it's about how you feel. |
| We don't ship originals outside the EU. | Not a template. A system. |
| Not suitable for dishwashers. | Forget everything you know about yoga. |

**Forms to catch:**

| Form | Example | Rewrite |
|---|---|---|
| Not just X, (but) Y | "Not just a gym, but a community." | "Open 6am–10pm. 40 classes a week." |
| X isn't/doesn't just…, it… | "Our studio doesn't just teach, it transforms." | Say what a class covers. |
| It's not X, it's Y (one or two sentences) | "It's not about the coffee. It's about the ritual." | Delete, or describe the ritual concretely. |
| Not X. Y. (fragment pair) | "Not a template. A system." | "37 patterns and 12 page layouts." |
| No X, no Y, (just) Z | "No fluff, no filler, just results." | Delete. Show the result. |
| Pre-emptive denial | "This isn't another gimmick." / "We're not like other agencies." | Delete. Nobody asked. |
| Zero/No + abstract noun fragments | "Zero compromises." "No nonsense." | Delete, or name the policy ("Fixed price, agreed before we start."). |
| All the X, without the Y | "All the flavour, without the guilt." | Give the number: "180 kcal." |
| Less X, more Y | "Less scrolling, more living." | Delete. |
| Forget X / Say goodbye to X | "Forget boring websites." | Delete. |
| X? Not here. / X? Never. | "Hidden fees? Not here." | "Prices include VAT and delivery." (state the positive fact) |
| Instead of X, Y / Rather than X, Y (as a flourish) | "Rather than simply retelling, it reimagines." | Only keep when comparing two real options for the reader. |
| Doesn't just / don't just + verb | "We don't just fix boilers, we build relationships." | "We fix boilers. Most of our customers have used us for years; ask for references." |
| Denial-then-reveal across a heading and body | H2: "More than a bakery". Body: "We're a community." | H2: "Opening times". |

**Why models do it:** it's the cheapest way to sound insightful. The pattern implies a misconception, corrects it, and makes the writer look perceptive, all without adding a fact. It also pairs with other tells: the em dash ("not X -- Y"), the rule of three ("no X, no Y, no Z"), and the colon reveal.

**In our own writing:** this research folder slipped into it too ("one option, not the default", "deep links, not homepages"). In research notes a contrast is sometimes the clearest way to state a rule, so the linter reports it there at severity 3. In shipped copy (patterns, demo content, readme) it is severity 5.

### 3.3 Structure

| Tell | Sev | Why | Fix |
|---|---|---|---|
| Rule of three everywhere ("fast, friendly and reliable") | 4 | Wikipedia's "rule of three": makes thin claims look complete | Use the real number of items: one, two, four. If there are three, fine, but not every time. |
| Every paragraph the same length (3 sentences, ~60 words) | 3 | Mechanical rhythm | Mix a one-line paragraph with a longer one. |
| Every sentence the same length | 3 | "Burstiness" is low in model text | Vary on purpose. Short. Then a longer one that carries detail. |
| A heading over every paragraph | 3 | Slide-deck habit | Headings mark real sections. A 200-word About page needs zero. |
| Headings containing only headings | 2 | Wikipedia lists it | Every heading gets text under it. |
| Intro that restates the heading, outro that restates the intro | 4 | Summary sandwich | Start with the first fact. End when you're done. |
| "In conclusion" / "In summary" / "Overall," | 5 | School essay | Delete. |
| "Challenges and future prospects" ending ("Despite its…, X faces challenges…") | 4 | Wikipedia's outline-like conclusion | Don't end a bio or About page on an outlook. |
| Importance inflation ("marking a pivotal moment in…") | 5 | Wikipedia's "undue emphasis on significance" | A bakery opening is not a pivotal moment. Give the date. |
| Balanced both-sides framing on a sales page | 3 | Hedging | Take a position: "We don't do rush jobs." |

### 3.4 Punctuation and formatting

| Tell | Sev | Fix |
|---|---|---|
| Em dash (any) | 5 | Banned. See section 2. |
| Spaced en dash or hyphen used as an em dash | 5 | Banned. |
| Bold inline header + colon on every bullet ("**Quality:** We…") | 4 | Wikipedia's "inline-header vertical lists". Plain bullets, or prose. |
| Bold scattered through body text for emphasis | 3 | Wikipedia's "overuse of boldface". Bold is for UI labels and prices, not ideas. |
| Title Case In Every Heading | 3 | Sentence case in all headings, buttons and nav ("Book a fitting", not "Book A Fitting"). |
| Emoji as bullets or heading decoration | 5 | None in shipped copy. |
| Exclamation marks | 3 | Max one per page, and only where a person would shout ("Sold out!" on a gig listing is fine). |
| Colon titles ("Sourdough: A Love Story") | 3 | Plain titles. |
| Ellipses for suspense | 3 | Banned in body copy. |
| Semicolons in marketing copy | 2 | Split the sentence. |
| Horizontal rules between every section | 2 | Wikipedia lists thematic breaks as a tell; use spacing and type. |
| Small tables for what should be a sentence | 2 | Wikipedia's "unusual use of tables". Use tables for real tabular data (prices, times, sizes). |

### 3.5 Tone

| Tell | Sev | Why | Fix |
|---|---|---|---|
| False enthusiasm ("We're thrilled to…", "We can't wait to…") | 4 | Performed feeling | Say the news. "The shop reopens 3 March." |
| Sycophancy toward the reader ("You deserve the best") | 4 | Flattery | Respect the reader's time instead. |
| Vague superlatives ("the finest", "exceptional quality") | 4 | Unfalsifiable | Replace with a checkable fact: flour source, years trading, licence number. |
| Hedging ("may help", "can potentially") | 3 | Legal nervousness everywhere | Be exact about what is true; hedge only where it's legally needed. |
| Weasel attribution ("Experts agree", "Customers love") | 4 | Wikipedia's "vague attributions" | Quote a named person, or drop it. |
| Fake specificity ("Over 10,000 happy customers") | 5 | Invented numbers in demo content | Demo content never invents stats. Use real-looking operational numbers instead (opening hours, prices, lead times). |
| Canned notability ("featured in leading publications") | 4 | Wikipedia's "canned emphasis on notability" | Name the publication and link the article, or drop it. |
| Chatbot service voice ("I hope this helps", "Feel free to reach out") | 5 | Wikipedia's "collaborative communication" | "Call or text 07700 900123. We answer 8am–6pm." |
| Moralising or disclaimers ("It's important to remember…") | 4 | Didactic disclaimer | Delete. |

### 3.6 Voice

These are the tells of absence: what AI copy doesn't have.

- **No point of view.** Real owners have opinions ("We don't sell decaf. Sorry."). Put at least one opinion in each demo About page.
- **No local detail.** Real sites mention streets, buses, the pub next door and the step at the entrance. Every demo site gets a real-feeling address, directions and one local quirk.
- **No numbers people use.** Real sites are full of operational numbers: £4.20, 48-hour ferment, 12 covers, closes 3pm Sundays, 6–8 week lead time. AI copy has marketing numbers (10,000+ customers, 99% satisfaction). Use the first kind and never the second.
- **No mess.** Real copy has a slightly odd sentence, a joke that only locals get, a sign-off. Leave some in.
- **No names.** Real sites say who does the work. Demo content names people.
- **Everything is positive.** Real sites say what they don't do: "No card under £5", "We don't do emergency call-outs on Sundays", "Dogs welcome, kids tolerated". Include limits.

### 3.7 Genre tells (by page type)

| Page type | AI version tell | Human version does |
|---|---|---|
| Artist bio | "[Name] is a multidisciplinary artist whose work explores the intersection of memory, identity and place." | Third person, short, factual: born where, studied where, works with what, shown where. "Kasia Nowak (b. 1991, Łódź) makes large woodcuts about river towns. She lives in Leeds." |
| About page | Mission statement, values in threes, "our story" arc | When and why it started, who's there now, what they do each day, one opinion. |
| Product description | "Elevate your space with this stunning, handcrafted piece" | Material, size, weight, how it's made, how to care for it, when it ships. |
| Menu | "A symphony of flavours", "delicately infused" | Dish name, 3–6 ingredients, price, allergen codes. No adjectives unless they're techniques (smoked, pickled). |
| FAQ | Questions nobody asks ("Why choose us?") | Questions people actually email: parking, deposits, cancellations, dogs, card payments. |
| Testimonials | "Absolutely amazing service! Highly recommend!" from "Sarah J." | Specific detail, full first name, context and date: "Fixed our boiler on Christmas Eve and didn't charge the holiday rate. Priya, Headingley, Dec 2025." |
| Case study | "Leveraging a user-centric approach, we delivered a seamless experience" | Problem in one sentence, constraints, what changed, what you'd do differently, real screenshots. |
| Services | "We offer a comprehensive range of solutions" | A price list. |
| Legal/T&Cs | Generic boilerplate that contradicts the business | Short, plain, specific to the trade (commission deposits, return window for prints). Mark clearly as a template to check. |
| readme.txt | "This versatile theme empowers you to create stunning websites" | What it's for, what it includes, which plugins it expects, how to set up the demo, and the changelog. |
| Alt text | "Image of a beautiful vibrant painting" | What is in the image: "Oil painting of a red boat on a grey beach, 60 × 80 cm." |
| Error/empty states | "Oops! Something went wrong." | What happened and what to do next (Anthropic's frontend guidance: errors don't apologise and are never vague). |

---

<!-- copylint-on -->

## 4. Voice briefs and before/after samples

For each archetype: a one-line voice brief, then an AI-ish version and a human version. The human versions are our demo-content standard. All names, places and numbers are invented for demo use but written the way real owners write.

### 4.1 Illustrator
**Voice:** first person, dry, practical about prints and deadlines.
<!-- copylint-off -->
**AI:** Welcome to my creative world! I'm a passionate illustrator whose vibrant work explores the intersection of nature and imagination. Each piece is meticulously crafted with love, bringing stories to life through bold colours and intricate details. Whether you're looking for a unique print to elevate your space or a bespoke commission, I'm here to help bring your vision to life. Let's create something magical together!
<!-- copylint-on -->
**Human:** I'm Joon, an illustrator in Bristol. I draw birds, maps and the occasional pub sign, mostly in gouache. Prints are A4 or A3 on 300gsm cotton paper, signed on the back, and they ship rolled in a tube within three working days. Commissions are open until the end of October. After that I'm drawing a book and won't take new work until March. Prices start at £180 for a single-bird portrait.

### 4.2 Architecture studio
**Voice:** third person plural, precise, understated. Numbers over adjectives.
<!-- copylint-off -->
**AI:** We are a forward-thinking architecture practice dedicated to creating innovative, sustainable spaces that inspire. Our holistic approach seamlessly blends form and function, resulting in timeless designs that stand as a testament to our commitment to excellence. From residential to commercial, we transform visions into reality.
<!-- copylint-on -->
**Human:** Ferro Ahmed Architects is a practice of nine people in Glasgow. We mostly work on housing, schools and the repair of old buildings. Current projects include 42 council homes in Govan and a library extension in Paisley, due on site in spring. We work in timber where we can. We don't enter unpaid competitions.

### 4.3 Band
**Voice:** short, a little funny, gig-poster direct.
<!-- copylint-off -->
**AI:** Get ready to experience the electrifying sound of The Paper Lanterns! Blending indie rock with soulful melodies, our music takes you on an unforgettable journey. Join us on tour this fall as we bring our passion to stages across the country. Don't miss out!
<!-- copylint-on -->
**Human:** The Paper Lanterns are four people from Cork who play loud songs about quiet towns. New album *Low Tide Club* is out 14 November on Rough Weather Records. We're touring Ireland and the UK in November and December. Dublin and Manchester are nearly gone. Merch ships after the tour, because we're packing it ourselves.

### 4.4 Plumber
**Voice:** plain, reassuring, numbers first.
<!-- copylint-off -->
**AI:** At FlowRight Plumbing, we pride ourselves on delivering top-quality plumbing solutions with a commitment to excellence. Our team of dedicated professionals is available 24/7 to tackle all your plumbing needs, ensuring your peace of mind. No job is too big or too small!
<!-- copylint-on -->
**Human:** Dave Okafor Plumbing & Heating. Boilers, leaks, bathrooms. Gas Safe no. 548211. We cover Leeds and 10 miles out. Boiler service is £85, and a call-out is £65 including the first half hour. We're booking about three days ahead for non-urgent jobs. If water is coming through a ceiling, turn off the stopcock (usually under the kitchen sink) and call 07700 900456.

### 4.5 Bakery
**Voice:** warm, early-morning, specific about times and flour.
<!-- copylint-off -->
**AI:** Nestled in the heart of the neighbourhood, our artisan bakery is a haven for bread lovers. Every loaf is lovingly handcrafted using time-honoured techniques and the finest ingredients, delivering an unforgettable taste experience. Discover the magic of real bread today!
<!-- copylint-on -->
**Human:** Rye & Salt, 18 Chapel Road. Open Wednesday to Sunday, 7am until we sell out (usually about 1pm on Saturdays). The country loaf is a 48-hour ferment with flour from Gilchester's in Northumberland. Order by Thursday 6pm for Saturday collection. We don't do gluten-free: our kitchen is full of flour and we'd rather not pretend.

### 4.6 Therapist
**Voice:** calm, plain, no promises. Practical information first.
<!-- copylint-off -->
**AI:** Embark on a transformative journey of healing and self-discovery. I provide a safe, compassionate space where you can explore your thoughts and feelings, empowering you to unlock your full potential and thrive. Together, we'll navigate life's challenges.
<!-- copylint-on -->
**Human:** I'm Ines Carvalho, a BACP-registered counsellor. I see adults for anxiety, grief and relationship difficulties, in person in Brighton on Tuesdays and Thursdays and online on Mondays. Sessions are 50 minutes and cost £60. I keep four places at £35 for people on low incomes. I'm currently taking new clients. If you're in crisis, call Samaritans on 116 123.

### 4.7 Food bank
**Voice:** direct, dignified, no pity language.
<!-- copylint-off -->
**AI:** Together, we're making a difference in our community! Our vibrant network of dedicated volunteers works tirelessly to combat food insecurity and empower families in need. Every donation helps us build a brighter future for all.
<!-- copylint-on -->
**Human:** Hilltop Food Bank is open Tuesdays 10am–1pm and Fridays 4–7pm at St Anne's Hall, Park Lane. You don't need a referral. Bring a bag if you can. This month we're short of tinned fish, UHT milk, deodorant and size 5 nappies. Drop donations at the hall or at the Co-op on Station Road.

### 4.8 Amateur football club
**Voice:** clubhouse noticeboard, cheerful but factual.
<!-- copylint-off -->
**AI:** Welcome to Riverside FC, where passion meets the pitch! We're a vibrant community club dedicated to fostering a love of the beautiful game for players of all ages and abilities. Join our family today and be part of something special!
<!-- copylint-on -->
**Human:** Riverside FC play in the Mid-Sussex League Division Two. Home games are at Kings Field, Saturdays at 3pm. Training is Tuesday 7pm on the 3G at Oathall. New players are welcome at any level, but bring shin pads. Subs are £15 a month, and £5 for students. Match fees go straight into the kit fund, which is why the away shirts are still from 2019.

### 4.9 Coffee roaster
**Voice:** knowledgeable, unpretentious, taste notes kept honest.
<!-- copylint-off -->
**AI:** Elevate your morning ritual with our meticulously sourced, small-batch coffees. Each bean tells a story, bringing you a symphony of rich, complex flavours from the world's finest growing regions. Experience coffee as it was meant to be.
<!-- copylint-on -->
**Human:** We roast on Tuesdays and Fridays in a 15kg Giesen in Unit 4, Hope Street, and post everything the same day. This month's filter is from the Kiruga washing station in Kenya: blackcurrant, grapefruit, a bit of tomato. We paid $6.10/kg FOB for it and publish every price we pay. Espresso subscribers get the house blend unless they ask otherwise.

### 4.10 Tattoo studio
**Voice:** friendly, blunt about rules.
<!-- copylint-off -->
**AI:** Welcome to Ink Haven, where art meets skin! Our talented artists bring your vision to life with stunning, one-of-a-kind designs crafted with precision and passion. Your journey to unforgettable body art starts here.
<!-- copylint-on -->
**Human:** Three artists, one room above the barber's on Wellgate. Mika does fine line and botanical, Ruth does traditional, and Sol's books are closed until January. We need a £50 deposit to book, which comes off the final price. You must be 18 and bring ID, no exceptions. Walk-ins for flash on the first Saturday of the month.

### 4.11 Indie SaaS
**Voice:** a developer explaining their tool to another developer.
<!-- copylint-off -->
**AI:** Supercharge your workflow with Loopline, the all-in-one platform that seamlessly streamlines team collaboration. Unlock powerful insights, boost productivity, and elevate your projects to the next level. Get started for free today!
<!-- copylint-on -->
**Human:** Loopline sends a Slack message when a scheduled job doesn't run. You add one curl line to the end of your cron job, and if we don't hear from it on time, we tell you. It's free for 20 checks. After that it's $9 a month for 500. I built it after a backup script failed silently for eleven weeks. Source for the ping client is on GitHub.

### 4.12 Dentist
**Voice:** reassuring through information, not adjectives.
<!-- copylint-off -->
**AI:** Your smile is our passion! Our state-of-the-art practice offers comprehensive dental solutions in a warm, welcoming environment. Our dedicated team is committed to providing exceptional care for the whole family.
<!-- copylint-on -->
**Human:** Moor Lane Dental is a small NHS and private practice with two dentists and one hygienist. We're accepting new NHS patients aged under 18. Adults can join our private list, where a check-up is £55. There's step-free access from the car park at the back. If you're nervous, say so when you book: we'll give you a longer first appointment and explain everything before we start.

### 4.13 Record label
**Voice:** catalogue-like, quietly proud, a bit dry.
<!-- copylint-off -->
**AI:** Rough Weather Records is a groundbreaking independent label dedicated to showcasing innovative artists who push the boundaries of sound. Our diverse roster represents the vibrant tapestry of contemporary music.
<!-- copylint-on -->
**Human:** Rough Weather is a small label in Cork, run by two people from a spare room. We've released 31 records since 2016, mostly guitar music and some things that don't fit anywhere. RW031, *Low Tide Club* by The Paper Lanterns, is out 14 November on black vinyl (500) and cassette (100). We listen to every demo but can't reply to all of them.

### 4.14 Wedding (couple's site)
**Voice:** the couple talking to friends.
<!-- copylint-off -->
**AI:** Join us as we celebrate our love story and embark on this beautiful new chapter together! We're so excited to share this magical day with our cherished friends and family.
<!-- copylint-on -->
**Human:** We're getting married on Saturday 6 June 2026 at Hebden Bridge Town Hall, ceremony at 1pm, then food and a ceilidh at the Trades Club from 4. Please RSVP by 1 April and tell us about any dietary needs. There's no parking at the Town Hall, so the train from Leeds (about 50 minutes) is the easy option. No gifts please. If you insist, there's a honeymoon fund page.

### 4.15 Small museum
**Voice:** curious, friendly and exact, like a good volunteer guide.
<!-- copylint-off -->
**AI:** Step back in time and discover the rich history of our vibrant town at the Hartley Museum. Our captivating exhibits showcase fascinating artefacts that bring the past to life, offering an unforgettable experience for visitors of all ages.
<!-- copylint-on -->
**Human:** The Hartley Museum is in the old corn exchange on Market Street. It's free, and open Thursday to Sunday, 10am–4pm. Upstairs is the town's weaving history, including a working 1890s loom we run on the first Saturday of each month. Downstairs is the café and a room of things people have donated that we can't identify yet. If you know what they are, tell us. There's a lift to both floors.

---

<!-- copylint-off -->

## 5. Demo-content rules

1. **Write as the owner, not a marketer.** First or third person, but always sounding like the person behind the counter.
2. **Names:** culturally varied and specific to the setting ("Priya, Headingley", "Tomek and Ana", "Joon"). Never "Sarah Johnson", "John Doe", "Jane Smith", "Alex Morgan" or "Emily Chen". Keep a shared names list per region in the companion plugin and don't reuse a name across themes.
3. **Places:** real-feeling street names, towns and directions ("opposite the library", "the 36 bus stops outside"). Use made-up businesses in real towns; don't invent landmarks that obviously aren't there.
4. **Numbers:** operational (prices, hours, lead times, sizes, weights, capacities). No invented social proof (customer counts, satisfaction percentages, "trusted by").
5. **Dates:** use current, plausible dates and never hard-code the copyright year (a pattern binding handles that).
6. **Imperfection:** each site needs at least one limit ("we don't do…"), one opinion, and one plain-spoken operational note.
7. **Testimonials:** full first name, context, month and year; a specific detail; no star icons; three at most per page.
8. **Placeholder brackets:** never ship `[Your Name]`-style Mad Libs (a Wikipedia-listed tell). If a field needs replacing, the demo still reads as a real business.
9. **Length:** homepage intro 40–80 words. About page 150–300 words. Product description 40–120 words. Menus have no description sentences at all.
10. **Headings and buttons:** sentence case. CTAs name the action and the result ("Book a fitting", "See this week's bake", "Call Dave").
11. **Alt text:** literal and specific. Include the medium and size for artworks.
12. **Readme and docs:** plain, second person, task-based ("To add a new menu section, …").

---

## 6. Voice sheet template (one per theme)

Every theme's `/docs/voice.md` fills this in before any demo copy is written:

```
Business: (one sentence, specific: "a two-person tattoo studio above a barber's in Dundee")
Owner(s): names, roles, one personal detail
Place: street, town, one landmark or transport note
Numbers: 5 real-feeling operational numbers (prices, hours, lead times…)
Limits: 2 things they don't do
Opinion: 1 thing they believe that a competitor might not
Voice: 3 adjectives + 1 sentence the owner would say out loud
Banned for this theme: 5 extra words that are clichés in this trade (e.g. tattoo: "ink journey", "masterpiece", "art on skin")
```

---

## 7. Machine checks (`tools/copylint.mjs`)

A small Node script runs on `patterns/*.php`, `templates/*.html`, `parts/*.html`, `styles/*.json` (titles), `readme.txt`, demo XML and all `.md` in `/research`. It fails CI on severity 5, and warns on 3–4.

| Rule | Severity | Check |
|---|---|---|
| Em dash | 5 | `--` count must be 0 |
| Spaced dash as em dash | 5 | `\s[–-]\s` between words (ignoring number ranges `\d\s?–\s?\d`) |
| Tier A words | 5 | case-insensitive word-boundary regex (list in the script) |
| Emphasis by negation (see 3.2b) | 5 shipped / 3 research | not just/only X but/it's; isn't/doesn't/don't just; it's not X(.|,) it's Y across up to two sentences; "Not X. Y." fragment pairs; no X, no Y(, just Z); zero/no + noun fragments; all the X without the Y; less X, more Y; forget X; X? Not here.; we're not your (average/typical); more than a/an + noun in headings |
| Chatbot phrases | 5 | `hope this helps`, `feel free to`, `let's dive`, `here's the thing`, `in today's`, `whether you're` |
| Placeholder brackets | 5 | `\[(Your\|Insert\|Company\|Name)[^\]]*\]` |
| Emoji | 5 | Unicode Extended_Pictographic in text content |
| Tier B words | 3 | more than 1 per 300 words |
| Tier C (GOV.UK) words | 2 | warn |
| Sentence openers | 4 | `^(Additionally\|Furthermore\|Moreover\|Ultimately\|Notably\|Importantly),` |
| Exclamation marks | 3 | more than 1 per page |
| Title Case headings | 3 | heading or button text where more than 60% of words over 3 letters are capitalised |
| Bold lead-in bullets | 4 | `<li><strong>…:</strong>` or `- **…:**` on more than 2 consecutive items |
| Sentence-length variance | 3 | coefficient of variation < 0.35 across a block of 5 or more sentences (too uniform) |
| Rule of three density | 3 | more than 2 `X, Y and Z` lists per 150 words |
| Hard-coded year | 4 | `©\s?20\d\d` in patterns |

The script ships in `research/tools/copylint.mjs` and the same list is mirrored in `ANTI-VIBE.md`'s copy section.

---

## 8. Editorial checklist (30 questions)

Answer in brackets required for release.

1. Zero em dashes in the theme and its docs? **[yes]**
2. Any spaced hyphen or en dash doing an em dash's job? **[no]**
3. Any Tier A word? **[no]**
4. Any "not just X, it's Y" or "no X, no Y, just Z"? **[no]**
5. Does any sentence start with Additionally/Furthermore/Moreover/Ultimately? **[no]**
6. Any "Whether you're…"? **[no]**
7. Any "Welcome to…" as the first words of a page? **[no]**
8. Is every heading and button in sentence case? **[yes]**
9. Does every CTA say what happens next? **[yes]**
10. Any emoji? **[no]**
11. Any bullet list where every item starts with a bold label and colon? **[no]**
12. Any invented statistic, customer count or "trusted by"? **[no]**
13. Any unnamed or initials-only testimonial ("Sarah J.")? **[no]**
14. Does the About page contain a place, a name, a number and a limit? **[yes]**
15. Does the About page contain one opinion? **[yes]**
16. Would the homepage intro still make sense on a competitor's site? **[no]**
17. Are there adjectives on the menu or price list that aren't techniques or materials? **[no]**
18. Is there a "symphony", "journey", "haven", "gem", "tapestry" or "testament" anywhere? **[no]**
19. Does any paragraph exist only to say something is important? **[no]**
20. Does the last paragraph of any page summarise the page? **[no]**
21. Are sentence lengths varied (read aloud: does it sound like a person)? **[yes]**
22. Are there more than one exclamation mark on any page? **[no]**
23. Is alt text literal (what's in the image), not evaluative ("beautiful")? **[yes]**
24. Do error, empty and 404 messages say what happened and what to do? **[yes]**
25. Any "[Your Name]"-style placeholders? **[no]**
26. Does the readme say who the theme is for in the first sentence, without adjectives? **[yes]**
27. Any "Oops", "Uh-oh" or apologetic error copy? **[no]**
28. Did `copylint` pass with zero severity-5 findings? **[yes]**
29. Did a person read the demo copy aloud once before release? **[yes]**
30. Could you name the business in one sentence, and does the copy prove it (trade words, local detail, real numbers)? **[yes]**

---

<!-- copylint-on -->

## 9. Sources

Read in full or in the relevant section:
- Wikipedia, "Signs of AI writing" (WikiProject AI Cleanup), full wikitext: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
<!-- copylint-off -->
- Kobak, González-Márquez, Horvát, Lause, "Delving into LLM-assisted writing in biomedical publications through excess vocabulary" (2024/2025): https://arxiv.org/abs/2406.07016 (full list of 291 excess style words: https://arxiv.org/html/2406.07016)
<!-- copylint-on -->
- Liang et al., "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews" (ICML 2024): https://arxiv.org/abs/2403.07183 and https://arxiv.org/html/2403.07183
- GOV.UK A to Z style guide, "Words to avoid" and sentence length: https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/
- Digital.gov plain language guide, "Writing for understanding": https://digital.gov/guides/plain-language/writing
- Mailchimp Content Style Guide, "Voice and tone": https://styleguide.mailchimp.com/voice-and-tone/
- George Orwell, "Politics and the English Language" (1946): https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/
- Anthropic, frontend-design skill (writing guidance section): https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md

Cited through the sources above, not read directly:
- The July 2026 study on em-dash rates across models (cited on the Wikipedia page, "Overuse of em dashes").
- The 2025 studies on human detection accuracy (cited on the Wikipedia page, "Caveats").

Not yet covered, but worth reading when the web search budget allows: Pangram and GPTZero public write-ups on stylometric features; essays on the "ChatGPT voice" in mainstream press; and style homogenisation studies in creative writing.
