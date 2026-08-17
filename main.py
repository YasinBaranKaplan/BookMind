from rag.parser import read_pdf
from rag.chunker import chunk_document
from rag.embeddings import Embedder
from rag.vector_store import InMemoryVectorStore
from rag.retriever import Retriever
from rag.generator import Generator


def main():
    print("Welcome to BookMind!")

    print("Welcome to BookMind!")

    document = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_document(document)

    print(f"Toplam chunk: {len(chunks)}")

    embedder = Embedder()

    chunks = embedder.embed_chunks(chunks)

    store = InMemoryVectorStore()
    store.add_chunks(chunks)

    retriever = Retriever(store)
    generator = Generator()


    query = "Nietzsche'nin python  programlama dili hakkındaki düşünceleri nelerdir?"

    query_embedding = embedder.embed_text(query)

    results = retriever.retrieve(
        query_embedding,
        top_k=5,
    )

    context = "\n\n".join(
        chunk.text
        for chunk in results
    )


    prompt = f"""
    Sen bir kitap analiz asistanısın.

    Aşağıdaki kitap parçalarını kullanarak soruyu cevapla.

    Kurallar:
    - Cevabını yalnızca verilen context'e dayandır.
    - Context'te cevap bulunmuyorsa bunu açıkça belirt.
    - Kendi genel bilgini kullanarak bilgi ekleme.

    CONTEXT:
    {context}

    QUESTION:
    {query}

    ANSWER:
    """


    answer = generator.generate(prompt)

    print("\n--- ANSWER ---")
    print(answer)

if __name__ == "__main__":
    main()