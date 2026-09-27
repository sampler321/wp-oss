<?php
/**
 * Title: Cookbook promo
 * Slug: pantry/cookbook-promo
 * Categories: featured,shop
 */
?>
<!-- wp:columns {"verticalAlignment":"center","align":"wide","className":"is-style-saffron","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"},"margin":{"top":"var:preset|spacing|70"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-center is-style-saffron" style="margin-top:var(--wp--preset--spacing--70)"><!-- wp:column {"width":"45%"} -->
<div class="wp-block-column" style="flex-basis:45%"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/flatbread.jpg' ) ); ?>" alt="Hummus topped with falafel and pickled carrot, with flatbread in a basket behind"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size">One Tray, Most Nights</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>My second book is 80 traybakes that go in the oven at 200°C and come out as dinner. Out 2 October from Kestrel Press, 288 pages, £26.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Independent shops get signed bookplates while they last. I'll sign anything you bring to an event, including the first book.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://uk.bookshop.org/">Buy from Bookshop.org</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/cookbooks/">Where I'm signing</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
