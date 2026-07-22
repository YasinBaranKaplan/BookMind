import fitz


def read_pdf(pdf_path: str) -> str:
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        page_text = page.get_text()
        text += page_text

    return text