<?php
/**
 * Title: Every wall, one line each
 * Slug: wall/wall-index
 * Categories: wall-murals,portfolio,query
 * Description: A text index of every wall, newest first.
 */
?>
<!-- wp:query {"queryId":1,"query":{"perPage":50,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"full"} -->
<div class="wp-block-query alignfull"><!-- wp:post-template -->
<!-- wp:group {"className":"is-style-rule-top","style":{"spacing":{"padding":{"top":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group is-style-rule-top" style="padding-top:var(--wp--preset--spacing--20)"><!-- wp:post-title {"level":3,"isLink":true,"fontSize":"x-large"} /-->

<!-- wp:post-terms {"term":"category","fontSize":"large"} /-->

<!-- wp:post-date {"format":"Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}},"fontSize":"large"} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
