<?php
/**
 * Title: Featured zine
 * Slug: drum/featured-zine
 * Categories: drum-shop,shop
 */
?>
<!-- wp:columns {"verticalAlignment":"center","align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/zine-rack.jpg' ) ); ?>" alt="A library wall rack full of colourful zines under a paper banner reading zines"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"is-style-sticker"} -->
<p class="is-style-sticker">Zine of the month</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"fontSize":"x-large"} -->
<h3 class="wp-block-heading has-x-large-font-size">Salt Water, issue 7</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Thirty-two pages of swimming stories from the Irish Sea, printed in blue and fluorescent pink on cream paper. Edition of 500.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"has-x-large-font-size","style":{"typography":{"fontWeight":"800"}},"fontSize":"x-large"} -->
<p class="has-x-large-font-size" style="font-weight:800">£6</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/shop/">See it in the shop</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
