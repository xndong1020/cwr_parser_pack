from dataclasses import dataclass
from typing import List

from models.base import EntityBase


@dataclass
class Xrf(EntityBase):
    organisation_code: str
    identifier: str
    identifier_type: str
    identifier_validity: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
