import fitz  # pymupdf
import requests
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

# Konfiguracija
COLLECTION_NAME = "dokumenti"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # ~90MB, radi na CPU
LITELLM_URL = "http://localhost:4000/v1/chat/completions"
LITELLM_KEY = "Bearer sk-mojkljuc123"

def ucitaj_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for page in doc:
        tekst = page.get_text().strip()
        if tekst:
            # Podeli stranicu na manje delove (~500 karaktera)
            for i in range(0, len(tekst), 500):
                chunk = tekst[i:i+500].strip()
                if len(chunk) > 50:  # ignorisi kratke delove
                    chunks.append(chunk)
    return chunks

def indeksiraj(chunks, embedder, qdrant):
    # Napravi kolekciju ako ne postoji
    existing = [c.name for c in qdrant.get_collections().collections]
    if COLLECTION_NAME not in existing:
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )
        print(f"Kolekcija '{COLLECTION_NAME}' kreirana.")

    print(f"Pravim embeddings za {len(chunks)} delova...")
    vectors = embedder.encode(chunks, show_progress_bar=True)

    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=v.tolist(),
            payload={"tekst": c}
        )
        for v, c in zip(vectors, chunks)
    ]

    qdrant.upsert(collection_name=COLLECTION_NAME, points=points)
    print(f"✔ {len(points)} delova upisano u Qdrant.")

def pretrazi(upit, embedder, qdrant, top_k=3):
    vektor = embedder.encode([upit])[0].tolist()
    rezultati = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=vektor,
        limit=top_k
    )
    return [r.payload["tekst"] for r in rezultati.points]

def pitaj_llm(upit, kontekst):
    prompt = f"""Na osnovu sledećeg konteksta, odgovori na pitanje.

Kontekst:
{chr(10).join(kontekst)}

Pitanje: {upit}
Odgovor:"""

    r = requests.post(
        LITELLM_URL,
        headers={"Authorization": LITELLM_KEY, "Content-Type": "application/json"},
        json={
            "model": "local-llama",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }
    )
    return r.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    import sys

    pdf_path = sys.argv[1] if len(sys.argv) > 1 else "test.pdf"
    upit = sys.argv[2] if len(sys.argv) > 2 else "O čemu govori ovaj dokument?"

    print("Učitavam embedding model...")
    embedder = SentenceTransformer(EMBEDDING_MODEL)
    qdrant = QdrantClient(host="localhost", port=6333)

    print(f"Čitam PDF: {pdf_path}")
    chunks = ucitaj_pdf(pdf_path)
    print(f"Pronađeno {len(chunks)} delova teksta.")

    indeksiraj(chunks, embedder, qdrant)

    print(f"\nPitanje: {upit}")
    kontekst = pretrazi(upit, embedder, qdrant)
    odgovor = pitaj_llm(upit, kontekst)
    print(f"\nOdgovor:\n{odgovor}")