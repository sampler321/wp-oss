<?php
/**
 * Title: 404: page not found
 * Slug: ink/page-404
 * Categories: text
 * Template Types: 404
 */
?>
<!-- wp:columns {"align":"wide"} -->
<div class="wp-block-columns alignwide"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading {"level":1,"fontSize":"xx-large"} -->
<h1 class="wp-block-heading has-xx-large-font-size">This page got rubbed out</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The link might be old, or I moved the drawing into a different folder. Try the <a href="/work/">work page</a>, the <a href="/shop/">shop</a>, or search below.</p>
<!-- /wp:paragraph -->

<!-- wp:search {"label":"Search","showLabel":false,"placeholder":"Birds, maps, pub signs","buttonText":"Search"} /--></div>
<!-- /wp:column -->

<!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:image {"lightbox":{"enabled":true},"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/sketch-2.jpg' ) ); ?>" alt="Faint pencil lines of a figure study on old paper"/><figcaption class="wp-element-caption">A rough that went the same way.</figcaption></figure>
<!-- /wp:image --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
