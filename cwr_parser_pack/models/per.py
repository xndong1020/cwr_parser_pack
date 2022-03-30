from typing import List

from cwr_parser_pack.models.base import EntityBase
from cwr_parser_pack.models.error import Error


class Per(EntityBase):
    errors: List[Error]
    performing_artist_last_name: str
    performing_artist_first_name: str
    

    def __init__(self, record_prefix, errors: List[str] = []):
        self.errors = errors
        EntityBase.__init__(self, record_prefix)