# Puppet manifest to kill a process "killmenow"
exec { 'killmenow':
command  => 'pkill -f "killmenow"',
path     => '/usr/bin',
provider => shell,

}
