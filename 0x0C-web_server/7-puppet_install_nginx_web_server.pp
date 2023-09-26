# Configure Nginx to listen on port 80
class nginx::config {
  package { 'nginx': ensure => present }

  service { 'nginx':
    ensure => running,
    enabled => true,
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => present,
    owner => 'root',
    group => 'root',
    mode => '0644',
    content => template('nginx/default.conf'),
  }
}

# Create a simple HTML file
file { '/var/www/html/index.html':
  ensure => present,
  content => 'Hello World!',
  owner => 'root',
  group => 'root',
  mode => '0644',
}

# Redirect /redirect_me to /
nginx::vhost { 'redirect_me':
  ensure => present,
  server_name => 'localhost',
  location => '/redirect_me',
  rewrite => { '^/$ permanent', },
}
