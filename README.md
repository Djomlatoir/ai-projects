### Projekt: AI Razvojna Platforma

#### Project Overview

AI razvojna platforma je projekat koji omogućava razmišljanje i izvršavanje različitih AI taksija, kao što su OCR, sintetizacija glasova i slično. Projekt koristi nuklearnu arhitekturu sa Dockerom i n8n integracijom, što omogućava lokalno izvršavanje bez troškova za cloud API.

#### Stack

*   **Docker**: Koristimo Docker kao osnovnu platformu za izvršavanje projekta.
*   **Ollama**: Koristimo Ollamu kao različite AI modelove, kao što su OCR i sintetizacija glasova.
*   **LiteLLM**: Koristimo LiteLLM kao korisničke API za interakciju s različitim AI modelima.
*   **n8n**: Koristimo n8n kao integritorsku platformu za povezivanje različitih taksija i procesa.
*   **Qdrant**: Koristimo Qdrant kao baznu baznu bazu podataka za sačuvanja rezultata i informacije o projektu.
*   **Open WebUI**: Koristimo Open WebUI kao korisničko interfejsu za pristup projektu i njegove funkcionalnosti.
*   **Playwright**: Koristimo Playwright kao browsera za različite web strane.
*   **Tesseract OCR**: Koristimo Tesseract OCR kao OCR tehnologije za scanciranje i analizu tekstualnog sadržaja.
*   **FFmpeg**: Koristimo FFmpeg kao biblioteke za izvršavanje video i audio procesora.
*   **faster-whisper**: Koristimo faster-whisper kao biblioteke za izvršavanje sintetizacije glasova.

#### Project Structure

 Projekt je organiziran u sledeći način:

*   `/outputs/`: Sadržaj koji se izdvaja iz procesa.
*   `python-tests/`: Sadržaj kojeg koristimo za različite testove i provere projekta.

#### How to Run

Da bi se izvršilo projekt, morate slatisi sledeće stepene:

1.  Izvršiti komande `docker-compose up` da biste izveli Docker kontajner.
2.  Pokrenite korisnički interfejs sa `/open-webui/`.
3.  Pokrenite `python-tests/full_pipeline.py` ili sledeće korisničke skripte kako bi se izvršilo različito testovo.

Zbog potrebe za lokalnim izvršavanjem, ova platforma radi bez troškova za cloud API-a.