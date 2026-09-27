<?php
/**
 * Title: Episode tiles (black and white squares)
 * Slug: freq/episode-tiles
 * Categories: query
 */
?>
<!-- wp:query {"queryId":42,"query":{"perPage":6,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"className":"is-style-bw-tiles","layout":{"type":"grid","columnCount":6,"minimumColumnWidth":"10rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"1"} /-->

<!-- wp:post-terms {"term":"category"} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"medium"} /-->

<!-- wp:post-date {"format":"j M Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
