<?php
/**
 * Scoop: pattern category only.
 *
 * @package scoop
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'scoop', array( 'label' => __( 'Scoop: gelateria', 'scoop' ) ) );
	}
);
