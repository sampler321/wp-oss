<?php
/**
 * Title: Post list
 * Slug: ink/post-list
 * Categories: posts,query
 * Inserter: no
 */
?>
<!-- wp:query {"queryId":0,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template -->
<!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:post-date {"metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}},"fontFamily":"mono"} /-->

<!-- wp:post-title {"isLink":true,"fontSize":"large"} /--></div>
<!-- /wp:group -->
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
