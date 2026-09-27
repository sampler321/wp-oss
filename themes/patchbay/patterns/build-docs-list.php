<?php
/**
 * Title: Latest build docs and demos
 * Slug: patchbay/build-docs-list
 * Categories: patchbay-docs,query
 */
?>
<!-- wp:group {"align":"wide","style":{"spacing":{"padding":{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60"}}}} -->
<div class="wp-block-group alignwide" style="padding-top:var(--wp--preset--spacing--60);padding-bottom:var(--wp--preset--spacing--60)"><!-- wp:group {"className":"is-style-wire","layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group is-style-wire"><!-- wp:heading -->
<h2 class="wp-block-heading">From the bench</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="/build-docs/">All build docs and demos</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":1,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"17rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/3","className":"is-style-framed"} /-->

<!-- wp:post-terms {"term":"category"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":20} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
