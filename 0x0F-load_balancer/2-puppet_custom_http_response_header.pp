# Puppet script to install and configure an Nginx server

exec { 'update':
  command => 'apt-get -y update',
  path    => '/usr/bin/',
}

package { 'nginx':
ensure          => installed,
provider        => 'apt',
install_options => ['-y'],
}

$after_line='listen \[::\]:80 default_server;'
$new_header="add_header X-Served-By \$hostname;"
$file='/home/mohamed/alx_projects/alx-system_engineering-devops/0x0F-load_balancer/default'

exec { 'Add header':
  command => "sed -i '/${after_line}/a\ \t${new_header}' ${file}",
  path    => '/usr/bin',
  unless  => "grep -q '${new_header}' '${file}'",
}

service { 'nginx':
  ensure => 'running',
}
