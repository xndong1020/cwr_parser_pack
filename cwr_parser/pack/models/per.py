from dataclasses import dataclass
from typing import List

from ..models.base import EntityBase
from ..models.error import Error


@dataclass
class Per(EntityBase):
    performing_artist_last_name: str
    performing_artist_first_name: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
