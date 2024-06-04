# Fixing the extension of a php file from phpp to php

exec { 'replace_phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/local/bin:/bin',
}
