from rag.parser import read_pdf
from rag.chunker import chunk_document
from rag.embeddings import Embedder

def main():
    print("Welcome to BookMind!")

    document = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_document(document)

    print(f"Toplam chunk: {len(chunks)}")

    embedder = Embedder()

    chunks = embedder.embed_chunks(chunks)

    print(f"\nİlk chunk embedding boyutu: {len(chunks[0].embedding)}")

    print("\nİlk 5 embedding değeri:")
    print(chunks[0].embedding[:5])



if __name__ =="__main__":
    main()