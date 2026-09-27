<?php
/**
 * Title: Notebook with ruling selector
 * Slug: paper/ruling-selector
 * Categories: shop,featured
 * Description: The signature: links for each ruling swap the photo of the page, with spacing in millimetres and paper weight beside it.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"44%"} -->
<div class="wp-block-column" style="flex-basis:44%"><!-- wp:group {"className":"is-style-ruling-preview","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-ruling-preview"><!-- wp:image {"aspectRatio":"1","scale":"cover","sizeSlug":"large","linkDestination":"none","anchor":"ruling-dot"} -->
<figure class="wp-block-image size-large" id="ruling-dot"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/dot-grid.jpg' ) ); ?>" alt="Open dot grid notebook with a handwritten shopping list in pen and highlighter" style="aspect-ratio:1;object-fit:cover"/><figcaption class="wp-element-caption">Dot grid 5mm</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"aspectRatio":"1","scale":"cover","sizeSlug":"large","linkDestination":"none","anchor":"ruling-ruled"} -->
<figure class="wp-block-image size-large" id="ruling-ruled"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/ruled-page.jpg' ) ); ?>" alt="Ruled notebook page with pencil shavings and a yellow pencil" style="aspect-ratio:1;object-fit:cover"/><figcaption class="wp-element-caption">Ruled 7mm</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"aspectRatio":"1","scale":"cover","sizeSlug":"large","linkDestination":"none","anchor":"ruling-squared"} -->
<figure class="wp-block-image size-large" id="ruling-squared"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/graph-books.jpg' ) ); ?>" alt="Two school exercise books, green and red, on squared paper with a ruler" style="aspect-ratio:1;object-fit:cover"/><figcaption class="wp-element-caption">Squared 5mm</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"aspectRatio":"1","scale":"cover","sizeSlug":"large","linkDestination":"none","anchor":"ruling-blank"} -->
<figure class="wp-block-image size-large" id="ruling-blank"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/sketchbook.jpg' ) ); ?>" alt="An old notebook page with handwriting and pen drawings of vases" style="aspect-ratio:1;object-fit:cover"/><figcaption class="wp-element-caption">Blank</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading -->
<h2 class="wp-block-heading">A5 notebook, in four rulings</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">Choose a ruling to see the page.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"className":"is-style-hairline","style":{"spacing":{"blockGap":"var:preset|spacing|40"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group is-style-hairline"><!-- wp:paragraph -->
<p><a href="#ruling-dot">Dot grid 5mm</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="#ruling-ruled">Ruled 7mm</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="#ruling-squared">Squared 5mm</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="#ruling-blank">Blank</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:table {"className":"is-style-spec"} -->
<figure class="wp-block-table is-style-spec"><table class="has-fixed-layout"><thead><tr><th>Ruling</th><th>Spacing</th></tr></thead><tbody><tr><td>Dot grid</td><td>5mm pitch, 0.3mm dots, pale grey</td></tr><tr><td>Ruled</td><td>7mm lines, no margin</td></tr><tr><td>Squared</td><td>5mm squares</td></tr><tr><td>Blank</td><td>Nothing printed</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:table {"className":"is-style-spec"} -->
<figure class="wp-block-table is-style-spec"><table class="has-fixed-layout"><tbody><tr><td>Size</td><td>148 × 210 mm</td></tr><tr><td>Paper</td><td>100gsm cream, acid-free</td></tr><tr><td>Pages</td><td>192</td></tr><tr><td>Fountain pen friendly</td><td>Yes, no bleed with a medium nib</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Each notebook is sewn by hand in Leith, so the thread colour and the squareness of the corners vary a little from one to the next.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/product/a5-notebook-dot-grid-5mm/">Buy the dot grid</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/product/a5-notebook-ruled-7mm/">Buy the ruled</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
