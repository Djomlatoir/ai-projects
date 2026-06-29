import subprocess
import sys
from pathlib import Path

def git_add_commit_push(repo_path, commit_message):
    repo = Path(repo_path)
    
    def run(cmd):
        result = subprocess.run(cmd, cwd=repo, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Greška: {result.stderr}")
            sys.exit(1)
        print(result.stdout.strip())
        return result
    
    print("git add...")
    run(["git", "add", "."])
    
    print("git commit...")
    run(["git", "commit", "-m", commit_message])
    
    print("git push...")
    run(["git", "push"])
    
    print("✔ Pushovan na GitHub!")

if __name__ == "__main__":
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    message = sys.argv[2] if len(sys.argv) > 2 else "auto: pipeline commit"
    git_add_commit_push(repo_path, message)