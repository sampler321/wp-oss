<?php
/**
 * Title: Also in the programme (horizontal cards)
 * Slug: reel/also-in-programme
 * Categories: films,query
 * Inserter: no
 */
?>
<!-- wp:group {"align":"wide","layout":{"type":"default"}} -->
<div class="wp-block-group alignwide"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Also in the programme</h3>
<!-- /wp:heading -->

<!-- wp:query {"queryId":4,"query":{"perPage":3,"pages":0,"offset":1,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-also-list"} -->
<!-- wp:columns {"style":{"spacing":{"blockGap":{"left":"var:preset|spacing|30"}}}} -->
<div class="wp-block-columns"><!-- wp:column {"width":"34%"} -->
<div class="wp-block-column" style="flex-basis:34%"><!-- wp:post-featured-image {"isLink":true} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"66%"} -->
<div class="wp-block-column" style="flex-basis:66%"><!-- wp:post-title {"level":4,"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-terms {"term":"category","className":"is-style-chip"} /-->

<!-- wp:post-excerpt {"moreText":"","excerptLength":18} /--></div>
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
