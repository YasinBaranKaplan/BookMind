from rag.parser import read_pdf
from rag.chunker import chunk_text
import rag.embeddings

def main():
    print("Welcome to the BookMind!")
    text = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_text(text)

    print(f"Toplam karakter : {len(text)}")
    print(f"Chunk sayısı    : {len(chunks)}")
    print()

    print("\nİlk Chunk\n")
    print("-" * 80)
    print(chunks[0])
    print("-" * 80)

    print("\nİkinci Chunk\n")
    print("-" * 80)
    print(chunks[1])
    print("-" * 80)



if __name__ =="__main__":
    main()