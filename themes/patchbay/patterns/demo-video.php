<?php
/**
 * Title: Demo video card
 * Slug: patchbay/demo-video
 * Categories: patchbay-docs
 * Description: Paste your video link into the button, or swap the group for an Embed block.
 */
?>
<!-- wp:group {"className":"is-style-enclosure-yellow","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-enclosure-yellow"><!-- wp:columns {"verticalAlignment":"center"} -->
<div class="wp-block-columns are-vertically-aligned-center"><!-- wp:column {"width":"40%"} -->
<div class="wp-block-column" style="flex-basis:40%"><!-- wp:image {"sizeSlug":"large","linkDestination":"none","className":"is-style-framed"} -->
<figure class="wp-block-image size-large is-style-framed"><img src="<?php echo esc_url( get_theme_file_uri( 'assets/images/amp.jpg' ) ); ?>" alt="Black Fender Champion II 50 amplifier with its control panel along the top"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {"width":"60%"} -->
<div class="wp-block-column" style="flex-basis:60%"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Watch the demo</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Four minutes, a Telecaster into a Champion with no other pedals. Knobs at noon for the first minute, then Rob turns things.</p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://www.youtube.com/">Play the demo on YouTube</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
