from rag.parser import read_pdf
from rag.chunker import chunk_document
from rag.embeddings import Embedder
from rag.vector_store import InMemoryVectorStore
from rag.retriever import Retriever


def main():
    print("Welcome to BookMind!")

    document = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_document(document)
    print(f"Toplam chunk: {len(chunks)}")

    embedder = Embedder()

    chunks = embedder.embed_chunks(chunks)

    store = InMemoryVectorStore()

    store.add_chunks(chunks)

    query = "Nietzsche neden yalnızdı?"

    query_embedding = embedder.embed_text(query)

    retriever = Retriever(store)

    results = retriever.retrieve(query_embedding, top_k=5)

    for chunk, score in results:
        print(f"Score: {score:.4f}")
        print(f"Pages: {chunk.page_start}-{chunk.page_end}")
        print(chunk.text)
        print("-" * 50)

    for chunk in results:
        print(chunk.page_start, chunk.page_end)
        print(chunk.text)
        print("-" * 50)


if __name__ == "__main__":
    main()