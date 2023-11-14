# Enable the user holberton to login and open files without error.

# Increase hard file
exec { 'increase-hard-file-limits':
  command  => 'sudo sed -i "/holberton hard/s/5/4096/" /etc/security/limits.conf',
  provider => shell
}

# Increase soft file limit
exec { 'increase-soft-file-limits':
  command  => 'sudo sed -i "/holberton soft/s/4/4096/" /etc/security/limits.conf',
  provider => shell
}