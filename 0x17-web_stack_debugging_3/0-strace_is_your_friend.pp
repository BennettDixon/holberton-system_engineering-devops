# issue on line 137 of /var/www/html/wp-settings.php
$rep = 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );'
$settings = '/var/www/html/wp-settings.php'
$cmd = "sed -i \"/class-wp-locale.phpp/c ${::rep}\" ${::settings}"
exec { 'serverfix':
  path    => '/bin',
  command => $cmd,
}
