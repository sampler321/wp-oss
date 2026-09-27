<?php
/**
 * Title: Case study: two images side by side
 * Slug: studio/case-image-pair
 * Categories: case-study
 */
?>
<!-- wp:gallery {"columns":2,"linkTo":"none","align":"wide"} -->
<figure class="wp-block-gallery alignwide has-nested-images columns-2 is-cropped"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/print-1.jpg' ) ); ?>" alt="Four matchbox labels on an orange ground, with a ship, a woman with a fan and a flower"/><figcaption class="wp-element-caption">Label set, four per box</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/pack-2.jpg' ) ); ?>" alt="Orange tin box with a hinged lid and a black printed label"/><figcaption class="wp-element-caption">The tin, kept from 1931, with the new stamp</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->
