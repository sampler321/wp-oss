<?php
/**
 * Title: Projects: latest
 * Slug: joint/projects-grid
 * Categories: query
 */
?>
<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|70"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--70)"><!-- wp:group {"align":"wide","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading -->
<h2 class="wp-block-heading">Recent projects</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="/projects/">All projects</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":31,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"16rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/3","scale":"contain","className":"is-style-plate"} /-->

<!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:post-terms {"term":"category"} /-->

<!-- wp:post-date {"format":"Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /--></div>
<!-- /wp:group -->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
