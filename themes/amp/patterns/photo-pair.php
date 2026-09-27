<?php
/**
 * Title: Two photos side by side
 * Slug: amp/photo-pair
 * Categories: gallery
 */
?>
<!-- wp:gallery {"columns":2,"linkTo":"none","align":"wide"} -->
<figure class="wp-block-gallery alignwide has-nested-images columns-2 is-cropped"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/venue-1.jpg' ) ); ?>" alt="A three-piece band playing on a small stage with fairy lights and a painted sign behind them"/></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/live-3.jpg' ) ); ?>" alt="Someone crowd-surfing over raised hands in front of a lit stage"/></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->
