from dataclasses import dataclass


@dataclass
class Page:
    number: int
    text: str

@dataclass
class Chunk:
    id: str
    text: str

    source: str

    page_start: int
    page_end: int

    chunk_index: int

@dataclass
class Document:
    source :str
    pages:list[Page]