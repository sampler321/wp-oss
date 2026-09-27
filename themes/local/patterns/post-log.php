<?php
/**
 * Title: News log (inherits the page query)
 * Slug: local/post-log
 * Categories: posts,query
 * Inserter: no
 */
?>
<!-- wp:query {"queryId":0,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-log"} -->
<!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"var:preset|spacing|40"}}}} -->
<div class="wp-block-columns"><!-- wp:column {"width":"9rem"} -->
<div class="wp-block-column" style="flex-basis:9rem"><!-- wp:post-date {"format":"j M Y"} /-->

<!-- wp:post-terms {"term":"category","separator":", "} /--></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:post-title {"isLink":true,"level":3,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":28,"moreText":""} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"220px"} -->
<div class="wp-block-column" style="flex-basis:220px"><!-- wp:post-featured-image {"isLink":true,"aspectRatio":"3/2","sizeSlug":"medium"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
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
