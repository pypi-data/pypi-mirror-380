import subprocess
import sys
import os

# ==============================
# CONFIG
# ==============================
HOST = "dev2.kleer.ai"
USER = "debian"
IMAGE_NAME = "kleer_front"
LOCAL_TAG = "v9.4"    # local build tag
REMOTE_TAG = "v9.4"   # remote deploy tag
REGISTRY = "registry.gitlab.com/kleer-tech/kleer_front"

def run(cmd, cwd=None):
    """Run a shell command and stream output"""
    print(f"👉 Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        sys.exit(result.returncode)

def main():
    print("🚀 Deploy Kleer Frontend")

    # Step 1: Build docker image locally
    run(f"docker build --no-cache -t {IMAGE_NAME}:{LOCAL_TAG} .")

    # Step 2: Tag for GitLab registry
    run(f"docker tag {IMAGE_NAME}:{LOCAL_TAG} {REGISTRY}:{REMOTE_TAG}")

    # Step 3: Push to GitLab registry
    run(f"docker push {REGISTRY}:{REMOTE_TAG}")

    # Step 4: SSH into server and restart services
    ssh_cmd = f"""
        cd system/ && \
        docker compose restart webserver && \
        docker compose up -d kleer_front && \
        docker stop kleer-front || true && \
        docker rm kleer-front || true && \
        docker run -d --name kleer-front -p 3000:3000 {REGISTRY}:{REMOTE_TAG}
    """
    run(f'ssh {USER}@{HOST} "{ssh_cmd}"')

    print("✅ Deployment complete!")

if __name__ == "__main__":
    main()
