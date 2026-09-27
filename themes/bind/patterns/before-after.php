<?php
/**
 * Title: Before and after pair with side-note
 * Slug: bind/before-after
 * Categories: featured,bind-cases
 * Description: Two photos at the same 4:5 crop, side by side, with the job details in the outer margin.
 */
?>
<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:columns {"align":"wide","className":"is-style-pair","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns alignwide is-style-pair"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/damaged.jpg' ) ); ?>" alt="Worn brown calf binding with a split spine, rubbed corners and a paper shelf label, a ruler along the right edge"/><figcaption class="wp-element-caption">Before: calf, spine split, both joints gone</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/restored.jpg' ) ); ?>" alt="Brown calf binding with tooled borders and a sound spine, photographed flat with a ruler below"/><figcaption class="wp-element-caption">After: rebacked, original boards and label kept</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"20%"} -->
<div class="wp-block-column" style="flex-basis:20%"><!-- wp:group {"className":"is-style-sidenote","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-sidenote"><!-- wp:heading {"level":6} -->
<h6 class="wp-block-heading">Case 41</h6>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Sermons, Venice 1492. Owned by a parish in Nowy Sącz.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Rebacked in dyed calf. Joints lined with Japanese tissue. Wheat starch paste only.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>31 bench hours, spread over five weeks while the paste dried.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="/case-studies/">All case studies</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
