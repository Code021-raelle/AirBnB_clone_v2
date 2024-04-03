#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

#Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo '<html>
 <head>
 </head>
 <body>
    Holberton School
 </body>
</html>' | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo bash -c 'cat > /etc/nginx/sites-available/hbnb_static << EOF
server {
    listen 80;
    server_name code021.tech;

    location /hbnb_static/ {
    	alias /data/web_static/current/;
	try_files \$uri \$uri/ =404;
    }
}
EOF'

# Enable the site and restart Nginx
sudo ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
sudo systemctl restart nginx

echo "Web servers setup for deployment of web_static is complete."
