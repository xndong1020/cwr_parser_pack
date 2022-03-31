from dataclasses import dataclass
from email.policy import default
import json


@dataclass
class Error:
    message: str
    level: str

    def __init__(self, message: str, level: str) -> None:
        self.message = message
        self.level = level

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
