# Puppet script to install and configure an Nginx server

exec { 'update':
  command  => 'apt-get update',
  path     => '/usr/bin/'
}

package { 'nginx':
ensure          => installed,
provider        => 'apt',
install_options => ['-y'],
}

file_line { 'add header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'http {',
  line   => "\tadd_header X-Served-By \"${hostname}\";",
}

service { 'nginx':
  ensure => 'running',
}
