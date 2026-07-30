from rag.parser import read_pdf
from rag.chunker import chunk_pages

def main():
    print("Welcome to the BookMind!")
    pages = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    chunks = chunk_pages(
        pages,
        source="Nietzsche-Agladiginda.pdf",
    )

    print(f"Toplam sayfa : {len(pages)}")
    print(f"Toplam chunk : {len(chunks)}")

    print(chunks[0])
    print(chunks[0].text[:300])




if __name__ =="__main__":
    main()