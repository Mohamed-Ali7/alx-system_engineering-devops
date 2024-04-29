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

$new_header="\tadd_header X-Served-By \$hostname;"

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'http {',
  line   => $new_header,
}

service { 'nginx':
  ensure => 'running',
}
