<?php
/**
 * Title: Hero: full-bleed photo with the wordmark
 * Slug: crate/hero-wordmark
 * Categories: featured,banner
 * Description: The home hero: one photograph, the shop name as big as the screen allows, and three small lines.
 */
?>
<!-- wp:image {"sizeSlug":"large","linkDestination":"none","align":"full","className":"crate-hero"} -->
<figure class="wp-block-image alignfull size-large crate-hero"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/hero.jpg' ) ); ?>" alt="A black LP playing on a white turntable, the tone arm in the groove"/></figure>
<!-- /wp:image -->

<!-- wp:site-title {"isLink":false,"className":"is-style-wordmark crate-pull"} /-->

<!-- wp:group {"align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|20","bottom":"var:preset|spacing|20","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignfull" style="padding-top:var(--wp--preset--spacing--20);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--20);padding-left:var(--wp--preset--spacing--30)"><!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label">Used and new records, graded by ear</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label"><a href="/latest-arrivals/">Latest 100 arrivals</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"is-style-label"} -->
<p class="is-style-label">Call Lane, Leeds. Open today 11 to 7</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
