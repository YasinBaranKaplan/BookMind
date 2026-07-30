from rag.parser import read_pdf
from rag.chunker import chunk_pages

def main():
    print("Welcome to the BookMind!")
    document = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_pages(
        document.pages,
        source="Nietzsche-Agladiginda.pdf",
    )

    print(f"Toplam sayfa : {len(document.pages)}")
    print(f"Kaynak : {document.source}")
    print(f"Toplam chunk : {len(chunks)}")
    print(f"Toplam kelime : {sum(len(chunk.text.split()) for chunk in chunks)}")
    

    print(chunks[0])
    print(chunks[0].text[:300])




if __name__ =="__main__":
    main()