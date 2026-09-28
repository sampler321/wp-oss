<?php
/**
 * Title: Photos of the actual copy (front, back, label)
 * Slug: crate/copy-photos
 * Categories: shop,gallery
 * Description: Three photos of the copy you will get. Replace them with your own; shoot them flat and square.
 */
?>
<!-- wp:gallery {"columns":3,"linkTo":"none","align":"wide"} -->
<figure class="wp-block-gallery has-nested-images columns-3 is-cropped alignwide"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/spinning.jpg' ) ); ?>" alt="The record itself on the platter, teal label showing"/><figcaption class="wp-element-caption">Label</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/stack.jpg' ) ); ?>" alt="The copy in a stack of Impulse! LPs, spine showing"/><figcaption class="wp-element-caption">Spine</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/sleeve-hands.jpg' ) ); ?>" alt="The front sleeve held above the turntable"/><figcaption class="wp-element-caption">Sleeve</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->
