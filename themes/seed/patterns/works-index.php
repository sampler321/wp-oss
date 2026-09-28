<?php
/**
 * Title: Works index (text list)
 * Slug: seed/works-index
 * Categories: seed-works,portfolio,query
 * Description: Every work as one line: year, title, category.
 */
?>
<!-- wp:query {"queryId":1,"query":{"perPage":100,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template -->
<!-- wp:group {"className":"is-style-rule-bottom","style":{"spacing":{"blockGap":"var:preset|spacing|50","padding":{"bottom":"var:preset|spacing|20"}}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group is-style-rule-bottom" style="padding-bottom:var(--wp--preset--spacing--20)"><!-- wp:post-date {"format":"Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-terms {"term":"category"} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
