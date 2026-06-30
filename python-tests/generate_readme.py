import requests
import subprocess
from pathlib import Path

def get_repo_structure():
    """Uzima strukturu fajlova iz repoa"""
    result = subprocess.run(
        ["git", "ls-files"], 
        cwd="C:\\AI-Projects",
        capture_output=True, text=True
    )
    return result.stdout.strip()

def generate_readme(structure):
    response = requests.post(
        "http://localhost:4000/v1/chat/completions",
        headers={
            "Authorization": "Bearer sk-mojkljuc123",
            "Content-Type": "application/json"
        },
        json={
            "model": "local-llama",
            "messages": [
                {
                    "role": "system",
                    "content": "Ti si tehnički pisac. Pišeš README.md fajlove za GitHub projekte. Koristi Markdown format sa sekcijama: Project Overview, Stack, Project Structure, How to Run."
                },
                {
                    "role": "user",
                    "content": f"Napiši README.md za AI development stack projekat koji ima sledeće fajlove:\n\n{structure}\n\nStack uključuje: Docker, Ollama, LiteLLM, n8n, Qdrant, Open WebUI, Playwright, Tesseract OCR, FFmpeg, faster-whisper. Sve radi lokalno bez cloud API troškova."
                }
            ],
            "max_tokens": 1000
        }
    )
    return response.json()["choices"][0]["message"]["content"]

def git_commit_push(content):
    readme_path = Path("C:\\AI-Projects\\README.md")
    readme_path.write_text(content, encoding="utf-8")
    
    subprocess.run(["git", "add", "README.md"], cwd="C:\\AI-Projects", check=True)
    subprocess.run(["git", "commit", "-m", "docs: auto-generisan README kroz lokalni LLM"], cwd="C:\\AI-Projects", check=True)
    subprocess.run(["git", "push"], cwd="C:\\AI-Projects", check=True)
    print("✔ README pushovan na branch!")

if __name__ == "__main__":
    print("1. Čitam strukturu repoa...")
    structure = get_repo_structure()
    print(structure)
    
    print("\n2. Generišem README kroz LiteLLM...")
    readme = generate_readme(structure)
    print(readme)
    
    print("\n3. Commit i push na feature branch...")
    git_commit_push(readme)