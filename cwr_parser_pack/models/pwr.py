from typing import List

from cwr_parser_pack.models.base import EntityBase
from cwr_parser_pack.models.error import Error


class Pwr(EntityBase):
    errors: List[Error]
    publisher_ip_number: str
    publisher_name: str
    submitter_agreement_number: str
    society_assigned_agreement_number: str
    writer_ip_number: str

    def __init__(self, record_prefix, errors: List[str] = []):
        self.errors = errors
        EntityBase.__init__(self, record_prefix)
