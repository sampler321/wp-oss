<?php
/**
 * Title: Read next
 * Slug: dispatch/read-next
 * Categories: posts,query
 */
?>
<!-- wp:group {"align":"wide","className":"is-style-rule-top","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide is-style-rule-top"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Read next</h3>
<!-- /wp:heading -->

<!-- wp:query {"queryId":3,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"12rem"}} -->
<!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:post-date {"format":"j M","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-title {"level":4,"isLink":true,"fontSize":"medium"} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
