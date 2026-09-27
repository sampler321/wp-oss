<?php
/**
 * Title: Before and after screens
 * Slug: case/before-after
 * Categories: gallery
 * Description: Two screens side by side with a label and a caption that says what changed in words.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"is-style-tag"} -->
<p class="is-style-tag">Before</p>
<!-- /wp:paragraph -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","className":"is-style-framed"} -->
<figure class="wp-block-image size-large is-style-framed"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/kiosk.jpg' ) ); ?>" alt="A ticket machine touchscreen showing a grid of fare prices in red and blue buttons"/><figcaption class="wp-element-caption">Fare grid first. You had to pick a price before a place.</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"is-style-tag"} -->
<p class="is-style-tag">After</p>
<!-- /wp:paragraph -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","className":"is-style-framed"} -->
<figure class="wp-block-image size-large is-style-framed"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/kiosk-3.jpg' ) ); ?>" alt="A blue and yellow ticket machine on a station platform, with a route map on its touchscreen and a card reader below"/><figcaption class="wp-element-caption">Destination first, with the map and a search box. Price comes last, railcard next to it.</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">What changed: the order of the questions. The visual design barely moved, because the operator’s brand rules fix the colours and the type on the machines.</p>
<!-- /wp:paragraph -->
