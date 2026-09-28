<?php
/**
 * Title: Before and after (two photos)
 * Slug: coat/before-after
 * Categories: portfolio,gallery
 * Description: Two images side by side with Before and After captions. Swap in your own photos taken from the same spot.
 */
?>
<!-- wp:columns {"align":"wide"} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/bedroom.jpg' ) ); ?>" alt="Watercolour of a pale 1820s bedroom with a four-poster bed and a chest of drawers"/><figcaption class="wp-element-caption">Before: pale, polite and a bit tired</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/decorator.jpg' ) ); ?>" alt="A room painted deep orange with black panels, wicker chairs and a desk"/><figcaption class="wp-element-caption">After: Charlotte's Locks with Railings panels</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
