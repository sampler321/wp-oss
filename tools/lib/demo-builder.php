<?php
/**
 * Build a demo site from demos/<slug>/content.json inside WordPress Playground.
 *
 * content.json keys (all optional except site):
 *   site:        { title, tagline }
 *   categories:  [ { slug, name, description } ]
 *   pages:       [ { slug, title, pattern: "<theme>/<pattern>" | content: "<blocks>", template: "page-wide", parent: "slug", order: 1 } ]
 *   front_page:  "home" (slug of a page to use as the static front page; the theme's front-page.html still renders it)
 *   posts_page:  "work" (slug of a page used as the posts index)
 *   posts:       [ { title, slug, category: "work", tags: [..], image: "file.jpg", excerpt, date: "2025-03-01",
 *                    pattern | content, template: "single-work" } ]
 *   nav:         [ { label, url: "/work/" } ]   (a wp_navigation menu, picked up by the header's Navigation block)
 *   products:    [ { name, price, sale_price, image, category, description, sku, stock (int), status } ]   (only if WooCommerce is active)
 *   options:     { option_name: value }
 */

function wposs_log( $msg ) {
	echo $msg . "\n";
}

function wposs_image_to_library( $theme_dir, $file ) {
	static $cache = array();
	if ( isset( $cache[ $file ] ) ) {
		return $cache[ $file ];
	}
	$path = $theme_dir . '/assets/images/' . $file;
	if ( ! file_exists( $path ) ) {
		wposs_log( "missing image $file" );
		return 0;
	}
	$upload = wp_upload_bits( $file, null, file_get_contents( $path ) );
	if ( ! empty( $upload['error'] ) ) {
		wposs_log( 'upload error ' . $upload['error'] );
		return 0;
	}
	$type = wp_check_filetype( $upload['file'] );
	$id   = wp_insert_attachment(
		array(
			'post_mime_type' => $type['type'],
			'post_title'     => preg_replace( '/\.[^.]+$/', '', $file ),
			'post_status'    => 'inherit',
		),
		$upload['file']
	);
	require_once ABSPATH . 'wp-admin/includes/image.php';
	wp_update_attachment_metadata( $id, wp_generate_attachment_metadata( $id, $upload['file'] ) );
	$cache[ $file ] = $id;
	return $id;
}

function wposs_pattern_content( $slug ) {
	$registry = WP_Block_Patterns_Registry::get_instance();
	$p        = $registry->get_registered( $slug );
	if ( ! $p ) {
		wposs_log( "missing pattern $slug" );
		return '';
	}
	return $p['content'];
}

function wposs_content( $item ) {
	if ( ! empty( $item['pattern'] ) ) {
		return wposs_pattern_content( $item['pattern'] );
	}
	return isset( $item['content'] ) ? $item['content'] : '';
}


/**
 * Pattern library: an index page plus one child page per pattern category, rendering every theme pattern
 * with its name, so the demo shows the whole kit.
 */
function wposs_pattern_library( $slug ) {
	$registry = WP_Block_Patterns_Registry::get_instance();
	$cats     = array();
	foreach ( $registry->get_all_registered() as $p ) {
		if ( 0 !== strpos( $p['name'], $slug . '/' ) ) {
			continue;
		}
		$cat = ! empty( $p['categories'] ) ? $p['categories'][0] : 'other';
		$cats[ $cat ][] = $p;
	}
	if ( ! $cats ) {
		return null;
	}
	ksort( $cats );
	$index_id = wp_insert_post( array( 'post_type' => 'page', 'post_status' => 'publish', 'post_title' => 'Pattern library', 'post_name' => 'pattern-library', 'menu_order' => 900, 'post_content' => '' ) );
	update_post_meta( $index_id, '_wp_page_template', 'page-wide' );
	$index = '<!-- wp:paragraph --><p>Every block pattern in this theme, grouped by type. Add any of them from the block inserter under Patterns.</p><!-- /wp:paragraph -->';
	$list  = '';
	foreach ( $cats as $cat => $items ) {
		$label = ucwords( str_replace( array( '-', '_' ), ' ', $cat ) );
		$body  = '';
		foreach ( $items as $p ) {
			$body .= '<!-- wp:separator {"className":"is-style-wide"} --><hr class="wp-block-separator has-alpha-channel-opacity is-style-wide"/><!-- /wp:separator -->';
			$body .= '<!-- wp:paragraph {"fontSize":"small"} --><p class="has-small-font-size"><strong>' . esc_html( $p['title'] ) . '</strong></p><!-- /wp:paragraph -->';
			$body .= '<!-- wp:pattern ' . wp_json_encode( array( 'slug' => $p['name'] ), JSON_UNESCAPED_SLASHES ) . ' /-->';
		}
		$cid = wp_insert_post( array( 'post_type' => 'page', 'post_status' => 'publish', 'post_title' => $label . ' patterns', 'post_name' => sanitize_title( $cat ), 'post_parent' => $index_id, 'post_content' => wp_slash( $body ) ) );
		update_post_meta( $cid, '_wp_page_template', 'page-wide' );
		$list .= '<!-- wp:list-item --><li><a href="' . esc_url( get_permalink( $cid ) ) . '">' . esc_html( $label ) . '</a> (' . count( $items ) . ')</li><!-- /wp:list-item -->';
	}
	$index .= '<!-- wp:list --><ul class="wp-block-list">' . $list . '</ul><!-- /wp:list -->';
	wp_update_post( array( 'ID' => $index_id, 'post_content' => wp_slash( $index ) ) );
	return $index_id;
}

function wposs_build_demo( $json_path ) {
	$data = json_decode( file_get_contents( $json_path ), true );
	if ( ! $data ) {
		wposs_log( 'bad content.json' );
		return;
	}
	$theme_dir = get_stylesheet_directory();

	update_option( 'blogname', $data['site']['title'] );
	update_option( 'blogdescription', isset( $data['site']['tagline'] ) ? $data['site']['tagline'] : '' );
	global $wp_rewrite;
	$wp_rewrite->set_permalink_structure( '/%postname%/' );
	update_option( 'permalink_structure', '/%postname%/' );
	update_option( 'posts_per_page', 12 );
	foreach ( ( isset( $data['options'] ) ? $data['options'] : array() ) as $k => $v ) {
		update_option( $k, $v );
	}

	// Remove WordPress defaults.
	foreach ( array( 'hello-world', 'sample-page', 'privacy-policy' ) as $slug ) {
		$p = get_page_by_path( $slug, OBJECT, array( 'post', 'page' ) );
		if ( $p ) {
			wp_delete_post( $p->ID, true );
		}
	}
	wp_delete_comment( 1, true );

	// Categories.
	$cats = array();
	foreach ( ( isset( $data['categories'] ) ? $data['categories'] : array() ) as $c ) {
		$t = term_exists( $c['slug'], 'category' );
		if ( ! $t ) {
			$t = wp_insert_term( $c['name'], 'category', array( 'slug' => $c['slug'], 'description' => isset( $c['description'] ) ? $c['description'] : '' ) );
		}
		$cats[ $c['slug'] ] = (int) ( is_array( $t ) ? $t['term_id'] : $t );
	}

	// Pages (two passes so parents exist).
	$pages = array();
	foreach ( ( isset( $data['pages'] ) ? $data['pages'] : array() ) as $i => $pg ) {
		$id = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_status'  => 'publish',
				'post_title'   => $pg['title'],
				'post_name'    => $pg['slug'],
				'post_content' => wp_slash( wposs_content( $pg ) ),
				'menu_order'   => isset( $pg['order'] ) ? $pg['order'] : $i,
			)
		);
		if ( ! empty( $pg['template'] ) ) {
			update_post_meta( $id, '_wp_page_template', $pg['template'] );
		}
		if ( ! empty( $pg['image'] ) ) {
			set_post_thumbnail( $id, wposs_image_to_library( $theme_dir, $pg['image'] ) );
		}
		$pages[ $pg['slug'] ] = $id;
	}
	foreach ( ( isset( $data['pages'] ) ? $data['pages'] : array() ) as $pg ) {
		if ( ! empty( $pg['parent'] ) && isset( $pages[ $pg['parent'] ] ) ) {
			wp_update_post( array( 'ID' => $pages[ $pg['slug'] ], 'post_parent' => $pages[ $pg['parent'] ] ) );
		}
	}
	if ( ! empty( $data['front_page'] ) && isset( $pages[ $data['front_page'] ] ) ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_on_front', $pages[ $data['front_page'] ] );
	}
	if ( ! empty( $data['posts_page'] ) && isset( $pages[ $data['posts_page'] ] ) ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_for_posts', $pages[ $data['posts_page'] ] );
	}

	// Posts, oldest first so the first listed item ends up newest.
	$posts = isset( $data['posts'] ) ? array_reverse( $data['posts'] ) : array();
	$n     = count( $posts );
	foreach ( $posts as $i => $po ) {
		$date = ! empty( $po['date'] ) ? $po['date'] . ' 10:00:00' : gmdate( 'Y-m-d H:i:s', time() - ( $n - $i ) * 5 * DAY_IN_SECONDS );
		$id   = wp_insert_post(
			array(
				'post_type'     => 'post',
				'post_status'   => 'publish',
				'post_title'    => $po['title'],
				'post_name'     => isset( $po['slug'] ) ? $po['slug'] : sanitize_title( $po['title'] ),
				'post_content'  => wp_slash( wposs_content( $po ) ),
				'post_excerpt'  => isset( $po['excerpt'] ) ? $po['excerpt'] : '',
				'post_date'     => $date,
				'post_category' => ! empty( $po['category'] ) ? array_map( function ( $c ) use ( $cats ) { return isset( $cats[ $c ] ) ? $cats[ $c ] : 1; }, (array) $po['category'] ) : array( 1 ),
				'tags_input'    => isset( $po['tags'] ) ? $po['tags'] : array(),
			)
		);
		if ( ! empty( $po['image'] ) ) {
			set_post_thumbnail( $id, wposs_image_to_library( $theme_dir, $po['image'] ) );
		}
		if ( ! empty( $po['template'] ) ) {
			update_post_meta( $id, '_wp_page_template', $po['template'] );
		}
	}

	// Pattern library (on by default).
	$library_id = ( ! isset( $data['pattern_library'] ) || $data['pattern_library'] ) ? wposs_pattern_library( get_stylesheet() ) : null;
	if ( $library_id && ! empty( $data['nav'] ) ) {
		$data['nav'][] = array( 'label' => 'Patterns', 'url' => '/pattern-library/' );
	}

	// Navigation.
	if ( ! empty( $data['nav'] ) ) {
		$links = '';
		foreach ( $data['nav'] as $l ) {
			$attrs  = array(
				'label' => $l['label'],
				'url'   => home_url( $l['url'] ),
				'kind'  => 'custom',
			);
			$links .= '<!-- wp:navigation-link ' . wp_json_encode( $attrs, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . ' /-->';
		}
		foreach ( get_posts( array( 'post_type' => 'wp_navigation', 'numberposts' => -1, 'post_status' => 'any' ) ) as $old ) {
			wp_delete_post( $old->ID, true );
		}
		wp_insert_post(
			array(
				'post_type'    => 'wp_navigation',
				'post_status'  => 'publish',
				'post_title'   => 'Main menu',
				'post_content' => wp_slash( $links ),
			)
		);
	}

	// WooCommerce products.
	if ( ! empty( $data['products'] ) && class_exists( 'WC_Product_Simple' ) ) {
		update_option( 'woocommerce_onboarding_profile', array( 'skipped' => true ) );
		delete_transient( '_wc_activation_redirect' );
		update_option( 'woocommerce_task_list_hidden', 'yes' );
		update_option( 'woocommerce_show_marketplace_suggestions', 'no' );
		update_option( 'woocommerce_allow_tracking', 'no' );
		update_option( 'woocommerce_coming_soon', 'no' );
		update_option( 'woocommerce_currency', isset( $data['currency'] ) ? $data['currency'] : 'GBP' );
		foreach ( $data['products'] as $pr ) {
			$p = new WC_Product_Simple();
			$p->set_name( $pr['name'] );
			$p->set_status( 'publish' );
			$p->set_regular_price( (string) $pr['price'] );
			if ( ! empty( $pr['sale_price'] ) ) {
				$p->set_sale_price( (string) $pr['sale_price'] );
			}
			$p->set_description( isset( $pr['description'] ) ? $pr['description'] : '' );
			$p->set_short_description( isset( $pr['short'] ) ? $pr['short'] : '' );
			if ( isset( $pr['sku'] ) ) {
				$p->set_sku( $pr['sku'] );
			}
			if ( isset( $pr['stock'] ) ) {
				$p->set_manage_stock( true );
				$p->set_stock_quantity( (int) $pr['stock'] );
				$p->set_stock_status( (int) $pr['stock'] > 0 ? 'instock' : 'outofstock' );
			}
			if ( ! empty( $pr['image'] ) ) {
				$p->set_image_id( wposs_image_to_library( $theme_dir, $pr['image'] ) );
			}
			if ( ! empty( $pr['category'] ) ) {
				$t = term_exists( $pr['category'], 'product_cat' );
				if ( ! $t ) {
					$t = wp_insert_term( $pr['category'], 'product_cat' );
				}
				$p->set_category_ids( array( (int) ( is_array( $t ) ? $t['term_id'] : $t ) ) );
			}
			$p->save();
		}
	}

	$wp_rewrite->set_permalink_structure( '/%postname%/' );
	$wp_rewrite->flush_rules( true );
	delete_option( 'rewrite_rules' );
	wposs_log( sprintf( 'demo built: %d pages, %d posts, %d products', count( $pages ), $n, isset( $data['products'] ) ? count( $data['products'] ) : 0 ) );
}
