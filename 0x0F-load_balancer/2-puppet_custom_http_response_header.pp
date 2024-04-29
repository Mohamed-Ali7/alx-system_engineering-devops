# Puppet script to install and configure an Nginx server

exec { 'update':
  command  => 'apt-get update',
  provider => shell,
}

package { 'nginx':
ensure          => installed,
provider        => 'apt',
install_options => ['-y'],
}

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen \[::\]:80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}

service { 'nginx':
  ensure => 'running',
}
