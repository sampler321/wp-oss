<?php
/**
 * Title: Gear inventory: by category, per room and shared
 * Slug: booth/gear-inventory
 * Categories: featured
 * Description: Equipment grouped by category with a sticky index. Each item says whether it stays in one room or is shared.
 */
?>
<!-- wp:columns {"align":"wide","style":{"spacing":{"blockGap":{"left":"var:preset|spacing|60"}}}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {"width":"26%","className":"is-style-sticky-index"} -->
<div class="wp-block-column is-style-sticky-index" style="flex-basis:26%"><!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Jump to</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="#consoles">Consoles and monitoring</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="#microphones">Microphones</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="#recorders">Recorders</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="#outboard">Outboard</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="#instruments">Instruments and amps</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="<?php echo esc_url( get_theme_file_uri( 'assets/gear-list.txt' ) ); ?>">Text-only list for engineers</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph {"className":"has-muted-color","fontSize":"x-small"} -->
<p class="has-muted-color has-x-small-font-size"><strong>A</strong> and <strong>B</strong> mean the item stays in that room. Shared gear moves to whichever room needs it, so ask if you need two of something on the same day.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:details {"showContent":true,"anchor":"consoles"} -->
<details id="consoles" class="wp-block-details" open><summary>Consoles and monitoring</summary><!-- wp:table {"className":"is-style-gear-table"} -->
<figure class="wp-block-table is-style-gear-table"><table class="has-fixed-layout"><thead><tr><th>Item</th><th>Notes</th><th>Room</th></tr></thead><tbody><tr><td>Polish Radio console, Neve-style</td><td>32 channels, 1084-style EQ, rebuilt by Tonmeister Szczecin in 2021</td><td><em>A</em></td></tr><tr><td>SSL XLogic X-Desk</td><td>16-channel summing mixer with SuperAnalogue preamps</td><td><em>B</em></td></tr><tr><td>ATC SCM45A</td><td>Main monitors in Studio A</td><td><em>A</em></td></tr><tr><td>ATC SCM25A, Yamaha NS-10M</td><td>Mix monitors in Studio B</td><td><em>B</em></td></tr><tr><td>Hear Back PRO</td><td>Six headphone mixes, 12 pairs of Beyerdynamic DT 770</td><td><strong>Shared</strong></td></tr></tbody></table></figure>
<!-- /wp:table --></details>
<!-- /wp:details -->

<!-- wp:details {"showContent":true,"anchor":"microphones"} -->
<details id="microphones" class="wp-block-details" open><summary>Microphones</summary><!-- wp:table {"className":"is-style-gear-table"} -->
<figure class="wp-block-table is-style-gear-table"><table class="has-fixed-layout"><thead><tr><th>Item</th><th>Notes</th><th>Room</th></tr></thead><tbody><tr><td>Neumann U 87 Ai (x2)</td><td>Large-diaphragm condenser</td><td><strong>Shared</strong></td></tr><tr><td>AKG C414 XLS (x2)</td><td>Multi-pattern condenser</td><td><strong>Shared</strong></td></tr><tr><td>Coles 4038 (pair)</td><td>Ribbon, our favourite on drum overheads</td><td><em>A</em></td></tr><tr><td>Royer R-121 (x2)</td><td>Ribbon, guitar cabs</td><td><strong>Shared</strong></td></tr><tr><td>Tonsil MD 263</td><td>Polish dynamic from the 70s. Sounds like a telephone, in a good way</td><td><strong>Shared</strong></td></tr><tr><td>Shure SM57 (x8), SM7B (x2), Beta 52A</td><td>Dynamics</td><td><strong>Shared</strong></td></tr></tbody></table></figure>
<!-- /wp:table --></details>
<!-- /wp:details -->

<!-- wp:details {"showContent":true,"anchor":"recorders"} -->
<details id="recorders" class="wp-block-details" open><summary>Recorders</summary><!-- wp:table {"className":"is-style-gear-table"} -->
<figure class="wp-block-table is-style-gear-table"><table class="has-fixed-layout"><thead><tr><th>Item</th><th>Notes</th><th>Room</th></tr></thead><tbody><tr><td>Studer A827</td><td>24-track, 2 inch. Tape is 1,150 zł a reel, bring your own if you like</td><td><em>A</em></td></tr><tr><td>Pro Tools HDX</td><td>64 inputs through Avid HD I/O and Burl B2 converters</td><td><strong>Shared</strong></td></tr><tr><td>Otari MX-5050</td><td>1/4 inch half-track for mixdown</td><td><em>B</em></td></tr></tbody></table></figure>
<!-- /wp:table --></details>
<!-- /wp:details -->

<!-- wp:details {"showContent":true,"anchor":"outboard"} -->
<details id="outboard" class="wp-block-details" open><summary>Outboard</summary><!-- wp:table {"className":"is-style-gear-table"} -->
<figure class="wp-block-table is-style-gear-table"><table class="has-fixed-layout"><thead><tr><th>Item</th><th>Notes</th><th>Room</th></tr></thead><tbody><tr><td>Universal Audio 1176LN (x2)</td><td>Compressor</td><td><strong>Shared</strong></td></tr><tr><td>Teletronix LA-2A</td><td>Compressor</td><td><em>A</em></td></tr><tr><td>Chandler TG1</td><td>Limiter</td><td><em>B</em></td></tr><tr><td>EMT 140</td><td>Plate reverb, in the old paint store next door</td><td><strong>Shared</strong></td></tr><tr><td>Roland RE-201 Space Echo</td><td>Tape echo. Works most days</td><td><strong>Shared</strong></td></tr></tbody></table></figure>
<!-- /wp:table --></details>
<!-- /wp:details -->

<!-- wp:details {"showContent":true,"anchor":"instruments"} -->
<details id="instruments" class="wp-block-details" open><summary>Instruments and amps</summary><!-- wp:table {"className":"is-style-gear-table"} -->
<figure class="wp-block-table is-style-gear-table"><table class="has-fixed-layout"><thead><tr><th>Item</th><th>Notes</th><th>Room</th></tr></thead><tbody><tr><td>Yamaha C7 grand</td><td>Tuned before every booking, included in the rate</td><td><em>A</em></td></tr><tr><td>Hammond A-100 with Leslie 147</td><td></td><td><em>A</em></td></tr><tr><td>Ludwig Classic Maple kit</td><td>22, 13, 16, with a Supraphonic snare</td><td><em>A</em></td></tr><tr><td>Fender Twin Reverb, Vox AC30, Ampeg B-15</td><td>Amps</td><td><strong>Shared</strong></td></tr><tr><td>Fender Champion II 50</td><td>Small practice combo, lives in the rehearsal room</td><td><em>Rehearsal</em></td></tr></tbody></table></figure>
<!-- /wp:table --></details>
<!-- /wp:details -->

<!-- wp:paragraph {"className":"is-style-lead"} -->
<p class="is-style-lead">Need something that is not here? We can usually hire it from Nord Rental in Gdynia with a day's notice, at cost.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
