<?php
/**
 * Title: Case study: before and after
 * Slug: case/cs-before-after
 * Categories: case-study
 */
?>
<!-- wp:heading {"level":3,"anchor":"before-after"} -->
<h3 id="before-after" class="wp-block-heading">Before and after</h3>
<!-- /wp:heading -->

<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"is-style-tag"} -->
<p class="is-style-tag">Before</p>
<!-- /wp:paragraph -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","className":"is-style-framed"} -->
<figure class="wp-block-image size-large is-style-framed"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/ui-kiosk-before.jpg' ) ); ?>" alt="Old ticket machine screen: a grid of twelve fare zone buttons, with the railcard question below"/><figcaption class="wp-element-caption">Fare grid first. You had to pick a zone before a place.</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"is-style-tag"} -->
<p class="is-style-tag">After</p>
<!-- /wp:paragraph -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","className":"is-style-framed"} -->
<figure class="wp-block-image size-large is-style-framed"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/ui-kiosk-after.jpg' ) ); ?>" alt="New ticket machine screen: a search box, then a list of nearby stations with journey times, Partick highlighted"/><figcaption class="wp-element-caption">Destination first, with the nearest stations listed.</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><strong>What changed:</strong> the order of the questions. The visual design barely moved, because the brand rules fix colours and type on the machines.</p>
<!-- /wp:paragraph -->
