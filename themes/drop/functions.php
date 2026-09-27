<?php
/**
 * Drop: pattern category only.
 *
 * @package drop
 */

add_action(
	'init',
	function () {
		register_block_pattern_category( 'drop', array( 'label' => __( 'Drop: merch table', 'drop' ) ) );
	}
);
