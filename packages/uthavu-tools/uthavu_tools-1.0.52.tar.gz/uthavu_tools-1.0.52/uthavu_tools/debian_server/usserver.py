import subprocess
import socket
import sys

# Server details (for remote use)
HOST = "72.60.97.244"   # Your server IP
USER = "root"           # Your server user (root/debian/etc)

# Detect if script is already inside the Debian server
def is_local_server():
    try:
        # Get current hostname/IP
        host_ip = socket.gethostbyname(socket.gethostname())
        # If this matches your VPS IP → we are inside the server
        return host_ip == HOST
    except Exception:
        return False

def run_remote(cmd):
    """Run command locally if inside server, else via SSH"""
    if is_local_server():
        full_cmd = cmd
    else:
        full_cmd = f"ssh {USER}@{HOST} '{cmd}'"

    print(f"👉 Running: {full_cmd}")
    result = subprocess.run(full_cmd, shell=True, text=True)
    return result.returncode

def main():
    if len(sys.argv) < 2:
        print("Usage: usserver <command>")
        print("Available commands: check, reload, restart, logs")
        sys.exit(1)

    action = sys.argv[1]

    if action == "check":
        run_remote("sudo nginx -t")

    elif action == "reload":
        run_remote("sudo systemctl reload nginx")

    elif action == "restart":
        run_remote("sudo systemctl restart nginx")

    elif action == "logs":
        run_remote("sudo tail -n 50 /var/log/nginx/error.log")

    else:
        print(f"❌ Unknown command: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
