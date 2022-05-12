from typing import List

from ..models.base import EntityBase
from ..models.error import Error


class Alt(EntityBase):
    alternate_title: str
    title_type: str
    language_code: str

    def __init__(self, record_prefix):
        EntityBase.__init__(self, record_prefix)
