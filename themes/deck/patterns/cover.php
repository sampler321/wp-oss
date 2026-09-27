<?php
/**
 * Title: Magazine cover (home hero)
 * Slug: deck/cover
 * Categories: featured,banner
 * Description: The home hero as a skate magazine cover: halftone photo, masthead over it, ransom-note cover lines.
 */
?>
<!-- wp:group {"className":"is-style-cover-stack","align":"full","layout":{"type":"default"}} -->
<div class="wp-block-group alignfull is-style-cover-stack"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","className":"is-style-halftone"} -->
<figure class="wp-block-image size-large is-style-halftone"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/venice-grind.jpg' ) ); ?>" alt="Black and white photo of a skater grinding the coping of a concrete bowl, palm trees behind"/></figure>
<!-- /wp:image -->

<!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:site-title {"level":1,"className":"is-style-masthead","isLink":false} /-->

<!-- wp:group {"style":{"spacing":{"blockGap":"var:preset|spacing|30"}},"layout":{"type":"flex","orientation":"vertical","justifyContent":"left"}} -->
<div class="wp-block-group"><!-- wp:heading {"className":"is-style-ransom","fontSize":"x-large"} -->
<h2 class="wp-block-heading is-style-ransom has-x-large-font-size"><mark>Free</mark> <strong>grip</strong> <em>on</em> <mark>every</mark> <em>deck</em></h2>
<!-- /wp:heading -->

<!-- wp:heading {"className":"is-style-ransom","fontSize":"x-large"} -->
<h2 class="wp-block-heading is-style-ransom has-x-large-font-size"><mark>Which</mark> <strong>trucks</strong> <em>fit</em> <mark>your</mark> <em>deck</em></h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"fontSize":"large","textColor":"accent-2"} -->
<p class="has-accent-2-color has-text-color has-large-font-size"><a href="/team/">Nia Campbell's new part is up</a>. <a href="/events/">Bowl jam, Saturday 11 October</a>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
