<?php
/**
 * Platter: pattern category only.
 *
 * @package platter
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'platter', array( 'label' => __( 'Platter: catering', 'platter' ) ) );
	}
);
