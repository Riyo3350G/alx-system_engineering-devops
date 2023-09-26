# Install The Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is enabled & running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80 and set the default page HTML
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    root /var/www/html;
    index index.html;
    location / {
        echo 'Hello World!';
    }
    location /redirect_me {
        return 301 http://www.example.com;
    }
  }",
  notify  => Service['nginx'],
  require => Package['nginx'],
}

# Create the document root directory
file { '/var/www/html':
  ensure => directory,
}

# Create a simple index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => File['/var/www/html'],
}
