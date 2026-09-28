<?php
/**
 * Title: Archive index: every mix by date
 * Slug: bpm/mix-index
 * Categories: query
 * Description: A dense list for crate-digging: date, title, genres, show.
 * Inserter: no
 */
?>
<!-- wp:query {"queryId":0,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:group {"className":"is-style-index-row","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-index-row"><!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"var:preset|spacing|30"}}},"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {"width":"14%"} -->
<div class="wp-block-column" style="flex-basis:14%"><!-- wp:post-date {"format":"d.m.Y"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"46%"} -->
<div class="wp-block-column" style="flex-basis:46%"><!-- wp:post-title {"isLink":true,"level":3,"fontSize":"large"} /--></div>
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
<p class="">Nothing matches that yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
