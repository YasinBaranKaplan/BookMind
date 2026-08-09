from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

class Embedder:
    def __init__(
        self,
        model_name: str = "BAAI/bge-m3",
    ):
        print("Loading embedding model...")
        self.model = SentenceTransformer(model_name)
        print("Embedding model loaded.")

    def embed_text(self, text: str) -> list[float]:
        return self.model.encode(
            text,
            normalize_embeddings=True,
        ).tolist()

    def embed_chunks(self, chunks):
        for chunk in chunks:
            chunk.embedding = self.embed_text(chunk.text)

        return chunks