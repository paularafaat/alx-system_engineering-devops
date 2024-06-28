# This Puppet manifest ensures the creation of a file with specific attributes.
file { '/tmp/school':
    ensure  => 'file',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
