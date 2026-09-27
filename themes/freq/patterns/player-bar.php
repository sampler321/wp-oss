<?php
/**
 * Title: Live player bar (fixed to the bottom)
 * Slug: freq/player-bar
 * Categories: banner
 * Description: The black bar with the live stream. Paste your stream URL into the audio block and update now/next each day.
 */
?>
<!-- wp:group {"align":"full","className":"is-style-player-bar","layout":{"type":"constrained"},"anchor":"player"} -->
<div class="wp-block-group alignfull is-style-player-bar" id="player"><!-- wp:columns {"verticalAlignment":"center","isStackedOnMobile":false,"align":"full","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|30"}}}} -->
<div class="wp-block-columns alignfull are-vertically-aligned-center is-not-stacked-on-mobile"><!-- wp:column {"verticalAlignment":"center","width":"14%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:14%"><!-- wp:paragraph {"className":"is-style-live-dot"} -->
<p class="is-style-live-dot">Live now</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"32%"} -->
<div class="wp-block-column is-vertically-aligned-center" style="flex-basis:32%"><!-- wp:paragraph -->
<p><strong>Kapsalon</strong> with DJ Yasmina, 20:00 to 22:00</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center","width":"24%","className":"is-hide-mobile"} -->
<div class="wp-block-column is-vertically-aligned-center is-hide-mobile" style="flex-basis:24%"><!-- wp:paragraph {"className":"is-hide-mobile"} -->
<p class="is-hide-mobile">Next: Klankkast with Sem van Dijk, 22:00</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column {"verticalAlignment":"center"} -->
<div class="wp-block-column is-vertically-aligned-center"><!-- wp:audio -->
<figure class="wp-block-audio"><audio controls src="https://stream.example.com/radiohavik-128.mp3"></audio></figure>
<!-- /wp:audio --></div>
<!-- /wp:column --></div>
<!-- /wp:columns --></div>
<!-- /wp:group -->
