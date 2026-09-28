<?php
/**
 * Title: Representing gallery
 * Slug: oil/gallery-card
 * Categories: oil-exhibitions,featured
 */
?>
<!-- wp:columns {"align":"wide","verticalAlignment":"center","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/j-leith.jpg' ) ); ?>" alt="A two-storey stone and white-rendered corner building on a sunny street"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Fairlie Gallery</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p class="">14 Dundas Street, Edinburgh EH3 6HZ. Tuesday to Saturday, 10am to 5pm. Morag Fairlie has shown my work since 2017 and handles loans and exhibitions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p class=""><a href="mailto:hello@example.com">hello@example.com</a>, 0131 496 0990</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
