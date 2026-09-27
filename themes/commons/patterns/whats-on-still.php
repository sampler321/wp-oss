<?php
/**
 * Title: What's on: photo with an overlapping label
 * Slug: commons/whats-on-still
 * Categories: featured
 * Description: A fixed version of the current show for any page: a wide photo with the label card overlapping its bottom edge.
 */
?>
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","align":"full","className":"is-style-crop-wide"} -->
<figure class="wp-block-image alignfull size-large is-style-crop-wide"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/hero.jpg' ) ); ?>" alt="A narrow gallery corridor with a wooden partition wall, a photograph in a cut-out window and drawings on white cloth to the left"/></figure>
<!-- /wp:image -->

<!-- wp:group {"align":"wide","className":"is-style-overlap-card","layout":{"type":"constrained","contentSize":"30rem","justifyContent":"left"}} -->
<div class="wp-block-group alignwide is-style-overlap-card"><!-- wp:paragraph {"className":"is-style-running-number"} -->
<p class="is-style-running-number">No. 184</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"fontSize":"xx-large"} -->
<h2 class="wp-block-heading has-xx-large-font-size">Soft borders</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Hana Mirza and Ciarán Doyle. 12 September to 25 October 2026.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"x-small"} -->
<p class="has-x-small-font-size">Thursday to Sunday, 12 to 6pm. Free, no booking.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/soft-borders/">Read about the show</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
