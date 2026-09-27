<?php
/**
 * Title: Lead film: still with an overlapping card, and news beside it
 * Slug: reel/lead-film
 * Categories: featured
 */
?>
<!-- wp:columns {"className":"alignwide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|40"},"padding":{"top":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide" style="padding-top:var(--wp--preset--spacing--50)"><!-- wp:column {"width":"72%"} -->
<div class="wp-block-column" style="flex-basis:72%"><!-- wp:group {"style":{"spacing":{"blockGap":"0"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:image {"lightbox":{"enabled":true},"aspectRatio":"16/10","scale":"cover","sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/still-9.jpg' ) ); ?>" alt="Inside a long old glasshouse with a tiled floor, rocks and plants" style="aspect-ratio:16/10;object-fit:cover"/></figure>
<!-- /wp:image -->

<!-- wp:group {"className":"is-style-overlap-card","style":{"spacing":{"blockGap":"var:preset|spacing|30"}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-overlap-card"><!-- wp:heading {"level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-xx-large-font-size">Glasland</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Every tomato in a Dutch supermarket in February was picked by someone who lives in a caravan behind a greenhouse. Noor Verbeek spent two winters in the Westland with four of them.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/screenings/">Dates and tickets</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"28%"} -->
<div class="wp-block-column" style="flex-basis:28%"><!-- wp:pattern {"slug":"reel/news-cards"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
