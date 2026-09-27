<?php
/**
 * Taproom: pattern categories only.
 *
 * @package taproom
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'taproom-taproom' => 'Taproom: tap list and visiting',
			'taproom-beers'   => 'Taproom: beers',
			'taproom-events'  => 'Taproom: events',
			'taproom-shop'    => 'Taproom: shop and beer club',
			'taproom-about'   => 'Taproom: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
