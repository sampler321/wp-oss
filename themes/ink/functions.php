<?php
/**
 * Ink: pattern categories only.
 *
 * @package ink
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'shop'        => __( 'Shop and originals', 'ink' ),
			'commissions' => __( 'Commissions', 'ink' ),
			'events'      => __( 'Events and workshops', 'ink' ),
			'pages'       => __( 'Page layouts', 'ink' ),
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
