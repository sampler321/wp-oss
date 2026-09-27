<?php
/**
 * Title: Studio shop link
 * Slug: studio/shop-link
 * Categories: call-to-action
 */
?>
<!-- wp:columns {"align":"wide","className":"is-style-proof","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|50"}}}} -->
<div class="wp-block-columns alignwide is-style-proof"><!-- wp:column {"width":"30%"} -->
<div class="wp-block-column" style="flex-basis:30%"><!-- wp:image {"sizeSlug":"large","linkDestination":"custom"} -->
<figure class="wp-block-image size-large"><a href="https://shop.example.com/"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/tote-1.jpg' ) ); ?>" alt="Red lithograph poster titled The Poster, with two women in long robes drawn in black line"/></a></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"70%"} -->
<div class="wp-block-column" style="flex-basis:70%"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">The shop</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We print a few things for ourselves between jobs: letterpress calendars, the Mabgate type specimen and posters from the print fair. Everything is printed in the studio and posted on Fridays.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://shop.example.com/">Go to the shop</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
