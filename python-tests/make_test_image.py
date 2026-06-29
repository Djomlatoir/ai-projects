# Pokreni ovo jednom da napraviš test sliku (sačuvaj kao make_test_image.py)
from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (600, 200), color="white")
draw = ImageDraw.Draw(img)
draw.text((20, 50), "Danas  sam instalirao kompletan AI development stack.\nStack ukljucuje Docker, n8n, LiteLLM, Qdrant i Whisper.\nSvi servisi rade lokalno bez placanja API troskova.", fill="black")
img.save("test_image.png")