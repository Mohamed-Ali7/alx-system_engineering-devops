# Puppet script to install and configure an Nginx server

package { 'nginx':
ensure          => installed,
provider        => 'apt',
install_options => ['-y'],
}

file {'index.html':
ensure  => 'present',
path    => '/var/index.html',
content => 'Hello World!',
mode    => '0644',
}

$new_content="location /redirect_me {
            return 301 https://www.google.com;
        }
"

file_line { '/etc/nginx/sites-available/default':
  ensure => 'present',
  after  => 'listen [::]:80 default_server;',
  line   => $new_content,
}
