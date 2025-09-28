import subprocess
import sys

def run_cmd(cmd):
    """Run a shell command and print output live"""
    print(f"👉 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        sys.exit(result.returncode)

def main():
    if len(sys.argv) < 2:
        print("❌ Usage1: pushmain \"Your commit message here\"")
        sys.exit(1)

    commit_msg = sys.argv[1]

    run_cmd("git add .")
    run_cmd(f'git commit -m "{commit_msg}" || echo \"✅ Nothing to commit\"')
    run_cmd("git push origin main")

    print("\n🚀 Code pushed to main successfully!")
