# Puppet script to install and configure an Nginx server

exec { 'update':
  command  => 'apt-get update',
  path     => '/usr/bin/'
}
-> package { 'nginx':
ensure          => installed,
provider        => 'apt',
install_options => ['-y'],
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> service { 'nginx':
  ensure => 'running',
}
