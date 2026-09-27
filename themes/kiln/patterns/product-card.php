<?php
/**
 * Title: Pot card (sold out, dimmed)
 * Slug: kiln/product-card
 * Categories: shop
 * Description: A square photo, name and price. Sold pots keep their card and the photo is dimmed.
 */
?>
<!-- wp:group {"className":"is-style-sold-out","style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","orientation":"vertical"}} -->
<div class="wp-block-group is-style-sold-out"><!-- wp:image {"sizeSlug":"large","linkDestination":"custom","className":"is-style-square"} -->
<figure class="wp-block-image size-large is-style-square"><a href="/shop/"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/tea-bowl.jpg' ) ); ?>" alt="A wide conical tea bowl in dark brown glaze with rust streaks and a pale foot ring"/></a></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3,"className":"wp-block-heading has-medium-font-size has-body-font-family","style":{"typography":{"fontWeight":"600","letterSpacing":"0"}}} -->
<h3 class="wp-block-heading has-medium-font-size has-body-font-family" style="font-weight:600;letter-spacing:0"><a href="/shop/">Tenmoku tea bowl</a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"is-style-price"} -->
<p class="is-style-price">£85, sold out</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
