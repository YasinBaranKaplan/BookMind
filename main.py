from rag.parser import read_pdf
from rag.chunker import chunk_text
import rag.embeddings

def main():
    print("Welcome to the BookMind!")
    pages = read_pdf("books/ Nietzsche-Agladiginda.pdf")

    print(f"Toplam sayfa: {len(pages)}")
    print(pages[0].number)

    for page in pages[:5]:
        print(f"Sayfa {page.number}")
        print(repr(page.text[:100]))
        print("-" * 40)



if __name__ =="__main__":
    main()