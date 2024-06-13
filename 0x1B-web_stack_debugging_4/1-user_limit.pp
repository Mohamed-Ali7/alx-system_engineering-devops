# Change the number of the files that a user is allowed to open.

# Increase limit of the files that a user can open.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i -E "s/holberton hard nofile [0-9]+/holberton hard nofile 4000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase limit of the files that a user can set.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i -E "s/holberton soft nofile [0-9]+/holberton hard nofile 4000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}