<?php
/**
 * Title: Hero: headline over a photo collage
 * Slug: booth/hero-collage
 * Categories: featured
 * Description: One very large headline with three photos behind it. Swap in your own rooms.
 */
?>
<!-- wp:group {"align":"wide","className":"is-style-collage","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide is-style-collage"><!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">A big room for bands who want to play together</h1>
<!-- /wp:heading -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/console.jpg' ) ); ?>" alt="The Studio A control room: a large console, five speakers on stands and acoustic panels on the walls"/></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drums.jpg' ) ); ?>" alt="A four-piece drum kit seen from above, with cymbals on stands"/></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/vocal.jpg' ) ); ?>" alt="A black and white photo of a large-diaphragm microphone with a pop filter"/></figure>
<!-- /wp:image --></div>
<!-- /wp:group -->
