<?php
/**
 * Title: Hero: latest mix on a full image
 * Slug: bpm/hero-latest-mix
 * Categories: featured,query
 * Description: The newest mix fills the left, with its tags on a black plate. Dates sit on the right.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"66%"} -->
<div class="wp-block-column" style="flex-basis:66%"><!-- wp:query {"queryId":21,"query":{"perPage":1,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:cover {"useFeaturedImage":true,"dimRatio":20,"overlayColor":"base","isUserOverlayColor":true,"minHeight":72,"minHeightUnit":"vh","contentPosition":"bottom left"} -->
<div class="wp-block-cover has-custom-content-position is-position-bottom-left" style="min-height:72vh"><span aria-hidden="true" class="wp-block-cover__background has-base-background-color has-background-dim-20 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:group {"className":"is-style-plate","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-plate"><!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:post-terms {"term":"category","className":"is-style-tag-boxes"} /-->

<!-- wp:post-date {"format":"j M Y"} /--></div>
<!-- /wp:group -->

<!-- wp:post-title {"level":2,"isLink":true,"fontSize":"xx-large"} /-->

<!-- wp:post-terms {"term":"post_tag","className":"is-style-tag-boxes"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":30} /--></div>
<!-- /wp:group --></div></div>
<!-- /wp:cover -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Coming up</h4>
<!-- /wp:heading -->

<!-- wp:pattern {"slug":"bpm/dates-compact"} /-->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/dates/">All dates</a></p>
<!-- /wp:paragraph -->

<!-- wp:group {"className":"is-style-boxed","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-boxed"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Szum 058 is up</h4>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Two hours with Kaja Ptak: Polish jazz on 45, broken beat, one Komeda edit that took three weeks to get right.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/mixes/">Play the latest mix</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
