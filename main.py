from rag.parser import read_pdf
from rag.chunker import chunk_document
from rag.embeddings import Embedder
from rag.vector_store import InMemoryVectorStore


def main():
    print("Welcome to BookMind!")

    document = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_document(document)
    print(f"Toplam chunk: {len(chunks)}")

    embedder = Embedder()
    chunks = embedder.embed_chunks(chunks)

    print(f"İlk chunk embedding boyutu: {len(chunks[0].embedding)}")

    store = InMemoryVectorStore()
    store.add_chunks(chunks)

    print(f"Vector Store Chunk Sayısı: {len(store)}")


if __name__ == "__main__":
    main()