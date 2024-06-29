#killmenow
exec { 'killmenow':
    commmand => 'pkill',
    onlyif   => '/usr/bin/pgrep -f killmenow',
    }
