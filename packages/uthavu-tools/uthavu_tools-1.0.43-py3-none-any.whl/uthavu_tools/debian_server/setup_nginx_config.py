import subprocess
import sys

# Server details
HOST = "72.60.97.244"   # e.g. 192.168.1.10 or domain
USER = "root"           # e.g. root, debian, jawahar
REMOTE_SCRIPT = "/etc/nginx/sites-available/create_nginx_config.py"  # Path on server

def run_remote(cmd):
    """Run a remote SSH command and return exit code"""
    full_cmd = f"ssh {USER}@{HOST} {cmd}"
    print(f"👉 Running on {HOST}: {full_cmd}")
    result = subprocess.run(full_cmd, shell=True, text=True)
    return result.returncode

def main():
    print("🌐 Remote Nginx Config Generator")

    # Ask for inputs
    domain = input("👉 Enter domain name (e.g. example.com): ").strip()
    port = input("👉 Enter port number (e.g. 8080): ").strip()

    if not domain or not port.isdigit():
        print("❌ Invalid input. Please provide a domain and numeric port.")
        sys.exit(1)

    # Build SSH command
   # Step 1: Run the remote config generator script
    cmd = f"sudo python3 {REMOTE_SCRIPT} {domain} {port}"
    if run_remote(cmd) != 0:
        print("❌ Remote config script failed.")
        sys.exit(1)
    
    # Step 2: Test nginx configuration
    if run_remote("sudo nginx -t") != 0:
        print("❌ Nginx configuration test failed. Not reloading.")
        sys.exit(1)

    # Step 3: Reload nginx
    if run_remote("sudo systemctl reload nginx") != 0:
        print("❌ Failed to reload Nginx.")
        sys.exit(1)

    print("✅ Nginx reloaded successfully 🚀")

if __name__ == "__main__":
    main()