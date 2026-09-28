<?php
/**
 * Drum: pattern categories only.
 *
 * @package drum
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'drum-home' => 'Riso: home and heroes',
			'drum-print' => 'Riso: print services',
			'drum-inks' => 'Riso: inks and paper',
			'drum-workshops' => 'Riso: workshops and club',
			'drum-shop' => 'Riso: shop',
			'drum-jobs' => 'Riso: jobs and portfolio',
			'drum-about' => 'Riso: about and co-op',
			'drum-contact' => 'Riso: contact and notices',
			'drum-pages' => 'Riso: page layouts',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
