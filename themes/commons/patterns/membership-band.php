<?php
/**
 * Title: Membership band with photo
 * Slug: commons/membership-band
 * Categories: call-to-action
 * Description: Image and text band pointing to the membership page.
 */
?>
<!-- wp:media-text {"align":"wide","mediaType":"image","mediaWidth":55,"className":"is-style-sage","style":{"spacing":{"margin":{"top":"var:preset|spacing|70"}}}} -->
<div class="wp-block-media-text alignwide is-stacked-on-mobile is-style-sage" style="margin-top:var(--wp--preset--spacing--70);grid-template-columns:55% auto"><figure class="wp-block-media-text__media"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/zine.jpg' ) ); ?>" alt="Engraving of a crowded print workshop, with people pulling prints and hanging sheets to dry"/></figure><div class="wp-block-media-text__content"><!-- wp:heading {"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-x-large-font-size">212 members keep the doors open</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Membership pays the rent on the gallery floor. It costs £25 a year and anyone can join. You get a wall in the members’ show, a vote, and first go at the residency.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/membership/">See what members get</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div></div>
<!-- /wp:media-text -->
