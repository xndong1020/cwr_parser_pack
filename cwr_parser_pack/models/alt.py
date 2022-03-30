from typing import List

from cwr_parser_pack.models.base import EntityBase
from cwr_parser_pack.models.error import Error


class Alt(EntityBase):
    errors: List[Error]
    alternate_title: str
    title_type: str
    language_code: str

    def __init__(self, record_prefix, errors: List[str] = []):
        self.errors = errors
        EntityBase.__init__(self, record_prefix)
