from uuid import uuid4

from rag.schema import Document, Chunk


def chunk_document(
    document: Document,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[Chunk]:

    full_text = ""
    page_offsets = []

    for page in document.pages:
        page_offsets.append(len(full_text))
        full_text += page.text

    chunks = []

    start = 0
    chunk_index = 0

    while start < len(full_text):

        end = min(start + chunk_size, len(full_text))

        chunk_text = full_text[start:end]

        # page_start hesapla
        page_start = 1
        for i, offset in enumerate(page_offsets):
            if offset <= start:
                page_start = i + 1
            else:
                break

        # page_end hesapla
        page_end = page_start
        for i, offset in enumerate(page_offsets):
            if offset <= end:
                page_end = i + 1
            else:
                break

        chunks.append(
            Chunk(
                id=str(uuid4()),
                text=chunk_text,
                source=document.source,
                page_start=page_start,
                page_end=page_end,
                chunk_index=chunk_index,
            )
        )

        chunk_index += 1
        start += chunk_size - overlap

    return chunks