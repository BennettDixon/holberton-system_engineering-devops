#!/usr/bin/env bash
# script to install and setup nginx
CONFIG_FILE="/etc/nginx/sites-available/default"
HOST_NAME=$(hostname)
MY_ID=496

# check if hostname is correct
if [[ $(hostname) =~ ^$MY_ID-web-[0-9]+ ]]; then
    echo 'hostname properly configured'
else
    (>&2 echo 'hostname not configured properly...')
    (>&2 echo 'please set hostname to pattern: 496-web-<server_id>...')
    (>&2 echo 'Example: sudo hostnamectl set-hostname 496-web-<insert_server_id_here>')
fi

# install nginx
apt-get -y update
apt-get -y install nginx

# update index.html file
echo 'Holberton School' > /usr/share/nginx/html/index.html
echo "Ceci n'est pas une page" > /usr/share/nginx/html/404.html

# update config file to redirect
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /usr/share/nginx/html;
    index  index.html index.htm;

    add_header X-Served-By $HOST_NAME;

    location /redirect_me {
        return 301 http://google.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
}" > $CONFIG_FILE

# start nginx after reloading config
service nginx start
# if nginx was already running restart it
service nginx restart
