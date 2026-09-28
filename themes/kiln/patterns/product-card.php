<?php
/**
 * Title: Pot card (sold out, dimmed)
 * Slug: kiln/product-card
 * Categories: kiln-pots,shop
 * Description: A square photo, name and price. Sold pots keep their card and the photo is dimmed.
 */
?>
<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"className":"is-style-sold-out","layout":{"type":"flex","orientation":"vertical"}} -->
<div class="wp-block-group is-style-sold-out"><!-- wp:image {"sizeSlug":"large","linkDestination":"custom","className":"is-style-square"} -->
<figure class="wp-block-image size-large is-style-square"><a href="/shop/"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/tea-bowl.jpg' ) ); ?>" alt="A wide conical tea bowl in dark brown glaze with rust streaks and a pale foot ring"/></a></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3,"fontSize":"medium","fontFamily":"body","style":{"typography":{"fontWeight":"600","letterSpacing":"0"}}} -->
<h3 class="wp-block-heading has-medium-font-size has-body-font-family"><a href="/shop/">Tenmoku tea bowl</a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"is-style-price"} -->
<p class="is-style-price">£85, sold out</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
