from dataclasses import dataclass
from typing import List

from ..models.base import EntityBase
from ..models.error import Error


@dataclass
class Rec(EntityBase):
    errors: List[Error]
    first_release_date: str
    constant: str
    first_release_duration: str
    duration_constant: str
    first_album_title: str
    first_album_label: str
    first_release_catalog_number: str
    ean: str
    recording_technique: str
    media_type: str

    def __init__(self, record_prefix, errors: List[str] = []):
        self.errors = errors
        EntityBase.__init__(self, record_prefix)

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, new_value):
        setattr(self, key, new_value)
