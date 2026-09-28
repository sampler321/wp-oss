<?php
/**
 * Title: Recent jobs in photos
 * Slug: pipe/job-photos
 * Categories: about
 */
?>
<!-- wp:columns {"align":"wide","className":"is-style-index-row"} -->
<div class="wp-block-columns alignwide is-style-index-row"><!-- wp:column {"width":"25%"} -->
<div class="wp-block-column" style="flex-basis:25%"><!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label">Recent jobs</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:gallery {"columns":4,"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-4 is-cropped"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/manifold.jpg' ) ); ?>" alt="A brass underfloor manifold with thermal actuators"/><figcaption class="wp-element-caption">Manifold, Crookes</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/cylinder.jpg' ) ); ?>" alt="A white hot water cylinder on a tiled wall"/><figcaption class="wp-element-caption">Old cylinder out, Broomhill</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/radiator.jpg' ) ); ?>" alt="A white panel radiator with a thermostatic valve"/><figcaption class="wp-element-caption">New radiator and TRV, Walkley</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/gauge.jpg' ) ); ?>" alt="An old pressure gauge on a stand"/><figcaption class="wp-element-caption">Not ours, but we like it</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
