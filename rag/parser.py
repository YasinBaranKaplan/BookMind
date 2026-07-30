import fitz

from rag.schema import Page,Document


def read_pdf(pdf_path: str) -> Document:

    document = fitz.open(pdf_path)

    pages = []

    for page in document:

        page_text = page.get_text()

        pages.append(
            Page(
                number=page.number + 1,
                text=page_text
            )
        )

    return Document(
        source=pdf_path,
        pages=pages
    )