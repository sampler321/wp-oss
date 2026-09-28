<?php
/**
 * Title: Editorial feature (big photo, short text)
 * Slug: crate/editorial-feature
 * Categories: featured,gallery
 */
?>
<!-- wp:columns {"align":"full","verticalAlignment":"bottom","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|30"}}}} -->
<div class="wp-block-columns alignfull"><!-- wp:column {"width":"66.66%"} -->
<div class="wp-block-column" style="flex-basis:66.66%"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","aspectRatio":"3/2","scale":"cover","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/digging.jpg' ) ); ?>" alt="A woman flicking through a crate of records by a shop window" style="aspect-ratio:3/2;object-fit:cover"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading -->
<h2 class="wp-block-heading">Saturday, 11am</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p class="">The first hour on a Saturday is the diggers' hour: new used stock goes out at 11, and the regulars know it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label"><a href="/latest-arrivals/">What went out this week</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
