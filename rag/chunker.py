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

        previous_start = start

        candidate_end = min(start + chunk_size, len(full_text))

        split_end = full_text.rfind(" ", start, candidate_end)

        if split_end == -1:
            split_end = candidate_end

        chunk_text = full_text[start:split_end]

        page_start = 1
        page_end = len(document.pages)

        for i, offset in enumerate(page_offsets):
            if offset <= start:
                page_start = i + 1
            if offset <= split_end:
                page_end = i + 1

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

        # Bir sonraki chunk'ın başlangıcını overlap kadar geri al
        next_start = max(0, split_end - overlap)

        # Overlap bölgesi içinde ilk boşluğu bul
        space_index = full_text.find(" ", next_start, split_end)

        if space_index != -1:
            start = space_index + 1
        else:
            start = next_start

        # Güvenlik: başlangıç ilerlemediyse sonsuz döngüyü engelle
        if start <= previous_start:
            start = split_end
        
        

        chunk_index += 1

    return chunks