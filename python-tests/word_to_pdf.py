import sys
import subprocess
from pathlib import Path

def convert_word_to_pdf(docx_path):
    docx = Path(docx_path)
    if not docx.exists():
        print(f"Fajl ne postoji: {docx_path}")
        return
    
    # Koristi LibreOffice ili Word ako je instaliran
    # Opcija 1 - LibreOffice (besplatno)
    result = subprocess.run([
        "soffice", "--headless", "--convert-to", "pdf",
        "--outdir", str(docx.parent),
        str(docx)
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        pdf_path = docx.with_suffix(".pdf")
        print(f"✔ Konvertovano: {pdf_path}")
    else:
        print(f"Greška: {result.stderr}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else None
    if not path:
        print("Korišćenje: uv run python word_to_pdf.py dokument.docx")
    else:
        convert_word_to_pdf(path)