<?php
/**
 * Title: Studio and journal strip (front page)
 * Slug: oil/studio-strip
 * Categories: oil-journal,featured
 */
?>
<!-- wp:columns {"align":"wide","className":"is-style-rule-top","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|70"}}}} -->
<div class="wp-block-columns alignwide is-style-rule-top"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"fontSize":"x-large"} -->
<h2 class="wp-block-heading has-x-large-font-size">From the journal</h2>
<!-- /wp:heading -->

<!-- wp:query {"queryId":3,"query":{"perPage":3,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false,"taxQuery":{"category":[5]}}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:post-date {"fontSize":"small"} /-->

<!-- wp:post-title {"isLink":true,"level":3,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":24} /-->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/category/journal/">All journal notes</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:pattern {"slug":"oil/representation"} /-->

<!-- wp:pattern {"slug":"oil/studio-visit"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
