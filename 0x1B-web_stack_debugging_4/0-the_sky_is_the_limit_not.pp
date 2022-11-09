# Sky is the limit, let's bring that limit higher
exec { 'fix--for-nginx':
  environment => ['DIR=/etc/default/nginx',
                  'OLD=ULIMIT="-n 15"',
                  'NEW=ULIMIT="-n 15000"'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR; sudo service nginx restart',
  path        => ['/usr/bin', '/bin'],
  returns     => [0, 1]
}
