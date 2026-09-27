<?php
/**
 * Title: Product sheet: drawing and title block
 * Slug: joint/product-sheet
 * Categories: featured,shop
 * Description: The product page layout: a drawing or photo at 7/12, and the facts in a boxed title block at 5/12.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","className":"is-style-plate"} -->
<figure class="wp-block-image size-large is-style-plate"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/chair-2.jpg' ) ); ?>" alt="Watercolour drawing of a spindle-back chair in pale wood with a saddle seat"/><figcaption class="wp-element-caption">Calder chair, drawn at 1:5 before the first one was made</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label">Chairs</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-xx-large-font-size">Calder chair</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A spindle-back dining chair with a carved saddle seat. Seven spindles, steam-bent back rail, no screws or metal anywhere.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"className":"is-style-title-block","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-title-block"><!-- wp:table -->
<figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr><td>Timber</td><td>English oak, cherry or elm</td></tr><tr><td>W / D / H</td><td>480 / 520 / 800 mm<br>18.9 / 20.5 / 31.5 in</td></tr><tr><td>Seat height</td><td>450 mm, 17.7 in</td></tr><tr><td>Finish</td><td>Hardwax oil or soap</td></tr><tr><td>Lead time</td><td>Made to order, 8 to 10 weeks</td></tr></tbody></table></figure>
<!-- /wp:table --></div>
<!-- /wp:group -->

<!-- wp:pattern {"slug":"joint/timber-prices"} /-->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/shop/">Order a Calder chair</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/commission/">Ask about another size</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
