<?php
/**
 * Title: Recipe mosaic
 * Slug: larder/recipe-mosaic
 * Categories: posts,query
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:query {"queryId":2,"query":{"perPage":10,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-mosaic","layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"12rem"}} -->
<!-- wp:cover {"useFeaturedImage":true,"dimRatio":0,"minHeight":260,"minHeightUnit":"px","contentPosition":"bottom left","isDark":false} -->
<div class="wp-block-cover is-light has-custom-content-position is-position-bottom-left" style="min-height:260px"><span aria-hidden="true" class="wp-block-cover__background has-background-dim-0 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:post-title {"isLink":true,"level":3} /--></div></div>
<!-- /wp:cover -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing cooked here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->

<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/recipes/">See all the recipes</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group -->
