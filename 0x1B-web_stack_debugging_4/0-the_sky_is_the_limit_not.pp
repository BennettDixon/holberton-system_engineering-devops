# puppet fix for allowing multiple worker processes
$new_limit = 'worker_rlimit_nofile 30000;'
$replace = "sed -i '/user www-data/a ${::new_limit}' /etc/nginx/nginx.conf"
$replace_exists = "grep \"${::new_limit}\" /etc/nginx/nginx.conf"
exec { 'nofile_fix' :
  path    => '/bin',
  unless  => $replace_exists,
  command => $replace,
}
exec { 'hard_stop_nginx' :
  path    => '/usr/bin',
  onlyif  => 'pgrep nginx',
  command => 'pkill nginx',
}

exec { 'nginx_start' :
  unless    => '/usr/bin/pgrep nginx',
  subscribe => Exec['hard_stop_nginx'],
  command   => '/usr/sbin/nginx'
}
