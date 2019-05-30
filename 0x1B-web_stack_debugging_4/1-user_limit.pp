# puppet fix for allowing higher hard/soft file open limits
$file = '/etc/security/limits.conf'
# setup search and replace strings
$hard_txt = 'holberton hard nofile'
$hard_rep = "${::hard_txt} 10000"
$soft_txt = 'holberton soft nofile'
$soft_rep = "${::soft_txt} 8000"
# verify text hasn't been replaced already
$hard_exists = "grep ${::hard_rep} ${::file}"
$soft_exists = "grep ${::soft_rep} ${::file}"
# replace the text
$hard_cmd = "sed -i '/${::hard_txt} /c ${::hard_rep}' ${::file}"
$soft_cmd = "sed -i '/${::soft_txt} /c ${::soft_rep}' ${::file}"

# actual execution / puppet logic
exec { 'hard_limit_fix' :
  path    => '/bin',
  unless  => $hard_exists,
  command => $hard_cmd,
}
exec { 'soft_limit_fix' :
  path    => '/bin',
  unless  => $soft_exists,
  command => $soft_cmd,
}

# restart sysctl after applying changes to limits file
exec { 'sysctl_restart' :
  path      => '/sbin',
  subscribe => Exec['soft_limit_fix', 'hard_limit_fix'],
  command   => 'sysctl -p',
}
