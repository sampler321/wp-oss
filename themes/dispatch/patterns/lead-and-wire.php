<?php
/**
 * Title: Lead story with the wire beside it
 * Slug: dispatch/lead-and-wire
 * Categories: featured,posts
 * Description: The home page opener: the lead story on the left, a timestamped wire of everything else on the right.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"68%"} -->
<div class="wp-block-column" style="flex-basis:68%"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"className":"is-style-dateline","textColor":"accent"} -->
<p class="is-style-dateline has-accent-color has-text-color">Investigation</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"className":"is-style-members-tag","fontSize":"x-small"} -->
<p class="is-style-members-tag has-x-small-font-size">Members</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:heading {"level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-xx-large-font-size"><a href="/ad-exchange-hospital-location-data/">An ad exchange sold location data from 41 hospitals</a></h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">Bid requests from a Dutch exchange carried the precise location of phones inside cancer wards and fertility clinics. Three data brokers bought the stream. Two of them sell to insurers.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|30"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"className":"has-small-font-size has-display-font-family","style":{"typography":{"fontWeight":"800"}},"fontSize":"small"} -->
<p class="has-small-font-size has-display-font-family" style="font-weight:800">By Lena Varga</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small","fontFamily":"display"} -->
<p class="has-display-font-family has-small-font-size">Brussels, 24 September 2026, 07:10</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"muted","fontSize":"small","fontFamily":"display"} -->
<p class="has-muted-color has-text-color has-display-font-family has-small-font-size">14 min read</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none","className":"is-style-photo"} -->
<figure class="wp-block-image size-large is-style-photo"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/phones.jpg' ) ); ?>" alt="A phone, an open notebook, a pencil and glasses on a white desk"/><figcaption class="wp-element-caption">The test phone we used for six weeks, running eleven free apps. Photo: stand-in, CC0.</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"32%"} -->
<div class="wp-block-column" style="flex-basis:32%"><!-- wp:group {"className":"is-style-rule-top","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-rule-top"><!-- wp:group {"layout":{"type":"flex","flexWrap":"wrap","justifyContent":"space-between"}} -->
<div class="wp-block-group"><!-- wp:heading {"fontSize":"large"} -->
<h2 class="wp-block-heading has-large-font-size">The wire</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size"><a href="/latest/">All</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:query {"queryId":1,"query":{"perPage":7,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":false}} -->
<div class="wp-block-query"><!-- wp:post-template {"className":"is-style-wire"} -->
<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|10"}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|20"}},"layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group"><!-- wp:post-date {"format":"D j M","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-terms {"term":"post_tag","className":"is-style-members-tag"} /--></div>
<!-- /wp:group -->

<!-- wp:post-title {"level":4,"isLink":true,"fontSize":"medium"} /--></div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-no-results -->
<!-- wp:paragraph -->
<p>Nothing here yet.</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results --></div>
<!-- /wp:query --></div>
<!-- /wp:group --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
