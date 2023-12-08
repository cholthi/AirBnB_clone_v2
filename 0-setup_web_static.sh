#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
#create folders if not exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#create html file
sudo touch /data/web_static/releases/test/index.html
html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
sudo echo "$html" | sudo tee /data/web_static/releases/test/index.html

#create simlink
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
#give ownership of data folder
sudo chown -R ubuntu:ubuntu /data/

#configure nginx
str="listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}"
sudo sed -i '/$str' /etc/nginx/sites-enabled/default
sudo service nginx restart
