# fix nginx limit file

exec { 'default-edit':
        onlyif   => 'test -e /etc/default/nginx',
        command  => 'sudo sed -i "5s/[0-9]\+/4096/" /etc/default/nginx; service nginx restart',
        provider => shell,
}