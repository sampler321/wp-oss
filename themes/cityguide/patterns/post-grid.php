<?php
/**
 * Title: Stories grid (inherits the page query)
 * Slug: cityguide/post-grid
 * Categories: cityguide-lists,query
 * Inserter: no
 */
?>
<!-- wp:query {"queryId":0,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"grid","columnCount":4,"minimumColumnWidth":"15rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"4/3"} /-->

<!-- wp:post-terms {"term":"category"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->
<!-- /wp:post-template -->

<!-- wp:query-pagination -->
<!-- wp:query-pagination-previous /-->

<!-- wp:query-pagination-numbers /-->

<!-- wp:query-pagination-next /-->
<!-- /wp:query-pagination -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing matches that yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
