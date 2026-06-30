**Project Overview**
=====================

LiteLLM AI Development Stack Projekat je lokalni projekat koji koristi Docker i n8n za automatsku implementaciju različitih faza razvoja aplikacija. Prosjecno, ovaj projekat omogućava korisnicima da kreiraju, testiraju i pobacuju AI modelove uz pomoć LiteLLM-a, kao što su uključene oznaka reci (OCR), prepoznaji gole (whisper) i analiza slike (image).

 Projekat koristi FFmpeg za procesiranje videa i Tesseract OCR za raznostu slike. Playwright se koristi za automatizirani testiranje web aplikacija, a Open WebUI daje mogućnost korisnicima da pristupaju interaktivnom pokrovima. Qdrant koriste kao odgovorno uklopno sistema koji omogućava korisnicima da pristupaju i izvode rezultate različitih testova.

 Projekat je dizajniran za lokalnu radnju, što znači da korisnici ne moraju plačati nula-troškove za procesiranje podataka. Uz pomoć Docker-a i n8n-a, ovaj projekat omogućava korisnicima da kreiraju i implementiraju različite faze razvoja AI modela uključujući treniranje, testiranje i pobacivanje.

**Stack**
---------

*   Docker
*   LiteLLM
*   n8n
*   Qdrant
*   Open WebUI
*   Playwright
*   Tesseract OCR
*   FFmpeg
*   faster-whisper

**Project Structure**
=====================

Projekat je organiziran u sledeći način:

| Sekcija | Fajlovi |
| :------------------------------------- | :--------------------------------- |
| `outputs`                                 | `.gitkeep`                           |
| `python-tests`                            | `.gitignore`, `.python-version`, `pyproject.toml`, `uv.lock` |
|                                                    | `generate_readme.py`, `git_pipeline.py`, `full_pipeline.py`, `main.py`, `make_test_image.py`, `mini4_ocr_summary.py`, `test.wav`, `test_image.png`, `test_playwright.py`, `test_real.wav`, `test_whisper.py` |
| `file-organizer`                          | Nije uključen u ovaj projekat                           |

**How to Run**
================

1.  **Pridrijedi projekat na localni komponent**: Pritisni "Git clone" i pridržite link na GitHubu.
2.  **Instaliraj potrebne dependencies**: Korišćenje komande `docker-compose up -d` ili `n8n start`.
3.  **Kreiraj novi projekat u n8n**: Pritisni `New node` i unesi URL `http://localhost:9000/n8n` u polje `Webhook`.
4.  **Pobaci različite faze razvoja AI modela**: Pokrenite komandu `python-tests/full_pipeline.py` ili `python-tests/generate_readme.py`.
5.  **Proveri rezultate i implementiraj novu fazu razvoja**: Pokrenite komandu `python-tests/git_pipeline.py` ili `python-tests/mini4_ocr_summary.py`.

Ukoliko imate neka pitanja ili potrebno pomoć, slobodan se kontaktira na [GitHub](https://github.com/user/litellm-ai-development-stack).