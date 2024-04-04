#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

#Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi

# Create directories if not exist
directories=("/data" "/data/web_static" "/data/web_static/releases" "/data/web_static/shared" "/data/web_static/releases/test")
for dir in "${directories[@]}"; do
	if [ ! -d "$dir" ]; then
		mkdir -P "$dir"
		chown -R ubuntu:ubuntu "$dir"
	fi
done

# Create a fake HTML file for testing
fake_html="/data/web_static/releases/test/index.html"
if [ ! -f "$fake_html" ]; then
	echo "<html>
	<head>
	</head>
	<body>
	  Holberton School
	</body>
</html>" > "$fake_html"
fi

# Create symbolic link
symlink="/data/web_static/current"
if [ -L "$symlink" ]; then
	rm "$symlink"
fi
ln -sf /data/web_static/releases/test/ "$symlink"

# Update nginx configuration
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/ {" "$nginx_config"; then
	sed -i '/server_name _;/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config"
fi

# Restart nginx
sudo service nginx restart

exit 0
