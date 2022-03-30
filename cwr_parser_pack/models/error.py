from dataclasses import dataclass


@dataclass
class Error:
    message: str
    level: str

    def __init__(self, message: str, level: str) -> None:
        self.message = message
        self.level = level
