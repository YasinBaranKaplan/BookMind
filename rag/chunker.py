from uuid import uuid4

from rag.schema import Document, Chunk


def find_split_end(text: str, start: int, candidate_end: int) -> int:
    """
    Chunk sonunu belirler.

    Öncelik sırası:
    1. Candidate_end'den sonraki en yakın cümle sonu (maksimum 150 karakter)
    2. Candidate_end'den önceki en yakın cümle sonu
    3. Candidate_end'den önceki en yakın boşluk
    4. Hard cut (candidate_end)
    """

    sentence_endings = ".!?"

    if candidate_end >= len(text):
        return len(text)

    # En fazla 150 karakter ileri bak
    forward_limit = min(candidate_end + 150, len(text) - 1)

    for i in range(candidate_end, forward_limit + 1):
        if text[i] in sentence_endings:
            return i + 1

    # Geriye doğru cümle sonu ara
    for i in range(candidate_end, start, -1):
        if text[i] in sentence_endings:
            return i + 1

    # Kelime sonuna düş
    word_end = text.rfind(" ", start, candidate_end)
    if word_end != -1:
        return word_end

    # Son çare
    return candidate_end


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

        if candidate_end == len(full_text):
            split_end = len(full_text)
        else:
            split_end = find_split_end(
                full_text,
                start,
                candidate_end,
            )

        chunk_text = full_text[start:split_end].strip()

        if not chunk_text:
            break

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

        # Overlap başlangıcı
        next_start = max(0, split_end - overlap)

        # Kelime başından başlamaya çalış
        space_index = full_text.find(" ", next_start, split_end)

        if space_index != -1:
            start = space_index + 1
        else:
            start = next_start

        # Sonsuz döngü koruması
        if start <= previous_start:
            start = split_end

        chunk_index += 1

    return chunks