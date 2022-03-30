from typing import List

from cwr_parser_pack.models.base import EntityBase
from cwr_parser_pack.models.error import Error


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
