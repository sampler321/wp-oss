<?php
/**
 * Title: Object: drawing first, then name and price
 * Slug: joint/obj-hero
 * Categories: object
 * Description: The object opens with the drawing or photo at full width. Name, price and actions follow.
 */
?>
<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","align":"wide","className":"is-style-plate"} -->
<figure class="wp-block-image alignwide size-large is-style-plate"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/chair-2.jpg' ) ); ?>" alt="Watercolour drawing of a spindle-back chair in pale wood with a saddle seat"/><figcaption class="wp-element-caption">Calder chair, drawn at 1:5 before the first one was made</figcaption></figure>
<!-- /wp:image -->

<!-- wp:columns {"verticalAlignment":"bottom","align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide are-vertically-aligned-bottom"><!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label">Chair</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-xx-large-font-size">Calder chair</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">A spindle-back dining chair with a carved saddle seat. Seven spindles, a steam-bent back rail, no screws or metal anywhere.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"fontSize":"x-large","fontFamily":"display"} -->
<p class="has-display-font-family has-x-large-font-size">From £1,450</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/shop/">Buy or order it</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/commission/">Ask for another size</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:group {"className":"is-style-lead-time","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-lead-time"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Ten-year guarantee on every joint. Delivery by our own van within 60 miles.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
