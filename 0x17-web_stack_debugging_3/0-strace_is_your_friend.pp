# issue on line 137 of /var/www/html/wp-settings.php
# extra p on the class-wp-locale.php
# remove the p and restart/reload apache
exec { 'sedfix':
  path => '/bin',
  command => 'sed -i "/class-wp-locale.phpp/ c\require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );" /var/www/html/wp-settings.php',
}

service { 'mysql':
  ensure => running,
}
