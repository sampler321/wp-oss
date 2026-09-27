<?php
/**
 * Title: Hero: this week in Eindhoven
 * Slug: cityguide/hero-this-week
 * Categories: featured
 * Description: Full-bleed photo with the week in the headline. Swap the image for this week's best photo.
 */
?>
<!-- wp:group {"align":"full","className":"is-style-photo-hero","style":{"spacing":{"padding":{"top":"var:preset|spacing|80","bottom":"var:preset|spacing|60","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}} -->
<div class="wp-block-group alignfull is-style-photo-hero" style="padding-top:var(--wp--preset--spacing--80);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--60);padding-left:var(--wp--preset--spacing--40)"><!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/dynamo.jpg' ) ); ?>" alt="A band on a dark stage under white spotlights, with the crowd in silhouette in front"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":1,"textColor":"base","fontSize":"display"} -->
<h1 class="wp-block-heading has-base-color has-text-color has-display-font-size">What's on in Eindhoven, 28 September to 4 October</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"base","fontSize":"large"} -->
<p class="has-base-color has-text-color has-large-font-size">Picked by Sanne and Joost, updated every Monday morning. Gigs, markets, openings and one very good soup.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/this-week/">See the whole week</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
