<?php
/**
 * Title: What's on: newest show over a full-bleed photo
 * Slug: commons/whats-on-hero
 * Categories: whats-on
 * Description: The newest show in the programme, as a full-width installation photo with a label card: number, title, artists and dates, opening hours.
 */
?>
<!-- wp:query {"queryId":11,"query":{"perPage":1,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false},"align":"full"} -->
<div class="wp-block-query alignfull"><!-- wp:post-template -->
<!-- wp:cover {"useFeaturedImage":true,"dimRatio":10,"overlayColor":"contrast","isUserOverlayColor":true,"minHeight":88,"minHeightUnit":"vh","contentPosition":"bottom left","align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|40","right":"var:preset|spacing|40"}}}} -->
<div class="wp-block-cover alignfull has-custom-content-position is-position-bottom-left" style="padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--40);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--40);min-height:88vh"><span aria-hidden="true" class="wp-block-cover__background has-contrast-background-color has-background-dim-10 has-background-dim"></span><div class="wp-block-cover__inner-container"><!-- wp:group {"className":"is-style-label-card","layout":{"type":"constrained","contentSize":"30rem","justifyContent":"left"}} -->
<div class="wp-block-group is-style-label-card"><!-- wp:post-terms {"term":"post_tag","className":"is-style-running-number"} /-->

<!-- wp:post-title {"level":1,"isLink":true,"fontSize":"xx-large"} /-->

<!-- wp:post-excerpt /-->

<!-- wp:paragraph {"fontSize":"x-small"} -->
<p class="has-x-small-font-size">Thursday to Sunday, 12 to 6pm. Free, no booking.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="/visit/">Plan a visit</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div></div>
<!-- /wp:cover -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query -->
