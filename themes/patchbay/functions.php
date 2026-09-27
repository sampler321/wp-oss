<?php
/**
 * Patchbay: pattern categories only.
 *
 * @package patchbay
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'patchbay-shop'    => 'Patchbay: shop',
			'patchbay-product' => 'Patchbay: product details',
			'patchbay-kits'    => 'Patchbay: kits and building',
			'patchbay-docs'    => 'Patchbay: build docs',
			'patchbay-support' => 'Patchbay: support',
			'patchbay-about'   => 'Patchbay: about',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
