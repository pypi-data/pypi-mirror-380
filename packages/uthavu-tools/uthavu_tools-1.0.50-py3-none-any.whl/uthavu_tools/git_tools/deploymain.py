import subprocess
import sys

def run_cmd(cmd, check=True):
    """Run a shell command and print output live"""
    print(f"👉 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=not check)
    if check and result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        sys.exit(result.returncode)
    return result.stdout.strip() if result.stdout else None

def get_current_branch():
    """Get the current Git branch name"""
    return run_cmd("git rev-parse --abbrev-ref HEAD", check=False)

def main():
    if len(sys.argv) < 2:
        print("❌ Usage: deploymain \"Your commit message here\"")
        sys.exit(1)

    commit_msg = sys.argv[1]

    # ✅ Safety check: must start on dev branch
    current_branch = get_current_branch()
    if current_branch != "dev":
        print(f"❌ You are on branch '{current_branch}', not 'dev'.")
        print("   Please checkout dev branch before running this command.")
        sys.exit(1)

    # Step 1: git add .
    run_cmd("git add .")

    # Step 2: git commit with custom message
    run_cmd(f'git commit -m "{commit_msg}" || echo \"✅ Nothing to commit\"')

    # Step 3: switch to main
    run_cmd("git checkout main")

    # Step 4: merge dev into main
    run_cmd("git merge dev")

    # Step 5: push main
    run_cmd("git push origin main")

    # Step 6: switch back to dev
    run_cmd("git checkout dev")

    print("\n🚀 Deployment pushed to main successfully, back on dev branch!")

if __name__ == "__main__":
    main()
