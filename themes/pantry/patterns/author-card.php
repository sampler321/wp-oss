<?php
/**
 * Title: Author card (short bio)
 * Slug: pantry/author-card
 * Categories: about
 */
?>
<!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"className":"is-style-rule-top"} -->
<div class="wp-block-columns is-style-rule-top"><!-- wp:column {"width":"96px"} -->
<div class="wp-block-column" style="flex-basis:96px"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","className":"is-style-round","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large is-style-round"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/herbs.jpg' ) ); ?>" alt="Bunches of fresh herbs"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Hana Qasem</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Cook and writer in Walthamstow. Two books, one small kitchen, a recipe every Thursday since 2016.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/about/">More about Hana</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
