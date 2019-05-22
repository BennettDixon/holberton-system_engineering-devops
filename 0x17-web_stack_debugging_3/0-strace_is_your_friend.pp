# issue on line 137 of /var/www/html/wp-settings.php
# extra p on the class-wp-locale.php
# remove the p and restart/reload apache
$rep = 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );'
$settings = '/var/www/html/wp-settings.php'
$cmd = "sed -i \"/class-wp-locale.phpp/c ${::rep}\" ${::settings}"
exec { 'serverfix':
  path    => '/bin',
  command => $cmd,
}
