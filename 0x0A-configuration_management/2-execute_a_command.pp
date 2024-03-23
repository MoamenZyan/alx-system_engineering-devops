# executing command using puppet

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
