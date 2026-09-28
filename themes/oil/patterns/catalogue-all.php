<?php
/**
 * Title: Catalogue, all work (posts page)
 * Slug: oil/catalogue-all
 * Categories: oil-catalogue,portfolio,query
 * Description: The whole catalogue. Choose your medium categories in the Query Loop settings.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60","top":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"25%","className":"is-style-index-column"} -->
<div class="wp-block-column is-style-index-column" style="flex-basis:25%"><!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">All work</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Every finished painting, drawing and monotype since 2014, sold ones included, so the prices here double as a record.</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"oil/filter-panel"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"75%"} -->
<div class="wp-block-column" style="flex-basis:75%"><!-- wp:query {"queryId":2,"query":{"perPage":48,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false,"taxQuery":{"category":[2,3,4]}}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-catalogue","layout":{"type":"grid","columnCount":4}} -->
<!-- wp:post-featured-image {"isLink":true} /-->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|10"}},"layout":{"type":"flex","orientation":"vertical"}} -->
<div class="wp-block-group"><!-- wp:post-title {"isLink":true,"level":3,"fontSize":"small","fontFamily":"body","style":{"typography":{"fontWeight":"500","lineHeight":"1.35"}}} /-->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:post-date {"format":"Y"} /-->

<!-- wp:post-terms {"term":"post_tag","separator":", "} /--></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
