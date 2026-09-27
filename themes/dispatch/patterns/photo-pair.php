<?php
/**
 * Title: Two photos side by side
 * Slug: dispatch/photo-pair
 * Categories: media,gallery
 */
?>
<!-- wp:gallery {"columns":2,"linkTo":"none","align":"wide","className":"is-style-photo"} -->
<figure class="wp-block-gallery alignwide has-nested-images columns-2 is-cropped is-style-photo"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/parliament.jpg' ) ); ?>" alt="The European Parliament hemicycle in Brussels, seen from the public gallery"/><figcaption class="wp-element-caption">The hemicycle before the vote.</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/mast.jpg' ) ); ?>" alt="A phone mast on a steel pole beside a fenced building site under a blue sky"/><figcaption class="wp-element-caption">The “temporary” mast in Mechelen.</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->
