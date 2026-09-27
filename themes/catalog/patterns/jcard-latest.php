<?php
/**
 * Title: J-card: latest release
 * Slug: catalog/jcard-latest
 * Categories: featured,query
 * Description: The newest release laid out as an unfolded J-card: spine, front panel and flap. Reads from your latest post.
 */
?>
<!-- wp:query {"queryId":11,"query":{"perPage":1,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"wide"} -->
<div class="wp-block-query"><!-- wp:post-template -->
<!-- wp:group {"className":"is-style-jcard","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-jcard"><!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {"width":"84px","className":"is-style-spine"} -->
<div class="wp-block-column is-style-spine" style="flex-basis:84px"><!-- wp:group {"layout":{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:post-terms {"term":"post_tag","className":"is-style-catno"} /-->

<!-- wp:post-title {"level":2} /--></div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"46%"} -->
<div class="wp-block-column" style="flex-basis:46%"><!-- wp:post-featured-image {"isLink":true,"aspectRatio":"1","scale":"cover","style":{"border":{"width":"0"}}} /--></div>
<!-- /wp:column -->

<!-- wp:column {"className":"is-style-flap"} -->
<div class="wp-block-column is-style-flap"><!-- wp:group {"layout":{"type":"flex","orientation":"vertical"}} -->
<div class="wp-block-group"><!-- wp:post-terms {"term":"post_tag","className":"is-style-catno","fontSize":"large"} /-->

<!-- wp:post-title {"level":2,"isLink":true,"fontSize":"display"} /--></div>
<!-- /wp:group -->

<!-- wp:group {"layout":{"type":"flex","orientation":"vertical"}} -->
<div class="wp-block-group"><!-- wp:post-excerpt {"moreText":"","excerptLength":40,"fontSize":"large"} /-->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|40"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:read-more {"content":"Listen and buy this tape","className":"is-style-buy"} /-->

<!-- wp:post-date {"format":"j F Y"} /--></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p class="">Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
