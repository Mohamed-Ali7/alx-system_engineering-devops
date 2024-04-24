# Puppet script to install and configure an Nginx server

package { 'nginx':
ensure          => installed,
provider        => 'apt',
install_options => ['-y'],
}

file {'/var/www/html/index.html':
ensure  => 'present',
content => 'Hello World!
',
}

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure => 'running',
}
