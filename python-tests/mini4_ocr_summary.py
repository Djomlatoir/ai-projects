import pytesseract
import requests
from PIL import Image
import sys

# Putanja do Tesseract executablea
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

def summarize_with_llm(text):
    response = requests.post(
        "http://localhost:4000/v1/chat/completions",
        headers={
            "Authorization": "Bearer sk-mojkljuc123",
            "Content-Type": "application/json"
        },
        json={
            "model": "local-llama",
            "messages": [
                {"role": "system", "content": "Ti si asistent koji sažima tekstove. Budi kratak i jasan."},
                {"role": "user", "content": f"Sažmi ovaj tekst u 2-3 rečenice:\n\n{text}"}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "test_image.png"
    
    print("OCR čitanje...")
    tekst = ocr_from_image(image_path)
    print(f"Izvučen tekst:\n{tekst}\n")
    
    print("LLM sažetak...")
    sazetak = summarize_with_llm(tekst)
    print(f"Sažetak:\n{sazetak}")