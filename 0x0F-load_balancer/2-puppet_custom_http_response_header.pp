# Puppet script to install and configure an Nginx server

package { 'nginx':
ensure          => installed,
provider        => 'apt',
install_options => ['-y'],
}

$new_header='add_header X-Served-By $hostname;'

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen \[::\]:80 default_server;',
  line   => $new_header,
}

service { 'nginx':
  ensure => 'running',
}
