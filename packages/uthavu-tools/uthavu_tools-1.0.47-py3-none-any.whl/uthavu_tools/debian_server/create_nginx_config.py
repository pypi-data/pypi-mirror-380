import os
import sys

# Paths
NGINX_SITES_AVAILABLE = "/etc/nginx/sites-available"
NGINX_SITES_ENABLED = "/etc/nginx/sites-enabled"

# Inline SSL-enabled template
NGINX_TEMPLATE = """
server {
    listen 80;
    server_name {DOMAIN} www.{DOMAIN};

    # Redirect all plain HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name {DOMAIN} www.{DOMAIN};

    ssl_certificate /etc/letsencrypt/live/{DOMAIN}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{DOMAIN}/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://127.0.0.1:{PORT};
        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_buffering off;
    }

    error_page 502 503 504 /50x.html;
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
"""

def create_nginx_config(domain, port):
    """Create nginx config file for given domain and port"""
    config = NGINX_TEMPLATE.replace("{DOMAIN}", domain).replace("{PORT}", str(port))

    # Save new config file
    config_path = os.path.join(NGINX_SITES_AVAILABLE, f"{domain}.conf")
    with open(config_path, "w") as f:
        f.write(config)

    # Create symlink in sites-enabled
    enabled_path = os.path.join(NGINX_SITES_ENABLED, f"{domain}.conf")
    if not os.path.exists(enabled_path):
        os.symlink(config_path, enabled_path)

    print(f"✅ Created SSL-enabled Nginx config for {domain} on port {port}")
    print(f"   {config_path} → {enabled_path}")
    print("Next steps:")
    print("   sudo nginx -t && sudo systemctl reload nginx")
    print("   Then run: sudo certbot --nginx -d {domain} -d www.{domain}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sudo python3 create_nginx_config.py <domain> <port>")
        sys.exit(1)

    domain = sys.argv[1]
    port = sys.argv[2]

    create_nginx_config(domain, port)