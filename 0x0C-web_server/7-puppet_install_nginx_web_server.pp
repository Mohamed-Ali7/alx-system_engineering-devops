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

$new_content="location /redirect_me {
            return 301 https://www.google.com;
        }
"

file_line { 'redirection-301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen \[::\]:80 default_server;',
  line   => $new_content,
}

service { 'nginx':
  ensure => 'running',
}
