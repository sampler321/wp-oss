<?php
/**
 * Title: Work page: gallery and info
 * Slug: seed/work-page
 * Categories: seed-works,portfolio
 * Description: A full work page: tabs, the numbered outputs, then the Info section.
 * Post Types: post
 */
?>
<!-- wp:paragraph {"className":"is-style-tabs"} -->
<p class="is-style-tabs"><a href="#gallery">Gallery</a> / <a href="#info">Info</a></p>
<!-- /wp:paragraph -->

<!-- wp:group {"align":"wide","className":"is-style-sheet","layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"9rem"},"anchor":"gallery"} -->
<div class="wp-block-group alignwide is-style-sheet" id="gallery"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-725.jpg' ) ); ?>" alt="Drift output 725, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 725</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-680.jpg' ) ); ?>" alt="Drift output 680, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 680</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-529.jpg' ) ); ?>" alt="Drift output 529, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 529</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-412.jpg' ) ); ?>" alt="Drift output 412, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 412</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-301.jpg' ) ); ?>" alt="Drift output 301, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 301</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-118.jpg' ) ); ?>" alt="Drift output 118, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 118</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-77.jpg' ) ); ?>" alt="Drift output 77, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 77</figcaption></figure>
<!-- /wp:image -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/drift-12.jpg' ) ); ?>" alt="Drift output 12, flow lines in black and red on off-white paper"/><figcaption class="wp-element-caption">No. 12</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-rule-top","layout":{"type":"constrained"},"anchor":"info"} -->
<div id="info" class="wp-block-group is-style-rule-top"><!-- wp:heading {"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-x-large-font-size">Info</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">Thousands of short lines follow a field of slow waves until they run out of room. Every output uses the same code and a different seed, so no two have the same knots.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","orientation":"vertical","justifyContent":"stretch"}} -->
<div class="wp-block-group"><!-- wp:group {"className":"is-style-rule-bottom","style":{"spacing":{"blockGap":"var:preset|spacing|30","padding":{"bottom":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group is-style-rule-bottom" style="padding-bottom:var(--wp--preset--spacing--20)"><!-- wp:paragraph {"textColor":"muted"} -->
<p class="has-muted-color has-text-color">Edition</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>512 outputs, all minted</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-rule-bottom","style":{"spacing":{"blockGap":"var:preset|spacing|30","padding":{"bottom":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group is-style-rule-bottom" style="padding-bottom:var(--wp--preset--spacing--20)"><!-- wp:paragraph {"textColor":"muted"} -->
<p class="has-muted-color has-text-color">Released</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>14 March 2026</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-rule-bottom","style":{"spacing":{"blockGap":"var:preset|spacing|30","padding":{"bottom":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group is-style-rule-bottom" style="padding-bottom:var(--wp--preset--spacing--20)"><!-- wp:paragraph {"textColor":"muted"} -->
<p class="has-muted-color has-text-color">Platform</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://example.com/drift">Drift on the project page</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-rule-bottom","style":{"spacing":{"blockGap":"var:preset|spacing|30","padding":{"bottom":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group is-style-rule-bottom" style="padding-bottom:var(--wp--preset--spacing--20)"><!-- wp:paragraph {"textColor":"muted"} -->
<p class="has-muted-color has-text-color">Code</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>p5.js, 190 lines</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-rule-bottom","style":{"spacing":{"blockGap":"var:preset|spacing|30","padding":{"bottom":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group is-style-rule-bottom" style="padding-bottom:var(--wp--preset--spacing--20)"><!-- wp:paragraph {"textColor":"muted"} -->
<p class="has-muted-color has-text-color">Sketch</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://example.com/drift/live">Run the sketch</a> (starts only when you press play)</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
