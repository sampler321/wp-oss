<?php
/**
 * Title: Next case study
 * Slug: case/next-case
 * Categories: query
 * Description: Shows the second-newest case study as a link to read next.
 */
?>
<!-- wp:group {"align":"wide","className":"is-style-rule-top","layout":{"type":"constrained","contentSize":"1240px"}} -->
<div class="wp-block-group alignwide is-style-rule-top"><!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Next case study</p>
<!-- /wp:paragraph -->

<!-- wp:query {"queryId":41,"query":{"perPage":1,"pages":0,"offset":1,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:post-featured-image {"isLink":true,"aspectRatio":"16/10","className":"is-style-framed"} /--></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:post-title {"isLink":true,"fontSize":"xx-large"} /-->

<!-- wp:post-excerpt /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->
