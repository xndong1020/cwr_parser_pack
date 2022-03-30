from typing import List

from cwr_parser_pack.models.base import EntityBase
from cwr_parser_pack.models.error import Error


class Spt(EntityBase):
    errors: List[Error]
    interested_party_number: str
    constant: str
    pr_ownership_share: str
    mr_ownership_share: str
    sr_ownership_share: str
    inclusion_exclusion_indicator: str
    tis_numeric_code: str
    sequence_number: str

    def __init__(self, record_prefix, errors: List[str] = []):
        self.errors = errors
        EntityBase.__init__(self, record_prefix)
