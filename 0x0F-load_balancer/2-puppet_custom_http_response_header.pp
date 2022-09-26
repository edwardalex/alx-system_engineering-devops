# Creating a custom HTTP header response with Puppet
exec { 'update':
  command => 'sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
}
package { 'nginx':
  ensure  => installed,
  require => Exec['update']
}
file_line { 'apply_config':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By "$HOSTNAME";',
  require => Package['nginx'],
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
