<?php
/**
 * Title: In use (latest posts)
 * Slug: glyph/in-use-grid
 * Categories: in-use
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading -->
<h2 class="wp-block-heading">In use</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p class=""><a href="/in-use/">Everything in use</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":51,"query":{"perPage":4,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template {"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"14rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"3/2","scale":"cover"} /-->

<!-- wp:post-title {"isLink":true,"level":3,"fontSize":"medium"} /-->

<!-- wp:post-terms {"term":"post_tag"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
