import subprocess
import sys
import requests
import pytesseract
from PIL import Image
from pathlib import Path
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr(image_path):
    return pytesseract.image_to_string(Image.open(image_path)).strip()

def summarize(text):
    r = requests.post(
        "http://localhost:4000/v1/chat/completions",
        headers={"Authorization": "Bearer sk-mojkljuc123", "Content-Type": "application/json"},
        json={
            "model": "local-llama",
            "messages": [
                {"role": "system", "content": "Sažmi tekst u 2-3 rečenice."},
                {"role": "user", "content": text}
            ]
        }
    )
    return r.json()["choices"][0]["message"]["content"]

def git_push(repo_path, message):
    for cmd in [["git", "add", "."], ["git", "commit", "-m", message], ["git", "push"]]:
        subprocess.run(cmd, cwd=repo_path, check=True)

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "test_image.png"
    repo_path = sys.argv[2] if len(sys.argv) > 2 else "C:\\AI-Projects"

    print("1. OCR...")
    tekst = ocr(image_path)
    print(f"Tekst: {tekst[:100]}...")

    print("2. LLM sažetak...")
    sazetak = summarize(tekst)
    print(f"Sažetak: {sazetak}")

    # Sačuvaj rezultat u fajl u repo-u
    output = Path(repo_path) / "outputs" / f"summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    output.parent.mkdir(exist_ok=True)
    output.write_text(f"ORIGINAL:\n{tekst}\n\nSAŽETAK:\n{sazetak}", encoding="utf-8")
    print(f"3. Sačuvano u {output}")

    print("4. Git push...")
    git_push(repo_path, f"auto: OCR summary {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("✔ Gotovo!")