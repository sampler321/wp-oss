<?php
/**
 * Title: Project layout: a book cover
 * Slug: rep/project-cover
 * Categories: project
 * Block Types: core/post-content
 */
?>
<!-- wp:columns {"align":"wide","verticalAlignment":"center"} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"42%"} -->
<div class="wp-block-column" style="flex-basis:42%"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","lightbox":{"enabled":true}} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/bw-2.jpg' ) ); ?>" alt="Bold black and white linocut of a stylised figure in striped patterns"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"58%"} -->
<div class="wp-block-column" style="flex-basis:58%"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Cut at 1:1</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p class="">Sade cut the cover at the size it prints, 129 x 198 mm, so every mark on the book is a mark on the block. It took nine days and one new blade.</p>
<!-- /wp:paragraph -->

<!-- wp:pattern {"slug":"rep/project-quote"} /--></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group"><!-- wp:heading {"level":6} -->
<h6 class="wp-block-heading">Credits</h6>
<!-- /wp:heading -->

<!-- wp:group {"style":{"spacing":{"blockGap":"0"},"border":{"top":{"color":"var:preset|color|line","width":"1px","style":"solid"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:group {"className":"is-style-ruled-row","layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group is-style-ruled-row"><!-- wp:paragraph -->
<p class="">Artist</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p class="">Sade Olatunji</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-ruled-row","layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group is-style-ruled-row"><!-- wp:paragraph -->
<p class="">Client</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p class="">Penguin Modern Classics</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-ruled-row","layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group is-style-ruled-row"><!-- wp:paragraph -->
<p class="">Agent</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p class="">Priya Raman</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"className":"is-style-ruled-row","layout":{"type":"flex","flexWrap":"wrap"}} -->
<div class="wp-block-group is-style-ruled-row"><!-- wp:paragraph -->
<p class="">Licence</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p class="">World, all editions, ten years</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
