<?php
/**
 * Wall: pattern categories only.
 *
 * @package wall
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'wall-hero' => 'Walls: openers',
			'wall-murals' => 'Walls: murals and archive',
			'wall-commissions' => 'Walls: commissions and prices',
			'wall-process' => 'Walls: process',
			'wall-shop' => 'Walls: prints',
			'wall-about' => 'Walls: about and press',
			'wall-contact' => 'Walls: contact and notices',
			'wall-pages' => 'Walls: page layouts',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
