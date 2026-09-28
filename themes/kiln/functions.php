<?php
/**
 * Kiln: pattern categories only.
 *
 * @package kiln
 */

add_action(
	'init',
	function () {
		foreach ( array(
			'kiln-shop' => 'Pottery: shop and updates',
			'kiln-pots' => 'Pottery: pots and product details',
			'kiln-opening' => 'Pottery: kiln openings',
			'kiln-process' => 'Pottery: process and glazes',
			'kiln-log' => 'Pottery: kiln log',
			'kiln-about' => 'Pottery: about, stockists and press',
			'kiln-contact' => 'Pottery: newsletter, contact and notices',
			'kiln-pages' => 'Pottery: page layouts',
		) as $slug => $label ) {
			register_block_pattern_category( $slug, array( 'label' => $label ) );
		}
	}
);
