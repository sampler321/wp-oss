<?php
/**
 * Cityguide: pattern categories only.
 *
 * @package cityguide
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'cityguide-events'    => 'City guide: events',
			'cityguide-places'    => 'City guide: places and map',
			'cityguide-lists'     => 'City guide: lists and stories',
			'cityguide-practical' => 'City guide: practical',
			'cityguide-shop'      => 'City guide: printed map',
			'cityguide-about'     => 'City guide: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
