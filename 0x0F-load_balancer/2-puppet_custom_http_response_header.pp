# automate the task of creating a custom HTTP header response, but with Puppet
# Define an exec resource to update the package list using 'apt-get update'.
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
->
# Define a package resource to ensure Nginx is present.
package {'nginx':
  ensure => present,
}
->
# Define a file_line resource to add a custom line to the Nginx configuration file.
file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "    location / {
    add_header X-Served-By ${hostname};",  # Add a custom header to the Nginx configuration
  match  => '^\tlocation / {',
}
->
# Define another exec resource to restart the Nginx service.
exec { 'restart the service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
