<?php
/**
 * Title: Episode: full layout (file card, player, chapters, sources, transcript)
 * Slug: evidence/episode-full
 * Categories: audio,featured
 * Description: Every part in the same order: file card, player, warning, chapters, sources, transcript.
 * Block Types: core/post-content
 */
?>
<!-- wp:group {"className":"is-style-file-card","layout":{"type":"constrained"}} -->
<div class="wp-block-group is-style-file-card"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Case file</h4>
<!-- /wp:heading -->

<!-- wp:table -->
<figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr><td>Case</td><td>Wagstaff’s Yard</td></tr><tr><td>Part</td><td>4 of 6</td></tr><tr><td>Released</td><td>Thursday 24 September 2026</td></tr><tr><td>Length</td><td>48 minutes</td></tr></tbody></table></figure>
<!-- /wp:table --></div>
<!-- /wp:group -->

<!-- wp:audio -->
<figure class="wp-block-audio"><audio controls src="https://upload.wikimedia.org/wikipedia/commons/a/a7/Trialofsusanbanthony_18_anonymous_128kb.ogg"></audio><figcaption class="wp-element-caption">Stand-in audio: a LibriVox reading from “An Account of the Proceedings on the Trial of Susan B. Anthony” (CC0, Wikimedia Commons). Replace with your episode file.</figcaption></figure>
<!-- /wp:audio -->

<!-- wp:pattern {"slug":"evidence/content-warning"} /-->

<!-- wp:pattern {"slug":"evidence/chapters-list"} /-->

<!-- wp:pattern {"slug":"evidence/sources-list"} /-->

<!-- wp:pattern {"slug":"evidence/guest-card"} /-->

<!-- wp:pattern {"slug":"evidence/transcript"} /-->

<!-- wp:pattern {"slug":"evidence/help-lines"} /-->
