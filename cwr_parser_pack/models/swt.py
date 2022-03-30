from typing import List

from cwr_parser_pack.models.base import EntityBase
from cwr_parser_pack.models.error import Error


class Swt(EntityBase):
    errors: List[Error]
    interested_party_number: str
    pr_collection_share: str
    mr_collection_share: str
    sr_collection_share: str
    inclusion_exclusion_indicator: str
    tis_numeric_code: str
    sequence_number: str

    def __init__(self, record_prefix, errors: List[str] = []):
        self.errors = errors
        EntityBase.__init__(self, record_prefix)
