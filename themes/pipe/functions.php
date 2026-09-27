<?php
/**
 * Pipe: pattern category only.
 *
 * @package pipe
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'pipe', array( 'label' => __( 'Pipe: heating and plumbing', 'pipe' ) ) );
	}
);
