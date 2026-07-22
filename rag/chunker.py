def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200,
):
    chunks = []

    start = 0

    while start < len(text):
        chunk = text[start:start+chunk_size]

        chunks.append(chunk)

        start += chunk_size - overlap
    return chunks