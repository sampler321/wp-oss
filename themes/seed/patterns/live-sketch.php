<?php
/**
 * Title: Live sketch with still fallback
 * Slug: seed/live-sketch
 * Categories: seed-works,media
 * Description: A still image with a link to the running sketch. Nothing animates on this site until a visitor asks for it.
 */
?>
<!-- wp:group {"className":"is-style-sheet-grey","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-sheet-grey"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-529.jpg' ) ); ?>" alt="Still of Drift output 529: black flow lines with a few red strands on off-white paper"/><figcaption class="wp-element-caption">Still from the live sketch, seed 529</figcaption></figure>
<!-- /wp:image -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|40"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://example.com/drift/live">Run the sketch</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">Opens the sketch on its own page. It never starts by itself, and it stops when you leave the tab.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
