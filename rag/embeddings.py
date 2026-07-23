from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("BAAI/bge-m3")

print("Embedding model loaded.")