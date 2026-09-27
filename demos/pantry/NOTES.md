# Pantry (Hana Qasem)

- Direction: the owner asked for something like ottolenghi.co.uk or mob.co.uk. Mob gives the heavy extended headline type, the lime panel and the soft 18 to 28px corners; Ottolenghi gives white pages, big food photos and a pomegranate red. The result is loud and hungry, where the researched "index card" look was quiet.
- Fonts: Mona Sans (display, 800 to 900 weight at 125% width via font-stretch in theme.json CSS, narrowed to 108% under 600px) and Figtree (body). Mona Sans is claimed in demos/pantry/fonts-claim.txt. No monospace.
- Palette: white plate, burnt #16140F, pomegranate #C8102E, herb #1E6B52, lime #E9F0A6, saffron #F4C542. Variations: Diner, Test kitchen, Larder.
- Signature: the recipe card (is-style-recipe-card) anchored as #recipe, reached by the "Jump to recipe" button in the single template. It has a four-cell facts strip, ingredients with grams first and cups in brackets, big red numbered steps (is-style-steps), then a scaling table, make-ahead notes and swaps in Details blocks. Print CSS hides the header, footer, photos and related recipes.
- Core-block limits: there is no live servings slider or US/metric toggle, so the scaling table (2, 4 and 6 servings) and dual units stand in for them. Times and servings are written into the excerpt so they show on cards.
- Recipes are posts; courses are categories, diets and ingredients are tags (the "What's in your fridge?" chips are a Tag Cloud).
