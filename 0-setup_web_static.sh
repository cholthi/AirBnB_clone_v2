#!/usr/bin/env bash
# prepares a server for static website deployment

# setup nginx webserver
apt-get update -y
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html><head>
      <title>Hello World</title>
      </head>
      <body>
      <h1>Hello World</h1>
      </body>
      </html>" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '12 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'  /etc/nginx/sites-enabled/default
service nginx restart

