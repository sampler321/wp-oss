<?php
/**
 * Title: This week's filter (front page label)
 * Slug: roast/this-weeks-filter
 * Categories: featured
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"},"padding":{"bottom":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide" style="padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:column {"width":"62%"} -->
<div class="wp-block-column" style="flex-basis:62%"><!-- wp:paragraph {"className":"has-small-font-size","style":{"typography":{"fontWeight":"800"}},"fontSize":"small"} -->
<p class="has-small-font-size" style="font-weight:800">This week's filter</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"roast/coffee-label"} /--></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/v60.jpg' ) ); ?>" alt="Water poured from a copper kettle into a pour-over dripper on a white table"/><figcaption class="wp-element-caption">Kiruga through a V60, 15g to 250g.</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/v60-15g-to-250g/">The V60 recipe we use for it</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
