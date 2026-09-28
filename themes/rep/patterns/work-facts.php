<?php
/**
 * Title: Work facts (artist, client, styles)
 * Slug: rep/work-facts
 * Categories: portfolio
 * Inserter: no
 */
?>
<!-- wp:group {"className":"is-style-rule-top","style":{"spacing":{"blockGap":"var:preset|spacing|10","margin":{"top":"0"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group is-style-rule-top" style="margin-top:0"><!-- wp:group {"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">Artist</p>
<!-- /wp:paragraph -->

<!-- wp:post-terms {"term":"category","separator":", "} /--></div>
<!-- /wp:group -->

<!-- wp:group {"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">Client and year</p>
<!-- /wp:paragraph -->

<!-- wp:post-excerpt {"moreText":""} /--></div>
<!-- /wp:group -->

<!-- wp:group {"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"textColor":"muted","fontSize":"small"} -->
<p class="has-muted-color has-text-color has-small-font-size">Styles</p>
<!-- /wp:paragraph -->

<!-- wp:post-terms {"term":"post_tag","separator":", "} /--></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
