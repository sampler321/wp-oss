<?php
/**
 * Title: Job details gallery (lightbox)
 * Slug: coat/job-gallery
 * Categories: gallery
 * Description: Three detail photos from one job. Click any to see it large.
 */
?>
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Close up</h3>
<!-- /wp:heading -->

<!-- wp:gallery {"columns":3,"linkTo":"none","align":"wide"} -->
<figure class="wp-block-gallery alignwide has-nested-images columns-3 is-cropped"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/brush.jpg' ) ); ?>" alt="A worn paintbrush with white paint on the bristles held against a pale wall"/><figcaption class="wp-element-caption">Cutting in by hand</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/frontdoor.jpg' ) ); ?>" alt="A green six-panel front door with a brass knocker between white columns"/><figcaption class="wp-element-caption">Laid-off eggshell, no brush marks</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/sash.jpg' ) ); ?>" alt="A white sash window with dark green sills in a cream wall"/><figcaption class="wp-element-caption">Oil paint on an old sash</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->
