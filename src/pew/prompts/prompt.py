from dataclasses import dataclass

@dataclass
class Prompt:
    name: str
    contents: str
    description: str