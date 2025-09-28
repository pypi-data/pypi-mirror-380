def main():
    tools = {
        "checkbranch": "Checks and shows the current Git branch.",
        "checkin": "Adds, commits with a message, and pushes changes to the current branch.",
        "cleanup": "Cleans up workspace (removes __pycache__, dist/, build/, .pytest_cache, etc.).",
        "deploymain": "Commits changes in dev, merges into main, pushes main, then switches back to dev.",
        "pushmain": "Quick utility: commit & push code directly to the main branch.",
        "releasetool": "Full release automation: bumps version, builds package, uploads to PyPI."
    }

    print("\n📦 Available uthavu-tools:\n")
    for tool, desc in tools.items():
        print(f"  🔹 {tool:<12} → {desc}")
    print("\n✅ Run any tool by typing its name in your terminal (e.g., `checkin \"msg\"`).\n")

if __name__ == "__main__":
    main()
