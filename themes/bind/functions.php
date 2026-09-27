<?php
/**
 * Bind: pattern categories only.
 *
 * @package bind
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'bind-services'  => 'Bindery: services',
			'bind-prices'    => 'Bindery: price guide',
			'bind-cases'     => 'Bindery: case studies',
			'bind-workshops' => 'Bindery: workshops',
			'bind-visit'     => 'Bindery: visit and orders',
			'bind-about'     => 'Bindery: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
