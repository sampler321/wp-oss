<?php
/**
 * Title: Hero: red cover with a deck
 * Slug: deck/hero-red
 * Categories: banner
 * Description: An alternative hero for a page or a drop: red field, ransom headline, one photo.
 */
?>
<!-- wp:columns {"verticalAlignment":"center","align":"full","className":"is-style-red"} -->
<div class="wp-block-columns alignfull are-vertically-aligned-center is-style-red"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":1,"className":"is-style-ransom","fontSize":"xx-large"} -->
<h1 class="wp-block-heading is-style-ransom has-xx-large-font-size"><mark>Fresh</mark> shop <strong>decks</strong></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">8.0, 8.25 and 8.5. Free grip. Fitted while you wait.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/product-category/decks/">See the decks</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"lightbox":{"enabled":true},"aspectRatio":"4/3","scale":"cover","sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/deck-wall.jpg' ) ); ?>" alt="A stack of brightly painted skateboard decks with cartoon graphics" style="aspect-ratio:4/3;object-fit:cover"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
