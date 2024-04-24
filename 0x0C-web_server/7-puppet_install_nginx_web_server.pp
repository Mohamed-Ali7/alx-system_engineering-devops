# Puppet script to install and configure an Nginx server

package { 'nginx':
ensure          => installed,
provider        => 'apt',
}

file {'/var/www/html/index.html':
ensure  => 'present',
content => 'Hello World!
',
}

$new_content="

server {
        listen 80 default_server;
        listen [::]:80 default_server;
        location /redirect_me {
            return 301 https://www.google.com;
        }

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files  / =404;
        }
}
"

file{ '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $new_content,
}

service { 'nginx':
  ensure => 'running',
}
