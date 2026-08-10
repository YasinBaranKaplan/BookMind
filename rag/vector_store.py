from rag.schema import Chunk

class InMemoryVectorStore:
    def __init__(self):
        self.chunks: list[Chunk] = []

    def add_chunk(self, chunk: Chunk) -> None:
        self.chunks.append(chunk)

    def add_chunks(self, chunks: list[Chunk])-> None:
        self.chunks.extend(chunks)

    def get_chunks(self) -> list[Chunk]:
        return self.chunks

    def clear(self) -> None:
        self.chunks.clear()

    def __len__(self):
        return len(self.chunks)