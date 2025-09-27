# this file is in our debian server, we took it to local for editing
import os
import sys

# Paths
TEMPLATE_FILE = "nginx_template.conf"
NGINX_SITES_AVAILABLE = "/etc/nginx/sites-available"
NGINX_SITES_ENABLED = "/etc/nginx/sites-enabled"

def create_nginx_config(domain, port):
    # Read the template
    with open(TEMPLATE_FILE, "r") as f:
        template = f.read()

    # Replace placeholders
    config = template.replace("<DOMAIN>", domain).replace("<PORT>", str(port))

    # Save new config file
    config_path = os.path.join(NGINX_SITES_AVAILABLE, domain)
    with open(config_path, "w") as f:
        f.write(config)

    # Create symlink in sites-enabled
    enabled_path = os.path.join(NGINX_SITES_ENABLED, domain)
    if not os.path.exists(enabled_path):
        os.symlink(config_path, enabled_path)

    print(f"✅ Created Nginx config for {domain} on port {port}")
    print(f"   {config_path} → {enabled_path}")
    print("Next steps:")
    print("   sudo nginx -t && sudo systemctl reload nginx")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: sudo python3 create_nginx_config.py <domain> <port>")
        sys.exit(1)

    domain = sys.argv[1]
    port = sys.argv[2]

    create_nginx_config(domain, port)