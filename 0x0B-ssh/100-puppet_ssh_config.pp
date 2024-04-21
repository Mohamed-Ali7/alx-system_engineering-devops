# Puppet script to make
# A ~/.ssh/config file that makes the SSH client
# to use the private key ~/.ssh/school and forbids authenticate using a password

exec { 'append_to_file':
  command =>
  'echo "Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin',
}
