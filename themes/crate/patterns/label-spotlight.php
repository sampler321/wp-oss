<?php
/**
 * Title: Label spotlight
 * Slug: crate/label-spotlight
 * Categories: shop,featured
 * Description: One label, a paragraph about it, and photos you can open large.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:heading -->
<h2 class="wp-block-heading">Label: Impulse!</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p class="">Orange and black spines, Van Gelder in the run-out, gatefolds that open like a book. We keep a whole divider for them and price the originals on condition, not hype.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label"><a href="/?s=impulse&amp;post_type=product">Every Impulse! record in stock</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:gallery {"columns":2,"linkTo":"none"} -->
<figure class="wp-block-gallery has-nested-images columns-2 is-cropped"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/spinning.jpg' ) ); ?>" alt="A black LP with a teal label turning on a dark turntable, seen from above"/><figcaption class="wp-element-caption">Alice Coltrane</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/stack.jpg' ) ); ?>" alt="A tall stack of LPs on their sides, spines showing catalogue numbers"/><figcaption class="wp-element-caption">The Impulse! divider</figcaption></figure>
<!-- /wp:image --></figure>
<!-- /wp:gallery --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
