<?php
/**
 * Title: Works index: latest fourteen, each credited
 * Slug: rep/works-index
 * Categories: portfolio,query
 * Keywords: work, grid, index
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:pattern {"slug":"rep/discipline-filter"} /-->

<!-- wp:query {"queryId":1,"query":{"perPage":14,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-index-grid"} -->
<!-- wp:post-featured-image {"isLink":true,"sizeSlug":"medium"} /-->

<!-- wp:post-title {"isLink":true,"level":3,"fontSize":"small","style":{"typography":{"fontWeight":"500","letterSpacing":"0"}}} /-->

<!-- wp:post-terms {"term":"category","separator":", ","fontSize":"x-small"} /-->

<!-- wp:post-excerpt {"excerptLength":8,"moreText":""} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">No work yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
