import fitz

from rag.schema import Page


def read_pdf(pdf_path: str) -> list[Page]:

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

    return pages