from dataclasses import dataclass

class Chunk:
    id:int
    text:str
    source:str
    start_char:int
    end_char:int