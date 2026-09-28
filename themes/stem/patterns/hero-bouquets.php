<?php
/**
 * Title: Hero: today's bouquets
 * Slug: stem/hero-bouquets
 * Categories: featured,banner
 * Description: An alternative opening: today's three sizes with the cut-off.
 */
?>
<!-- wp:group {"className":"is-style-marigold","align":"full","layout":{"type":"constrained","contentSize":"1360px"}} -->
<div class="wp-block-group alignfull is-style-marigold"><!-- wp:heading {"level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-xx-large-font-size">Today's bouquets</h1>
<!-- /wp:heading -->

<!-- wp:gallery {"columns":3,"linkTo":"none","align":"wide"} -->
<figure class="wp-block-gallery has-nested-images columns-3 is-cropped alignwide"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/posy.jpg' ) ); ?>" alt="A small posy of roses, yarrow and wildflowers held against a white top"/><figcaption class="wp-element-caption">Small, £40</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/roses-held.jpg' ) ); ?>" alt="A bouquet of cream and orange roses held in front of a dark red dress"/><figcaption class="wp-element-caption">Medium, £60</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/gerbera-mint.jpg' ) ); ?>" alt="Pink gerberas and berries in a glass jar against a mint green wall"/><figcaption class="wp-element-caption">Large, £85</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery -->

<!-- wp:paragraph {"className":"is-style-cutoff"} -->
<p class="is-style-cutoff">Order by 2pm for same-day delivery in E5, E8, E9, N16 and N4. Next day everywhere else in the UK.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
