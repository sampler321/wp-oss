<?php
/**
 * Title: Episode rail
 * Slug: patchnotes/episode-rail
 * Categories: audio
 * Inserter: no
 */
?>
<!-- wp:group {"className":"is-style-rail","layout":{"type":"default"}} -->
<div class="wp-block-group is-style-rail"></div>
<!-- /wp:group -->

<!-- wp:post-terms {"term":"post_tag","style":{"typography":{"fontWeight":"800"}},"fontSize":"large"} /-->

<!-- wp:post-date {"format":"l j F Y","metadata":{"bindings":{"datetime":{"source":"core/post-data","args":{"field":"date"}}}}} /-->

<!-- wp:post-terms {"term":"category"} /-->

<!-- wp:post-featured-image {"aspectRatio":"4/3"} /-->

<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"className":"has-muted-color has-text-color has-x-small-font-size","style":{"typography":{"fontWeight":"600"}},"textColor":"muted","fontSize":"x-small"} -->
<p class="has-muted-color has-text-color has-x-small-font-size" style="font-weight:600">Listen in an app</p>
<!-- /wp:paragraph -->

<!-- wp:list {"className":"is-style-listen-row"} -->
<ul class="wp-block-list is-style-listen-row"><!-- wp:list-item -->
<li><a href="https://podcasts.apple.com/">Apple Podcasts</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://pocketcasts.com/">Pocket Casts</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://overcast.fm/">Overcast</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://open.spotify.com/">Spotify</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://antennapod.org/">AntennaPod</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="/feed/">RSS</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:group -->

<!-- wp:group {"layout":{"type":"constrained"}} -->
<div class="wp-block-group"><!-- wp:paragraph {"className":"has-muted-color has-text-color has-x-small-font-size","style":{"typography":{"fontWeight":"600"}},"textColor":"muted","fontSize":"x-small"} -->
<p class="has-muted-color has-text-color has-x-small-font-size" style="font-weight:600">Something wrong in this episode?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"small"} -->
<p class="has-small-font-size">Email fixes@minorversion.example. It goes in next week’s “Fixed”.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->
