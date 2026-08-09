from rag.schema import Chunk

class InMemoryVectorStore:
    def __init__(self):
        self.chunks: list[Chunk] = []

    def add_chunks(self, chunks: list[Chunk])-> None:
        self.chunks.extend(chunks)

    def __len__(self):
        return len(self.chunks)