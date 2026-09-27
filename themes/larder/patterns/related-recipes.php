<?php
/**
 * Title: Recipe: more from the same shelf
 * Slug: larder/related-recipes
 * Categories: posts
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">More from the same shelf</h3>
<!-- /wp:heading -->

<!-- wp:query {"queryId":9,"query":{"perPage":4,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-tiles","layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"12rem"}} -->
<!-- wp:cover {"useFeaturedImage":true,"dimRatio":0,"minHeight":260,"minHeightUnit":"px","contentPosition":"bottom left","isDark":false} -->
<div class="wp-block-cover is-light has-custom-content-position is-position-bottom-left" style="min-height:260px"><span aria-hidden="true" class="wp-block-cover__background has-background-dim-0 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:post-title {"isLink":true,"level":3} /--></div></div>
<!-- /wp:cover -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing cooked here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
