<?php
/**
 * Title: Shop intro with photo
 * Slug: thrift/intro-split
 * Categories: about,featured
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading -->
<h2 class="wp-block-heading">Second Floor Vintage</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>One-off clothes from the 1940s to the early 2000s, up two flights of stairs on Oldham Street. Aoife buys the workwear and military, Kwame buys womenswear and anything with embroidery.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Every piece is washed, mended where it can be, and measured flat. We list the label size because it is on the label, and ignore it when we tell you what fits.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/shop/">See this week's rail</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:image {"lightbox":{"enabled":true},"aspectRatio":"3/2","scale":"cover","sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/shop-rails.jpg' ) ); ?>" alt="Rails of shirts and jackets in a bright shop with hanging lamps" style="aspect-ratio:3/2;object-fit:cover"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
