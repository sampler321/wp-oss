<?php
/**
 * Title: Post list
 * Slug: bpm/post-list
 * Categories: posts,query
 * Inserter: no
 */
?>
<!-- wp:query {"queryId":0,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template -->
<!-- wp:group {"className":"is-style-index-row","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-index-row"><!-- wp:columns {"verticalAlignment":"center","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|30"}}}} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {"width":"14%"} -->
<div class="wp-block-column" style="flex-basis:14%"><!-- wp:post-date {"format":"d.m.Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"46%"} -->
<div class="wp-block-column" style="flex-basis:46%"><!-- wp:post-title {"level":3,"isLink":true,"fontSize":"large"} /--></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:post-terms {"term":"post_tag","className":"is-style-tag-boxes"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"12%"} -->
<div class="wp-block-column" style="flex-basis:12%"><!-- wp:post-terms {"term":"category"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
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
