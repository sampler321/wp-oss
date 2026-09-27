<?php
/**
 * Title: Catalogue index (front page)
 * Slug: oil/catalogue-index
 * Categories: portfolio,featured,query
 * Description: Signature: the index column beside a grid of every work, newest first, with sold works marked by a red dot.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60","top":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"25%","className":"is-style-index-column"} -->
<div class="wp-block-column is-style-index-column" style="flex-basis:25%"><!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Work</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Agnes Brekke paints the rooms she lives in, the city around them and the people who visit, mostly in oil on linen, in a top-floor studio in Leith.</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"oil/filter-panel"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"75%"} -->
<div class="wp-block-column" style="flex-basis:75%"><!-- wp:query {"queryId":1,"query":{"perPage":12,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-catalogue","layout":{"type":"grid","columnCount":4}} -->
<!-- wp:post-featured-image {"isLink":true} /-->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|10"}},"layout":{"type":"flex","orientation":"vertical"}} -->
<div class="wp-block-group"><!-- wp:post-title {"level":3,"isLink":true,"style":{"typography":{"fontWeight":"500","lineHeight":"1.35"}},"fontSize":"small","fontFamily":"body"} /-->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:post-date {"format":"Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-terms {"term":"post_tag"} /--></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
