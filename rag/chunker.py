from uuid import uuid4
from rag.schema import Chunk,Page

def chunk_pages(
    pages: list[Page],
    source: str,
) -> list[Chunk]:

    chunks = []

    for index, page in enumerate(pages):

        chunk = Chunk(
            id=str(uuid4()),
            text=page.text,

            source=source,

            page_start=page.number,
            page_end=page.number,

            chunk_index=index,
        )

        chunks.append(chunk)

    return chunks