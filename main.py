from rag.parser import read_pdf
from rag.chunker import chunk_document

def main():
    print("Welcome to the BookMind!")
    document = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_document(document)

    print(f"Toplam chunk: {len(chunks)}\n")

    print(chunks[0],"\n")

    print(chunks[1])

  




if __name__ =="__main__":
    main()