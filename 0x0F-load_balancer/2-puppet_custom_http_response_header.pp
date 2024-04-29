# Puppet script to install and configure an Nginx server

exec { 'update':
  command  => '/urs/bin/apt-get -y update',
}

package { 'nginx':
ensure          => installed,
provider        => 'apt',
}

$new_header="\tadd_header X-Served-By ${hostname};"

file_line { 'add_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen \[::\]:80 default_server;',
  line   => $new_header,
}

service { 'nginx':
  ensure => 'running',
}
